#!/usr/bin/env python3
"""
profile_dataset.py
==================

Hitung metrik profiling deterministik dari sebuah dataset (CSV/XLSX/Parquet/JSON/JSONL).
Output: dua file JSON di direktori output yang akan dibaca oleh skill data-profiling-baseline
untuk ditambahi reasoning LLM (kategori, outlier, missing pattern, leakage, dst.) dan
ditulis ulang sebagai CSV per-kolom + Markdown report final.

Penggunaan:

    python profile_dataset.py <input-file> --out <output-dir> \\
        [--sheet <name-or-index>] [--encoding <enc>] [--delimiter <char>] \\
        [--sample-rows <n>] [--no-na-tokens]

Catatan:
- Tidak melakukan sampling default — profil dihitung pada seluruh baris.
- Untuk XLSX, default sheet pertama. Pakai --sheet untuk pilih sheet lain.
- "NA tokens" seperti "NA", "N/A", "-", "null", "NaN", "TBD", "" dianggap null
  (kecuali bila --no-na-tokens diaktifkan).
- Sample value diambil 10 nilai non-null pertama + 5 nilai unik teratas (frekuensi).

Hasil di <output-dir>:
- _dataset_meta.json   → ringkasan level dataset
- _profile_raw.json    → metrik per kolom (deterministik) + sample value untuk LLM
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import numpy as np

# Token yang umum dipakai untuk merepresentasikan null tetapi disimpan sebagai string.
DEFAULT_NA_TOKENS = {
    "", " ", "NA", "N/A", "n/a", "na", "NaN", "nan", "NULL", "null", "None",
    "none", "-", "--", "TBD", "tbd", "?", "#N/A", "#NA", "#NULL!", "missing",
}


def _read_dataset(path: Path, sheet: str | int | None, encoding: str | None,
                  delimiter: str | None, na_tokens: set[str]) -> pd.DataFrame:
    """Baca dataset adaptif berdasarkan ekstensi."""
    suffix = path.suffix.lower()
    na_list = sorted(na_tokens) if na_tokens else None

    if suffix == ".csv":
        # Coba beberapa encoding umum jika tidak diset.
        encodings = [encoding] if encoding else ["utf-8", "utf-8-sig", "latin-1", "cp1252"]
        for enc in encodings:
            try:
                read_kwargs: dict[str, Any] = {
                    "encoding": enc,
                    "na_values": na_list,
                    "keep_default_na": True,
                }
                if delimiter:
                    read_kwargs.update({"sep": delimiter, "engine": "c", "low_memory": False})
                else:
                    # Python engine wajib untuk auto-detect delimiter; tidak support low_memory.
                    read_kwargs.update({"sep": None, "engine": "python"})
                return pd.read_csv(path, **read_kwargs)
            except (UnicodeDecodeError, pd.errors.ParserError):
                continue
        raise RuntimeError(f"Gagal membaca {path} dengan encoding apapun.")

    if suffix in {".xlsx", ".xls", ".xlsm"}:
        sheet_arg = sheet if sheet is not None else 0
        try:
            sheet_arg = int(sheet_arg)
        except (TypeError, ValueError):
            pass
        return pd.read_excel(path, sheet_name=sheet_arg, na_values=na_list, keep_default_na=True)

    if suffix == ".parquet":
        return pd.read_parquet(path)

    if suffix == ".json":
        return pd.read_json(path)

    if suffix == ".jsonl":
        return pd.read_json(path, lines=True)

    raise ValueError(f"Ekstensi tidak didukung: {suffix}. Pakai CSV/XLSX/Parquet/JSON/JSONL.")


def _is_numeric_dtype(s: pd.Series) -> bool:
    return pd.api.types.is_numeric_dtype(s) and not pd.api.types.is_bool_dtype(s)


def _is_string_dtype(s: pd.Series) -> bool:
    return pd.api.types.is_string_dtype(s) or s.dtype == object


def _safe_float(x: Any) -> float | None:
    """Konversi numpy/pandas scalar → python float; nan/inf → None."""
    if x is None:
        return None
    try:
        f = float(x)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return f


def _to_jsonable(v: Any) -> Any:
    """Pastikan nilai bisa diserialize JSON."""
    if v is None:
        return None
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        f = float(v)
        return None if (math.isnan(f) or math.isinf(f)) else f
    if isinstance(v, (np.bool_,)):
        return bool(v)
    if isinstance(v, (pd.Timestamp,)):
        return v.isoformat()
    if pd.isna(v):
        return None
    return str(v) if not isinstance(v, (str, int, float, bool)) else v


_BOOLEAN_NAME_PREFIXES = ("is_", "has_", "can_", "should_", "allow_", "must_")
_ENUM_NAME_TOKENS = (
    "kode_", "_kode", "status", "tipe", "type_", "_type",
    "jenis", "kategori_", "category", "level", "tier", "golongan", "kelas_",
)


def _classify_numeric_subtype(name: str, s: pd.Series, total_filled: int, count_unique: int) -> dict:
    """Klasifikasi numeric_subtype + outlier_eligible.

    Mengembalikan dict dengan 3 field:
      - numeric_subtype: 'continuous'/'boolean-flag'/'fk-categorical'/'enum-numeric'/'id-sequence'/'n_a'
      - outlier_eligible: True hanya bila subtype 'continuous'
      - subtype_rationale: 1 kalimat alasan klasifikasi (untuk LLM downstream)

    Pohon keputusan top-down — pilih subtype pertama yang cocok. Lihat
    metrics_definitions.md > "Numeric Subtype Classification" untuk aturan
    lengkap.
    """
    if not _is_numeric_dtype(s) or total_filled == 0:
        return {"numeric_subtype": "n_a", "outlier_eligible": False, "subtype_rationale": ""}

    non_null = s.dropna()
    name_l = (name or "").lower()
    cardinality_ratio = count_unique / total_filled if total_filled else 0
    unique_vals = set(non_null.unique().tolist()) if count_unique <= 5 else None

    # 1. boolean-flag
    if count_unique <= 2 and (
        any(name_l.startswith(p) for p in _BOOLEAN_NAME_PREFIXES)
        or (unique_vals is not None and unique_vals.issubset({0, 1, 0.0, 1.0, True, False}))
    ):
        return {
            "numeric_subtype": "boolean-flag",
            "outlier_eligible": False,
            "subtype_rationale": (
                f"distinct_count={count_unique} dengan nilai ⊂ {{0,1,true,false}}"
                + (f" dan nama diawali boolean-prefix" if any(name_l.startswith(p) for p in _BOOLEAN_NAME_PREFIXES) else "")
            ),
        }

    # 2. id-sequence
    if (name_l == "id" or name_l.endswith("_pk") or name_l.endswith("_seq")) and cardinality_ratio >= 0.95:
        try:
            mn = float(non_null.min()); mx = float(non_null.max())
            range_ratio = (mx - mn + 1) / total_filled if total_filled else 0
            if 0.95 <= range_ratio <= 1.5:
                return {
                    "numeric_subtype": "id-sequence",
                    "outlier_eligible": False,
                    "subtype_rationale": (
                        f"nama '{name}' + cardinality_ratio={cardinality_ratio:.2f} "
                        f"+ range_ratio={range_ratio:.2f} (selaras dengan running sequence)"
                    ),
                }
        except Exception:
            pass

    # 3. fk-categorical or fk-likely (any *_id integer-valued column that isn't already an
    #    id-sequence above falls here — IQR on FK values is never meaningful regardless of
    #    cardinality). Note: SQL nullable integers often arrive as float64 in pandas because
    #    NaN forces a float upcast; we still treat them as FK if their non-null values are
    #    integer-valued.
    is_int_valued = pd.api.types.is_integer_dtype(s) or (
        pd.api.types.is_float_dtype(s) and len(non_null) > 0
        and bool(((non_null - non_null.astype("int64", errors="ignore")).abs() < 1e-9).all())
    )
    if name_l.endswith("_id") and name_l != "id" and is_int_valued:
        subtype_label = "fk-categorical" if cardinality_ratio < 0.5 else "fk-categorical"
        rationale_suffix = (
            f"cardinality_ratio={cardinality_ratio:.3f} (banyak baris share FK yang sama)"
            if cardinality_ratio < 0.5
            else f"cardinality_ratio={cardinality_ratio:.3f} tinggi — kemungkinan FK 1:1 atau ID-like"
        )
        return {
            "numeric_subtype": subtype_label,
            "outlier_eligible": False,
            "subtype_rationale": (
                f"nama berakhiran '_id' (selain 'id' sendiri) + tipe integer → FK; "
                + rationale_suffix
            ),
        }

    # 4. enum-numeric
    if count_unique <= 20 and cardinality_ratio < 0.05 and any(tok in name_l for tok in _ENUM_NAME_TOKENS):
        return {
            "numeric_subtype": "enum-numeric",
            "outlier_eligible": False,
            "subtype_rationale": (
                f"distinct_count={count_unique} + cardinality_ratio={cardinality_ratio:.3f} "
                f"+ nama mengandung token enum"
            ),
        }

    # 5. continuous (default)
    return {
        "numeric_subtype": "continuous",
        "outlier_eligible": True,
        "subtype_rationale": "tidak cocok kriteria boolean-flag/fk-categorical/enum-numeric/id-sequence",
    }


def _cardinality_level(unique: int, total_filled: int) -> str:
    """Heuristik kasar — final interpretasi tetap dilakukan LLM.

    Aturan:
    - is_unique (semua baris unik) → High, tanpa pandang ukuran absolut.
      Kunci natural seperti NIK/NPSN/order_id harus selalu High.
    - Ratio ≥ 50% → High (mendekati kunci natural).
    - Ratio < 2% atau jumlah unik ≤ 20 → Low (kandidat kategori).
    - Sisanya Medium.
    """
    if total_filled == 0:
        return "Low"
    if unique == total_filled:
        return "High"
    ratio = unique / total_filled
    if ratio >= 0.5:
        return "High"
    if unique <= 20 or ratio < 0.02:
        return "Low"
    return "Medium"


def _profile_column(name: str, s: pd.Series) -> dict:
    total_record = int(len(s))
    total_filled = int(s.notna().sum())
    pct_not_null = (total_filled / total_record * 100) if total_record else 0.0
    count_unique = int(s.nunique(dropna=True))
    is_unique = bool(count_unique == total_filled and total_filled > 0)

    subtype_info = _classify_numeric_subtype(name, s, total_filled, count_unique)

    profile: dict[str, Any] = {
        "column_name": name,
        "data_type": str(s.dtype),
        "total_record": total_record,
        "total_filled_record": total_filled,
        "pct_not_null": round(pct_not_null, 2),
        "count_unique": count_unique,
        "is_unique": is_unique,
        "cardinality_level": _cardinality_level(count_unique, total_filled),
        # Numeric subtype classification — kontinu vs kategorikal (boolean-flag /
        # fk-categorical / enum-numeric / id-sequence). Field outlier_eligible
        # menjadi guard supaya metode statistik dispersi (IQR/3σ/skew) tidak
        # diterapkan ke subtype kategoris. Lihat references/metrics_definitions.md
        # sub-bagian "Numeric Subtype Classification".
        "numeric_subtype": subtype_info["numeric_subtype"],
        "outlier_eligible": subtype_info["outlier_eligible"],
        "numeric_subtype_rationale": subtype_info["subtype_rationale"],
        "example_value": None,
        "sample_non_null": [],
        "top_values": [],
        "min_value": None,
        "max_value": None,
        "mean": None,
        "median": None,
        "std_dev": None,
        "p25": None,
        "p50": None,
        "p75": None,
        "max_length": None,
        "min_length": None,
        "avg_length": None,
    }

    non_null = s.dropna()
    if total_filled == 0:
        return profile

    profile["example_value"] = _to_jsonable(non_null.iloc[0])
    profile["sample_non_null"] = [_to_jsonable(v) for v in non_null.head(10).tolist()]

    # Top values — frekuensi tertinggi (untuk LLM nalar kategori).
    try:
        vc = non_null.value_counts(dropna=True).head(10)
        profile["top_values"] = [
            {"value": _to_jsonable(idx), "count": int(cnt)} for idx, cnt in vc.items()
        ]
    except TypeError:
        # Beberapa tipe (mis. dict/list) tidak hashable.
        profile["top_values"] = []

    if _is_numeric_dtype(s):
        desc = non_null.describe()
        profile["min_value"] = _safe_float(desc.get("min"))
        profile["max_value"] = _safe_float(desc.get("max"))
        profile["mean"] = round(_safe_float(desc.get("mean")) or 0, 4) if desc.get("mean") is not None else None
        profile["median"] = _safe_float(non_null.median())
        profile["std_dev"] = _safe_float(non_null.std(ddof=1)) if total_filled > 1 else None
        profile["p25"] = _safe_float(desc.get("25%"))
        profile["p50"] = _safe_float(desc.get("50%"))
        profile["p75"] = _safe_float(desc.get("75%"))
    elif _is_string_dtype(s):
        # Pakai stringified length untuk semua nilai non-null.
        lengths = non_null.astype(str).str.len()
        profile["max_length"] = int(lengths.max())
        profile["min_length"] = int(lengths.min())
        profile["avg_length"] = round(float(lengths.mean()), 2)

    return profile


def _dataset_meta(df: pd.DataFrame, source_path: Path, sheet: Any) -> dict:
    total_rows = int(len(df))
    total_cols = int(df.shape[1])
    total_cells = total_rows * total_cols
    null_cells = int(df.isna().sum().sum())
    overall_missing_pct = (null_cells / total_cells * 100) if total_cells else 0.0
    duplicate_rows = int(df.duplicated().sum())
    dtype_map = {col: str(dtype) for col, dtype in df.dtypes.items()}
    return {
        "source_file": str(source_path.name),
        "source_path": str(source_path.resolve()),
        "sheet": sheet,
        "total_rows": total_rows,
        "total_columns": total_cols,
        "duplicate_rows": duplicate_rows,
        "overall_missing_pct": round(overall_missing_pct, 2),
        "dtype_map": dtype_map,
        "column_order": list(df.columns),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Hitung metrik profiling deterministik dari dataset.")
    p.add_argument("input", help="Path ke file dataset (CSV/XLSX/Parquet/JSON/JSONL).")
    p.add_argument("--out", required=True, help="Direktori output untuk JSON hasil profiling.")
    p.add_argument("--sheet", default=None, help="Nama atau index sheet (XLSX). Default: 0.")
    p.add_argument("--encoding", default=None, help="Encoding (CSV). Auto-detect jika tidak diset.")
    p.add_argument("--delimiter", default=None, help="Delimiter eksplisit (CSV). Auto-detect jika tidak diset.")
    p.add_argument("--no-na-tokens", action="store_true",
                   help="Jangan treat token seperti 'NA', '-', 'TBD' sebagai null.")
    args = p.parse_args()

    src = Path(args.input).expanduser().resolve()
    if not src.exists():
        print(f"[ERROR] File tidak ditemukan: {src}", file=sys.stderr)
        return 2

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    na_tokens: set[str] = set() if args.no_na_tokens else set(DEFAULT_NA_TOKENS)

    print(f"[info] Membaca {src.name} ...", file=sys.stderr)
    df = _read_dataset(src, args.sheet, args.encoding, args.delimiter, na_tokens)
    print(f"[info] Loaded shape: {df.shape}", file=sys.stderr)

    meta = _dataset_meta(df, src, args.sheet)
    profile = {col: _profile_column(col, df[col]) for col in df.columns}

    # Aggregate numeric_subtype counts at the dataset level so consumers can
    # quickly see how many columns are truly continuous vs categorical-numeric.
    # The reasoning layer uses this to decide whether IQR-outlier metrics are
    # meaningful for the dataset as a whole.
    subtype_counts: dict[str, int] = {
        "continuous": 0,
        "boolean-flag": 0,
        "fk-categorical": 0,
        "enum-numeric": 0,
        "id-sequence": 0,
    }
    for col_profile in profile.values():
        st = col_profile.get("numeric_subtype")
        if st in subtype_counts:
            subtype_counts[st] += 1
    meta["numeric_subtype_counts"] = subtype_counts
    meta["columns_outlier_eligible_count"] = subtype_counts["continuous"]

    meta_path = out_dir / "_dataset_meta.json"
    profile_path = out_dir / "_profile_raw.json"
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    profile_path.write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[done] {meta_path}")
    print(f"[done] {profile_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
