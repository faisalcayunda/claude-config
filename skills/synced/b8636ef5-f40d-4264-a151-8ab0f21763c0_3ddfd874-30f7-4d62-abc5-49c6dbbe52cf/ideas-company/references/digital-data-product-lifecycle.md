# Digital & Data Product Lifecycle Management for IDEAS Services

**Last Updated: February 2026**

## Table of Contents

1. [Overview](#overview)
2. [Digital Product Lifecycle](#digital-product-lifecycle)
3. [Data Product Lifecycle](#data-product-lifecycle)
4. [Data Product Canvas](#data-product-canvas)
5. [Agile Methodology for Data Products](#agile-methodology-for-data-products)
6. [Dual-Track Agile: Discovery + Delivery](#dual-track-agile-discovery--delivery)
7. [Scaling Frameworks](#scaling-frameworks)
8. [IDEAS Service Alignment](#ideas-service-alignment)
9. [Glossary of Terms](#glossary-of-terms)
10. [Sources & References](#sources--references)

---

## Overview

Dokumen ini menyediakan kerangka kerja komprehensif untuk mengelola siklus hidup produk digital dan produk data dalam konteks layanan IDEAS. Kerangka ini mengintegrasikan best practices dari Digital Product Management, Data Product Management, Data Mesh Architecture, dan Agile Methodology — disesuaikan untuk kebutuhan klien pemerintah, BUMN, dan enterprise di Indonesia.

IDEAS menerapkan pendekatan **Product Thinking** dalam setiap engagement, di mana setiap deliverable diperlakukan sebagai produk yang memiliki pengguna, nilai bisnis, dan siklus hidup yang jelas. Pendekatan ini memastikan bahwa setiap output tidak hanya memenuhi spesifikasi teknis, tetapi juga memberikan dampak terukur bagi organisasi klien.

---

## Digital Product Lifecycle

### Definisi

Produk digital adalah setiap perangkat lunak, aplikasi, atau layanan yang disampaikan secara elektronik dan memberikan nilai kepada pengguna. Dalam konteks IDEAS, produk digital mencakup platform data, portal pemerintah, dashboard analitik, dan API gateway.

### Tahapan Lifecycle

| Tahap | Deskripsi | Aktivitas Kunci | IDEAS Service |
| :--- | :--- | :--- | :--- |
| **1. Ideation** | Identifikasi peluang dan kebutuhan pengguna | Market research, stakeholder interviews, problem framing | S1.1, S1.3 |
| **2. Discovery** | Validasi ide melalui riset dan prototyping | User research, competitive analysis, concept testing, feasibility study | S1.1, S1.2 |
| **3. Planning** | Perencanaan strategis dan roadmap | Product vision, OKR definition, roadmap creation, resource planning | S1.1, S1.4 |
| **4. Development** | Pembangunan produk secara iteratif | Agile sprints, CI/CD, quality assurance, governance-by-design | S2.1, S2.2, S2.3 |
| **5. Launch** | Peluncuran produk ke pengguna | Deployment, user onboarding, training, change management | S2.1, S3.1, S3.2 |
| **6. Growth** | Peningkatan adopsi dan fitur | Feature enhancement, user feedback loops, analytics-driven optimization | S2.4, S2.6 |
| **7. Maturity** | Stabilisasi dan optimasi | Performance tuning, cost optimization, governance strengthening | S3.1, S3.3 |
| **8. Sunset/Evolution** | Pensiun atau transformasi produk | Migration planning, data archival, next-gen planning | S1.1, S2.2 |

### Framework Referensi

Beberapa framework yang digunakan IDEAS dalam mengelola siklus hidup produk digital meliputi Pragmatic Institute Framework yang menekankan market-driven approach, SVPG Product Operating Model yang berfokus pada empowered product teams, Stage-Gate Model yang menyediakan decision gates di setiap tahap, serta Mind the Product's Four Lifecycles yang membedakan antara project, development, product, dan investment lifecycle.

---

## Data Product Lifecycle

### Definisi

Berdasarkan arsitektur Data Mesh, data product didefinisikan sebagai unit data yang otonom, terstandarisasi, dapat ditemukan, dipahami, dan diakses secara mandiri, serta memiliki nilai guna yang jelas. [9] Nilai utamanya terletak pada data itu sendiri, bukan pada antarmuka atau fungsionalitas perangkat lunak. Setiap data product memiliki pemilik yang jelas, SLA, dan dokumentasi yang lengkap.

### Tipe Data Product

| Tipe | Contoh | IDEAS Service |
| :--- | :--- | :--- |
| Database table/view | Master data pelanggan, reference data | S2.2, S2.4 |
| Data stream | Real-time event stream, CDC | S2.5, S2.2 |
| Simple files (CSV, Excel, Parquet) | Dataset terbuka pemerintah | S2.3, S2.4 |
| REST API | Data exchange endpoint | S2.5 |
| Visualization/Dashboard | Executive dashboard, operational report | S2.6, S2.4 |
| ML Features/Model | Predictive model, recommendation engine | S2.1 |

### Klasifikasi Data Product (Data Mesh)

Data product diklasifikasikan berdasarkan posisinya dalam data mesh architecture menjadi tiga kategori utama. **Source-aligned** data product mengekspos data dari sistem operasional domain asalnya dalam format yang mudah dikonsumsi. **Aggregate** data product menggabungkan data dari beberapa source-aligned product untuk menghasilkan insight lintas domain. **Consumer-aligned** data product dirancang khusus untuk memenuhi kebutuhan use case tertentu, seperti dashboard atau ML feature store.

### Tahapan Data Product Lifecycle

| Tahap | Aktivitas | Output Deliverable | DAMA KA |
| :--- | :--- | :--- | :--- |
| **1. Identify** | Identifikasi kebutuhan data, use case mapping | Data Product Canvas, Use Case Documentation | KA-01, KA-02 |
| **2. Define** | Spesifikasi produk, data contract | Data Product Specification, Data Contract, Data Dictionary | KA-03, KA-06, KA-09 |
| **3. Design** | Arsitektur, data model, security | Data Architecture Blueprint, Data Model, Access Control | KA-02, KA-03, KA-05 |
| **4. Build** | Implementasi pipeline, transformasi | ETL Documentation, Integration Job, Source-to-Target Mapping | KA-04, KA-06, KA-08 |
| **5. Test** | Validasi kualitas, profiling | Data Quality Rules, Profiling Results, Test Report | KA-11, KA-06 |
| **6. Deploy** | Peluncuran, monitoring setup | Operational Runbook, SLA Documentation, Monitoring Config | KA-04, KA-01 |
| **7. Operate** | Monitoring, incident response | Data Quality Scorecard, Issue Log, Governance Metrics | KA-11, KA-01 |
| **8. Evolve** | Iterasi, enhancement, retirement | Change Request Log, Model Change Log, Remediation Plan | KA-01, KA-03, KA-11 |

---

## Data Product Canvas

### Sumber

Framework ini berasal dari datamesh-architecture.com, dikembangkan oleh J. Majchrzak et al., dan dilisensikan di bawah CC BY 4.0. [10]

### 8 Building Blocks

Data Product Canvas terdiri dari 8 building block yang direkomendasikan untuk diisi dalam urutan workshop berikut.

**1. Domain** mendefinisikan siapa yang bertanggung jawab atas data product ini, siapa yang menentukan requirements, dan siapa yang memperbaiki ketika terjadi masalah. Ini adalah fondasi akuntabilitas.

**2. Data Product Name** menetapkan nama unik yang mengikuti naming strategy organisasi. Nama harus deskriptif dan konsisten.

**3. Consumer and Use Case(s)** menjelaskan alasan keberadaan data product ini. Mengikuti prinsip Product Thinking, dimulai dari kebutuhan konsumen, bukan dari data yang tersedia.

**4. Data Contract** mendefinisikan output ports (tabel, file, API, visualisasi), terms, data model, dan semantik. Ini adalah perjanjian formal antara producer dan consumer. IDEAS recommends using the **Open Data Contract Standard (ODCS) v3.1.0**, released by Bitol and the Linux Foundation in December 2025, as the baseline for data contracts, which provides a standardized, vendor-neutral specification.

**5. Sources** mengidentifikasi input ports, yaitu sistem operasional sumber atau data product lain (internal maupun eksternal) yang menjadi bahan baku.

**6. Data Product Architecture** menggambarkan internal antara input dan output ports, mencakup ingestion, storage, transport, wrangling, cleaning, transformasi, enrichment, dan analytics.

**7. Ubiquitous Language** memastikan bahasa yang sama digunakan oleh semua pihak yang terlibat, termasuk terminologi domain yang disepakati bersama.

**8. Classification** menentukan apakah data product ini bersifat source-aligned, aggregate, atau consumer-aligned.

### Penerapan di IDEAS

IDEAS menerapkan Data Product Canvas dalam service S2.1 (Data-Centric Digital Product Development), S2.2 (Core Data Platform), dan S2.4 (Enterprise Data Portal). Canvas ini digunakan pada tahap Discovery dan Define untuk memastikan setiap data product yang dibangun memiliki value proposition yang jelas dan arsitektur yang terstruktur.

> **Cross-Reference:** Untuk template data product canvas, lihat `templates/data-product-canvas-template.md`.

### GenAI-Enhanced Data Products (2025-2026 Evolution)

As of early 2026, data products are increasingly enriched with GenAI capabilities. This evolution requires a strong foundation in Responsible AI, including robust guardrails and a focus on data quality for training and fine-tuning Large Language Models (LLMs).

| Enhancement | Description | IDEAS Implementation |
| :--- | :--- | :--- |
| **AI-Powered Data Discovery** | Natural language queries for finding data products | IDEAS DataSpace semantic search |
| **Auto-Generated Documentation** | LLMs generate data dictionary and lineage documents | IDEAS Executive narrative generation |
| **Intelligent Data Quality** | GenAI-powered anomaly detection and auto-cleansing | IDEAS Collect NLP validation |
| **Conversational Analytics** | Chat-based interface for data exploration | IDEAS Executive AI insights |
| **Smart Data Contracts** | Auto-generation of contracts from schema analysis | ODCS-compliant contract templates |

#### Responsible AI & Guardrails

Implementing GenAI enhancements mandates a "secure-by-design" approach, incorporating guardrails to mitigate risks associated with LLMs. These are not merely technical controls but part of a comprehensive governance strategy.

| Guardrail Category | Specific Controls | IDEAS Service Alignment |
| :--- | :--- | :--- |
| **Input/Output Filtering** | PII detection & masking, harmful content filters | S2.1, S2.2 |
| **Hallucination Detection** | Fact-checking against knowledge bases, confidence scoring | S2.6, S3.1 |
| **Bias Mitigation** | Fairness metrics, demographic analysis of outputs | S1.2, S1.4 |
| **Prompt Injection Defense** | Instruction defense, input sanitization | S2.1, S2.5 |
| **Usage Monitoring** | Token usage tracking, cost control, audit trails | S3.1, S3.3 |

#### Data Quality for LLMs

The principle of "Garbage In, Garbage Out" is amplified with GenAI. The quality of the underlying data used for Retrieval-Augmented Generation (RAG) or fine-tuning is paramount.

- **Relevance:** Is the data relevant to the target domain and use case?
- **Accuracy:** Is the data factually correct and up-to-date?
- **Completeness:** Does the data cover the breadth of topics required?
- **Diversity:** Does the data represent a wide range of perspectives to avoid bias?
- **Safety:** Has the data been cleansed of PII, toxicity, and harmful content?

**Governance Prerequisite:** Before activating GenAI capabilities, a data product must meet a minimum maturity of Level 3 (Defined) on the DAMA maturity model, with a data quality score ≥ 80% and an established governance framework. Refer to `references/regulatory-standards.md` for AI governance standards (NIST AI RMF, ISO 42001) and `references/service-delivery-patterns.md` for specific checklists.

---

## Agile Methodology for Data Products

### Prinsip Dasar

IDEAS menerapkan Agile methodology yang diadaptasi untuk konteks data management, mengakui bahwa proyek data memiliki karakteristik unik dibandingkan pengembangan perangkat lunak tradisional. Ketidakpastian kualitas data, kompleksitas integrasi, dan kebutuhan governance memerlukan pendekatan yang lebih fleksibel namun tetap terstruktur.

### Framework Pilihan per Konteks

| Konteks | Framework | Alasan |
| :--- | :--- | :--- |
| Tim kecil (3-7 orang), single product | **Scrum** | Struktur sprint yang jelas, ceremonies yang terdefinisi |
| Tim dengan flow continuous, maintenance | **Kanban** | Fleksibilitas, WIP limits, continuous delivery |
| Multi-tim, enterprise scale | **SAFe** | Alignment portfolio-to-team, PI planning |
| Startup/innovation context | **Dual-Track Agile** | Parallel discovery + delivery |
| Government procurement (POLRI, Jabar) | **Hybrid Waterfall-Agile** | Milestone-based delivery sesuai kontrak, iterative execution |

### Sprint Adaptasi untuk Data Projects

Sprint untuk proyek data IDEAS diadaptasi dengan mempertimbangkan beberapa faktor khusus. Durasi sprint direkomendasikan 2 minggu untuk proyek implementasi dan 3-4 minggu untuk proyek advisory/governance. Setiap sprint harus mengalokasikan 20% kapasitas untuk data quality dan governance tasks. Definition of Done untuk data product harus mencakup data quality threshold, documentation completeness, dan governance compliance.

### Hybrid Waterfall-Agile Model in Practice

Model ini sering digunakan dalam kontrak pemerintah yang menuntut adanya milestone dan deliverable yang pasti (khas Waterfall), namun eksekusi internal dilakukan secara iteratif (Agile). 

**Contoh Implementasi:** Proyek Pembangunan Data Portal untuk Instansi X.
*   **Fase Waterfall (Kontrak):**
    1.  **M1 (Bulan 1-2):** Penyerahan Dokumen Perencanaan (Analisis Kebutuhan, Desain Arsitektur).
    2.  **M2 (Bulan 3-5):** Penyerahan Prototipe dan UAT (User Acceptance Test) Tahap 1.
    3.  **M3 (Bulan 6):** Peluncuran versi final dan serah terima (BAST).
*   **Fase Agile (Internal IDEAS):**
    *   Tim bekerja dalam **sprint 2 mingguan**.
    *   **Sprint 1-4:** Fokus pada deliverable M1, menghasilkan iterasi dokumen arsitektur dan backlog untuk pengembangan.
    *   **Sprint 5-10:** Fokus pada pengembangan prototipe untuk M2, dengan demo setiap akhir sprint kepada Product Owner internal.
    *   **Sprint 11-12:** Fokus pada finalisasi, bug fixing, dan persiapan deployment untuk M3.

Pendekatan ini memberikan kepastian bagi klien pemerintah sekaligus memungkinkan fleksibilitas dan adaptasi bagi tim development.

---

## Dual-Track Agile: Discovery + Delivery

### Konsep

Dual-Track Agile memisahkan proses pengembangan menjadi dua track paralel yang berjalan bersamaan. **Discovery Track** berfokus pada eksplorasi dan validasi ide baru melalui riset pengguna, prototyping, dan eksperimen. **Delivery Track** berfokus pada pembangunan dan pengiriman produk berkualitas tinggi secara iteratif.

### Penerapan di IDEAS

| Track | Aktivitas | Peran Utama | Output |
| :--- | :--- | :--- | :--- |
| **Discovery** | User research, data profiling, feasibility study, prototype | Business Analyst, Data Analyst, UX Designer | User stories, data product canvas, prototype |
| **Delivery** | Sprint execution, CI/CD, testing, deployment | Data Engineer, Developer, QA | Working increment, documentation, deployed product |

### Validasi 4 Risiko (SVPG Model)

Setiap data product yang dikembangkan IDEAS harus melewati validasi empat risiko utama. **Value Risk** memastikan bahwa pengguna benar-benar membutuhkan dan akan menggunakan produk ini. **Usability Risk** memastikan bahwa pengguna dapat menggunakan produk dengan mudah. **Feasibility Risk** memastikan bahwa tim teknis dapat membangun produk ini dengan teknologi dan data yang tersedia. **Viability Risk** memastikan bahwa produk ini layak secara bisnis dan sesuai dengan regulasi.

---

## Scaling Frameworks

### SAFe untuk Enterprise Data Programs

Untuk program data berskala enterprise (seperti Ekosistem Data Jabar dengan 46 OPD), IDEAS menerapkan elemen SAFe yang relevan.

| Level SAFe | Penerapan IDEAS | Contoh |
| :--- | :--- | :--- |
| **Portfolio** | Strategic themes, investment themes | "Mewujudkan Satu Data Jawa Barat" |
| **Large Solution** | Solution train, capabilities | Platform Data Jabar (12 capabilities) |
| **Program** | Agile Release Train (ART), PI Planning | ART "Data Services" (4 squads) |
| **Team** | Scrum/Kanban, Iterations | Squad "Data Quality" (2-week sprints) |

### Data Mesh Implementation Case: DTO Kemenkes RI

The Indonesian Ministry of Health's Digital Transformation Office (DTO Kemenkes RI) has implemented Data Mesh architecture, providing a local reference case for IDEAS. This demonstrates that Data Mesh principles are applicable in the Indonesian government context, not just in Western enterprise settings.

### Modern Data Catalog & Governance Tools Landscape

| Tool | Category | Strengths | IDEAS Context |
| :--- | :--- | :--- | :--- |
| Collibra | Enterprise Data Governance | Comprehensive, enterprise-grade | Reference for enterprise clients |
| Atlan | Modern Data Catalog | API-first, modern UI, active metadata | Competitor awareness |
| Alation | Data Catalog & Intelligence | Strong catalog, ML-powered | Competitor awareness |
| CKAN | Open Data Portal | Open-source, government standard | Used in IDEAS platform (data.go.id) |
| DataHub | Metadata Platform | Open-source, LinkedIn-backed | Alternative for enterprise |

### Spotify Model untuk Squad-Based Delivery

IDEAS mengadopsi elemen Spotify Model untuk delivery berbasis squad, khususnya pada proyek besar. **Squad** adalah tim cross-functional yang bertanggung jawab atas satu area produk (misalnya Squad Data Quality, Squad Portal). **Tribe** adalah kumpulan squad yang bekerja pada domain terkait. **Chapter** menghubungkan spesialis dengan peran yang sama lintas squad (misalnya Chapter Data Engineer). **Guild** adalah komunitas praktik lintas tribe untuk berbagi pengetahuan.

---

## IDEAS Service Alignment

### Mapping Service ke Lifecycle Stage

| IDEAS Service | Digital Product Stage | Data Product Stage | Primary Methodology |
| :--- | :--- | :--- | :--- |
| S1.1 Data Strategy & Roadmap | Ideation, Discovery, Planning | Identify | Advisory workshop |
| S1.2 Data Governance & Compliance | Planning | Define, Operate | Governance framework |
| S1.3 Data Maturity Assessment | Discovery | Identify | Assessment methodology |
| S1.4 Data Governance & Policy | Planning | Define | Policy development |
| S1.5 Data Asset Valuation | Discovery, Planning | Identify, Define | Infonomics, Advisory |
| S2.1 Digital Product Development | Development, Launch | Build, Test, Deploy | Dual-Track Agile |
| S2.2 Core Data Platform | Development | Design, Build, Deploy | Scrum/Kanban |
| S2.3 Government Data Portal | Development, Launch | Build, Deploy | Hybrid Waterfall-Agile |
| S2.4 Enterprise Data Portal | Development, Growth | Build, Deploy, Operate | Scrum |
| S2.5 Data Exchange & API Gateway | Development | Design, Build | Scrum/Kanban |
| S2.6 Analytics & Visualization | Development, Growth | Build, Operate | Kanban |
| S3.1 DGO as a Service | Maturity | Operate, Evolve | Kanban |
| S3.2 Data Literacy & Culture | Launch, Growth | — | Workshop-based |
| S3.3 Certified Training | — | — | Curriculum-based |
| S3.4 Knowledge Transfer | — | — | Engagement-based |

### Practical Integration Example: Launching a New Government Data Service

**Scenario:** A provincial government wants to launch a new public-facing dashboard to track infrastructure project progress, integrating data from 5 different agencies.

1.  **Phase 1: Strategy & Discovery (S1.1, S1.3, S1.5)**
    *   IDEAS conducts workshops to align the dashboard with the governor's strategic goals (RPJMD).
    *   A Data Maturity Assessment reveals significant data quality issues in two agencies.
    *   A preliminary Data Asset Valuation (using the Cost Approach from the Deloitte 2025 framework) justifies the project budget by estimating the replacement cost of the data to be integrated.
2.  **Phase 2: Governance & Planning (S1.2, S1.4)**
    *   A Data Governance charter is established with data stewards from each agency.
    *   Policies for data sharing, quality standards (adopting ODPQ), and access control are drafted.
3.  **Phase 3: Development & Launch (S2.2, S2.6, S3.2)**
    *   A Core Data Platform ingests and cleanses the data from the 5 agencies.
    *   An Analytics & Visualization squad builds the dashboard iteratively using Scrum.
    *   IDEAS provides Data Literacy training to agency staff to ensure they can maintain the data flow.
4.  **Phase 4: Operation & Evolution (S3.1)**
    *   The IDEAS DGO-as-a-Service team monitors data quality, manages user access, and provides monthly performance reports to the governor's office.

---

## IDEAS Product Platform — Lifecycle Mapping

Setiap produk dalam IDEAS Data Ecosystem Platform memiliki posisi spesifik dalam lifecycle:

| Produk | Lifecycle Stage | Core Engine Modules | Primary Service |
| :--- | :--- | :--- | :--- |
| **IDEAS Collect** | Data Acquisition (Build) | Data Connector, Data Tables Engine | S2.2, S2.4 |
| **IDEAS Data Hub** | Data Integration (Build, Deploy) | Data Orchestration Hub, Data Connector | S2.2, S2.4 |
| **IDEAS DataSpace** | Data Preparation (Build, Test) | Data Quality Platform, Metadata Platform | S2.2, S2.5 |
| **IDEAS Control Center** | Data Operations (Operate, Evolve) | Data Governance Platform, Data Quality Platform | S2.2, S3.1 |
| **IDEAS Executive** | Data Consumption (Operate) | Data Analytics Platform, Global Data Search | S2.6, S1.1 |
| **IDEAS Civic Insight** | Data Dissemination (Deploy, Operate) | Data Analytics Platform, Geospatial Intelligence | S2.3, S2.6 |
| **IDEAS MapEdge** | Geospatial Analysis (Build, Operate) | Geospatial Intelligence Engine | S2.3, S2.6 |

**Keunggulan Teknologi Tertanam:**
- **AI/ML Integration:** IDEAS Executive (narrative generation), IDEAS Collect (NLP forms), IDEAS DataSpace (auto-profiling)
- **Zero-Trust Security:** Tertanam di seluruh produk melalui Data Privacy Governance Hub dan Secure Data Exchange Platform Engine
- **Privacy-by-Design:** DPIA automation, DSAR management, data masking/pseudonymization terintegrasi

---

## Adaptasi Data Product Lifecycle untuk Konteks Pemerintah Indonesia

Data product lifecycle perlu diadaptasi untuk konteks pemerintahan Indonesia yang memiliki karakteristik unik:

### Penyesuaian per Fase

| Fase Lifecycle | Adaptasi Pemerintah | Regulasi Terkait |
| :--- | :--- | :--- |
| **Discovery** | Alignment dengan RPJMD/RPJMN, identifikasi kebutuhan OPD | Perpres 39/2019 (SDI) |
| **Design** | Standar metadata SDI, klasifikasi data (terbuka/tertutup) | Perpres 39/2019, UU 27/2022 (PDP) |
| **Development** | Compliance-first development, SPBE architecture alignment | Perpres 132/2022 (Arsitektur SPBE) |
| **Testing** | Validasi kualitas data sesuai ODPQ framework | Internal standard |
| **Deployment** | Publikasi di portal data resmi, integrasi SDI | Perpres 39/2019 |
| **Monitoring** | SPBE evaluation readiness, annual assessment | Perpres 132/2022, Permenkomdigi 6/2025 |

### Contoh Data Product Pemerintah

| Data Product | Domain | Tipe | Pengguna |
| :--- | :--- | :--- | :--- |
| Dashboard APBD | Keuangan | Analytical | Kepala Daerah, DPRD |
| Portal Open Data | Multi-domain | Platform | Publik, Akademisi, Media |
| Citizen Dashboard | Layanan Publik | Operational | Masyarakat |
| Executive Dashboard | Multi-domain | Strategic | Gubernur/Bupati |
| Data Exchange API | Multi-domain | Integration | OPD, Mitra |

### Data Privacy Roles & Responsibilities (RACI Matrix Example)

Implementasi UU 27/2022 (PDP) memerlukan kejelasan peran dan tanggung jawab. Berikut adalah contoh matriks RACI sederhana:

| Aktivitas | Data Protection Officer (DPO) | Data Owner (Eselon I/II) | Data Steward (PIC Teknis) | IT Team |
| :--- | :--- | :--- | :--- | :--- |
| **Data Privacy Impact Assessment (DPIA)** | C | A | R | I |
| **Persetujuan Pemrosesan Data** | C | A | R | I |
| **Manajemen Insiden Pelanggaran Data** | A | R | C | R |
| **Pemenuhan Hak Subjek Data (DSAR)** | R | A | C | I |
| **Pelatihan Kesadaran Privasi** | A | C | R | I |

*Legenda: R=Responsible, A=Accountable, C=Consulted, I=Informed*

> **Cross-Reference:** Untuk contoh implementasi nyata, lihat `references/portfolio-showcase-jabar.md`. Untuk panduan DAMA, lihat `dama-research/guides/industry/government-public-sector-guide.md`. Untuk Data Valuation frameworks (Infonomics, Deloitte 2025), lihat `references/thought-leadership-frameworks.md` Section 18. Untuk COGS model per service, lihat `references/cogs-methodology.md`.

---

## Glossary of Terms

- **BAST:** Berita Acara Serah Terima (Handover Document).
- **CDC:** Change Data Capture.
- **DAMA KA:** Data Management Association Knowledge Area.
- **DPIA:** Data Protection Impact Assessment.
- **DSAR:** Data Subject Access Request.
- **ODPQ:** Open Data-Quality Policy and framework. A set of standards and guidelines to ensure the quality of open data, focusing on accuracy, completeness, timeliness, and accessibility.
- **PII:** Personally Identifiable Information.
- **RACI:** Responsible, Accountable, Consulted, Informed. A matrix to define roles and responsibilities.
- **RPJMD/RPJMN:** Rencana Pembangunan Jangka Menengah Daerah/Nasional (Regional/National Medium-Term Development Plan).
- **SPBE:** Sistem Pemerintahan Berbasis Elektronik (Electronic-Based Government System).

---

## Sources & References

### Digital Product Management
1. Rapptrlabs — Digital Product Management Fundamentals
2. Airfocus — What is Digital Product Management?
3. ProductPlan — What is a Digital Product Manager?
4. Coursera/UVA Darden — Digital Product Management: Modern Fundamentals
5. Pragmatic Institute — What is the Product Life Cycle?
6. SVPG — Product Management Start Here
7. Mind the Product — How to Choose the Right Product Lifecycle
8. Stage-Gate International — The Stage-Gate Model Overview

### Data Product Management
9. datamesh-architecture.com — Data Mesh Architecture
10. datamesh-architecture.com — Data Product Canvas (J. Majchrzak et al.)
11. Dylan Anderson — The Data Ecosystem Substack (Issues #29-51)
12. Gartner — Data Product Management Framework
13. Harvard Business Review — What is a Data Product?
14. McKinsey — How to Unlock the Full Value of Data
15. Zhamak Dehghani — Data Mesh: Delivering Data-Driven Value at Scale (O'Reilly)
16. Deloitte (2025) — *Valuing data as an asset*.

### Agile Methodology
17. Atlassian — Epics, Stories, Themes, and Initiatives
18. SAFe Framework — scaledagile.com
19. Scrum.org — The Scrum Guide
20. Mountain Goat Software — User Stories Applied (Mike Cohn)
21. Atlassian — Kanban vs Scrum
22. Spotify Engineering Culture (Henrik Kniberg)

### Data-Specific Agile & Governance
23. The New Stack — Agile Data Management Explained
24. DataKitchen — DataOps Cookbook
25. DAMA International (2025) — *DAMA-DMBOK 3.0 Project Charter*. (Note: DMBOK 3.0 is a multi-year project launched in 2025)
26. Bitol, Linux Foundation (2025) — *Open Data Contract Standard (ODCS) v3.1.0*.

### Indonesian Regulations
27. Peraturan Presiden No. 39 Tahun 2019 tentang Satu Data Indonesia.
28. Peraturan Presiden No. 132 Tahun 2022 tentang Arsitektur Sistem Pemerintahan Berbasis Elektronik Nasional.
29. Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP).
30. Peraturan Menteri Komunikasi dan Digital No. 6 Tahun 2025 tentang Penyelenggaraan Sistem Pemerintahan Berbasis Elektronik.
