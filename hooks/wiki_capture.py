#!/usr/bin/env python3
"""Wiki capture hooks for Claude Code (Phase 3 of the context consolidation plan).

Subcommands (hook JSON on stdin):
  check       Stop (sync): after substantive work, exit 2 so Claude decides what to write as drafts
  autocommit  Stop (async): commit pending wiki changes; the repo pre-commit secret scan still runs
  selftest    run built-in checks

Trigger (decision Q12): at least 15 tool calls, or any DB query / WebFetch / WebSearch / Agent call,
since the last capture, AND at least 20 minutes since the last capture (or since the session was
first seen). The transcript is read incrementally from a stored byte offset.
Compatible with /usr/bin/python3 (3.9).
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import time

WIKI_ROOT = "/Users/isal/.claude/wiki"
STATE_DIR = "/Users/isal/.claude/cache/wiki-capture"
USAGE_LOG = "/Users/isal/.claude/metrics/wiki-usage.jsonl"
MIN_TOOL_CALLS = 15
MIN_INTERVAL_SECONDS = 20 * 60
STRONG_TOOLS = {"WebFetch", "WebSearch", "Agent"}
STRONG_PREFIXES = ("mcp__dbhub",)

REASON = """Wiki capture check (automatic): since the last capture this session made {tools} tool calls{strong}.
Decide now whether anything is page-worthy for the wiki at /Users/isal/.claude/wiki:
- page-worthy: hard-won facts about external systems not recorded in any repo, decisions with their rationale, recurring gotchas, repeated how-tos
- not page-worthy: progress narration, one-off outputs, things already in git or a repo, raw data rows
If something qualifies: search existing pages first (/usr/bin/grep -ril "<keyword>" /Users/isal/.claude/wiki --include='*.md') and update the matching page; otherwise create a page with status: draft following the Page conventions in the save skill (English body, Indonesian aliases, org, one-sentence description). Never include credentials or personal data. Changes are committed automatically.
If nothing qualifies, reply with one short line saying so."""


def log_event(event, **fields):
    try:
        os.makedirs(os.path.dirname(USAGE_LOG), exist_ok=True)
        rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": event}
        rec.update(fields)
        with open(USAGE_LOG, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec) + "\n")
    except OSError:
        pass


def _state_path(session_id):
    return os.path.join(STATE_DIR, re.sub(r"[^A-Za-z0-9_\-]", "_", session_id or "unknown") + ".json")


def load_state(session_id, now):
    try:
        with open(_state_path(session_id), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {"first_seen": now, "last_capture": None, "offset": 0, "tools": 0, "strong": False}


def save_state(session_id, state):
    os.makedirs(STATE_DIR, exist_ok=True)
    tmp = _state_path(session_id) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh)
    os.replace(tmp, _state_path(session_id))


def scan_transcript(path, offset):
    """Count tool_use blocks in complete lines after `offset`. Returns (tools, strong, new_offset)."""
    try:
        size = os.path.getsize(path)
    except OSError:
        return 0, False, offset
    if size < offset:                      # transcript rewritten: start over
        offset = 0
    tools, strong = 0, False
    with open(path, "rb") as fh:
        fh.seek(offset)
        chunk = fh.read()
    end = chunk.rfind(b"\n")
    if end < 0:
        return 0, False, offset
    for raw in chunk[: end + 1].splitlines():
        if b'"tool_use"' not in raw:
            continue
        try:
            rec = json.loads(raw)
        except ValueError:
            continue
        msg = rec.get("message") if rec.get("type") == "assistant" else None
        for block in (msg or {}).get("content") or []:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                tools += 1
                name = block.get("name") or ""
                if name in STRONG_TOOLS or name.startswith(STRONG_PREFIXES):
                    strong = True
    return tools, strong, offset + end + 1


def decide(state, tools, strong, new_offset, now):
    """Pure trigger logic. Returns (fire, state)."""
    state = dict(state)
    state["tools"] = state.get("tools", 0) + tools
    state["strong"] = bool(state.get("strong")) or strong
    state["offset"] = new_offset
    since = state.get("last_capture") or state.get("first_seen") or now
    worked = state["tools"] >= MIN_TOOL_CALLS or state["strong"]
    if worked and now - since >= MIN_INTERVAL_SECONDS:
        return True, state
    return False, state


def cmd_check(payload, now=None):
    now = now or time.time()
    if payload.get("stop_hook_active"):
        return 0
    session = payload.get("session_id") or "unknown"
    state = load_state(session, now)
    tools, strong, offset = scan_transcript(payload.get("transcript_path") or "", state.get("offset", 0))
    fire, state = decide(state, tools, strong, offset, now)
    if not fire:
        save_state(session, state)
        return 0
    n, s = state["tools"], state["strong"]
    state.update({"last_capture": now, "tools": 0, "strong": False})
    save_state(session, state)
    log_event("capture_prompt", session=session, tools=n, strong=s)
    sys.stderr.write(REASON.format(tools=n, strong=", including DB queries, web fetches or agent reports" if s else ""))
    return 2


def _git(*args):
    return subprocess.run(["git", "-C", WIKI_ROOT] + list(args), capture_output=True, text=True)


def cmd_autocommit(payload):
    if os.path.exists(os.path.join(WIKI_ROOT, ".git", "index.lock")):
        return 0                            # another git process (e.g. obsidian-git) is busy
    status = _git("status", "--porcelain")
    if status.returncode != 0 or not status.stdout.strip():
        return 0
    _git("add", "-A")
    stamp = time.strftime("%Y-%m-%d %H:%M")
    res = _git("commit", "-q", "-m", "docs: auto-commit wiki changes (%s)" % stamp)
    if res.returncode == 0:
        log_event("autocommit", session=payload.get("session_id"),
                  files=len(status.stdout.strip().splitlines()))
    else:
        _git("reset", "-q")                 # leave the working tree dirty, index clean
        log_event("autocommit_failed", session=payload.get("session_id"),
                  reason="pre-commit or git error")
    return 0


def selftest():
    global STATE_DIR, USAGE_LOG
    tmp = tempfile.mkdtemp()
    STATE_DIR, USAGE_LOG = os.path.join(tmp, "state"), os.path.join(tmp, "usage.jsonl")
    t0 = 1_000_000.0
    base = {"first_seen": t0, "last_capture": None, "offset": 0, "tools": 0, "strong": False}
    fire, st = decide(base, 20, False, 10, t0 + 60)
    assert not fire and st["tools"] == 20                     # too soon
    fire, st = decide(st, 0, False, 10, t0 + MIN_INTERVAL_SECONDS + 1)
    assert fire                                               # enough work and time
    fire, _ = decide(base, 3, False, 0, t0 + 3600)
    assert not fire                                           # time passed, little work
    fire, _ = decide(base, 1, True, 0, t0 + 3600)
    assert fire                                               # a DB query counts as substantive

    tr = os.path.join(tmp, "t.jsonl")
    def rec(name):
        return json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": name}]}})
    with open(tr, "w") as fh:
        fh.write("\n".join([rec("Bash"), rec("Read"), json.dumps({"type": "user"}),
                            rec("mcp__dbhub-mpm__execute_sql")]) + "\n")
    tools, strong, off = scan_transcript(tr, 0)
    assert (tools, strong) == (3, True) and off == os.path.getsize(tr)
    with open(tr, "a") as fh:
        fh.write(rec("Bash") + "\n" + '{"type": "assistant", "partial')     # incomplete last line
    tools2, strong2, off2 = scan_transcript(tr, off)
    assert (tools2, strong2) == (1, False) and off2 < os.path.getsize(tr)

    payload = {"session_id": "s1", "transcript_path": tr}
    assert cmd_check(payload, now=t0) == 0                     # first sighting only records state
    assert cmd_check(dict(payload, stop_hook_active=True), now=t0 + 9999) == 0
    with open(tr, "a") as fh:
        fh.write("\n" + "\n".join(rec("Bash") for _ in range(16)) + "\n")
    import io
    err, sys.stderr = sys.stderr, io.StringIO()
    try:
        assert cmd_check(payload, now=t0 + MIN_INTERVAL_SECONDS + 5) == 2
        assert "Wiki capture check" in sys.stderr.getvalue()
        assert cmd_check(payload, now=t0 + MIN_INTERVAL_SECONDS + 10) == 0   # counters reset
    finally:
        sys.stderr = err
    print("selftest OK")
    return 0


def main(argv):
    cmd = argv[0] if argv else ""
    if cmd == "selftest":
        return selftest()
    try:
        payload = json.load(sys.stdin)
        if cmd == "check":
            return cmd_check(payload)
        if cmd == "autocommit":
            return cmd_autocommit(payload)
    except Exception as exc:                                   # never break session stop
        log_event("error", command=cmd, error=type(exc).__name__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
