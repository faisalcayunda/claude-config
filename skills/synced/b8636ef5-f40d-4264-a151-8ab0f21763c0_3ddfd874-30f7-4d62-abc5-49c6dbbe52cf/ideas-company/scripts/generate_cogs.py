#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IDEAS COGS Generator — Full 4-Component Model.

Version: 1.1.0

Calculates the complete Cost of Goods Sold (COGS) estimate, which for IT
consulting is often referred to as Cost of Revenue (COR). This script models
all four key cost components: People, Software, Hardware, and Operational.

Industry benchmarks suggest SaaS companies target a 70-80% gross margin, while
IT consulting firms typically achieve 40-60%. The IDEAS standard margin is
30%, as defined in the 'pricing_engine.py' script.

Components:
  1. People (Biaya Tenaga Kerja Langsung): Derived from feature allocation JSON.
  2. Software (Biaya Perangkat Lunak): Derived from a software list JSON.
  3. Hardware (Biaya Perangkat Keras): Derived from a hardware list JSON.
  4. Operational (Biaya Operasional): Derived from an operational costs JSON.

Usage:
    # Calculate People cost only (original mode)
    python3 generate_cogs.py --input feature_allocation.json

    # Calculate full 4-component COGS
    python3 generate_cogs.py --input feature_allocation.json --software sw.json --hardware hw.json --operational ops.json

    # Output results in JSON format
    python3 generate_cogs.py --input feature_allocation.json --json

    # Filter by MoSCoW priority (e.g., only 'Must Have' features)
    python3 generate_cogs.py --input feature_allocation.json --priority must

Input JSON format for feature_allocation.json:
    [
        {"feature": "Data Catalog", "role": "Front-End Engineer", "level": "Senior", "man_days": 10, "priority": "Must Have"},
        {"feature": "Data Catalog", "role": "Back-End Engineer", "level": "Middle", "man_days": 15, "priority": "Must Have"}
    ]

Input JSON format for software/hardware/operational files:
    [
        {"item": "GitLab Enterprise", "category": "Product Development", "unit_price": 348, "currency": "USD", "quantity": 52, "kurs": 17500},
        {"item": "Rack Server", "category": "Infrastructure", "unit_price": 86752050, "currency": "IDR", "quantity": 1}
    ]
"""

import argparse
import json
import sys
import logging
from typing import List, Dict, Any, Optional, Callable

# --- Configuration ---
PPN_RATE = 0.11  # VAT rate as per Law No. 7 of 2021.
DEFAULT_KURS_USD = 17500  # Default USD to IDR exchange rate.
WORKING_DAYS_PER_MONTH = 20 # Standard working days in a month.
LEVEL_MAPPING = {
    "Senior": 10,
    "Middle": 7,
    "Junior": 3,
}
PRIORITY_ORDER = ["Must Have", "Should Have", "Could Have"]

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    stream=sys.stderr)
logger = logging.getLogger(__name__)

# --- Dependency Check ---
try:
    from pricing_engine import get_internal_daily_rate, RATE_CARD
except ImportError:
    logger.critical("Error: pricing_engine.py not found. Ensure it is in the same directory or accessible in the PYTHONPATH.")
    sys.exit(1)

# --- Helper Functions ---

def fmt(val: float) -> str:
    """Formats a numeric value into a Rupiah currency string."""
    return f"Rp {val:,.0f}"

# --- Core Calculation Functions ---

def generate_people_cost(input_file: str, priority_filter: Optional[str] = None) -> Dict[str, Any]:
    """Calculates People cost from a feature allocation JSON file.

    Args:
        input_file: Path to the JSON file with feature allocations.
        priority_filter: An optional string to filter features by MoSCoW priority.

    Returns:
        A dictionary containing calculated cost items, total cost, and any errors.
    """
    try:
        with open(input_file, 'r') as f:
            allocations = json.load(f)
    except FileNotFoundError:
        logger.error(f"Input file not found: {input_file}")
        return {"error": f"Input file not found: {input_file}"}
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {input_file}: {e}")
        return {"error": f"Invalid JSON in {input_file}. Please check the file format."}
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading {input_file}: {e}")
        return {"error": f"An unexpected error occurred while reading {input_file}: {e}"}

    items: List[Dict[str, Any]] = []
    total: float = 0
    errors: List[str] = []

    if not isinstance(allocations, list):
        msg = f"Input must be a JSON array of objects, got {type(allocations).__name__}. Expected: [{{'feature': ..., 'role': ..., 'level': ..., 'man_days': ...}}]"
        logger.error(msg)
        return {"error": msg}

    for idx, alloc in enumerate(allocations):
        line_num = idx + 2  # JSON array starts at line 2
        if not isinstance(alloc, dict):
            msg = f"L{line_num}: Each item must be a JSON object, got {type(alloc).__name__}. Skipping."
            errors.append(msg)
            logger.warning(msg)
            continue
        feature = alloc.get('feature', 'N/A')
        role = alloc.get('role', 'N/A')
        raw_level = alloc.get('level', 'N/A')
        man_days = alloc.get('man_days', 0)
        priority = alloc.get('priority', 'Must Have')

        if priority_filter and priority.lower().replace(" ", "") != priority_filter.lower().replace(" ", ""):
            continue

        if isinstance(raw_level, int):
            level_str = 'Senior' if raw_level >= 9 else 'Middle' if raw_level >= 5 else 'Junior'
        else:
            level_str = str(raw_level).capitalize()

        if level_str not in LEVEL_MAPPING:
            msg = f"L{line_num}: Invalid level '{alloc.get('level')}' for feature '{feature}'. Valid levels are Senior, Middle, Junior."
            errors.append(msg)
            logger.warning(msg)
            continue

        level_num = LEVEL_MAPPING[level_str]
        role_key = next((key for key in RATE_CARD if key.lower() == role.lower()), None)

        if role_key is None:
            msg = f"L{line_num}: Role '{role}' not found for feature '{feature}'. Check pricing_engine.py for available roles."
            errors.append(msg)
            logger.warning(msg)
            continue

        try:
            daily_rate = get_internal_daily_rate(role_key, level_num)
            cost = man_days * daily_rate
            items.append({
                "feature": feature,
                "role": role_key,
                "level": level_str,
                "man_days": man_days,
                "daily_rate": daily_rate,
                "cost": cost,
                "priority": priority,
            })
            total += cost
        except Exception as e:
            msg = f"L{line_num}: Could not calculate cost for role '{role_key}' and level {level_num}. Error: {e}"
            errors.append(msg)
            logger.error(msg)

    return {"items": items, "total": total, "errors": errors}

def generate_component_cost(input_file: Optional[str], cost_calculator_func: Callable[[List[Dict]], Dict]) -> Dict[str, Any]:
    """Generic function to calculate cost for a component (Software, Hardware, Operational)."""
    if not input_file:
        return {"items": [], "total": 0, "errors": []}
    try:
        with open(input_file, 'r') as f:
            item_list = json.load(f)
    except FileNotFoundError:
        return {"items": [], "total": 0, "errors": [f"File not found: {input_file}"]}
    except json.JSONDecodeError:
        return {"items": [], "total": 0, "errors": [f"Invalid JSON in {input_file}"]}
    except Exception as e:
        return {"items": [], "total": 0, "errors": [f"An unexpected error occurred: {e}"]}

    return cost_calculator_func(item_list)

def calc_software_cost(software_list: List[Dict]) -> Dict[str, Any]:
    """Calculates total software cost from a list of items, including PPN."""
    items, total = [], 0
    for sw in software_list:
        unit_price = sw.get('unit_price', 0)
        quantity = sw.get('quantity', 1)
        currency = sw.get('currency', 'IDR').upper()
        kurs = sw.get('kurs', DEFAULT_KURS_USD)
        dpp = (unit_price * quantity * kurs) if currency == 'USD' else (unit_price * quantity)
        ppn = dpp * PPN_RATE
        total_cost = dpp + ppn
        items.append({**sw, "dpp": dpp, "ppn": ppn, "total_cost": total_cost})
        total += total_cost
    return {"items": items, "total": total, "errors": []}

def calc_hardware_cost(hardware_list: List[Dict]) -> Dict[str, Any]:
    """Calculates total hardware cost from a list of items."""
    items, total = [], 0
    for hw in hardware_list:
        total_cost = hw.get('unit_price', 0) * hw.get('quantity', 1)
        items.append({**hw, "total_cost": total_cost})
        total += total_cost
    return {"items": items, "total": total, "errors": []}

def calc_operational_cost(ops_list: List[Dict]) -> Dict[str, Any]:
    """Calculates total operational cost from a list of items."""
    items, total = [], 0
    for op in ops_list:
        total_cost = op.get('people', 1) * op.get('months', 1) * op.get('monthly_rate', 0)
        items.append({**op, "total_cost": total_cost})
        total += total_cost
    return {"items": items, "total": total, "errors": []}

def generate_full_cogs(people: Dict, software: Optional[Dict] = None, hardware: Optional[Dict] = None, operational: Optional[Dict] = None) -> Dict[str, Any]:
    """Aggregates all four COGS components into a single report."""
    sw = software or {"items": [], "total": 0, "errors": []}
    hw = hardware or {"items": [], "total": 0, "errors": []}
    ops = operational or {"items": [], "total": 0, "errors": []}

    total_cogs = people["total"] + sw["total"] + hw["total"] + ops["total"]

    return {
        "components": {
            "people": {"total": people["total"], "item_count": len(people["items"])},
            "software": {"total": sw["total"], "item_count": len(sw["items"])},
            "hardware": {"total": hw["total"], "item_count": len(hw["items"])},
            "operational": {"total": ops["total"], "item_count": len(ops["items"])},
        },
        "total_cogs": total_cogs,
        "people_detail": people,
        "software_detail": sw,
        "hardware_detail": hw,
        "operational_detail": ops,
        "all_errors": people.get("errors", []) + sw.get("errors", []) + hw.get("errors", []) + ops.get("errors", []),
    }

# --- Output Functions ---

def print_cogs_table(cogs: Dict[str, Any]):
    """Prints a formatted COGS summary table to the console."""
    print(f"\n{'='*90}")
    print(f"  IDEAS COGS (HARGA POKOK PENJUALAN) SUMMARY")
    print(f"{'='*90}")

    print(f"\n  {'Component':<50} {'Items':>8} {'Total Cost':>25}")
    print(f"  {'-'*83}")
    for name, comp in cogs["components"].items():
        label = name.replace('_', ' ').upper()
        print(f"  {label:<50} {comp['item_count']:>8} {fmt(comp['total']):>25}")
    print(f"  {'-'*83}")
    print(f"  {'TOTAL COGS':<50} {'':>8} {fmt(cogs['total_cogs']):>25}")
    print(f"  {'='*83}")

    people = cogs["people_detail"]
    if people["items"]:
        print(f"\n  --- PEOPLE COST DETAIL ---")
        print(f"  {'Feature':<35} {'Role':<30} {'Level':<8} {'Days':>6} {'Cost':>20}")
        print(f"  {'-'*99}")
        for item in sorted(people["items"], key=lambda x: x['feature']):
            print(f"  {item['feature'][:34]:<35} {item['role'][:29]:<30} {item['level']:<8} {item['man_days']:>6} {fmt(item['cost']):>20}")
        print(f"  {'-'*99}")
        print(f"  {'SUBTOTAL PEOPLE':<79} {fmt(people['total']):>20}")

    if cogs["all_errors"]:
        print(f"\n  Warnings/Errors Encountered:")
        for err in cogs["all_errors"]:
            print(f"  - {err}")

    print()

# --- Main Execution ---

def main():
    """Main function to parse arguments and run the COGS generation process."""
    parser = argparse.ArgumentParser(
        description="IDEAS COGS Generator — Full 4-Component Model",
        epilog="Example: python3 generate_cogs.py --input features.json --software sw.json --json",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--input", required=True, help="Path to feature allocation JSON (People cost)")
    parser.add_argument("--software", help="Path to software list JSON")
    parser.add_argument("--hardware", help="Path to hardware list JSON")
    parser.add_argument("--operational", help="Path to operational list JSON")
    parser.add_argument("--priority", choices=['must', 'should', 'could'], help="Filter by MoSCoW priority (e.g., 'must' for Must Have)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format instead of a table")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging output")
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    priority_map = {"must": "Must Have", "should": "Should Have", "could": "Could Have"}
    priority_filter = priority_map.get(args.priority)

    logger.info(f"Starting COGS generation for input: {args.input}")
    people = generate_people_cost(args.input, priority_filter)
    if "error" in people:
        logger.critical(f"Fatal Error processing people cost: {people['error']}")
        sys.exit(1)

    software = generate_component_cost(args.software, calc_software_cost)
    hardware = generate_component_cost(args.hardware, calc_hardware_cost)
    operational = generate_component_cost(args.operational, calc_operational_cost)

    cogs = generate_full_cogs(people, software, hardware, operational)

    if args.json:
        print(json.dumps(cogs, indent=2, ensure_ascii=False, default=str))
    else:
        print_cogs_table(cogs)
    
    logger.info("COGS generation completed successfully.")

if __name__ == "__main__":
    main()
