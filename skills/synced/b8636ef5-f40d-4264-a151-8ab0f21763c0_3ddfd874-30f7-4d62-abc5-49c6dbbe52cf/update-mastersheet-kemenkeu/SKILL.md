---
name: "update-mastersheet-kemenkeu"
---


Kalau ada kolom deskripsi, isi dengan:
```
Update sheet Important Link dan Rapat pada Mastersheet Kemenkeu dengan file Drive dan rapat Fathom baru; file baru ditaruh di paling bawah, urut tanggal upload.
```

Isi skill:
```
## When to use
Pengguna minta "update sheet", "update mastersheet", "masukkan file/rapat baru", atau menyetujui hasil `cek-mastersheet-kemenkeu`. Langsung jalankan tanpa menunggu pengguna menjalankan skill cek: lakukan pengecekan (langkah 1 sampai 3 skill `cek-mastersheet-kemenkeu`) bila belum ada hasilnya pada percakapan ini, lalu tulis ke sheet. Fokus hanya project Kemenkeu dan hanya rapat yang sudah terlaksana.

## Struktur sheet
**Important Link** (header baris 4, data mulai baris 5): A No, B Kategori, C Nama (hyperlink), D Owner, E Tanggal upload, F Terakhir diedit, G Catatan. Baris baru SELALU ditambahkan di PALING BAWAH data, urut dari tanggal upload terlama ke terbaru.
**Rapat** (header baris 4, data mulai baris 5, urut dari lama ke baru, rapat baru di baris paling bawah): A No, B Tanggal, C Jam mulai, D Jam selesai, E Rapat (hyperlink Fathom), F Pihak, G Topik utama.

## Pencarian rapat
Jalankan DUA cara dan gabungkan hasilnya: `list_meetings` (sejak tanggal rapat terakhir di sheet dikurangi 2 hari) dan `scan_meeting_summaries` dengan kata kunci "Kemenkeu" (`recorded_by` = "anyone"). Untuk rapat berjudul umum (misalnya "Impromptu ..."), baca ringkasannya dulu (`get_meeting_summary`) dan masukkan hanya bila isinya project Kemenkeu, SIKD, DJPK, BATI, atau Fiscal Data Hub.

## Pencarian file Drive
Telusuri semua folder di bawah root `1IBAlqC9uNZn6eADVMcEGBlCQyhN6M0O3` (Public - SIKD) secara rekursif dengan `search_files` (`parentId = '<id>'`, `excludeContentSnippets`), ikuti `nextPageToken` sampai habis. Satu query per folder. Hasil pencarian global (tanpa parentId) bisa terpotong; jangan andalkan itu saja. Abaikan file `[LIV DOC] Mastersheet Kemenkeu` dan file di luar folder project (laporkan saja bila tampak terkait Kemenkeu).

## Aturan pencocokan (penting)
- Kunci pencocokan = ID file dari URL hyperlink di kolom C, bukan judul.
- Sebelum menambah baris, cek juga baris TANPA hyperlink (isian manual pengguna). Bila judulnya sama atau hampir sama dengan file Drive, anggap file yang sama: tambahkan hyperlink ke baris itu dan perbarui F bila perlu. JANGAN buat baris baru, dan JANGAN ubah judul, kategori, owner, atau catatan manual.
- ID sudah ada di sheet: JANGAN tambah baris dan JANGAN ubah judul. Perbarui hanya "Terakhir diedit" (F) bila Drive lebih baru, dan Owner (D) hanya bila kosong. Laporkan bila judul di Drive berbeda, tanpa menimpa.
- ID belum ada: tambahkan baris baru di paling bawah.
- Rapat: kunci = URL `https://fathom.video/calls/<id>`.
- Jangan menghapus atau menimpa baris yang sudah ada. Jangan menyentuh Catatan (G) yang sudah diisi.

## Mengisi baris baru Important Link
- Posisi: setelah baris data terakhir (baris terakhir yang kolom C-nya terisi). Pakai baris kosong berformat yang sudah ada di bawahnya; bila habis, salin format dari baris data terakhir lewat `copyTo(..., PASTE_FORMAT)`. JANGAN menyisipkan baris di tengah tabel.
- Urutkan baris baru dari tanggal upload (E) terlama ke terbaru.
- C: nama file persis seperti di Drive. Gunakan RichTextValue dengan hyperlink ke URL file. URL ditulis sebagai string literal "https://..." langsung di skrip, bukan hasil perhitungan. Satu skrip hanya boleh memuat sekitar 6 URL; pecah menjadi beberapa skrip bila lebih.
- B Kategori mengikuti pola yang ada:
  - Folder proyek dan folder utama: "Folder Proyek".
  - File di 03_Working Analysis, 04_Deliverables_Draft, 05_Deliverables_Final, 06_Presentation (dan subfolder): "Deliverable".
  - WBS, stakeholder map, dan sejenisnya di 01_Project Management: "Perencanaan".
  - Notulen rapat dan file di 07_Reference selain regulasi: "Referensi".
  - File di 00. Dasar Hukum: "Regulasi".
  - Tidak yakin: pilih yang paling dekat, lalu tandai di laporan agar pengguna mengecek.
- D Owner: pemilik file di Drive. Bila akun pribadi, tulis nama pendek yang sudah dipakai di sheet (Fathur = tryfatur, Willy = willywigias, Iqra = iqra.hardianto), selain itu pakai emailnya.
- E dan F: tanggal dalam WIB (UTC+7). Untuk E pakai `createdTime`, untuk F pakai `modifiedTime`. Tulis sebagai Date jam 12:00 agar tidak bergeser hari. Format sudah "DD MMM YYYY".
- Kosongkan G pada baris baru kecuali ada catatan dari pengguna.
- Jangan memasukkan satu per satu file kerja kecil (skrip .py/.do, .md, .csv, .zip, gambar) di dalam folder kerja yang induknya sudah tercatat. Sebutkan saja jumlahnya di laporan.
- Setelah selesai: hitung ulang kolom A menjadi 1..n berurutan.

## Mengisi baris baru Rapat
- Baris kosong berformat sudah tersedia di bawah data terakhir. Bila habis, salin format dari baris terakhir.
- A: nomor lanjutan. B: tanggal rapat (WIB, jam 12:00).
- C dan D (jam mulai dan selesai): KOSONGKAN. Fathom tidak menyediakannya. Sel kuning diisi manual oleh pengguna.
- E: judul rapat dari Fathom, dengan hyperlink `https://fathom.video/calls/<id>`.
- F Pihak: "Kemenkeu" bila rapat bersama klien Kemenkeu, DJPK, atau BATI. "Internal" bila rapat tim saja (Daily, Debrief, Sync, Weekly internal). Bila ragu, tandai di laporan.
- G Topik utama: 1 sampai 3 kalimat ringkas dalam Bahasa Indonesia dari ringkasan Fathom. Jangan mengarang. Kalau ringkasan tidak ada, isi "(ringkasan belum tersedia)".
- Bila ada beberapa rapat di hari yang sama, urutkan dari terlama ke terbaru.

## Verifikasi (wajib)
Baca ulang dengan `getDisplayValues` dan `getRichTextValues`, lalu pastikan:
- Nomor urut berurutan tanpa celah.
- Semua baris berisi data punya hyperlink di C (Important Link) dan E (Rapat).
- Tidak ada ID file atau URL Fathom yang duplikat.
- Baris baru ada di paling bawah dan urut tanggal upload.
- Format tanggal tampil "DD MMM YYYY".

## Laporan akhir (singkat)
Sebutkan baris yang ditambah (sheet dan nomor baris), baris manual yang diberi hyperlink, baris yang diperbarui tanggal editnya, apa yang sengaja tidak diisi (jam rapat, catatan), file yang tidak dimasukkan, dan hal yang ditentukan sendiri dan perlu dicek (kategori, owner, pihak). Sebutkan folder atau sumber yang tidak bisa dicek. Jangan klaim "semua sudah lengkap" kecuali semua folder benar-benar sudah ditelusuri.

Done when: sheet sudah diperbarui, diverifikasi lewat pembacaan ulang, dan laporan diberikan.
```

