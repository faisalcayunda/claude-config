#!/usr/bin/env python3
"""Orchestrator guard: blocks the main Claude Code session from writing
implementation code itself, so it delegates to specialist subagents
(CLAUDE.md rule 5).

Modes (argv[1]):
  remind - UserPromptSubmit: inject a short reminder as additionalContext.
  guard  - PreToolUse (Write|Edit|MultiEdit|NotebookEdit|Bash): deny large
           main-session code writes. Also checks Agent|Task dispatches: a
           missing `model` is denied, and reviewer/planner/designer/
           architect/auditor subagent_types must use model fable.

Discriminator: `agent_id` is present in the hook payload only when the hook
fires inside a subagent (verified via code.claude.com/docs/en/hooks). Main
session calls have no `agent_id`.

Fails open: malformed stdin or any exception prints to stderr and exits 0,
so a bug in this hook never blocks all writes.
"""
import json
import re
import sys
from os.path import exists, expanduser

MAX_SOLO_LINES = 20  # ponytail: constant, raise here if the threshold changes

CODE_EXTS = frozenset({
    "py", "ipynb", "swift", "go", "rs", "java", "kt", "kts", "scala", "rb", "php",
    "c", "cc", "cpp", "h", "hpp", "m", "mm", "cs", "dart", "ts", "tsx", "js", "jsx",
    "mjs", "cjs", "vue", "svelte", "html", "css", "scss", "sql", "sh", "bash", "zsh",
    "tf", "lua",
})

# ponytail: simple regex, not a shell parser. Catches `cat > x.py <<EOF`,
# `> x.swift`, `>> x.go`, `tee [-a] x.ts`. sed -i, python -c writes and
# similar still pass; upgrade to shlex-based parsing if that gap bites.
_EXT_ALT = "|".join(sorted(CODE_EXTS, key=len, reverse=True))
BASH_WRITE_RE = re.compile(
    r"(?:(?<!<)>{1,2}(?!>)|\btee(?:\s+-a)?\b)\s+"
    r"['\"]?[\w./~-]*\.(?:" + _EXT_ALT + r")\b"
)

MEMORY_DIR_RE = re.compile(r"/\.claude/projects/[^/]+/memory/")


def emit_deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}))


def deny(detail, session_id):
    reason = (
        "Orchestrator guard: the main session does not write implementation code "
        f"({detail}). Delegate to the matching specialist with the Agent tool and "
        "pass `model` (CLAUDE.md rule 5). Edits of 20 lines or fewer pass. If the "
        "user explicitly asked you to write this yourself, ask them to run "
        "`! mkdir -p ~/.claude/state/orchestrator-solo && touch "
        f"~/.claude/state/orchestrator-solo/{session_id}`. Never create that file "
        "yourself and never route around this block through Bash."
    )
    emit_deny(reason)


AGENT_REVIEW_RE = re.compile(r"review|plan|architect|design|audit", re.IGNORECASE)


def is_allowed_path(path, scratchpad_dir):
    if not path:
        return False
    if MEMORY_DIR_RE.search(path):
        return True
    if "/.claude/wiki/" in path or "/.claude/plans/" in path:
        return True
    if scratchpad_dir and scratchpad_dir in path:
        return True
    if "/private/tmp/claude-" in path or "/tmp/claude-" in path:
        return True
    return False


def ext_of(path):
    name = path.rsplit("/", 1)[-1]
    return name.rsplit(".", 1)[-1].lower() if "." in name else ""


def count_lines(text):
    return len(text.splitlines()) if text else 0


def guard(payload):
    tool_input = payload.get("tool_input") or {}
    if payload.get("tool_name") in ("Agent", "Task"):
        subagent_type = tool_input.get("subagent_type") or ""
        model = tool_input.get("model") or ""
        if subagent_type == "fork":
            return  # forks always run on the orchestrator's model
        if not model:
            emit_deny(
                "Pass `model` on every Agent dispatch (CLAUDE.md rule 5): fable "
                "for reviewers, planners, designers, architects, auditors and "
                "long tasks; sonnet for implementation and triage; haiku for "
                "Explore and pure search."
            )
            return
        if AGENT_REVIEW_RE.search(subagent_type) and not model.startswith(("fable", "claude-fable")):
            emit_deny(
                f"`{subagent_type}` is a reviewer/planner/designer role: dispatch "
                "it with model fable (CLAUDE.md rule 5)."
            )
        return
    if "agent_id" in payload:
        return  # subagents are the implementers
    session_id = payload.get("session_id", "")
    if session_id and exists(expanduser(
            f"~/.claude/state/orchestrator-solo/{session_id}")):
        return  # explicit user-authorized override

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}
    scratchpad_dir = payload.get("scratchpad_dir") or ""

    if tool_name == "Bash":
        command = tool_input.get("command", "") or ""
        if scratchpad_dir and scratchpad_dir in command:
            return
        if "/private/tmp/claude-" in command or "/tmp/claude-" in command:
            return
        m = BASH_WRITE_RE.search(command)
        if not m:
            return
        deny(f"shell write to {m.group(0).strip()}", session_id)
        return

    if tool_name == "Write":
        path = tool_input.get("file_path", "")
        lines = count_lines(tool_input.get("content", ""))
    elif tool_name == "Edit":
        path = tool_input.get("file_path", "")
        lines = count_lines(tool_input.get("new_string", ""))
    elif tool_name == "MultiEdit":
        path = tool_input.get("file_path", "")
        lines = sum(count_lines(e.get("new_string", ""))
                    for e in (tool_input.get("edits") or []))
    elif tool_name == "NotebookEdit":
        path = tool_input.get("notebook_path", "")
        lines = count_lines(tool_input.get("new_source", ""))
    else:
        return

    if is_allowed_path(path, scratchpad_dir):
        return
    if ext_of(path) not in CODE_EXTS:
        return
    if lines <= MAX_SOLO_LINES:
        return
    deny(f"{lines} lines to {path}", session_id)


def remind():
    text = (
        "Orchestrator mode: you route work, you do not implement it. "
        "Implementation, design and review go to the matching specialist "
        "through the Agent tool with `model` set (CLAUDE.md rule 5). Go solo "
        "only for a lookup, a measurement, or an edit of 20 lines or fewer, "
        "and say so. orchestrator_guard blocks larger main-session code writes. "
        "Talk to the user the humanoid way (load the skill for longer replies): "
        "santai Indonesian with aku/kamu, like a colleague, not a report. Lead "
        "with the answer, say it plainly, stop. No em dashes, no praise opener, "
        "no trailing offer or recap, no decorative triads. Lists only for real "
        "enumerations. Never state a fact you did not check."
    )
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": text,
    }}))


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        if mode == "remind":
            remind()
        elif mode == "guard":
            payload = json.loads(sys.stdin.read())
            guard(payload)
    except Exception as exc:  # fail open: never block on a hook bug
        print(f"orchestrator_guard error: {exc}", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
