<!-- NAV-TOC -->
## Sections in This File

This file contains **11 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 24 | DW BI Strategy |
| 416 | DW Architecture |
| 723 | Dimensional Model Standards |
| 1057 | BI Standards |
| 1394 | Dimensional Model |
| 1723 | ETL Documentation |
| 2131 | Report Specifications |
| 2503 | Dashboard Specifications |
| 2874 | KPI Definitions |
| 3290 | Source System Analysis |
| 3737 | Data Mart Design |

## Sections in This File

This file contains **13 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 1 | DW BI Strategy |
| 393 | DW Architecture |
| 700 | Dimensional Model Standards |
| 1034 | BI Standards |
| 1366 | End of BI Standards Deliverable Template |
| 1371 | Dimensional Model |
| 1700 | ETL Documentation |
| 2108 | Report Specifications |
| 2475 | End of Report Specifications Template |
| 2480 | Dashboard Specifications |
| 2851 | KPI Definitions |
| 3267 | Source System Analysis |
| 3714 | Data Mart Design |

---

# DW BI Strategy


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
  - [3.2. Vision and Business Alignment](#32-vision-and-business-alignment)
  - [3.3. Current State Assessment](#33-current-state-assessment)
  - [3.4. Future State Architecture](#34-future-state-architecture)
  - [3.5. BI and Analytics Roadmap](#35-bi-and-analytics-roadmap)
  - [3.6. Implementation Plan and Roadmap](#36-implementation-plan-and-roadmap)
  - [3.7. Governance and Operating Model](#37-governance-and-operating-model)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Vision and Business Alignment](#42-vision-and-business-alignment)
  - [4.3. Future State Architecture](#43-future-state-architecture)
  - [4.4. BI and Analytics Roadmap](#44-bi-and-analytics-roadmap)
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

The **Data Warehousing (DW) and Business Intelligence (BI) Strategy** is a comprehensive, enterprise-level plan that articulates the vision, architecture, and roadmap for leveraging data warehousing and business intelligence capabilities to drive strategic business outcomes. It ensures alignment between technology initiatives and business objectives, facilitating the transformation of raw data into trusted, actionable insights that empower decision-making at all organizational levels.

This strategy incorporates emerging trends and best practices in modern data management, including cloud-native architectures, data mesh and data fabric paradigms, AI governance, and integration of MLOps and DataOps practices. It also anticipates regulatory compliance requirements such as GDPR, HIPAA, CCPA, and the evolving EU AI Act.

> The DW BI Strategy answers the critical questions: *"How will we use data to improve our business performance?"* and *"What capabilities do we need to build to transform data into a strategic asset?"* It also addresses *"How do we govern and operationalize data and AI assets responsibly and sustainably?"*

Forward-looking note: The forthcoming DAMA-DMBOK 3.0 will expand on the integration of AI governance frameworks, agentic data stewardship, and the elevation of data products and data contracts as foundational elements of DW and BI strategy. Organizations are encouraged to anticipate these shifts and incorporate flexibility for evolving governance and operational models.

### 1.2. Scope

**Global** — This strategy applies enterprise-wide, encompassing all business units, functional areas, and geographic locations. It establishes a unified approach to data warehousing and business intelligence that supports scalability, interoperability, and agility. The scope includes traditional data warehouse systems, modern lakehouse architectures, data mesh domains, and BI/analytics platforms, as well as integration with AI/ML pipelines and operational systems.

The strategy also defines the governance and operating models necessary to support agentic data stewardship, data product management, and compliance with data privacy and AI regulations.

This scope explicitly embraces the synergy of modern architectural paradigms such as data mesh and data fabric, enabling decentralized data ownership while maintaining enterprise-wide data interoperability and security. It also includes the operationalization of MLOps, DataOps, and FinOps practices to ensure continuous delivery, quality, and cost optimization.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The DW BI Strategy is executed within the framework established by Data Governance, which ensures data quality, security, compliance, and increasingly, AI governance and ethical use of data. See also [knowledge-areas/KA-01-data-governance.md](knowledge-areas/KA-01-data-governance.md). |
| KA-02: Data Architecture | The strategy relies on the enterprise data architecture blueprint for technical guidance, including modern architectural patterns such as data mesh, data fabric, and cloud-native designs. See [knowledge-areas/KA-02-data-architecture.md](knowledge-areas/KA-02-data-architecture.md). |
| KA-03: Data Modeling and Design | Data models (conceptual, logical, physical) are foundational inputs for designing the data warehouse, lakehouse, and BI solutions defined in the strategy. See [knowledge-areas/KA-03-data-modeling-design.md](knowledge-areas/KA-03-data-modeling-and-design.md). |
| KA-06: Data Security and Privacy | Ensures that data warehousing and BI solutions comply with security policies and privacy regulations such as GDPR, HIPAA, CCPA, and the EU AI Act. See [knowledge-areas/KA-06-data-security-privacy.md](knowledge-areas/KA-06-data-integration-interoperability.md). |
| KA-08: Data Warehousing and Business Intelligence | This deliverable directly supports the core objectives of this knowledge area, providing the strategic framework for DW and BI initiatives. See [knowledge-areas/KA-08-data-warehousing-bi.md](knowledge-areas/KA-08-data-warehousing-and-bi.md). |
| KA-09: Data Integration and Interoperability | Defines the strategies for integrating diverse data sources into the warehouse and BI platforms, including real-time streaming and batch processing. See [knowledge-areas/KA-09-data-integration.md](knowledge-areas/KA-09-metadata-management.md). |
| KA-11: Data Quality | The success of the BI component of the strategy depends on robust data quality management, including automated testing and certification processes. See [knowledge-areas/KA-11-data-quality.md](knowledge-areas/KA-11-data-quality.md). |
| KA-14: Artificial Intelligence and Machine Learning | The strategy incorporates AI governance, MLOps integration, and the use of BI insights to support AI-driven decision-making and operationalization. See [knowledge-areas/KA-14-artificial-intelligence.md](knowledge-areas/KA-14-data-management-maturity-assessment.md). |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Chief Data Officer (CDO) | Ultimately accountable for the DW BI Strategy, ensuring alignment with enterprise data and AI strategies, business objectives, and compliance requirements. The CDO champions the integration of AI governance and emerging data management paradigms. |
| **R (Responsible)** | Data Analytics Manager (DA Mgr) | Responsible for developing, maintaining, and overseeing execution of the DW BI Strategy, including coordination with data engineering, governance, and business units. Leads the alignment of BI initiatives with business goals and emerging technologies. |
| **S (Supportive)** | Data Engineering Manager (DE Mgr), Data Warehouse Architect (DW Arch), MLOps Engineer, Data Product Manager | Provide technical expertise and support in designing, building, and operationalizing the data warehouse, BI infrastructure, AI/ML integration, and data product lifecycle management. Support implementation of data contracts and agentic stewardship. |
| **C (Consulted)** | Data Governance Council (DGC), Business Leaders, AI Ethics Officer | Consulted to ensure the strategy meets business needs, governance policies, ethical AI use, and regulatory compliance. The AI Ethics Officer advises on responsible AI deployment and compliance with the EU AI Act and other regulations. |
| **I (Informed)** | All Data Management Office (DMO) Members, Data Product Managers, BI Developers | Kept informed of the strategy and its progress, as it impacts their work and the organization's data and AI capabilities. |

### 2.2. Section-Level RASCI

| Strategy Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Vision and Business Alignment | DA Mgr | Business Leaders, CDO | CDO |
| Architecture and Technology | DW Arch, DE Mgr | DA Mgr, MLOps Engineer, Data Product Manager | CDO |
| Roadmap and Implementation Plan | DA Mgr | DE Mgr, DW Arch, MLOps Engineer, AI Ethics Officer | CDO |
| Governance and Operations | DA Mgr | DGC, AI Ethics Officer, Data Product Manager | CDO |

---

## 3. Template

> *The following is the standardized template for creating a DW BI Strategy. Replace all placeholders `[...]` with organization-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | [Organization Name] DW BI Strategy |
| Document ID | STR-DWBI-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Review Date | [YYYY-MM-DD, typically annual] |
| Owner | [Data Analytics Manager Name] |
| Approver | [Chief Data Officer Name] |

### 3.2. Vision and Business Alignment

> *Define the long-term vision for DW and BI in the organization. This should be an aspirational statement that connects data and analytics to business success. Then, detail the specific business goals the strategy will support.*

**Vision**: [e.g., "To empower every department with self-service analytics and trusted data, fostering a culture of data-driven decision-making that drives competitive advantage. We will leverage modern cloud-native architectures, AI-enabled analytics, and governed data products to accelerate innovation and operational excellence."]

**Business Goals Supported**:
- [e.g., Increase customer retention by 15% through personalized marketing campaigns powered by integrated customer 360 views]
- [e.g., Reduce operational costs by 10% by optimizing supply chain logistics using predictive analytics]
- [e.g., Improve product development by identifying emerging market trends through advanced BI and AI insights]
- [e.g., Ensure compliance with data privacy and AI regulations, mitigating risk and building customer trust]

> *Practical guidance:* Align your vision with enterprise strategic objectives and emerging data management trends such as AI governance, data mesh, and cloud-native architectures. Clearly articulate how DW and BI capabilities will deliver measurable business value.

### 3.3. Current State Assessment

> *Provide an honest assessment of the current DW and BI landscape. This includes an inventory of existing tools, an evaluation of data quality and accessibility, and an analysis of the organization's analytical maturity.*

**Existing Tools and Technologies**:  
[e.g., List current databases (e.g., on-premise SQL Server, cloud data lakes), ETL tools (e.g., Informatica, Talend), BI platforms (e.g., Power BI, Tableau), and AI/ML tools.]

**Data Landscape**:  
[e.g., Describe key data sources such as ERP, CRM, IoT devices; note data silos, integration challenges, and data quality issues including timeliness, completeness, and accuracy.]

**Analytical Maturity**:  
[e.g., Assess current capabilities ranging from descriptive reporting to advanced predictive and prescriptive analytics; identify gaps in self-service BI, data literacy, and AI integration.]

**Governance and Compliance Posture**:  
[e.g., Evaluate current data governance maturity, AI governance readiness, and compliance with GDPR, HIPAA, CCPA, and emerging EU AI Act requirements.]

> *Practical guidance:* Use maturity models such as DAMA-DMBOK 3.0’s updated frameworks to benchmark your organization’s readiness for modern data management paradigms. Identify gaps in AI governance and data product management as key focus areas.

### 3.4. Future State Architecture

> *Describe the target architecture for the data warehouse and BI platform. This should include the proposed data model, technology stack, and data integration approach. Use diagrams to illustrate the architecture.*

**Data Warehouse Architecture**:  
[e.g., Adopt a hybrid architecture combining data lakehouse for flexible storage and analytics with data mesh principles to enable domain-oriented data ownership and productization.]

**Technology Stack**:  
[e.g., Specify cloud platforms (AWS, Azure, GCP), data storage (Snowflake, Databricks Lakehouse), ETL/ELT tools (dbt, Airflow), BI platforms (Power BI, Looker), data catalogs (Alation, DataHub), and AI/ML platforms.]

**Data Integration Strategy**:  
[e.g., Employ a combination of batch ETL, real-time streaming (Kafka, Kinesis), data virtualization, and API-based integration to support diverse data consumption patterns.]

**Security and Compliance Controls**:  
[e.g., Integrate data masking, encryption, access controls, and audit logging to meet security policies and regulatory requirements.]

**AI and Analytics Enablement**:  
[e.g., Embed MLOps pipelines, model monitoring, and explainability tools within the architecture to operationalize AI responsibly.]

> *Practical guidance:* Incorporate data contracts to formalize producer-consumer data agreements, and design for agentic data stewardship to empower domain teams. Ensure architecture supports FinOps practices for cost management and includes compliance automation for GDPR and EU AI Act.

### 3.5. BI and Analytics Roadmap

> *Outline the key initiatives and deliverables for the BI and analytics program. This should include the development of new reports, dashboards, and advanced analytics models. Prioritize initiatives based on business impact and feasibility.*

| Initiative | Description | Business Driver | Priority | Timeline |
| :--- | :--- | :--- | :--- | :--- |
| [e.g., Sales Performance Dashboard] | [A dashboard for the sales team to track KPIs in real-time, integrating CRM and ERP data.] | [Improve sales effectiveness] | [High] | [Q1] |
| [e.g., Customer Churn Prediction Model] | [A predictive model to identify at-risk customers using machine learning.] | [Increase customer retention] | [High] | [Q2] |
| [e.g., Supply Chain Optimization Analysis] | [An analysis to identify cost-saving opportunities through demand forecasting.] | [Reduce operational costs] | [Medium] | [Q3] |
| [e.g., AI Governance Framework Implementation] | [Establish policies and tools to ensure ethical AI use and compliance with EU AI Act.] | [Mitigate regulatory risk] | [High] | [Q2] |

> *Practical guidance:* Balance quick wins with strategic initiatives that build foundational capabilities such as data productization, AI governance, and self-service analytics. Include milestones for integrating MLOps and DataOps pipelines.

### 3.6. Implementation Plan and Roadmap

> *Provide a high-level roadmap for the implementation of the DW BI strategy. Break down the implementation into phases, with clear milestones and timelines. This section should also address resource requirements and budget.*

**Phase 1: Foundation (Months 1-6)**  
- Establish governance framework including data and AI governance policies.  
- Select and onboard technology stack aligned with cloud-native and data mesh principles.  
- Build foundational data warehouse and data lakehouse layers.  
- Define roles including Data Product Managers and AI Ethics Officers.  
- Initiate data contract definitions and agentic stewardship pilots.  

**Phase 2: Initial Rollout (Months 7-12)**  
- Develop and launch initial dashboards and reports for pilot business units.  
- Implement automated data quality and data contract enforcement.  
- Integrate MLOps pipelines for initial AI models.  
- Conduct training and change management activities focused on data literacy and stewardship.  

**Phase 3: Enterprise Expansion (Months 13-24)**  
- Roll out DW and BI platform across all business units and geographies.  
- Expand advanced analytics and AI capabilities.  
- Implement data fabric solutions for seamless data access.  
- Monitor and optimize performance, governance, and compliance.  
- Embed FinOps practices to optimize cloud and data costs.  

**Phase 4: Continuous Improvement (Months 25-36)**  
- Mature self-service analytics and data literacy programs.  
- Enhance AI governance with continuous monitoring, ethical reviews, and compliance audits.  
- Evaluate and adopt emerging technologies and standards from DAMA-DMBOK 3.0.  
- Expand agentic stewardship and data product management maturity.  

> *Practical guidance:* Define clear success metrics for each phase and ensure continuous stakeholder engagement. Allocate budget for ongoing training, tool upgrades, and compliance activities.

### 3.7. Governance and Operating Model

> *Define the governance processes and operating model for the DW and BI program. This includes roles and responsibilities, data quality management, and change management processes.*

**Roles and Responsibilities**:  
- **BI Steering Committee**: Provides strategic oversight and prioritization, ensuring alignment with enterprise data and AI strategies.  
- **Data Product Managers**: Own data products as first-class assets, ensuring quality, usability, and compliance. They act as liaisons between domain teams and central governance.  
- **Data Stewards**: Manage data quality, metadata, and compliance within domains, empowered through agentic stewardship models.  
- **BI Developers and Analysts**: Design and deliver reports, dashboards, and analytics models aligned with business needs.  
- **AI Ethics Officer**: Oversees ethical AI use and compliance with AI governance policies, including the EU AI Act and emerging regulations.  
- **MLOps Engineer**: Manages AI/ML model deployment, monitoring, and lifecycle management integrated with BI platforms.  

**Data Quality Framework**:  
- Implement automated data quality monitoring and alerting integrated into data pipelines.  
- Establish data certification processes for trusted data products.  
- Use data contracts to formalize data expectations between producers and consumers, enabling proactive issue resolution.  

**Change Management**:  
- Define a formal process for requesting new reports, data sources, or changes to existing data products.  
- Implement version control and impact analysis for data warehouse schema changes.  
- Manage user access and permissions through role-based access control aligned with governance policies.  

**Compliance and Risk Management**:  
- Regularly audit data and AI assets for compliance with GDPR, HIPAA, CCPA, and EU AI Act.  
- Maintain documentation and evidence for regulatory reporting and internal reviews.  
- Integrate compliance automation tools to streamline audit readiness and reporting.  

> *Practical guidance:* Encourage a culture of shared responsibility through agentic stewardship and empower domain teams with clear accountability supported by central governance. Incorporate continuous training on compliance and ethical data use.

---

## 4. Example

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | GlobalRetail Inc. DW BI Strategy |
| Document ID | STR-DWBI-001 |
| Version | 1.0 |
| Effective Date | 2026-02-08 |
| Review Date | 2027-02-08 |
| Owner | John Doe, Data Analytics Manager |
| Approver | Jane Smith, Chief Data Officer |

### 4.2. Vision and Business Alignment

**Vision**: To become the most data-driven retailer in the industry by providing every employee with the insights they need to delight our customers and optimize our operations. We will leverage a cloud-native data lakehouse architecture, governed data products, and AI-enabled analytics to accelerate innovation and operational excellence.

**Business Goals Supported**:
- Increase customer lifetime value by 20% over the next 3 years through personalized marketing and customer 360 insights.
- Improve supply chain efficiency to reduce stockouts by 30% using predictive demand analytics.
- Achieve a 10% increase in marketing ROI through better campaign targeting and attribution analytics.
- Ensure full compliance with GDPR and emerging EU AI Act regulations to protect customer data and build trust.

### 4.3. Future State Architecture

**Data Warehouse Architecture**: We will implement a modern data lakehouse architecture on a cloud platform. This will combine the scalability of a data lake with the performance and data management capabilities of a traditional data warehouse. Additionally, we will adopt data mesh principles to enable domain teams to own and manage their data products, supported by a data fabric layer for unified data access.

**Technology Stack**:
- **Cloud Platform**: AWS
- **Data Lake**: Amazon S3
- **Data Warehouse**: Snowflake
- **ETL/ELT**: dbt
- **BI Platform**: Tableau
- **Data Catalog**: Alation
- **Streaming**: Kafka
- **MLOps Platform**: MLflow
- **AI Governance Tools**: Custom dashboards integrated with data catalog and model monitoring

### 4.4. BI and Analytics Roadmap

| Initiative | Description | Business Driver | Priority | Timeline |
| :--- | :--- | :--- | :--- | :--- |
| Customer 360 Dashboard | A comprehensive view of each customer, including purchase history, web activity, and marketing interactions. | Increase customer lifetime value | High | Q2 2026 |
| Inventory Optimization Model | A predictive model to forecast demand and optimize inventory levels across all stores. | Reduce stockouts | High | Q3 2026 |
| Marketing Mix Modeling | An analysis to determine the optimal allocation of the marketing budget across different channels. | Increase marketing ROI | Medium | Q4 2026 |
| AI Governance Framework Implementation | Establish policies and monitoring tools to ensure ethical AI use and compliance with EU AI Act. | Mitigate regulatory risk | High | Q2 2026 |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [reference/tools-landscape.md](references/reference-materials.md) |
| Metrics KPIs | Reference | [reference/metrics-kpis.md](references/reference-materials.md) |
| Data Governance Framework | Knowledge Area | [knowledge-areas/KA-01-data-governance.md](knowledge-areas/KA-01-data-governance.md) |
| Data Architecture Blueprint | Knowledge Area | [knowledge-areas/KA-02-data-architecture.md](knowledge-areas/KA-02-data-architecture.md) |
| AI Governance Guide | Guides | **guides/governance/ai-governance.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The strategy has a clear, compelling vision that is aligned with business goals and modern data management trends.
- [x] The future state architecture is well-defined, incorporating cloud-native, data mesh/fabric, and AI governance considerations.
- [x] The implementation roadmap is realistic, with clear phases, milestones, and timelines reflecting organizational capacity.
- [x] The governance and operating model is clearly defined, with roles and responsibilities assigned, including emerging roles such as AI Ethics Officer and Data Product Manager.
- [x] The strategy has been reviewed and approved by all key stakeholders, including the CDO, business leaders, and governance councils.
- [x] Compliance with relevant data privacy and AI regulations is explicitly addressed.
- [x] Integration points with MLOps, DataOps, and FinOps practices are identified.

### 5.2. Review Checklist

| Area | Question | Finding |
| :--- | :--- | :--- |
| **Strategic Alignment** | Does the strategy directly support the organization's strategic objectives and emerging data trends? | Yes |
| **Technical Feasibility** | Is the proposed architecture and technology stack technically sound, scalable, and aligned with cloud-native and data mesh principles? | Yes |
| **Business Value** | Does the strategy clearly articulate the expected business value, ROI, and risk mitigation? | Yes |
| **Governance and Compliance** | Are governance structures, roles, and compliance requirements adequately addressed? | Yes |
| **Completeness** | Does the strategy cover all key aspects, from vision to governance, including AI governance and emerging roles? | Yes |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Governance Charter | Provides the authority and framework for the DW BI Strategy. | `templates/templates-KA-01-data-governance.md` |
| Architecture Blueprint | Provides the technical standards and guidelines for the DW BI architecture. | `templates/templates-KA-02-data-architecture.md` |
| Data Quality Framework | Establishes standards and processes essential for BI success. | `templates/templates-KA-11-data-quality.md` |
| AI Governance Framework | Provides policies and controls for responsible AI use. | `templates/templates-KA-14-data-management-maturity.md` |

### 6.2. Consumers

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| DW Architecture | The detailed design of the data warehouse, based on the strategy. | `02-dw-architecture.md` |
| Dimensional Model Standards | The standards for designing dimensional models for the data warehouse. | `03-dimensional-model-standards.md` |
| BI Standards | The standards for developing and deploying BI reports and dashboards. | `04-bi-standards.md` |
| Data Product Catalog | Inventory of data products created and managed under the strategy. | `05-data-product-catalog.md` |
| AI/ML Model Registry | Catalog and governance of AI/ML models integrated with BI. | `06-ml-model-registry.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Warehousing** | Snowflake, Google BigQuery, Amazon Redshift | PostgreSQL, Greenplum |
| **ETL/ELT** | Fivetran, Matillion, Talend | dbt, Apache Airflow, Apache Spark |
| **Business Intelligence** | Tableau, Power BI, Looker | Metabase, Apache Superset, Redash |
| **Data Catalog** | Alation, Collibra, Atlan | Amundsen, DataHub |
| **Streaming and Integration** | Confluent Kafka, AWS Kinesis | Apache Kafka, Apache NiFi |
| **MLOps Platforms** | Databricks MLflow, Azure ML | Kubeflow, MLflow |
| **AI Governance** | IBM Watson OpenScale, Fiddler AI | Open-source explainability and monitoring tools |

### 7.2. Automation Opportunities

- **Automated Data Integration**: Use tools like Fivetran or Apache NiFi to automate extraction and loading of data from diverse sources into the data warehouse or lakehouse.
- **Automated Data Quality Testing**: Implement automated data quality tests embedded in pipelines using tools such as Great Expectations or dbt tests to ensure data accuracy and completeness.
- **Automated Reporting and Alerting**: Set up scheduled delivery of reports and dashboards, and create alerts to notify users of significant data changes or anomalies.
- **MLOps Automation**: Automate model training, deployment, monitoring, and retraining pipelines to ensure AI models remain accurate and compliant.
- **Governance Automation**: Leverage data catalog integrations and policy enforcement tools to automate metadata management, data lineage tracking, and compliance auditing.
- **FinOps Integration**: Use cloud cost monitoring tools to optimize data platform spending and resource utilization.

---

## 8. References

- DAMA-DMBOK2, Chapter 11: Data Warehousing and Business Intelligence  
- DAMA-DMBOK 3.0 (forthcoming, June 2025): Anticipated updates on data mesh, AI governance, and data product management  
- `reference/role-definitions.md`  
- `reference/metrics-kpis.md`  
- `reference/tools-landscape.md`  
- `knowledge-areas/KA-01-data-governance.md`  
- `knowledge-areas/KA-02-data-architecture.md`  
- `knowledge-areas/KA-08-data-warehousing-bi.md`  
- `knowledge-areas/KA-11-data-quality.md`  
- `knowledge-areas/KA-14-artificial-intelligence.md`  
- `guides/governance/ai-governance.md`


---

# DW Architecture


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Architecture Principles](#31-architecture-principles)
  - [3.2. Layered Architecture Diagram](#32-layered-architecture-diagram)
  - [3.3. Data Acquisition Layer](#33-data-acquisition-layer)
  - [3.4. Data Storage Layer](#34-data-storage-layer)
  - [3.5. Data Delivery Layer](#35-data-delivery-layer)
  - [3.6. Technology Stack](#36-technology-stack)
- [4. Example](#4-example)
  - [4.1. Architecture Principles](#41-architecture-principles)
  - [4.2. Layered Architecture Diagram](#42-layered-architecture-diagram)
  - [4.3. Data Acquisition Layer](#43-data-acquisition-layer)
  - [4.4. Data Storage Layer](#44-data-storage-layer)
  - [4.5. Data Delivery Layer](#45-data-delivery-layer)
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

The **DW Architecture** is a comprehensive blueprint that defines the structure, components, and standards for an organization's data warehousing and business intelligence (BI) environment. It is a strategic artifact that translates business requirements for analytics, reporting, and increasingly AI-enabled insights into a technical design. The architecture governs how data is acquired, integrated, stored, and delivered to end-users and AI/ML systems, ensuring scalability, performance, consistency, and governance.

> The purpose of the DW Architecture is to create a stable, scalable, and adaptable foundation for the enterprise's analytical and AI capabilities, ensuring that data is transformed into actionable insights in an efficient, reliable, and compliant manner.

In alignment with emerging trends, the DW Architecture also incorporates principles from modern paradigms such as Data Mesh and Data Fabric to support decentralized data ownership and seamless data interoperability across multi-cloud environments. It integrates AI governance considerations to ensure responsible use of data in AI/ML workflows, addressing compliance with regulations such as the EU AI Act alongside GDPR, HIPAA, and CCPA.

### 1.2. Scope

**Global** — This architecture applies to all data warehousing, business intelligence, and analytical AI initiatives across the organization. It provides a centralized set of standards, patterns, and governance mechanisms that all departmental or project-specific data marts, data products, and analytical solutions must adhere to, ensuring enterprise-wide consistency, interoperability, and compliance.

The scope includes:

- Traditional data warehousing components (ODS, EDW, data marts)
- Modern data platforms incorporating lakehouse architectures and data fabrics
- Integration with AI/ML pipelines and MLOps frameworks
- Support for agentic data stewardship roles and data contracts as first-class citizens

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-02: Data Architecture | The DW Architecture is a specialized domain within the broader Enterprise Data Architecture, inheriting its principles and standards, and extending them to analytical and AI use cases. |
| KA-03: Data Modeling and Design | The DW Architecture provides the context and standards for developing dimensional data models (star schemas, snowflake schemas), data vaults, and data products used in data marts and AI feature stores. |
| KA-06: Data Integration and Interoperability | The architecture defines the patterns and standards (e.g., ETL, ELT, streaming ingestion) for integrating data from various source systems into the data warehouse and data fabric layers. |
| KA-08: Data Warehousing and Business Intelligence | This deliverable is part of the KA-08 knowledge area, which covers the full lifecycle of DW and BI solutions. |
| KA-09: Artificial Intelligence and Machine Learning | The DW Architecture supports AI governance, data provisioning for ML models, and integration with MLOps pipelines. |
| KA-11: Data Quality | The DW Architecture incorporates processes and tools for ensuring data quality within the data warehouse and analytical pipelines, as its reliability is paramount for BI and AI. |
| KA-01: Data Governance | The architecture aligns with data governance frameworks, including emerging agentic stewardship models and data contracts to enforce data product SLAs and compliance. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately answerable for the definition, implementation, and maintenance of the DW Architecture, ensuring it meets business, AI governance, and compliance needs. |
| **R (Responsible)** | Data Warehouse Architect (DW Arch) | Responsible for designing, documenting, and evolving the DW Architecture, including selecting technologies, defining standards, and integrating AI governance requirements. |
| **S (Supportive)** | Data Architect (D-Arch), Data Engineer (D-Eng), MLOps Engineer | The Data Architect ensures alignment with the enterprise architecture. Data Engineers implement and operate the architecture. MLOps Engineers support AI/ML integration and automation. |
| **C (Consulted)** | Data Analytics Manager (DA Mgr), AI Ethics Officer | Provides input on business requirements, user needs, analytical use cases, and AI governance considerations to ensure the architecture is fit for purpose and compliant. |
| **I (Informed)** | Chief Data Officer (CDO), Chief AI Officer (CAIO) | Kept informed of the architecture's design and status as a key enabler of the organization's data and AI strategy. |

### 2.2. Section-Level RASCI

| Architecture Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Architectural Principles | DW Arch | D-Arch, DE Mgr, AI Ethics Officer | DE Mgr |
| Data Acquisition Layer | DW Arch | D-Eng, MLOps Engineer | DE Mgr |
| Data Storage Layer | DW Arch | D-Eng, Storage Admin, MLOps Engineer | DE Mgr |
| Data Delivery Layer | DW Arch | DA Mgr, BI Developer, AI Ethics Officer | DE Mgr |
| Technology Stack | DW Arch | D-Arch, IT Infrastructure, MLOps Engineer | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating a DW Architecture document. Replace all placeholders `[...]` with organization-specific information.*

### 3.1. Architecture Principles

> *Define the fundamental principles that guide all design decisions for the data warehouse. These principles should be aligned with the overall Enterprise Data Architecture principles and incorporate modern data management trends.*

1.  **[Principle 1: e.g., Single Source of Truth]**: [Description: e.g., The data warehouse will be the authoritative source for all enterprise-level reporting, analytics, and AI feature provisioning.]
2.  **[Principle 2: e.g., Scalability and Elasticity]**: [Description: e.g., The architecture must be able to scale compute and storage resources independently to meet fluctuating demands, leveraging cloud-native elasticity.]
3.  **[Principle 3: e.g., Data Quality by Design]**: [Description: e.g., Data quality checks and balances will be embedded into all data acquisition, transformation, and delivery processes, with automated testing and monitoring.]
4.  **[Principle 4: e.g., Separation of Concerns]**: [Description: e.g., The architecture will be layered to separate data acquisition, storage, and consumption, allowing for independent evolution of each layer and supporting multi-modal data access.]
5.  **[Principle 5: e.g., AI Governance and Compliance]**: [Description: e.g., The architecture will incorporate AI governance controls, ensuring data used in AI/ML workflows complies with ethical standards and regulatory requirements such as the EU AI Act.]
6.  **[Principle 6: e.g., Data Mesh and Fabric Integration]**: [Description: e.g., The architecture will support decentralized data ownership via Data Mesh principles, integrated with Data Fabric technologies for seamless data discovery and interoperability.]
7.  **[Principle 7: e.g., Data Products and Contracts]**: [Description: e.g., Data will be managed and delivered as products with clear SLAs, governed by data contracts to ensure quality, timeliness, and compliance.]
8.  **[Principle 8: e.g., Automation and MLOps Integration]**: [Description: e.g., The architecture will enable automation of data pipelines, transformations, and integration with MLOps workflows to accelerate AI/ML deployment.]

### 3.2. Layered Architecture Diagram

> *Provide a high-level diagram illustrating the different layers of the DW architecture (e.g., Data Sources, Staging Area, Integration Layer/ODS, Presentation Layer/Data Marts, BI & Analytics Tools, AI/ML Pipelines, Data Mesh Nodes, Data Fabric Layer).*

[Insert Architecture Diagram]

### 3.3. Data Acquisition Layer

> *Describe the methods, tools, and standards for acquiring data from source systems, including batch, streaming, and API-based ingestion.*

-   **Source Systems**: [List of key source systems, e.g., ERP, CRM, IoT devices, Web Analytics, external data feeds]
-   **Data Extraction Patterns**: [e.g., CDC (Change Data Capture), Batch File Extraction, API Polling, Event Streaming (Kafka, Kinesis)]
-   **Staging Area**: [Description of the staging area's purpose, structure, data retention policies, and support for raw and curated zones]
-   **ETL/ELT Standards**: [Reference to the `KA-06 05-etl-elt-standards.md` document, including guidelines for streaming and batch processing]
-   **AI Data Ingestion**: [Standards for ingesting data for AI/ML workflows, including feature store integration and data labeling pipelines]

### 3.4. Data Storage Layer

> *Describe the core data storage components of the architecture, including modern storage paradigms.*

-   **Operational Data Store (ODS)**: [Purpose, data model (e.g., 3NF), use cases for near-real-time operational reporting]
-   **Enterprise Data Warehouse (EDW)**: [Purpose, data model (e.g., Dimensional, Data Vault), subject areas covered, and support for historical and current data]
-   **Data Marts and Data Products**: [Strategy for data mart creation (e.g., dependent vs. independent), data product management, and integration with Data Mesh domains]
-   **Lakehouse and Data Fabric**: [Incorporation of lakehouse architectures combining data lakes and warehouses, and Data Fabric technologies for metadata-driven data integration]
-   **Storage Technology**: [e.g., Cloud Data Warehouse (Snowflake, BigQuery, Azure Synapse), On-Premise MPP Database (Teradata), Data Lake (Delta Lake, Apache Hudi)]

### 3.5. Data Delivery Layer

> *Describe how data is made available to end-users, applications, and AI systems.*

-   **BI & Reporting Tools**: [List of standardized BI tools, e.g., Tableau, Power BI, Looker]
-   **Semantic Layer**: [Description of the semantic layer (e.g., LookML, Power BI Datasets, dbt semantic models) to provide a business-friendly, governed view of the data]
-   **Data Access Methods**: [e.g., SQL Endpoints, APIs, Direct Query vs. Import, Data Virtualization]
-   **AI/ML Data Access**: [Mechanisms for provisioning data to AI/ML pipelines, feature stores, and model training environments]
-   **Performance & Caching**: [Strategies for ensuring query performance, e.g., materialized views, caching layers, query acceleration services]

### 3.6. Technology Stack

> *Provide a table summarizing the selected technologies for each component of the architecture, including AI/ML integration and governance tools.*

| Component | Technology | Vendor/Project | Rationale |
| :--- | :--- | :--- | :--- |
| Data Integration | [e.g., Apache Airflow, Fivetran] | [e.g., Open Source, Commercial] | [e.g., Flexible, scalable orchestration with support for batch and streaming] |
| Data Storage (EDW) | [e.g., Snowflake, Delta Lake] | [e.g., Snowflake Inc., Databricks] | [e.g., Cloud-native, scalable, supports lakehouse architecture] |
| BI Tool | [e.g., Tableau, Power BI] | [e.g., Salesforce, Microsoft] | [e.g., Strong visualization, user-friendly interface] |
| AI/ML Platform | [e.g., MLflow, Kubeflow] | [e.g., Open Source] | [e.g., Supports MLOps workflows and model lifecycle management] |
| Data Governance | [e.g., Collibra, Apache Atlas] | [e.g., Commercial, Open Source] | [e.g., Metadata management, data catalog, policy enforcement] |

---

## 4. Example

> *The following is a filled-in example for a fictional retail company, GlobalRetail Inc.*

### 4.1. Architecture Principles

1.  **Single Source of Truth**: The GlobalRetail DW will be the sole, authoritative source for all sales, inventory, and customer analytics across the enterprise.
2.  **Cloud-Native and Elastic**: The architecture will leverage cloud-native services to ensure scalability during peak shopping seasons and cost-efficiency during off-peak times.
3.  **Data Quality by Design**: Automated data quality checks for completeness, accuracy, and consistency will be integrated into every data pipeline using dbt tests.
4.  **Govern for Self-Service**: The architecture will empower business users with governed self-service analytics capabilities through a well-defined semantic layer.
5.  **AI Governance Compliance**: Data used in AI/ML workflows will comply with ethical standards and regulatory requirements, with audit trails and model explainability features.
6.  **Data Mesh Domains**: Data ownership is decentralized to business domains, with data products managed by domain teams and integrated via a Data Fabric layer.
7.  **Data Contracts**: SLAs and data quality expectations are formalized via data contracts between producers and consumers.
8.  **Automation and MLOps Integration**: Data pipelines and model training workflows are automated and orchestrated using Airflow and MLflow.

### 4.2. Layered Architecture Diagram

*(A diagram would be here showing data flowing from sources like SAP S/4HANA, Salesforce, Google Analytics, and IoT sensors, through Fivetran and Kafka for ingestion into a Snowflake staging area. dbt is used for transformation into the EDW and then into specific data marts and data products for Marketing and Sales. A Data Fabric layer enables cross-domain data discovery. Tableau and Power BI connect to these marts for reporting, while MLflow manages AI model lifecycle.)*

### 4.3. Data Acquisition Layer

-   **Source Systems**: SAP S/4HANA (Finance, Inventory), Salesforce (CRM), Google Analytics (Web Traffic), IoT sensors, Point-of-Sale (POS) systems.
-   **Data Extraction Patterns**: Fivetran connectors are used for CDC from SAP and Salesforce. Kafka streams ingest IoT sensor data in near real-time. Custom Python scripts extract data from POS system APIs nightly.
-   **Staging Area**: A dedicated 'STAGING' database in Snowflake, where raw data from Fivetran and Kafka lands. Data is kept for 7 days before being purged or archived.
-   **ETL/ELT Standards**: All transformations are performed in an ELT fashion using dbt Core, following the standards outlined in `KA-06 05-etl-elt-standards.md`. Streaming data is processed with Apache Spark Structured Streaming.
-   **AI Data Ingestion**: Feature engineering pipelines extract and curate data for ML models, with data labeling workflows integrated via custom tooling.

### 4.4. Data Storage Layer

-   **Enterprise Data Warehouse (EDW)**: A 'PRODUCTION' database in Snowflake containing a dimensionally modeled data warehouse based on the Kimball methodology. It integrates data from all source systems into conformed dimensions (e.g., Customer, Product, Date) and fact tables (e.g., Sales, Inventory Levels).
-   **Data Marts and Data Products**: Two primary dependent data marts are created: a `SALES_MART` for the sales team and a `MARKETING_MART` for the marketing team. These are composed of views on top of the EDW to prevent data duplication. Data products are managed by domain teams with defined SLAs.
-   **Lakehouse and Data Fabric**: Delta Lake is used to combine structured and unstructured data, enabling advanced analytics and AI use cases. A Data Fabric layer provides metadata-driven data discovery and governance.
-   **Storage Technology**: Snowflake Enterprise Edition on AWS, Delta Lake on Databricks.

### 4.5. Data Delivery Layer

-   **BI & Reporting Tools**: Tableau is the primary tool for executive dashboards and deep-dive analysis. Power BI is used by the finance team for operational reporting.
-   **Semantic Layer**: A dbt semantic layer is being developed to provide a consistent set of metrics and dimensions for all BI tools.
-   **Data Access Methods**: BI tools use dedicated Snowflake roles with read-only access to the data marts. Analysts with SQL skills can query the marts directly via the Snowflake UI. APIs expose data products for external applications.
-   **AI/ML Data Access**: Feature stores provision data to ML training pipelines managed by MLflow, with data versioning and lineage tracked.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Mesh Overview | Concept | [data-mesh.md](references/concepts-modern-paradigms.md) |
| AI Governance Framework | Guide | **ai-governance.md** |
| ETL and ELT Standards | Deliverable | [templates/templates-KA-06-data-integration-interoperability.md](templates/templates-KA-06-data-integration-interoperability.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The architecture has been approved by the Data Engineering Manager and the Data Architecture Review Board (DARB).
- [ ] The architecture clearly defines all layers from data acquisition to data delivery, including AI/ML integration.
- [ ] The technology stack has been vetted and approved, with consideration for cloud-native and multi-cloud deployments.
- [ ] The architecture aligns with the `01-dw-bi-strategy.md` and the organization's AI governance policies.
- [ ] The design addresses scalability, performance, security, and regulatory compliance requirements (e.g., GDPR, EU AI Act).
- [ ] Data contracts and data product management practices are defined and incorporated.
- [ ] The architecture supports automation and integration with MLOps and DataOps pipelines.

### 5.2. Review Checklist

| # | Review Question | Pass/Fail |
| :--- | :--- | :--- |
| 1 | Does the architecture support the key business intelligence, reporting, and AI use cases? | |
| 2 | Is the choice of data modeling methodology (e.g., Kimball, Inmon, Data Vault) justified and appropriate? | |
| 3 | Are the data integration patterns appropriate for the source systems and data velocity? | |
| 4 | Does the architecture include provisions for data quality management and monitoring? | |
| 5 | Is the architecture cost-effective and does it have a clear TCO analysis? | |
| 6 | Are AI governance and compliance requirements adequately addressed? | |
| 7 | Does the architecture support decentralized data ownership and data product management? | |
| 8 | Are automation and MLOps integration opportunities identified and planned? | |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship |
| :--- | :--- |
| [DW & BI Strategy](templates/templates-KA-08-data-warehousing-bi.md) | Provides the strategic goals and business requirements that this architecture must fulfill. |
| [Integration Architecture](templates/templates-KA-06-data-integration-interoperability.md) | Provides the enterprise-level patterns and standards for data integration that this architecture inherits. |
| [Data Governance Charter](templates/templates-KA-01-data-governance.md) | Establishes the authority, scope, and principles for data governance, which informs the DW architecture. |
| [Data Quality Framework](templates/templates-KA-11-data-quality.md) | Defines the standards and processes for data quality that must be implemented within the DW architecture. |
| **AI Governance Framework** | Provides policies and controls for responsible AI use, which the DW architecture must support. |

### 6.2. Consumers

| Output | Relationship |
| :--- | :--- |
| [Dimensional Model](templates/templates-KA-08-data-warehousing-bi.md) | The DW Architecture provides the framework and standards for creating specific dimensional models. |
| [Data Mart Design](templates/templates-KA-08-data-warehousing-bi.md) | The architecture governs the design and implementation of all data marts. |
| **MLOps Pipeline Design** | The DW Architecture supports data provisioning and integration with MLOps pipelines. |
| **Data Product Catalog** | The architecture supports the management and governance of data products cataloged here. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| Cloud Data Warehouse | Snowflake, Google BigQuery, Amazon Redshift, Azure Synapse | N/A (Managed Services) |
| Data Integration (ELT) | Fivetran, Matillion, Stitch | Airbyte, Meltano, Apache NiFi |
| Data Transformation | dbt Cloud | dbt Core |
| BI & Analytics | Tableau, Power BI, Looker | Apache Superset, Metabase |
| Streaming Data Platforms | Confluent Kafka, AWS Kinesis | Apache Kafka, Apache Pulsar |
| AI/ML Platforms | DataRobot, Azure ML, Google Vertex AI | MLflow, Kubeflow, Seldon Core |
| Data Governance & Catalog | Collibra, Alation | Apache Atlas, Amundsen |

### 7.2. Automation Opportunities

-   **Automated Ingestion**: Use tools like Fivetran or Airbyte to automate the extraction and loading of data from source systems into the data warehouse, reducing the need for custom pipelines.
-   **Streaming Data Pipelines**: Implement event-driven ingestion using Kafka or Pulsar to support real-time analytics and AI use cases.
-   **Automated Transformations & Testing**: Use dbt to schedule data transformation jobs and automatically run data quality tests on every run, ensuring data reliability.
-   **Infrastructure as Code (IaC)**: Manage the data warehouse, data lake, and BI tool configurations using Terraform or similar IaC tools to ensure consistency and repeatability.
-   **MLOps Integration**: Automate model training, validation, deployment, and monitoring workflows integrated with data pipelines using MLflow or Kubeflow.
-   **Data Contract Enforcement**: Use policy-as-code tools to enforce data contracts and SLA compliance automatically.
-   **Metadata and Lineage Automation**: Integrate metadata management tools to automatically capture data lineage and support impact analysis.

---

## 8. References

-   [1] DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 11: Data Warehousing and Business Intelligence)
-   [2] DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Community-driven update launching June 2025. [https://dama.org](https://dama.org)
-   [3] [Internal] [DW & BI Strategy](templates/templates-KA-08-data-warehousing-bi.md)
-   [4] [Internal] [Integration Architecture](templates/templates-KA-06-data-integration-interoperability.md)
-   [5] [Internal] **AI Governance Framework**
-   [6] European Commission. *EU AI Act Proposal*, 2021. [https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence)


---

# Dimensional Model Standards


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Naming Conventions](#31-naming-conventions)
  - [3.2. Dimension Table Standards](#32-dimension-table-standards)
  - [3.3. Fact Table Standards](#33-fact-table-standards)
  - [3.4. Surrogate Key Usage](#34-surrogate-key-usage)
- [4. Example](#4-example)
  - [4.1. Example Naming Conventions](#41-example-naming-conventions)
  - [4.2. Example Dimension: `dim_customer`](#42-example-dimension-dim_customer)
  - [4.3. Example Fact Table: `fact_sales`](#43-example-fact-table-fact_sales)
  - [4.4. Related Concepts and Guides](#44-related-concepts-and-guides)
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

**Dimensional Model Standards** are a comprehensive set of formal guidelines and best practices for designing, developing, and maintaining dimensional data models within the organization. These standards ensure that data warehouses, data lakes, lakehouses, and business intelligence (BI) systems are built consistently, are easy to understand, scalable, and perform efficiently. A dimensional model, typically structured as a star or snowflake schema, organizes data to optimize user-friendly, high-performance querying and analytical processing.

> The primary purpose of these standards is to create a unified and predictable approach to dimensional modeling, which reduces development time, improves data quality, and enhances the usability and trustworthiness of BI and analytics solutions. These standards also facilitate compliance with evolving regulatory requirements such as GDPR, HIPAA, CCPA, and emerging AI governance frameworks, ensuring that analytical data assets are governed responsibly.

As organizations increasingly adopt modern data architectures such as Data Mesh and Data Fabric, dimensional models remain a critical component of the analytical layer, serving as curated data products that enable self-service analytics and AI/ML workloads. These standards are designed to be adaptable to cloud-native environments, multi-cloud deployments, and hybrid architectures.

### 1.2. Scope

**Global** — These standards apply to all data warehousing, data mart, and BI projects across the entire organization, including cloud-based and hybrid implementations. They are mandatory guidelines for any new dimensional model development and serve as a benchmark for continuous improvement of existing models.

The standards encompass design principles, naming conventions, key management, historical data handling, and integration with operational and analytical data products. They also support emerging roles such as Data Product Managers and AI Ethics Officers by embedding governance and stewardship considerations into the model design.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-03: Data Modeling and Design | These standards are a specialized extension of the general data modeling standards, focusing specifically on the unique requirements of analytical and dimensional data models. They incorporate advanced modeling techniques and address integration with data mesh and fabric architectures. |
| KA-02: Data Architecture | The dimensional models must align with the overall enterprise data architecture, including cloud and hybrid environments, ensuring that the BI layer fits coherently into the broader data landscape and supports data productization. |
| KA-01: Data Governance | The standards support data governance by defining clear rules for the structure, quality, lineage, and stewardship of analytical data, and by assigning responsibilities for the creation and maintenance of these models. They also address compliance with AI governance frameworks and data privacy regulations. |
| KA-11: Data Quality | Adherence to these standards is a key factor in ensuring the quality, consistency, and trustworthiness of data presented to business users and downstream AI/ML models. |
| KA-08: Data Warehousing and Business Intelligence | These standards are foundational for the design and implementation of data warehousing and BI solutions, supporting the delivery of reliable, performant, and governed analytical data assets. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately accountable for the creation, enforcement, and continuous improvement of the dimensional model standards, ensuring alignment with enterprise data strategy and governance. |
| **R (Responsible)** | Data Warehouse Architect (DW Arch) | Responsible for drafting, defining, updating, and communicating the technical details of the standards, incorporating feedback from stakeholders and emerging best practices. |
| **S (Supportive)** | Data Modeler (D-Modeler) | Supports the DW Architect in developing and documenting the standards, applies the standards in model development, and provides practical insights from implementation experience. |
| **C (Consulted)** | Data Analytics Manager (DA Mgr), Business Intelligence Manager (BI Mgr), Data Product Manager | Consulted to ensure the standards meet the analytical, reporting, and data product needs of the business and align with AI governance and compliance requirements. |
| **I (Informed)** | Data Engineer (D-Eng), MLOps Engineer, AI Ethics Officer | Informed of the standards to ensure that ETL/ELT processes, AI/ML pipelines, and governance controls are designed to correctly populate and manage the dimensional models. |

### 2.2. Section-Level RASCI

| Standard Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Naming Conventions | DW Arch | D-Modeler, DA Mgr | DE Mgr |
| Dimension Table Standards | DW Arch | D-Modeler, Data Product Manager | DE Mgr |
| Fact Table Standards | DW Arch | D-Modeler, BI Mgr | DE Mgr |
| Surrogate Key Usage | DW Arch | D-Modeler, D-Eng | DE Mgr |
| Example and Template | D-Modeler | DW Arch, BI Mgr | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Dimensional Model Standards document. Replace all placeholders `[...]` with organization-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Naming Conventions

> *Clear and consistent naming conventions are critical for the usability, maintainability, and automation of dimensional models. Define the standard prefixes, suffixes, casing, and patterns for all database objects, considering cloud and multi-platform compatibility.*

**Input needed**: Existing organizational naming conventions, `KA-03 02-naming-conventions.md`.  
**Who fills this**: DW Arch.

| Object Type | Format | Example |
| :--- | :--- | :--- |
| Dimension Table | `dim_[BusinessName]` | `dim_customer` |
| Fact Table | `fact_[BusinessProcess]` | `fact_sales` |
| Surrogate Key (PK) | `[TableName]_key` | `customer_key` |
| Business Key (BK) | `[TableName]_bk` | `customer_bk` |
| Degenerate Dimension | `[DimensionName]_dd` | `order_number_dd` |
| Junk Dimension | `junk_[AttributeGroup]` | `junk_order_flags` |
| View | `v_[Purpose]` | `v_monthly_sales_summary` |

> *Note*: Naming conventions should consider integration with data catalogs and metadata management tools to support discoverability and lineage tracking.

### 3.2. Dimension Table Standards

> *Define the structure, characteristics, and lifecycle management of dimension tables. This includes standards for handling historical data (Slowly Changing Dimensions), hierarchies, conformed dimensions, and common attributes.*

**Input needed**: Business requirements for historical tracking, `KA-03 01-modeling-standards.md`.  
**Who fills this**: DW Arch, D-Modeler.

#### 3.2.1. Slowly Changing Dimensions (SCD)

*   **SCD Type 1**: Overwrite history. Use for attributes where historical changes are not relevant (e.g., correcting a typo in a name). Suitable for non-analytical attributes.
*   **SCD Type 2**: Create a new row for each change. This is the default for most attributes. Requires `row_start_date`, `row_end_date`, and `is_current_flag` columns to track historical versions and enable point-in-time analysis.
*   **SCD Type 3**: Add a new column for the previous value. Use sparingly for specific analytical requirements where limited historical context is sufficient.
*   **Hybrid Approaches**: Consider hybrid SCD implementations or temporal tables where supported by the database platform for enhanced historical tracking and auditability.

#### 3.2.2. Standard Dimension Columns

All dimension tables must include the following columns to ensure consistency, traceability, and support for historical tracking:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `[dim_name]_key` | INTEGER | Surrogate key, primary key of the dimension. Should be a meaningless, system-generated identifier. |
| `[dim_name]_bk` | VARCHAR(255) | Business key from the source system, used for traceability and reconciliation. |
| `row_start_date` | DATETIME | The date/time this version of the record became effective (for SCD2). |
| `row_end_date` | DATETIME | The date/time this version of the record expired (for SCD2). |
| `is_current_flag` | CHAR(1) | 'Y' or 'N' to indicate the current version of the record (for SCD2). |
| `source_system` | VARCHAR(50) | The name or code of the source system from which the record originated. |
| `load_timestamp` | DATETIME | The timestamp when the record was loaded into the data warehouse or data lake. |
| `record_hash` | VARCHAR(64) | Optional: Hash of the record contents to detect changes efficiently. |
| `data_contract_id` | VARCHAR(50) | Optional: Identifier linking to the data contract governing this data product. |

> *Note*: Inclusion of audit and metadata columns supports compliance with data governance, AI governance, and regulatory requirements.

### 3.3. Fact Table Standards

> *Define the structure and characteristics of fact tables, including standards for granularity, types of fact tables, degenerate dimensions, and integration with data products and AI/ML pipelines.*

**Input needed**: Business process documentation, analytical requirements.  
**Who fills this**: DW Arch, D-Modeler.

#### 3.3.1. Granularity

The grain of each fact table must be explicitly declared in its description. For example, "One row per sales order line item" or "One row per customer per day". Clear grain definitions enable accurate aggregation and prevent data duplication.

#### 3.3.2. Fact Table Types

*   **Transactional**: One row per transaction event. This is the most common type, capturing detailed event-level data.
*   **Periodic Snapshot**: One row per subject per time period (e.g., monthly account balances), capturing state at regular intervals.
*   **Accumulating Snapshot**: One row per process instance, updated as the process moves through its lifecycle (e.g., order fulfillment stages).
*   **Factless Fact Tables**: Capture events or conditions without numeric measures, useful for tracking occurrences or coverage.

#### 3.3.3. Degenerate Dimensions and Junk Dimensions

*   **Degenerate Dimensions**: Store identifiers or attributes that do not warrant a separate dimension table but are useful for filtering or grouping (e.g., order numbers).
*   **Junk Dimensions**: Group miscellaneous low-cardinality flags or indicators into a single dimension to reduce clutter and improve query performance.

### 3.4. Surrogate Key Usage

> *Define the policy for surrogate key usage. Surrogate keys are essential for decoupling the data warehouse from operational source systems and for correctly handling historical data.*

**Input needed**: `KA-03 01-modeling-standards.md`.  
**Who fills this**: DW Arch.

*   All dimension tables MUST use a meaningless integer surrogate key as the primary key to ensure uniqueness and independence from source system keys.
*   All foreign keys in fact tables MUST be surrogate keys referencing the corresponding dimension tables to maintain referential integrity.
*   The business key from the source system MUST be retained in the dimension table for traceability, reconciliation, and data contract enforcement.
*   Surrogate keys should be generated using sequences, identity columns, or UUIDs depending on platform capabilities and performance considerations.
*   Surrogate key management must support data mesh principles by enabling clear ownership and stewardship boundaries.

---

## 4. Example

> *This section provides a realistic example of applying the dimensional model standards to a fictional company, GlobalRetail Inc., for their Sales data mart.*

### 4.1. Example Naming Conventions

| Object Type | Example |
| :--- | :--- |
| Dimension Table | `dim_product` |
| Fact Table | `fact_sales` |
| Surrogate Key (PK) | `product_key` |
| Business Key (BK) | `product_bk` |
| Degenerate Dimension | `order_number_dd` |
| Junk Dimension | `junk_order_flags` |

### 4.2. Example Dimension: `dim_customer`

This dimension stores customer information. It is an SCD Type 2 dimension to track changes in customer attributes over time.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `customer_key` | INTEGER | Surrogate key, primary key. |
| `customer_bk` | VARCHAR(50) | Customer ID from the CRM system. |
| `customer_name` | VARCHAR(255) | Full name of the customer. |
| `customer_address` | VARCHAR(500) | Mailing address of the customer. |
| `customer_city` | VARCHAR(100) | City of the customer. |
| `customer_state` | VARCHAR(50) | State of the customer. |
| `customer_zip` | VARCHAR(20) | ZIP code of the customer. |
| `row_start_date` | DATETIME | Effective date of this customer record. |
| `row_end_date` | DATETIME | Expiration date of this customer record. |
| `is_current_flag` | CHAR(1) | 'Y' for the current record, 'N' for historical. |
| `source_system` | VARCHAR(50) | e.g., 'Salesforce CRM' |
| `load_timestamp` | DATETIME | Timestamp of the ETL load. |
| `record_hash` | VARCHAR(64) | SHA-256 hash of the record for change detection. |
| `data_contract_id` | VARCHAR(50) | 'DC-CRM-001' |

### 4.3. Example Fact Table: `fact_sales`

This fact table stores sales transaction data at the grain of one row per sales order line item.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `date_key` | INTEGER | FK to `dim_date`. |
| `customer_key` | INTEGER | FK to `dim_customer`. |
| `product_key` | INTEGER | FK to `dim_product`. |
| `store_key` | INTEGER | FK to `dim_store`. |
| `order_number_dd` | VARCHAR(50) | Degenerate dimension for the sales order number. |
| `sales_amount` | DECIMAL(18,2) | The total amount for the line item. |
| `quantity_sold` | INTEGER | The number of units sold. |
| `unit_price` | DECIMAL(18,2) | The price per unit. |
| `discount_amount` | DECIMAL(18,2) | The discount applied to the line item. |
| `load_timestamp` | DATETIME | Timestamp of the ETL load. |

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics KPIs | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Modeling and Design | Knowledge Area | **KA-03-data-modeling-and-design.md** |
| Data Governance | Knowledge Area | **KA-01-data-governance.md** |
| Data Quality | Knowledge Area | **KA-11-data-quality.md** |
| Dimensional Data Model | Deliverable | **10-dimensional-data-model.md** |
| Data Warehouse and BI Strategy | Deliverable | [01-dw-bi-strategy.md](./01-dw-bi-strategy.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] All tables, columns, and keys follow the defined naming conventions.
- [x] All dimension tables have a surrogate primary key.
- [x] All fact tables have foreign keys that reference dimension surrogate keys.
- [x] The grain of every fact table is clearly defined and documented.
- [x] SCD Type 2 dimensions have the required columns (`row_start_date`, `row_end_date`, `is_current_flag`).
- [x] Data contracts and lineage metadata are documented and linked to dimensional models.
- [x] The model supports compliance with relevant data privacy and AI governance regulations.
- [x] The model has been reviewed and approved by the DW Architect and Data Governance team.
- [x] The model supports integration with AI/ML pipelines and data product frameworks.

### 5.2. Review Checklist

| Criteria | Expected Outcome |
| :--- | :--- |
| **Understandability** | A business analyst with no prior knowledge of the model can understand the relationships between facts and dimensions, supported by clear documentation. |
| **Performance** | Queries for common analytical scenarios execute within acceptable timeframes, leveraging indexing and partitioning strategies. |
| **Scalability** | The model can accommodate future growth in data volume, velocity, and variety, including support for multi-cloud and hybrid environments. |
| **Extensibility** | The model can be extended to include new business processes and data products with minimal impact on existing structures. |
| **Compliance** | The model fully complies with all standards defined in this document, including data governance, privacy, and AI governance requirements. |
| **Automation** | The model supports automated validation, documentation generation, and integration with CI/CD pipelines for data engineering. |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| DW/BI Strategy | Provides the business context and priorities that the dimensional model must support. | `./01-dw-bi-strategy.md` |
| Modeling Standards | Provides the general modeling guidelines that these dimensional standards extend. | `templates/templates-KA-03-data-modeling-design.md` |
| Data Governance Framework | Defines governance policies and roles that impact dimensional model stewardship. | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Dimensional Data Model | This is the actual implementation of a dimensional model, which must adhere to these standards. | `templates/templates-KA-03-data-modeling-design.md` |
| Dimensional Model | A specific instance of a dimensional model for a particular data mart or data product. | `./05-dimensional-model.md` |
| Data Quality Scorecard | Measures the quality of data within the data warehouse, which is often built on dimensional models. | `templates/templates-KA-11-data-quality.md` |
| Data Governance Report | Reports on the governance of data assets, including those in the data warehouse. | `templates/templates-KA-01-data-governance.md` |
| AI Governance Report | Reports on compliance with AI governance policies related to data used in AI/ML models. | `templates/templates-KA-01-data-governance.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Modeling** | erwin Data Modeler, SAP PowerDesigner, ER/Studio | dbt (Data Build Tool), Vertabelo, OpenModelSphere |
| **ETL/ELT** | Informatica PowerCenter, Talend, Microsoft SSIS | Apache Airflow, Pentaho, dbt |
| **BI & Analytics** | Tableau, Power BI, Qlik Sense | Apache Superset, Metabase |
| **Data Catalog & Lineage** | Collibra, Alation, Informatica EDC | Amundsen, DataHub |
| **DataOps & MLOps** | DataKitchen, Domino Data Lab, MLflow | Kubeflow, MLflow, Airflow |

### 7.2. Automation Opportunities

*   **Model Generation**: Use metadata from source systems and data contracts to automatically generate initial drafts of dimensional models, accelerating development and ensuring compliance.
*   **Code Generation**: Automatically generate the DDL (Data Definition Language) scripts for creating dimensional model tables from the design artifacts.
*   **Validation**: Develop automated scripts and tools to validate that a given dimensional model complies with these standards (e.g., surrogate keys, naming conventions, presence of SCD columns, data contract adherence).
*   **Documentation**: Automatically generate data dictionaries, lineage diagrams, and other documentation from the model metadata to support transparency and governance.
*   **Monitoring**: Integrate with data quality and governance platforms to monitor dimensional model health, data freshness, and compliance in real-time.
*   **Integration with AI Pipelines**: Automate the provisioning of dimensional data products for AI/ML workflows, ensuring data governance and lineage are maintained.

---

## 8. References

1.  DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Chapter 11, "Data Warehousing and Business Intelligence".
2.  DAMA International. *DAMA-DMBOK 3.0* (forthcoming, June 2025). Expected to provide updated guidance on modern data architectures, AI governance, and data product management.
3.  DAMA Research Skill. `role-definitions.md`. Internal reference for role descriptions.
4.  DAMA Research Skill. `templates/templates-KA-03-data-modeling-design.md`. Internal reference for general modeling standards.
5.  European Commission. *EU AI Act* (2024). Regulatory framework impacting AI governance and data management practices.
6.  Data Mesh Principles. Zhamak Dehghani, ThoughtWorks. Foundational concepts for decentralized data ownership and product thinking.
7.  Data Fabric Architecture. Gartner Research. Guidance on integrated data management across hybrid and multi-cloud environments.


---

# BI Standards


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Data Visualization Standards](#31-data-visualization-standards)
  - [3.2. Reporting Standards](#32-reporting-standards)
  - [3.3. Dashboard Design Principles](#33-dashboard-design-principles)
  - [3.4. Calculation and Metric Definition Standards](#34-calculation-and-metric-definition-standards)
- [4. Example](#4-example)
  - [4.1. Data Visualization Standards](#41-data-visualization-standards)
  - [4.2. Reporting Standards](#42-reporting-standards)
  - [4.3. Dashboard Design Principles](#43-dashboard-design-principles)
  - [4.4. Related Concepts and Guides](#44-related-concepts-and-guides)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Inputs for This Output (Prerequisites)](#61-inputs-for-this-output-prerequisites)
  - [6.2. Outputs That Use This as Input](#62-outputs-that-use-this-as-input)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

**BI Standards** are a comprehensive set of guidelines, best practices, and governance principles that direct the development, deployment, and ongoing maintenance of Business Intelligence (BI) solutions. These standards ensure that all reports, dashboards, and analytics outputs are consistent, accurate, accessible, and aligned with strategic business objectives. They provide a unified framework for BI developers, data visualization specialists, data scientists, and business users, fostering a shared understanding of data presentation, interpretation, and trustworthiness.

> The purpose of BI Standards is to establish a consistent, scalable, and high-quality approach to BI development, ensuring that all BI solutions are reliable, user-centric, and provide a single source of truth to empower data-driven decision-making.

In the evolving landscape of data management, BI Standards play a pivotal role in supporting digital transformation initiatives by enabling a data-driven culture. They facilitate collaboration across diverse teams and ensure that BI solutions are not only technically robust but also ethically sound and compliant with emerging regulations such as the EU AI Act, GDPR, HIPAA, and CCPA. Furthermore, modern BI standards must incorporate considerations for AI governance, cloud-native architectures, and the integration of data mesh and data fabric paradigms to support agility and scalability.

> "Our ability to make timely and informed decisions is directly linked to the quality, consistency, and governance of our BI solutions. These standards are not just about making our reports look polished; they are about building trust in our data and empowering our people to make better decisions, faster." - *Fictional CEO, GlobalRetail Inc.*

Looking ahead, the forthcoming DAMA-DMBOK 3.0 (expected June 2025) emphasizes the integration of BI standards within broader data product management and AI governance frameworks, highlighting the importance of agentic data stewardship and the elevation of data contracts as foundational elements.

### 1.2. Scope

**Global** — These BI Standards apply universally to all Business Intelligence and analytics activities across the entire organization. They encompass all business units, departments, and data products, ensuring a consistent and seamless BI experience for all users. This includes BI solutions developed on corporate BI platforms (e.g., Tableau, Power BI, Qlik Sense), cloud-native BI tools, as well as departmental or ad-hoc reporting efforts.

The standards are mandatory for all BI developers, data analysts, data scientists, data engineers, and business users who create, manage, or consume BI content. They also extend to roles newly emerging in the BI ecosystem, such as Data Product Managers, MLOps Engineers, and AI Ethics Officers, reflecting the integration of BI with AI and machine learning operations.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | BI Standards are a critical component of the overall data governance framework, ensuring BI solutions comply with data policies, ethical use, and regulatory requirements. The Data Governance Council oversees the implementation and enforcement of these standards, including AI governance considerations. |
| KA-11: Data Quality | BI Standards depend on high-quality data to deliver trustworthy insights. They incorporate guidelines for data validation, error handling, and anomaly detection, working in tandem with the Data Quality Framework to ensure data fitness for purpose. |
| KA-09: Metadata Management | BI Standards leverage metadata extensively to provide context, lineage, and clarity. They include protocols for documenting data sources, business definitions, and transformation logic within the corporate data catalog, enhancing transparency and user trust. |
| KA-05: Data Security | BI Standards enforce role-based access control, data masking, and encryption to protect sensitive information within BI solutions, ensuring compliance with privacy regulations and internal security policies. |
| KA-02: Data Architecture | BI Standards align with enterprise data architecture principles, supporting modern architectures such as data mesh and data fabric. They guide the use of approved data sources, cloud-native BI platforms, and integration patterns consistent with the enterprise data model. |
| KA-12: Artificial Intelligence and Machine Learning | BI Standards increasingly intersect with AI governance and MLOps practices, ensuring that BI outputs incorporating AI-driven insights adhere to ethical standards, transparency, and explainability requirements. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Analytics Manager (DA Mgr) | Ultimately accountable for the creation, approval, and ongoing maintenance of the BI Standards. Ensures alignment with enterprise data and analytics strategy, including AI governance and compliance mandates. |
| **R (Responsible)** | BI Manager (BI Mgr) | Responsible for drafting, implementing, and enforcing the BI Standards. Manages day-to-day application and continuous improvement of standards, incorporating feedback and emerging best practices. |
| **S (Supportive)** | BI Developer (BI Dev), Data Visualization Specialist (DataViz), Data Product Manager | Support the implementation of BI Standards by adhering to them in their work, providing practical feedback, and championing adoption across teams. Data Product Managers help integrate BI standards into data product lifecycles. |
| **C (Consulted)** | Data Governance Manager (DG Mgr), AI Ethics Officer | Consulted to ensure BI Standards align with data governance frameworks, AI ethics, data quality, metadata management, and regulatory compliance. Provide expert input on emerging risks and controls. |
| **I (Informed)** | Business Users, Data Stewards | Informed about BI Standards to understand how to interpret and use BI solutions effectively. Their feedback is critical for continuous improvement and user adoption. |

### 2.2. Section-Level RASCI

| BI Standards Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Data Visualization Standards | DataViz | BI Dev, BI Mgr | DA Mgr |
| Reporting Standards | BI Dev | DataViz, BI Mgr | DA Mgr |
| Dashboard Design Principles | DataViz | BI Dev, BI Mgr | DA Mgr |
| Calculation and Metric Definition Standards | BI Mgr | DA Mgr, DG Mgr, AI Ethics Officer | DA Mgr |

---

## 3. Template

> *The following is the standardized template for creating BI Standards. Replace all placeholders `[...]` with organization-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Data Visualization Standards

> *This section defines the standards for creating clear, consistent, and effective data visualizations that support accurate interpretation and decision-making.*

#### 3.1.1. Chart Types

> *Specify the appropriate use of different chart types to ensure data is presented effectively and intuitively.*

- **Bar Charts**: [For comparing discrete values across categories; suitable for nominal or ordinal data.]
- **Line Charts**: [For illustrating trends and changes over time; ideal for continuous data.]
- **Pie Charts**: [For showing parts of a whole; use sparingly and only with up to 5 slices to avoid misinterpretation.]
- **Scatter Plots**: [For exploring relationships and correlations between two quantitative variables.]
- **Heat Maps**: [For visualizing data density or intensity across two dimensions.]
- **Tree Maps**: [For displaying hierarchical data and relative proportions within categories.]
- **Box Plots**: [For showing data distribution, variability, and outliers.]
- **Geospatial Maps**: [For visualizing location-based data; ensure appropriate map projections and scales.]

#### 3.1.2. Color Palette

> *Define the standard color palette to be used in all data visualizations to ensure brand consistency, accessibility, and effective communication.*

- **Primary Colors**: [List of primary brand colors with HEX/RGB codes]
- **Secondary Colors**: [Complementary colors for supporting elements]
- **Accent Colors**: [Colors used to highlight key data points or alerts]
- **Accessibility Guidelines**: [Ensure color choices meet WCAG 2.1 AA standards for contrast. Avoid relying solely on color to convey information; use patterns or labels as needed. Use color blindness simulators to validate palettes.]

#### 3.1.3. Chart Annotations

> *Provide guidelines for using annotations to highlight key insights and provide context.*

- **Data Labels**: [Display values on charts when it enhances readability; avoid clutter.]
- **Tooltips**: [Provide additional contextual information on hover or tap.]
- **Reference Lines**: [Use to indicate targets, thresholds, averages, or benchmarks.]
- **Annotations**: [Use sparingly to explain anomalies or important trends.]
- **Legends**: [Place consistently and ensure clarity; avoid redundancy.]

### 3.2. Reporting Standards

> *This section defines the standards for creating consistent, professional, and compliant reports.*

#### 3.2.1. Report Layout

> *Specify the standard layout for all reports, including headers, footers, and branding elements.*

- **Header**: [Include organization logo, report title, date/time of generation, and version number.]
- **Footer**: [Include page numbers, confidentiality notices, data source references, and contact information for report owner.]
- **Margins and Spacing**: [Define consistent margins and spacing for readability.]
- **Font Standards**: [Specify font types, sizes, and styles consistent with corporate branding.]

#### 3.2.2. Report Elements

> *Define standard elements to be included in all reports to ensure clarity and professionalism.*

- **Titles**: [Clear, concise, and descriptive; reflect report content accurately.]
- **Subtitles**: [Provide additional context such as reporting period or data scope.]
- **Data Labels**: [Include units and formatting consistent with metric definitions.]
- **Summary Sections**: [Include executive summaries or key insights where appropriate.]
- **Disclaimers**: [Include data limitations, assumptions, or caveats.]

#### 3.2.3. Report Naming Conventions

> *Establish a consistent naming convention for all reports to facilitate easy identification and retrieval.*

- **Format**: `[Business Unit]_[Report Name]_[Version]_[Date]`
- **Example**: `Sales_Monthly_Sales_Report_v1.2_20240430`
- **Version Control**: [Maintain version history and archive superseded reports.]

### 3.3. Dashboard Design Principles

> *This section outlines principles for designing user-friendly, performant, and insightful dashboards.*

- **Usability**: [Dashboards should be intuitive, with clear navigation and consistent layout. Use familiar UI patterns and provide user guidance.]
- **Interactivity**: [Enable filtering, drill-down, and exploration features. Clearly label interactive elements and provide instructions.]
- **Performance**: [Optimize data queries and caching to ensure dashboards load within acceptable timeframes (e.g., <5 seconds). Monitor and tune regularly.]
- **Layout and Composition**: [Use grid-based layouts for alignment. Group related metrics and visualizations logically. Prioritize key information above the fold.]
- **Color Theory in Dashboards**: [Use color strategically to highlight important metrics and create visual hierarchy. Avoid overuse of bright colors to reduce cognitive load.]
- **Mobile Responsiveness**: [Design dashboards to be accessible and usable on various devices, including tablets and smartphones.]
- **Accessibility**: [Ensure compliance with accessibility standards (e.g., keyboard navigation, screen reader support).]

### 3.4. Calculation and Metric Definition Standards

> *This section provides guidelines for defining, documenting, and managing calculations and metrics to ensure consistency, accuracy, and transparency.*

- **Metric Naming Conventions**: [Use standardized, descriptive names including units where applicable, e.g., `Total Sales (USD)`, `Customer Churn Rate (%)`.]
- **Calculation Logic**: [Document formulas, aggregation methods, filters applied, and assumptions. Use clear, unambiguous language.]
- **Data Sources**: [Specify source systems, tables, and columns used for each metric. Include versioning or snapshot details if applicable.]
- **Metric Lifecycle Management**: [Define processes for proposing, reviewing, approving, updating, and retiring metrics. Maintain a centralized metric catalog.]
- **Data Contracts**: [Where applicable, define data contracts specifying SLAs, data quality expectations, and ownership for metric data sources.]
- **Governance and Compliance**: [Ensure metrics comply with regulatory requirements and ethical guidelines, especially for AI-driven or predictive metrics.]

---

## 4. Example

> *The following is a filled-in example for a fictional company, GlobalRetail Inc.*

### 4.1. Data Visualization Standards

#### 4.1.1. Chart Types

- **Bar Charts**: Used for comparing sales across different product categories.
- **Line Charts**: Used for showing monthly sales trends over the past year.
- **Pie Charts**: Used for showing the percentage of sales by region (max 5 slices).
- **Scatter Plots**: Used for analyzing the relationship between advertising spend and sales revenue.
- **Heat Maps**: Used to visualize customer density by geographic region.
- **Tree Maps**: Used to display product category hierarchy and relative sales volumes.

#### 4.1.2. Color Palette

- **Primary Colors**: #005f73, #0a9396
- **Secondary Colors**: #94d2bd, #e9d8a6
- **Accent Colors**: #ee9b00, #ca6702
- **Accessibility**: All colors have been tested for color blindness accessibility and meet WCAG 2.1 AA contrast standards.

### 4.2. Reporting Standards

#### 4.2.1. Report Layout

- **Header**: GlobalRetail Inc. logo, "Monthly Sales Report", last refresh date.
- **Footer**: Page X of Y, "Confidential and Proprietary", data source references.

#### 4.2.2. Report Elements

- **Titles**: "Monthly Sales Report - April 2024"
- **Subtitles**: "Sales performance across all regions and product categories."
- **Data Labels**: Values formatted as currency with thousands separators.

#### 4.2.3. Report Naming Convention

- **Example**: `Sales_Monthly_Sales_Report_v1.2_20240430`

### 4.3. Dashboard Design Principles

- **Usability**: All dashboards include a "Help" button linking to the data dictionary and user guide.
- **Interactivity**: Users can filter by date, region, and product category; drill down into sales by store.
- **Performance**: Dashboards load within 5 seconds on average; optimized queries and caching implemented.
- **Mobile Responsiveness**: Dashboards are tested and optimized for tablet and smartphone use.
- **Accessibility**: Keyboard navigation and screen reader support enabled.

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Governance Framework | Knowledge Area | [KA-01-data-governance.md](knowledge-areas/KA-01-data-governance.md) |
| Data Quality Framework | Knowledge Area | [KA-11-data-quality.md](knowledge-areas/KA-11-data-quality.md) |
| AI Governance Guide | Guide | **guides/governance/ai-governance.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The BI Standards have been reviewed and approved by the Data Analytics Manager.
- [x] The BI Standards align with the overall data governance and AI governance frameworks.
- [x] The BI Standards are published and accessible to all BI developers, data scientists, and business users via the company intranet or data portal.
- [x] A comprehensive training program and supporting materials have been developed to educate BI developers and business users on the standards.
- [x] The BI Standards incorporate compliance requirements for relevant regulations (e.g., GDPR, HIPAA, EU AI Act).
- [x] The BI Standards support modern data architectures including data mesh and cloud-native BI platforms.

### 5.2. Review Checklist

| # | Review Question | Pass/Fail |
| :--- | :--- | :--- |
| 1 | Are the BI Standards clear, concise, and easy to understand? | Pass |
| 2 | Do the BI Standards cover all relevant aspects of BI development, including visualization, reporting, dashboard design, and metric definitions? | Pass |
| 3 | Are the BI Standards aligned with industry best practices and emerging trends (e.g., AI governance, data mesh)? | Pass |
| 4 | Do the standards address mobile BI and accessibility requirements? | Pass |
| 5 | Are the standards scalable and adaptable for future growth and technological changes? | Pass |
| 6 | Do the standards include guidance on compliance with data privacy and AI regulations? | Pass |
| 7 | Are roles and responsibilities clearly defined and assigned? | Pass |

---

## 6. Related Outputs

### 6.1. Inputs for This Output (Prerequisites)

| Source Output | KA | Relationship | File Path |
| :--- | :--- | :--- | :--- |
| DW-BI Strategy | KA-08 | Provides the strategic context and objectives for the BI Standards. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Data Governance Policy | KA-01 | Provides overarching data governance policies that BI Standards must adhere to. | `templates/templates-KA-01-data-governance.md` |
| Data Quality Framework | KA-11 | Provides data quality standards and processes that support BI accuracy. | `templates/templates-KA-11-data-quality.md` |

### 6.2. Outputs That Use This as Input

| Target Output | KA | Relationship | File Path |
| :--- | :--- | :--- | :--- |
| Report Specifications | KA-08 | Uses BI Standards to define detailed requirements for specific reports. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Dashboard Specifications | KA-08 | Uses BI Standards to define detailed requirements for dashboards. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Data Product Definition | KA-08 | Uses BI Standards to guide the creation of data products with embedded analytics. | `templates/templates-KA-08-data-warehousing-bi.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Examples | Open Source Examples |
| :--- | :--- | :--- |
| BI and Data Visualization | Tableau, Power BI, Qlik Sense, Looker | Apache Superset, Metabase, Grafana |
| Data Preparation and ETL | Alteryx, Trifacta, Tableau Prep | OpenRefine, KNIME, Apache NiFi |
| Data Catalog and Metadata Management | Alation, Collibra, data.world | Amundsen, DataHub, OpenMetadata |
| BI Testing and Validation | BI Validator, Testim | Selenium, Cypress, Great Expectations |
| MLOps and DataOps Integration | DataRobot, MLflow | Kubeflow, Airflow |

### 7.2. Automation Opportunities

- **Automated Style Guides**: Leverage BI tool templates and themes to enforce brand and visualization consistency automatically.
- **Automated Data Validation**: Integrate automated data quality checks and anomaly detection before data is consumed in BI solutions.
- **Automated Testing**: Implement automated functional, regression, and performance testing for BI reports and dashboards.
- **Automated Monitoring**: Use monitoring tools to track BI solution uptime, query performance, and data freshness, with alerting for anomalies.
- **Metadata-Driven Development**: Utilize metadata catalogs to automate lineage tracking, impact analysis, and documentation updates.
- **Integration with MLOps and DataOps**: Automate the deployment and monitoring of AI-enhanced BI features, ensuring compliance with AI governance policies.

---

## 8. References

1. DAMA International. (2017). *DAMA-DMBOK (Data Management Body of Knowledge), 2nd Edition*. Chapter 11: Data Warehousing and Business Intelligence.
2. DAMA International. (Expected 2025). *DAMA-DMBOK 3.0 (Data Management Body of Knowledge), 3rd Edition*. [In Development]
3. Few, S. (2012). *Show Me the Numbers: Designing Tables and Graphs to Enlighten*. Analytics Press.
4. Tufte, E. R. (2001). *The Visual Display of Quantitative Information*. Graphics Press.
5. European Commission. (2021). *Proposal for a Regulation laying down harmonized rules on artificial intelligence (EU AI Act)*.
6. Internal Reference: `reference/role-definitions.md`
7. Internal Reference: `concepts/data-contracts.md`
8. Internal Reference: `concepts/data-products.md`
9. Internal Reference: `guides/governance/ai-governance.md`
10. Internal Reference: `knowledge-areas/KA-01-data-governance.md`
11. Internal Reference: `knowledge-areas/KA-11-data-quality.md`

---

# End of BI Standards Deliverable Template


---

# Dimensional Model


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
  - [3.2. Business Process Overview](#32-business-process-overview)
  - [3.3. Dimensional Model Diagram (Star Schema)](#33-dimensional-model-diagram-star-schema)
  - [3.4. Fact Table Design](#34-fact-table-design)
  - [3.5. Dimension Table Design](#35-dimension-table-design)
- [4. Example](#4-example)
  - [4.1. Business Process Overview: Online Sales](#41-business-process-overview-online-sales)
  - [4.2. Dimensional Model Diagram (Star Schema)](#42-dimensional-model-diagram-star-schema)
  - [4.3. Fact Table Design: F_SALES](#43-fact-table-design-f_sales)
  - [4.4. Dimension Table Design: D_CUSTOMER](#44-dimension-table-design-d_customer)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Input for this Output)](#61-prerequisites-input-for-this-output)
  - [6.2. Consumers (Outputs that use this as Input)](#62-consumers-outputs-that-use-this-as-input)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Dimensional Model** is a specialized data modeling technique optimized for data warehousing and business intelligence (BI) activities. Unlike normalized models (such as 3NF) designed to minimize data redundancy and optimized for transactional (OLTP) systems, dimensional models are intentionally denormalized to enhance query performance, simplify analytical queries, and improve usability for business users. It organizes data into "facts" and "dimensions." A fact represents a measurable event or transaction within a business process (e.g., the sale amount of a transaction), while a dimension provides descriptive context around that measurement (e.g., who, what, where, when, and why).

> The primary purpose of a Dimensional Model is to provide a business-centric, intuitive, and high-performance structure for data analysis, reporting, and dashboarding. It translates complex business processes into a simplified schema that business users can easily understand and query without needing deep technical knowledge of relational database schemas.

In the evolving data landscape, dimensional models remain foundational but are increasingly integrated with modern data management paradigms such as data mesh and data fabric architectures. They serve as core components within cloud-native lakehouse platforms and support AI-driven analytics by providing clean, conformed data structures that facilitate trustworthy insights and governance.

### 1.2. Scope

**Per Product** — A Dimensional Model is typically created for a specific business process or subject area within a data product. For example, a "Sales" data product might have a dimensional model for sales transactions, while a "Marketing" data product might have a separate dimensional model for campaign performance. While some dimensions (like Customer or Date) can be shared across models (conformed dimensions), the fact tables are specific to the business process being modeled.

Dimensional models are designed to support a broad range of analytical use cases, including historical trend analysis, performance measurement, and predictive analytics. They must also align with organizational data governance policies, including emerging AI governance frameworks and compliance requirements such as the EU AI Act alongside GDPR, HIPAA, and CCPA.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-03: Data Modeling and Design | The Dimensional Model is a specific type of logical and physical data model, governed by the standards and conventions defined in this KA. It includes best practices for schema design, naming conventions, and Slowly Changing Dimensions (SCD) handling. |
| KA-02: Data Architecture | Dimensional models are key components of the overall data warehousing and BI architecture defined in the architecture blueprint, including cloud-native and hybrid architectures. |
| KA-06: Data Integration and Interoperability | The ETL/ELT processes defined in this KA are responsible for populating the dimensional models from various source systems, ensuring data quality and consistency. |
| KA-11: Data Quality | The usability of a dimensional model is highly dependent on the quality of its data. Data quality rules are applied before and during the loading of the model to ensure accuracy, completeness, and timeliness. |
| KA-09: Data Governance | Dimensional models must comply with data governance policies, including data stewardship, data contracts, and AI governance frameworks to ensure ethical and compliant data use. |
| KA-12: Data Security and Privacy | Dimensional models must incorporate security controls and privacy considerations, especially when handling sensitive data subject to regulations like GDPR and HIPAA. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately answerable for the delivery and quality of the dimensional model, ensuring it meets business requirements, performance standards, and governance policies including AI governance and compliance mandates. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Designs and develops the dimensional model, including the identification of facts, dimensions, schema creation, and integration with data contracts and data products. |
| **S (Supportive)** | Data Warehouse Architect (DW Arch) | Provides guidance on best practices, ensures the model fits within the overall data warehouse and data mesh/fabric architecture, and reviews the model for technical soundness and scalability. |
| **C (Consulted)** | Data Analyst (D-Analyst), BI Developer (BI Dev), AI Ethics Officer | Provide input on business requirements, query patterns, reporting needs, and ethical considerations to ensure the model is fit for purpose and compliant with AI governance standards. |
| **I (Informed)** | Data Analytics Manager (DA Mgr), Chief AI Officer (CAIO) | Informed of the model's completion, availability, and compliance status for use by the analytics and AI teams. |

### 2.2. Section-Level RASCI

| Model Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Business Requirements | D-Modeler | D-Analyst, BI Dev, AI Ethics Officer | DE Mgr |
| Fact Table Design | D-Modeler | DW Arch, MLOps Engineer | DE Mgr |
| Dimension Table Design | D-Modeler | DW Arch, D-Analyst, Data Steward | DE Mgr |
| Physical Model Implementation | D-Modeler | DW Arch, DataOps Engineer | DE Mgr |
| Data Mapping and ETL Logic | ETL Developer | D-Modeler, DataOps Engineer | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Dimensional Model document. Replace all placeholders `[...]` with project-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Dimensional Model for [Subject Area] |
| Document ID | DM-[KA#]-[Seq#] |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Modeler Name] |
| Approver | [Data Engineering Manager Name] |

### 3.2. Business Process Overview

> *Describe the business process that this dimensional model represents. What is the scope of the process? What are the key events and activities? This section sets the context for the model.*

**Input needed**: Business requirements document, interviews with business stakeholders, AI governance policies, and compliance requirements.
**Who fills this**: Data Modeler, in consultation with Data Analyst, AI Ethics Officer, and Data Steward.

[Provide a detailed description of the business process, e.g., "This model represents the customer sales order process, from order creation to final shipment. Include any relevant AI-driven decision points or data product considerations."]

### 3.3. Dimensional Model Diagram (Star Schema)

> *Include a visual diagram of the star schema. The fact table should be in the center, surrounded by the dimension tables. This provides an immediate, high-level understanding of the model.*

**Input needed**: The completed logical/physical model from a data modeling tool.
**Who fills this**: Data Modeler.

[Insert image of the star schema diagram here]

### 3.4. Fact Table Design

> *Detail the structure of the fact table. List all foreign keys to dimensions and all numeric, additive measures. Specify the grain of the fact table, which is the most critical design decision.*

**Input needed**: Business requirements, source data analysis, AI model outputs if applicable.
**Who fills this**: Data Modeler.

**Fact Table Name**: `[e.g., F_SALES_ORDER_LINE]`

**Grain**: `[e.g., One row per sales order line item]`

| Column Name | Data Type | Description | FK to Dimension |
| :--- | :--- | :--- | :--- |
| `[e.g., DATE_KEY]` | `INTEGER` | Foreign key to the Date Dimension | `D_DATE` |
| `[e.g., CUSTOMER_KEY]` | `INTEGER` | Foreign key to the Customer Dimension | `D_CUSTOMER` |
| `[e.g., PRODUCT_KEY]` | `INTEGER` | Foreign key to the Product Dimension | `D_PRODUCT` |
| `[e.g., ORDER_LINE_AMOUNT]` | `DECIMAL(18,2)` | The total amount for the sales order line. | | 
| `[e.g., ORDER_QUANTITY]` | `INTEGER` | The number of units of the product ordered. | | 
| `[e.g., UNIT_PRICE]` | `DECIMAL(18,2)` | The price of a single unit of the product. | | 
| `[e.g., AI_SCORE]` | `FLOAT` | Optional AI-generated score or prediction related to the transaction | |

### 3.5. Dimension Table Design

> *For each dimension table linked to the fact table, provide a detailed column-level specification. Include the primary key, business key (natural key), and all descriptive attributes. Pay special attention to how slowly changing dimensions (SCDs) will be handled.*

**Input needed**: Source data analysis, business reporting requirements, AI governance considerations.
**Who fills this**: Data Modeler.

#### 3.5.1. Dimension: [e.g., D_CUSTOMER]

**SCD Handling**: `[e.g., Type 2 - new row added for changes to specified attributes]`

| Column Name | Data Type | Description | Key Type |
| :--- | :--- | :--- | :--- |
| `[e.g., CUSTOMER_KEY]` | `INTEGER` | Surrogate primary key | PK |
| `[e.g., CUSTOMER_ID]` | `VARCHAR(50)` | Business key from the source system | BK |
| `[e.g., CUSTOMER_NAME]` | `VARCHAR(255)` | Full name of the customer | Attribute |
| `[e.g., CUSTOMER_SEGMENT]` | `VARCHAR(100)` | The customer's assigned market segment | Attribute (SCD Type 2) |
| `[e.g., ROW_EFFECTIVE_DATE]` | `DATE` | Start date for the version of the dimension record | SCD Control |
| `[e.g., ROW_EXPIRATION_DATE]` | `DATE` | End date for the version of the dimension record | SCD Control |
| `[e.g., IS_CURRENT]` | `BOOLEAN` | Flag to indicate the current version of the record | SCD Control |
| `[e.g., DATA_CONTRACT_ID]` | `VARCHAR(50)` | Identifier for the data contract governing this dimension | Attribute |

#### 3.5.2. Dimension: [e.g., D_PRODUCT]

**SCD Handling**: `[e.g., Type 1 - attribute is overwritten on change]`

| Column Name | Data Type | Description | Key Type |
| :--- | :--- | :--- | :--- |
| `[e.g., PRODUCT_KEY]` | `INTEGER` | Surrogate primary key | PK |
| `[e.g., PRODUCT_SKU]` | `VARCHAR(50)` | Business key (Stock Keeping Unit) | BK |
| `[e.g., PRODUCT_NAME]` | `VARCHAR(255)` | Name of the product | Attribute |
| `[e.g., PRODUCT_CATEGORY]` | `VARCHAR(100)` | The product's category | Attribute (SCD Type 1) |
| `[e.g., IS_ACTIVE]` | `BOOLEAN` | Flag indicating if the product is currently active | Attribute |

---

## 4. Example

> *This section provides a realistic, filled-in example of the Dimensional Model for a fictional company, GlobalRetail Inc. It illustrates how the template is applied to a real-world scenario.*

### 4.1. Business Process Overview: Online Sales

This model represents the online sales transaction process for GlobalRetail Inc. The process begins when a customer places an order on the e-commerce website and ends when the order is successfully processed for shipment. The model is designed to answer questions like "What were our total sales for a given product category in a specific region last quarter?" and "Who are our top 100 customers by sales volume?"

This dimensional model also supports AI-driven customer segmentation and personalized promotion targeting, integrating AI governance controls to ensure ethical use of customer data and compliance with relevant regulations.

### 4.2. Dimensional Model Diagram (Star Schema)

(A diagram would be here showing F_SALES connected to D_DATE, D_CUSTOMER, D_PRODUCT, D_GEOGRAPHY, and D_PROMOTION)

### 4.3. Fact Table Design: F_SALES

**Grain**: One row per product line item on a customer order.

| Column Name | Data Type | Description | FK to Dimension |
| :--- | :--- | :--- | :--- |
| `DATE_KEY` | `INTEGER` | Foreign key to the Date Dimension | `D_DATE` |
| `CUSTOMER_KEY` | `INTEGER` | Foreign key to the Customer Dimension | `D_CUSTOMER` |
| `PRODUCT_KEY` | `INTEGER` | Foreign key to the Product Dimension | `D_PRODUCT` |
| `GEOGRAPHY_KEY` | `INTEGER` | Foreign key to the Geography Dimension | `D_GEOGRAPHY` |
| `PROMOTION_KEY` | `INTEGER` | Foreign key to the Promotion Dimension | `D_PROMOTION` |
| `SALES_AMOUNT` | `DECIMAL(18,2)` | The total amount for the sales line (quantity * price). | | 
| `ORDER_QUANTITY` | `INTEGER` | The number of units of the product ordered. | | 
| `DISCOUNT_AMOUNT` | `DECIMAL(18,2)` | The discount amount applied to the line item. | | 
| `AI_RECOMMENDATION_SCORE` | `FLOAT` | AI-generated score indicating likelihood to accept promotion | |

### 4.4. Dimension Table Design: D_CUSTOMER

**SCD Handling**: Type 2 - new row added for changes to `CUSTOMER_TIER` and `CITY`.

| Column Name | Data Type | Description | Key Type |
| :--- | :--- | :--- | :--- |
| `CUSTOMER_KEY` | `INTEGER` | Surrogate primary key | PK |
| `CUSTOMER_ID` | `VARCHAR(50)` | Business key from the CRM system | BK |
| `CUSTOMER_NAME` | `VARCHAR(255)` | Full name of the customer | Attribute |
| `CUSTOMER_TIER` | `VARCHAR(50)` | Loyalty tier (e.g., Gold, Silver, Bronze) | Attribute (SCD Type 2) |
| `CITY` | `VARCHAR(100)` | The city where the customer resides | Attribute (SCD Type 2) |
| `ROW_EFFECTIVE_DATE` | `DATE` | Start date for this version of the customer record | SCD Control |
| `ROW_EXPIRATION_DATE` | `DATE` | End date for this version of the customer record | SCD Control |
| `IS_CURRENT` | `BOOLEAN` | True if this is the current customer record | SCD Control |
| `DATA_CONTRACT_ID` | `VARCHAR(50)` | Identifier for the data contract governing this customer data | Attribute |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Contracts | Concept | [concepts/data-contracts.md](references/concepts-modern-paradigms.md) |
| Data Product Management | Knowledge Area | knowledge-areas/KA-XX-data-product-management.md |
| AI Governance | Knowledge Area | knowledge-areas/KA-XX-ai-governance.md |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The grain of each fact table is clearly stated and unambiguous.
- [ ] All dimension tables have a surrogate primary key.
- [ ] All fact tables have foreign keys that join to dimension primary keys.
- [ ] The model has been reviewed and approved by the Data Warehouse Architect and AI Ethics Officer.
- [ ] The model successfully supports all required business queries, reports, and AI-driven analytics.
- [ ] SCD (Slowly Changing Dimension) strategies are defined for all relevant dimension attributes.
- [ ] The model adheres to the enterprise naming conventions (`02-naming-conventions.md`).
- [ ] Data contracts are defined and linked to relevant data elements.
- [ ] The model complies with data governance and AI governance policies, including privacy and security requirements.

### 5.2. Review Checklist

| # | Review Question | Pass/Fail |
| :--- | :--- | :--- |
| 1 | Is the model truly dimensional (star or snowflake schema)? | |
| 2 | Are all measures in the fact table numeric and additive? | |
| 3 | Are dimensions denormalized and contain descriptive, textual attributes? | |
| 4 | Have conformed dimensions (like Date, Customer) been used where applicable? | |
| 5 | Does the model avoid mixing grains in a single fact table? | |
| 6 | Is the model understandable to a business user with minimal training? | |
| 7 | Are SCD strategies clearly defined and implemented? | |
| 8 | Are data contracts and stewardship responsibilities documented? | |
| 9 | Does the model comply with AI governance and data privacy regulations? | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-08-data-warehousing-bi.md` | Provides the architectural context and standards into which this dimensional model must fit, including cloud-native and data mesh/fabric considerations. |
| `templates/templates-KA-03-data-modeling-design.md` | Contains the standards for data modeling that this dimensional model must follow, including naming conventions and SCD handling. |
| `templates/templates-KA-08-data-warehousing-bi.md` | Provides specific standards for dimensional modeling, such as naming conventions for facts and dimensions, and integration with data contracts. |
| `templates/templates-KA-09-metadata-management.md` | Defines governance policies and stewardship roles relevant to the dimensional model. |
| `#` | Provides guidance on AI governance considerations impacting data models used in AI/ML contexts. |

### 6.2. Consumers (Outputs that use this as Input)

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-08-data-warehousing-bi.md` | The ETL documentation will detail the process of loading data from source systems into this dimensional model. |
| `templates/templates-KA-08-data-warehousing-bi.md` | This dimensional model may serve as the source for one or more data marts. |
| `templates/templates-KA-08-data-warehousing-bi.md` | BI reports will be designed to query and visualize the data contained in this dimensional model. |
| `#` | MLOps processes may consume dimensional model data for training and scoring ML models. |
| `#` | DataOps pipelines will automate the deployment and monitoring of dimensional model updates. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling Tools** | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, SqlDBM | dbt (for modeling-as-code), Draw.io (for diagrams), OpenModelSphere |
| **Database Platforms** | Snowflake, Google BigQuery, Amazon Redshift, Teradata | PostgreSQL, MySQL (with appropriate indexing) |
| **BI & Visualization** | Tableau, Power BI, Qlik Sense | Apache Superset, Metabase, Grafana |
| **Data Governance & Catalog** | Collibra, Informatica Axon, Alation | Amundsen, DataHub |
| **AI Governance & MLOps** | DataRobot, MLflow, Seldon | Kubeflow, MLflow |

### 7.2. Automation Opportunities

- **Model Generation**: The physical data model (DDL scripts) can be automatically generated from the logical model designed in a data modeling tool, supporting rapid iteration and consistency.
- **Documentation Generation**: Tools like dbt can automatically generate documentation for dbt models, which can be used to populate sections of this document, ensuring up-to-date metadata.
- **ETL/ELT Code Generation**: Some data integration platforms can generate the basic ETL/ELT code required to load the dimensional model based on the source-to-target mappings, reducing manual coding errors.
- **Data Contract Enforcement**: Automation can validate data contracts and enforce SLAs during data ingestion and transformation.
- **Data Quality Monitoring**: Automated data quality checks can be integrated into the ETL pipelines to ensure dimensional model integrity.
- **AI Governance Integration**: Automated lineage and impact analysis tools can track AI model dependencies on dimensional data, supporting compliance and ethical oversight.

---

## 8. References

- **DAMA-DMBOK**: Chapter 11 (Data Warehousing and Business Intelligence), forthcoming DAMA-DMBOK 3.0 updates on AI governance and modern architectures.
- `templates/templates-KA-03-data-modeling-design.md`
- `templates/templates-KA-08-data-warehousing-bi.md`
- `templates/templates-KA-09-metadata-management.md`
- `#`
- `references/reference-materials.md`
- `references/reference-materials.md`


---

# ETL Documentation


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
  - [3.2. ETL Job Overview](#32-etl-job-overview)
  - [3.3. Source System Analysis](#33-source-system-analysis)
  - [3.4. Target Data Model Mapping](#34-target-data-model-mapping)
  - [3.5. Transformation Logic](#35-transformation-logic)
  - [3.6. Error Handling and Logging](#36-error-handling-and-logging)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. ETL Job Overview](#42-etl-job-overview)
  - [4.3. Source System Analysis](#43-source-system-analysis)
  - [4.4. Target Data Model Mapping](#44-target-data-model-mapping)
  - [4.5. Transformation Logic](#45-transformation-logic)
  - [4.6. Error Handling and Logging](#46-error-handling-and-logging)
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

**ETL Documentation** is a comprehensive set of documents that describes the entire Extract, Transform, and Load (ETL) process for a specific data product or data pipeline. It provides a detailed narrative and technical specification of how data is sourced, what transformations are applied to it, and how it is loaded into the target system, typically a data warehouse, data mart, or modern data platform such as a data lakehouse.

> The primary purpose of ETL Documentation is to provide a clear, unambiguous, and maintainable record of the data's journey from source to target. It is essential for debugging, maintenance, impact analysis, and for ensuring data quality, governance, and compliance. In the evolving landscape of data management, ETL documentation also supports AI governance requirements by ensuring transparency and traceability of data transformations that feed AI/ML models.

With the emergence of modern data architectures such as Data Mesh and Data Fabric, ETL documentation plays a critical role in enabling decentralized data ownership while maintaining interoperability and governance standards. Additionally, cloud-native ETL/ELT processes require documentation that reflects dynamic scaling, multi-cloud deployments, and integration with orchestration and MLOps pipelines.

### 1.2. Scope

**Per Product** — This documentation is created for each individual data product that involves an ETL or ELT process. While global standards and frameworks from KA-06 apply, the specifics of each ETL job are documented on a per-product basis to ensure clarity and accountability.

This documentation covers:

- Data extraction from source systems, including APIs, databases, and streaming platforms.
- Data transformation logic, including business rules, data quality checks, and enrichment.
- Data loading into target systems, which may include traditional data warehouses, data lakes, or lakehouses.
- Error handling, logging, and notification mechanisms.
- Compliance considerations such as GDPR, HIPAA, CCPA, and emerging AI regulations (e.g., EU AI Act).

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-06: Data Integration & Interoperability | Provides the standards and patterns (ETL/ELT Standards) that this documentation describes the implementation of. It also covers data contracts and APIs relevant to data ingestion. |
| KA-03: Data Modeling & Design | The Dimensional Model or other data models are key inputs, defining the target schema that the ETL process populates. |
| KA-11: Data Quality | The ETL process is a critical control point for data quality, and this documentation details the quality checks and transformations applied. |
| KA-09: Metadata Management | ETL documentation is a key source of technical metadata, lineage, and operational metadata, feeding metadata repositories and data catalogs. |
| KA-12: Data Governance | Ensures that ETL processes comply with governance policies, including data privacy, security, and AI governance frameworks. |
| KA-14: Data Architecture | Provides context on modern architectures such as Data Mesh, Data Fabric, and Lakehouse that influence ETL design and documentation. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Integration Manager (DI Mgr) | Ultimately answerable for the completeness, accuracy, and maintenance of the ETL documentation for all data products. Ensures compliance with governance and operational standards. |
| **R (Responsible)** | ETL Developer (ETL Dev) | Responsible for creating, updating, and maintaining the ETL documentation for the specific ETL jobs they develop, including reflecting changes from CI/CD pipelines. |
| **S (Supportive)** | Data Engineer (D-Eng) | Provides support by ensuring the underlying data pipelines, infrastructure, and orchestration are correctly represented in the documentation. Supports automation integration. |
| **C (Consulted)** | Data Warehouse Architect (DW Arch) | Consulted to ensure the ETL process and documentation align with the overall data warehouse or lakehouse architecture and design principles. |
| **I (Informed)** | Data Quality Analyst (DQ Analyst) | Informed by the documentation to understand the data transformations and quality rules implemented in the ETL process, supporting monitoring and issue resolution. |
| **C (Consulted)** | AI Ethics Officer / AI Governance Lead | Consulted to ensure ETL processes feeding AI/ML models comply with AI governance policies and regulatory requirements. |

### 2.2. Section-Level RASCI

| Documentation Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Job Overview & Scheduling | ETL Dev | DI Mgr | DI Mgr |
| Source System Analysis | ETL Dev | Source System SME | DI Mgr |
| Target Data Model Mapping | ETL Dev | DW Arch | DI Mgr |
| Transformation Logic | ETL Dev | Business Analyst, DQ Analyst | DI Mgr |
| Error Handling & Logging | ETL Dev | D-Eng | DI Mgr |

---

## 3. Template

> *The following is the standardized template for creating ETL Documentation. Replace all placeholders `[...]` with specific information for the ETL job.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | ETL Documentation: [Data Product Name] |
| Document ID | ETL-[YYYYMMDD]-[NNN] |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [ETL Developer Name] |
| Approver | [Data Integration Manager Name] |
| Related Data Product(s) | [List of data products or pipelines] |
| Compliance Considerations | [e.g., GDPR, HIPAA, EU AI Act] |

### 3.2. ETL Job Overview

> *Provide a high-level summary of the ETL job, its purpose, and its place in the overall data landscape.*

*   **Job Name:** `[ETL Job Name]`
*   **Description:** `[Brief description of the ETL job's purpose and the data it processes]`
*   **Business Purpose:** `[The business reason for this ETL process, e.g., to populate the Sales Data Mart for weekly reporting]`
*   **Scheduling:** `[e.g., Daily at 2:00 AM UTC]`
*   **Orchestration Tool:** `[e.g., Apache Airflow, dbt, Prefect]`
*   **Data Product Owner:** `[Name and contact]`
*   **Data Steward(s):** `[Names and roles, including emerging agentic stewardship roles]`
*   **Compliance and Governance Notes:** `[Notes on compliance requirements and governance policies]`

### 3.3. Source System Analysis

> *Detail each source system and the specific data entities being extracted. Repeat this section for each source.*

*   **Source System:** `[e.g., Salesforce CRM]`
*   **Source Type:** `[e.g., Database, API, Flat File, Streaming]`
*   **Extraction Method:** `[e.g., Full, Incremental, CDC]`
*   **Extraction Frequency:** `[e.g., Daily, Real-time]`
*   **Source Data Entities:**

| Entity/Table Name | Filter Conditions | Incremental Load Key | Description |
| :--- | :--- | :--- | :--- |
| `[e.g., Account]` | `[e.g., IsActive = true]` | `[e.g., LastModifiedDate]` | `[Description of the source entity]` |
| `[e.g., Opportunity]` | `[e.g., StageName = 'Closed Won']` | `[e.g., LastModifiedDate]` | `[Description of the source entity]` |

*   **Data Contracts:** `[Reference to data contracts or SLAs governing the source data]`
*   **Data Quality Considerations:** `[Known data quality issues or validations at source]`
*   **Security and Privacy Controls:** `[Encryption, masking, PII handling]`

### 3.4. Target Data Model Mapping

> *Map the source data elements to the target dimensional model or other data model. This is the core of the ETL documentation.*

*   **Target Schema:** `[e.g., dw_sales]`
*   **Target Table(s):** `[e.g., F_SALES, D_CUSTOMER, D_PRODUCT]`

#### 3.4.1. Fact Table Mapping: `[Fact Table Name]`

| Target Column | Data Type | Source Table(s) | Source Column(s) | Transformation Logic | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[e.g., CustomerKey]` | `INT` | `D_CUSTOMER` | `CustomerBK` | `Lookup on CustomerBK` | `[Additional notes]` |
| `[e.g., ProductKey]` | `INT` | `D_PRODUCT` | `ProductBK` | `Lookup on ProductBK` | |
| `[e.g., SalesAmount]` | `DECIMAL(18,2)` | `Opportunity` | `Amount` | `Direct Map` | |

#### 3.4.2. Dimension Table Mapping: `[Dimension Table Name]`

| Target Column | Data Type | SCD Type | Source Table(s) | Source Column(s) | Transformation Logic | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[e.g., CustomerBK]` | `VARCHAR(50)` | N/A | `Account` | `Id` | `Direct Map` | |
| `[e.g., CustomerName]` | `VARCHAR(255)` | SCD 1 | `Account` | `Name` | `Direct Map` | |
| `[e.g., Industry]` | `VARCHAR(100)` | SCD 2 | `Account` | `Industry` | `Direct Map` | |
| `[e.g., IsActive]` | `BOOLEAN` | SCD 1 | `Account` | `IsActive__c` | `Direct Map` | |

*   **Data Product Contracts:** `[Reference to data contracts or SLAs for target data]`
*   **Data Lineage:** `[Reference to lineage documentation or tools]`

### 3.5. Transformation Logic

> *Describe any complex business rules or transformations that are not covered in the mapping table. Use code snippets or pseudocode where helpful.*

*   **Business Rule 1:** `[Description of the business rule]`
*   **Implementation:** `[Pseudocode or code snippet]`

*   **Business Rule 2:** `[Additional rules as needed]`
*   **Implementation:** `[Pseudocode or code snippet]`

*   **Notes on AI/ML Impact:** `[If transformations feed AI models, document any special considerations for explainability or fairness]`

### 3.6. Error Handling and Logging

> *Detail the error handling, logging, and notification mechanisms for the ETL job.*

*   **Error Handling Strategy:** `[e.g., Fail on error, Skip row and log, Retry logic]`
*   **Logging Level:** `[e.g., INFO, DEBUG, ERROR]`
*   **Log Location:** `[e.g., /var/log/etl/job_name.log, Cloud logging service]`
*   **Notifications:** `[e.g., Email to etl-admins@example.com on failure, Slack alerts]`
*   **Monitoring and Alerting:** `[Integration with monitoring tools such as Prometheus, Datadog]`
*   **Audit and Compliance Logging:** `[Details on audit trails for regulatory compliance]`

---

## 4. Example

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | ETL Documentation: Sales Data Mart |
| Document ID | ETL-20260208-001 |
| Version | 1.0 |
| Effective Date | 2026-02-08 |
| Owner | John Doe |
| Approver | Jane Smith |
| Related Data Product(s) | Sales Data Mart |
| Compliance Considerations | GDPR, CCPA |

### 4.2. ETL Job Overview

*   **Job Name:** `load_sales_datamart`
*   **Description:** This ETL job extracts sales data from Salesforce and operational databases, transforms it, and loads it into the Sales Data Mart.
*   **Business Purpose:** To provide a consolidated view of sales performance for executive dashboards and weekly reporting.
*   **Scheduling:** Daily at 3:00 AM EST
*   **Orchestration Tool:** dbt Cloud
*   **Data Product Owner:** Jane Smith, Sales Analytics Lead
*   **Data Steward(s):** John Doe, ETL Developer; Mary Johnson, Data Quality Analyst
*   **Compliance and Governance Notes:** Data is handled in accordance with GDPR and CCPA. PII fields are masked during transformation.

### 4.3. Source System Analysis

*   **Source System:** Salesforce CRM
*   **Source Type:** API
*   **Extraction Method:** Incremental
*   **Extraction Frequency:** Daily
*   **Source Data Entities:**

| Entity/Table Name | Filter Conditions | Incremental Load Key | Description |
| :--- | :--- | :--- | :--- |
| `Account` | `IsActive__c = true` | `LastModifiedDate` | Customer account information. |
| `Opportunity` | `StageName = 'Closed Won'` | `LastModifiedDate` | Details of won sales opportunities. |
| `Product2` | `IsActive = true` | `LastModifiedDate` | Product information. |

*   **Data Contracts:** Salesforce API SLA guarantees 99.9% availability with daily data refresh.
*   **Data Quality Considerations:** Account records with missing `Industry` are flagged for review.
*   **Security and Privacy Controls:** PII fields such as customer email are masked post-extraction.

### 4.4. Target Data Model Mapping

*   **Target Schema:** `analytics`
*   **Target Table(s):** `fct_sales`, `dim_customer`, `dim_product`

#### 4.4.1. Fact Table Mapping: `fct_sales`

| Target Column | Data Type | Source Table(s) | Source Column(s) | Transformation Logic | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `customer_key` | `INT` | `dim_customer` | `customer_bk` | `Lookup on Opportunity.AccountId` | |
| `product_key` | `INT` | `dim_product` | `product_bk` | `Lookup on OpportunityLineItem.Product2Id` | |
| `sales_amount` | `DECIMAL(18,2)` | `Opportunity` | `Amount` | `Direct Map` | |
| `order_date_key` | `INT` | `Opportunity` | `CloseDate` | `CONVERT(INT, FORMAT(CloseDate, 'yyyyMMdd'))` | |

#### 4.4.2. Dimension Table Mapping: `dim_customer`

| Target Column | Data Type | SCD Type | Source Table(s) | Source Column(s) | Transformation Logic | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `customer_bk` | `VARCHAR(50)` | N/A | `Account` | `Id` | `Direct Map` | |
| `customer_name` | `VARCHAR(255)` | SCD 1 | `Account` | `Name` | `Direct Map` | |
| `industry` | `VARCHAR(100)` | SCD 2 | `Account` | `Industry` | `COALESCE(Industry, 'Unknown')` | |
| `is_active` | `BOOLEAN` | SCD 1 | `Account` | `IsActive__c` | `Direct Map` | |

*   **Data Product Contracts:** SLA requires 99.5% data freshness within 24 hours.
*   **Data Lineage:** Documented in `templates/templates-KA-06-data-integration-interoperability.md`.

### 4.5. Transformation Logic

*   **Business Rule 1:** The `sales_amount` is calculated as the sum of `OpportunityLineItem.TotalPrice` for a given `Opportunity`. If no line items exist, the `Opportunity.Amount` is used.
*   **Implementation:**

```sql
SELECT
  o.Id AS opportunity_id,
  COALESCE(SUM(oli.TotalPrice), o.Amount) AS sales_amount
FROM Opportunity AS o
LEFT JOIN OpportunityLineItem AS oli ON o.Id = oli.OpportunityId
GROUP BY o.Id, o.Amount;
```

*   **Business Rule 2:** Customer `industry` defaults to 'Unknown' if missing to maintain dimensional integrity.
*   **Implementation:**

```sql
SELECT
  Id,
  Name,
  COALESCE(Industry, 'Unknown') AS Industry,
  IsActive__c
FROM Account;
```

*   **AI/ML Considerations:** Transformation logic is version-controlled to support explainability of AI models consuming this data.

### 4.6. Error Handling and Logging

*   **Error Handling Strategy:** The dbt job will fail if any data quality tests fail. Invalid rows are reported but not loaded.
*   **Logging Level:** INFO
*   **Log Location:** dbt Cloud run history and centralized logging system.
*   **Notifications:** Slack notification to `#data-engineering` channel on job failure.
*   **Monitoring:** Integrated with Datadog for alerting on job failures and performance anomalies.
*   **Audit Logging:** All ETL runs are logged with timestamps, user actions, and data volume metrics for compliance audits.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Metrics KPIs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Lineage | Deliverable | **templates/templates-KA-06-data-integration-interoperability.md** |
| Data Contracts | Concept | [#](references/concepts-modern-paradigms.md) |
| Data Mesh Overview | Knowledge Area | **templates/templates-KA-14-data-management-maturity.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] All source-to-target mappings are documented with clear transformation logic.
- [x] All transformation logic is clearly described, including complex business rules.
- [x] The ETL job schedule, dependencies, and orchestration details are defined.
- [x] Error handling, logging procedures, and monitoring mechanisms are specified.
- [x] The documentation has been reviewed and approved by the Data Integration Manager.
- [x] Compliance and governance requirements (e.g., GDPR, AI Act) are addressed.
- [x] Data contracts and SLAs related to the ETL process are referenced.
- [x] Metadata and lineage integration points are identified.

### 5.2. Review Checklist

| Question | Yes/No | Comments |
| :--- | :--- | :--- |
| Is the business purpose of the ETL job clearly stated? | Yes | |
| Are all source systems and entities identified? | Yes | |
| Are data contracts and SLAs referenced where applicable? | Yes | |
| Is the source-to-target mapping complete and accurate? | Yes | |
| Is the transformation logic easy to understand and complete? | Yes | |
| Are the SCD types for dimension attributes correctly identified? | Yes | |
| Is the error handling strategy appropriate for the data product? | Yes | |
| Are compliance and governance considerations documented? | Yes | |
| Is the documentation linked to metadata and lineage systems? | Yes | |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-03-data-modeling-design.md` | Provides the target schema for the ETL process. |
| `templates/templates-KA-06-data-integration-interoperability.md` | Defines the standards and best practices that this ETL job must follow. |
| `templates/templates-KA-08-data-warehousing-bi.md` | Provides a detailed analysis of the source systems used in this ETL job. |
| `references/reference-materials.md` | Provides definitions for business terms used in transformation logic. |
| `templates/templates-KA-12-data-handling-ethics.md` | Provides governance policies relevant to ETL processes. |
| `templates/templates-KA-09-metadata-management.md` | Metadata repositories that ingest ETL technical metadata. |

### 6.2. Consumers

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-06-data-integration-interoperability.md` | This documentation is a key input for generating and validating data lineage. |
| `templates/templates-KA-11-data-quality.md` | The ETL documentation is used to investigate data quality issues found in the report. |
| `templates/templates-KA-14-data-management-maturity.md` | Supports decentralized data ownership and interoperability in Data Mesh architectures. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| ETL/ELT Platforms | Informatica PowerCenter, Talend, Fivetran, Matillion | dbt, Apache Airflow, Prefect, Talend Open Studio |
| Data Quality | Ataccama, Trillium, Collibra | Great Expectations, Soda Core, Deequ |
| Orchestration | Control-M, ActiveBatch, Azure Data Factory | Apache Airflow, Prefect, Luigi |
| Metadata & Lineage | Collibra, Alation, Informatica EDC | Amundsen, OpenLineage, Marquez |
| Monitoring & Logging | Splunk, Datadog, New Relic | ELK Stack, Prometheus, Grafana |

### 7.2. Automation Opportunities

*   **Documentation Generation:** Tools like dbt and Apache Atlas can automatically generate documentation for models, sources, and tests from the codebase itself, reducing manual effort and improving accuracy.
*   **Data Lineage:** Automated data lineage tools can parse ETL code, SQL queries, and orchestration workflows to visualize data flows, reducing the need for manual lineage documentation and enabling impact analysis.
*   **Testing:** Data quality and transformation logic tests can be automated and integrated into CI/CD pipelines for the ETL code, enabling continuous validation.
*   **Compliance Monitoring:** Automated scanning for PII and sensitive data can be integrated into ETL pipelines to ensure compliance with GDPR, HIPAA, and emerging AI regulations.
*   **AI Governance Integration:** ETL documentation can be linked with AI model registries and governance platforms to ensure traceability of data used in AI/ML workflows.

---

## 8. References

*   **DAMA-DMBOK2:** Chapter 11, "Data Warehousing and Business Intelligence"
*   **DAMA-DMBOK 3.0 (forthcoming):** Expected to include expanded guidance on AI governance, data mesh/fabric architectures, and cloud-native data management.
*   **Internal:** `reference/role-definitions.md`
*   **Internal:** `templates/templates-KA-06-data-integration-interoperability.md`
*   **Internal:** `templates/templates-KA-09-metadata-management.md`
*   **Internal:** `templates/templates-KA-12-data-handling-ethics.md`
*   **External:** EU AI Act compliance guidelines and GDPR/HIPAA/CCPA regulations.


---

# Report Specifications


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
  - [3.2. Report Overview](#32-report-overview)
  - [3.3. Data Requirements](#33-data-requirements)
  - [3.4. Layout and Visualization](#34-layout-and-visualization)
  - [3.5. Functional and Non-Functional Requirements](#35-functional-and-non-functional-requirements)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Report Overview](#42-report-overview)
  - [4.3. Data Requirements](#43-data-requirements)
  - [4.4. Layout and Visualization](#44-layout-and-visualization)
  - [4.5. Functional and Non-Functional Requirements](#45-functional-and-non-functional-requirements)
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

**Report Specifications** are comprehensive documents that articulate the detailed requirements for a business intelligence (BI) report or dashboard. They serve as a formal agreement between business stakeholders, data governance, and the development team, ensuring that the final report delivers accurate, relevant, and actionable information in the intended format and context. This document translates business needs and data governance policies into a technical blueprint for BI Developers and Data Engineers to build from.

> A Report Specification answers the question: *"What data should this report show, how should it look, and how should it behave?"*

In the evolving data landscape, Report Specifications also incorporate considerations for AI governance, data product integration, and cloud-native architectures, ensuring alignment with modern data mesh and data fabric principles. They support compliance with regulatory frameworks such as GDPR, HIPAA, CCPA, and the emerging EU AI Act by embedding data privacy, security, and ethical usage requirements into the report design.

### 1.2. Scope

**Per Product** — A Report Specification document is created for each individual report or a closely related group of reports within a specific data product or data domain. It covers all aspects from data sourcing and transformation logic to visualization and user interaction.

This deliverable is applicable across traditional BI platforms, cloud-native analytics environments, and hybrid architectures leveraging data mesh or lakehouse paradigms. It supports integration with MLOps and DataOps pipelines where reports may include AI-driven insights or operational metrics.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Business Glossary (KA-01) provides standardized definitions for metrics, attributes, and data policies referenced in the report. AI governance policies are also relevant here. |
| KA-03: Data Modeling and Design | Logical and Physical Data Models (KA-03) define the source tables, views, and data structures that the report queries, including data contracts and product boundaries. |
| KA-08: Data Warehousing and BI | This deliverable is part of KA-08 and aligns with BI standards, report development best practices, and data integration patterns. |
| KA-09: Metadata Management | KPI Definitions and metadata artifacts (KA-09) are direct inputs for defining calculations, lineage, and impact analysis within the report. |
| KA-11: Data Quality | Data Quality rules and thresholds (KA-11) for source data inform report accuracy expectations and error handling. |
| KA-12: Data Security and Privacy | Security requirements, data masking, and compliance controls are specified here to ensure reports meet regulatory and organizational standards. |
| KA-13: Artificial Intelligence and Machine Learning | For reports incorporating AI/ML outputs, governance, explainability, and model performance metrics are considered. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Analytics Manager (DA Mgr) or Chief Analytics Officer (CAIO) | Ultimately accountable for the quality, business alignment, and approval of the final report specification, ensuring it supports strategic objectives and governance policies. |
| **R (Responsible)** | BI Developer (BI Dev) / Data Engineer | Responsible for drafting and updating the report specification, implementing the report, and ensuring technical feasibility and performance. |
| **S (Supportive)** | Data Analyst (D-Analyst), Data Steward | Supports requirements gathering, metric definition, validation of data accuracy, and adherence to data stewardship principles. |
| **C (Consulted)** | Business Users, Subject Matter Experts (SME), Data Governance Manager (DG Mgr), AI Ethics Officer | Consulted to provide business context, validate requirements, ensure compliance with governance and ethical standards, and review technical design. |
| **I (Informed)** | Data Product Manager, MLOps Engineer, Security Officer | Kept informed about report specifications to coordinate integration with data products, AI/ML pipelines, and security frameworks. |

### 2.2. Section-Level RASCI

| Specification Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Report Purpose & Audience | Data Analyst | Business Users, SME | DA Mgr / CAIO |
| Data Requirements | Data Analyst, BI Developer | BI Dev, SME, Data Steward | DA Mgr / DG Mgr |
| Layout & Visualization | Data Analyst | Business Users, UX Designer | DA Mgr |
| Functional Requirements | BI Developer | Data Analyst, Security Officer | DA Mgr |
| Non-Functional Requirements (Performance, Security) | BI Developer, Security Officer | DG Mgr, MLOps Engineer | DA Mgr |
| Acceptance Criteria | Data Analyst | Business Users, DG Mgr | DA Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Report Specification. Replace all placeholders `[...]` with project-specific information.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Report Name | [Official Name of the Report] |
| Report ID | [Unique Identifier, e.g., BI-SALES-001] |
| Version | [e.g., 1.0] |
| Status | [Draft, In Review, Approved] |
| Business Owner | [Name and Title of the primary business stakeholder] |
| Technical Owner | [Name and Title of the BI Developer, Data Engineer, or technical lead] |
| Creation Date | [YYYY-MM-DD] |
| Last Updated | [YYYY-MM-DD] |
| Data Product | [Name of the associated data product or domain] |
| Compliance Requirements | [e.g., GDPR, HIPAA, EU AI Act] |

### 3.2. Report Overview

> *Provide a high-level summary of the report's purpose, audience, and the key business questions it answers.*

**Input needed**: Interviews with business stakeholders, data governance policies.  
**Who fills this**: Data Analyst.

*   **Purpose and Business Value**: [Describe the business objective of the report. What decisions will it support? How does it align with organizational goals and data strategy?]
*   **Target Audience**: [List the primary and secondary users of the report, e.g., Sales Managers, Marketing Analysts, Data Product Managers.]
*   **Key Business Questions**: [List the specific questions the report will answer, e.g., "What are our top 10 selling products by region?"]
*   **Governance Considerations**: [Summarize any relevant data governance, privacy, or AI ethics considerations impacting the report.]

### 3.3. Data Requirements

> *Detail the data needed for the report, including sources, specific fields, calculations, filters, and data contracts.*

**Input needed**: Logical Data Model, Business Glossary, KPI Definitions, Data Contracts.  
**Who fills this**: Data Analyst, with support from BI Developer and Data Steward.

#### 3.3.1. Data Sources

| Source System | Source Object (Table/View) | Description | Data Product / Domain |
| :--- | :--- | :--- | :--- |
| [e.g., EDW, Cloud Data Lake] | [e.g., `fact_sales`, `dim_product`] | [Primary source for sales transactions and product details.] | [e.g., Sales Data Product] |

#### 3.3.2. Data Elements and Metrics

| Element/Metric Name | Source Field / Calculation | Business Definition (from Glossary) | Data Type | Data Quality Rules |
| :--- | :--- | :--- | :--- | :--- |
| [e.g., Total Revenue] | [e.g., `SUM(fact_sales.sale_amount)`] | [Total value of all sales transactions.] | [Currency] | [e.g., Nulls not allowed, threshold > 0] |
| [e.g., Product Name] | [e.g., `dim_product.product_name`] | [The official name of the product.] | [String] | [e.g., Must match glossary term] |

#### 3.3.3. Report Filters and Prompts

| Filter/Prompt Name | Type | Options / Data Type | Default Value | Required? | Governance Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., Date Range] | [Prompt] | [Date] | [Current Quarter] | [Yes] | [e.g., Data masking for sensitive dates] |
| [e.g., Region] | [Filter] | [List of values from `dim_customer.region`] | [All] | [No] | [e.g., Access restricted by user role] |

### 3.4. Layout and Visualization

> *Describe the visual presentation of the report. Include mockups or wireframes whenever possible.*

**Input needed**: BI Standards, user feedback, UX guidelines.  
**Who fills this**: Data Analyst, UX Designer.

#### 3.4.1. Report Layout

[Provide a sketch, wireframe, or detailed description of the report layout. e.g., "Header section with logo and report name. Left panel for filters. Main content area with three charts arranged vertically."]

Consider accessibility standards and responsive design for multi-device support.

#### 3.4.2. Visualizations

| Chart/Component ID | Type | Dimensions | Measures | Description | Interaction Features |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., CHT-01] | [Bar Chart] | [Product Category] | [Total Revenue] | [Shows revenue by product category, sorted descending.] | [Drill-down, hover tooltips] |
| [e.g., TBL-01] | [Table] | [Product Name, Sale Date] | [Units Sold, Sale Amount] | [Detailed list of sales transactions.] | [Sorting, filtering] |

### 3.5. Functional and Non-Functional Requirements

> *Define how the report should behave and the performance, security, and compliance constraints.*

**Input needed**: BI Standards, SLA Documentation, Security Policies.  
**Who fills this**: BI Developer, Data Analyst, Security Officer.

*   **Drill-Down/Through**: [Describe any drill-down paths, e.g., "Users can drill down from Product Category to individual Product Name."]
*   **Sorting**: [Default sort order for all components, e.g., "All charts sorted descending by revenue."]
*   **Exporting**: [Specify allowed export formats, e.g., PDF, Excel, CSV.]
*   **Performance**: [Maximum acceptable report load time, e.g., "Report must render in under 10 seconds."]
*   **Security**: [Data access rules, e.g., "Sales reps can only see data for their own region." Include masking, anonymization, and compliance requirements.]
*   **Refresh Frequency**: [How often the data should be updated, e.g., "Daily at 6:00 AM UTC."]
*   **Audit and Logging**: [Specify requirements for usage tracking and data access logs.]
*   **AI/ML Integration**: [If applicable, specify how AI-driven insights are incorporated and governed.]
*   **Cloud and Multi-Environment Considerations**: [Specify any cloud-native or multi-cloud deployment requirements.]

---

## 4. Example

> *This is a filled-in example for a fictional company, GlobalRetail Inc.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Report Name | Quarterly Sales Performance Report |
| Report ID | BI-SALES-001 |
| Version | 1.0 |
| Status | Approved |
| Business Owner | John Smith, VP of Sales |
| Technical Owner | Jane Doe, Senior BI Developer |
| Creation Date | 2026-01-15 |
| Last Updated | 2026-02-05 |
| Data Product | Sales Analytics |
| Compliance Requirements | GDPR, Internal Data Governance Policies |

### 4.2. Report Overview

*   **Purpose and Business Value**: To provide executive leadership with a clear overview of sales performance across regions and product categories, enabling strategic decisions on resource allocation and marketing spend. Supports compliance with internal data privacy policies by restricting access and masking sensitive data.
*   **Target Audience**: C-Level Executives, VP of Sales, Regional Sales Managers.
*   **Key Business Questions**:
    1.  What was our total revenue for the quarter compared to the previous quarter and the same quarter last year?
    2.  Which regions are performing best and worst?
    3.  What are our top 5 selling product categories?
*   **Governance Considerations**: Data is filtered based on user roles to comply with data privacy policies. Audit logs will track report access.

### 4.3. Data Requirements

#### 4.3.1. Data Sources

| Source System | Source Object (Table/View) | Description | Data Product / Domain |
| :--- | :--- | :--- | :--- |
| Enterprise Data Warehouse | `v_sales_quarterly_summary`, `dim_date`, `dim_product`, `dim_region` | Aggregated quarterly sales data and related dimensions. | Sales Analytics |

#### 4.3.2. Data Elements and Metrics

| Element/Metric Name | Source Field / Calculation | Business Definition (from Glossary) | Data Type | Data Quality Rules |
| :--- | :--- | :--- | :--- | :--- |
| Total Revenue | `SUM(v_sales_quarterly_summary.total_revenue)` | Total value of all sales transactions in the quarter. | Currency | No nulls, must be >= 0 |
| Revenue vs. Prior Quarter | `(CurrentQ_Revenue - PriorQ_Revenue) / PriorQ_Revenue` | The percentage change in revenue from the previous quarter. | Percentage | Calculated field, validated monthly |
| Region | `dim_region.region_name` | The name of the sales region. | String | Must match approved region list |
| Product Category | `dim_product.category_name` | The highest-level category for a product. | String | Must align with business glossary |

#### 4.3.3. Report Filters and Prompts

| Filter/Prompt Name | Type | Options / Data Type | Default Value | Required? | Governance Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Quarter | Prompt | List of Quarters (e.g., Q1 2026) | Current Quarter | Yes | Access restricted by user role |
| Region | Filter | List of Regions | All | No | Data masked for unauthorized regions |

### 4.4. Layout and Visualization

#### 4.4.1. Report Layout

A single-page dashboard with the GlobalRetail Inc. logo and report title at the top. A prompt for "Quarter" is in the top-right corner. The main body contains three sections: KPIs at the top, a map visualization, and a bar chart below it. The layout is responsive and accessible per WCAG 2.1 standards.

#### 4.4.2. Visualizations

| Chart/Component ID | Type | Dimensions | Measures | Description | Interaction Features |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KPI-01 | KPI Card | - | Total Revenue | Displays total revenue for the selected quarter. | Hover tooltips |
| KPI-02 | KPI Card | - | Revenue vs. Prior Quarter | Displays the % change in revenue from the prior quarter. | Hover tooltips |
| MAP-01 | Geographic Map | Region | Total Revenue | A world map shaded by region, with darker shades indicating higher revenue. | Drill-down to regional report |
| CHT-01 | Horizontal Bar Chart | Product Category | Total Revenue | Shows the top 5 product categories by revenue. | Sorting, filtering |

### 4.5. Functional and Non-Functional Requirements

*   **Drill-Down/Through**: Users can click on a region on the map (MAP-01) to open a separate "Regional Details" report.
*   **Sorting**: The bar chart (CHT-01) is sorted descending by Total Revenue.
*   **Exporting**: Allowed formats are PDF and PNG.
*   **Performance**: The report must load in under 8 seconds.
*   **Security**: Access is restricted to users in the 'Executive' and 'Sales Leadership' security groups. Data masking is applied for unauthorized regions.
*   **Refresh Frequency**: The underlying summary view is refreshed daily at 4:00 AM UTC.
*   **Audit and Logging**: All report access and exports are logged for compliance.
*   **AI/ML Integration**: Not applicable for this report.
*   **Cloud Deployment**: Hosted on the company’s cloud BI platform with multi-region failover.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics KPIs | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Business Glossary | Deliverable | `templates/templates-KA-01-data-governance.md` |
| KPI Definitions | Deliverable | `templates/templates-KA-08-data-warehousing-bi.md` |
| BI Standards | Deliverable | `templates/templates-KA-08-data-warehousing-bi.md` |

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [ ] All metrics match the definitions in the Business Glossary and KPI Definitions.
- [ ] The report renders correctly in under the specified performance threshold.
- [ ] The default prompt values are current and contextually appropriate.
- [ ] Drill-through and interactive features function as specified.
- [ ] Data is refreshed according to the defined schedule and matches source systems.
- [ ] Access controls and data masking comply with governance policies.
- [ ] Audit logs capture report usage and data exports.
- [ ] The report layout meets accessibility and usability standards.
- [ ] Compliance with relevant regulations (e.g., GDPR, EU AI Act) is documented and enforced.

### 5.2. Review Checklist

| Review Area | Question | Reviewer |
| :--- | :--- | :--- |
| Business Alignment | Does the report answer the key business questions defined in the overview? | Business Owner |
| Data Accuracy | Is the data correct? Have the calculations been validated against the source? | Data Analyst |
| Usability | Is the report easy to understand and navigate? Is the layout intuitive and accessible? | Business Users, UX Designer |
| Technical Feasibility | Can the report be built as specified with the available tools and data? | BI Developer |
| Security and Compliance | Does the report comply with all relevant data standards, privacy policies, and regulations? | DG Mgr, Security Officer |
| Governance | Are data stewardship and AI governance principles applied appropriately? | Data Steward, AI Ethics Officer |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | Knowledge Area | File Path |
| :--- | :--- | :--- |
| BI Standards | KA-08: Data Warehousing and BI | `templates/templates-KA-08-data-warehousing-bi.md` |
| KPI Definitions | KA-09: Metadata Management | `templates/templates-KA-08-data-warehousing-bi.md` |
| Business Glossary | KA-01: Data Governance | `templates/templates-KA-01-data-governance.md` |
| Data Quality Rules | KA-11: Data Quality | `templates/templates-KA-11-data-quality.md` |
| Security and Privacy Policies | KA-12: Data Security and Privacy | `templates/templates-KA-12-data-handling-ethics.md` |

### 6.2. Consumers (Outputs)

| Output Name | Knowledge Area | File Path |
| :--- | :--- | :--- |
| Dashboard Specifications | KA-08: Data Warehousing and BI | `templates/templates-KA-08-data-warehousing-bi.md` |
| Data Product Release Notes | KA-08: Data Warehousing and BI | `templates/templates-KA-08-data-warehousing-bi.md` |
| AI/ML Model Reports | KA-13: Artificial Intelligence and Machine Learning | `templates/templates-KA-13-big-data-data-science.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| BI Reporting Platform | Power BI, Tableau, Qlik Sense, Looker | Apache Superset, Metabase, Redash |
| Specification Management | Confluence, Jira, SharePoint | DokuWiki, BookStack |
| Data Source Querying | DBeaver, SQL Server Management Studio, Snowflake UI | pgAdmin, MySQL Workbench |
| Metadata and Lineage | Collibra, Alation | Amundsen, OpenLineage |
| Automation & Testing | Great Expectations, dbt | Great Expectations, dbt |

### 7.2. Automation Opportunities

*   **Specification Generation**: Develop CLI tools or web forms to prompt users for required sections and generate initial Markdown files from templates, reducing manual effort and standardizing output.
*   **Metric Validation**: Implement automated tests that run SQL queries against the data warehouse to validate that metric calculations in the report match definitions in the specification and business glossary.
*   **Lineage Tracking**: Use metadata harvesting tools to parse report files and underlying queries to generate and update data lineage diagrams, illustrating data flow from source to report.
*   **Governance Compliance Checks**: Automate checks for compliance with data privacy, security, and AI governance policies, flagging potential issues before report deployment.
*   **Performance Monitoring**: Integrate automated performance testing to ensure reports meet load time SLAs.
*   **Version Control and Collaboration**: Use Git or similar tools to manage report specification versions and enable collaborative editing with audit trails.

---

## 8. References

*   **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 11)  
*   **[2]** DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Community-driven update launching June 2025, emphasizing AI governance, data mesh/fabric, and cloud-native architectures.  
*   **[3]** Internal Reference: `templates/templates-KA-01-data-governance.md`  
*   **[4]** Internal Reference: `templates/templates-KA-08-data-warehousing-bi.md`  
*   **[5]** Internal Reference: `templates/templates-KA-08-data-warehousing-bi.md`  
*   **[6]** Internal Reference: `references/reference-materials.md`  
*   **[7]** EU AI Act and GDPR Compliance Guidelines, [external regulatory documentation]  

---

# End of Report Specifications Template


---

# Dashboard Specifications


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI (for Template Usage)](#22-section-level-rasci-for-template-usage)
- [3. Template](#3-template)
  - [3.1. Document Control](#31-document-control)
  - [3.2. Overview & Business Purpose](#32-overview-business-purpose)
  - [3.3. Key Performance Indicators (KPIs) & Metrics](#33-key-performance-indicators-kpis-metrics)
  - [3.4. Functional Requirements](#34-functional-requirements)
  - [3.5. Data Requirements](#35-data-requirements)
  - [3.6. Visual Design & Layout (Wireframe)](#36-visual-design-layout-wireframe)
  - [3.7. Non-Functional Requirements](#37-non-functional-requirements)
- [4. Example](#4-example)
  - [**4.1. Document Control**](#41-document-control)
  - [**4.2. Overview & Business Purpose**](#42-overview-business-purpose)
  - [**4.3. Key Performance Indicators (KPIs) & Metrics**](#43-key-performance-indicators-kpis-metrics)
  - [**4.4. Functional Requirements**](#44-functional-requirements)
  - [**4.5. Data Requirements**](#45-data-requirements)
  - [**4.6. Visual Design & Layout (Wireframe)**](#46-visual-design-layout-wireframe)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria (Checklist)](#51-acceptance-criteria-checklist)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs to this Output)](#61-prerequisites-inputs-to-this-output)
  - [6.2. Consumers (Outputs that use this Output)](#62-consumers-outputs-that-use-this-output)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Dashboard Specifications** document is a comprehensive blueprint that details the business requirements, functional design, data sources, and visual layout for a business intelligence (BI) dashboard or data product. It serves as the primary communication tool between business stakeholders and the development team (BI Developers, Data Visualization Specialists, Data Engineers) to ensure the final product aligns precisely with user expectations, analytical needs, and governance requirements. Its purpose is to translate abstract business questions and strategic objectives into a concrete, actionable development plan, minimizing ambiguity, rework, and misalignment.

> This document acts as the "architectural plan" for a dashboard or data product, ensuring that what is built is precisely what the business needs to make informed decisions, while incorporating modern data management principles such as data product thinking, AI governance, and cloud-native architectures.

With the evolving data landscape, this specification also integrates considerations for emerging paradigms such as Data Mesh and Data Fabric architectures, ensuring that dashboards are designed as first-class data products with clear ownership, discoverability, and compliance with enterprise data policies including AI governance frameworks and regulatory mandates like the EU AI Act.

### 1.2. Scope

**Per Product** — A unique Dashboard Specifications document is created for each individual dashboard or data product. While it may follow a global template (this document), the content is specific to the particular business problem, dataset, user group, and deployment environment it serves. This includes dashboards deployed on-premises, in cloud environments, or hybrid architectures, and those integrating AI/ML-driven insights.

The scope also includes defining the dashboard’s role within the broader data ecosystem, including its relationships to upstream data products, data contracts, and downstream consumers. It ensures alignment with enterprise data governance and operational frameworks such as MLOps, DataOps, and FinOps.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-13: Big Data & Data Science | The dashboard is often the primary vehicle for delivering insights from data science models, AI/ML outputs, and big data analytics, making this specification a critical input for the `Data Visualization Dashboard` output. It must consider AI governance and model explainability where applicable. |
| KA-11: Data Quality | The specification must define the data quality expectations for the dashboard, including thresholds and monitoring mechanisms. The dashboard itself often serves as a tool for monitoring data quality metrics and anomaly detection. |
| KA-09: Metadata Management | This document relies heavily on business and technical metadata (e.g., KPI definitions from the Business Glossary, data lineage) and also generates metadata about the dashboard itself, supporting discoverability and compliance. |
| KA-01: Data Governance | The specification must adhere to established data standards, policies, and compliance requirements including GDPR, HIPAA, CCPA, and the EU AI Act. The roles defined in the RASCI are governed by the overall governance framework, including emerging AI governance roles. |
| KA-06: Data Integration & Interoperability | Data source integration, data contracts, and data product interfaces are critical considerations in the data requirements and refresh strategies defined in this specification. |
| KA-14: Data Architecture | The dashboard design must align with the enterprise data architecture, including modern paradigms such as Data Mesh, Data Fabric, and Lakehouse architectures, ensuring scalability, security, and performance. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

This RASCI defines responsibilities for the creation and maintenance of this **Dashboard Specifications template itself** and the governance of its usage across projects.

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Analytics Manager (DA Mgr) | Ultimately answerable for the quality, completeness, and approval of the Dashboard Specifications document and template. Ensures it meets business needs, technical feasibility, and governance compliance. |
| **R (Responsible)** | BI Developer (BI Dev) | Responsible for gathering requirements, drafting the majority of the technical sections of the specification, including data mapping, functional requirements, and integration points. |
| **S (Supportive)** | Data Visualization Specialist (DataViz) | Supports the creation of the specification by providing expertise on visual design, user experience (UX), and best practices for data storytelling. Creates mockups and wireframes. |
| **C (Consulted)** | Business Users, Subject Matter Experts (SME) | Provide the core business requirements, define KPIs, validate logic, and give feedback on usability and design throughout the process. |
| **C (Consulted)** | Data Governance Manager (DG Mgr) | Consulted to ensure the specification complies with enterprise data standards, policies, AI governance frameworks, and regulatory requirements. |
| **I (Informed)** | Data Architect | Kept informed to ensure alignment with enterprise data architecture and integration standards. |
| **I (Informed)** | Security Officer / AI Ethics Officer | Informed to ensure compliance with security policies, data privacy, and ethical AI considerations. |

### 2.2. Section-Level RASCI (for Template Usage)

This RASCI applies when a team **fills out the template** for a specific dashboard project, ensuring clear accountability and review.

| Specification Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Business Requirements & KPIs | Business Analyst / SME | BI Dev, DataViz, Data Governance Manager | Business Owner / DA Mgr |
| Functional & Non-Functional Req. | BI Developer | SME, Data Architect, Security Officer | DA Mgr |
| Data Requirements & Mapping | BI Developer | Data Engineer, Data Steward, Data Architect | Data Owner / DA Mgr |
| Visual Design & Mockups | Data Visualization Specialist | Business Users, BI Dev | Business Owner |
| Final Specification Document | BI Developer | All Stakeholders | DA Mgr & Business Owner |

---

## 3. Template

> *The following is the standardized template for creating a Dashboard Specification. Replace all placeholders `[...]` with project-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Control

| Field | Value |
| :--- | :--- |
| Dashboard Name | [Official Name of the Dashboard or Data Product] |
| Document ID | SPEC-DASH-[YYYYMMDD]-[Unique ID] |
| Version | [e.g., 1.0] |
| Status | [Draft, In Review, Approved] |
| Business Owner | [Name and Title of the primary business stakeholder] |
| Development Lead | [Name and Title of the BI Developer, Data Product Manager, or DA Manager] |
| Creation Date | [YYYY-MM-DD] |
| Last Updated | [YYYY-MM-DD] |
| Data Product Owner | [Name and Title responsible for ongoing data product lifecycle] |
| AI Governance Reviewer | [Name and Title, if applicable] |

### 3.2. Overview & Business Purpose

> *Start with a concise summary. Explain the business problem this dashboard solves and the value it will provide. Clearly define the target audience and the key business questions they need to answer.*

- **Problem Statement**: [Describe the current challenge or opportunity. e.g., "Sales leadership lacks a consolidated, near real-time view of regional performance, leading to delayed decision-making and missed revenue targets."]
- **Target Audience**: [Be specific. e.g., "Regional Sales VPs, Country Sales Managers, Marketing Analysts"]
- **Key Business Questions**: 
  - [e.g., "How is my region performing against its quarterly sales target?"]
  - [e.g., "Which products are the top and bottom performers in my region?"]
  - [e.g., "Who are my top sales representatives by revenue and activity?"]
  - [e.g., "Are there any emerging trends or anomalies indicating risk or opportunity?"]
- **Business Value**: [Describe the expected impact, e.g., "Enable faster, data-driven decision-making, improve sales forecasting accuracy, and increase revenue by 5% within the next fiscal year."]
- **Alignment with Strategic Initiatives**: [Optional: Link to corporate or departmental strategic goals.]

### 3.3. Key Performance Indicators (KPIs) & Metrics

> *List every KPI and metric that will be displayed on the dashboard. For each, provide a precise definition, the calculation formula, the data source, and the desired visual representation. This is a critical section for avoiding misinterpretation.*

| KPI / Metric | Definition | Calculation / Logic | Data Source(s) | Desired Visualization |
| :--- | :--- | :--- | :--- | :--- |
| [e.g., Total Revenue] | [The total value of all closed-won deals in the selected period.] | `SUM(Opportunity.Amount) WHERE Opportunity.Status = 'Closed-Won'` | [Salesforce: Opportunity Object] | [Big Number with Trend Indicator] |
| [e.g., YTD Target Attainment] | [The percentage of the year-to-date sales target that has been achieved.] | `(YTD_Total_Revenue / YTD_Sales_Target) * 100` | [Salesforce, Anaplan] | [Gauge or Bullet Chart] |
| [e.g., Average Deal Size] | [The average revenue per closed-won deal.] | `AVG(Opportunity.Amount) WHERE Opportunity.Status = 'Closed-Won'` | [Salesforce: Opportunity Object] | [Big Number with Period-over-Period Comparison] |
| [e.g., AI Model Confidence Score] | [Average confidence score of the sales forecast model predictions.] | `AVG(ForecastModel.ConfidenceScore)` | [ML Platform API] | [Line Chart with Threshold Indicators] |

*Note: Include any AI/ML-derived KPIs with appropriate explanation and governance notes.*

### 3.4. Functional Requirements

> *Describe the interactive features of the dashboard. How will users interact with the data?*

- **Filters**: [List all filters users will need to slice the data.]
  - *Example: Date Range (default: current quarter), Region, Country, Product Line, Sales Rep, Customer Segment.*
- **Drill-Down / Drill-Through**: [Specify the drill paths.]
  - *Example: Users can click on a region in the map to see a detailed table of country-level performance. Clicking a country drills through to a separate Sales Rep leaderboard page.*
- **Tooltips/Hover-over**: [Define the additional context to be shown on hover.]
  - *Example: Hovering over a data point on a time-series chart shows the exact value, the previous period's value, and the % change.*
- **Exporting**: [Describe the required export functionality.]
  - *Example: Users must be able to export the underlying data of any chart to CSV. The entire dashboard view must be exportable to PDF.*
- **Alerts & Notifications**: [If applicable, describe any alerting mechanisms based on KPI thresholds.]
  - *Example: Email or in-app notifications triggered when sales drop below target or anomalies detected.*
- **Collaboration Features**: [If applicable, describe commenting, sharing, or annotation capabilities.]
- **Mobile Responsiveness**: [Specify if the dashboard must be accessible and usable on mobile devices.]

### 3.5. Data Requirements

> *Detail the backend data needs. This section is for the data engineers and BI developers.*

- **Data Sources**: [List all source systems, databases, or files.]
  - *Example: Salesforce (REST API), SAP S/4HANA (ODP Connector), Anaplan (API), Regional Targets (Excel file on SharePoint), AI/ML Model Outputs (ML Platform API).*
- **Data Model**: [Describe or link to the data model. e.g., a star schema diagram.]
  - *Example: A star schema with a central `fct_Sales` table and dimensions for `dim_Date`, `dim_Customer`, `dim_Product`, `dim_Geography`, and `dim_Sales_Team`.*
- **Source-to-Target Mapping**: [Provide detailed mapping for key fields from source to the target data model.]
  - *Input needed: `KA-06-source-to-target-mapping.md`*
- **Data Refresh Frequency**: [How often should the data be updated?]
  - *Example: The core sales data from Salesforce and SAP will be refreshed every 4 hours. The sales targets from Anaplan will be refreshed daily at 5 AM UTC. AI model outputs refreshed hourly.*
- **Data Volume & History**: [Estimate data volumes and the required historical depth.]
  - *Example: The dashboard should load the last 3 years of sales history. The initial data volume is ~50 million rows, with an expected growth of 2 million rows per month.*
- **Data Contracts & SLAs**: [Specify any data contracts or service level agreements governing data availability, quality, and timeliness.]
- **Data Privacy & Compliance**: [Note any data privacy considerations, masking, or anonymization required.]
- **Data Lineage & Provenance**: [Describe how data lineage will be tracked and documented for audit and governance.]

### 3.6. Visual Design & Layout (Wireframe)

> *Provide a visual mockup or wireframe of the dashboard. This is crucial for aligning on the user experience. This can be a low-fidelity drawing or a high-fidelity design from a tool like Figma. Annotate the wireframe to explain the purpose of each component.*

**[Insert or link to a wireframe image/document here]**

- **Layout**: [Describe the overall grid and placement of elements.]
  - *Example: The top row will contain KPI cards for the most important metrics. The left pane will house all filters. The main central area will contain the primary time-series and map visualizations.*
- **Chart Types**: [Justify the choice of chart for each metric.]
  - *Example: A line chart will be used for revenue over time to show trends. A bar chart will be used for comparing product performance as it's best for categorical comparison.*
- **Color Palette & Branding**: [Specify colors, fonts, and logos to be used, referencing the corporate style guide.]
  - *Input needed: Corporate Branding Guide.*
- **Accessibility Considerations**: [Specify any requirements for color contrast, font sizes, and screen reader compatibility.]
- **AI/ML Visualization Elements**: [If applicable, describe how AI-driven insights will be visually represented, including uncertainty or confidence indicators.]

### 3.7. Non-Functional Requirements

> *Define the technical constraints and quality attributes.*

- **Performance**: [Specify load time and interaction speed.]
  - *Example: Initial dashboard load time must be under 10 seconds. Filter interactions must update the view in under 3 seconds.*
- **Security & Access Control**: [Describe who can see what data.]
  - *Example: Row-level security must be implemented so that Regional VPs can only see data for their respective regions and the countries within them.*
- **Usability**: [Mention any specific usability requirements.]
  - *Example: The dashboard must be fully functional and readable on standard company laptops (1920x1080 resolution) and on iPads without horizontal scrolling.*
- **Scalability & Availability**: [Specify uptime requirements, concurrent user support, and scalability expectations.]
- **Compliance**: [Ensure compliance with GDPR, HIPAA, CCPA, EU AI Act, and any other relevant regulations.]
- **Auditability & Traceability**: [Define requirements for logging user interactions, data access, and changes to the dashboard.]
- **Maintainability**: [Specify requirements for ease of updates, version control, and documentation.]
- **Integration with DataOps/MLOps Pipelines**: [Describe how the dashboard fits into automated deployment and monitoring pipelines.]

---

## 4. Example

> *This is a filled-in example for a fictional company, TechCorp Ltd., for a "Customer Support Ticket Analysis" dashboard.*

### **4.1. Document Control**

| Field | Value |
| :--- | :--- |
| Dashboard Name | Customer Support Ticket Analysis Dashboard |
| Document ID | SPEC-DASH-20260208-001 |
| Version | 1.0 |
| Status | Approved |
| Business Owner | Jane Doe, VP of Customer Success |
| Development Lead | John Smith, BI Manager |
| Data Product Owner | Emily Chen, Data Product Manager |
| AI Governance Reviewer | Michael Lee, AI Ethics Officer |

### **4.2. Overview & Business Purpose**

- **Problem Statement**: The Customer Success leadership team has limited visibility into support ticket trends, agent performance, and customer satisfaction. Analysis is done manually in spreadsheets, is often days out of date, and cannot be easily segmented or correlated with AI-driven sentiment analysis.
- **Target Audience**: VP of Customer Success, Support Team Leads, Senior Support Agents.
- **Key Business Questions**:
  - What is our average First Response Time (FRT) and Time to Resolution (TTR)?
  - Which ticket categories are generating the most volume?
  - How is our Customer Satisfaction (CSAT) score trending over time?
  - Who are our most productive agents?
  - Are there any emerging negative sentiment trends detected by AI models?
- **Business Value**: Enable proactive support management, improve customer satisfaction, reduce resolution times, and leverage AI insights for early issue detection.

### **4.3. Key Performance Indicators (KPIs) & Metrics**

| KPI / Metric | Definition | Calculation / Logic | Data Source(s) | Desired Visualization |
| :--- | :--- | :--- | :--- | :--- |
| Avg. First Response Time (FRT) | The average time in business hours from when a ticket is created to the first public agent response. | `AVG(Ticket.first_response_at - Ticket.created_at)` | [Zendesk] | [Big Number with Trend] |
| Avg. Time to Resolution (TTR) | The average time in business hours from when a ticket is created until it is solved. | `AVG(Ticket.solved_at - Ticket.created_at)` | [Zendesk] | [Big Number with Trend] |
| CSAT Score | The average customer satisfaction score from post-ticket surveys. | `AVG(Survey.score) WHERE Survey.question = 'CSAT'` | [Zendesk, SurveyMonkey] | [Line Chart over Time] |
| Ticket Volume | The total number of new tickets created in the period. | `COUNT(Ticket.id)` | [Zendesk] | [Bar Chart by Day/Week] |
| Sentiment Score | Average AI-derived sentiment score from ticket text analysis. | `AVG(SentimentModel.Score)` | [AI Platform] | [Heatmap by Category] |

### **4.4. Functional Requirements**

- **Filters**: Date Range, Channel (Email, Web, Phone), Priority (Low, Normal, High, Urgent), Team Lead, Agent, Sentiment Category.
- **Drill-Down**: Users can click on a ticket category bar to see a detailed table of all tickets within that category for the selected period. Clicking on sentiment heatmap cells drills down to ticket details with AI annotations.
- **Exporting**: Export underlying data to CSV and dashboard snapshots to PDF.
- **Alerts**: Email alerts triggered when average FRT exceeds SLA thresholds or negative sentiment spikes.
- **Collaboration**: Commenting enabled on key charts for team discussions.

### **4.5. Data Requirements**

- **Data Sources**: Zendesk API (Tickets, Users, Organizations), SurveyMonkey API (CSAT Surveys), AI Platform API (Sentiment Analysis).
- **Data Model**: Star schema with `fct_Tickets` and dimensions for `dim_Date`, `dim_Agent`, `dim_Customer`, `dim_Ticket_Attributes`.
- **Data Refresh Frequency**: Zendesk data refreshed every 1 hour. SurveyMonkey data refreshed every 6 hours. AI sentiment scores refreshed every 2 hours.
- **Data Volume & History**: Last 2 years of ticket data, approximately 10 million records.

### **4.6. Visual Design & Layout (Wireframe)**

*(A wireframe image would be embedded here showing a top row of KPI cards for FRT, TTR, and CSAT. Below, a large line chart shows ticket volume and CSAT over time. To the right, two bar charts show tickets by category and tickets by channel. A sentiment heatmap is positioned below with drill-down capability.)*

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Data Contracts | Concept | [data-contracts.md](references/concepts-modern-paradigms.md) |
| AI Governance | Knowledge Area | KA-XX-ai-governance.md |
| Data Mesh Fundamentals | Guide | **guides/data-architecture/data-mesh.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria (Checklist)

- [ ] All KPIs listed in Section 3.3 are present on the dashboard.
- [ ] The calculation for each KPI has been validated against the source system by a business analyst.
- [ ] All filters and drill-down paths defined in Section 3.4 function as expected.
- [ ] Row-level security has been tested and confirmed to work for all user roles.
- [ ] The dashboard load time is under the 10-second threshold on the production server.
- [ ] The dashboard meets accessibility standards (e.g., WCAG 2.1).
- [ ] The dashboard complies with all relevant data governance and AI governance policies.
- [ ] The dashboard has been signed off by the Business Owner (Jane Doe).
- [ ] AI/ML-driven insights have been reviewed and approved by the AI Ethics Officer.
- [ ] Data lineage and provenance are documented and traceable.

### 5.2. Review Checklist

| Area | Question | Reviewer |
| :--- | :--- | :--- |
| **Business Alignment** | Does the dashboard directly answer the key business questions defined in Section 3.2? | Business Owner |
| **Data Integrity** | Are the data sources reliable? Is the refresh frequency appropriate for the business need? Are data quality thresholds met? | Data Engineer |
| **Clarity & UX** | Are the chart choices appropriate? Is the layout intuitive and easy to understand for the target audience? | DataViz Specialist |
| **Technical Feasibility** | Are the performance and security requirements achievable with the current BI platform and data architecture? | BI Architect |
| **Governance & Compliance** | Does the dashboard comply with data governance, privacy, and AI governance policies? | Data Governance Manager |
| **Ethical AI** | Are AI/ML insights presented transparently with appropriate disclaimers and confidence indicators? | AI Ethics Officer |
| **Operational Readiness** | Are deployment, monitoring, and maintenance plans in place? | DataOps/MLOps Engineer |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs to this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| BI Standards | Provides the approved color palettes, fonts, and chart usage guidelines that must be followed in the dashboard design. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Report Specifications | May provide the basis for some visualizations or data requirements if the dashboard is replacing an existing report. | `templates/templates-KA-08-data-warehousing-bi.md` |
| KPI Definitions | Provides the authoritative definitions and calculation logic for enterprise-wide KPIs used in the dashboard. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Data Contracts | Defines the formal agreements on data interfaces and quality between source systems and the dashboard. | `#` |
| AI Governance Framework | Provides policies and guidelines for AI/ML model integration and ethical considerations. | `#` |

### 6.2. Consumers (Outputs that use this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Visualization Dashboard | This specification document is the direct input for the creation of the actual dashboard, which is a data visualization output. | `templates/templates-KA-13-big-data-data-science.md` |
| Data Product Catalog Entry | The dashboard specification informs the metadata and documentation for the data product catalog. | `templates/templates-KA-09-metadata-management.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **BI & Visualization** | Tableau, Power BI, Qlik Sense, Looker | Apache Superset, Metabase, Grafana |
| **Wireframing & Design** | Figma, Sketch, Adobe XD | diagrams.net (formerly Draw.io), Pencil Project |
| **Data Modeling** | Erwin, ER/Studio | dbt (for transformation modeling) |
| **Requirement Mgt.** | Jira, Confluence, Azure DevOps | Trello, Asana (Free tiers) |
| **AI Model Monitoring** | DataRobot MLOps, Seldon Core | MLflow, Kubeflow Pipelines |

### 7.2. Automation Opportunities

- **Automated Testing**: The data validation and KPI calculation checks can be automated using SQL-based testing frameworks (e.g., dbt tests) or Python scripts that run as part of the data pipeline. This ensures data accuracy after every refresh.
- **Performance Monitoring**: Automated alerts can be configured to trigger if the dashboard load time or query performance exceeds the defined thresholds in the non-functional requirements.
- **Specification Generation**: For simpler, standardized dashboards, parts of this specification document (like the data dictionary or source mapping) could be auto-generated from metadata stored in a data catalog tool.
- **AI Governance Automation**: Integration with AI governance platforms to automatically validate model compliance, fairness, and explainability metrics before dashboard deployment.
- **Version Control & CI/CD**: Use of version control systems (e.g., Git) and continuous integration/continuous deployment pipelines to automate specification updates, testing, and deployment.
- **Metadata Synchronization**: Automated synchronization of dashboard metadata with enterprise metadata repositories to ensure up-to-date lineage and impact analysis.

---

## 8. References

- **[1]** DAMA-DMBOK, 2nd Edition, Chapter 11: Data Warehousing and Business Intelligence.
- **[2]** DAMA-DMBOK 3.0 (forthcoming), Chapter on Data Products and AI Governance (expected June 2025).
- **[3]** Internal Document: `templates/templates-KA-01-data-governance.md`
- **[4]** Internal Document: `references/reference-materials.md`
- **[5]** EU AI Act Compliance Guidelines, Internal Policy Document.
- **[6]** Data Mesh Principles and Practices, Guide: `references/concepts-modern-paradigms.md`
- **[7]** AI Governance Framework, Knowledge Area: `#`


---

# KPI Definitions


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. KPI Identification](#31-kpi-identification)
  - [3.2. Business Context](#32-business-context)
  - [3.3. Technical Specification](#33-technical-specification)
  - [3.4. Dimensions and Granularity](#34-dimensions-and-granularity)
  - [3.5. Targets and Reporting](#35-targets-and-reporting)
  - [3.6. Ownership and Governance](#36-ownership-and-governance)
- [4. Example](#4-example)
  - [4.1. KPI Identification (Example)](#41-kpi-identification-example)
  - [4.2. Business Context (Example)](#42-business-context-example)
  - [4.3. Technical Specification (Example)](#43-technical-specification-example)
  - [3.4. Dimensions and Granularity (Example)](#34-dimensions-and-granularity-example)
  - [3.5. Targets and Reporting (Example)](#35-targets-and-reporting-example)
  - [3.6. Ownership and Governance (Example)](#36-ownership-and-governance-example)
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

**KPI Definitions** is a formal, authoritative document that specifies the precise calculation, data sources, business logic, ownership, and governance of each Key Performance Indicator (KPI) used within a data product, such as reports, dashboards, or analytical models. A KPI is a quantifiable measure that reflects how effectively an organization is achieving its strategic and operational objectives.

This document serves as a critical artifact in establishing a trusted, single source of truth for business metrics, ensuring alignment and clarity across diverse stakeholders including data analysts, business leaders, data stewards, and technical teams.

> The purpose of the KPI Definitions document is to eliminate ambiguity, foster trust in data, and enable consistent decision-making by translating strategic business goals into measurable, consistent, and universally understood indicators of performance. It also supports compliance, auditability, and continuous improvement in data-driven environments.

In the evolving landscape of data management, KPI definitions increasingly incorporate considerations for AI governance, data productization, and cloud-native architectures. This ensures that KPIs remain relevant and reliable in environments leveraging Data Mesh, Data Fabric, and Lakehouse patterns, and that they comply with emerging regulations such as the EU AI Act alongside GDPR, HIPAA, and CCPA.

### 1.2. Scope

**Per Product** — This deliverable is created for each individual data product (e.g., a specific sales dashboard, marketing campaign analysis report, or AI-driven recommendation engine). While some KPIs may be reused across products, a dedicated KPI Definitions document is required to provide context and specify any product-specific nuances in calculation, presentation, or governance.

The scope includes not only traditional KPIs but also extends to AI/ML model performance indicators, operational metrics, and data product health metrics, reflecting the integration of MLOps, DataOps, and FinOps practices.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Business Glossary (KA-01) provides standardized definitions for business terms used within KPIs, ensuring consistency and alignment with governance policies. This document is a key artifact of a governed data environment and supports compliance with data and AI governance frameworks. |
| KA-03: Data Modeling & Design | Logical and physical data models define the entities and attributes that serve as the source for KPI calculations. Modeling decisions impact KPI accuracy, granularity, and performance. |
| KA-06: Data Integration | Source-to-Target mapping and data lineage documents (KA-06) are critical inputs for tracing the origin and transformation of data used in KPIs, supporting transparency and auditability. |
| KA-11: Data Quality | The metrics defined here often underpin Data Quality Metrics (KA-11) to monitor the health of underlying data. Trustworthiness of KPIs depends directly on data quality and completeness. |
| KA-08: Data Warehousing and Business Intelligence | KPI definitions are foundational to BI reporting, dashboarding, and analytics design, enabling consistent metric calculation and visualization. |
| KA-12: Artificial Intelligence and Machine Learning | As AI governance matures, KPIs increasingly include AI model performance and fairness metrics, requiring integration with AI governance frameworks and ethical considerations. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Analytics Manager (DA Mgr) | Ultimately accountable for the accuracy, completeness, and approval of the KPI definitions for a given data product. Ensures alignment with business strategy, governance policies, and compliance requirements. |
| **R (Responsible)** | Data Analyst (D-Analyst) | Responsible for gathering requirements from business stakeholders, drafting the KPI definitions, performing data validation, and maintaining the document. Ensures clarity and precision in the definition. |
| **S (Supportive)** | BI Developer (BI Dev), Data Engineer | Supports the process by implementing the KPI logic in BI tools or data pipelines, validating technical feasibility, optimizing queries, and ensuring performance and scalability. |
| **C (Consulted)** | Business Leaders, Subject Matter Experts (SME), AI Ethics Officer | Consulted to provide business context, define strategic goals, set targets, validate KPI definitions, and ensure alignment with ethical and regulatory frameworks, including AI governance. |
| **I (Informed)** | Chief Data Officer (CDO), Chief AI Officer (CAIO) | Kept informed of key metrics used to run the business and AI initiatives, ensuring alignment with enterprise-wide data and AI governance strategies. |

### 2.2. Section-Level RASCI

| Template Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| KPI Business Details (Name, Goal) | D-Analyst | Business Leaders, SME | DA Mgr |
| KPI Technical Details (Formula, Source) | D-Analyst | BI Dev, Data Engineer | DA Mgr |
| Targets and Thresholds | D-Analyst | Business Leaders, SME | DA Mgr |
| Ownership and Reporting | D-Analyst | SME, AI Ethics Officer | DA Mgr |

---

## 3. Template

> *The following is the standardized template for defining a Key Performance Indicator. Fill out one instance of this template for each KPI included in the data product.*

### 3.1. KPI Identification

| Field | Value |
| :--- | :--- |
| **KPI Name** | `[Enter the full, official name of the KPI]` |
| **KPI ID** | `[Assign a unique identifier, e.g., KPISL001]` |
| **Version** | `[e.g., 1.0]` |
| **Status** | `[Proposed, Active, Deprecated]` |
| **Date Created** | `[YYYY-MM-DD]` |
| **Last Updated** | `[YYYY-MM-DD]` |

### 3.2. Business Context

> *This section explains the business relevance of the KPI. It connects the metric to strategic goals and defines its purpose in plain language.*

**Description**  
> *Provide a clear, concise definition of the KPI. What does it measure and why is it important?*  

[Enter KPI Description]

**Business Goal Alignment**  
> *Which strategic business objective does this KPI measure? Refer to the corporate or departmental strategic plan.*  

[e.g., "Increase customer loyalty and lifetime value"]

**Regulatory and Compliance Considerations**  
> *Specify any regulatory or compliance requirements relevant to this KPI, such as GDPR, HIPAA, CCPA, or EU AI Act.*  

[e.g., "Data used must comply with GDPR data minimization principles."]

### 3.3. Technical Specification

> *This section provides the unambiguous technical details required to calculate the KPI. It should be detailed enough for a developer or data engineer to implement it correctly.*

**Formula / Calculation Logic**  
> *Provide the precise mathematical formula. Define each component of the formula. For complex logic, use pseudocode or a numbered list of steps.*  

[e.g., `(Total Revenue from a Customer Segment) / (Total Number of Customers in that Segment)`]

**Data Source(s)**  
> *List the specific source systems, databases, tables, and columns required to calculate the KPI. Include filters, criteria, and data freshness.*  

| System | Database/Schema | Table(s) | Column(s) | Filters/Criteria | Data Freshness |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., ERP] | [e.g., `prod_db`] | [e.g., `orders`, `customers`] | [e.g., `order_total`, `customer_id`] | [e.g., `order_status = 'Completed'`] | [e.g., Daily at 2 AM] |

**Data Lineage Reference**  
> *Provide a link to the relevant Source-to-Target Mapping or Data Lineage document.*  

[Link to `templates/templates-KA-06-data-integration-interoperability.md`]

**Data Mesh / Fabric Considerations**  
> *If applicable, specify how this KPI leverages data products or contracts in a Data Mesh or Data Fabric architecture.*  

[e.g., "This KPI consumes data product 'Customer Transactions' managed by the Sales domain team."]

### 3.4. Dimensions and Granularity

> *Describe how the KPI can be segmented or broken down for deeper analysis.*

**Recommended Dimensions**  
> *List the business dimensions by which this KPI should be analyzed (e.g., by Product, Region, Time, Customer Segment).*  

- [e.g., Time (Day, Week, Month, Quarter, Year)]  
- [e.g., Geography (Country, Region, City)]  
- [e.g., Product (Category, SKU)]  
- [e.g., Customer Segment (New, Returning, VIP)]  

**Data Granularity**  
> *What is the lowest level of detail at which the data is captured?*  

[e.g., "Individual transaction line item"]

**Aggregation Rules**  
> *Specify any rules or constraints on aggregating data across dimensions to maintain KPI integrity.*  

[e.g., "Exclude test transactions and internal transfers from aggregation."]

### 3.5. Targets and Reporting

> *This section defines what "good" looks like and how the KPI will be presented to users.*

**Targets and Thresholds**  
> *Define the performance targets. Thresholds indicate different levels of performance (e.g., Poor, Good, Excellent). Include rationale if available.*  

| Performance Level | Threshold | Description |
| :--- | :--- | :--- |
| Excellent | `[e.g., > $550]` | Exceeds expectations and drives significant value. |
| Good (Target) | `[e.g., $500 - $550]` | Meets the business objective. |
| Poor | `[e.g., < $500]` | Below target, requires investigation or action. |

**Reporting Frequency**  
> *How often should this KPI be calculated and reported?*  

[e.g., Daily, Weekly, Monthly]

**Default Visualization**  
> *What is the recommended chart or visualization type for this KPI?*  

[e.g., Line chart over time, Bar chart comparing regions]

**Alerting and Threshold Management**  
> *Specify if automated alerts should be triggered when thresholds are crossed, including communication channels.*  

[e.g., "Send Slack alert to Sales leadership if KPI falls below Poor threshold."]

### 3.6. Ownership and Governance

> *This section clarifies roles and responsibilities for the ongoing management of the KPI.*

| Role | Assigned Person/Team | Responsibilities |
| :--- | :--- | :--- |
| **Business Owner** | `[The person accountable for the business outcome, e.g., VP of Sales]` | Owns the business definition, ensures KPI aligns with strategic goals, and acts on insights. |
| **Technical Owner** | `[The team responsible for the data pipeline and technical implementation, e.g., BI Team]` | Maintains data pipelines, implements calculation logic, ensures data availability and performance. |
| **Data Steward** | `[The person responsible for data quality and definition, e.g., Sales Data Steward]` | Ensures data quality, consistency, and compliance with governance policies. |
| **AI Ethics Officer** | `[If applicable, responsible for ethical considerations related to AI-driven KPIs]` | Reviews KPI for ethical implications, bias, and compliance with AI governance frameworks. |

---

## 4. Example

> *This is a realistic, filled-in example for a fictional e-commerce company, GlobalRetail Inc. This KPI is part of the "Quarterly Sales Performance Dashboard".*

### 4.1. KPI Identification (Example)

| Field | Value |
| :--- | :--- |
| **KPI Name** | Average Order Value (AOV) |
| **KPI ID** | KPIFIN003 |
| **Version** | 1.2 |
| **Status** | Active |
| **Date Created** | 2023-11-15 |
| **Last Updated** | 2024-04-10 |

### 4.2. Business Context (Example)

**Description**  
Average Order Value (AOV) measures the average dollar amount spent each time a customer places an order on the GlobalRetail Inc. website. It is a key indicator of customer purchasing behavior. A higher AOV indicates that customers are buying more expensive items or more items per order, which directly increases revenue without necessarily increasing the number of customers.

**Business Goal Alignment**  
"Increase revenue per customer and maximize profitability."

**Regulatory and Compliance Considerations**  
Data used complies with GDPR data minimization principles; no personal identifiable information (PII) is included in the calculation.

### 4.3. Technical Specification (Example)

**Formula / Calculation Logic**  
`SUM(order_total_usd) / COUNT(DISTINCT order_id)`

1. Filter all transactions for the specified time period.  
2. Sum the `order_total_usd` for all completed orders.  
3. Count the number of unique `order_id`s for the same set of orders.  
4. Divide the total revenue by the count of unique orders.

**Data Source(s)**

| System | Database/Schema | Table(s) | Column(s) | Filters/Criteria | Data Freshness |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E-commerce Platform | `prod_analytics` | `fct_orders` | `order_total_usd`, `order_id` | `order_status = 'COMPLETED'` AND `is_test_order = false` | Daily at 2 AM |

**Data Lineage Reference**  
[Link to `templates/templates-KA-06-data-integration-interoperability.md#fct_orders`]

**Data Mesh / Fabric Considerations**  
This KPI consumes the data product 'Customer Transactions' owned by the Sales domain team, accessed via the enterprise data fabric platform.

### 3.4. Dimensions and Granularity (Example)

**Recommended Dimensions**  
- Time (Month, Quarter)  
- Geography (Country)  
- Marketing Channel (e.g., Organic Search, Paid Social, Email)  
- Customer Segment (e.g., New, Returning)

**Data Granularity**  
Individual completed order.

**Aggregation Rules**  
Exclude test transactions and internal transfers from aggregation.

### 3.5. Targets and Reporting (Example)

**Targets and Thresholds**

| Performance Level | Threshold | Description |
| :--- | :--- | :--- |
| Excellent | `> $125` | Indicates successful up-selling/cross-selling initiatives. |
| Good (Target) | `$115 - $125` | On track with quarterly revenue goals. |
| Poor | `< $115` | Marketing and sales strategies may need review. |

**Reporting Frequency**  
Weekly

**Default Visualization**  
Combination chart: Line chart showing AOV over time, with bars representing total revenue.

**Alerting and Threshold Management**  
Slack alerts sent to Sales leadership if AOV falls below $115.

### 3.6. Ownership and Governance (Example)

| Role | Assigned Person/Team |
| :--- | :--- |
| **Business Owner** | VP of E-commerce |
| **Technical Owner** | BI & Analytics Team |
| **Data Steward** | E-commerce Data Steward |
| **AI Ethics Officer** | AI Governance Office |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [tools-landscape.md](references/reference-materials.md) |
| Metrics Kpis | Reference | [metrics-kpis.md](references/reference-materials.md) |
| Business Glossary | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| Data Lineage | Deliverable | **templates/templates-KA-06-data-integration-interoperability.md** |
| Report Specifications | Deliverable | [07-report-specifications.md](07-report-specifications.md) |
| Dashboard Specifications | Deliverable | [08-dashboard-specifications.md](08-dashboard-specifications.md) |
| Data Quality Metrics | Deliverable | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |
| AI Governance Framework | Knowledge Area | **templates/templates-KA-12-data-handling-ethics.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] KPI has a clear, unambiguous name and definition aligned with the Business Glossary (KA-01).  
- [x] KPI is directly linked to a documented business goal and strategic objectives.  
- [x] Calculation logic is precise, mathematically correct, and implementable.  
- [x] All data sources, tables, columns, filters, and business rules are explicitly identified and documented.  
- [x] Data lineage and source-to-target mappings are referenced to support traceability.  
- [x] Performance targets and thresholds are defined and agreed upon with business owners and stakeholders.  
- [x] Roles for Business Owner, Technical Owner, Data Steward, and AI Ethics Officer (if applicable) are assigned.  
- [x] Reporting frequency, visualization type, and alerting mechanisms are specified.  
- [x] Compliance and regulatory considerations are documented.  
- [x] The KPI supports scalability and integration within modern architectures such as Data Mesh or Data Fabric.  
- [x] The document is version-controlled and maintained as a living artifact.  

### 5.2. Review Checklist

| Review Area | Question | Reviewer Role |
| :--- | :--- | :--- |
| **Business Alignment** | Does this KPI accurately measure progress towards a strategic goal? | Business Leader, DA Mgr |
| **Clarity** | Is the definition understandable to a non-technical audience? | SME, D-Analyst |
| **Feasibility** | Can this KPI be reliably and performantly calculated with available data? | BI Dev, Data Engineer |
| **Consistency** | Does the terminology align with the official Business Glossary? | Data Steward |
| **Actionability** | Can a change in this KPI trigger a specific business action or decision? | Business Leader, SME |
| **Governance Compliance** | Does the KPI comply with relevant data governance, AI governance, and regulatory requirements? | Data Steward, AI Ethics Officer |
| **Technical Scalability** | Is the KPI calculation optimized for cloud-native, multi-cloud, or distributed data architectures? | Data Engineer, BI Dev |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | Path / Description | Purpose |
| :--- | :--- | :--- |
| Business Requirements | Project documentation or stakeholder interviews | Provides the strategic goals and analytical questions that KPIs are designed to answer. |
| Business Glossary | `templates/templates-KA-01-data-governance.md` | Ensures that the terms used in KPI names and definitions are consistent across the organization. |
| Source-to-Target Mapping | `templates/templates-KA-06-data-integration-interoperability.md` | Documents data lineage and transformation logic underpinning KPI calculations. |
| Data Quality Reports | `templates/templates-KA-11-data-quality.md` | Provides insight into data quality impacting KPI reliability. |

### 6.2. Consumers (Outputs)

| Output Name | Path | Purpose |
| :--- | :--- | :--- |
| Report Specifications | `07-report-specifications.md` | The KPI definitions are embedded within report designs to explain how metrics are calculated. |
| Dashboard Specifications | `08-dashboard-specifications.md` | KPI definitions are used to build the data models and visualizations for interactive dashboards. |
| Data Quality Metrics | `templates/templates-KA-11-data-quality.md` | The logic from KPI definitions is often adapted to create metrics that monitor the quality of the source data. |
| Data Product Specifications | `07-report-specifications.md`, `08-dashboard-specifications.md` | The KPI definitions are a key input for creating detailed specifications for data products like reports and dashboards. |
| AI Model Performance Reports | `templates/templates-KA-12-data-handling-ethics.md` | KPIs related to AI/ML model outcomes and fairness metrics. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **BI & Visualization** | Tableau, Power BI, Looker, Qlik Sense | Apache Superset, Metabase, Grafana |
| **Data Catalog & Governance** | Collibra, Alation, Atlan | Amundsen, DataHub |
| **Data Transformation** | dbt Cloud, Informatica | dbt Core, Apache Airflow |
| **Collaboration & Documentation** | Confluence, SharePoint, Notion | Wiki.js, BookStack |
| **AI Governance & Monitoring** | IBM Watson OpenScale, Fiddler AI | OpenLineage, MLflow |

### 7.2. Automation Opportunities

- **Automated KPI Reporting**: BI tools can be configured to automatically refresh data, calculate KPIs, and distribute dashboards via email or embedded portals on a set schedule, supporting near real-time decision-making.  
- **Data Catalog Integration**: KPI definitions can be automatically ingested into a data catalog from a version-controlled repository (e.g., Git). This allows users to discover and understand KPIs directly within their data exploration tools, supporting data mesh principles.  
- **Alerting and Threshold Monitoring**: Automated alerts can be configured to notify business owners via Slack, email, or other collaboration platforms when a KPI crosses a predefined threshold, enabling proactive response and operational agility.  
- **Metric-to-Code Generation**: The technical specifications in this document can be used as a basis to auto-generate SQL, dbt model code, or pipeline scripts required to produce the KPI, reducing manual development effort and errors.  
- **AI Model KPI Integration**: Integration with MLOps platforms to automatically track and report AI model KPIs such as accuracy, bias, and drift, ensuring continuous monitoring and governance.  
- **Version Control and Change Management**: Use of Git or similar tools to manage KPI definition versions, track changes, and enable collaborative editing with audit trails.  

---

## 8. References

| Ref | Description |
| :-- | :--- |
| [1] | DAMA-DMBOK (Data Management Body of Knowledge), 2nd Edition, Chapter 11: Data Warehousing and Business Intelligence. |
| [2] | DAMA-DMBOK 3.0 (In Development, Community-Driven Rebuild, Launch June 2025) - Future enhancements include AI governance integration, data product focus, and modern architectures. |
| [3] | Internal document: `references/reference-materials.md` for detailed role descriptions. |
| [4] | Internal document: `templates/templates-KA-01-data-governance.md` for standard business term definitions. |
| [5] | EU AI Act and GDPR compliance guidelines for data and AI governance. |
| [6] | AI Governance Framework and Best Practices: `templates/templates-KA-12-data-handling-ethics.md` |


---

# Source System Analysis


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Control](#31-document-control)
  - [3.2. Executive Summary](#32-executive-summary)
  - [3.3. System Overview](#33-system-overview)
  - [3.4. Data Scope and Objects for Analysis](#34-data-scope-and-objects-for-analysis)
  - [3.5. Data Profiling and Quality Assessment](#35-data-profiling-and-quality-assessment)
  - [3.6. Data Access and Extraction Plan](#36-data-access-and-extraction-plan)
  - [3.7. Data Dictionary and Semantics](#37-data-dictionary-and-semantics)
  - [3.8. Risks and Recommendations](#38-risks-and-recommendations)
- [4. Example](#4-example)
  - [**Document Control**](#document-control)
  - [**System Overview**](#system-overview)
  - [**Data Scope and Objects for Analysis**](#data-scope-and-objects-for-analysis)
  - [**Data Profiling and Quality Assessment**](#data-profiling-and-quality-assessment)
  - [**Data Access and Extraction Plan**](#data-access-and-extraction-plan)
  - [**Data Dictionary and Semantics**](#data-dictionary-and-semantics)
  - [**Risks and Recommendations**](#risks-and-recommendations)
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

**Source System Analysis** is the comprehensive process of investigating, documenting, and understanding the systems that serve as the original sources of data for data warehousing, business intelligence (BI), advanced analytics, or any data integration initiative. This analysis involves a detailed examination of the source system’s data structures, content, data quality, constraints, metadata, and the technical mechanisms for accessing and extracting data. It also includes assessing the system’s operational characteristics, data governance posture, and compliance with regulatory requirements.

The primary purpose of Source System Analysis is to:

- Determine the suitability and fitness-for-use of source data for its intended analytical or operational purpose.
- Identify potential risks, data quality issues, and technical challenges in data extraction and integration.
- Provide the necessary information and metadata to design robust, scalable, and maintainable data pipelines and integration processes.
- Support compliance with data governance, privacy, and AI governance frameworks by understanding data lineage, sensitivity, and usage constraints.
- Facilitate alignment with modern data architectures such as data mesh and data fabric by clarifying data product boundaries, data contracts, and stewardship responsibilities.

> A thorough Source System Analysis is the bedrock of a successful data warehousing, BI, or data product initiative. It prevents costly rework, data quality disasters, and project delays by ensuring a deep understanding of the raw materials—the source data—before any construction begins. In the era of cloud-native architectures, data mesh, and AI-driven analytics, this foundational step ensures that data products are trustworthy, compliant, and aligned with enterprise data governance and AI ethics standards.

> **Forward-Looking Note (DAMA-DMBOK 3.0):** The upcoming DAMA-DMBOK 3.0 emphasizes the integration of AI governance and data product thinking into traditional data management practices. Source System Analysis will increasingly incorporate AI model input data assessments, data contracts, and agentic data stewardship roles to ensure ethical, compliant, and high-quality data supply chains. This includes assessing data bias, lineage transparency, and compliance with emerging regulations such as the EU AI Act.

### 1.2. Scope

**Per Product and Contextualized** — Source System Analysis is conducted for each individual data product or data-intensive project. While some high-level characteristics of a source system might be reusable across projects, a detailed analysis is always specific to the data elements, business context, and consumption patterns required by the target data product or analytical use case.

This analysis extends beyond traditional relational databases to include APIs, streaming platforms, cloud data lakes, SaaS applications, and emerging data sources such as IoT devices or AI model outputs. It also considers modern data architectures including data mesh and data fabric environments, ensuring that data contracts, data products, and stewardship responsibilities are clearly understood and documented.

The scope also includes evaluation of:

- Data access patterns and extraction methods aligned with cloud-native and hybrid environments.
- Data quality and profiling with an emphasis on monitoring data drift and anomalies that impact AI/ML model performance.
- Compliance with data privacy laws (GDPR, HIPAA, CCPA) and AI-specific regulations (EU AI Act).
- Integration of MLOps, DataOps, and FinOps considerations where applicable.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-02: Data Architecture | Provides critical input for creating and validating data flow diagrams, data landscape maps, and architectural decisions, especially in multi-cloud and hybrid environments. Supports understanding of data mesh and data fabric implementations. |
| KA-03: Data Modeling & Design | Findings inform logical and physical data model design, including semantic consistency and alignment with business glossaries. Supports design of data products and data contracts. |
| KA-06: Data Integration & Interoperability | Serves as the foundational blueprint for designing ETL/ELT processes, source-to-target mappings, and data contracts. Includes modern integration patterns such as CDC, event streaming, and API-based ingestion. |
| KA-09: Metadata Management | Generates technical and business metadata that must be captured, managed, and integrated into data catalogs and lineage tools. Supports AI governance by documenting data provenance and transformations. |
| KA-10: Data Governance | Supports data stewardship, compliance with data policies, and AI governance by documenting data sensitivity, usage constraints, and lineage. Includes agentic stewardship roles and data product ownership. |
| KA-11: Data Quality | Includes initial data quality assessments that guide cleansing, validation, and monitoring strategies. Emphasizes continuous quality monitoring and data drift detection for AI/ML readiness. |
| KA-12: Document & Content Management | Documentation standards and version control practices ensure traceability and auditability of the analysis artifacts. Supports compliance and audit readiness. |

> **Forward-Looking Note (DAMA-DMBOK 3.0):** The integration of AI governance and data product management will require Source System Analysis to explicitly document data contracts, AI model input data characteristics, and stewardship responsibilities, reflecting the evolving enterprise data ecosystem.

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Integration Manager (DI Mgr) | Ultimately accountable for the completeness, accuracy, and timely delivery of the Source System Analysis. Ensures alignment with project objectives, enterprise data governance, and AI ethics standards. |
| **R (Responsible)** | Data Engineer (D-Eng) | Executes the detailed analysis, including data profiling, technical investigation, documentation, and coordination with stakeholders. Ensures technical feasibility and compliance with modern data architectures. |
| **S (Supportive)** | Data Quality Analyst (DQ Analyst) | Provides expertise, tools, and support for data profiling, quality assessment, and remediation recommendations. Supports continuous quality monitoring and anomaly detection. |
| **C (Consulted)** | Data Steward (D-Steward), Subject Matter Expert (SME), Source System Administrator | Provide business context, data semantics, system operational insights, and validation of findings. Engage in defining data contracts and stewardship roles. |
| **I (Informed)** | Data Warehouse Architect (DW Arch), Data Governance Officer, AI Ethics Officer | Kept informed of findings to ensure architectural compatibility, governance compliance, and AI ethics considerations. AI Ethics Officer involvement is critical when source data feeds AI/ML models. |

### 2.2. Section-Level RASCI

| Analysis Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| System Overview & Architecture | D-Eng | DW Arch, SME, Source Admin | DI Mgr |
| Data Profiling & Quality Assessment | D-Eng | DQ Analyst, D-Steward | DI Mgr |
| Data Access & Extraction Plan | D-Eng | Source Admin, Security Officer | DI Mgr |
| Data Dictionary & Semantics | D-Eng | D-Steward, SME | DI Mgr |
| Risks and Recommendations | D-Eng | DI Mgr, Data Governance Officer, AI Ethics Officer | DI Mgr |

> **Practical Guidance:**  
> - Engage SMEs and Data Stewards early to validate business definitions and data semantics.  
> - Include AI Ethics Officer when source data is used for AI/ML models to address bias, fairness, and compliance risks.  
> - Ensure security and privacy teams review access plans and extraction methods for compliance with GDPR, HIPAA, CCPA, and emerging regulations like the EU AI Act.  
> - Collaborate with Data Product Managers and Data Contract Owners in data mesh environments to ensure alignment with product SLAs and stewardship expectations.

---

## 3. Template

> *The following is the standardized template for conducting and documenting a Source System Analysis. Replace all placeholders `[...]` with project-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Control

| Field | Value |
| :--- | :--- |
| Document Title | Source System Analysis: [Source System Name] for [Data Product Name] |
| Document ID | SSA-[KA-ID]-[YYYYMMDD] |
| Version | [e.g., 1.0] |
| Analysis Date | [YYYY-MM-DD] |
| Author(s) | [Name(s) of Data Engineer(s)] |
| Approver | [Name of Data Integration Manager] |
| Related Documents | [e.g., Data Landscape Map, Data Catalog, Data Governance Policies, Data Contracts] |

### 3.2. Executive Summary

> *Provide a high-level summary of the analysis. Briefly describe the source system, the key findings, the overall assessment of its suitability, and a summary of any major risks or recommendations. This section should be written last.*

**Input needed**: Completed analysis in all subsequent sections.  
**Who fills this**: D-Eng drafts, DI Mgr reviews.

[Insert Executive Summary]

### 3.3. System Overview

> *Describe the source system in detail. Explain its business purpose, its users, and its role in the organization. Also, describe the underlying technology and architecture, including cloud/on-premise status, integration points, and data governance posture.*

**Input needed**: System documentation, interviews with SMEs, system administrators, and data governance officers.  
**Who fills this**: D-Eng.

*   **System Name**: `[e.g., Oracle ERP Cloud, Salesforce CRM, In-house Billing System]`
*   **Business Purpose**: `[e.g., Manages all financial transactions, including accounts payable and receivable.]`
*   **Key Business Processes Supported**: `[e.g., Order-to-Cash, Procure-to-Pay]`
*   **Primary Users**: `[e.g., Finance Department, Sales Operations]`
*   **System Owner**: `[Name and Title]`
*   **Technical Owner/Administrator**: `[Name and Title]`
*   **Architecture Overview**: `[e.g., 3-tier web application with Oracle 19c database backend, hosted on-premise; or cloud-native microservices architecture on AWS.]`
*   **Technology Stack**: `[e.g., Java, Oracle DB, WebLogic Server, REST APIs]`
*   **Deployment Environment**: `[e.g., On-premise, AWS Cloud, Hybrid]`
*   **Data Governance & Compliance**: `[e.g., GDPR applicable, data classified as PII, subject to EU AI Act compliance]`
*   **Integration Points**: `[e.g., Downstream BI system, data lake, AI model pipelines, data mesh federated queries]`
*   **Data Stewardship Model**: `[e.g., Centralized stewardship, federated data product ownership, agentic stewardship roles]`

### 3.4. Data Scope and Objects for Analysis

> *List the specific data objects (tables, views, files, APIs, streams) that are in scope for this analysis, as determined by the requirements of the data product. Include data contracts or SLAs if applicable.*

**Input needed**: Data product requirements, `templates/templates-KA-02-data-architecture.md`, `templates/templates-KA-09-metadata-management.md`.  
**Who fills this**: D-Eng, in consultation with SME and Data Steward.

| Object Name | Object Type | Description | Priority | Data Sensitivity Classification |
| :--- | :--- | :--- | :--- | :--- |
| `[e.g., AR_INVOICES_ALL]` | `[Table]` | `[Contains all customer invoice header information]` | `[High]` | `[Confidential, PII]` |
| `[e.g., AR_INVOICE_LINES_ALL]` | `[Table]` | `[Contains all customer invoice line item details]` | `[High]` | `[Confidential]` |
| `[e.g., HZ_CUST_ACCOUNTS]` | `[Table]` | `[Master table for customer account information]` | `[Medium]` | `[PII]` |
| `[e.g., customer_v1_api]` | `[API]` | `[REST API endpoint for retrieving customer details]` | `[Low]` | `[Public]` |

> **Note:** Include references to applicable data contracts or SLAs that define data quality, availability, and access expectations.

### 3.5. Data Profiling and Quality Assessment

> *This is a critical section. For each data object in scope, perform detailed data profiling and document the findings. This should go beyond simple column statistics to include pattern analysis, anomaly detection, and data drift considerations.*

**Input needed**: Data profiling tool results, queries against the source database, historical profiling data if available.  
**Who fills this**: D-Eng, with support from DQ Analyst.

#### 3.5.1. [Table/Object Name: e.g., AR_INVOICES_ALL]

*   **Record Count**: `[e.g., 15,450,800]`
*   **Data Volume**: `[e.g., 25 GB]`
*   **Update Frequency**: `[e.g., Real-time, intra-day updates]`
*   **Data Latency**: `[e.g., 1 hour delay on reporting replica]`

**Column-Level Profiling:**

| Column Name | Data Type | Null % | Distinct Values | Min/Max/Avg Value | Key Patterns/Formats | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `INVOICE_ID` | `NUMBER(15)` | 0% | 15,450,800 | 1 / 15450800 / - | `[Numeric]` | Primary Key. No issues observed. |
| `INVOICE_DATE` | `DATE` | 0% | 3,650 | 2016-01-01 / 2026-02-08 / - | `YYYY-MM-DD` | Appears reliable. |
| `CUSTOMER_ID` | `NUMBER(10)` | 1.2% | 55,230 | 1001 / 98765 / - | `[Numeric]` | **Issue**: 1.2% nulls. Needs investigation. Foreign key to `HZ_CUST_ACCOUNTS`. |
| `STATUS` | `VARCHAR2(30)` | 0% | 5 | - / - / - | `[A-Z_]` | Values: `OPEN`, `CLOSED`, `VOID`, `IN_DISPUTE`, `PARTIALLY_PAID`. Consistent. |
| `AMOUNT` | `NUMBER(14,2)` | 0% | 1,200,000 | -1500.00 / 50000.00 / 1250.75 | `[Numeric]` | **Issue**: Negative values present. Business rules needed to understand validity (e.g., credit memos). |

**Inter-Table Analysis:**

*   **Referential Integrity**: `[e.g., Test join between AR_INVOICES_ALL.CUSTOMER_ID and HZ_CUST_ACCOUNTS.CUSTOMER_ID. Found that 0.5% of CUSTOMER_ID values in the invoice table do not exist in the customer master. These are orphan records.]`
*   **Data Drift**: `[e.g., Monthly profiling shows a 10% increase in nulls for STATUS column over last 3 months, indicating potential process issues.]`
*   **Anomaly Detection**: `[e.g., Unusually high invoice amounts detected for certain customers, requiring further investigation.]`

> **Modern Context:**  
> Include AI governance considerations by profiling data used in AI/ML pipelines for bias, completeness, and representativeness. Document data lineage and transformations to support explainability and auditability. Monitor data drift and anomalies that could impact model fairness or accuracy.

### 3.6. Data Access and Extraction Plan

> *Describe the approved method for accessing and extracting data from the source system. Include details on protocols, security, performance, and compliance considerations.*

**Input needed**: Consultation with source system administrator, security team, and `templates/templates-KA-02-data-architecture.md`.  
**Who fills this**: D-Eng.

*   **Access Method**: `[e.g., Read-only SQL access to a dedicated reporting replica of the production database, REST API, or CDC stream.]`
*   **Protocol**: `[e.g., JDBC/ODBC, REST API, Kafka]`
*   **Security**: `[e.g., Service account with credentials stored in HashiCorp Vault. Access restricted to specific schemas and IP addresses. Encryption in transit and at rest.]`
*   **Extraction Strategy**: `[e.g., Incremental extraction based on a `LAST_UPDATE_DATE` column, CDC logs, or event streams. Batch or real-time.]`
*   **Performance Considerations**: `[e.g., The reporting replica is 1 hour behind production. Extraction queries must be optimized to avoid full table scans and run within the allocated batch window.]`
*   **Compliance Considerations**: `[e.g., Data masking applied for PII fields. Extraction complies with GDPR and EU AI Act requirements.]`
*   **Contact Person for Access**: `[Name and Email]`

> **Forward-Looking Note:**  
> With the rise of data mesh and data fabric architectures, extraction plans may involve federated queries, data contracts, and self-service data product APIs. Ensure alignment with organizational data product standards and SLAs. Consider integration with MLOps and DataOps pipelines for automated, monitored data ingestion.

### 3.7. Data Dictionary and Semantics

> *Provide a detailed data dictionary for the in-scope data elements. This goes beyond the physical definition to include business definitions, rules, data sensitivity, and context.*

**Input needed**: Interviews with SMEs and Data Stewards, `templates/templates-KA-01-data-governance.md`.  
**Who fills this**: D-Eng, with significant input from SME/D-Steward.

| Table | Column | Business Definition | Business Rules | Data Sensitivity | Example |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AR_INVOICES_ALL` | `STATUS` | The current lifecycle state of the invoice. | Cannot move from `CLOSED` to `OPEN`. `VOID` status is final. | Confidential | `IN_DISPUTE` |
| `AR_INVOICES_ALL` | `AMOUNT` | The total monetary value of the invoice in the local currency. | Can be negative only if the invoice type is 'Credit Memo'. | Confidential | `499.99` |
| `HZ_CUST_ACCOUNTS` | `ACCOUNT_TYPE` | The classification of the customer account. | Values are `INTERNAL`, `EXTERNAL`, `PARTNER`. Default is `EXTERNAL`. | PII | `PARTNER` |

> **Note:** Include data lineage references, data ownership, and stewardship responsibilities here or link to metadata management outputs (`../../KA-09-metadata-management/`). Document any data contracts or SLAs that apply to these data elements.

### 3.8. Risks and Recommendations

> *Summarize the identified risks and provide actionable recommendations to mitigate them. Include considerations for data quality, governance, technical constraints, and compliance.*

**Input needed**: All previous sections of the analysis.  
**Who fills this**: D-Eng drafts, DI Mgr reviews.

| # | Risk Category | Description | Impact | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Data Quality | 1.2% of invoices have a null `CUSTOMER_ID`, and 0.5% are orphans. | High | Implement a pre-processing step in the ETL to flag and quarantine these records. Work with the source system team to enforce a foreign key constraint. |
| 2 | Data Semantics | Negative values exist in the `AMOUNT` column. | Medium | Consult with SMEs to define the business logic for handling negative amounts (credit memos) in the target data model and BI reports. |
| 3 | Technical | The current incremental extraction key (`LAST_UPDATE_DATE`) does not capture hard deletes. | High | Propose a change to the source system to implement soft deletes (e.g., an `IS_DELETED` flag) or provide a separate change data capture (CDC) log. |
| 4 | Compliance | Source data contains PII subject to GDPR and EU AI Act requirements. | High | Apply data masking or pseudonymization during extraction. Ensure data usage aligns with consent and purpose limitations. |
| 5 | AI Governance | Data used for AI models lacks documented bias assessment. | Medium | Collaborate with AI Ethics Officer to conduct bias and fairness assessments on source data. Establish monitoring for data drift affecting model fairness. |
| 6 | Architecture | Source system integration points lack support for federated queries or data contracts. | Medium | Work with architecture teams to enable data contracts and APIs aligned with data mesh principles. |

---

## 4. Example

> *This is a fictional example of a completed Source System Analysis for the "Salesforce CRM" system, providing data for a new "Customer 360" data product at GlobalRetail Inc.*

### **Document Control**

*   **Document Title**: Source System Analysis: Salesforce CRM for Customer 360 Product
*   **Version**: 1.0
*   **Analysis Date**: 2026-02-08
*   **Author(s)**: Jane Doe, Data Engineer
*   **Approver**: John Smith, Data Integration Manager
*   **Related Documents**: Data Landscape Map, Data Catalog, Data Governance Policy, Customer 360 Data Contract

### **System Overview**

*   **System Name**: Salesforce Sales Cloud (SFDC)
*   **Business Purpose**: Manages customer relationships, sales pipeline, opportunities, and contact information for GlobalRetail Inc.
*   **Architecture Overview**: Multi-tenant SaaS application. Data access is provided via REST/SOAP APIs and a reporting replica (Salesforce Shield).
*   **Deployment Environment**: Cloud (SaaS)
*   **Data Governance & Compliance**: Contains PII, subject to GDPR and CCPA. Data usage governed by company data policies and EU AI Act compliance.
*   **Integration Points**: Downstream BI system, Customer Data Platform, AI/ML pipelines, federated queries via data mesh.
*   **Data Stewardship Model**: Federated data product ownership with Data Product Manager and Data Steward assigned.

### **Data Scope and Objects for Analysis**

| Object Name | Object Type | Description | Priority | Data Sensitivity Classification |
| :--- | :--- | :--- | :--- | :--- |
| `Account` | `Standard Object` | Represents individual customer companies. | High | PII |
| `Contact` | `Standard Object` | Represents individuals associated with Accounts. | High | PII |
| `Opportunity` | `Standard Object` | Represents potential sales deals. | High | Confidential |
| `Case` | `Standard Object` | Represents customer support issues. | Medium | Confidential |

### **Data Profiling and Quality Assessment**

#### **Account Object**

*   **Record Count**: 85,340
*   **Update Frequency**: Real-time
*   **Data Latency**: Near real-time (within 5 minutes)

| Column Name | Data Type | Null % | Distinct Values | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `Id` | `string(18)` | 0% | 85,340 | Primary Key. |
| `Name` | `string(255)` | 0% | 84,990 | High cardinality, some duplicates found (e.g., "GlobalRetail" vs "GlobalRetail, Inc."). |
| `Industry` | `picklist` | 22% | 45 | **High Null %**. Critical for segmentation; often not populated by sales reps. |
| `AnnualRevenue` | `currency` | 45% | 12,000 | **Very High Null %**. Unreliable for financial analysis. |
| `BillingCountry` | `picklist` | 2% | 150 | Mostly clean, but contains variations like "USA", "United States", "US". Needs standardization. |

> **AI Governance Note:** Data completeness and representativeness are critical for AI models using this data. Missing `Industry` and `AnnualRevenue` fields may bias segmentation models.

### **Data Access and Extraction Plan**

*   **Access Method**: REST API (Bulk API 2.0 for initial load, REST API for incremental).
*   **Extraction Strategy**: Incremental extraction using the `SystemModstamp` field. A nightly batch job will query for records updated in the last 24 hours.
*   **Security**: OAuth 2.0 authentication with token refresh. Access restricted to service account with minimal privileges.
*   **Compliance**: Data masking applied to sensitive fields during extraction. Logging and audit trails maintained.
*   **Contact Person for Access**: api-access@globalretail.com

### **Data Dictionary and Semantics**

| Object | Field | Business Definition | Business Rules |
| :--- | :--- | :--- | :--- |
| `Opportunity` | `StageName` | The current stage of the sales deal in the pipeline. | Controlled picklist. The final stage `Closed Won` triggers a process to create a customer in the ERP system. |
| `Account` | `Ownership` | The legal structure of the company. | Values are `Public`, `Private`, `Subsidiary`. This is a custom field. |

### **Risks and Recommendations**

| # | Risk Category | Description | Impact | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Data Quality | The `Industry` and `AnnualRevenue` fields in the `Account` object are highly incomplete. | High | 1. Make the `Industry` field mandatory in Salesforce. 2. Source `AnnualRevenue` from the official financial system (ERP) instead of relying on SFDC. |
| 2 | Technical | API rate limits could be an issue during the initial full data load. | Medium | Use the Bulk API 2.0 for the initial load and carefully monitor API consumption. Stagger the loading of objects. |
| 3 | Compliance | PII data requires masking and auditing for GDPR compliance. | High | Implement data masking and maintain audit logs for data access. |
| 4 | AI Governance | Lack of bias assessment for AI models consuming this data. | Medium | Collaborate with AI Ethics Officer to conduct bias and fairness assessments. Implement monitoring for data drift. |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Metrics & KPIs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Governance | Knowledge Area | **templates/templates-KA-01-data-governance.md** |
| Data Contracts | Concept | [#](references/concepts-modern-paradigms.md) |
| Data Mesh | Concept | [references/concepts-modern-paradigms.md](references/concepts-modern-paradigms.md) |
| AI Governance | Concept | **#** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [x] All in-scope data objects are listed and prioritized.
- [x] Each object has been profiled for record count, volume, update frequency, and latency.
- [x] Column-level profiling has been completed for all critical columns, including null percentages, distinct value counts, and data patterns.
- [x] At least one form of inter-table analysis (e.g., referential integrity check) has been performed.
- [x] The data access and extraction method is clearly defined, approved, and compliant with security and privacy policies.
- [x] A data dictionary with clear business definitions, rules, and data sensitivity classifications is provided for key fields.
- [x] All identified data quality issues and other risks have corresponding, actionable recommendations.
- [x] The document has been reviewed and approved by the Data Integration Manager and relevant governance stakeholders.
- [x] AI governance considerations are addressed where applicable, including bias and fairness assessments.
- [x] Compliance with relevant regulations (GDPR, HIPAA, CCPA, EU AI Act) is documented and mitigated.
- [x] Data contracts, stewardship responsibilities, and data product ownership are clearly documented.
- [x] Extraction methods align with modern architectures such as data mesh and data fabric.

### 5.2. Review Checklist

| Review Item | Expected Outcome |
| :--- | :--- |
| Completeness | All required sections are filled with sufficient detail. |
| Accuracy | Data profiling results and metadata are accurate and validated. |
| Compliance | Data governance, privacy, and AI governance requirements are met. |
| Risk Mitigation | Risks are identified with practical, actionable recommendations. |
| Stakeholder Engagement | Relevant SMEs, stewards, and governance officers have reviewed and approved. |
| Alignment | Analysis aligns with enterprise data architecture and data product standards. |
| Documentation | Version control and document control fields are complete and current. |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

- Data product requirements and use cases.
- Source system documentation and metadata.
- Data governance policies and data contracts (`../../KA-10-data-governance/`).
- Data landscape maps (`templates/templates-KA-02-data-architecture.md`).
- Data catalogs and metadata repositories (`templates/templates-KA-09-metadata-management.md`).

### 6.2. Consumers (Outputs)

- Data integration and ETL/ELT design documents.
- Data models and semantic layers (`../../KA-03-data-modeling-design/`).
- Data quality monitoring plans (`../../KA-11-data-quality/`).
- Data governance and compliance reports.
- AI model input data assessments and bias reports.
- Data product documentation and SLAs.

---

## 7. Tools and Automation

### 7.1. Recommended Tools

- Data profiling tools: e.g., Talend Data Quality, Informatica Data Quality, Apache Griffin.
- Metadata management platforms: e.g., Collibra, Alation, Apache Atlas.
- Data catalog and lineage tools: e.g., Microsoft Purview, DataHub.
- Data governance platforms with AI governance modules.
- API management and CDC tools for modern extraction.
- Automation platforms for DataOps and MLOps integration.

### 7.2. Automation Opportunities

- Automated data profiling and anomaly detection integrated into CI/CD pipelines.
- Continuous data quality monitoring with alerting for data drift.
- Automated lineage capture and metadata synchronization.
- Integration of AI governance checks into data ingestion workflows.
- Use of data contracts and SLAs enforced via automation in data mesh environments.
- Automated compliance checks for GDPR, HIPAA, CCPA, and EU AI Act.

---

## 8. References

- DAMA International. (2025). *DAMA-DMBOK 3.0* (in development).  
- DAMA International. (2017). *DAMA-DMBOK 2*.  
- EU AI Act (Proposal). European Commission.  
- GDPR (General Data Protection Regulation). European Union.  
- HIPAA (Health Insurance Portability and Accountability Act). U.S. Department of Health & Human Services.  
- CCPA (California Consumer Privacy Act). State of California.  
- *Data Mesh* concept: [references/concepts-modern-paradigms.md](references/concepts-modern-paradigms.md)  
- *Data Contracts* concept: [#](references/concepts-modern-paradigms.md)  
- *AI Governance* concept: **#**  
- *Data Governance* knowledge area: **templates/templates-KA-01-data-governance.md**  
- *Metadata Management* knowledge area: **templates/templates-KA-09-metadata-management.md**  
- *Data Architecture* knowledge area: **templates/templates-KA-02-data-architecture.md**


---

# Data Mart Design


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Document Control](#31-document-control)
  - [3.2. Business Requirements](#32-business-requirements)
  - [3.3. Data Sources](#33-data-sources)
  - [3.4. Dimensional Data Model](#34-dimensional-data-model)
  - [3.5. ETL/ELT Design](#35-etlelt-design)
  - [3.6. Reporting and BI Access](#36-reporting-and-bi-access)
- [4. Example](#4-example)
  - [4.1. Business Requirements](#41-business-requirements)
  - [4.2. Data Sources](#42-data-sources)
  - [4.3. Dimensional Data Model](#43-dimensional-data-model)
  - [4.4. ETL/ELT Design](#44-etlelt-design)
  - [4.5. Reporting and BI Access](#45-reporting-and-bi-access)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
  - [5.2. Review Checklist](#52-review-checklist)
- [6. Related Outputs](#6-related-outputs)
  - [6.1. Prerequisites (Inputs to this Output)](#61-prerequisites-inputs-to-this-output)
  - [6.2. Consumers (Outputs that depend on this Output)](#62-consumers-outputs-that-depend-on-this-output)
- [7. Tools and Automation](#7-tools-and-automation)
  - [7.1. Recommended Tools](#71-recommended-tools)
  - [7.2. Automation Opportunities](#72-automation-opportunities)
- [8. References](#8-references)

---

## 1. Overview

### 1.1. Definition and Purpose

The **Data Mart Design** is a comprehensive and detailed document that specifies the architecture, structure, and components of a data mart. A data mart is a subject-oriented, curated subset of a larger data warehouse or data platform, designed to meet the specific analytical and reporting needs of a particular business unit or user group (e.g., Sales, Marketing, Finance). This design document serves as the blueprint for the development, deployment, and ongoing maintenance of the data mart.

> The purpose of the Data Mart Design is to translate business requirements for a specific domain into a scalable, maintainable, and performant technical solution that provides accessible, understandable, and relevant data for analysis and reporting. This enables faster, more effective decision-making and supports operational and strategic business objectives.

In the context of modern data management, the Data Mart Design must also consider emerging paradigms such as data mesh and data fabric architectures, ensuring that the mart fits within a federated data product ecosystem and supports interoperability, discoverability, and self-service analytics. Additionally, considerations for AI governance, data privacy regulations (e.g., GDPR, HIPAA, EU AI Act), and cloud-native deployment patterns are increasingly critical.

### 1.2. Scope

**Per Product** — A Data Mart Design is created for each individual data product or business area that requires its own analytical platform. While it may draw data from a central enterprise data warehouse or data lakehouse, its design is scoped specifically to the requirements of a single department, line of business, or subject area.

The design encompasses:

- Logical and physical data modeling tailored to business questions.
- Data integration and transformation processes.
- Security and access controls aligned with data governance policies.
- Performance and scalability considerations for current and future workloads.
- Compliance with relevant data privacy and AI governance frameworks.

This deliverable is a critical component in the phased rollout of enterprise data platforms, typically forming part of the 3-6 month foundational implementation timeline and supporting longer-term enterprise-wide adoption.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-02: Data Architecture | The Data Mart Design must align with the overall enterprise data architecture blueprint and technology standards. The [Data Warehouse Architecture](knowledge-areas/KA-02-data-architecture.md) is a key input, especially regarding cloud-native and hybrid deployment models. |
| KA-03: Data Modeling and Design | The logical and physical data models for the data mart, particularly the [Dimensional Model](knowledge-areas/KA-03-data-modeling-and-design.md), are core components of the design. This includes evolving modeling techniques to support data products and contracts. |
| KA-06: Data Integration and Interoperability | The design specifies how data will be extracted, transformed, and loaded (ETL/ELT) into the data mart from various source systems, including real-time streaming and batch integration patterns. |
| KA-08: Data Warehousing and Business Intelligence | This deliverable is a foundational artifact supporting BI and analytics use cases, including integration with modern BI tools and AI/ML pipelines. |
| KA-10: Data Security | The design must incorporate security controls, including data masking, encryption, and row-level security, to comply with governance and regulatory requirements. |
| KA-11: Data Quality | The design must incorporate data quality rules, monitoring, and remediation processes to ensure the data within the mart is accurate, complete, and trustworthy. |
| KA-12: Data Governance | The Data Mart Design must align with data governance policies, stewardship roles, and compliance mandates, including emerging AI governance frameworks. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately accountable for the successful creation, implementation, and ongoing maintenance of the data mart. Ensures the design is technically sound, meets business objectives, and aligns with enterprise standards and governance. |
| **R (Responsible)** | Data Warehouse Architect (DW Arch) | Leads the design of the data mart, including data modeling, architecture, and ETL/ELT processes. Authors and maintains the Data Mart Design document. |
| **S (Supportive)** | Data Modeler (D-Modeler) | Develops the dimensional data model (star/snowflake schema) and supports the design of data contracts and product interfaces. |
| **C (Consulted)** | Data Analyst (D-Analyst), BI Manager (BI Mgr), Data Steward | Provide input on business requirements, analytical needs, reporting requirements, and data quality considerations to ensure the design is fit for purpose and compliant. |
| **I (Informed)** | Data Administration Manager (DA Mgr), AI Ethics Officer | Kept informed of the design to ensure alignment with data governance policies, AI governance, and compliance with regulatory frameworks. |

### 2.2. Section-Level RASCI

| Design Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Business Requirements | DW Arch | D-Analyst, BI Mgr | DE Mgr |
| Data Model (Dimensional) | D-Modeler | DW Arch, Data Steward | DE Mgr |
| Architecture & Technology | DW Arch | DE Mgr, Data Security Lead | DE Mgr |
| ETL/ELT Design | DW Arch | D-Modeler, Data Integration Lead | DE Mgr |
| Reporting & BI Access | DW Arch | BI Mgr | DE Mgr |

---

## 3. Template

> *The following is the standardized template for a Data Mart Design. Replace all placeholders `[...]` with project-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Control

| Field | Value |
| :--- | :--- |
| Document Title | Data Mart Design: [Subject Area, e.g., Sales] |
| Document ID | DMD-[KA#]-[Seq#] |
| Version | [e.g., 1.0] |
| Status | [e.g., Draft, In Review, Approved] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Warehouse Architect] |
| Reviewers | [List of reviewers] |
| Approver | [Data Engineering Manager] |

### 3.2. Business Requirements

> *Summarize the business goals and analytical questions this data mart is intended to answer. This section provides the "why" behind the design.*

**Input needed**: Business requirements documents, interviews with stakeholders, data product definitions.  
**Who fills this**: DW Arch, with input from D-Analyst, BI Mgr, and Data Steward.

- **Business Goal**: [e.g., To increase customer retention by 10% by identifying at-risk customers through predictive analytics.]
- **Key Business Questions**:
  - [e.g., What are the key drivers of customer churn?]
  - [e.g., Which customer segments have the highest lifetime value?]
  - [e.g., How effective are our marketing campaigns at acquiring new customers?]
  - [e.g., What is the impact of pricing changes on sales volume?]
- **Success Criteria**: [e.g., The data mart must provide the data necessary to build a churn prediction model with at least 85% accuracy and support daily refreshes within SLA.]

### 3.3. Data Sources

> *List all source systems from which data will be extracted for this data mart. Include details on the type of data, extraction method, and any relevant data contracts or SLAs.*

**Input needed**: Source system documentation, data flow diagrams (`03-data-flow-diagrams.md`), data contracts.  
**Who fills this**: DW Arch.

| Source System | System Owner | Data Provided | Extraction Method | Frequency | Data Contract Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., Salesforce CRM] | [e.g., Sales Operations] | [e.g., Customer accounts, contacts, opportunities] | [e.g., API Connector] | [e.g., Daily] | [Contract ID or link] |
| [e.g., SAP ERP] | [e.g., Finance] | [e.g., Sales orders, invoices, product master] | [e.g., JDBC Connection] | [e.g., Daily] | [Contract ID or link] |
| [e.g., Google Analytics] | [e.g., Marketing] | [e.g., Website traffic, user behavior] | [e.g., API] | [e.g., Hourly] | [Contract ID or link] |

### 3.4. Dimensional Data Model

> *This is the core of the design. Include the star or snowflake schema diagram and define all dimension and fact tables. Reference the detailed dimensional data model document.*

**Input needed**: [Dimensional Data Model](knowledge-areas/KA-03-data-modeling-and-design.md).  
**Who fills this**: D-Modeler, reviewed by DW Arch and Data Steward.

#### 3.4.1. Schema Diagram

[Insert a diagram of the star/snowflake schema for the data mart. This can be an embedded image or a Mermaid diagram.]

#### 3.4.2. Dimension Tables

| Dimension Name | Description | Key Attributes | Slowly Changing Dimension (SCD) Type | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `DIM_Customer` | Contains attributes of individual customers, including demographics and segmentation. | `Customer_SK`, `CustomerID`, `FullName`, `Email`, `City`, `State` | Type 2 | Supports historical tracking of customer attribute changes. |
| `DIM_Product` | Contains attributes of products sold, including category and pricing. | `Product_SK`, `ProductID`, `ProductName`, `Category`, `Subcategory` | Type 1 | Overwrites on update; no history maintained. |
| `DIM_Date` | Contains date and time attributes for analysis, including fiscal calendars. | `Date_SK`, `FullDate`, `DayOfWeek`, `Month`, `Quarter`, `Year` | N/A | Standard corporate date dimension. |

#### 3.4.3. Fact Tables

| Fact Table Name | Granularity | Key Measures | Foreign Keys (Dimension SKs) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `FACT_Sales` | One row per sales order line item | `OrderQuantity`, `UnitPrice`, `TotalAmount`, `DiscountAmount` | `Customer_SK`, `Product_SK`, `OrderDate_SK`, `ShipDate_SK` | Supports detailed sales analysis and aggregation. |
| `FACT_Web_Traffic` | One row per daily website session per user | `PageViews`, `SessionDuration`, `BounceRate` | `Customer_SK`, `Date_SK` | Enables digital engagement analytics. |

### 3.5. ETL/ELT Design

> *Describe the high-level process for extracting data from sources, transforming it, and loading it into the data mart tables. Reference detailed source-to-target mapping documents.*

**Input needed**: [Source-to-Target Mapping](knowledge-areas/KA-06-data-integration-interoperability.md).  
**Who fills this**: DW Arch.

- **Staging Area**: [e.g., Describe the staging database schema and purpose, including data landing zones and raw data storage.]
- **Data Transformation Logic**: [e.g., Detail key business rule implementations, data cleansing steps, handling of slowly changing dimensions, and calculations for derived measures.]
- **Loading Strategy**: [e.g., Incremental load for fact tables using watermark columns; SCD Type 2 handling for dimension tables.]
- **ETL Tool**: [e.g., Talend, Informatica, dbt, Apache Airflow, custom Python scripts]
- **Data Quality Checks**: [e.g., Automated validation steps integrated into ETL pipelines to ensure completeness and accuracy.]
- **AI Governance Considerations**: [e.g., Ensure data lineage and provenance are captured to support explainability and compliance with AI regulations.]

### 3.6. Reporting and BI Access

> *Describe how users will access and analyze the data in the mart. List the BI tools that will be supported and any pre-built reports or dashboards.*

**Input needed**: BI tool documentation, reporting requirements, data product catalog.  
**Who fills this**: DW Arch, with input from BI Mgr.

- **BI Tools**: [e.g., Tableau, Power BI, Looker, Superset]
- **Access Method**: [e.g., Direct query via SQL, connection through BI tool semantic layer, API endpoints]
- **Pre-built Dashboards**:
  - [e.g., Sales Performance Dashboard]
  - [e.g., Customer 360 Dashboard]
  - [e.g., Marketing Campaign Effectiveness]
- **Security**: [e.g., Describe row-level security implementation based on user roles, data masking, and compliance with privacy regulations.]
- **Self-Service Analytics**: [e.g., Enable data discovery and exploration capabilities for business users via data catalogs and semantic layers.]
- **Integration with MLOps/DataOps**: [e.g., Support data access for machine learning pipelines and operational analytics.]

---

## 4. Example

> *This is a realistic example for a **Sales Data Mart** at a fictional company, **GlobalRetail Inc.***

### 4.1. Business Requirements

- **Business Goal**: To provide the sales team with a unified view of sales performance across all regions and product lines to identify growth opportunities and improve forecast accuracy.
- **Key Business Questions**:
  - What are our top-selling products and product categories by region?
  - How is sales performance trending month-over-month and year-over-year?
  - Which sales representatives are meeting or exceeding their quotas?
  - How do promotions impact sales volume and revenue?
- **Success Criteria**: The data mart must refresh daily by 6 AM local time and support the generation of the weekly Sales Performance Review dashboard within 5 minutes.

### 4.2. Data Sources

| Source System | System Owner | Data Provided | Extraction Method | Frequency | Data Contract Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GlobalRetail ERP | Finance | Sales Orders, Invoices, Product Master, Customer Master | JDBC Connection | Daily (2 AM) | Contract #GR-ERP-2024 |
| Anaplan | Sales Operations | Sales Quotas, Territory Assignments | REST API | Weekly (Mon 4 AM) | Contract #GR-ANAPLAN-2024 |

### 4.3. Dimensional Data Model

#### 4.3.1. Schema Diagram

*A star schema centered on `FACT_Sales` with `DIM_Customer`, `DIM_Product`, `DIM_Salesperson`, and `DIM_Date` dimensions.*

#### 4.3.2. Dimension Tables

| Dimension Name | Description | Key Attributes | SCD Type | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `DIM_Customer` | Contains all B2B customer accounts. | `Customer_SK`, `CustomerID`, `CustomerName`, `Industry`, `Region` | Type 2 | Tracks changes in customer attributes over time. |
| `DIM_Product` | Contains all products from the master catalog. | `Product_SK`, `ProductID`, `ProductName`, `Category`, `ListPrice` | Type 1 | Overwrites on update; no history maintained. |
| `DIM_Salesperson` | Contains sales team members and their hierarchy. | `Salesperson_SK`, `EmployeeID`, `FullName`, `ManagerName`, `Region` | Type 2 | Supports organizational changes and reporting lines. |
| `DIM_Date` | Standard corporate date dimension. | `Date_SK`, `FullDate`, `FiscalMonth`, `FiscalQuarter`, `FiscalYear` | N/A | Fiscal calendar aligned with corporate standards. |

#### 4.3.3. Fact Tables

| Fact Table Name | Granularity | Key Measures | Foreign Keys | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `FACT_Sales` | One row per invoice line. | `QuantitySold`, `GrossAmount`, `NetAmount`, `DiscountAmount` | `Customer_SK`, `Product_SK`, `Salesperson_SK`, `InvoiceDate_SK` | Supports detailed sales analysis. |
| `FACT_Sales_Quota` | One row per salesperson per month. | `QuotaAmount` | `Salesperson_SK`, `MonthStartDate_SK` | Used for quota attainment reporting. |

### 4.4. ETL/ELT Design

- **Staging Area**: A dedicated schema `stg` in the Snowflake data warehouse is used to land raw data from the ERP and Anaplan systems. Data is ingested in near real-time where possible, with batch loads scheduled overnight.
- **Data Transformation Logic**: Transformations are performed using dbt (Data Build Tool). Key logic includes calculating `NetAmount` by applying discounts and handling currency conversion to USD. Customer and Salesperson dimensions are managed using dbt snapshots to implement SCD Type 2 logic. Data quality checks are embedded in the dbt pipeline.
- **Loading Strategy**: `FACT_Sales` is loaded incrementally based on `last_modified_date` columns. `FACT_Sales_Quota` is a snapshot fact, fully reloaded weekly. ETL jobs are orchestrated using Apache Airflow with automated alerting on failures.
- **AI Governance**: Data lineage is captured and documented to support explainability for downstream AI/ML models using this data mart.

### 4.5. Reporting and BI Access

- **BI Tools**: The primary BI tool is Power BI, with additional support for Tableau for certain user groups.
- **Access Method**: Power BI connects to the Snowflake data warehouse using a live connection to a dedicated `analytics` schema containing the final data mart tables. Semantic models are published to enable self-service.
- **Pre-built Dashboards**: A "Sales Leadership" Power BI App with reports on YTD Performance, Quota Attainment, and Product Category Analysis.
- **Security**: Row-level security is implemented in Power BI using DAX rules based on the user's assigned sales region and their position in the manager hierarchy. Data masking is applied for sensitive customer information.
- **Self-Service**: Business users have access to a curated data catalog and semantic layer to build ad-hoc reports and explore data.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Tools Landscape | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Metrics KPIs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Contracts | Concept | [#](references/concepts-modern-paradigms.md) |
| Data Mesh | Concept | [references/concepts-modern-paradigms.md](references/concepts-modern-paradigms.md) |
| Data Governance Roles | Guide | **#** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The design document is formally approved by the Data Engineering Manager.
- [x] The dimensional model is validated by the Data Modeler and Data Warehouse Architect.
- [x] All data sources are identified, accessible, and covered by data contracts.
- [x] ETL/ELT logic correctly implements all specified business rules and transformation requirements.
- [x] The data mart can be refreshed within the defined SLA (e.g., daily by 6 AM).
- [x] Pre-built dashboards render correctly and match data from source systems.
- [x] Row-level security and data masking are tested and confirmed to be working as expected.
- [x] Data lineage and provenance are documented to support AI governance and compliance.
- [x] The design aligns with enterprise data architecture, naming conventions, and governance policies.

### 5.2. Review Checklist

| Criteria | What to Check | Reviewer |
| :--- | :--- | :--- |
| **Completeness** | Does the design address all stated business requirements? Are all tables, columns, and ETL processes documented? | DW Arch |
| **Clarity** | Is the document easy to understand for both technical and business stakeholders? Are diagrams and definitions clear? | BI Mgr |
| **Correctness** | Does the dimensional model follow best practices? Is the ETL logic sound? Do the measures calculate correctly? | D-Modeler |
| **Scalability** | Is the architecture designed to handle future growth in data volume and user concurrency? | DE Mgr |
| **Consistency** | Does the design align with the enterprise data architecture, naming conventions, and other standards? | DW Arch |
| **Governance Compliance** | Are data governance, security, and AI governance requirements addressed? | Data Steward, AI Ethics Officer |
| **Automation Readiness** | Are opportunities for automation and CI/CD incorporated? | DW Arch |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs to this Output)

| Output Name | File Path | Description |
| :--- | :--- | :--- |
| Data Warehouse Architecture | `templates/templates-KA-08-data-warehousing-bi.md` | Provides the overall architectural context and standards for the data warehouse environment in which the data mart will exist. |
| Dimensional Model | `templates/templates-KA-08-data-warehousing-bi.md` | Provides the detailed logical and physical dimensional model that is a core component of the data mart design. |
| Source-to-Target Mapping | `templates/templates-KA-06-data-integration-interoperability.md` | Defines the data flow and transformation rules for populating the data mart from source systems. |
| Business Requirements Document | [Project-specific location] | Captures the business goals and analytical questions driving the data mart design. |

### 6.2. Consumers (Outputs that depend on this Output)

| Output Name | File Path | Description |
| :--- | :--- | :--- |
| Dimensional Data Model | `templates/templates-KA-03-data-modeling-design.md` | The Data Mart Design is a key input for the creation of the specific dimensional data model for that mart. |
| BI Reports and Dashboards | [Project-specific location] | Consume the data mart as the source for business intelligence and analytics. |
| Data Quality Reports | [Project-specific location] | Use the data mart to monitor and report on data quality metrics. |
| AI/ML Pipelines | [Project-specific location] | Use the data mart as a trusted data source for model training and scoring. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **Data Modeling** | Erwin, SAP PowerDesigner, ER/Studio | dbt, draw.io, Archi |
| **ETL/ELT** | Informatica PowerCenter, Talend, Fivetran, Matillion | Apache Airflow, dbt, Python, NiFi |
| **Database** | Snowflake, Google BigQuery, Amazon Redshift, Azure Synapse | PostgreSQL, MySQL, Apache Hive |
| **BI & Reporting** | Tableau, Power BI, Looker, Qlik | Apache Superset, Metabase |
| **Data Catalog and Lineage** | Collibra, Alation | Amundsen, DataHub |

### 7.2. Automation Opportunities

- **Automated Testing**: Implement automated data validation tests (e.g., using dbt tests, Great Expectations) within the ETL/ELT pipeline to check for nulls, referential integrity, and other quality issues.
- **CI/CD for ETL**: Use a CI/CD pipeline (e.g., Jenkins, GitLab CI, Azure DevOps) to automate the testing and deployment of ETL/ELT code (e.g., dbt projects), ensuring rapid and reliable updates.
- **Automated Documentation**: Tools like dbt can automatically generate documentation for the data models and publish it as a website, ensuring documentation stays in sync with code.
- **Data Lineage Capture**: Integrate lineage capture tools to automatically track data flows and transformations, supporting governance and AI compliance.
- **Self-Service Provisioning**: Implement automation for provisioning data marts and access controls to accelerate delivery and reduce manual errors.
- **Monitoring and Alerting**: Automate monitoring of data freshness, quality, and pipeline health with alerting to data engineering teams.

---

## 8. References

- **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 11: Data Warehousing and Business Intelligence)  
- **[2]** DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Expected release June 2025. Incorporates modern data management paradigms including data mesh, AI governance, and cloud-native architectures.  
- **[3]** Internal Reference: [Roles and Responsibilities](knowledge-areas/KA-01-data-governance.md)  
- **[4]** Internal Reference: [Modeling Standards](knowledge-areas/KA-03-data-modeling-and-design.md)  
- **[5]** EU AI Act Compliance Guidelines, [EU Commission](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence)  
- **[6]** Data Mesh Principles and Practices, [Zhamak Dehghani](https://martinfowler.com/articles/data-mesh-principles.html)  
- **[7]** AI Governance Frameworks, [O'Reilly Media](https://www.oreilly.com/library/view/ai-governance/9781492090453/)
