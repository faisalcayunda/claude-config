#!/usr/bin/env python3
"""PreToolUse Bash guard — the HARD enforcement layer.

CLAUDE.md is advisory and the model can forget it. This hook cannot be forgotten:
it fires on every Bash call. It maps the user's non-negotiable rules
(git writes + destructive ops need explicit in-session approval; catastrophic
commands never) to real platform decisions: deny / ask.

Output contract (verified against this install's hooks):
  {"hookSpecificOutput":{"hookEventName":"PreToolUse",
   "permissionDecision":"deny"|"ask","permissionDecisionReason":"..."}}
Silent exit 0 = no opinion (command proceeds to other hooks / normal perms).
"""
import json
import re
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

if data.get("tool_name") not in (None, "Bash"):
    sys.exit(0)

cmd = ((data.get("tool_input") or {}).get("command") or "").strip()
if not cmd:
    sys.exit(0)


def decide(decision: str, reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason,
    }}))
    sys.exit(0)


# 1) CATASTROPHIC -> deny outright (run it yourself if you truly mean it)
DENY = [
    (r'\brm\s+-[a-z]*r[a-z]*f[a-z]*\s+(/|/\*|~|\$HOME|\.\.)(\s|$|;|&)', "rm -rf on / ~ $HOME or .."),
    (r'\brm\s+-[a-z]*f[a-z]*r[a-z]*\s+(/|/\*|~|\$HOME)(\s|$|;|&)', "rm -fr on / or $HOME"),
    (r':\s*\(\s*\)\s*\{', "fork bomb"),
    (r'\bmkfs\b', "filesystem format (mkfs)"),
    (r'\bdd\b[^\n]*\bof=/dev/', "dd to a raw device"),
    (r'>\s*/dev/(sd|nvme|disk)', "overwrite a raw disk"),
    (r'\bchmod\s+-R\s+777\s+/(\s|$)', "recursive 777 on /"),
    # Secrets reach tools through the environment (Infisical wrapper), so a bare dump prints them.
    (r'(^|[;&|(]\s*)(env|printenv|set)\s*($|[;&|)])', "bare env/printenv/set dumps environment secrets"),
    (r'(^|[;&|(]\s*)(export\s+-p|declare\s+-[a-z]*x[a-z]*)\s*($|[;&|)])', "export -p / declare -x dumps environment secrets"),
]
for pat, why in DENY:
    if re.search(pat, cmd, re.IGNORECASE):
        decide("deny", f"BLOCKED (catastrophic): {why}. Tidak dijalankan. Lakukan manual bila benar-benar perlu.")

# 2) NEEDS EXPLICIT APPROVAL -> ask (forces a human yes/no = "in-session approval")
ASK = [
    (r'\bgit\s+push\b[^\n]*(--force|--force-with-lease|\s-f\b)', "git FORCE push"),
    (r'\bgit\s+push\b[^\n]*(--delete|\s:\S)', "delete remote branch"),
    (r'\bgit\s+push\b', "git push"),
    (r'\bgit\s+commit\b', "git commit"),
    (r'\bgit\s+reset\s+--hard\b', "git reset --hard"),
    (r'\bgit\s+rebase\b', "git rebase"),
    (r'\bgit\s+clean\s+-[a-z]*f', "git clean -f"),
    (r'\bgit\s+branch\s+-D\b', "git branch -D (force delete)"),
    (r'\brm\s+-[a-z]*r[a-z]*f|\brm\s+-[a-z]*f[a-z]*r', "rm -rf"),
    (r'\b(drop|truncate)\s+(table|database|schema)\b', "destructive SQL (DROP/TRUNCATE)"),
    (r'\bterraform\s+destroy\b', "terraform destroy"),
    (r'\bkubectl\s+delete\b', "kubectl delete"),
    (r'\bdocker\s+system\s+prune\b', "docker system prune"),
]
for pat, why in ASK:
    if re.search(pat, cmd, re.IGNORECASE):
        decide("ask", f"Perlu persetujuan eksplisit: {why}. (Aturan: git-write & operasi merusak harus disetujui in-session.)")

sys.exit(0)
