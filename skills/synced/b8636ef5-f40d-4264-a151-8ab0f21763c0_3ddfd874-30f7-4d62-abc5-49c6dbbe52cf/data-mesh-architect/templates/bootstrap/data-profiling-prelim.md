---
title: "Preliminary Data Profiling Report — <Nama Data Product>"
sidebar_label: "Data Profiling (Preliminary)"
sidebar_position: 4
description: "Laporan profiling data awal untuk menilai kualitas dan karakteristik sumber data"
tags: [bootstrap, data-profiling, data-quality]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: bootstrap
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Preliminary Data Profiling Report

> **Tujuan dokumen ini:** Menilai karakteristik, kualitas, dan kesiapan sumber data **sebelum** desain pipeline dimulai. Laporan ini menjadi input kritis bagi Data Quality Design, Infrastructure Brief, dan Data Contract.

:::warning
Ini adalah laporan **preliminary** (awal). Profiling mendalam dilakukan saat fase Development. Dokumen ini cukup untuk menjawab: *"Apakah sumber data cukup layak untuk dibangun data product-nya?"*
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Profiling awal | `<Nama>` |

---

## Definisi Umum

| Atribut | Nilai |
|---|---|
| **Data Product** | `<Nama Data Product>` |
| **Domain** | `<Nama Domain>` |
| **Tanggal Profiling** | `<YYYY-MM-DD>` |
| **Profiler** | `<Nama Data Engineer / Data Analyst>` |
| **Environment** | `<Dev / Staging / Produksi (read-only)>` |
| **Tools yang Digunakan** | `<Great Expectations / pandas-profiling / SQL manual / Soda>` |

---

## 1. Inventori Sumber Data

`[Mandatory]`

### 1.1 Daftar Sumber yang Diprofile

| ID | Sistem Sumber | Tabel/Endpoint/Topik | Tipe | Jumlah Record (Sample) | Rentang Tanggal Data |
|---|---|---|---|---|---|
| SRC-01 | `<Nama sistem>` | `<nama_tabel / /api/resource>` | `<DB/API/File/Stream>` | `<~X juta>` | `<YYYY-MM-DD s.d. YYYY-MM-DD>` |
| SRC-02 | | | | | |

### 1.2 Akses & Koneksi

| Sumber | Status Akses | Metode Koneksi | Catatan |
|---|---|---|---|
| SRC-01 | `<[x] Berhasil / [!] Terbatas / [ ] Belum>` | `<Direct DB / API key / Sample file>` | `<Catatan kendala>` |

---

## 2. Profil per Tabel / Dataset

*Duplikasi seksi ini untuk setiap sumber data.*

---

### Dataset: `<nama_tabel_atau_endpoint>` (SRC-01)

#### 2.1 Ringkasan Dataset

| Atribut | Nilai |
|---|---|
| **Nama Lengkap** | `<schema.table_name atau /api/v1/resource>` |
| **Jumlah Row (sample)** | `<~X.XXX.XXX>` |
| **Jumlah Kolom** | `<X>` |
| **Ukuran Estimasi** | `<X GB>` |
| **Tanggal Data Terlama** | `<YYYY-MM-DD>` |
| **Tanggal Data Terbaru** | `<YYYY-MM-DD>` |
| **Frekuensi Update** | `<Real-time / Setiap X menit / Harian / Mingguan>` |

#### 2.2 Profil Kolom

| Kolom | Tipe Data | % Non-Null | Kardinalitas | Min | Max | Contoh Value | Anomali Terdeteksi |
|---|---|---|---|---|---|---|---|
| `<nama_kolom>` | `<VARCHAR/INT/DATE>` | `<98.5%>` | `<Unique/High/Low>` | `<->` | `<->` | `<contoh>` | `<None / Deskripsi masalah>` |
| | | | | | | | |

#### 2.3 Dimensi Kualitas Data (Preliminary Assessment)

| Dimensi | Skor Awal | Temuan | Rekomendasi |
|---|---|---|---|
| **Completeness** | `<Baik Baik / Sedang Sedang / Kritis Buruk>` | `<% null per kolom kritis>` | `<Apa yang perlu dilakukan>` |
| **Uniqueness** | `<Baik/Sedang/Kritis>` | `<% duplikat pada PK>` | |
| **Validity** | `<Baik/Sedang/Kritis>` | `<Format yang salah, range di luar batas>` | |
| **Consistency** | `<Baik/Sedang/Kritis>` | `<Inkonsistensi dengan sumber lain>` | |
| **Accuracy** | `<Baik/Sedang/Kritis>` | `<Nilai yang mencurigakan / tidak masuk akal>` | |
| **Timeliness** | `<Baik/Sedang/Kritis>` | `<Keterlambatan update data>` | |

**Keterangan skor:** Baik Baik (>95%) | Sedang Sedang (80-95%) | Kritis Buruk (<80%)

#### 2.4 Temuan Kritis (Jika Ada)

:::danger Temuan Kritis
Daftar masalah yang **harus** diselesaikan sebelum data product bisa dibangun:
- `[Isi jika ada — contoh: "30% NIK kosong di tabel X"]`
:::

:::warning Temuan Minor
Daftar masalah yang perlu ditangani dalam Quality Design:
- `[Isi jika ada — contoh: "Format tanggal tidak konsisten (YYYY-MM-DD vs DD/MM/YYYY)"]`
:::

---

## 3. Distribusi & Statistik Ringkas

`[Opsional tapi sangat direkomendasikan]`

### 3.1 Distribusi Volume Data Over Time

```
[Jika tersedia, tempelkan grafik atau tabel distribusi data per periode]
Contoh format tabel:

| Bulan | Jumlah Record Baru | % Change |
|---|---|---|
| 2024-01 | 1.234.567 | - |
| 2024-02 | 1.345.678 | +9.0% |
```

### 3.2 Kolom Kritis — Distribusi Nilai

`[Isi untuk kolom-kolom yang menjadi kunci bisnis atau sering digunakan dalam filter]`

| Kolom | Top 5 Nilai | Frekuensi | Catatan |
|---|---|---|---|
| `<nama_kolom>` | `<value1>` | `<X%>` | |

---

## 4. Pemetaan Sumber → Target

`[Mandatory]` — *Role: Data Engineer*

Hasil preliminary mapping sumber ke kolom target data product:

| Target Field | Tipe Target | Sumber | Source Field | Transformasi Diperlukan | Confidence |
|---|---|---|---|---|---|
| `<target_field>` | `<VARCHAR>` | `<SRC-01>` | `<source_field>` | `<TRIM, UPPER, format date>` | `<Baik Tinggi / Sedang Sedang / Kritis Rendah>` |
| | | | | | |

**Kolom Target yang Belum Ada Sumbernya:**

| Target Field | Status | Solusi Potensial |
|---|---|---|
| `<field_name>` | `<Tidak ada di sumber>` | `<Derive dari kolom X / Butuh sumber tambahan / Default value>` |

---

## 5. Identifikasi Data Pribadi (PII Scan)

`[Mandatory jika ada indikasi PII]`

| Kolom | Sumber | Kemungkinan PII | Kategori | Rekomendasi Penanganan |
|---|---|---|---|---|
| `<nama>` | `<SRC-01.tabel_x>` | `<Tinggi>` | `<PII Umum (Nama)>` | `<Pseudonymize / Mask>` |
| `<nik>` | `<SRC-01.tabel_x>` | `<Tinggi>` | `<PII Umum (Identitas)>` | `<Dynamic masking>` |
| `<diagnosa>` | `<SRC-02.tabel_y>` | `<Tinggi>` | `<PII Spesifik (Kesehatan)>` | `<Encrypt + strict RBAC>` |
| | | | | |

---

## 6. Penilaian Risiko Data

`[Mandatory]`

| Risiko | Probabilitas | Dampak | Tindak Lanjut |
|---|---|---|---|
| `<Sumber tidak stabil/sering down>` | `<Tinggi/Sedang/Rendah>` | `<Tinggi/Sedang/Rendah>` | `<Buat SLA agreement dengan tim sumber>` |
| `<Kualitas data buruk di kolom kritis>` | | | |
| `<Volume tumbuh lebih cepat dari estimasi>` | | | |
| `<Perubahan skema sumber tanpa notifikasi>` | | | |

---

## 7. Kesimpulan & Go/No-Go Recommendation

`[Mandatory]`

### 7.1 Overall Data Readiness Score

| Kategori | Skor | Keterangan |
|---|---|---|
| **Kelengkapan Sumber** | `<Baik/Sedang/Kritis>` | `<Semua sumber yang dibutuhkan tersedia?>` |
| **Kualitas Data** | `<Baik/Sedang/Kritis>` | `<Kualitas cukup untuk memenuhi SLO target?>` |
| **Aksesibilitas** | `<Baik/Sedang/Kritis>` | `<Akses teknis dan agreement sudah ada?>` |
| **Privasi & Kepatuhan** | `<Baik/Sedang/Kritis>` | `<Risiko privasi teridentifikasi dan bisa dimitigasi?>` |
| **Skalabilitas** | `<Baik/Sedang/Kritis>` | `<Volume dan growth rate masuk akal untuk infra yang direncanakan?>` |

### 7.2 Rekomendasi

`[ ] [x] GO` — Lanjutkan ke fase Design. Sumber data cukup siap.

`[ ] [!] GO WITH CONDITIONS` — Lanjutkan ke Design dengan syarat:
- `<Syarat 1>`
- `<Syarat 2>`

`[ ] [ ] NO-GO` — Profiling menemukan hambatan fundamental:
- `<Hambatan 1>`
- Diperlukan: `<Tindakan remedial sebelum bisa dilanjutkan>`

### 7.3 Tindak Lanjut

| Aksi | Owner | Due Date |
|---|---|---|
| `<Resolve critical finding X>` | `<Nama>` | `<Tanggal>` |
| `<Negotiate data access agreement>` | `<Nama>` | `<Tanggal>` |
| `<Request additional sample data>` | `<Nama>` | `<Tanggal>` |
