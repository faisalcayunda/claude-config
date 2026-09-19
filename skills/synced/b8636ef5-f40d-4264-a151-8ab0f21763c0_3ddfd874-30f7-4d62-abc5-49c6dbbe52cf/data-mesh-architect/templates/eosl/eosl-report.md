---
title: "End of Service Life Report — <Nama Data Product>"
sidebar_label: "EoSL Report"
sidebar_position: 1
description: "Laporan resmi penutupan layanan data product mencakup justifikasi, dampak consumer, arsip data, dan lessons learned"
tags: [eosl, deprecation, retirement, end-of-life]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Internal>"
phase: eosl
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: false
---

# End of Service Life (EoSL) Report

> **Tujuan dokumen ini:** Mendokumentasikan proses penghentian layanan data product secara terstruktur, memastikan consumer sudah dinotifikasi dan ter-migrasi, data diarsipkan sesuai kebijakan, dan lessons learned terdokumentasi.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 1.0 | Draft EoSL proposal | `<Nama DPO>` |
| `<YYYY-MM-DD>` | 2.0 | Sign-off final | `<Nama>` |

---

## Ringkasan

| Atribut | Detail |
|---|---|
| **Nama Data Product** | `<Nama Data Product>` |
| **Domain** | `<Nama Domain>` |
| **Data Product Owner** | `<Nama>` |
| **Versi Terakhir** | `<X.Y.Z>` |
| **Tanggal Go-Live Pertama** | `<YYYY-MM-DD>` |
| **Tanggal Deprecation Announced** | `<YYYY-MM-DD>` |
| **Tanggal EoSL Efektif** | `<YYYY-MM-DD>` |
| **Total Umur Layanan** | `<X tahun X bulan>` |
| **Pengganti** | `<Nama data product pengganti / "Tidak ada pengganti">` |

---

## 1. Justifikasi EoSL

`[Mandatory]`

**Alasan penghentian layanan** (centang yang berlaku):

- [ ] Tidak ada consumer aktif selama > 3 bulan terakhir
- [ ] Domain bisnis ditutup atau di-merge dengan domain lain
- [ ] Data product digantikan oleh versi baru yang lebih baik
- [ ] Data source underlying dihentikan
- [ ] Biaya operasional tidak sebanding dengan value yang diberikan
- [ ] Regulasi atau kebijakan baru mengharuskan penghentian
- [ ] Keputusan strategic lainnya: `<Jelaskan>`

**Narasi justifikasi:**
> `[Penjelasan lengkap mengapa data product ini dihentikan]`

**Data pendukung:**
- Consumer aktif 3 bulan terakhir: `<X consumer (target minimal: Y)>`
- Biaya operasional per bulan: `<Rp X>`
- Usage (queries/API calls) per bulan: `<X (target minimal: Y)>`

---

## 2. Dampak Consumer & Rencana Migrasi

`[Mandatory]`

### 2.1 Registered Consumer

| Consumer | Sistem/Tim | Cara Penggunaan | Status Migrasi | Target Migrasi |
|---|---|---|---|---|
| `<Nama Consumer 1>` | `<Tim/Sistem>` | `<API / SQL / Dashboard>` | `<[x] Sudah migrasi / [In Progress] Dalam proses / [ ] Belum>` | `<YYYY-MM-DD>` |
| `<Nama Consumer 2>` | | | | |

### 2.2 Jalur Migrasi yang Direkomendasikan

| Dari | Ke | Langkah Migrasi | Dokumen |
|---|---|---|---|
| `<Output port lama>` | `<Output port di data product pengganti>` | `<1. Daftar ke product baru 2. Update koneksi 3. Validasi data>` | `<Link ke migration guide>` |

### 2.3 Notifikasi Consumer

| Tanggal | Channel | Isi Notifikasi | Penerima |
|---|---|---|---|
| `<YYYY-MM-DD>` | `<Email + Slack>` | `<Pengumuman deprecation 6 bulan sebelumnya>` | `<Semua registered consumers>` |
| `<YYYY-MM-DD>` | `<Email>` | `<Reminder 3 bulan sebelumnya>` | `<Consumer belum migrasi>` |
| `<YYYY-MM-DD>` | `<Email>` | `<Final notice 1 bulan sebelumnya>` | `<Consumer belum migrasi>` |
| `<YYYY-MM-DD>` | `<Email + Slack>` | `<EoSL effective — service stopped>` | `<Semua consumer>` |

---

## 3. Rencana Archival Data

`[Mandatory]`

### 3.1 Kebijakan Retensi per Layer

| Layer | Lokasi Saat Ini | Action | Target Lokasi | Tanggal |
|---|---|---|---|---|
| `<Bronze (raw)>` | `<s3://bucket/bronze/...>` | `<Archive>` | `<s3://archive/bronze/...>` | `<YYYY-MM-DD>` |
| `<Silver>` | `<s3://bucket/silver/...>` | `<Archive>` | `<s3://archive/silver/...>` | `<YYYY-MM-DD>` |
| `<Gold>` | `<schema.table_gold>` | `<Export + Archive + Drop>` | `<s3://archive/gold/...>` | `<YYYY-MM-DD>` |

### 3.2 PII Handling saat EoSL

Sesuai **UU PDP Pasal 32** dan kebijakan retensi data:

| Tindakan | Kolom/Data | Metode | Tanggal |
|---|---|---|---|
| `<Hapus PII>` | `<nik, nama, tanggal_lahir>` | `<Secure deletion (DoD 5220.22-M)>` | `<YYYY-MM-DD>` |
| `<Anonimisasi aggregate>` | `<Statistik demografi>` | `<K-anonymization k=50>` | `<YYYY-MM-DD>` |
| `<Pertahankan>` | `<Data agregat non-PII>` | `<Archive cold storage>` | `<Permanent>` |

---

## 4. Decommissioning Checklist

```
Infrastructure:
[ ] Semua consumer sudah off atau ter-migrasi
[ ] Data di-archive sesuai kebijakan retensi
[ ] PII dihapus sesuai UU PDP dan jadwal
[ ] Database tabel di-drop (setelah archive dikonfirmasi)
[ ] Object storage di-lifecycle ke cold/archive tier
[ ] API/service instances di-shutdown
[ ] DNS records dihapus atau dialihkan
[ ] Monitoring & alerting dinonaktifkan
[ ] CI/CD pipeline dinonaktifkan

Governance:
[ ] Data Catalog entry diupdate ke status "Retired"
[ ] Data Contract diarsipkan (bukan dihapus — untuk audit)
[ ] RoPA diupdate: catat tanggal penghentian pemrosesan
[ ] JIRA project diarsipkan
[ ] Git repository diarsipkan (bukan dihapus)
[ ] Biaya infrastruktur sudah berhenti (verifikasi billing)

Documentation:
[ ] EoSL report ini sudah final dan di-approve
[ ] Lessons learned didokumentasikan
[ ] Knowledge transfer ke tim lain (jika relevan) sudah dilakukan
```

---

## 5. Lessons Learned

`[Mandatory]`

### Yang Berjalan Baik
- `<Hal positif yang bisa direplikasi ke data product lain>`

### Yang Bisa Diperbaiki
- `<Hal yang seharusnya dilakukan berbeda>`

### Rekomendasi untuk Data Product Berikutnya
- `<Saran praktis berdasarkan pengalaman ini>`

---

## Sign-Off

| Role | Nama | Persetujuan | Tanggal |
|---|---|---|---|
| Data Product Owner | `<Nama>` | `☐ Approved` | |
| Data Architect | `<Nama>` | `☐ Approved` | |
| Legal / DPO Officer | `<Nama>` | `☐ Approved (PII deletion verified)` | |
| SRE / DevOps | `<Nama>` | `☐ Infra decommissioned` | |
