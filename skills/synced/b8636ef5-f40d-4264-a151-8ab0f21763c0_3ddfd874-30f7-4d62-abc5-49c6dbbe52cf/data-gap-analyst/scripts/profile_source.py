"""
profile_source.py — Profiling modul untuk Mode A (live DB) dan Mode C (raw file)
Bagian dari skill `data-gap-analyst`.

Output: dict per-kolom dengan metrik standar yang dipakai oleh compute_gap.py.

Mode A — Live DB via SQLAlchemy (PostgreSQL, MySQL, BigQuery, Snowflake).
Mode C — Raw file (CSV/XLSX/Parquet/JSON) via pandas, chunked untuk file besar.

Anti-halusinasi: setiap metric di-tag dengan `source_query` (Mode A) atau
`source_file` (Mode C) supaya traceable.

Usage:
    python profile_source.py --mode=db --conn=postgresql://... --tables=orders,customers
    python profile_source.py --mode=file --path=./data.csv --output=./profile.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

# Lazy imports — only loaded when actually needed (keeps CLI startup fast).
# Required: pandas. Optional: sqlalchemy (Mode A), pyarrow (Parquet).

CHUNK_SIZE = 100_000
SAMPLE_THRESHOLD_ROWS = 10_000_000  # >10M baris → TABLESAMPLE
SAMPLE_PCT = 1  # TABLESAMPLE 1%


@dataclass
class ColumnProfile:
    """Metrik per-kolom yang dihitung untuk satu source."""
    column_name: str
    data_type: str
    row_count: int
    null_count: int
    null_ratio: float
    distinct_count: int
    min_value: Any = None
    max_value: Any = None
    mean: float | None = None
    median: float | None = None
    stddev: float | None = None
    top_values: list[tuple[Any, int]] = field(default_factory=list)
    avg_length: float | None = None  # untuk string
    source_query_or_file: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class TableProfile:
    """Metrik per-tabel + list kolom."""
    table_name: str
    row_count: int
    columns: list[ColumnProfile] = field(default_factory=list)
    constraints: dict = field(default_factory=dict)  # PK, FK, UNIQUE, CHECK
    indexes: list[dict] = field(default_factory=list)
    profiled_at: str = ""
    mode: str = ""
    source_identity: str = ""

    def to_dict(self) -> dict:
        return {
            "table_name": self.table_name,
            "row_count": self.row_count,
            "columns": [c.to_dict() for c in self.columns],
            "constraints": self.constraints,
            "indexes": self.indexes,
            "profiled_at": self.profiled_at,
            "mode": self.mode,
            "source_identity": self.source_identity,
        }


def profile_db(conn_str: str, tables: list[str] | None = None) -> list[TableProfile]:
    """Mode A — profile live DB via SQLAlchemy.

    Auto-discover all tables if `tables` is None.
    Uses TABLESAMPLE for tables >10M rows (catat sampling rate di output).
    """
    try:
        from sqlalchemy import create_engine, inspect, text
    except ImportError:
        print("ERROR: sqlalchemy diperlukan untuk Mode A. Install: pip install sqlalchemy",
              file=sys.stderr)
        sys.exit(1)

    engine = create_engine(conn_str)
    inspector = inspect(engine)
    profiled_at = datetime.now(timezone.utc).isoformat()
    source_identity = _redact_conn(conn_str)

    discovered_tables = tables or inspector.get_table_names()
    results: list[TableProfile] = []

    with engine.connect() as conn:
        for tbl in discovered_tables:
            row_count = conn.execute(text(f"SELECT COUNT(*) FROM {tbl}")).scalar() or 0
            use_sample = row_count > SAMPLE_THRESHOLD_ROWS
            sample_clause = f"TABLESAMPLE SYSTEM ({SAMPLE_PCT})" if use_sample else ""

            tbl_profile = TableProfile(
                table_name=tbl,
                row_count=row_count,
                profiled_at=profiled_at,
                mode="A",
                source_identity=source_identity,
            )

            cols = inspector.get_columns(tbl)
            for col in cols:
                cname = col["name"]
                ctype = str(col["type"])
                col_profile = _profile_column_db(conn, tbl, cname, ctype, sample_clause)
                tbl_profile.columns.append(col_profile)

            # Constraints (PK, FK, UNIQUE)
            tbl_profile.constraints = {
                "primary_key": inspector.get_pk_constraint(tbl),
                "foreign_keys": inspector.get_foreign_keys(tbl),
                "unique_constraints": inspector.get_unique_constraints(tbl),
                "check_constraints": inspector.get_check_constraints(tbl),
            }
            tbl_profile.indexes = inspector.get_indexes(tbl)

            results.append(tbl_profile)

    return results


def _profile_column_db(conn, table: str, column: str, dtype: str, sample_clause: str) -> ColumnProfile:
    """Hitung metrik untuk satu kolom via SQL."""
    from sqlalchemy import text

    base = f"FROM {table} {sample_clause}" if sample_clause else f"FROM {table}"
    query = f"""
        SELECT
            COUNT(*) AS total,
            COUNT(*) FILTER (WHERE {column} IS NULL) AS null_count,
            COUNT(DISTINCT {column}) AS distinct_count,
            MIN({column}::text) AS min_val,
            MAX({column}::text) AS max_val
        {base}
    """
    try:
        row = conn.execute(text(query)).fetchone()
    except Exception as e:
        # Fallback minimal jika type tidak support MIN/MAX cast
        query2 = f"SELECT COUNT(*) AS total, COUNT(*) FILTER (WHERE {column} IS NULL) AS null_count FROM {table}"
        row = conn.execute(text(query2)).fetchone()
        return ColumnProfile(
            column_name=column,
            data_type=dtype,
            row_count=row.total,
            null_count=row.null_count,
            null_ratio=row.null_count / row.total if row.total else 0.0,
            distinct_count=-1,  # unknown
            source_query_or_file=f"fallback: {query2}",
        )

    return ColumnProfile(
        column_name=column,
        data_type=dtype,
        row_count=row.total,
        null_count=row.null_count,
        null_ratio=row.null_count / row.total if row.total else 0.0,
        distinct_count=row.distinct_count,
        min_value=row.min_val,
        max_value=row.max_val,
        source_query_or_file=query.strip(),
    )


def profile_file(path: str | Path) -> TableProfile:
    """Mode C — profile raw file via pandas chunked untuk file besar."""
    try:
        import pandas as pd
    except ImportError:
        print("ERROR: pandas diperlukan untuk Mode C. Install: pip install pandas",
              file=sys.stderr)
        sys.exit(1)

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {path}")

    ext = path.suffix.lower()
    file_size_mb = path.stat().st_size / (1024 * 1024)
    profiled_at = datetime.now(timezone.utc).isoformat()

    if ext == ".csv":
        df = _read_csv_smart(path, file_size_mb)
    elif ext in (".xlsx", ".xls"):
        df = pd.read_excel(path)
    elif ext == ".parquet":
        df = pd.read_parquet(path)
    elif ext == ".json":
        df = pd.read_json(path, lines=path.read_text().lstrip().startswith("{"))
    else:
        raise ValueError(f"Format file tidak didukung: {ext}")

    tbl_profile = TableProfile(
        table_name=path.stem,
        row_count=len(df),
        profiled_at=profiled_at,
        mode="C",
        source_identity=str(path),
    )

    for col in df.columns:
        s = df[col]
        col_profile = ColumnProfile(
            column_name=str(col),
            data_type=str(s.dtype),
            row_count=len(s),
            null_count=int(s.isna().sum()),
            null_ratio=float(s.isna().sum() / len(s)) if len(s) else 0.0,
            distinct_count=int(s.nunique(dropna=True)),
            source_query_or_file=str(path),
        )

        non_null = s.dropna()
        if len(non_null) > 0:
            try:
                col_profile.min_value = _serialize(non_null.min())
                col_profile.max_value = _serialize(non_null.max())
            except Exception:
                pass

            if s.dtype.kind in "biufc":  # numeric
                col_profile.mean = float(non_null.mean())
                col_profile.median = float(non_null.median())
                col_profile.stddev = float(non_null.std())
            elif s.dtype == object:
                col_profile.avg_length = float(non_null.astype(str).str.len().mean())

            top = non_null.value_counts().head(10)
            col_profile.top_values = [(_serialize(v), int(c)) for v, c in top.items()]

        tbl_profile.columns.append(col_profile)

    return tbl_profile


def _read_csv_smart(path: Path, size_mb: float):
    """CSV reader yang chunk untuk file besar."""
    import pandas as pd
    if size_mb < 500:
        return pd.read_csv(path)
    # Chunked aggregation untuk file >500MB
    chunks = []
    for chunk in pd.read_csv(path, chunksize=CHUNK_SIZE):
        chunks.append(chunk)
    return pd.concat(chunks, ignore_index=True)


def _serialize(v: Any) -> Any:
    """Convert non-JSON-serializable values to string."""
    import pandas as pd
    if pd.isna(v):
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()
    if isinstance(v, (int, float, str, bool)):
        return v
    return str(v)


def _redact_conn(conn_str: str) -> str:
    """Hapus password dari connection string untuk logging."""
    import re
    return re.sub(r":[^:@/]+@", ":***@", conn_str)


def main():
    p = argparse.ArgumentParser(description="Profile source data untuk gap analysis.")
    p.add_argument("--mode", choices=["db", "file"], required=True)
    p.add_argument("--conn", help="Connection string untuk Mode A")
    p.add_argument("--tables", help="Comma-separated table names (Mode A)")
    p.add_argument("--path", help="File path (Mode C)")
    p.add_argument("--output", default="profile.json", help="Output JSON file")
    args = p.parse_args()

    if args.mode == "db":
        if not args.conn:
            p.error("--conn required for Mode A")
        tables = args.tables.split(",") if args.tables else None
        result = profile_db(args.conn, tables)
        data = [t.to_dict() for t in result]
    else:
        if not args.path:
            p.error("--path required for Mode C")
        result = profile_file(args.path)
        data = result.to_dict()

    Path(args.output).write_text(json.dumps(data, indent=2, default=str))
    print(f"Profile saved to: {args.output}")


if __name__ == "__main__":
    main()
