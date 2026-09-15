#!/usr/bin/env python3
"""UserPromptSubmit reminder for the TOP-LEVEL agent only.

Replaces the old ~550-token "MANDATORY PROTOCOL" block which (a) fired on every
turn including continuations — contradicting CLAUDE.md §16.0 — and (b) claimed to
"enforce" what a UserPromptSubmit hook cannot (it only injects text).

This version skips trivial continuations, stays concise, and is honest that
CLAUDE.md is advisory and governs only this agent (not subagents/workflows).
"""
import json
import sys

prompt = ""
try:
    data = json.load(sys.stdin)
    prompt = (data.get("prompt") or "").strip()
except Exception:
    pass

low = prompt.lower()
words = low.split()
CONT = {
    "ya", "iya", "ok", "oke", "sip", "yes", "y", "lanjut", "lanjutkan",
    "teruskan", "gas", "proceed", "go", "next", "no", "ngga", "nggak",
    "tidak", "batal", "stop", "abort", "noted", "thanks", "thx",
    "makasih", "ty", "done",
}

# Continuation / short acknowledgment -> no injection (honors §16.0).
if not prompt or low in CONT or (len(words) <= 4 and any(w in CONT for w in words)):
    print(json.dumps({}))
    sys.exit(0)

msg = (
    "\n[orchestration reminder — advisory, applies to THIS top-level agent only; "
    "subagents/workflows do NOT inherit CLAUDE.md, only hooks hard-enforce]\n"
    "- New non-trivial task: consider Wave 0 (context-manager ∥ prompt-engineer) "
    "and skill-first (Law 6) before specialists. Trivial/continuation: skip.\n"
    "- Hierarchy (startup model): you are tech lead, user is CEO/CTO. Route "
    "substantive work to the right specialist. Cost order: solo < 1 specialist < "
    "fan-out; prefer one correct specialist over a crowd. Full roster + routing "
    "table: governance/org-chart.md.\n"
    "- Escalate to CEO only for: ambiguous direction, big tradeoffs, "
    "destructive/outward-facing ops, final sign-off. Otherwise run autonomously and "
    "report the outcome, not every step.\n"
    "- Low confidence on a fact or system state: research/verify before asserting "
    "(Law 7/8).\n"
    "- ALWAYS-ON: any prose output (chat answers, docs, commit bodies, PR text, "
    "articles) follows the anti-slop-writing skill. Indonesian -> "
    "`anti-slop-writing-id`, English -> `anti-slop-writing`. Load it before "
    "writing anything longer than a couple of sentences. Code/tool output exempt.\n"
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": msg,
    }
}))
