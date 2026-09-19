# System Design Document: [System Name]
## Author: [Name] | Date: [Date] | Version: [1.0]
## 1. Overview
[What the system does, why it exists, key constraints]
## 2. Requirements
### Functional
| # | Requirement | Priority |
|:---|:---|:---|
### Non-Functional (Quality Attributes)
| Attribute | Requirement | Measure |
|:---|:---|:---|
| Performance | [e.g., p99 < 200ms] | [Load test] |
| Availability | [e.g., 99.9%] | [SLO monitoring] |
| Scalability | [e.g., 10K→100K users] | [Load testing] |
## 3. Architecture
### System Context (C4 Level 1)
[Diagram: system + actors + external dependencies]
### Container Diagram (C4 Level 2)
[Diagram: applications, databases, queues, caches]
### Component Diagram (C4 Level 3) — for complex containers
[Internal component breakdown]
## 4. Data Model
[Entity relationships, key schemas, data flow]
## 5. API Design
[Key endpoints, request/response formats]
## 6. Infrastructure
[Cloud services, deployment topology, IaC references]
## 7. Security
[Authentication, authorization, data encryption, threat model reference]
## 8. Observability
[Key metrics, dashboards, alerts, SLIs]
## 9. Trade-offs & Decisions
[Key ADRs or decisions made during design]
## 10. Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|:---|:---|:---|:---|
