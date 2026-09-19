# Service Delivery Patterns & Commercial Models

**Last Updated:** February 2026

## Standard Service Delivery Process

All IDEAS services follow a dual-sided delivery pattern: **Frontstage** (visible to the client) and **Backstage** (internal to IDEAS). This ensures a clear separation of concerns and a structured approach to client interaction and internal execution.

### Advisory & Governance Pattern (Pillar 1 Services)

This pattern is the foundation for strategic services like Data Strategy (S1.1), Governance Framework Development (S1.2, S1.4), and Data Maturity Assessment (S1.3).

**Frontstage:**
1.  **Kick-off Meeting:** Aligning on objectives, scope, timeline, and success criteria.
2.  **Stakeholder Interviews:** Structured interviews with leadership and key personnel to understand context and pain points.
3.  **Assessment Workshop:** Collaborative session to map the current state of data management capabilities.
4.  **Initial Findings Presentation:** Validating preliminary findings and analysis with the client.
5.  **Strategy Design Workshop:** Co-designing the future-state vision, goals, and strategic initiatives.
6.  **Final Presentation & Handover:** Delivering the final approved strategy, roadmap, and associated deliverables.

**Backstage:**
1.  **Document Analysis:** Reviewing the client's existing strategic documents, policies, and architectural diagrams.
2.  **Analysis & Benchmarking:** Performing quantitative and qualitative analysis against industry benchmarks and maturity models (e.g., DAMA-DMBOK, DCAM).
3.  **Gap Analysis:** Identifying gaps against target standards or regulations (e.g., UU PDP, GDPR, ISO/IEC 27001).
4.  **Synthesis & Modeling:** Developing strategic scenarios, financial impact models, and operating models.
5.  **Deliverable Authoring:** Authoring reports, policy documents, presentations, and other deliverables.
6.  **Internal Quality Assurance:** Senior expert review to ensure quality, consistency, and actionable recommendations.

### Platform Implementation Pattern (Dual-Track Agile)

Used for implementing platform-based solutions (Pillar 2), such as Data Catalogs (S2.2) or Analytics Platforms (S2.4), following a Dual-Track Agile methodology.

**Discovery Track (Frontstage - Defining the Right Product):**
1.  **Data Product Canvas Workshop:** Defining the data domain, consumers, value proposition, and key use cases.
2.  **Requirements & Customization Workshop:** Prioritizing the product backlog and defining customization needs.
3.  **Sprint Review & Demo:** Demonstrating working software and gathering feedback every two weeks.
4.  **Phased UAT (User Acceptance Testing):** Client validation of features and functionality in a staging environment.
5.  **Go-Live and Handover:** Production deployment, final knowledge transfer, and official handover.

**Delivery Track (Backstage - Building the Product Right):**
1.  **Sprint Planning:** Selecting and breaking down user stories from the prioritized backlog.
2.  **Platform Configuration & Deployment:** Setting up and configuring the core platform components.
3.  **Iterative Customization Development:** Developing custom features, integrations, and extensions in sprints.
4.  **Security & Performance Testing:** Conducting rigorous testing for vulnerabilities and performance bottlenecks.
5.  **Documentation & Training Material Preparation:** Creating user guides, technical documentation, and training content.

**Agile Cadence:** Sprints are typically 2 weeks long, concluding with a Sprint Review and Retrospective. For a detailed breakdown of the work hierarchy, see [`agile-work-hierarchy.md`](./agile-work-hierarchy.md).

### Data Asset Valuation Pattern (S1.5)

A specialized pattern for the Data Asset Valuation service, combining advisory and technical analysis.

**Frontstage:**
1.  **Kick-off & Stakeholder Alignment:** Aligning on valuation objectives, scope, and methodology.
2.  **Data Domain Prioritization Workshop:** Identifying high-value data domains for initial valuation.
3.  **Valuation Methodology Workshop:** Selecting appropriate models from Infonomics and other frameworks (e.g., Deloitte 2025).
4.  **Interim Findings Presentation:** Validating initial valuation results and data quality impact.
5.  **Executive Value Communication Session:** Presenting the financial and strategic value of data assets to leadership.
6.  **Final Presentation & Roadmap:** Delivering the complete valuation report and a data monetization/value realization roadmap.

**Backstage:**
1.  **Data Asset Inventory & Profiling:** Cataloging and profiling data assets to understand their characteristics.
2.  **COPQ (Cost of Poor Quality) Analysis:** Quantifying the financial impact of data quality issues.
3.  **Valuation Model Application:** Applying selected models (e.g., IVF, BVF, Income, Cost, Market approaches).
4.  **Quality-Value Correlation Analysis:** Correlating data quality scores with business value and financial impact.
5.  **Monetization Opportunity Assessment:** Identifying internal and external data monetization opportunities.
6.  **Report Compilation & Quality Review:** Compiling the final report and conducting an internal quality assurance review.

**Agile Cadence:** This service follows a milestone-based approach (e.g., Milestone 1: Discovery, Milestone 2: Valuation, Milestone 3: Strategy). For the internal cost model, see [`cogs-methodology.md`](./cogs-methodology.md).

### Training & Certification Pattern (Pillar 3)

This pattern applies to all public and in-house training services (S3.1-S3.4).

**Frontstage:**
1.  **Information Session & Webinars:** Providing information to prospective participants.
2.  **Online Registration & Payment:** Self-service portal for registration and payment.
3.  **Training Delivery:** Instructor-led training, either in-person or virtual.
4.  **Post-Training Support:** Access to materials, forums, and instructor support after the training.

**Backstage:**
1.  **Curriculum Development & Updates:** Continuously updating course content to reflect industry changes (e.g., DMBOK 3.0 project).
2.  **Logistics Management:** Managing venues, virtual platforms, and materials.
3.  **Accreditation & Certification Body Liaison:** Maintaining relationships with bodies like DAMA International and BNSP.
4.  **Marketing & Sales:** Promoting training programs to target audiences.

### GenAI-Enhanced Delivery Pattern

For services integrating Generative AI capabilities (e.g., S2.1, S2.4, S2.6), this pattern adds a crucial layer of responsibility and governance.

**Frontstage:**
1.  **AI Readiness Assessment:** Evaluating data quality, infrastructure, and governance readiness for AI.
2.  **Use Case Prioritization Workshop:** Identifying high-value GenAI use cases with the AI Value Canvas.
3.  **Proof of Concept (PoC) Demo:** Demonstrating a functional GenAI prototype within 2-4 weeks.
4.  **Production Deployment Review:** Validating model performance, bias testing, and explainability with stakeholders.
5.  **Go-Live & Monitoring Setup:** Deploying the solution with robust guardrails and monitoring dashboards.

**Backstage:**
1.  **Data Pipeline Assessment:** Evaluating data readiness for AI/ML training and RAG.
2.  **Model Selection & Fine-tuning:** Selecting the appropriate LLM/SLM and designing the RAG architecture.
3.  **Responsible AI Review:** Conducting a FATE (Fairness, Accountability, Transparency, Explainability) assessment.
4.  **Security & Privacy Review:** Implementing data masking, PII detection, and compliance checks.
5.  **MLOps/LLMOps Setup:** Establishing a CI/CD pipeline, model versioning, and drift monitoring.

**Guardrails:** Every GenAI deployment must include a set of technical and procedural guardrails to ensure safe and responsible operation. These include:
-   **Input/Output Filtering:** Automated PII filtering to prevent data leakage.
-   **Hallucination Detection:** Mechanisms to flag potentially non-factual outputs, often by cross-referencing with a verified knowledge base.
-   **Bias Monitoring:** Continuous testing to detect and mitigate demographic or other biases.
-   **Human-in-the-Loop (HITL):** Workflows for human validation in high-risk or low-confidence scenarios.
-   **Output Quality Monitoring:** Real-time dashboards for metrics like relevance, coherence, and safety.
-   **Data Provenance Tracking:** Logging the data sources used for training and generation to ensure transparency.

#### Responsible AI Review Checklist

Before deployment, every GenAI solution must pass a *Responsible AI Review*. The following checklist serves as a template.

| Kategori | Item Pemeriksaan | Status (Pass/Fail/N.A.) |
| :--- | :--- | :--- |
| **Fairness** | Has the model been tested for bias against different demographic groups? | *To be filled per project* |
| | Is there a mitigation strategy if bias is detected? | *To be filled per project* |
| **Accountability** | Who is responsible for the model's outputs? | *To be filled per project* |
| | Is there a clear escalation path for problematic outputs? | *To be filled per project* |
| **Transparency** | Are users informed they are interacting with an AI system? | *To be filled per project* |
| | Can the data sources used by the model be explained? | *To be filled per project* |
| **Explainability** | Can the system provide a rationale for how an output was generated? | *To be filled per project* |
| **Security** | Are there protections against prompt injection or adversarial attacks? | *To be filled per project* |
| **Privacy** | Is user data anonymized or processed in a privacy-preserving manner? | *To be filled per project* |
| **Reliability** | Does the model perform consistently across various scenarios? | *To be filled per project* |

### Data Mesh/Fabric Delivery Pattern

For services implementing modern data architectures like Data Mesh or Data Fabric (e.g., S1.1, S2.2).

**Frontstage:**
1.  **Domain Discovery Workshop:** Identifying business domain boundaries and potential data products.
2.  **Data Product Canvas per Domain:** Defining ownership, SLAs, and consumers for each data product.
3.  **Self-Serve Platform Demo:** Demonstrating the capabilities of the data infrastructure platform.
4.  **Domain Team Onboarding:** Training domain teams to become data product owners.
5.  **Federated Governance Activation:** Launching the federated governance operating model.

**Backstage:**
1.  **Domain Topology Mapping:** Analyzing the organizational structure against data domains.
2.  **Data Contract Design:** Designing ODCS-compliant data contracts for interoperability.
3.  **Platform Engineering:** Building and configuring the self-serve data infrastructure.
4.  **Computational Governance:** Automating policy enforcement through metadata and code.
5.  **Interoperability Testing:** Validating cross-domain data flows and contract adherence.

## Commercial Models

IDEAS employs a flexible range of commercial models tailored to the service type and client context.

| Model | Layanan | Deskripsi | Value Indicator |
| :--- | :--- | :--- | :--- |
| **Fixed-Price** | Advisory (S1.x), Portal Implementation (S2.x) | Harga tetap berdasarkan paket atau ruang lingkup yang jelas. | Deliverable completion |
| **Fixed + Success Fee** | Data Asset Valuation (S1.5) | Fixed fee + success fee berdasarkan realisasi nilai atau valuasi yang teridentifikasi. | Monetization value identified/realized |
| **Outcome-Based** | GenAI Solutions (S2.6), Analytics (S2.4) | Fee terikat pada hasil bisnis yang terukur. | KPI improvement (e.g., 20% faster decisions) |
| **Retainer** | Strategic Partnership, DGO as a Service (S1.2) | Biaya tetap + retainer bulanan/triwulanan untuk dukungan berkelanjutan. | Governance maturity score improvement |
| **Per-Participant** | Public Training (S3.1, S3.2) | Biaya per peserta untuk pelatihan publik. | Certification pass rate |
| **Fixed per Session** | In-House Training (S3.3, S3.4) | Harga tetap per sesi pelatihan, dengan potensi diskon volume. | Knowledge assessment scores |
| **Subscription (PaaS)** | Government Portal PaaS (S2.5) | Biaya setup awal + langganan tahunan. | Platform uptime, active users |
| **License + Maintenance** | Platform Products (S2.1, S2.2, S2.3) | Lisensi perangkat lunak + biaya pemeliharaan tahunan. | Feature utilization rate |

> **Value-Based Pricing Principle:** IDEAS targets a minimum **10:1 value-to-fee ratio**. Every Rp 1 invested by the client should generate at least Rp 10 in measurable value (cost savings, revenue uplift, risk reduction, or efficiency gains). See [`business-frameworks.md`](./business-frameworks.md) Section 7 for pricing strategy details and [`rab-hps-methodology.md`](./rab-hps-methodology.md) for government procurement models.

## Success Metrics Framework

Every IDEAS service has measurable success metrics, categorized using the **Balanced Scorecard (BSC)** framework.

| BSC Perspective | Kategori | Contoh Metrik | Target |
| :--- | :--- | :--- | :--- |
| **Financial** | ROI | Return on Data Investment (RODI) | >300% dalam 3 tahun |
| | Cost Savings | Pengurangan biaya operasional terkait data | 15-30% YoY |
| | Revenue | Revenue dari inisiatif data monetization | Terukur dalam 12 bulan |
| **Customer** | Kepuasan | CSAT/NPS dari pemangku kepentingan | CSAT >4.2/5.0, NPS >50 |
| | Adopsi | Jumlah pengguna aktif, dataset terpublikasi | >80% target users active |
| | Persetujuan | Strategi disetujui oleh dewan direksi | 100% approval rate |
| **Internal Process** | Kualitas | Skor kualitas data (DQ Score) | >85% across critical dimensions |
| | Efisiensi | Pengurangan *time-to-insight* atau *time-to-market* | 30-50% reduction |
| | Compliance | Tingkat kepatuhan regulasi (UU PDP, SPBE) | 100% compliance |
| **Learning & Growth** | Kepemilikan | Data stewards ditugaskan per domain | 100% coverage |
| | Sertifikasi | Tingkat kelulusan sertifikasi (CDMP, BNSP) | >85% pass rate |
| | Literasi | Peningkatan skor literasi data organisasi | >20% improvement |

## Reporting Standards

| Frekuensi | Konteks | Contoh Layanan |
| :--- | :--- | :--- |
| Mingguan | Laporan kemajuan proyek | Advisory (S1.x) |
| Dua Mingguan | Laporan kemajuan sprint | Platform Implementation (S2.x) |
| Bulanan | Kinerja platform, uptime, statistik | PaaS (S2.5) |
| Per Milestone | Presentasi temuan, hasil UAT | Advisory, Implementation |
| Final | Dokumen strategi, laporan asesmen, serah terima | Semua Layanan |

## Deliverable Delivery Pattern

Every deliverable follows a standard quality assurance workflow:

```
Draft → Internal Review → Client Review → Revision → Approved → Delivered
```

Deliverables are typically submitted per milestone, not per sprint, to ensure they represent a coherent body of work. See [`service-deliverables-map.md`](./service-deliverables-map.md) for a detailed mapping of deliverables to services and milestones.

## Business Analysis Integration in Delivery

Every engagement involving Pillar 1 (Advisory) services must include a structured business analysis phase, leveraging frameworks from BABOK and others.

| Delivery Phase | Business Analysis Activity | Framework/Toolkit | Output Example |
| :--- | :--- | :--- | :--- |
| Discovery | Stakeholder analysis, current state assessment | SWOT, PESTEL, Five Forces | Situation Analysis Report |
| Strategy | Gap analysis, target state definition | BABOK Strategy Analysis | Business Requirements Document |
| Design | Solution architecture, requirements validation | BABOK Requirements Analysis | Solution Design Document |
| Implementation | Change impact assessment, adoption planning | Kotter 8-Step + ADKAR | Change Management Plan |
| Transition | Knowledge transfer, capability assessment | Technology Adoption Lifecycle | Training & Handover Report |

> For a complete reference, see [`business-frameworks.md`](./business-frameworks.md) (Section 4: Business Analysis Toolkit, Section 10: Change Management Playbook).

---
**See Also:**
- [`services-catalog.md`](./services-catalog.md): For a detailed list of all 15 services that these patterns apply to.
- [`task-decomposition.md`](./task-decomposition.md): For granular task breakdowns of each service.
- [`service-deliverables-map.md`](./service-deliverables-map.md): For mapping services to output deliverables.
- [`agile-work-hierarchy.md`](./agile-work-hierarchy.md): For the Agile work hierarchy (Initiative → Subtask).
- [`digital-data-product-lifecycle.md`](./digital-data-product-lifecycle.md): For the Digital & Data Product lifecycle methodology.
- [`cogs-methodology.md`](./cogs-methodology.md): For internal cost calculation principles.
- [`rab-hps-methodology.md`](./rab-hps-methodology.md): For government procurement pricing models (RAB/HPS).
- [`business-frameworks.md`](./business-frameworks.md): For BMC, Porter Value Chain, business analysis toolkit, and more.
- [`thought-leadership-frameworks.md`](./thought-leadership-frameworks.md): For PMBOK, Data Valuation, and other guiding frameworks.
- `../scripts/estimate_service_cost.py`: To calculate precise project costs based on task decomposition.


## Cross-Skill Integration

When executing service delivery patterns, leverage companion skills at each phase:

- **Discovery Phase**: Use `web-scraper` to collect client intelligence (SPBE scores, portal status, competitor data) before engagement. Use `dama-research` KA-14 for maturity assessment framework.
- **Analysis Phase**: Use `dama-research` knowledge areas for theoretical grounding. Apply KA-11 data quality dimensions, KA-01 governance frameworks, or KA-02 architecture patterns as appropriate.
- **Delivery Phase**: Use `dama-research/templates/deliverables/INDEX.md` for standardized output templates. Use `web-scraper` for ongoing data collection and monitoring.
- **Handover Phase**: Document data lineage using `dama-research` KA-09 metadata standards. Establish monitoring using `web-scraper` for continuous assessment.
