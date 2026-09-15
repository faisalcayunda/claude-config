#!/usr/bin/env python3
# secret-scan: allow-file
"""PreToolUse guard (decision Q27): deny Write/Edit/MultiEdit that would put credentials or
personal IDs into the wiki or any memory directory. Values are never echoed.

Scope: /Users/isal/.claude/wiki/** and any path with a /memory/ segment.
Fails closed for in-scope paths if the scanner cannot be loaded.
Compatible with /usr/bin/python3 (3.9).
"""
import json
import sys

WIKI_ROOT = "/Users/isal/.claude/wiki/"
SCANNER_DIR = "/Users/isal/.claude/scripts"


def in_scope(path):
    return bool(path) and (path.startswith(WIKI_ROOT) or "/memory/" in path)


def texts_from(tool_input):
    out = []
    for key in ("content", "new_string"):
        if isinstance(tool_input.get(key), str):
            out.append(tool_input[key])
    for edit in tool_input.get("edits") or []:
        if isinstance(edit, dict) and isinstance(edit.get("new_string"), str):
            out.append(edit["new_string"])
    return out


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}))


def evaluate(payload, scanner=None):
    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or ""
    if not in_scope(path):
        return None
    if scanner is None:
        try:
            sys.path.insert(0, SCANNER_DIR)
            import secret_scan as scanner
        except Exception:
            return "Secret guard could not load its scanner; refusing to write to %s." % path
    findings = scanner.scan_text("\n".join(texts_from(tool_input)))
    if not findings:
        return None
    kinds = sorted({k for _, k in findings})
    return ("Secret guard: %d finding(s) of %s in content for %s. Remove credentials or personal data "
            "(write a placeholder such as ${VAR} or describe where the secret lives) and retry."
            % (len(findings), ", ".join(kinds), path))


def selftest():
    sys.path.insert(0, SCANNER_DIR)
    import secret_scan
    fake = "postgresql://svc:" + "Zx9" + "fake7Qq" + "@db.example.invalid/app"
    assert evaluate({"tool_input": {"file_path": WIKI_ROOT + "concepts/x.md", "content": fake}}, secret_scan)
    assert evaluate({"tool_input": {"file_path": WIKI_ROOT + "concepts/x.md", "content": "clean text"}}, secret_scan) is None
    assert evaluate({"tool_input": {"file_path": "/Users/isal/Workspaces/app/.env", "content": fake}}, secret_scan) is None
    assert evaluate({"tool_input": {"file_path": "/Users/isal/.claude/projects/p/memory/a.md",
                                    "edits": [{"new_string": "ok"}, {"new_string": fake}]}}, secret_scan)
    assert evaluate({"tool_input": {"file_path": WIKI_ROOT + "a.md", "content": "x"}}, scanner=None) is None
    print("selftest OK")
    return 0


def main(argv):
    if argv[:1] == ["selftest"]:
        return selftest()
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    reason = evaluate(payload)
    if reason:
        deny(reason)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
