#!/usr/bin/env bash
# init-repo.sh  v2.0
# Bootstrap a complete Docusaurus data mesh docs repository — 47 documents.
#
# Usage:
#   bash scripts/init-repo.sh \
#     --project  "program-makan-bergizi" \
#     --domain   "pendidikan" \
#     --products "master-data-sekolah,profil-peserta-didik" \
#     --surge-domain "mbg-docs.surge.sh" \
#     [--enable-gdrive] [--enable-confluence] \
#     [--confluence-url "https://org.atlassian.net"] \
#     [--confluence-space "DATAMESH"] \
#     [--output-dir "./"]

set -euo pipefail

PROJECT=""
DOMAIN=""
PRODUCTS=""
SURGE_DOMAIN=""
ENABLE_GDRIVE=false
ENABLE_CONFLUENCE=false
CONFLUENCE_URL=""
CONFLUENCE_SPACE="DATAMESH"
OUTPUT_DIR="."

while [[ $# -gt 0 ]]; do
    case $1 in
        --project)           PROJECT="$2";           shift 2 ;;
        --domain)            DOMAIN="$2";            shift 2 ;;
        --products)          PRODUCTS="$2";          shift 2 ;;
        --surge-domain)      SURGE_DOMAIN="$2";      shift 2 ;;
        --enable-gdrive)     ENABLE_GDRIVE=true;     shift ;;
        --enable-confluence) ENABLE_CONFLUENCE=true; shift ;;
        --confluence-url)    CONFLUENCE_URL="$2";    shift 2 ;;
        --confluence-space)  CONFLUENCE_SPACE="$2";  shift 2 ;;
        --output-dir)        OUTPUT_DIR="$2";        shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

if [[ -z "$PROJECT" || -z "$DOMAIN" || -z "$PRODUCTS" ]]; then
    echo "❌ --project, --domain, and --products are required."
    exit 1
fi

SURGE_DOMAIN="${SURGE_DOMAIN:-${PROJECT}.surge.sh}"
REPO_DIR="${OUTPUT_DIR}/${PROJECT}-docs"
IFS=',' read -ra PRODUCT_LIST <<< "$PRODUCTS"
TODAY=$(date +%Y-%m-%d)

echo "🚀 Scaffolding: ${REPO_DIR} (47 documents)"
echo "   Domain   : ${DOMAIN}"
echo "   Products : ${PRODUCTS}"

# ── Root structure ────────────────────────────────────────────────────────────
mkdir -p \
    "${REPO_DIR}/.github" \
    "${REPO_DIR}/scripts" \
    "${REPO_DIR}/static/img" \
    "${REPO_DIR}/src/css" \
    "${REPO_DIR}/docs/governance" \
    "${REPO_DIR}/docs/decisions" \
    "${REPO_DIR}/docs/project-management"

# ── Per-product directories ───────────────────────────────────────────────────
for PRODUCT in "${PRODUCT_LIST[@]}"; do
    PRODUCT=$(echo "$PRODUCT" | xargs)
    BASE="${REPO_DIR}/docs/${DOMAIN}/${PRODUCT}"
    mkdir -p \
        "${BASE}/bootstrap" \
        "${BASE}/design" \
        "${BASE}/development" \
        "${BASE}/delivery" \
        "${BASE}/monitoring" \
        "${BASE}/eosl"
done

# ── Helper: write frontmatter + section stubs ────────────────────────────────
# write_fm FILE TITLE LABEL POSITION PHASE PRODUCT_ID TAGS DOC_ID
write_fm() {
    local file="$1" title="$2" label="$3" pos="$4"
    local phase="$5" product_id="$6" tags="$7" doc_id="$8"

    cat > "$file" <<FRONTMATTER
---
title: "${title}"
sidebar_label: "${label}"
sidebar_position: ${pos}
description: "TODO: Deskripsi singkat dokumen ini."
tags: [${tags}]
doc_id: "${doc_id}"
data_product_id: "${DOMAIN}/${product_id}/v1"
data_product_owner: "TODO: Nama Domain Owner"
data_classification: "Internal"
phase: "${phase}"
version: "0.1.0"
last_updated: "${TODAY}"
pii_flag: false
---

# ${title}

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| \`${TODAY}\` | 0.1 | Draft awal | \`TODO: Nama, Role\` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | \`${doc_id}\` |
| **Domain** | \`${DOMAIN}\` |
| **Data Product** | \`${product_id}\` |
| **Versi Data Product** | \`v0.1.0\` |
| **Penanggung Jawab** | \`TODO: Role — Nama, Email\` |
| **Dokumen terkait** | TODO |

---

:::tip Cara Mengisi
Gunakan \`/data-mesh-architect\` skill untuk mengisi dokumen ini berdasarkan business context brief Anda.
:::

> **Status:** 🚧 Draft — Belum diisi

FRONTMATTER
}

# ── Scaffold per product ──────────────────────────────────────────────────────
for PRODUCT in "${PRODUCT_LIST[@]}"; do
    PRODUCT=$(echo "$PRODUCT" | xargs)
    BASE="${REPO_DIR}/docs/${DOMAIN}/${PRODUCT}"
    PT=$(echo "$PRODUCT" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2); print}')

    echo "  📁 Scaffolding: ${PRODUCT} (47 docs)"

    # README
    cat > "${BASE}/README.md" <<README
---
title: "Overview — ${PT}"
sidebar_label: "📋 Overview"
sidebar_position: 1
doc_id: "README"
data_product_id: "${DOMAIN}/${PRODUCT}/v1"
data_product_owner: "TODO"
data_classification: "Internal"
phase: "bootstrap"
version: "0.1.0"
last_updated: "${TODAY}"
pii_flag: false
---

# ${PT}

| Atribut | Nilai |
|---|---|
| Domain | \`${DOMAIN}\` |
| Data Product ID | \`${DOMAIN}/${PRODUCT}/v1\` |
| Owner | TODO |
| Fase Saat Ini | Bootstrap |
| Klasifikasi | Internal |

## Quick Links

| Fase | Dokumen |
|---|---|
| 🟡 Bootstrap | [B-01](./bootstrap/business-process-research.md) · [B-02 Proposal](./bootstrap/proposal.md) · [B-03 Canvas](./bootstrap/canvas.md) · [B-04 Profiling](./bootstrap/data-profiling-prelim.md) · [B-05 EDA](./bootstrap/eda-template.md) |
| 🔵 Design | [D-01 Design](./design/design-document.md) · [D-02 Contract](./design/data-contract-spec.md) · [D-04 Catalog](./design/data-catalog.md) · [D-13 Metrics](./design/metrics-catalog.md) |
| 🟢 Development | [V-01 Pipeline Brief](./development/pipeline-brief.md) · [V-05 Pipeline](./development/data-pipeline.md) · [V-02 API Brief](./development/api-brief.md) · [V-06 API](./development/data-api.md) |
| 🚀 Delivery | [DLV-01 Onboarding](./delivery/consumer-onboarding-guide.md) · [DLV-02 Self-Service](./delivery/self-service-infra-guide.md) |
| 📊 Monitoring | [M-07 Runbook](./monitoring/operations-runbook.md) · [M-05 Backup DR](./monitoring/backup-dr-plan.md) · [M-06 Changelog](./monitoring/change-log.md) |
| 🏛️ Governance | [G-01 Vocabulary](../../governance/data-vocabulary.md) · [G-02 Access Control](../../governance/data-access-control-matrix.md) · [G-05 Gov Checklist](../../governance/federated-governance-checklist.md) |

## Deskripsi

> TODO: Deskripsikan data product ini — apa yang dihasilkan, siapa konsumennya, dan nilai bisnis utamanya.
README

    # CHANGELOG (doc-history, berbeda dari M-06 change-log)
    cat > "${BASE}/CHANGELOG.md" <<CHANGELOG
---
title: "Doc History — ${PT}"
sidebar_label: "📝 Doc History"
sidebar_position: 99
doc_id: "CHANGELOG"
data_product_id: "${DOMAIN}/${PRODUCT}/v1"
data_classification: "Internal"
phase: "bootstrap"
version: "0.1.0"
last_updated: "${TODAY}"
pii_flag: false
---

# Document History — ${PT}

Format: [Keep a Changelog](https://keepachangelog.com/) · Versi: [SemVer](https://semver.org/)
**Diupdate otomatis oleh Jenkins saat merge ke \`main\`.**

> **Catatan:** Ini adalah riwayat *dokumen* ini (kapan ditulis/direvisi).
> Untuk riwayat *perubahan data product* (schema, SLA), lihat [M-06 Change Log](./monitoring/change-log.md).

---

## [Unreleased]

---
CHANGELOG

    # ── Bootstrap ──────────────────────────────────────────────────────────────
    write_fm "${BASE}/bootstrap/business-process-research.md" \
        "Business Process Research — ${PT}" "B-01 Business Research" 1 \
        "bootstrap" "$PRODUCT" "bootstrap,business-process" "B-01"
    echo -e "\n## 1. Tujuan Bisnis\n\nTODO\n\n## 2. Proses Bisnis\n\nTODO\n\n## 3. Stakeholder\n\nTODO" \
        >> "${BASE}/bootstrap/business-process-research.md"

    write_fm "${BASE}/bootstrap/proposal.md" \
        "Data Product Proposal — ${PT}" "B-02 Proposal" 2 \
        "bootstrap" "$PRODUCT" "bootstrap,proposal" "B-02"
    echo -e "\n## 1. Problem Statement\n\nTODO\n\n## 2. Solusi yang Diusulkan\n\nTODO\n\n## 3. Value Proposition\n\nTODO" \
        >> "${BASE}/bootstrap/proposal.md"

    write_fm "${BASE}/bootstrap/canvas.md" \
        "Data Product Canvas — ${PT}" "B-03 Canvas" 3 \
        "bootstrap" "$PRODUCT" "bootstrap,canvas" "B-03"

    write_fm "${BASE}/bootstrap/data-profiling-prelim.md" \
        "Preliminary Data Profiling — ${PT}" "B-04 Data Profiling" 4 \
        "bootstrap" "$PRODUCT" "bootstrap,data-profiling" "B-04"

    write_fm "${BASE}/bootstrap/eda-template.md" \
        "Preliminary EDA Report — ${PT}" "B-05 EDA Report" 5 \
        "bootstrap" "$PRODUCT" "bootstrap,eda,exploratory-analysis" "B-05"

    # ── Design ─────────────────────────────────────────────────────────────────
    write_fm "${BASE}/design/design-document.md" \
        "Design Document — ${PT}" "D-01 Design" 1 \
        "design" "$PRODUCT" "design,architecture" "D-01"

    write_fm "${BASE}/design/data-contract-spec.md" \
        "Data Contract Specification — ${PT}" "D-02 Contract Spec" 2 \
        "design" "$PRODUCT" "design,data-contract" "D-02"

    # D-03: Data Contract YAML
    cat > "${BASE}/design/data-contract.yaml" <<YAML
# D-03: Data Contract YAML — ${PT}
# doc_id: D-03
# Generated: ${TODAY}
# Fill using /data-mesh-architect skill

apiVersion: v2
kind: DataContract
metadata:
  id: "${DOMAIN}/${PRODUCT}/v1"
  version: "0.1.0"
  domain: "${DOMAIN}"
  name: "${PRODUCT}"
  owner: "TODO: Domain Owner"
  classification: "Internal"
  pii: false
  created: "${TODAY}"

schema:
  - name: TODO_TABLE_NAME
    description: "TODO"
    columns:
      - name: id
        type: UUID
        nullable: false
        pii: false
        description: "Primary key"

sla:
  availability: "99.5%"
  freshness: "daily"
  latency_p95_ms: 500

quality:
  completeness: "> 99%"
  uniqueness: "100% on primary key"

consumers:
  - name: "TODO"
    contact: "TODO"
YAML

    write_fm "${BASE}/design/data-catalog.md" \
        "Data Catalog & Metadata — ${PT}" "D-04 Data Catalog" 4 \
        "design" "$PRODUCT" "design,catalog,metadata" "D-04"

    write_fm "${BASE}/design/quality-design.md" \
        "Data Quality Design — ${PT}" "D-05 Quality Design" 5 \
        "design" "$PRODUCT" "design,quality" "D-05"

    write_fm "${BASE}/design/risk-assessment.md" \
        "Risk Assessment & Privacy — ${PT}" "D-06 Risk & Privacy" 6 \
        "design" "$PRODUCT" "design,risk,privacy,ropa,dpia" "D-06"

    write_fm "${BASE}/design/infra-brief.md" \
        "Infrastructure Brief — ${PT}" "D-09 Infra" 9 \
        "design" "$PRODUCT" "design,infrastructure" "D-09"

    write_fm "${BASE}/design/dashboard-design.md" \
        "Dashboard Design — ${PT}" "D-11 Dashboard Design" 11 \
        "design" "$PRODUCT" "design,dashboard" "D-11"

    write_fm "${BASE}/design/scd-audit-design.md" \
        "SCD & Audit Logging Design — ${PT}" "D-12 SCD & Audit" 12 \
        "design" "$PRODUCT" "design,scd,audit" "D-12"

    write_fm "${BASE}/design/metrics-catalog.md" \
        "Data Product Metrics & Insights Catalog — ${PT}" "D-13 Metrics Catalog" 13 \
        "design" "$PRODUCT" "design,metrics,slo,insights" "D-13"

    # ── Development ────────────────────────────────────────────────────────────
    write_fm "${BASE}/development/pipeline-brief.md" \
        "Data Pipeline Brief — ${PT}" "V-01 Pipeline Brief" 1 \
        "development" "$PRODUCT" "development,pipeline" "V-01"

    write_fm "${BASE}/development/api-brief.md" \
        "Data API Brief — ${PT}" "V-02 API Brief" 2 \
        "development" "$PRODUCT" "development,api" "V-02"

    write_fm "${BASE}/development/uat-integration-test.md" \
        "UAT & Integration Test — ${PT}" "V-03 UAT" 3 \
        "development" "$PRODUCT" "development,uat,testing" "V-03"

    write_fm "${BASE}/development/data-pipeline.md" \
        "Data Pipeline — ${PT}" "V-05 Data Pipeline" 5 \
        "development" "$PRODUCT" "development,pipeline,implementation" "V-05"
    echo -e "\n:::note\nIni adalah dokumentasi implementasi aktual pipeline (as-built). Spec desain ada di [V-01 Pipeline Brief](./pipeline-brief.md).\n:::" \
        >> "${BASE}/development/data-pipeline.md"

    write_fm "${BASE}/development/data-api.md" \
        "Data API — ${PT}" "V-06 Data API" 6 \
        "development" "$PRODUCT" "development,api,implementation,rest-api" "V-06"
    echo -e "\n:::note\nIni adalah dokumentasi API yang sudah di-deploy (living reference). Spec desain ada di [V-02 API Brief](./api-brief.md).\n:::" \
        >> "${BASE}/development/data-api.md"

    write_fm "${BASE}/development/dashboard-development.md" \
        "Dashboard Development — ${PT}" "V-07 Dashboard Dev" 7 \
        "development" "$PRODUCT" "development,dashboard,implementation" "V-07"

    write_fm "${BASE}/development/data-science-model.md" \
        "Data Science Model — ${PT}" "V-08 Model Card" 8 \
        "development" "$PRODUCT" "development,ml,model-card,mlops" "V-08"

    write_fm "${BASE}/development/dataset-artifact.md" \
        "Dataset — ${PT}" "V-09 Dataset" 9 \
        "development" "$PRODUCT" "development,dataset,artifact" "V-09"

    write_fm "${BASE}/development/migration-report.md" \
        "Migration Report — ${PT}" "V-10 Migration" 10 \
        "development" "$PRODUCT" "development,migration,validation" "V-10"

    write_fm "${BASE}/development/analytical-report.md" \
        "Analytical Report — ${PT}" "V-11 Analytical Report" 11 \
        "development" "$PRODUCT" "development,analytics,report,insights" "V-11"

    # ── Delivery ───────────────────────────────────────────────────────────────
    write_fm "${BASE}/delivery/consumer-onboarding-guide.md" \
        "Consumer Onboarding Guide — ${PT}" "DLV-01 Onboarding" 1 \
        "delivery" "$PRODUCT" "delivery,onboarding,consumer" "DLV-01"
    echo -e "\n## 1. Pendahuluan\n\nTODO: Panduan onboarding consumer dari zero hingga first successful query.\n\n## 2. Prasyarat\n\nTODO\n\n## 3. Provisioning Akses\n\nTODO\n\n## 4. Quick Start\n\nTODO" \
        >> "${BASE}/delivery/consumer-onboarding-guide.md"

    write_fm "${BASE}/delivery/self-service-infra-guide.md" \
        "Self-Service Infrastructure Guide — ${PT}" "DLV-02 Self-Service" 2 \
        "delivery" "$PRODUCT" "delivery,self-service,infrastructure" "DLV-02"

    # ── Monitoring ─────────────────────────────────────────────────────────────
    write_fm "${BASE}/monitoring/operational-reports.md" \
        "Operational Reports — ${PT}" "M-02 Reports" 2 \
        "monitoring" "$PRODUCT" "monitoring,quality,cost,incident" "M-02"

    write_fm "${BASE}/monitoring/backup-dr-plan.md" \
        "Backup & DR Plan — ${PT}" "M-05 Backup & DR" 5 \
        "monitoring" "$PRODUCT" "monitoring,backup,disaster-recovery,rto,rpo" "M-05"

    write_fm "${BASE}/monitoring/change-log.md" \
        "Change Log — ${PT}" "M-06 Change Log" 6 \
        "monitoring" "$PRODUCT" "monitoring,changelog,versioning,breaking-change" "M-06"
    cat >> "${BASE}/monitoring/change-log.md" <<CHANGELOG_STUB

## [Unreleased]

---

## v0.1.0 — ${TODAY} (Initial Release)

### Features
- TODO: Daftarkan perubahan pertama di sini menggunakan format `[ADDITIVE]`, `[BREAKING]`, `[DATA-FIX]`, `[PATCH]`, `[DOCS]`
CHANGELOG_STUB

    write_fm "${BASE}/monitoring/operations-runbook.md" \
        "Operations Runbook — ${PT}" "M-07 Runbook" 7 \
        "monitoring" "$PRODUCT" "monitoring,operations,runbook,incident-response,sre" "M-07"
    echo -e "\n## 1. Quick Reference\n\nTODO: Isi kontak, links Airflow, Grafana, Data Catalog.\n\n## 2. Klasifikasi Insiden\n\nTODO\n\n## 3. Prosedur Health Check\n\nTODO" \
        >> "${BASE}/monitoring/operations-runbook.md"

    # ── EoSL ───────────────────────────────────────────────────────────────────
    write_fm "${BASE}/eosl/eosl-report.md" \
        "End of Service Life Report — ${PT}" "E-01 EoSL" 1 \
        "eosl" "$PRODUCT" "eosl,retirement,archival" "E-01"

done

# ── Governance ────────────────────────────────────────────────────────────────
echo "  📁 Scaffolding: governance (5 documents)"

write_fm "${REPO_DIR}/docs/governance/data-vocabulary.md" \
    "Data Vocabulary & Business Glossarium" "G-01 Vocabulary" 1 \
    "governance" "governance" "governance,vocabulary,glossarium" "G-01"

write_fm "${REPO_DIR}/docs/governance/data-access-control-matrix.md" \
    "Data Access Control Matrix" "G-02 Access Control" 2 \
    "governance" "governance" "governance,access-control,rbac,security" "G-02"

write_fm "${REPO_DIR}/docs/governance/data-dictionary.md" \
    "Data Dictionary" "G-03 Data Dictionary" 3 \
    "governance" "governance" "governance,data-dictionary,schema,metadata" "G-03"
echo -e "\n## 1. Inventori Tabel\n\nTODO\n\n## 2. Data Dictionary per Objek\n\nTODO\n\n## 3. Enum Values\n\nTODO" \
    >> "${REPO_DIR}/docs/governance/data-dictionary.md"

write_fm "${REPO_DIR}/docs/governance/data-retention-policy.md" \
    "Data Retention Policy" "G-04 Retention Policy" 4 \
    "governance" "governance" "governance,data-retention,privacy,compliance,uu-pdp" "G-04"

write_fm "${REPO_DIR}/docs/governance/federated-governance-checklist.md" \
    "Federated Governance Checklist" "G-05 Gov Checklist" 5 \
    "governance" "governance" "governance,federated-governance,compliance,lifecycle-gate" "G-05"

# ── Project Management ────────────────────────────────────────────────────────
echo "  📁 Scaffolding: project-management (4 documents)"

write_fm "${REPO_DIR}/docs/project-management/ways-of-working.md" \
    "Ways of Working" "PM-01 Ways of Working" 1 \
    "project-management" "project-management" "project-management,ways-of-working" "PM-01"

write_fm "${REPO_DIR}/docs/project-management/rasci-matrix.md" \
    "RASCI Matrix" "PM-02 RASCI" 2 \
    "project-management" "project-management" "project-management,rasci,responsibility" "PM-02"

write_fm "${REPO_DIR}/docs/project-management/jira-structure.md" \
    "JIRA Structure & Epic Breakdown" "PM-03 JIRA" 3 \
    "project-management" "project-management" "project-management,jira,backlog" "PM-03"

write_fm "${REPO_DIR}/docs/project-management/sprint-plan.md" \
    "Sprint Plan Template" "PM-04 Sprint Plan" 4 \
    "project-management" "project-management" "project-management,sprint,agile" "PM-04"

# ── ADR template ──────────────────────────────────────────────────────────────
cat > "${REPO_DIR}/docs/decisions/ADR-0001-template.md" <<ADR
---
title: "ADR-0001: [Judul Keputusan]"
sidebar_label: "ADR-0001"
sidebar_position: 1
doc_id: "ADR-01"
data_product_id: "${DOMAIN}/decisions/v1"
data_product_owner: "TODO"
data_classification: "Internal"
phase: "design"
status: "proposed"
date: "${TODAY}"
version: "0.1.0"
last_updated: "${TODAY}"
pii_flag: false
---

# ADR-0001: [Judul Keputusan Arsitektur]

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| \`${TODAY}\` | 0.1 | Draft | \`TODO\` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | \`ADR-01\` |
| **Status** | \`Proposed\` |
| **Tanggal** | \`${TODAY}\` |
| **Pembuat Keputusan** | \`TODO: Nama DA\` |

---

## Konteks dan Masalah

TODO: Apa permasalahan yang mendorong keputusan ini?

## Opsi yang Dipertimbangkan

- Opsi A: TODO
- Opsi B: TODO

## Keputusan

**Opsi yang dipilih: TODO**

Alasan: TODO

## Konsekuensi

**Positif:** TODO
**Negatif / Risiko:** TODO
ADR

# ── Intro page ────────────────────────────────────────────────────────────────
cat > "${REPO_DIR}/docs/intro.md" <<INTRO
---
title: "Data Mesh Documentation Hub"
sidebar_label: "🏠 Overview"
sidebar_position: 1
doc_id: "INTRO"
data_product_id: "root/intro/v1"
data_product_owner: "${PROJECT}"
data_classification: "Internal"
phase: "bootstrap"
version: "0.1.0"
last_updated: "${TODAY}"
pii_flag: false
---

# Data Mesh Docs — ${PROJECT}

Selamat datang di dokumentasi terpusat **${PROJECT}** Data Mesh.

| Info | Detail |
|---|---|
| Project | \`${PROJECT}\` |
| Domain | \`${DOMAIN}\` |
| Data Products | ${PRODUCTS} |
| Site | [${SURGE_DOMAIN}](https://${SURGE_DOMAIN}) |

## Navigasi

- 📦 **Data Products** — 47 dokumen per data product (Bootstrap → EoSL)
- 🏛️ **Governance** — G-01 Vocabulary, G-02 Access Control, G-03 Dictionary, G-04 Retention, G-05 Checklist
- 🗂️ **Project Management** — PM-01 Ways of Working, PM-02 RASCI, PM-03 JIRA, PM-04 Sprint
- 🧭 **Decisions (ADR)** — Architecture Decision Records

## Document Index (47 Templates)

| Code | Document | Phase |
|---|---|---|
| B-01 – B-05 | Business Research, Proposal, Canvas, Profiling, EDA | Bootstrap |
| D-01 – D-13 | Design, Contract, Catalog, Quality, Risk, Infra, Dashboard, SCD, Metrics + ADR | Design |
| V-01 – V-11 | Pipeline Brief+Doc, API Brief+Doc, UAT, Dashboard Dev, Model, Dataset, Migration, Report | Development |
| DLV-01, DLV-02 | Consumer Onboarding, Self-Service Infra | Delivery |
| M-02 – M-07 | Quality Report, Cost, Incident, Backup DR, Change Log, Runbook | Monitoring |
| G-01 – G-05, E-01 | Vocabulary, Access Control, Dictionary, Retention, Gov Checklist, EoSL | Governance |
| PM-01 – PM-04 | Ways of Working, RASCI, JIRA, Sprint Plan | Project Mgmt |

## Cara Berkontribusi

1. Clone repo ini
2. Buat branch: \`feature/[DOC_ID]-[deskripsi]\` (contoh: \`feature/D-02-data-contract-spec\`)
3. Isi dokumen menggunakan \`/data-mesh-architect\` skill
4. Push dan buat PR ke \`develop\`
5. Merge ke \`develop\` → auto preview
6. Release via \`release/vX.Y.Z\` → auto deploy + doc history update
INTRO

# ── Config files ──────────────────────────────────────────────────────────────
echo "  📄 Writing config files"

cat > "${REPO_DIR}/.gitignore" <<GITIGNORE
node_modules/
.docusaurus/
build/
.env
*.local
.DS_Store
__pycache__/
*.pyc
*.egg-info/
dist/
*.tmp
GITIGNORE

cat > "${REPO_DIR}/.env.example" <<ENVEXAMPLE
# ── Surge.sh ──────────────────────────────────────────────────────────────────
SURGE_DOMAIN=${SURGE_DOMAIN}
SURGE_TOKEN=          # Run: npx surge token

# ── Docusaurus ────────────────────────────────────────────────────────────────
DOCS_TITLE=${PROJECT} Data Mesh Docs
DOCS_URL=https://${SURGE_DOMAIN}
REPO_URL=https://github.com/your-org/${PROJECT}-docs

# ── Google Drive (set GDRIVE_ENABLED=true to activate) ────────────────────────
GDRIVE_ENABLED=${ENABLE_GDRIVE}
GDRIVE_SERVICE_ACCOUNT_JSON=/path/to/service-account.json
GDRIVE_FOLDER_ID=
GDRIVE_SHARE_EMAILS=

# ── Confluence (set CONFLUENCE_ENABLED=true to activate) ──────────────────────
CONFLUENCE_ENABLED=${ENABLE_CONFLUENCE}
CONFLUENCE_URL=${CONFLUENCE_URL}
CONFLUENCE_SPACE=${CONFLUENCE_SPACE}
CONFLUENCE_USERNAME=your-email@example.com
CONFLUENCE_API_TOKEN=
CONFLUENCE_PARENT_PAGE_ID=

# ── Slack notifications (optional) ────────────────────────────────────────────
SLACK_ENABLED=false
SLACK_WEBHOOK_URL=
ENVEXAMPLE

cat > "${REPO_DIR}/.github/CODEOWNERS" <<CODEOWNERS
*                              @data-mesh-team
/docs/${DOMAIN}/               @${DOMAIN}-domain-team
/docs/governance/              @data-governance-team
/docs/project-management/      @project-management-team
/Jenkinsfile                   @devops-team
/scripts/                      @devops-team
CODEOWNERS

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for script in sync-gdrive.py sync-confluence.py update-doc-history.sh; do
    [[ -f "${SCRIPT_DIR}/../scripts/${script}" ]] && \
        cp "${SCRIPT_DIR}/../scripts/${script}" "${REPO_DIR}/scripts/${script}"
done
[[ -f "${SCRIPT_DIR}/../assets/Jenkinsfile" ]] && \
    cp "${SCRIPT_DIR}/../assets/Jenkinsfile" "${REPO_DIR}/Jenkinsfile"

cat > "${REPO_DIR}/QUICKSTART.md" <<QUICKSTART
# Quickstart — ${PROJECT} Docs

## 1. Install dependencies
\`\`\`bash
cd ${PROJECT}-docs && npm install
\`\`\`

## 2. Copy env file
\`\`\`bash
cp .env.example .env  # Edit dengan nilai yang sesuai
\`\`\`

## 3. Run locally
\`\`\`bash
npm start   # http://localhost:3000
\`\`\`

## 4. Deploy ke surge.sh
\`\`\`bash
npm run build && npx surge build/ ${SURGE_DOMAIN}
\`\`\`

## 5. Isi dokumen
Semua file sudah di-scaffold. Gunakan \`/data-mesh-architect\` Claude skill
untuk mengisi setiap placeholder berdasarkan business context brief Anda.

## 6. Git Flow
- Tulis dokumen di branch \`feature/[DOC_ID]-[deskripsi]\`
- PR ke \`develop\` → auto preview di surge.sh
- Release via \`release/vX.Y.Z\` → auto deploy ke main + doc history update
QUICKSTART

echo ""
echo "✅ Repository scaffolded: ${REPO_DIR}"
echo "   47 documents created per data product"
echo ""
echo "Next steps:"
echo "  1. cd ${REPO_DIR}"
echo "  2. cp .env.example .env && edit .env"
echo "  3. npm install && npm start"
echo "  4. Fill documents using /data-mesh-architect skill"
