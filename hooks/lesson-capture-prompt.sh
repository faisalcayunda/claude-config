#!/usr/bin/env bash
# Injects a lesson-capture reminder after every Edit tool call.
# Prompts the model to record any correction/mistake into lessons_learned.md.

python3 - <<'EOF'
import json, sys

msg = (
    "If this Edit corrects a prior wrong answer, bad assumption, or speculative fix — "
    "append the lesson to:\n"
    "~/.claude/lessons_learned.md\n"
    "\n"
    "Format: date | what was wrong | correct answer | source/evidence | prevention rule.\n"
    "Skip this if the edit is purely additive with no correction involved."
)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": msg
    }
}))
EOF
