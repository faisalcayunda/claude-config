> # Agile Work Item Hierarchy for IDEAS Service Delivery
> 
> *Last Updated: February 2026*
> 
> ## Table of Contents
> 
> 1. [Overview](#overview)
> 2. [Hierarchy Levels](#hierarchy-levels)
> 3. [Relationships & Decomposition](#relationships--decomposition)
> 4. [Milestones, Artefacts & Output Deliverables](#milestones-artefacts--output-deliverables)
> 5. [IDEAS Service Mapping](#ideas-service-mapping)
> 6. [Practical Examples per Pillar](#practical-examples-per-pillar)
> 7. [Tools & Tracking](#tools--tracking)
> 8. [Glossary of Terms](#glossary-of-terms)
> 9. [References](#references)
> 
> ---
> 
> ## Overview
> 
> Dokumen ini mendefinisikan hierarki work item yang digunakan IDEAS dalam mengelola proyek data management. Hierarki ini mengadaptasi best practices dari **SAFe 6.0**, Scrum, dan Kanban, disesuaikan dengan konteks layanan konsultansi data di Indonesia — termasuk kebutuhan pengadaan pemerintah yang milestone-based dan delivery enterprise yang sprint-based.
> 
> ### SAFe 6.0 Key Updates (Integrated)
> - **Eight Flow Accelerators:** Visualize & limit WIP, Address bottlenecks, Minimize handoffs, Get faster feedback, Work in smaller batches, Reduce queue length, Optimize time in the zone, Remediate legacy policies.
> - **AI/Big Data/Cloud Guidance:** SAFe 6.0 includes specific guidance for data-intensive projects, which IDEAS integrates into its service delivery patterns.
> - **Quarterly Releases:** Aligned with PI (Program Increment) cadence, mirroring our government project milestone reporting.
> 
> ### Hybrid Waterfall-Agile for Government Projects (PMBOK-Enhanced)
> IDEAS uses a **tri-level hybrid approach** for government engagements, enhanced with PMBOK governance:
> - **PMBOK Governance Level:** Provides project management rigor through 5 Process Groups (Initiating → Closing), formal change control, EVM monitoring, and stakeholder management aligned with PMBOK 6th Edition.
> - **Waterfall Level:** Meets all government requirements (SELC, milestone-based deliverables, and compliance with **Perpres 46/2025** regarding government procurement [1]).
> - **Agile Level:** Enables iterative development within each milestone phase using Scrum/Kanban sprints.
> - **Integration:** Work from the Agile environment is "bubbled up" quarterly into formal deliverables for the client's production environment, with PMBOK governance ensuring scope control, risk management, and value delivery alignment (PMBOK 7th Edition Principle #4).
> 
> Hierarki ini memastikan **traceability** dari tujuan strategis klien hingga task terkecil yang dikerjakan tim, sehingga setiap jam kerja dapat dijustifikasi terhadap nilai bisnis yang dihasilkan.
> 
> ---
> 
> ## Hierarchy Levels
> 
> ### Level 1: Strategic Theme / Initiative
> 
> **Definisi:** Tujuan strategis berskala besar yang menjadi alasan utama engagement. Biasanya berasal dari visi organisasi klien, regulasi, atau transformasi bisnis. Satu initiative dapat mencakup beberapa engagement IDEAS.
> 
> **Durasi:** 1-3 tahun
> **Pemilik:** C-Level klien (CIO, CDO, Sekretaris Daerah)
> **Contoh:**
> - "Mewujudkan Satu Data Jawa Barat sesuai Perpres 39/2019"
> - "Transformasi Data-Driven Decision Making di PT KAI"
> - "Modernisasi Infrastruktur Data POLRI"
> 
> ### Level 2: Epic
> 
> **Definisi:** Badan kerja besar yang memberikan nilai signifikan dan dapat dipecah menjadi beberapa feature. Satu epic biasanya sejajar dengan satu service IDEAS atau satu work package dalam RAB/HPS.
> 
> **Durasi:** 1-6 bulan
> **Pemilik:** Project Manager / Product Owner IDEAS
> **Contoh:**
> - "Implementasi Data Governance Framework" (related to [S1.2](services-catalog.md#s12-data-governance--compliance-framework))
> - "Pembangunan Portal Data Pemerintah" (related to [S2.3](services-catalog.md#s23-government-data-portal))
> - "Pelaksanaan Data Maturity Assessment" (related to [S1.3](services-catalog.md#s13-data-maturity-assessment--roadmap))
> 
> ### Level 3: Feature
> 
> **Definisi:** Kapabilitas atau layanan yang memenuhi kebutuhan stakeholder tertentu. Feature biasanya sejajar dengan satu fase dalam service delivery atau satu sub-work-package dalam RAB.
> 
> **Durasi:** 2-6 minggu (1-3 sprint)
> **Pemilik:** Product Owner / Lead Consultant
> **Contoh:**
> - "Data Quality Framework Design" (fase dalam S1.2)
> - "Dashboard Eksekutif Gubernur" (komponen S2.6)
> - "API Gateway untuk Pertukaran Data OPD" (komponen S2.5)
> 
> ### Level 4: User Story
> 
> **Definisi:** Unit kerja terkecil yang memberikan nilai kepada pengguna akhir. Ditulis dari perspektif pengguna menggunakan format: "Sebagai [peran], saya ingin [tujuan] agar [manfaat]."
> 
> **Durasi:** 1-5 hari (dalam 1 sprint)
> **Pemilik:** Development Team
> **Contoh:**
> - "Sebagai Data Steward, saya ingin mendefinisikan aturan kualitas data untuk dataset kependudukan agar akurasi data terjamin."
> - "Sebagai Kepala OPD, saya ingin melihat dashboard capaian SPM agar dapat mengambil keputusan berbasis data."
> - "Sebagai Admin Portal, saya ingin mengunggah dataset dalam format CSV agar data tersedia untuk publik."
> 
> ### Level 5: Task
> 
> **Definisi:** Aktivitas teknis granular yang diperlukan untuk menyelesaikan user story. Task adalah unit kerja terkecil yang di-assign ke satu orang.
> 
> **Durasi:** 2-8 jam
> **Pemilik:** Individual contributor
> **Contoh:**
> - "Desain skema tabel data_quality_rules di PostgreSQL"
> - "Implementasi endpoint REST API /datasets/{id}/quality-score"
> - "Tulis unit test untuk fungsi validasi format NIK"
> 
> ### Level 6: Subtask
> 
> **Definisi:** Pecahan task yang lebih granular, digunakan ketika task terlalu besar untuk diselesaikan dalam satu sesi kerja atau memerlukan kolaborasi beberapa orang.
> 
> **Durasi:** 30 menit - 4 jam
> **Pemilik:** Individual contributor
> **Contoh:**
> - "Review DDL script oleh Data Architect"
> - "Deploy migration script ke staging environment"
> - "Update API documentation di Swagger"
> 
> ---
> 
> ## Relationships & Decomposition
> 
> ### Hierarki Parent-Child
> 
> ```
> Strategic Theme / Initiative
>   └── Epic (= IDEAS Service / Work Package)
>         └── Feature (= Service Phase / Sub-Work-Package)
>               └── User Story (= User-facing value unit)
>                     └── Task (= Technical work unit)
>                           └── Subtask (= Granular activity)
> ```
> 
> ### Rasio Dekomposisi Tipikal
> 
> | Parent | Child | Rasio Tipikal | Contoh IDEAS |
> | :--- | :--- | :--- | :--- |
> | Initiative → Epic | 1 : 3-8 | 1 engagement = 3-5 services |
> | Epic → Feature | 1 : 3-6 | 1 service = 4-6 fase |
> | Feature → User Story | 1 : 5-15 | 1 fase = 5-10 stories |
> | User Story → Task | 1 : 3-8 | 1 story = 3-5 tasks |
> | Task → Subtask | 1 : 2-4 | 1 task = 2-3 subtasks |
> 
> ### Relasi Lintas Hierarki
> 
> Selain hubungan parent-child, terdapat beberapa relasi lintas hierarki yang penting.
> 
> **Dependency (depends-on):** Feature A tidak dapat dimulai sebelum Feature B selesai. Contoh: "API Gateway" depends on "Data Model Design".
> 
> **Blocks/Blocked-by:** Task tertentu memblokir task lain. Contoh: "Database migration" blocks "API development".
> 
> **Related-to:** Work item yang saling terkait tetapi tidak memiliki dependency langsung. Contoh: "Data Quality Rules" related-to "Data Dictionary".
> 
> **Contributes-to:** Task yang berkontribusi pada milestone tertentu. Contoh: Beberapa user stories dari berbagai features "contributes-to" Milestone "Phase 1 Go-Live".
> 
> ---
> 
> ## Milestones, Artefacts & Output Deliverables
> 
> ### Milestone
> 
> **Definisi:** Titik pencapaian signifikan dalam proyek yang menandai selesainya sekelompok deliverable. Milestone bukan work item — milestone adalah checkpoint yang digunakan untuk mengukur kemajuan dan memicu pembayaran (termin).
> 
> **Karakteristik:**
> - Tidak memiliki durasi (zero-duration event)
> - Terikat pada tanggal target
> - Biasanya sejajar dengan termin pembayaran dalam kontrak
> - Memiliki acceptance criteria yang jelas
> 
> **Milestone Tipikal per Engagement Type:**
> 
> | Engagement Type | Milestone 1 | Milestone 2 | Milestone 3 | Milestone 4 |
> | :--- | :--- | :--- | :--- | :--- |
> | Advisory (S1.x) | Kick-off & Assessment Complete | Framework/Strategy Draft | Final Deliverable & Presentation | Knowledge Transfer |
> | Implementation (S2.x) | Requirements & Design Complete | Development Sprint Complete | UAT & Go-Live | Stabilization & Handover |
> | Managed Service (S3.x) | Onboarding Complete | Quarterly Review | Annual Assessment | Renewal/Transition |
> 
> ### Artefact
> 
> **Definisi:** Dokumen, model, atau aset yang dihasilkan selama proses kerja dan digunakan sebagai input untuk tahap berikutnya atau sebagai bukti penyelesaian. Artefact bersifat **living document** — terus diperbarui sepanjang proyek.
> 
> **Kategori Artefact:**
> 
> | Kategori | Contoh | Dihasilkan Oleh |
> | :--- | :--- | :--- |
> | **Planning** | Product Backlog, Sprint Backlog, Roadmap | Product Owner, PM |
> | **Design** | Data Model, Architecture Blueprint, Wireframe | Data Architect, UX Designer |
> | **Development** | Source Code, ETL Script, Configuration | Data Engineer, Developer |
> | **Testing** | Test Plan, Test Results, Bug Report | QA, Data Quality Analyst |
> | **Governance** | Policy Document, SOP, RACI Matrix | Data Governance Manager |
> | **Communication** | Meeting Minutes, Status Report, Presentation | PM, Business Analyst |
> 
> ### Output Deliverable
> 
> **Definisi:** Produk akhir yang diserahkan kepada klien sebagai bukti penyelesaian pekerjaan. Output deliverable bersifat **final** — sudah melalui review dan approval. Output deliverable adalah subset dari artefact yang secara eksplisit tercantum dalam kontrak atau proposal.
> 
> **Hubungan:** Milestone → memicu penyerahan → Output Deliverable(s) → yang merupakan versi final dari → Artefact(s) → yang dihasilkan melalui → Task(s) dalam User Story.
> 
> ---
> 
> ## IDEAS Service Mapping
> 
> ### Mapping Hierarki ke RAB/HPS
> 
> | Hierarchy Level | RAB/HPS Equivalent | Keterangan |
> | :--- | :--- | :--- |
> | Initiative | Judul Proyek | "Pengembangan SOP dan Standar Data Walidta POLRI" |
> | Epic | Work Package (Paket Pekerjaan) | WP-1: Data Governance Framework |
> | Feature | Sub-Work-Package | SWP-1.1: Assessment & Gap Analysis |
> | User Story | Item Pekerjaan | Pelaksanaan Data Quality Assessment |
> | Task | Rincian Biaya | Man-days × daily rate per role |
> 
> ### Mapping Hierarki ke Task Decomposition
> 
> Setiap task dalam `task-decomposition.md` (misalnya S1.1-01, S1.1-02) berada pada **Level 4-5** dalam hierarki ini. Dokumen [task-decomposition.md](task-decomposition.md) menyediakan granularitas yang diperlukan untuk kalkulasi COGS dan RAB, sementara hierarki ini menyediakan konteks strategis dan traceability ke atas.
> 
> **Contoh Konkret 1: Data Quality Rules**
> 
> Mari kita lihat dekomposisi dari User Story: *"Sebagai Data Steward, saya ingin mendefinisikan aturan kualitas data untuk dataset kependudukan agar akurasi data terjamin."*
> 
> User Story ini dipecah menjadi beberapa **Task** teknis yang dapat ditemukan dalam `task-decomposition.md`:
> 
> *   **Task 1 (Level 5):** `S1.2-04.1` - Identify Critical Data Elements (CDE) for the 'kependudukan' dataset.
>     *   **Subtask 1.1 (Level 6):** Review data dictionary and business process documents.
>     *   **Subtask 1.2 (Level 6):** Facilitate workshop with data owners to confirm CDEs.
> *   **Task 2 (Level 5):** `S1.2-04.2` - Profile data to establish baseline quality metrics.
>     *   **Subtask 2.1 (Level 6):** Execute data profiling scripts on the dataset.
>     *   **Subtask 2.2 (Level 6):** Analyze profiling results and document findings.
> *   **Task 3 (Level 5):** `S1.2-04.3` - Define and formalize data quality rules.
>     *   **Subtask 3.1 (Level 6):** Draft data quality rules (e.g., completeness, uniqueness, validity) based on findings.
>     *   **Subtask 3.2 (Level 6):** Formalize rules in the data governance tool or a shared repository.
> 
> **Contoh Konkret 2: Data Cataloging**
> 
> Mari kita lihat dekomposisi dari User Story: *"Sebagai Analis Data, saya ingin mencari dan memahami dataset yang relevan dengan cepat agar dapat mempercepat analisis saya."*
> 
> User Story ini dipecah menjadi beberapa **Task** teknis dari layanan [S1.4 Data Governance & Policy Framework Development](services-catalog.md#s14-data-governance--policy-framework-development):
> 
> *   **Task 1 (Level 5):** `S1.4-02.1` - Define metadata standards and taxonomy.
>     *   **Subtask 1.1 (Level 6):** Research industry-standard taxonomies (e.g., DCAT, ISO 11179).
>     *   **Subtask 1.2 (Level 6):** Adapt taxonomy for organizational context.
> *   **Task 2 (Level 5):** `S1.4-03.2` - Implement data cataloging tool.
>     *   **Subtask 2.1 (Level 6):** Configure connectors to priority data sources.
>     *   **Subtask 2.2 (Level 6):** Ingest and index initial set of metadata.
> *   **Task 3 (Level 5):** `S1.4-04.1` - Develop data stewardship and curation workflows.
>     *   **Subtask 3.1 (Level 6):** Define roles and responsibilities for metadata curation.
>     *   **Subtask 3.2 (Level 6):** Create SOP for new dataset registration and certification.
> 
> Dengan demikian, hierarki ini menghubungkan kebutuhan pengguna ("Saya ingin data akurat", "Saya ingin mencari data") dengan pekerjaan teknis spesifik (`S1.2-04.1`, `S1.4-02.1`, dll.) yang memiliki estimasi effort dan biaya dalam COGS.
> 
> ---
> 
> ## Practical Examples per Pillar
> 
> ### Pillar 1: Advisory & Governance (Contoh: S1.2 Data Governance Framework)
> 
> ```
> INITIATIVE: Modernisasi Tata Kelola Data POLRI
>   │
>   ├── EPIC: Pengembangan SOP dan Standar Data & Metadata (S1.2 + S1.4)
>   │     │
>   │     ├── FEATURE: Assessment & Gap Analysis
>   │     │     ├── STORY: Sebagai CDO POLRI, saya ingin mengetahui gap tata kelola data saat ini
>   │     │     │     ├── TASK: Conduct stakeholder interviews (S1.1-01)
>   │     │     │     ├── TASK: Assess current data landscape (S1.1-02)
>   │     │     │     └── TASK: Benchmark against standards (S1.1-04)
>   │     │     └── MILESTONE: Assessment Report Delivered ──→ Termin 1 (30%)
>   │     │
>   │     ├── FEATURE: Framework Design
>   │     │     ├── STORY: Sebagai Data Steward, saya ingin SOP yang jelas untuk pengelolaan data
>   │     │     │     ├── TASK: Design governance structure (S1.2-02)
>   │     │     │     ├── TASK: Define data quality standards (S1.2-04)
>   │     │     │     └── TASK: Create metadata standards (S1.4-03)
>   │     │     └── MILESTONE: Framework Draft Approved ──→ Termin 2 (40%)
>   │     │
>   │     └── FEATURE: Socialization & Handover
>   │           ├── STORY: Sebagai tim IT POLRI, saya ingin pelatihan implementasi SOP
>   │           │     ├── TASK: Conduct training sessions (S3.2)
>   │           │     └── TASK: Create implementation guide
>   │           └── MILESTONE: Final Handover ──→ Termin 3 (30%)
> ```
> 
> ### Pillar 2: Implementation (Contoh: S2.3 Government Data Portal)
> 
> ```
> INITIATIVE: Implementasi Portal Satu Data Provinsi
>   │
>   ├── EPIC: Pembangunan Government Data Portal Platform (S2.3)
>   │     │
>   │     ├── FEATURE: Portal Core Development
>   │     │     ├── STORY: Sebagai admin, saya ingin mengunggah dataset CSV/JSON
>   │     │     │     ├── TASK: Design upload API endpoint
>   │     │     │     ├── TASK: Implement file validation
>   │     │     │     └── TASK: Create upload UI component
>   │     │     └── STORY: Sebagai publik, saya ingin mencari dataset berdasarkan kategori
>   │     │           ├── TASK: Implement search indexing
>   │     │           └── TASK: Build search UI with filters
>   │     │
>   │     ├── FEATURE: Data Quality & Governance Module
>   │     │     ├── STORY: Sebagai data steward, saya ingin validasi otomatis saat upload
>   │     │     └── STORY: Sebagai admin, saya ingin melihat data quality scorecard
>   │     │
>   │     └── FEATURE: Analytics & Visualization
>   │           ├── STORY: Sebagai gubernur, saya ingin dashboard capaian SPM
>   │           └── MILESTONE: Portal Go-Live ──→ Termin Final
> ```
> 
> ### Pillar 3: Empowerment (Contoh: S3.1 DGO as a Service)
> 
> ```
> INITIATIVE: Keberlanjutan Tata Kelola Data Organisasi
>   │
>   ├── EPIC: Operasionalisasi DGO (S3.1)
>   │     │
>   │     ├── FEATURE: DGO Setup & Onboarding (Bulan 1)
>   │     │     ├── STORY: Sebagai CDO, saya ingin struktur DGO yang jelas
>   │     │     └── MILESTONE: DGO Operational ──→ Termin 1
>   │     │
>   │     ├── FEATURE: Monthly Governance Operations (Bulan 2-11)
>   │     │     ├── STORY: Sebagai data owner, saya ingin review kualitas data bulanan
>   │     │     └── STORY: Sebagai DGO, saya ingin tracking compliance metrics
>   │     │
>   │     └── FEATURE: Annual Review & Transition (Bulan 12)
>   │           ├── STORY: Sebagai manajemen, saya ingin laporan tahunan governance
>   │           └── MILESTONE: Annual Assessment Complete ──→ Termin Final
> ```
> 
> ---
> 
> ## Tools & Tracking
> 
> ### Rekomendasi Tools per Engagement Size
> 
> | Ukuran Proyek | Man-days | Tool Rekomendasi | Alasan |
> | :--- | :--- | :--- | :--- |
> | Kecil (< 100 MD) | < 100 | Notion, Trello | Sederhana, visual, kolaborasi mudah. |
> | Sedang (100-500 MD) | 100-500 | Jira, Azure DevOps | Backlog management, sprint tracking, integrasi CI/CD. |
> | Besar (> 500 MD) | > 500 | Jira + Confluence, Azure DevOps | Portfolio management (SAFe), PI planning, knowledge base. |
> | Government (milestone-based) | Any | MS Project + Jira | Gantt chart untuk pelaporan kontrak + agile untuk eksekusi tim. |
> | **IDEAS Standard** | **Any** | **ClickUp** | **Platform terintegrasi untuk semua proyek IDEAS, menghubungkan Tasks, Docs, Goals (OKRs), dan Dashboards dalam satu tempat.** |
> 
> ### Tool Integration in ClickUp
> IDEAS menggunakan ClickUp sebagai platform kerja standar untuk mengimplementasikan hierarki ini. Berikut cara pemetaannya:
> - **Goals** di ClickUp digunakan untuk melacak **Initiatives** dan **Epics**.
> - **Lists** atau **Folders** merepresentasikan **Features**.
> - **Tasks** di ClickUp adalah **User Stories**.
> - **Subtasks** di ClickUp adalah **Tasks** teknis.
> - **Checklists** di dalam subtask digunakan untuk merepresentasikan **Subtasks** granular.
> - **Custom Fields** digunakan untuk melacak atribut penting seperti `Service Code`, `Man-days Estimate`, dan `RAB Line Item`.
> - **Gantt View** digunakan untuk visualisasi timeline dan dependensi, terutama untuk pelaporan ke klien pemerintah.
> 
> ### Government Hybrid Delivery Cadence
> 
> ```
> Quarter 1: Sprint 1-6 → Milestone 1 Deliverable (Waterfall gate)
> Quarter 2: Sprint 7-12 → Milestone 2 Deliverable (Waterfall gate)
> Quarter 3: Sprint 13-18 → Milestone 3 Deliverable (Waterfall gate)
> Quarter 4: Sprint 19-24 → Final Deliverable + Handover (Waterfall gate)
> ```
> 
> Each sprint (2 weeks) produces working increments; each quarter produces formal government deliverables.
> 
> ### Metrik Tracking
> 
> | Level | Metrik | Frekuensi |
> | :--- | :--- | :--- |
> | Initiative | OKR progress, business value delivered | Quarterly |
> | Epic | Scope completion %, budget burn rate | Monthly |
> | Feature | Feature completion %, sprint velocity | Per sprint |
> | User Story | Story points completed, cycle time | Per sprint |
> | Task | Hours logged, blockers | Daily |
> 
> ---
> 
> ## CRISP-DM: Cross-Industry Standard Process for Data Mining
> 
> > **Sumber:** [IDEAS Company Profile](company-profile.md) — Methodology Section
> 
> IDEAS menggunakan **CRISP-DM** sebagai metodologi standar untuk proyek-proyek yang melibatkan analitik data, machine learning, dan data mining. CRISP-DM, bersama Agile, Data Lifecycle, dan PMBOK, membentuk empat pilar metodologi IDEAS.
> 
> ### 6 Fase CRISP-DM
> 
> | Fase | Deskripsi | IDEAS Service Alignment |
> | :--- | :--- | :--- |
> | **1. Business Understanding** | Memahami kebutuhan bisnis dan mendefinisikan tujuan analitik | S1.1, S1.3 |
> | **2. Data Understanding** | Eksplorasi data awal, identifikasi kualitas data, dan temuan awal | S1.3, S2.4 |
> | **3. Data Preparation** | Pembersihan, transformasi, dan integrasi data untuk pemodelan | S2.2, S2.4 |
> | **4. Modeling** | Pemilihan dan penerapan teknik pemodelan yang sesuai | S2.6 |
> | **5. Evaluation** | Evaluasi model terhadap kriteria bisnis dan validasi hasil | S2.6 |
> | **6. Deployment** | Implementasi model ke lingkungan produksi dan monitoring | S2.6, S3.1 |
> 
> ### Integrasi CRISP-DM dengan Agile
> 
> CRISP-DM bersifat iteratif — setiap fase dapat kembali ke fase sebelumnya. Dalam konteks IDEAS, CRISP-DM diintegrasikan dengan Agile melalui:
> 
> 1. **Sprint-based iterations:** Setiap sprint dapat mencakup satu atau lebih fase CRISP-DM
> 2. **Data Product Canvas:** Digunakan untuk mendefinisikan output setiap iterasi CRISP-DM, merujuk pada [data-product-canvas-template.md](../templates/data-product-canvas-template.md).
> 3. **Governance-by-Design:** Data quality rules dan governance policies diterapkan di setiap fase
> 
> ### 4 Pilar Metodologi IDEAS
> 
> | Pilar | Framework | Fokus | Applicable Services |
> | :--- | :--- | :--- | :--- |
> | **Data Management** | Data Lifecycle (DAMA-DMBOK) | Pengelolaan data sepanjang siklus hidup | All services |
> | **Product Development** | Agile (Scrum/Kanban/SAFe) | Pengembangan produk digital dan data | S2.x services |
> | **Data Analytics** | CRISP-DM | Analitik data dan machine learning | S2.4, S2.6 |
> | **Project Management** | PMBOK (6th + 7th Edition) | Governance, delivery, dan value management | All services |
> 
> > **Catatan DAMA-DMBOK:** IDEAS secara aktif memonitor pengembangan **DAMA-DMBOK 3.0** yang diluncurkan pada Juni 2025. Framework kami akan diperbarui untuk menginkorporasi topik-topik baru seperti AI governance, cloud data management, dan data fabresh setelah versi 3.0 dirilis. [2]
> 
> ---
> 
> ## PMBOK-Aligned Project Governance Framework
> 
> IDEAS mengintegrasikan PMBOK (Project Management Body of Knowledge) sebagai pilar keempat metodologi, memberikan kerangka governance dan delivery management yang melengkapi DAMA-DMBOK, Agile, dan CRISP-DM. Integrasi ini mengadopsi pendekatan hybrid yang menggabungkan process-based rigor dari PMBOK 6th Edition dengan principles-based adaptability dari PMBOK 7th Edition.
> 
> ### PMBOK Process Groups → IDEAS Delivery Phases
> 
> Setiap proyek IDEAS melewati lima fase yang selaras dengan PMBOK Process Groups, dengan tailoring berdasarkan sektor klien dan kompleksitas proyek.
> 
> | PMBOK Process Group | IDEAS Delivery Phase | Key Activities | Key Artifacts |
> | :--- | :--- | :--- | :--- |
> | **Initiating** | Engagement Setup | Project Charter, Stakeholder Register, Kick-off Meeting | Signed contract, RASCI matrix, stakeholder map |
> | **Planning** | Sprint 0 / Planning Phase | WBS creation, Sprint Backlog, Risk Register, Communication Plan | Proposal, RAB/HPS, timeline, risk register |
> | **Executing** | Sprint Execution (iterative) | Deliverable production, team coordination, quality assurance | Working increments, sprint demos, status reports |
> | **Monitoring & Controlling** | Continuous Oversight | EVM tracking, scope change control, risk monitoring | CPI/SPI reports, change requests, updated risk register |
> | **Closing** | Handover & Knowledge Transfer | BAST, lessons learned, knowledge transfer sessions | Final deliverables, handover documentation, lessons learned register |
> 
> ### PMBOK Performance Domains → IDEAS Delivery Dimensions
> 
> PMBOK 7th Edition mendefinisikan 8 Performance Domains yang menjadi dimensi perhatian dalam setiap proyek IDEAS. Setiap domain dipetakan ke praktik operasional IDEAS yang sudah ada.
> 
> | Performance Domain | IDEAS Implementation | Measurement |
> | :--- | :--- | :--- |
> | **Stakeholders** | Stakeholder mapping di proposal, engagement plan per milestone | Stakeholder satisfaction survey, feedback loops |
> | **Team** | Squad-based allocation, RASCI per deliverable, Tuckman model for team development | Velocity, team satisfaction, knowledge transfer effectiveness |
> | **Development Approach & Life Cycle** | Hybrid Waterfall-Agile untuk pemerintah, Adaptive untuk enterprise | Approach suitability assessment per engagement |
> | **Planning** | RAB/HPS, sprint planning, complexity scaling (0.7x-1.8x) | Plan accuracy (estimated vs actual man-days) |
> | **Project Work** | Sprint execution, retrospectives, knowledge management | Sprint completion rate, blocker resolution time |
> | **Delivery** | Iterative delivery, UAT, acceptance criteria per deliverable | Deliverable acceptance rate, defect density |
> | **Measurement** | EVM (CPI/SPI), velocity tracking, burn-down charts | CPI ≥ 0.9, SPI ≥ 0.9 as health thresholds |
> | **Uncertainty** | Risk register, contingency budget (5-10%), VUCA analysis | Risk exposure trend, contingency utilization rate |
> 
> ### PMBOK Tailoring Guide per Sector
> 
> Berdasarkan PMBOK 7th Edition Chapter 3 (Tailoring), IDEAS menyesuaikan pendekatan delivery berdasarkan sektor klien.
> 
> | Aspek | Pemerintah (Government) | Enterprise / BUMN | International |
> | :--- | :--- | :--- | :--- |
> | **Development Approach** | Hybrid (Waterfall gates + Agile sprints) | Adaptive (Scrum/Kanban) | Predictive or Hybrid |
> | **Governance Level** | High (formal change control, steering committee) | Medium (product owner decisions) | High (cross-border compliance) |
> | **Documentation** | Extensive (BAST, berita acara, laporan kemajuan) | Lean (user stories, sprint reports) | Moderate (international standards) |
> | **Milestone Structure** | Quarterly termin-based (30-40-30 or 30-30-40) | Sprint-based (bi-weekly demos) | Phase-based (Discovery-Design-Build-Run) |
> | **Risk Management** | Formal risk register + contingency in RAB | Risk backlog in sprint planning | Comprehensive risk assessment |
> | **Change Control** | Formal CCB (Change Control Board) | Product backlog reprioritization | Formal change request process |
> | **Quality Assurance** | UAT + formal acceptance (BAST) | Continuous testing + sprint review | ISO-aligned quality gates |
> | **Stakeholder Engagement** | Steering committee + monthly reports | Sprint demos + retrospectives | Regular status calls + quarterly reviews |
> | **Compliance** | Perpres 46/2025, SPBE, SDI | Industry standards, UU PDP | Local regulations + international standards |
> 
> ### PMBOK-Enhanced Hybrid Delivery Cadence
> 
> Berikut adalah cadence delivery yang telah diperkaya dengan PMBOK governance layers, menunjukkan bagaimana PMBOK Process Groups beroperasi di atas Agile sprint cadence.
> 
> ```
>                     PMBOK GOVERNANCE LAYER
> +--------------------------------------------------------------------+
> | Initiating | Planning |         Executing & Monitoring         | Closing |
> +--------------------------------------------------------------------+
>       |          |               |               |                |
>       ▼          ▼               ▼               ▼                ▼
> +----------+ +-------------+ +-------------+ +--------------+ +-----------+
> | Kick-off | | Q1 Sprints  | | Q2 Sprints  | | Q3 Sprints   | | Q4 Sprints| + Handover
> |          | | (1-6)       | | (7-12)      | | (13-18)      | | (19-24)   | + BAST
> +----------+ +-------------+ +-------------+ +--------------+ +-----------+
>              | Milestone 1 | | Milestone 2 | | Milestone 3  | | Final     |
>              | Deliverable | | Deliverable | | Deliverable  | | Deliverable|
>              +-------------+ +-------------+ +--------------+ +-----------+
>                  (Termin 1)    (Termin 2)      (Termin 3)       (Termin 4)
> 
>                      AGILE DELIVERY LAYER
> ```
> 
> ---
> 
> ## Glossary of Terms
> 
> | Akronim | Kepanjangan | Konteks |
> | :--- | :--- | :--- |
> | **BAST** | Berita Acara Serah Terima | Dokumen legal serah terima pekerjaan, prasyarat untuk termin pembayaran. |
> | **CCB** | Change Control Board | Komite formal yang me-review dan menyetujui perubahan scope dalam proyek pemerintah. |
> | **COGS** | Cost of Goods Sold | Biaya langsung yang terkait dengan produksi barang atau jasa. Di IDEAS, ini adalah biaya man-days. |
> | **CPI** | Cost Performance Index | Ukuran efisiensi biaya proyek (EV/AC). Nilai < 1.0 mengindikasikan over budget. |
> | **EVM** | Earned Value Management | Metodologi manajemen proyek untuk mengukur kinerja proyek secara objektif. |
> | **HPS** | Harga Perkiraan Sendiri | Estimasi biaya yang disusun oleh panitia pengadaan, digunakan sebagai acuan. (Owner's Estimate) |
> | **Perpres** | Peraturan Presiden | Peraturan perundang-undangan yang ditetapkan oleh Presiden Indonesia. |
> | **PMK** | Peraturan Menteri Keuangan | Peraturan yang ditetapkan oleh Menteri Keuangan, seringkali terkait standar biaya. |
> | **RAB** | Rencana Anggaran Biaya | Rincian usulan biaya proyek yang diajukan oleh penyedia jasa. |
> | **SBM** | Standar Biaya Masukan | Batas tertinggi biaya yang dapat dialokasikan dalam anggaran pemerintah (ditetapkan oleh PMK). |
> | **SELC** | Systems Engineering Life Cycle | Metodologi pengembangan sistem yang umum digunakan di lingkungan pemerintah. |
> | **SPI** | Schedule Performance Index | Ukuran efisiensi jadwal proyek (EV/PV). Nilai < 1.0 mengindikasikan keterlambatan. |
> | **UAT** | User Acceptance Testing | Fase pengujian akhir dimana pengguna/klien memvalidasi fungsionalitas sistem. |
> | **VUCA** | Volatility, Uncertainty, Complexity, Ambiguity | Kerangka kerja untuk menggambarkan lingkungan bisnis yang menantang dan tidak stabil. |
> 
> ---
> 
> ## References
> 
> [1] Peraturan Presiden (Perpres) Nomor 46 Tahun 2025 tentang Perubahan Kedua atas Perpres 16/2018 tentang Pengadaan Barang/Jasa Pemerintah.
> [2] DAMA International. (2025). *DMBOK 3 Project*. Retrieved from DAMA International website. (Status as of February 2026)
> 
