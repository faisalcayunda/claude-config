# Cross-Skill Integration — RASCI, Dependency Chains, WoW, Proactive Triggers
# Cross-Skill Integration — RASCI, Dependency Chains, WoW, Proactive Triggers

> Built from: Abbott/Fisher RASCI (Art of Scalability), SAFe 6.0 PI cadences, Reinertsen (Product Development Flow), Cagan (Dual-Track Agile), Torres (Continuous Discovery), Atlassian automation patterns.

---

## RASCI Antar Skill per Deliverable

| Deliverable | R (Responsible) | A (Accountable) | S (Supportive) | C (Consulted) | I (Informed) |
|:---|:---|:---|:---|:---|:---|
| PRD | PM drafts | PM | PR (market), UXR (usability) | BA (req), ER (feasibility) | PDS |
| BRD | BA drafts | BA | PM (biz context) | PR (market), ER (tech) | PDS |
| SRS | BA drafts | BA | ER (tech validation) | DM (data model), PM (scope) | PDS |
| Tracking Plan | PA drafts | PA | ER (instrumentation) | BA (data dict), PM (metrics) | PDS |
| Research Plan | PR drafts | PR | UXR (methods) | PA (quant), PM (focus) | PDS |
| Usability Test | UXR plans | UXR | PR (participants) | PM (scope), BA (scenarios) | PDS |
| System Design | ER drafts | ER | DM (data arch) | BA (req), PM (scope) | PDS |
| Data Strategy | DM drafts | DM | DAMA (DMBOK) | BA (biz), ER (tech) | PM |
| Governance Charter | DAMA drafts | DM | BA (stakeholder) | ER (tech), PM (biz) | PDS |
| Sprint Plan | PDS facilitates | PDS | BA (stories), ER (tasks) | PM (priorities), PA (data) | All |
| GTM Launch | PDS leads | PDS | PR (intel), PM (product) | PA (metrics), UXR (UX) | All |
| Proposal | IDEAS drafts | IDEAS | DM (scope), BA (req) | PM (product), DAMA (theory) | PDS |

**Rule**: Exactly 1 Accountable per deliverable. S = hands-on assistance. C = two-way SME input. I = one-way notification.

---

## Prerequisite-Companion-Downstream Chains

### Chain 1: Product Discovery → Delivery → Growth
```
PR(research-plan) → PR(interview-guide) → PR(research-persona)
  ↓ feeds
PM(product-brief) → PM(persona) → PM(opportunity-assessment)
  ↓ feeds
BA(brd) → BA(srs) → BA(use-case) → BA(rtm)
  ↓ feeds
ER(system-design) → ER(adr) → ER(api-design)
  ↓ feeds
PDS(sprint-plan) → PDS(release-plan) → PDS(dora-dashboard)
  ↓ feeds
PDS(gtm-launch) → PDS(positioning) → PDS(launch-readiness)
  ↓ feeds
PA(health-scorecard) → PA(funnel-analysis) → PA(cohort-retention)
```

### Chain 2: Data Governance Program
```
DM(maturity-assessment) + DAMA(KA-14 maturity)
  ↓ feeds
DM(data-strategy) → DAMA(KA-01 governance charter)
  ↓ feeds
DM(architecture-blueprint) + DAMA(KA-02 architecture)
  ↓ feeds
DAMA(KA-11 quality) + DM(dq-framework-comparison)
  ↓ feeds
DM(mdm-strategy) + DAMA(KA-10 master data)
  ↓ feeds
BA(stakeholder + raci) → PDS(sprint-plan + change-management)
```

### Chain 3: Analytics → Experimentation Loop
```
PM(okr) → PA(metric-definition) → PA(data-taxonomy) → PA(tracking-plan)
  ↓ feeds
ER(system-design for instrumentation)
  ↓ feeds
PA(experiment-design) → PA(sample-size) → PA(ab-test-report)
  ↓ feeds back
PM(product-review) → PM(feature-spec for winning variant)
```

### Chain 4: IDEAS Proposal Pipeline
```
IDEAS(recommend_service.py) → IDEAS(estimate_service_cost.py)
  ↓ feeds
DM(data-strategy preview) + DAMA(KA alignment)
  ↓ feeds
IDEAS(technical-proposal) → IDEAS(business-proposal)
  ↓ feeds
IDEAS(boq) → IDEAS(surat-penawaran)
  ↓ if won
PDS(sprint-plan + release-plan) — execution begins
```

---

## Proactive Trigger Rules

Ketika skill X dipanggil, rekomendasikan deliverable dari skill Y:

| Trigger (Skill Dipanggil) | Rekomendasikan | Alasan |
|:---|:---|:---|
| PM → PRD | BA → SRS + use-case | PRD needs technical spec |
| PM → Persona | PR → research-persona | Validate with research |
| PM → Roadmap | PDS → release-plan | Roadmap needs execution |
| PM → OKR | PA → metric-definition | OKRs need measurable metrics |
| BA → BRD | PM → product-brief | BRD needs business context |
| BA → SRS | ER → system-design + adr | SRS needs architecture |
| BA → UAT | UXR → usability-test-plan | UAT should include UX |
| PA → Tracking Plan | ER → system-design | Tracking needs engineering |
| PA → Experiment wins | PM → feature-spec | Winning experiments → features |
| PR → Research Plan | UXR → usability-test-plan | Research + usability together |
| PR → Competitive | PDS → battlecard | Intel → sales tools |
| UXR → Heuristic | BA → impact-analysis | UX issues → impact assess |
| UXR → Accessibility | BA → nfr | A11y → NFR requirements |
| ER → System Design | DM → architecture-blueprint | System needs data arch |
| ER → ADR | PDS → sprint-plan | ADRs may create tech debt |
| ER → Postmortem | PDS → retrospective | Incident → team reflection |
| DM → Data Strategy | DAMA → KA-01 charter | Strategy needs governance |
| DM → Maturity | IDEAS → service recommendation | Gaps → service opportunities |
| PDS → Sprint Plan | PA → health-scorecard | Sprints need monitoring |
| PDS → GTM Launch | PR → win-loss setup | Launch needs feedback |
| IDEAS → Proposal | DM + DAMA → scope | Proposals need depth |
| DAMA → KA-14 Maturity | DM → data-strategy | Assessment → strategy |

---

## Ways of Working — Operating Cadences

### Sprint Cadence (1-2 weekly)
| Ceremony | Lead | Participating Skills |
|:---|:---|:---|
| Sprint Planning | PDS | PM (priorities), BA (stories), ER (tech tasks) |
| Daily Standup | PDS | All active |
| Sprint Review | PDS | PM (demo), PA (metrics), UXR (usability data) |
| Sprint Retro | PDS | All team |

### Monthly Cadence
| Ceremony | Lead | Participating Skills |
|:---|:---|:---|
| Product Review | PM | PA (data), PDS (DORA), UXR (UX data) |
| Research Shareout | PR | PM, UXR, PA |
| Architecture Review | ER | DM (data), BA (req), PM (scope) |
| Data Quality Review | DM | DAMA, PA (metrics), BA (rules) |

### Quarterly Cadence
| Ceremony | Lead | Participating Skills |
|:---|:---|:---|
| OKR Setting | PM | PA (metrics), PDS (capacity), PR (market) |
| PI Planning (SAFe) | PDS | PM (vision), BA (epics), ER (constraints) |
| Tech Radar | ER | DM (data tools), PM (needs) |
| Competitive Update | PR | PDS (battlecard), PM (positioning) |

### Per-Launch Cadence
| Milestone | Lead | Skills |
|:---|:---|:---|
| T-8w: Positioning | PDS | PR (intel), PM (strategy) |
| T-6w: Enablement | PDS | PR (research), PM (specs) |
| T-4w: Readiness | PDS | ER (benchmark), UXR (audit), PA (analytics) |
| T-0: Launch | PDS | All standby |
| T+2w: Review | PM | PA (data), PR (win/loss), UXR (usability) |

---

## Collaboration Archetypes per Deliverable

| Archetype | Description | Example Deliverables |
|:---|:---|:---|
| **Workshop-Driven** | Sync co-creation, semua kontributor hadir | Sprint Plan, Retro, PI Planning, Positioning, RCA |
| **Collaborative Draft** | 1 drafts → others contribute sections → review | PRD, BRD, System Design, Data Strategy, Proposal |
| **Data Assembly** | Pull from multiple quantitative sources | Health Scorecard, DORA Dashboard, Product Review, Growth Dashboard |
| **Solo + Review** | 1 creates → C reviews → I receives | ADR, Heuristic Eval, Tracking Plan, Tech Radar |

---

## Practical Cross-Functional Workflow Patterns (Round 5 Research)

### Pattern 1: Three Amigos + Example Mapping (BA ↔ ER ↔ PA)
**What**: Sesi 30-45 menit, 3 perspektif: Business (BA/PM), Development (ER), Testing (PA/QA).
**When**: 1-2 sprint sebelum development. Jika sesi >45 menit → fitur terlalu besar, decompose.
**How**: Gunakan Example Mapping (colored cards):
- 🟡 Yellow = Story | 🔵 Blue = Business rules | 🟢 Green = Concrete examples per rule | 🔴 Red = Open questions
**Output**: Gherkin scenarios (Given-When-Then) yang langsung masuk ke BA → user-story-bdd template.
**Impact**: Tim yang konsisten pakai teknik ini melaporkan pengurangan defect 80-90%.

### Pattern 2: Dual-Track Agile in Practice (PM ↔ UXR ↔ PR ↔ ER)
**What**: Discovery dan delivery berjalan paralel, bukan sequential.
**How**: 
- **Discovery Board** (Kanban): Ideas → Problem Validation → Solution Validation → Ready for Delivery
- **Delivery Board** (Scrum/Kanban): Backlog → Sprint → Review → Done
- Buffer: "Ready for Delivery" column = input ke delivery backlog
**Key Practice (Trustpilot)**: Validasi sebelum build — kirim 3,000 mockup email, ukur 52% open rate + 21% retention sebelum engineering build. Developer tanpa discovery work → bayar tech debt.
**Cadence**: Sprint planning cover BOTH tracks. Standup cover BOTH. Sprint review include discovery learnings + shipped features.
**Skill Mapping**: PR(research-plan) → UXR(prototype-test) → PM(feature-spec for validated ideas) → BA(use-case) → ER(adr) → PDS(sprint-plan)

### Pattern 3: DORA Metrics Implementation (PDS ↔ ER ↔ PA)
**What**: 4 key metrics + Reliability. Framing: improvement tool, bukan surveillance.
**Architecture Options**:
- Open source: Google Four Keys (webhook → BigQuery → DataStudio) atau Apache DevLake (Docker + Grafana)
- Platform-native: GitLab DORA dashboard, Datadog Software Delivery
- Commercial: LinearB (free, benchmarks from 8M+ PRs), Sleuth, Swarmia
**Benchmark**: Syngenta improved 50% → 98% DORA health scores in <6 months using LinearB.
**Skill Mapping**: PDS(dora-dashboard) + ER(system-design for pipeline) + PA(metric-definition)

### Pattern 4: Atomic UX Research Repository (UXR ↔ PR ↔ PM)
**What**: Break research into 4 atomic levels: Experiments → Facts → Insights → Recommendations
**How**: Each nugget links observation to tagged evidence (video clips, quotes, data). Searchable across studies.
**Tools**: Dovetail (43% adoption), Confluence/SharePoint (32%), Notion/Airtable (14%).
**Best Practices**: Make repo references part of design-to-dev handoffs. Schedule insight office hours. Track search success rate.
**Skill Mapping**: UXR(ux-findings,usability-test-report) → PR(insight-report,thematic-analysis) → PM(persona update, feature-spec informed by evidence)

### Pattern 5: Value Stream Mapping for Software Delivery (PDS ↔ ER ↔ PA)
**What**: Map happy path + recovery stream. Per step: Lead Time, Process Time, %Complete&Accurate.
**Key Insight**: Measurements need LOW precision — "common for some steps to take minutes while others take days."
**Real Results**: BDC Canada reduced pre-dev time 74%, QA time 81%. Newforma achieved 22× more frequent deliveries.
**7 Wastes (Poppendieck)**: Partially done work, extra features, relearning, handoffs, task switching, delays, defects.
**Skill Mapping**: PDS(vsm) + ER(system-design for bottleneck fix) + PA(metric-definition for flow metrics)

---

## Handoff Anti-Patterns & Real-World Org Models (Round 6 Research)

### Anti-Pattern 1: Lean Waterfall
**What**: Setiap skill/function pakai agile sendiri-sendiri, tapi antar skill tetap sequential handoff.
**Symptom**: "Everyone is working, yet nothing is done." High utilization, low throughput.
**Fix**: Vertical slicing — deliver end-to-end across skills dalam 1 sprint. Gunakan DDDI (Driver-Decider-Doers-Informed) per handoff.
**Orchestrator Rule**: Jangan sequence 5 skill berturut-turut. Parallelkan yang bisa. Minimize handoff points.

### Anti-Pattern 2: Tacit Knowledge Stripping
**What**: Setiap handoff kehilangan konteks implisit yang tidak terdokumentasi.
**Symptom**: Downstream skill harus tanya ulang pertanyaan yang sudah dijawab upstream.
**Fix**: SSOT (Project Context Canvas) sebagai shared context. Setiap handoff wajib include: acceptance criteria, context summary, escalation threshold.
**Orchestrator Rule**: Selalu reference SSOT di setiap prompt. Update SSOT setelah setiap deliverable.

### Real Org Models yang Bisa Diadopsi

| Organisasi | Model | Lesson untuk IDEAS |
|:---|:---|:---|
| **Gojek** | SWAT teams + floating specialists. Conway's Law as design principle | Core team per project (PM+BA+PDS) + floating specialists (UXR, PA, ER, DM) |
| **Grab** | 3-layer platform + X-as-a-Service | Skills = services with API contracts. Quality SLAs per skill output |
| **DBS Bank** | 700-person Data Chapter embedded in squads. Time-to-value: 12mo → 2-3mo | Data skills (DM+DAMA) embedded in project team, bukan siloed |
| **Bank Mandiri** | Federated DG + monthly User Group community | DAMA skills support + community of practice across projects |
| **UK GDS** | 12 defined roles, 4 phases (Discovery→Live) | Role composition changes per project phase |
| **Singapore GovTech** | Team Topologies + Forward Deployed Teams | Enabling teams embedded di klien untuk knowledge transfer |
| **Netflix** | Full Cycle Developer + Paved Road | Platform approach: reusable templates + conventions, not mandates |

### SAFe PI Planning Key Insight
- **50% of work discovered DURING planning**, not before
- Confidence vote: teams assess EACH OTHER's feasibility
- For orchestrator: structured planning session (ORCH-01 prompt) surfaces dependencies early
- Banking PI Planning lesson: intense coordination creates trust between siloed teams

---

## Skill Composability Principles (Round 7 Research: 90+ Sources)

### 12-Factor Agents Applied to 10 IDEAS Skills
Prinsip inti: "Agents are just software" — setiap skill harus diperlakukan sebagai software artifact.

| Principle | Application to IDEAS Skills |
|:---|:---|
| **Single Responsibility** | 1 skill = 1 domain. PM owns strategy, BA owns requirements, PA owns analytics. Tidak overlap |
| **Bounded Context (DDD)** | Setiap skill punya ubiquitous language sendiri. "Persona" di PM ≠ "research-persona" di PR |
| **Interface Contract** | Input/output setiap skill terdefinisi: SSOT sebagai shared context, deliverable templates sebagai output contract |
| **Progressive Disclosure** | Skill discovery: name+description saja. Activation: baca SKILL.md. Execution: load references/templates on demand |
| **Dependency Injection** | Skill bisa di-swap tanpa ubah orchestrator. Contoh: DM dan DAMA keduanya handle data governance — routing map menentukan kapan pakai yang mana |
| **Stateless Execution** | Setiap skill call berdiri sendiri. State dikelola di SSOT (Project Context Canvas), bukan di skill |
| **Composability** | Simple skills combine into complex workflows via 6 patterns: sequential, routing, parallel, orchestrator-workers, evaluator-optimizer, composition |

### Interface Protocols Antar Skill
| Protocol | Fungsi | Implementasi IDEAS |
|:---|:---|:---|
| **SSOT as Shared Context** | Setiap skill baca dari + tulis ke Project Context Canvas | `templates/project-context-canvas-template.md` |
| **Deliverable as Contract** | Output setiap skill = structured template dengan sections terdefinisi | 284 templates across 10 skills |
| **RASCI as Access Control** | Siapa boleh create/review/approve setiap deliverable | `cross-skill-integration.md` → RASCI table |
| **Gate as Quality Contract** | Output harus PASS quality criteria sebelum jadi input skill berikutnya | `bank-prompt.md` → QA-01, CHAIN-01 |

### Composability Patterns untuk IDEAS
```
Pattern 1 — Sequential Pipeline (paling umum):
  PM(PRD) →[gate]→ BA(SRS) →[gate]→ ER(system-design) →[gate]→ PDS(sprint-plan)

Pattern 2 — Parallel Fan-Out:
  PA(data analysis) || UXR(usability) || PR(market research) → PM(decision)

Pattern 3 — Routing (conditional):
  IF product → PM chain | IF data governance → DM+DAMA chain | IF SPBE → IDEAS chain

Pattern 4 — Evaluator-Optimizer:
  PM(PRD draft) → QA-01(review) → PM(revise) → QA-01(re-review) → PASS

Pattern 5 — Orchestrator-Workers:
  IDEAS(decompose project) → delegate to 5 skills simultaneously → synthesize results
```

---

## AI Governance for Multi-Skill Systems (Round 7)

### Governance Frameworks
| Framework | Scope | Key for IDEAS |
|:---|:---|:---|
| **NIST AI RMF** | Govern → Map → Measure → Manage | Risk assessment per skill output. GenAI Profile for LLM-specific risks |
| **ISO/IEC 42001** | 38 controls, 9 objectives, PDCA cycle | Certifiable AI management system. Microsoft sudah certified untuk Copilot |
| **EU AI Act** | Risk-based classification, fines up to 7% revenue | Multi-purpose AI agents assumed high-risk unless specific precautions taken |
| **UU PDP (Indonesia)** | Data protection, breach notification 3×24 jam | Setiap skill yang handle data pribadi harus comply |

### Human-in-the-Loop (HITL) Gates
**Rule**: Hard separation antara "propose" dan "commit." AI generates → Human reviews → Human approves → System executes.

| Trigger | Action | Contoh di IDEAS |
|:---|:---|:---|
| **Irreversible action** | Mandatory approval | Kirim proposal ke klien, submit tender LKPP |
| **High-value transaction** | Mandatory approval | Cost estimation > Rp 500jt, pricing decision |
| **Low-confidence output** | Request review | QA score < 4/5, deliverable pertama untuk klien baru |
| **Novel scenario** | Request review | Tipe project yang belum pernah ditangani |
| **Routine task** | Auto-proceed + spot check | Sprint plan update, SSOT refresh, internal draft |

### Audit Trail Requirements
Setiap deliverable yang di-generate harus record:
1. **Which skill** generated the output
2. **What SSOT version** was referenced
3. **What prompt** was used (with version)
4. **Who reviewed** and approved
5. **When** each step occurred
6. **What changes** were made post-generation

---

## Measuring Orchestrator Effectiveness (Round 7)

### 4-Tier Metrics Framework
| Tier | Metrics | Target |
|:---|:---|:---|
| **Quality** | Deliverable accuracy, completeness, MECE score, Pyramid compliance | QA-01 score ≥ 4/5 per dimension |
| **Efficiency** | Time-to-deliverable, revision count, prompt iterations needed | <3 revisions per deliverable |
| **Adoption** | Skills used per project, prompts used per week, SSOT completion rate | >80% projects have SSOT |
| **Business Impact** | Client satisfaction, proposal win rate, project delivery on-time | Win rate tracking per quarter |

### Token Waste Indicators
- **Regeneration rate**: Berapa kali output di-regenerate karena kualitas rendah? Target: <15%
- **Context bloat**: Berapa % context window terpakai oleh informasi non-esensial? Target: <30%
- **Abandoned outputs**: Berapa deliverable yang di-generate tapi tidak digunakan? Target: <10%
