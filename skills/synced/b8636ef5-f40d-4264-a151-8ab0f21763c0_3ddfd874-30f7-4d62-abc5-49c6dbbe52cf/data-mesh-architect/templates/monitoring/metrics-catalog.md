---
title: "Data Product Metrics & Insights Catalog — <Nama Data Product>"
sidebar_label: "Metrics Catalog"
sidebar_position: 1
description: "Katalog lengkap metrik, KPI, dan insights yang dapat dihasilkan dari data product ini"
tags: [monitoring, metrics, kpi, insights]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: monitoring
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Product Metrics & Insights Catalog

> **Tujuan dokumen ini:** Mendokumentasikan semua metrik bisnis, operasional, dan teknis yang dapat dihasilkan dari data product ini. Dokumen ini menjadi panduan bagi Data Analyst dan consumer untuk memaksimalkan nilai data product.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## 1. Metrik Bisnis

`[Mandatory]` — *Role: Data Analyst + DPO*

### 1.1 KPI Utama (North Star Metrics)

| Metrik | Definisi | Formula / Query | Granularitas | Update Frequency |
|---|---|---|---|---|
| `<Nama KPI>` | `<Definisi bisnis KPI ini>` | `<COUNT(*) / SUM(nilai) / dsb.>` | `<Harian / Mingguan / Bulanan>` | `<Real-time / Harian>` |
| | | | | |

### 1.2 Metrik Operasional

| Metrik | Definisi | Dimensi Analisis | Contoh Insight |
|---|---|---|---|
| `<Volume aktivitas>` | `<Jumlah transaksi/kejadian per periode>` | `<Per hari, per wilayah, per kategori>` | `<"Terjadi penurunan 20% pada Maret — investigasi cause">` |
| `<Tingkat keberhasilan>` | `<% aktivitas yang selesai/berhasil>` | `<Per tipe, per wilayah>` | `<"Wilayah X memiliki tingkat gagal tertinggi">` |
| `<Pertumbuhan MoM>` | `<Perubahan volume dari bulan sebelumnya>` | `<Per segmen>` | `<"Growth melambat di Q3">` |

### 1.3 Metrik Dampak (Impact Metrics)

| Metrik | Bagaimana Mengukurnya | Baseline | Target |
|---|---|---|---|
| `<Efisiensi proses>` | `<Waktu rata-rata penyelesaian proses>` | `<X hari (sebelum data product)>` | `<Y hari (target)>` |
| `<Cakupan program>` | `<% target terlayani>` | `<X%>` | `<Y%>` |

---

## 2. Metrik Kualitas Data Product

`[Mandatory]` — *Role: Data Steward*

### 2.1 SLO Health Dashboard

| Metrik | SLO | Cara Ukur | Dashboard Link |
|---|---|---|---|
| **Freshness** | `<< 25 jam>` | `<CURRENT_TIMESTAMP - MAX(updated_at)>` | `<Link>` |
| **Availability** | `<99.9%>` | `<Uptime monitoring>` | `<Link>` |
| **Completeness** | `<>99.5%>` | `<% non-null kolom mandatory>` | `<Link>` |
| **Uniqueness** | `<100%>` | `<Duplikat count>` | `<Link>` |
| **Error Budget** | `<Remaining %>` | `<1 - (SLO breaches / total checks)>` | `<Link>` |

### 2.2 Consumer Adoption Metrics

| Metrik | Cara Ukur | Target |
|---|---|---|
| `<Jumlah consumer aktif>` | `<COUNT DISTINCT consumer_id per bulan>` | `<>X tim aktif dalam 3 bulan>` |
| `<Query frequency>` | `<Total queries per hari>` | `<>X queries/hari>` |
| `<Consumer satisfaction>` | `<NPS survey bulanan>` | `<NPS > X>` |

---

## 3. Pertanyaan Bisnis yang Dapat Dijawab

`[Mandatory]` — *Role: DPO + Data Analyst*

Daftar pertanyaan analitik yang dapat dijawab menggunakan data product ini, beserta query referensi:

### Pertanyaan 1: `<Contoh: "Berapa total volume aktivitas per wilayah bulan ini?"`

```sql
-- Query referensi (run di Gold layer)
SELECT 
    wilayah,
    COUNT(*) as total_aktivitas,
    SUM(nilai) as total_nilai,
    DATE_TRUNC('month', tanggal) as bulan
FROM <schema>.<gold_table>
WHERE 
    tanggal >= DATE_TRUNC('month', CURRENT_DATE)
    AND status = 'aktif'
GROUP BY 1, 4
ORDER BY 2 DESC;
```

**Visualisasi yang direkomendasikan:** Bar chart horizontal, breakdown per wilayah

---

### Pertanyaan 2: `<Contoh: "Bagaimana tren pertumbuhan month-over-month?"`

```sql
WITH monthly_volume AS (
    SELECT 
        DATE_TRUNC('month', tanggal) as bulan,
        COUNT(*) as volume_bulan_ini
    FROM <schema>.<gold_table>
    GROUP BY 1
),
growth AS (
    SELECT 
        bulan,
        volume_bulan_ini,
        LAG(volume_bulan_ini) OVER (ORDER BY bulan) as volume_bulan_lalu,
        ROUND(
            (volume_bulan_ini - LAG(volume_bulan_ini) OVER (ORDER BY bulan)) 
            / NULLIF(LAG(volume_bulan_ini) OVER (ORDER BY bulan), 0) * 100, 2
        ) as growth_pct
    FROM monthly_volume
)
SELECT * FROM growth ORDER BY bulan;
```

---

### Pertanyaan 3: `<Tambahkan pertanyaan lainnya sesuai use case>`

*(Tambahkan pertanyaan dan query referensi sesuai kebutuhan bisnis)*

---

## 4. Segmentasi & Dimensi Analisis

`[Mandatory]` — *Role: Data Analyst*

| Dimensi | Field | Nilai Unik (Est.) | Keterangan |
|---|---|---|---|
| `<Wilayah/Geografi>` | `<wilayah, provinsi, kabupaten>` | `<38 provinsi, ~514 kabupaten>` | `<Gunakan untuk analisis regional>` |
| `<Waktu>` | `<tanggal, bulan, tahun, kuartal>` | `<N/A>` | `<Granularitas harian, mingguan, bulanan>` |
| `<Kategori>` | `<kategori, sub_kategori>` | `<X kategori>` | `<Klasifikasi bisnis utama>` |
| `<Status>` | `<status>` | `<3: aktif, nonaktif, pending>` | `<Lifecycle status>` |
