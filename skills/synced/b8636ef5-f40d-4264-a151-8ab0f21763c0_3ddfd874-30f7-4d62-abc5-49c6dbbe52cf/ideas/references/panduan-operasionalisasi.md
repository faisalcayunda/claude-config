# Panduan Operasionalisasi Project / Project Operations Guide
# 20 Panduan Lengkap dengan 5W1H + Contoh / 20 Complete Guides with 5W1H + Examples

> Dibangun dari: PMBOK 7 (12 principles), Stage-Gate (Cooper), McKinsey TEAM FOCUS, SAFe 6.0, Federal Data Strategy Playbook, UK GDS Service Manual, dan 400+ sumber riset.

---

## PANDUAN 1: Product Development — Membangun Produk Digital Baru

### 5W1H
- **What**: Membangun produk digital dari ide hingga launch / Build digital product from idea to launch
- **Who**: PM, BA, ER, PA, UXR, PDS | Tim: 5-12 orang
- **When**: Ada kebutuhan produk baru atau fitur major | Timeline: 3-12 bulan
- **Where**: Semua 10 skill terlibat, dimulai dari discovery
- **Why**: Memastikan produk dibangun berdasarkan evidence (Cagan: EMPOWERED)
- **How**: Stage-Gate 5 fase + Dual-Track Agile (discovery || delivery)

### Langkah (Gate-based)
1. **GATE 0 — Kickoff**: `/ideas` → project-context-canvas (SSOT) + skill-selection-guide
2. **FASE 1 — Discover**: `/product-researcher` → research-plan + interview-guide + market-sizing | `/product-manager` → product-brief + persona | `/ux-researcher` → competitive-ux + card-sort
3. **GATE 1 Review**: Problem validated? Evidence ≥ Gilad Confidence 1.0?
4. **FASE 2 — Define**: `/business-analyst` → brd + srs + use-case + rtm | `/product-analyst` → tracking-plan + metric-definition | `/engineering-researcher` → system-design + adr
5. **GATE 2 Review**: Requirements complete? Architecture approved?
6. **FASE 3 — Build**: `/product-delivery-specialist` → sprint-plan + release-plan | `/engineering-researcher` → test-strategy + runbook | `/ux-researcher` → usability-test-plan
7. **GATE 3 Review**: Quality gates passed? Launch criteria met?
8. **FASE 4 — Launch**: `/product-delivery-specialist` → gtm-launch + positioning + launch-readiness + sales-enablement | `/product-analyst` → health-scorecard
9. **GATE 4 Review**: Launch metrics on target?
10. **FASE 5 — Optimize**: `/product-manager` → product-review | `/product-analyst` → cohort-retention + funnel-analysis + ab-test-report | `/product-delivery-specialist` → retrospective

### Contoh Prompt
```
Saya ingin membangun platform data analytics untuk pemerintah daerah.
Target: Kepala OPD dan analis data. Budget: Rp 2M. Timeline: 6 bulan.
Bantu saya mulai dari project context canvas hingga launch plan.
```

---

## PANDUAN 2: Data Governance Implementation — Implementasi Tata Kelola Data

### 5W1H
- **What**: Framework tata kelola data organisasi (DAMA-DMBOK2 aligned)
- **Who**: DM, DAMA, BA, ER, PDS | CDO/CIO sebagai sponsor
- **When**: Organisasi belum punya DG atau perlu upgrade | Timeline: 6-24 bulan
- **Where**: `/data-management-researcher` + `/dama-research` + `/business-analyst` + `/product-delivery-specialist`
- **Why**: Kepatuhan regulasi (UU PDP, SPBE), kualitas data, trust in data. Gartner: 80% DG initiatives fail tanpa business crisis. DBS Bank: compressed AI time-to-value 12mo → 2-3mo melalui Data Chapter 700 orang embedded di squads
- **How**: 5-phase consulting arc: Assess → Strategy → Quick Wins → Scale → Sustain

### Langkah (5-Phase Consulting Arc + CDO Playbook)
1. **Phase 1 — Assess (4-8 minggu)**: `/dama-research` → KA-14 maturity + tools/maturity-calculator.py | `/data-management-researcher` → maturity-assessment (CMMI-DMM/DCAM)
2. **Phase 2 — Strategy & Roadmap (4-6 minggu)**: `/data-management-researcher` → data-strategy | `/dama-research` → KA-01 governance charter | `/business-analyst` → stakeholder + raci
3. **Phase 3 — Quick Wins / Pilot (6-12 minggu)**: Pilih 1-2 domain high-impact. `/dama-research` → KA-11 quality + KA-09 metadata (business glossary). `/product-delivery-specialist` → sprint-plan
4. **Phase 4 — Scale (3-12 bulan)**: `/data-management-researcher` → architecture-blueprint | `/dama-research` → KA-02 + KA-10 MDM | `/data-management-researcher` → mdm-strategy + catalog-evaluation | `/engineering-researcher` → system-design (tooling)
5. **Phase 5 — Sustain (ongoing)**: `/product-analyst` → health-scorecard (governance KPIs) | `/data-management-researcher` → maturity re-assessment | `/product-delivery-specialist` → change-management (ADKAR)

### Governance Structure (3-Tier)
- **Data Governance Council** (strategic): sponsor decisions, cross-department. Meet monthly
- **Data Management Office** (operational): standards, coordination. Meet weekly
- **Domain Data Stewards** (execution): day-to-day quality per domain. Embedded in business

### Case Studies (Round 6 Research)
- **DBS Bank**: Data Chapter 700 orang embedded in squads (bukan siloed). PURE Framework: Purposeful, Unsurprising, Respectful, Explainable. AI time-to-value 12-15mo → 2-3mo
- **JPMorgan Chase**: Federated data mesh. Common taxonomy critical — "it took extensive debate to define what a transaction means across lines of business"
- **Bank Mandiri**: Consolidated 50+ legacy systems → single data lake. Monthly Tableau User Group with volunteer coaches. Won "Data Governance Initiative of the Year"

### Contoh Prompt
```
Organisasi kami (Dinas Kominfo Kab. Bandung) ingin membangun framework tata kelola data
sesuai SPBE dan Satu Data Indonesia. Maturity level saat ini belum diketahui.
Bantu saya mulai dari assessment hingga implementation plan.
Gunakan 5-phase consulting arc: Assess → Strategy → Quick Wins → Scale → Sustain.
```

---

## PANDUAN 3: SPBE Digital Transformation — Transformasi Digital Pemerintah

### 5W1H
- **What**: Meningkatkan skor SPBE instansi (Perpres 95/2018, diperkuat Perpres 132/2022)
- **Who**: IDEAS + DM + DAMA + BA + PDS | Sponsor: Sekda/Kadis
- **When**: Menjelang evaluasi SPBE atau inisiatif transformasi | Timeline: 6-18 bulan
- **Where**: `/ideas-company` + `/dama-research` + `/data-management-researcher` + `/business-analyst` + `/product-delivery-specialist`
- **Why**: 47 indikator evaluasi across 4 domain. Indeks SPBE nasional 2024: 3.12/5 (predikat "Baik"). Top: Kemenkomdigi 4.75, Jateng 4.26, Kota Bandung 4.59. UN e-Gov ranking Indonesia: #64/193 (2024)
- **How**: Baseline SPBE → Gap analysis per domain → Roadmap → Implement → Evaluasi

### Konteks Regulasi (Round 5 Research)
- **4 Domain SPBE**: Kebijakan (10 indikator, 13%), Tata Kelola (10 indikator, 25%), Manajemen (11 indikator, 16%), Layanan (16 indikator, 25%)
- **5-Level Maturity**: Rintisan → Terkelola → Terstandarisasi → Terintegrasi → Optimum
- **Satu Data Indonesia (Perpres 39/2019)**: Roles: Walidata (data steward), Produsen Data (data producer), Pembina Data (BPS/BIG). Portal data.go.id: 453,000+ datasets
- **INA Digital**: Konsolidasi ~27,000 aplikasi pemerintah ke portal terpadu. Moratorium pembangunan app baru
- **UU PDP (UU 27/2022)**: Efektif 17 Okt 2024. Breach notification 3×24 jam. Sanksi 2% revenue. Catatan: PP pelaksana dan Lembaga PDP belum terbentuk per April 2026
- **Perpres 46/2025**: Pengadaan IT — prinsip Cepat, Akuntabel, Berbasis Data. e-Katalog prioritas utama

### Langkah
1. **SPBE Baseline**: `/ideas-company` → references/spbe-evaluation-framework.md + scripts/query_spbe.py (cek skor instansi)
2. **Gap Analysis**: `/business-analyst` → gap-analysis (current vs target per 47 indikator, 4 domain)
3. **SDI Alignment**: Cek status Walidata, Produsen Data, interoperabilitas data.go.id
4. **DAMA-SPBE Alignment**: `/dama-research` → references/dama-integration-map.md (mapping KA ke indikator SPBE)
5. **Architecture**: `/data-management-researcher` → architecture-blueprint (arsitektur 5 layer SPBE)
6. **UU PDP Compliance**: `/data-management-researcher` → pia + `/dama-research` → KA-05, KA-12
7. **Policy**: `/ideas-company` → templates/policy-framework-template
8. **Change Management**: `/product-delivery-specialist` → change-management (ADKAR — adaptasi untuk budaya birokrasi: approval hierarkis, rotasi pimpinan, risiko ego sektoral)
9. **Roadmap**: `/product-delivery-specialist` → release-plan
10. **Proposal LKPP**: `/ideas-company` → templates/technical-proposal-template (format Dokumen Seleksi LKPP: Tanggapan KAK, Pendekatan Metodologi, Komposisi Tim, Jadwal, CV Tenaga Ahli)
11. **Pricing**: `/ideas-company` → scripts/estimate_service_cost.py (HPS: billing rate INKINDO + SBM PMK 32/2025)

### Contoh Prompt
```
Dinas Kominfo Provinsi Jawa Barat ingin meningkatkan skor SPBE dari 2.8 ke 3.5.
Buatkan: (1) gap analysis per 4 domain SPBE (47 indikator), (2) roadmap 18 bulan,
(3) alignment dengan Satu Data Indonesia, (4) UU PDP compliance check,
(5) technical proposal format LKPP. Sertakan estimasi HPS.
```

---

## PANDUAN 4: Enterprise Product Analytics Setup

### 5W1H
- **What**: Infrastruktur analytics produk dari nol / Analytics stack setup
- **Who**: PA, ER, PM | Data Engineer sebagai pelaksana
- **When**: Produk baru atau existing tanpa analytics | Timeline: 2-4 bulan
- **Where**: `/product-analyst` + `/engineering-researcher` + `/product-manager`
- **Why**: Data-driven decisions, mengukur PMF (HEART/AARRR framework)
- **How**: Define metrics → Instrument → Analyze → Experiment → Iterate

### Langkah
1. **North Star + OKR**: `/product-manager` → okr + metrics-dashboard
2. **Metric Framework**: `/product-analyst` → metric-definition (HEART: Happiness/Engagement/Adoption/Retention/Task Success)
3. **Data Taxonomy**: `/product-analyst` → data-taxonomy (naming conventions, entity definitions)
4. **Tracking Plan**: `/product-analyst` → tracking-plan (events, properties, triggers)
5. **Data Pipeline**: `/engineering-researcher` → system-design (analytics architecture)
6. **Dashboard**: `/product-analyst` → saas-dashboard + health-scorecard
7. **Experimentation**: `/product-analyst` → experiment-design + sample-size
8. **Data Story**: `/product-analyst` → data-story + analytics-brief

---

## PANDUAN 5: Competitive Intelligence & Market Entry

### 5W1H
- **What**: Riset kompetitor dan strategi masuk pasar
- **Who**: PR, PM, UXR, PDS
- **When**: Sebelum launch atau masuk segmen baru | Timeline: 4-8 minggu
- **Where**: `/product-researcher` + `/product-manager` + `/ux-researcher` + `/product-delivery-specialist`
- **Why**: Mengurangi risiko kegagalan, positioning yang tepat (Dunford: Obviously Awesome)
- **How**: Research → Analyze → Position → Launch

### Langkah
1. **Market Sizing**: `/product-researcher` → market-sizing (TAM/SAM/SOM)
2. **Competitive Deep**: `/product-researcher` → competitive-deep
3. **Competitive UX**: `/ux-researcher` → competitive-ux
4. **Trend Analysis**: `/product-researcher` → trend-analysis
5. **Pricing Research**: `/product-researcher` → pricing-research
6. **Positioning**: `/product-delivery-specialist` → positioning (Dunford 10-step)
7. **GTM Plan**: `/product-delivery-specialist` → gtm-launch
8. **Sales Tools**: `/product-delivery-specialist` → battlecard + sales-enablement

---

## PANDUAN 6: Requirements Engineering — Rekayasa Kebutuhan

### 5W1H
- **What**: Capture, analyze, document requirements (BABOK v3 + IEEE 29148)
- **Who**: BA, PM, ER | Stakeholders sebagai source
- **When**: Setelah discovery, sebelum development | Timeline: 2-6 minggu
- **How**: Elicit → Analyze → Specify → Validate → Manage (BABOK 4-task elicitation)

### Langkah
1. **Stakeholder**: `/business-analyst` → stakeholder + raci
2. **Business Req**: `/business-analyst` → brd
3. **Product Req**: `/product-manager` → prd + feature-spec
4. **System Req**: `/business-analyst` → srs + frs + nfr
5. **Use Cases**: `/business-analyst` → use-case + user-story-bdd
6. **Traceability**: `/business-analyst` → rtm
7. **Architecture**: `/engineering-researcher` → adr + technical-rfc
8. **Acceptance**: `/business-analyst` → uat-plan + business-rules

---

## PANDUAN 7: UX Research Program

### 5W1H
- **What**: Program riset UX sistematis (NNGroup + Maze REFINE framework)
- **Who**: UXR, PR, PM
- **When**: Setiap cycle development
- **How**: Plan → Recruit → Test → Analyze → Recommend → Validate

### Langkah
1. **Research Plan**: `/product-researcher` → research-plan
2. **Interview Guide**: `/product-researcher` → interview-guide (Mom Test principles)
3. **Usability Test**: `/ux-researcher` → usability-test-plan → usability-test-report
4. **Heuristic Eval**: `/ux-researcher` → heuristic-eval (Nielsen 10 heuristics)
5. **Accessibility**: `/ux-researcher` → accessibility-audit (WCAG 2.1 AA)
6. **UX Findings**: `/ux-researcher` → ux-findings + design-recommendation
7. **IA Assessment**: `/ux-researcher` → ia-assessment + card-sort
8. **Persona Update**: `/product-researcher` → research-persona

---

## PANDUAN 8: Technical Architecture & Engineering

### 5W1H
- **What**: Merancang arsitektur teknis (C4 model, ADR, API design)
- **Who**: ER, DM, BA
- **When**: Awal project atau refactoring besar
- **How**: Design → Decide → Document → Review → Implement

### Langkah
1. `/engineering-researcher` → system-design (Google design doc format)
2. `/engineering-researcher` → adr (MADR format, "yes, if" review — Squarespace)
3. `/data-management-researcher` → architecture-blueprint
4. `/engineering-researcher` → api-design (OpenAPI 3.1)
5. `/engineering-researcher` → tech-radar (Adopt/Trial/Assess/Hold)
6. `/engineering-researcher` → test-strategy
7. `/engineering-researcher` → threat-model (STRIDE)
8. `/engineering-researcher` → runbook + performance-benchmark

---

## PANDUAN 9: Agile Delivery & Scrum

### 5W1H
- **What**: Setup dan eksekusi agile delivery (Scrum/Kanban/SAFe)
- **Who**: PDS (lead), PM, BA, ER, PA | Scrum Master / RTE sebagai facilitator
- **When**: Setiap project yang menggunakan iterative delivery | Timeline: ongoing per sprint/PI
- **Where**: `/product-delivery-specialist` + cross-skill support
- **Why**: Faster feedback loops, adaptability, measurable delivery (DORA metrics)
- **How**: Setup → Plan → Execute → Review → Retro → Improve

### Langkah
1. **Team Setup**: `/product-delivery-specialist` → team-agreement (DoD, DoR, working norms)
2. **Sprint Planning**: `/product-delivery-specialist` → sprint-plan (capacity-based). Cross-functional: PM frames goal, BA provides stories, ER judges feasibility, UXR confirms UX alignment
3. **Release Planning**: `/product-delivery-specialist` → release-plan (phased rollout)
4. **PI Planning (SAFe)**: `/product-delivery-specialist` → pi-planning (8-12 week PI, 50-125 people per ART)
5. **DORA Monitoring**: `/product-delivery-specialist` → dora-dashboard (Deployment Frequency, Lead Time, Change Failure Rate, MTTR)
6. **Retrospective**: `/product-delivery-specialist` → retrospective (4Ls format, max 3 action items per retro)
7. **Maturity Assessment**: `/product-delivery-specialist` → agile-maturity
8. **Value Stream**: `/product-delivery-specialist` → vsm (map happy path + recovery stream)

### SAFe PI Planning Real-World Insights (Round 6)
- **50% of work discovered DURING planning** — bukan sebelumnya. Plan for emergence.
- **Confidence vote**: Tim menilai feasibility tim LAIN, bukan diri sendiri — "I'm worried about you, you have work planned until end of PI"
- **Banking PI**: 8-team, 105-person replatform, 4 timezones. Intense coordination creates trust between siloed teams
- **Anti-pattern**: Beware "Lean Waterfall" — setiap skill agile sendiri tapi antar skill tetap sequential

### Contoh Prompt
```
Setup agile delivery untuk project [nama]. Tim: [N] orang, [roles].
Methodology: [Scrum/Kanban/SAFe]. Sprint: [2w]. Buatkan team agreement + sprint plan Sprint 1.
Include DORA baseline metrics dan retrospective format.
```

---

## PANDUAN 10: IDEAS Proposal & Pitch
### Langkah
1. `/ideas-company` → scripts/recommend_service.py
2. `/ideas-company` → scripts/estimate_service_cost.py
3. `/ideas-company` → templates/technical-proposal-template
4. `/ideas-company` → templates/business-proposal-template
5. `/ideas-company` → templates/pitch-deck-template
6. `/ideas-company` → templates/surat-penawaran-template
7. `/ideas-company` → templates/boq-template
8. `/ideas-company` → references/competitive-landscape.md

---

## PANDUAN 11: Data Mesh & Modern Data Architecture

### 5W1H
- **What**: Transisi ke arsitektur data modern (mesh/fabric/lakehouse)
- **Who**: DM, DAMA, ER | Data Architect sebagai lead
- **When**: Organisasi sudah punya data platform tapi silos berkembang | Timeline: 6-12 bulan
- **Where**: `/data-management-researcher` + `/dama-research` + `/engineering-researcher`
- **Why**: Scalability, domain ownership, self-serve analytics (Dehghani: Data Mesh)
- **How**: Assess readiness → Define domains → Design architecture → Implement → Monitor

### Langkah
1. **Readiness**: `/data-management-researcher` → mesh-readiness (4 pillars: domain ownership, data as product, self-serve platform, federated governance)
2. **Concepts**: `/dama-research` → references/concepts-modern-paradigms.md (Data Mesh, Fabric, Lakehouse comparison)
3. **Domain Design**: `/data-management-researcher` → data-product-canvas (per domain: sources, SLOs, consumers, schema)
4. **Architecture**: `/data-management-researcher` → architecture-blueprint + `/engineering-researcher` → system-design
5. **Standards**: `/data-management-researcher` → standards-mapping + fair-assessment
6. **ADR**: `/engineering-researcher` → adr (mesh vs monolith decision)
7. **Implementation**: `/product-delivery-specialist` → sprint-plan + release-plan

### Contoh Prompt
```
Organisasi kami punya 5 domain bisnis, masing-masing punya data silo.
Evaluasi kesiapan kami untuk data mesh. Platform saat ini: Snowflake + dbt.
```

---

## PANDUAN 12: Post-Launch Optimization

### 5W1H
- **What**: Optimasi produk setelah launch berdasarkan data real
- **Who**: PA, PM, UXR, PDS | Product trio sebagai core
- **When**: T+2w setelah launch, lalu quarterly | Timeline: ongoing
- **Where**: `/product-analyst` + `/product-manager` + `/ux-researcher` + `/product-delivery-specialist`
- **Why**: Data-driven iteration, reduce churn, increase engagement
- **How**: Measure → Analyze → Hypothesize → Test → Implement → Repeat

### Langkah
1. **Health Check**: `/product-analyst` → health-scorecard (AARRR: Acquisition/Activation/Retention/Revenue/Referral)
2. **Funnel Deep-Dive**: `/product-analyst` → funnel-analysis (identify biggest drop-off)
3. **Cohort Analysis**: `/product-analyst` → cohort-retention (D1/D7/D30/D90)
4. **Feature Adoption**: `/product-analyst` → feature-adoption (per-feature usage metrics)
5. **Usability Issues**: `/ux-researcher` → usability-test-report (top 5 usability issues)
6. **Experiment**: `/product-analyst` → experiment-design + sample-size → ab-test-report
7. **Product Review**: `/product-manager` → product-review (quarterly)
8. **Growth Plan**: `/product-delivery-specialist` → growth-dashboard + retrospective

### Contoh Prompt
```
Produk kami sudah launch 4 minggu. DAU: 500, D7 retention: 25%, activation rate: 40%.
Analisis funnel, identifikasi bottleneck terbesar, dan desain 3 eksperimen untuk improve.
```

---

## PANDUAN 13: Incident Management & Postmortem

### 5W1H
- **What**: Manajemen insiden dan blameless postmortem (Google SRE style)
- **Who**: ER, BA, PDS | Incident Commander sebagai lead
- **When**: Setelah setiap P0/P1 incident | Timeline: 24-72 jam post-incident
- **Where**: `/engineering-researcher` + `/business-analyst` + `/product-delivery-specialist`
- **Why**: Prevent recurrence, improve system reliability, organizational learning
- **How**: Contain → Diagnose → Fix → Postmortem → Systemic improvement

### Langkah
1. **Postmortem**: `/engineering-researcher` → postmortem (Google SRE format: timeline, root cause, impact, action items)
2. **Root Cause**: `/business-analyst` → rca (5-Why + Fishbone)
3. **Impact Analysis**: `/business-analyst` → impact-analysis (users affected, revenue impact, SLA breach)
4. **Runbook Update**: `/engineering-researcher` → runbook (update with new failure mode)
5. **Retrospective**: `/product-delivery-specialist` → retrospective (team reflection, systemic fixes)

### Contoh Prompt
```
Kemarin database production down selama 45 menit. 2000 users terdampak.
Root cause: disk full karena log rotation gagal. Buatkan postmortem blameless + action items.
```

---

## PANDUAN 14: Privacy & Compliance (UU PDP / GDPR)

### 5W1H
- **What**: Privacy impact assessment + compliance framework
- **Who**: DM, DAMA, ER, BA | DPO/Legal sebagai advisor
- **When**: Sebelum launch fitur yang mengolah data pribadi | Timeline: 2-4 minggu
- **Where**: `/data-management-researcher` + `/dama-research` + `/engineering-researcher` + `/business-analyst`
- **Why**: Kepatuhan UU PDP (UU 27/2022), GDPR, reputasi, denda hingga 2% revenue
- **How**: Assess → Design → Implement → Audit → Monitor

### Langkah
1. **PIA**: `/data-management-researcher` → pia (Privacy Impact Assessment)
2. **Standards**: `/data-management-researcher` → standards-mapping (UU PDP vs GDPR vs sector-specific)
3. **Security**: `/dama-research` → KA-05 (data security templates)
4. **Ethics**: `/dama-research` → KA-12 (data handling ethics)
5. **Threat Model**: `/engineering-researcher` → threat-model (STRIDE: identify privacy threats)
6. **NFR**: `/business-analyst` → nfr (privacy & security requirements)

### Contoh Prompt
```
Fitur baru kami mengumpulkan data lokasi real-time pengguna.
Lakukan PIA berdasarkan UU PDP Indonesia. Identifikasi risiko dan mitigasi.
```

---

## PANDUAN 15: Strategic Planning & OKR Cascade

### 5W1H
- **What**: Perencanaan strategi produk + OKR cascade (company → team → individual)
- **Who**: PM, PR, PDS | CEO/CPO sebagai sponsor
- **When**: Quarterly atau annual planning | Timeline: 2-4 minggu
- **Where**: `/product-manager` + `/product-researcher` + `/product-delivery-specialist` + `/ideas-company`
- **Why**: Alignment, focus, measurable outcomes (Doerr: Measure What Matters)
- **How**: Vision → Strategy → OKR → Roadmap → Execute → Review

### Langkah
1. **Market Context**: `/product-researcher` → market-sizing + trend-analysis
2. **Vision**: `/product-manager` → product-brief (vision + strategy)
3. **OKR**: `/product-manager` → okr (2-3 Objectives, 3-4 KRs each, confidence levels)
4. **Roadmap**: `/product-manager` → roadmap (NOW/NEXT/LATER aligned to OKRs)
5. **Pricing**: `/product-manager` → pricing-strategy (jika ada revenue OKR)
6. **Change**: `/product-delivery-specialist` → change-management (rollout OKR ke seluruh tim)
7. **Frameworks**: `/ideas-company` → references/business-frameworks.md (BMC, BSC, Porter)

### Contoh Prompt
```
Annual planning 2027. Produk SaaS data analytics. Current ARR: $500K. Target: $1.2M.
Buatkan OKR cascade dari company level ke product team level, plus roadmap aligned.
```

---

## PANDUAN 16: Platform Migration

### 5W1H
- **What**: Migrasi platform/sistem (legacy → modern, on-prem → cloud)
- **Who**: ER, BA, DM, PDS | Tech Lead sebagai architect
- **When**: EOL system, scalability issues, cost optimization | Timeline: 3-12 bulan
- **Where**: `/engineering-researcher` + `/business-analyst` + `/data-management-researcher` + `/product-delivery-specialist`
- **Why**: Technical debt reduction, maintainability, performance, cost
- **How**: Assess → Plan → Execute (strangler fig pattern) → Validate → Cutover

### Langkah
1. **Current Architecture**: `/engineering-researcher` → architecture-review + system-design
2. **ADR**: `/engineering-researcher` → adr (migration strategy: lift-shift, re-platform, re-architect)
3. **Gap Analysis**: `/business-analyst` → gap-analysis + impact-analysis
4. **Requirements**: `/business-analyst` → srs (target system requirements)
5. **Data Migration**: `/data-management-researcher` → architecture-blueprint (data migration plan)
6. **Release Plan**: `/product-delivery-specialist` → release-plan (phased cutover strategy)
7. **Change Mgmt**: `/product-delivery-specialist` → change-management (user migration communication)

### Contoh Prompt
```
Kami migrasi dari on-prem Oracle DB + monolith Java ke AWS + microservices.
500GB data, 50 API endpoints. Buatkan migration ADR + phased release plan.
```

---

## PANDUAN 17: Product-Led Growth (PLG)

### 5W1H
- **What**: Strategi pertumbuhan berbasis produk (self-serve, freemium, viral loops)
- **Who**: PM, PA, PR, UXR, PDS | Growth team sebagai core
- **When**: Post-PMF, siap scale | Timeline: 6-12 bulan continuous
- **Where**: `/product-manager` + `/product-analyst` + `/product-researcher` + `/ux-researcher` + `/product-delivery-specialist`
- **Why**: Lower CAC, higher LTV, scalable growth (Wes Bush: Product-Led Growth)
- **How**: PMF → Onboarding optimization → Activation → Expansion → Virality

### Langkah
1. **PMF Check**: `/product-researcher` → pmf-analysis (Sean Ellis: >40% very disappointed) + survey-design
2. **Pricing**: `/product-manager` → pricing-strategy (freemium/free trial/reverse trial model)
3. **Personas**: `/product-manager` → persona + journey-map (PLG-specific: self-serve flow)
4. **Analytics**: `/product-analyst` → tracking-plan + funnel-analysis + experiment-design
5. **Onboarding UX**: `/ux-researcher` → usability-test-plan + prototype-test (time-to-value optimization)
6. **Growth Metrics**: `/product-delivery-specialist` → growth-dashboard + onboarding-playbook
7. **Experiment Cadence**: `/product-analyst` → experiment-design → ab-test-report (weekly experiment cycle)

### Contoh Prompt
```
SaaS produk kami punya free tier (1000 users) dan Pro tier ($49/mo, 200 paying).
Conversion rate free→paid: 3%. Target: 8%. Buatkan PLG strategy + experiment backlog.
```

---

## PANDUAN 18: Enterprise Data Quality Program

### 5W1H
- **What**: Program DQ sistematis (measure → improve → monitor 6 dimensi)
- **Who**: DAMA, DM, PA, BA | Data Quality Manager sebagai lead
- **When**: Data-driven decisions diperlukan tapi data unreliable | Timeline: 3-12 bulan
- **Where**: `/dama-research` + `/data-management-researcher` + `/product-analyst` + `/business-analyst`
- **Why**: "Garbage in, garbage out" — compliance, trust, operational efficiency
- **How**: Profile → Assess → Cleanse → Monitor → Govern (DAMA KA-11 lifecycle)

### Langkah
1. **Framework**: `/dama-research` → KA-11 templates (12 deliverables: DQ strategy, rules, metrics, dashboard)
2. **Comparison**: `/data-management-researcher` → dq-framework-comparison (ISO 8000 vs DAMA vs DCAM)
3. **Metrics**: `/product-analyst` → metric-definition (6 dimensi: accuracy, completeness, consistency, timeliness, validity, uniqueness)
4. **Dashboard**: `/product-analyst` → health-scorecard (DQ scorecard per domain/entity)
5. **Root Cause**: `/business-analyst` → rca (why DQ issues occur) + business-rules (enforcement rules)
6. **Governance**: `/dama-research` → KA-01 (governance overlay for DQ program)

### Contoh Prompt
```
Database pelanggan kami punya 30% duplicate records dan 15% alamat invalid.
Buatkan DQ program: profiling → cleansing → monitoring. 6 dimensi kualitas.
```

---

## PANDUAN 19: Metadata & Data Catalog Implementation

### 5W1H
- **What**: Implementasi metadata management + data catalog enterprise
- **Who**: DAMA, DM, ER | Metadata Manager sebagai lead
- **When**: Organisasi punya >50 data assets tanpa discoverability | Timeline: 3-6 bulan
- **Where**: `/dama-research` + `/data-management-researcher` + `/engineering-researcher`
- **Why**: Data discoverability, lineage tracking, governance enforcement, self-serve analytics
- **How**: Inventory → Classify → Catalog → Automate → Govern

### Langkah
1. **Framework**: `/dama-research` → KA-09 templates (11 deliverables: metadata strategy, standards, catalog design)
2. **Tool Selection**: `/data-management-researcher` → catalog-evaluation + tool-landscape (Atlan vs Collibra vs DataHub vs OpenMetadata)
3. **Architecture**: `/engineering-researcher` → system-design (catalog architecture, integration points)
4. **Implementation**: `/product-delivery-specialist` → sprint-plan

### Contoh Prompt
```
Kami punya 200+ tabel di 3 databases tanpa dokumentasi. Tim data sering kesulitan
menemukan data yang tepat. Buatkan metadata strategy + evaluasi 3 catalog tools.
```

---

## PANDUAN 20: Team Onboarding & Knowledge Transfer

### 5W1H
- **What**: Onboarding anggota tim baru + transfer knowledge dari outgoing member
- **Who**: PDS, IDEAS, BA | Team Lead sebagai facilitator
- **When**: New hire, team rotation, project handover | Timeline: 2-4 minggu
- **Where**: `/product-delivery-specialist` + `/ideas-company` + `/business-analyst`
- **Why**: Reduce time-to-productivity, prevent knowledge loss, team continuity
- **How**: Prepare → Orient → Train → Mentor → Validate (30-60-90 day plan)

### Langkah
1. **Onboarding Plan**: `/product-delivery-specialist` → onboarding-playbook (30-60-90 day milestones)
2. **Team Agreement**: `/product-delivery-specialist` → team-agreement (DoD, DoR, norms, tools)
3. **KT Document**: `/ideas-company` → templates/knowledge-transfer-template (system knowledge, contacts, runbooks)
4. **Training Material**: `/ideas-company` → templates/training-material-template
5. **RACI Update**: `/business-analyst` → raci (update roles setelah perubahan tim)

### Contoh Prompt
```
Data engineer senior kami resign bulan depan. Dia pegang 3 critical pipelines.
Buatkan knowledge transfer plan + onboarding guide untuk penggantinya.
```

---

## PANDUAN 21: Banking Data Governance & Compliance (Vertikal Perbankan)

### 5W1H
- **What**: Data governance untuk bank sesuai regulasi OJK + BCBS 239 + UU PDP
- **Who**: DAMA, DM, BA, ER, IDEAS | CDO/CIO bank sebagai sponsor
- **When**: Saat bank butuh compliance POJK, modernisasi core banking, atau setup AML | Timeline: 6-18 bulan
- **Where**: `/dama-research` + `/data-management-researcher` + `/engineering-researcher` + `/ideas-company` + `/business-analyst`
- **Why**: OJK mandates (POJK 11/2022 cybersecurity maturity, POJK 15/2024 internal control). BCBS 239: hanya 2/31 G-SIBs fully compliant. SLIK covers 96.4M debtors
- **How**: Regulatory mapping → Maturity assessment → Gap analysis → Architecture → Implementation → Monitoring

### Langkah
1. **Regulatory Mapping**: `/ideas-company` → map POJK 11/2022, POJK 21/2023, BCBS 239, UU PDP ke data requirements
2. **DMAB Assessment**: `/dama-research` → KA-14 maturity + DMAB (Digital Maturity Assessment for Banks) per SEOJK 24/2023
3. **Gap Analysis**: `/business-analyst` → gap-analysis (current vs BCBS 239 14 principles)
4. **AML Architecture**: `/engineering-researcher` → system-design (graph DB: Neo4j/TigerGraph + Kafka streaming + feature store)
5. **Data Quality for Regulatory Reporting**: `/dama-research` → KA-11 (LBUT/LBU/LHBU accuracy requirements)
6. **SNAP API Integration**: `/engineering-researcher` → api-design (SNAP standard per BI Decree 23/10/2021)
7. **Credit Scoring Pipeline**: `/engineering-researcher` → system-design (SLIK integration + alternative data sources)
8. **UU PDP Compliance**: `/data-management-researcher` → pia + `/dama-research` → KA-05, KA-12
9. **Implementation**: `/product-delivery-specialist` → sprint-plan + change-management (ADKAR for bank culture)
10. **Proposal**: `/ideas-company` → technical-proposal (LKPP format jika BUMN, enterprise format jika swasta)

### Contoh Prompt
```
Bank regional (BUKU 3) butuh compliance POJK 11/2022 + BCBS 239.
Saat ini belum punya data governance formal. Core banking: Temenos T24.
Buatkan: (1) BCBS 239 gap analysis, (2) data governance roadmap 12 bulan,
(3) AML architecture design, (4) SNAP API integration plan, (5) HPS/RAB.
```

---

## PANDUAN 22: Government Digital Platform & SPBE (Vertikal Pemerintah)

### 5W1H
- **What**: Platform data pemerintah: open data portal, interoperabilitas, dashboard kinerja
- **Who**: DAMA, DM, ER, BA, PDS, IDEAS | Sekda/Kadis Kominfo sebagai sponsor
- **When**: Menjelang evaluasi SPBE, inisiatif smart city, atau mandate SDI | Timeline: 6-24 bulan
- **Where**: `/dama-research` + `/data-management-researcher` + `/engineering-researcher` + `/business-analyst` + `/product-delivery-specialist` + `/ideas-company`
- **Why**: 59% instansi masih di bawah level SPBE adequate. UN EGDI Indonesia naik ke #64. INA Digital consolidating 27,000 apps
- **How**: SPBE baseline → Architecture design → Platform build → Integration → Capacity building

### Langkah
1. **SPBE Baseline**: `/ideas-company` → scripts/query_spbe.py + gap analysis per 47 indikator (lihat Panduan 3)
2. **Benchmark International**: Bandingkan dengan Estonia X-Road (929 institutions, 1,887 systems), Singapore CODEX/SGTS
3. **Open Data Portal**: `/engineering-researcher` → system-design (CKAN deployment + SDI metadata compliance per Perpres 39/2019)
4. **Interoperability Layer**: `/engineering-researcher` → system-design (API gateway, data exchange platform inspired by X-Road once-only principle)
5. **Dashboard Kinerja**: `/product-analyst` → analytics-dashboard aligned to SAKIP/e-Monev hierarchy (K1-K8)
6. **Smart City Platform**: `/engineering-researcher` → system-design (IoT data lake + citizen app integration, reference: Jakarta JAKI)
7. **Data Governance SDI**: `/dama-research` → KA-01 governance charter + `/data-management-researcher` → data-strategy (Walidata/Produsen Data roles)
8. **Change Management**: `/product-delivery-specialist` → change-management (ADKAR adapted for birokrasi: approval hierarkis, rotasi pejabat)
9. **Capacity Building**: `/product-delivery-specialist` → training-plan (ToT model for sustainability)
10. **Proposal LKPP**: `/ideas-company` → technical-proposal (Dokumen Seleksi format, HPS per INKINDO rates)

### Contoh Prompt
```
Pemerintah Kota [nama] ingin membangun smart city data platform.
Skor SPBE saat ini: 2.5. Target: 3.5 dalam 18 bulan.
Buatkan: (1) SPBE gap analysis, (2) open data portal architecture (CKAN-based),
(3) interoperability design, (4) SAKIP dashboard, (5) proposal LKPP.
Reference: Jakarta Smart City (JAKI), Estonia X-Road, Singapore CODEX.
```

---

## PANDUAN 23: Enterprise Data Platform & Modern Data Stack (Vertikal Enterprise)

### 5W1H
- **What**: Implementasi modern data stack: lakehouse + dbt + DataOps + self-service analytics
- **Who**: ER, DM, DAMA, PA, BA | CTO/VP Data sebagai sponsor
- **When**: Perusahaan butuh data platform dari nol atau modernisasi legacy DWH | Timeline: 3-12 bulan
- **Where**: `/engineering-researcher` + `/data-management-researcher` + `/dama-research` + `/product-analyst` + `/business-analyst`
- **Why**: ELT > ETL. Medallion architecture (Bronze→Silver→Gold). Self-service analytics needs semantic layer + governance
- **How**: Discovery → Foundation → Build-Out → Optimize/Handover (4-phase consulting arc)

### Langkah
1. **Discovery (2-4w)**: `/business-analyst` → stakeholder + requirements. `/product-analyst` → metric-definition (KPI inventory). `/engineering-researcher` → tech-radar (tool selection: Snowflake vs Databricks vs BigQuery)
2. **Architecture Design**: `/engineering-researcher` → system-design (medallion lakehouse: Bronze raw → Silver conformed → Gold marts)
3. **dbt Project Structure**: `/engineering-researcher` → system-design (staging → intermediate → marts per dbt best practices)
4. **Data Pipeline (Foundation, 4-8w)**: `/engineering-researcher` → system-design (ingestion: Fivetran/Airbyte/CDC + orchestration: Airflow/Dagster)
5. **DataOps CI/CD**: `/engineering-researcher` → system-design (Write-Audit-Publish pattern, dbt tests, Great Expectations)
6. **Data Catalog**: `/data-management-researcher` → catalog-evaluation (OpenMetadata vs DataHub vs Atlan)
7. **Semantic Layer + Self-Service**: `/product-analyst` → analytics-dashboard + `/data-management-researcher` → data-strategy (business glossary → semantic layer → governed self-service)
8. **Data Governance**: `/dama-research` → KA-01 governance + KA-09 metadata + KA-11 quality
9. **Handover (4-8w)**: `/product-delivery-specialist` → knowledge-transfer + training-plan
10. **Pricing**: `/ideas-company` → estimate (T-shirt sizing: S=2-3 sprints, M=3-5, L=5-8, XL=8+)

### Contoh Prompt
```
Perusahaan e-commerce menengah (500 karyawan) butuh data platform dari nol.
Sumber data: PostgreSQL (transaksi), MongoDB (catalog), event tracking (Segment).
Buatkan: (1) architecture design (medallion lakehouse), (2) dbt project structure,
(3) DataOps CI/CD pipeline, (4) data catalog recommendation, (5) 6-month roadmap.
Budget: Rp 2M. Cloud: GCP (BigQuery).
```
