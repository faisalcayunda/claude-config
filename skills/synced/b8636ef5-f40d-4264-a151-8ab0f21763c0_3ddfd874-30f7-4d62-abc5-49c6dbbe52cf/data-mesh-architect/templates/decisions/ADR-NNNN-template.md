---
title: "ADR-<NNNN> — <Judul Keputusan>"
sidebar_label: "ADR-<NNNN>"
sidebar_position: 1
description: "<Ringkasan singkat keputusan arsitektur>"
tags: [decisions, architecture, adr]
data_product_id: "<domain>/<data-product-name>/v<version>"
status: "<proposed|accepted|deprecated|superseded>"
date: "<YYYY-MM-DD>"
decision_makers: ["<Nama DA>", "<Nama DPO>"]
consulted: ["<Nama DE>", "<Nama SRE>"]
informed: ["<Nama PM>", "<Nama Consumer>"]
supersedes: "<ADR-NNNN jika menggantikan ADR lain, atau null>"
superseded_by: "<ADR-NNNN jika digantikan, atau null>"
---

# ADR-`<NNNN>` — `<Judul Keputusan Arsitektur>`

**Status:** `<Proposed | Accepted | Deprecated | Superseded>`  
**Tanggal:** `<YYYY-MM-DD>`  
**Decision Makers:** `<Nama DA, Nama DPO>`

---

## Konteks & Permasalahan

`[Mandatory]`

> Deskripsikan konteks dan situasi yang memunculkan kebutuhan untuk keputusan ini. Apa masalah yang perlu diselesaikan? Faktor apa yang perlu dipertimbangkan? Tuliskan secara netral tanpa menyebut solusi.

`[Contoh: "Data product ini perlu menyimpan data historis dengan volume ~500 GB yang akan tumbuh ~50 GB/bulan. Data perlu bisa di-query oleh multiple consumers dengan latency < 5 detik, dan harus mendukung schema evolution tanpa downtime. Tim memiliki keahlian SQL dan Python, tetapi tidak familiar dengan proprietary tools."]`

---

## Decision Drivers

`[Mandatory]`

Faktor-faktor yang mempengaruhi keputusan ini (prioritas dari yang paling penting):

1. `<Contoh: Tidak ada vendor lock-in — data product harus tetap bisa berjalan jika vendor berganti>`
2. `<Contoh: Biaya operasional < Rp X/bulan>`
3. `<Contoh: Tim sudah familiar dengan teknologi pilihan (learning curve rendah)>`
4. `<Contoh: Mendukung schema evolution tanpa memerlukan full rewrite>`
5. `<Contoh: Data residency: harus bisa self-hosted di Indonesia>`

---

## Opsi yang Dipertimbangkan

### Opsi A: `<Nama Opsi — contoh: Apache Iceberg di MinIO>`

| Dimensi | Penilaian |
|---|---|
| **Biaya** | `<Estimasi biaya>` |
| **Kompleksitas** | `<Tinggi/Sedang/Rendah>` |
| **Vendor Lock-in** | `<Ada/Tidak ada>` |
| **Learning Curve** | `<Tinggi/Sedang/Rendah>` |
| **Maturity** | `<Mature/Emerging/Experimental>` |

**Pro:**
- `<Pro 1>`
- `<Pro 2>`

**Kontra:**
- `<Kontra 1>`
- `<Kontra 2>`

---

### Opsi B: `<Nama Opsi — contoh: Delta Lake di object storage>`

*(Format sama dengan Opsi A)*

**Pro:**
- `<Pro 1>`
- `<Pro 2>`

**Kontra:**
- `<Kontra 1>`
- `<Kontra 2>`

---

### Opsi C: `<Nama Opsi>`

*(Format sama dengan Opsi A)*

---

## Keputusan

`[Mandatory]`

**Opsi yang Dipilih: `<Nama Opsi>`**

**Alasan:**
> `[Jelaskan mengapa opsi ini dipilih dibanding yang lain. Hubungkan dengan Decision Drivers di atas. Contoh: "Apache Iceberg di MinIO dipilih karena (1) engine-agnostic sehingga tidak ada vendor lock-in, (2) mendukung schema evolution secara native, (3) bisa self-hosted sesuai kebutuhan data residency, dan (4) biaya ~40% lebih rendah dari alternatif managed service. Tim akan memerlukan ~2 sprint untuk learning curve, yang dianggap acceptable."]`

---

## Konsekuensi

### Positif
- [x] `<Konsekuensi positif 1>`
- [x] `<Konsekuensi positif 2>`

### Negatif / Tradeoff
- [!] `<Tradeoff yang diterima — contoh: "Tim perlu 2 sprint learning curve">`
- [!] `<Tradeoff lain>`

### Risiko
- Kritis `<Risiko yang muncul dari keputusan ini — contoh: "Iceberg masih relative new, community support belum sekuat Delta Lake">`
- Mitigasi: `<Bagaimana risiko akan dimitigasi>`

### Dependensi Baru
- `<Dependensi yang muncul — contoh: "Perlu MinIO cluster sebagai prerequisite">`

---

## Konfirmasi

Bagaimana keputusan ini akan divalidasi? Kapan kita tahu keputusan ini tepat?

> `[Contoh: "Keputusan ini dikonfirmasi valid jika dalam 3 bulan pertama: query latency terpenuhi < 5 detik P95, biaya storage < Rp X/bulan, dan tim berhasil melakukan schema evolution setidaknya 1 kali tanpa insiden."]`

---

## Catatan Tambahan

`[Opsional]`

- Link ke PoC/benchmark yang mendukung keputusan: `<URL>`
- Link ke diskusi awal: `<Slack thread / meeting notes URL>`
- Link ke dokumentasi teknis opsi yang dipilih: `<URL>`
