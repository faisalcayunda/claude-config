# PA-01: Event Tracking & Data Taxonomy

## Tracking Plan Structure
| Column | Description | Example |
|:---|:---|:---|
| **Event Name** | [Object] + [Past-Tense Verb] (Amplitude) or [Object] + [Action] (Segment) | "Article Viewed", "Order Completed" |
| **Description** | Business meaning of this event | "User views a full article page" |
| **Trigger** | When exactly this fires | "On page load of /article/* URL" |
| **Properties** | Key-value pairs sent with event | article_id, category, word_count, author |
| **Property Type** | Data type | string, integer, boolean, datetime |
| **Platform** | Where tracked | Web, iOS, Android, Server |
| **Source** | Client-side vs server-side | Client (for UI), Server (for transactions) |
| **Status** | Implementation state | Planned, Implemented, Verified, Deprecated |

## Naming Conventions
| Standard | Format | Example |
|:---|:---|:---|
| **Amplitude** | [Noun] + [Past-Tense Verb], Title Case | "Song Played", "Cart Updated" |
| **Segment** | [Object] + [Action], Title Case | "Product Viewed", "Order Completed" |
| **Mixpanel** | [Object] + [Verb], snake_case for properties | "sign_up_completed" |

## Client-Side vs Server-Side Tracking
| Aspect | Client-Side | Server-Side |
|:---|:---|:---|
| **Reliability** | Blocked by ad blockers (~30%) | Always fires |
| **Data access** | UI interactions, page views | Transactions, subscriptions, backend events |
| **Latency** | Real-time | Near real-time |
| **Best for** | Behavioral analytics | Revenue events, critical business logic |

## Identity Resolution
**Deterministic**: Exact match on login email, user ID — high precision, lower coverage
**Probabilistic**: Statistical match on device fingerprint, IP — lower precision, higher coverage
**Best practice**: Use deterministic as foundation, probabilistic to fill gaps, merge with CDP

---

# PA-02: Funnel Analysis & Conversion Optimization

## AARRR Pirate Metrics (McClure 2007)
| Stage | Question | Key Metric | Benchmark |
|:---|:---|:---|:---|
| **Acquisition** | How do users find us? | Visitors, signups by channel | Channel-dependent |
| **Activation** | Do they have a great first experience? | Onboarding completion | Median ~25% (Rachitsky) |
| **Retention** | Do they come back? | D7/D30 retention | See PA-03 |
| **Referral** | Do they tell others? | Viral coefficient, NPS | K > 1 for virality |
| **Revenue** | Do they pay? | Conversion, ARPU, LTV | Model-dependent |

## Activation Framework (Reforge/Balfour)
Three moments: **Setup Moment** (prerequisites complete) → **Aha Moment** (first value experience) → **Habit Moment** (repeated core action)
Finding the aha moment: Correlate early behaviors with long-term retention. E.g., Facebook: "7 friends in 10 days", Slack: "2,000 messages", Dropbox: "1 file in 1 folder on 1 device".

## CRO Process — ResearchXL (CXL/Laja)
1. Technical analysis (speed, errors, browser compatibility)
2. Heuristic evaluation (clarity, relevancy, friction, distraction)
3. Web analytics analysis (funnels, segments, flow reports)
4. Mouse tracking (heatmaps, scroll depth, click maps)
5. Qualitative research (surveys, interviews, session replay)
6. User testing (task-based usability tests)
7. Hypothesis prioritization (ICE or PXL framework)

---

# PA-03: Cohort Analysis & Retention

## Retention Analysis Methods (Amplitude)
| Method | How | Best For |
|:---|:---|:---|
| **N-day** | Did user return on exactly day N? | Daily-use products (social, messaging) |
| **Unbounded** | Did user return on day N or later? | Variable-frequency products (e-commerce, SaaS) |
| **Bracket** | Did user return within a custom window? | Weekly/monthly products |

## Retention Benchmarks (Rachitsky/Winters 2020)
| Category | Good (6mo) | Great (6mo) | Metric Type |
|:---|:---|:---|:---|
| Consumer Social | ~25% | ~45% | Unbounded monthly |
| Consumer SaaS | ~40% | ~70% | Unbounded monthly |
| SMB SaaS | ~60% | ~80% | Unbounded monthly |
| Enterprise SaaS | ~70% | ~90% | Unbounded monthly |

## Growth Accounting (Hsu/Social Capital)
**MAU = Retained + New + Resurrected − Churned**
**Quick Ratio** = (New + Resurrected) / Churned — measures growth sustainability
QR > 4 = strong growth; QR < 1 = shrinking

## Survival Analysis for Churn
- **Kaplan-Meier**: Non-parametric survival curve estimation
- **Cox Proportional Hazards**: Semi-parametric model identifying churn risk factors
- Advantage over binary classification: predicts WHEN (not just if) customers churn

---

# PA-04: A/B Testing & Experimentation

## Experiment Design Checklist (Kohavi)
1. Define **Overall Evaluation Criteria (OEC)** — the primary metric
2. Set **guardrail metrics** — must not degrade
3. Calculate **sample size** for desired power (typically 80%) and significance (α = 0.05)
4. Define **Minimum Detectable Effect (MDE)** — smallest meaningful change
5. Determine **experiment duration** — account for weekly patterns (≥2 full weeks)
6. Randomize assignment — check for **Sample Ratio Mismatch (SRM)**
7. Run to completion — **no peeking** (or use sequential testing)
8. Analyze primary metric, then guardrails, then secondary metrics

## Sample Size Formula (simplified)
**n = 2 × (Z_α/2 + Z_β)² × σ² / δ²**
Where: α = significance level (0.05), β = 1 - power (0.20), σ = standard deviation, δ = MDE
Rule of thumb (Miller): n ≈ 16 × σ² / δ²

## CUPED Variance Reduction (Deng et al. 2013)
Use pre-experiment data as covariate to reduce metric variance by 50%+
**Y_adjusted = Y − θ × (X − E[X])** where X is pre-experiment metric value
Result: Same statistical power with ~50% fewer users or ~50% shorter duration

## Bayesian vs Frequentist
| Aspect | Frequentist | Bayesian |
|:---|:---|:---|
| **Question** | "Is the result statistically significant?" | "What's the probability B is better than A?" |
| **Output** | p-value, confidence interval | Posterior distribution, credible interval |
| **Peeking** | Inflates false positives | Less sensitive (but not immune — Robinson 2015) |
| **Prior knowledge** | Not used | Incorporated via prior |

## Experimentation Maturity (Thomke ABCDE Model)
**A**wareness → **B**uy-in → **C**apability → **D**emocratization → **E**mbedding

---

# PA-05: Statistical Methods for Product Analytics

## Causal Inference Ladder (Pearl)
| Level | Question | Method |
|:---|:---|:---|
| **Association** | "What do I observe?" | Regression, correlation |
| **Intervention** | "What if I do X?" | A/B test, do-calculus |
| **Counterfactual** | "What if I had done differently?" | Structural causal models |

## Quasi-Experimental Methods (when A/B testing isn't possible)
| Method | When to Use | Key Assumption |
|:---|:---|:---|
| **Difference-in-Differences (DiD)** | Treatment affects one group, not another | Parallel trends |
| **Regression Discontinuity (RDD)** | Treatment assigned by threshold | Continuity at cutoff |
| **Instrumental Variables (IV)** | Confounding prevents direct estimation | Valid instrument exists |
| **Propensity Score Matching** | Observational data, need comparable groups | No unmeasured confounders |

## Common Statistical Pitfalls
| Pitfall | Problem | Prevention |
|:---|:---|:---|
| **Peeking** | Inflates false positive rate to 30%+ | Sequential testing or fixed-horizon |
| **Simpson's Paradox** | Aggregate trend reverses in subgroups | Always segment before concluding |
| **Survivorship Bias** | Analyzing only surviving users | Include all users from assignment |
| **Multiple Comparisons** | Testing many metrics inflates FP | Bonferroni or FDR correction |
| **Sample Ratio Mismatch** | Unequal randomization | Check SRM before analyzing results |
