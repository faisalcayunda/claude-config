#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IDEAS RAB/HPS Generator — Enterprise Grade.

Version: 2.0.0
Compliance: Perpres 46/2025, PMK 32/2025 (SBM TA 2026), PP 49/2025.
Reference: rab-hps-methodology.md § 5 (24-column structure), § 6 (HPS formula).

Generates a Rencana Anggaran Biaya (RAB) / Harga Perkiraan Sendiri (HPS)
document for Indonesian government procurement. Outputs CSV (UTF-8 BOM for
Excel), XLSX, JSON, or formatted console table.

HPS Formula (per line item):
    Sub Total      = Harga Dasar × Koefisien Kompleksitas
    Margin         = Sub Total × margin_rate
    PPH            = (Sub Total + Margin) × pph_rate / (1 - pph_rate)   [gross-up]
    Harga Satuan   = Sub Total + Margin + PPH
    Total Biaya    = Harga Satuan × Volume

Grand Total:
    Subtotal HPS   = Σ Total Biaya
    PPN            = Subtotal HPS × ppn_rate
    Grand Total    = Subtotal HPS + PPN

Usage:
    python3 generate_rab.py --project "Ekosistem Data Jateng" --services S1.1,S1.2,S2.3 --level 10
    python3 generate_rab.py --project "Portal Data" --services S2.3 --level 8 --output rab.csv
    python3 generate_rab.py --project "DGO" --services S1.2 --level 12 --output rab.xlsx
    python3 generate_rab.py --project "DGO" --services S1.2 --level 12 --json
"""

import argparse
import csv
import json
import logging
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# ---------------------------------------------------------------------------
# Version & Constants
# ---------------------------------------------------------------------------
__version__ = "2.0.0"

# Default financial rates — Perpres 46/2025 compliant
DEFAULT_MARGIN_RATE: float = 0.50   # 50% standard margin for government HPS
DEFAULT_PPH_RATE: float = 0.02      # 2% PPh Pasal 23
DEFAULT_PPN_RATE: float = 0.11      # 11% PPN (UU HPP No. 7/2021)
WORKING_DAYS_PER_MONTH: int = 20

# Pillar mappings
PILLAR_META: Dict[int, Dict[str, str]] = {
    1: {"wp_name": "Kajian, Analisis & Strategi", "category": "TATA KELOLA"},
    2: {"wp_name": "Pengembangan Platform & Implementasi", "category": "PRODUCT & PLATFORM"},
    3: {"wp_name": "Pendampingan, Pelatihan & Pemberdayaan", "category": "SDM & PEMBERDAYAAN"},
}

# 24-column header matching rab-hps-template.csv § 5
HEADER_24 = [
    "Level 1",                              # [0]  Work Package
    "Level 2",                              # [1]  Sub-Package / Service
    "Level 3",                              # [2]  Task
    "Level 4",                              # [3]  Detail (reserved)
    "No.",                                  # [4]
    "KOMPONEN / TAHAPAN PEKERJAAN",         # [5]
    "SATUAN",                               # [6]
    "SATUAN DETAIL",                        # [7]
    "PERKIRAAN VOLUME / KUANTITAS",         # [8]
    "PERKIRAAN VOLUME DETAIL",              # [9]
    "PERKIRAAN LAMA WAKTU (BULAN)",         # [10]
    "PERKIRAAN JUMLAH ORANG / UNIT",        # [11]
    "PERKIRAAN TOTAL",                      # [12]
    "HARGA DASAR (Rp)",                     # [13]
    "KOEFISIEN / INDEKS KOMPLEKSITAS",      # [14]
    "SUB TOTAL",                            # [15]
    "MARGIN 50%",                           # [16]
    "PPH 2%",                               # [17]
    "HARGA SATUAN (Rp) INTERNAL",           # [18]
    "HARGA SATUAN (Rp)",                    # [19]
    "TOTAL BIAYA (Rp) INTERNAL",            # [20]
    "TOTAL BIAYA (Rp)",                     # [21]
    "PERSENTASE (%)",                       # [22]
    "KATEGORI",                             # [23]
]

# Logging — always to stderr so stdout stays clean for piping
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Dependency imports
# ---------------------------------------------------------------------------
try:
    from estimate_service_cost import SERVICES, estimate_service_cost
    from pricing_engine import get_daily_rate, get_internal_daily_rate
except ImportError as exc:
    logger.critical("Cannot import core modules: %s", exc)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _fmt(val: Union[int, float]) -> str:
    """Format numeric value as Rupiah string."""
    if not isinstance(val, (int, float)):
        return "Rp 0"
    return f"Rp {val:,.0f}"


def _r(val: float) -> int:
    """Round to nearest integer for Rupiah."""
    return round(val)


def _calc_item(task: Dict[str, Any], complexity: float,
               margin_rate: float, pph_rate: float) -> Dict[str, Any]:
    """Calculate full HPS cost components for one task.

    Implements the 5-step formula from rab-hps-methodology.md § 6:
      Step 1: sub_total     = harga_dasar × koefisien
      Step 2: margin        = sub_total × margin_rate
      Step 3: pph           = (sub_total + margin) × pph_rate / (1 - pph_rate)
      Step 4: harga_satuan  = sub_total + margin + pph
      Step 5: total_biaya   = harga_satuan × volume (always 1)
    """
    harga_dasar = task["total_cost"]
    sub_total = harga_dasar * complexity
    margin_amount = sub_total * margin_rate
    pph_amount = (sub_total + margin_amount) * pph_rate / (1 - pph_rate)
    harga_satuan_ext = sub_total + margin_amount + pph_amount

    # Internal pricing: cost basis only (no margin, no PPH gross-up)
    harga_satuan_int = sub_total

    return {
        "harga_dasar": harga_dasar,
        "koefisien": complexity,
        "sub_total": sub_total,
        "margin_rate": margin_rate,
        "margin_amount": margin_amount,
        "pph_rate": pph_rate,
        "pph_amount": pph_amount,
        "harga_satuan_int": harga_satuan_int,
        "harga_satuan_ext": harga_satuan_ext,
        "total_biaya_int": harga_satuan_int,
        "total_biaya_ext": harga_satuan_ext,
    }


# ---------------------------------------------------------------------------
# Core generator
# ---------------------------------------------------------------------------
def generate_rab(
    project_name: str,
    service_ids: List[str],
    level: int,
    level_map: Optional[Dict[str, int]],
    complexity: float,
    margin_rate: float,
    pph_rate: float,
    ppn_rate: float,
    pricing_mode: str,
) -> Dict[str, Any]:
    """Build the complete RAB/HPS data structure.

    Returns a dict with all items, work-package hierarchy, and totals.
    If no valid services can be processed, returns ``{"error": "..."}``.
    """
    all_items: List[Dict[str, Any]] = []
    work_packages: Dict[int, Dict[str, Any]] = {}
    item_no = 0

    for sid in service_ids:
        if sid not in SERVICES:
            logger.error("Service '%s' not found. Skipping.", sid)
            continue

        try:
            result = estimate_service_cost(sid, level, level_map, complexity, pricing_mode)
            if "error" in result:
                logger.warning("Cannot estimate '%s': %s", sid, result["error"])
                continue
        except Exception as exc:
            logger.error("Unexpected error estimating '%s': %s", sid, exc)
            continue

        pillar = result["pillar"]
        meta = PILLAR_META.get(pillar, {"wp_name": f"Work Package {pillar}", "category": "LAINNYA"})

        if pillar not in work_packages:
            work_packages[pillar] = {
                "wp_no": pillar,
                "wp_name": meta["wp_name"],
                "category": meta["category"],
                "services": [],
                "subtotal_ext": 0.0,
                "subtotal_int": 0.0,
                "total_man_days": 0.0,
            }

        svc_items = []
        for task in result["tasks"]:
            item_no += 1
            costs = _calc_item(task, complexity, margin_rate, pph_rate)

            man_days = task["adjusted_man_days"]
            role_count = len(task.get("roles", [])) or 1
            est_months = round(man_days / WORKING_DAYS_PER_MONTH / max(role_count, 1), 2) or 0.25

            item = {
                "no": item_no,
                "service_id": sid,
                "service_name": result["service_name"],
                "task_id": task["task_id"],
                "description": task["description"],
                "dama_ka": task["dama_ka"],
                "satuan": "Paket",
                "satuan_detail": f"{man_days:.0f} Man-Days",
                "volume": 1,
                "volume_detail": f"{role_count} roles x {man_days:.0f} MD",
                "est_months": est_months,
                "est_people": role_count,
                "perkiraan_total": 1,
                "man_days": man_days,
                "category": meta["category"],
                "pillar": pillar,
                "roles": task.get("roles", []),
                **costs,
            }
            svc_items.append(item)

        svc_total_ext = sum(i["total_biaya_ext"] for i in svc_items)
        svc_total_int = sum(i["total_biaya_int"] for i in svc_items)
        svc_man_days = sum(i["man_days"] for i in svc_items)

        work_packages[pillar]["services"].append({
            "service_id": sid,
            "service_name": result["service_name"],
            "tasks": svc_items,
            "total_ext": svc_total_ext,
            "total_int": svc_total_int,
            "man_days": svc_man_days,
        })
        work_packages[pillar]["subtotal_ext"] += svc_total_ext
        work_packages[pillar]["subtotal_int"] += svc_total_int
        work_packages[pillar]["total_man_days"] += svc_man_days
        all_items.extend(svc_items)

    if not all_items:
        return {"error": "No valid services processed. Check service IDs."}

    grand_ext = sum(wp["subtotal_ext"] for wp in work_packages.values())
    grand_int = sum(wp["subtotal_int"] for wp in work_packages.values())
    ppn_amount = grand_ext * ppn_rate

    return {
        "project_name": project_name,
        "generated_date": date.today().isoformat(),
        "version": __version__,
        "parameters": {
            "level": level,
            "complexity": complexity,
            "margin_rate": margin_rate,
            "pph_rate": pph_rate,
            "ppn_rate": ppn_rate,
            "pricing_mode": pricing_mode,
        },
        "total_items": len(all_items),
        "total_services": len([s for wp in work_packages.values() for s in wp["services"]]),
        "total_man_days": sum(i["man_days"] for i in all_items),
        "subtotal_ext": grand_ext,
        "subtotal_int": grand_int,
        "ppn_rate": ppn_rate,
        "ppn_amount": ppn_amount,
        "grand_total_hps": grand_ext + ppn_amount,
        "grand_total_int": grand_int,
        "work_packages": work_packages,
        "items": all_items,
    }


# ---------------------------------------------------------------------------
# Output: CSV (24-column, UTF-8 BOM, hierarchical rows)
# ---------------------------------------------------------------------------
def write_csv(summary: Dict[str, Any], output_path: str) -> None:
    """Write 24-column RAB/HPS CSV with UTF-8 BOM for Excel compatibility.

    Hierarchy is expressed via Level 1-4 columns. No empty separator rows.
    All numeric fields are written as integers (no string-formatted percentages
    in financial columns) so Excel can sum/chart them directly.
    """
    grand_ext = summary["subtotal_ext"]
    p = summary["parameters"]

    try:
        with open(output_path, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh)

            # Metadata rows (4 rows before header)
            w.writerow(["RENCANA ANGGARAN BIAYA (RAB) / HARGA PERKIRAAN SENDIRI (HPS)"] + [""] * 23)
            w.writerow([f"Proyek: {summary['project_name']}"] + [""] * 23)
            param_str = (f"Tanggal: {summary['generated_date']}  |  Level: {p['level']}  |  "
                         f"Kompleksitas: {p['complexity']}  |  Margin: {p['margin_rate']*100:.0f}%  |  "
                         f"PPH: {p['pph_rate']*100:.0f}%  |  PPN: {p['ppn_rate']*100:.0f}%")
            w.writerow([param_str] + [""] * 23)
            w.writerow([""] * 24)

            # Header
            w.writerow(HEADER_24)

            for wp_key in sorted(summary["work_packages"]):
                wp = summary["work_packages"][wp_key]
                wp_label = f"WP{wp_key}: {wp['wp_name']}"

                # WP header row
                row = _empty_row()
                row[0] = wp_label
                row[5] = wp_label
                row[23] = wp["category"]
                w.writerow(row)

                for svc in wp["services"]:
                    svc_label = f"{svc['service_id']}: {svc['service_name']}"

                    # Service header row
                    row = _empty_row()
                    row[1] = svc_label
                    row[5] = svc_label
                    w.writerow(row)

                    # Task data rows
                    for item in svc["tasks"]:
                        pct = (item["total_biaya_ext"] / grand_ext * 100) if grand_ext else 0
                        w.writerow([
                            "",                             # 0  Level 1
                            "",                             # 1  Level 2
                            item["task_id"],                # 2  Level 3
                            "",                             # 3  Level 4
                            item["no"],                     # 4  No.
                            item["description"],            # 5  Komponen
                            item["satuan"],                 # 6  Satuan
                            item["satuan_detail"],          # 7  Satuan Detail
                            item["volume"],                 # 8  Volume
                            item["volume_detail"],          # 9  Volume Detail
                            round(item["est_months"], 2),   # 10 Lama Waktu
                            item["est_people"],             # 11 Jumlah Orang
                            item["perkiraan_total"],        # 12 Perkiraan Total
                            _r(item["harga_dasar"]),        # 13 Harga Dasar
                            round(item["koefisien"], 2),    # 14 Koefisien
                            _r(item["sub_total"]),          # 15 Sub Total
                            _r(item["margin_amount"]),      # 16 Margin
                            _r(item["pph_amount"]),         # 17 PPH
                            _r(item["harga_satuan_int"]),   # 18 Internal
                            _r(item["harga_satuan_ext"]),   # 19 External
                            _r(item["total_biaya_int"]),    # 20 Total Internal
                            _r(item["total_biaya_ext"]),    # 21 Total External
                            round(pct, 2),                  # 22 Persentase
                            item["category"],               # 23 Kategori
                        ])

                    # Service subtotal row
                    svc_pct = (svc["total_ext"] / grand_ext * 100) if grand_ext else 0
                    row = _empty_row()
                    row[1] = "SUBTOTAL"
                    row[5] = f"Subtotal {svc['service_id']}: {svc['service_name']}"
                    row[12] = round(svc["man_days"])
                    row[20] = _r(svc["total_int"])
                    row[21] = _r(svc["total_ext"])
                    row[22] = round(svc_pct, 2)
                    w.writerow(row)

                # WP subtotal row
                wp_pct = (wp["subtotal_ext"] / grand_ext * 100) if grand_ext else 0
                row = _empty_row()
                row[0] = "SUBTOTAL"
                row[5] = f"SUBTOTAL {wp_label}"
                row[12] = round(wp["total_man_days"])
                row[20] = _r(wp["subtotal_int"])
                row[21] = _r(wp["subtotal_ext"])
                row[22] = round(wp_pct, 2)
                w.writerow(row)

            # Grand totals
            row = _empty_row()
            row[5] = "SUBTOTAL (SEBELUM PPN)"
            row[20] = _r(summary["subtotal_int"])
            row[21] = _r(summary["subtotal_ext"])
            row[22] = 100.0
            w.writerow(row)

            row = _empty_row()
            row[5] = f"PPN {summary['ppn_rate']*100:.0f}%"
            row[21] = _r(summary["ppn_amount"])
            w.writerow(row)

            row = _empty_row()
            row[5] = "TOTAL HPS (TERMASUK PPN)"
            row[21] = _r(summary["grand_total_hps"])
            w.writerow(row)

        logger.info("CSV written: %s (%d items, 24 columns, UTF-8 BOM)", output_path, summary["total_items"])

    except IOError as exc:
        logger.error("Failed to write CSV: %s", exc)


def _empty_row() -> list:
    """Return a 24-element list of empty strings."""
    return [""] * 24


# ---------------------------------------------------------------------------
# Output: XLSX (24-column, formatted, auto-width, color-coded)
# ---------------------------------------------------------------------------
def write_xlsx(summary: Dict[str, Any], output_path: str) -> None:
    """Write 24-column RAB/HPS as a formatted Excel workbook with color-coded
    hierarchy rows, auto-width, frozen header, and Rupiah number formatting."""
    try:
        import openpyxl
        from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
    except ImportError:
        logger.error("openpyxl not installed. Run: pip install openpyxl --break-system-packages")
        logger.info("Falling back to CSV output.")
        csv_path = str(Path(output_path).with_suffix(".csv"))
        write_csv(summary, csv_path)
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "RAB-HPS"

    # --- Styles ---
    hdr_font = Font(bold=True, size=10, color="FFFFFF")
    hdr_fill = PatternFill("solid", fgColor="1F4E79")
    wp_fill = PatternFill("solid", fgColor="D6E4F0")
    svc_fill = PatternFill("solid", fgColor="E8F0FE")
    sub_fill = PatternFill("solid", fgColor="FFF2CC")
    total_fill = PatternFill("solid", fgColor="C6EFCE")
    thin = Border(
        left=Side("thin"), right=Side("thin"),
        top=Side("thin"), bottom=Side("thin"),
    )
    rp_fmt = '#,##0'
    pct_fmt = '0.00"%"'
    coef_fmt = '0.00'

    grand_ext = summary["subtotal_ext"]
    p = summary["parameters"]
    cur = 1

    # --- Metadata ---
    ws.cell(cur, 1, "RENCANA ANGGARAN BIAYA (RAB) / HARGA PERKIRAAN SENDIRI (HPS)").font = Font(bold=True, size=14)
    cur += 1
    ws.cell(cur, 1, f"Proyek: {summary['project_name']}").font = Font(bold=True, size=11)
    cur += 1
    ws.cell(cur, 1,
            f"Tanggal: {summary['generated_date']}  |  Level: {p['level']}  |  "
            f"Kompleksitas: {p['complexity']}  |  Margin: {p['margin_rate']*100:.0f}%  |  "
            f"PPH: {p['pph_rate']*100:.0f}%  |  PPN: {p['ppn_rate']*100:.0f}%"
    ).font = Font(size=9, italic=True)
    cur += 2  # blank row

    # --- Header ---
    hdr_row = cur
    for ci, h in enumerate(HEADER_24, 1):
        c = ws.cell(cur, ci, h)
        c.font = hdr_font
        c.fill = hdr_fill
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        c.border = thin
    cur += 1

    # Rupiah columns (0-indexed in HEADER_24)
    rp_cols = {14, 16, 17, 18, 19, 20, 21, 22}  # 1-indexed in Excel
    coef_col = 15
    pct_col = 23

    def _xrow(row_num: int, vals: list, fill=None, bold=False):
        for ci, val in enumerate(vals, 1):
            c = ws.cell(row_num, ci, val if val != "" else None)
            c.border = thin
            if fill:
                c.fill = fill
            if bold:
                c.font = Font(bold=True, size=10)
            if isinstance(val, (int, float)):
                if ci == pct_col:
                    c.number_format = '0.00'
                elif ci == coef_col:
                    c.number_format = coef_fmt
                elif ci in rp_cols:
                    c.number_format = rp_fmt

    for wp_key in sorted(summary["work_packages"]):
        wp = summary["work_packages"][wp_key]
        wp_label = f"WP{wp_key}: {wp['wp_name']}"

        vals = [""] * 24
        vals[0] = wp_label; vals[5] = wp_label; vals[23] = wp["category"]
        _xrow(cur, vals, fill=wp_fill, bold=True); cur += 1

        for svc in wp["services"]:
            svc_label = f"{svc['service_id']}: {svc['service_name']}"
            vals = [""] * 24
            vals[1] = svc_label; vals[5] = svc_label
            _xrow(cur, vals, fill=svc_fill, bold=True); cur += 1

            for item in svc["tasks"]:
                pct = (item["total_biaya_ext"] / grand_ext * 100) if grand_ext else 0
                vals = [
                    "", "", item["task_id"], "",
                    item["no"], item["description"], item["satuan"], item["satuan_detail"],
                    item["volume"], item["volume_detail"],
                    item["est_months"], item["est_people"], item["perkiraan_total"],
                    _r(item["harga_dasar"]), item["koefisien"],
                    _r(item["sub_total"]), _r(item["margin_amount"]), _r(item["pph_amount"]),
                    _r(item["harga_satuan_int"]), _r(item["harga_satuan_ext"]),
                    _r(item["total_biaya_int"]), _r(item["total_biaya_ext"]),
                    round(pct, 2), item["category"],
                ]
                _xrow(cur, vals); cur += 1

            svc_pct = (svc["total_ext"] / grand_ext * 100) if grand_ext else 0
            vals = [""] * 24
            vals[1] = "SUBTOTAL"
            vals[5] = f"Subtotal {svc['service_id']}"
            vals[12] = round(svc["man_days"])
            vals[20] = _r(svc["total_int"]); vals[21] = _r(svc["total_ext"])
            vals[22] = round(svc_pct, 2)
            _xrow(cur, vals, fill=sub_fill, bold=True); cur += 1

        wp_pct = (wp["subtotal_ext"] / grand_ext * 100) if grand_ext else 0
        vals = [""] * 24
        vals[0] = "SUBTOTAL"; vals[5] = f"SUBTOTAL {wp_label}"
        vals[12] = round(wp["total_man_days"])
        vals[20] = _r(wp["subtotal_int"]); vals[21] = _r(wp["subtotal_ext"])
        vals[22] = round(wp_pct, 2)
        _xrow(cur, vals, fill=sub_fill, bold=True); cur += 1

    # Grand totals
    vals = [""] * 24
    vals[5] = "SUBTOTAL (SEBELUM PPN)"
    vals[20] = _r(summary["subtotal_int"]); vals[21] = _r(summary["subtotal_ext"]); vals[22] = 100.0
    _xrow(cur, vals, fill=total_fill, bold=True); cur += 1

    vals = [""] * 24
    vals[5] = f"PPN {summary['ppn_rate']*100:.0f}%"; vals[21] = _r(summary["ppn_amount"])
    _xrow(cur, vals, fill=total_fill, bold=True); cur += 1

    vals = [""] * 24
    vals[5] = "TOTAL HPS (TERMASUK PPN)"; vals[21] = _r(summary["grand_total_hps"])
    _xrow(cur, vals, fill=total_fill, bold=True)

    # Auto-width
    for col in ws.columns:
        max_len = max((len(str(c.value or "")) for c in col), default=8)
        ws.column_dimensions[col[0].column_letter].width = min(max_len + 3, 42)

    ws.freeze_panes = f"A{hdr_row + 1}"

    try:
        wb.save(output_path)
        logger.info("XLSX written: %s (%d items, 24 columns)", output_path, summary["total_items"])
    except IOError as exc:
        logger.error("Failed to write XLSX: %s", exc)


# ---------------------------------------------------------------------------
# Output: Console table (compact, auditable)
# ---------------------------------------------------------------------------
def print_table(summary: Dict[str, Any]) -> None:
    """Print a formatted RAB/HPS table to stdout."""
    SEP = "=" * 130
    DASH = chr(0x2500) * 126

    p = summary["parameters"]
    print(f"\n  {SEP}")
    print("  RENCANA ANGGARAN BIAYA (RAB) / HARGA PERKIRAAN SENDIRI (HPS)")
    print(f"  Proyek    : {summary['project_name']}")
    print(f"  Tanggal   : {summary['generated_date']}")
    print(f"  Parameter : Level {p['level']} | Kompleksitas {p['complexity']} | "
          f"Margin {p['margin_rate']*100:.0f}% | PPH {p['pph_rate']*100:.0f}% | PPN {p['ppn_rate']*100:.0f}%")
    print(f"  Total     : {summary['total_items']} item | {summary['total_man_days']:.0f} man-days | "
          f"{summary['total_services']} layanan")
    print(f"  {SEP}")

    hdr = (f"  {'No':<5} {'Uraian Pekerjaan':<50} {'MD':>5} "
           f"{'Harga Dasar':>15} {'Sub Total':>15} {'Margin':>14} {'PPH':>11} "
           f"{'Harga Satuan':>16} {'%':>7}")

    grand_ext = summary["subtotal_ext"]

    for wp_key in sorted(summary["work_packages"]):
        wp = summary["work_packages"][wp_key]
        print(f"\n  WP{wp_key}: {wp['wp_name'].upper()} [{wp['category']}]")
        print(f"  {DASH}")
        print(hdr)
        print(f"  {DASH}")

        for svc in wp["services"]:
            print(f"  {'':5} {svc['service_id']}: {svc['service_name']}")
            for item in svc["tasks"]:
                pct = (item["total_biaya_ext"] / grand_ext * 100) if grand_ext else 0
                desc = item["description"][:48]
                print(f"  {item['no']:<5} {desc:<50} {item['man_days']:>5.0f} "
                      f"{_fmt(item['harga_dasar']):>15} {_fmt(item['sub_total']):>15} "
                      f"{_fmt(item['margin_amount']):>14} {_fmt(item['pph_amount']):>11} "
                      f"{_fmt(item['harga_satuan_ext']):>16} {pct:>6.1f}%")

            svc_pct = (svc["total_ext"] / grand_ext * 100) if grand_ext else 0
            print(f"  {'':5} {'Subtotal ' + svc['service_id']:>50} {'':>5} "
                  f"{'':>15} {'':>15} {'':>14} {'':>11} "
                  f"{_fmt(svc['total_ext']):>16} {svc_pct:>6.1f}%")
            print(f"  {DASH}")

        wp_pct = (wp["subtotal_ext"] / grand_ext * 100) if grand_ext else 0
        print(f"  {'':5} {'SUBTOTAL WP' + str(wp_key):>50} {'':>5} "
              f"{'':>15} {'':>15} {'':>14} {'':>11} "
              f"{_fmt(wp['subtotal_ext']):>16} {wp_pct:>6.1f}%")

    print(f"\n  {SEP}")
    print(f"  {'SUBTOTAL (SEBELUM PPN)':>95} {_fmt(summary['subtotal_ext']):>16} {'100.0%':>7}")
    ppn_label = f"PPN {summary['ppn_rate']*100:.0f}%"
    print(f"  {ppn_label:>95} {_fmt(summary['ppn_amount']):>16}")
    print(f"  {'─' * 130}")
    print(f"  {'TOTAL HPS (TERMASUK PPN)':>95} {_fmt(summary['grand_total_hps']):>16}")
    print(f"  {SEP}")
    print(f"  {'Internal (COGS basis)':>95} {_fmt(summary['grand_total_int']):>16}")
    margin_val = summary['subtotal_ext'] - summary['subtotal_int']
    margin_pct = (margin_val / summary['subtotal_ext'] * 100) if summary['subtotal_ext'] else 0
    print(f"  {f'Gross Margin ({margin_pct:.1f}%)':>95} {_fmt(margin_val):>16}")
    print()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"IDEAS RAB/HPS Generator v{__version__} — Perpres 46/2025 compliant",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Output: .csv (UTF-8 BOM for Excel), .xlsx (formatted), --json, or console table.\n"
               "Example:\n"
               "  python3 generate_rab.py --project 'Ekosistem Data' --services S1.1,S2.3 --level 10\n"
               "  python3 generate_rab.py --project 'Portal' --services S2.3 --level 8 --output rab.xlsx",
    )
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--services", required=True, help="Comma-separated service IDs")
    parser.add_argument("--level", type=int, default=8, help="Role level 1-24 (default: 8)")
    parser.add_argument("--level-map", type=str, help='JSON: \'{"TATA KELOLA": 12}\'')
    parser.add_argument("--complexity", type=float, default=1.0, help="Complexity multiplier (default: 1.0)")
    parser.add_argument("--margin", type=float, default=DEFAULT_MARGIN_RATE, help=f"Margin (default: {DEFAULT_MARGIN_RATE})")
    parser.add_argument("--pph", type=float, default=DEFAULT_PPH_RATE, help=f"PPH (default: {DEFAULT_PPH_RATE})")
    parser.add_argument("--ppn", type=float, default=DEFAULT_PPN_RATE, help=f"PPN (default: {DEFAULT_PPN_RATE})")
    parser.add_argument("--pricing-mode", choices=["external", "internal"], default="external")
    parser.add_argument("--output", type=str, help="Output path (.csv or .xlsx)")
    parser.add_argument("--json", action="store_true", help="JSON to stdout")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()

    # --- Validation ---
    if not (1 <= args.level <= 24):
        parser.error(f"Level must be between 1 and 24, got {args.level}.")
    for name, val in [("margin", args.margin), ("pph", args.pph), ("ppn", args.ppn)]:
        if not (0 <= val <= 1):
            parser.error(f"--{name} must be between 0 and 1, got {val}.")

    parsed_level_map = None
    if args.level_map:
        try:
            parsed_level_map = json.loads(args.level_map)
        except json.JSONDecodeError:
            parser.error("Invalid JSON for --level-map.")

    service_ids = [s.strip() for s in args.services.split(",") if s.strip()]
    if not service_ids:
        parser.error("No service IDs provided.")

    # --- Generate ---
    result = generate_rab(
        args.project, service_ids, args.level, parsed_level_map,
        args.complexity, args.margin, args.pph, args.ppn, args.pricing_mode,
    )

    if "error" in result:
        logger.critical("Execution failed: %s", result["error"])
        sys.exit(1)

    # --- Output routing ---
    if args.json:
        clean = json.loads(json.dumps(result, default=str))
        print(json.dumps(clean, indent=2, ensure_ascii=False))
    elif args.output:
        ext = Path(args.output).suffix.lower()
        if ext == ".xlsx":
            write_xlsx(result, args.output)
        else:
            write_csv(result, args.output)
        print_table(result)
    else:
        print_table(result)


if __name__ == "__main__":
    main()
