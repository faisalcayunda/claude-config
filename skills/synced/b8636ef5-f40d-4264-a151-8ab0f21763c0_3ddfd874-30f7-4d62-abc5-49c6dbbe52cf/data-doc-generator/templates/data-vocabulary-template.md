---
title: Kamus Data — {SCHEMA_TABLE_NAME}
sidebar_label: G-01 Vocabulary
sidebar_position: 1
description: Referensi kosakata data resmi untuk tabel {SCHEMA_TABLE_NAME}. Mendefinisikan semua nilai enum yang valid dan aturan validasi field beserta dasar regulasi masing-masing.
tags:
  - governance
  - data-vocabulary
  - enum
  - {DOMAIN_SLUG}
doc_id: {DOC_ID}
doc_title: Kamus Data — {SCHEMA_TABLE_NAME}
data_product_id: {DATA_PRODUCT_ID}
version: 0.1.0
date: '{CURRENT_DATE}'
last_updated: '{CURRENT_DATE}'
author: ''
owner: ''
classification: {CLASSIFICATION}
pii_flag: {PII_FLAG}
---

# Kamus Data — Referensi Kosakata — `{SCHEMA_TABLE_NAME}`

> **Tujuan dokumen ini:** Mendefinisikan dan menstandarkan semua nilai enum yang valid serta aturan validasi untuk setiap field dalam tabel `{SCHEMA_TABLE_NAME}`. Dokumen ini adalah otoritas tunggal yang mendefinisikan *nilai yang valid* untuk setiap atribut. Aturan tentang keberadaan (NOT NULL) dan keunikan (UNIQUE constraint) ada di Data Dictionary tabel yang sama.

:::info

Cara Menggunakan Dokumen Ini
Setiap entri kosakata mencakup: kode kanonik yang digunakan di database, nama tampilan untuk UI, definisi bisnis yang presisi, aturan validasi atau enum values, dan referensi regulasi yang menjadi landasan hukumnya. Untuk panduan lengkap tentang penambahan entri baru, lihat seksi Panduan Penambahan Kosakata Baru di bawah.

:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi Perubahan | Penulis |
|---|---|---|---|
| `{CURRENT_DATE}` | 0.1.0 | Initial draft | |

---

{REGULATORY_REFERENCES_SECTION}

{DOMAIN_PROFILE_SECTION}

## Entri Kosakata

> Dokumen ini mencakup **semua field** dari tabel `{SCHEMA_TABLE_NAME}`. Setiap field memiliki salah satu dari: (a) daftar enum values untuk field kategorikal, atau (b) aturan validasi untuk field non-kategorikal.

{VOCABULARY_ENTRIES}

---

## Panduan Penambahan Kosakata Baru

:::note

Kapan Membuat Entri Baru
Buat entri baru hanya ketika: (1) ada regulasi atau standar yang mendefinisikan nilai tersebut dan belum ada padanannya, atau (2) tim bisnis memerlukan nilai baru yang tidak terdapat dalam standar manapun dan telah mendapat persetujuan formal Data Steward.

:::

**Langkah-langkah:**

1. Cari terlebih dahulu apakah nilai tersebut sudah terdefinisi di kosakata universal atau di dokumen ini.
2. Identifikasi regulasi atau standar yang menjadi landasan nilai baru tersebut. Jika tidak ada, dokumentasikan alasan bisnis yang kuat.
3. Buat Pull Request ke file ini dengan format entri yang lengkap.
4. Minta review dari Data Steward domain dan Data Architect.
5. Setelah disetujui, update tabel konversi jika relevan, dan update Data Catalog.
6. Jika penambahan nilai baru berdampak pada data contract yang sudah ada (consumer sudah pakai field ini), tentukan apakah ini breaking change atau non-breaking.

---

## Riwayat Review

| Tanggal Review | Reviewer | Keputusan | Catatan |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<Nama>` | `<Approved / Rejected / Revision Needed>` | `<Catatan reviewer>` |

---

## Referensi Silang

- Data Dictionary tabel ini: `./{TABLE_NAME}_dictionary.md`
- Data Catalog: `/{DOMAIN_SLUG}/{PRODUCT_SLUG}/design/data-catalog.md`
- Data Contract: `/{DOMAIN_SLUG}/{PRODUCT_SLUG}/design/data-contract-spec.md`
- Risk Assessment (PII): `/{DOMAIN_SLUG}/{PRODUCT_SLUG}/design/risk-assessment.md`
