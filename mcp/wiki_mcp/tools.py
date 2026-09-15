"""Wiki MCP tool implementations: wiki_search, wiki_read, wiki_list."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

from wiki_mcp.config import DB_PATH, EMBED_MODEL, WIKI_ROOT

_model: SentenceTransformer | None = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def _has_schema(conn: sqlite3.Connection) -> bool:
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='chunks'"
    )
    return cur.fetchone() is not None


def wiki_search(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """Embed query and return nearest-neighbor wiki chunks via numpy cosine search."""
    include_meta = any(kw in query.lower() for kw in ("session", "log"))

    if not DB_PATH.exists():
        return []

    conn = _connect()
    try:
        if not _has_schema(conn):
            return []

        q_vec = _get_model().encode(query, normalize_embeddings=True).astype(np.float32)

        # Load all embeddings; corpus ~200 chunks — fits in memory easily
        rows = conn.execute(
            "SELECT e.chunk_id, e.embedding FROM embeddings e"
        ).fetchall()

        if not rows:
            return []

        chunk_ids = [r["chunk_id"] for r in rows]
        matrix = np.stack([
            np.frombuffer(r["embedding"], dtype=np.float32) for r in rows
        ])  # shape (N, 384)

        scores = matrix @ q_vec  # cosine sim (embeddings are normalized)
        top_indices = np.argsort(scores)[::-1][:top_k * 3]  # oversample for meta filter

        results = []
        for idx in top_indices:
            if len(results) >= top_k:
                break
            chunk_id = chunk_ids[idx]
            score = float(scores[idx])

            row = conn.execute(
                "SELECT page_id, title, type, tags, status, content FROM chunks WHERE id = ?",
                (chunk_id,),
            ).fetchone()
            if row is None:
                continue
            if not include_meta and row["type"] == "meta":
                continue

            excerpt = (row["content"] or "")[:300]
            results.append({
                "page_id": row["page_id"],
                "title": row["title"],
                "type": row["type"],
                "tags": row["tags"],
                "status": row["status"],
                "excerpt": excerpt,
                "score": score,
            })

        return results
    finally:
        conn.close()


def wiki_read(page_id: str) -> dict[str, Any]:
    """Return full content and metadata for a wiki page.

    page_id is a relative path from wiki root without the .md extension,
    e.g. 'concepts/cherry-picks'.
    """
    path = WIKI_ROOT / f"{page_id}.md"
    if not path.exists():
        raise FileNotFoundError(f"Wiki page not found: {page_id} (resolved: {path})")

    raw = path.read_text(encoding="utf-8")

    frontmatter: dict[str, Any] = {}
    content = raw

    if raw.startswith("---"):
        end = raw.find("---", 3)
        if end != -1:
            fm_block = raw[3:end].strip()
            content = raw[end + 3 :].strip()
            for line in fm_block.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    frontmatter[k.strip()] = v.strip().strip('"')

    title = frontmatter.get("title", page_id.split("/")[-1])

    return {
        "page_id": page_id,
        "title": title,
        "content": content,
        "frontmatter": frontmatter,
    }


def wiki_list(tag: str | None = None, type: str | None = None) -> list[dict[str, Any]]:
    """List wiki pages, optionally filtered by tag or type.

    Prefers DB metadata when the schema is present; falls back to parsing index.md.
    """
    if not DB_PATH.exists():
        return _list_from_index(tag=tag, type_filter=type)
    conn = _connect()
    try:
        if _has_schema(conn):
            return _list_from_db(conn, tag=tag, type_filter=type)
        return _list_from_index(tag=tag, type_filter=type)
    finally:
        conn.close()


def _list_from_db(
    conn: sqlite3.Connection,
    tag: str | None,
    type_filter: str | None,
) -> list[dict[str, Any]]:
    conditions = []
    params: list[Any] = []

    if type_filter:
        conditions.append("type = ?")
        params.append(type_filter)

    where = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    sql = f"SELECT DISTINCT page_id, title, type, tags, status FROM chunks {where} ORDER BY title"
    rows = conn.execute(sql, params).fetchall()

    results = []
    for row in rows:
        tags_raw: str = row["tags"] or ""
        page_tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
        if tag and tag not in page_tags:
            continue
        results.append(
            {
                "page_id": row["page_id"],
                "title": row["title"],
                "type": row["type"],
                "tags": page_tags,
                "status": row["status"],
            }
        )
    return results


def _list_from_index(
    tag: str | None,
    type_filter: str | None,
) -> list[dict[str, Any]]:
    index_path = WIKI_ROOT / "index.md"
    if not index_path.exists():
        return []

    pages: list[dict[str, Any]] = []
    text = index_path.read_text(encoding="utf-8")

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("- [["):
            continue
        inner_end = line.find("]]")
        if inner_end == -1:
            continue
        raw_link = line[4:inner_end]
        title = raw_link
        page_id = raw_link.lower().replace(" ", "-")

        dash_pos = line.find("—")
        status = ""
        if dash_pos != -1:
            trailing = line[dash_pos + 1 :].strip()
            for word in ("mature", "current", "evergreen", "developing", "shipped"):
                if word in trailing.lower():
                    status = word
                    break

        pages.append(
            {
                "page_id": page_id,
                "title": title,
                "type": "unknown",
                "tags": [],
                "status": status,
            }
        )

    if tag:
        pages = [p for p in pages if tag in p["tags"]]
    if type_filter:
        pages = [p for p in pages if p["type"] == type_filter]

    return pages
