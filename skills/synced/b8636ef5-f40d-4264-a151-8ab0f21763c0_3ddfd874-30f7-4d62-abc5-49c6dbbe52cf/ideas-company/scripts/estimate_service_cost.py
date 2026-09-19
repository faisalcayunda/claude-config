#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#_VERSION: 1.1.0
"""
IDEAS Service Cost Estimator (Task-Based)

Calculates precise project costs by decomposing services into granular tasks
with role involvement percentages. This script reads the task-decomposition
data and uses the unified pricing_engine for rate calculations.

Usage:
    # Estimate cost for a single service
    python3 estimate_service_cost.py --service S2.3 --level 8

    # Estimate with complexity multiplier
    python3 estimate_service_cost.py --service S1.1 --level 10 --complexity 1.5

    # Estimate multiple services (full project)
    python3 estimate_service_cost.py --services S1.1,S1.2,S2.3 --level 8

    # Estimate with custom level per role category
    python3 estimate_service_cost.py --service S2.1 --level-map '{{"Management":15,"Managerial":12,"Lead":10,"Analyst":8,"Engineer":8,"Officer":6}}'

    # List all services and their total man-days
    python3 estimate_service_cost.py --list-services

    # Show task breakdown for a service
    python3 estimate_service_cost.py --service S1.1 --breakdown

    # Export as JSON
    python3 estimate_service_cost.py --service S2.3 --level 8 --json
"""

# Cross-Skill Integration:
#   web-scraper: Collect market pricing data from INAPROC e-Katalog
#     using domain_crawler.py for competitive cost benchmarking.
#   dama-research: Reference KA scope definitions to validate service
#     scope and effort estimates against DAMA-DMBOK standards.


import argparse
import json
import sys
import textwrap
import logging
from typing import List, Dict, Any, Tuple, Union

from pricing_engine import get_daily_rate, get_internal_daily_rate, get_cost_breakdown, RATE_CARD

# =============================================================================
# CONFIGURATION
# =============================================================================

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)
logger = logging.getLogger(__name__)

# Complexity multipliers adjust the man-days based on project difficulty.
COMPLEXITY_MULTIPLIERS: Dict[str, float] = {
    "simple": 0.7,
    "medium": 1.0,
    "complex": 1.5,
}

# =============================================================================
# TASK DECOMPOSITION DATABASE
# =============================================================================
# FUTURE IMPROVEMENT: This data could be externalized to a JSON or YAML file
# for easier maintenance and to allow non-developers to update service definitions.
# Each service contains tasks. Each task has:
#   - id: unique task ID
#   - desc: task description
#   - dama_ka: relevant DAMA Knowledge Area
#   - man_days: estimated total man-days for the task
#   - roles: list of (role_name, involvement_percentage) tuples
# =============================================================================

SERVICES: Dict[str, Dict[str, Any]] = {
    # --- Pillar 1: Advisory & Governance ---
    "S1.1": {
        "name": "Data Strategy & Roadmap Development",
        "pillar": 1,
        "dama_kas": ["KA-01", "KA-02", "KA-14"],
        "tasks": [
            {"id": "S1.1-01", "desc": "Conduct stakeholder interviews & requirements gathering", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Project Manager (Data)", 0.20), ("Business Analyst (Data)", 0.40), ("Subject Matter Expert (SME)", 0.20), ("Chief Data Officer (CDO)", 0.10), ("Data Governance Manager", 0.10)]},
            {"id": "S1.1-02", "desc": "Assess current data landscape & inventory", "dama_ka": "KA-14", "man_days": 15,
             "roles": [("Data Architect", 0.30), ("Data Governance Analyst", 0.25), ("Data Engineer", 0.20), ("Business Analyst (Data)", 0.15), ("Data Quality Analyst", 0.10)]},
            {"id": "S1.1-03", "desc": "Conduct data maturity assessment (DAMA-DMBOK based)", "dama_ka": "KA-14", "man_days": 12,
             "roles": [("Data Governance Manager", 0.25), ("Data Governance Analyst", 0.30), ("Business Analyst (Data)", 0.20), ("Subject Matter Expert (SME)", 0.15), ("Project Manager (Data)", 0.10)]},
            {"id": "S1.1-04", "desc": "Benchmark against industry standards & peers", "dama_ka": "KA-14", "man_days": 8,
             "roles": [("Data Governance Manager", 0.30), ("Data Analyst", 0.35), ("Data Governance Analyst", 0.20), ("Business Analyst (Data)", 0.15)]},
            {"id": "S1.1-05", "desc": "Define data vision, mission, and strategic objectives", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Chief Data Officer (CDO)", 0.30), ("Data Governance Manager", 0.25), ("Project Manager (Data)", 0.20), ("Business Analyst (Data)", 0.15), ("Data Architect", 0.10)]},
            {"id": "S1.1-06", "desc": "Design target-state data architecture blueprint", "dama_ka": "KA-02", "man_days": 15,
             "roles": [("Data Architect", 0.40), ("Data Engineering Manager", 0.20), ("Data Engineer", 0.20), ("Data Governance Manager", 0.10), ("Product Engineering Architect", 0.10)]},
            {"id": "S1.1-07", "desc": "Develop prioritized implementation roadmap", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Project Manager (Data)", 0.30), ("Chief Data Officer (CDO)", 0.20), ("Data Governance Manager", 0.20), ("Data Architect", 0.15), ("Business Analyst (Data)", 0.15)]},
            {"id": "S1.1-08", "desc": "Define KPIs, success metrics, and governance model", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Governance Manager", 0.30), ("Data Quality Analyst", 0.25), ("Chief Data Officer (CDO)", 0.15), ("Business Analyst (Data)", 0.15), ("Project Manager (Data)", 0.15)]},
            {"id": "S1.1-09", "desc": "Prepare executive presentation & final report", "dama_ka": "KA-01", "man_days": 5,
             "roles": [("Project Manager (Data)", 0.30), ("Business Analyst (Data)", 0.30), ("Chief Data Officer (CDO)", 0.20), ("Product Writer", 0.20)]},
        ]
    },
    "S1.2": {
        "name": "Data Governance & Compliance Framework",
        "pillar": 1,
        "dama_kas": ["KA-01", "KA-05", "KA-12"],
        "tasks": [
            {"id": "S1.2-01", "desc": "Assess current governance maturity & gap analysis", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Data Governance Manager", 0.30), ("Data Governance Analyst", 0.30), ("Business Analyst (Data)", 0.20), ("Compliance Officer (Data)", 0.10), ("Data Protection Officer (DPO)", 0.10)]},
            {"id": "S1.2-02", "desc": "Map regulatory requirements (UU PDP, SPBE, SDI)", "dama_ka": "KA-05", "man_days": 12,
             "roles": [("Compliance Officer (Data)", 0.30), ("Data Protection Officer (DPO)", 0.25), ("Data Governance Manager", 0.20), ("Data Security Manager", 0.15), ("Business Analyst (Data)", 0.10)]},
            {"id": "S1.2-03", "desc": "Design data governance organizational structure", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Chief Data Officer (CDO)", 0.25), ("Data Governance Manager", 0.30), ("Change Manager (Data)", 0.20), ("Project Manager (Data)", 0.15), ("Business Analyst (Data)", 0.10)]},
            {"id": "S1.2-04", "desc": "Define data ownership & stewardship model (RASCI)", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Data Governance Manager", 0.30), ("Data Owner", 0.20), ("Data Steward", 0.20), ("Business Analyst (Data)", 0.15), ("Subject Matter Expert (SME)", 0.15)]},
            {"id": "S1.2-05", "desc": "Develop data policies & standards documentation", "dama_ka": "KA-01", "man_days": 15,
             "roles": [("Data Governance Manager", 0.25), ("Data Governance Analyst", 0.25), ("Compliance Officer (Data)", 0.20), ("Data Protection Officer (DPO)", 0.15), ("Product Writer", 0.15)]},
            {"id": "S1.2-06", "desc": "Design data classification & sensitivity framework", "dama_ka": "KA-05", "man_days": 10,
             "roles": [("Data Security Manager", 0.30), ("Data Protection Officer (DPO)", 0.25), ("Data Governance Analyst", 0.20), ("Data Steward", 0.15), ("Compliance Officer (Data)", 0.10)]},
            {"id": "S1.2-07", "desc": "Develop data quality rules & SLA framework", "dama_ka": "KA-11", "man_days": 10,
             "roles": [("Data Quality Manager", 0.30), ("Data Quality Analyst", 0.30), ("Data Steward", 0.20), ("Data Owner", 0.10), ("Business Analyst (Data)", 0.10)]},
            {"id": "S1.2-08", "desc": "Create data governance charter & council structure", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Chief Data Officer (CDO)", 0.25), ("Data Governance Manager", 0.30), ("Change Manager (Data)", 0.20), ("Project Manager (Data)", 0.15), ("Product Writer", 0.10)]},
            {"id": "S1.2-09", "desc": "Design governance metrics & monitoring dashboard spec", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Governance Manager", 0.25), ("Data Quality Analyst", 0.25), ("Data Analyst", 0.20), ("BI Developer", 0.15), ("Product Designer", 0.15)]},
            {"id": "S1.2-10", "desc": "Conduct governance framework socialization & training", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Change Manager (Data)", 0.30), ("Data Literacy Champion", 0.25), ("Data Governance Manager", 0.20), ("Data Steward", 0.15), ("Product Writer", 0.10)]},
        ]
    },
    "S1.3": {
        "name": "Data Maturity Assessment & Benchmarking",
        "pillar": 1,
        "dama_kas": ["KA-14", "KA-01", "KA-11"],
        "tasks": [
            {"id": "S1.3-01", "desc": "Design assessment methodology & questionnaire", "dama_ka": "KA-14", "man_days": 8,
             "roles": [("Data Governance Manager", 0.30), ("Data Governance Analyst", 0.30), ("Business Analyst (Data)", 0.25), ("Project Manager (Data)", 0.15)]},
            {"id": "S1.3-02", "desc": "Conduct interviews & evidence collection across KAs", "dama_ka": "KA-14", "man_days": 15,
             "roles": [("Business Analyst (Data)", 0.30), ("Data Governance Analyst", 0.25), ("Subject Matter Expert (SME)", 0.20), ("Data Quality Analyst", 0.15), ("Data Architect", 0.10)]},
            {"id": "S1.3-03", "desc": "Score & analyze maturity across 14 DAMA KAs", "dama_ka": "KA-14", "man_days": 10,
             "roles": [("Data Governance Manager", 0.25), ("Data Governance Analyst", 0.30), ("Data Analyst", 0.25), ("Business Analyst (Data)", 0.20)]},
            {"id": "S1.3-04", "desc": "Benchmark against industry & regulatory standards", "dama_ka": "KA-14", "man_days": 8,
             "roles": [("Data Governance Manager", 0.30), ("Data Analyst", 0.30), ("Business Analyst (Data)", 0.20), ("Compliance Officer (Data)", 0.20)]},
            {"id": "S1.3-05", "desc": "Identify gaps & prioritize improvement areas", "dama_ka": "KA-14", "man_days": 8,
             "roles": [("Data Governance Manager", 0.25), ("Chief Data Officer (CDO)", 0.20), ("Data Architect", 0.20), ("Data Quality Manager", 0.20), ("Project Manager (Data)", 0.15)]},
            {"id": "S1.3-06", "desc": "Develop improvement roadmap with quick wins", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Project Manager (Data)", 0.25), ("Data Governance Manager", 0.25), ("Chief Data Officer (CDO)", 0.20), ("Business Analyst (Data)", 0.15), ("Data Architect", 0.15)]},
            {"id": "S1.3-07", "desc": "Prepare maturity assessment report & presentation", "dama_ka": "KA-14", "man_days": 5,
             "roles": [("Data Governance Analyst", 0.30), ("Business Analyst (Data)", 0.25), ("Project Manager (Data)", 0.20), ("Product Writer", 0.25)]},
        ]
    },
    "S1.4": {
        "name": "Data Governance & Policy Framework Development",
        "pillar": 1,
        "dama_kas": ["KA-01", "All KAs"],
        "tasks": [
            {"id": "S1.4-01", "desc": "Audit existing policies, SOPs, and data procedures", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Data Governance Analyst", 0.35), ("Compliance Officer (Data)", 0.25), ("Business Analyst (Data)", 0.20), ("Data Protection Officer (DPO)", 0.20)]},
            {"id": "S1.4-02", "desc": "Gap analysis against regulations (UU PDP, SPBE, SDI)", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Governance Manager", 0.25), ("Compliance Officer (Data)", 0.25), ("Data Protection Officer (DPO)", 0.20), ("Data Security Manager", 0.15), ("Business Analyst (Data)", 0.15)]},
            {"id": "S1.4-03", "desc": "Develop data governance policy & charter", "dama_ka": "KA-01", "man_days": 12,
             "roles": [("Data Governance Manager", 0.30), ("Compliance Officer (Data)", 0.20), ("Data Protection Officer (DPO)", 0.15), ("Data Owner", 0.15), ("Product Writer", 0.20)]},
            {"id": "S1.4-04", "desc": "Develop data quality management SOP", "dama_ka": "KA-11", "man_days": 10,
             "roles": [("Data Quality Manager", 0.30), ("Data Quality Analyst", 0.25), ("Data Steward", 0.20), ("Data Governance Analyst", 0.15), ("Product Writer", 0.10)]},
            {"id": "S1.4-05", "desc": "Develop data security & privacy policy (UU PDP aligned)", "dama_ka": "KA-05", "man_days": 12,
             "roles": [("Data Protection Officer (DPO)", 0.25), ("Data Security Manager", 0.25), ("Compliance Officer (Data)", 0.20), ("Data Governance Manager", 0.15), ("Product Writer", 0.15)]},
            {"id": "S1.4-06", "desc": "Develop metadata management SOP", "dama_ka": "KA-09", "man_days": 8,
             "roles": [("Metadata Manager", 0.30), ("Metadata Analyst", 0.25), ("Data Steward", 0.20), ("Data Governance Analyst", 0.15), ("Product Writer", 0.10)]},
            {"id": "S1.4-07", "desc": "Develop data lifecycle management SOP", "dama_ka": "KA-04", "man_days": 8,
             "roles": [("Data Governance Manager", 0.25), ("Data Custodian", 0.25), ("Database Administrator (DBA)", 0.20), ("Data Steward", 0.15), ("Product Writer", 0.15)]},
            {"id": "S1.4-08", "desc": "Develop data ethics & handling guidelines", "dama_ka": "KA-12", "man_days": 8,
             "roles": [("Data Ethics Manager", 0.30), ("Data Ethicist", 0.25), ("Data Protection Officer (DPO)", 0.20), ("Compliance Officer (Data)", 0.15), ("Product Writer", 0.10)]},
            {"id": "S1.4-09", "desc": "Develop master & reference data management SOP", "dama_ka": "KA-10", "man_days": 8,
             "roles": [("Master Data Manager (MDM)", 0.30), ("Reference Data Manager", 0.25), ("Data Steward", 0.20), ("Data Governance Analyst", 0.15), ("Product Writer", 0.10)]},
            {"id": "S1.4-10", "desc": "Review, approval, and socialization of all policies", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Chief Data Officer (CDO)", 0.20), ("Data Governance Manager", 0.20), ("Change Manager (Data)", 0.25), ("Data Literacy Champion", 0.20), ("Product Writer", 0.15)]},
        ]
    },
    "S1.5": {
        "name": "Data Asset Valuation & Monetization Advisory",
        "pillar": 1,
        "dama_kas": ["KA-01", "KA-14", "KA-11"],
        "tasks": [
            {"id": "S1.5-01", "desc": "Inventory & classify data assets across business domains", "dama_ka": "KA-01", "man_days": 12,
             "roles": [("Data Valuation Specialist", 0.25), ("Data Governance Manager", 0.25), ("Data Steward", 0.20), ("Business Analyst (Data)", 0.15), ("Data Architect", 0.15)]},
            {"id": "S1.5-02", "desc": "Assess data quality & completeness for valuation readiness", "dama_ka": "KA-11", "man_days": 10,
             "roles": [("Data Quality Manager", 0.25), ("Data Quality Analyst", 0.30), ("Data Valuation Specialist", 0.20), ("Data Steward", 0.15), ("Data Analyst", 0.10)]},
            {"id": "S1.5-03", "desc": "Apply Infonomics valuation models (IVA, BVA, PVA, CVA, EVA, MVA)", "dama_ka": "KA-14", "man_days": 15,
             "roles": [("Data Valuation Specialist", 0.35), ("Data Monetization Analyst", 0.25), ("Business Analyst (Data)", 0.20), ("Data Analyst", 0.10), ("Chief Data Officer (CDO)", 0.10)]},
            {"id": "S1.5-04", "desc": "Benchmark data asset value against industry standards", "dama_ka": "KA-14", "man_days": 8,
             "roles": [("Data Valuation Specialist", 0.30), ("Data Monetization Analyst", 0.30), ("Business Analyst (Data)", 0.20), ("Data Analyst", 0.20)]},
            {"id": "S1.5-05", "desc": "Design data monetization strategy & revenue model", "dama_ka": "KA-01", "man_days": 12,
             "roles": [("Data Monetization Analyst", 0.30), ("Data Valuation Specialist", 0.25), ("Chief Data Officer (CDO)", 0.20), ("Business Analyst (Data)", 0.15), ("Data Product Manager", 0.10)]},
            {"id": "S1.5-06", "desc": "Develop data asset balance sheet & executive report", "dama_ka": "KA-14", "man_days": 10,
             "roles": [("Data Valuation Specialist", 0.30), ("Data Monetization Analyst", 0.20), ("Chief Data Officer (CDO)", 0.20), ("Project Manager (Data)", 0.15), ("Product Writer", 0.15)]},
            {"id": "S1.5-07", "desc": "Define data valuation governance & periodic review process", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Governance Manager", 0.30), ("Data Valuation Specialist", 0.25), ("Compliance Officer (Data)", 0.20), ("Data Steward", 0.15), ("Product Writer", 0.10)]},
            {"id": "S1.5-08", "desc": "Present valuation findings & monetization roadmap", "dama_ka": "KA-01", "man_days": 4,
             "roles": [("Chief Data Officer (CDO)", 0.30), ("Data Valuation Specialist", 0.30), ("Data Monetization Analyst", 0.20), ("Project Manager (Data)", 0.20)]},
        ]
    },

    # --- Pillar 2: Platform & Solution ---
    "S2.1": {
        "name": "Data-Centric Digital Product Development & UX Design",
        "pillar": 2,
        "dama_kas": ["KA-03", "KA-02", "KA-05"],
        "tasks": [
            {"id": "S2.1-01", "desc": "Gather & analyze product requirements (PRD)", "dama_ka": "KA-03", "man_days": 10,
             "roles": [("Product Manager", 0.30), ("Product Researcher", 0.25), ("Business Analyst (Data)", 0.25), ("Product Designer", 0.10), ("Data Architect", 0.10)]},
            {"id": "S2.1-02", "desc": "Create business requirements document (BRD)", "dama_ka": "KA-03", "man_days": 8,
             "roles": [("Business Analyst (Data)", 0.35), ("Product Manager", 0.25), ("Subject Matter Expert (SME)", 0.20), ("Product Writer", 0.20)]},
            {"id": "S2.1-03", "desc": "Design functional specification document (FSD)", "dama_ka": "KA-03", "man_days": 12,
             "roles": [("Product Manager", 0.25), ("Product Engineering Architect", 0.25), ("Data Architect", 0.20), ("Business Analyst (Data)", 0.15), ("Product Designer", 0.15)]},
            {"id": "S2.1-04", "desc": "Design data model (conceptual, logical, physical)", "dama_ka": "KA-03", "man_days": 15,
             "roles": [("Data Architect", 0.35), ("Data Modeler", 0.30), ("Data Engineer", 0.15), ("Database Administrator (DBA)", 0.10), ("Data Governance Analyst", 0.10)]},
            {"id": "S2.1-05", "desc": "UI/UX research & wireframing", "dama_ka": "KA-03", "man_days": 12,
             "roles": [("Product Designer", 0.40), ("Product Researcher", 0.30), ("Product Manager", 0.15), ("Data Visualization Specialist", 0.15)]},
            {"id": "S2.1-06", "desc": "UI high-fidelity design & prototyping", "dama_ka": "KA-03", "man_days": 15,
             "roles": [("Product Designer", 0.50), ("Data Visualization Specialist", 0.20), ("Product Manager", 0.15), ("Product Researcher", 0.15)]},
            {"id": "S2.1-07", "desc": "Front-end development", "dama_ka": "KA-03", "man_days": 30,
             "roles": [("Product Engineering Front-End Engineer", 0.60), ("Product Designer", 0.15), ("Product Engineering QA Engineer", 0.15), ("Site Reliability Engineer (DevOps)", 0.10)]},
            {"id": "S2.1-08", "desc": "Back-end development & API design", "dama_ka": "KA-06", "man_days": 30,
             "roles": [("Product Engineering Back-End Engineer", 0.55), ("Product Engineering Architect", 0.15), ("Data Engineer", 0.10), ("Security Engineer", 0.10), ("Product Engineering QA Engineer", 0.10)]},
            {"id": "S2.1-09", "desc": "Data integration & pipeline setup", "dama_ka": "KA-06", "man_days": 15,
             "roles": [("Data Engineer", 0.40), ("ETL/ELT Developer", 0.25), ("Data Architect", 0.15), ("Site Reliability Engineer (DataOps)", 0.10), ("Data Quality Engineer", 0.10)]},
            {"id": "S2.1-10", "desc": "Unit testing & code review", "dama_ka": "KA-03", "man_days": 10,
             "roles": [("Product Engineering QA Engineer", 0.35), ("Product Engineering Front-End Engineer", 0.25), ("Product Engineering Back-End Engineer", 0.25), ("Security Engineer", 0.15)]},
            {"id": "S2.1-11", "desc": "User acceptance testing (UAT)", "dama_ka": "KA-03", "man_days": 10,
             "roles": [("Product Engineering QA Analyst", 0.30), ("Product Manager", 0.20), ("Business Analyst (Data)", 0.20), ("Product Researcher", 0.15), ("Subject Matter Expert (SME)", 0.15)]},
            {"id": "S2.1-12", "desc": "Deploy to staging & production", "dama_ka": "KA-04", "man_days": 8,
             "roles": [("Site Reliability Engineer (DevOps)", 0.40), ("Product Engineering Back-End Engineer", 0.20), ("Product Engineering Front-End Engineer", 0.15), ("Database Administrator (DBA)", 0.15), ("Security Engineer", 0.10)]},
            {"id": "S2.1-13", "desc": "Documentation & knowledge transfer", "dama_ka": "KA-03", "man_days": 8,
             "roles": [("Product Writer", 0.30), ("Product Engineering Writer", 0.25), ("Product Manager", 0.20), ("Product Engineering Architect", 0.15), ("Data Architect", 0.10)]},
        ]
    },
    "S2.2": {
        "name": "Core Data Platform & Modernization",
        "pillar": 2,
        "dama_kas": ["KA-02", "KA-04", "KA-06", "KA-09"],
        "tasks": [
            {"id": "S2.2-01", "desc": "Assess current data infrastructure & architecture", "dama_ka": "KA-02", "man_days": 12,
             "roles": [("Data Architect", 0.30), ("Data Engineering Manager", 0.20), ("Database Administrator (DBA)", 0.20), ("Data Engineer", 0.15), ("Data Governance Analyst", 0.15)]},
            {"id": "S2.2-02", "desc": "Design target data architecture (lake/warehouse/mesh)", "dama_ka": "KA-02", "man_days": 15,
             "roles": [("Data Architect", 0.35), ("Data Warehouse Architect", 0.25), ("Data Engineering Manager", 0.15), ("Data Fabric Architect", 0.15), ("Data Governance Manager", 0.10)]},
            {"id": "S2.2-03", "desc": "Design data modeling & schema for new platform", "dama_ka": "KA-03", "man_days": 12,
             "roles": [("Data Modeler", 0.35), ("Data Architect", 0.25), ("Data Engineer", 0.15), ("Database Administrator (DBA)", 0.15), ("Data Steward", 0.10)]},
            {"id": "S2.2-04", "desc": "Setup cloud/hybrid infrastructure & environments", "dama_ka": "KA-04", "man_days": 15,
             "roles": [("Data Platform/Infrastructure Engineer", 0.35), ("Site Reliability Engineer (DevOps)", 0.25), ("Database Administrator (DBA)", 0.15), ("Security Engineer", 0.15), ("Data Architect", 0.10)]},
            {"id": "S2.2-05", "desc": "Build data ingestion & ETL/ELT pipelines", "dama_ka": "KA-06", "man_days": 20,
             "roles": [("Data Engineer", 0.40), ("ETL/ELT Developer", 0.25), ("Data Architect", 0.15), ("DataOps Engineer", 0.10), ("Data Quality Engineer", 0.10)]},
            {"id": "S2.2-06", "desc": "Implement data quality framework & monitoring", "dama_ka": "KA-11", "man_days": 10,
             "roles": [("Data Quality Engineer", 0.30), ("Data Quality Analyst", 0.25), ("Data Engineer", 0.20), ("Data Steward", 0.15), ("Data Governance Analyst", 0.10)]},
            {"id": "S2.2-07", "desc": "Implement metadata management & data catalog", "dama_ka": "KA-09", "man_days": 12,
             "roles": [("Metadata Manager", 0.25), ("Metadata Analyst", 0.25), ("Data Engineer", 0.20), ("Data Steward", 0.15), ("Data Architect", 0.15)]},
            {"id": "S2.2-08", "desc": "Implement data security & access control", "dama_ka": "KA-05", "man_days": 12,
             "roles": [("Data Security Manager", 0.30), ("Security Engineer", 0.25), ("Data Protection Officer (DPO)", 0.15), ("Data Governance Analyst", 0.15), ("Data Custodian", 0.15)]},
            {"id": "S2.2-09", "desc": "Performance testing & optimization", "dama_ka": "KA-04", "man_days": 10,
             "roles": [("Database Administrator (DBA)", 0.25), ("Data Engineer", 0.25), ("Site Reliability Engineer (DataOps)", 0.20), ("Data Platform/Infrastructure Engineer", 0.15), ("Product Engineering QA Engineer", 0.15)]},
            {"id": "S2.2-10", "desc": "Data migration from legacy systems", "dama_ka": "KA-06", "man_days": 15,
             "roles": [("Data Engineer", 0.30), ("ETL/ELT Developer", 0.25), ("Database Administrator (DBA)", 0.15), ("Data Quality Engineer", 0.15), ("Data Steward", 0.15)]},
            {"id": "S2.2-11", "desc": "Documentation, training, & handover", "dama_ka": "KA-02", "man_days": 8,
             "roles": [("Product Writer", 0.25), ("Data Architect", 0.20), ("Data Engineering Manager", 0.20), ("Data Literacy Champion", 0.20), ("Project Manager (Data)", 0.15)]},
        ]
    },
    "S2.3": {
        "name": "Government Data Portal Platform",
        "pillar": 2,
        "dama_kas": ["KA-09", "KA-01", "KA-02", "KA-06"],
        "tasks": [
            {"id": "S2.3-01", "desc": "Analyze SDI & SPBE compliance requirements", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Compliance Officer (Data)", 0.25), ("Data Governance Manager", 0.25), ("Business Analyst (Data)", 0.25), ("Data Protection Officer (DPO)", 0.15), ("Project Manager (Data)", 0.10)]},
            {"id": "S2.3-02", "desc": "Design portal information architecture", "dama_ka": "KA-02", "man_days": 12,
             "roles": [("Data Architect", 0.30), ("Product Manager", 0.25), ("Product Designer", 0.20), ("Metadata Manager", 0.15), ("Data Governance Analyst", 0.10)]},
            {"id": "S2.3-03", "desc": "Design metadata schema & data catalog structure", "dama_ka": "KA-09", "man_days": 12,
             "roles": [("Metadata Manager", 0.30), ("Metadata Analyst", 0.25), ("Data Architect", 0.20), ("Data Steward", 0.15), ("Data Governance Analyst", 0.10)]},
            {"id": "S2.3-04", "desc": "Design UI/UX for citizen-facing portal", "dama_ka": "KA-09", "man_days": 15,
             "roles": [("Product Designer", 0.40), ("Product Researcher", 0.25), ("Data Visualization Specialist", 0.15), ("Product Manager", 0.10), ("Content Strategist", 0.10)]},
            {"id": "S2.3-05", "desc": "Develop portal front-end (Civic Insight)", "dama_ka": "KA-09", "man_days": 25,
             "roles": [("Product Engineering Front-End Engineer", 0.55), ("Product Designer", 0.15), ("Product Engineering QA Engineer", 0.15), ("Site Reliability Engineer (DevOps)", 0.10), ("Data Visualization Specialist", 0.05)]},
            {"id": "S2.3-06", "desc": "Develop portal back-end & API layer", "dama_ka": "KA-06", "man_days": 25,
             "roles": [("Product Engineering Back-End Engineer", 0.50), ("Product Engineering Architect", 0.15), ("Data Engineer", 0.15), ("Security Engineer", 0.10), ("Product Engineering QA Engineer", 0.10)]},
            {"id": "S2.3-07", "desc": "Build data integration pipelines (multi-OPD)", "dama_ka": "KA-06", "man_days": 20,
             "roles": [("Data Engineer", 0.35), ("ETL/ELT Developer", 0.25), ("Data Integration Specialist", 0.15), ("Data Quality Engineer", 0.15), ("DataOps Engineer", 0.10)]},
            {"id": "S2.3-08", "desc": "Implement open data publishing workflow", "dama_ka": "KA-09", "man_days": 10,
             "roles": [("Data Steward", 0.25), ("Metadata Analyst", 0.25), ("Data Governance Analyst", 0.20), ("Product Engineering Back-End Engineer", 0.15), ("Data Quality Analyst", 0.15)]},
            {"id": "S2.3-09", "desc": "Implement geospatial module (MapEdge)", "dama_ka": "KA-06", "man_days": 15,
             "roles": [("Geospatial Engineer", 0.35), ("Geospatial Analyst", 0.25), ("Geospatial Lead", 0.15), ("Product Engineering Back-End Engineer", 0.15), ("Data Engineer", 0.10)]},
            {"id": "S2.3-10", "desc": "Implement executive dashboard module", "dama_ka": "KA-08", "man_days": 15,
             "roles": [("BI Developer", 0.30), ("Data Visualization Specialist", 0.25), ("Data Analyst", 0.20), ("Product Designer", 0.15), ("Product Engineering Front-End Engineer", 0.10)]},
            {"id": "S2.3-11", "desc": "Security hardening & penetration testing", "dama_ka": "KA-05", "man_days": 10,
             "roles": [("Security Engineer", 0.40), ("Data Security Manager", 0.20), ("Site Reliability Engineer (DevOps)", 0.15), ("Product Engineering QA Engineer", 0.15), ("Data Custodian", 0.10)]},
            {"id": "S2.3-12", "desc": "UAT, performance testing, & go-live", "dama_ka": "KA-04", "man_days": 12,
             "roles": [("Product Engineering QA Analyst", 0.25), ("Product Engineering QA Engineer", 0.20), ("Site Reliability Engineer (DevOps)", 0.20), ("Product Manager", 0.15), ("Project Manager (Data)", 0.20)]},
            {"id": "S2.3-13", "desc": "Training, documentation, & knowledge transfer", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Data Literacy Champion", 0.25), ("Product Writer", 0.25), ("Change Manager (Data)", 0.20), ("Product Manager", 0.15), ("Data Governance Analyst", 0.15)]},
        ]
    },
    "S2.4": {
        "name": "Enterprise Data Portal & Self-Service Analytics",
        "pillar": 2,
        "dama_kas": ["KA-08", "KA-09", "KA-11"],
        "tasks": [
            {"id": "S2.4-01", "desc": "Assess analytics needs & data readiness", "dama_ka": "KA-08", "man_days": 10,
             "roles": [("Data Analytics Manager", 0.25), ("Data Analyst", 0.25), ("Business Analyst (Data)", 0.25), ("Data Architect", 0.15), ("Subject Matter Expert (SME)", 0.10)]},
            {"id": "S2.4-02", "desc": "Design semantic layer & data mart structure", "dama_ka": "KA-08", "man_days": 12,
             "roles": [("Data Warehouse Architect", 0.30), ("Data Architect", 0.25), ("Data Modeler", 0.20), ("Analytics Engineer", 0.15), ("BI Developer", 0.10)]},
            {"id": "S2.4-03", "desc": "Build analytics data pipelines & transformations", "dama_ka": "KA-06", "man_days": 15,
             "roles": [("Analytics Engineer", 0.30), ("Data Engineer", 0.30), ("ETL/ELT Developer", 0.20), ("Data Quality Engineer", 0.10), ("DataOps Engineer", 0.10)]},
            {"id": "S2.4-04", "desc": "Design & develop BI dashboards & reports", "dama_ka": "KA-08", "man_days": 20,
             "roles": [("BI Developer", 0.35), ("Data Visualization Specialist", 0.25), ("Data Analyst", 0.20), ("Product Designer", 0.10), ("Subject Matter Expert (SME)", 0.10)]},
            {"id": "S2.4-05", "desc": "Implement self-service analytics tooling", "dama_ka": "KA-08", "man_days": 12,
             "roles": [("BI Developer", 0.30), ("Data Analyst", 0.25), ("Data Literacy Champion", 0.15), ("Analytics Engineer", 0.15), ("Product Engineering Front-End Engineer", 0.15)]},
            {"id": "S2.4-06", "desc": "Implement data quality monitoring for analytics", "dama_ka": "KA-11", "man_days": 10,
             "roles": [("Data Quality Analyst", 0.30), ("Data Quality Engineer", 0.25), ("Data Steward", 0.20), ("Analytics Engineer", 0.15), ("Data Governance Analyst", 0.10)]},
            {"id": "S2.4-07", "desc": "Implement metadata & data catalog for discovery", "dama_ka": "KA-09", "man_days": 10,
             "roles": [("Metadata Manager", 0.25), ("Metadata Analyst", 0.25), ("Data Steward", 0.20), ("Data Analyst", 0.15), ("Data Governance Analyst", 0.15)]},
            {"id": "S2.4-08", "desc": "User training & self-service enablement", "dama_ka": "KA-08", "man_days": 8,
             "roles": [("Data Literacy Champion", 0.30), ("BI Developer", 0.20), ("Data Analyst", 0.20), ("Change Manager (Data)", 0.15), ("Product Writer", 0.15)]},
        ]
    },
    "S2.5": {
        "name": "Secure & Trusted Data Exchange - API Gateway Platform",
        "pillar": 2,
        "dama_kas": ["KA-06", "KA-05"],
        "tasks": [
            {"id": "S2.5-01", "desc": "Analyze data exchange requirements & use cases", "dama_ka": "KA-06", "man_days": 10,
             "roles": [("Data Integration Manager", 0.25), ("Business Analyst (Data)", 0.25), ("Data Architect", 0.20), ("Data Security Manager", 0.15), ("Product Manager", 0.15)]},
            {"id": "S2.5-02", "desc": "Design API architecture & data exchange patterns", "dama_ka": "KA-06", "man_days": 12,
             "roles": [("Product Engineering Architect", 0.30), ("Data Architect", 0.25), ("Data Integration Manager", 0.15), ("Security Engineer", 0.15), ("Product Engineering Back-End Engineer", 0.15)]},
            {"id": "S2.5-03", "desc": "Design security framework (OAuth, encryption, audit)", "dama_ka": "KA-05", "man_days": 10,
             "roles": [("Security Engineer", 0.35), ("Data Security Manager", 0.25), ("Data Protection Officer (DPO)", 0.15), ("Product Engineering Architect", 0.15), ("Data Custodian", 0.10)]},
            {"id": "S2.5-04", "desc": "Develop API gateway core platform", "dama_ka": "KA-06", "man_days": 25,
             "roles": [("Product Engineering Back-End Engineer", 0.45), ("Product Engineering Architect", 0.15), ("Security Engineer", 0.15), ("Site Reliability Engineer (DevOps)", 0.15), ("Product Engineering QA Engineer", 0.10)]},
            {"id": "S2.5-05", "desc": "Develop API management console (UI)", "dama_ka": "KA-06", "man_days": 15,
             "roles": [("Product Engineering Front-End Engineer", 0.45), ("Product Designer", 0.20), ("Product Engineering Back-End Engineer", 0.15), ("Product Engineering QA Engineer", 0.10), ("Product Manager", 0.10)]},
            {"id": "S2.5-06", "desc": "Implement data validation & transformation layer", "dama_ka": "KA-06", "man_days": 12,
             "roles": [("Data Engineer", 0.30), ("Data Integration Specialist", 0.25), ("Data Quality Engineer", 0.20), ("Product Engineering Back-End Engineer", 0.15), ("ETL/ELT Developer", 0.10)]},
            {"id": "S2.5-07", "desc": "Implement rate limiting, logging, & monitoring", "dama_ka": "KA-05", "man_days": 10,
             "roles": [("Site Reliability Engineer (DevOps)", 0.30), ("Security Engineer", 0.25), ("Product Engineering Back-End Engineer", 0.20), ("DataOps Engineer", 0.15), ("Product Engineering QA Engineer", 0.10)]},
            {"id": "S2.5-08", "desc": "Security testing & penetration testing", "dama_ka": "KA-05", "man_days": 8,
             "roles": [("Security Engineer", 0.40), ("Product Engineering QA Engineer", 0.25), ("Data Security Manager", 0.15), ("Site Reliability Engineer (DevOps)", 0.10), ("Product Engineering QA Analyst", 0.10)]},
            {"id": "S2.5-09", "desc": "API documentation & developer portal", "dama_ka": "KA-06", "man_days": 8,
             "roles": [("Product Engineering Writer", 0.30), ("Product Writer", 0.25), ("Product Engineering Architect", 0.20), ("Product Engineering Back-End Engineer", 0.15), ("Product Manager", 0.10)]},
        ]
    },
    "S2.6": {
        "name": "Analytics and Visualization Solutions",
        "pillar": 2,
        "dama_kas": ["KA-08", "KA-11"],
        "tasks": [
            {"id": "S2.6-01", "desc": "Gather analytics & visualization requirements", "dama_ka": "KA-08", "man_days": 8,
             "roles": [("Data Analyst", 0.30), ("Business Analyst (Data)", 0.25), ("Data Visualization Specialist", 0.20), ("Subject Matter Expert (SME)", 0.15), ("Product Manager", 0.10)]},
            {"id": "S2.6-02", "desc": "Design KPI framework & metrics hierarchy", "dama_ka": "KA-08", "man_days": 10,
             "roles": [("Data Analytics Manager", 0.25), ("Data Analyst", 0.25), ("Business Analyst (Data)", 0.20), ("Subject Matter Expert (SME)", 0.15), ("BI Developer", 0.15)]},
            {"id": "S2.6-03", "desc": "Design dashboard wireframes & visual mockups", "dama_ka": "KA-08", "man_days": 10,
             "roles": [("Data Visualization Specialist", 0.35), ("Product Designer", 0.30), ("Data Analyst", 0.15), ("BI Developer", 0.10), ("Product Manager", 0.10)]},
            {"id": "S2.6-04", "desc": "Build data preparation & aggregation pipelines", "dama_ka": "KA-06", "man_days": 12,
             "roles": [("Analytics Engineer", 0.30), ("Data Engineer", 0.25), ("ETL/ELT Developer", 0.20), ("Data Quality Engineer", 0.10), ("DataOps Engineer", 0.15)]},
            {"id": "S2.6-05", "desc": "Develop interactive dashboards & reports", "dama_ka": "KA-08", "man_days": 15,
             "roles": [("BI Developer", 0.35), ("Data Visualization Specialist", 0.25), ("Data Analyst", 0.15), ("Product Engineering Front-End Engineer", 0.15), ("Product Designer", 0.10)]},
            {"id": "S2.6-06", "desc": "Conduct UAT & gather user feedback", "dama_ka": "KA-08", "man_days": 5,
             "roles": [("Product Engineering QA Analyst", 0.30), ("Data Analyst", 0.25), ("Business Analyst (Data)", 0.20), ("Product Manager", 0.15), ("Subject Matter Expert (SME)", 0.10)]},
            {"id": "S2.6-07", "desc": "User training & solution handover", "dama_ka": "KA-08", "man_days": 4,
             "roles": [("Data Literacy Champion", 0.30), ("BI Developer", 0.25), ("Data Analyst", 0.20), ("Change Manager (Data)", 0.15), ("Product Writer", 0.10)]},
        ]
    },

    # --- Pillar 3: Capability & Delivery ---
    "S3.1": {
        "name": "Data Literacy & Corporate Training Program",
        "pillar": 3,
        "dama_kas": ["KA-01", "All KAs"],
        "tasks": [
            {"id": "S3.1-01", "desc": "Conduct training needs analysis (TNA)", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Literacy Champion", 0.30), ("Change Manager (Data)", 0.25), ("Business Analyst (Data)", 0.25), ("Subject Matter Expert (SME)", 0.20)]},
            {"id": "S3.1-02", "desc": "Design curriculum & learning paths by role", "dama_ka": "KA-01", "man_days": 15,
             "roles": [("Data Literacy Champion", 0.35), ("Subject Matter Expert (SME)", 0.25), ("Change Manager (Data)", 0.20), ("Product Writer", 0.20)]},
            {"id": "S3.1-03", "desc": "Develop training materials (slides, labs, quizzes)", "dama_ka": "KA-01", "man_days": 20,
             "roles": [("Product Writer", 0.30), ("Data Literacy Champion", 0.25), ("Subject Matter Expert (SME)", 0.25), ("Product Designer", 0.20)]},
            {"id": "S3.1-04", "desc": "Deliver training sessions (instructor-led)", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Data Literacy Champion", 0.50), ("Subject Matter Expert (SME)", 0.50)]},
            {"id": "S3.1-05", "desc": "Develop e-learning modules", "dama_ka": "KA-01", "man_days": 15,
             "roles": [("Product Writer", 0.30), ("Product Designer", 0.25), ("Data Literacy Champion", 0.25), ("Product Engineering Front-End Engineer", 0.20)]},
            {"id": "S3.1-06", "desc": "Post-training evaluation & feedback analysis", "dama_ka": "KA-01", "man_days": 5,
             "roles": [("Data Literacy Champion", 0.40), ("Change Manager (Data)", 0.30), ("Business Analyst (Data)", 0.30)]},
        ]
    },
    "S3.2": {
        "name": "Center of Excellence (CoE) Setup & Operations",
        "pillar": 3,
        "dama_kas": ["KA-01", "KA-02"],
        "tasks": [
            {"id": "S3.2-01", "desc": "Define CoE vision, mission, and charter", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Chief Data Officer (CDO)", 0.30), ("Data Governance Manager", 0.25), ("Data Analytics Manager", 0.25), ("Project Manager (Data)", 0.20)]},
            {"id": "S3.2-02", "desc": "Design CoE operating model & organizational structure", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Chief Data Officer (CDO)", 0.25), ("Data Governance Manager", 0.25), ("Change Manager (Data)", 0.20), ("Project Manager (Data)", 0.15), ("Business Analyst (Data)", 0.15)]},
            {"id": "S3.2-03", "desc": "Develop CoE service catalog & engagement model", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Governance Manager", 0.30), ("Data Analytics Manager", 0.25), ("Business Analyst (Data)", 0.20), ("Project Manager (Data)", 0.15), ("Product Writer", 0.10)]},
            {"id": "S3.2-04", "desc": "Define CoE roles, responsibilities, and career paths", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Change Manager (Data)", 0.30), ("Data Governance Manager", 0.25), ("Data Analytics Manager", 0.25), ("Chief Data Officer (CDO)", 0.20)]},
            {"id": "S3.2-05", "desc": "Develop CoE governance processes & performance metrics", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Data Governance Manager", 0.35), ("Data Quality Manager", 0.20), ("Project Manager (Data)", 0.20), ("Chief Data Officer (CDO)", 0.15), ("Data Analyst", 0.10)]},
            {"id": "S3.2-06", "desc": "Knowledge management & best practice sharing framework", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Data Literacy Champion", 0.30), ("Change Manager (Data)", 0.25), ("Data Governance Analyst", 0.20), ("Product Writer", 0.15), ("Data Steward", 0.10)]},
            {"id": "S3.2-07", "desc": "CoE launch, communication, and change management", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Change Manager (Data)", 0.40), ("Project Manager (Data)", 0.20), ("Chief Data Officer (CDO)", 0.15), ("Data Literacy Champion", 0.15), ("Product Writer", 0.10)]},
        ]
    },
    "S3.3": {
        "name": "Strategic Staffing & Expert Placement (Body Leasing)",
        "pillar": 3,
        "dama_kas": ["All KAs"],
        "tasks": [
            {"id": "S3.3-01", "desc": "Client role requirement analysis", "dama_ka": "KA-01", "man_days": 5,
             "roles": [("Account Manager", 0.40), ("Talent Acquisition Specialist", 0.30), ("Subject Matter Expert (SME)", 0.30)]},
            {"id": "S3.3-02", "desc": "Candidate sourcing & screening", "dama_ka": "KA-01", "man_days": 10,
             "roles": [("Talent Acquisition Specialist", 0.60), ("Subject Matter Expert (SME)", 0.40)]},
            {"id": "S3.3-03", "desc": "Technical & cultural fit interviews", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Subject Matter Expert (SME)", 0.50), ("Account Manager", 0.25), ("Talent Acquisition Specialist", 0.25)]},
            {"id": "S3.3-04", "desc": "Contract negotiation & onboarding", "dama_ka": "KA-01", "man_days": 4,
             "roles": [("Account Manager", 0.50), ("Talent Acquisition Specialist", 0.50)]},
        ]
    },
    "S3.4": {
        "name": "Managed Data Services",
        "pillar": 3,
        "dama_kas": ["All KAs"],
        "tasks": [
            {"id": "S3.4-01", "desc": "Service level agreement (SLA) definition", "dama_ka": "KA-01", "man_days": 8,
             "roles": [("Account Manager", 0.30), ("Project Manager (Data)", 0.25), ("Data Governance Manager", 0.20), ("Subject Matter Expert (SME)", 0.15), ("Data Quality Manager", 0.10)]},
            {"id": "S3.4-02", "desc": "Service transition & setup", "dama_ka": "KA-01", "man_days": 15,
             "roles": [("Project Manager (Data)", 0.30), ("Data Engineer", 0.20), ("Database Administrator (DBA)", 0.15), ("Data Governance Analyst", 0.15), ("Site Reliability Engineer (DataOps)", 0.20)]},
            {"id": "S3.4-03", "desc": "Ongoing service delivery & monitoring", "dama_ka": "KA-01", "man_days": 30, # Placeholder for monthly effort
             "roles": [("Project Manager (Data)", 0.20), ("Data Engineer", 0.20), ("Data Analyst", 0.15), ("Data Quality Analyst", 0.15), ("Data Steward", 0.15), ("Site Reliability Engineer (DataOps)", 0.15)]},
            {"id": "S3.4-04", "desc": "Service reporting & review meetings", "dama_ka": "KA-01", "man_days": 5,
             "roles": [("Project Manager (Data)", 0.30), ("Account Manager", 0.25), ("Data Analyst", 0.25), ("Data Governance Manager", 0.20)]},
        ]
    }
}

def validate_service_data():
    """
    Validates the integrity of the SERVICES data structure.

    Checks for:
    - Duplicate service IDs.
    - Duplicate task IDs within a service.
    - Role names that do not exist in the RATE_CARD.
    - Role involvement percentages that do not sum to 1.0 per task.

    Raises:
        ValueError: If any validation check fails.
    """
    logger.info("Performing data validation on SERVICES dictionary...")
    rate_card_roles = set(RATE_CARD.keys())
    
    for service_id, service_data in SERVICES.items():
        task_ids = set()
        for task in service_data.get("tasks", []):
            # Check for duplicate task IDs
            task_id = task.get("id")
            if task_id in task_ids:
                raise ValueError(f"Duplicate task ID '{task_id}' found in service '{service_id}'.")
            task_ids.add(task_id)

            # Check role validity and percentage sum
            total_involvement = 0
            for role_name, involvement in task.get("roles", []):
                if role_name not in rate_card_roles:
                    raise ValueError(f"Role '{role_name}' in task '{task_id}' (Service '{service_id}') not found in RATE_CARD.")
                total_involvement += involvement
            
            # Allow for minor floating point inaccuracies
            if not (0.999 < total_involvement < 1.001):
                logger.warning(
                    f"Role involvement for task '{task_id}' (Service '{service_id}') does not sum to 1.0. "
                    f"Actual sum: {total_involvement:.3f}"
                )
    logger.info("SERVICES data validation successful.")

def get_service_total_man_days(service_id: str, complexity_multiplier: float = 1.0) -> float:
    """
    Calculates the total man-days for a given service, adjusted for complexity.

    Args:
        service_id: The ID of the service.
        complexity_multiplier: The complexity factor to apply.

    Returns:
        The total adjusted man-days for the service.
    
    Raises:
        ValueError: If the service_id is not found.
    """
    if service_id not in SERVICES:
        raise ValueError(f"Service '{service_id}' not found.")
    
    total_man_days = sum(task['man_days'] for task in SERVICES[service_id]['tasks'])
    return total_man_days * complexity_multiplier

def calculate_service_cost(service_id: str, level_spec: Union[int, Dict[str, int]], complexity_multiplier: float = 1.0, internal: bool = False) -> Tuple[float, List[Dict[str, Any]]]:
    """
    Calculates the total cost of a single service by breaking it down into tasks and roles.

    Args:
        service_id: The ID of the service to calculate.
        level_spec: The project level, either as a single integer or a dictionary mapping role categories to levels.
        complexity_multiplier: A factor to adjust man-days for project complexity.
        internal: If True, calculates internal cost (COGS). Otherwise, calculates external client price.

    Returns:
        A tuple containing:
        - The total cost of the service.
        - A detailed breakdown of costs per task and role.

    Raises:
        ValueError: If the service_id is not found or a role is invalid.
    """
    if service_id not in SERVICES:
        raise ValueError(f"Service '{service_id}' not found.")

    service = SERVICES[service_id]
    total_cost = 0.0
    task_breakdown = []

    get_rate = get_internal_daily_rate if internal else get_daily_rate

    for task in service['tasks']:
        task_man_days = task['man_days'] * complexity_multiplier
        task_cost = 0.0
        role_breakdown = []

        for role_name, involvement in task['roles']:
            try:
                level = get_role_level(role_name, level_spec)
                daily_rate = get_rate(role_name, level)
                
                role_man_days = task_man_days * involvement
                role_cost = role_man_days * daily_rate
                task_cost += role_cost

                role_breakdown.append({
                    "role": role_name,
                    "level": level,
                    "man_days": round(role_man_days, 2),
                    "daily_rate": daily_rate,
                    "cost": role_cost
                })
            except (ValueError, TypeError) as e:
                logger.error(f"Could not calculate cost for role '{role_name}' in task '{task['id']}': {e}")
                # Optionally, decide whether to continue or stop
                continue # Skip roles that cannot be priced
        
        total_cost += task_cost
        task_breakdown.append({
            "task_id": task['id'],
            "description": task['desc'],
            "man_days": round(task_man_days, 2),
            "cost": task_cost,
            "roles": role_breakdown
        })

    return total_cost, task_breakdown


def estimate_service_cost(service_id: str, level_spec: Union[int, Dict[str, int]], level_map: Dict[str, int] = None, complexity_multiplier: float = 1.0, pricing_mode: str = "external") -> Dict[str, Any]:
    """
    Backward-compatible wrapper that returns a dict with keys expected by
    other scripts like generate_rab.py and generate_proposal.py.

    Args:
        service_id: The ID of the service.
        level_spec: The project level (integer) or level map (dict).
        level_map: A dictionary mapping role categories to levels (legacy support).
        complexity_multiplier: The complexity factor.
        pricing_mode: 'external' for client price, 'internal' for COGS.

    Returns:
        A dictionary containing the detailed cost estimation for the service.
    """
    if service_id not in SERVICES:
        logger.error(f"Service '{service_id}' not found in the database.")
        return {"error": f"Service '{service_id}' not found in the database."}
    
    service = SERVICES[service_id]
    internal = (pricing_mode == "internal")
    effective_level = level_map if level_map else level_spec

    try:
        total_cost, task_breakdown = calculate_service_cost(
            service_id, effective_level, complexity_multiplier, internal
        )
    except Exception as e:
        logger.exception(f"An error occurred during cost calculation for service '{service_id}'.")
        return {"error": str(e)}

    total_man_days = sum(t["man_days"] for t in task_breakdown)
    tasks = []
    for t in task_breakdown:
        tasks.append({
            "task_id": t["task_id"],
            "description": t["description"],
            "dama_ka": next((tk.get("dama_ka", "") for tk in service["tasks"] if tk["id"] == t["task_id"]), ""),
            "man_days": t["man_days"],
            "adjusted_man_days": t["man_days"], # Retained for compatibility
            "total_cost": t["cost"],
            "roles": t["roles"],
        })

    return {
        "service_id": service_id,
        "service_name": service["name"],
        "pillar": service.get("pillar", 0),
        "total_cost": total_cost,
        "total_man_days": total_man_days,
        "tasks": tasks,
    }


def get_role_level(role_name: str, level_spec: Union[int, Dict[str, int]]) -> int:
    """
    Determines the appropriate level for a given role based on the level specification.

    Args:
        role_name: The name of the role.
        level_spec: An integer for a project-wide level, or a dictionary mapping
                    role categories to specific levels.

    Returns:
        The determined level for the role.

    Raises:
        ValueError: If the role or its category is not found when using a level map.
        TypeError: If level_spec is not an int or dict.
    """
    if isinstance(level_spec, int):
        return level_spec
    
    if isinstance(level_spec, dict):
        # Find the category for the given role from the master RATE_CARD
        for role_name_key, role_info in RATE_CARD.items():
            if role_name_key == role_name:
                category = role_info['category']
                if category in level_spec:
                    return level_spec[category]
                else:
                    raise ValueError(f"Role category '{category}' for role '{role_name}' not found in custom level map.")
        raise ValueError(f"Role '{role_name}' not found in the rate card.")

    raise TypeError(f"level_spec must be an integer or a dictionary, but got {type(level_spec)}.")

def display_results(total_cost: float, total_man_days: float, service_names: List[str], args: argparse.Namespace, breakdown: Dict[str, Any] = None):
    """Formats and prints the estimation results to the console."""
    print("\n" + "="*80)
    print(" " * 25 + "IDEAS Service Cost Estimate")
    print("="*80)
    svc_list = ', '.join(service_names)
    print(f"Services: {svc_list}")
    print(f"Total Estimated Man-Days: {total_man_days:.2f}")
    print(f"Complexity Multiplier: {args.complexity}")
    print("-" * 80)
    
    print("-" * 80)
    print(f"TOTAL ESTIMATED PROJECT COST: IDR {total_cost:,.2f}")
    print("="*80)
    print("\nNote: This is a budgetary estimate. Actual costs may vary.")
    print("Final costs are subject to a detailed Statement of Work (SoW).")

    if args.breakdown and breakdown:
        print("\n" + "="*80)
        print(" " * 28 + "Detailed Task Breakdown")
        print("="*80)
        for service_id, service_breakdown in breakdown.items():
            service_name = SERVICES[service_id]['name']
            print(f"\n--- Service: {service_id} - {service_name} ---\n")
            for task in service_breakdown:
                print(f"  - Task: {task['task_id']} ({task['description']})")
                print(f"    Man-Days: {task['man_days']:.2f}, Cost: IDR {task['cost']:,.2f}")
                for role in task['roles']:
                    print(f"      - {role['role']} (L{role['level']}): {role['man_days']:.2f} days @ IDR {role['daily_rate']:,.2f}/day = IDR {role['cost']:,.2f}")

def main():
    """Main function to parse arguments and run the estimator."""
    parser = argparse.ArgumentParser(
        description="IDEAS Service Cost Estimator.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent(__doc__)
    )
    parser.add_argument(
        '--service', 
        help="A single service ID to estimate (e.g., S1.1)."
    )
    parser.add_argument(
        '--services', 
        help="A comma-separated list of service IDs to estimate (e.g., S1.1,S2.3)."
    )
    parser.add_argument(
        '--level', 
        type=int, 
        help="The project level (e.g., 8). Overridden by --level-map if provided."
    )
    parser.add_argument(
        '--level-map', 
        type=json.loads, 
        help="A JSON string mapping role categories to levels, e.g., '{{\"Management\":15, \"Analyst\":8}}'."
    )
    parser.add_argument(
        '--complexity', 
        type=float, 
        default=COMPLEXITY_MULTIPLIERS['medium'],
        help=f"Complexity multiplier. Can be a float or a keyword:\n"
             f"  simple:  {COMPLEXITY_MULTIPLIERS['simple']}\n"
             f"  medium:  {COMPLEXITY_MULTIPLIERS['medium']} (default)\n"
             f"  complex: {COMPLEXITY_MULTIPLIERS['complex']}"
    )
    parser.add_argument(
        '--internal', 
        action='store_true', 
        help="Calculate internal cost (COGS) instead of client price."
    )
    parser.add_argument(
        '--list-services', 
        action='store_true', 
        help="List all available services and their base man-days."
    )
    parser.add_argument(
        '--breakdown', 
        action='store_true', 
        help="Show a detailed breakdown of tasks and roles for the selected service(s)."
    )
    parser.add_argument(
        '--json', 
        action='store_true', 
        help="Output the results in JSON format."
    )

    args = parser.parse_args()

    try:
        validate_service_data()
    except ValueError as e:
        logger.error(f"Data validation failed: {e}")
        sys.exit(1)

    if args.list_services:
        print("Available Services:")
        for sid, s_info in sorted(SERVICES.items()):
            total_days = get_service_total_man_days(sid)
            print(f"  - {sid}: {s_info['name']} ({total_days:.2f} man-days)")
        sys.exit(0)

    if not (args.service or args.services) or (args.level is None and args.level_map is None):
        parser.error("You must specify at least one service (--service or --services) and a level (--level or --level-map).")

    service_ids = []
    if args.services:
        service_ids = [s.strip() for s in args.services.split(',')]
    elif args.service:
        service_ids = [args.service]

    level_spec = args.level_map if args.level_map else args.level

    # Validate level range
    if isinstance(level_spec, int) and not (1 <= level_spec <= 24):
        parser.error(f"Level must be between 1 and 24, got {level_spec}.")

    total_cost = 0.0
    total_man_days = 0.0
    service_names = []
    full_breakdown = {}

    for sid in service_ids:
        try:
            # Note: get_service_total_man_days is not used for final cost calculation,
            # but retained for potential independent man-day estimation.
            man_days = get_service_total_man_days(sid, args.complexity)
            cost, task_breakdown = calculate_service_cost(sid, level_spec, args.complexity, args.internal)
            
            # The true total man-days comes from the sum of the breakdown
            total_man_days += sum(t['man_days'] for t in task_breakdown)
            total_cost += cost
            service_names.append(f"{sid} - {SERVICES[sid]['name']}")
            full_breakdown[sid] = task_breakdown
        except (ValueError, TypeError) as e:
            logger.error(f"Error processing service '{sid}': {e}", exc_info=True)
            sys.exit(1)

    if args.json:
        output = {
            "services": service_names,
            "total_man_days": round(total_man_days, 2),
            "complexity_multiplier": args.complexity,
            "total_cost": total_cost,
            "cost_breakdown": {"total_cost": total_cost}, # Retained for compatibility
            "detailed_breakdown": full_breakdown if args.breakdown else "Not requested"
        }
        print(json.dumps(output, indent=4))
    else:
        display_results(total_cost, total_man_days, service_names, args, full_breakdown)

if __name__ == "__main__":
    main()
