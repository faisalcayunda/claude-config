---
name: cek-mastersheet-kemenkeu
description: Cek (read-only) file Drive baru dan rapat Fathom baru project Kemenkeu, lalu beri rekap singkat tanpa mengubah sheet.
---

## When to use
Pengguna minta "cek update","cek mastersheet", "ada file/rapat baru?", atau "rekap perubahan" untuk project Kemenkeu pada spreadsheet "[LIV DOC] Mastersheet Kemenkeu" (sheet `Important Link` dan `Rapat`). Skill ini HANYA MEMBACA. Jangan menulis apa pun ke sheet. Untuk menulis, pakai skill `update-mastersheet-kemenkeu`.

## Data tetap
- Folder root Drive: `1IBAlqC9uNZn6eADVMcEGBlCQyhN6M0O3` (Public - SIKD).
- Subfolder: 00_Administrasi `1241fmR3Uq8QJuUwVm5rzuvxgleo03VpA`, 01_Project Management `1HzmR-PIBvmGXn9GflNZRZHrSIf-0fe80`, 02_Client Inputs `1b-gnebDSEg44NIAS7K--FJ0w7PqlwXhp`, 03_Working Analysis `1scGnp5Ej4h9y2aZokhuMPB_EFe5ZL0KT`, 04_Deliverables_Draft `1KzInwbVHQbgOUqO99Llm1njyb1SSLxwX`, 05_Deliverables_Final `1ACUBeYZ2k682xaWLxJrngE-SSDnngESD`, 06_Presentation `1NdcG8J48pLhkfgIJqfLK_trcGjZh3LxC`, 07_Reference `1bADUSpWJCXNO6-qeVpNLe6vA5xqqSW1z`.
- Subfolder yang bisa bertambah: temukan dengan menelusuri anak folder secara rekursif. Jangan hanya memakai daftar di atas.
- Rapat: hanya rapat Kemenkeu. Judul rapat memuat "Kemenkeu" atau "KEMENKEU", atau topiknya SIKD, DJPK, atau Fiscal Data Hub. Lewati rapat lain (Kemenpan, Portal Adpem, Inagov, dan sebagainya). Hanya rapat yang sudah terlaksana.

## Langkah
1. Baca sheet (`get_cell_ranges` atau script read-only) untuk mengumpulkan:
   - ID file yang sudah ada: ambil dari hyperlink kolom C di `Important Link` (RichText link, regex ID 25+ karakter). Cocokkan dengan ID, bukan judul.
   - URL Fathom yang sudah ada: hyperlink kolom E di `Rapat`.
   - Tanggal terakhir pada kolom F `Important Link` dan kolom B `Rapat`.
2. Drive (konektor Google Drive, muat skemanya dengan `tool_search_tool_bm25` bila perlu): telusuri semua folder di bawah root dengan `search_files` memakai `parentId = '<id>'` dan `excludeContentSnippets`. Ikuti `nextPageToken` sampai habis. Satu query per folder, jangan menggabungkan banyak parentId dengan `or` karena sering error. Untuk setiap anak:
   - Ada di sheet (ID cocok)? Bandingkan `modifiedTime` dengan kolom "Terakhir diedit" (zona WIB, UTC+7). Kalau lebih baru, catat sebagai "diubah".
   - Tidak ada di sheet: catat sebagai "baru".
   Abaikan file `[LIV DOC] Mastersheet Kemenkeu` itu sendiri.
3. Fathom (`list_meetings` dengan `created_after` = 2 hari sebelum tanggal rapat terakhir di sheet, `include_summary` true, `max_pages` 3). Saring rapat Kemenkeu, lalu cocokkan URL `fathom.video/calls/<id>` dengan sheet. Yang tidak ada di sheet = rapat baru.
4. Laporkan, tanpa mengubah apa pun.

## Format laporan (singkat)
- **File baru** (n): nama, lokasi folder, owner, tanggal. Satu baris per file.
- **File diubah** (n): nama, tanggal edit lama menjadi tanggal edit baru.
- **Rapat baru** (n): tanggal, judul, tebakan Pihak (Internal atau Kemenkeu), dan satu kalimat topik.
- **Belum dicek / catatan**: folder yang kosong atau gagal diakses, serta konektor yang tidak tersambung.
- Tutup dengan satu kalimat: "Mau saya update sheet-nya? (pakai update-mastersheet-kemenkeu)".
Kalau tidak ada perubahan, tulis "Tidak ada file atau rapat baru sejak <tanggal>".

## Aturan
- Jangan mengarang. Kalau konektor gagal, katakan terus terang dan jangan menebak isi.
- Sebelum menulis, jangan membuka isi file. Metadata cukup.
- Jika konektor tidak ada di daftar tool, panggil `refresh_mcp_connectors` dulu.

Done when: laporan rekap sudah diberikan dan tidak ada sel yang diubah.
