#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# 
#  IDEAS Client Intelligence - SPBE Query Engine
#
#  Version: 1.1.0
#  Last Modified: 2026-02-20
#
#  Description:
#  This script provides a command-line interface to query, analyze, and rank 
#  potential government clients based on the 2024 SPBE evaluation results. 
#  It supports filtering by various criteria, sorting by a calculated 
#  opportunity score, and generating concise pitch briefs for targeted entities.
#
# ------------------------------------------------------------------------------

"""
IDEAS Client Intelligence - SPBE Query Engine

Query and analyze SPBE 2024 data to identify potential government clients.
Supports filtering, ranking by opportunity score, and pitch brief generation.

This script provides a command-line interface to query the SPBE 2024 evaluation results
for both regional governments (Pemda) and central government institutions (K/L).
It calculates an opportunity score to prioritize potential clients based on their
SPBE index, APBD (for regions), and data portal status.

Usage:
    python3 query_spbe.py --top 10 --sort opportunity
    python3 query_spbe.py --province "Jawa Tengah" --portal-status not_accessible
    python3 query_spbe.py --region "Kab. Kutai Kartanegara" --pitch-brief
    python3 query_spbe.py --type kl --top 10
    python3 query_spbe.py --spbe-max 3.0 --apbd-min 5000000000000 --top 20
    python3 query_spbe.py --stats
    python3 query_spbe.py --json --top 5
"""

# Cross-Skill Integration:
#   web-scraper: Use page_scraper.py --ai-extract to refresh SPBE data
#     from government portals before running queries. Use data_pipeline.py
#     to clean and deduplicate scraped SPBE scores.
#   dama-research: Apply KA-14 maturity assessment framework to interpret
#     SPBE scores; use KA-01 governance dimensions for gap analysis.


import argparse
import csv
import json
import logging
import os
import re
import sys
from typing import Any, Dict, List, Optional, Union

# --- Constants & Configuration --- #

# Version Information
__version__ = "1.1.0"
__author__ = "The Manus team"

# File Paths (relative to the script's location)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "references")
DAERAH_CSV_PATH = os.path.join(DATA_DIR, "spbe-2024-daerah.csv")
KL_CSV_PATH = os.path.join(DATA_DIR, "spbe-2024-kl.csv")

# Opportunity Score Weights
PORTAL_SCORE_NOT_FOUND = 3
PORTAL_SCORE_NOT_ACCESSIBLE = 2
SPBE_SCORE_MULTIPLIER = 2
APBD_SCORE_CEILING = 5e12  # 5 Trillion Rupiah

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

# --- Data Parsing Functions --- #

def parse_number(s: Optional[str]) -> float:
    """
    Parse an Indonesian-formatted number string into a float.

    Handles 'Rp' prefix, thousands separators ('.'), and decimal commas (',').
    Returns 0.0 for empty, invalid, or non-string inputs.

    Args:
        s: The string representation of the number.

    Returns:
        The parsed float value, or 0.0 if parsing fails.
    """
    if not s or not isinstance(s, str) or s.strip() == "":
        return 0.0
    s_cleaned = s.strip().replace("Rp", "").replace(".", "").replace(",", ".").strip()
    s_cleaned = re.sub(r'[^-?\d.]', '', s_cleaned)
    try:
        return float(s_cleaned)
    except (ValueError, TypeError):
        logger.debug(f"Could not parse '{s}' as a number.", exc_info=True)
        return 0.0

def parse_spbe(s: Optional[str]) -> float:
    """
    Parse an SPBE score string, which may use a comma as a decimal separator.

    Args:
        s: The string representation of the SPBE score.

    Returns:
        The parsed float value, or 0.0 if parsing fails.
    """
    if not s or not isinstance(s, str) or s.strip() == "":
        return 0.0
    s_cleaned = s.strip().replace(",", ".")
    try:
        return float(s_cleaned)
    except (ValueError, TypeError):
        logger.debug(f"Could not parse '{s}' as an SPBE score.", exc_info=True)
        return 0.0

# --- Data Loading Functions --- #

def load_daerah() -> List[Dict[str, Any]]:
    """
    Load and process regional government (Pemda) SPBE data from the CSV file.

    Calculates an opportunity score for each entity based on SPBE index, APBD,
    and data portal status.

    Returns:
        A list of dictionaries, where each dictionary represents a regional entity.
        Returns an empty list if the data file is not found or fails to load.
    """
    rows: List[Dict[str, Any]] = []
    if not os.path.exists(DAERAH_CSV_PATH):
        logger.error(f"Data file not found at {DAERAH_CSV_PATH}")
        return []

    try:
        with open(DAERAH_CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                apbd = parse_number(row.get("APBD 2024", "0"))
                spbe = parse_spbe(row.get("SPBE", "0"))
                portal_status = (row.get("STATUS PORTAL", "") or "unknown").strip().lower().replace(" ", "_")

                # Opportunity score calculation
                portal_score = PORTAL_SCORE_NOT_FOUND if portal_status == "not_found" else (PORTAL_SCORE_NOT_ACCESSIBLE if portal_status == "not_accessible" else 0)
                spbe_score = max(0, (5.0 - spbe)) * SPBE_SCORE_MULTIPLIER
                apbd_score = min(10, apbd / APBD_SCORE_CEILING)
                opportunity = portal_score + spbe_score + apbd_score

                rows.append({
                    "name": (row.get("PROVINSI/KOTA/KABUPATEN") or "").strip(),
                    "jenis": (row.get("JENIS") or "").strip(),
                    "province": (row.get("NAMA PROV") or "").strip(),
                    "spbe": spbe,
                    "predikat": (row.get("PREDIKAT") or "").strip(),
                    "rank": row.get("RANK", "0"),
                    "apbd": apbd,
                    "apbd_formatted": f"Rp {apbd:,.0f}" if apbd > 0 else "N/A",
                    "portal_name": (row.get("PORTAL DATA") or "").strip(),
                    "portal_link": (row.get("LINK PORTAL DATA") or "").strip(),
                    "portal_status": portal_status,
                    "integrasi_sdi": row.get("INTEGRASI SDI", "0"),
                    "opportunity_score": round(opportunity, 2),
                    "source": "daerah",
                })
    except FileNotFoundError:
        logger.error(f"Data file not found at {DAERAH_CSV_PATH}")
        return []
    except Exception as e:
        logger.error(f"Failed to load or process regional data: {e}", exc_info=True)
        return []
    return rows

def load_kl() -> List[Dict[str, Any]]:
    """
    Load and process central government (K/L) SPBE data from the CSV file.

    Calculates an opportunity score based on SPBE index and portal status.

    Returns:
        A list of dictionaries, where each dictionary represents a K/L entity.
        Returns an empty list if the data file is not found or fails to load.
    """
    rows: List[Dict[str, Any]] = []
    if not os.path.exists(KL_CSV_PATH):
        logger.error(f"Data file not found at {KL_CSV_PATH}")
        return []

    try:
        with open(KL_CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                spbe = parse_spbe(row.get("Indeks", "0"))
                portal = (row.get("Portal Data?") or "").strip().lower()
                portal_link = (row.get("Link Portal Data") or "").strip()

                portal_status = "unknown"
                if portal_link:
                    portal_status = "verified" if portal in ["ya", "yes", "1", "ada"] else "not_accessible"
                else:
                    portal_status = "not_found"

                # Opportunity score for K/L (no APBD)
                portal_score = PORTAL_SCORE_NOT_FOUND if portal_status == "not_found" else (PORTAL_SCORE_NOT_ACCESSIBLE if portal_status == "not_accessible" else 0)
                spbe_score = max(0, (5.0 - spbe)) * SPBE_SCORE_MULTIPLIER
                opportunity = portal_score + spbe_score

                rows.append({
                    "name": (row.get("Nama Instansi") or "").strip(),
                    "jenis": (row.get("Jenis") or "").strip(),
                    "province": "",
                    "spbe": spbe,
                    "predikat": (row.get("Predikat") or "").strip(),
                    "rank": "",
                    "apbd": 0,
                    "apbd_formatted": "N/A",
                    "portal_name": portal,
                    "portal_link": portal_link,
                    "portal_status": portal_status,
                    "integrasi_sdi": "",
                    "opportunity_score": round(opportunity, 2),
                    "source": "kl",
                })
    except FileNotFoundError:
        logger.error(f"Data file not found at {KL_CSV_PATH}")
        return []
    except Exception as e:
        logger.error(f"Failed to load or process K/L data: {e}", exc_info=True)
        return []
    return rows

# --- Data Processing Functions --- #

def filter_data(rows: List[Dict[str, Any]], args: argparse.Namespace) -> List[Dict[str, Any]]:
    """
    Apply command-line argument filters to the dataset.

    Args:
        rows: The list of data rows to filter.
        args: The parsed command-line arguments.

    Returns:
        A new list containing only the filtered rows.
    """
    filtered = rows
    if args.province:
        prov_lower = args.province.lower()
        filtered = [r for r in filtered if prov_lower in r.get("province", "").lower() or prov_lower in r.get("name", "").lower()]
    if args.portal_status:
        ps = args.portal_status.lower().replace(" ", "_")
        filtered = [r for r in filtered if r.get("portal_status") == ps]
    if args.spbe_max is not None:
        filtered = [r for r in filtered if r.get("spbe", 0) <= args.spbe_max and r.get("spbe", 0) > 0]
    if args.spbe_min is not None:
        filtered = [r for r in filtered if r.get("spbe", 0) >= args.spbe_min]
    if args.apbd_min is not None:
        filtered = [r for r in filtered if r.get("apbd", 0) >= args.apbd_min]
    if args.jenis:
        j = args.jenis.lower()
        filtered = [r for r in filtered if j in r.get("jenis", "").lower()]
    return filtered

def sort_data(rows: List[Dict[str, Any]], sort_key: str) -> List[Dict[str, Any]]:
    """
    Sort data by a specified key.

    Args:
        rows: The list of data rows to sort.
        sort_key: The key to sort by (e.g., 'opportunity', 'spbe_asc').

    Returns:
        A new list containing the sorted rows.
    """
    key_map = {
        "opportunity": ("opportunity_score", True),
        "spbe_asc": ("spbe", False),
        "spbe_desc": ("spbe", True),
        "apbd": ("apbd", True),
        "name": ("name", False),
    }

    if sort_key not in key_map:
        logger.warning(f"Invalid sort key '{sort_key}'. Returning unsorted data.")
        return rows

    key, reverse = key_map[sort_key]

    def sort_func(x: Dict[str, Any]) -> Union[float, str]:
        val = x.get(key, 0)
        # Special handling for ascending SPBE sort to put 0s at the end
        if sort_key == "spbe_asc" and val == 0:
            return float('inf')
        return val

    try:
        return sorted(rows, key=sort_func, reverse=reverse)
    except TypeError:
        logger.error(f"Type error while sorting by key '{key}'. Returning unsorted data.")
        return rows

# --- Output Functions --- #

def print_table(rows: List[Dict[str, Any]], top_n: Optional[int] = None) -> None:
    """
    Print a formatted table of results to the console.

    Args:
        rows: The data rows to print.
        top_n: The maximum number of rows to display.
    """
    if not rows:
        print("No matching records found.")
        return

    display_rows = rows[:top_n] if top_n else rows

    print(f"\n{'No':<4} {'Nama':<45} {'Jenis':<12} {'SPBE':>5} {'Predikat':<14} {'Portal Status':<16} {'APBD':>22} {'Opp.':>5}")
    print("─" * 130)
    for i, r in enumerate(display_rows, 1):
        apbd = r.get('apbd', 0)
        if apbd > 1e11:
            apbd_str = f"Rp {apbd / 1e12:.1f}T"
        elif apbd > 0:
            apbd_str = f"Rp {apbd / 1e9:.1f}M"
        else:
            apbd_str = "N/A"
        
        print(f"{i:<4} {(r.get('name', '') or '')[:43]:<45} {(r.get('jenis', '') or '')[:10]:<12} {r.get('spbe', 0):>5.2f} {(r.get('predikat', '') or '')[:12]:<14} "
              f"{(r.get('portal_status', '') or ''):<16} {apbd_str:>22} {r.get('opportunity_score', 0):>5.1f}")
    print("─" * 130)
    print(f"Showing {len(display_rows)} of {len(rows)} records\n")

def print_stats(rows: List[Dict[str, Any]]) -> None:
    """
    Print summary statistics for the loaded data.

    Args:
        rows: The data for which to print statistics.
    """
    total = len(rows)
    if total == 0:
        print("No data available for statistics.")
        return

    portal_counts: Dict[str, int] = {}
    for r in rows:
        ps = r.get("portal_status", "unknown")
        portal_counts[ps] = portal_counts.get(ps, 0) + 1

    spbe_scores = [r.get("spbe", 0) for r in rows if r.get("spbe", 0) > 0]
    avg_spbe = (sum(spbe_scores) / len(spbe_scores)) if spbe_scores else 0

    predikat_counts: Dict[str, int] = {}
    for r in rows:
        p = r.get("predikat") if r.get("predikat") else "N/A"
        predikat_counts[p] = predikat_counts.get(p, 0) + 1

    print(f"\n{'='*60}")
    print(f"  SPBE 2024 STATISTICS (n={total})")
    print(f"{'='*60}")
    print(f"  Average SPBE Score: {avg_spbe:.2f}")
    print("\n  Portal Status Distribution:")
    for ps, count in sorted(portal_counts.items(), key=lambda item: item[1], reverse=True):
        pct = (count / total) * 100
        print(f"    {ps:<20} {count:>5} ({pct:.1f}%)")
    print("\n  Predikat Distribution:")
    for p, count in sorted(predikat_counts.items(), key=lambda item: item[1], reverse=True):
        pct = (count / total) * 100
        print(f"    {p:<20} {count:>5} ({pct:.1f}%)")
    print(f"{'='*60}\n")

def print_pitch_brief(row: Dict[str, Any]) -> None:
    """
    Generate and print a structured pitch brief for a specific entity.

    Args:
        row: The data row for the entity.
    """
    print(f"\n{'='*70}")
    print(f"  PITCH BRIEF: {row.get('name')}")
    print(f"{'='*70}")
    print(f"  - Jenis        : {row.get('jenis', 'N/A')}")
    print(f"  - Provinsi     : {row.get('province', 'N/A')}")
    print(f"  - SPBE Score   : {row.get('spbe', 0):.2f} ({row.get('predikat', 'N/A')})")
    print(f"  - APBD 2024    : {row.get('apbd_formatted', 'N/A')}")
    print(f"  - Portal Data  : {row.get('portal_name') or 'N/A'}")
    print(f"  - Portal Link  : {row.get('portal_link') or 'N/A'}")
    print(f"  - Portal Status: {row.get('portal_status', 'unknown')}")
    print(f"  - Opp. Score   : {row.get('opportunity_score', 0)}")
    print("-" * 70)

    print("  REKOMENDASI LAYANAN:")
    if row.get("portal_status") in ["not_found", "not_accessible"]:
        print("  1. [HIGH] S2.3 Government Data Portal Platform")
    if row.get("spbe", 5) < 3.5:
        print("  2. [HIGH] S1.1 Data Strategy & Roadmap Development")
        print(f"     -> Skor SPBE {row.get('spbe', 0):.2f} menunjukkan perlunya strategi data yang komprehensif.")
    if row.get("spbe", 5) < 4.0:
        print("  3. [MEDIUM] S1.2 Data Governance & Compliance Framework")
        print("     -> Implementasi tata kelola data untuk perbaikan domain kunci SPBE.")
    print("  4. [MEDIUM] S1.3 Data Maturity Assessment & Benchmarking")
    print("     -> Lakukan asesmen kematangan data sebagai baseline program perbaikan berkelanjutan.")
    if row.get("spbe", 0) > 0:
        print("  5. [LOW] S3.2 Data Literacy & Culture Program")
        print("     -> Program literasi untuk meningkatkan adopsi dan pemanfaatan data di seluruh OPD/unit.")
    print("-" * 70)

    print("  TALKING POINTS:")
    print("  - Referensi Sukses: Ekosistem Data Jabar (Indeks SPBE 4.58 di 2023, salah satu tertinggi nasional).")
    print("  - Kepatuhan Regulasi: Mendukung Perpres 39/2019 (Satu Data Indonesia), UU 27/2022 (PDP), dan Perpres 132/2022 (Arsitektur SPBE).")
    print("  - Diferensiasi IDEAS: Bukan hanya portal, tapi ekosistem data terintegrasi 7-komponen yang holistik.")
    print(f"{'='*70}\n")

# --- Main Execution --- #

def main() -> None:
    """Main function to parse arguments and drive the script execution."""
    parser = argparse.ArgumentParser(
        description="IDEAS Client Intelligence - SPBE Query Engine (Data from 2024 Evaluation)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--type", choices=['daerah', 'kl', 'all'], default="daerah", help="Tipe data: daerah, kl, atau all. Default: daerah.")
    parser.add_argument("--province", type=str, help="Filter berdasarkan nama provinsi (pencocokan parsial).")
    parser.add_argument("--portal-status", type=str, choices=['not_found', 'not_accessible', 'verified', 'unknown'], help="Filter berdasarkan status portal data.")
    parser.add_argument("--spbe-max", type=float, help="Filter SPBE dengan skor maksimal tertentu.")
    parser.add_argument("--spbe-min", type=float, help="Filter SPBE dengan skor minimal tertentu.")
    parser.add_argument("--apbd-min", type=float, help="Filter APBD dengan nilai minimal tertentu (dalam Rupiah).")
    parser.add_argument("--jenis", type=str, help="Filter berdasarkan jenis (Provinsi, Kabupaten, Kota, Kementerian, Lembaga).")
    parser.add_argument("--region", type=str, help="Cari institusi spesifik dan tampilkan pitch brief-nya.")
    parser.add_argument("--pitch-brief", action="store_true", help="Tampilkan pitch brief untuk hasil pencarian --region.")
    parser.add_argument("--sort", choices=['opportunity', 'spbe_asc', 'spbe_desc', 'apbd', 'name'], default="opportunity", help="Kunci untuk pengurutan data.")
    parser.add_argument("--top", type=int, help="Tampilkan N hasil teratas.")
    parser.add_argument("--stats", action="store_true", help="Tampilkan statistik ringkasan dari data.")
    parser.add_argument("--json", action="store_true", help="Output hasil dalam format JSON.")
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    # Load data
    data: List[Dict[str, Any]] = []
    if args.type in ['daerah', 'all']:
        data.extend(load_daerah())
    if args.type in ['kl', 'all']:
        data.extend(load_kl())

    if not data:
        logger.critical("Failed to load any data. Exiting.")
        sys.exit(1)

    # Handle different modes
    if args.stats:
        print_stats(data)
        return

    if args.region:
        region_lower = args.region.lower()
        matches = [r for r in data if region_lower in r.get("name", "").lower()]
        if not matches:
            logger.warning(f"No institution found matching '{args.region}'")
            sys.exit(1)
        
        output_items = matches
        if args.pitch_brief or len(matches) == 1:
            output_items = matches[:5] # Limit to 5 briefs
            if args.json:
                print(json.dumps(output_items, indent=2, ensure_ascii=False))
            else:
                for item in output_items:
                    print_pitch_brief(item)
        else:
            output_items = matches[:20] # Limit to 20 table rows
            if args.json:
                print(json.dumps(output_items, indent=2, ensure_ascii=False))
            else:
                print_table(output_items, 20)
        return

    # Default mode: filter, sort, and print
    filtered_data = filter_data(data, args)
    sorted_data = sort_data(filtered_data, args.sort)

    if args.json:
        output_data = sorted_data[:args.top] if args.top else sorted_data
        print(json.dumps(output_data, indent=2, ensure_ascii=False))
    else:
        print_table(sorted_data, args.top)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}", exc_info=True)
        sys.exit(1)
