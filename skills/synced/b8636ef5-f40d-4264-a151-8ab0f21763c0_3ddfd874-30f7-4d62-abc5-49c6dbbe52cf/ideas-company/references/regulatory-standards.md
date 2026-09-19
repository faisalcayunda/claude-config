# Regulatory & Industry Standards

IDEAS services and products are designed to comply with and implement key Indonesian regulations and international standards for data management. This reference provides a comprehensive regulatory knowledge base covering **over 30 primary regulations** across 6 tiers of the Indonesian legal hierarchy, plus international standards and frameworks.

> **Last Updated:** February 2026 | **Version:** 5.8
>
> **Cross-References:** `services-catalog.md` (service codes S1.1-S3.4), `dama-integration-map.md` (DAMA KA alignment), `rab-hps-methodology.md` (SBM rates), `client-intelligence-spbe.md` (SPBE analysis), `inaproc-digital-catalog.md` (e-Katalog products)

## Indonesian Regulatory Hierarchy

The Indonesian legal system follows a strict hierarchy established by UU 12/2011 jo. UU 13/2022. Understanding this hierarchy is critical for proposals and compliance frameworks, as higher-tier regulations take precedence.

```
Tier 1: Undang-Undang (UU) — Laws enacted by Parliament
  └─ Tier 2: Peraturan Pemerintah (PP) — Government Regulations implementing UU
     └─ Tier 3: Peraturan Presiden (Perpres) — Presidential Regulations
        └─ Tier 4: Peraturan Menteri (Permen) — Ministerial Regulations
           └─ Tier 5: Peraturan Lembaga (Peraturan BPS, BIG, etc.) & Keputusan Menteri
              └─ Tier 6: Peraturan Daerah (Perda) & Peraturan Gubernur (Pergub)
```

---

## Tier 1: Foundational Laws (Undang-Undang)

### UU No. 27/2022 — Pelindungan Data Pribadi (PDP)

Indonesia's comprehensive personal data protection law, modeled on GDPR. This is the **highest-urgency** regulation for IDEAS clients.

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Undang-Undang tentang Pelindungan Data Pribadi |
| **Penerbit** | Presiden RI (DPR) |
| **Tanggal Berlaku** | 17 Oktober 2022 |
| **Enforcement Penuh** | **17 Oktober 2024** (masa transisi 2 tahun telah berakhir) |
| **Cakupan** | Seluruh pengendali dan prosesor data pribadi, baik pemerintah maupun swasta |
| **Sanksi Administratif** | Denda hingga **2% pendapatan tahunan**; perintah penghapusan data |
| **Sanksi Pidana** | Penjara hingga 5 tahun dan/atau denda hingga **Rp 5 miliar** (pengumpulan ilegal); hingga 6 tahun dan/atau **Rp 6 miliar** (pemalsuan); korporasi hingga **Rp 60 miliar** |
| **PP Pelaksana** | Masih dalam proses penyusunan (per Feb 2026) |
| **Badan Pengawas** | Lembaga Pelindungan Data Pribadi (belum sepenuhnya operasional) |

**Ketentuan Kunci:**
- Pasal 5-6: Jenis data pribadi (umum dan spesifik)
- Pasal 8-15: Hak subjek data (akses, koreksi, hapus, portabilitas, keberatan, penarikan consent)
- Pasal 16-19: Kewajiban pengendali data (dasar hukum pemrosesan, DPIA, pencatatan aktivitas)
- Pasal 20-26: Pemrosesan data pribadi (consent, legitimate interest, kontrak, kewajiban hukum)
- Pasal 34-39: Transfer data lintas batas (adequacy decision, safeguards)
- Pasal 46: Notifikasi pelanggaran data dalam **72 jam**
- Pasal 53: Kewajiban penunjukan **Data Protection Officer (DPO)**

**Implikasi IDEAS:** Mendorong permintaan urgent untuk `S1.2 Data Governance & Compliance Framework` (UU PDP compliance readiness), `S3.1 DGO as a Service` (fungsi DPO), dan `S1.4 SOP Development` (17 SOP termasuk data retention, deletion, breach notification).

### UU No. 11/2008 jo. UU No. 19/2016 — Informasi dan Transaksi Elektronik (ITE)

Kerangka hukum utama untuk informasi dan transaksi elektronik di Indonesia.

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | UU tentang Informasi dan Transaksi Elektronik (sebagaimana diubah) |
| **Penerbit** | Presiden RI (DPR) |
| **Tanggal Berlaku** | UU 11/2008: 21 April 2008; UU 19/2016: 25 November 2016 |
| **Cakupan** | Seluruh penyelenggara sistem elektronik |

**Ketentuan Kunci UU 11/2008:**
- Pasal 5-12: Keabsahan dokumen dan tanda tangan elektronik
- Pasal 15-16: Kewajiban penyelenggara sistem elektronik (andal, aman, bertanggung jawab)
- Pasal 26: Perlindungan data pribadi dalam sistem elektronik
- Pasal 27-37: Perbuatan yang dilarang (konten ilegal, akses ilegal, intersepsi ilegal)

**Perubahan Kunci UU 19/2016:**
- Pasal 26 (baru): **Right to be forgotten** — hak meminta penghapusan informasi elektronik yang tidak relevan berdasarkan putusan pengadilan
- Pasal 31: Penyadapan hanya melalui permintaan penegak hukum, diatur dengan UU
- Pasal 40: Kewenangan pemerintah memutus akses konten yang melanggar hukum
- Pasal 45: Pencemaran nama baik menjadi **delik aduan**, hukuman dikurangi dari 6 tahun menjadi 4 tahun

**Implikasi IDEAS:** Fondasi hukum untuk seluruh sistem elektronik yang dibangun IDEAS. Pasal 26 (right to be forgotten) memerlukan mekanisme data deletion dalam platform data. Relevan untuk `S2.5 Secure Data Exchange` dan `S1.2 Data Governance & Compliance Framework`.

### UU No. 14/2008 — Keterbukaan Informasi Publik (KIP)

Dasar hukum Open Data dan transparansi pemerintah.

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Undang-Undang tentang Keterbukaan Informasi Publik |
| **Penerbit** | Presiden RI (DPR) |
| **Tanggal Berlaku** | 30 April 2008 (efektif penuh 30 April 2010) |
| **Kelembagaan** | Komisi Informasi (Pusat, Provinsi, Kabupaten/Kota) |
| **Sanksi Pidana** | Penjara hingga 2 tahun dan/atau denda Rp 10 juta (penghancuran dokumen) |

**Ketentuan Kunci:**
- Pasal 2: Prinsip — seluruh informasi publik bersifat terbuka, pengecualian bersifat ketat dan terbatas
- Pasal 7(3): **Kewajiban membangun sistem informasi dan dokumentasi** untuk mengelola informasi publik
- Pasal 9: Informasi wajib disediakan secara berkala (setiap 6 bulan)
- Pasal 10: Informasi wajib diumumkan serta-merta (ancaman publik)
- Pasal 11: Informasi wajib tersedia setiap saat (termasuk **Daftar Informasi Publik** — fungsional sebagai data catalog)
- Pasal 13: Kewajiban penunjukan **PPID** (Pejabat Pengelola Informasi dan Dokumentasi)
- Pasal 17: Informasi yang dikecualikan (uji konsekuensi wajib dilakukan)

**Implikasi IDEAS:** Dasar hukum utama untuk pembangunan portal data terbuka dan data catalog. Pasal 7(3) adalah mandat langsung untuk `S2.3 Government Data Portal Platform`. Pasal 11 mendorong `S2.2 Data Catalog & Metadata Management`. PPID sebagai data steward alami.

### UU No. 25/2009 — Pelayanan Publik

Kerangka hukum untuk standar dan kualitas pelayanan publik.

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Undang-Undang tentang Pelayanan Publik |
| **Penerbit** | Presiden RI (DPR) |
| **Tanggal Berlaku** | 18 Juli 2009 |
| **Sanksi** | Teguran tertulis, penurunan gaji, pembebasan jabatan, hingga pemberhentian |

**Ketentuan Kunci:**
- Pasal 4: Prinsip pelayanan publik (kepentingan umum, kepastian hukum, kesamaan hak, keterbukaan)
- Pasal 15: Kewajiban sistem pelayanan terpadu (PTSP) — fisik dan **virtual**
- Pasal 21: Komponen standar pelayanan (14 komponen termasuk sistem, mekanisme, prosedur)
- Pasal 23: **Sistem Informasi Pelayanan Publik** — mandat pembangunan sistem informasi elektronik
- Pasal 36-37: Mekanisme pengaduan dan penyelesaian sengketa

**Implikasi IDEAS:** Pasal 15 (sistem pelayanan terpadu virtual) dan Pasal 23 (sistem informasi pelayanan publik) adalah justifikasi hukum untuk pembangunan platform e-government. Relevan untuk `S2.3 Government Data Portal Platform` dan `S2.4 Data Portal & Catalog Implementation`.

### UU No. 4/2011 — Informasi Geospasial

Kerangka hukum untuk pengumpulan, pengolahan, penyimpanan, dan penyebarluasan informasi geospasial.

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Undang-Undang tentang Informasi Geospasial |
| **Penerbit** | Presiden RI (DPR) |
| **Tanggal Berlaku** | 21 April 2011 |
| **Kelembagaan** | Badan Informasi Geospasial (BIG) sebagai penyelenggara IGD |
| **Sanksi Pidana** | Penjara hingga 5 tahun dan/atau denda hingga Rp 1,25 miliar |

**Ketentuan Kunci:**
- Pasal 19-20: Seluruh IGT wajib merujuk pada IGD resmi; dilarang mengubah posisi dan akurasi geometri IGD
- Pasal 22: BIG sebagai satu-satunya penyelenggara IGD
- Pasal 45: Mandat pembangunan **Jaringan Informasi Geospasial Nasional**
- Pasal 49: Seluruh IG wajib disertai **metadata** yang mendeskripsikan kualitasnya
- Pasal 55-56: Kewajiban sertifikasi kompetensi profesional geospasial

**Implikasi IDEAS:** Mendorong permintaan untuk `P1 IDEAS MapEdge` dan layanan geospasial. Pasal 45 (jaringan IG nasional) relevan untuk `S2.3 Government Data Portal Platform`. Pasal 49 (kewajiban metadata) mendorong `S2.2 Data Catalog & Metadata Management`.

---

## Tier 2: Government Regulations (Peraturan Pemerintah)

### PP No. 61/2010 — Pelaksanaan UU Keterbukaan Informasi Publik

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Pemerintah tentang Pelaksanaan UU No. 14/2008 tentang Keterbukaan Informasi Publik |
| **Penerbit** | Presiden RI |
| **Tanggal Berlaku** | 23 Agustus 2010 |

**Ketentuan Kunci:**
- Mengatur prosedur klasifikasi informasi (terbuka vs dikecualikan)
- Mengatur peran dan tanggung jawab PPID secara detail
- Mengatur mekanisme permintaan informasi dan penyelesaian sengketa
- Mengatur standar biaya perolehan informasi publik

**Implikasi IDEAS:** Memperkuat dasar hukum untuk pembangunan sistem PPID digital dan portal informasi publik. Relevan untuk `S1.2 Data Governance & Compliance Framework` (klasifikasi data) dan `S2.3 Government Data Portal Platform`.

### PP No. 96/2012 — Pelaksanaan UU Pelayanan Publik

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Pemerintah tentang Pelaksanaan UU No. 25/2009 tentang Pelayanan Publik |
| **Penerbit** | Presiden RI |
| **Tanggal Berlaku** | 5 Oktober 2012 |
| **Sanksi** | Teguran tertulis, penurunan gaji, pembebasan jabatan, hingga pemberhentian; pembekuan/pencabutan izin untuk swasta |

**Ketentuan Kunci:**
- Pasal 11-21: **Sistem Pelayanan Terpadu** — mengatur pelayanan terpadu fisik dan **virtual**
- Pasal 14: Justifikasi hukum utama untuk pembangunan platform e-government terintegrasi
- Pasal 25: Komponen standar pelayanan (blueprint untuk fitur platform digital)
- Pasal 30: **Maklumat Pelayanan** — dapat diimplementasikan sebagai service pledge digital
- Pasal 41-42: Partisipasi masyarakat — justifikasi untuk feedback channel digital dan publikasi data kinerja
- Pasal 49: Sanksi administratif bertingkat untuk ketidakpatuhan

**Implikasi IDEAS:** Pasal 14 (pelayanan terpadu virtual) adalah justifikasi hukum primer untuk pembangunan platform e-government. Relevan untuk `S2.3 Government Data Portal Platform` dan `S2.4 Data Portal & Catalog Implementation`.

---

## Tier 3: Presidential Regulations (Peraturan Presiden)

### Perpres No. 95/2018 → Perpres No. 132/2022 — Sistem Pemerintahan Berbasis Elektronik (SPBE)

Dua Perpres ini membentuk kerangka utama e-government Indonesia.

| Aspek | Perpres 95/2018 | Perpres 132/2022 |
| :--- | :--- | :--- |
| **Fokus** | Kerangka dasar SPBE | Arsitektur SPBE Nasional |
| **Tanggal Berlaku** | 2 Oktober 2018 | 2022 |
| **Status** | Masih berlaku (sebagian diperbarui) | Memperkuat dan melengkapi |

**Perpres 95/2018 — Ketentuan Kunci:**
- Pasal 1: Definisi SPBE sebagai penyelenggaraan pemerintahan yang memanfaatkan TIK
- Pasal 7-13: **Tata Kelola SPBE** — Rencana Induk, Arsitektur, Anggaran
- Pasal 14-25: **Manajemen SPBE** — 8 area: risiko, keamanan informasi, **manajemen data**, aset TIK, SDM, pengetahuan, perubahan, layanan
- Pasal 26: **Data dan informasi** — penekanan pada berbagi pakai data dan interoperabilitas
- Pasal 27-33: **Infrastruktur SPBE** — pusat data nasional, sistem penghubung layanan
- Pasal 34-39: **Aplikasi SPBE** — aplikasi umum dan khusus
- Pasal 49: **Manajemen data** — proses pengelolaan data sebagai aset strategis

**Perpres 132/2022 — Ketentuan Kunci:**
- Menetapkan **Arsitektur SPBE Nasional** sebagai acuan seluruh K/L/D
- Domain arsitektur: proses bisnis, data dan informasi, infrastruktur, aplikasi, keamanan
- Arsitektur SPBE Nasional ditinjau setiap 5 tahun
- Seluruh K/L/D wajib menyusun Arsitektur SPBE Instansi yang selaras dengan arsitektur nasional

**Target:** Seluruh K/L/D mencapai minimum Indeks SPBE "Baik" pada 2025.

**Implikasi IDEAS:** Klien dengan Indeks SPBE rendah adalah target utama. Layanan IDEAS secara langsung meningkatkan skor pada domain **Manajemen Data** dan **Layanan Publik Berbasis Elektronik**. Selalu referensikan Perpres 132/2022 sebagai regulasi terkini. Relevan untuk seluruh layanan IDEAS, terutama `S1.1`, `S1.2`, `S2.3`, `S2.4`.

### Perpres No. 39/2019 — Satu Data Indonesia (SDI)

Kebijakan tata kelola data pemerintah nasional.

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Presiden tentang Satu Data Indonesia |
| **Penerbit** | Presiden RI |
| **Tanggal Berlaku** | Juni 2019 |
| **Portal** | [data.go.id](https://data.go.id) |
| **Rencana Aksi** | Rencana Aksi SDI 2022-2024 |

**Ketentuan Kunci:**
- Pasal 1: Definisi SDI — kebijakan tata kelola data pemerintah untuk menghasilkan data yang akurat, mutakhir, terpadu, dan dapat dipertanggungjawabkan
- Pasal 2: **Tiga prinsip SDI:** (1) Standar Data, (2) Metadata, (3) Interoperabilitas Data
- Pasal 6-12: **Peran kunci:**
  - **Pembina Data** — menetapkan standar data (BPS untuk statistik, BIG untuk geospasial)
  - **Walidata** — mengumpulkan, memeriksa, dan mengelola data sesuai standar
  - **Produsen Data** — menghasilkan data sesuai standar yang ditetapkan
- Pasal 20-24: Portal Satu Data Indonesia sebagai medium berbagi pakai data
- Pasal 25-26: Forum Satu Data Indonesia untuk koordinasi

**Implikasi IDEAS:** Mendorong permintaan utama untuk `S2.3 Government Data Portal Platform` dan `S1.1 Data Strategy & Roadmap`. Peran Walidata dan Produsen Data selaras dengan konsep data stewardship dalam DAMA-DMBOK. Tiga prinsip SDI (standar data, metadata, interoperabilitas) menjadi kerangka kerja untuk `S2.2 Data Catalog & Metadata Management`.

### Perpres No. 27/2014 — Jaringan Informasi Geospasial Nasional

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Presiden tentang Jaringan Informasi Geospasial Nasional |
| **Penerbit** | Presiden RI |
| **Tanggal Berlaku** | 17 April 2014 |
| **Kelembagaan** | BIG sebagai Penghubung Simpul Jaringan |

**Ketentuan Kunci:**
- Membentuk jaringan nasional untuk berbagi pakai informasi geospasial
- Simpul Jaringan: seluruh K/L, TNI, Polri
- Penghubung Simpul Jaringan: BIG — mengintegrasikan seluruh simpul
- Pembiayaan desentralisasi — masing-masing simpul bertanggung jawab atas anggarannya
- Seluruh jaringan IG yang ada wajib menyesuaikan dalam 1 tahun

**Implikasi IDEAS:** Relevan untuk `P1 IDEAS MapEdge` dan layanan integrasi data geospasial. Model simpul jaringan dapat diadopsi untuk arsitektur data portal daerah.

---

## Tier 4: Ministerial Regulations (Peraturan Menteri)

### Permen PPN No. 16/2020 — Manajemen Data SPBE

**Regulasi paling detail tentang manajemen data pemerintah di Indonesia.**

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri PPN/Kepala Bappenas tentang Manajemen Data Sistem Pemerintahan Berbasis Elektronik |
| **Penerbit** | Menteri PPN/Kepala Bappenas |
| **Tanggal Berlaku** | 2020 |
| **Cakupan** | Seluruh Instansi Pusat dan Pemerintah Daerah |

**Ketentuan Kunci:**
- Mengatur **siklus hidup data** lengkap: perencanaan, pengumpulan, pemeriksaan, penyebarluasan, penyimpanan, pemusnahan
- Mengatur **arsitektur data** termasuk data induk (master data), data referensi, dan basis data
- Mengatur **kualitas data** termasuk standar kualitas dan mekanisme pemeriksaan
- Mengatur **interoperabilitas data** untuk berbagi pakai antar instansi
- Mengatur **tata kelola data** termasuk peran dan tanggung jawab pengelola data

**Implikasi IDEAS:** Regulasi ini adalah **blueprint langsung** untuk seluruh layanan IDEAS. Setiap aspek yang diatur selaras dengan DAMA-DMBOK Knowledge Areas. Sangat relevan untuk `S1.1`, `S1.2`, `S1.3`, `S2.1`, `S2.2`, `S2.3`, `S3.1`.

### Permen PPN No. 17/2020 — Pengelolaan Portal Satu Data Indonesia

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri PPN/Kepala Bappenas tentang Pengelolaan Portal Satu Data Indonesia |
| **Penerbit** | Menteri PPN/Kepala Bappenas |
| **Tanggal Berlaku** | 2020 |

**Ketentuan Kunci:**
- Mengatur tata kelola Portal Satu Data Indonesia (data.go.id)
- Mengatur mekanisme pengunggahan, pemutakhiran, dan pencabutan dataset
- Mengatur standar metadata untuk dataset di portal
- Mengatur mekanisme akses dan pengunduhan data oleh publik

**Implikasi IDEAS:** Referensi teknis langsung untuk `S2.3 Government Data Portal Platform`. Standar metadata portal menjadi acuan untuk `S2.2 Data Catalog & Metadata Management`.

### Permen PPN No. 18/2020 — Tata Kerja Penyelenggara SDI Tingkat Pusat

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri PPN/Kepala Bappenas tentang Tata Kerja Penyelenggara Satu Data Indonesia Tingkat Pusat |
| **Penerbit** | Menteri PPN/Kepala Bappenas |
| **Tanggal Berlaku** | 2020 |

**Ketentuan Kunci:**
- Mengatur tata kerja Sekretariat SDI, Forum SDI, dan Kelompok Kerja
- Mengatur mekanisme koordinasi antara Pembina Data, Walidata, dan Produsen Data
- Mengatur prosedur penetapan dan pemutakhiran standar data
- Mengatur mekanisme pelaporan dan evaluasi penyelenggaraan SDI

**Implikasi IDEAS:** Memperkuat pemahaman tentang struktur organisasi SDI untuk penyusunan proposal yang akurat. Relevan untuk `S1.1 Data Strategy` (alignment dengan struktur SDI) dan `S3.4 Knowledge Transfer` (pelatihan peran SDI).

### PermenpanRB No. 59/2020 — Pemantauan dan Evaluasi SPBE

**Regulasi utama untuk evaluasi SPBE yang menentukan Indeks SPBE.**

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri PANRB tentang Pemantauan dan Evaluasi SPBE |
| **Penerbit** | Menteri PANRB |
| **Tanggal Berlaku** | 1 Januari 2021 |
| **Hasil Evaluasi Terbaru** | SK MenpanRB No. 13/2024 (hasil evaluasi 2023) |

**Ketentuan Kunci — 47 Indikator dalam 4 Domain:**

| Domain | Jumlah Indikator | Indikator Kunci untuk IDEAS |
| :--- | :--- | :--- |
| **Domain 1: Kebijakan SPBE** | 9 | Ind. 3: Kebijakan Manajemen Data; Ind. 7: Sistem Penghubung Layanan |
| **Domain 2: Tata Kelola SPBE** | 5 | Ind. 11: Arsitektur SPBE; Ind. 14: Inovasi Proses Bisnis |
| **Domain 3: Manajemen SPBE** | 10 | **Ind. 23: Penerapan Manajemen Data**; Ind. 18: Sistem Penghubung Layanan |
| **Domain 4: Layanan SPBE** | 23 | **Ind. 43: Layanan Data Terbuka** |

**Skala Kematangan (1-5):**

| Level | Predikat | Deskripsi |
| :--- | :--- | :--- |
| 1 | Rintisan | Ad hoc, belum ada kebijakan formal |
| 2 | Terkelola | Kebijakan ada tetapi belum terintegrasi |
| 3 | Terstandardisasi | Kebijakan terintegrasi dan terstandarisasi |
| 4 | Terintegrasi | Implementasi terintegrasi antar unit |
| 5 | Optimum | Berkelanjutan dan inovatif |

**Implikasi IDEAS:** Data SPBE di `references/spbe-2024-kl.csv` dan `references/spbe-2024-daerah.csv` digunakan untuk mengidentifikasi klien potensial. Indikator 3 (Kebijakan Manajemen Data), Indikator 23 (Penerapan Manajemen Data), dan Indikator 43 (Layanan Data Terbuka) adalah indikator yang paling langsung ditingkatkan oleh layanan IDEAS.

### Permen Kominfo No. 1/2023 — Interoperabilitas Data dalam SPBE dan SDI

**Jembatan regulasi antara SPBE dan Satu Data Indonesia.**

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri Kominfo tentang Interoperabilitas Data dalam Penyelenggaraan SPBE dan SDI |
| **Penerbit** | Menteri Komunikasi dan Informatika |
| **Tanggal Berlaku** | 2023 |

**Ketentuan Kunci:**
- Definisi: Interoperabilitas Data = kemampuan sistem elektronik dengan karakteristik berbeda untuk berbagi pakai data secara terintegrasi
- Mengatur **standar interoperabilitas** meliputi: format data, protokol pertukaran, API, metadata
- Mengatur **arsitektur interoperabilitas** yang menghubungkan SPBE dan SDI
- Mengatur **tata kelola interoperabilitas** termasuk peran koordinator dan pengelola

**Implikasi IDEAS:** Regulasi ini adalah dasar hukum langsung untuk `S2.5 Secure & Trusted Data Exchange — API Gateway Platform`. Juga memperkuat proposisi nilai `S2.2 Data Catalog & Metadata Management` dan `S2.3 Government Data Portal Platform` yang harus memenuhi standar interoperabilitas.

### Permenkomdigi No. 6/2025 — Standar Teknis dan Prosedur Pembangunan Aplikasi SPBE

**Regulasi terbaru (Maret 2025) — standar teknis untuk pengembangan aplikasi SPBE.**

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri Komunikasi dan Digital tentang Standar Teknis dan Prosedur Pembangunan dan Pengembangan Aplikasi SPBE |
| **Penerbit** | Menteri Komunikasi dan Digital |
| **Tanggal Berlaku** | Maret 2025 |

**Ketentuan Kunci:**
- Mengatur **siklus pembangunan aplikasi SPBE** (perencanaan, analisis, desain, pengembangan, pengujian, implementasi, pemeliharaan)
- Mengatur **persyaratan teknis** termasuk keamanan, interoperabilitas, aksesibilitas
- Mengatur **standar arsitektur aplikasi** yang harus selaras dengan Arsitektur SPBE Nasional
- Seluruh instansi pusat dan daerah wajib mematuhi standar ini

**Implikasi IDEAS:** Seluruh produk platform IDEAS (P1-P8) harus memenuhi standar teknis ini. Relevan untuk `S2.1 Data-Centric Digital Product Development` dan seluruh layanan implementasi platform.

### Permenkes No. 18/2022 — Satu Data Bidang Kesehatan

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Menteri Kesehatan tentang Penyelenggaraan Satu Data Bidang Kesehatan melalui Sistem Informasi Kesehatan |
| **Penerbit** | Menteri Kesehatan |
| **Tanggal Berlaku** | 2022 |

**Ketentuan Kunci:**
- Mengatur implementasi kebijakan Satu Data di sektor kesehatan
- Mengatur **Sistem Informasi Kesehatan (SIK)** sebagai platform integrasi data kesehatan
- Mengatur standar data kesehatan, metadata, dan interoperabilitas
- Mengatur peran Walidata dan Produsen Data di lingkungan Kemenkes dan Dinkes

**Implikasi IDEAS:** Contoh implementasi sektoral SDI yang dapat dijadikan referensi untuk sektor lain. Membuka peluang pasar di sektor kesehatan untuk `S1.1 Data Strategy`, `S1.2 Data Governance`, dan `S2.3 Government Data Portal Platform`.

---

## Tier 5: Agency Regulations & Decisions

### Kepmenpanrb No. 962/2021 — Pedoman Teknis Evaluasi SPBE

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Keputusan Menteri PANRB tentang Pedoman Teknis Pelaksanaan Pemantauan dan Evaluasi SPBE |
| **Penerbit** | Menteri PANRB |
| **Tanggal Berlaku** | 2021 |

**Ketentuan Kunci:**
- Mengatur **instrumen evaluasi** detail untuk 47 indikator SPBE
- Mengatur **prosedur penilaian**: Penilaian Mandiri → Penilaian Dokumen → Penilaian Interviu → Penilaian Visitasi
- Mengatur **kode etik asesor** (integritas, objektivitas, kerahasiaan, kompetensi)
- Mengatur **formula perhitungan Indeks SPBE** dengan bobot per domain, aspek, dan indikator

**Implikasi IDEAS:** Pedoman teknis ini adalah referensi utama untuk `scripts/query_spbe.py` dan analisis klien pemerintah. Memahami bobot dan kriteria penilaian memungkinkan IDEAS menyusun proposal yang secara spesifik menargetkan peningkatan indikator tertentu.

### Peraturan BPS No. 4/2020 — Petunjuk Teknis Standar Data Statistik

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan BPS tentang Petunjuk Teknis Standar Data Statistik |
| **Penerbit** | Badan Pusat Statistik |
| **Tanggal Berlaku** | 2020 |

**Ketentuan Kunci:**
- Mengatur **5 komponen standar data**: konsep, definisi, klasifikasi, ukuran, satuan
- Mengatur **tahapan identifikasi standar data statistik**
- Mengatur **prosedur dan alur pengajuan standar data** dari Produsen Data → Walidata → BPS (Pembina Data)
- Mengatur peran BPS sebagai Pembina Data untuk statistik nasional

**Implikasi IDEAS:** Referensi teknis untuk standarisasi data dalam implementasi SDI. 5 komponen standar data menjadi acuan untuk `S2.2 Data Catalog & Metadata Management` dan `S2.3 Government Data Portal Platform`. Relevan untuk `S1.1 Data Strategy` dan `S3.1 Data Literacy & Capacity Building`.

### Peraturan BIG No. 2/2020 — Manajemen Kualitas Informasi Geospasial

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan BIG tentang Manajemen Kualitas Informasi Geospasial pada BIG |
| **Penerbit** | Badan Informasi Geospasial |
| **Tanggal Berlaku** | 14 Mei 2020 |

**Ketentuan Kunci:**
- Mengatur **Kontrol Kualitas** (Quality Control) oleh Produsen Data: perencanaan, pengumpulan DG, pengolahan DG/IG
- Mengatur **Penjaminan Kualitas** (Quality Assurance) oleh Walidata: evaluasi IG dan metadata
- Mengatur **Elemen Kualitas** berdasarkan SNI (Standar Nasional Indonesia)
- Mengatur **evaluasi berkala** minimal 1 tahun sekali
- Output: IG dengan Metadata dan dokumen kontrol/penjaminan kualitas

**Implikasi IDEAS:** Model QC/QA BIG dapat diadopsi untuk framework kualitas data di sektor lain. Relevan untuk `S2.1 Data Quality Management` dan `S1.2 Data Governance & Compliance Framework`. Konsep Produsen Data dan Walidata selaras dengan data stewardship DAMA-DMBOK.

---

## Tier 6: Regional Regulations

### Perda Jabar No. 4/2021 — Penyelenggaraan Komunikasi dan Informatika, Statistik, dan Persandian

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Daerah Provinsi Jawa Barat tentang Penyelenggaraan Komunikasi dan Informatika, Statistik, dan Persandian |
| **Penerbit** | Gubernur Jawa Barat |
| **Tanggal Berlaku** | 10 Februari 2021 |
| **Mencabut** | Perda Jabar No. 29/2010 (Kominfo) dan **Perda Jabar No. 24/2012 (Satu Data Pembangunan Jabar)** |

**Ketentuan Kunci:**
- Pasal 17-33: **Penyelenggaraan SPBE** — tata kelola, domain name (jabarprov.go.id), Pusat Data Provinsi, DRC, jaringan intra-pemerintah, dokumen elektronik, tanda tangan digital
- Pasal 34: **Pengembangan Provinsi Digital** — mandat pembangunan ekosistem digital komprehensif
- Pasal 36: **Statistik dalam kerangka Satu Data Indonesia** di tingkat provinsi
- Pasal 37: Proses bisnis statistik (identifikasi kebutuhan → desain → pengumpulan → pengolahan → penyebarluasan → evaluasi)
- Pasal 44: Kewajiban seluruh OPD menyampaikan data ke instansi statistik provinsi
- Pasal 46-50: **Persandian** — keamanan informasi pemerintah

**Implikasi IDEAS:** Regulasi ini adalah dasar hukum langsung untuk Ekosistem Data Jabar yang dibangun IDEAS. Mencabut Perda 24/2012 yang sebelumnya menjadi dasar. Relevan sebagai referensi model untuk proposal ke provinsi lain.

### Pergub Jabar No. 47/2022 — Pelaksanaan Satu Data Jawa Barat

| Aspek | Detail |
| :--- | :--- |
| **Nama Resmi** | Peraturan Gubernur Jawa Barat tentang Peraturan Pelaksanaan Satu Data Jawa Barat |
| **Penerbit** | Gubernur Jawa Barat |
| **Tanggal Berlaku** | 2022 |

**Ketentuan Kunci:**
- Mengatur implementasi teknis Satu Data di tingkat Jawa Barat
- Mengatur peran Walidata Provinsi, Walidata Perangkat Daerah, dan Produsen Data
- Mengatur standar data, metadata, dan interoperabilitas di tingkat daerah
- Mengatur mekanisme pengelolaan portal data daerah
- Mengatur koordinasi dengan SDI tingkat pusat

**Implikasi IDEAS:** Regulasi pelaksanaan yang menjadi acuan langsung untuk operasional Ekosistem Data Jabar. Model implementasi ini dapat direplikasi untuk provinsi lain.

---

## Additional National Regulations

Regulasi tambahan yang relevan dengan implementasi tata kelola data di Indonesia:

| Regulasi | Tentang | Implikasi |
| :--- | :--- | :--- |
| **PP No. 82/2012 → PP No. 71/2019** | Penyelenggaraan Sistem dan Transaksi Elektronik | Mengatur keamanan dan keandalan sistem elektronik; PP 71/2019 mewajibkan penyimpanan data di Indonesia untuk sektor publik |
| **Permenkominfo No. 4/2016** | Sistem Manajemen Pengamanan Informasi | Standar keamanan informasi untuk sistem data pemerintah |
| **Permendagri No. 70/2019** | Sistem Informasi Pemerintahan Daerah | Pengelolaan informasi pemerintahan daerah secara terintegrasi |
| **Peraturan BSSN No. 10/2019** | Pelaksanaan Persandian Untuk Pengamanan Informasi | Standar keamanan kriptografi untuk data pemerintah daerah |
| **Perpres 16/2018 jo. Perpres 12/2021** | Pengadaan Barang/Jasa Pemerintah (dasar hukum utama) | Mengatur e-Purchasing via e-Katalog, preferensi UMKK (min 40% alokasi), dan metode pengadaan. IDEAS terdaftar sebagai penyedia UMKK di INAPROC e-Katalog v6 |
| **Perpres 46/2025** | Pengadaan Barang/Jasa Pemerintah (pembaruan) | Seluruh RAB/HPS harus mematuhi prosedur pengadaan terbaru. Lihat `rab-hps-methodology.md` |
| **Inpres No. 2/2022** | Percepatan Penggunaan Produk Dalam Negeri dan Produk UMKK | Mendorong penggunaan produk UMKK dalam pengadaan pemerintah. IDEAS sebagai UMKK mendapat preferensi |
| **Keppres No. 17/2023** | Percepatan Transformasi Digital Pengadaan | Menugaskan PT Telkom untuk menyelenggarakan SPSE dan sistem pendukung INAPROC |
| **SE Kepala LKPP No. 9/2024** | Mandatory E-Katalog v6 | E-Katalog v6 wajib digunakan seluruh K/L/Pemda sejak 1 Januari 2025 |
| **Kepka LKPP No. 93/2025** | Mini-Kompetisi dalam E-Purchasing | Memperkenalkan metode mini-kompetisi untuk mendapatkan harga terbaik dalam e-Katalog |
| **Perpres 9/2019** | Kebijakan Satu Peta (KSP) | Integrasi informasi geospasial ke dalam satu peta referensi; mendorong `P1 IDEAS MapEdge` |
| **UU No. 11/2020** | Cipta Kerja | Mendorong digitalisasi perizinan (OSS); relevan untuk `S2.5 Secure Data Exchange` |

---

## Labor & Pricing Regulations

| Regulation | Key Points & Implication for IDEAS Services |
| :--- | :--- |
| **PMK 39/2024 & PMK 32/2025 (Standar Biaya Masukan)** | Sets government standard cost inputs (SBM) for budget planning including honorarium rates for experts. Key Rate: Honorarium Expert/Witness (Echelon I level): Rp 1,400,000/hour. All RAB/HPS calculations must reference current SBM rates. See `rab-hps-methodology.md`. |
| **PP No. 49/2025 (Perubahan Kedua PP 36/2021 tentang Pengupahan)** | **PENTING:** PP 49/2025 mengatur tentang **pengupahan (WAGES)**, bukan pengadaan. Mewajibkan seluruh pemberi kerja menyusun dan menerapkan Struktur dan Skala Upah (SUSU). IDEAS rate card (`scripts/rate_card.py`) harus mematuhi ketentuan ini. Termasuk ketentuan upah minimum, upah lembur, dan tunjangan. |
| **UU HPP No. 7/2021 & PMK 105/2025 (PPh 21)** | Progressive income tax with top bracket at 35% for income > Rp 5 billion/year. PTKP (K/2): Rp 67,000,000/year. All COGS calculations must use updated PPh 21 brackets. See `cogs-methodology.md`. |

---

## Professional Competency Standards

| Standard | Key Points & Implication for IDEAS Services |
| :--- | :--- |
| **BNSP SKM-LSPTD-002 (Data Management Competency)** | Indonesian national competency standard for data management professionals, covering 11 competency units. Certification Cost: ~Rp 700,000 per assessment. IDEAS consultants should align with BNSP competency standards. Strengthens credibility in government proposals. |

---

## International Standards

| Standard | Key Points & Implication for IDEAS Services |
| :--- | :--- |
| **DAMA-DMBOK2 / DAMA-DMBOK 3.0** | Global foundation for 14 Knowledge Areas in data management. **DAMA-DMBOK 3.0 Project** kicked off June 25, 2025 — community-driven, multi-year effort with **Triple Helix governance**: Editorial Board (11 Specialty Editors), CDMP Masters Review Panel (7 members), and Global Community. New topics include **AI governance, cloud data management, data fabric/mesh fusion, and modern data platforms**. Quarterly Town Halls ongoing (latest: January 21, 2026). Publication target: **Q2 2027**. All IDEAS service pillars are mapped to DAMA KAs. See `dama-integration-map.md`. |
| **ISO/IEC 27001:2022** | International standard for ISMS. Updated 2022 version with 93 controls in 4 themes. Required for UU PDP compliance. `S1.2 Data Governance & Compliance Framework` includes ISO 27001:2022 alignment. |
| **EU AI Act (Regulation 2024/1689)** | World's first comprehensive AI regulation. Fully applicable August 2, 2026. Prohibited AI practices banned from February 2, 2025. Relevant for clients with international operations. Drives AI Governance consulting within `S1.2`. |
| **NIST AI Risk Management Framework (AI RMF 1.0)** | US voluntary AI risk management framework (January 2023). Four core functions: Govern, Map, Measure, Manage. Complementary to EU AI Act. |
| **ISO/IEC 42001:2023** | International standard for AI Management Systems (AIMS). Harmonizes with ISO 27001 and ISO 9001. Enables certifiable AI governance consulting. |
| **Stranas KA 2020-2045** | Indonesia's national AI strategy: Ethics & Policy, Data Ecosystem, Talent, Infrastructure, R&D. Aligns IDEAS AI governance services with national priorities. |
| **COBIT 2019** | Governance and management of enterprise IT. COBIT APO14 (Managed Data) maps to DAMA-DMBOK. Ensures integration with broader IT governance. |
| **ISO 20000-1:2018** | International standard for ITSMS. Ekosistem Data Jabar tersertifikasi ISO 20000-1:2018 oleh TÜV NORD Indonesia. Bukti kapabilitas IDEAS. |
| **PMBOK 6th Edition** | Process-based PM standard with 49 processes. IDEAS adopts for project governance. See `thought-leadership-frameworks.md` Section 17. |
| **PMBOK 7th Edition** | Principles-based PM standard with 12 Principles and 8 Performance Domains. IDEAS adopts for adaptive delivery. See `thought-leadership-frameworks.md` Section 17. |
| **Infonomics Framework (Laney, 2018)** | Data asset valuation with 6 models (IVI, BVI, PVI, CVI, MVI, EVI). IDEAS adopts for `S1.5 Data Asset Valuation`. See `thought-leadership-frameworks.md` Section 18. |
| **Deloitte Data Valuation Framework (2025)** | Three data asset categories: **Targeted data sets**, **Contextualized insights**, **Customized models/algorithms**. Three valuation approaches: **Income** (MPEEM, Relief-from-royalty, With-and-without), **Cost** (Reproduction/Replacement), **Market** (comparable transactions). Introduces **data debt** concept: lifecycle costs, quality problems, compliance risks, data decay. Organizations treating data as assets achieve **2-3x ROI**. Complements Infonomics for `S1.5 Data Asset Valuation`. |
| **IAS 38 / IFRS (Intangible Assets)** | International accounting standard for intangible assets. China's 2024 provisions for data on balance sheet. IDEAS positions as first-mover for data valuation. |

---

## Indonesian Data Governance Regulatory Framework

Kerangka regulasi tata kelola data Indonesia membentuk ekosistem yang saling terkait. Diagram berikut menunjukkan hubungan hierarkis dan tematik antar regulasi:

### Regulatory Stack (Hierarki Regulasi)

```
UU PDP (27/2022)           ← Perlindungan data pribadi [ENFORCEMENT: Okt 2024]
  └─ PP 71/2019             ← Penyelenggaraan sistem elektronik
  └─ UU ITE (11/2008 jo. 19/2016) ← Informasi dan transaksi elektronik

UU KIP (14/2008)           ← Keterbukaan informasi publik [Open Data]
  └─ PP 61/2010             ← Pelaksanaan UU KIP
  └─ Perpres 9/2019 (KSP)  ← Kebijakan satu peta

UU Pelayanan Publik (25/2009) ← Standar pelayanan publik
  └─ PP 96/2012             ← Pelaksanaan UU Pelayanan Publik

Perpres SDI (39/2019)      ← Satu Data Indonesia [data.go.id]
  ├─ Permen PPN 16/2020     ← Manajemen Data SPBE
  ├─ Permen PPN 17/2020     ← Pengelolaan Portal SDI
  ├─ Permen PPN 18/2020     ← Tata Kerja SDI Tingkat Pusat
  ├─ Peraturan BPS 4/2020   ← Standar Data Statistik
  └─ Permenkes 18/2022      ← Satu Data Bidang Kesehatan

Perpres SPBE (95/2018)     ← Sistem Pemerintahan Berbasis Elektronik
  ├─ Perpres 132/2022       ← Arsitektur SPBE Nasional
  ├─ PermenpanRB 59/2020    ← Pemantauan dan Evaluasi SPBE [47 Indikator]
  ├─ Kepmenpanrb 962/2021   ← Pedoman Teknis Evaluasi SPBE
  ├─ Permen Kominfo 1/2023  ← Interoperabilitas Data SPBE & SDI
  └─ Permenkomdigi 6/2025   ← Standar Teknis Aplikasi SPBE

UU IG (4/2011)             ← Informasi Geospasial
  ├─ Perpres 27/2014        ← Jaringan IG Nasional
  └─ Peraturan BIG 2/2020   ← Manajemen Kualitas IG

DAERAH (Jawa Barat):
  ├─ Perda Jabar 4/2021     ← Kominfo, Statistik, Persandian
  └─ Pergub Jabar 47/2022   ← Pelaksanaan Satu Data Jabar
```

### Comprehensive Mapping: Regulasi → DAMA KAs → IDEAS Services

| Regulasi | DAMA KA Alignment | IDEAS Services | Urgency |
| :--- | :--- | :--- | :--- |
| UU PDP (27/2022) | KA-01, KA-05, KA-12 | S1.2, S1.4, S3.1 | **CRITICAL** (Okt 2024 — sudah berlaku penuh) |
| UU ITE (11/2008 jo. 19/2016) | KA-01, KA-05, KA-12 | S1.2, S2.5 | HIGH |
| UU KIP (14/2008) | KA-01, KA-02, KA-09 | S1.2, S2.2, S2.3 | HIGH |
| UU Pelayanan Publik (25/2009) | KA-01, KA-02 | S1.1, S2.3 | MEDIUM |
| UU IG (4/2011) | KA-01, KA-02, KA-06, KA-08 | S1.2, S2.2, S2.3, P1 | MEDIUM |
| PP 61/2010 (Pelaksanaan KIP) | KA-01, KA-09 | S1.2, S2.3 | MEDIUM |
| PP 96/2012 (Pelaksanaan Pelayanan Publik) | KA-01, KA-02 | S2.3, S2.4 | MEDIUM |
| Perpres SDI (39/2019) | KA-01, KA-02, KA-08, KA-09 | S1.1, S2.2, S2.3 | HIGH |
| Perpres SPBE (95/2018 → 132/2022) | KA-01, KA-02, KA-06, KA-08 | S1.1, S1.2, S2.3, S2.4 | HIGH |
| Permen PPN 16/2020 (Manajemen Data) | KA-01 to KA-14 | S1.1, S1.2, S1.3, S2.1-S2.3, S3.1 | **HIGH** |
| Permen PPN 17/2020 (Portal SDI) | KA-01, KA-02, KA-09 | S2.2, S2.3 | HIGH |
| Permen PPN 18/2020 (Tata Kerja SDI) | KA-01, KA-02 | S1.1, S3.4 | MEDIUM |
| PermenpanRB 59/2020 (Evaluasi SPBE) | KA-01, KA-02, KA-06, KA-08 | S1.1, S1.2, S2.3, S3.2 | HIGH |
| Kepmenpanrb 962/2021 (Pedoman Teknis) | KA-01, KA-02 | S1.1, S1.2, S3.4 | HIGH |
| Permen Kominfo 1/2023 (Interoperabilitas) | KA-01, KA-06, KA-08 | S2.2, S2.3, S2.5 | HIGH |
| Permenkomdigi 6/2025 (Standar Teknis) | KA-01, KA-06 | S2.1, S2.3, S2.4 | HIGH |
| Permenkes 18/2022 (Satu Data Kesehatan) | KA-01, KA-02, KA-08 | S1.1, S1.2, S2.3 | MEDIUM |
| Peraturan BPS 4/2020 (Standar Data) | KA-01, KA-02, KA-08, KA-09 | S1.1, S2.2, S2.3, S3.1 | MEDIUM |
| Peraturan BIG 2/2020 (Kualitas IG) | KA-01, KA-06, KA-08 | S1.2, S2.1, P1 | MEDIUM |
| Perpres 27/2014 (Jaringan IG) | KA-01, KA-02, KA-08 | S1.1, S2.3, P1 | LOW |
| Perda Jabar 4/2021 | KA-01, KA-02, KA-06, KA-08, KA-12 | S1.1, S1.2, S2.3, S3.1 | HIGH (referensi model) |
| Pergub Jabar 47/2022 | KA-01, KA-02, KA-08, KA-09 | S1.1, S2.2, S2.3 | HIGH (referensi model) |
| Stranas KA | KA-01, KA-02, KA-08 | S1.2, S2.1, S2.6 | MEDIUM |
| NIST AI RMF | KA-01, KA-12 | S1.2, S1.4 | MEDIUM |
| ISO/IEC 42001 | KA-01, KA-12 | S1.2 | MEDIUM |
| PP 49/2025 | N/A (labor) | Pricing/HR | MEDIUM |

> **Cross-Reference:** Untuk detail pemetaan SPBE-DAMA, lihat `references/dama-integration-map.md` Section "SPBE-DAMA Knowledge Area Alignment". Untuk analisis klien pemerintah, lihat `references/client-intelligence-spbe.md`.

---

## Key Regulatory Timeline

| Date | Event | Impact |
| :--- | :--- | :--- |
| Okt 2024 | **UU PDP full enforcement** | Seluruh organisasi wajib patuh — masa transisi 2 tahun telah berakhir |
| Mar 2025 | Permenkomdigi 6/2025 berlaku | Standar teknis baru untuk aplikasi SPBE |
| Jan 2025 | **E-Katalog v6 mandatory** | Seluruh K/L/Pemda wajib menggunakan e-Katalog v6 INAPROC (SE LKPP 9/2024) |
| 2025 | Perpres 46/2025 berlaku | Prosedur pengadaan pemerintah diperbarui |
| 2025 | Kepka LKPP 93/2025 | Mini-Kompetisi dalam e-Purchasing INAPROC |
| 2025 | PP 49/2025 berlaku | Kewajiban struktur dan skala upah |
| 2025 | Target seluruh K/L/D Indeks SPBE "Baik" | Evaluasi SPBE tahunan |
| 2025 | DAMA-DMBOK 3.0 development | Framework updates expected |
| Aug 2025 | EU AI Act high-risk obligations | High-risk AI system providers must comply |
| Aug 2026 | EU AI Act fully applicable | International clients need AI governance |
| 2026 | Siklus evaluasi SPBE | Penilaian tahunan seluruh K/L/D |
| 2025-2026 | IASB data asset standard discussions | Potential IFRS updates for data asset recognition |

---

## Regulatory Compliance Checklist for IDEAS Proposals

Saat menyusun proposal, pastikan referensi regulasi yang tepat berdasarkan jenis layanan:

| Jenis Layanan | Regulasi Wajib Direferensikan |
| :--- | :--- |
| Data Governance & Compliance | UU PDP 27/2022, UU ITE 11/2008 jo. 19/2016, Perpres SPBE 95/2018 & 132/2022, Permen PPN 16/2020 |
| Data Portal & Open Data | UU KIP 14/2008, PP 61/2010, Perpres SDI 39/2019, Permen PPN 17/2020, Permen Kominfo 1/2023 |
| SPBE Improvement | Perpres SPBE 95/2018 & 132/2022, PermenpanRB 59/2020, Kepmenpanrb 962/2021, Permenkomdigi 6/2025 |
| Satu Data Implementation | Perpres SDI 39/2019, Permen PPN 16/2020, 17/2020, 18/2020, Peraturan BPS 4/2020 |
| Geospatial Data | UU IG 4/2011, Perpres 27/2014, Perpres 9/2019, Peraturan BIG 2/2020 |
| Health Data | Permenkes 18/2022, Perpres SDI 39/2019, UU PDP 27/2022 |
| Regional (Jabar) | Perda Jabar 4/2021, Pergub Jabar 47/2022, plus regulasi nasional di atas |
| RAB/HPS & Procurement | Perpres 46/2025, Perpres 16/2018 jo. 12/2021, PMK 39/2024 & 32/2025, PP 49/2025, SE LKPP 9/2024 (e-Katalog v6) |
| INAPROC E-Katalog | Perpres 16/2018 jo. 12/2021, Inpres 2/2022, Keppres 17/2023, SE LKPP 9/2024, Kepka LKPP 93/2025 |
| AI Governance | Stranas KA, EU AI Act, NIST AI RMF, ISO/IEC 42001:2023 |

---

**See Also:**
- `dama-integration-map.md`: For detailed mapping of IDEAS services to DAMA Knowledge Areas.
- `rab-hps-methodology.md`: For SBM rate application in government budgets.
- `cogs-methodology.md`: For PPh 21 and labor cost calculations.
- `thought-leadership-frameworks.md` Section 17: For comprehensive PMBOK 6th/7th Edition frameworks.
- `agile-work-hierarchy.md`: For PMBOK-Aligned Project Governance Framework and sector-specific tailoring.
- `thought-leadership-frameworks.md` Section 18: For Data Valuation & Infonomics Framework.
- `client-intelligence-spbe.md`: For SPBE score analysis and client targeting.
- `portfolio-showcase-jabar.md`: For Jawa Barat ecosystem implementation details.
- `inaproc-digital-catalog.md`: For IDEAS INAPROC product catalog, KBLI codes, and cross-selling strategy.
- `human-resources-and-pricing.md`: For role definitions, salary rates, and pricing models.
- `role-definitions.md`: For DDaT-aligned role definitions, responsibilities, and skills for all 141 roles.
- `spbe-evaluation-framework.md`: For 47 SPBE indicators and maturity model.
- `competitive-landscape.md`: For competitor analysis and win themes.

---

## Glossary of Key Terms

| Term | Definition |
| :--- | :--- |
| **APBD** | Anggaran Pendapatan dan Belanja Daerah — Regional Government Budget |
| **APBN** | Anggaran Pendapatan dan Belanja Negara — National Government Budget |
| **BAST** | Berita Acara Serah Terima — Handover Report |
| **BNSP** | Badan Nasional Sertifikasi Profesi — National Professional Certification Agency |
| **DPO** | Data Protection Officer |
| **DRC** | Disaster Recovery Center |
| **HPS** | Harga Perkiraan Sendiri — Owner's Estimate |
| **INAPROC** | Indonesia National Public Procurement Portal |
| **K/L/D** | Kementerian/Lembaga/Daerah — Ministries/Agencies/Regions |
| **KSP** | Kebijakan Satu Peta — One Map Policy |
| **LKPP** | Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah — Government Procurement Policy Agency |
| **OPD** | Organisasi Perangkat Daerah — Regional Government Organization |
| **PDP** | Pelindungan Data Pribadi — Personal Data Protection |
| **PPh 21** | Pajak Penghasilan Pasal 21 — Income Tax Article 21 |
| **PPN** | Pajak Pertambahan Nilai — Value Added Tax (currently 12%) |
| **RAB** | Rencana Anggaran Biaya — Budget Plan |
| **SBM** | Standar Biaya Masukan — Standard Cost Input (PMK 32/2025 for FY 2026) |
| **SDI** | Satu Data Indonesia — One Data Indonesia |
| **SPBE** | Sistem Pemerintahan Berbasis Elektronik — Electronic-Based Government System |
| **SPSE** | Sistem Pengadaan Secara Elektronik — Electronic Procurement System |
| **SUSU** | Struktur dan Skala Upah — Salary Structure and Scale (PP 49/2025) |
| **UMKK** | Usaha Mikro, Kecil, dan Koperasi — Micro, Small Enterprises and Cooperatives |


## Cross-Skill Integration

- **`web-scraper`**: Monitor regulatory changes by scraping JDIH (jdih.go.id), Kemenkeu, and LKPP portals. Use `sitemap_discoverer.py --url <jdih-portal>` to discover new regulations, then `page_scraper.py --ai-extract "regulation_number,title,date,status"` for structured extraction. Follow `web-scraper/references/legal_ethics_guide.md` for scraping compliance.
- **`dama-research`**: Map regulatory requirements to DAMA-DMBOK knowledge areas — UU PDP maps to KA-05 (Security) and KA-12 (Ethics), Perpres SDI maps to KA-02 (Architecture) and KA-06 (Integration), SPBE maps to KA-01 (Governance) and KA-14 (Maturity). See `dama-research/knowledge-areas/` for detailed frameworks.
