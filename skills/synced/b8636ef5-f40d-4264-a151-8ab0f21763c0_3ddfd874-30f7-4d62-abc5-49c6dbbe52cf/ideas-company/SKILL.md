---
name: ideas-company
description: Knowledge base for PT Indonesian Data Ecosystem (IDEAS) — Indonesia's data infrastructure & analytics provider. 141 roles, 8 products, PMBOK, Infonomics, business frameworks (BMC, VPC, BSC, SPIN, Shipley, BABOK). Trigger whenever user mentions IDEAS, Indonesian Data Ecosystem, SPBE, or needs proposals, RAB/HPS, COGS, pitch decks, surat penawaran, BoQ, LKPP technical proposals, cost estimates, pricing, service recommendations, case studies, agile planning, data product canvas, or business analysis (SWOT, PESTEL, Five Forces, OKR) for Indonesian government/enterprise data projects. Also trigger for Indonesian government data procurement, SPBE scores, or data ecosystem consulting even without explicit IDEAS mention.
---

# IDEAS Company Knowledge Base Skill (v7.1 — Claude Edition)

Act as an expert consultant representing IDEAS. Use this knowledge base to answer queries, generate documents, calculate costs, and provide strategic recommendations.

> **v7.1** — Fixed timeline hardcoded paths, added input validation (level 1-24, COGS structure), stderr logging for clean JSON output, BUMN/international sector support, improved task descriptions in Gantt charts.

## Setup

All scripts require the working directory to be `scripts/` (for inter-module imports):

```bash
SKILL_DIR="$(dirname "$(find /mnt/skills -path '*/ideas-company/SKILL.md' -print -quit 2>/dev/null)")"
cd "$SKILL_DIR/scripts"
pip install tabulate pyyaml --break-system-packages -q 2>/dev/null
```

## Collaborative Workflow with `dama-research`

| Skill | Role | When to Use |
|:---|:---|:---|
| `dama-research` | Theory | DAMA-DMBOK KAs, maturity models, global best practices, deliverable templates |
| `ideas-company` | Practice | Indonesian context, pricing, proposals, service delivery, case studies |

Activate `dama-research` for theoretical grounding, maturity assessment frameworks, RASCI matrices, and standardized deliverable templates. See `references/dama-integration-map.md` for the full service-to-KA mapping.

## Workflow

### Step 1: Classify Intent

| Intent Category | Description |
|:---|:---|
| **Information** | Company profile, services, products, clients, regulations |
| **Proposal/Pitch** | Government procurement (Type B) or enterprise/BUMN pitch (Type A) |
| **Admin Documents** | Surat penawaran, BoQ, LKPP technical proposal, business proposal |
| **Cost & Pricing** | Role-based, task-based, flexible competency, lump sum pricing |
| **Financial Planning** | COGS, RAB/HPS, scenario comparison |
| **Client Analysis** | SPBE scores, portal status, opportunity scoring |
| **Recommendation** | Service matching by need or sector |
| **Project Planning** | Timeline/Gantt, agile hierarchy, deliverable mapping |
| **Strategic Analysis** | BMC, SWOT, PESTEL, Five Forces, BSC, OKR, VPC |

### Step 2: Read Reference Files

Use `view` to read the relevant reference file(s). **Never answer from memory.**

| Topic | File |
|:---|:---|
| Company profile, CEO, vision/mission | `references/company-profile.md` |
| 15 services (S1.1-S3.4), pillars | `references/services-catalog.md` |
| 8 product platforms, GenAI capabilities | `references/products-catalog.md` |
| 25 regulations (UU PDP, SPBE, SDI, etc.) | `references/regulatory-standards.md` |
| SPBE 47 indicators, 4 domains, maturity | `references/spbe-evaluation-framework.md` |
| Delivery process, commercial models | `references/service-delivery-patterns.md` |
| Roles, salary rates, pricing models | `references/human-resources-and-pricing.md` |
| 15 services -> 613 subtasks, RASCI | `references/task-decomposition.md` |
| COGS methodology (4-component) | `references/cogs-methodology.md` |
| RAB/HPS structure, PPH gross-up | `references/rab-hps-methodology.md` |
| SPBE national scores 2018-2024 | `references/client-intelligence-spbe.md` |
| Jabar ecosystem showcase (46 OPD) | `references/portfolio-showcase-jabar.md` |
| 8 case studies + testimonials | `references/case-studies.md` |
| Competitor map, 16 USPs, win themes | `references/competitive-landscape.md` |
| Proposal/Pitch patterns, Shipley/Minto | `references/proposal-patterns.md` |
| Document checklists, numbering system | `references/project-administration-guide.md` |
| PMBOK, Infonomics, Dylan Anderson | `references/thought-leadership-frameworks.md` |
| Data Ecosystem newsletter (52 issues) | `references/data-ecosystem-knowledge-base.md` |
| 102 DAMA deliverables -> 15 services | `references/service-deliverables-map.md` |
| Agile hierarchy, sprint planning | `references/agile-work-hierarchy.md` |
| Digital/Data Product lifecycle | `references/digital-data-product-lifecycle.md` |
| SPBE-DAMA alignment per indicator | `references/dama-integration-map.md` |
| BMC, Porter, SPIN, BABOK, BSC/OKR | `references/business-frameworks.md` |
| SPBE data schema, CSV files | `references/spbe-schema.md` + CSVs |
| INAPROC e-Katalog, KBLI codes | `references/inaproc-digital-catalog.md` |
| 141 DDaT-aligned role definitions | `references/role-definitions.md` |

For files >300 lines, read the TOC first (lines 1-30), then `view_range` to the needed section.

### Step 3: Run Scripts

All scripts log to stderr; structured output goes to stdout. Pipe `2>/dev/null` for clean data output.

#### Service Recommendation

```bash
# By need (Indonesian/English)
python3 recommend_service.py --need "kami butuh portal data pemerintah"
# By sector: government | enterprise | bumn | international | academia | media
python3 recommend_service.py --sector bumn
# JSON output
python3 recommend_service.py --need "data governance" --json
```

#### Cost Estimation (Task-Based)

```bash
# Single service (level 1-24)
python3 estimate_service_cost.py --service S1.1 --level 8
# Multiple services with complexity multiplier
python3 estimate_service_cost.py --services S1.1,S1.2,S2.3 --level 10 --complexity 1.5
# Detailed task/role breakdown
python3 estimate_service_cost.py --service S1.1 --level 8 --breakdown
# List all 15 services with man-days
python3 estimate_service_cost.py --list-services
```

#### Cost Calculation (Role-Based)

```bash
python3 calculate_project_cost.py --role "Data Analyst" --level 8 --duration 6
python3 calculate_project_cost.py --role "Data Architect" --level 10 --duration 3 --unit month
python3 calculate_project_cost.py --list-roles
```

#### Flexible Competency-Based Pricing (Recommended for Government)

```python
from pricing_engine import calculate_gov_proposal_flexible, format_flexible_pricing_table
team = [
    {"role": "Chief Data Officer (CDO)", "education": "S2", "years_experience": 15},
    {"role": "Data Governance Lead", "education": "S2", "years_experience": 8},
    {"role": "Data Architect", "education": "S1", "years_experience": 6},
    {"role": "Data Analyst", "education": "S1", "years_experience": 3},
]
result = calculate_gov_proposal_flexible(team, months=6)
print(format_flexible_pricing_table(result))
# Education tiers: SMK | D3 | S1 | S2 | S3 (rates increase monotonically)
```

#### RAB/HPS Generation

```bash
python3 generate_rab.py --project "Ekosistem Data Jateng" --services S1.1,S1.2,S2.3 --level 10
python3 generate_rab.py --project "Portal Data" --services S2.3 --level 8 --output rab.csv
```

#### COGS Generation

Input JSON format — **flat rows**, one per role per feature:
```json
[
  {"feature": "Data Catalog", "role": "Data Architect", "level": "Senior", "man_days": 10, "priority": "Must Have"},
  {"feature": "Data Catalog", "role": "Data Engineer", "level": "Middle", "man_days": 15, "priority": "Must Have"}
]
```
Levels: `Senior` (maps to L10), `Middle` (L7), `Junior` (L3). Priority: `Must Have` | `Should Have` | `Could Have`.

```bash
python3 generate_cogs.py --input features.json
python3 generate_cogs.py --input features.json --software sw.json --hardware hw.json --operational ops.json
python3 generate_cogs.py --input features.json --priority must
python3 generate_cogs.py --input features.json --json 2>/dev/null  # Clean JSON output
```

#### Scenario Comparison

```bash
python3 scenario_model.py --quick S1.1 --levels 6,8,10
python3 scenario_model.py --quick S1.1,S2.3 --levels 8,12 --complexities 1.0,1.5
python3 scenario_model.py --scenarios scenarios.json
```

#### SPBE Client Intelligence

```bash
# Sort: opportunity | spbe_asc | spbe_desc | apbd | name
python3 query_spbe.py --top 10 --sort opportunity
# Filter by province, portal status, SPBE range
python3 query_spbe.py --province "Jawa Tengah" --portal-status not_accessible
python3 query_spbe.py --spbe-min 3.0 --spbe-max 4.0 --top 20
# Dataset: daerah (default) | kl | all
python3 query_spbe.py --type kl --top 10
# Pitch brief for specific region
python3 query_spbe.py --region "KOTA BANDUNG" --pitch-brief
```

#### Proposal & Pitch Generation

```bash
# Government proposal — output format auto-detected from extension
python3 generate_proposal.py --type proposal --client "Pemerintah Provinsi Jawa Tengah" \
  --sector government --services S1.1,S1.2,S1.3,S2.3 --headcount 12 --months 8 \
  --output proposal.md      # Markdown
python3 generate_proposal.py --type proposal --client "Pemda Jateng" --sector government \
  --services S1.1,S1.2,S1.3,S2.3 --headcount 12 --months 8 \
  --output proposal.pptx    # Direct PPTX (15 slides, professional layout)
python3 generate_proposal.py --type proposal --client "Pemda Jateng" --sector government \
  --services S1.1,S1.2,S1.3,S2.3 --headcount 12 --months 8 \
  --output proposal.docx    # Direct DOCX (8 tables, branded)

# Enterprise/BUMN pitch (Type A)
python3 generate_proposal.py --type pitch --client "PT KAI" --sector bumn \
  --services S1.1,S1.2,S2.4 --working-days 132 --price 575250000 --output pitch.md
# Sectors: government | enterprise | bumn | international | academia
```

#### Project Timeline (Mermaid Gantt)

```bash
python3 generate_timeline.py --services S1.1,S2.3 --start 2026-04-01 --output timeline.mmd
python3 generate_timeline.py --services S1.1 --start 2026-04-01 --team-size 5 --buffer 20
```
Render `.mmd` output using `Mermaid Chart:validate_and_render_mermaid_diagram` tool.

### Step 4: Generate Documents

**Primary** — Use Claude's built-in document skills (read the relevant SKILL.md first):
- `/mnt/skills/public/pdf/SKILL.md` for PDF
- `/mnt/skills/public/pptx/SKILL.md` for PPTX
- `/mnt/skills/public/docx/SKILL.md` for DOCX
- `/mnt/skills/public/xlsx/SKILL.md` for XLSX

**Fallback** — built-in scripts:
```bash
pip install python-pptx python-docx openpyxl --break-system-packages -q
python3 generate_document.py --input proposal.md --output proposal.pptx
python3 generate_document.py --input proposal.md --output proposal.docx
```

Key templates: `proposal-template.md`, `pitch-deck-template.md`, `surat-penawaran-template.md`, `boq-template.md`, `technical-proposal-template.md`, `business-proposal-template.md`, `assessment-report-template.md`, `policy-framework-template.md`, `training-material-template.md`, `data-product-canvas-template.md`, `service-description-template.md`, `output-deliverable-template.md`, `product-spec-template.md`, `knowledge-transfer-template.md`.

Brand logos: `templates/LogoIDEASLandscape.png`, `templates/LogoIDEASPotrait.png`, `templates/Logo_ideas.png`, `templates/LogoLandscape.png`.

### Step 5: Deliver

- **Client-facing** -> Indonesian | **Internal/technical** -> English
- Copy to `/mnt/user-data/outputs/` and use `present_files`

## Quick Reference: 15 Services

| Code | Service | Pillar | Man-Days |
|:---|:---|:---|:---|
| S1.1 | Data Strategy & Roadmap Development | Advisory | 91 |
| S1.2 | Data Governance & Compliance Framework | Advisory | 101 |
| S1.3 | Data Maturity Assessment & Benchmarking | Advisory | 62 |
| S1.4 | Data Governance & Policy Framework Dev | Advisory | 94 |
| S1.5 | Data Asset Valuation & Monetization | Advisory | 79 |
| S2.1 | Data-Centric Digital Product Dev & UX | Platform | 183 |
| S2.2 | Core Data Platform & Modernization | Platform | 141 |
| S2.3 | Government Data Portal Platform | Platform | 191 |
| S2.4 | Enterprise Data Portal & Self-Service | Platform | 97 |
| S2.5 | Secure Data Exchange - API Gateway | Platform | 110 |
| S2.6 | Analytics and Visualization Solutions | Platform | 64 |
| S3.1 | Data Literacy & Corporate Training | Empowerment | 73 |
| S3.2 | Center of Excellence Setup & Operations | Empowerment | 62 |
| S3.3 | Strategic Staffing & Expert Placement | Empowerment | 27 |
| S3.4 | Managed Data Services | Empowerment | 58 |

## Resource Index

- **`references/`** (28 files) — `company-profile.md`, `services-catalog.md`, `products-catalog.md`, `regulatory-standards.md`, `spbe-evaluation-framework.md`, `service-delivery-patterns.md`, `human-resources-and-pricing.md`, `task-decomposition.md`, `cogs-methodology.md`, `rab-hps-methodology.md`, `client-intelligence-spbe.md`, `portfolio-showcase-jabar.md`, `case-studies.md`, `competitive-landscape.md`, `proposal-patterns.md`, `project-administration-guide.md`, `thought-leadership-frameworks.md`, `data-ecosystem-knowledge-base.md`, `service-deliverables-map.md`, `agile-work-hierarchy.md`, `digital-data-product-lifecycle.md`, `dama-integration-map.md`, `business-frameworks.md`, `spbe-schema.md`, `spbe-2024-daerah.csv`, `spbe-2024-kl.csv`, `inaproc-digital-catalog.md`, `role-definitions.md`
- **`scripts/`** (18 files) — `rate_card.py`, `pricing_engine.py`, `estimate_service_cost.py`, `calculate_project_cost.py`, `recommend_service.py`, `generate_cogs.py`, `generate_proposal.py`, `build_proposal_docs.py`, `generate_rab.py`, `generate_document.py`, `generate_pdf.py`, `generate_pptx.py`, `generate_docx.py`, `query_spbe.py`, `scenario_model.py`, `generate_timeline.py`, `validate_skill.py`, `__init__.py`
- **`templates/`** (20 files) — `proposal-template.md`, `pitch-deck-template.md`, `surat-penawaran-template.md`, `boq-template.md`, `technical-proposal-template.md`, `business-proposal-template.md`, `assessment-report-template.md`, `policy-framework-template.md`, `training-material-template.md`, `data-product-canvas-template.md`, `service-description-template.md`, `output-deliverable-template.md`, `product-spec-template.md`, `knowledge-transfer-template.md`, `cogs-template.xlsx`, `rab-hps-template.csv`, `LogoIDEASLandscape.png`, `LogoIDEASPotrait.png`, `Logo_ideas.png`, `LogoLandscape.png`
- **`data/`** (1 file) — `services.json`

---
**Total Resources:** 68 files across 5 directories

> **Legal Entity:** PT Indonesian Data Ecosystem | **NIB:** 2207250135544
