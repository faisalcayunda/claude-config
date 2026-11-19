---
name: update-output-weekly-kemenpan
description: Update slide "Output" di weekly/monthly report INAGov (Portal Administrasi Pemerintah, KemenPANRB) dengan output mingguan dari ClickUp, chat INAGov, dan Google Drive. Jalankan saat user bilang "update output weekly report kemenpan".
---

## When to use
- User bilang "update output weekly report kemenpan" (atau variasinya: "update slide output kemenpan", "recap output INAGov minggu ini").
- Presentasi yang terbuka adalah laporan Portal Administrasi Pemerintah (INAGov, klien KemenPANRB) yang punya slide berjudul "Output".
- User boleh menyebut periode manual ("periode 30 oktober sampai hari ini"). Kalau ada, pakai itu dan lewati Step 1.

## Konstanta (sudah diverifikasi, JANGAN pakai ID lain)
- ClickUp space INAGov: `901811230583`
- ClickUp list Sprint Milestone: `901818617458`
- ClickUp chat channel INAGov: `6-901818584262-8`
- Nama parent task sprint: "Sprint NN (26 Okt - 6 Nov)", dan seterusnya.
- File Figma tim: `https://www.figma.com/design/X8xK3f2hPM12vyjmaWEq6N/INA-GOV-Adpem?node-id=XXXX-XXXXX`
- Zona waktu WIB (UTC+7).

## Step 1 — Tentukan periode
1. Cari slide "Output" terakhir di deck, lalu ambil tanggal terakhir dari subjudulnya (mis. "Sprint 11: 30 Oktober - 5 November 2026" berarti 5 November). Tanggal mulai = H+1. Kalau tidak ada slide Output, tanggal mulai = Jumat minggu lalu.
2. Tanggal selesai:
   - Kalau hari ini Kamis: hari ini.
   - Kalau hari ini Jumat sebelum 06.00 WIB: Kamis kemarin.
   - Selain itu: Kamis terakhir yang sudah lewat.
   - Cek waktu sekarang lewat `clickup_get_user` (current_time).
3. Kalau tanggal selesai < tanggal mulai, berhenti dan tanya user.
4. Siklus normal 7 hari (Jumat–Kamis). Kalau lebih panjang, tetap jalankan dan sebutkan di ringkasan.
5. Cocokkan periode dengan parent task sprint. Kalau periode memotong 2 sprint, pisahkan per sprint (Sabtu/Minggu ikut sprint sebelumnya; task sprint lama yang ditutup saat sprint review di awal periode ikut sprint lama).
6. Tulis satu baris di chat: "Periode: [mulai] s.d. [selesai], Sprint [x]".

Done when: periode dan sprint sudah ditulis di chat.

## Step 2 — Kumpulkan data (cek SEMUA sumber)
1. **ClickUp tasks**: `clickup_filter_tasks` dengan list_ids `["901818617458"]`, include_closed true, order_by updated, fields status/tags/date_updated/date_closed. Ambil task dan subtask dengan date_updated di dalam periode (bandingkan epoch ms dengan batas WIB). Paginasi kalau has_more.
2. Untuk tiap kandidat: `clickup_get_task` dengan include `["description"]` dan `clickup_get_task_comments`. Link output biasanya ada di deskripsi atau komentar. Jalankan paralel dalam batch.
3. **Chat INAGov**: `clickup_get_chat_channel_messages` channel `6-901818584262-8`, paginasi sampai pesan sebelum periode. Buka replies (`clickup_get_chat_message_replies`) untuk thread [DAILY SSxx] dan thread topik yang aktif di periode, termasuk thread lama yang masih dibalas.
4. **Google Drive** (connector Google Drive; kalau tool `search_files` tidak terlihat, muat dulu lewat `tool_search_tool_bm25` dengan query `mcp__google_drive__search_files`):
   - `createdTime >= '<mulai>T00:00+07:00' and createdTime <= '<selesai>T23:59+07:00' and (fullText contains 'Adpem' or fullText contains 'INAGov' or fullText contains 'Portal Administrasi')`, excludeContentSnippets true.
   - Pakai `get_file_metadata` untuk tahu judul asli dokumen yang link-nya ditemukan di ClickUp/chat. Judul ini dipakai untuk menulis Judul Task yang akurat.

Done when: semua task kandidat, thread chat dalam periode, dan hasil pencarian Drive sudah dibaca.

## Step 3 — Aturan isi
- Hanya item yang PUNYA LINK dan output BARU di periode ini. Jangan ulang link yang sama untuk pekerjaan yang sama dari slide Output sebelumnya, kecuali ada tahap/section baru atau pekerjaannya baru Done/Review di periode ini.
- Kalau satu task menghasilkan beberapa dokumen terpisah, pecah jadi beberapa baris.
- JANGAN masukkan:
  - link rekaman Fathom;
  - semua item Kemenkeu/SIKD (Fiscal Data Hub, SIKD Cerdas, DBH Perikanan, DJPK, PMK 93, meeting "IDEAS - KEMENKEU", file milik tim Kemenkeu) dan proyek lain (mis. KLH);
  - link internal ClickUp (doc page, attachment, artifact), screenshot (file .png daily di Drive), link berisi kredensial;
  - deck/file referensi pihak luar (mis. JAKI, s.menpan, surveidigital, file data.menpan.go.id, folder Drive hasil nemu);
  - catatan internal tim (dokumen yang ditandai "sifatnya internal", mis. "Daftar Konfirmasi dan Rekomendasi Fitur");
  - duplikat .docx dari Google Doc yang sama.
- Bersihkan URL dari usp=, ouid=, rtpof=, sd=, t=, viewport=, scaling, p=f. Pertahankan node-id, page-id, gid, slide=.

### Kategori (hanya 4, urutan baris begini)
1. **Design**: tag ui, link Figma.
2. **Research**: tag ba/ux, survei, UT, inventarisasi, desk research, SIT, metric/dashboard discovery, interview stakeholder.
3. **Development**: tag dev/devops, PoC teknis. Hanya kalau ada link non-ClickUp.
4. **Project Management**: tag po/pm/co, TnC/PP, bug & defect, UAT, risk register, laporan.

### Aturan [WIP] (dari user)
- Status ClickUp **done** atau **review** dianggap selesai, jadi TANPA [WIP].
- Status **in progress** / **to do**: tulis prefix "[WIP] " di Judul Task.
- Ikuti status task yang paling langsung menghasilkan dokumen itu (mis. Resume SKM ikut task Interview Stakeholder, bukan parent Discovery SKM). Status ClickUp menang atas label "[WIP]" di nama file Drive.
- Item yang cuma dari chat (tanpa task jelas) dan berupa desain final: tanpa [WIP].

### Judul Task
Singkat dan deskriptif, pakai judul asli dokumen dari Drive kalau ada (mis. "Draft Kebijakan Privasi Portal Adpem v2.0"). Jangan pakai label generik seperti "(1)" atau "(2)".

Done when: daftar baris final (kategori, judul, teks link, URL bersih) sudah siap dan terurut.

## Step 4 — Tulis ke slide
**Mode update (default dari user):** slide recap periode baru MENGGANTIKAN slide Output lama. Isi tabel hanya item periode yang diminta.
1. `duplicate_slide` dari slide Output terakhir (sekali per slide yang dibutuhkan). Lalu hapus slide Output lama (`slide.remove()` via execute_apps_script). User sudah setuju slide Output lama dihapus.
2. Style yang harus dipertahankan (sudah ada di template, set ulang tiap sel setelah setText):
   - Subjudul: font asli, warna `#6C757D`, teks "Sprint NN: D Bulan - D Bulan YYYY" (bulan ditulis lengkap: Oktober, November). Slide kedua dan seterusnya: tambahkan " (lanjutan)".
   - Sel No/Kategori/Judul: Mulish 9pt, tidak bold, hitam `#000000`, tanpa underline. No rata tengah, lainnya rata kiri.
   - Sel Link: Mulish 8pt, underline, warna `SlidesApp.ThemeColorType.HYPERLINK`, setLinkUrl. Teks "Link Figma" untuk Figma, URL bersih lengkap untuk yang lain.
   - Jangan ubah lebar kolom, header, border, atau fill.
3. **Batas script**: satu `execute_apps_script` maksimal 6 URL, dan setiap URL HARUS ditulis sebagai string literal `"https://..."` (tidak boleh dibaca dari dokumen atau digabung). Pecah pengisian jadi beberapa script (mis. 6 baris Design, lalu 4 baris Research, dst.).
4. Maksimal sekitar 9–10 baris per slide. Nomor No lanjut di slide berikutnya, dan mulai dari 1 di tiap sprint. Kalau 2 sprint, buat slide terpisah per sprint.
5. Hapus baris kosong sisa (`table.getRow(k).remove()` dari bawah).
6. Untuk memindah baris antar slide: `insertRow(1)` di tabel tujuan, isi teks, lalu tulis URL sebagai literal.

Done when: semua baris terisi, baris kosong terhapus, slide lama sudah dihapus.

## Step 5 — Verifikasi
- `verify_slides` untuk slide Output. Kalau tabel overflow melewati 405pt, pindahkan baris terakhir ke slide lanjutan. Overlap judul/subjudul memang bawaan template dan boleh diabaikan.
- Baca ulang tabel via script (No | Kategori | Judul) untuk cek urutan, nomor, dan [WIP].

Done when: tidak ada overflow dan isi tabel sesuai daftar final.

## Step 6 — Ringkasan ke user (bahasa Indonesia santai, singkat)
- Periode dan sprint yang dipakai, serta slide mana yang berisi recap.
- Jumlah baris per kategori.
- Output baru yang menonjol.
- Item yang di-skip beserta alasannya.
- Hal yang perlu dicek manual (mis. item dari sebelum periode yang mungkin mau dimasukkan, status yang ambigu).

## Contoh baris
| No | Kategori | Judul Task | Link Output |
|---|---|---|---|
| 1 | Design | Finalisasi Tampilan UI Modul Bantuan & Helpdesk | Link Figma (node-id=8758-92309) |
| 6 | Design | [WIP] Improvement UI Design berdasarkan Hasil UT | Link Figma |
| 14 | Project Management | Draft Kebijakan Privasi Portal Adpem v2.0 | https://docs.google.com/document/d/1HvAD1tkd2uITRQsjKR-pOG3flIS7gZSn4WgygquOXy0/edit |
