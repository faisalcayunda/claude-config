# Dokumentasi Sumber Data MBG Command Center

## Context

`apps/mbg-cc` menayangkan `data/mbg-dashboard.json` (92 KB, 38 provinsi, 51 metrik aktif) dan file itu sampai sekarang dirakit manual. Generatornya, `scripts/gabung-data.py`, tercantum di `package.json` tapi masuk `.gitignore` dan tidak ada di repo. Begitu juga validatornya, `scripts/validasi-data.mjs`. Artinya tidak ada satu pun orang selain pemilik mesin asal yang bisa mereproduksi file datanya, dan `npm run validasi` mati.

`docs/Mapping Metrics Dashboard Executive.xlsx` sebenarnya sudah memetakan tiap metrik ke dashboard sumbernya: 16 metrik dari Metabase (`kpm-replica.public.mv_dm_rekap_provinsi_kpm`), 25 dari empat dashboard Tableau (Kinops Executive, Kinops Executive - Provinsi, Manajemen SPPG, Reviu Menu MBG), dan 10 metrik tanpa sumber sama sekali. Peta itu tinggal di satu spreadsheet, kolomnya belum ternormalisasi (SQL Trino nyangkut di kolom `DB` untuk baris Tableau), dan tidak bisa dibaca mesin.

Tujuannya: kumpulkan pengetahuan yang tersebar di empat tempat (dataset, xlsx, dokumentasi Metabase API, dokumentasi Tableau Server Client) jadi satu paket dokumen di `scripts/mbg-cc-pipelines/`, sehingga DAG Airflow penggantinya bisa dibangun tanpa menebak. Fase pipeline menyusul setelah 10 metrik yatim itu punya pemilik.

Akses yang tersedia: Metabase URL + API key, Tableau Server PAT. Tidak ada akses langsung ke Trino/Postgres, jadi ekstraksi harus lewat API BI.

## Target

`/Users/isal/Workspaces/Organizations/BGN/scripts/mbg-cc-pipelines/` (folder sudah ada, kosong; nama jamak, bukan `mbg-cc-pipeline`).

Konvensi mengikuti `scripts/kpm_scraping`: `uv` + `pyproject.toml`, `docs/`, `tools/`. Fase ini belum butuh `src/` karena belum ada kode pipeline.

## Berkas yang dibuat

```
mbg-cc-pipelines/
├── README.md
├── docs/
│   ├── 01-kontrak-data.md
│   ├── 02-peta-sumber-metrik.md
│   ├── 03-ekstraksi-metabase-tableau.md
│   └── 04-rancangan-dag-airflow.md
├── registry/
│   └── peta-metrik.csv
└── tools/
    └── cek_invarian.py
```

Bahasa Indonesia, mengikuti seluruh dokumen di repo `mbg-cc`.

### README.md

Orientasi: apa isi folder ini, status fase 1 vs fase 2, daftar isi, dan ringkasan temuan. Termasuk enam temuan teknis di repo `apps/mbg-cc` yang ditemukan selama kajian (bukan bagian pipeline, tapi harus tercatat di satu tempat sebelum hilang):

1. `server/api/status.get.ts:25,28` membaca `isi?._dokumen?.versi` dan `isi?.provinsi?.baris.length`. Format v2.2 sudah array polos tanpa `_dokumen`, jadi endpoint selalu balik `versi: null, jumlah_provinsi: 0`. Perbaikannya dua baris; `composables/useDashboard.ts:61-64` sudah punya pembaca dua-bentuk (`baris()`) yang bisa ditiru.
2. `scripts/` di-`.gitignore` (baris 12) sehingga `npm run gabung-data` dan `npm run validasi` tidak jalan bagi siapa pun yang clone.
3. Blok `arsip` (9 koleksi, sekitar 30 KB dari 92 KB) tidak dibaca satu komponen pun, tapi tetap dikirim ke browser tiap refresh 60 detik dengan `cache-control: no-store`.
4. `components/ChartBatang.vue` (176 baris) tidak pernah di-import.
5. 10 dari 16 export `utils/agg.ts` mati (`groupBy`, `aggregateBy`, `bottomN`, `maxOf`, `weightedPct`, `lastN`, `latest`, `deltaPct`, `bucketWaktu`, `cumulative`), plus `fdelta` di `utils/format.ts` dan `bersihkanCacheDataset()` di `server/utils/dataset.ts`.
6. `sumber_pembaruan[]` masih memuat 4 label versi SMO yang kartunya sudah dihapus di v2.

### docs/01-kontrak-data.md

Kontrak `mbg-dashboard.json` sebagai target keluaran pipeline. Isinya:

- Struktur 11 kunci puncak + 9 koleksi `arsip`, dengan 30 field `provinsi[]` disebut lengkap (identifier persis, bukan parafrase).
- 14 invarian dari sheet `Invarian` beserta hasil uji terhadap file yang sekarang tayang. Semuanya lolos: Σ SPPG 27.485, Σ PM terpadankan 31.770.000, Σ KPM terpadankan 311.887, 566.722 + 19.957 = 586.679, baris tren terakhir cocok dengan Σ provinsi dan `meta.per_tanggal`, pipeline nasional monoton 4.329 ≥ 3.709 ≥ 3.465 ≥ 2.798 ≥ 2.076 ≥ 1.095, arsip 28.062 dan 28.605 sesuai.
- Enam invarian yang tidak tertulis di kamus tapi terbukti benar di 38 provinsi: monoton per provinsi, `pm_terpadankan_* ≤ pm_target_*`, `kpm_terpadankan_sppg ≤ kpm_total_institusi`, `ops_sppg_operasional ≤ ops_sppg_pop_terdaftar`, `ops_porsi_aktual ≤ sppg_kapasitas_porsi_harian`, `Σ ops_tahap_persiapan == Σ ops_sppg_operasional`. Usulkan naikkan jadi aturan validator karena gratis.
- Aturan relasi yang gampang dilanggar generator: `kode_peta` cuma punya 34 poligon di `public/geo/indonesia-provinces.json` (Papua 92→91, 95/96/97→94, nilainya dijumlahkan), `tahapan_operasional[].kunci` join lewat nama field bukan id, `catatan.<kunci>` dipanggil komponen sebagai prop `info` sehingga ganti nama kunci menghapus tooltip tanpa error, dan file data tidak boleh punya field berawalan garis bawah.
- Satu ketidakcocokan semantik yang perlu keputusan pemilik data: Σ `pm_dilayani_hari_ini` = 21.170.339 sementara Σ `ops_porsi_aktual` = 8.124.187, rasio 2,61x. Kalau satu PM dilayani berarti satu porsi, dua angka ini tidak bisa dua-duanya benar untuk tanggal yang sama. Rasio tertinggi di Sumatera Utara (4,45x) dan Jawa Timur (3,82x).
- Catatan bahwa `sppg_operasional_teridentifikasi` per provinsi masih prorata dari `arsip.profil_sppg_smo[].sppg_aktif` (28.062 turun ke 27.485), jadi angka provinsi belum angka asli.
- Turun-naik akhir pekan di `tren_operasional_harian` (Sabtu dan Minggu jatuh ke sekitar 1,2 juta porsi dari 7,8 juta) sudah diverifikasi wajar, bukan anomali data. Ditulis eksplisit supaya tidak ada yang memasang alert palsu di situ.

### docs/02-peta-sumber-metrik.md

Inti paket ini. Menerjemahkan xlsx jadi peta yang bisa dieksekusi.

- Komposisi: 74 metrik total, 51 aktif (35 dasar, 16 turunan), 23 arsip. Per domain: Penerima Manfaat 18, Institusi KPM 7, Profil SPPG 4, Operasional SPPG 21, Lintas Domain 1.
- Tabel per metrik: ID, domain, jenis, satuan, agregasi, rumus, tempat tampil di dashboard, sistem sumber, nama dashboard, section, koneksi, tabel, dan kalkulasi.
- Catatan normalisasi: untuk 25 baris Tableau, kolom `DB` di xlsx berisi kueri Trino lengkap (CTE `step_ref` dengan enam `step_id`), bukan nama database. Itu wajar karena koneksi Tableau-nya custom SQL, tapi di registry harus dipecah jadi `sumber_tipe`, `koneksi`, `kueri`.
- Register gap: 10 metrik aktif tanpa sumber sama sekali. Enam dasar (`pm_dilayani_hari_ini`, `pm_target_peserta_didik`, `pm_target_ptk_gtk`, `sppg_kapasitas_porsi_harian`, `ops_porsi_kumulatif`, `ops_work_order`, `tren_operasional_harian[].porsi_didistribusikan`) dan empat turunan yang bergantung pada mereka. Untuk tiap satu: apa dampaknya kalau kosong, dan siapa yang perlu ditanya. Sheet `Definisi dan Disclaimer Metriks` menyebut dua PIC, Zidan untuk domain PM dan Institusi KPM, Gandes untuk SPPG.
- Lima dashboard sumber dan berapa metrik yang bergantung padanya, supaya jelas mana yang paling mahal kalau tumbang.

### docs/03-ekstraksi-metabase-tableau.md

Cara menarik data dari kedua sistem, ditulis dari spesifikasi resmi bukan dari ingatan.

Metabase (OpenAPI 3.1.0, 541 path, 127 tag, diambil dari `https://www.metabase.com/docs/latest/api.json`):
- Autentikasi `ApiKeyAuth`, header `X-API-Key`. Alternatif `POST /api/session` untuk sesi cookie.
- Alur yang disarankan: `GET /api/dashboard/{id}` sekali untuk memetakan dashcard ke card, lalu `POST /api/card/{card-id}/query/{export-format}` per kartu. Enum format cuma empat: `csv`, `api`, `xlsx`, `json`. Body menerima `parameters`, `format_rows`, `csv_include_bom`, `pivot_results`, dikirim sebagai `application/x-www-form-urlencoded`.
- `POST /api/dataset` untuk kueri ad-hoc (MBQL atau native), dan `POST /api/dataset/{export-format}` untuk unduhannya. Bedanya: `/api/dataset` selalu lewat cache-bypass.
- Bentuk balasan `query-result`: `status` (`completed`/`failed`), `row_count`, `data`, `running_time`, `cached`. Cek `status` sebelum pakai `data`, jangan cuma andalkan HTTP 200.
- Endpoint lain yang berguna: `/api/card/{id}/query_metadata` untuk skema kolom, `/api/database/{id}/metadata` untuk katalog, `/api/api-key` untuk rotasi kunci.

Tableau (`tableau.github.io/server-client-python`):
- `TSC.PersonalAccessTokenAuth(nama_token, nilai_token, site_id)` lalu `TSC.Server(url, use_server_version=True)`, dipakai sebagai context manager `with server.auth.sign_in(auth):` supaya sign-out otomatis.
- `views.get(req_options)` atau `views.filter(name=...)`, lalu `views.populate_csv(view, CSVRequestOptions(maxage=...))` dan baca `b''.join(view.csv)`. Filter view pakai prefiks `vf_`, contoh `vf_Provinsi='Aceh'`.
- `RequestOptions` untuk paginasi (`page_size`, default 100), `Filter(Field, Operator, value)`, `Sort(Field, Direction)`. Field yang tersedia: `CreatedAt`, `LastLogin`, `Name`, `OwnerName`, `SiteRole`, `Tags`, `UpdatedAt`. Operator: `Equals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`, `In`, `Has`.
- Peringatan yang harus masuk dokumen: `populate_csv` mengembalikan hasil agregasi viz, bukan baris mentah. Kalau view Kinops tidak menampilkan rincian per provinsi, angkanya tidak akan pecah per provinsi. Perlu dicek per view sebelum DAG dibangun, dan kalau ternyata tidak pecah, opsinya minta view khusus atau pakai Metadata API / unduh datasource.
- Sesi Tableau kedaluwarsa sekitar 2 jam, jadi task panjang harus sign-in ulang, bukan menahan satu sesi.
- URL wajib HTTPS, kalau HTTP akan kena redirect dan muncul `405 Method Not Allowed`.

### docs/04-rancangan-dag-airflow.md

Rancangan, belum implementasi. Airflow 3.1.7, TaskFlow API.

- DAG `mbg_cc_dashboard_json`, jadwal harian mengikuti irama `meta.per_tanggal`.
- Graf task: `ekstrak_metabase` dan `ekstrak_tableau` paralel, lalu `normalisasi_provinsi` (padankan ke 38 kode BPS, isi nol untuk provinsi yang tidak muncul di sumber), `rakit_json`, `validasi_invarian`, `terbitkan`.
- Connection: `metabase_sipgn` (tipe HTTP, `X-API-Key` di extra) dan `tableau_sipgn` (PAT di login/password, site di extra). Tidak ada kredensial di kode.
- `validasi_invarian` jadi gerbang. Kalau ada invarian bocor, DAG gagal dan file lama tetap tayang, karena `NUXT_DATA_SOURCE=auto` di `apps/mbg-cc` sudah jatuh ke `./data` waktu URL bermasalah. Ini perilaku yang diinginkan, bukan kecelakaan.
- 10 metrik tanpa sumber: bawa maju dari file hari sebelumnya dan catat di log task, jangan diam-diam diisi nol. Nol akan lolos invarian tapi merusak KPI di layar.
- Terbitkan sebagai `mbg-dashboard-YYYY-MM-DD.json` plus salinan `mbg-dashboard.json` di `DATA_BASE_URL`, supaya rollback tinggal timpa salinannya.
- Keputusan yang ditunda ke fase 2: apakah `arsip` tetap dibawa (30% payload mati) atau dipangkas, dan apakah `kamus-data.json` ikut digenerasi seperti janji `gabung-data.py`.

### registry/peta-metrik.csv

Versi ternormalisasi dari sheet `Metrik Aktif`, satu baris per metrik aktif (51 baris). Kolom: `id_metrik`, `nama_metrik`, `domain`, `jenis`, `level`, `satuan`, `agregasi`, `rumus`, `objek_sumber`, `tampil_di`, `sumber_tipe`, `sumber_dashboard`, `sumber_section`, `koneksi`, `skema`, `tabel`, `kalkulasi`, `status_sumber`.

`status_sumber` bernilai `terpetakan` atau `yatim`, sehingga 10 metrik tanpa sumber bisa difilter dengan satu perintah. File ini yang nanti dibaca DAG, bukan xlsx-nya.

### tools/cek_invarian.py

Pemeriksa 14 invarian plus 6 invarian tak tertulis, Python murni tanpa dependensi, terima path JSON sebagai argumen dan keluar dengan kode 1 kalau ada yang gagal. Ini juga jawaban sementara untuk `validasi-data.mjs` yang hilang, dan nanti dipanggil langsung oleh task `validasi_invarian` di DAG. Logikanya sudah diuji terhadap file yang sekarang tayang; tinggal dirapikan jadi skrip yang bisa dipanggil ulang.

## Sumber yang dibaca (jangan diulang saat eksekusi)

- `apps/mbg-cc/data/mbg-dashboard.json` dan `data/kamus-data.json` (versi 2.2, 21 objek, 13 relasi, 3 invarian formal)
- `apps/mbg-cc/docs/kamus-data.md` (render otomatis dari kamus JSON; ada dua artefak generasi: pipa `|` merusak sel tabel di `sppg_status.kolom.nama` dan `arsip.status_sppg_smo.kolom.nama`, plus spasi nyasar sebelum titik)
- `apps/mbg-cc/README.md`, `server/utils/dataset.ts`, `server/api/*.ts`, `composables/useDashboard.ts`, `utils/{agg,format,palette}.ts`, `pages/index.vue`, `components/*.vue`
- `docs/Mapping Metrics Dashboard Executive.xlsx`, 7 sheet: `Ringkasan`, `Metrik Aktif` (51), `Definisi dan Disclaimer Metriks` (24 baris terisi dari 997), `Metrik Arsip` (23), `Invarian` (14), `Relasi Antar Objek` (13), `Daftar Kolom` (84)
- Spesifikasi OpenAPI Metabase dan dokumentasi TSC, sudah diringkas di atas

## Verifikasi

1. `python3 tools/cek_invarian.py ../../apps/mbg-cc/data/mbg-dashboard.json` harus melaporkan 14 invarian lolos dan keluar dengan kode 0. Jalankan juga dengan file yang sengaja dirusak (ubah satu angka provinsi) untuk memastikan exit code 1 dan pesan gagalnya menunjuk invarian yang benar.
2. `registry/peta-metrik.csv` harus 51 baris data, dan hitungan `status_sumber` harus 41 `terpetakan` + 10 `yatim`. Hitungan per domain harus cocok dengan sheet `Ringkasan`: 18 + 7 + 4 + 21 + 1.
3. Tiap `id_metrik` yang berbentuk `provinsi[].x` harus punya field `x` yang benar-benar ada di 38 baris `provinsi[]`, dan punya entri di `kamus-data.json`. Cek silang ini yang menggantikan sinkronisasi dua arah yang dulu dikerjakan `validasi-data.mjs`.
4. Baca ulang `docs/03` sambil memanggil satu endpoint Metabase yang aman (`GET /api/database` dengan `X-API-Key`) dan satu panggilan TSC (`views.get` dengan `page_size=5`), untuk memastikan bentuk autentikasi yang ditulis memang jalan di instance BGN. Ini yang paling mungkin meleset dari dokumentasi generik.
5. Kirim `docs/02` ke Zidan dan Gandes untuk menutup 10 metrik yatim sebelum fase 2 dimulai.
