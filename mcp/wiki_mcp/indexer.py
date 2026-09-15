"""Wiki semantic search indexer using plain sqlite3 + numpy cosine similarity."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

from wiki_mcp.config import CHUNK_LARGE, CHUNK_MAX_CHARS, CHUNK_SMALL, DB_PATH, EMBED_MODEL, SKIP_DIRS, SKIP_EXTENSIONS, WIKI_ROOT

_model: SentenceTransformer | None = None


def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def open_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS chunks (
            id TEXT PRIMARY KEY,
            page_id TEXT NOT NULL,
            title TEXT,
            type TEXT,
            tags TEXT,
            status TEXT,
            chunk_index INTEGER DEFAULT 0,
            content TEXT NOT NULL,
            updated TEXT
        );
        CREATE TABLE IF NOT EXISTS embeddings (
            chunk_id TEXT PRIMARY KEY,
            embedding BLOB NOT NULL
        );
    """)
    conn.commit()


def drop_schema(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS embeddings;
    """)
    conn.commit()


def parse_frontmatter(raw: str) -> tuple[dict[str, object], str]:
    """Frontmatter parsing is shared with ~/.claude/hooks/wiki_hooks.py so both read pages the same way."""
    import sys as _sys
    _sys.path.insert(0, "/Users/isal/.claude/hooks")
    import wiki_hooks

    meta: dict[str, object] = dict(wiki_hooks.parse_frontmatter(raw))
    end = raw.find("\n---", 3) if raw.startswith("---") else -1
    body = raw[end + 4:].lstrip("\n") if end != -1 else raw
    tags = meta.get("tags")
    meta["tags"] = json.dumps(tags if isinstance(tags, list) else ([tags] if tags else []))
    return meta, body


def split_chunks(body: str, byte_size: int) -> list[str]:
    if byte_size < CHUNK_SMALL:
        text = body.strip()
        return [text] if text else []

    h2_pattern = re.compile(r"^## .+", re.MULTILINE)
    splits = list(h2_pattern.finditer(body))

    if not splits:
        text = body.strip()
        return [text] if text else []

    sections: list[str] = []
    boundaries = [m.start() for m in splits]

    # Text before first H2
    preamble = body[: boundaries[0]].strip()
    if preamble:
        sections.append(preamble)

    for i, start in enumerate(boundaries):
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(body)
        section = body[start:end].strip()
        if not section:
            continue
        if byte_size > CHUNK_LARGE and len(section) > CHUNK_MAX_CHARS:
            for offset in range(0, len(section), CHUNK_MAX_CHARS):
                sub = section[offset : offset + CHUNK_MAX_CHARS].strip()
                if sub:
                    sections.append(sub)
        else:
            sections.append(section)

    return sections


def embed(text: str) -> bytes:
    model = get_model()
    vector = model.encode(text, normalize_embeddings=True)
    return np.array(vector, dtype=np.float32).tobytes()


def page_id_from_path(path: Path) -> str:
    return str(path.relative_to(WIKI_ROOT).with_suffix(""))


def should_skip(path: Path) -> bool:
    if path.suffix in SKIP_EXTENSIONS:
        return True
    for part in path.relative_to(WIKI_ROOT).parts[:-1]:
        if part in SKIP_DIRS:
            return True
    return False


def collect_pages() -> list[Path]:
    return [
        p
        for p in WIKI_ROOT.rglob("*.md")
        if p.is_file() and not should_skip(p)
    ]


def already_indexed(conn: sqlite3.Connection, page_id: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM chunks WHERE page_id = ? LIMIT 1", (page_id,)
    ).fetchone()
    return row is not None


def delete_page_chunks(conn: sqlite3.Connection, page_id: str) -> None:
    ids = [
        row[0]
        for row in conn.execute(
            "SELECT id FROM chunks WHERE page_id = ?", (page_id,)
        )
    ]
    for chunk_id in ids:
        conn.execute("DELETE FROM embeddings WHERE chunk_id = ?", (chunk_id,))
    conn.execute("DELETE FROM chunks WHERE page_id = ?", (page_id,))


def _embedding_header(meta: dict[str, object]) -> str:
    aliases = meta.get("aliases")
    alias_text = "; ".join(aliases) if isinstance(aliases, list) else str(aliases or "")
    parts = [str(meta.get("title") or ""), alias_text, str(meta.get("description") or "")]
    return ". ".join(p for p in parts if p) + "\n"


def _insert_chunk(
    conn: sqlite3.Connection,
    chunk_id: str,
    page_id: str,
    meta: dict[str, object],
    chunk_index: int,
    content: str,
) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO chunks
            (id, page_id, title, type, tags, status, chunk_index, content, updated)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            chunk_id,
            page_id,
            meta.get("title"),
            meta.get("type"),
            meta.get("tags"),
            meta.get("status"),
            chunk_index,
            content,
            meta.get("updated"),
        ),
    )
    conn.execute(
        "INSERT OR REPLACE INTO embeddings (chunk_id, embedding) VALUES (?, ?)",
        (chunk_id, embed(_embedding_header(meta) + content)),
    )


def index_page(conn: sqlite3.Connection, path: Path) -> int:
    raw = path.read_text(encoding="utf-8", errors="replace")
    byte_size = path.stat().st_size
    meta, body = parse_frontmatter(raw)
    page_id = page_id_from_path(path)
    chunks = split_chunks(body, byte_size)

    delete_page_chunks(conn, page_id)

    for i, content in enumerate(chunks):
        chunk_id = f"{page_id}::{i}"
        _insert_chunk(conn, chunk_id, page_id, meta, i, content)

    conn.commit()
    return len(chunks)


def run_index(rebuild: bool = False) -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = open_db()

    if rebuild:
        drop_schema(conn)
    create_schema(conn)

    pages = collect_pages()
    total = len(pages)
    chunk_count = 0

    for n, path in enumerate(pages, 1):
        page_id = page_id_from_path(path)
        if not rebuild and already_indexed(conn, page_id):
            continue
        chunks_written = index_page(conn, path)
        chunk_count += chunks_written
        print(f"Indexed {n}/{total}: {page_id}")

    conn.close()
    print(f"Done. {chunk_count} chunks from {total} pages.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Index wiki pages into sqlite-vec.")
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Drop and recreate the index from scratch.",
    )
    args = parser.parse_args()
    run_index(rebuild=args.rebuild)


if __name__ == "__main__":
    main()
