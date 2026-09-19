---
title: "Analytical Report — <Judul Laporan>"
sidebar_label: "Analytical Report"
sidebar_position: 11
description: "Template laporan analitik terstruktur: metodologi, temuan, visualisasi, insight, dan rekomendasi berbasis data."
tags: [development, analytics, report, insights, recommendation]
doc_id: "V-11"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Analytical Report: `<Judul Laporan>`

> **Tujuan dokumen ini:** Menyampaikan temuan analisis berbasis data dengan metodologi yang transparan, visualisasi yang mendukung, dan rekomendasi yang actionable bagi pengambil keputusan.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 1.0 | Laporan final | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `V-11` |
| **Domain** | `<Nama Domain>` |
| **Periode Analisis** | `<YYYY-MM-DD s.d. YYYY-MM-DD>` |
| **Tanggal Laporan** | `<YYYY-MM-DD>` |
| **Analyst** | `<Nama, Email>` |
| **Requester** | `<Nama, Tim>` |
| **Audience** | `<Management / Operasional / Regulasi>` |
| **Dokumen terkait** | [D-04 Data Catalog](../design/data-catalog.md) · [D-13 Metrics Catalog](../monitoring/metrics-catalog.md) · [G-03 Data Dictionary](../../governance/data-dictionary.md) |

---

## 1. Executive Summary

> `[3–5 kalimat: Apa pertanyaan utama yang dijawab? Apa temuan paling penting? Apa rekomendasi utama?]`

**Temuan Kunci:**
- `<Temuan 1 — dengan angka/metrik spesifik>`
- `<Temuan 2>`
- `<Temuan 3>`

**Rekomendasi Utama:** `<1 kalimat rekomendasi yang paling penting>`

---

## 2. Latar Belakang dan Pertanyaan Analisis

### 2.1 Konteks Bisnis

> `[Jelaskan konteks: mengapa analisis ini diperlukan, keputusan bisnis apa yang akan dipengaruhi, dan siapa yang akan menggunakan hasil ini.]`

### 2.2 Pertanyaan Analisis

| # | Pertanyaan | Prioritas |
|---|---|---|
| Q1 | `<Pertanyaan utama yang dijawab analisis ini>` | Tinggi |
| Q2 | `<Pertanyaan pendukung>` | Sedang |
| Q3 | `<Pertanyaan eksploratori>` | Rendah |

---

## 3. Metodologi

### 3.1 Data yang Digunakan

| Dataset | Periode | Rows | Sumber | Catatan |
|---|---|---|---|---|
| `<schema>.v_<product>_daily` | `<periode>` | `<N>` | Data Product | Data final post-cleaning |
| `<sumber referensi>` | `<periode>` | `<N>` | `<sumber>` | Untuk benchmarking |

### 3.2 Metode Analisis

| Teknik | Tujuan | Tools |
|---|---|---|
| `<Deskriptif statistik>` | Memahami distribusi data | Python pandas, SQL |
| `<Trend analysis>` | Identifikasi pola temporal | Python matplotlib |
| `<Segmentasi>` | Pengelompokan berdasarkan `<dimensi>` | SQL GROUP BY |
| `<Korelasi>` | Hubungan antar variabel | Python scipy |

### 3.3 Asumsi dan Keterbatasan

:::warning Keterbatasan Analisis
- `<Asumsi 1 — contoh: data diasumsikan lengkap untuk periode yang dianalisis>`
- `<Asumsi 2>`
- `<Keterbatasan: data tidak mencakup X sehingga insight tentang Y mungkin tidak lengkap>`
:::

---

## 4. Temuan

### 4.1 Temuan 1 — `<Judul Temuan>`

> `[Deskripsikan temuan dengan data konkret. Selalu sertakan angka, persentase, atau metrik spesifik.]`

**Data pendukung:**

```sql
-- Query yang menghasilkan temuan ini
SELECT
    <dimensi>,
    COUNT(*)              AS jumlah,
    SUM(<metrik>)         AS total,
    AVG(<metrik>)         AS rata_rata
FROM <schema>.v_<product>_daily
WHERE <filter>
GROUP BY 1
ORDER BY 3 DESC;
```

| `<Dimensi>` | Jumlah | Total | % dari Total |
|---|---|---|---|
| `<nilai_1>` | `<N>` | `<N>` | `<X>%` |
| `<nilai_2>` | `<N>` | `<N>` | `<X>%` |

### 4.2 Temuan 2 — `<Judul Temuan>`

> `[Temuan berikutnya dengan format serupa]`

---

## 5. Insight dan Interpretasi

> `[Section ini berisi INTERPRETASI analyst — "apa artinya" dari temuan-temuan di atas dalam konteks bisnis. Bukan sekadar mengulang angka.]`

| Temuan | Interpretasi Bisnis | Implikasi |
|---|---|---|
| `<Temuan 1>` | `<Apa artinya secara bisnis>` | `<Apa yang perlu dilakukan / diperhatikan>` |
| `<Temuan 2>` | `<Interpretasi>` | `<Implikasi>` |

---

## 6. Rekomendasi

| # | Rekomendasi | Prioritas | Owner | Deadline | KPI Sukses |
|---|---|---|---|---|---|
| R-01 | `<Rekomendasi spesifik dan actionable>` | Tinggi | `<Tim/Role>` | `<YYYY-MM-DD>` | `<Metrik yang berubah>` |
| R-02 | `<Rekomendasi>` | Sedang | `<Tim/Role>` | `<YYYY-MM-DD>` | `<Metrik>` |

---

## 7. Analisis Lanjutan yang Disarankan

- `<Pertanyaan yang belum terjawab dan layak dianalisis lebih lanjut>`
- `<Data tambahan yang jika tersedia akan memperkuat/memperbaiki analisis ini>`

---

## Annex A — Query Lengkap

`[Lampirkan semua query yang digunakan dalam analisis ini untuk reproducibility]`

```sql
-- Query 1: <deskripsi>
<query lengkap>

-- Query 2: <deskripsi>
<query lengkap>
```
