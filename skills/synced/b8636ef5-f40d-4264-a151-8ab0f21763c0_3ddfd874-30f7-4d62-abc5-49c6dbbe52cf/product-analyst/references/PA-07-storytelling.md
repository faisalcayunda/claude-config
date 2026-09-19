# PA-06: Product Metrics & KPI Frameworks

## North Star Framework (Amplitude)
Three "games" determine your North Star Metric:
| Game | NSM Type | Example | Inputs |
|:---|:---|:---|:---|
| **Attention** | Time spent engaging | Spotify: hours listened | Playlists created, songs liked, sessions/week |
| **Transaction** | Volume/value | Amazon: purchases/month | Items viewed, cart adds, checkout starts |
| **Productivity** | Tasks completed | Slack: messages sent | Channels joined, files shared, integrations |

## HEART Framework (Google — Rodden et al. 2010)
| Dimension | Goals | Signals | Metrics |
|:---|:---|:---|:---|
| **Happiness** | Users satisfied | Survey responses | NPS, CSAT, SUS score |
| **Engagement** | Users actively using | Session frequency | DAU/MAU, sessions/week |
| **Adoption** | New users trying features | First-time feature usage | % users trying feature in 7d |
| **Retention** | Users coming back | Return visits | D7/D30 retention rate |
| **Task Success** | Users completing goals | Task completion | Completion rate, time-on-task |

## SaaS Unit Economics (Skok)
| Metric | Formula | Benchmark |
|:---|:---|:---|
| **LTV** | ARPU × Gross Margin / Churn | LTV ≥ 3× CAC |
| **CAC** | (Sales + Marketing) / New Customers | — |
| **CAC Payback** | CAC / (ARPU × Gross Margin) | < 12 months |
| **NRR** | (Start MRR + Expansion − Contraction − Churn) / Start MRR | >110% top quartile |
| **Quick Ratio** | (New MRR + Expansion) / (Contraction + Churn) | >4 excellent |

## Metric Tree Structure
North Star Metric → Input Metrics (3-5 levers) → Team-Level Metrics
Example: Revenue = Users × Conversion Rate × ARPU
Each branch becomes a team's focus area with its own leading indicators.

## Counter-Metrics / Guardrails (Eppo)
For every success metric, define what must NOT degrade:
| Success Metric | Counter-Metric | Rationale |
|:---|:---|:---|
| Revenue per user | Customer satisfaction | Don't extract value at cost of experience |
| Signup rate | Activation rate | Don't optimize top of funnel if nobody activates |
| Feature adoption | Support ticket rate | Don't push features that confuse users |

---

# PA-07: Data Storytelling & Visualization

## Storytelling with Data — 6 Lessons (Knaflic 2015)
1. **Understand the context** — Who is your audience? What action do you want?
2. **Choose an effective visual** — Bar, line, scatter — match chart to message
3. **Eliminate clutter** — Remove chartjunk, maximize data-ink ratio (Tufte)
4. **Focus attention** — Use preattentive attributes (color, size, position)
5. **Think like a designer** — Gestalt principles: proximity, similarity, enclosure
6. **Tell a story** — Setup (context) → Conflict (insight) → Resolution (recommendation)

## Dashboard Design Principles (Few)
- **No more than 5-7 metrics per dashboard** — cognitive load limit
- **Use bullet graphs** instead of gauges — more information, less space
- **Context always**: show vs target, vs last period, vs benchmark
- **Alert-driven**: highlight only what needs attention
- **Avoid pie charts**: humans are bad at comparing angles

## Executive Reporting Structure
| Section | Content | Time |
|:---|:---|:---|
| **Headline** | One-sentence takeaway | 5 sec |
| **So What?** | Why this matters to the business | 15 sec |
| **Key Metrics** | 3-5 metrics with trends | 30 sec |
| **Deep Dive** | Supporting analysis | 2 min |
| **Recommendation** | What to do next | 15 sec |

---

# PA-08: Predictive Analytics

## Customer Lifetime Value Models (Fader)
| Model | Type | Best For |
|:---|:---|:---|
| **BG/NBD** | Probabilistic (non-contractual) | E-commerce, marketplaces |
| **Pareto/NBD** | Probabilistic (non-contractual) | General purchase behavior |
| **sBG** | Shifted Beta-Geometric (contractual) | Subscriptions |
| **CBCV** | Customer-Based Corporate Valuation | Company-level valuation from customer data |

## Attribution Models
| Model | Logic | Limitation |
|:---|:---|:---|
| **Last Touch** | 100% credit to last touchpoint | Ignores discovery |
| **First Touch** | 100% credit to first touchpoint | Ignores conversion |
| **Linear** | Equal credit to all touchpoints | Oversimplifies |
| **Time Decay** | More credit to recent touchpoints | Arbitrary decay |
| **Data-Driven** | ML-based allocation | Requires volume |

## Marketing Mix Modeling
**Meta Robyn** (open-source): Ridge regression + Prophet decomposition + multi-objective optimization
**Google Meridian** (open-source): Bayesian regression with geo-level hierarchical modeling
Both solve: "How much of my growth is attributable to each marketing channel?"

---

# PA-09: Analytics Engineering & Tools

## dbt Project Structure (Machado/Russa)
```
models/
├── staging/     ← 1:1 with source tables, renamed, retyped
├── intermediate/ ← business logic transformations
└── marts/       ← final tables for analysis (fact/dim)
```

## Semantic/Metrics Layer (Stancil 2021, Airbnb Minerva)
Define metrics once, use everywhere: "Revenue = SUM(amount) WHERE status = 'completed'"
Benefits: No conflicting metric definitions across dashboards/reports/ad-hoc queries.

## SQL for Product Analysts — Essential Patterns
| Pattern | Use |
|:---|:---|
| Window functions (LAG, LEAD, ROW_NUMBER) | Retention analysis, sequential events |
| CASE WHEN + GROUP BY | Cohort bucketing, funnel steps |
| DATE_TRUNC + COUNT DISTINCT | Time-series analysis |
| Self-joins | Comparing user behavior across time periods |
| CTEs (WITH clause) | Readable, composable analysis queries |

---

# PA-10: Behavioral Analytics, Growth & Privacy

## Hook Model Metrics (Eyal 2014)
| Phase | Metric | Example |
|:---|:---|:---|
| **Trigger** | Notification open rate, email CTR | Push notification → app open |
| **Action** | Core action completion rate | Feed scroll, search, post |
| **Variable Reward** | Engagement depth | Time in feed, content consumed |
| **Investment** | Data stored, connections made | Profile completion, follows, uploads |

## Growth Loops (Balfour/Reforge)
Replace linear funnels with self-reinforcing loops:
- **Viral Loop**: User uses → invites friend → friend uses → invites...
- **Content Loop**: User creates content → indexed by search → new user discovers → uses...
- **Paid Loop**: Revenue → reinvest in ads → new user → revenue...
Key metric: **Loop cycle time** (shorter = faster compounding)

## Privacy-Preserving Analytics
| Approach | Mechanism | Tool Example |
|:---|:---|:---|
| **Differential Privacy** | Add calibrated noise to protect individuals | Apple ε-DP, Google RAPPOR |
| **Cookieless Tracking** | First-party data, server-side, fingerprint-free | Plausible, Fathom |
| **Aggregated Reporting** | Report only group-level metrics | Privacy Sandbox Attribution API |
| **Data Minimization** | Collect only what's needed, delete when done | GDPR Article 5 |
