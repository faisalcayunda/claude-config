# Skill Routing Map — Peta Routing Detail 10 Skill IDEAS
# Skill Routing Map — Detailed Routing for 10 IDEAS Skills

> Tiered routing: keyword match (L1) → semantic similarity (L2) → contextual LLM routing (L3)

---

## Decision Tree / Pohon Keputusan Routing

```
Pengguna butuh bantuan tentang...
│
├── PRODUK (fitur, strategi, roadmap, pricing)
│   ├── Strategy/vision/roadmap/OKR/PMF → /product-manager
│   ├── Market research/competitive/persona/VoC → /product-researcher
│   ├── Analytics/metrics/A-B test/funnel/cohort → /product-analyst
│   └── Usability/UX audit/accessibility/IA → /ux-researcher
│
├── REQUIREMENTS (dokumen kebutuhan sistem)
│   ├── BRD/SRS/FRS/use case/UAT/BPMN → /business-analyst
│   ├── PRD/feature spec/product brief → /product-manager
│   └── NFR + architecture → /business-analyst + /engineering-researcher
│
├── DELIVERY (eksekusi & launch)
│   ├── Sprint/release/PI/retro/agile → /product-delivery-specialist
│   ├── GTM/positioning/sales/battlecard → /product-delivery-specialist
│   └── DORA/value stream/growth → /product-delivery-specialist
│
├── ENGINEERING (arsitektur & teknis)
│   ├── System design/ADR/RFC/API → /engineering-researcher
│   ├── Tech radar/tech debt/perf → /engineering-researcher
│   └── Threat model/postmortem/runbook → /engineering-researcher
│
├── DATA (tata kelola & manajemen data)
│   ├── Modern: strategy/mesh/fabric/lakehouse → /data-management-researcher
│   ├── Classic: DAMA-DMBOK/KA/maturity → /dama-research
│   ├── Governance charter/policy → /dama-research (KA-01)
│   ├── DQ/MDM/metadata → /dama-research (KA-10,11,09) + /data-management-researcher
│   └── PIA/compliance/standards → /data-management-researcher
│
├── IDEAS COMPANY (company-specific)
│   ├── Proposal/pitch/surat penawaran/BoQ → /ideas-company
│   ├── Pricing/COGS/RAB/cost estimation → /ideas-company
│   ├── SPBE assessment/scores → /ideas-company
│   └── Service recommendation → /ideas-company
│
└── BINGUNG / MULTI-SKILL
    ├── "Skill apa yang harus dipakai?" → /ideas (this skill)
    ├── "Bagaimana memulai project?" → /ideas → context gathering
    └── "Butuh beberapa skill sekaligus" → /ideas → orchestration flow
```

---

## Template Quick Reference per Skill (284 total)

### /product-manager (14): prd, product-brief, prfaq, roadmap, okr, persona, journey-map, competitive-analysis, feature-spec, pricing-strategy, opportunity-assessment, product-launch-checklist, metrics-dashboard, product-review

### /business-analyst (20): brd, srs, frs, nfr, use-case, user-story-bdd, rtm, business-rules, business-case, feasibility, gap-analysis, stakeholder, raci, rca, bpmn-process, sipoc, data-dictionary, uat-plan, impact-analysis, solution-assessment

### /product-analyst (14): tracking-plan, data-taxonomy, metric-definition, experiment-design, ab-test-report, sample-size, funnel-analysis, cohort-retention, feature-adoption, segmentation, health-scorecard, saas-dashboard, analytics-brief, data-story

### /product-researcher (15): research-plan, interview-guide, survey-design, market-sizing, competitive-deep, trend-analysis, research-persona, voc-report, win-loss, pmf-analysis, pricing-research, thematic-analysis, insight-report, journey-research, research-repo

### /ux-researcher (14): usability-test-plan, usability-test-report, heuristic-eval, cognitive-walkthrough, card-sort, ia-assessment, sus-scoring, accessibility-audit, ux-benchmark, ux-findings, design-recommendation, prototype-test, design-system-eval, competitive-ux

### /engineering-researcher (12): adr, technical-rfc, system-design, architecture-review, tech-radar, tech-debt-register, runbook, postmortem, threat-model, test-strategy, api-design, performance-benchmark

### /data-management-researcher (13): maturity-assessment, data-strategy, dq-framework-comparison, mesh-readiness, data-product-canvas, mdm-strategy, tool-landscape, fair-assessment, standards-mapping, architecture-blueprint, pia, governance-comparison, catalog-evaluation

### /product-delivery-specialist (16): sprint-plan, retrospective, release-plan, pi-planning, team-agreement, dora-dashboard, vsm, agile-maturity, gtm-launch, positioning, sales-enablement, launch-readiness, growth-dashboard, battlecard, change-management, onboarding-playbook

### /dama-research (152+): Organized by KA-01 through KA-14. Use `templates/INDEX.md` for master list.

### /ideas-company (14): assessment-report, boq, business-proposal, data-product-canvas, knowledge-transfer, output-deliverable, pitch-deck, policy-framework, product-spec, proposal, service-description, surat-penawaran, technical-proposal, training-material

---

## Confusion Zone Resolver — Template yang Mirip Tapi Beda Skill

| Sering Tertukar | Skill A | Skill B | Perbedaan Kunci |
|:---|:---|:---|:---|
| competitive-analysis (PM) vs competitive-deep (PR) | PM | PR | PM=strategic positioning, PR=deep market intel with methodology |
| competitive-ux (UXR) | — | UXR | UX benchmarking spesifik, bukan market/business |
| persona (PM) vs research-persona (PR) | PM | PR | PM=assumption-based/lean, PR=research-validated from interviews |
| journey-map (PM) vs journey-research (PR) | PM | PR | PM=design tool for team, PR=research methodology with evidence |
| data-dictionary (BA) vs metadata (DAMA KA-09) | BA | DAMA | BA=system-level for 1 project, DAMA=enterprise-wide standard |
| data-product-canvas: DM vs IDEAS | DM | IDEAS | DM=general enterprise, IDEAS=IDEAS-company-specific |
| pricing-strategy (PM) vs pricing-research (PR) | PM | PR | PM=strategy document, PR=research methodology (Van Westendorp/Conjoint) |
| data-strategy (DM) vs governance (DAMA KA-01) | DM | DAMA | DM=modern frameworks (mesh/fabric), DAMA=DMBOK2 standard |
| maturity-assessment (DM) vs KA-14 (DAMA) | DM | DAMA | DM=custom/CMMI-DMM, DAMA=DMBOK2 maturity calculator |
| architecture-blueprint (DM) vs system-design (ER) | DM | ER | DM=data architecture focus, ER=full system architecture |
| nfr (BA) vs threat-model (ER) | BA | ER | BA=requirements document, ER=security analysis methodology |

### Rule of Thumb
- **Kalau soal "apa yang harus dibangun" → PM**
- **Kalau soal "bagaimana requirement-nya" → BA**
- **Kalau soal "bagaimana diukur" → PA**
- **Kalau soal "apa yang user butuhkan" → PR/UXR**
- **Kalau soal "bagaimana arsitekturnya" → ER**
- **Kalau soal "bagaimana data-nya dikelola" → DM/DAMA**
- **Kalau soal "bagaimana di-deliver" → PDS**
- **Kalau soal "proposal/pricing IDEAS" → IDEAS**

---

## Executable Scripts — IDEAS Company & DAMA

### /ideas-company Scripts (16 scripts)
| Script | Fungsi | Contoh Command |
|:---|:---|:---|
| `recommend_service.py` | Rekomendasi layanan IDEAS berdasarkan kebutuhan | `--need "data governance" --sector government` |
| `estimate_service_cost.py` | Estimasi biaya layanan (level 1-24) | `--service S1.1 --level 8 --breakdown` |
| `calculate_project_cost.py` | Kalkulasi biaya project lengkap | Multi-service project cost |
| `generate_proposal.py` | Generate proposal lengkap | Orchestrate template + pricing |
| `build_proposal_docs.py` | Build PPTX/DOCX proposal | Direct structured-data builder |
| `generate_rab.py` | RAB/HPS 24-kolom enterprise (Perpres 46/2025) | Budget plan per komponen |
| `generate_cogs.py` | COGS calculation (4-component) | Direct/Indirect/Overhead/Margin |
| `generate_timeline.py` | Gantt chart timeline project | Phase + milestone + dependencies |
| `pricing_engine.py` | Pricing engine (rate card + markup) | Service-level pricing |
| `rate_card.py` | Rate card per role/level | 141 DDaT roles |
| `query_spbe.py` | Query SPBE scores nasional | `--province "Jawa Barat"` |
| `scenario_model.py` | What-if scenario modeling | Budget/timeline/scope tradeoffs |
| `generate_docx.py` | Generate Word document | Template-driven DOCX |
| `generate_pptx.py` | Generate PowerPoint | Template-driven PPTX |
| `generate_pdf.py` | Generate PDF | Template-driven PDF |
| `generate_document.py` | Universal document generator | Route to docx/pptx/pdf |

### /dama-research Tools
| Tool | Fungsi | Command |
|:---|:---|:---|
| `maturity-calculator.py` | Maturity assessment DAMA-DMBOK2 (14 KA) | `python maturity-calculator.py interactive` |
