# Architecture Review: [System/Feature]
## Date: [Date] | Reviewers: [Names]
## Review Type: [Design Review | Architecture Assessment | Pre-Launch]
## System Overview
[Brief description of system under review]
## Checklist
### Design Principles
- [ ] Single Responsibility per component/service
- [ ] Loose coupling between services
- [ ] Clear bounded contexts (DDD)
- [ ] Dependency direction follows Clean Architecture rules
### Reliability
- [ ] SLOs defined and measurable
- [ ] Failure modes identified and handled (Circuit Breaker, Retry, Timeout)
- [ ] No single points of failure
- [ ] Graceful degradation strategy
- [ ] Disaster recovery plan
### Security
- [ ] Threat model completed (STRIDE)
- [ ] Authentication/authorization appropriate
- [ ] Data encrypted at rest and in transit
- [ ] Input validation on all boundaries
- [ ] Secrets management (no hardcoded credentials)
### Observability
- [ ] Structured logging with correlation IDs
- [ ] Key metrics with dashboards
- [ ] Alerting with clear runbooks
- [ ] Distributed tracing enabled
### Scalability
- [ ] Horizontal scaling strategy defined
- [ ] Database scaling plan (read replicas, sharding)
- [ ] Caching strategy appropriate
- [ ] Load tested at 2-3x expected traffic
### Data
- [ ] Data model supports evolution (migrations)
- [ ] Backup and recovery tested
- [ ] Data retention policies defined
- [ ] PII handling compliant with regulations
## Findings
| # | Finding | Severity | Category | Recommendation |
|:---|:---|:---|:---|:---|
## Decision
[Approved / Approved with conditions / Needs redesign]
