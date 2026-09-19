# DM-06: International Standards

## ISO 8000 — Data Quality Standard
Multi-part standard: Part 1 (overview), Part 2 (vocabulary), Part 8 (master data exchange), Part 60 (DQ management overview), Part 62 (process maturity assessment).
Key use: Formal DQ certification and cross-organization data exchange.

## ISO/IEC 38505 — Governance of Data
Applies evaluate-direct-monitor model from ISO/IEC 38500 to data.
Three principles: Value, Risk, Constraint — governing data across the lifecycle.

## ISO/IEC 25012 — Data Quality Model (SQuaRE)
15 characteristics in two perspectives:
| Perspective | Characteristics |
|:---|:---|
| **Inherent** | Accuracy, Completeness, Consistency, Credibility, Currentness |
| **System-Dependent** | Availability, Portability, Recoverability |
| **Both** | Accessibility, Compliance, Confidentiality, Efficiency, Precision, Traceability, Understandability |

## FAIR Principles (Wilkinson et al. 2016)
| Principle | Requirements |
|:---|:---|
| **Findable** | Globally unique persistent identifier, rich metadata, registered in searchable resource |
| **Accessible** | Retrievable by ID using open protocol, metadata available even when data isn't |
| **Interoperable** | Uses formal, shared vocabulary, includes qualified references |
| **Reusable** | Clear usage license, provenance, community standards |

## Other Key Standards
| Standard | Scope |
|:---|:---|
| ISO/IEC 11179 | Metadata registries — data element concepts |
| Dublin Core (ISO 15836) | 15 core metadata properties |
| DCAT v3 (W3C) | Data catalog vocabulary for interoperability |
| NIST NBDIF | 9-volume big data interoperability framework |
| ISO/IEC 8183 | AI data lifecycle (10 stages) |
| ISO 27001 | Information security management (93 controls) |

---

# DM-07: Data Strategy & Valuation

## Laney's Infonomics — 6 Valuation Models
| Model | Measures | Approach |
|:---|:---|:---|
| **IVI** (Intrinsic Value) | Quality + scarcity of data | Accuracy, completeness, exclusivity |
| **BVI** (Business Value) | Impact on business processes | Revenue impact, cost avoidance |
| **PVI** (Performance Value) | Contribution to KPIs | Correlation with performance metrics |
| **CVI** (Cost Value) | Replacement cost if lost | Acquisition + maintenance cost |
| **MVI** (Market Value) | Price if traded/sold | Comparable transactions |
| **EVI** (Economic Value) | Future income generation | DCF of expected data revenue |

## DalleMule & Davenport — Offense vs. Defense
| | Defensive | Offensive |
|:---|:---|:---|
| **Goal** | Minimize downside risk | Generate business value |
| **Focus** | Compliance, privacy, security, quality | Analytics, monetization, innovation |
| **Structure** | Centralized, standardized | Flexible, domain-specific |
Most orgs need BOTH — balance based on industry context.

## Wixom — Improve-Wrap-Sell (MIT CISR)
| Strategy | Description | Example |
|:---|:---|:---|
| **Improve** | Use data to enhance internal processes | Predictive maintenance |
| **Wrap** | Wrap data services around products | IoT analytics dashboard |
| **Sell** | Sell data as a product | Data marketplace |

---

# DM-08: Metadata Management & Data Catalog

## Three Generations of Metadata (LinkedIn/DataHub)
| Generation | Architecture | Example |
|:---|:---|:---|
| **1st Gen** | Pull-based (crawlers) | Apache Atlas |
| **2nd Gen** | Push-based (API-first) | Amundsen |
| **3rd Gen** | Stream-first (real-time events) | DataHub |

## Data Catalog Evaluation Criteria
| Dimension | What to Assess |
|:---|:---|
| **Discovery** | Search quality, auto-classification, lineage visualization |
| **Governance** | Policy enforcement, stewardship workflows, access controls |
| **Collaboration** | Social features, knowledge graph, annotations |
| **Integration** | Connectors, API coverage, embedded in workflows |
| **Automation** | ML-powered tagging, schema detection, quality alerts |
| **Scalability** | Performance at enterprise scale, multi-cloud |

## Active Metadata
Shift from passive catalog to active orchestration: metadata drives automated decisions about data quality, access, lineage, and lifecycle without human intervention.

---

# DM-09: Master Data Management

## MDM Styles (Loshin)
| Style | Description | When |
|:---|:---|:---|
| **Registry** | Index linking distributed records | Minimal disruption, quick start |
| **Consolidation** | Physical golden record (read-only) | Analytics, reporting |
| **Coexistence** | Golden record synced back to sources | Gradual migration |
| **Centralized** | Single authoritative hub | Full MDM commitment |

## Entity Resolution (Christen 2012)
Process: **Standardize → Block → Compare → Classify → Merge**
Techniques: Probabilistic matching, ML matching, deterministic rules
Key challenge: False positives (merging different entities) vs false negatives (missing duplicates)

---

# DM-10: Privacy, Ethics & AI Data Management

## GDPR Key Articles for Data Management
| Article | Requirement | DM Implication |
|:---|:---|:---|
| Art. 5 | Data processing principles | Quality, minimization, purpose limitation |
| Art. 17 | Right to erasure | Requires comprehensive data lineage |
| Art. 25 | Data protection by design | Privacy-first architecture |
| Art. 30 | Records of processing | Data catalog / ROPA |
| Art. 35 | DPIA for high-risk processing | Impact assessment template |

## Cavoukian's Privacy by Design — 7 Principles
1. Proactive not reactive
2. Privacy as the default
3. Privacy embedded into design
4. Full functionality (positive-sum, not zero-sum)
5. End-to-end security
6. Visibility and transparency
7. Respect for user privacy

## AI/ML Data Management
| Concern | Approach | Tools |
|:---|:---|:---|
| Training data quality | Data-centric AI (Ng) | Great Expectations, Cleanlab |
| Feature management | Feature stores | Feast, Hopsworks |
| Data versioning | Git-like versioning for data | DVC, LakeFS |
| Bias detection | Statistical analysis of training data | Fairlearn, AI Fairness 360 |
| Model lineage | Track data → features → model → predictions | MLflow, W&B |

## Differential Privacy (Dwork 2006)
ε-differential privacy: Adding calibrated noise ensures individual records cannot be identified.
Mechanisms: Laplace (for numerical queries), Exponential (for categorical queries)
Trade-off: Privacy (lower ε) vs. accuracy (higher ε)
