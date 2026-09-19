# Changelog — skill badan-gizi-nasional

## v4.0.0 (2026-06-10) — REBUILD PASS (review komprehensif)

**Perbaikan kritis:**
- Paket terinstal v3.2.0 hanya berisi SKILL.md — SELURUH 28 references, 5 scripts, 5 templates, dan data/ yang dirujuk tidak ada (routing 100% putus, setiap jawaban jatuh ke fallback). v4.0.0 dibangun ulang self-contained: 10 references terkonsolidasi + 3 scripts + 2 templates, semua benar-benar ada di paket.

**Update faktual besar (internet, per 10 Juni 2026):**
- Kepala BGN: Dadan Hindayana dicopot (2 Jun) & tersangka (3 Jun); Kepala baru **Nanik S. Deyang**; wakil baru Agustina Arumsari & Mayjen TNI Trenggono.
- **Moratorium SPPG baru** + portal mitra ditutup; refocusing PM ke 3B; target 82,9 jt "berpotensi tak tercapai".
- Pagu 2026: **Rp268 T** (Rp67 T cadangan dihapus Mei 2026); realisasi 31 Mei: Rp88,15 T, 63,13 jt PM, 29.679 SPPG.
- Keracunan kumulatif per 10 Mei 2026: 445 kejadian / 37.673 korban; suspensi bergelombang 62→1.780→1.152; akreditasi SPPG A/B/C; SLHS 16.046 dapur.
- Regulasi baru: PP 1/2026, PerBGN 1/2026 (limbah), 2/2026 (ZI), 4/2026 (keamanan & mutu pangan), **7/2026 (Satu Data Pemenuhan Gizi Nasional)**, SK 31679/2026 (wilayah terpencil) + perubahan, SE 3/2026.
- SIPGN live publik: sipgn.bgn.go.id/public, portal-doc-sipgn.bgn.go.id, apps Android SIPGN Produksi/Distribusi; nilai proyek (Rp550 M + Rp199 M IoT) & sorotan audit; SAGI 127; "Jaga Dapur MBG"; krisis pencairan dana Juni 2026.

**Koreksi faktual dari dokumen project:**
- Urutan 7 modul DIPERBAIKI sesuai penomoran dokumen Peruri (M2=Logistik/Distribusi, M3=Penerima Manfaat, M5=Pengadaan/Supply Chain) + dokumentasi DUA skema penomoran (ref 07). v3.2.0 hanya memuat satu urutan (skema fungsional) tanpa disambiguasi.
- Jenis dokumen ke-5 = **ERD** (bukan "Data Mapping"); pen test & security test = per MODUL (bukan per submodul); +Laporan Final Proyek (PMO/LFP/SIPGN/XII/2025) = dokumen ke-23.
- 31 submodul dipetakan lengkap dgn kode (PIP, PKS-MR, PMA-01..05, SDK-01..07) dan format nomor `{TYPE}/{KODE}/SIPGN/{ROMAWI}/{TAHUN}` dari dokumen asli.
- Pagu: dibedakan **acuan dasar bahan baku** (8k/10k, at cost) vs **pagu maksimal Rp13.000** (balita–SD 1-3) vs **rata-rata Rp15.000 all-in** — v3.2.0 menyajikan 8k/10k sebagai "pagu bahan baku" tanpa Rp13.000.
- Hari distribusi: 6 hari/313 hari (Juknis) + kebijakan 5 hari sekolah (Mar 2026), aturan libur H-1 paket kering.
- Definisi 3B resmi (bumil/busui/balita ≥6 bln) + disambiguasi.
- Klaim tidak tergrounding dihapus: "150 m² luas min", "52 personel maks", "25.000 CCTV terpasang" → ditandai target desain; "MBG Care" (tidak ada); kompatibilitas model fiktif di frontmatter.
- Referensi baru ekosistem data (ref 09) dari log kerja Pusdatin Apr–Mei 2026: Data Mesh, MDM PM/KPM, MPM, SMO/Pormit, VA Himbara, MonSAKTI, OpenMetadata, dashboard, CR Gateway.

**Struktural:**
- Description frontmatter ditulis ulang (lebih ringkas, trigger baru, disambiguasi); metadata dibersihkan; prinsip **akurasi temporal** + banner knowledge-cutoff ditambahkan; scripts dibangun ulang (3 yang tergrounding; `validate_sppg_location.py` & `nutrition_requirement.py` DIHAPUS karena kriteria/tabel sumbernya tidak tersedia utk digrounding — lebih baik tidak ada daripada mengarang).

## v3.2.0 (2026-04-22) dan sebelumnya
Lihat riwayat di SKILL.md lama (scraping pass 703 dokumen, integrasi master metadata, dsb.). Konten references v3.x hilang dari paket terinstal dan tidak dapat dipulihkan; v4.0.0 menggantikan dengan sumber primer baru.

## v4.1.0 (2026-06-10) — DESCRIPTION OPTIMIZATION PASS
- Description dioptimasi via trigger-eval harness (32 query, 6 kategori positif + 5 kategori negatif near-miss, 3 run/kandidat, split train/holdout 18/14 terstratifikasi, judge = router simulasi dgn 7 skill pesaing nyata).
- Baseline D0: holdout F1 0.949 (recall 0.905), FPR 0.000; kelemahan tunggal: query "draft issue Jira KPM/MPM" (trigger rate 0.33).
- Final D2 (1.023 char): tambah trigger "issue Jira/template narasi SIPGN" + OpenMetadata BGN, klausul prioritas atas skill data umum bila konteks BGN, hapus trigger standalone "Peruri"/"dapur MBG" (risiko FP). Hasil: F1/precision/recall/accuracy 1.000±0.000 di train DAN holdout, 0 query tidak stabil. Kandidat D1 (minimal-edit) juga 1.000 — D2 dipilih krn klausul arbitrase = asuransi generalisasi thd failure mode yg terobservasi.
- Catatan metodologi: claude CLI sandbox tidak ter-autentikasi → loop resmi run_loop.py digantikan harness subagent batch-judging (deviasi: 32 query dinilai satu konteks per run; mitigasi: instruksi penilaian independen per query + 3 run variansi). Raw results: badan-gizi-nasional-workspace/trigger-runs/.
