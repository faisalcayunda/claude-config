#!/usr/bin/env python3
"""Wiki -> AFFiNE sync reminder hook for Claude Code.

Stop hook (sync): scans the wiki git repo for changed .md files tagged `org: BGN` in frontmatter,
and if any are found, exits 2 with a reason on stderr so Claude considers syncing them to the
AFFiNE "BGN Digital" workspace -- but Claude must still get explicit user approval before any actual
AFFiNE write (hooks cannot call MCP tools themselves, so nothing is ever pushed from here).

Dedup: a small JSON state file remembers which (path, mtime) pairs were already flagged, so this
does not nag on every Stop for the same unchanged content -- only for genuinely new/changed BGN pages.

Usage (hook JSON arrives on stdin):
  wiki_bgn_sync.py            default: run the check
  wiki_bgn_sync.py selftest   run built-in checks (no stdin needed)

Compatible with /usr/bin/python3 (3.9).
"""
import json
import os
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_hooks import parse_frontmatter  # shared frontmatter parser, avoid duplicating it

WIKI_ROOT = "/Users/isal/.claude/wiki"
STATE_PATH = "/Users/isal/.claude/cache/wiki-bgn-sync-state.json"
USAGE_LOG = "/Users/isal/.claude/metrics/wiki-usage.jsonl"
AFFINE_WORKSPACE_ID = "b0b8ef97-b4c9-4099-a600-a905d15a23e4"

REASON = """Wiki -> AFFiNE sync check (automatic): these wiki pages changed this session and are tagged org: BGN:
{files}

If this content should also live in the AFFiNE workspace "BGN Digital" (workspaceId %s):
1. Check whether a matching AFFiNE doc already exists first (mcp__affine-bgn-digital__search_docs by title or domain code) -- don't create a duplicate.
2. Ask the user for explicit confirmation before any AFFiNE write call (create_doc_from_markdown, replace_doc_with_markdown, update_doc_title, etc.) -- this is an outward-facing write to a shared workspace, needs a fresh yes each time, same rule as git pushes (CLAUDE.md rule 3). Hooks cannot call MCP tools themselves, so nothing has been written yet.
3. If the user doesn't want to sync now, say so in one short line and move on -- this won't repeat for this exact version of the file.
If none of these pages actually belong in AFFiNE (e.g. personal working notes, not team-facing), reply with one short line saying so.""" % AFFINE_WORKSPACE_ID


def log_event(event, **fields):
    try:
        os.makedirs(os.path.dirname(USAGE_LOG), exist_ok=True)
        rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": event}
        rec.update(fields)
        with open(USAGE_LOG, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec) + "\n")
    except OSError:
        pass


def _git(*args):
    return subprocess.run(["git", "-C", WIKI_ROOT] + list(args), capture_output=True, text=True)


def _load_state():
    try:
        with open(STATE_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def _save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh)
    os.replace(tmp, STATE_PATH)


def cmd_check(payload):
    if payload.get("stop_hook_active"):
        return 0
    status = _git("status", "--porcelain")
    if status.returncode != 0 or not status.stdout.strip():
        return 0
    state = _load_state()
    candidates = []
    for line in status.stdout.splitlines():
        path_part = line[3:].strip()
        if " -> " in path_part:              # renamed files: "R  old -> new"
            path_part = path_part.split(" -> ", 1)[1]
        if not path_part.endswith(".md"):
            continue
        full = path_part if os.path.isabs(path_part) else os.path.join(WIKI_ROOT, path_part)
        try:
            mtime = os.stat(full).st_mtime
        except OSError:
            continue
        try:
            with open(full, encoding="utf-8", errors="replace") as fh:
                fm = parse_frontmatter(fh.read(4000))
        except OSError:
            continue
        if str(fm.get("org") or "") != "BGN":
            continue
        if state.get(full) == mtime:
            continue                          # already flagged this exact version
        candidates.append(full)
        state[full] = mtime
    if not candidates:
        return 0
    _save_state(state)
    rel = [os.path.relpath(p, WIKI_ROOT) for p in candidates]
    log_event("bgn_sync_candidate", session=payload.get("session_id"), files=rel)
    sys.stderr.write(REASON.format(files="\n".join("- " + r for r in rel)))
    return 2


def selftest():
    global WIKI_ROOT, STATE_PATH
    import io
    old_root, old_state = WIKI_ROOT, STATE_PATH
    tmp = tempfile.mkdtemp()
    WIKI_ROOT = os.path.join(tmp, "wiki")
    STATE_PATH = os.path.join(tmp, "state.json")
    os.makedirs(WIKI_ROOT, exist_ok=True)
    # git status paths come back relative to the repo root, and the real wiki repo's .git lives at
    # WIKI_ROOT itself -- so the temp repo must have that same layout (WIKI_ROOT == repo root)
    subprocess.run(["git", "init", "-q", WIKI_ROOT], check=True)
    subprocess.run(["git", "-C", WIKI_ROOT, "config", "user.email", "test@test"], check=True)
    subprocess.run(["git", "-C", WIKI_ROOT, "config", "user.name", "test"], check=True)
    bgn_file = os.path.join(WIKI_ROOT, "bgn.md")
    other_file = os.path.join(WIKI_ROOT, "personal.md")
    with open(bgn_file, "w", encoding="utf-8") as fh:
        fh.write("---\norg: BGN\n---\nbody\n")
    with open(other_file, "w", encoding="utf-8") as fh:
        fh.write("---\norg: personal\n---\nbody\n")
    err, sys.stderr = sys.stderr, io.StringIO()
    try:
        assert cmd_check({"session_id": "s1"}) == 2
        reason = sys.stderr.getvalue()
        assert "bgn.md" in reason and "personal.md" not in reason, reason
        sys.stderr = io.StringIO()
        assert cmd_check({"session_id": "s1"}) == 0                  # dedup: same mtime
        time.sleep(0.01)
        with open(bgn_file, "w", encoding="utf-8") as fh:
            fh.write("---\norg: BGN\n---\nbody changed\n")
        sys.stderr = io.StringIO()
        assert cmd_check({"session_id": "s1"}) == 2                  # content changed -> re-flag
        # sanity: everything ran against the temp repo, never touched the real wiki repo's state file
        assert os.path.exists(STATE_PATH) and STATE_PATH != old_state
    finally:
        sys.stderr = err
        WIKI_ROOT, STATE_PATH = old_root, old_state
    print("selftest OK")
    return 0


def main(argv):
    if argv and argv[0] == "selftest":
        return selftest()
    try:
        payload = json.load(sys.stdin)
        return cmd_check(payload)
    except Exception as exc:                                        # never break session stop
        log_event("error", error=type(exc).__name__)
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
