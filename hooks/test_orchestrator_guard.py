#!/usr/bin/env python3
"""Runnable check for orchestrator_guard.py. Plain asserts, no framework.
Pipes real payloads into the actual script via subprocess.
"""
import json
import os
import subprocess
import sys

HOOK = "/Users/isal/.claude/hooks/orchestrator_guard.py"
PY = "/usr/bin/python3"


def run(mode, payload=None):
    stdin = json.dumps(payload) if payload is not None else ""
    r = subprocess.run([PY, HOOK, mode], input=stdin, capture_output=True, text=True)
    return r


def out_json(r):
    return json.loads(r.stdout) if r.stdout.strip() else None


def is_deny(r):
    j = out_json(r)
    return bool(j) and j.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"


def base(tool_name, tool_input, session_id="sess-1", agent_id=None):
    p = {
        "session_id": session_id,
        "cwd": "/tmp",
        "permission_mode": "default",
        "hook_event_name": "PreToolUse",
        "tool_name": tool_name,
        "tool_input": tool_input,
    }
    if agent_id:
        p["agent_id"] = agent_id
    return p


checks = []


def check(name, cond):
    checks.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


# 1. main-session Write of 30 lines to a .py outside the allowlist is denied
content30 = "\n".join(f"line {i}" for i in range(30))
r = run("guard", base("Write", {"file_path": "/Users/isal/proj/app.py", "content": content30}))
check("30-line Write .py main-session denied", r.returncode == 0 and is_deny(r))

# 2. same payload with agent_id is allowed
r = run("guard", base("Write", {"file_path": "/Users/isal/proj/app.py", "content": content30}, agent_id="ag-1"))
check("30-line Write .py with agent_id allowed", r.returncode == 0 and out_json(r) is None)

# 3. a 5-line Edit is allowed
content5 = "\n".join(f"line {i}" for i in range(5))
r = run("guard", base("Edit", {"file_path": "/Users/isal/proj/app.py", "new_string": content5}))
check("5-line Edit allowed", r.returncode == 0 and out_json(r) is None)

# 4. a 30-line Write to a .md is allowed
r = run("guard", base("Write", {"file_path": "/Users/isal/proj/notes.md", "content": content30}))
check("30-line Write .md allowed", r.returncode == 0 and out_json(r) is None)

# 5. a 30-line Write under ~/.claude/wiki/ is allowed
r = run("guard", base("Write", {"file_path": "/Users/isal/.claude/wiki/concepts/x.py", "content": content30}))
check("30-line Write under wiki/ allowed", r.returncode == 0 and out_json(r) is None)

# 5b. a 30-line Write under scratchpad_dir is allowed
p = base("Write", {"file_path": "/private/tmp/claude-501/scratch/x.py", "content": content30})
p["scratchpad_dir"] = "/private/tmp/claude-501/scratch"
r = run("guard", p)
check("30-line Write under scratchpad_dir allowed", r.returncode == 0 and out_json(r) is None)

# 6. MultiEdit summing over 20 is denied
edits = [{"old_string": "a", "new_string": "\n".join(f"l{i}" for i in range(12))},
         {"old_string": "b", "new_string": "\n".join(f"l{i}" for i in range(12))}]
r = run("guard", base("MultiEdit", {"file_path": "/Users/isal/proj/app.go", "edits": edits}))
check("MultiEdit sum >20 denied", r.returncode == 0 and is_deny(r))

# 7. Bash `cat > /Users/x/app.py <<EOF` denied
r = run("guard", base("Bash", {"command": "cat > /Users/x/app.py <<EOF\nprint(1)\nEOF"}))
check("Bash heredoc write to .py denied", r.returncode == 0 and is_deny(r))

# 8. same with agent_id allowed
r = run("guard", base("Bash", {"command": "cat > /Users/x/app.py <<EOF\nprint(1)\nEOF"}, agent_id="ag-1"))
check("Bash heredoc write with agent_id allowed", r.returncode == 0 and out_json(r) is None)

# 9. ls -la > out.txt allowed
r = run("guard", base("Bash", {"command": "ls -la > out.txt"}))
check("Bash redirect to .txt allowed", r.returncode == 0 and out_json(r) is None)

# 10. override file present allows
fake_session = "test-override-session-xyz"
override_path = f"/Users/isal/.claude/state/orchestrator-solo/{fake_session}"
os.makedirs(os.path.dirname(override_path), exist_ok=True)
open(override_path, "w").close()
try:
    r = run("guard", base("Write", {"file_path": "/Users/isal/proj/app.py", "content": content30}, session_id=fake_session))
    check("override file allows solo write", r.returncode == 0 and out_json(r) is None)
finally:
    os.remove(override_path)

# 11. garbage stdin exits 0
r = subprocess.run([PY, HOOK, "guard"], input="not json {{{", capture_output=True, text=True)
check("garbage stdin exits 0", r.returncode == 0)

# 12. remind prints valid JSON with hookSpecificOutput.additionalContext
r = run("remind")
j = out_json(r)
check("remind prints additionalContext", r.returncode == 0 and bool(
    j and "additionalContext" in j.get("hookSpecificOutput", {})))

# 13. Agent Explore without model is denied
r = run("guard", base("Agent", {"subagent_type": "Explore"}))
check("Agent Explore without model denied", r.returncode == 0 and is_deny(r))

# 14. Agent Explore with model haiku is allowed
r = run("guard", base("Agent", {"subagent_type": "Explore", "model": "haiku"}))
check("Agent Explore with model haiku allowed", r.returncode == 0 and out_json(r) is None)

# 15. Agent fork without model is allowed
r = run("guard", base("Agent", {"subagent_type": "fork"}))
check("Agent fork without model allowed", r.returncode == 0 and out_json(r) is None)

# 16. Agent code-reviewer with model sonnet is denied
r = run("guard", base("Agent", {"subagent_type": "code-reviewer", "model": "sonnet"}))
check("Agent code-reviewer with model sonnet denied", r.returncode == 0 and is_deny(r))

# 17. Agent planner with model opus is allowed
r = run("guard", base("Agent", {"subagent_type": "planner", "model": "opus"}))
check("Agent planner with model opus allowed", r.returncode == 0 and out_json(r) is None)

# 18. Agent python-pro with model sonnet is allowed
r = run("guard", base("Agent", {"subagent_type": "python-pro", "model": "sonnet"}))
check("Agent python-pro with model sonnet allowed", r.returncode == 0 and out_json(r) is None)

# 19. full model ID for opus is accepted for a reviewer
r = run("guard", base("Agent", {"subagent_type": "code-reviewer", "model": "claude-opus-5"}))
check("Agent code-reviewer with claude-opus-5 allowed", r.returncode == 0 and out_json(r) is None)

failed = [n for n, c in checks if not c]
if failed:
    print(f"\n{len(failed)}/{len(checks)} FAILED: {failed}")
    sys.exit(1)
print(f"\nAll {len(checks)} checks passed.")
