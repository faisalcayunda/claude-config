# Ekosistem Data BGN Digital / Pusdatin (per Juni 2026)

> Konteks: Tim Data Pusdatin BGN (BGN Digital) mengelola arsitektur data MBG/SIPGN pasca-handover Peruri. Payung regulasi: **PerBGN 7/2026 — Satu Data Pemenuhan Gizi Nasional** (+ UU 27/2022 PDP). Sumber file ini: log kerja Tim Data Apr–Mei 2026, artefak project, dokumen CR.

## Arsitektur: Data Mesh

- Paradigma **Data Mesh** dgn federated governance: domain → data product, masing-masing punya dokumentasi baku (Data Product Canvas, **Data Contract**, API Brief, data vocabulary **G-01**, data dictionary **G-03**), direktori terpusat (**Data Mesh Directory** sebagai landing page seluruh domain & data product), dan template repo dokumentasi markdown (sink Google Drive ↔ Confluence ↔ Docusaurus; deploy di domain bgn.go.id sejak Mei 2026).
- **Katalog & metadata**: OpenMetadata (terpusat); data vocabulary per modul (contoh nyata: G-01 Fleet/Distribusi `mbg-fleet-distribusi-v1`, v0.1.0, 13 Mei 2026, pii_flag true); Master Metadata SIPGN (snapshot 27 Mar 2026: ±20 aplikasi × 22 database × ±20.300 baris atribut — file `Master Metadata SIPGN.xlsx`).
- **Lapisan data**: medallion Bronze/Silver/Gold; DWH (deployment RDS production per Mei 2026); query federation **TrinoDB**; alur kerja JIRA terotomasi saat data product baru dibuat; CI/CD pipeline dokumentasi; Capacity Planning (RCP-01) & gap analysis SDM per data product.
- **Keamanan data**: riset & implementasi **PostgreSQL Anonymizer + Trino** untuk data masking; klasifikasi sensitivitas + uji konsekuensi utk metrik publik; SOP Pengendalian Permintaan Data (konsolidasi kebijakan akses data/sistem/infra dgn tim Tata Kelola); audit histori **SCD tipe 4** pada Master Data Individu.

## Master Data & MDM Penerima Manfaat (produk inti)

- **MDM Penerima Manfaat (aplikasi "MPM" / Manajemen Penerima Manfaat)**: master **Individu** + **KPM (Kelompok Penerima Manfaat)**; **kode KPM = NPSN** utk kelompok sekolah (pemadanan dimulai 424 SPPG → pairing 15 SPPG prioritas Mei 2026); status keanggotaan PM/KPM dgn pemisahan **non-aktif permanen vs temporary**; model **Entitlement** (kontrol pemadanan per individu dlm satu KPM); siklus hidup PM & KPM difinalisasi bersama Pusdatin × MLTI (akhir Mei 2026); migrasi dari `shareddb` ke database MDM terpisah (isolasi environment).
- **Sumber data integrasi**: **Dapodik** (Kemendikdasmen), **EMIS/Data Peserta Didik Kemenag** (pipeline brief Apr 2026), **SMO/dialur** (tabel terobservasi: `api_smo_unit_pelayanan`, `v1_api_smo_kpm`), **Pormit** (mitra), deduplikasi Profil Balita, profil pendidikan & medis (draft data catalog), rencana pertukaran data **Kemenkes/SATUSEHAT** (draft juknis 2026; FHIR, NIK balita).
- **Master Data SPPG**: data product tersendiri (proposal & desain Apr–Mei 2026); gap analysis **Master SPPG Pormit vs SMO**; metrik "SPPG Non-Operasional"; filter SPPG dummy utk dashboard.
- **CR Gateway (change request data mesh)** — pola tata kelola perubahan master data (dok. `PEM-CR-IMPL-PLAN-001`): source-aligned (mis. Dapodik → Gold) → DQ check PASS → DAG pembentukan batch CR → update package (JSON) → governance app → review Data Steward (human-in-the-loop) → callback APPROVED/REJECTED + id_assignments → writeback Gold → konsumsi consumer-aligned via API delta. State machine PENDING→APPROVED/REJECTED; SLA PENDING >24 jam = alert. (Ringkasan; detail teknis di dokumen CR internal.)

## Keuangan: VA SPPG & MonSAKTI

- **Data Quality VA 5 Bank Himbara**: rekonsiliasi transaksi VA SPPG; anomali ditangani per bank (kasus BSI Apr 2026; salah tarik BNI Mei 2026); scheduler DQ check otomatis; metrics definition VA terstandar; glosarium data source dashboard VA.
- **Analisis fraud "saldo mengendap" VA SPPG** (Apr 2026) → laporan eskalasi ke CDO/pimpinan.
- **MonSAKTI (Kemenkeu)**: EDA pagu & realisasi anggaran BGN; standardisasi enum struktur anggaran (Group Unit → Item); data mart Keuangan.
- Komparasi **harga pangan Bapanas vs modul SCM** utk deteksi disparitas harga komoditas rantai pasok MBG.

## Dashboard & pelaporan (produk BI per Mei–Juni 2026)

| Dashboard | Audiens | Catatan |
|---|---|---|
| SCM Overview / Executive SCM (Tableau) | Pimpinan | Revisi per arahan Kapusdatin; user guide eksekutif |
| KinOps (Metabase) | Operasional | Presensi, pengiriman, insiden, sebaran SPPG; desain 3 level (Ka.SPPG, Eksekutif, Publik) |
| Monitoring Organoleptik / Rating Makanan | Ka.SPPG → publik (rencana) | Dari form submission organoleptik; seeding 15 SPPG prioritas; rencana publikasi publik |
| Dashboard Reviu MBG | Internal | Filter exclusion SPPG dummy |
| Monitoring VA / DQ VA | Keuangan | Wireframe + glosarium |
| Supplier SPPG (V2) | Analisis rantai pasok | Sankey pop-out; basis SCM |
| **Dashboard Nasional MBG (Publik)** | Publik | Datamart khusus, uji konsekuensi metrik, wireframe final Apr–Mei 2026 |
| Daily Report / Daily Deck MBG | Pimpinan harian | Mockup + master metrics |
| Funnel Aktivitas User SSO | Internal | Dari export XPASS Peruri; analytics login |
| Master metrics lintas dashboard | Semua | Definisi, logika hitung, sumber data — dokumentasi standar |

## Cara kerja tim & artefak proses

Sprint planning dua-mingguan (squad A/B), daily KPM management, weekly report ke pimpinan, bimtek SCM nasional (analisis funnel adopsi; sasaran SPPG yang belum login SSO), pairing & transfer knowledge (DataArts→Peruri, Data Flow & ERD Peruri→Pusdatin), SLA & SOP Data Collection BNBA PM, template narasi issue SIPGN (`SIPGN_ISSUE_NARRATIVE_TEMPLATE`, v1.0 17 Mei 2026 — 6 parameter universal; pakai utk menulis issue Jira), profiling gold (contoh: `ref_pem_*`, `kpm_custom_tags` per 9 Mei 2026), KAK Dashboard Monev (template pengadaan, Apr 2026).

## Anti-halusinasi khusus data

1. Nama tabel/skema: HANYA kutip yang terobservasi (mis. `api_smo_unit_pelayanan`, `v1_api_smo_kpm`, `ref_pem_*`); selainnya katakan "perlu cek katalog".
2. Angka atribut metadata = snapshot 27 Mar 2026; sebut tanggalnya.
3. Status integrasi (Kafka HRIS, SATUSEHAT, EMIS) = berproses 2026; jangan klaim "sudah live" tanpa bukti baru.
4. Untuk detail kolom/enum: rujuk OpenMetadata/G-01/G-03 aktual, bukan ingatan.
