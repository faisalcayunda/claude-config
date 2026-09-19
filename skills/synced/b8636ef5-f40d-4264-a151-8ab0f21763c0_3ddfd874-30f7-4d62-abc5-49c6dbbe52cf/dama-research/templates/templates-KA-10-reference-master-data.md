<!-- NAV-TOC -->
## Sections in This File

This file contains **13 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 24 | MDM Strategy |
| 367 | Golden Record Definition |
| 726 | Reference Data Standards |
| 1146 | Match Merge Rules |
| 1503 | Anti-Patterns to Avoid |
| 1518 | Forward-Looking Notes on DAMA-DMBOK 3.0 |
| 1529 | Data Integration Rules |
| 1874 | Master Data Model |
| 2196 | Reference Data Tables |
| 2538 | Data Quality Rules for Master Data Management (MDM) |
| 2894 | Hierarchy Definitions |
| 3204 | Master Data Governance Workflow |
| 3577 | Data Survivorship Rules |

## Sections in This File

This file contains **13 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 1 | MDM Strategy |
| 344 | Golden Record Definition |
| 703 | Reference Data Standards |
| 1123 | Match Merge Rules |
| 1480 | Anti-Patterns to Avoid |
| 1495 | Forward-Looking Notes on DAMA-DMBOK 3.0 |
| 1506 | Data Integration Rules |
| 1851 | Master Data Model |
| 2173 | Reference Data Tables |
| 2515 | Data Quality Rules for Master Data Management (MDM) |
| 2871 | Hierarchy Definitions |
| 3181 | Master Data Governance Workflow |
| 3554 | Data Survivorship Rules |

---

# MDM Strategy


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Vision and Mission](#31-vision-and-mission)
  - [3.2. Goals and Objectives](#32-goals-and-objectives)
  - [3.3. MDM Governance Model](#33-mdm-governance-model)
  - [3.4. MDM Architecture](#34-mdm-architecture)
  - [3.5. Implementation Roadmap](#35-implementation-roadmap)
- [4. Example](#4-example)
  - [4.1. Vision and Mission](#41-vision-and-mission)
  - [4.2. Goals and Objectives](#42-goals-and-objectives)
  - [4.3. MDM Governance Model](#43-mdm-governance-model)
  - [4.4. MDM Architecture](#44-mdm-architecture)
  - [4.5. Implementation Roadmap](#45-implementation-roadmap)
- [5. Quality Criteria](#5-quality-criteria)
  - [5.1. Acceptance Criteria](#51-acceptance-criteria)
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

The **MDM (Master Data Management) Strategy** is a comprehensive, enterprise-wide plan that articulates the organization's approach to governing, managing, and leveraging its master data assets. It defines the vision, strategic goals, governance structures, and technology infrastructure necessary to establish and maintain a single, authoritative source of truth for critical data domains such as Customer, Product, Supplier, Employee, and increasingly, AI-related metadata and data products.

The strategy ensures master data is consistent, accurate, timely, and accessible across all business units and systems, thereby reducing operational inefficiencies, enhancing analytics and reporting capabilities, and enabling data-driven decision-making at scale. It also integrates emerging considerations such as AI governance, compliance with evolving regulations (e.g., EU AI Act), and alignment with modern data architectures like Data Mesh and Data Fabric.

> The MDM Strategy answers the question: *"How will our organization govern, manage, and leverage its most critical shared data assets to achieve strategic business and digital transformation goals, while adapting to evolving technologies and regulatory landscapes?"*

### 1.2. Scope

**Global and Enterprise-Wide** — The MDM Strategy applies across all business units, geographies, and master data domains. It provides the overarching framework and principles that guide all MDM initiatives, whether implemented centrally, federated, or hybrid. The strategy encompasses not only traditional master data domains but also emerging master data types such as AI model metadata, data products, and agentic stewardship roles.

While specific implementations may be phased by domain, business unit, or technology platform, the strategy ensures consistency, interoperability, and alignment with enterprise data governance, architecture, and compliance requirements.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The MDM Strategy operationalizes governance principles specifically for master data, including stewardship, policies, and compliance with regulations such as GDPR, HIPAA, CCPA, and the EU AI Act. |
| KA-02: Data Architecture | Defines the architectural approach for MDM (centralized, federated, hybrid, or mesh-enabled) and ensures alignment with enterprise data architecture blueprints, including cloud-native and multi-cloud environments. |
| KA-06: Data Integration | Specifies standards and patterns for integrating master data from diverse source systems into the MDM hub and distributing it to consuming applications, leveraging modern integration paradigms like event-driven architecture and APIs. |
| KA-07: Data Security and Privacy | Ensures master data management adheres to security policies and privacy regulations, incorporating data masking, encryption, and access controls. |
| KA-08: Data Quality | Establishes data quality frameworks, metrics, and remediation processes critical to maintaining master data integrity and trustworthiness. |
| KA-10: Reference and Master Data Management | Provides detailed methodologies and best practices for master data lifecycle management, stewardship, and governance. |
| KA-12: Data Operations (DataOps) | Integrates operational practices such as MLOps, DataOps, and FinOps to ensure continuous delivery, monitoring, and optimization of MDM processes and platforms. |
| KA-13: AI and Analytics Governance | Addresses governance of AI-related master data, including model metadata, data contracts, and ethical considerations, reflecting the emerging role of AI Ethics Officers and CAIOs. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Chief Data Officer (CDO) | Ultimately accountable for the success of the MDM program, including strategy approval, resource allocation, and alignment with enterprise data and AI governance initiatives. |
| **R (Responsible)** | MDM Manager (MDM Mgr) | Responsible for developing, documenting, executing, and continuously improving the MDM Strategy. Manages day-to-day operations and coordinates cross-functional teams. |
| **S (Supportive)** | Data Governance Manager (DG Mgr) | Supports alignment of the MDM Strategy with broader data governance frameworks, policies, and standards, including AI governance and regulatory compliance. |
| **C (Consulted)** | Data Owner (D-Owner), Data Architect (D-Arch), AI Ethics Officer | Provide domain-specific requirements, business rules, architectural guidance, and ethical oversight to ensure the MDM architecture and governance meet business and regulatory needs. |
| **I (Informed)** | Data Governance Council (DGC), Chief Information Officer (CIO), Chief Analytics and AI Officer (CAIO) | Kept informed of progress, key decisions, risks, and performance metrics related to the MDM Strategy and its integration with enterprise data and AI governance programs. |

### 2.2. Section-Level RASCI

| Strategy Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Vision, Goals, and Metrics | MDM Mgr | D-Owner, Business Stakeholders, AI Ethics Officer | CDO |
| MDM Architecture | D-Arch (MDM) | Enterprise Architect, D-Arch, Cloud Architect | CDO |
| Governance Model | DG Mgr | DGC, MDM Mgr, AI Ethics Officer | CDO |
| Technology Selection | MDM Mgr | D-Arch, IT Procurement, Security Officer | CIO / CDO |
| Implementation Roadmap | MDM Mgr | Project Management Office (PMO), Business Unit Leaders | CDO |

---

## 3. Template

> *The following is the standardized template for creating an MDM Strategy. Replace all placeholders `[...]` with organization-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Vision and Mission

> *Define the long-term vision for MDM and the mission of the MDM program. The vision should be aspirational and forward-looking, incorporating emerging trends such as AI governance and modern data architectures. The mission should clearly state the program’s purpose and scope.*

**Input needed**: Corporate strategic goals, interviews with executive stakeholders, AI governance policies.  
**Who fills this**: MDM Mgr drafts, CDO, DGC, and AI Ethics Officer review.

**Vision**: [e.g., "To enable a single, trusted, and governed view of our customers, products, suppliers, and AI data assets across all channels and systems, driving seamless customer experiences, operational excellence, and responsible AI adoption."]

**Mission**: [e.g., "To establish and operate an enterprise MDM program that delivers reliable, high-quality master data through effective governance, standardized processes, and a scalable, cloud-native technology platform aligned with data mesh principles and AI governance frameworks."]

### 3.2. Goals and Objectives

> *List specific, measurable, achievable, relevant, and time-bound (SMART) goals for the MDM program. Include objectives that address traditional master data challenges as well as emerging needs such as AI data governance, compliance, and operational integration.*

**Input needed**: Business cases, pain point analysis, AI governance requirements, regulatory compliance needs.  
**Who fills this**: MDM Mgr drafts, business stakeholders and AI governance leads validate.

| # | Goal Category | Specific Objective | Metric | Target | Timeline |
|:--|:---|:---|:---|:---|:---|
| 1 | Improve Operational Efficiency | Reduce manual effort in customer data reconciliation and stewardship | Manual hours spent per week | < 10 hours | 12 Months |
| 2 | Enhance Analytics & BI | Increase confidence in sales reporting accuracy through master data consistency | Report restatements due to data errors | 0 per quarter | 18 Months |
| 3 | Support Digital Transformation | Enable a 360-degree real-time view of the customer on the e-commerce platform | % of customer attributes available in real-time | 95% | 24 Months |
| 4 | Strengthen AI Governance | Ensure master data and AI model metadata comply with EU AI Act and internal ethical standards | % compliance with AI governance policies | 100% | 18 Months |
| 5 | Accelerate Cloud Adoption | Migrate MDM platform to a cloud-native, multi-cloud architecture supporting data mesh principles | % of MDM workloads on cloud-native infrastructure | 80% | 24 Months |

### 3.3. MDM Governance Model

> *Describe the governance structure, roles, responsibilities, and processes that oversee the MDM program. Include emerging roles such as AI Ethics Officer and Data Product Manager. Address decision-making, stewardship, quality assurance, and compliance workflows.*

**Input needed**: `KA-01-governance-framework.md`, `KA-01-roles-responsibilities.md`, AI governance policies.  
**Who fills this**: DG Mgr and MDM Mgr collaborate, with input from AI Ethics Officer.

**Key Roles & Responsibilities**:
- **MDM Process Owner**: [e.g., VP of Sales Operations for Customer domain]
- **Master Data Steward**: [e.g., Senior Sales Analyst responsible for validating new customer records]
- **MDM Operations Team**: [e.g., IT team responsible for maintaining the MDM hub]
- **AI Ethics Officer**: Oversees ethical use of AI-related master data and compliance with AI governance policies.
- **Data Product Manager**: Manages master data as a product, ensuring quality, availability, and usability.

**Decision Rights Matrix**:
| Decision Area | Decision Maker | Escalation Path |
|:---|:---|:---|
| New Customer attribute approval | Master Data Steward | MDM Process Owner |
| Match/Merge rule changes | MDM Mgr | Data Governance Council |
| AI model metadata updates | AI Ethics Officer | CAIO / CDO |

**Governance Workflows**:
- New Record Creation Workflow
- Record Update/Change Request Workflow
- Issue Resolution Workflow
- AI Data Compliance Review Workflow

### 3.4. MDM Architecture

> *Define the technical architecture for the MDM solution, including implementation style, technology stack, and integration with existing data landscapes. Incorporate modern architectural paradigms such as Data Mesh, Data Fabric, Lakehouse, and multi-cloud strategies.*

**Input needed**: `KA-02-architecture-blueprint.md`, `KA-06-integration-architecture.md`, cloud strategy documents.  
**Who fills this**: D-Arch (MDM) drafts, Enterprise Architect and Cloud Architect review.

**Implementation Style**: [e.g., "A hybrid approach will be adopted, starting with a Registry style for initial implementation, evolving to a Centralized (Transactional) style for the Customer domain, and progressively integrating Data Mesh principles to enable domain-oriented data ownership and self-service capabilities."]

**Core Components**:
- **MDM Hub**: [e.g., Semarchy, Profisee, Informatica MDM]
- **Data Integration Layer**: [e.g., Talend, MuleSoft, Azure Data Factory, Apache Kafka for event streaming]
- **Data Quality Engine**: [e.g., Trillium, Informatica IDQ, Great Expectations]
- **Data Modeling Tool**: [e.g., Erwin, ER/Studio]
- **Cloud Infrastructure**: Multi-cloud deployment leveraging AWS, Azure, or GCP with container orchestration (Kubernetes)
- **Data Lakehouse Integration**: Integration with Lakehouse platforms (e.g., Databricks, Snowflake) for unified data storage and analytics

**Integration Patterns**:
- Batch ETL for initial load from legacy systems
- Real-time APIs and event streaming for integration with Salesforce (CRM), e-commerce platforms, and AI model registries
- Data contracts to formalize data exchange agreements between domains and consumers

### 3.5. Implementation Roadmap

> *Provide a high-level, phased roadmap for MDM implementation. Break down the program into manageable phases by data domain, business unit, or technology platform. Include milestones for governance, technology adoption, and compliance.*

**Input needed**: Project management estimates, business priorities, regulatory deadlines.  
**Who fills this**: MDM Mgr drafts, PMO and business leaders review.

| Phase | Timeline | Data Domain(s) | Key Deliverables |
|:---|:---|:---|:---|
| **Phase 1: Foundation** | Q1-Q2 2026 | Customer (B2B) | MDM platform installed, governance model defined, data profiling complete, golden record for 10 core attributes, initial AI metadata integration |
| **Phase 2: Expansion** | Q3-Q4 2026 | Product | Product master implemented, integration with ERP and PIM systems, data quality scorecards live, data contracts established |
| **Phase 3: Optimization** | 2027 | Supplier, Customer (B2C) | Automated stewardship workflows, hierarchy management, MDM extended to new business units, cloud-native migration underway |
| **Phase 4: AI and Data Products** | 2027-2028 | AI Model Metadata, Data Products | Integration of AI governance workflows, data product management, compliance with EU AI Act, operationalization of MLOps and DataOps |

---

## 4. Example

> *This example illustrates an MDM Strategy for a fictional multinational company, GlobalRetail Inc., incorporating modern data management and AI governance considerations.*

### 4.1. Vision and Mission

**Vision**: "To power GlobalRetail's journey to becoming the world's leading omnichannel retailer through a single, trusted, and real-time view of our customers, products, suppliers, and AI data assets, enabling responsible innovation and superior customer experiences."

**Mission**: "To establish and operate a federated MDM program that empowers business domains to manage their master data with central oversight, ensuring consistent data quality, streamlined operations, deep analytical insights, and ethical AI governance across the enterprise."

### 4.2. Goals and Objectives

| # | Goal Category | Specific Objective | Metric | Target | Timeline |
|:--|:---|:---|:---|:---|:---|
| 1 | Enhance Customer Experience | Unify customer profiles from in-store, online, and mobile channels | % of customers with a single, unified ID | 98% | 24 Months |
| 2 | Accelerate Time-to-Market | Reduce the time required to launch a new product online | New Product Introduction (NPI) cycle time | < 5 days | 18 Months |
| 3 | Improve Supply Chain Visibility | Create a single source of truth for supplier information | Supplier onboarding time | < 48 hours | 12 Months |
| 4 | Ensure AI Compliance | Achieve full compliance with EU AI Act for AI-related master data | % compliance with AI governance policies | 100% | 18 Months |
| 5 | Modernize Architecture | Transition MDM platform to a cloud-native, multi-cloud environment | % of workloads migrated | 80% | 24 Months |

### 4.3. MDM Governance Model

**Key Roles & Responsibilities**:
- **MDM Process Owner**: VP of Merchandising for Product domain; VP of Marketing for Customer domain.
- **Master Data Steward**: Senior Merchandising Specialist responsible for product hierarchy management.
- **MDM Operations Team**: Central IT team managing the Profisee MDM platform.
- **AI Ethics Officer**: Oversees ethical use and compliance of AI-related master data.
- **Data Product Manager**: Manages master data as a product, ensuring quality and usability.

**Decision Rights Matrix**:
| Decision Area | Decision Maker | Escalation Path |
|:---|:---|:---|
| New product attribute approval | Product Data Steward | VP of Merchandising |
| Cross-domain matching rules | MDM Manager | Data Governance Council |
| AI model metadata updates | AI Ethics Officer | CAIO / CDO |

### 4.4. MDM Architecture

**Implementation Style**: "A federated, multi-domain MDM approach using Profisee. The Customer domain is managed centrally, while the Product domain is managed by the Merchandising business unit with central governance and technical support. The architecture leverages Data Mesh principles to enable domain ownership and self-service."

**Core Components**:
- **MDM Hub**: Profisee Platform
- **Data Integration Layer**: Microsoft Azure Data Factory (ADF), Apache Kafka for event streaming
- **Data Quality Engine**: Profisee Data Quality
- **Data Modeling Tool**: Profisee Data Modeling
- **Cloud Infrastructure**: Azure Kubernetes Service (AKS) for container orchestration
- **Lakehouse Integration**: Databricks Lakehouse for unified analytics

**Integration Patterns**:
- ADF pipelines for batch ingestion from SAP (ERP) and legacy systems
- Real-time REST APIs and event streaming for synchronizing customer data with Salesforce Marketing Cloud, Sitecore e-commerce platform, and AI model registries
- Data contracts formalizing data exchange agreements between domains

### 4.5. Implementation Roadmap

| Phase | Timeline | Data Domain(s) | Key Deliverables |
|:---|:---|:---|:---|
| **Phase 1: Customer 360** | Q1-Q3 2026 | Customer (B2C) | Unified customer profile, integration with Salesforce and Sitecore, real-time de-duplication, initial AI metadata integration |
| **Phase 2: Product Master** | Q4 2026 - Q2 2027 | Product | Centralized product catalog, enriched product attributes, syndication to e-commerce channels, data contracts implemented |
| **Phase 3: Supplier Hub** | Q3-Q4 2027 | Supplier | Streamlined supplier onboarding, integration with Coupa (Procurement), supplier hierarchy management |
| **Phase 4: AI and Data Products** | 2027-2028 | AI Model Metadata, Data Products | AI governance workflows operationalized, data product management, compliance with EU AI Act, MLOps and DataOps integration |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Governance Framework | Knowledge Area | **templates/templates-KA-01-data-governance.md** |
| Data Architecture Blueprint | Knowledge Area | **templates/templates-KA-02-data-architecture.md** |
| MDM Governance Workflow | Deliverable | [10-master-data-governance-workflow.md](10-master-data-governance-workflow.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The strategy clearly defines an MDM vision and mission aligned with executive-level business goals, including AI governance and modern data management paradigms.
- [ ] At least 3-5 SMART goals are defined with clear metrics, targets, and timelines, covering operational, analytical, and compliance objectives.
- [ ] The governance model explicitly defines key roles, decision rights, stewardship processes, and emerging roles such as AI Ethics Officer and Data Product Manager.
- [ ] The chosen architectural style (centralized, federated, hybrid, or mesh-enabled) is justified and aligns with enterprise architecture and cloud strategy.
- [ ] The implementation roadmap is phased, realistic, prioritizes data domains based on business value, and includes AI governance and cloud migration milestones.
- [ ] The strategy has been reviewed and formally signed off by the CDO, AI Ethics Officer, and key business stakeholders.

### 5.2. Review Checklist

| Category | Question | Pass/Fail |
| :--- | :--- | :--- |
| **Strategic Alignment** | Does the strategy solve a clearly articulated business problem and support digital transformation goals? | |
| **Completeness** | Are all major components (Vision, Goals, Governance, Architecture, Roadmap) included and sufficiently detailed? | |
| **Feasibility** | Is the roadmap achievable given the organization's resources, budget, and technical capabilities? | |
| **Governance** | Are the roles, responsibilities, and decision-making processes unambiguous and inclusive of AI governance? | |
| **Clarity** | Is the document easy to understand for both business and technical audiences? | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs to this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Governance Charter | Provides the overall authority and mandate for all data-related initiatives, including MDM and AI governance. | `templates/templates-KA-01-data-governance.md` |
| Enterprise Data Model | Provides the conceptual and logical view of key data entities that will be managed as master data. | `templates/templates-KA-02-data-architecture.md` |
| AI Governance Framework | Provides policies and standards for managing AI-related data and models, relevant to MDM strategy. | `templates/templates-KA-13-big-data-data-science.md` |

### 6.2. Consumers (Outputs that use this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Golden Record Definition | The strategy sets the scope and priorities for which master data entities will have a golden record defined. | `02-golden-record-definition.md` |
| Master Data Governance Workflow | The strategy defines the high-level governance model that is detailed in the workflow. | `10-master-data-governance-workflow.md` |
| Data Product Management Plan | Builds upon the MDM strategy to manage master data as data products. | `11-data-product-management-plan.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| **Multi-Domain MDM Platforms** | Profisee, Semarchy, Informatica MDM, TIBCO EBX, Reltio | Pimcore (primarily PIM/MDM), OpenMDM | 
| **Data Integration Tools** | Talend, MuleSoft, Informatica PowerCenter, Azure Data Factory, AWS Glue | Apache NiFi, Airbyte, Meltano |
| **Data Quality & Profiling** | Ataccama, Informatica IDQ, Trillium, Monte Carlo | Great Expectations, Soda Core, OpenRefine |
| **Data Modeling Tools** | Erwin, ER/Studio, SAP PowerDesigner | Draw.io (for diagrams), Vertabelo (freemium) |
| **AI Metadata Management** | MLflow, DataRobot MLOps, Databricks Model Registry | MLflow (open source), Kubeflow Pipelines |

### 7.2. Automation Opportunities

- **Automated Data Profiling**: Tools can automatically scan source systems to analyze data quality, identify potential master data, and suggest cleansing rules, accelerating the initial analysis phase.
- **Workflow Automation**: Stewardship tasks, such as change requests and approvals for new records, can be automated through workflows in the MDM platform, reducing manual effort and ensuring process consistency.
- **Automated DQ Monitoring**: Data quality rules can be executed automatically on a schedule, with alerts sent to data stewards when anomalies or rule violations are detected, enabling proactive quality management.
- **API-Driven Syndication**: The distribution of master data to consuming systems can be fully automated via real-time APIs, ensuring that downstream applications always have the most current and accurate information without manual intervention.
- **AI Governance Automation**: Integration of AI model metadata management with MDM platforms to automate compliance checks, lineage tracking, and ethical review workflows.
- **Cloud-Native Orchestration**: Use of container orchestration and infrastructure-as-code to automate deployment, scaling, and monitoring of MDM components in multi-cloud environments.

---

## 8. References

- **DAMA-DMBOK2**: Chapter 10, "Reference and Master Data Management"  
- **DAMA-DMBOK3 (Upcoming)**: Expected release June 2025, will include expanded coverage on AI governance, data mesh/fabric architectures, and agentic stewardship.  
- **Internal**: `reference/role-definitions.md`, `reference/tools-landscape.md`  
- **EU AI Act**: Regulatory framework for AI governance impacting master data and AI metadata management.  
- **Related Knowledge Areas**:  
  - `templates/templates-KA-01-data-governance.md`  
  - `templates/templates-KA-02-data-architecture.md`  
  - `templates/templates-KA-06-data-integration-interoperability.md`  
  - `templates/templates-KA-13-big-data-data-science.md`


---

# Golden Record Definition


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
  - [3.2. Master Data Domain Overview](#32-master-data-domain-overview)
  - [3.3. Golden Record Attributes](#33-golden-record-attributes)
  - [3.4. Identification and Matching Rules](#34-identification-and-matching-rules)
  - [3.5. Survivorship and Merge Rules](#35-survivorship-and-merge-rules)
  - [3.6. Data Quality Standards](#36-data-quality-standards)
- [4. Example](#4-example)
  - [4.1. Master Data Domain: Customer](#41-master-data-domain-customer)
  - [4.2. Golden Record Attributes (Partial Example)](#42-golden-record-attributes-partial-example)
  - [4.3. Identification and Matching Rules Example](#43-identification-and-matching-rules-example)
  - [4.4. Survivorship and Merge Rules Example](#44-survivorship-and-merge-rules-example)
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

> The **Golden Record Definition** is a formal, authoritative document that specifies the structure, attributes, data quality standards, and governance rules for the single, trusted version of a master data entity, commonly referred to as the "golden record." It serves as the foundational blueprint for creating the most accurate, complete, and reliable view of critical business entities such as Customer, Product, Supplier, or Employee.  
>
> By establishing a consistent, enterprise-wide understanding of what constitutes a golden record, this definition helps eliminate data silos, reduce inconsistencies, and support integrated business processes. It is essential for enabling effective data integration, quality assurance, governance, and advanced analytics initiatives, including AI and machine learning applications that rely on high-quality master data.  
>
> In the evolving data landscape, the Golden Record Definition also supports compliance with emerging regulations (e.g., EU AI Act alongside GDPR/HIPAA/CCPA), and aligns with modern data architectures like Data Mesh and Lakehouse, ensuring master data remains a trusted, governed data product.  
>
> Looking forward to DAMA-DMBOK 3.0, the Golden Record Definition will increasingly emphasize agentic data stewardship, data contracts, and the treatment of master data as a first-class data product, integrating tightly with AI governance frameworks and operationalizing MLOps, DataOps, and FinOps practices.

### 1.2. Scope

**Global** — The Golden Record Definition is a global standard applicable across the entire organization, regardless of business unit or geography. While individual master data domains (e.g., Customer, Product, Supplier) will have domain-specific golden record definitions, the methodology, governance framework, and template structure remain consistent enterprise-wide.  
>
> This universality ensures that master data management (MDM) is scalable, repeatable, and aligned with enterprise data governance and AI governance strategies. It also facilitates interoperability across multi-cloud environments and hybrid data architectures, supporting the organization's digital transformation and data-driven decision-making goals.  
>
> The scope includes integration with modern architectural paradigms such as Data Mesh and Data Fabric, enabling decentralized ownership while maintaining centralized standards and interoperability. The golden record is positioned as a core data product, accessible via APIs and governed through data contracts, ensuring agility and compliance in dynamic environments.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-03: Data Modeling & Design | The Golden Record Definition provides the conceptual and logical data model for master data entities, detailing entities, attributes, and relationships that must be physically implemented in data stores and MDM platforms. It also supports evolving modeling techniques for data products and mesh domains. |
| KA-06: Data Integration & Interoperability | Serves as the canonical data model for integration processes, ensuring data from disparate sources is harmonized, conformed, and interoperable across systems, including cloud-native and data mesh environments. Supports data contracts and API-driven integration patterns. |
| KA-09: Metadata Management | Acts as a critical piece of business and technical metadata, capturing attribute definitions, data lineage, and governance rules. Metadata repositories store and manage these definitions to enable traceability, impact analysis, and support AI model explainability. |
| KA-10: Reference & Master Data Management | Central deliverable within this knowledge area, defining the authoritative master data records that underpin enterprise data consistency and quality. Incorporates emerging agentic stewardship roles and data product management concepts. |
| KA-11: Data Quality | Specifies the data quality dimensions, rules, and thresholds the golden record must meet, serving as a key input for data quality monitoring and remediation efforts. Integrates with DataOps pipelines and automated quality monitoring tools. |
| KA-12: Data Governance | Supports formal governance structures, roles, and policies to maintain the golden record definition, ensuring accountability and compliance with regulatory requirements and AI governance principles, including EU AI Act adherence. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | **MDM Manager** | Ultimately accountable for the completeness, accuracy, approval, and ongoing maintenance of the Golden Record Definition. Ensures alignment with enterprise MDM strategy, data governance, and AI governance frameworks. Oversees integration with modern architectures and compliance with emerging regulations. |
| **R (Responsible)** | **Data Steward** | Leads the creation and maintenance of the golden record definition. Facilitates collaboration with business stakeholders, documents attribute definitions, matching, survivorship, and data quality rules. Coordinates with technical teams for implementation feasibility, and integrates AI governance considerations. |
| **S (Supportive)** | **Data Quality Analyst** | Provides expertise in data profiling, quality metrics, and validation rules. Supports defining measurable data quality standards and monitoring criteria for the golden record. Collaborates on automation and DataOps integration. |
| **C (Consulted)** | **Data Owner, Subject Matter Experts (SMEs)** | Provide business context, validate attribute definitions, and ensure the definition meets operational and strategic needs. Consulted on domain-specific rules, compliance, and AI governance implications. |
| **I (Informed)** | **Data Engineer** | Informed of the finalized definition to implement data pipelines, transformations, and storage structures. Ensures technical feasibility and integration with MDM platforms, data lakes, and AI/ML pipelines. Supports automation and cloud-native deployments. |
| **C (Consulted)** | **AI Ethics Officer / CAIO** | Consulted to ensure the golden record definition supports responsible AI practices, data privacy, and compliance with AI governance policies, including EU AI Act requirements. Advises on explainability, fairness, and ethical data use. |
| **S (Supportive)** | **MLOps Engineer** | Supports integration of golden record data into machine learning pipelines, ensuring data quality and governance compliance in model training and deployment. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| 1. Overview | Data Steward | Data Owner, SME, AI Ethics Officer | MDM Manager |
| 2. RASCI Assignment | MDM Manager | Data Governance Manager | MDM Manager |
| 3. Template | Data Steward | MDM Manager, Data Architect | MDM Manager |
| 4. Example | Data Steward | SME | MDM Manager |
| 5. Quality Criteria | Data Quality Analyst | Data Steward, AI Ethics Officer | MDM Manager |
| 6. Related Outputs | Data Steward | Data Architect | MDM Manager |
| 7. Tools & Automation | MDM Manager | Data Architect, Data Engineer | MDM Manager |
| 8. References | Data Steward | Data Governance Manager | MDM Manager |

---

## 3. Template

> *The following is the standardized template for creating a Golden Record Definition. Replace all placeholders `[...]` with domain-specific information. Each section includes inline guidance in blockquotes to ensure clarity and completeness.*

### 3.1. Document Control

| Field | Value |
| :--- | :--- |
| Document Title | Golden Record Definition: [Master Data Domain, e.g., Customer] |
| Document ID | MDM-DEF-[Domain Code]-001 |
| Version | [e.g., 1.0] |
| Status | [Draft, In Review, Approved] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Owner Name] |
| Author | [Data Steward Name] |
| Reviewers | [List of Reviewers] |
| Approver | [MDM Manager Name] |
| Related Documents | [List related deliverables, e.g., Match & Merge Rules, Data Quality Rules, Data Survivorship Rules] |

### 3.2. Master Data Domain Overview

> *Provide a high-level description of the master data domain. Explain its business significance, key business processes it supports, and its role in modern data architectures and AI initiatives.*

**Description**: [e.g., The Customer domain encompasses all individuals and organizations that engage with the company through purchases, service interactions, or marketing activities. It includes both B2C and B2B customers.]

**Business Importance**: [e.g., A unified, accurate customer view is critical for personalized marketing, sales forecasting, customer service excellence, regulatory compliance, and AI-driven analytics. It supports omnichannel engagement and enables data mesh principles by serving as a trusted data product.]

**Architectural Context**: [e.g., The golden record will be integrated into the enterprise data fabric, accessible via APIs and data products, supporting cloud-native applications and AI/ML pipelines. It supports multi-cloud deployments and real-time data access for operational and analytical use cases.]

### 3.3. Golden Record Attributes

> *This is the core of the definition. List every attribute that will be part of the golden record. For each attribute, provide a clear business definition, data type, format examples, source systems, criticality, and data quality rules.*

| Attribute Name | Business Definition | Data Type & Length | Format/Example | Source System(s) | Criticality | DQ Rules |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CustomerID` | Unique identifier for the customer across all systems. | `VARCHAR(20)` | `CUST-12345` | MDM System, CRM | High | Not Null, Unique, Immutable |
| `FirstName` | The legal first name of the individual customer. | `VARCHAR(100)` | `John` | CRM, ERP | High | Not Null, Alphabetic, No Special Characters |
| `LastName` | The legal last name of the individual customer. | `VARCHAR(100)` | `Smith` | CRM, ERP | High | Not Null, Alphabetic |
| `EmailAddress` | Primary email address for communication and login. | `VARCHAR(255)` | `john.smith@example.com` | CRM, Marketing | High | Not Null, Valid Email Format, Verified |
| `PhoneNumber` | Primary contact phone number. | `VARCHAR(20)` | `+1-555-123-4567` | CRM, Billing | Medium | Valid Format, Normalized |
| `StreetAddress` | Street address line for primary residence or billing. | `VARCHAR(255)` | `123 Main St` | Billing, Shipping | High | Not Null, Standardized via Address Validation API |
| `City` | City of the primary address. | `VARCHAR(100)` | `Anytown` | Billing, Shipping | High | Not Null |
| `State` | State or province of the primary address. | `VARCHAR(50)` | `CA` | Billing, Shipping | High | Valid Abbreviation, ISO Codes |
| `PostalCode` | Postal or ZIP code of the primary address. | `VARCHAR(20)` | `90210` | Billing, Shipping | High | Valid Format per Country |
| `Country` | Country of the primary address. | `VARCHAR(50)` | `USA` | Billing, Shipping | High | ISO 3166-1 Alpha-3 Code |
| `DateOfBirth` | Customer's date of birth for identity verification. | `DATE` | `1980-01-01` | CRM | Medium | Valid Date, Age Verification |
| `CustomerStatus` | Current status of the customer relationship. | `VARCHAR(20)` | `Active`, `Inactive` | CRM, ERP | High | Controlled Vocabulary |
| `ConsentFlag` | Indicates if customer has consented to data processing. | `BOOLEAN` | `True` / `False` | Marketing, CRM | High | Must Comply with GDPR/CCPA, EU AI Act |

### 3.4. Identification and Matching Rules

> *Define the logic used to identify unique entities and match records from different source systems. This is fundamental to creating the golden record and must balance precision and recall to avoid duplicates or false merges.*

**Unique Identifier**: [e.g., The `CustomerID` generated and maintained by the MDM system is the definitive unique identifier for each customer.]

**Matching Strategy**: [e.g., A hybrid approach combining deterministic and probabilistic matching is employed to maximize accuracy and minimize false positives.]

**Deterministic Match Rules (Exact Matches)**:
1. Exact match on `EmailAddress` (case-insensitive).
2. Exact match on `CustomerID` where available.
3. Exact match on `LoyaltyID` if applicable.

**Probabilistic Match Rules (Fuzzy Matches)**:
1. Fuzzy match on `FirstName` and `LastName` using Jaro-Winkler similarity > 0.9 combined with exact match on `PostalCode`.
2. Fuzzy match on normalized `PhoneNumber` and `LastName`.
3. Use of machine learning models to score match likelihood based on multiple attributes and historical merge outcomes.

**Additional Considerations**:
- Incorporate AI governance principles to ensure matching algorithms are explainable, auditable, and free from bias.
- Regularly review and tune match thresholds based on feedback, data quality monitoring, and operational outcomes.
- Leverage data contracts to formalize expectations and SLAs for source system data quality impacting matching.
- Document matching logic and rationale in metadata repositories for transparency and compliance.

### 3.5. Survivorship and Merge Rules

> *Define the rules that determine which attribute value "survives" to become part of the golden record when source systems have conflicting or overlapping information. These rules must be transparent, auditable, and aligned with business priorities.*

| Attribute Name | Survivorship Rule | Rationale |
| :--- | :--- | :--- |
| `FirstName` | Source System Priority: 1. CRM, 2. ERP, 3. External Data Provider | CRM is considered the most reliable source for customer-provided name information. |
| `LastName` | Source System Priority: 1. CRM, 2. ERP | Consistent with `FirstName` to maintain name integrity. |
| `EmailAddress` | Most Recently Updated and Verified | The latest verified email is most likely to be current and valid for communication. |
| `PhoneNumber` | Source System Priority: 1. Billing, 2. CRM | Billing system phone numbers are typically maintained for payment and contact purposes, thus more reliable. |
| `StreetAddress` | Use Address Validation Service Result; if multiple valid addresses, choose Most Recently Updated | External address validation ensures accuracy and standardization; recency indicates current residence. |
| `CustomerStatus` | Business Rule: If any source marks as `Inactive`, mark golden record as `Inactive` unless overridden by Data Owner | Ensures conservative approach to customer status to avoid erroneous active status. |
| `ConsentFlag` | Logical AND across all source systems | Ensures compliance with privacy regulations by only marking consent if all sources confirm. |

> *Note: Survivorship rules should be codified in MDM platform configurations or data contracts to enable automated enforcement and auditability. These rules must also be aligned with AI governance policies to prevent unintended bias or data misuse.*

### 3.6. Data Quality Standards

> *Define the specific, measurable data quality dimensions, thresholds, and targets for the golden record. These standards support continuous monitoring and improvement, and are critical for trustworthy master data.*

| DQ Dimension | Metric | Target | Threshold (Actionable) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Completeness** | % of records with all `High` criticality attributes populated | > 99% | < 98% | Missing critical attributes trigger data remediation workflows. |
| **Uniqueness** | % of duplicate records (post-match & merge) | < 0.1% | > 0.2% | Duplicate detection alerts trigger investigation and correction. |
| **Validity** | % of records where all attributes pass format and business rules validation | > 99.5% | < 99% | Includes format checks, controlled vocabularies, and external validation (e.g., address verification). |
| **Accuracy** | % of records verified against trusted external sources (e.g., postal services, credit bureaus) | > 98% | < 95% | Accuracy assessments support confidence in analytics and AI models. |
| **Timeliness** | % of source system updates reflected in the golden record within 24 hours | > 99.9% | < 99% | Ensures golden record reflects current state for operational use and AI pipelines. |
| **Consistency** | % of attributes consistent across source systems before merging | > 98% | < 95% | High inconsistency rates may indicate source system issues or integration errors. |
| **Compliance** | % of records compliant with data privacy and AI governance policies | 100% | < 100% | Includes consent flags, data retention, and usage restrictions per EU AI Act and GDPR. |

---

## 4. Example

> *This section provides a realistic, filled-in example for the **Customer** domain at a fictional company, **GlobalRetail Inc.** It illustrates how the template is applied in practice, including modern considerations such as AI governance and cloud-native architectures.*

### 4.1. Master Data Domain: Customer

**Description**: The Customer domain at GlobalRetail Inc. represents all individuals who have registered for an online account, made a purchase, or enrolled in the loyalty program. It includes both retail consumers and business customers.

**Business Importance**: A unified customer view is essential for personalizing the e-commerce experience, targeting promotions, managing loyalty programs, and providing efficient customer support. It directly impacts revenue, customer satisfaction, and regulatory compliance.  
>
> The golden record supports AI-driven personalization models and real-time decisioning systems, integrated via the company’s data mesh architecture and accessible through the enterprise data fabric. It enables multi-cloud data sharing and supports compliance with GDPR and the EU AI Act.

### 4.2. Golden Record Attributes (Partial Example)

| Attribute Name | Business Definition | Data Type & Length | Format/Example | Source System(s) | Criticality | DQ Rules |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `LoyaltyID` | Unique identifier for the customer's loyalty program account. | `VARCHAR(15)` | `GL-8934729` | Loyalty Platform | High | Not Null, Unique, Starts with 'GL-' |
| `FirstName` | The legal first name of the customer. | `VARCHAR(100)` | `Jennifer` | E-commerce, CRM | High | Not Null, Alphabetic |
| `LastName` | The legal last name of the customer. | `VARCHAR(100)` | `Walters` | E-commerce, CRM | High | Not Null, Alphabetic |
| `EmailAddress` | The primary email used for login and communication. | `VARCHAR(255)` | `jen.walters@email.com` | E-commerce | High | Not Null, Valid Email Format, Verified |
| `ShippingAddress` | The primary address used for shipping orders. | `VARCHAR(255)` | `456 Oak Avenue` | E-commerce, Order Mgmt | High | Not Null, Standardized via API |
| `ConsentFlag` | Indicates if the customer has consented to marketing communications. | `BOOLEAN` | `True` | Marketing Platform | High | Must Comply with GDPR/CCPA, EU AI Act |

### 4.3. Identification and Matching Rules Example

**Deterministic Match Rules**:
1. Exact match on `EmailAddress` (case-insensitive).
2. Exact match on `LoyaltyID`.

**Probabilistic Match Rules**:
1. Fuzzy match on `FirstName` (Jaro-Winkler > 0.9) AND `LastName` (Jaro-Winkler > 0.9) AND exact match on `PostalCode`.
2. Fuzzy match on normalized `PhoneNumber` AND `LastName`.

> *Matching algorithms are periodically reviewed and tuned by the Data Steward and AI Ethics Officer to ensure fairness, transparency, and compliance with AI governance policies. Machine learning models used for matching are versioned and monitored for drift.*

### 4.4. Survivorship and Merge Rules Example

| Attribute Name | Survivorship Rule | Rationale |
| :--- | :--- | :--- |
| `FirstName` | Source System Priority: 1. E-commerce, 2. CRM | The e-commerce platform is where customers manage their own profile, thus considered most accurate. |
| `ShippingAddress` | Most Recently Updated | The address used in the most recent order is most likely current and valid. |
| `ConsentFlag` | Logical AND across all source systems | Ensures compliance with privacy regulations by only marking consent if confirmed by all sources. |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Match & Merge Rules | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| Data Quality Rules (MDM) | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| Data Survivorship Rules | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| MDM Strategy | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| AI Governance Framework | Knowledge Area | **templates/templates-KA-12-data-handling-ethics.md** |
| Data Mesh Principles | Concept | [#](references/concepts-modern-paradigms.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] All `High` criticality attributes are identified, clearly defined, and agreed upon by Data Owners and SMEs.
- [x] Business definitions are clear, concise, and aligned with enterprise data governance and AI governance policies.
- [x] Data types, formats, and validation rules are specified for all attributes.
- [x] At least one deterministic match rule and supporting probabilistic match rules are defined.
- [x] Survivorship and merge rules are defined for all attributes with multiple source systems.
- [x] Data quality dimensions, metrics, thresholds, and targets are defined and measurable.
- [x] The definition supports compliance with relevant regulations including GDPR, HIPAA, CCPA, and the EU AI Act.
- [x] The definition has been formally reviewed, approved, and signed off by the MDM Manager, Data Owner, and AI Ethics Officer.
- [x] The definition is integrated into metadata repositories and aligned with enterprise data architecture standards.
- [x] The definition supports automation opportunities for rule generation, monitoring, and documentation.
- [x] The definition incorporates forward-looking DAMA-DMBOK 3.0 principles including agentic stewardship, data contracts, and data product management.

### 5.2. Review Checklist

| Review Area | Question | Reviewer Role |
| :--- | :--- | :--- |
| **Business Alignment** | Does this definition accurately reflect the business's need for a single, trusted view of this entity? | Data Owner, SME |
| **Technical Feasibility** | Can the defined attributes, matching, and survivorship rules be implemented with current tools and architectures (including cloud-native and data mesh)? | Data Architect, Data Engineer |
| **Data Quality** | Are the data quality targets realistic, measurable, and sufficient to ensure the golden record is trustworthy? | Data Quality Analyst |
| **Governance & Compliance** | Are roles, responsibilities, and compliance requirements (including AI governance) clearly defined and assigned? | MDM Manager, AI Ethics Officer |
| **Completeness** | Have all relevant source systems, attributes, and data domains been considered? | Data Steward |
| **Security & Privacy** | Does the definition ensure data privacy, consent management, and compliance with regulations? | Data Privacy Officer, AI Ethics Officer |
| **Automation Readiness** | Is the definition structured to support automation in profiling, rule generation, and monitoring? | Data Engineer |
| **Future-Proofing** | Does the definition incorporate emerging best practices from DAMA-DMBOK 3.0 and evolving data management paradigms? | Data Governance Manager |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | File Path | Description |
| :--- | :--- | :--- |
| MDM Strategy | `templates/templates-KA-10-reference-master-data.md` | Provides strategic context and priorities guiding which golden records to define and how to align with enterprise goals. |
| Data Governance Framework | `templates/templates-KA-01-data-governance.md` | Defines governance policies, roles, and processes that underpin the golden record definition lifecycle. |
| Data Quality Assessment Report | `templates/templates-KA-11-data-quality.md` | Provides baseline data quality insights to inform attribute selection and quality thresholds. |
| AI Governance Framework | `templates/templates-KA-12-data-handling-ethics.md` | Provides principles and policies for responsible AI use impacting master data definitions. |

### 6.2. Consumers (Outputs)

| Output Name | File Path | Description |
| :--- | :--- | :--- |
| Match & Merge Rules | `templates/templates-KA-10-reference-master-data.md` | This definition is the direct input for detailed technical implementation of match and merge logic in MDM tools. |
| Master Data Model | `templates/templates-KA-10-reference-master-data.md` | The attributes and structure defined here become part of the official master data model used across the enterprise. |
| Data Quality Rules (MDM) | `templates/templates-KA-10-reference-master-data.md` | The data quality standards defined here are translated into executable rules for monitoring and remediation. |
| Data Survivorship Rules | `templates/templates-KA-10-reference-master-data.md` | Survivorship logic is formalized and expanded in this dedicated deliverable for operational use. |
| Data Product Catalog | `references/reference-materials.md` | The golden record is a key data product listed and managed in the enterprise data product catalog. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

- **MDM Platforms** (e.g., Informatica MDM, IBM InfoSphere, SAP Master Data Governance) for managing golden record definitions, match & merge, and survivorship rules.
- **Data Quality Tools** (e.g., Talend, Collibra, Ataccama) for profiling, monitoring, and enforcing data quality standards.
- **Metadata Repositories** (e.g., Apache Atlas, Collibra) for capturing attribute definitions, lineage, and governance metadata.
- **AI Governance Platforms** (e.g., Fiddler, IBM Watson OpenScale) for monitoring AI model fairness and explainability related to master data.
- **DataOps and MLOps Tools** (e.g., MLflow, Kubeflow, Airflow) for automating data pipelines and model lifecycle management.
- **Cloud-Native Data Platforms** (e.g., Snowflake, Databricks Lakehouse) supporting scalable, multi-cloud golden record storage and access.

### 7.2. Automation Opportunities

- Automated generation of data quality rules from attribute definitions.
- Continuous monitoring and alerting on data quality metrics aligned with golden record standards.
- Automated match & merge rule testing and tuning using machine learning feedback loops.
- Integration of golden record updates into AI/ML pipelines via DataOps and MLOps workflows.
- Use of data contracts to automate SLA enforcement and data quality validations across source systems.
- Automated documentation updates and metadata synchronization to maintain transparency and auditability.

---

## 8. References

- DAMA International. (2024). *DAMA-DMBOK2: Data Management Body of Knowledge* (2nd ed.). Technics Publications.  
- DAMA International. (2025). *DAMA-DMBOK3: Data Management Body of Knowledge* (3rd ed., forthcoming).  
- European Commission. (2021). *Proposal for a Regulation laying down harmonized rules on artificial intelligence (AI Act)*.  
- IBM. (2023). *AI Governance and Responsible AI Frameworks*.  
- Fowler, M. (2022). *Data Mesh Principles and Logical Architecture*.  
- Informatica. (2024). *Master Data Management Best Practices*.  
- Collibra. (2023). *Data Governance and Data Quality Integration*.  
- Talend. (2023). *Data Quality and Data Stewardship Automation*.  

---

*End of Golden Record Definition Template*


---

# Reference Data Standards


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
  - [3.2. Overview](#32-overview)
  - [3.3. Standard Specification](#33-standard-specification)
  - [3.4. Lifecycle Management](#34-lifecycle-management)
  - [3.5. Governance and Maintenance](#35-governance-and-maintenance)
  - [3.6. Distribution and Access](#36-distribution-and-access)
  - [3.7. Spreadsheet Template](#37-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Overview](#42-overview)
  - [4.3. Standard Specification](#43-standard-specification)
  - [4.4. Lifecycle Management](#44-lifecycle-management)
  - [4.5. Governance and Maintenance](#45-governance-and-maintenance)
  - [4.6. Distribution and Access](#46-distribution-and-access)
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

The **Reference Data Standards** document defines the rules, formats, and lifecycle management processes for reference data across the organization. Reference data is a specific type of master data that is used to classify or categorize other data. Examples include country codes, currency codes, order statuses, and product categories. These standards are essential for ensuring consistency, integrity, and interoperability of data across different systems and business processes.

> The purpose of Reference Data Standards is to create a common, authoritative language for categorizing business data, thereby reducing ambiguity, improving data quality, and enabling meaningful data integration and analysis.  
>  
> In the evolving data management landscape, these standards also support emerging paradigms such as data mesh and data fabric architectures by providing consistent domain-level vocabularies that enable decentralized data ownership while maintaining interoperability. Furthermore, as AI governance becomes critical, well-defined reference data standards underpin trustworthy AI models by ensuring consistent and accurate categorical inputs.

### 1.2. Scope

**Global** — These standards apply to all reference data sets used across the entire organization, regardless of the system, department, or geographical location. While specific reference data sets may have their own stewards and lifecycles, the framework and rules defined in this document are universal.

> The scope includes reference data used in cloud-native environments, multi-cloud deployments, and hybrid architectures, ensuring that standards accommodate modern data platforms such as lakehouses and support compliance with regulations including GDPR, HIPAA, CCPA, and the emerging EU AI Act.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The overall Data Governance program provides the authority and oversight for creating and enforcing these standards. The Data Governance Manager is accountable for this output. Reference data standards are foundational to effective governance, especially in AI governance contexts where data quality and lineage are critical. |
| KA-03: Data Modeling and Design | Reference data standards inform data models by providing the valid domain values for attributes, ensuring that models are consistent with enterprise-wide classifications. This supports semantic consistency across data products and data contracts. |
| KA-06: Data Integration & Interoperability | Standardized reference data is a prerequisite for successful data integration, as it allows for the consistent mapping and transformation of data between systems. It also facilitates interoperability in data mesh and fabric architectures. |
| KA-10: Reference and Master Data Management | This deliverable is a core artifact within this knowledge area, defining the standards that govern master and reference data sets. |
| KA-11: Data Quality | Adherence to reference data standards is a key measure of data quality. These standards prevent data entry errors and ensure the consistency of categorical data, which is critical for reliable analytics and AI model training. |
| KA-14: Data Security and Privacy | Reference data standards contribute to compliance with data security and privacy regulations by ensuring that sensitive categorical data is properly classified and managed. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Governance Manager (DG Mgr) | Ultimately answerable for the creation, maintenance, and enforcement of the Reference Data Standards. Ensures the standards align with business needs, governance policies, and regulatory compliance, including emerging AI governance requirements. |
| **R (Responsible)** | Reference Data Manager (RefData Mgr) | Responsible for drafting, documenting, and updating the standards. Manages the central repository of reference data and facilitates the standard-setting process, including integration with MLOps and DataOps workflows. |
| **S (Supportive)** | Data Steward (D-Steward) | Supports the process by providing domain expertise, validating reference data sets, and managing the lifecycle of specific reference data within their domain. Acts as an agentic steward, proactively ensuring data quality and compliance. |
| **C (Consulted)** | Subject Matter Expert (SME) | Provides deep business context and requirements for specific reference data sets, ensuring the standards are practical and meet business needs, including AI ethics considerations where applicable. |
| **I (Informed)** | Data Engineer (D-Eng) | Kept informed of the standards to ensure that data pipelines, systems, and applications are designed to consume and enforce the standardized reference data, including in cloud-native and multi-cloud environments. |

### 2.2. Section-Level RASCI

| Standard Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Standard Specification | RefData Mgr | SME, D-Steward | DG Mgr |
| Lifecycle Management | RefData Mgr | D-Steward | DG Mgr |
| Governance Process | DG Mgr | RefData Mgr | DG Mgr |
| Maintenance & Change Control | RefData Mgr | D-Steward | DG Mgr |

---

## 3. Template

> *The following is the standardized template for defining a new Reference Data Standard. This template should be filled out for each new reference data set that is brought under governance.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Standard Name | [Name of the Reference Data Set, e.g., "Country Codes"] |
| Standard ID | [Unique ID, e.g., RDS-001] |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Data Steward | [Name of the assigned Data Steward] |
| Data Domain | [e.g., Customer, Product, Finance] |
| AI Governance Considerations | [e.g., Impact on AI models, ethical use guidelines] |

### 3.2. Overview

> *Provide a brief description of the reference data set, its purpose, and its importance to the business. Explain what it is used to classify or categorize.*

**Input needed**: Business context from SMEs.  
**Who fills this**: Reference Data Manager, with input from the Data Steward.

[Insert Overview Description]

> Consider including notes on how this reference data supports data mesh domains or data product definitions, and any relevant compliance or AI governance implications.

### 3.3. Standard Specification

> *This section defines the technical and business rules for the reference data itself. It is the core of the standard.*

**Input needed**: Data modeling standards, external standards (e.g., ISO), business requirements.  
**Who fills this**: Reference Data Manager.

#### 3.3.1. Code Format and Structure

> *Define the exact format of the reference data codes. Specify data type, length, character set, and any patterns.*

| Attribute | Specification |
| :--- | :--- |
| Data Type | [e.g., VARCHAR, INTEGER] |
| Length | [e.g., 2 characters, 10 digits] |
| Pattern / Regex | [e.g., `^[A-Z]{2}$`] |
| Case Sensitivity | [e.g., Case-insensitive] |
| Encoding | [e.g., UTF-8] |

#### 3.3.2. Value Definitions

> *Provide a table listing all valid codes and their corresponding descriptions or definitions. This is the actual reference data set.*

| Code | Description | Notes |
| :--- | :--- | :--- |
| [Code 1] | [Full description for Code 1] | [Any additional context or usage notes] |
| [Code 2] | [Full description for Code 2] | [e.g., Legacy code, do not use for new entries] |

#### 3.3.3. Sourcing and Authority

> *Specify the source of truth for this reference data. Is it created internally or adopted from an external standard (e.g., ISO, industry body)?*

- **Source Type**: [Internal / External]
- **External Standard (if applicable)**: [e.g., ISO 3166-1 Alpha-2]
- **Source System / Authority**: [e.g., "Internal, created and maintained by the Finance Department"]
- **Data Contracts**: [Reference any data contracts or SLAs governing this reference data]

### 3.4. Lifecycle Management

> *Define the processes for managing the reference data set over time, from creation to retirement.*

**Input needed**: Change management procedures, governance framework.  
**Who fills this**: Data Steward, in consultation with the Reference Data Manager.

#### 3.4.1. Process for Adding New Values

> *Describe the step-by-step process for requesting, reviewing, and approving a new code/value.*

1.  **Request**: [Who can request a new value and how? e.g., "Submit a change request ticket in Jira."]
2.  **Review**: [Who reviews the request? e.g., "The Data Steward for the domain."]
3.  **Approval**: [Who has the final approval authority? e.g., "The Data Governance Council."]
4.  **Implementation**: [How is the new value added to the master list and communicated? Include automation steps if applicable.]

#### 3.4.2. Process for Modifying Existing Values

> *Describe the process for changing a description or other attribute of an existing code. Note: Changing the code itself should be strongly discouraged and likely follow the retirement/addition process.*

1.  **Request**: Initiated by Data Steward or SME with justification.
2.  **Impact Analysis**: Evaluate downstream dependencies including AI models, data products, and contracts.
3.  **Review and Approval**: By Reference Data Manager and Data Governance Council.
4.  **Implementation**: Update metadata, notify consumers, and update documentation and data catalogs.

#### 3.4.3. Process for Retiring Values

> *Describe the process for deactivating or retiring a code that is no longer in use. This should include an impact analysis.*

1.  **Identification**: Data Steward identifies obsolete or deprecated codes.
2.  **Impact Analysis**: Assess impact on systems, reports, AI models, and data products.
3.  **Remediation Plan**: Define migration or substitution strategy.
4.  **Execution**: Implement changes with coordination from Data Engineering and DataOps teams.
5.  **Communication**: Notify all stakeholders and update documentation.
6.  **Archival**: Retired codes are flagged but retained for historical and audit purposes.

### 3.5. Governance and Maintenance

> *Define the roles and responsibilities for ongoing governance and maintenance of this specific reference data set.*

**Input needed**: RASCI matrix, role definitions.  
**Who fills this**: Data Governance Manager.

| Role | Responsibility |
| :--- | :--- |
| **Data Steward** | Manages the lifecycle, ensures data quality, resolves issues, and acts as an agentic steward proactively monitoring usage and compliance. |
| **Reference Data Manager** | Manages the central repository, enforces standards, integrates with MLOps/DataOps pipelines, and reports on compliance and AI governance metrics. |
| **Data Custodian** | Implements the reference data in the source system, manages access, and ensures secure distribution consistent with privacy and security policies. |
| **AI Ethics Officer** | (Optional) Reviews reference data usage in AI models to ensure ethical considerations are met. |

### 3.6. Distribution and Access

> *Describe how the authoritative reference data is made available to downstream systems and users.*

- **Distribution Mechanism**: [e.g., API, database replication, flat file export, data fabric integration]
- **Access Point**: [e.g., URL for the API, database connection string]
- **Update Frequency**: [e.g., Real-time, daily, weekly]
- **Access Controls**: [Describe authentication, authorization, and audit logging mechanisms]
- **Integration with Data Mesh**: [Describe how this reference data is exposed as a data product or via data contracts]

### 3.7. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-10_reference-data-standards.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

> *This is a filled-in example of the template for a "Country Code" reference data standard at the fictional company GlobalRetail Inc.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Standard Name | Country Codes |
| Standard ID | RDS-001 |
| Version | 2.1 |
| Effective Date | 2024-01-15 |
| Data Steward | John Doe, International Sales Manager |
| Data Domain | Customer & Supplier |
| AI Governance Considerations | Used as input for regional sales forecasting AI models; ensures ethical use by avoiding biased regional groupings. |

### 4.2. Overview

This standard defines the official list of country codes to be used across all GlobalRetail Inc. systems. Its purpose is to ensure that customer, supplier, and transactional data is tagged with a consistent, unambiguous country identifier. This is critical for international shipping, tax calculation, regional sales reporting, and compliance with trade regulations.

The standard supports GlobalRetail's data mesh initiative by providing a shared domain vocabulary for the Customer & Supplier domain. It also underpins AI governance by ensuring consistent categorical inputs for machine learning models used in demand forecasting and risk assessment.

### 4.3. Standard Specification

#### 4.3.1. Code Format and Structure

| Attribute | Specification |
| :--- | :--- |
| Data Type | VARCHAR |
| Length | 2 characters |
| Pattern / Regex | `^[A-Z]{2}$` |
| Case Sensitivity | Case-insensitive (stored as uppercase) |
| Encoding | UTF-8 |

#### 4.3.2. Value Definitions

| Code | Description | Notes |
| :--- | :--- | :--- |
| US | United States | |
| CA | Canada | |
| MX | Mexico | |
| GB | United Kingdom | Post-Brexit, use instead of individual country codes like ENG. |
| DE | Germany | |
| ... | ... | *List includes all 249 ISO 3166-1 Alpha-2 codes.* |

#### 4.3.3. Sourcing and Authority

- **Source Type**: External
- **External Standard (if applicable)**: ISO 3166-1 Alpha-2
- **Source System / Authority**: The authoritative list is maintained in the "Profisee" Master Data Management (MDM) platform.
- **Data Contracts**: The country code list is governed by the GlobalRetail Data Contract for Customer Domain Reference Data.

### 4.4. Lifecycle Management

#### 4.4.1. Process for Adding New Values

As this standard is based on an international ISO standard, new values are only added when the ISO 3166-1 standard is officially updated. The Reference Data Manager is subscribed to ISO update notifications.

1.  **Request**: The ISO issues an update.
2.  **Review**: The Reference Data Manager reviews the change and performs an impact analysis, including AI model retraining needs.
3.  **Approval**: Approval is automatic for ISO-driven changes, but the Data Governance Council is notified.
4.  **Implementation**: The new code is added to the Profisee MDM platform and an announcement is posted on the data governance portal. Automated workflows update downstream data products and notify data consumers.

#### 4.4.2. Process for Modifying Existing Values

Modifications (e.g., changing the official name of a country) follow the same ISO-driven process as additions. Any changes trigger a review of dependent AI models and data products to ensure consistency.

#### 4.4.3. Process for Retiring Values

When the ISO 3166-1 standard retires a code, the following process is initiated:

1.  **Impact Analysis**: The Data Steward and Reference Data Manager identify all systems, reports, AI models, and data products using the retired code.
2.  **Remediation Plan**: A plan is created to migrate all existing records to a new, valid code, including retraining AI models if necessary.
3.  **Execution**: Data Engineering executes the remediation plan with support from DataOps.
4.  **Deactivation**: Once all instances are migrated, the code is marked as "retired" in the MDM platform. It is not physically deleted for historical reporting and audit purposes.

### 4.5. Governance and Maintenance

| Role | Responsibility |
| :--- | :--- |
| **Data Steward (John Doe)** | Manages remediation plans for retired codes, provides context on country usage in sales reports, and monitors AI model impacts. |
| **Reference Data Manager** | Monitors ISO updates, manages the country code list in Profisee, integrates updates with MLOps pipelines, and reports on compliance. |
| **Data Custodian (IT MDM Team)** | Manages the Profisee platform, ensures the API for country codes is operational, and enforces access controls. |
| **AI Ethics Officer** | Reviews use of country codes in AI models to ensure compliance with ethical guidelines and regulatory requirements. |

### 4.6. Distribution and Access

- **Distribution Mechanism**: A REST API managed by the IT MDM Team, integrated with the enterprise data fabric.
- **Access Point**: `https://api.globalretail.com/v1/referencedata/countries`
- **Update Frequency**: Real-time. Updates in Profisee are immediately available via the API.
- **Access Controls**: OAuth 2.0 authentication with role-based authorization; audit logs maintained for all access.
- **Data Mesh Integration**: Exposed as a data product with defined SLAs and data contracts.

---

### 4.7. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Concept | [concepts/data-contracts.md](references/concepts-modern-paradigms.md) |
| AI Governance Framework | Guide | **guides/governance/ai-governance.md** |
| Data Mesh Principles | Guide | **guides/architecture/data-mesh.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The standard has a clearly defined owner (Data Steward).
- [x] The code format and all valid values are explicitly defined.
- [x] The source of truth (internal or external) is identified.
- [x] The lifecycle processes (add, modify, retire) are documented.
- [x] The governance roles for maintenance are assigned.
- [x] The distribution mechanism is documented and an access point is provided.
- [x] AI governance considerations are addressed, including ethical use and impact on AI models.
- [x] Integration with modern data architectures (data mesh, data fabric) is considered.
- [x] Compliance with relevant regulations (GDPR, HIPAA, CCPA, EU AI Act) is documented.

### 5.2. Review Checklist

| Review Area | Question | Reviewer |
| :--- | :--- | :--- |
| **Completeness** | Does the standard cover all necessary attributes and values for its business purpose? | SME, Data Steward |
| **Clarity** | Are the definitions and processes unambiguous and easy to understand? | DG Mgr |
| **Consistency** | Does the standard align with other existing data standards (e.g., naming conventions)? | RefData Mgr |
| **Feasibility** | Can the standard be technically implemented and enforced in key systems? | Data Engineer |
| **Compliance** | Does the standard comply with relevant external regulations (if any)? | Legal, Compliance |
| **AI Governance** | Are AI-related risks and ethical considerations addressed? | AI Ethics Officer |
| **Modern Architecture** | Does the standard support deployment in data mesh/fabric and cloud-native environments? | Enterprise Architect |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Standards | This document is a specific type of Data Standard and inherits its guiding principles from the main framework. | `templates/templates-KA-01-data-governance.md` |
| Data Contracts | Reference data standards inform data contracts that specify data quality and usage expectations. | `templates/templates-KA-10-reference-master-data.md` |

### 6.2. Consumers (Outputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Reference Data Tables | This standard defines the content and structure that will be implemented in physical reference data tables. | `./07-reference-data-tables.md` |
| Attribute Definitions | When defining attributes in a data model, this standard provides the permissible values for categorical attributes. | `templates/templates-KA-03-data-modeling-design.md` |
| Data Products | Reference data sets are often exposed as data products within a data mesh architecture. | `templates/templates-KA-10-reference-master-data.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Type | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| **MDM / RDM Platforms** | Profisee, Informatica MDM, TIBCO EBX, Semarchy | Talend Open Studio for MDM, OpenRefine |
| **Data Catalogs** | Collibra, Alation, data.world | Amundsen, DataHub |
| **Workflow/Ticketing** | Jira, ServiceNow | Redmine, MantisBT |
| **AI Governance Platforms** | IBM Watson OpenScale, Fiddler AI | AI Fairness 360, Explainability libraries |
| **Data Mesh Platforms** | Starburst, DataKitchen | Open Data Mesh Frameworks |

### 7.2. Automation Opportunities

- **Automated Validation**: Data quality rules can be automated to scan databases and identify values that do not conform to the published reference data standards, integrated with DataOps pipelines.
- **Automated Distribution**: Changes in the central MDM/RDM tool can automatically trigger cache invalidation or updates in downstream applications via webhooks or messaging queues, supporting real-time data fabric synchronization.
- **Lifecycle Workflow**: The process for requesting, approving, and implementing changes to reference data can be fully automated in a workflow tool like Jira or ServiceNow, with integration to data catalogs and governance dashboards.
- **AI Model Integration**: Automated triggers can notify MLOps pipelines to retrain models when reference data changes impact model features.
- **Compliance Monitoring**: Automated audits can verify adherence to regulatory requirements and AI governance policies related to reference data usage.

---

## 8. References

- **DAMA-DMBOK (2nd Edition)**: Chapter 10, "Reference and Master Data Management".  
- **DAMA-DMBOK 3.0 (forthcoming)**: Anticipated enhancements include expanded guidance on AI governance, data mesh/fabric integration, and agentic stewardship models.  
- **Internal Roles**: For detailed role descriptions, see `references/reference-materials.md`.  
- **ISO 3166-1**: The international standard for country codes, which serves as the source for the example in this document.  
- **EU AI Act**: Regulatory framework impacting AI governance and data management compliance.  
- **Data Mesh Principles**: See `references/concepts-modern-paradigms.md` for architectural context.  
- **AI Governance Framework**: See `templates/strategy-assessment-governance.md` for policies and best practices.

---

# End of Document


---

# Match Merge Rules


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
  - [3.2. Rule Set Overview](#32-rule-set-overview)
  - [3.3. Match Rule Definitions](#33-match-rule-definitions)
  - [3.4. Merge and Survivorship Rules](#34-merge-and-survivorship-rules)
  - [3.5. Rule Testing and Validation Plan](#35-rule-testing-and-validation-plan)
- [4. Example](#4-example)
  - [4.1. Rule Set Overview (Example)](#41-rule-set-overview-example)
  - [4.2. Match Rule Definitions (Example)](#42-match-rule-definitions-example)
  - [4.3. Merge and Survivorship Rules (Example)](#43-merge-and-survivorship-rules-example)
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

**Match Merge Rules** are a specific set of configurable instructions, algorithms, and policies used within a Master Data Management (MDM) system to identify, link, and consolidate duplicate or related records into a single, authoritative "golden record." These rules form the logical core of data deduplication, survivorship, and data harmonization processes. They define the precise criteria for how records are compared (matching) and how data from multiple source records are combined to create the master record (merging).

> The primary purpose of Match Merge Rules is to systematically and automatically enforce data consistency, integrity, and trustworthiness by eliminating redundancy and resolving conflicts. They are the engine that drives the creation of a Single Source of Truth (SSOT) for critical data domains such as Customer, Product, Supplier, or Employee, enabling reliable analytics, improved operational efficiency, and trustworthy reporting.

In the evolving data management landscape, match merge rules must also align with emerging paradigms such as AI governance, data mesh and fabric architectures, and cloud-native deployments. This ensures that master data remains accurate and compliant in increasingly complex, distributed, and automated environments.

### 1.2. Scope

**Global** — Match Merge Rules are typically defined at the enterprise level for each master data domain to ensure consistency and standardization across the organization. While the core logic and standards are established globally, their application may be tailored or parameterized to accommodate specific data sources, business units, or regional regulatory requirements.

These rules are integral to multiple processes including data ingestion, integration, cleansing, and stewardship workflows, and must be adaptable to evolving data governance policies, regulatory compliance (e.g., GDPR, HIPAA, CCPA, EU AI Act), and operational needs.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-11: Data Quality | Match Merge Rules are a primary remediation mechanism for data quality issues, especially duplication and inconsistency. They leverage data quality assessments and profiling outcomes to define matching thresholds and criteria. |
| KA-06: Data Integration & Interoperability | These rules are executed during data integration and synchronization processes, as new or updated data is ingested into the MDM hub from various source systems, including cloud and multi-cloud environments. |
| KA-09: Metadata Management | The logic of match rules, the lineage of merged records, and the audit trail of merges (survivorship) are critical metadata artifacts that must be captured, versioned, and managed for transparency and compliance. |
| KA-01: Data Governance | The governance framework oversees the definition, approval, enforcement, and continuous improvement of these rules, ensuring alignment with business objectives, regulatory requirements, and ethical AI principles. |
| KA-14: AI and Machine Learning Governance | As AI-driven matching and merging become more prevalent, governance of AI models, explainability, and bias mitigation become essential components of match merge rule management. |
| KA-12: Data Architecture | Match merge rules must be designed and implemented in harmony with modern data architectures such as Data Mesh, Data Fabric, and Lakehouse models to support scalability and agility. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager (MDM Mgr) | Ultimately accountable for the effectiveness, accuracy, compliance, and ongoing maintenance of the match merge rules for the master data domain. Approves all new rules and changes, ensuring alignment with enterprise data governance and AI governance policies. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Responsible for analyzing data to identify matching patterns, drafting, testing, refining, and documenting the match merge rules. Conducts impact analysis for rule changes and ensures alignment with data quality standards and AI governance guidelines. |
| **S (Supportive)** | Data Engineer (D-Eng) | Implements and configures the match merge rules within the MDM platform or data integration pipelines. Provides technical support for rule execution, automation, and performance monitoring. Supports integration with cloud-native and multi-cloud environments. |
| **C (Consulted)** | Data Steward, Subject Matter Expert (SME) | Provides domain expertise to validate the business logic of the rules, helps resolve complex matching scenarios and data conflicts, and advises on regulatory and ethical considerations, including AI fairness and bias mitigation. |
| **I (Informed)** | Data Owner (D-Owner) | Kept informed of the rules governing their data domain, the impact of rule changes on data quality, reporting, and compliance. Engaged in periodic reviews and governance meetings. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Match Rule Definition | DQ Analyst | SME, Data Steward | MDM Mgr |
| Merge & Survivorship Logic | DQ Analyst | Data Steward | MDM Mgr |
| Rule Testing & Validation | DQ Analyst | D-Eng, SME | MDM Mgr |
| Rule Performance Monitoring | D-Eng | DQ Analyst | MDM Mgr |

---

## 3. Template

> *The following is the standardized template for defining Match Merge Rules for a master data domain. Replace all placeholders `[...]` with domain-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Match Merge Rules for [Master Data Domain, e.g., Customer] |
| Document ID | MDM-RULES-CUST-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [MDM Manager Name] |
| Approver | [MDM Manager Name] |

### 3.2. Rule Set Overview

> *Provide a high-level summary of the rule set, its purpose, and the business context. Explain the overall strategy for matching (e.g., conservative vs. aggressive), the desired outcome, and how the rules align with enterprise data governance, AI governance, and modern data architecture principles.*

**Input needed**: `02-golden-record-definition.md`, Business requirements, AI governance policies.  
**Who fills this**: DQ Analyst.

[Provide a 2-3 paragraph summary of the match merge strategy for this domain, including considerations for AI-driven matching, cloud deployment, and compliance with data protection regulations.]

### 3.3. Match Rule Definitions

> *This is the core section for defining how duplicate records are identified. Rules are typically executed in a specific sequence, from most precise to most fuzzy. Define each rule with clear logic, columns, matching algorithms, and confidence thresholds. Include notes on AI or machine learning augmentation where applicable.*

**Input needed**: Data profiling results, `KA-11/04-data-quality-rules.md`, AI model outputs.  
**Who fills this**: DQ Analyst, with input from SME and AI governance team.

#### 3.3.1. Rule 1: Exact Match on Unique Identifier

> *This rule looks for perfect duplicates based on a reliable, unique business identifier.*

| Parameter | Value |
| :--- | :--- |
| **Rule Name** | Exact Match on [Primary ID, e.g., National ID] |
| **Match Columns** | `[e.g., National_ID_Number]` |
| **Match Logic** | **Exact**. Both records must have the same non-null value in the match column. |
| **Confidence Score** | 100% (Automatic Match) |
| **Description** | Identifies records that are unequivocally the same entity. This rule is foundational and typically triggers automatic merges without manual review. |

#### 3.3.2. Rule 2: Precise Match on Key Attributes

> *This rule uses a combination of highly stable attributes to identify matches with high confidence.*

| Parameter | Value |
| :--- | :--- |
| **Rule Name** | Precise Match on [e.g., Name and DOB] |
| **Match Columns** | `[e.g., Full_Name]`, `[e.g., Date_of_Birth]` |
| **Match Logic** | - `Full_Name`: **Exact** <br>- `Date_of_Birth`: **Exact** |
| **Confidence Score** | 95% (Automatic Match) |
| **Description** | Identifies individuals with the same full name and date of birth. Suitable for automatic merges with low risk of false positives. |

#### 3.3.3. Rule 3: Fuzzy Match on Name and Address

> *This rule uses fuzzy logic and probabilistic matching to account for variations, typos, abbreviations, and partial data in names and addresses.*

| Parameter | Value |
| :--- | :--- |
| **Rule Name** | Fuzzy Match on [e.g., Name and Address] |
| **Match Columns** | `[e.g., Full_Name]`, `[e.g., Street_Address]`, `[e.g., Postal_Code]` |
| **Match Logic** | - `Full_Name`: **Fuzzy (e.g., Jaro-Winkler, Threshold > 0.9)** <br>- `Street_Address`: **Fuzzy (Address-specific algorithm)** <br>- `Postal_Code`: **Exact** |
| **Confidence Score** | 80% (Potential Match - requires manual review) |
| **Description** | Identifies potential duplicates with slight variations in name or address. These matches are flagged for Data Steward review to minimize false positives. |

_[Add additional rules as necessary, including those leveraging AI/ML models, phonetic algorithms, or external reference data (e.g., phone, email, social media handles). Document any AI model versioning and explainability considerations.]_

### 3.4. Merge and Survivorship Rules

> *Once a match is confirmed, these rules define how the data from the source records is merged to create the golden record. This is also known as survivorship logic. Include rules that address conflict resolution, source system trust levels, temporal considerations, and data privacy compliance.*

**Input needed**: `02-golden-record-definition.md`, Data Steward input, data privacy policies.  
**Who fills this**: DQ Analyst.

| Golden Record Attribute | Survivorship Rule | Rationale |
| :--- | :--- | :--- |
| `[e.g., Customer_ID]` | **Create New** | A new, unique master ID is generated for the golden record to ensure enterprise-wide uniqueness. |
| `[e.g., Full_Name]` | **Most Frequent** | The most common spelling of the name across source records is used to maximize consistency. |
| `[e.g., Primary_Address]` | **Most Recent** | The address from the source record with the latest timestamp is chosen to reflect current information. |
| `[e.g., Email_Address]` | **Source Priority** | The email from a specific trusted source system (e.g., CRM) is always preferred to ensure reliability. |
| `[e.g., Phone_Number]` | **Concatenate (if multiple unique)** | All unique phone numbers are retained in a collection field to preserve contact options. |
| `[e.g., Date_of_Birth]` | **Oldest Value** | The earliest non-null date of birth is considered the most reliable, assuming later values are less accurate. |
| `[e.g., Consent Status]` | **Most Restrictive** | To comply with privacy regulations, the most restrictive consent status across sources is retained. |

_[List all critical attributes of the golden record and their corresponding survivorship rule, including any AI-driven conflict resolution logic or data product considerations.]_

### 3.5. Rule Testing and Validation Plan

> *Describe the process for testing the rules before deploying them to production. This should include the dataset used, testing methodology, success criteria, and ongoing monitoring. Include considerations for AI model validation, bias assessment, and compliance testing.*

**Input needed**: Test data scenarios, QA procedures, AI governance guidelines.  
**Who fills this**: DQ Analyst.

- **Test Dataset**: [e.g., A curated dataset of 10,000 records, including known duplicates, non-duplicates, and edge cases, representative of production data diversity.]
- **Methodology**: 
  1. Execute rules in a sandbox or staging environment.
  2. Compare automated match results against a manually verified "ground truth" set.
  3. Analyze false positives and false negatives.
  4. Perform bias and fairness assessment for AI-driven matching components.
  5. Validate compliance with data privacy and regulatory requirements.
- **Success Criteria**: 
  - Achieve >98% precision (minimize false positives).
  - Achieve >90% recall (minimize false negatives).
  - No significant bias detected in AI models.
  - Compliance with GDPR, HIPAA, CCPA, and EU AI Act requirements.
- **Ongoing Monitoring**: Implement dashboards and alerts to track rule performance, error rates, and data quality trends post-deployment.

---


### 3.6. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-10_match-merge-rules.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

## 4. Example

> *This section provides a realistic, filled-in example for the **Customer** master data domain at **GlobalRetail Inc.**.*

### 4.1. Rule Set Overview (Example)

For the GlobalRetail Customer domain, the match strategy is moderately aggressive to balance consolidation with accuracy. The primary goal is to create a comprehensive 360-degree customer view, reduce marketing waste, and improve customer service. The rules automatically merge high-confidence matches while flagging ambiguous cases for manual review by Data Stewards to prevent incorrect merges of distinct individuals.

The strategy incorporates AI-assisted fuzzy matching algorithms and leverages source system trust scores. It also aligns with GlobalRetail’s AI governance policies to ensure explainability and fairness. The MDM platform is deployed in a multi-cloud environment, supporting scalable, real-time matching and merging.

### 4.2. Match Rule Definitions (Example)

#### 4.2.1. Rule 1: Exact Match on Loyalty Card Number

| Parameter | Value |
| :--- | :--- |
| **Rule Name** | Exact Match on Loyalty Card Number |
| **Match Columns** | `Loyalty_Card_ID` |
| **Match Logic** | **Exact**. Both records must have the same non-null Loyalty Card ID. |
| **Confidence Score** | 100% (Automatic Match) |
| **Description** | Identifies unequivocal duplicates based on a unique loyalty card number. |

#### 4.2.2. Rule 2: Precise Match on Full Name and Email

| Parameter | Value |
| :--- | :--- |
| **Rule Name** | Precise Match on Full Name and Email |
| **Match Columns** | `FullName`, `EmailAddress` |
| **Match Logic** | - `FullName`: **Exact (case-insensitive)** <br>- `EmailAddress`: **Exact (case-insensitive)** |
| **Confidence Score** | 98% (Automatic Match) |
| **Description** | Matches customers with identical full names and emails, accounting for case variations. |

#### 4.2.3. Rule 3: Fuzzy Match on Name and Phone Number

| Parameter | Value |
| :--- | :--- |
| **Rule Name** | Fuzzy Match on Name and Phone Number |
| **Match Columns** | `FullName`, `PhoneNumber` |
| **Match Logic** | - `FullName`: **Fuzzy (Metaphone 3, Threshold > 0.95)** <br>- `PhoneNumber`: **Exact (after normalizing to E.164 format)** |
| **Confidence Score** | 85% (Potential Match - requires manual review) |
| **Description** | Identifies potential duplicates with phonetic similarity in names and exact phone numbers. |

### 4.3. Merge and Survivorship Rules (Example)

| Golden Record Attribute | Survivorship Rule | Rationale |
| :--- | :--- | :--- |
| `MasterCustomerID` | **Create New** | A new UUID is generated for the master record to ensure uniqueness. |
| `FullName` | **Most Complete** | The name with the most components (e.g., including middle initial) is chosen for completeness. |
| `PrimaryAddress` | **Source Priority (Source = 'Billing') then Most Recent** | The Billing system address is preferred due to higher trust; otherwise, the most recent address is used. |
| `EmailAddress` | **Most Recently Verified** | The email with the latest successful validation timestamp is selected to ensure deliverability. |
| `LoyaltyTier` | **Highest Value** | The highest loyalty tier (e.g., 'Gold' beats 'Silver') is retained to maximize customer value. |
| `ConsentStatus` | **Most Restrictive** | To comply with privacy laws, the most restrictive consent status across sources is retained. |

---


### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Golden Record Definition | Deliverable | [02-golden-record-definition.md](templates/templates-KA-10-reference-master-data.md) |
| Data Quality Rules | Deliverable | **04-data-quality-rules.md** |
| Data Governance Roles | Deliverable | [05-roles-responsibilities.md](templates/templates-KA-01-data-governance.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [x] All match rules have a clearly defined confidence score and matching logic.
- [x] At least one "exact" match rule is defined for high-precision matching.
- [x] At least one "fuzzy" match rule is defined to capture variations and potential duplicates.
- [x] All golden record attributes have defined survivorship rules that resolve conflicts deterministically.
- [x] Survivorship logic incorporates source system trust, temporal factors, and compliance considerations.
- [x] The rule testing and validation plan includes metrics for precision, recall, bias assessment, and regulatory compliance.
- [x] RASCI assignments clearly define accountability and responsibilities for rule maintenance and governance.
- [x] Rules and processes align with enterprise AI governance policies and modern data architecture principles.
- [x] Documentation includes versioning, audit trail, and metadata management for transparency.

### 5.2. Review Checklist

| Review Area | Question | Reviewer |
| :--- | :--- | :--- |
| **Business Logic** | Do the match rules accurately reflect how the business identifies unique entities and handle edge cases? | SME, Data Steward |
| **Technical Feasibility** | Can the defined rules be implemented efficiently with the current MDM toolset and data architecture? | D-Eng |
| **Risk of False Positives** | Is there a significant risk of incorrectly merging two distinct entities? How is this risk mitigated? | DQ Analyst |
| **Risk of False Negatives** | What is the estimated rate of missed duplicates? Is this acceptable given business needs? | DQ Analyst, MDM Mgr |
| **AI Governance** | Are AI/ML components explainable, fair, and compliant with governance policies? | AI Ethics Officer, Data Governance |
| **Performance Impact** | Will the execution of these rules meet the required performance SLAs for data integration and real-time processing? | D-Eng |
| **Regulatory Compliance** | Do the rules and survivorship logic comply with GDPR, HIPAA, CCPA, EU AI Act, and other relevant regulations? | Compliance Officer |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| # | Output Name | Relative Path |
| :--- | :--- | :--- |
| 1 | Golden Record Definition | `templates/templates-KA-10-reference-master-data.md` |
| 2 | Data Quality Rules | `templates/templates-KA-11-data-quality.md` |
| 3 | Data Governance Roles and Responsibilities | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers (Outputs)

| # | Output Name | Relative Path |
| :--- | :--- | :--- |
| 1 | Data Integration Rules | `templates/templates-KA-10-reference-master-data.md` |
| 2 | Data Survivorship Rules | `templates/templates-KA-10-reference-master-data.md` |
| 3 | Data Stewardship Playbook | `templates/templates-KA-01-data-governance.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| **MDM Platforms** | Informatica MDM, TIBCO EBX, Semarchy, Profisee, IBM InfoSphere MDM | OpenMDM, Pimcore, Talend MDM |
| **Data Quality Tools** | Talend Data Quality, Ataccama, Trillium, Informatica Data Quality | OpenRefine, Apache Griffin, Deequ |
| **Fuzzy Matching Libraries** | Proprietary libraries embedded in MDM tools | Python: `fuzzywuzzy`, `recordlinkage`, `dedupe`; Java: `Apache Commons Text`, `Simmetrics` |
| **AI/ML Platforms for Matching** | DataRobot, H2O.ai, AWS SageMaker, Azure ML | TensorFlow, PyTorch, scikit-learn |

### 7.2. Automation Opportunities

- **Automated Rule Tuning**: Machine learning models can be trained on manually reviewed match-sets to suggest optimal thresholds and new rule combinations, adapting dynamically to changing data patterns and reducing manual effort.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Rule changes and AI model updates can be managed in version control systems (e.g., Git) and automatically deployed through CI/CD pipelines that include automated testing and validation, ensuring rapid and reliable updates.
- **Automated Performance Monitoring**: Dashboards can be configured to automatically track rule execution times, match rates, false positive/negative rates, and volumes of records sent for manual review, alerting administrators to performance degradation or data quality shifts.
- **Agentic Data Stewardship**: Emerging AI agents can assist Data Stewards by proactively identifying anomalies, suggesting rule improvements, and automating routine stewardship tasks while maintaining human oversight.
- **Cloud-Native Integration**: Leveraging cloud-native services and serverless architectures to scale match merge processing elastically, supporting real-time or near-real-time master data updates.
- **Data Contracts and Data Products**: Embedding match merge rules within data contracts and data product definitions to ensure consistent enforcement across distributed data domains in a data mesh environment.

---

## 8. References

| Ref | Description |
| :--- | :--- |
| [1] | DAMA-DMBOK (Data Management Body of Knowledge), 2nd Edition, Chapter 10: Reference and Master Data. |
| [2] | DAMA-DMBOK 3.0 (In Development, Launching June 2025) — Anticipated updates on AI governance, data mesh integration, and cloud-native MDM practices. |
| [3] | Internal Reference: `templates/templates-KA-01-data-governance.md` |
| [4] | Internal Reference: `templates/templates-KA-11-data-quality.md` |
| [5] | EU AI Act Compliance Guidelines (External) |
| [6] | Data Product Outputs | `references/reference-materials.md` |

---

# Anti-Patterns to Avoid

> *To ensure effective match merge rule implementation, avoid the following common pitfalls:*

- **Overly Aggressive Matching**: Defining rules that are too broad or fuzzy can lead to high false positive rates, merging distinct entities incorrectly.
- **Insufficient Testing**: Deploying rules without rigorous testing and validation can cause data quality degradation and operational issues.
- **Ignoring AI Governance**: Using AI/ML models for matching without explainability, bias assessment, or compliance considerations risks ethical and legal violations.
- **Lack of Version Control**: Not managing rule versions and audit trails impedes traceability and rollback capabilities.
- **Neglecting Source System Trust**: Treating all data sources equally without weighting trust or data quality can propagate errors into the golden record.
- **Static Rules in Dynamic Environments**: Failing to update rules to reflect changing data patterns, business needs, or regulatory requirements leads to stale and ineffective matching.
- **Poor Stakeholder Engagement**: Excluding Data Stewards, SMEs, and governance bodies from rule definition and review reduces rule accuracy and acceptance.
- **Ignoring Modern Architectures**: Implementing match merge rules without considering data mesh, fabric, or cloud-native architectures limits scalability and agility.

---

# Forward-Looking Notes on DAMA-DMBOK 3.0

> The upcoming DAMA-DMBOK 3.0 release (June 2025) emphasizes the integration of AI governance, data mesh and fabric architectures, and cloud-native MDM solutions. Match merge rules will increasingly incorporate AI/ML models with embedded governance controls, support decentralized data stewardship via agentic AI, and align with data contracts and product thinking to enable scalable, trustworthy master data management in complex enterprise environments.

---

# End of Document


---

# Data Integration Rules


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Rule Identification](#31-rule-identification)
  - [3.2. Rule Overview](#32-rule-overview)
  - [3.3. Source and Target Systems](#33-source-and-target-systems)
  - [3.4. Transformation and Cleansing Logic](#34-transformation-and-cleansing-logic)
  - [3.5. Data Quality Checks](#35-data-quality-checks)
  - [3.6. Error Handling and Logging](#36-error-handling-and-logging)
  - [3.7. Spreadsheet Template](#37-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Rule Identification](#41-rule-identification)
  - [4.2. Rule Overview](#42-rule-overview)
  - [4.3. Source and Target Systems](#43-source-and-target-systems)
  - [4.4. Transformation and Cleansing Logic](#44-transformation-and-cleansing-logic)
  - [4.5. Data Quality Checks](#45-data-quality-checks)
  - [4.6. Related Concepts and Guides](#46-related-concepts-and-guides)
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

**Data Integration Rules** are a comprehensive set of documented, actionable instructions that govern the movement, transformation, validation, and consolidation of data between disparate systems and applications. Within the Master Data Management (MDM) framework, these rules are foundational to establishing and maintaining the "golden record" — a single, authoritative, and trusted view of master data entities such as Customer, Product, or Supplier.

These rules operationalize the data integration strategy by specifying the procedural logic for ETL (Extract, Transform, Load), ELT (Extract, Load, Transform), and increasingly, streaming and event-driven data pipelines. They ensure that data from heterogeneous source systems is cleansed, standardized, enriched, and harmonized before integration into the master data hub or data product.

In modern data management environments, Data Integration Rules also support emerging paradigms such as Data Mesh and Data Fabric by enabling decentralized yet consistent data transformations and enforcing data contracts between domains. They are critical for compliance with regulatory frameworks including GDPR, HIPAA, CCPA, and the EU AI Act, particularly when integrating data used in AI/ML models.

> The purpose of Data Integration Rules is to bridge the conceptual data integration strategy and the technical implementation, providing developers, data engineers, and data product teams with precise, unambiguous specifications to build reliable, scalable, and auditable data pipelines.

### 1.2. Scope

**Global and Domain-Specific** — While Data Integration Rules are often defined at a global level to ensure consistency across the enterprise for a given master data domain (e.g., customer contact information), they can also be tailored to specific integration jobs or data products to accommodate unique source system characteristics or business requirements. The core logic remains standardized to maintain data integrity and interoperability.

With the rise of cloud-native architectures and multi-cloud environments, these rules increasingly encompass integration across hybrid platforms, including on-premises systems, cloud data lakes, lakehouses, and streaming platforms. They must therefore be flexible enough to adapt to various execution engines and orchestration frameworks.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-02: Data Architecture | Provides the foundational integration patterns, data flow diagrams, and architectural context that guide the design and application of Data Integration Rules. |
| KA-03: Data Modeling and Design | Defines the logical and physical data models that the integration rules populate, ensuring schema alignment and semantic consistency. |
| KA-06: Data Integration and Interoperability | The primary knowledge area for these rules, covering source-to-target mappings, transformation logic, and interoperability standards. |
| KA-08: Data Governance | Ensures that integration rules comply with governance policies, data stewardship responsibilities, and regulatory requirements, including AI governance considerations. |
| KA-10: Reference and Master Data | Focuses on the management of master data domains, where integration rules are essential to creating and maintaining authoritative data. |
| KA-11: Data Quality | Embeds data quality rules within integration logic to validate, cleanse, and monitor data accuracy, completeness, and consistency. |
| KA-12: Metadata Management | Captures metadata about integration rules, lineage, and transformation logic to support transparency, auditability, and impact analysis. |
| KA-14: Data Security | Ensures that integration processes enforce data privacy, masking, and security controls during data movement and transformation. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager (MDM Mgr) | Ultimately accountable for the quality, compliance, and effectiveness of the data integration rules within the master data program. Ensures alignment with enterprise data strategy and governance frameworks, including AI governance where applicable. |
| **R (Responsible)** | Data Integration Specialist (DI Spec) | Responsible for analyzing business and technical requirements, designing, documenting, and maintaining the data integration rules. Ensures rules are implementable and scalable. |
| **S (Supportive)** | ETL Developer (ETL Dev) | Supports the process by implementing the defined rules in ETL/ELT jobs or data pipelines, providing technical feedback on feasibility and performance. |
| **C (Consulted)** | Data Steward (D-Steward) | Provides business context, validates transformation logic, defines data quality requirements, and ensures compliance with data governance policies. |
| **I (Informed)** | Data Integration Manager (DI Mgr) | Kept informed of the status, changes, and performance of the data integration rules to coordinate integration across domains and platforms. |
| **C (Consulted)** | AI Ethics Officer / CAIO (where applicable) | Consulted to ensure integration rules comply with AI governance policies, ethical data usage, and regulatory requirements related to AI/ML data pipelines. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Rule Definition & Logic | DI Spec | D-Steward, ETL Dev, AI Ethics Officer | MDM Mgr |
| Source/Target Specification | DI Spec | System Owners, Data Architect (D-Arch) | MDM Mgr |
| Transformation & Cleansing | DI Spec | D-Steward, Data Quality Analyst (DQ Analyst) | MDM Mgr |
| Error Handling & Logging | DI Spec | ETL Dev, DataOps Engineer | MDM Mgr |

---

## 3. Template

> *The following template provides a standardized format for documenting a single Data Integration Rule or a set of related rules for a specific data flow. It is designed to support modern data management environments, including cloud-native pipelines, data mesh domains, and AI governance considerations.*

### 3.1. Rule Identification

| Field | Value |
| :--- | :--- |
| Rule ID | [e.g., DIR-CUST-001] |
| Rule Name | [e.g., Customer Address Standardization] |
| Master Data Domain | [e.g., Customer, Product, Supplier] |
| Version | [e.g., 1.0] |
| Status | [e.g., Draft, Active, Inactive] |
| Last Updated | [YYYY-MM-DD] |
| Data Product Owner | [Name/Role responsible for the data product] |
| AI Governance Impact | [Yes/No; if Yes, specify AI-related compliance or ethical considerations] |

### 3.2. Rule Overview

> *Provide a concise, high-level description of the rule's purpose, the integration scenario it applies to, and any relevant business or technical context.*

[Insert overview here]

### 3.3. Source and Target Systems

> *Identify the source system(s) from which data is extracted and the target system(s) where data is loaded. Include specific tables, APIs, or data streams, and detail any filtering or extraction logic.*

**Source(s):**

| System Name | Table / API Endpoint | Column(s) | Filter/Extraction Logic |
| :--- | :--- | :--- | :--- |
| [e.g., Salesforce CRM] | `Account` | `BillingStreet`, `BillingCity`, `BillingState`, `BillingPostalCode`, `BillingCountry` | `LastModifiedDate > @LastRunDate` |
| [e.g., Magento E-commerce] | `sales_order_address` | `street`, `city`, `region`, `postcode`, `country_id` | `updated_at > @LastRunDate` |

**Target:**

| System Name | Table | Column(s) |
| :--- | :--- | :--- |
| [e.g., MDM Hub] | `C_PTY_ADDRESS` | `ADDR_LINE_1`, `CITY`, `STATE_PROV`, `POSTAL_CODE`, `COUNTRY_CD` |

### 3.4. Transformation and Cleansing Logic

> *Detail the step-by-step transformation, cleansing, and mapping logic. Include reference to any external services, lookup tables, or AI/ML models used for enrichment or validation.*

| Step | Transformation Logic | Target Column | Notes |
| :--- | :--- | :--- | :--- |
| 1 | **Address Parsing**: Use a reference data service (e.g., Loqate, Melissa) or AI-powered address validation API to parse source address fields into standardized components. | `ADDR_LINE_1`, `CITY`, `STATE_PROV`, `POSTAL_CODE` | Handles variations like 'Street' vs 'St.' and validates address existence. |
| 2 | **Country Code Standardization**: Map source country name or code to ISO 3166-1 alpha-2 standard using reference tables or APIs. | `COUNTRY_CD` | Use `REF_COUNTRY` reference table or external service for up-to-date mappings. |
| 3 | **State/Province Standardization**: Map source state/province to standard abbreviations using reference data. | `STATE_PROV` | Use `REF_STATE_PROV` reference table. |
| 4 | **Concatenation**: Concatenate multi-line street address fields where applicable. | `ADDR_LINE_1` | Use `TRIM(CONCAT(source.street_line1, ' ', source.street_line2))`. |
| 5 | **Case Conversion**: Convert all address components to uppercase for consistency. | All Target Columns | Use `UPPER(...)`. |
| 6 | **AI-Based Enrichment (Optional)**: Apply AI models to enrich address data with geolocation or demographic attributes. | Additional columns as applicable | Ensure AI governance policies are followed. |

### 3.5. Data Quality Checks

> *Define specific data quality checks to be performed during integration, including thresholds, validation rules, and failure actions. Incorporate AI governance and compliance checks where relevant.*

| DQ Dimension | Check Description | Failure Action |
| :--- | :--- | :--- |
| Completeness | `POSTAL_CODE` must not be null or empty. | Reject record and log for manual review. |
| Validity | `COUNTRY_CD` must exist in the `REF_COUNTRY` table and conform to ISO standards. | Reject record and log for review. |
| Accuracy | Address must be verifiable by the address parsing service or AI model confidence score above threshold. | Flag record with `ACCURACY_FLAG = 'Unverified'`; allow to proceed with caution. |
| Consistency | State/Province code must match country code standards. | Reject or flag for review depending on severity. |
| Compliance | Data must comply with privacy masking or anonymization rules if applicable. | Mask or reject data as per policy. |

### 3.6. Error Handling and Logging

> *Describe procedures for handling errors during rule execution, including retry logic, error categorization, and logging requirements to support monitoring, auditing, and troubleshooting.*

- **Connection Errors**: Retry connection up to 3 times with exponential backoff (e.g., 5, 10, 20 minutes). If still failing, abort job and send alert to DataOps and Data Steward teams.
- **Transformation Errors**: Records failing transformation or data quality checks with a 'Reject' action are written to an error staging table (e.g., `ERR_CUST_ADDRESS`) with source data, Rule ID, error code, and detailed message.
- **Partial Failures**: For non-critical errors (e.g., low confidence in AI enrichment), flag records but allow processing to continue.
- **Logging**: Capture and log metrics including total records processed, successful integrations, rejected records, and processing time. Include lineage metadata for traceability.
- **Audit Trail**: Maintain versioned documentation of rule changes and approvals to support compliance audits, especially for regulated industries and AI governance.

### 3.7. Spreadsheet Template

> For operational efficiency and collaboration, a spreadsheet template is provided to manage multiple Data Integration Rules systematically.

> *Note: The spreadsheet template KA-10_data-integration-rules.xlsx can be generated by Claude on request.*

> This spreadsheet supports bulk data entry, filtering, sorting, and version control, complementing this Markdown template. It is designed to integrate with metadata management tools and data catalogs for enhanced governance.

---

## 4. Example

### 4.1. Rule Identification

| Field | Value |
| :--- | :--- |
| Rule ID | DIR-CUST-001 |
| Rule Name | Customer Address Standardization |
| Master Data Domain | Customer |
| Version | 1.0 |
| Status | Active |
| Last Updated | 2026-02-08 |
| Data Product Owner | Jane Doe, Customer Data Product Manager |
| AI Governance Impact | Yes – Address verification uses AI-powered Melissa Data API |

### 4.2. Rule Overview

This rule standardizes customer address information sourced from GlobalRetail Inc.'s Salesforce CRM and Magento e-commerce platform, integrating it into the central MDM Hub. The objective is to create a single, clean, validated, and enriched address record for each customer party, supporting downstream analytics, personalized marketing, and compliance reporting.

The rule incorporates AI-based address verification and enrichment while adhering to the organization's AI governance framework, ensuring transparency and ethical use of AI models.

### 4.3. Source and Target Systems

**Source(s):**

| System Name | Table / API Endpoint | Column(s) | Filter/Extraction Logic |
| :--- | :--- | :--- | :--- |
| Salesforce CRM | `Account` | `BillingStreet`, `BillingCity`, `BillingState`, `BillingPostalCode`, `BillingCountry` | `LastModifiedDate > @LastRunDate` |
| Magento E-commerce | `sales_order_address` | `street`, `city`, `region`, `postcode`, `country_id` | `updated_at > @LastRunDate` |

**Target:**

| System Name | Table | Column(s) |
| :--- | :--- | :--- |
| MDM Hub | `C_PTY_ADDRESS` | `ADDR_LINE_1`, `CITY`, `STATE_PROV`, `POSTAL_CODE`, `COUNTRY_CD` |

### 4.4. Transformation and Cleansing Logic

| Step | Transformation Logic | Target Column | Notes |
| :--- | :--- | :--- | :--- |
| 1 | **Address Parsing**: Use Melissa Data's Global Address Verification API to parse and validate the source address components. | `ADDR_LINE_1`, `CITY`, `STATE_PROV`, `POSTAL_CODE` | API standardizes street suffixes, city names, postal formats, and returns validation status. |
| 2 | **Country Code Standardization**: Map `BillingCountry` (e.g., "United States") or `country_id` (e.g., "US") to ISO 3166-1 alpha-2 codes using `country_mapping.csv`. | `COUNTRY_CD` | Example mappings: 'United States' -> 'US', 'Canada' -> 'CA'. |
| 3 | **State/Province Standardization**: Map `BillingState` (e.g., 'California') or `region` (e.g., 'CA') to standard 2-letter abbreviations using `state_mapping.csv`. | `STATE_PROV` | Example mappings: 'California' -> 'CA', 'New York' -> 'NY'. |
| 4 | **Concatenation**: Combine multiple street address lines if present. | `ADDR_LINE_1` | `TRIM(CONCAT(source.street_line1, ' ', source.street_line2))` |
| 5 | **Case Conversion**: Convert all address components to uppercase for consistency. | All Target Columns | `UPPER(...)` |
| 6 | **AI-Based Enrichment**: Append geolocation coordinates using AI geocoding service. | `LATITUDE`, `LONGITUDE` | Enrichment supports location-based analytics and personalization. |

### 4.5. Data Quality Checks

| DQ Dimension | Check Description | Failure Action |
| :--- | :--- | :--- |
| Completeness | `POSTAL_CODE` must not be null after transformation. | Reject record and write to `ERR_CUST_ADDRESS` for manual review by Data Steward. |
| Validity | `COUNTRY_CD` must be a valid ISO 3166-1 alpha-2 code present in reference data. | Reject record and write to `ERR_CUST_ADDRESS`. |
| Accuracy | Melissa API must return an `AV` (Address Valid) status code. | If status is `AE` (Address Error), reject record. If `AS` (Address Suggestion), proceed but flag for review. |
| Consistency | State/Province code must align with country code standards. | Flag for review; reject if critical mismatch. |
| Compliance | Address data must comply with GDPR masking rules for EU customers. | Mask PII fields or reject record as per policy. |

### 4.6. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Source-to-Target Mapping | Deliverable | **templates/templates-KA-06-data-integration-interoperability.md** |
| Match/Merge Rules | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| Survivorship Rules | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| Data Governance and AI Ethics | Knowledge Area | **templates/templates-KA-08-data-warehousing-bi.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] Rule has a unique, sequential Rule ID following organizational standards.
- [x] All source and target systems, tables, and columns are explicitly identified with extraction/filter logic.
- [x] Transformation and cleansing logic is fully defined for every target column, including AI/ML enrichment steps if applicable.
- [x] All lookups, reference data tables, and external services are specified with versioning and update frequency.
- [x] Data quality checks cover completeness, validity, accuracy, consistency, and compliance dimensions.
- [x] Error handling procedures, retry logic, and logging requirements are clearly defined and aligned with operational standards.
- [x] The rule has been reviewed and approved by the MDM Manager, Data Steward, and AI Ethics Officer (if AI governance impact exists).
- [x] Metadata capturing lineage, version history, and approvals is maintained for auditability.
- [x] The rule supports cloud-native execution environments and multi-cloud interoperability where applicable.

### 5.2. Review Checklist

| Category | Question | Reviewer Sign-off |
| :--- | :--- | :--- |
| **Clarity** | Is the rule's logic unambiguous, well-documented, and easy for ETL developers or data engineers to implement? | [Name/Date] |
| **Correctness** | Does the transformation logic accurately implement business and technical requirements? | [Name/Date] |
| **Robustness** | Does the error handling cover likely failure scenarios (e.g., nulls, invalid data, system unavailability)? | [Name/Date] |
| **Efficiency** | Is the logic optimized for performance and scalability? Are there any unnecessary steps or inefficient lookups? | [Name/Date] |
| **Compliance** | Does the rule comply with relevant data governance, privacy, and AI ethics policies? | [Name/Date] |
| **Maintainability** | Is the rule modular and maintainable for future updates and extensions? | [Name/Date] |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-10-reference-master-data.md` | Match/Merge rules determine which source records should be combined, providing the input data for integration. |
| `templates/templates-KA-10-reference-master-data.md` | Survivorship rules determine which source value wins in a conflict, which this rule then integrates into the target. |
| `templates/templates-KA-06-data-integration-interoperability.md` | Source-to-target mapping specifications provide field-level mappings that Data Integration Rules implement. |
| `templates/templates-KA-08-data-warehousing-bi.md` | AI governance policies inform the ethical and regulatory considerations embedded in integration rules involving AI/ML data. |

### 6.2. Consumers (This Output is Input for)

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-06-data-integration-interoperability.md` | This document provides the detailed, field-level logic required to populate the high-level Source-to-Target map. |
| `templates/templates-KA-11-data-quality.md` | Data quality monitoring uses the checks defined in integration rules to track data health and trigger remediation. |
| `templates/templates-KA-10-reference-master-data.md` | Data stewards use integration rules to understand data flows and enforce stewardship responsibilities. |
| `templates/templates-KA-14-data-management-maturity.md` | Privacy and compliance teams use integration rules to verify enforcement of masking and data protection controls. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **ETL/ELT Platforms** | Informatica PowerCenter, Talend, Microsoft SSIS, IBM DataStage, AWS Glue, Azure Data Factory | Apache Airflow, Apache NiFi, Pentaho Data Integration, dbt (data build tool) |
| **Data Quality & Cleansing** | Trillium, Melissa Data, Loqate, Collibra Data Quality | OpenRefine, Great Expectations, Deequ |
| **Orchestration & Workflow** | Control-M, ActiveBatch, Azure Data Factory Pipelines | Apache Airflow, Dagster, Prefect |
| **Metadata Management** | Collibra, Alation, Informatica EDC | Amundsen, DataHub |
| **AI/ML Integration** | DataRobot, H2O.ai, Azure ML | MLflow, Kubeflow |
| **Cloud-Native Platforms** | Snowflake, Databricks Lakehouse, Google BigQuery, AWS Redshift | Apache Spark, Presto, Apache Flink |

### 7.2. Automation Opportunities

- Fully automate ETL/ELT jobs implementing these rules with scheduling and monitoring via orchestration tools.
- Configure automated alerts to notify DataOps and Data Stewardship teams when error thresholds are exceeded (e.g., >5% rejected records).
- Automate calculation and publication of data quality metrics (e.g., % records integrated successfully, % addresses verified) to dashboards or Data Quality Scorecards.
- Integrate AI governance checkpoints to automatically validate compliance with ethical and regulatory policies during AI/ML data processing.
- Leverage Infrastructure as Code (IaC) and CI/CD pipelines to version, test, and deploy integration rules and associated data pipelines.
- Use data contracts and schema registries to enforce interface agreements between data producers and consumers in a Data Mesh environment.

---

## 8. References

- DAMA-DMBOK (Data Management Body of Knowledge), 2nd Edition, Chapter 10: Reference and Master Data.
- DAMA-DMBOK 3.0 (forthcoming, June 2025) — evolving guidance on data integration in cloud-native, AI-governed environments.
- `references/reference-materials.md`
- `templates/templates-KA-06-data-integration-interoperability.md`
- `templates/templates-KA-08-data-warehousing-bi.md`
- `templates/templates-KA-10-reference-master-data.md`
- `templates/templates-KA-10-reference-master-data.md`
- ISO 3166-1 alpha-2 country codes standard
- EU AI Act compliance guidelines and GDPR/HIPAA/CCPA regulations relevant to data integration and AI data usage

---

*End of Document*


---

# Master Data Model


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
  - [3.2. Model Overview](#32-model-overview)
  - [3.3. Entity Definitions](#33-entity-definitions)
  - [3.4. Attribute Definitions](#34-attribute-definitions)
  - [3.5. Relationship and Hierarchy Definitions](#35-relationship-and-hierarchy-definitions)
  - [3.6. Business and Data Quality Rules](#36-business-and-data-quality-rules)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Model Overview](#42-model-overview)
  - [4.3. Entity Definitions](#43-entity-definitions)
  - [4.4. Attribute Definitions](#44-attribute-definitions)
  - [4.5. Relationship and Hierarchy Definitions](#45-relationship-and-hierarchy-definitions)
  - [4.6. Business and Data Quality Rules](#46-business-and-data-quality-rules)
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

> A **Master Data Model** is a specialized data model that defines the single, authoritative, and consistent representation of an organization's core business entities, known as master data. These entities include, but are not limited to, Customer, Product, Supplier, Employee, and Location. Unlike transactional or analytical models, the Master Data Model focuses on the attributes, relationships, and hierarchies that create a "golden record" or a single source of truth for each master data entity across the enterprise.

The primary purpose of the Master Data Model is to enforce consistency, reduce data redundancy, and improve data quality for the organization's most critical and shared data assets. It provides a standardized blueprint for how master data is structured, stored, and managed, ensuring that all applications and business processes are using the same, accurate information. This model is a cornerstone of a successful Master Data Management (MDM) program, enabling better decision-making, improved operational efficiency, and a unified view of the business.

In the evolving data management landscape, the Master Data Model must also support modern paradigms such as data mesh and data fabric architectures, enabling decentralized ownership while maintaining enterprise-wide standards. It should be designed to integrate with cloud-native platforms and support multi-cloud environments to ensure scalability and resilience. Furthermore, with the growing importance of AI governance, the model must incorporate metadata and attributes that facilitate responsible AI use, compliance with regulations such as the EU AI Act, and alignment with ethical data stewardship practices.

Looking forward to DAMA-DMBOK 3.0, the Master Data Model is expected to evolve to incorporate agentic stewardship concepts, data contracts, and data products as first-class citizens, reflecting the shift towards treating master data as a managed product with clear ownership, SLAs, and lifecycle management.

### 1.2. Scope

**Per Product** — A Master Data Model is typically developed for each specific master data domain (e.g., a Customer Master Data Model, a Product Master Data Model). While guided by enterprise-level standards and integrated into the Enterprise Data Architecture, each model is tailored to the unique attributes, relationships, and governance requirements of its respective data product.

The scope includes defining entities, attributes, relationships, hierarchies, and associated business and data quality rules. It also encompasses metadata necessary for AI governance, data lineage, and compliance tracking. The model should be extensible to support evolving business needs, integration with MLOps and DataOps pipelines, and enable automation in data quality monitoring and data product delivery.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-03: Data Modeling and Design | The Master Data Model is a specific application of data modeling principles, leveraging conceptual, logical, and physical modeling techniques to define master data structures. It incorporates modern modeling approaches to support data mesh and fabric architectures. |
| KA-02: Data Architecture | The model must align with the overall Enterprise Data Model and Data Architecture Blueprint to ensure it integrates seamlessly into the broader data landscape, including cloud-native and multi-cloud environments. |
| KA-01: Data Governance | The model is governed by data policies and standards, and its creation and maintenance are managed through the established RASCI roles and stewardship plans. It must also support AI governance and compliance with regulatory frameworks such as GDPR, HIPAA, CCPA, and the EU AI Act. |
| KA-11: Data Quality | The model is a key tool for enforcing data quality, as it defines the business rules and validation criteria that master data must adhere to. It supports integration with DataOps and FinOps practices for continuous quality improvement. |
| KA-12: Data Security and Privacy | The model includes considerations for data security classifications, privacy controls, and masking requirements to protect sensitive master data in compliance with organizational policies and regulations. |
| KA-14: AI and Analytics | The model supports AI governance by including metadata and attributes necessary for explainability, fairness, and traceability of AI models that consume master data. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager (MDM Mgr) | Ultimately answerable for the quality, completeness, and approval of the Master Data Model for a specific domain. Ensures alignment with enterprise data governance and AI governance policies. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Responsible for designing, developing, and maintaining the Master Data Model, including entities, attributes, and relationships. Collaborates with data architects to ensure architectural compliance and supports automation efforts. |
| **S (Supportive)** | Data Architect (D-Arch) | Provides guidance and support to ensure the model aligns with enterprise architecture principles and standards, including cloud-native and multi-cloud considerations. Supports integration with data mesh and fabric strategies. |
| **C (Consulted)** | Data Steward (D-Steward), Subject Matter Expert (SME), AI Ethics Officer | Consulted to provide business requirements, define business rules, validate the accuracy and completeness of the model, and ensure AI governance and ethical considerations are embedded. |
| **I (Informed)** | Data Engineer (D-Eng), MLOps Engineer | Informed of the model's structure to effectively build data pipelines and integrations that consume or populate the master data. Supports operationalization and automation of data quality and AI model data inputs. |

### 2.2. Section-Level RASCI

| Model Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Entity and Attribute Definitions | D-Modeler | D-Steward, SME | MDM Mgr |
| Hierarchies and Relationships | D-Modeler | D-Steward, D-Arch | MDM Mgr |
| Business and Quality Rules | D-Steward, SME | D-Modeler, DQ Analyst | MDM Mgr |
| Source System Mapping | D-Modeler | D-Eng, SME | MDM Mgr |
| AI Governance Metadata | D-Modeler, AI Ethics Officer | D-Steward, D-Arch | MDM Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Master Data Model. Replace all placeholders `[...]` with domain-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | [Domain] Master Data Model |
| Document ID | MDM-MOD-[Domain Code]-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [MDM Manager Name] |
| AI Governance Compliance | [Yes/No] |
| Data Product Owner | [Name] |
| Data Stewardship Model | [Centralized/Decentralized/Agentic] |

### 3.2. Model Overview

> *Provide a brief narrative of the master data domain this model represents. Describe its business importance, the key entities included, and how it supports enterprise data governance, AI governance, and modern data architectures.*

[Insert Model Overview]

Example guidance: Describe how this model supports data mesh principles by enabling domain ownership, how it integrates with data fabric for seamless data access, and how it incorporates AI governance metadata to ensure responsible AI use.

### 3.3. Entity Definitions

> *List and define all core entities within this master data domain. An entity is a person, place, thing, or concept about which data is stored.*

| Entity Name | Definition |
| :--- | :--- |
| [e.g., Customer] | [e.g., An individual or organization that has purchased goods or services.] |
| [e.g., Address] | [e.g., A physical location associated with an entity.] |

### 3.4. Attribute Definitions

> *For each entity, define its attributes. Attributes are the specific pieces of information that describe an entity. Specify data type, length, constraints, and provide a clear business definition. Include metadata for AI governance and data product management where applicable.*

#### 3.4.1. [Entity Name 1]

| Attribute Name | Data Type | Length | Constraints | Business Definition | AI Governance Metadata | Data Product Metadata |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., CustomerID] | INTEGER | | NOT NULL, PK | [Unique identifier for the customer.] | [e.g., Sensitivity Level] | [e.g., Data Owner] |
| [e.g., FirstName] | VARCHAR | 50 | | [The customer's legal first name.] | [e.g., Usage Restrictions] | [e.g., SLA] |
| [e.g., EmailAddress] | VARCHAR | 100 | NOT NULL, UNIQUE | [The customer's primary email address.] | [e.g., Masking Required] | [e.g., Update Frequency] |

### 3.5. Relationship and Hierarchy Definitions

> *Define the relationships between entities and any hierarchies that exist within the domain. Use a diagram and a table to describe the cardinality and nature of each relationship. Include notes on how these relationships support data lineage and AI model explainability.*

#### 3.5.1. Relationship Diagram

[Insert ERD or other relationship diagram here]

#### 3.5.2. Relationship Descriptions

| Parent Entity | Child Entity | Relationship Type | Cardinality | Description | Lineage Impact | AI Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., Customer] | [e.g., Address] | Identifying | One-to-Many | [A customer can have multiple addresses.] | [Tracks source of address data] | [Supports address validation in AI models] |

### 3.6. Business and Data Quality Rules

> *Document the business rules and data quality rules that apply to the entities and attributes in this model. These rules are critical for maintaining the integrity of the master data and ensuring compliance with governance frameworks.*

| Rule ID | Rule Description | Entity/Attribute | Rule Type | Enforcement Mechanism | AI Governance Considerations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., DQ-001] | [e.g., EmailAddress must be in a valid format.] | [e.g., Customer.EmailAddress] | [e.g., Format] | [Automated validation in ETL] | [Ensures reliable AI input] |
| [e.g., BR-001] | [e.g., A customer must be at least 18 years old.] | [e.g., Customer.BirthDate] | [e.g., Validation] | [Manual review and automated checks] | [Compliance with ethical AI use] |

---

## 4. Example

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Product Master Data Model |
| Document ID | MDM-MOD-PROD-001 |
| Version | 1.0 |
| Effective Date | 2026-02-08 |
| Owner | John Doe |
| AI Governance Compliance | Yes |
| Data Product Owner | Jane Smith |
| Data Stewardship Model | Agentic |

### 4.2. Model Overview

This document defines the Master Data Model for the "Product" domain at GlobalRetail Inc. This model provides the single source of truth for all product information across the organization, from procurement to sales. It is critical for e-commerce, supply chain management, financial reporting, and AI-driven product recommendations.

The model supports the organization's data mesh strategy by enabling domain teams to own and manage product master data while adhering to enterprise-wide standards. It integrates with the data fabric platform to provide seamless access across multi-cloud environments. AI governance metadata is embedded to ensure compliance with the EU AI Act and internal ethical guidelines.

### 4.3. Entity Definitions

| Entity Name | Definition |
| :--- | :--- |
| Product | A good or service offered for sale by GlobalRetail Inc. |
| Brand | The commercial name under which a product or group of products is marketed. |
| Category | A classification used to group similar products. |

### 4.4. Attribute Definitions

#### 4.4.1. Product

| Attribute Name | Data Type | Length | Constraints | Business Definition | AI Governance Metadata | Data Product Metadata |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ProductSKU | VARCHAR | 20 | NOT NULL, PK | Unique identifier for the product (Stock Keeping Unit). | Sensitivity: Low | Owner: Product Team |
| ProductName | VARCHAR | 255 | NOT NULL | The official name of the product. | Usage: Public | SLA: Daily Update |
| ProductDescription | TEXT | | | A detailed description of the product for use on the website. | Usage: Public | SLA: Weekly Update |
| UnitPrice | DECIMAL | 10,2 | > 0 | The retail price of a single unit of the product. | Sensitivity: Medium | SLA: Real-time |
| BrandID | INTEGER | | FK to Brand | The identifier for the product's brand. | Sensitivity: Low | Owner: Brand Team |

### 4.5. Relationship and Hierarchy Definitions

#### 4.5.1. Relationship Diagram

(A conceptual diagram would be here showing Product, Brand, and Category relationships)

#### 4.5.2. Relationship Descriptions

| Parent Entity | Child Entity | Relationship Type | Cardinality | Description |
| :--- | :--- | :--- | :--- | :--- |
| Brand | Product | Non-identifying | One-to-Many | A brand can have many products. |
| Category | Product | Non-identifying | One-to-Many | A category can contain many products. |

### 4.6. Business and Data Quality Rules

| Rule ID | Rule Description | Entity/Attribute | Rule Type | Enforcement Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| DQ-001 | UnitPrice must be greater than the CostPrice. | Product.UnitPrice | Validation | Automated ETL checks |
| BR-001 | If a product is in the "Electronics" category, it must have a WarrantyPeriod attribute. | Product | Conditional | Manual review and automated alerts |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Governance Framework | Knowledge Area | **knowledge-areas/KA-01-data-governance.md** |
| Data Modeling and Design | Knowledge Area | **knowledge-areas/KA-03-data-modeling-and-design.md** |
| AI Governance Guide | Guide | **#** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] All entities and attributes are clearly defined, including AI governance and data product metadata.
- [ ] All relationships and hierarchies are accurately modeled and documented.
- [ ] All business and data quality rules are documented with enforcement mechanisms.
- [ ] The model has been reviewed and approved by the Data Steward, AI Ethics Officer, and MDM Manager.
- [ ] The model aligns with the Enterprise Data Model and Data Architecture Blueprint.
- [ ] The model supports compliance with relevant regulations (GDPR, HIPAA, CCPA, EU AI Act).
- [ ] The model supports integration with data mesh, data fabric, and cloud-native architectures.
- [ ] The model supports automation opportunities for data quality and AI governance.

### 5.2. Review Checklist

| Question | Yes/No | Comments |
| :--- | :--- | :--- |
| Is the model in 3rd Normal Form (3NF)? | | |
| Are all attributes atomic and appropriately typed? | | |
| Are all data types and lengths appropriate for the business context? | | |
| Does the model meet all documented business requirements? | | |
| Are AI governance metadata and compliance attributes included? | | |
| Does the model support data product management and lifecycle tracking? | | |
| Is the model aligned with enterprise data governance and architecture standards? | | |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship |
| :--- | :--- |
| [02-golden-record-definition.md](./02-golden-record-definition.md) | Provides the definition of the golden record that this model is designed to produce. |
| [01-enterprise-data-model.md](templates/templates-KA-02-data-architecture.md) | Provides the enterprise context and standards that this model must align with. |
| **03-data-quality-rules.md** | Defines the data quality rules that the master data must satisfy. |
| **04-data-governance-policies.md** | Contains governance policies relevant to master data management and AI governance. |

### 6.2. Consumers

| Output | Relationship |
| :--- | :--- |
| [09-hierarchy-definitions.md](./09-hierarchy-definitions.md) | Consumes the hierarchy structures defined in this model to create detailed hierarchy definitions. |
| **10-data-product-catalog.md** | Uses master data definitions to enrich data product metadata and catalog entries. |
| **11-ai-model-input-specifications.md** | Consumes master data attributes and quality rules to define AI model inputs and governance controls. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| Data Modeling | Erwin, ER/Studio, SAP PowerDesigner | Draw.io, OpenModelSphere, Archi |
| MDM Platforms | Informatica MDM, TIBCO EBX, Semarchy | Pimcore, AtroPIM, ODPi Egeria |
| Data Quality & Governance | Collibra, Alation, Talend Data Quality | Apache Atlas, OpenMetadata |

### 7.2. Automation Opportunities

- **Model Generation:** The physical data model can be automatically generated from the logical data model using data modeling tools, reducing manual effort and errors.
- **Data Dictionary Generation:** The data dictionary for the master data can be automatically generated from the model's metadata, ensuring up-to-date documentation.
- **Data Quality Monitoring:** Data quality rules defined in the model can be used to automate data quality monitoring and reporting, integrating with DataOps pipelines.
- **AI Governance Automation:** Metadata and rules embedded in the model can trigger automated compliance checks, bias detection, and lineage tracking for AI models.
- **Data Product Lifecycle Management:** Integration with data product management tools to automate versioning, SLA tracking, and stakeholder notifications.
- **Cloud-Native Integration:** Use of APIs and metadata services to enable dynamic model consumption in multi-cloud and hybrid environments.

---

## 8. References

- [1] DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017.
- [2] DAMA International. *DAMA-DMBOK 3.0 (Draft)*. Community-driven rebuild, expected launch June 2025.
- [3] [role-definitions.md](references/reference-materials.md)
- [4] [data-product-outputs.md](references/reference-materials.md)
- [5] **ai-governance.md**
- [6] European Commission. *EU AI Act*. 2021.
- [7] Gartner. *Data Mesh and Data Fabric Synergy*. 2023.
- [8] O'Reilly. *Modern Data Architectures: Lakehouse, Mesh, and Fabric*. 2024.


---

# Reference Data Tables


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Table Properties](#31-table-properties)
  - [3.2. Column Definitions](#32-column-definitions)
  - [3.3. Data Content (Initial Set)](#33-data-content-initial-set)
  - [3.4. Governance and Maintenance](#34-governance-and-maintenance)
  - [3.5. Spreadsheet Template](#35-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Table Properties](#41-table-properties)
  - [4.2. Column Definitions](#42-column-definitions)
  - [4.3. Data Content](#43-data-content)
  - [4.4. Governance and Maintenance](#44-governance-and-maintenance)
  - [4.5. Related Concepts and Guides](#45-related-concepts-and-guides)
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

**Reference Data Tables** are curated, authoritative datasets that define a set of permissible values to be used for categorizing or classifying other data within an organization. These tables provide context to data, ensuring consistency and uniformity across different systems, applications, and reports. Unlike transactional data, which changes frequently, reference data is relatively static and serves as a common vocabulary for business operations.

> The primary purpose of Reference Data Tables is to enforce data consistency, improve data quality, and enable seamless data integration and interoperability. They are the bedrock of semantic consistency, ensuring that when a business term like "Country" or "Product Status" is used, it has a single, unambiguous meaning across the enterprise.

In modern data environments, reference data plays a critical role in enabling **data mesh** and **data fabric** architectures by providing standardized vocabularies that facilitate cross-domain interoperability and autonomous data product development. Additionally, with the rise of **cloud-native** platforms and **multi-cloud** strategies, reference data tables must be designed for scalability, accessibility, and real-time synchronization across distributed systems.

From a forward-looking perspective, the upcoming **DAMA-DMBOK 3.0** emphasizes the integration of reference data management with **AI governance** frameworks, recognizing that consistent reference data is foundational for trustworthy AI models and automated decision-making processes. This includes ensuring compliance with emerging regulations such as the **EU AI Act**, which mandates transparency and traceability in AI data inputs.

### 1.2. Scope

**Per Product** — While the standards for creating reference data are global, the tables themselves are typically managed and applied at the individual data product level. This allows for domain-specific sets of reference values (e.g., "Marketing Campaign Types") while still adhering to a centralized governance model.

In decentralized data governance models, such as data mesh, reference data stewardship may be distributed among domain teams, with a central governance body providing oversight, standards, and tooling. This hybrid approach balances agility with enterprise-wide consistency.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The governance program charters the creation and management of reference data, and the Business Glossary often provides the definitions for reference data domains. Governance frameworks increasingly incorporate AI governance and ethical data stewardship roles. |
| KA-03: Data Modeling and Design | Data models consume reference data tables as the source for valid values in specific attributes (e.g., foreign key constraints). Modern modeling includes support for hierarchical and graph-based reference data structures. |
| KA-06: Data Integration and Interoperability | Reference data is essential for mapping and transforming data between systems, ensuring that values from a source system are correctly translated to a target system. Integration patterns now include API-based distribution and event-driven synchronization. |
| KA-08: Data Architecture | Reference data tables are foundational components in data architecture, supporting data mesh and fabric patterns, and enabling scalable, cloud-native deployments. |
| KA-10: Reference and Master Data Management | This knowledge area directly addresses the lifecycle, governance, and operationalization of reference data tables as part of master data management strategies. |
| KA-11: Data Quality | The use of standardized reference data is a primary mechanism for preventing data quality issues related to consistency, accuracy, and validity. Automated data quality frameworks and MLOps pipelines increasingly leverage reference data for validation. |
| KA-13: Data Security and Privacy | Reference data management must align with security policies and privacy regulations, ensuring controlled access and compliance with GDPR, HIPAA, CCPA, and emerging AI regulations. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Reference Data Manager (RefData Mgr) | Ultimately answerable for the entire lifecycle of reference data, including its quality, accessibility, and alignment with business needs. Approves new reference data sets and major changes. Ensures compliance with data governance and AI governance policies. |
| **R (Responsible)** | Data Steward (D-Steward) | Manages the content of specific reference data tables within their domain. Responsible for defining values, ensuring accuracy, and performing day-to-day maintenance. Acts as an agentic steward, proactively identifying improvements and risks. |
| **S (Supportive)** | Data Engineer (D-Eng) | Provides technical support for the storage, integration, and distribution of reference data tables, ensuring they are available to consuming systems. Supports automation, API development, and cloud-native deployment. |
| **C (Consulted)** | Subject Matter Expert (SME) | Provides deep business knowledge to define the valid values and business rules for a specific reference data domain. Advises on regulatory compliance and AI ethical considerations. |
| **I (Informed)** | Data Analyst (D-Analyst) | Kept informed of the available reference data sets and any changes, as they are a primary consumer of this data for analytics and reporting. Also includes AI modelers and data scientists who rely on consistent reference data for training and inference. |

### 2.2. Section-Level RASCI

| Template Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Table Properties | D-Steward | SME | RefData Mgr |
| Column Definitions | D-Steward | D-Eng | RefData Mgr |
| Data Content | D-Steward | SME | RefData Mgr |
| Governance and Metadata | D-Steward | RefData Mgr | RefData Mgr |

---

## 3. Template

> *The following is the standardized template for defining a Reference Data Table. This template should be completed for each new reference data set requested by the business.*

### 3.1. Table Properties

> *This section captures the high-level metadata and characteristics of the reference data table.*

**Input needed**: Business request, Data Domain from Business Glossary.  
**Who fills this**: Data Steward.

| Property | Value |
| :--- | :--- |
| **Table Name** | `[e.g., REF_Country]` |
| **Business Domain** | `[e.g., Customer]` |
| **Description** | `[A brief description of the data contained in the table and its purpose.]` |
| **Data Steward** | `[Name of the assigned Data Steward]` |
| **Subject Matter Expert** | `[Name of the primary SME]` |
| **Volatility** | `[Low / Medium / High - e.g., Low for countries, Medium for product categories]` |
| **Update Frequency** | `[e.g., Annually, Quarterly, As needed]` |
| **Data Classification** | `[e.g., Public, Internal, Confidential]` |
| **Compliance Requirements** | `[e.g., GDPR, HIPAA, EU AI Act]` |
| **Distribution Method** | `[e.g., API, Database replication, Flat file]` |
| **Source System(s)** | `[List of systems providing or consuming this reference data]` |

### 3.2. Column Definitions

> *Define the structure of the reference table, specifying each column's data type, constraints, and business meaning. Every reference table should have columns for a business key, a description, and lifecycle dates.*

**Input needed**: Naming conventions, data modeling standards.  
**Who fills this**: Data Steward, with consultation from a Data Engineer.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `[e.g., Country_Code]` | `[e.g., VARCHAR(2)]` | `PRIMARY KEY, NOT NULL` | `[The unique, business-friendly code for the reference value (e.g., ISO 3166-1 alpha-2).]` |
| `[e.g., Country_Name]` | `[e.g., VARCHAR(100)]` | `NOT NULL` | `[The full, descriptive name of the reference value.]` |
| `[e.g., Is_Active_Flag]` | `[e.g., CHAR(1)]` | `NOT NULL, CHECK (in ('Y','N'))` | `[Flag to indicate if the value is currently active and available for use.]` |
| `[e.g., Effective_Start_Date]` | `[e.g., DATE]` | `NOT NULL` | `[The date from which this reference value is valid.]` |
| `[e.g., Effective_End_Date]` | `[e.g., DATE]` | `NULL` | `[The date until which this reference value is valid. A NULL value indicates it is currently valid indefinitely.]` |
| `[e.g., Created_By]` | `[e.g., VARCHAR(50)]` | `NOT NULL` | `[User or system that created the record.]` |
| `[e.g., Created_Date]` | `[e.g., TIMESTAMP]` | `NOT NULL` | `[Date and time the record was created.]` |
| `[e.g., Last_Updated_By]` | `[e.g., VARCHAR(50)]` | `NULL` | `[User or system that last updated the record.]` |
| `[e.g., Last_Updated_Date]` | `[e.g., TIMESTAMP]` | `NULL` | `[Date and time the record was last updated.]` |
| `[...]` | `[...]` | `[...]` | `[Add any additional relevant attribute columns as needed.]` |

### 3.3. Data Content (Initial Set)

> *Provide the initial set of values for the reference data table. For large sets, this section can reference an attached file. The focus here is on providing a representative sample.*

**Input needed**: SME knowledge, external standards (e.g., ISO).  
**Who fills this**: Data Steward, with data provided by the SME.

| `[Country_Code]` | `[Country_Name]` | `[Is_Active_Flag]` | `[Effective_Start_Date]` | `[Effective_End_Date]` |
| :--- | :--- | :--- | :--- | :--- |
| `US` | `United States` | `Y` | `2000-01-01` | `NULL` |
| `CA` | `Canada` | `Y` | `2000-01-01` | `NULL` |
| `GB` | `United Kingdom` | `Y` | `2000-01-01` | `NULL` |
| `DE` | `Germany` | `Y` | `2000-01-01` | `NULL` |
| `FR` | `France` | `Y` | `2000-01-01` | `NULL` |
| `[...]` | `[...]` | `[...]` | `[...]` | `[...]` |

### 3.4. Governance and Maintenance

> *Describe the rules and processes for managing this reference data set over its lifecycle.*

**Input needed**: Data governance policies, change management procedures.  
**Who fills this**: Data Steward.

*   **Change Request Process**: `[Describe the process for requesting new values, or changes to existing values. Reference the Change Request Log output.]` Typically involves submission via a formal ticketing system (e.g., ServiceNow), including business justification and impact analysis. AI stewardship considerations should be included for reference data impacting AI models.
*   **Approval Workflow**: `[Detail the steps for approval, from submission by a business user to final approval by the Data Steward and/or Reference Data Manager.]` May include SME review, data governance council endorsement, and compliance checks.
*   **Data Quality Rules**: `[List specific data quality rules that apply to this table, e.g., "Country_Code must conform to ISO 3166-1 alpha-2 format."]` Include automated validation rules, periodic audits, and exception handling procedures.
*   **Distribution and Access**: `[Explain how consuming systems will access this data (e.g., via API, database replication, flat file). Reference the API Documentation or Integration Job Documentation outputs.]` Consider cloud-native distribution methods, caching strategies, and real-time synchronization.
*   **Security and Privacy Controls**: `[Outline access controls, encryption, and compliance with data protection regulations.]`
*   **Lifecycle Management**: `[Define archival policies, versioning, and deprecation procedures for obsolete reference data.]`
*   **AI Governance Alignment**: `[Describe how this reference data supports AI model governance, including traceability, bias mitigation, and auditability.]`

### 3.5. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-10_reference-data-tables.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

> *This is a realistic, filled-in example for a "Product Category" reference data table at a fictional company, GlobalRetail Inc.*

### 4.1. Table Properties

| Property | Value |
| :--- | :--- |
| **Table Name** | `REF_Product_Category` |
| **Business Domain** | `Product` |
| **Description** | `Defines the hierarchical classification of all products sold by GlobalRetail Inc. This table is the master source for product categorization in all sales, marketing, and inventory systems.` |
| **Data Steward** | `John Doe` |
| **Subject Matter Expert** | `Jane Smith (Head of Merchandising)` |
| **Volatility** | `Medium` |
| **Update Frequency** | `Quarterly` |
| **Data Classification** | `Internal` |
| **Compliance Requirements** | `GDPR, EU AI Act` |
| **Distribution Method** | `API, Database replication` |
| **Source System(s)** | `MDM Hub, ERP System` |

### 4.2. Column Definitions

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `Category_ID` | `INT` | `PRIMARY KEY, NOT NULL` | `The unique integer identifier for the product category.` |
| `Category_Name` | `VARCHAR(100)` | `NOT NULL` | `The business-friendly name of the category.` |
| `Parent_Category_ID` | `INT` | `NULL, FOREIGN KEY (REF_Product_Category.Category_ID)` | `The ID of the parent category, creating a hierarchy. NULL for top-level categories.` |
| `Is_Active_Flag` | `CHAR(1)` | `NOT NULL, CHECK (in ('Y','N'))` | `Indicates if the category is active for assigning to new products.` |
| `Effective_Start_Date` | `DATE` | `NOT NULL` | `The date from which this category is valid.` |
| `Effective_End_Date` | `DATE` | `NULL` | `The date until which this category is valid.` |
| `Created_By` | `VARCHAR(50)` | `NOT NULL` | `User who created the record.` |
| `Created_Date` | `TIMESTAMP` | `NOT NULL` | `Date and time the record was created.` |
| `Last_Updated_By` | `VARCHAR(50)` | `NULL` | `User who last updated the record.` |
| `Last_Updated_Date` | `TIMESTAMP` | `NULL` | `Date and time the record was last updated.` |

### 4.3. Data Content

| `Category_ID` | `Category_Name` | `Parent_Category_ID` | `Is_Active_Flag` | `Effective_Start_Date` | `Effective_End_Date` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Electronics | NULL | Y | 2010-03-01 | NULL |
| 2 | Home Goods | NULL | Y | 2010-03-01 | NULL |
| 3 | Televisions | 1 | Y | 2010-03-01 | NULL |
| 4 | Laptops | 1 | Y | 2012-08-15 | NULL |
| 5 | Kitchenware | 2 | Y | 2011-05-20 | NULL |
| 6 | Bedding | 2 | N | 2011-05-20 | 2023-12-31 |

### 4.4. Governance and Maintenance

*   **Change Request Process**: All requests for new categories or changes must be submitted via the "Product Category Request" form in ServiceNow. The request must include a business justification, expected impact, and any AI governance considerations if the data impacts AI models.
*   **Approval Workflow**: Requests are reviewed by the Merchandising team (SMEs). If approved, the Data Steward (John Doe) implements the change in the master reference data hub. Changes are bundled and deployed quarterly. Compliance and data governance councils may be consulted for high-impact changes.
*   **Data Quality Rules**: 
    1. `Category_Name` must be unique.
    2. A `Parent_Category_ID` must correspond to an existing, active `Category_ID`.
    3. No circular dependencies are allowed in the hierarchy.
    4. `Effective_Start_Date` must be before `Effective_End_Date` if the latter is not NULL.
*   **Distribution and Access**: The `REF_Product_Category` table is replicated in near real-time from the MDM hub to the Enterprise Data Warehouse and is exposed via the `ProductAPI` for other applications to consume. API access is secured via OAuth 2.0 and audited for compliance.
*   **Security and Privacy Controls**: Access is role-based, with read-only access for analytics teams and write access restricted to Data Stewards and Data Engineers.
*   **Lifecycle Management**: Obsolete categories are marked inactive and retained for historical reporting for 7 years before archival.
*   **AI Governance Alignment**: This reference data supports AI model feature engineering and classification tasks. Changes are logged and versioned to ensure traceability and reproducibility of AI outcomes.

---

### 4.5. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Change Request Log | Deliverable | **templates/deliverables/templates/templates-KA-01-data-governance.md** |
| API Documentation | Guide | **guides/integration/api-documentation.md** |
| Data Stewardship | Concept | [concepts/data-stewardship.md](references/concepts-governance-strategy.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [x] Table and column names adhere to enterprise naming conventions.
- [x] A Data Steward and SME have been formally assigned.
- [x] All columns are clearly defined with appropriate data types and constraints.
- [x] The table includes standard lifecycle columns (`Is_Active_Flag`, `Effective_Start_Date`, `Effective_End_Date`).
- [x] The change management process is clearly documented and linked to the corporate change management system.
- [x] At least one data quality rule is defined for the table.
- [x] The initial data content has been reviewed and approved by the SME.
- [x] Security and privacy controls are documented and enforced.
- [x] Compliance requirements (e.g., GDPR, EU AI Act) are identified and addressed.
- [x] Distribution methods support modern architectures (e.g., API, cloud-native replication).
- [x] AI governance considerations are integrated where applicable.

### 5.2. Review Checklist

| Criteria | What to Check | Expected Outcome |
| :--- | :--- | :--- |
| **Necessity** | Is this reference data set truly needed? Does a similar set already exist? | The reference data set fulfills a unique and documented business need. |
| **Clarity** | Are the table and column descriptions clear and unambiguous? | A business user can understand the purpose and content of the table without assistance. |
| **Atomicity** | Does each column represent a single, atomic piece of information? | No columns contain concatenated values (e.g., "Code - Description"). |
| **Consistency** | Is the format and content consistent with other, related reference data sets? | The table uses the same keys and conventions as other tables in the same domain. |
| **Maintainability** | Is the process for maintaining the data clear, efficient, and sustainable? | The defined workflow is practical and the assigned roles have the capacity to perform their duties. |
| **Security** | Are access controls and data protection measures in place? | Access is restricted appropriately and data is protected according to classification. |
| **Compliance** | Are regulatory requirements identified and met? | The table and processes comply with relevant laws and policies. |
| **Automation** | Are there opportunities for automation to improve quality and efficiency? | Automated validation, workflow, and distribution are planned or implemented. |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | Relationship | Relative Path |
| :--- | :--- | :--- |
| Reference Data Standards | Provides the rules, formats, and lifecycle management standards that this table must adhere to. | `templates/templates-KA-10-reference-master-data.md` |
| Business Glossary | Provides the business definition for the domain this reference data belongs to. | `templates/templates-KA-01-data-governance.md` |
| Change Request Log | Tracks requests for changes to reference data. | `templates/templates-KA-01-data-governance.md` |
| Data Governance Framework | Defines roles and responsibilities for reference data management. | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers (Outputs)

| Output Name | Relationship | Relative Path |
| :--- | :--- | :--- |
| Attribute Definitions | The attributes in a logical data model will be defined to use this reference table as their source of valid values. | `templates/templates-KA-03-data-modeling-design.md` |
| Transformation Rules | ETL/ELT jobs will use this reference table to validate or enrich data as it moves between systems. | `templates/templates-KA-06-data-integration-interoperability.md` |
| Data Quality Reports | Reports that monitor the quality of reference data values. | `templates/templates-KA-11-data-quality.md` |
| AI Model Feature Definitions | Reference data used as features or labels in AI/ML models. | `templates/templates-KA-12-data-handling-ethics.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **MDM / RDM Hub** | Informatica MDM, TIBCO EBX, Profisee | OpenMDM, Pimcore |
| **Data Catalog** | Collibra, Alation, Atlan | Amundsen, DataHub |
| **Data Quality** | Talend Data Quality, Ataccama, Informatica IDQ | Great Expectations, dbt |
| **Workflow Automation** | ServiceNow, IBM BPM, Camunda | Apache Airflow, n8n |
| **API Management** | Apigee, MuleSoft, Kong | Tyk, KrakenD |

### 7.2. Automation Opportunities

- **Automated Validation**: Implement automated data quality checks (using tools like Great Expectations) that run every time the reference data is updated, preventing invalid data from being published. Integrate with CI/CD pipelines for data products.
- **Workflow Automation**: Use a workflow engine (like the one in ServiceNow or a BPM tool) to automate the change request and approval process, reducing manual effort and improving traceability. Include AI governance checkpoints where applicable.
- **Automated Distribution**: Configure automated replication or API caching to ensure that as soon as reference data is updated in the central hub, it is immediately and consistently available to all consuming systems without manual intervention.
- **Versioning and Auditing**: Use tools that support version control and audit logging for reference data changes, enabling traceability for compliance and AI model reproducibility.
- **Integration with Data Mesh Platforms**: Leverage data mesh orchestration tools to synchronize reference data across domains while maintaining autonomy and governance.
- **FinOps and Cost Monitoring**: Monitor and optimize the cost of reference data storage and distribution, especially in multi-cloud environments.

---

## 8. References

1.  **DAMA-DMBOK2**: This output is based on the principles and practices described in Chapter 10, "Reference and Master Data Management," of the DAMA-DMBOK 2nd Edition.
2.  **DAMA-DMBOK3.0 (forthcoming)**: The upcoming 3rd Edition will expand on AI governance integration, agentic stewardship, and modern data architectures relevant to reference data management.
3.  **Internal Roles**: All role definitions can be found in the master `role-definitions.md` document.
4.  **Internal Standards**: All data management standards can be found in the respective KA folders (e.g., `templates/templates-KA-03-data-modeling-design.md`).
5.  **EU AI Act**: European Union legislation regulating AI systems, emphasizing data governance, transparency, and risk management.
6.  **Data Mesh Principles**: Refer to **guides/data-mesh-principles.md** for architectural context.
7.  **AI Governance Framework**: See **templates/templates-KA-12-data-handling-ethics.md** for governance integration details.


---

# Data Quality Rules for Master Data Management (MDM)


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Rule Identification](#31-rule-identification)
  - [3.2. Rule Definition](#32-rule-definition)
  - [3.3. Technical Implementation](#33-technical-implementation)
  - [3.4. Rule Governance](#34-rule-governance)
  - [3.5. Spreadsheet Template](#35-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Rule Identification](#41-rule-identification)
  - [4.2. Rule Definition](#42-rule-definition)
  - [4.3. Technical Implementation](#43-technical-implementation)
  - [4.4. Rule Governance](#44-rule-governance)
  - [4.5. Related Concepts and Guides](#45-related-concepts-and-guides)
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

**Data Quality Rules for Master Data Management (MDM)** are a specific set of conditions, constraints, and validation logic applied to master data entities to ensure they meet the organization's standards for accuracy, completeness, consistency, timeliness, validity, and uniqueness. These rules are the engine of data quality within an MDM framework, programmatically enforcing the policies and standards defined by data governance.

> The primary purpose of MDM Data Quality Rules is to proactively prevent data defects at the point of creation or modification, and to detect and facilitate the remediation of existing issues within the master data repository. They transform abstract quality dimensions into executable logic that safeguards the integrity of the 'golden record', which is foundational for trusted analytics, operational excellence, and AI/ML initiatives.

In the evolving landscape of data management, these rules also serve as critical enablers for **AI governance** by ensuring that master data feeding AI models is reliable and compliant with emerging regulations such as the **EU AI Act**. Furthermore, in modern architectures embracing **Data Mesh** and **Data Fabric** paradigms, data quality rules help maintain consistency across decentralized domains and federated data products.

Looking forward to **DAMA-DMBOK 3.0** (anticipated June 2025), the role of data quality rules will expand to incorporate **agentic data stewardship** and integration with **MLOps** and **DataOps** pipelines, emphasizing automation, continuous monitoring, and remediation within cloud-native and multi-cloud environments.

### 1.2. Scope

**Per Product** — Data Quality Rules are typically defined on a per-product or per-domain basis (e.g., for the Customer master, Product master, or Supplier master). While some generic rules (like format validation) may be reusable across domains, the most critical rules are context-specific to the attributes, business processes, and data contracts of a particular master data entity.

The scope also extends to ensuring compliance with **privacy and security regulations** such as GDPR, HIPAA, and CCPA, as well as emerging AI governance requirements. Rules may incorporate checks for data lineage, consent status, and ethical use flags, reflecting the growing importance of **AI Ethics Officers** and **Data Product Managers** in the governance ecosystem.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-11: Data Quality | This output is a direct implementation of the broader Data Quality KA. It operationalizes the concepts of data quality dimensions, metrics, and thresholds specifically for master data. It also aligns with the evolving practices in data quality automation and AI-driven anomaly detection. |
| KA-01: Data Governance | The rules are an enforcement mechanism for the policies and standards established by the Data Governance program. The Business Glossary (KA-01) provides the semantic foundation for rule definitions. The integration of AI governance and ethical data use policies is increasingly relevant here. |
| KA-03: Data Modeling & Design | The logical and physical data models for master data entities define the attributes and relationships upon which these quality rules are built. The rise of data contracts and data products as first-class citizens necessitates close collaboration with modeling teams. |
| KA-06: Data Integration & Interoperability | Data quality rules are critical for validating data as it is integrated into the MDM hub from various source systems, including cloud-native platforms and streaming data sources. They support interoperability in hybrid and multi-cloud environments. |
| KA-14: AI and Machine Learning | While not traditionally included, the upcoming DAMA-DMBOK 3.0 will formalize AI governance as a knowledge area, highlighting the role of master data quality rules in ensuring trustworthy AI outputs and compliance with AI regulations. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager (MDM Mgr) | Ultimately answerable for the definition, implementation, and effectiveness of the data quality rules within the MDM solution, including alignment with enterprise data governance and AI governance frameworks. |
| **R (Responsible)** | Data Quality Analyst (DQ Analyst) | Analyzes data quality requirements, profiles data, and defines the detailed logic for each data quality rule in collaboration with Data Stewards and Data Product Managers. Responsible for ensuring rules support automation and integration with DataOps/MLOps pipelines. |
| **S (Supportive)** | Data Steward (D-Steward) | Provides the business context, definitions, and acceptance criteria for data quality rules within their specific data domain. Supports the review and validation of rule outputs and participates in remediation workflows. |
| **C (Consulted)** | Data Owner (D-Owner) | Consulted to ensure that the data quality rules align with the business objectives, strategic value of the master data, and compliance requirements including AI ethics and regulatory mandates. |
| **I (Informed)** | Data Governance Manager (DG Mgr) | Kept informed of the defined rules to ensure they are consistent with the overall data governance framework, policies, and emerging AI governance practices. |

### 2.2. Section-Level RASCI

| Section / Activity | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Rule Identification & Prioritization | DQ Analyst | D-Steward, D-Owner | MDM Mgr |
| Rule Logic Definition | DQ Analyst | D-Steward, Data Product Manager | MDM Mgr |
| Rule Implementation & Testing | MDM Developer | DQ Analyst, MLOps Engineer | MDM Mgr |
| Rule Execution & Monitoring | MDM System (Automated) | DQ Analyst, D-Steward | MDM Mgr |
| Exception Handling & Remediation | D-Steward | DQ Analyst | D-Owner |

---

## 3. Template

> *The following is the standardized template for defining a Data Quality Rule for a master data entity. Each rule should be documented using this template.*

### 3.1. Rule Identification

| Field | Value |
| :--- | :--- |
| Rule ID | [e.g., DQ-MDM-CUST-001] |
| Rule Name | [A concise, descriptive name, e.g., 'Valid US State Abbreviation'] |
| Master Data Entity | [e.g., Customer, Product, Supplier] |
| Attribute(s) | [The specific attribute(s) the rule applies to, e.g., `Address.State`] |
| Data Quality Dimension(s) | [e.g., Validity, Accuracy, Consistency] |
| Creation Date | [YYYY-MM-DD] |
| Version | [e.g., 1.0] |
| Status | [e.g., Proposed, Active, Inactive, Retired] |

### 3.2. Rule Definition

> *This section provides the business context and logic for the rule in plain language.*

**Input needed**: Business Glossary, Data Dictionary, interviews with Data Stewards, Data Product Managers, AI Ethics Officers.  
**Who fills this**: DQ Analyst, in consultation with D-Steward and Data Product Manager.

**Description**:  
> *Explain what the rule does and why it is important. What business impact does it prevent or enable?*  
[e.g., This rule ensures that the state field for all US customer addresses contains a valid two-letter state abbreviation as defined by the USPS. This is critical for accurate mail delivery, sales tax calculation, and territory assignment. Additionally, it supports compliance with regional regulations and enables reliable AI-driven customer segmentation.]

**Business Logic**:  
> *Describe the rule's logic in a clear, step-by-step manner using business terms.*  
1. Check if the `Address.Country` is 'USA'.  
2. If yes, check if the value in `Address.State` exists in the official 'US State Abbreviations' reference data list.  
3. If the value is not in the reference list, the record fails this quality check.

### 3.3. Technical Implementation

> *This section provides the technical details for implementing the rule in the MDM tool.*

**Input needed**: MDM tool documentation, technical specifications, AI governance policies.  
**Who fills this**: MDM Developer or DQ Analyst.

**Rule Type**: [e.g., Validation, Cleansing, Standardization, Matching]

**Execution Trigger**: [e.g., On Create, On Update, Batch (Nightly), Streaming]

**Technical Logic / Pseudocode**:  
> *Provide the logic in a format that a developer can easily translate into code or configure in the tool.*

```sql
CASE
  WHEN Address.Country = 'USA' AND Address.State NOT IN (SELECT state_code FROM reference.us_states)
  THEN 'FAIL'
  ELSE 'PASS'
END
```

**Source of Truth / Reference Data**: [e.g., `reference.us_states` table, external API call to validation service]

**Integration Notes**:  
> Consider integrating rule execution with DataOps and MLOps pipelines to enable continuous data quality monitoring and automated remediation where feasible. Leverage cloud-native orchestration tools and APIs for scalability.

### 3.4. Rule Governance

> *This section defines the ownership and handling procedures for the rule.*

**Input needed**: RASCI matrix, SLA documentation, AI governance policies.  
**Who fills this**: DQ Analyst, MDM Mgr.

**Rule Owner**: [The role accountable for the rule's performance, e.g., MDM Manager]

**Remediation Workflow**:  
> *Describe the process for handling records that fail this rule.*  
1. Failing records are flagged with Rule ID [DQ-MDM-CUST-001].  
2. A data quality exception task is created and assigned to the [Customer Data Steward] group.  
3. The Data Steward has [2] business days (SLA) to review the exception and correct the address information in the source system or MDM hub.  
4. For recurring failures, escalation to the Data Governance Manager and AI Ethics Officer may be triggered to assess systemic issues or compliance risks.

**Severity Level**: [e.g., High, Medium, Low - based on business impact and regulatory risk]

**Audit and Compliance**:  
> Maintain audit logs of rule execution and remediation actions to support compliance with GDPR, HIPAA, CCPA, and the EU AI Act. Ensure traceability of data corrections and approvals.

---

### 3.5. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-10_data-quality-rules-mdm.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.  
>
> The spreadsheet also supports integration with automated data quality tools and dashboards, enabling real-time monitoring and reporting.

## 4. Example

> *This is a realistic example of a filled-in template for a data quality rule at the fictional company GlobalRetail Inc.*

### 4.1. Rule Identification

| Field | Value |
| :--- | :--- |
| Rule ID | DQ-MDM-PROD-012 |
| Rule Name | Consistent Unit of Measure (UOM) for Weight |
| Master Data Entity | Product |
| Attribute(s) | `Product.Weight`, `Product.WeightUOM` |
| Data Quality Dimension(s) | Consistency, Standardization |
| Creation Date | 2025-10-26 |
| Version | 1.1 |
| Status | Active |

### 4.2. Rule Definition

**Description**:  
This rule ensures that the Unit of Measure (UOM) for product weight is standardized to 'KG' (Kilograms) for all products classified under the 'Electronics' category. Inconsistent UOMs (e.g., lbs, grams, oz) for similar products lead to major errors in logistics planning, shipping cost calculation, and inventory management. This rule enforces a standard to enable accurate reporting and analytics. It also supports AI models that rely on consistent measurement units for demand forecasting and pricing optimization.

**Business Logic**:  
1. Check if the `Product.Category` is 'Electronics'.  
2. If yes, check if the `Product.WeightUOM` is not equal to 'KG'.  
3. If the UOM is not 'KG', the rule attempts to automatically convert the weight and UOM.  
4. If auto-conversion is not possible (e.g., UOM is invalid), the record fails and is flagged for manual review.

### 4.3. Technical Implementation

**Rule Type**: Standardization & Cleansing

**Execution Trigger**: On Update, Batch (Nightly)

**Technical Logic / Pseudocode**:  
```javascript
if (Product.Category === 'Electronics' && Product.WeightUOM !== 'KG') {
  let newWeight = Product.Weight;
  let newUOM = 'KG';
  switch (Product.WeightUOM) {
    case 'LBS':
      newWeight = Product.Weight * 0.453592;
      break;
    case 'G':
      newWeight = Product.Weight / 1000;
      break;
    case 'OZ':
      newWeight = Product.Weight * 0.0283495;
      break;
    default:
      return 'FAIL'; // Invalid or non-convertible UOM
  }
  Product.Weight = newWeight.toFixed(4);
  Product.WeightUOM = newUOM;
  return 'PASS_CONVERTED';
} else {
  return 'PASS';
}
```

**Source of Truth / Reference Data**: Internal UOM conversion factors table.

**Integration Notes**:  
This rule is integrated with the DataOps pipeline to enable automated remediation where possible, reducing manual intervention and improving data freshness. Monitoring dashboards track conversion success rates and flag anomalies for further investigation.

### 4.4. Rule Governance

**Rule Owner**: MDM Manager

**Remediation Workflow**:  
1. Records that fail (i.e., have an invalid UOM that cannot be converted) are flagged with Rule ID DQ-MDM-PROD-012.  
2. An exception task is routed to the 'Product Data Stewardship' queue in the MDM workflow tool.  
3. The Product Data Steward must investigate the source system record, determine the correct weight and UOM, and update the master record within 1 business day (SLA).  
4. Persistent issues trigger escalation to the Data Governance Manager and Data Product Manager for root cause analysis and potential source system remediation.

**Severity Level**: High

### 4.5. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Quality Dimensions | Knowledge Area | [templates/templates-KA-11-data-quality.md](templates/templates-KA-11-data-quality.md) |
| Data Governance Roles | Reference | [references/reference-materials.md](references/reference-materials.md) |
| Data Contracts | Concept | [#](references/concepts-modern-paradigms.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The rule has a unique, well-formed Rule ID.  
- [x] The rule is mapped to at least one Data Quality Dimension.  
- [x] The business logic is clear, unambiguous, and validated by a Data Steward and Data Product Manager.  
- [x] The technical logic is documented, tested, and integrated with automation pipelines where applicable.  
- [x] A remediation workflow and SLA are defined, including escalation paths for persistent issues.  
- [x] The rule has an assigned owner and severity level aligned with business impact and compliance risk.  
- [x] The rule has been successfully tested against a representative data sample and monitored in production.  
- [x] The rule supports auditability and compliance with relevant regulations and AI governance policies.

### 5.2. Review Checklist

| Question | Check | Reviewer Role |
| :--- | :--- | :--- |
| Is the rule's business purpose clearly articulated and justified? | &#9744; | D-Owner |
| Does the rule logic correctly reflect the documented business requirement? | &#9744; | D-Steward |
| Is the rule overly complex? Can it be simplified? | &#9744; | MDM Developer |
| Does the rule have any unintended performance impacts on the MDM system? | &#9744; | MDM Architect |
| Is the remediation process clear and actionable for the assigned stewards? | &#9744; | D-Steward |
| Does the rule conflict with or duplicate any other existing rules? | &#9744; | DQ Analyst |
| Is the rule aligned with AI governance and regulatory compliance requirements? | &#9744; | AI Ethics Officer |
| Is the rule integrated with DataOps/MLOps pipelines for automation? | &#9744; | MLOps Engineer |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Golden Record Definition | Provides the list of master data attributes that require quality rules. | `templates/templates-KA-10-reference-master-data.md` |
| Data Quality Dimensions | Defines the standard quality dimensions (e.g., Accuracy, Completeness) that this rule measures. | `templates/templates-KA-11-data-quality.md` |
| Business Glossary | Provides semantic definitions and business terms used in rule definitions. | `templates/templates-KA-09-metadata-management.md` |
| Data Contracts | Defines the expectations and SLAs for data products and master data entities. | `#` |

### 6.2. Consumers (This Output is Input for)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Quality Rules (Enterprise) | These MDM-specific rules may be promoted or adapted for broader enterprise use, including data products in a Data Mesh architecture. | `templates/templates-KA-11-data-quality.md` |
| Data Quality Report | The output of these rules (pass/fail counts) is a key input for data quality reports and dashboards, including AI model data quality monitoring. | `templates/templates-KA-11-data-quality.md` |
| Data Product Outputs | Data quality rules influence the quality and trustworthiness of data products. | `references/reference-materials.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Examples | Open Source Examples |
| :--- | :--- | :--- |
| **MDM Platforms** | Informatica MDM, TIBCO EBX, Semarchy, Profisee | Pimcore, OpenMDM |
| **Data Quality Suites** | Informatica Data Quality (IDQ), Talend Data Quality, Ataccama, Trillium | Great Expectations, Soda Core, Apache Griffin |
| **Data Profiling Tools** | Included in most DQ Suites | Pandas Profiling, DataCleaner |
| **Workflow/BPM Tools** | ServiceNow, Pega, Appian | Camunda, jBPM |
| **DataOps / MLOps Platforms** | DataKitchen, Domino Data Lab, MLflow | Kedro, Kubeflow |

### 7.2. Automation Opportunities

- **Rule Execution**: The core execution of data quality rules should be fully automated within the MDM platform, triggered by data creation/update events or scheduled batch jobs. Integration with streaming platforms supports near real-time validation in cloud-native environments.  
- **Exception Notification**: When a rule fails, the system should automatically generate a notification and create a task in a workflow tool, assigning it to the appropriate Data Steward or remediation queue. AI-driven prioritization can optimize task assignment.  
- **Dashboarding**: The results of rule executions (pass, fail, converted counts) should be automatically aggregated and fed into data quality dashboards (e.g., in Power BI, Tableau) to provide real-time monitoring of the health of master data and data products.  
- **Automated Remediation**: For certain predictable errors (like the UOM conversion example), the system can be configured to automatically apply the fix without human intervention, logging the action for audit purposes. This aligns with emerging **FinOps** practices to optimize operational costs.  
- **AI Governance Integration**: Data quality rules can feed into AI governance frameworks by flagging data quality issues that may bias or degrade AI model performance, supporting continuous model monitoring and retraining triggers.

---

## 8. References

1.  DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge*. 2nd ed., Technics Publications, 2017. (Chapter 10: Reference and Master Data)  
2.  DAMA International. *DAMA-DMBOK 3.0* (In Development, Launch Expected June 2025). For updates on AI governance, data mesh/fabric integration, and emerging roles.  
3.  Internal Document: `role-definitions.md` - For detailed descriptions of the roles mentioned in the RASCI matrices.  
4.  European Commission. *EU AI Act* (Draft) – Regulatory framework impacting data governance and quality for AI systems.  
5.  Gartner Research. *Data Mesh and Data Fabric Synergy* – Trends in modern data architectures supporting decentralized data governance.  
6.  Ataccama. *Automated Data Quality and AI Governance* – Whitepaper on integrating data quality rules with AI governance frameworks.


---

# Hierarchy Definitions


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
  - [3.2. Hierarchy Overview](#32-hierarchy-overview)
  - [3.3. Hierarchy Structure](#33-hierarchy-structure)
  - [3.4. Node Relationship Rules](#34-node-relationship-rules)
  - [3.5. Hierarchy Maintenance](#35-hierarchy-maintenance)
  - [3.6. Spreadsheet Template](#36-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Hierarchy Overview](#42-hierarchy-overview)
  - [4.3. Hierarchy Structure](#43-hierarchy-structure)
  - [4.4. Node Relationship Rules](#44-node-relationship-rules)
  - [4.5. Hierarchy Maintenance](#45-hierarchy-maintenance)
  - [4.6. Related Concepts and Guides](#46-related-concepts-and-guides)
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

**Hierarchy Definitions** are a foundational component of Master Data Management (MDM) that formally document the relationships and organizational structures between master data entities. These definitions specify how individual data records aggregate into parent levels, creating a tree-like or networked structure that reflects the business’s operational and analytical realities. Hierarchies enable consistent data aggregation, drill-down analysis, and alignment across disparate systems and business units.

In the evolving landscape of data management, hierarchy definitions play a pivotal role in enabling modern analytics, AI governance, and data productization. They ensure that data consumers—from business analysts to AI models—interpret data consistently, supporting trustworthy insights and compliance with regulatory frameworks such as GDPR, HIPAA, CCPA, and the emerging EU AI Act.

> The purpose of defining hierarchies is to enable consistent aggregation, drill-down, and analysis of data, ensuring that all business units and data consumers view and interpret data through a unified structural lens. This consistency supports data mesh and data fabric architectures by providing clear data domain boundaries and lineage.

### 1.2. Scope

**Per Product** — Hierarchy Definitions are typically created for each master data product (e.g., Customer, Product, Chart of Accounts). While the principles of hierarchy management are global, the specific structures are tailored to the nuances of each data domain and business context.

With the rise of cloud-native architectures and multi-cloud deployments, hierarchy definitions must also consider cross-platform consistency and interoperability. They support the creation of data contracts and data products, enabling autonomous teams within a data mesh to manage their hierarchies while adhering to enterprise-wide standards.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| [KA-01: Data Governance](knowledge-areas/KA-01-data-governance.md) | Data governance processes are essential for approving, auditing, and managing changes to master data hierarchies, ensuring compliance with policies and regulations including AI governance frameworks. |
| [KA-03: Data Modeling and Design](knowledge-areas/KA-03-data-modeling-and-design.md) | Logical and physical data models provide the foundational entities upon which hierarchies are built, supporting integration with data mesh domains and data fabric layers. |
| [KA-08: Data Warehousing and BI](knowledge-areas/KA-08-data-warehousing-and-bi.md) | Hierarchies are fundamental to dimensional modeling (e.g., star schemas) used in data warehouses, lakehouses, and BI reporting, enabling performant and consistent analytics. |
| [KA-09: Metadata Management](knowledge-areas/KA-09-metadata-management.md) | The metadata repository stores and manages hierarchy definitions, making them discoverable, understandable, and traceable, which is critical for lineage and AI model explainability. |
| [KA-10: Reference and Master Data](knowledge-areas/KA-10-reference-and-master-data.md) | Hierarchy definitions are a key deliverable within master data management, supporting the integrity and usability of reference data domains. |
| [KA-11: Data Quality](knowledge-areas/KA-11-data-quality.md) | Data quality rules ensure the integrity and validity of hierarchical relationships, preventing issues such as circular references or orphan nodes. |
| [KA-14: AI and Analytics Governance](knowledge-areas/KA-14-data-management-maturity-assessment.md) | Hierarchies support AI governance by providing structured, validated data inputs for AI/ML models, enabling traceability and compliance with AI ethics and regulatory requirements. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager (MDM Mgr) | Ultimately accountable for the accuracy, completeness, approval, and compliance of hierarchy definitions within the master data domain, including alignment with AI governance and data product standards. |
| **R (Responsible)** | Data Steward (D-Steward) | Responsible for defining, documenting, maintaining, and periodically reviewing hierarchy structures based on evolving business requirements and data governance policies. |
| **S (Supportive)** | Data Modeler (D-Modeler) | Supports by ensuring data models can accommodate hierarchy requirements and by assisting with technical implementation and validation. |
| **C (Consulted)** | Subject Matter Expert (SME), Data Owner (D-Owner) | Consulted to provide domain expertise, business rules, and logic governing hierarchical relationships, including regulatory and compliance considerations. |
| **I (Informed)** | Data Analyst (D-Analyst), AI/ML Engineer | Informed of hierarchy definitions to ensure correct usage in reporting, analytics, and AI/ML model development, supporting data literacy and governance. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Hierarchy Overview | D-Steward | SME, D-Owner | MDM Mgr |
| Hierarchy Levels | D-Steward | D-Modeler | MDM Mgr |
| Node Relationships | D-Steward | SME | MDM Mgr |
| Maintenance Rules | D-Steward | D-Owner | MDM Mgr |

---

## 3. Template

> *The following is the standardized template for creating Hierarchy Definitions. Replace all placeholders `[...]` with specific information for the master data domain.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Hierarchy Definitions for [Master Data Domain] |
| Document ID | HIER-DEF-[Domain Code]-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [MDM Manager Name] |

### 3.2. Hierarchy Overview

> *Provide a high-level description of the hierarchy, its purpose, and the business context it represents.*

**Hierarchy Name**: [e.g., Product Category Hierarchy]

**Description**: [e.g., This hierarchy organizes individual products into a multi-level structure for sales and marketing reporting.]

**Business Purpose**: [e.g., To enable analysis of product performance at different levels of granularity, from individual SKU to product line to division.]

**Contextual Notes**:  
- Alignment with enterprise data governance and AI governance policies.  
- Integration with data mesh domains or data fabric layers, if applicable.  
- Compliance considerations (e.g., GDPR, EU AI Act).  
- Support for data productization and data contracts.

### 3.3. Hierarchy Structure

> *Define the levels of the hierarchy, from the top (most aggregated) to the bottom (most granular).*

| Level | Level Name | Description |
| :--- | :--- | :--- |
| 1 | [e.g., Division] | [e.g., The highest-level business unit responsible for a portfolio of product lines.] |
| 2 | [e.g., Product Line] | [e.g., A group of related products marketed under a single brand or to a specific customer segment.] |
| 3 | [e.g., Product Family] | [e.g., A sub-grouping of products within a product line with similar features or technology.] |
| 4 | [e.g., Product SKU] | [e.g., The individual stock-keeping unit, representing a specific product variant.] |

> *Consider including additional levels or alternative structures to support ragged or unbalanced hierarchies as needed.*

### 3.4. Node Relationship Rules

> *Describe the rules that govern the relationships between nodes in the hierarchy. This includes cardinality and any specific business logic.*

- **Parent-Child Relationship**: [e.g., A record at a lower level can have only one parent in the level directly above it.]  
- **Cardinality**: [e.g., One-to-many from parent to child (e.g., one Product Line can have many Product Families).]  
- **Ragged/Unbalanced**: [e.g., Specify if the hierarchy can be ragged (nodes at the same level have different numbers of children) or unbalanced (leaf nodes are at different depths).]  
- **Circular Reference Prevention**: [e.g., Rules to prevent cycles within the hierarchy.]  
- **Cross-Domain Relationships**: [e.g., If applicable, define rules for relationships crossing master data domains or data products.]  
- **Versioning and Temporal Validity**: [e.g., Rules for managing historical changes and effective dates of hierarchy nodes.]

### 3.5. Hierarchy Maintenance

> *Outline the procedures for maintaining the hierarchy, including adding, updating, and retiring nodes and relationships.*

- **New Node Creation**: [e.g., Process for requesting and approving the addition of a new product to the hierarchy, including data quality checks and governance approvals.]  
- **Re-parenting Nodes**: [e.g., Rules and approvals required to move a product from one product family to another, including impact analysis.]  
- **Node Deactivation**: [e.g., Process for retiring a product from the hierarchy when it is no longer sold or relevant, including archival and audit trail requirements.]  
- **Change Management**: [e.g., Formal change request process, including stakeholder notification and documentation updates.]  
- **Periodic Review**: [e.g., Scheduled reviews to validate hierarchy accuracy and relevance, aligned with data governance cycles.]  
- **Integration with Automation**: [e.g., Use of automated workflows, alerts, and validations to support maintenance activities.]  

---

### 3.6. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:

> *Note: The spreadsheet template KA-10_hierarchy-definitions.xlsx can be generated by Claude on request.*

> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Hierarchy Definitions for GlobalRetail Inc. Customer Demographics |
| Document ID | HIER-DEF-CUST-001 |
| Version | 1.2 |
| Effective Date | 2025-10-26 |
| Owner | John Smith, MDM Manager |

### 4.2. Hierarchy Overview

**Hierarchy Name**: Customer Geographic Hierarchy

**Description**: This hierarchy organizes individual customers into a geographic structure for sales territory management and regional marketing campaigns.

**Business Purpose**: To enable analysis of customer distribution and sales performance by geographic area, from individual postal code to global region.

**Contextual Notes**:  
- Supports compliance with data privacy regulations by enabling region-based data segmentation.  
- Integrated with data mesh domains responsible for geographic data products.  
- Enables AI models to incorporate geographic context for customer segmentation.

### 4.3. Hierarchy Structure

| Level | Level Name | Description |
| :--- | :--- | :--- |
| 1 | Global Region | The highest-level geographic area (e.g., Americas, EMEA, APAC). |
| 2 | Country | A specific country within a Global Region. |
| 3 | State/Province | A state or province within a Country. |
| 4 | City | A city within a State/Province. |
| 5 | Postal Code | The most granular level, representing a customer's postal code. |

### 4.4. Node Relationship Rules

- **Parent-Child Relationship**: A customer is assigned to a single Postal Code. Each Postal Code belongs to one City, each City to one State/Province, and so on.  
- **Cardinality**: One-to-many from parent to child (e.g., one Country can have many States/Provinces).  
- **Ragged/Unbalanced**: The hierarchy is unbalanced as some countries may not have states/provinces as a relevant administrative level.  
- **Circular Reference Prevention**: Hierarchy validation rules prevent loops in geographic assignments.  
- **Versioning**: Changes to geographic boundaries are tracked with effective dates to support historical reporting.

### 4.5. Hierarchy Maintenance

- **New Node Creation**: New geographic nodes (e.g., a new city) are added based on quarterly reviews of customer address data. The Data Steward for Customer data is responsible for these updates, following governance approval.  
- **Re-parenting Nodes**: Changes to administrative boundaries (e.g., redistricting) require a formal change request, impact analysis, and approval from the MDM Manager.  
- **Node Deactivation**: Geographic nodes with no associated customers for more than 12 months are reviewed for deactivation, with archival in metadata repositories.  
- **Automation**: Automated workflows notify stakeholders of proposed changes and validate data quality before approval.

---

### 4.6. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Master Data Model | Deliverable | [06-master-data-model.md](./06-master-data-model.md) |
| Data Governance Roles and Responsibilities | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| Dimensional Model | Deliverable | [templates/templates-KA-08-data-warehousing-bi.md](templates/templates-KA-08-data-warehousing-bi.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The hierarchy has a clearly defined and documented business purpose aligned with enterprise goals.  
- [x] All levels of the hierarchy are documented with clear, unambiguous descriptions.  
- [x] The rules governing parent-child relationships are explicitly stated and validated.  
- [x] The maintenance procedures for the hierarchy are defined, including governance and automation aspects.  
- [x] The hierarchy definitions have been reviewed and formally approved by the MDM Manager and relevant stakeholders.  
- [x] The hierarchy supports compliance with applicable data governance, AI governance, and regulatory requirements.  
- [x] The hierarchy structure is compatible with enterprise data architecture patterns such as data mesh and data fabric.

### 5.2. Review Checklist

| Question | Yes/No |
| :--- | :--- |
| Is the hierarchy structure aligned with business reporting and analytical requirements? | Yes |
| Are the hierarchy levels mutually exclusive and collectively exhaustive? | Yes |
| Are the node relationship rules unambiguous and enforceable? | Yes |
| Is there a clear process for managing changes to the hierarchy, including governance and automation? | Yes |
| Does the hierarchy support AI governance and regulatory compliance needs? | Yes |
| Are the hierarchy definitions integrated with metadata management and data quality processes? | Yes |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship |
| :--- | :--- |
| [Master Data Model](./06-master-data-model.md) | The Master Data Model provides the underlying entities (e.g., Customer, Product) for which hierarchies are defined. |
| [Data Governance Roles and Responsibilities](templates/templates-KA-01-data-governance.md) | Defines the roles (e.g., Data Steward, MDM Manager) responsible for creating and maintaining hierarchies. |
| **Data Quality Rules** | Data quality rules ensure the integrity and validity of hierarchical relationships. |

### 6.2. Consumers

| Output | Relationship |
| :--- | :--- |
| [Dimensional Model](templates/templates-KA-08-data-warehousing-bi.md) | The Hierarchy Definitions are used to create the dimension tables in the dimensional model. |
| [Data Product Outputs](references/reference-materials.md) | Hierarchy definitions support the creation and management of data products and data contracts. |
| **Metadata Repository** | Stores and manages hierarchy metadata for discovery and lineage. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| MDM Platforms | Informatica MDM, TIBCO EBX, Profisee | Pimcore, AtroPIM |
| Data Modeling Tools | Erwin, ER/Studio | Draw.io, OpenModelSphere |
| Metadata Management | Collibra, Alation | Apache Atlas, Amundsen |
| Workflow Automation | ServiceNow, Jira | Apache Airflow, n8n |

### 7.2. Automation Opportunities

- **Hierarchy Discovery**: Automated tools can analyze data relationships and distributions to suggest potential hierarchies, accelerating initial design and ongoing validation.  
- **Hierarchy Maintenance**: Workflow automation can manage requests for new nodes or changes, including routing for approvals, notifications, and audit logging.  
- **Hierarchy Validation**: Automated data quality rules can validate hierarchy integrity, checking for circular references, orphan nodes, and compliance with cardinality rules.  
- **Version Control and Change Tracking**: Integration with version control systems and metadata repositories to maintain historical versions and audit trails.  
- **Integration with MLOps and DataOps**: Ensuring that hierarchy changes propagate correctly to AI/ML pipelines and data product deployments, supporting continuous delivery and governance.

---

## 8. References

- DAMA-DMBOK2, Chapter 10: Reference and Master Data.  
- DAMA-DMBOK 3.0 (forthcoming, June 2025): Enhanced guidance on AI governance, data mesh/fabric integration, and cloud-native data architectures.  
- EU AI Act and GDPR compliance frameworks relevant to master data and hierarchy governance.  
- Industry best practices for data product management, data contracts, and agentic data stewardship.


---

# Master Data Governance Workflow


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Workflow Diagram (BPMN)](#31-workflow-diagram-bpmn)
  - [3.2. Workflow Stages](#32-workflow-stages)
- [4. Example](#4-example)
  - [4.1. Scenario Overview](#41-scenario-overview)
  - [4.2. Detailed Walkthrough](#42-detailed-walkthrough)
  - [4.3. Lessons Learned](#43-lessons-learned)
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

The **Master Data Governance Workflow** is a standardized, repeatable process that defines the steps for creating, approving, managing, and retiring master data. It serves as the operational arm of the Master Data Management (MDM) strategy, translating governance policies into a series of actionable tasks and decision points. The workflow ensures that every piece of master data adheres to defined quality standards, business rules, and architectural principles throughout its lifecycle.

This workflow is increasingly critical in modern data environments characterized by distributed data ownership, cloud-native architectures, and the integration of AI-driven data processes. It supports the enforcement of data governance policies in complex ecosystems such as data mesh and data fabric, where master data serves as a foundational asset enabling interoperability and data productization.

> The primary purpose of this workflow is to enforce consistency, accuracy, and accountability in the management of master data assets, thereby reducing operational risk, improving decision-making, and increasing the overall value of the organization's data. It also supports compliance with emerging regulations including the EU AI Act, GDPR, HIPAA, and CCPA, ensuring that master data governance aligns with ethical and legal standards in AI and data use.

Looking forward, the forthcoming DAMA-DMBOK 3.0 emphasizes the integration of AI governance, agentic data stewardship, and the elevation of data contracts and data products as first-class concepts within workflows such as this. Organizations are encouraged to evolve this workflow to incorporate these emerging best practices.

### 1.2. Scope

**Global** — This workflow applies to all master data domains (e.g., Customer, Product, Supplier, Employee) across the entire organization. It provides a universal framework adaptable for the specific nuances of each domain while maintaining a consistent governance process.

The scope includes:

- Governance of master data lifecycle stages from creation through retirement.
- Integration with data quality, data privacy, and compliance controls.
- Support for multi-cloud and hybrid environments, ensuring synchronization across diverse platforms.
- Alignment with data mesh principles by facilitating decentralized stewardship and domain-oriented ownership while maintaining centralized standards.
- Incorporation of AI governance checkpoints where AI-generated or AI-enriched master data is involved.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The workflow is a direct implementation of the principles and policies defined in the Data Governance Framework. It operationalizes the roles and responsibilities established in the governance charter and integrates with AI governance practices. |
| KA-03: Data Modeling and Design | The workflow ensures that all new or modified master data entities conform to the approved conceptual, logical, and physical data models, including data product definitions and data contracts. |
| KA-06: Data Integration & Interoperability | The workflow governs the data shared and synchronized across systems, ensuring that integration processes are fed with high-quality, standardized master data, supporting data fabric and mesh architectures. |
| KA-09: Data Privacy & Security | The workflow embeds privacy and security controls, ensuring compliance with GDPR, HIPAA, CCPA, and the EU AI Act. |
| KA-11: Data Quality | Data quality rules and metrics are embedded as checkpoints within the workflow to prevent the creation or propagation of poor-quality data, including AI-driven data quality monitoring. |
| KA-12: Reference and Master Data Management | This workflow is a core deliverable within this knowledge area, operationalizing master data governance best practices and supporting the creation and maintenance of golden records. |
| KA-14: Data Operations (DataOps) | The workflow supports integration with DataOps practices, enabling automation, monitoring, and continuous improvement of master data processes. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager (MDM Mgr) | Ultimately answerable for the effectiveness, efficiency, and adoption of the master data governance workflow across the enterprise. Responsible for ensuring alignment with enterprise data strategy and compliance requirements, including AI governance. |
| **R (Responsible)** | Data Governance Analyst (DG Analyst) | Designs, documents, maintains, and monitors the workflow. Provides training and support to users of the workflow. Leads continuous improvement initiatives and integration with DataOps and MLOps teams. |
| **S (Supportive)** | Data Steward (D-Steward) | Executes the tasks within the workflow, such as data validation, enrichment, and issue remediation. Provides subject matter expertise and acts as a liaison with domain teams and AI ethics officers when applicable. |
| **C (Consulted)** | Data Owner (D-Owner), Data Governance Manager (DG Mgr), AI Ethics Officer | Consulted on workflow design and any proposed changes to ensure alignment with business needs, overall governance strategy, and ethical AI considerations. |
| **I (Informed)** | Chief Data Officer (CDO), Chief AI Officer (CAIO) | Kept informed of the workflow's performance, key metrics, and any significant escalations or changes. Ensures strategic oversight and alignment with enterprise data and AI governance policies. |

### 2.2. Section-Level RASCI

| Workflow Stage | Primary Executor (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| 1. Request Initiation | Business User, DG Analyst | Data Steward | N/A |
| 2. Data Validation & Enrichment | Data Steward | Subject Matter Expert, AI Ethics Officer (if AI-generated data) | Data Steward |
| 3. Duplicate Check & Resolution | MDM System, Data Steward | Data Steward | Data Owner |
| 4. Approval | Data Owner | Business Stakeholder, AI Ethics Officer (if applicable) | Data Owner |
| 5. Data Creation/Update | MDM System (automated), Data Custodian | N/A | N/A |
| 6. Publication & Synchronization | MDM System (automated) | Integration Team | N/A |
| 7. Issue Management | Data Steward | DG Analyst | MDM Mgr |

---

## 3. Template

> *This template provides a standardized workflow for governing master data. It should be configured within a workflow management tool (e.g., BPMN-compliant engine) and integrated with the organization's MDM platform. Consider incorporating AI governance checkpoints and automation to enhance efficiency and compliance.*

### 3.1. Workflow Diagram (BPMN)

> *A visual representation of the workflow should be created using Business Process Model and Notation (BPMN 2.0). This diagram serves as the primary reference for understanding the flow of tasks, decisions, and roles. The diagram should be embedded here.*

[Placeholder for BPMN 2.0 XML or an embedded image of the workflow diagram]

### 3.2. Workflow Stages

#### 3.2.1. Stage 1: Request Initiation

> *This stage describes how a request to create a new master data record or modify an existing one is initiated.*

- **Trigger**: A business user identifies the need for a new master data record (e.g., a new customer) or a change to an existing one.
- **Action**: The user accesses the Master Data Request Form through the company portal or MDM interface.
- **Input Form Fields**:
    - `[Request Type (New/Modify)]`
    - `[Master Data Domain (e.g., Customer, Product)]`
    - `[Record ID (if Modify)]`
    - `[Requester Name & Department]`
    - `[Business Justification]`
    - `[Core Data Attributes (as required by the domain)]`
    - `[Attached Supporting Documents]`
    - `[AI Involvement Indicator]` *(New field to flag if AI-generated or AI-enriched data is involved)*
- **Output**: A new request is created in the workflow system with a unique `[Request ID]` and a status of "Submitted".

**Input needed**: Requester's knowledge of the business need.  
**Who fills this**: Any authorized business user.

#### 3.2.2. Stage 2: Data Validation & Enrichment

> *This stage involves automated and manual checks to ensure the submitted data is accurate, complete, and compliant with standards.*

- **Trigger**: Successful submission of a request in Stage 1.
- **Action**: The request is assigned to the designated Data Steward for the respective data domain.
- **Steps**:
    1.  **Automated Validation**: The MDM system automatically runs validation rules:
        - `[Data Type & Format Checks (e.g., date format, numeric)]`
        - `[Completeness Checks (mandatory fields)]`
        - `[Validity Checks (against reference data, e.g., valid country codes)]`
        - `[AI Anomaly Detection]` *(New: AI models flag unusual or inconsistent data patterns)*
    2.  **Manual Review**: The Data Steward reviews the submitted information and any validation errors.
    3.  **Data Enrichment**: The Data Steward enriches the record by adding missing information from internal or approved external sources (e.g., D&B for company data).
    4.  **AI Governance Checkpoint**: If AI involvement is flagged, the AI Ethics Officer or designated reviewer assesses compliance with AI governance policies.
- **Output**: The request status is updated to "Validated" or "Pending Information" (if sent back to the requester for clarification).

**Input needed**: [Data Standards](references/reference-materials.md), [Business Glossary](references/reference-materials.md), external data sources, AI governance policies.  
**Who fills this**: Data Steward, AI Ethics Officer (if applicable).

#### 3.2.3. Stage 3: Duplicate Check & Resolution

> *This critical stage prevents the creation of duplicate master data records, which is a primary cause of data quality issues.*

- **Trigger**: Request status changes to "Validated".
- **Action**: The MDM system performs a matching process against the existing master data repository.
- **Steps**:
    1.  **Fuzzy Matching**: The system uses fuzzy logic and matching algorithms to identify potential duplicates based on key attributes (`[e.g., Name, Address, Tax ID]`).
    2.  **Match Review**: The Data Steward reviews the list of potential duplicates.
    3.  **Resolution**:
        - If **No Duplicates Found**: The request proceeds to the next stage.
        - If **Duplicates Found**: The Data Steward initiates the merge/linkage process. This may require consultation with the Data Owner if the merge has significant business impact.
- **Output**: A clean, de-duplicated record is ready for approval. The request status is updated to "Pending Approval".

**Input needed**: Existing master data repository, matching rules configuration.  
**Who fills this**: MDM System (automated), Data Steward (manual review).

#### 3.2.4. Stage 4: Approval

> *This stage provides the formal sign-off from the accountable party, ensuring that the new or modified data is fit for purpose.*

- **Trigger**: Request status changes to "Pending Approval".
- **Action**: The request is routed to the designated Data Owner for the domain.
- **Steps**:
    1.  **Review**: The Data Owner reviews the complete, validated, and de-duplicated data record.
    2.  **Decision**: The Data Owner makes a decision:
        - **Approve**: The record is approved for creation/update.
        - **Reject**: The record is rejected, and a reason is provided. The workflow is terminated.
        - **Request Changes**: The request is sent back to the Data Steward with comments for rework.
    3.  **AI Ethics Review**: If AI-generated or AI-enriched data is involved, the AI Ethics Officer reviews the approval decision to ensure compliance with ethical standards and regulatory requirements.
- **Output**: The request status is updated to "Approved" or "Rejected".

**Input needed**: Business context and understanding of the data's impact, AI governance considerations.  
**Who fills this**: Data Owner, AI Ethics Officer (if applicable).

#### 3.2.5. Stage 5: Data Creation/Update (Golden Record Management)

> *This is the technical stage where the master data is formally created or updated in the central MDM hub.*

- **Trigger**: Request status changes to "Approved".
- **Action**: The MDM system automatically executes the creation or update.
- **Steps**:
    1.  **Transaction**: The system commits the new/updated record to the master data database.
    2.  **Golden Record Generation**: A unique, persistent enterprise identifier (`[Golden Record ID]`) is generated and assigned to the record.
    3.  **Auditing**: A complete audit trail of the transaction is created, logging the `[Request ID]`, approver, and timestamp.
    4.  **FinOps Monitoring**: Integration with FinOps tools to monitor and optimize resource costs associated with data storage and processing.
- **Output**: The golden record is created or updated in the MDM hub. The request status is updated to "Processed".

**Input needed**: Approved data from the workflow.  
**Who fills this**: MDM System (automated).

#### 3.2.6. Stage 6: Publication & Synchronization

> *This stage ensures that the newly created or updated golden record is propagated to all relevant downstream systems.*

- **Trigger**: Request status changes to "Processed".
- **Action**: The MDM system initiates the data synchronization process.
- **Steps**:
    1.  **Identify Subscribers**: The system identifies all downstream systems that subscribe to this master data domain.
    2.  **Publish**: The golden record data is published to the enterprise service bus (ESB), API gateway, or data mesh/data fabric endpoints.
    3.  **Synchronization**: Downstream systems consume the data and update their local records.
    4.  **Monitoring**: The integration platform monitors the synchronization process for any failures and SLA adherence.
    5.  **MLOps Integration**: If master data is used in AI/ML pipelines, triggers notify MLOps systems for model retraining or validation.
- **Output**: The master data is consistent across all connected systems. The request status is updated to "Completed".

**Input needed**: `KA-06-source-to-target-mapping.md`, system subscription list, AI/ML pipeline integration points.  
**Who fills this**: MDM System (automated), Integration Team (monitoring).

#### 3.2.7. Stage 7: Issue Management (Extended)

> *Ongoing management of issues arising from master data, including corrections, escalations, and continuous improvement.*

- **Trigger**: Detection of data issues via monitoring, user feedback, or audit.
- **Action**: Data Steward logs and manages issues, escalating as needed.
- **Steps**:
    1.  **Issue Logging**: Capture issue details in the Issue Resolution Log.
    2.  **Root Cause Analysis**: Collaborate with Data Governance Analyst and Data Owner.
    3.  **Resolution**: Implement fixes, which may include data correction, process adjustment, or workflow enhancement.
    4.  **Feedback Loop**: Update training materials and workflow documentation.
- **Output**: Resolved issues and updated governance processes.

**Input needed**: Issue reports, audit logs, user feedback.  
**Who fills this**: Data Steward, DG Analyst, MDM Manager.

---

## 4. Example

### 4.1. Scenario Overview

> *This example illustrates the workflow for adding a new supplier, "GlobalRetail Inc.", to the master data repository.*

- **Company**: TechCorp Ltd.
- **Data Domain**: Supplier
- **Requester**: John Doe, Procurement Specialist

### 4.2. Detailed Walkthrough

1.  **Request Initiation**: John Doe fills out the "New Supplier Request" form. He enters "GlobalRetail Inc." as the supplier name, provides their address and contact information, and attaches the signed contract as a supporting document. The system generates Request ID `SR-2026-0208-001`.

2.  **Data Validation & Enrichment**: The request is assigned to Jane Smith, the Supplier Data Steward. The system automatically validates that the phone number is in the correct format and the address fields are complete. Jane then uses TechCorp's D&B subscription to enrich the record with the official legal name ("GlobalRetail, Incorporated"), D-U-N-S number, and corporate hierarchy information. AI anomaly detection flags a discrepancy in the tax ID format, which Jane investigates and corrects. Since AI enrichment was involved, the AI Ethics Officer reviews and approves the data enrichment process.

3.  **Duplicate Check & Resolution**: The MDM system runs a match process. It finds a potential duplicate: a record for "Global Retail" entered two years ago with an inactive status. Jane reviews the two records and determines they are the same entity. She initiates the "Merge" process, marking the old record as a duplicate and carrying over its history to the new, enriched record.

4.  **Approval**: The merged and validated record is routed to Mary Major, the Data Owner for Supplier data. Mary reviews the full record, including the D&B enrichment data and the attached contract. She sees that everything is in order and clicks "Approve". The AI Ethics Officer confirms the approval aligns with AI governance policies.

5.  **Data Creation/Update**: The MDM system automatically creates the new golden record for GlobalRetail, Incorporated and assigns it the persistent Golden Record ID `GR-894321`. FinOps monitoring tools track the resource usage associated with this transaction.

6.  **Publication & Synchronization**: The MDM hub publishes the new supplier record. The ERP system, the Accounts Payable system, and the Procurement platform all receive the new record via the enterprise service bus, ensuring that "GlobalRetail, Incorporated" is represented consistently across all key applications. The MLOps platform is notified to retrain supplier risk models using the updated master data.

7.  **Issue Management**: Two weeks later, a data quality issue is reported regarding the supplier's payment terms. The Data Steward logs the issue, performs root cause analysis, and updates the workflow to include an additional validation step for payment terms in future requests.

### 4.3. Lessons Learned

- Integration of AI validation and ethics review enhances data quality and compliance but requires clear role definitions.
- Automated enrichment accelerates data onboarding but must be monitored for accuracy and bias.
- Close collaboration between Data Stewards, Data Owners, and AI Ethics Officers is essential for effective governance.
- Continuous feedback and issue management loops improve the workflow over time.
- FinOps and MLOps integrations provide operational and cost transparency, supporting sustainable data management.

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Concept | [concepts/data-contracts.md](references/concepts-modern-paradigms.md) |
| Data Mesh Principles | Guide | **guides/modern-architectures/data-mesh-principles.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The workflow is documented using BPMN 2.0.
- [x] Every stage has a clearly defined trigger, action, and output.
- [x] Roles and responsibilities (RASCI) are explicitly defined for each stage.
- [x] The workflow includes automated data validation checks, including AI-powered anomaly detection.
- [x] A mandatory duplicate check and resolution stage is included.
- [x] A formal approval stage by the Data Owner is required, with AI ethics oversight where applicable.
- [x] The workflow generates a complete audit trail for every request.
- [x] Service Level Agreements (SLAs) for each stage are defined and monitored.
- [x] Compliance with relevant regulations (GDPR, HIPAA, CCPA, EU AI Act) is enforced.
- [x] Integration with DataOps, MLOps, and FinOps practices is established.
- [x] The workflow supports multi-cloud and hybrid environments.
- [x] Feedback and issue management mechanisms are embedded for continuous improvement.

### 5.2. Review Checklist

| Area | Question | Finding (Pass/Fail) |
| :--- | :--- | :--- |
| **Efficiency** | Does the workflow minimize manual steps and handoffs through automation and AI integration? | |
| **Effectiveness** | Does the workflow consistently prevent data quality errors and duplicates? | |
| **Clarity** | Is the workflow documentation easy for business users, stewards, and AI governance roles to understand? | |
| **Compliance** | Does the workflow enforce all relevant data policies, standards, and AI governance requirements? | |
| **Scalability** | Can the workflow handle the expected volume of master data requests in a multi-cloud, distributed environment? | |
| **Integration** | Is the workflow seamlessly integrated with the MDM platform, downstream systems, and AI/ML pipelines? | |
| **Governance** | Are roles such as AI Ethics Officer and CAIO properly incorporated into the workflow? | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | Relative Path |
| :--- | :--- |
| MDM Strategy | `templates/templates-KA-10-reference-master-data.md` |
| Data Governance Framework | `templates/templates-KA-01-data-governance.md` |
| Data Standards | `#` |
| Business Glossary | `references/reference-materials.md` |

### 6.2. Consumers (Outputs)

| Output | Relative Path |
| :--- | :--- |
| Issue Resolution Log | `templates/templates-KA-01-data-governance.md` |
| Master Data Audit Report | `templates/templates-KA-10-reference-master-data.md` |
| Data Product Outputs | `references/reference-materials.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| **MDM Platforms** | Informatica MDM, TIBCO EBX, Semarchy xDM, Profisee | Pimcore, OpenMDM | 
| **Workflow Engines** | Camunda, Appian, Pega | Camunda (Community), Flowable, jBPM |
| **Data Quality** | Talend Data Quality, Ataccama, Informatica IDQ | OpenRefine, Apache Griffin |
| **API / Integration** | MuleSoft Anypoint, Boomi, Apigee | Kong, Tyk, Apache Camel |
| **AI Governance & Monitoring** | IBM Watson OpenScale, Microsoft Azure Purview | OpenAI Governance Toolkit (community projects) |
| **FinOps Tools** | Cloudability, Apptio Cloudability | Kubecost, Cloud Custodian |
| **MLOps Platforms** | MLflow, Kubeflow, DataRobot | MLflow (Open Source), Seldon Core |

### 7.2. Automation Opportunities

- **AI-Powered Validation**: Use machine learning models to suggest data corrections and identify anomalies during the validation stage, improving accuracy and reducing manual effort.
- **Automated Enrichment**: Integrate with third-party data providers via API to automatically enrich records with firmographic, geographic, or other relevant data.
- **Intelligent Matching**: Employ advanced machine learning algorithms for more accurate and context-aware duplicate detection, reducing false positives and negatives.
- **Robotic Process Automation (RPA)**: Use RPA bots to automate the initial data entry for requests that originate from unstructured sources like emails or PDFs.
- **AI Ethics Automation**: Implement automated compliance checks for AI governance policies, including bias detection and explainability assessments.
- **FinOps Integration**: Automate cost monitoring and optimization for data storage and processing related to master data management.
- **MLOps Integration**: Automate notifications and triggers for model retraining when master data changes impact AI/ML models.
- **Workflow Orchestration**: Use BPMN engines with event-driven architecture to enable real-time, scalable workflow execution across multi-cloud environments.

---

## 8. References

- **DAMA-DMBOK (2nd Edition)**: Chapter 10, "Reference and Master Data Management"
- **DAMA-DMBOK 3.0 (Upcoming)**: Emphasizes AI governance, data mesh/fabric integration, agentic stewardship, and data products as first-class citizens.
- **Internal**: `templates/templates-KA-01-data-governance.md`
- **Internal**: `references/reference-materials.md`
- **EU AI Act**: Regulatory framework for AI governance compliance.
- **GDPR, HIPAA, CCPA**: Data privacy and protection regulations relevant to master data governance.
- **Data Mesh Principles**: **guides/modern-architectures/data-mesh-principles.md**


---

# Data Survivorship Rules


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
  - [3.2. Survivorship Rule Set: [Master Data Entity Name]](#32-survivorship-rule-set-master-data-entity-name)
  - [3.3. Attribute-Level Survivorship Rules](#33-attribute-level-survivorship-rules)
  - [3.4. Spreadsheet Template](#34-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Survivorship Rule Set: Customer](#42-survivorship-rule-set-customer)
  - [4.3. Attribute-Level Survivorship Rules](#43-attribute-level-survivorship-rules)
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

**Data Survivorship Rules** are a foundational element of Master Data Management (MDM) that codify the logic and decision-making framework for consolidating multiple, often conflicting, data records into a single, authoritative "golden record." These rules systematically resolve discrepancies in attribute values sourced from diverse systems (e.g., CRM, ERP, e-commerce platforms), ensuring that the master data entity reflects the most accurate, trusted, and business-relevant information.

Survivorship rules are essential for maintaining data integrity, enabling consistent reporting, analytics, and operational processes that depend on reliable master data. They also underpin compliance with regulatory requirements by ensuring data accuracy and traceability.

> Data Survivorship Rules codify the decision-making process for building the single version of the truth, transforming data chaos into a trusted, reliable asset.

In the evolving data landscape, survivorship rules must also accommodate modern data architectures such as Data Mesh and Data Fabric, where master data may be federated or distributed. Additionally, with the rise of AI-driven data governance and automation, survivorship logic increasingly incorporates machine learning insights and adaptive rules to enhance accuracy and responsiveness.

### 1.2. Scope

**Global** — Survivorship rules are typically defined at the enterprise level as standardized logic sets for each master data domain (e.g., Customer, Product, Supplier). These rules serve as the authoritative framework applied during the master data consolidation process, which may be executed centrally or in federated environments consistent with Data Mesh principles.

While the rules themselves are global, their application is dynamic and executed per record during data integration, enrichment, and consolidation workflows. They must be flexible enough to support cloud-native deployments, multi-cloud environments, and hybrid architectures.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Data Governance Council approves survivorship rules, ensuring alignment with policies, compliance (e.g., GDPR, EU AI Act), and AI governance frameworks. Data Stewards provide domain expertise and business context. |
| KA-02: Data Architecture | Defines the logical and physical data models that specify master data entities and attributes subject to survivorship rules. Supports modern architectures such as Data Mesh, Data Fabric, and Lakehouse. |
| KA-03: Data Modeling & Design | Provides the schema and attribute definitions that guide the application of survivorship rules at the attribute level. |
| KA-06: Data Integration & Interoperability | Survivorship rules are implemented within ETL/ELT pipelines, data virtualization, and streaming platforms to consolidate master data in real-time or batch modes. |
| KA-10: Reference and Master Data Management | Core knowledge area encompassing survivorship rules, golden record definitions, match-merge logic, and master data lifecycle management. |
| KA-11: Data Quality | Survivorship rules are a critical mechanism for resolving data conflicts, improving accuracy, completeness, and consistency of master data. |
| KA-13: Data Security & Privacy | Ensures survivorship rules comply with data privacy regulations and security policies, especially when handling sensitive master data attributes. |
| KA-14: Artificial Intelligence & Machine Learning | Emerging integration of AI/ML techniques to automate and optimize survivorship decisions, anomaly detection, and exception handling. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | MDM Manager / Chief Data Officer (CDO) | Ultimately accountable for the definition, implementation, governance, and effectiveness of data survivorship rules aligned with enterprise data strategy and compliance mandates. |
| **R (Responsible)** | Data Quality Analyst / Data Scientist | Responsible for analyzing source data, profiling conflicts, drafting survivorship logic, and integrating AI/ML insights where applicable. |
| **S (Supportive)** | Data Integration Specialist / MLOps Engineer | Supports implementation of survivorship rules within data integration pipelines, MDM platforms, and automation frameworks. |
| **C (Consulted)** | Data Steward, Data Owner, AI Ethics Officer | Provide business context, domain expertise, and ethical considerations to ensure survivorship rules reflect operational priorities and AI governance principles. |
| **I (Informed)** | Data Engineer, Data Product Manager | Kept informed of survivorship rules to understand master data creation, support data product development, and ensure alignment with data contracts. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Rule Definition | Data Quality Analyst | Data Steward, Data Owner, AI Ethics Officer | MDM Manager / CDO |
| Rule Implementation | Data Integration Specialist | Data Quality Analyst, MLOps Engineer | MDM Manager / CDO |
| Rule Testing | Data Quality Analyst | Data Steward, Data Product Manager | MDM Manager / CDO |
| Exception Handling | Data Steward | Data Quality Analyst, AI Ethics Officer | MDM Manager / CDO |

---

## 3. Template

> *The following template is used to define data survivorship rules for a specific master data entity. It should be completed for each attribute requiring conflict resolution, incorporating modern governance and architectural considerations.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Data Survivorship Rules: [Master Data Domain] |
| Document ID | MDM-SURV-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [MDM Manager / CDO Name] |
| Approver | [Data Governance Council / AI Governance Board] |

### 3.2. Survivorship Rule Set: [Master Data Entity Name]

> *Define the overall survivorship strategy for this entity. This includes default rules, source system precedence, and any AI-assisted decision logic.*

**Default Strategy**: [e.g., Source system precedence with AI-enhanced confidence scoring. If no attribute-specific rule exists, the value from the most trusted source system or highest confidence score will be used.]

Considerations for modern environments:
- Incorporate data product ownership and data contracts to define source trustworthiness.
- Leverage AI/ML models to detect anomalies or suggest rule adjustments.
- Align with Data Mesh principles by respecting domain boundaries and federated stewardship.
- Ensure compliance with regulations such as the EU AI Act and GDPR.

### 3.3. Attribute-Level Survivorship Rules

> *For each attribute requiring specific survivorship logic, provide detailed rules including rationale, source precedence, and exception handling.*

**Input needed**: Data profiling results, source system metadata, business input from Data Stewards, AI governance guidelines.

**Who fills this**: Data Quality Analyst, Data Steward, with AI Ethics Officer consultation as needed.

| Attribute Name | Rule Logic | Rationale | Source System Precedence | Exception Handling |
| :--- | :--- | :--- | :--- | :--- |
| [e.g., CustomerEmail] | **Most Recent**: Use the value with the latest timestamp or highest AI confidence score. | The most recently updated email is most likely to be correct; AI models may flag suspicious changes. | 1. CRM (Salesforce)<br>2. E-commerce (Magento)<br>3. ERP (SAP) | If timestamps are identical or confidence scores are low, use the value from the highest precedence source. If conflict persists, flag for manual review by a Data Steward and AI Ethics Officer. |
| [e.g., CustomerPhone] | **Most Frequent**: Use the value appearing most frequently across sources, weighted by source trust score. | Frequent occurrence indicates higher accuracy; weighting accounts for source reliability. | N/A | In case of ties or low confidence, escalate to Data Steward for verification. |
| [e.g., AddressLine1] | **Source Precedence with Validation**: Use the value from the designated source of truth, validated by third-party services. | Billing system is most reliable; validation ensures deliverability and compliance. | 1. Billing System<br>2. CRM<br>3. E-commerce | If primary source value is null, invalid, or unvalidated, fallback to next source. If no valid value, escalate to Data Steward. |
| [e.g., ProductName] | **Aggregation and Enrichment**: Concatenate values from multiple sources, enriched by AI-based normalization. | Different systems may store complementary product details; AI ensures consistency and user-friendly formatting. | N/A | Data Steward reviews aggregated names; AI Ethics Officer reviews for bias or inappropriate content. |
| [e.g., CreditLimit] | **Richest Data**: Use the value with the most complete associated metadata (e.g., credit score, risk rating). | Richer data provides better decision support; AI models may enhance richness scoring. | N/A | If richness cannot be determined, default to highest credit limit; flag for periodic review. |

---

### 3.4. Spreadsheet Template

> For operational efficiency, use the spreadsheet version of this deliverable optimized for collaboration, filtering, and bulk editing:

**[Download KA-10_data-survivorship-rules.xlsx](#)**

The spreadsheet complements this Markdown template by providing a structured, tabular format for managing large volumes of survivorship rules. It supports integration with data governance platforms and automation tools.

---

## 4. Example

> *This section illustrates a practical application of survivorship rules for a fictional enterprise, GlobalRetail Inc., incorporating modern governance and AI considerations.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Data Survivorship Rules: Customer Master |
| Document ID | MDM-SURV-CUST-001 |
| Version | 1.2 |
| Effective Date | 2025-10-01 |
| Owner | John Doe, MDM Manager |
| Approver | GlobalRetail Data Governance Council and AI Governance Board |

### 4.2. Survivorship Rule Set: Customer

**Default Strategy**: Source system precedence augmented with AI confidence scoring. The default order of precedence is: 1. Salesforce (CRM), 2. SAP (ERP), 3. Magento (E-commerce). AI models analyze data freshness, completeness, and anomaly detection to adjust survivorship decisions dynamically.

### 4.3. Attribute-Level Survivorship Rules

| Attribute Name | Rule Logic | Rationale | Source System Precedence | Exception Handling |
| :--- | :--- | :--- | :--- | :--- |
| EmailAddress | **Most Recent with AI Confidence**: Use the value with the latest `last_updated_timestamp` and highest AI confidence score. | Customer emails change frequently; AI models flag suspicious or invalid emails. | 1. Magento<br>2. Salesforce<br>3. SAP | If timestamps and confidence scores are identical, prefer Magento as customer-provided data. Persisting conflicts trigger stewardship tasks with AI Ethics Officer review. |
| PhoneNumber | **Source Precedence**: Use the value from the source with the highest trust score for phone numbers, verified by AI validation. | Salesforce is primary for sales outreach; AI validates format and usage patterns. | 1. Salesforce<br>2. SAP<br>3. Magento | If Salesforce phone is null or invalid, fallback to SAP, then Magento. Null across all results in null phone number in master record. |
| MailingAddress | **Richest and Validated**: Use address validated by third-party services and AI verification. | Validated addresses reduce delivery errors and comply with privacy regulations. | N/A | If no validated address exists, use SAP billing address. Incomplete or conflicting data escalates to Data Steward and AI Ethics Officer. |
| CompanyName | **Most Frequent with Normalization**: Use the company name appearing most often, normalized by AI to correct spelling and abbreviations. | Corrects minor variations and ensures consistency across systems. | N/A | Ties resolved by preferring Salesforce value; AI flags unusual variations for review. |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Match-Merge Rules | Deliverable | [templates/templates-KA-10-reference-master-data.md](templates/templates-KA-10-reference-master-data.md) |
| Data Governance Roles and Responsibilities | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| AI Governance Framework | Guide | **templates/strategy-assessment-governance.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] Each survivorship rule is clearly defined, unambiguous, and aligned with business priorities.
- [x] A clear rationale is provided for each rule, including business and technical justification.
- [x] Exception handling processes are defined, actionable, and incorporate escalation paths including AI Ethics oversight.
- [x] Rules have been reviewed and approved by Data Stewards, Data Owners, AI Ethics Officers, and relevant governance bodies.
- [x] Rules have been tested with representative sample data, including edge cases and AI model validation, to ensure expected results.
- [x] Survivorship rules comply with applicable regulations such as GDPR, HIPAA, CCPA, and the EU AI Act.
- [x] Rules support modern data architectures and integrate with data contracts and data product frameworks.

### 5.2. Review Checklist

| Criteria | Reviewer Role | Result (Pass/Fail) |
| :--- | :--- | :--- |
| Rule logic aligns with business priorities and data governance policies. | Data Owner | Pass |
| Rules are technically feasible and scalable within integration and MDM platforms. | Data Integration Specialist | Pass |
| Exception handling processes are clear, actionable, and include AI governance considerations. | Data Steward, AI Ethics Officer | Pass |
| Rules do not result in loss of critical information or introduce bias. | Data Quality Analyst | Pass |
| The overall impact on the golden record enhances data trustworthiness and usability. | MDM Manager / CDO | Pass |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | File Path |
| :--- | :--- |
| Golden Record Definition | `templates/templates-KA-10-reference-master-data.md` |
| Match-Merge Rules | `templates/templates-KA-10-reference-master-data.md` |
| Data Profiling Reports | `templates/templates-KA-11-data-quality.md` |

### 6.2. Consumers (Outputs)

| Output | File Path |
| :--- | :--- |
| Data Integration Rules | `templates/templates-KA-10-reference-master-data.md` |
| Data Architecture | `knowledge-areas/KA-02-data-architecture.md` |
| Data Security & Privacy | `knowledge-areas/KA-05-data-security.md` |
| AI Governance Policies | `templates/strategy-assessment-governance.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| MDM Platforms | Informatica MDM, TIBCO EBX, Semarchy xDM, IBM InfoSphere MDM | Pimcore, AtroPIM |
| Data Integration Tools | Talend, Informatica PowerCenter, Fivetran, Microsoft Azure Data Factory | Apache NiFi, Airbyte |
| Data Quality Tools | Ataccama, Trillium, Talend Data Quality, Collibra | OpenRefine, Great Expectations |
| AI/ML Platforms for Data Governance | DataRobot, H2O.ai, IBM Watson OpenScale | TensorFlow, MLflow |
| Address Validation Services | Experian, Loqate, Melissa | OpenAddresses |

### 7.2. Automation Opportunities

- **Automated Rule Execution**: Survivorship rules should be fully automated within MDM platforms or data integration workflows, supporting real-time and batch consolidation with minimal manual intervention.
- **AI-Enhanced Decisioning**: Incorporate AI/ML models to dynamically adjust survivorship logic based on data quality metrics, anomaly detection, and evolving business rules.
- **Automated Exception Queuing**: Exceptions triggered by survivorship rules should automatically generate stewardship tasks, routed to appropriate Data Stewards and AI Ethics Officers for review.
- **Continuous Profiling and Monitoring**: Use data profiling tools integrated with AI to continuously monitor source data quality, detect emerging conflicts, and recommend rule updates.
- **Integration with Data Contracts and Data Products**: Automate validation of source system trustworthiness and data freshness based on contractual SLAs and data product health metrics.
- **Cloud-Native and Multi-Cloud Support**: Leverage cloud-native automation frameworks and orchestration tools (e.g., Kubernetes, Apache Airflow) to scale survivorship rule execution across hybrid environments.

---

## 8. References

- **DAMA-DMBOK2**: Chapter 10, "Reference and Master Data Management"
- **DAMA-DMBOK3.0 (Upcoming)**: Emphasizes AI governance, Data Mesh/Fabric integration, and cloud-native master data management practices (expected June 2025)
- **Internal**: `templates/templates-KA-01-data-governance.md`
- **EU AI Act Compliance Guide**: `#`
- **Data Product Outputs Reference**: `references/reference-materials.md`
- **AI Governance Framework**: `templates/strategy-assessment-governance.md`
