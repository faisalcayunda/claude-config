---
title: "JIRA Structure — <Nama Data Product>"
sidebar_label: "JIRA Structure"
sidebar_position: 2
description: "Template struktur JIRA dengan hierarki Epic > Task > Subtask. Epic adalah data product itu sendiri, Task adalah setiap dokumen output, Subtask adalah langkah kerja di dalamnya."
tags: [project-management, jira, backlog, sprint-planning]
data_product_id: "<domain>/<data-product-name>/v<version>"
phase: bootstrap
last_updated: "<YYYY-MM-DD>"
---

# JIRA Structure

> **Tujuan dokumen ini:** Template siap-pakai untuk setup JIRA data product. Hierarki yang digunakan: **Epic = Data Product**, **Task = Dokumen Output / Deliverable**, **Subtask = Langkah kerja di dalam deliverable tersebut**.

---

## Konfigurasi Project

```
Project Key:     <DP-DOMAIN-PRODUCT>     contoh: DP-LOGISTICS-SHIPMENT
Project Type:    Scrum
Sprint Duration: 2 minggu
Story Points:    Fibonacci (1, 2, 3, 5, 8, 13)
Issue Hierarchy: Epic > Task > Subtask
```

---

## Konvensi Penamaan

| Level | Format | Contoh |
|---|---|---|
| **Epic** | `[DOMAIN] Nama Data Product` | `[LOGISTICS] Shipment Tracking Data Product` |
| **Task** | `[FASE-ID] Nama Dokumen — Nama Data Product` | `[B-02] Data Product Proposal — Shipment Tracking` |
| **Subtask** | `Aksi spesifik` | `Draft business case dan estimasi biaya` |

**Label standar yang digunakan:**

| Label | Digunakan pada |
|---|---|
| `bootstrap` `design` `development` `monitoring` `eosl` | Semua Task sesuai fase |
| `pii` | Task yang menyentuh data pribadi |
| `breaking-change` | Task yang mengubah Data Contract secara breaking |
| `governance` | Task terkait vocabulary, access control, DPIA |
| `recurring` | Task yang diulang setiap bulan (quality report, cost report) |
| `sign-off-required` | Task yang butuh persetujuan formal sebelum dianggap selesai |

---

## Epic

Satu Epic mewakili satu Data Product secara keseluruhan, dari Bootstrap sampai EoSL.

```
Epic: [<DOMAIN>] <Nama Data Product>
  Description: <Deskripsi singkat data product>
  Labels:      <nama-domain>
  Owner:       <Data Product Owner>
  Fix Version: v1.0.0
```

---

## Fase 1 — Bootstrap

### Task B-01: Business Process Research & Context

```
Task:    [B-01] Business Process Research — <Nama Data Product>
Labels:  bootstrap
Points:  8 SP
Owner:   Data Architect + Business Analyst
Dokumen: templates/bootstrap/business-process-research.md

  Subtask: Siapkan interview guide dan daftar pertanyaan
           Owner: DA | 1 SP
  Subtask: Jadwalkan dan lakukan stakeholder interview
           Owner: PM + BA | 2 SP
  Subtask: Dokumentasikan domain events dan entitas bisnis
           Owner: DA | 2 SP
  Subtask: Buat diagram alur proses bisnis (BPMN/swimlane)
           Owner: DA | 1 SP
  Subtask: Validasi temuan dengan domain expert
           Owner: DPO | 1 SP
  Subtask: Identifikasi dan dokumentasikan atribut PII
           Labels: pii | Owner: DA + Legal | 1 SP
```

### Task B-02: Data Product Proposal

```
Task:    [B-02] Data Product Proposal — <Nama Data Product>
Labels:  bootstrap, sign-off-required
Points:  8 SP
Owner:   Data Product Owner + Project Manager
Dokumen: templates/bootstrap/proposal.md

  Subtask: Tulis problem statement dan strategic alignment
           Owner: DPO | 2 SP
  Subtask: Definisikan consumer persona dan output ports
           Owner: DA + DPO | 1 SP
  Subtask: Buat estimasi biaya build dan run
           Owner: PM | 2 SP
  Subtask: Privacy quick check (ada PII / perlu DPIA?)
           Labels: pii | Owner: Legal | 1 SP
  Subtask: Stakeholder review dan iterasi
           Owner: PM | 1 SP
  Subtask: DPO sign-off formal
           Labels: sign-off-required | Owner: DPO | 1 SP
```

### Task B-03: Data Product Canvas

```
Task:    [B-03] Data Product Canvas — <Nama Data Product>
Labels:  bootstrap, sign-off-required
Points:  5 SP
Owner:   Data Architect + Data Product Owner
Dokumen: templates/bootstrap/canvas.md

  Subtask: Isi bagian Consumer dan Use Cases
           Owner: DPO + DA | 1 SP
  Subtask: Isi bagian Source Systems dan Architecture
           Owner: DA + DE | 1 SP
  Subtask: Isi ringkasan Data Contract (schema, SLO, security)
           Owner: DA | 1 SP
  Subtask: Isi Ubiquitous Language dan Classification
           Owner: DPO + DS | 1 SP
  Subtask: Canvas review bersama tim dan DPO sign-off
           Labels: sign-off-required | Owner: DPO | 1 SP
```

### Task B-04: Preliminary Data Profiling

```
Task:    [B-04] Preliminary Data Profiling — <Nama Data Product>
Labels:  bootstrap
Points:  8 SP
Owner:   Data Engineer + Data Analyst
Dokumen: templates/bootstrap/data-profiling-prelim.md

  Subtask: Setup akses dev environment ke semua sumber data
           Owner: DE + SRE | 2 SP
  Subtask: Jalankan profiling pada sumber data A
           Owner: DE | 2 SP
  Subtask: Jalankan profiling pada sumber data B (jika ada)
           Owner: DE | 1 SP
  Subtask: Identifikasi kolom PII dari hasil profiling
           Labels: pii | Owner: DA | 1 SP
  Subtask: Tulis laporan temuan dan rekomendasi Go/No-Go
           Owner: DA | 2 SP
```

---

## Fase 2 — Design

### Task D-01: Data Product Design Document

```
Task:    [D-01] Data Product Design Document — <Nama Data Product>
Labels:  design, sign-off-required
Points:  13 SP
Owner:   Data Architect + Data Engineer
Dokumen: templates/design/design-document.md

  Subtask: Tulis ADR-001 — strategi penyimpanan data (storage)
           Owner: DA | 2 SP
  Subtask: Tulis ADR-002 — strategi ingestion (CDC / batch / streaming)
           Owner: DA | 2 SP
  Subtask: Tulis ADR-003 — penanganan PII dan keamanan
           Labels: pii | Owner: DA + Legal | 2 SP
  Subtask: Definisikan logika pemrosesan: Ingestion → Cleansing → Transformation → Projection
           Owner: DA + DE | 3 SP
  Subtask: Buat diagram arsitektur C4 (container level)
           Owner: DA | 2 SP
  Subtask: DA review dan sign-off
           Labels: sign-off-required | Owner: DA | 1 SP
  Subtask: Verifikasi Definition of Ready sebelum masuk Development
           Owner: PM | 1 SP
```

### Task D-02 & D-03: Data Contract

```
Task:    [D-02] Data Contract & Interface Specification — <Nama Data Product>
Labels:  design, sign-off-required, breaking-change
Points:  13 SP
Owner:   Data Architect + Data Product Owner
Dokumen: templates/design/data-contract-spec.md
         templates/design/data-contract.yaml

  Subtask: Definisikan schema semua output port (kolom, tipe, constraint)
           Owner: DA + DE | 3 SP
  Subtask: Tentukan SLI dan SLO (freshness, availability, completeness, uniqueness)
           Owner: DA + DPO | 2 SP
  Subtask: Tulis SLA dan error budget policy
           Owner: DPO + PM | 2 SP
  Subtask: Tulis data-contract.yaml (datacontract-specification v1.2.1)
           Owner: DA | 2 SP
  Subtask: Validasi YAML dengan datacontract-cli lint
           Owner: DE | 1 SP
  Subtask: Consumer review dan negosiasi SLO
           Owner: DPO + Consumer | 2 SP
  Subtask: Sign-off DPO dan consumer representative
           Labels: sign-off-required | Owner: DPO | 1 SP
```

### Task D-04: Data Catalog & Metadata

```
Task:    [D-04] Data Catalog & Metadata — <Nama Data Product>
Labels:  design
Points:  13 SP
Owner:   Data Steward + Data Engineer
Dokumen: templates/design/data-catalog.md

  Subtask: Isi Table Index (nama tabel, layer, owner, frekuensi update)
           Owner: DS | 2 SP
  Subtask: Tulis Data Dictionary per tabel (definisi bisnis setiap kolom)
           Owner: DS + Domain Expert | 5 SP
  Subtask: Buat Source-to-Target Mapping lengkap dengan transformation logic
           Owner: DE | 3 SP
  Subtask: Buat lineage diagram (Mermaid)
           Owner: DA | 1 SP
  Subtask: Buat entri di OpenMetadata / DataHub
           Owner: DS | 2 SP
```

### Task D-05: Data Quality Design

```
Task:    [D-05] Data Quality Design — <Nama Data Product>
Labels:  design
Points:  8 SP
Owner:   Data Steward + Data Engineer
Dokumen: templates/design/quality-design.md

  Subtask: Definisikan DQ rules per dimensi (completeness, uniqueness, validity, consistency, freshness)
           Owner: DS | 3 SP
  Subtask: Tentukan threshold SLO dan severity per rule
           Owner: DS + DPO | 2 SP
  Subtask: Tulis implementasi test suite (dbt tests atau SodaCL)
           Owner: DE | 2 SP
  Subtask: Konfigurasi alerting ke Slack/Grafana
           Owner: DE + SRE | 1 SP
```

### Task D-12: SCD & Audit Logging Design

```
Task:    [D-12] SCD & Audit Logging Design — <Nama Data Product>
Labels:  design, pii
Points:  8 SP
Owner:   Data Architect + Data Engineer
Dokumen: templates/design/scd-audit-design.md

  Subtask: Tentukan SCD type untuk setiap tabel (0, 1, 2, 3, 4, atau 6)
           Owner: DA | 2 SP
  Subtask: Buat DDL PostgreSQL SCD Type 2 dengan kolom valid_from, valid_to, is_current, version
           Owner: DE | 2 SP
  Subtask: Implement generic audit trigger function
           Labels: pii | Owner: DE | 2 SP
  Subtask: Setup pg_partman untuk audit_log partisi bulanan + retention policy
           Owner: DE + DBA | 1 SP
  Subtask: Tulis query patterns point-in-time dan forensics
           Owner: DA | 1 SP
```

### Task D-06+07+08: Risk Assessment & Privacy

```
Task:    [D-06] Risk Assessment & Privacy — <Nama Data Product>
Labels:  design, pii, sign-off-required, governance
Points:  13 SP
Owner:   Data Architect + Legal/Compliance
Dokumen: templates/design/risk-assessment.md

  Subtask: Jalankan DPIA screening (apakah DPIA penuh wajib?)
           Labels: pii | Owner: Legal + DA | 2 SP
  Subtask: Isi DPIA penuh jika screening positif
           Labels: pii | Owner: Legal | 5 SP
  Subtask: Isi RoPA (Record of Processing Activities)
           Labels: pii | Owner: Legal + DS | 3 SP
  Subtask: Isi risk register teknis + organisasi dengan mitigasi
           Owner: DA + PM | 2 SP
  Subtask: Legal sign-off DPO / Compliance Officer
           Labels: sign-off-required | Owner: Legal | 1 SP
```

### Task D-09: Infrastructure Brief

```
Task:    [D-09] Infrastructure Brief — <Nama Data Product>
Labels:  design, sign-off-required
Points:  13 SP
Owner:   Data Architect + SRE
Dokumen: templates/design/infra-brief.md

  Subtask: Estimasi volume data dan proyeksi pertumbuhan 12 bulan
           Owner: DE + DA | 2 SP
  Subtask: Desain topologi deployment dan network isolation
           Owner: DA + SRE | 3 SP
  Subtask: Tulis konfigurasi PostgreSQL (postgresql.conf, autovacuum, extensions)
           Owner: DE + DBA | 2 SP
  Subtask: Buat provisioning script PostgreSQL lengkap (schema, roles, RLS, views)
           Owner: DE | 3 SP
  Subtask: Konfigurasi pgBackRest + backup policy
           Owner: SRE | 2 SP
  Subtask: Security review (enkripsi, secrets di OpenBao, network policy)
           Owner: SRE + Security | 1 SP
```

### Task D-10: Preliminary EDA

```
Task:    [D-10] Preliminary EDA — <Nama Data Product>
Labels:  design
Points:  8 SP
Owner:   Data Analyst + Data Engineer
Dokumen: templates/design/eda-template.md

  Subtask: Setup Jupyter notebook + koneksi ke dev database
           Owner: DE | 1 SP
  Subtask: Analisis completeness dan distribusi kolom kunci
           Owner: DA | 2 SP
  Subtask: Analisis uniqueness, duplikasi, dan anomali
           Owner: DA | 2 SP
  Subtask: Identifikasi kolom PII dari hasil EDA
           Labels: pii | Owner: DA | 1 SP
  Subtask: Dokumentasikan temuan dan input untuk quality-design.md
           Owner: DA | 2 SP
```

### Task D-11: Dashboard Design (jika ada)

```
Task:    [D-11] Dashboard Design — <Nama Data Product>
Labels:  design
Points:  8 SP
Owner:   Data Analyst + Data Product Owner
Dokumen: templates/design/dashboard-design.md

  Subtask: Definisikan KPI cards dan metrik utama
           Owner: DPO + DA | 2 SP
  Subtask: Buat wireframe halaman per audience (Apache Superset)
           Owner: DA | 2 SP
  Subtask: Tulis SQL / query referensi per chart
           Owner: DA | 2 SP
  Subtask: Consumer review wireframe
           Owner: Consumer | 1 SP
  Subtask: DPO sign-off
           Labels: sign-off-required | Owner: DPO | 1 SP
```

### Task G-01: Data Vocabulary Reference (Governance)

```
Task:    [G-01] Data Vocabulary Reference — <Nama Data Product>
Labels:  design, governance
Points:  8 SP
Owner:   Data Steward + Data Architect
Dokumen: templates/governance/data-vocabulary-template.md

  Subtask: Inventori semua atribut bertipe enum dalam data product ini
           Owner: DS | 1 SP
  Subtask: Research regulasi yang mengatur setiap enum (Permendagri, UU PDP, BPS, dsb.)
           Owner: DS + Legal | 3 SP
  Subtask: Tulis entri vocabulary dengan kode kanonik, definisi bisnis, dan referensi regulasi
           Owner: DS | 2 SP
  Subtask: Buat tabel konversi dari kode sistem sumber ke kode kanonik
           Owner: DE | 1 SP
  Subtask: DS review dan approve
           Labels: sign-off-required | Owner: DS + DA | 1 SP
```

### Task G-02: Data Access Control Matrix (Governance)

```
Task:    [G-02] Data Access Control Matrix — <Nama Data Product>
Labels:  design, pii, governance, sign-off-required
Points:  8 SP
Owner:   Data Architect + DPO + CISO
Dokumen: templates/governance/data-access-control-matrix.md

  Subtask: Definisikan inventori role (bisnis dan PostgreSQL)
           Owner: DA + DPO | 1 SP
  Subtask: Isi matriks akses per layer (Bronze, Silver, Gold, API, Dashboard)
           Owner: DA | 2 SP
  Subtask: Definisikan masking rules per kolom PII
           Labels: pii | Owner: DA + Legal | 2 SP
  Subtask: Buat provisioning SQL: roles, RLS policies, masked views
           Owner: DE | 2 SP
  Subtask: DPO + CISO sign-off
           Labels: sign-off-required | Owner: DPO + CISO | 1 SP
```

---

## Fase 3 — Development

### Task V-01: Data Pipeline Brief

```
Task:    [V-01] Data Pipeline Brief — <Nama Data Product>
Labels:  development
Points:  21 SP
Owner:   Data Engineer (Lead)
Dokumen: templates/development/pipeline-brief.md

  Subtask: Setup CI/CD pipeline dan dev environment
           Owner: SRE + DE | 3 SP
  Subtask: Implementasi Bronze layer (ingestion dari semua sumber)
           Owner: DE | 5 SP
  Subtask: Implementasi Silver layer (cleansing + DQ rules)
           Owner: DE | 5 SP
  Subtask: Implementasi Gold layer (business logic + output ports)
           Owner: DE + DA | 5 SP
  Subtask: Pasang monitoring + alerting DQ ke Grafana
           Owner: DE + SRE | 2 SP
  Subtask: Finalisasi Pipeline Brief document (Metadata Workload / DPDS YAML)
           Owner: DE | 1 SP
```

### Task V-02: Data API Brief (jika ada API output port)

```
Task:    [V-02] Data API Brief — <Nama Data Product>
Labels:  development
Points:  13 SP
Owner:   Data Engineer
Dokumen: templates/development/api-brief.md

  Subtask: Implementasi REST endpoints (FastAPI)
           Owner: DE | 5 SP
  Subtask: Konfigurasi Auth via Keycloak (OAuth 2.0) + Kong rate limiting
           Owner: SRE + DE | 3 SP
  Subtask: Implementasi PII masking di response layer
           Labels: pii | Owner: DE | 2 SP
  Subtask: Tulis API tests (unit + integration)
           Owner: DE | 2 SP
  Subtask: Finalisasi API Brief document (Port YAML)
           Owner: DE | 1 SP
```

### Task V-03+04: UAT & Integration Test

```
Task:    [V-03] UAT & Integration Test — <Nama Data Product>
Labels:  development, sign-off-required
Points:  13 SP
Owner:   Project Manager + Data Analyst + Consumer
Dokumen: templates/development/uat-integration-test.md

  Subtask: Tulis test cases UAT per use case
           Owner: PM + DA | 3 SP
  Subtask: Siapkan staging environment dan test data
           Owner: DE + SRE | 2 SP
  Subtask: Jalankan integration tests (datacontract-cli test, dbt test)
           Owner: DE | 2 SP
  Subtask: Eksekusi UAT bersama consumer representative
           Owner: Consumer + PM | 3 SP
  Subtask: Fix defects dari hasil UAT
           Owner: DE | variable SP
  Subtask: Go/No-Go checklist dan sign-off
           Labels: sign-off-required | Owner: DPO + PM + SRE | 1 SP
  Subtask: Deployment ke production
           Owner: SRE + DE | 2 SP
```

---

## Fase 4 — Delivery

### Task V-05: Go-Live & Hypercare

```
Task:    [V-05] Go-Live & Hypercare (2 minggu) — <Nama Data Product>
Labels:  development
Points:  8 SP
Owner:   Project Manager + SRE + Data Steward

  Subtask: Consumer onboarding (credentials, dokumentasi, walkthrough)
           Owner: PM + DS | 3 SP
  Subtask: Monitor pipeline 2 minggu pertama (SLO adherence)
           Owner: DS + SRE | 3 SP
  Subtask: Finalisasi semua dokumentasi ke Git
           Owner: DA + PM | 2 SP
```

---

## Fase 5 — Monitoring/Evaluation

### Task M-01: Metrics & Insights Catalog

```
Task:    [M-01] Data Product Metrics Catalog — <Nama Data Product>
Labels:  monitoring
Points:  5 SP
Owner:   Data Steward + Data Product Owner
Dokumen: templates/monitoring/metrics-catalog.md

  Subtask: Definisikan KPI bisnis dan North Star Metric
           Owner: DPO | 2 SP
  Subtask: Tulis query referensi untuk setiap pertanyaan bisnis utama
           Owner: DA | 2 SP
  Subtask: Link ke dashboard dan monitoring SLO
           Owner: DS | 1 SP
```

### Task M-02: Monthly Quality Report (Recurring)

```
Task:    [M-02] Quality Report — <Bulan YYYY> — <Nama Data Product>
Labels:  monitoring, recurring
Points:  5 SP
Owner:   Data Steward
Dokumen: templates/monitoring/operational-reports.md (Quality Report section)

  Subtask: Jalankan quality checks dan kumpulkan data SLO bulan ini
           Owner: DS | 1 SP
  Subtask: Analisis SLO breaches dan trend
           Owner: DS | 2 SP
  Subtask: Tulis laporan dan rekomendasi perbaikan
           Owner: DS | 1 SP
  Subtask: Presentasikan ke DPO dan stakeholders
           Owner: DPO | 1 SP
```

### Task M-03: Monthly Cost Report (Recurring)

```
Task:    [M-03] Cost Report — <Bulan YYYY> — <Nama Data Product>
Labels:  monitoring, recurring
Points:  3 SP
Owner:   Project Manager + SRE
Dokumen: templates/monitoring/operational-reports.md (Cost Report section)

  Subtask: Extract metrics biaya dari Grafana / billing dashboard
           Owner: SRE | 1 SP
  Subtask: Analisis variance vs budget dan peluang optimasi
           Owner: PM + SRE | 1 SP
  Subtask: Finalisasi laporan
           Owner: PM | 1 SP
```

### Task M-04: Incident Report (Per Insiden)

```
Task:    [M-04] Incident Report — <INC-ID> — <Nama Data Product>
Labels:  monitoring
Points:  variable SP
Owner:   Incident Commander (on-call)
Dokumen: templates/monitoring/operational-reports.md (Incident Report section)

  Subtask: Dokumentasikan timeline insiden secara real-time
           Owner: On-call DE | 1 SP
  Subtask: Identifikasi root cause (5 Whys)
           Owner: DA + DE | 2 SP
  Subtask: Tulis corrective actions dan assign owner
           Owner: PM | 1 SP
  Subtask: Post-mortem review dengan seluruh tim
           Owner: PM | 1 SP
```

---

## Fase 6 — End of Service Life

### Task E-01: EoSL Report

```
Task:    [E-01] End of Service Life Report — <Nama Data Product>
Labels:  eosl, pii, sign-off-required
Points:  13 SP
Owner:   Data Product Owner + Project Manager
Dokumen: templates/eosl/eosl-report.md

  Subtask: Notifikasi semua consumer (minimum 6 bulan sebelum EoSL)
           Owner: PM + DPO | 1 SP
  Subtask: Monitor dan bantu consumer migration ke data product pengganti
           Owner: DS + PM | 3 SP
  Subtask: Arsip data ke cold storage (Bronze, Silver, Gold)
           Owner: SRE + DE | 2 SP
  Subtask: Hapus PII sesuai kebijakan retensi (UU PDP right to erasure)
           Labels: pii | Owner: DBA + Legal | 2 SP
  Subtask: Decommission infrastruktur (DB, MinIO, Airflow DAG, API)
           Owner: SRE | 2 SP
  Subtask: Sign-off final (DPO + Legal + SRE)
           Labels: sign-off-required | Owner: DPO + Legal | 1 SP
  Subtask: Dokumentasikan lessons learned
           Owner: PM + DA | 2 SP
```

---

## Sprint Allocation Guide

Estimasi alokasi sprint per fase untuk data product dengan kompleksitas sedang:

| Sprint | Fase | Task yang Direkomendasikan |
|---|---|---|
| Sprint 0 | Bootstrap | B-01, B-02, B-03, B-04 |
| Sprint 1 | Design | D-01, D-02+03, G-01 |
| Sprint 2 | Design | D-04, D-05, D-12, D-09 |
| Sprint 3 | Design | D-06+07+08, D-10, G-02 |
| Sprint 4 | Design + Dev Start | D-11 (jika ada), V-01 (Bronze) |
| Sprint 5 | Development | V-01 (Silver + Gold) |
| Sprint 6 | Development | V-01 (selesai), V-02 (jika ada) |
| Sprint 7 | Development + Delivery | V-03+04 (UAT), V-05 (Go-live) |
| Sprint 8+ | Monitoring | M-01, M-02, M-03 (recurring) |

---

## Template Deskripsi Task

Gunakan format berikut saat membuat Task di JIRA:

```
Summary:     [<FASE-ID>] <Nama Dokumen> — <Nama Data Product>
Description:
  Dokumen output: <path ke template file>
  
  Tujuan: <satu kalimat tujuan dokumen ini>
  
  Acceptance Criteria:
  - [ ] Semua section Mandatory terisi
  - [ ] Review oleh <role> selesai
  - [ ] Sign-off dari <role> diterima (jika required)
  - [ ] File di-commit ke Git: <domain>/<product>/<fase>/<nama-file>.md
  - [ ] Data Catalog diupdate jika ada perubahan schema

Labels:      <fase>, <label tambahan>
Story Points: <SP>
Assignee:    <Nama>
Epic Link:   [<DOMAIN>] <Nama Data Product>
Sprint:      Sprint <N>
```
