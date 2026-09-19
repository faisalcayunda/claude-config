---
title: "Dataset — <Nama Dataset>"
sidebar_label: "Dataset"
sidebar_position: 9
description: "Dokumentasi dataset output sebagai artefak data product: schema, sample data, format, dan panduan konsumsi."
tags: [development, dataset, artifact, tabular, output]
doc_id: "V-09"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Dataset

> **Tujuan dokumen ini:** Mendokumentasikan dataset output yang dihasilkan data product ini sebagai artefak yang dapat dikonsumsi — mencakup schema teknis, format file, sample data, dan panduan konsumsi.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `V-09` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Nama Dataset** | `<Nama deskriptif dataset>` |
| **Format** | `<CSV / Parquet / Excel / JSON Lines>` |
| **Lokasi** | `<s3://<bucket>/<path>/>` atau `<schema.tabel>` |
| **Ukuran Tipikal** | `<~500 MB / ~2M rows>` |
| **Update Frekuensi** | `<Harian / Mingguan / Per request>` |
| **Dokumen terkait** | [D-02 Data Contract](../design/data-contract-spec.md) · [G-03 Data Dictionary](../../governance/data-dictionary.md) · [DLV-01 Onboarding](../../delivery/consumer-onboarding-guide.md) |

---

## 1. Schema Dataset

| # | Nama Kolom | Tipe | Nullable | Klasifikasi | Deskripsi | Contoh Nilai |
|---|---|---|---|---|---|---|
| 1 | `<id>` | `string` | No | 🔵 Internal | Identifier unik | `"a1b2c3d4-..."` |
| 2 | `<kode>` | `string` | No | 🔵 Internal | Kode referensi | `"KD-001"` |
| 3 | `<nama>` | `string` | Yes | 🟡 Restricted | Nama entitas | `"<MASKED>"` |
| 4 | `<status>` | `string` | No | 🔵 Internal | Enum status | `"aktif"` |
| 5 | `<jumlah>` | `integer` | Yes | 🔵 Internal | Nilai dalam Rupiah | `1500000` |
| 6 | `<tanggal>` | `date` | No | 🔵 Internal | Tanggal record (YYYY-MM-DD) | `"2025-01-15"` |
| 7 | `updated_at` | `datetime` | No | 🔵 Internal | Timestamp update (ISO 8601) | `"2025-01-15T08:30:00+07:00"` |

---

## 2. Format File dan Konvensi

### 2.1 Parquet (format utama)

```
Partisi    : year=YYYY/month=MM/day=DD/
Kompresi   : Snappy
Encoding   : UTF-8
Null value : null (bukan empty string atau "N/A")
Timestamp  : ISO 8601 dengan timezone UTC+7
```

### 2.2 CSV (format alternatif)

```
Delimiter  : comma (,)
Quote char : double quote (")
Header     : baris pertama berisi nama kolom
Encoding   : UTF-8 with BOM (untuk kompatibilitas Excel)
Null value : empty field (kolom kosong)
Date format: YYYY-MM-DD
```

---

## 3. Cara Mengakses Dataset

```python
import pandas as pd

# Parquet dari S3
df = pd.read_parquet(
    "s3://<bucket>/<path>/year=2025/month=01/",
    storage_options={"key": AWS_KEY, "secret": AWS_SECRET}
)

# Filter incremental
df_recent = pd.read_parquet(
    "s3://<bucket>/<path>/",
    filters=[("year", "=", "2025"), ("month", "=", "01")]
)

# Dari SQL
df = pd.read_sql(
    "SELECT * FROM <schema>.<tabel> WHERE tanggal >= '2025-01-01'",
    con=engine
)
```

---

## 4. Sample Data

```
id,kode,status,jumlah,tanggal,updated_at
a1b2c3d4-e5f6-...,KD-001,aktif,1500000,2025-01-15,2025-01-15T08:30:00+07:00
b2c3d4e5-f6a7-...,KD-002,pending,,2025-01-15,2025-01-15T09:00:00+07:00
c3d4e5f6-a7b8-...,KD-003,nonaktif,750000,2025-01-14,2025-01-15T07:45:00+07:00
```

*Field PII (`nama`, `nik`) tidak diikutsertakan dalam sample di dokumen ini.*

---

## 5. Statistik Kualitas Dataset

*Diperbarui setiap bulan*

| Kolom | % Not Null | % Unique | Min | Max | Catatan |
|---|---|---|---|---|---|
| `id` | 100% | 100% | — | — | PK |
| `kode` | 100% | 99.8% | — | — | Hampir unik |
| `status` | 100% | — | — | — | Enum: aktif/nonaktif/pending |
| `jumlah` | 87% | — | 0 | 50.000.000 | 13% NULL = belum ada nilai |
| `tanggal` | 100% | — | `<first date>` | `<latest date>` | — |
