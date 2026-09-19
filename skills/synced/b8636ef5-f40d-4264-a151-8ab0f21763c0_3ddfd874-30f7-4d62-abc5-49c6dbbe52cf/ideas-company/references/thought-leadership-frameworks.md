# Thought Leadership Frameworks — IDEAS Knowledge Arsenal

**Last Updated: February 2026**

Dokumen ini mendokumentasikan framework dan konsep yang digunakan oleh CEO IDEAS dalam paparan thought leadership dan knowledge transfer. Framework ini menjadi fondasi intelektual yang membedakan IDEAS dari kompetitor dan memposisikan perusahaan sebagai otoritas di bidang data management.

## Table of Contents

1. [MIT CISR Framework](#1-mit-cisr-framework)
2. [DAMA-DMBOK Framework](#2-dama-dmbok-framework)
3. [Dylan Anderson — The Data Ecosystem](#3-dylan-anderson--the-data-ecosystem)
4. [North Star Metric & OMTM](#4-north-star-metric--omtm)
5. [Data Fabric vs Data Mesh Hybrid](#5-data-fabric-vs-data-mesh-hybrid)
6. [Data Product & Supply Chain](#6-data-product--supply-chain)
7. [Data Management Office (DMO)](#7-data-management-office-dmo)
8. [Enterprise Data Architecture Evolution](#8-enterprise-data-architecture-evolution)
9. [HBR Digital Transformation Components](#9-hbr-digital-transformation-components)
10. [Open Data Watch Data Value Chain](#10-open-data-watch-data-value-chain)
11. [Policy Analytics Ladder](#11-policy-analytics-ladder)
12. [Data Analytics Activity Flow](#12-data-analytics-activity-flow)
13. [Executive Dashboard User Level](#13-executive-dashboard-user-level)
14. [Framework Selection Guide](#14-framework-selection-guide)
15. [Modern Data Architecture Patterns for Indonesian Context](#15-modern-data-architecture-patterns-for-indonesian-context)
16. [Change Management untuk Tata Kelola Data](#16-change-management-untuk-tata-kelola-data)
17. [PMBOK Project Management Frameworks](#17-pmbok-project-management-frameworks)
18. [Data Valuation & Infonomics Framework](#18-data-valuation--infonomics-framework)
19. [End-to-End Business Strategy Frameworks](#19-end-to-end-business-strategy-frameworks)
20. [Data Ethics Frameworks](#20-data-ethics-frameworks)
21. [Glossary of Terms](#21-glossary-of-terms)

---
## 1. MIT CISR Framework

> **Three Principles for Treating Data as a Strategic Asset** — MIT Center for Information Systems Research (Wixom & Beath, 2015) [1]

**Prinsip 1: Senior Management Must Clarify Data's Value Proposition.** Manajemen puncak harus mengartikulasikan secara eksplisit bagaimana data akan menciptakan nilai bisnis. Mekanisme penciptaan nilai meliputi: meningkatkan customer experience, menurunkan biaya operasional, diferensiasi produk inti, dan menciptakan aliran pendapatan baru.

**Prinsip 2: The Owner of Business Outcomes Should Be Charged With Data Ownership.** Pemilik data harus berada di sisi bisnis, bukan IT. Data Owner bertanggung jawab memahami data apa yang dibutuhkan (pada kualitas berapa), mengidentifikasi gap data, dan memiliki wewenang mengalokasikan sumber daya.

**Prinsip 3: The Data That Matters Must Be Curated.** Data kritis harus dikurasi dengan standar emas: master data management, data quality dashboards, auditability, dan pencegahan akses tidak sah (vault-like protection).

**Kapan Digunakan:** Saat mempresentasikan data strategy kepada C-Level, terutama untuk meyakinkan bahwa investasi data memerlukan komitmen manajemen puncak.

**Referensi Silang:** Konsep ini sangat terkait dengan [North Star Metric & OMTM](#4-north-star-metric--omtm) untuk mengukur proposisi nilai dan [End-to-End Business Strategy Frameworks](#19-end-to-end-business-strategy-frameworks) untuk penyelarasan strategis.

---
## 2. DAMA-DMBOK Framework

> **Data Management Body of Knowledge** — DAMA International, 2nd Edition [2]

IDEAS menggunakan dua representasi visual DAMA-DMBOK sebagai fondasi metodologi, yang dijelaskan lebih lanjut dalam `references/dama-integration-map.md`.

**DAMA Pyramid:** Menunjukkan hierarki dari Plan & Design → Enable & Maintain → Use & Enhance → Lifecycle Management, dengan Foundational Activities (Data Governance, Quality, Security, Metadata) sebagai penyangga. Outer ring mencakup aspek strategis seperti Culture, Strategy, dan Data Valuation.

**DAMA Wheel:** Menempatkan Data Governance di pusat, dikelilingi oleh 11 knowledge areas: Data Architecture, Data Modeling & Design, Data Storage & Operations, Data Security, Data Integration & Interoperability, Document & Content Management, Reference & Master Data, Data Warehousing & BI, Metadata, dan Data Quality.

**Definisi Data Governance (DAMA DMBOK 2nd Ed):** "Data Governance is the exercise of authority, control, and shared decision-making (planning, monitoring, and enforcement) over the management of data assets."

**Distingsi Kunci:**
-   Data Governance = **WHAT** should be done and **WHO** is responsible.
-   Data Management (11 Knowledge Areas lainnya) = **HOW** it should be done.

**Kapan Digunakan:** Sebagai fondasi utama di setiap engagement IDEAS. Selalu menjadi referensi standar global untuk semua layanan, terutama S1.1 (Data Management Maturity Assessment) dan S1.2 (Data Governance & Compliance Framework).

### Update DAMA-DMBOK 3.0 (Proyek 2025-2027)

DAMA International telah meluncurkan proyek DAMA-DMBOK 3rd Edition pada Juni 2025. Proyek ini mengadopsi model tata kelola **Triple Helix** yang melibatkan Editorial Board, CDMP Masters Review Panel, dan kontribusi komunitas global. Publikasi DMBOK 3.0 ditargetkan pada tahun 2027. IDEAS secara aktif memonitor perkembangan ini untuk memastikan metodologi tetap sejalan dengan standar global terkini.

**Topik Baru yang Diantisipasi di DMBOK 3.0:**
-   **AI Governance & Management:** Kerangka kerja untuk mengelola data dalam siklus hidup AI.
-   **Cloud Data Management:** Praktik terbaik untuk data di lingkungan cloud.
-   **Modern Data Platforms:** Pembahasan mendalam tentang arsitektur modern.
-   **Data Fabric & Data Mesh Fusion:** Konvergensi antara pendekatan terpusat dan terdesentralisasi.

**Referensi Silang:** Untuk pemetaan DAMA ke layanan IDEAS, lihat `references/dama-integration-map.md`. Untuk detail peran terkait DAMA, lihat `references/human-resources-and-pricing.md`.

---
### 3. Dylan Anderson — The Data Ecosystem

> **The Data Ecosystem Substack** — 52 Issues, Framework praktis untuk implementasi data governance, data architecture, data quality, data products, analytics, dan AI/ML [3]

Dylan Anderson (Head of Data Strategy, Profusion) adalah sumber referensi utama yang digunakan CEO IDEAS untuk framework operasional. Seluruh 52 edisi newsletter telah dipelajari dan dirangkum dalam `references/data-ecosystem-knowledge-base.md`. Framework ini sangat berharga karena sifatnya yang praktis dan langsung dapat diterapkan.

#### 3.1 Foundational Capabilities for Data Delivery
Empat lapisan: Strategic Alignment → Infrastructure/Architecture/Engineering → Data & Product Governance → Data Management.

#### 3.2 People, Process, Technology & Data (PPTD)
-   Organisational Goals/Targets di puncak
-   People → Processes → Technology → Data (base layer)
-   Saat transformasi: Data → Strategy → People → Processes → Technology → Data (cycle)
-   Ekspansi dari PPT klasik — Data sebagai dimensi keempat yang setara (Issue #17).

#### 3.3 Data Governance Strategy Framework
Tiga langkah: (1) Set out the 'Why' — Governance Vision & Direction, (2) Develop the Directional 'How' — Team Goals, Roles, Operational Principles, (3) Articulate 'What' Needs to be Done — Delivery Roadmap.

**Five-Component Data Governance Strategy** (Issue #48):
1.  **Executive Sponsorship** — C-level champion
2.  **Business Value Orientation** — Governance for value, not compliance
3.  **Operating Model** — How governance operates daily
4.  **Technology Enablement** — Tools supporting governance
5.  **Culture & Change Management** — People adoption

#### 3.4 End-to-End Data Governance Structure
Tiga tier: Centralised Management (Data Governance Office) → Cross-functional Oversight (Data Governance Council) → Federated Team (Data Owners, Data Stewards, Data Custodians). Model ini selaras dengan struktur yang diusulkan dalam layanan S3.1 (DGO as a Service).

#### 3.5 Data Governance Implementation Scorecard
Lima kategori metrik: Business Impact, Implementation Progress, Data Quality Metrics, Compliance Metrics, Adoption/Culture Metrics.

#### 3.6 Data Technology Landscape
Flow: Data Sources → Data Ingestion → Data Storage → Processing/Transformation → Serve & Access → Analytics/AI → Consumption. Dengan Orchestration layer dan Data Governance/Mgmt/Security sebagai fondasi.

**Nine-Category Technology Landscape** (Issue #20): Data Integration, Data Storage, Data Processing, Data Quality, Data Governance, Data Catalog, BI & Analytics, Data Science, Data Orchestration.

#### 3.7 Data Lifecycle
Flow: Data Generation → Data Storage & Processing → Serving → Analysis → Reintroduction or Disposal. Management layer: Metadata Management, MDM, Data Lineage & Observability.

#### 3.8 Data Quality Platform Approach (Issue #43-45)
Tiga pilar modern data quality:
-   **Detection:** Automated anomaly detection dan profiling
-   **Enforcement:** Quality gates dan validation rules
-   **Ownership:** Clear accountability per data domain

**Five Pillars of Data Observability** (Issue #44): Freshness, Distribution, Volume, Schema, Lineage. **1-10-100 Rule:** $1 to prevent, $10 to correct, $100 if left unresolved.

**Five Pillars of Data Contract** (Issue #45): Schema, Quality, SLA, Ownership, Metadata. Quality Gates: Critical (block), Warning (alert), Info (log).

#### 3.9 Data Product Framework (Issue #26-28)
**Data Product Pyramid:** Raw Data (base) → Derived Data (middle) → Analytical Products (top).

**Data Product Supply Chain:** Source → Ingest → Store → Process → Serve → Consume → Act. Four foundational capabilities: Ingestion, Storage, Processing, Serving.

**Data Product Operational Delivery Model:** Product-not-Project mindset. Key role: Data Product Manager (DPM). Iterative: Discovery → MVP → Iterate → Scale → Maintain.

#### 3.10 Business Strategy Temple (Issue #7)
Framework yang menempatkan business strategy sebagai fondasi dari seluruh inisiatif data. Foundation: Business Strategy & Objectives → Pillars: Data Strategy, Technology Strategy, People Strategy → Roof: Business Value & Outcomes.

#### 3.11 Four Levels of Analytics (Issue #29)
Descriptive (What happened?) → Diagnostic (Why?) → Predictive (What will happen?) → Prescriptive (What should we do?).

#### 3.12 Five A's of Dashboard Design (Issue #32)
Accuracy, Aesthetics, Accessibility, Actionability, Adaptability.

#### 3.13 AI Governance Framework (Issue #50-51)
Lima pilar: Enabling Value, Transparency, Operational Integrity, Ethical Responsibility, Regulatory Compliance (EU AI Act).

**Comprehensive AI Governance Stack:**

| Framework | Scope | Type | IDEAS Application |
| :--- | :--- | :--- | :--- |
| **EU AI Act (2024/1689)** | Risk-based AI regulation | Mandatory (EU) | High-risk AI classification, conformity assessment |
| **NIST AI RMF 1.0** | AI risk management (Govern, Map, Measure, Manage) | Voluntary (US) | Practical implementation guide for AI governance |
| **ISO/IEC 42001:2023** | AI Management Systems (AIMS) | Certifiable | Auditable AI governance for enterprise clients |
| **Stranas KA 2020-2045** | Indonesia national AI strategy | National policy | Alignment with government AI priorities |
| **Responsible AI (FATE)** | Fairness, Accountability, Transparency, Ethics | Principles | Embedded in all AI-related service delivery |

**GenAI-Specific Governance Considerations:**
-   **Model Risk:** Hallucination detection, output validation, human-in-the-loop requirements
-   **Data Privacy:** Training data provenance, PII in prompts, consent management (UU PDP alignment)
-   **IP & Copyright:** Generated content ownership, training data licensing
-   **Bias & Fairness:** Demographic parity testing, disparate impact analysis
-   **Security:** Prompt injection prevention, adversarial robustness, red teaming

**Regulatory Context Update (2026-2027):**
- EU AI Act fully applicable **August 2, 2026**; prohibited AI practices were banned from **February 2, 2025**, with high-risk obligations starting **August 2025**.
- NIST AI RMF 1.0 published **January 2023**; Generative AI Profile released **July 2024**
- ISO/IEC 42001:2023 published **December 2023** — first certifiable AI management standard

#### 3.14 Five Organizational Models for Data (Issue #18)
Centralized, Decentralized, Federated, Hub & Spoke, Chapter & Tribe (Spotify model).

**Referensi Utama:** Seluruh 52 issues — lihat `references/data-ecosystem-knowledge-base.md` untuk detail lengkap. Validasi pada Februari 2026 mengkonfirmasi bahwa file ini ada dan dapat diakses.

---
## 4. North Star Metric & OMTM

> **One Metric That Matters** — Konsep alignment data strategy dengan tujuan bisnis [4]

**North Star Metric (NSM)** adalah satu metrik jangka panjang yang merepresentasikan nilai inti yang diberikan perusahaan kepada pelanggan. **OMTM (One Metric That Matters)** adalah metrik taktis jangka pendek per tim yang berubah setiap 3-6 bulan untuk mendorong pencapaian NSM.

**Contoh NSM per Perusahaan:**

| Perusahaan | North Star Metric | Tipe Game |
| :--- | :--- | :--- |
| Facebook | Daily Active Users | Attention |
| Spotify | Time Spent Listening | Attention |
| Amazon | Monthly Revenue | Transaction |
| Uber | Rides per Week | Transaction |
| Slack | Messages Sent | Productivity |

**Tipe Game:** Attention (engagement), Transaction (revenue), Productivity (efficiency).

**Aplikasi untuk Klien IDEAS:** Membantu klien mendefinisikan NSM yang terkait data, misalnya: "Menggunakan data untuk mengurangi downtime kereta sebesar 20% dan meningkatkan kepuasan pelanggan sebesar 15%" (contoh KAI). Metrik terukur: IDR, %, NPS, CSAT, downtime, on-time performance.

**Kapan Digunakan:** Saat membantu klien menyusun Data Strategy dan Value Proposition (Layanan S1.5). Sangat efektif untuk C-Level yang membutuhkan kejelasan ROI dan alignment antara inisiatif data dengan tujuan bisnis utama.

**Referensi Silang:** Terhubung langsung dengan [MIT CISR Framework](#1-mit-cisr-framework) (Prinsip 1: Clarify Value Proposition) dan [Business Strategy Temple](#310-business-strategy-temple-issue-7).

---
## 5. Data Fabric vs Data Mesh Hybrid

> **Pendekatan Hybrid** — Menggabungkan kekuatan sentralisasi (Fabric) dan desentralisasi (Mesh) untuk konteks enterprise Indonesia.

### Data Fabric (Centralized, Technology-Centric)
Lapisan arsitektur yang menggunakan teknologi untuk mengintegrasikan data dari berbagai sumber secara otomatis dan cerdas. Karakteristik: Technology-Centric, Centralized Approach, Active Metadata, Intelligent Automation (AI/ML), No "Rip and Replace".

### Data Mesh (Decentralized, Organization-Centric)
Pendekatan arsitektur yang mendistribusikan kepemilikan data ke tim domain bisnis. Empat prinsip: Domain-Oriented Decentralized Data Ownership, Data as a Product, Self-Serve Data Platform, Federated Computational Governance.

### Hybrid Approach: The "Data Fabresh"
IDEAS mengadvokasikan pendekatan hybrid yang menggabungkan fondasi teknis Data Fabric dengan struktur organisasi Data Mesh. Konsep ini, kadang disebut "Data Fabresh", menjadi semakin relevan di industri.

| Aspek | Data Fabric (Fondasi Teknis) | Data Mesh (Struktur Organisasi) |
| :--- | :--- | :--- |
| **Data Integration** | Otomatisasi integrasi dari berbagai sumber (structured, unstructured). | Tim domain bertanggung jawab atas pipeline data mereka sendiri. |
| **Governance** | Standar governance global, kebijakan terpusat (centralized policies). | Tim domain mengimplementasikan kebijakan dalam konteks lokal mereka (local context). |
| **Data Access** | Lapisan akses terpadu dan aman melalui *active metadata*. | Tim domain membuat dan mempublikasikan *Data Products* yang dapat ditemukan. |
| **Innovation** | Menyediakan platform dan tools terpusat untuk inovasi. | Tim domain berinovasi dengan data mereka untuk menciptakan nilai bisnis. |

### GenAI & 2026+ Architecture Evolution

| Layer | GenAI Enhancement | IDEAS Implementation |
| :--- | :--- | :--- |
| **Active Metadata** | LLM-powered metadata enrichment, auto-classification, semantic search | IDEAS DataSpace AI auto-profiling |
| **Data Quality** | GenAI anomaly detection, automated data cleansing suggestions | IDEAS Collect NLP validation |
| **Data Contracts** | Auto-generated contracts from schema analysis (ODCS-compliant) | Federated governance enforcement |
| **Self-Serve Platform** | Natural language data discovery, conversational analytics | IDEAS Executive narrative generation |
| **Governance** | AI-assisted policy generation, automated compliance checking | NIST AI RMF + ISO 42001 alignment |
| **Context Engineering** | LLM grounding with private knowledge graphs, prompt enrichment | IDEAS Knowledge Base integration |
| **AI Observability** | Monitoring for hallucinations, bias drift, and operational metrics | IDEAS Responsible AI Guardrails |
| **Adaptive Governance** | Dynamic policy adjustment based on real-time monitoring | Continuous compliance framework |

### Data Contract Standard
Data Contracts adalah perjanjian formal antara data producer dan consumer yang mendefinisikan schema, SLA, quality rules, dan ownership. IDEAS mengadopsi **Open Data Contract Standard (ODCS)** sebagai baseline:

-   **Schema Definition:** Field names, types, constraints, semantic tags
-   **Quality SLA:** Freshness, completeness, accuracy thresholds
-   **Ownership:** Domain owner, steward, technical contact
-   **Lineage:** Source systems, transformation logic, dependencies

**Kapan Digunakan:** Saat klien memiliki arsitektur data yang kompleks dan membutuhkan keseimbangan antara kontrol terpusat dan inovasi terdesentralisasi. Sangat relevan untuk BUMN dan enterprise besar (Layanan S2.1, S2.2). GenAI layer relevan untuk klien yang sudah memiliki fondasi data matang (Level 3+ DAMA maturity).

**Referensi Silang:** Untuk konsep mendalam, lihat `dama-research/concepts/data-mesh.md` dan `dama-research/concepts/data-fabric.md`. Untuk panduan industri, lihat `dama-research/guides/industry/government-public-sector-guide.md`.

---
## 6. Data Product & Supply Chain

> **Data as a Product** — Memperlakukan data sebagai produk digital dengan ownership, siklus hidup, dan ROI yang jelas.

### Definisi Data Product
Data product adalah unit data yang otonom, read-optimized, dan terstandarisasi yang berisi minimal satu Domain Dataset, diciptakan untuk memenuhi kebutuhan pengguna. Karakteristiknya mencakup *discoverable, addressable, trustworthy, self-describing, interoperable,* dan *secure*.

### Contoh Data Products
Database table/view, raw unstructured files (dengan metadata), data stream dari sistem transaksi, change data capture (CDC) stream, CSV/Excel files, Parquet files, REST API, MDM database, ML features, visualizations/dashboards.

### Data Product Supply Chain (Dylan Anderson)
Empat fase yang menggambarkan alur dari kebutuhan bisnis hingga konsumsi data:
1.  **Discovery & Design:** Business Stakeholder Request → Business Case → Business/Data Strategy → Solutions Architecture → Enterprise Data Models
2.  **Underpinning Data Assets Layer:** Source Data (
'Bronze
') → Accessible Raw Data → Reusable Data Assets → Cleansed & Conformed Data (
'Silver
') → Data Quality Standards/Data Contracts
3.  **Curated Data Feeding into Data Product:** Data Marts → Curated Datasets (
'Gold
') → Business Logic → Consumer-Facing Data Products (KPI Dashboard, Customer Model, Sales Forecast)
4.  **Customer Support:** Training & Support, Continuous Improvement

### Data Product Ways of Working (Dylan Anderson)
Lima fase: Discovery → Design → Development → Testing & Validation → Productionisation & Deployment, dengan Continuous Improvement loop. Pendekatan ini menekankan pola pikir produk-bukan-proyek.

**Kapan Digunakan:** Saat klien ingin mengoperasionalisasikan data mereka menjadi produk yang bernilai bisnis. Relevan untuk enterprise yang sudah memiliki data platform dan ingin menerapkan prinsip Data Mesh (Layanan S2.4, S2.6).

**Referensi Silang:** Konsep ini adalah inti dari prinsip [Data Mesh](#5-data-fabric-vs-data-mesh-hybrid). Untuk template praktis, lihat `dama-research/templates/deliverables/KA-03/data-product-canvas.md`.

---
## 7. Data Management Office (DMO)

> **Centralized Organizational Unit** — Hub strategis dan operasional untuk seluruh inisiatif data, memastikan alignment dan standardisasi.

### Definisi
Data Management Office (DMO) adalah unit organisasi terpusat yang bertanggung jawab mengawasi dan mengimplementasikan praktik manajemen data di seluruh enterprise. Berfungsi sebagai hub strategis (menyelaraskan dengan bisnis) dan operasional (menyediakan layanan data).

### Manfaat DMO
Improved Data Quality, Enhanced Data Access and Use, Reduced Data Risks, Improved Compliance, Better Data Governance, Increased Data Value (ROI).

### Struktur Organisasi DMO (dari paparan KAI)

**Level 1 — Strategic:**
-   Business Owners → Data Owners

**Level 2 — Tactical:**
-   Data Product Squads (Domain A-E) → Data Managers
-   DATA MANAGEMENT OFFICE: Head of Data → Data Management Council

**Level 3 — Operational (3 Domain Roles):**

| Domain | Roles |
| :--- | :--- |
| Data Governance | Data Quality Steward, Data Steward, Data Custodian, Data Security |
| Data Engineering | DataOps Specialist, Data Pipeline Specialist, Data Process Specialist |
| Data Analytics | Data Analyst, Data Product Analyst, Data Scientist, Business Analyst, BI Analyst, Data Storytelling Specialist |

**Data Management Knowledge Areas (DMO scope):** Data Lake, Data Mart, Data Warehouse, MDM, Data Integration, Data Quality, Metadata, Data Modelling, Data Architecture, Data Security, Data Governance.

**Kapan Digunakan:** Saat klien membutuhkan pembentukan atau optimasi fungsi data management terpusat. Sangat relevan untuk layanan S3.1 (DGO as a Service) dan menjadi komponen kunci dalam implementasi Data Governance.

**Referensi Silang:** Struktur peran ini harus selaras dengan daftar peran dalam `references/human-resources-and-pricing.md`.

---
## 8. Enterprise Data Architecture Evolution

> **Gartner 2023** — Evolusi arsitektur data dari EDW ke Active Metadata, menunjukkan pergeseran menuju analisis yang lebih cerdas dan terotomatisasi [5].

| Era | Periode | Karakteristik | Komponen Kunci |
| :--- | :--- | :--- | :--- |
| **Post-EDW** | 2000s | Fragmented Analysis | Data warehouse, data marts, custom ETL, BI tools. |
| **LDW (Logical Data Warehouse)** | 2010s | Unified Analysis | Common semantic layer, DW/marts/lakes, ODS, data virtualization. |
| **Active Metadata** | 2020s | Augmented Analysis | Recommendation engines, adaptive practices, metadata analysis, data/AI orchestration. |

**EDA Layers (dalam Enterprise Architecture):**
-   Business Architecture → Application Architecture → **Data Architecture** → Infrastructure Architecture → Security Architecture
-   Tiga level: Conceptual (Entity/KPI Matrix) → Logical (Entity/Business Function Matrix) → Physical (Entity/Role Matrix CRUD)

**Kapan Digunakan:** Saat mempresentasikan roadmap modernisasi arsitektur data kepada CTO/CIO. Framework ini membantu membenarkan investasi dalam teknologi metadata aktif dan platform data modern (Layanan S2.1, S2.2).

**Referensi Silang:** Konsep Active Metadata adalah pendorong utama [Data Fabric](#5-data-fabric-vs-data-mesh-hybrid).

---
## 9. HBR Digital Transformation Components

> **What the Companies on the Right Side of the Digital Divide Have in Common** — Harvard Business Review (2020) [6]

Framework ini digunakan dalam paparan Ekosistem Data Jabar untuk menjelaskan posisi data ecosystem dalam konteks transformasi digital yang lebih luas. HBR mengidentifikasi 3 fase transformasi digital, yang oleh IDEAS diperkaya dengan kapabilitas spesifik yang diperlukan di setiap fase untuk mencapai kematangan.

| Fase | Fokus | Contoh di Jabar | Kapabilitas Kunci yang Dibangun IDEAS |
| :--- | :--- | :--- | :--- |
| **Digitization** | Konversi proses manual ke digital | Jabar Form (menggantikan formulir kertas) | **Data Capture & Integration:** Membangun pipeline data dari sumber analog/digital yang terfragmentasi. **Data Storage:** Menyediakan repositori data yang andal dan terstruktur (Data Lake/Warehouse). |
| **Analytics** | Pemanfaatan data untuk insight | Dashboard Jabar, Policy Analytics | **Data Quality & Governance:** Memastikan data akurat, konsisten, dan terkelola. **BI & Visualization:** Mengubah data mentah menjadi insight yang mudah dipahami oleh pemangku kepentingan. |
| **Digital Operations** | Operasi bisnis berbasis digital end-to-end | Core Data Jabar, DataOps, API Management | **Data as a Product:** Mengemas data sebagai produk yang dapat dikonsumsi (API, dataset terkurasi). **Automation & AI/ML:** Mengotomatisasi proses dan menciptakan nilai prediktif/preskriptif dari data. **Data-Driven Culture:** Menanamkan pengambilan keputusan berbasis data di seluruh organisasi. |

**Kapan Digunakan:** Saat memposisikan solusi data ecosystem dalam konteks transformasi digital klien yang lebih luas, terutama untuk pemerintah daerah. Membantu menjelaskan bahwa data adalah fondasi untuk operasi digital yang matang.

---
## 10. Open Data Watch Data Value Chain

> **The Data Value Chain: A Framework for Measuring Data Use** — Open Data Watch [7]

Framework ini memetakan perjalanan data dari pengumpulan hingga penciptaan dampak. IDEAS memperkaya model ini dengan menambahkan lapisan **Governance & Quality** yang melandasi seluruh rantai nilai, memastikan bahwa setiap langkah—mulai dari pengumpulan hingga pemanfaatan—dikelola dengan standar yang tinggi untuk menghasilkan dampak yang tepercaya.

**Alur Data Value Chain (dengan Lapisan Tata Kelola):**

| Fase Rantai Nilai | Langkah Spesifik (Open Data Watch) | Aktivitas Tata Kelola & Kualitas (IDEAS) |
| :--- | :--- | :--- |
| **Production** | Collection, Processing, Curation | **Data Quality Profiling:** Validasi data di titik masuk. **Metadata Management:** Dokumentasi sumber dan definisi data. **Data Security:** Klasifikasi dan proteksi data sensitif. |
| **Publication** | Publication, Distribution | **Access Control:** Menetapkan hak akses pengguna. **Data Cataloging:** Memastikan data dapat ditemukan (discoverable). **Versioning:** Mengelola versi dataset. |
| **Uptake** | Discovery, Access, Analysis | **Data Lineage:** Melacak alur transformasi data. **Query Auditing:** Memonitor penggunaan data. **Usage Analytics:** Menganalisis pola akses untuk optimasi. |
| **Impact** | Visualization, Communication, Decision, Action | **Impact Measurement:** Mengukur ROI dan hasil kebijakan. **Feedback Loop:** Mengumpulkan masukan dari pengguna untuk perbaikan. **Ethical Review:** Memastikan penggunaan data yang adil dan bertanggung jawab. |

**Penerapan di Jabar:**
-   **Production:** 46 OPD mengumpulkan data → Satu Data Jabar memproses dan mengkurasi → Open Data Jabar mempublikasikan
-   **Uptake & Impact:** Dashboard Jabar untuk discovery → API untuk access → Policy Analytics untuk analysis → DataViz Festival untuk visualization → Executive Dashboard untuk decision

**Kapan Digunakan:** Saat menjelaskan value proposition open data kepada klien pemerintah, terutama yang belum memahami manfaat transparansi data (Layanan S1.3). Framework ini secara visual menunjukkan bagaimana investasi dalam tata kelola data menghasilkan dampak nyata.

---
## 11. Policy Analytics Ladder

> **Policy Lab / ResearchGate** — 6 level analytics untuk perumusan kebijakan, diperkaya dengan contoh output dan teknologi.

Framework ini digunakan untuk menjelaskan tingkat kematangan analytics dalam konteks pengambilan keputusan kebijakan publik. Setiap jenjang membutuhkan kapabilitas teknis dan analitis yang semakin canggih untuk menghasilkan nilai yang lebih tinggi.

| Level | Konsep | Pertanyaan | Contoh di Jabar | Contoh Output & Teknologi |
| :--- | :--- | :--- | :--- | :--- |
| **Descriptive** | Hindsight | Apa yang terjadi? | Dashboard kasus Covid-19 harian | **Output:** Laporan statis, dashboard KPI. **Teknologi:** SQL, BI Tools (Tableau, Power BI), Excel. |
| **Investigative** | Oversight | Dimana masalahnya? | Quadrant analysis vaksinasi per Kab/Kota | **Output:** Analisis drill-down, segmentasi. **Teknologi:** OLAP cubes, interactive dashboards. |
| **Diagnostic** | Insight | Mengapa terjadi? | Analisis korelasi mobilitas vs kasus | **Output:** Root Cause Analysis (RCA), A/B testing report. **Teknologi:** Python/R (statsmodels), Statistical analysis. |
| **Predictive** | Foresight | Apa yang akan terjadi? | Forecasting kebutuhan isoman (ARIMA) | **Output:** Model prediksi, skor probabilitas. **Teknologi:** Machine Learning (Scikit-learn, TensorFlow), Time Series Forecasting. |
| **Prescriptive** | Outsight | Apa yang harus dilakukan? | Rekomendasi kebijakan PPKM | **Output:** Skenario "what-if", rekomendasi aksi. **Teknologi:** Optimization solvers (Gurobi, CPLEX), Simulation models. |
| **Optimization** | Adaptive | Bagaimana mengoptimalkan secara dinamis? | Optimasi distribusi vaksin secara real-time | **Output:** Sistem rekomendasi adaptif, alokasi sumber daya otomatis. **Teknologi:** Reinforcement Learning, Multi-agent Systems, Digital Twins. |

**Kapan Digunakan:** Saat mempresentasikan kapabilitas analytics kepada pemerintah (Layanan S2.5), terutama untuk menunjukkan bahwa data bukan hanya untuk reporting tetapi juga untuk prediksi dan optimasi kebijakan. Ini membantu membangun visi jangka panjang untuk investasi data.

---
## 12. Data Analytics Activity Flow

> **5-step pyramid** — Alur aktivitas analytics dari business understanding hingga storytelling, mengadaptasi metodologi CRISP-DM.

Framework ini menstrukturkan proses analytics menjadi 5 langkah, memastikan bahwa setiap proyek analitik didasarkan pada pemahaman bisnis yang kuat dan diakhiri dengan insight yang dapat ditindaklanjuti.

1.  **Business Understanding** — objectives, problem question, success criteria
2.  **Data Understanding** — structure, metadata, quality, ownership
3.  **Analytical Approach & Methodology** — EDA, methodology selection
4.  **Model Development & Evaluation** — prescriptive analytics, optimization
5.  **Performing Insight & Storytelling** — key findings, conclusion, recommendation

Dua pendekatan komplementer:
-   **Top Down:** Problem question → data → jawaban (hypothesis-driven)
-   **Bottom Up:** Data tersedia → gali informasi → insight (data-driven discovery)

**Kapan Digunakan:** Saat menyusun proposal analytics atau data science engagement (Layanan S2.3, S2.5), untuk menunjukkan metodologi yang terstruktur dan profesional kepada klien.

---
## 13. Executive Dashboard User Level

> **3-Tier Pyramid** — Desain dashboard berdasarkan level pengguna untuk memastikan relevansi dan kegunaan informasi.

Framework ini memastikan dashboard dirancang sesuai kebutuhan setiap level organisasi, dari strategis hingga operasional.

| Level | Pengguna | Fokus | Frekuensi | Contoh Metrik |
| :--- | :--- | :--- | :--- | :--- |
| **Strategic** | Gubernur, Wakil Gubernur, Sekda | Policy, Helicopter View | Annual/Quarterly | Indeks SPBE, Pertumbuhan Ekonomi, Tingkat Kemiskinan. |
| **Tactical** | Kepala Dinas/Badan/Biro | Procedure, Semi-Operational | Monthly | Realisasi Anggaran per Program, Tingkat Vaksinasi, On-time Performance. |
| **Operational** | Kepala Bidang/UPT, Pejabat Fungsional | Execution, Operational View | Daily/Weekly | Jumlah Tiket Terbuka, Waktu Respons, Ketersediaan Layanan. |

**Kapan Digunakan:** Saat merancang dashboard untuk klien pemerintah atau enterprise (Layanan S2.4), untuk memastikan setiap level mendapatkan informasi yang relevan dan dapat ditindaklanjuti, menghindari kelebihan informasi.

---
## 14. Framework Selection Guide

Panduan ini membantu memilih framework yang paling relevan berdasarkan konteks dan kebutuhan klien.

| Konteks Klien | Framework Utama | Framework Pendukung |
| :--- | :--- | :--- |
| C-Level buy-in untuk investasi data | MIT CISR | North Star Metric, Business Strategy Temple, Data Valuation & Infonomics |
| Pembentukan governance dari nol | DAMA-DMBOK + Five-Component DG Strategy | DMO Structure, DG Balanced Scorecard, Change Management (ADKAR/Kotter) |
| Modernisasi arsitektur data | EDA Evolution + Data Fabric/Mesh Hybrid | Nine-Category Technology Landscape, Data Contracts |
| Operasionalisasi data sebagai produk | Data Product Canvas + Supply Chain + Pyramid | Data Product Operational Delivery Model, Data Mesh |
| Alignment data strategy dengan bisnis | North Star Metric + Value Proposition | MIT CISR Principle 1, Business Strategy Temple |
| Knowledge transfer / capacity building | Semua framework di atas | DAMA Pyramid sebagai overview, PMBOK Principles |
| Transformasi digital pemerintah daerah | HBR Digital Transformation | Open Data Watch Value Chain, Policy Analytics Ladder |
| Analytics untuk kebijakan publik | Policy Analytics Ladder + Four Levels of Analytics | Data Analytics Activity Flow |
| Desain dashboard multi-level | Executive Dashboard User Level + Five A's | KPI Tree, Strategic Dashboarding |
| Data quality improvement | Eight Dimensions DQ + DQ Platform Approach | Data Observability, Data Contracts, 1-10-100 Rule |
| AI/ML readiness & governance | AI Governance Framework (5 pillars) | Data Ethics Frameworks, NIST AI RMF, ISO 42001 |
| UU PDP compliance readiness | DAMA-DMBOK KA-05 (Data Security) | ISO 27001:2022, Data Ethics Frameworks |
| Open data portal quality | ODPQ Framework | Open Data Watch Value Chain, CKAN/DKAN |
| Organisasi & struktur tim data | Five Organizational Models | DMO Structure, Tuckman's Team Development |
| Project & delivery management | PMBOK 7th Edition Principles | PMBOK 6th Edition Processes, Agile Work Hierarchy |

---
## 15. Modern Data Architecture Patterns for Indonesian Context

Pola arsitektur data modern perlu diadaptasi untuk konteks Indonesia, khususnya untuk sektor pemerintahan dan BUMN yang memiliki karakteristik unik terkait regulasi, silo organisasi, dan kematangan digital.

### Data Mesh untuk Pemerintahan Indonesia

| Prinsip Data Mesh | Adaptasi Indonesia | Contoh Implementasi |
| :--- | :--- | :--- |
| **Domain Ownership** | OPD (Organisasi Perangkat Daerah) sebagai domain owner. | Setiap OPD mengelola data domain masing-masing (kesehatan, pendidikan, kependudukan) sesuai dengan tusi-nya. |
| **Data as a Product** | Data sebagai layanan publik yang terstandarisasi. | Portal data terbuka per domain dengan SLA, metadata lengkap (sesuai standar SDI), dan kualitas terukur. |
| **Self-serve Platform** | Platform data terpusat yang disediakan oleh Diskominfo/Walidata. | Ekosistem Data Jabar sebagai contoh self-serve platform yang menyediakan tools dan infrastruktur. |
| **Federated Governance** | Walidata sebagai federasi yang menetapkan standar interoperabilitas. | Struktur Walidata Provinsi → Walidata Kabupaten/Kota sesuai amanat Perpres Satu Data Indonesia (SDI). |

### Data Fabric untuk Enterprise Indonesia

Data Fabric cocok untuk organisasi dengan arsitektur data yang sudah kompleks (BUMN, perbankan) yang membutuhkan integrasi tanpa reorganisasi domain secara masif.

-   **Knowledge Graph:** Metadata-driven discovery dan lineage otomatis untuk memetakan aset data yang tersebar.
-   **Active Metadata:** Real-time data governance dan quality monitoring untuk memastikan kepatuhan terhadap regulasi (OJK, BI).
-   **AI-Augmented Integration:** Automated data pipeline recommendation untuk mempercepat integrasi sistem legacy dan modern.

**Referensi Silang:** Untuk implementasi Data Fabric, lihat `dama-research/concepts/data-fabric.md`. Untuk integrasi dengan enterprise architecture, lihat `dama-research/guides/industry/financial-services-guide.md`.

---
## 16. Change Management untuk Tata Kelola Data

Implementasi data governance di lingkungan birokrasi memerlukan pendekatan change management yang disesuaikan untuk mengatasi resistensi dan membangun budaya data.

### Framework ADKAR untuk Konteks Pemerintahan

| Tahap ADKAR | Adaptasi Birokrasi | Taktik |
| :--- | :--- | :--- |
| **Awareness** | Sosialisasi pentingnya data untuk pencapaian target kinerja (IKU). | Roadshow, seminar, mengaitkan dengan target SPBE dan reformasi birokrasi. |
| **Desire** | Menciptakan insentif (reward & recognition) bagi OPD yang proaktif. | Kompetisi inovasi berbasis data, penghargaan walidata terbaik. |
| **Knowledge** | Pelatihan bertahap per level jabatan dan peran (struktural, fungsional). | Data literacy program (awareness → practitioner → expert), sertifikasi. |
| **Ability** | Pendampingan hands-on dan penyediaan tools yang mudah digunakan. | DGO as a Service (S3.1), embedded consultants, platform data self-service. |
| **Reinforcement** | Monitoring dan evaluasi berkala yang terintegrasi dengan penilaian kinerja. | Dashboard KPI adopsi, integrasi ke dalam penilaian SPBE tahunan. |

### Kotter’s 8-Step untuk Transformasi Data Pemerintah

1.  **Create Urgency:** Leverage UU PDP enforcement (berlaku penuh sejak Okt 2024) dan target SPBE nasional.
2.  **Form Coalition:** Libatkan Walidata, Sekda, Bappeda, dan Kepala OPD kunci.
3.  **Create Vision:** Visi ekosistem data terintegrasi untuk pelayanan publik yang lebih baik (contoh: Jabar).
4.  **Communicate Vision:** Roadshow ke seluruh OPD, forum data, media internal.
5.  **Empower Action:** Bentuk tim data steward per OPD, berikan kewenangan dan pelatihan.
6.  **Create Quick Wins:** Pilot portal data atau dashboard di 2-3 OPD prioritas untuk menunjukkan nilai.
7.  **Build on Change:** Ekspansi ke seluruh OPD secara bertahap berdasarkan keberhasilan pilot.
8.  **Anchor Change:** Institusionalisasi melalui Peraturan Gubernur/Bupati dan integrasi ke dalam proses bisnis.

**Referensi Silang:** Untuk template change management, lihat `dama-research/guides/implementation/risk-management.md`. Untuk framework kolaborasi, lihat `dama-research/guides/implementation/collaboration-framework.md`.

---
## 17. PMBOK Project Management Frameworks

> **PMI Project Management Body of Knowledge** — ANSI/PMI 99-001-2017 (6th Edition) & ANSI/PMI 99-001-2021 (7th Edition) [8]

IDEAS mengintegrasikan best practices dari PMBOK sebagai **pilar keempat metodologi** untuk memperkuat delivery, terutama dalam proyek-proyek berskala besar yang memerlukan governance ketat. PMBOK melengkapi tiga pilar lainnya (DAMA-DMBOK, Agile, CRISP-DM) dengan kerangka kerja pengelolaan proyek yang terstruktur, membentuk **4 Pilar Metodologi IDEAS** yang komprehensif.

### 17.1 PMBOK 6th Edition: Process-Based Framework (2017)
PMBOK 6th Edition mendefinisikan project management melalui **49 proses** dalam **5 Process Groups** dan **10 Knowledge Areas**. Framework ini sangat relevan untuk proyek pemerintah Indonesia yang memerlukan dokumentasi formal dan milestone-based delivery.

**5 Process Groups:**

| Process Group | Fokus | Relevansi IDEAS |
| :--- | :--- | :--- |
| **Initiating** | Project Charter, Stakeholder Identification | Kick-off meeting, stakeholder mapping di awal engagement. |
| **Planning** | Scope, Schedule, Cost, Quality, Risk, Communications | Penyusunan proposal, RAB/HPS, timeline, risk register. |
| **Executing** | Direct & Manage Work, Quality Assurance, Team Development | Sprint execution, deliverable production, capacity building. |
| **Monitoring & Controlling** | Performance Reporting, Change Control, Risk Monitoring | EVM tracking, status reporting, scope change management. |
| **Closing** | Formal Acceptance, Lessons Learned, Knowledge Transfer | BAST, knowledge transfer, handover documentation. |

**10 Knowledge Areas (dengan update regulasi):**

| Knowledge Area | Proses Kunci | Mapping ke IDEAS & Regulasi Terkait |
| :--- | :--- | :--- |
| **Integration Management** | Project Charter, Change Control, Lessons Learned | Proposal → Kontrak → BAST lifecycle. |
| **Scope Management** | WBS, Scope Verification, Scope Control | `task-decomposition.md` (15 services, 46 Features, 563 Subtasks). |
| **Schedule Management** | Activity Sequencing, Critical Path, Schedule Control | `generate_timeline.py`, Gantt chart, sprint planning. |
| **Cost Management** | Cost Estimation, Budgeting, EVM | `cogs-methodology.md`, `pricing_engine.py`, RAB/HPS (mengacu **PMK 32/2025**). |
| **Quality Management** | Quality Planning, QA, QC | Internal review, UAT, acceptance criteria per deliverable. |
| **Resource Management** | Team Planning, RACI/RASCI, Team Development | `rate_card.py`, 46 roles, squad-based allocation. |
| **Communications Management** | Stakeholder Reporting, Status Updates | Status reports, steering committee presentations. |
| **Risk Management** | Risk Identification, Qualitative/Quantitative Analysis, Response Planning | Risk register, contingency budget (5-10% dalam RAB). |
| **Procurement Management** | Procurement Planning, Vendor Selection | Kepatuhan **Perpres 46/2025**, metodologi HPS. |
| **Stakeholder Management** | Stakeholder Analysis, Engagement Planning | Stakeholder mapping, power/interest grid. |

### 17.2 PMBOK 7th Edition: Principles-Based Framework (2021)
PMBOK 7th Edition merepresentasikan pergeseran paradigma dari pendekatan berbasis proses ke pendekatan berbasis prinsip. Framework ini lebih adaptif dan selaras dengan pendekatan hybrid yang diterapkan IDEAS.

**12 Prinsip Project Management:**

| # | Prinsip | Deskripsi | Alignment dengan IDEAS Core Values |
| :--- | :--- | :--- | :--- |
| 1 | **Stewardship** | Bertindak dengan integritas, kepedulian, dan kepatuhan. | INTEGRITAS (Core Value #1) |
| 2 | **Team** | Membangun lingkungan tim yang kolaboratif. | KOLABORASI (Core Value #2) |
| 3 | **Stakeholders** | Melibatkan stakeholder secara proaktif. | KOLABORASI (Core Value #2) |
| 4 | **Value** | Fokus pada penyampaian nilai, bukan hanya deliverable. | INOVASI (Core Value #3) |
| 5 | **Systems Thinking** | Memahami proyek sebagai bagian dari sistem yang lebih besar. | KONTEKSTUAL (Keunggulan Kompetitif) |
| 6 | **Leadership** | Kepemimpinan adaptif, bukan hanya otoritas. | KEUNGGULAN (Core Value #4) |
| 7 | **Tailoring** | Menyesuaikan pendekatan berdasarkan konteks. | Hybrid Waterfall-Agile untuk pemerintah. |
| 8 | **Quality** | Membangun kualitas ke dalam proses dan deliverable. | KEUNGGULAN (Core Value #4) |
| 9 | **Complexity** | Menavigasi kompleksitas (VUCA) secara berkelanjutan. | KONTEKSTUAL (Keunggulan Kompetitif) |
| 10 | **Risk** | Mengoptimalkan respons terhadap ancaman dan peluang. | Risk Management dalam RAB/proposal. |
| 11 | **Adaptability** | Membangun ketahanan dan kemampuan adaptasi. | INOVASI (Core Value #3) |
| 12 | **Change** | Memungkinkan perubahan untuk mencapai visi. | PEMBERDAYAAN (Core Value #6) |

### 17.3 Tailoring Framework (PMBOK 7th Edition Chapter 3)
Tailoring adalah proses menyesuaikan pendekatan manajemen proyek. Proses ini meliputi empat langkah: **Select Initial Development Approach** (predictive, adaptive, hybrid), **Tailor for the Organization** (menyesuaikan dengan budaya dan governance klien, misal kepatuhan Perpres 46/2025), **Tailor for the Project** (menyesuaikan dengan kompleksitas dan skala proyek), dan **Implement Ongoing Improvement** (retrospective dan continuous improvement).

### 17.4 Models, Methods, and Artifacts (PMBOK 7th Edition Chapter 4)
PMBOK 7th Edition memperkenalkan berbagai model yang memperkaya toolkit IDEAS, termasuk:
-   **Models untuk Complexity & Decision-Making:** Cynefin Framework, Stacey Matrix, VUCA Analysis.
-   **Models untuk Change Management:** ADKAR, Bridges' Transition Model, Kotter's 8-Step (sudah terintegrasi di [Section 16](#16-change-management-untuk-tata-kelola-data)).
-   **Models untuk Team & Leadership:** Tuckman's Team Development, Situational Leadership II, Salience Model.
-   **Estimation Methods:** Analogous, Parametric, Bottom-Up, Three-Point (PERT), Story Points, T-Shirt Sizing.

**Referensi Silang:** Metodologi Agile IDEAS dijelaskan lebih detail di `references/agile-work-hierarchy.md`.

---

## 18. Data Valuation & Infonomics Framework

> **Infonomics: How to Monetize, Manage, and Measure Information as an Asset for Competitive Advantage** — Douglas B. Laney [9]

Infonomics adalah teori ekonomi dan praktik memperlakukan informasi sebagai aset nyata. IDEAS mengadopsi prinsip Infonomics untuk membantu klien mengukur dan merealisasikan nilai dari aset data mereka. Kami mengintegrasikan ini dengan kerangka kerja valuasi praktis dari Deloitte.

### Prinsip Dasar Infonomics
-   **Monetize:** Mengidentifikasi cara-cara untuk menghasilkan nilai ekonomi dari data, baik secara langsung (menjual data) maupun tidak langsung (meningkatkan efisiensi, menciptakan produk baru).
-   **Manage:** Menerapkan disiplin manajemen aset (seperti pada aset fisik atau finansial) ke data, termasuk tata kelola, kualitas, dan keamanan.
-   **Measure:** Mengukur nilai ekonomi data, baik potensial maupun yang sudah terealisasi, serta kontribusinya terhadap tujuan bisnis.

### Kerangka Valuasi Data Deloitte (2025)
Deloitte menyediakan tiga pendekatan utama untuk menilai aset data, yang diadopsi oleh IDEAS dalam layanan S1.5 (Data Strategy & Value Proposition Design) [10].

| Pendekatan | Metode | Deskripsi Singkat & Contoh Penggunaan |
| :--- | :--- | :--- |
| **Income Approach** | Multi-Period Excess Earnings (MPEE) | Mengisolasi arus kas masa depan yang diatribusikan secara spesifik ke aset data. (Contoh: Valuasi data pelanggan untuk akuisisi perusahaan). |
| | Relief-from-Royalty | Mengestimasi biaya yang akan dikeluarkan jika harus membayar lisensi untuk menggunakan data serupa dari pihak ketiga. (Contoh: Menilai data geospasial internal). |
| | With-and-Without Method | Membandingkan proyeksi arus kas perusahaan dengan dan tanpa aset data tertentu. (Contoh: Mengukur nilai data histori transaksi untuk model prediksi fraud). |
| **Cost Approach** | Cost to Reproduce | Mengestimasi biaya untuk membuat replika identik dari aset data yang ada. (Contoh: Menilai dataset riset yang dikumpulkan secara manual). |
| | Cost to Replace | Mengestimasi biaya untuk membuat aset data baru dengan kegunaan yang setara, menggunakan teknologi saat ini. (Contoh: Menilai data warehouse lama yang akan dimigrasi). |
| **Market Approach** | Comparable Transactions | Menganalisis harga transaksi jual-beli aset data yang sebanding di pasar. (Contoh: Menentukan harga jual untuk dataset anonim). |

### Konsep "Data Debt"
Diperkenalkan oleh Deloitte, **Data Debt** adalah kewajiban tersembunyi yang terkait dengan aset data, meliputi:
-   **Biaya Lifecycle:** Biaya penyimpanan, pemeliharaan, dan pengarsipan data.
-   **Masalah Kualitas:** Biaya untuk memperbaiki data yang tidak akurat atau tidak lengkap.
-   **Risiko Kepatuhan:** Potensi denda atau kerugian reputasi akibat pelanggaran privasi (UU PDP).
-   **Data Decay:** Penurunan nilai data seiring waktu.

**Rasio Utang Data (Data Debt Ratio):** `Nilai Data / Utang Data`. Rasio yang sehat menunjukkan bahwa nilai yang dihasilkan dari data jauh melampaui biaya pengelolaannya.

**Kapan Digunakan:** Saat berdiskusi dengan CFO atau CEO untuk membenarkan investasi dalam data governance dan data management. Membantu mengubah percakapan dari "data sebagai biaya" menjadi "data sebagai aset yang menghasilkan nilai".

---

## 19. End-to-End Business Strategy Frameworks

Kerangka kerja ini membantu IDEAS dalam memahami dan menyelaraskan solusi data dengan strategi bisnis klien secara keseluruhan, dari konsepsi hingga eksekusi. Detail lebih lanjut untuk setiap framework tersedia di `references/business-frameworks.md`.

| Kategori | Framework | Kegunaan Utama |
| :--- | :--- | :--- |
| **Business Model Design** | Business Model Canvas (BMC) | Memvisualisasikan dan merancang model bisnis klien. |
| | Value Proposition Canvas (VPC) | Memastikan produk dan layanan data sesuai dengan kebutuhan pelanggan. |
| **Strategic Analysis** | SWOT & PESTEL Analysis | Menganalisis kekuatan, kelemahan, peluang, dan ancaman internal & eksternal. |
| | Porter's Five Forces | Menganalisis lanskap kompetitif industri klien. |
| **Execution & Goal Setting** | Balanced Scorecard (BSC) | Menerjemahkan visi dan strategi menjadi tujuan operasional yang terukur. |
| | Objectives and Key Results (OKR) | Menetapkan tujuan yang ambisius dan melacak kemajuan secara transparan. |
| **Sales & Proposal** | SPIN Selling & Shipley Process | Metodologi untuk penjualan konsultatif dan pengembangan proposal yang menang. |
| **Business Analysis** | BABOK (Business Analysis Body of Knowledge) | Kerangka kerja standar untuk praktik analisis bisnis. |

**Kapan Digunakan:** Digunakan secara internal oleh tim Business Development dan Solution Architects pada fase awal engagement untuk memahami konteks klien secara mendalam dan merancang solusi yang paling berdampak.

---

## 20. Data Ethics Frameworks

Selain AI Governance, IDEAS juga menerapkan kerangka kerja etika data yang lebih luas untuk memastikan penggunaan data yang bertanggung jawab di semua proyek, tidak hanya yang melibatkan AI.

### The FATE Framework (Fairness, Accountability, Transparency, Ethics)
Prinsip FATE adalah fondasi dari pendekatan etika IDEAS:
-   **Fairness:** Memastikan bahwa model data dan analitik tidak menciptakan atau memperkuat bias yang tidak adil terhadap kelompok tertentu.
-   **Accountability:** Menetapkan garis tanggung jawab yang jelas untuk hasil dari sistem data, termasuk siapa yang bertanggung jawab jika terjadi kesalahan.
-   **Transparency:** Memastikan bahwa cara kerja sistem data dapat dijelaskan kepada pengguna dan pemangku kepentingan dalam bahasa yang dapat dimengerti.
-   **Ethics:** Secara proaktif mempertimbangkan dampak sosial dan etis dari pengumpulan, penggunaan, dan pembagian data.

### Deon: A Command-Line Tool for Data Ethics Checklists
IDEAS menggunakan `deon`, sebuah tool open-source, untuk menanamkan checklist etika langsung ke dalam siklus pengembangan proyek data. Checklist ini mencakup pertanyaan-pertanyaan kritis di berbagai tahap:

| Tahap Proyek | Contoh Pertanyaan Checklist Etika (Deon) |
| :--- | :--- |
| **Pengumpulan Data** | Apakah kami mengumpulkan data yang tidak diperlukan? Apakah ada potensi bias dalam metode pengumpulan? |
| **Eksplorasi Data** | Apakah ada korelasi yang dapat menyebabkan diskriminasi? Apakah ada kelompok yang kurang terwakili? |
| **Pemodelan** | Apakah metrik evaluasi model dapat menyembunyikan bias? Bagaimana model akan diinterpretasikan oleh pengguna? |
| **Deployment** | Apakah ada mekanisme untuk pengguna melaporkan masalah? Bagaimana kita akan memonitor dampak yang tidak diinginkan? |

**Kapan Digunakan:** Prinsip FATE diterapkan di semua engagement. Checklist Deon diintegrasikan ke dalam proyek pengembangan analitik dan AI (Layanan S2.3, S2.5, S2.6) sebagai praktik standar.

---

## 21. Glossary of Terms

-   **ADKAR:** *Awareness, Desire, Knowledge, Ability, Reinforcement* - Model manajemen perubahan.
-   **BAST:** *Berita Acara Serah Terima* - Dokumen serah terima pekerjaan formal.
-   **DAMA-DMBOK:** *Data Management Body of Knowledge* - Kerangka kerja standar global untuk manajemen data.
-   **DMO:** *Data Management Office* - Unit organisasi terpusat untuk manajemen data.
-   **HPS:** *Harga Perkiraan Sendiri* - Estimasi biaya proyek oleh pemilik pekerjaan (pemerintah).
-   **NSM:** *North Star Metric* - Metrik tunggal yang mengukur nilai inti produk bagi pelanggan.
-   **ODCS:** *Open Data Contract Standard* - Standar terbuka untuk kontrak data.
-   **OMTM:** *One Metric That Matters* - Metrik taktis jangka pendek.
-   **OPD:** *Organisasi Perangkat Daerah* - Dinas atau badan di tingkat pemerintah daerah.
-   **Perpres:** *Peraturan Presiden* - Peraturan yang dikeluarkan oleh Presiden RI.
-   **PMBOK:** *Project Management Body of Knowledge* - Kerangka kerja standar global untuk manajemen proyek.
-   **PMK:** *Peraturan Menteri Keuangan* - Peraturan yang dikeluarkan oleh Menteri Keuangan RI.
-   **RAB:** *Rencana Anggaran Biaya* - Rencana anggaran biaya yang diajukan oleh penyedia jasa.
-   **SPBE:** *Sistem Pemerintahan Berbasis Elektronik* - E-government di Indonesia.
-   **UU PDP:** *Undang-Undang Pelindungan Data Pribadi* - UU No. 27 Tahun 2022.

---

## References

[1] Wixom, B. H., & Beath, C. (2015). *Data Is a Strategic Asset, So Why Is It Still So Hard to Get Value from It?* MIT Center for Information Systems Research.
[2] DAMA International. (2017). *DAMA-DMBOK: Data Management Body of Knowledge (2nd ed.)*.
[3] Anderson, D. (2022-2024). *The Data Ecosystem*. Substack. Retrieved from https://thedataecosystem.substack.com/
[4] Croll, A., & Yoskovitz, B. (2013). *Lean Analytics: Use Data to Build a Better Startup Faster*.
[5] Gartner, Inc. (2023). *Hype Cycle for Data Management, 2023*.
[6] Westerman, G., et al. (2020). *What the Companies on the Right Side of the Digital Divide Have in Common*. Harvard Business Review.
[7] Open Data Watch. (2018). *The Data Value Chain: A Framework for Measuring Data Use*.
[8] Project Management Institute. (2017, 2021). *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)* – 6th & 7th Editions.
[9] Laney, D. B. (2017). *Infonomics: How to Monetize, Manage, and Measure Information as an Asset for Competitive Advantage*.
[10] Deloitte. (2025). *Data as an Asset: Valuation in the Age of AI*. Deloitte Insights.
