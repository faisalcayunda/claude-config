---
title: "Federated Governance Checklist — <Nama Domain / Nama Data Product>"
sidebar_label: "Federated Governance Checklist"
sidebar_position: 5
description: "Instrumen verifikasi konformitas governance terfederasi: dari registrasi domain, lifecycle gate per fase, ongoing cadence, interoperabilitas lintas domain, kepatuhan privasi, hingga kesiapan retirement."
tags: [governance, federated-governance, compliance, lifecycle-gate, checklist]
doc_id: "G-05"
scope: "<domain-level | data-product-level>"
domain: "<Nama Domain>"
data_product_id: "<domain>/<data-product-name>/v<version> | N/A jika domain-level>"
data_product_owner: "<Nama Domain Owner>"
dgo_reviewer: "<Nama Data Governance Officer>"
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
next_review_date: "<YYYY-MM-DD>"
review_cycle: "<Kuartalan>"
---

# Federated Governance Checklist

> **Tujuan dokumen ini:** Instrumen verifikasi formal bahwa domain dan data product telah memenuhi standar governance terfederasi — mencakup konformitas lifecycle, interoperabilitas lintas domain, kepatuhan privasi, dan kesiapan operasional. Dokumen ini bersifat **auditable** dan menjadi bukti kepatuhan dalam review governance.

:::tip Cara Membaca Dokumen Ini
Dokumen ini terdiri dari **enam bagian checklist** yang dijalankan pada konteks dan waktu berbeda. Gunakan [Bagian 2 — Cara Menggunakan Checklist](#2-cara-menggunakan-checklist) untuk menentukan bagian mana yang relevan sebelum mengisi.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis | Reviewer |
|---|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` | `<Nama DGO>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `G-05` |
| **Scope** | `<Domain-level: seluruh domain>` / `<Data-product-level: satu data product>` |
| **Domain** | `<Nama Domain>` |
| **Data Product** (jika berlaku) | `<Nama Data Product v.X.Y>` |
| **Domain Owner** | `<Nama, Email>` |
| **Data Steward** | `<Nama, Email>` |
| **DGO / Governance Reviewer** | `<Nama, Email>` |
| **Dokumen terkait** | [PM-02 RASCI Matrix](../project-management/rasci-matrix.md) · [PM-01 Ways of Working](../project-management/ways-of-working.md) · [G-02 Access Control Matrix](./data-access-control-matrix.md) |

---

## 1. Pendahuluan

### 1.1 Target Audience

| Persona | Konteks Penggunaan |
|---|---|
| **Domain Owner / Data Product Owner** | Mengisi checklist sebelum setiap lifecycle gate; bertanggung jawab atas kelengkapan |
| **Data Steward** | Mengisi bagian ongoing governance (Bagian C) secara berkala |
| **Data Governance Officer (DGO)** | Reviewer akhir; memvalidasi konformitas dan memberikan sign-off |
| **Internal Auditor** | Menggunakan checklist ini sebagai bukti kepatuhan saat audit |

### 1.2 Prinsip Governance Terfederasi

Checklist ini mengimplementasikan empat prinsip governance terfederasi Data Mesh:

| Prinsip | Implementasi dalam Checklist |
|---|---|
| **Otonomi domain** | Domain bebas memilih tools dan cara kerja selama memenuhi standar global |
| **Standar global yang tidak bisa dikompromikan** | Item yang diberi `[GLOBAL]` adalah wajib tanpa pengecualian |
| **Interoperabilitas by design** | Bagian D memverifikasi bahwa data product bisa dikonsumsi lintas domain |
| **Kepatuhan komputasional** | Bukti berupa artefak tertulis dan link dokumen, bukan pernyataan lisan |

### 1.3 Scope Dokumen Ini

Checklist ini beroperasi di **dua level**:

```
Level 1 — Domain Level (Bagian A)
  Dijalankan SEKALI saat domain pertama kali diregistrasikan ke Data Mesh
  PIC: Domain Owner + DGO

Level 2 — Data Product Level (Bagian B, C, D, E, F)
  Dijalankan PER DATA PRODUCT, mulai fase Bootstrap hingga Retirement
  PIC: Data Product Owner + Data Steward
```

---

## 2. Cara Menggunakan Checklist

### 2.1 Panduan Pemilihan Bagian

| Situasi | Bagian yang Dijalankan |
|---|---|
| Domain baru bergabung ke Data Mesh | **Bagian A** |
| Data product melewati lifecycle gate | **Bagian B** (pilih sub-bagian sesuai gate) |
| Review bulanan atau kuartalan | **Bagian C** |
| Data product akan dikonsumsi lintas domain | **Bagian D** |
| Ada perubahan pemrosesan data PII | **Bagian E** |
| Data product akan diretire | **Bagian F** |

### 2.2 Skoring dan Status

Setiap item checklist diberi status dari empat pilihan:

| Status | Kode | Definisi |
|---|---|---|
| Lulus | `✅ PASS` | Item terpenuhi, bukti tersedia |
| Gagal | `❌ FAIL` | Item tidak terpenuhi; **harus diselesaikan sebelum gate** |
| Tidak Berlaku | `➖ N/A` | Item tidak relevan untuk konteks ini; DGO harus setuju |
| Parsial | `⚠️ PARTIAL` | Sebagian terpenuhi; action item terdefinisi dengan deadline |

:::warning Status PARTIAL
Item dengan status `⚠️ PARTIAL` **tidak memblokir gate** jika dan hanya jika:
1. Action item remediasi sudah terdefinisi jelas
2. Deadline remediasi tidak lebih dari `<14 hari kalender>` setelah gate
3. DGO memberikan persetujuan eksplisit secara tertulis

Item dengan status `❌ FAIL` **selalu memblokir gate** tanpa pengecualian.
:::

### 2.3 Cara Mengisi

Untuk setiap item checklist:

1. **Tentukan status** menggunakan kode di atas
2. **Isi kolom Bukti/Evidence** — berupa link dokumen, screenshot, atau referensi tiket
3. **Isi Catatan** jika ada konteks tambahan atau justifikasi N/A
4. **Hitung Compliance Score** menggunakan rumus di [Annex A](#annex-a--scoring-guide--compliance-score)

### 2.4 Cadence dan Ownership

| Bagian | Frekuensi | Owner Pengisi | Reviewer/Approver |
|---|---|---|---|
| A — Domain Registration | Sekali (saat onboarding) | Domain Owner | DGO |
| B — Lifecycle Gates | Per gate per data product | Data Product Owner | DGO + Domain Owner |
| C1 — Monthly Governance | Bulanan | Data Steward | Data Product Owner |
| C2 — Quarterly Governance | Kuartalan | Data Product Owner | DGO |
| C3 — Annual Audit | Tahunan | DGO | Executive / CISO |
| D — Cross-Domain Interop | Saat ada consumer baru lintas domain | Data Product Owner | Domain Owner tujuan |
| E — Privacy & Compliance | Saat ada perubahan pemrosesan | Data Steward + Legal | DPO Organisasi |
| F — Retirement Readiness | Saat keputusan retirement | Data Product Owner | DGO + Domain Owner |

---

## Bagian A — Domain Registration Checklist

> **Kapan dijalankan:** Satu kali, saat domain pertama kali diregistrasikan ke Data Mesh.
> **Diblokir oleh:** Tidak ada gate sebelumnya.
> **Output:** Domain dinyatakan aktif di Data Mesh registry.

### Hasil Review

| | |
|---|---|
| **Tanggal Review** | `<YYYY-MM-DD>` |
| **Reviewer** | `<Nama DGO>` |
| **Status Keseluruhan** | `<PASS / FAIL / CONDITIONAL>` |
| **Tanggal Efektif Domain** | `<YYYY-MM-DD>` |

---

### A.1 — Identitas dan Batas Domain

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| A-01 | Bounded context domain telah didefinisikan secara eksplisit (bukan berdasarkan struktur organisasi IT) | `[GLOBAL]` | `[ ]` | `<Link ke domain charter>` | |
| A-02 | Nama domain mengikuti konvensi penamaan global (lowercase, kebab-case, tanpa singkatan ambigu) | `[GLOBAL]` | `[ ]` | `<Nama: domain-name>` | |
| A-03 | Hubungan dengan domain lain telah dipetakan (upstream/downstream) | `[GLOBAL]` | `[ ]` | `<Link ke domain relationship diagram>` | |
| A-04 | Tidak ada overlap bounded context dengan domain yang sudah ada | `[GLOBAL]` | `[ ]` | `<Konfirmasi DGO + domain owners terdampak>` | |

### A.2 — Kepemilikan dan Struktur Tim

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| A-05 | Domain Owner ditetapkan dengan nama dan kontak yang terdaftar | `[GLOBAL]` | `[ ]` | `<Nama: ___, Email: ___>` | |
| A-06 | Data Steward ditetapkan untuk domain (minimal 1 orang) | `[GLOBAL]` | `[ ]` | `<Nama: ___, Email: ___>` | |
| A-07 | Escalation path ke Data Governance Council terdefinisi | `[GLOBAL]` | `[ ]` | `<Link ke Ways of Working §Eskalasi>` | |
| A-08 | RASCI matrix untuk domain telah dibuat | `[GLOBAL]` | `[ ]` | `<Link ke PM-02 RASCI>` | |

### A.3 — Standar dan Artefak Awal

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| A-09 | Ways of Working document domain telah dibuat dan disetujui tim | `[GLOBAL]` | `[ ]` | `<Link ke PM-01>` | |
| A-10 | Kamus Data domain versi awal telah dibuat (minimal entitas utama) | `[GLOBAL]` | `[ ]` | `<Link ke G-01>` | |
| A-11 | Domain telah terdaftar di Data Catalog dengan metadata dasar | `[GLOBAL]` | `[ ]` | `<Link ke catalog entry>` | |
| A-12 | Channel komunikasi domain tersedia (Slack / Teams / mailing list) | `[Lokal]` | `[ ]` | `<Link channel: #dp-domain-name>` | |

**Score Bagian A:** `_____ / 12 item` — Compliance: `_____% `

---

## Bagian B — Lifecycle Gate Checklist

> **Kapan dijalankan:** Setiap kali data product akan melewati gate antar fase lifecycle.
> **Catatan:** Setiap sub-bagian adalah gate mandiri. Gate hanya dibuka jika semua item `[GLOBAL]` berstatus `✅ PASS`.

---

### B.1 — Bootstrap Gate (→ Masuk Fase Design)

> **Tujuan gate ini:** Memastikan justifikasi bisnis valid dan scope terdefinisi sebelum resources desain dialokasikan.

| Tanggal Gate | Keputusan | DPO Sign-off | DGO Sign-off |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<OPEN / HOLD / REJECT>` | `<Nama, tgl>` | `<Nama, tgl>` |

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B1-01 | Data Product Canvas telah diisi lengkap (semua 8 blok) dan disetujui DPO | `[GLOBAL]` | `[ ]` | `<Link ke B-03 Canvas>` | |
| B1-02 | Data Product Proposal telah disetujui stakeholder bisnis | `[GLOBAL]` | `[ ]` | `<Link ke B-02 Proposal + sign-off>` | |
| B1-03 | Business case memiliki justifikasi bisnis yang terukur (KPI atau use case spesifik) | `[GLOBAL]` | `[ ]` | `<Link ke proposal §Business Case>` | |
| B1-04 | Consumer dan use case minimal telah diidentifikasi (min. 1 confirmed consumer) | `[GLOBAL]` | `[ ]` | `<Nama consumer: ___>` | |
| B1-05 | Preliminary data profiling telah dilakukan pada sistem sumber | `[GLOBAL]` | `[ ]` | `<Link ke B-04 Profiling Report>` | |
| B1-06 | Klasifikasi data awal telah ditentukan (Public/Internal/Restricted/Confidential) | `[GLOBAL]` | `[ ]` | `<Klasifikasi: ___, Dasar: ___>` | |
| B1-07 | Apakah data product memproses data pribadi? Jika Ya → checklist Bagian E sudah dimulai | `[GLOBAL]` | `[ ]` | `<Ya/Tidak. Jika Ya: link ke E-01 awal>` | |
| B1-08 | Estimasi biaya operasional (infra + SDM) tersedia dan dalam batas anggaran | `[Lokal]` | `[ ]` | `<Link ke proposal §Cost Estimate>` | |

**Score B.1:** `_____ / 8 item` — Compliance: `_____%`

---

### B.2 — Design Gate (→ Masuk Fase Development)

> **Tujuan gate ini:** Memastikan arsitektur, kontrak, dan compliance selesai sebelum kode ditulis.

| Tanggal Gate | Keputusan | DPO Sign-off | DGO Sign-off |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<OPEN / HOLD / REJECT>` | `<Nama, tgl>` | `<Nama, tgl>` |

#### B.2.1 — Arsitektur dan Kontrak

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B2-01 | Data Product Design Document (D-01) selesai dan di-review oleh Data Architect | `[GLOBAL]` | `[ ]` | `<Link ke D-01>` | |
| B2-02 | Data Contract Specification (D-02) selesai: schema, SLO, SLA, semantic definitions | `[GLOBAL]` | `[ ]` | `<Link ke D-02>` | |
| B2-03 | Data Contract YAML (D-03) valid secara sintaks dan tersimpan di Git | `[GLOBAL]` | `[ ]` | `<Link ke repo/D-03, commit hash>` | |
| B2-04 | Output port telah didefinisikan dan mengikuti standar global (format, naming) | `[GLOBAL]` | `[ ]` | `<D-02 §Output Port>` | |
| B2-05 | SLO dan SLA telah disetujui oleh DPO dan di-acknowledge oleh consumer | `[GLOBAL]` | `[ ]` | `<Link ke D-02 §SLA, bukti consumer ack>` | |
| B2-06 | Skema menggunakan vocabulary dari Kamus Data domain (G-01); tidak ada istilah baru tanpa registrasi | `[GLOBAL]` | `[ ]` | `<Konfirmasi Data Steward>` | |
| B2-07 | Architecture Decision Records (ADR) dibuat untuk setiap keputusan arsitektur non-trivial | `[Lokal]` | `[ ]` | `<Link ke decisions/ADR-*.md>` | |

#### B.2.2 — Data Catalog & Metadata

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B2-08 | Data Catalog entry (D-04) telah dibuat dengan metadata lengkap (owner, classification, lineage) | `[GLOBAL]` | `[ ]` | `<Link ke D-04 + catalog URL>` | |
| B2-09 | Data Lineage dari sumber hingga output port terdokumentasi | `[GLOBAL]` | `[ ]` | `<Link ke D-04 §Lineage>` | |
| B2-10 | Tags klasifikasi data diterapkan per kolom di catalog | `[GLOBAL]` | `[ ]` | `<Link ke D-04 §Schema Classification>` | |

#### B.2.3 — Kualitas Data

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B2-11 | Data Quality Design (D-05) selesai: rules, thresholds, dan tool implementasi terdefinisi | `[GLOBAL]` | `[ ]` | `<Link ke D-05>` | |
| B2-12 | Minimal DQ rules untuk dimensi Completeness, Freshness, dan Accuracy telah didefinisikan | `[GLOBAL]` | `[ ]` | `<D-05 §Quality Rules>` | |
| B2-13 | Threshold SLO kualitas telah disetujui DPO dan bisa diukur secara otomatis | `[GLOBAL]` | `[ ]` | `<D-05 §SLO Thresholds>` | |

#### B.2.4 — Keamanan dan Privasi

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B2-14 | Data Risk Assessment (D-06) selesai dan disetujui | `[GLOBAL]` | `[ ]` | `<Link ke D-06>` | |
| B2-15 | Data Access Control Matrix (G-02) selesai: role, hak akses per kolom, mekanisme enforcement | `[GLOBAL]` | `[ ]` | `<Link ke G-02>` | |
| B2-16 | Jika ada PII: RoPA (D-07) selesai dan diverifikasi Legal | `[GLOBAL jika PII]` | `[ ]` | `<Link ke D-07, atau "N/A — no PII" + justifikasi>` | |
| B2-17 | Jika high-risk: DPIA (D-08) selesai, disetujui DPO Organisasi | `[GLOBAL jika high-risk]` | `[ ]` | `<Link ke D-08, atau "N/A" + justifikasi>` | |
| B2-18 | PII masking strategy terdefinisi per kolom per role | `[GLOBAL jika PII]` | `[ ]` | `<G-02 §PII Masking>` | |

#### B.2.5 — Infrastruktur

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B2-19 | Infrastructure Brief (D-09) selesai: stack, sizing, deployment model | `[GLOBAL]` | `[ ]` | `<Link ke D-09>` | |
| B2-20 | SCD & Audit Logging Design (D-12) selesai (jika tabel membutuhkan histori) | `[Lokal]` | `[ ]` | `<Link ke D-12, atau "N/A">` | |
| B2-21 | Consumer Onboarding Guide (DLV-01) draft tersedia sebelum development selesai | `[GLOBAL]` | `[ ]` | `<Link ke DLV-01 draft>` | |

**Score B.2:** `_____ / 21 item` — Compliance: `_____%`

---

### B.3 — Development Gate (→ Masuk Fase Delivery / UAT)

> **Tujuan gate ini:** Memastikan implementasi sesuai desain, semua test lulus, dan siap untuk UAT.

| Tanggal Gate | Keputusan | DPO Sign-off | DGO Sign-off |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<OPEN / HOLD / REJECT>` | `<Nama, tgl>` | `<Nama, tgl>` |

#### B.3.1 — Implementasi Pipeline

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B3-01 | Data Pipeline Brief (V-01) selesai dan disetujui Data Architect | `[GLOBAL]` | `[ ]` | `<Link ke V-01>` | |
| B3-02 | Pipeline bersifat idempoten (re-run menghasilkan output yang sama) | `[GLOBAL]` | `[ ]` | `<Bukti: test case idempotency>` | |
| B3-03 | Error handling dan dead-letter strategy terimplementasi | `[GLOBAL]` | `[ ]` | `<Link ke kode / pipeline config>` | |
| B3-04 | Data lineage ter-capture otomatis di tool (OpenLineage / DataHub / dbt) | `[GLOBAL]` | `[ ]` | `<Link ke lineage graph>` | |

#### B.3.2 — Implementasi Kualitas Data

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B3-05 | Semua DQ rules dari D-05 terimplementasi di pipeline (dbt test / Great Expectations / Soda) | `[GLOBAL]` | `[ ]` | `<Link ke kode DQ tests, last run result>` | |
| B3-06 | DQ test suite berjalan di CI/CD pipeline (tidak hanya manual) | `[GLOBAL]` | `[ ]` | `<Link ke CI/CD config>` | |
| B3-07 | Schema output telah divalidasi terhadap Data Contract (D-03) menggunakan Data Contract CLI | `[GLOBAL]` | `[ ]` | `<Output validasi: "Contract validation: PASS">` | |

#### B.3.3 — Implementasi Keamanan

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B3-08 | RBAC dari G-02 terimplementasi di database / API gateway | `[GLOBAL]` | `[ ]` | `<Link ke infra config, atau test evidence>` | |
| B3-09 | PII masking terimplementasi dan diverifikasi per role | `[GLOBAL jika PII]` | `[ ]` | `<Test result per role>` | |
| B3-10 | Audit logging aktif (siapa mengakses apa kapan) | `[GLOBAL]` | `[ ]` | `<Link ke audit log config>` | |
| B3-11 | Tidak ada secret/credential yang di-hardcode di kode | `[GLOBAL]` | `[ ]` | `<Output secret scan (trufflehog / gitleaks)>` | |

#### B.3.4 — Testing

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B3-12 | Unit tests pipeline lulus (coverage ≥ `<80%>`) | `[GLOBAL]` | `[ ]` | `<Link ke test report, coverage %>` | |
| B3-13 | Integration tests (end-to-end dari source hingga output port) lulus | `[GLOBAL]` | `[ ]` | `<Link ke V-04 Integration Test Report>` | |
| B3-14 | Performance test pada volume data representatif selesai dan dalam batas SLO | `[Lokal]` | `[ ]` | `<Hasil benchmark: latency P95 = ___ms>` | |
| B3-15 | UAT test cases (V-03) telah disiapkan dan disetujui consumer | `[GLOBAL]` | `[ ]` | `<Link ke V-03 UAT Template>` | |

#### B.3.5 — Dokumentasi

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B3-16 | Data API Brief (V-02) selesai (jika ada REST API output port) | `[GLOBAL jika API]` | `[ ]` | `<Link ke V-02>` | |
| B3-17 | README data product di-update di Git repository | `[GLOBAL]` | `[ ]` | `<Link ke README.md>` | |
| B3-18 | Consumer Onboarding Guide (DLV-01) final tersedia | `[GLOBAL]` | `[ ]` | `<Link ke DLV-01 final>` | |

**Score B.3:** `_____ / 18 item` — Compliance: `_____%`

---

### B.4 — Delivery Gate (→ Masuk Fase Monitoring)

> **Tujuan gate ini:** Memastikan go-live aman, consumer siap, dan monitoring aktif sebelum produksi resmi.

| Tanggal Gate | Keputusan | DPO Sign-off | DGO Sign-off |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<OPEN / HOLD / REJECT>` | `<Nama, tgl>` | `<Nama, tgl>` |

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| B4-01 | UAT sign-off dari consumer dan domain owner tersedia secara tertulis | `[GLOBAL]` | `[ ]` | `<Link ke V-03 UAT Sign-off>` | |
| B4-02 | Deployment production berhasil (smoke test lulus) | `[GLOBAL]` | `[ ]` | `<Link ke deployment log / CI/CD run>` | |
| B4-03 | Data Catalog entry di-publish dan data product discoverable | `[GLOBAL]` | `[ ]` | `<Link ke catalog URL>` | |
| B4-04 | Data Contract published dan versioned di Git | `[GLOBAL]` | `[ ]` | `<Link ke repo, tag versi>` | |
| B4-05 | Monitoring dan alerting aktif (freshness, uptime, DQ) | `[GLOBAL]` | `[ ]` | `<Link ke monitoring dashboard>` | |
| B4-06 | Operations Runbook (M-07) tersedia dan diverifikasi on-call engineer | `[GLOBAL]` | `[ ]` | `<Link ke M-07>` | |
| B4-07 | Consumer pertama berhasil melakukan first query / first call (verified) | `[GLOBAL]` | `[ ]` | `<Bukti: screenshot / log>` | |
| B4-08 | Channel notifikasi consumer aktif (Slack, mailing list) | `[GLOBAL]` | `[ ]` | `<Link ke channel: #dp-___ -announce>` | |
| B4-09 | Backup & DR Plan (M-05) terdokumentasi (jika applicable) | `[Lokal]` | `[ ]` | `<Link ke M-05, atau "N/A">` | |
| B4-10 | Self-Service Infrastructure Guide (DLV-02) tersedia (jika applicable) | `[Lokal]` | `[ ]` | `<Link ke DLV-02, atau "N/A">` | |

**Score B.4:** `_____ / 10 item` — Compliance: `_____%`

---

## Bagian C — Ongoing Governance Checklist

> **Kapan dijalankan:** Secara berkala selama fase Monitoring & Operations.

---

### C.1 — Monitoring Bulanan

> **Frekuensi:** Setiap akhir bulan.
> **Owner:** Data Steward, dilaporkan ke Data Product Owner.

**Periode Review:** `<YYYY-MM (contoh: 2025-01)>`

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| C1-01 | Data Quality Report bulan ini telah dipublikasikan (M-02) | `[GLOBAL]` | `[ ]` | `<Link ke M-02 bulan ini>` | |
| C1-02 | SLO freshness terpenuhi (compliance ≥ target SLO) | `[GLOBAL]` | `[ ]` | `<Metric: ___% (target: ≥___)>` | |
| C1-03 | SLO completeness terpenuhi | `[GLOBAL]` | `[ ]` | `<Metric: ___% (target: ≥___)>` | |
| C1-04 | Uptime terpenuhi (sesuai SLA) | `[GLOBAL]` | `[ ]` | `<Metric: ___% (target: ≥___)>` | |
| C1-05 | Semua insiden bulan ini telah ditangani dan post-mortem selesai (jika ada SEV-1/SEV-2) | `[GLOBAL]` | `[ ]` | `<Link ke incident log / post-mortem>` | |
| C1-06 | Consumer feedback bulan ini telah di-review dan action items terdefinisi | `[GLOBAL]` | `[ ]` | `<Link ke feedback log / JIRA>` | |
| C1-07 | Cost Report bulan ini selesai (M-03) | `[Lokal]` | `[ ]` | `<Link ke M-03>` | |
| C1-08 | Tidak ada schema drift yang tidak terdeteksi | `[GLOBAL]` | `[ ]` | `<Konfirmasi: schema validation log atau "no drift">` | |

**Score C.1:** `_____ / 8 item` — Compliance: `_____%`

---

### C.2 — Review Kuartalan

> **Frekuensi:** Setiap kuartal (Q1/Q2/Q3/Q4).
> **Owner:** Data Product Owner, di-review oleh DGO.

**Periode Review:** `<YYYY-QN (contoh: 2025-Q1)>`

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| C2-01 | Data Product masih relevan dan memiliki consumer aktif | `[GLOBAL]` | `[ ]` | `<Metric: unique consumers bulan ini = ___ >` | |
| C2-02 | SLO dan SLA masih sesuai kebutuhan bisnis dan consumer (tidak perlu perubahan) | `[GLOBAL]` | `[ ]` | `<Konfirmasi DPO + consumer representative>` | |
| C2-03 | Data Contract masih valid; tidak ada breaking change tanpa notifikasi 30 hari | `[GLOBAL]` | `[ ]` | `<Link ke changelog (M-06)>` | |
| C2-04 | Access Control Matrix (G-02) di-review; tidak ada akun zombie atau akses kadaluarsa | `[GLOBAL]` | `[ ]` | `<Link ke G-02 review record>` | |
| C2-05 | Kamus Data (G-01) diperbarui jika ada istilah atau enum baru | `[GLOBAL]` | `[ ]` | `<Link ke G-01 changelog>` | |
| C2-06 | Data Dictionary (G-03) diperbarui jika ada kolom baru | `[GLOBAL]` | `[ ]` | `<Link ke G-03 changelog, atau "no new columns">` | |
| C2-07 | Risk Assessment (D-06) masih relevan; tidak ada risiko baru yang belum di-assess | `[GLOBAL]` | `[ ]` | `<Konfirmasi DA + Legal>` | |
| C2-08 | Dokumentasi onboarding consumer (DLV-01) masih akurat | `[GLOBAL]` | `[ ]` | `<Konfirmasi Data Steward: "reviewed, up-to-date">` | |
| C2-09 | Roadmap data product untuk kuartal berikutnya tersedia | `[Lokal]` | `[ ]` | `<Link ke JIRA roadmap / sprint plan>` | |
| C2-10 | Consumer aktif dinotifikasi tentang perubahan kuartal ini | `[GLOBAL]` | `[ ]` | `<Link ke announcement di channel>` | |

**Score C.2:** `_____ / 10 item` — Compliance: `_____%`

---

### C.3 — Audit Tahunan

> **Frekuensi:** Sekali setahun.
> **Owner:** DGO, hasilnya dilaporkan ke governance council.

**Tahun Audit:** `<YYYY>`

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| C3-01 | Seluruh data product di domain telah diinventarisasi dan diverifikasi statusnya | `[GLOBAL]` | `[ ]` | `<Link ke domain data product inventory>` | |
| C3-02 | Data product yang tidak memiliki consumer aktif >6 bulan telah di-flag untuk evaluasi retirement | `[GLOBAL]` | `[ ]` | `<Daftar produk yang di-flag: ___, ___>` | |
| C3-03 | Seluruh RoPA domain diverifikasi akurat dan disetujui DPO Organisasi | `[GLOBAL jika PII]` | `[ ]` | `<Link ke D-07 per product, tanda tangan DPO>` | |
| C3-04 | DPIA di-review dan tidak ada perubahan pemrosesan yang memerlukan DPIA baru | `[GLOBAL jika PII]` | `[ ]` | `<Link ke D-08 review record>` | |
| C3-05 | Data Retention Policy (G-04) diimplementasikan dan diverifikasi | `[GLOBAL]` | `[ ]` | `<Link ke G-04, bukti enforcement>` | |
| C3-06 | Seluruh akses privileged (Restricted/Confidential) di-audit log-nya dan tidak ada anomali | `[GLOBAL]` | `[ ]` | `<Link ke audit log review>` | |
| C3-07 | Federated governance standards global diikuti oleh semua domain (interoperability check) | `[GLOBAL]` | `[ ]` | `<Laporan DGO lintas domain>` | |
| C3-08 | Lessons learned dari insiden tahun ini telah diintegrasikan ke dalam template dan SOP | `[GLOBAL]` | `[ ]` | `<Link ke post-mortem repository>` | |

**Score C.3:** `_____ / 8 item` — Compliance: `_____%`

---

## Bagian D — Cross-Domain Interoperability Checklist

> **Kapan dijalankan:** Setiap kali data product ini akan dikonsumsi oleh domain lain (lintas domain boundary).
> **Owner:** Data Product Owner domain sumber + Domain Owner tujuan.

**Domain Tujuan (Consumer):** `<Nama Domain Konsumen>`
**Data Product yang Diinteroperasi:** `<Nama Data Product>`

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| D-01 | Semantic alignment: atribut kunci menggunakan definisi dari Kamus Data global atau shared vocabulary | `[GLOBAL]` | `[ ]` | `<Konfirmasi: atribut X domain A = atribut Y domain B>` | |
| D-02 | Tidak ada konflik definisi atau nilai enum antara dua domain | `[GLOBAL]` | `[ ]` | `<Perbandingan G-01 domain A vs domain B>` | |
| D-03 | Data Contract (D-03) dari domain sumber telah diakui dan di-acknowledge oleh domain konsumen | `[GLOBAL]` | `[ ]` | `<Bukti: consumer ack pada D-03, atau ticket sign-off>` | |
| D-04 | Output port yang digunakan mengikuti format standar global (OpenAPI / AsyncAPI / ISO format) | `[GLOBAL]` | `[ ]` | `<Link ke output port spec>` | |
| D-05 | Data lineage lintas domain terdokumentasi (dari sumber hingga ke domain konsumen) | `[GLOBAL]` | `[ ]` | `<Link ke lineage graph lintas domain>` | |
| D-06 | Tidak ada circular dependency antara domain A dan domain B | `[GLOBAL]` | `[ ]` | `<Konfirmasi: dependency graph clean>` | |
| D-07 | SLA antara domain sumber dan domain konsumen telah disepakati secara tertulis | `[GLOBAL]` | `[ ]` | `<Link ke cross-domain SLA agreement>` | |
| D-08 | Access provisioning untuk domain konsumen mengikuti prosedur standar (DLV-01 §3) | `[GLOBAL]` | `[ ]` | `<Ticket akses: DAR-___>` | |
| D-09 | Jika data product mengandung PII: domain konsumen telah menandatangani Data Sharing Agreement | `[GLOBAL jika PII]` | `[ ]` | `<Link ke DSA yang ditandatangani>` | |
| D-10 | Notifikasi perubahan (breaking change) akan dikirim ke domain konsumen minimum 30 hari sebelumnya | `[GLOBAL]` | `[ ]` | `<Konfirmasi: domain konsumen ada di subscriber list>` | |

**Score Bagian D:** `_____ / 10 item` — Compliance: `_____%`

---

## Bagian E — Privacy & Compliance Checklist

> **Kapan dijalankan:** Saat onboarding (jika ada PII), dan setiap kali ada perubahan pada jenis atau cara pemrosesan data pribadi.
> **Owner:** Data Steward + Legal/Compliance.

:::warning Mandatory untuk Data PII
Bagian ini **wajib diselesaikan** dan disetujui DPO Organisasi sebelum data product yang memproses PII melewati Design Gate (B.2).
:::

**Tanggal Review:** `<YYYY-MM-DD>`
**Perubahan yang Memicu Review:** `<deskripsi perubahan / "initial assessment">`

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| E-01 | Inventori PII lengkap: setiap kolom PII teridentifikasi dengan kategori (biasa / sensitif / anak) | `[GLOBAL]` | `[ ]` | `<Link ke D-04 §Data Classification>` | |
| E-02 | Dasar hukum pemrosesan data pribadi terdefinisi per kategori PII (persetujuan / kontrak / kewajiban hukum) | `[GLOBAL]` | `[ ]` | `<Link ke D-07 RoPA §Legal Basis>` | |
| E-03 | RoPA (D-07) selesai, akurat, dan disetujui Legal | `[GLOBAL]` | `[ ]` | `<Link ke D-07 + tanda tangan Legal>` | |
| E-04 | Jika volume subjek data >1.000 atau pemrosesan high-risk: DPIA (D-08) selesai | `[GLOBAL jika high-risk]` | `[ ]` | `<Link ke D-08, atau "N/A: volume = ___, tidak high-risk">` | |
| E-05 | DPIA telah disetujui DPO Organisasi (bukan hanya DPO domain) | `[GLOBAL jika DPIA wajib]` | `[ ]` | `<Link ke D-08 + tanda tangan DPO Organisasi>` | |
| E-06 | Data Retention Policy (G-04) diterapkan: setiap kategori data memiliki jadwal retensi dan purge | `[GLOBAL]` | `[ ]` | `<Link ke G-04>` | |
| E-07 | Mekanisme hak subjek data terimplementasi: akses, koreksi, penghapusan (sesuai UU PDP) | `[GLOBAL jika PII]` | `[ ]` | `<Prosedur: ___, link SOP>` | |
| E-08 | Transfer data ke pihak ketiga (vendor, partner) memiliki DPA atau klausul perlindungan data | `[GLOBAL jika ada transfer]` | `[ ]` | `<Link ke DPA, atau "tidak ada transfer pihak ketiga">` | |
| E-09 | Prosedur notifikasi breach data terdefinisi dan on-call team mengetahuinya | `[GLOBAL jika PII]` | `[ ]` | `<Link ke M-07 §Breach Notification>` | |
| E-10 | Data tidak disimpan di sistem personal (laptop, personal cloud storage) | `[GLOBAL]` | `[ ]` | `<Konfirmasi: policy communicated + audit spot-check>` | |

**Score Bagian E:** `_____ / 10 item` — Compliance: `_____%`

---

## Bagian F — Retirement Readiness Checklist

> **Kapan dijalankan:** Setelah keputusan retirement dibuat, sebelum proses decommission dimulai.
> **Owner:** Data Product Owner, disetujui DGO dan Domain Owner.

**Tanggal Keputusan Retirement:** `<YYYY-MM-DD>`
**Target Sunset Date:** `<YYYY-MM-DD>`
**Alasan Retirement:** `<Tidak ada consumer aktif / Digantikan vX.Y / End of program / Lainnya>`

| ID | Item | Tag | Status | Bukti / Evidence | Catatan |
|---|---|---|---|---|---|
| F-01 | Usage analysis selesai: konfirmasi tidak ada consumer aktif atau semua consumer setuju migrasi | `[GLOBAL]` | `[ ]` | `<Metric: last query date = ___, consumer count = 0>` | |
| F-02 | Impact analysis selesai: tidak ada sistem kritis yang masih bergantung pada data product ini | `[GLOBAL]` | `[ ]` | `<Link ke E-01 EoSL Report §Impact Analysis>` | |
| F-03 | Consumer notification dikirim **minimum 90 hari** sebelum sunset date | `[GLOBAL]` | `[ ]` | `<Bukti: email / announcement, tanggal kirim = ___)>` | |
| F-04 | Migration path tersedia bagi consumer (data product pengganti atau alternatif) | `[GLOBAL]` | `[ ]` | `<Link ke pengganti: ___, atau konfirmasi "no replacement needed">` | |
| F-05 | Consumer migration guide tersedia (langkah pindah dari produk lama ke baru) | `[GLOBAL jika ada pengganti]` | `[ ]` | `<Link ke migration guide>` | |
| F-06 | Data archival plan sesuai Data Retention Policy (G-04): apa yang diarsip, berapa lama, di mana | `[GLOBAL]` | `[ ]` | `<Link ke G-04 + archival plan>` | |
| F-07 | PII deletion plan terdefinisi dan disetujui DPO Organisasi | `[GLOBAL jika PII]` | `[ ]` | `<Link ke deletion plan + DPO approval>` | |
| F-08 | EoSL Report (E-01) selesai dan disetujui | `[GLOBAL]` | `[ ]` | `<Link ke E-01>` | |
| F-09 | Infrastructure decommission plan tersedia: timeline shutdown compute, storage, network | `[GLOBAL]` | `[ ]` | `<Link ke infra decommission ticket>` | |
| F-10 | Data Catalog entry di-update status menjadi "deprecated" atau "retired" | `[GLOBAL]` | `[ ]` | `<Link ke catalog entry yang sudah di-update>` | |
| F-11 | Final lessons learned terdokumentasi dan dimasukkan ke knowledge base tim | `[GLOBAL]` | `[ ]` | `<Link ke post-mortem / lessons learned doc>` | |

**Score Bagian F:** `_____ / 11 item` — Compliance: `_____%`

---

## Annex A — Scoring Guide & Compliance Score

### Rumus Compliance Score

```
Compliance Score (%) = (Jumlah PASS + 0.5 × Jumlah PARTIAL) / (Total item - Jumlah N/A) × 100
```

**Contoh:**
- Total item: 20, PASS: 16, PARTIAL: 2, FAIL: 1, N/A: 1
- Score = (16 + 0.5×2) / (20-1) × 100 = 17/19 × 100 = **89.5%**

### Interpretasi Score

| Score | Status | Konsekuensi |
|---|---|---|
| `≥ 95%` | **PASS — Gate Terbuka** | Boleh lanjut ke fase berikutnya |
| `85% – <95%` | **CONDITIONAL** | Lanjut dengan action plan terdefinisi; DGO sign-off required |
| `70% – <85%` | **HOLD** | Gate ditahan; remediasi dalam `<14 hari>` sebelum re-review |
| `< 70%` | **REJECT** | Gate ditolak; kembali ke fase sebelumnya; re-review dari awal |

:::note Pengecualian untuk Item `[GLOBAL]`
Satu pun item berlabel `[GLOBAL]` yang berstatus `❌ FAIL` secara otomatis menghasilkan **REJECT**, terlepas dari total score. Item global tidak bisa dikompensasi dengan score keseluruhan yang tinggi.
:::

### Rekapitulasi Score

| Bagian | Total Item | PASS | PARTIAL | FAIL | N/A | Score |
|---|---|---|---|---|---|---|
| A — Domain Registration | 12 | | | | | |
| B.1 — Bootstrap Gate | 8 | | | | | |
| B.2 — Design Gate | 21 | | | | | |
| B.3 — Development Gate | 18 | | | | | |
| B.4 — Delivery Gate | 10 | | | | | |
| C.1 — Monthly | 8 | | | | | |
| C.2 — Quarterly | 10 | | | | | |
| C.3 — Annual Audit | 8 | | | | | |
| D — Cross-Domain Interop | 10 | | | | | |
| E — Privacy & Compliance | 10 | | | | | |
| F — Retirement Readiness | 11 | | | | | |

---

## Annex B — Panduan Remediasi per Item Gagal

Gunakan tabel ini sebagai referensi cepat saat item berstatus `❌ FAIL` atau `⚠️ PARTIAL`.

| Item ID | Tindakan Remediasi | PIC Default | Estimasi Waktu |
|---|---|---|---|
| A-01 s.d. A-04 | Lakukan domain mapping workshop (Event Storming); output: bounded context diagram | DA + Domain Owner | `1–2 hari kerja` |
| B1-01 | Buat / lengkapi Data Product Canvas bersama DPO dan consumer representative | DA + DPO | `1 hari kerja` |
| B2-02, B2-03 | Lengkapi dan validasi Data Contract; jalankan `data-contract-cli validate` | DA + DE | `1–2 hari kerja` |
| B2-16, B2-17 | Ajukan permohonan DPIA ke DPO Organisasi; sertakan dokumen RoPA | DS + Legal | `3–7 hari kerja` |
| B3-07 | Jalankan `data-contract-cli test --contract D-03.yaml`; perbaiki discrepancy | DE | `Setengah hari kerja` |
| B3-11 | Jalankan secret scanning: `trufflehog git <repo-url>`; hapus secrets dari history | DE | `1 hari kerja` |
| C2-04 | Jalankan access review di IAM/Vault; revoke akun yang tidak aktif >90 hari | DS + SRE | `Setengah hari kerja` |
| D-02 | Lakukan semantic alignment workshop antara dua domain; output: mapping table | DS domain A + DS domain B | `2–4 jam` |
| E-03 | Lengkapi RoPA menggunakan template D-07; minta sign-off Legal dalam 3 hari | DS + Legal | `1–2 hari kerja` |
| F-03 | Kirim notifikasi retirement via email dan channel Slack; simpan bukti pengiriman | DPO + PM | `2 jam` |

---

## Annex C — Ownership Matrix dan Eskalasi Governance

### RASCI Governance Checklist

| Aktivitas | Domain Owner | Data Steward | DGO | Legal | Exec Sponsor |
|---|---|---|---|---|---|
| Pengisian checklist harian/bulanan | C | **R** | I | I | I |
| Gate review per lifecycle phase | **A** | S | **R** | C | I |
| Pemberian sign-off gate | **A** | S | **R** | C | I |
| Annual audit | C | S | **A/R** | C | I |
| Resolusi item FAIL kritis | C | **R** | A | C | I |
| Eskalasi cross-domain conflict | C | S | **A/R** | C | I |
| Eskalasi ke governance council | I | I | **R** | C | **A** |

### Jalur Eskalasi

| Level | Trigger | PIC | SLA Respons |
|---|---|---|---|
| **L1** | Item PARTIAL — deadline remediasi terlewat | Data Steward → Data Product Owner | `1 hari kerja` |
| **L2** | Item FAIL — gate tidak bisa dibuka | Data Product Owner → DGO | `2 hari kerja` |
| **L3** | Konflik antar domain (interoperabilitas, kepemilikan data) | DGO → Data Governance Council | `5 hari kerja` |
| **L4** | Pelanggaran privasi / regulatory violation | DGO → DPO Organisasi + Legal + Exec | `Segera (< 4 jam)` |

---

*Dokumen ini dikelola oleh **Data Governance Officer** dan diperbarui setiap kali ada perubahan pada standar governance global atau regulasi yang berlaku. Versi terbaru selalu ada di: `<https://catalog.domain.org/governance/G-05>`.*
