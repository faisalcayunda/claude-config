# Proposal Bisnis: {{JUDUL_PROYEK}}

> **Panduan Penggunaan:** Template ini digunakan untuk menyusun proposal bisnis yang ringkas dan berorientasi nilai untuk para pengambil keputusan (C-level, Kepala Dinas, Direktur). Berbeda dengan proposal teknis (Form T-1 s.d. T-7) yang detail dan prosedural, proposal bisnis fokus pada *value proposition*, ROI, dan diferensiasi. Cocok untuk: (1) pitch awal ke enterprise/BUMN, (2) executive summary yang menyertai proposal teknis, (3) engagement internasional. Sesuaikan setiap placeholder `{{...}}` dengan informasi aktual. Dokumen ini mengacu pada praktik terbaik dari Shipley (2025) dan metodologi DAMA-DMBOK 3.0.

---

## 1. Executive Summary

{{EXECUTIVE_SUMMARY}}

> **Panduan Executive Summary:**
> Tulis maksimal 1 halaman yang menjawab 4 pertanyaan kunci:
> 1. **Apa masalahnya?** — Tantangan utama yang dihadapi klien, termasuk *data debt* dan *Cost of Poor Quality* (COPQ).
> 2. **Apa solusinya?** — Pendekatan IDEAS secara ringkas, mengacu pada *value proposition* yang jelas.
> 3. **Apa hasilnya?** — *Outcome* terukur yang dijanjikan, termasuk estimasi ROI 2-3x lipat dari investasi data.
> 4. **Mengapa IDEAS?** — Diferensiasi utama (1-2 kalimat), seperti metodologi terintegrasi atau produk *proprietary*.
>
> Gunakan Minto Pyramid: Governing Thought → Supporting Arguments → Evidence.
> Referensi: `../references/proposal-patterns.md` Section "Minto Pyramid Structure"

---

## 2. Pemahaman Kebutuhan Klien

### 2.1 Konteks Bisnis

{{KONTEKS_BISNIS_KLIEN}}

> **Panduan:** Tunjukkan bahwa IDEAS memahami bisnis klien secara mendalam — bukan hanya kebutuhan teknis. Sertakan: (1) profil singkat klien, (2) visi/misi/strategi klien, (3) tantangan industri, (4) inisiatif strategis yang relevan. Untuk pemerintah, referensikan RPJMD/Renstra dan skor SPBE terbaru (gunakan `../scripts/query_spbe.py` dengan data 2025 jika tersedia).

### 2.2 Tantangan yang Diidentifikasi

| No | Tantangan | Dampak Bisnis | Urgensi |
|:---|:---|:---|:---|
| 1 | {{TANTANGAN_1}} | {{DAMPAK_1}} | {{URGENSI_1}} |
| 2 | {{TANTANGAN_2}} | {{DAMPAK_2}} | {{URGENSI_2}} |
| 3 | {{TANTANGAN_3}} | {{DAMPAK_3}} | {{URGENSI_3}} |

> **Panduan:** Gunakan framework "Hidden Cost of Poor Data" dari pitch deck IDEAS: (1) Fragmented Truth, (2) Snowball Effect, (3) Unclear Ownership. Kuantifikasi dampak jika memungkinkan. Referensi: `../references/proposal-patterns.md` Section "Pain Points"

### 2.3 Cost of Inaction (Biaya Tidak Bertindak)

{{COST_OF_INACTION}}

> **Panduan:** Jelaskan apa yang terjadi jika klien tidak mengambil tindakan. Gunakan COPQ (Cost of Poor Quality) analysis dari Infonomics dan konsep *data debt* dari Deloitte (2025). Referensi: `../references/thought-leadership-frameworks.md` Section 18 (Infonomics).

---

## 3. Solusi yang Ditawarkan

### 3.1 Pendekatan Strategis

{{PENDEKATAN_STRATEGIS}}

> **Panduan:** Jelaskan filosofi pendekatan IDEAS: "Governance that enables, not blocks" — Shift Left, Seamless Integration, Data as Product. Fokus pada *outcome*, bukan aktivitas. Hubungkan dengan tren DAMA-DMBOK 3.0 seperti Data Fabric/Mesh. Referensi: `../references/proposal-patterns.md` Section "Our Approach"

### 3.2 Lingkup Solusi

| Fase | Aktivitas Utama | Durasi | Outcome |
|:---|:---|:---|:---|
| 1. {{FASE_1}} | {{AKTIVITAS_1}} | {{DURASI_1}} | {{OUTCOME_1}} |
| 2. {{FASE_2}} | {{AKTIVITAS_2}} | {{DURASI_2}} | {{OUTCOME_2}} |
| 3. {{FASE_3}} | {{AKTIVITAS_3}} | {{DURASI_3}} | {{OUTCOME_3}} |
| 4. {{FASE_4}} | {{AKTIVITAS_4}} | {{DURASI_4}} | {{OUTCOME_4}} |

### 3.3 Deliverables Utama

| No | Deliverable | Deskripsi | Nilai bagi Klien |
|:---|:---|:---|:---|
| 1 | {{DELIVERABLE_1}} | {{DESKRIPSI_1}} | {{NILAI_1}} |
| 2 | {{DELIVERABLE_2}} | {{DESKRIPSI_2}} | {{NILAI_2}} |
| 3 | {{DELIVERABLE_3}} | {{DESKRIPSI_3}} | {{NILAI_3}} |
| 4 | {{DELIVERABLE_4}} | {{DESKRIPSI_4}} | {{NILAI_4}} |

> **Panduan:** Setiap deliverable harus memiliki kolom "Nilai bagi Klien" — frame dalam bahasa bisnis, bukan teknis. Pastikan kode layanan (misal S1.1) konsisten dengan `../references/services-catalog.md`. Referensi deliverables: `../references/service-deliverables-map.md`

---

## 4. Nilai Tambah & Diferensiasi

### 4.1 Mengapa IDEAS?

| Diferensiasi | Penjelasan | Bukti |
|:---|:---|:---|
| **Proven Track Record** | {{DIFERENSIASI_1}} | {{BUKTI_1}} |
| **Metodologi Terintegrasi** | {{DIFERENSIASI_2}} | {{BUKTI_2}} |
| **Produk Proprietary** | {{DIFERENSIASI_3}} | {{BUKTI_3}} |
| **Knowledge Transfer** | {{DIFERENSIASI_4}} | {{BUKTI_4}} |

> **Panduan:** Gunakan Win Theme Framework dari Shipley (2025) yang ada di `../references/proposal-patterns.md`. Setiap klaim harus didukung bukti kuantitatif dari `../references/case-studies.md` (contoh: SPBE 4.73, 3.448 dataset, 46 OPD). Referensi USP: `../references/competitive-landscape.md`

### 4.2 Return on Investment (ROI)

{{ROI_ANALYSIS}}

> **Panduan:** Kuantifikasi nilai investasi klien. Gunakan framework dari Deloitte (2025):
> - **Efisiensi Operasional:** Pengurangan waktu/biaya proses manual
> - **Peningkatan Kualitas:** Pengurangan error rate, peningkatan data quality score
> - **Kepatuhan Regulasi:** Penghindaran denda/sanksi (UU PDP: maks 2% revenue)
> - **Nilai Data:** Gunakan model valuasi data Infonomics (IVI/BVI/CVI) atau Deloitte (Income/Cost/Market Approach).
> - Referensi: `../references/thought-leadership-frameworks.md` Section 18

---

## 5. Timeline & Milestones

{{TIMELINE_VISUAL}}

> **Panduan:** Sajikan timeline visual yang ringkas (bukan detail Gantt). Fokus pada milestones dan deliverables per fase. Gunakan `../scripts/generate_timeline.py` untuk generate diagram. Referensi: `../references/task-decomposition.md`

---

## 6. Tim Proyek & Tata Kelola

### 6.1 Struktur Tim

{{STRUKTUR_TIM_VISUAL}}

> **Panduan:** Tampilkan struktur tim proyek yang diusulkan, menyoroti peran kunci dan jalur eskalasi. Gunakan peran standar dari `../scripts/rate_card.py` untuk konsistensi. Contoh: Project Manager, Lead Data Architect, Senior Data Engineer.

### 6.2 Profil Tim Inti

| Nama | Peran | Pengalaman Relevan & Sertifikasi |
|:---|:---|:---|
| {{NAMA_TIM_1}} | {{PERAN_TIM_1}} | {{PENGALAMAN_TIM_1}} |
| {{NAMA_TIM_2}} | {{PERAN_TIM_2}} | {{PENGALAMAN_TIM_2}} |
| {{NAMA_TIM_3}} | {{PERAN_TIM_3}} | {{PENGALAMAN_TIM_3}} |

> **Panduan:** Sertakan 2-3 profil singkat dari anggota tim kunci. Fokus pada pengalaman yang paling relevan dengan proyek ini dan sertifikasi profesional (misal, CDMP, PMP, AWS Certified).

---

## 7. Investasi

### 7.1 Opsi Investasi

| Opsi | Lingkup | Durasi | Investasi |
|:---|:---|:---|---:|
| A. {{OPSI_A}} | {{LINGKUP_A}} | {{DURASI_A}} | Rp {{NILAI_A}} |
| B. {{OPSI_B}} | {{LINGKUP_B}} | {{DURASI_B}} | Rp {{NILAI_B}} |
| C. {{OPSI_C}} | {{LINGKUP_C}} | {{DURASI_C}} | Rp {{NILAI_C}} |

> **Panduan Pricing:**
> - Sediakan 2-3 opsi (Good-Better-Best) untuk memberikan pilihan kepada klien.
> - Untuk enterprise/BUMN: gunakan lump sum (Pricing Model 2).
> - Untuk pemerintah: sertakan BoQ detail sebagai lampiran (lihat `boq-template.md`). Pastikan mengacu pada PMK 32/2025 dan Kepka LKPP 93/2025.
> - Untuk pitch awal: boleh tanpa pricing (Pricing Model 3).
> - Referensi: `../references/proposal-patterns.md` Section "Three Pricing Models"
> - Kalkulasi: `../scripts/pricing_engine.py`

### 7.2 Termin Pembayaran

{{TERMIN_PEMBAYARAN}}

> **Panduan:** Lihat `surat-penawaran-template.md` untuk standar termin IDEAS.

---

## 8. Risiko & Mitigasi

| No | Kategori Risiko | Deskripsi Risiko | Rencana Mitigasi |
|:---|:---|:---|:---|
| 1 | Teknis | {{RISIKO_TEKNIS_1}} | {{MITIGASI_TEKNIS_1}} |
| 2 | Operasional | {{RISIKO_OPERASIONAL_1}} | {{MITIGASI_OPERASIONAL_1}} |
| 3 | Ketergantungan | {{RISIKO_KETERGANTUNGAN_1}} | {{MITIGASI_KETERGANTUNGAN_1}} |

> **Panduan:** Identifikasi 3-5 risiko utama yang mungkin terjadi selama proyek. Fokus pada risiko yang relevan bagi klien dan tunjukkan bahwa IDEAS memiliki rencana proaktif untuk menanganinya.

---

## 9. Profil Perusahaan (Ringkas)

**PT Indonesian Data Ecosystem (IDEAS)** adalah firma konsultansi dan implementasi yang berfokus secara eksklusif pada ekosistem data. Didirikan dengan visi menjadi mitra utama dalam membangun ekosistem data yang berdampak, IDEAS telah membantu berbagai organisasi pemerintah dan swasta dalam merancang, membangun, dan mengelola aset data mereka.

### Tiga Pilar Layanan

1. **Advisory & Governance** — Strategi data, tata kelola (termasuk AI Governance), valuasi data (S1.1-S1.5)
2. **Platform & Solution** — Arsitektur data modern (Data Fabric/Mesh), rekayasa data, portal data (S2.1-S2.6)
3. **Empowerment & Managed Services** — Pelatihan, DGO as a Service, managed services (S3.1-S3.4)

> **Catatan:** Pastikan kode layanan (S1.1-S3.4) sesuai dengan `../references/services-catalog.md` versi terbaru.

### Klien Terpilih

{{DAFTAR_KLIEN_TERPILIH}}

> **Panduan:** Cantumkan 5-8 klien paling relevan dengan industri/sektor klien target. Referensi: `../references/company-profile.md` dan `../references/case-studies.md`

---

## 10. Referensi & Case Studies

### Case Study: {{NAMA_CASE_STUDY}}

{{RINGKASAN_CASE_STUDY}}

> **Panduan:** Pilih 1-2 case study yang paling relevan. Gunakan format: Tantangan → Solusi → Hasil (kuantitatif). Referensi: `../references/case-studies.md`

---

## 11. Syarat & Ketentuan

| No | Ketentuan | Detail |
|:---|:---|:---|
| 1 | Masa Berlaku Penawaran | {{MASA_BERLAKU}} hari kalender |
| 2 | Cara Pembayaran | Transfer bank ke rekening PT Indonesian Data Ecosystem |
| 3 | Pembatalan | Pembatalan setelah SPMK dikenakan biaya {{BIAYA_PEMBATALAN}} |
| 4 | Kerahasiaan | Kedua belah pihak menjaga kerahasiaan informasi proyek sesuai UU PDP |
| 5 | Hak Kekayaan Intelektual | Deliverables menjadi milik klien setelah pembayaran lunas |
| 6 | Force Majeure | Sesuai ketentuan hukum yang berlaku di Indonesia |
| 7 | Penyelesaian Sengketa | Musyawarah mufakat, atau melalui Pengadilan Negeri Bandung |

> **Panduan:** Pastikan ketentuan ini telah ditinjau oleh tim legal. Acu pada Perpres 46/2025 untuk proyek pemerintah.

---

## 12. Langkah Selanjutnya

| Langkah | Timeline | PIC |
|:---|:---|:---|
| 1. Presentasi proposal | {{TIMELINE_STEP_1}} | IDEAS + Klien |
| 2. Diskusi dan klarifikasi | {{TIMELINE_STEP_2}} | IDEAS + Klien |
| 3. Negosiasi dan finalisasi | {{TIMELINE_STEP_3}} | IDEAS + Klien |
| 4. Penandatanganan kontrak | {{TIMELINE_STEP_4}} | IDEAS + Klien |
| 5. Kick-off meeting | {{TIMELINE_STEP_5}} | IDEAS + Klien |

---

## 13. Glosarium

| Istilah | Definisi |
|:---|:---|
| **AI Governance** | Tata kelola yang memastikan penggunaan Kecerdasan Buatan (AI) yang etis, transparan, dan akuntabel. |
| **CDMP** | Certified Data Management Professional, sertifikasi dari DAMA International. |
| **Data Fabric** | Arsitektur data terintegrasi yang menyederhanakan akses data di lingkungan hybrid dan multi-cloud. |
| **Data Mesh** | Pendekatan arsitektur data terdesentralisasi yang mengorganisir data berdasarkan domain bisnis. |
| **SPBE** | Sistem Pemerintahan Berbasis Elektronik, penyelenggaraan pemerintahan yang memanfaatkan TIK. |
| **UU PDP** | Undang-Undang Pelindungan Data Pribadi (UU No. 27 Tahun 2022). |

---

**PT Indonesian Data Ecosystem (IDEAS)**
Komplek Margahayu Raya, Jl. Uranus IV Blok C3 No.59, Bandung 40286, Indonesia
contact@data-ecosystem.id | https://data-ecosystem.id

---

> **Cross-References:**
> - Surat Penawaran: `surat-penawaran-template.md`
> - BoQ / Rincian Biaya: `boq-template.md`
> - Proposal Teknis (LKPP): `technical-proposal-template.md`
> - Pitch Deck: `pitch-deck-template.md`
> - Referensi Pola Proposal: `../references/proposal-patterns.md`
> - Referensi Regulasi: `../references/regulatory-standards.md`
> - Katalog Layanan: `../references/services-catalog.md`
> - Panduan Administrasi Proyek: `../references/project-administration-guide.md`
