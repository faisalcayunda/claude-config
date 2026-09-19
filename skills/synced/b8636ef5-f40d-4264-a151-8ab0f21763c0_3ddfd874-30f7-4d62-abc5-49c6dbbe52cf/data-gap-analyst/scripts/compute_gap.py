"""
compute_gap.py — Modul perhitungan 4 dimensi gap.
Bagian dari skill `data-gap-analyst`.

Input: dua TableProfile dict (Source A, Source B) dari profile_source.py
       atau parse output `data-profiling-baseline` (Mode B), atau schema-only
       dict (Mode D).
Output: list gap findings (dict yang siap di-feed ke llm_reasoning_helper.py
        untuk reasoning chain).

Anti-halusinasi: setiap finding di-tag dengan source_trace yang merujuk ke
metric origin (query/file).

Dimensi:
    D1 — Volume & Completeness
    D2 — Schema & Structural
    D3 — Value Distribution & Semantic
    D4 — Temporal & Freshness

Threshold default ada di assets/threshold_rubric.md. User boleh override via
config dict.
"""
from __future__ import annotations

import json
from typing import Any

DEFAULT_THRESHOLDS = {
    "d1": {
        "row_count_diff_minor": 0.02,
        "row_count_diff_critical": 0.10,
        "null_ratio_delta_minor_pp": 0.02,
        "null_ratio_delta_critical_pp": 0.10,
        "distinct_count_diff_minor": 0.02,
        "distinct_count_diff_critical": 0.10,
    },
    "d3": {
        "ks_pvalue_critical": 0.01,
        "ks_pvalue_moderate": 0.05,
        "jaccard_critical": 0.80,
        "jaccard_moderate": 0.95,
        "mean_delta_moderate": 0.05,
        "mean_delta_critical": 0.20,
    },
    "d4": {
        "sla_hours_default": 24,  # T+1
        "lag_pct_sla_moderate": 0.50,
        "lag_pct_sla_critical": 1.00,
    },
}


def merge_thresholds(user_override: dict | None) -> dict:
    """Merge user override ke default threshold (deep merge 2-level)."""
    out = {k: dict(v) if isinstance(v, dict) else v for k, v in DEFAULT_THRESHOLDS.items()}
    if not user_override:
        return out
    for dim, vals in user_override.items():
        if dim in out and isinstance(vals, dict):
            out[dim].update(vals)
        else:
            out[dim] = vals
    return out


def classify_severity(value: float, minor_thresh: float, critical_thresh: float,
                      reverse: bool = False) -> str:
    """Klasifikasi 🟢/🟡/🔴 dengan threshold."""
    if reverse:
        # For metrics where HIGHER value = better (e.g. Jaccard similarity)
        if value > critical_thresh:
            return "🟢"
        if value > minor_thresh:
            return "🟡"
        return "🔴"
    if value < minor_thresh:
        return "🟢"
    if value < critical_thresh:
        return "🟡"
    return "🔴"


# ============================================================
# D1 — Volume & Completeness
# ============================================================

def gap_d1_row_count(table_a: dict, table_b: dict, thresholds: dict) -> dict | None:
    """Row count delta per tabel."""
    a, b = table_a["row_count"], table_b["row_count"]
    if a == 0 and b == 0:
        return None
    rel = abs(a - b) / max(a, b)
    if rel < thresholds["d1"]["row_count_diff_minor"]:
        return None  # below minor threshold = skip

    severity = classify_severity(
        rel,
        thresholds["d1"]["row_count_diff_minor"],
        thresholds["d1"]["row_count_diff_critical"],
    )
    return {
        "dimension": "D1",
        "metric": "row_count_diff",
        "severity": severity,
        "value_a": a,
        "value_b": b,
        "absolute": abs(a - b),
        "relative": rel,
        "unit": "rows",
        "context": f"{table_a['table_name']} vs {table_b['table_name']}",
        "source_trace": {
            "query_a": f"SELECT COUNT(*) FROM {table_a['table_name']}",
            "query_b": f"SELECT COUNT(*) FROM {table_b['table_name']}",
        },
    }


def gap_d1_null_ratio(col_a: dict, col_b: dict, thresholds: dict) -> dict | None:
    """NULL ratio delta per kolom (percentage point)."""
    delta_pp = abs(col_a["null_ratio"] - col_b["null_ratio"])
    if delta_pp < thresholds["d1"]["null_ratio_delta_minor_pp"]:
        return None
    severity = classify_severity(
        delta_pp,
        thresholds["d1"]["null_ratio_delta_minor_pp"],
        thresholds["d1"]["null_ratio_delta_critical_pp"],
    )
    return {
        "dimension": "D1",
        "metric": "null_ratio_delta",
        "severity": severity,
        "value_a": col_a["null_ratio"],
        "value_b": col_b["null_ratio"],
        "absolute": delta_pp,
        "relative": delta_pp,
        "unit": "percentage_point",
        "context": f"col {col_a['column_name']}",
        "source_trace": {
            "query_a": col_a.get("source_query_or_file", ""),
            "query_b": col_b.get("source_query_or_file", ""),
        },
    }


def gap_d1_table_coverage(tables_a: list[dict], tables_b: list[dict]) -> list[dict]:
    """Tabel di A tidak di B (dan sebaliknya)."""
    names_a = {t["table_name"] for t in tables_a}
    names_b = {t["table_name"] for t in tables_b}
    missing_in_b = names_a - names_b
    missing_in_a = names_b - names_a

    findings = []
    for tbl in missing_in_b:
        findings.append({
            "dimension": "D1",
            "metric": "table_missing_in_b",
            "severity": "🔴",
            "context": f"table {tbl} ada di Source A, tidak di Source B",
        })
    for tbl in missing_in_a:
        findings.append({
            "dimension": "D1",
            "metric": "table_missing_in_a",
            "severity": "🔴",
            "context": f"table {tbl} ada di Source B, tidak di Source A",
        })
    return findings


# ============================================================
# D2 — Schema & Structural
# ============================================================

DESTRUCTIVE_TYPE_NARROWING = [
    ("BIGINT", "INT"), ("BIGINT", "SMALLINT"),
    ("VARCHAR(255)", "VARCHAR(100)"), ("VARCHAR(100)", "VARCHAR(50)"),
    ("NUMERIC(14,2)", "NUMERIC(10,2)"), ("TIMESTAMPTZ", "TIMESTAMP"),
    ("TEXT", "VARCHAR(255)"),
]


def gap_d2_column_diff(table_a: dict, table_b: dict) -> list[dict]:
    """Kolom present di A tidak di B (dan sebaliknya), plus type diff."""
    cols_a = {c["column_name"]: c for c in table_a["columns"]}
    cols_b = {c["column_name"]: c for c in table_b["columns"]}

    findings = []
    for name in cols_a.keys() - cols_b.keys():
        findings.append({
            "dimension": "D2",
            "metric": "missing_column_in_b",
            "severity": "🟡",
            "context": f"column {name} ada di A tidak di B",
            "value_a": cols_a[name]["data_type"],
        })
    for name in cols_b.keys() - cols_a.keys():
        findings.append({
            "dimension": "D2",
            "metric": "missing_column_in_a",
            "severity": "🟡",
            "context": f"column {name} ada di B tidak di A",
            "value_b": cols_b[name]["data_type"],
        })

    # Type diff untuk kolom yang ada di kedua source
    for name in cols_a.keys() & cols_b.keys():
        ta = cols_a[name]["data_type"]
        tb = cols_b[name]["data_type"]
        if ta != tb:
            severity = "🔴" if _is_destructive_type_change(ta, tb) else "🟡"
            findings.append({
                "dimension": "D2",
                "metric": "type_change",
                "severity": severity,
                "context": f"column {name}: {ta} → {tb}",
                "value_a": ta,
                "value_b": tb,
            })
    return findings


def _is_destructive_type_change(a: str, b: str) -> bool:
    """Cek apakah perubahan tipe data berisiko data loss."""
    a_norm = a.upper().strip()
    b_norm = b.upper().strip()
    for src, dst in DESTRUCTIVE_TYPE_NARROWING:
        if a_norm.startswith(src) and b_norm.startswith(dst):
            return True
    return False


def gap_d2_constraint_diff(table_a: dict, table_b: dict) -> list[dict]:
    """Constraint delta — PK, FK, UNIQUE, NOT NULL, CHECK."""
    findings = []
    pk_a = (table_a.get("constraints", {}).get("primary_key") or {}).get("constrained_columns")
    pk_b = (table_b.get("constraints", {}).get("primary_key") or {}).get("constrained_columns")
    if pk_a and pk_b and pk_a != pk_b:
        findings.append({
            "dimension": "D2",
            "metric": "primary_key_change",
            "severity": "🔴",
            "context": f"PK A={pk_a} vs B={pk_b}",
        })

    fk_a = {tuple(f["constrained_columns"]) for f in table_a.get("constraints", {}).get("foreign_keys", [])}
    fk_b = {tuple(f["constrained_columns"]) for f in table_b.get("constraints", {}).get("foreign_keys", [])}
    for missing in fk_a - fk_b:
        findings.append({
            "dimension": "D2",
            "metric": "foreign_key_missing_in_b",
            "severity": "🟡",
            "context": f"FK on {missing} ada di A tidak di B",
        })
    return findings


# ============================================================
# D3 — Value Distribution & Semantic
# ============================================================

def gap_d3_distribution(col_a: dict, col_b: dict, thresholds: dict,
                        raw_data_a: list | None = None,
                        raw_data_b: list | None = None) -> dict | None:
    """Distribusi numeric — KS test jika raw_data tersedia, else mean delta."""
    if col_a.get("mean") is None or col_b.get("mean") is None:
        return None

    mean_a, mean_b = col_a["mean"], col_b["mean"]
    if mean_a == 0:
        return None
    mean_delta = abs(mean_a - mean_b) / abs(mean_a)

    ks_pvalue = None
    if raw_data_a and raw_data_b:
        try:
            from scipy.stats import ks_2samp
            ks_pvalue = float(ks_2samp(raw_data_a, raw_data_b).pvalue)
        except ImportError:
            pass

    if ks_pvalue is not None:
        if ks_pvalue >= thresholds["d3"]["ks_pvalue_moderate"]:
            severity_ks = "🟢"
        elif ks_pvalue >= thresholds["d3"]["ks_pvalue_critical"]:
            severity_ks = "🟡"
        else:
            severity_ks = "🔴"
    else:
        severity_ks = None

    severity_mean = classify_severity(
        mean_delta,
        thresholds["d3"]["mean_delta_moderate"],
        thresholds["d3"]["mean_delta_critical"],
    )

    # Pakai yang paling severe antara KS dan mean
    severity = max([s for s in (severity_ks, severity_mean) if s], key=_severity_rank)

    if severity == "🟢":
        return None
    return {
        "dimension": "D3",
        "metric": "distribution_delta",
        "severity": severity,
        "value_a": {"mean": mean_a, "median": col_a.get("median"), "stddev": col_a.get("stddev")},
        "value_b": {"mean": mean_b, "median": col_b.get("median"), "stddev": col_b.get("stddev")},
        "ks_pvalue": ks_pvalue,
        "mean_delta_relative": mean_delta,
        "context": f"col {col_a['column_name']}",
    }


def gap_d3_categorical(col_a: dict, col_b: dict, thresholds: dict) -> dict | None:
    """Jaccard similarity untuk distinct value set."""
    set_a = set(v for v, _ in col_a.get("top_values", []))
    set_b = set(v for v, _ in col_b.get("top_values", []))
    if not set_a and not set_b:
        return None
    union = set_a | set_b
    if not union:
        return None
    jaccard = len(set_a & set_b) / len(union)
    if jaccard > thresholds["d3"]["jaccard_moderate"]:
        return None  # similar enough
    severity = classify_severity(
        jaccard,
        thresholds["d3"]["jaccard_moderate"],
        thresholds["d3"]["jaccard_critical"],
        reverse=True,
    )
    return {
        "dimension": "D3",
        "metric": "categorical_diff",
        "severity": severity,
        "value_a": sorted(set_a),
        "value_b": sorted(set_b),
        "jaccard": jaccard,
        "only_in_a": sorted(set_a - set_b),
        "only_in_b": sorted(set_b - set_a),
        "context": f"col {col_a['column_name']}",
    }


def _severity_rank(s: str) -> int:
    return {"🟢": 0, "🟡": 1, "🔴": 2}.get(s, 0)


# ============================================================
# D4 — Temporal & Freshness
# ============================================================

def gap_d4_freshness(table_a: dict, table_b: dict, thresholds: dict,
                     timestamp_col: str = "updated_at") -> dict | None:
    """Lag estimation antar source."""
    col_a = next((c for c in table_a["columns"] if c["column_name"] == timestamp_col), None)
    col_b = next((c for c in table_b["columns"] if c["column_name"] == timestamp_col), None)
    if not (col_a and col_b and col_a.get("max_value") and col_b.get("max_value")):
        return None

    from datetime import datetime as dt
    try:
        max_a = dt.fromisoformat(str(col_a["max_value"]).replace("Z", "+00:00"))
        max_b = dt.fromisoformat(str(col_b["max_value"]).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return {
            "dimension": "D4",
            "metric": "freshness_unparseable",
            "severity": "🟡",
            "context": f"max({timestamp_col}) tidak bisa di-parse — butuh investigasi",
        }

    lag_hours = abs((max_a - max_b).total_seconds() / 3600)
    sla = thresholds["d4"]["sla_hours_default"]
    pct_sla = lag_hours / sla if sla else 0

    if pct_sla < thresholds["d4"]["lag_pct_sla_moderate"]:
        severity = "🟢"
    elif pct_sla < thresholds["d4"]["lag_pct_sla_critical"]:
        severity = "🟡"
    else:
        severity = "🔴"

    return {
        "dimension": "D4",
        "metric": "freshness_lag",
        "severity": severity,
        "value_a": col_a["max_value"],
        "value_b": col_b["max_value"],
        "lag_hours": lag_hours,
        "sla_hours": sla,
        "pct_sla": pct_sla,
        "context": f"max({timestamp_col}) {table_a['table_name']} vs {table_b['table_name']}",
    }


# ============================================================
# Orchestrator
# ============================================================

def compute_all_gaps(profile_a: list[dict] | dict, profile_b: list[dict] | dict,
                     thresholds_override: dict | None = None,
                     column_mapping: dict | None = None) -> list[dict]:
    """Hitung semua gap finding antar dua source.

    Args:
        profile_a, profile_b: list of TableProfile dict OR single dict
        thresholds_override: dict override (akan di-merge ke default)
        column_mapping: dict {table_a: {col_a: col_b}} hasil fuzzy match user-confirmed

    Returns:
        List of gap finding dicts, ready untuk reasoning chain generation.
    """
    thresholds = merge_thresholds(thresholds_override)
    tables_a = profile_a if isinstance(profile_a, list) else [profile_a]
    tables_b = profile_b if isinstance(profile_b, list) else [profile_b]

    findings: list[dict] = []

    # D1 — Table coverage
    findings.extend(gap_d1_table_coverage(tables_a, tables_b))

    # Per-table comparisons (untuk tabel yang ada di kedua source)
    names_b = {t["table_name"]: t for t in tables_b}
    for ta in tables_a:
        tb = names_b.get(ta["table_name"])
        if not tb:
            continue

        # D1 row count
        f = gap_d1_row_count(ta, tb, thresholds)
        if f:
            findings.append(f)

        # D2 schema diff
        findings.extend(gap_d2_column_diff(ta, tb))
        findings.extend(gap_d2_constraint_diff(ta, tb))

        # D1 NULL ratio + D3 distribution per kolom yang matched
        cols_a = {c["column_name"]: c for c in ta["columns"]}
        cols_b = {c["column_name"]: c for c in tb["columns"]}
        mapping = (column_mapping or {}).get(ta["table_name"], {})

        for cname_a, ca in cols_a.items():
            cname_b = mapping.get(cname_a, cname_a)
            cb = cols_b.get(cname_b)
            if not cb:
                continue

            f = gap_d1_null_ratio(ca, cb, thresholds)
            if f:
                findings.append(f)

            f = gap_d3_distribution(ca, cb, thresholds)
            if f:
                findings.append(f)

            f = gap_d3_categorical(ca, cb, thresholds)
            if f:
                findings.append(f)

        # D4 freshness
        for ts_col in ("updated_at", "created_at"):
            f = gap_d4_freshness(ta, tb, thresholds, timestamp_col=ts_col)
            if f and f["severity"] != "🟢":
                findings.append(f)
                break

    # Assign gap_id per dimension
    counter = {"D1": 0, "D2": 0, "D3": 0, "D4": 0}
    for f in findings:
        dim = f["dimension"]
        counter[dim] += 1
        f["gap_id"] = f"{dim}-{counter[dim]:03d}"

    return findings


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--profile-a", required=True, help="Path to source A profile JSON")
    p.add_argument("--profile-b", required=True, help="Path to source B profile JSON")
    p.add_argument("--config", help="Path to threshold override YAML/JSON")
    p.add_argument("--output", default="gap_findings_raw.json")
    args = p.parse_args()

    with open(args.profile_a) as f:
        pa = json.load(f)
    with open(args.profile_b) as f:
        pb = json.load(f)

    config = None
    if args.config:
        with open(args.config) as f:
            config = json.load(f) if args.config.endswith(".json") else None
            # YAML support optional

    findings = compute_all_gaps(pa, pb, thresholds_override=config)
    with open(args.output, "w") as f:
        json.dump(findings, f, indent=2, default=str)
    print(f"Found {len(findings)} gaps. Saved to: {args.output}")
