# Performance Benchmark Report: [System/Feature]
## Author: [Name] | Date: [Date] | Environment: [Staging/Production]
## Test Configuration
| Parameter | Value |
|:---|:---|
| Tool | [k6 / Gatling / Locust] |
| Duration | [X minutes] |
| Virtual users | [Ramp: X → Y over Z min] |
| Target | [URL / Service] |
| Infrastructure | [Instance types, replicas, region] |
## Scenarios Tested
| Scenario | User Pattern | Expected RPS |
|:---|:---|:---|
| Normal load | [Steady state] | [X RPS] |
| Peak load | [2-3x normal] | [Y RPS] |
| Stress test | [Find breaking point] | [Max RPS] |
## Results
### Summary
| Metric | Normal | Peak | Stress | Target | Status |
|:---|:---|:---|:---|:---|:---|
| RPS achieved | [X] | [Y] | [Z] | [Target] | ✅/❌ |
| p50 latency | [Xms] | [Yms] | [Zms] | [<Xms] | |
| p95 latency | [Xms] | | | | |
| p99 latency | [Xms] | | | | |
| Error rate | [X%] | [Y%] | [Z%] | [<1%] | |
| CPU utilization | [X%] | | | [<80%] | |
| Memory utilization | [X%] | | | [<80%] | |
## Bottlenecks Identified
| # | Bottleneck | Component | Impact | Recommendation |
|:---|:---|:---|:---|:---|
## Capacity Recommendation
[Based on results, recommended scaling configuration for target load]
