---
title: "Data Quality Report — <Nama Data Product> — <Periode>"
sidebar_label: "Quality Report"
sidebar_position: 2
description: "Laporan kualitas data bulanan mencakup SLO health, temuan, insiden, dan rekomendasi perbaikan"
tags: [monitoring, data-quality, report, slo]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Internal>"
phase: monitoring
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: false
---

# Data Quality Report

**Periode:** `<Bulan YYYY>` | **Dibuat:** `<YYYY-MM-DD>` | **Oleh:** `<Nama Data Steward>`

---

## Ringkasan Eksekutif

| Dimensi | SLO | Aktual | Status | Trend |
|---|---|---|---|---|
| **Freshness** | `<< 25 jam>` | `<Avg: X jam>` | `<Baik/Sedang/Kritis>` | `<↑↓→>` |
| **Availability** | `<99.9%>` | `<X%>` | `<Baik/Sedang/Kritis>` | `<↑↓→>` |
| **Completeness** | `<>99.5%>` | `<X%>` | `<Baik/Sedang/Kritis>` | `<↑↓→>` |
| **Uniqueness** | `<100%>` | `<X%>` | `<Baik/Sedang/Kritis>` | `<↑↓→>` |
| **Validity** | `<>99%>` | `<X%>` | `<Baik/Sedang/Kritis>` | `<↑↓→>` |
| **Error Budget** | `<>50% remaining>` | `<X% remaining>` | `<Baik/Sedang/Kritis>` | `<↑↓→>` |

**Overall Quality Score: `<Baik PASS / Sedang WARNING / Kritis BREACH>`**

---

## 1. Detail SLO per Dimensi

### 1.1 Freshness

| Metrik | Target | Actual | % Days Met |
|---|---|---|---|
| Avg latensi batch | `< 25 jam` | `<X jam>` | `<X%>` |
| Max latensi batch | `< 30 jam` | `<X jam>` | `<X%>` |
| Hari dengan SLO breach | `0` | `<X hari>` | |

**Insiden freshness:**
- `<Tanggal X: Pipeline delay X jam karena Y — RESOLVED>`

### 1.2 Availability

| Periode | Planned Downtime | Unplanned Downtime | Total Availability |
|---|---|---|---|
| `<Bulan ini>` | `<X menit>` | `<X menit>` | `<X%>` |

### 1.3 Completeness per Kolom Kritis

| Kolom | SLO | Jan | Feb | Mar | Trend |
|---|---|---|---|---|---|
| `<id>` | `100%` | `<100%>` | `<100%>` | `<100%>` | `→` |
| `<nama>` | `>99.5%` | `<99.8%>` | `<99.7%>` | `<99.2%>` | `↓[!]` |
| `<tanggal>` | `>99%` | `<99.9%>` | `<99.8%>` | `<99.5%>` | `→` |

### 1.4 Volume Anomali

| Tanggal | Expected (±30%) | Actual | Status | Investigasi |
|---|---|---|---|---|
| `<YYYY-MM-DD>` | `<100K–180K>` | `<X>` | `<Baik/Kritis>` | `<Catatan jika anomali>` |

---

## 2. Insiden Kualitas Bulan Ini

| ID | Tanggal | Severity | Deskripsi | Root Cause | Resolusi | SLA Met? |
|---|---|---|---|---|---|---|
| `<INC-001>` | `<YYYY-MM-DD>` | `<P1/P2/P3>` | `<Deskripsi singkat>` | `<Penyebab>` | `<Cara fix>` | `<[x]/[ ]>` |

**Total insiden bulan ini:** `<X insiden (P1: X, P2: X, P3: X)>`
**MTTR (Mean Time to Resolve):** `<X jam>`

---

## 3. Temuan & Rekomendasi

| Temuan | Dampak | Rekomendasi | Priority | Owner | Due |
|---|---|---|---|---|---|
| `<Completeness nama turun ke 99.2%>` | `<Medium — masih di atas SLO>` | `<Investigasi sumber upstream>` | `<P2>` | `<DE>` | `<YYYY-MM-DD>` |

---

## 4. Consumer Feedback

| Consumer | Feedback | Aksi |
|---|---|---|
| `<Tim A>` | `<"Data terlambat 2x bulan ini">` | `<Investigasi pipeline bottleneck>` |

---
---
title: "Cost Report — <Nama Data Product> — <Periode>"
sidebar_label: "Cost Report"
sidebar_position: 3
description: "Laporan biaya infrastruktur dan operasional data product per periode"
tags: [monitoring, cost, finops, infrastructure]
data_product_id: "<domain>/<data-product-name>/v<version>"
phase: monitoring
last_updated: "<YYYY-MM-DD>"
---

# Cost Report

**Periode:** `<Bulan YYYY>` | **Dibuat:** `<YYYY-MM-DD>` | **Oleh:** `<Nama PM/SRE>`

---

## Ringkasan Biaya

| Komponen | Budget | Aktual | Variance | Status |
|---|---|---|---|---|
| **Storage** | `<Rp X>` | `<Rp X>` | `<+/-X%>` | `<Baik/Sedang/Kritis>` |
| **Compute** | `<Rp X>` | `<Rp X>` | `<+/-X%>` | `<Baik/Sedang/Kritis>` |
| **Database** | `<Rp X>` | `<Rp X>` | `<+/-X%>` | `<Baik/Sedang/Kritis>` |
| **Networking** | `<Rp X>` | `<Rp X>` | `<+/-X%>` | `<Baik/Sedang/Kritis>` |
| **Total** | `<Rp X>` | `<Rp X>` | `<+/-X%>` | `<Baik/Sedang/Kritis>` |

**Biaya per record yang diproses:** `<Rp X / record>`

---

## Detail per Komponen

### Storage

| Layer | Storage Used | Cost/GB | Total |
|---|---|---|---|
| Bronze | `<X GB>` | `<Rp X>` | `<Rp X>` |
| Silver | `<X GB>` | `<Rp X>` | `<Rp X>` |
| Gold | `<X GB>` | `<Rp X>` | `<Rp X>` |

### Compute (Pipeline Runs)

| Pipeline | Runs/Bulan | Avg Duration | Compute Hours | Cost |
|---|---|---|---|---|
| `<Ingestion>` | `<30>` | `<45 menit>` | `<22.5 jam>` | `<Rp X>` |
| `<Transformation>` | `<30>` | `<60 menit>` | `<30 jam>` | `<Rp X>` |

---

## Tren & Proyeksi

| Bulan | Aktual | Budget | Forecast Next Month |
|---|---|---|---|
| `<Jan>` | `<Rp X>` | `<Rp X>` | |
| `<Feb>` | `<Rp X>` | `<Rp X>` | |
| `<Mar>` | `<Rp X>` | `<Rp X>` | `<Rp X (estimasi)>` |

---

## Rekomendasi Optimasi

| Opportunity | Estimasi Penghematan | Tradeoff | Priority |
|---|---|---|---|
| `<Pindah Bronze ke cold storage setelah 30 hari>` | `<~Rp X/bulan>` | `<Query slower>` | `<P2>` |
| `<Enable Parquet Snappy compression>` | `<~Rp X/bulan>` | `<Minimal CPU overhead>` | `<P1>` |

---
---
title: "Incident Report — <ID Insiden> — <Nama Data Product>"
sidebar_label: "Incident Report"
sidebar_position: 4
description: "Laporan insiden data product: timeline, root cause analysis, dan corrective actions"
tags: [monitoring, incident, post-mortem, sla]
data_product_id: "<domain>/<data-product-name>/v<version>"
phase: monitoring
last_updated: "<YYYY-MM-DD>"
---

# Incident Report

:::danger Insiden Aktif
`[Hapus blok ini setelah insiden resolved]`
Insiden ini **masih aktif**. Update dokumen ini setiap 2 jam selama insiden berlangsung.
:::

---

## Ringkasan Insiden

| Atribut | Detail |
|---|---|
| **Incident ID** | `<INC-YYYY-MM-DD-001>` |
| **Severity** | `<P1 Critical / P2 High / P3 Medium / P4 Low>` |
| **Status** | `<Kritis Active / Sedang Monitoring / Baik Resolved>` |
| **Data Product** | `<Nama Data Product>` |
| **Komponen Terdampak** | `<Pipeline / API / Database / Dashboard>` |
| **Terdeteksi** | `<YYYY-MM-DD HH:MM WIB>` |
| **Incident Commander** | `<Nama>` |
| **Resolved (jika ada)** | `<YYYY-MM-DD HH:MM WIB>` |
| **Durasi** | `<X jam X menit>` |

---

## Dampak

**Consumer yang terdampak:**
- `<Tim/Sistem A: Tidak dapat akses data sejak HH:MM>`
- `<Tim/Sistem B: Data stale, SLO freshness breached>`

**SLO yang dilanggar:**
- `<Freshness: Data delayed X jam (SLO: < 25 jam)>`
- `<Availability: API down selama X menit (SLO: 99.9%)>`

---

## Timeline

| Waktu (WIB) | Kejadian | Oleh |
|---|---|---|
| `<HH:MM>` | `<Incident terdeteksi via alert Grafana>` | `<Automated>` |
| `<HH:MM>` | `<Incident Commander di-page>` | `<Grafana OnCall>` |
| `<HH:MM>` | `<Root cause diidentifikasi>` | `<Nama DE>` |
| `<HH:MM>` | `<Fix diterapkan>` | `<Nama DE>` |
| `<HH:MM>` | `<Pipeline rerun berhasil>` | `<Nama DE>` |
| `<HH:MM>` | `<Monitoring 1 jam — stabil>` | `<Nama DS>` |
| `<HH:MM>` | `<Incident resolved, consumer dinotifikasi>` | `<PM>` |

---

## Root Cause Analysis (5 Whys)

| Why | Temuan |
|---|---|
| **Why 1:** Mengapa insiden terjadi? | `<Contoh: Pipeline gagal berjalan>` |
| **Why 2:** Mengapa pipeline gagal? | `<Contoh: Connection ke sumber timeout>` |
| **Why 3:** Mengapa connection timeout? | `<Contoh: Sumber melakukan maintenance mendadak>` |
| **Why 4:** Mengapa tidak ada notifikasi maintenance? | `<Contoh: Tidak ada SLA atau komunikasi dari tim sumber>` |
| **Why 5 (Root Cause):** | `<Contoh: Tidak ada SLA agreement dengan tim sumber yang mewajibkan pra-notifikasi maintenance>` |

---

## Corrective Actions

| Aksi | Tipe | Owner | Due Date | Status |
|---|---|---|---|---|
| `<Buat SLA agreement dengan tim sumber>` | `<Preventif>` | `<DPO + PM>` | `<YYYY-MM-DD>` | `<[In Progress] In Progress>` |
| `<Tambahkan retry policy 3x pada ingestion>` | `<Preventif>` | `<DE>` | `<YYYY-MM-DD>` | `<[ ] TODO>` |
| `<Setup dead letter queue>` | `<Korektif>` | `<DE>` | `<YYYY-MM-DD>` | `<[ ] TODO>` |
| `<Add source availability check ke pre-flight>` | `<Preventif>` | `<DE>` | `<YYYY-MM-DD>` | `<[ ] TODO>` |

---

## Komunikasi

**Notifikasi yang dikirimkan:**

| Waktu | Channel | Pesan | Penerima |
|---|---|---|---|
| `<HH:MM>` | `<Slack #dq-alerts>` | `<"Incident P1 aktif — pipeline X down">` | `<Tim data + consumer>` |
| `<HH:MM>` | `<Email>` | `<Status update: root cause identified>` | `<DPO + consumer leads>` |
| `<HH:MM>` | `<Slack #dq-alerts>` | `<"Incident resolved — data sudah normal">` | `<Tim data + consumer>` |

---

## Lessons Learned

**Apa yang berjalan baik:**
- `<Alert terdeteksi dalam 5 menit>`
- `<Tim on-call merespons cepat>`

**Apa yang bisa diperbaiki:**
- `<Tidak ada runbook untuk skenario ini — perlu dibuat>`
- `<Komunikasi ke consumer lambat (30 menit setelah detect)>`

**Action untuk mencegah recurrence:**
> `[Rangkuman 1-3 aksi paling penting dari tabel corrective actions di atas]`
