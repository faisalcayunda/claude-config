---
title: "Data Product Proposal — <Nama Data Product>"
sidebar_label: "Proposal"
sidebar_position: 2
description: "Inisiasi dan justifikasi bisnis untuk pembangunan data product baru"
tags: [bootstrap, proposal, business-case]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: bootstrap
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Product Proposal

> **Tujuan dokumen ini:** Memberikan justifikasi bisnis yang kuat dan rencana awal untuk pembangunan data product. Dokumen ini menjadi dasar keputusan *go/no-go* oleh Data Product Owner dan stakeholder.

:::info
Dokumen ini mengikuti format **Initiation Request** standar. Harus diselesaikan sebelum fase Design dimulai dan memerlukan sign-off formal dari DPO.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi Perubahan | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |
| | | | |

---

## Definisi Umum

| Atribut | Nilai |
|---|---|
| **Nama Data Product** | `<Nama Data Product>` |
| **Domain** | `<Nama Domain>` |
| **Pemilik Domain** | `<Tim / Organisasi>` |
| **Data Product Owner** | `<Nama, Email>` |
| **Tujuan Utama** | `<Satu kalimat tujuan>` |
| **Archetype** | `<Source-Aligned / Aggregate / Consumer-Aligned>` |
| **Tanggal Pengajuan** | `<YYYY-MM-DD>` |
| **Target Go-Live** | `<YYYY-MM-DD>` |

---

## 1. Ringkasan Eksekutif & Strategic Alignment

### 1.1 Pemetaan Masalah

`[Mandatory]` — *Role: Data Product Owner*

Deskripsikan masalah bisnis yang akan diselesaikan oleh data product ini. Gunakan format **Problem Statement**:

> *"[Aktor] tidak bisa [melakukan sesuatu] karena [alasan/hambatan], yang mengakibatkan [dampak bisnis negatif]."*

**Contoh:** *"Tim Monitoring tidak bisa mendeteksi anomali distribusi secara real-time karena data dari lapangan baru tersedia T+3 hari, yang mengakibatkan intervensi lambat dan target program tidak tercapai."*

> **[Isi problem statement di sini]**

**Dampak saat ini (tanpa data product ini):**

| Dampak | Ukuran / Estimasi |
|---|---|
| `<Contoh: Waktu yang terbuang>` | `<X jam/minggu>` |
| `<Contoh: Keputusan berdasarkan data stale>` | `<X% keputusan>` |
| `<Contoh: Risiko kepatuhan>` | `<Deskripsi>` |

### 1.2 Keselarasan Strategis

`[Mandatory]`

| Tujuan Strategis | Kontribusi Data Product Ini |
|---|---|
| `<Tujuan organisasi/program>` | `<Bagaimana data product mendukung tujuan ini>` |
| | |

### 1.3 Kepemilikan Domain

`[Mandatory]`

Data product ini berada dalam domain **`<Nama Domain>`** karena:
- `<Alasan 1: bounded context yang jelas>`
- `<Alasan 2: tim yang bertanggung jawab sudah ada>`
- `<Alasan 3: sumber data berasal dari domain ini>`

---

## 2. Analisis Target Konsumen Data

### 2.1 Target Persona Konsumen

`[Mandatory]` — *Role: Data Analyst*

| Persona | Jabatan | Organisasi | Kebutuhan Utama | Frekuensi Akses |
|---|---|---|---|---|
| `<Nama Persona>` | `<Jabatan>` | `<Organisasi>` | `<Apa yang ingin diketahui>` | `<Harian/Mingguan>` |
| | | | | |

### 2.2 Actionable Insights yang Diharapkan

`[Mandatory]`

**Tujuan (Goal):**
- Goal 1: `<...>`
- Goal 2: `<...>`
- Goal 3: `<...>`

**Contoh Pertanyaan Bisnis yang Akan Terjawab:**
- `<Pertanyaan 1: "Berapa persen penerima manfaat yang sudah terlayani di wilayah X?">`
- `<Pertanyaan 2>`
- `<Pertanyaan 3>`

**Pemanfaatan Data (Insight → Action):**

| Insight | Tindakan yang Dipicu |
|---|---|
| `<Contoh insight dari data>` | `<Keputusan atau aksi bisnis yang dihasilkan>` |
| | |

### 2.3 Antarmuka Konsumsi (Output Ports)

`[Mandatory]` — Centang yang relevan dan isi detail:

- [ ] **REST API (Terautentikasi)** — `<Deskripsi use case API>`
- [ ] **Streaming Pipeline** — `<Deskripsi use case streaming>`
- [ ] **SQL View / Datamart** — `<Deskripsi use case query>`
- [ ] **Dashboard Eksekutif** — `<Deskripsi use case dashboard>`
- [ ] **File Export (CSV/Parquet)** — `<Deskripsi use case file>`
- [ ] **Lainnya:** `<Sebutkan>`

---

## 3. Ruang Lingkup

### 3.1 Ruang Lingkup Data

`[Mandatory]`

**In-Scope:**
- `<Entitas data yang termasuk>`
- `<Periode waktu yang dicakup>`
- `<Geografi / unit organisasi yang tercakup>`

**Out-of-Scope:**
- `<Apa yang TIDAK termasuk dan alasannya>`
- `<Transformasi yang akan dikerjakan di fase lain>`
- `<Data dari sumber yang belum siap diintegrasikan>`

### 3.2 Sumber Input (Upstream)

`[Mandatory]`

| Sistem Sumber | Tipe | Data yang Diambil | Status Ketersediaan |
|---|---|---|---|
| `<Nama sistem>` | `<API/DB/File/Stream>` | `<Entitas/tabel/topik>` | `<Tersedia/Perlu agreement/Dalam assessment>` |
| | | | |

### 3.3 Antarmuka Konsumsi (Output Ports Detail)

`[Mandatory]`

| Output Port | Tipe | Consumer | Format | Frekuensi Refresh |
|---|---|---|---|---|
| `<Nama port>` | `<Tabel/API/Stream/File>` | `<Nama consumer/sistem>` | `<SQL/JSON/Parquet>` | `<Real-time/15min/Harian>` |
| | | | | |

---

## 4. Business Case

### 4.1 Estimasi Biaya (Build & Run)

`[Mandatory]` — *Role: PM + Data Architect*

| Komponen | Fase Build (Satu Kali) | Fase Run (Per Bulan) |
|---|---|---|
| Infrastructure (storage, compute) | `<Rp / USD>` | `<Rp / USD>` |
| Lisensi tools | `<Rp / USD>` | `<Rp / USD>` |
| Engineering effort | `<X sprint @ Y orang>` | `<X jam/bulan>` |
| **Total Estimasi** | **`<Total>`** | **`<Total/bulan>`** |

### 4.2 Manfaat yang Diharapkan

`[Mandatory]`

| Manfaat | Tipe | Estimasi Nilai |
|---|---|---|
| `<Contoh: Pengurangan waktu pelaporan>` | `<Kuantitatif>` | `<X jam/minggu>` |
| `<Contoh: Peningkatan kualitas keputusan>` | `<Kualitatif>` | `<Deskripsi>` |
| `<Contoh: Kepatuhan regulasi>` | `<Risk reduction>` | `<Mitigasi risiko denda>` |

### 4.3 Metrik Kesuksesan (SLO/KPI)

`[Mandatory]`

| Metrik | Definisi | Target | Cara Mengukur |
|---|---|---|---|
| `<Contoh: Freshness>` | `<Data tersedia dalam X jam setelah sumber update>` | `<99% dalam 4 jam>` | `<Pipeline monitoring>` |
| `<Contoh: Consumer adoption>` | `<Jumlah tim aktif menggunakan data product>` | `<5 tim dalam 3 bulan>` | `<Usage analytics>` |
| `<Contoh: Data quality score>` | `<% data yang lolos semua quality rules>` | `<>99.5%>` | `<Great Expectations dashboard>` |

---

## 5. Pemeriksaan Tata Kelola & Kepatuhan

### 5.1 Klasifikasi Data

`[Mandatory]`

| Level Klasifikasi | Berlaku untuk | Kontrol yang Diperlukan |
|---|---|---|
| `<Public / Internal / Restricted / Confidential>` | `<Atribut/entitas mana>` | `<Enkripsi/Masking/RBAC>` |

### 5.2 Batasan Penggunaan

`[Mandatory jika ada]`

- `<Contoh: Data hanya boleh digunakan untuk keperluan operasional program X>`
- `<Contoh: Dilarang dikombinasikan dengan dataset Y tanpa persetujuan DPO>`
- `<Contoh: Tidak boleh diekspor ke pihak ketiga tanpa DPIA>`

### 5.3 Privacy & Compliance Quick Check

`[Mandatory]`

| Pertanyaan | Jawaban | Tindak Lanjut |
|---|---|---|
| Apakah ada data pribadi (nama, NIK, alamat, dsb.)? | `<Ya/Tidak>` | `<RoPA wajib dibuat>` |
| Apakah ada data pribadi spesifik (kesehatan, biometrik, anak)? | `<Ya/Tidak>` | `<DPIA wajib>` |
| Apakah pemrosesan melibatkan >1.000 data subjek? | `<Ya/Tidak>` | `<DPIA dipertimbangkan>` |
| Apakah ada transfer data lintas batas negara? | `<Ya/Tidak>` | `<Evaluasi data residency>` |

---

## 6. Perencanaan Proyek

### 6.1 Tim Inti

`[Mandatory]`

| Role | Nama | Organisasi | FTE Alokasi |
|---|---|---|---|
| Data Product Owner | `<Nama>` | `<Org>` | `<0.2 FTE>` |
| Data Architect | `<Nama>` | `<Org>` | `<0.5 FTE>` |
| Lead Data Engineer | `<Nama>` | `<Org>` | `<1.0 FTE>` |
| Data Steward / Analyst | `<Nama>` | `<Org>` | `<0.5 FTE>` |
| Project Manager | `<Nama>` | `<Org>` | `<0.3 FTE>` |
| Legal / Compliance | `<Nama>` | `<Org>` | `<0.1 FTE>` |

### 6.2 Timeline Project

`[Mandatory]`

```
Fase Bootstrap:    <YYYY-MM-DD> s.d. <YYYY-MM-DD>  (~2 minggu)
Fase Design:       <YYYY-MM-DD> s.d. <YYYY-MM-DD>  (~3 minggu)
Fase Development:  <YYYY-MM-DD> s.d. <YYYY-MM-DD>  (~6-8 minggu)
Fase Delivery:     <YYYY-MM-DD> s.d. <YYYY-MM-DD>  (~2 minggu)
Go-Live:           <YYYY-MM-DD>
```

| Milestone | Target Tanggal | Owner |
|---|---|---|
| Business Process Research selesai | `<Tanggal>` | DA + BA |
| Data Product Canvas disetujui | `<Tanggal>` | DPO |
| Data Contract v1.0 disetujui | `<Tanggal>` | DA |
| Development sprint pertama mulai | `<Tanggal>` | PM |
| UAT dimulai | `<Tanggal>` | PM + Consumer |
| Go-Live | `<Tanggal>` | DPO + SRE |

### 6.3 Dependensi & Risiko Awal

| Dependensi | Tipe | Status | Owner |
|---|---|---|---|
| `<Akses ke sistem sumber X>` | `<Teknis>` | `<Dalam proses>` | `<Nama>` |
| `<Persetujuan data sharing dari Y>` | `<Governance>` | `<Belum dimulai>` | `<Nama>` |

---

## 7. Sign-Off

`[Mandatory sebelum fase Design]`

| Role | Nama | Tanda Tangan / Approval | Tanggal |
|---|---|---|---|
| Data Product Owner | `<Nama>` | `☐ Approved / ☐ Rejected / ☐ Revision needed` | |
| Domain Lead | `<Nama>` | `☐ Approved / ☐ Rejected / ☐ Revision needed` | |
| Data Architect | `<Nama>` | `☐ Approved / ☐ Rejected / ☐ Revision needed` | |
| Governance / Legal | `<Nama>` | `☐ Approved / ☐ Rejected / ☐ Revision needed` | |

**Catatan Sign-Off:**
> `[Isi catatan jika ada kondisi khusus atau syarat approval]`

---

## 8. Lampiran

`[Opsional]`

- Link ke Business Process Research: `../bootstrap/business-process-research.md`
- Link ke Data Product Canvas: `../bootstrap/canvas.md`
- Dokumen referensi tambahan: `<URL>`
