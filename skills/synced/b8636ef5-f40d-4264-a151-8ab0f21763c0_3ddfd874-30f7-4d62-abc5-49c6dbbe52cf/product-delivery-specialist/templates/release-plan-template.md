# Release Plan: [Release Name/Version]
## Target Date: [Date] | Release Manager: [Name]
## Release Overview
| Field | Value |
|:---|:---|
| Version | [X.Y.Z] |
| Type | [Major / Minor / Patch] |
| Scope | [Features included] |
| Deployment strategy | [Blue-green / Canary / Rolling / Feature flags] |
## Feature Manifest
| Feature | Status | Flag | Rollout % | Owner |
|:---|:---|:---|:---|:---|
| [Feature A] | [Ready/In Progress] | [Flag name] | [100%/Canary] | [Name] |
## Release Checklist
### Pre-Release
- [ ] All features meet Definition of Done
- [ ] Performance testing passed (p99 < [X]ms at [Y] RPS)
- [ ] Security review completed
- [ ] Rollback procedure tested
- [ ] Runbooks updated
### Release Day
- [ ] Deploy to canary ([X]% traffic)
- [ ] Monitor SLOs for [30 min]
- [ ] Progressive rollout to [50%] → [100%]
- [ ] Verify feature flags operational
### Post-Release
- [ ] Monitor error rates for [24 hours]
- [ ] Confirm customer-facing docs live
- [ ] Send release notes to stakeholders
- [ ] Release retrospective scheduled
## Rollback Plan
| Trigger | Action | Owner | RTO |
|:---|:---|:---|:---|
| Error rate > [X%] | [Automated rollback / manual] | [Name] | [< X min] |
