# Bank Use Case — 50+ Use Case untuk 10 Skill IDEAS (Cockburn Levels)
# Use Case Bank — 50+ Use Cases for 10 IDEAS Skills (Cockburn Levels)

> Dokumentasi per Cockburn goal levels: ☁️ Cloud (enterprise) → 🪁 Kite (summary) → 🌊 Sea (user goal) → 🐟 Fish (subfunction)
> Setiap use case: 5W1H + skill mapping + impact-feasibility score + contoh prompt

---

## KATEGORI 1: Product Development (UC-01 — UC-10)

### UC-01 ☁️ End-to-End Digital Product Build
- **Who**: Full product team (PM+BA+ER+PA+UXR+PDS) untuk klien enterprise/pemerintah
- **What**: Membangun produk digital dari ide hingga launch
- **When**: Ada kebutuhan produk baru, budget ≥Rp 500jt, timeline 3-12 bulan
- **Where**: Semua 10 skill | Environment: cloud-native
- **Why**: Deliver value ke end users, revenue/impact generation
- **How**: Stage-Gate 5 fase + Dual-Track Agile | Lihat Panduan 1
- **Skills**: PM(PRD,roadmap) → PR(research-plan) → BA(BRD,SRS) → ER(system-design) → PDS(sprint-plan,gtm-launch) → PA(tracking-plan,health-scorecard) → UXR(usability-test)
- **Impact**: ⭐⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐ | **Complexity**: L4 Expert
- **Prompt**: "Orkestrasi full product development untuk [deskripsi produk]. Budget [Rp], timeline [bulan]. Mulai dari project context canvas."

### UC-02 🌊 New Feature Development
- **Who**: PM + BA + ER + PA | Tim: 3-5 orang
- **What**: Menambah fitur baru pada produk existing berdasarkan user feedback
- **When**: Quarterly planning, ada validated demand | Timeline: 4-8 minggu
- **Skills**: PM(feature-spec,prfaq) → BA(use-case,user-story-bdd) → ER(adr) → PA(experiment-design,tracking-plan) → PDS(sprint-plan)
- **Impact**: ⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐⭐ | **Complexity**: L2-L3
- **Prompt**: "Buatkan PR/FAQ untuk fitur [nama fitur]. User problem: [masalah]. Lalu generate use cases dan tracking plan."

### UC-03 🌊 Product Redesign / UX Overhaul
- **Who**: UXR + PR + PM + BA
- **What**: Redesign UX/UI aplikasi existing
- **When**: NPS < 0, SUS score < 68, high churn | Timeline: 2-4 bulan
- **Skills**: UXR(heuristic-eval,usability-test-plan,usability-test-report) → PR(interview-guide,research-persona) → PM(persona,journey-map) → BA(use-case) → PDS(sprint-plan)
- **Prompt**: "Lakukan heuristic evaluation terhadap [aplikasi] menggunakan Nielsen 10 heuristics. Lalu buatkan usability test plan."

### UC-04 🌊 Pricing Strategy Development
- **Who**: PM + PR + PA
- **What**: Mengembangkan/revisi strategi pricing produk
- **Skills**: PR(pricing-research) → PM(pricing-strategy) → PA(experiment-design untuk pricing A/B test) → PDS(sales-enablement)
- **Prompt**: "Buatkan pricing strategy untuk [produk]. Current pricing: [X]. Kompetitor: [A=$X, B=$Y]. Target: [segmen]."

### UC-05 🐟 Persona Creation (Research-Validated)
- **Who**: PR + PM + UXR
- **Skills**: PR(interview-guide → research-persona) → PM(persona) → UXR(card-sort untuk IA validation)
- **Prompt**: "Buatkan research-validated persona dari [N] interview transcripts. Distinguish facts vs hypotheses."

### UC-06 🌊 Competitive Intelligence Program
- **Who**: PR + PM + UXR + PDS
- **What**: Program competitive intelligence sistematis untuk positioning dan win rate
- **When**: Quarterly update, sebelum market entry, saat win rate turun | Timeline: 4-6 minggu
- **Where**: Discovery phase, recurring quarterly
- **Why**: Informed positioning, better win rate, defensible differentiation
- **How**: Research → Analyze → Position → Arm Sales
- **Skills**: PR(competitive-deep,trend-analysis) → UXR(competitive-ux) → PM(competitive-analysis) → PDS(battlecard,positioning,sales-enablement)
- **Impact**: ⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐⭐ | **Complexity**: L3 Advanced
- **Prompt**: "Analisis kompetitif mendalam: [produk] vs [A, B, C]. Feature matrix, UX benchmark, pricing comparison, positioning map 2x2, dan battlecard untuk sales."

### UC-07 🌊 Full Product Launch (Cross-Functional)
- **Who**: PDS (lead) + PM + PR + PA + UXR + ER
- **What**: Launch produk/fitur major dengan koordinasi 6+ skill
- **When**: Fitur ready for release, GTM alignment needed | Timeline: 8 minggu (T-8w countdown)
- **Where**: Build → Launch transition (Gate 3 → Gate 4)
- **Why**: Coordinated launch maximizes adoption, minimizes post-launch issues
- **How**: T-8w positioning → T-6w enablement → T-4w readiness → T-0 launch → T+2w review
- **Skills**: PDS(gtm-launch,positioning,launch-readiness,sales-enablement) → PR(competitive-deep,win-loss) → PA(health-scorecard,tracking-plan) → UXR(accessibility-audit) → ER(runbook,performance-benchmark) → PM(product-launch-checklist)
- **Impact**: ⭐⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐ | **Complexity**: L4 Expert
- **Prompt**: "Launch produk [nama] dalam 8 minggu. Orkestrasi GTM: positioning, enablement, readiness check, launch day plan, T+2w review. Koordinasi 6 skill."

### UC-08 🌊 A/B Testing & Experimentation Program
- **Who**: PA + PM + UXR
- **What**: Program eksperimentasi sistematis (weekly experiment cadence)
- **When**: Post-launch, ketika ada fitur yang perlu divalidasi | Timeline: ongoing
- **Why**: Data-driven decision making, reduce HIPPO bias
- **How**: Hypothesis → Design → Run → Analyze → Ship/Kill → Repeat
- **Skills**: PA(experiment-design,sample-size,ab-test-report) → PM(feature-spec untuk winning variants) → UXR(prototype-test untuk qual validation)
- **Impact**: ⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐⭐ | **Complexity**: L2-L3
- **Prompt**: "Setup experimentation program: hipotesis backlog, prioritization (ICE), sample size calculator, weekly cadence. Baseline CR: [X]%, traffic: [Y]/week."

### UC-09 🌊 Quarterly Product Review Cadence
- **Who**: PM + PA + PDS
- **What**: Review performa produk quarterly dengan data-backed insights
- **When**: Setiap akhir quarter | Timeline: 1-2 minggu preparation
- **Why**: Accountability, course correction, OKR tracking
- **How**: Collect metrics → Analyze trends → Identify actions → Present → Decide
- **Skills**: PM(product-review,metrics-dashboard) → PA(health-scorecard,funnel-analysis,cohort-retention) → PDS(dora-dashboard,retrospective)
- **Impact**: ⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐⭐⭐ | **Complexity**: L2
- **Prompt**: "Buatkan quarterly product review Q[N]. Metrics: AARRR + DORA. Include: trends, wins, concerns, action items, next quarter priorities."

### UC-10 🌊 Customer Journey Mapping (Research-Backed)
- **Who**: PM + PR + UXR
- **What**: Journey map berdasarkan riset (bukan asumsi) — end-to-end customer experience
- **When**: Discovery phase, redesign, atau saat CX score turun | Timeline: 3-4 minggu
- **Why**: Identify moments of truth, pain points, opportunity for delight
- **How**: Research → Map → Validate → Prioritize → Design improvements
- **Skills**: PR(interview-guide,research-persona,journey-research) → PM(persona,journey-map) → UXR(card-sort,usability-test-plan) → PA(funnel-analysis untuk quantitative overlay)
- **Impact**: ⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐⭐ | **Complexity**: L3 Advanced
- **Prompt**: "Buatkan customer journey map untuk [persona] di [produk]. Stages, touchpoints, emotions, pain points. Overlay dengan funnel data. Evidence-based, bukan asumsi."

---

## KATEGORI 2: Data Management & Governance (UC-11 — UC-20)

### UC-11 ☁️ Enterprise Data Governance Program
- **Who**: DM + DAMA + BA + ER + PDS | CDO/CIO sponsor
- **What**: Framework tata kelola data lengkap dari nol
- **When**: Organisasi belum punya DG atau maturity < level 2 | Timeline: 12-24 bulan
- **Skills**: DAMA(KA-14 maturity) → DM(maturity-assessment,data-strategy) → DAMA(KA-01 charter) → DM(architecture-blueprint) → DAMA(KA-11 quality) → BA(stakeholder,raci) → PDS(sprint-plan,change-management)
- **Impact**: ⭐⭐⭐⭐⭐ | **Feasibility**: ⭐⭐⭐ | **Complexity**: L4 Expert
- **Prompt**: "Orkestrasi program data governance untuk [organisasi]. Maturity: [level/unknown]. Full program dari assessment hingga implementation."

### UC-12 🌊 Data Maturity Assessment
- **Who**: DM + DAMA
- **What**: Mengukur maturity level data management organisasi
- **Skills**: DAMA(KA-14 → maturity-calculator.py) + DM(maturity-assessment)
- **Impact**: ⭐⭐⭐⭐ | **Complexity**: L2
- **Prompt**: "Lakukan data management maturity assessment untuk [organisasi] menggunakan CMMI-DMM. Assess 14 Knowledge Area."

### UC-13 🌊 Data Mesh Implementation
- **Who**: DM + ER + DAMA
- **What**: Transisi ke arsitektur data mesh
- **Skills**: DM(mesh-readiness,data-product-canvas,architecture-blueprint) → DAMA(concepts-modern-paradigms) → ER(system-design,adr)
- **Prompt**: "Evaluasi kesiapan organisasi untuk data mesh. 5 domain bisnis, 3 data engineer, Snowflake data warehouse."

### UC-14 🌊 Data Quality Improvement
- **Skills**: DAMA(KA-11) → DM(dq-framework-comparison) → PA(metric-definition,health-scorecard) → BA(rca,business-rules)
- **Prompt**: "Buatkan DQ framework: 6 dimensi, measurement methodology, thresholds, remediation process."

### UC-15 🌊 MDM Strategy
- **Who**: DM + DAMA + BA + ER
- **What**: Strategi master data management untuk konsistensi data lintas sistem
- **When**: Multiple systems punya definisi entitas berbeda | Timeline: 3-6 bulan
- **Skills**: DM(mdm-strategy) → DAMA(KA-10) → BA(data-dictionary) → ER(system-design)
- **Impact**: ⭐⭐⭐⭐ | **Complexity**: L3
- **Prompt**: "Buatkan MDM strategy: golden record approach, match/merge rules, governance model. 3 source systems, entity: customer."

### UC-16 🌊 Data Catalog Implementation
- **Who**: DM + DAMA + ER
- **What**: Implementasi catalog untuk data discoverability dan lineage
- **When**: >50 data assets tanpa dokumentasi | Timeline: 3-6 bulan
- **Skills**: DM(catalog-evaluation,tool-landscape) → DAMA(KA-09) → ER(system-design)
- **Impact**: ⭐⭐⭐⭐ | **Complexity**: L3
- **Prompt**: "Evaluasi 3 catalog tools (Atlan vs Collibra vs DataHub) untuk organisasi kami. 200+ tabel, Snowflake."

### UC-17 🌊 Privacy Impact Assessment
- **Who**: DM + DAMA + ER + BA
- **What**: PIA untuk fitur/sistem yang memproses data pribadi
- **When**: Sebelum launch fitur data pribadi, compliance UU PDP | Timeline: 2-4 minggu
- **Skills**: DM(pia) → DAMA(KA-05,KA-12) → ER(threat-model) → BA(nfr)
- **Impact**: ⭐⭐⭐⭐⭐ | **Complexity**: L3
- **Prompt**: "Lakukan PIA untuk fitur yang mengumpulkan data lokasi. Regulasi: UU PDP Indonesia. Breach notification 3×24 jam."

### UC-18 🐟 Data Strategy Document
- **Who**: DM | **What**: Dokumen strategi data organisasi
- **Skills**: DM(data-strategy)
- **Complexity**: L2
- **Prompt**: "Buatkan data strategy: vision, principles, current state, target state, initiatives, governance model, success metrics."

### UC-19 🐟 Standards Mapping
- **Who**: DM | **What**: Mapping standar data (ISO 8000, FAIR, UU PDP, GDPR)
- **Skills**: DM(standards-mapping,fair-assessment)
- **Complexity**: L2
- **Prompt**: "Map standar data yang berlaku: UU PDP vs GDPR, ISO 8000, FAIR principles. Gap analysis per standar."

### UC-20 🐟 Tool Landscape Evaluation
- **Who**: DM | **What**: Evaluasi tools data management di pasar
- **Skills**: DM(tool-landscape,catalog-evaluation)
- **Complexity**: L2
- **Prompt**: "Evaluasi landscape tools untuk [kategori: catalog/quality/lineage/MDM]. Top 5 per kategori, comparison matrix."

---

## KATEGORI 3: Government & SPBE (UC-21 — UC-28)

### UC-21 ☁️ SPBE Score Improvement Program
- **Who**: IDEAS + DM + DAMA + BA + PDS
- **What**: Meningkatkan skor SPBE instansi
- **When**: Menjelang evaluasi SPBE | Timeline: 6-18 bulan
- **Skills**: IDEAS(SPBE framework) → BA(gap-analysis) → DAMA(DAMA-SPBE alignment) → DM(architecture-blueprint) → IDEAS(policy-framework) → PDS(release-plan,change-management)
- **Impact**: ⭐⭐⭐⭐⭐ | **Complexity**: L4 Expert
- **Prompt**: "Skor SPBE [instansi] = [skor], target [target]. Buatkan gap analysis per domain + roadmap + proposal."

### UC-22 🌊 Satu Data Indonesia Implementation
- **Skills**: IDEAS(policy-framework) → DAMA(KA-01,KA-09) → DM(standards-mapping) → BA(stakeholder)
- **Prompt**: "Buatkan policy framework Satu Data Indonesia untuk Pemkot. Mencakup: kebijakan, standar metadata, walidata."

### UC-23 🌊 Government Procurement Proposal (LKPP)
- **Skills**: IDEAS(technical-proposal,boq,surat-penawaran) → BA(feasibility) → DM(data-strategy preview)
- **Prompt**: "Technical proposal pengadaan 'Portal Data Terpadu' Dinas Kominfo. Budget pagu Rp 1.5M."

### UC-24 🌊 Enterprise/BUMN Pitch
- **Who**: IDEAS + PM
- **What**: Pitch deck untuk klien enterprise/BUMN
- **When**: Ada peluang bisnis, pre-proposal | Timeline: 1-2 minggu
- **Skills**: IDEAS(pitch-deck,service-description) → PM(product-brief) → IDEAS(competitive-landscape)
- **Complexity**: L2
- **Prompt**: "Buatkan pitch deck untuk [klien BUMN]. Kebutuhan: [deskripsi]. Gunakan Shipley win themes + competitive differentiators."

### UC-25 🐟 Service Recommendation
- **Who**: IDEAS | **What**: Rekomendasi layanan IDEAS berdasarkan kebutuhan klien
- **Skills**: IDEAS(scripts/recommend_service.py)
- **Prompt**: "Jalankan /ideas-company → scripts/recommend_service.py --need '[kebutuhan]' --sector [government/enterprise]"

### UC-26 🐟 Cost Estimation
- **Who**: IDEAS | **What**: Estimasi biaya layanan per level kompleksitas
- **Skills**: IDEAS(scripts/estimate_service_cost.py)
- **Prompt**: "Jalankan /ideas-company → scripts/estimate_service_cost.py --service [kode] --level [N] --breakdown"

### UC-27 🐟 SPBE Score Lookup
- **Who**: IDEAS | **What**: Cek skor SPBE instansi target
- **Skills**: IDEAS(scripts/query_spbe.py, references/client-intelligence-spbe.md)
- **Prompt**: "Cek skor SPBE [instansi/provinsi]. Benchmark vs rata-rata nasional (3.12/5). Identifikasi domain terlemah."

### UC-28 🐟 Case Study Reference
- **Who**: IDEAS | **What**: Referensi case study untuk proposal/pitch
- **Skills**: IDEAS(references/case-studies.md)
- **Prompt**: "Cari case study IDEAS yang relevan untuk [tipe project] di [sektor]. Sertakan lessons learned + testimonials."

---

## KATEGORI 4: Analytics & Experimentation (UC-29 — UC-35)

### UC-29 🌊 Analytics Stack Setup from Zero
- **Skills**: PA(tracking-plan,data-taxonomy,metric-definition) → PM(okr,metrics-dashboard) → ER(system-design)
- **Prompt**: "Setup analytics dari nol untuk [produk]. Events, taxonomy, dashboard. Platform: [Amplitude/Mixpanel/PostHog]."

### UC-30 🌊 Experimentation Program
- **Skills**: PA(experiment-design,sample-size,ab-test-report) → PM(feature-spec)
- **Prompt**: "Desain A/B test: '[hipotesis]'. Baseline CR [X]%. Traffic [Y]/week. Calculate sample + duration."

### UC-31 🌊 Product Health Dashboard
- **Who**: PA + PM + PDS
- **What**: Dashboard terpadu metrics produk + delivery + growth
- **When**: Post-launch, quarterly review cadence | Timeline: 2-3 minggu setup
- **Skills**: PA(health-scorecard,saas-dashboard) → PM(metrics-dashboard) → PDS(dora-dashboard,growth-dashboard)
- **Complexity**: L3
- **Prompt**: "Buatkan product health dashboard: AARRR metrics + DORA metrics + growth indicators. Data sources: [tools]."

### UC-32 🌊 Data Storytelling for C-Level
- **Who**: PA + PM
- **What**: Narrative data story untuk presentasi eksekutif (Knaflic framework)
- **When**: Board meeting, quarterly review, investor update | Timeline: 1-2 minggu
- **Skills**: PA(data-story,analytics-brief) → PM(product-review)
- **Complexity**: L2
- **Prompt**: "Buatkan data story untuk [audience C-Level] tentang [insight]. Framework: Context→Data→Insight→Recommendation."

### UC-33 🐟 Funnel Analysis
- **Who**: PA | **What**: Analisis conversion funnel per step
- **Skills**: PA(funnel-analysis)
- **Prompt**: "Analisis funnel [journey]: [steps]. Per step: volume, CR, drop-off %. Segment by [dimension]. Top 3 recommendations."

### UC-34 🐟 Cohort Retention
- **Who**: PA | **What**: Analisis retention per cohort (D1/D7/D30/D90)
- **Skills**: PA(cohort-retention)
- **Prompt**: "Analisis cohort retention bulanan. Identify best/worst cohorts, retention curve shape, benchmark vs industry."

### UC-35 🐟 Segmentation
- **Who**: PA | **What**: Behavioral segmentation pengguna
- **Skills**: PA(segmentation)
- **Prompt**: "Segmentasi users berdasarkan [behavior/engagement/value]. Identify: segment size, characteristics, actionable strategies per segment."

---

## KATEGORI 5: Technical Architecture (UC-36 — UC-40)

### UC-36 🌊 System Design for New Service
- **Who**: ER + BA + DM
- **What**: Desain arsitektur sistem baru (Google design doc format)
- **When**: Awal project atau fitur major baru | Timeline: 2-4 minggu
- **Skills**: ER(system-design) → BA(srs,nfr) → DM(architecture-blueprint) → ER(adr)
- **Complexity**: L3
- **Prompt**: "Desain arsitektur untuk [service]. Requirements: [list]. Constraints: [infra, scale, budget]. Include: C4 diagram, API contracts, data model."

### UC-37 🌊 API Design & Documentation
- **Who**: ER + BA
- **What**: Desain REST/GraphQL API dengan dokumentasi OpenAPI
- **When**: Sebelum development, saat integrasi dengan tim lain | Timeline: 1-2 minggu
- **Skills**: ER(api-design) → BA(srs) → ER(technical-rfc)
- **Complexity**: L2
- **Prompt**: "Desain REST API untuk [service]. Endpoints, schemas, auth, error codes, pagination. OpenAPI 3.1 format."

### UC-38 🌊 Security Threat Modeling
- **Who**: ER + BA + DM
- **What**: Threat modeling STRIDE untuk identifikasi security risks
- **When**: Sebelum launch, setelah architecture review | Timeline: 1-2 minggu
- **Skills**: ER(threat-model) → BA(nfr) → DM(pia)
- **Complexity**: L3
- **Prompt**: "Threat modeling STRIDE untuk [system]. Per threat category: identify, assess risk (likelihood×impact), mitigate."

### UC-39 🌊 Platform Migration
- **Who**: ER + BA + DM + PDS
- **What**: Migrasi platform (legacy→modern, on-prem→cloud)
- **When**: EOL system, scalability issues | Timeline: 3-12 bulan
- **Skills**: ER(system-design,adr,architecture-review) → BA(gap-analysis,impact-analysis) → PDS(release-plan,change-management)
- **Complexity**: L4
- **Prompt**: "Migrasi [source] ke [target]. Data volume: [X]GB, [N] API endpoints. ADR + phased release plan + rollback strategy."

### UC-40 🐟 Tech Debt Management
- **Who**: ER + PDS
- **What**: Register dan prioritisasi tech debt
- **Skills**: ER(tech-debt-register) → PDS(sprint-plan)
- **Prompt**: "Buatkan tech debt register. Per item: description, impact, effort, priority. Alokasi 15-20% sprint capacity."

---

## KATEGORI 6: Delivery & GTM (UC-41 — UC-46)

### UC-41 🌊 Agile Transformation
- **Who**: PDS (lead)
- **What**: Assessment dan improvement agile maturity organisasi
- **When**: Tim baru ke agile, atau stagnasi delivery | Timeline: 3-6 bulan
- **Skills**: PDS(agile-maturity,team-agreement,retrospective,dora-dashboard)
- **Complexity**: L3
- **Prompt**: "Assess agile maturity tim kami. Current: [Scrum/Kanban/none]. Buatkan improvement plan + team agreement + DORA baseline."

### UC-42 🌊 SAFe PI Planning
- **Who**: PDS + PM
- **What**: Program Increment planning untuk 50-125 orang (8-12 week PI)
- **When**: Setiap PI boundary | Timeline: 2-day event + prep
- **Skills**: PDS(pi-planning,release-plan) + PM(roadmap,okr)
- **Complexity**: L4
- **Prompt**: "Facilitasi PI Planning: [N] teams, PI duration [weeks]. Vision, features, capacity, dependencies. Confidence vote mechanism."

### UC-43 🌊 GTM Launch Campaign
- **Who**: PDS + PR + PA
- **What**: Koordinasi launch produk cross-functional (T-8w countdown)
- **When**: Fitur ready for market | Timeline: 8 minggu
- **Skills**: PDS(gtm-launch,positioning,sales-enablement,battlecard,launch-readiness) + PR(competitive-deep,win-loss) + PA(health-scorecard)
- **Complexity**: L4
- **Prompt**: "GTM launch [produk]. T-8w countdown: positioning → enablement → readiness → launch → review. RACI per workstream."

### UC-44 🌊 Change Management Program
- **Who**: PDS + BA
- **What**: Program change management (ADKAR) untuk adopsi sistem baru
- **When**: New system rollout, proses berubah | Timeline: 3-6 bulan
- **Skills**: PDS(change-management,onboarding-playbook) + BA(impact-analysis,stakeholder)
- **Complexity**: L3
- **Prompt**: "Change management plan ADKAR untuk rollout [sistem]. Stakeholders: [list]. Adaptasi untuk konteks [government/enterprise]."

### UC-45 🐟 Sprint Planning
- **Who**: PDS | **What**: Perencanaan sprint capacity-based
- **Skills**: PDS(sprint-plan)
- **Prompt**: "Sprint plan Sprint [N], [duration]. Goal: [goal]. Capacity: [points]. Stories + assignees + acceptance criteria."

### UC-46 🐟 Retrospective
- **Who**: PDS | **What**: Fasilitasi retrospective dengan action items
- **Skills**: PDS(retrospective)
- **Prompt**: "Fasilitasi retro Sprint [N]. Format: [4Ls/Start-Stop-Continue/Sailboat]. Max 3 action items dengan owner + due date."

---

## KATEGORI 7: Research & Discovery (UC-47 — UC-50)

### UC-47 🌊 Customer Discovery Program
- **Who**: PR + UXR + PM
- **What**: Program discovery sistematis untuk validasi problem-solution fit
- **When**: Sebelum build, validasi asumsi | Timeline: 4-6 minggu
- **Skills**: PR(research-plan,interview-guide) + UXR(usability-test-plan) + PM(persona,journey-map)
- **Complexity**: L3
- **Prompt**: "Program customer discovery untuk [produk/ide]. Target: [N] interviews. Metodologi: Mom Test. Output: validated personas + journey map."

### UC-48 🌊 VoC Program
- **Who**: PR + PA + PM
- **What**: Program Voice of Customer sistematis (continuous)
- **When**: Post-launch, ongoing feedback loop | Timeline: ongoing quarterly
- **Skills**: PR(voc-report,thematic-analysis,insight-report) + PA(segmentation) + PM(product-review)
- **Complexity**: L3
- **Prompt**: "Setup VoC program: collection channels, thematic analysis cadence, segmented insights, quarterly report format."

### UC-49 🌊 Competitive Intelligence
- **Who**: PR + UXR + PDS
- **What**: Program competitive intel untuk positioning dan win rate
- **When**: Quarterly update, sebelum tender | Timeline: 4-6 minggu
- **Skills**: PR(competitive-deep,trend-analysis) + UXR(competitive-ux) + PDS(battlecard)
- **Complexity**: L3
- **Prompt**: "Competitive intel: [produk] vs [A, B, C]. Feature matrix + UX benchmark + pricing + positioning map + battlecard."

### UC-50 🌊 PMF Assessment
- **Who**: PR + PA
- **What**: Assessment product-market fit (Sean Ellis test + retention curve)
- **When**: Post-launch 3-6 bulan, sebelum scale | Timeline: 2-4 minggu
- **Skills**: PR(pmf-analysis,survey-design) + PA(cohort-retention,health-scorecard)
- **Complexity**: L3
- **Prompt**: "Assess PMF: Sean Ellis survey (target >40% very disappointed), retention curve analysis, engagement depth metrics."

---

## INDUSTRY-SPECIFIC USE CASES (Round 9: Banking, Government, Enterprise)

### UC-51 🏦 Banking: AML Graph Analytics Architecture
- **Who**: ER + DM + DAMA + BA
- **What**: Anti-money laundering system dengan graph database + streaming detection
- **When**: Bank butuh PPATK compliance atau upgrade dari rule-based AML | Timeline: 4-6 bulan
- **Skills**: ER(system-design: Neo4j/TigerGraph + Kafka + Flink) + DM(data-strategy: entity resolution) + DAMA(KA-05 security, KA-06 integration) + BA(requirements: POJK + UU 8/2010)
- **Complexity**: L4
- **Impact**: High (regulatory compliance + fraud reduction)
- **Prompt**: "Desain AML architecture untuk bank [nama]. Volume: [N] transaksi/hari. Regulasi: POJK 12/2017 + PPATK. Architecture: graph DB untuk entity resolution + Kafka streaming untuk real-time detection + ML scoring."

### UC-52 🏦 Banking: BCBS 239 Compliance Assessment
- **Who**: DAMA + DM + BA
- **What**: Gap assessment terhadap 14 prinsip BCBS 239 (risk data aggregation)
- **When**: Bank yang ingin improve risk reporting atau diminta regulator | Timeline: 6-8 minggu
- **Skills**: DAMA(KA-14 maturity + KA-01 governance) + DM(maturity-assessment: BCBS 239 mapping) + BA(gap-analysis per 14 prinsip)
- **Complexity**: L3
- **Prompt**: "Assess BCBS 239 compliance untuk [bank]. Evaluate 14 principles: governance, architecture, accuracy, completeness, timeliness, adaptability. Map ke DAMA KAs. Output: gap scorecard + roadmap."

### UC-53 🏦 Banking: SNAP Open API Integration
- **Who**: ER + BA + PA
- **What**: Integrasi SNAP (Standar Nasional Open API Pembayaran) per BI mandate
- **When**: Bank/fintech yang belum comply SNAP deadline | Timeline: 3-4 bulan
- **Skills**: ER(api-design: SNAP standard + ISO 27001) + BA(requirements: partner integration matrix) + PA(analytics-dashboard: API usage metrics)
- **Complexity**: L3
- **Prompt**: "Desain SNAP integration plan untuk [bank]. Services: direct debit, transfer, QRIS. Include: API gateway architecture, security (OAuth 2.0, mTLS), partner onboarding flow, monitoring dashboard."

### UC-54 🏦 Banking: Core Banking Migration Data Strategy
- **Who**: ER + DM + DAMA + PDS
- **What**: Data migration strategy dari legacy core banking ke cloud-native platform
- **When**: Bank modernisasi dari Temenos T24/Silverlake ke Thought Machine/Mambu | Timeline: 12-24 bulan
- **Skills**: ER(system-design: migration architecture) + DM(data-strategy: data mapping) + DAMA(KA-06 integration, KA-04 storage) + PDS(release-plan: progressive migration)
- **Complexity**: L4
- **Prompt**: "Data migration strategy dari [legacy system] ke [target]. Domains: customers, accounts, transactions. Approach: progressive capability-based + dual-running. Include: data mapping framework, validation rules, reconciliation plan."

### UC-55 🏛️ Government: Open Data Portal Implementation
- **Who**: ER + DM + DAMA + BA
- **What**: Deploy open data portal CKAN sesuai Satu Data Indonesia (Perpres 39/2019)
- **When**: Pemerintah daerah yang belum punya portal data terbuka | Timeline: 3-6 bulan
- **Skills**: ER(system-design: CKAN + metadata API) + DM(data-strategy: SDI compliance) + DAMA(KA-09 metadata standards) + BA(requirements: dataset inventory)
- **Complexity**: L3
- **Prompt**: "Implementasi open data portal untuk [instansi]. Platform: CKAN. Requirements: SDI metadata compliance, integrasi data.go.id, kode referensi standar. Dataset target: [N] datasets dari [N] OPD."

### UC-56 🏛️ Government: Smart City Data Platform
- **Who**: ER + PA + DM + PDS
- **What**: Platform data smart city (IoT + citizen services + analytics dashboard)
- **When**: Kota yang implement smart city program | Timeline: 6-18 bulan
- **Skills**: ER(system-design: IoT data lake + API gateway) + PA(analytics-dashboard: 6 pillars) + DM(data-strategy: cross-OPD integration) + PDS(release-plan: phased rollout)
- **Complexity**: L4
- **Reference**: Jakarta Smart City (JAKI: 56 departments, 9-hour avg complaint handling, 88% completion rate)
- **Prompt**: "Desain smart city data platform untuk [kota]. Pillars: governance, society, economy, living, environment, branding. Include: IoT integration, citizen app, cross-OPD data lake, performance dashboard aligned SAKIP."

### UC-57 🏛️ Government: SAKIP Performance Dashboard
- **Who**: PA + BA + PDS
- **What**: Dashboard kinerja instansi aligned ke SAKIP/e-Monev hierarchy
- **When**: Instansi yang ingin improve akuntabilitas kinerja | Timeline: 2-4 bulan
- **Skills**: PA(analytics-dashboard: KPI hierarchy K1-K8) + BA(requirements: Renstra/Renja mapping) + PDS(sprint-plan)
- **Complexity**: L2
- **Prompt**: "Dashboard kinerja untuk [instansi]. Hierarchy: Renstra → Renja → IKU → IKK. Data source: e-Monev Bappenas. Visualisasi: target vs realisasi per program, traffic light, drill-down per unit kerja."

### UC-58 🏢 Enterprise: Medallion Lakehouse Implementation
- **Who**: ER + DM + DAMA + PA
- **What**: Implementasi data lakehouse dengan arsitektur medallion (Bronze→Silver→Gold)
- **When**: Enterprise butuh data platform scalable dari nol atau modernisasi DWH | Timeline: 3-6 bulan
- **Skills**: ER(system-design: Databricks/Snowflake + Delta Lake/Iceberg) + DM(architecture-blueprint: medallion layers) + DAMA(KA-02 architecture, KA-08 DW/BI) + PA(metric-definition: data quality per layer)
- **Complexity**: L3
- **Prompt**: "Desain medallion lakehouse. Cloud: [GCP/AWS/Azure]. Sources: [list]. Bronze: raw CDC ingestion. Silver: 3NF/Data Vault conformed. Gold: star schema marts. Include: dbt project structure (staging→intermediate→marts), DataOps CI/CD."

### UC-59 🏢 Enterprise: Data Catalog & Governance Setup
- **Who**: DM + DAMA + ER
- **What**: Implementasi data catalog + business glossary + lineage
- **When**: Enterprise dengan >50 data sources tanpa metadata management | Timeline: 2-4 bulan
- **Skills**: DM(catalog-evaluation: OpenMetadata vs DataHub vs Atlan) + DAMA(KA-09 metadata, KA-01 governance) + ER(system-design: deployment + integration)
- **Complexity**: L3
- **Prompt**: "Implementasi data catalog untuk [perusahaan]. Stack: [Snowflake/Databricks] + dbt. Evaluate: OpenMetadata vs DataHub. Include: business glossary (50 key terms), column-level lineage, data quality profiling, access policies."

### UC-60 🏢 Enterprise: Real-Time Analytics Architecture
- **Who**: ER + PA + DM
- **What**: Streaming analytics pipeline (Kappa architecture: Kafka + Flink + serving layer)
- **When**: Perusahaan butuh real-time decisioning (<100ms latency) | Timeline: 3-6 bulan
- **Skills**: ER(system-design: Kappa arch + CDC + Flink) + PA(metric-definition: real-time KPIs) + DM(data-strategy: streaming data quality)
- **Complexity**: L4
- **Prompt**: "Desain real-time analytics. Use case: [fraud detection/personalization/monitoring]. Architecture: source → CDC (Debezium) → Kafka → Flink processing → Redis feature store → serving. Include: latency SLA, data quality checks, fallback to batch."
