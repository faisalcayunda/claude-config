# BA-01: BABOK v3 & IIBA Framework

## BABOK v3 — 6 Knowledge Areas
| KA | Focus | Key Tasks |
|:---|:---|:---|
| **BA Planning & Monitoring** | Plan BA approach | Plan approach, plan stakeholder engagement, plan governance, plan information mgmt, identify BA performance improvements |
| **Elicitation & Collaboration** | Gather information | Prepare for elicitation, conduct elicitation, confirm results, communicate BA info, manage stakeholder collaboration |
| **Requirements Life Cycle Mgmt** | Manage requirements | Trace requirements, maintain requirements, prioritize requirements, assess changes, approve requirements |
| **Strategy Analysis** | Define change strategy | Analyze current state, define future state, assess risks, define change strategy |
| **Requirements Analysis & Design Definition** | Shape solution | Specify & model requirements, verify requirements, validate requirements, define requirements architecture, define design options, analyze potential value |
| **Solution Evaluation** | Assess solution | Measure solution performance, analyze performance measures, assess solution limitations, assess enterprise limitations, recommend actions |

## BACCM — 6 Core Concepts
| Concept | Definition | Relationships |
|:---|:---|:---|
| **Change** | Controlled transformation in response to a Need | Driven by Need, produces Solution |
| **Need** | Problem or opportunity to be addressed | Creates Change, addressed by Solution |
| **Solution** | Way to satisfy Need within a Context | Addresses Need, delivers Value |
| **Stakeholder** | Individual/group with relationship to the Change | Has Needs, perceives Value |
| **Value** | Worth of Solution to Stakeholder | Determined by Stakeholder, delivered by Solution |
| **Context** | Circumstances influencing Change | Constrains/enables all other concepts |

## 50 Techniques (Key Selection)
Acceptance Criteria, Backlog Management, Balanced Scorecard, Brainstorming, Business Capability Analysis, Business Cases, Business Model Canvas, Business Rules Analysis, Collaborative Games, Concept Modelling, Data Dictionary, Data Flow Diagrams, Data Modelling, Decision Analysis, Decision Modelling, Document Analysis, Estimation, Financial Analysis, Focus Groups, Functional Decomposition, Interviews, Item Tracking, Lessons Learned, Metrics/KPIs, Mind Mapping, Non-Functional Requirements, Observation, Org Modelling, Prioritization, Process Analysis, Process Modelling, Prototyping, Reviews, Risk Analysis, Root Cause Analysis, Roles/Permissions Matrix, Scope Modelling, Sequence Diagrams, Stakeholder List/Map/Personas, State Modelling, Survey/Questionnaire, SWOT, Use Cases/Scenarios, User Stories, Vendor Assessment, Workshops

---

# BA-02: Requirements Engineering

## Requirements Classification
| Type | Description | Example |
|:---|:---|:---|
| **Business** | High-level needs of the organization | "Reduce customer onboarding time by 50%" |
| **Stakeholder** | Needs of specific stakeholder groups | "Sales team needs real-time inventory visibility" |
| **Solution — Functional** | What the system must do | "System shall calculate shipping cost based on weight and destination" |
| **Solution — Non-Functional** | Quality attributes and constraints | "Page load time < 2 seconds at 95th percentile" |
| **Transition** | Temporary capabilities for changeover | "Data migration from legacy system" |

## Elicitation Techniques (by effectiveness)
| Technique | Best For | Effort |
|:---|:---|:---|
| **Interviews** | Deep exploration, sensitive topics | Medium |
| **Workshops (JAD)** | Consensus building, complex requirements | High |
| **Observation** | Understanding actual (vs stated) processes | Medium |
| **Prototyping** | UI requirements, validating understanding | High |
| **Document Analysis** | Existing systems, regulations, policies | Low |
| **Surveys** | Large stakeholder groups, quantitative data | Low-Medium |
| **Brainstorming** | Generating ideas, early-stage exploration | Low |

## INVEST Criteria for User Stories (Cohn)
**I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable

## VOLERE Requirements Shell (Robertson/Robertson)
Requirement #, Type, Event/Use Case, Description, Rationale, Source, **Fit Criterion** (measurable acceptance), Priority, Conflicts, Supporting Materials, History

## Prioritization Methods
| Method | How | Best For |
|:---|:---|:---|
| **MoSCoW** | Must/Should/Could/Won't | Time-boxed delivery |
| **Kano Model** | Must-be/One-dimensional/Attractive/Indifferent/Reverse | Feature delight analysis |
| **100-Dollar Test** | Distribute $100 across requirements | Stakeholder voting |
| **Weighted Scoring** | Criteria × weights | Multi-criteria decisions |

---

# BA-03: Business Process Modeling

## BPMN 2.0 Core Elements
| Category | Elements |
|:---|:---|
| **Events** | Start (circle), Intermediate (double circle), End (thick circle) — Message, Timer, Error, Signal |
| **Activities** | Task (rounded rect), Sub-Process (+ marker), Call Activity |
| **Gateways** | Exclusive (X), Parallel (+), Inclusive (O), Event-based |
| **Flows** | Sequence Flow (→), Message Flow (- - →), Association (···→) |
| **Swimlanes** | Pool (organization), Lane (role/dept within pool) |
| **Artifacts** | Data Object, Data Store, Annotation, Group |

## SIPOC Template
**S**uppliers → **I**nputs → **P**rocess (high-level steps) → **O**utputs → **C**ustomers

## Process Improvement Approaches
| Approach | Focus | Key Tool |
|:---|:---|:---|
| **Lean** | Eliminate waste (7 wastes) | Value Stream Mapping |
| **Six Sigma** | Reduce variation | DMAIC (Define-Measure-Analyze-Improve-Control) |
| **BPR** | Radical redesign | Clean-sheet process design |
| **Process Mining** | Data-driven discovery | Event log analysis |

---

# BA-04: Stakeholder Analysis & Management

## Power/Interest Grid (Eden/Ackermann)
| | Low Interest | High Interest |
|:---|:---|:---|
| **High Power** | Keep Satisfied | **Manage Closely** |
| **Low Power** | Monitor | Keep Informed |

## Mitchell Salience Model
Three attributes: **Power** (ability to influence) × **Legitimacy** (appropriateness of claim) × **Urgency** (time sensitivity)
7 classes from Dormant (1 attribute) → Definitive (all 3)

## RACI Framework
| Role | Definition |
|:---|:---|
| **R** — Responsible | Does the work |
| **A** — Accountable | Final decision authority (one per task) |
| **C** — Consulted | Provides input (two-way communication) |
| **I** — Informed | Kept updated (one-way communication) |

---

# BA-05: Data Analysis & Modeling

## ER Diagram (Chen 1976)
Entity (rectangle) — Relationship (diamond) — Attribute (oval)
Cardinality: 1:1, 1:M, M:N

## Data Flow Diagram (DeMarco/Yourdon)
External Entity (rectangle) → Process (circle) → Data Store (open rectangle)
Levels: Context (Level 0) → Level 1 → Level 2 (decomposition)

## Data Dictionary Entry
| Field | Content |
|:---|:---|
| Data Element Name | [Unique identifier] |
| Alias/Synonym | [Alternative names] |
| Definition | [Business meaning] |
| Data Type | [String/Integer/Date/Boolean/etc.] |
| Length/Format | [Max length, mask] |
| Valid Values | [Range, enumeration, business rules] |
| Source | [System/process of origin] |
| Owner | [Business owner] |

## Decision Table Structure
| Condition 1 | Condition 2 | → Action |
|:---|:---|:---|
| Y | Y | Action A |
| Y | N | Action B |
| N | Y | Action C |
| N | N | Action D |
