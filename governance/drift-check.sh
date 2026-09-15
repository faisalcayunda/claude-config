#!/usr/bin/env bash
# Deterministic config drift-check. NO LLM, fast (<1s). Silent when clean;
# prints a short WARN banner (into SessionStart context) only when something drifted.
# Catches the exact rot this config suffered: leaked secrets, doc-vs-reality model
# claims, stale wiki index, loose file perms, unbounded growth.
ROOT="/Users/isal/.claude"
issues=()

# A) Inline secrets in MCP config (report location + count, never the value)
for f in "$ROOT/.mcp.json" "$HOME/.claude.json"; do
  [ -f "$f" ] || continue
  dsn=$(grep -oE '://[^:@/"]+:[^@/"]+@' "$f" 2>/dev/null | wc -l | tr -d ' ')
  key=$(grep -oiE '"(api[_-]?key|token|z_ai_api_key|secret|password)"[[:space:]]*:[[:space:]]*"[^"$][^"]{6,}"' "$f" 2>/dev/null | wc -l | tr -d ' ')
  n=$((dsn + key))
  [ "$n" -gt 0 ] && issues+=("CRITICAL: $n inline secret(s) in $(basename "$f") — rotate + move to \${ENV} (see audit TIER 0)")
done

# B) .mcp.json world/group readable (should be 600)
if [ -f "$ROOT/.mcp.json" ]; then
  perm=$(stat -f '%Lp' "$ROOT/.mcp.json" 2>/dev/null || stat -c '%a' "$ROOT/.mcp.json" 2>/dev/null)
  case "$perm" in 600|400) ;; *) issues+=("WARN: .mcp.json perms=$perm (want 600) — chmod 600 ~/.claude/.mcp.json");; esac
fi

# C) Orchestrator model doc-vs-reality drift
if [ -f "$ROOT/CLAUDE.md" ]; then
  has_model=$(grep -c '"model"' "$ROOT/settings.json" 2>/dev/null)
  if [ "${has_model:-0}" -eq 0 ] && grep -qiE 'orchestrator.*sonnet \(settings|settings\.json model: sonnet|running on Sonnet' "$ROOT/CLAUDE.md" 2>/dev/null; then
    issues+=("WARN: CLAUDE.md still claims a Sonnet orchestrator but settings.json has no model key")
  fi
fi

# D) Wiki semantic index stale (a page newer than the db)
db="$ROOT/mcp/wiki.db"
if [ -f "$db" ]; then
  newer=$(find "$ROOT/wiki" -name '*.md' -newer "$db" -not -path '*/templates/*' -not -path '*/canvases/*' -print -quit 2>/dev/null)
  [ -n "$newer" ] && issues+=("WARN: wiki index stale — run: cd ~/.claude/mcp && ./.venv/bin/python -m wiki_mcp.indexer --rebuild")
fi

# E) Agent count vs whatever CLAUDE.md claims
if [ -f "$ROOT/CLAUDE.md" ]; then
  actual=$(ls "$ROOT"/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
  claim=$(grep -oE '[0-9]+ agents' "$ROOT/CLAUDE.md" 2>/dev/null | grep -oE '[0-9]+' | head -1)
  [ -n "$claim" ] && [ "$claim" != "$actual" ] && issues+=("WARN: CLAUDE.md says $claim agents, actual is $actual")
fi

# F) Unbounded growth
ll="$ROOT/lessons_learned.md"
[ -f "$ll" ] && kb=$(( $(wc -c < "$ll") / 1024 )) && [ "$kb" -gt 200 ] && issues+=("INFO: lessons_learned.md ${kb}KB — consider folding/archiving")

if [ ${#issues[@]} -gt 0 ]; then
  printf '\n⚠ CONFIG DRIFT (%d) — from ~/.claude/governance/drift-check.sh:\n' "${#issues[@]}"
  for i in "${issues[@]}"; do printf '  - %s\n' "$i"; done
  printf '\n'
fi
exit 0
