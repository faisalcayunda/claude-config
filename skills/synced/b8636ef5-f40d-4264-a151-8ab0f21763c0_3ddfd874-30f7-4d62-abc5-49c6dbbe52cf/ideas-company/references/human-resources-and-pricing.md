# Human Resources & Pricing Framework (2026) - DAMA Enriched

**Version**: 4.0 | **Last Updated**: February 21, 2026

---

## Table of Contents

1. [The Unified Pricing Engine](#1-the-unified-pricing-engine)
2. [DAMA Role Enrichment Strategy](#2-dama-role-enrichment-strategy)
3. [Cost Component Breakdown](#3-cost-component-breakdown)
4. [Pricing Tiers: Full-Time vs. Freelance](#4-pricing-tiers-full-time-vs-freelance)
5. [How to Use the Calculation Scripts](#5-how-to-use-the-calculation-scripts)
6. [Indonesian Data Management Professional Salary Benchmarks (2026)](#6-indonesian-data-management-professional-salary-benchmarks-2026)
7. [GenAI & AI Specialist Roles (2026-2027 Emerging)](#7-genai--ai-specialist-roles-2026-2027-emerging)
8. [Value-Based Pricing Principles](#8-value-based-pricing-principles)
9. [Glossary of Terms](#9-glossary-of-terms)

---

## 1. The Unified Pricing Engine

All financial calculations in this skill are centralized in the **Unified Pricing Engine** (`scripts/pricing_engine.py`). This module is the single source of truth and contains:

- **Constants**: UMK 2026 (Rp 4,737,678), BPJS rates (individu & perusahaan), margin (30%), freelance premiums.
- **`GROWTH_TABLE`**: 24-level growth multiplier from -20% (L1) to +370% (L24), with Level 5 as baseline (0%).
- **`RATE_CARD`**: Master list of **141 roles** (fully integrated) with their tunjangan structures.
- **`TYPICAL_TEAMS`**: Pre-defined team compositions for major services. See example below.

- **`SALARY_MASTER`** *(NEW in v7.0)*: Comprehensive competency-based salary data sourced from `DataMasterSalaryRate2026.xlsx`. Contains **141 roles × 24 levels** with a full cost breakdown for each education tier (SMK/D3/S1/S2/S3). This replaces the fixed Rp 20M/person/month government model with flexible, competency-driven pricing.

It exposes the following functions used by all other scripts:

| Function | Returns | Use Case |
| :--- | :--- | :--- |
| `get_cost_breakdown(role, level)` | Full 9-component cost structure | Detailed analysis |
| `get_external_price(role, level)` | Final client price (Man-Month) | RAB/COGS pricing |
| `get_freelancer_price(role, level)` | Gross salary (Man-Month) | Internal/freelance |
| `get_daily_rate(role, level, model)` | Daily rate | Short-term engagements |
| `get_hourly_rate(role, level, model)` | Hourly rate | Consulting/advisory |
| `get_flexible_personnel_cost(role, edu, exp, months)` | Competency-based cost | **Model 4 flexible pricing** |
| `calculate_team_flexible_cost(team_members, months)` | Team total cost | **Model 4 team pricing** |

> **Model 4 (RECOMMENDED)**: For all new government and enterprise proposals, use `calculate_gov_proposal_flexible()` in `pricing_engine.py` instead of the legacy `calculate_gov_proposal_pricing()`. The flexible model prices each team member individually based on their role, education tier, and years of experience. Senior experts (S2/S3, ≥8yr) cost more; junior staff (S1/D3, ≤3yr) cost less. This provides more accurate and competitive pricing.

### Example `TYPICAL_TEAMS` Composition

To illustrate how team compositions are defined, here is an example for the **Data Governance Quickstart** service (S1.2):

```python
'S1.2': {
    'team': [
        {'role': 'Data Valuation Specialist', 'level': 18, 'fte': 0.25},
        {'role': 'Data Governance Lead', 'level': 16, 'fte': 0.5},
        {'role': 'Data Governance Analyst', 'level': 12, 'fte': 1.0},
        {'role': 'Business Analyst (Data)', 'level': 10, 'fte': 1.0}
    ],
    'duration_months': 3
},
```

> **Cross-Reference:** For a complete list of services and their descriptions, see `references/services-catalog.md`.

## 2. Role Taxonomy and Structure

The pricing engine now includes a comprehensive and unified taxonomy of **141 roles**. This taxonomy integrates the original IDEAS roles with an extensive set of roles derived from the DAMA-DMBOK framework and modern data team structures. All roles are now first-class citizens within the pricing engine, with their salary and cost structures directly defined in the `SALARY_MASTER` dictionary in `rate_card.py`. The previous responsibility-based mapping for DAMA roles is now deprecated, as each role has its own complete and independent pricing data.

### Role Distribution Summary

| Group | Count | Description |
| :--- | :--- | :--- |
| **Board** | 14 | IDEAS C-Level and Heads of Function |
| **Biz&Digital** | 9 | IDEAS Business, Project Management, and Content |
| **PDT** | 118 | IDEAS Product, Data, and Technology Roles |

| **Total** | **141** | |

### All Roles by Category

| Category | Count | Example Roles |
| :--- | :--- | :--- |
| **Management** | 14 | Chief Data Officer (CDO), Head of Product, Head of PMO |
| **Managerial** | 16 | Data Governance Manager, Product Manager, MLOps Manager |
| **Lead** | 40 | Data Valuation Specialist, Data Owner, Data Protection Officer (DPO) |
| **Analyst** | 45 | Data Analyst, Business Analyst (Data), Data Modeler |
| **Engineer** | 11 | Data Engineer, Machine Learning Engineer, Security Engineer |
| **Officer** | 15 | Data Steward, Data Custodian, Project Management Officer |

> **Cross-Reference:** For a complete definition of all 141 roles, including summaries, key responsibilities, and DDaT-aligned skills, see the new `references/role-definitions.md` document.

### Role-Specific Salary Multiplier (ROLE_MULTIPLIER)

Since v5.9, a **ROLE_MULTIPLIER** dictionary in `scripts/rate_card.py` applies market-based salary differentials to each role. This ensures that high-demand, scarce roles (e.g., GenAI Specialist, AI/ML Research Scientist) command higher rates than commodity roles within the same salary category.

| Multiplier Range | Description | Example Roles |
| :--- | :--- | :--- |
| **0.95–0.99** | Commodity roles (high supply, lower specialization) | Content Officer (Writer), Data Custodian |
| **1.00** | Standard baseline for the category | Data Analyst, Data Steward, Account Manager |
| **1.01–1.09** | Moderate specialization premium | Data Modeler, Project Manager, Business Analyst |
| **1.10–1.15** | High-demand specialization | Data Architect, Security Engineer, SRE |
| **1.16–1.22** | Scarce/cutting-edge roles | GenAI Specialist (1.22), AI/ML Research Scientist (1.22), Machine Learning Engineer (1.20) |

The multiplier is applied in `pricing_engine.py`'s `get_cost_breakdown()` function to adjust `gaji_pokok` and `tunjangan` before all downstream calculations (BPJS, PPh21, margin).

### Certification & Standards Context (2026)

| Standard | Relevance | Impact on Pricing |
| :--- | :--- | :--- |
| **BNSP SKM-LSPTD-002** | Indonesian national competency standard for data management. | Certified roles may command a 10-15% premium. |
| **PMK 32/2025** | Standar Biaya Masukan (SBM) TA 2026, sets maximum government consultant rates. | Aligns government project pricing with the national standard ceiling. |
| **Perpres 46/2025** | Second amendment to Perpres 16/2018 on Government Procurement. | Reinforces mandatory e-Katalog use and introduces new procurement methods. |
| **PP 49/2025** | Government regulation on **Wages**, not procurement. Amends PP 36/2021. | Defines the new minimum wage formula, impacting the UMK baseline. |
| **SKKNI Data Management** | National competency framework. | Basis for BNSP certification curriculum and exam content. |
| **DAMA-DMBOK 3.0** | Next-gen global standard (project kicked off June 25, 2025). | Incorporates AI, cloud, and modern platforms. In development, expected Q2 2027. |

> **CDO Landscape (2026):** 51% of CDOs cite Data Governance as top priority; 87% report to C-Suite; 54% grew teams last year. This validates the demand for IDEAS's data management consulting roles.

## 3. Cost Component Breakdown

The pricing model is built from the ground up, starting with Gaji Pokok and layering on costs and margins. The `pricing_engine.get_cost_breakdown()` function automates this entire flow.

| # | Component | Formula / Derivation | Owner |
| :-: | :--- | :--- | :--- |
| 1 | **Gaji Pokok** | `UMK * (1 + Growth)` | - |
| 2 | **Tunjangan Tetap** | `Tunjangan Jabatan + Tunjangan Keahlian` | Perusahaan |
| 3 | **Tunjangan Tidak Tetap** | `Tunjangan Harian` | Perusahaan |
| 4 | **Gaji Kotor (Freelancer Rate)** | `(1) + (2) + (3)` | - |
| 5 | **Potongan Individu** | BPJS Individu (4%) + PPh 21 (progresif) | Individu |
| 6 | **Take Home Pay (THP)** | `(4) - (5)` | Individu |
| 7 | **Beban Perusahaan** | BPJS Perusahaan (11.74%) | Perusahaan |
| 8 | **Biaya Personil Internal** | `(4) + (7) - (5)` | Perusahaan |
| 9 | **Harga Eksternal (Client Price)** | `(8) * 1.3` (margin 30%) | Eksternal |

**Note on PPh 21:** The PPh 21 (income tax) is calculated using a progressive tariff based on annual income brackets as defined by Indonesian tax law. The engine approximates this calculation for monthly costing.

## 4. Pricing Tiers: Full-Time vs. Freelance

The engine supports two pricing models:

| Model | Calculation | Use Case |
| :--- | :--- | :--- |
| **Full-Time (External)** | `Biaya Personil Internal * 1.3` | Default for RAB/COGS client pricing |
| **Freelancer** | `Gaji Kotor` (no BPJS, no margin) | Internal projects, short-term contractors |

Daily and hourly rates are derived from monthly rates:

| Unit | Full-Time | Freelancer |
| :--- | :--- | :--- |
| **Daily** | `External Price / 22` | `Gross / 22 * 1.10` (10% premium) |
| **Hourly** | `Daily / 8` | `Daily / 8 * 1.30` (30% premium) |

## 5. How to Use the Calculation Scripts

### `calculate_project_cost.py` (CLI for the Engine)

```bash
# Standard external price for a DAMA role
python3 scripts/calculate_project_cost.py --role "Data Steward" --level 8 --duration 6

# Daily freelancer rate
python3 scripts/calculate_project_cost.py --role "Database Administrator (DBA)" --level 10 --unit day --model freelancer

# Full cost breakdown
python3 scripts/calculate_project_cost.py --role "Chief Data Officer (CDO)" --level 20 --breakdown

# List all available roles (filter by group)
python3 scripts/calculate_project_cost.py --list-roles --group DAMA
```

### `generate_cogs.py` (People Cost for COGS)

```bash
# Generate COGS with DAMA roles
python3 scripts/generate_cogs.py --input feature_allocation.json
```

### `recommend_service.py` (with Cost Estimates)

```bash
# Get recommendations with estimated costs
python3 scripts/recommend_service.py --need "kami butuh data governance"
```

---

## 6. Indonesian Data Management Professional Salary Benchmarks (2026)

> **Note:** Salary benchmarks have been updated to reflect the 2026 market perspective. The INKINDO 2026 *Pedoman Standar Minimal* is now available and has been factored into our pricing structure for engineering and technical consulting roles, ensuring our rates are competitive and aligned with the latest industry standards for professional services in Indonesia.

Pemetaan role DAMA standar ke pasar tenaga kerja IT Indonesia, dengan benchmark gaji dan ketersediaan talent:

### Role Mapping: DAMA Standard → Indonesian Market

| DAMA Standard Role | Indonesian Market Equivalent | Availability | Salary Range (Monthly) |
| :--- | :--- | :--- | :--- |
| Chief Data Officer (CDO) | Head of Data / VP Data | Sangat Langka | Rp 80-150 juta |
| Data Governance Manager | Data Governance Lead | Langka | Rp 40-70 juta |
| Data Architect | Data Architect / Solution Architect | Terbatas | Rp 35-60 juta |
| Data Steward | Data Analyst Senior / Data Coordinator | Moderat | Rp 15-30 juta |
| Data Quality Analyst | QA Data / Data Analyst | Moderat | Rp 12-25 juta |
| Metadata Specialist | Data Catalog Engineer | Sangat Langka | Rp 20-40 juta |
| Data Security Officer | IT Security / DPO | Terbatas | Rp 30-50 juta |
| Data Integration Specialist | ETL Developer / Data Engineer | Moderat | Rp 18-35 juta |

### Implikasi untuk Pricing IDEAS

1. **Premium Positioning:** Role langka (CDO, Metadata Specialist) membenarkan premium rate IDEAS karena klien sulit merekrut sendiri.
2. **BNSP Certification Value:** Sertifikasi BNSP (Data Scientist, BI Analyst, Assessor) menambah kredibilitas dan membenarkan rate lebih tinggi.
3. **DGO as a Service Justification:** Kelangkaan CDO/DG Manager di pasar Indonesia menjadi justifikasi utama layanan S3.1 (DGO as a Service).
4. **PMK 32/2025 Alignment:** Rate card harus disesuaikan dengan SBM (Standar Biaya Masukan) untuk proyek pemerintah.

> **Cross-Reference:** Untuk definisi lengkap setiap role DAMA, lihat skill `dama-research` (reference/role-definitions.md). Untuk benchmark industri, lihat `references/competitive-landscape.md`.

---

## 7. GenAI & AI Specialist Roles (2026-2027 Emerging)

Role baru yang dibutuhkan untuk mendukung layanan AI governance dan GenAI readiness:

| Role | Responsibility | Salary Range (Monthly) | Availability |
| :--- | :--- | :--- | :--- |
| AI/ML Engineer | Model development, MLOps, deployment | Rp 25-50 juta | Terbatas |
| GenAI Specialist | LLM fine-tuning, prompt engineering, RAG | Rp 30-60 juta | Sangat Langka |
| AI Ethics Officer | Responsible AI policy, bias audit, FATE | Rp 35-55 juta | Sangat Langka |
| AI Governance Analyst | NIST AI RMF, ISO 42001 compliance | Rp 25-45 juta | Langka |
| Data Contract Engineer | ODCS implementation, schema validation | Rp 20-40 juta | Langka |

**Implikasi Pricing:** Kelangkaan talent GenAI/AI di Indonesia membenarkan premium rate 20-40% di atas role data management tradisional. IDEAS dapat memanfaatkan keahlian internal untuk menawarkan layanan AI governance yang sulit ditemukan di pasar.

## 8. Value-Based Pricing Principles

Selain cost-plus pricing (Man-Month/Man-Day), IDEAS dapat menerapkan **value-based pricing** untuk engagement tertentu. This is especially relevant for services where value is directly quantifiable, such as data asset valuation, drawing on frameworks like the Deloitte 2025 model.

| Pricing Model | Applicable Service | Basis |
| :--- | :--- | :--- |
| **Outcome-Based** | S1.5 Data Asset Valuation | Persentase dari nilai data asset yang teridentifikasi (Income/Cost/Market Approach). |
| **Success Fee** | S1.1 Data Strategy | Bonus jika target maturity level tercapai. |
| **Subscription** | S3.1 DGO as a Service | Monthly retainer dengan SLA terukur. |
| **Tiered Licensing** | S2.x Platform Services | Per-user/per-domain pricing. |

**Prinsip Utama:** Harga layanan harus mencerminkan **10:1 value ratio** — klien harus menerima minimal 10x nilai dari biaya yang dikeluarkan. Ini diukur melalui cost savings, revenue enablement, risk reduction, or compliance achievement.

> **Cross-Reference:** Untuk detail pricing strategy frameworks, lihat `references/business-frameworks.md`. Untuk COGS calculation, lihat `references/cogs-methodology.md`.

---

## 9. Glossary of Terms

| Term | Definition |
| :--- | :--- |
| **UMK** | Upah Minimum Kota/Kabupaten (Regional Minimum Wage). The baseline for salary calculations. |
| **BPJS** | Badan Penyelenggara Jaminan Sosial. Indonesia's mandatory social security program, covering health and employment. |
| **PPh 21** | Pajak Penghasilan Pasal 21. Employee income tax. |
| **RAB** | Rencana Anggaran Biaya (Cost Budget Plan). |
| **COGS** | Cost of Goods Sold. In this context, the cost of services delivered. |
| **SBM** | Standar Biaya Masukan. Standard cost inputs for government budgeting. |
| **BNSP** | Badan Nasional Sertifikasi Profesi. Indonesia's national professional certification authority. |
| **SKKNI** | Standar Kompetensi Kerja Nasional Indonesia. National work competency standards. |

---

> **Cross-references**: For the complete DAMA role definitions and responsibilities, see skill `dama-research` (reference/role-definitions.md). For the mapping between IDEAS services and DAMA Knowledge Areas, see `references/dama-integration-map.md`.
