# Experiment Design: [Experiment Name]
## ID: [EXP-NNN] | Author: [Name] | Date: [Date]
## 1. Hypothesis
**If** we [change/intervention],
**Then** [metric] will [direction] by [magnitude],
**Because** [rationale/mechanism].
## 2. Metrics
| Type | Metric | Current | MDE | Direction |
|:---|:---|:---|:---|:---|
| **Primary (OEC)** | [Main metric] | [Baseline] | [Min meaningful change] | ↑ |
| **Guardrail** | [Must not degrade] | [Baseline] | [Threshold] | ≥ |
| **Secondary** | [Supporting insight] | [Baseline] | [Exploratory] | ↑ |
## 3. Sample Size & Duration
| Parameter | Value |
|:---|:---|
| Statistical significance (α) | 0.05 |
| Power (1-β) | 0.80 |
| Baseline conversion/value | [X%] |
| MDE (absolute or relative) | [X% relative] |
| **Required sample per variant** | **[N]** |
| Daily eligible traffic | [N] |
| **Estimated duration** | **[N days]** (min 2 full weeks) |
| Variance reduction | [CUPED: Yes/No] |
## 4. Design
| Element | Detail |
|:---|:---|
| Variants | Control (current) vs Treatment (change) |
| Randomization unit | User / Session / Device |
| Allocation | 50/50 |
| Targeting | [All users / Segment] |
| Exclusions | [Other running experiments] |
## 5. Risks & Mitigations
| Risk | Mitigation |
|:---|:---|
| Novelty effect | Run ≥ 2 weeks, check time-based segments |
| Interaction effects | Check for conflicts with concurrent experiments |
| SRM | Monitor sample ratio daily |
## 6. Decision Framework
| Result | Action |
|:---|:---|
| Primary ↑ significant, guardrails safe | Ship to 100% |
| Primary ↑ significant, guardrail degraded | Investigate tradeoff |
| Primary not significant | Document learning, iterate |
| Primary ↓ significant | Kill experiment, document |
