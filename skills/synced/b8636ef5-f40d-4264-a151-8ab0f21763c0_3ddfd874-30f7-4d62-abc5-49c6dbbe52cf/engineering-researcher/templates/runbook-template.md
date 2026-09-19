# Runbook: [Service/Process Name]
## Owner: [Team] | Last Updated: [Date] | Review Cycle: [Quarterly]
## Service Overview
| Field | Value |
|:---|:---|
| Service | [Name] |
| Repository | [URL] |
| Dashboard | [URL] |
| On-call | [PagerDuty/OpsGenie rotation] |
| SLO | [e.g., 99.9% availability, p99 < 200ms] |
## Common Alerts & Response
### Alert: [Alert Name]
| Field | Value |
|:---|:---|
| Severity | [P1/P2/P3] |
| Trigger | [Condition that fires alert] |
| Impact | [What users experience] |
| Dashboard | [Link] |
**Diagnosis Steps:**
1. [Check X metric/dashboard]
2. [Verify Y service health]
3. [Check Z logs with query: `...`]
**Resolution Steps:**
1. [Step 1 with exact commands]
2. [Step 2]
**Escalation**: If not resolved in [X min], escalate to [team/person]
## Deployment
| Step | Command/Action |
|:---|:---|
| Deploy | [CI/CD pipeline URL or command] |
| Rollback | [Exact rollback command] |
| Verify | [Health check URL/command] |
## Dependencies
| Service | Type | Failure Impact |
|:---|:---|:---|
