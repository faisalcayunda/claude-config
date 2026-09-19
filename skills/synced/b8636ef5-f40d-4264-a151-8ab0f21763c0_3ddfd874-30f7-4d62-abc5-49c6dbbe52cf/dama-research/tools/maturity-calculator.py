#!/usr/bin/env python3
"""
DAMA Data Management Maturity Calculator v2.0

A comprehensive tool for assessing organizational data management maturity
across all 14 DAMA-DMBOK2 Knowledge Areas.

Features:
- Interactive CLI assessment mode
- CSV/XLSX input support for batch assessment
- Weighted scoring across all 14 Knowledge Areas
- Gap analysis with prioritized recommendations
- Console-based heat map and bar chart visualization
- Markdown report generation

Usage:
    python maturity-calculator.py interactive          # Interactive assessment
    python maturity-calculator.py assess <file>        # Assess from CSV/XLSX file
    python maturity-calculator.py report <file> [out]  # Generate Markdown report
    python maturity-calculator.py help                 # Show detailed help

Related Templates:
    - templates/templates-KA-14-data-management-maturity.md
    - templates/templates-KA-14-data-management-maturity.md
    - templates/templates-KA-14-data-management-maturity.md
    - # (Maturity Scorecard section)
    - # (Assessment Questionnaire section)

Related Guides:
    - references/guides.md

Author: DAMA Research Skill
Version: 2.0
"""

import sys
import os
import csv
import json
from datetime import datetime

# ============================================================
# KNOWLEDGE AREA DEFINITIONS
# ============================================================

KNOWLEDGE_AREAS = {
    "KA-01": {
        "name": "Data Governance",
        "weight": 0.12,
        "capabilities": [
            "Policy Management",
            "Stewardship Program",
            "Data Standards",
            "Issue Resolution",
            "Change Management",
        ],
    },
    "KA-02": {
        "name": "Data Architecture",
        "weight": 0.08,
        "capabilities": [
            "Enterprise Data Model",
            "Architecture Standards",
            "Technology Alignment",
            "Data Flow Management",
            "Architecture Governance",
        ],
    },
    "KA-03": {
        "name": "Data Modeling & Design",
        "weight": 0.07,
        "capabilities": [
            "Modeling Standards",
            "Conceptual Modeling",
            "Logical/Physical Modeling",
            "Model Governance",
            "Naming Conventions",
        ],
    },
    "KA-04": {
        "name": "Data Storage & Operations",
        "weight": 0.06,
        "capabilities": [
            "Database Management",
            "Performance Optimization",
            "Backup & Recovery",
            "Capacity Planning",
            "Operational Monitoring",
        ],
    },
    "KA-05": {
        "name": "Data Security",
        "weight": 0.09,
        "capabilities": [
            "Access Control",
            "Data Classification",
            "Encryption & Masking",
            "Audit & Compliance",
            "Incident Response",
        ],
    },
    "KA-06": {
        "name": "Data Integration & Interoperability",
        "weight": 0.07,
        "capabilities": [
            "ETL/ELT Processes",
            "API Management",
            "Data Lineage",
            "Real-time Integration",
            "Standards Compliance",
        ],
    },
    "KA-07": {
        "name": "Document & Content Management",
        "weight": 0.05,
        "capabilities": [
            "Content Lifecycle",
            "Taxonomy & Classification",
            "Retention Management",
            "Search & Discovery",
            "Version Control",
        ],
    },
    "KA-08": {
        "name": "Data Warehousing & BI",
        "weight": 0.07,
        "capabilities": [
            "DW Architecture",
            "ETL Pipeline Quality",
            "BI & Reporting",
            "Self-Service Analytics",
            "Performance Management",
        ],
    },
    "KA-09": {
        "name": "Metadata Management",
        "weight": 0.08,
        "capabilities": [
            "Metadata Repository",
            "Business Glossary",
            "Data Catalog",
            "Lineage Tracking",
            "Metadata Standards",
        ],
    },
    "KA-10": {
        "name": "Reference & Master Data",
        "weight": 0.07,
        "capabilities": [
            "MDM Strategy",
            "Golden Record Management",
            "Reference Data Standards",
            "Match & Merge Rules",
            "Data Stewardship",
        ],
    },
    "KA-11": {
        "name": "Data Quality",
        "weight": 0.10,
        "capabilities": [
            "DQ Strategy & Framework",
            "DQ Rules & Profiling",
            "DQ Monitoring & Reporting",
            "Issue Management",
            "Continuous Improvement",
        ],
    },
    "KA-12": {
        "name": "Data Handling Ethics",
        "weight": 0.05,
        "capabilities": [
            "Ethical Principles",
            "Privacy & Consent",
            "Bias Detection",
            "Transparency",
            "Ethics Governance",
        ],
    },
    "KA-13": {
        "name": "Big Data & Data Science",
        "weight": 0.05,
        "capabilities": [
            "Analytics Strategy",
            "Model Development",
            "MLOps & Deployment",
            "Data Visualization",
            "Model Governance",
        ],
    },
    "KA-14": {
        "name": "Data Management Maturity",
        "weight": 0.04,
        "capabilities": [
            "Assessment Process",
            "Benchmarking",
            "Improvement Planning",
            "Capability Tracking",
            "Stakeholder Engagement",
        ],
    },
}

MATURITY_LEVELS = {
    1: "Initial / Ad Hoc",
    2: "Repeatable / Managed",
    3: "Defined / Standardized",
    4: "Measured / Quantitatively Managed",
    5: "Optimizing / Continuously Improving",
}

MATURITY_CRITERIA = {
    1: "No formal processes. Activities are ad hoc and reactive. No documentation or standards.",
    2: "Basic processes exist but are inconsistent. Some documentation. Dependent on individuals.",
    3: "Processes are standardized and documented. Organization-wide adoption. Roles defined.",
    4: "Processes are measured with KPIs. Data-driven decision making. Automated monitoring.",
    5: "Continuous optimization. Industry-leading practices. Innovation-driven. Fully automated.",
}

# ============================================================
# CORE FUNCTIONS
# ============================================================

def calculate_scores(responses):
    """Calculate maturity scores from assessment responses.
    
    Args:
        responses: dict of {ka_id: {capability: score}} or {ka_id: [scores]}
    
    Returns:
        dict with ka_scores, weighted_scores, overall_score, etc.
    """
    ka_scores = {}
    weighted_total = 0.0
    weight_sum = 0.0
    
    for ka_id, ka_info in KNOWLEDGE_AREAS.items():
        if ka_id in responses:
            resp = responses[ka_id]
            if isinstance(resp, dict):
                scores = list(resp.values())
            elif isinstance(resp, list):
                scores = resp
            else:
                continue
            
            valid_scores = [s for s in scores if isinstance(s, (int, float)) and 1 <= s <= 5]
            if valid_scores:
                avg = sum(valid_scores) / len(valid_scores)
                ka_scores[ka_id] = {
                    "name": ka_info["name"],
                    "score": round(avg, 2),
                    "weight": ka_info["weight"],
                    "weighted_score": round(avg * ka_info["weight"], 4),
                    "capability_scores": dict(zip(ka_info["capabilities"], scores)),
                    "min_capability": min(valid_scores),
                    "max_capability": max(valid_scores),
                }
                weighted_total += avg * ka_info["weight"]
                weight_sum += ka_info["weight"]
    
    overall = round(weighted_total / weight_sum, 2) if weight_sum > 0 else 0
    
    return {
        "ka_scores": ka_scores,
        "overall_score": overall,
        "overall_level": get_maturity_level(overall),
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "kas_assessed": len(ka_scores),
        "total_kas": len(KNOWLEDGE_AREAS),
    }

def get_maturity_level(score):
    """Get the maturity level name for a given score."""
    level = max(1, min(5, round(score)))
    return MATURITY_LEVELS.get(level, "Unknown")

def generate_recommendations(ka_scores, target=4.0):
    """Generate prioritized recommendations based on scores and target."""
    recs = []
    for ka_id, data in ka_scores.items():
        gap = target - data["score"]
        if gap > 0:
            priority = "CRITICAL" if gap >= 2.0 else "HIGH" if gap >= 1.0 else "MEDIUM"
            
            # Find weakest capabilities
            weak_caps = sorted(data["capability_scores"].items(), key=lambda x: x[1])
            weakest = [f"{cap} ({score:.1f})" for cap, score in weak_caps[:2]]
            
            recs.append({
                "ka_id": ka_id,
                "name": data["name"],
                "current": data["score"],
                "target": target,
                "gap": round(gap, 2),
                "priority": priority,
                "weakest_capabilities": weakest,
                "recommendation": get_recommendation(ka_id, data["score"]),
            })
    
    recs.sort(key=lambda x: x["gap"], reverse=True)
    return recs

def get_recommendation(ka_id, score):
    """Get specific recommendation based on KA and score."""
    base_recs = {
        "KA-01": {
            "low": "Establish a Data Governance Council and define foundational policies and standards.",
            "mid": "Formalize stewardship roles, implement policy automation, and establish metrics.",
            "high": "Optimize governance through AI-assisted policy enforcement and continuous feedback loops.",
        },
        "KA-02": {
            "low": "Create an Enterprise Data Model and document current-state architecture.",
            "mid": "Implement architecture review boards and align with cloud-native patterns.",
            "high": "Adopt Data Mesh/Fabric principles and automate architecture compliance.",
        },
        "KA-03": {
            "low": "Define modeling standards and naming conventions. Train staff on data modeling.",
            "mid": "Implement model governance, version control, and automated model validation.",
            "high": "Integrate modeling with CI/CD pipelines and adopt model-driven development.",
        },
        "KA-04": {
            "low": "Document database standards and implement basic monitoring and backup procedures.",
            "mid": "Automate capacity planning, implement DR testing, and optimize performance.",
            "high": "Adopt infrastructure-as-code, auto-scaling, and predictive maintenance.",
        },
        "KA-05": {
            "low": "Implement basic access controls, data classification, and security policies.",
            "mid": "Deploy encryption, audit trails, and automated compliance monitoring.",
            "high": "Implement zero-trust architecture, AI-driven threat detection, and privacy-by-design.",
        },
        "KA-06": {
            "low": "Document integration patterns and implement basic ETL processes.",
            "mid": "Standardize APIs, implement data lineage tracking, and adopt CDC patterns.",
            "high": "Implement real-time streaming, event-driven architecture, and self-healing pipelines.",
        },
        "KA-07": {
            "low": "Define content taxonomy and implement basic retention schedules.",
            "mid": "Deploy enterprise content management, automate classification, and enforce retention.",
            "high": "Implement AI-powered content discovery, auto-classification, and lifecycle automation.",
        },
        "KA-08": {
            "low": "Define DW/BI strategy and implement basic reporting infrastructure.",
            "mid": "Implement self-service BI, data marts, and automated ETL quality checks.",
            "high": "Adopt modern data stack, real-time analytics, and augmented BI capabilities.",
        },
        "KA-09": {
            "low": "Implement a metadata repository and define metadata standards.",
            "mid": "Deploy a data catalog, automate metadata harvesting, and track lineage.",
            "high": "Implement active metadata management, ML-powered discovery, and knowledge graphs.",
        },
        "KA-10": {
            "low": "Define MDM strategy and identify critical master data entities.",
            "mid": "Implement golden record management, match-merge rules, and reference data governance.",
            "high": "Deploy real-time MDM, graph-based entity resolution, and federated MDM.",
        },
        "KA-11": {
            "low": "Define DQ dimensions and implement basic profiling and monitoring.",
            "mid": "Implement DQ rules engine, automated monitoring, and issue management workflows.",
            "high": "Deploy ML-based anomaly detection, predictive DQ, and self-healing data pipelines.",
        },
        "KA-12": {
            "low": "Define ethical principles and establish an ethics review process.",
            "mid": "Implement bias detection, consent management, and transparency reporting.",
            "high": "Deploy algorithmic auditing, automated fairness monitoring, and ethics-by-design.",
        },
        "KA-13": {
            "low": "Define analytics strategy and establish basic data science capabilities.",
            "mid": "Implement MLOps, model governance, and standardized experimentation frameworks.",
            "high": "Deploy AutoML, feature stores, real-time inference, and responsible AI frameworks.",
        },
        "KA-14": {
            "low": "Conduct initial maturity assessment and establish baseline metrics.",
            "mid": "Implement regular assessments, benchmarking, and improvement tracking.",
            "high": "Deploy continuous maturity monitoring, predictive gap analysis, and adaptive roadmaps.",
        },
    }
    
    ka_recs = base_recs.get(ka_id, {"low": "Improve foundational capabilities.", "mid": "Standardize and optimize.", "high": "Innovate and lead."})
    
    if score < 2.0:
        return ka_recs["low"]
    elif score < 3.5:
        return ka_recs["mid"]
    else:
        return ka_recs["high"]

# ============================================================
# VISUALIZATION
# ============================================================

def render_bar_chart(ka_scores, width=50):
    """Render a console bar chart of maturity scores."""
    print("\n" + "=" * 70)
    print("  MATURITY SCORE BAR CHART")
    print("=" * 70)
    
    for ka_id in sorted(ka_scores.keys()):
        data = ka_scores[ka_id]
        score = data["score"]
        bar_len = int(score / 5.0 * width)
        
        # Color coding via symbols
        if score >= 4.0:
            bar_char = "█"
        elif score >= 3.0:
            bar_char = "▓"
        elif score >= 2.0:
            bar_char = "▒"
        else:
            bar_char = "░"
        
        bar = bar_char * bar_len + "·" * (width - bar_len)
        label = f"{ka_id} {data['name'][:28]:<28}"
        print(f"  {label} |{bar}| {score:.1f}")
    
    print()
    print("  Legend: █ >= 4.0 (Optimizing)  ▓ >= 3.0 (Defined)  ▒ >= 2.0 (Managed)  ░ < 2.0 (Ad Hoc)")

def render_heat_map(ka_scores):
    """Render a console heat map of capability scores."""
    print("\n" + "=" * 70)
    print("  CAPABILITY HEAT MAP")
    print("=" * 70)
    
    # Header
    print(f"  {'KA':<8} {'Cap-1':>6} {'Cap-2':>6} {'Cap-3':>6} {'Cap-4':>6} {'Cap-5':>6} {'Avg':>6}")
    print("  " + "-" * 50)
    
    heat_symbols = {1: "░ 1.0", 2: "▒ 2.0", 3: "▓ 3.0", 4: "█ 4.0", 5: "█ 5.0"}
    
    for ka_id in sorted(ka_scores.keys()):
        data = ka_scores[ka_id]
        caps = list(data["capability_scores"].values())
        row = f"  {ka_id:<8}"
        for c in caps[:5]:
            val = round(c, 1)
            row += f" {val:>5.1f}"
        row += f" {data['score']:>5.1f}"
        print(row)
    
    print()

def render_gap_analysis(recommendations, target=4.0):
    """Render gap analysis table."""
    print("\n" + "=" * 70)
    print(f"  GAP ANALYSIS (Target: {target:.1f})")
    print("=" * 70)
    
    if not recommendations:
        print("  All Knowledge Areas meet or exceed the target. Congratulations!")
        return
    
    print(f"  {'Priority':<10} {'KA':<8} {'Name':<30} {'Current':>8} {'Target':>8} {'Gap':>6}")
    print("  " + "-" * 72)
    
    for rec in recommendations:
        print(f"  {rec['priority']:<10} {rec['ka_id']:<8} {rec['name']:<30} {rec['current']:>7.1f} {rec['target']:>7.1f} {rec['gap']:>5.1f}")

# ============================================================
# I/O FUNCTIONS
# ============================================================

def interactive_assessment():
    """Run an interactive CLI assessment."""
    print("\n" + "=" * 70)
    print("  DAMA DATA MANAGEMENT MATURITY ASSESSMENT")
    print("  Interactive Mode")
    print("=" * 70)
    print("\n  For each capability, enter a score from 1 to 5:")
    for level, desc in MATURITY_LEVELS.items():
        print(f"    {level} = {desc}")
    print(f"    {MATURITY_CRITERIA[1]}")
    print()
    
    responses = {}
    
    for ka_id, ka_info in KNOWLEDGE_AREAS.items():
        print(f"\n  --- {ka_id}: {ka_info['name']} ---")
        scores = {}
        for cap in ka_info["capabilities"]:
            while True:
                try:
                    val = input(f"    {cap}: ")
                    score = float(val)
                    if 1 <= score <= 5:
                        scores[cap] = score
                        break
                    else:
                        print("      Please enter a value between 1 and 5.")
                except ValueError:
                    print("      Invalid input. Please enter a number between 1 and 5.")
                except (EOFError, KeyboardInterrupt):
                    print("\n  Assessment cancelled.")
                    return None
        responses[ka_id] = scores
    
    return responses

def load_from_csv(filepath):
    """Load assessment data from a CSV file.
    
    Expected CSV format:
    KA_ID,Capability,Score
    KA-01,Policy Management,3
    KA-01,Stewardship Program,2
    ...
    """
    responses = {}
    
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ka_id = row.get("KA_ID", row.get("ka_id", "")).strip()
            score_str = row.get("Score", row.get("score", "0")).strip()
            
            try:
                score = float(score_str)
            except ValueError:
                continue
            
            if ka_id not in responses:
                responses[ka_id] = []
            responses[ka_id].append(score)
    
    return responses

def load_from_xlsx(filepath):
    """Load assessment data from an XLSX file."""
    try:
        from openpyxl import load_workbook
    except ImportError:
        print("Error: openpyxl is required for XLSX support. Install with: pip install openpyxl")
        sys.exit(1)
    
    wb = load_workbook(filepath, read_only=True)
    responses = {}
    
    # Try to find the assessment sheet
    ws = wb.active
    
    # Read header row
    headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]
    
    # Find column indices
    ka_col = None
    score_col = None
    for i, h in enumerate(headers):
        if h and "ka" in str(h).lower():
            ka_col = i
        if h and "score" in str(h).lower():
            score_col = i
        if h and "level" in str(h).lower() and score_col is None:
            score_col = i
        if h and "selected" in str(h).lower() and score_col is None:
            score_col = i
    
    if ka_col is None or score_col is None:
        # Try positional: assume KA_ID in col 0/1, Score in col 2+
        ka_col = 0
        score_col = 2
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[ka_col] is None:
            continue
        ka_id = str(row[ka_col]).strip()
        try:
            score = float(row[score_col])
        except (ValueError, TypeError):
            continue
        
        if ka_id not in responses:
            responses[ka_id] = []
        responses[ka_id].append(score)
    
    wb.close()
    return responses

def generate_markdown_report(results, recommendations, output_path=None):
    """Generate a comprehensive Markdown report."""
    lines = []
    lines.append("# Data Management Maturity Assessment Report")
    lines.append("")
    lines.append(f"**Assessment Date:** {results['assessment_date']}")
    lines.append(f"**Knowledge Areas Assessed:** {results['kas_assessed']} / {results['total_kas']}")
    lines.append(f"**Overall Maturity Score:** {results['overall_score']:.2f} / 5.00")
    lines.append(f"**Overall Maturity Level:** {results['overall_level']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Scorecard Summary")
    lines.append("")
    lines.append("| KA | Knowledge Area | Score | Level | Weight | Weighted |")
    lines.append("|---|---|---|---|---|---|")
    
    for ka_id in sorted(results["ka_scores"].keys()):
        d = results["ka_scores"][ka_id]
        level = get_maturity_level(d["score"])
        lines.append(f"| {ka_id} | {d['name']} | {d['score']:.2f} | {level} | {d['weight']:.0%} | {d['weighted_score']:.4f} |")
    
    lines.append(f"| | **Overall** | **{results['overall_score']:.2f}** | **{results['overall_level']}** | | |")
    lines.append("")
    
    lines.append("## 2. Capability Detail")
    lines.append("")
    for ka_id in sorted(results["ka_scores"].keys()):
        d = results["ka_scores"][ka_id]
        lines.append(f"### {ka_id}: {d['name']} (Score: {d['score']:.2f})")
        lines.append("")
        lines.append("| Capability | Score |")
        lines.append("|---|---|")
        for cap, score in d["capability_scores"].items():
            lines.append(f"| {cap} | {score:.1f} |")
        lines.append("")
    
    lines.append("## 3. Gap Analysis & Recommendations")
    lines.append("")
    if recommendations:
        lines.append("| Priority | KA | Current | Target | Gap | Recommendation |")
        lines.append("|---|---|---|---|---|---|")
        for rec in recommendations:
            lines.append(f"| {rec['priority']} | {rec['ka_id']}: {rec['name']} | {rec['current']:.1f} | {rec['target']:.1f} | {rec['gap']:.1f} | {rec['recommendation']} |")
    else:
        lines.append("All Knowledge Areas meet or exceed the target score.")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by DAMA Maturity Calculator v2.0*")
    
    report = "\n".join(lines)
    
    if output_path:
        with open(output_path, "w") as f:
            f.write(report)
        print(f"\n  Report saved to: {output_path}")
    
    return report

# ============================================================
# MAIN CLI
# ============================================================

def print_help():
    """Print detailed help information."""
    print("""
DAMA Data Management Maturity Calculator v2.0
==============================================

USAGE:
    python maturity-calculator.py <command> [arguments]

COMMANDS:
    interactive              Run an interactive assessment via CLI prompts
    assess <file>            Load and assess from a CSV or XLSX file
    report <file> [output]   Generate a Markdown report from assessment data
    help                     Show this help message

FILE FORMAT (CSV):
    KA_ID,Capability,Score
    KA-01,Policy Management,3
    KA-01,Stewardship Program,2
    KA-01,Data Standards,3
    KA-01,Issue Resolution,2
    KA-01,Change Management,3
    KA-02,Enterprise Data Model,2
    ...

FILE FORMAT (XLSX):
    Use the assessment questionnaire template:
    #

MATURITY LEVELS:
    1 = Initial / Ad Hoc
    2 = Repeatable / Managed
    3 = Defined / Standardized
    4 = Measured / Quantitatively Managed
    5 = Optimizing / Continuously Improving

KNOWLEDGE AREAS (14):
""")
    for ka_id, info in KNOWLEDGE_AREAS.items():
        print(f"    {ka_id}: {info['name']} (weight: {info['weight']:.0%})")
        for cap in info["capabilities"]:
            print(f"      - {cap}")
    print()

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)
    
    command = sys.argv[1].lower()
    
    if command == "help":
        print_help()
    
    elif command == "interactive":
        responses = interactive_assessment()
        if responses:
            results = calculate_scores(responses)
            render_bar_chart(results["ka_scores"])
            render_heat_map(results["ka_scores"])
            recs = generate_recommendations(results["ka_scores"])
            render_gap_analysis(recs)
            
            # Ask to save report
            try:
                save = input("\n  Save report to file? (y/n): ").strip().lower()
                if save == "y":
                    path = input("  Output path [maturity-report.md]: ").strip()
                    if not path:
                        path = "maturity-report.md"
                    generate_markdown_report(results, recs, path)
            except (EOFError, KeyboardInterrupt):
                pass
    
    elif command == "assess":
        if len(sys.argv) < 3:
            print("Error: Please provide a file path.")
            print("Usage: python maturity-calculator.py assess <file.csv|file.xlsx>")
            sys.exit(1)
        
        filepath = sys.argv[2]
        if not os.path.exists(filepath):
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
        
        if filepath.endswith(".xlsx"):
            responses = load_from_xlsx(filepath)
        elif filepath.endswith(".csv"):
            responses = load_from_csv(filepath)
        else:
            print("Error: Unsupported file format. Use .csv or .xlsx")
            sys.exit(1)
        
        if not responses:
            print("\n  No valid assessment data found in file.")
            print("  Please ensure CSV has header: KA_ID,Capability,Score")
            print("  See 'help' for file format details.")
            return
        
        results = calculate_scores(responses)
        
        print(f"\n  Loaded {results['kas_assessed']} Knowledge Areas from {filepath}")
        print(f"  Overall Score: {results['overall_score']:.2f} ({results['overall_level']})")
        
        render_bar_chart(results["ka_scores"])
        render_heat_map(results["ka_scores"])
        recs = generate_recommendations(results["ka_scores"])
        render_gap_analysis(recs)
    
    elif command == "report":
        if len(sys.argv) < 3:
            print("Error: Please provide a file path.")
            print("Usage: python maturity-calculator.py report <file> [output.md]")
            sys.exit(1)
        
        filepath = sys.argv[2]
        output = sys.argv[3] if len(sys.argv) > 3 else "maturity-report.md"
        
        if not os.path.exists(filepath):
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
        
        if filepath.endswith(".xlsx"):
            responses = load_from_xlsx(filepath)
        elif filepath.endswith(".csv"):
            responses = load_from_csv(filepath)
        else:
            print("Error: Unsupported file format. Use .csv or .xlsx")
            sys.exit(1)
        
        results = calculate_scores(responses)
        recs = generate_recommendations(results["ka_scores"])
        generate_markdown_report(results, recs, output)
        
        print(f"\n  Assessment complete.")
        print(f"  Overall Score: {results['overall_score']:.2f} ({results['overall_level']})")
        print(f"  Report saved to: {output}")
    
    else:
        print(f"Unknown command: {command}")
        print("Use 'help' for usage information.")
        sys.exit(1)

if __name__ == "__main__":
    main()
