---
name: update-mastersheet-kemenkeu
description: Update sheet Important Link dan Rapat pada Mastersheet Kemenkeu dengan file Drive dan rapat Fathom baru, sesuai aturan pencocokan dan format yang sudah disepakati.
---

## When to use
Pengguna minta "update sheet","update mastersheet", "masukkan file/rapat baru", atau menyetujui hasil `cek-mastersheet-kemenkeu`. Langsung jalankan tanpa menunggu pengguna menjalankan skill cek: lakukan pengecekan (langkah 1 sampai 3 skill `cek-mastersheet-kemenkeu`) bila belum ada hasilnya pada percakapan ini, lalu tulis ke sheet. Fokus hanya project Kemenkeu dan hanya rapat yang sudah terlaksana.

## Struktur sheet
**Important Link** (header baris 4, data mulai baris 5): A No, B Kategori, C Nama (hyperlink), D Owner, E Tanggal upload, F Terakhir diedit, G Catatan.
**Rapat** (header baris 4, data mulai baris 5, urut dari lama ke baru, rapat baru di baris paling bawah): A No, B Tanggal, C Jam mulai, D Jam selesai, E Rapat (hyperlink Fathom), F Pihak, G Topik utama.

## Aturan pencocokan (penting)
- Kunci pencocokan = ID file dari URL hyperlink di kolom C, bukan judul.
- ID sudah ada di sheet: JANGAN tambah baris dan JANGAN ubah judul manual. Perbarui hanya "Terakhir diedit" (F) bila Drive lebih baru, dan Owner (D) hanya bila kosong. Laporkan bila judul di Drive berbeda, tanpa menimpa.
- ID belum ada: tambahkan baris baru.
- Rapat: kunci = URL `https://fathom.video/calls/<id>`.
- Jangan menghapus atau menimpa baris yang sudah ada. Jangan menyentuh Catatan (G) yang sudah diisi.

## Mengisi baris baru Important Link
- C: nama file persis seperti di Drive. Gunakan RichTextValue dengan hyperlink ke URL file. URL ditulis sebagai string literal "https://..." langsung di skrip, bukan hasil perhitungan, karena skrip dengan link yang dihitung ditolak. Bila perlu, tulis tiap link secara eksplisit.
- B Kategori mengikuti pola yang ada:
  - Folder proyek dan folder utama: "Folder Proyek".
  - File di 04_Deliverables_Draft, 05_Deliverables_Final, 06_Presentation (dan subfolder): "Deliverable".
  - WBS, stakeholder map, dan sejenisnya di 01_Project Management: "Perencanaan".
  - File di 07_Reference selain regulasi: "Referensi".
  - File di 00. Dasar Hukum: "Regulasi".
  - Tidak yakin: pilih yang paling dekat, lalu tandai di laporan agar pengguna mengecek.
- D Owner: pemilik file di Drive. Bila akun pribadi, tulis nama pendek yang sudah dipakai di sheet (Fathur = tryfatur, Willy = willywigias, Iqra = iqra.hardianto), selain itu pakai emailnya.
- E dan F: tanggal dalam WIB (UTC+7). Untuk E pakai `createdTime`, untuk F pakai `modifiedTime`. Tulis sebagai Date jam 12:00 agar tidak bergeser hari. Format sudah "DD MMM YYYY".
- Sisipkan baris dengan `insertRowsAfter` di posisi yang logis, yaitu setelah kelompok kategori yang sama, atau setelah folder induknya untuk isi folder. Salin format dari baris tetangga lewat `copyTo(..., PASTE_FORMAT)`. Kosongkan G pada baris baru kecuali ada catatan dari pengguna.
- Setelah semua sisipan: hitung ulang kolom A menjadi 1..n berurutan.

## Mengisi baris baru Rapat
- Baris kosong berformat sudah tersedia di bawah data terakhir. Bila habis, salin format dari baris terakhir.
- A: nomor lanjutan. B: tanggal rapat (WIB, jam 12:00).
- C dan D (jam mulai dan selesai): KOSONGKAN. Fathom tidak menyediakannya. Sel kuning diisi manual oleh pengguna.
- E: judul rapat dari Fathom, dengan hyperlink `https://fathom.video/calls/<id>`.
- F Pihak: "Kemenkeu" bila rapat bersama klien Kemenkeu atau DJPK (misalnya Kick off, Koordinasi, Weekly SIKD). "Internal" bila rapat tim saja (Daily, Debrief, Weekly internal). Bila ragu, tandai di laporan.
- G Topik utama: 1 sampai 3 kalimat ringkas dalam Bahasa Indonesia dari ringkasan Fathom (`include_summary`). Jangan mengarang. Kalau ringkasan tidak ada, isi "(ringkasan belum tersedia)".
- Urutan kronologis: bila ada beberapa rapat di hari yang sama, urutkan sesuai urutan di Fathom, dari terlama ke terbaru.

## Verifikasi (wajib)
Baca ulang baris yang diubah dengan `getDisplayValues` dan pastikan:
- Nomor urut berurutan tanpa celah.
- Hyperlink C dan E terisi (cek `getRichTextValues`).
- Tidak ada ID file atau URL Fathom yang duplikat.
- Format tanggal tampil "DD MMM YYYY".

## Laporan akhir (singkat)
Sebutkan baris yang ditambah (sheet dan nomor baris), baris yang diperbarui tanggal editnya, apa yang sengaja tidak diisi (jam rapat, catatan), dan hal yang ditentukan sendiri dan perlu dicek (kategori, owner, pihak). Sebutkan folder atau sumber yang tidak bisa dicek. Jangan klaim "semua sudah lengkap" kecuali semua folder benar-benar sudah ditelusuri.

Done when: sheet sudah diperbarui, diverifikasi lewat pembacaan ulang, dan laporan diberikan.
