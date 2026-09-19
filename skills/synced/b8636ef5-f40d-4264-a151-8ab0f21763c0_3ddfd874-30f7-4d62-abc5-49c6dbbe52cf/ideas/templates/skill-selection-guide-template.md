# Skill Selection Guide — Panduan Pemilihan Skill per Fase Project
# Skill Selection Guide — Skill Selection per Project Phase

> Gunakan panduan ini untuk menentukan kombinasi skill berdasarkan tipe + fase project.

---

## Step 1: Identifikasi Tipe Project

| Tipe | Skill Inti | Skill Pendukung | Panduan # |
|:---|:---|:---|:---|
| Product Development | PM, BA, ER, PDS | PR, UXR, PA | Panduan 1 |
| Data Governance | DM, DAMA, BA | ER, PDS, IDEAS | Panduan 2 |
| SPBE/Digital Transformation | IDEAS, DM, DAMA | BA, ER, PDS | Panduan 3 |
| Analytics & Experimentation | PA, PM, ER | BA, PR | Panduan 4 |
| Competitive & Market Entry | PR, PDS, PM | PA, UXR | Panduan 5 |
| Requirements Engineering | BA, PM, ER | PR, UXR | Panduan 6 |
| UX Research Program | UXR, PR, PM | BA, PA | Panduan 7 |
| Technical Architecture | ER, DM, BA | PM, PDS | Panduan 8 |
| Agile Delivery | PDS, PM, BA | ER, PA | Panduan 9 |
| IDEAS Proposal | IDEAS, BA, DM | DAMA, PM | Panduan 10 |

---

## Step 2: Tentukan Fase → Skill → Template

### FASE 1 — DISCOVER
| Aktivitas | Skill | Template | Priority |
|:---|:---|:---|:---|
| Project Context | `/ideas` | project-context-canvas | P0 |
| Market Research | `/product-researcher` | research-plan, market-sizing | P0 |
| User Interviews | `/product-researcher` | interview-guide | P0 |
| Competitive Intel | `/product-researcher` | competitive-deep | P1 |
| Competitive UX | `/ux-researcher` | competitive-ux | P1 |
| Stakeholder Map | `/business-analyst` | stakeholder | P0 |
| Maturity Assess | `/data-management-researcher` | maturity-assessment | P0 (data) |
| SPBE Baseline | `/ideas-company` | SPBE framework | P0 (gov) |

### FASE 2 — DEFINE
| Aktivitas | Skill | Template | Priority |
|:---|:---|:---|:---|
| Product Brief/PRD | `/product-manager` | product-brief, prd | P0 |
| Business Req | `/business-analyst` | brd | P0 |
| System Req | `/business-analyst` | srs, frs, nfr | P0 |
| Use Cases | `/business-analyst` | use-case, user-story-bdd | P0 |
| System Design | `/engineering-researcher` | system-design, adr | P0 |
| Data Architecture | `/data-management-researcher` | architecture-blueprint | P1 |
| Analytics Setup | `/product-analyst` | tracking-plan, metric-definition | P1 |
| DG Charter | `/dama-research` | KA-01 governance charter | P0 (data) |

### FASE 3 — BUILD
| Aktivitas | Skill | Template | Priority |
|:---|:---|:---|:---|
| Sprint Planning | `/product-delivery-specialist` | sprint-plan | P0 |
| Release Planning | `/product-delivery-specialist` | release-plan | P0 |
| Test Strategy | `/engineering-researcher` | test-strategy | P1 |
| UAT Planning | `/business-analyst` | uat-plan | P1 |
| Usability Test | `/ux-researcher` | usability-test-plan | P1 |
| DORA Monitor | `/product-delivery-specialist` | dora-dashboard | P2 |

### FASE 4 — LAUNCH
| Aktivitas | Skill | Template | Priority |
|:---|:---|:---|:---|
| GTM Plan | `/product-delivery-specialist` | gtm-launch | P0 |
| Positioning | `/product-delivery-specialist` | positioning | P0 |
| Readiness | `/product-delivery-specialist` | launch-readiness | P0 |
| Sales Tools | `/product-delivery-specialist` | sales-enablement, battlecard | P1 |
| Launch Metrics | `/product-analyst` | health-scorecard | P0 |
| A11y Audit | `/ux-researcher` | accessibility-audit | P1 |
| Runbook | `/engineering-researcher` | runbook | P0 |

### FASE 5 — OPTIMIZE
| Aktivitas | Skill | Template | Priority |
|:---|:---|:---|:---|
| Product Review | `/product-manager` | product-review | P0 |
| Funnel Analysis | `/product-analyst` | funnel-analysis | P0 |
| Cohort Retention | `/product-analyst` | cohort-retention | P0 |
| A/B Testing | `/product-analyst` | experiment-design | P1 |
| Win/Loss | `/product-researcher` | win-loss | P1 |
| Retrospective | `/product-delivery-specialist` | retrospective | P0 |
| Growth Dashboard | `/product-delivery-specialist` | growth-dashboard | P1 |

---

## Step 3: 5 Contoh Kombinasi Project / 5 Example Combinations

### Contoh A: Portal Data Pemda (6 bulan, Rp 2M)
```
DISCOVER: IDEAS(SPBE) + PR(research-plan) + BA(stakeholder)
DEFINE: PM(PRD) + BA(BRD,SRS) + DM(data-strategy) + DAMA(KA-01)
BUILD: ER(system-design) + PDS(sprint-plan) + PA(tracking-plan)
LAUNCH: PDS(gtm-launch) + IDEAS(training-material)
OPTIMIZE: PA(health-scorecard) + PM(product-review)
Total deliverables: ~20 | Skills: 8/10
```

### Contoh B: Data Governance Enterprise (12 bulan, Rp 3M)
```
DISCOVER: DM(maturity-assessment) + DAMA(KA-14)
DEFINE: DM(data-strategy) + DAMA(KA-01 charter) + BA(stakeholder,raci)
BUILD: DAMA(KA-02,KA-11) + ER(system-design) + PDS(sprint-plan)
LAUNCH: PDS(change-management,onboarding-playbook)
OPTIMIZE: PA(health-scorecard) + DM(maturity re-assessment)
Total deliverables: ~15 | Skills: 6/10
```

### Contoh C: SaaS Feature Launch (3 bulan, self-funded)
```
DISCOVER: PR(interview-guide,competitive-deep) + PA(funnel-analysis)
DEFINE: PM(prfaq,feature-spec) + BA(use-case,user-story-bdd)
BUILD: ER(adr) + PDS(sprint-plan) + PA(experiment-design)
LAUNCH: PDS(launch-readiness) + PA(ab-test-report)
OPTIMIZE: PA(feature-adoption,cohort-retention) + PM(product-review)
Total deliverables: ~12 | Skills: 6/10
```

### Contoh D: SPBE Improvement (18 bulan, Rp 5M)
```
DISCOVER: IDEAS(SPBE baseline,service-rec) + DM(maturity-assessment) + DAMA(KA-14)
DEFINE: BA(gap-analysis) + DM(data-strategy,architecture-blueprint) + DAMA(KA-01,KA-02)
BUILD: DAMA(KA-05,KA-09,KA-11) + ER(system-design) + PDS(sprint-plan,release-plan)
LAUNCH: IDEAS(policy-framework,technical-proposal) + PDS(change-management)
OPTIMIZE: PA(health-scorecard) + DM(maturity re-assessment) + IDEAS(assessment-report)
Total deliverables: ~25 | Skills: 8/10
```

### Contoh E: Product-Led Growth (6 bulan)
```
DISCOVER: PR(pmf-analysis,survey-design) + PA(funnel-analysis,segmentation)
DEFINE: PM(pricing-strategy,persona,journey-map) + PA(tracking-plan,metric-definition)
BUILD: PA(experiment-design) + UXR(usability-test-plan,prototype-test) + PDS(sprint-plan)
LAUNCH: PDS(onboarding-playbook,growth-dashboard) + PM(product-launch-checklist)
OPTIMIZE: PA(cohort-retention,ab-test-report,feature-adoption) + PR(win-loss)
Total deliverables: ~18 | Skills: 6/10
```
