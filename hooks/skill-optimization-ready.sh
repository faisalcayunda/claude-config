#!/usr/bin/env bash
# skill-optimization-ready.sh
# UserPromptSubmit hook — scans eval.json files and injects advisory notice
# when any skill has 10+ scored runs (score != null).
# Must complete <50ms. Never blocks. Always exits 0.

# Fast pre-check: skip Python entirely if no scored runs exist anywhere
grep -qr '"score": [0-9]' /Users/isal/.claude/skills/ 2>/dev/null || exit 0

python3 2>/dev/null <<'PYEOF'
import sys
import json
import os
import glob

SKILLS_DIR = "/Users/isal/.claude/skills"
THRESHOLD = 10

def main():
    if not os.path.isdir(SKILLS_DIR):
        return

    pattern = os.path.join(SKILLS_DIR, "*/eval.json")
    ready_skills = []

    for eval_path in glob.iglob(pattern):
        skill_name = os.path.basename(os.path.dirname(eval_path))
        try:
            with open(eval_path, "r") as f:
                data = json.load(f)
            runs = data.get("runs")
            if not isinstance(runs, list):
                continue
            scored = sum(1 for r in runs if r.get("score") is not None)
            if scored >= THRESHOLD:
                ready_skills.append((skill_name, scored))
        except Exception:
            continue

    if not ready_skills:
        return

    lines = [
        f"📊 Skill optimization available: {name} has {count} scored runs. "
        f"Run /optimize-skill --skill {name} to generate improvement variants."
        for name, count in ready_skills
    ]
    context_str = "\n".join(lines)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context_str
        }
    }
    print(json.dumps(output))

main()
PYEOF

exit 0
