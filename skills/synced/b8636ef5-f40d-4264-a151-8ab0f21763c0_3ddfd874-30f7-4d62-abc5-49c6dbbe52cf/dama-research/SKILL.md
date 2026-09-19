---
name: dama-research
description: Comprehensive DAMA-DMBOK skill for data strategy, governance, architecture, quality, and deliverable generation. Trigger whenever user mentions data governance, data strategy, data architecture, data quality, maturity, DAMA-DMBOK, MDM, data catalog, data lineage, metadata, data modeling, data security, data warehousing, BI, data mesh, data fabric, data lakehouse, data products, data contracts, data observability, or KA-01 through KA-14. Also trigger for creating deliverables like governance charters, data policies, architecture blueprints, data dictionaries, quality scorecards, maturity assessments, or any enterprise data management document. Even without explicit DAMA mention, trigger for any data management planning, assessment, or deliverable task.
---

# DAMA Research & Deliverable Generation Skill

Covers the full DAMA-DMBOK2 framework: 14 Knowledge Areas, 26 foundational concepts, 152+ deliverable templates, 9 industry guides, and a Python maturity calculator.

## Quick Routing Table

| User asks about... | Read this file | How to navigate |
|:---|:---|:---|
| A concept (data mesh, governance, quality, etc.) | `references/concepts-*.md` | Open file → read "Sections in This File" table at top → use `view_range` |
| A Knowledge Area deep dive | `knowledge-areas/KA-XX-*.md` | Read from top; use TOC inside file |
| Creating a specific deliverable | `templates/templates-KA-XX-*.md` | Open file → read "Sections in This File" table → jump to template line |
| Which template to use | `templates/INDEX.md` | Master list of all 152 templates with KA mapping |
| Strategy, maturity assessment, governance framework | `templates/strategy-assessment-governance.md` | 6 strategy-level templates in one file |
| Industry-specific guidance | `references/guides.md` | 22 sections: getting started + 8 implementation + 9 industry + PMBOK |
| Roles, RASCI, KPIs, glossary, acronyms | `references/reference-materials.md` | 8 reference sections in one file |
| Running a maturity assessment | `tools/maturity-calculator.py` | `python maturity-calculator.py interactive` or `assess <file>` |

## File Navigation Pattern

Every merged file has a **"Sections in This File"** navigation table at the top. This table lists every section with its **line number**. Always read this table first, then use `view_range` to jump directly to the section you need.

Example workflow:
```
1. view references/concepts-modern-paradigms.md [1, 30]    ← Read nav table
2. Find "Data Mesh" is at line 575
3. view references/concepts-modern-paradigms.md [575, 650]  ← Read Data Mesh section
```

## Concept File Routing

| File | Topics |
|:---|:---|
| `references/concepts-governance-strategy.md` | Governance Models, Data Strategy, Maturity Models, Stewardship & Ownership, Data Literacy, Data Lifecycle, Data Classification, Data Ethics & Privacy |
| `references/concepts-architecture-design.md` | Architecture Patterns, Modeling Paradigms, Dimensional Modeling, Data Warehouse & Lake, Data Lakehouse |
| `references/concepts-modern-paradigms.md` | Data Mesh, Data Fabric, Data Product, Data Contract, Data Observability, Data Valuation |
| `references/concepts-integration-operations.md` | Integration Patterns, Data Pipeline, Data Security Fundamentals |
| `references/concepts-metadata-quality.md` | Metadata, Data Catalog, Data Lineage, Data Quality Dimensions, Master & Reference Data |

## Template File Routing

| KA | Template File | Deliverable Count |
|:---|:---|:---|
| KA-01 Data Governance | `templates/templates-KA-01-data-governance.md` | 13 |
| KA-02 Data Architecture | `templates/templates-KA-02-data-architecture.md` | 10 |
| KA-03 Data Modeling | `templates/templates-KA-03-data-modeling-design.md` | 11 |
| KA-04 Storage & Ops | `templates/templates-KA-04-data-storage-operations.md` | 10 |
| KA-05 Data Security | `templates/templates-KA-05-data-security.md` | 13 |
| KA-06 Integration | `templates/templates-KA-06-data-integration-interoperability.md` | 12 |
| KA-07 Document Mgmt | `templates/templates-KA-07-document-content-management.md` | 10 |
| KA-08 DW & BI | `templates/templates-KA-08-data-warehousing-bi.md` | 11 |
| KA-09 Metadata | `templates/templates-KA-09-metadata-management.md` | 11 |
| KA-10 Master Data | `templates/templates-KA-10-reference-master-data.md` | 11 |
| KA-11 Data Quality | `templates/templates-KA-11-data-quality.md` | 12 |
| KA-12 Data Ethics | `templates/templates-KA-12-data-handling-ethics.md` | 9 |
| KA-13 Big Data & DS | `templates/templates-KA-13-big-data-data-science.md` | 10 |
| KA-14 Maturity | `templates/templates-KA-14-data-management-maturity.md` | 9 |

## Deliverable Generation Workflow

When the user asks you to create a data management deliverable:

1. **Identify the KA** — Which Knowledge Area does the deliverable belong to?
2. **Read the nav table** — Open the template file, read lines 1-25 to see all available templates and their line numbers
3. **Read the template** — Use `view_range` to read the specific template section
4. **Read context** — If needed, read the relevant KA file or concept file for deeper context
5. **Customize** — Adapt the template to the user's organization, industry, maturity level
6. **Output** — Generate as markdown, .docx, or other format. For spreadsheets, use the xlsx skill to generate .xlsx files from template descriptions

## Maturity Assessment Workflow

1. Run `python tools/maturity-calculator.py interactive` for guided CLI assessment
2. Or prepare a CSV file (format: `KA_ID,Capability,Score`) and run `python tools/maturity-calculator.py assess input.csv`
3. Generate report: `python tools/maturity-calculator.py report input.csv output.md`
4. For the assessment template, read `templates/templates-KA-14-data-management-maturity.md`

## Important Notes

- **Always read the nav table first** — Every merged file starts with a "Sections in This File" table showing line numbers. Use this to navigate efficiently.
- **Large files** — Some KA files are 100KB+. Use `view_range` to read specific sections, never load entire files.
- **Template sections** are separated by `---` dividers. Each starts with a `# Template Name` heading.
- **Spreadsheet templates** — Original .xlsx files were consolidated. Claude can generate fresh .xlsx files from template descriptions using the xlsx skill.
