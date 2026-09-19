---
title: "Dashboard Design — <Nama Data Product>"
sidebar_label: "Dashboard Design"
sidebar_position: 11
description: "Spesifikasi desain dashboard dan visualisasi data untuk data product"
tags: [design, dashboard, visualization, ux]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: design
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Dashboard Design Document

> **Tujuan dokumen ini:** Mendefinisikan spesifikasi lengkap dashboard dan visualisasi yang akan dibangun sebagai consumer-aligned output port dari data product. Dokumen ini menjadi panduan bagi Data Analyst dan Frontend Developer.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## 1. Overview Dashboard

| Atribut | Detail |
|---|---|
| **Nama Dashboard** | `<Nama Dashboard>` |
| **Platform** | `<Apache Superset / Metabase / Grafana / Apache Superset / Apache Superset>` |
| **Target Pengguna** | `<Contoh: Manajer Program, Analis Data, Eksekutif>` |
| **Frekuensi Refresh** | `<Real-time / 15 menit / Harian>` |
| **Akses** | `<Internal only / Public / Role-based>` |
| **Sumber Data** | `<schema.table_name atau view_name>` |
| **Link Prototype** | `<https://figma.com/... atau https://dashboard.domain.org/...>` |

**Tujuan dashboard ini:**
> `[Apa pertanyaan bisnis utama yang dijawab dashboard ini? Siapa yang akan menggunakan dan untuk keputusan apa?]`

---

## 2. Struktur Halaman & Layout

### 2.1 Daftar Halaman/Tab

| # | Nama Halaman | Audience | Konten Utama |
|---|---|---|---|
| 1 | `<Overview / Ringkasan>` | `<Semua pengguna>` | `<KPI utama, ringkasan status>` |
| 2 | `<Detail Operasional>` | `<Operator / Manajer>` | `<Tabel detail, filter, drill-down>` |
| 3 | `<Analitik & Tren>` | `<Analis Data>` | `<Time series, distribusi, perbandingan>` |
| 4 | `<Eksekutif View>` | `<Pimpinan>` | `<High-level KPI, summary>` |

### 2.2 Global Filters

Filter yang berlaku di semua halaman:

| Filter | Tipe | Default | Opsi |
|---|---|---|---|
| `<Periode Waktu>` | `<Date Range>` | `<30 hari terakhir>` | `<7 hari / 30 hari / YTD / Custom>` |
| `<Wilayah / Region>` | `<Multi-select>` | `<Semua>` | `<List wilayah>` |
| `<Kategori>` | `<Single-select>` | `<Semua>` | `<List kategori>` |

---

## 3. Spesifikasi Komponen per Halaman

### Halaman 1: `<Overview / Ringkasan>`

#### KPI Cards (Row 1)

| KPI | Metrik | Format | Warna Threshold | Sumber |
|---|---|---|---|---|
| `<Total Aktif>` | `<COUNT WHERE status='aktif'>` | `<Integer, ribuan-separator>` | `<Baik >90% / Sedang 70-90% / Kritis <70%>` | `<schema.dim_entitas>` |
| `<Pertumbuhan MoM>` | `<(bulan_ini - bulan_lalu) / bulan_lalu>` | `<%, +/- arrow>` | `<Baik Positif / Kritis Negatif>` | `<schema.fact_summary>` |
| `<% Target Tercapai>` | `<aktual / target>` | `<%, progress bar>` | `<Baik >80% / Sedang 60-80% / Kritis <60%>` | `<schema.fact_target>` |
| `<Total Nilai>` | `<SUM(nilai)>` | `<IDR, miliar>` | `<Netral>` | `<schema.fact_transaksi>` |

#### Chart 1: Tren Waktu (Row 2 — Full width)

| Atribut | Detail |
|---|---|
| **Tipe** | `<Line chart>` |
| **Judul** | `<"Tren [Metrik] per Bulan">` |
| **X-axis** | `<Bulan (monthly granularity)>` |
| **Y-axis** | `<Jumlah / Nilai>` |
| **Series** | `<Actual vs Target (dua garis)>` |
| **Tooltip** | `<Nilai, % perubahan dari periode sebelumnya>` |
| **Query** | `<SELECT DATE_TRUNC('month', tanggal), COUNT(*) FROM ... GROUP BY 1>` |

#### Chart 2 & 3: Distribusi (Row 3 — 50/50)

| Atribut | Chart 2 | Chart 3 |
|---|---|---|
| **Tipe** | `<Bar chart horizontal>` | `<Pie / Donut chart>` |
| **Judul** | `<"Top 10 [Kategori] berdasarkan Volume">` | `<"Distribusi per [Status]">` |
| **Data** | `<Aggregasi per kategori>` | `<Distribusi status>` |
| **Catatan** | `<Klik untuk drill-down>` | `<Legend di kanan>` |

---

### Halaman 2: `<Detail Operasional>`

#### Tabel Detail (Full page)

| Atribut | Detail |
|---|---|
| **Tipe** | `<Data Table dengan pagination>` |
| **Kolom yang Ditampilkan** | `<id, kode, nama*, status, tanggal, jumlah>` |
| **Kolom PII** | `<nama: tampilkan masked (3 huruf + ***) / hanya untuk role authorized>` |
| **Sort Default** | `<updated_at DESC>` |
| **Pagination** | `<50 rows per page>` |
| **Export** | `<CSV (tanpa kolom PII untuk non-privileged role)>` |
| **Search** | `<Full-text search pada kode, nama>` |

**Filter tambahan halaman ini:**
- Status: Multi-select dropdown
- Rentang tanggal: Date range picker
- Kolom kustom: Sesuai kebutuhan pengguna

---

## 4. Spesifikasi Teknis

### 4.1 Query Optimization

```sql
-- Contoh query untuk Chart 1 (tren bulanan)
-- HARUS menggunakan materialized view / pre-aggregated table untuk performa
SELECT 
    DATE_TRUNC('month', tanggal) AS bulan,
    COUNT(*) AS total,
    SUM(jumlah) AS total_jumlah,
    SUM(nilai) AS total_nilai
FROM <schema.fact_transaksi>
WHERE 
    tanggal >= :start_date 
    AND tanggal <= :end_date
    -- Filter yang diterapkan dari global filter:
    AND (wilayah = :wilayah OR :wilayah = 'SEMUA')
GROUP BY 1
ORDER BY 1;

-- CATATAN: Jika query ini > 2 detik, buat materialized view:
-- CREATE MATERIALIZED VIEW mv_monthly_summary AS ...
-- REFRESH MATERIALIZED VIEW CONCURRENTLY mv_monthly_summary;
```

### 4.2 Performance Requirements

| Komponen | Target Load Time | Strategi |
|---|---|---|
| KPI Cards | `< 1 detik` | `Pre-aggregated table, cache 5 menit` |
| Charts | `< 2 detik` | `Materialized views, cache 15 menit` |
| Detail Table | `< 3 detik` | `Index pada filter columns, pagination` |
| Export CSV | `< 30 detik` | `Async export, email/download link` |

### 4.3 Access Control di Dashboard

| Role | Halaman | Kolom PII | Export |
|---|---|---|---|
| `<Executive>` | `<Overview, Analitik>` | `<Tidak tampil>` | `<Tidak>` |
| `<Manager>` | `<Semua>` | `<Masked>` | `<Ya, tanpa PII>` |
| `<Analyst>` | `<Semua>` | `<Full (authorized)>` | `<Ya, semua kolom>` |
| `<Public>` | `<Overview saja>` | `<Tidak tampil>` | `<Tidak>` |

---

## 5. Mockup & Wireframe

`[Opsional — sertakan screenshot Figma atau ASCII wireframe]`

```
┌─────────────────────────────────────────────────────────────────┐
│  <Nama Dashboard>                    Filter: [30 hari ▼] [All ▼] │
├─────────────┬─────────────┬─────────────┬─────────────────────────┤
│  Total Aktif│  MoM Growth │  % Target   │   Total Nilai            │
│   125.430   │   +5.2% ↑  │   87% Baik    │   Rp 2.3 Miliar         │
├─────────────┴─────────────┴─────────────┴─────────────────────────┤
│  Tren Bulanan ─────────────────────────────────────────────────   │
│  [Line Chart: Actual vs Target, Jan-Des 2024]                     │
├──────────────────────────────────┬──────────────────────────────── │
│  Top 10 Kategori                 │  Distribusi Status              │
│  [Horizontal Bar Chart]          │  [Donut Chart]                  │
└──────────────────────────────────┴──────────────────────────────── ┘
```

---

## 6. Sign-Off

| Role | Nama | Persetujuan | Tanggal |
|---|---|---|---|
| Data Product Owner | `<Nama>` | `☐ Approved` | |
| Data Analyst (builder) | `<Nama>` | `☐ Acknowledged` | |
| Consumer Representative | `<Nama>` | `☐ Approved` | |
