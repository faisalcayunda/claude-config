#!/usr/bin/env bash
# Guard: no-op if wiki context is not yet populated.
HOT_MD="/Users/isal/.claude/wiki/hot.md"
[ -f "$HOT_MD" ] || exit 0
printf '{"hookSpecificOutput":{"hookEventName":"PostCompact","additionalContext":"Context compaction occurred. Re-read /Users/isal/.claude/wiki/hot.md silently now to restore recent wiki context. Do not announce this action."}}\n'
