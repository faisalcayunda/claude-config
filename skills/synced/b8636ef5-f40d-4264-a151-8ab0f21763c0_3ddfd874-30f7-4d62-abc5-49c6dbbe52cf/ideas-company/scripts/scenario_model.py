#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#_VERSION = '1.1.0'
"""
IDEAS Financial Scenario Modeling

Compare multiple project scenarios side-by-side with different
scope, level, complexity, and team configurations.

Usage:
    python3 scenario_model.py --scenarios scenarios.json
    python3 scenario_model.py --quick S1.1,S2.3 --levels 6,8,10
    python3 scenario_model.py --quick S1.1,S1.2,S2.3 --levels 8,10,12 --json
"""

import argparse
import json
import sys
import io
import logging
from typing import List, Dict, Any, Union

# Third-party libraries
from tabulate import tabulate

# Internal modules
from estimate_service_cost import SERVICES, estimate_service_cost

# --- CONFIGURATION ---
# FUTURE IMPROVEMENT: This configuration could be externalized to a YAML or JSON file.
DEFAULT_AVG_TEAM_SIZE = 4
DEFAULT_WORKING_DAYS_PER_MONTH = 22
LEVEL_LABELS = {
    6: "Budget",
    7: "Economy",
    8: "Standard",
    9: "Professional",
    10: "Premium",
    11: "Enterprise",
    12: "Enterprise+",
    13: "Executive",
    14: "Executive+",
    15: "C-Suite",
}

# --- LOGGING SETUP ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)
logger = logging.getLogger(__name__)


def fmt(val: Union[int, float]) -> str:
    """Format a number as Indonesian Rupiah."""
    return "Rp {:,.0f}".format(val)


def run_scenario(scenario: Dict[str, Any]) -> Dict[str, Any]:
    """Run a single scenario and return results.

    Args:
        scenario: A dictionary defining the scenario parameters.

    Returns:
        A dictionary containing the calculated results for the scenario.
    """
    name = scenario.get("name", "Unnamed")
    services = scenario.get("services", [])
    level = scenario.get("level", 8)
    level_map = scenario.get("level_map", None)
    complexity = scenario.get("complexity", 1.0)
    pricing_mode = scenario.get("pricing_mode", "external")

    total_cost = 0
    total_man_days = 0
    service_results = []

    for sid in services:
        if sid not in SERVICES:
            logger.warning(f"Service ID '{sid}' not found. Skipping.")
            continue
        try:
            result = estimate_service_cost(sid, level, level_map, complexity, pricing_mode)
            if "error" in result:
                logger.warning(f"Could not estimate cost for service '{sid}'. Error: {result['error']}")
                continue
            total_cost += result["total_cost"]
            total_man_days += result["total_man_days"]
            service_results.append({
                "service_id": sid,
                "service_name": result["service_name"],
                "man_days": result["total_man_days"],
                "cost": result["total_cost"],
            })
        except Exception as e:
            logger.error(f"An unexpected error occurred while estimating cost for service '{sid}': {e}", exc_info=True)
            continue

    # Estimate duration
    # FUTURE IMPROVEMENT: Duration estimation could be more sophisticated, factoring in dependencies and parallel workstreams.
    avg_team_size = max(3, len(services)) # A simple heuristic for team size
    est_months = total_man_days / (avg_team_size * DEFAULT_WORKING_DAYS_PER_MONTH) if total_man_days > 0 else 0

    return {
        "name": name,
        "services": services,
        "level": level,
        "complexity": complexity,
        "total_cost": total_cost,
        "total_man_days": total_man_days,
        "est_months": round(est_months, 1),
        "service_count": len(service_results),
        "service_details": service_results,
        "cost_per_manday": total_cost / total_man_days if total_man_days > 0 else 0,
    }


def compare_scenarios(scenarios: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Run all scenarios and generate comparison.

    Args:
        scenarios: A list of scenario dictionaries.

    Returns:
        A list of result dictionaries for each scenario.
    """
    results = []
    for s in scenarios:
        results.append(run_scenario(s))
    return results


def print_comparison(results: List[Dict[str, Any]]):
    """Print side-by-side comparison table using the 'tabulate' library.

    Args:
        results: A list of result dictionaries from compare_scenarios.
    """
    if not results:
        print("No scenarios to compare.")
        return

    headers = ["Metric"] + [r['name'] for r in results]
    table = []

    # Summary Data
    table.append(["Jumlah Layanan"] + [r['service_count'] for r in results])
    table.append(["Level"] + [r['level'] for r in results])
    table.append(["Kompleksitas"] + [f"{r['complexity']:.1f}" for r in results])
    table.append(["Total Man-Days"] + [f"{r['total_man_days']:.0f}" for r in results])
    table.append(["Est. Durasi (bulan)"] + [f"{r['est_months']:.1f}" for r in results])
    table.append(["Biaya per Man-Day"] + [fmt(r['cost_per_manday']) for r in results])
    table.append(["TOTAL BIAYA"] + [fmt(r['total_cost']) for r in results])

    # Relative Comparison
    if len(results) > 1:
        base_cost = results[0]["total_cost"]
        base_name = results[0]['name']
        relative_costs = ["N/A"]
        for r in results[1:]:
            if base_cost > 0:
                pct = ((r["total_cost"] - base_cost) / base_cost) * 100
                relative_costs.append(f"{pct:+.1f}%")
            else:
                relative_costs.append("N/A")
        table.append([f"Relatif vs {base_name}"] + relative_costs)

    print("\nSCENARIO COMPARISON SUMMARY")
    print(tabulate(table, headers=headers, tablefmt="grid", stralign="right"))

    # Service Breakdown
    print("\nRINCIAN PER LAYANAN")
    all_sids = sorted(list(set(sid for r in results for sid in r["services"])))

    for sid in all_sids:
        svc_name = SERVICES.get(sid, {}).get("name", sid)
        print(f"\n--- {sid}: {svc_name} ---")
        service_table = []
        service_headers = ["Scenario", "Man-Days", "Cost"]
        for r in results:
            detail = next((d for d in r["service_details"] if d["service_id"] == sid), None)
            if detail:
                service_table.append([r['name'], f"{detail['man_days']:.0f} MD", fmt(detail['cost'])])
            else:
                service_table.append([r['name'], "(not included)", ""])
        print(tabulate(service_table, headers=service_headers, tablefmt="grid", stralign="right"))


def generate_quick_scenarios(service_str: str, levels_str: str, complexity_list: str = None) -> List[Dict[str, Any]]:
    """Generate scenarios from quick parameters.

    Args:
        service_str: Comma-separated string of service IDs.
        levels_str: Comma-separated string of levels.
        complexity_list: Optional comma-separated string of complexity values.

    Returns:
        A list of generated scenario dictionaries.
    """
    try:
        services = [s.strip() for s in service_str.split(",")]
        levels = [int(l.strip()) for l in levels_str.split(",")]
        complexities = [float(c.strip()) for c in complexity_list.split(",")] if complexity_list else [1.0] * len(levels)
    except ValueError as e:
        logger.error(f"Invalid input for quick scenarios. Please check your numbers: {e}")
        return []

    scenarios = []
    for i, level in enumerate(levels):
        c = complexities[i] if i < len(complexities) else 1.0
        label = LEVEL_LABELS.get(level, f"Level {level}")
        scenarios.append({
            "name": label,
            "services": services,
            "level": level,
            "complexity": c,
        })
    return scenarios


def main():
    """Main function to parse arguments and run the scenario modeling."""
    parser = argparse.ArgumentParser(description="IDEAS Financial Scenario Modeling")
    parser.add_argument("--scenarios", type=str, help="Path to JSON file with scenario definitions")
    parser.add_argument("--quick", type=str, help="Quick mode: comma-separated service IDs")
    parser.add_argument("--levels", type=str, default="6,8,10", help="Quick mode: comma-separated levels to compare")
    parser.add_argument("--complexities", type=str, help="Quick mode: comma-separated complexity values")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--output", type=str, help="Output file path for the report (JSON or Markdown)")

    args = parser.parse_args()

    scenarios = []
    if args.scenarios:
        try:
            with open(args.scenarios, "r") as f:
                scenarios = json.load(f)
        except FileNotFoundError:
            logger.error(f"Scenario file not found at '{args.scenarios}'")
            sys.exit(1)
        except json.JSONDecodeError:
            logger.error(f"Could not decode JSON from '{args.scenarios}'")
            sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred while reading the scenario file: {e}", exc_info=True)
            sys.exit(1)

    elif args.quick:
        scenarios = generate_quick_scenarios(args.quick, args.levels, args.complexities)
    else:
        parser.print_help()
        sys.exit(1)

    if not scenarios:
        logger.warning("No valid scenarios were defined. Exiting.")
        sys.exit(1)

    results = compare_scenarios(scenarios)

    # --- OUTPUT HANDLING ---
    # FUTURE IMPROVEMENT: Refactor the output saving logic to avoid code duplication.
    if args.output:
        try:
            if args.json:
                output_content = json.dumps(results, indent=2, ensure_ascii=False, default=str)
                with open(args.output, "w", encoding='utf-8') as f:
                    f.write(output_content)
            else:
                # Capture printed output to save to a file
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()
                print_comparison(results)
                sys.stdout = old_stdout
                report_content = buffer.getvalue()
                with open(args.output, "w", encoding='utf-8') as f:
                    f.write(f"```\n{report_content}\n```\n")
            logger.info(f"Results saved to: {args.output}")
        except IOError as e:
            logger.error(f"Error writing to file {args.output}: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred during output generation: {e}", exc_info=True)
            sys.exit(1)

    # --- CONSOLE OUTPUT ---
    if args.json and not args.output:
        print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
    elif not args.json:
        print_comparison(results)

if __name__ == "__main__":
    main()
