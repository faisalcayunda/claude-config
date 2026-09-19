# PM-06: Product Metrics & Analytics

## AARRR Pirate Metrics (McClure 2007)
| Stage | Question | Example Metrics |
|:---|:---|:---|
| **Acquisition** | How do users find us? | Visitors, signups, channel attribution |
| **Activation** | Do they have a great first experience? | Onboarding completion, "aha moment" |
| **Retention** | Do they come back? | D1/D7/D30 retention, DAU/MAU |
| **Referral** | Do they tell others? | Viral coefficient, NPS, invite rate |
| **Revenue** | Do they pay? | Conversion, ARPU, LTV |

## North Star Metric Framework (Amplitude)
Three "games" determine your NSM:
| Game | NSM Type | Example |
|:---|:---|:---|
| **Attention** | Time spent | Spotify: time listening |
| **Transaction** | Volume/value | Amazon: purchases per month |
| **Productivity** | Tasks completed | Slack: messages sent |
NSM = leading indicator of sustainable growth. Supported by 3-5 input metrics teams can influence.

## HEART Framework (Google — Rodden et al. 2010)
| Dimension | Definition | Example |
|:---|:---|:---|
| **Happiness** | Satisfaction, NPS | Survey score |
| **Engagement** | Depth of interaction | Sessions/week, features used |
| **Adoption** | New users of feature | % users trying new feature |
| **Retention** | Users coming back | Weekly retention rate |
| **Task Success** | Efficiency, completion | Task completion rate, time-on-task |
Process: Goals → Signals → Metrics (GSM)

## SaaS Unit Economics (Skok)
| Metric | Formula | Benchmark |
|:---|:---|:---|
| **LTV** | ARPU × Gross Margin / Churn Rate | LTV ≥ 3× CAC |
| **CAC** | Sales + Marketing / New Customers | — |
| **CAC Payback** | CAC / (ARPU × Gross Margin) | < 12 months |
| **NRR** | (Start MRR + Expansion - Contraction - Churn) / Start MRR | >110% top quartile |

---

# PM-07: PM Operating Model & Career

## Product Operating Model (Cagan/Transformed 2024)
Three transformations:
1. **How you build** → Empowered product teams (not feature teams)
2. **How you solve problems** → Product discovery (not project execution)
3. **How you decide which problems to solve** → Product strategy (not stakeholder requests)

## Product Trio (Torres)
PM + Designer + Tech Lead — co-own discovery.
Weekly rhythm: customer interview → OST update → assumption test → iterate.

## Dual-Track Agile
| Track | Focus | Cadence |
|:---|:---|:---|
| **Discovery** | Validate ideas (value + usability) | Continuous |
| **Delivery** | Build validated solutions | Sprint-based |
Ideas flow from Discovery → Backlog → Delivery only when validated.

## PM Competency Model (Mehta — 12 competencies)
| Category | Competencies |
|:---|:---|
| **Product Execution** | Feature specification, product delivery, quality assurance |
| **Customer Insight** | User research, data analysis, market expertise |
| **Product Strategy** | Product vision, roadmapping, strategic impact |
| **Influencing People** | Stakeholder management, team leadership, culture |

## PM Career Ladder
Associate PM → PM → Senior PM → Staff/Principal PM → Group PM → Director → VP Product → CPO

---

# PM-08: Competitive Analysis & Market

## Five Forces (Porter 1980)
1. Threat of New Entrants (barriers to entry)
2. Bargaining Power of Suppliers
3. Bargaining Power of Buyers
4. Threat of Substitutes
5. Industry Rivalry

## Positioning (Dunford — Obviously Awesome)
Five components: Competitive Alternatives → Unique Attributes → Value → Target Customers → Market Category
Three styles: **Head to Head** | **Big Fish Small Pond** | **Category Creation**

## Technology Adoption Lifecycle (Moore)
Innovators → Early Adopters → **[CHASM]** → Early Majority → Late Majority → Laggards
Cross the chasm: dominate one beachhead segment with the Whole Product.

## Market Sizing
| Level | Definition | Method |
|:---|:---|:---|
| **TAM** | Total Addressable Market | Top-down from industry data |
| **SAM** | Serviceable Available Market | TAM filtered by your reach |
| **SOM** | Serviceable Obtainable Market | SAM × realistic market share |

---

# PM-09: Pricing & Monetization

## 9 Rules of Monetization (Ramanujam 2016)
1. Have the willingness-to-pay conversation early
2. Don't default to one-size-fits-all
3. Configuration not customization
4. Choose the right pricing model
5. Price on value, not cost
6. Develop options: Good/Better/Best
7. Know the four types of monetization failures (Feature Shock, Minivation, Hidden Gem, Undead)
8. Build an ROI model
9. Test pricing as rigorously as features

## Van Westendorp Price Sensitivity Meter
Four questions: At what price is it too expensive? Too cheap? Getting expensive but still consider? A bargain?
Intersection points define: **Point of Marginal Cheapness, Optimal Price Point, Indifference Price, Point of Marginal Expensiveness**

## Pricing Models
| Model | How | Best For |
|:---|:---|:---|
| **Per-seat** | $/user/month | Collaboration tools |
| **Usage-based** | Pay per unit consumed | API, infrastructure |
| **Tiered** | Good/Better/Best packages | SaaS |
| **Freemium** | Free tier + paid upgrades | PLG |
| **Free trial** | Time-limited full access | High-value products |

---

# PM-10: AI Product Management

## AI Product Lifecycle (Nika/Granados 2025)
Traditional: Idea → Build → Launch → Iterate
AI: Idea → **Data** → **Model** → **Evaluate** → Build → Launch → **Monitor & Retrain**
Key differences: data is the raw material, models are probabilistic, continuous monitoring required.

## AI Opportunity Tree (Lipenkova 2025)
Customer Problem → **AI Benefit** (speed, personalization, prediction, generation) → AI Capability → Data Requirement → Technical Feasibility

## Four Risks for AI (extended from Cagan)
| Risk | AI-Specific Question |
|:---|:---|
| **Value** | Does the AI actually solve the problem better than rules-based approach? |
| **Usability** | Can users understand/trust probabilistic outputs? |
| **Feasibility** | Do we have sufficient training data? Is accuracy achievable? |
| **Ethics** | Is the model fair? Explainable? Privacy-preserving? |

## Human-AI Interaction Guidelines (Microsoft HAX)
18 guidelines across: Initially (set expectations), During (support interaction), When wrong (support correction), Over time (remember, update, adapt)

## Google PAIR — People + AI Guidebook
When to use AI? Only when: (1) it solves a real user need, (2) it outperforms non-AI alternatives, (3) users can understand/correct errors, (4) the failure mode is acceptable.
