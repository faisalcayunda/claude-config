# ER-01: Software Architecture & System Design

## Domain-Driven Design (Evans 2003)
**Strategic Patterns**: Bounded Context, Context Map, Shared Kernel, Anti-Corruption Layer, Published Language
**Tactical Patterns**: Entity, Value Object, Aggregate, Repository, Domain Event, Domain Service, Factory
**Key Principle**: Ubiquitous Language — one model, one language per bounded context.

## Architecture Patterns (Richards/Ford 2020)
| Pattern | Coupling | Scalability | Simplicity | Best For |
|:---|:---|:---|:---|:---|
| **Monolith (layered)** | High | Low | High | Small teams, early stage |
| **Modular monolith** | Medium | Low-Med | Medium | Growing orgs, pre-microservices |
| **Microservices** | Low | High | Low | Large orgs, independent teams |
| **Event-driven** | Low | High | Low | Async workflows, decoupling |
| **Microkernel** | Medium | Medium | Medium | Plugin architectures |
| **Serverless** | Low | High | Medium | Event-triggered, variable load |

## CQRS + Event Sourcing (Young)
**CQRS**: Separate read model (optimized for queries) from write model (optimized for commands).
**Event Sourcing**: Store state changes as immutable event log. Current state = replay all events.
Use together when: Complex domain, audit requirements, temporal queries, multiple read projections.

## C4 Model (Brown)
Level 1: **System Context** — system + external actors/systems
Level 2: **Container** — applications, databases, message queues
Level 3: **Component** — internal components within containers
Level 4: **Code** — class/module level (rarely needed)

## ADR Format (Nygard / MADR)
**Status**: Proposed / Accepted / Deprecated / Superseded
**Context**: What forces are at play?
**Decision**: What is the change we're proposing?
**Consequences**: What becomes easier/harder?

---

# ER-02: DevOps, SRE & Platform Engineering

## Three Ways (Kim 2013)
1. **Flow**: Left-to-right flow from dev to ops to customer (reduce WIP, small batches)
2. **Feedback**: Right-to-left feedback at every stage (telemetry, alerts, review)
3. **Continual Learning**: Culture of experimentation, repetition, practice

## SRE Fundamentals (Google 2016)
| Concept | Definition |
|:---|:---|
| **SLI** | Service Level Indicator — quantitative measure (e.g., latency p99 < 200ms) |
| **SLO** | Service Level Objective — target for SLI (e.g., 99.9% of requests < 200ms) |
| **SLA** | Service Level Agreement — contract with consequences for missing SLO |
| **Error Budget** | 100% - SLO = budget for experimentation/velocity |
| **Toil** | Manual, repetitive, automatable operational work |
**Key principle**: When error budget is exhausted → slow down releases, fix reliability.

## Observability (Majors 2022)
Traditional monitoring: known-unknowns (dashboards, alerts for expected failures)
Observability: unknown-unknowns (explore any question with high-cardinality telemetry)
Three signals: **Traces** (request flow), **Metrics** (aggregated measures), **Logs** (discrete events)
Modern: structured events with **high cardinality** (user_id, request_id, build_sha) + **high dimensionality**.

## Platform Engineering
**Internal Developer Platform (IDP)**: Self-service capabilities reducing cognitive load on stream-aligned teams.
Backstage (Spotify): Software catalog, TechDocs, scaffolding templates, plugin ecosystem.
Key principle (Team Topologies): Platform team exists to reduce cognitive load of stream-aligned teams.

---

# ER-03: Cloud Architecture & Security

## AWS Well-Architected — 6 Pillars
1. **Operational Excellence**: Runbooks, IaC, observability
2. **Security**: IAM, detection, infrastructure protection, data protection
3. **Reliability**: Fault tolerance, recovery, scaling
4. **Performance Efficiency**: Right resource selection, monitoring
5. **Cost Optimization**: Expenditure awareness, right-sizing
6. **Sustainability**: Region selection, efficient algorithms

## STRIDE Threat Model (Shostack 2014)
| Threat | Violated Property | Example |
|:---|:---|:---|
| **S**poofing | Authentication | Stolen credentials |
| **T**ampering | Integrity | Modified data in transit |
| **R**epudiation | Non-repudiation | Deleted audit logs |
| **I**nformation Disclosure | Confidentiality | Data leak |
| **D**enial of Service | Availability | DDoS attack |
| **E**levation of Privilege | Authorization | Admin access exploit |

## Zero Trust (NIST SP 800-207)
Core principle: **"Never trust, always verify"** — every request authenticated/authorized regardless of network location.
Pillars: Identity-centric, micro-segmentation, least privilege, continuous verification, assume breach.

---

# ER-04: Engineering Metrics & Developer Experience

## DORA 4 Key Metrics (Forsgren/Humble/Kim 2018)
| Metric | Elite | High | Medium | Low |
|:---|:---|:---|:---|:---|
| **Deployment Frequency** | On-demand (multiple/day) | Daily-weekly | Weekly-monthly | Monthly-6monthly |
| **Lead Time for Changes** | <1 hour | 1 day-1 week | 1 week-1 month | 1-6 months |
| **Change Failure Rate** | 0-15% | 16-30% | 16-30% | 46-60% |
| **Time to Restore (MTTR)** | <1 hour | <1 day | 1 day-1 week | >6 months |

## SPACE Framework (Forsgren et al. 2021)
| Dimension | Example Metrics |
|:---|:---|
| **S**atisfaction | Developer satisfaction survey, NPS |
| **P**erformance | Code review quality, customer impact |
| **A**ctivity | PR throughput, deployments, commits |
| **C**ommunication | Knowledge sharing, review turnaround |
| **E**fficiency | Code review cycle time, CI wait time |
Key: Use metrics from ≥3 dimensions; no single metric captures productivity.

## DevEx Framework (Noda et al. 2023)
Three core dimensions: **Feedback Loops** (CI speed, code review turnaround), **Cognitive Load** (codebase complexity, documentation), **Flow State** (interruptions, deep work time).

---

# ER-05: Data Engineering & ML Engineering

## Data Engineering Lifecycle (Reis/Housley 2022)
Generation → Ingestion → Transformation → Serving (Analytics / ML / Reverse ETL)
**Undercurrents**: Security, Data Management, DataOps, Data Architecture, Orchestration, Software Engineering

## MLOps Maturity (Google 2020)
| Level | Characteristics |
|:---|:---|
| **L0: Manual** | Manual training, manual deployment, no CI/CD |
| **L1: ML Pipeline** | Automated training pipeline, CT (continuous training) |
| **L2: CI/CD + CT** | Full CI/CD for ML code + data + model, automated testing |

## Streaming vs Batch
| Dimension | Batch | Streaming |
|:---|:---|:---|
| Latency | Hours/days | Seconds/minutes |
| Complexity | Lower | Higher |
| Cost | Predictable | Variable |
| Best for | Reports, warehousing | Real-time features, alerts |
| Architecture | Lambda (both) → **Kappa** (streaming-only, Kreps) |
