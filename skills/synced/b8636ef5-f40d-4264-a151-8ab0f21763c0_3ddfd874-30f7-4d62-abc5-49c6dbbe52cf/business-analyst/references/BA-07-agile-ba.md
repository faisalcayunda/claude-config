# BA-06: Solution Assessment & Validation

## Business Case — Five Case Model (OGC/MSP)
| Case | Question | Content |
|:---|:---|:---|
| **Strategic** | Is there a compelling case? | Strategic fit, investment objectives |
| **Economic** | Does it provide VfM? | CBA, NPV, options analysis |
| **Commercial** | Is it commercially viable? | Procurement strategy, risk allocation |
| **Financial** | Is it affordable? | Funding, cash flow, budget impact |
| **Management** | Is it achievable? | Project plan, governance, change mgmt |

## Financial Analysis Methods
| Method | Formula | Use |
|:---|:---|:---|
| **NPV** | Σ [Cash Flow / (1+r)^t] | Time value of future benefits |
| **ROI** | (Benefits - Costs) / Costs × 100 | Simple return percentage |
| **IRR** | Rate where NPV = 0 | Compare investment alternatives |
| **Payback Period** | Time until cumulative benefits = costs | Liquidity / risk assessment |
| **TCO** | Purchase + Implementation + Operations + Decommission | Full lifecycle cost |

## Feasibility — TELOS Framework
| Dimension | Question |
|:---|:---|
| **Technical** | Can we build it with available technology? |
| **Economic** | Does the CBA justify investment? |
| **Legal** | Does it comply with regulations? |
| **Operational** | Will the organization adopt it? |
| **Schedule** | Can we deliver within the timeframe? |

## Benefits Realization (Bradley/Ward-Daniel)
Benefits Dependency Network: **Investment Objectives → Business Benefits → Business Changes → Enabling Changes → IT Enablers**
Track: planned benefits → realized benefits → delta analysis → corrective action

## UAT Approach (ISTQB)
Entry Criteria → Test Planning → Test Design → Test Execution → Defect Logging → Exit Criteria → Sign-off
Key: BA writes acceptance criteria, QA designs test cases from them, business users execute.

---

# BA-07: Agile BA Practices

## Story Mapping (Patton 2014)
```
User Activity:  [Login]     [Search]    [Purchase]   [Track Order]
                  |            |            |             |
User Tasks:    [Email]     [Keyword]    [Cart]       [Status]
               [SSO]       [Filter]     [Pay]        [History]
               [Reset]     [Sort]       [Confirm]    [Returns]
                  |            |            |             |
               Release 1 ─────────────────────────────────
               Release 2 ─────────────────────────────────
```
Backbone (top) = user activities. Walking skeleton = thinnest horizontal slice that delivers value.

## BDD Given-When-Then (North 2006)
```gherkin
Feature: [Feature name]
  As a [role]
  I want [goal]
  So that [benefit]

  Scenario: [Scenario name]
    Given [precondition / initial context]
    And [additional context]
    When [action / trigger]
    Then [expected outcome]
    And [additional outcome]
```

## Three Amigos Pattern
| Perspective | Role | Focus |
|:---|:---|:---|
| **Business** | BA / Product Owner | What problem does this solve? What are the acceptance criteria? |
| **Development** | Developer | How will we build this? What are the edge cases? |
| **Testing** | QA / Tester | How will we test this? What could go wrong? |
Output: Shared understanding, refined acceptance criteria, identified unknowns.

## Impact Mapping (Adzic 2012)
**Goal** → **Actors** (who can help/hinder?) → **Impacts** (how should their behavior change?) → **Deliverables** (what can we do to cause that impact?)

## Example Mapping
| Card Color | Content |
|:---|:---|
| **Yellow** | Story/Rule being discussed |
| **Blue** | Business rules discovered |
| **Green** | Concrete examples (Given-When-Then) |
| **Red** | Questions / unknowns to resolve |

---

# BA-08: BA Tools & Techniques

## SWOT Analysis
| | Helpful | Harmful |
|:---|:---|:---|
| **Internal** | **Strengths** | **Weaknesses** |
| **External** | **Opportunities** | **Threats** |

## PESTLE Analysis
**P**olitical, **E**conomic, **S**ocial, **T**echnological, **L**egal, **E**nvironmental

## Porter's Five Forces (1980)
1. Threat of New Entrants
2. Bargaining Power of Suppliers
3. Bargaining Power of Buyers
4. Threat of Substitutes
5. Industry Rivalry

## Root Cause Analysis Tools
| Tool | Method | Best For |
|:---|:---|:---|
| **Fishbone (Ishikawa)** | 6M categories: Man, Machine, Method, Material, Measurement, Mother Nature | Structured brainstorming |
| **5 Whys** | Ask "Why?" iteratively until root cause emerges | Quick, focused analysis |
| **Pareto (80/20)** | Rank causes by frequency/impact | Prioritizing which cause to fix first |

## Kano Model Categories
| Category | If Present | If Absent |
|:---|:---|:---|
| **Must-Be** | No satisfaction increase | High dissatisfaction |
| **One-Dimensional** | Satisfaction increases linearly | Dissatisfaction increases linearly |
| **Attractive (Delighter)** | High satisfaction | No dissatisfaction |
| **Indifferent** | No effect | No effect |
| **Reverse** | Dissatisfaction | Satisfaction |

---

# BA-09: Enterprise & Business Architecture

## TOGAF ADM — Phase B: Business Architecture
Inputs: Architecture Vision → Develop Baseline Business Architecture → Develop Target Business Architecture → Gap Analysis → Candidate Roadmap
Artifacts: Business Footprint Diagram, Functional Decomposition, Business Service/Information Diagram, Process/Event/Use-Case Catalogs

## BIZBOK v14 — Core Domains
| Domain | Content |
|:---|:---|
| **Capabilities** | What the business does (ability to achieve outcomes) |
| **Value Streams** | How the business delivers value end-to-end |
| **Information** | What information the business uses/creates |
| **Organization** | How the business is structured |
| **Strategies** | Where the business is heading |
| **Initiatives** | How the business executes change |

## Balanced Scorecard (Kaplan/Norton 1996)
Four perspectives: **Financial** (shareholder view) → **Customer** (value proposition) → **Internal Process** (operational excellence) → **Learning & Growth** (capabilities and culture)
Strategy Maps link objectives across perspectives with cause-effect arrows.

## Capability Mapping
Business Capability = stable representation of WHAT an organization does (not HOW)
Level 0 (Enterprise) → Level 1 (Domain) → Level 2 (Sub-domain) → Level 3 (Component)
Heat-map capabilities by: strategic importance, current maturity, investment level

---

# BA-10: Digital Transformation & Emerging BA

## AI/ML Requirements (New Requirement Types)
| Requirement Type | Example |
|:---|:---|
| **Data Requirements** | Training data volume, quality, labeling, bias mitigation |
| **Accuracy/Performance** | Precision/recall targets, acceptable false positive rate |
| **Explainability** | Model decisions must be interpretable by compliance team |
| **Fairness** | No demographic bias in lending decisions (within 5% parity) |
| **Drift Monitoring** | Alert when model accuracy drops below threshold |

## RPA Requirements Checklist
- [ ] Process is rule-based and repetitive
- [ ] Process involves structured data
- [ ] Process has stable, well-defined inputs/outputs
- [ ] Volume justifies automation investment
- [ ] Exception handling paths defined
- [ ] Human-in-the-loop triggers specified

## BA Role Evolution
| Traditional BA | Modern BA |
|:---|:---|
| Requirements document author | Product Trio collaborator |
| Gatekeeper between business and IT | Embedded in agile team |
| Waterfall phase deliverables | Continuous discovery |
| BRD/SRS focus | Story maps + BDD + prototypes |
| Project-scoped | Product-scoped |
