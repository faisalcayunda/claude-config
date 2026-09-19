---
title: "Data Dictionary — <Nama Data Product>"
sidebar_label: "Data Dictionary"
sidebar_position: 3
description: "Kamus data teknis level field: definisi, tipe, constraint, nilai valid, dan konteks bisnis setiap atribut dalam data product."
tags: [governance, data-dictionary, schema, metadata, data-catalog]
doc_id: "G-03"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: governance
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Dictionary

> **Tujuan dokumen ini:** Mendefinisikan setiap atribut data dalam data product ini — dari tipe teknis hingga makna bisnis — sehingga setiap consumer dan engineer memiliki pemahaman yang sama tentang apa yang dimaksud oleh setiap field.

:::note G-03 vs G-01
**G-01 Kamus Data (Vocabulary)** = Definisi bisnis dan enum values yang berlaku lintas domain (bukan spesifik ke satu data product).
**G-03 Data Dictionary** = Definisi teknis level field yang spesifik untuk tabel-tabel dalam data product ini, termasuk constraint, nilai default, dan lineage field.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `G-03` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Versi Data Product** | `<vX.Y.Z>` |
| **Data Steward** | `<Nama, Email>` |
| **Dokumen terkait** | [G-01 Kamus Data](./data-vocabulary-template.md) · [D-02 Data Contract](../design/data-contract-spec.md) · [D-04 Data Catalog](../design/data-catalog.md) |

---

## 1. Inventori Tabel dan Objek

| Objek | Tipe | Layer | Baris Tipikal | Diperbarui |
|---|---|---|---|---|
| `<schema>.v_<product>_daily` | SQL View | Gold | `<~1.2M>` | Harian |
| `<schema>.fct_<entity>` | Table | Gold | `<~5M>` | Harian |
| `<schema>.dim_<entity>` | Table | Gold | `<~200K>` | Harian |
| `/api/v1/<resource>` | REST API | API Layer | — | Real-time (from Gold) |

---

## 2. Data Dictionary per Objek

> **Legenda Klasifikasi:**
> - `🟢 Public` — Tidak ada pembatasan
> - `🔵 Internal` — Hanya akses internal organisasi
> - `🟡 Restricted` — Memerlukan justifikasi; PII standar
> - `🔴 Confidential` — Data sangat sensitif; PII kategori khusus

---

### 2.1 `<schema>.v_<product>_daily`

**Deskripsi:** `<Deskripsi singkat view ini — apa yang direpresentasikan, untuk use case apa.>`

| # | Nama Field | Tipe Data | Nullable | Klasifikasi | Kunci | Default | Deskripsi Teknis | Makna Bisnis | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `id` | `UUID` | `NOT NULL` | 🔵 Internal | PK | — | Identifier unik generated via `gen_random_uuid()` | Identifier internal record ini | Generated |
| 2 | `kode_referensi` | `VARCHAR(20)` | `NOT NULL` | 🔵 Internal | — | — | Kode alfanumerik dari sistem sumber. Format: `<[A-Z]{2}-[0-9]{6}>` | Kode yang digunakan dalam dokumen operasional | `<schema_sumber.table_sumber.kolom_sumber>` |
| 3 | `nama` | `VARCHAR(255)` | `NULL` | 🟡 Restricted | — | `NULL` | Nama lengkap entitas. NULL jika belum diverifikasi | Nama seperti tercantum dalam dokumen resmi | `<sumber>` |
| 4 | `nik` | `VARCHAR(16)` | `NULL` | 🔴 Confidential | — | `NULL` | NIK 16 digit. Dimasking di API kecuali role privileged | Nomor Induk Kependudukan sesuai e-KTP | `<sumber>` |
| 5 | `status` | `VARCHAR(20)` | `NOT NULL` | 🔵 Internal | — | `'pending'` | Enum status. Lihat nilai valid di Bagian 3 | Status proses bisnis entitas saat ini | `<sumber>` |
| 6 | `jumlah` | `BIGINT` | `NULL` | 🔵 Internal | — | `NULL` | Dalam satuan Rupiah (IDR), bukan ribu/juta | Nilai nominal yang terkait dengan record ini | `<sumber>` |
| 7 | `tanggal` | `DATE` | `NOT NULL` | 🔵 Internal | — | — | Tanggal record bisnis (bukan tanggal insert). Format: `YYYY-MM-DD` | Tanggal efektif dalam proses bisnis | `<sumber>` |
| 8 | `wilayah_kode` | `VARCHAR(10)` | `NULL` | 🔵 Internal | FK | `NULL` | Kode wilayah BPS 10 digit (provinsi+kab+kec) | Lokasi geografis entitas | `<sumber>` |
| 9 | `_source_system` | `VARCHAR(50)` | `NOT NULL` | 🔵 Internal | — | — | Nama sistem sumber asal data. Metadata field. | Untuk audit lineage | Pipeline-generated |
| 10 | `_loaded_at` | `TIMESTAMPTZ` | `NOT NULL` | 🔵 Internal | — | `NOW()` | Timestamp saat record diinsert ke data product (UTC+7) | Untuk monitoring freshness | Pipeline-generated |
| 11 | `created_at` | `TIMESTAMPTZ` | `NOT NULL` | 🔵 Internal | — | — | Timestamp record dibuat di sistem sumber | Untuk analisis temporal | `<sumber>` |
| 12 | `updated_at` | `TIMESTAMPTZ` | `NOT NULL` | 🔵 Internal | — | — | Timestamp record terakhir diupdate di data product | Untuk incremental load downstream | Pipeline-generated |

---

### 2.2 `<schema>.fct_<entity>`

**Deskripsi:** `<Deskripsi tabel fakta ini.>`

| # | Nama Field | Tipe Data | Nullable | Klasifikasi | Kunci | Deskripsi Teknis | Makna Bisnis | Sumber |
|---|---|---|---|---|---|---|---|---|
| 1 | `fct_id` | `UUID` | `NOT NULL` | 🔵 Internal | PK | Surrogate key fakta | Identifier unik transaksi/event | Generated |
| 2 | `dim_entity_id` | `UUID` | `NOT NULL` | 🔵 Internal | FK→`dim_entity.id` | Foreign key ke dimensi entitas | Entitas yang terlibat | `<sumber>` |
| 3 | `<metric_field>` | `NUMERIC(15,2)` | `NULL` | 🔵 Internal | — | Nilai metrik utama dalam satuan `<Rupiah / unit / %>`  | `<Definisi bisnis metrik>` | `<sumber>` |
| 4 | `event_date` | `DATE` | `NOT NULL` | 🔵 Internal | — | Tanggal event bisnis | Tanggal kejadian yang diukur | `<sumber>` |
| 5 | `_loaded_at` | `TIMESTAMPTZ` | `NOT NULL` | 🔵 Internal | — | Timestamp insert ke data product | Untuk monitoring freshness | Pipeline-generated |

---

### 2.3 `<schema>.dim_<entity>` (SCD Type 2)

**Deskripsi:** `<Deskripsi dimensi dengan riwayat SCD Type 2.>`

| # | Nama Field | Tipe Data | Nullable | Klasifikasi | SCD Role | Deskripsi |
|---|---|---|---|---|---|---|
| 1 | `sk_<entity>` | `BIGINT` | `NOT NULL` | 🔵 Internal | Surrogate Key | Auto-increment surrogate key |
| 2 | `nk_<entity>` | `VARCHAR(20)` | `NOT NULL` | 🔵 Internal | Natural Key | Business key dari sistem sumber |
| 3 | `<atribut_1>` | `VARCHAR(255)` | `NULL` | 🔵 Internal | Tracked | Atribut yang berubah dan ditracking histori |
| 4 | `<atribut_2>` | `VARCHAR(50)` | `NOT NULL` | 🔵 Internal | Tracked | Atribut berubah lainnya |
| 5 | `valid_from` | `DATE` | `NOT NULL` | 🔵 Internal | SCD Metadata | Tanggal mulai berlaku record ini |
| 6 | `valid_to` | `DATE` | `NULL` | 🔵 Internal | SCD Metadata | Tanggal akhir berlaku. `NULL` = record terkini |
| 7 | `is_current` | `BOOLEAN` | `NOT NULL` | 🔵 Internal | SCD Metadata | `TRUE` jika ini versi terkini entitas |
| 8 | `_loaded_at` | `TIMESTAMPTZ` | `NOT NULL` | 🔵 Internal | Metadata | Timestamp insert |

**Query pattern untuk dimensi SCD Type 2:**

```sql
-- Ambil versi terkini saja
SELECT * FROM <schema>.dim_<entity>
WHERE is_current = TRUE;

-- Ambil record yang valid pada tanggal tertentu
SELECT * FROM <schema>.dim_<entity>
WHERE '<tanggal>'::date BETWEEN valid_from AND COALESCE(valid_to, '9999-12-31');
```

---

## 3. Enum Values dan Nilai Valid

### 3.1 `status`

| Nilai | Label Bisnis | Deskripsi | Berlaku sejak |
|---|---|---|---|
| `aktif` | Aktif | Record aktif dalam sistem | `<YYYY-MM-DD>` |
| `nonaktif` | Tidak Aktif | Dinonaktifkan, tidak diproses | `<YYYY-MM-DD>` |
| `pending` | Menunggu | Dalam proses verifikasi | `<YYYY-MM-DD>` |
| `<nilai lain>` | `<label>` | `<deskripsi>` | `<tanggal>` |

*Sumber kebenaran enum: [G-01 Kamus Data §status](./data-vocabulary-template.md)*

### 3.2 `wilayah_kode`

Format: 10 digit BPS. Contoh: `3171040000` = DKI Jakarta, Kota Jakarta Pusat.

Referensi lengkap: [BPS Kode Wilayah](https://sig.bps.go.id/bridging-kode/index)

---

## 4. Aturan Kualitas per Field

| Field | Rule | Threshold | Tool |
|---|---|---|---|
| `id` | Unique, not null | 100% | dbt: `unique`, `not_null` |
| `kode_referensi` | Not null, matches regex `[A-Z]{2}-[0-9]{6}` | 100% | dbt: `not_null`, `accepted_values` |
| `status` | Values dalam enum yang valid | 100% | dbt: `accepted_values` |
| `tanggal` | Tidak ada tanggal di masa depan | 100% | dbt: custom test |
| `jumlah` | Nilai ≥ 0 jika tidak null | 100% | dbt: custom test |
| `nik` | 16 digit, dimulai dengan kode provinsi valid | 99.5% (beberapa record legacy) | Great Expectations |
| `updated_at` | Monotonically increasing per `id` | 100% | dbt: custom test |

---

## 5. Panduan Penggunaan untuk Analyst

### 5.1 Query Paling Umum

```sql
-- Agregasi harian standar
SELECT
    tanggal,
    status,
    COUNT(*)          AS jumlah_record,
    SUM(jumlah)       AS total_nilai
FROM <schema>.v_<product>_daily
WHERE tanggal BETWEEN '<start>' AND '<end>'
GROUP BY 1, 2
ORDER BY 1 DESC;

-- Lookup entity terkini
SELECT v.*, d.<atribut_1>, d.<atribut_2>
FROM <schema>.v_<product>_daily v
JOIN <schema>.dim_<entity> d
  ON v.kode_referensi = d.nk_<entity>
  AND d.is_current = TRUE
WHERE v.tanggal = CURRENT_DATE - 1;
```

### 5.2 Field yang Sering Disalahpahami

| Field | Kesalahpahaman Umum | Klarifikasi |
|---|---|---|
| `jumlah` | "Dianggap dalam ribuan" | Nilai aktual dalam Rupiah penuh. `1500000` = Rp 1.500.000 |
| `tanggal` | "Tanggal data diproses" | Tanggal bisnis (kapan kejadian terjadi), bukan kapan data masuk |
| `_loaded_at` | "Sama dengan `updated_at`" | `_loaded_at` = kapan pipeline memasukkan data. `updated_at` = kapan record terakhir berubah di data product |
| `status = NULL` | "Berarti tidak aktif" | NULL berarti status tidak diketahui / belum diverifikasi. Beda dengan `nonaktif` |

---

## Annex A — Field Lineage Diagram

```
Sistem Sumber A (schema_src.table_raw)
  ├── kolom_a        → bronze.stg_table.col_a     → silver.clean.col_a   → gold.id (transformed)
  ├── kolom_b        → bronze.stg_table.col_b     → silver.clean.col_b   → gold.kode_referensi
  ├── kolom_status   → bronze.stg_table.col_st    → silver.clean.status  → gold.status (mapped via enum)
  └── kolom_tgl      → bronze.stg_table.col_tgl   → silver.clean.tanggal → gold.tanggal (cast to DATE)

Sistem Sumber B (schema_src2.table_ref)
  └── nama_lengkap   → bronze.stg_ref.nama        → silver.clean.nama    → gold.nama
```
