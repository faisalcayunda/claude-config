# Service-to-Deliverables Mapping for IDEAS

**Last Updated: February 2026**

## Table of Contents

1. [Overview](#overview)
2. [How to Use This Document](#how-to-use-this-document)
3. [Deliverable Categories](#deliverable-categories)
4. [Pillar 1: Advisory & Governance Deliverables](#pillar-1-advisory--governance-deliverables)
5. [Pillar 2: Platform & Solution Implementation Deliverables](#pillar-2-platform--solution-implementation-deliverables)
6. [Pillar 3: Empowerment & Managed Services Deliverables](#pillar-3-empowerment--managed-services-deliverables)
7. [Cross-Service Deliverables](#cross-service-deliverables)
8. [Deliverable Lifecycle & Agile Mapping](#deliverable-lifecycle--agile-mapping)
9. [Regulatory Compliance Mapping](#regulatory-compliance-mapping)
10. [Glossary of Terms](#glossary-of-terms)
11. [Summary Statistics](#summary-statistics)

---

## Overview

Dokumen ini memetakan seluruh output deliverable dari 152 template DAMA-DMBOK (dari skill `dama-research`) ke **15 layanan** IDEAS. Setiap deliverable dikategorikan berdasarkan tipe, fase lifecycle, dan tingkat prioritas (Must/Should/Could) untuk memudahkan penyusunan proposal, scoping proyek, dan estimasi biaya. Pemetaan ini selaras dengan perkembangan proyek DAMA-DMBOK 3.0 dan lanskap regulasi Indonesia terbaru tahun 2025-2026.

Pemetaan ini memungkinkan IDEAS untuk secara konsisten dan terstandar mendefinisikan output deliverable dalam setiap engagement, memastikan bahwa setiap deliverable memiliki template yang siap digunakan dan terhubung dengan DAMA Knowledge Area yang relevan.

---

## How to Use This Document

1.  **Saat menyusun proposal:** Identifikasi service yang diminta klien, lalu lihat daftar deliverable yang relevan. Pilih deliverable berdasarkan prioritas (Must/Should/Could) sesuai scope dan budget.
2.  **Saat estimasi biaya:** Setiap deliverable memiliki estimasi effort (man-days) yang dapat digunakan sebagai input untuk `scripts/generate_cogs.py` dan `scripts/generate_rab.py`.
3.  **Saat delivery:** Gunakan template dari `dama-research/templates/deliverables/` untuk menghasilkan deliverable yang konsisten dan berkualitas.
4.  **Saat scoping:** Gunakan kategori Must/Should/Could untuk menyesuaikan scope dengan budget klien.

---

## Deliverable Categories

| Kategori | Deskripsi | Contoh |
| :--- | :--- | :--- |
| **Strategic** | Dokumen arah strategis dan visi | Data Strategy, Roadmap, Maturity Assessment |
| **Governance** | Kerangka tata kelola dan kebijakan | Governance Charter, Policies, RASCI, SOP |
| **Architecture** | Desain arsitektur dan model data | Architecture Blueprint, Data Model, Data Flow |
| **Quality** | Standar dan laporan kualitas data | DQ Framework, Profiling Results, Scorecard |
| **Security** | Keamanan dan privasi data | Security Policy, Classification, PIA |
| **Integration** | Integrasi dan interoperabilitas | ETL Documentation, API Specs, Data Contract |
| **Metadata** | Pengelolaan metadata | Data Catalog, Data Dictionary, Business Glossary |
| **Analytics** | Analitik dan visualisasi | Dashboard Specs, KPI Definitions, Report Specs |
| **Operations** | Operasional dan pemeliharaan | Runbooks, SLA, Monitoring, Backup Procedures |
| **Training** | Pelatihan dan pemberdayaan | Training Plan, Curriculum, Assessment |

---

## Pillar 1: Advisory & Governance Deliverables

### S1.1 Data Strategy & Roadmap Development

**Primary DAMA KAs:** KA-01, KA-02, KA-14

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Strategy Document | `dama-research/templates/deliverables/KA-01/governance-framework.md` | 8 | Strategic |
| **Must** | Maturity Assessment Report | `dama-research/templates/deliverables/KA-14/maturity-assessment-report.md` | 12 | Strategic |
| **Must** | Maturity Scorecard (Spider Chart) | `dama-research/templates/deliverables/KA-14/maturity-scorecard.md` | 3 | Strategic |
| **Must** | Data Architecture Roadmap | `dama-research/templates/deliverables/KA-02/architecture-roadmap.md` | 10 | Strategic |
| **Must** | Gap Analysis Report | `dama-research/templates/deliverables/KA-14/gap-analysis-report.md` | 5 | Strategic |
| **Must** | Current State Analysis | `dama-research/templates/deliverables/KA-14/current-state-analysis.md` | 8 | Strategic |
| **Should** | Data Landscape Map | `dama-research/templates/deliverables/KA-02/data-landscape-map.md` | 5 | Architecture |
| **Should** | Improvement Roadmap | `dama-research/templates/deliverables/KA-14/improvement-roadmap.md` | 5 | Strategic |
| **Should** | Benchmarking Report | `dama-research/templates/deliverables/KA-14/benchmarking-report.md` | 5 | Strategic |
| **Should** | Executive Presentation | `dama-research/templates/deliverables/KA-14/executive-presentation.md` | 3 | Strategic |
| **Could** | Capability Heat Map | `dama-research/templates/deliverables/KA-14/capability-heat-map.md` | 2 | Strategic |
| **Could** | Assessment Questionnaire | `dama-research/templates/deliverables/KA-14/assessment-questionnaire.md` | 3 | Strategic |

**Total Must:** 46 MD | **Total Should:** 18 MD | **Total Could:** 5 MD

### S1.2 Data Governance & Compliance Framework

**Primary DAMA KAs:** KA-01, KA-05, KA-12

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Governance Charter | `dama-research/templates/deliverables/KA-01/governance-charter.md` | 5 | Governance |
| **Must** | Data Governance Framework | `dama-research/templates/deliverables/KA-01/governance-framework.md` | 10 | Governance |
| **Must** | Data Policies | `dama-research/templates/deliverables/KA-01/data-policies.md` | 8 | Governance |
| **Must** | Data Standards | `dama-research/templates/deliverables/KA-01/data-standards.md` | 8 | Governance |
| **Must** | Roles and Responsibilities (RASCI) | `dama-research/templates/deliverables/KA-01/roles-responsibilities.md` | 5 | Governance |
| **Must** | Data Governance Operating Model | `dama-research/templates/deliverables/KA-01/governance-operating-model.md` | 8 | Governance |
| **Should** | Business Glossary | `dama-research/templates/deliverables/KA-01/business-glossary.md` | 10 | Metadata |
| **Should** | Data Stewardship Plan | `dama-research/templates/deliverables/KA-01/stewardship-plan.md` | 5 | Governance |
| **Should** | Communication and Training Plan | `dama-research/templates/deliverables/KA-01/communication-training-plan.md` | 3 | Training |
| **Should** | Data Security Policy | `dama-research/templates/deliverables/KA-05/security-policy.md` | 5 | Security |
| **Should** | Data Classification Scheme | `dama-research/templates/deliverables/KA-05/classification-scheme.md` | 5 | Security |
| **Should** | Ethical Principles Document | `dama-research/templates/deliverables/KA-12/ethical-principles-document.md` | 3 | Governance |
| **Could** | Governance Metrics Report | `dama-research/templates/deliverables/KA-01/governance-metrics-report.md` | 3 | Governance |
| **Could** | Privacy Impact Assessment (PIA) | `dama-research/templates/deliverables/KA-05/privacy-impact-assessment.md` | 5 | Security |

**Total Must:** 44 MD | **Total Should:** 31 MD | **Total Could:** 8 MD

### S1.3 Data Maturity Assessment & Benchmarking

**Primary DAMA KAs:** KA-14

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Maturity Assessment Report | `dama-research/templates/deliverables/KA-14/maturity-assessment-report.md` | 15 | Strategic |
| **Must** | Maturity Scorecard | `dama-research/templates/deliverables/KA-14/maturity-scorecard.md` | 3 | Strategic |
| **Must** | Current State Analysis | `dama-research/templates/deliverables/KA-14/current-state-analysis.md` | 10 | Strategic |
| **Must** | Gap Analysis Report | `dama-research/templates/deliverables/KA-14/gap-analysis-report.md` | 8 | Strategic |
| **Must** | Assessment Questionnaire | `dama-research/templates/deliverables/KA-14/assessment-questionnaire.md` | 5 | Strategic |
| **Should** | Benchmarking Report | `dama-research/templates/deliverables/KA-14/benchmarking-report.md` | 8 | Strategic |
| **Should** | Capability Heat Map | `dama-research/templates/deliverables/KA-14/capability-heat-map.md` | 3 | Strategic |
| **Should** | Improvement Roadmap | `dama-research/templates/deliverables/KA-14/improvement-roadmap.md` | 5 | Strategic |
| **Should** | Executive Presentation | `dama-research/templates/deliverables/KA-14/executive-presentation.md` | 3 | Strategic |

**Total Must:** 41 MD | **Total Should:** 19 MD

### S1.4 Data Governance & Policy Framework Development

**Primary DAMA KAs:** KA-01, KA-09, KA-11

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Policies (SOP) | `dama-research/templates/deliverables/KA-01/data-policies.md` | 10 | Governance |
| **Must** | Data Standards | `dama-research/templates/deliverables/KA-01/data-standards.md` | 10 | Governance |
| **Must** | Metadata Standards | `dama-research/templates/deliverables/KA-09/metadata-standards.md` | 8 | Metadata |
| **Must** | Data Quality Framework | `dama-research/templates/deliverables/KA-11/data-quality-framework.md` | 8 | Quality |
| **Must** | Data Quality Dimensions | `dama-research/templates/deliverables/KA-11/data-quality-dimensions.md` | 5 | Quality |
| **Should** | Business Rules | `dama-research/templates/deliverables/KA-01/business-rules.md` | 5 | Governance |
| **Should** | Data Quality Metrics | `dama-research/templates/deliverables/KA-11/data-quality-metrics.md` | 5 | Quality |
| **Should** | Content Management Policy | `dama-research/templates/deliverables/KA-07/content-management-policy.md` | 5 | Governance |
| **Should** | Data Retention and Archiving Policy | `dama-research/templates/deliverables/KA-04/retention-archiving-policy.md` | 5 | Governance |
| **Could** | Ethical Data Handling Policy | `dama-research/templates/deliverables/KA-12/ethical-data-handling-policy.md` | 5 | Governance |

**Total Must:** 41 MD | **Total Should:** 20 MD | **Total Could:** 5 MD

### S1.5 Data Asset Valuation & Monetization Advisory

**Description:** This service leverages frameworks like Infonomics and the Deloitte 2025 Data Valuation Framework to quantify the economic value of data assets. It involves identifying and inventorying data, applying valuation models (Income, Cost, Market approaches), analyzing the 'cost of poor quality' (COPQ) and 'data debt', and developing strategies for value realization and monetization.

**Primary DAMA KAs:** KA-01, KA-02, KA-11, KA-14

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Asset Inventory | `dama-research/templates/deliverables/KA-09/data-asset-inventory.md` | 8 | Strategic |
| **Must** | Data Valuation Report (Deloitte & Infonomics) | *Generated on-demand* (`data-valuation-report.md`) | 15 | Strategic |
| **Must** | COPQ & Data Debt Analysis Report | `dama-research/templates/deliverables/KA-11/copq-analysis-report.md` | 10 | Quality |
| **Must** | Executive Value Communication Deck | *Generated on-demand* (`value-communication-deck.md`) | 5 | Strategic |
| **Should** | Data Monetization Strategy | *Generated on-demand* (`monetization-strategy.md`) | 10 | Strategic |
| **Should** | Data Asset Register | `dama-research/templates/deliverables/KA-09/metadata-strategy.md` | 8 | Metadata |
| **Should** | Value Realization Roadmap | *Generated on-demand* (`value-realization-roadmap.md`) | 8 | Strategic |
| **Should** | Data Quality-Value Correlation Matrix | `dama-research/templates/deliverables/KA-11/data-quality-metrics.md` | 5 | Quality |
| **Could** | Data Balance Sheet Readiness Assessment | *Generated on-demand* (`balance-sheet-readiness.md`) | 5 | Strategic |
| **Could** | Benchmarking Report (Industry Data Value) | `dama-research/templates/deliverables/KA-14/benchmarking-report.md` | 5 | Strategic |

**Total Must:** 38 MD | **Total Should:** 31 MD | **Total Could:** 10 MD

---

## Pillar 2: Platform & Solution Implementation Deliverables

### S2.1 Data-Centric Digital Product Development & UX Design

**Primary DAMA KAs:** KA-02, KA-03, KA-06, KA-11

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Product Canvas | *Generated on-demand* (`data-product-canvas.md`) | 3 | Architecture |
| **Must** | Data Architecture Blueprint | `dama-research/templates/deliverables/KA-02/architecture-blueprint.md` | 10 | Architecture |
| **Must** | Conceptual Data Model | `dama-research/templates/deliverables/KA-03/conceptual-data-model.md` | 5 | Architecture |
| **Must** | Logical Data Model | `dama-research/templates/deliverables/KA-03/logical-data-model.md` | 8 | Architecture |
| **Must** | Physical Data Model | `dama-research/templates/deliverables/KA-03/physical-data-model.md` | 8 | Architecture |
| **Must** | Data Contract | `dama-research/templates/deliverables/KA-06/data-contract.md` | 5 | Integration |
| **Must** | Data Quality Rules | `dama-research/templates/deliverables/KA-11/data-quality-rules.md` | 5 | Quality |
| **Must** | API Documentation | `dama-research/templates/deliverables/KA-06/api-documentation.md` | 5 | Integration |
| **Should** | Source-to-Target Mapping | `dama-research/templates/deliverables/KA-06/source-to-target-mapping.md` | 5 | Integration |
| **Should** | Integration Test Plan | `dama-research/templates/deliverables/KA-06/integration-test-plan.md` | 3 | Integration |
| **Should** | Data Lineage | `dama-research/templates/deliverables/KA-06/data-lineage.md` | 5 | Metadata |
| **Should** | UX Wireframes & Prototypes | *Generated on-demand* (`ux-wireframes.md`) | 8 | Architecture |
| **Could** | Model Review and Validation Report | `dama-research/templates/deliverables/KA-03/model-review-validation-report.md` | 3 | Quality |

**Total Must:** 49 MD | **Total Should:** 21 MD | **Total Could:** 3 MD

### S2.2 Core Data Platform & Modernization

**Primary DAMA KAs:** KA-02, KA-04, KA-06

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Architecture Blueprint | `dama-research/templates/deliverables/KA-02/architecture-blueprint.md` | 12 | Architecture |
| **Must** | Storage Architecture | `dama-research/templates/deliverables/KA-04/storage-architecture.md` | 8 | Architecture |
| **Must** | Integration Architecture | `dama-research/templates/deliverables/KA-06/integration-architecture.md` | 8 | Integration |
| **Must** | ETL/ELT Standards | `dama-research/templates/deliverables/KA-06/etl-elt-standards.md` | 5 | Integration |
| **Must** | Technology Standards | `dama-research/templates/deliverables/KA-02/technology-standards.md` | 5 | Architecture |
| **Should** | Data Warehouse Architecture | `dama-research/templates/deliverables/KA-08/dw-architecture.md` | 8 | Architecture |
| **Should** | Database Design | `dama-research/templates/deliverables/KA-04/database-design.md` | 8 | Architecture |
| **Should** | Disaster Recovery Plan | `dama-research/templates/deliverables/KA-04/disaster-recovery-plan.md` | 5 | Operations |
| **Should** | Performance Baselines | `dama-research/templates/deliverables/KA-04/performance-baselines.md` | 3 | Operations |
| **Could** | Integration Patterns | `dama-research/templates/deliverables/KA-02/integration-patterns.md` | 3 | Architecture |

**Total Must:** 43 MD | **Total Should:** 19 MD | **Total Could:** 3 MD

### S2.3 Government Data Portal Platform

**Primary DAMA KAs:** KA-02, KA-06, KA-09, KA-11

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Architecture Blueprint | `dama-research/templates/deliverables/KA-02/architecture-blueprint.md` | 10 | Architecture |
| **Must** | Data Catalog | `dama-research/templates/deliverables/KA-09/data-catalog.md` | 10 | Metadata |
| **Must** | Data Dictionary | `dama-research/templates/deliverables/KA-09/data-dictionary.md` | 8 | Metadata |
| **Must** | API Documentation | `dama-research/templates/deliverables/KA-06/api-documentation.md` | 5 | Integration |
| **Must** | API Standards | `dama-research/templates/deliverables/KA-06/api-standards.md` | 5 | Integration |
| **Must** | Data Quality Framework | `dama-research/templates/deliverables/KA-11/data-quality-framework.md` | 5 | Quality |
| **Must** | Data Exchange Formats | `dama-research/templates/deliverables/KA-06/data-exchange-formats.md` | 3 | Integration |
| **Should** | Business Glossary | `dama-research/templates/deliverables/KA-09/business-glossary.md` | 8 | Metadata |
| **Should** | Taxonomy | `dama-research/templates/deliverables/KA-07/taxonomy.md` | 5 | Metadata |
| **Should** | Data Lineage | `dama-research/templates/deliverables/KA-09/data-lineage.md` | 5 | Metadata |
| **Should** | SLA Documentation | `dama-research/templates/deliverables/KA-04/sla-documentation.md` | 3 | Operations |
| **Should** | Operational Runbooks | `dama-research/templates/deliverables/KA-04/operational-runbooks.md` | 5 | Operations |
| **Could** | Content Standards | `dama-research/templates/deliverables/KA-07/content-standards.md` | 3 | Metadata |
| **Could** | Access Permissions | `dama-research/templates/deliverables/KA-07/access-permissions.md` | 3 | Security |

**Total Must:** 46 MD | **Total Should:** 26 MD | **Total Could:** 6 MD

### S2.4 Enterprise Data Portal & Self-Service Analytics

**Primary DAMA KAs:** KA-08, KA-09, KA-11

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | DW/BI Strategy | `dama-research/templates/deliverables/KA-08/dw-bi-strategy.md` | 5 | Analytics |
| **Must** | Dashboard Specifications | `dama-research/templates/deliverables/KA-08/dashboard-specifications.md` | 8 | Analytics |
| **Must** | KPI Definitions | `dama-research/templates/deliverables/KA-08/kpi-definitions.md` | 5 | Analytics |
| **Must** | Data Catalog | `dama-research/templates/deliverables/KA-09/data-catalog.md` | 8 | Metadata |
| **Must** | Data Dictionary | `dama-research/templates/deliverables/KA-09/data-dictionary.md` | 5 | Metadata |
| **Should** | Report Specifications | `dama-research/templates/deliverables/KA-08/report-specifications.md` | 5 | Analytics |
| **Should** | Dimensional Model | `dama-research/templates/deliverables/KA-08/dimensional-model.md` | 5 | Architecture |
| **Should** | Source System Analysis | `dama-research/templates/deliverables/KA-08/source-system-analysis.md` | 5 | Analytics |
| **Should** | Data Quality Scorecard | `dama-research/templates/deliverables/KA-11/data-quality-scorecard.md` | 3 | Quality |
| **Could** | Data Mart Design | `dama-research/templates/deliverables/KA-08/data-mart-design.md` | 5 | Architecture |

**Total Must:** 31 MD | **Total Should:** 18 MD | **Total Could:** 5 MD

### S2.5 Secure & Trusted Data Exchange — API Gateway Platform

**Primary DAMA KAs:** KA-05, KA-06

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | API Standards | `dama-research/templates/deliverables/KA-06/api-standards.md` | 5 | Integration |
| **Must** | API Documentation | `dama-research/templates/deliverables/KA-06/api-documentation.md` | 8 | Integration |
| **Must** | Data Contract | `dama-research/templates/deliverables/KA-06/data-contract.md` | 5 | Integration |
| **Must** | Security Architecture | `dama-research/templates/deliverables/KA-05/security-architecture.md` | 8 | Security |
| **Must** | Access Control Standards | `dama-research/templates/deliverables/KA-05/access-control-standards.md` | 5 | Security |
| **Must** | Integration Architecture | `dama-research/templates/deliverables/KA-06/integration-architecture.md` | 5 | Integration |
| **Should** | Encryption Standards | `dama-research/templates/deliverables/KA-05/encryption-standards.md` | 3 | Security |
| **Should** | Audit Trail Configuration | `dama-research/templates/deliverables/KA-05/audit-trail-configuration.md` | 3 | Security |
| **Should** | Data Exchange Formats | `dama-research/templates/deliverables/KA-06/data-exchange-formats.md` | 3 | Integration |
| **Could** | Incident Response Plan | `dama-research/templates/deliverables/KA-05/incident-response-plan.md` | 5 | Security |

**Total Must:** 36 MD | **Total Should:** 9 MD | **Total Could:** 5 MD

### S2.6 Analytics and Visualization Solutions

**Primary DAMA KAs:** KA-08, KA-13

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Dashboard Specifications | `dama-research/templates/deliverables/KA-08/dashboard-specifications.md` | 8 | Analytics |
| **Must** | KPI Definitions | `dama-research/templates/deliverables/KA-08/kpi-definitions.md` | 5 | Analytics |
| **Must** | Report Specifications | `dama-research/templates/deliverables/KA-08/report-specifications.md` | 5 | Analytics |
| **Must** | Data Visualization Dashboard | `dama-research/templates/deliverables/KA-13/data-visualization-dashboard.md` | 8 | Analytics |
| **Should** | Analytical Report | `dama-research/templates/deliverables/KA-13/analytical-report.md` | 5 | Analytics |
| **Should** | ETL Documentation | `dama-research/templates/deliverables/KA-08/etl-documentation.md` | 5 | Integration |
| **Should** | Source System Analysis | `dama-research/templates/deliverables/KA-08/source-system-analysis.md` | 3 | Analytics |
| **Could** | Exploratory Data Analysis Report | `dama-research/templates/deliverables/KA-13/eda-report.md` | 5 | Analytics |

**Total Must:** 26 MD | **Total Should:** 13 MD | **Total Could:** 5 MD

---

## Pillar 3: Empowerment & Managed Services Deliverables

### S3.1 Data Governance Office (DGO) as a Service

**Primary DAMA KAs:** KA-01, KA-11

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Data Governance Operating Model | `dama-research/templates/deliverables/KA-01/governance-operating-model.md` | 8 | Governance |
| **Must** | Governance Metrics Report (Monthly) | `dama-research/templates/deliverables/KA-01/governance-metrics-report.md` | 3/mo | Governance |
| **Must** | Issue Resolution Log | `dama-research/templates/deliverables/KA-01/issue-resolution-log.md` | 2/mo | Governance |
| **Must** | Data Quality Report (Monthly) | `dama-research/templates/deliverables/KA-11/data-quality-report.md` | 3/mo | Quality |
| **Must** | Data Quality Scorecard | `dama-research/templates/deliverables/KA-11/data-quality-scorecard.md` | 2/mo | Quality |
| **Should** | Change Request Log | `dama-research/templates/deliverables/KA-01/change-request-log.md` | 1/mo | Governance |
| **Should** | Remediation Plan | `dama-research/templates/deliverables/KA-11/remediation-plan.md` | 3/mo | Quality |
| **Should** | Data Stewardship Plan (Annual) | `dama-research/templates/deliverables/KA-01/stewardship-plan.md` | 5 | Governance |
| **Could** | Root Cause Analysis Report | `dama-research/templates/deliverables/KA-11/root-cause-analysis-report.md` | 3 | Quality |

**Total Must (Year 1):** 8 + (10 × 12) = 128 MD | **Total Should:** 5 + (4 × 12) = 53 MD

### S3.2 Data Literacy & Culture Program

**Primary DAMA KAs:** KA-01

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Communication and Training Plan | `dama-research/templates/deliverables/KA-01/communication-training-plan.md` | 5 | Training |
| **Must** | Training Curriculum & Materials | *Generated on-demand* (`training-curriculum.md`) | 15 | Training |
| **Must** | Assessment & Evaluation Report | *Generated on-demand* (`assessment-report.md`) | 3 | Training |
| **Should** | Security Awareness Training Program | `dama-research/templates/deliverables/KA-05/security-awareness-training.md` | 5 | Training |
| **Should** | Ethics Training Program | `dama-research/templates/deliverables/KA-12/ethics-training-program.md` | 3 | Training |
| **Could** | Data Literacy Maturity Assessment | *Generated on-demand* (`literacy-maturity-assessment.md`) | 5 | Strategic |

**Total Must:** 23 MD | **Total Should:** 8 MD | **Total Could:** 5 MD

### S3.3 Data Management Certified Training

**Primary DAMA KAs:** All 14 KAs

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Training Curriculum (DAMA-DMBOK Based) | *Generated on-demand* (`dama-training-curriculum.md`) | 20 | Training |
| **Must** | Training Materials per Module | *Generated on-demand* (`dama-training-materials.md`) | 30 | Training |
| **Must** | Pre/Post Assessment | *Generated on-demand* (`pre-post-assessment.md`) | 5 | Training |
| **Must** | Certificate of Completion | *Generated on-demand* (`certificate-of-completion.md`) | 1 | Training |
| **Should** | Hands-on Lab Guide | *Generated on-demand* (`hands-on-lab-guide.md`) | 10 | Training |

**Total Must:** 56 MD | **Total Should:** 10 MD

### S3.4 Knowledge Transfer & Thought Leadership

**Primary DAMA KAs:** Varies by topic

| Priority | Deliverable | DAMA Template | Est. MD | Category |
| :--- | :--- | :--- | ---: | :--- |
| **Must** | Presentation Materials | *Generated on-demand* (`presentation-materials.md`) | 5 | Training |
| **Must** | Executive Summary | *Generated on-demand* (`executive-summary.md`) | 2 | Strategic |
| **Should** | Session Recording | *Generated on-demand* (`session-recording.md`) | 1 | Training |
| **Should** | Action Items & Recommendations | *Generated on-demand* (`action-items.md`) | 2 | Strategic |
| **Could** | Follow-up Assessment | *Generated on-demand* (`follow-up-assessment.md`) | 3 | Strategic |

**Total Must:** 7 MD | **Total Should:** 3 MD | **Total Could:** 3 MD

---

## Cross-Service Deliverables

Beberapa deliverable digunakan oleh lebih dari satu service. Deliverable ini harus dibuat sekali dan direferensikan oleh service lain untuk menghindari duplikasi.

| Deliverable | Used By Services | Create Once In |
| :--- | :--- | :--- |
| Data Architecture Blueprint | S1.1, S2.1, S2.2, S2.3 | S1.1 atau S2.2 |
| Data Governance Framework | S1.2, S1.4, S3.1 | S1.2 |
| Data Catalog | S2.3, S2.4 | S2.3 atau S2.4 |
| Data Dictionary | S2.1, S2.3, S2.4 | Per data product |
| Data Quality Framework | S1.4, S2.3, S3.1 | S1.4 |
| API Documentation | S2.1, S2.3, S2.5 | Per API |
| Data Contract | S2.1, S2.5 | Per data product |
| KPI Definitions | S2.4, S2.6 | S2.4 |

---

## Deliverable Lifecycle & Agile Mapping

### Deliverable Status Flow

```
Draft → In Review → Approved → Delivered → Maintained (for living docs)
```

### Mapping ke Agile Hierarchy

| Agile Level | Deliverable Relationship |
| :--- | :--- |
| **Epic** | Menghasilkan 5-15 deliverables (= 1 service) |
| **Feature** | Menghasilkan 2-5 deliverables (= 1 fase) |
| **User Story** | Berkontribusi pada 1 deliverable |
| **Task** | Mengerjakan bagian spesifik dari 1 deliverable |
| **Milestone** | Memicu penyerahan batch deliverables ke klien |

### Deliverable per Milestone (Tipikal)

| Milestone | Termin | Deliverables yang Diserahkan |
| :--- | :--- | :--- |
| M1: Assessment Complete | 30% | Maturity Report, Current State Analysis, Gap Analysis |
| M2: Framework/Design Complete | 40% | Governance Framework, Architecture Blueprint, Data Model |
| M3: Implementation Complete | 20% | Operational Runbooks, Test Reports, API Documentation |
| M4: Handover & Knowledge Transfer | 10% | Training Materials, Final Report, Maintenance Guide |

---

## Regulatory Compliance Mapping

Setiap deliverable yang dihasilkan harus mempertimbangkan kepatuhan terhadap regulasi Indonesia yang relevan. Berikut adalah pemetaan regulasi utama ke kategori deliverable, diperbarui per Februari 2026.

| Regulasi | Deliverable yang Terdampak | Compliance Requirement |
| :--- | :--- | :--- |
| **UU PDP (UU 27/2022)** | Data Classification, Access Control Policy, PIA, Data Retention Policy | Mandatory — berlaku penuh sejak Okt 2024 |
| **Perpres 132/2022 (SPBE)** | Architecture Blueprint, Data Portal, API Documentation, Governance Charter | Mandatory — annual SPBE evaluation |
| **Perpres 39/2019 (SDI)** | Metadata Standards, Data Dictionary, Interoperability Specs | Mandatory — Satu Data compliance |
| **Perpres 46/2025 (PBJ)** | RAB/HPS, Proposal, Cost Estimation | Mandatory — procurement compliance |
| **PMK 32/2025 (SBM TA 2026)** | Rate Card, Personnel Costing, RAB/HPS | Mandatory — government rate standards (ceiling) |
| **PP 49/2025 (Pengupahan)** | Kontrak Kerja, Perhitungan Gaji | Mandatory — standar pengupahan |
| **UU ITE (11/2008 jo. 19/2016)** | Security Architecture, Data Deletion Policy, Right to be Forgotten procedures | Mandatory — sistem elektronik wajib andal dan aman |
| **UU KIP (14/2008) + PP 61/2010** | Data Catalog, PPID System, Information Classification | Mandatory — keterbukaan informasi publik |

> **Cross-Reference:** For detailed regulatory context (25+ primary regulations), see `references/regulatory-standards.md`. For DAMA deliverable templates, see `dama-research/templates/deliverables/`.

---

## Glossary of Terms

| Term | Definition |
| :--- | :--- |
| **COPQ** | Cost of Poor Quality. Biaya yang timbul akibat kualitas data yang buruk. |
| **DAMA KA** | DAMA Knowledge Area. Area pengetahuan dalam kerangka DAMA-DMBOK. |
| **MD** | Man-Day. Satuan estimasi effort, setara dengan satu orang bekerja selama satu hari. |
| **PIA** | Privacy Impact Assessment. Penilaian dampak privasi. |
| **RAB** | Rencana Anggaran Biaya. Detailed budget plan. |
| **HPS** | Harga Perkiraan Sendiri. Owner's estimate for procurement. |
| **SBM** | Standar Biaya Masukan. Standard cost inputs for government budgeting. |
| **SPBE** | Sistem Pemerintahan Berbasis Elektronik. e-Government in Indonesia. |
| **SDI** | Satu Data Indonesia. National data sharing initiative. |

---

## Role-to-Service Assignment Summary

Berikut adalah ringkasan penugasan role ke setiap service, yang diambil dari `task-decomposition.md` dan `estimate_service_cost.py`. Data ini juga tersedia secara programatis melalui `ROLE_SERVICE_MAP` di `rate_card.py` dan fungsi `get_role_services()` / `get_service_roles()` di `pricing_engine.py`.

### Key Roles per Service

| Service | Key Roles (Responsible) |
| :--- | :--- |
| **S1.1** Data Strategy & Roadmap | Project Manager (Data), Business Analyst (Data), Data Architect, Data Governance Analyst, Data Analyst, Data Quality Analyst, Data Visualization Specialist, Product Writer |
| **S1.2** Data Governance & Compliance | Data Governance Manager, Data Governance Analyst, Data Quality Manager, Data Security Manager, Data Steward, Data Owner, Compliance Officer (Data), Product Writer |
| **S1.3** Data Maturity Assessment | Data Governance Analyst, Data Analyst, Business Analyst (Data), Data Quality Analyst, Data Visualization Specialist, Subject Matter Expert (SME) |
| **S1.4** Data Governance & Policy Framework | Data Governance Manager, Data Governance Analyst, Data Quality Manager, Metadata Manager, Data Security Manager, Data Protection Officer (DPO), Database Administrator (DBA) |
| **S1.5** Data Asset Valuation | Data Valuation Specialist, Data Monetization Analyst, Data Product Manager, Chief Data Officer (CDO), Business Analyst (Data), Data Quality Manager |
| **S2.1** Digital Product Dev. & UX | Product Manager, Product Designer, Product Engineering Front-End/Back-End Engineer, Data Architect, Data Modeler, Data Quality Engineer |
| **S2.2** Core Data Platform | Data Architect, Data Engineer, Data Fabric Architect, Data Warehouse Architect, DataOps Engineer, ETL/ELT Developer, Site Reliability Engineer (DevOps) |
| **S2.3** Government Data Portal | Data Architect, Data Engineer, Content Strategist, Geospatial Lead/Analyst/Engineer, Data Integration Specialist, Metadata Manager |
| **S2.4** Enterprise Data Portal & Analytics | Data Analytics Manager, Analytics Engineer, BI Developer, Data Visualization Specialist, Data Analyst, Data Quality Engineer |
| **S2.5** Secure Data Exchange | Security Engineer, Data Protection Officer (DPO), Data Integration Manager, DataOps Engineer, Product Engineering Back-End Engineer |
| **S2.6** Analytics & Visualization | Data Scientist, Data Visualization Specialist, Data Analytics Manager, Analytics Engineer, BI Developer, ETL/ELT Developer |
| **S3.1** DGO as a Service | Chief Data Officer (CDO), Data Governance Manager, Data Governance Analyst, Data Quality Analyst, Data Steward, BI Developer |
| **S3.2** Data Literacy & Culture | Data Literacy Champion, Data Governance Manager, Data Quality Manager, Change Manager (Data), Data Analyst, Data Steward |
| **S3.3** Data Management Training | Data Governance Analyst, Data Quality Manager, Data Architect, Account Manager, Talent Acquisition Specialist, Subject Matter Expert (SME) |
| **S3.4** Knowledge Transfer | Subject Matter Expert (SME), Chief Data Officer (CDO), Data Governance Manager, Data Analyst, Data Engineer, Account Manager |

### Role Utilization Statistics

| Metric | Value |
| :--- | :--- |
| Total roles in RATE_CARD | 141 |
| Roles with service assignments | 63 (45%) |
| Roles without assignments (support/leadership/emerging) | 78 (55%) |
| Average services per assigned role | 5.0 |
| Most-utilized roles | Project Manager (Data) (15), Product Writer (15), Business Analyst (Data) (14) |

> **Note:** Roles without service assignments include C-Level/Board roles (CEO, COO, CTO), emerging AI/ML roles (GenAI Specialist, AI Ethics Officer), and specialized lead/manager roles that provide oversight rather than direct task execution. These roles are available for pricing and team composition but are not directly assigned to WBS subtasks.

> **Cross-Reference:** For complete role definitions including responsibilities, skills, and competency levels, see [`role-definitions.md`](role-definitions.md). For the programmatic role-service mapping, use `ROLE_SERVICE_MAP` in `rate_card.py`.

---

## Summary Statistics

| Metric | Value |
| :--- | :--- |
| Total unique DAMA deliverables mapped | 102 (of 152) |
| IDEAS custom deliverables | 18 |
| Total deliverable types | 120 |
| Services with most deliverables | S1.2 (14), S2.1 (13), S2.3 (14) |
| Services with fewest deliverables | S3.4 (5) |
| Average Must deliverables per service | 6.5 |
| Cross-service shared deliverables | 8 |
| DAMA KAs covered | All 14 |

