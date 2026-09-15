#!/usr/bin/env bash
# Thin launcher so the hook's stdin (PreToolUse JSON) reaches python untouched.
# Logic in guard-dangerous.py. Runs BEFORE rtk-rewrite so it sees the raw command.
exec python3 "$HOME/.claude/hooks/guard-dangerous.py"
