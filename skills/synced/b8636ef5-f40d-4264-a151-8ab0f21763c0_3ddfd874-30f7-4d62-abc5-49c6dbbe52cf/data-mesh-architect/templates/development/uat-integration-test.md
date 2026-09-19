---
title: "UAT & Integration Test — <Nama Data Product>"
sidebar_label: "UAT & Integration Test"
sidebar_position: 3
description: "Template User Acceptance Testing dan Integration Testing untuk validasi data product sebelum go-live"
tags: [development, uat, integration-test, testing, quality-assurance]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# UAT & Integration Test Template

> **Tujuan dokumen ini:** Mendefinisikan skenario, kriteria penerimaan, dan prosedur pengujian yang harus diselesaikan sebelum data product di-deploy ke production. UAT dilakukan bersama consumer data product, Integration Test dilakukan oleh tim teknis.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## Informasi Pengujian

| Atribut | Nilai |
|---|---|
| **Data Product** | `<Nama Data Product>` |
| **Versi yang Diuji** | `<1.0.0>` |
| **Environment** | `<Staging>` |
| **Periode UAT** | `<YYYY-MM-DD s.d. YYYY-MM-DD>` |
| **UAT Coordinator** | `<Nama PM>` |
| **Consumer Tester** | `<Nama, Organisasi>` |
| **Technical Tester** | `<Nama Data Engineer>` |

---

## Bagian 1 — User Acceptance Testing (UAT)

### 1.1 Kriteria Penerimaan Global

Data product **dinyatakan LULUS UAT** jika:

```
[ ] Semua test case Critical (P0) lulus
[ ] Minimal 90% test case High (P1) lulus
[ ] Minimal 80% test case Medium (P2) lulus
[ ] Tidak ada open defect dengan severity Critical
[ ] Data Contract validation: datacontract-cli test → 0 failures
[ ] Persetujuan tertulis dari minimal 1 consumer representative
```

### 1.2 Skenario UAT per Use Case

**Format pengisian:**
- **ID:** Kode unik (UAT-001, UAT-002, dst.)
- **Prioritas:** P0 Critical / P1 High / P2 Medium / P3 Low
- **Status:** [ ] Belum / [In Progress] In Progress / [x] Lulus / [ ] Gagal / [Skip] Skip

---

#### Use Case 1: `<Nama Use Case — contoh: Akses Data Profil Beneficiary>`

| ID | Skenario | Langkah | Data Input | Expected Result | Prioritas | Status | Tester | Catatan |
|---|---|---|---|---|---|---|---|---|
| UAT-001 | `<Query data aktif berhasil>` | `<1. Login dengan role analyst_role 2. Query SELECT * WHERE status='aktif' LIMIT 10>` | `<Role: analyst_role>` | `<Return data dengan nama ter-mask; NIK ter-mask>` | `<P0>` | `<[ ]>` | `<Nama>` | |
| UAT-002 | `<Freshness data terpenuhi>` | `<1. Cek MAX(updated_at) di tabel Gold 2. Bandingkan dengan waktu saat ini>` | `<->` | `<MAX(updated_at) < 25 jam dari sekarang>` | `<P0>` | `<[ ]>` | `<Nama>` | |
| UAT-003 | `<Jumlah record sesuai ekspektasi>` | `<1. COUNT(*) di tabel Gold 2. Bandingkan dengan perkiraan volume>` | `<->` | `<COUNT(*) dalam rentang [X-10%, X+10%]>` | `<P1>` | `<[ ]>` | `<Nama>` | |
| UAT-004 | `<PII masking berfungsi>` | `<1. Login sebagai non-privileged user 2. Query kolom NIK>` | `<Role: analyst_role>` | `<NIK tampil sebagai "317104******0001">` | `<P0>` | `<[ ]>` | `<Nama>` | |
| UAT-005 | `<Role unauthorized tidak bisa akses>` | `<1. Login dengan role invalid_role 2. Coba query tabel>` | `<Role: invalid_role>` | `<Error: PERMISSION DENIED>` | `<P0>` | `<[ ]>` | `<Nama>` | |

---

#### Use Case 2: `<Nama Use Case — contoh: API Endpoint Berfungsi>`

| ID | Skenario | Langkah | Input | Expected Result | Prioritas | Status | Tester | Catatan |
|---|---|---|---|---|---|---|---|---|
| UAT-010 | `<GET list resource berhasil>` | `<1. Kirim GET /v1/resource dengan valid token 2. Cek response>` | `<Valid OAuth token>` | `<HTTP 200, response JSON valid, meta ada>` | `<P0>` | `<[ ]>` | `<Nama>` | |
| UAT-011 | `<Pagination berfungsi>` | `<1. GET /v1/resource?page=1&per_page=10 2. Cek meta.total_pages>` | `<page=1, per_page=10>` | `<Response memiliki 10 records, meta.has_next=true>` | `<P1>` | `<[ ]>` | `<Nama>` | |
| UAT-012 | `<Filter status berfungsi>` | `<1. GET /v1/resource?status=aktif 2. Cek semua record>` | `<status=aktif>` | `<Semua record di response memiliki status='aktif'>` | `<P1>` | `<[ ]>` | `<Nama>` | |
| UAT-013 | `<Rate limiting aktif>` | `<1. Kirim 150 request dalam 1 menit 2. Cek response ke-101>` | `<>100 requests/menit>` | `<HTTP 429 dengan header Retry-After>` | `<P1>` | `<[ ]>` | `<Nama>` | |
| UAT-014 | `<Unauthorized request ditolak>` | `<1. GET /v1/resource tanpa token 2. GET dengan expired token>` | `<No token / expired token>` | `<HTTP 401>` | `<P0>` | `<[ ]>` | `<Nama>` | |

---

#### Use Case 3: `<Nama Use Case — contoh: Dashboard menampilkan data yang benar>`

| ID | Skenario | Langkah | Input | Expected Result | Prioritas | Status | Tester | Catatan |
|---|---|---|---|---|---|---|---|---|
| UAT-020 | `<KPI cards menampilkan nilai yang benar>` | `<1. Login ke dashboard 2. Cek nilai KPI 3. Bandingkan dengan query manual>` | `<->` | `<Nilai dashboard = query manual ±0.1%>` | `<P0>` | `<[ ]>` | `<Nama>` | |
| UAT-021 | `<Filter wilayah berfungsi>` | `<1. Pilih filter wilayah "X" 2. Cek semua chart terupdate>` | `<Wilayah = "X">` | `<Semua chart menampilkan data wilayah X saja>` | `<P1>` | `<[ ]>` | `<Nama>` | |

---

### 1.3 Defect Log

| ID Defect | Ditemukan dari Test | Deskripsi | Severity | Status | Assignee | Resolusi |
|---|---|---|---|---|---|---|
| DEF-001 | `<UAT-003>` | `<Deskripsi bug>` | `<P0/P1/P2>` | `<Open/Fixed/Closed>` | `<Nama DE>` | `<Cara fix>` |

### 1.4 UAT Sign-Off

| Role | Nama | Keputusan | Tanggal | Catatan |
|---|---|---|---|---|
| Consumer Representative | `<Nama>` | `☐ LULUS ☐ LULUS BERSYARAT ☐ GAGAL` | | |
| Data Product Owner | `<Nama>` | `☐ Approved for Production` | | |
| Data Architect | `<Nama>` | `☐ Technical sign-off` | | |
| Project Manager | `<Nama>` | `☐ Koordinasi selesai` | | |

**Kondisi jika "LULUS BERSYARAT":**
> `[Isi kondisi yang harus dipenuhi sebelum atau sesaat setelah go-live]`

---

## Bagian 2 — Integration Test

### 2.1 Scope Integration Test

Integration test dilaksanakan oleh tim teknis untuk memvalidasi bahwa semua komponen bekerja bersama dengan benar di environment staging.

### 2.2 Test Suite — Pipeline End-to-End

| ID | Komponen | Skenario | Expected | Automated? | Status |
|---|---|---|---|---|---|
| INT-001 | `<Ingestion>` | `<Source → Bronze: Data terserap tanpa hilang>` | `<Row count sumber = row count Bronze>` | `<[x] Ya>` | `<[ ]>` |
| INT-002 | `<Cleansing>` | `<Bronze → Silver: Rules diterapkan>` | `<0 null di kolom mandatory, 0 duplikat PK>` | `<[x] Ya>` | `<[ ]>` |
| INT-003 | `<Transformation>` | `<Silver → Gold: Business logic benar>` | `<Nilai kalkulasi sesuai spec>` | `<[x] Ya>` | `<[ ]>` |
| INT-004 | `<Reconciliation>` | `<Gold row count = expected>` | `<Count dalam batas ±5%>` | `<[x] Ya>` | `<[ ]>` |
| INT-005 | `<API>` | `<API connect ke database Gold>` | `<Latency < 200ms P95>` | `<[x] Ya>` | `<[ ]>` |
| INT-006 | `<Data Contract>` | `<datacontract-cli test pass>` | `<0 test failures>` | `<[x] Ya>` | `<[ ]>` |
| INT-007 | `<Security>` | `<PII masking berfungsi di semua output port>` | `<0 PII exposed ke non-privileged roles>` | `<[x] Ya>` | `<[ ]>` |
| INT-008 | `<Monitoring>` | `<Alert terpicu saat DQ failure disimulasikan>` | `<Alert masuk ke Slack dalam 5 menit>` | `<[x] Ya>` | `<[ ]>` |
| INT-009 | `<Rollback>` | `<Rollback ke Bronze berhasil>` | `<Pipeline bisa rerun dari Bronze>` | `<[ ] Manual>` | `<[ ]>` |
| INT-010 | `<Performance>` | `<Pipeline selesai dalam window yang ditentukan>` | `<Total runtime < 4 jam>` | `<[x] Ya>` | `<[ ]>` |

### 2.3 Automated Integration Test Script

```bash
# Jalankan dari root repository
# Pre-requisite: staging environment sudah di-deploy

# 1. Data Contract Test
datacontract-cli test --server staging design/data-contract.yaml

# 2. dbt test (quality rules)
cd dbt_project
dbt test --target staging --select tag:product_name

# 3. Reconciliation check
python tests/integration/test_reconciliation.py --env staging

# 4. API health & latency test
pytest tests/integration/test_api_integration.py \
    --base-url https://api-staging.domain.org/v1 \
    --auth-token $STAGING_API_TOKEN \
    -v

# 5. Security test (PII masking)
pytest tests/integration/test_pii_masking.py \
    --env staging \
    -v

# Expected output:
# ============= X passed, 0 failed in X.Xs =============
```

### 2.4 Performance Benchmark

| Test | Tool | Run Command | Pass Criteria |
|---|---|---|---|
| `<API load test>` | `<k6 / locust>` | `<k6 run tests/load/api_load.js>` | `<P95 < 200ms, 0 error rate>` |
| `<Pipeline throughput>` | `<Airflow metrics>` | `<Monitor DAG run time>` | `<Total < 4 jam>` |
| `<DB query benchmark>` | `<pgbench / custom SQL>` | `<python tests/perf/db_bench.py>` | `<Complex query < 5s>` |

### 2.5 Security Penetration Test Checklist

`[Opsional — lakukan jika data product memproses data sensitif/PII]`

| Test | Tool | Expected | Status |
|---|---|---|---|
| `<SQL Injection>` | `<sqlmap / manual>` | `<No vulnerability found>` | `<[ ]>` |
| `<Authentication bypass>` | `<Manual>` | `<All endpoints require valid auth>` | `<[ ]>` |
| `<Broken authorization>` | `<Manual>` | `<Role isolation berfungsi>` | `<[ ]>` |
| `<PII in logs/responses>` | `<Manual log review>` | `<0 PII dalam log>` | `<[ ]>` |
| `<TLS configuration>` | `<SSL Labs / testssl.sh>` | `<Grade A minimum>` | `<[ ]>` |

---

## Bagian 3 — Go/No-Go Checklist

`[Mandatory sebelum deployment ke production]`

### Technical Readiness
```
[ ] Semua integration tests lulus
[ ] UAT sign-off diterima
[ ] Data Contract validated (0 failures)
[ ] Performance benchmark terpenuhi
[ ] Security review selesai
[ ] Monitoring & alerting dikonfigurasi dan ditest
[ ] Runbook operasional sudah ada
[ ] Rollback procedure sudah ditest
```

### Documentation Readiness
```
[ ] Data Catalog entry sudah diupdate
[ ] Pipeline Brief final sudah dicommit
[ ] API Brief & OpenAPI spec sudah dipublikasikan
[ ] Consumer onboarding guide sudah ada
```

### Governance & Compliance
```
[ ] RoPA sudah diisi (jika ada PII)
[ ] DPIA sudah disetujui (jika diperlukan)
[ ] Data Classification labels sudah diterapkan
[ ] Access control sudah dikonfigurasi sesuai design
```

**Keputusan Go/No-Go:**

| Role | Nama | Keputusan | Tanggal |
|---|---|---|---|
| Data Product Owner | `<Nama>` | `☐ GO ☐ NO-GO` | |
| Data Architect | `<Nama>` | `☐ GO ☐ NO-GO` | |
| SRE / DevOps | `<Nama>` | `☐ GO ☐ NO-GO` | |
| Project Manager | `<Nama>` | `☐ GO ☐ NO-GO` | |
