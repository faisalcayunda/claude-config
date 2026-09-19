# Bank Prompt — 120+ Prompt Siap Pakai untuk 10 Skill IDEAS (4 Level Kompleksitas)
# Prompt Bank — 120+ Ready-to-Use Prompts for 10 IDEAS Skills (4 Complexity Levels)

> Format: **RCTO** (Role → Context → Task → Output) per Anthropic/OpenAI/Google best practices.
> 4 Level: L1 Basic (zero-shot) → L2 Intermediate (few-shot+context) → L3 Advanced (CoT+multi-skill) → L4 Expert (orchestration)

---

## /product-manager — 14 Prompt

**PM-01 [L1] Generate OKR**
```
Buatkan OKR untuk [nama produk] di [quarter]. 2-3 Objectives (aspirational), masing-masing 3-4 Key Results (measurable dengan angka spesifik). Sertakan confidence level dan initiatives per KR. Template: /product-manager → okr-template.
```

**PM-02 [L2] PRD dengan Konteks**
```
Role: Product Manager senior dengan 10+ tahun pengalaman di [industri].
Context: Produk [nama] melayani [persona] dengan masalah [problem]. Kompetitor utama: [X, Y, Z]. Current metrics: [DAU, retention, revenue].
Task: Buatkan PRD lengkap dengan problem statement, user stories (Given/When/Then), functional requirements, non-functional requirements, success metrics (SMART), dan release plan.
Output: Markdown terstruktur dengan section headers. Template: /product-manager → prd-template.
```

**PM-03 [L2] Competitive Analysis**
```
Role: Strategic Product Manager.
Context: Produk [nama] vs kompetitor [A, B, C]. Pasar: [segmen]. Revenue model: [model].
Task: Analisis kompetitif: feature matrix, pricing comparison, positioning map (2x2), SWOT per kompetitor, opportunity gaps.
Output: Tabel perbandingan + strategic recommendations. Template: /product-manager → competitive-analysis-template.
```

**PM-04 [L2] Pricing Strategy**
```
Role: PM + Pricing Specialist. Context: Produk [nama], target [segmen], kompetitor pricing [range].
Task: Buat pricing strategy: cost-based analysis, value-based justification, competitor benchmarking. Sertakan 3 pricing tiers dengan feature gating, freemium analysis jika relevan.
Output: Template: /product-manager → pricing-strategy-template.
```

**PM-05 [L1] Product Roadmap**: "Buatkan roadmap NOW/NEXT/LATER untuk [produk]. Sertakan dependencies, risks, dan success metrics per item."

**PM-06 [L1] Product Brief**: "Buatkan product brief 1-2 halaman untuk ide produk [deskripsi]. Include: vision, target user, problem, proposed solution, success criteria."

**PM-07 [L2] PR/FAQ (Amazon Working Backwards)**: "Buatkan PR/FAQ format Amazon untuk [fitur/produk]. Press release: customer-centric, future tense. FAQ: internal (5 Q) + external (5 Q)."

**PM-08 [L1] Persona**: "Buatkan persona untuk [tipe pengguna] produk [nama]. Demographics, goals, frustrations, behaviors, tech comfort."

**PM-09 [L2] Journey Map**: "Buatkan customer journey map untuk [persona] menggunakan [produk]. Stages, touchpoints, actions, thoughts, emotions, pain points, opportunities."

**PM-10 [L1] Product Review**: "Buatkan product review untuk [produk] quarter [Q]. Metrics: acquisition, activation, engagement, retention, revenue. Status per metric: 🟢/🟡/🔴."

---

## /business-analyst — 14 Prompt

**BA-01 [L2] BRD**
```
Role: Senior Business Analyst (CBAP, BABOK v3).
Context: Project [nama] untuk [organisasi]. Sponsor: [nama]. Problem: [masalah bisnis].
Task: Buatkan BRD: executive summary, business objectives (SMART), scope (in/out), stakeholders, business requirements (BR-001 format: ID, description, priority MoSCoW, source, rationale), constraints, assumptions, dependencies.
Output: IEEE format. Template: /business-analyst → brd-template.
```

**BA-02 [L2] SRS**
```
Role: Systems Analyst (IEEE 29148 certified).
Context: Sistem [nama], module [modul]. BRD reference: [BR-IDs].
Task: Buatkan SRS: functional requirements (FR-001 format), non-functional requirements (performance, security, availability, scalability), interface requirements, data requirements. Setiap requirement: SHALL/SHOULD/MAY + acceptance criteria.
Output: Template: /business-analyst → srs-template.
```

**BA-03 [L1] Gap Analysis**: "Lakukan gap analysis: Current State vs Future State untuk [area/proses]. Format tabel: Area | Current | Desired | Gap | Priority | Action."

**BA-04 [L2] Business Case**: "Buatkan business case untuk investasi [nama]. 3 options analysis + cost-benefit (NPV, ROI, payback period) + risk assessment + recommendation."

**BA-05 [L1] Use Case**: "Buatkan use case untuk [fitur]. Format Cockburn: ID, actors, preconditions, main flow (numbered), alternative flows, postconditions, business rules."

**BA-06 [L1] User Story BDD**: "Buatkan user stories format BDD untuk [fitur]. As a [persona], I want [goal], so that [benefit]. Acceptance: Given/When/Then."

**BA-07 [L1] RACI Matrix**: "Buatkan RACI matrix untuk project [nama]. Deliverables sebagai rows, roles sebagai columns. Satu A per row."

**BA-08 [L2] Root Cause Analysis**: "Lakukan RCA menggunakan 5-Why + Fishbone (Ishikawa) untuk masalah [masalah]. Identifikasi root causes, contributing factors, recommendations."

**BA-09 [L1] Stakeholder Analysis**: "Buatkan stakeholder map untuk project [nama]. Per stakeholder: nama, jabatan, interest level, influence level, communication strategy."

**BA-10 [L1] UAT Plan**: "Buatkan UAT plan untuk [sistem/fitur]. Test scenarios, acceptance criteria, test data, pass/fail criteria, sign-off process."

---

## /product-analyst — 12 Prompt

**PA-01 [L2] Tracking Plan**
```
Role: Product Analyst senior.
Context: Produk [nama/jenis], platform [web/mobile/both]. Analytics tool: [Amplitude/Mixpanel/PostHog/GA4].
Task: Buatkan tracking plan lengkap. Events: nama (snake_case), trigger, properties (name, type, example), user properties. Categorize: pageview, interaction, transaction, system.
Output: Tabel format. Template: /product-analyst → tracking-plan-template.
```

**PA-02 [L2] A/B Test Design**
```
Role: Experimentation Lead.
Context: Hipotesis: "[H0: perubahan X tidak meningkatkan Y]". Baseline: [metric] = [value]. Traffic: [jumlah]/week.
Task: Desain experiment: hypothesis, control vs variant, primary metric, secondary metrics, guardrail metrics, sample size calculation (power 80%, significance 95%), duration, segmentasi.
Output: Template: /product-analyst → experiment-design-template.
```

**PA-03 [L2] Funnel Analysis**: "Analisis funnel [journey]: [step1]→[step2]→[step3]→[step4]. Per step: volume, conversion rate, drop-off %. Segment by [dimension]. Recommendations."

**PA-04 [L2] Data Story (Knaflic)**: "Buatkan data story untuk [audience] tentang [insight]. Framework: Context→Data→Insight→Recommendation. Narrative arc: setup→tension→resolution."

**PA-05 [L1] Health Scorecard**: "Buatkan product health scorecard. AARRR metrics: Acquisition, Activation, Retention, Revenue, Referral. Status 🟢/🟡/🔴 + trend + action items."

**PA-06 [L1] Metric Definition**: "Definisikan metric [nama] secara SMART. Formula, data source, measurement frequency, owner, target, threshold."

**PA-07 [L2] Cohort Retention**: "Analisis cohort retention untuk [produk]. Monthly cohorts, D1/D7/D30/D90 retention. Identify: best/worst cohorts, retention curve shape, benchmarks."

**PA-08 [L1] Sample Size Calculator**: "Hitung sample size: baseline [rate]%, MDE [%]%, power 80%, significance 95%. Berapa traffic dan durasi yang dibutuhkan?"

---

## /product-researcher — 10 Prompt

**PR-01 [L2] Research Plan**: "Buatkan research plan untuk [topik]. Research questions, methodology (qual/quant/mixed), participant criteria, recruitment, timeline, deliverables, budget."

**PR-02 [L2] Interview Guide (Mom Test)**: "Buatkan interview guide untuk [tujuan]. 15-20 questions. Hindari leading questions (Fitzpatrick Mom Test). Include: screening, warm-up, core, probing, wrap-up."

**PR-03 [L2] Market Sizing**: "Hitung TAM/SAM/SOM untuk [produk] di [pasar]. Top-down + bottom-up approach. Data sources, assumptions, confidence level."

**PR-04 [L2] Survey Design**: "Desain survey untuk mengukur [metrik]. Target: [N] responden. Screening, Likert scales, open-ended, skip logic. <10 min completion."

**PR-05 [L2] Win/Loss Analysis**: "Lakukan win/loss analysis. [N] won, [N] lost deals. Win themes, loss reasons, competitive factors, pricing impact, feature gaps."

**PR-06 [L1] Trend Analysis**: "Analisis trend di industri [industri]. 5-10 trend utama, impact assessment (high/med/low), timeline, strategic implications."

**PR-07 [L2] PMF Analysis**: "Evaluasi product-market fit untuk [produk]. Sean Ellis survey (>40% very disappointed), NPS, retention curve, engagement depth."

---

## /ux-researcher — 8 Prompt

**UXR-01 [L2] Usability Test Plan (REFINE)**: "Role: Senior UX Researcher. Expectation: Rigorous usability evaluation. Format: Structured test plan. Participants: [N] dari [segmen]. 5-7 realistic task scenarios. Metrics: task completion, time, errors, SUS."

**UXR-02 [L2] Heuristic Eval (Nielsen 10)**: "Evaluasi [produk] menggunakan 10 Nielsen heuristics. Per heuristic: rating severity (0-4), evidence description, recommendation."

**UXR-03 [L2] Accessibility Audit**: "Audit [produk] berdasarkan WCAG 2.1 Level AA. Per criterion: pass/fail, evidence, remediation. Prioritize by impact."

**UXR-04 [L1] Competitive UX**: "Benchmark UX [produk] vs [kompetitor 1, 2, 3]. Criteria: navigation, onboarding, task efficiency, visual design, accessibility."

**UXR-05 [L2] Design Recommendation**: "Berdasarkan findings [list findings], buatkan design recommendations. Per rec: finding, recommendation, expected impact, effort, priority."

---

## /engineering-researcher — 8 Prompt

**ER-01 [L2] System Design (Google format)**: "Buatkan system design: Context & Goals, Non-Goals, Design (architecture, components, data flow), API contracts, data model, scalability, alternatives considered."

**ER-02 [L2] ADR (MADR)**: "Buatkan ADR: Status, Context, Decision Drivers (min 3), Considered Options (min 3 with pros/cons), Decision Outcome, Consequences."

**ER-03 [L1] Tech Radar**: "Buatkan tech radar untuk [team]. Quadrants: Languages/Frameworks, Tools, Platforms, Techniques. Rings: Adopt, Trial, Assess, Hold."

**ER-04 [L2] Threat Model (STRIDE)**: "Lakukan threat modeling STRIDE untuk [system]. Per threat: Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege."

**ER-05 [L2] API Design**: "Desain REST API untuk [service]. Endpoints, HTTP methods, request/response schemas, auth, error codes, pagination. OpenAPI 3.1 format."

---

## /data-management-researcher — 6 Prompt

**DM-01 [L2] Data Strategy**: "Buatkan data strategy untuk [organisasi]. Vision, principles, current state, target state, initiatives, governance model, technology roadmap, success metrics."

**DM-02 [L2] Maturity Assessment**: "Lakukan DM maturity assessment (CMMI-DMM). Assess: Governance, Architecture, Quality, Security, Integration, Metadata. Rating 1-5 per capability."

**DM-03 [L1] Data Product Canvas**: "Buatkan data product canvas: domain, sources, SLOs, consumers, schema, access patterns, quality metrics, ownership, lifecycle."

---

## /dama-research — 4 Prompt

**DAMA-01 [L2] Governance Charter**: "Buatkan DG charter (DAMA KA-01): vision, scope, principles, org structure, roles (RASCI), decision rights, policies, metrics, communication plan."

**DAMA-02 [L2] DQ Framework**: "Buatkan DQ framework (KA-11): 6 dimensions (accuracy, completeness, consistency, timeliness, validity, uniqueness), measurement, thresholds, remediation."

---

## /product-delivery-specialist — 8 Prompt

**PDS-01 [L1] Sprint Plan**: "Buatkan sprint plan Sprint [N], [duration] weeks. Goal: [goal]. Capacity: [points]. Format: Story | Points | Assignee | Criteria | Dependencies."

**PDS-02 [L2] GTM Launch (T-8w countdown)**: "Buatkan GTM launch plan: T-8w positioning → T-6w enablement → T-4w readiness → T-0 launch → T+2w review. Channels, messaging, success metrics."

**PDS-03 [L1] Retrospective (4Ls)**: "Fasilitasi retro Sprint [N]. 4Ls: Liked, Learned, Lacked, Longed For. Action items dengan owner + due date."

**PDS-04 [L1] DORA Dashboard**: "Buatkan DORA metrics: Deployment Frequency, Lead Time, Change Failure Rate, MTTR. Classification: Elite/High/Medium/Low."

---

## /ideas-company — 10 Prompt (Enriched Round 5: Indonesian Context)

**IDEAS-01 [L2] Technical Proposal LKPP**
```
Role: Konsultan senior IDEAS yang ahli pengadaan pemerintah.
Context: Klien [nama instansi], level [K/L/Prov/Kab/Kota]. Kebutuhan: [deskripsi].
Pagu anggaran: Rp [jumlah]. Metode seleksi: [Seleksi/Pengadaan Langsung].
Task: Buatkan technical proposal sesuai format Dokumen Seleksi LKPP:
1. Tanggapan dan Saran terhadap KAK
2. Uraian Pendekatan, Metodologi, dan Program Kerja
3. Komposisi Tim dan Penugasan (dengan billing rate INKINDO)
4. Jadwal Pelaksanaan Pekerjaan (Gantt chart)
5. Daftar Riwayat Hidup Tenaga Ahli
Output: Format LKPP-compliant. Baca /ideas-company references dulu.
```

**IDEAS-02 [L2] HPS/RAB Calculation**
```
Role: Estimator project IDEAS.
Context: Layanan [kode S1.x-S3.x], level [1-24], jumlah service: [N].
Task: Hitung HPS dengan struktur:
- Biaya Langsung Personil (posisi × person-months × billing rate INKINDO DKI ×multiplier provinsi)
- Biaya Langsung Non-Personil (10-40% dari BLP)
- PPN 11% (PMK 131/2024)
- PPH gross-up jika applicable
Output: Tabel 24 kolom per Perpres 46/2025. Run: /ideas-company → scripts/generate_rab.py
```

**IDEAS-03 [L1] Cost Estimation**: "Hitung estimasi biaya layanan [kode]. Level: [1-24]. Run: /ideas-company → scripts/estimate_service_cost.py --service [kode] --level [N] --breakdown."

**IDEAS-04 [L1] Service Recommendation**: "Klien butuh [kebutuhan]. Sektor: [government/enterprise/bumn]. Run: /ideas-company → scripts/recommend_service.py --need '[kebutuhan]' --sector [sektor]."

**IDEAS-05 [L2] Proposal Pitch Deck (Shipley Method)**
```
Role: Business Development Manager IDEAS.
Context: Klien [nama], bidding vs [kompetitor]. Win themes: [differentiator].
Task: Buatkan pitch deck menggunakan Shipley framework:
- Win strategy (discriminators vs competitors)
- Customer hot buttons (dari intake/interview)
- Solution overview dengan State-Support-Summarize per slide
- Team credentials mapping to client needs
- Pricing summary visual
Gunakan Color Team Review: Blue (strategy) → Pink (draft) → Red (persuasiveness) → Gold (compliance).
Output: Template: /ideas-company → templates/pitch-deck-template.
```

**IDEAS-06 [L2] SPBE Gap Analysis**
```
Role: Konsultan SPBE senior.
Context: Instansi [nama], skor SPBE [skor saat ini], target [target].
Task: Gap analysis per 4 domain SPBE:
- Domain 1 Kebijakan (10 indikator, bobot 13%): skor per indikator, gap, rekomendasi
- Domain 2 Tata Kelola (10 indikator, bobot 25%): skor per indikator, gap, rekomendasi
- Domain 3 Manajemen (11 indikator, bobot 16%): skor per indikator, gap, rekomendasi
- Domain 4 Layanan (16 indikator, bobot 25%): skor per indikator, gap, rekomendasi
Sertakan: mapping ke Satu Data Indonesia (Walidata/Produsen Data), status UU PDP compliance.
Run: /ideas-company → scripts/query_spbe.py untuk data benchmark.
```

**IDEAS-07 [L2] Surat Penawaran**: "Buatkan surat penawaran resmi untuk [klien]. Jenis: [pemerintah/enterprise]. Include: lingkup pekerjaan, metodologi, timeline, tim, biaya. Template: /ideas-company → templates/surat-penawaran-template."

**IDEAS-08 [L2] Change Management ADKAR (Government)**
```
Role: Change Management Specialist untuk proyek pemerintah Indonesia.
Context: Instansi [nama], project [deskripsi], stakeholders [list].
Task: Buatkan change management plan menggunakan ADKAR yang diadaptasi untuk konteks birokrasi Indonesia:
- Awareness: kaitkan dengan target kinerja dan SAKIP, bukan abstract benefits
- Desire: demonstrasi manfaat praktis (akses lebih cepat, peran lebih jelas)
- Knowledge: training policies, tools, stewardship roles + ToT (Training of Trainers)
- Ability: hands-on practice, coaching, dampingan selama adopsi
- Reinforcement: KPI di SKP, recognition, review governance berkala
Pertimbangkan: approval hierarkis, rotasi pejabat, ego sektoral, siklus anggaran APBD.
```

**IDEAS-09 [L2] UU PDP Compliance Assessment**
```
Role: Data Protection Specialist.
Context: Organisasi [nama] mengolah data pribadi [tipe: lokasi/kesehatan/finansial/identitas].
Task: Assess compliance UU 27/2022:
- 9 hak subjek data: apakah sudah difasilitasi?
- 6 dasar pemrosesan: mana yang berlaku?
- Notifikasi breach 3×24 jam: SOP sudah ada?
- DPIA: apakah sudah dilakukan?
- DPO: sudah ditunjuk?
- Transfer data lintas batas: mekanisme?
Catatan: PP pelaksana belum terbit, Lembaga PDP belum terbentuk. Rekomendasikan alignment ISO 27701 + GDPR sebagai best practice interim.
```

**IDEAS-10 [L1] Competitive Landscape**: "Analisis posisi IDEAS vs kompetitor untuk tender [nama]. Baca /ideas-company → references/competitive-landscape.md. Identifikasi win themes dan discriminators."

---

## MULTI-SKILL ORCHESTRATION PROMPTS

**ORCH-01 [L3] Project Kickoff (CoT)**
```
Saya memulai project baru: [deskripsi singkat].
Klien: [nama]. Tipe: [pemerintah/enterprise/startup]. Budget: [Rp]. Timeline: [durasi].

Mari kita pikirkan step by step:
1. Apa konteks yang perlu diperjelas? (gunakan panduan context gathering)
2. Project ini di fase apa? (Discover/Define/Build/Launch/Review)
3. Skill mana yang dibutuhkan per fase?
4. Apa deliverables prioritas per fase?
5. Berikan prompt spesifik untuk setiap deliverable.
```

**ORCH-02 [L3] Cross-Skill Analysis**
```
Saya sudah punya [deliverable, misal: PRD dari /product-manager].
Pikirkan step by step:
1. Deliverable apa yang harus dibuat selanjutnya?
2. Skill mana yang bertanggung jawab?
3. Apa dependency dan prerequisite?
4. Berikan prompt untuk masing-masing.
```

**ORCH-03 [L4] Full End-to-End Orchestration**
```
Orkestrasi penuh project [deskripsi]. Budget: [Rp]. Timeline: [bulan].
Untuk setiap fase (Discover→Define→Build→Launch→Review):
- List semua deliverables yang dibutuhkan
- Map ke skill yang tepat
- Tentukan urutan (prerequisite → companion → downstream)
- Berikan prompt siap pakai per deliverable
- Definisikan gate criteria per transisi fase
```

**ORCH-04 [L4] SPBE Improvement Orchestration**
```
Instansi [nama] skor SPBE [skor], target [target]. 
Orkestrasi: gap analysis (BA) → DAMA-SPBE alignment (DAMA) → data strategy (DM) → architecture (ER) → policy (IDEAS) → implementation (PDS) → proposal (IDEAS).
Per deliverable: skill, template, prompt, timeline, dependencies.
```

**ORCH-05 [L4] Data Governance Full Program**
```
Orkestrasi program data governance untuk [organisasi]. Maturity: [level/unknown].
Fase 1 (Assess): DAMA maturity + DM maturity assessment
Fase 2 (Strategy): DM data strategy + DAMA governance charter
Fase 3 (Build): DAMA KA-02 architecture + KA-11 quality + KA-09 metadata
Fase 4 (Implement): PDS sprint plan + BA stakeholder + PDS change management
Fase 5 (Monitor): PA health scorecard + DM maturity re-assessment
```

---

## QUALITY REVIEW PROMPTS (Round 6: Self-Improving Feedback Loops)

**QA-01 [L3] Deliverable Quality Review (LLM-as-Judge)**
```
Review deliverable berikut menggunakan 5 quality dimensions:
[paste deliverable]

Evaluasi MASING-MASING dimensi secara independen (score 1-5 + evidence):
1. ACCURACY — apakah fakta, data, angka benar?
2. COMPLETENESS — apakah semua section yang dibutuhkan ada?
3. RELEVANCE — apakah konten sesuai konteks project?
4. ACTIONABILITY — apakah output bisa langsung dieksekusi?
5. STRUCTURE — apakah mengikuti Pyramid Principle (assertion first, MECE supporting)?

Untuk setiap dimensi yang <4, berikan:
- Apa yang kurang
- Bagaimana cara memperbaiki (specific, actionable)
- Contoh perbaikan

Verdict: PASS (semua ≥4) atau REVISE (ada yang <4) + prioritized fix list.
```

**QA-02 [L2] Pyramid Principle & MECE Check**
```
Review dokumen ini terhadap standar consulting-grade:
[paste document]

Check 1 — Pyramid Principle: Apakah setiap section dimulai dengan ANSWER/ASSERTION dulu, baru supporting evidence? Tandai section yang belum.
Check 2 — MECE: Apakah arguments mutually exclusive (tidak overlap) dan collectively exhaustive (tidak ada gap)? Tandai overlap dan gap.
Check 3 — So What: Untuk setiap data point, apakah ada insight + recommendation? Tandai "naked data" tanpa interpretation.
Check 4 — Action Items: Apakah setiap recommendation punya owner, timeline, dan success metric?
```

**QA-03 [L3] Evaluator-Optimizer Loop (Anthropic Pattern)**
```
Saya akan memberikan output yang perlu di-improve melalui iterasi.

STEP 1 — EVALUATE: Review output berikut terhadap criteria [list criteria].
Berikan verdict PASS atau REVISE dengan specific issues.

STEP 2 — OPTIMIZE: Jika REVISE, perbaiki output berdasarkan feedback.
Jangan ubah bagian yang sudah PASS. Fokus hanya pada issues yang diidentifikasi.

STEP 3 — RE-EVALUATE: Review ulang hasil perbaikan.
Ulangi hingga PASS atau max 3 iterasi.

Output yang perlu di-review:
[paste output]

Criteria: [list specific criteria per deliverable type]
```

---

## PROMPT CHAINING PATTERNS (Round 6: Multi-Step Workflow Architecture)

**CHAIN-01 [L4] Sequential Chain with Quality Gates**
```
Jalankan workflow multi-step berikut. Setiap step harus PASS quality gate sebelum lanjut.

STEP 1: [Skill A] → Generate [deliverable 1]
  GATE 1: Cek completeness + accuracy. Jika FAIL → revise, max 2 iterasi.

STEP 2: [Skill B] → Gunakan output Step 1 sebagai input → Generate [deliverable 2]
  GATE 2: Cek consistency dengan Step 1 + completeness. Jika FAIL → revise.

STEP 3: [Skill C] → Gunakan output Step 1+2 → Generate [deliverable 3]
  GATE 3: Final review semua deliverables untuk coherence.

Context yang harus dipertahankan antar step:
- Project name, client, constraints dari SSOT
- Keputusan di step sebelumnya
- Assumptions yang sudah divalidasi

Contoh: PM(PRD) →[gate]→ BA(SRS) →[gate]→ ER(system-design) →[gate]→ PDS(sprint-plan)
```

**CHAIN-02 [L3] Parallel Fan-Out + Aggregation**
```
Jalankan 3 analisis PARALEL terhadap [topik/deliverable]:

BRANCH A — [Skill X] perspektif: [fokus A]
BRANCH B — [Skill Y] perspektif: [fokus B]  
BRANCH C — [Skill Z] perspektif: [fokus C]

Setelah ketiga branch selesai, AGGREGATE:
1. Identifikasi area KONSENSUS (semua setuju)
2. Identifikasi area KONTRADIKSI (perlu resolusi)
3. Synthesize menjadi satu recommendation set

Contoh: PA(data analysis) || UXR(usability findings) || PR(market research) → PM(feature prioritization)
```

**CHAIN-03 [L3] Conditional Routing Chain**
```
Berdasarkan konteks project berikut:
[paste SSOT atau deskripsi]

CLASSIFY tipe project → route ke chain yang tepat:

IF product development → CHAIN: PM(brief) → PR(research) → BA(BRD) → ER(design) → PDS(sprint)
IF data governance → CHAIN: DM(maturity) → DAMA(charter) → DM(strategy) → PDS(implementation)
IF SPBE improvement → CHAIN: IDEAS(baseline) → BA(gap) → DAMA(alignment) → PDS(roadmap) → IDEAS(proposal)
IF proposal/pitch → CHAIN: IDEAS(recommend) → IDEAS(estimate) → IDEAS(proposal) → IDEAS(pitch)

Untuk chain yang dipilih, jalankan step-by-step dengan quality gate antar step.
```

---

## GOVERNANCE & MEASUREMENT PROMPTS (Round 7: Composable Skill Architecture)

**GOV-01 [L2] AI Governance Assessment**
```
Role: AI Governance Specialist (NIST AI RMF + ISO 42001).
Context: Organisasi [nama] menggunakan AI untuk [use cases]. Jumlah AI tools: [N].
Task: Assess AI governance maturity menggunakan framework berikut:
1. GOVERN — Kebijakan AI, accountability structure, risk appetite
2. MAP — Context mapping, stakeholder identification, use case inventory
3. MEASURE — Risk quantification per use case (bias, accuracy, security, privacy)
4. MANAGE — Risk responses, monitoring, incident procedures

Per dimension: rating (1-5), evidence, gaps, recommendations.
Sertakan alignment check ke UU PDP Indonesia dan ISO 42001 controls.
```

**GOV-02 [L2] HITL Approval Workflow Design**
```
Desain human-in-the-loop approval workflow untuk project [nama].

Untuk setiap deliverable yang di-generate AI, tentukan:
1. CATEGORY: [ ] Auto-proceed [ ] Spot-check (10%) [ ] Mandatory review [ ] Mandatory approval
2. REVIEWER: Siapa yang review (by role, bukan nama)
3. CRITERIA: Apa yang harus dicek (checklist)
4. SLA: Berapa lama review harus selesai
5. ESCALATION: Apa yang terjadi jika SLA terlewat

Rule of thumb:
- Client-facing → Mandatory approval
- Internal draft → Auto-proceed + spot check
- Cost/pricing → Mandatory approval
- First-time deliverable type → Mandatory review
- Recurring deliverable → Spot-check

Output: Decision matrix table.
```

**GOV-03 [L2] Deliverable Audit Trail**
```
Buatkan audit trail untuk deliverable [nama deliverable].
Record:
- Skill yang generate: [skill name]
- SSOT version referenced: [version]
- Prompt used: [prompt ID + version]
- Generated at: [timestamp]
- Reviewed by: [reviewer name + role]
- Review status: [ ] Approved [ ] Approved with changes [ ] Rejected
- Changes made post-generation: [list changes]
- Final version delivered to client: [ ] Yes [ ] No
- Client feedback: [if available]

Format sebagai appendix yang bisa di-attach ke deliverable.
```

**MEASURE-01 [L2] Orchestrator Effectiveness Dashboard**
```
Buatkan effectiveness dashboard untuk IDEAS orchestrator di project [nama].

Track 4 tiers:
1. QUALITY: QA-01 scores per deliverable, revision count, Pyramid compliance rate
2. EFFICIENCY: Time from prompt to final deliverable, number of iterations, skills used
3. ADOPTION: % deliverables generated via skill (vs manual), SSOT completion %, prompts used per week
4. BUSINESS IMPACT: Client satisfaction (1-5), proposal win rate, delivery on-time rate

Per metric: current value, target, trend (↑↓→), action needed.
Sertakan token waste indicators: regeneration rate, context bloat %, abandoned outputs %.
```

---

## CONSULTING DELIVERABLE QUALITY PROMPTS (Round 8: MBB Standards + Indonesian Adaptation)

**CONSULT-01 [L3] Ghost Deck / Dot-Dash Storyline**
```
Sebelum membuat deliverable lengkap, buatkan dot-dash storyline dulu:

Project: [nama]. Klien: [nama]. Tipe deliverable: [report/proposal/assessment/strategy].

Format dot-dash:
• [Main point 1 — complete sentence, action-oriented]
  - Supporting evidence/data
  - Supporting evidence/data
• [Main point 2]
  - Supporting evidence/data
  - Supporting evidence/data

Rules:
- Setiap main point (dot) = satu slide title / section heading
- Baca semua dots secara berurutan → harus membentuk storyline yang koheren
- Ikuti SCQA: Situation (10-15%) → Complication (15-20%) → Resolution (60-70%)
- Setiap dot harus assertion, bukan topic label
  ❌ "Analisis Revenue" 
  ✅ "Revenue tumbuh 12% YoY namun margin turun 3pp karena kenaikan COGS"

Review dot-dash sebelum lanjut ke full deliverable.
```

**CONSULT-02 [L3] Pyramid Principle + SCQA Structure**
```
Struktur deliverable ini menggunakan Pyramid Principle + SCQA:

EXECUTIVE SUMMARY (gunakan format SCQA):
- Situation: [konteks yang sudah diketahui klien — 2-3 kalimat]
- Complication: [masalah/perubahan yang memicu engagement — 2-3 kalimat]
- Question: [pertanyaan bisnis yang dijawab deliverable ini — implisit atau eksplisit]
- Answer: [rekomendasi utama — 1-2 kalimat, tegas, tanpa hedging]

BODY (Pyramid top-down):
- Level 1: Governing thought (= Answer dari SCQA)
- Level 2: 3 key supporting arguments (MECE — mutually exclusive, collectively exhaustive)
- Level 3: Evidence per argument (data, benchmarks, case studies)

PER SECTION CHECK:
- [ ] Action title (complete sentence, bukan topic label)?
- [ ] One message per section?
- [ ] Evidence has source citation?
- [ ] "So What" stated explicitly?
- [ ] Recommendation has: Owner + Timeline + Success Metric + Dependencies?
```

**CONSULT-03 [L2] Anti-AI-Speak Quality Filter**
```
Review deliverable berikut dan perbaiki AI writing artifacts:

[paste deliverable]

BANNED PHRASES — ganti dengan specific alternatives:
- "leverage" → gunakan kata kerja spesifik (gunakan, manfaatkan, terapkan)
- "synergy" → jelaskan manfaat spesifik yang dimaksud
- "cutting-edge/state-of-the-art" → sebutkan teknologi/metode spesifik
- "holistic" → "mencakup [list specific areas]"
- "transformative" → quantify the change
- "paradigm shift" → describe what actually changed
- "It is important to note" → hapus, langsung sampaikan
- "In conclusion" → hapus, gunakan action title
- "This report aims to" → hapus, langsung ke content

HEDGE-WORD CHECK — target: <5% hedge density:
- Ganti "may/might/could" → definitive statement atau explicit uncertainty with rationale
- Ganti "generally/typically" → specific data or "in [N]% of cases"
- Ganti "significant" → quantify (berapa? dibanding apa?)

SPECIFICITY CHECK:
- Setiap claim harus punya angka, sumber, atau contoh konkret
- Setiap rekomendasi harus punya owner, timeline, metric
```

**CONSULT-04 [L2] Indonesian Government Tone Adaptation**
```
Adaptasi deliverable berikut untuk klien pemerintah Indonesia:

[paste deliverable]

RULES:
1. BAHASA: Gunakan Bahasa Indonesia baku (per Perpres 63/2019). Bilingual OK jika diminta
2. REGISTER: Formal. "Kami merekomendasikan untuk mempertimbangkan..." bukan imperatif langsung
3. HONORIFICS: Selalu gunakan Bapak/Ibu untuk nama individu
4. FRAMING: "Area untuk pengembangan" bukan "kelemahan/kekurangan"
5. VOICE: Passive voice lebih sering dari English consulting norms — untuk soften directness
6. REGULATORY: Reference framework pemerintah (SPBE, RPJMN, Perpres) untuk menunjukkan alignment
7. OPENING: Formal greeting + pleasantries sebelum substansi
8. CLOSING: Ekspresi penghargaan + komitmen kemitraan berkelanjutan
9. HIERARCHY: Rekomendasi di-frame sebagai saran untuk didiskusikan bersama, bukan diktasi
10. FACE-SAVING: Jangan atribusikan kegagalan ke individu/unit spesifik secara publik

FORMAT SURAT RESMI (jika applicable):
- Kop surat IDEAS
- Nomor surat, perihal, lampiran
- "Dengan hormat," opening
- "Hormat kami," closing + nama + jabatan
```
