#!/usr/bin/env python3
"""Standalone stdlib wiki Git synchronizer. Run: wiki_sync.py start|finalize."""
from __future__ import annotations
import datetime as dt
import fcntl
import fnmatch
import json
import os
import pathlib
import posixpath
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(os.environ.get("WIKI_ROOT", "")).expanduser()
REMOTE = os.environ.get("WIKI_REMOTE", "origin")
BRANCH = os.environ.get("WIKI_BRANCH", "main")
AUTOPUSH = os.environ.get("WIKI_AUTOPUSH", "true").lower() in {"1", "true", "yes", "on"}
SYNC_URL = os.environ.get("SYNCTHING_URL", "http://127.0.0.1:8384").rstrip("/")
FOLDER_ID = os.environ.get("SYNCTHING_FOLDER_ID", "claude-wiki")
SYNC_CONFIG = pathlib.Path(os.environ.get("SYNCTHING_CONFIG", "~/syncthing/config/config.xml")).expanduser()
TIMEOUT = int(os.environ.get("WIKI_GIT_TIMEOUT", "12"))
NET_TIMEOUT = int(os.environ.get("WIKI_GIT_NET_TIMEOUT", "60"))  # pull, push and the pre-commit hook
STALE_LOCK_SECONDS = 15 * 60
GIT_ENV = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
SYNC_WAIT_SECONDS = int(os.environ.get("WIKI_SYNC_WAIT_SECONDS", "60"))
_KEY = r"(?:token|api[_ -]?key|secret|passw(?:or)?d|(?<![a-z])(?:pass|pwd)(?![a-z]))(?:[_-](?:access|secret|key|id|value))*"
# ponytail: values shorter than 6 chars are not flagged (keeps "token: none" prose quiet); `${VAR}` and `<angle>` placeholders are exempt.
# Prose such as "password = secret key" still blocks the round; fix the line or reword it.
SECRET_RE = re.compile(
    r"(?i)" + _KEY + r"""["']?\s*[:=]\s*["']?(?!\$\{|<)[^\s"']{6,}"""
    r"|(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{12,}|github_pat_[A-Za-z0-9_]{20,}"
    r"|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,}|eyJ[A-Za-z0-9_-]{5,}\.eyJ[A-Za-z0-9_-]{5,}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----"
)
SECRET_NAMES = (".env", ".env.*", "*.pem", "*.key", "*.p12", "*.pfx", "id_rsa*", "id_ed25519*")

class SyncError(Exception):
    pass

def log(action: str, result: str) -> None:
    try:
        stamp = dt.datetime.now().astimezone().isoformat(timespec="seconds")
        with (ROOT.parent / "wiki-sync.log").open("a", encoding="utf-8", errors="replace") as f:
            f.write(f"{stamp} {action}: {result.replace(chr(10), ' ')[:300]}\n")
    except Exception:
        pass

def status(ok: bool, why: str = "") -> None:
    """One-line state file next to the log: `ok <time>` after a full round, `FAIL <time> <why>` after an error. Skips leave it alone, so a stale `ok` shows a stuck sync."""
    try:
        stamp = dt.datetime.now().astimezone().isoformat(timespec="seconds")
        text = f"ok {stamp}" if ok else f"FAIL {stamp} {why.replace(chr(10), ' ')[:200]}"
        (ROOT.parent / "wiki-sync.status").write_text(text + "\n", encoding="utf-8", errors="replace")
    except Exception:
        pass

def git(*args: str, check: bool = True, timeout: int = TIMEOUT) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(["git", *args], cwd=ROOT, text=True, encoding="utf-8", errors="surrogateescape", capture_output=True, timeout=timeout, env=GIT_ENV)
    if check and p.returncode:
        raise SyncError(f"git {' '.join([a for a in args if not a.startswith('-') and '=' not in a][:2])}: exit {p.returncode}")
    return p

def tail(p: subprocess.CompletedProcess[str]) -> str:
    return re.sub(r"://[^/@\s]+@", "://***@", p.stderr.strip()[-200:])  # strip URL credentials

def check_root() -> None:
    if not ROOT.is_absolute() or not ROOT.is_dir():
        raise SyncError("WIKI_ROOT must be an existing absolute directory")

def validate() -> None:
    if git("rev-parse", "--show-toplevel").stdout.strip() != str(ROOT.resolve()):
        raise SyncError("WIKI_ROOT is not the Git root")
    if not REMOTE or not BRANCH or not FOLDER_ID:
        raise SyncError("remote, branch, and Syncthing folder id must be non-empty")
    head = git("symbolic-ref", "--short", "HEAD", check=False).stdout.strip()
    if head != BRANCH:
        raise SyncError(f"HEAD is {head or 'detached'}, expected {BRANCH}; refusing to run")
    # ponytail: assumes .git is a directory (no linked worktrees)
    if any((ROOT / ".git" / d).exists() for d in ("rebase-merge", "rebase-apply")):
        raise SyncError("rebase in progress; resolve it by hand")

def index_locked() -> bool:
    """True for a fresh index.lock (normal skip); a stale one is a failure."""
    try:
        age = time.time() - (ROOT / ".git" / "index.lock").stat().st_mtime
    except FileNotFoundError:
        return False
    if age > STALE_LOCK_SECONDS:
        raise SyncError(f"stale index.lock ({int(age // 60)} min old); remove it after checking no git is running")
    return True

def blocked_files() -> list[str]:
    """Staged files to block: by name, or by secret-like text in their added lines."""
    names = git("diff", "--cached", "--name-only", "--diff-filter=d", "--no-color", "--no-renames", "-z").stdout.split("\0")  # deleted files add no text
    bad = []
    for name in filter(None, names):
        if any(fnmatch.fnmatchcase(posixpath.basename(name).lower(), pat) for pat in SECRET_NAMES):
            bad.append(name)
            continue
        # ponytail: binary files other than the names above are not content-scanned
        diff = git("--literal-pathspecs", "-c", "core.quotePath=false", "diff", "--cached", "--no-color", "--text", "--no-textconv", "--no-ext-diff", "-U0", "--", name).stdout
        in_hunk = False
        for line in diff.split("\n"):
            if line.startswith("@@"):
                in_hunk = True
            elif in_hunk and line.startswith("+") and SECRET_RE.search(line[1:]):
                bad.append(name)
                break
    return bad

def run_hook() -> None:
    """Extra check only: the built-in scan has already run. Never log the hook's output."""
    rel = git("rev-parse", "--git-path", "hooks/pre-commit").stdout.strip()
    hook = ROOT / rel
    if hook.is_file() and os.access(hook, os.X_OK):
        rc = subprocess.run([str(hook)], cwd=ROOT, env=GIT_ENV, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=NET_TIMEOUT).returncode
        if rc:
            log("pre-commit", f"hook failed exit={rc}")
            raise SyncError(f"pre-commit hook failed: exit {rc}")

def commit_changes() -> bool:
    if not git("status", "--porcelain").stdout:
        log("commit", "no working-tree changes")
        return False
    git("add", "-A", "--", ".", ":(exclude,glob)**/.stfolder/**", ":(exclude,glob)**/.stversions/**", ":(exclude,glob)**/.syncthing.*.tmp", ":(exclude,glob)**/~syncthing~*.tmp", ":(exclude,glob)**/*.sync-conflict-*")
    if not git("diff", "--cached", "--quiet", check=False).returncode:
        log("commit", "no trackable changes")
        return False
    try:
        bad = blocked_files()
        if bad:
            log("secret-scan", "blocked files=" + ",".join(bad))
            raise SyncError("secret-like content; unstaged all changes; review files: " + ", ".join(bad))
        run_hook()
    except Exception:
        git("reset", "-q", check=False)  # index only; the working tree is untouched
        raise
    now = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")
    # --no-verify: the pre-commit hook already ran above (and its stderr must not reach our log)
    p = git("-c", "user.useConfigOnly=true", "commit", "--no-verify", "-m", f"docs: auto-commit wiki changes ({now})", check=False)
    if p.returncode:
        raise SyncError("git commit failed: " + p.stderr.strip()[:240])
    log("commit", "created " + p.stdout.strip().splitlines()[0][:180])
    return True

def pull_rebase() -> None:
    try:
        # ponytail: --no-autostash means a Syncthing write landing after the commit makes this round fail (exit 1); the next run recommits
        p = git("pull", "--rebase", "--no-autostash", REMOTE, BRANCH, check=False, timeout=NET_TIMEOUT)
    except subprocess.TimeoutExpired:
        git("rebase", "--abort", check=False)
        log("pull-rebase", "timed out; rebase aborted")
        raise SyncError("pull --rebase timed out; rebase aborted")
    if p.returncode:
        git("rebase", "--abort", check=False)
        log("pull-rebase", "failed; rebase aborted: " + tail(p))
        raise SyncError("pull --rebase failed; rebase aborted: " + tail(p))
    log("pull-rebase", "ok")

def push() -> None:
    for attempt in (1, 2):
        try:
            p = git("push", REMOTE, BRANCH, check=False, timeout=NET_TIMEOUT)
        except subprocess.TimeoutExpired:
            raise SyncError("push timed out")
        if p.returncode == 0:
            log("push", f"ok attempt={attempt}")
            return
        log("push", f"rejected/failed attempt={attempt}: " + tail(p))
        if attempt == 1:
            pull_rebase()
    raise SyncError("push failed after rebase retry; manual review required")

def syncthing_key() -> str:
    try:
        root = ET.parse(SYNC_CONFIG).getroot()
    except (OSError, ET.ParseError) as e:
        raise SyncError("Syncthing config.xml unreadable: " + type(e).__name__)
    key = root.findtext("gui/apikey") or root.findtext("gui/APIKey")
    if not key:
        raise SyncError("Syncthing API key missing from config.xml")
    return key

def syncthing_status() -> dict:
    req = urllib.request.Request(SYNC_URL + "/rest/db/status?folder=" + urllib.parse.quote(FOLDER_ID), headers={"X-API-Key": syncthing_key()})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # never send the API key to a proxy
    with opener.open(req, timeout=TIMEOUT) as resp:
        return json.load(resp)

def wait_idle() -> bool:
    deadline = time.monotonic() + SYNC_WAIT_SECONDS
    while True:
        try:
            status = syncthing_status()
            if status.get("state") == "idle" and status.get("needTotalItems") == 0:
                log("syncthing", "idle")
                return True
        except SyncError:
            raise  # config.xml missing or no API key: not a transient condition
        except urllib.error.HTTPError as e:
            if e.code < 500:
                raise SyncError(f"Syncthing API HTTP {e.code}; check API key and folder id")
            log("syncthing", f"status HTTP {e.code}")
        except Exception as e:  # connection refused, timeout: Syncthing is busy or down, retry then skip
            log("syncthing", "status error " + type(e).__name__)
        if time.monotonic() >= deadline:
            log("syncthing", f"not idle after {SYNC_WAIT_SECONDS} seconds; skipped")
            return False
        time.sleep(min(2, max(0, deadline - time.monotonic())))

def run(mode: str) -> None:
    if mode not in ("start", "finalize"):
        raise SyncError("usage: wiki_sync.py start|finalize")
    check_root()
    with (ROOT / ".git" / "wiki-sync.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            log(mode, "skipped; another wiki_sync run holds the lock")
            return
        validate()
        if index_locked():
            log(mode, "skipped; index.lock exists")
            return
        if not wait_idle():
            log(mode, "skipped; Syncthing not idle")
            return
        commit_changes()
        pull_rebase()
        if mode == "finalize" and AUTOPUSH:
            push()
        log(mode, "complete")
        status(True)

def main() -> int:
    try:
        if len(sys.argv) != 2:
            raise SyncError("usage: wiki_sync.py start|finalize")
        run(sys.argv[1])
        return 0
    except Exception as e:
        try:
            log("error", type(e).__name__ + ": " + str(e))
        except Exception:
            pass
        status(False, type(e).__name__ + ": " + str(e))
        print(f"wiki-sync: {type(e).__name__}: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
