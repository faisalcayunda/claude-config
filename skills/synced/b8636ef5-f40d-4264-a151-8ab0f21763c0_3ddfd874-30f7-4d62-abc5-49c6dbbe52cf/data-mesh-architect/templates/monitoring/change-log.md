---
title: "Change Log — <Nama Data Product>"
sidebar_label: "Change Log"
sidebar_position: 6
description: "Riwayat perubahan data product menggunakan semantic versioning: schema changes, API changes, SLA updates, dan breaking changes."
tags: [monitoring, changelog, versioning, breaking-change]
doc_id: "M-06"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: monitoring
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Change Log

> **Tujuan dokumen ini:** Riwayat semua perubahan signifikan pada data product ini — terurut dari yang terbaru. Consumer menggunakan dokumen ini untuk mengetahui apa yang berubah, kapan, dan bagaimana migrasinya.

:::note Format Versioning
Dokumen ini menggunakan **Semantic Versioning (SemVer)**:
- **MAJOR** (`v2.0.0`) — Breaking change: hapus kolom, ubah tipe, rename endpoint
- **MINOR** (`v1.1.0`) — Additive change: kolom baru, endpoint baru (backward-compatible)
- **PATCH** (`v1.0.1`) — Bug/data fix tanpa perubahan skema
:::

:::warning Breaking Changes
Setiap entri berlabel `[BREAKING]` memerlukan action dari consumer. Lihat bagian Migration Guide di setiap entri untuk panduan migrasi.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 1.0 | Versi awal changelog | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `M-06` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Versi Terkini** | `v<MAJOR.MINOR.PATCH>` |
| **Tanggal Release Terkini** | `<YYYY-MM-DD>` |
| **Dokumen terkait** | [D-02 Data Contract](../design/data-contract-spec.md) · [V-06 Data API](../development/data-api.md) · [V-05 Data Pipeline](../development/data-pipeline.md) · [DLV-01 Onboarding](../../delivery/consumer-onboarding-guide.md) |

---

## Kebijakan Change Management

| Tipe Perubahan | Klasifikasi | Notice Minimum | Notifikasi Channel |
|---|---|---|---|
| Hapus kolom / rename kolom | **`[BREAKING]`** | 90 hari | Email + `#dp-<product>-announce` |
| Ubah tipe data kolom | **`[BREAKING]`** | 90 hari | Email + `#dp-<product>-announce` |
| Hapus endpoint API / rename path | **`[BREAKING]`** | 90 hari | Email + `#dp-<product>-announce` |
| Ubah format nilai (enum, datetime) | **`[BREAKING]`** | 60 hari | Email + `#dp-<product>-announce` |
| Ubah SLA (lebih ketat) | **`[BREAKING]`** | 30 hari | Email + `#dp-<product>-announce` |
| Tambah kolom baru | `[ADDITIVE]` | 7 hari | `#dp-<product>-announce` |
| Tambah endpoint baru | `[ADDITIVE]` | 7 hari | `#dp-<product>-announce` |
| Perubahan data (fix konten) | `[DATA-FIX]` | Segera setelah deploy | `#dp-<product>-announce` |
| Bug fix teknis tanpa dampak consumer | `[PATCH]` | — | `#dp-<product>-announce` |
| Perbaikan dokumentasi | `[DOCS]` | — | — |

---

## Changelog

### [Unreleased]

> *Perubahan yang sudah diimplementasikan tapi belum di-release ke versi stabil.*

- `[ADDITIVE]` Tambah field `<nama_field_baru>` di endpoint `GET /v<N>/<resource>` — nilai berupa `<deskripsi>`

---

### v<MAJOR.MINOR.PATCH> — `<YYYY-MM-DD>`

**Ringkasan:** `<Deskripsi singkat release ini dalam satu kalimat.>`

#### Breaking Changes

:::danger Breaking Change — Action Required
**Berlaku:** `<YYYY-MM-DD>` (notice dikirim: `<YYYY-MM-DD>`)

**Perubahan:** `[Describe what changed]`

**Yang terdampak:** Consumer yang menggunakan `<field / endpoint / fitur yang dihapus/diubah>`

**Migration Guide:**
```sql
-- Sebelum (tidak lagi valid setelah YYYY-MM-DD)
SELECT <kolom_lama> FROM <schema>.<tabel>;

-- Sesudah (gunakan ini)
SELECT <kolom_baru> FROM <schema>.<tabel>;
```
:::

#### Additive Changes

- `[ADDITIVE]` Tambah kolom `<nama_kolom>` (`<tipe>`) di `<schema>.<tabel>` — `<deskripsi bisnis>`
- `[ADDITIVE]` Tambah endpoint `GET /v<N>/<resource>/<sub-resource>` — `<deskripsi>`

#### Data Fixes

- `[DATA-FIX]` Koreksi nilai `<field>` untuk record periode `<YYYY-MM-DD s.d. YYYY-MM-DD>` — sebelumnya `<nilai salah>`, kini `<nilai benar>`. Row count terdampak: `<N>`

#### Patches

- `[PATCH]` Fix memory leak di pipeline Bronze layer saat volume > 2M rows
- `[PATCH]` Perbaiki timezone handling di field `updated_at` (sebelumnya UTC, kini UTC+7 konsisten)

---

### v1.0.0 — `<YYYY-MM-DD>` (Initial Release)

**Ringkasan:** Release pertama data product ke production.

#### Features

- `[ADDITIVE]` SQL output port: `<schema>.v_<product>_daily` — view harian teragregasi
- `[ADDITIVE]` REST API output port: `GET /v1/<resource>` dengan cursor pagination
- `[ADDITIVE]` REST API output port: `GET /v1/<resource>/{id}` untuk lookup single record
- `[ADDITIVE]` File export: S3 path `s3://<bucket>/dp/<domain>/<product>/YYYY/MM/DD/`
- `[ADDITIVE]` Freshness SLO: data tersedia ≤ 1 jam setelah cut-off 23:59 WIB

---

## Riwayat Notifikasi Consumer

| Versi | Tipe | Tanggal Notif Dikirim | Channel | Consumer Konfirmasi |
|---|---|---|---|---|
| `v<N.N.N>` | `BREAKING` | `<YYYY-MM-DD>` | Email + Slack | `<N> dari <M> consumer` |
| `v<N.N.0>` | `ADDITIVE` | `<YYYY-MM-DD>` | Slack | — |

---

## Annex — Panduan Berkontribusi ke Changelog

Setiap Pull Request yang mengubah:
- Skema tabel (tambah/hapus/ubah kolom)
- Endpoint API (tambah/hapus/ubah path atau parameter)
- Business rules yang mempengaruhi output
- SLO atau SLA

**Wajib** menyertakan entri changelog di file ini sebagai bagian dari PR description.

**Format entri:**

```markdown
### [Unreleased]
- `[BREAKING|ADDITIVE|DATA-FIX|PATCH|DOCS]` <deskripsi singkat dan jelas>
  - Terdampak: <apa yang berubah bagi consumer>
  - Migration: <jika breaking — langkah migrasi>
```
