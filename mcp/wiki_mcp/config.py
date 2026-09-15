from pathlib import Path
from typing import Final

WIKI_ROOT: Final[Path] = Path("/Users/isal/.claude/wiki")
DB_PATH: Final[Path] = Path("/Users/isal/.claude/mcp/wiki.db")

EMBED_MODEL: Final[str] = "paraphrase-multilingual-MiniLM-L12-v2"  # Indonesian prompts vs English pages (Q26)
EMBED_DIM: Final[int] = 384

DEFAULT_TOP_K: Final[int] = 5

SKIP_DIRS: Final[set[str]] = {"templates", "canvases"}
SKIP_EXTENSIONS: Final[set[str]] = {".canvas", ".png", ".gif", ".svg", ".base", ".json"}

CHUNK_SMALL: Final[int] = 3000
CHUNK_LARGE: Final[int] = 10000
CHUNK_MAX_CHARS: Final[int] = 6000
