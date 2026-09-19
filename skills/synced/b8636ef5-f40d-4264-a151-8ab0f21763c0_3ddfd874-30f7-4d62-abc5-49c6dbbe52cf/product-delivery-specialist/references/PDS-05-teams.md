# PDS-01: Scrum & Agile Frameworks

## Scrum Guide 2020 (Schwaber/Sutherland)
**3 Pillars**: Transparency, Inspection, Adaptation
**5 Values**: Commitment, Focus, Openness, Respect, Courage
**Accountabilities**: Product Owner (value maximization), Scrum Master (effectiveness), Developers (increment delivery)
**Events**: Sprint (≤4 weeks) → Sprint Planning → Daily Scrum → Sprint Review → Sprint Retrospective
**Artifacts**: Product Backlog → Sprint Backlog → Increment (meets Definition of Done)
**Commitments**: Product Goal, Sprint Goal, Definition of Done

## SAFe 6.0 (Leffingwell/Knaster)
7 Core Competencies: Team & Technical Agility, Agile Product Delivery, Enterprise Solution Delivery, Lean Portfolio Management, Organizational Agility, Continuous Learning Culture, Lean-Agile Leadership
**PI Planning**: 2-day big room event, every 8-12 weeks. Outputs: PI Objectives, Program Board, ROAM risks.
**ART**: 50-125 people, 5-12 teams on a shared mission.

## Shape Up (Singer/Basecamp 2019)
**6-week cycles** (not 2-week sprints). Shaping (senior) → Betting Table (leadership) → Building (teams).
**Appetite**: Fixed time, variable scope (opposite of Scrum's fixed scope, variable time).
**Hill Charts**: Track progress as "figuring out" → "making it happen."

## Key Framework Comparison
| Framework | Team Size | Scaling | Planning | Best For |
|:---|:---|:---|:---|:---|
| **Scrum** | 3-9 | Nexus, LeSS, S@S | Sprint (1-4 wk) | Cross-functional product teams |
| **SAFe** | ARTs 50-125 | Built-in (4 configs) | PI (8-12 wk) | Large enterprise, compliance |
| **LeSS** | 2-8 teams | LeSS Huge (>8) | Sprint | Large-scale, minimal process |
| **Shape Up** | ~2-3 people | Limited | Cycle (6 wk) | Small teams, high autonomy |
| **Kanban** | Any | Flight Levels | Continuous | Support, maintenance, ops |

---

# PDS-02: Kanban & Flow

## Kanban Method (Anderson 2010) — 6 Practices
1. **Visualize** the work (board, cards, columns)
2. **Limit WIP** (the single most impactful practice)
3. **Manage flow** (measure cycle time, identify bottlenecks)
4. **Make policies explicit** (column criteria, WIP limits, classes of service)
5. **Implement feedback loops** (cadences: standup, replenishment, delivery planning, ops review)
6. **Improve collaboratively, evolve experimentally** (kaizen, no big-bang changes)

## Little's Law (applied to knowledge work)
**L = λ × W** (Average WIP = Average Throughput × Average Cycle Time)
Implication: To reduce cycle time → reduce WIP (not add people).

## Flow Metrics (Vacanti 2015)
| Metric | Measures | Action |
|:---|:---|:---|
| **Cycle Time** | Time from start to done | Lower = faster delivery |
| **Throughput** | Items completed per time period | Higher = more capacity |
| **WIP** | Items in progress simultaneously | Lower = faster flow |
| **Work Item Age** | Time since item started (not yet done) | Older = stuck — investigate |

## Monte Carlo Forecasting (Magennis/Vacanti)
Use historical throughput data → run 10,000+ simulations → produce probability distribution for "When will N items be done?"
Example output: "85% confidence: done by March 15. 50% confidence: done by March 8."
Advantage: No estimation needed — uses actual throughput data. Far more accurate than velocity-based planning.

## Cost of Delay (Reinertsen 2009)
| Profile | Description | Prioritization |
|:---|:---|:---|
| **Standard** | Linear value loss over time | CD3 (Cost of Delay ÷ Duration) = WSJF |
| **Urgent** | Value drops steeply | Do immediately |
| **Fixed date** | Value cliff at deadline | Schedule around constraint |
| **Intangible** | Hard to quantify but important | Don't defer indefinitely |

---

# PDS-03: Delivery Metrics

## DORA 4 Key Metrics (Forsgren/Humble/Kim 2018)
| Metric | Elite | High | Medium | Low |
|:---|:---|:---|:---|:---|
| **Deployment Frequency** | Multiple/day | Weekly-daily | Monthly-weekly | Monthly-6mo |
| **Lead Time for Changes** | <1 hour | 1 day-1 week | 1 week-1 month | 1-6 months |
| **Change Failure Rate** | 0-15% | 16-30% | 16-30% | 46-60% |
| **Time to Restore** | <1 hour | <1 day | 1 day-1 week | >6 months |

Key insight: These metrics are CORRELATED — improving one tends to improve all four. High performers are BOTH faster AND more stable.

## Flow Framework (Kersten 2018)
4 flow items: **Features, Defects, Risk, Debt**
5 flow metrics: **Velocity** (items/time), **Time** (from accept to done), **Load** (WIP), **Efficiency** (active vs wait), **Distribution** (% across 4 types)
Key insight: If >25% of flow goes to Defects + Debt, product value stream is unhealthy.

## Evidence-Based Management (Scrum.org)
4 Key Value Areas: **Current Value** (customer satisfaction, revenue), **Unrealized Value** (market gap), **Ability to Innovate** (% spent on new features), **Time to Market** (release frequency, cycle time)

---

# PDS-04: Continuous Improvement

## Retrospective 5-Phase (Derby/Larsen 2006)
1. **Set the stage** — Check-in, establish safety, set focus
2. **Gather data** — What happened? (timeline, 4Ls, mad/sad/glad)
3. **Generate insights** — Why did it happen? (5 Whys, fishbone, patterns)
4. **Decide what to do** — Concrete experiments with owners + due dates
5. **Close** — Appreciation, evaluate the retro itself

## Theory of Constraints (Goldratt 1984)
5 Focusing Steps: **Identify** the constraint → **Exploit** it (maximize throughput) → **Subordinate** everything else → **Elevate** (invest to remove) → **Repeat** (find next constraint)
In delivery: The constraint is usually testing, review, or deployment — NOT coding.

## Value Stream Mapping (Rother/Shook 1999)
Map current state: Each step → **Process Time** (value-adding) + **Wait Time** (waste)
Calculate: **Flow Efficiency** = Process Time ÷ Lead Time × 100%
Typical knowledge work: **5-15% flow efficient** (85-95% waiting!)
Target improvements on the largest wait-time gaps.

## Toyota Kata (Rother 2009)
**Improvement Kata** (4 steps): Understand the direction → Grasp current condition → Set next target condition → Experiment toward target
**Coaching Kata** (5 questions): What's the target? What's the actual? What obstacles? What's your next step? When can we see results?

---

# PDS-05: Team Dynamics & Coaching

## Team Topologies (Skelton/Pais 2019)
| Team Type | Purpose | Example |
|:---|:---|:---|
| **Stream-aligned** | Deliver value on a business stream | Feature team, product squad |
| **Platform** | Reduce cognitive load of stream teams | Internal developer platform |
| **Enabling** | Help teams overcome obstacles | Agile coaching, DevEx team |
| **Complicated-subsystem** | Deep specialist expertise | ML model team, legacy system |

3 Interaction Modes: **Collaboration** (working together), **X-as-a-Service** (consuming), **Facilitating** (helping)
Key principle: Minimize cognitive load on stream-aligned teams. Apply Conway's Law deliberately.

## Psychological Safety (Edmondson 2018 / Google Aristotle)
4 zones (Safety × Accountability):
- **Learning Zone** (high safety + high accountability) ← TARGET
- Comfort Zone (high safety + low accountability) — no growth
- Anxiety Zone (low safety + high accountability) — fear
- Apathy Zone (low safety + low accountability) — disengagement

## Coaching Stances (Adkins 2010)
| Stance | When |
|:---|:---|
| **Teacher** | Team needs new knowledge/skill |
| **Mentor** | Team needs experience-based guidance |
| **Facilitator** | Team needs structured conversation |
| **Coach** | Team needs to discover their own answers |
Move from teaching → coaching as team matures (Tuckman: Forming → Performing).

## Motivation (Pink 2009)
3 intrinsic motivators: **Autonomy** (self-direction), **Mastery** (getting better), **Purpose** (meaningful work)
For delivery teams: Give autonomy over HOW (not what), create mastery paths, connect work to customer outcomes.
