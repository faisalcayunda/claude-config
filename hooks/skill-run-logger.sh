#!/usr/bin/env bash
# skill-run-logger.sh — PostToolUse:Skill hook
# Appends a null-score run entry to the matching skill's eval.json for later human scoring.
# Silent on success; silently exits 0 on any error.

# Capture bash stdin first (heredoc would displace it from python3's stdin)
_SKILL_LOGGER_STDIN=$(cat)

_SKILL_LOGGER_STDIN="$_SKILL_LOGGER_STDIN" \
python3 2>/dev/null -c '
import sys, os, json, random, string, tempfile
from datetime import datetime, timezone

def main():
    raw = os.environ.get("_SKILL_LOGGER_STDIN", "")
    if not raw:
        return
    try:
        data = json.loads(raw)
    except Exception:
        return
    try:
        tool_input = data.get("tool_input", {})
        skill_name = tool_input.get("skill", "")
        if not skill_name:
            return

        args = tool_input.get("args", "")
        if args is None:
            args = ""

        session_id = (
            data.get("session_id")
            or os.environ.get("CLAUDE_CODE_SESSION_ID", "unknown")
            or "unknown"
        )

        duration_ms = data.get("duration_ms", None)

        tool_response = data.get("tool_response", {})
        if isinstance(tool_response, dict):
            content = tool_response.get("content", "")
        elif isinstance(tool_response, str):
            content = tool_response
        else:
            try:
                content = json.dumps(tool_response)
            except Exception:
                content = ""
        if content is None:
            content = ""
        elif not isinstance(content, str):
            try:
                content = json.dumps(content)
            except Exception:
                content = ""

        final_lines = content[-300:] if len(content) > 300 else content

        eval_path = os.path.join(
            "/Users/isal/.claude/skills", skill_name, "eval.json"
        )
        if not os.path.isfile(eval_path):
            return

        try:
            with open(eval_path, "r", encoding="utf-8") as f:
                eval_data = json.load(f)
        except Exception:
            return

        if not isinstance(eval_data, dict):
            return
        if "runs" not in eval_data or not isinstance(eval_data["runs"], list):
            return

        now_utc = datetime.now(timezone.utc)
        iso_ts = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
        rand_hex = "".join(random.choices(string.hexdigits[:16], k=6)).lower()
        run_id = f"{iso_ts}-{rand_hex}"

        run_entry = {
            "run_id": run_id,
            "session_id": session_id,
            "timestamp": iso_ts,
            "invocation_trigger": "claude-proactive",
            "arguments": args,
            "score": None,
            "outcome": None,
            "duration_ms": duration_ms,
            "trace": {
                "output_length_tokens": None,
                "tool_calls_made": [],
                "final_lines": final_lines,
                "failure_reason": None,
            },
            "human_review": {
                "scored_at": None,
                "correction": None,
                "note": None,
            },
        }

        eval_data["runs"].append(run_entry)

        eval_dir = os.path.dirname(eval_path)
        fd, tmp_path = tempfile.mkstemp(dir=eval_dir, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as tf:
                json.dump(eval_data, tf, indent=2, ensure_ascii=False)
                tf.write("\n")
            os.replace(tmp_path, eval_path)
        except Exception:
            try:
                os.unlink(tmp_path)
            except Exception:
                pass

    except Exception:
        return

main()
'

exit 0
