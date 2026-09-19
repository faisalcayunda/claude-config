# Client Intelligence: SPBE 2025 Analysis

> **Last Updated:** February 2026
> **Note:** The analysis in this document is based on the official 2025 SPBE evaluation results. This data should be refreshed annually as new evaluation data becomes publicly available to ensure the most current and actionable intelligence.
>
> **Automated Data Collection:** Use the `web-scraper` skill to automate SPBE data collection. Run `sitemap_discoverer.py` on `evaluasi.spbe.go.id` to discover evaluation URLs, then `page_scraper.py --ai-extract "instansi, indeks_spbe, domain_kebijakan, domain_tata_kelola, domain_manajemen, domain_layanan"` to extract scores. Process with `data_pipeline.py --deduplicate --remove-errors` before feeding into `query_spbe.py`. See `web-scraper/references/scaling_guide.md` for the full SPBE Client Intelligence Pipeline workflow.

This document provides strategic analysis of the 2025 SPBE Index to identify potential government clients for IDEAS. The analysis focuses on institutions with low SPBE scores and/or problematic data portals, cross-referenced with their budget (APBD).

## 1. Market Overview

### National Context (2026 Targets)

The Indonesian government has set ambitious targets for digital transformation, creating a significant market for data and digital governance services. [1]

- **SPBE 2026 Target:** All K/L/D must achieve a minimum "Baik" (Good) SPBE Index score.
- **APBN 2026:** Rp 3,621.3 trillion total budget, with significant allocations for digital government and infrastructure.
- **OECD Finding (Sep 2025 - Feb 2026):** Indonesia is one of only eight Southeast Asian countries with a National Digital Government Strategy that includes all key enablers.
- **SDI Integration:** Satu Data Indonesia continues to drive standardization across all government data portals, mandating interoperability and data quality standards.
- **RPJMN 2025-2029 (Perpres 12/2025):** Emphasizes the acceleration of digital government transformation as a national priority.

### National SPBE Index Trajectory

The national average SPBE index has shown consistent improvement, indicating strong government commitment. However, a significant gap remains between top performers and laggards.

| Tahun | Indeks | Predikat | UN e-Gov Rank | Catatan |
|:---|:---|:---|:---|:---|
| 2019 | 2.18 | Cukup | - | Baseline before major push |
| 2021 | 2.24 | Cukup | - | 69.25% IPPD still below "Baik" |
| 2022 | 2.34 | Cukup | 77 | Incremental progress |
| 2023 | 2.79 | Baik | - | Significant jump in score |
| 2024 | 3.12 | Baik | 64 | Exceeded RPJMN target of 2.60 |
| 2025 | **3.52** | **Baik** | - | **New PEMDI indicator introduced** [2] |

### 2025 Evaluation Highlights

- **New Regulation:** The 2025 evaluation was guided by the new **Permenkomdigi 6/2025**.
- **Top Performers:** Bekasi achieved a "Memuaskan" score of 4.48, while Kaltim reached 4.13. [2]
- **New Indicator:** A key change is the introduction of the **PEMDI (Pemerintahan Digital)** indicator, focusing on user satisfaction and service impact.
- **Efficiency Gains:** The national SPBE program reported efficiency savings of Rp 446 billion from evaluating 12,190 ICT activities. [2]

### 2025 Assessment Results (Portal Status)

While the overall SPBE index is rising, a detailed analysis based on the 2024 data (the latest available granular portal status data) reveals a persistent and significant market opportunity. Over 62% of local governments represent a greenfield or brownfield opportunity for IDEAS to implement a proper data ecosystem.

| Portal Status (2024 Data) | Count | Percentage |
| :--- | :--- | :--- |
| Not Accessible | 325 | 58.9% |
| Verified | 205 | 37.1% |
| Not Found | 22 | 4.0% |
| **Total** | **552** | **100%** |

## 2. High-Potential Target Segments

We can segment potential clients into several tiers based on their SPBE score, budget, and current portal status.

### Tier 1: High APBD, High Need

These are the most attractive clients. They have a large budget and a clear, demonstrable need for improvement (low SPBE score or a broken/missing portal).

| Province/Region | APBD 2025 (Trillion Rp) | SPBE Score (2025) | Portal Status (2024 Data) |
| :--- | :--- | :--- | :--- |
| **Jawa Timur** | 33.3 | 3.60 (Baik) | **Not Found** |
| **Kab. Kutai Kartanegara** | 13.4 | 3.09 (Cukup) | Not Accessible |
| **Sumatera Selatan** | 10.5 | 3.00 (Cukup) | Not Accessible |
| **Sulawesi Selatan** | 10.1 | 3.94 (Baik) | Not Accessible |
| **Kab. Kutai Timur** | 9.1 | 3.02 (Cukup) | Not Accessible |
| **Lampung** | 8.3 | 4.09 (Sangat Baik) | Not Accessible |
| **Kota Medan** | 8.0 | 3.67 (Baik) | Not Accessible |
| **Kab. Mimika** | 7.5 | 0.00 (Kurang) | Not Accessible |

### Tier 2: Greenfield Opportunities (No Portal)

These 22 regions had no data portal found in the 2024 assessment, making them ideal candidates for a full Ekosistem Data implementation from scratch.

| No. | Province | Region |
|:---:|:---|:---|
| 1 | Banten | Kab. Lebak |
| 2 | Jawa Tengah | Kab. Demak |
| 3 | Jawa Timur | **Prov. Jawa Timur** |
| 4 | Jawa Timur | Kab. Jember |
| 5 | Jawa Timur | Kab. Nganjuk |
| 6 | Jawa Timur | Kab. Sampang |
| 7 | Jawa Timur | Kab. Situbondo |
| 8 | Maluku | Kab. Kepulauan Tanimbar |
| 9 | Maluku Utara | Kab. Pulau Taliabu |
| 10 | Nusa Tenggara Timur | Kab. Sumba Tengah |
| 11 | Papua | **Prov. Papua** |
| 12 | Papua | Kab. Asmat |
| 13 | Papua | Kab. Mappi |
| 14 | Papua | Kab. Mimika |
| 15 | Papua | Kab. Paniai |
| 16 | Papua | Kab. Puncak Jaya |
| 17 | Papua Barat | Kab. Pegunungan Arfak |
| 18 | Papua Barat Daya | **Prov. Papua Barat Daya** |
| 19 | Papua Pegunungan | **Prov. Papua Pegunungan** |
| 20 | Papua Pegunungan | Kab. Lanny Jaya |
| 21 | Papua Pegunungan | Kab. Tolikara |
| 22 | Sulawesi Tengah | Kab. Banggai Kepulauan |

### Tier 3: Brownfield Opportunities (Broken Portals)

These 325 regions have a portal, but it's inaccessible. This indicates a failed implementation and a clear pain point. They have already invested in the idea of a data portal and are likely frustrated with the results, making them receptive to a proven solution like the Jabar Ekosistem.

## 3. SPBE Evaluation Framework & IDEAS Service Mapping

The SPBE evaluation framework consists of **4 Domains, 8 Aspects, and 47 Indicators**. The Layanan (Service) domain carries the highest weight at 45.5%, making it the most impactful area for score improvement.

> **Cross-Reference:** For the full 47-indicator breakdown, maturity criteria, and evidence requirements, see `references/spbe-evaluation-framework.md`.

### Domain Weight Distribution

| Domain | Bobot | Indikator | Key Focus |
|:---|:---|:---|:---|
| Kebijakan Internal SPBE | 13% | 10 (@1.3%) | Internal policies (SK/Perkada) |
| Tata Kelola SPBE | 25% | 10 (@2.5%) | Strategic planning, architecture, Tim Koordinasi |
| Manajemen SPBE | 16.5% | 11 (@1.5%) | Risk, security, data, assets, HR, knowledge |
| Layanan SPBE | **45.5%** | 16 (@2.75-3%) | Admin services + public services |

### IDEAS Service to SPBE Indicator Mapping

| IDEAS Service | SPBE Domain | Specific Indicators | Impact |
|:---|:---|:---|:---|
| **S1.1 Data Strategy** | Tata Kelola | 11 (Arsitektur), 12 (Peta Rencana), 13 (Keterpaduan) | **HIGH** |
| **S1.2 Data Governance** | Kebijakan + Manajemen | 1-10 (Kebijakan), 21 (Risiko), 23 (Data) | **CRITICAL** |
| **S1.3 Data Architecture** | Tata Kelola | 11 (Arsitektur), 15 (Pembangunan Aplikasi) | **HIGH** |
| **S1.4 Data Quality** | Manajemen | 23 (Manajemen Data), 43 (Data Terbuka) | **MEDIUM** |
| **S1.5 Data Asset Valuation** | Manajemen | 23 (Data), 24 (Aset TIK) | **MEDIUM** |
| **S2.1 Data Analytics** | Layanan | 40 (Akuntabilitas), 43 (Data Terbuka) | **HIGH** |
| **S2.3 Gov Data Portal** | Layanan | **43 (Data Terbuka - 3%)** | **CRITICAL** |
| **S2.4 Data Integration** | Layanan + Tata Kelola | 18 (Sistem Penghubung), All Level 4 | **HIGH** |
| **S2.5 Secure Data Exchange** | Keamanan + Layanan | 22 (Keamanan), 31 (Audit), Level 4 | **HIGH** |
| **S3.1 DGO as a Service** | Tata Kelola + Manajemen | 19 (Tim Koordinasi), 20 (Kolaborasi), 25 (SDM) | **HIGH** |
| **S3.2 SPBE Assessment** | All Domains | All 47 indicators | **CRITICAL** |
| **S3.3 Digital Transformation** | All Domains | All 47 indicators | **CRITICAL** |
| **S3.4 Knowledge Transfer** | Manajemen | 25 (SDM), 26 (Pengetahuan) | **MEDIUM** |

### Quick-Win Indicators (Highest ROI)

| Priority | Indicator | Weight | Typical Gap | IDEAS Solution |
|:---|:---|:---|:---|:---|
| 1 | 43 - Data Terbuka | 3% | Portal tidak aktif/tidak ada | S2.3 Gov Data Portal |
| 2 | 23 - Manajemen Data | 1.5% | Belum ada SOP manajemen data | S1.2 Data Governance |
| 3 | 11 - Arsitektur SPBE | 2.5% | Belum ada dokumen arsitektur | S1.1 Data Strategy |
| 4 | 12 - Peta Rencana SPBE | 2.5% | Belum ada peta rencana 5 tahun | S1.1 Data Strategy |
| 5 | 3 - Kebijakan Manajemen Data | 1.3% | Belum ada SK/Perkada | S1.2 Data Governance |

## 4. Strategic Approach

1.  **Prioritize Tier 1 & 2**: Focus business development on high-APBD, high-need regions (Tier 1) and those with no existing portal infrastructure (Tier 2).
2.  **Showcase Jabar Success**: Use the comprehensive Ekosistem Data Jabar as the primary case study. Emphasize its 7 integrated components and its role in Jabar's consistent "Memuaskan" SPBE scores. Frame it as a de-risked, proven blueprint.
3.  **Tailor the Pitch**: 
    - For **Greenfield** clients (Tier 2), pitch the full, integrated Ekosistem Data vision as a foundational investment in digital sovereignty and public service excellence.
    - For **Brownfield** clients (Tier 3), diagnose their existing portal's failures and position IDEAS as the expert partner to deliver a working, compliant, and impactful solution.
4.  **Leverage `recommend_service.py`**: Use the script for data-driven initial recommendations, demonstrating analytical rigor from the first interaction.
5.  **UU PDP Compliance Angle**: With UU 27/2022 (UU PDP) in full enforcement since October 2024, position data governance services (S1.2) as urgent necessities for legal risk mitigation. [3]
6.  **Data Valuation & Data Debt Angle**: Use S1.5 Data Asset Valuation to quantify the economic value of data assets. Introduce the **Deloitte 2025 framework** and the concept of **"data debt"** (lifecycle costs, quality issues, compliance risks) to build stronger business cases. Frame investment as a way to increase the data value to data debt ratio. [4]
7.  **IKN Opportunity**: The new capital (IKN) requires greenfield data infrastructure. Proactively engage with IKN authorities to position IDEAS as a foundational data partner.
8.  **DAMA-Aligned Maturity Roadmap**: For sophisticated clients, use the SPBE-DAMA alignment to propose a multi-year roadmap. This positions IDEAS as a long-term strategic advisor. Mention the ongoing **DAMA-DMBOK 3.0 project** to show alignment with future industry standards. [5]

## 5. SPBE-DAMA Maturity Alignment Framework

The SPBE framework can be strategically aligned with the DAMA-DMBOK maturity assessment to provide a dual-lens analysis. This satisfies both Indonesian regulatory requirements (SPBE) and international best practices (DAMA).

### SPBE Domain → DAMA Knowledge Area Mapping

| SPBE Domain | DAMA Knowledge Area | Assessment Synergy |
| :--- | :--- | :--- |
| Tata Kelola SPBE | KA-01 Data Governance, KA-14 Maturity Assessment | Governance charter, stewardship roles, policy framework |
| Manajemen SPBE | KA-02 Data Architecture, KA-09 Metadata Management | Architecture blueprints, metadata standards, catalog design |
| Layanan SPBE | KA-06 Data Integration, KA-08 DW & BI | Portal integration, API governance, analytics services |
| Data & Informasi | KA-03 Data Modeling, KA-11 Data Quality, KA-10 MDM | Data standards, quality dimensions, master data management |
| Keamanan SPBE | KA-05 Data Security, KA-12 Data Ethics | Classification, access control, privacy compliance (UU PDP) |

### Recommended Assessment Methodology

1. **Phase 1 — SPBE Baseline:** Use SPBE evaluation data (from `references/spbe-2024-daerah.csv`) to identify current score and gaps.
2. **Phase 2 — DAMA Deep Dive:** Apply `dama-research/tools/maturity-calculator.py` to assess each relevant DAMA KA.
3. **Phase 3 — Gap Synthesis:** Map SPBE gaps to specific DAMA KA improvements, creating a prioritized roadmap.
4. **Phase 4 — Service Recommendation:** Use `scripts/recommend_service.py` to map identified gaps to IDEAS service offerings.

> **Cross-Reference:** For DAMA maturity assessment templates, see `dama-research/templates/assessment/maturity-assessment-template.md`. For the full SPBE-DAMA integration strategy, see `references/dama-integration-map.md`.

## 6. Glossary of Terms

| Term | Definition |
|:---|:---|
| **APBD** | Anggaran Pendapatan dan Belanja Daerah (Regional Government Budget) |
| **DAMA** | Data Management Association International |
| **DMBOK** | Data Management Body of Knowledge |
| **IPPD** | Instansi Pusat dan Pemerintah Daerah (Central and Regional Government Agencies) |
| **K/L/D** | Kementerian/Lembaga/Daerah (Ministry/Institution/Region) |
| **PEMDI** | Pemerintahan Digital (Digital Government), a new SPBE indicator for 2025 |
| **RPJMN** | Rencana Pembangunan Jangka Menengah Nasional (National Medium-Term Development Plan) |
| **SDI** | Satu Data Indonesia (One Data Indonesia) |
| **SPBE** | Sistem Pemerintahan Berbasis Elektronik (Electronic-Based Government System) |
| **UU PDP** | Undang-Undang Pelindungan Data Pribadi (Personal Data Protection Act) |

---

## 7. References

[1] Peraturan Presiden (Perpres) Nomor 12 Tahun 2025 tentang Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2025-2029.
[2] Kementerian Komunikasi dan Digital (Komdigi), "Hasil Evaluasi SPBE Tahun 2025," Januari 2026.
[3] Undang-Undang (UU) Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.
[4] Deloitte, "The value of data: A new framework for data valuation," 2025.
[5] DAMA International, "DAMA-DMBOK3 Project," accessed February 2026.

---

## 8. Related Documents

- `spbe-evaluation-framework.md`: **Comprehensive SPBE evaluation reference** - 47 indicators, 4 domains, architecture, Tim Koordinasi, Peta Rencana.
- `portfolio-showcase-jabar.md`: Proven solution showcase for potential clients.
- `regulatory-standards.md`: Full regulatory context including SPBE, UU PDP, and SDI.
- `services-catalog.md`: Complete service offerings (15 services) to map to client needs.
- `thought-leadership-frameworks.md`: Section 18 for Data Valuation frameworks applicable to government data assets.
- `dama-integration-map.md`: The full SPBE-DAMA integration strategy.
- `cogs-methodology.md`: Section 12 for Data Valuation service COGS model.
