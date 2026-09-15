# wiki-mcp

A lightweight local MCP server that indexes `~/.claude/wiki/` and exposes semantic search, read, and list tools to Claude Desktop over stdio. It embeds wiki pages with `all-MiniLM-L6-v2` and stores vectors in a local SQLite database — no external services required.

## Requirements

- macOS
- Python 3.12+
- `~/.claude/wiki/` populated with Obsidian markdown pages
- ~420 MB disk space for the embedding model (downloaded once on first run)

## Install

```bash
cd ~/.claude/mcp && bash install.sh
```

The script:
1. Creates a `.venv` virtualenv and installs dependencies
2. Runs a full index rebuild (`wiki.db`)
3. Prints the Claude Desktop config snippet to add

Then add the printed JSON to your Claude Desktop config and restart Claude Desktop.

## Claude Desktop Config

File: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "wiki": {
      "command": "/Users/isal/.claude/mcp/.venv/bin/python",
      "args": ["-m", "wiki_mcp"]
    }
  }
}
```

## Tools

### `search(query, top_k=5)`

Semantic search over indexed wiki pages. Returns up to `top_k` results ordered by relevance, each with `page_id`, `title`, `type`, `tags`, `status`, an excerpt (first 300 chars), and a cosine distance score (lower = more similar). Meta/log pages are excluded unless the query mentions `session` or `log`.

### `read(page_id)`

Read the full markdown content of a page by its path relative to the wiki root, without the `.md` extension.

```
read("concepts/cherry-picks")
read("hot")
read("index")
```

Returns `page_id`, `title`, full markdown `content`, and parsed frontmatter.

### `list_pages(tag=None, type=None)`

List all wiki pages. Optionally filter by `tag` or `type` (uses DB metadata when available, falls back to `index.md`). Returns `page_id`, `title`, `type`, `tags`, and `status` per page.

## Re-indexing

**Incremental** (new/modified files only):

```bash
python -m wiki_mcp.indexer
```

**Full rebuild** (drop and re-embed everything):

```bash
python -m wiki_mcp.indexer --rebuild
```

**Auto-watch** (re-indexes on file change):

```bash
python -m wiki_mcp.watcher
```

## Notes

- The embedding model (`all-MiniLM-L6-v2`, 384-dim) is downloaded from HuggingFace on first run (~420 MB). Set `HF_TOKEN` to suppress the rate-limit warning.
- No auth is needed — the server runs over stdio and is scoped to the Claude Desktop process.
- `wiki.db` lives at `~/.claude/mcp/wiki.db` (typically a few MB for ~200 chunks).
- Directories `templates/` and `canvases/` and files with extensions `.canvas`, `.png`, `.gif`, `.svg`, `.base`, `.json` are skipped during indexing.
