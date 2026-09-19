# Bill of Quantities (BoQ) — Rincian Biaya Jasa Konsultansi

> **Panduan Penggunaan:** Template ini digunakan untuk menyusun rincian biaya (BoQ) yang melampiri surat penawaran dan proposal. BoQ memberikan transparansi biaya kepada klien dengan breakdown per komponen. Untuk proyek pemerintah, BoQ ini menjadi dasar penyusunan HPS oleh PPK (lihat `../references/rab-hps-methodology.md`). Sesuaikan setiap placeholder `{{...}}` dengan data proyek aktual. Gunakan `../scripts/pricing_engine.py` untuk kalkulasi otomatis.

---

## 🏁 Pre-flight Checklist

Sebelum finalisasi BoQ, pastikan hal-hal berikut telah diperiksa:

- [ ] **Informasi Proyek:** Semua placeholder (`{{...}}`) di tabel Informasi Proyek telah diisi dengan data yang akurat.
- [ ] **Komposisi Tim:** Komposisi tim di Biaya Personel (Bagian A) sudah sesuai dengan kebutuhan proyek dan `../references/human-resources-and-pricing.md`.
- [ ] **Tarif Personel:** Tarif yang digunakan (SBM/Internal) konsisten dengan tipe proyek (Pemerintah/Enterprise).
- [ ] **Biaya Non-Personel:** Semua biaya di Bagian B bersifat *at-cost* dan didukung oleh justifikasi yang kuat (misal: penawaran dari vendor).
- [ ] **Overhead & Profit:** Persentase di Bagian C sesuai dengan standar IDEAS dan regulasi yang berlaku.
- [ ] **Cross-references:** Semua path file yang direferensikan sudah benar dan sesuai dengan struktur direktori skill.
- [ ] **Konsistensi:** Total biaya di Rekapitulasi (Bagian D) sudah sinkron dengan nilai yang tertera di `surat-penawaran-template.md`.

---

## Informasi Proyek

| Field | Isi |
|:---|:---|
| Nama Pekerjaan | {{JUDUL_PEKERJAAN}} |
| Klien | {{NAMA_KLIEN}} |
| Nomor Referensi | {{NOMOR_REFERENSI}} |
| Tanggal Penyusunan | {{TANGGAL}} |
| Masa Pelaksanaan | {{DURASI}} bulan |
| Lokasi Pekerjaan | {{LOKASI}} |
| Disusun oleh | PT Indonesian Data Ecosystem (IDEAS) |

---

## A. Biaya Langsung Personel (Tenaga Ahli)

Biaya personel dihitung berdasarkan jumlah tenaga ahli, durasi penugasan, dan tarif bulanan sesuai level kompetensi. Tarif mengacu pada *rate card* internal IDEAS (lihat `../references/human-resources-and-pricing.md`) dan disesuaikan dengan Standar Biaya Masukan (SBM) yang relevan (misal: PMK 49/2023) untuk proyek pemerintah.

| No | Posisi / Peran | Level | Jumlah Orang | Durasi (Bulan) | Tarif/OB (Rp) | Jumlah (Rp) |
|:---|:---|:---|---:|---:|---:|---:|
| A.1 | {{POSISI_1}} (Team Lead) | {{LEVEL_1}} | {{JML_1}} | {{DUR_1}} | {{TARIF_1}} | {{TOTAL_A1}} |
| A.2 | {{POSISI_2}} | {{LEVEL_2}} | {{JML_2}} | {{DUR_2}} | {{TARIF_2}} | {{TOTAL_A2}} |
| A.3 | {{POSISI_3}} | {{LEVEL_3}} | {{JML_3}} | {{DUR_3}} | {{TARIF_3}} | {{TOTAL_A3}} |
| A.4 | {{POSISI_4}} | {{LEVEL_4}} | {{JML_4}} | {{DUR_4}} | {{TARIF_4}} | {{TOTAL_A4}} |
| A.5 | {{POSISI_5}} | {{LEVEL_5}} | {{JML_5}} | {{DUR_5}} | {{TARIF_5}} | {{TOTAL_A5}} |
| | **Subtotal Biaya Personel** | | | | | **Rp {{SUBTOTAL_A}}** |

> **Catatan Tarif:**
> - OB = Orang-Bulan (1 OB = 22 hari kerja × 8 jam).
> - Untuk proyek pemerintah, gunakan tarif per level sesuai SBM yang berlaku atau *blended rate* yang dapat dipertanggungjawabkan.
> - Untuk proyek enterprise/BUMN, gunakan tarif internal IDEAS dari `../scripts/rate_card.py`.
> - Level mengacu pada skala 1-10 di `../references/human-resources-and-pricing.md`.

---

## B. Biaya Langsung Non-Personel

Biaya non-personel mencakup seluruh biaya operasional yang diperlukan untuk pelaksanaan pekerjaan di luar biaya tenaga ahli. Komponen ini bersifat *at-cost* (sesuai pengeluaran riil) dan disesuaikan dengan kebutuhan proyek.

| No | Uraian | Satuan | Volume | Harga Satuan (Rp) | Jumlah (Rp) |
|:---|:---|:---|---:|---:|---:|
| **B.1** | **Perjalanan Dinas** | | | | |
| B.1.1 | Tiket pesawat PP ({{ASAL}}-{{TUJUAN}}) | Kali | {{VOL_B11}} | {{HS_B11}} | {{TOTAL_B11}} |
| B.1.2 | Transportasi lokal | Hari | {{VOL_B12}} | {{HS_B12}} | {{TOTAL_B12}} |
| B.1.3 | Akomodasi hotel | Malam | {{VOL_B13}} | {{HS_B13}} | {{TOTAL_B13}} |
| B.1.4 | Uang harian (per diem) | OH | {{VOL_B14}} | {{HS_B14}} | {{TOTAL_B14}} |
| **B.2** | **Peralatan & Software** | | | | |
| B.2.1 | Lisensi software/tools (e.g., PowerBI, Tableau) | Paket | {{VOL_B21}} | {{HS_B21}} | {{TOTAL_B21}} |
| B.2.2 | Cloud infrastructure (e.g., AWS, GCP) | Bulan | {{VOL_B22}} | {{HS_B22}} | {{TOTAL_B22}} |
| B.2.3 | Peralatan pendukung (e.g., server, storage) | Paket | {{VOL_B23}} | {{HS_B23}} | {{TOTAL_B23}} |
| **B.3** | **Workshop & Pelatihan** | | | | |
| B.3.1 | Sewa ruang meeting/workshop | Kali | {{VOL_B31}} | {{HS_B31}} | {{TOTAL_B31}} |
| B.3.2 | Konsumsi workshop | Paket | {{VOL_B32}} | {{HS_B32}} | {{TOTAL_B32}} |
| B.3.3 | Materi pelatihan & sertifikasi | Paket | {{VOL_B33}} | {{HS_B33}} | {{TOTAL_B33}} |
| **B.4** | **Dokumentasi & Pelaporan** | | | | |
| B.4.1 | Pencetakan dokumen | Paket | {{VOL_B41}} | {{HS_B41}} | {{TOTAL_B41}} |
| B.4.2 | Penjilidan dan pengemasan | Paket | {{VOL_B42}} | {{HS_B42}} | {{TOTAL_B42}} |
| | **Subtotal Biaya Non-Personel** | | | | **Rp {{SUBTOTAL_B}}** |

> **Catatan Biaya Non-Personel:**
> - Tarif perjalanan dinas mengacu pada SBM yang berlaku untuk proyek pemerintah.
> - Rasio standar: Biaya Non-Personel berkisar 15-30% dari Biaya Personel, tergantung kompleksitas.
> - Untuk proyek lokal (Bandung/Jakarta), komponen B.1 dapat diminimalkan.

---

## C. Overhead, Manajemen & Profit

Komponen ini mencakup biaya tidak langsung (overhead), mitigasi risiko, dan margin keuntungan perusahaan.

| No | Uraian | Basis Perhitungan | Persentase | Jumlah (Rp) |
|:---|:---|:---|---:|---:|
| C.1 | Overhead kantor (biaya operasional) | Subtotal A + B | {{PERSEN_OVERHEAD}}% | {{TOTAL_C1}} |
| C.2 | Manajemen risiko & Kontingensi | Subtotal A + B | {{PERSEN_RISK}}% | {{TOTAL_C2}} |
| C.3 | Keuntungan (profit margin) | Subtotal A + B | {{PERSEN_PROFIT}}% | {{TOTAL_C3}} |
| | **Subtotal Overhead & Profit** | | | **Rp {{SUBTOTAL_C}}** |

> **Catatan Overhead & Profit:**
> - **Proyek Pemerintah:** Mengacu pada Perpres 16/2018 dan perubahannya. Umumnya: Overhead & Profit digabung (maks 15%), ditambah biaya tidak langsung lainnya. Total biaya tidak langsung tidak melebihi persentase tertentu dari total biaya langsung.
> - **Proyek Enterprise:** Overhead & Profit biasanya sudah termasuk (*built-in*) dalam tarif personel (Bagian A).
> - **Manajemen Risiko:** Alokasi 5-10% adalah standar IDEAS untuk mengantisipasi perubahan lingkup atau tantangan tak terduga.

---

## D. Rekapitulasi Biaya

| Komponen | Jumlah (Rp) |
|:---|---:|
| A. Biaya Langsung Personel | {{SUBTOTAL_A}} |
| B. Biaya Langsung Non-Personel | {{SUBTOTAL_B}} |
| C. Overhead, Manajemen & Profit | {{SUBTOTAL_C}} |
| **Subtotal Sebelum Pajak** | **Rp {{SUBTOTAL_SEBELUM_PAJAK}}** |
| PPN (Pajak Pertambahan Nilai) 11% | {{NILAI_PPN}} |
| **TOTAL PENAWARAN (termasuk PPN)** | **Rp {{GRAND_TOTAL}}** |

Terbilang: *{{NILAI_TERBILANG}}*

---

## Asumsi dan Klarifikasi

1.  **Tarif & Durasi:** Tarif personel adalah *all-in* (gaji, tunjangan, asuransi). Durasi dihitung per Orang-Bulan (OB) setara 22 hari kerja.
2.  **Pajak:** PPN (Pajak Pertambahan Nilai) dihitung sebesar 11% sesuai UU HPP No. 7/2021. PPh 23 sebesar 2% (untuk WAPENDAGRI) atau 1.5% (untuk non-WAPENDAGRI) akan dipotong oleh klien dari setiap pembayaran.
3.  **Masa Berlaku:** Penawaran ini berlaku selama **30 (tiga puluh) hari kalender**. Setelahnya, harga dapat disesuaikan.
4.  **Lingkup Kerja:** Biaya ini hanya mencakup pekerjaan yang tertera dalam proposal. Perubahan lingkup akan diatur melalui *Change Order Request* (COR) atau Addendum Kontrak.
5.  **Model Kerja:** Pekerjaan dilaksanakan secara `{{MODEL_KERJA}}` (e.g., on-site, hybrid, remote). Biaya perjalanan (Bagian B.1) disesuaikan dengan model ini.

---

## Panduan Penyesuaian & Otomatisasi

### Proyek Pemerintah (RAB/HPS)

Untuk proyek pemerintah, BoQ ini adalah versi sederhana. Format akhirnya harus mengikuti struktur **RAB (Rencana Anggaran Biaya)** untuk penawaran atau **HPS (Harga Perkiraan Sendiri)** untuk PPK. Gunakan `../references/rab-hps-methodology.md` untuk panduan konversi ke format standar pengadaan (e.g., 6 *work packages*, 24 kolom). Pastikan tarif mengacu pada SBM PMK 49/2023 dan format sesuai Perpres 16/2018 (beserta perubahannya).

### Proyek Enterprise / BUMN

Untuk klien korporat, BoQ dapat disederhanakan menjadi format *lump sum* per fase atau per *deliverable*. Fokus pada *value* yang dihasilkan, bukan detail *man-days*. Gunakan *Pricing Model 2 (Lump Sum)* dari `../references/proposal-patterns.md`.

### Proyek Internasional (Foreign Currency)

Untuk proyek internasional, BoQ disusun dalam mata uang yang disepakati (umumnya USD). Gunakan *daily rates* (tarif harian) untuk fleksibilitas. Tambahkan komponen biaya seperti *international travel*, visa, asuransi perjalanan, dan perhitungkan *currency exchange risk*.

### Otomatisasi dengan `pricing_engine.py`

Untuk mempercepat kalkulasi, gunakan skrip `pricing_engine.py`. Skrip ini dapat menghasilkan total biaya berdasarkan input dari file CSV.

**Contoh Penggunaan:**
```bash
# Navigasi ke direktori skrip
cd scripts/

# Jalankan skrip dengan menunjuk ke file input CSV
python3 pricing_engine.py --input /path/to/your-project-input.csv
```

Skrip akan membaca `rate_card.py` dan menghasilkan output rincian biaya yang bisa disalin ke template ini.

---

## ✍️ Contoh Pengisian BoQ (Studi Kasus Fiktif)

Berikut adalah contoh pengisian BoQ untuk proyek "Penyusunan Master Plan Data Kota X" selama 3 bulan.

**Informasi Proyek:**
- **Nama Pekerjaan:** Penyusunan Master Plan Data Kota X
- **Klien:** Pemerintah Kota X
- **Durasi:** 3 Bulan

**A. Biaya Langsung Personel (Flexible Competency-Based Model)**

Tarif per orang-bulan (OB) dihitung berdasarkan kompetensi individu menggunakan `SALARY_MASTER` dari `rate_card.py`. Setiap personel dinilai berdasarkan **peran**, **pendidikan**, dan **tahun pengalaman** untuk menentukan level dan tarif yang sesuai.

| No | Posisi / Peran | Edu | Exp (thn) | Level | Jml Orang | Durasi (Bln) | Tarif/OB (Rp) | Jumlah (Rp) |
|:---|:---|:---|---:|:---|---:|---:|---:|---:|
| A.1 | Data Valuation Specialist (Team Lead) | S2 | 8 | L15 | 1 | 3 | 20.827.458 | 62.482.374 |
| A.2 | Data Governance Specialist | S1 | 5 | L10 | 1 | 3 | 13.581.463 | 40.744.389 |
| A.3 | Data Analyst | S1 | 3 | L8 | 2 | 2 | 11.755.774 | 47.023.096 |
| | **Subtotal Biaya Personel** | | | | | | | **Rp 150.249.859** |

> **Catatan**: Tarif dihitung dari `SALARY_MASTER` field `external_margin30` (sudah termasuk margin 30%). Untuk proyek yang membutuhkan tenaga ahli senior, gunakan personel dengan pendidikan S2/S3 dan pengalaman ≥8 tahun. Untuk proyek rutin, gunakan personel S1 dengan pengalaman 3-5 tahun untuk efisiensi biaya.

**D. Rekapitulasi Biaya (Contoh)**

| Komponen | Jumlah (Rp) |
|:---|---:|
| A. Biaya Langsung Personel | 150.249.859 |
| B. Biaya Langsung Non-Personel | 30.000.000 |
| C. Overhead, Manajemen & Profit | 27.037.479 |
| **Subtotal Sebelum Pajak** | **Rp 207.287.338** |
| PPN 11% | 22.801.607 |
| **TOTAL PENAWARAN (termasuk PPN)** | **Rp 230.088.945** |

Terbilang: *Dua Ratus Tiga Puluh Juta Delapan Puluh Delapan Ribu Sembilan Ratus Empat Puluh Lima Rupiah*

> **Implementasi**: Gunakan `calculate_gov_proposal_flexible()` di `pricing_engine.py` untuk kalkulasi otomatis. Lihat juga `rate_card.py` untuk daftar lengkap 50 peran × 24 level.

---

> **Cross-References:**
> - Surat Penawaran: `surat-penawaran-template.md`
> - Metodologi RAB/HPS: `../references/rab-hps-methodology.md`
> - Template RAB/HPS (CSV): `rab-hps-template.csv`
> - Kalkulator Biaya: `../scripts/pricing_engine.py`
> - Rate Card Internal: `../scripts/rate_card.py`
> - Referensi SDM & Harga: `../references/human-resources-and-pricing.md`
> - Pola Proposal & Pricing: `../references/proposal-patterns.md`
> - Panduan Administrasi Proyek: `../references/project-administration-guide.md`
