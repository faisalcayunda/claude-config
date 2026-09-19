#!/usr/bin/env python3
"""
IDEAS Project Cost Calculator (2026) - Unified
Version: 1.1.0

Calculates personnel costs for IDEAS project proposals using the unified
pricing_engine. This script acts as a user-friendly CLI for the engine.

Usage:
    # Get standard external client price for a role
    python3 calculate_project_cost.py --role "Data Analyst" --level 8 --months 6

    # Get freelancer daily rate
    python3 calculate_project_cost.py --role "Data Analyst" --level 8 --model freelancer --unit day

    # Calculate cost for a full team from a JSON file
    python3 calculate_project_cost.py --team team_spec.json

    # Get a full cost breakdown for a role
    python3 calculate_project_cost.py --role "Data Scientist" --level 15 --breakdown

    # List all available roles
    python3 calculate_project_cost.py --list-roles
"""

import argparse
import json
import sys
import logging
from typing import Dict, Any, Optional, List, Union

# --- Configuration ---
# Centralized configuration for default values and script behavior.
# FUTURE IMPROVEMENT: This could be loaded from an external config file (e.g., YAML or .ini)
# to allow for easier modification without changing the script source code.
CONFIG: Dict[str, Union[int, float, str]] = {
    "DEFAULT_LEVEL": 5,
    "DEFAULT_DURATION": 1.0,
    "DEFAULT_QTY": 1,
    "DEFAULT_UNIT": "month",
    "DEFAULT_MODEL": "fulltime",
    "CURRENCY_SYMBOL": "Rp",
    "TEAM_SPEC_FILENAME": "team_spec.json"
}

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Import from the Unified Pricing Engine ---
# FUTURE IMPROVEMENT: Implement dynamic loading of the pricing engine to decouple this script
# from the engine's direct file structure. This would make the script more robust to changes
# in the underlying library.
try:
    from pricing_engine import (
        RATE_CARD,
        get_cost_breakdown,
        get_external_price,
        get_freelancer_price,
        get_daily_rate,
        get_hourly_rate
    )
except ImportError as e:
    logger.error("Fatal: The 'pricing_engine.py' module was not found. %s", e)
    print("Error: The 'pricing_engine.py' module was not found.", file=sys.stderr)
    print("Please ensure it is in the same directory or in the Python path.", file=sys.stderr)
    sys.exit(1)

def fmt(val: Union[int, float, str]) -> str:
    """Formats a numeric value as an Indonesian Rupiah currency string.

    Args:
        val: The numeric value to format.

    Returns:
        A string formatted as 'Rp {value:,.0f}' or the original value if not numeric.
    """
    if not isinstance(val, (int, float)):
        return str(val)
    return f'{CONFIG["CURRENCY_SYMBOL"]} {val:,.0f}'

def calculate_total_cost(role: str, level: int, unit: str = "month", model: str = "fulltime", duration: float = 1.0, qty: int = 1) -> Dict[str, Any]:
    """Calculates the total cost for a given role based on various parameters.

    This function fetches the base rate from the pricing engine according to the specified
    unit and pricing model, then calculates the total cost based on the duration and quantity.

    Args:
        role: The title of the role to calculate.
        level: The seniority level of the role (1-24).
        unit: The unit of time for the calculation ('month', 'day', 'hour').
        model: The pricing model ('fulltime' or 'freelancer').
        duration: The duration of the engagement in the specified units.
        qty: The number of personnel for this role.

    Returns:
        A dictionary containing the detailed cost calculation or an error message.
    """
    logger.info(f"Calculating cost for role='{role}', level={level}, unit='{unit}', model='{model}', duration={duration}, qty={qty}")
    role_key = next((key for key in RATE_CARD if key.lower() == role.lower()), None)

    if not role_key:
        error_msg = f"Role '{role}' not found. Use --list-roles to see available roles."
        logger.error(error_msg)
        return {"error": error_msg}

    try:
        if unit == "month":
            base_rate = get_external_price(role_key, level) if model == "fulltime" else get_freelancer_price(role_key, level)
        elif unit == "day":
            base_rate = get_daily_rate(role_key, level, model)
        elif unit == "hour":
            base_rate = get_hourly_rate(role_key, level, model)
        else:
            error_msg = f"Invalid unit '{unit}'. Valid units are 'month', 'day', 'hour'."
            logger.error(error_msg)
            return {"error": error_msg}

        if isinstance(base_rate, dict) and "error" in base_rate:
            logger.warning(f"Error from pricing engine for {role_key} (L{level}): {base_rate['error']}")
            return base_rate

    except Exception as e:
        error_msg = f"Could not calculate rate for {role} (L{level}): {e}"
        logger.exception(error_msg) # Log with stack trace
        return {"error": error_msg}

    total_cost = base_rate * duration * qty
    logger.info(f"Successfully calculated cost for {role_key}: {total_cost}")

    return {
        "role": role_key,
        "level": level,
        "unit": unit,
        "model": model,
        "duration": duration,
        "qty": qty,
        "rate_per_unit": fmt(base_rate),
        "total_cost": fmt(total_cost),
        "total_cost_raw": total_cost,
    }

def list_roles(category_filter: Optional[str] = None, group_filter: Optional[str] = None) -> None:
    """Prints a formatted list of all available roles from the RATE_CARD.

    Args:
        category_filter: An optional string to filter roles by category.
        group_filter: An optional string to filter roles by group.
    """
    header = "{:<50} {:<12} {:<25}".format("Role", "Category", "Group")
    print("\n" + header)
    print("-" * 90)
    count = 0
    sorted_roles = sorted(RATE_CARD.items(), key=lambda x: (x[1]["category"], x[0]))

    for role, info in sorted_roles:
        if category_filter and info["category"].lower() != category_filter.lower():
            continue
        if group_filter and info["group"].lower() != group_filter.lower():
            continue
        print("{:<50} {:<12} {:<25}".format(role, info["category"], info["group"]))
        count += 1
    print(f"\nShowing: {count} roles (Total in system: {len(RATE_CARD)})")

def main() -> None:
    """Main function to parse arguments and execute the cost calculation logic."""
    parser = argparse.ArgumentParser(
        description="IDEAS Unified Project Cost Calculator (2026)",
        epilog="Example: python3 calculate_project_cost.py --role \"Data Scientist\" --level 15 --breakdown"
    )
    parser.add_argument("--role", type=str, help="Role title (e.g., 'Data Analyst')")
    parser.add_argument("--level", type=int, default=CONFIG["DEFAULT_LEVEL"], help=f"Level (1-24, default: {CONFIG['DEFAULT_LEVEL']})")
    parser.add_argument("--duration", type=float, default=CONFIG["DEFAULT_DURATION"], help=f"Duration in the specified unit (default: {CONFIG['DEFAULT_DURATION']})")
    parser.add_argument("--qty", type=int, default=CONFIG["DEFAULT_QTY"], help=f"Number of personnel (default: {CONFIG['DEFAULT_QTY']})")
    parser.add_argument("--unit", type=str, choices=["month", "day", "hour"], default=CONFIG["DEFAULT_UNIT"], help="Unit of calculation")
    parser.add_argument("--model", type=str, choices=["fulltime", "freelancer"], default=CONFIG["DEFAULT_MODEL"], help="Pricing model")
    parser.add_argument("--team", type=str, default=None, help=f"Path to team spec JSON file (default: {CONFIG['TEAM_SPEC_FILENAME']})")
    parser.add_argument("--breakdown", action="store_true", help="Show full cost breakdown for a single role or entire team")
    parser.add_argument("--list-roles", action="store_true", help="List all available roles and exit")
    parser.add_argument("--category", type=str, help="Filter roles by category (used with --list-roles)")
    parser.add_argument("--group", type=str, help="Filter roles by group: Board, PDT, Biz&Digital, DAMA (used with --list-roles)")
    parser.add_argument("--months", type=float, help=argparse.SUPPRESS) # Legacy support

    args = parser.parse_args()

    if not (1 <= args.level <= 24):
        parser.error(f"Level must be between 1 and 24, got {args.level}.")

    if args.list_roles:
        list_roles(args.category, args.group)
        return

    duration = args.months if args.months is not None else args.duration

    if args.team:
        try:
            with open(args.team) as f:
                team = json.load(f)
        except FileNotFoundError:
            logger.error(f"Team spec file not found at '{args.team}'")
            print(f"Error: Team spec file not found at '{args.team}'", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in team spec file '{args.team}': {e}")
            print(f"Error: Invalid JSON in team spec file '{args.team}'", file=sys.stderr)
            sys.exit(1)

        results: List[Dict[str, Any]] = []
        grand_total = 0
        header = "{:<3} {:<35} {:<5} {:<10} {:<10} {:<8} {:<4} {:<20}".format(
            "#", "Role", "Lvl", "Unit", "Model", "Duration", "Qty", "Total")
        print("\n" + header)
        print("-" * 110)

        for i, member in enumerate(team, 1):
            result = calculate_total_cost(
                member.get("role"),
                member.get("level", CONFIG["DEFAULT_LEVEL"]),
                member.get("unit", CONFIG["DEFAULT_UNIT"]),
                member.get("model", CONFIG["DEFAULT_MODEL"]),
                member.get("duration", CONFIG["DEFAULT_DURATION"]),
                member.get("qty", CONFIG["DEFAULT_QTY"])
            )
            if "error" in result:
                print(f"  ERROR processing team member #{i} ({member.get('role', 'N/A')}): {result['error']}", file=sys.stderr)
                continue

            results.append(result)
            grand_total += result["total_cost_raw"]
            print("{:<3} {:<35} {:<5} {:<10} {:<10} {:<8.1f} {:<4} {:<20}".format(
                i, result["role"], result["level"], result["unit"], result["model"],
                result["duration"], result["qty"], result["total_cost"]))

        print("-" * 110)
        print("{:<87} {}".format("GRAND TOTAL", fmt(grand_total)))

        if args.breakdown:
            print("\n--- Team Cost Breakdown ---")
            for i, member in enumerate(team, 1):
                breakdown = get_cost_breakdown(member["role"], member.get("level", CONFIG["DEFAULT_LEVEL"]))
                if "error" in breakdown:
                    print(f"\n#{i}: Could not get breakdown for {member['role']}: {breakdown['error']}", file=sys.stderr)
                    continue
                print(f"\n#{i}: {member['role']} (L{member.get('level', CONFIG['DEFAULT_LEVEL'])})")

                for key, val in breakdown.items():
                    if key not in ['role', 'level']:
                        print(f"  {key:<28}: {fmt(val)}")

    elif args.role:
        if args.breakdown:
            result = get_cost_breakdown(args.role, args.level)
            if 'error' in result:
                 print(f"Error: {result['error']}", file=sys.stderr)
                 sys.exit(1)
            print("\n--- Full Cost Breakdown ---")
            print(f"Role:  {result['role']}")
            print(f"Level: {result['level']}\n")
            for key, val in result.items():
                if key not in ['role', 'level']:
                    print(f"{key:<30}: {fmt(val)}")
        else:
            result = calculate_total_cost(args.role, args.level, args.unit, args.model, duration, args.qty)
            if 'error' in result:
                print(json.dumps(result, indent=2, ensure_ascii=False), file=sys.stderr)
                sys.exit(1)
            print(json.dumps(result, indent=2, ensure_ascii=False))

    else:
        parser.print_help()
        sys.exit(0)

if __name__ == "__main__":
    main()
