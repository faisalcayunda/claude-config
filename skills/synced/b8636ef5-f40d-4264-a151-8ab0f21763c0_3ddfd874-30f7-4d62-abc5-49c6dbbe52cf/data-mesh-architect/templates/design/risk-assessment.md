---
title: "Data Risk Assessment & Privacy — <Nama Data Product>"
sidebar_label: "Risk Assessment & Privacy"
sidebar_position: 6
description: "Penilaian risiko data, Record of Processing Activities (RoPA), dan Data Protection Impact Assessment (DPIA)"
tags: [design, risk-assessment, ropa, dpia, privacy, uu-pdp, gdpr]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: design
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Risk Assessment & Privacy

> **Tujuan dokumen ini:** Mengidentifikasi, menilai, dan mendokumentasikan semua risiko yang berkaitan dengan data product ini — mencakup risiko privasi, keamanan, kepatuhan, operasional, dan teknis — beserta rencana mitigasi yang konkret.

:::warning Kewajiban Hukum
Dokumen ini merupakan bagian dari kepatuhan terhadap:
- **UU No. 27 Tahun 2022** tentang Pelindungan Data Pribadi (UU PDP Indonesia)
- **GDPR** jika memproses data warga negara EU
- **PP 71/2019** tentang data residency untuk sistem elektronik publik
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## Definisi Umum

| Atribut | Nilai |
|---|---|
| **Nama Data Product** | `<Nama Data Product>` |
| **Domain / Pengendali Data** | `<Nama Tim / Organisasi>` |
| **Penulis Penilaian** | `<Nama, Jabatan>` |
| **Direview oleh** | `<Legal / DPO Officer>` |
| **Tanggal Penilaian** | `<YYYY-MM-DD>` |
| **Tanggal Review Berikutnya** | `<YYYY-MM-DD>` |

---

## Bagian 1 — Privacy Impact Assessment (Penilaian Dampak Privasi)

`[Mandatory jika memproses data pribadi]`

### 1.1 Screening: Apakah DPIA Penuh Diperlukan?

Jawab setiap pertanyaan:

| Pertanyaan Screening | Jawaban | Poin Risiko |
|---|---|---|
| Apakah memproses data pribadi **spesifik** (kesehatan, biometrik, agama, anak, keuangan)? | `<Ya / Tidak>` | `Ya = +3` |
| Apakah ada **profiling atau scoring** sistematis terhadap individu? | `<Ya / Tidak>` | `Ya = +2` |
| Apakah data diproses dalam **skala besar** (>1.000 data subjek)? | `<Ya / Tidak>` | `Ya = +2` |
| Apakah ada **pemantauan sistematis** terhadap individu (lokasi, aktivitas)? | `<Ya / Tidak>` | `Ya = +2` |
| Apakah menggunakan **teknologi inovatif** atau baru yang belum ada preseden? | `<Ya / Tidak>` | `Ya = +1` |
| Apakah ada **transfer data lintas batas negara**? | `<Ya / Tidak>` | `Ya = +2` |
| Apakah melibatkan **kelompok rentan** (anak-anak, lansia, penyandang disabilitas)? | `<Ya / Tidak>` | `Ya = +2` |

**Total Poin:** `<X poin>`

**Kesimpulan:**
- `0-2 poin` → DPIA **tidak wajib**, Privacy Notice cukup
- `3-5 poin` → DPIA **disarankan**
- `>5 poin` → DPIA **wajib** (UU PDP Pasal 34, GDPR Article 35)

:::danger DPIA Wajib
`[Hapus blok ini jika DPIA tidak wajib]`
Berdasarkan hasil screening, DPIA penuh **wajib dilakukan** sebelum data product ini di-deploy ke production.
:::

---

### 1.2 Data Protection Impact Assessment (DPIA)

`[Isi bagian ini jika DPIA diperlukan dari screening 1.1]`

#### Deskripsi Pemrosesan

| Aspek | Detail |
|---|---|
| **Tujuan Pemrosesan** | `<Untuk apa data pribadi ini diproses>` |
| **Dasar Hukum** | `<Pasal 20 UU PDP: Persetujuan / Kepentingan Publik / Kewajiban Hukum / dst.>` |
| **Kategori Data Subjek** | `<Contoh: Peserta didik, Ibu hamil, Warga negara>` |
| **Kategori Data Pribadi** | `<Contoh: Nama, NIK (umum); Kondisi kesehatan (spesifik)>` |
| **Estimasi Jumlah Data Subjek** | `<~X.XXX.XXX individu>` |
| **Lokasi Pemrosesan** | `<Indonesia — data center: Cikarang / GovCloud>` |
| **Periode Retensi** | `<X tahun, lalu dianonimisasi/dihapus>` |
| **Penerima Data** | `<Internal: Tim A, Tim B. Eksternal: Mitra X>` |

#### Penilaian Risiko Privasi

Skala: Kemungkinan (L) dan Dampak (I): `Rendah=1 / Sedang=2 / Tinggi=3`

| ID | Skenario Risiko | Justifikasi Proporsionalitas | Kemungkinan (L) | Dampak (I) | Risiko (L×I) |
|---|---|---|---|---|---|
| RSK-P01 | `<Eksposur PII ke pihak tidak berwenang>` | `<Identifikasi diperlukan untuk X, namun detail lengkap tidak diperlukan>` | `<Sedang=2>` | `<Tinggi=3>` | `<Kritis TINGGI=6>` |
| RSK-P02 | `<Pemrosesan data anak di bawah umur tanpa consent orang tua>` | `<Diperlukan untuk program pendidikan, dasar hukum: kepentingan publik>` | `<Rendah=1>` | `<Tinggi=3>` | `<Sedang SEDANG=3>` |
| RSK-P03 | `<Retensi data melebihi kebutuhan>` | `<Audit memerlukan histori 5 tahun, namun PII tidak diperlukan setelah periode aktif>` | `<Tinggi=3>` | `<Sedang=2>` | `<Tinggi TINGGI=6>` |
| RSK-P04 | `<Profiling tidak proporsional>` | `<Agregasi lokasi diperlukan untuk logistics optimization>` | `<Sedang=2>` | `<Sedang=2>` | `<Sedang SEDANG=4>` |

**Skala Risiko:** Kritis Tinggi (6-9) | Tinggi Menengah-Tinggi (4-5) | Sedang Sedang (3) | Baik Rendah (1-2)

#### Langkah Mitigasi & Kontrol

| ID Risiko | Strategi | Kontrol Teknis & Organisasi | Risiko Setelah Mitigasi | Action Owner |
|---|---|---|---|---|
| RSK-P01 | `<Minimisasi Data + Masking>` | `<Dynamic Data Masking pada kolom PII; hanya tampilkan data yang diperlukan per role>` | `<Baik Rendah>` | `<Lead DE>` |
| RSK-P02 | `<Dasar Hukum Kuat>` | `<Dokumentasikan dasar hukum; tambahkan privacy notice; pastikan orang tua/wali terinformasi>` | `<Baik Rendah>` | `<Legal Officer>` |
| RSK-P03 | `<Data Lifecycle Management>` | `<Implementasi automated purge: hapus PII setelah X tahun, simpan data agregat anonim>` | `<Baik Rendah>` | `<DBA + DS>` |
| RSK-P04 | `<Aggregasi & Generalisasi>` | `<Bulatkan koordinat ke 3 desimal; gunakan centroid wilayah bukan lokasi tepat>` | `<Baik Rendah>` | `<DA>` |

#### Konsultasi

`[Mandatory — catat siapa yang dikonsultasikan dalam proses DPIA ini]`

| Pihak | Peran | Tanggal Konsultasi | Kesimpulan |
|---|---|---|---|
| `<Legal Officer>` | `<Validasi dasar hukum>` | `<YYYY-MM-DD>` | `<Approved dengan catatan X>` |
| `<Data Subject Representative>` | `<Input dari kelompok terdampak>` | `<YYYY-MM-DD>` | `<Tidak ada keberatan>` |
| `<CISO / Security Team>` | `<Review kontrol keamanan>` | `<YYYY-MM-DD>` | `<Approved>` |

#### Persetujuan DPIA

| Role | Nama | Keputusan | Tanggal |
|---|---|---|---|
| Data Protection Officer / Legal | `<Nama>` | `☐ Approved ☐ Approved with conditions ☐ Rejected` | |
| Data Product Owner | `<Nama>` | `☐ Acknowledged` | |

**Kondisi jika "Approved with conditions":**
> `[Isi kondisi spesifik yang harus dipenuhi sebelum go-live]`

---

## Bagian 2 — Record of Processing Activities (RoPA)

`[Mandatory untuk setiap data product yang memproses data pribadi — UU PDP Pasal 47, GDPR Article 30]`

### RoPA Entry

| Atribut | Detail |
|---|---|
| **Nama Aktivitas Pemrosesan** | `<Nama deskriptif aktivitas, misal: "Profil Penerima Manfaat Program X">` |
| **Nama Data Product** | `<Nama Data Product>` |
| **Tujuan Pemrosesan** | `<Untuk apa data pribadi ini diproses — harus spesifik dan terukur>` |
| **Dasar Hukum** | `<UU PDP Pasal 20: (a) Persetujuan / (b) Kontrak / (c) Kewajiban Hukum / (d) Perlindungan Kepentingan Vital / (e) Kepentingan Umum / (f) Kepentingan Sah>` |
| **Pengendali Data (Controller)** | `<Nama Organisasi + Jabatan yang bertanggung jawab>` |
| **Pemroses Data (Processor)** | `<Nama Tim Domain + Nama Organisasi>` |
| **Kategori Data Subjek** | `<Contoh: Peserta didik SD/SMP, Ibu hamil, Karyawan>` |
| **Kategori Data Pribadi** | `<Daftar lengkap atribut yang diproses>` |
| **Penerima Data Internal** | `<Tim-tim internal yang menerima data>` |
| **Penerima Data Eksternal** | `<Mitra, vendor, lembaga pemerintah lain yang menerima data>` |
| **Transfer ke Luar Negeri** | `<Ya/Tidak. Jika Ya: negara tujuan + safeguard>` |
| **Masa Retensi** | `<Berapa lama data disimpan, dasar penetapan periode retensi>` |
| **Langkah Keamanan Teknis** | `<Enkripsi at-rest/in-transit, masking, RBAC, audit log, dsb.>` |
| **Langkah Keamanan Organisasi** | `<Pelatihan, NDA, access review berkala, dsb.>` |

---

## Bagian 3 — Risk Register (Risiko Non-Privasi)

`[Mandatory]` — *Role: Data Architect + PM*

### 3.1 Penilaian Risiko

Skala: Kemungkinan dan Dampak: `Rendah=1 / Sedang=2 / Tinggi=3`

| ID | Kategori | Deskripsi Risiko | L | I | Skor | Level |
|---|---|---|---|---|---|---|
| RSK-T01 | `<Teknis>` | `<Pipeline gagal karena perubahan skema sumber tanpa notifikasi>` | `3` | `3` | `9` | `Kritis Kritis` |
| RSK-T02 | `<Teknis>` | `<Sumber data tidak tersedia / downtime>` | `2` | `3` | `6` | `Kritis Tinggi` |
| RSK-T03 | `<Teknis>` | `<Volume data tumbuh lebih cepat dari kapasitas infrastruktur>` | `2` | `2` | `4` | `Sedang Sedang` |
| RSK-G01 | `<Governance>` | `<Data digunakan di luar tujuan yang ditetapkan>` | `2` | `3` | `6` | `Kritis Tinggi` |
| RSK-G02 | `<Governance>` | `<Konsumen tidak mengetahui breaking change>` | `2` | `2` | `4` | `Sedang Sedang` |
| RSK-O01 | `<Operasional>` | `<Turnover key personnel (Data Engineer utama)>` | `2` | `2` | `4` | `Sedang Sedang` |
| RSK-C01 | `<Compliance>` | `<Audit menemukan akses tidak sah ke data PII>` | `1` | `3` | `3` | `Sedang Sedang` |

### 3.2 Rencana Mitigasi

| ID Risiko | Strategi | Kontrol | Risiko Sisa | Action Owner | Due Date | Mekanisme Pemantauan |
|---|---|---|---|---|---|---|
| RSK-T01 | `<Preventif: Schema registry + CI/CD contract test>` | `<Implementasi Data Contract test di CI pipeline; alert jika schema drift>` | `<Baik Rendah>` | `<Lead DE>` | `<YYYY-MM-DD>` | `<Automated CI test setiap commit>` |
| RSK-T02 | `<Preventif + Korektif: Retry + fallback>` | `<Retry policy 3x, dead letter queue, SLA agreement dengan tim sumber>` | `<Sedang Sedang>` | `<SRE>` | `<YYYY-MM-DD>` | `<Pipeline monitoring + alert>` |
| RSK-T03 | `<Preventif: Capacity planning>` | `<Monthly cost + volume review; auto-scaling policy>` | `<Baik Rendah>` | `<SRE + PM>` | `<Ongoing>` | `<Monthly cost report>` |
| RSK-G01 | `<Preventif: Terms dalam data contract>` | `<Dokumentasikan purpose limitation; consumer onboarding wajib sign terms>` | `<Baik Rendah>` | `<DPO + Legal>` | `<YYYY-MM-DD>` | `<Annual access audit>` |
| RSK-G02 | `<Preventif: Versioning + komunikasi>` | `<Deprecation notice minimum 3 bulan; changelog otomatis dari Git>` | `<Baik Rendah>` | `<DPO + DE>` | `<Ongoing>` | `<Changelog di setiap release>` |
| RSK-O01 | `<Preventif: Dokumentasi + knowledge transfer>` | `<Runbook lengkap; pair programming; dokumentasi di Git>` | `<Sedang Sedang>` | `<PM>` | `<Ongoing>` | `<Doc coverage review per kuartal>` |
| RSK-C01 | `<Preventif: RBAC + Audit log>` | `<Audit log semua akses PII; quarterly access review>` | `<Baik Rendah>` | `<Security Team>` | `<Ongoing>` | `<Quarterly access review report>` |

### 3.3 Jadwal Review Risiko

| Frekuensi | Aktivitas | Owner |
|---|---|---|
| Per rilis major | Re-assess semua risiko terkait perubahan | DA + Legal |
| Kuartalan | Review status mitigasi, update skor | DPO + PM |
| Tahunan | Full risk assessment refresh | Seluruh tim + Legal |
| Ad-hoc | Review segera jika ada insiden | DPO + DA |
