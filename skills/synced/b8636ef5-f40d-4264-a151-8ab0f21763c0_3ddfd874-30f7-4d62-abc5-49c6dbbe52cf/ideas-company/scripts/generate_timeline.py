#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: 1.1
# Last-Modified: 2026-02-20
"""IDEAS Project Timeline & Gantt Generator.

Generates a Mermaid Gantt diagram or JSON output from service task decomposition data,
calculating durations based on man-days, team size, and working days.

This script provides a command-line interface to generate project timelines based on
predefined service modules, estimating task durations and dependencies to produce a
visual Gantt chart in Mermaid format or a structured JSON output.

Usage:
    python3 generate_timeline.py --services S1.1,S2.3 --start 2026-04-01
    python3 generate_timeline.py --services S1.1,S1.2,S2.3 --start 2026-04-01 --team-size 5 --output timeline.mmd
    python3 generate_timeline.py --services S1.1,S2.3 --start 2026-04-01 --buffer 20 --json-output timeline.json
"""

import argparse
import json
import sys
import logging
from datetime import date, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional, Union

# =============================================================================
# CONFIGURATION CONSTANTS
# =============================================================================

# Default number of working days in a week. Affects calendar day calculations.
DEFAULT_WORKING_DAYS_PER_WEEK: int = 5

# Default average number of team members assigned to the project.
DEFAULT_TEAM_SIZE: int = 3

# Default buffer percentage to add to each task's duration for contingency.
DEFAULT_BUFFER_PCT: int = 10  # 10% buffer

# Default parallelism factor, representing efficiency gain from multiple team members.
DEFAULT_PARALLELISM_FACTOR: float = 0.7

# Path to the service data file. Resolves relative to skill directory.
_SKILL_DIR = Path(__file__).resolve().parent.parent
SERVICES_DATA_PATH: str = str(_SKILL_DIR / "data" / "services.json")

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)


def load_services(path: str) -> Dict[str, Any]:
    """Loads service definitions from a JSON file.

    Args:
        path (str): The file path to the services JSON data.

    Returns:
        Dict[str, Any]: A dictionary of service definitions.

    Raises:
        FileNotFoundError: If the services file cannot be found.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Fatal: Service data file not found at '{path}'.")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Fatal: Could not decode JSON from '{path}': {e}")
        raise


def add_working_days(start_date: date, working_days: int, days_per_week: int = DEFAULT_WORKING_DAYS_PER_WEEK) -> date:
    """Calculates the end date by adding working days, skipping weekends.

    Args:
        start_date (date): The starting date.
        working_days (int): The number of working days to add.
        days_per_week (int): The number of working days in a week.

    Returns:
        date: The calculated end date.
    """
    if working_days <= 0:
        return start_date
    current = start_date
    added = 0
    while added < working_days:
        current += timedelta(days=1)
        if days_per_week == 5 and current.weekday() < 5:  # Monday is 0, Friday is 4
            added += 1
        elif days_per_week > 5:
            added += 1
    return current


def calculate_task_duration(man_days: float, team_size: int, parallelism: float = DEFAULT_PARALLELISM_FACTOR) -> int:
    """Calculates calendar working days from man-days, team size, and parallelism.

    Args:
        man_days (float): Total effort in man-days.
        team_size (int): Number of people on the task.
        parallelism (float): Factor (0-1) for task parallelization.

    Returns:
        int: Estimated duration in calendar working days.
    """
    if team_size <= 0 or man_days <= 0:
        return 0
    effective_team = 1 + (team_size - 1) * parallelism
    duration = man_days / effective_team
    return max(1, round(duration))


def generate_timeline(service_ids: List[str], start_date_str: str, team_size: int, buffer_pct: int,
                      days_per_week: int, output_path: Optional[str], as_json: bool, json_output_path: Optional[str]) -> Dict[str, Any]:
    """Main function to generate the project timeline.

    Orchestrates parsing services, calculating durations, and assembling the output.
    """
    try:
        start_date = date.fromisoformat(start_date_str)
    except (ValueError, TypeError):
        logging.error(f"Invalid start date format: '{start_date_str}'. Please use YYYY-MM-DD.")
        return {"error": f"Invalid start date format: '{start_date_str}'."}

    try:
        SERVICES = load_services(SERVICES_DATA_PATH)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "Failed to load essential service data."}

    phases = []
    current_date = start_date
    pillar_services: Dict[str, List] = {}

    for sid in service_ids:
        if sid not in SERVICES:
            logging.warning(f"Service ID '{sid}' not found, skipping.")
            continue
        svc = SERVICES[sid]
        pillar = svc.get("pillar", "Uncategorized")
        if pillar not in pillar_services:
            pillar_services[pillar] = []
        pillar_services[pillar].append((sid, svc))

    if not pillar_services:
        logging.error("No valid services found for the given IDs.")
        return {"error": "No valid services found."}

    all_tasks = []
    task_id_counter = 0

    for pillar in sorted(pillar_services.keys()):
        for sid, svc in pillar_services[pillar]:
            service_tasks = []
            for task in svc.get("tasks", []):
                task_id_counter += 1
                raw_days = task.get("man_days", 0)
                cal_days = calculate_task_duration(raw_days, team_size)
                buffer_days = max(1, round(cal_days * buffer_pct / 100))
                total_days = cal_days + buffer_days
                end_date = add_working_days(current_date, total_days, days_per_week)

                task_entry = {
                    "id": f"t{task_id_counter}", "service_id": sid, "service_name": svc.get("name", "Unknown"),
                    "task_id": task.get("id", "N/A"), "description": task.get("desc", "No description"),
                    "man_days": raw_days, "calendar_days": cal_days, "buffer_days": buffer_days,
                    "total_days": total_days, "start_date": current_date.isoformat(), "end_date": end_date.isoformat(),
                }
                service_tasks.append(task_entry)
                all_tasks.append(task_entry)
                current_date = end_date  # Tasks are sequential

            if service_tasks:
                phases.append({
                    "service_id": sid, "service_name": svc.get("name", "Unknown"), "pillar": pillar,
                    "tasks": service_tasks, "start_date": service_tasks[0]["start_date"],
                    "end_date": service_tasks[-1]["end_date"], "total_man_days": sum(t["man_days"] for t in service_tasks),
                    "total_calendar_days": sum(t["total_days"] for t in service_tasks),
                })

    if not all_tasks:
        logging.warning("No tasks could be generated from the selected services.")
        return {"error": "No tasks generated."}

    project_end = current_date
    total_calendar_days = (project_end - start_date).days

    summary = {
        "project_start": start_date.isoformat(), "project_end": project_end.isoformat(),
        "total_calendar_days": total_calendar_days, "total_months": round(total_calendar_days / 30.44, 1),
        "team_size": team_size, "buffer_pct": buffer_pct, "phases": phases, "tasks": all_tasks,
    }

    if as_json or json_output_path:
        json_output = json.dumps(summary, indent=2, ensure_ascii=False)
        if json_output_path:
            try:
                with open(json_output_path, 'w', encoding='utf-8') as f:
                    f.write(json_output)
                logging.info(f"JSON timeline data saved to {json_output_path}")
            except IOError as e:
                logging.error(f"Failed to write JSON to {json_output_path}: {e}")
                return {"error": f"Failed to write to {json_output_path}"}
        else:
            print(json_output)
        return summary

    mermaid = generate_mermaid(summary, service_ids)

    if output_path:
        try:
            with open(output_path, "w", encoding='utf-8') as f:
                f.write(mermaid)
            logging.info(f"Success: Timeline generated at {output_path}")
            print(f"  Project runs from {start_date.isoformat()} to {project_end.isoformat()} ({total_calendar_days} days)." )
            print(f"  To render, use Mermaid Chart tool or paste content into a Mermaid renderer.")
        except IOError as e:
            logging.error(f"Failed to write to output file {output_path}: {e}")
            return {"error": f"Failed to write to output file {output_path}: {e}"}
    else:
        print(mermaid)

    return summary


def generate_mermaid(summary: Dict[str, Any], service_ids: List[str]) -> str:
    """Generates the Gantt chart in Mermaid syntax from the summary data."""
    lines = [
        "gantt",
        f"    title IDEAS Project Timeline ({', '.join(service_ids)})",
        "    dateFormat YYYY-MM-DD",
        "    axisFormat %b %d",
        ""
    ]
    for phase in summary.get("phases", []):
        lines.append(f"    section {phase.get('service_id', '')} {phase.get('service_name', 'Unknown')[:40]}")
        prev_id = None
        for task in phase.get("tasks", []):
            desc = task.get("description", "")[:45].replace(":", "")
            if prev_id:
                lines.append(f"    {desc} :{task.get('id')}, after {prev_id}, {task.get('total_days')}d")
            else:
                lines.append(f"    {desc} :{task.get('id')}, {task.get('start_date')}, {task.get('total_days')}d")
            prev_id = task.get("id")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    """Parses command-line arguments and triggers the timeline generation."""
    parser = argparse.ArgumentParser(
        description="IDEAS Project Timeline & Gantt Generator",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--services", required=True, help="Comma-separated list of service IDs (e.g., S1.1,S2.3).")
    parser.add_argument("--start", type=str, default=date.today().isoformat(), help="Project start date (YYYY-MM-DD). Defaults to today.")
    parser.add_argument("--team-size", type=int, default=DEFAULT_TEAM_SIZE, help=f"Average team size (default: {DEFAULT_TEAM_SIZE}).")
    parser.add_argument("--buffer", type=int, default=DEFAULT_BUFFER_PCT, help=f"Contingency buffer percentage (default: {DEFAULT_BUFFER_PCT}%%).")
    parser.add_argument("--days-per-week", type=int, default=DEFAULT_WORKING_DAYS_PER_WEEK, help=f"Working days per week (default: {DEFAULT_WORKING_DAYS_PER_WEEK}).")
    parser.add_argument("--output", type=str, help="Optional path to save the output Mermaid (.mmd) file.")
    parser.add_argument("--json", action="store_true", help="Output timeline data in JSON format to stdout.")
    parser.add_argument("--json-output", type=str, help="Optional path to save the output JSON data file.")

    args = parser.parse_args()
    service_ids = [s.strip() for s in args.services.split(",") if s.strip()]

    if not service_ids:
        logging.error("No service IDs provided. Please use the --services flag.")
        sys.exit(1)

    result = generate_timeline(
        service_ids, args.start, args.team_size, args.buffer,
        args.days_per_week, args.output, args.json, args.json_output
    )

    if isinstance(result, dict) and "error" in result:
        logging.error(f"An error occurred: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
