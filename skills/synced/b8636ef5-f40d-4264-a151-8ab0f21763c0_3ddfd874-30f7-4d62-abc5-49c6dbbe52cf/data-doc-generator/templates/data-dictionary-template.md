---
title: Data Dictionary — {SCHEMA_TABLE_NAME}
sidebar_label: G-03 Data Dictionary
sidebar_position: 3
description: 'Kamus data teknis level field: definisi, tipe, constraint, dan konteks bisnis setiap atribut dalam tabel {SCHEMA_TABLE_NAME}.'
tags:
  - governance
  - data-dictionary
  - schema
  - metadata
  - data-catalog
doc_id: {DOC_ID}
doc_title: Data Dictionary — {SCHEMA_TABLE_NAME}
data_product_id: {DATA_PRODUCT_ID}
phase: governance
version: 0.1.0
date: '{CURRENT_DATE}'
last_updated: '{CURRENT_DATE}'
author: ''
owner: ''
classification: {CLASSIFICATION}
data_classification: {DATA_CLASSIFICATION}
pii_flag: {PII_FLAG}
---

# Data Dictionary — `{SCHEMA_TABLE_NAME}`

> **Tujuan dokumen ini:** Mendefinisikan setiap atribut dalam tabel `{SCHEMA_TABLE_NAME}` — dari tipe teknis hingga makna bisnis — sehingga setiap consumer dan engineer memiliki pemahaman yang sama tentang apa yang dimaksud oleh setiap field.

:::note

G-03 vs G-01
**G-01 Kamus Data (Vocabulary)** = Definisi bisnis, enum values, dan aturan validasi (format/range/length/FK/cross-field) yang mendefinisikan nilai valid untuk setiap field.
**G-03 Data Dictionary** = Definisi teknis level field yang spesifik untuk tabel ini, termasuk aturan uniqueness, completeness, dan data quality SLA.

:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi Perubahan | Penulis |
|---|---|---|---|
| `{CURRENT_DATE}` | 0.1.0 | Initial draft | |

---

{HEADER_IDENTIFICATION_SECTION}

## 1. Informasi Tabel

| Atribut | Nilai |
|---|---|
| **Nama Tabel** | `{SCHEMA_TABLE_NAME}` |
| **Tipe Objek** | {Table / View / Materialized View} |
| **Layer** | {Bronze / Silver / Gold / Semantic} |
| **Tipe Tabel** | {Fakta / Dimensi SCD1 / Dimensi SCD2 / Bridge / Reference} |
| **Baris Tipikal** | {jumlah_baris} |
| **Frekuensi Update** | {Harian / Real-time / Bulanan / dst} |
| **Sistem Sumber** | {nama sistem} |

---

## 2. Data Dictionary

> **Legenda Klasifikasi:**
> - `🟢 Public` — Tidak ada pembatasan
> - `🔵 Internal` — Hanya akses internal organisasi
> - `🟡 Restricted` — Memerlukan justifikasi; PII standar
> - `🔴 Confidential` — Data sangat sensitif; PII kategori khusus

---

{TABLE_COLUMNS_SECTION}

---

## 3. Aturan Kualitas per Field

Seksi ini mendokumentasikan aturan yang mengatur **keberadaan** (completeness) dan **keunikan** (uniqueness) nilai di tabel ini. Aturan validasi nilai (format, range, enum, FK, cross-field) ada di file Vocabulary tabel yang sama.

Kolom **Ref. Aturan Bisnis** berisi ID `BVR-{NNN}` yang menunjuk ke aturan bisnis padanannya di Vocabulary — ini yang menjadi dasar bisnis dari setiap constraint teknis di sini. Isi `—` jika tidak ada padanan (misal: PK surrogate yang murni teknis tanpa konteks bisnis).

| Field | Tipe Rule | Rule | Threshold / Implementasi | Ref. Aturan Bisnis | Keterangan |
|---|---|---|---|---|---|
{QUALITY_RULES_ROWS}

**Panduan pengisian:**

- **Uniqueness**: untuk field yang harus unik (PK, natural key, UNIQUE constraint, atau partial UNIQUE)
  - Contoh: `UNIQUE (field_name)` atau `CREATE UNIQUE INDEX idx ON tabel (field) WHERE kondisi`
- **Completeness**: untuk field yang punya aturan kelengkapan (NOT NULL, null rate threshold, wajib diisi dalam kondisi tertentu)
  - Contoh: `NOT NULL` + alasan bisnis; atau `null_rate < 1%` yang dimonitor
- **Mandatory Conditional**: field yang wajib diisi hanya jika field lain memenuhi kondisi tertentu
  - Contoh: `CHECK (status <> 'aktif' OR field IS NOT NULL)`
- **Data Quality SLA**: threshold kualitas yang dimonitor secara otomatis (freshness, accuracy rate, completeness rate)
  - Contoh: `freshness < 24 jam`, `duplicate_rate < 0.01%`
- **Ref. Aturan Bisnis**: ID BVR dari Vocabulary yang menjadi landasan bisnis rule ini. Contoh: `BVR-003` → berarti lihat `BVR-003` di `{table_name}_vocabulary.md` untuk penjelasan plain-language-nya.

---

## 4. Panduan Penggunaan untuk Analyst

### 4.1 Query Paling Umum

```sql
{COMMON_QUERIES}
```

### 4.2 Field yang Sering Disalahpahami

| Field | Kesalahpahaman Umum | Klarifikasi |
|---|---|---|
{MISUNDERSTOOD_FIELDS_ROWS}

---

## Annex A — Field Lineage Diagram

```
{LINEAGE_DIAGRAM}
```
