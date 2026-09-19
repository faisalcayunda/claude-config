---
title: "Data Quality Design — <Nama Data Product>"
sidebar_label: "Quality Design"
sidebar_position: 5
description: "Desain aturan kualitas data, threshold, monitoring, dan proses remediasi untuk data product"
tags: [design, data-quality, slo, great-expectations, soda]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: design
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Quality Design

> **Tujuan dokumen ini:** Mendefinisikan semua aturan kualitas data yang akan diimplementasikan secara otomatis, threshold SLO yang mengikat, strategi monitoring, dan proses remediasi insiden kualitas. Dokumen ini menjadi spesifikasi bagi Data Engineer untuk mengimplementasikan test suite.

:::info Hubungan dengan Data Contract
SLO kualitas di dokumen ini **harus konsisten** dengan yang tertulis di Data Contract:
- Narasi: `../design/data-contract-spec.md` — Bagian 2 (SLI/SLO)
- YAML: `../design/data-contract.yaml` — Bagian `quality`
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## Ringkasan Quality Strategy

| Atribut | Detail |
|---|---|
| **Framework** | `<Great Expectations / Soda Core / dbt tests / Kombinasi>` |
| **Eksekusi** | `<Setiap pipeline run / Terjadwal setiap X jam / On-demand>` |
| **Alerting** | `<Slack channel: #dq-alerts / Email / Grafana OnCall>` |
| **Dashboard** | `<Link ke DQ dashboard>` |
| **Penangung Jawab** | `<Data Steward: Nama>` |

---

## 1. Quality Dimensions & SLO per Tabel

`[Mandatory]`

### 1.1 Tabel: `<nama_tabel_1>`

#### Completeness (Kelengkapan)

> *Seberapa lengkap data yang ada — tidak ada nilai yang hilang pada kolom yang seharusnya terisi.*

| Kolom | Aturan | SLO (Target) | Severity Jika Breach | Action |
|---|---|---|---|---|
| `<id>` | Tidak boleh NULL | `100%` | `Kritis Critical` | `Block pipeline, alert immediate` |
| `<nama>` | Tidak boleh NULL | `>99.5%` | `Tinggi High` | `Alert, quarantine bad records` |
| `<tanggal>` | Tidak boleh NULL | `>99%` | `Tinggi High` | `Alert, log missing records` |
| `<alamat>` | Tidak boleh NULL | `>90%` | `Sedang Medium` | `Log, report weekly` |
| `<keterangan>` | Boleh NULL (opsional) | `N/A` | `N/A` | `N/A` |

#### Uniqueness (Keunikan)

> *Tidak ada duplikasi pada kolom atau kombinasi kolom yang seharusnya unik.*

| Kolom / Kombinasi | Aturan | SLO | Severity | Action |
|---|---|---|---|---|
| `<id>` | Unique per table | `100%` | `Kritis Critical` | `Block load, deduplicate upstream` |
| `<kode_referensi>` | Unique per table | `100%` | `Kritis Critical` | `Block load, investigate source` |
| `<(tanggal, entitas_id)>` | Composite unique | `>99.9%` | `Tinggi High` | `Alert, deduplicate` |

#### Validity (Validitas Format & Range)

> *Data berada dalam format yang benar dan rentang nilai yang masuk akal.*

| Kolom | Aturan Validasi | SLO | Severity | Action |
|---|---|---|---|---|
| `<nik>` | Tepat 16 digit angka | `>99.9%` | `Tinggi High` | `Quarantine, notify upstream` |
| `<tanggal_lahir>` | `< CURRENT_DATE` | `100%` | `Kritis Critical` | `Reject record` |
| `<email>` | Format email valid | `>99%` | `Sedang Medium` | `Flag, report` |
| `<status>` | IN ('aktif','nonaktif','pending') | `100%` | `Tinggi High` | `Default ke 'pending', alert` |
| `<jumlah>` | `>= 0` | `100%` | `Kritis Critical` | `Reject record` |
| `<koordinat_lat>` | BETWEEN -11 AND 6 | `>99%` | `Sedang Medium` | `Nullify, alert` |

#### Consistency (Konsistensi)

> *Data konsisten dengan sumber lain atau aturan bisnis lintas-kolom.*

| Aturan | Kolom Terlibat | Cara Ukur | SLO | Severity |
|---|---|---|---|---|
| `<Kode referensi harus ada di tabel referensi>` | `<kode_ref, dim_referensi.kode>` | `<Referential integrity check>` | `100%` | `Kritis Critical` |
| `<Jumlah total harus = sum of detail>` | `<total, detail_table.subtotal>` | `<Aggregation reconciliation>` | `>99.9%` | `Tinggi High` |
| `<Tanggal selesai >= tanggal mulai>` | `<tgl_mulai, tgl_selesai>` | `<Cross-column comparison>` | `100%` | `Kritis Critical` |

#### Timeliness / Freshness (Kemutakhiran)

> *Data tersedia tepat waktu sesuai SLO freshness.*

| Metric | Cara Ukur | SLO | Severity |
|---|---|---|---|
| `<Freshness dari sumber>` | `<MAX(updated_at) - CURRENT_TIMESTAMP>` | `<< 25 jam>` | `Kritis Critical jika > 25 jam` |
| `<Row count dibanding hari sebelumnya>` | `<COUNT(*) vs yesterday>` | `<Dalam batas ±30%>` | `Tinggi High jika anomali` |
| `<Ketersediaan data hari ini>` | `<COUNT(*) WHERE tanggal = CURRENT_DATE>` | `<> 0 setelah jam 06:00>` | `Kritis Critical` |

*(Duplikasi seksi 1.1 untuk setiap tabel dalam data product)*

---

## 2. Implementasi Test Suite

`[Mandatory]` — *Role: Data Engineer*

### 2.1 dbt Tests (untuk SQL-based pipelines)

```yaml
# models/<schema>/<nama_tabel_1>.yml
version: 2

models:
  - name: <nama_tabel_1>
    description: "<Deskripsi tabel>"
    columns:
      - name: <id>
        description: "Primary key"
        tests:
          - not_null
          - unique

      - name: <kode_referensi>
        tests:
          - not_null
          - unique
          - relationships:
              to: ref('<tabel_referensi>')
              field: kode

      - name: <status>
        tests:
          - not_null
          - accepted_values:
              values: ['aktif', 'nonaktif', 'pending']

      - name: <jumlah>
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0

      - name: <tanggal_lahir>
        tests:
          - dbt_utils.expression_is_true:
              expression: "tanggal_lahir < current_date"

    # Custom tests untuk freshness
    tests:
      - dbt_utils.recency:
          datepart: hour
          field: updated_at
          interval: 25
```

### 2.2 Great Expectations Suite (untuk Python-based pipelines)

```python
# expectations/<nama_tabel_1>_suite.json
# Link ke file: <https://github.com/org/repo/great_expectations/expectations/...>

"""
Suite summary untuk <nama_tabel_1>:
- expect_column_to_exist: [id, nama, status, tanggal, ...]
- expect_column_values_to_not_be_null: [id, nama, status, tanggal]
- expect_column_values_to_be_unique: [id, kode_referensi]
- expect_column_values_to_be_in_set: status → ['aktif', 'nonaktif', 'pending']
- expect_column_values_to_match_regex: nik → r'^[0-9]{16}$'
- expect_column_values_to_be_between: jumlah → min=0
- expect_table_row_count_to_be_between: min=1, max=None
- expect_column_max_to_be_between: tanggal_lahir → max='today'
"""
```

### 2.3 Soda Core Checks (alternatif)

```yaml
# checks/<nama_tabel_1>_checks.yml
checks for <nama_tabel_1>:
  # Completeness
  - missing_count(id) = 0:
      name: "ID tidak boleh null"
      severity: critical
  - missing_percent(nama) < 0.5:
      name: "Nama max 0.5% missing"
      severity: high

  # Uniqueness
  - duplicate_count(id) = 0:
      name: "ID harus unique"
      severity: critical

  # Validity
  - values in (status) must exist in [aktif, nonaktif, pending]:
      name: "Status harus nilai valid"
      severity: high
  - invalid_percent(nik) < 0.1:
      name: "NIK max 0.1% tidak valid"
      valid regex: '^[0-9]{16}$'
      severity: high

  # Volume anomaly
  - row_count > 0:
      name: "Tabel tidak kosong"
      severity: critical
  - change for row_count < 50%:
      name: "Volume tidak drop > 50% dari kemarin"
      severity: high

  # Freshness
  - freshness(updated_at) < 25h:
      name: "Data tidak lebih dari 25 jam"
      severity: critical
```

---

## 3. Monitoring & Alerting

`[Mandatory]` — *Role: Data Steward + SRE*

### 3.1 Alert Routing

| Severity | Kondisi | Channel | Respons Waktu |
|---|---|---|---|
| `Kritis Critical` | SLO breach pada completeness/uniqueness/freshness | `Slack #dq-critical + Grafana OnCall` | `< 1 jam` |
| `Tinggi High` | SLO breach pada validity/consistency | `Slack #dq-alerts + Email DPO` | `< 2 jam` |
| `Sedang Medium` | Near-breach warning (>80% error budget digunakan) | `Slack #dq-alerts` | `< 4 jam` |
| `[i] Info` | Laporan harian quality scorecard | `Slack #dq-reports` | `Informasional` |

### 3.2 Quality Scorecard (Template Harian)

Scorecard dikirimkan setiap pukul `<07:00 WIB>` ke `<Slack #dq-reports>`:

```
📊 DATA QUALITY SCORECARD — <Nama Data Product>
📅 Tanggal: YYYY-MM-DD | Pipeline Run: HH:MM WIB

Tabel: <nama_tabel_1>
  [x] Completeness:  99.8% (SLO: >99.5%) 
  [x] Uniqueness:    100%  (SLO: 100%)
  [x] Validity:      99.6% (SLO: >99%)
  [x] Freshness:     18h   (SLO: <25h)
  [!] Row Count:     125.430 (-15% vs kemarin) — monitoring

Overall Score: Baik PASS (4/5 checks green)
Error Budget Remaining: 72% bulan ini
```

### 3.3 Quality Dashboard

- **Tool:** `<Grafana / Metabase / Elementary>`
- **Link:** `<https://dashboard.domain.org/dq/product-name>`
- **Refresh:** `<Setiap pipeline run>`

---

## 4. Proses Remediasi Insiden Kualitas

`[Mandatory]`

### 4.1 Decision Tree Remediasi

```
Quality Alert Triggered
│
├── Severity CRITICAL?
│   ├── Ya → Page on-call engineer → Block downstream consumption
│   │         → Investigate root cause → Fix in < 4 jam
│   │         → Post-mortem dalam 48 jam
│   └── Tidak → Continue ke bawah
│
├── Severity HIGH?
│   ├── Ya → Alert DPO + DS → Quarantine bad records
│   │         → Notify consumer → Fix dalam business day
│   └── Tidak → Continue ke bawah
│
└── Severity MEDIUM?
    └── Ya → Log incident → Track in backlog → Fix in next sprint
```

### 4.2 Quarantine Strategy

Bad records yang tidak lolos quality check dipindahkan ke tabel quarantine:

```sql
-- Tabel quarantine: <schema>.<nama_tabel_1>_quarantine
-- Memiliki schema yang sama + kolom tambahan:
--   quarantine_reason   VARCHAR  -- Alasan quarantine
--   quarantine_at       TIMESTAMP -- Kapan di-quarantine
--   quarantine_run_id   VARCHAR  -- Pipeline run ID
--   resolved_at         TIMESTAMP -- Kapan diselesaikan (NULL jika belum)
```

### 4.3 Rollback Strategy

| Kondisi | Strategi Rollback | Execution |
|---|---|---|
| `<Corruption data Gold layer>` | `<Re-run dari Silver layer>` | `<Airflow: trigger DAG dengan date range>` |
| `<Corruption data Silver layer>` | `<Re-run dari Bronze layer>` | `<Airflow: trigger DAG>` |
| `<Salah ingestion dari sumber>` | `<Re-ingest dari sumber asli>` | `<Manual trigger + koordinasi tim sumber>` |

---

## 5. Quality Improvement Roadmap

`[Opsional — isi setelah baseline measurement tersedia]`

| Dimensi | Baseline (Profiling) | Target Q1 | Target Q2 | Inisiatif |
|---|---|---|---|---|
| `<Completeness nama>` | `<97%>` | `<98.5%>` | `<>99.5%>` | `<Improve upstream validation>` |
| `<Validity nik>` | `<95%>` | `<98%>` | `<>99.9%>` | `<Add format validation at ingestion>` |
