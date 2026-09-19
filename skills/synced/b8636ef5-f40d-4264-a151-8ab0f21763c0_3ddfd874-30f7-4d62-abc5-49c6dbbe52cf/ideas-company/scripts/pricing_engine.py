#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- version: 2.0 ---
"""
Unified Pricing Engine for IDEAS.

Version: 2.0

This module is the single source of truth for all financial calculations related to
personnel cost, project pricing, and proposal generation. It centralizes all
constants, rate cards, and calculation logic to ensure consistency and ease of
maintenance.

It supports four primary pricing models:
  1. Man-day/Monthly (Internal COGS): Detailed cost breakdown per role, used for
     internal cost of goods sold (COGS) and profitability analysis.
  2. Headcount-Based (Government Proposal — LEGACY): A simplified model using a
     flat rate per person per month. DEPRECATED in favor of Model 4.
  3. Lump Sum (Enterprise/BUMN Pitch): A single, fixed price for a defined scope
     of work, typically used for enterprise clients and state-owned enterprises (BUMN).
  4. Flexible Competency-Based (Government/Enterprise — RECOMMENDED): A dynamic
     model that prices each team member individually based on their role, education
     tier (SMK/D3/S1/S2/S3), and years of experience. Sourced from SALARY_MASTER
     (DataMasterSalaryRate2026.xlsx). This model replaces the fixed Rp 20M/person/month
     approach with granular, competency-driven pricing.

Key Improvements in v2.0:
  - Added Model 4: Flexible Competency-Based pricing via SALARY_MASTER.
  - Deprecated fixed GOV_FLAT_RATE_PER_PERSON_PER_MONTH (Rp 20M) in favor of
    dynamic lookup by role + education + experience.
  - Added calculate_gov_proposal_flexible() for new government proposals.
  - Added format_flexible_pricing_table() for human-readable output.
  - Retained Model 2 for backward compatibility with legacy proposals only.
"""

import logging
from typing import Dict, Any, Optional, Union

# ==============================================================================
# CONFIGURATION & CONSTANTS
# ==============================================================================
# All financial and policy-related constants are defined here. This section
# serves as the central configuration for the entire pricing engine.
# ==============================================================================

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# --- Import from Rate Card ---
# Support both direct execution (python3 scripts/pricing_engine.py) and
# package-style import (from scripts.pricing_engine import ...)
import sys as _sys
import os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
try:
    from rate_card import (
        RATE_CARD, TYPICAL_TEAMS, SALARY_MASTER, ROLE_MULTIPLIER, ROLE_SERVICE_MAP,
        EDUCATION_TIERS, EDUCATION_EXP_KEY,
        get_salary_rate, find_level_by_experience,
        get_flexible_personnel_cost, calculate_team_cost_flexible,
        list_salary_master_roles, get_role_salary_range,
    )
except ImportError:
    logger.critical("Failed to import from rate_card.py. Please ensure the file exists and is in the same directory.")
    RATE_CARD = {}
    TYPICAL_TEAMS = {}
    SALARY_MASTER = {}
    ROLE_MULTIPLIER = {}
    ROLE_SERVICE_MAP = {}

# --- Financial & HR Constants ---
# These constants define the core financial parameters for salary and cost
# calculations. They are based on Indonesian labor laws and company policy.

UMK_2026: int = 4737678  # UMP/UMK reference for the year 2026. FUTURE: Update annually.

# BPJS Rates (Social Security)
# Individual contributions (deducted from employee salary)
BPJS_KESEHATAN_INDIVIDU_RATE: float = 0.01  # BPJS Kesehatan (Health)
BPJS_JHT_INDIVIDU_RATE: float = 0.02      # Jaminan Hari Tua (Old Age Security)
BPJS_JP_INDIVIDU_RATE: float = 0.01       # Jaminan Pensiun (Pension)

# Company contributions (paid by the employer)
BPJS_KESEHATAN_PERUSAHAAN_RATE: float = 0.04  # BPJS Kesehatan (Health)
BPJS_JKK_PERUSAHAAN_RATE: float = 0.0174     # Jaminan Kecelakaan Kerja (Work Accident)
BPJS_JKM_PERUSAHAAN_RATE: float = 0.003      # Jaminan Kematian (Death Benefit)
BPJS_JHT_PERUSAHAAN_RATE: float = 0.037      # Jaminan Hari Tua (Old Age Security)
BPJS_JP_PERUSAHAAN_RATE: float = 0.02       # Jaminan Pensiun (Pension)

# --- PPh 21 Tax Brackets (2026) ---
# Based on UU HPP No. 7 Tahun 2021, effective 2022.
PPH21_BRACKETS: list[dict[str, Union[float, None]]] = [
    {'min': 0, 'max': 60_000_000, 'rate': 0.05},
    {'min': 60_000_001, 'max': 250_000_000, 'rate': 0.15},
    {'min': 250_000_001, 'max': 500_000_000, 'rate': 0.25},
    {'min': 500_000_001, 'max': 5_000_000_000, 'rate': 0.30},
    {'min': 5_000_000_001, 'max': None, 'rate': 0.35},
]

# --- Pricing & Margin Constants ---
MARGIN_RATE: float = 0.30  # Standard profit margin applied to internal costs for external pricing.
FREELANCE_DAILY_PREMIUM: float = 0.10  # Premium added to daily rates for freelance contracts.
FREELANCE_HOURLY_PREMIUM: float = 0.30 # Premium added to hourly rates for freelance contracts.

# --- Government Proposal Constants ---
# These constants are aligned with Indonesian government procurement standards.
# Compliant with Perpres 46/2025 (replaces Perpres 16/2018).
# Reference: SBM (Standar Biaya Masukan) for IT consulting rates.
#
# IMPORTANT: The fixed flat rate (GOV_FLAT_RATE_PER_PERSON_PER_MONTH) is DEPRECATED.
# Use the flexible competency-based model via calculate_gov_proposal_flexible() instead.
# The flat rate is retained ONLY for backward compatibility with legacy proposals.
# New proposals MUST use the flexible model that prices each team member individually
# based on their role, education, and years of experience.
GOV_FLAT_RATE_PER_PERSON_PER_MONTH: int = 20_000_000  # DEPRECATED: Legacy blended rate. Use SALARY_MASTER instead.
GOV_OPERATIONAL_RATIO: float = 0.225  # Operational cost ratio (~22.5% of personnel cost).
GOV_RISK_MANAGEMENT_RATE: float = 0.10  # Risk management surcharge (10% of personnel + operational).

# --- Growth Table (Level-based Salary Multiplier) ---
# Defines the salary multiplier based on employee level. This table is crucial
# for mapping experience and seniority to compensation.
GROWTH_TABLE: Dict[int, float] = {
    1: -0.20, 2: -0.15, 3: -0.10, 4: -0.05, 5: 0.00,
    6: 0.10, 7: 0.20, 8: 0.30, 9: 0.40, 10: 0.55,
    11: 0.70, 12: 0.85, 13: 1.00, 14: 1.20, 15: 1.40,
    16: 1.60, 17: 1.80, 18: 2.05, 19: 2.30, 20: 2.55,
    21: 2.80, 22: 3.10, 23: 3.40, 24: 3.70,
}

# ==============================================================================
# INTERNAL CALCULATION HELPERS
# ==============================================================================

def _calculate_pph21(gaji_kotor_tahunan: float) -> float:
    """
    Calculate the annual PPh 21 income tax based on Indonesian tax brackets.

    This function uses a data-driven approach from the PPH21_BRACKETS constant,
    making it easy to update tax regulations without changing the code logic.

    Args:
        gaji_kotor_tahunan: The gross annual salary.

    Returns:
        The calculated annual PPh 21 tax amount.
    """
    if not isinstance(gaji_kotor_tahunan, (int, float)) or gaji_kotor_tahunan < 0:
        logger.warning(f"Invalid input for PPh 21 calculation: {gaji_kotor_tahunan}. Returning 0.")
        return 0

    tax: float = 0
    remaining_income: float = gaji_kotor_tahunan

    for i, bracket in enumerate(PPH21_BRACKETS):
        bracket_min = bracket['min']
        bracket_max = bracket['max']
        rate = bracket['rate']

        if remaining_income <= 0:
            break

        # Determine the taxable amount in the current bracket
        if bracket_max is None: # Top bracket
            taxable_in_bracket = remaining_income
        else:
            # Calculate the width of the previous bracket to find the taxable amount
            prev_max = PPH21_BRACKETS[i-1]['max'] if i > 0 else 0
            taxable_in_bracket = min(remaining_income, bracket_max - prev_max)

        tax += taxable_in_bracket * rate
        remaining_income -= taxable_in_bracket

    return tax

# ============================================================
# MODEL 1: Man-day/Monthly (Internal COGS) — Original Model
# ============================================================

def get_cost_breakdown(role: str, level: int) -> Dict[str, Any]:
    """
    Calculates a detailed cost breakdown for a given role and level.
    This is the core function for determining internal costs and external pricing.

    The calculation applies a role-specific salary multiplier (ROLE_MULTIPLIER)
    that reflects market scarcity and specialization premium for each role.
    This ensures that high-demand roles (e.g., GenAI Specialist, ML Engineer)
    command higher rates than commodity roles within the same category.

    Args:
        role: The job title/role (must exist as a key in RATE_CARD).
        level: The seniority level (must exist as a key in GROWTH_TABLE).

    Returns:
        A dictionary containing a detailed breakdown of costs, or an error message.
    """
    try:
        if role not in RATE_CARD:
            logger.error(f"Role '{role}' not found in rate_card.")
            return {'error': f"Role '{role}' not found in rate_card."}
        if level not in GROWTH_TABLE:
            logger.error(f"Level {level} is invalid. Must be between 1 and {len(GROWTH_TABLE)}.")
            return {'error': f"Level {level} is invalid. Must be between 1 and {len(GROWTH_TABLE)}."}

        info = RATE_CARD[role]
        growth_factor = 1 + GROWTH_TABLE[level]

        # Apply role-specific multiplier for market scarcity/specialization premium
        role_mult = ROLE_MULTIPLIER.get(role, 1.00)

        gaji_pokok = UMK_2026 * growth_factor * role_mult
        tunjangan_tetap = (info.get("tunjangan_jabatan", 0) + info.get("tunjangan_keahlian", 0)) * role_mult
        tunjangan_tidak_tetap = info.get("tunjangan_harian", 0) * role_mult
        gaji_kotor = gaji_pokok + tunjangan_tetap + tunjangan_tidak_tetap
        
        potongan_bpjs_individu = gaji_kotor * (BPJS_KESEHATAN_INDIVIDU_RATE + BPJS_JHT_INDIVIDU_RATE + BPJS_JP_INDIVIDU_RATE)
        pph21 = _calculate_pph21(gaji_kotor * 12) / 12
        total_potongan_individu = potongan_bpjs_individu + pph21
        take_home_pay = gaji_kotor - total_potongan_individu

        beban_bpjs_perusahaan = gaji_kotor * (BPJS_KESEHATAN_PERUSAHAAN_RATE + BPJS_JKK_PERUSAHAAN_RATE + BPJS_JKM_PERUSAHAAN_RATE + BPJS_JHT_PERUSAHAAN_RATE + BPJS_JP_PERUSAHAAN_RATE)
        biaya_personil_internal = take_home_pay + beban_bpjs_perusahaan
        harga_eksternal = biaya_personil_internal * (1 + MARGIN_RATE)

        return {
            "role": role,
            "level": level,
            "role_multiplier": role_mult,
            "gaji_pokok": gaji_pokok,
            "tunjangan_tetap": tunjangan_tetap,
            "tunjangan_tidak_tetap": tunjangan_tidak_tetap,
            "gaji_kotor_freelancer_rate": gaji_kotor,
            "potongan_bpjs_individu": potongan_bpjs_individu,
            "pph21": pph21,
            "total_potongan_individu": total_potongan_individu,
            "take_home_pay": take_home_pay,
            "beban_bpjs_perusahaan": beban_bpjs_perusahaan,
            "biaya_personil_internal": biaya_personil_internal,
            "harga_eksternal_client_price": harga_eksternal,
        }
    except Exception as e:
        logger.exception(f"An unexpected error occurred in get_cost_breakdown for role '{role}' L{level}: {e}")
        return {'error': "An unexpected error occurred during calculation."}

def get_external_price(role: str, level: int) -> float:
    """Gets the final external client price for a role and level."""
    breakdown = get_cost_breakdown(role, level)
    return breakdown.get("harga_eksternal_client_price", 0)

def get_freelancer_price(role: str, level: int) -> float:
    """Gets the gross monthly rate for a freelancer."""
    breakdown = get_cost_breakdown(role, level)
    return breakdown.get("gaji_kotor_freelancer_rate", 0)

def get_daily_rate(role: str, level: int, model: str = "fulltime") -> float:
    """Calculates the daily rate, with an optional premium for freelancers."""
    try:
        if model == "freelancer":
            monthly_rate = get_freelancer_price(role, level)
            return (monthly_rate / 22) * (1 + FREELANCE_DAILY_PREMIUM)
        else:
            monthly_rate = get_external_price(role, level)
            return monthly_rate / 22
    except (TypeError, ZeroDivisionError) as e:
        logger.error(f"Could not calculate daily rate for {role} L{level}: {e}")
        return 0

def get_hourly_rate(role: str, level: int, model: str = "fulltime") -> float:
    """Calculates the hourly rate, with an optional premium for freelancers."""
    try:
        daily_rate = get_daily_rate(role, level, model)
        if model == "freelancer":
            return (daily_rate / 8) * (1 + FREELANCE_HOURLY_PREMIUM)
        else:
            return daily_rate / 8
    except (TypeError, ZeroDivisionError) as e:
        logger.error(f"Could not calculate hourly rate for {role} L{level}: {e}")
        return 0

def get_internal_cost(role: str, level: int) -> float:
    """Gets the total internal monthly cost for an employee."""
    breakdown = get_cost_breakdown(role, level)
    return breakdown.get("biaya_personil_internal", 0)

def get_internal_daily_rate(role: str, level: int) -> float:
    """Calculates the internal daily cost rate."""
    try:
        monthly_rate = get_internal_cost(role, level)
        return monthly_rate / 22
    except (TypeError, ZeroDivisionError) as e:
        logger.error(f"Could not calculate internal daily rate for {role} L{level}: {e}")
        return 0

# ============================================================
# MODEL 2: Headcount-Based (Government Proposal) — LEGACY
# DEPRECATED: Use Model 4 (calculate_gov_proposal_flexible) for new proposals.
# Retained for backward compatibility with existing legacy proposals only.
# ============================================================

def calculate_gov_proposal_pricing(
    headcount: int,
    months: int,
    flat_rate: float = GOV_FLAT_RATE_PER_PERSON_PER_MONTH,
    operational_ratio: float = GOV_OPERATIONAL_RATIO,
    risk_rate: float = GOV_RISK_MANAGEMENT_RATE,
    custom_operational: Optional[float] = None,
) -> Dict[str, Any]:
    """
    DEPRECATED: Use calculate_gov_proposal_flexible() for new proposals.
    
    Calculate government proposal pricing using a headcount-based flat rate model.
    This function uses a fixed rate per person per month regardless of competency.
    It is retained ONLY for backward compatibility with legacy proposals.
    
    Based on real POLRI proposal structure:
      A. Personnel = headcount × months × flat_rate
      B. Operational = operational_ratio × A (or custom amount)
      C. Risk Management = risk_rate × (A + B)
      D. Total = A + B + C

    Args:
        headcount: The number of personnel.
        months: The duration of the project in months.
        flat_rate: The blended rate per person per month.
        operational_ratio: The ratio of operational costs to personnel costs.
        risk_rate: The risk management surcharge.
        custom_operational: A fixed amount for operational costs, overriding the ratio-based calculation.

    Returns:
        A dictionary with the detailed government proposal pricing breakdown.
    """
    if not all(isinstance(i, (int, float)) and i >= 0 for i in [headcount, months, flat_rate, operational_ratio, risk_rate]):
        logger.error("Invalid input for government proposal pricing. All inputs must be non-negative numbers.")
        return {'error': "Invalid input. Headcount, months, and rates must be non-negative numbers."}

    try:
        personnel = headcount * months * flat_rate
        
        if custom_operational is not None:
            if not isinstance(custom_operational, (int, float)) or custom_operational < 0:
                logger.error(f"Custom operational cost must be a non-negative number, but got {custom_operational}")
                return {'error': "Custom operational cost must be a non-negative number."}
            operational = custom_operational
        else:
            operational = personnel * operational_ratio
        
        risk_management = (personnel + operational) * risk_rate
        total = personnel + operational + risk_management
        
        return {
            "model": "headcount_government",
            "headcount": headcount,
            "months": months,
            "flat_rate_per_person_per_month": flat_rate,
            "a_personnel": personnel,
            "b_operational": operational,
            "c_risk_management": risk_management,
            "d_total": total,
            "operational_ratio": operational / personnel if personnel > 0 else 0,
            "risk_rate": risk_rate,
        }
    except Exception as e:
        logger.exception(f"An unexpected error occurred in calculate_gov_proposal_pricing: {e}")
        return {'error': "An unexpected error occurred during government pricing calculation."}

def format_gov_pricing_table(pricing: Dict[str, Any]) -> str:
    """
    Formats government pricing calculation results into a human-readable string table.

    Args:
        pricing: The dictionary output from calculate_gov_proposal_pricing.

    Returns:
        A formatted string representing the pricing table.
    """
    if "error" in pricing:
        return f"Cannot generate table due to error: {pricing['error']}"
    try:
        lines = []
        lines.append(f"{ 'Item':<60} {'Biaya':>20}")
        lines.append("-" * 82)
        flat_str = f"{pricing['flat_rate_per_person_per_month']:,.0f}"
        label_a = f"A. Tenaga Ahli ({pricing['headcount']} Orang x {pricing['months']} Bulan x Rp {flat_str})"
        risk_pct = f"{pricing['risk_rate']*100:.0f}"
        label_c = f"C. Manajemen Risiko ({risk_pct}%)"
        lines.append(f"{label_a:<60} Rp {pricing['a_personnel']:>17,.0f}")
        lines.append(f"{'B. Biaya Operasional (Transportasi, Akomodasi, Konsumsi)':<60} Rp {pricing['b_operational']:>17,.0f}")
        lines.append(f"{label_c:<60} Rp {pricing['c_risk_management']:>17,.0f}")
        lines.append("-" * 82)
        lines.append(f"{'D. TOTAL ANGGARAN':<60} Rp {pricing['d_total']:>17,.0f}")
        return "\n".join(lines)
    except (KeyError, TypeError) as e:
        logger.error(f"Failed to format government pricing table due to missing or invalid key: {e}")
        return "Error: Could not format pricing table due to incomplete data."

# ============================================================
# MODEL 3: Lump Sum (Enterprise/BUMN Pitch)
# ============================================================

def calculate_lumpsum_pricing(
    working_days: int,
    daily_rate: Optional[float] = None,
    total_price: Optional[float] = None,
    include_tax: bool = False,
    tax_rate: float = 0.11,
    scope_label: str = "Advisory & Governance",
) -> Dict[str, Any]:
    """
    Calculate lump sum pricing for enterprise/BUMN pitches.
    
    Provide either daily_rate (to calculate total) or total_price (to calculate daily_rate).
    
    Based on real SID and KAI pitch structures:
      - SID: Rp 170,000,000 / ±44 hari kerja (sudah termasuk pajak)
      - KAI: Rp 575,250,000 / ±132 hari kerja (belum termasuk pajak)

    Args:
        working_days: The estimated number of working days for the project.
        daily_rate: The daily rate for the project team.
        total_price: The total fixed price for the project.
        include_tax: Whether the provided total_price includes tax.
        tax_rate: The applicable tax rate (e.g., PPN).
        scope_label: A brief description of the project scope.

    Returns:
        A dictionary with the detailed lump sum pricing breakdown.
    """
    if not ((daily_rate is not None) ^ (total_price is not None)):
        logger.error("Invalid input for lumpsum pricing. Provide either daily_rate OR total_price, not both or neither.")
        return {'error': "Provide either daily_rate or total_price, but not both."}

    try:
        price_before_tax: float
        effective_daily_rate: float

        if total_price is not None:
            if not isinstance(total_price, (int, float)) or total_price < 0:
                 return {'error': "Total price must be a non-negative number."}
            price_before_tax = total_price / (1 + tax_rate) if include_tax else total_price
            if working_days <= 0:
                return {'error': "Working days must be positive."}
            effective_daily_rate = price_before_tax / working_days
        elif daily_rate is not None:
            if not isinstance(daily_rate, (int, float)) or daily_rate < 0:
                 return {'error': "Daily rate must be a non-negative number."}
            price_before_tax = daily_rate * working_days
            effective_daily_rate = daily_rate
        
        tax_amount = price_before_tax * tax_rate
        price_after_tax = price_before_tax + tax_amount
        quoted_price = price_after_tax if include_tax else price_before_tax

        return {
            "model": "lumpsum_enterprise",
            "working_days": working_days,
            "effective_daily_rate": effective_daily_rate,
            "price_before_tax": price_before_tax,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "price_after_tax": price_after_tax,
            "include_tax_in_quote": include_tax,
            "quoted_price": quoted_price,
            "tax_status": "Sudah termasuk pajak" if include_tax else "Belum termasuk pajak",
            "scope_label": scope_label,
        }
    except (ZeroDivisionError, TypeError) as e:
        logger.exception(f"An error occurred during lumpsum calculation: {e}")
        return {'error': f"Calculation error: {e}"}

def format_lumpsum_card(pricing: Dict[str, Any]) -> str:
    """
    Formats lump sum pricing into a pitch-style card.

    Args:
        pricing: The dictionary output from calculate_lumpsum_pricing.

    Returns:
        A formatted string representing the pricing card.
    """
    if "error" in pricing:
        return f"Cannot generate card due to error: {pricing['error']}"
    try:
        lines = []
        lines.append("=" * 50)
        lines.append(f"  Rp {pricing['quoted_price']:,.0f}")
        lines.append(f"  ({pricing['tax_status']})")
        lines.append("")
        lines.append(f"  ±{pricing['working_days']} hari kerja")
        lines.append("")
        lines.append(f"  {pricing['scope_label']}")
        lines.append("=" * 50)
        return "\n".join(lines)
    except (KeyError, TypeError) as e:
        logger.error(f"Failed to format lumpsum card due to missing or invalid key: {e}")
        return "Error: Could not format pricing card due to incomplete data."

# ============================================================
# MODEL 4: Flexible Competency-Based (RECOMMENDED)
# ============================================================
# This model replaces the fixed Rp 20M/person/month approach.
# Each team member is priced individually based on their role,
# education tier (SMK/D3/S1/S2/S3), and years of experience.
# Source: SALARY_MASTER from DataMasterSalaryRate2026.xlsx
# ============================================================

def calculate_gov_proposal_flexible(
    team_members: list,
    months: int,
    operational_ratio: float = GOV_OPERATIONAL_RATIO,
    risk_rate: float = GOV_RISK_MANAGEMENT_RATE,
    custom_operational: Optional[float] = None,
    pricing_field: str = "external_margin30",
) -> Dict[str, Any]:
    """
    Calculate government proposal pricing using the flexible competency-based model.

    This is the RECOMMENDED replacement for calculate_gov_proposal_pricing().
    Instead of a fixed flat rate per person, each team member is priced individually
    based on their role, education, and years of experience.

    For urgent/large-scale projects requiring senior expertise, specify team members
    with higher education and more years of experience to automatically select
    higher-level (and higher-cost) personnel.

    For smaller/routine projects, specify junior team members with fewer years
    of experience to optimize costs.

    Args:
        team_members: List of dicts, each with keys:
            - "role": str (must exist in SALARY_MASTER)
            - "education": str (SMK/D3/S1/S2/S3)
            - "years_experience": float
        months: Project duration in months.
        operational_ratio: Operational cost ratio (default 22.5%).
        risk_rate: Risk management surcharge (default 10%).
        custom_operational: Fixed operational cost (overrides ratio).
        pricing_field: Cost field from SALARY_MASTER (default "external_margin30").

    Returns:
        A dictionary with the full government proposal pricing breakdown.

    Example:
        >>> team = [
        ...     {"role": "Data Governance Lead", "education": "S2", "years_experience": 8},
        ...     {"role": "Data Analyst", "education": "S1", "years_experience": 3},
        ...     {"role": "Data Engineer", "education": "S1", "years_experience": 5},
        ... ]
        >>> result = calculate_gov_proposal_flexible(team, months=6)
    """
    if not team_members:
        return {'error': 'team_members cannot be empty'}
    if months <= 0:
        return {'error': 'months must be positive'}

    try:
        team_result = calculate_team_cost_flexible(team_members, months, pricing_field)
        personnel = team_result['total_personnel_cost']

        if custom_operational is not None:
            operational = custom_operational
        else:
            operational = personnel * operational_ratio

        risk_management = (personnel + operational) * risk_rate
        total = personnel + operational + risk_management

        return {
            "model": "flexible_competency_government",
            "team_size": len(team_members),
            "months": months,
            "pricing_field": pricing_field,
            "member_breakdowns": team_result['member_breakdowns'],
            "a_personnel": personnel,
            "average_monthly_rate_per_person": team_result['average_monthly_rate'],
            "b_operational": operational,
            "c_risk_management": risk_management,
            "d_total": total,
            "operational_ratio": operational / personnel if personnel > 0 else 0,
            "risk_rate": risk_rate,
        }
    except Exception as e:
        logger.exception(f"Error in calculate_gov_proposal_flexible: {e}")
        return {'error': f'Calculation error: {e}'}


def format_flexible_pricing_table(pricing: Dict[str, Any]) -> str:
    """
    Format flexible government pricing into a human-readable table.

    Shows individual team member costs and the full A/B/C/D breakdown.

    Args:
        pricing: Output from calculate_gov_proposal_flexible().

    Returns:
        A formatted string table.
    """
    if 'error' in pricing:
        return f"Error: {pricing['error']}"

    try:
        lines = []
        lines.append(f"{'='*100}")
        lines.append(f"  MODEL 4: FLEXIBLE COMPETENCY-BASED GOVERNMENT PROPOSAL")
        lines.append(f"  Team: {pricing['team_size']} members | Duration: {pricing['months']} months")
        lines.append(f"{'='*100}")
        lines.append(f"")
        mo = pricing['months']
        lines.append(f"  {'No':<4} {'Role':<35} {'Edu':<5} {'Exp':<5} {'Lvl':<5} {'Monthly Rate':>18} {f'Total ({mo}mo)':>18}")
        lines.append(f"  {'-'*90}")

        for i, m in enumerate(pricing['member_breakdowns'], 1):
            lines.append(
                f"  {i:<4} {m['role']:<35} {m['education']:<5} {m['years_experience']:<5.0f} "
                f"L{m['matched_level']:<4} Rp {m['monthly_rate']:>14,.0f} Rp {m['total_cost']:>14,.0f}"
            )

        lines.append(f"  {'-'*90}")
        lines.append(f"")
        lines.append(f"  {'A. Biaya Personil (Tenaga Ahli)':<60} Rp {pricing['a_personnel']:>17,.0f}")
        lines.append(f"  {'   Rata-rata per orang per bulan':<60} Rp {pricing['average_monthly_rate_per_person']:>17,.0f}")
        lines.append(f"  {'B. Biaya Operasional':<60} Rp {pricing['b_operational']:>17,.0f}")
        risk_pct = int(pricing['risk_rate'] * 100)
        lines.append(f"  {f'C. Manajemen Risiko ({risk_pct}%)':<60} Rp {pricing['c_risk_management']:>17,.0f}")
        lines.append(f"  {'='*80}")
        lines.append(f"  {'D. TOTAL ANGGARAN':<60} Rp {pricing['d_total']:>17,.0f}")
        lines.append(f"  {'='*80}")

        return "\n".join(lines)
    except (KeyError, TypeError) as e:
        logger.error(f"Failed to format flexible pricing table: {e}")
        return f"Error formatting table: {e}"


# ============================================================
# USAGE EXAMPLE
# ============================================================

if __name__ == '__main__':
    # This block demonstrates how to use the pricing engine functions.
    # It is executed only when the script is run directly.

    print("="*80)
    print(" MODEL 1: MAN-DAY/MONTHLY (INTERNAL COGS) EXAMPLE")
    print("="*80)
    
    role_example = "Data Scientist"
    level_example = 10
    cost_breakdown = get_cost_breakdown(role_example, level_example)
    
    if "error" in cost_breakdown:
        print(f"Error calculating cost for {role_example} L{level_example}: {cost_breakdown['error']})")
    else:
        print(f"Cost Breakdown for: {role_example} (Level {level_example})")
        for key, value in cost_breakdown.items():
            if isinstance(value, (int, float)):
                print(f"  {key:<30}: Rp {value:,.0f}")
            else:
                print(f"  {key:<30}: {value}")
        print("-" * 40)
        print(f"External Daily Rate (Full-time): Rp {get_daily_rate(role_example, level_example):,.0f}")
        print(f"External Daily Rate (Freelance): Rp {get_daily_rate(role_example, level_example, model='freelancer'):,.0f}")
        print(f"Internal Cost (Monthly):         Rp {get_internal_cost(role_example, level_example):,.0f}")

    print("\n" + "="*80)
    print(" MODEL 2: HEADCOUNT-BASED (GOVERNMENT PROPOSAL) — LEGACY/DEPRECATED")
    print("="*80)
    print("NOTE: This model uses a fixed Rp 20M/person/month. Use Model 4 for new proposals.")

    gov_pricing = calculate_gov_proposal_pricing(headcount=5, months=6)
    print(format_gov_pricing_table(gov_pricing))

    print("\n" + "="*80)
    print(" MODEL 3: LUMP SUM (ENTERPRISE/BUMN PITCH) EXAMPLE")
    print("="*80)

    # Example 1: Calculate total from daily rate (KAI style)
    lumpsum_pricing_1 = calculate_lumpsum_pricing(
        working_days=132,
        daily_rate=4358000, # Derived from 575,250,000 / 132
        include_tax=False,
        scope_label="End-to-End Data Strategy & Governance"
    )
    print("--- Example based on KAI (Price from Daily Rate) ---")
    print(format_lumpsum_card(lumpsum_pricing_1))

    # Example 2: Calculate daily rate from total price (SID style)
    lumpsum_pricing_2 = calculate_lumpsum_pricing(
        working_days=44,
        total_price=170000000,
        include_tax=True,
        scope_label="Data Governance Advisory"
    )
    print("\n--- Example based on SID (Rate from Total Price) ---")
    print(format_lumpsum_card(lumpsum_pricing_2))
    if "error" not in lumpsum_pricing_2:
      print(f"Effective Daily Rate: Rp {lumpsum_pricing_2['effective_daily_rate']:,.0f}")

    print("\n" + "="*80)
    print(" MODEL 4: FLEXIBLE COMPETENCY-BASED (RECOMMENDED)")
    print("="*80)
    print("This model prices each team member individually based on competency.")
    print("Senior experts (more experience, higher education) cost more.")
    print("Junior staff (less experience) cost less. No more fixed Rp 20M/person.\n")

    # Example: Government data governance project team
    team_example = [
        {"role": "Data Governance Lead", "education": "S2", "years_experience": 8},
        {"role": "Data Analyst", "education": "S1", "years_experience": 3},
        {"role": "Data Engineer", "education": "S1", "years_experience": 5},
        {"role": "Data Quality Analyst", "education": "S1", "years_experience": 4},
        {"role": "Project Manager", "education": "S2", "years_experience": 10},
    ]
    flexible_pricing = calculate_gov_proposal_flexible(team_example, months=6)
    print(format_flexible_pricing_table(flexible_pricing))

    # Compare with legacy model
    print("\n--- COMPARISON: Legacy vs Flexible ---")
    legacy = calculate_gov_proposal_pricing(headcount=5, months=6)
    print(f"Legacy (5 × 6 × Rp 20M):  Rp {legacy['d_total']:>17,.0f}")
    print(f"Flexible (competency):     Rp {flexible_pricing['d_total']:>17,.0f}")
    diff = flexible_pricing['d_total'] - legacy['d_total']
    pct = (diff / legacy['d_total']) * 100
    print(f"Difference:                Rp {diff:>17,.0f} ({pct:+.1f}%)")
    print(f"\nThe flexible model provides more accurate pricing based on actual competency.")


# ============================================================================
# ROLE-SERVICE MAPPING HELPERS
# ============================================================================

def get_role_services(role_name: str) -> list:
    """Return the list of service IDs where a role is assigned.
    
    Args:
        role_name: The exact role name as defined in RATE_CARD.
        
    Returns:
        List of service IDs (e.g., ["S1.1", "S1.2", "S2.3"]).
        Empty list if role has no assignments or is not found.
    """
    return ROLE_SERVICE_MAP.get(role_name, [])

def get_service_roles(service_id: str) -> list:
    """Return all roles assigned to a specific service.
    
    Args:
        service_id: The service ID (e.g., "S1.1", "S2.3").
        
    Returns:
        Sorted list of role names assigned to that service.
    """
    return sorted([
        role for role, services in ROLE_SERVICE_MAP.items()
        if service_id in services
    ])

def get_role_utilization_summary() -> dict:
    """Return a summary of role utilization across services.
    
    Returns:
        Dict with keys:
        - total_roles: Total number of roles
        - assigned_roles: Number of roles with at least one service assignment
        - unassigned_roles: Number of roles with no service assignments
        - avg_services_per_role: Average number of services per assigned role
        - most_utilized: Top 5 most-utilized roles
        - least_utilized: Roles with only 1 service assignment
    """
    assigned = {r: s for r, s in ROLE_SERVICE_MAP.items() if s}
    unassigned = {r: s for r, s in ROLE_SERVICE_MAP.items() if not s}
    
    avg = sum(len(s) for s in assigned.values()) / len(assigned) if assigned else 0
    
    most_utilized = sorted(assigned.items(), key=lambda x: -len(x[1]))[:5]
    least_utilized = sorted([r for r, s in assigned.items() if len(s) == 1])
    
    return {
        "total_roles": len(ROLE_SERVICE_MAP),
        "assigned_roles": len(assigned),
        "unassigned_roles": len(unassigned),
        "unassigned_role_names": sorted(unassigned.keys()),
        "avg_services_per_role": round(avg, 1),
        "most_utilized": [(r, len(s), s) for r, s in most_utilized],
        "least_utilized": least_utilized,
    }
