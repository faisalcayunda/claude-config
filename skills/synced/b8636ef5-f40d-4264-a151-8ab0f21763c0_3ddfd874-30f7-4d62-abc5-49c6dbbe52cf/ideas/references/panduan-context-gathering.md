# Panduan Context Gathering — 4-Tier Progressive + Adaptive Questioning
# Context Gathering Guide — 4-Tier Progressive + Adaptive Questioning

> Dibangun dari: MojoTech 25 Questions, OnboardMap 40 Questions, Amazon 6-Pager, BABOK Elicitation (9 techniques), AURA Framework (adaptive AI surveys), MemGPT 3-tier memory.
> Prinsip: 1 Project = 1 SSOT (Single Source of Truth). Output → `templates/project-context-canvas-template.md`

---

## Cara Menggunakan / How to Use

### Pilih Tier Berdasarkan Kompleksitas Project

| Tier | Jumlah | Waktu | Kapan Digunakan |
|:---|:---|:---|:---|
| **Tier 1 — Quick** | 8 pertanyaan | 2-3 menit | Project kecil, scope jelas, ≤3 bulan |
| **Tier 2 — Standard** | 25 pertanyaan | 10-15 menit | Project medium, 3-6 bulan |
| **Tier 3 — Deep** | 50 pertanyaan | 30 menit | Project besar, 6-12 bulan, multi-skill |
| **Tier 4 — Enterprise** | 100+ pertanyaan | Multi-sesi | Enterprise/government, >12 bulan, >Rp 1M |

### Adaptive Questioning Rules
- Ajukan pertanyaan **5-7 per sesi** (jangan overload)
- **Branching**: Jika jawaban Tier 1 menunjukkan kompleksitas tinggi → escalate ke Tier 2
- **Progressive deepening**: Setiap jawaban bisa trigger follow-up questions
- **Skip logic**: Jika tipe klien = startup, skip pertanyaan government/SPBE
- **Confirmation**: Setelah setiap tier, rangkum dan minta konfirmasi sebelum lanjut

---

## TIER 1 — QUICK CONTEXT (8 Pertanyaan Esensial)

> Tujuan: Cukup untuk routing skill dan deliverable selection dasar.

1. **Apa nama project ini?** / Project name?
2. **Deskripsikan project dalam 1-2 kalimat** / 1-2 sentence description?
3. **Siapa klien/sponsor?** / Who is the client/sponsor?
4. **Apa tipe project?** [ ] Product Development [ ] Data Governance [ ] SPBE [ ] Digital Transformation [ ] Analytics [ ] Research [ ] Proposal [ ] Architecture [ ] Other: ___
5. **Berapa budget dan timeline?** / Budget & timeline?
6. **Apa masalah utama yang ingin diselesaikan?** / Core problem?
7. **Siapa target pengguna akhir?** / End users?
8. **Ada di fase mana?** [ ] Ideation [ ] Discovery [ ] Definition [ ] Build [ ] Launch [ ] Optimize

→ **Output**: Bisa langsung routing ke skill yang tepat dan rekomendasikan deliverables prioritas.

---

## TIER 2 — STANDARD CONTEXT (+17 Pertanyaan = Total 25)

> Tujuan: Cukup untuk generate Project Context Canvas dan deliverable plan.

### Problem & Opportunity (Q9-Q13)
9. **Apa dampak masalah ini jika tidak diselesaikan?** (kuantitatif: Rp, %, waktu)
10. **Solusi apa yang sudah pernah dicoba?** Mengapa tidak berhasil?
11. **Apa definisi sukses?** (metrik spesifik, measurable)
12. **Apa yang BUKAN scope?** (eksplisit out-of-scope)
13. **Apa 3 risiko terbesar?**

### Stakeholder (Q14-Q18)
14. **Siapa decision maker utama?** (nama, jabatan)
15. **Siapa stakeholder yang harus dikonsultasikan?** (RASCI context)
16. **Berapa jumlah target pengguna?**
17. **Apa 2-3 persona utama?** (role, pain points)
18. **Tim internal: siapa saja, skill apa?**

### Technical (Q19-Q22)
19. **Tech stack saat ini?**
20. **Sistem yang harus diintegrasikan?** (legacy, API, database)
21. **Infrastruktur?** [ ] Cloud (___) [ ] On-premise [ ] Hybrid
22. **Constraint teknis?** (security, compliance, performance)

### Delivery (Q23-Q25)
23. **Methodology delivery?** [ ] Scrum [ ] Kanban [ ] SAFe [ ] Waterfall [ ] Hybrid
24. **Sprint duration?** [ ] 1w [ ] 2w [ ] 3w [ ] 4w
25. **Tools yang digunakan?** (Jira/Notion/Linear/etc)

→ **Output**: Generate Project Context Canvas lengkap. Bisa plan deliverables per fase.

---

## TIER 3 — DEEP CONTEXT (+25 Pertanyaan = Total 50)

> Tujuan: Enterprise-grade project planning dengan full RASCI dan gate criteria.

### Data Context (Q26-Q33)
26. Apa sumber data utama? Format? Volume?
27. Ada data governance framework yang sudah ada?
28. Isu kualitas data yang diketahui?
29. Siapa data owner/steward saat ini?
30. Regulasi data yang berlaku? [ ] UU PDP [ ] GDPR [ ] SPBE [ ] Satu Data Indonesia
31. Ada master data management (MDM)?
32. Metadata standard yang digunakan?
33. Bagaimana data security saat ini? (encryption, access control)

### Business Context (Q34-Q40)
34. Model bisnis? Revenue model?
35. Kompetitor utama? (top 3)
36. Differentiator utama?
37. Market size (TAM/SAM/SOM)?
38. OKR/KPI organisasi yang terkait?
39. Procurement model? [ ] Direct [ ] Tender/LKPP [ ] e-Katalog
40. Partnership/vendor yang terlibat?

### Delivery Deep (Q41-Q45)
41. Definition of Done tim?
42. Communication cadence? (daily standup, weekly sync, monthly review)
43. Dependency external?
44. Launch strategy? [ ] Big Bang [ ] Phased [ ] Beta [ ] Canary
45. Success measurement post-launch?

### Historical (Q46-Q50)
46. Lessons learned dari project serupa?
47. Benchmark industri yang relevan?
48. Assumptions yang perlu divalidasi?
49. Decisions yang sudah fixed (constraints)?
50. Unknowns yang perlu di-research?

→ **Output**: Full project plan dengan RASCI, gate criteria, risk register.

---

## TIER 4 — ENTERPRISE CONTEXT (+50 Pertanyaan = Total 100+)

> Tujuan: Multi-year transformation programs, government compliance, cross-department.

### Government/SPBE Context (Q51-Q60) — Jika klien pemerintah
51. Level instansi? (Kementerian/Lembaga/Provinsi/Kabupaten/Kota)
52. Skor SPBE saat ini?
53. Domain SPBE fokus? (Kebijakan/Tata Kelola/Manajemen/Layanan/Teknologi)
54. Perpol/Pergub/Perbup terkait tata kelola data?
55. Terhubung Satu Data Indonesia?
56. Walidata dan Produsen Data?
57. Integrasi INAPROC/e-Katalog?
58. PPH gross-up rate?
59. Anggaran APBD/APBN tahun berapa?
60. Contact person BAPPEDA/Kominfo?

### AI/ML Context (Q61-Q68) — Jika project melibatkan AI
61. Tipe AI? (NLP/CV/Predictive/GenAI/Agent)
62. Training data tersedia? Volume?
63. Model yang dipertimbangkan? (open-source/proprietary/fine-tuned)
64. Latency requirement inference?
65. Responsible AI? (fairness, transparency, privacy)
66. Evaluation metrics model? (accuracy, F1, BLEU)
67. MLOps maturity?
68. Compute budget untuk training/inference?

### Organizational Context (Q69-Q80)
69. Org structure yang terlibat? (berapa departemen/divisi)
70. Change readiness? (ADKAR assessment)
71. Executive sponsorship strength? (1-10)
72. Cultural barriers?
73. Training/upskilling needs?
74. Governance committee sudah ada?
75. Previous transformation failures?
76. Union/regulatory constraints?
77. Multi-site/multi-timezone?
78. Vendor management maturity?
79. Budget approval process?
80. Procurement timeline constraints?

### Integration Context (Q81-Q90)
81. Berapa sistem yang harus diintegrasikan? List.
82. API maturity level tiap sistem?
83. Data migration volume?
84. ETL/ELT pipeline existing?
85. Monitoring/observability stack?
86. Disaster recovery requirements?
87. Data residency requirements?
88. Network topology constraints?
89. SSO/Identity provider?
90. Compliance certifications needed? (ISO 27001, SOC2)

### Program Management (Q91-Q100)
91. Governance model? (steering committee, PMO, TMO)
92. Reporting cadence ke sponsor?
93. Budget tracking method? (earned value?)
94. Resource allocation model?
95. Quality assurance framework?
96. Communications plan?
97. Benefits realization tracking?
98. Post-implementation support plan?
99. Knowledge transfer plan?
100. Sustainability/handover plan?

→ **Output**: Full program charter + transformation roadmap + multi-year plan.

---

## PANDUAN MEMBANGUN SSOT / Building the SSOT

Setelah context gathering selesai:

1. **Compile** semua jawaban ke `templates/project-context-canvas-template.md`
2. **Validate** dengan stakeholder — kirim rangkuman untuk konfirmasi tertulis
3. **Version** — setiap update diberi tanggal dan author
4. **Reference** — semua deliverable harus merujuk ke SSOT ini
5. **Update** — review SSOT di setiap gate review

### SSOT Principles (Atlassian + Red Hat)
- **One tool per domain** — jangan duplicate context across systems
- **Living document** — update saat ada informasi baru
- **Accessible** — semua tim bisa akses
- **Authoritative** — satu-satunya sumber kebenaran
- **Versioned** — track changes over time

---

## Context Engineering Principles (Round 8: 85+ Sources)

> "Context engineering supersedes prompt engineering" — Tobi Lütke (Shopify), Andrej Karpathy, Harrison Chase (LangChain), Anthropic Applied AI.
> Core insight: **Most agent failures are context failures, not model failures.** LLM = CPU, context window = RAM. Engineer's job = curate what gets loaded.

### 4-Tier Context System untuk IDEAS Projects

| Tier | Isi | Persistence | Update Frequency |
|:---|:---|:---|:---|
| **System Context** | Identitas IDEAS, metodologi, 10 skill descriptions, quality standards | Permanent | Per skill version |
| **Project Context** | SSOT per klien: brief, stakeholders, constraints, decisions, regulatory | Per-engagement | Setiap session |
| **Workstream Context** | Deliverable-specific: data sources, analysis goals, template selected | Per-deliverable | Per-task |
| **Task Context** | Ephemeral: current prompt, active instructions, last 3-5 turns | Per-invocation | Real-time |

### Write/Select/Compress/Isolate Framework (LangChain)
- **Write**: Capture decisions, findings, client feedback ke SSOT — jangan hanya di conversation
- **Select**: Retrieve relevant context via SSOT sections, bukan dump semua. Gunakan XML tags: `<project_context>`, `<workstream>`, `<task>`
- **Compress**: Summarize older history. Keep: decisions + rationale. Discard: verbose tool output, redundant explanations
- **Isolate**: Delegate subtasks ke skill-specific agents dengan context window terpisah. Cegah context overload

### Context Rot Detection & Prevention
**Context rot** = degradasi kualitas output seiring bertambahnya context window usage.
- **Alert at 50%**: Review apakah semua context masih relevan
- **Compress at 60%**: Summarize older turns, keep decisions + entities
- **Critical at 70%**: Mandatory compaction — SSOT refresh, discard completed tasks
- **Emergency at 85%**: Start new session dengan structured handoff document

**4 Failure Modes (Drew Breunig)**:
1. **Poisoning** — hallucination masuk context, di-reference berulang → fix: validate sebelum persist
2. **Distraction** — context overwhelm training knowledge → fix: minimize non-essential context
3. **Confusion** — superfluous content influence responses → fix: curate ruthlessly
4. **Clash** — contradictory information → fix: resolve conflicts sebelum feed ke LLM

### Structured Format Rules untuk Claude
- **XML tags** untuk prompt structure (Claude fine-tuned untuk XML): `<project_context>`, `<deliverables>`, `<constraints>`, `<task>`
- **Markdown** untuk knowledge base documents (token-efficient, readable)
- **YAML** untuk structured metadata (project parameters, config)
- **JSON** hanya untuk machine-to-machine exchange

### Session Handoff Protocol (Multi-Session Projects)
Di akhir setiap session, generate handoff document (2 menit investasi, hemat 15 menit re-explanation):

```
## Session Handoff — [Project Name] — [Date]
### Goal: [one-sentence objective]
### Status: [% complete, what's done]
### Key Decisions Made:
- [Decision 1]: [rationale] — [date]
- [Decision 2]: [rationale] — [date]
### Active Constraints: [budget, timeline, regulatory, political]
### What to Avoid: [approaches tried and rejected, with reasons]
### Artifacts Changed: [specific deliverables modified]
### Blocked Items: [waiting on external input]
### Very Next Step: [specific, actionable]
### Context Notes: [client preferences, stakeholder dynamics, cultural considerations]
```

### Memory Architecture (3-Layer Persistent)
- **Layer 1 — Working Memory**: Current conversation, active task, token budget monitoring
- **Layer 2 — Project Memory**: Per-client SSOT, engagement history, decision logs (→ `templates/project-context-canvas-template.md`)
- **Layer 3 — Organizational Memory**: Cross-client patterns, error/lesson database, Indonesian regulatory KB, template library
