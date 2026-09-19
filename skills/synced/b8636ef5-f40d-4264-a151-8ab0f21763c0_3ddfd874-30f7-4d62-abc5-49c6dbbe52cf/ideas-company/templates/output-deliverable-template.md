# Template: Output Deliverable Document

**Version:** 1.1
**Last Updated:** 2026-02-20

> **Purpose:** This is a master template for creating standardized, high-quality client deliverables. It integrates best practices from DAMA-DMBOK 2, regulatory standards, and internal IDEAS methodologies. For highly specific deliverables, refer to the 152 templates in `dama-research/templates/deliverables/`.

---

## Document Header

| Field | Value |
|:---|:---|
| **Document Title** | `[DELIVERABLE_TITLE]` |
| **Project Name** | `[PROJECT_NAME]` |
| **Client** | `[CLIENT_NAME]` |
| **Service Code** | `[S1.X / S2.X / S3.X]` - *Cross-reference with `references/services-catalog.md`* |
| **DAMA Knowledge Area** | `[KA-XX: Knowledge Area Name]` |
| **DAMA Template Reference** | `dama-research/templates/deliverables/{KA-XX}/{filename}` |
| **Version** | `1.0` |
| **Date** | `[DD Month YYYY]` |
| **Author** | `[AUTHOR_NAME / Tim Konsultan IDEAS]` |
| **Reviewer** | `[REVIEWER_NAME / Client Role]` |
| **Status** | `[Draft / In Review / Approved / Final]` |

## 1. Executive Summary

`[Provide a concise, 1-2 paragraph summary. State the document's purpose, scope, key findings, and primary recommendations. This section should be written last but placed first.]`

## 2. Background & Context

### 2.1 Project Context
`[Describe the business problem or opportunity that necessitates this deliverable. Explain why it's important for the client and what strategic objectives it supports.]`

### 2.2 Scope
`[Clearly define the boundaries of this deliverable. Use a bulleted list to specify what is **In Scope** and what is **Out of Scope** to manage expectations.]`

### 2.3 Regulatory Context (2025-2026)
`[Identify relevant regulations. Refer to the most current versions. See `references/regulatory-standards.md` for a comprehensive list of 25+ primary regulations, including UU PDP No. 27/2022, Perpres SPBE No. 95/2018, and Perpres Satu Data No. 39/2019.]`

## 3. Methodology

### 3.1 Approach
`[Detail the methodology used (e.g., stakeholder interviews, focus group discussions (FGD), quantitative analysis, desk research, maturity assessment). Justify why this approach was chosen.]`

### 3.2 Data Sources
`[List all primary and secondary data sources used, such as internal client documents, system databases, public datasets, or survey results. Specify the timeframe of the data.]`

### 3.3 Standards & Frameworks
`[List the specific frameworks and standards applied, such as DAMA-DMBOK 2, ISO 8000 (Data Quality), ISO 27001 (Information Security), COBIT, or TOGAF.]`

## 4. Findings & Analysis

### 4.1 Current State (As-Is)
`[Present the factual findings from your assessment. Use diagrams, tables, and metrics to illustrate the current situation. Structure the analysis by theme or process area.]`

### 4.2 Gap Analysis
`[Compare the current state against best practices, desired future state, or regulatory requirements. Clearly articulate the gaps and their business implications.]`

### 4.3 Key Issues & Root Causes
`[Synthesize the findings to identify the top 3-5 critical issues. For each issue, perform a root cause analysis to understand the underlying problems, not just the symptoms.]`

## 5. Recommendations

### 5.1 Strategic Recommendations
`[Propose high-level, long-term recommendations (12-24 months) that align with the client's strategic goals. Each recommendation should address one or more key issues.]`

### 5.2 Tactical Recommendations
`[Provide specific, actionable, short-to-medium term recommendations (3-12 months). These should be concrete steps the client can take to implement the strategic recommendations.]`

### 5.3 Implementation Roadmap
`[Present a visual roadmap (e.g., Gantt chart) that prioritizes recommendations and sequences them over time. Include phases, key milestones, dependencies, and estimated timelines.]`

## 6. Risk & Mitigation

`[Identify potential risks and challenges associated with implementing the recommendations. For each risk, propose concrete mitigation strategies.]`

| Risk Category | Risk Description | Likelihood (1-5) | Impact (1-5) | Mitigation Strategy |
|:---|:---|:---:|:---:|:---|
| **Organizational** | `[e.g., Resistance to change]` | `[Score]` | `[Score]` | `[e.g., Develop a change management and communication plan]` |
| **Technical** | `[e.g., Data migration complexity]` | `[Score]` | `[Score]` | `[e.g., Conduct a pilot migration project]` |
| **Financial** | `[e.g., Budget constraints]` | `[Score]` | `[Score]` | `[e.g., Phase implementation to align with budget cycles]` |

## 7. Deliverable Details

`[This is the core content section. The structure will vary based on the deliverable type (e.g., a Data Governance Charter will have different content than a Data Quality Assessment Report). Refer to the specific DAMA templates in `dama-research/templates/deliverables/` for detailed structures.]`

## 8. Security & Privacy Considerations

### 8.1 Data Classification
`[Classify the data handled or produced by this deliverable according to the client's policy or the standard below.]`

| Classification Level | Description | Handling Requirements |
|:---|:---|:---|
| **Sangat Rahasia** | Strategic data, sensitive personal data | End-to-end encryption, need-to-know access, full audit trail |
| **Rahasia** | Internal organizational data | Role-based access control, encryption at-rest |
| **Terbatas** | Internal operational data | Department-level access |
| **Publik** | Open data for public consumption | Adherence to Satu Data Indonesia principles |

### 8.2 Privacy Impact Assessment (PIA)
`[Summarize the PIA findings based on UU No. 27 Tahun 2022 (PDP).]`

| Aspect | Status | Notes & Mitigation Actions |
|:---|:---|:---|
| Data Pribadi Umum | `[Ya/Tidak]` | `[e.g., Data minimization techniques applied]` |
| Data Pribadi Spesifik | `[Ya/Tidak]` | `[e.g., Explicit consent mechanism implemented]` |
| Persetujuan Subjek Data | `[Ya/Tidak]` | `[e.g., Consent records are managed and auditable]` |
| Mekanisme Penghapusan | `[Ya/Tidak]` | `[e.g., Automated data retention and deletion process]` |
| Transfer Lintas Batas | `[Ya/Tidak]` | `[e.g., Adequacy decision or approved transfer mechanism in place]` |

### 8.3 Security Controls
`[List the specific security controls recommended or applied.]`
- **Access Control:** `[e.g., Role-Based Access Control (RBAC) using Active Directory]`
- **Encryption:** `[e.g., AES-256 for data at rest, TLS 1.3 for data in transit]`
- **Auditing:** `[e.g., All access to sensitive data is logged in a central SIEM]`
- **Incident Response:** `[e.g., Refer to the corporate Incident Response Plan (IRP-2025)]`

## 9. Team & Roles (RACI Matrix)

`[Define the roles and responsibilities for the activities related to this deliverable. Use role names from the `scripts/rate_card.py` RATE_CARD dictionary for consistency.]`

| Activity | Responsible | Accountable | Consulted | Informed |
|:---|:---|:---|:---|:---|
| `[Activity 1: e.g., Data Policy Approval]` | `[e.g., Data Governance Committee]` | `[e.g., Chief Data Officer]` | `[e.g., Legal Counsel]` | `[e.g., All Department Heads]` |
| `[Activity 2: e.g., Data Quality Monitoring]` | `[e.g., Data Steward]` | `[e.g., Data Owner]` | `[e.g., Data Analyst]` | `[e.g., IT Operations]` |
| `[Activity 3]` | `[Role]` | `[Role]` | `[Role]` | `[Role]` |

> **RACI Guide:**
> - **Responsible (R):** The doer(s).
> - **Accountable (A):** The one ultimately answerable (only one per activity).
> - **Consulted (C):** Kept in the loop with two-way communication.
> - **Informed (I):** Kept up-to-date with one-way communication.

## 10. Quality Assurance

### 10.1 Review Checklist
- [ ] Content aligns with the agreed-upon scope.
- [ ] Terminology is consistent with DAMA-DMBOK 2 and the project glossary.
- [ ] Regulatory references are current (2025-2026) and correctly interpreted.
- [ ] Formatting adheres to IDEAS branding and quality standards.
- [ ] No sensitive or confidential data is improperly exposed.
- [ ] Privacy Impact Assessment has been completed and signed off.
- [ ] All cross-references are validated and working.

### 10.2 Approval History

| Version | Date | Reviewer | Status | Notes |
|:---|:---|:---|:---|:---|
| `0.1` | `[Date]` | `[Internal Reviewer]` | `In Review` | `Initial draft for internal review.` |
| `1.0` | `[Date]` | `[Client Reviewer]` | `Approved` | `Final version approved by client.` |

## 11. Appendices

### Appendix A: Glossary
`[Define key terms, acronyms, and abbreviations used in the document to ensure a common understanding.]`

| Term | Definition |
|:---|:---|
| `[Term]` | `[Definition]` |
| `[Term]` | `[Definition]` |

### Appendix B: References
`[List all external documents, articles, and web links cited in this deliverable.]`

### Appendix C: Supporting Data
`[Include supplementary charts, tables, or data extracts that are too detailed for the main body of the document.]`

---

## Example: Completed Header

| Field | Value |
|:---|:---|
| **Document Title** | Data Governance Charter — Kementerian XYZ |
| **Project Name** | Implementasi Tata Kelola Data Kementerian XYZ |
| **Client** | Kementerian XYZ |
| **Service Code** | S1.1 |
| **DAMA Knowledge Area** | KA-01: Data Governance |
| **DAMA Template Reference** | `dama-research/templates/deliverables/KA-01-data-governance/01-governance-charter.md` |
| **Version** | 1.0 |
| **Date** | 20 Februari 2026 |
| **Author** | Tim Konsultan IDEAS |
| **Reviewer** | Chief Data Officer Kementerian XYZ |
| **Status** | Draft |

---

**Related Skill Documents:**
- **DAMA Templates:** For 152 specific deliverable structures, see `dama-research/templates/deliverables/`.
- **Service Catalog:** For details on S-codes, see `references/services-catalog.md`.
- **Deliverable Map:** For service-to-deliverable mapping, see `references/service-deliverables-map.md`.
- **Regulatory Guide:** For details on all regulations, see `references/regulatory-standards.md`.
- **Proposal Template:** For proposal structure, see `templates/proposal-template.md`.
- **Rate Card:** For standard role names, see `scripts/rate_card.py`.
