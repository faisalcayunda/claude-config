---
name: data-mesh-docs-boilerplate
description: >
  Generate a complete Docusaurus-based Git repository boilerplate for Data Mesh documentation,
  wired to the /data-mesh-architect document library (47 templates, full lifecycle).
  Trigger whenever the user asks to: scaffold a data mesh docs repo, create a documentation
  site for data products, generate Docusaurus boilerplate for data governance, set up a
  docs-as-code pipeline for data mesh, publish data product documentation to surge.sh,
  sync docs to Google Drive or Confluence, automate documentation CI/CD with Jenkins,
  set up git-flow for documentation, create document history from git commits, or bootstrap
  any centralized documentation repo for data products. Also trigger when users mention
  "docs repo", "documentation pipeline", "Docusaurus data product", "surge.sh docs",
  "Google Docs sync", "Confluence sync", or "Jenkins docs pipeline" in any data mesh or
  data governance context.
compatibility: "Requires /data-mesh-architect skill. Tools: bash_tool, create_file, present_files."
---

# Data Mesh Docs Boilerplate Skill

Scaffold sebuah **Git repository lengkap** dalam format Docusaurus berisi boilerplate semua
**47 dokumen** dari `/data-mesh-architect`. Repository ini bisa:

- Di-build sebagai **static site** dan di-deploy ke **surge.sh**
- Di-sync ke **Google Drive** via script Python
- Di-sync ke **Confluence** via `mark` CLI
- Di-automate via **Jenkinsfile** dengan **git-flow strategy**
- Memiliki **Document History** yang diupdate otomatis dari commit messages saat release

---

## Quick Reference

| Kebutuhan | File |
|---|---|
| Setup Docusaurus + surge.sh | `references/docusaurus-setup.md` |
| Google Drive sync integration | `references/gdrive-integration.md` |
| Confluence sync integration | `references/confluence-integration.md` |
| Git Flow + Document History | `references/git-flow.md` |
| Init repo script (47 dokumen) | `scripts/init-repo.sh` |
| Google Drive sync script | `scripts/sync-gdrive.py` |
| Confluence sync script | `scripts/sync-confluence.py` |
| Jenkinsfile template | `assets/Jenkinsfile` |
| Environment variables sample | `assets/.env.example` |

---

## Alur Kerja

### LANGKAH 1 — Terima Context

User akan memberikan:
- **Nama project / domain** (contoh: `program-makan-bergizi`, `fintech-lending`)
- **Daftar data product** yang akan didokumentasikan
- **Target hosting**: surge.sh domain (default: `<project>.surge.sh`)
- **Integrasi aktif**: Google Drive? Confluence? Keduanya?
- **Confluence space key** dan **base URL** (jika Confluence aktif)
- **Google Drive folder ID** (jika Google Drive aktif)

Jika informasi tidak lengkap, tanyakan satu per satu — jangan hujani user.

---

### LANGKAH 2 — Generate Repo Structure

Baca `references/docusaurus-setup.md` untuk konfigurasi Docusaurus.

Jalankan `scripts/init-repo.sh` dengan parameter dari context user. Script ini menghasilkan
**semua 47 dokumen** sebagai placeholder yang siap diisi menggunakan `/data-mesh-architect`.

**Struktur repo yang dihasilkan:**

```
<project-name>-docs/
├── .github/
│   └── CODEOWNERS
├── .gitignore
├── .env.example
├── package.json
├── docusaurus.config.js
├── sidebars.js
├── Jenkinsfile
├── scripts/
│   ├── sync-gdrive.py
│   ├── sync-confluence.py
│   └── update-doc-history.sh
├── docs/
│   ├── intro.md
│   ├── {domain-name}/
│   │   └── {data-product-name}/
│   │       ├── README.md
│   │       ├── CHANGELOG.md               ← document history (release only)
│   │       ├── bootstrap/
│   │       │   ├── business-process-research.md  B-01
│   │       │   ├── proposal.md                   B-02
│   │       │   ├── canvas.md                     B-03
│   │       │   ├── data-profiling-prelim.md      B-04
│   │       │   └── eda-template.md               B-05
│   │       ├── design/
│   │       │   ├── design-document.md            D-01
│   │       │   ├── data-contract-spec.md         D-02
│   │       │   ├── data-contract.yaml            D-03
│   │       │   ├── data-catalog.md               D-04
│   │       │   ├── quality-design.md             D-05
│   │       │   ├── risk-assessment.md            D-06/07/08
│   │       │   ├── infra-brief.md                D-09
│   │       │   ├── dashboard-design.md           D-11
│   │       │   ├── scd-audit-design.md           D-12
│   │       │   └── metrics-catalog.md            D-13
│   │       ├── development/
│   │       │   ├── pipeline-brief.md             V-01
│   │       │   ├── api-brief.md                  V-02
│   │       │   ├── uat-integration-test.md       V-03/04
│   │       │   ├── data-pipeline.md              V-05 (as-built)
│   │       │   ├── data-api.md                   V-06 (as-built)
│   │       │   ├── dashboard-development.md      V-07
│   │       │   ├── data-science-model.md         V-08
│   │       │   ├── dataset-artifact.md           V-09
│   │       │   ├── migration-report.md           V-10
│   │       │   └── analytical-report.md          V-11
│   │       ├── delivery/
│   │       │   ├── consumer-onboarding-guide.md  DLV-01
│   │       │   └── self-service-infra-guide.md   DLV-02
│   │       ├── monitoring/
│   │       │   ├── operational-reports.md        M-02/03/04
│   │       │   ├── backup-dr-plan.md             M-05
│   │       │   ├── change-log.md                 M-06
│   │       │   └── operations-runbook.md         M-07
│   │       └── eosl/
│   │           └── eosl-report.md                E-01
│   ├── decisions/
│   │   └── ADR-0001-template.md                  ADR-01
│   ├── governance/
│   │   ├── data-vocabulary.md                    G-01
│   │   ├── data-access-control-matrix.md         G-02
│   │   ├── data-dictionary.md                    G-03
│   │   ├── data-retention-policy.md              G-04
│   │   └── federated-governance-checklist.md     G-05
│   └── project-management/
│       ├── ways-of-working.md                    PM-01
│       ├── rasci-matrix.md                       PM-02
│       ├── jira-structure.md                     PM-03
│       └── sprint-plan.md                        PM-04
└── static/
    └── img/logo.svg
```

---

### LANGKAH 3 — Populate Boilerplate Documents

Setiap dokumen di-scaffold dengan:

1. **Frontmatter** lengkap termasuk `doc_id` (X-Road convention)
2. **Riwayat Versi** table (kosong, siap diisi)
3. **Header Identifikasi** table dengan placeholder
4. **Placeholder content** kontekstual sesuai domain/product
5. `:::tip` admonition di setiap section yang perlu diisi tim

**Frontmatter standar yang di-generate script:**

```yaml
---
title: "[Doc Title] — [Product Name]"
sidebar_label: "[Doc ID] [Short Label]"
sidebar_position: [N]
description: "TODO: Deskripsi singkat dokumen ini."
tags: [phase, domain, doc-type]
doc_id: "[X-NN]"
data_product_id: "[domain]/[product]/v1"
data_product_owner: "TODO: Nama Domain Owner"
data_classification: "Internal"
phase: "[phase]"
version: "0.1.0"
last_updated: "[YYYY-MM-DD]"
pii_flag: false
---
```

---

### LANGKAH 4 — Konfigurasi Pipeline

Baca `assets/Jenkinsfile` untuk template pipeline lengkap.

```
Push ke feature/* atau develop
  → Lint Markdown (markdownlint-cli2)
  → Validate Frontmatter (cek doc_id, version, phase wajib ada)
  → Build Docusaurus (npm run build)

Push/merge ke develop
  → Deploy preview ke surge.sh/preview/{branch}

Merge ke main (release)
  → Update CHANGELOG.md dari commit messages
  → Tag versi (semver dari conventional commits)
  → Build + Deploy ke surge.sh/{project}
  → [Optional] Sync ke Confluence (CONFLUENCE_ENABLED=true)
  → [Optional] Sync ke Google Drive (GDRIVE_ENABLED=true)
  → Notify Slack/Teams
```

---

### LANGKAH 5 — Environment Variables

Generate `.env.example` dari `references/gdrive-integration.md` dan `references/confluence-integration.md`.

---

## Git Flow Strategy

Baca `references/git-flow.md` untuk panduan lengkap.

```
main           ← production docs, CHANGELOG diupdate saat release
  └── develop  ← staging docs (surge.sh preview)
        └── feature/[doc-id]-[desc]   ← penulisan dokumen
        └── fix/[doc-id]-[desc]       ← koreksi
release/vX.Y.Z ← dari develop, merge ke main + develop
hotfix/[desc]  ← urgent fix dari main
```

**Conventional Commits:**
```
feat(bootstrap): add B-02 data product proposal for domain-X
fix(design):     correct D-02 data contract schema for product-Y
docs(delivery):  update DLV-01 onboarding guide quick start section
chore(monitoring): update M-07 operations runbook runbook K8s commands
```

---

## Cara Menggunakan Skill Ini

```bash
# 1. Generate repo
bash scripts/init-repo.sh \
  --project "program-makan-bergizi" \
  --domain "pendidikan" \
  --products "master-data-sekolah,profil-peserta-didik" \
  --surge-domain "mbg-docs.surge.sh" \
  --enable-gdrive \
  --enable-confluence \
  --confluence-url "https://your-org.atlassian.net" \
  --confluence-space "DATAMESH"

# 2. Install dan jalankan lokal
cd program-makan-bergizi-docs
npm install && npm start   # localhost:3000

# 3. Deploy ke surge.sh
npm run build && npx surge build/ mbg-docs.surge.sh

# 4. Sync ke Google Drive
python scripts/sync-gdrive.py

# 5. Sync ke Confluence
python scripts/sync-confluence.py
```

---

## Output Files yang Dihasilkan

Output ke `/mnt/user-data/outputs/`:

1. `<project>-docs.zip` — Full repo structure (47 dokumen placeholder)
2. `Jenkinsfile` — Copy terpisah untuk referensi
3. `.env.example` — Template environment variables
4. `QUICKSTART.md` — Panduan setup 5 menit

---

## Catatan Penting

1. **Boilerplate ≠ content** — File yang dihasilkan adalah placeholder. Konten aktual diisi menggunakan `/data-mesh-architect` skill.
2. **doc_id wajib** — Script `init-repo.sh` menambahkan `doc_id` ke setiap frontmatter secara otomatis. Frontmatter validator di CI/CD akan menolak dokumen tanpa `doc_id`.
3. **Delivery phase** adalah fase baru — direktori `delivery/` otomatis dibuat per data product.
4. **Google Drive sync** mengkonversi Markdown ke Google Docs via Pandoc + Google Drive API. Formatting kompleks mungkin perlu adjustment manual.
5. **Surge.sh** adalah public hosting — pastikan tidak ada dokumen Restricted/Confidential yang di-deploy tanpa autentikasi tambahan.
6. **CHANGELOG.md** per data product hanya diupdate saat release, dihasilkan otomatis oleh Jenkins dari commit messages. Beda dari **M-06 Change Log** (changelog data product itu sendiri — perubahan schema, SLA, dsb.).
