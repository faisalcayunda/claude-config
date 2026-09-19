---
name: badan-gizi-nasional
description: >-
  Knowledge base Badan Gizi Nasional (BGN), program Makan Bergizi Gratis (MBG), SIPGN, dan ekosistem data Pusdatin/BGN Digital. Pakai SELALU bila query menyebut entitas BGN/MBG/SIPGN; menang atas skill data umum jika konteksnya BGN — regulasi (Juknis MBG 2026/Kepka 401.1, Perpres 83/2024 & 115/2025, PerBGN 1-7/2026), operasional (SPPG, KPPG, SPPI, yayasan mitra, VA SPPG, BAST, PKS, insentif, suspend), gizi & keamanan pangan (AKG, 3B, SLHS, organoleptik, Kejadian Menonjol), SIPGN (7 modul, 31 submodul, 22+1 dokumen Peruri, IoT CCTV/PVR/POP/Signage, Kong, SSO), portal (mitra/dialur/sipgn.bgn.go.id, Tauwas Care, SAGI 127), ekosistem data (Data Mesh Pusdatin, MDM Penerima Manfaat, KPM, MPM, SMO, Pormit, MonSAKTI, Dapodik/EMIS, OpenMetadata BGN, dashboard SCM/Kinops/Organoleptik, issue Jira/template narasi SIPGN), dan dinamika 2026 (pergantian Kepala BGN, moratorium, refocusing). Trigger pula: "masak/dapur makan gratis sekolah", "mitra BGN", "keracunan MBG". JANGAN untuk PKH/BPNT/KIP/PIP/BLT. Baca references/ dulu.
license: >-
  Konten regulasi = dokumen publik Pemerintah RI; struktur dokumen teknis SIPGN
  didokumentasikan tanpa memuat isi rahasia (dokumen sumber berklasifikasi Terbatas).
compatibility: Dirancang untuk Claude Code/Cowork/claude.ai. scripts/ butuh python>=3.9 (stdlib saja).
metadata:
  version: 4.1.0
  last_updated: 2026-06-10
  description_optimized: trigger-eval 32 query, holdout F1 1.000 (2026-06-10)
  knowledge_cutoff: 2026-06-10
  author: Tim Data Pusdatin BGN / BGN Digital (kurasi)
  tags: [bgn, mbg, sipgn, sppg, kppg, gizi, peruri, pusdatin, data-mesh, penerima-manfaat, iot, juknis-2026]
---

# Badan Gizi Nasional (BGN), MBG, SIPGN & Ekosistem Data

## Overview

Skill ini adalah single source of truth untuk empat domain yang saling terkait dan sering dibingungkan:

1. **MBG (Makan Bergizi Gratis)** — program prioritas nasional (mulai 6 Jan 2025) menuju Generasi Emas 2045; TA 2026 ditargetkan ~82,9 juta penerima manfaat via SPPG di 38 provinsi (per Juni 2026: ±29,7 ribu SPPG, 63,1 juta PM, dengan moratorium SPPG baru).
2. **BGN (Badan Gizi Nasional)** — lembaga pemerintah di bawah Presiden (Perpres 83/2024) penyelenggara MBG. Kepala BGN per Juni 2026: **Nanik S. Deyang** (menggantikan Dadan Hindayana, dicopot 2 Juni 2026).
3. **SIPGN (Sistem Informasi Pemenuhan Gizi Nasional)** — platform digital MBG yang dibangun Peruri (GovTech) bersama Pusdatin BGN: 7 modul, 31 submodul, 22+1 jenis dokumen teknis, IoT dapur, portal publik sipgn.bgn.go.id.
4. **Ekosistem Data BGN Digital/Pusdatin** — Data Mesh, master data Penerima Manfaat/KPM/SPPG, dashboard eksekutif, integrasi Dapodik/EMIS/MonSAKTI/VA Himbara.

**PENTING — kebaruan data:** knowledge base ini di-freeze **10 Juni 2026** di tengah periode sangat dinamis (pergantian pimpinan, kasus hukum berjalan, moratorium baru berumur ~1 minggu). Untuk klaim tentang "kondisi terkini" setelah tanggal itu, verifikasi via web search/portal resmi sebelum menjawab, dan nyatakan tanggal validitas fakta.

## Kapan Menggunakan — dan Kapan Tidak

**Gunakan** untuk pertanyaan menyebut: BGN, MBG, SPPG, KPPG, Ka.SPPG, SPPI, yayasan mitra, penerima manfaat MBG, 3B, AKG, HET, insentif fasilitas, VA SPPG, Juknis/Kepka BGN, Perpres 83/2024, Perpres 115/2025, PerBGN 2026, SIPGN, Peruri, Pusdatin BGN, Tauwas Care, SAGI 127, mitra/dialur/sipgn.bgn.go.id, SMO, Pormit, MPM, KPM, Kinops, Menu Planner, CR Gateway, PVR, POP, Digital Signage dapur, keracunan MBG, moratorium SPPG, dan ekosistem data BGN (Data Mesh, MDM PM, MonSAKTI, OpenMetadata BGN).

**Jangan gunakan** untuk: PKH, BPNT, BLT, KIP, PIP (bansos lain, bukan BGN); sistem K/L lain (SAKTI, SIMPONI) kecuali sebagai sumber data integrasi; konsep gizi umum tanpa kaitan MBG.

## Prinsip Kerja

1. **Akurasi numerik mutlak.** Angka (Rp15.000 rata-rata/hari, Rp13.000 pagu balita–SD kelas 3, Rp8.000/Rp10.000 acuan dasar bahan baku, Rp6.000.000/hari insentif, 313 hari, radius 6 km/30 menit, 2.500→3.000 PM, 82,9 juta target, Rp268 T pagu 2026) adalah fakta dari Juknis/berita resmi. Jangan bulatkan, jangan rekonstruksi dari ingatan — baca reference-nya.
2. **Akurasi temporal.** Banyak fakta berubah sepanjang 2026 (Kepala BGN, jumlah SPPG, status portal mitra, kebijakan 5 vs 6 hari). Selalu sebutkan per-tanggal-kapan suatu fakta berlaku. Bedakan "teks Juknis" vs "kebijakan berjalan".
3. **Akurasi terminologi.** BGN ≠ KPPG ≠ SPPG ≠ yayasan ≠ Peruri ≠ PM. Modul SIPGN punya DUA skema penomoran (lihat ref 07) — selalu klarifikasi skema mana yang dipakai user. "3B" = ibu hamil, ibu menyusui, balita (bukan slogan gizi).
4. **Rujuk sumber eksplisit.** "Juknis 2026 Bab 3.1.6" lebih berharga daripada "menurut Juknis". Sebut nomor dokumen Peruri (mis. `PRD/PMA-01/SIPGN/X/2025`) bila relevan.
5. **Pisahkan fakta dari interpretasi.** Koreksi asumsi keliru user dengan sopan + sumber. Jangan kompromi akurasi demi afirmasi.

## Routing: Topik → File Reference

Identifikasi topik, **baca file reference yang relevan** (boleh beberapa), lalu sintesiskan.

| Topik | Baca |
|---|---|
| Dasar hukum, Perpres, Kepka, PerBGN, SE, juknis/pedoman per topik | `references/01_regulasi.md` |
| Struktur BGN, pimpinan (sejarah & terkini), deputi, KPPG/SPPG/SPPI, Pusdatin/BGN Digital, Peruri | `references/02_organisasi_kelembagaan.md` |
| Siapa berhak MBG, 3B, Dapodik/EMIS/NPSN/NISN, AKG, menu, jadwal makan & hari distribusi | `references/03_penerima_manfaat_dan_gizi.md` |
| Operasional SPPG: lokasi, kapasitas, personel, keamanan pangan, SLHS, organoleptik, sanksi/suspend, akreditasi | `references/04_operasional_sppg_keamanan_pangan.md` |
| Anggaran, pagu per porsi, at cost/HET, insentif, VA & pencairan, pagu APBN 2026 | `references/05_anggaran_dan_pendanaan.md` |
| Peristiwa 2026: keracunan, korupsi, pergantian kepala, moratorium, refocusing, krisis pencairan | `references/06_dinamika_2026.md` |
| SIPGN: 7 modul & 31 submodul, dua skema penomoran, 22+1 dokumen Peruri, format nomor dokumen | `references/07_sipgn_modul_dan_dokumen.md` |
| Aplikasi & portal SIPGN/BGN, role pengguna, IoT (CCTV/PVR/POP/Signage), SSO/Kong, kanal aduan | `references/08_sipgn_aplikasi_portal_iot.md` |
| Ekosistem data: Data Mesh Pusdatin, MDM PM/KPM, master metadata, dashboard, integrasi data, CR Gateway | `references/09_ekosistem_data_bgn_digital.md` |
| Istilah, singkatan, disambiguasi (3B, SMO, Pormit, MPM/KPM/PM, kode submodul) | `references/10_glosarium.md` |

Pertanyaan holistik ("jelaskan SIPGN lengkap") → baca beberapa file sekaligus. Pertanyaan kondisi terkini pasca 10 Juni 2026 → reference + web search.

## Quick Reference (validasi per 10 Juni 2026)

### MBG & BGN

| Topik | Fakta |
|---|---|
| Dasar pembentukan BGN / tata kelola MBG | Perpres 83/2024 / Perpres 115/2025 |
| Juknis TA 2026 | Kepka BGN No. 401.1/2025 (berlaku, belum direvisi) |
| Kepala BGN | Nanik S. Deyang (sejak 2–8 Juni 2026); sebelumnya Dadan Hindayana (dicopot, tersangka korupsi) |
| Mulai MBG | 6 Januari 2025 |
| Target TA 2026 | ~82,9 juta PM, 38 provinsi (BGN: "berpotensi tak tercapai"; refocusing) |
| Realisasi 31 Mei 2026 | 63,13 juta PM; 29.679 SPPG; serapan Rp88,15 T |
| Status SPPG baru | **Moratorium** + portal mitra ditutup (Juni 2026) |
| Pagu APBN MBG 2026 | Rp268 T (Rp67 T dana cadangan dihapus Mei 2026) |
| Hari distribusi | Juknis: 6 hari (Senin–Sabtu), 313 hari/tahun; kebijakan Mar 2026: 5 hari sekolah — sebut keduanya |
| Makan pagi / siang | 06.00–09.00 (20–25% AKG) / 11.00–14.00 (30–35% AKG); AKG = Permenkes 28/2019 |
| 3B | Ibu hamil, ibu menyusui, balita (≥6 bulan–<5 tahun) |
| Pagu bantuan | Rata-rata Rp15.000/PM/hari (bahan baku + operasional at cost + insentif); balita/PAUD/TK/RA/SD 1–3 maks Rp13.000 |
| Acuan dasar bahan baku | Rp8.000 (balita–SD 1–3) / Rp10.000 (SD 4–6 s.d. SMA, santri, pendidik, tendik, bumil, busui) — merujuk HET/survei 3 penyedia |
| Insentif fasilitas SPPG | Rp6.000.000/hari (6 hari/minggu), tak tergantung jumlah PM, 2 tahun sejak operasional |
| Kapasitas SPPG | ≤2.500 PM (≤2.000 peserta didik); dengan Jurutama Masak BNSP ≤3.000 |
| Radius layanan | maks 6 km dan/atau 30 menit |
| Keracunan (kumulatif per 10 Mei 2026) | 445 kejadian, 37.673 korban — kasus tunggal terbesar SMAN 2 Kudus (Jan 2026) |
| Suspensi SPPG | Gelombang: 62 (Mar) → 1.780 (21 Apr) → 1.152 masih disuspend (25 Mei) |

### SIPGN & Ekosistem Data

| Topik | Fakta |
|---|---|
| Pengembang / pengawas | Peruri (GovTech, penunjukan langsung — disorot audit) / Pusdatin BGN (BGN Digital) |
| Nilai proyek | Aplikasi SIPGN Rp550 M + managed service IoT Rp199 M (klarifikasi BGN, Apr 2026) |
| 7 Modul (penomoran dokumen Peruri) | 1 Promosi & Kerjasama · 2 Logistik/Distribusi · 3 Penerima Manfaat · 4 Produksi · 5 Pengadaan/Supply Chain · 6 Pemantauan & Pelaporan · 7 Sistem & Tata Kelola — total 31 submodul (ada skema penomoran alternatif; lihat ref 07) |
| Dokumen teknis | 22 jenis per submodul/modul + Laporan Final Proyek (`PMO/LFP/SIPGN/XII/2025`); format nomor `{TYPE}/{KODE-SUBMODUL}/SIPGN/{BULAN-ROMAWI}/{TAHUN}` |
| Portal publik | sipgn.bgn.go.id/public; dokumentasi portal-doc-sipgn.bgn.go.id; apps Android "SIPGN Produksi" & "SIPGN Distribusi" |
| Portal operasional | dialur.bgn.go.id (SMO); mitra.bgn.go.id (Pormit — pendaftaran DITUTUP per Juni 2026) |
| Pengawasan & aduan | Tauwas Care (internal Ka.SPPG); publik: SAGI call center 127, WA 0811-1000-8008, SP4N bgn.lapor.go.id; "Jaga Dapur MBG" (dgn Kejagung) |
| Identity / API gateway | SSO Keycloak (XPASS Peruri) / Kong Manager |
| Master Metadata SIPGN | snapshot 27 Mar 2026: ±20 aplikasi × 22 DB × ±20.300 baris atribut |
| Data ekosistem | Data Mesh Pusdatin; MDM Penerima Manfaat & KPM (kode KPM = NPSN); sumber: Dapodik, EMIS Kemenag, MonSAKTI, Bapanas, VA 5 Bank Himbara |

## Prinsip Menjawab: Plan–Verify–Answer

1. **Plan.** Identifikasi topik → tentukan file reference.
2. **Verify.** Baca reference. Quick Reference hanya untuk jawaban sependek tabelnya; selebihnya wajib baca file.
3. **Answer.** Struktur jelas; cite sumber eksplisit (bab Juknis, nomor PerBGN, nomor dokumen Peruri, tanggal berita).
4. **Stamp & caveat.** Cantumkan tanggal validitas untuk fakta dinamis; tawarkan verifikasi web untuk kondisi terkini.

## Contoh

**1 — Faktual:** "Berapa pagu MBG per porsi?" → ref 05 → "Rata-rata Rp15.000/PM/hari mencakup bahan baku + operasional (at cost, rujukan HET) + insentif fasilitas; khusus balita/PAUD/TK/RA/SD 1–3 pagu maksimal Rp13.000 (Juknis 2026, Bab 3.1.6). Acuan dasar belanja bahan baku Rp8.000/Rp10.000 per kelompok."

**2 — Temporal:** "Berapa SPPG sekarang?" → ref 06 → "Per 31 Mei 2026: 29.679 SPPG (63,13 juta PM). Target Juknis ~35.270, namun sejak awal Juni 2026 berlaku moratorium SPPG baru. Setelah 10 Juni 2026 angka bisa berubah — mau saya cek berita terbaru?"

**3 — SIPGN struktural:** "PRD submodul pendaftaran PM nomornya berapa?" → ref 07 → "`PRD/PMA-01/SIPGN/X/2025` — Modul Penerima Manfaat, Submodul Pendaftaran & Pengelolaan Data Penerima (v1.0, 12 Des 2025, Tim Peruri); berelasi dgn PMA-02..05 dan SDK-03."

**4 — Multi-topik (yayasan calon mitra):** syarat (ref 04) + status pendaftaran TUTUP (ref 06/08) + pendanaan (ref 05) + aplikasi Ka.SPPG (ref 08). Jangan beri saran finansial — sajikan fakta.

## Critical Rules

- **JANGAN** menjawab angka/tanggal/nomor regulasi dari ingatan tanpa membaca reference — risiko halusinasi tinggi.
- **JANGAN** menyatakan Dadan Hindayana sebagai Kepala BGN (dicopot 2 Juni 2026) — kecuali konteks historis, beri keterangan periode.
- **JANGAN** mencampur MBG dengan bansos lain (PKH/BPNT/KIP/PIP) atau menyebut MBG "bansos" tanpa kualifikasi (skema resminya Bantuan Pemerintah kepada Penerima Bantuan/yayasan).
- **JANGAN** beri legal opinion sanksi/kasus hukum berjalan; sajikan fakta tertulis + status "praduga tak bersalah" untuk tersangka.
- **JANGAN** beri saran finansial jadi/tidaknya mitra; sajikan fakta (apalagi saat moratorium).
- **JANGAN** bocorkan kredensial, akun demo, isi dokumen klasifikasi Terbatas di luar struktur yang sudah publik.
- **JANGAN** memproses data pribadi PM (NIK dsb.) — arahkan ke mekanisme resmi BGN (UU 27/2022 PDP).
- **SELALU** bedakan BGN (pusat) vs KPPG (UPT layanan) vs SPPG (unit dapur) vs yayasan (penerima bantuan) vs Peruri (vendor) vs PM (penerima makanan).
- **SELALU** bedakan modul vs submodul vs aplikasi vs dokumen; dan dua skema penomoran modul (ref 07).
- **JIKA** user melaporkan keracunan/Kejadian Menonjol aktual: prioritaskan keselamatan — Puskesmas/118, lalu Ka.SPPG/KPPG, SAGI 127; administrasi belakangan.
- **JIKA** ditanya kondisi pasca 10 Juni 2026: baca ref 06 untuk baseline, lalu tawarkan/lakukan web search.

## Error Recovery

| Situasi | Tindakan |
|---|---|
| Topik tak tercakup reference | Nyatakan keterbatasan; arahkan ke Juknis lengkap (folder regulasi project / jdih.bgn.go.id) |
| Angka user kontradiksi Juknis | Koreksi sopan + kutip bab/halaman |
| Fakta mungkin sudah berubah | Beri fakta + tanggal validitas + tawarkan web search |
| Reference file gagal dibaca | Jawab dari Quick Reference DENGAN caveat eksplisit |
| Minta isi dokumen Terbatas | Berikan struktur/metadata yang sudah publik saja; akses isi via kanal resmi BGN–Peruri |

## Scripts (`scripts/`)

Jalankan via bash; jangan hitung manual:

- `calculate_mbg_budget.py` — proyeksi kebutuhan bantuan SPPG per komposisi PM (acuan Juknis 2026: 8k/10k/13k/15k + insentif). `python3 scripts/calculate_mbg_budget.py --help`
- `verhoeff_checksum.py` — generate/validasi check digit (algoritma Verhoeff) untuk ID numerik (mis. UIN PM 10 digit).
- `sipgn_doc_checklist.py` — generate checklist 22+1 dokumen kontrol per modul/submodul SIPGN.

## Assets (`assets/templates/`)

- `laporan_2mingguan.md` — kerangka laporan pertanggungjawaban 2-mingguan SPPG (sesuaikan lampiran Juknis).
- `sipgn_doc_control_checklist.md` — checklist kelengkapan dokumen kontrol per submodul.

## Versioning

- v4.0.0 merefleksikan kondisi per **10 Juni 2026**; regulasi inti TA 2026.
- Fakta paling rawan kedaluwarsa: pimpinan BGN, jumlah SPPG/PM, status moratorium & portal, status hukum kasus, kebijakan Nanik (banyak baru berupa pengumuman, belum regulasi).
- Riwayat perubahan: `CHANGELOG.md`.
