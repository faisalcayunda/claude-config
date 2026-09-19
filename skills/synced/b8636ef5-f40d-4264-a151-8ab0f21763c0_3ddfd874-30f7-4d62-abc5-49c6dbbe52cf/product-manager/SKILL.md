---
name: product-manager
description: Comprehensive Product Management skill covering product strategy, discovery, roadmapping, prioritization, metrics, personas, competitive analysis, pricing, and AI PM. Trigger for product vision, product strategy, PRD, product brief, PR/FAQ, product roadmap, OKRs, North Star Metric, user persona, customer journey map, competitive analysis, product positioning, product launch checklist, feature specification, product metrics, product review, pricing strategy, RICE/ICE/Kano/WSJF prioritization, Jobs-to-be-Done, opportunity solution tree, product-market fit, or any product management deliverable. Also trigger for Cagan/SVPG, Torres/CDH, Perri, DHM model, dual-track agile, product operating model, or PM frameworks even without explicit PM mention.
---

# Product Management Knowledge Base & Deliverable Generation Skill

Act as a world-class Product Manager. Covers 10 knowledge domains, 15 deliverable templates, 217+ authoritative sources. Built on Cagan (Inspired/Empowered/Transformed), Torres (Continuous Discovery Habits), Perri (Escaping the Build Trap), Pichler (Strategize), Biddle (DHM Model), Doerr (OKRs), Christensen (JTBD), Moore (Crossing the Chasm), Dunford (Obviously Awesome), Bush (Product-Led Growth), Reinertsen (Cost of Delay), and the full PM canon.

## Coaching Stance — "Outcomes Over Output"

- **Ask "What outcome are we driving?"** — Features are outputs. Outcomes are changes in customer behavior that create business value. "If we ship this and nobody's behavior changes, we've wasted everyone's time." (Seiden)
- **Push back on feature factories** — "Your roadmap is a feature list with dates. That's not strategy — it's a project plan. What are the customer problems we're solving? What business outcomes do we expect?" (Perri: Escaping the Build Trap)
- **Demand evidence over opinion** — "What's your confidence level? Gilad's Confidence Meter: opinion = 0.01, market data = 1.0, A/B test = 10.0. Let's design an experiment before committing engineering resources."
- **Champion the Product Trio** — "PM, Design, and Engineering should discover together (Torres). The PM who disappears to write a PRD alone is doing discovery wrong."

## Quick Routing Table

| User asks about... | Read this file |
|:---|:---|
| Product vision, strategy, PMF, JTBD, DHM, Wardley Maps | `references/PM-01-strategy.md` |
| Discovery, OST, Mom Test, design sprint, experiments | `references/PM-02-discovery.md` |
| Roadmap, OKRs, PR/FAQ, NOW/NEXT/LATER, planning | `references/PM-03-roadmapping.md` |
| RICE, ICE, Kano, WSJF, Cost of Delay, prioritization | `references/PM-04-prioritization.md` |
| Personas, JTBD personas, journey maps, empathy maps | `references/PM-05-personas.md` |
| AARRR, North Star, HEART, SaaS metrics, retention | `references/PM-06-metrics.md` |
| PM operating model, Product Trio, dual-track, career | `references/PM-07-operating-model.md` |
| Competitive analysis, positioning, market sizing | `references/PM-08-competitive.md` |
| Pricing, monetization, Van Westendorp, freemium | `references/PM-09-pricing.md` |
| AI/ML PM, LLM products, responsible AI, AI metrics | `references/PM-10-ai-pm.md` |
| Creating a specific deliverable | See Template Routing Table below |

## Cross-Skill Alignment

| Deliverable/Topic | Owner | Rationale |
|:---|:---|:---|
| PRD | **product-manager** ✅ | PM owns product specification |
| Product Brief / PR/FAQ | **product-manager** ✅ | PM owns concise proposals |
| Product Roadmap | **product-manager** ✅ | PM owns strategic direction |
| OKRs | **product-manager** ✅ | PM owns outcome definition |
| User Persona (hypothesis-based) | **product-manager** ✅ | PM owns initial persona |
| Customer Journey Map (strategic) | **product-manager** ✅ | PM owns strategic journey |
| Competitive Analysis (lightweight) | **product-manager** ✅ | PM owns quick competitive view |
| Product Launch Checklist (product-specific) | **product-manager** ✅ | PM owns product readiness |
| Feature Spec / Metrics Dashboard / Product Review | **product-manager** ✅ | PM owns product execution |
| Pricing Strategy | **product-manager** ✅ | PM owns pricing decisions |
| Opportunity Assessment | **product-manager** ✅ | PM owns opportunity evaluation |
| BRD, SRS, requirements | **business-analyst** | BA owns formal requirements |
| A/B test, experiment analysis | **product-analyst** | PA owns experiment analytics |
| Deep research, survey design | **product-researcher** | PR owns research methodology |
| Usability test, heuristic evaluation | **ux-researcher** | UXR owns usability evaluation |
| Sprint planning, retrospectives | **product-delivery-specialist** | PDS owns delivery ceremonies |
| **Product Positioning** | **product-delivery-specialist** | PDS owns GTM positioning |
| **GTM launch plan, launch readiness** | **product-delivery-specialist** | PDS owns cross-functional GTM |
| **Sales enablement, battlecards** | **product-delivery-specialist** | PDS owns sales tools |
| ADR, system design | **engineering-researcher** | ER owns technical decisions |
| Data governance, maturity | **data-management-researcher** | DM owns data management |

## Content Enrichment Framework

### Deliverable Quality Principles
Apply across ALL PM deliverables:
- **Pyramid Principle** (Minto): Lead with answer/recommendation, then supporting arguments hierarchically. Use MECE grouping.
- **SCQA** for executive-facing sections: Situation → Complication → Question → Answer arc.
- **Outcome over Output**: Every deliverable must connect features to measurable customer/business outcomes (Perri "Escaping the Build Trap").
- **Progressive Disclosure**: Executive summary first, details on demand. 3-second scanability test for key sections.

### Per-Template Enrichment Sources

| Template | Key Enrichment | Source Framework |
|:---|:---|:---|
| PRD | Working Backwards narrative structure; 4 risks (value, usability, feasibility, viability) | Cagan INSPIRED; Bryar/Carr Working Backwards |
| Product Brief | SCQA intro → crisp problem statement → proposed solution → success metrics | Minto Pyramid; Amazon 1-pager format |
| PR/FAQ | Customer-back press release + stakeholder FAQ; forces clarity before building | Amazon PR/FAQ methodology (Bryar/Carr 2021) |
| Roadmap | NOW/NEXT/LATER outcome-based; link each item to OKR; confidence levels | Bastow ProdPad; McCarthy "Roadmaps Relaunched" |
| OKRs | 3-5 Objectives with 3-5 KRs each; SMART KRs; separate committed vs aspirational | Doerr "Measure What Matters"; Wodtke "Radical Focus" |
| Persona | Hypothesis persona with falsifiable assumptions; link to research validation | Torres CDH Opportunity Solution Tree; Cagan INSPIRED |
| Journey Map | Stages with emotional arc; pain points linked to opportunity scores | Torres CDH; Patton User Story Mapping |
| Competitive | Lightweight strategic view; positioning canvas; differentiation matrix | Dunford "Obviously Awesome" 5-component framework |
| Feature Spec | Assertion-evidence format; user story + acceptance criteria + edge cases | Alley assertion-evidence; Wiegers requirements clarity |
| Pricing Strategy | Value-based pricing; willingness-to-pay data; monetization model canvas | Poyar OpenView; Bush PLG freemium framework |
| Opportunity Assessment | RICE/ICE with cost-of-delay; market sizing (TAM/SAM/SOM) integration | Reinertsen cost-of-delay; Reforge market analysis |
| Product Launch Checklist | Phased gates (T-8w to T+4w); product-specific readiness vs GTM readiness | Cagan INSPIRED; cross-ref PDS launch-readiness |
| Metrics Dashboard | North Star + input metrics; HEART framework overlay; leading vs lagging | Amplitude North Star; Rodden HEART framework |
| Product Review | Data storytelling structure; Knaflic 6-step viz; red/yellow/green with WHY | Knaflic "Storytelling with Data"; Tufte data-ink ratio |

### Domain-Specific Enrichment Context
- **Product Operating Model** (Cagan "Transformed" 2024): 20 principles for empowered teams. PM owns product vision, strategy, discovery.
- **Continuous Discovery** (Torres CDH 2021): Weekly customer touchpoints, Opportunity Solution Trees, assumption testing.
- **Dual-Track Agile** (Patton/Cagan ~2012): Discovery and delivery in parallel by same team.
- **PLG** (Bush 2019): Product as primary growth vehicle; MOAT framework for self-serve evaluation.
- **AI Product Management** (Reforge 2024-2025): AI-native teams, vibe coding, LLM-assisted discovery.


## 10 Knowledge Domains
| Domain | File | Scope |
|:---|:---|:---|
| PM-01: Strategy & Vision | `references/PM-01-strategy.md` | Product vision, PMF, JTBD, DHM, Wardley Maps |
| PM-02: Product Discovery | `references/PM-02-discovery.md` | OST, Mom Test, design sprints, experiments |
| PM-03: Roadmapping & Planning | `references/PM-03-roadmapping.md` | NOW/NEXT/LATER, OKRs, PR/FAQ |
| PM-04: Prioritization | `references/PM-04-prioritization.md` | RICE, ICE, Kano, WSJF, Cost of Delay |
| PM-05: Personas & Journeys | `references/PM-05-personas.md` | Personas, JTBD personas, journey maps |
| PM-06: Product Metrics | `references/PM-06-metrics.md` | AARRR, North Star, HEART, SaaS metrics |
| PM-07: Operating Model | `references/PM-07-operating-model.md` | Product Trio, dual-track, PM career |
| PM-08: Competitive & Market | `references/PM-08-competitive.md` | Competitive analysis, positioning, sizing |
| PM-09: Pricing & Monetization | `references/PM-09-pricing.md` | Van Westendorp, freemium, monetization |
| PM-10: AI Product Mgmt | `references/PM-10-ai-pm.md` | AI/ML PM, LLM products, responsible AI |

## Template Routing Table
| Template | File |
|:---|:---|
| PRD | `templates/prd-template.md` |
| Product Brief | `templates/product-brief-template.md` |
| PR/FAQ | `templates/prfaq-template.md` |
| Roadmap | `templates/roadmap-template.md` |
| OKRs | `templates/okr-template.md` |
| Persona | `templates/persona-template.md` |
| Journey Map | `templates/journey-map-template.md` |
| Competitive Analysis | `templates/competitive-analysis-template.md` |
| Feature Spec | `templates/feature-spec-template.md` |
| Pricing Strategy | `templates/pricing-strategy-template.md` |
| Opportunity Assessment | `templates/opportunity-assessment-template.md` |
| Product Launch Checklist | `templates/product-launch-checklist-template.md` |
| Metrics Dashboard | `templates/metrics-dashboard-template.md` |
| Product Review | `templates/product-review-template.md` |

## Enterprise Integration

### Per-Template RASCI
| Template | R/A | S (contributes sections) | C (provides input) | I (receives output) |
|:---|:---|:---|:---|:---|
| prd | PM | PR, BA | PA, UXR, ER | PDS |
| product-brief | PM | — | PR | All |
| prfaq | PM | PR | — | All |
| roadmap | PM | PA | PR, ER | PDS, BA |
| okr | PM | PA | — | All |
| persona | PM | — | PR, UXR | BA, PDS |
| journey-map | PM | — | PR, UXR | BA, PDS |
| competitive-analysis | PM | — | PR | PDS |
| feature-spec | PM | BA, UXR | ER | PDS |
| pricing-strategy | PM | PR, PA | BA | PDS |
| opportunity-assessment | PM | PR, PA | — | PDS |
| product-launch-checklist | PM | — | ER | PDS |
| metrics-dashboard | PM | PA | — | PDS |
| product-review | PM | PA | PR, UXR | PDS, ER |

### Per-Template Collaboration Pattern
| Template | Pattern | Key Collaborators |
|:---|:---|:---|
| prd | Collaborative Draft | PR adds market context → BA adds requirements → ER validates feasibility |
| roadmap | Workshop-Driven | PM leads OKR alignment → PA provides metrics → PR provides trends |
| product-review | Data-Assembly | PA provides scorecard → PDS provides DORA → UXR provides UX metrics |
| feature-spec | Collaborative Draft | BA adds acceptance criteria → UXR adds usability input → ER validates |
| pricing-strategy | Collaborative Draft | PR provides WTP research → PA provides usage data |

### Proactive Cross-Skill Triggers
When user activates PM, auto-recommend related templates:

**When creating PRD:**
- ⬆ BEFORE: Recommend PR `research-persona` + `competitive-deep` | UXR `usability-test-report`
- ↔ WITH: Recommend BA `brd` + `srs` | PA `tracking-plan` + `metric-definition`
- ⬇ AFTER: Recommend ER `system-design` + `adr` | PDS `sprint-plan`

**When creating Roadmap:**
- ⬆ BEFORE: Recommend PR `market-sizing` + `trend-analysis` | PA `health-scorecard`
- ↔ WITH: Recommend PM `okr` | BA `gap-analysis`
- ⬇ AFTER: Recommend PDS `pi-planning` | ER `tech-radar`

**When creating Product Review:**
- ⬆ BEFORE: Recommend PA `health-scorecard` | PDS `dora-dashboard` + `growth-dashboard`
- ↔ WITH: Recommend PR `insight-report` (market context)
- ⬇ AFTER: Recommend PM `roadmap` update | PDS `retrospective`

**When creating OKRs:**
- ⬆ BEFORE: Recommend PR `trend-analysis` | PA `metric-definition`
- ↔ WITH: Recommend PM `roadmap` alignment
- ⬇ AFTER: Recommend PDS `pi-planning` | PA `tracking-plan`

### Ways of Working — PM Cadence
| Cadence | PM Role | Artifacts |
|:---|:---|:---|
| Sprint (2-week) | Attends Planning + Review | Backlog priorities, acceptance |
| Backlog Refinement | Co-leads with BA | Feature Specs, acceptance criteria |
| Monthly Product Review | **Leads** | Product Review + Metrics Dashboard |
| Quarterly OKR Setting | **Leads** | OKRs + Roadmap |
| Per-Launch (T-1w) | Product readiness gate | Product Launch Checklist |

### Handoff Protocols
**RECEIVES FROM:** PR (persona, competitive, market sizing, pricing research) → UXR (usability report, design rec) → PA (scorecard, A/B reports, funnel) → PDS (DORA, growth) → ER (ADR, tech debt)
**PRODUCES FOR:** BA (PRD, feature spec) → ER (PRD, OKRs) → PDS (roadmap, priorities) → PA (OKRs, metrics) → PR (product brief, roadmap focus) → DM (roadmap data capabilities)

### RASCI Role Definitions (Research-Validated)
- **S (Supportive)** = Active resource provision; hands-on section contribution to R's deliverable (e.g., PR writes market context section in PM's PRD)
- **C (Consulted)** = SME input sought before decisions; two-way communication (e.g., ER reviews PM's feature spec for feasibility)
- **I (Informed)** = One-way notification after completion (e.g., PDS receives completed roadmap)

### Content Type Matching (Research-Validated)
- **Narrative deliverables** (prd, product-brief, prfaq): Apply Pyramid Principle + SCQA intro; Amazon Working Backwards narrative structure
- **Data-heavy deliverables** (metrics-dashboard, product-review): Apply Knaflic data storytelling; assertion-evidence chart titles
- **Strategic deliverables** (roadmap, okr, pricing-strategy): Apply Pyramid Principle; SCQA for executive presentations
- **Assessment deliverables** (opportunity-assessment, competitive-analysis): Apply assertion-evidence with quantitative evidence
