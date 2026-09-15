#!/usr/bin/env bash
# Async wiki semantic-index refresh — keeps mcp/wiki.db in sync with wiki/*.md.
# Root cause it fixes: server.py never launches watcher.py, and watcher.py was
# broken (imported SKIP_SUFFIXES), so the index never auto-updated. This rebuilds
# ONLY when a wiki page changed since the last index, in the background, non-blocking.
ROOT="/Users/isal/.claude"
DB="$ROOT/mcp/wiki.db"
WIKI="$ROOT/wiki"
PY="$ROOT/mcp/.venv/bin/python"
LOG="$ROOT/mcp/reindex.log"

# Drain stdin (Stop hook passes JSON); not needed.
cat >/dev/null 2>&1 || true

[ -x "$PY" ] || exit 0
[ -d "$WIKI" ] || exit 0

need=0
if [ ! -f "$DB" ]; then
  need=1
else
  newer="$(find "$WIKI" -name '*.md' -newer "$DB" \
    -not -path '*/templates/*' -not -path '*/canvases/*' -print -quit 2>/dev/null || true)"
  [ -n "$newer" ] && need=1
fi
[ "$need" -eq 1 ] || exit 0

# Detached rebuild; never blocks session end.
( cd "$ROOT/mcp" && nohup "$PY" -m wiki_mcp.indexer --rebuild >>"$LOG" 2>&1 & ) >/dev/null 2>&1
exit 0
