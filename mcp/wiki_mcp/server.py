"""Wiki MCP server — stdio transport for Claude Desktop."""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from wiki_mcp.tools import wiki_list, wiki_read, wiki_search

mcp = FastMCP("wiki")


@mcp.tool()
def search(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """Search wiki pages by semantic similarity.

    Returns up to top_k results ordered by relevance. Each result includes
    page_id, title, type, tags, status, an excerpt (first 300 chars), and a
    cosine distance score (lower = more similar). Meta/log pages are excluded
    unless the query mentions 'session' or 'log'.
    """
    return wiki_search(query=query, top_k=top_k)


@mcp.tool()
def read(page_id: str) -> dict[str, Any]:
    """Read a wiki page by its relative path (no .md extension).

    Example page_id: 'concepts/cherry-picks', 'hot', 'index'.
    Returns page_id, title, full markdown content, and parsed frontmatter.
    Raises an error if the page does not exist.
    """
    return wiki_read(page_id=page_id)


@mcp.tool()
def list_pages(tag: str | None = None, type: str | None = None) -> list[dict[str, Any]]:
    """List wiki pages, optionally filtered by tag or type.

    Uses DB metadata when available; falls back to parsing index.md.
    Returns page_id, title, type, tags, and status for each page.
    """
    return wiki_list(tag=tag, type=type)


if __name__ == "__main__":
    mcp.run()
