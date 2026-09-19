---
title: "Dashboard Development — <Nama Dashboard>"
sidebar_label: "Dashboard Development"
sidebar_position: 7
description: "Dokumentasi implementasi dashboard: komponen aktual, koneksi data, filter logic, publish record, dan panduan maintenance."
tags: [development, dashboard, implementation, bi, visualization]
doc_id: "V-07"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Dashboard Development

> **Tujuan dokumen ini:** Mendokumentasikan implementasi aktual dashboard — layout, koneksi data, filter logic, dan prosedur maintenance — sebagai referensi bagi analyst dan developer yang perlu memahami atau memodifikasi dashboard.

:::note V-07 vs D-11
**D-11 Dashboard Design** = Spesifikasi desain sebelum build (wireframe, mockup, UX spec).
**V-07 Dashboard Development** = Dokumentasi implementasi setelah build (apa yang benar-benar dibangun dan dipublish).
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Dokumentasi awal post-publish | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `V-07` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Nama Dashboard** | `<Nama Dashboard>` |
| **BI Tool** | `<Tableau / Power BI / Looker / Metabase / Superset>` |
| **URL Production** | `<https://bi.<domain>.org/dashboard/<id>>` |
| **URL Staging** | `<https://bi-staging.<domain>.org/dashboard/<id>>` |
| **Dashboard Owner** | `<Nama Data Analyst, Email>` |
| **Audience** | `<Tim Analitik / Management / Operasional>` |
| **Refresh Schedule** | `<Harian jam 06:00 WIB / Real-time / Manual>` |
| **Dokumen terkait** | [D-11 Dashboard Design](../design/dashboard-design.md) · [D-02 Data Contract](../design/data-contract-spec.md) · [D-04 Data Catalog](../design/data-catalog.md) · [DLV-01 Onboarding](../../delivery/consumer-onboarding-guide.md) |

---

## 1. Inventori Halaman dan Komponen

| Halaman | Tujuan | Audience | Komponen Utama |
|---|---|---|---|
| `<Overview>` | Ringkasan eksekutif KPI utama | Management | KPI cards, trend chart, map |
| `<Detail <Entity>>` | Analisis per entitas | Analyst | Table, bar chart, filter panel |
| `<Drilldown>` | Analisis mendalam per dimensi | Power User | Crosstab, scatter plot |

---

## 2. Koneksi Data

| Nama Koneksi | Tipe | Source | Objek | Refresh |
|---|---|---|---|---|
| `dp_<product>_main` | SQL / Live | `<schema>.v_<product>_daily` | View | Harian 06:00 |
| `dp_<product>_dim` | SQL / Extract | `<schema>.dim_<entity>` | Table | Harian 06:00 |
| `dp_<product>_ref` | SQL / Extract | `<schema>.<referensi>` | Table | Mingguan |

**Credentials:** Disimpan di Vault → `secret/<env>/<domain>/bi-service-account`

---

## 3. Struktur Filter dan Interaksi

| Filter | Tipe | Field Source | Default | Berlaku ke Halaman |
|---|---|---|---|---|
| Periode Tanggal | Date Range | `tanggal` | Bulan berjalan | Semua |
| Status | Multi-select | `status` | Semua | Semua |
| Wilayah | Dropdown Hierarchy | `wilayah_kode` | Semua | Overview, Detail |
| `<Filter lain>` | `<tipe>` | `<field>` | `<default>` | `<halaman>` |

---

## 4. Kalkulasi dan Metrik Kustom

| Nama Kalkulasi | Formula | Satuan | Keterangan |
|---|---|---|---|
| `Total Nilai` | `SUM([jumlah])` | Rupiah | Agregasi sederhana |
| `Penetrasi (%)` | `COUNT([id]) / COUNTD([wilayah_kode]) * 100` | Persen | Rate per wilayah |
| `Growth MoM` | `(SUM([jumlah]) - LOOKUP(SUM([jumlah]),-1)) / ABS(LOOKUP(SUM([jumlah]),-1))` | Persen | Month-over-month |
| `<Kalkulasi lain>` | `<formula>` | `<satuan>` | `<keterangan>` |

---

## 5. Publikasi dan Akses

| Grup Akses | Role | Level | Cara Provision |
|---|---|---|---|
| Management | View Only | Full dashboard | SSO group `mgmt-<domain>` |
| Analyst Internal | View + Download | Full dashboard + data export | SSO group `analyst-<domain>` |
| Consumer Eksternal | View Only | Halaman Overview only | Request via DLV-01 §3 |

---

## 6. Maintenance

**Memperbarui koneksi data setelah schema change:**

1. Buka BI Tool → Edit dashboard
2. Navigate ke Data Source → Edit `dp_<product>_main`
3. Update field yang berubah (rename, tipe baru)
4. Verifikasi semua kalkulasi masih valid
5. Publish ke staging → test → publish ke production

**Troubleshooting refresh gagal:**

| Gejala | Kemungkinan Penyebab | Solusi |
|---|---|---|
| Dashboard stale / tidak update | Pipeline gagal | Cek [M-07 Runbook §4](../monitoring/operations-runbook.md) |
| Error "field not found" | Schema change di source | Update koneksi data |
| Loading lambat (>10 detik) | Extract perlu di-refresh atau query berat | Optimize kalkulasi atau jadwal extract |
| Data berbeda dari SQL query | Filter tersembunyi aktif | Cek context filter di setiap sheet |
