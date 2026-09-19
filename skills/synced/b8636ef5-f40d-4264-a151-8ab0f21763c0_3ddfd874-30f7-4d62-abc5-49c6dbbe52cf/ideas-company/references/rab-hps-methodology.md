# IDEAS RAB & HPS Methodology for Government Projects

**Last Updated: February 2026**

This document outlines the standardized framework for creating a Rencana Anggaran Biaya (RAB) and Harga Perkiraan Sendiri (HPS) for IDEAS projects, specifically for Indonesian government clients. It is aligned with **Perpres No. 46 Tahun 2025** (the second amendment to Perpres 16/2018 on government procurement), **PMK 32/2025** (Standar Biaya Masukan for Fiscal Year 2026), and best practices from the DAMA-DMBOK framework. The methodology has been proven in large-scale projects like "Satu Data POLRI".

## Table of Contents

1. [Core Principles](#1-core-principles)
2. [Quick Reference: Key Parameters](#2-quick-reference-key-parameters)
3. [RAB vs HPS: Key Distinctions](#3-rab-vs-hps-key-distinctions)
4. [RAB Structure: 6 Major Work Packages](#4-rab-structure-6-major-work-packages)
5. [RAB Template: 24-Column Structure](#5-rab-template-24-column-structure)
6. [HPS Pricing Formula (Pembentukan Harga)](#6-hps-pricing-formula-pembentukan-harga)
7. [Mini Case Study: Pricing a Single Feature](#7-mini-case-study-pricing-a-single-feature)
8. [5 Cost Categories](#8-5-cost-categories)
9. [Standard SDLC Costing per Feature](#9-standard-sdlc-costing-per-feature)
10. [Koefisien Kompleksitas](#10-koefisien-kompleksitas)
11. [Tax Treatment (PPN & PPh 23)](#11-tax-treatment-ppn--pph-23)
12. [From COGS to HPS: Complete Pricing Chain](#12-from-cogs-to-hps-complete-pricing-chain)
13. [Special Considerations for GenAI/AI Projects](#13-special-considerations-for-genai-ai-projects)
14. [Templates & Scripts](#14-templates--scripts)
15. [Glossary of Terms](#15-glossary-of-terms)

## 1. Core Principles

- **Work Package Breakdown**: RAB is structured into major work packages (Tahapan Pekerjaan) reflecting the entire project lifecycle, from governance to capacity building.
- **Feature-Level Granularity**: Costs are broken down to the feature and SDLC step level for maximum transparency and auditability.
- **Cost-Based Calculation**: Adheres to the government's cost-based method for *jasa konsultansi* as stipulated in **Perpres No. 46 Tahun 2025**.
- **Standardized Pricing Formula**: A consistent formula is applied to each line item, incorporating base price, complexity, margin, and taxes.
- **Dual Pricing Track**: Internal price (for IDEAS profitability analysis) and external price (for client HPS) are calculated side-by-side in the `rab-hps-template.csv`.

## 2. Quick Reference: Key Parameters

This section provides a summary of standard parameters for quick data retrieval.

| Parameter | Standard Value | Notes |
|:---|:---|:---|
| **Harga Dasar** | Rp 50,000,000 / Paket | Standard for consulting deliverables (e.g., SOP, Kajian). Derived from COGS. |
| **Koefisien Kompleksitas** | 25% - 100% | Adjusts base price for task difficulty. See section below for guidelines. |
| **Margin** | 50% | Standard IDEAS markup for government projects. |
| **PPh 23** | 2% (grossed up) | Withholding tax for consulting services, calculated as `(Sub Total + Margin) * 2% / 98%`. |
| **PPN** | 11% | Value Added Tax, added on top of the final HPS total. |
| **Working Days / Month** | 20 days | Standard for converting monthly rates to daily rates for man-day calculations. |

## 3. RAB vs HPS: Key Distinctions

| Aspect | RAB (Rencana Anggaran Biaya) | HPS (Harga Perkiraan Sendiri) |
|:---|:---|:---|
| **Prepared by** | IDEAS (as vendor/consultant) | PPK (Pejabat Pembuat Komitmen) on the client side |
| **Purpose** | Internal budget plan for project execution and profitability analysis. | Official government estimate, setting the maximum contract award price for procurement. |
| **Legal Basis** | Internal methodology, COGS data. | **Perpres 46/2025**, Perlem LKPP, **PMK 32/2025 (SBM TA 2026)**. |
| **Data Sources** | Internal COGS, `rate_card.py`. | Market surveys, **e-Katalog LKPP v6** (katalog.inaproc.id), vendor quotes, SBM. For IDEAS' digital products, the e-Katalog price can be a direct HPS reference (see `inaproc-digital-catalog.md`). |
| **Confidentiality** | Strictly internal IDEAS document. | Government document, may be published as part of the procurement process. |
| **Relationship** | IDEAS' RAB is the primary input for the client's PPK to prepare the official HPS. | HPS is the non-negotiable ceiling price for bid evaluation and negotiation. |

In practice, IDEAS prepares its detailed RAB and shares it with the client's PPK team, who then uses it as a foundational reference to prepare the official HPS, validating it against other sources like the SBM and market rates.

## 4. RAB Structure: 6 Major Work Packages

Based on the proven POLRI "Satu Data" project, the RAB is structured into six core work packages, aligning with IDEAS service categories.

| # | Work Package | Description | Service Category | POLRI Value (Example) |
|:-:|:---|:---|:---|:---|
| 1 | **Kajian & Analisis Komprehensif** | Data governance maturity assessment, stakeholder analysis, and strategic roadmap development using interviews, FGDs, co-creation, and benchmarking. | TATA KELOLA (S1) | Rp 11.02B |
| 2 | **Penyusunan Juknis & Juklak** | Development of technical guidelines (Juknis), implementation directives (Juklak), SOPs, data architecture, and metadata standards. | TATA KELOLA (S1) | Rp 51.43B |
| 3 | **Implementasi Tata Kelola Data** | Hands-on implementation of data discovery, data quality management, master data management, and governance processes. | DATA (S2) | Rp 24.80B |
| 4 | **Pengembangan Platform** | Core software development lifecycle for all platform modules and features, including infrastructure setup. | PRODUCT & HARDWARE (S3) | Rp 283.22B |
| 5 | **Implementasi & Adopsi Platform** | User training, adoption measurement, change management, and post-launch support across all user groups. | PRODUCT (S3) | Rp 14.76B |
| 6 | **Peningkatan Kapasitas SDM** | Broader human resource development, training programs, professional certification, and knowledge transfer sessions. | SDM (S4) | Rp 59.12B |

## 5. RAB Template: 24-Column Structure

The `templates/rab-hps-template.csv` uses a comprehensive 24-column structure with 4 hierarchy levels to ensure granular detail.

| Column | Name | Description |
|:---    |:---  |:---|
| [0-3]  | Hierarchy Levels | 4 levels for nesting (Work Package → Sub-Package → Activity → Detail) |
| [4]    | No. | Item number |
| [5]    | KOMPONEN / TAHAPAN PEKERJAAN | Work component or activity description |
| [6]    | SATUAN | Unit of measurement (e.g., Paket, Unit, Orang, Sesi, Laporan) |
| [7]    | SATUAN DETAIL | Detailed unit description (e.g., "Laporan Kajian per Unit Kerja") |
| [8]    | PERKIRAAN VOLUME / KUANTITAS | Estimated volume/quantity |
| [9]    | PERKIRAAN VOLUME DETAIL | Detailed volume breakdown (e.g., "5 Unit Kerja x 2 Laporan") |
| [10]   | PERKIRAAN LAMA WAKTU (BULAN) | Estimated duration in months |
| [11]   | PERKIRAAN JUMLAH ORANG/UNIT | Estimated number of people/units involved |
| [12]   | PERKIRAAN TOTAL | Total effort units (= Volume × Waktu × Orang) |
| [13]   | HARGA DASAR (Rp) | Base price per unit, derived from COGS. |
| [14]   | KOEFISIEN / INDEKS KOMPLEKSITAS | Complexity coefficient (e.g., 100%) |
| [15]   | SUB TOTAL | = Harga Dasar × Koefisien |
| [16]   | MARGIN 50% | = Sub Total × 50% |
| [17]   | PPH 2% | Grossed-up PPh 23 = (Sub Total + Margin) × 2% / 98% |
| [18]   | HARGA SATUAN (Rp) INTERNAL | = Sub Total + Margin + PPH (for internal tracking) |
| [19]   | HARGA SATUAN (Rp) | External/client unit price, the basis for HPS. |
| [20]   | TOTAL BIAYA (Rp) INTERNAL | = Harga Satuan Internal × Perkiraan Total |
| [21]   | TOTAL BIAYA (Rp) | = Harga Satuan × Perkiraan Total |
| [22]   | PERSENTASE (%) | Percentage of total project cost |
| [23]   | KATEGORI | Cost category (TATA KELOLA, DATA, PRODUCT, HARDWARE, SDM) |

## 6. HPS Pricing Formula (Pembentukan Harga)

Each line item in the RAB/HPS is calculated using a standardized, auditable formula.

### Step-by-Step Formula

```
Step 1: Sub Total = Harga Dasar × Koefisien Kompleksitas
Step 2: Margin = Sub Total × 50%
Step 3: PPH = (Sub Total + Margin) × 2% / (100% - 2%)
         Note: PPH is "grossed up" so the net amount received by IDEAS after withholding equals the intended gross profit.
Step 4: Harga Satuan = Sub Total + Margin + PPH
Step 5: Total Biaya = Harga Satuan × Perkiraan Total
```

## 7. Mini Case Study: Pricing a Single Feature

Let's walk through a complete example for one deliverable: **"S1.4: Penyusunan SOP Penyimpanan dan Klasifikasi Data"**.

**Step 1: COGS Calculation (Internal Cost)**
- From `task-decomposition.md`, this task requires a Sr. Data Governance Consultant (30 man-days) and a Jr. Consultant (40 man-days).
- From `human-resources-and-pricing.md`, the internal daily rates (COGS) are:
  - Sr. Consultant: Rp 2,500,000 / day
  - Jr. Consultant: Rp 1,500,000 / day
- **Total People COGS** = (30 * 2.5M) + (40 * 1.5M) = 75M + 60M = **Rp 135,000,000**
- Add overheads (software, operational @ 20% of people cost) = 135M * 20% = Rp 27,000,000
- **Total COGS** = 135M + 27M = **Rp 162,000,000**

**Step 2: RAB/HPS Calculation (Client Price)**

| Parameter | Value | Calculation | Notes |
|:---|:---|:---|:---|
| **Harga Dasar** | Rp 162,000,000 | From COGS calculation above. | This is the base cost for one "Paket" of this SOP. |
| **Koefisien Kompleksitas** | 75% | | Assumed high complexity due to sensitive data classification. |
| **Volume** | 1 Paket | | The deliverable is a single package. |
| **Perkiraan Total** | 1 | | Total effort units. |
| **Sub Total** | Rp 121,500,000 | `162,000,000 * 75%` | Adjusted base price. |
| **Margin 50%** | Rp 60,750,000 | `121,500,000 * 50%` | Standard IDEAS margin. |
| **PPH 2% (Gross Up)** | Rp 3,742,347 | `(121.5M + 60.75M) * 2% / 98%` | Grossed-up withholding tax. |
| **Harga Satuan (HPS)** | **Rp 185,992,347** | `121.5M + 60.75M + 3.74M` | This is the final unit price for the HPS. |
| **Total Biaya (HPS)** | **Rp 185,992,347** | `185,992,347 * 1` | Total line item cost in the HPS. |
| **PPN 11%** | Rp 20,459,158 | `185,992,347 * 11%` | Added on top of the HPS total. |
| **Grand Total to Client** | **Rp 206,451,505** | `185,992,347 + 20,459,158` | The final amount on the contract. |

## 8. 5 Cost Categories

All RAB line items are classified into one of five categories for strategic analysis.

| Category | Description | Typical Work Packages |
|:---|:---|:---|
| **TATA KELOLA** | Governance SOPs, data architecture, metadata standards, policies, compliance frameworks. | WP1, WP2 |
| **DATA** | Data management, quality assessment, data discovery, MDM, data lifecycle management. | WP3 |
| **PRODUCT** | Platform development, features, UI/UX, testing, deployment, and adoption support. | WP4, WP5 |
| **HARDWARE** | Servers, networking, GPU, storage, and other physical or cloud infrastructure. | WP4 |
| **SDM** | Training, capacity building, certification, knowledge transfer, and change management. | WP6 |

## 9. Standard SDLC Costing per Feature

For the "Pengembangan Platform" work package (WP4), each feature is broken down into 11 standard SDLC steps for granular man-day estimation.

| # | SDLC Step | Typical Man-Days | Typical Team Roles |
|:-:|:---|:---|:---|
| 1 | Penyusunan Spesifikasi Kebutuhan Produk (PRD) | 5-10 | PM, PA |
| 2 | Penyusunan Spesifikasi Kebutuhan Bisnis (BRD) | 5-10 | PM, PA, PR |
| 3 | Penyusunan Spesifikasi Kebutuhan Fungsional (FSD) | 5-10 | PM, SA, PA |
| 4 | Antarmuka Pengguna (User Interface Design) | 5-10 | PD |
| 5 | Pengalaman Pengguna (UX Design) dan Pembuatan Prototype | 5-10 | PD, PR |
| 6 | Pemrograman dan Pengkodean | 10-30 | FE, BE, AI |
| 7 | Pelaksanaan Unit Testing | 5-10 | QA Analyst, QA Engineer |
| 8 | Pelaksanaan User Acceptance Test (UAT) | 5-10 | QA, PDO, CSO |
| 9 | Deployment ke Server Development | 2-5 | SRE-DevOps |
| 10 | Deployment ke Server Staging | 2-5 | SRE-DevOps |
| 11 | Deployment ke Server Production | 2-5 | SRE-DevOps, Platform Manager |

## 10. Koefisien Kompleksitas

The Koefisien Kompleksitas (Complexity Coefficient) adjusts the base price based on task difficulty. While not formally standardized by LKPP for IT services, IDEAS uses these internal guidelines for justification.

| Koefisien | When to Apply | Examples |
|:---|:---|:---|
| **25%** | Simple, repetitive tasks with existing templates. | Basic data entry, standard report generation from existing dashboards. |
| **50%** | Moderate complexity, some customization needed. | Standard SOP development for non-critical domains, basic API integration. |
| **75%** | High complexity, significant customization or integration. | Custom data architecture design, complex ETL pipeline development, multi-system integration. |
| **100%** | Maximum complexity, novel, or cutting-edge R&D work. | Generative AI model development, large-scale enterprise platform from scratch, advanced cybersecurity architecture. |

Justification for the chosen coefficient must be documented in the RAB narrative, referencing factors such as: technological novelty, integration requirements, data sensitivity, scale and scope, security posture, and regulatory compliance needs (e.g., UU PDP).

## 11. Tax Treatment (PPN & PPh 23)

### PPh Pasal 23 (Withholding Tax)
- **Rate**: 2% of the gross amount (excluding PPN).
- **Withheld by**: The client (government agency) upon payment.
- **Applied to**: *Jasa konsultansi, jasa teknik, jasa manajemen*.
- **In RAB**: "Grossed up" using the formula: `PPH = (Sub Total + Margin) × 2% / 98%` to ensure IDEAS' net revenue is not affected.

### PPN (Value Added Tax)
- **Rate**: 11% (as per UU HPP No. 7/2021, effective April 2022).
- **Applied on**: The total HPS value (before PPN).
- **Collected by**: IDEAS (as a registered PKP — Pengusaha Kena Pajak).
- **Remitted to**: DJP (Direktorat Jenderal Pajak).

### Complete Tax Chain
```
Harga Satuan (before PPN) = Sub Total + Margin + PPH
Total HPS (before PPN) = Σ (Harga Satuan × Volume)
PPN = Total HPS × 11%
Grand Total Contract Value = Total HPS + PPN
```

## 12. From COGS to HPS: Complete Pricing Chain

The complete chain from internal cost to the final client price is a critical, auditable process.

```mermaid
graph TD
    A[COGS - Internal Cost] --> B{Calculated via pricing_engine.py};
    B --> C[Biaya Personil Internal<br>(Take-home pay + BPJS etc.)];
    C --> D{Divided by 20 working days};
    D --> E[Daily Rate Internal];
    E --> F{Multiplied by man-days per feature};
    F --> G[People Cost per Feature];
    G --> H{+ Software/Hardware/Operational Costs};
    H --> I[Total COGS];
    I --> J{+ Margin 50%};
    J --> K[Harga Dasar - Base Price for HPS];
    K --> L{Adjusted by Koefisien Kompleksitas};
    L --> M[Sub Total];
    M --> N{+ PPH 2% (grossed up)};
    N --> O[Harga Satuan - Unit Price for HPS];
    O --> P{Multiplied by Volume};
    P --> Q[Total Biaya per Item];
    Q --> R{Sum of all items};
    R --> S[Total HPS - before PPN];
    S --> T{+ PPN 11%};
    T --> U[Grand Total HPS - Final Client Price];
```

## 13. Special Considerations for GenAI/AI Projects

Projects involving Generative AI or advanced Machine Learning require specific adjustments to the RAB to account for unique cost structures.

- **Software & Infrastructure Component:**
  - **LLM API Costs:** Include line items for token-based usage (e.g., OpenAI API calls). *Example: `Paket, 10,000,000 tokens, Rp 50/1k tokens`.*
  - **GPU Compute:** Add costs for model training or fine-tuning, either as a cloud service (e.g., AWS SageMaker, GCP Vertex AI) or on-premise hardware amortization. *Example: `Jam, 200 GPU hours, Rp 150,000/hour`.*
  - **Vector Database:** Include licensing or operational costs for vector databases like Pinecone or ChromaDB.
  - **MLOps Platform:** Factor in costs for platforms like MLflow or Weights & Biases.
  - **Guideline:** Expect these costs to be 25-40% of total COGS, compared to 15-25% for traditional projects.

- **People Component:**
  - Utilize the premium rate cards for GenAI specialist roles (e.g., AI Engineer, MLOps Specialist), which carry a 20-40% premium over traditional roles. See `human-resources-and-pricing.md` Section 7 for details.

- **Complexity Factor:**
  - AI/ML development, especially novel applications, justifies a **complexity coefficient of 80-100%**.

- **Value-Based Alternative (for S1.5 Data Asset Valuation):**
  - For services like S1.5 Data Asset Valuation, consider proposing an outcome-based pricing model as an alternative to the standard cost-plus approach. This could be a percentage of the identified data asset value, aligning IDEAS' compensation with the value delivered to the client. This aligns with advanced frameworks like **Deloitte's 2025 Data Valuation methodology** (see `thought-leadership-frameworks.md`).

## 14. Templates & Scripts

- **Template**: `templates/rab-hps-template.csv` — Full 24-column, 1006-row RAB structure with built-in pricing formulas.
- **Template**: `templates/cogs-template.xlsx` — 10-sheet COGS workbook, the source data for the RAB's "Harga Dasar".
- **Script**: `scripts/generate_rab.py` — Python script to automate RAB/HPS generation from a list of service IDs.
- **Script**: `scripts/generate_cogs.py` — People cost component generator based on feature allocation and man-day estimates.
- **Engine**: `scripts/pricing_engine.py` — Centralized library for all rate calculations, containing 3 distinct pricing models.

---

## 15. Glossary of Terms

- **COGS**: Cost of Goods Sold. The direct internal costs to deliver a service.
- **HPS**: Harga Perkiraan Sendiri. The government's official price estimate.
- **LKPP**: Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah. The national public procurement policy agency.
- **PKP**: Pengusaha Kena Pajak. A VAT-registered business.
- **PMK**: Peraturan Menteri Keuangan. Regulation from the Minister of Finance.
- **PPK**: Pejabat Pembuat Komitmen. The client-side official responsible for the commitment-making process.
- **PPN**: Pajak Pertambahan Nilai. Value Added Tax (VAT).
- **PPh 23**: Pajak Penghasilan Pasal 23. Withholding tax on services.
- **Perpres**: Peraturan Presiden. Presidential Regulation.
- **RAB**: Rencana Anggaran Biaya. The vendor's detailed budget plan.
- **SBM**: Standar Biaya Masukan. Standard Input Costs, published annually by the Ministry of Finance.

---

**Related Documents:**
- For underlying COGS structure and calculation: `cogs-methodology.md`
- For detailed personnel rates and roles: `human-resources-and-pricing.md`
- For task decomposition and man-day estimates: `task-decomposition.md`
- For the comprehensive regulatory framework: `regulatory-standards.md` (includes details on **PMK 32/2025**)
- For advanced data valuation and project management frameworks: `thought-leadership-frameworks.md`
- For IDEAS' product listings on the government e-catalog: `inaproc-digital-catalog.md`
