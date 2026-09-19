# A/B Test Report: [Experiment Name]
## ID: [EXP-NNN] | Author: [Name] | Date: [Date]
## Executive Summary
**Result**: [Won / Lost / Inconclusive] — [One sentence: what we tested and what happened]
## Test Configuration
| Parameter | Value |
|:---|:---|
| Duration | [Start] – [End] ([N] days) |
| Sample Size | Control: [N] / Treatment: [N] |
| SRM Check | [Pass ✅ / Fail ❌] (p-value: [X]) |
## Results
| Metric | Type | Control | Treatment | Δ (abs) | Δ (%) | p-value | CI (95%) | Significant? |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| [Primary] | OEC | [X] | [Y] | [Δ] | [X%] | [p] | [low, high] | ✅/❌ |
| [Guardrail 1] | Guard | [X] | [Y] | [Δ] | [X%] | [p] | [low, high] | Safe ✅/⚠️ |
| [Secondary] | Explore | [X] | [Y] | [Δ] | [X%] | [p] | [low, high] | — |
## Segment Analysis
| Segment | Control | Treatment | Δ (%) | Significant? | Notes |
|:---|:---|:---|:---|:---|:---|
| [New users] | [X] | [Y] | [X%] | ✅/❌ | [Observation] |
| [Power users] | [X] | [Y] | [X%] | ✅/❌ | [Simpson's paradox check] |
## Interpretation & Learning
[What did we learn? Why did we see this result? What does it mean for the product?]
## Decision
**Action**: [Ship / Iterate / Kill]
**Rationale**: [Why this decision based on the data]
## Follow-up
| Action | Owner | Timeline |
|:---|:---|:---|
