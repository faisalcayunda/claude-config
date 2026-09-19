# SIPGN: Modul, Submodul, dan Dokumen Kontrol Peruri

## ⚠️ DUA skema penomoran modul — selalu klarifikasi

Di lapangan beredar dua urutan "7 Modul SIPGN". Keduanya valid di konteksnya masing-masing; jika user menyebut "Modul 2" dkk., tanyakan/deteksi skema mana.

| # | **Skema A — Penomoran dokumen Peruri** (folder PRD/FSD/TSD project; deliverable resmi) | **Skema B — Skema fungsional/aplikasi** (dipakai a.l. template issue internal Tim Data, 17 Mei 2026) |
|---|---|---|
| 1 | Promosi & Kerjasama | Promosi |
| 2 | **Logistik / Distribusi** | **Penerima Manfaat (PEM)** |
| 3 | **Penerima Manfaat** | **Pengadaan (SCM)** |
| 4 | Produksi | Produksi (ERP) |
| 5 | **Pengadaan / Supply Chain** | **Distribusi (POP)** |
| 6 | Pemantauan & Pelaporan (dashboard) | Monitoring & Evaluasi |
| 7 | Sistem & Tata Kelola | Tata Kelola |

Catatan: dokumen governance lain (mis. data vocabulary G-01 Fleet/Distribusi) ada yang memakai "Modul 5 Distribusi" (Skema B). Modul yang isinya sama: Promosi(1), Produksi(4), Monev(6), Tata Kelola(7); yang BERTUKAR: Distribusi, PM, Pengadaan.

## 31 Submodul (Skema A — sesuai deliverable Peruri)

**Modul 1 — Promosi & Kerjasama (3):** 1.1 Pusat Informasi Program (kode PIP) · 1.2 Informasi Kepesertaan · 1.3 Manajemen Kerjasama.
**Modul 2 — Logistik/Distribusi (4):** 2.1 Perencanaan & Penugasan Pengiriman · 2.2 Pelacakan & Pemantauan Pengiriman · 2.3 Konfirmasi & Serah Terima Digital · 2.4 Manajemen Laporan & Insiden.
**Modul 3 — Penerima Manfaat (5, kode PMA):** 3.1 Pendaftaran & Pengelolaan Data Penerima (PMA-01) · 3.2 Informasi & Notifikasi (PMA-02) · 3.3 Konfirmasi Penerimaan & Absensi (PMA-03) · 3.4 Umpan Balik & Pelaporan (PMA-04) · 3.5 Perencanaan Penerima Manfaat (PMA-05).
**Modul 4 — Produksi (4):** 4.1 Perencanaan Produksi Harian · 4.2 Manajemen Proses Memasak · 4.3 Pemantauan Kualitas & Kepatuhan · 4.4 Manajemen Limbah.
**Modul 5 — Pengadaan/Supply Chain (2):** 5.1 Manajemen Pengadaan · 5.2 Manajemen Rantai Pasok.
**Modul 6 — Pemantauan & Pelaporan (6):** 6.1 Dashboard Kinerja & Operasional · 6.2 Dashboard Keuangan & Audit · 6.3 Dashboard Dampak & Kesehatan · 6.4 Dashboard Aspirasi & Media · 6.5 Notifikasi & Peringatan Dini · 6.6 Manajemen Pelaporan (Service Desk).
**Modul 7 — Sistem & Tata Kelola (7, kode SDK):** 7.1 Manajemen Infrastruktur Perkantoran (AMS) · 7.2 Manajemen API · 7.3 Manajemen Pengguna & Hak Akses (SDK-03) · 7.4 Manajemen Kepegawaian (HRIS) · 7.5 Manajemen Pengetahuan & Regulasi (LMS) · 7.6 Manajemen Risiko Pemenuhan Gizi · 7.7 Manajemen Keamanan Sistem.

Kode submodul yang terobservasi di nomor dokumen: `PIP` (Pusat Informasi Program), `PKS-MR` (Manajemen Kerjasama), `PMA-01..05`, `SDK-01..07`. Pola: akronim submodul + indeks.

## 22+1 jenis dokumen kontrol

Per submodul/modul, Peruri menyusun **22 jenis dokumen** + 1 dokumen penutup proyek:

| # | Folder project | Jenis dokumen | Granularitas |
|---|---|---|---|
| 1 | 01 - PRD | Product Requirement Document | per submodul |
| 2 | 02 - FSD | Functional Specification Document | per submodul |
| 3 | 03 - TSD | Technical Specification Document | per submodul |
| 4 | 04 - Implementation Plan | Rencana implementasi | per submodul |
| 5 | 05 - ERD | Entity Relationship Diagram | per submodul |
| 6 | 06 - API Spesification | Spesifikasi API | per submodul |
| 7 | 07 - Environment Setup | Setup lingkungan | per submodul |
| 8 | 08 - UI UX Design | Desain UI/UX | per submodul |
| 9 | 09 - Security Risk Analysis | Analisis risiko keamanan | per submodul |
| 10 | 10 - Playbook User Manual | Buku panduan per ROLE pengguna | per submodul × role (±23 role; lihat ref 08) |
| 11 | 11 - Release Note | Catatan rilis | per submodul |
| 12 | 12 - Version Control Records | Riwayat versi | per submodul |
| 13 | 13 - Root Cause Analysis | RCA insiden/defect | per submodul |
| 14 | 14 - System Integration Testing | Laporan SIT | per submodul |
| 15 | 15 - Bug Fix Report | Laporan perbaikan bug | per submodul |
| 16 | 16 - Incident Report | Incident/Bugs Report Log | per submodul |
| 17 | 17 - Penetration Test Report | Pen test | **per modul** (contoh: "01. Pen Test Modul Promosi dan Kerjasama", "02. ... Modul Distribusi", "03. ... Modul Penerima Manfaat") |
| 18 | 18 - Test Plan | Rencana uji | per submodul |
| 19 | 19 - Security Test Report | Uji keamanan | **per modul** |
| 20 | 20 - UAT Report | User Acceptance Test | per submodul |
| 21 | 21 - Performance Test Report | Uji performa | per submodul/modul |
| 22 | 22 - Change Request Document | CRD | per submodul |
| +1 | 23 - Laporan Final Proyek | **Laporan Final Proyek SIPGN** (`PMO/LFP/SIPGN/XII/2025`, v1.0, 28 Des 2025) — 10 seksi: Ringkasan Eksekutif; Capaian Tujuan & KPI; Varians vs Baseline; Deliverable & Penerima; Kualitas & Hasil Uji; Risiko & Isu Final; Lessons Learned; Rekomendasi Operasional (support plan, monitoring infra, pengembangan); Aset yang Diserahkan; Rencana Pasca Implementasi | per proyek |

Catatan urutan pen test/sec test per modul mengikuti **Skema A** (02 = Distribusi).

## Format nomor & kontrol dokumen

- **Nomor**: `{TYPE}/{KODE-SUBMODUL}/SIPGN/{BULAN-ROMAWI}/{TAHUN}` — contoh `PRD/PMA-01/SIPGN/X/2025`, `PRD/PIP-01/SIPGN/X/2025`, `PMO/LFP/SIPGN/XII/2025`.
- **Header standar**: Nomor Dokumen, Versi, Tanggal Perubahan, **Klasifikasi: Terbatas**.
- **Tabel DOKUMEN KONTROL**: Nama Dokumen | Versi | Tanggal | Log | Oleh (umumnya "Tim Peruri") | Relasi Dokumen (cross-reference antar PRD/submodul terkait — mis. PRD PMA-01 berelasi PMA-02..05 & SDK-03).
- **Struktur isi PRD** (pola umum): Latar Belakang Masalah → Tujuan → Ruang Lingkup → (user stories/kebutuhan, NFR, dependensi...). Daftar isi + daftar tabel/gambar baku.
- Penulis: Tim Peruri; reviewer: BGN (Pusdatin/Tim Aplikasi Bisnis). Mayoritas dokumen tertanggal Okt–Des 2025 (proyek 2025), beberapa CR/penyempurnaan berlanjut 2026; folder 11–23 dimutakhirkan di project per 8–9 Juni 2026.

## Status proyek & keberlanjutan

- Kontrak pengembangan Peruri 2025 ditutup dengan Laporan Final Proyek (Des 2025) → masa support/pemeliharaan + **transfer knowledge ke Pusdatin** (berjalan 2026: handover Data Flow, ERD, dsb.).
- Pembahasan **"SIPGN 2.0"** (proses bisnis target berikutnya) berjalan sejak Mei 2026 di internal BGN.
- Konteks audit nilai proyek IT: lihat ref 06 (Rp550 M + Rp199 M; reviu APIP Rp893,1 M).
- File sumber lengkap (md+pdf per dokumen) tersedia di folder project "Ekosistem Data Gizi Nasional" — kutip nama file persis bila merujuk.
