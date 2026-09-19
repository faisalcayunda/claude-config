# Referensi Kanonik Kamus Data (Canonical Data Vocabulary Reference)

> **Tujuan file ini:** Menjadi sumber kebenaran tunggal (*single source of truth*) untuk semua tipe data enum yang berlaku lintas domain dalam ekosistem data ini. Setiap entri dilengkapi dengan dasar regulasi yang menjadi acuan resmi, sehingga konsistensi antara data product dapat dijamin dalam kerangka Federated Data Governance.

---

## Hierarki Regulasi yang Digunakan

Urutan otoritas regulasi dari tertinggi ke terendah:

1. Undang-Undang Republik Indonesia
2. Peraturan Pemerintah (PP)
3. Putusan Mahkamah Konstitusi (MK)
4. Peraturan Menteri (Permen/Permendagri/Permenkes/dsb.)
5. Keputusan Menteri / Keputusan Kepala Badan
6. Standar Nasional Indonesia (SNI) / Klasifikasi BPS
7. Standar Internasional (ISO, WHO ICD, dsb.)
8. Standar Platform / Sistem (Dapodik, BPJS, dsb.)
9. Kebijakan Internal Program (Juknis, SOP)

---

## Daftar Referensi Regulasi Utama

| Kode Referensi | Nama Lengkap | Lingkup Penggunaan |
|---|---|---|
| UU-24-2013 | UU No. 24 Tahun 2013 tentang Perubahan atas UU No. 23 Tahun 2006 tentang Administrasi Kependudukan | Jenis kelamin, agama, pekerjaan, hubungan keluarga, golongan darah, disabilitas |
| UU-27-2022 | UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi | Klasifikasi data, PII, PHI, data sensitif |
| UU-36-2009 | UU No. 36 Tahun 2009 tentang Kesehatan | Klasifikasi kesehatan, jenis layanan kesehatan |
| UU-8-2016 | UU No. 8 Tahun 2016 tentang Penyandang Disabilitas | Kategori disabilitas (versi lebih baru dari UU 24/2013) |
| PP-40-2019 | PP No. 40 Tahun 2019 tentang Pelaksanaan UU Administrasi Kependudukan | Turunan teknis UU-24-2013 |
| PP-71-2019 | PP No. 71 Tahun 2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik | Klasifikasi sistem elektronik, residensi data |
| PERMENDAGRI-109-2019 | Permendagri No. 109 Tahun 2019 tentang Formulir dan Buku yang Digunakan dalam Administrasi Kependudukan | Kode standar jenis kelamin, pekerjaan, agama, perkawinan, hubungan keluarga, golongan darah, disabilitas, pendidikan |
| PERMENDAGRI-14-2015 | Permendagri No. 14 Tahun 2015 tentang Pedoman Pendataan Penduduk Nonpermanen | Status domisili permanen/nonpermanen |
| PUTUSAN-MK-97-2016 | Putusan MK Nomor 97/PUU-XIV/2016 | Hak penganut kepercayaan untuk dicantumkan dalam kolom agama KTP |
| DAPODIK-KEMENDIKDASMEN | Standar Data Dapodik — Kemendikdasmen | Jenis pekerjaan PTK, status kepegawaian, bentuk pendidikan |
| JUKNIS-MBG-2026 | Juknis Tata Kelola MBG 2026 — SK BGN No. 401.1/2025 | Jenis kelompok penerima manfaat, status keanggotaan, kode SPPG |
| ISO-3166-1 | ISO 3166-1 — Country Codes (Alpha-2/3, Numeric) | Kode negara |
| ISO-3166-2-ID | ISO 3166-2:ID — Indonesian Administrative Subdivisions | Kode provinsi Indonesia |
| BPS-KBJI-2014 | Klasifikasi Baku Jabatan Indonesia (KBJI) 2014 — BPS | Klasifikasi jabatan/pekerjaan standar BPS |
| ICD-11 | International Classification of Diseases v11 — WHO | Klasifikasi penyakit dan kondisi kesehatan |
| SNOMED-CT | Systematized Nomenclature of Medicine Clinical Terms | Terminologi klinis medis |

---

## Domain 1: Kependudukan

*Sumber: UU-24-2013, PERMENDAGRI-109-2019*

### 1.1 Jenis Kelamin

**Document ID:** VOC-KEPENDUDUKAN-JENIS-KELAMIN
**Tipe Data:** `VARCHAR(5)`
**Nullable:** Ya (nilai NULL = tidak diketahui)
**PII:** Ya — Masked: Ya
**Referensi:** UU-24-2013 (Pasal 58), PERMENDAGRI-109-2019

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `L` | Laki-laki | Individu berjenis kelamin laki-laki secara biologis sesuai dokumen kependudukan | UU-24-2013 Pasal 58; PERMENDAGRI-109-2019 |
| `P` | Perempuan | Individu berjenis kelamin perempuan secara biologis sesuai dokumen kependudukan | UU-24-2013 Pasal 58; PERMENDAGRI-109-2019 |
| `NULL` | Tidak Diketahui | Jenis kelamin tidak diketahui atau belum tercatat | Konvensi sistem |
| `N/A` | Tidak Dapat Diterapkan | Entitas non-individu (organisasi, benda, dsb.) yang tidak memiliki jenis kelamin | Konvensi sistem |

**Catatan Implementasi PostgreSQL:**
```sql
-- Gunakan CHECK constraint untuk membatasi nilai yang valid
ALTER TABLE dim_individu
    ADD CONSTRAINT chk_jenis_kelamin
    CHECK (jenis_kelamin IN ('L','P') OR jenis_kelamin IS NULL);
-- Jangan gunakan ENUM type PostgreSQL — VARCHAR lebih fleksibel untuk evolusi skema
```

---

### 1.2 Agama dan Kepercayaan

**Document ID:** VOC-KEPENDUDUKAN-AGAMA
**Tipe Data:** `VARCHAR(30)`
**Nullable:** Tidak (setiap individu wajib memiliki nilai)
**PII:** Ya — Masked: Ya (data sensitif per UU-27-2022)
**Referensi:** UU-24-2013, PERMENDAGRI-109-2019, PUTUSAN-MK-97-2016

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `islam` | Islam | Penganut agama Islam | UU-24-2013; PERMENDAGRI-109-2019 |
| `kristen` | Kristen | Penganut agama Kristen (Protestan) | UU-24-2013; PERMENDAGRI-109-2019 |
| `katolik` | Katolik | Penganut agama Katolik | UU-24-2013; PERMENDAGRI-109-2019 |
| `hindu` | Hindu | Penganut agama Hindu | UU-24-2013; PERMENDAGRI-109-2019 |
| `buddha` | Buddha | Penganut agama Buddha | UU-24-2013; PERMENDAGRI-109-2019 |
| `khonghucu` | Khonghucu | Penganut agama Khonghucu | UU-24-2013; PERMENDAGRI-109-2019 |
| `kepercayaan-lainnya` | Kepercayaan Lainnya | Penganut aliran kepercayaan terhadap Tuhan Yang Maha Esa — dijamin oleh Putusan MK | PUTUSAN-MK-97-2016; PERMENDAGRI-109-2019 |

**Tabel Konversi Kode Kemendagri ke Kode Kanonik:**

| Kode Kemendagri | Nama Kemendagri | Kode Kanonik |
|---|---|---|
| `1` | Islam | `islam` |
| `2` | Kristen | `kristen` |
| `3` | Katholik | `katolik` |
| `4` | Hindu | `hindu` |
| `5` | Budha | `buddha` |
| `6` | Khonghucu | `khonghucu` |
| `7` | Kepercayaan Terhadap Tuhan YME / Lainnya | `kepercayaan-lainnya` |

---

### 1.3 Status Perkawinan

**Document ID:** VOC-KEPENDUDUKAN-STATUS-PERKAWINAN
**Tipe Data:** `VARCHAR(30)`
**Nullable:** Tidak
**PII:** Ya — Masked: Ya
**Referensi:** UU-24-2013, PERMENDAGRI-109-2019

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `belum-kawin` | Belum Kawin | Penduduk yang belum terikat pernikahan | PERMENDAGRI-109-2019 |
| `kawin-tercatat` | Kawin Tercatat | Pernikahan sah secara agama dan tercatat oleh hukum negara | PERMENDAGRI-109-2019 |
| `kawin-belum-tercatat` | Kawin Belum Tercatat | Pernikahan sah secara agama namun belum dicatatkan di instansi negara | PERMENDAGRI-109-2019 |
| `cerai-hidup-tercatat` | Cerai Hidup Tercatat | Perpisahan hidup yang telah diputuskan pengadilan dan tercatat negara | PERMENDAGRI-109-2019 |
| `cerai-hidup-belum-tercatat` | Cerai Hidup Belum Tercatat | Perpisahan hidup namun belum memiliki dokumen sah perceraian | PERMENDAGRI-109-2019 |
| `cerai-mati` | Cerai Mati | Perpisahan akibat salah satu pasangan meninggal dunia | PERMENDAGRI-109-2019 |

---

### 1.4 Status Hubungan Dalam Keluarga

**Document ID:** VOC-KEPENDUDUKAN-STATUS-KELUARGA
**Tipe Data:** `VARCHAR(30)`
**Nullable:** Tidak
**PII:** Tidak
**Referensi:** UU-24-2013, PERMENDAGRI-109-2019

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `kepala-keluarga` | Kepala Keluarga | Penanggung jawab unit keluarga yang terdaftar dalam Kartu Keluarga | UU-24-2013; PERMENDAGRI-109-2019 |
| `suami` | Suami | Pasangan laki-laki dari istri dalam keluarga | PERMENDAGRI-109-2019 |
| `istri` | Istri | Pasangan perempuan dari suami dalam keluarga | PERMENDAGRI-109-2019 |
| `anak` | Anak | Anak kandung, anak tiri, atau anak angkat | PERMENDAGRI-109-2019 |
| `menantu` | Menantu | Anak menantu yang sudah menikah dengan anak kandung/tiri/angkat | PERMENDAGRI-109-2019 |
| `cucu` | Cucu | Anak dari anak kandung/tiri/angkat | PERMENDAGRI-109-2019 |
| `orangtua` | Orangtua | Orang tua yang tinggal dalam satu unit keluarga | PERMENDAGRI-109-2019 |
| `mertua` | Mertua | Orang tua dari pasangan suami/istri yang tinggal dalam satu unit keluarga | PERMENDAGRI-109-2019 |
| `famili-lain` | Famili Lain | Individu lain yang tinggal dalam satu unit keluarga | PERMENDAGRI-109-2019 |
| `pembantu` | Pembantu | Asisten rumah tangga yang tinggal dalam satu unit keluarga | PERMENDAGRI-109-2019 |
| `lainnya` | Lainnya | Status hubungan di luar kategori di atas | PERMENDAGRI-109-2019 |

---

### 1.5 Status Domisili

**Document ID:** VOC-KEPENDUDUKAN-STATUS-DOMISILI
**Tipe Data:** `VARCHAR(15)`
**Nullable:** Tidak
**PII:** Tidak
**Referensi:** PERMENDAGRI-14-2015

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `permanen` | Permanen (Sesuai KTP) | Penduduk yang tinggal sesuai alamat domisili di KTP-el atau Kartu Keluarga | PERMENDAGRI-14-2015 |
| `non-permanen` | Nonpermanen (Luar KTP) | Penduduk yang bertempat tinggal di luar alamat domisili KTP paling lama 1 tahun dan tidak bermaksud menetap | PERMENDAGRI-14-2015 |

---

### 1.6 Jenis Pekerjaan

**Document ID:** VOC-KEPENDUDUKAN-JENIS-PEKERJAAN
**Tipe Data:** `VARCHAR(50)`
**Nullable:** Tidak
**PII:** Tidak
**Referensi:** PERMENDAGRI-109-2019, DAPODIK-KEMENDIKDASMEN

Terdapat 101 kode pekerjaan standar dari Kemendagri (nomor 1-99 + kode tambahan Dapodik). Berikut subset yang paling sering digunakan dalam konteks data kependudukan umum:

| Kode | Display Name | Referensi |
|---|---|---|
| `tidak-bekerja` | Belum / Tidak Bekerja | PERMENDAGRI-109-2019 |
| `mengurus-rumah-tangga` | Mengurus Rumah Tangga | PERMENDAGRI-109-2019 |
| `pelajar` | Pelajar / Mahasiswa | PERMENDAGRI-109-2019 |
| `pensiunan` | Pensiunan | PERMENDAGRI-109-2019 |
| `pns` | Pegawai Negeri Sipil (PNS) | PERMENDAGRI-109-2019 |
| `tni` | Tentara Nasional Indonesia (TNI) | PERMENDAGRI-109-2019 |
| `polisi` | Kepolisian RI (POLRI) | PERMENDAGRI-109-2019 |
| `karyawan-swasta` | Karyawan Swasta | PERMENDAGRI-109-2019 |
| `karyawan-bumn` | Karyawan BUMN | PERMENDAGRI-109-2019 |
| `karyawan-bumd` | Karyawan BUMD | PERMENDAGRI-109-2019 |
| `petani` | Petani / Pekebun | PERMENDAGRI-109-2019 |
| `nelayan` | Nelayan / Perikanan | PERMENDAGRI-109-2019 |
| `wiraswasta` | Wiraswasta | PERMENDAGRI-109-2019 |
| `dokter` | Dokter | PERMENDAGRI-109-2019 |
| `guru` | Guru | PERMENDAGRI-109-2019; DAPODIK-KEMENDIKDASMEN |
| `kepala-sekolah` | Kepala Sekolah | DAPODIK-KEMENDIKDASMEN |
| `tenaga-kependidikan` | Tenaga Kependidikan | DAPODIK-KEMENDIKDASMEN |
| `lainnya` | Lainnya | PERMENDAGRI-109-2019 |

**Lihat tabel lengkap:** `Tabel Konversi - Kependudukan - Jenis Pekerjaan.xlsx` (101 kode)

---

## Domain 2: Kesehatan dan Disabilitas

*Sumber: UU-24-2013, UU-8-2016, PERMENDAGRI-109-2019*

### 2.1 Golongan Darah

**Document ID:** VOC-KESEHATAN-GOLONGAN-DARAH
**Tipe Data:** `VARCHAR(10)`
**Nullable:** Ya
**PII:** Ya — Masked: Ya (data kesehatan per UU-27-2022)
**Referensi:** UU-24-2013, PERMENDAGRI-109-2019

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `A` | A | Golongan darah A tanpa spesifikasi rhesus | PERMENDAGRI-109-2019 |
| `B` | B | Golongan darah B tanpa spesifikasi rhesus | PERMENDAGRI-109-2019 |
| `AB` | AB | Golongan darah AB tanpa spesifikasi rhesus | PERMENDAGRI-109-2019 |
| `O` | O | Golongan darah O tanpa spesifikasi rhesus | PERMENDAGRI-109-2019 |
| `A+` | A+ | Golongan darah A dengan rhesus positif | PERMENDAGRI-109-2019 |
| `A-` | A- | Golongan darah A dengan rhesus negatif | PERMENDAGRI-109-2019 |
| `B+` | B+ | Golongan darah B dengan rhesus positif | PERMENDAGRI-109-2019 |
| `B-` | B- | Golongan darah B dengan rhesus negatif | PERMENDAGRI-109-2019 |
| `AB+` | AB+ | Golongan darah AB dengan rhesus positif | PERMENDAGRI-109-2019 |
| `AB-` | AB- | Golongan darah AB dengan rhesus negatif | PERMENDAGRI-109-2019 |
| `O+` | O+ | Golongan darah O dengan rhesus positif | PERMENDAGRI-109-2019 |
| `O-` | O- | Golongan darah O dengan rhesus negatif | PERMENDAGRI-109-2019 |
| `tidak-tahu` | Tidak Tahu | Individu belum mengetahui/memeriksakan golongan darah | PERMENDAGRI-109-2019 |

---

### 2.2 Kategori Disabilitas

**Document ID:** VOC-KESEHATAN-DISABILITAS
**Tipe Data:** `VARCHAR(30)`
**Nullable:** Ya (NULL = tidak penyandang disabilitas)
**PII:** Ya — Masked: Ya (data kesehatan sensitif per UU-27-2022)
**Referensi:** UU-24-2013 (Pasal 58), UU-8-2016, PERMENDAGRI-109-2019

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `cacat-fisik` | Cacat Fisik | Mengalami keterbatasan fungsi fisik secara umum | UU-24-2013 Pasal 58; PERMENDAGRI-109-2019 |
| `cacat-netra` | Cacat Netra/Buta | Mengalami keterbatasan fungsi penglihatan | PERMENDAGRI-109-2019 |
| `cacat-rungu` | Cacat Rungu/Wicara | Mengalami keterbatasan pendengaran dan/atau wicara | PERMENDAGRI-109-2019 |
| `cacat-mental` | Cacat Mental/Jiwa | Mengalami keterbatasan fungsi mental, perilaku, atau kejiwaan | PERMENDAGRI-109-2019 |
| `cacat-fisik-mental` | Cacat Fisik dan Mental | Mengalami disabilitas ganda (fisik dan mental sekaligus) | PERMENDAGRI-109-2019 |
| `cacat-lainnya` | Cacat Lainnya | Disabilitas yang tidak termasuk dalam 5 kategori di atas | PERMENDAGRI-109-2019 |

**Catatan:** UU-8-2016 menggunakan klasifikasi yang lebih rinci (disabilitas fisik, intelektual, mental, sensorik, multiple). Gunakan tabel konversi jika sumber menggunakan klasifikasi UU-8-2016.

---

## Domain 3: Pendidikan

*Sumber: PERMENDAGRI-109-2019, DAPODIK-KEMENDIKDASMEN*

### 3.1 Pendidikan Terakhir

**Document ID:** VOC-PENDIDIKAN-TERAKHIR
**Tipe Data:** `VARCHAR(30)`
**Nullable:** Tidak
**PII:** Tidak
**Referensi:** PERMENDAGRI-109-2019

| Kode | Display Name | Definisi | Referensi |
|---|---|---|---|
| `tidak-sekolah` | Tidak / Belum Sekolah | Belum atau tidak pernah menempuh pendidikan formal | PERMENDAGRI-109-2019 |
| `belum-tamat-sd` | Belum Tamat SD / Sederajat | Sedang menempuh SD namun belum lulus | PERMENDAGRI-109-2019 |
| `tamat-sd` | Tamat SD / Sederajat | Lulusan jenjang Sekolah Dasar atau sederajat (MI, SDLB, Paket A) | PERMENDAGRI-109-2019 |
| `sltp` | SLTP / Sederajat | Lulusan Sekolah Menengah Pertama atau sederajat (MTs, SMPLB, Paket B) | PERMENDAGRI-109-2019 |
| `slta` | SLTA / Sederajat | Lulusan Sekolah Menengah Atas atau sederajat (MA, SMK, MAK, SMALB, Paket C) | PERMENDAGRI-109-2019 |
| `diploma-1-2` | Diploma I/II | Lulusan Pendidikan Tinggi Diploma I/II | PERMENDAGRI-109-2019 |
| `diploma-3` | Diploma III | Lulusan Pendidikan Tinggi Akademi/Diploma III/Sarjana Muda | PERMENDAGRI-109-2019 |
| `s1` | S1 | Lulusan Pendidikan Tinggi Diploma IV/Strata I | PERMENDAGRI-109-2019 |
| `s2` | S2 | Lulusan Pendidikan Tinggi Strata II | PERMENDAGRI-109-2019 |
| `s3` | S3 | Lulusan Pendidikan Tinggi Strata III | PERMENDAGRI-109-2019 |

---

### 3.2 Jenis Kelompok Penerima Manfaat (Satuan Pendidikan)

**Document ID:** VOC-PENDIDIKAN-JENIS-SATDIK
**Tipe Data:** `VARCHAR(10)`
**Nullable:** Tidak
**PII:** Tidak
**Referensi:** JUKNIS-MBG-2026, DAPODIK-KEMENDIKDASMEN

| Kode | Display Name | Referensi |
|---|---|---|
| `PAUD01` | PAUD | JUKNIS-MBG-2026 |
| `TK02` | TK | JUKNIS-MBG-2026 |
| `RA03` | RA | JUKNIS-MBG-2026 |
| `SD04` | SD | JUKNIS-MBG-2026 |
| `MI05` | MI | JUKNIS-MBG-2026 |
| `SMP06` | SMP | JUKNIS-MBG-2026 |
| `MTS07` | MTs | JUKNIS-MBG-2026 |
| `SMA08` | SMA | JUKNIS-MBG-2026 |
| `MA09` | MA | JUKNIS-MBG-2026 |
| `SMK10` | SMK | JUKNIS-MBG-2026 |
| `MAK11` | MAK | JUKNIS-MBG-2026 |
| `SLB12` | SLB | JUKNIS-MBG-2026 |
| `PES13` | Pondok Pesantren | JUKNIS-MBG-2026 |
| `SEM14` | Seminari | JUKNIS-MBG-2026 |
| `POS15` | Posyandu | JUKNIS-MBG-2026 |
| `ATS16` | Anak Tidak Sekolah (ATS) | JUKNIS-MBG-2026 |
| `PKBM17` | PKBM | JUKNIS-MBG-2026 |

**Lihat tabel lengkap:** `Tabel Konversi - Kelompok Penerima Manfaat.xlsx`

---

## Domain 4: Tipe Data Universal — Lintas Domain

Enum-enum berikut bersifat lintas domain. Setiap data product yang menggunakan atribut ini WAJIB merujuk ke definisi di bagian ini untuk menjamin konsistensi.

### 4.1 Klasifikasi Data

**Document ID:** VOC-UNIVERSAL-KLASIFIKASI-DATA
**Tipe Data:** `VARCHAR(20)`
**Nullable:** Tidak
**Referensi:** UU-27-2022, PP-71-2019, Kebijakan Keamanan Informasi Internal

| Kode | Display Name | Definisi | Regulasi Terkait |
|---|---|---|---|
| `public` | Publik | Data yang boleh diakses dan dipublikasikan tanpa batasan. Tidak mengandung informasi yang dapat membahayakan individu atau organisasi | PP-71-2019 |
| `internal` | Internal | Data untuk penggunaan internal organisasi. Tidak untuk dipublikasikan, tetapi tidak mengandung PII atau informasi rahasia kritis | Kebijakan internal |
| `restricted` | Terbatas | Data yang mengandung PII umum (nama, alamat, NIK) atau informasi bisnis yang membatasi aksesnya hanya kepada pihak tertentu yang berwenang | UU-27-2022 Pasal 4; PP-71-2019 |
| `confidential` | Rahasia | Data yang mengandung PII sensitif (kesehatan, biometrik, kepercayaan, orientasi seksual, kondisi keuangan pribadi) atau rahasia negara/bisnis kritis | UU-27-2022 Pasal 4 ayat (2) |

**Hierarki klasifikasi:** `public` < `internal` < `restricted` < `confidential`

---

### 4.2 Kategori Data Pribadi (PII/PHI Classification)

**Document ID:** VOC-UNIVERSAL-KATEGORI-PII
**Tipe Data:** `VARCHAR(30)`
**Nullable:** Ya (NULL = bukan data pribadi)
**Referensi:** UU-27-2022

| Kode | Display Name | Contoh Atribut | Dasar Hukum |
|---|---|---|---|
| `pii-umum` | PII Umum | Nama, alamat, NIK, tanggal lahir, nomor telepon, email | UU-27-2022 Pasal 4 ayat (1) |
| `pii-sensitif-kesehatan` | PII Sensitif — Kesehatan | Kondisi kesehatan, diagnosa, riwayat pengobatan, golongan darah, disabilitas | UU-27-2022 Pasal 4 ayat (2) huruf b |
| `pii-sensitif-biometrik` | PII Sensitif — Biometrik | Sidik jari, retina, iris, wajah, DNA | UU-27-2022 Pasal 4 ayat (2) huruf a |
| `pii-sensitif-keuangan` | PII Sensitif — Keuangan | Nomor rekening, data kartu kredit, riwayat transaksi keuangan | UU-27-2022 Pasal 4 ayat (2) huruf f |
| `pii-sensitif-kepercayaan` | PII Sensitif — Kepercayaan/Agama | Agama, kepercayaan, pandangan politik | UU-27-2022 Pasal 4 ayat (2) huruf c |
| `pii-sensitif-anak` | PII Sensitif — Data Anak | Data pribadi anak di bawah umur (< 18 tahun) | UU-27-2022 Pasal 25 |
| `pii-sensitif-etnis` | PII Sensitif — Ras/Etnis | Ras, etnis, suku bangsa | UU-27-2022 Pasal 4 ayat (2) huruf d |

---

### 4.3 Tipe Operasi SCD / Audit Log

**Document ID:** VOC-UNIVERSAL-OPERASI-SCD
**Tipe Data:** `VARCHAR(10)`
**Nullable:** Tidak
**Referensi:** Konvensi sistem standar (ISO/IEC 13249 SQL Standard)

| Kode | Display Name | Definisi | Digunakan Di |
|---|---|---|---|
| `INSERT` | Insert | Penambahan baris/record baru ke tabel | audit_log.operation, SCD history |
| `UPDATE` | Update | Perubahan nilai atribut pada record yang sudah ada | audit_log.operation |
| `DELETE` | Delete | Penghapusan record dari tabel (fisik maupun soft delete) | audit_log.operation |
| `TRUNCATE` | Truncate | Penghapusan seluruh isi tabel sekaligus | audit_log.operation |
| `MERGE` | Merge (Upsert) | Operasi gabungan INSERT atau UPDATE tergantung keberadaan record | pipeline operations |

---

### 4.4 Tipe SCD (Slowly Changing Dimension)

**Document ID:** VOC-UNIVERSAL-TIPE-SCD
**Tipe Data:** `SMALLINT` atau `VARCHAR(10)`
**Nullable:** Tidak
**Referensi:** Ralph Kimball — The Data Warehouse Toolkit (3rd Edition)

| Kode | Display Name | Definisi | Kasus Penggunaan |
|---|---|---|---|
| `0` | Type 0 — Fixed | Nilai tidak pernah berubah setelah insert. Tabel dilindungi dari mutasi. | Kode referensi, konstanta regulasi |
| `1` | Type 1 — Overwrite | Nilai ditimpa langsung. Tidak ada riwayat disimpan. | Koreksi kesalahan ketik, data tidak material |
| `2` | Type 2 — Row Versioning | Setiap perubahan menghasilkan baris baru. Versi lama ditutup. | Master data yang butuh rekonstruksi historis |
| `3` | Type 3 — Previous Column | Simpan nilai sebelumnya di kolom `prev_*`. Satu lapis histori saja. | Atribut yang jarang berubah, hanya butuh 1 transisi |
| `4` | Type 4 — History Table | Tabel current + tabel history terpisah sebagai ledger audit. | Fact tables, entitas sering berubah, audit compliance |
| `6` | Type 6 — Hybrid | Kombinasi Type 1+2+3. Full history dengan current value di setiap baris. | Analitik yang butuh current vs historical dalam satu query |

---

### 4.5 Status Pipeline Run

**Document ID:** VOC-UNIVERSAL-STATUS-PIPELINE
**Tipe Data:** `VARCHAR(20)`
**Nullable:** Tidak
**Referensi:** Konvensi platform Apache Airflow

| Kode | Display Name | Definisi | Aksi Berikutnya |
|---|---|---|---|
| `queued` | Antrian | Run terjadwal dan menunggu eksekusi | Tunggu worker tersedia |
| `running` | Berjalan | Run sedang aktif dieksekusi | Monitor progress |
| `success` | Berhasil | Run selesai tanpa error | Tidak ada — catat di log |
| `failed` | Gagal | Run selesai dengan error | Alert, investigasi log, retry |
| `skipped` | Dilewati | Run dilewati berdasarkan kondisi (opsional task) | Tidak ada |
| `upstream_failed` | Gagal (Upstream) | Run tidak dimulai karena task upstream gagal | Perbaiki upstream terlebih dahulu |
| `deferred` | Ditunda | Run menunggu kondisi eksternal (sensor) | Tunggu kondisi terpenuhi |

---

### 4.6 Tipe Output Port Data Product

**Document ID:** VOC-UNIVERSAL-TIPE-OUTPUT-PORT
**Tipe Data:** `VARCHAR(20)`
**Nullable:** Tidak
**Referensi:** Data Mesh Principles — Zhamak Dehghani; DPDS Specification

| Kode | Display Name | Definisi | Teknologi Umum |
|---|---|---|---|
| `sql-table` | Tabel SQL | Output berupa tabel atau view yang dapat dikueri via SQL | PostgreSQL, ClickHouse |
| `rest-api` | REST API | Output berupa HTTP REST API | FastAPI, Kong |
| `event-stream` | Event Stream | Output berupa aliran event real-time | Apache Kafka, Redpanda |
| `file-export` | File Export | Output berupa file yang dapat diunduh | Parquet, CSV, JSON di MinIO |
| `graphql` | GraphQL | Output berupa GraphQL API | Hasura, PostGraphile |

---

### 4.7 Klasifikasi Tingkat Keparahan Insiden (Incident Severity)

**Document ID:** VOC-UNIVERSAL-SEVERITY-INSIDEN
**Tipe Data:** `VARCHAR(5)`
**Nullable:** Tidak
**Referensi:** Konvensi industri ITIL v4; Google SRE Book

| Kode | Display Name | Definisi | Response Time Target | Eskalasi |
|---|---|---|---|---|
| `P1` | Kritis | Layanan data product tidak tersedia sama sekali atau ada korupsi data yang mempengaruhi seluruh consumer | 1 jam | On-call + DPO |
| `P2` | Tinggi | SLO breach yang berdampak langsung pada consumer. Degradasi signifikan. | 2 jam | On-call + DPO |
| `P3` | Sedang | Degradasi performa atau anomali kualitas data. SLO near-breach. | 4 jam | Tim data engineering |
| `P4` | Rendah | Pertanyaan, peningkatan minor, tidak ada dampak operasional | 1 hari kerja | Backlog |

---

### 4.8 Level Risiko

**Document ID:** VOC-UNIVERSAL-LEVEL-RISIKO
**Tipe Data:** `VARCHAR(10)`
**Nullable:** Tidak
**Referensi:** ISO 31000:2018 — Risk Management; NIST SP 800-30

| Kode | Skor (L x I) | Display Name | Definisi | Tindakan |
|---|---|---|---|---|
| `kritis` | 7-9 | Kritis | Risiko yang sangat mungkin terjadi dan berdampak sangat tinggi | Harus dimitigasi sebelum go-live |
| `tinggi` | 5-6 | Tinggi | Risiko mungkin terjadi dengan dampak tinggi | Wajib ada rencana mitigasi eksplisit |
| `sedang` | 3-4 | Sedang | Risiko cukup mungkin terjadi dengan dampak moderat | Perlu dipantau dan ada tindakan pencegahan |
| `rendah` | 1-2 | Rendah | Risiko tidak mungkin terjadi atau dampak minimal | Monitor saja, tidak perlu tindakan segera |

---

### 4.9 Status Tindak Lanjut / Task

**Document ID:** VOC-UNIVERSAL-STATUS-TASK
**Tipe Data:** `VARCHAR(20)`
**Nullable:** Tidak
**Referensi:** Konvensi JIRA/Kanban

| Kode | Display Name | Definisi |
|---|---|---|
| `todo` | TODO | Belum dimulai, ada dalam backlog |
| `in-progress` | In Progress | Sedang dikerjakan |
| `in-review` | In Review | Menunggu review/approval |
| `done` | Done | Selesai dan memenuhi DoD |
| `blocked` | Blocked | Tidak dapat dilanjutkan karena ada hambatan eksternal |
| `cancelled` | Dibatalkan | Tidak akan dikerjakan — keputusan eksplisit untuk dibatalkan |

---

### 4.10 Tipe Perubahan Data Contract (Versioning)

**Document ID:** VOC-UNIVERSAL-TIPE-BREAKING-CHANGE
**Tipe Data:** `VARCHAR(20)`
**Nullable:** Tidak
**Referensi:** Semantic Versioning 2.0.0 (semver.org); Data Contract Specification

| Kode | Display Name | Definisi | Dampak Versi |
|---|---|---|---|
| `non-breaking` | Non-Breaking | Penambahan kolom baru (opsional), nilai default baru, penambahan enum value | MINOR atau PATCH bump |
| `breaking` | Breaking | Hapus kolom, ubah tipe data, rename field, hapus enum value yang digunakan | MAJOR bump wajib |
| `deprecation` | Deprecation | Menandai fitur/kolom akan dihapus di versi berikutnya | Notifikasi consumer minimum 3 bulan |

---

## Domain 5: Kelompok Penerima Manfaat

*Sumber: JUKNIS-MBG-2026*

### 5.1 Status Keanggotaan Kelompok Penerima Manfaat

**Document ID:** VOC-KPM-STATUS-KEANGGOTAAN
**Tipe Data:** `BOOLEAN`
**Nullable:** Tidak
**PII:** Tidak
**Referensi:** JUKNIS-MBG-2026

| Kode | Display Name | Definisi |
|---|---|---|
| `TRUE` | Aktif | Individu dinyatakan berstatus aktif menjadi bagian dari kelompok penerima manfaat saat ini |
| `FALSE` | Tidak Aktif | Individu dinyatakan berstatus tidak aktif menjadi bagian dari kelompok penerima manfaat saat ini |

---

## Konversi dan Kompatibilitas Antar Sistem

### Pola Umum Tabel Konversi

Setiap tabel konversi menggunakan format:

```
[Kode Sumber Sistem A] → [Kode Kanonik]
```

Di mana **kode kanonik** selalu merujuk ke vocabulary dalam dokumen ini. Jika kode sumber tidak ada padanannya dalam kode kanonik, gunakan kode `lainnya` atau buat entri baru dengan approval Data Steward.

**Prinsip tata kelola konversi:**
1. Konversi bersifat many-to-one: banyak kode sistem sumber dapat dipetakan ke satu kode kanonik
2. Konversi tidak boleh many-to-many: satu kode kanonik tidak boleh bermakna ganda
3. Perubahan pemetaan konversi dianggap sebagai breaking change dan wajib melalui proses Data Contract update
4. Tabel konversi harus disimpan di Git dan diverifikasi via CI pipeline

---

## Prosedur Penambahan Kosakata Baru

Jika proses bisnis atau sumber data baru memerlukan nilai enum yang belum terdokumentasi di sini, ikuti prosedur berikut:

1. **Identifikasi regulasi** — Cari apakah ada regulasi nasional atau standar internasional yang mendefinisikan nilai tersebut. Jangan membuat kode sendiri jika sudah ada standar resmi.
2. **Konsultasi Data Steward** — Ajukan proposal ke Data Steward domain terkait.
3. **Submit Pull Request** ke file ini (`references/data-vocabulary.md`) dengan penambahan entri baru beserta referensi regulasinya.
4. **Peer review** oleh Data Architect dan Data Steward.
5. **Update tabel konversi** jika sumber data menggunakan kode berbeda.
6. **Bump versi** dokumen Data Contract jika perubahan bersifat breaking.
