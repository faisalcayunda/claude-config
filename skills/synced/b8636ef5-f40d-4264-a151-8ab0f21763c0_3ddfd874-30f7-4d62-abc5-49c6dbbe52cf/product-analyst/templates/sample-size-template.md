# Sample Size Calculator: [Experiment Name]
## Parameters
| Input | Value | Notes |
|:---|:---|:---|
| Baseline rate | [X%] | Current conversion/metric value |
| MDE (relative) | [X%] | Smallest meaningful improvement |
| MDE (absolute) | [X pp] | Calculated: baseline × relative MDE |
| Significance (α) | 0.05 | Two-tailed |
| Power (1-β) | 0.80 | Standard; use 0.90 for critical tests |
| Variants | 2 | Control + 1 treatment |
## Calculation
**Formula**: n = 2 × (Z_α/2 + Z_β)² × p(1-p) / δ²
Where Z_0.025 = 1.96, Z_0.20 = 0.84
**Result**: [N] users per variant → [2N] total
## Duration Estimate
| Scenario | Daily Traffic | Duration |
|:---|:---|:---|
| All users | [N/day] | [X days] |
| 50% allocation | [N/day × 0.5] | [X days] |
| With CUPED (~50% reduction) | [N/day] | [X/2 days] |
## Sensitivity Table
| MDE | Sample/variant | Duration (all traffic) |
|:---|:---|:---|
| 1% relative | [N] | [X days] |
| 3% relative | [N] | [X days] |
| 5% relative | [N] | [X days] |
| 10% relative | [N] | [X days] |
