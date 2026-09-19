# PDS-06: Release Management & Change

## Continuous Delivery (Humble/Farley 2010)
**Deployment Pipeline**: Commit → Build → Unit Test → Integration Test → Staging → Production
**Principles**: Every check-in is a release candidate. Automate everything repeatable. If it hurts, do it more often.
**Trunk-based development**: Short-lived branches (<1 day), feature flags for incomplete work.

## Feature Flags (Hodgson 2017)
| Type | Purpose | Lifespan |
|:---|:---|:---|
| **Release** | Decouple deployment from release | Short (days-weeks) |
| **Experiment** | A/B testing, canary | Medium (weeks) |
| **Ops** | Circuit breakers, kill switches | Long (permanent) |
| **Permission** | Premium features, entitlements | Long (permanent) |
**Toggle debt**: Remove flags after use — stale flags are hidden complexity.

## Progressive Delivery (Governor 2018/2025)
4 Tenets: **Abundance** (deploy often), **Automation** (rollback automatic), **Alignment** (business + eng), **Autonomy** (teams own release)
Sequence: Feature flag → Canary (1%) → Progressive rollout (10%→50%→100%) → Full GA
Rollback: Automated based on SLO violation — no human approval needed.

## Deployment Strategies
| Strategy | Risk | Complexity | When |
|:---|:---|:---|:---|
| **Blue-Green** | Low | Medium | Zero-downtime switchover |
| **Canary** | Very Low | High | Gradual validation in prod |
| **Rolling** | Medium | Low | Standard Kubernetes default |
| **Feature Flags** | Very Low | Medium | Decouple deploy from release |

## ADKAR Change Model (Prosci/Hiatt)
**A**wareness → **D**esire → **K**nowledge → **A**bility → **R**einforcement
Sequential — each step must be achieved before next. Diagnose resistance by identifying which step is blocked.

## Kotter's 8 Steps (2012)
1. Create urgency → 2. Build coalition → 3. Form vision → 4. Communicate vision → 5. Empower action → 6. Generate short-term wins → 7. Build on change → 8. Anchor in culture
Key update (XLR8 2014): Run 8 steps CONCURRENTLY via volunteer army, not sequentially.

## Switch Framework (Heath & Heath 2010)
**Direct the Rider** (rational): Find bright spots, script critical moves, point to destination
**Motivate the Elephant** (emotional): Find the feeling, shrink the change, grow your people
**Shape the Path** (environment): Tweak the environment, build habits, rally the herd

---

# PDS-07: GTM Strategy & Positioning

## Dunford Positioning (Obviously Awesome 2019) — 10 Steps
1. Understand customers who love your product
2. Form positioning team (cross-functional)
3. Align positioning vocabulary
4. List true competitive alternatives
5. Isolate unique attributes
6. Map attributes to value themes
7. Determine target market
8. Determine market category
9. Layer on relevant trends
10. Capture positioning in messaging

**5 Components**: Competitive alternatives, Unique attributes, Value (for customer), Target customers, Market category

## Crossing the Chasm (Moore 2014)
Technology Adoption: Innovators → Early Adopters → [CHASM] → Early Majority → Late Majority → Laggards
**Beachhead strategy**: Pick ONE narrow segment. Dominate it. Expand from there.
**Whole Product Model**: Core product + expected + augmented + potential. Early Majority needs the WHOLE product.

## Product-Led Growth (Bush 2019)
**PLG Flywheel**: Acquire → Activate → Retain → Expand → Advocate
**Time to Value (TTV)**: Minimize time from signup to "aha moment"
**Decision**: Freemium (wide top of funnel) vs Free Trial (higher-intent, time-limited) vs Hybrid
**PLG metrics**: Signup rate, activation rate, TTV, free-to-paid conversion, expansion revenue

## GTM Motions
| Motion | Lead | Best For | Key Metric |
|:---|:---|:---|:---|
| **Product-led** | Product | Self-serve, low ACV | PQLs, activation rate |
| **Sales-led** | Sales | Enterprise, high ACV | SQL, deal velocity |
| **Marketing-led** | Marketing | Mid-market, content | MQLs, pipeline |
| **Channel-led** | Partners | Geographic/vertical reach | Partner revenue |
| **Community-led** | Community | Developer tools, OSS | Community engagement |

## Revenue Architecture (van der Kooij 2023)
**Bow Tie Model**: Extends traditional funnel (Awareness→Acquisition→Activation) through post-sale (Adoption→Retention→Expansion→Advocacy). Revenue = Acquisition × Retention × Expansion.

---

# PDS-08: Product Launch

## Launch Types
| Type | Scope | GTM Effort | Example |
|:---|:---|:---|:---|
| **Soft launch / Beta** | Limited users | Minimal | Closed beta with select customers |
| **Feature release** | Single feature | Light | In-app announcement + blog |
| **Minor launch** | Multiple features | Medium | Email + webinar + docs update |
| **Major launch** | New product/version | Full | Press, events, sales enablement |

## Launch Readiness Dimensions
1. **Product**: Feature complete, tested, performance validated, docs ready
2. **Marketing**: Positioning finalized, content created, channels activated
3. **Sales**: Enablement done, demo trained, battlecards ready, pricing set
4. **Support**: Docs published, support trained, escalation paths defined
5. **Success**: Onboarding ready, health metrics defined, CSM briefed

## Loved (Lauchengco 2022) — 4 PMM Fundamentals
1. **Ambassador**: Voice of market to product team
2. **Strategist**: GTM strategy and positioning
3. **Storyteller**: Messaging and content
4. **Evangelist**: Market awareness and adoption

## Launch Metrics
| Phase | Metrics |
|:---|:---|
| **Awareness** | Impressions, website traffic, press mentions |
| **Acquisition** | Signups, trials, demo requests |
| **Activation** | First value moment, setup completion, TTV |
| **Adoption** | DAU/MAU, feature adoption, engagement depth |

---

# PDS-09: Sales Enablement

## Battlecard Structure (Klue FIA Framework)
**F**rame: Reframe the conversation around your strengths
**I**solate: Highlight where competitor falls short
**A**ttack: Provide specific proof points and responses

## Key Sales Methodologies
| Method | Author | Core Idea |
|:---|:---|:---|
| **SPIN** | Rackham | Situation→Problem→Implication→Need-Payoff questions |
| **Challenger** | Dixon/Adamson | Teach-Tailor-Take Control commercial insight |
| **MEDDICC** | Whyte | Metrics, Economic Buyer, Decision Criteria/Process, Identify Pain, Champion |
| **Gap Selling** | Keenan | Current state→Future state→Gap identification |

## Sales Enablement Kit Components
1. **Pitch deck** — Customer-facing story (Raskin 5-element narrative)
2. **Battlecards** — Per competitor (FIA framework, updated quarterly)
3. **Demo script** — Guided product walkthrough with talk track
4. **Objection handling** — Top 10 objections with responses
5. **Case studies** — Customer stories with quantified outcomes
6. **ROI calculator** — Spreadsheet with customer-input variables
7. **One-pager** — Single-page value proposition summary
8. **Pricing guide** — Internal pricing + negotiation boundaries

## Demand Waterfall (SiriusDecisions/Forrester)
Inquiry → MQL → SAL → SQL → Close
Evolution: Now includes product-qualified leads (PQLs) alongside MQLs for PLG companies.

---

# PDS-10: Growth & Adoption Metrics

## AARRR Pirate Metrics (McClure 2007)
| Stage | Metric | Example |
|:---|:---|:---|
| **Acquisition** | How users find you | Website visits, signups |
| **Activation** | First value experience | Setup complete, aha moment |
| **Retention** | Users come back | D1/D7/D30, MAU/DAU |
| **Revenue** | Users pay | Trial-to-paid, ARPU, LTV |
| **Referral** | Users tell others | Viral coefficient, NPS |

## North Star Metric (Ellis/Amplitude)
Single metric that best captures core value delivered to customers.
Examples: Spotify = "time spent listening"; Airbnb = "nights booked"; Slack = "messages sent in team"
Supported by **input metrics** (3-5 leading indicators the team can influence directly).

## PLG Benchmarks (OpenView/Poyar)
| Metric | Good | Great | Best-in-Class |
|:---|:---|:---|:---|
| Visitor→Signup (freemium) | 2% | 4% | 6%+ |
| Free→Paid conversion | 3% | 5% | 8%+ |
| Net Revenue Retention | 100% | 110% | 120%+ |
| Logo Retention | 80% | 90% | 95%+ |

## Growth Loops (Balfour/Reforge)
Replace funnel thinking with **compounding loops**:
- **Viral loop**: User invites → new users → more invites
- **Content loop**: Content → SEO traffic → signups → user-generated content
- **Paid loop**: Revenue → reinvest in ads → more revenue
Key: Loops compound; funnels leak. Design for loops.

## Onboarding (John 2021 — EUREKA Framework)
**E**stablish value prop → **U**nderstand user goals → **R**educe friction → **E**ncourage quick wins → **K**eep users engaged → **A**nalyze and optimize
Key metric: **Time to Value (TTV)** — minimize time from signup to first meaningful outcome.
