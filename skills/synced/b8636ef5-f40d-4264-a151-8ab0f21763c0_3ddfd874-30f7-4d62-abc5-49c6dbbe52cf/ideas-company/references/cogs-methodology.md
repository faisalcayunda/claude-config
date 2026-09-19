# IDEAS COGS Methodology Framework

**Version:** 2.0
**Last Updated:** February 2026

This document outlines the standardized framework for calculating Cost of Goods Sold (COGS)—or Harga Pokok Penjualan (HPP)—for IDEAS' digital product development and platform implementation projects. It integrates best practices from SaaS industry standards, agile development, and Indonesian government procurement regulations, providing a comprehensive methodology for internal cost calculation and project budgeting.

## Table of Contents

1. [Version History](#1-version-history)
2. [Core Principles](#2-core-principles)
3. [COGS Structure: 4 Core Components](#3-cogs-structure-4-core-components)
4. [Visual Calculation Flowchart](#4-visual-calculation-flowchart)
5. [Calculation Formulas](#5-calculation-formulas)
6. [COGS Template Structure (10 Sheets)](#6-cogs-template-structure-10-sheets)
7. [MoSCoW-Driven Scope & Cost Allocation](#7-moscow-driven-scope--cost-allocation)
8. [Squad-Based Team Allocation](#8-squad-based-team-allocation)
9. [Calculation Workflow: A Step-by-Step Guide](#9-calculation-workflow-a-step-by-step-guide)
10. [Worked Example: "Fitur Analisis Prediktif"](#10-worked-example-fitur-analisis-prediktif)
11. [From COGS to Selling Price](#11-from-cogs-to-selling-price)
12. [Industry Benchmarks](#12-industry-benchmarks)
13. [EVM-Based Cost Control (PMBOK Integration)](#13-evm-based-cost-control-pmbok-integration)
14. [Specialized COGS Models](#14-specialized-cogs-models)
15. [Risk Factors in COGS Estimation](#15-risk-factors-in-cogs-estimation)
16. [Templates & Scripts](#16-templates--scripts)
17. [Glossary of Terms](#17-glossary-of-terms)
18. [Related Documents](#18-related-documents)

## 1. Version History

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | Nov 2025 | Manus | Initial draft. |
| 2.0 | Feb 2026 | Manus | Comprehensive update: Added glossary, risk factors, worked example, flowchart, and updated regulatory/framework references (PMK 32/2025, DMBOK 3.0, Deloitte 2025). Fixed all cross-references. |

## 2. Core Principles

- **Product-Centric Costing**: Costs are allocated directly to the products and features being developed.
- **MoSCoW-Driven Scope**: Feature prioritization (Must/Should/Could Have) dictates the scope and budget scenarios.
- **Squad-Based Allocation**: Costs are calculated based on the allocation of agile, cross-functional squads.
- **HPS Alignment**: The structure maps directly to the Harga Perkiraan Sendiri (HPS) format required for Indonesian government proposals.
- **Dual Pricing Track**: Internal cost (COGS/HPP) and the external client price (HPS) are calculated separately to manage profitability.
- **COR Alignment**: For service-based projects, the model aligns with the Cost of Revenue (COR) concept per Indonesian accounting standards, distinguishing direct costs from general operating expenses.

### COGS vs. COR Distinction

For a professional services company like IDEAS, the technically correct accounting term is **Cost of Revenue (COR)**, not COGS. However, we use "COGS" and "HPP" (Harga Pokok Penjualan) interchangeably throughout our documentation for familiarity and alignment with government procurement terminology.

| Component | Included in COR/COGS (Direct Costs) | Excluded from COR/COGS (Operating Expenses) |
| :--- | :--- | :--- |
| Direct labor (project-based) | Yes | |
| Project-specific software/cloud services | Yes | |
| Project-specific hardware | Yes | |
| Project travel & accommodation | Yes | |
| Direct marketing for the project | Yes | |
| Fixed employee salaries (non-project) | | Yes |
| Office rent & utilities | | Yes |
| General & administrative expenses | | Yes |

## 3. COGS Structure: 4 Core Components

This structure is based on the proven model from the POLRI "Satu Data" project and aligns with government budgeting standards.

| # | Component | Description | Typical % of Total COGS |
|:-:|:---|:---|:---|
| 1 | **People (Biaya Tenaga Kerja Langsung)** | Salaries and benefits for personnel directly involved in the project, including dedicated squad members and shared experts/management. Calculated as man-days multiplied by the internal daily rate. | 55-70% |
| 2 | **Software (Biaya Perangkat Lunak)** | Costs for third-party software licenses, cloud services (IaaS/PaaS/SaaS), and specialized AI tools. Includes PPN 11%. | 15-25% |
| 3 | **Hardware (Biaya Perangkat Keras)** | Costs for on-premise servers, networking equipment, GPU servers, storage, UPS, and virtualization software. | 5-15% |
| 4 | **Operational (Biaya Operasional)** | Project-specific operational costs, including transportation, accommodation, co-working space rentals, meals, and stakeholder engagement activities. | 5-10% |

### Master Formula

```
Total COGS = People Cost + Software Cost + Hardware Cost + Operational Cost
```

## 4. Visual Calculation Flowchart

```mermaid
graph TD
    A[Start: Project Brief] --> B{Define Product & Features};
    B --> C{Prioritize Features (MoSCoW)};
    C --> D[Allocate Squads & Roles];
    D --> E[Calculate People Costs];
    C --> F[Estimate Non-People Costs];
    F --> G[Software Costs];
    F --> H[Hardware Costs];
    F --> I[Operational Costs];
    E --> J{Aggregate Total COGS};
    G --> J;
    H --> J;
    I --> J;
    J --> K[Apply Margin & Taxes];
    K --> L[End: Final HPS/RAB];

    subgraph People Cost Calculation
        D1[Define Roles per Feature] --> D2[Estimate Man-Days];
        D2 --> D3{Get Internal Daily Rate};
        D3 --> D4[Cost = Man-Days * Daily Rate];
    end

    E --> D4;
    style J fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#bbf,stroke:#333,stroke-width:2px
```

## 5. Calculation Formulas

### 5.1 People Cost (Biaya Tenaga Kerja Langsung)

This is the largest and most complex component, calculated at the feature level.

```
People Cost per Feature = Σ (Kuantitas_Orang × Waktu_Hari × Biaya_Satuan_Harian)
Biaya_Satuan_Harian = Biaya_Satuan_Bulanan / 22 (working days)
```

The `Biaya_Satuan_Bulanan` is sourced from the `pricing_engine.py` script via the `get_internal_cost()` function, which includes base salary plus all employer-side burdens (BPJS, etc.), reflecting the true internal cost.

### 5.2 Software Cost (Biaya Perangkat Lunak)

```
Software Cost per Item = (Harga_Satuan_USD × Kuantitas × Kurs_USD) + PPN_11%
```
- **Standard Kurs USD**: Rp 17,500 (as of Feb 2026, subject to change).
- **PPN (VAT)**: 11% applied to the DPP (Dasar Pengenaan Pajak).

### 5.3 Hardware Cost (Biaya Perangkat Keras)

```
Hardware Cost per Item = Biaya_Satuan × Kuantitas
```
Prices are sourced from e-Katalog LKPP, official vendor quotes, or market research.

### 5.4 Operational Cost (Biaya Operasional)

```
Operational Cost per Item = Kuantitas_Orang × Waktu_Periode × Biaya_Satuan_Periode
```
Rates are based on the latest **Standar Biaya Masukan (SBM)** from the Ministry of Finance (e.g., PMK 32/2025 for TA 2026) or actual at-cost rates.

## 6. COGS Template Structure (10 Sheets)

The `templates/cogs-template.xlsx` workbook is the primary tool for calculation.

| Sheet | Purpose |
|:---|:---|
| **COGS Total** | Master summary linking Product → Module → Feature with MoSCoW priority and total COGS. |
| **COGS Gabungan** | Consolidated view linking Modul → Fitur → Sub-Fitur to role assignments, man-days, and costs. |
| **People (Summary)** | High-level team structure, showing roles across squads and shared teams. |
| **People (Shared)** | Allocation model for shared resources (e.g., Management, Architects). |
| **People (Assignment)** | Maps specific individuals to roles and squads. |
| **helper** | The master rate card lookup, containing salary levels (Senior/Middle/Junior) for all roles. |
| **Software** | Detailed list of software licenses with pricing, quantity, and tax calculations. |
| **Hardware** | Detailed list of hardware specifications with pricing and e-Katalog references. |
| **Operational** | Breakdown of operational costs based on SBM or at-cost rates. |
| **Biaya Tenaga Kerja Langsung** | The most granular sheet, detailing per-feature role assignments with man-days. |
| **Komponen** | Master list of all features with their MoSCoW classification. |

## 7. MoSCoW-Driven Scope & Cost Allocation

MoSCoW prioritization is fundamental to our scoping and budgeting process.

| Priority | Budget Impact | Decision Rule |
|:---|:---|:---|
| **Must Have** | Forms the baseline budget. Always included. | Non-negotiable; the product is not viable without these features. |
| **Should Have** | Included in the standard project scope if the budget allows. | Important for full functionality, but the product can launch without them. |
| **Could Have** | Included only in the maximum budget scenario. | Nice-to-have features; these are the first to be cut if the budget is constrained. |

## 8. Squad-Based Team Allocation

IDEAS utilizes a scalable, squad-based organizational model for large projects.

| Department | Squad 1 | Squad 2 | Squad 3 | Shared Team | Total |
|:---|:---:|:---:|:---:|:---:|:---:|
| Product Management | 4 | 4 | 4 | 1 | 13 |
| Engineering | 8 | 8 | 7 | 2 | 25 |
| Data Management | 4 | 4 | 6 | 3 | 17 |
| Platform | 1 | 1 | 3 | 1 | 6 |
| Product Delivery | 2 | 2 | 2 | 1 | 7 |
| Communication | 2 | 2 | 0 | 2 | 6 |
| Management | 0 | 0 | 0 | 10 | 10 |
| Administration | 0 | 0 | 0 | 1 | 1 |
| **Total** | **21** | **21** | **22** | **20** | **85** |

## 9. Calculation Workflow: A Step-by-Step Guide

1.  **Define Product & Feature Breakdown**: Decompose the project into a hierarchy: **Product → Module → Feature → Sub-Feature**. Use the `references/products-catalog.md` as a baseline.
2.  **Prioritize Features (MoSCoW)**: Assign a Must, Should, or Could Have priority to each feature in the `Komponen` sheet.
3.  **Allocate Roles & Man-Days**: For each feature, define the required roles and estimate the man-day allocation based on complexity. Reference `references/human-resources-and-pricing.md` for role definitions and `references/role-definitions.md` for DDaT-aligned role descriptions, responsibilities, and skills. Note that `ROLE_MULTIPLIER` in `scripts/rate_card.py` applies market scarcity premiums (0.95–1.22x) to differentiate roles within the same salary category.
4.  **Calculate People Costs**: The `Biaya Tenaga Kerja Langsung` sheet automatically calculates costs by multiplying man-days by the internal daily rates from the `helper` sheet.
5.  **Estimate Other Costs**: Detail all required licenses, hardware, and operational expenses in their respective sheets.
6.  **Aggregate Total COGS**: The `COGS Total` sheet consolidates all costs to provide a final COGS figure, broken down by feature and MoSCoW priority.

## 10. Worked Example: "Fitur Analisis Prediktif"

Let's calculate the People Cost for a single "Could Have" feature.

- **Feature**: Fitur Analisis Prediktif (S2.4)
- **Complexity**: High
- **Estimated Man-Days**: 60 MD total

**Role Allocation:**

| Role | Level | Man-Days | Internal Daily Rate (IDR) | Cost (IDR) |
| :--- | :--- | :--- | :--- | :--- |
| Data Scientist | Senior | 20 | 2,500,000 | 50,000,000 |
| ML Engineer | Middle | 30 | 1,800,000 | 54,000,000 |
| Backend Engineer | Middle | 10 | 1,500,000 | 15,000,000 |
| **Total** | | **60** | | **119,000,000** |

This **Rp 119,000,000** represents the *People Cost* component for this feature. Software costs (e.g., GPU compute, MLOps tools) and shared team costs would be added to determine the total feature COGS.

## 11. From COGS to Selling Price

The path from internal cost (COGS) to the final client price (HPS) involves several markups.

```
COGS (Internal Cost)
  ↓ + Margin (e.g., 30-50%)
  = Harga Dasar (Base Price)
  ↓ + PPh (e.g., 2% Withholding Tax, if applicable)
  = Harga Satuan Internal
  ↓ + PPN (11% VAT)
  = Harga Satuan Eksternal (Final Client Price)
```

For a complete breakdown of this process, see the `references/rab-hps-methodology.md` document.

## 12. Industry Benchmarks

### SaaS & Professional Services COGS Benchmarks (2026)

| Metric | SaaS Industry | IT Consulting | IDEAS Target |
| :--- | :--- | :--- | :--- |
| COGS as % of Revenue | ~24% of ARR | 40-60% | 45-55% |
| Gross Margin | ~76% | 40-60% | 45-55% |
| People as % of COGS | 60-70% | 70-85% | 55-70% |
| Software as % of COGS | 15-25% | 5-15% | 15-25% |

## 13. EVM-Based Cost Control (PMBOK Integration)

For projects exceeding 200 man-days, IDEAS applies **Earned Value Management (EVM)** from the PMBOK® Guide to monitor cost performance against the COGS baseline.

- **Cost Baseline (BAC)**: The total approved COGS for the project.
- **Earned Value (EV)**: The value of work completed to date (COGS of accepted deliverables).
- **Actual Cost (AC)**: The actual amount of money spent to date.

Key performance indices, **CPI (Cost Performance Index)** and **SPI (Schedule Performance Index)**, are tracked monthly. A value below 1.0 indicates cost overruns or schedule delays, triggering a review.

For more details, see `references/thought-leadership-frameworks.md`.

## 14. Specialized COGS Models

### 14.1 Data Valuation Service COGS Model (S1.5)

This advisory service is labor-intensive. Its COGS structure reflects this focus, incorporating modern valuation frameworks.

- **Cost Structure**: Dominated by **Direct Labor (70-80%)** for senior consultants, data analysts, and financial analysts.
- **Valuation Approaches**: The methodology integrates the **Deloitte 2025 Data Valuation Framework**, which includes:
    - **Income Approach**: Multi-period excess earnings, relief-from-royalty.
    - **Cost Approach**: Cost to reproduce vs. replace, accounting for developer's profit.
    - **Market Approach**: Analysis of comparable transactions and licensing benchmarks.
- **Data Debt Concept**: The valuation also considers "data debt"—the lifecycle costs, quality issues, and compliance risks that detract from an asset's value.

### 14.2 GenAI & AI Infrastructure Cost Considerations

Projects involving Generative AI have a different cost profile, with software and infrastructure costs becoming more significant.

| Cost Component | Description | Typical Range (per month) |
| :--- | :--- | :--- |
| **LLM API Costs** | Per-token usage for models like GPT-4, Gemini, etc. | Rp 5-50 juta |
| **GPU Compute** | Cloud GPU rental (e.g., NVIDIA H100) for fine-tuning or inference. | Rp 10-100 juta |
| **Vector Database** | Managed services like Pinecone, Weaviate for RAG. | Rp 2-15 juta |

This typically shifts the COGS balance, with Software increasing to **25-40%** of the total.

## 15. Risk Factors in COGS Estimation

- **Scope Creep**: Uncontrolled changes to project scope are the primary cause of budget overruns. Mitigation: Strict change control process and MoSCoW reprioritization.
- **Inaccurate Man-Day Estimates**: Overly optimistic estimates lead to cost blowouts. Mitigation: Peer review of estimates and comparison with historical data from similar projects (`references/task-decomposition.md`).
- **Rate Fluctuation**: Changes in currency exchange rates (for software) or consultant day rates. Mitigation: Hedging strategies for large foreign currency purchases and locking in rates with contractors.
- **Supplier Risk**: Delays or price increases from hardware or software vendors. Mitigation: Pre-approved vendor lists and alternative supplier identification.

## 16. Templates & Scripts

- **Template**: `/templates/cogs-template.xlsx` — The master 10-sheet Excel workbook.
- **Script**: `/scripts/generate_cogs.py` — Python script to automate People Cost calculations from a JSON input.
- **Pricing Engine**: `/scripts/pricing_engine.py` — The centralized Python script for all internal and external rate calculations.

## 17. Glossary of Terms

- **COGS**: Cost of Goods Sold. The direct costs attributable to the production of goods or services.
- **COR**: Cost of Revenue. A more accurate term for service-based businesses.
- **HPS**: Harga Perkiraan Sendiri. Owner's Estimate, used in government procurement.
- **EVM**: Earned Value Management. A project management technique for measuring performance.
- **MoSCoW**: A prioritization technique for managing requirements (Must, Should, Could, Won't).
- **PPN**: Pajak Pertambahan Nilai. Value Added Tax (VAT) in Indonesia, currently 11%.
- **SBM**: Standar Biaya Masukan. Standard Cost Inputs published by the Ministry of Finance.

## 18. Related Documents

- For selling price formation: `../references/rab-hps-methodology.md`
- For personnel rates and roles: `../references/human-resources-and-pricing.md`
- For task and man-day estimates: `../references/task-decomposition.md`
- For regulatory context (PPN, SBM): `../references/regulatory-standards.md`
- For PMBOK and Data Valuation frameworks: `../references/thought-leadership-frameworks.md`
- For DAMA-DMBOK concepts: `../dama-research/concepts/data-valuation.md`
