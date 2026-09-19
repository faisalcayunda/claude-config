---
title: "Ways of Working — <Nama Data Product>"
sidebar_label: "Ways of Working"
sidebar_position: 1
description: "Panduan cara kerja tim data product: ceremonies, Definition of Done, branching strategy, dan team norms"
tags: [project-management, ways-of-working, agile, team]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
phase: bootstrap
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
---

# Ways of Working

> **Tujuan dokumen ini:** Mendefinisikan bagaimana tim data product ini bekerja sehari-hari — mulai dari ceremonies, komunikasi, Git workflow, hingga standar kualitas. Dokumen ini disetujui bersama di Sprint 0 dan diupdate saat ada perubahan signifikan.

---

## Tim & Kontak

| Role | Nama | Email | Slack | Availability |
|---|---|---|---|---|
| **Data Product Owner** | `<Nama>` | `<email>` | `<@handle>` | `<WIB timezone>` |
| **Data Architect** | `<Nama>` | `<email>` | `<@handle>` | |
| **Lead Data Engineer** | `<Nama>` | `<email>` | `<@handle>` | |
| **Data Steward/Analyst** | `<Nama>` | `<email>` | `<@handle>` | |
| **Project Manager** | `<Nama>` | `<email>` | `<@handle>` | |
| **SRE/DevOps** | `<Nama>` | `<email>` | `<@handle>` | |

**On-call rotation:** `<Link ke Grafana OnCall / escalation policy>`
**Slack channel utama:** `<#dp-[product-name]>`
**Jira board:** `<Link>`

---

## Ceremonies

| Ceremony | Kapan | Durasi | Fasilitator | Peserta |
|---|---|---|---|---|
| **Daily Standup** | `<Setiap hari Senin–Jumat, 09:15 WIB>` | `15 menit` | Rotating | Tim inti |
| **Sprint Planning** | `<Senin pertama setiap sprint, 09:00 WIB>` | `2-3 jam` | PM | Tim inti |
| **Sprint Review** | `<Jumat terakhir sprint, 14:00 WIB>` | `1 jam` | DPO | Tim + Stakeholder |
| **Sprint Retrospective** | `<Jumat terakhir sprint, 15:30 WIB>` | `1 jam` | PM | Tim inti |
| **Backlog Refinement** | `<Rabu, 14:00 WIB>` | `1 jam` | DPO + PM | Tim inti |
| **Data Contract Review** | `<Ad-hoc saat ada perubahan>` | `1 jam` | DA | DA + DE + DS + Consumer |
| **Monthly Data Review** | `<Jumat ke-4 setiap bulan, 14:00>` | `1 jam` | DPO | Tim + Stakeholder |

**Format Daily Standup:**
1. Apa yang dikerjakan kemarin?
2. Apa yang akan dikerjakan hari ini?
3. Ada blocker?
4. Apakah sprint on-track? (konfirmasi cepat dari PM)

---

## Definition of Done (DoD)

Story dianggap **Done** ketika semua kriteria ini terpenuhi:

### Technical DoD
```
[ ] Code sudah di-review oleh minimal 1 engineer lain
[ ] Semua automated tests lulus (unit + integration)
[ ] datacontract-cli test 0 failures (jika relevan)
[ ] Tidak ada critical security findings dari scan
[ ] Performance benchmark terpenuhi
[ ] Tidak ada TODO/FIXME yang belum di-address
```

### Documentation DoD
```
[ ] Dokumen terkait diupdate di Git (pipeline brief, API brief, dsb.)
[ ] Data Catalog entry diupdate
[ ] CHANGELOG.md diupdate
[ ] Jika ada perubahan schema: data contract diupdate
```

### Compliance DoD
```
[ ] Privacy checklist diverifikasi
[ ] Data classification tag diaplikasikan
[ ] Audit log berfungsi (untuk data sensitif)
[ ] Tidak ada PII exposed di luar kebijakan masking
```

### Stakeholder DoD
```
[ ] DPO review dan approve
[ ] Consumer yang terdampak sudah dikonfirmasi (untuk breaking changes)
[ ] Sprint Review demo sudah dilakukan
```

---

## Git Workflow

### Branching Strategy

```
main                     ← Production-ready, protected branch
├── develop              ← Integration branch
│   ├── feature/JIRA-ID-deskripsi   ← Development work
│   ├── fix/JIRA-ID-deskripsi       ← Bug fixes
│   ├── docs/JIRA-ID-deskripsi      ← Documentation only
│   └── refactor/JIRA-ID-deskripsi  ← Refactoring
└── release/v1.2.0       ← Release candidate (dari develop)
```

### Commit Message Convention (Conventional Commits)

```
<type>(<scope>): <deskripsi singkat>

Types:
  feat     → Fitur baru
  fix      → Bug fix
  docs     → Perubahan dokumentasi saja
  refactor → Refactoring (tidak ada perubahan fungsional)
  test     → Menambah atau update tests
  chore    → Maintenance (update dependencies, dsb.)
  ci       → Perubahan CI/CD

Contoh:
  feat(pipeline): add incremental load for dim_entitas
  fix(api): correct null handling for optional fields
  docs(catalog): update data dictionary for new columns
  test(quality): add uniqueness check for business key
```

### Pull Request Standard

Setiap PR wajib:
- Merujuk Jira ticket: `Refs: PROJ-123`
- Mengisi PR template (di `.github/pull_request_template.md`)
- Minimal 1 reviewer (2 untuk perubahan Data Contract)
- Semua CI checks lulus sebelum merge
- Squash merge ke `develop` (bersihkan commit history)

---

## Definition of Ready (DoR)

Story siap masuk ke Sprint ketika:
```
[ ] Story punya Acceptance Criteria yang jelas dan testable
[ ] Story ter-estimasi (story points)
[ ] Dependencies sudah diidentifikasi
[ ] Mockup/wireframe tersedia (jika UI/dashboard)
[ ] Data source sudah diverifikasi accessible
[ ] Tidak ada blocker yang diketahui
```

---

## Escalation Path

| Situasi | Eskalasi ke | Cara |
|---|---|---|
| Blocker teknis > 2 jam | Lead DE → DA | Slack DM langsung |
| Blocker bisnis/requirement | PM → DPO | Slack + Jira comment |
| Data quality incident P1-P2 | On-call → DPO | Grafana OnCall + Slack |
| Security concern | DA → Security Team | Email + Jira ticket |
| Consumer complaint | DS → DPO | Slack #dp-[product] |

---

## Prinsip Kerja Tim

1. **Documentation as Code** — Semua dokumentasi di Git, diperbarui bersama kode
2. **Privacy by Default** — PII selalu di-mask, tidak ada opt-in masking
3. **Test First** — Tulis quality rules sebelum membangun pipeline
4. **No Hardcoded Secrets** — Semua credentials dari Vault
5. **Consumer-First** — Keputusan arsitektur mempertimbangkan dampak ke consumer
6. **Fail Fast, Fix Faster** — Alert segera, rollback cepat, post-mortem dalam 48 jam
7. **Blameless Culture** — Insiden bukan kesalahan individu, tapi peluang perbaikan sistem
