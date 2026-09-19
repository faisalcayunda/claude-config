#!/usr/bin/env python3
"""
visualize_profile.py
====================

Generate 3-10 profiling charts (PNG) dari hasil profile_dataset.py.
Charts dipilih otomatis berdasarkan konten data.

Penggunaan:
    python visualize_profile.py \
        --meta <output-dir>/_dataset_meta.json \
        --profile <output-dir>/_profile_raw.json \
        --out <charts-output-dir>/ \
        [--dataset <original-dataset-path>]

Output: PNG files di <charts-output-dir>/
Tidak ada narasi teks di dalam gambar — hanya title, axis labels, legend.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
import math
from pathlib import Path
from typing import Any

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec

# ─── Color palette ───────────────────────────────────────────────
C_COMPLETE   = "#2196F3"   # blue — completeness
C_MISSING    = "#F44336"   # red  — missing/error
C_ANOMALY    = "#FF9800"   # orange — anomaly/outlier
C_CATEGORY   = "#4CAF50"   # green — category
C_NEUTRAL    = "#9E9E9E"   # grey  — neutral
C_HIGHLIGHT  = "#673AB7"   # purple — highlight

DPI = 150
FIGSIZE_WIDE = (14, 6)
FIGSIZE_SQUARE = (10, 8)
THRESHOLD_COMPLETENESS = 95.0


# ─── Helpers ─────────────────────────────────────────────────────

def _load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _savefig(fig, outdir: Path, name: str) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    p = outdir / f"{name}.png"
    fig.savefig(p, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"[chart] Saved: {p.name}")
    return p


def _numeric_cols(profile: dict) -> list[str]:
    return [c for c, v in profile.items()
            if v.get("data_type") in ("float64", "int64", "float32", "int32")
            and v.get("total_filled_record", 0) > 0]


def _categorical_cols(profile: dict, max_unique: int = 30) -> list[str]:
    return [c for c, v in profile.items()
            if v.get("data_type") in ("str", "object", "category")
            and v.get("count_unique", 0) <= max_unique
            and v.get("total_filled_record", 0) > 0]


def _datetime_cols(profile: dict) -> list[str]:
    return [c for c, v in profile.items()
            if "datetime" in str(v.get("data_type", "")).lower()
            or (v.get("data_type") == "str" and v.get("example_value")
                and any(ch in str(v.get("example_value", "")) for ch in ["-", "/"])
                and any(kw in c.lower() for kw in ["date", "time", "tanggal", "dt", "created", "updated"]))]


# ─── Chart 1: Completeness Bar Chart ─────────────────────────────

def chart_completeness(profile: dict, meta: dict, outdir: Path) -> Path:
    cols = list(profile.keys())
    pct = [profile[c].get("pct_not_null", 0) for c in cols]
    
    # Sort ascending by completeness
    sorted_pairs = sorted(zip(pct, cols), key=lambda x: x[0])
    pct_sorted, cols_sorted = zip(*sorted_pairs) if sorted_pairs else ([], [])
    
    colors = [C_MISSING if p < THRESHOLD_COMPLETENESS else C_COMPLETE for p in pct_sorted]
    
    fig, ax = plt.subplots(figsize=(14, max(5, len(cols) * 0.3 + 2)))
    bars = ax.barh(cols_sorted, pct_sorted, color=colors, height=0.7, edgecolor="white")
    ax.axvline(x=THRESHOLD_COMPLETENESS, color=C_ANOMALY, linewidth=1.5, linestyle="--", label=f"{THRESHOLD_COMPLETENESS}% threshold")
    ax.set_xlim(0, 102)
    ax.set_xlabel("Completeness (%)", fontsize=11)
    ax.set_title("Column Completeness Overview", fontsize=13, fontweight="bold", pad=12)
    ax.legend(fontsize=9)
    
    # Annotate bars
    for bar, p in zip(bars, pct_sorted):
        ax.text(min(p + 0.5, 101), bar.get_y() + bar.get_height() / 2,
                f"{p:.1f}%", va="center", ha="left", fontsize=8,
                color="black" if p > 10 else "white")
    
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return _savefig(fig, outdir, "01_completeness")


# ─── Chart 2: Data Type Distribution ─────────────────────────────

def chart_dtype_distribution(profile: dict, outdir: Path) -> Path:
    dtype_counts: dict[str, int] = {}
    for v in profile.values():
        dt = str(v.get("data_type", "unknown"))
        dtype_counts[dt] = dtype_counts.get(dt, 0) + 1
    
    labels = list(dtype_counts.keys())
    sizes = list(dtype_counts.values())
    colors_map = plt.cm.Set3(np.linspace(0, 1, len(labels)))  # type: ignore
    
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.1f%%",
        colors=colors_map, startangle=90,
        pctdistance=0.8, labeldistance=1.12
    )
    for at in autotexts:
        at.set_fontsize(9)
    ax.set_title("Column Data Type Distribution", fontsize=13, fontweight="bold", pad=12)
    fig.tight_layout()
    return _savefig(fig, outdir, "02_dtype_distribution")


# ─── Chart 3: Missing Pattern Heatmap ────────────────────────────

def chart_missing_heatmap(profile: dict, outdir: Path) -> Path | None:
    # Only show if any column has missing > 5%
    missing_cols = {c: 100 - v.get("pct_not_null", 100)
                    for c, v in profile.items()
                    if (100 - v.get("pct_not_null", 100)) > 5}
    if not missing_cols:
        return None
    
    sorted_missing = sorted(missing_cols.items(), key=lambda x: x[1], reverse=True)
    cols, pct_miss = zip(*sorted_missing)
    
    fig, ax = plt.subplots(figsize=(12, max(4, len(cols) * 0.35 + 2)))
    bars = ax.barh(cols, pct_miss, color=[
        C_MISSING if p > 50 else C_ANOMALY for p in pct_miss
    ], height=0.7, edgecolor="white")
    ax.set_xlim(0, 105)
    ax.set_xlabel("Missing (%)", fontsize=11)
    ax.set_title("Missing Values Distribution (columns >5% missing)", fontsize=13, fontweight="bold", pad=12)
    
    for bar, p in zip(bars, pct_miss):
        ax.text(p + 0.5, bar.get_y() + bar.get_height() / 2,
                f"{p:.1f}%", va="center", ha="left", fontsize=9)
    
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return _savefig(fig, outdir, "03_missing_pattern")


# ─── Chart 4: Numeric Distributions (top 5 by std_dev) ───────────

def chart_numeric_distributions(profile: dict, df: pd.DataFrame | None, outdir: Path) -> Path | None:
    num_cols = _numeric_cols(profile)
    if not num_cols:
        return None
    
    # Pick top 5 by std_dev relative to range
    def _cv(c):
        p = profile[c]
        mn, mx = p.get("min_value", 0) or 0, p.get("max_value", 1) or 1
        return (p.get("std_dev") or 0) / max(abs(mx - mn), 1e-9)
    
    top5 = sorted(num_cols, key=_cv, reverse=True)[:5]
    n = len(top5)
    
    fig, axes = plt.subplots(1, n, figsize=(max(14, n * 3.5), 5))
    if n == 1:
        axes = [axes]
    
    for ax, col in zip(axes, top5):
        p = profile[col]
        if df is not None and col in df.columns:
            data = df[col].dropna()
            ax.hist(data, bins=30, color=C_COMPLETE, edgecolor="white", alpha=0.85)
            ax.axvline(p.get("mean", 0), color=C_ANOMALY, linewidth=1.5, linestyle="--", label=f"Mean: {p.get('mean', 0):.2f}")
            ax.axvline(p.get("median", 0), color=C_HIGHLIGHT, linewidth=1.5, linestyle=":", label=f"Median: {p.get('median', 0):.2f}")
            ax.legend(fontsize=7)
        else:
            # Draw approximate normal with stats
            mu = p.get("mean", 0) or 0
            sig = p.get("std_dev", 1) or 1
            x = np.linspace(mu - 4 * sig, mu + 4 * sig, 200)
            ax.fill_between(x, np.exp(-0.5 * ((x - mu) / sig) ** 2) / (sig * np.sqrt(2 * np.pi)),
                            alpha=0.6, color=C_COMPLETE)
        ax.set_title(col, fontsize=10, fontweight="bold")
        ax.set_xlabel("Value", fontsize=8)
        ax.set_ylabel("Frequency", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    
    fig.suptitle("Numeric Column Distributions (Top 5 by CV)", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    return _savefig(fig, outdir, "04_numeric_distributions")


# ─── Chart 5: Categorical Frequency ──────────────────────────────

def chart_categorical_frequencies(profile: dict, outdir: Path) -> Path | None:
    cat_cols = _categorical_cols(profile)[:6]  # max 6 columns
    if not cat_cols:
        return None
    
    n = len(cat_cols)
    ncols_grid = min(3, n)
    nrows_grid = math.ceil(n / ncols_grid)
    
    fig, axes = plt.subplots(nrows_grid, ncols_grid, figsize=(ncols_grid * 5, nrows_grid * 4))
    axes_flat = np.array(axes).flatten() if n > 1 else [axes]
    
    for ax, col in zip(axes_flat, cat_cols):
        top_vals = profile[col].get("top_values", [])[:10]
        if not top_vals:
            ax.set_visible(False)
            continue
        labels = [str(v["value"])[:20] for v in top_vals]
        counts = [v["count"] for v in top_vals]
        
        bars = ax.barh(labels[::-1], counts[::-1], color=C_CATEGORY, edgecolor="white")
        ax.set_title(col, fontsize=10, fontweight="bold")
        ax.set_xlabel("Count", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    
    # Hide unused subplots
    for ax in axes_flat[n:]:
        ax.set_visible(False)
    
    fig.suptitle("Categorical Column Frequency (Top 10 Values)", fontsize=13, fontweight="bold")
    fig.tight_layout()
    return _savefig(fig, outdir, "05_categorical_frequencies")


# ─── Chart 6: Correlation Heatmap ────────────────────────────────

def chart_correlation_heatmap(profile: dict, df: pd.DataFrame | None, outdir: Path) -> Path | None:
    num_cols = _numeric_cols(profile)
    if len(num_cols) < 3:
        return None
    
    if df is not None:
        valid_cols = [c for c in num_cols if c in df.columns][:15]
        if len(valid_cols) < 3:
            return None
        corr = df[valid_cols].corr(method="spearman")
    else:
        return None
    
    fig, ax = plt.subplots(figsize=(max(8, len(valid_cols) * 0.9), max(6, len(valid_cols) * 0.8)))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    cmap = plt.cm.RdBu_r
    im = ax.imshow(corr.where(~mask), cmap=cmap, vmin=-1, vmax=1, aspect="auto")
    
    ticks = range(len(valid_cols))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(valid_cols, rotation=45, ha="right", fontsize=9)
    ax.set_yticklabels(valid_cols, fontsize=9)
    
    # Annotate cells
    for i in range(len(valid_cols)):
        for j in range(len(valid_cols)):
            if not mask[i, j]:
                val = corr.iloc[i, j]
                if not math.isnan(val):
                    ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                            fontsize=8, color="white" if abs(val) > 0.7 else "black")
    
    plt.colorbar(im, ax=ax, shrink=0.8, label="Spearman ρ")
    ax.set_title("Correlation Matrix (Spearman ρ, lower triangle)", fontsize=13, fontweight="bold", pad=12)
    fig.tight_layout()
    return _savefig(fig, outdir, "06_correlation_heatmap")


# ─── Chart 7: Outlier Boxplots ────────────────────────────────────

def chart_outlier_boxplots(profile: dict, df: pd.DataFrame | None, outdir: Path) -> Path | None:
    # Find numeric cols with potential outliers
    outlier_cols = [c for c in _numeric_cols(profile)
                    if "yes" in str(profile[c].get("outlier_detected", "")).lower()
                    or (profile[c].get("std_dev", 0) or 0) > (profile[c].get("mean", 0) or 0) * 2][:6]
    
    if not outlier_cols and len(_numeric_cols(profile)) < 2:
        return None
    
    target_cols = outlier_cols if outlier_cols else _numeric_cols(profile)[:5]
    
    if df is None:
        return None
    
    valid_cols = [c for c in target_cols if c in df.columns]
    if not valid_cols:
        return None
    
    fig, axes = plt.subplots(1, len(valid_cols), figsize=(max(10, len(valid_cols) * 2.5), 5))
    if len(valid_cols) == 1:
        axes = [axes]
    
    for ax, col in zip(axes, valid_cols):
        data = df[col].dropna()
        bp = ax.boxplot(data, patch_artist=True, notch=False, vert=True,
                        medianprops=dict(color=C_ANOMALY, linewidth=2))
        for patch in bp["boxes"]:
            patch.set_facecolor(C_COMPLETE)
            patch.set_alpha(0.7)
        for flier in bp["fliers"]:
            flier.set(marker="o", color=C_MISSING, alpha=0.5, markersize=4)
        ax.set_title(col, fontsize=9, fontweight="bold")
        ax.tick_params(labelsize=7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    
    fig.suptitle("Numeric Columns Outlier Boxplots", fontsize=13, fontweight="bold")
    fig.tight_layout()
    return _savefig(fig, outdir, "07_outlier_boxplots")


# ─── Chart 8: Cardinality Pareto ────────────────────────────────

def chart_cardinality_pareto(profile: dict, outdir: Path) -> Path:
    cols = list(profile.keys())
    unique_counts = [profile[c].get("count_unique", 0) for c in cols]
    
    sorted_pairs = sorted(zip(unique_counts, cols), reverse=True)
    u_sorted, c_sorted = zip(*sorted_pairs) if sorted_pairs else ([], [])
    
    cum_pct = np.cumsum(u_sorted) / max(sum(u_sorted), 1) * 100
    
    fig, ax1 = plt.subplots(figsize=FIGSIZE_WIDE)
    ax2 = ax1.twinx()
    
    ax1.bar(range(len(c_sorted)), u_sorted, color=C_HIGHLIGHT, alpha=0.7, edgecolor="white")
    ax2.plot(range(len(c_sorted)), cum_pct, color=C_ANOMALY, linewidth=2, marker="o", markersize=4)
    ax2.axhline(80, color=C_NEUTRAL, linewidth=1, linestyle="--")
    
    ax1.set_xticks(range(len(c_sorted)))
    ax1.set_xticklabels(c_sorted, rotation=45, ha="right", fontsize=8)
    ax1.set_ylabel("Unique Value Count", fontsize=10)
    ax2.set_ylabel("Cumulative %", fontsize=10)
    ax2.set_ylim(0, 105)
    ax1.set_title("Cardinality Pareto Chart", fontsize=13, fontweight="bold", pad=12)
    
    ax1.spines["top"].set_visible(False)
    fig.tight_layout()
    return _savefig(fig, outdir, "08_cardinality_pareto")


# ─── Chart 9: Time Series Overview ───────────────────────────────

def chart_time_series(profile: dict, df: pd.DataFrame | None, outdir: Path) -> Path | None:
    if df is None:
        return None
    dt_cols = _datetime_cols(profile)
    if not dt_cols:
        return None
    
    dt_col = dt_cols[0]
    if dt_col not in df.columns:
        return None
    
    try:
        ts = pd.to_datetime(df[dt_col], errors="coerce").dropna().sort_values()
    except Exception:
        return None
    
    if len(ts) < 5:
        return None
    
    # Count records per time bucket
    try:
        ts_df = ts.value_counts().sort_index()
        # Resample if too many points
        if len(ts_df) > 200:
            ts_df = ts_df.resample("ME").sum() if hasattr(ts_df.index, "freq") else ts_df.iloc[::max(1, len(ts_df) // 100)]
    except Exception:
        return None
    
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    ax.plot(ts_df.index, ts_df.values, color=C_COMPLETE, linewidth=1.5, alpha=0.9)
    ax.fill_between(ts_df.index, ts_df.values, alpha=0.2, color=C_COMPLETE)
    ax.set_xlabel("Date", fontsize=10)
    ax.set_ylabel("Record Count", fontsize=10)
    ax.set_title(f"Record Distribution Over Time — {dt_col}", fontsize=13, fontweight="bold", pad=12)
    ax.tick_params(axis="x", rotation=30, labelsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return _savefig(fig, outdir, "09_time_series")


# ─── Chart 10: Dataset Condition Snapshot ────────────────────────
# (Sebelumnya DQ Scorecard DAMA — DIHAPUS. Skill ini fokus melaporkan kondisi
#  apa adanya, bukan menilai/mengskor kualitas data per dimensi.)
#
# Chart ini menampilkan JUMLAH kolom yang terkena tiap jenis kondisi:
# - berapa kolom punya null
# - berapa kolom terdeteksi inkonsistensi format
# - berapa kolom punya nilai invalid (vs business rule yang dilaporkan)
# - berapa kolom punya outlier terdeteksi
# - berapa kolom kategorikal vs numerik vs datetime vs ID-like
# Sumbu Y = jumlah kolom (count), bukan score (%).

def chart_condition_snapshot(profile: dict, meta: dict, outdir: Path) -> Path:
    total_cols = max(len(profile), 1)

    # Hitung kondisi per kolom (deskriptif, bukan score)
    cols_with_null = sum(
        1 for v in profile.values()
        if (v.get("pct_not_null") is not None and v.get("pct_not_null") < 100)
    )
    cols_with_inconsistency = sum(
        1 for v in profile.values()
        if v.get("is_consistent") is False
    )
    cols_with_invalid = sum(
        1 for v in profile.values()
        if v.get("is_there_unvalid_value") is True
    )
    cols_with_outlier = sum(
        1 for v in profile.values()
        if str(v.get("outlier_detected", "")).lower().startswith("yes")
    )
    cols_categorical = sum(1 for v in profile.values() if v.get("is_category") is True)
    cols_numeric = sum(
        1 for v in profile.values()
        if any(t in str(v.get("data_type", "")).lower() for t in ("int", "float", "numeric"))
    )
    cols_datetime = sum(
        1 for v in profile.values()
        if "datetime" in str(v.get("data_type", "")).lower()
        or any(kw in str(k).lower() for k, v_ in [(k, v) for k, v in profile.items()]
               for kw in [])  # no-op, keep simple
    )
    # Simpler datetime detection by column name
    cols_datetime = sum(
        1 for k, v in profile.items()
        if "datetime" in str(v.get("data_type", "")).lower()
        or any(kw in str(k).lower() for kw in ["date", "time", "tanggal", "dt"])
    )
    cols_id_like = sum(1 for v in profile.values() if v.get("is_unique") is True)

    # Susun deret kondisi — urut dari yang paling banyak terjadi
    labels_counts = [
        ("Punya null", cols_with_null),
        ("Inkonsistensi format", cols_with_inconsistency),
        ("Nilai invalid (vs business rule)", cols_with_invalid),
        ("Outlier terdeteksi", cols_with_outlier),
        ("Kategorikal", cols_categorical),
        ("Numerik", cols_numeric),
        ("Datetime-like", cols_datetime),
        ("ID/Unique (kandidat key)", cols_id_like),
    ]
    # Sort by count desc, keep labels
    labels_counts.sort(key=lambda x: x[1], reverse=True)
    labels = [lc[0] for lc in labels_counts]
    counts = [lc[1] for lc in labels_counts]

    fig, ax = plt.subplots(figsize=(10, 5.2))
    bars = ax.barh(labels, counts, color=C_HIGHLIGHT, edgecolor="white", height=0.65, alpha=0.85)
    ax.set_xlim(0, max(total_cols, max(counts) if counts else 1) + 1)
    ax.set_xlabel(f"Jumlah kolom (dari total {total_cols} kolom)", fontsize=10)
    ax.set_title(
        "Dataset Condition Snapshot\n(deskriptif kondisi — bukan skor kualitas data)",
        fontsize=11, fontweight="bold", pad=10,
    )

    for bar, c in zip(bars, counts):
        ax.text(
            c + 0.15, bar.get_y() + bar.get_height() / 2,
            f"{c}",
            va="center", ha="left", fontsize=9,
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.invert_yaxis()  # paling banyak di atas
    fig.tight_layout()
    return _savefig(fig, outdir, "10_condition_snapshot")


# ─── Chart 11: Column Category Distribution ──────────────────────
# Distribusi kolom per kategori peran data (Master/Reference/
# Transaksional/Log/Lainnya). Field `data_category` diisi via LLM
# reasoning setelah profile_dataset.py — jika belum diisi, fungsi
# tetap render chart dengan kategori "Lainnya" sebagai placeholder.

CATEGORY_ORDER = ["Master", "Reference", "Transaksional", "Log", "Lainnya"]
CATEGORY_COLORS = {
    "Master":        "#1976D2",  # biru
    "Reference":     "#388E3C",  # hijau
    "Transaksional": "#F57C00",  # oranye
    "Log":           "#7B1FA2",  # ungu
    "Lainnya":       "#9E9E9E",  # abu
}

def _normalize_category(raw: str) -> str:
    """Normalisasi nilai data_category ke salah satu CATEGORY_ORDER."""
    if not raw:
        return "Lainnya"
    s = str(raw).strip().lower()
    if s in ("master", "data master", "m"):
        return "Master"
    if s in ("reference", "ref", "data reference", "lookup", "code list"):
        return "Reference"
    if s in ("transaksional", "transactional", "transaction", "trx", "data transaksional"):
        return "Transaksional"
    if s in ("log", "audit", "data log", "system log"):
        return "Log"
    return "Lainnya"


def chart_category_distribution(profile: dict, outdir: Path) -> Path:
    # Hitung jumlah kolom per kategori
    counts = {k: 0 for k in CATEGORY_ORDER}
    for v in profile.values():
        cat = _normalize_category(v.get("data_category"))
        counts[cat] = counts.get(cat, 0) + 1

    total_cols = sum(counts.values()) or 1
    labels = CATEGORY_ORDER
    values = [counts[k] for k in labels]
    colors_bar = [CATEGORY_COLORS[k] for k in labels]

    fig, ax = plt.subplots(figsize=(9, 4.8))
    bars = ax.bar(labels, values, color=colors_bar, edgecolor="white", width=0.6, alpha=0.9)
    ax.set_ylabel(f"Jumlah kolom (dari total {total_cols})", fontsize=10)
    ax.set_title(
        "Column Category Distribution\n(peran kolom dalam ekosistem data — deskriptif, bukan skor)",
        fontsize=11, fontweight="bold", pad=10,
    )
    ax.set_ylim(0, max(values) * 1.18 if max(values) > 0 else 1)

    for bar, v in zip(bars, values):
        pct = (v / total_cols * 100) if total_cols else 0
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(values) * 0.02 + 0.05,
            f"{v}\n({pct:.0f}%)",
            ha="center", va="bottom", fontsize=9,
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return _savefig(fig, outdir, "11_category_distribution")


# ─── Main ─────────────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(description="Generate profiling charts from profile_dataset output.")
    p.add_argument("--meta", required=True, help="Path to _dataset_meta.json")
    p.add_argument("--profile", required=True, help="Path to _profile_raw.json")
    p.add_argument("--out", required=True, help="Output directory for PNG files")
    p.add_argument("--dataset", default=None, help="Path to original dataset (for real distributions)")
    args = p.parse_args()
    
    meta = _load_json(Path(args.meta))
    profile = _load_json(Path(args.profile))
    outdir = Path(args.out)
    
    # Try to load original dataset for richer charts
    df: pd.DataFrame | None = None
    if args.dataset:
        try:
            src = Path(args.dataset)
            if src.suffix.lower() == ".csv":
                df = pd.read_csv(src, na_values=["", "NA", "N/A", "null", "None", "-", "NaN"],
                                 keep_default_na=True, sep=None, engine="python")
            elif src.suffix.lower() in (".xlsx", ".xls"):
                df = pd.read_excel(src, na_values=["", "NA", "N/A", "null", "None", "-"], keep_default_na=True)
            print(f"[info] Loaded dataset for richer charts: {src.name} shape={df.shape}")
        except Exception as e:
            print(f"[warn] Could not load dataset for charts: {e}", file=sys.stderr)
    
    generated = []
    
    # Core charts (always)
    generated.append(chart_completeness(profile, meta, outdir))
    generated.append(chart_dtype_distribution(profile, outdir))
    r = chart_missing_heatmap(profile, outdir)
    if r: generated.append(r)
    
    # Conditional charts
    r = chart_numeric_distributions(profile, df, outdir)
    if r: generated.append(r)
    
    r = chart_categorical_frequencies(profile, outdir)
    if r: generated.append(r)
    
    r = chart_correlation_heatmap(profile, df, outdir)
    if r: generated.append(r)
    
    r = chart_outlier_boxplots(profile, df, outdir)
    if r: generated.append(r)
    
    generated.append(chart_cardinality_pareto(profile, outdir))
    
    r = chart_time_series(profile, df, outdir)
    if r: generated.append(r)
    
    generated.append(chart_condition_snapshot(profile, meta, outdir))
    generated.append(chart_category_distribution(profile, outdir))

    print(f"\n[done] Generated {len(generated)} chart(s) in: {outdir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
