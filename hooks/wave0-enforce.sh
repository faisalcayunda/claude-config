#!/usr/bin/env bash
# Thin launcher so the hook's stdin (the UserPromptSubmit JSON payload) reaches
# python untouched. Logic lives in wave0-enforce.py.
exec python3 "$HOME/.claude/hooks/wave0-enforce.py"
