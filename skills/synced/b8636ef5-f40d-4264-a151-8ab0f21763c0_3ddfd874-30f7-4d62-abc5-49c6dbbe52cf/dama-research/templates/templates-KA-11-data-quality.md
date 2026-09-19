<!-- NAV-TOC -->
## Sections in This File

This file contains **12 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 24 | Data Quality Strategy |
| 360 | Data Quality Framework |
| 694 | Data Quality Dimensions |
| 1003 | Data Quality Metrics |
| 1307 | Data Quality Rules |
| 1643 | Data Profiling Results |
| 1993 | Data Quality Scorecard |
| 2357 | Data Quality Report |
| 2704 | Issue Log |
| 2973 | Remediation Plan |
| 3363 | Data Quality SLA |
| 3790 | Root Cause Analysis Report |

## Sections in This File

This file contains **13 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 1 | Data Quality Strategy |
| 337 | Data Quality Framework |
| 671 | Data Quality Dimensions |
| 980 | Data Quality Metrics |
| 1284 | Data Quality Rules |
| 1620 | Data Profiling Results |
| 1970 | Data Quality Scorecard |
| 2329 | End of Data Quality Scorecard Template |
| 2334 | Data Quality Report |
| 2681 | Issue Log |
| 2950 | Remediation Plan |
| 3340 | Data Quality SLA |
| 3767 | Root Cause Analysis Report |

---

# Data Quality Strategy


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Header](#31-document-header)
  - [3.2. Vision and Mission](#32-vision-and-mission)
  - [3.3. Guiding Principles](#33-guiding-principles)
  - [3.4. Strategic Objectives](#34-strategic-objectives)
  - [3.5. Data Quality Governance](#35-data-quality-governance)
  - [3.6. Data Quality Management Process](#36-data-quality-management-process)
  - [3.7. Technology and Tools Architecture](#37-technology-and-tools-architecture)
  - [3.8. Implementation Roadmap](#38-implementation-roadmap)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Vision and Mission](#42-vision-and-mission)
  - [4.3. Guiding Principles](#43-guiding-principles)
  - [4.4. Strategic Objectives](#44-strategic-objectives)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs to this Output)](#61-prerequisites-inputs-to-this-output)
  - [6.2. Consumers (Outputs that depend on this one)](#62-consumers-outputs-that-depend-on-this-one)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Quality Strategy** is a comprehensive, long-term plan that defines an organization's approach to achieving and maintaining high-quality data as a critical enterprise asset. It is a foundational component of the overall data governance framework and provides the roadmap for all data quality initiatives, ensuring alignment with business goals, regulatory requirements, and emerging technological trends.

This strategy articulates the principles, objectives, governance structures, processes, and technology architecture necessary to ensure that data is fit for its intended purpose, trustworthy, and compliant with applicable standards.

> According to DAMA-DMBOK 2nd Edition (Chapter 13), a data quality strategy is essential for proactively managing data as a critical asset. Looking forward, DAMA-DMBOK 3.0 (expected June 2025) emphasizes the integration of data quality with AI governance, data product management, and modern architectural paradigms such as Data Mesh and Lakehouse architectures.

The purpose of this document is to:
- Establish a clear vision and mission for data quality aligned with organizational strategy.
- Secure commitment and accountability from stakeholders across business and IT.
- Define roles, responsibilities, and governance mechanisms for data quality.
- Guide the allocation of resources and prioritization of initiatives.
- Embed data quality as a continuous, enterprise-wide capability that supports decision-making, operational efficiency, regulatory compliance (including GDPR, HIPAA, CCPA, and emerging AI regulations such as the EU AI Act), and customer satisfaction.

### 1.2. Scope

**Global** — This strategy applies to all data assets across the entire organization, encompassing all business units, departments, and data products. It covers data at every stage of its lifecycle, from creation or acquisition through transformation, consumption, archiving, and eventual deletion.

The strategy recognizes the increasing prevalence of distributed data ownership models, including domain-oriented Data Mesh implementations, and the need to manage data quality in multi-cloud, hybrid, and lakehouse environments. While specific data quality rules, metrics, and remediation approaches may be defined at the domain or product level, the principles, governance framework, and strategic objectives outlined here are universal and provide a consistent foundation.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Data Quality Strategy is a key deliverable of the Data Governance program. It operationalizes governance policies, standards, and stewardship models to ensure data quality is managed as a shared responsibility. See also `templates/templates-KA-01-data-governance.md` for detailed role definitions. |
| KA-02: Data Architecture | Data architecture must enable data quality through design principles such as data contracts, schema enforcement, and lineage tracking. Modern architectures like Data Mesh and Data Fabric require embedded quality controls and observability. See `../KA-02-data-architecture/` for architecture patterns supporting quality. |
| KA-03: Data Modeling and Design | High-quality data models enforce business rules and constraints at data entry points, preventing quality issues. Data products and contracts are emerging concepts that formalize data quality expectations at the model level. |
| KA-09: Metadata Management | Metadata provides critical context for defining, measuring, and remediating data quality issues. It supports lineage, impact analysis, and root cause identification, enabling proactive quality management. See `../KA-09-metadata-management/` for metadata strategy. |
| KA-12: Data Ethics and AI Governance | With the rise of AI and machine learning, data quality is integral to ethical AI practices. Ensuring data used in AI models is accurate, unbiased, and compliant with regulations like the EU AI Act is essential. See `../KA-12-data-ethics-ai-governance/` for governance integration. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Chief Data Officer (CDO) | Ultimately accountable for the existence, approval, and ongoing success of the enterprise Data Quality Strategy. Ensures alignment with business strategy, regulatory compliance, and emerging trends such as AI governance. |
| **R (Responsible)** | Data Quality Manager (DQ Mgr) | Responsible for drafting, maintaining, and overseeing the implementation of the Data Quality Strategy. Leads execution, coordinates cross-functional teams, and drives continuous improvement. |
| **S (Supportive)** | Data Governance Manager (DG Mgr) | Supports integration of the Data Quality Strategy within the broader governance framework, ensuring policies, stewardship, and compliance are aligned. Facilitates collaboration with data owners and stewards. |
| **C (Consulted)** | Data Owner (D-Owner), Data Architecture Manager (DA Mgr), AI Ethics Officer | Provide critical input on business requirements, architectural feasibility, AI governance considerations, and priorities for their respective domains. |
| **I (Informed)** | Data Governance Council (DGC), Chief AI Officer (CAIO), IT Operations | Kept informed of strategy progress, performance metrics, and emerging risks. Provide oversight and strategic guidance, especially on AI and cloud-native data quality implications. |

### 2.2. Section-Level RASCI

| Strategy Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Vision and Objectives | DQ Mgr | D-Owner, Business Leaders, CAIO | CDO |
| DQ Principles | DQ Mgr | DGC, DA Mgr, AI Ethics Officer | CDO |
| Governance and Roles | DG Mgr | DQ Mgr, HR, Data Stewards | CDO |
| DQ Processes | DQ Mgr | Data Stewards, Data Custodians, MLOps Engineer | DQ Mgr |
| Technology and Tools | DA Mgr | DQ Mgr, IT Operations, FinOps | CDO |
| Implementation Roadmap | DQ Mgr | DGC, PMO, AI Governance Committee | CDO |

---

## 3. Template

> *The following is the standardized template for creating a Data Quality Strategy. This template provides a comprehensive structure to guide organizations in defining their approach to managing data quality.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | [Organization Name] Data Quality Strategy |
| Document ID | STR-DQ-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Review Date | [YYYY-MM-DD, typically annual] |
| Owner | [Data Quality Manager Name] |
| Approver | [Chief Data Officer Name] |

### 3.2. Vision and Mission

> *Define the long-term vision for data quality and the mission of the data quality program. The vision should be aspirational, while the mission should be actionable and state the program's purpose.*

**Vision**: [e.g., "To create an environment where all strategic decisions are made with complete confidence in the underlying data, enabling innovation and trust across the enterprise."]

**Mission**: [e.g., "To proactively manage the quality of our enterprise data assets through a collaborative, continuous improvement lifecycle of assessment, monitoring, and remediation, ensuring data is fit for purpose, compliant, and supports business value creation in a cloud-native, AI-enabled environment."]

### 3.3. Guiding Principles

> *List the core principles that will guide all data quality decisions and activities. These are high-level, foundational beliefs.*

1.  **Data Quality is a Business Responsibility**: Data quality ownership resides with business stakeholders, with IT and data teams providing enabling support and technology.
2.  **Prevention over Correction**: Emphasize embedding quality controls at data creation points and upstream processes to minimize downstream remediation.
3.  **Fit for Purpose**: Data quality is context-dependent; quality criteria must align with specific business use cases and data products.
4.  **Data Quality is Measurable and Transparent**: All initiatives will be driven by clear, actionable metrics linked to business outcomes and made visible to stakeholders.
5.  **Continuous Improvement and Automation**: Data quality is an ongoing program leveraging automation, AI-powered anomaly detection, and integration with DataOps, MLOps, and FinOps practices.
6.  **Compliance and Ethical Use**: Data quality efforts will ensure compliance with data protection laws (GDPR, HIPAA, CCPA) and emerging AI regulations (EU AI Act), supporting ethical data and AI governance.
7.  **Agentic Stewardship**: Empower data stewards and data product managers with tools and authority to act decisively on quality issues.
8.  **Modern Architecture Alignment**: Support data quality in distributed architectures including Data Mesh, Data Fabric, and Lakehouse, ensuring interoperability and data contracts enforcement.

### 3.4. Strategic Objectives

> *Define the high-level, SMART (Specific, Measurable, Achievable, Relevant, Time-bound) objectives of the data quality strategy. These should link directly to organizational goals.*

| # | Strategic Goal | Objective | Target Metric | Timeline |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [e.g., Improve Customer Satisfaction] | Reduce customer data errors impacting service delivery. | Decrease customer data-related complaints by 25%. | 18 months |
| 2 | [e.g., Increase Operational Efficiency] | Eliminate rework caused by inaccurate product data. | Reduce order processing errors by 20%. | 12 months |
| 3 | [e.g., Enhance Analytics and BI] | Improve completeness and accuracy of sales data for analytics. | Achieve 98% data quality score on critical sales fields. | 24 months |
| 4 | [e.g., Ensure Regulatory Compliance] | Maintain data quality standards to meet GDPR, HIPAA, and EU AI Act requirements. | Zero non-compliance incidents related to data quality. | Ongoing |

### 3.5. Data Quality Governance

> *Describe the roles, responsibilities, and structures that will govern the data quality program. Reference the main Roles and Responsibilities output for detailed role descriptions.*

**Input needed**: `templates/templates-KA-01-data-governance.md`  
**Who fills this**: DG Mgr, DQ Mgr

- **Data Quality Manager (DQ Mgr)**: Leads the data quality program, manages the DQ team, coordinates cross-domain initiatives, and ensures alignment with governance and compliance requirements.
- **Data Stewards**: Domain experts responsible for defining data quality rules, thresholds, and remediation priorities for their data domains. Act as agentic stewards empowered to enforce quality standards.
- **Data Custodians**: Technical personnel responsible for implementing data quality controls, monitoring, and remediation within systems and pipelines.
- **Data Product Managers**: Oversee data products ensuring quality, availability, and compliance, working closely with stewards and custodians.
- **Data Quality Working Group**: A cross-functional team of data stewards, custodians, architects, and AI governance representatives that meets regularly to review data quality metrics, prioritize initiatives, and address escalations.
- **AI Ethics Officer**: Ensures that data quality supports ethical AI practices, including bias mitigation and compliance with AI governance frameworks.
- **Data Governance Council (DGC)**: Provides oversight, strategic guidance, and resource allocation for the data quality program.

### 3.6. Data Quality Management Process

> *Outline the end-to-end process for managing data quality. This should be a cyclical process.*

1.  **Assess Data Quality**: Profile data sources using automated tools to establish baselines, identify quality hotspots, and detect anomalies using AI-powered techniques.
2.  **Define Data Quality Rules**: Collaborate with data stewards and product managers to establish business rules, validation criteria, and thresholds aligned with data contracts and product SLAs.
3.  **Measure and Monitor**: Implement continuous monitoring via dashboards and scorecards integrated into data pipelines, with real-time alerts for deviations.
4.  **Analyze and Remediate**: Conduct root cause analysis for quality issues, distinguishing between tactical data cleansing and strategic process improvements. Leverage DataOps and MLOps practices to embed quality controls.
5.  **Report and Communicate**: Provide transparent, timely reporting to stakeholders, including executive summaries for governance bodies and detailed metrics for operational teams.
6.  **Review and Improve**: Regularly review data quality processes, update rules and tools, and incorporate lessons learned to drive continuous improvement.

### 3.7. Technology and Tools Architecture

> *Describe the technology stack that will support the data quality strategy. Reference the Tools and Automation section for specific tool recommendations.*

- **Data Profiling Tools**: Automated tools that analyze data sources to understand structure, content, and quality, supporting initial assessments and ongoing monitoring.
- **Data Quality Engine**: Platforms enabling definition, execution, and management of data quality rules, validations, and cleansing workflows. Support integration with data contracts and product SLAs.
- **Monitoring and Reporting Dashboard**: BI tools or specialized dashboards that visualize data quality metrics, trends, and issue status for stakeholders at all levels.
- **Issue Management System**: Workflow and ticketing systems (e.g., Jira, ServiceNow) to track data quality issues, remediation activities, and resolution timelines.
- **AI-Powered Anomaly Detection**: Machine learning models embedded in pipelines to detect subtle or emerging data quality issues beyond rule-based checks.
- **Integration with DataOps, MLOps, FinOps**: Tools and processes that embed data quality checks into CI/CD pipelines, model training, and cost management workflows.
- **Cloud-Native and Multi-Cloud Support**: Architecture designed to operate seamlessly across cloud platforms, supporting data mesh and fabric implementations with federated governance and quality enforcement.

### 3.8. Implementation Roadmap

> *Provide a high-level, phased roadmap for the implementation of the data quality strategy.*

| Phase | Timeline | Key Activities | Expected Outcomes |
| :--- | :--- | :--- | :--- |
| **Phase 1: Foundation** | [e.g., Q1-Q2 2026] | Establish Data Quality Working Group, select and pilot DQ tools, define initial data quality rules for a pilot domain (e.g., Customer). Develop baseline metrics and reporting. | DQ baseline established, governance structures in place, initial toolset operational. |
| **Phase 2: Expansion** | [e.g., Q3 2026 - Q2 2027] | Roll out DQ program to additional high-priority domains (e.g., Product, Financials). Develop enterprise-wide DQ dashboards. Integrate with DataOps and MLOps pipelines. | Measurable improvements in multiple domains, enterprise visibility, and integration with operational workflows. |
| **Phase 3: Optimization** | [e.g., Q3 2027 onwards] | Embed DQ controls into data creation and ingestion processes (prevention). Expand automation and AI-powered anomaly detection. Foster agentic stewardship and data product management. | Shift from reactive to proactive DQ management, data quality embedded in culture, compliance assured, and continuous improvement institutionalized. |

---

## 4. Example

> *The following is a filled-in example of a Data Quality Strategy for a fictional company, **GlobalRetail Inc.**.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | GlobalRetail Inc. Data Quality Strategy |
| Document ID | STR-DQ-001 |
| Version | 1.0 |
| Effective Date | 2026-02-08 |
| Review Date | 2027-02-08 |
| Owner | John Smith, Data Quality Manager |
| Approver | Jane Doe, Chief Data Officer |

### 4.2. Vision and Mission

**Vision**: "To power a world-class, personalized customer experience through complete, accurate, and timely data across all channels, enabling innovation and trust."

**Mission**: "To establish and operate a sustainable data quality program that ensures our customer, product, and sales data is trusted, secure, and fit for purpose, enabling GlobalRetail Inc. to drive revenue growth, operational excellence, and ethical AI deployment."

### 4.3. Guiding Principles

1.  **Data Quality is a Shared Responsibility**: Every employee who creates, uses, or manages data is responsible for its quality.
2.  **Fix at the Source**: Prioritize fixing root causes of data quality issues in source systems over downstream cleansing.
3.  **Quality is Defined by Business Impact**: Prioritize efforts based on impact on customer satisfaction, supply chain efficiency, and AI model performance.
4.  **Transparency is Key**: Data quality metrics and issue statuses are visible to all relevant stakeholders.
5.  **Pragmatic and Iterative**: Deliver value incrementally, focusing on continuous improvement rather than a single, large-scale project.
6.  **Compliance and Ethics**: Ensure data quality supports compliance with GDPR, HIPAA, and the EU AI Act, and fosters ethical AI use.
7.  **Leverage Modern Architecture**: Support data quality in our Data Mesh and Lakehouse environments, enforcing data contracts and product SLAs.

### 4.4. Strategic Objectives

| # | Strategic Goal | Objective | Target Metric | Timeline |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Improve E-commerce Conversion | Reduce orders delayed due to inaccurate product dimension or stock level data. | Decrease "Inaccurate Stock" order cancellations by 30%. | 12 months |
| 2 | Enhance Marketing ROI | Improve customer segmentation by ensuring completeness of customer demographic and preference data. | Increase email campaign open rates by 10% through better targeting. | 18 months |
| 3 | Streamline Supply Chain | Ensure accuracy and timeliness of supplier and shipment data to reduce logistics errors. | Reduce incorrect shipment fines by 25%. | 24 months |
| 4 | Ensure AI Model Reliability | Improve data quality feeding AI models to reduce bias and errors. | Achieve 95% data quality score on AI training datasets. | 18 months |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics and KPIs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Governance Roles and Responsibilities | Deliverable | **templates/templates-KA-01-data-governance.md** |
| AI Governance Framework | Knowledge Area | **templates/templates-KA-12-data-handling-ethics.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The strategy has been formally approved by the CDO and endorsed by the Data Governance Council.
- [ ] The vision and objectives are directly aligned with the organization's annual strategic goals and emerging AI governance requirements.
- [ ] All key roles and responsibilities for data quality, including new roles such as AI Ethics Officer and Data Product Manager, have been defined and assigned.
- [ ] The implementation roadmap includes clear, achievable phases with defined timelines, outcomes, and integration points with DataOps, MLOps, and FinOps.
- [ ] Success metrics are defined for each strategic objective, are measurable, and linked to business outcomes.
- [ ] The strategy clearly outlines the end-to-end process for identifying, measuring, remediating, and continuously improving data quality.
- [ ] The strategy accounts for compliance with relevant regulations including GDPR, HIPAA, CCPA, and the EU AI Act.
- [ ] The technology architecture supports modern data management paradigms (Data Mesh, Lakehouse) and cloud-native environments.

### 5.2. Review Checklist

| # | Review Question | Pass/Fail |
| :--- | :--- | :--- |
| 1 | Is the strategy clear, concise, and understandable to both business and technical audiences? | |
| 2 | Does the scope clearly define what is in and out of the program's purview, including AI data and multi-cloud environments? | |
| 3 | Are the guiding principles practical, forward-looking, and aligned with company culture and emerging trends? | |
| 4 | Is the proposed technology architecture feasible, scalable, and does it integrate with existing and planned systems? | |
| 5 | Has the strategy been reviewed and received input from key stakeholders (e.g., Data Owners, IT, AI Governance, business leaders)? | |
| 6 | Does the roadmap account for resource availability, dependencies on other projects, and regulatory timelines? | |
| 7 | Are automation and AI-powered data quality capabilities adequately addressed? | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs to this Output)

| Output | Relationship |
| :--- | :--- |
| [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) | Provides the executive mandate and authority for establishing a data quality program. |
| [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) | Defines the overall governance structure, roles, and policies within which the Data Quality Strategy operates. |
| [templates/templates-KA-09-metadata-management.md](templates/templates-KA-09-metadata-management.md) | Provides metadata standards and lineage requirements critical for data quality management. |

### 6.2. Consumers (Outputs that depend on this one)

| Output | Relationship |
| :--- | :--- |
| [02-data-quality-framework.md](./02-data-quality-framework.md) | This strategy provides the high-level vision and objectives that the Data Quality Framework will detail and operationalize. |
| **templates/templates-KA-12-data-handling-ethics.md** | Relies on the Data Quality Strategy to ensure AI data governance and quality standards are met. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Examples | Open Source Examples |
| :--- | :--- | :--- |
| **Data Profiling & Discovery** | Informatica DQ, Talend Data Quality, Ataccama ONE | Great Expectations, Pandas Profiling, Deequ |
| **Data Cleansing & Standardization** | Trillium, Melissa Data, SAP Data Services | OpenRefine, dbt (for transformations) |
| **DQ Monitoring & Reporting** | Collibra, Alation (with DQ partners), Tableau, Power BI | Custom dashboards using Grafana, Superset |
| **Issue Management & Workflow** | Jira, ServiceNow, ServiceNow ITSM | Redmine, osTicket |
| **AI-Powered Anomaly Detection** | IBM Watson OpenScale, DataRobot MLOps | Custom ML models integrated with monitoring tools |

### 7.2. Automation Opportunities

- **Automated Profiling**: Automatically profile new data sources upon ingestion into data lakes or warehouses to establish immediate quality baselines.
- **Continuous Monitoring**: Embed data quality checks directly into data pipelines using tools like Great Expectations or dbt tests to validate data in-stream and prevent propagation of errors.
- **Automated Alerting and Ticketing**: Configure workflows to automatically generate alerts and create remediation tickets in systems like Jira when data quality metrics fall below thresholds.
- **AI-Powered Anomaly Detection**: Deploy machine learning models to learn normal data patterns and detect anomalies or emerging quality issues beyond rule-based systems.
- **Integration with DataOps, MLOps, and FinOps**: Automate quality validations as part of CI/CD pipelines for data and ML models, ensuring quality gates before deployment.
- **Data Contracts Enforcement**: Automate validation of data contracts between producers and consumers to ensure agreed-upon quality and SLA adherence.
- **Agentic Stewardship Enablement**: Provide stewards and product managers with automated dashboards and decision support tools to act swiftly on quality issues.

---

## 8. References

1.  **DAMA-DMBOK2**: Data Management Body of Knowledge, 2nd Edition. Chapter 13, "Data Quality".
2.  **DAMA-DMBOK3 (forthcoming)**: Expected June 2025, will include expanded guidance on AI governance, data products, and modern architectures.
3.  **Internal Reference**: `templates/templates-KA-01-data-governance.md` - Detailed definitions of governance roles.
4.  **Internal Reference**: `templates/templates-KA-01-data-governance.md` - Executive mandate for data quality program.
5.  **EU AI Act**: European Union regulation on AI systems, emphasizing data quality and governance requirements.
6.  **GDPR, HIPAA, CCPA**: Data protection regulations with data quality implications.
7.  **Data Mesh Principles**: For decentralized data ownership and quality management.
8.  **Data Product Management**: Emerging discipline formalizing data as a product with quality SLAs.
9.  **AI Governance Frameworks**: Integration of data quality with ethical AI practices.


---

# Data Quality Framework


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Introduction](#31-introduction)
  - [3.2. Data Quality Principles](#32-data-quality-principles)
  - [3.3. Data Quality Roles and Responsibilities](#33-data-quality-roles-and-responsibilities)
  - [3.4. Data Quality Dimensions](#34-data-quality-dimensions)
  - [3.5. Data Quality Processes](#35-data-quality-processes)
  - [3.6. Data Quality Technology and Tools](#36-data-quality-technology-and-tools)
- [4. Example](#4-example)
  - [4.1. Introduction (GlobalRetail Inc.)](#41-introduction-globalretail-inc)
  - [4.2. Data Quality Principles (GlobalRetail Inc.)](#42-data-quality-principles-globalretail-inc)
  - [4.3. Data Quality Roles (GlobalRetail Inc.)](#43-data-quality-roles-globalretail-inc)
  - [4.4. Data Quality Dimensions (GlobalRetail Inc.)](#44-data-quality-dimensions-globalretail-inc)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites](#61-prerequisites)
  - [6.2. Consumers](#62-consumers)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Quality Framework** is a comprehensive, systematic approach to ensuring that data is fit for its intended purpose. It consists of a collection of principles, policies, standards, processes, roles, and technologies that work together to manage and improve the quality of an organization's data assets. The framework provides the structure for all data quality activities, from defining quality dimensions to monitoring, reporting, and remediating data issues.

> The purpose of the Data Quality Framework is to operationalize the Data Quality Strategy, creating a repeatable and scalable system for embedding data quality into the fabric of the organization's operations and culture. It supports the evolving needs of modern data environments, including cloud-native architectures, data mesh and fabric paradigms, and AI governance requirements.

This framework is designed to be adaptable to emerging trends such as agentic data stewardship, data contracts, and the integration of MLOps and DataOps practices, ensuring data quality remains a foundational pillar in the enterprise data ecosystem.

### 1.2. Scope

**Global** — This framework applies to all data across the enterprise, regardless of system, business unit, or data domain. It provides the overarching structure that guides the implementation of data quality controls and processes for all data products, including those managed in multi-cloud, lakehouse, and hybrid environments.

It encompasses structured and unstructured data, streaming and batch data, as well as data used in AI/ML models, ensuring compliance with regulatory frameworks such as GDPR, HIPAA, CCPA, and the emerging EU AI Act.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Data Governance program authorizes and provides the oversight for the Data Quality Framework. The framework is a key component of the overall governance structure, including AI governance and ethical data use. |
| KA-02: Data Architecture | The Data Architecture defines the systems and data flows where data quality rules and controls will be implemented, including modern architectures such as Data Mesh and Data Fabric. |
| KA-09: Metadata Management | Metadata is essential for understanding data lineage, definitions, and business rules, which are critical inputs for the Data Quality Framework and support automated data quality monitoring. |
| KA-10: Reference and Master Data | Master and reference data are often the first domains to which the Data Quality Framework is applied, as their quality has a cascading impact across the organization. |
| KA-12: Data Ethics and AI Governance | Emerging area focusing on ethical considerations and governance of AI models, which rely heavily on high-quality data inputs governed by this framework. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Governance Manager (DG Mgr) | Ultimately accountable for the definition, approval, and maintenance of the Data Quality Framework, ensuring alignment with enterprise data governance and AI governance policies. |
| **R (Responsible)** | Data Quality Manager (DQ Mgr) | Responsible for drafting, implementing, and managing the Data Quality Framework, including integration with DataOps and MLOps teams. |
| **S (Supportive)** | Data Quality Analyst (DQ Analyst) | Supports the DQ Manager in developing and implementing the framework components, such as profiling data, defining rules, and supporting automated monitoring. |
| **C (Consulted)** | Data Architect (D-Arch), Data Steward (D-Steward), AI Ethics Officer | Consulted to ensure the framework is architecturally sound, meets business needs, and aligns with ethical AI and data governance standards. |
| **I (Informed)** | All DMO Members, Data Product Managers, CAIO | Kept informed of the framework's content, updates, and its role in supporting data products and AI initiatives. |

### 2.2. Section-Level RASCI

| Framework Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| DQ Principles & Policies | DQ Mgr | DG Mgr, DGC, AI Ethics Officer | CDO |
| DQ Roles & Responsibilities | DQ Mgr | HR, DG Mgr, CAIO | DGC |
| DQ Dimensions & Metrics | DQ Analyst | D-Steward, Business SMEs, Data Product Managers | DQ Mgr |
| DQ Processes & Procedures | DQ Mgr | D-Steward, IT Operations, MLOps Engineer | DG Mgr |
| DQ Technology & Tools | D-Arch | DQ Mgr, Enterprise Architect, FinOps Lead | CIO |

---

## 3. Template

> *The following is the standardized template for a Data Quality Framework. This document outlines the core components required to establish a successful data quality program.*

### 3.1. Introduction

> *Provide a brief introduction to the Data Quality Framework, its purpose, and the intended audience.*

**Input needed**: Data Quality Strategy, Data Governance Charter, AI Governance Policy.  
**Who fills this**: DQ Mgr.

[Insert Introduction]

The introduction should emphasize the criticality of data quality in supporting not only traditional business intelligence and operational reporting but also advanced analytics, AI/ML models, and data products. It should highlight the framework’s role in enabling compliance with regulatory requirements such as GDPR and the EU AI Act, and its adaptability to modern data architectures like Data Mesh and Lakehouse.

### 3.2. Data Quality Principles

> *Define the fundamental principles that guide the organization's approach to data quality. These should be high-level, timeless statements.*

**Input needed**: Corporate values, Data Governance Charter, AI Ethics Guidelines.  
**Who fills this**: DQ Mgr, DGC, AI Ethics Officer.

- **DQ is a Shared Responsibility**: All employees who create, manage, or use data are responsible for its quality, including AI model developers and data product teams.
- **DQ is Proactive and Preventive**: Focus on preventing data quality issues at the source through automated validation, data contracts, and embedded controls.
- **DQ is Business-Driven and Customer-Centric**: Data quality priorities are determined by business impact, customer experience, and strategic importance, including AI outcomes.
- **DQ is Measured, Monitored, and Transparent**: Continuously measure data quality, report transparently, and integrate with data observability platforms.
- **DQ Supports Ethical and Compliant Data Use**: Ensure data quality practices uphold privacy, security, and ethical standards, supporting compliance with GDPR, HIPAA, CCPA, and the EU AI Act.
- **DQ is Adaptive and Evolves with Technology**: The framework embraces emerging technologies and methodologies such as Data Mesh, Data Fabric, MLOps, and FinOps integration.

### 3.3. Data Quality Roles and Responsibilities

> *Detail the specific roles and responsibilities for data quality management across the organization. Reference the main Roles and Responsibilities output for full definitions.*

**Input needed**: `templates/templates-KA-01-data-governance.md`, AI Governance Role Definitions.  
**Who fills this**: DQ Mgr.

| Role | Key Data Quality Responsibilities |
| :--- | :--- |
| Data Owner | Accountable for the quality of data within their domain, including ensuring data contracts are enforced and data products meet quality standards. |
| Data Steward | Responsible for defining data quality rules, thresholds, and remediation processes; acts as the liaison between business and technical teams. |
| Data Quality Manager | Manages the overall DQ program and framework, coordinates with AI governance and DataOps teams to embed quality controls. |
| Data Quality Analyst | Profiles data, analyzes DQ issues, develops and tests DQ rules, and supports automated monitoring and reporting. |
| Data Producer/Creator | Responsible for creating high-quality data at the point of entry, including developers embedding validation in applications and pipelines. |
| Data Consumer | Responsible for reporting data quality issues they encounter and providing feedback to improve data products and services. |
| AI Ethics Officer | Ensures data quality practices support ethical AI development, including bias detection and data provenance. |
| MLOps Engineer | Integrates data quality checks into ML pipelines and monitors model input data quality continuously. |
| Data Product Manager | Oversees data products, ensuring they meet defined quality standards and customer expectations. |

### 3.4. Data Quality Dimensions

> *Define the standard set of data quality dimensions the organization will use to measure and assess data quality. Provide a definition for each.* 

**Input needed**: DAMA-DMBOK, industry best practices, AI governance frameworks.  
**Who fills this**: DQ Analyst, DQ Mgr.

| Dimension | Definition |
| :--- | :--- |
| **Accuracy** | The degree to which data correctly represents the 'real-world' object or event, including correctness for AI model training data. |
| **Completeness** | The proportion of stored data against the potential of 100% complete, ensuring no critical data elements are missing. |
| **Consistency** | The absence of difference when comparing two or more representations of a thing against a definition, across systems and data products. |
| **Timeliness** | The degree to which data represents reality from the required point in time, supporting near real-time analytics and operational decisions. |
| **Uniqueness** | No thing will be recorded more than once based upon how that thing is identified, preventing duplicates that can skew analytics and AI outcomes. |
| **Validity** | The degree to which data conforms to the syntax (format, type, range) of its definition, including adherence to data contracts and schemas. |
| **Integrity** | The degree to which data is complete, unaltered, and trustworthy throughout its lifecycle, including lineage and provenance. |
| **Relevance** | The degree to which data is applicable and useful for the intended business or analytical purpose, including AI model relevance. |

### 3.5. Data Quality Processes

> *Describe the key processes that make up the data quality lifecycle. Use diagrams where helpful.*

**Input needed**: ITIL/ITSM processes, business process models, DataOps/MLOps workflows.  
**Who fills this**: DQ Mgr.

#### 3.5.1. Data Profiling
> *The process of analyzing data sources to understand their structure, content, and quality levels. Includes automated profiling integrated with data observability tools.*

#### 3.5.2. Data Quality Assessment
> *The process of measuring data against the defined DQ dimensions and rules, including continuous validation in streaming and batch environments.*

#### 3.5.3. Data Quality Issue Management
> *The end-to-end process for identifying, logging, prioritizing, and resolving data quality issues, integrated with issue tracking systems and automated alerting.*

#### 3.5.4. Data Cleansing and Remediation
> *The process of correcting or removing inaccurate, incomplete, or invalid data, leveraging automated workflows and self-healing pipelines where possible.*

#### 3.5.5. Data Quality Monitoring and Reporting
> *The process of continuously monitoring data quality levels and reporting them to stakeholders via dashboards, including integration with AI model monitoring.*

#### 3.5.6. Data Contract Enforcement
> *The process of defining, implementing, and monitoring data contracts between data producers and consumers to ensure agreed quality standards are met.*

#### 3.5.7. Continuous Improvement and Feedback
> *The process of using data quality metrics and stakeholder feedback to refine rules, processes, and tools, fostering a culture of quality.*

### 3.6. Data Quality Technology and Tools

> *Describe the architecture and types of tools that will be used to support the data quality processes.*

**Input needed**: Technology standards, enterprise architecture blueprint, cloud-native and AI governance toolsets.  
**Who fills this**: D-Arch, DQ Mgr.

| Tool Category | Description | Recommended Tool(s) |
| :--- | :--- | :--- |
| Data Profiling Tools | Tools to analyze data sources and discover metadata, supporting automated and continuous profiling. | Informatica DQ, Talend Data Quality, Great Expectations |
| Data Quality Rule Engines | Platforms to define, execute, and manage DQ rules, including integration with DataOps and MLOps pipelines. | Ataccama, Deequ, Soda Core |
| Data Quality Dashboards | BI tools to visualize DQ metrics and trends, integrated with data observability platforms. | Power BI, Tableau, Collibra DQ |
| Issue Tracking Systems | Systems to log and manage DQ issues, supporting automated ticket creation and workflow management. | Jira, ServiceNow, Redmine |
| Data Contract Management | Tools to define and enforce data contracts between producers and consumers. | Monte Carlo, Datafold |
| AI Data Quality & Monitoring | Specialized tools for monitoring data quality in AI/ML pipelines, including bias detection and lineage. | Fiddler, WhyLabs |

---

## 4. Example

> *This section provides a realistic example of how the Data Quality Framework could be applied at a fictional company, GlobalRetail Inc.*

### 4.1. Introduction (GlobalRetail Inc.)

At GlobalRetail Inc., data is a critical asset that drives our customer experience, supply chain efficiency, and strategic decision-making. The purpose of this Data Quality Framework is to establish a consistent and scalable approach to ensuring our data is trustworthy and fit for purpose. This document is intended for all employees who interact with data, from our data engineers and analysts to our business leaders.

The framework supports our cloud-native data platforms, integrates with our Data Mesh architecture, and ensures compliance with GDPR and emerging AI regulations. It also aligns with our AI governance program to ensure responsible use of data in machine learning models.

### 4.2. Data Quality Principles (GlobalRetail Inc.)

- **DQ is Customer-Centric**: Our data quality efforts are prioritized based on their impact on the customer experience and business outcomes.
- **DQ is Embedded**: Data quality checks are automated and integrated directly into our data pipelines, applications, and AI model training workflows.
- **DQ is Transparent**: Data quality metrics are published openly and reviewed regularly by all data stakeholders, fostering trust and accountability.
- **DQ is a Journey, Not a Destination**: We are committed to continuous improvement in our data quality maturity, leveraging feedback and innovation.
- **DQ Supports Ethical AI**: We ensure data quality practices uphold fairness, privacy, and compliance in all AI initiatives.

### 4.3. Data Quality Roles (GlobalRetail Inc.)

| Role | Key Data Quality Responsibilities |
| :--- | :--- |
| Product Data Owner | Accountable for the accuracy and completeness of all product information in our PIM system, ensuring data contracts are enforced. |
| Customer Data Steward | Responsible for defining rules for customer name and address standardization and collaborating with AI Ethics Officer on bias mitigation. |
| Supply Chain DQ Analyst | Profiles supplier data, identifies anomalies, and works with suppliers to remediate issues using automated workflows. |
| Application Developer | Responsible for implementing data validation controls in the front-end of our e-commerce platform and integrating DQ checks in CI/CD pipelines. |
| MLOps Engineer | Ensures data quality checks are embedded in ML pipelines and monitors input data quality continuously. |

### 4.4. Data Quality Dimensions (GlobalRetail Inc.)

| Dimension | Example Application at GlobalRetail Inc. |
| :--- | :--- |
| **Accuracy** | A customer's shipping address must match the address validated by our third-party address verification service, ensuring correct delivery. |
| **Completeness** | 99.5% of all products listed on the website must have a product image and a detailed description to enhance customer experience. |
| **Consistency** | The price for a specific SKU must be the same in the ERP, the PIM, and on the e-commerce website to avoid customer confusion. |
| **Timeliness** | Inventory stock levels must be updated in near real-time, with a maximum latency of 5 minutes from the store POS system to online channels. |
| **Uniqueness** | Each customer should have only one unique customer ID, with no duplicate accounts, to ensure accurate marketing and service. |
| **Validity** | All email addresses collected must conform to the standard `user@domain.com` format and pass validation checks before use. |
| **Integrity** | Data lineage is tracked for all customer transactions to ensure traceability and auditability for compliance and analytics. |
| **Relevance** | Only relevant customer demographic data is collected and used for targeted marketing campaigns, respecting privacy and consent. |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Governance Roles and Responsibilities | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| AI Governance Framework | Knowledge Area | **templates/templates-KA-13-big-data-data-science.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The framework clearly defines DQ principles, roles, dimensions, and processes, incorporating modern data management and AI governance considerations.
- [x] The framework is aligned with the organization's Data Governance Charter, Data Strategy, and AI Governance policies.
- [x] The roles and responsibilities are clearly defined, including emerging roles such as AI Ethics Officer and MLOps Engineer.
- [x] The defined DQ dimensions are relevant to the business and include considerations for AI and data product quality.
- [x] The processes for DQ management are clearly documented, including data contract enforcement and continuous improvement.
- [x] The technology stack for data quality is identified, covering cloud-native, DataOps, and AI monitoring tools.

### 5.2. Review Checklist

| Reviewer | Aspect to Check | Status |
| :--- | :--- | :--- |
| Data Governance Manager | Alignment with overall data governance policies and structures, including AI governance. | `[ ] Pending` |
| Data Architect | Technical feasibility and alignment with enterprise architecture, including Data Mesh/Fabric. | `[ ] Pending` |
| Data Stewards | Practicality and usability of the framework for their domains and stewardship responsibilities. | `[ ] Pending` |
| Business Stakeholders | Relevance of the framework to their business needs, priorities, and data product goals. | `[ ] Pending` |
| AI Governance Officer | Compliance with ethical AI data quality standards and regulatory requirements. | `[ ] Pending` |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Strategy | The framework operationalizes the goals and objectives defined in the strategy. | `templates/templates-KA-11-data-quality.md` |
| Data Governance Framework | The DQ Framework is a key component of the overall governance framework. | `templates/templates-KA-01-data-governance.md` |
| AI Governance Framework | Provides policies and guidelines that influence data quality requirements for AI. | `templates/templates-KA-13-big-data-data-science.md` |

### 6.2. Consumers

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Dimensions | This output provides the detailed definitions and rules for each dimension defined in the framework. | `templates/templates-KA-11-data-quality.md` |
| Data Quality Metrics | This output defines the specific KPIs and metrics used to measure the dimensions in the framework. | `templates/templates-KA-11-data-quality.md` |
| Data Quality SLA | The framework provides the context for defining data quality service level agreements. | `templates/templates-KA-11-data-quality.md` |
| Data Product Outputs | Data products rely on the framework to ensure quality and trustworthiness. | `references/reference-materials.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Profiling** | Informatica Analyst, Talend Data Explorer, IBM InfoSphere Information Analyzer | Pandas Profiling, Great Expectations, Deequ |
| **Data Cleansing** | Trillium, Melissa Data, Informatica Data Quality | OpenRefine, dbt, Apache Griffin |
| **DQ Monitoring** | Collibra DQ, Monte Carlo, Ataccama | Soda Core, Deequ, WhyLabs |
| **Issue Management** | Jira, ServiceNow | Redmine, Bugzilla |
| **Data Contract Management** | Monte Carlo, Datafold | OpenLineage, Apache Atlas |
| **AI Data Quality & Monitoring** | Fiddler, WhyLabs, Arize AI | TensorFlow Data Validation, MLflow |

### 7.2. Automation Opportunities

- **Automated Data Profiling**: Schedule profiling jobs to run automatically on a regular basis to detect data drift and anomalies, integrated with data observability platforms.
- **CI/CD for DQ Rules**: Integrate data quality tests into your CI/CD pipelines to catch issues before they reach production, enabling DataOps best practices.
- **Automated Issue Creation**: Automatically create tickets in Jira or ServiceNow when a data quality rule fails, enabling rapid response and remediation.
- **Self-Healing Data Pipelines**: Implement automated remediation workflows for common data quality issues using orchestration tools like Apache Airflow or Prefect.
- **Data Contract Enforcement**: Automate validation of data contracts at ingestion points to ensure producers meet agreed quality standards.
- **AI Model Input Monitoring**: Automate monitoring of input data quality for ML models to detect drift, bias, and anomalies in real time.

---

## 8. References

- **DAMA-DMBOK2**: Chapter 13, "Data Quality".  
- **DAMA-DMBOK 3.0 (forthcoming)**: Expected to include expanded coverage on AI governance, data mesh, and data product quality (launch June 2025).  
- **Internal**: `role-definitions.md`, `data-governance-charter.md`  
- **EU AI Act**: Regulatory framework impacting data quality requirements for AI systems.  
- **DataOps and MLOps Best Practices**: Industry standards for integrating data quality into operational pipelines.


---

# Data Quality Dimensions


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Dimension Definition Document](#31-dimension-definition-document)
  - [3.2. Detailed Definition](#32-detailed-definition)
  - [3.3. Business Impact](#33-business-impact)
  - [3.4. Measurement Formula](#34-measurement-formula)
  - [3.5. Standard Metrics](#35-standard-metrics)
  - [3.6. Implementation Guidance](#36-implementation-guidance)
- [4. Example](#4-example)
  - [4.1. Dimension Definition Document (Example)](#41-dimension-definition-document-example)
  - [4.2. Detailed Definition (Example)](#42-detailed-definition-example)
  - [4.3. Business Impact (Example)](#43-business-impact-example)
  - [4.4. Measurement Formula (Example)](#44-measurement-formula-example)
  - [4.5. Standard Metrics (Example)](#45-standard-metrics-example)
  - [4.6. Implementation Guidance (Example)](#46-implementation-guidance-example)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

**Data Quality Dimensions** are a standardized set of characteristics or attributes used to measure and evaluate the fitness of data for a specific purpose. They provide a common vocabulary for understanding, assessing, and communicating the quality of data across an organization. Rather than being a monolithic concept, data quality is a multi-faceted construct, and each dimension represents a distinct aspect of quality that can be objectively measured, managed, and improved.

> The primary purpose of defining data quality dimensions is to deconstruct the abstract concept of "good data" into tangible, measurable, and actionable components. This allows the organization to move from subjective complaints about "bad data" to a structured, empirical approach to data quality management.

In the evolving landscape of data management, these dimensions serve as foundational pillars that support advanced initiatives such as AI governance, data mesh and fabric architectures, and cloud-native data platforms. As organizations increasingly embed AI and machine learning into decision-making, ensuring data quality across these dimensions becomes critical to mitigate bias, ensure compliance (e.g., EU AI Act, GDPR), and maintain trustworthiness.

### 1.2. Scope

**Global** — The framework of Data Quality Dimensions is a global standard applicable to all data across the enterprise. While the specific metrics and thresholds may be tailored for individual data products or domains, the core set of dimensions (e.g., Accuracy, Completeness, Timeliness) and their definitions are consistent organization-wide. This ensures a shared understanding and comparable measurement of data quality.

This global applicability is essential in modern distributed data environments such as data mesh, where domain teams own their data products but must adhere to enterprise-wide quality standards. Similarly, in multi-cloud and hybrid cloud architectures, consistent data quality dimensions enable interoperability and reliable data sharing.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Data Governance program charters the data quality initiative and is responsible for approving the standard set of DQ dimensions. It also integrates data quality into broader governance policies including AI governance and compliance frameworks. |
| KA-06: Data Integration & Interoperability | Data quality dimensions are critical for defining data contracts and ensuring that data moving between systems meets quality thresholds, especially in data mesh and data fabric environments. |
| KA-09: Metadata Management | The DQ dimensions, their definitions, and associated rules are critical metadata that must be captured in the metadata repository to enable automated quality assessments and lineage tracking. |
| KA-10: Reference and Master Data | Master data is often subject to the most stringent data quality standards, and DQ dimensions are used to define and enforce these standards, supporting consistency and trust in key business entities. |
| KA-12: Artificial Intelligence and Machine Learning | Data quality dimensions underpin the reliability of AI/ML models by ensuring training and operational data meet quality standards, reducing bias and improving model performance. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Quality Manager (DQ Mgr) | Ultimately answerable for the definition, standardization, and maintenance of the enterprise-wide Data Quality Dimensions framework. Ensures alignment with evolving standards such as DAMA-DMBOK 3.0 and AI governance requirements. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Responsible for researching, defining, documenting, and proposing the standard DQ dimensions and their associated business rules, incorporating modern data management practices and compliance needs. |
| **S (Supportive)** | Data Steward (D-Steward) | Supports the DQ Analyst by providing domain-specific context and validating the applicability and relevance of the dimensions to their data assets, including emerging agentic stewardship roles. |
| **C (Consulted)** | Subject Matter Expert (SME), Data Analyst | Consulted to provide input on how data is used in practice and what quality characteristics are most critical for business operations, analytics, and AI/ML applications. |
| **I (Informed)** | Data Engineer (D-Eng), Data Architect (D-Arch) | Informed of the approved DQ dimensions to ensure they are incorporated into data pipeline design, data modeling, and architectural standards, especially within cloud-native and data mesh environments. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| 1. Overview | DQ Analyst | DQ Mgr, D-Steward | DQ Mgr |
| 2. RASCI Assignment | DQ Analyst | DG Mgr | DQ Mgr |
| 3. Template | DQ Analyst | D-Steward, SME | DQ Mgr |
| 4. Example | DQ Analyst | D-Steward | DQ Mgr |
| 5. Quality Criteria | DQ Analyst | QA Analyst | DQ Mgr |
| 6. Related Outputs | DQ Analyst | D-Arch | DQ Mgr |
| 7. Tools & Automation | DQ Analyst | D-Eng | DQ Mgr |
| 8. References | DQ Analyst | DG Mgr | DQ Mgr |

---

## 3. Template

> *The following is the standardized template for defining a specific Data Quality Dimension. This template should be used for each dimension adopted by the organization to ensure consistent and comprehensive documentation.*

### 3.1. Dimension Definition Document

| Field | Value |
| :--- | :--- |
| Dimension Name | [e.g., Accuracy] |
| Dimension ID | [e.g., DQ-DIM-001] |
| Version | [e.g., 1.0] |
| Status | [e.g., Proposed, Active, Deprecated] |
| Owner | [Data Quality Manager] |
| Review Date | [YYYY-MM-DD] |

### 3.2. Detailed Definition

> *Provide a clear, unambiguous definition of the data quality dimension. Explain what it measures and why it is important for the business. Include both a business-friendly definition and a more technical definition if necessary.*

**Business Definition**: [e.g., Accuracy is the degree to which data correctly represents the "real-world" object or event it describes.]

**Technical Definition**: [e.g., The measure of conformity of a data value to a trusted source or an authoritative standard. It is often expressed as a percentage of correct values to total values.]

Include considerations for AI governance, such as how data accuracy impacts model fairness and reliability, and how data contracts enforce accuracy requirements in data mesh environments.

### 3.3. Business Impact

> *Describe the potential business impact of poor quality in this dimension. Provide concrete examples of what could go wrong if this dimension is not managed effectively.*

[e.g., Inaccurate customer addresses lead to failed deliveries, increased shipping costs, and customer dissatisfaction. Inaccurate financial data can lead to incorrect reporting, poor investment decisions, and regulatory fines.]

Highlight risks related to AI bias, regulatory non-compliance (e.g., EU AI Act), and operational inefficiencies in cloud-native data platforms.

### 3.4. Measurement Formula

> *Provide the standard formula(s) used to measure this dimension. Be explicit about the components of the formula.*

**Formula**: `(Number of Conforming Values / Total Number of Values) * 100%`

**Components**:
- **Conforming Values**: [e.g., The count of records where the data value matches the value in the authoritative source system (e.g., USPS for addresses, Dun & Bradstreet for company names).]
- **Total Values**: [e.g., The total number of records assessed.]

Include notes on automated measurement integration with data contracts and monitoring tools in modern data platforms.

### 3.5. Standard Metrics

> *List the standard, pre-defined metrics associated with this dimension. These are the specific calculations that will be implemented in DQ tools.*

| Metric ID | Metric Name | Description | Formula |
| :--- | :--- | :--- | :--- |
| [e.g., DQ-MET-001] | [Address Accuracy] | [Measures the percentage of customer addresses that match the USPS address validation service.] | `(Count of Validated Addresses / Total Addresses) * 100%` |
| [e.g., DQ-MET-002] | [Product Price Accuracy] | [Measures the percentage of product prices that match the official price book.] | `(Count of Matching Prices / Total Products) * 100%` |

Consider including AI-specific metrics such as data label accuracy or training data consistency.

### 3.6. Implementation Guidance

> *Provide guidance for Data Stewards and Data Engineers on how to implement checks for this dimension. Include information on authoritative sources, validation rules, and potential challenges.*

**Authoritative Sources**: [e.g., For customer data, the authoritative source is the CRM. For financial data, it is the ERP.]

**Validation Rules**: [e.g., A validation rule for email address accuracy could be a regex pattern check `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` combined with a domain existence check.]

**Challenges**: [e.g., Lack of a single authoritative source can make accuracy measurement difficult. Data entry errors at the source are a common root cause.]

Include guidance on leveraging data contracts to enforce accuracy SLAs, integrating with MLOps pipelines for AI data validation, and addressing challenges in distributed data mesh environments.

---

## 4. Example

> *This section provides a realistic, filled-in example of the template for the "Completeness" dimension at a fictional company, GlobalRetail Inc.*

### 4.1. Dimension Definition Document (Example)

| Field | Value |
| :--- | :--- |
| Dimension Name | Completeness |
| Dimension ID | DQ-DIM-002 |
| Version | 1.1 |
| Status | Active |
| Owner | John Doe, Data Quality Manager |
| Review Date | 2027-02-08 |

### 4.2. Detailed Definition (Example)

**Business Definition**: Completeness is the extent to which all required data is present in our records. It ensures we have a full picture of our customers, products, and operations.

**Technical Definition**: The percentage of non-null values for a specific set of critical attributes within a dataset. It can be measured at the attribute, record, or dataset level.

In the context of AI governance, completeness ensures that training datasets are representative and sufficient to avoid model bias. In data mesh architectures, domain teams are accountable for completeness of their data products.

### 4.3. Business Impact (Example)

Incomplete customer profiles prevent effective marketing segmentation and personalization, leading to lower campaign ROI. Incomplete product information on our e-commerce site (e.g., missing images, descriptions, or specifications) results in a poor customer experience and lost sales. Incomplete order information can delay fulfillment and cause revenue recognition issues.

In AI use cases, incomplete data can cause model underperformance or unfair outcomes, increasing reputational and regulatory risks.

### 4.4. Measurement Formula (Example)

**Formula**: `(Number of Non-Null Values / Total Number of Expected Values) * 100%`

**Components**:
- **Non-Null Values**: The count of records where a specific attribute is populated with a value (i.e., not NULL, empty string, or default placeholder like 'N/A').
- **Total Expected Values**: The total number of records that should have a value for that attribute.

### 4.5. Standard Metrics (Example)

| Metric ID | Metric Name | Description | Formula |
| :--- | :--- | :--- | :--- |
| DQ-MET-005 | Customer Profile Completeness | Measures the percentage of customer records with a populated email address, phone number, and mailing address. | `(Count of Records with Email, Phone, AND Address / Total Customer Records) * 100%` |
| DQ-MET-006 | Product Attribute Completeness | Measures the percentage of products that have all required attributes (image, description, price, weight) populated. | `(Count of Fully Populated Products / Total Products) * 100%` |

### 4.6. Implementation Guidance (Example)

**Authoritative Sources**: The definition of which fields are "required" is documented in the Business Glossary (KA-01) and the Logical Data Model (KA-03). Domain teams maintain completeness requirements in their data product documentation as part of data contracts (KA-06).

**Validation Rules**: Rules should be configured in the ETL process to check for null or empty values in fields designated as mandatory. A record-level completeness score can be calculated by `(Number of populated fields / Total number of fields) * 100%`. Automated alerts should notify Data Stewards when completeness falls below thresholds.

**Challenges**: Determining whether a field is truly missing or if it is not applicable for a specific record can be challenging. This requires clear business rules to differentiate between the two. In federated data environments, harmonizing completeness definitions across domains is critical.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Deliverable | **templates/templates-KA-06-data-integration-interoperability.md** |
| Data Governance Roles | Reference | **references/reference-materials.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The document defines at least six core data quality dimensions (e.g., Accuracy, Completeness, Timeliness, Uniqueness, Consistency, Validity).
- [x] Each dimension has a clear, unambiguous business and technical definition.
- [x] The business impact of poor quality for each dimension is clearly articulated with examples.
- [x] Standard measurement formulas and at least two example metrics are provided for each dimension.
- [x] The RASCI assignment is complete and logical.
- [x] The example section is filled out with realistic, context-specific information.
- [x] Modern data management context (AI governance, data mesh, cloud-native) is incorporated where relevant.
- [x] Cross-references to related deliverables, concepts, and knowledge areas are included and updated.

### 5.2. Review Checklist

| Reviewer Role | Checklist Item | Status |
| :--- | :--- | :--- |
| Data Governance Manager | Verify that the dimensions align with the overall data governance framework and policies, including AI governance and regulatory compliance. | `[ ] Reviewed` |
| Data Steward | Confirm that the dimension definitions and metrics are relevant and practical for their specific data domains and data product responsibilities. | `[ ] Reviewed` |
| Data Architect | Ensure that the dimensions and their implementation guidance are consistent with the enterprise data architecture, including data mesh and cloud-native platforms. | `[ ] Reviewed` |
| QA Analyst | Validate that the measurement formulas are mathematically sound and the acceptance criteria are met. | `[ ] Reviewed` |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Framework | Provides the high-level structure and governance for the data quality program, which the dimensions operationalize. | `templates/templates-KA-11-data-quality.md` |
| Business Glossary | The glossary defines the business terms and critical data elements that will be assessed using the DQ dimensions. | `templates/templates-KA-01-data-governance.md` |
| Logical Data Model | The data model specifies which attributes are mandatory, providing a basis for completeness checks. | `templates/templates-KA-03-data-modeling-design.md` |
| Data Contracts | Define quality expectations and SLAs for data products, leveraging DQ dimensions as core criteria. | `templates/templates-KA-06-data-integration-interoperability.md` |

### 6.2. Consumers (Outputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Metrics | This output defines the specific, detailed metrics that are derived from the broader DQ dimensions. | `templates/templates-KA-11-data-quality.md` |
| Data Quality Rules | This output contains the executable business rules that implement the measurement of the DQ dimensions. | `templates/templates-KA-11-data-quality.md` |
| Data Quality Rules (MDM) | This output applies the DQ dimensions and rules specifically to master data domains. | `templates/templates-KA-10-reference-master-data.md` |
| Data Contracts | Data contracts specify required data quality levels for data products, using the standard DQ dimensions as the basis for SLAs. | `templates/templates-KA-06-data-integration-interoperability.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| Data Profiling & DQ Assessment | Informatica DQ, Talend Data Quality, Ataccama | Great Expectations, Deequ, Apache Griffin |
| Data Governance & Metadata | Collibra, Alation, IBM Watson Knowledge Catalog | Amundsen, DataHub, OpenMetadata |
| Data Quality Monitoring | Monte Carlo, Bigeye, Anomalo | Soda Core, custom scripts with Prometheus/Grafana |
| AI Data Quality & MLOps | DataRobot, Fiddler AI, WhyLabs | Evidently AI, MLflow, TensorFlow Data Validation |

### 7.2. Automation Opportunities

- **Automated Profiling**: Data quality assessment tools can be configured to automatically scan new datasets and calculate scores for standard dimensions like completeness, uniqueness, and validity (e.g., data type, pattern matching). Integration with data mesh platforms enables domain-level ownership and visibility.
- **In-stream Validation**: Data quality rules based on these dimensions can be embedded directly into ETL/ELT pipelines (using tools like dbt, Spark, or Talend) to validate data in motion and prevent poor quality data from propagating downstream. This is critical for real-time data fabric implementations.
- **Anomaly Detection**: Machine learning-based monitoring tools can learn the normal statistical profile of a dataset (e.g., null rates, value distributions) and automatically flag significant deviations, which often indicate a data quality issue. This supports proactive data quality management in AI and analytics pipelines.
- **Dashboarding and Alerting**: DQ scores and metrics should be automatically pushed to a centralized dashboard (e.g., in Tableau, Power BI, or the DQ tool itself). Alerts should be automatically triggered and sent to the responsible Data Stewards when a metric drops below a defined threshold. Integration with FinOps and DataOps tooling can optimize resource allocation for remediation.
- **Data Contracts Enforcement**: Automated enforcement of data quality SLAs defined in data contracts can be integrated into CI/CD pipelines for data products, ensuring compliance before data is published or consumed.

---

## 8. References

- **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge (2nd Edition)*. Technics Publications, 2017. (Chapter 13: Data Quality)
- **[2]** DAMA International. *DAMA-DMBOK 3.0 (Draft)*. Community-driven update launching June 2025. [https://dama.org/dmbok3](https://dama.org/dmbok3)
- **[3]** `references/reference-materials.md`
- **[4]** `templates/templates-KA-11-data-quality.md`
- **[5]** EU AI Act and Data Governance Compliance Guidelines (external resource)
- **[6]** `templates/templates-KA-06-data-integration-interoperability.md`
- **[7]** `templates/templates-KA-12-data-handling-ethics.md`


---

# Data Quality Metrics


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Metric Identification](#31-metric-identification)
  - [3.2. Data Quality Dimension Alignment](#32-data-quality-dimension-alignment)
  - [3.3. Calculation Logic](#33-calculation-logic)
  - [3.4. Thresholds and Targets](#34-thresholds-and-targets)
  - [3.5. Implementation and Monitoring](#35-implementation-and-monitoring)
- [4. Example](#4-example)
  - [4.1. Metric Identification](#41-metric-identification)
  - [4.2. Data Quality Dimension Alignment](#42-data-quality-dimension-alignment)
  - [4.3. Calculation Logic](#43-calculation-logic)
  - [4.4. Thresholds and Targets](#44-thresholds-and-targets)
  - [4.5. Implementation and Monitoring](#45-implementation-and-monitoring)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Input for this Output)](#61-prerequisites-input-for-this-output)
  - [6.2. Consumers (This Output is Input for)](#62-consumers-this-output-is-input-for)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

**Data Quality Metrics** are specific, quantifiable measurements used to assess the quality of data against defined data quality dimensions. They serve as the fundamental units of measurement in any data quality program, converting abstract concepts such as "accuracy," "completeness," or "timeliness" into concrete, objective, and comparable scores. These metrics provide empirical evidence to identify data quality issues, track improvements over time, and demonstrate the business value of data quality initiatives.

In the evolving landscape of data management, especially with the rise of AI governance, data mesh architectures, and cloud-native platforms, data quality metrics have become even more critical. They enable organizations to maintain trust in data products and data contracts, ensuring that data assets are fit for purpose across decentralized domains and complex pipelines.

> The purpose of Data Quality Metrics is to move beyond subjective opinions about data quality and establish a rigorous, evidence-based practice for measuring, monitoring, and managing the fitness for purpose of an organization's data assets. They answer the question: *"How good is our data?"* with objective numbers, supporting operational excellence, regulatory compliance (including GDPR, HIPAA, CCPA, and emerging AI Act requirements), and strategic decision-making.

Looking forward, DAMA-DMBOK 3.0 (expected June 2025) emphasizes the integration of data quality metrics within broader data and AI governance frameworks, highlighting the need for metrics that also reflect AI model input quality, data product health, and stewardship effectiveness in agentic data stewardship models.

### 1.2. Scope

**Global** — This document establishes a standardized template and process for defining, calculating, and interpreting data quality metrics across the entire organization. While specific metric thresholds and targets may be defined on a per-product, per-domain, or per-data product basis, the methodology for creating the metrics themselves is universal and adaptable to modern data architectures such as Data Mesh and Data Fabric.

This deliverable supports both traditional centralized data governance programs and decentralized data stewardship models, ensuring metrics are actionable and aligned with enterprise data governance and AI governance objectives. It also considers multi-cloud and hybrid environments, where consistent metric definitions enable unified data quality monitoring across diverse platforms.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Governance Metrics Report (`09-governance-metrics-report.md`) consumes DQ metrics to report on the overall health of the data landscape to leadership, including AI governance integration. |
| KA-03: Data Modeling & Design | Data models provide the context for what constitutes "valid" data (e.g., data types, constraints), which is a prerequisite for many DQ metrics. |
| KA-09: Metadata Management | Metadata provides the business context, definitions, and lineage required to understand and interpret DQ metrics correctly, especially in complex data mesh environments. |
| KA-11: Data Quality | This deliverable is a core component of the Data Quality knowledge area, supporting the definition and operationalization of metrics. |
| KA-14: Maturity Assessment | The results of DQ metrics are a key input into assessing the organization's data management maturity level, including readiness for AI governance and data product management. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Quality Manager (DQ Mgr) | Ultimately accountable for the definition, standardization, and oversight of all data quality metrics across the enterprise, ensuring alignment with data and AI governance frameworks. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Responsible for defining, documenting, and validating the logic for specific data quality metrics in collaboration with Data Stewards and Data Product Managers. |
| **S (Supportive)** | DataOps Engineer (DataOps) | Supports the implementation, automation, and integration of DQ metric calculations within data pipelines, orchestration workflows (e.g., Airflow, Prefect), and monitoring systems. |
| **C (Consulted)** | Data Steward (D-Steward), Data Owner (D-Owner), AI Ethics Officer, MLOps Engineer | Consulted to provide business context, define acceptable quality thresholds, validate metric relevance, and ensure metrics support AI governance and ethical data use. |
| **I (Informed)** | Data Governance Manager (DG Mgr), Chief AI Officer (CAIO) | Kept informed of defined metrics to ensure alignment with the overall data governance and AI governance frameworks and for inclusion in governance reporting. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Metric Definition | DQ Analyst | D-Steward, D-Owner, Data Product Manager | DQ Mgr |
| Calculation Logic | DQ Analyst | DataOps, Data Architect | DQ Mgr |
| Thresholds & Targets | D-Steward, D-Owner | DQ Analyst, AI Ethics Officer | DQ Mgr |
| Monitoring & Reporting | DQ Analyst | DataOps, MLOps Engineer | DQ Mgr |

---

## 3. Template

> *The following is the standardized template for defining a Data Quality Metric. This template should be filled out for each individual metric being created.*

### 3.1. Metric Identification

> *Provide a unique identifier and clear, descriptive name for the metric. The description should explain what the metric measures and why it is important in business terms.*

| Field | Value |
| :--- | :--- |
| **Metric ID** | `[DQ-M-XXX]` |
| **Metric Name** | `[e.g., Customer Email Format Validity]` |
| **Metric Description** | `[A concise description of what the metric measures and its business purpose.]` |
| **Data Domain** | `[e.g., Customer, Product, Finance]` |
| **Critical Data Element(s)** | `[List the specific data element(s) this metric applies to, e.g., Customer.EmailAddress]` |
| **Related Data Product(s)** | `[Optional: List of data products this metric supports, e.g., Customer 360 Data Product]` |

### 3.2. Data Quality Dimension Alignment

> *Map the metric to the primary and any secondary data quality dimensions it measures. Refer to the Data Quality Dimensions output (`03-data-quality-dimensions.md`) for a standard list of dimensions.*

| Dimension | Type | Justification |
| :--- | :--- | :--- |
| `[e.g., Validity]` | Primary | `[Explain why this is the primary dimension measured.]` |
| `[e.g., Accuracy]` | Secondary | `[Explain how this metric also relates to this secondary dimension.]` |

### 3.3. Calculation Logic

> *Provide a detailed, unambiguous definition of how the metric is calculated. This should be clear enough for a developer or DataOps engineer to implement. Include the numerator, the denominator, and the formula.*

- **Denominator**: `[Define the total population of records to be evaluated. e.g., All active customer records created or updated in the last 24 hours.]`
- **Numerator**: `[Define the subset of the denominator that represents the passing or failing condition. e.g., The number of records from the denominator where the Customer.EmailAddress field conforms to the standard email format regex.]`
- **Formula**: `[Provide the mathematical formula. e.g., (Numerator / Denominator) * 100]`
- **Exclusion Criteria**: `[Specify any records that should be explicitly excluded from the calculation. e.g., Records where the email address is NULL and the customer type is 'Prospect'.]`
- **Data Source(s)**: `[Specify the data source(s) or system(s) where the metric is calculated, e.g., Customer Master Data in Snowflake.]`
- **Calculation Frequency**: `[e.g., Real-time, Daily batch, Weekly aggregate]`

### 3.4. Thresholds and Targets

> *Define the acceptable performance levels for the metric. Thresholds indicate the boundaries between good, acceptable, and unacceptable quality. The target represents the desired future state.*

| Level | Value (%) | Description |
| :--- | :--- | :--- |
| **Target** | `[e.g., > 99.5%]` | The desired, long-term quality level aligned with business objectives and regulatory requirements. |
| **Green Threshold** | `[e.g., >= 98.0%]` | The data is considered high quality and fit for purpose. No immediate action required. |
| **Amber Threshold** | `[e.g., 95.0% - 97.9%]` | The data is of acceptable quality but requires monitoring. A remediation plan should be considered. |
| **Red Threshold** | `[e.g., < 95.0%]` | The data is of poor quality and may not be fit for purpose. Immediate investigation and remediation are required. |

### 3.5. Implementation and Monitoring

> *Describe how and where the metric will be implemented and monitored.*

- **Tool(s)**: `[Specify the tool(s) used to calculate and monitor the metric, e.g., Great Expectations, Soda, Informatica DQ, Custom Python Script]`
- **Execution Frequency**: `[e.g., Daily, Hourly, On-Demand, Real-time]`
- **Owner / Steward**: `[The role responsible for monitoring this metric, e.g., Customer Data Steward]`
- **Alerting Rules**: `[Define the conditions under which alerts should be triggered, e.g., "Trigger a high-priority alert to the Data Steward and DataOps team if the metric falls into the Red Threshold for two consecutive runs."]`
- **Integration Points**: `[Optional: Indicate integration with orchestration (e.g., Airflow), observability platforms (e.g., Monte Carlo), or governance dashboards.]`
- **Remediation Workflow**: `[Optional: Describe the process triggered by alerts, e.g., automated ticket creation, data steward notification, or self-healing actions.]`

---

## 4. Example

> *This is a realistic example of a filled-in template for a specific data quality metric at the fictional company, GlobalRetail Inc.*

### 4.1. Metric Identification

| Field | Value |
| :--- | :--- |
| **Metric ID** | `DQ-M-027` |
| **Metric Name** | `Customer Mobile Phone Number Completeness` |
| **Metric Description** | `Measures the percentage of active B2C customer records that have a value present in the MobilePhone field. This is critical for SMS marketing campaigns and two-factor authentication.` |
| **Data Domain** | `Customer` |
| **Critical Data Element(s)** | `Customer.MobilePhone` |
| **Related Data Product(s)** | `Customer 360 Data Product` |

### 4.2. Data Quality Dimension Alignment

| Dimension | Type | Justification |
| :--- | :--- | :--- |
| Completeness | Primary | The metric directly measures the presence of a value in a critical field, which is the definition of completeness. |
| Availability | Secondary | A low completeness score for mobile numbers directly impacts the availability of this data for critical business processes like marketing and security. |

### 4.3. Calculation Logic

- **Denominator**: `All records in the production Customer table where Customer.Status = 'Active' and Customer.Type = 'B2C'.`
- **Numerator**: `The number of records from the denominator where the Customer.MobilePhone field is NOT NULL and is not an empty string ('').`
- **Formula**: `(Numerator / Denominator) * 100`
- **Exclusion Criteria**: `Records where Customer.Country = 'DE' (Germany), as local regulations prevent us from making this field mandatory.`
- **Data Source(s)**: `Customer Master Data stored in Snowflake.`
- **Calculation Frequency**: `Daily, aligned with the nightly data warehouse refresh.`

### 4.4. Thresholds and Targets

| Level | Value (%) | Description |
| :--- | :--- | :--- |
| **Target** | `> 98.0%` | The desired state to maximize reach for SMS campaigns. |
| **Green Threshold** | `>= 95.0%` | Data is sufficient for most operational needs. |
| **Amber Threshold** | `90.0% - 94.9%` | Marketing campaign effectiveness is impacted. Root cause analysis is initiated. |
| **Red Threshold** | `< 90.0%` | Significant impact on security (2FA) and marketing. High-priority issue. |

### 4.5. Implementation and Monitoring

- **Tool(s)**: `Great Expectations, integrated with our dbt project and Airflow orchestration.`
- **Execution Frequency**: `Daily, as part of the nightly data warehouse refresh cycle.`
- **Owner / Steward**: `Customer Data Steward`
- **Alerting Rules**: `If the metric falls into the Red Threshold for two consecutive days, automatically create a P2 ticket in Jira and assign it to the Customer Data Steward. Notifications sent via Slack to DataOps and Marketing teams.`
- **Integration Points**: `Monitored via Monte Carlo Data Observability platform and visualized in Tableau dashboards.`
- **Remediation Workflow**: `Upon alert, Data Steward initiates root cause analysis and coordinates with DataOps for pipeline fixes or data correction.`

---

### 4.6. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics KPIs | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Quality Dimensions | Deliverable | [03-data-quality-dimensions.md](templates/templates-KA-11-data-quality.md) |
| Data Quality Rules | Deliverable | [05-data-quality-rules.md](templates/templates-KA-11-data-quality.md) |
| Governance Metrics Report | Deliverable | [09-governance-metrics-report.md](templates/templates-KA-01-data-governance.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The metric has a unique, non-ambiguous name and ID.
- [ ] The business purpose and importance of the metric are clearly described, including alignment with business objectives and regulatory requirements.
- [ ] The metric is mapped to at least one primary Data Quality Dimension, with justification.
- [ ] The calculation logic (numerator, denominator, formula) is precise, unambiguous, and implementable.
- [ ] All exclusion criteria and data sources are explicitly defined.
- [ ] Target and threshold values are defined and justified by business impact and risk tolerance.
- [ ] The implementation tool(s), execution frequency, and owner/steward are clearly specified.
- [ ] Alerting rules and remediation workflows are defined for out-of-bounds conditions.
- [ ] Integration points with orchestration, observability, and governance tools are identified where applicable.
- [ ] The metric supports modern data management practices, including data product and AI governance considerations.

### 5.2. Review Checklist

| Question | Check | Reviewer Notes |
| :--- | :--- | :--- |
| Is the metric truly measuring what it claims to measure? | ☐ Yes / ☐ No | |
| Is the calculation logic robust, unambiguous, and free of loopholes? | ☐ Yes / ☐ No | |
| Are the thresholds realistic, achievable, and aligned with business needs? | ☐ Yes / ☐ No | |
| Can this metric be practically implemented with the specified tools and data sources? | ☐ Yes / ☐ No | |
| Is the ownership of the metric clear, appropriate, and supported by the organization? | ☐ Yes / ☐ No | |
| Does the metric align with data governance, AI governance, and regulatory compliance requirements? | ☐ Yes / ☐ No | |
| Are alerting and remediation processes defined and actionable? | ☐ Yes / ☐ No | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Dimensions | Provides the standardized list of dimensions (e.g., Completeness, Validity) that this metric must align with. | `templates/templates-KA-11-data-quality.md` |
| Data Governance Framework | Provides policies and standards that influence metric definitions and thresholds. | `templates/templates-KA-01-data-governance.md` |
| Metadata Repository | Supplies definitions and lineage to support metric interpretation. | `templates/templates-KA-09-metadata-management.md` |

### 6.2. Consumers (This Output is Input for)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Rules | DQ Metrics define *what* to measure, while DQ Rules define the specific logic to implement the measurement. | `templates/templates-KA-11-data-quality.md` |
| Data Quality Scorecard | The results of this metric are a key component of the overall Data Quality Scorecard. | `templates/templates-KA-11-data-quality.md` |
| Governance Metrics Report | High-level, aggregated DQ metrics are included in the governance report for executive review. | `templates/templates-KA-01-data-governance.md` |
| AI Governance Metrics | Data quality metrics feed into AI governance dashboards to ensure data fitness for AI/ML models. | `#` (future) |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Quality Platforms** | Informatica DQ, Talend Data Quality, Ataccama, Collibra DQ | Great Expectations, Soda Core, Deequ |
| **Data Observability** | Monte Carlo, Bigeye, Acceldata | Elementary, OpenLineage |
| **Orchestration** | Airflow, Prefect, Dagster | Airflow, Prefect, Dagster |
| **Visualization** | Tableau, Power BI, Looker | Superset, Metabase, Grafana |
| **MLOps Integration** | DataRobot, MLflow, Seldon | MLflow, Kubeflow Pipelines |

### 7.2. Automation Opportunities

- **Automated Calculation**: Embed data quality metric calculations fully within data processing pipelines (e.g., dbt, Spark jobs, Airflow workflows). This ensures consistent, repeatable, and timely metric generation without manual intervention.
- **Automated Alerting**: Configure alerting mechanisms (e.g., Slack, PagerDuty, email) to notify stakeholders immediately upon threshold violations, enabling proactive issue resolution.
- **Scorecard Generation**: Automate aggregation of individual metrics into comprehensive Data Quality Scorecards (`07-data-quality-scorecard.md`), providing near real-time visibility into data health at domain and enterprise levels.
- **Self-Healing**: Implement automated remediation rules for certain data quality issues detected by metrics. For example, invalid state codes detected by a metric could trigger an auto-correction rule referencing a trusted dataset.
- **AI Governance Integration**: Integrate data quality metrics with AI governance tools to monitor data fitness for AI/ML models, supporting MLOps pipelines and ethical AI practices.
- **Data Contracts Enforcement**: Use metrics as part of data contracts to enforce SLAs between data producers and consumers in data mesh environments.

---

## 8. References

- **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 13: Data Quality)
- **[2]** DAMA International. *DAMA-DMBOK 3.0 (Draft)*. Expected June 2025. (Emerging guidance on data and AI governance integration)
- **[3]** `references/reference-materials.md` (Internal reference for role descriptions)
- **[4]** `03-data-quality-dimensions.md` (Internal reference for DQ dimensions)
- **[5]** European Commission. *EU AI Act* (2021). Regulatory framework for trustworthy AI including data quality requirements.
- **[6]** IBM. *Data Mesh and Data Fabric Synergy*. Whitepaper, 2023.
- **[7]** Gartner. *Data Observability and DataOps Trends*, 2024.
- **[8]** `templates/templates-KA-11-data-quality.md` (Related deliverable for implementing rules based on metrics)
- **[9]** `templates/templates-KA-01-data-governance.md` (Governance reporting using DQ metrics)


---

# Data Quality Rules


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Header](#31-document-header)
  - [3.2. Data Quality Rule Inventory](#32-data-quality-rule-inventory)
  - [3.3. Data Quality Rule Specification (Repeat for each rule)](#33-data-quality-rule-specification-repeat-for-each-rule)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Data Quality Rule Inventory](#42-data-quality-rule-inventory)
  - [4.3. Data Quality Rule Specification (Example)](#43-data-quality-rule-specification-example)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

**Data Quality Rules** are the specific, executable logic statements that evaluate data against predefined quality standards and dimensions. They serve as the atomic building blocks of a comprehensive data quality program, translating abstract quality dimensions—such as completeness, accuracy, timeliness, consistency, and validity—into concrete, measurable, and verifiable assertions. These rules are applied across data assets to identify, quantify, and report data quality issues, enabling proactive management and remediation.

> The purpose of Data Quality Rules is to operationalize the data quality framework by providing a clear, consistent, and automated mechanism for assessing whether data conforms to both business requirements and technical standards. This operationalization supports data governance, compliance, and trustworthiness, which are foundational for effective data-driven decision-making.

In the evolving landscape of data management, Data Quality Rules also play a critical role in AI governance frameworks, ensuring that data feeding AI/ML models meets stringent quality criteria to prevent bias, inaccuracies, or compliance violations. They are increasingly integrated into modern data architectures such as Data Mesh and Data Fabric, where decentralized ownership and dynamic data products require adaptable and context-aware quality enforcement.

### 1.2. Scope

**Per Product and Data Product Lifecycle** — Data Quality Rules are typically defined for specific data products or critical data elements (CDEs) within those products. While some generic rules (e.g., primary key uniqueness or null checks) can be standardized and reused across domains, the most impactful rules are context-sensitive, designed to reflect the unique business logic, data usage patterns, and regulatory requirements of each product.

With the rise of data products as first-class citizens in data ecosystems, Data Quality Rules are embedded within data contracts and SLAs, forming part of the formal agreements between data producers and consumers. Furthermore, these rules evolve alongside the data product lifecycle, requiring periodic review and adjustment to accommodate changes in source systems, business processes, or compliance mandates such as GDPR, HIPAA, CCPA, and the emerging EU AI Act.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | Business rules and policies defined under Data Governance provide the authoritative source for Data Quality Rules. Governance programs oversee the enforcement, exception management, and continuous improvement of these rules. |
| KA-03: Data Modeling and Design | Data models define structural and semantic constraints (e.g., data types, referential integrity) that Data Quality Rules enforce to ensure data consistency and correctness. |
| KA-06: Data Integration and Interoperability | Data Quality Rules validate data as it flows between systems, ensuring that integration processes maintain or improve data quality and support interoperability standards. |
| KA-09: Metadata Management | Metadata repositories, including data dictionaries and business glossaries, supply the definitions, formats, valid values, and lineage information necessary to define precise and meaningful Data Quality Rules. |
| KA-12: Data Architecture | Modern architectures such as Data Mesh and Data Fabric influence how Data Quality Rules are designed, deployed, and managed across decentralized domains and hybrid cloud environments. |
| KA-14: Data Security and Privacy | Data Quality Rules must align with security and privacy requirements, ensuring that sensitive data is validated without violating compliance mandates or exposing protected information. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Owner (D-Owner) | Ultimately accountable for the quality of the data within their domain, including approving and endorsing the Data Quality Rules applied to their data products. Ensures alignment with business objectives and compliance requirements. |
| **R (Responsible)** | Data Steward (D-Steward) | Responsible for defining, documenting, maintaining, and periodically reviewing Data Quality Rules in collaboration with business, technical teams, and subject matter experts. Ensures rules are actionable and reflect current business needs. |
| **S (Supportive)** | Data Quality Analyst (DQ Analyst) | Supports the Data Steward by profiling data, analyzing rule outcomes, refining rule logic, and assisting with technical implementation and testing. Provides insights to improve rule effectiveness. |
| **C (Consulted)** | Subject Matter Expert (SME) | Provides business context, validation criteria, acceptable thresholds, and domain expertise to ensure rules are relevant and meaningful. Consulted during rule definition and review cycles. |
| **I (Informed)** | Data Engineer (D-Eng) | Informed of Data Quality Rules to implement, automate, and monitor them within data pipelines, workflows, and operational environments. Ensures technical feasibility and integration with data platforms. |
| **S (Supportive)** | AI Ethics Officer / MLOps Engineer | (Emerging roles) Support the integration of Data Quality Rules within AI/ML pipelines to ensure data fairness, bias mitigation, and model reliability. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Rule Definition | Data Steward | SME, DQ Analyst | Data Owner |
| Rule Implementation | Data Engineer | DQ Analyst | Data Steward |
| Rule Execution & Monitoring | Data Quality Analyst | Data Steward | Data Owner |
| Exception Management | Data Steward | SME | Data Owner |
| AI Governance Alignment | AI Ethics Officer | Data Steward, SME | CAIO (Chief AI Officer) |

---

## 3. Template

> *The following is the standardized template for defining a set of Data Quality Rules for a data product. Replace all placeholders `[...]` with specific information.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Data Product Name | [e.g., Customer Master Data Product] |
| Data Product Owner | [Name of the accountable Data Owner] |
| Document ID | DQ-RULE-[ProductCode]-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Review Date | [YYYY-MM-DD] |
| AI Governance Compliance | [Yes/No; specify if rule supports AI governance or EU AI Act compliance] |

### 3.2. Data Quality Rule Inventory

> *This section provides a summary of all data quality rules defined for this data product. Each rule should have a unique identifier.*

| Rule ID | Rule Name | Data Quality Dimension | Criticality | Status | Owner | AI Governance Impact |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., CUST-ACC-001] | [e.g., Valid Email Format] | [e.g., Accuracy] | [e.g., High] | [e.g., Active] | [e.g., D-Steward] | [e.g., Supports bias mitigation] |
| [...] | [...] | [...] | [...] | [...] | [...] | [...] |
| [...] | [...] | [...] | [...] | [...] | [...] | [...] |

### 3.3. Data Quality Rule Specification (Repeat for each rule)

> *This section provides the detailed specification for a single data quality rule. Create one such section for each rule listed in the inventory above.*

#### 3.3.1. Rule: [Rule ID] - [Rule Name]

> *Provide a clear and concise description of the rule and the business purpose it serves.*

**Description**: [e.g., This rule verifies that the email address for a customer record conforms to the standard email format (e.g., user@domain.com).]

**Business Rationale**: [e.g., An accurate email address is critical for customer communication, marketing campaigns, and account recovery. Invalid email formats lead to bounced emails and a poor customer experience. This rule also supports AI governance by ensuring input data quality for customer segmentation models.]

**Compliance Considerations**: [e.g., Ensures compliance with GDPR requirements for accurate and up-to-date contact information.]

#### 3.3.2. Rule Logic

> *Define the specific logic of the rule in a way that can be implemented by a technical team. This can be expressed as pseudocode, a SQL query, or a regular expression.*

**Input needed**: `KA-09 06-data-dictionary`, `KA-01 07-business-rules`

**Who fills this**: Data Steward, with support from DQ Analyst.

**Logic**: [e.g., `WHERE email_address NOT LIKE '%_@__%.__%'` or `WHERE NOT REGEXP_LIKE(email_address, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')`]

**Notes**: Include any assumptions, dependencies, or exceptions (e.g., internationalized email addresses).

#### 3.3.3. Rule Parameters

> *List any parameters or thresholds used in the rule logic.*

| Parameter | Description | Value |
| :--- | :--- | :--- |
| [e.g., Regular Expression] | [The regex pattern used for validation] | [e.g., `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`] |
| [e.g., Acceptance Threshold] | [The minimum percentage of passing records] | [e.g., 99.5%] |
| [e.g., Execution Frequency] | [How often the rule is run] | [e.g., Daily, Real-time] |

#### 3.3.4. Action on Failure

> *Specify the automated or manual actions to be taken when a record fails this data quality rule.*

**Input needed**: `KA-01 10-issue-resolution-log`

**Who fills this**: Data Steward, in consultation with the Data Owner.

| Action | Description | Owner |
| :--- | :--- | :--- |
| [e.g., Log] | [Log the failing record ID and the rule violation to the Data Quality Issue Log] | [e.g., Automated Process] |
| [e.g., Quarantine] | [Move the failing record to a quarantine area for manual review] | [e.g., Automated Process] |
| [e.g., Alert] | [Send an alert to the responsible Data Steward] | [e.g., Automated Process] |
| [e.g., Remediate] | [Attempt to automatically correct the data (e.g., by standardizing format)] | [e.g., Data Steward] |
| [e.g., Escalate] | [Escalate persistent or critical failures to Data Owner or AI Ethics Officer] | [e.g., Data Steward] |

**Additional Guidance**: Consider integrating failure actions with automated ticketing systems (e.g., Jira, ServiceNow) and monitoring dashboards for real-time visibility.

---

### 3.4. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-11_data-quality-rules.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

## 4. Example

> *This is a realistic, filled-in example for a fictional company, GlobalRetail Inc., for their "Product Catalog" data product.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Data Product Name | Product Catalog |
| Data Product Owner | Jane Doe |
| Document ID | DQ-RULE-PRODCAT-001 |
| Version | 1.2 |
| Effective Date | 2025-10-01 |
| Review Date | 2026-10-01 |
| AI Governance Compliance | Yes (Supports model input validation) |

### 4.2. Data Quality Rule Inventory

| Rule ID | Rule Name | Data Quality Dimension | Criticality | Status | Owner | AI Governance Impact |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PROD-COMP-001 | Mandatory Product Name | Completeness | High | Active | John Smith | Ensures completeness for product recommendation models |
| PROD-ACC-001 | Valid SKU Format | Accuracy | High | Active | John Smith | Prevents identifier errors in AI inventory forecasting |
| PROD-CONS-001 | Consistent Pricing | Consistency | Medium | Active | Sarah Chen | Supports pricing fairness algorithms |
| PROD-TIME-001 | Launch Date in Future | Timeliness | High | Active | John Smith | Ensures timely product availability data |

### 4.3. Data Quality Rule Specification (Example)

#### 4.3.1. Rule: PROD-ACC-001 - Valid SKU Format

**Description**: This rule ensures that the Stock Keeping Unit (SKU) for each product follows the official GlobalRetail Inc. format, which is two uppercase letters followed by six digits (e.g., GR123456).

**Business Rationale**: The SKU is the primary identifier for products across all inventory, sales, and logistics systems. An invalid SKU breaks the supply chain, leading to lost sales and inaccurate inventory counts. This rule also supports AI models that rely on SKU-level data for demand forecasting.

**Compliance Considerations**: Ensures data integrity for audit and regulatory reporting.

#### 4.3.2. Rule Logic

**Logic**: `WHERE NOT REGEXP_LIKE(sku, '^[A-Z]{2}[0-9]{6}$')`

#### 4.3.3. Rule Parameters

| Parameter | Description | Value |
| :--- | :--- | :--- |
| Regular Expression | The regex pattern for a valid SKU | `^[A-Z]{2}[0-9]{6}$` |
| Acceptance Threshold | The minimum percentage of valid SKUs | 99.9% |
| Execution Frequency | Frequency of rule execution | Daily |

#### 4.3.4. Action on Failure

| Action | Description | Owner |
| :--- | :--- | :--- |
| Log | Log the Product ID and invalid SKU to the "Product Data Quality Issues" table. | Automated Process |
| Alert | Send a high-priority email alert to the "Catalog Management" distribution list. | Automated Process |
| Quarantine | Flag the product as "Incomplete" in the Product Information Management (PIM) system, preventing it from going live on the e-commerce site. | Automated Process |
| Escalate | Notify Data Owner and AI Ethics Officer if failure rate exceeds threshold for 3 consecutive days. | Data Steward |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Quality Dimensions | Knowledge Area | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |
| Data Quality Metrics | Knowledge Area | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |
| Business Rules | Knowledge Area | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| Data Product Outputs | Reference | [reference/data-product-outputs.md](references/reference-materials.md) |
| AI Governance Framework | Guide | **guides/ai-governance/ai-governance-framework.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] Each rule has a unique, meaningful ID.
- [x] Each rule is mapped to a specific data quality dimension.
- [x] The business rationale for each rule is clearly articulated, including compliance and AI governance considerations where applicable.
- [x] The rule logic is unambiguous, implementable, and includes parameters and thresholds.
- [x] Acceptance thresholds are defined and realistic, reflecting business tolerance for data quality issues.
- [x] Actions for rule failure are clearly specified, assigned, and include escalation paths.
- [x] The set of rules provides adequate coverage for the critical data elements of the product, balancing completeness and feasibility.
- [x] Rules are reviewed and updated regularly to reflect changes in business context, technology, and regulatory environment.
- [x] Integration with AI governance and modern data architectures is considered and documented where relevant.

### 5.2. Review Checklist

| Area | Question | Reviewer |
| :--- | :--- | :--- |
| **Clarity** | Is the rule description and logic easy to understand for both business and technical stakeholders? | Data Steward, SME |
| **Correctness** | Does the rule logic accurately reflect the business requirement and compliance needs? | SME, DQ Analyst |
| **Necessity** | Is this rule necessary to ensure the fitness for purpose of the data and AI governance? | Data Owner, AI Ethics Officer |
| **Feasibility** | Can this rule be implemented efficiently with the available tools and technology? | Data Engineer |
| **Impact** | Has the potential impact of rule failures (and the resulting actions) been assessed, including AI model risk? | Data Owner, Data Steward, CAIO |
| **Compliance** | Does the rule align with relevant regulatory and ethical standards (e.g., GDPR, EU AI Act)? | Compliance Officer, AI Ethics Officer |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | File Path | Purpose |
| :--- | :--- | :--- |
| Data Quality Dimensions | `templates/templates-KA-11-data-quality.md` | Provides the standard dimensions (e.g., Accuracy, Completeness) that rules are based on. |
| Data Quality Metrics | `templates/templates-KA-11-data-quality.md` | Defines the metrics used to measure the output of the rules (e.g., % Pass/Fail). |
| Business Glossary | `templates/templates-KA-01-data-governance.md` | Provides the definitions for business terms used in the rules. |
| Business Rules | `templates/templates-KA-01-data-governance.md` | Contains the high-level business logic that is translated into specific data quality rules. |
| Data Contracts | `templates/templates-KA-06-data-integration-interoperability.md` | Defines SLAs and expectations that include data quality rule pass rates. |
| AI Governance Policies | `templates/strategy-assessment-governance.md` | Provides policies and standards for data quality in AI/ML contexts. |

### 6.2. Consumers (Outputs)

| Output | File Path | Purpose |
| :--- | :--- | :--- |
| Data Profiling Results | `templates/templates-KA-11-data-quality.md` | The execution of data quality rules generates profiling results that are analyzed to understand the state of data quality. |
| Data Quality Issue Log | `templates/templates-KA-11-data-quality.md` | Records and tracks data quality rule violations and remediation actions. |
| Data Contracts | `templates/templates-KA-06-data-integration-interoperability.md` | Data quality rules and their expected pass rates are often included as part of the Service Level Agreement (SLA) in a data contract. |
| AI Model Input Validation Reports | `templates/strategy-assessment-governance.md` | Reports on data quality as it pertains to AI/ML model inputs and performance. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| **Data Quality Platforms** | Informatica Data Quality, Talend Data Quality, Ataccama, Collibra Data Quality | Great Expectations, Apache Griffin, Deequ, Soda SQL |
| **Data Profiling Tools** | Tableau Prep, Power BI (Data Profiling features), Trifacta | Pandas Profiling, DataCleaner, OpenRefine |
| **SQL-based Testing** | dbt (Data Build Tool), QuerySurge | Custom SQL scripts, SQLFluff |
| **AI Governance Platforms** | IBM Watson OpenScale, Fiddler AI | Fairlearn, AI Fairness 360 |
| **Workflow Automation** | Apache Airflow, Azure Data Factory | Prefect, Luigi |

### 7.2. Automation Opportunities

- **Automated Rule Execution**: Integrate the execution of Data Quality Rules directly into ETL/ELT pipelines or streaming data flows to validate data continuously or in batch. This supports real-time data quality monitoring in cloud-native and hybrid environments.
- **Automated Issue Creation**: Automatically generate tickets in ITSM systems like Jira or ServiceNow when Data Quality Rules fail, assigning them to the appropriate Data Steward or Data Owner for remediation.
- **CI/CD for Data Quality Rules**: Store Data Quality Rule definitions as code in version control systems (e.g., Git) and implement continuous integration/continuous deployment (CI/CD) pipelines to test, validate, and deploy rule changes, enabling "quality as code" practices.
- **Automated Dashboarding and Alerts**: Feed the results of Data Quality Rule executions into BI tools (e.g., Tableau, Power BI) or observability platforms to create real-time dashboards and alerts for Data Owners, Stewards, and AI governance teams.
- **AI-Driven Anomaly Detection**: Leverage machine learning models to detect anomalies and suggest new Data Quality Rules or adjustments to existing ones based on evolving data patterns.
- **Integration with Data Contracts**: Automate the enforcement of Data Quality Rules as part of data contracts and SLAs, enabling dynamic validation and compliance reporting across data mesh domains.

---

## 8. References

- **DAMA-DMBOK 2nd Edition**: Chapter 13, "Data Quality"  
- **DAMA-DMBOK 3.0 (Upcoming)**: Emphasizes AI governance, data mesh/fabric architectures, and agentic stewardship in data quality management.  
- **Internal**: `references/reference-materials.md`  
- **Internal**: `templates/templates-KA-11-data-quality.md`  
- **Internal**: `templates/templates-KA-11-data-quality.md`  
- **Internal**: `templates/templates-KA-11-data-quality.md`  
- **Internal**: `templates/templates-KA-06-data-integration-interoperability.md`  
- **Guides**: `templates/strategy-assessment-governance.md`  
- **Reference**: `references/reference-materials.md`


---

# Data Profiling Results


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Header](#31-document-header)
  - [3.2. Executive Summary](#32-executive-summary)
  - [3.3. Single-Column Analysis](#33-single-column-analysis)
  - [3.4. Multi-Column Analysis](#34-multi-column-analysis)
  - [3.5. Summary of Findings](#35-summary-of-findings)
  - [3.6. Spreadsheet Template](#36-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Executive Summary](#42-executive-summary)
  - [4.3. Single-Column Analysis](#43-single-column-analysis)
  - [4.4. Related Concepts and Guides](#44-related-concepts-and-guides)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Profiling Results** document is the formal output of the data profiling process, a foundational activity within the Data Quality Knowledge Area (KA-11). It provides a comprehensive statistical and analytical summary of a specific data asset (e.g., a database table, a file, or a data product). The process involves systematically examining the data for its structure, content, completeness, uniqueness, and the relationships between its elements.

The purpose of this document is to deliver objective, fact-based insights into the actual state of the data, serving as a critical input for nearly all other data quality, governance, and data management activities. It enables data professionals to identify data quality issues, validate metadata, assess data fitness for purpose, and inform remediation strategies.

> Data Profiling is the art and science of reverse-engineering data specifications through observation. The Data Profiling Results document captures these observations, answering key questions such as: *What is the true format of this data? What values does it contain? How complete is it? Does it conform to our expectations?*

In modern data ecosystems, profiling results also support AI governance by ensuring that training data meets quality standards, and they underpin data mesh and data fabric initiatives by providing transparency and trust in distributed data products. As DAMA-DMBOK 3.0 evolves, data profiling is increasingly recognized as a continuous, automated activity embedded within DataOps and MLOps pipelines.

### 1.2. Scope

**Per Product or Data Asset** — A Data Profiling Results document is generated for a specific data product or a significant component thereof (e.g., a critical table within a data warehouse, a dataset in a data lakehouse, or a data product in a data mesh). While the profiling methodology is standardized globally, the results are context-specific to the data asset being analyzed, reflecting its unique characteristics, business rules, and quality expectations.

Profiling can be performed on structured, semi-structured, and unstructured data sources, and may include both batch and streaming data profiles. The scope may also extend to derived or synthetic data used in AI/ML models, where profiling helps ensure compliance with regulations such as the EU AI Act and privacy laws like GDPR, HIPAA, and CCPA.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-09: Metadata Management | Profiling results are used to validate and enrich business and technical metadata in the Data Catalog. Discrepancies between profiling findings and existing metadata are a key source of metadata quality issues and drive metadata stewardship activities. |
| KA-01: Data Governance | The findings in this document provide the evidence needed to enforce data policies, standards, and data contracts. It is a key input for the Issue Resolution Log and for agentic Data Stewardship activities emerging in modern governance frameworks. |
| KA-03: Data Modeling and Design | Profiling validates whether the physical and logical data models are implemented correctly and can reveal anomalies or deviations from the intended design, supporting model evolution and refinement. |
| KA-06: Data Integration | When profiling data sources for integration projects, the results inform the design of transformation rules, help anticipate data-related challenges, and support FinOps by optimizing data processing costs. |
| KA-12: Data Operations (DataOps) | Data profiling results feed into automated monitoring and alerting systems, enabling continuous quality assessment and integration with CI/CD pipelines for data products and AI models. |
| KA-14: Artificial Intelligence and Machine Learning | Profiling supports AI governance by assessing training data quality, detecting bias, and ensuring compliance with ethical and regulatory requirements. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Quality Manager (DQ Mgr) | Ultimately accountable for the completeness, accuracy, and timely delivery of the data profiling results. Ensures adherence to organizational standards, regulatory compliance (e.g., GDPR, EU AI Act), and alignment with enterprise data governance frameworks. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Executes data profiling tools, analyzes results, compiles the document, and ensures findings are actionable. Integrates profiling activities within DataOps and MLOps workflows where applicable. |
| **S (Supportive)** | Data Engineer (D-Eng) | Provides access to data sources, assists with profiling tool configuration, supports data extraction, and helps interpret technical aspects of data structures and pipelines. |
| **C (Consulted)** | Data Steward (D-Steward) | Provides business context, interprets profiling findings, validates business impact of issues, and collaborates on remediation plans. May include emerging roles such as AI Ethics Officer or Data Product Manager in AI-related profiling. |
| **I (Informed)** | Data Owner (D-Owner) | Kept informed of the data quality state as revealed by profiling, especially regarding significant issues affecting business operations, compliance, or AI model performance. |

### 2.2. Section-Level RASCI

| Profiling Activity | Executor (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Tool Setup & Execution | DQ Analyst | D-Eng | DQ Mgr |
| Single-Column Analysis | DQ Analyst | D-Steward | DQ Mgr |
| Multi-Column Analysis | DQ Analyst | D-Steward, Data Architect (D-Arch) | DQ Mgr |
| Summary & Recommendations | DQ Analyst | D-Steward, D-Owner | DQ Mgr |
| Final Report Sign-off | DQ Analyst | DQ Mgr | D-Owner |

---

## 3. Template

> *The following is the standardized template for a Data Profiling Results document. Replace all placeholders `[...]` with information specific to the data asset being profiled. Each section includes inline guidance in blockquotes.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Data Profiling Results for [Data Product/Asset Name] |
| Document ID | DPR-[KA_ID]-[Asset_ID]-[YYYYMMDD] |
| Version | [e.g., 1.0] |
| Profiling Date | [YYYY-MM-DD] |
| Data Source | [e.g., Database, Schema, Table, File Path, Cloud Object Storage URI] |
| Profiling Tool | [e.g., Informatica DQ, Talend Data Quality, Great Expectations, Atlan] |
| Author | [DQ Analyst Name] |
| Related Data Product Owner | [Name] |
| Data Steward(s) | [Name(s)] |
| Data Governance Program | [Name or ID] |

### 3.2. Executive Summary

> *Provide a high-level summary of the key findings and recommendations. This section is intended for management and stakeholders who may not read the entire document. Focus on business impact, compliance risks, and strategic priorities.*

- **Overall Assessment**: [e.g., The Customer dimension table is largely fit for purpose, but exhibits significant issues in the `email` and `phone_number` columns that require immediate remediation to support marketing and customer engagement initiatives.]
- **Key Strengths**: [e.g., 99.8% of records have a valid and unique `customer_key`. Address information is highly complete and conforms to expected formats.]
- **Critical Issues Found**: [e.g., Over 30% of email addresses are syntactically invalid, posing risks to communication campaigns and AI model training. The `date_of_birth` column contains future dates and non-date values, violating data policies.]
- **Top Recommendations**: [e.g., 1. Implement data cleansing rules for email and phone number fields. 2. Add validation constraints to the `date_of_birth` column to prevent invalid entries. 3. Initiate a data enrichment project to fill missing demographic data. 4. Integrate profiling into automated DataOps pipelines for continuous monitoring.]

### 3.3. Single-Column Analysis

> *This section details the analysis of individual columns (attributes). Repeat this block for each important column in the dataset. Focus on columns with high business value or suspected quality issues.*

#### 3.3.1. Column: `[Column_Name]`

- **Data Type (Inferred vs. Documented)**: [e.g., Inferred: VARCHAR(100), Documented: VARCHAR(50)]
- **Nullability**: [e.g., 1,500 Nulls (1.5%) out of 100,000 records. Expected to be 0% Null.]
- **Uniqueness**: [e.g., 98,000 unique values (98%). Expected to be 100% unique.]
- **Value Distribution (Frequency)**:
    > *Summarize the most and least common values. This helps identify default values, codes, or potential data entry errors.*
    | Value | Frequency | Percentage |
    | :--- | :--- | :--- |
    | [e.g., 'N/A'] | [e.g., 500] | [e.g., 0.5%] |
    | [e.g., 'Unknown'] | [e.g., 450] | [e.g., 0.45%] |
    | [...] | [...] | [...] |
- **Pattern & Format Analysis**:
    > *Analyze the patterns of the data using regular expressions or other pattern recognition methods. This is crucial for identifying format inconsistencies in fields like phone numbers, emails, or codes.*
    | Pattern (Regex) | Matched Count | Percentage | Example |
    | :--- | :--- | :--- | :--- |
    | [e.g., `^\d{10}$`] | [e.g., 85,000] | [e.g., 85.0%] | [e.g., '1234567890'] |
    | [e.g., `^\(\d{3}\) \d{3}-\d{4}$`] | [e.g., 10,000] | [e.g., 10.0%] | [e.g., '(123) 456-7890'] |
    | [e.g., Other/Invalid] | [e.g., 5,000] | [e.g., 5.0%] | [e.g., '123-456-7890'] |
- **Statistical Analysis** (for numeric/date columns):
    - **Min/Max**: [e.g., Min: 1920-01-15, Max: 2045-12-31]
    - **Average/Mean**: [e.g., 35.6]
    - **Standard Deviation**: [e.g., 12.3]
    - **Outliers**: [e.g., Values outside expected range detected at 0.1% frequency]
- **Findings & Anomalies**: [e.g., The column contains future dates, which should be impossible. Multiple phone number formats exist, complicating downstream processing. Default values such as 'N/A' and 'Unknown' indicate data entry issues.]

### 3.4. Multi-Column Analysis

> *This section explores relationships between columns. This can uncover more complex data quality issues that are not visible when looking at columns in isolation.*

#### 3.4.1. Dependency Analysis

> *Analyze functional dependencies between columns. For example, does the value in `city` always correspond to the value in `zip_code`?*

- **Columns Analyzed**: `[Column_A]`, `[Column_B]`
- **Expected Dependency**: [e.g., `zip_code` -> `city` (A given zip code should always map to the same city)]
- **Findings**: [e.g., Found 25 instances where the same `zip_code` maps to multiple `city` values (e.g., 90210 -> 'Beverly Hills', 90210 -> 'Los Angeles'). This indicates a data consistency issue that may affect geospatial analysis and customer segmentation.]

#### 3.4.2. Redundancy Analysis

> *Identify if multiple columns are storing the same information. For example, `product_name` and `product_description` might be highly correlated.*

- **Columns Analyzed**: `[Column_X]`, `[Column_Y]`
- **Correlation/Similarity Score**: [e.g., 0.95]
- **Findings**: [e.g., The columns `order_total` and `invoice_amount` are identical in 99.9% of records. This suggests one column is redundant and could be removed to simplify the data model and reduce storage costs.]

#### 3.4.3. Pattern Consistency Across Columns

> *Evaluate if related columns maintain consistent patterns or formats, such as date fields or categorical codes.*

- **Columns Analyzed**: `[Column_M]`, `[Column_N]`
- **Findings**: [e.g., Date fields `start_date` and `end_date` contain inconsistent formats and some `end_date` values precede `start_date`, indicating data entry errors.]

### 3.5. Summary of Findings

> *Consolidate all identified issues into a single, actionable table. Prioritize issues based on their potential business impact, compliance risk, and operational urgency.*

| ID | Issue Description | Column(s) Affected | Issue Type | Severity (H/M/L) | Recommendation |
|:---|:---|:---|:---|:---|:---|
| 1 | Future dates present in `date_of_birth` | `date_of_birth` | Validity | H | Implement a check constraint to prevent dates after today. Cleanse existing invalid records. |
| 2 | Inconsistent phone number formats | `phone_number` | Consistency | M | Standardize all phone numbers to the E.164 format using automated cleansing tools. |
| 3 | High percentage of nulls in email | `email_address` | Completeness | H | Investigate the source of nulls. Consider a data enrichment initiative and implement mandatory entry validation. |
| 4 | Zip code does not uniquely determine city | `zip_code`, `city` | Consistency | M | Use a master postal code reference to correct inconsistencies and update data governance rules. |
| 5 | Duplicate values in supposedly unique ID | `customer_id` | Uniqueness | H | Investigate data ingestion processes. Enforce uniqueness constraints and remediate duplicates. |
| 6 | Default or placeholder values detected | `status` | Accuracy | M | Identify and replace default values such as 'N/A' or 'Unknown' with valid entries or NULLs where appropriate. |
|... | [...] | [...] | [...] | [...] | [...] |

---

### 3.6. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-11_data-profiling-results.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. It supports sorting, filtering, and linking to issue logs or remediation workflows. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

> *This is a realistic, filled-in example for the "Customer" table at a fictional company, GlobalRetail Inc.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Data Profiling Results for Dim_Customer |
| Document ID | DPR-11-CUST-20260208 |
| Version | 1.0 |
| Profiling Date | 2026-02-08 |
| Data Source | EDW.dbo.Dim_Customer |
| Profiling Tool | Atlan |
| Author | Jane Doe, DQ Analyst |
| Related Data Product Owner | John Smith |
| Data Steward(s) | Alice Johnson |
| Data Governance Program | GlobalRetail Data Governance 2026 |

### 4.2. Executive Summary

- **Overall Assessment**: The Dim_Customer table is structurally sound and highly complete for core attributes like name and address. However, it exhibits critical quality issues in contact (email, phone) and demographic (`date_of_birth`) fields that will impede marketing campaigns, personalization efforts, and AI model accuracy.
- **Key Strengths**: 99.9% of records have a valid `CustomerSK`. Address fields (`AddressLine1`, `City`, `State`, `ZipCode`) have a completeness score above 98% and conform to expected formats.
- **Critical Issues Found**: 42% of `EmailAddress` values are either NULL or syntactically invalid (e.g., missing '@'). The `DateOfBirth` column contains values from the 18th century and future dates, indicating a lack of validation and potential data entry errors.
- **Top Recommendations**: 1. Immediately implement a cleansing and validation routine for the `EmailAddress` field. 2. Apply a range constraint to `DateOfBirth` (e.g., 1900-01-01 to current date). 3. Purge records with invalid birth dates that are clearly test data. 4. Integrate profiling into automated DataOps pipelines to enable continuous monitoring and alerting.

### 4.3. Single-Column Analysis

#### 4.3.1. Column: `EmailAddress`

- **Data Type (Inferred vs. Documented)**: Inferred: VARCHAR(255), Documented: VARCHAR(255)
- **Nullability**: 2,100,540 Nulls (21.0%) out of 10,000,000 records. Expected to be < 5% Null.
- **Uniqueness**: 6,850,112 unique values (68.5%).
- **Value Distribution (Frequency)**:
    | Value | Frequency | Percentage |
    | :--- | :--- | :--- |
    | NULL | 2,100,540 | 21.0% |
    | 'test@test.com' | 50,123 | 0.5% |
    | 'none@none.com' | 45,888 | 0.46% |
- **Pattern & Format Analysis**:
    | Pattern (Regex) | Matched Count | Percentage | Example |
    | :--- | :--- | :--- | :--- |
    | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | 5,800,000 | 58.0% | 'john.doe@email.com' |
    | Other/Invalid | 2,100,000 | 21.0% | 'jane.doe@com', 'no-email' |
- **Findings & Anomalies**: The high volume of nulls and invalid formats makes this column unreliable for email marketing and AI model training. The presence of default values like 'test@test.com' indicates systemic issues in source systems and data entry processes. Immediate remediation is required to improve data trustworthiness.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Quality Rules | Deliverable | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |
| Data Catalog | Deliverable | [templates/templates-KA-09-metadata-management.md](templates/templates-KA-09-metadata-management.md) |
| Issue Log | Deliverable | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] Profiling has been run on the entire dataset, not just a sample, to ensure comprehensive coverage.
- [x] Every column of business importance has been analyzed, including key identifiers, contact information, and critical attributes.
- [x] At least one multi-column analysis has been performed to detect dependencies, redundancies, or inconsistencies.
- [x] Findings have been summarized, prioritized by severity, and linked to business impact and compliance risk.
- [x] Actionable recommendations have been provided for each high-severity issue, including remediation steps and responsible parties.
- [x] The report has been reviewed and signed off by the Data Steward and Data Owner to ensure alignment with business expectations and governance policies.

### 5.2. Review Checklist

| Review Area | Question | Reviewer | Status (Pass/Fail) |
| :--- | :--- | :--- | :--- |
| Completeness | Does the report cover all critical attributes of the data asset? | DQ Mgr | Pass |
| Accuracy | Are the statistics and findings mathematically correct? | Peer DQ Analyst | Pass |
| Clarity | Is the report easy to understand for both technical and business audiences? | D-Steward | Pass |
| Actionability | Are the recommendations specific, measurable, and realistic? | D-Owner | Pass |
| Context | Has the business impact of the findings been clearly articulated? | D-Steward | Pass |
| Compliance | Are regulatory and policy implications addressed (e.g., GDPR, EU AI Act)? | Data Governance Lead | Pass |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | File Path | Purpose |
| :--- | :--- | :--- |
| Data Quality Rules | `templates/templates-KA-11-data-quality.md` | Provides the expected rules, thresholds, and validation logic against which the data is profiled. |
| Data Catalog | `templates/templates-KA-09-metadata-management.md` | Provides the documented metadata (e.g., data types, descriptions, business definitions) to compare against inferred profiling results. |
| Data Model Documentation | `templates/templates-KA-03-data-modeling-design.md` | Provides the logical and physical data model specifications to validate structure and relationships. |

### 6.2. Consumers (Outputs)

| Output Name | File Path | Purpose |
| :--- | :--- | :--- |
| Data Quality Scorecard | `templates/templates-KA-11-data-quality.md` | The metrics and findings from this report are used to calculate and update the official data quality scores and dashboards. |
| Issue Log | `templates/templates-KA-11-data-quality.md` | Each significant finding in this report should be logged as a formal issue for tracking, prioritization, and remediation. |
| Data Governance Reports | `templates/templates-KA-01-data-governance.md` | Profiling results feed into governance metrics and compliance reporting. |
| Data Product Improvement Plans | `templates/templates-KA-10-reference-master-data.md` | Findings inform continuous improvement initiatives for data products, including data contracts and SLAs. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Standalone Profiling** | Informatica Data Quality, SAP Information Steward, Ataccama, Talend Data Quality | OpenRefine, DataCleaner |
| **Library-Based** | (Part of larger platforms) | Pandas Profiling (Python), Great Expectations (Python), Deequ (Scala/Spark), Apache Griffin |
| **Cloud-Native** | AWS Glue Data Quality, Google Cloud Dataprep, Azure Purview, Databricks Lakehouse Platform | (Often integrated into cloud data platforms) |

### 7.2. Automation Opportunities

Data profiling is a highly automatable process and should be embedded within modern data management practices to enable continuous quality assurance and governance:

- **Scheduled Execution**: Profiling jobs should be scheduled to run automatically on a recurring basis (e.g., daily, weekly) to monitor data for drift, detect new issues proactively, and maintain data trustworthiness.
- **CI/CD Integration**: Integrate profiling into Continuous Integration/Continuous Deployment pipelines. New code or data changes that deploy or alter a data asset should trigger profiling jobs, with pipeline failures if quality metrics drop below defined thresholds.
- **Automated Alerting**: Configure automated alerts to be sent to Data Stewards, Data Owners, and AI Ethics Officers when profiling results deviate significantly from established baselines or violate critical data quality or governance rules.
- **Dynamic Report Generation**: Automate generation of this Markdown report using scripts or tools that pull results from profiling tool APIs and populate the template, enabling rapid dissemination and integration with issue tracking systems.
- **Integration with Data Mesh/Fabric**: Embed profiling into data product lifecycle management within data mesh and data fabric architectures to ensure decentralized data ownership with centralized quality standards.
- **AI Governance Support**: Use profiling outputs to assess training data quality, detect bias, and ensure compliance with AI governance frameworks and regulations such as the EU AI Act.
- **FinOps Optimization**: Profile data to identify redundant or low-value data that can be archived or deleted to optimize cloud storage and processing costs.

---

## 8. References

| Ref | Description |
| :-- | :--- |
| [1] | DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge*. 2nd ed., 2017. (Chapter 13: Data Quality) |
| [2] | DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Community-driven update launched June 2025, emphasizing AI governance, data mesh, and cloud-native architectures. |
| [3] | `templates/templates-KA-01-data-governance.md` (Internal reference for role definitions) |
| [4] | `templates/templates-KA-09-metadata-management.md` (Internal reference for data asset metadata) |
| [5] | `templates/templates-KA-11-data-quality.md` (Internal reference for data quality rules) |
| [6] | `templates/templates-KA-11-data-quality.md` (Internal reference for issue tracking) |
| [7] | European Commission. *EU AI Act*. Regulatory framework for trustworthy AI, including data quality requirements for training datasets. |
| [8] | GDPR, HIPAA, CCPA. Privacy and data protection regulations impacting data profiling and governance activities. |


---

# Data Quality Scorecard


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Scorecard Header](#31-scorecard-header)
  - [3.2. Executive Summary](#32-executive-summary)
  - [3.3. Data Quality Dimensions Score](#33-data-quality-dimensions-score)
  - [3.4. Trend Analysis](#34-trend-analysis)
  - [3.5. Key Issues and Findings](#35-key-issues-and-findings)
  - [3.6. Recommended Remediation Actions](#36-recommended-remediation-actions)
  - [3.7. Spreadsheet Template](#37-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Scorecard Header](#41-scorecard-header)
  - [4.2. Executive Summary](#42-executive-summary)
  - [4.3. Data Quality Dimensions Score](#43-data-quality-dimensions-score)
  - [4.4. Trend Analysis](#44-trend-analysis)
  - [4.5. Key Issues and Findings](#45-key-issues-and-findings)
  - [4.6. Recommended Remediation Actions](#46-recommended-remediation-actions)
  - [4.7. Related Concepts and Guides](#47-related-concepts-and-guides)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Input for this Output)](#61-prerequisites-input-for-this-output)
  - [6.2. Consumers (Outputs that use this Output)](#62-consumers-outputs-that-use-this-output)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Quality Scorecard** is a standardized, comprehensive report that provides a consolidated, at-a-glance view of the health and fitness-for-purpose of a specific data product or dataset. It aggregates multiple data quality metrics aligned with industry-standard dimensions, measured against predefined thresholds and targets, and presents these in an intuitive, visual format. This enables diverse stakeholders—including data owners, stewards, business users, and executives—to quickly understand the current state of data quality, identify problem areas, and track improvements over time.

In the context of modern data management paradigms such as Data Mesh and Data Fabric, the Data Quality Scorecard plays a pivotal role in enabling decentralized data ownership while maintaining enterprise-wide quality standards. It supports AI governance initiatives by ensuring that data feeding AI/ML models meets rigorous quality criteria, thereby reducing risks related to bias, errors, and compliance.

With the upcoming DAMA-DMBOK 3.0 (launched June 2025), the Data Quality Scorecard is evolving to incorporate AI governance considerations, data product lifecycle integration, and cloud-native architectures, reflecting the increasing complexity and scale of data ecosystems.

> The Data Quality Scorecard answers the critical business question: *"Is our data good enough for its intended use, where are the problems, and are we getting better?"* It serves as a foundational tool for data governance, operational excellence, and continuous improvement.

### 1.2. Scope

**Per Product** — A Data Quality Scorecard is generated for a specific data product (e.g., "Customer 360 View," "Monthly Sales Report," "AI Training Dataset"). While the template is global and standardized, the content and results are specific to the data product being assessed, ensuring relevance and actionable insights for the product's stakeholders.

The scorecard can be adapted to various data architectures, including traditional data warehouses, cloud data lakes, lakehouses, and distributed data mesh environments. It supports multi-cloud and hybrid deployments by enabling consistent quality measurement across diverse platforms.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The scorecard is a key tool for governance oversight, providing the metrics needed to enforce data policies, standards, and compliance requirements including GDPR, HIPAA, CCPA, and emerging AI regulations such as the EU AI Act. |
| KA-09: Metadata Management | The scorecard relies heavily on business and technical metadata to provide context for the metrics, such as data element definitions, lineage, and data product ownership, supporting traceability and accountability. |
| KA-06: Data Integration & Interoperability | Data quality issues identified in the scorecard often originate in upstream source systems or integration processes, highlighting areas for improvement in data pipelines and contracts. |
| KA-08: Data Warehousing & BI | Scorecards are often embedded within BI dashboards to give users context about the trustworthiness of the reports they are viewing, enabling data-driven decision-making. |
| KA-12: Data Architecture | The scorecard supports modern architectures including Data Mesh and Data Fabric by providing decentralized yet standardized quality metrics for data products across domains. |
| KA-13: Data Security & Privacy | Quality metrics can include checks related to data masking, anonymization, and compliance with privacy policies, ensuring data is both high-quality and secure. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | **Data Quality Manager (DQ Mgr)** | Ultimately accountable for the standards, generation, validation, and distribution of all Data Quality Scorecards. Ensures consistency, accuracy, and alignment with governance policies and regulatory requirements. |
| **R (Responsible)** | **Data Quality Analyst (DQ Analyst)** | Responsible for configuring, generating, analyzing, and interpreting the scorecard. Investigates anomalies, drafts the executive summary, and recommends next steps. |
| **S (Supportive)** | **DataOps Engineer (DataOps)** | Provides technical support by automating data pipelines, profiling jobs, and scorecard generation processes. Ensures data freshness and availability. |
| **C (Consulted)** | **Data Owner (D-Owner)** | Consulted to review scorecard results, provide business context for anomalies, approve remediation plans, and ensure alignment with business objectives. |
| **I (Informed)** | **Chief Data Officer (CDO)** | Kept informed of the overall data quality posture of the organization through aggregated scorecard results and trend reports, supporting strategic decision-making. |
| **S (Supportive)** | **AI Ethics Officer** | Consulted when scorecards include AI training data products to ensure ethical data quality standards and compliance with AI governance frameworks. |

### 2.2. Section-Level RASCI

| Scorecard Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Header & Summary | DQ Analyst | D-Owner | DQ Mgr |
| DQ Dimension Scores | DQ Analyst | Data Steward | DQ Mgr |
| Trend Analysis | DQ Analyst | D-Owner | DQ Mgr |
| Key Issues & Findings | DQ Analyst | Data Steward, D-Owner | DQ Mgr |
| Remediation Actions | Data Steward | D-Owner | D-Owner |

---

## 3. Template

> *The following is the standardized template for a Data Quality Scorecard. This template is populated automatically by data quality tools and reviewed by the DQ Analyst. Placeholders `[...]` indicate where specific information is inserted.*

### 3.1. Scorecard Header

> *This section provides essential metadata to identify the scorecard and its context.*

| Field | Value |
| :--- | :--- |
| Scorecard Title | Data Quality Scorecard for [Data Product Name] |
| Data Product ID | [Unique Identifier for the Data Product] |
| Reporting Period | [e.g., Q4 2025, January 2026] |
| Generation Date | [YYYY-MM-DD HH:MM UTC] |
| Overall DQ Score | [e.g., 92.5%] |
| Overall DQ Rating | [e.g., Excellent, Good, Fair, Poor] |
| Trend vs. Previous Period | [e.g., ▲ +1.2% or ▼ -0.8%] |
| Data Owner | [Name of assigned Data Owner] |
| Data Steward(s) | [Name(s) of assigned Data Steward(s)] |
| Data Product Type | [e.g., Transactional, Analytical, AI Training Dataset] |
| Data Architecture Context | [e.g., Data Mesh Domain, Lakehouse, Cloud Platform] |

### 3.2. Executive Summary

> *A brief, non-technical summary of the data quality status for an executive audience. It should highlight the overall score, key achievements, and critical issues that require attention.*

**Input needed**: Overall DQ score, key findings from the analysis, trend insights, and any compliance or governance notes.  
**Who fills this**: DQ Analyst writes the initial summary.

[Provide a 3-4 sentence summary of the data product's quality, noting any significant changes from the previous period, highlighting the most critical data quality issues affecting the business, and referencing any relevant regulatory or AI governance implications.]

### 3.3. Data Quality Dimensions Score

> *This is the core of the scorecard. It presents the aggregated scores for each of the six standard data quality dimensions. Scores are typically color-coded (e.g., Green >95%, Yellow 85-95%, Red <85%).*

**Input needed**: Aggregated metric results from `04-data-quality-metrics.md` and `06-data-profiling-results.md`.  
**Who fills this**: Automated process, validated by DQ Analyst.

| DQ Dimension | Score (%) | Threshold (%) | Status | Trend | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Completeness** | [e.g., 98.2] | 95.0 | [e.g., ✅] | [e.g., ▲] | The degree to which all required data is present and available for use. |
| **Uniqueness** | [e.g., 99.5] | 99.0 | [e.g., ✅] | [e.g., ▬] | The absence of duplicate records or data elements. |
| **Timeliness** | [e.g., 95.1] | 95.0 | [e.g., ✅] | [e.g., ▲] | The degree to which data is available when required by business processes. |
| **Validity** | [e.g., 94.3] | 95.0 | [e.g., ⚠️] | [e.g., ▼] | The degree to which data conforms to defined formats, business rules, and constraints. |
| **Accuracy** | [e.g., 88.7] | 90.0 | [e.g., ❌] | [e.g., ▼] | The degree to which data correctly represents the real-world objects or events it describes. |
| **Consistency** | [e.g., 96.0] | 95.0 | [e.g., ✅] | [e.g., ▲] | The absence of contradictions between data elements or across datasets, including cross-domain consistency. |

> **Note:** DAMA-DMBOK 3.0 is exploring expanded dimensions and AI-specific quality metrics, such as fairness and explainability, which may be incorporated in future versions of this scorecard.

### 3.4. Trend Analysis

> *A visualization showing the overall data quality score over time (e.g., the last 6-12 months). This helps identify trends, seasonal patterns, and the impact of improvement efforts.*

**Input needed**: Historical scorecard data.  
**Who fills this**: Automated process.

[Chart showing Overall DQ Score on the Y-axis and Reporting Period on the X-axis. A line graph is typically used here.]

> **Guidance:** Include annotations for major remediation initiatives, data platform changes, or regulatory events to provide context for trend shifts.

### 3.5. Key Issues and Findings

> *This section details the most significant data quality issues discovered during the reporting period. Each issue should be linked to a specific data element or business rule and its potential business impact.*

**Input needed**: Detailed output from profiling and rule execution tools, enriched with business context.  
**Who fills this**: DQ Analyst identifies and documents the issues.

| Issue ID | DQ Dimension | Data Element / Rule | Finding Description | Business Impact | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., DQ-123] | Accuracy | `Customer.Address.PostalCode` | [e.g., 15% of postal codes do not match the city and state, leading to failed mailings.] | [e.g., Increased marketing costs, delayed deliveries.] | [High] |
| [e.g., DQ-124] | Validity | `Order.TransactionDate` | [e.g., 5% of transaction dates are in the future, skewing sales forecasts.] | [e.g., Inaccurate financial reporting and planning.] | [High] |
| [e.g., DQ-125] | Completeness | `Product.Weight` | [e.g., 30% of new products are missing weight information, preventing accurate shipping cost calculation.] | [e.g., Revenue loss, poor customer experience.] | [Medium] |

> **Best Practice:** Link issues to data contracts and data product SLAs where applicable to enforce accountability and track remediation progress.

### 3.6. Recommended Remediation Actions

> *For each key issue identified, this section proposes a concrete action plan for remediation. It assigns ownership and a target date for resolution.*

**Input needed**: Analysis of root cause for the identified issues.  
**Who fills this**: Data Steward, in consultation with the DQ Analyst and Data Owner.

| Issue ID | Recommended Action | Owner | Target Date |
| :--- | :--- | :--- | :--- |
| [e.g., DQ-123] | [e.g., Implement a third-party address validation service at the point of data entry.] | [e.g., CRM Platform Owner] | [YYYY-MM-DD] |
| [e.g., DQ-124] | [e.g., Add a validation rule to the order entry system to prevent future-dated transactions.] | [e.g., ERP Development Team] | [YYYY-MM-DD] |
| [e.g., DQ-125] | [e.g., Make the `Weight` field mandatory in the product information management (PIM) system.] | [e.g., PIM Data Steward] | [YYYY-MM-DD] |

> **Additional Guidance:** Consider integrating remediation actions with DataOps and MLOps pipelines for automated issue detection and correction where feasible.

---

### 3.7. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-11_data-quality-scorecard.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

> *This is a realistic, filled-in example of a Data Quality Scorecard for a fictional company, GlobalRetail Inc.*

### 4.1. Scorecard Header

| Field | Value |
| :--- | :--- |
| Scorecard Title | Data Quality Scorecard for Customer 360 Data Product |
| Data Product ID | DP-CUST360 |
| Reporting Period | Q4 2025 |
| Generation Date | 2026-01-15 08:00 UTC |
| Overall DQ Score | 91.8% |
| Overall DQ Rating | Fair |
| Trend vs. Previous Period | ▼ -1.1% |
| Data Owner | John Smith, VP of Marketing |
| Data Steward(s) | Jane Doe, CRM Data Steward |
| Data Product Type | Analytical |
| Data Architecture Context | Data Mesh Domain: Customer Insights, Cloud Platform: AWS Lakehouse |

### 4.2. Executive Summary

The overall data quality for the Customer 360 Data Product is rated as **Fair** at 91.8%, a slight decrease from the previous quarter. While Completeness and Uniqueness remain strong, a significant drop in Accuracy, driven by incorrect email address formats, poses a risk to upcoming digital marketing campaigns. Additionally, minor validity issues with phone number formats could impact customer outreach efforts. Priority action is required to remediate the email validation process and enhance data entry controls. These findings also have implications for AI models relying on this data, underscoring the need for improved governance and monitoring.

### 4.3. Data Quality Dimensions Score

| DQ Dimension | Score (%) | Threshold (%) | Status | Trend | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Completeness** | 99.1 | 95.0 | ✅ | ▲ | The degree to which all required data is present and available. |
| **Uniqueness** | 99.8 | 99.0 | ✅ | ▬ | The absence of duplicate records. |
| **Timeliness** | 96.5 | 95.0 | ✅ | ▲ | The degree to which data is available when required. |
| **Validity** | 93.2 | 95.0 | ⚠️ | ▼ | The degree to which data conforms to defined formats and constraints. |
| **Accuracy** | 84.5 | 90.0 | ❌ | ▼ | The degree to which data correctly represents the real-world object or event. |
| **Consistency** | 95.9 | 95.0 | ✅ | ▬ | The absence of contradictions between data elements or across datasets. |

### 4.4. Trend Analysis

*(A line chart would be displayed here showing the overall score declining from 92.9% in Q3 2025 to 91.8% in Q4 2025, with scores from the previous 4 quarters for context.)*

### 4.5. Key Issues and Findings

| Issue ID | DQ Dimension | Data Element / Rule | Finding Description | Business Impact | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DQ-241 | Accuracy | `Customer.Email` | 22% of email addresses do not follow a valid format (e.g., missing '@', invalid domain). Root cause is a faulty web form regex. | High bounce rate for email campaigns, inability to contact customers, wasted marketing spend. | High |
| DQ-242 | Validity | `Customer.PhoneNumber` | 8% of phone numbers do not have the correct number of digits for their country code. | Failed SMS notifications, poor customer service experience when agents cannot dial out. | High |
| DQ-243 | Completeness | `Customer.LoyaltyTier` | 5% of loyalty program members have a null `LoyaltyTier` field, excluding them from targeted promotions. | Lost sales opportunities, customer dissatisfaction. | Medium |

### 4.6. Recommended Remediation Actions

| Issue ID | Recommended Action | Owner | Target Date |
| :--- | :--- | :--- | :--- |
| DQ-241 | Fix the regex pattern on the public-facing web registration form and run a one-time script to cleanse existing invalid emails. | Web Development Team | 2026-02-15 |
| DQ-242 | Procure and implement a phone number validation library in the CRM system for real-time checks. | CRM Platform Owner | 2026-03-31 |
| DQ-243 | Run a batch job to recalculate and populate the `LoyaltyTier` for all affected members based on their purchase history. | BI & Analytics Team | 2026-02-28 |

---

### 4.7. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics KPIs | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Quality Metrics | Deliverable | [04-data-quality-metrics.md](templates/templates-KA-11-data-quality.md) |
| Data Profiling Results | Deliverable | [06-data-profiling-results.md](templates/templates-KA-11-data-quality.md) |
| Data Governance Roles & Responsibilities | Deliverable | [05-roles-responsibilities.md](templates/templates-KA-01-data-governance.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The scorecard is generated for a single, clearly identified data product.
- [x] The overall DQ score is calculated based on a weighted average of the dimension scores, reflecting business priorities.
- [x] All six standard DQ dimensions are included and scored.
- [x] The status for each dimension is correctly marked (✅, ⚠️, ❌) based on the defined thresholds.
- [x] The trend indicator for each dimension is correctly marked (▲, ▼, ▬).
- [x] At least one key issue is documented if any dimension score is below the threshold.
- [x] A remediation action is proposed for every "High" priority issue.
- [x] The scorecard has been reviewed and signed off by the Data Owner.
- [x] The scorecard includes context on data product type and architecture.
- [x] The executive summary addresses AI governance or regulatory compliance considerations where relevant.

### 5.2. Review Checklist

| Review Question | Reviewer | Status (Pass/Fail) |
| :--- | :--- | :--- |
| Are the data product and reporting period clearly stated? | DQ Analyst | Pass |
| Does the executive summary accurately reflect the detailed results and business context? | D-Owner | Pass |
| Are the dimension scores mathematically correct based on the underlying metrics? | DQ Analyst | Pass |
| Is the business impact of each key issue clear, realistic, and linked to remediation? | D-Owner | Pass |
| Are the recommended remediation actions feasible, assigned, and time-bound? | Data Steward | Pass |
| Is the trend analysis chart easy to understand, accurate, and annotated? | DQ Analyst | Pass |
| Are AI governance and compliance considerations included where applicable? | AI Ethics Officer / DQ Analyst | Pass |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Related Output | Relationship | File Path |
| :--- | :--- | :--- |
| Data Quality Metrics | Provides the specific, measurable metrics that are aggregated into the scorecard dimensions. | `templates/templates-KA-11-data-quality.md` |
| Data Profiling Results | Delivers the raw data and statistics about the data product that are used to calculate the quality metrics. | `templates/templates-KA-11-data-quality.md` |
| Business Glossary | Provides the definitions for data elements mentioned in the scorecard, ensuring clear understanding. | `templates/templates-KA-01-data-governance.md` |
| Data Contracts | Defines data quality expectations and SLAs used as thresholds in the scorecard. | `templates/templates-KA-06-data-integration-interoperability.md` |

### 6.2. Consumers (Outputs that use this Output)

| Related Output | Relationship | File Path |
| :--- | :--- | :--- |
| Data Quality Report | The scorecard is a key component of the more detailed Data Quality Report, often included as a summary section. | `templates/templates-KA-11-data-quality.md` |
| Governance Metrics Report | Aggregated scores from multiple scorecards are rolled up into the overall Governance Metrics Report to show the health of the data landscape. | `templates/templates-KA-01-data-governance.md` |
| Data Product Catalog | The overall DQ score and rating are often displayed in the Data Product Catalog to help users assess the fitness of a data product. | `templates/templates-KA-09-metadata-management.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Profiling & Quality** | Informatica DQ, Talend Data Quality, Ataccama, Monte Carlo | Great Expectations, Soda Core, Deequ |
| **Data Catalog & Governance** | Collibra, Alation, data.world | Amundsen, DataHub |
| **BI & Visualization** | Tableau, Power BI, Qlik Sense | Apache Superset, Metabase |
| **Workflow Orchestration** | N/A | Apache Airflow, Prefect |
| **AI Governance & Monitoring** | IBM Watson OpenScale, Fiddler AI | WhyLabs, Evidently AI |

### 7.2. Automation Opportunities

The generation of the Data Quality Scorecard is highly automatable and can be integrated into modern data management pipelines. A typical workflow involves:

- Using an orchestrator like Apache Airflow or Prefect to trigger data quality tools (e.g., Great Expectations, Soda Core) to run profiling jobs and validation rules against a data product.
- Collecting, aggregating, and storing results in a centralized reporting database or data lake.
- Connecting a BI tool (e.g., Power BI, Tableau) to this database to populate the scorecard template dynamically.
- Automatically distributing the completed scorecard to stakeholders via email or publishing it to a data governance portal or data product catalog.
- Integrating with MLOps pipelines to monitor AI training data quality continuously.
- Leveraging data contracts and SLAs to trigger alerts and remediation workflows when thresholds are breached.

This automation reduces manual effort, increases timeliness, and enhances the reliability of data quality reporting, supporting continuous improvement and compliance.

---

## 8. References

- [1] DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge, Second Edition," Chapter 13 (Data Quality).
- [2] DAMA International, "DAMA-DMBOK 3.0," Community-driven update launched June 2025.
- [3] `templates/templates-KA-01-data-governance.md`
- [4] `templates/templates-KA-11-data-quality.md`
- [5] `templates/templates-KA-11-data-quality.md`
- [6] `templates/templates-KA-06-data-integration-interoperability.md`
- [8] EU AI Act and GDPR compliance guidelines (external references)

---

# End of Data Quality Scorecard Template


---

# Data Quality Report


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Report Header](#31-report-header)
  - [3.2. Executive Summary](#32-executive-summary)
  - [3.3. Data Quality Scorecard](#33-data-quality-scorecard)
  - [3.4. Detailed Issue Analysis](#34-detailed-issue-analysis)
  - [3.5. Trend Analysis](#35-trend-analysis)
  - [3.6. Remediation Plan](#36-remediation-plan)
- [4. Example](#4-example)
  - [4.1. Report Header](#41-report-header)
  - [4.2. Executive Summary](#42-executive-summary)
  - [4.3. Data Quality Scorecard](#43-data-quality-scorecard)
  - [4.4. Detailed Issue Analysis](#44-detailed-issue-analysis)
  - [4.5. Trend Analysis](#45-trend-analysis)
  - [4.6. Remediation Plan](#46-remediation-plan)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites](#61-prerequisites)
  - [6.2. Consumers](#62-consumers)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Quality Report** is a formal, structured document that presents the results of comprehensive data quality assessments for a specific data product or dataset. It synthesizes quantitative metrics and qualitative insights across multiple data quality dimensions, providing a holistic view of data health. The report highlights trends, uncovers root causes of data issues, and proposes actionable remediation strategies. It serves as a critical communication vehicle for data stewards, data owners, data governance bodies, and other stakeholders to monitor, manage, and improve the quality of their data assets.

> The purpose of the Data Quality Report is to translate raw data quality measurements into actionable intelligence, enabling data-driven decision-making that enhances data reliability, supports compliance, and builds organizational trust in data as a strategic asset.

In the evolving landscape of data management, this report increasingly incorporates considerations for AI governance, cloud-native architectures, and modern data paradigms such as Data Mesh and Data Fabric. It also aligns with emerging regulatory requirements including the EU AI Act alongside GDPR, HIPAA, and CCPA, ensuring that data quality supports both operational excellence and compliance mandates.

### 1.2. Scope

**Per Product** — This report is generated for a specific data product or dataset, reflecting the quality of data within its defined domain. It provides targeted insights relevant to the product’s business use cases, consumers, and operational context. The scope includes:

- Assessment of all relevant data quality dimensions (e.g., completeness, accuracy, timeliness, validity, uniqueness, consistency).
- Identification and analysis of critical data quality issues impacting business outcomes.
- Trend analysis over defined reporting periods to monitor progress or degradation.
- Recommendations for remediation aligned with data governance and stewardship frameworks.

This focused scope supports agile, product-centric data quality management, consistent with modern data architectures such as Data Mesh, where data products are treated as first-class citizens.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | Provides key data quality metrics that feed into governance reporting and supports governance decision-making. |
| KA-03: Data Modeling and Design | Identifies data quality issues that may stem from data model design flaws requiring remediation. |
| KA-06: Data Integration and Interoperability | Highlights data quality challenges arising during data ingestion, transformation, and integration processes. |
| KA-11: Data Quality | Core knowledge area underpinning the methodologies and metrics used in this report. |
| KA-14: Data Management Maturity Assessment | Supplies critical inputs for evaluating organizational data quality maturity and capability levels. |

Cross-reference to related deliverables such as the [Data Quality Scorecard](templates/templates-KA-11-data-quality.md) and [Governance Metrics Report](templates/templates-KA-01-data-governance.md) is essential for integrated data management.

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Quality Manager (DQ Mgr) | Ultimately accountable for the accuracy, completeness, timeliness, and distribution of the Data Quality Report. Ensures alignment with organizational data governance and AI governance policies. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Responsible for collecting data quality metrics, performing detailed analysis, drafting the report, and updating the Data Quality Scorecard. |
| **S (Supportive)** | Data Steward (D-Steward) | Provides domain expertise, business context, assists in root cause investigations, and supports remediation planning and implementation. May also facilitate agentic stewardship activities. |
| **C (Consulted)** | Data Owner (D-Owner) | Consulted to validate findings, provide business impact insights, and approve remediation plans. Engages in AI governance considerations where applicable. |
| **I (Informed)** | Data Governance Council (DGC) | Kept informed of data quality status and trends across the enterprise to support strategic oversight and compliance monitoring. |

### 2.2. Section-Level RASCI

| Report Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Executive Summary | DQ Analyst | D-Owner, D-Steward | DQ Mgr |
| Data Quality Scorecard | DQ Analyst | D-Steward | DQ Mgr |
| Detailed Issue Analysis | DQ Analyst, D-Steward | D-Owner | DQ Mgr |
| Trend Analysis | DQ Analyst | D-Steward | DQ Mgr |
| Remediation Plan | D-Steward, DQ Analyst | D-Owner | D-Owner |

**Practical Guidance:**  
- The Data Quality Manager ensures the report aligns with enterprise data governance and AI governance frameworks, reflecting the organization’s maturity and compliance posture.  
- Data Quality Analysts should leverage automated profiling and monitoring tools integrated with DataOps and MLOps pipelines where available.  
- Data Stewards play a vital role in contextualizing issues, especially in complex environments such as multi-cloud or data mesh architectures.  
- Data Owners provide critical business validation and sign-off, ensuring remediation plans are feasible and aligned with business priorities.

---

## 3. Template

> *The following is the standardized template for creating a Data Quality Report. Replace all placeholders `[...]` with product-specific information.*

### 3.1. Report Header

| Field | Value |
| :--- | :--- |
| Report Title | Data Quality Report: [Data Product Name] |
| Report ID | DQR-[YYYYMMDD]-[ProductID] |
| Reporting Period | [e.g., Q1 2026] |
| Version | [e.g., 1.0] |
| Owner | [Data Owner Name] |
| Author | [Data Quality Analyst Name] |
| Data Product Type | [e.g., Customer Data, Financial Data, IoT Sensor Data] |
| Data Architecture Context | [e.g., Data Mesh Domain, Lakehouse, Multi-cloud Environment] |

### 3.2. Executive Summary

> *Provide a high-level overview of the report's key findings. This section should be understandable to a non-technical audience and highlight the overall data quality score, critical issues, and the business impact.*

- **Overall Data Quality Score**: [e.g., 85%]  
- **Key Findings**: [e.g., 3 critical data quality issues identified in the Customer Address dimension, impacting delivery accuracy.]  
- **Business Impact**: [e.g., Potential for 5% of marketing mailings to be undeliverable, costing an estimated $50,000 in lost revenue and customer dissatisfaction.]  
- **Summary of Recommendations**: [e.g., Implement address validation service at point of entry, enhance data stewardship protocols, and integrate real-time monitoring.]  
- **Regulatory and Compliance Considerations**: [e.g., Data quality issues may affect GDPR compliance related to customer contact data.]  
- **AI Governance Implications**: [e.g., Poor data quality in training datasets could degrade AI model performance and fairness.]

### 3.3. Data Quality Scorecard

> *Present the detailed data quality scores for the data product, broken down by data quality dimension. Use the official Data Quality Scorecard as the primary input.*

**Input needed**: `07-data-quality-scorecard.md` for the specific product.  
**Who fills this**: DQ Analyst.

| Data Quality Dimension | Metric | Score (%) | Trend vs. Last Period | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Completeness | [e.g., Percentage of complete records] | [e.g., 90%] | [e.g., +2%] | [e.g., Improvement due to new data ingestion validation.] |
| Accuracy | [e.g., Percentage of records matching a trusted source] | [e.g., 80%] | [e.g., -1%] | [e.g., Decline linked to recent source system changes.] |
| Timeliness | [e.g., Percentage of records loaded within SLA] | [e.g., 95%] | [e.g., Stable] | [e.g., Consistent with SLA targets.] |
| Validity | [e.g., Percentage of records conforming to defined formats] | [e.g., 88%] | [e.g., +3%] | [e.g., Format validation rules enhanced.] |
| Uniqueness | [e.g., Percentage of unique records] | [e.g., 98%] | [e.g., Stable] | [e.g., Duplicate detection processes effective.] |
| Consistency | [e.g., Percentage of records consistent across systems] | [e.g., 82%] | [e.g., -2%] | [e.g., Integration issues identified.] |

### 3.4. Detailed Issue Analysis

> *For each data quality issue identified with a score below the target threshold, provide a detailed analysis. Include the issue description, the specific data elements affected, and the identified root cause.*

**Input needed**: Output from data profiling tools, feedback from Data Stewards.  
**Who fills this**: DQ Analyst with support from D-Steward.

**Issue ID**: [e.g., DQ-2026-001]  
- **Description**: [e.g., Customer email addresses are not valid.]  
- **Affected Data Elements**: [e.g., `Customer.EmailAddress`]  
- **Root Cause Analysis**: [e.g., No validation on the web form used for customer registration, compounded by lack of real-time feedback.]  
- **Business Impact**: [e.g., Inability to communicate with customers via email, leading to lost sales opportunities and reduced campaign effectiveness.]  
- **Regulatory Impact**: [e.g., Potential non-compliance with communication consent under GDPR.]  
- **AI Governance Impact**: [e.g., Poor email data quality affects customer segmentation models and personalization accuracy.]  
- **Remediation Status**: [e.g., Planned, In Progress, Completed]  

### 3.5. Trend Analysis

> *Visualize and discuss the trends in data quality scores over time. This helps to demonstrate the effectiveness of remediation efforts and identify recurring problems.*

**Input needed**: Historical Data Quality Reports.  
**Who fills this**: DQ Analyst.

[Insert Chart: Data Quality Score Trend Over Last 4 Quarters]

> *Discuss the trends observed in the chart. For example,*  
> "The overall data quality score has improved by 5% over the last year, primarily due to the successful implementation of the new address validation service. However, we observe a concerning downward trend in accuracy for the Product dimension, likely due to recent source system changes and integration challenges."  
>
> "Timeliness has remained stable despite increased data volume, reflecting effective scaling of data pipelines in our cloud-native environment."  
>
> "Recurring issues in uniqueness suggest the need for enhanced data contracts and product-level ownership as advocated in Data Mesh principles."

### 3.6. Remediation Plan

> *Outline the recommended actions to address the identified data quality issues. For each action, specify the owner, the timeline, and the expected outcome.*

**Input needed**: Root cause analysis, input from Data Owner and Stewards.  
**Who fills this**: D-Steward and DQ Analyst.

| Issue ID | Recommended Action | Owner | Target Date | Expected Outcome | Dependencies | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., DQ-2026-001] | Implement real-time email validation API on the customer registration form. | Web Development Team | 2026-06-30 | Increase email address validity to 99%. | Integration with CRM system | Planned |
| [e.g., DQ-2026-002] | Conduct data cleansing project on existing customer email records using validation service. | Data Stewardship Team | 2026-08-15 | Correct at least 90% of invalid email addresses. | Availability of cleansing tools | In Progress |

---

## 4. Example

### 4.1. Report Header

| Field | Value |
| :--- | :--- |
| Report Title | Data Quality Report: GlobalRetail Inc. Customer Data Product |
| Report ID | DQR-20260331-CUST01 |
| Reporting Period | Q1 2026 |
| Version | 1.0 |
| Owner | John Smith, VP Marketing |
| Author | Jane Doe, Data Quality Analyst |
| Data Product Type | Customer Master Data |
| Data Architecture Context | Data Mesh Domain - Customer Experience |

### 4.2. Executive Summary

- **Overall Data Quality Score**: 82%  
- **Key Findings**: Significant data quality issues were found in the customer address and phone number data. Over 15% of customer records have inaccurate or incomplete address information.  
- **Business Impact**: This has led to a 10% return rate on direct mail campaigns, at an estimated quarterly cost of $120,000. It also impacts the efficiency of our customer service team and risks regulatory non-compliance under GDPR.  
- **Summary of Recommendations**: We recommend a two-phased approach: immediate data cleansing of the existing customer database, followed by the implementation of an address verification service integrated into our CRM and e-commerce platforms.  
- **Regulatory and AI Governance Considerations**: Address data quality issues may affect customer consent management and AI-driven marketing personalization models.

### 4.3. Data Quality Scorecard

| Data Quality Dimension | Metric | Score (%) | Trend vs. Last Period | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Completeness | Percentage of records with a complete address | 85% | -3% | Decline linked to new e-commerce platform launch |
| Accuracy | Percentage of addresses verified against postal service data | 78% | -2% | Validation missing at point of entry |
| Timeliness | Percentage of new customer records available within 1 hour | 98% | Stable | SLA consistently met |
| Validity | Percentage of phone numbers in a valid format | 88% | +1% | Improved format validation |
| Uniqueness | Percentage of unique customer records | 99% | Stable | Duplicate detection effective |
| Consistency | Percentage of customer data consistent between CRM and Billing systems | 80% | -1% | Integration issues identified |

### 4.4. Detailed Issue Analysis

**Issue ID**: DQ-2026-003  
- **Description**: Customer street addresses are frequently incomplete or contain typos.  
- **Affected Data Elements**: `Customer.AddressLine1`, `Customer.City`, `Customer.PostalCode`  
- **Root Cause Analysis**: The online checkout form allows free-text entry for addresses with no validation. Call center staff are not consistently following address entry standards.  
- **Business Impact**: Increased shipping costs due to returned packages, customer dissatisfaction, and wasted marketing spend.  
- **Regulatory Impact**: Potential GDPR compliance risks due to inaccurate customer contact data.  
- **AI Governance Impact**: Poor address data quality undermines location-based analytics and AI-driven customer segmentation.  
- **Remediation Status**: Planned

### 4.5. Trend Analysis

[Chart showing a steady decline in Completeness and Accuracy over the past 3 quarters, while other dimensions remain relatively stable.]

The decline in address quality correlates with the launch of our new e-commerce platform in Q3 2025. The lack of address validation at the point of entry is the primary driver of this negative trend. This highlights the need for integrating data quality controls into product-level data contracts and stewardship responsibilities, consistent with Data Mesh principles.

### 4.6. Remediation Plan

| Issue ID | Recommended Action | Owner | Target Date | Expected Outcome | Dependencies | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DQ-2026-003 | 1. Procure and implement a certified address validation service for the e-commerce platform and CRM. | IT Department | 2026-07-31 | Increase address accuracy to 98%. | Vendor selection, integration with CRM | Planned |
| DQ-2026-003 | 2. Conduct a one-time data cleansing project on the existing customer database using the new validation service. | Data Stewardship Team | 2026-09-30 | Correct at least 90% of existing address errors. | Availability of cleansing tools | Planned |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics and KPIs | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Quality Scorecard | Deliverable | [07-data-quality-scorecard.md](templates/templates-KA-11-data-quality.md) |
| Data Governance Metrics Report | Deliverable | [09-governance-metrics-report.md](templates/templates-KA-01-data-governance.md) |
| Data Stewardship Guide | Guide | **guides/data-stewardship.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The report is generated for a single, clearly defined data product or dataset.  
- [x] The overall data quality score is calculated and prominently displayed.  
- [x] All relevant data quality dimensions from the scorecard are included with supporting metrics.  
- [x] At least one critical data quality issue is analyzed in detail with root cause and business impact.  
- [x] A trend analysis chart with commentary is included to show progress or degradation over time.  
- [x] A remediation plan with clear actions, owners, timelines, dependencies, and expected outcomes is provided.  
- [x] The report includes considerations for regulatory compliance (e.g., GDPR, EU AI Act) and AI governance where applicable.  
- [x] The report aligns with modern data management paradigms such as Data Mesh, Data Fabric, and cloud-native environments.  
- [x] Cross-references to related deliverables and knowledge areas are included for integrated data management.

### 5.2. Review Checklist

| Review Area | Check | Reviewer |
| :--- | :--- | :--- |
| Accuracy of Data | [ ] | Data Owner |
| Completeness of Metrics | [ ] | Data Quality Analyst |
| Clarity and Readability | [ ] | Data Quality Manager |
| Feasibility and Alignment of Remediation Plan | [ ] | Data Steward |
| Alignment with Business and Regulatory Goals | [ ] | Data Owner / Compliance Officer |
| Integration with AI Governance and DataOps Practices | [ ] | AI Ethics Officer / MLOps Engineer |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output Name | Path |
| :--- | :--- |
| Data Quality Scorecard | `templates/templates-KA-11-data-quality.md` |

### 6.2. Consumers

| Output Name | Path |
| :--- | :--- |
| Governance Metrics Report | `templates/templates-KA-01-data-governance.md` |
| Maturity Assessment Report | `templates/templates-KA-14-data-management-maturity.md` |
| AI Governance Compliance Report | `#` (forthcoming in DAMA-DMBOK 3.0) |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| Data Profiling & Data Quality Monitoring | Informatica Data Quality, Talend Data Quality, Ataccama ONE, Collibra | Great Expectations, Apache Griffin, Deequ |
| Reporting & Visualization | Tableau, Power BI, Qlik Sense, Looker | Metabase, Apache Superset, Redash |
| DataOps & MLOps Integration | DataKitchen, Domino Data Lab | MLflow, Kedro |
| Data Catalog & Data Lineage | Alation, Collibra, Informatica EDC | Amundsen, OpenLineage |

### 7.2. Automation Opportunities

- **Automated Report Generation**: Automate the generation of Data Quality Reports on a scheduled basis (e.g., monthly, quarterly) by integrating data quality monitoring tools with reporting platforms and templated outputs.  
- **Automated Distribution**: Configure automated distribution workflows to deliver reports via email or collaboration platforms (e.g., Slack, MS Teams) to relevant stakeholders including Data Owners, Stewards, and Governance Councils.  
- **Real-time Alerting**: Implement real-time alerts triggered by data quality score thresholds or anomaly detection to notify Data Stewards and Owners for immediate action.  
- **Integration with Data Contracts**: Leverage data contracts in Data Mesh environments to automate data quality validation and reporting as part of data product lifecycle management.  
- **AI Governance Integration**: Incorporate data quality metrics into AI model monitoring dashboards to ensure training data quality aligns with model performance and fairness requirements.

---

## 8. References

- DAMA-DMBOK2, Chapter 13: Data Quality  
- DAMA-DMBOK 3.0 (forthcoming, June 2025): Enhanced guidance on AI governance, data mesh, and cloud-native data quality management  
- `references/reference-materials.md`  
- `templates/templates-KA-11-data-quality.md`  
- `templates/templates-KA-01-data-governance.md`  
- `references/reference-materials.md`  
- `references/reference-materials.md`


---

# Issue Log


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Log Header](#31-log-header)
  - [3.2. Issue Log Table](#32-issue-log-table)
  - [3.3. Field Definitions](#33-field-definitions)
  - [3.4. Spreadsheet Template](#34-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Log Header](#41-log-header)
  - [4.2. Issue Log Table](#42-issue-log-table)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Issue Log** is a formal, centralized repository used to capture, track, manage, and resolve data-related issues as they are identified. It serves as the authoritative system of record for all problems, anomalies, and questions raised by data consumers, technical staff, or automated monitoring systems concerning a specific data product or data domain. Its primary purpose is to ensure that no issue is lost, that all issues are triaged and prioritized according to business impact and risk, and that there is a transparent and auditable trail from identification through to resolution and closure.

> The Issue Log is the tactical backbone of operational data quality management and increasingly, AI governance. It transforms reactive problem identification into a structured, proactive resolution process, ensuring accountability, traceability, and continuous improvement in data and AI product reliability.

In the context of modern data management, the Issue Log supports not only traditional data quality concerns but also emerging challenges such as AI model data drift, bias detection, and compliance with evolving regulations like the EU AI Act. It is a critical component in the feedback loop of data mesh and data fabric architectures, enabling decentralized teams to report and resolve issues locally while contributing to enterprise-wide transparency.

### 1.2. Scope

**Per Product or Data Domain** — An Issue Log is typically maintained for each individual data product, data domain, or AI model dataset. This focused scope ensures that the log is manageable, relevant to the specific data stewards, owners, and AI governance officers responsible for that asset, and provides a clear view of the health and challenges associated with a particular data asset or AI pipeline. While issues may be aggregated at a higher level for enterprise-wide reporting and governance, the detailed tracking and resolution activities occur at the product or domain level.

In cloud-native and multi-cloud environments, Issue Logs may be integrated with platform-native monitoring and incident management tools, enabling seamless issue capture across distributed data pipelines and AI workflows.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Issue Log is a key operational tool for the Data Governance program. The `KA-01/10-issue-resolution-log.md` provides a framework for escalating and reporting on systemic issues identified in product-specific logs. It also supports governance of AI data and model issues. |
| KA-03: Data Modeling and Design | Issues logged may reveal fundamental flaws in a data model (e.g., incorrect data types, missing relationships), triggering a review or change request to the underlying model. This is critical in evolving data mesh environments where models are federated. |
| KA-06: Data Integration and Interoperability | Many data quality and data pipeline issues originate in source systems or during integration processes. The Issue Log provides critical feedback to data integration teams for improving ETL/ELT jobs, data contracts, and source-to-target mappings. |
| KA-10: Reference and Master Data | Inconsistencies with master or reference data are a common source of issues. The log helps identify where data products are out of sync with authoritative sources, supporting master data governance and data product reliability. |
| KA-12: Data Ethics and AI Governance | Emerging AI governance frameworks require logging and managing issues related to AI data bias, fairness, and compliance. The Issue Log supports transparency and accountability in AI data stewardship. |
| KA-14: Data Operations (DataOps) | The Issue Log is integral to DataOps practices, enabling continuous monitoring, rapid triage, and remediation of data issues as part of automated data pipelines and MLOps workflows. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Owner (D-Owner) | Ultimately accountable for the resolution of all issues within their data product or domain. They have the final say on prioritization, acceptance of solutions, and ensuring alignment with business objectives and compliance requirements. |
| **R (Responsible)** | Data Steward (D-Steward) | Responsible for the day-to-day management of the Issue Log, including logging new issues, assigning owners, tracking progress, verifying resolutions, and communicating status updates. In AI contexts, may collaborate with AI Data Stewards. |
| **S (Supportive)** | Data Quality Analyst (DQ Analyst) | Supports the Data Steward by performing root cause analysis, investigating complex issues, recommending solutions, and providing data profiling insights. In AI contexts, may include AI model monitoring specialists. |
| **C (Consulted)** | Subject Matter Expert (SME), Data Custodian (D-Custod), AI Ethics Officer | Consulted for business context (SME), technical details about data storage and processing (D-Custod), or ethical considerations and regulatory compliance (AI Ethics Officer) to aid in issue investigation and resolution. |
| **I (Informed)** | Data Governance Manager (DG Mgr), Chief AI Officer (CAIO) | Kept informed of high-priority issues and overall issue trends to monitor the health of data governance and AI governance across the organization. |

### 2.2. Section-Level RASCI

| Activity / Section | Primary Actor (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Logging a New Issue | Any Stakeholder | Data Steward | N/A |
| Triage and Prioritization | Data Steward | SME, D-Owner, AI Ethics Officer | D-Owner |
| Root Cause Analysis | DQ Analyst | D-Steward, D-Custod, AI Ethics Officer | D-Steward |
| Developing Remediation Plan | D-Steward | DQ Analyst, SME, AI Ethics Officer | D-Owner |
| Implementing Fix | D-Custod / Technical Team | D-Steward | D-Steward |
| Verifying and Closing Issue | Data Steward | Original Reporter, AI Ethics Officer (if applicable) | D-Owner |

---

## 3. Template

> *The following is the standardized template for a Data Product Issue Log. This log should be implemented in a dedicated tool (like Jira, ServiceNow, or a DataOps platform) but can be exported into this format for reporting. Each new entry constitutes a new row in the table.*

### 3.1. Log Header

| Field | Value |
| :--- | :--- |
| Data Product Name | [Name of the Data Product, e.g., Customer Master] |
| Data Product ID | [Unique Identifier for the Data Product] |
| Data Owner | [Name of the Accountable Data Owner] |
| Data Steward | [Name of the Responsible Data Steward] |
| AI Governance Officer | [Name of the AI Ethics Officer or CAIO, if applicable] |
| Last Updated | [YYYY-MM-DD] |
| Data Product Type | [Data Product, Data Mesh Domain, AI Model Dataset, etc.] |
| Environment | [Production, Staging, Development] |

### 3.2. Issue Log Table

> *This table forms the core of the Issue Log. Each row represents a unique data issue. The columns provide all necessary information for tracking the issue through its lifecycle.*

| Issue ID | Date Reported | Reported By | Issue Title | Description | Data Element(s) | Priority | Status | Assigned To | Target Date | Resolution Summary | Compliance Impact | AI Impact |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[DQ-PROD-ID-NNNN]` | `[YYYY-MM-DD]` | `[Name/Team]` | `[Brief, clear title]` | `> *Detailed description of the issue, including observed vs. expected behavior, specific record examples (with masked PII), and perceived business impact.*` | `[e.g., Customer.EmailAddress]` | `[Critical, High, Medium, Low]` | `[New, Open, In Progress, Resolved, Closed, On Hold]` | `[Name/Team]` | `[YYYY-MM-DD]` | `> *Summary of the root cause and the actions taken to resolve the issue. Include links to code changes or related documentation.*` | `[e.g., GDPR, HIPAA, EU AI Act]` | `[e.g., Model bias detected, Data drift]` |
| `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` |

### 3.3. Field Definitions

> *This section provides clear definitions for each column in the log to ensure consistent data entry.*

*   **Issue ID**: A unique identifier for the issue, often generated by the tracking tool (e.g., `DQ-CUST-0101`).
*   **Date Reported**: The date the issue was formally logged.
*   **Reported By**: The name of the person, team, or system that identified the issue.
*   **Issue Title**: A concise, one-sentence summary of the problem.
*   **Description**: A detailed explanation of the issue. Should be comprehensive enough for someone unfamiliar with the problem to understand it, including business impact and technical context.
*   **Data Element(s)**: The specific data elements (columns/attributes) affected by the issue.
*   **Priority**: The urgency of the issue, based on business impact, severity, and compliance risk. Typically defined in an SLA.
*   **Status**: The current stage of the issue in its lifecycle (e.g., New, Open, In Progress, Resolved, Closed, On Hold).
*   **Assigned To**: The individual or team responsible for investigating and resolving the issue.
*   **Target Date**: The agreed-upon date for issue resolution.
*   **Resolution Summary**: A description of the final resolution, confirming the fix and outlining any preventative measures put in place. Include references to related documentation or code repositories.
*   **Compliance Impact**: Any regulatory or compliance frameworks impacted by the issue (e.g., GDPR, HIPAA, EU AI Act).
*   **AI Impact**: For AI-related data products, notes on impacts such as model bias, data drift, or fairness concerns.

---

### 3.4. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-11_issue-log.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. It supports filtering by priority, status, compliance impact, and AI impact to facilitate focused remediation efforts. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

> *This is a realistic, filled-in example of an Issue Log for a fictional company, GlobalRetail Inc. It demonstrates how the template is used in practice, including AI governance considerations.*

### 4.1. Log Header

| Field | Value |
| :--- | :--- |
| Data Product Name | `Customer Analytics Mart` |
| Data Product ID | `DP-MKT-003` |
| Data Owner | `Alice Johnson` |
| Data Steward | `Bob Williams` |
| AI Governance Officer | `Dr. Emily Chen` |
| Last Updated | `2026-02-08` |
| Data Product Type | `Data Product` |
| Environment | `Production` |

### 4.2. Issue Log Table

| Issue ID | Date Reported | Reported By | Issue Title | Description | Data Element(s) | Priority | Status | Assigned To | Target Date | Resolution Summary | Compliance Impact | AI Impact |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `DQ-MKT-0023` | `2026-01-15` | `Sales Analytics Team` | `Null values in 'LastPurchaseDate' for active customers` | `> The 'Active Customers' segment in the weekly sales report shows 15% of customers with a NULL LastPurchaseDate. This is incorrect, as an active customer must have at least one purchase. This skews our customer lifetime value calculations. Example Customer ID: 892341` | `FactSales.LastPurchaseDate` | `High` | `Closed` | `Charlie Davis (BI Eng)` | `2026-01-29` | `> Root Cause: The nightly ETL job was failing to update the date for customers whose only purchase was returned. Resolution: The transformation logic was updated to ignore returned orders when calculating the LastPurchaseDate. A backfill script was run to correct 3,104 affected records.` | `None` | `None` |
| `DQ-MKT-0024` | `2026-01-22` | `Automated DQ Scan` | `Invalid email formats in DimCustomer` | `> The nightly data profiling job detected 5,200 records in DimCustomer where the 'EmailAddress' field does not conform to the standard RFC 5322 format (e.g., contains spaces, missing '@' symbol). This impacts email marketing campaign delivery.` | `DimCustomer.EmailAddress` | `Medium` | `In Progress` | `Data Quality Analyst` | `2026-02-20` | `> Investigation ongoing. Initial analysis suggests a data entry issue from the in-store signup form. A remediation plan is being developed.` | `GDPR` | `None` |
| `DQ-MKT-0025` | `2026-02-05` | `Marketing Team` | `'Country' field is inconsistent (USA vs. United States)` | `> The 'Country' dimension in our customer reports shows two different values for the United States: 'USA' and 'United States'. This causes incorrect grouping in geographical analysis dashboards. We need to standardize on a single value.` | `DimCustomer.Country` | `Medium` | `Open` | `Bob Williams (D-Steward)` | `2026-02-12` | `> Issue triaged. Agreed to standardize on 'United States'. A change request will be submitted to the ETL team to implement a transformation rule. Will also check against the master Reference Data.` | `None` | `None` |
| `DQ-MKT-0026` | `2026-02-07` | `AI Model Monitoring` | `Potential bias detected in credit risk model input data` | `> Automated monitoring flagged a statistically significant underrepresentation of a demographic group in recent credit application data, potentially impacting model fairness and compliance with the EU AI Act.` | `CreditApplication.DemographicGroup` | `Critical` | `New` | `AI Ethics Officer` | `2026-02-14` | `> Investigation initiated. Data team and AI governance working on root cause and mitigation plan.` | `EU AI Act` | `Model bias` |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Governance Roles and Responsibilities | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| Remediation Plan | Deliverable | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |
| Issue Resolution Log | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The Issue Log must be stored in a system accessible to all relevant stakeholders, supporting role-based access control.
- [x] Every identified data or AI governance issue, regardless of source (manual or automated), must be logged promptly.
- [x] Each logged issue must have a unique, persistent ID that is traceable across related systems.
- [x] All fields in the log template must be filled in accurately and kept up-to-date, including compliance and AI impact fields where applicable.
- [x] Priority levels (Critical, High, Medium, Low) must be clearly defined, consistently applied, and aligned with organizational SLAs.
- [x] The log must show a clear owner (Assigned To) for every open issue, with escalation paths defined.
- [x] No issue can be moved to 'Closed' status without a documented resolution, verification, and sign-off by the Data Owner or AI Governance Officer.
- [x] The Issue Log must support integration with automated monitoring and alerting systems to enable near real-time issue capture.
- [x] The Issue Log must support linkage to remediation plans, change requests, and governance metrics reporting.

### 5.2. Review Checklist

| Review Area | Check | Finding/Comment |
| :--- | :--- | :--- |
| **Completeness** | Are all known issues captured in the log? | `[e.g., Cross-referenced with support tickets; 3 tickets found that were not logged]` |
| **Timeliness** | Are issues being logged and updated in a timely manner? | `[e.g., Average time to log a new issue is < 24 hours]` |
| **Clarity** | Are descriptions and resolutions clear and understandable? | `[e.g., Some resolution summaries are too technical; need simplification]` |
| **Lifecycle Management** | Is there a backlog of 'New' or stale 'In Progress' issues? | `[e.g., 15% of issues have been 'In Progress' for > 60 days; requires review]` |
| **Trend Analysis** | Does the log reveal recurring issues or problematic data elements? | `[e.g., 'EmailAddress' appears in 30% of all logged issues, indicating a systemic problem]` |
| **Compliance and AI Governance** | Are compliance and AI impact fields consistently filled and reviewed? | `[e.g., Missing AI impact assessments on recent model-related issues]` |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Profiling Results | The automated analysis of data sources is a primary input for discovering and logging new data quality issues. | `templates/templates-KA-11-data-quality.md` |
| Business Glossary | Provides the standard definitions for data elements, which are used to determine if data is being used or represented correctly. | `templates/templates-KA-01-data-governance.md` |
| AI Model Monitoring Reports | Provide alerts and insights on AI model data quality, drift, and bias, feeding into the Issue Log for AI governance. | `templates/templates-KA-12-data-handling-ethics.md` |

### 6.2. Consumers (Outputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Remediation Plan | High-priority or systemic issues identified in the log become formal inputs into a detailed Remediation Plan. | `templates/templates-KA-11-data-quality.md` |
| Issue Resolution Log | Aggregated and escalated issues from this product-specific log are fed into the enterprise-level Issue Resolution Log for governance oversight. | `templates/templates-KA-01-data-governance.md` |
| Governance Metrics Report | Metrics such as issue count, resolution time, backlog size, and AI governance KPIs are key performance indicators reported in the governance metrics dashboard. | `templates/templates-KA-01-data-governance.md` |
| Change Management Requests | Issues requiring changes to data models, pipelines, or AI models trigger formal change requests. | `templates/templates-KA-03-data-modeling-design.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| **Issue Tracking / ITSM** | **Jira Service Management**: Excellent for creating custom workflows, linking to development tickets, and building dashboards. <br> **ServiceNow IT Service Management**: Integrates well with broader ITIL processes and CMDB. | **Redmine**: A flexible project management web application with issue tracking. <br> **Bugzilla**: A mature, web-based bug tracking system. |
| **Data Quality Platforms** | **Informatica DQ, Talend DQ, Ataccama**: These tools can automatically identify anomalies and, via API, create new issues directly in the Issue Log. | **Great Expectations**: Can be configured to run data validation and trigger alerts or API calls to a logging system when expectations fail. |
| **AI Model Monitoring Tools** | **Fiddler AI, Arize AI, WhyLabs**: Provide AI model monitoring with bias detection and drift alerts, integrating with Issue Logs for AI governance. | **Evidently AI**: Open source tool for monitoring ML model performance and data drift. |

### 7.2. Automation Opportunities

*   **Automated Issue Creation**: Integrate data quality monitoring and profiling tools (like Great Expectations) and AI model monitoring platforms (like Fiddler AI) to automatically create a new issue in the log when a data validation rule fails, an anomaly is detected, or AI bias/drift is identified. This reduces manual effort and ensures immediate capture.
*   **Automated Notifications**: Configure the issue tracking tool to send automated email or Slack notifications to the assigned owner when an issue's status changes, a comment is added, or a target date is approaching.
*   **SLA Monitoring Dashboards**: Create automated dashboards that track the age of open issues and highlight any that are approaching or have breached their Service Level Agreement (SLA) for resolution.
*   **Workflow Enforcement**: Use the workflow engine in tools like Jira to enforce the issue lifecycle. For example, prevent an issue from being closed unless the 'Resolution Summary' and 'Compliance Impact' fields are filled out.
*   **Integration with Data Mesh Platforms**: Leverage APIs to synchronize Issue Logs across federated data domains, enabling enterprise-wide visibility while preserving local ownership.
*   **AI Governance Reporting**: Automate extraction of AI-related issue metrics for inclusion in AI governance reports and compliance audits.

---

## 8. References

*   **DAMA-DMBOK (2nd Edition)**: Chapter 13, "Data Quality Management". The chapter provides the foundational concepts for identifying, logging, and resolving data quality issues.
*   **DAMA-DMBOK 3.0 (forthcoming)**: Expected to expand on AI governance, data mesh/fabric architectures, and integrated operational management, including enhanced guidance on issue management.
*   **Internal Documents**:
    *   `templates/templates-KA-01-data-governance.md`: For detailed definitions of roles like Data Owner and Data Steward.
    *   `templates/templates-KA-04-data-storage-operations.md`: For the specific Service Level Agreements that define issue priorities and target resolution times.
    *   `templates/templates-KA-12-data-handling-ethics.md`: For guidance on monitoring AI models and managing AI-related issues.
    *   `templates/templates-KA-03-data-modeling-design.md`: For managing change requests triggered by issues.

---


---

# Remediation Plan


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Header](#31-document-header)
  - [3.2. Executive Summary](#32-executive-summary)
  - [3.3. Issue Identification and Prioritization](#33-issue-identification-and-prioritization)
  - [3.4. Root Cause Summary](#34-root-cause-summary)
  - [3.5. Remediation Actions and Tasks](#35-remediation-actions-and-tasks)
  - [3.6. Resource and Timeline Planning](#36-resource-and-timeline-planning)
  - [3.7. Validation and Monitoring Plan](#37-validation-and-monitoring-plan)
  - [3.8. Communication Plan](#38-communication-plan)
- [4. Example](#4-example)
  - [**Document Header**](#document-header)
  - [**Executive Summary**](#executive-summary)
  - [**Issue Identification and Prioritization**](#issue-identification-and-prioritization)
  - [**Root Cause Summary**](#root-cause-summary)
  - [**Remediation Actions and Tasks**](#remediation-actions-and-tasks)
  - [**Resource and Timeline Planning**](#resource-and-timeline-planning)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria Checklist](#51-acceptance-criteria-checklist)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Remediation Plan** is a formal, structured document that defines the approach to identify, prioritize, and resolve data quality issues within a data product or system. It translates diagnostic findings from issue logs and root cause analyses into actionable, measurable steps with assigned responsibilities, timelines, and success criteria. The plan serves as a tactical roadmap to restore and enhance data trustworthiness, fitness for use, and compliance with organizational policies and regulatory requirements.

In the evolving landscape of data management, the Remediation Plan also supports integration with emerging paradigms such as AI governance, data mesh and data fabric architectures, cloud-native platforms, and lakehouse environments. It ensures that remediation efforts align with enterprise-wide data governance strategies and operationalize controls that prevent recurrence, including those relevant to AI model data inputs and outputs. This includes embedding remediation within MLOps, DataOps, and FinOps frameworks to ensure continuous improvement and operational efficiency.

> A Remediation Plan moves beyond issue identification to active resolution. It answers the questions: *"What are we going to fix, who will fix it, how will they fix it, and by when?"* It also establishes how success will be measured and sustained, incorporating feedback loops to adapt to evolving data and AI governance requirements.

As DAMA-DMBOK 3.0 approaches release (expected mid-2025), this deliverable anticipates enhanced guidance on integrating remediation with agentic data stewardship, data contracts, and data product management, reflecting the shift towards treating data as a product and embedding governance into operational workflows.

### 1.2. Scope

**Per Product** — This deliverable is created for a specific data product, such as a customer master database, a sales data warehouse, or a product information management system. While a global remediation framework or template may exist, each Remediation Plan is tailored to the unique data quality issues, business context, and technical environment of the data product in question.

The scope includes:

- Identification and prioritization of data quality issues impacting the product, considering business impact, regulatory risk (e.g., GDPR, HIPAA, CCPA), and AI governance implications (e.g., EU AI Act compliance).
- Root cause analysis summaries to inform targeted remediation, leveraging metadata lineage and integration insights.
- Detailed remediation actions and task breakdowns, including both manual corrections and automated fixes aligned with modern architectures such as data mesh nodes, data fabrics, and lakehouse platforms.
- Resource allocation and timeline estimates, factoring in cross-functional teams and new roles like AI Ethics Officers, MLOps Engineers, and Data Product Managers.
- Validation and ongoing monitoring strategies integrated with data quality metrics, dashboards, and AI governance controls.
- Communication plans for stakeholder engagement, ensuring transparency and alignment with enterprise data governance and AI governance programs.

The plan may also incorporate considerations for compliance with emerging regulatory frameworks such as the EU AI Act alongside traditional data privacy regulations, especially when data quality issues impact AI/ML model inputs or outputs.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The remediation plan operates under the authority of the data governance program. It relies on governance roles such as Data Owners, Data Stewards, and Data Quality Managers for accountability, execution, and oversight. It also aligns with governance policies, standards, and emerging AI governance frameworks. |
| KA-09: Metadata Management | Metadata provides essential context for understanding data quality issues, including data lineage to trace root causes, business definitions to assess impact, and data catalog entries to facilitate issue identification and resolution. Metadata also supports AI model data provenance and auditability. |
| KA-06: Data Integration and Interoperability | Many remediation actions involve correcting data integration pipelines (ETL/ELT), fixing transformation logic, or improving interoperability between systems to prevent data inconsistencies. Integration with DataOps pipelines and cloud-native data platforms is increasingly important. |
| KA-04: Data Storage and Operations | Operational tasks such as running data cleansing scripts, restoring backups, modifying database schemas, or adjusting storage configurations are often part of remediation efforts. Cloud-native storage and multi-cloud considerations are increasingly relevant. |
| KA-12: Artificial Intelligence and Machine Learning | As AI governance matures, remediation plans increasingly address data quality issues that affect AI/ML model performance, fairness, and compliance, integrating with MLOps and DataOps practices. Remediation must consider AI ethics, bias mitigation, and model retraining triggers. |
| KA-07: Data Architecture | Remediation plans should consider the data architecture context, including modern paradigms like data mesh, data fabric, and lakehouse architectures, ensuring fixes align with architectural principles, tooling, and distributed ownership models. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Owner (D-Owner) | Ultimately accountable for the successful execution and outcome of the remediation plan for the data product they own. They approve the plan, allocate necessary resources, and ensure alignment with business objectives, compliance requirements, and AI governance mandates. |
| **R (Responsible)** | Data Steward (D-Steward) | Responsible for creating the remediation plan, coordinating the execution of remediation tasks, tracking progress, and reporting status. They act as the day-to-day managers of the remediation effort and serve as the liaison between technical teams, business stakeholders, and AI governance bodies. |
| **S (Supportive)** | Data Quality Analyst (DQ Analyst), Data Engineer (D-Eng), MLOps Engineer (if AI/ML involved) | DQ Analysts support by providing detailed issue analysis, validation, and reporting. Data Engineers execute technical remediation tasks such as data cleansing, pipeline fixes, and automation. MLOps Engineers may support remediation related to AI data quality, model retraining, and deployment pipelines. |
| **C (Consulted)** | Subject Matter Expert (SME), AI Ethics Officer (if applicable), Compliance Officer | SMEs provide business context, validate remediation approaches, and ensure alignment with business rules. AI Ethics Officers may be consulted for remediation impacting AI fairness, bias, or compliance with AI governance policies. Compliance Officers ensure regulatory adherence. |
| **I (Informed)** | Data Quality Manager (DQ Mgr), Chief AI Officer (CAIO), Compliance Officer | Kept informed of remediation status, risks, and outcomes. The DQ Manager oversees the broader data quality program, while the CAIO and Compliance Officer are informed when remediation impacts AI governance or regulatory compliance. |

### 2.2. Section-Level RASCI

| Plan Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Issue Identification & Prioritization | DQ Analyst | D-Steward, SME | D-Owner |
| Root Cause Summary | DQ Analyst | D-Eng, SME | D-Steward |
| Remediation Actions & Tasks | D-Steward | D-Eng, SME, AI Ethics Officer (if applicable) | D-Owner |
| Resource & Timeline Planning | D-Steward | D-Owner | D-Owner |
| Validation & Monitoring Plan | DQ Analyst | D-Steward | D-Steward |
| Communication Plan | D-Steward | DQ Manager, SME, Compliance Officer | D-Owner |

---

## 3. Template

> *The following is the standardized template for creating a Data Quality Remediation Plan. This template should be filled out for each data product requiring corrective action.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Plan Title | Data Quality Remediation Plan for [Data Product Name] |
| Plan ID | DQ-REM-[YYYYMMDD]-[ID] |
| Version | [e.g., 1.0] |
| Status | [Draft, In Review, Approved, In Progress, Completed] |
| Data Product Owner | [Name of Data Owner] |
| Data Steward | [Name of Data Steward] |
| Creation Date | [YYYY-MM-DD] |
| Last Updated | [YYYY-MM-DD] |
| Related AI Governance Plan | [If applicable, reference AI governance plan or policy] |
| Data Product Architecture | [Brief note on architecture: e.g., Data Mesh Node, Lakehouse, Multi-cloud] |

### 3.2. Executive Summary

> *Provide a high-level summary of the remediation plan. Briefly describe the key data quality issues being addressed, the overall goal of the plan, the estimated effort and duration, and the expected business benefits upon completion.*

**Input needed**: `09-issue-log.md`, Business Impact Analysis, AI Governance considerations (if applicable).  
**Who fills this**: Data Steward.

[Insert Executive Summary here]

### 3.3. Issue Identification and Prioritization

> *List the specific data quality issues to be remediated. Reference the Issue ID from the `09-issue-log.md`. Prioritize the issues based on severity, business impact, regulatory risk, AI governance risk, and feasibility of correction.*

**Input needed**: `09-issue-log.md`.  
**Who fills this**: DQ Analyst, reviewed by Data Steward.

| Issue ID | Issue Description | Data Quality Dimension | Priority (High/Med/Low) | Business Impact | Regulatory/AI Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., DQ-435] | [Customer records missing email addresses] | Completeness | [High] | [Prevents marketing campaigns, impacts customer communication] | [Medium: impacts GDPR consent management] |
| [e.g., DQ-438] | [Product prices inconsistent between CRM and ERP] | Consistency | [High] | [Causes billing errors, customer dissatisfaction, revenue loss] | [Low] |
| [e.g., DQ-441] | [Order dates are in an invalid format (MM-DD-YY)] | Validity | [Medium] | [Hinders reporting and analytics, requires manual data cleaning] | [Low] |

### 3.4. Root Cause Summary

> *For each high-priority issue, provide a brief summary of the root cause. This information is critical for ensuring the remediation addresses the source of the problem, not just the symptoms. This section may be updated after the `12-root-cause-analysis-report.md` is completed.*

**Input needed**: Initial findings from issue investigation, `12-root-cause-analysis-report.md` (when available).  
**Who fills this**: DQ Analyst.

- **Issue ID [e.g., DQ-435]**: [Root cause is a faulty API endpoint from the web registration form that does not properly validate the email field.]
- **Issue ID [e.g., DQ-438]**: [Root cause is a nightly batch job failure that prevents price updates from the ERP from synchronizing to the CRM.]
- **Issue ID [e.g., DQ-441]**: [Root cause is inconsistent date formatting rules applied in different ingestion pipelines.]

### 3.5. Remediation Actions and Tasks

> *This is the core of the plan. Detail the specific actions and tasks required to fix each issue. Break down actions into manageable tasks that can be assigned and tracked. Include both manual and automated remediation, as well as preventative controls.*

**Input needed**: Technical analysis, SME consultation, AI governance input (if applicable).  
**Who fills this**: Data Steward, with input from Data Engineer, SME, and AI Governance Officer (if applicable).

**Issue: [e.g., DQ-438: Product prices inconsistent between CRM and ERP]**

| Task ID | Task Description | Task Type (Manual/Automated) | Assigned To (Role) | Estimated Effort (Hours) | Dependencies / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REM-001 | Manually correct all current price discrepancies for top 100 products. | Manual | Data Steward | 16 | Requires access to ERP and CRM data |
| REM-002 | Analyze and fix the bug in the nightly ERP-to-CRM sync job. | Automated (Fix) | Data Engineer | 24 | Coordinate with integration team |
| REM-003 | Develop a reconciliation report to run daily and flag any future price mismatches. | Automated (Control) | DQ Analyst | 8 | Integrate with DQ monitoring tools |
| REM-004 | Backfill historical sales orders with corrected price data. | Automated (Correction) | Data Engineer | 40 | Schedule during low system usage |

### 3.6. Resource and Timeline Planning

> *Outline the resources required (personnel, tools) and provide a realistic timeline for the completion of the remediation plan. Use a simple Gantt chart or timeline table. Consider dependencies, team availability, and potential risks.*

**Input needed**: Task effort estimates, team availability, tool access.  
**Who fills this**: Data Steward.

**Required Resources**:
- **Personnel**: 1x Data Steward (Part-time), 1x Data Engineer (Full-time for 2 weeks), 1x DQ Analyst (Part-time), AI Governance Officer (Consulted, if applicable)
- **Tools**: SQL Client, Data Integration Platform (e.g., Informatica, Talend), DQ Monitoring Tool (e.g., Great Expectations), Issue Tracking System (e.g., Jira)

**Timeline**:

| Task ID | Start Date | End Date | Duration (Days) | Comments |
| :--- | :--- | :--- | :--- | :--- |
| REM-001 | 2026-03-01 | 2026-03-03 | 3 | Manual corrections prioritized by business impact |
| REM-002 | 2026-03-01 | 2026-03-08 | 6 | Includes testing and deployment |
| REM-003 | 2026-03-09 | 2026-03-10 | 2 | Integrate with existing DQ dashboards |
| REM-004 | 2026-03-11 | 2026-03-17 | 5 | Schedule to minimize operational impact |

### 3.7. Validation and Monitoring Plan

> *Describe how the success of the remediation will be validated. This includes defining acceptance criteria for each fix and the plan for ongoing monitoring to prevent recurrence. Include integration with data quality metrics and dashboards.*

**Input needed**: Data Quality Rules, `04-data-quality-metrics.md`, monitoring tools.  
**Who fills this**: DQ Analyst.

| Issue ID | Validation Method | Acceptance Criteria | Monitoring Plan | Frequency | Responsible Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., DQ-438] | Run reconciliation report. | 100% match between ERP and CRM prices for all products. | Daily reconciliation report monitored by Data Steward. Alerts trigger immediate investigation. | Daily | Data Steward |
| [e.g., DQ-435] | Query customer table for null emails. | 0 records with null email addresses for customers created after fix date. | Completeness metric added to monthly DQ dashboard. | Monthly | DQ Analyst |
| [e.g., DQ-441] | Automated data validation scripts on ingestion pipelines. | 0% invalid date formats in new data. | Continuous monitoring integrated with DataOps pipeline. | Real-time | Data Engineer |

### 3.8. Communication Plan

> *Outline how progress and completion of the remediation plan will be communicated to stakeholders. Include communication channels, frequency, and content focus. Consider AI governance and compliance stakeholders if applicable.*

**Input needed**: Stakeholder register, communication policies.  
**Who fills this**: Data Steward.

| Stakeholder | Communication Method | Frequency | Content | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| Data Owner | Weekly Email Update | Weekly | Progress against timeline, risks, and issues. | Keep accountable informed and engaged |
| DQ Manager | DQ Dashboard | Daily/Weekly | Updated DQ metrics post-remediation, risk alerts. | Oversight and program management |
| Business Users | Team Meeting | Bi-weekly | Demo of fixes, impact on business processes. | User awareness and feedback |
| AI Governance Committee | Monthly Report | Monthly | Status of remediation impacting AI data quality and compliance. | Ensure AI governance alignment |
| Compliance Officer | Ad-hoc Reports | As needed | Compliance risk assessments and remediation status. | Regulatory oversight |

---

## 4. Example

> *This is a realistic example of a filled-in Remediation Plan for a fictional company, GlobalRetail Inc. It addresses a critical data quality issue in their customer data product.*

### **Document Header**

| Field | Value |
| :--- | :--- |
| Plan Title | Data Quality Remediation Plan for Customer Master Data Product |
| Plan ID | DQ-REM-20260215-001 |
| Version | 1.0 |
| Status | Approved |
| Data Product Owner | John Smith, VP of Marketing |
| Data Steward | Emily White, Senior Marketing Analyst |
| Creation Date | 2026-02-15 |
| Last Updated | 2026-02-18 |
| Related AI Governance Plan | AI Data Quality Compliance Plan v1.2 |
| Data Product Architecture | Data Mesh Node, Cloud-Native Lakehouse |

### **Executive Summary**

This plan addresses critical completeness and validity issues within the Customer Master Data Product. Specifically, over 30% of new customer records are missing postal codes, and 15% have invalid email address formats. These issues severely impact direct mail campaigns and email marketing ROI, as well as compliance with GDPR consent management. This plan outlines a 3-week effort to correct the existing data, fix the root causes in the data entry systems, and implement preventative controls including enhanced validation rules and real-time data quality monitoring. The expected benefit is a 10% increase in marketing campaign effectiveness, improved customer engagement, and a significant reduction in operational costs associated with manual data correction.

### **Issue Identification and Prioritization**

| Issue ID | Issue Description | Data Quality Dimension | Priority (High/Med/Low) | Business Impact | Regulatory/AI Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DQ-112 | Customer records missing postal codes. | Completeness | High | Inability to target customers for regional promotions; increased shipping costs due to address verification failures. | Medium (impacts GDPR address validation) |
| DQ-113 | Invalid email address format (e.g., missing '@'). | Validity | High | High bounce rate for email campaigns; wasted marketing spend; potential blacklisting of our domain. | High (GDPR consent and communication compliance) |

### **Root Cause Summary**

- **Issue ID DQ-112**: The postal code field on the in-store tablet registration form is not set as a mandatory field, allowing sales associates to skip it.
- **Issue ID DQ-113**: The web registration form's JavaScript validation for the email field is outdated and does not catch all invalid formats. It only checks for the presence of an '@' symbol.

### **Remediation Actions and Tasks**

**Issue: DQ-112 & DQ-113**

| Task ID | Task Description | Task Type (Manual/Automated) | Assigned To (Role) | Estimated Effort (Hours) | Dependencies / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REM-CUST-01 | Use a third-party service (e.g., Melissa Data) to look up and backfill missing postal codes for existing customers. | Automated | Data Engineer | 30 | Requires API access and data extraction |
| REM-CUST-02 | Update the in-store tablet registration app to make the postal code field mandatory. | Automated (Fix) | IT App Dev Team | 40 | Coordinate with retail IT |
| REM-CUST-03 | Replace the web form's email validation with a robust regex pattern and an API-based real-time validation service. | Automated (Fix) | Web Dev Team | 20 | Integrate with external validation API |
| REM-CUST-04 | Run a script to identify and flag all existing invalid email addresses for manual review. | Automated | DQ Analyst | 8 | Prepare data for customer service outreach |
| REM-CUST-05 | Manually contact customers with invalid emails to obtain the correct address. | Manual | Customer Service Team | 60 | Requires CRM access and outreach scripts |

### **Resource and Timeline Planning**

**Required Resources**:
- **Personnel**: 1x Data Steward, 1x Data Engineer, 1x DQ Analyst, IT App Dev, Web Dev, Customer Service
- **Tools**: Melissa Data API subscription, SQL Workbench, Jira for tracking, DQ Monitoring Dashboard

**Timeline**:

| Task ID | Start Date | End Date | Duration (Days) | Comments |
| :--- | :--- | :--- | :--- | :--- |
| REM-CUST-01 | 2026-02-22 | 2026-02-26 | 5 | Backfill process scheduled during off-peak hours |
| REM-CUST-02 | 2026-02-22 | 2026-03-08 | 10 | Includes testing and deployment |
| REM-CUST-03 | 2026-02-22 | 2026-02-26 | 5 | Web form update and validation testing |
| REM-CUST-04 | 2026-02-27 | 2026-02-27 | 1 | Data extraction and flagging |
| REM-CUST-05 | 2026-02-28 | 2026-03-14 | 10 | Customer outreach and data correction |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics KPIs | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Issue Log | Deliverable | [09-issue-log.md](templates/templates-KA-11-data-quality.md) |
| Root Cause Analysis Report | Deliverable | [12-root-cause-analysis-report.md](templates/templates-KA-11-data-quality.md) |
| Data Quality Metrics | Deliverable | [04-data-quality-metrics.md](templates/templates-KA-11-data-quality.md) |
| Roles and Responsibilities | Knowledge Area | [05-roles-responsibilities.md](templates/templates-KA-01-data-governance.md) |
| AI Governance Fundamentals | Concept | **ai-governance.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [x] All high-priority issues from the `09-issue-log.md` are included in the plan.
- [x] A root cause summary is provided for each issue, referencing `12-root-cause-analysis-report.md` where applicable.
- [x] Specific, actionable remediation tasks are defined, including manual and automated actions.
- [x] Each task is assigned to a specific role with clear accountability.
- [x] Realistic effort estimates and timelines are provided, considering resource availability and dependencies.
- [x] A clear validation plan with acceptance criteria is defined, linked to `04-data-quality-metrics.md`.
- [x] Ongoing monitoring plans are established to prevent recurrence, including integration with data quality dashboards and AI governance controls.
- [x] The plan includes a communication strategy tailored to stakeholders, including AI governance and compliance where relevant.
- [x] The plan has been reviewed and approved by the Data Owner and relevant SMEs.
- [x] The plan aligns with organizational data governance policies and emerging DAMA-DMBOK 3.0 guidance, including considerations for AI governance and modern data architectures.

### 5.2. Review Checklist

| Reviewer Role | Aspect to Review | Status (Approved/Rejected) | Comments |
| :--- | :--- | :--- | :--- |
| Data Owner | Business Impact and Priority | Approved | The plan correctly prioritizes issues that affect revenue and customer experience. |
| Data Engineer | Technical Feasibility | Approved | The proposed technical fixes are sound and the effort estimates are reasonable. |
| SME | Business Logic | Approved | The proposed corrections align with business rules and processes. |
| DQ Manager | Completeness and Standards | Approved | The plan adheres to the organization's data quality management standards. |
| AI Ethics Officer | AI Governance Compliance | Approved | Remediation addresses AI data quality risks and aligns with AI governance policies. |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | File Path | Description |
| :--- | :--- | :--- |
| Issue Log | `templates/templates-KA-11-data-quality.md` | Provides the list of data quality issues that this plan aims to remediate. |
| Data Quality Metrics | `templates/templates-KA-11-data-quality.md` | Defines the metrics and thresholds used to identify issues and validate their resolution. |
| Root Cause Analysis Report | `templates/templates-KA-11-data-quality.md` | Provides detailed root cause analysis to inform remediation actions. |
| Stakeholder Register | (Varies) | Lists stakeholders to be informed or consulted during remediation. |

### 6.2. Consumers (Outputs)

| Output Name | File Path | Description |
| :--- | :--- | :--- |
| Root Cause Analysis Report | `templates/templates-KA-11-data-quality.md` | This plan may trigger a more in-depth root cause analysis for complex issues. |
| Data Quality Dashboard | (Varies) | The results of the remediation (improved DQ scores) will be reflected in data quality dashboards. |
| AI Governance Reports | (Varies) | Reports on remediation status impacting AI data quality and compliance. |
| Compliance Audit Reports | (Varies) | Evidence of remediation actions for regulatory audits. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

- **Data Quality Monitoring Platforms** (e.g., Great Expectations, Talend Data Quality) for automated detection and validation of data issues.
- **Issue Tracking Systems** (e.g., Jira, ServiceNow) to manage remediation tasks and workflows.
- **Data Integration and Pipeline Tools** (e.g., Apache NiFi, Informatica, Azure Data Factory) to implement automated fixes and data corrections.
- **Metadata Management Tools** (e.g., Collibra, Alation) to provide lineage and impact analysis supporting root cause identification.
- **AI Governance Platforms** (e.g., IBM Watson OpenScale, Fiddler AI) to monitor AI model data quality and fairness.
- **Collaboration Tools** (e.g., Confluence, SharePoint) for documentation and communication.

### 7.2. Automation Opportunities

- Automated detection of recurring data quality issues via continuous monitoring integrated with DataOps pipelines.
- Auto-triggered remediation workflows for common, low-risk issues (e.g., automated data cleansing scripts).
- Integration of remediation status updates with AI governance dashboards to provide real-time visibility.
- Use of data contracts to enforce data quality expectations at ingestion points, preventing issues upstream.
- Leveraging MLOps pipelines to automate retraining and validation of AI models impacted by data quality remediation.

---

## 8. References

- DAMA-DMBOK2 Framework, DAMA International  
- DAMA-DMBOK 3.0 (forthcoming, 2025)  
- EU AI Act and GDPR Compliance Guidelines  
- AI Governance Fundamentals (**ai-governance.md**)  
- Data Mesh Principles and Practices  
- Data Fabric Architecture Patterns  
- MLOps and DataOps Integration Best Practices  
- [09-issue-log.md](templates/templates-KA-11-data-quality.md)  
- [12-root-cause-analysis-report.md](templates/templates-KA-11-data-quality.md)  
- [04-data-quality-metrics.md](templates/templates-KA-11-data-quality.md)  
- [05-roles-responsibilities.md](templates/templates-KA-01-data-governance.md)


---

# Data Quality SLA


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Header](#31-document-header)
  - [3.2. Business Context](#32-business-context)
  - [3.3. Scope of Agreement](#33-scope-of-agreement)
  - [3.4. Data Quality Dimensions and Metrics](#34-data-quality-dimensions-and-metrics)
  - [3.5. Service Level Objectives (SLOs)](#35-service-level-objectives-slos)
  - [3.6. Monitoring, Reporting, and Auditing](#36-monitoring-reporting-and-auditing)
  - [3.7. Escalation and Remediation Process](#37-escalation-and-remediation-process)
  - [3.8. Signatures](#38-signatures)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Business Context](#42-business-context)
  - [4.3. Scope of Agreement](#43-scope-of-agreement)
  - [4.4. Data Quality Dimensions and Metrics](#44-data-quality-dimensions-and-metrics)
  - [4.5. Service Level Objectives (SLOs)](#45-service-level-objectives-slos)
  - [4.6. Monitoring, Reporting, and Auditing](#46-monitoring-reporting-and-auditing)
  - [4.7. Escalation and Remediation Process](#47-escalation-and-remediation-process)
  - [4.8. Signatures](#48-signatures)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Quality Service Level Agreement (SLA)** is a formal, documented contract between a data provider and a data consumer that defines specific, measurable targets for the quality of a dataset or data service. It transforms data quality from a subjective aspiration into an objective, enforceable standard with agreed-upon metrics, thresholds, and remediation processes.

In the evolving landscape of data management, where data products are increasingly treated as first-class assets, and data contracts govern exchanges, the Data Quality SLA serves as a critical mechanism to ensure trust, reliability, and accountability. It supports operational excellence in data mesh and data fabric architectures by codifying quality expectations across decentralized domains and multi-cloud environments.

The primary purposes of a Data Quality SLA include:

- Establishing clear, shared expectations for data quality aligned with business needs.
- Providing a framework for continuous monitoring, reporting, and auditing of data quality.
- Defining escalation and remediation protocols to address quality breaches promptly.
- Enabling compliance with regulatory requirements such as GDPR, HIPAA, CCPA, and the emerging EU AI Act, especially where data quality impacts AI governance and ethical use.
- Supporting emerging roles such as Data Product Managers, AI Ethics Officers, and MLOps Engineers in operationalizing data quality within AI and analytics workflows.

> The Data Quality SLA answers the critical questions: *"How good does this data need to be for its intended use?"* and *"What happens if the data quality falls short?"*

### 1.2. Scope

This deliverable encompasses two complementary components:

- **Global SLA Template**: A standardized, enterprise-wide Data Quality SLA template (defined in Section 3) that provides a consistent structure and terminology for all SLAs. This template incorporates modern data management concepts, including data contracts, agentic data stewardship, and integration with MLOps/DataOps pipelines.

- **Per-Product SLA Documents**: Individual, tailored SLA documents created for each critical data product or dataset. These documents are derived from the global template and specify unique data quality metrics, thresholds, and operational details relevant to the specific data asset.

The scope includes datasets, data services, APIs, and data products across various platforms, including cloud-native, multi-cloud, and hybrid environments. It is designed to support data mesh domains and data fabric overlays, ensuring SLAs are adaptable to decentralized governance models.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | Provides the overarching framework authorizing SLA creation, enforcement, and dispute resolution. The Data Governance Council (DGC) often serves as the final escalation authority. AI governance considerations, including compliance with the EU AI Act, are increasingly integrated here. |
| KA-04: Data Storage and Operations | Operational SLAs (e.g., system uptime, data pipeline availability) are prerequisites for Data Quality SLAs. Failures in storage or operations can directly degrade data quality (e.g., data loss, corruption). This KA also covers monitoring and alerting infrastructure. |
| KA-06: Data Integration and Interoperability | Data contracts, a key output of this KA, define the terms of data exchange. Data Quality SLAs extend these contracts by adding quantitative quality dimensions and enforceable standards. |
| KA-09: Metadata Management | Metadata provides essential context for SLAs, including data lineage, definitions of Critical Data Elements (CDEs), and data product ownership. It supports root cause analysis and auditability of quality issues. |
| KA-11: Data Quality | The foundational KA for defining quality dimensions, metrics, and frameworks that underpin SLA content. This deliverable is a direct output from this KA. |
| KA-12: Artificial Intelligence and Machine Learning | Emerging integration of data quality SLAs with MLOps and AI governance frameworks to ensure data used in AI models meets ethical and quality standards. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Quality Manager (DQ Mgr) | Ultimately accountable for the creation, standardization, and oversight of the Data Quality SLA process across the organization, ensuring alignment with enterprise data governance and AI governance policies. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Responsible for drafting individual SLAs, defining metrics and thresholds, monitoring SLA adherence, and producing quality reports. Collaborates closely with data stewards and product managers. |
| **S (Supportive)** | Data Product Manager (DPM) | Supports SLA development by articulating business requirements, negotiating achievable quality targets, and facilitating communication between data consumers and providers. |
| **C (Consulted)** | Data Owner (D-Owner), Data Steward (D-Steward), AI Ethics Officer | Consulted to provide input on critical data elements, business impact of poor quality, acceptable quality thresholds, and AI ethical considerations where applicable. |
| **I (Informed)** | Data Engineering Manager (DE Mgr), MLOps Engineer | Kept informed of SLA requirements and performance to ensure data pipelines, AI model pipelines, and systems can support agreed-upon quality levels and remediation workflows. |

### 2.2. Section-Level RASCI

| SLA Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Business Context & Scope | DQ Analyst | DPM, D-Owner, AI Ethics Officer | DQ Mgr |
| Data Quality Dimensions & Metrics | DQ Analyst | D-Steward, SME, MLOps Engineer | DQ Mgr |
| Service Level Objectives (SLOs) | DQ Analyst | D-Owner, DPM | D-Owner |
| Monitoring & Reporting | DQ Analyst | DE Mgr, MLOps Engineer | DQ Mgr |
| Escalation & Remediation | DQ Analyst | DGC, D-Owner, AI Ethics Officer | DQ Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Data Quality Service Level Agreement. Replace all placeholders `[...]` with specific information for the data product or service.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Data Quality Service Level Agreement for [Data Product Name] |
| Document ID | SLA-DQ-[YYYYMMDD]-[Seq#] |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Review Date | [YYYY-MM-DD, typically quarterly or annually] |
| Data Provider | [Team/Department Name, e.g., Data Engineering] |
| Data Consumer | [Team/Department Name, e.g., Sales Analytics] |
| Data Product Owner | [Name, e.g., Data Product Manager] |
| AI Ethics Officer (if applicable) | [Name] |

### 3.2. Business Context

> *Describe the business purpose of the data product and why data quality is critical for its intended use. Explain the potential business impact of poor data quality (e.g., incorrect reporting, flawed analysis, poor customer experience, regulatory risk). Include AI governance implications if data supports AI/ML models.*

**Input needed**: Business requirements document, interviews with data consumers, AI governance policies.  
**Who fills this**: DQ Analyst, with input from DPM, D-Owner, and AI Ethics Officer.

[Insert Business Context Description]

### 3.3. Scope of Agreement

> *Clearly define the boundaries of this SLA. Specify which datasets, tables, data services, or APIs are covered. List the specific Critical Data Elements (CDEs) that are subject to the quality metrics defined in this agreement. Include references to data contracts where applicable.*

**Input needed**: [`templates/templates-KA-02-data-architecture.md`](templates/templates-KA-02-data-architecture.md), [`templates/templates-KA-09-metadata-management.md`](templates/templates-KA-09-metadata-management.md), **`templates/templates-KA-06-data-integration-interoperability.md`**.  
**Who fills this**: DQ Analyst.

**Covered Data Assets**:

| Asset Type | Name / Endpoint | Location / Database |
| :--- | :--- | :--- |
| [e.g., Table] | [e.g., `prod.sales_transactions`] | [e.g., Snowflake] |
| [e.g., API] | [e.g., `/v1/customer/{id}`] | [e.g., Customer API Service] |

**Critical Data Elements (CDEs)**:

- [e.g., `transaction_id`]
- [e.g., `customer_email`]
- [e.g., `transaction_amount`]
- [e.g., `product_sku`]

### 3.4. Data Quality Dimensions and Metrics

> *For each relevant data quality dimension, define the specific metric that will be used for measurement, the calculation formula, and the tool used to measure it. This is the core of the SLA. Include modern dimensions such as AI data fairness or lineage completeness if applicable.*

**Input needed**: [`templates/templates-KA-11-data-quality.md`](templates/templates-KA-11-data-quality.md), [`templates/templates-KA-11-data-quality.md`](templates/templates-KA-11-data-quality.md).  
**Who fills this**: DQ Analyst, with input from D-Steward and MLOps Engineer.

| Dimension | Metric | Calculation Formula | Measurement Tool |
| :--- | :--- | :--- | :--- |
| **Completeness** | [e.g., CDE Fill Rate] | `(Number of non-null values / Total number of records) * 100%` | [e.g., dbt-expectations] |
| **Uniqueness** | [e.g., Duplicate Record Count] | `Total records - Count of distinct primary keys` | [e.g., Great Expectations] |
| **Timeliness** | [e.g., Data Latency] | `Timestamp of data availability - Timestamp of source event` | [e.g., Monte Carlo] |
| **Validity** | [e.g., Format Compliance Rate] | `(Number of values matching regex '[pattern'] / Total records) * 100%` | [e.g., Custom SQL] |
| **Accuracy** | [e.g., Address Validation Rate] | `(Number of addresses verified by third-party service / Total addresses) * 100%` | [e.g., Melissa Clean Suite] |
| **Consistency** | [e.g., Cross-System Discrepancy] | `Count of records where [System A].[Field] != [System B].[Field]` | [e.g., Custom Python Script] |
| **Lineage Completeness** | [e.g., Percentage of data elements with full lineage] | `(Number of data elements with complete lineage / Total data elements) * 100%` | [e.g., Metadata Catalog Tool] |
| **Fairness (if AI data)** | [e.g., Bias Metric Score] | `[Defined per AI fairness framework]` | [e.g., Fairness Toolkit] |

### 3.5. Service Level Objectives (SLOs)

> *Define the agreed-upon target and threshold for each metric. The **Target** is the desired state. The **Threshold** is the minimum acceptable level of quality. A breach of the threshold triggers the remediation process. Include AI governance thresholds where relevant.*

**Input needed**: Business impact analysis, technical feasibility assessment, AI governance policies.  
**Who fills this**: DQ Analyst, negotiated with D-Owner, DPM, and AI Ethics Officer.

| Metric | Target | Threshold |
| :--- | :--- | :--- |
| [e.g., CDE Fill Rate] | [e.g., > 99.9%] | [e.g., >= 99.5%] |
| [e.g., Duplicate Record Count] | [e.g., 0] | [e.g., <= 5] |
| [e.g., Data Latency] | [e.g., < 15 minutes] | [e.g., <= 1 hour] |
| [e.g., Format Compliance Rate] | [e.g., 100%] | [e.g., >= 99.8%] |
| [e.g., Address Validation Rate] | [e.g., > 98%] | [e.g., >= 95%] |
| [e.g., Cross-System Discrepancy] | [e.g., 0] | [e.g., <= 10] |
| [e.g., Fairness Metric] | [e.g., Bias score < 0.05] | [e.g., Bias score < 0.10] |

### 3.6. Monitoring, Reporting, and Auditing

> *Describe how the SLOs will be monitored, how results will be reported, and the process for auditing compliance. Include integration with DataOps/MLOps pipelines and AI governance monitoring where applicable.*

**Input needed**: **`templates/templates-KA-04-data-storage-operations.md`**.  
**Who fills this**: DQ Analyst.

- **Monitoring Frequency**: [e.g., Real-time for critical metrics, daily batch for others]
- **Reporting Mechanism**: [e.g., A dedicated Data Quality Dashboard in Tableau, updated hourly]
- **Reporting Frequency**: [e.g., Daily summary report via email, monthly review meeting]
- **Audit Process**: [e.g., The Data Governance Office will conduct a quarterly audit of the monitoring process and results to ensure accuracy and impartiality. AI governance audits will be coordinated with the AI Ethics Office.]

### 3.7. Escalation and Remediation Process

> *Define the step-by-step process for handling an SLA breach. Who is notified? What are the expected response and resolution times? What are the consequences for repeated breaches? Include escalation to AI Ethics Officer or Data Governance Council for AI-related data quality issues.*

**Input needed**: [`templates/templates-KA-01-data-governance.md`](templates/templates-KA-01-data-governance.md), **`reference/role-definitions.md`**.  
**Who fills this**: DQ Analyst.

| Level | Trigger | Notified Parties | Expected Response Time | Expected Resolution Time |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Any SLO threshold breached | Data Provider (on-call), Data Steward | [e.g., 30 minutes] | [e.g., 4 hours] |
| **2** | Resolution time for Level 1 exceeded | DQ Analyst, DE Mgr, DPM | [e.g., 1 hour] | [e.g., 24 hours] |
| **3** | Resolution time for Level 2 exceeded | D-Owner, DQ Mgr, AI Ethics Officer (if AI data) | [e.g., 4 hours] | [e.g., 3 business days] |
| **4** | Resolution time for Level 3 exceeded | Data Governance Council, CDO | [e.g., 1 business day] | [e.g., Root Cause Analysis required] |

**Consequences for Non-Compliance**: [e.g., For more than 3 Level 3 breaches in a quarter, a formal Post-Mortem and Corrective Action Plan is required, to be presented to the DGC. Financial penalties (chargebacks) may apply if the data is provided to an external party. For AI data, non-compliance may trigger additional governance reviews or model retraining requirements.]

### 3.8. Signatures

> *Formal sign-off from both the data provider and consumer representatives signifies their agreement to the terms of this SLA. Include AI Ethics Officer signature if applicable.*

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Data Provider Representative | [Name of DE Mgr or equivalent] | _____________ | [YYYY-MM-DD] |
| Data Consumer Representative | [Name of D-Owner or DPM] | _____________ | [YYYY-MM-DD] |
| AI Ethics Officer (if applicable) | [Name] | _____________ | [YYYY-MM-DD] |
| Approved By | [Name of DQ Mgr] | _____________ | [YYYY-MM-DD] |

---

## 4. Example

> *This is a realistic, filled-in example of a Data Quality SLA for a fictional company, GlobalRetail Inc.* 

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Data Quality Service Level Agreement for Customer Master Data Product |
| Document ID | SLA-DQ-20260208-001 |
| Version | 1.0 |
| Effective Date | 2026-03-01 |
| Review Date | 2026-06-01 |
| Data Provider | Master Data Management (MDM) Team |
| Data Consumer | Marketing Analytics Team |
| Data Product Owner | Sarah Lee (Data Product Manager) |
| AI Ethics Officer | Michael Tan |

### 4.2. Business Context

GlobalRetail Inc.'s Marketing Analytics team relies on the Customer Master Data Product to drive personalized marketing campaigns, calculate customer lifetime value, and segment the customer base. The accuracy and completeness of customer contact information and purchase history are critical. Poor data quality leads to wasted marketing spend (undeliverable emails), inaccurate analytics, and a negative customer experience.

Additionally, customer data feeds AI-driven recommendation engines and churn prediction models. Ensuring data quality supports AI fairness and compliance with the EU AI Act, mitigating risks of biased or unethical model outcomes.

### 4.3. Scope of Agreement

**Covered Data Assets**:

| Asset Type | Name / Endpoint | Location / Database |
| :--- | :--- | :--- |
| Table | `mdm.customer_master` | Snowflake |
| View | `analytics.active_customers_vw` | Snowflake |

**Critical Data Elements (CDEs)**:

- `customer_id`
- `email_address`
- `is_email_verified`
- `first_name`
- `last_name`
- `lifetime_value`
- `last_purchase_date`

### 4.4. Data Quality Dimensions and Metrics

| Dimension | Metric | Calculation Formula | Measurement Tool |
| :--- | :--- | :--- | :--- |
| **Completeness** | Verified Email Fill Rate | `(Count of records where is_email_verified = TRUE / Total active customers) * 100%` | Great Expectations |
| **Uniqueness** | Duplicate Customer ID Count | `Total records in customer_master - Count of distinct customer_id` | dbt-expectations |
| **Timeliness** | LTV Update Latency | `Timestamp of LTV calculation job completion - Timestamp of last sales transaction ingestion` | Monte Carlo |
| **Validity** | Email Format Compliance | `(Count of records where email_address matches regex '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' / Total active customers) * 100%` | Custom SQL |
| **Accuracy** | LTV Accuracy vs. Source | `AVG(ABS(customer_master.lifetime_value - sales_ledger.total_spend)) for matched customers` | Custom Python Script |
| **Consistency** | Name Case Consistency | `Count of records where first_name != INITCAP(first_name) OR last_name != INITCAP(last_name)` | Custom SQL |
| **Fairness** | Demographic Parity Difference | `Difference in positive outcome rates across demographic groups` | Fairness Toolkit |

### 4.5. Service Level Objectives (SLOs)

| Metric | Target | Threshold |
| :--- | :--- | :--- |
| Verified Email Fill Rate | > 95% | >= 90% |
| Duplicate Customer ID Count | 0 | <= 2 |
| LTV Update Latency | < 6 hours | <= 12 hours |
| Email Format Compliance | 100% | >= 99.9% |
| LTV Accuracy vs. Source | < $1.00 | <= $5.00 |
| Name Case Consistency | 0 | <= 10 |
| Demographic Parity Difference | < 0.05 | <= 0.10 |

### 4.6. Monitoring, Reporting, and Auditing

- **Monitoring Frequency**: Uniqueness, Validity, Consistency, and Fairness metrics are monitored on every data commit. Completeness and Timeliness are monitored via a batch process that runs every hour.
- **Reporting Mechanism**: A real-time Data Quality Dashboard (ID: DQ-03) in Tableau shows the current status of all SLOs, integrated with the AI governance dashboard.
- **Reporting Frequency**: Automated alerts are sent to the `#customer-data-quality` Slack channel upon any threshold breach. A weekly summary is emailed to all stakeholders, including the AI Ethics Officer.
- **Audit Process**: The Data Governance Office conducts a quarterly audit of the Great Expectations and dbt test results against the dashboard to ensure reporting accuracy. AI governance audits are coordinated semi-annually with the AI Ethics Office.

### 4.7. Escalation and Remediation Process

| Level | Trigger | Notified Parties | Expected Response Time | Expected Resolution Time |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `Duplicate Customer ID Count` > 2 | MDM On-call Engineer, Customer Data Steward | 15 minutes | 2 hours |
| **2** | Resolution time for Level 1 > 2 hours | MDM Team Lead, Marketing Analytics Lead | 30 minutes | 8 hours |
| **3** | `Verified Email Fill Rate` < 90% for > 12 hours or Fairness metric breach | Customer Data Owner, DQ Manager, AI Ethics Officer | 2 hours | 48 hours |
| **4** | Resolution time for Level 3 > 48 hours | Data Governance Council, CDO | 24 hours | Root Cause Analysis and formal Corrective Action Plan required within 5 business days. |

**Consequences for Non-Compliance**: If the `Verified Email Fill Rate` remains below 90% for more than 72 hours, a 10% chargeback of the MDM team's operational budget for the month will be credited to the Marketing department's budget. For AI fairness breaches, additional governance reviews and potential suspension of affected AI models may be enforced.

### 4.8. Signatures

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Data Provider Representative | John Smith (MDM Team Lead) | *John Smith* | 2026-02-28 |
| Data Consumer Representative | Jane Doe (Customer Data Owner) | *Jane Doe* | 2026-02-28 |
| AI Ethics Officer | Michael Tan | *Michael Tan* | 2026-02-28 |
| Approved By | David Chen (Data Quality Manager) | *David Chen* | 2026-02-28 |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Deliverable | **templates/templates-KA-06-data-integration-interoperability.md** |
| AI Governance Framework | Knowledge Area | **templates/templates-KA-12-data-handling-ethics.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] All 8 sections of the master template are present.
- [x] The SLA is co-signed by both a provider and a consumer representative.
- [x] At least 3 data quality dimensions are included.
- [x] Every metric has a clearly defined Target and Threshold in the SLOs.
- [x] The escalation path has at least 3 levels.
- [x] The `Business Context` section clearly explains the business impact of poor quality.
- [x] The `Scope` section lists specific, identifiable data assets (tables, views, or APIs).
- [x] The `Example` section is filled with realistic, contextually appropriate data.
- [x] AI governance considerations are included where applicable.
- [x] Metrics and tools reflect modern architectures (e.g., data mesh, cloud-native).

### 5.2. Review Checklist

| Review Area | Question | Reviewer |
| :--- | :--- | :--- |
| **Clarity** | Are the metric definitions and calculations unambiguous? | DQ Analyst |
| **Measurability** | Can every defined metric be realistically measured with available tools? | DE Manager |
| **Achievability** | Are the SLO targets and thresholds achievable given current systems and processes? | Data Provider |
| **Relevance** | Do the selected metrics directly support the business purpose described in the context? | Data Consumer |
| **Enforceability** | Is the escalation process clear, and are the consequences for non-compliance meaningful? | DQ Manager |
| **AI Governance** | Are AI-related data quality and fairness metrics included and appropriately governed? | AI Ethics Officer |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | Knowledge Area | File Path |
| :--- | :--- | :--- |
| Data Quality Framework | KA-11: Data Quality | `templates/templates-KA-11-data-quality.md` |
| Data Quality Metrics | KA-11: Data Quality | `templates/templates-KA-11-data-quality.md` |
| SLA Documentation | KA-04: Data Storage and Operations | `templates/templates-KA-04-data-storage-operations.md` |
| Data Contracts | KA-06: Data Integration and Interoperability | `templates/templates-KA-06-data-integration-interoperability.md` |
| AI Governance Framework | KA-12: Artificial Intelligence | `templates/templates-KA-12-data-handling-ethics.md` |

### 6.2. Consumers (Outputs)

| Output Name | Knowledge Area | File Path |
| :--- | :--- | :--- |
| Data Contract | KA-06: Data Integration and Interoperability | `templates/templates-KA-06-data-integration-interoperability.md` |
| Data Quality Reports | KA-11: Data Quality | `templates/templates-KA-11-data-quality.md` |
| AI Model Monitoring Reports | KA-12: Artificial Intelligence | `templates/templates-KA-12-data-handling-ethics.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Quality Monitoring** | Monte Carlo, Bigeye, Ataccama | Great Expectations, dbt-expectations, Soda Core |
| **Data Catalog & Metadata** | Alation, Collibra, Atlan | OpenMetadata, Amundsen, DataHub |
| **Workflow & Orchestration** | Airflow (Managed), Prefect Cloud | Airflow (Self-hosted), Dagster, Mage |
| **Dashboarding & Reporting** | Tableau, Power BI, Looker | Metabase, Superset, Grafana |
| **AI Fairness and Governance** | IBM AI Fairness 360, Fiddler AI | Fairlearn, AI Explainability 360 |

### 7.2. Automation Opportunities

- **Automated SLO Monitoring**: Integrate data quality tools like Great Expectations directly into CI/CD pipelines and data orchestration workflows (e.g., Airflow) to automatically run data quality checks on every data commit or batch load.
- **Dynamic Alerting**: Configure alerts to be sent automatically to specific Slack channels or PagerDuty services based on the severity and type of SLA breach.
- **Dashboard Generation**: Use tools like Metabase or Superset with embedded data quality test results to automatically generate and update the SLA compliance dashboard, eliminating manual reporting.
- **Automated Remediation**: For certain predictable quality issues (e.g., inconsistent casing, whitespace issues), simple automated cleaning jobs can be triggered to run immediately upon detection, fixing the issue before it escalates.
- **AI Governance Integration**: Automate fairness and bias detection in AI data pipelines, triggering alerts and remediation workflows when thresholds are breached.
- **Agentic Stewardship Bots**: Emerging agentic data stewardship tools can autonomously monitor SLA compliance, initiate remediation, and escalate issues based on predefined policies.

---

## 8. References

| # | Reference | Type |
| :--- | :--- | :--- |
| [1] | DAMA-DMBOK (2nd Edition), Chapter 13: Data Quality | Book |
| [2] | `references/reference-materials.md` | Internal Reference |
| [3] | `templates/templates-KA-11-data-quality.md` | Internal Reference |
| [4] | `templates/templates-KA-11-data-quality.md` | Internal Reference |
| [5] | DAMA-DMBOK 3.0 (forthcoming, 2025) | Book (forthcoming) |
| [6] | `templates/templates-KA-12-data-handling-ethics.md` | Internal Reference |
| [7] | EU AI Act Compliance Guidelines | External Regulation |


---

# Root Cause Analysis Report


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Header](#31-document-header)
  - [3.2. Issue Summary](#32-issue-summary)
  - [3.3. Investigation Team](#33-investigation-team)
  - [3.4. Evidence and Data Collection](#34-evidence-and-data-collection)
  - [3.5. Analysis Method and Findings](#35-analysis-method-and-findings)
  - [3.6. Root Cause Identification](#36-root-cause-identification)
  - [3.7. Corrective and Preventive Actions (CAPA)](#37-corrective-and-preventive-actions-capa)
  - [3.8. Sign-Off](#38-sign-off)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Issue Summary](#42-issue-summary)
  - [4.3. Investigation Team](#43-investigation-team)
  - [4.4. Evidence and Data Collection](#44-evidence-and-data-collection)
  - [4.5. Analysis Method and Findings](#45-analysis-method-and-findings)
  - [4.6. Root Cause Identification](#46-root-cause-identification)
  - [4.7. Corrective and Preventive Actions (CAPA)](#47-corrective-and-preventive-actions-capa)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs)](#61-prerequisites-inputs)
  - [6.2. Consumers (Outputs)](#62-consumers-outputs)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Root Cause Analysis (RCA) Report** is a formal, structured document that methodically investigates a specific data quality or data-related issue to identify its fundamental cause(s). It transcends symptom-level fixes—such as correcting erroneous records or patching data pipelines—to uncover the underlying process, system, organizational, or human factor failures that allowed the issue to manifest. This deep understanding enables organizations to implement effective corrective and preventive actions (CAPA) that reduce recurrence risk and improve overall data reliability.

In the evolving landscape of data management, where AI governance, cloud-native architectures, and data mesh paradigms are becoming mainstream, the RCA Report plays a critical role in maintaining trustworthiness and compliance across complex, distributed data ecosystems.

> This report provides a structured, evidence-based narrative that answers: *What happened? Why did it happen? And what will be done to ensure it never happens again?* It supports continuous improvement in data quality, governance, and operational resilience.

### 1.2. Scope

**Per Product and Issue** — A Root Cause Analysis Report is typically commissioned for a specific, significant data quality or data integrity issue identified within a particular data product or data domain. Its scope is confined to the investigation of that single issue, including its impact, affected systems, processes, and stakeholders. While the RCA may reveal systemic organizational or architectural weaknesses, the report focuses on actionable insights relevant to the issue at hand.

In modern data environments, this scope may extend to include AI model data inputs, data contracts violations, or data mesh node interactions, reflecting the increasing integration of data quality with AI governance and distributed data ownership.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The RCA process is a critical component of the issue resolution framework established by data governance. Findings often lead to the creation or revision of data policies, standards, and governance workflows, including AI governance policies. |
| KA-09: Metadata Management | Data lineage and metadata are essential inputs for tracing the path of a data error back to its source, especially in complex multi-cloud or data mesh environments. |
| KA-06: Data Integration & Interoperability | RCA frequently identifies issues within data integration pipelines (ETL/ELT), data contracts, or interoperability failures that cause data quality problems. |
| KA-05: Data Security | The investigation may uncover security vulnerabilities, access control lapses, or compliance gaps (e.g., GDPR, EU AI Act) that contributed to the data quality issue. |
| KA-12: AI and Analytics Governance | As AI models increasingly consume data products, RCA may need to consider model input data quality and AI governance risks, integrating findings with MLOps and FinOps practices. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Quality Manager (DQ Mgr) | Ultimately accountable for the completeness, accuracy, and approval of the RCA report. Ensures that root causes are correctly identified and that CAPA recommendations are feasible and aligned with organizational priorities, including AI governance considerations. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Leads the investigation, facilitates RCA sessions, collects and analyzes evidence, and drafts the RCA report. Coordinates with data stewards, engineers, and SMEs to ensure comprehensive analysis. |
| **S (Supportive)** | Data Steward (D-Steward) | Provides deep business context, domain expertise, and validation of findings. Supports identification of impacted stakeholders and helps ensure alignment with data product ownership and data mesh stewardship principles. |
| **C (Consulted)** | Subject Matter Expert (SME), Data Engineer (D-Eng), AI Ethics Officer (if applicable) | SMEs provide specialized knowledge about business processes and data usage. Data Engineers provide technical insights into data pipelines, transformations, and system behavior. AI Ethics Officers may be consulted when AI governance or ethical considerations are implicated. |
| **I (Informed)** | Data Owner (D-Owner), Chief AI Officer (CAIO) (if applicable) | Kept informed of investigation progress and final report. Data Owners are accountable for data domains; CAIO or equivalent roles may be informed when AI governance risks are involved. |

### 2.2. Section-Level RASCI

| Report Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| 1.0 Issue Identification | DQ Analyst | D-Steward | DQ Mgr |
| 2.0 Investigation Team | DQ Analyst | DQ Mgr | DQ Mgr |
| 3.0 Evidence Collection | DQ Analyst | D-Eng, SME | DQ Mgr |
| 4.0 Analysis | DQ Analyst | D-Steward, SME, AI Ethics Officer (if applicable) | DQ Mgr |
| 5.0 Root Cause Identification | DQ Analyst | D-Steward, D-Eng | DQ Mgr |
| 6.0 Corrective/Preventive Actions | DQ Analyst | D-Owner, D-Eng, CAIO (if applicable) | DQ Mgr |

---

## 3. Template

> *The following is the standardized template for a Root Cause Analysis Report. Replace all placeholders `[...]` with issue-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Report Title | Root Cause Analysis Report: [Brief Description of Issue] |
| Report ID | RCA-[YYYYMMDD]-[Issue ID] |
| Data Product | [Name of the Affected Data Product or Data Mesh Node] |
| Version | [e.g., 1.0] |
| Status | [Draft, In Review, Approved, Closed] |
| Report Date | [YYYY-MM-DD] |
| Report Author | [Name of DQ Analyst] |
| Report Approver | [Name of DQ Manager] |

### 3.2. Issue Summary

> *Provide a concise summary of the data quality issue, its business impact, and when it was detected. Reference the corresponding entry in the Issue Log.*

**Input needed**: `09-issue-log.md`  
**Who fills this**: DQ Analyst

- **Issue ID**: [Issue ID from Log]
- **Date Detected**: [YYYY-MM-DD]
- **Problem Statement**: [A clear, one-sentence description of the problem. e.g., "Customer 'Date of Birth' field is being populated with the order date for a subset of e-commerce transactions."]
- **Business Impact**: [Describe the consequences of the issue. e.g., "Inaccurate age-based marketing campaigns, compliance risk with age-restricted products, erosion of customer trust, and potential AI model bias due to corrupted training data."]

### 3.3. Investigation Team

> *List all individuals who participated in the RCA investigation, along with their roles.*

**Input needed**: Meeting minutes, participant list.  
**Who fills this**: DQ Analyst

| Name | Role | Contribution |
| :--- | :--- | :--- |
| [Name] | DQ Analyst (Lead) | Facilitated RCA, authored report |
| [Name] | Data Steward | Provided business context for customer data |
| [Name] | Data Engineer | Analyzed the ETL pipeline and data flows |
| [Name] | SME (Marketing, Compliance, AI Ethics) | Explained domain-specific impacts and AI governance considerations |

### 3.4. Evidence and Data Collection

> *Detail all the information gathered during the investigation. This section should be factual and objective. Link to all relevant documentation and data sources.*

**Input needed**: `KA-09/07-data-lineage.md`, database queries, system logs, process maps, AI model input data audits.  
**Who fills this**: DQ Analyst, with support from D-Eng, AI Governance team.

- **Data Lineage Review**: [Summary of findings from tracing the data from the point of error back to its source, including lineage across data mesh nodes or multi-cloud environments.]
- **System Logs**: [Relevant error messages, timestamps, or transaction IDs from application or database logs.]
- **Process Walkthrough**: [Description of the business and technical processes that create or modify the data in question, including data contracts and data product interactions.]
- **User Interviews**: [Key quotes or summaries from interviews with SMEs, data stewards, or AI model owners.]
- **Data Samples**: [Provide examples of correct vs. incorrect records, including any AI model input data anomalies.]

### 3.5. Analysis Method and Findings

> *Describe the RCA methodology used (e.g., 5 Whys, Fishbone Diagram, Fault Tree Analysis) and present the step-by-step analysis. This section should clearly show the logical path from the problem statement to the root cause.*

**Input needed**: The evidence from the previous section.  
**Who fills this**: DQ Analyst

#### 3.5.1. Method Used: [e.g., 5 Whys]

1.  **Why did the customer's DOB match the order date?**
    > *Because the `customer_dob` field in the `orders` table was incorrectly mapped from the source system.*
2.  **Why was it incorrectly mapped?**
    > *Because the ETL job used the `order_creation_date` as the source field for the `customer_dob` target field.*
3.  **Why did the ETL job use the wrong source field?**
    > *Because the source-to-target mapping document was ambiguous, and the developer made an incorrect assumption.*
4.  **Why was the mapping document ambiguous?**
    > *Because it was not reviewed by a data steward or SME from the customer domain before development.*
5.  **Why was it not reviewed?**
    > *Because the development process at the time did not mandate a formal data stewardship review for ETL changes, nor was there integration with data contracts or automated schema validation.*

*Additional notes:*  
- Consider including AI governance impact analysis if AI models consume this data.  
- Reflect on how modern data architectures (e.g., data mesh) might have influenced the issue propagation or detection.

### 3.6. Root Cause Identification

> *State the final, fundamental root cause(s) of the issue. There may be more than one. Distinguish between the direct cause and the systemic root cause.*

**Input needed**: The final "Why" from the analysis.  
**Who fills this**: DQ Analyst

- **Direct Cause**: [The immediate cause of the problem. e.g., "Incorrect field mapping in the `load_orders` ETL job."]
- **Systemic Root Cause**: [The fundamental process or system failure. e.g., "Lack of a mandatory data stewardship review process for changes to critical data pipelines, absence of automated schema validation, and insufficient integration of data contracts in the SDLC."]

*Forward-looking note:*  
With DAMA-DMBOK 3.0 emphasizing AI governance and data product management, organizations should consider embedding RCA findings into continuous improvement cycles for data mesh governance, data contracts enforcement, and AI model monitoring.

### 3.7. Corrective and Preventive Actions (CAPA)

> *Based on the root cause, recommend specific, actionable steps to fix the problem and prevent it from happening again. Assign an owner and a due date for each action.*

**Input needed**: `10-remediation-plan.md`  
**Who fills this**: DQ Analyst, in consultation with D-Owner, D-Eng, and AI Governance stakeholders.

| Action ID | Action Type | Description | Owner | Due Date |
| :--- | :--- | :--- | :--- | :--- |
| CAPA-001 | Corrective | [Fix the field mapping in the `load_orders` ETL job and reprocess historical data to correct affected records.] | [D-Eng Name] | [YYYY-MM-DD] |
| CAPA-002 | Preventive | [Update the SDLC process to mandate a formal sign-off from the designated Data Steward and AI Ethics Officer for any changes to ETL jobs involving Critical Data Elements or AI model inputs.] | [DG Mgr Name] | [YYYY-MM-DD] |
| CAPA-003 | Preventive | [Implement automated schema validation and data contract enforcement in the data ingestion pipelines to detect and prevent ambiguous mappings.] | [D-Eng Name] | [YYYY-MM-DD] |
| CAPA-004 | Preventive | [Conduct training sessions for developers and data stewards on data contracts, data mesh stewardship responsibilities, and AI governance principles.] | [DG Mgr Name] | [YYYY-MM-DD] |

### 3.8. Sign-Off

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Data Quality Analyst | [Name] | _____________ | [YYYY-MM-DD] |
| Data Steward | [Name] | _____________ | [YYYY-MM-DD] |
| Data Quality Manager | [Name] | _____________ | [YYYY-MM-DD] |
| AI Ethics Officer (if applicable) | [Name] | _____________ | [YYYY-MM-DD] |

---

## 4. Example

> *This is a realistic, filled-in example of a Root Cause Analysis Report for the fictional company GlobalRetail Inc.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Report Title | Root Cause Analysis Report: Product 'Shipping Weight' is Null for 3PL-sourced items |
| Report ID | RCA-20260208-DQ-0145 |
| Data Product | Product Master Data Product |
| Version | 1.0 |
| Status | Approved |
| Report Date | 2026-02-08 |
| Report Author | Alice Johnson (DQ Analyst) |
| Report Approver | Bob Williams (DQ Manager) |

### 4.2. Issue Summary

- **Issue ID**: DQ-0145
- **Date Detected**: 2026-01-25
- **Problem Statement**: The `shipping_weight` attribute for all products sourced from our new Third-Party Logistics (3PL) partner, "ShipFast Inc.", is NULL in the master product database.
- **Business Impact**: This has led to a 100% failure rate in calculating shipping costs for these products at checkout, forcing a manual override process. This causes significant delays, increased operational costs ($5k/day), and a poor customer experience. Additionally, inaccurate shipping cost data risks downstream AI model predictions for logistics optimization.

### 4.3. Investigation Team

| Name | Role | Contribution |
| :--- | :--- | :--- |
| Alice Johnson | DQ Analyst (Lead) | Facilitated RCA, authored report |
| Charles Davis | Data Steward (Product) | Provided business context for product master data |
| Eve Martinez | Data Engineer | Analyzed the new 3PL data ingestion pipeline |
| Frank Miller | SME (Logistics) | Explained the 3PL data feed specifications |
| Grace Lee | AI Ethics Officer | Assessed AI governance implications of data quality issue |

### 4.4. Evidence and Data Collection

- **Data Lineage Review**: The `shipping_weight` field originates from a daily CSV file (`products_YYYYMMDD.csv`) delivered by ShipFast Inc. via SFTP. An ETL job (`ingest_shipfast_products`) parses this file and loads it into a staging table, which then merges into the main `product_master` table. Data lineage diagrams confirmed no upstream data transformations altered this field.
- **System Logs**: The ETL job logs for `ingest_shipfast_products` showed no errors. The job reported successful completion each day, but lacked schema validation logs.
- **Process Walkthrough**: The data feed specification document from ShipFast Inc. was reviewed. It specifies the weight field header as `item_weight_kg`.
- **Data Samples**: A sample of the `products_20260125.csv` file was inspected. The header for the weight column was found to be `weight_in_kg`, not `item_weight_kg` as documented.
- **AI Model Input Audit**: The logistics optimization AI model was found to consume the `shipping_weight` field directly. The NULL values caused model prediction errors flagged by MLOps monitoring tools.

### 4.5. Analysis Method and Findings

#### 4.5.1. Method Used: Fishbone Diagram (Ishikawa)

A virtual whiteboard session was held to construct a fishbone diagram, exploring potential causes across People, Process, Technology, Data, and Governance.

- **Technology**: The ETL script was hardcoded to look for the header `item_weight_kg`. When this header was not found, the script did not throw an error but simply loaded a NULL value for that column.
- **Process**: The process for onboarding a new data feed did not include a step to programmatically validate the incoming file structure (headers, data types) against the provided specification before processing.
- **Data**: The data provider (ShipFast Inc.) sent a file with a header (`weight_in_kg`) that did not match their own documentation (`item_weight_kg`).
- **People**: The developer who wrote the ETL script did not implement defensive coding practices (e.g., error handling for missing columns).
- **Governance**: There was no formal data contract or schema validation enforcement between GlobalRetail and ShipFast Inc., nor a data steward sign-off on the onboarding process.
- **AI Governance**: The AI Ethics Officer highlighted that the lack of data quality controls on model inputs could propagate errors into AI-driven decisions, increasing operational risk.

### 4.6. Root Cause Identification

- **Direct Cause**: The ETL script `ingest_shipfast_products` failed to parse the shipping weight because the CSV header `weight_in_kg` did not match the expected header `item_weight_kg`.
- **Systemic Root Cause**: The data ingestion framework lacks a mandatory schema validation step. Incoming data files are not automatically checked for structural integrity against their specifications before being processed, making the system brittle to provider-side changes. Additionally, the absence of formal data contracts and stewardship sign-offs allowed this misalignment to go undetected. AI governance processes did not include monitoring of data quality at the model input level.

### 4.7. Corrective and Preventive Actions (CAPA)

| Action ID | Action Type | Description | Owner | Due Date |
| :--- | :--- | :--- | :--- | :--- |
| CAPA-0145-1 | Corrective | Update the `ingest_shipfast_products` ETL script to use the correct header `weight_in_kg`. Backfill all NULL shipping weights from the raw files. | Eve Martinez | 2026-02-10 |
| CAPA-0145-2 | Preventive | Implement a "Schema Validator" module in the data ingestion framework. All new and existing ETL jobs must call this module to validate incoming files. The job must fail and send an alert if validation fails. | Data Engineering Lead | 2026-04-30 |
| CAPA-0145-3 | Preventive | Update the "New Data Provider Onboarding" SOP to include a formal sign-off on schema validation test results by the responsible Data Steward and AI Ethics Officer. | Charles Davis | 2026-03-15 |
| CAPA-0145-4 | Preventive | Integrate data contract enforcement and automated alerts for schema deviations into the data mesh governance framework. | Data Governance Manager | 2026-05-01 |
| CAPA-0145-5 | Preventive | Establish AI model input data quality monitoring as part of MLOps workflows to detect and alert on anomalies. | MLOps Engineer | 2026-04-15 |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Concepts | [concepts/data-contracts.md](references/concepts-modern-paradigms.md) |
| AI Governance | Knowledge Area | [knowledge-areas/KA-12-ai-governance.md](knowledge-areas/KA-12-data-handling-ethics.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The problem statement is clear, concise, and specific to the data product or domain.
- [x] The business impact is quantified or clearly qualified, including operational, compliance, and AI governance risks.
- [x] Evidence is comprehensive, objective, and supports the analysis.
- [x] A clear, logical path from symptom to root cause is demonstrated, using recognized RCA methodologies.
- [x] The distinction between the direct cause and the systemic root cause is explicitly made.
- [x] Corrective actions directly address the immediate problem and include remediation steps.
- [x] Preventive actions address systemic root causes, including process, technology, and governance improvements.
- [x] All CAPA items are specific, measurable, assigned, and time-bound.
- [x] The report has been reviewed and signed off by all required stakeholders, including AI governance roles where applicable.
- [x] The report references relevant data governance, metadata, and AI governance frameworks consistent with DAMA-DMBOK 3.0 principles.

### 5.2. Review Checklist

| Review Area | Question | Finding (Pass/Fail) |
| :--- | :--- | :--- |
| **Clarity** | Is the report easy to understand for both technical and non-technical audiences? | Pass |
| **Completeness** | Are all sections of the template filled out appropriately? | Pass |
| **Evidence** | Is the root cause supported by objective, verifiable evidence? | Pass |
| **Logic** | Is the analytical reasoning sound and free from logical fallacies? | Pass |
| **Actionability** | Are the recommended CAPAs realistic and sufficient to prevent recurrence? | Pass |
| **Governance Alignment** | Does the report align with current data governance and AI governance frameworks? | Pass |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | Path / Link | Purpose |
| :--- | :--- | :--- |
| Issue Log | `templates/templates-KA-11-data-quality.md` | Provides the initial problem statement and tracking ID. |
| Remediation Plan | `templates/templates-KA-11-data-quality.md` | May contain initial triage information before a full RCA is commissioned. |
| Data Lineage | `templates/templates-KA-09-metadata-management.md` | Essential for tracing the data flow to identify the point of failure. |
| Data Contracts | `#` | Provides context on contractual data quality and schema expectations. |
| AI Governance Framework | `#` | Guides considerations for AI-related data quality impacts. |

### 6.2. Consumers (Outputs)

| Output Name | Path / Link | Purpose |
| :--- | :--- | :--- |
| Data Quality Rules | `templates/templates-KA-11-data-quality.md` | The findings from the RCA will be used to create new or update existing data quality rules to monitor for this issue proactively. |
| Remediation Plan | `templates/templates-KA-11-data-quality.md` | To track and manage implementation of CAPA actions. |
| AI Model Monitoring Reports | `templates/templates-KA-12-data-handling-ethics.md` | To incorporate data quality findings into AI model monitoring and governance. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Issue Tracking** | Jira, ServiceNow, Azure DevOps | Redmine, Bugzilla |
| **Collaborative Whiteboard** | Miro, Mural | OpenBoard |
| **Wiki/Knowledge Base** | Confluence, SharePoint | BookStack, DokuWiki |
| **Data Quality Platforms** | Collibra, Informatica DQ, Ataccama | Great Expectations, Soda Core |
| **Data Lineage and Metadata** | Alation, Informatica EDC | Apache Atlas, Amundsen |
| **AI Governance & MLOps** | MLflow, DataRobot, Azure ML | Kubeflow, MLRun |

### 7.2. Automation Opportunities

- **Automated RCA Triggering**: Configure the Data Quality Monitoring tool to automatically create an RCA ticket in Jira when a Critical Data Element's quality score drops below a predefined threshold for more than an hour.
- **Evidence Gathering**: Develop scripts to automatically pull relevant system logs, data lineage diagrams, data contract validation reports, and data samples based on the Issue Log entry, attaching them to the RCA ticket.
- **CAPA Tracking**: Integrate the issue tracking system with project management tools to automatically create tasks for assigned CAPAs and monitor their completion status.
- **Schema Validation Automation**: Implement automated schema validation tools integrated into CI/CD pipelines for data ingestion and transformation jobs.
- **AI Model Input Monitoring**: Deploy automated data quality checks on AI model input datasets, triggering RCA processes when anomalies are detected.

---

## 8. References

| Ref | Description |
| :-- | :--- |
| [1] | DAMA-DMBOK: Data Management Body of Knowledge, 2nd Edition, Chapter 13: "Data Quality". |
| [2] | DAMA-DMBOK 3.0 (forthcoming 2025): Emphasizes AI governance, data mesh, and cloud-native data management principles. |
| [3] | Internal Document: `references/reference-materials.md` |
| [4] | Internal Document: `templates/templates-KA-01-data-governance.md` |
| [5] | EU AI Act and GDPR Compliance Guidelines: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32021R0740 |
