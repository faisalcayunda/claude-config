---
name: data-mesh-architect
description: "Arsitek Data Mesh dan Data Governance untuk merancang dan mendokumentasikan data products end-to-end dari business brief apapun. Trigger untuk: data mesh, data product, domain mapping, data architecture, data product canvas, data contract, data catalog, pipeline documentation, data API documentation, data governance, federated governance checklist, data vocabulary, kamus data, business glossarium, data dictionary, access control matrix, RoPA, DPIA, data retention policy, data quality design, risk assessment, SCD, audit logging, infra brief, consumer onboarding guide, self-service infra guide, operations runbook, change log, backup DR plan, data science model, dataset artifact, migration report, analytical report, delivery phase, ways of working, RASCI, JIRA, sprint planning, UAT, EDA report. Berlaku untuk semua industri: pemerintahan, fintech, kesehatan, logistik, pendidikan, e-commerce."
---

# Data Mesh Architect Skill

Skill ini mengubah **business process brief apapun** menjadi arsitektur Data Mesh yang lengkap: dari pemetaan domain hingga dokumentasi teknis yang siap commit ke Git repository dengan kompatibilitas Docusaurus.

**Bahasa default: Bahasa Indonesia.** Ganti ke English hanya jika user secara eksplisit meminta.

---

## Quick Reference: Apa yang bisa skill ini hasilkan?

| Kebutuhan | File Referensi |
|---|---|
| Routing & overview lengkap | File ini (SKILL.md) |
| Framework Data Mesh + DAMA + Privacy | `references/framework.md` |
| Lifecycle + PM² + Ways of Working + RASCI | `references/lifecycle.md` |
| **Master index semua 47 template + gap status** | `templates/INDEX.md` |
| Bootstrap templates (B-01 s.d. B-05) | `templates/bootstrap/` |
| Design templates (D-01 s.d. D-13 + ADR-01) | `templates/design/` + `templates/decisions/` |
| Development templates (V-01 s.d. V-11) | `templates/development/` |
| Delivery templates (DLV-01, DLV-02) | `templates/delivery/` |
| Monitoring & Operations (M-02 s.d. M-07) | `templates/monitoring/` |
| Governance & Lifecycle (G-01 s.d. G-05 + E-01) | `templates/governance/` + `templates/eosl/` |
| Project Management (PM-01 s.d. PM-04) | `templates/project-management/` |
| **Referensi vocabulary kanonik (enum + regulasi)** | `references/data-vocabulary.md` |

---

## Konvensi Doc ID (X-Road style)

Setiap dokumen memiliki **Doc ID unik** yang wajib ada di frontmatter dan digunakan untuk cross-reference.

```
B-NN    Bootstrap        D-NN   Design            V-NN   Development
DLV-NN  Delivery         M-NN   Monitoring & Ops  E-NN   End of Service Life
G-NN    Governance       PM-NN  Project Mgmt      ADR-NN Architecture Decisions
```

**Format cross-reference:** `[D-02 Data Contract](../design/data-contract-spec.md)`

---

## Alur Kerja Utama

### LANGKAH 1 — Terima dan pahami Business Context Brief

Baca `references/framework.md` bagian "Context Intake" untuk checklist pertanyaan. Jika informasi kurang, ajukan pertanyaan klarifikasi **sebelum** memulai desain — satu pertanyaan per sesi.

**Yang harus dipahami dari brief:** tujuan bisnis & KPI, aktor utama, proses bisnis inti, entitas data, regulasi applicable, skala, dan organisasi yang terlibat.

---

### LANGKAH 2 — Domain Discovery dan Mapping

Baca `references/framework.md` bagian "Domain Mapping Methodology".

**Output:** Domain Map + Domain Relationship Diagram (Mermaid) + Data Product Inventory per domain.

---

### LANGKAH 3 — Produksi Dokumen Output

Gunakan `templates/INDEX.md` sebagai master navigasi. **Urutan produksi per Data Product:**

```
Bootstrap Phase:
  B-01  Business Process Research & Context
  B-02  Data Product Proposal
  B-03  Data Product Canvas
  B-04  Preliminary Data Profiling Report
  B-05  Preliminary EDA Report

Design Phase:
  D-01  Data Product Design Document
  D-02  Data Contract & Interface Specification
  D-03  Data Contract YAML
  D-04  Data Catalog & Metadata
  D-05  Data Quality Design
  D-06  Data Risk Assessment & Mitigation
  D-07  RoPA                                  [jika ada PII]
  D-08  DPIA                                  [jika high-risk]
  D-09  Infrastructure Brief
  D-11  Dashboard Design Document             [jika ada dashboard]
  D-12  SCD & Audit Logging Design            [jika butuh histori]
  D-13  Data Product Metrics & Insights Catalog
  ADR-01 Architecture Decision Record         [per keputusan]

Development Phase:
  V-01  Data Pipeline Brief
  V-02  Data API Brief                        [jika ada API output]
  V-03  UAT Template
  V-04  Integration Test Template
  V-05  Data Pipeline (implementasi)          ← as-built, pasangan V-01
  V-06  Data API (implementasi)               ← as-built, pasangan V-02
  V-07  Dashboard Development                 [jika ada dashboard]
  V-08  Data Science Model (model card)       [jika ada ML]
  V-09  Dataset (Table-View / Spreadsheet)    [jika output dataset]
  V-10  Migration Report                      [jika ada migrasi]
  V-11  Analytical Report                     [per laporan analitik]

Delivery Phase:
  DLV-01 Consumer Onboarding Guide
  DLV-02 Self-Service Infrastructure Guide    [jika consumer self-serve]

Monitoring & Operations Phase:
  M-02  Data Quality Report        (bulanan)
  M-03  Cost Report                (bulanan)
  M-04  Incident Management Template
  M-05  Backup & DR Plan
  M-06  Change Log
  M-07  Operations Runbook

Governance & Lifecycle (lintas semua data product):
  G-01  Data Vocabulary & Business Glossarium
  G-02  Data Access Control Matrix
  G-03  Data Dictionary
  G-04  Data Retention Policy
  G-05  Federated Governance Checklist
  E-01  End of Service Life Report

Project Management:
  PM-01 Ways of Working Document
  PM-02 RASCI Matrix
  PM-03 JIRA Structure & Epic Breakdown
  PM-04 Sprint Plan Template
```

---

### LANGKAH 4 — Project Management Structure

Baca `references/lifecycle.md` bagian "PM² + JIRA Structure". Output: sprint template, JIRA breakdown, RASCI, WoW, timeline.

---

## Format Output Markdown (Docusaurus-Compatible)

**Frontmatter wajib setiap dokumen:**

```yaml
---
title: "[Nama Dokumen]"
sidebar_label: "[Label Singkat]"
sidebar_position: [nomor]
description: "[Deskripsi singkat]"
tags: [data-product, [domain-name], [phase]]
doc_id: "[X-NN]"
data_product_id: "[domain/product-name/versi]"
data_product_owner: "[Nama Domain]"
data_classification: "[Public|Internal|Restricted|Confidential]"
phase: "[bootstrap|design|development|delivery|monitoring|governance|eosl]"
version: "[semver]"
last_updated: "[YYYY-MM-DD]"
pii_flag: [true|false]
---
```

**Dua section wajib setelah H1 (pola X-Road):**

```markdown
## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `X-NN` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Versi Data Product** | `<vX.Y.Z>` |
| **Penanggung Jawab** | `<Role: Nama, Email>` |
| **Dokumen terkait** | [X-NN Judul](../path/file.md) |

---
```

**Aturan formatting:**
- H1 hanya satu; H2 untuk seksi utama dengan nomor (1., 2.); H3 untuk sub-seksi (1.1, 1.2)
- Admonitions: `:::note`, `:::warning`, `:::tip`, `:::danger`
- Code blocks dengan language tag; Mermaid untuk diagram
- Internal links menggunakan path relatif + Doc ID: `[D-02 Data Contract](../design/data-contract-spec.md)`

---

## Struktur Direktori Git (lengkap, 47 dokumen)

```
{domain-name}/
├── {data-product-name}/
│   ├── README.md
│   ├── bootstrap/
│   │   ├── business-process-research.md   B-01
│   │   ├── proposal.md                    B-02
│   │   ├── canvas.md                      B-03
│   │   ├── data-profiling-prelim.md       B-04
│   │   └── eda-template.md                B-05
│   ├── design/
│   │   ├── design-document.md             D-01
│   │   ├── data-contract-spec.md          D-02
│   │   ├── data-contract.yaml             D-03
│   │   ├── data-catalog.md                D-04
│   │   ├── quality-design.md              D-05
│   │   ├── risk-assessment.md             D-06/D-07/D-08
│   │   ├── infra-brief.md                 D-09
│   │   ├── dashboard-design.md            D-11
│   │   ├── scd-audit-design.md            D-12
│   │   └── metrics-catalog.md             D-13
│   ├── development/
│   │   ├── pipeline-brief.md              V-01
│   │   ├── api-brief.md                   V-02
│   │   ├── uat-integration-test.md        V-03/V-04
│   │   ├── data-pipeline.md               V-05 (as-built)
│   │   ├── data-api.md                    V-06 (as-built)
│   │   ├── dashboard-development.md       V-07
│   │   ├── data-science-model.md          V-08
│   │   ├── dataset-artifact.md            V-09
│   │   ├── migration-report.md            V-10
│   │   └── analytical-report.md           V-11
│   ├── delivery/
│   │   ├── consumer-onboarding-guide.md   DLV-01
│   │   └── self-service-infra-guide.md    DLV-02
│   ├── monitoring/
│   │   ├── operational-reports.md         M-02/M-03/M-04
│   │   ├── backup-dr-plan.md              M-05
│   │   ├── change-log.md                  M-06
│   │   └── operations-runbook.md          M-07
│   └── eosl/
│       └── eosl-report.md                 E-01
├── decisions/
│   └── ADR-NNNN-[judul].md                ADR-01
├── governance/
│   ├── data-vocabulary-template.md        G-01
│   ├── data-access-control-matrix.md      G-02
│   ├── data-dictionary.md                 G-03
│   ├── data-retention-policy.md           G-04
│   └── federated-governance-checklist.md  G-05
└── project-management/
    ├── ways-of-working.md                 PM-01
    ├── rasci-matrix.md                    PM-02
    ├── jira-structure.md                  PM-03
    └── sprint-plan.md                     PM-04
```

---

## Pipeline Jenkins → Docusaurus → Confluence → Google Drive

Baca `references/documentation.md` untuk Jenkinsfile lengkap dan konfigurasi.

```
Git commit/PR → Jenkins trigger
  → Lint markdown + Validate frontmatter (cek doc_id, version, phase)
  → Build Docusaurus (npm run build)
  → Deploy ke hosting
  → Sync ke Confluence (mark CLI)
  → Export ke Google Drive (gdrive API)
  → Notify Slack/Teams
```

---

## Compliance Check Wajib

**Quick check (jawab sebelum desain Data Contract):**
- [ ] Apakah data product memproses Nama, NIK, Alamat, Nomor Telepon, Email?
- [ ] Apakah memproses data kesehatan, biometrik, genetik, agama, atau data anak?
- [ ] Apakah ada profiling, scoring, atau keputusan otomatis atas individu?
- [ ] Berapa volume data subjek yang terdampak? (>1.000 → DPIA wajib)

Jika satu atau lebih "Ya" → DPIA wajib, RoPA wajib, data classification ≥ Restricted.
Gunakan **G-05 Federated Governance Checklist** Bagian E untuk verifikasi compliance lengkap.

---

## Cara Membaca Skill Ini

```
SKILL.md          → Overview, routing, konvensi
references/       → Framework, methodology, standar mendalam
templates/INDEX.md → Master registry 47 template
templates/*/      → Template siap pakai per fase
```

---

## Catatan Penting

1. **Skill ini bersifat context-driven** — business brief yang diberikan user menentukan isi konten.
2. **Jangan hardcode domain atau entitas bisnis spesifik** — selalu derive dari brief.
3. **Selalu tanya dahulu** jika brief tidak cukup untuk merancang domain yang kohesif.
4. **doc_id wajib di semua output** — setiap dokumen harus punya `doc_id` di frontmatter + Riwayat Versi + Header Identifikasi.
5. **Cross-reference menggunakan Doc ID** — format `[D-02 Data Contract](../path)`.
6. **Gunakan `/dama-research`** untuk pendalaman DAMA-DMBOK2 spesifik.
7. **Gunakan `/ideas-company`** untuk proyek IDEAS/klien IDEAS.
8. **Gunakan `/data-mesh-docs-boilerplate`** untuk scaffold Git repo lengkap 47 template.
