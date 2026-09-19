# DM-01: Data Management Foundations

## DAMA-DMBOK2 Framework Overview
14 Knowledge Areas organized in the **DAMA Wheel**:
- Center: **Data Governance** (KA-01)
- Ring: Data Architecture (02), Data Modeling (03), Data Storage (04), Data Security (05), Data Integration (06), Document Management (07), Data Warehousing/BI (08), Metadata (09), Reference/Master Data (10), Data Quality (11), Data Handling Ethics (12), Big Data/Data Science (13), DM Maturity (14)

**→ For KA deep dives, use `/dama-research` skill (14 KA files, 152 templates)**

## Key Thought Leaders & Their Frameworks
| Author | Framework | Core Contribution |
|:---|:---|:---|
| Aiken | CDO Case / Data Strategy | First business case for CDO role; data strategy alignment |
| Ladley | DG Program Lifecycle | Comprehensive governance design-deploy-sustain lifecycle |
| Seiner | Non-Invasive DG (NIDG) | Formalize existing accountability, don't impose new bureaucracy |
| Madsen | Data Governance Ops (DGOps) | Agile, people-driven, decentralized governance |
| Burbank | Data Modeling for Business | High-level modeling as business communication tool |
| Sebastian-Coleman | Executive DM Guide | DMBOK2 distilled for executives |
| Eryurek et al. | Cloud-Native DG | Google Cloud governance approach |

---

# DM-02: Data Governance Frameworks

## Khatri & Brown (2010) — 5 Decision Domains
| Domain | Key Decisions |
|:---|:---|
| **Data Principles** | How data is valued and used as asset |
| **Data Quality** | Standards for accuracy, completeness, timeliness |
| **Metadata** | Semantics, definitions, master data |
| **Data Access** | Who can access what data, under what conditions |
| **Data Lifecycle** | Creation, retention, archival, disposal |

## Governance Models Comparison
| Model | Approach | Best For |
|:---|:---|:---|
| **DGI Framework** (Thomas) | 10 components, 7-step lifecycle | First governance program |
| **NIDG** (Seiner) | Formalize existing stewards | Low-resistance adoption |
| **DGOps** (Madsen) | Agile sprints for governance | Modern, fast-moving orgs |
| **Weill/Ross Archetypes** | Business monarchy, federal, feudal, duopoly | Aligning with IT governance |
| **Abraham et al.** | 6-dimension conceptual framework | Academic research, comprehensive analysis |

## BCBS 239 — 14 Principles for Banking
4 sections: Overarching Governance (2), Risk Data Aggregation (4), Risk Reporting (4), Supervisory Review (4)
Impact: Drove massive data governance investment across global banking. As of 2024, compliance remains incomplete among G-SIBs.

---

# DM-03: Data Quality Management

## Wang & Strong (1996) — 15 DQ Dimensions
| Category | Dimensions |
|:---|:---|
| **Intrinsic** | Accuracy, Objectivity, Believability, Reputation |
| **Contextual** | Relevancy, Value-Added, Timeliness, Completeness, Appropriate Amount |
| **Representational** | Interpretability, Ease of Understanding, Concise Representation, Consistent Representation |
| **Accessibility** | Accessibility, Access Security |

## DQ Assessment Approaches
| Approach | Author | Method |
|:---|:---|:---|
| **Profiling** | Olson | Statistical analysis of actual data values |
| **TIQM** | English | Total Information Quality Management — 14 processes |
| **Ten Steps** | McGilvray | Project-based DQ improvement methodology |
| **DQAF** | Sebastian-Coleman | Technology-independent assessment framework |
| **Data Observability** | Moses et al. | 5 pillars: freshness, distribution, volume, schema, lineage |

## Modern DQ Tools
| Tool | Approach | Strength |
|:---|:---|:---|
| Great Expectations | Declarative expectations | Tests as documentation |
| dbt tests | SQL-based assertions | Integrated with transformation |
| Monte Carlo | ML anomaly detection | Automated observability |
| Soda | Open-source checks | Multi-engine support |

---

# DM-04: Modern Data Architecture

## Data Mesh (Dehghani 2022) — 4 Principles
1. **Domain Ownership**: Domains own and serve their data as products
2. **Data as a Product**: Apply product thinking (discoverability, trust, SLAs)
3. **Self-Serve Data Platform**: Reduce domain cognitive load with platform capabilities
4. **Federated Computational Governance**: Automated policies embedded in the platform

## Architecture Paradigm Comparison
| Paradigm | Centralized? | Schema | Best For |
|:---|:---|:---|:---|
| **Data Warehouse** (Kimball/Inmon) | Yes | Schema-on-write | Structured, known queries |
| **Data Lake** (Dixon) | Yes | Schema-on-read | Raw data, exploration |
| **Lakehouse** (Armbrust) | Yes | ACID on lake | Best of both worlds |
| **Data Mesh** (Dehghani) | No — federated | Domain-specific | Large orgs, many domains |
| **Data Fabric** (Gartner) | Overlay | Metadata-driven | Integration across silos |

## Data Contracts (Jones 2023)
Formal agreement between data producer and consumer specifying:
- Schema (fields, types, constraints)
- SLAs (freshness, completeness, availability)
- Semantics (business definitions)
- Ownership (who to contact when issues arise)

## DataOps (Bergh) — 18 Principles
Rooted in: Agile Manifesto + DevOps + Lean Manufacturing + Statistical Process Control
Key practices: Automated testing, version control for data, CI/CD pipelines, monitoring/alerting, collaboration between data teams.

---

# DM-05: Maturity Assessment Models

## Major Maturity Models Comparison
| Model | Levels | Dimensions | Strengths | Limitations |
|:---|:---|:---|:---|:---|
| **CMMI-DMM** | 5 (Initial→Optimized) | 6 process areas, 25 categories | CMMI brand, process rigor | Less modern paradigm coverage |
| **DCAM v3** | 1-6 scoring | 8 components, 136 sub-capabilities | Financial services standard | Complex to assess |
| **Stanford** | 5 levels | 6 components in 2 groups | Higher education origin | Limited industry validation |
| **IBM** | 5 levels | 11 categories | Enterprise adoption | IBM-centric |
| **TDWI** | 6 stages | 4 imperatives | Analytics focus | BI-oriented |
| **DataOps** (DataKitchen) | 5 levels | People, process, tech, culture | Modern practices | Narrow scope |

## Maturity Assessment Process
1. **Select model** — Match to industry and organizational context
2. **Define scope** — Which domains/capabilities to assess
3. **Gather evidence** — Interviews, document review, tool audit
4. **Score capabilities** — Rate against maturity levels with evidence
5. **Identify gaps** — Current vs target state per capability
6. **Prioritize** — High impact + achievable improvements first
7. **Create roadmap** — Phased plan with milestones and KPIs
