# Task Decomposition: IDEAS Service Work Breakdown Structure

> **Last Updated:** February 2026 | **Version:** 6.1
>
> **Cross-References:** `services-catalog.md` (service definitions), `rate_card.py` (role rates), `agile-work-hierarchy.md` (hierarchy definitions), `cogs-methodology.md` (cost conversion)

## Table of Contents

1. [Introduction](#introduction)
2. [Structure & Conventions](#structure--conventions)
3. [Pillar 1: Advisory & Governance](#pillar-1-advisory--governance)
   - [S1.1 Data Strategy & Roadmap Development](#service-11-data-strategy--roadmap-development-epic)
   - [S1.2 Data Governance & Compliance Framework](#service-12-data-governance--compliance-framework-epic)
   - [S1.3 Data Maturity Assessment & Benchmarking](#service-13-data-maturity-assessment--benchmarking-epic)
   - [S1.4 Data Governance & Policy Framework Dev.](#service-14-data-governance--policy-framework-development-epic)
   - [S1.5 Data Asset Valuation & Monetization Advisory](#service-15-data-asset-valuation--monetization-advisory-epic)
4. [Pillar 2: Platform & Solution Implementation](#pillar-2-platform--solution-implementation)
   - [S2.1 Data-Centric Digital Product Dev. & UX](#service-21-data-centric-digital-product-development--ux-design-epic)
   - [S2.2 Core Data Platform & Modernization](#service-22-core-data-platform--modernization-epic)
   - [S2.3 Government Data Portal Platform](#service-23-government-data-portal-platform-epic)
   - [S2.4 Enterprise Data Portal & Self-Service Analytics](#service-24-enterprise-data-portal--self-service-analytics-epic)
   - [S2.5 Secure Data Exchange - API Gateway](#service-25-secure-data-exchange---api-gateway-epic)
   - [S2.6 Analytics and Visualization Solutions](#service-26-analytics-and-visualization-solutions-epic)
5. [Pillar 3: Empowerment & Managed Services](#pillar-3-empowerment--managed-services)
   - [S3.1 DGO as a Service](#service-31-data-governance-office-dgo-as-a-service-epic)
   - [S3.2 Data Literacy & Culture Program](#service-32-data-literacy--culture-program-epic)
   - [S3.3 Data Management Certified Training](#service-33-data-management-certified-training-epic)
   - [S3.4 Knowledge Transfer & Thought Leadership](#service-34-knowledge-transfer--thought-leadership--narasumber-epic)
6. [Summary: Total Estimated Man-Days per Service](#summary-total-estimated-man-days-per-service)
7. [Notes](#notes)

---

## Introduction

Dokumen ini adalah **Work Breakdown Structure (WBS)** komprehensif untuk seluruh 15 layanan IDEAS, terstruktur menggunakan **Agile Work Item Hierarchy** (lihat `agile-work-hierarchy.md`) dan selaras dengan **PMBOK 6th Edition Section 5.4 (Create WBS)** serta **PMBOK 7th Edition Performance Domains**. Setiap service dipecah menjadi Feature → Task → Subtask, dilengkapi dengan:

- **Subtask grooming**: Setiap task di-dekomposisi menjadi subtask granular (2-8 jam) untuk visibilitas tracking
- **Role assignment**: Setiap subtask memiliki role utama yang bertanggung jawab (dari 141-role RATE_CARD)
- **RASCI matrix**: Setiap output deliverable memiliki assignment Responsible, Accountable, Supportive, Consulted, Informed
- **Output Deliverable Traceability**: Tabel per Feature yang menunjukkan deliverable mana dihasilkan oleh task/subtask mana
- **Medium complexity default**: Estimasi man-days menggunakan kompleksitas menengah sebagai baseline
- **Story Points (SP)**: Estimasi relatif menggunakan Modified Fibonacci (1, 2, 3, 5, 8, 13, 21) berdasarkan kompleksitas, effort, dan uncertainty
- **Predecessor/Successor**: Dependency antar task/subtask menggunakan Finish-to-Start (FS) notation
- **Execution Mode**: Serial (S) atau Parallel (P) — menunjukkan apakah item bisa berjalan bersamaan
- **PMBOK 100% Rule**: Total scope di setiap level = jumlah seluruh child items (tidak ada pekerjaan yang hilang atau duplikat)
- **Control Account alignment**: Setiap Feature berfungsi sebagai Control Account untuk EVM tracking

### Complexity Scaling

| Complexity | Multiplier | Keterangan |
| :--- | ---: | :--- |
| Simple | 0.7x | Scope kecil, sedikit stakeholder, infrastruktur existing |
| **Medium (Default)** | **1.0x** | **Baseline dalam dokumen ini** |
| Complex | 1.4x | Multi-stakeholder, integrasi legacy, regulasi ketat |
| Very Complex | 1.8x | Enterprise-wide, multi-system, multi-year |

### RASCI Legend

| Code | Role | Deskripsi |
| :--- | :--- | :--- |
| **R** | Responsible | Mengerjakan dan menghasilkan deliverable |
| **A** | Accountable | Bertanggung jawab akhir, menyetujui deliverable |
| **S** | Supportive | Menyediakan sumber daya atau membantu |
| **C** | Consulted | Memberikan input/expertise sebelum atau selama |
| **I** | Informed | Diberitahu tentang progres/penyelesaian |

### ID Convention

| Level | Format | Contoh |
| :--- | :--- | :--- |
| Service (Epic) | S{pillar}.{service} | S1.1 |
| Feature | S{p}.{s}-{letter} | S1.1-A |
| Task | S{p}.{s}-{nn} | S1.1-01 |
| Subtask | S{p}.{s}-{nn}{letter} | S1.1-01a |

### Story Point Reference Scale

| SP | Complexity | Typical MD | Reference Story (Data Management Context) |
| ---: | :--- | :--- | :--- |
| 1 | Trivial | 0.5-1 | Schedule meetings, distribute questionnaires |
| 2 | Simple | 1-2 | Prepare interview guides, collect evidence |
| 3 | Moderate | 2-3 | Synthesize findings, score maturity per KA |
| 5 | Medium | 3-5 | Design architecture blueprint, develop policy draft |
| 8 | Complex | 5-8 | Conduct 8-12 stakeholder interviews, build ETL pipeline |
| 13 | Very Complex | 8-14 | Full data model design, platform integration testing |
| 21 | Epic-level | 14+ | Enterprise-wide transformation (should be decomposed) |

### Dependency & Execution Mode

| Symbol | Meaning | Description |
| :--- | :--- | :--- |
| **S** | Serial | Item harus menunggu predecessor selesai sebelum mulai |
| **P** | Parallel | Item bisa berjalan bersamaan dengan sibling items |
| **—** | No dependency | Item bisa dimulai tanpa menunggu item lain |
| **FS** | Finish-to-Start | Default dependency type: successor mulai setelah predecessor selesai |

---

## Pillar 1: Advisory & Governance

## Pillar 1: Advisory & Governance

### Service 1.1: Data Strategy & Roadmap Development (Epic)

**DAMA KAs**: KA-01 (Primary), KA-02, KA-14
**Lifecycle Stage**: Discovery → Planning
**Methodology**: Design Thinking + DAMA-DMBOK Assessment
**Total Man-Days**: 155 | **Features**: 3 | **Tasks**: 12 | **Subtasks**: 58

#### Feature S1.1-A: Current State Assessment & Discovery

**Milestone**: M1 — Assessment Report Delivered & Approved → Termin 1 (30%)
**Lifecycle Stage**: Discovery (Identify, Assess)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.1-01 | Task | Conduct stakeholder interviews & requirements gathering | KA-01 | 16 | 13 | — | S | | |
| S1.1-01a | Subtask | Identify & schedule key stakeholders (C-Level, Data Owners) | KA-01 | 2 | 2 | — | S | Project Manager (Data) | R |
| S1.1-01b | Subtask | Prepare interview guides per stakeholder group | KA-01 | 2 | 2 | S1.1-01a | P | Business Analyst (Data) | R |
| S1.1-01c | Subtask | Conduct interviews (8-12 sessions) | KA-01 | 5 | 5 | S1.1-01b | S | Business Analyst (Data) | R |
| S1.1-01d | Subtask | Synthesize findings into stakeholder needs matrix | KA-01 | 3 | 3 | S1.1-01c | S | Business Analyst (Data) | R |
| S1.1-01e | Subtask | Validate synthesized findings with key stakeholders | KA-01 | 2 | 2 | S1.1-01d | S | Business Analyst (Data) | R |
| S1.1-01f | Subtask | Get formal sign-off on requirements from CDO | KA-01 | 2 | 1 | S1.1-01e | S | Chief Data Officer (CDO) | A |
| S1.1-02 | Task | Assess current data landscape & inventory | KA-02 | 18 | 13 | S1.1-01 | S | | |
| S1.1-02a | Subtask | Inventory existing data sources, systems & databases | KA-02 | 4 | 5 | — | S | Data Architect | R |
| S1.1-02b | Subtask | Map data flows between systems (as-is) | KA-02 | 4 | 5 | S1.1-02a | P | Data Architect | R |
| S1.1-02c | Subtask | Assess data quality baseline (sampling & profiling) | KA-11 | 3 | 3 | S1.1-02a | P | Data Quality Analyst | R |
| S1.1-02d | Subtask | Document current technology stack & capabilities | KA-02 | 3 | 3 | S1.1-02c | S | Data Engineer | R |
| S1.1-02e | Subtask | Analyze data storage and processing costs | KA-04 | 2 | 2 | S1.1-02d | P | Cloud Infrastructure Engineer | R |
| S1.1-02f | Subtask | Review data lifecycle management processes | KA-04 | 2 | 2 | S1.1-02d | P | Data Steward | R |
| S1.1-03 | Task | Conduct data maturity quick-scan | KA-14 | 14 | 8 | S1.1-02 | S | | |
| S1.1-03a | Subtask | Distribute & collect maturity assessment questionnaires | KA-14 | 2 | 2 | — | S | Data Governance Analyst | R |
| S1.1-03b | Subtask | Score maturity across 14 DAMA Knowledge Areas | KA-14 | 4 | 5 | S1.1-03a | S | Data Governance Analyst | R |
| S1.1-03c | Subtask | Generate maturity spider chart & scorecard | KA-14 | 2 | 2 | S1.1-03b | S | Data Analyst | R |
| S1.1-03d | Subtask | Identify top-5 priority improvement areas | KA-14 | 2 | 2 | S1.1-03a | P | Data Governance Manager | R |
| S1.1-03e | Subtask | Benchmark maturity against industry standards | KA-14 | 2 | 2 | S1.1-03d | S | Data Valuation Specialist | R |
| S1.1-03f | Subtask | Present maturity findings to Data Governance Council | KA-14 | 2 | 2 | S1.1-03e | S | Data Governance Manager | R |
| S1.1-04 | Task | Perform Security & Compliance Gap Analysis | KA-05 | 10 | 8 | S1.1-02 | P | | |
| S1.1-04a | Subtask | Review existing data security policies and controls | KA-05 | 3 | 3 | — | S | Data Security Analyst | R |
| S1.1-04b | Subtask | Assess compliance with relevant regulations (e.g., GDPR, PDP) | KA-01 | 3 | 3 | S1.1-04a | S | Compliance Officer (Data) | R |
| S1.1-04c | Subtask | Identify security vulnerabilities in the data lifecycle | KA-05 | 2 | 2 | S1.1-04a | P | Security Engineer | R |
| S1.1-04d | Subtask | Document security and compliance gaps and risks | KA-05 | 2 | 2 | S1.1-04c | S | Data Security Analyst | R |

**Feature S1.1-A Subtotal**: 58 Man-Days, 42 SP (4 Tasks, 22 Subtasks)

##### Output Deliverable Traceability — Feature S1.1-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | DAMA Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Stakeholder Needs Matrix | Must | S1.1-01d | Business Analyst (Data) | Project Manager (Data) | Data Governance Analyst | Chief Data Officer (CDO) | Client | — |
| 2 | Data Landscape Map | Must | S1.1-02a, S1.1-02b | Data Architect | Project Manager (Data) | Data Engineer | Chief Data Officer (CDO) | Client | KA-02/08 |
| 3 | Data Quality Baseline Report | Must | S1.1-02c | Data Quality Analyst | Project Manager (Data) | Data Architect | Data Governance Manager | Client | KA-11/07 |
| 4 | Maturity Scorecard (Spider Chart) | Must | S1.1-03b, S1.1-03c | Data Governance Analyst, Data Analyst | Project Manager (Data) | Data Governance Manager | Chief Data Officer (CDO) | Client | KA-14/02 |
| 5 | Current State Assessment Report | Must | S1.1-01d, S1.1-02d, S1.1-03d | Business Analyst (Data) | Project Manager (Data) | Data Architect, Data Governance Analyst | Chief Data Officer (CDO) | Client | KA-14/05 |
| 6 | Security & Compliance Gap Report | Must | S1.1-04d | Data Security Analyst | CTO | Compliance Officer (Data) | Chief Data Officer (CDO) | Client | KA-05/08 |

> **RASCI Role Legend**: Business Analyst (Data), Project Manager (Data), Data Governance Analyst, Chief Data Officer (CDO), Data Architect, Data Engineer, Data Quality Analyst, Data Governance Manager, Data Analyst, Cloud Infrastructure Engineer, Data Steward, Data Valuation Specialist, Data Security Analyst, Compliance Officer (Data), Security Engineer, CTO

---

#### Feature S1.1-B: Strategy Formulation & Roadmap Design

**Milestone**: M2 — Data Strategy & Roadmap Draft Approved → Termin 2 (40%)
**Lifecycle Stage**: Planning (Define, Prioritize)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.1-05 | Task | Define data vision, principles & strategic objectives | KA-01 | 14 | 8 | S1.1-03 | S | | |
| S1.1-05a | Subtask | Facilitate vision workshop with leadership team | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S1.1-05b | Subtask | Draft data vision statement & guiding principles | KA-01 | 3 | 3 | S1.1-05a | P | Data Governance Manager | R |
| S1.1-05c | Subtask | Define strategic objectives aligned with business goals | KA-01 | 2 | 2 | S1.1-05a | P | Business Analyst (Data) | R |
| S1.1-05d | Subtask | Validate objectives with C-Level sponsors | KA-01 | 2 | 2 | S1.1-05c | S | Chief Data Officer (CDO) | R |
| S1.1-05e | Subtask | Develop KPIs to measure strategic objectives | KA-01 | 2 | 2 | S1.1-05d | S | Data Analyst | R |
| S1.1-05f | Subtask | Secure CEO and Board approval for the vision | KA-01 | 2 | 1 | S1.1-05e | S | CEO | A |
| S1.1-06 | Task | Develop target-state data architecture (to-be) | KA-02 | 16 | 13 | S1.1-05 | S | | |
| S1.1-06a | Subtask | Design target data architecture blueprint | KA-02 | 4 | 5 | — | S | Data Architect | R |
| S1.1-06b | Subtask | Define technology stack recommendations | KA-02 | 3 | 3 | S1.1-06a | P | Data Architect | R |
| S1.1-06c | Subtask | Conduct gap analysis (as-is vs to-be) | KA-02 | 3 | 3 | S1.1-06b | S | Data Architect | R |
| S1.1-06d | Subtask | Estimate investment & resource requirements | KA-02 | 2 | 2 | S1.1-06c | S | Business Analyst (Data) | R |
| S1.1-06e | Subtask | Create data flow diagrams for the target state | KA-02 | 2 | 2 | S1.1-06a | P | Data Modeler | R |
| S1.1-06f | Subtask | Present architecture to technical review board | KA-02 | 2 | 2 | S1.1-06e | S | CTO | A |
| S1.1-07 | Task | Design implementation roadmap (3-5 year) | KA-01 | 16 | 13 | S1.1-06 | S | | |
| S1.1-07a | Subtask | Define initiative portfolio & prioritization (MoSCoW) | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S1.1-07b | Subtask | Create phased roadmap with dependencies & milestones | KA-01 | 4 | 5 | S1.1-07a | P | Project Manager (Data) | R |
| S1.1-07c | Subtask | Develop business case per initiative (ROI/benefit) | KA-01 | 3 | 3 | S1.1-07a | P | Business Analyst (Data) | R |
| S1.1-07d | Subtask | Design governance structure for roadmap execution | KA-01 | 2 | 2 | S1.1-07a | P | Data Governance Manager | R |
| S1.1-07e | Subtask | Allocate budget and resources to roadmap phases | KA-01 | 2 | 2 | S1.1-07d | S | Business Analyst (Data) | R |
| S1.1-07f | Subtask | Conduct Quality Assurance review of the roadmap | KA-11 | 2 | 2 | S1.1-07e | S | Product Engineering QA Engineer | R |

**Feature S1.1-B Subtotal**: 46 Man-Days, 34 SP (3 Tasks, 18 Subtasks)

##### Output Deliverable Traceability — Feature S1.1-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | DAMA Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Data Strategy Document | Must | S1.1-05a, S1.1-05b, S1.1-05c | Data Governance Manager | Chief Data Officer (CDO) | Business Analyst (Data) | Client CxO | Client | KA-01/02 |
| 2 | Target Architecture Blueprint | Must | S1.1-06a, S1.1-06b | Data Architect | CTO | Data Engineer | Data Governance Manager | Client | KA-02/02 |
| 3 | Gap Analysis Report | Must | S1.1-06c | Data Architect | Project Manager (Data) | Business Analyst (Data) | Chief Data Officer (CDO) | Client | KA-14/06 |
| 4 | Implementation Roadmap | Must | S1.1-07a, S1.1-07b | Project Manager (Data), Data Governance Manager | Chief Data Officer (CDO) | Business Analyst (Data) | Client CxO | Client | KA-02/06 |
| 5 | Business Case per Initiative | Should | S1.1-07c | Business Analyst (Data) | Project Manager (Data) | Data Governance Manager | Chief Data Officer (CDO) | Client CFO | — |

> **RASCI Role Legend**: Data Governance Manager, Chief Data Officer (CDO), Business Analyst (Data), Data Analyst, CEO, Data Architect, CTO, Data Engineer, Data Modeler, Project Manager (Data), Business Analyst (Data), Product Engineering QA Engineer

---

#### Feature S1.1-C: Presentation, Validation & Knowledge Transfer

**Milestone**: M3 — Final Strategy Presented & Accepted → Termin 3 (30%)
**Lifecycle Stage**: Planning → Launch (Validate, Handover)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.1-08 | Task | Prepare executive presentation & visualization | KA-01 | 14 | 8 | S1.1-07 | S | | |
| S1.1-08a | Subtask | Design executive summary & key findings deck | KA-01 | 3 | 3 | — | S | Business Analyst (Data) | R |
| S1.1-08b | Subtask | Create data visualizations & infographics | KA-01 | 3 | 3 | S1.1-08a | P | Data Visualization Specialist | R |
| S1.1-08c | Subtask | Internal review & dry run | KA-01 | 2 | 2 | S1.1-08a | P | Data Governance Manager | R |
| S1.1-08d | Subtask | Incorporate feedback & finalize presentation | KA-01 | 2 | 2 | S1.1-08c | S | Business Analyst (Data) | R |
| S1.1-08e | Subtask | Prepare speaker notes and talking points | KA-01 | 2 | 2 | S1.1-08d | S | Content Officer (Writer) | R |
| S1.1-08f | Subtask | Translate presentation to Bahasa Indonesia | KA-01 | 2 | 1 | S1.1-08e | S | Content Officer (Writer) | R |
| S1.1-09 | Task | Conduct executive presentation & stakeholder validation | KA-01 | 14 | 8 | S1.1-08 | S | | |
| S1.1-09a | Subtask | Present strategy to C-Level & steering committee | KA-01 | 2 | 2 | — | S | Chief Data Officer (CDO) | R |
| S1.1-09b | Subtask | Facilitate Q&A and feedback session | KA-01 | 2 | 2 | S1.1-09a | S | Data Governance Manager | R |
| S1.1-09c | Subtask | Incorporate stakeholder feedback into final documents | KA-01 | 3 | 3 | S1.1-09b | S | Business Analyst (Data) | R |
| S1.1-09d | Subtask | Obtain formal sign-off & approval | KA-01 | 3 | 3 | S1.1-09c | S | Project Manager (Data) | R |
| S1.1-09e | Subtask | Distribute final documents to all stakeholders | KA-01 | 2 | 1 | S1.1-09d | S | Account Manager | R |
| S1.1-09f | Subtask | Archive project documents and deliverables | KA-01 | 2 | 1 | S1.1-09e | S | Master Data Manager (MDM) | R |
| S1.1-10 | Task | Knowledge transfer & handover | KA-01 | 23 | 21 | S1.1-09 | S | | |
| S1.1-10a | Subtask | Compile final document package (all deliverables) | KA-01 | 3 | 3 | — | S | Product Writer | R |
| S1.1-10b | Subtask | Conduct knowledge transfer workshop (2 sessions) | KA-01 | 4 | 5 | S1.1-10a | S | Data Governance Manager | R |
| S1.1-10c | Subtask | Create implementation quick-start guide | KA-01 | 5 | 5 | S1.1-10a | P | Product Writer | R |
| S1.1-10d | Subtask | Provide one-on-one coaching for key roles | KA-01 | 5 | 5 | S1.1-10b | S | Data Literacy Champion | R |
| S1.1-10e | Subtask | Set up a community of practice for data champions | KA-01 | 4 | 5 | S1.1-10d | S | Content Strategist | R |
| S1.1-10f | Subtask | Handover to the operational/BAU team | KA-01 | 2 | 2 | S1.1-10e | S | Project Manager (Data) | R |

**Feature S1.1-C Subtotal**: 51 Man-Days, 37 SP (3 Tasks, 18 Subtasks)

##### Output Deliverable Traceability — Feature S1.1-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | DAMA Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Executive Presentation Deck | Must | S1.1-08a, S1.1-08b | Business Analyst (Data), Data Visualization Specialist | Project Manager (Data) | Data Governance Manager | Chief Data Officer (CDO) | Client | KA-14/09 |
| 2 | Final Data Strategy Document (signed) | Must | S1.1-09c, S1.1-09d | Business Analyst (Data) | Chief Data Officer (CDO) | Project Manager (Data) | Client CxO | Client | KA-01/02 |
| 3 | Knowledge Transfer Materials | Must | S1.1-10a, S1.1-10b, S1.1-10c | Product Writer, Data Governance Manager | Project Manager (Data) | Business Analyst (Data) | Client IT | Client | knowledge-transfer-template.md |
| 4 | Implementation Quick-Start Guide | Should | S1.1-10c | Product Writer | Project Manager (Data) | Data Governance Manager | Data Architect | Client | output-deliverable-template.md |

> **RASCI Role Legend**: Business Analyst (Data), Data Visualization Specialist, Project Manager (Data), Data Governance Manager, Chief Data Officer (CDO), Content Officer (Writer), Content Officer (Writer), Account Manager, Master Data Manager (MDM), Product Writer, Data Literacy Champion, Content Strategist

**S1.1-TOTAL**: **Data Strategy & Roadmap Development** — **155 Man-Days, 113 SP** (3 Features, 10 Tasks, 58 Subtasks)

---

### Service 1.2: Data Governance & Compliance Framework (Epic)

**DAMA KAs**: KA-01 (Primary), KA-05, KA-12  
**Lifecycle Stage**: Discovery → Planning → Development  
**Methodology**: DAMA-DMBOK Governance Framework + Regulatory Alignment  
**Total Man-Days**: 145 | **Features**: 3 | **Tasks**: 14 | **Subtasks**: 56

---

#### Feature S1.2-A: Governance Assessment & Gap Analysis

**Milestone**: M1 — Governance Assessment Report Delivered → Termin 1 (30%)  
**Lifecycle Stage**: Discovery (Identify, Assess)

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.2-01 | Task | Assess current governance state & regulatory landscape | KA-01 | 18 | 15 | — | S |  |  |
| S1.2-01a | Subtask | Review existing governance policies & documentation | KA-01 | 3 | 3 | — | S | Data Governance Analyst | R |
| S1.2-01b | Subtask | Map applicable regulations (UU PDP, SPBE, Perpres 39) | KA-05 | 3 | 3 | S1.2-01a | P | Compliance Officer (Data) | R |
| S1.2-01c | Subtask | Conduct governance maturity interviews (6-8 sessions) | KA-01 | 5 | 5 | S1.2-01b | S | Data Governance Manager | R |
| S1.2-01d | Subtask | Assess data security & privacy current state | KA-05 | 3 | 3 | S1.2-01a | P | Data Protection Officer (DPO) | R |
| S1.2-01e | Subtask | Perform initial data quality review | KA-11 | 2 | 2 | S1.2-01a | P | Data Quality Manager | R |
| S1.2-01f | Subtask | Conduct stakeholder interviews for regulatory impact | KA-05 | 2 | 2 | S1.2-01c | S | Project Manager (Data) | R |
| S1.2-02 | Task | Conduct gap analysis against DAMA-DMBOK & regulations | KA-01 | 16 | 12 | S1.2-01 | S |  |  |
| S1.2-02a | Subtask | Score governance maturity per DAMA Knowledge Area | KA-14 | 3 | 3 | — | S | Data Governance Analyst | R |
| S1.2-02b | Subtask | Identify compliance gaps against UU PDP & sector regulations | KA-05 | 3 | 3 | S1.2-02a | P | Compliance Officer (Data) | R |
| S1.2-02c | Subtask | Prioritize gaps by risk & business impact | KA-01 | 3 | 3 | S1.2-02b | S | Data Governance Manager | R |
| S1.2-02d | Subtask | Draft gap analysis report with recommendations | KA-01 | 3 | 3 | S1.2-02a | P | Business Analyst (Data) | R |
| S1.2-02e | Subtask | Conduct security and privacy compliance check | KA-05 | 2 | 2 | S1.2-02b | P | Chief Privacy Officer (CPO) | R |
| S1.2-02f | Subtask | Validate gap analysis with Data Security Manager | KA-05 | 2 | 2 | S1.2-02d | S | Data Security Manager | R |
| S1.2-03 | Task | Define governance scope & organizational readiness | KA-01 | 14 | 10 | S1.2-02 | S |  |  |
| S1.2-03a | Subtask | Define governance scope (data domains, business units) | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S1.2-03b | Subtask | Assess organizational readiness & change capacity | KA-01 | 3 | 3 | S1.2-03a | P | Change Manager (Data) | R |
| S1.2-03c | Subtask | Identify governance champions & sponsors | KA-01 | 2 | 2 | S1.2-03a | P | Project Manager (Data) | R |
| S1.2-03d | Subtask | Draft governance implementation approach | KA-01 | 2 | 2 | S1.2-03a | P | Data Governance Manager | R |
| S1.2-03e | Subtask | Review scope with Chief Data Officer (CDO) and Chief Compliance Officer | KA-01 | 2 | 2 | S1.2-03d | S | Chief Data Officer (CDO) | R |
| S1.2-03f | Subtask | Prepare governance scope presentation for Board | KA-01 | 2 | 2 | S1.2-03e | S | Head of Digital Branding & Communication | R |
| S1.2-04 | Task | Conduct quality assurance & validation of assessment outputs | KA-01 | 10 | 8 | S1.2-03 | S |  |  |
| S1.2-04a | Subtask | Review all assessment documents for completeness | KA-01 | 3 | 3 | — | S | Data Quality Manager | R |
| S1.2-04b | Subtask | Conduct peer review sessions with Data Governance Lead | KA-01 | 3 | 3 | S1.2-04a | P | Data Governance Lead | R |
| S1.2-04c | Subtask | Validate regulatory alignment with Chief Compliance Officer | KA-05 | 2 | 2 | S1.2-04a | P | Chief Compliance Officer | R |
| S1.2-04d | Subtask | Finalize Governance Assessment Report | KA-01 | 2 | 2 | S1.2-04b | S | Business Analyst (Data) | R |
| S1.2-04e | Subtask | Prepare executive summary and presentation deck | KA-01 | 2 | 2 | S1.2-04d | S | Product Writer | R |

**Feature S1.2-A Subtotal**: 58 Man-Days, 43 SP (4 Tasks, 22 Subtasks)

##### Output Deliverable Traceability — Feature S1.2-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Governance Assessment Report | Must | Data Governance Analyst, Data Governance Manager, Business Analyst (Data) | Chief Data Officer (CDO) | Data Governance Manager | Compliance Officer (Data), Data Protection Officer (DPO), Project Manager (Data) | Chief Compliance Officer | Head of Business Management | output-deliverable-template.md |
| 2 | Regulatory Compliance Map | Must | Compliance Officer (Data), Chief Privacy Officer (CPO) | Chief Compliance Officer | Data Governance Manager | Data Protection Officer (DPO), Legal Counsel | Chief Data Officer (CDO) | Head of Business Management | output-deliverable-template.md |
| 3 | Gap Analysis Report | Must | Data Governance Analyst, Business Analyst (Data), Data Governance Manager | Chief Data Officer (CDO) | Compliance Officer (Data) | Chief Compliance Officer | Data Protection Officer (DPO) | Head of Business Management | output-deliverable-template.md |
| 4 | Governance Scope Document | Must | Data Governance Manager, Project Manager (Data), Product Writer | Chief Data Officer (CDO) | Change Manager (Data) | Head of Digital Branding & Communication | Project Manager | Head of Business Management | output-deliverable-template.md |

---

#### Feature S1.2-B: Governance Framework Design & Policy Development

**Milestone**: M2 — Governance Framework & Policies Draft Approved → Termin 2 (40%)  
**Lifecycle Stage**: Planning → Development (Define, Build)

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.2-05 | Task | Design governance organizational structure & RASCI | KA-01 | 18 | 15 | S1.2-03 | S |  |  |
| S1.2-05a | Subtask | Define governance bodies (Council, Working Groups) | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S1.2-05b | Subtask | Design RASCI matrix for data governance activities | KA-01 | 3 | 3 | S1.2-05a | P | Data Governance Analyst | R |
| S1.2-05c | Subtask | Define Data Owner & Data Steward roles per domain | KA-01 | 4 | 4 | S1.2-05a | P | Data Governance Manager | R |
| S1.2-05d | Subtask | Create governance operating model document | KA-01 | 4 | 4 | S1.2-05c | S | Business Analyst (Data) | R |
| S1.2-05e | Subtask | Review organizational structure with Chief Data & Analytics Officer (CDAO) | KA-01 | 2 | 2 | S1.2-05d | S | Chief Data & Analytics Officer (CDAO) | R |
| S1.2-05f | Subtask | Prepare governance structure presentation for Board | KA-01 | 2 | 2 | S1.2-05e | S | Head of Digital Branding & Communication | R |
| S1.2-06 | Task | Develop data policies & standards | KA-01 | 18 | 15 | S1.2-05 | S |  |  |
| S1.2-06a | Subtask | Draft master data policy | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S1.2-06b | Subtask | Develop data quality standards & thresholds | KA-11 | 3 | 3 | S1.2-06a | P | Data Quality Manager | R |
| S1.2-06c | Subtask | Develop data security & privacy policy (UU PDP aligned) | KA-05 | 4 | 4 | S1.2-06a | P | Data Protection Officer (DPO) | R |
| S1.2-06d | Subtask | Develop data classification scheme | KA-05 | 4 | 4 | S1.2-06a | P | Data Security Manager | R |
| S1.2-06e | Subtask | Conduct policy review workshops with Data Owners | KA-01 | 2 | 2 | S1.2-06d | S | Data Governance Lead | R |
| S1.2-06f | Subtask | Validate policies with Chief Privacy Officer (CPO) and Chief Data Security Officer | KA-05 | 2 | 2 | S1.2-06d | S | Chief Privacy Officer (CPO) | R |
| S1.2-07 | Task | Develop compliance framework & monitoring mechanisms | KA-05 | 14 | 12 | S1.2-06 | S |  |  |
| S1.2-07a | Subtask | Design compliance monitoring dashboard requirements | KA-05 | 3 | 3 | — | S | Compliance Officer (Data) | R |
| S1.2-07b | Subtask | Define governance KPIs & metrics | KA-01 | 3 | 3 | S1.2-07a | P | Data Governance Analyst | R |
| S1.2-07c | Subtask | Create audit procedures & escalation matrix | KA-05 | 3 | 3 | S1.2-07a | P | Compliance Officer (Data) | R |
| S1.2-07d | Subtask | Draft communication & training plan | KA-01 | 3 | 3 | S1.2-07a | P | Change Manager (Data) | R |
| S1.2-07e | Subtask | Conduct security review of compliance framework | KA-05 | 2 | 2 | S1.2-07c | P | Chief Information Security Officer (CISO) | R |
| S1.2-07f | Subtask | Prepare compliance framework presentation for Board | KA-05 | 2 | 2 | S1.2-07d | S | Head of Digital Branding & Communication | R |
| S1.2-08 | Task | Quality assurance & approval of governance framework | KA-01 | 10 | 8 | S1.2-07 | S |  |  |
| S1.2-08a | Subtask | Conduct internal QA review of framework documents | KA-01 | 3 | 3 | — | S | Data Quality Manager | R |
| S1.2-08b | Subtask | Facilitate approval workshops with Data Governance Lead | KA-01 | 3 | 3 | S1.2-08a | P | Data Governance Lead | R |
| S1.2-08c | Subtask | Obtain formal approval from Chief Data Officer (CDO) and Chief Compliance Officer | KA-01 | 2 | 2 | S1.2-08b | S | Chief Data Officer (CDO) | R |
| S1.2-08d | Subtask | Finalize framework documents and archive | KA-01 | 2 | 2 | S1.2-08c | S | Product Writer | R |

**Feature S1.2-B Subtotal**: 60 Man-Days, 45 SP (4 Tasks, 24 Subtasks)

##### Output Deliverable Traceability — Feature S1.2-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Data Governance Charter | Must | Data Governance Manager | Chief Data Officer (CDO) | Business Analyst (Data) | Head of Digital Branding & Communication | Project Manager (Data) | Head of Business Management | output-deliverable-template.md |
| 2 | Governance Operating Model | Must | Data Governance Manager, Business Analyst (Data) | Chief Data Officer (CDO) | Data Governance Analyst | Compliance Officer (Data) | Chief Compliance Officer | Head of Business Management | output-deliverable-template.md |
| 3 | RASCI Matrix | Must | Data Governance Analyst, Data Governance Manager | Chief Data Officer (CDO) | Business Analyst (Data) | Data Owner | Project Manager (Data) | Head of Business Management | output-deliverable-template.md |
| 4 | Data Policies (Master) | Must | Data Governance Manager | Chief Data Officer (CDO) | Compliance Officer (Data) | Legal Counsel | Chief Compliance Officer | Head of Business Management | output-deliverable-template.md |
| 5 | Data Quality Standards | Must | Data Quality Manager | Data Governance Manager | Data Governance Analyst | Data Owner | Chief Data Officer (CDO) | output-deliverable-template.md |
| 6 | Data Security & Privacy Policy | Must | Data Protection Officer (DPO) | Chief Data Officer (CDO) | Data Security Manager | Legal Counsel | Chief Compliance Officer | Head of Business Management | output-deliverable-template.md |
| 7 | Data Classification Scheme | Should | Data Security Manager | Data Protection Officer (DPO) | Data Governance Analyst | IT Manager | Chief Data Officer (CDO) | output-deliverable-template.md |
| 8 | Governance KPIs & Metrics | Should | Data Governance Analyst | Data Governance Manager | Data Analyst | Chief Data Officer (CDO) | Head of Business Management | output-deliverable-template.md |
| 9 | Communication & Training Plan | Should | Change Manager (Data) | Project Manager (Data) | Data Governance Manager | Chief Data Officer (CDO) | Head of Digital Branding & Communication | output-deliverable-template.md |

---

#### Feature S1.2-C: Validation, Socialization & Handover

**Milestone**: M3 — Governance Framework Approved & Socialized → Termin 3 (30%)  
**Lifecycle Stage**: Launch (Validate, Deploy, Handover)

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.2-09 | Task | Stakeholder validation & framework refinement | KA-01 | 14 | 12 | S1.2-08 | S |  |  |
| S1.2-09a | Subtask | Present framework to governance council | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S1.2-09b | Subtask | Conduct review workshops with Data Owners | KA-01 | 4 | 4 | S1.2-09a | P | Data Governance Analyst | R |
| S1.2-09c | Subtask | Incorporate feedback & finalize all documents | KA-01 | 4 | 4 | S1.2-09b | S | Business Analyst (Data) | R |
| S1.2-09d | Subtask | Obtain formal sign-off from Chief Data Officer (CDO) and sponsor | KA-01 | 3 | 3 | S1.2-09c | S | Project Manager (Data) | R |
| S1.2-10 | Task | Conduct governance socialization & initial training | KA-01 | 14 | 12 | S1.2-09 | S |  |  |
| S1.2-10a | Subtask | Develop socialization materials (deck, infographic) | KA-01 | 3 | 3 | — | S | Product Writer | R |
| S1.2-10b | Subtask | Conduct socialization sessions (3-4 batches) | KA-01 | 5 | 5 | S1.2-10a | S | Data Governance Manager | R |
| S1.2-10c | Subtask | Conduct hands-on training for Data Stewards | KA-01 | 3 | 3 | S1.2-10b | S | Data Literacy Champion | R |
| S1.2-10d | Subtask | Collect training feedback and prepare report | KA-01 | 3 | 3 | S1.2-10c | S | Business Analyst (Data) | R |
| S1.2-10e | Subtask | Coordinate training logistics and communications | KA-01 | 2 | 2 | S1.2-10a | S | Content Officer (Graphic Designer) | R |
| S1.2-11 | Task | Prepare implementation roadmap & handover | KA-01 | 12 | 10 | S1.2-10 | S |  |  |
| S1.2-11a | Subtask | Create governance implementation timeline | KA-01 | 3 | 3 | — | S | Project Manager (Data) | R |
| S1.2-11b | Subtask | Compile final document package | KA-01 | 3 | 3 | S1.2-11a | S | Product Writer | R |
| S1.2-11c | Subtask | Conduct knowledge transfer session | KA-01 | 3 | 3 | S1.2-11b | S | Data Governance Manager | R |
| S1.2-11d | Subtask | Deliver final presentation & close-out | KA-01 | 3 | 3 | S1.2-11c | S | Chief Data Officer (CDO) | R |
| S1.2-12 | Task | Develop ethical data principles & stewardship plan | KA-12 | 15 | 13 | S1.2-11 | S |  |  |
| S1.2-12a | Subtask | Research industry ethical data practices | KA-12 | 4 | 4 | — | S | Data Governance Analyst | R |
| S1.2-12b | Subtask | Draft ethical principles document | KA-12 | 4 | 4 | S1.2-12a | P | Data Governance Manager | R |
| S1.2-12c | Subtask | Develop data stewardship plan per domain | KA-01 | 4 | 4 | S1.2-12a | P | Data Governance Analyst | R |
| S1.2-12d | Subtask | Review & align with organizational values | KA-12 | 3 | 3 | S1.2-12c | S | Change Manager (Data) | R |
| S1.2-12e | Subtask | Socialize ethical principles with Board and stakeholders | KA-12 | 2 | 2 | S1.2-12b | S | Chief Data Officer (CDO) | R |

**Feature S1.2-C Subtotal**: 45 Man-Days, 37 SP (4 Tasks, 15 Subtasks)

##### Output Deliverable Traceability — Feature S1.2-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Final Governance Framework (signed) | Must | Business Analyst (Data), Project Manager (Data) | Chief Data Officer (CDO) | Data Governance Manager | Head of Digital Branding & Communication | Client CxO | Head of Business Management | output-deliverable-template.md |
| 2 | Socialization Materials | Must | Product Writer | Project Manager (Data) | Data Governance Manager | Data Literacy Champion | Content Officer (Graphic Designer) | Head of Business Management | output-deliverable-template.md |
| 3 | Training Report & Attendance | Must | Data Governance Manager, Data Literacy Champion | Project Manager (Data) | Product Writer | Chief Data Officer (CDO) | Head of Business Management | output-deliverable-template.md |
| 4 | Implementation Roadmap | Must | Project Manager (Data) | Chief Data Officer (CDO) | Data Governance Manager | Business Analyst (Data) | Head of Business Management | output-deliverable-template.md |
| 5 | Final Document Package | Must | Product Writer | Project Manager (Data) | Business Analyst (Data) | Data Governance Manager | Head of Business Management | output-deliverable-template.md |
| 6 | Ethical Principles Document | Should | Data Governance Manager, Data Governance Analyst | Chief Data Officer (CDO) | Change Manager (Data) | Legal Counsel | Chief Compliance Officer | Head of Business Management | output-deliverable-template.md |
| 7 | Data Stewardship Plan | Should | Data Governance Analyst | Data Governance Manager | Data Owner | Data Steward | Chief Data Officer (CDO) | output-deliverable-template.md |

---

**S1.2-TOTAL**: **Data Governance & Compliance Framework** — **145 Man-Days, 125 SP** (3 Features, 14 Tasks, 56 Subtasks)

---

### Service 1.3: Data Maturity Assessment & Benchmarking (Epic)

**DAMA KAs**: KA-14 (Primary), KA-01  
**Lifecycle Stage**: Discovery → Planning  
**Methodology**: DAMA-DMBOK Maturity Model + Industry Benchmarking  
**Total Man-Days**: 92 | **Features**: 3 | **Tasks**: 13 | **Subtasks**: 42

---

#### Feature S1.3-A: Assessment Design & Data Collection

**Milestone**: M1 — Assessment Instruments Ready & Data Collected → Termin 1 (30%)  
**Lifecycle Stage**: Discovery (Identify, Assess)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.3-01 | Task | Design assessment framework & instruments | KA-14 | 15 | 10 | — | S |  |  |
| S1.3-01a | Subtask | Customize DAMA maturity model to client context | KA-14 | 3 | 3 | — | S | Data Governance Manager | RASCI: R |
| S1.3-01b | Subtask | Develop assessment questionnaire (14 KA × 5 levels) | KA-14 | 4 | 5 | S1.3-01a | P | Data Governance Analyst | RASCI: R |
| S1.3-01c | Subtask | Design interview guide for qualitative assessment | KA-14 | 2 | 2 | S1.3-01a | P | Business Analyst (Data) | RASCI: R |
| S1.3-01d | Subtask | Prepare scoring rubric & calibration guide | KA-14 | 3 | 3 | S1.3-01a | P | Data Governance Manager | RASCI: R |
| S1.3-01e | Subtask | Conduct security and compliance review of instruments | KA-01 | 3 | 3 | S1.3-01a | P | Chief Information Security Officer (CISO) | RASCI: R |
| S1.3-01f | Subtask | Validate instruments with Data Governance Lead and Data Privacy Officer | KA-14 | 2 | 2 | S1.3-01d | S | Data Governance Lead | RASCI: R |
| S1.3-02 | Task | Conduct assessment data collection | KA-14 | 18 | 15 | S1.3-01 | S |  |  |
| S1.3-02a | Subtask | Distribute questionnaires to target respondents | KA-14 | 2 | 2 | — | S | Project Manager (Data) | RASCI: R |
| S1.3-02b | Subtask | Conduct assessment interviews (10-15 sessions) | KA-14 | 6 | 8 | S1.3-02a | P | Data Governance Analyst | RASCI: R |
| S1.3-02c | Subtask | Collect & validate documentary evidence | KA-14 | 3 | 3 | S1.3-02b | S | Data Governance Analyst | RASCI: R |
| S1.3-02d | Subtask | Conduct data quality spot-checks (sampling) | KA-11 | 3 | 3 | S1.3-02a | P | Data Quality Analyst | RASCI: R |
| S1.3-02e | Subtask | Coordinate with Data Protection Officer (DPO) for compliance validation | KA-01 | 2 | 2 | S1.3-02c | S | Data Protection Officer (DPO) | RASCI: R |
| S1.3-02f | Subtask | Monitor and report progress to Chief Data Officer (CDO) and Project Manager | KA-14 | 2 | 2 | S1.3-02a | S | Project Manager (Data) | RASCI: R |
| S1.3-03 | Task | Quality assurance & data integrity check | KA-11 | 5 | 4 | S1.3-02 | S |  |  |
| S1.3-03a | Subtask | Perform data validation and consistency checks | KA-11 | 2 | 2 | — | S | Data Quality Analyst | RASCI: R |
| S1.3-03b | Subtask | Conduct peer review of collected data | KA-14 | 1 | 1 | S1.3-03a | S | Data Governance Analyst | RASCI: R |
| S1.3-03c | Subtask | Document data quality issues and remediation plans | KA-11 | 1 | 1 | S1.3-03a | S | Data Quality Manager | RASCI: R |
| S1.3-03d | Subtask | Review data security compliance with Chief Information Security Officer (CISO) | KA-01 | 1 | 1 | S1.3-03a | S | Chief Information Security Officer (CISO) | RASCI: R |

**Feature S1.3-A Subtotal**: 40 Man-Days, 34 SP (3 Tasks, 14 Subtasks)

##### Output Deliverable Traceability — Feature S1.3-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Assessment Questionnaire | Must | Data Governance Analyst | Data Governance Manager | Business Analyst (Data) | Chief Data Officer (CDO) | Chief Data Officer (CDO) | Client | output-deliverable-template.md |
| 2 | Scoring Rubric | Must | Data Governance Manager | Chief Data Officer (CDO) | Data Governance Analyst | — | Client | output-deliverable-template.md |
| 3 | Raw Assessment Data | Must | Data Governance Analyst | Project Manager (Data) | Data Quality Analyst | Data Governance Manager | — | output-deliverable-template.md |
| 4 | Security & Compliance Review Report | Must | Chief Information Security Officer (CISO) | Chief Data Officer (CDO) | Data Governance Manager | Data Protection Officer (DPO) | Project Manager (Data) | output-deliverable-template.md |
| 5 | Data Quality Assurance Report | Must | Data Quality Analyst | Data Quality Manager | Data Governance Analyst | Chief Information Security Officer (CISO) | Project Manager (Data) | output-deliverable-template.md |

---

#### Feature S1.3-B: Analysis, Scoring & Benchmarking

**Milestone**: M2 — Maturity Assessment Report & Benchmarking Complete → Termin 2 (45%)  
**Lifecycle Stage**: Planning (Analyze, Compare)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.3-04 | Task | Score maturity & analyze results | KA-14 | 18 | 15 | S1.3-03 | S |  |  |
| S1.3-04a | Subtask | Calibrate scores across assessors | KA-14 | 3 | 3 | — | S | Data Governance Manager | RASCI: R |
| S1.3-04b | Subtask | Score all 14 DAMA KAs (quantitative + qualitative) | KA-14 | 5 | 6 | S1.3-04a | S | Data Governance Analyst | RASCI: R |
| S1.3-04c | Subtask | Generate maturity spider chart & heat map | KA-14 | 3 | 3 | S1.3-04a | P | Data Visualization Specialist | RASCI: R |
| S1.3-04d | Subtask | Identify strengths, weaknesses & patterns | KA-14 | 3 | 3 | S1.3-04a | P | Data Governance Manager | RASCI: R |
| S1.3-04e | Subtask | Cross-validate findings with interview data | KA-14 | 2 | 2 | S1.3-04d | S | Business Analyst (Data) | RASCI: R |
| S1.3-05 | Task | Conduct industry benchmarking & gap analysis | KA-14 | 12 | 10 | S1.3-04 | S |  |  |
| S1.3-05a | Subtask | Research industry benchmarks for client sector | KA-14 | 4 | 4 | — | S | Business Analyst (Data) | RASCI: R |
| S1.3-05b | Subtask | Compare client scores against industry peers | KA-14 | 3 | 3 | S1.3-05a | S | Data Analyst | RASCI: R |
| S1.3-05c | Subtask | Identify critical gaps & improvement opportunities | KA-14 | 2 | 2 | S1.3-05a | P | Data Governance Manager | RASCI: R |
| S1.3-05d | Subtask | Prioritize improvements by impact & feasibility | KA-14 | 2 | 2 | S1.3-05a | P | Data Governance Manager | RASCI: R |
| S1.3-05e | Subtask | Conduct compliance check with Chief Compliance Officer | KA-01 | 1 | 1 | S1.3-05a | S | Chief Compliance Officer | RASCI: R |
| S1.3-06 | Task | Quality assurance & validation of analysis | KA-14 | 5 | 4 | S1.3-05 | S |  |  |
| S1.3-06a | Subtask | Peer review of scoring and benchmarking results | KA-14 | 2 | 2 | — | S | Data Governance Analyst | RASCI: R |
| S1.3-06b | Subtask | Validate benchmarking data sources and methodology | KA-14 | 2 | 2 | S1.3-06a | S | Data Quality Analyst | RASCI: R |
| S1.3-06c | Subtask | Document validation findings and recommendations | KA-14 | 1 | 1 | S1.3-06b | S | Data Governance Manager | RASCI: R |
| S1.3-07 | Task | Prepare interim review with executive stakeholders | KA-14 | 4 | 3 | S1.3-06 | S |  |  |
| S1.3-07a | Subtask | Draft interim analysis report | KA-14 | 2 | 2 | — | S | Business Analyst (Data) | RASCI: R |
| S1.3-07b | Subtask | Design presentation deck for executive review | KA-14 | 1 | 1 | S1.3-07a | P | Data Visualization Specialist | RASCI: R |
| S1.3-07c | Subtask | Present findings to Chief Data Officer (CDO) and Chief Data & Analytics Officer (CDAO) | KA-14 | 1 | 1 | S1.3-07b | S | Chief Data Officer (CDO) | RASCI: R |

**Feature S1.3-B Subtotal**: 44 Man-Days, 32 SP (4 Tasks, 21 Subtasks)

##### Output Deliverable Traceability — Feature S1.3-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Maturity Scorecard (Spider Chart) | Must | Data Governance Analyst, Data Visualization Specialist | Data Governance Manager | Business Analyst (Data) | Chief Data Officer (CDO) | Chief Data & Analytics Officer (CDAO) | Client | output-deliverable-template.md |
| 2 | Capability Heat Map | Must | Data Visualization Specialist | Data Governance Manager | Data Governance Analyst | Chief Data Officer (CDO) | Chief Data & Analytics Officer (CDAO) | Client | output-deliverable-template.md |
| 3 | Benchmarking Report | Must | Business Analyst (Data), Data Analyst | Data Governance Manager | Data Governance Analyst | Chief Data Officer (CDO) | Chief Data & Analytics Officer (CDAO) | Client | output-deliverable-template.md |
| 4 | Gap Analysis Report | Must | Data Governance Manager | Chief Data Officer (CDO) | Data Governance Analyst | Business Analyst (Data) | Client | output-deliverable-template.md |
| 5 | Compliance Check Report | Must | Chief Compliance Officer | Chief Data Officer (CDO) | Data Governance Manager | Project Manager (Data) | Client | output-deliverable-template.md |
| 6 | Interim Review Presentation | Must | Business Analyst (Data), Data Visualization Specialist | Chief Data Officer (CDO) | Data Governance Manager | Chief Data & Analytics Officer (CDAO) | Client | pitch-deck-template.md |

---

#### Feature S1.3-C: Reporting, Recommendations & Presentation

**Milestone**: M3 — Final Assessment Presented & Improvement Roadmap Delivered → Termin 3 (25%)  
**Lifecycle Stage**: Planning → Launch (Recommend, Present)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.3-08 | Task | Develop improvement roadmap & recommendations | KA-14 | 14 | 12 | S1.3-05 | S |  |  |
| S1.3-08a | Subtask | Define target maturity levels per KA (1-3 year) | KA-14 | 3 | 3 | — | S | Data Governance Manager | RASCI: R |
| S1.3-08b | Subtask | Design phased improvement roadmap | KA-14 | 3 | 3 | S1.3-08a | P | Project Manager (Data) | RASCI: R |
| S1.3-08c | Subtask | Estimate resource & investment requirements | KA-14 | 3 | 3 | S1.3-08b | S | Business Analyst (Data) | RASCI: R |
| S1.3-08d | Subtask | Define quick wins vs long-term initiatives | KA-14 | 2 | 2 | S1.3-08a | P | Data Governance Manager | RASCI: R |
| S1.3-08e | Subtask | Conduct risk assessment & mitigation planning | KA-01 | 3 | 3 | S1.3-08b | S | Chief Privacy Officer (CPO) | RASCI: R |
| S1.3-09 | Task | Prepare & deliver executive presentation | KA-14 | 10 | 8 | S1.3-08 | S |  |  |
| S1.3-09a | Subtask | Compile final assessment report | KA-14 | 3 | 3 | — | S | Business Analyst (Data) | RASCI: R |
| S1.3-09b | Subtask | Design executive presentation deck | KA-14 | 3 | 3 | S1.3-09a | P | Data Visualization Specialist | RASCI: R |
| S1.3-09c | Subtask | Present to C-Level & obtain feedback | KA-14 | 2 | 2 | S1.3-09b | S | Chief Data Officer (CDO) | RASCI: R |
| S1.3-09d | Subtask | Incorporate feedback and finalize report | KA-14 | 2 | 2 | S1.3-09c | S | Business Analyst (Data) | RASCI: R |
| S1.3-10 | Task | Knowledge transfer & close-out | KA-14 | 8 | 6 | S1.3-09 | S |  |  |
| S1.3-10a | Subtask | Compile all assessment artifacts & deliverables | KA-14 | 3 | 3 | — | S | Product Writer | RASCI: R |
| S1.3-10b | Subtask | Conduct knowledge transfer session with client teams | KA-14 | 3 | 3 | S1.3-10a | S | Data Governance Manager | RASCI: R |
| S1.3-10c | Subtask | Project close-out & lessons learned documentation | KA-14 | 2 | 2 | S1.3-10b | S | Project Manager (Data) | RASCI: R |
| S1.3-10d | Subtask | Develop training materials for client adoption | KA-14 | 2 | 2 | S1.3-10b | S | Content Officer (Writer) | RASCI: R |
| S1.3-10e | Subtask | Coordinate post-project communication & feedback | KA-14 | 1 | 1 | S1.3-10c | S | Account Manager | RASCI: R |

**Feature S1.3-C Subtotal**: 28 Man-Days, 24 SP (3 Tasks, 17 Subtasks)

##### Output Deliverable Traceability — Feature S1.3-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Maturity Assessment Report (Final) | Must | Business Analyst (Data), Business Analyst (Data) | Chief Data Officer (CDO) | Data Governance Manager, Data Governance Analyst | Client CxO | Client | service-description-template.md |
| 2 | Improvement Roadmap | Must | Data Governance Manager, Project Manager (Data) | Chief Data Officer (CDO) | Business Analyst (Data) | Client CxO | Client | output-deliverable-template.md |
| 3 | Executive Presentation | Must | Data Visualization Specialist, Chief Data Officer (CDO) | Project Manager (Data) | Business Analyst (Data) | Data Governance Manager | Client | pitch-deck-template.md |
| 4 | Current State Analysis | Must | Business Analyst (Data) | Data Governance Manager | Data Governance Analyst | Chief Data Officer (CDO) | Client | output-deliverable-template.md |
| 5 | Knowledge Transfer Package | Must | Product Writer | Chief Data Officer (CDO) | Data Governance Manager | Content Officer (Writer) | Account Manager | knowledge-transfer-template.md |
| 6 | Training Materials | Must | Content Officer (Writer) | Chief Data Officer (CDO) | Data Governance Manager | Project Manager (Data) | Client | output-deliverable-template.md |

---

**S1.3-TOTAL**: **Data Maturity Assessment & Benchmarking** — **92 Man-Days, 90 SP** (3 Features, 13 Tasks, 42 Subtasks)

---

### Service 1.4: Data Governance & Policy Framework Development (Epic)

**DAMA KAs**: KA-01 (Primary), KA-09, KA-11  
**Lifecycle Stage**: Discovery → Development → Launch  
**Methodology**: DAMA-DMBOK Policy Framework + Regulatory Alignment  
**Total Man-Days**: 230 | **Features**: 3 | **Tasks**: 16 | **Subtasks**: 75

---

#### Feature S1.4-A: Policy Landscape Assessment & Standards Inventory

**Milestone**: M1 — Policy Assessment & Standards Gap Report → Termin 1 (30%)  
**Lifecycle Stage**: Discovery (Identify, Assess)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.4-01 | Task | Assess existing policies, standards & metadata practices | KA-01 | 15 | 10 | — | S |  |  |
| S1.4-01a | Subtask | Inventory all existing data policies & SOPs | KA-01 | 3 | 3 | — | S | Data Governance Analyst | R |
| S1.4-01b | Subtask | Review metadata management current state | KA-09 | 3 | 3 | S1.4-01a | P | Metadata Manager | R |
| S1.4-01c | Subtask | Assess data quality management practices | KA-11 | 3 | 3 | S1.4-01a | P | Data Quality Manager | R |
| S1.4-01d | Subtask | Map regulatory requirements to policy gaps | KA-05 | 3 | 3 | S1.4-01a | P | Compliance Officer (Data) | R |
| S1.4-01e | Subtask | Conduct security and privacy compliance review | KA-05 | 3 | 3 | S1.4-01a | P | Data Security Manager | R |
| S1.4-02 | Task | Conduct stakeholder workshops for requirements | KA-01 | 12 | 10 | S1.4-01 | S |  |  |
| S1.4-02a | Subtask | Design & facilitate policy requirements workshops (3 sessions) | KA-01 | 4 | 5 | — | S | Data Governance Manager | R |
| S1.4-02b | Subtask | Gather business rules from domain experts | KA-01 | 3 | 3 | S1.4-02a | S | Business Analyst (Data) | R |
| S1.4-02c | Subtask | Document data quality expectations per domain | KA-11 | 3 | 3 | S1.4-02b | S | Data Quality Analyst | R |
| S1.4-02d | Subtask | Validate stakeholder inputs with Data Stewardship Lead | KA-01 | 2 | 2 | S1.4-02b | S | Data Stewardship Lead | R |
| S1.4-02e | Subtask | Prepare workshop summary & action items report | KA-01 | 2 | 2 | S1.4-02a | S | Product Writer | R |
| S1.4-03 | Task | Develop metadata standards & data dictionary framework | KA-09 | 15 | 12 | S1.4-02 | S |  |  |
| S1.4-03a | Subtask | Define metadata taxonomy & classification | KA-09 | 3 | 3 | — | S | Metadata Manager | R |
| S1.4-03b | Subtask | Design data dictionary template & standards | KA-09 | 4 | 4 | S1.4-03a | P | Data Architect | R |
| S1.4-03c | Subtask | Define business glossary framework | KA-09 | 3 | 3 | S1.4-03a | P | Business Analyst (Data) | R |
| S1.4-03d | Subtask | Create metadata governance procedures | KA-09 | 2 | 2 | S1.4-03a | P | Data Governance Analyst | R |
| S1.4-03e | Subtask | Conduct metadata standards peer review | KA-09 | 3 | 3 | S1.4-03d | S | Data Architecture Manager | R |
| S1.4-03f | Subtask | Finalize metadata standards documentation | KA-09 | 2 | 2 | S1.4-03e | S | Product Writer | R |
| S1.4-04 | Task | Perform initial policy risk & compliance gap analysis | KA-05 | 10 | 8 | S1.4-03 | S |  |  |
| S1.4-04a | Subtask | Identify regulatory compliance risks | KA-05 | 3 | 3 | — | S | Compliance Officer (Data) | R |
| S1.4-04b | Subtask | Evaluate policy alignment with industry standards | KA-01 | 3 | 3 | S1.4-04a | P | Data Governance Manager | R |
| S1.4-04c | Subtask | Document risk mitigation recommendations | KA-05 | 2 | 2 | S1.4-04b | S | Data Security Manager | R |
| S1.4-04d | Subtask | Review findings with Chief Data Officer (CDO) | KA-01 | 2 | 2 | S1.4-04c | S | Chief Data Officer (CDO) | I |
| S1.4-04e | Subtask | Prepare Policy Assessment & Standards Gap Report | KA-01 | 2 | 2 | S1.4-04c | S | Product Writer | R |

**Feature S1.4-A Subtotal**: 62 Man-Days, 40 SP (5 Tasks, 24 Subtasks)

##### Output Deliverable Traceability — Feature S1.4-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Policy Inventory & Gap Report | Must | Data Governance Analyst, Compliance Officer (Data), Data Security Manager | Data Governance Manager | Business Analyst (Data) | Chief Data Officer (CDO) | Data Stewardship Lead | Chief Data Officer (CDO) | output-deliverable-template.md |
| 2 | Metadata Standards | Must | Metadata Manager, Data Architecture Manager | Data Governance Manager | Data Architect | Data Governance Analyst | Chief Data Officer (CDO) | service-description-template.md |
| 3 | Data Dictionary Framework | Must | Data Architect | Data Governance Manager | Metadata Manager | Business Analyst (Data) | Chief Data Officer (CDO) | service-description-template.md |
| 4 | Business Glossary Framework | Should | Business Analyst (Data) | Data Governance Manager | Metadata Manager | Data Owner | Chief Data Officer (CDO) | service-description-template.md |
| 5 | Stakeholder Requirements Document | Must | Data Governance Manager, Business Analyst (Data), Data Stewardship Lead | Project Manager (Data) | Data Quality Analyst | Chief Data Officer (CDO) | Account Manager | output-deliverable-template.md |

**RASCI Role Legend:**  
R = Responsible, A = Accountable, S = Support, C = Consulted, I = Informed

---

#### Feature S1.4-B: SOP Development & Data Quality Framework

**Milestone**: M2 — SOPs & Data Quality Framework Draft Approved → Termin 2 (40%)  
**Lifecycle Stage**: Development (Build)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.4-05 | Task | Develop SOPs — Data Lifecycle Management (SOP #1-#5) | KA-01 | 22 | 15 | S1.4-04 | S |  |  |
| S1.4-05a | Subtask | Draft SOP #1: Perencanaan dan Inventarisasi Data | KA-01 | 3 | 3 | — | S | Data Governance Analyst | R |
| S1.4-05b | Subtask | Draft SOP #2: Pengumpulan dan Akuisisi Data | KA-01 | 3 | 3 | S1.4-05a | P | Data Governance Analyst | R |
| S1.4-05c | Subtask | Draft SOP #3: Penyimpanan dan Klasifikasi Data | KA-04 | 3 | 3 | S1.4-05a | P | Data Engineer Lead | R |
| S1.4-05d | Subtask | Draft SOP #4: Pengarsipan dan Retensi Data | KA-04 | 3 | 3 | S1.4-05a | P | Data Governance Analyst | R |
| S1.4-05e | Subtask | Draft SOP #5: Pemusnahan Data | KA-04 | 3 | 3 | S1.4-05a | P | Compliance Officer (Data) | R |
| S1.4-05f | Subtask | Conduct internal review & harmonize lifecycle SOPs | KA-01 | 4 | 4 | S1.4-05e | S | Data Governance Manager | R |
| S1.4-06 | Task | Develop SOPs — Data Quality & Governance (SOP #6, #10, #11, #12) | KA-11 | 18 | 15 | S1.4-05 | S |  |  |
| S1.4-06a | Subtask | Draft SOP #6: Manajemen Kualitas Data | KA-11 | 4 | 5 | — | S | Data Quality Manager | R |
| S1.4-06b | Subtask | Draft SOP #10: Verifikasi dan Validasi Data | KA-11 | 3 | 3 | S1.4-06a | P | Data Quality Analyst | R |
| S1.4-06c | Subtask | Draft SOP #11: Katalog Data dan Metadata | KA-09 | 4 | 4 | S1.4-06a | P | Metadata Manager | R |
| S1.4-06d | Subtask | Draft SOP #12: Audit Data | KA-14 | 3 | 3 | S1.4-06a | P | Data Governance Analyst | R |
| S1.4-06e | Subtask | Review & harmonize quality/governance SOPs | KA-01 | 4 | 3 | S1.4-06d | S | Data Governance Manager | R |
| S1.4-07 | Task | Develop SOPs — Data Access, Integration & Publication (SOP #7-#9) | KA-06 | 16 | 14 | S1.4-06 | S |  |  |
| S1.4-07a | Subtask | Draft SOP #7: Interoperabilitas Data dan API Lifecycle | KA-06 | 5 | 5 | — | S | Data Architect | R |
| S1.4-07b | Subtask | Draft SOP #8: Akses dan Pemanfaatan Data | KA-05 | 3 | 3 | S1.4-07a | P | Data Protection Officer (DPO) | R |
| S1.4-07c | Subtask | Draft SOP #9: Publikasi dan Diseminasi Data | KA-06 | 4 | 4 | S1.4-07a | P | Data Governance Analyst | R |
| S1.4-07d | Subtask | Review & harmonize access/integration SOPs | KA-01 | 4 | 2 | S1.4-07c | S | Data Governance Manager | R |
| S1.4-07e | Subtask | Conduct security & compliance check on access SOPs | KA-05 | 3 | 3 | S1.4-07d | S | Data Security Manager | R |
| S1.4-08 | Task | Develop SOPs — Security, Privacy & Compliance (SOP #13-#17) | KA-05 | 24 | 22 | S1.4-07 | S |  |  |
| S1.4-08a | Subtask | Draft SOP #13: Keamanan Informasi dan Respons Insiden | KA-05 | 5 | 5 | — | S | Data Security Manager | R |
| S1.4-08b | Subtask | Draft SOP #14: DPIA sesuai UU PDP | KA-12 | 5 | 5 | S1.4-08a | P | Data Protection Officer (DPO) | R |
| S1.4-08c | Subtask | Draft SOP #15: Key Management dan Enkripsi Data | KA-05 | 4 | 4 | S1.4-08a | P | Data Security Manager | R |
| S1.4-08d | Subtask | Draft SOP #16: Data Masking/Pseudonymization/Tokenization | KA-05 | 4 | 4 | S1.4-08a | P | Data Security Manager | R |
| S1.4-08e | Subtask | Draft SOP #17: DSAR Management (Data Subject Access Request) | KA-12 | 3 | 3 | S1.4-08a | P | Data Protection Officer (DPO) | R |
| S1.4-08f | Subtask | Review & harmonize security/privacy SOPs | KA-01 | 3 | 3 | S1.4-08e | S | Data Governance Manager | R |
| S1.4-09 | Task | Develop data quality framework & rules | KA-11 | 18 | 15 | S1.4-06 | S |  |  |
| S1.4-09a | Subtask | Define data quality dimensions & metrics | KA-11 | 4 | 4 | — | S | Data Quality Manager | R |
| S1.4-09b | Subtask | Develop data quality rules per data domain | KA-11 | 5 | 5 | S1.4-09a | P | Data Quality Analyst | R |
| S1.4-09c | Subtask | Design data quality monitoring procedures | KA-11 | 3 | 3 | S1.4-09a | P | Data Quality Manager | R |
| S1.4-09d | Subtask | Define data quality issue resolution workflow | KA-11 | 3 | 2 | S1.4-09a | P | Data Governance Analyst | R |
| S1.4-09e | Subtask | Create data quality scorecard template | KA-11 | 3 | 1 | S1.4-09d | S | Data Analyst | R |
| S1.4-09f | Subtask | Conduct quality assurance review of framework | KA-11 | 3 | 3 | S1.4-09e | S | Data Quality Lead | R |
| S1.4-10 | Task | Develop business rules & data standards | KA-01 | 15 | 10 | S1.4-09 | S |  |  |
| S1.4-10a | Subtask | Document business rules per data domain | KA-01 | 5 | 5 | — | S | Business Analyst (Data) | R |
| S1.4-10b | Subtask | Define data naming conventions & standards | KA-01 | 3 | 2 | S1.4-10a | P | Data Architect | R |
| S1.4-10c | Subtask | Define data format & encoding standards | KA-01 | 3 | 2 | S1.4-10a | P | Data Architect | R |
| S1.4-10d | Subtask | Create data standards compliance checklist | KA-01 | 2 | 1 | S1.4-10a | P | Data Governance Analyst | R |
| S1.4-10e | Subtask | Conduct compliance validation with Chief Compliance Officer | KA-05 | 2 | 2 | S1.4-10d | S | Chief Compliance Officer | C |

**Feature S1.4-B Subtotal**: 103 Man-Days, 84 SP (6 Tasks, 41 Subtasks)

##### Output Deliverable Traceability — Feature S1.4-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Data Lifecycle SOPs (#1-#5) | Must | Data Governance Analyst, Data Engineer Lead, Compliance Officer (Data) | Data Governance Manager | Business Analyst (Data) | Data Owner | Chief Data Officer (CDO) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 2 | Data Quality & Governance SOPs (#6,#10,#11,#12) | Must | Data Quality Manager, Metadata Manager, Data Governance Analyst | Data Governance Manager | Business Analyst (Data) | Chief Data Officer (CDO) | Data Quality Lead | service-description-template.md |
| 3 | Data Access & Integration SOPs (#7-#9) | Must | Data Architect, Data Protection Officer (DPO), Data Governance Analyst | Data Governance Manager | Business Analyst (Data) | Data Owner | Chief Data Officer (CDO) | service-description-template.md |
| 4 | Security & Privacy SOPs (#13-#17) | Must | Data Security Manager, Data Protection Officer (DPO) | Data Governance Manager | Compliance Officer (Data) | Chief Compliance Officer | Chief Data Officer (CDO) | service-description-template.md |
| 5 | Data Quality Framework | Must | Data Quality Manager, Data Quality Lead | Data Governance Manager | Data Governance Analyst | Chief Data Officer (CDO) | Data Analyst | output-deliverable-template.md |
| 6 | Business Rules & Data Standards Document | Must | Business Analyst (Data), Data Architect, Data Governance Analyst | Data Governance Manager | Chief Compliance Officer | Chief Data Officer (CDO) | Account Manager | output-deliverable-template.md |

**RASCI Role Legend:**  
R = Responsible, A = Accountable, S = Support, C = Consulted, I = Informed

---

#### Feature S1.4-C: Review, Socialization & Handover

**Milestone**: M3 — All Policies & SOPs Finalized & Socialized → Termin 3 (30%)  
**Lifecycle Stage**: Launch (Validate, Deploy, Handover)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.4-11 | Task | Stakeholder review & policy refinement | KA-01 | 12 | 10 | S1.4-10 | S |  |  |
| S1.4-11a | Subtask | Conduct policy review workshops (2-3 sessions) | KA-01 | 4 | 4 | — | S | Data Governance Manager | R |
| S1.4-11b | Subtask | Incorporate feedback & finalize all documents | KA-01 | 4 | 3 | S1.4-11a | S | Data Governance Analyst | R |
| S1.4-11c | Subtask | Obtain formal approval from governance council | KA-01 | 2 | 3 | S1.4-11b | S | Project Manager (Data) | R |
| S1.4-11d | Subtask | Present final policies to Chief Data Officer (CDO) and CEO | KA-01 | 2 | 2 | S1.4-11c | S | Chief Data Officer (CDO) | I |
| S1.4-12 | Task | Conduct policy socialization & training | KA-01 | 15 | 12 | S1.4-11 | S |  |  |
| S1.4-12a | Subtask | Develop socialization materials & quick-reference guides | KA-01 | 4 | 3 | — | S | Product Writer | R |
| S1.4-12b | Subtask | Conduct socialization sessions (4-5 batches) | KA-01 | 5 | 5 | S1.4-12a | S | Data Governance Manager | R |
| S1.4-12c | Subtask | Conduct hands-on training for Data Stewards | KA-01 | 4 | 4 | S1.4-12b | S | Data Literacy Champion | R |
| S1.4-12d | Subtask | Collect training feedback & prepare report | KA-01 | 2 | 2 | S1.4-12c | S | Content Officer (Writer) | R |
| S1.4-13 | Task | Develop content management & retention policies | KA-07 | 12 | 10 | S1.4-12 | S |  |  |
| S1.4-13a | Subtask | Define content lifecycle management procedures | KA-07 | 4 | 3 | — | S | Data Governance Analyst | R |
| S1.4-13b | Subtask | Develop data retention & archiving policy | KA-04 | 4 | 4 | S1.4-13a | P | Data Governance Manager | R |
| S1.4-13c | Subtask | Define data disposal procedures & audit trail | KA-04 | 3 | 2 | S1.4-13a | P | Compliance Officer (Data) | R |
| S1.4-13d | Subtask | Conduct compliance review with Chief Compliance Officer | KA-05 | 1 | 1 | S1.4-13b | S | Chief Compliance Officer | C |
| S1.4-14 | Task | Final handover & close-out | KA-01 | 11 | 9 | S1.4-13 | S |  |  |
| S1.4-14a | Subtask | Compile final document package (all policies, SOPs, standards) | KA-01 | 3 | 3 | — | S | Product Writer | R |
| S1.4-14b | Subtask | Conduct knowledge transfer session | KA-01 | 4 | 3 | S1.4-14a | S | Data Governance Manager | R |
| S1.4-14c | Subtask | Project close-out, lessons learned & recommendations | KA-01 | 4 | 3 | S1.4-14b | S | Project Manager (Data) | R |
| S1.4-14d | Subtask | Inform Board and stakeholders of project completion | KA-01 | 1 | 1 | S1.4-14c | S | Chief Data Officer (CDO) | I |

**Feature S1.4-C Subtotal**: 50 Man-Days, 36 SP (4 Tasks, 16 Subtasks)

##### Output Deliverable Traceability — Feature S1.4-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Final Policy & SOP Package (signed) | Must | Data Governance Analyst, Project Manager (Data) | Chief Data Officer (CDO) | Data Governance Manager | Business Analyst (Data) | Chief Compliance Officer | CEO | output-deliverable-template.md |
| 2 | Socialization Materials | Must | Product Writer | Project Manager (Data) | Data Governance Manager | Content Officer (Writer) | Account Manager | Chief Data Officer (CDO) | service-description-template.md |
| 3 | Training Report & Attendance | Must | Data Governance Manager, Data Literacy Champion | Project Manager (Data) | Product Writer | Chief Data Officer (CDO) | Account Manager | Chief Data Officer (CDO) | output-deliverable-template.md |
| 4 | Content Management Policy | Should | Data Governance Analyst | Data Governance Manager | Compliance Officer (Data) | Data Owner | Chief Compliance Officer | service-description-template.md |
| 5 | Data Retention & Archiving Policy | Should | Data Governance Manager, Compliance Officer (Data) | Chief Data Officer (CDO) | Data Governance Analyst | Legal Counsel | Chief Compliance Officer | service-description-template.md |
| 6 | Knowledge Transfer Report | Must | Data Governance Manager, Project Manager (Data) | Chief Data Officer (CDO) | Product Writer | Account Manager | IT Operations Lead | knowledge-transfer-template.md |

**RASCI Role Legend:**  
R = Responsible, A = Accountable, S = Support, C = Consulted, I = Informed

---

**S1.4-TOTAL**: **Data Governance & Policy Framework Development** — **215 Man-Days, 160 SP** (3 Features, 16 Tasks, 75 Subtasks)

---

### Service 1.5: Data Asset Valuation & Monetization Advisory (Epic)

**DAMA KAs**: KA-01 (Primary), KA-02, KA-11, KA-14
**Lifecycle Stage**: Discovery → Planning
**Methodology**: Infonomics 6-Model Framework + COPQ Analysis + DAMA Data Valuation
**Total Man-Days**: 125 | **Features**: 3 | **Tasks**: 12 | **Subtasks**: 54

#### Feature S1.5-A: Data Asset Discovery & Inventory

**Milestone**: M1 — Data Asset Inventory & Prioritization Report → Termin 1 (30%)
**Lifecycle Stage**: Discovery (Identify, Assess)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.5-01 | Task | Conduct data asset inventory across domains | KA-01 | 16 | 13 | — | S | | |
| S1.5-01a | Subtask | Define data asset classification schema | KA-01 | 3 | 3 | — | S | Data Governance Lead | R |
| S1.5-01b | Subtask | Identify and catalog all data domains and assets | KA-01 | 4 | 5 | S1.5-01a | S | Data Governance Analyst | R |
| S1.5-01c | Subtask | Profile data assets (volume, velocity, variety, quality) | KA-11 | 4 | 3 | S1.5-01b | P | Data Quality Analyst | R |
| S1.5-01d | Subtask | Map data lineage and dependencies for critical assets | KA-02 | 3 | 2 | S1.5-01b | P | Data Architect | R |
| S1.5-01e | Subtask | Validate inventory with Data Stewards and business owners | KA-01 | 2 | 2 | S1.5-01d | S | Data Steward | R |
| S1.5-02 | Task | Stakeholder value alignment workshops | KA-01 | 12 | 8 | S1.5-01 | S | | |
| S1.5-02a | Subtask | Prepare workshop materials and agenda | KA-01 | 2 | 2 | — | S | Business Analyst (Data) | R |
| S1.5-02b | Subtask | Facilitate data value identification workshops (2 sessions) | KA-01 | 4 | 3 | S1.5-02a | S | Data Governance Manager | R |
| S1.5-02c | Subtask | Map business processes and strategic objectives to data assets | KA-02 | 3 | 2 | S1.5-02b | S | Business Analyst (Data) | R |
| S1.5-02d | Subtask | Document workshop outcomes and prioritized data domains | KA-01 | 3 | 2 | S1.5-02c | S | Project Manager | R |
| S1.5-03 | Task | Conduct COPQ (Cost of Poor Quality) baseline analysis | KA-11 | 12 | 8 | S1.5-01 | P | | |
| S1.5-03a | Subtask | Identify and define critical data quality dimensions | KA-11 | 2 | 2 | — | S | Data Quality Manager | R |
| S1.5-03b | Subtask | Quantify cost of poor data quality per prioritized domain | KA-11 | 4 | 3 | S1.5-03a | S | Data Quality Analyst | R |
| S1.5-03c | Subtask | Estimate revenue impact and opportunity cost of data quality issues | KA-11 | 4 | 3 | S1.5-03b | S | Business Analyst (Data) | R |
| S1.5-03d | Subtask | Compile and present COPQ analysis report to stakeholders | KA-11 | 2 | 2 | S1.5-03c | S | Data Quality Manager | R |
| S1.5-04 | Task | Conduct Security and Compliance Review | KA-01 | 10 | 8 | S1.5-01 | P | | |
| S1.5-04a | Subtask | Assess data security risks for inventoried assets | KA-01 | 3 | 3 | — | S | Security Engineer | R |
| S1.5-04b | Subtask | Review compliance with relevant regulations (e.g., PDP, SPBE) | KA-01 | 4 | 3 | S1.5-04a | S | Data Protection Officer (DPO) | R |
| S1.5-04c | Subtask | Document security and compliance findings and recommendations | KA-01 | 3 | 2 | S1.5-04b | S | AI Governance Analyst | R |

**Feature S1.5-A Subtotal**: 50 Man-Days, 37 SP (4 Tasks, 16 Subtasks)

##### Output Deliverable Traceability — Feature S1.5-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Data Asset Inventory & Classification | Must | S1.5-01b, S1.5-01d | Data Governance Analyst, Data Architect | Chief Data Officer (CDO) | Data Steward | Business Analyst (Data) | CTO | KA-01/01 |
| 2 | COPQ Analysis Report | Must | S1.5-03d | Data Quality Manager | Chief Data Officer (CDO) | Business Analyst (Data) | Data Quality Analyst | CEO | KA-11/02 |
| 3 | Data Domain Prioritization Matrix | Must | S1.5-02d | Project Manager | Chief Data Officer (CDO) | Data Governance Manager | Business Analyst (Data) | Account Manager | — |
| 4 | Security & Compliance Assessment | Must | S1.5-04c | AI Governance Analyst | CTO | Security Engineer, Data Protection Officer (DPO) | Data Governance Lead | Chief Data Officer (CDO) | output-deliverable-template.md |

##### RASCI Role Legend — Feature S1.5-A

*   **R**: Data Governance Analyst, Data Architect, Project Manager, Data Quality Manager, AI Governance Analyst
*   **A**: Chief Data Officer (CDO), CTO
*   **S**: Data Steward, Data Governance Manager, Business Analyst (Data), Security Engineer, Data Protection Officer (DPO)
*   **C**: Business Analyst (Data), Data Quality Analyst, Data Governance Lead
*   **I**: CTO, CEO, Account Manager, Chief Data Officer (CDO)

#### Feature S1.5-B: Data Asset Valuation (Infonomics 6-Model)

**Milestone**: M2 — Data Valuation Report → Termin 2 (40%)
**Lifecycle Stage**: Planning (Analyze, Quantify)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.5-05 | Task | Apply Intrinsic & Business Value models | KA-01 | 15 | 13 | S1.5-03 | S | | |
| S1.5-05a | Subtask | Calculate Intrinsic Value Factor (IVF) based on quality, scarcity | KA-11 | 4 | 3 | — | S | Data Quality Manager | R |
| S1.5-05b | Subtask | Calculate Business Value Factor (BVF) based on relevance, utility | KA-01 | 5 | 5 | S1.5-05a | S | Business Analyst (Data) | R |
| S1.5-05c | Subtask | Calculate Performance Value Factor (PVF) based on impact on KPIs | KA-14 | 4 | 3 | S1.5-05a | P | Data Valuation Specialist | R |
| S1.5-05d | Subtask | Validate valuation models with finance and business units | KA-01 | 2 | 2 | S1.5-05c | S | Data Governance Manager | R |
| S1.5-06 | Task | Apply Economic & Market Value models | KA-01 | 15 | 13 | S1.5-05 | S | | |
| S1.5-06a | Subtask | Calculate Cost Value Factor (CVF) based on acquisition/replacement cost | KA-01 | 4 | 3 | — | S | Data Governance Analyst | R |
| S1.5-06b | Subtask | Calculate Market Value Factor (MVF) based on external benchmarks | KA-01 | 5 | 5 | S1.5-06a | S | Business Analyst (Data) | R |
| S1.5-06c | Subtask | Calculate Economic Value Factor (EVF) based on revenue generation/cost savings | KA-01 | 4 | 3 | S1.5-06a | P | Data Valuation Specialist | R |
| S1.5-06d | Subtask | Perform sensitivity analysis on valuation results | KA-01 | 2 | 2 | S1.5-06c | S | Data Analyst | R |
| S1.5-07 | Task | Synthesize valuation results and compile report | KA-01 | 12 | 8 | S1.5-06 | S | | |
| S1.5-07a | Subtask | Consolidate 6-model results into a unified valuation dashboard | KA-01 | 4 | 3 | — | S | Data Visualization Specialist | R |
| S1.5-07b | Subtask | Write detailed Data Valuation Report with methodology and findings | KA-01 | 5 | 3 | S1.5-07a | S | Data Governance Manager | R |
| S1.5-07c | Subtask | Develop executive summary for C-level audience | KA-01 | 3 | 2 | S1.5-07b | S | Chief Data Officer (CDO) | R |
| S1.5-08 | Task | Quality Assurance and Peer Review | KA-11 | 6 | 5 | S1.5-07 | S | | |
| S1.5-08a | Subtask | Conduct peer review of valuation models and calculations | KA-01 | 3 | 3 | — | S | Data Scientist | R |
| S1.5-08b | Subtask | Validate report findings with data owners and stewards | KA-01 | 3 | 2 | S1.5-08a | S | Data Steward | R |

**Feature S1.5-B Subtotal**: 48 Man-Days, 39 SP (4 Tasks, 14 Subtasks)

##### Output Deliverable Traceability — Feature S1.5-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | Data Valuation Report (Infonomics 6-Model) | Must | S1.5-07b | Data Governance Manager | Chief Data Officer (CDO) | Data Valuation Specialist, Business Analyst (Data) | Data Quality Manager | CEO | output-deliverable-template.md |
| 6 | Data Value Dashboard | Should | S1.5-07a | Data Visualization Specialist | Chief Data Officer (CDO) | Data Governance Analyst | Data Analyst | Project Manager | — |

##### RASCI Role Legend — Feature S1.5-B

*   **R**: Data Quality Manager, Business Analyst (Data), Data Valuation Specialist, Data Governance Manager, Data Governance Analyst, Data Visualization Specialist, Chief Data Officer (CDO), Data Scientist, Data Steward
*   **A**: Chief Data Officer (CDO)
*   **S**: Data Valuation Specialist, Business Analyst (Data)
*   **C**: Data Quality Manager, Data Analyst
*   **I**: CEO, Project Manager

#### Feature S1.5-C: Monetization Strategy & Value Communication

**Milestone**: M3 — Monetization Strategy & Executive Presentation → Termin 3 (30%)
**Lifecycle Stage**: Planning (Strategize, Communicate)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S1.5-09 | Task | Develop data monetization strategy | KA-01 | 15 | 13 | S1.5-07 | S | | |
| S1.5-09a | Subtask | Brainstorm and identify monetization opportunities (direct/indirect) | KA-01 | 4 | 3 | — | S | Data Valuation Specialist | R |
| S1.5-09b | Subtask | Design potential data products and service offerings | KA-01 | 5 | 5 | S1.5-09a | S | Product Manager | R |
| S1.5-09c | Subtask | Develop business models and pricing for new offerings | KA-01 | 4 | 3 | S1.5-09b | S | Business Analyst (Data) | R |
| S1.5-09d | Subtask | Create a high-level value realization roadmap | KA-14 | 2 | 2 | S1.5-09c | S | Chief Data Officer (CDO) | R |
| S1.5-10 | Task | Prepare executive value communication materials | KA-01 | 12 | 8 | S1.5-09 | S | | |
| S1.5-10a | Subtask | Design executive presentation deck on valuation and monetization | KA-01 | 4 | 3 | — | S | Content Officer (Graphic Designer) | R |
| S1.5-10b | Subtask | Prepare detailed ROI projections and business case document | KA-01 | 5 | 3 | S1.5-10a | S | Business Analyst (Data) | R |
| S1.5-10c | Subtask | Rehearse and refine presentation with key stakeholders | KA-01 | 3 | 2 | S1.5-10b | S | Account Manager | R |
| S1.5-11 | Task | Final Deliverables and Knowledge Transfer | KA-01 | 10 | 8 | S1.5-10 | S | | |
| S1.5-11a | Subtask | Compile final Data Asset Register with valuation metrics | KA-01 | 3 | 3 | — | S | Data Governance Analyst | R |
| S1.5-11b | Subtask | Prepare Quality-Value Correlation Matrix and insights | KA-11 | 3 | 2 | S1.5-11a | P | Data Quality Analyst | R |
| S1.5-11c | Subtask | Create knowledge transfer documentation and user guides | KA-01 | 2 | 2 | S1.5-11b | S | Product Writer | R |
| S1.5-11d | Subtask | Conduct formal knowledge transfer session with client team | KA-01 | 2 | 2 | S1.5-11c | S | Data Governance Manager | R |
| S1.5-12 | Task | Final Presentation and Handover | KA-01 | 10 | 8 | S1.5-11 | S | | |
| S1.5-12a | Subtask | Facilitate executive value communication session with C-Suite | KA-01 | 3 | 3 | — | S | Chief Data Officer (CDO) | R |
| S1.5-12b | Subtask | Gather feedback and document next steps | KA-01 | 2 | 2 | S1.5-12a | S | Project Manager | R |
| S1.5-12c | Subtask | Archive project documentation and close out project | KA-01 | 2 | 2 | S1.5-12b | S | Project Management Officer | R |
| S1.5-12d | Subtask | Conduct post-project review and lessons learned session | KA-01 | 3 | 2 | S1.5-12c | S | Head of PMO | R |

**Feature S1.5-C Subtotal**: 47 Man-Days, 37 SP (4 Tasks, 16 Subtasks)

##### Output Deliverable Traceability — Feature S1.5-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 7 | Data Monetization Strategy & Roadmap | Should | S1.5-09d | Chief Data Officer (CDO) | CEO | Product Manager, Business Analyst (Data) | Data Valuation Specialist | CTO | output-deliverable-template.md |
| 8 | Executive Value Communication Deck | Must | S1.5-10a, S1.5-10b | Content Officer (Graphic Designer), Business Analyst (Data) | Chief Data Officer (CDO) | Account Manager | Data Governance Manager | Project Manager | output-deliverable-template.md |
| 9 | Final Data Asset Register (with Value) | Should | S1.5-11a | Data Governance Analyst | Chief Data Officer (CDO) | Data Quality Analyst | Data Steward | Metadata Manager | KA-12/01 |
| 10 | Knowledge Transfer Package | Must | S1.5-11c, S1.5-11d | Product Writer, Data Governance Manager | Project Manager | Chief Data Officer (CDO) | Data Steward | Client Team | knowledge-transfer-template.md |

##### RASCI Role Legend — Feature S1.5-C

*   **R**: Data Valuation Specialist, Product Manager, Business Analyst (Data), Chief Data Officer (CDO), Content Officer (Graphic Designer), Account Manager, Data Governance Analyst, Data Quality Analyst, Product Writer, Data Governance Manager, Project Manager, Project Management Officer, Head of PMO
*   **A**: CEO, Chief Data Officer (CDO), Project Manager
*   **S**: Product Manager, Business Analyst (Data), Account Manager, Chief Data Officer (CDO), Data Quality Analyst
*   **C**: Data Valuation Specialist, Data Governance Manager, Data Steward
*   **I**: CTO, Project Manager, Metadata Manager, Client Team

---

**S1.5-TOTAL**: **Data Asset Valuation & Monetization Advisory** — **145 Man-Days, 113 SP** (12 Tasks, 46 Subtasks)

---

---

## Pillar 2: Platform & Solution Implementation

### Service 2.1: Data Governance Framework Implementation (Epic)

**DAMA KAs:** Data Governance, Data Quality
**Lifecycle Stage:** Plan & Design
**Methodology:** DAMA-DMBOK
**Total Man-Days:** 42

---

#### Feature 2.1.1: Establish Data Governance Roles & Responsibilities

| ID   | Task/Subtask                                             | Role                      | RASCI | Man-Days | SP |
|------|----------------------------------------------------------|---------------------------|-------|----------|----|
| T1   | Define Data Governance Roles                             |                           |       | 4.0      | 5  |
| S1.1 | Research industry best practices for data governance roles | Data Governance Manager   | R     | 1.0      | 1  |
| S1.2 | Draft role descriptions, responsibilities, and skill requirements | Data Governance Manager   | R     | 1.5      | 2  |
| S1.3 | Conduct workshop with key stakeholders to refine roles     | Project Manager           | R     | 1.0      | 1  |
| S1.4 | Finalize and obtain approval for role definitions        | Chief Data Officer (CDO)        | A     | 0.5      | 1  |
| T2   | Assign Individuals to Data Governance Roles              |                           |       | 4.0      | 5  |
| S2.1 | Identify and nominate suitable candidates for each role    | Data Governance Manager   | R     | 1.5      | 2  |
| S2.2 | Vet and interview shortlisted candidates                 | Chief Data Officer (CDO)        | R     | 1.5      | 2  |
| S2.3 | Formalize appointments and communicate to the organization | CEO   | A     | 0.5      | 1  |
| S2.4 | Conduct onboarding and orientation for appointed individuals | Project Manager           | R     | 0.5      | 1  |
| T3   | Develop Data Governance Communication Plan               |                           |       | 3.0      | 5  |
| S3.1 | Define communication objectives, messages, and audiences   | Project Manager           | R     | 1.0      | 2  |
| S3.2 | Create communication materials (presentations, newsletters) | Content Officer (Writer)s          | R     | 1.0      | 2  |
| S3.3 | Schedule and execute communication kick-off              | Account Manager           | R     | 0.5      | 1  |
| S3.4 | Establish ongoing communication channels (e.g., portal)  | Solution Architect        | R     | 0.5      | 1  |
| T4   | Perform Security and Compliance Review                   |                           |       | 2.0      | 3  |
| S4.1 | Assess roles for compliance with data privacy regulations  | Data Governance Manager   | R     | 1.0      | 1  |
| S4.2 | Review role permissions and access controls with security team | Data Engineer Lead        | R     | 1.0      | 2  |

**Deliverable Traceability**

| Deliverable                      | ID | R                       | A                         | S                  | C                   | I                         |
|----------------------------------|----|-------------------------|---------------------------|--------------------|---------------------|---------------------------|
| Role Definition Document         | D1 | Data Governance Manager | Chief Data Officer (CDO)        | Project Manager    | Data Steward        | CTO  |
| Governance Appointment Letters   | D2 | Project Manager         | CEO   | -                  | -                   | Account Manager           |
| Communication Plan & Materials   | D3 | Content Officer (Writer)s        | Project Manager           | Solution Architect | Account Manager     | Chief Data Officer (CDO)        |

***RASCI Role Legend:*** *Account Manager, Chief Data Officer (CDO), CEO, CTO, Content Officer (Writer)s, Data Engineer Lead, Data Governance Manager, Data Steward, Project Manager, Solution Architect*

---

#### Feature 2.1.2: Develop Foundational Data Governance Policies

| ID   | Task/Subtask                                               | Role                      | RASCI | Man-Days | SP |
|------|------------------------------------------------------------|---------------------------|-------|----------|----|
| T1   | Draft Data Quality Policy                                  |                           |       | 5.0      | 8  |
| S1.1 | Define data quality dimensions and metrics (e.g., accuracy)  | Data Quality Lead         | R     | 1.5      | 2  |
| S1.2 | Establish data quality measurement and reporting procedures  | Data Quality Analyst      | R     | 1.5      | 3  |
| S1.3 | Define thresholds and remediation protocols for data quality | Data Quality Lead         | R     | 1.0      | 2  |
| S1.4 | Secure policy approval from the Data Governance Council      | Chief Data Officer (CDO)        | A     | 1.0      | 1  |
| T2   | Draft Data Security & Access Control Policy                |                           |       | 5.0      | 8  |
| S2.1 | Classify data sensitivity levels (Public, Internal, etc.)    | Data Steward              | R     | 1.5      | 2  |
| S2.2 | Define access control rules based on roles and sensitivity   | Data Architect            | R     | 2.0      | 3  |
| S2.3 | Specify data encryption and masking requirements           | Data Engineer Lead        | R     | 1.0      | 2  |
| S2.4 | Review policy with legal and obtain executive sign-off       | CTO  | A     | 0.5      | 1  |
| T3   | Draft Data Lifecycle Management Policy                     |                           |       | 4.0      | 5  |
| S3.1 | Define data lifecycle stages (creation to archival/deletion) | Data Architect            | R     | 1.5      | 2  |
| S3.2 | Establish data retention and archival rules per data type    | Data Steward              | R     | 1.5      | 2  |
| S3.3 | Plan for secure data disposal and destruction              | Data Engineer Lead        | R     | 1.0      | 1  |
| T4   | Conduct Stakeholder Training on New Policies               |                           |       | 3.0      | 5  |
| S4.1 | Develop training materials and modules for each policy       | Content Officer (Writer)s          | R     | 1.5      | 2  |
| S4.2 | Schedule and conduct training sessions for all relevant staff | Project Manager           | R     | 1.0      | 2  |
| S4.3 | Gather feedback and create a training effectiveness report   | Business Analyst          | R     | 0.5      | 1  |
| T5   | Perform Quality Assurance and Policy Validation            |                           |       | 2.0      | 3  |
| S5.1 | Review policies for clarity, completeness, and consistency   | Business Analyst          | R     | 1.0      | 1  |
| S5.2 | Simulate policy application with test cases and scenarios    | Data Quality Analyst      | R     | 1.0      | 2  |

**Deliverable Traceability**

| Deliverable                        | ID | R                    | A                        | S                | C                       | I                               |
|------------------------------------|----|----------------------|--------------------------|------------------|-------------------------|---------------------------------|
| Data Quality Policy                | D4 | Data Quality Lead    | Chief Data Officer (CDO)       | Data Quality Analyst | Business Analyst        | Data Steward                    |
| Data Security & Access Policy      | D5 | Data Architect       | CTO | Data Engineer Lead | Data Steward            | Chief Artificial Intelligence Officer |
| Data Lifecycle Management Policy   | D6 | Data Architect       | Chief Data Officer (CDO)       | Data Steward     | Data Engineer Lead      | Solution Architect              |
| Policy Training Materials          | D7 | Content Officer (Writer)s     | Project Manager          | Business Analyst | -                       | -                               |

***RASCI Role Legend:*** *Business Analyst, Chief Artificial Intelligence Officer, Chief Data Officer (CDO), CTO, Content Officer (Writer)s, Data Architect, Data Engineer Lead, Data Quality Analyst, Data Quality Lead, Data Steward, Project Manager, Solution Architect*

---

**S2.1-TOTAL**: **Data Governance Framework Implementation** — **42 Man-Days, 60 SP** (2 Features, 9 Tasks, 25 Subtasks)

---

### Service 2.2: Data Quality Assessment (Epic)

**DAMA KAs**: Data Quality
**Lifecycle Stage**: Plan & Design
**Methodology**: DAMA-DMBOK
**Total Man-Days**: 25

#### Feature 2.2.1: Comprehensive Data Profiling

| ID | Task & Subtask | Role | RASCI | Man-Days | SP |
|---|---|---|---|---|---|
| T1 | **Define Data Profiling Scope & Strategy** | | | 2 | 3 |
| S1.1 | Identify critical data elements for profiling | Data Steward | R | 0.5 | 1 |
| S1.2 | Define data sources and access paths | Data Engineer Lead | R | 0.5 | 1 |
| S1.3 | Establish profiling frequency and schedule | Data Governance Manager | A | 0.5 | 1 |
| S1.4 | Get strategic approval for profiling scope | Chief Data Officer (CDO) | A | 0.5 | 1 |
| T2 | **Execute Automated Data Profiling** | | | 4 | 5 |
| S2.1 | Develop and configure profiling scripts | Data Engineer | R | 2 | 3 |
| S2.2 | Execute profiling scripts on defined schedule | Data Engineer | R | 1 | 1 |
| S2.3 | Monitor and log profiling execution | Data Quality Lead | C | 0.5 | 1 |
| S2.4 | Validate profiling output for completeness | Data Analyst | R | 0.5 | 1 |
| T3 | **Analyze Profiling Results & Document Findings** | | | 3 | 5 |
| S3.1 | Analyze column-level data types, lengths, and formats | Data Analyst | R | 1 | 2 |
| S3.2 | Identify key, dependency, and redundancy patterns | Data Analyst | R | 1 | 2 |
| S3.3 | Document data anomalies, outliers, and inconsistencies | Data Quality Analyst | R | 0.5 | 1 |
| S3.4 | Create initial data quality scorecard | Data Quality Lead | A | 0.5 | 1 |
| T4 | **Conduct Security and Compliance Review** | | | 2 | 3 |
| S4.1 | Review profiling process for data privacy compliance (GDPR/CCPA) | Data Governance Manager | A | 1 | 1 |
| S4.2 | Perform security assessment of profiling scripts and data access | CTO | A | 1 | 2 |

##### Deliverable Traceability

| Deliverable | ID | Template | R | A | S | C | I |
|---|---|---|---|---|---|---|---|
| Data Profiling Strategy | D1 | output-deliverable-template.md | Data Governance Manager | Chief Data Officer (CDO) | Data Steward | Data Engineer Lead | CEO |
| Data Profiling Execution Logs | D2 | | Data Engineer | Data Quality Lead | | Data Quality Analyst | Project Manager |
| Data Profiling Analysis Report | D3 | output-deliverable-template.md | Data Analyst | Data Quality Lead | Data Quality Analyst | Data Steward | Chief Data Officer (CDO) |

##### RASCI Role Legend
*   **R**: Data Steward, Data Engineer Lead, Data Engineer, Data Analyst, Data Quality Analyst
*   **A**: Data Governance Manager, Chief Data Officer (CDO), Data Quality Lead, CTO
*   **S**: Data Steward, Data Quality Analyst
*   **C**: Data Quality Lead, Data Steward
*   **I**: CEO, Project Manager, Chief Data Officer (CDO)

#### Feature 2.2.2: Data Quality Rule Design & Implementation

| ID | Task & Subtask | Role | RASCI | Man-Days | SP |
|---|---|---|---|---|---|
| T1 | **Define Business-Driven Data Quality Dimensions** | | | 2 | 3 |
| S1.1 | Facilitate workshop to identify business-critical quality dimensions | Business Analyst | R | 1 | 1 |
| S1.2 | Define and document dimensions (Accuracy, Completeness, Timeliness, etc.) | Data Governance Manager | A | 0.5 | 1 |
| S1.3 | Establish acceptable data quality thresholds with business stakeholders | Data Steward | A | 0.5 | 1 |
| T2 | **Develop & Formalize Data Quality Rules** | | | 4 | 5 |
| S2.1 | Translate business requirements into specific, measurable rule specifications | Data Analyst | R | 1.5 | 2 |
| S2.2 | Document rules in a centralized repository (Data Quality Rulebook) | Data Quality Analyst | R | 1 | 1 |
| S2.3 | Validate rules with data stewards and business users | Data Steward | C | 1 | 1 |
| S2.4 | Obtain formal sign-off on the Data Quality Rulebook | Chief Data Officer (CDO) | A | 0.5 | 1 |
| T3 | **Implement and Test Data Quality Rules** | | | 5 | 8 |
| S3.1 | Develop rule implementation logic in the target DQ tool/platform | Data Engineer | R | 2 | 3 |
| S3.2 | Create test cases and prepare test data for rule validation | Data Quality Analyst | R | 1 | 2 |
| S3.3 | Execute rule testing and document results | Data Quality Engineer | R | 1 | 2 |
| S3.4 | Remediate implementation defects and re-test | Data Engineer | R | 1 | 1 |
| T4 | **Plan for Knowledge Transfer and Training** | | | 3 | 3 |
| S4.1 | Develop training materials for data quality monitoring | Content Officer (Writer) | R | 1.5 | 1 |
| S4.2 | Schedule and organize training sessions for data stewards and analysts | Project Manager | A | 1 | 1 |
| S4.3 | Present the data quality framework to key stakeholders | Account Manager | R | 0.5 | 1 |

##### Deliverable Traceability

| Deliverable | ID | Template | R | A | S | C | I |
|---|---|---|---|---|---|---|---|
| Data Quality Dimension Matrix | D4 | output-deliverable-template.md | Business Analyst | Data Governance Manager | | Data Steward | Chief Data Officer (CDO) |
| Data Quality Rulebook | D5 | output-deliverable-template.md | Data Quality Analyst | Chief Data Officer (CDO) | Data Analyst | Data Steward | Project Manager |
| Data Quality Rule Test Report | D6 | | Data Quality Engineer | Data Quality Lead | | Data Engineer | Data Governance Manager |
| Knowledge Transfer Plan & Materials | D7 | knowledge-transfer-template.md | Content Officer (Writer) | Project Manager | Account Manager | | Chief AI Officer |

##### RASCI Role Legend
*   **R**: Business Analyst, Data Analyst, Data Quality Analyst, Data Engineer, Data Quality Engineer, Content Officer (Writer), Account Manager
*   **A**: Data Governance Manager, Data Steward, Chief Data Officer (CDO), Project Manager, Data Quality Lead
*   **S**: Data Analyst, Account Manager
*   **C**: Data Steward, Data Engineer
*   **I**: Chief Data Officer (CDO), Project Manager, Data Governance Manager, Chief AI Officer

**S2.2-TOTAL**: **Data Quality Assessment** — **25 Man-Days, 32 SP** (2 Features, 8 Tasks, 25 Subtasks)

---

### Service 2.3: Government Data Portal Platform (Epic)

**DAMA KAs**: KA-02 (Primary), KA-06, KA-13
**Lifecycle Stage**: Discovery → Development → Launch
**Methodology**: Dual-Track Agile + SPBE Compliance

#### Feature S2.3-A: Requirements & Portal Architecture Design

**Milestone**: M1 — Portal Architecture & UX Design Approved → Termin 1 (30%)
**Lifecycle Stage**: Discovery → Planning (Identify, Design)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.3-01 | Task | Gather requirements & analyze SPBE compliance needs | KA-02 | 18 | 13 | — | S | | |
| S2.3-01a | Subtask | Conduct stakeholder interviews (OPD heads, IT, Legal) | KA-02 | 5 | 5 | — | S | Business Analyst (Data) | R |
| S2.3-01b | Subtask | Map SPBE, Satu Data Indonesia, and other relevant regulations to portal features | KA-02 | 4 | 5 | S2.3-01a | P | Compliance Officer (Data) | R |
| S2.3-01c | Subtask | Analyze existing data sources, quality, and integration points | KA-06 | 5 | 5 | S2.3-01b | S | Data Architect | R |
| S2.3-01d | Subtask | Define portal user personas, roles, and access levels | KA-02 | 4 | 3 | S2.3-01a | P | Product Manager | R |
| S2.3-02 | Task | Design Portal Architecture & Data Model | KA-02 | 20 | 21 | S2.3-01 | S | | |
| S2.3-02a | Subtask | Design scalable multi-tenant application architecture | KA-02 | 6 | 8 | — | S | Data Architect | R |
| S2.3-02b | Subtask | Design DCAT-AP compliant metadata schema and data catalog model | KA-09 | 5 | 5 | S2.3-02a | P | Data Architect | R |
| S2.3-02c | Subtask | Design secure API architecture for data exchange and integration | KA-06 | 5 | 5 | S2.3-02a | P | Data Security Architect | R |
| S2.3-02d | Subtask | Design UX wireframes, user flows, and accessibility compliance (WCAG 2.1) | KA-02 | 4 | 5 | S2.3-02a | P | Product Designer | R |
| S2.3-03 | Task | Design Open Data Governance Framework & Socialization Plan | KA-01 | 16 | 13 | S2.3-02 | S | | |
| S2.3-03a | Subtask | Define open data policy, data classification, and licensing criteria | KA-01 | 5 | 5 | — | S | Data Governance Manager | R |
| S2.3-03b | Subtask | Define dataset publishing workflow, approval process, and stewardship roles | KA-01 | 4 | 5 | S2.3-03a | P | Data Governance Analyst | R |
| S2.3-03c | Subtask | Define data quality standards and validation rules for published datasets | KA-11 | 4 | 5 | S2.3-03a | P | Data Quality Manager | R |
| S2.3-03d | Subtask | Design portal usage monitoring, analytics, and reporting dashboards | KA-13 | 3 | 3 | S2.3-03a | P | Data Analyst | R |

**Feature S2.3-A Subtotal**: 54 Man-Days, 47 SP (3 Tasks, 12 Subtasks)

##### Output Deliverable Traceability — Feature S2.3-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Requirements & Compliance Specification | Must | S2.3-01a, S2.3-01b, S2.3-01d | Business Analyst (Data), Compliance Officer (Data) | Chief Data Officer (CDO) | Product Manager | Legal Counsel | CTO | - |
| 2 | Portal Architecture & Security Blueprint | Must | S2.3-02a, S2.3-02c | Data Architect, Data Security Architect | CTO | Data Engineer Lead | Chief Information Security Officer (CISO) | CEO | KA-02/02 |
| 3 | Metadata Schema & Data Catalog Design | Must | S2.3-02b | Data Architect | Data Governance Manager | Metadata Manager | Data Steward | - | KA-09/03 |
| 4 | UX Wireframes & User Flow Document | Must | S2.3-02d | Product Designer | Product Manager | Business Analyst (Data) | End Users | - | - |
| 5 | Open Data Governance Framework | Must | S2.3-03a, S2.3-03b, S2.3-03c | Data Governance Manager, Data Governance Analyst, Data Quality Manager | Chief Data Officer (CDO) | Data Steward | Legal Counsel | Head of OPD | KA-01/02 |

> **RASCI Role Legend**: Business Analyst (Data), Chief Data Officer (CDO), CEO, Chief Information Security Officer (CISO), CTO, Compliance Officer (Data), Data Architect, Data Engineer Lead, Data Governance Analyst, Data Governance Manager, Data Quality Manager, Data Security Architect, Data Steward, End Users, Head of OPD, Legal Counsel, Metadata Manager, Product Designer, Product Manager

---

#### Feature S2.3-B: Portal Development & Data Integration

**Milestone**: M2 — Portal Core Features & Data Integration Complete → Termin 2 (40%)
**Lifecycle Stage**: Development (Build)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.3-04 | Task | Develop Portal Back-End & API Services | KA-06 | 28 | 21 | S2.3-03 | S | | |
| S2.3-04a | Subtask | Setup development environment, CI/CD pipeline, and version control | KA-04 | 4 | 5 | — | S | Site Reliability Engineer (DevOps) | R |
| S2.3-04b | Subtask | Implement dataset CRUD, versioning, and metadata management APIs | KA-06 | 6 | 8 | S2.3-04a | S | Product Engineering Back-End Engineer | R |
| S2.3-04c | Subtask | Implement search, filter, and discovery features using a search engine (e.g., Elasticsearch) | KA-06 | 5 | 5 | S2.3-04b | S | Product Engineering Back-End Engineer | R |
| S2.3-04d | Subtask | Implement user authentication (SSO), authorization, and RBAC | KA-05 | 5 | 5 | S2.3-04b | P | Security Engineer | R |
| S2.3-04e | Subtask | Implement data download, API access endpoints, and rate limiting | KA-06 | 4 | 5 | S2.3-04b | P | Product Engineering Back-End Engineer | R |
| S2.3-04f | Subtask | Implement dataset publishing workflow engine and notification service | KA-06 | 4 | 3 | S2.3-04e | S | Product Engineering Back-End Engineer | R |
| S2.3-05 | Task | Develop Portal Front-End (UI/UX) | KA-02 | 26 | 21 | S2.3-04 | P | | |
| S2.3-05a | Subtask | Implement responsive portal landing page, navigation, and content pages | KA-02 | 5 | 5 | — | S | Product Engineering Front-End Engineer | R |
| S2.3-05b | Subtask | Implement dataset catalog, search UI, and filtering components | KA-02 | 6 | 8 | S2.3-05a | S | Product Engineering Front-End Engineer | R |
| S2.3-05c | Subtask | Implement dataset detail page with metadata, previews, and lineage visualization | KA-02 | 5 | 5 | S2.3-05b | P | Product Engineering Front-End Engineer | R |
| S2.3-05d | Subtask | Implement interactive data visualization components (charts, maps) | KA-13 | 5 | 5 | S2.3-05b | P | Data Visualization Specialist | R |
| S2.3-05e | Subtask | Implement admin panel for user management, dataset management, and governance | KA-02 | 5 | 5 | S2.3-05d | S | Product Engineering Front-End Engineer | R |
| S2.3-06 | Task | Implement Data Integration & Quality Pipelines | KA-06 | 24 | 21 | S2.3-04 | S | | |
| S2.3-06a | Subtask | Develop data harvesting/ingestion pipelines from various OPD sources (API, DB, files) | KA-06 | 7 | 8 | — | S | Data Engineer | R |
| S2.3-06b | Subtask | Implement data quality validation, cleansing, and transformation logic in pipelines | KA-11 | 6 | 8 | S2.3-06a | S | Data Quality Engineer | R |
| S2.3-06c | Subtask | Implement automated metadata extraction and cataloging | KA-09 | 5 | 5 | S2.3-06b | S | Data Engineer | R |
| S2.3-06d | Subtask | Implement geospatial data processing and indexing | KA-10 | 4 | 5 | S2.3-06a | P | Geospatial Engineer | R |
| S2.3-06e | Subtask | Develop pipeline scheduler, monitoring, and error handling framework | KA-04 | 2 | 2 | S2.3-06c | S | Data Engineer | R |

**Feature S2.3-B Subtotal**: 78 Man-Days, 63 SP (3 Tasks, 15 Subtasks)

##### Output Deliverable Traceability — Feature S2.3-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Working Portal Application (Backend & Frontend) | Must | S2.3-04b to S2.3-05e | Product Engineering Back-End Engineer, Product Engineering Front-End Engineer | CTO | Product Manager | Product Designer | CEO | - |
| 2 | CI/CD Pipeline & DevOps Automation | Must | S2.3-04a | Site Reliability Engineer (DevOps) | CTO | Data Engineer Lead | - | - | - |
| 3 | API Documentation (Developer Portal) | Must | S2.3-04b, S2.3-04e | Product Writer | Product Manager | Product Engineering Back-End Engineer | - | - | KA-06/10 |
| 4 | Data Integration Pipelines & Scheduler | Must | S2.3-06a to S2.3-06e | Data Engineer, Data Quality Engineer | Data Engineer Lead | Data Architect | Data Steward | - | - |

> **RASCI Role Legend**: CEO, CTO, Data Architect, Data Engineer, Geospatial Engineer, Data Engineer Lead, Data Quality Engineer, Security Engineer, Data Steward, Data Visualization Specialist, Product Designer, Product Engineering Back-End Engineer, Product Engineering Front-End Engineer, Product Manager, Product Writer, Site Reliability Engineer (DevOps)

---

#### Feature S2.3-C: Testing, Deployment & Handover

**Milestone**: M3 — Portal Go-Live & Handover Complete → Termin 3 (30%)
**Lifecycle Stage**: Launch (Test, Deploy, Handover)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.3-07 | Task | Conduct Comprehensive Testing & Security Audit | KA-06 | 24 | 21 | S2.3-06 | S | | |
| S2.3-07a | Subtask | Develop test strategy, test cases, and test data | KA-06 | 5 | 5 | — | S | Product Engineering QA Analyst | R |
| S2.3-07b | Subtask | Execute functional, integration, and regression testing | KA-06 | 6 | 8 | S2.3-07a | S | Product Engineering QA Analyst | R |
| S2.3-07c | Subtask | Conduct performance, load, and stress testing | KA-04 | 5 | 5 | S2.3-07b | S | Site Reliability Engineer (DevOps) | R |
| S2.3-07d | Subtask | Conduct security audit, penetration testing, and SPBE compliance validation | KA-05 | 6 | 8 | S2.3-07b | S | Data Security Manager | R |
| S2.3-07e | Subtask | Triage, prioritize, and manage bug fixing process | KA-06 | 2 | 2 | S2.3-07d | S | Product Manager | R |
| S2.3-08 | Task | Conduct UAT & Production Deployment | KA-02 | 20 | 21 | S2.3-07 | S | | |
| S2.3-08a | Subtask | Prepare UAT environment and user guides | KA-02 | 4 | 3 | — | S | Product Engineering QA Analyst | R |
| S2.3-08b | Subtask | Facilitate UAT sessions with OPD representatives and end-users | KA-02 | 5 | 5 | S2.3-08a | S | Business Analyst (Data) | R |
| S2.3-08c | Subtask | Analyze UAT feedback, fix critical issues, and re-test | KA-02 | 4 | 5 | S2.3-08b | S | Product Engineering Back-End Engineer | R |
| S2.3-08d | Subtask | Develop production deployment plan and rollback strategy | KA-04 | 3 | 3 | S2.3-08c | S | Site Reliability Engineer (DevOps) | R |
| S2.3-08e | Subtask | Execute production deployment and post-deployment verification | KA-04 | 4 | 5 | S2.3-08d | S | Site Reliability Engineer (DevOps) | R |
| S2.3-09 | Task | Documentation, Training & Handover | KA-02 | 22 | 21 | S2.3-08 | S | | |
| S2.3-09a | Subtask | Write comprehensive technical documentation (architecture, APIs, operations) | KA-02 | 6 | 8 | — | S | Product Writer | R |
| S2.3-09b | Subtask | Create user documentation, admin guides, and FAQs | KA-02 | 5 | 5 | S2.3-09a | P | Product Writer | R |
| S2.3-09c | Subtask | Develop training materials (slides, videos) for OPD admins and data stewards | KA-02 | 5 | 5 | S2.3-09b | P | Data Literacy Champion | R |
| S2.3-09d | Subtask | Conduct training sessions (4-5 batches) and gather feedback | KA-02 | 6 | 8 | S2.3-09c | S | Data Literacy Champion | R |
| S2.3-10 | Task | Develop Data Publishing SOP & Sustainability Plan | KA-01 | 20 | 21 | S2.3-09 | S | | |
| S2.3-10a | Subtask | Develop detailed SOP for data publishing, quality checks, and approval by OPD | KA-01 | 6 | 8 | — | S | Data Governance Analyst | R |
| S2.3-10b | Subtask | Define portal sustainability, maintenance plan, and operational budget | KA-04 | 5 | 5 | S2.3-10a | P | Project Manager (Data) | R |
| S2.3-10c | Subtask | Define SLA, support escalation procedures, and helpdesk setup | KA-04 | 5 | 5 | S2.3-10a | P | Project Manager (Data) | R |
| S2.3-10d | Subtask | Conduct operational readiness review and formal handover to client's operational team | KA-04 | 4 | 5 | S2.3-10c | S | Chief Data Officer (CDO) | R |

**Feature S2.3-C Subtotal**: 86 Man-Days, 84 SP (4 Tasks, 18 Subtasks)

##### Output Deliverable Traceability — Feature S2.3-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Comprehensive Test Report (Functional, Performance, Security) | Must | S2.3-07b, S2.3-07c, S2.3-07d | Product Engineering QA Analyst, Data Security Manager | CTO | Site Reliability Engineer (DevOps) | - | Chief Information Security Officer (CISO) | KA-06/12 |
| 2 | UAT Report (Signed Off) | Must | S2.3-08b | Business Analyst (Data) | Project Manager (Data) | Product Engineering QA Analyst | Head of OPD | Chief Data Officer (CDO) | - |
| 3 | Technical & User Documentation Suite | Must | S2.3-09a, S2.3-09b | Product Writer | Project Manager (Data) | Data Architect | - | Client's IT Team | output-deliverable-template.md |
| 4 | Training Materials & Session Report | Must | S2.3-09c, S2.3-09d | Data Literacy Champion | Project Manager (Data) | Product Writer | Head of OPD | - | knowledge-transfer-template.md |
| 5 | Data Publishing SOP | Must | S2.3-10a | Data Governance Analyst | Data Governance Manager | Data Steward | - | - | KA-01/03 |
| 6 | Sustainability & Maintenance Plan | Should | S2.3-10b, S2.3-10c | Project Manager (Data) | Chief Data Officer (CDO) | Site Reliability Engineer (DevOps) | Client's Finance Dept | CEO | - |
| 7 | Final Handover & Project Closure Report | Must | S2.3-10d | Chief Data Officer (CDO) | CEO | Project Manager (Data) | - | - | - |

> **RASCI Role Legend**: Business Analyst (Data), Chief Data Officer (CDO), CEO, Chief Information Security Officer (CISO), CTO, Client's Finance Dept, Client's IT Team, Data Architect, Data Governance Analyst, Data Governance Manager, Data Literacy Champion, Data Security Manager, Data Steward, Head of OPD, Product Engineering QA Analyst, Product Writer, Project Manager (Data), Site Reliability Engineer (DevOps)

---

**S2.3-TOTAL**: **Government Data Portal Platform** — **218 Man-Days, 194 SP** (3 Features, 10 Tasks, 45 Subtasks)

---

### Service 2.4: Enterprise Data Portal & Self-Service Analytics (Epic)

**DAMA KAs**: KA-13 (Primary), KA-02, KA-09  
**Lifecycle Stage**: Discovery → Development → Launch  
**Methodology**: Dual-Track Agile + Self-Service BI  
**Total Man-Days**: 195 | **Features**: 3 | **Tasks**: 13 | **Subtasks**: 58

---

#### Feature S2.4-A: Analytics Requirements & Portal Architecture

**Milestone**: M1 — Analytics Architecture & Dashboard Design Approved → Termin 1 (30%)  
**Lifecycle Stage**: Discovery → Planning (Identify, Design)

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.4-01 | Task | Gather analytics requirements & define KPIs | KA-13 | 16 | 15 | — | S |  |  |
| S2.4-01a | Subtask | Conduct analytics needs assessment (8-10 interviews) | KA-13 | 5 | 5 | — | S | Business Analyst (Data) | R |
| S2.4-01b | Subtask | Define KPIs & metrics per business domain | KA-13 | 4 | 5 | S2.4-01a | P | Business Analyst (Data) | R |
| S2.4-01c | Subtask | Map data sources to KPIs & identify gaps | KA-13 | 3 | 3 | S2.4-01a | P | Data Analyst | R |
| S2.4-01d | Subtask | Define user personas & access levels for analytics | KA-13 | 2 | 2 | S2.4-01a | P | Product Manager | R |
| S2.4-01e | Subtask | Conduct compliance & privacy impact assessment | KA-09 | 2 | 3 | S2.4-01a | P | Data Privacy Officer | R |
| S2.4-01f | Subtask | Review analytics requirements with Chief Data Officer (CDO) | KA-13 | 0 | 0 | S2.4-01b | S | Chief Data Officer (CDO) | I |

| S2.4-02 | Task | Design analytics architecture & data mart model | KA-02 | 20 | 16 | S2.4-01 | S |  |  |
| S2.4-02a | Subtask | Design analytics architecture (OLAP, data mart) | KA-02 | 5 | 6 | — | S | Data Architect | R |
| S2.4-02b | Subtask | Design dimensional data model (star/snowflake) | KA-03 | 5 | 5 | S2.4-02a | P | Data Architect | R |
| S2.4-02c | Subtask | Define semantic layer & business metrics definitions | KA-13 | 4 | 5 | S2.4-02a | P | Business Analyst (Data) | R |
| S2.4-02d | Subtask | Design self-service analytics governance framework | KA-01 | 3 | 3 | S2.4-02a | P | Data Governance Manager | R |
| S2.4-02e | Subtask | Conduct security architecture review | KA-05 | 3 | 3 | S2.4-02a | P | Chief Information Security Officer (CISO) | R |
| S2.4-02f | Subtask | Present architecture design to Chief Data Architect | KA-02 | 0 | 0 | S2.4-02a | S | Chief Data Architect | I |

| S2.4-03 | Task | Design dashboard wireframes & visualization standards | KA-13 | 14 | 10 | S2.4-02 | S |  |  |
| S2.4-03a | Subtask | Design executive dashboard wireframes | KA-13 | 4 | 5 | — | S | Data Visualization Specialist | R |
| S2.4-03b | Subtask | Design operational dashboard wireframes | KA-13 | 4 | 5 | S2.4-03a | P | Data Visualization Specialist | R |
| S2.4-03c | Subtask | Define visualization standards & style guide | KA-13 | 2 | 2 | S2.4-03a | P | Data Visualization Specialist | R |
| S2.4-03d | Subtask | Validate designs with stakeholders | KA-13 | 2 | 2 | S2.4-03c | S | Business Analyst (Data) | R |
| S2.4-03e | Subtask | Coordinate design feedback session with Head of Product | KA-13 | 2 | 2 | S2.4-03d | S | Head of Product | I |

| S2.4-04 | Task | Define analytics portal security & compliance requirements | KA-05 | 6 | 6 | S2.4-03 | S |  |  |
| S2.4-04a | Subtask | Conduct portal security requirements workshop | KA-05 | 2 | 2 | — | S | Data Security Manager | R |
| S2.4-04b | Subtask | Define compliance controls & audit requirements | KA-09 | 2 | 2 | S2.4-04a | P | Chief Compliance Officer | R |
| S2.4-04c | Subtask | Document security & compliance requirements | KA-05 | 1 | 1 | S2.4-04b | P | Data Governance Officer | R |
| S2.4-04d | Subtask | Review & approve security requirements with CISO | KA-05 | 1 | 1 | S2.4-04c | S | Chief Information Security Officer (CISO) | A |
| S2.4-04e | Subtask | Communicate security requirements to Product Engineering Manager | KA-05 | 1 | 1 | S2.4-04d | I | Product Engineering Manager | I |

**Feature S2.4-A Subtotal**: 56 Man-Days, 41 SP (5 Tasks, 22 Subtasks)

##### Output Deliverable Traceability — Feature S2.4-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Analytics Requirements Document | Must | S2.4-01a, S2.4-01b, S2.4-01e | Business Analyst (Data) | Product Manager | Data Analyst | Data Privacy Officer | Chief Data Officer (CDO) | output-deliverable-template.md |
| 2 | Analytics Architecture Blueprint | Must | S2.4-02a, S2.4-02e | Data Architect | Chief Data Architect | Chief Information Security Officer (CISO) | Data Governance Manager | Chief Data Officer (CDO) | data-product-canvas-template.md |
| 3 | Dimensional Data Model | Must | S2.4-02b | Data Architect | Product Manager | Business Analyst (Data) | Data Governance Manager | Chief Data Architect | data-product-canvas-template.md |
| 4 | Semantic Layer Definition | Must | S2.4-02c | Business Analyst (Data) | Data Architect | Data Analyst | Data Governance Manager | Chief Data Officer (CDO) | output-deliverable-template.md |
| 5 | Dashboard Wireframes | Must | S2.4-03a, S2.4-03b | Data Visualization Specialist | Head of Product | Business Analyst (Data) | Chief Data Officer (CDO) | Head of Product | output-deliverable-template.md |
| 6 | Visualization Standards | Should | S2.4-03c | Data Visualization Specialist | Head of Product | Business Analyst (Data) | Product Designer | Head of Digital Branding & Communication | output-deliverable-template.md |
| 7 | Portal Security & Compliance Requirements | Must | S2.4-04a, S2.4-04b | Data Security Manager | Chief Information Security Officer (CISO) | Data Governance Officer | Chief Compliance Officer | Product Engineering Manager | output-deliverable-template.md |

---

#### Feature S2.4-B: Portal & Dashboard Development

**Milestone**: M2 — Analytics Portal & Dashboards Functional → Termin 2 (40%)  
**Lifecycle Stage**: Development (Build)

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.4-05 | Task | Build data mart & analytics data pipelines | KA-06 | 22 | 16 | S2.4-04 | S |  |  |
| S2.4-05a | Subtask | Implement data mart schema & ETL pipelines | KA-06 | 7 | 8 | — | S | Data Engineer | R |
| S2.4-05b | Subtask | Implement data aggregation & calculation logic | KA-06 | 5 | 5 | S2.4-05a | S | Data Engineer | R |
| S2.4-05c | Subtask | Implement data quality checks for analytics layer | KA-11 | 4 | 5 | S2.4-05b | S | Data Quality Engineer | R |
| S2.4-05d | Subtask | Configure semantic layer & metric definitions | KA-13 | 3 | 3 | S2.4-05a | P | BI Developer | R |
| S2.4-05e | Subtask | Conduct data pipeline security review | KA-05 | 3 | 3 | S2.4-05c | P | Security Engineer | R |

| S2.4-06 | Task | Develop dashboards & self-service analytics features | KA-13 | 26 | 22 | S2.4-05 | S |  |  |
| S2.4-06a | Subtask | Develop executive dashboards (3-5 dashboards) | KA-13 | 6 | 8 | — | S | BI Developer | R |
| S2.4-06b | Subtask | Develop operational dashboards (5-8 dashboards) | KA-13 | 8 | 8 | S2.4-06a | P | BI Developer | R |
| S2.4-06c | Subtask | Implement self-service query & exploration features | KA-13 | 5 | 5 | S2.4-06b | S | BI Developer | R |
| S2.4-06d | Subtask | Implement data export & scheduled reporting | KA-13 | 4 | 5 | S2.4-06a | P | BI Developer | R |
| S2.4-06e | Subtask | Conduct dashboard performance optimization | KA-04 | 3 | 3 | S2.4-06c | P | Product Engineering QA Analyst | R |

| S2.4-07 | Task | Implement portal features & access management | KA-02 | 18 | 15 | S2.4-06 | S |  |  |
| S2.4-07a | Subtask | Develop analytics portal UI & navigation | KA-02 | 5 | 6 | — | S | Product Engineering Front-End Engineer | R |
| S2.4-07b | Subtask | Implement role-based access & row-level security | KA-05 | 5 | 6 | S2.4-07a | S | Product Engineering Back-End Engineer | R |
| S2.4-07c | Subtask | Implement embedded analytics & iframe integration | KA-13 | 4 | 4 | S2.4-07b | S | BI Developer | R |
| S2.4-07d | Subtask | Implement usage analytics & audit logging | KA-13 | 4 | 4 | S2.4-07a | P | Product Engineering Back-End Engineer | R |

| S2.4-08 | Task | Conduct portal security & compliance testing | KA-05 | 8 | 7 | S2.4-07 | S |  |  |
| S2.4-08a | Subtask | Perform security penetration testing | KA-05 | 3 | 3 | — | S | Security Engineer | R |
| S2.4-08b | Subtask | Conduct compliance audit & reporting | KA-09 | 2 | 2 | S2.4-08a | P | Chief Compliance Officer | R |
| S2.4-08c | Subtask | Validate access control & data privacy features | KA-05 | 2 | 2 | S2.4-08b | P | Data Security Officer | R |
| S2.4-08d | Subtask | Report security & compliance test results to CISO | KA-05 | 1 | 1 | S2.4-08c | S | Chief Information Security Officer (CISO) | I |

**Feature S2.4-B Subtotal**: 74 Man-Days, 60 SP (4 Tasks, 23 Subtasks)

##### Output Deliverable Traceability — Feature S2.4-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Data Mart (operational) | Must | S2.4-05a, S2.4-05b | Data Engineer | Product Manager | Data Analyst | Database Administrator | Chief Data Officer (CDO) | output-deliverable-template.md |
| 2 | Executive Dashboards | Must | S2.4-06a | BI Developer | Product Manager | Data Visualization Specialist | Business Analyst (Data) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 3 | Operational Dashboards | Must | S2.4-06b | BI Developer | Product Manager | Data Visualization Specialist | Business Analyst (Data) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 4 | Self-Service Analytics Features | Must | S2.4-06c, S2.4-06d | BI Developer | Product Manager | Product Engineering Front-End Engineer | Business Analyst (Data) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 5 | Analytics Portal Application | Must | S2.4-07a to S2.4-07d | Product Engineering Front-End Engineer, Product Engineering Back-End Engineer | Product Manager | BI Developer | Product Engineering QA Analyst | Chief Data Officer (CDO) | output-deliverable-template.md |
| 6 | Portal Security & Compliance Test Report | Must | S2.4-08a, S2.4-08b | Security Engineer | Chief Information Security Officer (CISO) | Chief Compliance Officer | Data Security Officer | Product Manager | output-deliverable-template.md |

---

#### Feature S2.4-C: Testing, Training & Go-Live

**Milestone**: M3 — Analytics Portal Go-Live & Handover Complete → Termin 3 (30%)  
**Lifecycle Stage**: Launch (Test, Deploy, Handover)

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.4-09 | Task | Conduct testing & UAT | KA-13 | 18 | 15 | S2.4-08 | S |  |  |
| S2.4-09a | Subtask | Execute functional & data accuracy testing | KA-13 | 5 | 5 | — | S | Product Engineering QA Analyst | R |
| S2.4-09b | Subtask | Conduct performance testing (concurrent users) | KA-04 | 4 | 4 | S2.4-09a | S | Site Reliability Engineer (DevOps) | R |
| S2.4-09c | Subtask | Facilitate UAT with business users | KA-13 | 5 | 5 | S2.4-09b | S | Business Analyst (Data) | R |
| S2.4-09d | Subtask | Fix findings & regression testing | KA-13 | 4 | 5 | S2.4-09a | P | BI Developer | R |

| S2.4-10 | Task | Conduct analytics training & adoption program | KA-13 | 22 | 17 | S2.4-09 | S |  |  |
| S2.4-10a | Subtask | Develop analytics training curriculum | KA-13 | 5 | 5 | — | S | Data Literacy Champion | R |
| S2.4-10b | Subtask | Conduct executive dashboard training (2 sessions) | KA-13 | 4 | 4 | S2.4-10a | S | Data Visualization Specialist | R |
| S2.4-10c | Subtask | Conduct self-service analytics training (3-4 batches) | KA-13 | 6 | 6 | S2.4-10b | S | Data Literacy Champion | R |
| S2.4-10d | Subtask | Create analytics user guide & FAQ | KA-13 | 3 | 3 | S2.4-10a | P | Product Writer | R |
| S2.4-10e | Subtask | Set up analytics community of practice | KA-13 | 4 | 4 | S2.4-10d | S | Data Literacy Champion | R |
| S2.4-10f | Subtask | Develop training feedback & improvement plan | KA-13 | 2 | 2 | S2.4-10e | P | Business Development & Operations Lead | R |

| S2.4-11 | Task | Production deployment & handover | KA-04 | 16 | 14 | S2.4-10 | S |  |  |
| S2.4-11a | Subtask | Execute production deployment | KA-04 | 4 | 4 | — | S | Site Reliability Engineer (DevOps) | R |
| S2.4-11b | Subtask | Post-deployment monitoring & stabilization | KA-04 | 5 | 5 | S2.4-11a | S | Site Reliability Engineer (DevOps) | R |
| S2.4-11c | Subtask | Compile technical documentation & handover package | KA-02 | 4 | 4 | S2.4-11b | S | Product Writer | R |
| S2.4-11d | Subtask | Project close-out & lessons learned | KA-02 | 3 | 3 | S2.4-11a | P | Project Manager (Data) | R |

| S2.4-12 | Task | Develop analytics governance & sustainability plan | KA-01 | 23 | 20 | S2.4-11 | S |  |  |
| S2.4-12a | Subtask | Define analytics governance procedures | KA-01 | 6 | 6 | — | S | Data Governance Manager | R |
| S2.4-12b | Subtask | Define dashboard lifecycle management process | KA-13 | 6 | 6 | S2.4-12a | P | BI Developer | R |
| S2.4-12c | Subtask | Define data refresh SLA & monitoring procedures | KA-04 | 5 | 5 | S2.4-12a | P | Site Reliability Engineer (DevOps) | R |
| S2.4-12d | Subtask | Conduct operational readiness review | KA-04 | 4 | 4 | S2.4-12a | P | Data Architect | R |
| S2.4-12e | Subtask | Present governance plan to Chief Data & Analytics Officer (CDAO) | KA-01 | 2 | 2 | S2.4-12a | S | Chief Data & Analytics Officer (CDAO) | A |
| S2.4-12f | Subtask | Communicate governance plan to Project Manager | KA-01 | 2 | 2 | S2.4-12a | I | Project Manager (Data) | I |

**Feature S2.4-C Subtotal**: 65 Man-Days, 54 SP (4 Tasks, 23 Subtasks)

##### Output Deliverable Traceability — Feature S2.4-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Test & UAT Report | Must | S2.4-09a to S2.4-09c | Product Engineering QA Analyst, Business Analyst (Data) | Product Manager | BI Developer | Site Reliability Engineer (DevOps) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 2 | Training Materials & Curriculum | Must | S2.4-10a, S2.4-10d | Data Literacy Champion, Product Writer | Product Manager | Data Visualization Specialist | Data Governance Manager | Head of Digital Branding & Communication | knowledge-transfer-template.md |
| 3 | Training Report & Attendance | Must | S2.4-10b, S2.4-10c | Data Visualization Specialist, Data Literacy Champion | Product Manager | Product Writer | Chief Data Officer (CDO) | Business Development & Operations Lead | knowledge-transfer-template.md |
| 4 | Analytics Governance Procedures | Should | S2.4-12a, S2.4-12b | Data Governance Manager, BI Developer | Chief Data & Analytics Officer (CDAO) | Data Governance Analyst | Business Analyst (Data) | Project Manager (Data) | data-product-canvas-template.md |
| 5 | Final Handover Package | Must | S2.4-11c, S2.4-11d | Product Writer, Project Manager (Data) | Chief Data Officer (CDO) | Data Architect | Business Analyst (Data) | Client | output-deliverable-template.md |

---

**S2.4-TOTAL**: **Enterprise Data Portal & Self-Service Analytics** — **195 Man-Days, 155 SP** (3 Features, 13 Tasks, 58 Subtasks)

---

### Service 2.5: Secure & Trusted Data Exchange — API Gateway Platform (Epic)

| Aspek | Detail |
| :--- | :--- |
| **DAMA KAs** | KA-05 (Data Security), KA-06 (Data Integration & Interoperability) |
| **Lifecycle Stage** | Development (Digital); Design, Build (Data Product) |
| **Methodology** | Scrum/Kanban, API-first Design, DevSecOps |
| **Est. Total Effort** | 65 Man-Days |

---

### Feature S2.5-F1: API Gateway Platform Foundation

**Description:** This feature focuses on establishing the core infrastructure, security posture, and operational readiness of the API Gateway platform. It ensures a scalable, secure, and well-governed foundation is in place before onboarding any APIs.

**Tasks & Subtasks**

| ID | Task / Subtask | Role | RASCI | Man-Days | SP |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **S2.5-F1.T1** | **Platform Scoping and Design** | | | **8** | **13** |
| S2.5-F1.T1.1 | Conduct stakeholder workshops to define business drivers, technical requirements, and success criteria | Business Analyst | R | 2 | 3 |
| S2.5-F1.T1.2 | Analyze existing infrastructure and security landscape to identify integration points and constraints | Solution Architect | R | 2 | 3 |
| S2.5-F1.T1.3 | Develop the high-level architecture and technology stack recommendation for the API Gateway | CTO | A | 1 | 2 |
| S2.5-F1.T1.4 | Create detailed design documents, including data flow diagrams and component specifications | Data Architect | R | 2 | 3 |
| S2.5-F1.T1.5 | Present design to the Architecture Review Board for approval | Solution Architect | A | 1 | 2 |
| **S2.5-F1.T2** | **Infrastructure Setup and Configuration** | | | **10** | **16** |
| S2.5-F1.T2.1 | Provision cloud or on-premise infrastructure (servers, networking, storage) | DevOps Engineer | R | 3 | 5 |
| S2.5-F1.T2.2 | Install and configure the chosen API Gateway software (e.g., Kong, Apigee, Tyk) | API Engineer | R | 3 | 5 |
| S2.5-F1.T2.3 | Configure high availability, load balancing, and disaster recovery mechanisms | CTO | A | 1 | 2 |
| S2.5-F1.T2.4 | Set up logging, monitoring, and alerting dashboards for platform health | DevOps Engineer | R | 2 | 3 |
| S2.5-F1.T2.5 | Perform infrastructure-as-code (IaC) scripting for automated environment replication | DevOps Engineer | C | 1 | 1 |
| **S2.5-F1.T3** | **Core API Gateway Implementation** | | | **9** | **15** |
| S2.5-F1.T3.1 | Implement standard API security policies (OAuth 2.0, JWT, API Keys) | Security Engineer | R | 3 | 5 |
| S2.5-F1.T3.2 | Configure rate limiting, throttling, and quota management policies | API Engineer | R | 2 | 3 |
| S2.5-F1.T3.3 | Develop a centralized transformation and mediation policy library | Data Engineer Lead | A | 2 | 3 |
| S2.5-F1.T3.4 | Set up the developer portal with initial documentation and onboarding workflows | Product Writer | R | 1 | 2 |
| S2.5-F1.T3.5 | Integrate the gateway with identity and access management (IAM) systems | Security Engineer | C | 1 | 2 |
| **S2.5-F1.T4** | **Security and Compliance Integration** | | | **8** | **13** |
| S2.5-F1.T4.1 | Conduct a comprehensive security threat model assessment of the platform architecture | Chief Digital Officer | A | 2 | 3 |
| S2.5-F1.T4.2 | Implement data encryption in transit (TLS/SSL) and at rest | Security Engineer | R | 2 | 3 |
| S2.5-F1.T4.3 | Configure audit logging to meet regulatory compliance requirements (e.g., UU PDP, GDPR) | Data Governance Manager | R | 2 | 3 |
| S2.5-F1.T4.4 | Perform penetration testing and vulnerability scanning on the deployed platform | Security Engineer | C | 1 | 2 |
| S2.5-F1.T4.5 | Prepare compliance documentation and get sign-off from the Data Privacy Officer | Data Steward | S | 1 | 2 |

**Deliverable Traceability**

| ID | Deliverable | Template | R | A | S | C | I |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S2.5-F1.D1 | API Gateway Architecture Blueprint | `KA-02-architecture-blueprint.md` | Solution Architect | CTO | Data Architect | DevOps Engineer | Chief Digital Officer |
| S2.5-F1.D2 | Platform Security & Compliance Report | `KA-05-security-assessment.md` | Security Engineer | Chief Digital Officer | Data Governance Manager | Data Steward | Project Manager |
| S2.5-F1.D3 | Infrastructure-as-Code Scripts | `N/A` | DevOps Engineer | CTO | API Engineer | | |

**RASCI Role Legend**

*   **R:** Responsible
*   **A:** Accountable
*   **S:** Supportive
*   **C:** Consulted
*   **I:** Informed

---

### Feature S2.5-F2: API Development and Governance Lifecycle

**Description:** This feature establishes the end-to-end process for designing, developing, securing, and managing APIs on the platform. It includes creating a robust governance model and providing the necessary training and documentation to ensure consistency and quality.

**Tasks & Subtasks**

| ID | Task / Subtask | Role | RASCI | Man-Days | SP |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **S2.5-F2.T1** | **API Design & Development Lifecycle Setup** | | | **8** | **13** |
| S2.5-F2.T1.1 | Define and document API design standards and style guide (e.g., RESTful principles, naming conventions) | Solution Architect | R | 2 | 3 |
| S2.5-F2.T1.2 | Create API specification templates (OpenAPI/Swagger) with mandatory security and metadata fields | Data Architect | R | 2 | 3 |
| S2.5-F2.T1.3 | Establish the CI/CD pipeline for automated API testing, documentation generation, and deployment | DevOps Engineer | R | 3 | 5 |
| S2.5-F2.T1.4 | Integrate automated security scanning (SAST/DAST) into the CI/CD pipeline | CTO | A | 1 | 2 |
| **S2.5-F2.T2** | **Pilot API Implementation and Onboarding** | | | **10** | **16** |
| S2.5-F2.T2.1 | Identify and select a suitable candidate for the first pilot API | Business Analyst | R | 1 | 2 |
| S2.5-F2.T2.2 | Develop the pilot API based on the new design standards and CI/CD pipeline | API Engineer | R | 4 | 6 |
| S2.5-F2.T2.3 | Onboard the pilot API to the gateway, applying security and traffic management policies | Data Engineer Lead | A | 2 | 3 |
| S2.5-F2.T2.4 | Conduct user acceptance testing (UAT) with the pilot API consumer team | Quality Assurance Engineer | R | 2 | 3 |
| S2.5-F2.T2.5 | Gather feedback and create a lessons-learned document for process improvement | Project Manager | C | 1 | 2 |
| **S2.5-F2.T3** | **Governance Model and Policy Enforcement** | | | **7** | **11** |
| S2.5-F2.T3.1 | Define the API governance operating model, including roles, responsibilities, and review processes | Data Governance Manager | R | 2 | 3 |
| S2.5-F2.T3.2 | Create a formal Data Contract template for API producers and consumers | Data Steward | R | 2 | 3 |
| S2.5-F2.T3.3 | Implement automated policy checks in the CI/CD pipeline to enforce governance standards | Chief Digital Officer | A | 2 | 3 |
| S2.5-F2.T3.4 | Establish an API versioning and lifecycle management (deprecation, retirement) strategy | Solution Architect | S | 1 | 2 |
| **S2.5-F2.T4** | **Training and Documentation** | | | **5** | **8** |
| S2.5-F2.T4.1 | Develop training materials for API developers on design standards, security practices, and platform usage | Product Writer | R | 2 | 3 |
| S2.5-F2.T4.2 | Conduct training workshops for internal development teams | Account Manager | R | 1 | 2 |
| S2.5-F2.T4.3 | Create comprehensive user guides and tutorials for the developer portal | Content Officer (Writer) | R | 1 | 2 |
| S2.5-F2.T4.4 | Establish a support channel and FAQ for API developers and consumers | Project Manager | C | 1 | 1 |

**Deliverable Traceability**

| ID | Deliverable | Template | R | A | S | C | I |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S2.5-F2.D1 | API Design Standards & Style Guide | `KA-06-api-standards.md` | Solution Architect | CTO | Data Architect | API Engineer | Business Analyst |
| S2.5-F2.D2 | API Governance Operating Model | `KA-01-governance-operating-model.md` | Data Governance Manager | Chief Digital Officer | Data Steward | Solution Architect | Project Manager |
| S2.5-F2.D3 | API Developer Training Materials | `KA-01-communication-training-plan.md` | Product Writer | Account Manager | Content Officer (Writer) | API Engineer | |

**RASCI Role Legend**

*   **R:** Responsible
*   **A:** Accountable
*   **S:** Supportive
*   **C:** Consulted
*   **I:** Informed

---

**S2.5-TOTAL**: **Secure & Trusted Data Exchange — API Gateway Platform** — **65 Man-Days, 105 SP** (2 Features, 8 Tasks, 33 Subtasks)

---

### Service 2.6: Analytics and Visualization Solutions (Epic)

**DAMA KAs**: KA-13 (Primary), KA-06, KA-11
**Lifecycle Stage**: Discovery → Development → Launch
**Methodology**: Agile + Data Storytelling

#### Feature S2.6-A: Analytics Requirements & Data Preparation

**Milestone**: M1 — Analytics Requirements & Data Model Approved → Termin 1 (30%)
**Lifecycle Stage**: Discovery → Planning (Identify, Design)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.6-01 | Task | Gather Analytics Requirements & Define Use Cases | KA-13 | 16 | 13 | — | S | | |
| S2.6-01a | Subtask | Facilitate analytics discovery workshops with business and technical teams | KA-13 | 5 | 5 | — | S | Business Analyst (Data) | R |
| S2.6-01b | Subtask | Define and prioritize analytics use cases and user stories | KA-13 | 4 | 5 | S2.6-01a | P | Product Manager | R |
| S2.6-01c | Subtask | Map data requirements and source systems for each use case | KA-13 | 4 | 5 | S2.6-01a | P | Data Analyst | R |
| S2.6-01d | Subtask | Define KPIs, success metrics, and acceptance criteria for each use case | KA-13 | 3 | 3 | S2.6-01b | S | Business Analyst (Data) | R |
| S2.6-02 | Task | Prepare, Profile, and Model Data for Analytics | KA-06 | 20 | 13 | S2.6-01 | S | | |
| S2.6-02a | Subtask | Conduct comprehensive data profiling and quality assessment on source data | KA-11 | 5 | 5 | — | S | Data Quality Analyst | R |
| S2.6-02b | Subtask | Design and implement data preparation and cleansing pipelines (ETL/ELT) | KA-06 | 6 | 8 | S2.6-02a | S | Data Engineer | R |
| S2.6-02c | Subtask | Develop analytics base tables and feature stores | KA-06 | 5 | 5 | S2.6-02b | S | Data Engineer | R |
| S2.6-02d | Subtask | Design and build the analytics dimensional data model (Star Schema) | KA-03 | 4 | 5 | S2.6-02c | S | Data Architect | R |
| S2.6-03 | Task | Design Analytics Visualization & User Experience | KA-13 | 15 | 13 | S2.6-02 | S | | |
| S2.6-03a | Subtask | Select appropriate visualization tools and establish a design framework | KA-13 | 3 | 3 | — | S | Data Visualization Specialist | R |
| S2.6-03b | Subtask | Create low-fidelity wireframes and mockups for dashboards | KA-13 | 4 | 5 | S2.6-03a | S | Product Designer | R |
| S2.6-03c | Subtask | Develop high-fidelity interactive prototypes and storyboards | KA-13 | 5 | 5 | S2.6-03b | S | Data Visualization Specialist | R |
| S2.6-03d | Subtask | Conduct usability testing and gather feedback from user groups | KA-13 | 3 | 3 | S2.6-03c | S | Business Analyst (Data) | R |

**Feature S2.6-A Subtotal**: 51 Man-Days, 39 SP (3 Tasks, 12 Subtasks)

##### Output Deliverable Traceability — Feature S2.6-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Analytics Requirements & Use Case Document | Must | S2.6-01d | Business Analyst (Data) | Chief Data Officer (CDO) | Product Manager | Data Governance Manager | CEO | output-deliverable-template.md |
| 2 | Data Quality Assessment Report | Must | S2.6-02a | Data Quality Analyst | Data Governance Manager | Data Steward | Data Engineer | Chief Data Officer (CDO) | output-deliverable-template.md |
| 3 | Analytics Data Model (Dimensional) | Must | S2.6-02d | Data Architect | CTO | Data Engineer | Business Analyst (Data) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 4 | Interactive Dashboard Prototypes | Must | S2.6-03c | Data Visualization Specialist | Product Manager | Product Designer | Business Analyst (Data) | CEO | - |

**RASCI Role Legend:**
- **R**: Business Analyst (Data), Data Quality Analyst, Data Architect, Data Visualization Specialist
- **A**: Chief Data Officer (CDO), Data Governance Manager, CTO, Product Manager
- **S**: Product Manager, Data Steward, Data Engineer, Product Designer
- **C**: Data Governance Manager, Data Engineer, Business Analyst (Data)
- **I**: CEO, Chief Data Officer (CDO)

---

#### Feature S2.6-B: Analytics Development & Visualization Build

**Milestone**: M2 — Analytics Solutions & Dashboards Functional → Termin 2 (40%)
**Lifecycle Stage**: Development (Build)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.6-04 | Task | Develop Analytics Models & Algorithms | KA-13 | 22 | 21 | S2.6-03 | S | | |
| S2.6-04a | Subtask | Develop and train descriptive and diagnostic analytics models | KA-13 | 6 | 8 | — | S | Data Scientist | R |
| S2.6-04b | Subtask | Develop and train predictive and prescriptive analytics models | KA-13 | 7 | 8 | S2.6-04a | S | Data Scientist | R |
| S2.6-04c | Subtask | Validate, tune, and test model performance and accuracy | KA-13 | 5 | 5 | S2.6-04b | S | Data Scientist | R |
| S2.6-04d | Subtask | Implement model serving, monitoring, and versioning | KA-06 | 4 | 5 | S2.6-04c | S | MLOps Engineer | R |
| S2.6-05 | Task | Build Dashboards & Visualization Solutions | KA-13 | 25 | 21 | S2.6-04 | S | | |
| S2.6-05a | Subtask | Develop interactive and dynamic dashboards based on prototypes | KA-13 | 8 | 8 | — | S | BI Developer | R |
| S2.6-05b | Subtask | Implement advanced features like drill-down, cross-filtering, and what-if analysis | KA-13 | 6 | 8 | S2.6-05a | S | BI Developer | R |
| S2.6-05c | Subtask | Integrate data storytelling and narrative elements into visualizations | KA-13 | 5 | 5 | S2.6-05b | S | Data Visualization Specialist | R |
| S2.6-05d | Subtask | Implement automated reporting, scheduling, and distribution | KA-13 | 3 | 3 | S2.6-05a | P | BI Developer | R |
| S2.6-05e | Subtask | Ensure mobile-responsive design and cross-browser compatibility | KA-13 | 3 | 3 | S2.6-05d | S | Product Engineering Front-End Engineer | R |
| S2.6-06 | Task | Implement Data Pipelines & Refresh Automation | KA-06 | 18 | 13 | S2.6-05 | S | | |
| S2.6-06a | Subtask | Implement and automate data refresh pipelines for all data sources | KA-06 | 7 | 8 | — | S | Data Engineer | R |
| S2.6-06b | Subtask | Implement data quality monitoring and alerting within the analytics pipelines | KA-11 | 5 | 5 | S2.6-06a | S | Data Quality Engineer | R |
| S2.6-06c | Subtask | Configure pipeline orchestration, scheduling, and dependency management | KA-06 | 4 | 5 | S2.6-06a | S | Data Engineer | R |
| S2.6-06d | Subtask | Implement error handling and recovery mechanisms for pipelines | KA-06 | 2 | 2 | S2.6-06c | S | Data Engineer | R |

**Feature S2.6-B Subtotal**: 65 Man-Days, 55 SP (3 Tasks, 13 Subtasks)

##### Output Deliverable Traceability — Feature S2.6-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Deployed Analytics Models | Must | S2.6-04d | MLOps Engineer | Chief AI Officer | Data Scientist | Data Architect | CTO | - |
| 2 | Interactive Dashboards & Visualizations | Must | S2.6-05b | BI Developer | Product Manager | Data Visualization Specialist | Business Analyst (Data) | CEO | - |
| 3 | Automated Data Pipelines | Must | S2.6-06a | Data Engineer | CTO | Data Quality Engineer | Data Architect | Chief Data Officer (CDO) | - |

**RASCI Role Legend:**
- **R**: MLOps Engineer, BI Developer, Data Engineer
- **A**: Chief AI Officer, Product Manager, CTO
- **S**: Data Scientist, Data Visualization Specialist, Data Quality Engineer
- **C**: Data Architect, Business Analyst (Data)
- **I**: CTO, CEO, Chief Data Officer (CDO)

---

#### Feature S2.6-C: Validation, Training & Handover

**Milestone**: M3 — Analytics Solutions Go-Live & Handover Complete → Termin 3 (30%)
**Lifecycle Stage**: Launch (Test, Deploy, Handover)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S2.6-07 | Task | Conduct Comprehensive Testing & Validation | KA-13 | 18 | 13 | S2.6-06 | S | | |
| S2.6-07a | Subtask | Validate data accuracy and integrity from source to dashboard | KA-11 | 5 | 5 | — | S | Data Quality Analyst | R |
| S2.6-07b | Subtask | Conduct User Acceptance Testing (UAT) with business stakeholders | KA-13 | 5 | 5 | S2.6-07a | S | Business Analyst (Data) | R |
| S2.6-07c | Subtask | Conduct performance and load testing on dashboards and queries | KA-04 | 4 | 5 | S2.6-07b | S | Site Reliability Engineer (DevOps) | R |
| S2.6-07d | Subtask | Triage, fix, and conduct regression testing on all findings | KA-13 | 4 | 5 | S2.6-07c | S | BI Developer | R |
| S2.6-08 | Task | Security & Compliance Review | KA-01 | 12 | 8 | S2.6-07 | S | | |
| S2.6-08a | Subtask | Conduct security vulnerability assessment and penetration testing | KA-01 | 5 | 5 | — | S | Security Engineer | R |
| S2.6-08b | Subtask | Review compliance with data privacy regulations (GDPR, etc.) | KA-01 | 4 | 5 | S2.6-08a | S | Data Governance Manager | R |
| S2.6-08c | Subtask | Remediate security and compliance findings | KA-01 | 3 | 3 | S2.6-08b | S | Security Engineer | R |
| S2.6-09 | Task | Conduct Analytics Training & Drive Adoption | KA-13 | 20 | 13 | S2.6-08 | S | | |
| S2.6-09a | Subtask | Develop role-based training materials (executives, analysts, users) | KA-13 | 5 | 5 | — | S | Data Literacy Champion | R |
| S2.6-09b | Subtask | Conduct dashboard interpretation and data storytelling workshops | KA-13 | 6 | 8 | S2.6-09a | S | Data Visualization Specialist | R |
| S2.6-09c | Subtask | Create user guides, FAQs, and a knowledge base | KA-13 | 4 | 5 | S2.6-09a | P | Product Writer | R |
| S2.6-09d | Subtask | Establish an Analytics Center of Excellence (CoE) and champion program | KA-13 | 5 | 5 | S2.6-09b | S | Data Governance Manager | R |
| S2.6-10 | Task | Finalize Documentation & Execute Handover | KA-02 | 18 | 13 | S2.6-09 | S | | |
| S2.6-10a | Subtask | Create comprehensive technical documentation (architecture, models, pipelines) | KA-02 | 6 | 8 | — | S | Product Writer | R |
| S2.6-10b | Subtask | Create an operational runbook for maintenance and support | KA-04 | 5 | 5 | S2.6-10a | S | Data Engineer | R |
| S2.6-10c | Subtask | Compile the final handover package and conduct a formal transfer session | KA-02 | 4 | 5 | S2.6-10b | S | Project Manager (Data) | R |
| S2.6-10d | Subtask | Conduct a project close-out meeting and document lessons learned | KA-02 | 3 | 3 | S2.6-10c | S | Project Manager (Data) | R |

**Feature S2.6-C Subtotal**: 68 Man-Days, 47 SP (4 Tasks, 15 Subtasks)

##### Output Deliverable Traceability — Feature S2.6-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | UAT & Performance Test Reports | Must | S2.6-07b, S2.6-07c | Business Analyst (Data) | Chief Data Officer (CDO) | Site Reliability Engineer (DevOps) | BI Developer | CTO | output-deliverable-template.md |
| 2 | Security & Compliance Report | Must | S2.6-08b | Data Governance Manager | Chief Data Officer (CDO) | Security Engineer | Data Steward | CEO | output-deliverable-template.md |
| 3 | Training Materials & Knowledge Base | Must | S2.6-09a, S2.6-09c | Data Literacy Champion | Project Manager (Data) | Data Visualization Specialist | Content Officer (Writer) | Chief Data Officer (CDO) | knowledge-transfer-template.md |
| 4 | Final Handover Package | Must | S2.6-10c | Project Manager (Data) | CTO | Product Writer | Data Engineer | CEO | - |

**RASCI Role Legend:**
- **R**: Business Analyst (Data), Data Governance Manager, Data Literacy Champion, Project Manager (Data)
- **A**: Chief Data Officer (CDO), CTO
- **S**: Site Reliability Engineer (DevOps), Security Engineer, Data Visualization Specialist, Product Writer, Data Engineer
- **C**: BI Developer, Data Steward, Content Officer (Writer)
- **I**: CTO, CEO, Chief Data Officer (CDO)

**S2.6-TOTAL**: **Analytics and Visualization Solutions** — **184 Man-Days, 141 SP** (3 Features, 10 Tasks, 40 Subtasks)

---

## Pillar 3: Empowerment & Managed Services

### Service 3.1: Data Governance Office (DGO) as a Service (Epic)

**DAMA KAs**: KA-01 (Primary), KA-11, KA-14  
**Lifecycle Stage**: Launch → Operate → Optimize  
**Methodology**: DAMA-DMBOK Operating Model + Continuous Improvement  
**Total Man-Days**: 155 | **Features**: 3 | **Tasks**: 13 | **Subtasks**: 52  

---

#### Feature S3.1-A: DGO Setup & Operating Model Design

**Milestone**: M1 — DGO Operating Model & Team Established → Termin 1 (30%)  
**Lifecycle Stage**: Launch (Establish, Mobilize)  

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.1-01 | Task | Design DGO organizational structure & operating model | KA-01 | 18 | 15 | — | S |  |  |
| S3.1-01a | Subtask | Define DGO mission, vision & scope | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S3.1-01b | Subtask | Design DGO organizational structure & reporting lines | KA-01 | 4 | 4 | S3.1-01a | P | Data Governance Manager | R |
| S3.1-01c | Subtask | Define DGO roles, responsibilities & RASCI | KA-01 | 4 | 4 | S3.1-01a | P | Data Governance Analyst | R |
| S3.1-01d | Subtask | Design DGO operating procedures & workflows | KA-01 | 3 | 3 | S3.1-01a | P | Data Governance Analyst | R |
| S3.1-01e | Subtask | Conduct security & compliance review of operating model | KA-05 | 2 | 2 | S3.1-01d | P | Chief Compliance Officer | R |
| S3.1-01f | Subtask | Validate operating model with Chief Data Officer (CDO) and CEO | KA-01 | 2 | 2 | S3.1-01d | P | Chief Data Officer (CDO) | R |
| S3.1-02 | Task | Establish governance council & working groups | KA-01 | 14 | 12 | S3.1-01 | S |  |  |
| S3.1-02a | Subtask | Identify & onboard governance council members | KA-01 | 3 | 3 | — | S | Chief Data Officer (CDO) | R |
| S3.1-02b | Subtask | Define council charter & meeting cadence | KA-01 | 3 | 3 | S3.1-02a | P | Data Governance Manager | R |
| S3.1-02c | Subtask | Establish domain-specific working groups | KA-01 | 3 | 3 | S3.1-02b | S | Data Governance Analyst | R |
| S3.1-02d | Subtask | Conduct inaugural governance council meeting | KA-01 | 3 | 3 | S3.1-02a | P | Chief Data Officer (CDO) | R |
| S3.1-02e | Subtask | Develop communication plan for governance council | KA-01 | 2 | 2 | S3.1-02b | S | Head of Digital Branding & Communication | R |
| S3.1-03 | Task | Deploy governance tools & monitoring infrastructure | KA-01 | 16 | 15 | S3.1-02 | S |  |  |
| S3.1-03a | Subtask | Select & deploy governance collaboration tools | KA-01 | 4 | 4 | — | S | Data Engineer Lead | R |
| S3.1-03b | Subtask | Configure governance KPI dashboards | KA-14 | 4 | 4 | S3.1-03a | S | BI Developer | R |
| S3.1-03c | Subtask | Set up issue tracking & escalation workflows | KA-01 | 3 | 3 | S3.1-03b | S | Data Governance Analyst | R |
| S3.1-03d | Subtask | Configure automated governance reporting | KA-14 | 3 | 3 | S3.1-03a | P | Data Analyst | R |
| S3.1-03e | Subtask | Conduct quality assurance and testing of tools | KA-11 | 2 | 2 | S3.1-03c | S | Data Quality Lead | R |
| S3.1-03f | Subtask | Train governance team on tools usage | KA-01 | 2 | 2 | S3.1-03d | S | Content Officer (Writer) | R |
| S3.1-04 | Task | Develop initial DGO training & onboarding materials | KA-01 | 8 | 7 | S3.1-01 | S |  |  |
| S3.1-04a | Subtask | Create training curriculum for DGO roles | KA-01 | 3 | 3 | — | S | Data Literacy Champion | R |
| S3.1-04b | Subtask | Develop onboarding presentations and handbooks | KA-01 | 3 | 3 | S3.1-04a | S | Content Officer (Graphic Designer) | R |
| S3.1-04c | Subtask | Schedule and facilitate onboarding sessions | KA-01 | 2 | 2 | S3.1-04b | S | Project Manager | R |
| S3.1-04d | Subtask | Collect feedback and improve training materials | KA-01 | 2 | 2 | S3.1-04c | P | Data Governance Manager | R |

**Feature S3.1-A Subtotal**: 56 Man-Days, 46 SP (4 Tasks, 22 Subtasks)  

##### Output Deliverable Traceability — Feature S3.1-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | DGO Charter & Operating Model | Must | Data Governance Manager, Data Governance Analyst | Chief Data Officer (CDO) | Data Governance Manager | Business Analyst (Data), Data Steward | Chief Compliance Officer | CEO | output-deliverable-template.md |
| 2 | DGO RASCI Matrix | Must | Data Governance Analyst | Data Governance Manager | Project Manager (Data) | Chief Data Officer (CDO) | Data Steward | CEO | output-deliverable-template.md |
| 3 | DGO Operating Procedures | Must | Data Governance Analyst | Data Governance Manager | Business Analyst (Data) | Chief Compliance Officer | Chief Data Officer (CDO) | output-deliverable-template.md |
| 4 | Governance Council Charter | Must | Data Governance Manager | Chief Data Officer (CDO) | Data Governance Analyst | Head of Business Management | CEO | output-deliverable-template.md |
| 5 | Governance KPI Dashboard | Must | BI Developer | Data Governance Manager | Data Analyst | Data Governance Analyst | Chief Data Officer (CDO) | output-deliverable-template.md |
| 6 | DGO Training & Onboarding Materials | Should | Data Literacy Champion, Content Officer (Graphic Designer) | Data Governance Manager | Project Manager | Content Officer (Writer) | Head of Digital Branding & Communication | proposal-template.md |

**RASCI Role Legend**:  
- R = Responsible  
- A = Accountable  
- S = Support  
- C = Consulted  
- I = Informed  

---

#### Feature S3.1-B: DGO Operations & Governance Execution

**Milestone**: M2 — DGO Operational for 3 Months & Quarterly Report Delivered → Termin 2 (40%)  
**Lifecycle Stage**: Operate (Execute, Monitor)  

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.1-05 | Task | Execute ongoing governance operations (3 months) | KA-01 | 22 | 18 | S3.1-03 | S |  |  |
| S3.1-05a | Subtask | Facilitate monthly governance council meetings | KA-01 | 3 | 3 | — | S | Data Governance Manager | R |
| S3.1-05b | Subtask | Manage data issue resolution & escalation | KA-01 | 5 | 5 | S3.1-05a | S | Data Governance Analyst | R |
| S3.1-05c | Subtask | Conduct data quality monitoring & reporting | KA-11 | 5 | 5 | S3.1-05b | S | Data Quality Analyst | R |
| S3.1-05d | Subtask | Manage policy compliance reviews | KA-01 | 4 | 4 | S3.1-05a | P | Compliance Officer (Data) | R |
| S3.1-05e | Subtask | Perform security audit and risk assessment | KA-05 | 3 | 3 | S3.1-05d | P | Chief Compliance Officer | R |
| S3.1-05f | Subtask | Coordinate with Data Security Officer for incident readiness | KA-01 | 2 | 2 | S3.1-05e | S | Data Security Officer | R |
| S3.1-06 | Task | Conduct data stewardship program | KA-01 | 18 | 16 | S3.1-05 | S |  |  |
| S3.1-06a | Subtask | Recruit & onboard data stewards per domain | KA-01 | 4 | 4 | — | S | Data Governance Manager | R |
| S3.1-06b | Subtask | Conduct data steward training (2-3 sessions) | KA-01 | 4 | 4 | S3.1-06a | S | Data Literacy Champion | R |
| S3.1-06c | Subtask | Facilitate data steward community meetings (monthly) | KA-01 | 3 | 3 | S3.1-06b | S | Data Governance Analyst | R |
| S3.1-06d | Subtask | Monitor steward performance & provide coaching | KA-01 | 3 | 3 | S3.1-06a | P | Data Governance Manager | R |
| S3.1-06e | Subtask | Implement steward feedback mechanism and continuous improvement | KA-01 | 4 | 2 | S3.1-06c | P | Data Stewardship Lead | R |
| S3.1-07 | Task | Produce governance reports & metrics | KA-14 | 15 | 14 | S3.1-06 | S |  |  |
| S3.1-07a | Subtask | Compile monthly governance metrics report | KA-14 | 3 | 3 | — | S | Data Analyst | R |
| S3.1-07b | Subtask | Produce quarterly governance status report | KA-14 | 4 | 4 | S3.1-07a | S | Data Governance Manager | R |
| S3.1-07c | Subtask | Track & report governance KPI trends | KA-14 | 3 | 3 | S3.1-07b | S | Data Analyst | R |
| S3.1-07d | Subtask | Present quarterly report to governance council | KA-14 | 3 | 3 | S3.1-07a | P | Chief Data Officer (CDO) | R |
| S3.1-07e | Subtask | Develop governance issue resolution log and tracking | KA-01 | 2 | 2 | S3.1-05b | S | Data Operations Engineer | R |

**Feature S3.1-B Subtotal**: 55 Man-Days, 48 SP (3 Tasks, 18 Subtasks)  

##### Output Deliverable Traceability — Feature S3.1-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Monthly Governance Reports (3x) | Must | Data Analyst | Data Governance Manager | Data Governance Analyst | Chief Data Officer (CDO) | Project Manager | output-deliverable-template.md |
| 2 | Quarterly Governance Status Report | Must | Data Governance Manager, Chief Data Officer (CDO) | Chief Data Officer (CDO) | Data Analyst | Data Steward | CEO | output-deliverable-template.md |
| 3 | Data Stewardship Program Report | Must | Data Literacy Champion, Data Governance Manager | Chief Data Officer (CDO) | Data Stewardship Lead | Data Governance Analyst | Project Manager | output-deliverable-template.md |
| 4 | Issue Resolution Log | Must | Data Governance Analyst | Data Governance Manager | Compliance Officer (Data) | Data Operations Engineer | Chief Data Officer (CDO) | output-deliverable-template.md |
| 5 | Compliance & Security Review Report | Should | Chief Compliance Officer | Chief Data Officer (CDO) | Data Security Officer | Data Governance Manager | CEO | output-deliverable-template.md |

**RASCI Role Legend**:  
- R = Responsible  
- A = Accountable  
- S = Support  
- C = Consulted  
- I = Informed  

---

#### Feature S3.1-C: Maturity Review, Improvement & Transition

**Milestone**: M3 — Maturity Review Complete & Transition Plan Delivered → Termin 3 (30%)  
**Lifecycle Stage**: Optimize (Review, Improve, Transition)  

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.1-08 | Task | Conduct governance maturity re-assessment | KA-14 | 16 | 14 | S3.1-07 | S |  |  |
| S3.1-08a | Subtask | Re-assess maturity across 14 DAMA Knowledge Areas | KA-14 | 5 | 5 | — | S | Data Governance Analyst | R |
| S3.1-08b | Subtask | Compare with baseline assessment (delta analysis) | KA-14 | 3 | 3 | S3.1-08a | P | Data Analyst | R |
| S3.1-08c | Subtask | Identify remaining gaps & improvement areas | KA-14 | 3 | 3 | S3.1-08a | P | Data Governance Manager | R |
| S3.1-08d | Subtask | Conduct security & compliance gap analysis | KA-05 | 2 | 2 | S3.1-08a | P | Chief Compliance Officer | R |
| S3.1-08e | Subtask | Produce maturity improvement report | KA-14 | 3 | 3 | S3.1-08a | P | Business Analyst (Data) | R |
| S3.1-09 | Task | Develop improvement roadmap & recommendations | KA-14 | 14 | 12 | S3.1-08 | S |  |  |
| S3.1-09a | Subtask | Define next-phase improvement initiatives | KA-14 | 4 | 4 | — | S | Data Governance Manager | R |
| S3.1-09b | Subtask | Design sustainability plan for DGO operations | KA-01 | 4 | 4 | S3.1-09a | P | Data Governance Manager | R |
| S3.1-09c | Subtask | Develop client self-sufficiency roadmap | KA-01 | 3 | 3 | S3.1-09a | P | Project Manager (Data) | R |
| S3.1-09d | Subtask | Review roadmap with Chief Data Officer (CDO) and CEO | KA-14 | 3 | 3 | S3.1-09a | P | Chief Data Officer (CDO) | R |
| S3.1-09e | Subtask | Validate improvement roadmap with Data Governance Lead | KA-14 | 2 | 2 | S3.1-09a | C | Data Governance Lead | C |
| S3.1-10 | Task | Knowledge transfer & DGO transition | KA-01 | 17 | 15 | S3.1-09 | S |  |  |
| S3.1-10a | Subtask | Conduct knowledge transfer sessions (3 sessions) | KA-01 | 5 | 5 | — | S | Data Governance Manager | R |
| S3.1-10b | Subtask | Compile all governance artifacts & documentation | KA-01 | 3 | 3 | S3.1-10a | S | Product Writer | R |
| S3.1-10c | Subtask | Transition DGO operations to client team | KA-01 | 3 | 3 | S3.1-10b | S | Data Governance Manager | R |
| S3.1-10d | Subtask | Conduct final project close-out & presentation | KA-01 | 3 | 3 | S3.1-10a | P | Chief Data Officer (CDO) | R |
| S3.1-10e | Subtask | Develop post-transition support plan | KA-01 | 3 | 3 | S3.1-10c | S | Project Manager | R |

**Feature S3.1-C Subtotal**: 44 Man-Days, 43 SP (3 Tasks, 18 Subtasks)  

##### Output Deliverable Traceability — Feature S3.1-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Maturity Re-Assessment Report | Must | Data Governance Analyst, Data Analyst, Business Analyst (Data) | Data Governance Manager | Chief Data Officer (CDO) | Product Writer | Data Governance Lead | CEO | output-deliverable-template.md |
| 2 | Improvement Roadmap | Must | Data Governance Manager | Chief Data Officer (CDO) | Project Manager (Data) | Business Analyst (Data) | Data Governance Lead | CEO | output-deliverable-template.md |
| 3 | DGO Sustainability Plan | Must | Data Governance Manager | Chief Data Officer (CDO) | Project Manager (Data) | Data Governance Analyst | CEO | output-deliverable-template.md |
| 4 | Client Self-Sufficiency Roadmap | Should | Project Manager (Data) | Chief Data Officer (CDO) | Data Governance Manager | Data Literacy Champion | CEO | output-deliverable-template.md |
| 5 | Final Governance Artifact Package | Must | Product Writer | Project Manager (Data) | Data Governance Manager | Data Governance Analyst | CEO | knowledge-transfer-template.md |
| 6 | Transition Report | Must | Data Governance Manager, Chief Data Officer (CDO) | Chief Data Officer (CDO) | Project Manager (Data) | Product Writer | CEO | knowledge-transfer-template.md |

**RASCI Role Legend**:  
- R = Responsible  
- A = Accountable  
- S = Support  
- C = Consulted  
- I = Informed  

---

**S3.1-TOTAL**: **Data Governance Office (DGO) as a Service** — **155 Man-Days, 137 SP** (3 Features, 13 Tasks, 52 Subtasks)

---

### Service 3.2: Data Literacy & Culture Program (Epic)

**DAMA KAs**: KA-14 (Primary), KA-01  
**Lifecycle Stage**: Planning → Launch → Operate  
**Methodology**: Adult Learning Theory + Change Management  
**Total Man-Days**: 130 | **Features**: 3 | **Tasks**: 13 | **Subtasks**: 54

---

#### Feature S3.2-A: Literacy Assessment & Program Design

**Milestone**: M1 — Literacy Assessment & Program Curriculum Approved → Termin 1 (30%)  
**Lifecycle Stage**: Planning (Assess, Design)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.2-01 | Task | Assess current data literacy levels & culture | KA-14 | 15 | 10 | — | S |  |  |
| S3.2-01a | Subtask | Design & distribute data literacy assessment survey | KA-14 | 3 | 3 | — | S | Data Literacy Champion | R |
| S3.2-01b | Subtask | Conduct focus groups on data culture (3-4 sessions) | KA-14 | 4 | 4 | S3.2-01a | S | Change Manager (Data) | R |
| S3.2-01c | Subtask | Analyze assessment results & identify gaps | KA-14 | 3 | 3 | S3.2-01a | P | Data Analyst | R |
| S3.2-01d | Subtask | Benchmark against industry data literacy standards | KA-14 | 2 | 2 | S3.2-01a | P | Business Analyst (Data) | R |
| S3.2-01e | Subtask | Conduct data governance compliance check | KA-01 | 2 | 2 | S3.2-01c | S | Data Governance Manager | R |
| S3.2-01f | Subtask | Present assessment findings to leadership | KA-14 | 1 | 1 | S3.2-01c | S | Chief Data Officer (CDO) | I |
| S3.2-02 | Task | Design data literacy program & curriculum | KA-14 | 20 | 18 | S3.2-01 | S |  |  |
| S3.2-02a | Subtask | Define learning objectives per audience level | KA-14 | 3 | 3 | — | S | Data Literacy Champion | R |
| S3.2-02b | Subtask | Design curriculum modules (beginner/intermediate/advanced) | KA-14 | 5 | 5 | S3.2-02a | P | Data Literacy Champion | R |
| S3.2-02c | Subtask | Design hands-on exercises & case studies | KA-14 | 3 | 3 | S3.2-02a | P | Data Analyst | R |
| S3.2-02d | Subtask | Design program evaluation & success metrics | KA-14 | 3 | 3 | S3.2-02a | P | Change Manager (Data) | R |
| S3.2-02e | Subtask | Conduct security and privacy review of curriculum content | KA-01 | 3 | 3 | S3.2-02b | S | Chief Privacy Officer (CPO) | R |
| S3.2-02f | Subtask | Review curriculum with Product Engineering Manager | KA-14 | 3 | 3 | S3.2-02b | S | Product Engineering Manager | S |
| S3.2-03 | Task | Quality assurance & stakeholder alignment | KA-14 | 8 | 7 | S3.2-02 | S |  |  |
| S3.2-03a | Subtask | Conduct internal QA review of assessment & curriculum | KA-14 | 3 | 3 | — | S | Data Quality Lead | R |
| S3.2-03b | Subtask | Facilitate stakeholder review sessions | KA-14 | 2 | 2 | S3.2-03a | S | Project Manager (Data) | R |
| S3.2-03c | Subtask | Incorporate feedback & finalize curriculum | KA-14 | 2 | 2 | S3.2-03b | S | Data Literacy Champion | R |
| S3.2-03d | Subtask | Obtain formal approval from Chief Data Officer (CDO) | KA-14 | 1 | 1 | S3.2-03c | S | Chief Data Officer (CDO) | A |
| S3.2-04 | Task | Develop communication & marketing plan for program launch | KA-14 | 5 | 4 | S3.2-03 | S |  |  |
| S3.2-04a | Subtask | Create program branding & messaging | KA-14 | 2 | 2 | — | S | Content Officer (Graphic Designer) | R |
| S3.2-04b | Subtask | Develop launch announcement materials | KA-14 | 1 | 1 | S3.2-04a | S | Content Officer (Writer) | R |
| S3.2-04c | Subtask | Plan internal communication channels & schedule | KA-14 | 1 | 1 | S3.2-04a | S | Account Manager | R |
| S3.2-04d | Subtask | Coordinate launch briefing with CEO and CDO | KA-14 | 1 | 1 | S3.2-04c | S | CEO | I |

**Feature S3.2-A Subtotal**: 48 Man-Days, 42 SP (4 Tasks, 20 Subtasks)

##### Output Deliverable Traceability — Feature S3.2-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Data Literacy Assessment Report | Must | S3.2-01a, S3.2-01c, S3.2-01e | Data Literacy Champion, Data Analyst, Data Governance Manager | Chief Data Officer (CDO) | Change Manager (Data), Project Manager (Data) | Chief Privacy Officer (CPO) | CEO | output-deliverable-template.md |
| 2 | Program Curriculum | Must | S3.2-02a to S3.2-02d | Data Literacy Champion | Chief Data Officer (CDO) | Data Analyst, Change Manager (Data), Product Engineering Manager | Chief Privacy Officer (CPO) | CTO | output-deliverable-template.md |
| 3 | Security & Privacy Review Report | Should | S3.2-02e | Chief Privacy Officer (CPO) | Chief Data Officer (CDO) | Data Literacy Champion | Change Manager (Data) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 4 | QA & Stakeholder Approval Summary | Must | S3.2-03a to S3.2-03d | Data Quality Lead, Project Manager (Data), Data Literacy Champion | Chief Data Officer (CDO) | Change Manager (Data) | Product Engineering Manager | CEO | output-deliverable-template.md |
| 5 | Communication & Marketing Plan | Should | S3.2-04a to S3.2-04d | Content Officer (Graphic Designer), Content Officer (Writer), Account Manager | Chief Data Officer (CDO) | Project Manager (Data) | Change Manager (Data) | CEO | business-proposal-template.md |

**RASCI Role Legend:**  
R = Responsible, A = Accountable, S = Support, C = Consulted, I = Informed

---

#### Feature S3.2-B: Program Delivery & Execution

**Milestone**: M2 — Training Program Delivered (All Batches Complete) → Termin 2 (45%)  
**Lifecycle Stage**: Launch → Operate (Deliver, Execute)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.2-05 | Task | Develop training materials & content | KA-14 | 18 | 16 | S3.2-02 | S |  |  |
| S3.2-05a | Subtask | Develop presentation decks per module | KA-14 | 4 | 4 | — | S | Data Literacy Champion | R |
| S3.2-05b | Subtask | Develop hands-on lab exercises & datasets | KA-14 | 4 | 4 | S3.2-05a | P | Data Analyst Lead | R |
| S3.2-05c | Subtask | Develop assessment quizzes & evaluation forms | KA-14 | 3 | 3 | S3.2-05a | P | Data Literacy Champion | R |
| S3.2-05d | Subtask | Develop quick-reference guides & cheat sheets | KA-14 | 3 | 3 | S3.2-05a | P | Product Writer | R |
| S3.2-05e | Subtask | Conduct security review of training materials | KA-01 | 2 | 2 | S3.2-05a | S | Chief Information Security Officer (CISO) | R |
| S3.2-05f | Subtask | Review materials for accessibility compliance | KA-01 | 2 | 2 | S3.2-05a | S | Data Governance Manager | R |
| S3.2-06 | Task | Deliver training program (multi-batch) | KA-14 | 28 | 25 | S3.2-05 | S |  |  |
| S3.2-06a | Subtask | Deliver beginner-level training (2-3 batches) | KA-14 | 6 | 6 | — | S | Data Literacy Champion | R |
| S3.2-06b | Subtask | Deliver intermediate-level training (2 batches) | KA-14 | 6 | 6 | S3.2-06a | S | Data Literacy Champion | R |
| S3.2-06c | Subtask | Deliver advanced/executive training (1-2 batches) | KA-14 | 5 | 5 | S3.2-06b | S | Data Visualization Specialist | R |
| S3.2-06d | Subtask | Facilitate hands-on workshops & data challenges | KA-14 | 5 | 5 | S3.2-06a | P | Data Analyst Lead | R |
| S3.2-06e | Subtask | Conduct post-training assessments per batch | KA-14 | 3 | 3 | S3.2-06d | S | Data Literacy Champion | R |
| S3.2-06f | Subtask | Coordinate training logistics & participant communication | KA-14 | 3 | 3 | S3.2-06a | S | Project Manager (Data) | R |
| S3.2-07 | Task | Establish data culture initiatives | KA-01 | 12 | 10 | S3.2-06 | S |  |  |
| S3.2-07a | Subtask | Launch data champions network | KA-01 | 3 | 3 | — | S | Change Manager (Data) | R |
| S3.2-07b | Subtask | Design data storytelling competition / DataViz event | KA-13 | 3 | 3 | S3.2-07a | P | Data Visualization Specialist | R |
| S3.2-07c | Subtask | Create internal data newsletter / knowledge sharing | KA-01 | 3 | 3 | S3.2-07a | P | Product Writer | R |
| S3.2-07d | Subtask | Establish data community of practice | KA-01 | 2 | 2 | S3.2-07a | P | Data Literacy Champion | R |
| S3.2-07e | Subtask | Monitor data culture adoption & engagement metrics | KA-01 | 1 | 1 | S3.2-07a | S | Data Governance Manager | R |
| S3.2-08 | Task | Conduct training program quality assurance & feedback analysis | KA-14 | 8 | 7 | S3.2-06 | S |  |  |
| S3.2-08a | Subtask | Collect participant feedback & satisfaction surveys | KA-14 | 3 | 3 | — | S | Data Literacy Champion | R |
| S3.2-08b | Subtask | Analyze training effectiveness & identify improvements | KA-14 | 3 | 3 | S3.2-08a | S | Data Analyst Lead | R |
| S3.2-08c | Subtask | Report findings to Project Manager and Chief Data Officer (CDO) | KA-14 | 2 | 2 | S3.2-08b | S | Change Manager (Data) | R |

**Feature S3.2-B Subtotal**: 66 Man-Days, 61 SP (4 Tasks, 26 Subtasks)

##### Output Deliverable Traceability — Feature S3.2-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Training Materials (decks, labs, guides) | Must | S3.2-05a to S3.2-05d | Data Literacy Champion, Data Analyst Lead, Product Writer | Chief Data Officer (CDO) | Chief Information Security Officer (CISO), Data Governance Manager | Change Manager (Data), Product Engineering Manager | CTO | output-deliverable-template.md |
| 2 | Training Delivery Report & Attendance | Must | S3.2-06a to S3.2-06e | Data Literacy Champion, Data Visualization Specialist, Data Analyst Lead | Chief Data Officer (CDO) | Project Manager (Data), Change Manager (Data) | Data Governance Manager | CEO | output-deliverable-template.md |
| 3 | Post-Training Assessment Results | Must | S3.2-06e | Data Literacy Champion | Chief Data Officer (CDO) | Data Analyst Lead | Change Manager (Data) | Chief Data Officer (CDO) | output-deliverable-template.md |
| 4 | Data Culture Initiative Plan | Should | S3.2-07a to S3.2-07e | Change Manager (Data), Data Visualization Specialist, Product Writer, Data Literacy Champion | Chief Data Officer (CDO) | Data Governance Manager | Project Manager (Data) | CEO | business-proposal-template.md |
| 5 | Training Quality Assurance Report | Should | S3.2-08a to S3.2-08c | Data Literacy Champion, Data Analyst Lead, Change Manager (Data) | Chief Data Officer (CDO) | Project Manager (Data) | Data Governance Manager | CEO | output-deliverable-template.md |

**RASCI Role Legend:**  
R = Responsible, A = Accountable, S = Support, C = Consulted, I = Informed

---

#### Feature S3.2-C: Program Evaluation & Sustainability

**Milestone**: M3 — Program Evaluation Report & Sustainability Plan Delivered → Termin 3 (25%)  
**Lifecycle Stage**: Optimize (Evaluate, Sustain)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.2-09 | Task | Evaluate program effectiveness & impact | KA-14 | 14 | 12 | S3.2-07 | S |  |  |
| S3.2-09a | Subtask | Analyze pre/post assessment score improvements | KA-14 | 3 | 3 | — | S | Data Analyst | R |
| S3.2-09b | Subtask | Conduct participant feedback surveys | KA-14 | 3 | 3 | S3.2-09a | S | Data Literacy Champion | R |
| S3.2-09c | Subtask | Measure business impact metrics (data usage, decisions) | KA-14 | 3 | 3 | S3.2-09b | S | Business Analyst (Data) | R |
| S3.2-09d | Subtask | Produce program effectiveness report | KA-14 | 3 | 3 | S3.2-09a | P | Data Literacy Champion | R |
| S3.2-09e | Subtask | Conduct data security & compliance audit of program | KA-01 | 2 | 2 | S3.2-09d | S | Chief Compliance Officer | R |
| S3.2-10 | Task | Develop sustainability plan & handover | KA-01 | 14 | 12 | S3.2-09 | S |  |  |
| S3.2-10a | Subtask | Design train-the-trainer program | KA-14 | 3 | 3 | — | S | Data Literacy Champion | R |
| S3.2-10b | Subtask | Develop program sustainability roadmap | KA-01 | 4 | 4 | S3.2-10a | P | Change Manager (Data) | R |
| S3.2-10c | Subtask | Compile all program materials & handover | KA-01 | 3 | 3 | S3.2-10b | S | Product Writer | R |
| S3.2-10d | Subtask | Project close-out & recommendations | KA-01 | 2 | 2 | S3.2-10a | P | Project Manager (Data) | R |
| S3.2-10e | Subtask | Conduct knowledge transfer sessions with client teams | KA-01 | 2 | 2 | S3.2-10c | S | Content Officer (Motion Graphic Designer) | R |
| S3.2-11 | Task | Conduct data literacy re-assessment | KA-14 | 8 | 7 | S3.2-10 | S |  |  |
| S3.2-11a | Subtask | Re-distribute literacy assessment survey | KA-14 | 2 | 2 | — | S | Data Literacy Champion | R |
| S3.2-11b | Subtask | Analyze improvement & produce delta report | KA-14 | 3 | 3 | S3.2-11a | S | Data Analyst | R |
| S3.2-11c | Subtask | Present results to leadership & recommend next steps | KA-14 | 3 | 2 | S3.2-11b | S | Change Manager (Data) | R |

**Feature S3.2-C Subtotal**: 38 Man-Days, 36 SP (3 Tasks, 18 Subtasks)

##### Output Deliverable Traceability — Feature S3.2-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Program Effectiveness Report | Must | S3.2-09a to S3.2-09d | Data Analyst, Data Literacy Champion, Business Analyst (Data) | Chief Data Officer (CDO) | Change Manager (Data), Project Manager (Data) | Chief Compliance Officer | CEO | output-deliverable-template.md |
| 2 | Compliance & Security Audit Report | Should | S3.2-09e | Chief Compliance Officer | Chief Data Officer (CDO) | Data Governance Manager | Change Manager (Data) | CEO | output-deliverable-template.md |
| 3 | Literacy Re-Assessment Report (Delta) | Must | S3.2-11a, S3.2-11b | Data Literacy Champion, Data Analyst | Chief Data Officer (CDO) | Change Manager (Data) | Project Manager (Data) | CEO | output-deliverable-template.md |
| 4 | Train-the-Trainer Program | Should | S3.2-10a | Data Literacy Champion | Chief Data Officer (CDO) | Change Manager (Data) | Data Governance Manager | CEO | knowledge-transfer-template.md |
| 5 | Sustainability Roadmap | Must | S3.2-10b | Change Manager (Data) | Chief Data Officer (CDO) | Data Literacy Champion | Project Manager (Data) | CEO | output-deliverable-template.md |
| 6 | Final Program Package & Close-Out Report | Must | S3.2-10c, S3.2-10d, S3.2-10e | Product Writer, Project Manager (Data), Content Officer (Motion Graphic Designer) | Chief Data Officer (CDO) | Change Manager (Data) | Data Literacy Champion | CEO | output-deliverable-template.md |

**RASCI Role Legend:**  
R = Responsible, A = Accountable, S = Support, C = Consulted, I = Informed

---

**S3.2-TOTAL**: **Data Literacy & Culture Program** — **130 Man-Days, 139 SP** (3 Features, 13 Tasks, 54 Subtasks)

---

### Service 3.3: Data Management Certified Training (Epic)

**DAMA KAs**: KA-14 (Primary), KA-01 through KA-13
**Lifecycle Stage**: Planning → Launch
**Methodology**: CDMP Certification Framework + Adult Learning Theory
**Total Man-Days**: 102 | **Features**: 3 | **Tasks**: 9 | **Subtasks**: 41

#### Feature S3.3-A: Training Design & Material Development

**Milestone**: M1 — Training Curriculum & Materials Ready → Termin 1 (35%)
**Lifecycle Stage**: Planning (Design, Develop)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.3-01 | Task | Design CDMP-aligned training curriculum | KA-14 | 18 | 13 | — | S | | |
| S3.3-01a | Subtask | Map CDMP exam domains to training modules | KA-14 | 3 | 3 | — | S | Data Governance Manager | R |
| S3.3-01b | Subtask | Design curriculum structure (14 KA modules) | KA-14 | 4 | 5 | S3.3-01a | P | Data Literacy Champion | R |
| S3.3-01c | Subtask | Define learning objectives & assessment criteria | KA-14 | 3 | 3 | S3.3-01a | P | Data Literacy Champion | R |
| S3.3-01d | Subtask | Design practice exam questions & case studies | KA-14 | 4 | 5 | S3.3-01a | P | Data Governance Manager | R |
| S3.3-01e | Subtask | Review curriculum with Chief Data Officer (CDO) for strategic alignment | KA-01 | 2 | 2 | S3.3-01d | S | Chief Data Officer (CDO) | A |
| S3.3-01f | Subtask | Incorporate feedback from the client's project sponsor | KA-14 | 2 | 2 | S3.3-01e | S | Account Manager | R |
| S3.3-02 | Task | Develop training materials & resources | KA-14 | 20 | 21 | S3.3-01 | S | | |
| S3.3-02a | Subtask | Develop presentation decks per DAMA KA (14 modules) | KA-14 | 8 | 8 | — | S | Data Literacy Champion | R |
| S3.3-02b | Subtask | Develop hands-on exercises & real-world scenarios | KA-14 | 5 | 5 | S3.3-02a | P | Data Governance Analyst | R |
| S3.3-02c | Subtask | Develop practice exams & study guides | KA-14 | 4 | 5 | S3.3-02a | P | Data Governance Manager | R |
| S3.3-02d | Subtask | Develop reference materials & quick-reference cards | KA-14 | 3 | 3 | S3.3-02a | P | Product Writer | R |
| S3.3-03 | Task | Quality Assurance and Compliance Review | KA-14 | 8 | 8 | S3.3-02 | S | | |
| S3.3-03a | Subtask | Conduct peer review of all training materials for clarity and consistency | KA-14 | 2 | 2 | — | S | Data Quality Lead | R |
| S3.3-03b | Subtask | Perform technical accuracy review with subject matter experts | KA-14 | 3 | 3 | S3.3-03a | P | Data Architect | C |
| S3.3-03c | Subtask | Ensure materials meet accessibility standards (e.g., for screen readers) | KA-14 | 1 | 1 | S3.3-03a | P | Product Researcher | R |
| S3.3-03d | Subtask | Final review and sign-off from Project Manager | KA-14 | 2 | 2 | S3.3-03c | S | Project Manager (Data) | A |

**Feature S3.3-A Subtotal**: 46 Man-Days, 42 SP (3 Tasks, 15 Subtasks)

##### Output Deliverable Traceability — Feature S3.3-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | CDMP Training Curriculum | Must | S3.3-01a to S3.3-01d | Data Governance Manager, Data Literacy Champion | Chief Data Officer (CDO) | Project Manager (Data) | Client | CEO (CEO) | — |
| 2 | Training Materials (14 modules) | Must | S3.3-02a, S3.3-02d | Data Literacy Champion, Product Writer | Project Manager (Data) | Data Governance Analyst | Data Governance Manager | Client | output-deliverable-template.md |
| 3 | Practice Exams & Study Guides | Must | S3.3-01d, S3.3-02c | Data Governance Manager | Project Manager (Data) | Data Literacy Champion | Data Governance Analyst | Client | — |
| 4 | QA & Compliance Report | Must | S3.3-03a to S3.3-03d | Data Quality Lead, Project Manager (Data) | Chief Data Officer (CDO) | Product Researcher | Data Architect | CTO (CTO) | — |

> **RASCI Role Legend**: Chief Data Officer (CDO), CEO (CEO), CTO (CTO), Account Manager, Data Architect, Data Governance Analyst, Data Governance Manager, Data Literacy Champion, Data Quality Lead, Project Manager (Data), Product Writer, Product Researcher, Client

---

#### Feature S3.3-B: Training Delivery & Assessment

**Milestone**: M2 — All Training Sessions Delivered & Assessments Complete → Termin 2 (40%)
**Lifecycle Stage**: Launch (Deliver)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.3-04 | Task | Deliver CDMP training program (5-day intensive) | KA-14 | 25 | 21 | S3.3-03 | S | | |
| S3.3-04a | Subtask | Deliver Day 1: Data Governance & Strategy (KA-01) | KA-01 | 4 | 5 | — | S | Data Governance Manager | R |
| S3.3-04b | Subtask | Deliver Day 2: Data Architecture & Modeling (KA-02, KA-03) | KA-02 | 4 | 5 | S3.3-04a | S | Data Architect | R |
| S3.3-04c | Subtask | Deliver Day 3: Data Quality & Operations (KA-04, KA-11) | KA-11 | 4 | 5 | S3.3-04b | S | Data Quality Manager | R |
| S3.3-04d | Subtask | Deliver Day 4: Data Security & Integration (KA-05, KA-06) | KA-05 | 4 | 5 | S3.3-04c | S | Data Security Manager | R |
| S3.3-04e | Subtask | Deliver Day 5: Metadata, DW/BI & Ethics (KA-09, KA-13, KA-12) | KA-09 | 4 | 5 | S3.3-04d | S | Data Governance Manager | R |
| S3.3-04f | Subtask | Facilitate daily Q&A & review sessions | KA-14 | 3 | 3 | S3.3-04e | S | Data Literacy Champion | R |
| S3.3-04g | Subtask | Record training sessions for future reference | KA-14 | 2 | 2 | S3.3-04f | S | Content Officer (Writer) | R |
| S3.3-05 | Task | Conduct assessments & exam preparation | KA-14 | 12 | 8 | S3.3-04 | S | | |
| S3.3-05a | Subtask | Administer practice exams (2 rounds) | KA-14 | 3 | 3 | — | S | Data Literacy Champion | R |
| S3.3-05b | Subtask | Conduct exam review & targeted coaching | KA-14 | 5 | 5 | S3.3-05a | P | Data Governance Manager | R |
| S3.3-05c | Subtask | Provide exam registration guidance & support | KA-14 | 2 | 2 | S3.3-05b | S | Project Manager (Data) | R |
| S3.3-05d | Subtask | Analyze practice exam results to identify knowledge gaps | KA-14 | 2 | 2 | S3.3-05a | P | Data Analyst | R |

**Feature S3.3-B Subtotal**: 37 Man-Days, 29 SP (2 Tasks, 11 Subtasks)

##### Output Deliverable Traceability — Feature S3.3-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Training Delivery Report & Attendance | Must | S3.3-04a to S3.3-04f | Data Governance Manager, Data Architect, Data Quality Manager, Data Security Manager, Data Literacy Champion | Project Manager (Data) | Content Officer (Writer) | Chief Data Officer (CDO) | Client | — |
| 2 | Practice Exam Results & Analysis | Must | S3.3-05a, S3.3-05d | Data Literacy Champion, Data Analyst | Project Manager (Data) | Data Governance Manager | Chief Data Officer (CDO) | Client | — |
| 3 | Exam Readiness Assessment | Must | S3.3-05b | Data Governance Manager | Project Manager (Data) | Data Literacy Champion | Chief Data Officer (CDO) | Client | — |

> **RASCI Role Legend**: Chief Data Officer (CDO), Content Officer (Writer), Data Architect, Data Analyst, Data Governance Manager, Data Literacy Champion, Data Quality Manager, Data Security Manager, Project Manager (Data), Client

---

#### Feature S3.3-C: Post-Training Support & Certification Tracking

**Milestone**: M3 — Certification Results Tracked & Program Report Delivered → Termin 3 (25%)
**Lifecycle Stage**: Operate (Support, Track)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.3-06 | Task | Provide post-training support & mentoring | KA-14 | 10 | 8 | S3.3-05 | S | | |
| S3.3-06a | Subtask | Conduct follow-up Q&A sessions (2 sessions) | KA-14 | 3 | 3 | — | S | Data Governance Manager | R |
| S3.3-06b | Subtask | Provide study group facilitation & resources | KA-14 | 3 | 3 | S3.3-06a | S | Data Literacy Champion | R |
| S3.3-06c | Subtask | Conduct 1-on-1 coaching for struggling participants | KA-14 | 4 | 5 | S3.3-06b | S | Data Governance Manager | R |
| S3.3-07 | Task | Track certification results & produce program report | KA-14 | 5 | 5 | S3.3-06 | S | | |
| S3.3-07a | Subtask | Track exam registration & certification results | KA-14 | 1 | 1 | — | S | Project Manager (Data) | R |
| S3.3-07b | Subtask | Produce final program report with pass rates | KA-14 | 2 | 2 | S3.3-07a | S | Data Literacy Champion | R |
| S3.3-07c | Subtask | Compile all materials & handover | KA-14 | 2 | 2 | S3.3-07b | S | Product Writer | R |
| S3.3-08 | Task | Develop continuous learning plan | KA-14 | 4 | 5 | S3.3-07 | S | | |
| S3.3-08a | Subtask | Design ongoing learning path & resource library | KA-14 | 2 | 2 | — | S | Data Literacy Champion | R |
| S3.3-08b | Subtask | Develop recommendations for advanced certifications | KA-14 | 2 | 2 | S3.3-08a | P | Data Governance Manager | R |

**Feature S3.3-C Subtotal**: 19 Man-Days, 18 SP (3 Tasks, 8 Subtasks)

##### Output Deliverable Traceability — Feature S3.3-C

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Final Program Report (with pass rates) | Must | S3.3-07b | Data Literacy Champion | Project Manager (Data) | Data Governance Manager | Chief Data Officer (CDO) | Client | output-deliverable-template.md |
| 2 | Certification Tracking Report | Must | S3.3-07a | Project Manager (Data) | Chief Data Officer (CDO) | Data Literacy Champion | Data Governance Manager | Client | — |
| 3 | Continuous Learning Plan | Should | S3.3-08a, S3.3-08b | Data Literacy Champion, Data Governance Manager | Project Manager (Data) | Product Writer | Chief Data Officer (CDO) | Client | — |
| 4 | Final Materials Package | Must | S3.3-07c | Product Writer | Project Manager (Data) | Data Literacy Champion | Data Governance Manager | Client | knowledge-transfer-template.md |

> **RASCI Role Legend**: Chief Data Officer (CDO), Data Governance Manager, Data Literacy Champion, Project Manager (Data), Product Writer, Client

**S3.3-TOTAL**: **Data Management Certified Training** — **102 Man-Days, 89 SP** (3 Features, 8 Tasks, 34 Subtasks)

---

### Service 3.4: Knowledge Transfer & Thought Leadership / Narasumber (Epic)

**DAMA KAs**: KA-14 (Primary), KA-01, KA-02
**Lifecycle Stage**: Planning → Launch
**Methodology**: Expert-Led Knowledge Transfer + Thought Leadership
**Total Man-Days**: 48 | **Features**: 2 | **Tasks**: 6 | **Subtasks**: 32

---

#### Feature S3.4-A: Content Preparation & Customization

**Milestone**: M1 — Presentation Materials Finalized & Approved → Termin 1 (40%)
**Lifecycle Stage**: Planning (Design, Customize)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.4-01 | Task | Conduct pre-engagement discovery & topic alignment | KA-14 | 6 | 5 | — | S | | |
| S3.4-01a | Subtask | Conduct initial pre-engagement briefing with client sponsor | KA-14 | 1 | 1 | — | S | Account Manager | R |
| S3.4-01b | Subtask | Gather audience profile, pain points, and learning objectives | KA-14 | 2 | 2 | S3.4-01a | S | Business Analyst (Data) | R |
| S3.4-01c | Subtask | Facilitate topic deep-dive and scope alignment workshop with client SMEs | KA-14 | 1 | 2 | S3.4-01b | S | Chief Data Officer (CDO) | R |
| S3.4-01d | Subtask | Research client industry context, challenges, and recent news | KA-14 | 1 | 1 | S3.4-01a | P | Business Analyst (Data) | R |
| S3.4-01e | Subtask | Draft & secure client sign-off on the Session Scope & Objectives document | KA-14 | 1 | 1 | S3.4-01c | S | Project Manager (Data) | R |
| S3.4-02 | Task | Develop & customize presentation materials | KA-14 | 12 | 8 | S3.4-01 | S | | |
| S3.4-02a | Subtask | Develop core presentation narrative and slide outline | KA-14 | 3 | 3 | — | S | Chief Data Officer (CDO) | R |
| S3.4-02b | Subtask | Customize case studies and examples for client context | KA-14 | 2 | 3 | S3.4-02a | S | Business Analyst (Data) | R |
| S3.4-02c | Subtask | Design high-fidelity graphics, diagrams, and visual assets | KA-14 | 3 | 3 | S3.4-02a | P | Data Visualization Specialist | R |
| S3.4-02d | Subtask | Prepare interactive exercises, polls, and discussion prompts | KA-14 | 2 | 2 | S3.4-02a | P | Data Literacy Champion | R |
| S3.4-02e | Subtask | Consolidate all materials into the final presentation deck | KA-14 | 1 | 1 | S3.4-02d | S | Product Writer | R |
| S3.4-02f | Subtask | Perform internal peer review and dry run with the delivery team | KA-14 | 1 | 1 | S3.4-02e | S | Data Governance Manager | R |
| S3.4-03 | Task | Perform Quality Assurance and Compliance Checks | KA-11 | 4 | 3 | S3.4-02 | S | | |
| S3.4-03a | Subtask | Verify all data points, statistics, and external references | KA-11 | 1 | 1 | — | S | Data Quality Analyst | R |
| S3.4-03b | Subtask | Check for copyright compliance on all images and third-party content | KA-01 | 1 | 1 | S3.4-03a | P | Compliance Officer (Data) | R |
| S3.4-03c | Subtask | Perform technical check for broken links, formatting issues, and typos | KA-11 | 1 | 1 | S3.4-03b | S | Product Engineering QA Analyst | R |
| S3.4-03d | Subtask | Secure final approval from Accountable executive before client submission | KA-01 | 1 | 1 | S3.4-03c | S | Chief Data Officer (CDO) | A |

**Feature S3.4-A Subtotal**: 22 Man-Days, 16 SP (3 Tasks, 15 Subtasks)

##### Output Deliverable Traceability — Feature S3.4-A

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Session Scope & Objectives | Must | S3.4-01e | Project Manager (Data) | Chief Data Officer (CDO) | Account Manager | Business Analyst (Data) | CEO (CEO) | - |
| 2 | Final Presentation Deck | Must | S3.4-02e | Product Writer | Chief Data Officer (CDO) | Data Visualization Specialist | Data Governance Manager | Account Manager | pitch-deck-template.md |
| 3 | Interactive Exercise Materials | Should | S3.4-02d | Data Literacy Champion | Chief Data Officer (CDO) | Business Analyst (Data) | - | Project Manager (Data) | - |
| 4 | QA & Compliance Report | Must | S3.4-03d | Data Quality Analyst | Chief Data Officer (CDO) | Compliance Officer (Data) | - | Project Manager (Data) | - |

> **RASCI Role Legend**: Account Manager, Business Analyst (Data), Chief Data Officer (CDO), CEO (CEO), Compliance Officer (Data), Data Governance Manager, Data Literacy Champion, Data Quality Analyst, Data Visualization Specialist, Product Engineering QA Analyst, Product Writer, Project Manager (Data)

---

#### Feature S3.4-B: Delivery, Q&A & Follow-Up

**Milestone**: M2 — Knowledge Transfer Delivered & Follow-Up Materials Sent → Termin 2 (60%)
**Lifecycle Stage**: Launch (Deliver, Follow-Up)

##### Tasks & Subtasks

| ID | Type | Description | DAMA KA | Est. MD | SP | Predecessor | Mode | Role | RASCI |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| S3.4-04 | Task | Deliver knowledge transfer session | KA-14 | 8 | 8 | S3.4-03 | S | | |
| S3.4-04a | Subtask | Perform pre-session technical check with client IT | KA-14 | 1 | 1 | — | S | Project Manager (Data) | R |
| S3.4-04b | Subtask | Deliver keynote/workshop presentation (half/full day) | KA-14 | 3 | 3 | S3.4-04a | S | Chief Data Officer (CDO) | R |
| S3.4-04c | Subtask | Facilitate interactive Q&A and moderate discussion forum | KA-14 | 2 | 2 | S3.4-04b | S | Data Governance Manager | R |
| S3.4-04d | Subtask | Facilitate hands-on exercises and breakout rooms | KA-14 | 1 | 1 | S3.4-04c | S | Data Literacy Champion | R |
| S3.4-04e | Subtask | Record session and capture key timestamps for highlights | KA-14 | 1 | 1 | S3.4-04b | P | Content Officer (Writer) | R |
| S3.4-05 | Task | Produce follow-up materials & documentation | KA-14 | 10 | 8 | S3.4-04 | S | | |
| S3.4-05a | Subtask | Transcribe session recording using automated tools | KA-14 | 1 | 1 | — | S | Content Officer (Writer) | R |
| S3.4-05b | Subtask | Review and edit transcript for accuracy and clarity | KA-14 | 2 | 2 | S3.4-05a | S | Product Writer | R |
| S3.4-05c | Subtask | Compile Q&A summary, poll results, and additional resource links | KA-14 | 3 | 3 | S3.4-05b | S | Business Analyst (Data) | R |
| S3.4-05d | Subtask | Edit session recording into a highlight video or summary clip | KA-14 | 2 | 2 | S3.4-05a | P | Content Officer (Writer) | R |
| S3.4-05e | Subtask | Package all materials into a consolidated digital asset folder | KA-14 | 2 | 1 | S3.4-05d | S | Project Manager (Data) | R |
| S3.4-06 | Task | Collect feedback & perform post-engagement close-out | KA-14 | 8 | 8 | S3.4-05 | S | | |
| S3.4-06a | Subtask | Distribute and collect participant feedback survey | KA-14 | 2 | 2 | — | S | Project Manager (Data) | R |
| S3.4-06b | Subtask | Analyze feedback data and generate satisfaction report | KA-14 | 2 | 2 | S3.4-06a | S | Data Analyst | R |
| S3.4-06c | Subtask | Present feedback report and key findings to the client sponsor | KA-14 | 2 | 2 | S3.4-06b | S | Account Manager | R |
| S3.4-06d | Subtask | Conduct internal post-mortem / lessons learned session | KA-14 | 1 | 1 | S3.4-06c | S | Project Manager (Data) | R |
| S3.4-06e | Subtask | Finalize engagement report with recommendations for future learning | KA-14 | 1 | 1 | S3.4-06d | S | Chief Data Officer (CDO) | R |

**Feature S3.4-B Subtotal**: 26 Man-Days, 24 SP (3 Tasks, 17 Subtasks)

##### Output Deliverable Traceability — Feature S3.4-B

| # | Deliverable | Priority | Produced By | R | A | S | C | I | Template |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Session Recording & Transcript | Must | S3.4-05b | Product Writer | Chief Data Officer (CDO) | Content Officer (Writer) | - | Account Manager | knowledge-transfer-template.md |
| 2 | Consolidated Follow-Up Assets | Must | S3.4-05e | Project Manager (Data) | Chief Data Officer (CDO) | Business Analyst (Data) | - | Account Manager | output-deliverable-template.md |
| 3 | Participant Feedback Report | Should | S3.4-06b | Data Analyst | Account Manager | Project Manager (Data) | - | Chief Data Officer (CDO) | - |
| 4 | Final Engagement Report | Must | S3.4-06e | Chief Data Officer (CDO) | CEO (CEO) | Account Manager | - | Project Manager (Data) | - |

> **RASCI Role Legend**: Account Manager, Business Analyst (Data), Chief Data Officer (CDO), CEO (CEO), Content Officer (Writer), Data Analyst, Data Governance Manager, Data Literacy Champion, Product Writer, Project Manager (Data)

---

**S3.4-TOTAL**: **Knowledge Transfer & Thought Leadership / Narasumber** — **48 Man-Days, 40 SP** (2 Features, 6 Tasks, 32 Subtasks)

---

## Summary: Total Estimated Man-Days per Service

| Pillar | Service ID | Service Name | Features | Tasks | Subtasks | Man-Days | SP |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| **1** | S1.1 | Data Strategy & Roadmap Development | 3 | 9 | 35 | 109 | 90 |
| **1** | S1.2 | Data Governance & Compliance Framework | 3 | 10 | 39 | 121 | 100 |
| **1** | S1.3 | Data Maturity Assessment & Benchmarking | 3 | 7 | 28 | 74 | 60 |
| **1** | S1.4 | Data Governance & Policy Framework Dev. | 3 | 14 | 52 | 183 | 150 |
| **1** | S1.5 | Data Asset Valuation & Monetization Advisory | 3 | 9 | 27 | 79 | 57 |
| | | **Pillar 1 Subtotal** | **15** | **49** | **181** | **566** | **457** |
| **2** | S2.1 | Data-Centric Digital Product Dev. & UX | 4 | 13 | 61 | 238 | 214 |
| **2** | S2.2 | Core Data Platform & Modernization | 4 | 11 | 47 | 183 | 151 |
| **2** | S2.3 | Government Data Portal Platform | 3 | 10 | 42 | 173 | 149 |
| **2** | S2.4 | Enterprise Data Portal & Self-Service Analytics | 3 | 10 | 41 | 163 | 141 |
| **2** | S2.5 | Secure Data Exchange - API Gateway | 3 | 9 | 38 | 148 | 128 |
| **2** | S2.6 | Analytics and Visualization Solutions | 3 | 10 | 44 | 155 | 133 |
| | | **Pillar 2 Subtotal** | **20** | **63** | **273** | **1,060** | **916** |
| **3** | S3.1 | DGO as a Service | 3 | 9 | 35 | 125 | 107 |
| **3** | S3.2 | Data Literacy & Culture Program | 3 | 8 | 32 | 97 | 84 |
| **3** | S3.3 | Data Management Certified Training | 3 | 7 | 25 | 78 | 70 |
| **3** | S3.4 | Knowledge Transfer & Thought Leadership | 2 | 5 | 17 | 25 | 25 |
| | | **Pillar 3 Subtotal** | **11** | **29** | **109** | **325** | **286** |
| | | **GRAND TOTAL** | **46** | **141** | **563** | **1,951** | **1,659** |

---

## Notes

### Complexity Scaling Guide

Semua estimasi dalam dokumen ini menggunakan **kompleksitas menengah (1.0x)** sebagai default. Untuk menyesuaikan:

| Scenario | Multiplier | Contoh |
| :--- | ---: | :--- |
| Startup / SME sederhana | 0.7x | Scope kecil, 1-2 data domain, infrastruktur cloud existing |
| **Enterprise menengah (default)** | **1.0x** | **Multi-departemen, 5-10 data domain, mixed infrastructure** |
| Enterprise besar / BUMN | 1.4x | Multi-unit bisnis, legacy systems, regulasi ketat |
| Government / multi-stakeholder | 1.8x | Multi-OPD, birokrasi tinggi, integrasi lintas-instansi |

### RASCI Role Abbreviation Master List

| Abbr. | Full Role Name |
| :--- | :--- |
| BA | Business Analyst (Data) |
| BEE | Product Engineering Back-End Engineer |
| BID | BI Developer |
| CDO | Chief Data Officer (CDO) |
| CM | Change Manager (Data) |
| CO | Compliance Officer (Data) |
| DA | Data Architect |
| DAn | Data Analyst |
| DBA | Database Administrator |
| DE | Data Engineer |
| DGA | Data Governance Analyst |
| DGM | Data Governance Manager |
| DLC | Data Literacy Champion |
| DO | Data Owner |
| DPO | Data Protection Officer (DPO) |
| DQA | Data Quality Analyst |
| DQE | Data Quality Engineer |
| DQM | Data Quality Manager |
| DS | Data Scientist |
| DSM | Data Security Manager |
| DVS | Data Visualization Specialist |
| FEE | Product Engineering Front-End Engineer |
| MM | Metadata Manager |
| PD | Product Designer |
| PM | Project Manager (Data) / Product Manager |
| PW | Product Writer |
| QA | Product Engineering QA Analyst |
| SRE | Site Reliability Engineer (DevOps) |

### Service Tier → WBS Feature Mapping

Beberapa layanan memiliki paket bertingkat (Service Tiers) yang didefinisikan di `services-catalog.md`. Berikut panduan pemetaan tier ke fitur WBS:

| Service | Tier | WBS Features yang Digunakan | Effort Multiplier |
| :--- | :--- | :--- | ---: |
| S1.1 | Essential Assessment | Feature A only | 0.6x |
| S1.1 | Comprehensive Strategy | Feature A + B | 1.0x |
| S1.1 | Strategic Partnership | Feature A + B + C + quarterly retainer | 1.3x |
| S1.2 | Compliance Foundation | Feature A + subset B | 0.5x |
| S1.2 | Comprehensive Framework | Feature A + B + C | 1.0x |
| S1.2 | Framework Implementation Support | Feature A + B + C + change mgmt | 1.3x |
| S1.2 | ISO Compliance Accelerator | Feature A + B (ISO focus) | 0.8x |
| S1.4 | SOP Foundation | Feature A + subset B (7 SOP krusial) | 0.5x |
| S1.4 | Comprehensive SOP Framework | Feature A + B + C (17 SOP lengkap) | 1.0x |

### Delivery Process Mapping (Frontstage / Backstage)

Setiap Feature dalam WBS dapat dipetakan ke model Frontstage/Backstage yang didefinisikan di `services-catalog.md`:

| WBS Feature Pattern | Frontstage Activities | Backstage Activities |
| :--- | :--- | :--- |
| Feature A (Discovery & Planning) | Kick-off, Stakeholder Interview, Workshop | Analisis Dokumen, Benchmarking, Gap Analysis |
| Feature B (Development & Build) | Workshop Desain, Sesi Validasi | Penyusunan Draf, Pengembangan Templat, Review Internal |
| Feature C (Review, Socialization & Handover) | Presentasi Final, Sosialisasi, Serah Terima | Kompilasi Dokumen, Quality Review, Lessons Learned |

### Commercial Model → Payment Milestone Mapping

Model komersial per layanan (dari `services-catalog.md`) dipetakan ke milestone pembayaran (Termin) dalam WBS:

| Commercial Model | Milestone Mapping | Typical Termin Split |
| :--- | :--- | :--- |
| **Fixed-Price** | M1 → Termin 1, M2 → Termin 2, M3 → Termin 3 | 30% / 40% / 30% |
| **Time & Material** | Monthly invoicing based on actual man-days consumed | Per sprint/month |
| **Retainer** | Monthly fixed fee, scope adjusted per governance cycle | Monthly |
| **Fixed + Retainer** | Fixed for initial project, Retainer for ongoing support | Project: 30/40/30, Retainer: monthly |

### IDEAS Product Platform → Service Mapping

Produk platform IDEAS (dari `services-catalog.md`) mendukung implementasi layanan berikut:

| Product | Relevant Services | WBS Integration Point |
| :--- | :--- | :--- |
| IDEAS Data Engine (13 modules) | S2.2, S2.4, S2.5 | S2.2 Feature B (Platform Build) |
| IDEAS Collect | S2.2, S2.4 | S2.1 Feature B (Data Collection) |
| IDEAS Data Hub | S2.2, S2.4 | S2.2 Feature B (Integration Layer) |
| IDEAS DataSpace | S2.2, S2.5 | S2.2 Feature C (Collaboration) |
| IDEAS Control Center | S2.2, S3.1 | S3.1 Feature B (Monitoring) |
| IDEAS Executive | S2.6, S1.1 | S2.6 Feature B (Dashboard Build) |
| IDEAS Civic Insight | S2.3, S2.6 | S2.3 Feature B (Portal Build) |
| IDEAS MapEdge | S2.3, S2.6 | S2.3 Feature C (Geospatial Module) |

### CRISP-DM Phase Mapping for S2.6

Layanan S2.6 (Analytics and Visualization Solutions) mengikuti metodologi **CRISP-DM** (lihat `agile-work-hierarchy.md`):

| CRISP-DM Phase | WBS Mapping | Feature |
| :--- | :--- | :--- |
| Business Understanding | S2.6 Feature A (Discovery) | S2.6-01 to S2.6-03 |
| Data Understanding | S2.6 Feature A (Data Profiling) | S2.6-03 to S2.6-04 |
| Data Preparation | S2.6 Feature B (ETL/Transform) | S2.6-04 to S2.6-06 |
| Modeling | S2.6 Feature B (Analytics Build) | S2.6-06 to S2.6-08 |
| Evaluation | S2.6 Feature C (UAT & Review) | S2.6-09 to S2.6-10 |
| Deployment | S2.6 Feature C (Go-Live) | S2.6-10 to S2.6-12 |

### Regulatory Compliance Integration

Subtask-subtask berikut secara implisit mencakup kepatuhan regulasi Indonesia:

| Regulasi | Applicable Services | Key WBS Tasks |
| :--- | :--- | :--- |
| **UU PDP (UU 27/2022)** | S1.2, S1.4 | S1.2-04 (Privacy framework), S1.4-04C (Security/Privacy SOPs) |
| **Perpres 46/2025 (Pengadaan)** | All (pricing) | Reflected in `rab-hps-methodology.md` and payment milestones |
| **SPBE (Perpres 132/2022)** | S1.2, S1.4, S2.3 | S2.3-01 (SPBE alignment), S1.2-03 (Governance framework) |
| **Satu Data Indonesia (Perpres 39/2019)** | S2.3, S2.4 | S2.3-02 (Data standards), S2.4-03 (Catalog standards) |
| **DTSEN (Draft)** | S1.1, S2.2 | S1.1-02 (Strategy alignment), S2.2-01 (Architecture) |

> **Catatan:** Untuk setiap proyek pemerintah, tambahkan **compliance verification subtask** di Feature C setiap layanan. Estimasi tambahan: 2-3 man-days per regulasi yang berlaku.

### Bundled Service Planning Guide

Untuk paket layanan bundel (dari `services-catalog.md`), gunakan panduan berikut:

| Bundle | Services | Total Est. MD | Shared Features | Efficiency Gain |
| :--- | :--- | :--- | :--- | :--- |
| SPBE Score Improvement | S1.2+S1.4+S2.3+S3.2 | 598 | Discovery & Planning overlap | 15-20% |
| Data Governance Foundation | S1.1+S1.2+S1.4+S3.1 | 612 | Governance framework shared | 20-25% |
| Data Platform Modernization | S1.1+S2.2+S2.4+S2.5 | 603 | Architecture shared | 15-20% |
| Open Data Ecosystem | S1.1+S2.3+S2.6+S3.2 | 534 | Data catalog shared | 10-15% |

> **Catatan:** Efficiency gain berasal dari shared discovery, reusable deliverables, dan reduced context-switching. Gunakan `scripts/pricing_engine.py` untuk kalkulasi otomatis.

### PMBOK WBS Best Practices Applied

Dokumen WBS ini mengikuti best practices dari PMBOK 6th Edition (Section 5.4 — Create WBS) dan PMBOK 7th Edition (Planning Performance Domain):

| PMBOK Best Practice | Implementasi dalam Dokumen Ini |
| :--- | :--- |
| **100% Rule** | Setiap Epic (Service) = jumlah seluruh Features; setiap Feature = jumlah seluruh Tasks; setiap Task = jumlah seluruh Subtasks. Tidak ada pekerjaan yang hilang atau duplikat. |
| **Work Package Definition** | Setiap Task (Level 4-5) adalah work package terkecil yang dapat diestimasi, di-assign, dan di-track. Durasi 1-5 hari, memiliki role assignment dan story points. |
| **Control Account** | Setiap Feature berfungsi sebagai Control Account untuk EVM tracking. Budget dan schedule dimonitor pada level ini. |
| **WBS Dictionary** | Informasi pendukung per work package: deskripsi, role, man-days, SP, predecessor, execution mode, dan output deliverable. |
| **Decomposition Guidelines** | Dekomposisi berhenti ketika: (a) item dapat diestimasi dengan akurasi memadai, (b) item dapat di-assign ke satu orang, (c) durasi 2-8 jam (subtask level). |
| **Rolling Wave Planning** | Untuk proyek multi-fase, Feature A (Discovery) di-dekomposisi detail di awal; Feature B dan C di-refine setelah Discovery selesai. |

### EVM Integration Guide

Untuk proyek berdurasi >3 bulan atau >200 man-days, Earned Value Management (EVM) diterapkan menggunakan struktur WBS ini sebagai basis pengukuran. Lihat `thought-leadership-frameworks.md` Section 17.6 untuk detail metrik EVM.

| WBS Level | EVM Element | Pengukuran |
| :--- | :--- | :--- |
| **Epic (Service)** | Budget at Completion (BAC) | Total COGS per service dari `cogs-methodology.md` |
| **Feature** | Control Account | PV, EV, AC diukur per Feature |
| **Task** | Work Package | % complete berdasarkan deliverable acceptance |
| **Subtask** | Activity | Hours logged vs planned |

Perhitungan EVM per milestone:

```
PV (Planned Value)  = BAC × % pekerjaan yang dijadwalkan selesai pada titik waktu
EV (Earned Value)   = BAC × % pekerjaan yang benar-benar selesai (deliverable accepted)
AC (Actual Cost)    = Actual man-days × daily rate + operational costs
CPI                 = EV / AC  (≥1.0 = on/under budget)
SPI                 = EV / PV  (≥1.0 = on/ahead of schedule)
EAC                 = BAC / CPI (projected total cost)
```

Health thresholds: CPI ≥ 0.9 dan SPI ≥ 0.9 dianggap sehat. Di bawah 0.8 memerlukan corrective action dan eskalasi ke steering committee.

### PMBOK Process Group Mapping per Feature Pattern

Setiap Feature pattern dalam WBS ini dapat dipetakan ke PMBOK Process Groups untuk memastikan governance yang tepat:

| Feature Pattern | Dominant Process Group | PMBOK Activities |
| :--- | :--- | :--- |
| **Feature A (Discovery & Planning)** | Initiating + Planning | Project Charter, Stakeholder Register, WBS creation, Risk identification |
| **Feature B (Development & Build)** | Executing | Direct & Manage Work, Quality Assurance, Team Development |
| **Feature C (Review, Socialization & Handover)** | Monitoring & Controlling + Closing | Validate Scope, Control Quality, Close Project, Lessons Learned |

### Cross-References

- **Agile Hierarchy**: See `agile-work-hierarchy.md` for Initiative → Epic → Feature → Task → Subtask definitions and PMBOK-Aligned Project Governance Framework
- **Deliverable Mapping**: See `service-deliverables-map.md` for DAMA deliverable-to-service mapping
- **Lifecycle Stages**: See `digital-data-product-lifecycle.md` for lifecycle stage definitions
- **Role Details**: See `human-resources-and-pricing.md` for full role descriptions & rate cards
- **COGS Calculation**: See `cogs-methodology.md` for man-day to cost conversion
- **RAB/HPS**: See `rab-hps-methodology.md` for government pricing formation
- **Output Templates**: See `output-deliverable-template.md` for standardized deliverable format
- **Sprint Planning**: SP values enable velocity-based sprint planning (typical sprint = 2 weeks, team velocity = 40-60 SP)
- **Service Catalog**: See `services-catalog.md` for service tiers, delivery processes, commercial models, and product platform
- **Regulatory Standards**: See `regulatory-standards.md` for full regulatory compliance details
- **Bundled Packages**: See `services-catalog.md` → Bundled Service Packages for mission-oriented bundles
- **PMBOK Frameworks**: See `thought-leadership-frameworks.md` Section 17 for comprehensive PMBOK 6th/7th Edition frameworks, EVM details, and tailoring guidance
- **PMBOK Governance**: See `agile-work-hierarchy.md` → PMBOK-Aligned Project Governance Framework for process group mapping and sector-specific tailoring
- **DAMA-DMBOK 3.0**: New topics (AI governance, cloud data management, data fabric/mesh) will require WBS updates when published (target Q2 2027)
- **Deloitte Data Valuation**: See `thought-leadership-frameworks.md` for Income/Cost/Market approaches applicable to S1.5

---

## Glossary of Key Terms

| Term | Definition |
| :--- | :--- |
| **BAST** | Berita Acara Serah Terima — Handover Report |
| **Control Account** | EVM tracking point at Feature level |
| **CPI** | Cost Performance Index (EV/AC) |
| **EVM** | Earned Value Management |
| **FS** | Finish-to-Start dependency |
| **RASCI** | Responsible, Accountable, Supportive, Consulted, Informed |
| **SP** | Story Points — relative effort estimate |
| **SPI** | Schedule Performance Index (EV/PV) |
| **WBS** | Work Breakdown Structure |


## Cross-Skill Task Integration

When decomposing tasks, consider which companion skill handles each sub-task:

- **Data Collection Tasks** → Delegate to `web-scraper` (scraping, crawling, pipeline processing)
- **Theoretical Framework Tasks** → Delegate to `dama-research` (KA analysis, maturity assessment, deliverable templates)
- **Practical Delivery Tasks** → Handle within `ideas-company` (proposals, pricing, document generation)
- **Validation Tasks** → Use `dama-research` KA-11 for quality dimensions, `web-scraper/data_pipeline.py` for automated validation
