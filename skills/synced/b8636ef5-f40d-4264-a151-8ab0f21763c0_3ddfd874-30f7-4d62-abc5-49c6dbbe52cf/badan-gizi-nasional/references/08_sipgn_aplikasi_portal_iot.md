# SIPGN: Aplikasi, Portal, Role Pengguna, dan IoT

## Portal & aplikasi resmi (status per 10 Juni 2026)

| Kanal | URL/nama | Fungsi | Status |
|---|---|---|---|
| Situs utama | www.bgn.go.id | Berita, siaran pers, juknis, FAQ, klarifikasi hoaks, daftar SPPG operasional | Aktif |
| Dashboard publik SIPGN | **sipgn.bgn.go.id/public** | Transparansi capaian program | Aktif |
| Dokumentasi SIPGN | **portal-doc-sipgn.bgn.go.id** | Panduan aplikasi (mis. panduan-sipgn/produksi/ai-surveillance) | Aktif |
| Portal mitra ("Pormit") | **mitra.bgn.go.id** | Pendaftaran & manajemen mitra/yayasan | Aktif, **pendaftaran DITUTUP** (moratorium Juni 2026; sebelumnya pernah tutup Okt 2025, buka 3 Nov 2025 dgn aturan kuota/45 hari) |
| Sistem Manajemen Operasional ("SMO") | **dialur.bgn.go.id** | Operasional harian (login internal) | Aktif |
| Aplikasi Android | **SIPGN Produksi** (`id.go.bgn.sipgn.produksi`), **SIPGN Distribusi** (`id.go.bgn.sipgn.distribusi`) — publisher BGN/Pusdatin; plus PPID BGN | Operasional dapur & distribusi | Aktif (Play Store) |
| Pengawasan internal | **Tauwas Care** (tauwascare.tauwas.bgn.go.id) | Checklist kelayakan dapur oleh Ka.SPPG; pemantauan Deputi Tauwas | Aktif |
| Aduan publik | **SAGI — call center 127** (24 jam), WA 0811-1000-8008, SP4N **bgn.lapor.go.id**, PPID ppid.bgn.go.id, JDIH jdih.bgn.go.id | Pengaduan & informasi | Aktif |
| Pengawasan kejaksaan | **"Jaga Dapur MBG"** (dgn Kejagung, Mar 2026) | Kanal pengawasan daerah | Aktif |
| Internal proyek | Confluence/Jira `bgn-peruri.atlassian.net` (akses terbatas) | Dokumen kontrol & kolaborasi BGN–Peruri | Terbatas |

⚠️ Tidak ada produk resmi bernama "MBG Care" — kanal aduan publik yang benar: SAGI 127 / SP4N Lapor. Semua portal resmi berakhiran `.bgn.go.id`.

## Role pengguna SIPGN (dari Playbook per submodul, ±23 role)

Masyarakat · Pranata Humas · Admin Portal Mitra · Kepala SPPG · Asisten Lapangan · Petugas Distribusi MBG · PIC Penerima Manfaat · BGN (pusat) · Pengawas Gizi · Petugas Kebersihan · Pengawas Keuangan · Auditor · Manager · PPSPM · Staff · Staff Dapur · Admin Service Desk · Admin AMS (Biro BMN) · Admin SDM · Admin LMS (Mentor) · Kepala Departemen · PIC Unit · Superadmin.

Pemetaan contoh: Ka.SPPG memakai submodul produksi (4.1–4.4), distribusi (2.x), pengadaan (5.x), kepegawaian (7.4), infrastruktur (7.1); PIC Penerima Manfaat memakai 3.1–3.4; BGN pusat memakai dashboard 6.x & perencanaan PM 3.5; Superadmin memakai 7.2 (API) & 7.7 (keamanan).

## Aplikasi fungsional dalam ekosistem (nama yang dipakai internal)

Rumah SIPGN (landing), SCM (pengadaan/rantai pasok), ERP (produksi), POP (distribusi/titik layanan), **Menu Planner** (perencanaan menu; v1.2 per Mei 2026), HRIS (kepegawaian; integrasi via Kafka), AMS (aset), LMS (pembelajaran), Service Desk, Manajemen Risiko, AI Surveillance (CCTV analytics produksi), KinOps (dashboard kinerja operasional), FinDash (keuangan), Geotag, Manajemen Limbah, Notifikasi, Mobile MBG/aplikasi lapangan, Fleet (distribusi armada), Core API. Identity: **SSO Keycloak** (instansiasi "XPASS" Peruri). API gateway: **Kong Manager**. Infra: Huawei Cloud Indonesia (alpha → staging → production). Daftar ini = inventaris internal; sebagian nama tidak dipublikasikan resmi — gunakan dgn label "internal".

## IoT dapur SPPG (target desain 5.000 SPPG ber-IoT)

| Perangkat | Rasio desain | Total target | Fungsi |
|---|---|---|---|
| CCTV | 5/SPPG | 25.000 | Pemantauan dapur; feed AI Surveillance |
| CPU Tower AI | 1/SPPG | 5.000 | Edge processing analitik video |
| Digital Signage | 1/SPPG | 5.000 | Informasi menu/jadwal/capaian |
| **PVR (Palm Vein Reader)** | 1/dapur + 15/sekolah | 80.000 (5.000 dapur + 75.000 sekolah) | Absensi/verifikasi biometrik telapak tangan (vendor terobservasi: EFIS/HFSecurity/Vizion/Tencent PalmAI/Sentuh/Roomi) |
| POP device | 1/SPPG | 5.000 | Terminal titik layanan/serah terima |
| Laptop | 1/SPPG | 5.000 | Operasional SPPG |

Managed service IoT bagian dari kontrak Rp199 M (lihat ref 06). Angka = target desain pengadaan, BUKAN realisasi terpasang; jangan klaim "sudah terpasang X" tanpa sumber baru. Retrieval data IoT (contoh berjalan: wilayah Aceh–Jawa Barat, Mei 2026) jadi fondasi Data Product PVR (ref 09).

## NFR & operasional teknis (dari dokumen teknis/TW audit)

Target response API 300 ms (maks toleransi 10 dtk — dinilai terlalu longgar oleh auditor); baseline load test 250 VU (perlu skala ke 5.000 titik); SSO wajib utk petugas (deadline data petugas 10 Jan 2026); quality gate kode (SonarQube A/A/A), DefectDojo, jam.dev (tooling QA Peruri); OWASP Top 10 modul 1: passed (sampel pen test).
