# Panduan Administrasi Proyek IDEAS

**Last Updated: February 2026**

Dokumen ini merupakan panduan komprehensif untuk penyiapan dan pengelolaan dokumen administrasi proyek di IDEAS. Panduan ini mencakup seluruh dokumen yang diperlukan mulai dari tahap penawaran hingga penutupan proyek, disesuaikan dengan standar pengadaan pemerintah (merujuk pada [Perpres 46/2025](#6-referensi-regulasi-pengadaan)) dan praktik terbaik industri konsultansi global seperti Shipley dan DAMA.

## 1. Dokumen Administrasi Proyek — Gambaran Umum

Setiap engagement IDEAS memerlukan serangkaian dokumen administrasi yang disesuaikan dengan tipe klien dan mekanisme pengadaan. Tabel berikut merangkum dokumen yang diperlukan per tipe proyek.

| No | Dokumen | Pemerintah (Tender) | Pemerintah (PL) | Enterprise/BUMN | Internasional |
|:---|:---|:---|:---|:---|:---|
| 1 | Surat Penawaran | Wajib | Wajib | Wajib | Opsional |
| 2 | Proposal Teknis (Form T-1 s.d. T-7) | Wajib | Ringkas | Tidak | Tidak |
| 3 | Proposal Bisnis | Opsional | Opsional | Wajib | Wajib |
| 4 | Proposal Full (Type B) | Wajib | Wajib | Opsional | Opsional |
| 5 | Pitch Deck (Type A) | Tidak | Opsional | Wajib | Wajib |
| 6 | BoQ / Rincian Biaya | Wajib | Wajib | Opsional | Opsional |
| 7 | RAB/HPS | Wajib | Wajib | Tidak | Tidak |
| 8 | Dokumen Kualifikasi | Wajib | Wajib | Opsional | Opsional |
| 9 | Profil Perusahaan | Wajib | Wajib | Wajib | Wajib |
| 10 | Surat Perjanjian/Kontrak | Wajib | Wajib | Wajib | Wajib |

Keterangan: **Tender** = Seleksi/Tender melalui SPSE; **PL** = Pengadaan Langsung (nilai ≤ Rp 100 juta untuk jasa konsultansi perorangan, atau ≤ Rp 200 juta untuk badan usaha sesuai [Perpres 46/2025](#6-referensi-regulasi-pengadaan)).

---

## 2. Alur Kerja Penyusunan Dokumen

### 2.1 Alur untuk Proyek Pemerintah (Tender via SPSE)

Alur penyusunan dokumen untuk proyek pemerintah melalui mekanisme tender mengikuti tahapan berikut secara berurutan. Setiap tahapan memiliki output dokumen yang spesifik dan harus diselesaikan sebelum melanjutkan ke tahapan berikutnya.

| Tahap | Aktivitas | Output Dokumen | Template/Script Terkait |
|:---|:---|:---|:---|
| 1. Opportunity Assessment | Analisis peluang, evaluasi go/no-go | Internal assessment memo | `scripts/query_spbe.py` |
| 2. Capture Planning | Identifikasi win strategy, mapping layanan | Service recommendation | `scripts/recommend_service.py` |
| 3. Penyusunan Proposal Teknis | Pengisian Form T-1 s.d. T-7 | Dokumen Penawaran Teknis | `templates/technical-proposal-template.md` |
| 4. Penyusunan Proposal Full | Penulisan proposal lengkap | Proposal (Type B) | `templates/proposal-template.md` |
| 5. Kalkulasi Biaya | Perhitungan RAB dan BoQ | RAB + BoQ | `scripts/generate_rab.py`, `templates/boq-template.md` |
| 6. Penyusunan Surat Penawaran | Pembuatan surat penawaran resmi | Surat Penawaran | `templates/surat-penawaran-template.md` |
| 7. Review & Validasi | Pink/Red/Gold Team review | Reviewed documents | Shipley Color Team process |
| 8. Upload ke SPSE | Unggah seluruh dokumen | Submitted bid | — |

### 2.2 Alur untuk Proyek Enterprise/BUMN

Alur untuk proyek enterprise dan BUMN lebih fleksibel dan berorientasi pada consultative selling. Fokus utama adalah membangun pemahaman kebutuhan klien dan menyajikan solusi yang bernilai.

| Tahap | Aktivitas | Output Dokumen | Template/Script Terkait |
|:---|:---|:---|:---|
| 1. Discovery Meeting | Identifikasi kebutuhan klien | Meeting notes | — |
| 2. Penyusunan Pitch Deck | Pembuatan presentasi pitch | Pitch Deck (Type A) | `templates/pitch-deck-template.md` |
| 3. Presentasi & Diskusi | Presentasi ke decision makers | — | — |
| 4. Penyusunan Proposal Bisnis | Penulisan proposal bisnis | Proposal Bisnis | `templates/business-proposal-template.md` |
| 5. Penyusunan Surat Penawaran | Pembuatan penawaran resmi + BoQ | Surat Penawaran + BoQ | `templates/surat-penawaran-template.md`, `templates/boq-template.md` |
| 6. Negosiasi | Diskusi harga dan lingkup | Revised proposal | — |
| 7. Kontrak | Penandatanganan perjanjian | Surat Perjanjian | — |

---

## 3. Standar Kualitas Dokumen

### 3.1 Prinsip Umum

Seluruh dokumen IDEAS harus memenuhi standar kualitas berikut yang mencerminkan profesionalisme dan komitmen perusahaan terhadap keunggulan.

| Prinsip | Penjelasan | Implementasi |
|:---|:---|:---|
| **Akurasi** | Seluruh data, angka, dan referensi harus akurat dan dapat diverifikasi | Cross-check dengan `references/`, gunakan scripts untuk kalkulasi |
| **Konsistensi** | Terminologi, format, dan branding harus konsisten antar dokumen | Gunakan templates standar, ikuti brand assets (`templates/LogoIDEASLandscape.png`, etc.) and Section 3.3 above |
| **Kelengkapan** | Seluruh informasi yang diminta harus terjawab tanpa ada bagian kosong | Gunakan checklist per tipe dokumen (lihat [Section 5](#5-checklist-dokumen-per-tipe-proyek)) |
| **Kejelasan** | Bahasa harus jelas, ringkas, dan mudah dipahami oleh target pembaca | Hindari jargon berlebihan, gunakan tabel dan visual, lihat [Glossary](#9-glossary-of-terms) |
| **Profesionalisme** | Tampilan visual harus rapi, bersih, dan mencerminkan brand IDEAS | Gunakan `scripts/generate_document.py` untuk output akhir |

### 3.2 Standar Format Dokumen

Standar format berikut berlaku untuk seluruh dokumen yang dihasilkan IDEAS, baik dalam format digital maupun cetak.

| Elemen | Standar |
|:---|:---|
| Font Body | 10-11pt, serif atau sans-serif yang mudah dibaca |
| Font Heading | 14-18pt, bold, navy (#0A0A5C) |
| Font Tabel | 8.5-9pt untuk konten tabel |
| Margin | 2.5cm (atas/bawah), 2cm (kiri/kanan) |
| Spasi | 1.15-1.5 line spacing |
| Bahasa | Indonesia (proyek domestik), English (proyek internasional) |
| Penomoran | Hierarkis: 1. → 1.1 → 1.1.1 |
| Header | Logo IDEAS + judul dokumen |
| Footer | Tagline + nomor dokumen + halaman |

### 3.3 Standar Branding

Seluruh dokumen harus menggunakan elemen branding IDEAS yang konsisten untuk membangun brand recognition dan profesionalisme.

| Elemen | Spesifikasi |
|:---|:---|
| Logo | `templates/LogoIDEASLandscape.png` (header) atau `templates/Logo_ideas.png` (cover) |
| Warna Primer | Navy #0A0A5C |
| Warna Sekunder | Gold #C4A35A, Light Gray #F5F5F5 |
| Tagline | "Building Indonesia's Data Ecosystem" |
| Legal Entity | PT Indonesian Data Ecosystem |
| Brand Name | IDEAS — Indonesian Data Ecosystem Agency & Solutions |

---

## 4. Sistem Penomoran Dokumen

IDEAS menggunakan sistem penomoran dokumen yang terstruktur untuk memudahkan pelacakan dan pengelolaan dokumen.

### 4.1 Format Penomoran

Format standar penomoran dokumen IDEAS mengikuti pola berikut:

`IDEAS/[TIPE]/[TAHUN]/[NOMOR_URUT]`

### 4.2 Kode Tipe Dokumen

| Kode | Tipe Dokumen | Contoh |
|:---|:---|:---|
| SP | Surat Penawaran | IDEAS/SP/2026/001 |
| PROP | Proposal (Teknis/Bisnis/Full) | IDEAS/PROP/2026/001 |
| PT | Pitch Deck | IDEAS/PT/2026/001 |
| RAB | Rencana Anggaran Biaya | IDEAS/RAB/2026/001 |
| BOQ | Bill of Quantities | IDEAS/BOQ/2026/001 |
| SPK | Surat Perintah Kerja | IDEAS/SPK/2026/001 |
| INV | Invoice | IDEAS/INV/2026/001 |
| LAP | Laporan (Pendahuluan/Antara/Akhir) | IDEAS/LAP/2026/001 |
| BA | Berita Acara | IDEAS/BA/2026/001 |
| MoM | Minutes of Meeting | IDEAS/MoM/2026/001 |

---

## 5. Checklist Dokumen per Tipe Proyek

### 5.1 Checklist Proyek Pemerintah (Tender)

Checklist berikut memastikan kelengkapan dokumen untuk pengadaan jasa konsultansi pemerintah melalui mekanisme tender SPSE.

| No | Dokumen | Status | Catatan |
|:---|:---|:---|:---|
| 1 | Surat Penawaran (bermaterai) | ☐ | Ditandatangani Direktur, sesuai `templates/surat-penawaran-template.md` |
| 2 | Dokumen Penawaran Teknis | ☐ | Form T-1 s.d. T-7 lengkap, sesuai `templates/technical-proposal-template.md` |
| 3 | Form T-1: Data Organisasi | ☐ | Maks 2 halaman latar belakang |
| 4 | Form T-2: Pengalaman Kerja Sejenis | ☐ | 10 tahun terakhir, relevan dengan `references/case-studies.md` |
| 5 | Form T-3: Uraian Pengalaman Detail | ☐ | Per proyek relevan |
| 6 | Form T-4: Pendekatan & Metodologi | ☐ | Maks 50 halaman, sinkron dengan `references/proposal-patterns.md` |
| 7 | Form T-5: Jadwal Pelaksanaan | ☐ | Gantt chart, output dari `scripts/generate_timeline.py` |
| 8 | Form T-6: CV Tenaga Ahli | ☐ | Per personel inti, sesuai `references/human-resources-and-pricing.md` |
| 9 | Form T-7: Komposisi Tim | ☐ | Tenaga Ahli + Teknis, sesuai `references/human-resources-and-pricing.md` |
| 10 | Dokumen Penawaran Biaya (BoQ) | ☐ | Breakdown personel + non-personel, output dari `scripts/generate_rab.py` |
| 11 | Dokumen Kualifikasi | ☐ | NIB, NPWP, neraca, SPT |
| 12 | Surat Pernyataan (pakta integritas) | ☐ | Bermaterai |
| 13 | Profil Perusahaan | ☐ | Terbaru, dari `references/company-profile.md` |
| 14 | Fotokopi ijazah & sertifikasi tenaga ahli | ☐ | Sesuai Form T-6 |
| 15 | Referensi kerja / surat keterangan | ☐ | Dari pemberi kerja sebelumnya |

### 5.2 Checklist Proyek Enterprise/BUMN

Checklist berikut memastikan kelengkapan dokumen untuk engagement dengan klien enterprise dan BUMN.

| No | Dokumen | Status | Catatan |
|:---|:---|:---|:---|
| 1 | Pitch Deck (Type A) | ☐ | 15-32 halaman, sesuai `templates/pitch-deck-template.md` |
| 2 | Proposal Bisnis | ☐ | Fokus value proposition, sesuai `templates/business-proposal-template.md` |
| 3 | Surat Penawaran | ☐ | Dengan BoQ ringkas, sesuai `templates/surat-penawaran-template.md` |
| 4 | BoQ / Rincian Biaya | ☐ | Opsional (bisa lump sum), sesuai `templates/boq-template.md` |
| 5 | Profil Perusahaan | ☐ | Versi ringkas, dari `references/company-profile.md` |
| 6 | Case Studies Relevan | ☐ | 1-2 case study, dari `references/case-studies.md` |
| 7 | NDA (jika diminta) | ☐ | Sebelum sharing informasi sensitif |

### 5.3 Checklist Proyek Internasional

Checklist ini mencakup dokumen untuk klien internasional, dengan penekanan pada bahasa Inggris, standar global, dan kepatuhan lintas negara.

| No | Dokumen | Status | Catatan |
|:---|:---|:---|:---|
| 1 | Pitch Deck (Type A) — English | ☐ | Tanpa pricing, fokus pada kapabilitas dan value. |
| 2 | Proposal Bisnis — English | ☐ | Fokus pada metodologi, ROI, dan perbandingan dengan standar global. |
| 3 | Company Profile — English | ☐ | Versi lengkap, menyoroti pengalaman internasional dan tim. |
| 4 | Team CVs — English | ☐ | Per personel kunci, format Europass atau sesuai permintaan klien. |
| 5 | Reference Letters | ☐ | Dari klien sebelumnya, idealnya dari perusahaan multinasional. |
| 6 | Compliance Statement | ☐ | Pernyataan kepatuhan terhadap regulasi internasional (e.g., GDPR, CCPA). |
| 7 | Master Service Agreement (MSA) | ☐ | Draft MSA dalam bahasa Inggris sebagai dasar negosiasi kontrak. |

---

## 6. Referensi Regulasi Pengadaan

Dokumen administrasi proyek pemerintah harus mematuhi regulasi pengadaan yang berlaku. Berikut adalah regulasi utama yang menjadi acuan.

| Regulasi | Tentang | Relevansi |
|:---|:---|:---|
| Perpres 46/2025 | Perubahan Kedua atas Perpres 16/2018 tentang Pengadaan Barang/Jasa Pemerintah | Mekanisme pengadaan, HPS, evaluasi, kewajiban E-Katalog. |
| PMK 32/2025 | Standar Biaya Masukan (SBM) TA 2026 | Tarif honorarium, perjalanan dinas, batas tertinggi biaya. Kunci untuk RAB/HPS. |
| Perlem LKPP 12/2021 | Pedoman Pelaksanaan Pengadaan | Prosedur detail seleksi jasa konsultansi. |
| Perpres 95/2018 jo. 132/2022 | Sistem Pemerintahan Berbasis Elektronik (SPBE) | Konteks utama untuk sebagian besar proyek data pemerintah. |
| UU 27/2022 | Perlindungan Data Pribadi (PDP) | Kepatuhan data privacy dalam setiap proyek. |
| Perpres 39/2019 | Satu Data Indonesia (SDI) | Konteks proyek integrasi dan standardisasi data pemerintah. |
| PP 49/2025 | Perubahan Kedua PP 36/2021 tentang Pengupahan | Acuan standar pengupahan, bukan pengadaan. Penting untuk struktur biaya tenaga kerja internal. |

> **Detail regulasi lengkap:** Lihat `references/regulatory-standards.md`

---

## 7. Tips Penyusunan Dokumen Berkualitas

### 7.1 Surat Penawaran

Surat penawaran yang efektif harus ringkas namun lengkap, menunjukkan profesionalisme dan perhatian terhadap detail. Pastikan nomor surat terurut, lampiran lengkap, dan nilai penawaran konsisten dengan BoQ. Untuk proyek pemerintah, surat harus bermaterai dan ditandatangani oleh pejabat yang berwenang (Direktur).

### 7.2 Proposal Teknis

Proposal teknis yang unggul menunjukkan pemahaman mendalam terhadap KAK, metodologi yang terstruktur, dan tim yang kompeten. Gunakan Minto Pyramid untuk struktur argumentasi, sertakan "Wow Factor" di setiap bagian, dan pastikan setiap klaim didukung bukti kuantitatif. Bobot evaluasi teknis 60-70% menjadikan kualitas proposal teknis sebagai faktor penentu utama.

### 7.3 BoQ / Rincian Biaya

BoQ yang baik memberikan transparansi penuh tanpa mengungkapkan margin internal. Pastikan total BoQ konsisten dengan nilai di surat penawaran, satuan dan volume logis, dan tarif mengacu pada standar yang berlaku. Untuk proyek pemerintah, BoQ harus dapat diverifikasi terhadap SBM (PMK 32/2025). Pertimbangkan juga pendekatan valuasi data dari Deloitte (Income/Cost/Market approach) saat mengestimasi nilai dari data-driven deliverables.

### 7.4 Proposal Bisnis

Proposal bisnis yang efektif berbicara dalam bahasa bisnis, bukan teknis. Fokus pada ROI, value proposition, dan diferensiasi. Sediakan 2-3 opsi investasi (Good-Better-Best) untuk memberikan fleksibilitas kepada klien. Gunakan case studies dan testimonial sebagai social proof.

---

## 8. Integrasi dengan Scripts dan Tools IDEAS

Seluruh proses penyusunan dokumen administrasi dapat dipercepat dengan memanfaatkan scripts dan tools yang tersedia dalam skill IDEAS. Untuk panduan eksekusi lengkap, selalu rujuk ke file `SKILL.md`.

| Kebutuhan | Script/Tool | Perintah Contoh |
|:---|:---|:---|
| Kalkulasi biaya | `pricing_engine.py` | Lihat `SKILL.md` Step 3 |
| Generate RAB | `generate_rab.py` | `python3 scripts/generate_rab.py --project "..." --services S1.1,S1.2` |
| Estimasi biaya layanan | `estimate_service_cost.py` | `python3 scripts/estimate_service_cost.py --services S1.1,S1.2` |
| Generate proposal | `generate_proposal.py` | `python3 scripts/generate_proposal.py --type proposal --client "..."` |
| Generate pitch deck | `generate_proposal.py` | `python3 scripts/generate_proposal.py --type pitch --client "..."` |
| Query SPBE data | `query_spbe.py` | `python3 scripts/query_spbe.py --top 10 --sort opportunity` |
| Rekomendasi layanan | `recommend_service.py` | `python3 scripts/recommend_service.py --need "..."` |
| Generate Dokumen Final | `generate_document.py` | `python3 scripts/generate_document.py --input doc.md --output doc.pdf` |

---

## 9. Glossary of Terms

| Istilah | Kepanjangan / Definisi |
|:---|:---|
| **BoQ** | Bill of Quantities. Rincian detail item pekerjaan beserta volume dan harga satuan. |
| **DAMA-DMBOK** | Data Management Body of Knowledge. Kerangka kerja standar global untuk manajemen data. Versi 3.0 sedang dalam pengembangan (status per Feb 2026). |
| **HPS** | Harga Perkiraan Sendiri. Estimasi biaya yang disusun oleh pemilik proyek (pemerintah). |
| **KAK** | Kerangka Acuan Kerja. Dokumen yang menjelaskan latar belakang, tujuan, lingkup, dan spesifikasi pekerjaan. |
| **LKPP** | Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah. |
| **PL** | Pengadaan Langsung. Metode pemilihan penyedia untuk pekerjaan dengan nilai tertentu. |
| **PMK** | Peraturan Menteri Keuangan. |
| **Perpres** | Peraturan Presiden. |
| **RAB** | Rencana Anggaran Biaya. Estimasi biaya yang disusun oleh penyedia jasa. |
| **SBM** | Standar Biaya Masukan. Batas tertinggi biaya yang ditetapkan oleh Menteri Keuangan. |
| **SPSE** | Sistem Pengadaan Secara Elektronik. |

---

## 10. Cross-References

Panduan ini terintegrasi dengan seluruh komponen skill IDEAS sebagai berikut:

| Kebutuhan | File Referensi Terkait |
|:---|:---|
| Panduan Penggunaan Skill | `SKILL.md` |
| Template Surat Penawaran | `templates/surat-penawaran-template.md` |
| Template BoQ | `templates/boq-template.md` |
| Template Proposal Teknis (LKPP) | `templates/technical-proposal-template.md` |
| Template Proposal Bisnis | `templates/business-proposal-template.md` |
| Template Proposal Full (Type B) | `templates/proposal-template.md` |
| Template Pitch Deck (Type A) | `templates/pitch-deck-template.md` |
| Template RAB/HPS (CSV) | `templates/rab-hps-template.csv` |
| Metodologi RAB/HPS | `references/rab-hps-methodology.md` |
| Pola Proposal & Pitch | `references/proposal-patterns.md` |
| SDM & Tarif | `references/human-resources-and-pricing.md` |
| Regulasi & Standar | `references/regulatory-standards.md` |
| Profil Perusahaan | `references/company-profile.md` |
| Studi Kasus | `references/case-studies.md` |
| Lanskap Kompetitif | `references/competitive-landscape.md` |
| Katalog Layanan | `references/services-catalog.md` |
| Peta Deliverables Layanan | `references/service-deliverables-map.md` |
| Dekomposisi Tugas | `references/task-decomposition.md` |
| Kerangka Kerja Bisnis | `references/business-frameworks.md` |

---

## 11. Version History

| Versi | Tanggal | Perubahan | Author |
|:---|:---|:---|:---|
| 1.0 | Jan 2025 | Dokumen awal dibuat. | Manus |
| 1.1 | Feb 2026 | Update regulasi (Perpres 46/2025, PMK 32/2025), penambahan detail checklist internasional, glossary, dan cross-references. | Manus |
