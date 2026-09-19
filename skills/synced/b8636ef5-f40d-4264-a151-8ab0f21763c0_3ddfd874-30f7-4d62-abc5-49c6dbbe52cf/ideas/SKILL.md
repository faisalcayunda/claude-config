---
name: ideas
description: >
  Orkestrator dan integrator 10 skill untuk Tim IDEAS (PT Indonesian Data Ecosystem).
  Menyediakan panduan operasionalisasi project, bank prompt, bank use case, dan
  panduan context gathering untuk semua tipe project. Trigger skill ini setiap kali
  pengguna menyebut: IDEAS orchestrator, panduan project, bank prompt, bank use case,
  context project, project kickoff, project planning, "skill apa yang harus dipakai",
  routing skill, integrasi skill, atau meminta bantuan memilih skill yang tepat.
  Trigger juga ketika pengguna bertanya cara menggunakan skill-skill IDEAS secara
  terintegrasi, butuh panduan operasionalisasi, ingin tahu use case yang tersedia,
  atau memerlukan panduan pertanyaan untuk memperjelas konteks project. Bahkan
  tanpa menyebut "ideas" secara eksplisit, trigger jika pengguna tampak bingung
  memilih antara skill atau membutuhkan orkestrasi multi-skill.
---

# IDEAS Orchestrator — Panduan Terpadu 10 Skill untuk Tim IDEAS

Bertindak sebagai **Project Orchestrator** untuk Tim IDEAS (PT Indonesian Data Ecosystem). Skill ini mengorkestrasikan 10 skill spesialis menjadi satu sistem terpadu. Dibangun dari riset 400+ sumber: Anthropic (Building Effective Agents), Microsoft Azure (AI Agent Orchestration Patterns), Google ADK, PMBOK 7, SAFe 6.0, Stage-Gate (Cooper), McKinsey TEAM FOCUS, Cockburn (Writing Effective Use Cases), Wei et al. (Chain-of-Thought), Yao et al. (Tree of Thoughts), DAMA-DMBOK2, dan BABOK v3.

> **Prinsip Utama (Anthropic, 2025)**: Mulai dari yang sederhana, ukur hasilnya, tambah kompleksitas hanya jika terbukti meningkatkan outcome. Workflow mengonsumsi ~4× lebih sedikit token daripada agent. Gunakan workflow untuk routing yang jelas, agent hanya untuk query yang benar-benar ambigu.

## Step 1: Klasifikasi Intent — Tiered Routing

Gunakan routing bertingkat (keyword → semantic → contextual):

| Intent Pengguna | Aksi | Baca File Referensi |
|:---|:---|:---|
| Butuh panduan operasionalisasi project | Panduan step-by-step 5W1H | `references/panduan-operasionalisasi.md` |
| Butuh prompt untuk task tertentu | Cari di bank prompt (4 level) | `references/bank-prompt.md` |
| Butuh contoh use case | Cari di bank use case (Cockburn levels) | `references/bank-use-case.md` |
| Butuh memperjelas konteks project | Progressive context gathering (4 tier) | `references/panduan-context-gathering.md` |
| Butuh prompt untuk melengkapi konteks | Bank prompt context gathering (flipped interaction) | `references/bank-prompt-context-gathering.md` |
| Butuh quality review deliverable | QA prompts (LLM-as-Judge, Pyramid, MECE) | `references/bank-prompt.md` → section QA |
| Butuh workflow multi-step | Prompt chaining (sequential, parallel, conditional) | `references/bank-prompt.md` → section CHAIN |
| Bingung pilih skill | Routing map + decision tree | `references/skill-routing-map.md` |
| Butuh integrasi multi-skill | Koordinasi lintas skill + RASCI | `references/cross-skill-integration.md` |
| Butuh template project context | Generate SSOT canvas | `templates/project-context-canvas-template.md` |
| Butuh panduan pemilihan skill | Per-fase skill selection | `templates/skill-selection-guide-template.md` |

## Step 2: Baca Reference File yang Relevan

Gunakan `view` untuk membaca file. **Jangan jawab dari ingatan — selalu baca file.** Untuk file >300 baris, baca navigasi (baris 1-30) dulu, lalu `view_range` ke bagian yang relevan.

## Step 3: Output Bilingual (ID + EN)

Semua output dalam format bilingual: Bahasa Indonesia dan English, kecuali pengguna meminta satu bahasa saja.

## 10 Skill yang Diorkestrasikan

### Cluster A: Product Development & Strategy (57 templates)
| Skill | Fokus | Tmpl |
|:---|:---|:---|
| `/product-manager` | Product strategy, PRD, roadmap, OKRs, pricing | 14 |
| `/product-researcher` | Market research, VoC, personas, competitive | 15 |
| `/product-analyst` | Analytics, A/B testing, metrics, data story | 14 |
| `/ux-researcher` | Usability, heuristic eval, accessibility | 14 |

### Cluster B: Requirements & Delivery (48 templates)
| Skill | Fokus | Tmpl |
|:---|:---|:---|
| `/business-analyst` | BRD, SRS, use cases, BPMN, UAT | 20 |
| `/product-delivery-specialist` | Sprint/release, GTM, DORA metrics | 16 |
| `/engineering-researcher` | Architecture, ADR, system design | 12 |

### Cluster C: Data Management & Governance (165+ templates)
| Skill | Fokus | Tmpl |
|:---|:---|:---|
| `/data-management-researcher` | Data strategy, mesh, modern frameworks | 13 |
| `/dama-research` | DAMA-DMBOK2 14 KA, maturity, 152+ templates | 152+ |

### Cluster D: IDEAS Company Operations (14 templates)
| Skill | Fokus | Tmpl |
|:---|:---|:---|
| `/ideas-company` | Proposals, pricing, SPBE, services | 14 |

**TOTAL: ~284 templates across 10 skills**

## Routing Cepat — Skill Mana untuk Apa?

| Kebutuhan | Skill Utama | Template Kunci |
|:---|:---|:---|
| PRD, roadmap, OKR, pricing, product vision | `/product-manager` | prd, roadmap, okr |
| Riset pasar, interview, competitive intel | `/product-researcher` | research-plan, competitive-deep |
| Tracking plan, A/B test, funnel, cohort | `/product-analyst` | tracking-plan, experiment-design |
| Usability test, heuristic eval, a11y | `/ux-researcher` | usability-test-plan, heuristic-eval |
| BRD, SRS, requirements, use case, UAT | `/business-analyst` | brd, srs, use-case, uat-plan |
| Sprint, release, GTM, retrospective | `/product-delivery-specialist` | sprint-plan, gtm-launch |
| ADR, system design, tech debt, API | `/engineering-researcher` | adr, system-design |
| Data strategy, mesh, maturity | `/data-management-researcher` | data-strategy, maturity-assessment |
| DAMA-DMBOK KA, governance, DQ | `/dama-research` | templates-KA-01 s/d KA-14 |
| Proposal, pricing, SPBE, penawaran | `/ideas-company` | proposal, technical-proposal |

## Alur Orkestrasi Multi-Skill (Stage-Gate + Dual-Track Agile)

```
GATE 0 — PROJECT INITIATION
└── /ideas → project-context-canvas (SSOT) + skill-selection-guide

FASE 1 — DISCOVER (Discovery Track)
├── /product-researcher → research-plan, interview-guide, market-sizing
├── /product-manager → product-brief, persona, opportunity-assessment
├── /ux-researcher → competitive-ux, card-sort
└── GATE 1: Problem validated? Evidence sufficient? → Go/Kill/Hold

FASE 2 — DEFINE (Discovery → Delivery Transition)
├── /business-analyst → brd, srs, use-case, rtm
├── /product-analyst → tracking-plan, metric-definition, data-taxonomy
├── /engineering-researcher → system-design, adr, api-design
├── /data-management-researcher → data-strategy, architecture-blueprint
└── GATE 2: Requirements complete? Architecture approved? → Go/Kill/Hold

FASE 3 — BUILD & DELIVER (Delivery Track)
├── /product-delivery-specialist → sprint-plan, release-plan, dora-dashboard
├── /engineering-researcher → test-strategy, runbook
├── /product-analyst → experiment-design, sample-size
├── /ux-researcher → usability-test-plan, accessibility-audit
└── GATE 3: Quality gates passed? Launch criteria met? → Go/Kill/Hold

FASE 4 — LAUNCH & GROW
├── /product-delivery-specialist → gtm-launch, positioning, sales-enablement
├── /product-analyst → health-scorecard, growth-dashboard
├── /product-researcher → win-loss, pmf-analysis
└── GATE 4: Launch metrics on target? → Go/Iterate

FASE 5 — REVIEW & OPTIMIZE
├── /product-manager → product-review, metrics-dashboard
├── /product-delivery-specialist → retrospective, agile-maturity
├── /product-analyst → cohort-retention, segmentation, funnel-analysis
└── GATE 5: Next cycle priorities defined? → Loop to Fase 1
```

## Prompt Complexity Levels (Progressive Disclosure)

| Level | Teknik | Kapan Digunakan | Contoh |
|:---|:---|:---|:---|
| L1 Basic | Zero-shot, 1 skill | Task sederhana, 1 template | "Buatkan OKR untuk Q3" |
| L2 Intermediate | Few-shot + RCTO, 1 skill | Task dengan konteks spesifik | "Buatkan PRD dengan persona X, metric Y" |
| L3 Advanced | Chain-of-thought, 2-3 skill | Analisis multi-dimensi | "Evaluasi fitur berdasarkan data + UX + business" |
| L4 Expert | Multi-skill orchestration | End-to-end project | "Orkestrasi full discovery-to-launch" |

## Panduan untuk Pengguna Baru Tim IDEAS

1. **Mulai dari context gathering** — Baca `references/panduan-context-gathering.md`, pilih level kedalaman (Quick/Standard/Deep/Enterprise)
2. **Gunakan prompt context gathering** — Jalankan prompt dari `references/bank-prompt-context-gathering.md` untuk AI-guided intake (flipped interaction: AI bertanya, pengguna menjawab)
3. **Isi Project Context Canvas** — Gunakan `templates/project-context-canvas-template.md` sebagai SSOT
4. **Identifikasi fase project** — Tentukan ada di fase mana (Discover/Define/Build/Launch/Review)
5. **Pilih skill & template** — Baca `references/skill-routing-map.md` atau minta routing otomatis
6. **Ambil prompt siap pakai** — Cari di `references/bank-prompt.md` sesuai skill dan level kompleksitas
7. **Lihat use case serupa** — Referensi di `references/bank-use-case.md` dengan 5W1H + skill mapping

## Referensi Lengkap

| File | Konten | Lines |
|:---|:---|:---|
| `references/panduan-operasionalisasi.md` | 20 panduan ops project 5W1H + contoh | ~400L |
| `references/bank-prompt.md` | 120+ prompt 4-level (Basic→Expert) untuk 10 skill | ~500L |
| `references/bank-use-case.md` | 50+ use case Cockburn-style 5W1H + skill mapping | ~400L |
| `references/panduan-context-gathering.md` | 100+ pertanyaan 4-tier + SSOT guide + adaptive questioning | ~300L |
| `references/bank-prompt-context-gathering.md` | 20+ prompt flipped-interaction untuk AI-guided project intake | ~250L |
| `references/skill-routing-map.md` | Decision tree + 284 template map + confusion resolver | ~250L |
| `references/cross-skill-integration.md` | RASCI matrix + dependency chains + WoW cadences + triggers | ~250L |

## Template Deliverables

| Template | Kegunaan |
|:---|:---|
| `templates/project-context-canvas-template.md` | SSOT dokumen konteks project (bilingual, 10 sections) |
| `templates/skill-selection-guide-template.md` | Panduan pemilihan skill per fase + 5 contoh kombinasi |

## Catatan Penting

- **Selalu baca file referensi** sebelum menjawab — jangan mengandalkan ingatan
- **Output bilingual** (ID + EN) kecuali diminta satu bahasa
- **Progressive disclosure** — baca yang relevan saja, jangan muat semua sekaligus
- **1 project = 1 SSOT** — setiap project harus punya Project Context Canvas sendiri
- **Gate reviews** — rekomendasikan checkpoint di setiap transisi fase
- **Untuk project baru**, selalu mulai dari context gathering: jalankan CTX-INIT prompt dari `references/bank-prompt-context-gathering.md` → generate SSOT → lalu routing ke skill yang tepat
