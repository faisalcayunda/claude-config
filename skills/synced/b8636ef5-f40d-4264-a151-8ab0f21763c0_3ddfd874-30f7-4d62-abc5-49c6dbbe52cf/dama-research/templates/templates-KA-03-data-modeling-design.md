<!-- NAV-TOC -->
## Sections in This File

This file contains **11 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 22 | Modeling Standards |
| 386 | Naming Conventions |
| 726 | Conceptual Data Model |
| 1057 | Logical Data Model |
| 1397 | Physical Data Model |
| 1824 | Entity Definitions |
| 2193 | Attribute Definitions |
| 2642 | Relationship Documentation |
| 2971 | Model Change Log |
| 3303 | Dimensional Data Model |
| 3669 | Model Review and Validation Report |

## Sections in This File

This file contains **11 sections**. Use `view_range` with the line numbers below to jump to a specific section.

| Line | Section |
|:---|:---|
| 1 | Modeling Standards |
| 365 | Naming Conventions |
| 705 | Conceptual Data Model |
| 1036 | Logical Data Model |
| 1376 | Physical Data Model |
| 1803 | Entity Definitions |
| 2172 | Attribute Definitions |
| 2621 | Relationship Documentation |
| 2950 | Model Change Log |
| 3282 | Dimensional Data Model |
| 3648 | Model Review and Validation Report |

---

# Modeling Standards


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
  - [3.2. Introduction](#32-introduction)
  - [3.3. Modeling Levels](#33-modeling-levels)
  - [3.4. Diagramming and Notation Standards](#34-diagramming-and-notation-standards)
  - [3.5. Naming Conventions](#35-naming-conventions)
  - [3.6. Data Typing Standards](#36-data-typing-standards)
  - [3.7. Model Management and Versioning](#37-model-management-and-versioning)
- [4. Example](#4-example)
  - [4.1. Scenario: Customer Order Model](#41-scenario-customer-order-model)
  - [4.2. Conceptual Data Model (CDM) Example](#42-conceptual-data-model-cdm-example)
  - [4.3. Logical Data Model (LDM) Example](#43-logical-data-model-ldm-example)
  - [4.4. Physical Data Model (PDM) Example (for PostgreSQL)](#44-physical-data-model-pdm-example-for-postgresql)
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

The **Modeling Standards** document provides a comprehensive set of rules, guidelines, and best practices for creating, documenting, and managing data models across the organization. These standards ensure that data models are consistent, understandable, and of high quality, regardless of who creates them. The primary purpose of these standards is to improve communication between business and technical stakeholders, reduce ambiguity in data definitions, accelerate development, and ensure that data structures are aligned with both business requirements and architectural principles.

In the evolving data management landscape, these standards also incorporate considerations for modern data architectures such as Data Mesh and Data Fabric, cloud-native implementations, and AI governance frameworks. This ensures that data models not only serve traditional transactional and analytical needs but also support emerging capabilities like data products, data contracts, and operationalized AI systems.

> This document answers the question: *"How must we build and document our data models to ensure they are clear, consistent, and fit for purpose?"*

### 1.2. Scope

**Global** — These Modeling Standards apply to all data modeling activities across the enterprise, including conceptual, logical, and physical data models for transactional systems, data warehouses, data marts, analytical platforms, and AI/ML pipelines. They are mandatory for all projects that create or modify data structures and data products.

The standards also address compliance with relevant regulations such as GDPR, HIPAA, CCPA, and the EU AI Act, ensuring that data models incorporate necessary privacy, security, and ethical considerations. Furthermore, they support agentic data stewardship practices and integration with DataOps, MLOps, and FinOps processes.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The standards are a key artifact of data governance, enforcing policies and rules at the design stage. The Business Glossary (KA-01) is a primary input for entity and attribute naming and ensures alignment with data governance and AI governance frameworks. |
| KA-02: Data Architecture | Modeling standards must align with the Enterprise Data Model and architectural blueprints to ensure models fit within the overall data landscape, including modern architectures like Data Mesh, Data Fabric, and Lakehouse patterns. |
| KA-09: Metadata Management | Data models are a critical source of metadata. These standards ensure that the metadata captured in models is consistent, richly annotated, and can be effectively managed in a metadata repository supporting lineage, impact analysis, and AI model explainability. |
| KA-11: Data Quality | High-quality models are a prerequisite for high-quality data. The standards enforce rules (e.g., data types, constraints) that prevent data quality issues at the source and support continuous data quality monitoring integrated with DataOps and MLOps pipelines. |
| KA-12: Data Security and Privacy | Modeling standards incorporate security and privacy requirements, ensuring that sensitive data elements are properly classified, masked, or encrypted as per compliance mandates and AI ethical guidelines. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately answerable for the definition, maintenance, enforcement, and continuous improvement of the modeling standards, ensuring alignment with enterprise strategy and regulatory requirements. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Drafts, updates, and promotes the modeling standards. Provides training and guidance to other teams. Ensures standards incorporate modern data management practices including AI governance and cloud-native architectures. |
| **S (Supportive)** | Data Architect (D-Arch) | Provides strategic input to ensure standards align with the enterprise architecture, long-term technology roadmap, and emerging trends such as Data Mesh and Data Fabric. Supports integration with AI and analytics platforms. |
| **C (Consulted)** | Data Governance Manager (DG Mgr), AI Ethics Officer | Consulted to ensure standards are consistent with data governance policies, AI governance frameworks, business glossary, and ethical guidelines. |
| **I (Informed)** | Data Engineer (D-Eng), Database Administrator (DBA), MLOps Engineer | Informed of the standards as they are the primary implementers and consumers of the physical data models and AI operationalization. |

### 2.2. Section-Level RASCI

| Standard Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Conceptual Modeling Standards | D-Modeler | D-Arch, Business Analyst | DE Mgr |
| Logical Modeling Standards | D-Modeler | D-Arch, DG Mgr, AI Ethics Officer | DE Mgr |
| Physical Modeling Standards | D-Modeler | DBA, D-Eng, MLOps Engineer | DE Mgr |
| Naming Conventions | D-Modeler | DG Mgr | DE Mgr |
| Model Review Process | D-Modeler | D-Arch | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating and documenting Modeling Standards. This template should be used as the single source of truth for all data modeling practices.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | [Organization Name] Data Modeling Standards |
| Document ID | STD-MOD-001 |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Engineering Manager] |

### 3.2. Introduction

> *Provide a brief overview of the purpose, scope, and intended audience for the modeling standards. Explain why adherence to these standards is important for the organization.*

[Insert Introduction]

These standards are designed to ensure that data models are consistent, reusable, and aligned with enterprise data governance and architecture. They facilitate collaboration across business, data science, engineering, and compliance teams, supporting the creation of trusted data products and enabling AI/ML initiatives. Adherence to these standards reduces risks related to data quality, security, and regulatory compliance.

### 3.3. Modeling Levels

> *Define the different levels of data models used in the organization and the purpose of each. This typically includes Conceptual, Logical, and Physical models.*

#### 3.3.1. Conceptual Data Model (CDM)

> *Describe the purpose of the CDM (high-level business concepts). Specify the required components (e.g., key business entities, relationships) and the approved notation (e.g., simple block diagrams, IDEF1X).*

- **Purpose**: To represent the business perspective of data, independent of technology, capturing key business entities, their high-level relationships, and constraints. Supports stakeholder alignment and initial requirements gathering.
- **Components**: Major business entities, high-level relationships, business rules, and key attributes that define the scope of the domain.
- **Notation**: Barker, Chen, UML Class Diagrams, or simple block diagrams as approved by the enterprise architecture team.

#### 3.3.2. Logical Data Model (LDM)

> *Describe the purpose of the LDM (detailed business rules). Specify required components (entities, attributes, primary keys, foreign keys, relationships, cardinality) and notation. Mandate that all entities and attributes must be defined.*

- **Purpose**: To provide a detailed representation of business entities, attributes, and relationships, serving as the blueprint for the physical model and supporting data quality and governance requirements.
- **Components**: All entities, attributes, primary keys, alternate keys, foreign keys, relationships with full cardinality and optionality, business rules, and data classifications.
- **Normalization**: All logical models must be in at least Third Normal Form (3NF), unless an exception is documented and approved for performance or architectural reasons.
- **Additional Considerations**: Logical models should incorporate metadata annotations supporting AI explainability, data lineage, and compliance tagging.

#### 3.3.3. Physical Data Model (PDM)

> *Describe the purpose of the PDM (database-specific implementation). Specify required components (tables, columns, data types, constraints, indexes) and how it should be derived from the LDM. Address denormalization rules.*

- **Purpose**: To represent the database-specific implementation of the logical model, optimized for performance, storage, and platform-specific features.
- **Components**: Tables, columns, data types, constraints (primary key, foreign key, unique, check), indexes, partitions, and storage parameters.
- **Denormalization**: Denormalization is only permitted for performance reasons and must be explicitly documented and approved by the Data Architect. Denormalized structures must maintain data integrity and be reconciled with upstream logical models.
- **Cloud-Native and Multi-Cloud**: Physical models must consider cloud platform capabilities (e.g., serverless databases, data lake tables) and support multi-cloud or hybrid deployments where applicable.

### 3.4. Diagramming and Notation Standards

> *Specify the mandatory notation to be used for each model type to ensure consistency. Include visual examples.*

- **Standard Notation**: Information Engineering (IE) / Crow's Foot Notation is the default for logical and physical models. Conceptual models may use UML or simplified block diagrams.
- **Layout Rules**: Parent entities should be placed above child entities. Lines should not cross to maintain clarity. Use consistent color coding to denote entity types, data sensitivity, or ownership.
- **Accessibility**: Diagrams should be created using tools that support accessibility features and export to standard formats (PDF, SVG) for broad consumption.
- **AI Governance**: Diagrams should include annotations or layers indicating data lineage, stewardship, and AI model dependencies where applicable.

### 3.5. Naming Conventions

> *Reference the separate Naming Conventions document. Provide a summary of key principles here.*

- **Reference**: See the [Naming Conventions](./02-naming-conventions.md) document for full details.
- **Entity/Table Naming**: Singular nouns, PascalCase (e.g., `CustomerAccount`), avoiding abbreviations unless standardized.
- **Attribute/Column Naming**: camelCase without special characters (e.g., `firstName`), with prefixes or suffixes to indicate data type or sensitivity where appropriate.
- **Consistency**: Names must align with the Business Glossary (KA-01) and include metadata tags for data classification and AI governance.
- **Avoidance of Reserved Words**: Names must avoid reserved keywords of target database platforms and scripting languages used in data pipelines.

### 3.6. Data Typing Standards

> *Provide a list of approved standard data types and their usage guidelines for logical and physical models. This ensures consistency and prevents data type mismatches.*

| Logical Type | Physical Type (PostgreSQL) | Physical Type (Oracle) | Usage Guideline |
| :--- | :--- | :--- | :--- |
| Text(n) | VARCHAR(n) | VARCHAR2(n) | For variable-length strings. Use appropriate length limits based on business requirements. |
| Integer | INTEGER | NUMBER(10) | For whole numbers. Use appropriate size to optimize storage. |
| Decimal(p,s) | NUMERIC(p,s) | NUMBER(p,s) | For fixed-point numbers, e.g., monetary values. Precision and scale must be defined explicitly. |
| DateTime | TIMESTAMP | DATE | For date and time values. Use timezone-aware types where applicable. |
| Boolean | BOOLEAN | CHAR(1) CHECK (in ('Y','N')) | For true/false values. Use standard representations consistent across platforms. |
| UUID | UUID | RAW(16) | For globally unique identifiers, especially in distributed systems and Data Mesh environments. |
| JSON / JSONB | JSONB | CLOB / JSON | For semi-structured data. Use judiciously and ensure indexing strategies are defined. |

### 3.7. Model Management and Versioning

> *Define the process for storing, sharing, and versioning data models. Specify the central repository and versioning scheme.*

- **Repository**: All data models must be stored and versioned in the Erwin ModelMart repository or an approved enterprise metadata repository that supports collaboration, lineage, and impact analysis.
- **Versioning**: Use semantic versioning (Major.Minor.Patch) for all model changes. Major versions indicate breaking changes, minor versions add features, and patches fix errors or clarifications.
- **Change Management**: All changes must be reviewed and approved according to the model review process (Section 5). Change logs must be maintained and linked to relevant project documentation.
- **Integration**: Model repositories should integrate with CI/CD pipelines, DataOps, and MLOps tools to enable automated validation and deployment of data models and related artifacts.
- **Data Contracts and Products**: Models that define data products or data contracts must include versioning metadata and support backward compatibility where feasible.

---

## 4. Example

> *This section provides a concrete example of applying the modeling standards to a fictional project at GlobalRetail Inc.*

### 4.1. Scenario: Customer Order Model

This example shows the development of a data model for managing customer orders, supporting both transactional processing and analytical reporting, while ensuring compliance with data governance and AI ethics policies.

### 4.2. Conceptual Data Model (CDM) Example

- **Entities**: `Customer`, `Order`, `Product`
- **Relationships**:
  - A `Customer` can place many `Orders`.
  - An `Order` contains many `Products`.

(A simple diagram would be included here showing three boxes connected by lines, annotated with cardinality and business rules)

### 4.3. Logical Data Model (LDM) Example

**Entity: Customer**
- `customerID` (PK)
- `firstName`
- `lastName`
- `emailAddress`
- `customerStatus` (e.g., Active, Inactive)
- `consentFlag` (Boolean, for GDPR compliance)

**Entity: Order**
- `orderID` (PK)
- `customerID` (FK)
- `orderDate`
- `shippingAddress`
- `orderStatus`

**Entity: OrderItem**
- `orderItemID` (PK)
- `orderID` (FK)
- `productID` (FK)
- `quantity`
- `price`

**Entity: Product**
- `productID` (PK)
- `productName`
- `unitPrice`
- `productCategory`

### 4.4. Physical Data Model (PDM) Example (for PostgreSQL)

**Table: Customer**
- `customer_id` INTEGER PRIMARY KEY
- `first_name` VARCHAR(50) NOT NULL
- `last_name` VARCHAR(50) NOT NULL
- `email_address` VARCHAR(100) UNIQUE NOT NULL
- `customer_status` VARCHAR(20) NOT NULL DEFAULT 'Active'
- `consent_flag` BOOLEAN NOT NULL DEFAULT TRUE

**Table: Order**
- `order_id` INTEGER PRIMARY KEY
- `customer_id` INTEGER NOT NULL REFERENCES Customer(customer_id)
- `order_date` TIMESTAMP NOT NULL
- `shipping_address` VARCHAR(255) NOT NULL
- `order_status` VARCHAR(20) NOT NULL DEFAULT 'Pending'

**Table: OrderItem**
- `order_item_id` INTEGER PRIMARY KEY
- `order_id` INTEGER NOT NULL REFERENCES `Order`(order_id)
- `product_id` INTEGER NOT NULL REFERENCES Product(product_id)
- `quantity` INTEGER NOT NULL CHECK (quantity > 0)
- `price` NUMERIC(10, 2) NOT NULL

**Table: Product**
- `product_id` INTEGER PRIMARY KEY
- `product_name` VARCHAR(100) NOT NULL
- `unit_price` NUMERIC(10, 2) NOT NULL
- `product_category` VARCHAR(50)

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Concept | [data-contracts.md](references/concepts-modern-paradigms.md) |
| AI Governance | Knowledge Area | KA-XX-ai-governance.md |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The model adheres to the specified naming conventions.
- [ ] All entities and attributes have clear, concise, and unambiguous definitions in the model or business glossary.
- [ ] The correct diagramming notation has been used.
- [ ] The logical model is in at least 3rd Normal Form (3NF), unless an exception is documented and approved.
- [ ] All relationships have correctly defined cardinality and optionality.
- [ ] Standard data types have been used for all attributes/columns.
- [ ] Data sensitivity and classification metadata are included where applicable.
- [ ] The model supports compliance requirements such as GDPR and the EU AI Act.
- [ ] The model has been reviewed and approved by the required stakeholders, including AI Ethics Officer when relevant.
- [ ] Versioning and change history are properly documented.

### 5.2. Review Checklist

| Category | Checkpoint | Status (Pass/Fail) |
| :--- | :--- | :--- |
| **Completeness** | Does the model meet all business requirements? | |
| **Clarity** | Are entity and attribute names understandable to business users? | |
| **Consistency** | Does the model use standard definitions from the Business Glossary? | |
| **Accuracy** | Does the model correctly represent the business rules? | |
| **Compliance** | Does the model adhere to all documented modeling standards and regulatory requirements? | |
| **Security & Privacy** | Are sensitive data elements properly classified and protected? | |
| **AI Governance** | Are AI-related data and model dependencies properly annotated and governed? | |
| **Version Control** | Is the model versioned and change history documented? | |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship |
| :--- | :--- |
| [Data Standards](templates/templates-KA-01-data-governance.md) | Provides the foundational data element standards that modeling must adhere to. |
| **Business Glossary** | Provides authoritative definitions for entities and attributes used in models. |
| **Data Architecture Blueprint** | Provides architectural context and constraints for modeling efforts. |

### 6.2. Consumers

| Output | Relationship |
| :--- | :--- |
| [Naming Conventions](./02-naming-conventions.md) | This document is a direct extension of the modeling standards, detailing specific naming rules. |
| [Conceptual Data Model](./03-conceptual-data-model.md) | This output is an instance of a model created following these standards. |
| [Model Review and Validation Report](./11-model-review-validation-report.md) | This report is generated during the review process defined in these standards. |
| Data Product Specification | Uses models as inputs to define data products and contracts. |
| AI Model Documentation | Leverages data models for feature and data lineage documentation. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling** | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, SqlDBM | OpenModelSphere, Draw.io (for CDMs), dbt (for modeling as code) |
| **Model Repository** | Erwin ModelMart, ER/Studio Team Server, Collibra | Git (with a structured folder system), Apache Atlas |
| **Validation** | Custom scripts, linters, data quality platforms | SQLFluff, Great Expectations, OpenLineage |

### 7.2. Automation Opportunities

- **Model Validation**: Scripts can be developed to automatically parse model files (e.g., XML exports) to check for compliance with naming conventions, data type standards, and other rules. Integration with CI/CD pipelines enables continuous validation.
- **Model Generation**: Physical data models can be automatically generated from logical models for different database platforms using the forward-engineering features of modeling tools, reducing manual errors.
- **Documentation Generation**: Reports and documentation for data models can be automatically generated from the metadata stored in the modeling tool, ensuring up-to-date and consistent documentation.
- **Metadata Synchronization**: Automated synchronization between data models and metadata repositories supports lineage, impact analysis, and AI explainability.
- **Data Contract Enforcement**: Automation can validate that data models comply with defined data contracts and service-level agreements (SLAs) in Data Mesh environments.
- **AI Governance Integration**: Automated tagging and annotation of models to support AI governance workflows, including bias detection and model audit trails.

---

## 8. References

- **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 5)
- **[2]** DAMA International. *DAMA-DMBOK 3.0 (Draft)*. Community-driven update launched June 2025. [https://dama.org/dmbok3](https://dama.org/dmbok3)
- **[3]** [Internal Link to Role Definitions Document](references/reference-materials.md)
- **[4]** [Internal Link to Naming Conventions Document](./02-naming-conventions.md)
- **[5]** **Internal Link to Data Governance Knowledge Area**
- **[6]** Internal Link to AI Governance Knowledge Area
- **[7]** European Commission. *Proposal for a Regulation laying down harmonized rules on artificial intelligence (EU AI Act)*, 2021.
- **[8]** Cloud Native Computing Foundation. *Cloud Native Landscape*. [https://landscape.cncf.io/](https://landscape.cncf.io/)


---

# Naming Conventions


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. General Naming Rules](#31-general-naming-rules)
  - [3.2. Abbreviation and Acronym Dictionary](#32-abbreviation-and-acronym-dictionary)
  - [3.3. Logical Naming Conventions](#33-logical-naming-conventions)
  - [3.4. Physical Naming Conventions](#34-physical-naming-conventions)
- [4. Example](#4-example)
  - [4.1. Abbreviation Dictionary (Excerpt)](#41-abbreviation-dictionary-excerpt)
  - [4.2. Logical Model Example](#42-logical-model-example)
  - [4.3. Physical Model Example (Oracle Database)](#43-physical-model-example-oracle-database)
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

The **Naming Conventions** document is a global standard that establishes clear, consistent, and unambiguous rules for naming data assets across the enterprise. These assets include, but are not limited to, databases, schemas, tables, columns, views, indexes, procedures, and files. The primary purpose of this document is to ensure that data assets are easily identifiable, understandable, and manageable, which in turn improves data quality, facilitates data integration, and enhances communication between technical and business teams.

> A well-defined naming convention is the grammatical foundation of a data-literate organization. It transforms cryptic technical identifiers into a shared business vocabulary.

In the evolving landscape of data management, naming conventions play a critical role in supporting modern architectures such as Data Mesh and Data Fabric, enabling seamless interoperability and discoverability across distributed data products. Furthermore, with the increasing adoption of AI and machine learning, consistent naming supports AI governance frameworks by ensuring traceability and auditability of data assets used in model training and inference.

### 1.2. Scope

**Global** — The Naming Conventions standard applies to all data and database development activities across the entire organization. It is a foundational document that governs the creation of all new data assets and provides a guideline for the remediation of existing ones. While specific technologies might have minor variations, the core principles and structures defined herein are universal.

This standard encompasses logical and physical data models, metadata artifacts, and extends to data contracts and data products as first-class entities in the enterprise data ecosystem. It supports cloud-native environments, multi-cloud deployments, and hybrid architectures by providing adaptable yet consistent naming frameworks.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The Naming Conventions are a key policy enforced by the Data Governance program to ensure data consistency, quality, and compliance with regulations such as GDPR, HIPAA, CCPA, and the EU AI Act. |
| KA-02: Data Architecture | Naming conventions are a fundamental component of the data architecture, ensuring that the structure of the data landscape is logical, understandable, and aligned with modern architectural paradigms like Data Mesh and Lakehouse. |
| KA-06: Data Integration and Interoperability | Standardized names simplify the process of mapping and integrating data from different sources, enabling effective DataOps and FinOps practices. |
| KA-09: Metadata Management | Consistent naming is critical for the effective management of metadata, as it allows for the automated discovery, cataloging, and lineage tracking of data assets, which supports AI governance and MLOps workflows. |
| KA-11: Data Quality Management | Naming conventions contribute to data quality by reducing ambiguity and enhancing clarity, which facilitates data validation and error detection. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Modeling/Design Manager (DE Mgr) | Ultimately answerable for the definition, approval, and maintenance of the enterprise-wide Naming Conventions. Ensures alignment with enterprise data governance and architecture strategies. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Drafts, refines, and socializes the naming convention standards, ensuring they are practical, comprehensive, and adaptable to emerging technologies and methodologies. |
| **S (Supportive)** | Data Architect (D-Arch), Database Administrator (DBA), AI Ethics Officer | Provide expert input on technical constraints, platform-specific requirements, AI governance considerations, and best practices for physical naming and ethical data use. |
| **C (Consulted)** | Data Governance Manager (DG Mgr), Metadata Manager (Meta Mgr), Data Product Manager | Consulted to ensure alignment with the overall data governance framework, metadata management strategy, and data product lifecycle requirements. |
| **I (Informed)** | Data Engineer (D-Eng), MLOps Engineer | Informed of the standards to ensure all data pipeline, integration, and model operationalization development adheres to the conventions. |

### 2.2. Section-Level RASCI

| Convention Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| General Naming Rules | D-Modeler | D-Arch, DBA, AI Ethics Officer | DE Mgr |
| Logical Naming Conventions | D-Modeler | Business Analysts, Data Stewards, Data Product Manager | DE Mgr |
| Physical Naming Conventions | D-Modeler | DBA, D-Arch | DE Mgr |
| Abbreviation and Acronym Dictionary | D-Modeler | All Stakeholders | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Naming Conventions document. This template provides a comprehensive structure for defining naming rules for all types of data assets.*

### 3.1. General Naming Rules

> *This section defines the universal principles that apply to all data asset names, regardless of type or platform. These are the foundational rules of your naming grammar.*

- **Case**: [e.g., All names must be in UPPERCASE / lowercase / PascalCase / camelCase.]  
  *Considerations*: Consistency in case usage facilitates automated parsing and integration across heterogeneous systems, including cloud-native platforms and AI pipelines.

- **Separators**: [e.g., Words in names must be separated by an underscore (_). Spaces and other special characters are not permitted.]  
  *Rationale*: Using standard separators enhances readability and compatibility with scripting and querying languages.

- **Length**: [e.g., Names should be concise but descriptive. Avoid overly long names, but do not sacrifice clarity for brevity. Maximum length for any object name is [XX] characters.]  
  *Note*: Length limits may vary by platform; ensure compliance with the most restrictive system in use.

- **Reserved Words**: [e.g., Avoid using SQL reserved words (e.g., SELECT, TABLE, INDEX) or platform-specific keywords as object names.]  
  *Additional*: Include reserved terms from AI frameworks and cloud services to prevent conflicts.

- **Clarity**: [e.g., Names must be in English and should be self-explanatory to a non-technical business user where possible.]  
  *Best Practice*: Avoid ambiguous abbreviations; use terms aligned with the enterprise business glossary.

- **Uniqueness**: Ensure names are unique within their scope to prevent confusion and enable precise data lineage and impact analysis.

- **Versioning**: If applicable, include version identifiers in names to support data product lifecycle management and model version tracking.

### 3.2. Abbreviation and Acronym Dictionary

> *A centralized, approved list of abbreviations and acronyms is essential for consistency. This section should provide a link to or include the official dictionary.*

- **Source of Truth**: [e.g., The official list of approved abbreviations and acronyms is maintained at [Link to Confluence/SharePoint page]].  
  *Governance*: The dictionary is maintained by the Data Governance team with periodic reviews to incorporate new terms arising from evolving business and technology needs.

- **Request Process**: [e.g., To request a new abbreviation, submit a ticket to the Data Governance team.]  
  *Review Criteria*: Requests are evaluated for clarity, necessity, and alignment with existing standards.

| Full Word | Abbreviation | Description |
| :--- | :--- | :--- |
| [e.g., Number] | [e.g., NUM] | [e.g., Used for numeric identifiers] |
| [e.g., Amount] | [e.g., AMT] | [e.g., Used for monetary values] |
| [e.g., Indicator] | [e.g., IND] | [e.g., Used for boolean flags (Y/N)] |

### 3.3. Logical Naming Conventions

> *Define the naming standards for the logical data model. These names should be business-friendly and independent of any physical implementation.*

Logical names serve as the bridge between business concepts and technical implementation, supporting data literacy and governance.

#### 3.3.1. Entity Naming

- **Format**: `[Entity Name]`  
- **Guidance**: Use singular nouns that represent a person, place, thing, or concept. Example: `CUSTOMER`, `PRODUCT`, `ORDER`.  
- **Best Practices**: Align entity names with business glossary terms to ensure consistency and facilitate cross-functional understanding.

#### 3.3.2. Attribute Naming

- **Format**: `[Entity Name]_[Attribute Name]`  
- **Guidance**: Attribute names should be descriptive and unique within the entity. Use adjectives and nouns. Example: `CUSTOMER_FIRST_NAME`, `PRODUCT_UNIT_PRICE`.  
- **Additional Considerations**: Avoid redundancy where the entity name already implies context; however, include it for clarity in flat or denormalized models.

### 3.4. Physical Naming Conventions

> *Define the naming standards for the physical data model. These names are often shorter and more technical, adhering to platform-specific limitations.*

Physical naming conventions must balance clarity, brevity, and technical constraints, supporting automation and operational efficiency.

#### 3.4.1. Table Naming

- **Format**: `[Schema]_[Table Name]_[Suffix]`  
- **Guidance**: Use the approved abbreviation for the business subject area as the table name. Suffixes indicate the type of table.  
- **Modern Context**: In Data Mesh environments, include domain identifiers to support decentralized ownership and discoverability.

| Table Type | Suffix | Example |
| :--- | :--- | :--- |
| Dimension | `_DIM` | `PROD_DIM` (Product Dimension) |
| Fact | `_FCT` | `SALES_FCT` (Sales Fact) |
| Aggregate | `_AGG` | `DLY_SALES_AGG` (Daily Sales Aggregate) |
| Staging | `_STG` | `SRC_CUST_STG` (Source Customer Staging) |
| Snapshot | `_SNP` | `INV_SNP` (Inventory Snapshot) |

#### 3.4.2. Column Naming

- **Format**: `[Abbreviated Attribute Name]`  
- **Guidance**: Use the approved abbreviations from the dictionary. Keep names concise. Maximum length is 30 characters.  
- **Additional Notes**: Include data type hints or flags if necessary to support automated tooling and AI governance traceability.

| Logical Name | Physical Name | Data Type |
| :--- | :--- | :--- |
| `CUSTOMER_FIRST_NAME` | `CUST_FST_NM` | `VARCHAR(50)` |
| `PRODUCT_UNIT_PRICE` | `PROD_UNIT_PRC` | `DECIMAL(10,2)` |

#### 3.4.3. Index Naming

- **Format**: `[Table Name]_[Index Type]_[Sequence]`  
- **Guidance**: Use a standard prefix to identify the index type.  
- **Best Practice**: Include index purpose or column hints for clarity in complex schemas.

| Index Type | Prefix | Example |
| :--- | :--- | :--- |
| Primary Key | `PK_` | `PK_CUSTOMER` |
| Foreign Key | `FK_` | `FK_ORDER_CUSTOMER` |
| Unique Index | `UK_` | `UK_CUSTOMER_EMAIL` |
| Non-Unique Index | `IX_` | `IX_ORDER_DATE` |

---

## 4. Example

> *This section provides a realistic example of applying the naming conventions for a fictional company, GlobalRetail Inc. This demonstrates how the logical and physical names are derived for a simple Order Management domain.*

### 4.1. Abbreviation Dictionary (Excerpt)

| Full Word | Abbreviation |
| :--- | :--- |
| Customer | CUST |
| Product | PROD |
| Order | ORD |
| Detail | DTL |
| Identifier | ID |
| Name | NM |
| Quantity | QTY |
| Price | PRC |

### 4.2. Logical Model Example

- **Entities**: `CUSTOMER`, `PRODUCT`, `ORDER`, `ORDER_DETAIL`
- **Attributes**:
    - `CUSTOMER`: `CUSTOMER_ID`, `CUSTOMER_FIRST_NAME`, `CUSTOMER_LAST_NAME`, `CUSTOMER_EMAIL_ADDRESS`
    - `PRODUCT`: `PRODUCT_ID`, `PRODUCT_NAME`, `PRODUCT_UNIT_PRICE`
    - `ORDER`: `ORDER_ID`, `CUSTOMER_ID`, `ORDER_DATE`
    - `ORDER_DETAIL`: `ORDER_DETAIL_ID`, `ORDER_ID`, `PRODUCT_ID`, `ORDER_QUANTITY`

### 4.3. Physical Model Example (Oracle Database)

- **Tables**:
    - `CRM.CUSTOMER_DIM`
    - `INV.PRODUCT_DIM`
    - `SALES.ORDER_FCT`
    - `SALES.ORDER_DETAIL_FCT`

- **Columns**:
    - `CUSTOMER_DIM`: `CUST_ID` (PK), `CUST_FST_NM`, `CUST_LST_NM`, `CUST_EML_ADDR`
    - `PRODUCT_DIM`: `PROD_ID` (PK), `PROD_NM`, `PROD_UNIT_PRC`
    - `ORDER_FCT`: `ORD_ID` (PK), `CUST_ID` (FK), `ORD_DT`
    - `ORDER_DETAIL_FCT`: `ORD_DTL_ID` (PK), `ORD_ID` (FK), `PROD_ID` (FK), `ORD_QTY`

- **Indexes**:
    - `PK_CUSTOMER_DIM` on `CUST_ID`
    - `UK_CUSTOMER_DIM_EMAIL` on `CUST_EML_ADDR`
    - `FK_ORDER_FCT_CUSTOMER` on `CUST_ID`
    - `IX_ORDER_FCT_DATE` on `ORD_DT`

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Concept | [data-contracts.md](references/concepts-modern-paradigms.md) |
| Data Mesh Principles | Guide | **data-mesh-principles.md** |
| AI Governance Framework | Guide | **ai-governance-framework.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The document defines conventions for all major database object types.
- [x] An official, managed list of abbreviations is established.
- [x] The distinction between logical and physical naming is clear.
- [x] The conventions are unambiguous and easy to follow.
- [x] The document includes a practical example of the conventions in use.
- [x] Naming conventions support modern data architectures and AI governance requirements.
- [x] The document aligns with anticipated DAMA-DMBOK 3.0 updates and emerging industry best practices.

### 5.2. Review Checklist

| Criteria | Reviewer Role | Result (Pass/Fail) |
| :--- | :--- | :--- |
| Consistency with architectural standards | D-Arch | Pass |
| Feasibility for physical implementation | DBA | Pass |
| Alignment with metadata strategy | Meta Mgr | Pass |
| Clarity for business stakeholders | Data Steward | Pass |
| Support for AI governance and compliance | AI Ethics Officer | Pass |
| Overall completeness and correctness | DE Mgr | Pass |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Modeling Standards | Provides the context and overall framework for data modeling, of which naming is a key part. | `templates/templates-KA-03-data-modeling-design.md` |
| Data Governance Framework | Establishes policies and procedures that underpin naming conventions. | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Conceptual Data Model | The entities and attributes in the conceptual model must follow the logical naming conventions. | `templates/templates-KA-03-data-modeling-design.md` |
| Data Dictionary | The data dictionary is populated with metadata derived from correctly named data assets. | `templates/templates-KA-09-metadata-management.md` |
| Data Product Specification | Naming conventions ensure consistency in data product definitions and interfaces. | `templates/templates-KA-10-reference-master-data.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| Data Modeling Tools | Erwin, ER/Studio, SAP PowerDesigner | pgModeler, Vertabelo |
| Data Dictionary / Glossary | Collibra, Alation, Informatica Axon | Apache Atlas, Amundsen |
| Database IDEs | DBeaver, DataGrip, Toad | SQL Developer, pgAdmin |
| AI Governance Platforms | IBM Watson OpenScale, Microsoft Azure Purview | OpenAI Governance Toolkit (community tools) |

### 7.2. Automation Opportunities

- **Linting/Auditing**: Scripts can be developed to automatically scan database schemas to identify objects that do not conform to the naming conventions. These reports can be used to enforce compliance and prioritize remediation efforts. Integration with CI/CD pipelines supports continuous compliance.

- **Code Generation**: Data modeling tools can be configured with the naming convention rules to automatically generate DDL scripts with correct physical names from the logical model, reducing manual errors and accelerating delivery.

- **Glossary Integration**: Data dictionary tools can be integrated with modeling tools to automatically link physical column names to their logical definitions and business terms, supporting metadata-driven AI governance and data product management.

- **AI-Assisted Naming Suggestions**: Emerging AI tools can assist in proposing consistent and contextually appropriate names based on existing conventions and business glossaries, enhancing productivity and standard adherence.

- **Data Contract Validation**: Automation can verify that data contracts and APIs adhere to naming conventions, ensuring consistency across data products and services.

---

## 8. References

- **DAMA-DMBOK2**: Chapter 5 (Data Modeling and Design)  
- **DAMA-DMBOK 3.0 (forthcoming)**: Expected to include expanded guidance on AI governance, data mesh, and data product management.  
- **Internal References**:
    - `templates/templates-KA-01-data-governance.md`
    - `templates/templates-KA-03-data-modeling-design.md`
    - `templates/templates-KA-09-metadata-management.md`
    - `templates/templates-KA-10-reference-master-data.md`
- **External Standards and Regulations**:
    - EU AI Act compliance guidelines
    - GDPR, HIPAA, CCPA regulatory frameworks

---


---

# Conceptual Data Model


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
  - [3.3. Conceptual Model Diagram](#33-conceptual-model-diagram)
  - [3.4. Entity Definitions](#34-entity-definitions)
  - [3.5. Key Attribute Definitions](#35-key-attribute-definitions)
  - [3.6. Relationship Definitions](#36-relationship-definitions)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Model Overview](#42-model-overview)
  - [4.3. Conceptual Model Diagram](#43-conceptual-model-diagram)
  - [4.4. Entity Definitions](#44-entity-definitions)
  - [4.5. Key Attribute Definitions](#45-key-attribute-definitions)
  - [4.6. Relationship Definitions](#46-relationship-definitions)
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

The **Conceptual Data Model (CDM)** represents the highest-level, technology-agnostic view of the data necessary to support business processes and operations. It defines the key business entities, their attributes, and the relationships between them, without specifying technical implementation details such as data types or storage mechanisms. The CDM serves as a foundational artifact to foster clear communication between business stakeholders, data architects, and technical teams, ensuring a shared understanding of the business domain and its data requirements before progressing to more detailed logical and physical data models.

In modern data management contexts, the CDM also plays a pivotal role in supporting emerging paradigms such as Data Mesh and Data Fabric architectures by clearly delineating domain boundaries and data product scopes. It provides the semantic backbone for data contracts and data products, facilitating governance, discoverability, and interoperability across distributed data environments.

> The Conceptual Data Model answers the fundamental question: *"What are the most important things in our business, and how do they relate to each other?"*

Looking ahead, the forthcoming DAMA-DMBOK 3.0 emphasizes the evolving role of conceptual modeling in AI governance frameworks, where clear entity definitions and relationships underpin responsible AI data usage, lineage, and compliance with regulations such as the EU AI Act alongside GDPR, HIPAA, and CCPA.

### 1.2. Scope

**Per Product / Domain** — A Conceptual Data Model is typically created for a specific business domain, data product, or solution area. While it should align with the broader Enterprise Data Model to maintain organizational consistency, the CDM focuses on the entities and relationships relevant to the particular initiative or domain. This domain-centric approach aligns with Data Mesh principles, where each domain owns and governs its data products, supported by well-defined conceptual models.

The CDM does not delve into implementation specifics such as physical storage, indexing, or performance tuning, which are addressed in logical and physical data models. Instead, it provides a stable, business-oriented abstraction that supports cross-domain collaboration, data stewardship, and governance.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The CDM is a critical input for the Business Glossary and Data Governance policies, as it defines the primary business entities requiring standardized definitions and stewardship. It supports AI governance efforts by clarifying data lineage and usage contexts. |
| KA-02: Data Architecture | The CDM must align with the Enterprise Data Model and architectural standards to ensure consistency and interoperability across domains, especially in multi-cloud and hybrid environments. It supports modern architectures such as Data Mesh and Data Fabric by defining domain boundaries and data product semantics. |
| KA-03: Data Modeling and Design | The CDM is the first step in the multi-layered data modeling process, preceding logical and physical models. It establishes the foundational business concepts and relationships. |
| KA-09: Metadata Management | Entities, attributes, and relationships defined in the CDM are key business metadata assets captured in metadata repositories, enabling data discovery, lineage tracking, and impact analysis. |
| KA-13: Big Data and Data Science | Data scientists leverage the CDM to understand the business context of data, identify relevant entities for analytical models, and ensure alignment with business objectives and AI governance requirements. |
| KA-14: Data Product Management | The CDM supports the definition and management of data products by clearly specifying domain entities and relationships, facilitating data contracts and product lifecycle management. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Architect (D-Arch) | Ultimately accountable for the completeness, accuracy, and alignment of the Conceptual Data Model with enterprise standards, architectural principles, and governance policies. Ensures the model supports compliance with data and AI governance frameworks. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Leads the creation, maintenance, and iterative refinement of the Conceptual Data Model. Facilitates workshops with business stakeholders and technical teams to gather requirements and validate the model. Ensures the model reflects current business realities and domain boundaries. |
| **S (Supportive)** | Business Analyst (BA) | Supports the Data Modeler by gathering and documenting detailed business requirements, validating entity and attribute definitions, and ensuring alignment with business processes and objectives. |
| **C (Consulted)** | Data Steward (D-Steward), Subject Matter Expert (SME), AI Ethics Officer | Provide domain expertise, validate entity definitions and relationships, and ensure the model accurately reflects business reality and ethical considerations related to data usage and AI governance. |
| **I (Informed)** | Data Engineer (D-Eng), MLOps Engineer, Data Product Manager | Kept informed of the approved Conceptual Data Model to understand the business context for downstream data pipeline development, AI model training, and data product lifecycle management. |

### 2.2. Section-Level RASCI

| Model Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Entity Identification | D-Modeler | SME, BA, D-Steward | D-Arch |
| Attribute Definition | D-Modeler | D-Steward, SME, AI Ethics Officer | D-Arch |
| Relationship Definition | D-Modeler | SME, BA, AI Ethics Officer | D-Arch |
| Model Diagram | D-Modeler | D-Arch, BA, Data Product Manager | D-Arch |

---

## 3. Template

> *The following is the standardized template for creating a Conceptual Data Model. This template guides the documentation of the high-level data structures for a specific data product or domain.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Conceptual Data Model: [Data Product or Domain Name] |
| Document ID | CDM-[KA#]-[Seq#] |
| Version | [e.g., 1.0] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Architect Name] |
| Related Data Product | [Name of Data Product] |
| AI Governance Status | [e.g., Compliant / Under Review] |

### 3.2. Model Overview

> *Provide a brief narrative of the business domain or data product covered by this model. Describe the key business processes, objectives, and any relevant governance or compliance considerations that this model supports.*

**Input needed**: Business requirements document, process flows, governance policies.  
**Who fills this**: D-Modeler, with input from BA, D-Steward, and AI Ethics Officer.

[Insert narrative overview of the business domain, purpose of the model, and any relevant compliance or governance context.]

### 3.3. Conceptual Model Diagram

> *Insert a visual diagram of the Conceptual Data Model. This diagram should show the key entities and their relationships. Use a standard notation such as Crow's Foot, UML Class Diagram, or ArchiMate. Consider including metadata annotations to support data governance and lineage.*

**Input needed**: List of entities and relationships.  
**Who fills this**: D-Modeler.

[Insert Diagram Here]

### 3.4. Entity Definitions

> *For each entity in the model, provide a clear and concise business definition. The definition should be understandable to a non-technical audience and include references to related business glossary terms and data products.*

**Input needed**: Business glossary, SME interviews, data product documentation.  
**Who fills this**: D-Modeler, with validation from D-Steward, SME, and AI Ethics Officer.

| Entity Name | Definition | Related Glossary Term | Data Product(s) |
| :--- | :--- | :--- | :--- |
| [Entity 1 Name] | [Clear, concise business definition of the entity.] | [Glossary Term] | [Data Product Name(s)] |
| [Entity 2 Name] | [Clear, concise business definition of the entity.] | [Glossary Term] | [Data Product Name(s)] |

### 3.5. Key Attribute Definitions

> *For each entity, list and define its most important attributes from a business perspective. Focus on key identifiers and critical descriptive attributes that are essential for understanding and using the entity.*

**Input needed**: Business requirements, SME interviews, data governance policies.  
**Who fills this**: D-Modeler, with validation from D-Steward, SME, and AI Ethics Officer.

**Entity: [Entity 1 Name]**

| Attribute Name | Definition | Data Sensitivity | Governance Notes |
| :--- | :--- | :--- | :--- |
| [Attribute 1.1 Name] | [Business definition of the key attribute.] | [e.g., PII, Confidential] | [Notes on stewardship, usage constraints] |
| [Attribute 1.2 Name] | [Business definition of the key attribute.] | [e.g., Public] | [Notes on stewardship, usage constraints] |

**Entity: [Entity 2 Name]**

| Attribute Name | Definition | Data Sensitivity | Governance Notes |
| :--- | :--- | :--- | :--- |
| [Attribute 2.1 Name] | [Business definition of the key attribute.] | [e.g., PII, Confidential] | [Notes on stewardship, usage constraints] |
| [Attribute 2.2 Name] | [Business definition of the key attribute.] | [e.g., Public] | [Notes on stewardship, usage constraints] |

### 3.6. Relationship Definitions

> *Describe the relationships between the entities. For each relationship, specify the entities involved, the cardinality (e.g., one-to-one, one-to-many), and a business description of the relationship. Include any governance or compliance considerations relevant to the relationship.*

**Input needed**: Business rules, process flows, governance policies.  
**Who fills this**: D-Modeler, with validation from BA, SME, and AI Ethics Officer.

| Relationship | From Entity | To Entity | Cardinality | Description | Governance Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., Places] | [e.g., Customer] | [e.g., Order] | [e.g., One-to-Many] | [A Customer can place one or more Orders.] | [Notes on data sharing, privacy] |
| [Relationship Name] | [Entity Name] | [Entity Name] | [Cardinality] | [Business description of the relationship.] | [Governance or compliance notes] |

---

## 4. Example

> *This section provides a realistic example of a Conceptual Data Model for a fictional online retail company, GlobalRetail Inc., for their new "Customer Loyalty Program" data product.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Conceptual Data Model: Customer Loyalty Program |
| Document ID | CDM-03-001 |
| Version | 1.0 |
| Effective Date | 2026-02-08 |
| Owner | John Smith, Data Architect |
| Related Data Product | Customer Loyalty Program |
| AI Governance Status | Compliant |

### 4.2. Model Overview

The Customer Loyalty Program is a strategic initiative at GlobalRetail Inc. designed to increase customer retention and lifetime value. This model defines the data structures required to manage loyalty program members, track their purchase activities, calculate loyalty points, and administer rewards. The model supports compliance with GDPR and the EU AI Act by clearly defining personal data entities and their relationships, enabling effective data governance and ethical AI usage in loyalty analytics.

### 4.3. Conceptual Model Diagram

*(A diagram would be embedded here showing the entities Customer, Loyalty Account, Purchase, and Reward, and their relationships, annotated with cardinalities and governance metadata.)*

### 4.4. Entity Definitions

| Entity Name | Definition | Related Glossary Term | Data Product(s) |
| :--- | :--- | :--- | :--- |
| Customer | An individual who has made at least one purchase from GlobalRetail Inc. and is eligible for loyalty rewards. | Customer | Customer Loyalty Program |
| Loyalty Account | An account that tracks a customer's participation, points, and status in the loyalty program. | Loyalty Account | Customer Loyalty Program |
| Purchase | A transaction where a customer buys one or more products. | Purchase | Sales Data Product |
| Reward | A benefit or item that a customer can redeem using their loyalty points. | Reward | Customer Loyalty Program |

### 4.5. Key Attribute Definitions

**Entity: Customer**

| Attribute Name | Definition | Data Sensitivity | Governance Notes |
| :--- | :--- | :--- | :--- |
| Customer ID | Unique identifier for each customer. | PII | Managed under GDPR compliance; access restricted. |
| Full Name | The full legal name of the customer. | PII | Used for identity verification; protected data. |

**Entity: Loyalty Account**

| Attribute Name | Definition | Data Sensitivity | Governance Notes |
| :--- | :--- | :--- | :--- |
| Account ID | Unique identifier for the loyalty account. | Confidential | Internal identifier; access controlled. |
| Points Balance | The current number of redeemable loyalty points. | Public | Used for customer engagement; no PII. |
| Tier Level | The current status level of the member (e.g., Bronze, Silver, Gold). | Public | Used for marketing segmentation. |

### 4.6. Relationship Definitions

| Relationship | From Entity | To Entity | Cardinality | Description | Governance Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Has | Customer | Loyalty Account | One-to-One | Each Customer has exactly one Loyalty Account. | Customer consent required for data linkage. |
| Makes | Customer | Purchase | One-to-Many | A Customer can make multiple Purchases. | Purchase data subject to privacy policies. |
| Redeems | Loyalty Account | Reward | One-to-Many | A Loyalty Account can redeem multiple Rewards. | Reward redemption tracked for audit. |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Governance Framework | Knowledge Area | **KA-01-data-governance.md** |
| Data Architecture | Knowledge Area | **KA-02-data-architecture.md** |
| Modeling Standards | Deliverable | [01-modeling-standards.md](templates/templates-KA-03-data-modeling-design.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The model is technology-agnostic and independent of physical implementation.
- [x] All key business entities relevant to the domain or data product are identified and defined.
- [x] All entities have clear, unambiguous business definitions aligned with the enterprise Business Glossary.
- [x] The relationships between entities are correctly identified, defined, and cardinalities specified.
- [x] The model has been reviewed and validated by business stakeholders, data stewards, and AI governance officers.
- [ ] The model is aligned with the Enterprise Data Model and architectural standards.
- [ ] The model supports compliance with relevant data privacy and AI governance regulations (e.g., GDPR, EU AI Act).
- [ ] The model is documented with appropriate metadata for discoverability and lineage tracking.

### 5.2. Review Checklist

| Criteria | Status (Pass/Fail) | Comments |
| :--- | :--- | :--- |
| **Clarity** | Pass | Definitions are clear and understandable to business and technical audiences. |
| **Completeness** | Pass | All major domain concepts and relationships are included. |
| **Correctness** | Pass | The model accurately reflects the business domain and rules. |
| **Consistency** | Fail | The "Customer" entity definition is not aligned with the enterprise definition. Needs revision. |
| **Governance Alignment** | Pass | Model supports data stewardship and AI governance requirements. |
| **Compliance Readiness** | Pass | Sensitive data elements are identified and annotated for compliance. |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output Name | Path |
| :--- | :--- |
| Enterprise Data Model | `templates/templates-KA-02-data-architecture.md` |
| Modeling Standards | `templates/templates-KA-03-data-modeling-design.md` |
| Business Glossary | `templates/templates-KA-01-data-governance.md` |
| Data Governance Framework | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers

| Output Name | Path |
| :--- | :--- |
| Logical Data Model | `./04-logical-data-model.md` |
| Entity Definitions | `./06-entity-definitions.md` |
| Data Product Specification | `templates/templates-KA-14-data-management-maturity.md` |
| AI Model Training Data Definition | `templates/templates-KA-13-big-data-data-science.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Category | Commercial Tools | Open Source Tools |
| :--- | :--- | :--- |
| Data Modeling | Erwin Data Modeler, SAP PowerDesigner, ER/Studio, IBM InfoSphere Data Architect | draw.io (diagrams.net), OpenModelica, Archi, Modelio |
| Diagramming | Microsoft Visio, Lucidchart, Sparx Systems Enterprise Architect | PlantUML, Mermaid.js, Graphviz |
| Metadata Management | Collibra, Informatica EDC, Alation | Apache Atlas, Amundsen |

### 7.2. Automation Opportunities

Automation can be leveraged to accelerate the creation and maintenance of Conceptual Data Models by:

- Using Natural Language Processing (NLP) to scan business requirement documents, process flows, and meeting transcripts to identify candidate entities (nouns) and relationships (verbs).
- Integrating with metadata repositories to auto-populate entity and attribute definitions, ensuring consistency and traceability.
- Automatically generating initial Logical Data Models from approved Conceptual Data Models, reducing manual effort and improving alignment.
- Embedding governance annotations and compliance flags directly into models to support AI governance and regulatory audits.
- Utilizing AI-assisted modeling tools that suggest model improvements based on best practices and organizational standards.

These automation capabilities support faster delivery, higher quality, and better governance of data models in modern, cloud-native, and multi-domain environments.

---

## 8. References

- DAMA-DMBOK2, Chapter 5: Data Modeling and Design  
- DAMA-DMBOK 3.0 (forthcoming, 2025): Enhanced focus on AI governance, data mesh integration, and data product management  
- EU AI Act and GDPR Compliance Guidelines  
- Internal Reference: `references/reference-materials.md`  
- Internal Reference: `templates/templates-KA-02-data-architecture.md`  
- Internal Reference: `templates/templates-KA-01-data-governance.md`  
- Internal Reference: `templates/templates-KA-14-data-management-maturity.md`


---

# Logical Data Model


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
  - [3.3. Logical Data Model Diagram](#33-logical-data-model-diagram)
  - [3.4. Entity and Attribute Definitions](#34-entity-and-attribute-definitions)
  - [3.5. Relationship Definitions](#35-relationship-definitions)
  - [3.6. Normalization](#36-normalization)
- [4. Example](#4-example)
  - [4.1. Model Overview](#41-model-overview)
  - [4.2. Logical Data Model Diagram](#42-logical-data-model-diagram)
  - [4.3. Entity and Attribute Definitions](#43-entity-and-attribute-definitions)
  - [4.4. Relationship Definitions](#44-relationship-definitions)
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

The **Logical Data Model (LDM)** is a detailed, technology-agnostic representation of the data requirements for a specific business domain or product. It evolves from the Conceptual Data Model by adding significantly more detail, including all entities, attributes with their data types and constraints, and the relationships between them with cardinality and optionality. The LDM describes the *what* and the *how* of the data structure from a business perspective, without specifying *how* it will be physically implemented in a database.

> The primary purpose of a Logical Data Model is to serve as a precise blueprint for data-related development, ensuring that business requirements are accurately translated into a structured format that can be understood by both business stakeholders and technical teams. It is the critical bridge between conceptual ideas and physical implementation.

In the evolving data management landscape, the LDM also plays a vital role in supporting modern data architectures such as Data Mesh and Data Fabric by defining clear, domain-oriented data structures that enable decentralized ownership and interoperability. Furthermore, with the increasing importance of AI governance, the LDM helps ensure that data used in AI/ML models is well-defined, consistent, and compliant with regulatory frameworks such as the EU AI Act, GDPR, HIPAA, and CCPA.

Looking forward to DAMA-DMBOK 3.0 (expected mid-2025), the Logical Data Model is anticipated to integrate more explicitly with data product concepts and data contracts, emphasizing its role in enabling data as a product and supporting operational governance in cloud-native and multi-cloud environments.

### 1.2. Scope

**Per Product** — A Logical Data Model is typically created for a specific data product, application, or a well-defined project scope. While it must align with the global Enterprise Data Model, its focus is on detailing the data requirements for a particular solution, making it a product-specific artifact.

This product-centric focus aligns with emerging practices in agentic data stewardship and data product management, where clear ownership and accountability for data domains are established. The LDM serves as a foundational artifact that supports these roles by providing a clear, authoritative definition of the data elements and their relationships within the product scope.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-02: Data Architecture | The LDM must conform to the principles and standards defined in the `02-architecture-blueprint.md` and align with the `01-enterprise-data-model.md`. It supports architectural patterns such as Data Mesh and Lakehouse by providing domain-specific logical structures. |
| KA-01: Data Governance | The LDM is a key input for the `06-business-glossary.md` and `07-business-rules.md`, as it defines the attributes and relationships that require clear business definitions and rules. It also supports AI governance frameworks by ensuring data definitions are precise and compliant. |
| KA-06: Data Integration | The LDM provides the structural definition needed for creating accurate `06-source-to-target-mapping.md` documents and supports DataOps practices by enabling consistent integration pipelines. |
| KA-11: Data Quality | The data types, constraints, and business rules defined in the LDM are foundational for establishing data quality rules and metrics in the `11-data-quality-rules.md` output. It also underpins automated validation in MLOps and FinOps contexts. |
| KA-10: Metadata Management | The LDM contributes to metadata repositories by providing detailed entity and attribute definitions that feed into business glossaries and data catalogs, supporting discoverability and lineage. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately answerable for the quality, completeness, and timely delivery of the Logical Data Model. Ensures it meets business requirements, architectural standards, and compliance mandates including AI governance and regulatory requirements. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Leads the creation, refinement, and maintenance of the Logical Data Model. Works with stakeholders to gather requirements and translates them into the model. Ensures alignment with data product definitions and data contracts. |
| **S (Supportive)** | Data Architect (D-Arch) | Provides guidance on architectural alignment, modeling standards, and best practices. Reviews the model to ensure it fits within the enterprise data landscape and supports modern architectures such as Data Mesh and Lakehouse. |
| **C (Consulted)** | Data Steward (D-Steward), Subject Matter Expert (SME), AI Ethics Officer | Provide deep business knowledge, define business rules, validate attribute definitions, and confirm relationship logic. Their input is critical for the model's accuracy and compliance with AI ethics and governance policies. |
| **I (Informed)** | Data Engineer (D-Eng), MLOps Engineer | Informed of the finalized LDM, which they will use as a primary input for designing and building the Physical Data Model, data pipelines, and operational ML workflows. |

### 2.2. Section-Level RASCI

| LDM Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Entity & Attribute Definition | D-Modeler | D-Steward, SME, AI Ethics Officer | DE Mgr |
| Relationship Modeling | D-Modeler | D-Steward, SME | DE Mgr |
| Normalization & Structure | D-Modeler | D-Arch | DE Mgr |
| Data Typing & Constraints | D-Modeler | D-Arch, D-Steward | DE Mgr |
| Alignment with Conceptual Model | D-Modeler | D-Arch | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Logical Data Model document. This template guides the Data Modeler in capturing all necessary details to translate business requirements into a structured model.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Logical Data Model: [Product/Project Name] |
| Document ID | LDM-[KA_CODE]-[SEQ_NUM] |
| Version | [e.g., 1.0] |
| Status | [Draft, In Review, Approved] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Modeler Name] |
| Approver | [Data Engineering Manager Name] |

### 3.2. Model Overview

> *Provide a high-level summary of the model. Describe the business process or domain it represents, its key purpose, and the major entities included. Reference the corresponding Conceptual Data Model.*

**Input needed**: `03-conceptual-data-model.md`, project charter, business requirements document, AI governance policies.
**Who fills this**: Data Modeler.

- **Business Domain**: [e.g., Customer Order Management, Inventory Control]
- **Purpose**: [e.g., To define the data structure required to support the new e-commerce checkout process, ensuring compliance with data privacy and AI governance standards.]
- **Related Conceptual Model**: [Link to `templates/templates-KA-03-data-modeling-design.md`]
- **Alignment with Data Product Strategy**: [Describe how this LDM supports the data product roadmap and data contracts.]
- **Compliance Considerations**: [Note any regulatory or AI governance requirements impacting the model.]

### 3.3. Logical Data Model Diagram

> *Embed a visual diagram of the Logical Data Model. This diagram is the centerpiece of the document and should clearly show all entities, their attributes, and the relationships between them. Use standard notation (e.g., Crow's Foot) to depict cardinality and optionality.*

**Input needed**: Data modeling tool (e.g., Erwin, ER/Studio, Lucidchart).
**Who fills this**: Data Modeler.

[Insert Logical Data Model Diagram Image Here]

### 3.4. Entity and Attribute Definitions

> *This section provides a detailed dictionary of every entity and attribute in the model. It is the most verbose and critical part of the LDM, ensuring clarity and eliminating ambiguity.*

**Input needed**: Business Glossary, SME interviews, requirements documents, AI governance guidelines.
**Who fills this**: Data Modeler, with heavy consultation from Data Stewards, SMEs, and AI Ethics Officers.

#### 3.4.1. Entity: [Entity Name 1]

- **Definition**: [Clear, concise business definition of the entity.]
- **Supertype/Subtype**: [If applicable, e.g., Subtype of 'Party']

| Attribute Name | Data Type | PK/FK | Nullable? | Business Definition | Business Rules & Constraints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[attribute_id]` | `INTEGER` | PK | No | Unique system identifier for the entity. | Generated by the system. Immutable. |
| `[attribute_name]` | `VARCHAR(100)` | | No | The official business name for the entity. | Must be unique. |
| `[attribute_desc]` | `VARCHAR(255)` | | Yes | A detailed description of the entity instance. | |
| `[foreign_key_id]` | `INTEGER` | FK | No | Foreign key referencing the `[Parent_Entity]` table. | Must correspond to a valid record in `[Parent_Entity]`. |
| `[attribute_code]` | `CHAR(10)` | | No | A standardized code representing a classification. | Must exist in the `Reference_Code` table. |
| `[eff_start_date]` | `DATE` | | No | The date from which this record is effective. | Cannot be in the future. |

#### 3.4.2. Entity: [Entity Name 2]

- **Definition**: [Clear, concise business definition of the entity.]
- **Supertype/Subtype**: [If applicable]

| Attribute Name | Data Type | PK/FK | Nullable? | Business Definition | Business Rules & Constraints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` |

### 3.5. Relationship Definitions

> *Explicitly document each relationship shown in the diagram. Describe the business rule that the relationship enforces.*

**Input needed**: Business process documentation, SME interviews, AI governance policies.
**Who fills this**: Data Modeler.

| Parent Entity | Child Entity | Relationship Name | Cardinality | Optionality | Business Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[Entity A]` | `[Entity B]` | `Manages` | One-to-Many | Mandatory (1..*) | Each `[Entity A]` must manage one or more `[Entity B]`. Each `[Entity B]` must be managed by exactly one `[Entity A]`. |
| `[Entity C]` | `[Entity D]` | `Contains` | One-to-Many | Optional (0..*) | Each `[Entity C]` may contain zero or more `[Entity D]`. Each `[Entity D]` must be contained within exactly one `[Entity C]`. |
| `[Entity E]` | `[Entity F]` | `Links` | Many-to-Many | Optional (0..*) | An `[Entity E]` can be linked to many `[Entity F]`s, and an `[Entity F]` can be linked to many `[Entity E]`s. (This will be resolved via a linking table in the physical model). |

### 3.6. Normalization

> *State the level of normalization achieved by the model (typically Third Normal Form - 3NF for transactional systems) and provide a brief justification. If any denormalization is intentionally included, document it here with a clear rationale (e.g., for performance reasons).*

**Input needed**: Data modeling best practices, performance requirements.
**Who fills this**: Data Modeler, with review from Data Architect.

- **Target Normal Form**: [e.g., Third Normal Form (3NF)]
- **Justification**: [e.g., The model is designed to be in 3NF to minimize data redundancy, prevent update anomalies, and ensure data integrity.]
- **Documented Denormalization**: [e.g., The `customer_summary` attribute on the `Customer` entity is a calculated, denormalized field included to improve query performance for the main dashboard. It is updated via a nightly batch process.]
- **Performance Considerations**: [Note any denormalization or design choices made to support cloud-native architectures, data mesh domain boundaries, or AI/ML model performance.]

---

## 4. Example

> *This example illustrates a partial Logical Data Model for a customer order system at the fictional company, GlobalRetail Inc.*

### 4.1. Model Overview

- **Business Domain**: E-commerce Sales
- **Purpose**: To define the data structure for capturing customer orders placed through the GlobalRetail Inc. website, ensuring data quality and compliance with privacy regulations and AI governance policies.
- **Related Conceptual Model**: `templates/templates-KA-03-data-modeling-design.md`

### 4.2. Logical Data Model Diagram

*(A diagram would be embedded here showing Customer, Order, OrderLine, and Product entities with their relationships.)*

### 4.3. Entity and Attribute Definitions

#### Entity: Customer

- **Definition**: A person or organization that has registered an account with GlobalRetail Inc.

| Attribute Name | Data Type | PK/FK | Nullable? | Business Definition | Business Rules & Constraints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `customer_id` | `INTEGER` | PK | No | Unique system identifier for the customer. | System-generated, immutable. |
| `first_name` | `VARCHAR(50)` | | No | The customer's legal first name. | |
| `last_name` | `VARCHAR(50)` | | No | The customer's legal last name. | |
| `email_address` | `VARCHAR(100)`| | No | The customer's unique email address, used for login. | Must be a valid email format. Must be unique across all customers. |
| `registration_date`| `TIMESTAMP` | | No | The date and time the customer created their account. | Defaults to `CURRENT_TIMESTAMP`. |
| `customer_status` | `CHAR(8)` | | No | The current status of the customer account. | Must be one of: 'Active', 'Inactive', 'Suspended'. Defaults to 'Active'. |

#### Entity: Order

- **Definition**: A single transaction where a customer purchases one or more products.

| Attribute Name | Data Type | PK/FK | Nullable? | Business Definition | Business Rules & Constraints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `order_id` | `INTEGER` | PK | No | Unique system identifier for the order. | System-generated, immutable. |
| `customer_id` | `INTEGER` | FK | No | Foreign key referencing the `Customer` who placed the order. | Must be a valid `customer_id` from the `Customer` table. |
| `order_date` | `TIMESTAMP` | | No | The date and time the order was successfully submitted. | |
| `order_status` | `VARCHAR(15)` | | No | The current stage of the order in the fulfillment process. | Must be one of: 'Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled'. |
| `shipping_address` | `VARCHAR(255)`| | No | The full address where the order is to be shipped. | |
| `total_amount` | `DECIMAL(10, 2)`| | No | The final calculated total cost of the order, including tax and shipping. | Must be greater than 0. |

### 4.4. Relationship Definitions

| Parent Entity | Child Entity | Relationship Name | Cardinality | Optionality | Business Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Customer` | `Order` | `Places` | One-to-Many | Optional (0..*) | A `Customer` may place zero or more `Order`s. Each `Order` must be placed by exactly one `Customer`. |
| `Order` | `OrderLine` | `Comprises` | One-to-Many | Mandatory (1..*) | An `Order` must be comprised of one or more `OrderLine`s. Each `OrderLine` belongs to exactly one `Order`. |
| `Product` | `OrderLine` | `Fulfills` | One-to-Many | Optional (0..*) | A `Product` may fulfill zero or more `OrderLine`s. Each `OrderLine` must be for exactly one `Product`. |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Conceptual Data Model | Deliverable | [03-conceptual-data-model.md](templates/templates-KA-03-data-modeling-design.md) |
| Business Glossary | Deliverable | [06-business-glossary.md](templates/templates-KA-01-data-governance.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [ ] The Logical Data Model has been formally approved by the Accountable role (DE Mgr).
- [ ] The model accurately reflects all data-related business requirements from the source documentation.
- [ ] All entities, attributes, and relationships are clearly and unambiguously defined.
- [ ] The model is confirmed to be in the target normal form (e.g., 3NF).
- [ ] All data types and constraints are appropriate for the business data they represent.
- [ ] The model is consistent with the Enterprise Data Model and architectural standards, including alignment with Data Mesh and Data Fabric principles.
- [ ] The model incorporates considerations for AI governance, privacy, and regulatory compliance.
- [ ] A visual diagram of the model is included and is legible.
- [ ] The model has been reviewed and validated by the designated business stakeholders (SMEs, Data Stewards, AI Ethics Officer).
- [ ] The model supports integration with data contracts and data product management frameworks.

### 5.2. Review Checklist

| Review Area | Question | Expected Outcome |
| :--- | :--- | :--- |
| **Clarity** | Are entity and attribute definitions understandable to a business user? | Yes, definitions should use business language and avoid technical jargon. |
| **Completeness** | Does the model capture all required data elements for the specified scope? | Yes, all fields from source systems or required by business processes are included. |
| **Correctness** | Do relationships and cardinalities correctly represent the business rules? | Yes, a one-to-many relationship in the model reflects a one-to-many rule in the business. |
| **Consistency** | Does the model use standard naming conventions and data types? | Yes, all elements adhere to the `02-naming-conventions.md` and `01-modeling-standards.md`. |
| **Non-Redundancy** | Is the model free from unnecessary data duplication (normalized)? | Yes, the same piece of information should not be stored in multiple places unless intentionally denormalized for a documented reason. |
| **Compliance** | Does the model incorporate necessary constraints and definitions to support GDPR, HIPAA, CCPA, and EU AI Act compliance? | Yes, personal data and sensitive attributes are clearly identified and governed. |
| **Governance** | Does the model support AI governance and ethical considerations? | Yes, includes attributes and relationships that enable traceability, explainability, and accountability. |
| **Integration** | Is the model designed to support integration with DataOps, MLOps, and FinOps workflows? | Yes, the model supports automation and operationalization needs. |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output Name | File Path | Purpose |
| :--- | :--- | :--- |
| Conceptual Data Model | `templates/templates-KA-03-data-modeling-design.md` | Provides the high-level business entities and relationships that are the starting point for the LDM. |
| Modeling Standards | `templates/templates-KA-03-data-modeling-design.md` | Defines the rules, notations, and best practices to be followed during modeling. |
| Naming Conventions | `templates/templates-KA-03-data-modeling-design.md` | Ensures consistent and understandable naming of entities and attributes. |
| Business Glossary | `templates/templates-KA-01-data-governance.md` | Provides standard definitions for business terms used in the model. |
| AI Governance Framework | `templates/templates-KA-01-data-governance.md` | Provides policies and guidelines for AI-related data management and ethical considerations. |

### 6.2. Consumers (Outputs)

| Output Name | File Path | Purpose |
| :--- | :--- | :--- |
| Physical Data Model | `templates/templates-KA-03-data-modeling-design.md` | The LDM is the direct input for creating the technology-specific physical model. |
| Attribute Definitions | `templates/templates-KA-03-data-modeling-design.md` | The detailed attribute definitions from the LDM are extracted into this dedicated document. |
| Source-to-Target Mapping | `templates/templates-KA-06-data-integration-interoperability.md` | The LDM defines the target structure for data integration and mapping activities. |
| Data Contracts | `templates/templates-KA-03-data-modeling-design.md` | Defines formal agreements on data structure, quality, and delivery based on the LDM. |
| Data Product Definition | `templates/templates-KA-03-data-modeling-design.md` | Uses the LDM to define data products with clear ownership and service levels. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling** | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, Navicat Data Modeler | Lucidchart (Free Tier), draw.io (diagrams.net), OpenModelSphere |
| **Collaboration** | Confluence, SharePoint | Git (with Markdown), Wiki.js |
| **Metadata Management**| Collibra, Alation, Informatica EDC | Apache Atlas, Amundsen |
| **AI Governance & MLOps** | DataRobot, MLflow, Seldon | Kubeflow, TensorBoard |

### 7.2. Automation Opportunities

- **Model Generation**: Some tools can reverse-engineer a basic logical model from an existing database schema, which can then be refined. More advanced tools can forward-engineer the Physical Data Model (DDL scripts) directly from the approved Logical Data Model.
- **Documentation Generation**: Metadata management tools can connect to data modeling tools to automatically ingest and publish entity and attribute definitions, creating a "living" data dictionary and business glossary.
- **Validation**: Scripts can be developed to automatically validate a model against naming conventions and other defined standards, flagging non-compliant objects for review.
- **Governance Enforcement**: Automated checks can verify that data models comply with AI governance policies, privacy regulations, and data contracts.
- **Integration with DevOps Pipelines**: Logical models can be integrated into CI/CD pipelines for data infrastructure, supporting DataOps and MLOps workflows.
- **Change Impact Analysis**: Tools can analyze changes in the LDM to assess downstream impacts on data products, contracts, and AI models.

---

## 8. References

| Ref | Description |
| :--- | :--- |
| [1] | DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge*. 2nd ed., 2017. (Chapter 5: Data Modeling and Design) |
| [2] | DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Expected 2025. Emphasizes data products, AI governance, and modern architectures. |
| [3] | Internal Document: `templates/templates-KA-03-data-modeling-design.md` |
| [4] | Internal Document: `references/reference-materials.md` |
| [5] | EU AI Act and GDPR Compliance Guidelines, 2023. |
| [6] | Data Mesh Principles and Practices, Zhamak Dehghani, ThoughtWorks, 2020. |
| [7] | AI Governance Framework, Internal Document: `templates/templates-KA-01-data-governance.md` |


---

# Physical Data Model


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
  - [3.3. Physical Data Model Diagram](#33-physical-data-model-diagram)
  - [3.4. Table and View Specifications](#34-table-and-view-specifications)
  - [3.5. Indexing Strategy](#35-indexing-strategy)
  - [3.6. Partitioning Strategy](#36-partitioning-strategy)
  - [3.7. Data Definition Language (DDL)](#37-data-definition-language-ddl)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Model Overview](#42-model-overview)
  - [4.3. Physical Data Model Diagram](#43-physical-data-model-diagram)
  - [4.4. Table and View Specifications](#44-table-and-view-specifications)
  - [4.5. Indexing Strategy](#45-indexing-strategy)
  - [4.6. Partitioning Strategy](#46-partitioning-strategy)
  - [4.7. Data Definition Language (DDL)](#47-data-definition-language-ddl)
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

The **Physical Data Model (PDM)** is the definitive specification for how data is physically stored and accessed within a specific database technology or data platform. It translates the business-oriented logical data model into a concrete, implementation-ready blueprint that reflects the physical constraints, capabilities, and optimizations of the target environment.

The PDM is not merely a diagram; it is a comprehensive set of technical specifications that includes table names, column names, data types, primary keys, foreign keys, indexes, constraints, partitioning schemes, storage parameters, and other database-specific or platform-specific parameters required to create and maintain the database schema or data product.

> The primary purpose of the Physical Data Model is to provide the Data Definition Language (DDL) and related artifacts required to instantiate the database or data product, ensuring that the data structure is optimized for performance, integrity, scalability, and the specific requirements of the consuming applications and services.

In the evolving data management landscape, the PDM also supports modern data architectures such as data mesh and data fabric, where physical models may be distributed across multiple cloud platforms or data lakes, and must comply with AI governance and regulatory requirements (e.g., EU AI Act, GDPR). The PDM thus plays a critical role in enabling data products that are compliant, performant, and interoperable.

### 1.2. Scope

**Per Product or System** — A Physical Data Model is created for each individual data product, data service, or system that requires its own physical data representation. While it must adhere to enterprise-wide standards (such as naming conventions, approved data types, and security policies), the PDM itself is specific to the technology platform (e.g., Oracle, PostgreSQL, Snowflake, Databricks Lakehouse) and the unique operational requirements of that product.

The scope includes:

- Defining physical tables, views, materialized views, and indexes.
- Specifying storage parameters, partitioning, and clustering strategies.
- Incorporating data governance controls such as masking, encryption, and access control annotations.
- Supporting multi-cloud or hybrid cloud deployments by specifying platform-specific features.
- Enabling integration with MLOps and DataOps pipelines through version-controlled DDL and schema evolution strategies.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-02: Data Architecture | The PDM must conform to the approved `04-technology-standards.md` and `02-architecture-blueprint.md` defined by the Data Architecture KA. It reflects architectural decisions including cloud platform choices and data mesh domains. |
| KA-04: Data Storage and Operations | The PDM is the primary input for the Database Administrator (DBA) and DataOps teams to create, configure, and manage the physical data stores as described in `01-database-standards.md`. It supports operational concerns like backup, recovery, and performance tuning. |
| KA-06: Data Integration and Interoperability | The PDM defines the target schema for data integration processes documented in `06-source-to-target-mapping.md`, enabling consistent data ingestion and transformation pipelines. |
| KA-09: Metadata Management | The PDM serves as a key source of technical metadata for populating the data dictionary and metadata repositories (`06-data-dictionary.md`), supporting data lineage and impact analysis. |
| KA-11: Data Quality | Data quality rules from `05-data-quality-rules.md` are often implemented as constraints, triggers, and data type definitions within the PDM to enforce data integrity at the physical level. |
| KA-12: Data Security and Privacy | The PDM must incorporate security controls and privacy requirements, including encryption, masking, and access control policies, as defined in `01-data-security-privacy.md`. |
| KA-14: Artificial Intelligence and Machine Learning | The PDM supports AI governance by ensuring data structures comply with model input requirements and regulatory constraints, facilitating integration with MLOps pipelines (`01-mlops-integration.md`). |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately accountable for the creation, quality, maintenance, and compliance of the Physical Data Model, ensuring it meets performance, scalability, and governance requirements including AI governance and regulatory compliance. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Designs and creates the Physical Data Model, translating the logical model into a technology-specific implementation. Generates the DDL and documents design decisions, including performance optimizations and compliance controls. |
| **S (Supportive)** | Database Administrator (DBA), Data Engineer (D-Eng), DataOps Engineer | The DBA provides expertise on database performance tuning, storage, and security. The Data Engineer advises on data ingestion and usage patterns. The DataOps Engineer supports deployment automation and schema versioning. |
| **C (Consulted)** | Data Architect (D-Arch), Data Governance Lead, AI Ethics Officer | Consulted to ensure the PDM aligns with enterprise data architecture, governance policies, AI ethical standards, and technology standards. |
| **I (Informed)** | Application Developers, Data Analysts, MLOps Engineer | Informed of the final schema to enable application development, analytics, and model training pipelines. |

### 2.2. Section-Level RASCI

| PDM Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Document Header | D-Modeler | Data Architect | DE Mgr |
| Model Overview | D-Modeler | Data Architect, Data Governance Lead | DE Mgr |
| Physical Data Model Diagram | D-Modeler | DBA, Data Engineer | DE Mgr |
| Table and Column Definitions | D-Modeler | DBA, Data Steward | DE Mgr |
| Data Type and Constraint Selection | D-Modeler | DBA, Data Governance Lead | DE Mgr |
| Indexing Strategy | D-Modeler, DBA | Data Engineer | DE Mgr |
| Partitioning Strategy | DBA | D-Modeler | DE Mgr |
| DDL Script Generation | D-Modeler | DBA, DataOps Engineer | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating a Physical Data Model document. This document accompanies the actual DDL script and provides the necessary context, design decisions, and governance considerations.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Physical Data Model for [Product Name] |
| Document ID | PDM-[KA_ID]-[Product_ID] |
| Version | [e.g., 1.0] |
| Technology Platform | [e.g., PostgreSQL 15.4, Snowflake, Oracle 19c, Databricks Lakehouse] |
| Related Logical Data Model | [Link to LDM file, e.g., `templates/templates-KA-03-data-modeling-design.md`] |
| Data Product Owner | [Name/Role] |
| Data Steward | [Name/Role] |
| Date Created | [YYYY-MM-DD] |
| Last Updated | [YYYY-MM-DD] |

### 3.2. Model Overview

> *Provide a high-level description of the model's purpose, the business process it supports, and the data product context. Include a summary of key design decisions such as normalization level, denormalization for performance, partitioning choices, and compliance considerations.*

- Purpose and scope of the model.
- Supported business processes and applications.
- Key design principles (e.g., normalization, denormalization).
- Performance optimization strategies.
- Compliance with data governance and AI governance policies.
- Considerations for cloud-native or multi-cloud deployment.
- Integration points with MLOps and DataOps pipelines.

[Insert Model Overview]

### 3.3. Physical Data Model Diagram

> *Embed a diagram of the physical model. The diagram should show all tables, columns, data types, and relationships (primary/foreign keys). This provides a visual representation of the schema.*

**Input needed**: Data modeling tool (e.g., Erwin, ER/Studio, Draw.io, Vertabelo).  
**Who fills this**: D-Modeler.

[Insert Diagram Image or Link to Diagram]

### 3.4. Table and View Specifications

> *For each table and view in the model, create a subsection with a detailed specification. This is the core of the PDM documentation.*

#### 3.4.1. [Table Name]

- **Description**: [Briefly describe the purpose of the table and its role in the data product.]
- **Owner**: [Data Steward or Business Owner]
- **Estimated Rows**: [e.g., 10 Million initial, growing 1M/year]
- **Compliance Notes**: [e.g., Contains PII, subject to GDPR; masked columns for AI use]

| Column Name | Data Type | PK | FK | Not Null | Unique | Default | Check Constraint | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [column_id] | [e.g., INT] | Y | N | Y | Y | `nextval('seq_name')` | `> 0` | [Primary key for the table] |
| [column_name] | [e.g., VARCHAR(255)] | N | N | Y | N | | | [Description of the column] |
| [foreign_key_id] | [e.g., INT] | N | Y | Y | N | | | [Foreign key referencing Table X] |

### 3.5. Indexing Strategy

> *Detail the indexes that will be created to support query performance. Explain the rationale for each index, referencing specific query patterns, SLAs, or data access patterns.*

**Input needed**: Application query patterns, performance requirements from SLAs, data volume projections.  
**Who fills this**: D-Modeler, with input from DBA and Data Engineer.

| Table Name | Index Name | Indexed Columns | Index Type | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| [Table Name] | [e.g., idx_customer_name] | [customer_name, customer_zip] | [e.g., B-Tree, Bitmap, Hash] | [Supports frequent lookups by customer name and location.] |

### 3.6. Partitioning Strategy

> *For very large tables (VLDBs), describe the partitioning strategy. Specify the partitioning key, the type of partitioning (e.g., range, list, hash), and the expected benefits for performance, maintenance, and compliance.*

**Input needed**: Data volume projections, data access patterns, archival policies.  
**Who fills this**: DBA, with input from D-Modeler and Data Governance Lead.

- **Table**: [Table Name]
- **Partitioning Type**: [e.g., Range, List, Hash, Composite]
- **Partitioning Key**: [e.g., transaction_date, region]
- **Partitioning Scheme**: [e.g., One partition per month, per region]
- **Rationale**: [e.g., Improves query performance for time-based analysis, simplifies archival, supports data locality for compliance.]

### 3.7. Data Definition Language (DDL)

> *Include the complete, executable DDL script to create all tables, views, indexes, sequences, and constraints. This script is the final, actionable output of the PDM process.*

```sql
-- DDL for [Product Name]
-- Generated on [YYYY-MM-DD]

CREATE TABLE [SchemaName].[TableName] (
    -- ... column definitions ...
);

CREATE INDEX [IndexName] ON [SchemaName].[TableName] ([ColumnName]);

-- ... etc. ...
```

---

## 4. Example

> *This is a realistic example of a Physical Data Model for a 'Customer Orders' database for the fictional company GlobalRetail Inc. The target database is PostgreSQL.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Document Title | Physical Data Model for Customer Orders |
| Document ID | PDM-KA03-ORD001 |
| Version | 1.0 |
| Technology Platform | PostgreSQL 15.4 |
| Related Logical Data Model | `templates/templates-KA-03-data-modeling-design.md` |
| Data Product Owner | Jane Doe, Head of Sales Analytics |
| Data Steward | John Smith, Customer Data Steward |
| Date Created | 2026-02-01 |
| Last Updated | 2026-02-08 |

### 4.2. Model Overview

This model captures customer order information for GlobalRetail's e-commerce platform. It is designed to support high-volume transactional processing (OLTP) and analytical reporting (OLAP) through denormalization and partitioning.

Key design decisions include:

- Denormalization in the `order_summary` table to improve read performance for the order dashboard, reducing complex joins during peak hours.
- Partitioning the `sales.orders` table by quarter to optimize query performance and simplify archival.
- Use of UUIDs for natural keys to support data mesh interoperability.
- Compliance with GDPR by masking sensitive customer data in analytical views.
- Integration with DataOps pipelines for automated deployment and testing.
- Support for multi-cloud deployment with platform-agnostic data types.

### 4.3. Physical Data Model Diagram

*(A diagram created in a tool like Draw.io would be embedded here)*

### 4.4. Table and View Specifications

#### 4.4.1. `sales.customers`

- **Description**: Master table for customer information.
- **Owner**: Customer Data Steward
- **Estimated Rows**: 50 Million, growing 5M/year
- **Compliance Notes**: Contains Personally Identifiable Information (PII); subject to GDPR and CCPA. Sensitive columns are masked in analytical views.

| Column Name | Data Type | PK | FK | Not Null | Unique | Default | Check Constraint | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `customer_id` | `BIGSERIAL` | Y | N | Y | Y | | | Surrogate primary key |
| `customer_uuid` | `UUID` | N | N | Y | Y | `gen_random_uuid()` | | Natural key for external systems and data mesh interoperability |
| `first_name` | `VARCHAR(100)` | N | N | Y | N | | | Customer's first name |
| `last_name` | `VARCHAR(100)` | N | N | Y | N | | | Customer's last name |
| `email` | `VARCHAR(255)` | N | N | Y | Y | | | Customer's unique email address |
| `created_at` | `TIMESTAMPTZ` | N | N | Y | N | `NOW()` | | Timestamp of record creation |

#### 4.4.2. `sales.orders`

- **Description**: Contains header-level information for each customer order.
- **Owner**: Sales Data Steward
- **Estimated Rows**: 200 Million, growing 50M/year
- **Compliance Notes**: Order data subject to retention policies; partitioned for efficient archival.

| Column Name | Data Type | PK | FK | Not Null | Unique | Default | Check Constraint | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `order_id` | `BIGSERIAL` | Y | N | Y | Y | | | Surrogate primary key |
| `customer_id` | `BIGINT` | N | Y | Y | N | | | Foreign key to `sales.customers` |
| `order_date` | `DATE` | N | N | Y | N | `CURRENT_DATE` | | Date the order was placed |
| `order_status` | `VARCHAR(20)` | N | N | Y | N | `'PENDING'` | `IN ('PENDING', 'SHIPPED', 'DELIVERED', 'CANCELLED')` | Current status of the order |
| `total_amount` | `NUMERIC(10, 2)` | N | N | Y | N | | `> 0` | Total value of the order |

### 4.5. Indexing Strategy

| Table Name | Index Name | Indexed Columns | Index Type | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| `sales.customers` | `idx_customers_email` | `email` | B-Tree | Supports fast login lookups by email address. |
| `sales.orders` | `idx_orders_customer_id` | `customer_id` | B-Tree | Supports efficient retrieval of all orders for a given customer. |
| `sales.orders` | `idx_orders_order_date` | `order_date` | B-Tree | Supports time-based queries and reporting. |

### 4.6. Partitioning Strategy

- **Table**: `sales.orders`
- **Partitioning Type**: Range
- **Partitioning Key**: `order_date`
- **Partitioning Scheme**: One partition per quarter (e.g., `orders_q1_2026`, `orders_q2_2026`).
- **Rationale**: Improves query performance for sales reports that are typically filtered by date range. Simplifies archival of order data older than 7 years in compliance with retention policies.

### 4.7. Data Definition Language (DDL)

```sql
-- DDL for GlobalRetail Inc. Customer Orders
-- Generated on 2026-02-08

CREATE SCHEMA sales;

CREATE TABLE sales.customers (
    customer_id BIGSERIAL PRIMARY KEY,
    customer_uuid UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE sales.orders (
    order_id BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL REFERENCES sales.customers(customer_id),
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    order_status VARCHAR(20) NOT NULL DEFAULT 'PENDING' CHECK (order_status IN ('PENDING', 'SHIPPED', 'DELIVERED', 'CANCELLED')),
    total_amount NUMERIC(10, 2) NOT NULL CHECK (total_amount > 0)
)
PARTITION BY RANGE (order_date);

CREATE INDEX idx_customers_email ON sales.customers(email);
CREATE INDEX idx_orders_customer_id ON sales.orders(customer_id);
CREATE INDEX idx_orders_order_date ON sales.orders(order_date);
```

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Logical Data Model | Deliverable | **`templates/templates-KA-03-data-modeling-design.md`** |
| Data Quality Rules | Deliverable | **`templates/templates-KA-11-data-quality.md`** |
| Data Governance | Knowledge Area | **`templates/templates-KA-01-data-governance.md`** |
| MLOps Integration | Guide | **`templates/templates-KA-14-data-management-maturity.md`** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] The PDM has been formally approved by the Data Engineering Manager.
- [x] The PDM fully implements all entities and attributes from the corresponding Logical Data Model.
- [x] All data types used are from the approved `04-technology-standards.md`.
- [x] All naming conventions follow the `02-naming-conventions.md` standard.
- [ ] The generated DDL script has been successfully executed in a development environment without errors.
- [ ] A performance test has been conducted to verify the indexing and partitioning strategies meet query performance SLAs.
- [ ] The PDM has been reviewed and signed off by the DBA and Data Governance Lead.
- [ ] Compliance checks have been performed to ensure data masking, encryption, and access controls are correctly implemented.
- [ ] The PDM supports integration with DataOps and MLOps pipelines for automated deployment and testing.

### 5.2. Review Checklist

| Category | Question | Status (Pass/Fail) |
| :--- | :--- | :--- |
| **Normalization** | Have all denormalization decisions been justified and documented? | Pass |
| **Integrity** | Are primary keys, foreign keys, and check constraints correctly defined to enforce data integrity? | Pass |
| **Data Types** | Are data types the most efficient choice for the storage and usage of the data (e.g., using INT instead of BIGINT where appropriate)? | Pass |
| **Performance** | Are indexes sufficient to support all critical application queries? Is the partitioning strategy sound and scalable? | Pass |
| **Standards** | Does the model adhere to all enterprise data modeling, naming, and technology standards? | Pass |
| **Security & Privacy** | Are security controls such as encryption, masking, and access controls implemented per policy? | Pass |
| **Documentation** | Is the documentation clear, complete, and sufficient for a DBA and DataOps team to build, maintain, and deploy the database? | Pass |
| **Governance** | Does the model comply with AI governance, regulatory requirements, and data stewardship policies? | Pass |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Logical Data Model | The PDM is the physical implementation of the approved logical model. | `templates/templates-KA-03-data-modeling-design.md` |
| Modeling Standards | Provides the rules and guidelines that the PDM must follow. | `templates/templates-KA-03-data-modeling-design.md` |
| Naming Conventions | Defines the standard naming for all database objects in the PDM. | `templates/templates-KA-03-data-modeling-design.md` |
| Technology Standards | Lists the approved database technologies and data types to be used. | `templates/templates-KA-02-data-architecture.md` |
| Data Governance Policies | Defines governance and compliance requirements impacting the PDM. | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Database Standards | The PDM is a key input for the DBA to apply database configuration and operational standards. | `templates/templates-KA-04-data-storage-operations.md` |
| Source-to-Target Mapping | The PDM defines the target schema for ETL/ELT jobs. | `templates/templates-KA-06-data-integration-interoperability.md` |
| Data Dictionary | The PDM is a primary source for populating the data dictionary with technical metadata. | `templates/templates-KA-09-metadata-management.md` |
| Data Quality Rules | The PDM implements constraints and validations defined in data quality rules. | `templates/templates-KA-11-data-quality.md` |
| MLOps Pipelines | The PDM supports schema definitions for machine learning model training and deployment. | `templates/templates-KA-14-data-management-maturity.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling** | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, SqlDBM | Draw.io (for diagrams), dbt (for model-as-code), Vertabelo |
| **Database IDE** | DataGrip, DBeaver Pro, Navicat | DBeaver Community, pgAdmin, SQL Developer |
| **Version Control** | GitHub Enterprise, GitLab, Bitbucket | Git, Gitea |
| **CI/CD** | Jenkins, Azure DevOps, GitLab CI | GitHub Actions, Flyway, Liquibase |
| **DataOps Platforms** | Collibra, Informatica, Alation | OpenLineage, Apache Airflow |

### 7.2. Automation Opportunities

- **DDL Generation**: Use data modeling tools to automatically generate the DDL script from the visual model, ensuring consistency and reducing manual errors.
- **Schema Deployment**: Integrate the DDL script into CI/CD pipelines using tools like Flyway or Liquibase for automated, version-controlled deployment of schema changes across environments (dev, test, prod).
- **Documentation Generation**: Automate generation of documentation sections (e.g., table specifications) by reverse-engineering the database or parsing the DDL.
- **Model-as-Code**: Define the physical model entirely as code using tools like dbt, enabling version control, automated testing, and integration with data transformation and MLOps workflows.
- **Compliance Automation**: Integrate automated checks for compliance with data governance and AI governance policies during schema deployment.
- **Monitoring and Alerting**: Use tools to monitor schema changes, data quality, and performance metrics post-deployment.

---

## 8. References

- **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge (2nd Edition)*. 2017. Chapter 5, "Data Modeling and Design".
- **[2]** DAMA International. *DAMA-DMBOK 3.0 (Draft and Community Edition)*. 2025. Emerging best practices in data modeling and AI governance.
- **[3]** Internal Document: `role-definitions.md`
- **[4]** Internal Document: `templates/templates-KA-02-data-architecture.md`
- **[5]** Internal Document: `templates/templates-KA-03-data-modeling-design.md`
- **[6]** EU AI Act and GDPR Compliance Guidelines, 2024.
- **[7]** MLOps and DataOps Integration Guide, `templates/templates-KA-14-data-management-maturity.md`
- **[8]** Data Mesh and Data Fabric Architecture Patterns, Industry Whitepaper, 2024.


---

# Entity Definitions


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
  - [3.2. Core Definition](#32-core-definition)
  - [3.3. Aliases and Synonyms](#33-aliases-and-synonyms)
  - [3.4. Business Rules](#34-business-rules)
  - [3.5. Identifying Attributes (Natural and Surrogate Keys)](#35-identifying-attributes-natural-and-surrogate-keys)
  - [3.6. Relationships](#36-relationships)
  - [3.7. Notes and Comments](#37-notes-and-comments)
  - [3.8. Spreadsheet Template](#38-spreadsheet-template)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Core Definition](#42-core-definition)
  - [4.3. Aliases and Synonyms](#43-aliases-and-synonyms)
  - [4.4. Business Rules](#44-business-rules)
  - [4.5. Identifying Attributes (Natural and Surrogate Keys)](#45-identifying-attributes-natural-and-surrogate-keys)
  - [4.6. Relationships](#46-relationships)
  - [4.7. Notes and Comments](#47-notes-and-comments)
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

An **Entity Definition** is a formal, detailed description of a fundamental "thing" of interest to the business, such as a person, place, object, event, or concept, whose data is captured and stored. It represents a class of real-world objects and serves as a cornerstone of a data model. The purpose of creating standardized entity definitions is to establish a shared, unambiguous understanding of key business concepts across the organization. This clarity is essential for developing accurate data models, ensuring data quality, and enabling effective communication between business and technical stakeholders.

Entity definitions underpin not only traditional data modeling efforts but also emerging paradigms such as data mesh and data fabric architectures, where decentralized ownership and domain-driven design require clear, authoritative definitions to maintain interoperability and governance. Furthermore, with the rise of AI and machine learning initiatives, precise entity definitions contribute to AI governance by ensuring that data inputs are well-understood, consistent, and compliant with regulatory requirements such as the EU AI Act, GDPR, HIPAA, and CCPA.

> The Entity Definition answers the fundamental question: *"What exactly is a [Customer/Product/Order], and what does it represent in our business context?"*

As DAMA-DMBOK 3.0 evolves, entity definitions are expected to incorporate richer metadata, including lineage, data contracts, and stewardship attributes, supporting agentic data stewardship and integration with MLOps/DataOps pipelines.

### 1.2. Scope

**Per Product** — Entity Definitions are typically created for each data product or project. While some core entities (e.g., Customer, Employee) may have enterprise-wide definitions, most are defined within the specific context of the data model they belong to.

In modern data architectures, entity definitions may also be scoped to domains in a data mesh or to layers in a data lakehouse, reflecting the distributed nature of data ownership and consumption. This contextualization supports data product managers and CAIOs in aligning data assets with business capabilities and AI initiatives.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The charter and stewardship plan define the ownership and accountability for approving and maintaining entity definitions, critical for compliance with data and AI governance frameworks. |
| KA-09: Metadata Management | Entity definitions are a critical type of business metadata, managed within a metadata repository or data catalog, often integrated with data contracts and data product metadata. |
| KA-11: Data Quality | Clear entity definitions are a prerequisite for assessing and ensuring the quality of data; they define what "correct" data looks like and inform data validation and monitoring processes. |
| KA-02: Data Architecture | Entity definitions are the building blocks of the Enterprise Data Model and Subject Area Models, supporting modern architectures such as data mesh, data fabric, and lakehouse. |
| KA-06: Data Security and Privacy | Entity definitions help identify sensitive data elements and support compliance with privacy regulations and AI ethics policies. |
| KA-10: Data Operations (DataOps) | Entity definitions provide foundational context for automation in data pipelines, MLOps, and FinOps, enabling consistent data handling and lineage tracking. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately answerable for the completeness, accuracy, and quality of all entity definitions within a data product or domain. Ensures alignment with governance policies and enterprise standards. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Responsible for drafting, documenting, and maintaining the entity definitions as part of the data modeling process, incorporating inputs from business and technical stakeholders. |
| **S (Supportive)** | Data Steward (D-Steward) | Supports the process by providing the official business definition, validating accuracy, and ensuring alignment with business usage and compliance requirements. |
| **C (Consulted)** | Subject Matter Expert (SME), Metadata Analyst (Meta Analyst), AI Ethics Officer | Consulted to provide deep business context, metadata strategy alignment, and ethical considerations for AI-related data usage. |
| **I (Informed)** | Data Analyst (D-Analyst), Data Product Manager, MLOps Engineer | Informed of the final definitions to ensure correct interpretation and use of the data in analytics, AI models, and operational pipelines. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Entity Definition | D-Modeler | SME, D-Steward | DE Mgr |
| Business Rules | D-Modeler, SME | D-Steward | DE Mgr |
| Identifying Attributes | D-Modeler | Data Architect (D-Arch) | DE Mgr |
| Relationships | D-Modeler | D-Arch | DE Mgr |
| Aliases and Synonyms | D-Modeler, Meta Analyst | SME | DE Mgr |
| Notes and Comments | D-Modeler | SME, D-Steward | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating an Entity Definition document. This template should be filled out for each major entity within a data model.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Entity Name | [Official Business Name of the Entity] |
| Data Model | [Name/ID of the Data Model or Data Product] |
| Version | [e.g., 1.0] |
| Status | [e.g., Draft, In Review, Approved] |
| Owner | [Data Steward Name] |
| Stewardship Domain | [Domain or Data Product Ownership] |
| Last Updated | [Date] |

### 3.2. Core Definition

> *Provide a clear, concise, and unambiguous definition of the entity. The definition should be understandable to a business audience and explain the entity's role in the business process.*

**Input needed**: Business glossary, interviews with SMEs, AI governance policies, data product documentation.  
**Who fills this**: D-Modeler, with input from D-Steward, SME, and AI Ethics Officer if applicable.

[Insert the complete business definition of the entity here.]

Include references to any relevant AI use cases or compliance considerations if the entity's data is used in AI/ML models or governed under AI regulations.

### 3.3. Aliases and Synonyms

> *List any alternative names, acronyms, or synonyms used to refer to this entity in different business units, systems, or data products. This helps map business language to the data model.*

**Input needed**: System documentation, user interviews, metadata catalogs.  
**Who fills this**: D-Modeler, Meta Analyst.

| Alias/Synonym | Context/System |
| :--- | :--- |
| [e.g., Client] | [e.g., Sales CRM] |
| [e.g., Member] | [e.g., Loyalty Program] |

Documenting aliases supports data mesh interoperability and helps avoid semantic confusion in multi-cloud or multi-domain environments.

### 3.4. Business Rules

> *Document the key business rules that govern the entity's existence, behavior, and state. These are not data validation rules, but higher-level operational constraints.*

**Input needed**: Business process documentation, policy documents, AI governance guidelines.  
**Who fills this**: SME, D-Steward, D-Modeler.

- [e.g., A Customer must have at least one associated Order to be considered 'Active'.]
- [e.g., An Order cannot be created for a Product that is out of stock.]
- [e.g., Personal data fields must comply with GDPR retention policies.]

Include any AI-specific constraints such as data usage restrictions or ethical considerations.

### 3.5. Identifying Attributes (Natural and Surrogate Keys)

> *Specify the attribute or set of attributes that uniquely identify an instance of the entity. Document both natural keys (business-defined identifiers) and surrogate keys (system-generated identifiers).*

**Input needed**: Conceptual and Logical Data Models, system design documents.  
**Who fills this**: D-Modeler.

| Key Type | Attribute(s) | Description |
| :--- | :--- | :--- |
| Natural Key | [e.g., Social Security Number] | [e.g., Government-issued identifier for a citizen.] |
| Surrogate Key | [e.g., CustomerID] | [e.g., System-generated unique identifier.] |

Clarify stability and uniqueness guarantees, especially important for data contracts and AI model training data consistency.

### 3.6. Relationships

> *Describe the entity's relationships with other entities in the data model. For each relationship, specify the related entity, the cardinality (e.g., one-to-many), and a brief description of the business rule it represents.*

**Input needed**: Logical Data Model, relationship documentation.  
**Who fills this**: D-Modeler.

| Related Entity | Cardinality | Description |
| :--- | :--- | :--- |
| [e.g., Order] | One-to-Many (1:M) | [e.g., A Customer can place many Orders.] |
| [e.g., Address] | Many-to-Many (M:M) | [e.g., A Customer can have multiple Addresses (Shipping, Billing), and an Address can be associated with multiple Customers.] |

Include notes on relationship ownership and stewardship, particularly in federated or mesh environments.

### 3.7. Notes and Comments

> *Include any additional information, historical context, or implementation considerations that are not captured in the other sections. This can include notes on data quality, lineage, AI model usage, or future state plans.*

**Input needed**: Design documents, meeting notes, AI governance records.  
**Who fills this**: D-Modeler, SME.

[Insert any relevant notes or comments here.]

Examples:

- Data lineage considerations for this entity in multi-cloud environments.
- Known data quality issues or remediation plans.
- AI model dependencies or ethical considerations.

---

### 3.8. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-03_entity-definitions.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

---

## 4. Example

> *This example illustrates the definition for the 'Product' entity at the fictional company, GlobalRetail Inc.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Entity Name | Product |
| Data Model | Enterprise Product Master |
| Version | 2.1 |
| Status | Approved |
| Owner | Jane Doe, Product Data Steward |
| Stewardship Domain | Retail Product Management |
| Last Updated | 2024-05-15 |

### 4.2. Core Definition

A **Product** represents a unique, sellable item that GlobalRetail Inc. offers for sale to its customers through any of its sales channels (online, in-store, catalog). This includes physical goods, digital downloads, and service contracts. Each product has a unique Stock Keeping Unit (SKU) and is associated with a specific brand and product category.

This entity supports AI-driven pricing optimization and recommendation engines, requiring consistent and accurate definitions to ensure model reliability and compliance with pricing regulations.

### 4.3. Aliases and Synonyms

| Alias/Synonym | Context/System |
| :--- | :--- |
| Item | Warehouse Management System (WMS) |
| SKU | Point of Sale (POS), Inventory System |
| Offering | Marketing Campaign Management |

### 4.4. Business Rules

- A Product must be assigned to a primary product category.
- A Product cannot be made available for sale until its status is 'Active'.
- The retail price of a Product can be overridden by a promotional price, but cannot be sold below the defined cost price.
- Every physical product must have weight and dimensions recorded before it can be shipped.
- Product data used in AI models must exclude any items flagged as restricted under compliance policies.

### 4.5. Identifying Attributes (Natural and Surrogate Keys)

| Key Type | Attribute(s) | Description |
| :--- | :--- | :--- |
| Natural Key | SKU | The unique Stock Keeping Unit assigned to the product for inventory tracking. |
| Surrogate Key | ProductID | System-generated unique identifier used in all internal databases. |

### 4.6. Relationships

| Related Entity | Cardinality | Description |
| :--- | :--- | :--- |
| Supplier | Many-to-One (M:1) | Each Product is sourced from one primary Supplier. |
| Product Category | Many-to-One (M:1) | Each Product belongs to one primary Product Category. |
| Order Line Item | One-to-Many (1:M) | A Product can appear on many Order Line Items. |
| Warehouse Inventory | One-to-Many (1:M) | A Product's stock is held in multiple Warehouse Inventory locations. |

### 4.7. Notes and Comments

- The 'Product' entity was redesigned in Q3 2023 to support digital products and services. Legacy product data from before this date may not have a value for the 'DigitalAssetURL' attribute.
- Future plans include adding support for bundled products (kits), which will require a self-referencing relationship.
- Product data is integrated into AI recommendation engines; therefore, data quality and timeliness are critical.
- Data contracts define SLAs for product data updates to support real-time pricing models.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Business Glossary | Deliverable | [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) |
| Conceptual Data Model | Deliverable | [templates/templates-KA-03-data-modeling-design.md](templates/templates-KA-03-data-modeling-design.md) |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The entity definition is clear, concise, and written in plain business language.
- [ ] The entity has a designated Data Steward as its owner, with documented stewardship domain.
- [ ] All aliases and synonyms used across major systems and domains are documented.
- [ ] At least one unique identifier (natural or surrogate key) is defined, with stability and uniqueness considerations.
- [ ] All critical business rules governing the entity are listed, including compliance and AI governance rules if applicable.
- [ ] All major relationships to other entities are documented with correct cardinality and stewardship notes.
- [ ] The definition has been reviewed and approved by the Data Steward, SME, and relevant governance roles (e.g., AI Ethics Officer).
- [ ] The entity definition aligns with enterprise metadata standards and integrates with data catalog and data product metadata.
- [ ] The document includes notes on data lineage, quality, and any AI or regulatory considerations.

### 5.2. Review Checklist

| # | Question | Reviewer Checks (Y/N) |
|:--|:---|:---:|
| 1 | Is the definition atomic and not overlapping with other entities? | Y |
| 2 | Does the definition accurately reflect how the business uses this concept? | Y |
| 3 | Are the identifying attributes truly unique and stable? | Y |
| 4 | Are the relationships described consistent with the logical data model? | Y |
| 5 | Is the definition free of technical jargon where possible? | Y |
| 6 | Are AI governance and compliance considerations addressed where relevant? | Y |
| 7 | Has the definition been integrated with metadata management tools and data catalogs? | Y |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Output | Relationship |
| :--- | :--- |
| [templates/templates-KA-03-data-modeling-design.md](templates/templates-KA-03-data-modeling-design.md) | Provides the high-level entities that require detailed definition. |
| [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md) | Provides the source for many core entity definitions. |
| **templates/templates-KA-09-metadata-management.md** | Provides metadata standards and integration guidelines. |

### 6.2. Consumers (This Output is Input for)

| Output | Relationship |
| :--- | :--- |
| [templates/templates-KA-03-data-modeling-design.md](templates/templates-KA-03-data-modeling-design.md) | Provides the context for defining the attributes that belong to each entity. |
| [templates/templates-KA-09-metadata-management.md](templates/templates-KA-09-metadata-management.md) | The entity definitions form a core component of the business data dictionary. |
| [templates/templates-KA-02-data-architecture.md](templates/templates-KA-02-data-architecture.md) | The collection of approved entity definitions informs the creation of the enterprise-wide data model. |
| **templates/templates-KA-01-data-governance.md** | Entity definitions support the creation and enforcement of data contracts. |
| **templates/templates-KA-10-reference-master-data.md** | Entity definitions inform data pipelines and AI model training data specifications. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| Data Modeling Tools | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, Sparx Enterprise Architect | OpenModelSphere, Draw.io (for basic diagrams), Archi |
| Data Catalogs | Collibra, Alation, Informatica EDC, Microsoft Purview | Amundsen, DataHub, OpenMetadata |
| Wiki/Collaboration | Confluence, SharePoint | BookStack, DokuWiki |
| AI Governance Platforms | IBM Watson OpenScale, Fiddler AI | AI Fairness 360 (AIF360), TensorFlow Model Analysis |

### 7.2. Automation Opportunities

- **Reverse Engineering**: Entity definitions can be partially auto-generated by reverse-engineering existing database schemas. The tool can extract table names and columns, which a Data Modeler then refines into business-friendly definitions.
- **Data Catalog Integration**: When a data model is checked into a version control system, a CI/CD pipeline can be triggered to parse the model file (e.g., an XML or DDL file) and automatically push the entity and attribute definitions to the enterprise data catalog via its API.
- **Glossary Sync**: Entity definitions can be synchronized with the Business Glossary. When a term is updated in the glossary, it can automatically update the corresponding entity definition in the data catalog or modeling tool.
- **AI Governance Linkage**: Automation can link entity definitions to AI model metadata, ensuring that any changes in entity definitions trigger reviews of AI model inputs and outputs for compliance.
- **Data Contract Enforcement**: Automated validation of entity definitions against data contracts can ensure that data producers and consumers adhere to agreed standards.
- **Change Impact Analysis**: Tools can analyze changes in entity definitions and notify stakeholders, including Data Product Managers and MLOps Engineers, to assess impact on data products and AI models.

---

## 8. References

- [1] DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 5)  
- [2] DAMA International. *DAMA-DMBOK 3.0 (Draft)*. Community-driven update, 2024-2025.  
- [3] Internal Document: [templates/templates-KA-01-data-governance.md](templates/templates-KA-01-data-governance.md)  
- [4] Internal Document: [templates/templates-KA-03-data-modeling-design.md](templates/templates-KA-03-data-modeling-design.md)  
- [5] EU AI Act and GDPR Compliance Guidelines, 2023.  
- [6] Data Mesh Principles and Practices, Zhamak Dehghani, ThoughtWorks, 2020.  
- [7] Data Fabric Architecture Overview, Gartner Research, 2023.  
- [8] AI Governance Maturity Model, Forrester Research, 2024.


---

# Attribute Definitions


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Attribute Identifier](#31-attribute-identifier)
  - [3.2. Business Definition](#32-business-definition)
  - [3.3. Technical Specification](#33-technical-specification)
  - [3.4. Value Domain](#34-value-domain)
  - [3.5. Data Quality](#35-data-quality)
  - [3.6. Governance and Security](#36-governance-and-security)
- [4. Example](#4-example)
  - [**Example 1: ProductSKU**](#example-1-productsku)
  - [**Example 2: ProductLaunchDate**](#example-2-productlaunchdate)
  - [4.4. Related Concepts and Guides](#44-related-concepts-and-guides)
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

**Attribute Definitions** are the detailed, unambiguous specifications for each individual data attribute within a data model. An attribute represents a single property or characteristic of an entity. This output provides a comprehensive dictionary that describes the business meaning, technical format, and valid values for each attribute. The primary purpose of defining attributes is to ensure consistency, clarity, and shared understanding of data across the organization. It is the most granular level of data modeling and is critical for preventing data quality issues, facilitating accurate data integration, and enabling effective data governance.

In the evolving landscape of data management, Attribute Definitions also play a pivotal role in supporting **AI governance**, ensuring that data attributes feeding AI/ML models are well-understood, trustworthy, and compliant with regulatory requirements such as the **EU AI Act**, **GDPR**, **HIPAA**, and **CCPA**. They are foundational for implementing **data contracts** and defining **data products** in modern architectures like **Data Mesh** and **Data Fabric**, where decentralized ownership and interoperability are key.

> Attribute Definitions answer the question: *"What, precisely, does this specific data field mean, what form does it take, and what are the rules that govern it?"*

Looking forward to **DAMA-DMBOK 3.0**, Attribute Definitions will increasingly integrate with AI lifecycle management (MLOps), data product management, and agentic stewardship frameworks, reflecting the shift towards automated, policy-driven data governance.

### 1.2. Scope

**Per Product** — Attribute Definitions are created for each data product. While some attributes may be standardized globally (e.g., via a master data model or enterprise-wide reference data), their specific implementation, context, constraints, and governance details are documented within the scope of the data product they belong to. This approach aligns with **Data Mesh principles**, emphasizing domain-oriented decentralized ownership while maintaining enterprise-wide interoperability.

Attributes defined here support not only traditional relational and dimensional models but also modern **cloud-native** data platforms, **lakehouse architectures**, and **multi-cloud** environments, where attribute metadata must be portable, interoperable, and machine-readable to enable automation and AI-driven insights.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-09: Metadata Management | Attribute Definitions are a critical form of business and technical metadata, serving as a core input for the corporate Data Dictionary and Business Glossary. They enable metadata-driven automation and lineage tracking. |
| KA-11: Data Quality | The rules and constraints defined for attributes (e.g., data type, valid ranges) are the foundation for data quality rules and validation checks, essential for both operational and analytical data quality. |
| KA-10: Reference and Master Data | Attributes often derive their valid values from reference data sets (e.g., a list of country codes). This output links attributes to the appropriate reference data standards and master data entities. |
| KA-06: Data Integration | Clear attribute definitions are essential for creating accurate source-to-target mappings and transformation rules during data integration, especially in complex multi-cloud and hybrid environments. |
| KA-01: Data Governance | Attribute Definitions support governance policies by embedding stewardship, classification, and compliance metadata, critical for AI governance and regulatory adherence. |
| KA-05: Data Security | Attributes include classification and sensitivity metadata, supporting data protection, masking, and anonymization strategies. |
| KA-12: Data Architecture | Attribute definitions inform physical and logical data models, supporting architecture decisions in modern data platforms including Data Mesh and Lakehouse designs. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately answerable for the completeness, accuracy, and quality of the attribute definitions for a given data product. Ensures resources and tooling are available for the modeling effort and that definitions align with enterprise standards and AI governance policies. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Leads the process of discovering, analyzing, and documenting all attribute definitions. Creates and maintains the official documentation and ensures technical specifications are consistent with physical implementations and data architecture. |
| **S (Supportive)** | Data Steward (D-Steward) | Provides the business context, definitions, and rules for attributes within their domain. Validates the accuracy and completeness of the documented definitions and ensures alignment with data governance and compliance requirements. |
| **C (Consulted)** | Subject Matter Expert (SME), Metadata Analyst (Meta Analyst), AI Ethics Officer | SMEs provide deep business knowledge about specific attributes. Metadata Analysts ensure definitions align with enterprise metadata standards and are captured in the data catalog. AI Ethics Officers consult on attributes related to sensitive or regulated data, ensuring ethical considerations are addressed. |
| **I (Informed)** | Data Analyst (D-Analyst), Data Product Manager | As primary consumers of the data, Data Analysts and Data Product Managers are kept informed of the final attribute definitions to ensure their analyses and product designs are accurate and compliant. |

### 2.2. Section-Level RASCI

| Activity / Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Business Definition & Rules | D-Steward | SME, AI Ethics Officer | D-Steward |
| Technical Specification | D-Modeler | Data Architect (D-Arch), DBA | DE Mgr |
| Data Quality Rules | D-Modeler | Data Quality Analyst (DQ Analyst) | D-Steward |
| Linkage to Reference Data | D-Modeler | Metadata Analyst (Meta Analyst) | D-Steward |
| Governance and Security | D-Steward | Data Security Officer (DSO), AI Ethics Officer | DE Mgr |

---

## 3. Template

> *The following is the standardized template for documenting Attribute Definitions. This template should be completed for each attribute within an entity. Use this structure to ensure all critical aspects of an attribute are captured.*

### 3.1. Attribute Identifier

> *Provide basic identifying information for the attribute.*

| Field | Value |
| :--- | :--- |
| **Entity Name** | [e.g., Product] |
| **Attribute Name (Logical)** | [e.g., ProductStatus] |
| **Attribute Name (Physical)** | [e.g., PROD_STAT_CD] |
| **Attribute ID** | [e.g., ATTR-PRD-005] |
| **Attribute Owner** | [Name of responsible Data Steward or Product Manager] |
| **Attribute Version** | [Version number or date of last update] |

### 3.2. Business Definition

> *Describe the attribute in clear business terms. This section should be understandable by non-technical stakeholders.*

**Input needed**: Business requirements, SME interviews, glossary terms, AI governance policies.  
**Who fills this**: Data Steward, with input from SMEs and AI Ethics Officer.

- **Description**: [A full-sentence description of the attribute's meaning, purpose, and business context.]
- **Business Rules**: [List any business rules that govern the attribute's value or behavior. e.g., "A ProductStatus can only be set to 'Discontinued' if the AvailableInventory is zero."]
- **Regulatory Considerations**: [Specify any compliance or regulatory constraints impacting the attribute, e.g., GDPR restrictions, EU AI Act requirements.]

### 3.3. Technical Specification

> *Detail the technical characteristics of the attribute as it would be implemented in a physical database or data structure.*

**Input needed**: Logical data model, database standards, technology standards, cloud platform specifications.  
**Who fills this**: Data Modeler.

| Property | Value | Description |
| :--- | :--- | :--- |
| **Data Type** | [e.g., VARCHAR, INTEGER, DECIMAL, TIMESTAMP] | The physical data type of the attribute. |
| **Length/Precision** | [e.g., 50, (10,2)] | The size of the attribute (e.g., number of characters, total digits and decimal places). |
| **Primary Key?** | [Yes/No] | Is this attribute part of the entity's primary key? |
| **Foreign Key?** | [Yes/No] | Does this attribute reference the primary key of another entity? |
| **Referenced Entity** | [If Foreign Key, specify the entity, e.g., 'LookupStatus'] | The entity this foreign key points to. |
| **Nullable?** | [Yes/No] | Can this attribute have a null value? |
| **Default Value** | [Specify default, e.g., 'Active' or NULL] | The value assigned if no value is provided. |
| **Physical Storage** | [e.g., Column name, table, file path] | Location or physical implementation details. |
| **Cloud/Platform Specifics** | [e.g., Partition keys, encryption at rest] | Any platform-specific technical notes. |

### 3.4. Value Domain

> *Define the set of all possible valid values for the attribute. This is crucial for data quality and user interface design.*

**Input needed**: Reference data standards, SME knowledge, data contracts.  
**Who fills this**: Data Steward, documented by Data Modeler.

| Property | Value | Description |
| :--- | :--- | :--- |
| **Domain Type** | [Range, Enumerated List, Pattern, Unconstrained] | The type of value domain. |
| **Value Range** | [e.g., 0 to 9999.99] | For numeric types, the minimum and maximum allowed values. |
| **Enumerated List** | [List of valid codes and their meanings, e.g., {'A':'Active', 'I':'Inactive'}] | For coded values, the complete list of allowed codes and their definitions. |
| **Format/Pattern** | [e.g., YYYY-MM-DD, (###) ###-####] | For strings, the required regular expression or format mask. |
| **Reference Data Source** | [e.g., `KA-10/03-reference-data-standards.md#CountryCodes`] | If the list is managed as official reference data, link to it here. |
| **Data Contract Link** | [If applicable, link to data contract specifying value domain] | Supports automated validation and SLA enforcement. |

### 3.5. Data Quality

> *Specify the rules that define a high-quality value for this attribute. These rules are often implemented as automated checks.*

**Input needed**: Data quality requirements, business rules, AI governance policies.  
**Who fills this**: Data Modeler, in consultation with Data Quality Analyst.

| DQ Dimension | Rule Description | Validation Check Logic |
| :--- | :--- | :--- |
| **Completeness** | [e.g., Must not be null if ProductStatus is 'Active'] | `IS NOT NULL` |
| **Uniqueness** | [e.g., Must be unique within the Product entity] | `COUNT(DISTINCT value) = COUNT(value)` |
| **Conformity** | [e.g., Must conform to the specified data type and length] | `VALIDATE_DATATYPE(value, 'VARCHAR', 50)` |
| **Consistency** | [e.g., LaunchDate must be before DiscontinuedDate] | `LaunchDate < DiscontinuedDate` |
| **Accuracy** | [e.g., Must exist in the master list of approved brand names] | `EXISTS IN (SELECT brand_name FROM master_brands)` |
| **Timeliness** | [e.g., Attribute must be updated within 24 hours of change] | `TIMESTAMP_DIFF(current_time, last_update) < 24h` |
| **Lineage Traceability** | [e.g., Source system and transformation steps documented] | `LINEAGE_METADATA_PRESENT` |

### 3.6. Governance and Security

> *Detail the ownership and security classification of the attribute.*

**Input needed**: Stewardship plan, data classification scheme, AI governance framework.  
**Who fills this**: Data Steward.

| Property | Value |
| :--- | :--- |
| **Data Steward** | [Name of the assigned Data Steward] |
| **Data Owner** | [Name of business owner responsible for data] |
| **Data Classification** | [e.g., Public, Internal, Confidential, Restricted] |
| **PII/Sensitive?** | [Yes/No] |
| **Anonymization/Masking Rule** | [e.g., Mask all but last 4 digits, Hash value] |
| **Retention Policy** | [e.g., Retain for 7 years, then archive] |
| **Access Controls** | [e.g., Role-based access, encryption requirements] |
| **AI Governance Considerations** | [e.g., Attribute used in AI models subject to fairness review] |

---

### 3.7. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-03_attribute-definitions.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

## 4. Example

> *This is a realistic, filled-in example for two attributes of a 'Product' entity at a fictional company, GlobalRetail Inc.*

### **Example 1: ProductSKU**

#### 4.1. Attribute Identifier

| Field | Value |
| :--- | :--- |
| **Entity Name** | Product |
| **Attribute Name (Logical)** | ProductSKU |
| **Attribute Name (Physical)** | PROD_SKU |
| **Attribute ID** | ATTR-PRD-001 |
| **Attribute Owner** | Product Data Steward |
| **Attribute Version** | 1.3 (2024-05-15) |

#### 4.2. Business Definition

- **Description**: The ProductSKU is the unique, internal identifier for a distinct, sellable product variation (e.g., a specific size and color of a shirt). It is the primary key for identifying a product within all internal systems.
- **Business Rules**: 
  - A SKU must be assigned to every product before it can be made available for sale.
  - A SKU can never be changed or reassigned once created.
- **Regulatory Considerations**: Not subject to PII regulations but must comply with internal data retention and audit policies.

#### 4.3. Technical Specification

| Property | Value | Description |
| :--- | :--- | :--- |
| **Data Type** | VARCHAR | The physical data type of the attribute. |
| **Length/Precision** | 12 | The size of the attribute. |
| **Primary Key?** | Yes | This attribute is the primary key. |
| **Foreign Key?** | No | |
| **Referenced Entity** | N/A | |
| **Nullable?** | No | A SKU is mandatory. |
| **Default Value** | None | Must be explicitly provided. |
| **Physical Storage** | PROD_SKU column in Product table | |
| **Cloud/Platform Specifics** | Partition key in cloud data lake | |

#### 4.4. Value Domain

| Property | Value | Description |
| :--- | :--- | :--- |
| **Domain Type** | Pattern | The type of value domain. |
| **Value Range** | N/A | |
| **Enumerated List** | N/A | |
| **Format/Pattern** | `^[A-Z]{2}\d{10}$` | Two uppercase letters followed by 10 digits (e.g., SH1234567890). |
| **Reference Data Source** | N/A | |
| **Data Contract Link** | **Product SKU Data Contract** | |

#### 4.5. Data Quality

| DQ Dimension | Rule Description | Validation Check Logic |
| :--- | :--- | :--- |
| **Completeness** | Must not be null. | `IS NOT NULL` |
| **Uniqueness** | Must be unique across all products. | `COUNT(DISTINCT PROD_SKU) = COUNT(PROD_SKU)` |
| **Conformity** | Must match the `^[A-Z]{2}\d{10}$` pattern. | `REGEXP_LIKE(PROD_SKU, '^[A-Z]{2}\\d{10}$')` |
| **Timeliness** | SKU must be assigned before product activation. | `SKU_ASSIGNED_DATE <= PRODUCT_ACTIVE_DATE` |

#### 4.6. Governance and Security

| Property | Value |
| :--- | :--- |
| **Data Steward** | Product Data Steward |
| **Data Owner** | Product Line Manager |
| **Data Classification** | Internal |
| **PII/Sensitive?** | No |
| **Anonymization/Masking Rule** | N/A |
| **Retention Policy** | Retain indefinitely for audit purposes |
| **Access Controls** | Restricted to Product Management and Data Engineering teams |
| **AI Governance Considerations** | Used as a key identifier in AI models; must be stable and unique |

---

### **Example 2: ProductLaunchDate**

#### 4.1. Attribute Identifier

| Field | Value |
| :--- | :--- |
| **Entity Name** | Product |
| **Attribute Name (Logical)** | ProductLaunchDate |
| **Attribute Name (Physical)** | PROD_LAUNCH_DT |
| **Attribute ID** | ATTR-PRD-012 |
| **Attribute Owner** | Product Data Steward |
| **Attribute Version** | 2.0 (2024-05-20) |

#### 4.2. Business Definition

- **Description**: The date on which a product is first made available for sale to customers on the public website.
- **Business Rules**: 
  - The launch date cannot be in the past relative to the current date at the time of entry.
  - The launch date must be on or after the date the product record was created.
- **Regulatory Considerations**: No PII involved; however, date accuracy is critical for compliance with promotional and advertising regulations.

#### 4.3. Technical Specification

| Property | Value | Description |
| :--- | :--- | :--- |
| **Data Type** | DATE | The physical data type of the attribute. |
| **Length/Precision** | N/A | |
| **Primary Key?** | No | |
| **Foreign Key?** | No | |
| **Referenced Entity** | N/A | |
| **Nullable?** | Yes | A launch date can be pending. |
| **Default Value** | NULL | |
| **Physical Storage** | PROD_LAUNCH_DT column in Product table | |
| **Cloud/Platform Specifics** | Indexed for query performance | |

#### 4.4. Value Domain

| Property | Value | Description |
| :--- | :--- | :--- |
| **Domain Type** | Range | The type of value domain. |
| **Value Range** | `CURRENT_DATE` to `2999-12-31` | Cannot be a past date relative to entry time. |
| **Enumerated List** | N/A | |
| **Format/Pattern** | `YYYY-MM-DD` | ISO 8601 date format. |
| **Reference Data Source** | N/A | |

#### 4.5. Data Quality

| DQ Dimension | Rule Description | Validation Check Logic |
| :--- | :--- | :--- |
| **Completeness** | Must not be null for any product with a status of 'Active'. | `CASE WHEN PROD_STAT_CD = 'A' THEN PROD_LAUNCH_DT IS NOT NULL ELSE TRUE END` |
| **Consistency** | Must be earlier than the `ProductDiscontinuedDate` if it exists. | `PROD_LAUNCH_DT < PROD_DISCONTINUED_DT` |
| **Accuracy** | Must be a valid calendar date. | `IS_DATE(PROD_LAUNCH_DT)` |
| **Timeliness** | Date must be updated promptly when product status changes. | `TIMESTAMP_DIFF(current_time, last_update) < 48h` |

#### 4.6. Governance and Security

| Property | Value |
| :--- | :--- |
| **Data Steward** | Product Data Steward |
| **Data Owner** | Product Line Manager |
| **Data Classification** | Public |
| **PII/Sensitive?** | No |
| **Anonymization/Masking Rule** | N/A |
| **Retention Policy** | Retain as long as product is active |
| **Access Controls** | Publicly accessible metadata |
| **AI Governance Considerations** | Used in forecasting models; must be accurate and timely |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Contracts | Concept | [data-contracts.md](references/concepts-modern-paradigms.md) |
| Data Governance Roles and Responsibilities | Deliverable | **templates/templates-KA-01-data-governance.md** |
| Naming Conventions | Deliverable | **templates/templates-KA-03-data-modeling-design.md** |
| Data Classification Scheme | Deliverable | **templates/templates-KA-05-data-security.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria Checklist

- [x] Every attribute in the logical data model has a corresponding definition file.
- [x] The business definition is clear, unambiguous, and written in non-technical language.
- [x] All technical specifications (data type, length, precision) are documented and align with database and platform standards.
- [x] The value domain is explicitly defined (list, range, or pattern).
- [x] Nullability (i.e., optionality) is clearly stated and justified.
- [x] At least one data quality rule is defined for each attribute, covering multiple DQ dimensions.
- [x] Security and governance properties (steward, classification, PII status) are assigned.
- [x] Regulatory and AI governance considerations are documented where applicable.
- [x] The definition has been reviewed and approved by the assigned Data Steward and relevant governance roles.
- [x] Attribute definitions are linked to related data contracts and data products where applicable.
- [x] Definitions support automation and integration with metadata management and data catalog tools.

### 5.2. Review Checklist

| Review Area | Question | Expected Outcome |
| :--- | :--- | :--- |
| **Clarity** | Can a business user understand what this attribute means without further explanation? | Yes, the business definition is self-explanatory and free of jargon. |
| **Precision** | Are the technical details (data type, length, precision) specific enough to build a database table or data product from? | Yes, there is no ambiguity for a DBA, developer, or data engineer. |
| **Testability** | Can the data quality rules be translated into automated tests? | Yes, the rules are logical, specific, measurable, and executable. |
| **Consistency** | Does the attribute name and definition align with the Business Glossary, enterprise naming conventions, and reference data standards? | Yes, terminology is used consistently across all documentation. |
| **Necessity** | Is this attribute truly required? Does it represent a unique piece of information? | Yes, the attribute is not redundant or duplicative with other attributes. |
| **Governance** | Are stewardship, ownership, classification, and security metadata complete and accurate? | Yes, governance metadata supports compliance and auditability. |
| **AI Governance** | Are attributes used in AI/ML models identified and documented with ethical and compliance considerations? | Yes, AI governance notes are included where relevant. |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| # | Output Name | File Path | Description |
|:--|:---|:---|:---|
| 1 | Entity Definitions | `templates/templates-KA-03-data-modeling-design.md` | Provides the parent entity for which the attributes are being defined. |
| 2 | Logical Data Model | `templates/templates-KA-03-data-modeling-design.md` | The source diagram that identifies the attributes that need to be defined. |
| 3 | Business Glossary | `templates/templates-KA-09-metadata-management.md` | Provides standard business terms and definitions for attributes. |
| 4 | Data Contracts | `templates/templates-KA-09-metadata-management.md` | Defines formal agreements on data attributes, quality, and usage. |

### 6.2. Consumers (Outputs)

| # | Output Name | File Path | Description |
|:--|:---|:---|:---|
| 1 | Relationship Documentation | `templates/templates-KA-03-data-modeling-design.md` | Uses attribute definitions to specify the foreign key attributes involved in relationships. |
| 2 | Data Dictionary | `templates/templates-KA-09-metadata-management.md` | Attribute definitions are a primary source of content for the enterprise data dictionary. |
| 3 | Reference Data Standards | `templates/templates-KA-10-reference-master-data.md` | Attribute definitions specify which reference data sets should be used for an attribute's valid values. |
| 4 | Data Quality Reports | `templates/templates-KA-11-data-quality.md` | Data quality rules defined here feed into automated quality monitoring and reporting. |
| 5 | Data Product Catalog | `templates/templates-KA-09-metadata-management.md` | Attribute definitions support the description and management of data products. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling Tools** | Erwin Data Modeler, SAP PowerDesigner, ER/Studio | `dbt` (for documenting models), Draw.io (for diagrams), Archi |
| **Data Catalogs** | Collibra, Alation, Informatica EDC | Amundsen, DataHub, OpenMetadata |
| **Data Quality Platforms** | Informatica Data Quality, Talend Data Quality | Great Expectations, Deequ |
| **Collaboration** | Confluence, SharePoint | Wiki.js, BookStack |
| **AI Governance Platforms** | IBM Watson OpenScale, Microsoft Purview | Open source AI fairness and explainability toolkits |

### 7.2. Automation Opportunities

- **Metadata Ingestion**: Automatically scan database schemas (DDL) and data lake metadata to create initial drafts of attribute definitions, pre-populating technical specifications like data type and length.
- **Glossary Integration**: Link attribute definitions directly to terms in the Business Glossary. When a glossary term is updated, automatically flag related attribute definitions for review.
- **Data Quality Rule Generation**: Automatically generate data quality test scripts (e.g., SQL queries, dbt tests) based on the rules defined in the 'Data Quality' section.
- **Documentation Generation**: Automatically generate user-friendly documentation (e.g., HTML pages, dashboards) from the master attribute definition files stored in version control.
- **AI Governance Integration**: Link attribute metadata to AI model feature stores and governance tools to ensure traceability, fairness, and compliance.
- **Data Contract Enforcement**: Use attribute definitions to enforce data contracts via automated validation and alerting in data pipelines.
- **Change Impact Analysis**: Automated detection of changes in attribute definitions triggering impact assessments across data products and AI models.

---

## 8. References

- [1] DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 5)
- [2] DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Expected Release June 2025. Community-driven rebuild emphasizing AI governance, data mesh, and data products.
- [3] Internal Document: `templates/templates-KA-01-data-governance.md`
- [4] Internal Document: `templates/templates-KA-03-data-modeling-design.md`
- [5] Internal Document: `templates/templates-KA-05-data-security.md`
- [6] Internal Document: `templates/templates-KA-09-metadata-management.md`
- [7] EU AI Act and GDPR Compliance Guidelines, 2023 Edition
- [8] Data Mesh Principles and Data Product Management, Zhamak Dehghani, ThoughtWorks, 2020


---

# Relationship Documentation


## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Definition and Purpose](#11-definition-and-purpose)
  - [1.2. Scope](#12-scope)
  - [1.3. Related Knowledge Areas](#13-related-knowledge-areas)
- [2. RASCI Assignment](#2-rasci-assignment)
  - [2.1. Output-Level RASCI](#21-output-level-rasci)
  - [2.2. Section-Level RASCI](#22-section-level-rasci)
- [3. Template](#3-template)
  - [3.1. Relationship Header](#31-relationship-header)
  - [3.2. Participating Entities](#32-participating-entities)
  - [3.3. Relationship Description](#33-relationship-description)
  - [3.4. Cardinality and Optionality](#34-cardinality-and-optionality)
  - [3.5. Referential Integrity and Constraints](#35-referential-integrity-and-constraints)
  - [3.6. Relationship Type](#36-relationship-type)
- [4. Example](#4-example)
  - [4.1. Relationship Header](#41-relationship-header)
  - [4.2. Participating Entities](#42-participating-entities)
  - [4.3. Relationship Description](#43-relationship-description)
  - [4.4. Cardinality and Optionality](#44-cardinality-and-optionality)
  - [4.5. Referential Integrity and Constraints](#45-referential-integrity-and-constraints)
  - [4.6. Relationship Type](#46-relationship-type)
- [4.4. Related Concepts and Guides](#44-related-concepts-and-guides)
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

**Relationship Documentation** is the formal process and artifact that defines the associations between entities within a data model. It captures the underlying business rules that govern how entities interact, including cardinality (the number of instances of one entity that relate to another) and optionality (whether participation in the relationship is mandatory or optional). This documentation is essential for ensuring clarity and consistency in data models, enabling both business and technical stakeholders to understand the structural and contextual connections within the data landscape.

In modern data management environments—characterized by distributed data architectures such as Data Mesh and Data Fabric, cloud-native deployments, and AI-driven automation—relationship documentation serves as a foundational element for enabling interoperability, governance, and compliance. It supports the creation of data products with well-defined interfaces and contracts, which are critical for scalable, federated data ecosystems.

> The primary purpose of Relationship Documentation is to translate complex and often implicit business rules into a clear, unambiguous, and verifiable format. This facilitates alignment across stakeholders, supports automated validation and enforcement of data integrity, and ensures that data models accurately reflect operational realities and regulatory requirements, including emerging mandates such as the EU AI Act alongside GDPR, HIPAA, and CCPA.

### 1.2. Scope

**Per Product** — Relationship Documentation is created for each individual data product or data domain. While enterprise-wide standards and templates for relationship types and definitions may exist, the specific instances, cardinalities, constraints, and referential integrity rules are unique to the entities within a given data product’s model.

In the context of evolving data architectures, this granularity supports decentralized data ownership and stewardship, enabling agentic data stewards and data product managers to maintain control and accountability over their respective data products. This approach aligns with the principles of Data Mesh, where relationship documentation becomes a key artifact in the data product lifecycle.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | Business rules, which are a key input to relationship definitions, are governed and managed as part of the overall data governance framework. This includes policies for data quality, security, and compliance that impact relationship constraints. |
| KA-03: Data Modeling and Design | Relationship documentation is a core deliverable within this knowledge area, providing the detailed specifications for entity associations that underpin logical and physical data models. |
| KA-06: Data Integration and Interoperability | Source-to-target mapping, a key consumer of this output, relies on clear relationship documentation to correctly link data between systems and ensure data consistency across integration pipelines. |
| KA-09: Metadata Management | Relationship definitions are a critical form of structural metadata, managed within metadata repositories and catalogs to provide context, enable data lineage, and support impact analysis. |
| KA-11: Data Quality | The constraints defined in relationship documentation (e.g., referential integrity, cardinality) are fundamental rules that data quality processes must validate and monitor. |
| KA-12: Data Security and Privacy | Relationship documentation informs access control policies and data masking strategies by clarifying entity dependencies and data flows. |
| KA-14: Data Architecture | Relationship documentation supports the design and evolution of data architectures, including modern paradigms such as Data Mesh, Data Fabric, and Lakehouse architectures. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately accountable for the completeness, accuracy, and timely delivery of relationship documentation for data products within their scope. Ensures alignment with enterprise standards and governance policies. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Responsible for discovering, analyzing, documenting, and validating all entity relationships as part of the data modeling lifecycle. Collaborates with business and technical stakeholders to ensure accuracy. |
| **S (Supportive)** | Data Architect (D-Arch) | Provides architectural guidance on relationship patterns, ensures consistency with enterprise data architecture, and advises on referential integrity and performance considerations. |
| **C (Consulted)** | Data Steward (D-Steward) | Consulted to provide and validate the business rules, definitions, and constraints that govern entity relationships within their domain. Ensures that documentation reflects operational realities and compliance requirements. |
| **I (Informed)** | Data Engineer (D-Eng) | Informed of the defined relationships to ensure correct implementation in physical database structures, data pipelines, and integration processes. |

### 2.2. Section-Level RASCI

| Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Relationship Identification | D-Modeler | D-Steward, Business Analyst | DE Mgr |
| Cardinality & Optionality | D-Modeler | D-Steward | DE Mgr |
| Referential Integrity Rules | D-Modeler | D-Arch, D-Eng | DE Mgr |
| Relationship Examples | D-Modeler | D-Steward | DE Mgr |

---

## 3. Template

> *The following is the standardized template for creating Relationship Documentation. This template should be completed for each significant relationship within a data model to ensure consistency, clarity, and completeness.*

### 3.1. Relationship Header

| Field | Value |
| :--- | :--- |
| Relationship ID | [e.g., REL-CUST-ORD-001] |
| Relationship Name | [e.g., Customer Places Order] |
| Data Product | [Data Product Name] |
| Version | [e.g., 1.0] |
| Status | [e.g., Draft, In Review, Approved] |
| Last Updated | [Date] |
| Author | [Name/Role] |

### 3.2. Participating Entities

> *Identify the two entities participating in this relationship. Define the role each entity plays from the perspective of the other. Include entity ownership and data product context where applicable.*

| Entity (Parent/Source) | Role in Relationship | Data Product | Owner |
| :--- | :--- | :--- | :--- |
| [e.g., Customer] | [e.g., The party that initiates a purchase transaction.] | [e.g., Customer Data Product] | [e.g., Customer Domain Steward] |

| Entity (Child/Target) | Role in Relationship | Data Product | Owner |
| :--- | :--- | :--- | :--- |
| [e.g., Order] | [e.g., The transaction record created as a result of a customer's purchase.] | [e.g., Order Management Data Product] | [e.g., Order Domain Steward] |

### 3.3. Relationship Description

> *Provide a clear, natural language description of the business rule this relationship represents. Explain the 'verb phrase' that connects the two entities, including any relevant business context or constraints.*

**Input needed**: Business process documentation, interviews with Data Stewards, Subject Matter Experts (SMEs), and business analysts.  
**Who fills this**: D-Modeler.

[e.g., This relationship captures the rule that a Customer can place one or more Orders. Each Order must be placed by exactly one Customer. Orders cannot exist without an associated Customer.]

### 3.4. Cardinality and Optionality

> *Define the numerical constraints of the relationship using standard notation (e.g., Crow's Foot Notation). Specify both the minimum and maximum instances for each side of the relationship, including optionality.*

**Input needed**: Business rule analysis, data profiling, and stakeholder validation.  
**Who fills this**: D-Modeler.

| From (Parent) | To (Child) | Cardinality | Description |
| :--- | :--- | :--- | :--- |
| [e.g., Customer] | [e.g., Order] | One-to-Many (1:M) | A single Customer can be associated with many Orders. |

**Cardinality Details:**
- **From [Parent] to [Child]**: `[e.g., (1,1)]` (Exactly one)
- **From [Child] to [Parent]**: `[e.g., (0,N)]` (Zero or many)

Include notes on optionality, e.g., whether the child entity can exist without the parent, or if participation is mandatory.

### 3.5. Referential Integrity and Constraints

> *Define the rules for maintaining the integrity of the relationship, especially when data is created, updated, or deleted. Include cascading actions, restrictions, and any domain-specific constraints.*

**Input needed**: Data lifecycle requirements, architectural standards, compliance mandates.  
**Who fills this**: D-Modeler, with input from D-Arch, D-Eng, and Data Steward.

| Operation on Parent | Action on Child | Description |
| :--- | :--- | :--- |
| **DELETE** | [e.g., RESTRICT] | [e.g., A Customer cannot be deleted if they have existing Orders. Orders must be archived or reassigned first.] |
| **UPDATE (Primary Key)** | [e.g., CASCADE] | [e.g., If a Customer's primary identifier changes, the corresponding foreign key in the Order table should be updated automatically.] |

Include any additional constraints such as uniqueness, default values, or triggers related to the relationship.

### 3.6. Relationship Type

> *Classify the relationship based on its structural role in the data model and its impact on data integrity and business logic.*

**Input needed**: Data model context and business rules.  
**Who fills this**: D-Modeler.

- **Identifying vs. Non-Identifying**: [e.g., Identifying (The primary key of the Order entity includes the primary key of the Customer entity)]
- **Recursive**: [Yes/No - e.g., No]
- **Supertype/Subtype**: [Yes/No - e.g., No]
- **Associative Entity**: [Yes/No - e.g., Yes, if relationship resolved through an associative entity]
- **Temporal or Versioned**: [Yes/No - e.g., Yes, if relationship changes over time]

---

## 4. Example

> *This example illustrates the relationship documentation for a fictional 'Product Has Parts' relationship at GlobalRetail Inc., demonstrating best practices and completeness.*

### 4.1. Relationship Header

| Field | Value |
| :--- | :--- |
| Relationship ID | REL-PROD-PART-001 |
| Relationship Name | Product Comprises Parts |
| Data Product | Product Catalog |
| Version | 1.2 |
| Status | Approved |
| Last Updated | 2024-05-15 |
| Author | Jane Doe, Data Modeler |

### 4.2. Participating Entities

| Entity (Parent/Source) | Role in Relationship | Data Product | Owner |
| :--- | :--- | :--- | :--- |
| Product | The final, sellable item offered to customers. | Product Catalog | Product Domain Steward |

| Entity (Child/Target) | Role in Relationship | Data Product | Owner |
| :--- | :--- | :--- | :--- |
| Part | A component or raw material used in the assembly of a Product. | Product Catalog | Product Domain Steward |

### 4.3. Relationship Description

This is a recursive, bill-of-materials (BOM) relationship. It defines the rule that a Product can be composed of other Products (which function as sub-assemblies) or basic Parts. This allows for a hierarchical product structure, supporting complex manufacturing and inventory processes.

### 4.4. Cardinality and Optionality

| From (Parent) | To (Child) | Cardinality | Description |
| :--- | :--- | :--- | :--- |
| Product | Part | Many-to-Many (M:N) | A Product can be made of many Parts, and a Part can be used in many Products. An associative entity, `Product_Component`, resolves this M:N relationship. |

**Cardinality Details:**
- **From `Product` to `Product_Component`**: `(1,1)` (Each component must belong to exactly one product)
- **From `Part` to `Product_Component`**: `(1,1)` (Each component must reference exactly one part)

### 4.5. Referential Integrity and Constraints

| Operation on Parent | Action on Child | Description |
| :--- | :--- | :--- |
| **DELETE (`Product`)** | CASCADE | If a Product is deleted, all its corresponding entries in the `Product_Component` table are also deleted to maintain referential integrity. |
| **DELETE (`Part`)** | RESTRICT | A Part cannot be deleted if it is currently a component of any active Product, preventing orphaned components. |
| **UPDATE (Primary Key)** | CASCADE | Changes to Product or Part identifiers cascade to the associative entity to maintain consistency. |

### 4.6. Relationship Type

- **Identifying vs. Non-Identifying**: Non-Identifying (The relationship is resolved through an associative entity `Product_Component`).
- **Recursive**: Yes (A Product can be composed of other Products).
- **Supertype/Subtype**: No.
- **Associative Entity**: Yes (`Product_Component`).
- **Temporal or Versioned**: No.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable, supporting deeper understanding and practical application.

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Business Rules | Deliverable | **templates/templates-KA-01-data-governance.md** |
| Source-to-Target Mapping | Deliverable | **templates/templates-KA-06-data-integration-interoperability.md** |
| Physical Data Model | Deliverable | **templates/templates-KA-03-data-modeling-design.md** |

---

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] Every relationship in the logical data model has a corresponding, complete documentation entry.
- [ ] The relationship name is a clear, concise verb phrase that accurately describes the business interaction (e.g., "Customer Places Order").
- [ ] Cardinality and optionality are explicitly defined for both sides of the relationship using standard notation.
- [ ] Referential integrity actions (ON DELETE, ON UPDATE) are clearly defined and aligned with business rules and technical constraints.
- [ ] The business rule behind the relationship is described in plain language, free of unnecessary technical jargon.
- [ ] The documentation has been reviewed and formally approved by the assigned Data Steward and Data Engineering Manager.
- [ ] Relationship documentation aligns with enterprise data governance policies, including considerations for AI governance and compliance mandates.
- [ ] Documentation supports automation and integration with metadata management and data catalog tools.

### 5.2. Review Checklist

| Question | Check | Reviewer Notes |
| :--- | :--- | :--- |
| Does the relationship accurately reflect the current business process and rules? | ☐ | |
| Is the cardinality correct and validated against real-world scenarios? (e.g., can a customer *really* have zero orders?) | ☐ | |
| Are the referential integrity rules safe, logical, and compliant with data lifecycle policies? (e.g., will they prevent accidental data loss?) | ☐ | |
| Is the relationship name unambiguous and consistent with naming conventions? | ☐ | |
| Is the documentation free of technical jargon where possible and understandable by business stakeholders? | ☐ | |
| Has the documentation been cross-checked against metadata repositories and data catalogs? | ☐ | |
| Does the documentation consider modern data architecture paradigms (e.g., Data Mesh, Data Fabric) and AI governance implications? | ☐ | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Input for this Output)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Entity Definitions | Provides the definition of the entities that are being related, including attributes and keys. | `templates/templates-KA-03-data-modeling-design.md` |
| Attribute Definitions | Provides the definition of the attributes (keys) used to form the relationship, including data types and constraints. | `templates/templates-KA-03-data-modeling-design.md` |
| Business Rules Documentation | Source of business rules that inform relationship cardinality, optionality, and constraints. | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers (Outputs that use this as Input)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Source-to-Target Mapping | Uses relationship documentation to define how foreign key relationships should be populated in the target system and integration pipelines. | `templates/templates-KA-06-data-integration-interoperability.md` |
| Physical Data Model | Implements the logical relationships as physical database constraints (e.g., foreign keys, indexes). | `templates/templates-KA-03-data-modeling-design.md` |
| Metadata Repository | Ingests relationship definitions as structural metadata to support lineage, impact analysis, and governance. | `templates/templates-KA-09-metadata-management.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling Tools** | Erwin, ER/Studio, SAP PowerDesigner, SqlDBM, IBM InfoSphere Data Architect | `draw.io` (for diagrams), DBeaver, OpenModelSphere, Archi |
| **Metadata Catalogs** | Collibra, Alation, Informatica EDC, IBM Watson Knowledge Catalog | Amundsen, DataHub, OpenMetadata, Apache Atlas |
| **Documentation Platforms** | Confluence, SharePoint, Atlassian Jira | MkDocs, Docusaurus, GitBook, Hugo |

### 7.2. Automation Opportunities

- **Automated Generation**: Many data modeling tools can auto-generate initial relationship documentation (including diagrams and constraints) directly from the visual model, reducing manual effort and improving accuracy.
- **Metadata Integration**: Relationship definitions can be automatically extracted from database system catalogs (e.g., `information_schema`, system views) and ingested into metadata catalogs to maintain up-to-date structural metadata.
- **Validation Scripts**: Custom scripts or tools can be developed to automatically validate that physical database constraints match the approved relationship documentation, flagging discrepancies for remediation.
- **Governance and Compliance Checks**: Automated workflows can verify that relationship documentation complies with data governance policies, AI governance frameworks, and regulatory requirements such as the EU AI Act.
- **Change Impact Analysis**: Integration with metadata lineage tools enables automated impact analysis when relationships change, supporting risk assessment and communication.
- **Integration with MLOps/DataOps Pipelines**: Relationship documentation can be linked with operational pipelines to ensure data quality and integrity are maintained throughout model training and deployment cycles.

---

## 8. References

- **DAMA-DMBOK2**: Chapter 5, "Data Modeling and Design"  
- **DAMA-DMBOK 3.0 (Upcoming)**: Anticipated enhancements include expanded coverage of AI governance, data mesh/fabric architectures, and data product-centric modeling approaches.  
- **Internal**: `templates/templates-KA-01-data-governance.md`  
- **Internal**: `references/reference-materials.md`  
- **EU AI Act**: Regulatory framework impacting data governance and documentation requirements for AI systems.  
- **Data Mesh Principles**: Emphasize decentralized data ownership and product thinking, influencing relationship documentation scope and granularity.  
- **Metadata Management Best Practices**: For integrating relationship definitions into enterprise metadata catalogs and lineage tools.


---

# Model Change Log


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
  - [3.2. Model Change Log](#32-model-change-log)
  - [3.3. Detailed Change Descriptions](#33-detailed-change-descriptions)
- [4. Example](#4-example)
  - [4.1. Document Header](#41-document-header)
  - [4.2. Model Change Log](#42-model-change-log)
  - [4.3. Detailed Change Descriptions](#43-detailed-change-descriptions)
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

The **Model Change Log** is a critical governance and operational document that provides a comprehensive, chronological record of all modifications made to a data model throughout its lifecycle. It captures the what, why, when, and who of every change, from initial creation through subsequent updates, enhancements, corrections, and decommissioning activities. The primary purpose of the change log is to ensure transparency, traceability, and accountability in the data modeling process, which is essential for maintaining data integrity, compliance, and alignment with evolving business needs.

In modern data environments, where data models underpin complex data products, data mesh architectures, and AI-driven analytics, the Model Change Log also supports:

- **Auditability and Compliance**: Providing evidence for regulatory compliance (e.g., GDPR, HIPAA, CCPA, and emerging EU AI Act requirements) by documenting model changes and their governance approvals.
- **Impact Analysis and Risk Management**: Enabling data stewards, architects, and engineers to assess the downstream and upstream effects of model changes, especially in multi-cloud and hybrid environments.
- **Collaboration and Communication**: Facilitating coordination among diverse roles including Data Product Managers, AI Ethics Officers, and MLOps Engineers, reflecting the expanded data governance ecosystem.
- **Integration with DevOps Practices**: Supporting CI/CD pipelines, DataOps, and MLOps workflows by maintaining an authoritative source of model change history.

> A comprehensive Model Change Log is the definitive history of a data model's evolution, enabling stakeholders to understand its lineage, rationale, and compliance posture, thereby fostering trust and agility in data-driven decision-making.

### 1.2. Scope

**Per Product** — A Model Change Log is created and maintained for each individual data product that has an associated data model (Conceptual, Logical, or Physical). It tracks the evolution of the specific models related to that data product only, ensuring granularity and relevance.

This deliverable applies across all deployment environments, including on-premises, cloud-native, multi-cloud, and hybrid architectures. It supports data mesh and data fabric paradigms by enabling decentralized stewardship while maintaining centralized oversight through standardized logging.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The change log is a key control for enforcing data governance policies, including AI governance mandates. It provides evidence for the Change Request Log and ensures that model changes are properly authorized and compliant with regulatory frameworks. |
| KA-02: Data Architecture | Changes to data models must align with the overall enterprise data architecture, including modern paradigms such as data mesh and lakehouse architectures. The change log provides input for the Data Architecture Review Board (DARB) to assess compliance and architectural integrity. |
| KA-09: Metadata Management | The Model Change Log is a critical piece of technical metadata, providing lineage, versioning, and historical context that should be captured and managed in the metadata repository to support data discovery and impact analysis. |
| KA-11: Data Quality | Changes to data models can directly impact data quality. The log helps trace the origin of data quality issues that may arise from model modifications and supports continuous quality improvement processes. |
| KA-12: Data Security and Privacy | Model changes can affect data classification, masking, and access controls. The change log assists in ensuring that security and privacy requirements are maintained throughout the model lifecycle. |
| KA-14: Data Product Management | The change log supports the lifecycle management of data products by documenting model evolution, enabling data product managers to coordinate releases and enhancements effectively. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately accountable for ensuring that all model changes are logged accurately, completely, and in a timely manner, and that the change log complies with governance and audit requirements. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Responsible for creating, updating, and maintaining the change log entry for every modification they perform on a data model, ensuring completeness and accuracy. |
| **S (Supportive)** | Database Administrator (DBA) | Supports the process by providing information on the impact of physical model changes on database performance, security, and operations. |
| **C (Consulted)** | Data Architect (D-Arch) | Consulted to review significant model changes to ensure alignment with enterprise architecture standards, cloud-native best practices, and data mesh principles. |
| **C (Consulted)** | AI Ethics Officer | Consulted for changes impacting AI models or data used in AI/ML pipelines to ensure ethical considerations and compliance with AI governance policies. |
| **I (Informed)** | Data Governance Manager (DG Mgr) | Kept informed of all model changes to monitor compliance with governance policies and to update related governance artifacts, including data contracts and stewardship assignments. |
| **I (Informed)** | Data Product Manager | Informed of model changes that affect data product features, SLAs, or consumer expectations. |

### 2.2. Section-Level RASCI

| Log Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Change Identification | D-Modeler | N/A | DE Mgr |
| Change Description | D-Modeler | D-Arch, Business Analyst, AI Ethics Officer (if applicable) | DE Mgr |
| Impact Analysis | D-Modeler | DBA, Application Owner, Data Product Manager | DE Mgr |
| Approval & Status | DE Mgr | Data Governance Committee (DGC) for major or high-risk changes | DE Mgr |

---

## 3. Template

> *The following is the standardized template for a Model Change Log. This template should be used for every data product to ensure consistency. All placeholders `[...]` should be replaced with specific information for each change.*

### 3.1. Document Header

| Field | Value |
| :--- | :--- |
| Data Product Name | [Name of the Data Product] |
| Data Product ID | [Unique ID of the Data Product] |
| Model Type(s) | [e.g., Conceptual, Logical, Physical] |
| Owner | [Data Engineering Manager Name] |
| Last Updated | [YYYY-MM-DD] |
| Data Product Manager | [Name] |
| AI Governance Impact | [Yes/No; if Yes, specify AI models or pipelines affected] |

### 3.2. Model Change Log

> *This table provides a high-level summary of all changes. Each row represents a distinct change request or version. For complex changes, provide a detailed description in Section 3.3.*

| Change ID | Request Date | Model Name / ID | Version | Change Type | Brief Description | Author | Reviewer | Approval Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [e.g., MCL-001] | [YYYY-MM-DD] | [e.g., Customer LDM] | [e.g., 1.1] | [e.g., Creation, Enhancement, Correction, Decommission] | [Briefly describe the change, e.g., "Added new entity for Customer Preferences"] | [Author Name] | [Reviewer Name] | [YYYY-MM-DD] | [Proposed, In Progress, Awaiting Review, Completed, Rejected] |
| [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] |

### 3.3. Detailed Change Descriptions

> *For each significant change listed in the log above, create a dedicated subsection below. Use the Change ID as the subsection header. This section provides the necessary detail to understand the full context and impact of the change.*

#### 3.3.1. Change ID: [MCL-XXX]

*   **Change Details**
    > *Provide a comprehensive description of the change. What entities, attributes, or relationships were added, modified, or removed? Include the business justification or technical reason for the change. Specify if the change affects AI models, data contracts, or data product SLAs.*
    
    [Detailed description of the change.]

*   **Rationale / Justification**
    > *Explain why this change was necessary. Link to business requirements, issue tickets, governance mandates, or AI ethics reviews.*
    
    [Rationale for the change.]

*   **Impact Analysis**
    > *Describe the potential impact on upstream and downstream systems, applications, reports, data products, and other data models. Include any compliance or governance implications.*
    
    *   **Upstream Systems**: [...]
    *   **Downstream Systems**: [...]
    *   **Databases/Schemas**: [...]
    *   **ETL/ELT Jobs**: [...]
    *   **Reports/Dashboards**: [...]
    *   **AI/ML Pipelines**: [...]
    *   **Data Contracts**: [...]
    *   **Data Product SLAs**: [...]

*   **Implementation Details (Optional)**
    > *For physical model changes, include any relevant DDL scripts, configuration changes, or deployment notes required for implementation.*
    
    ```sql
    -- [Paste relevant DDL script here]
    ```

*   **Testing and Validation**
    > *Describe the steps taken to test and validate the model change. Who performed the testing and what were the results? Include validation against data quality, security, and AI governance criteria.*
    
    [Description of testing and validation activities.]

---

### 3.4. Spreadsheet Template

> For a ready-to-use, operational template optimized for data entry, filtering, and collaboration, use the spreadsheet version of this deliverable:
>
> *Note: The spreadsheet template KA-03_model-change-log.xlsx can be generated by Claude on request.*
>
> The spreadsheet format complements this Markdown template by providing a structured, tabular format for managing large volumes of entries. Refer to the sections above for detailed guidance on each field.

## 4. Example

> *This section provides a realistic, filled-in example of a Model Change Log for a fictional company, GlobalRetail Inc.*

### 4.1. Document Header

| Field | Value |
| :--- | :--- |
| Data Product Name | Customer 360 Analytics |
| Data Product ID | DP-CUST-001 |
| Model Type(s) | Logical, Physical |
| Owner | John Smith, Data Engineering Manager |
| Last Updated | 2026-02-08 |
| Data Product Manager | Sarah Lee |
| AI Governance Impact | Yes - Loyalty Program data used in AI-driven marketing models |

### 4.2. Model Change Log

| Change ID | Request Date | Model Name / ID | Version | Change Type | Brief Description | Author | Reviewer | Approval Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MCL-001 | 2025-11-15 | Customer LDM | 1.0 | Creation | Initial creation of the Customer Logical Data Model. | Alice Johnson | David Chen | 2025-11-20 | Completed |
| MCL-002 | 2026-01-20 | Customer PDM | 1.0 | Creation | Initial creation of the Customer Physical Data Model for Snowflake. | Alice Johnson | David Chen | 2026-01-25 | Completed |
| MCL-003 | 2026-02-05 | Customer LDM | 1.1 | Enhancement | Added new 'Loyalty Program' entity and related attributes. | Alice Johnson | David Chen | 2026-02-08 | Completed |

### 4.3. Detailed Change Descriptions

#### 4.3.1. Change ID: MCL-003

*   **Change Details**
    A new entity, `LoyaltyProgram`, was added to the Customer Logical Data Model. This entity is designed to capture details about customer participation in GlobalRetail's new loyalty program.
    *   **New Entity**: `LoyaltyProgram` (Attributes: `LoyaltyID` (PK), `ProgramName`, `TierLevel`, `JoinDate`, `PointsBalance`)
    *   **New Relationship**: A one-to-many relationship was created between `Customer` and `LoyaltyProgram` (`CustomerID` as FK in `LoyaltyProgram`).
    *   **AI Governance**: The loyalty data will feed AI-driven marketing models; ethical review completed.

*   **Rationale / Justification**
    The change was driven by the launch of the "GlobalRewards" loyalty program, a key strategic initiative for FY2026. The business requirement (BR-182) mandated the ability to track customer loyalty status and points for targeted marketing campaigns. AI Ethics Officer reviewed data usage for fairness and privacy compliance.

*   **Impact Analysis**
    *   **Upstream Systems**: The `Customer-API` will need to be updated to include loyalty program data from the CRM.
    *   **Downstream Systems**: The `Marketing-Analytics-DB` and AI/ML pipelines will consume this new data.
    *   **Databases/Schemas**: The `CUSTOMER_MART` schema in Snowflake will be altered to include the new `LOYALTY_PROGRAM` table.
    *   **ETL/ELT Jobs**: The `elt_customer_daily` job will be modified to load data into the new table.
    *   **Reports/Dashboards**: The "Customer Profile" dashboard in Tableau will be updated to display loyalty tier and points.
    *   **AI/ML Pipelines**: Marketing AI models will incorporate loyalty data for segmentation and personalization.
    *   **Data Contracts**: Updated to include loyalty data attributes and SLAs.
    *   **Data Product SLAs**: Enhanced to reflect new data freshness and accuracy requirements.

*   **Implementation Details (Optional)**
    ```sql
    CREATE TABLE CUSTOMER_MART.LOYALTY_PROGRAM (
        LoyaltyID VARCHAR(50) PRIMARY KEY,
        CustomerID VARCHAR(50) NOT NULL,
        ProgramName VARCHAR(100),
        TierLevel VARCHAR(50),
        JoinDate DATE,
        PointsBalance INT,
        FOREIGN KEY (CustomerID) REFERENCES CUSTOMER_MART.CUSTOMER(CustomerID)
    );
    ```

*   **Testing and Validation**
    Unit testing was performed by the Data Modeler to confirm relational integrity. The QA team validated the ETL job and the updated Tableau dashboard in the UAT environment. AI Ethics Officer reviewed model input data for bias and privacy compliance. All tests passed successfully.

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Modeling Standards | Guide | [01-modeling-standards.md](templates/templates-KA-03-data-modeling-design.md) |
| Change Request Log | Deliverable | [11-change-request-log.md](templates/templates-KA-01-data-governance.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [x] A change log entry exists for every version of the data model.
- [x] Each change entry has a unique, sequential Change ID following organizational conventions.
- [x] The business or technical rationale for every change is clearly documented and linked to formal requirements or governance mandates.
- [x] The author, reviewer, and approver of each change are identified with their roles and responsibilities.
- [x] The status of each change (e.g., Proposed, Completed) is accurately reflected and updated in a timely manner.
- [x] A detailed impact analysis has been completed for all non-trivial changes, including AI governance and data product implications.
- [x] The change log is stored in a version control system alongside the model artifacts to maintain integrity and auditability.
- [x] Changes comply with enterprise modeling standards, naming conventions, and security/privacy policies.
- [x] Testing and validation results are documented and confirm the successful implementation of the change.

### 5.2. Review Checklist

| # | Review Item | Check | Reviewer Notes |
|:--|:---|:---:|:---|
| 1 | Is the change description clear, complete, and unambiguous? | ☐ | |
| 2 | Is the justification for the change valid, documented, and linked to a requirement or governance mandate? | ☐ | |
| 3 | Is the impact analysis comprehensive, covering all affected systems, data products, and compliance aspects? | ☐ | |
| 4 | Does the change comply with modeling standards, naming conventions, and security/privacy policies? | ☐ | |
| 5 | Has the change been properly reviewed and approved by the correct roles, including AI Ethics Officer if applicable? | ☐ | |
| 6 | Is the implementation plan sound, with appropriate testing and validation steps defined? | ☐ | |
| 7 | Are data contracts and data product SLAs updated to reflect the change? | ☐ | |
| 8 | Has the change log entry been updated in the version control system alongside model artifacts? | ☐ | |

---

## 6. Related Outputs

### 6.1. Prerequisites

| Output Name | Path / Link to Output |
| :--- | :--- |
| Conceptual Data Model | `templates/templates-KA-03-data-modeling-design.md` |
| Logical Data Model | `templates/templates-KA-03-data-modeling-design.md` |
| Physical Data Model | `templates/templates-KA-03-data-modeling-design.md` |
| Change Request Log | `templates/templates-KA-01-data-governance.md` |

### 6.2. Consumers

| Output Name | Path / Link to Output |
| :--- | :--- |
| Change Request Log | `templates/templates-KA-01-data-governance.md` |
| Data Lineage | `templates/templates-KA-06-data-integration-interoperability.md` |
| Data Product Release Notes | `templates/templates-KA-14-data-management-maturity.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Options | Open Source Options |
| :--- | :--- | :--- |
| **Version Control** | GitHub Enterprise, GitLab, Azure DevOps | Git, Subversion (SVN) |
| **Data Modeling Tools** | erwin Data Modeler, ER/Studio, SAP PowerDesigner | dbt (for physical models), OpenModelSphere |
| **Collaboration and Documentation** | Confluence, SharePoint | Wiki.js, Markdown files in Git |
| **Workflow Automation** | Jira, ServiceNow | GitHub Actions, Jenkins |
| **AI Governance Platforms** | IBM OpenScale, Microsoft Azure Purview | MLflow, Feast |

### 7.2. Automation Opportunities

*   **Git Hooks**: Implement pre-commit hooks to ensure that every commit to a data model file is accompanied by an update to the `model-change-log.md` file, enforcing completeness.
*   **CI/CD Integration**: Integrate the change log into a CI/CD pipeline. A pull request that modifies a model can trigger a workflow requiring the change log to be updated, reviewed, and approved before merging.
*   **Automated Notifications**: Configure webhooks in the version control system to automatically notify stakeholders (e.g., in Slack, Microsoft Teams, or email) whenever a model change is logged, reviewed, or approved.
*   **Template Generation**: Use scripts or tools to automatically generate a new change log entry template when a new change request is initiated, ensuring consistency.
*   **Metadata Repository Integration**: Automate synchronization of change log entries with the enterprise metadata repository to maintain up-to-date lineage and impact data.
*   **AI Governance Checks**: Integrate AI governance tools to flag changes that impact AI/ML models, triggering additional review workflows.
*   **Dashboards and Reporting**: Automate generation of dashboards summarizing model change activity, compliance status, and impact metrics for governance committees.

---

## 8. References

| # | Reference | Description |
|:--|:---|:---|
| 1 | DAMA-DMBOK2, Chapter 5 | Data Modeling and Design - Discusses the importance of managing and controlling changes to data models as part of the modeling lifecycle. |
| 2 | DAMA-DMBOK 3.0 (forthcoming) | The upcoming version emphasizes AI governance, data mesh integration, and cloud-native architectures in data modeling lifecycle management. |
| 3 | `references/reference-materials.md` | Provides the official definitions for all roles mentioned in the RASCI charts. |
| 4 | `templates/templates-KA-03-data-modeling-design.md` | Outlines the standards that all model changes must adhere to, including naming conventions and versioning. |
| 5 | `templates/templates-KA-01-data-governance.md` | Change Request Log deliverable, closely linked to the Model Change Log for governance tracking. |
| 6 | `templates/templates-KA-06-data-integration-interoperability.md` | Data Lineage deliverable, which uses information from the Model Change Log for traceability. |
| 7 | EU AI Act and GDPR Compliance Guidelines | Regulatory frameworks requiring documentation and governance of AI-related data changes. |


---

# Dimensional Data Model


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
  - [3.2. Business Process Overview](#32-business-process-overview)
  - [3.3. Model Diagram](#33-model-diagram)
  - [3.4. Fact Table Design](#34-fact-table-design)
  - [3.5. Dimension Table Design](#35-dimension-table-design)
- [4. Example](#4-example)
  - [4.1. Document Control](#41-document-control)
  - [4.2. Business Process Overview](#42-business-process-overview)
  - [4.3. Model Diagram (Conceptual)](#43-model-diagram-conceptual)
  - [4.4. Fact Table Design](#44-fact-table-design)
  - [4.5. Dimension Table Design](#45-dimension-table-design)
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

A **Dimensional Data Model** is a specialized database structure designed specifically to optimize analytical queries, business intelligence (BI), and data warehousing workloads. Unlike normalized models (such as Third Normal Form - 3NF), which prioritize transactional efficiency and data integrity, dimensional models are intentionally denormalized to enhance query performance, simplify data navigation, and improve usability for business users and analysts.

The dimensional model is organized around a central business process and is composed primarily of two types of tables:

- **Fact tables**: Store quantitative transactional or event data (measures) that represent business metrics or key performance indicators (KPIs).
- **Dimension tables**: Contain descriptive attributes that provide context to the facts, enabling slicing, dicing, filtering, and grouping of measures.

> The primary purpose of a Dimensional Data Model is to present data in a standardized, intuitive framework that allows for high-performance access while supporting complex analytical queries such as slicing, dicing, drilling down, and rolling up. This design supports self-service analytics, accelerates BI report development, and facilitates advanced analytics including AI and machine learning workloads.

With the evolving data landscape, dimensional models remain foundational but are increasingly integrated within modern data architectures such as data mesh and data fabric, supporting cloud-native, multi-cloud, and lakehouse environments. The model also plays a critical role in enabling governance frameworks, including AI governance, by clearly defining data lineage, semantics, and quality expectations.

### 1.2. Scope

**Per Product / Business Process** — A Dimensional Data Model is typically created for a specific business process or data product (e.g., Sales, Inventory, Marketing Campaigns). While some dimensions (like Date, Customer, or Geography) may be shared and conformed across multiple models, each fact table and its associated dimensional model is scoped to a particular analytical requirement or data product.

This scoped approach aligns with modern data product thinking, where dimensional models serve as logical blueprints for data marts or data products that are managed as first-class entities within data mesh or data fabric architectures. The model supports integration with data contracts and stewardship practices, ensuring data quality and compliance (e.g., GDPR, HIPAA, EU AI Act).

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-08: Data Warehousing and BI | Dimensional modeling is the foundational design technique for building data warehouses, data marts, and BI reporting layers. It supports analytical workloads and enables high-performance querying. |
| KA-03: Data Modeling and Design | Dimensional modeling is a specialized discipline within the broader field of data modeling, complementing conceptual, logical, and physical modeling for transactional systems. |
| KA-06: Data Integration and Interoperability | ETL/ELT processes that populate dimensional models are core to data integration, transforming and loading data from source systems into fact and dimension tables. |
| KA-09: Metadata Management | Effective dimensional modeling relies on comprehensive metadata that defines facts, dimensions, attributes, hierarchies, business rules, and lineage, supporting governance and AI compliance. |
| KA-11: Data Governance | Dimensional models must align with data governance policies, including data stewardship, data contracts, and compliance requirements, especially in regulated environments and AI governance contexts. |
| KA-12: Data Architecture | Dimensional models are integral components of enterprise data architecture, supporting modern architectures such as data mesh, data fabric, and lakehouse implementations. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Engineering Manager (DE Mgr) | Ultimately accountable for the successful delivery, quality, and ongoing maintenance of the dimensional data model, ensuring alignment with business requirements, data governance policies, and architectural standards. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Responsible for the hands-on design, development, and documentation of the dimensional model, including fact and dimension tables, hierarchies, slowly changing dimension (SCD) implementations, and relationships. |
| **S (Supportive)** | Data Warehouse Architect (DW Arch) | Provides architectural guidance, ensures the model aligns with enterprise standards, cloud-native and modern data architecture principles, and assists with complex design decisions and performance optimization. |
| **C (Consulted)** | Data Analyst (D-Analyst), BI Developer (BI Dev), AI/ML Engineer | Provide input on business requirements, analytical needs, AI model data requirements, and usability. Validate that the model supports reporting, analytics, and AI/ML use cases. |
| **I (Informed)** | Data Analytics Manager (DA Mgr), Data Governance Lead | Kept informed of the model's design, status, and compliance with governance and AI regulations, as it impacts analytics delivery and data stewardship activities. |

### 2.2. Section-Level RASCI

| Model Section/Task | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Business Requirements Gathering | D-Analyst | D-Modeler, Business Stakeholders, AI Ethics Officer | DE Mgr |
| Fact Table Design & Granularity | D-Modeler | DW Arch, D-Analyst | DE Mgr |
| Dimension Table Design & Attributes | D-Modeler | DW Arch, D-Analyst | DE Mgr |
| Hierarchy and SCD Type Definition | D-Modeler | DW Arch, Data Governance Lead | DE Mgr |
| Model Validation and Testing | BI Dev, D-Analyst, AI/ML Engineer | D-Modeler | DE Mgr |

---

## 3. Template

> *The following is the standardized template for a Dimensional Data Model. Replace all placeholders `[...]` with project-specific information. Each section includes inline guidance in blockquotes.*

### 3.1. Document Control

| Field | Value |
| :--- | :--- |
| Model Name | [e.g., Sales and Profitability] |
| Data Product | [e.g., Retail Sales Analytics] |
| Version | [e.g., 1.0] |
| Status | [e.g., Draft, In Review, Approved] |
| Effective Date | [YYYY-MM-DD] |
| Owner | [Data Modeler Name] |
| Approver | [Data Engineering Manager Name] |

### 3.2. Business Process Overview

> *Describe the business process that this model represents. This should be a concise summary (1-2 paragraphs) that explains the activities, participants, and the grain of the process being measured. Include any relevant compliance or governance considerations, and note if the model supports AI/ML use cases.*

**Input needed**: Business requirements document, interviews with business stakeholders, AI/ML model requirements, governance policies.  
**Who fills this**: D-Modeler, D-Analyst.

[e.g., This model represents the retail sales process, which begins when a customer purchases one or more products at a store and ends when the transaction is finalized. The model captures key performance indicators at the level of an individual product line item within a single sales transaction. It supports compliance with GDPR and enables AI-driven sales forecasting.]

### 3.3. Model Diagram

> *Insert a visual diagram of the dimensional model (e.g., a star or snowflake schema). The diagram should clearly show the central fact table and its connections to all dimension tables, including primary and foreign keys. Indicate any conformed dimensions shared across models.*

**Input needed**: A data modeling tool (e.g., Erwin, ER/Studio, Draw.io).  
**Who fills this**: D-Modeler.

[Placeholder for Dimensional Model Diagram Image]

### 3.4. Fact Table Design

> *Detail the structure of the central fact table. Specify the grain, list all foreign keys to dimensions, and define each measure (fact). Include notes on data freshness, update frequency, and any AI/ML feature columns.*

#### 3.4.1. Fact Table Grain

> *The grain statement is a clear declaration of what a single row in the fact table represents. It is the most important step in dimensional design.*

**Grain Statement**: [e.g., One row per product line item on a customer sales receipt.]

#### 3.4.2. Fact Table Columns

| Column Name | Data Type | Description | Type | Source System / Calculation |
| :--- | :--- | :--- | :--- | :--- |
| `[dim_name]_key` | `INTEGER` | Foreign key to the `[dim_name]` dimension. | Foreign Key | N/A |
| `[measure_name]` | `DECIMAL(18,4)` | [Description of the numeric measure] | [Additive/Semi-Additive/Non-Additive] | `[SourceTable].[SourceColumn]` or `[Calculation Logic]` |
| `[ai_feature_name]` | `[Data Type]` | [Description of AI/ML feature derived from fact or dimension data] | Derived | `[Calculation Logic]` |

### 3.5. Dimension Table Design

> *For each dimension table connected to the fact table, provide a detailed column-level specification. Include the primary key, business keys, and all descriptive attributes. Specify the Slowly Changing Dimension (SCD) type for attributes that change over time. Highlight any attributes critical for AI governance or compliance.*

#### 3.5.1. Dimension: `[Dimension Name]` (e.g., `DimProduct`)

| Column Name | Data Type | Description | SCD Type | Source System.Table.Column |
| :--- | :--- | :--- | :--- | :--- |
| `[dim_name]_key` | `INTEGER` | Surrogate primary key. | N/A | Generated by ETL process |
| `[dim_name]_id` | `VARCHAR(50)` | Natural/business key from the source system. | Type 1 | `[SourceTable].[SourceColumn]` |
| `[attribute_name]` | `VARCHAR(255)` | [Descriptive attribute of the dimension] | [Type 1/2/3] | `[SourceTable].[SourceColumn]` |
| `row_is_current` | `CHAR(1)` | For SCD Type 2, flag indicating if the record is the current version ('Y' or 'N'). | N/A | Generated by ETL process |
| `row_start_date` | `DATETIME` | For SCD Type 2, the date the record became effective. | N/A | Generated by ETL process |
| `row_end_date` | `DATETIME` | For SCD Type 2, the date the record expired. | N/A | Generated by ETL process |

#### 3.5.2. Hierarchies in `[Dimension Name]`

> *Define any hierarchies present within the dimension. Hierarchies enable drill-down and roll-up analysis, which are critical for business intelligence and AI feature engineering.*

- **Hierarchy Name**: [e.g., Product Category]
  - **Levels**: `[Level 1 (e.g., Category)]` -> `[Level 2 (e.g., Subcategory)]` -> `[Level 3 (e.g., Product Name)]`

---

## 4. Example

> *This is a realistic example of a dimensional model for the "Sales" business process at a fictional company, GlobalRetail Inc. It includes modern considerations such as AI feature columns and governance notes.*

### 4.1. Document Control

| Field | Value |
| :--- | :--- |
| Model Name | Retail Sales and Profitability |
| Data Product | GlobalRetail Sales Analytics |
| Version | 1.0 |
| Status | Approved |
| Effective Date | 2026-02-08 |
| Owner | Jane Doe (Data Modeler) |
| Approver | John Smith (DE Manager) |

### 4.2. Business Process Overview

This model represents the retail sales process at GlobalRetail Inc. The process begins when a customer purchases one or more products at a physical or online store and ends when the transaction is finalized and payment is confirmed. The model captures key performance indicators such as sales amount, quantity sold, and profit at the level of an individual product line item within a single sales transaction, providing a granular view of sales performance.

The model supports AI-driven demand forecasting and customer segmentation by including derived features such as rolling averages and customer lifetime value. It complies with GDPR and internal AI governance policies by tracking data lineage and supporting data stewardship.

### 4.3. Model Diagram (Conceptual)

```
+-----------------+      +-----------------+
| DimDate         |<-----|                 |
+-----------------+      |                 |
                       | FactSales       |
+-----------------+      |                 |
| DimProduct      |<-----|                 |
+-----------------+      +-----------------+
                       ^
+-----------------+      |
| DimCustomer     |------+
+-----------------+      |
                       | |
+-----------------+      |
| DimStore        |------+
+-----------------+
```

### 4.4. Fact Table Design

#### 4.4.1. Fact Table Grain

**Grain Statement**: One row per product line item on a customer sales receipt.

#### 4.4.2. Fact Table: `FactSales`

| Column Name | Data Type | Description | Type | Source System / Calculation |
| :--- | :--- | :--- | :--- | :--- |
| `date_key` | `INTEGER` | FK to the `DimDate` dimension. | Foreign Key | N/A |
| `product_key` | `INTEGER` | FK to the `DimProduct` dimension. | Foreign Key | N/A |
| `customer_key` | `INTEGER` | FK to the `DimCustomer` dimension. | Foreign Key | N/A |
| `store_key` | `INTEGER` | FK to the `DimStore` dimension. | Foreign Key | N/A |
| `sales_amount` | `DECIMAL(18,2)` | The total revenue for the line item (Quantity * Unit Price). | Additive | `Sales.Transactions.LineItemTotal` |
| `quantity_sold` | `INTEGER` | The number of units of the product sold. | Additive | `Sales.Transactions.Quantity` |
| `unit_cost` | `DECIMAL(18,2)` | The cost of a single unit of the product. | Non-Additive | `Inventory.ProductCost.UnitCost` |
| `profit_amount` | `DECIMAL(18,2)` | The profit for the line item. | Additive | `sales_amount - (quantity_sold * unit_cost)` |
| `rolling_7d_avg_sales` | `DECIMAL(18,2)` | 7-day rolling average of sales amount for the product. | Semi-Additive | Calculated via window function in ETL |
| `customer_lifetime_value` | `DECIMAL(18,2)` | Estimated lifetime value of the customer at the time of transaction. | Derived | Calculated from historical sales data |

### 4.5. Dimension Table Design

#### 4.5.1. Dimension: `DimDate`

| Column Name | Data Type | Description | SCD Type | Source |
| :--- | :--- | :--- | :--- | :--- |
| `date_key` | `INTEGER` | Surrogate PK (e.g., 20260208) | N/A | ETL |
| `full_date` | `DATE` | The full calendar date. | N/A | ETL |
| `day_of_week` | `VARCHAR(10)` | e.g., 'Monday' | N/A | ETL |
| `month_name` | `VARCHAR(10)` | e.g., 'February' | N/A | ETL |
| `quarter` | `CHAR(2)` | e.g., 'Q1' | N/A | ETL |
| `year` | `INTEGER` | e.g., 2026 | N/A | ETL |

#### 4.5.2. Dimension: `DimProduct`

| Column Name | Data Type | Description | SCD Type | Source System.Table.Column |
| :--- | :--- | :--- | :--- | :--- |
| `product_key` | `INTEGER` | Surrogate primary key. | N/A | ETL |
| `product_sku` | `VARCHAR(50)` | Natural key from the source system. | Type 1 | `Products.Master.SKU` |
| `product_name` | `VARCHAR(255)` | The name of the product. | Type 2 | `Products.Master.Name` |
| `subcategory` | `VARCHAR(100)` | The product's subcategory. | Type 2 | `Products.Categories.SubcategoryName` |
| `category` | `VARCHAR(100)` | The product's main category. | Type 2 | `Products.Categories.CategoryName` |
| `brand` | `VARCHAR(100)` | The brand of the product. | Type 1 | `Products.Master.Brand` |
| `row_is_current` | `CHAR(1)` | 'Y' or 'N' | N/A | ETL |
| `row_start_date` | `DATETIME` | Effective date of the record. | N/A | ETL |
| `row_end_date` | `DATETIME` | Expiration date of the record. | N/A | ETL |

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Governance | Knowledge Area | **KA-11-data-governance.md** |
| Data Warehouse Architecture | Knowledge Area | **KA-08-data-warehousing-bi.md** |
| Source-to-Target Mapping | Deliverable | **06-source-to-target-mapping.md** |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] The model's grain is explicitly stated, unambiguous, and consistently applied throughout the design.
- [ ] The model directly corresponds to a well-defined business process or data product scope.
- [ ] All dimension tables contain surrogate primary keys and appropriate business keys.
- [ ] All fact tables connect to dimension tables via their surrogate keys, ensuring referential integrity.
- [ ] All measures in the fact table are numeric and classified as additive, semi-additive, or non-additive, with clear definitions.
- [ ] All proposed hierarchies within dimensions are clearly defined with fixed levels supporting drill-down and roll-up.
- [ ] Slowly Changing Dimension (SCD) policies (Type 1, 2, 3, etc.) are defined and applied consistently for all relevant attributes.
- [ ] The model has been validated against business requirements by data analysts, BI developers, and AI/ML engineers.
- [ ] Naming conventions for tables and columns are followed as per `templates/templates-KA-03-data-modeling-design.md`.
- [ ] The model complies with applicable data governance policies, including data stewardship, data contracts, and AI governance requirements.
- [ ] The model design supports scalability, performance, and integration within modern data architectures (e.g., data mesh, lakehouse).
- [ ] Documentation includes lineage and metadata to support auditability and regulatory compliance (e.g., GDPR, EU AI Act).

### 5.2. Review Checklist

| Category | Question | Reviewer Notes |
| :--- | :--- | :--- |
| **Business Alignment** | Does the model accurately represent the business process and answer the key business questions? | |
| **Granularity** | Is the grain of the fact table at the lowest possible level required for analysis? Is it unambiguous? | |
| **Completeness** | Are all required facts and descriptive attributes for the specified business process included in the model? | |
| **Scalability** | Is the model designed to accommodate future growth in data volume and potential new attributes or measures? | |
| **Performance** | Is the model sufficiently denormalized to support high-performance queries? Have snowflake structures been avoided unless necessary? | |
| **Clarity** | Are column names intuitive and easy for business users to understand? | |
| **Governance & Compliance** | Does the model include metadata and lineage to support data governance and regulatory compliance? | |
| **AI Readiness** | Does the model support AI/ML use cases with appropriate feature columns and data quality? | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Logical Data Model | Provides the normalized source structure and business rules that are denormalized into this dimensional model. | `templates/templates-KA-03-data-modeling-design.md` |
| Dimensional Model Standards | Contains the guiding principles and standards that this dimensional model must adhere to, including naming conventions and SCD policies. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Business Requirements Document | Defines the business processes, KPIs, and analytical needs that drive the dimensional model design. | `templates/templates-KA-01-data-governance.md` |
| Data Governance Policies | Provides data stewardship, data contract, and compliance requirements relevant to the model. | `templates/templates-KA-11-data-quality.md` |

### 6.2. Consumers (Outputs)

| Output | Relationship | Relative Path |
| :--- | :--- | :--- |
| Data Mart Design | This dimensional model serves as the logical blueprint for one or more physical data marts. | `templates/templates-KA-08-data-warehousing-bi.md` |
| Source-to-Target Mapping | This model is the "target" for ETL/ELT jobs, requiring detailed source-to-target mapping documents. | `templates/templates-KA-06-data-integration-interoperability.md` |
| BI Reports and Dashboards | Consume the dimensional model to deliver business insights and analytics. | `templates/templates-KA-08-data-warehousing-bi.md` |
| AI/ML Feature Store | Uses dimensional model data and derived features for training and inference. | `templates/templates-KA-10-reference-master-data.md` |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling** | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, SqlDBM | dbt (for modeling-as-code), Draw.io (for diagrams), OpenModelSphere |
| **Database/Warehouse** | Snowflake, Teradata, Azure Synapse, Google BigQuery | PostgreSQL, MySQL |
| **ETL/ELT** | Informatica PowerCenter, Talend, Azure Data Factory, Fivetran | dbt, Airflow, Pentaho |
| **BI & Visualization** | Tableau, Power BI, Qlik Sense | Apache Superset, Metabase |
| **AI/ML Platforms** | Databricks, DataRobot, H2O.ai | TensorFlow, MLflow, Kubeflow |

### 7.2. Automation Opportunities

- **Model Generation from Metadata**: Portions of the dimensional model, particularly dimension tables and hierarchies, can be automatically generated or updated from a central metadata repository or business glossary, ensuring consistency and governance.
- **Code Generation (DDL)**: Data Definition Language (DDL) scripts to create tables, indexes, and relationships in the target database can be automatically generated from data modeling tools or metadata catalogs.
- **ETL Scaffolding**: Based on the model design and source-to-target mappings, scaffolding for ETL/ELT jobs (e.g., dbt models, Airflow DAGs) can be automatically generated to load fact and dimension tables, including SCD handling.
- **Documentation Generation**: This markdown document itself can be partially generated or updated from metadata stored within the data modeling tool or metadata management system, ensuring up-to-date documentation.
- **Data Quality and Lineage Automation**: Integration with data quality tools and lineage trackers can automate validation and compliance reporting for the dimensional model.
- **AI Feature Engineering Pipelines**: Automation of feature extraction and transformation pipelines to populate AI/ML feature columns within the dimensional model or feature store.

---

## 8. References

- **[1]** DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 5: Data Modeling and Design)  
- **[2]** DAMA International. *DAMA-DMBOK 3.0 (In Development)*. Community-driven update launching June 2025, emphasizing AI governance, data mesh/fabric, and modern architectures.  
- **[3]** `templates/templates-KA-03-data-modeling-design.md`  
- **[4]** `templates/templates-KA-08-data-warehousing-bi.md`  
- **[5]** `references/reference-materials.md`  
- **[6]** European Commission. *EU AI Act* (2023). Regulatory framework for trustworthy AI systems, impacting data governance and modeling.  
- **[7]** IBM. *Data Mesh and Data Fabric Synergy*. Whitepaper on modern data architectures and their impact on data modeling.  
- **[8]** Microsoft Azure. *Lakehouse Architecture*. Guidance on integrating data lakes and warehouses for analytics and AI.


---

# Model Review and Validation Report


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
  - [3.2. Model Identification](#32-model-identification)
  - [3.3. Review Scope and Objectives](#33-review-scope-and-objectives)
  - [3.4. Validation Checklist](#34-validation-checklist)
  - [3.5. Findings and Issues](#35-findings-and-issues)
  - [3.6. Recommendations](#36-recommendations)
  - [3.7. Approval Decision](#37-approval-decision)
- [4. Example](#4-example)
  - [4.1. Report Header](#41-report-header)
  - [4.2. Model Identification](#42-model-identification)
  - [4.3. Review Scope and Objectives](#43-review-scope-and-objectives)
  - [4.4. Validation Checklist (Excerpt)](#44-validation-checklist-excerpt)
  - [4.5. Findings and Issues](#45-findings-and-issues)
  - [4.6. Recommendations](#46-recommendations)
  - [4.7. Approval Decision](#47-approval-decision)
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

The **Model Review and Validation Report** is a formal, comprehensive document that captures the assessment of a data model against enterprise standards, business requirements, technical best practices, and emerging governance mandates. It serves as the authoritative record of the validation process, detailing findings, issues, and actionable recommendations from the review. The primary purpose of this report is to ensure that a data model is fit for purpose, structurally sound, compliant with governance policies (including AI governance and regulatory requirements), and aligned with enterprise data architecture principles before approval and deployment.

This report provides a structured mechanism for quality assurance within the data modeling lifecycle and supports traceability for audit and compliance purposes. It is a critical control point in modern data management frameworks, especially as organizations adopt cloud-native architectures, data mesh and fabric patterns, and integrate AI/ML pipelines.

> This report answers the critical question: *"Is this data model correct, complete, compliant, and ready for enterprise use?"* It provides evidence-based justification for approving, rejecting, or requesting modifications to a proposed data model.

**Forward-looking note:** With the forthcoming DAMA-DMBOK 3.0 (expected June 2025), this deliverable will evolve to explicitly incorporate AI governance checkpoints, data product lifecycle considerations, and agentic stewardship roles, reflecting the community-driven modernization of data management practices.

### 1.2. Scope

**Per Product** — This report is generated for each individual data model (Conceptual, Logical, or Physical) developed for a specific data product, data domain, or project. While the review process is governed by global enterprise standards, the validation is contextualized to the specific business requirements, technical environment (e.g., cloud platform, multi-cloud), and governance mandates (e.g., GDPR, EU AI Act, HIPAA, CCPA) relevant to the model under review.

The scope includes evaluation of:

- Alignment with enterprise data architecture and modeling standards.
- Compliance with data governance and AI governance policies.
- Structural integrity, normalization, and performance considerations.
- Security, privacy, and regulatory compliance controls embedded in the model.
- Readiness for integration into modern data platforms, including data mesh and lakehouse architectures.
- Support for data productization and data contracts as applicable.

### 1.3. Related Knowledge Areas

| Knowledge Area | Relationship |
| :--- | :--- |
| KA-01: Data Governance | The review enforces governance standards defined in `04-data-standards.md` and ensures the model aligns with the business glossary (`06-business-glossary.md`) and data stewardship policies, including emerging AI governance frameworks. |
| KA-02: Data Architecture | The model is validated against the enterprise data model (`01-enterprise-data-model.md`) and architectural principles (`09-architecture-principles.md`), including considerations for data mesh, fabric, and cloud-native design patterns. |
| KA-03: Data Modeling and Design | This deliverable is a core artifact within the data modeling lifecycle, directly linked to modeling standards (`01-modeling-standards.md`) and naming conventions (`02-naming-conventions.md`). |
| KA-06: Data Integration and Interoperability | The approved model serves as a definitive source or target for source-to-target mappings (`06-source-to-target-mapping.md`) and supports data contracts and product interfaces. |
| KA-09: Metadata Management | The review ensures all model components (entities, attributes) are properly defined, documented, and ready for ingestion into metadata repositories and catalogues. |
| KA-11: Data Quality | The report assesses whether the model design supports data quality rules and metrics required for the data product, including integration with DataOps and MLOps pipelines. |

---

## 2. RASCI Assignment

### 2.1. Output-Level RASCI

| Role Category | Assigned Role | Responsibility Description |
| :--- | :--- | :--- |
| **A (Accountable)** | Data Architect (D-Arch) | Ultimately accountable for the integrity and completeness of the model review process and for the final decision on model approval based on the report's findings. Ensures alignment with enterprise architecture and governance policies, including AI governance. |
| **R (Responsible)** | Data Modeler (D-Modeler) | Conducts the detailed model review, performs validation checks, authors this report, and coordinates input from other roles. Ensures the model meets technical and business requirements. |
| **S (Supportive)** | Data Quality Analyst (DQ Analyst) | Supports the review by validating that the model structure can support required data quality checks, business rules, and metrics. Provides input on data quality implications of the model design. |
| **C (Consulted)** | Data Steward (D-Steward), Database Administrator (DBA), AI Ethics Officer (optional) | The Data Steward ensures the model accurately reflects business semantics and governance policies. The DBA advises on physical model feasibility and performance. The AI Ethics Officer (where applicable) reviews AI-related data models for ethical compliance and bias mitigation. |
| **I (Informed)** | Data Engineering Manager (DE Mgr), Chief AI Officer (CAIO) | Informed of review results for operational planning and governance oversight. The CAIO may be informed for AI-related data products to ensure alignment with AI governance frameworks. |

### 2.2. Section-Level RASCI

| Report Section | Primary Author (R) | Reviewer (C) | Approver (A) |
| :--- | :--- | :--- | :--- |
| Validation Checklist | D-Modeler | D-Steward, DQ Analyst, AI Ethics Officer (if applicable) | D-Arch |
| Findings and Issues | D-Modeler | D-Steward, DBA | D-Arch |
| Recommendations | D-Modeler | D-Arch | D-Arch |
| Final Approval | D-Arch | N/A | D-Arch |

---

## 3. Template

> *The following is the standardized template for a Model Review and Validation Report. This template guides the reviewer in performing a structured and comprehensive assessment, incorporating modern data management considerations.*

### 3.1. Report Header

| Field | Value |
| :--- | :--- |
| Report Title | Model Review and Validation Report: [Model Name] |
| Report ID | MRV-[YYYYMMDD]-[ModelID] |
| Version | [e.g., 1.0] |
| Review Date | [YYYY-MM-DD] |
| Reviewer(s) | [Data Modeler Name(s)] |
| Approver | [Data Architect Name] |
| AI Governance Review | [Yes/No/NA] |
| Regulatory Compliance Review | [Yes/No/NA] |

### 3.2. Model Identification

> *Clearly identify the data model being reviewed, including its name, version, type, and the project or data product it supports.*

- **Model Name**: `[e.g., Customer Master Logical Data Model]`
- **Model Version**: `[e.g., 2.1]`
- **Model Type**: `[Conceptual | Logical | Physical]`
- **Data Product / Project**: `[e.g., Project Phoenix - Customer 360]`
- **Link to Model Artifact**: `[Link to model file in repository or tool]`
- **Platform / Environment**: `[e.g., AWS Lakehouse, Azure Synapse, On-Premises]`
- **Data Mesh Domain**: `[If applicable, e.g., Customer Domain]`
- **Data Product Owner**: `[Name and contact]`

### 3.3. Review Scope and Objectives

> *State the primary objectives of this review. What are the key areas of focus? This sets the context for the validation checklist.*

**Input needed**: Project requirements, business rules documentation, governance policies, AI ethics guidelines.  
**Who fills this**: D-Modeler.

The objectives of this review are to:

1. Verify compliance with enterprise `01-modeling-standards.md` and `02-naming-conventions.md`.
2. Ensure the model accurately and completely represents the business requirements and aligns with the business glossary (`06-business-glossary.md`).
3. Validate the structural integrity, normalization, and performance considerations of the model.
4. Assess the model's alignment with the enterprise data architecture (`KA-02-01-enterprise-data-model.md`) and architectural principles (`09-architecture-principles.md`).
5. Confirm that the model supports data quality rules and metrics (`KA-11-data-quality.md`).
6. Evaluate compliance with data governance and AI governance policies, including privacy and security controls.
7. (For Physical Models) Confirm performance, scalability, security, and cloud-native deployment considerations are addressed.
8. Assess readiness for integration into modern data platforms such as data mesh, data fabric, or lakehouse architectures.
9. Identify any AI-specific ethical or regulatory risks in the model design (if applicable).

### 3.4. Validation Checklist

> *This is the core of the review. Use this checklist to systematically assess the model. Mark each item as Pass, Fail, or N/A and provide comments for any "Fail" items.*

**Input needed**: The data model itself, modeling standards, business glossary, governance policies, AI ethics guidelines.  
**Who fills this**: D-Modeler, with input from DQ Analyst, D-Steward, AI Ethics Officer (if applicable).

#### 3.4.1. Conceptual Model Checklist

| # | Item | Pass/Fail/N/A | Comments |
|---|:---|:---:|:---|
| C1 | Are all major business entities and concepts identified and aligned with business domains? | | |
| C2 | Are the relationships between entities correctly identified, named, and cardinalities defined? | | |
| C3 | Does the model align with the scope defined in the project charter and data mesh domain boundaries? | | |
| C4 | Is the terminology consistent with the enterprise business glossary (`06-business-glossary.md`)? | | |
| C5 | Are data product boundaries and ownership clearly represented? | | |
| C6 | Does the model consider data privacy and regulatory constraints at a conceptual level? | | |

#### 3.4.2. Logical Model Checklist

| # | Item | Pass/Fail/N/A | Comments |
|---|:---|:---:|:---|
| L1 | Are all entities and attributes fully defined with business and technical metadata? | | |
| L2 | Is the model normalized to at least 3rd Normal Form (3NF), or justified denormalization applied? | | |
| L3 | Are primary keys and foreign keys correctly identified and consistent with data contracts? | | |
| L4 | Are data types and constraints (e.g., NOT NULL, domain constraints) defined for all attributes? | | |
| L5 | Does the model resolve all many-to-many relationships with associative entities? | | |
| L6 | Are naming conventions from `02-naming-conventions.md` followed consistently? | | |
| L7 | Are data quality rules and validation points incorporated or supported by the model design? | | |
| L8 | Does the model incorporate AI governance considerations, such as data lineage and bias mitigation points? | | |

#### 3.4.3. Physical Model Checklist

| # | Item | Pass/Fail/N/A | Comments |
|---|:---|:---:|:---|
| P1 | Are data types optimized for the target database platform and cloud environment? | | |
| P2 | Are appropriate indexing, partitioning, and clustering strategies defined for performance and scalability? | | |
| P3 | Are views, stored procedures, or other database objects documented and aligned with data product interfaces? | | |
| P4 | Have denormalization strategies been applied justifiably and documented, considering query patterns? | | |
| P5 | Does the model incorporate security controls (e.g., column-level encryption, masking) aligned with privacy policies? | | |
| P6 | Is the model designed to support multi-cloud or hybrid cloud deployment if applicable? | | |
| P7 | Are audit and logging mechanisms incorporated to support data lineage and compliance? | | |

### 3.5. Findings and Issues

> *Summarize all "Fail" items from the checklist in this section. For each finding, provide a clear description of the issue, its impact, and a reference to the specific checklist item.*

**Input needed**: Completed validation checklist.  
**Who fills this**: D-Modeler.

| ID | Checklist Item | Issue Description | Impact Assessment |
|:---|:---|:---|:---|
| F-01 | `[e.g., L2]` | `[e.g., The 'CustomerAddress' entity contains transitive dependencies (City, State, Zip), violating 3NF.]` | `[e.g., High. Leads to data redundancy and potential update anomalies.]` |
| F-02 | `[e.g., L6]` | `[e.g., Several attributes use the 'ID' suffix instead of the standard '_KEY' suffix.]` | `[e.g., Medium. Causes inconsistency and violates enterprise standards.]` |
| F-03 | `[e.g., P5]` | `[e.g., Sensitive PII columns lack encryption or masking controls.]` | `[e.g., High. Non-compliance with GDPR and HIPAA may result in legal penalties.]` |

### 3.6. Recommendations

> *For each finding identified in the previous section, propose a concrete, actionable recommendation for remediation.*

**Input needed**: List of findings.  
**Who fills this**: D-Modeler.

| ID | Recommendation | Recommended Action |
|:---|:---|:---|
| R-01 | `[e.g., For Finding F-01]` | `[e.g., Normalize the 'CustomerAddress' entity by creating a separate 'ZipCode' entity containing City and State.]` |
| R-02 | `[e.g., For Finding F-02]` | `[e.g., Refactor all primary and foreign key attributes to use the '_KEY' suffix as per the naming conventions document.]` |
| R-03 | `[e.g., For Finding F-03]` | `[e.g., Implement column-level encryption and masking on PII fields according to the enterprise security policy.]` |

### 3.7. Approval Decision

> *The Data Architect provides the final decision based on the review. This section is the formal sign-off.*

**Input needed**: Completed report.  
**Who fills this**: D-Arch.

- [ ] **Approved**: The model meets all quality criteria and is approved for the next stage.
- [ ] **Approved with Conditions**: The model is approved, contingent on the successful implementation of all recommendations by [YYYY-MM-DD]. A follow-up review is required.
- [ ] **Rejected**: The model has significant issues and requires a major revision. A full re-review will be required after remediation.

**Approver Comments**:  
`[Insert comments from the Data Architect explaining the decision.]`

**Approver Signature**: _________________________ Date: ______________

---

## 4. Example

> *The following is a filled-in example for a fictional company, GlobalRetail Inc., reviewing a new logical data model for its loyalty program.*

### 4.1. Report Header

| Field | Value |
| :--- | :--- |
| Report Title | Model Review and Validation Report: Loyalty Program LDM |
| Report ID | MRV-20260208-LOY-LDM-01 |
| Version | 1.0 |
| Review Date | 2026-02-08 |
| Reviewer(s) | John Smith (Data Modeler) |
| Approver | Jane Doe (Data Architect) |
| AI Governance Review | Yes |
| Regulatory Compliance Review | Yes |

### 4.2. Model Identification

- **Model Name**: Loyalty Program Logical Data Model
- **Model Version**: 1.2
- **Model Type**: Logical
- **Data Product / Project**: Loyalty Program Revamp
- **Link to Model Artifact**: `[https://git.globalretail.com/data-models/loyalty/ldm_v1.2.erwin]`
- **Platform / Environment**: AWS Lakehouse
- **Data Mesh Domain**: Customer Engagement
- **Data Product Owner**: Sarah Lee (sarah.lee@globalretail.com)

### 4.3. Review Scope and Objectives

The objectives of this review are to:

1. Verify compliance with GlobalRetail's enterprise modeling standards.
2. Ensure the model accurately represents the new tiered loyalty program structure.
3. Validate the model is in 3rd Normal Form.
4. Assess alignment with the Customer and Product subject areas in the Enterprise Data Model.
5. Confirm that data privacy controls and AI governance principles are embedded.
6. Evaluate readiness for deployment in the AWS Lakehouse environment.

### 4.4. Validation Checklist (Excerpt)

| # | Item | Pass/Fail/N/A | Comments |
|---|:---|:---:|:---|
| L1 | Are all entities and attributes fully defined? | **Pass** | All 15 entities and 85 attributes have complete definitions in the model dictionary. |
| L2 | Is the model normalized to at least 3rd Normal Form (3NF)? | **Fail** | The `Member` entity contains a `TierName` attribute, which is dependent on `TierID`, a non-key attribute. This is a transitive dependency. |
| L3 | Are primary keys and foreign keys correctly identified? | **Pass** | All keys are correctly defined. |
| L6 | Are naming conventions from `02-naming-conventions.md` followed? | **Fail** | The entity `Transactions` should be named `MemberTransaction` to include the parent entity name as per standards. |
| P5 | Does the model incorporate security controls (e.g., column-level encryption)? | **Pass** | PII columns are encrypted and masked as per policy. |
| L8 | Does the model incorporate AI governance considerations? | **Pass** | Data lineage and bias mitigation attributes are included. |

### 4.5. Findings and Issues

| ID | Checklist Item | Issue Description | Impact Assessment |
|:---|:---|:---|:---|
| F-01 | L2 | The `Member` entity violates 3NF. The `TierName` attribute is transitively dependent on the primary key via `TierID`. | **High**. This will cause data redundancy and update anomalies. If a tier name changes (e.g., "Gold" to "Gold Plus"), every member record in that tier would need to be updated. |
| F-02 | L6 | The `Transactions` entity is not named according to the `EntityNamingStandard` which requires child entities to be prefixed with the parent name. | **Medium**. Violates enterprise standards, leading to confusion and inconsistency in the data landscape. It makes it harder for developers to understand relationships. |

### 4.6. Recommendations

| ID | Recommendation | Recommended Action |
|:---|:---|:---|
| R-01 | For Finding F-01 | Remove the `TierName` attribute from the `Member` entity. The tier name should be looked up from the `LoyaltyTier` entity via the existing `TierID` foreign key. |
| R-02 | For Finding F-02 | Rename the `Transactions` entity to `MemberTransaction`. Update all related foreign key attribute names accordingly (e.g., `TransactionID` becomes `MemberTransactionID`). |

### 4.7. Approval Decision

- [X] **Approved with Conditions**: The model is approved, contingent on the successful implementation of all recommendations by 2026-02-15. A follow-up review is required.

**Approver Comments**:  
`The model is well-structured overall, but the normalization and naming convention issues must be fixed before implementation can begin. Please address the recommendations and submit for a final review.`

**Approver Signature**: *Jane Doe* Date: *2026-02-08*

---

### 4.4. Related Concepts and Guides

> The following resources provide additional context and guidance for this deliverable:

| Resource | Type | Path |
| :--- | :--- | :--- |
| Metadata | Concept | [metadata.md](references/concepts-metadata-quality.md) |
| Data Product Outputs | Reference | [data-product-outputs.md](references/reference-materials.md) |
| Data Modeling Standards | Deliverable | [01-modeling-standards.md](templates/templates-KA-03-data-modeling-design.md) |
| Naming Conventions | Deliverable | [02-naming-conventions.md](templates/templates-KA-03-data-modeling-design.md) |
| Enterprise Data Model | Deliverable | [01-enterprise-data-model.md](templates/templates-KA-02-data-architecture.md) |
| Architecture Principles | Deliverable | [09-architecture-principles.md](templates/templates-KA-02-data-architecture.md) |

## 5. Quality Criteria

### 5.1. Acceptance Criteria

- [ ] All sections of the report template are filled out completely and accurately.
- [ ] Every "Fail" on the checklist has a corresponding entry in the Findings and Recommendations sections.
- [ ] Recommendations are specific, actionable, and directly address the identified issues.
- [ ] The final approval decision is clearly marked and signed by the Data Architect.
- [ ] The report is stored in the official document repository with a link in the `09-model-change-log.md`.
- [ ] AI governance and regulatory compliance reviews are documented where applicable.
- [ ] The report supports traceability for audit and compliance purposes.

### 5.2. Review Checklist

| # | Review Question | Pass/Fail |
| :--- | :--- | :--- |
| 1 | Was the correct and latest version of the data model used for the review? | |
| 2 | Were all relevant stakeholders (D-Steward, DBA, AI Ethics Officer) consulted during the review? | |
| 3 | Are the findings described with enough detail to be understood and actionable by the development team? | |
| 4 | Do the recommendations align with enterprise standards, governance policies, and best practices? | |
| 5 | Is the impact assessment for each finding realistic and clearly articulated? | |
| 6 | Are AI governance and regulatory compliance considerations adequately addressed? | |

---

## 6. Related Outputs

### 6.1. Prerequisites (Inputs)

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-03-data-modeling-design.md` | Provides the core standards and normalization rules against which the model is validated. |
| `templates/templates-KA-02-data-architecture.md` | Provides architectural principles and checkpoints that inform the model review process. |
| `templates/templates-KA-01-data-governance.md` | Used to validate that entity and attribute names are consistent with enterprise business terminology. |
| `templates/templates-KA-01-data-governance.md` | Provides governance policies and standards, including data security and privacy requirements. |
| `templates/templates-KA-11-data-quality.md` | Provides data quality rules that the model must support. |
| `templates/templates-KA-07-document-content-management.md` | Provides security and privacy policies relevant to model validation. |

### 6.2. Consumers (Outputs)

| Output | Relationship |
| :--- | :--- |
| `templates/templates-KA-03-data-modeling-design.md` | The findings and approval status from this report trigger entries in the change log to track the model's revision history. |
| `templates/templates-KA-06-data-integration-interoperability.md` | An approved model from this report becomes a definitive source or target for data mapping documents. |
| `templates/templates-KA-01-data-governance.md` | Summary of governance compliance including model validation outcomes. |
| `templates/templates-KA-10-reference-master-data.md` | The model supports DataOps pipelines for continuous integration and deployment. |
| `templates/templates-KA-12-data-handling-ethics.md` | AI governance considerations for models supporting AI/ML workloads. |

---

## 7. Tools and Automation

### 7.1. Recommended Tools

| Tool Category | Commercial Tools | Open Source / Free Tools |
| :--- | :--- | :--- |
| **Data Modeling Tools** | Erwin Data Modeler, ER/Studio, SAP PowerDesigner, SqlDBM | `draw.io` (for conceptual), DBeaver, OpenModelSphere |
| **Model Validation** | Erwin DM, ER/Studio (built-in validation rules), Collibra, Informatica Axon | Custom Python scripts using libraries like `pandas`, `sqlalchemy`, and `Great Expectations` to inspect database schemas and validate data quality. |
| **Collaboration and Workflow** | Confluence, Jira, ServiceNow | GitHub/GitLab (for model versioning and issue tracking), Apache Airflow (for workflow orchestration) |
| **AI Governance Tools** | IBM OpenScale, Microsoft Azure Purview | Open-source AI fairness and lineage tools (e.g., AI Fairness 360) |

### 7.2. Automation Opportunities

- **Automated Checklist Validation**: Develop scripts or tools that connect to databases or parse DDL/model files to automatically validate compliance with naming conventions, data type standards, normalization rules, and security controls. This can pre-fill a significant portion of the validation checklist.
- **AI Governance Checks**: Integrate AI governance validation tools to assess model fairness, bias, lineage, and compliance with AI ethics policies.
- **Report Generation**: Automate generation of the initial draft of this report in Markdown or PDF format using outputs from validation tools combined with manual findings.
- **Workflow Integration**: Embed the model review process into CI/CD pipelines or data product lifecycle management platforms. Pull requests containing model changes can trigger automated validation and post results as comments or approval gates.
- **Metadata Synchronization**: Automate ingestion of model metadata into enterprise metadata repositories and catalogues to maintain up-to-date lineage and impact analysis.

---

## 8. References

1.  DAMA International. *DAMA-DMBOK: Data Management Body of Knowledge, Second Edition*. Technics Publications, 2017. (Chapter 5: Data Modeling and Design)  
2.  DAMA International. *DAMA-DMBOK 3.0 (Draft)*. Community-driven update expected June 2025.  
3.  `templates/templates-KA-03-data-modeling-design.md`  
4.  `templates/templates-KA-02-data-architecture.md`  
5.  `templates/templates-KA-01-data-governance.md`  
6.  `templates/templates-KA-11-data-quality.md`  
7.  `templates/templates-KA-07-document-content-management.md`  
8.  `templates/templates-KA-12-data-handling-ethics.md`  
9.  `references/reference-materials.md`  
10. European Commission. *EU AI Act* (Proposed Regulation).  
11. NIST. *AI Risk Management Framework*.  
12. Gartner. *Data Mesh and Data Fabric Synergies*.  
13. Microsoft Azure. *Lakehouse Architecture Patterns*.
