"""File watcher that keeps the sqlite-vec wiki index up to date."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from watchfiles import awatch, Change

from wiki_mcp.indexer import (
    WIKI_ROOT,
    DB_PATH,
    SKIP_DIRS,
    open_db,
    create_schema,
    index_page,
    delete_page_chunks,
    page_id_from_path,
    should_skip,
)


def _handle_change(change_type: Change, raw_path: str) -> None:
    path = Path(raw_path)

    if path.suffix != ".md":
        return
    if not path.is_relative_to(WIKI_ROOT):
        return
    if should_skip(path):
        return

    page_id = page_id_from_path(path)

    conn = open_db()
    create_schema(conn)

    if change_type == Change.deleted or not path.exists():
        delete_page_chunks(conn, page_id)
        conn.commit()
        conn.close()
        print(f"Removed: {page_id}")
        return

    index_page(conn, path)
    conn.close()
    print(f"Re-indexed: {page_id}")


async def watch() -> None:
    print(f"Watching {WIKI_ROOT} — Ctrl+C to stop.")
    async for changes in awatch(WIKI_ROOT):
        for change_type, raw_path in changes:
            try:
                _handle_change(change_type, raw_path)
            except Exception as exc:
                print(f"Error processing {raw_path}: {exc}", file=sys.stderr)


def main() -> None:
    try:
        asyncio.run(watch())
    except KeyboardInterrupt:
        print("Watcher stopped.")


if __name__ == "__main__":
    main()
