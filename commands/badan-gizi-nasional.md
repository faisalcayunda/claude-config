---
name: badan-gizi-nasional
description: >-
  Authoritative knowledge base Badan Gizi Nasional (BGN), Makan Bergizi Gratis (MBG), dan Sistem Informasi Pemenuhan Gizi Nasional (SIPGN). Pakai SELALU sebelum menjawab BGN/MBG/SIPGN — operasional (SPPG, KPPG, SPPI, Ka.SPPG, Kreg/Korwil/Korcam, Yayasan mitra, BAST, PKS, VA SPPG), regulasi (Juknis MBG 2026, Kepka 401.1/2025, Perpres 83/2024, 115/2025), program (3B, AKG, HET, 82,9 juta PM, 35.270 SPPG, Generasi Emas 2045), keamanan pangan (SLHS, organoleptik, GMP, Kejadian Menonjol), portal (mitra.bgn.go.id, dialur.bgn.go.id, Tauwas Care), SIPGN (7 modul, 27 aplikasi SCM/ERP/HRIS/POP/MenuPlanner/Kong/SSO, 22 dokumen Peruri PRD/FSD/TSD/ImplPlan/DataMapping/APISpec/EnvSetup/UIUX/SecRisk/Playbook/ReleaseNotes/VerControl/RCA/SIT/UAT/BugFix/Incident/PenTest/TestPlan/PerfTest/SecTest/CRD, CR Gateway data mesh, IoT CCTV/CPUTowerAI/DigitalSignage/PVR/POP), BGN Digital (Pusdatin, INA Digital). Trigger pula "masak makan gratis sekolah", "mitra BGN", "Peruri". JANGAN untuk PKH/BPNT/KIP/PIP/BLT. Baca reference dulu.
license: Public domain (sumber regulasi publik Pemerintah Republik Indonesia) + Confidential (dokumen teknis SIPGN milik BGN Digital × Peruri — skill ini hanya mendokumentasikan struktur, bukan isi konkret akses-terbatas)
allowed-tools: bash, view, str_replace
compatibility:
  models: [claude-opus-4-7, claude-sonnet-4-6, claude-opus-4-6]
  runtime: [claude-code, claude-ai, cowork]
  dependencies:
    - python>=3.10 (untuk scripts/)
    - awk/grep (untuk query CSV master metadata)
metadata:
  version: 3.2.0
  author: BGN Digital Knowledge Base Curator
  last_updated: 2026-04-22
  tags: [bgn, mbg, makan-bergizi-gratis, gizi-nasional, indonesia, sppg, kppg, sipgn, peruri, iot, digital-signage, pvr, pop, cctv, palm-vein-reader, cr-gateway, data-mesh, penerima-manfaat, doc-control, doc-scraped, owasp, sonarqube, defectdojo]
  classification: Public-Information + Structural-Reference
  source_authority: |
    1. Keputusan Kepala BGN Nomor 401.1 Tahun 2025 (Juknis MBG 2026)
    2. Perpres 83/2024 (Pembentukan BGN)
    3. Perpres 115/2025 (Tata Kelola MBG)
    4. Dokumen kontrol Peruri (PRD, TSD, FSD, SIT, UAT, RCA, Release Notes, Playbook) untuk 7 modul SIPGN
    5. Buku Panduan Aplikasi SIPGN & IoT (27 manual aplikasi + 14 manual IoT)
    6. Google Sheet "Doc Control - PERURI" (bgn-peruri.atlassian.net, akses terbatas)
    7. CR Implementation Plan untuk Domain Penerima Manfaat (PEM-CR-IMPL-PLAN-001)
    8. Master Metadata SIPGN (20 apps × 22 DB × 20.192 atribut, scraped 27 Mar 2026)
    9. Referensi organisasi BGN Digital 2026
    10. Hasil scraping "Doc Control - PERURI" (Google Sheet ID 1z6Z7KiPovZUnlQqeGXgbg4eraJbAXAgc6mSgRI7jPIA, 27 tab, 703 dokumen ter-klasifikasi, 10 dokumen sampel ditarik via `get_file_metadata`, 22 Apr 2026)
changelog_summary: |
  v3.2.0 (2026-04-22): SCRAPING PASS — indexed all 703 dokumen kontrol Peruri from Google Sheet "Doc Control - PERURI" (27 tab × ~26 baris). Added ref 28 (`references/28_peruri_doc_scraped_enriched.md`, 457 baris) dengan format penomoran aktual, struktur baku PRD/FSD/TSD/DMD/APISpec/SIT/UAT/PenTest/SecTest/LFP berdasarkan isi dokumen asli, tools stack (SonarQube quality gate A/A/A, DefectDojo, jam.dev), 12 PIC Peruri + INA Digital, hasil OWASP Top 10 Modul 1 (semua PASSED), taksonomi 30 submodul, naming convention `promotion_*` / `sipportal-{area}-{function}-{tier}`. Data mentah tersimpan di `data/master_doc_index.json` (703 entri ter-klasifikasi), `data/team_members.json`, `data/hyperlinks_extracted.json`, `data/doc_control_peruri.xlsx`.
  v3.1.0 (2026-04-22): Added ref 27 (Laporan Final Proyek Termin 3) to routing table. All 27 references now filed on disk and cross-linked. Bonus scripts + templates scaffolded.
  v3.0.0 (2026-04-22): Playbook-aligned rewrite. Added ref 25 (CR Gateway), ref 26 (22 tab deep-dive Doc Control). Slimmed SKILL.md body per progressive-disclosure. Added allowed-tools + compatibility + changelog_summary. Tightened description with explicit trigger/non-trigger phrases.
  v2.1.0 (2026-04-15): Added Master Metadata (ref 22), kontak stakeholder (ref 23), log rapat historical (ref 24).
  v2.0.0 (2026-04-10): Integrated SIPGN 7 modul + 22 dokumen + 27 apps + IoT.
  v1.0.0 (2026-03): Initial release — MBG tata kelola + organisasi BGN.
---
 
# Badan Gizi Nasional (BGN), MBG, dan Ekosistem Digital SIPGN
 
## Overview
 
Skill ini adalah **single source of truth** terstruktur untuk tiga domain yang saling terkait dan sering dibingungkan:
 
1. **MBG (Makan Bergizi Gratis)** — program nasional dengan target ~82,9 juta penerima manfaat via ~35.270 SPPG di 38 provinsi pada TA 2026, untuk mewujudkan **Generasi Emas 2045**.
2. **BGN (Badan Gizi Nasional)** — lembaga setingkat kementerian di bawah Presiden yang menyelenggarakan MBG; terdiri dari Deputi, Direktorat, Pusdatin, BGN Digital; bermitra dengan Peruri (vendor), Gunadarma (akademik), INA Digital (ekosistem).
3. **SIPGN (Sistem Informasi Pemenuhan Gizi Nasional)** — platform digital terintegrasi Peruri yang mengoperasikan MBG end-to-end: 7 modul, 27 aplikasi, 5.000 SPPG ber-IoT, 22 jenis dokumen teknis per modul.
**Sumber otoritas utama:** Kepka BGN 401.1/2025, Perpres 83/2024, Perpres 115/2025, dokumen kontrol Peruri (PRD, TSD, FSD, SIT, UAT, RCA, Release Notes, Playbook), dan Master Metadata SIPGN.
 
## Kapan Menggunakan Skill Ini — dan Kapan Tidak
 
**Gunakan** untuk setiap pertanyaan menyebut: BGN, MBG, SPPG, KPPG, Ka.SPPG, SPPI, Kreg/Korwil/Korcam, penerima manfaat MBG, Yayasan mitra BGN, Peruri, SIPGN, Tauwas Care, mitra.bgn.go.id, dialur.bgn.go.id, 3B, AKG, HET MBG, insentif fasilitas, Juknis MBG 2026, Kepka BGN, Perpres 83/2024, Perpres 115/2025, CR Gateway (BGN), PVR, Digital Signage SIPGN, POP SPPG, Menu Planner AI, dll.
 
**Jangan gunakan** untuk: PKH, BPNT, BLT, KIP, PIP (bukan MBG); sistem pemerintah lain (SAKTI, SIMPONI, ALKI); kementerian di luar ekosistem BGN; konsep gizi umum tanpa kaitan MBG.
 
## Prinsip Kerja
 
1. **Akurasi numerik mutlak.** Angka spesifik (Rp15.000/porsi acuan, Rp8.000/Rp10.000 belanja bahan baku, 35.270 SPPG, 82,9 juta PM, 5.000 SPPG IoT, 25.000 CCTV, 75.000 PVR sekolah, 150 m² luas min SPPG, 52 orang personel maks, 6 km/30 menit radius logistik, 300 ms target response API) adalah fakta spesifik dari Juknis/PRD. **Jangan bulatkan, jangan estimasi, jangan rekonstruksi dari ingatan.** Alasan: satu digit keliru dapat menyebabkan mispersepsi di deck pimpinan atau rapat DPR.
2. **Akurasi terminologi.** BGN ≠ KPPG ≠ SPPG ≠ Yayasan ≠ Peruri ≠ penerima manfaat — semuanya stakeholder berbeda dengan peran berbeda. Salah labeling = salah koordinasi. Periksa glosarium (`references/12_glosarium_istilah.md`) sebelum memakai istilah.
3. **Rujuk regulasi/dokumen eksplisit.** Jawaban "dasar hukum X adalah Pasal Y Juknis Z" lebih berharga dari sekadar "menurut Juknis". Sebutkan nomor regulasi atau nama dokumen (misal: "PRD SIPGN Modul 4 Produksi v1.2").
4. **Pisahkan fakta dari interpretasi.** Jika user berasumsi ("apakah SIPGN sudah go-live di semua provinsi?"), koreksi dengan status aktual. Jangan kompromi akurasi demi afirmasi.
## Routing: Topik → File Reference
 
Identifikasi topik pertanyaan, **baca file reference yang relevan** (boleh multiple), kemudian sintesiskan jawaban.
 
### A. Regulasi & Tata Kelola MBG (Domain Pemerintah)
 
| Topik Pertanyaan | Baca File |
|---|---|
| Dasar hukum, regulasi, Perpres, UU, Kepka BGN | `references/01_regulasi_dan_dasar_hukum.md` |
| Struktur BGN, fungsi KPPG/SPPG, peran Kreg/Korwil/Korcam | `references/02_organisasi_bgn_kppg_sppg.md` |
| Siapa berhak MBG, kelompok sasaran, kriteria 3B | `references/03_penerima_manfaat_dan_sasaran.md` |
| Standar gizi, AKG, kalori/protein, menu, makan pagi vs siang | `references/04_standar_gizi_dan_menu.md` |
| Operasional SPPG, lokasi, bangunan, peralatan, personel, shift | `references/05_operasional_sppg.md` |
| Keamanan pangan, GMP, sanitasi, SLHS, uji organoleptik, food sample | `references/06_keamanan_pangan_gmp_sanitasi.md` |
| Anggaran, pagu, indeks per porsi, HET, VA SPPG, insentif fasilitas | `references/07_anggaran_bantuan_pemerintah.md` |
| Pemantauan, evaluasi, sanksi, SP1/SP2/SP3, Kejadian Menonjol (KM) | `references/08_monev_pengawasan_sanksi.md` |
| Tauwas Care, Dialur, Mitra portal (overview digitalisasi MBG) | `references/09_sistem_informasi_sipgn.md` |
| Koordinasi pusat/provinsi/kecamatan, Camat/Danramil/Kapolsek, Bappenas | `references/10_koordinasi_lintas_sektor.md` |
| Pertukaran data BGN–Kemenkes, SATUSEHAT, NIK balita, FHIR | `references/11_pertukaran_data_kemenkes.md` |
| Glosarium, singkatan, istilah | `references/12_glosarium_istilah.md` |
 
### B. Sistem Informasi Pemenuhan Gizi Nasional (SIPGN)
 
| Topik Pertanyaan | Baca File |
|---|---|
| 7 modul + sub-modulnya, proses bisnis end-to-end, integrasi antar modul | `references/13_sipgn_modul_lengkap.md` |
| Overview 22 dokumen teknis per modul, framework QA TW | `references/14_sipgn_dokumen_kontrol.md` |
| **Deep-dive per tab** (PRD/FSD/TSD/Impl Plan/Data Mapping/API Spec/Env Setup/UI-UX/Sec Risk/Playbook/Release Notes/Ver Control/RCA/SIT/UAT/Bug Fix/Incident/Pen Test/Test Plan/Perf Test/Sec Test/CRD) — struktur standar, common findings audit, PIC Peruri | `references/26_sipgn_dokumen_tabs_deepdive.md` |
| 27 Buku Panduan Aplikasi SIPGN (Rumah SIPGN, SCM, ERP, POP, Menu Planner, KinOps, FinDash, dst) | `references/15_sipgn_buku_panduan_aplikasi.md` |
| IoT perangkat SPPG: CCTV, CPU Tower AI, Digital Signage, PVR (EFIS/HFSecurity/Vizion/Tencent PalmAI/Sentuh/Roomi), POP, Laptop | `references/16_sipgn_iot_perangkat.md` |
| Security SIPGN: RBAC, SSO, Kong Manager, pen test, data classification, PII masking, endpoint security, DR | `references/17_sipgn_keamanan_dan_api.md` |
| **CR Gateway** — data mesh change-request flow antar source-aligned ↔ governance app ↔ consumer-aligned data products (Airflow DAG, update package JSON, callback handler, state machine, SLA) | `references/25_sipgn_cr_gateway_impl.md` |
 
### C. Organisasi BGN Digital & Master Data
 
| Topik Pertanyaan | Baca File |
|---|---|
| Struktur BGN Digital (CDO, Compliance, PMO, klaster), 11 bidang DTO, 141 role, chapter INA Digital | `references/18_organisasi_bgn_digital.md` |
| Timeline kerja 4 fase (Inisiasi → Draf Awal → Validasi → Penyerahan), cascading deliverables | `references/19_timeline_dan_fase_kerja.md` |
| Template Deck BGN (Kepala, Pusdatin, BGN Digital), Visual Design System, Logo 2026 | `references/20_template_deck_bgn.md` |
| Sistem ID Penerima Manfaat (UIN 10 digit, Verhoeff, non-NIK handling, ID Kelompok) | `references/21_sistem_id_penerima_manfaat.md` |
| Master Metadata SIPGN — 20 apps × 22 DB × 20.192 atribut; Bronze/Silver/Gold; query via awk | `references/22_sipgn_master_metadata.md` |
| Kontak PIC Peruri/INA Digital/BGN Pusdatin/Tim Klaster Data, escalation matrix, meeting ritual | `references/23_kontak_stakeholder.md` |
| Log rapat historical Juni–Desember 2025 (111 rapat), audit trail stakeholder | `references/24_log_rapat_historical.md` |
| Laporan Final Proyek Termin 3 — kerangka deliverable closing kontrak Peruri (PIC Widi Utomo + Rian), 8 seksi, kriteria BAST Final | `references/27_laporan_final_proyek_t3.md` |
| **Hasil scraping aktual Doc Control - PERURI** — 703 dokumen diindeks, format nomor `{TYPE}/{MOD-CODE}-{SUB}/SIPGN/{MONTH-ROMAN}/{YEAR}`, struktur standar PRD/FSD/TSD/DMD/APISpec/SIT/UAT/PenTest/SecTest/LFP (sampel aktual), tools stack (SonarQube, DefectDojo, jam.dev), 12 PIC (Peruri + INA Digital), hasil OWASP Modul 1 (PASSED all 10), quality gate Sonar A/A/A. Dibuat dari file asli ter-download dan `get_file_metadata` | `references/28_peruri_doc_scraped_enriched.md` + `data/master_doc_index.json` |
 
Untuk pertanyaan holistik ("jelaskan SIPGN secara lengkap"), baca beberapa file dan sintesiskan.
 
## Quick Reference: Fakta-Fakta Kunci
 
### Tabel 1: MBG & BGN (Program & Regulasi)
 
| Topik | Fakta |
|---|---|
| Nama program | Makan Bergizi Gratis (MBG) |
| Lembaga penyelenggara | Badan Gizi Nasional (BGN) — di bawah Presiden RI |
| Dasar pembentukan BGN | Perpres 83 Tahun 2024 |
| Dasar tata kelola MBG | Perpres 115 Tahun 2025 |
| Petunjuk Teknis 2026 | Kepka BGN No. 401.1 Tahun 2025 |
| Tanggal mulai MBG | 6 Januari 2025 |
| Target SPPG 2026 | ~35.270 (termasuk Aglomerasi & Terpencil) |
| Target penerima manfaat | ~82,9 juta orang, 38 provinsi |
| Visi jangka panjang | Generasi Emas 2045 |
| Frekuensi pemberian | Senin–Sabtu, kecuali libur |
| Waktu makan pagi / siang | 06.00–09.00 (20–25% AKG) / 11.00–14.00 (30–35% AKG) |
| Acuan pagu/porsi | Rp15.000/orang |
| Pagu bahan baku PAUD/TK/SD 1–3/Balita | Rp8.000/orang |
| Pagu bahan baku SD 4–6/SMP/SMA/Pendidik/3B | Rp10.000/orang |
| Acuan biaya operasional | Rp3.000/orang |
| Insentif fasilitas SPPG | Rp6.000.000/hari (availability-based) |
| Radius SPPG standar | Max 6 km / 30 menit |
| Kapasitas SPPG standar | ≤2.500 PM (≤3.000 dengan Jurutama BNSP) |
| Luas min. SPPG | 150 m² |
| Personel maks. SPPG | 52 orang |
| Food sample per batch | 2 porsi, disimpan 3 hari |
| Standar gizi | AKG Permenkes 28/2019 |
 
### Tabel 2: SIPGN (Sistem, Modul, Dokumen)
 
| Topik | Fakta |
|---|---|
| Nama sistem | Sistem Informasi Pemenuhan Gizi Nasional (SIPGN) |
| Pengembang | PT Peruri (Peruri Digital) |
| Pengawas Teknis | BGN Digital Tim Aplikasi Bisnis |
| 7 Modul | Promosi-Kerjasama, Penerima Manfaat, Pengadaan, Produksi, Distribusi, Pemantauan-Pelaporan, Tata Kelola-Sistem |
| 22 Dokumen per Modul | PRD, FSD, TSD, Impl Plan, Data Mapping, API Spec, Env Setup, UI/UX, Sec Risk, Playbook, Release Notes, Ver Control, RCA, SIT, UAT, Bug Fix, Incident Log, Pen Test, Test Plan, Perf Test, Sec Test, CRD |
| Aplikasi SIPGN (27) | Rumah SIPGN, SIPGN Distribusi (Web+Mobile), Penerima Manfaat, Produksi, Menu Planner AI, SCM, ERP, HRIS, AMS, LMS, Service Desk, Manrisk, Geotag, Man. Limbah, AI Surveillance, KinOps, FinDash, Dampak-Kesehatan, Aspirasi-Media, Notifikasi, Kong Manager, Huawei Cloud, SSO, Mobile MBG, Fleet, Core API |
| Target IoT deployment | 5.000 SPPG: 25.000 CCTV (5/SPPG) + 5.000 CPU Tower AI + 5.000 Digital Signage + 80.000 PVR (5.000 dapur + 75.000 sekolah × 15) + 5.000 POP + 5.000 Laptop |
| Portal pendaftaran mitra | https://mitra.bgn.go.id |
| Portal operasional | https://dialur.bgn.go.id |
| Aplikasi pengawasan | Tauwas Care (internal BGN) |
| Go-live SIPGN | 9 Februari 2026 |
| Identity | Keycloak (SSO) |
| API Gateway | Kong Manager |
| Environment | Alpha → Staging → Production (Huawei Cloud Indonesia region, private) |
| NFR response time | 300 ms target, 10 s max tolerable (dianggap terlalu lama oleh audit TW) |
| NFR load capacity | 250 VU baseline (perlu scale ke 5.000 titik) |
| Dokumen control canonical | Google Sheets "Doc Control - PERURI" (akses VPN+auth via bgn-peruri.atlassian.net) |
 
## Prinsip Menjawab: Plan-Verify-Answer
 
1. **Plan.** Identifikasi topik utama; tentukan file reference mana dibaca. "Pertanyaan ini tentang [topik] → saya baca [file X, Y]."
2. **Verify.** Baca file reference. Jangan menjawab dari ingatan Quick Reference saja kecuali pertanyaan sepersis itu.
3. **Answer.** Jawab berstruktur. Untuk kompleks: heading + tabel. Selalu cite sumber regulasi/dokumen eksplisit (Pasal Juknis, nama dokumen PRD/TSD).
4. **Caveat saat uncertain.** Jika pertanyaan menyentuh area tidak diatur eksplisit (status terkini SIPGN per provinsi), nyatakan keterbatasan knowledge base.
## Examples (Input → Thinking → Output)
 
**Example 1 — Pertanyaan Faktual:**
> **Input:** Berapa target SPPG MBG tahun 2026?
> **Thinking:** Angka ada di Quick Reference Tabel 1. Validasi dengan ref 02 untuk konteks tipe SPPG.
> **Output:** Target TA 2026 adalah **~35.270 SPPG** (termasuk Standar, Aglomerasi, Terpencil) di 38 provinsi untuk ~82,9 juta PM. Angka dapat menyesuaikan dengan arahan Presiden (Kepka BGN 401.1/2025, Bab 1 Sub-bab 1.2).
 
**Example 2 — Pertanyaan SIPGN Struktural:**
> **Input:** Apa isi PRD SIPGN dan siapa yang bikin?
> **Thinking:** User tanya struktur dokumen PRD. Baca ref 26 (deep-dive tab PRD) + ref 14 (overview).
> **Output:** [Ringkasan struktur standar PRD: Document Control, Problem Statement, Objectives, User Stories, Acceptance Criteria, NFR, Dependencies, dll. PIC: Tim Aplikasi Bisnis Peruri. 7 PRD minimum (satu per modul). Link canonical: Google Sheets "Doc Control - PERURI" tab PRD, akses via Confluence BGN-Peruri.]
 
**Example 3 — Pertanyaan CR Gateway:**
> **Input:** Bagaimana alur `penerima_manfaat_id` diterbitkan dari source-aligned ke Master Data PM?
> **Thinking:** Topik CR Gateway data mesh. Baca ref 25 (CR Gateway Impl).
> **Output:** [Sequence flow: Dapodik → Gold UPSERT → DQ PASS → `dag_cr_create_batch` → POST update package → governance app → Human-in-the-Loop Data Steward review → callback APPROVED dengan `id_assignments` → writeback ke Gold → consumer-aligned consume via REST API delta. State machine: PENDING → APPROVED/REJECTED. SLA: PENDING >24 jam = alert High.]
 
**Example 4 — Pertanyaan Kompleks Multi-Topik:**
> **Input:** Saya yayasan mau daftar jadi mitra SPPG. Apa syaratnya, berapa SPPG yang bisa saya kelola, alur pendanaan, aplikasi apa yang K.SPPG saya pakai?
> **Thinking:** 4 topik — pendaftaran mitra (ref 02), kuota yayasan (ref 02+05), pendanaan (ref 07), aplikasi K.SPPG (ref 15).
> **Output:** [Struktur jawaban dengan heading per topik + referensi dokumen eksplisit.]
 
## Critical Rules
 
- **JANGAN** menyebutkan angka/tanggal/nomor regulasi/versi aplikasi dari ingatan tanpa verifikasi reference — risiko hallucination tinggi pada detail spesifik.
- **JANGAN** mencampur MBG dengan bansos lain (PKH, BPNT, KIP, PIP) — mereka bukan bagian BGN.
- **JANGAN** memberikan legal opinion tentang sanksi. Sebutkan saja yang tertulis di Juknis; interpretasi hukum → PPK BGN atau Inspektorat Utama.
- **JANGAN** memberi saran finansial apakah sebaiknya jadi mitra BGN. Sediakan fakta; keputusan finansial ada pada user.
- **JANGAN** bocorkan credential, password, API key, akun demo SIPGN. Redirect ke PIC resmi (Pusdatin/Peruri).
- **JANGAN** menganggap status "Sesuai"/"Tidak Sesuai" di daftar buku panduan sebagai permanen — itu snapshot audit tertentu; status terkini di repository aktif.
- **SELALU** beri disclaimer saat data mungkin perlu update (HET, versi aplikasi, status go-live fase). Juknis menyatakan HET merujuk Pemda + survei mingguan.
- **SELALU** jelaskan perbedaan: **BGN** (pusat kebijakan) vs **KPPG** (provinsi/kabupaten koordinasi) vs **SPPG** (kecamatan operasional). Sering salah kaprah.
- **SELALU** bedakan: **Yayasan/Mitra** (swasta non-profit penerima bantuan) vs **BGN** (pemerintah pemberi) vs **Peruri** (vendor sistem) vs **Penerima Manfaat** (end-user makanan).
- **SELALU** bedakan **modul** (kategori fungsional Promosi/PM/Pengadaan/Produksi/Distribusi/Monev/TataKelola) dari **aplikasi** (SCM, ERP, HRIS, POP, PVR sbg implementasi konkret).
- **JIKA** user bertanya data individu PM (NIK spesifik), arahkan ke mekanisme resmi BGN — jangan memproses data individu di skill.
- **JIKA** user melaporkan Kejadian Menonjol aktual (keracunan), prioritaskan kontak darurat: SPPG/KPPG setempat, Puskesmas, BGN Pusat. Jangan fokus ke prosedur administratif dulu.
## Error Recovery
 
| Situasi | Tindakan |
|---|---|
| Regulasi spesifik tak ada di reference | "Diatur di Pedoman Teknis tersendiri per catatan Juknis, tidak di knowledge base ini." |
| User menyebut angka kontradiksi dengan Juknis/PRD | Koreksi sopan dengan sumber: "Menurut Juknis 2026, angkanya X, bukan Y." |
| User minta prediksi masa depan | "Knowledge base ini TA 2026. Untuk update, rujuk portal resmi BGN atau Confluence SIPGN." |
| Pertanyaan sensitif/fitnah tentang program/figur publik | Sajikan fakta netral dari Juknis/dokumen resmi tanpa opini. |
| File reference tidak tersedia / error baca | Nyatakan keterbatasan; jawab dari Quick Reference dengan caveat. |
| User minta link download app SIPGN atau dokumen PRD | "Akses aplikasi dan dokumen kontrol PRD terbatas via Confluence Bgn-Peruri / distribusi resmi Pusdatin. Tidak ada direct-download di skill ini." |
| User ingin konten tab Google Sheets canonical | Pointer ke ref 26 untuk struktur; nyatakan bahwa isi live memerlukan akses VPN+auth Confluence. |
 
## Scripts Tersedia
 
Script deterministik untuk kalkulasi/validasi berulang (jalankan via bash, jangan hitung manual):
 
- `scripts/calculate_mbg_budget.py` — Hitung kebutuhan anggaran mingguan/bulanan SPPG berdasarkan komposisi PM.
- `scripts/validate_sppg_location.py` — Validasi usulan lokasi SPPG terhadap 13+ kriteria teknis Juknis.
- `scripts/nutrition_requirement.py` — Lookup kebutuhan gizi (kalori/protein/lemak/karbohidrat) per kelompok sasaran.
- `scripts/verhoeff_checksum.py` — Generate/validasi UIN 10-digit PM dengan algoritma Verhoeff.
- `scripts/sipgn_doc_checklist.py` — Generate checklist 22 dokumen teknis per modul SIPGN.
## Template Tersedia (`assets/templates/`)
 
- `BAST_template.md` — Berita Acara Serah Terima (kerangka)
- `PKS_template.md` — Perjanjian Kerja Sama BGN–Yayasan (kerangka)
- `laporan_2mingguan.md` — Laporan pertanggungjawaban 2-mingguan SPPG
- `deck_outline_bgn_pusdatin.md` — Outline deck formal tema Pusdatin/BGN Digital
- `sipgn_doc_control_checklist.md` — Checklist 22 dokumen kontrol per modul SIPGN
Gunakan hanya bila user meminta draft dokumen.
 
## Versioning & Update
 
- Knowledge base mencerminkan **TA 2026** dan kondisi SIPGN per April 2026.
- Regulasi BGN di-update per TA → untuk TA 2027+, bandingkan dengan Kepka BGN terbaru.
- Status aplikasi SIPGN berubah sprint-by-sprint → rujuk Confluence/Atlassian untuk status live.
- Perubahan skill ini tercatat di `CHANGELOG.md`.
## Referensi Otoritatif
 
### Regulasi Pemerintah
1. Kepka BGN No. 401.1 Tahun 2025 — Juknis MBG 2026 (sumber utama)
2. Perpres 83/2024 — Badan Gizi Nasional
3. Perpres 115/2025 — Tata Kelola MBG
4. Permenkes 28/2019 — AKG
5. PP 86/2019 — Keamanan Pangan
6. Perbangnas BGN 1/2/6 Tahun 2024 (OTK BGN, KPPG, Banper)
7. Keppres 28/2025 — Tim Koordinasi MBG
8. SE Kepka BGN 3/2025 — Sinkronisasi PM
9. UU 27/2022 — PDP
10. Draft Juknis Pertukaran Data Kemenkes–BGN (2026)
### Dokumen Teknis SIPGN (Peruri)
11. PRD, FSD, TSD — 7 modul
12. Implementation Plan, Data Mapping, API Specification, Environment Setup, UI/UX Design Spec
13. Security Risk Analysis, Penetration Test, Performance Test, Security Test, Test Plan
14. SIT Report, UAT Report
15. Release Notes, Version Control, RCA, CRD, Bug Fix, Incident/Bug Report Log
16. Playbook / User Manual (27 apps + 14 IoT devices)
17. Master Metadata SIPGN
18. CR Implementation Plan (PEM-CR-IMPL-PLAN-001)
### Portal & Aplikasi
- Portal mitra: https://mitra.bgn.go.id
- Portal operasional: https://dialur.bgn.go.id
- Aplikasi pengawasan: Tauwas Care (internal BGN)
- Repository SIPGN: Confluence Bgn-Peruri (https://bgn-peruri.atlassian.net)
- Official BGN: https://www.bgn.go.id
- Doc Control canonical (Google Sheet): akses via Confluence BGN-Peruri, butuh VPN + authorized credential
Semua URL resmi BGN berakhiran `.bgn.go.id`. untuk skill tentang Badan Gizi Nasional
