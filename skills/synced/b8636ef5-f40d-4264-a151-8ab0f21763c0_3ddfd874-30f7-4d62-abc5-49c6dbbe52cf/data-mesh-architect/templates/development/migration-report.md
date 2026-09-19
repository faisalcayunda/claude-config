---
title: "Migration Report — <Nama Migrasi>"
sidebar_label: "Migration Report"
sidebar_position: 10
description: "Laporan pelaksanaan migrasi data: source-to-target mapping aktual, row counts, validasi, issues, dan sign-off."
tags: [development, migration, data-migration, validation]
doc_id: "V-10"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Migration Report

> **Tujuan dokumen ini:** Laporan eksekusi migrasi data — mendokumentasikan apa yang sebenarnya terjadi (bukan yang direncanakan), mencakup row counts, temuan, deviasi dari rencana, dan sign-off.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 1.0 | Laporan migrasi selesai | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `V-10` |
| **Domain** | `<Nama Domain>` |
| **Nama Migrasi** | `<Deskripsi singkat migrasi>` |
| **Tanggal Eksekusi** | `<YYYY-MM-DD HH:MM – HH:MM WIB>` |
| **Status** | `<COMPLETE / PARTIAL / FAILED>` |
| **Migration Lead** | `<Nama DE, Email>` |
| **Sign-off** | `<Nama DPO, tanggal>` |
| **Dokumen terkait** | [D-01 Design Document](../design/design-document.md) · [D-02 Data Contract](../design/data-contract-spec.md) · [V-03 UAT Template](./uat-integration-test.md) |

---

## 1. Ringkasan Eksekusi

| Atribut | Nilai |
|---|---|
| Total rows di source | `<N>` |
| Total rows berhasil dimigrasikan | `<N>` |
| Rows gagal / ditolak | `<N>` |
| Success rate | `<___>%` |
| Durasi total | `<X jam Y menit>` |
| Rollback dilakukan? | `<Ya / Tidak>` |

---

## 2. Source-to-Target Mapping Aktual

| Source Object | Target Object | Rows Source | Rows Target | Delta | Status |
|---|---|---|---|---|---|
| `<src_schema.table_1>` | `<tgt_schema.table_1>` | `<N>` | `<N>` | `0` | ✅ |
| `<src_schema.table_2>` | `<tgt_schema.table_2>` | `<N>` | `<N-5>` | `-5` | ⚠️ 5 rejected |
| `<src_schema.lookup>` | `<tgt_schema.dim_ref>` | `<N>` | `<N>` | `0` | ✅ |

---

## 3. Validasi Pasca Migrasi

### 3.1 Row Count Reconciliation

```sql
-- Source count
SELECT '<table_1>' AS tabel, COUNT(*) AS rows FROM <src_schema>.table_1
UNION ALL SELECT '<table_2>', COUNT(*) FROM <src_schema>.table_2;

-- Target count  
SELECT '<table_1>' AS tabel, COUNT(*) AS rows FROM <tgt_schema>.table_1
UNION ALL SELECT '<table_2>', COUNT(*) FROM <tgt_schema>.table_2;
```

### 3.2 Checksum Validation

| Tabel | Kolom | Source Checksum | Target Checksum | Match? |
|---|---|---|---|---|
| `table_1` | `SUM(jumlah)` | `<nilai>` | `<nilai>` | ✅ |
| `table_1` | `MAX(updated_at)` | `<nilai>` | `<nilai>` | ✅ |
| `table_2` | `COUNT(DISTINCT id)` | `<nilai>` | `<nilai>` | ✅ |

### 3.3 Business Rule Validation

| Rule | Expected | Actual | Status |
|---|---|---|---|
| Tidak ada NIK duplikat | 0 duplicates | `<hasil>` | `<✅/❌>` |
| Status hanya dari enum valid | 100% valid | `<hasil>%` | `<✅/❌>` |
| Jumlah non-negatif | 100% ≥ 0 | `<hasil>%` | `<✅/❌>` |

---

## 4. Issues dan Resolusi

| ID | Tabel | Deskripsi Issue | Rows Terdampak | Resolusi | Status |
|---|---|---|---|---|---|
| ISS-01 | `table_2` | `<5 records memiliki tanggal NULL>` | `5` | `<Di-set ke tanggal default YYYY-MM-DD>` | ✅ Resolved |
| ISS-02 | `<tabel>` | `<Deskripsi issue>` | `<N>` | `<Resolusi>` | `<Status>` |

---

## 5. Sign-off

| Role | Nama | Sign-off Date | Catatan |
|---|---|---|---|
| Migration Lead (DE) | `<Nama>` | `<YYYY-MM-DD>` | |
| Data Product Owner | `<Nama>` | `<YYYY-MM-DD>` | |
| Consumer Representative | `<Nama>` | `<YYYY-MM-DD>` | |
| Data Steward | `<Nama>` | `<YYYY-MM-DD>` | |
