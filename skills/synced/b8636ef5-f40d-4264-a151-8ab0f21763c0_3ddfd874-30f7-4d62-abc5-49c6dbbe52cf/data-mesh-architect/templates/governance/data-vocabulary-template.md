---
title: "Kamus Data — <Nama Domain> — <Nama Atribut>"
sidebar_label: "Kamus: <Nama Domain>"
sidebar_position: 1
description: "Referensi kosakata data resmi untuk atribut <Nama Domain>. Mendefinisikan semua nilai enum yang valid beserta dasar regulasi masing-masing."
tags: [governance, data-vocabulary, enum, <nama-domain>]
document_id: "VOC-<DOMAIN>-<ATRIBUT>"
data_domain: "<Nama Domain>"
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
author: "<Nama Data Architect / Data Steward>"
review_status: "<Draft|Under Review|Approved>"
next_review_date: "<YYYY-MM-DD>"
---

# Kamus Data — Referensi Kosakata

> **Tujuan dokumen ini:** Mendefinisikan dan menstandarkan semua nilai enum yang valid untuk atribut data pada domain `<Nama Domain>`. Dokumen ini adalah otoritas tunggal yang dirujuk oleh semua data product yang mengonsumsi atau memproduksi atribut-atribut ini, dalam rangka menegakkan konsistensi semantik di seluruh ekosistem data (Federated Data Governance).

:::info Cara Menggunakan Dokumen Ini
Setiap entri kosakata mencakup: kode kanonik yang digunakan di database, nama tampilan untuk UI, definisi bisnis yang presisi, dan referensi regulasi yang menjadi landasan hukumnya. Untuk panduan lengkap tentang penambahan entri baru, lihat `references/data-vocabulary.md` bagian Prosedur Penambahan.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi Perubahan | Penulis | Reviewer |
|---|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` | `<Nama>` |

---

## Referensi Regulasi yang Berlaku

Daftar semua regulasi yang menjadi landasan definisi kosakata dalam dokumen ini:

| Kode Regulasi | Nama Lengkap | Pasal / Bagian yang Relevan | Lingkup |
|---|---|---|---|
| `<contoh: UU-24-2013>` | `<UU No. 24 Tahun 2013 tentang Administrasi Kependudukan>` | `<Pasal 58>` | `<Atribut yang diatur>` |
| `<contoh: PERMENDAGRI-109-2019>` | `<Permendagri No. 109 Tahun 2019>` | `<Lampiran Tabel Kode>` | `<Seluruh atribut kependudukan>` |
| `<contoh: UU-27-2022>` | `<UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi>` | `<Pasal 4>` | `<Klasifikasi sensitivitas data>` |

*Lihat daftar lengkap referensi di `references/data-vocabulary.md`.*

---

## Profil Domain

| Atribut | Nilai |
|---|---|
| **Nama Domain** | `<Nama Domain yang memiliki data ini>` |
| **Data Steward** | `<Nama, Email>` |
| **Data Architect** | `<Nama, Email>` |
| **Sistem Sumber Utama** | `<Nama sistem yang menjadi sumber asli data ini>` |
| **Frekuensi Perubahan Kosakata** | `<Sangat Jarang / Jarang / Sesekali>` |
| **Proses Perubahan** | `<Siapa yang berwenang mengubah? Melalui proses apa?>` |

---

## Entri Kosakata

*Gunakan pola berikut untuk setiap atribut bertipe enum dalam domain ini. Duplikasi seksi ini untuk setiap atribut.*

---

### `<NamaAtribut>`: `<Nama Tampilan Atribut>`

**Document ID:** `VOC-<DOMAIN>-<ATRIBUT>`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `<nama_kolom_di_tabel>` |
| **Nama Bisnis** | `<Nama yang digunakan tim bisnis>` |
| **Deskripsi** | `<Apa yang direpresentasikan atribut ini dalam konteks bisnis?>` |
| **Tipe Data** | `<VARCHAR(N) / BOOLEAN / SMALLINT / TEXT>` |
| **Custom Data Type** | `<Ya — nama type / Tidak>` |
| **Nullable** | `<Ya / Tidak>` — `<Alasan jika tidak nullable>` |
| **Masked (PII)** | `<Ya — aturan masking / Tidak>` |
| **Klasifikasi** | `<public / internal / restricted / confidential>` |
| **Kategori PII** | `<NULL / pii-umum / pii-sensitif-kesehatan / pii-sensitif-biometrik / ...>` |
| **Referensi Regulasi Utama** | `<Regulasi yang mendefinisikan nilai-nilai ini>` |
| **Sumber Otoritatif** | `<Sistem mana yang dianggap sebagai sumber kebenaran untuk atribut ini>` |
| **SCD Type** | `<0 / 1 / 2 — alasan>` |

#### Nilai yang Valid (Enum)

| Kode | Display Name | Definisi Bisnis | Referensi Regulasi | Catatan |
|---|---|---|---|---|
| `<kode-slug>` | `<Nama Tampilan>` | `<Definisi presisi dalam bahasa bisnis>` | `<Nomor UU/Permen + Pasal>` | `<Catatan tambahan jika ada>` |
| `<kode-slug-2>` | `<Nama Tampilan>` | `<Definisi>` | `<Referensi>` | |
| `NULL` | `<Nama Tampilan untuk NULL>` | `<Kapan NULL diizinkan dan apa artinya?>` | `<Referensi jika ada>` | Hanya jika `Nullable = Ya` |

#### Nilai yang Tidak Valid / Deprecated

Jika ada nilai yang pernah digunakan namun sekarang tidak valid, dokumentasikan di sini untuk mencegah confusi:

| Kode Lama | Alasan Deprecated | Pengganti | Deprecated Sejak |
|---|---|---|---|
| `<kode-lama>` | `<Alasan>` | `<kode-baru>` | `<YYYY-MM-DD>` |

#### Tabel Konversi

Jika sumber data menggunakan kode yang berbeda dari kode kanonik, dokumentasikan pemetaan di sini:

**Konversi dari `<Nama Sistem Sumber>` ke Kode Kanonik:**

| Kode Sumber | Nama Sumber | Kode Kanonik | Nama Kanonik | Catatan |
|---|---|---|---|---|
| `<kode-di-sistem-sumber>` | `<Nama di sistem sumber>` | `<kode-kanonik>` | `<Nama kanonik>` | |

#### Implementasi PostgreSQL

```sql
-- Constraint CHECK untuk membatasi nilai yang valid
-- Gunakan ini pada tabel yang menyimpan atribut ini
ALTER TABLE <schema>.<table_name>
    ADD CONSTRAINT chk_<nama_atribut>
    CHECK (<nama_kolom> IN (
        '<kode-1>',
        '<kode-2>',
        '<kode-3>'
        -- tambahkan semua kode valid
    ));

-- Jika nullable, tambahkan OR IS NULL:
-- CHECK (<nama_kolom> IN (...) OR <nama_kolom> IS NULL)

-- Lookup table untuk referensi (direkomendasikan untuk enum yang sering berubah)
CREATE TABLE ref_<nama_atribut> (
    kode            VARCHAR(50)     NOT NULL,
    display_name    VARCHAR(100)    NOT NULL,
    definisi        TEXT            NOT NULL,
    referensi       TEXT            NOT NULL,
    aktif           BOOLEAN         NOT NULL DEFAULT true,
    berlaku_sejak   DATE            NOT NULL,
    berlaku_sampai  DATE,           -- NULL = masih berlaku

    CONSTRAINT pk_ref_<nama_atribut> PRIMARY KEY (kode)
);

-- Populate dengan nilai-nilai yang valid
INSERT INTO ref_<nama_atribut> (kode, display_name, definisi, referensi, berlaku_sejak)
VALUES
    ('<kode-1>', '<display-1>', '<definisi-1>', '<regulasi-1>', '<YYYY-MM-DD>'),
    ('<kode-2>', '<display-2>', '<definisi-2>', '<regulasi-2>', '<YYYY-MM-DD>');
```

---

*(Duplikasi seksi di atas untuk setiap atribut enum dalam domain ini)*

---

## Panduan Penambahan Kosakata Baru

:::note Kapan Membuat Entri Baru
Buat entri baru hanya ketika: (1) ada regulasi atau standar yang mendefinisikan nilai tersebut dan belum ada padanannya, atau (2) tim bisnis memerlukan nilai baru yang tidak terdapat dalam standar manapun dan telah mendapat persetujuan formal Data Steward.
:::

**Langkah-langkah:**

1. Cari terlebih dahulu apakah nilai tersebut sudah terdefinisi di `references/data-vocabulary.md` (Kosakata Universal) atau di dokumen ini.
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

- Kosakata Universal: `../references/data-vocabulary.md`
- Data Catalog: `../design/data-catalog.md`
- Data Contract: `../design/data-contract-spec.md`
- Risk Assessment (PII): `../design/risk-assessment.md`
