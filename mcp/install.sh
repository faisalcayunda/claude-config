#!/usr/bin/env bash
# chmod +x /Users/isal/.claude/mcp/install.sh
set -e

VENV="/Users/isal/.claude/mcp/.venv"
PROJECT="/Users/isal/.claude/mcp"

python3 -m venv "$VENV"

"$VENV/bin/pip" install -e "$PROJECT" --quiet

"$VENV/bin/python" -m wiki_mcp.indexer --rebuild

cat <<'EOF'

Add this to your Claude Desktop config (~/Library/Application Support/Claude/claude_desktop_config.json):

{
  "mcpServers": {
    "wiki": {
      "command": "/Users/isal/.claude/mcp/.venv/bin/python",
      "args": ["-m", "wiki_mcp"]
    }
  }
}

EOF

echo "Done. Restart Claude Desktop to activate."
