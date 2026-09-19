# Layer 2 Template — Untuk Stakeholder Awam

Insight bisnis untuk Direktur, Manager non-teknis, Regulator, Auditor. **TANPA istilah teknis**. Pakai analogi sehari-hari, konsekuensi bisnis konkret, dan pertanyaan strategis untuk pimpinan.

## Kerangka Wajib

```
### [Gap ID — Judul Singkat Bahasa Awam]

**Tingkat Keseriusan**: [🟢 Aman / 🟡 Perlu Diperhatikan / 🔴 Mendesak]

**Apa Yang Kami Temukan**
<1-2 kalimat, bahasa biasa. Ceritakan SELISIH yang teramati, BUKAN cara
mengukurnya. Pakai angka bulat atau pembulatan friendly (mis. "sekitar 150
ribu" bukan "144.436").>

**Analogi Singkat**
<1-2 kalimat analogi sehari-hari. Pilih analogi yang relevan untuk konteks
organisasi pembaca — daftar absen siswa, daftar tagihan, daftar inventory
toko, dll.>

**Konsekuensi untuk Bisnis**
<Narasi konkret: siapa terdampak, apa yang berisiko salah, berapa besar
potensi kerugian/risiko reputasi/sanksi regulator. WAJIB pakai unit yang
relevan pembaca (Rp, hari, jumlah pelanggan, jumlah laporan).>

**Pertanyaan untuk Pimpinan**
<2-3 pertanyaan strategis yang HARUS dijawab oleh pengambil keputusan.
BUKAN to-do teknis. Format: pertanyaan terbuka yang memaksa keputusan.>
```

## Daftar Istilah Teknis yang DILARANG di Layer 2

| Jangan tulis | Pakai gantinya |
|---|---|
| schema, skema | "struktur data" atau jelaskan saja perubahannya |
| constraint, batasan kolom | "aturan validasi" atau "aturan isi data" |
| NULL ratio | "persentase data yang kosong" |
| cardinality | "jumlah nilai berbeda" atau "variasi data" |
| Kolmogorov-Smirnov | "tes statistik" atau "pengujian pola" |
| KS p-value | "tingkat keyakinan statistik" (boleh sebut, asal jelaskan) |
| Jaccard similarity | "tingkat kemiripan daftar" |
| primary key, PK | "kode unik identifikasi" |
| foreign key, FK | "kode penghubung antar tabel" |
| index, indeks | "alat pencarian cepat" atau jangan disebut |
| ETL, pipeline | "proses pemindahan data" |
| query, SQL | "permintaan data" atau "cek data" |
| DDL, ALTER TABLE | "perubahan struktur" |
| referential integrity | "konsistensi rujukan antar data" |
| stddev, kurtosis, skewness | "sebaran data" atau "variasi nilai" |

Jika TERPAKSA pakai istilah teknis (mis. karena pembaca regulator yang familiar), WAJIB jelaskan sekali di tanda kurung. Contoh: *"persentase data kosong (yang teknisnya disebut 'NULL ratio')"*.

## Contoh — D1 Volume Gap (Layer 2 dari case yang sama di layer1_template)

### D1-003 — Daftar Pesanan di Sistem Laporan Lebih Sedikit ~150 Ribu Dibanding Sistem Asal

**Tingkat Keseriusan**: 🔴 Mendesak

**Apa Yang Kami Temukan**

Saat membandingkan dua sistem pencatatan pesanan periode Januari–Mei 2026, sistem asal (yang dipakai operasional harian) tercatat sekitar 1,25 juta pesanan, sedangkan sistem laporan (yang dipakai bikin laporan ke pimpinan dan regulator) hanya tercatat sekitar 1,1 juta pesanan. Ada selisih sekitar 150 ribu pesanan yang muncul di sistem asal tapi tidak muncul di sistem laporan.

**Analogi Singkat**

Bayangkan dua daftar transaksi di toko: kasir mencatat semua transaksi termasuk yang dibatalkan, tapi rekapitulasi malam hari hanya menyalin yang berhasil. Selisih 150 ribu pesanan ini adalah pesanan yang dibatalkan atau gagal — mereka memang terjadi (pelanggan sempat klik beli), tapi tidak masuk ke laporan akhir.

**Konsekuensi untuk Bisnis**

Selisih ini berdampak pada tiga hal:

1. **Laporan ke regulator** — jika tim akuntansi menghitung total transaksi dari sistem operasional, sedangkan tim BI mengirim laporan ke regulator dari sistem laporan, dua laporan akan tidak match. Saat audit, ini akan dipertanyakan dan butuh penjelasan formal. Estimasi biaya menjelaskan dan rekonsiliasi: Rp 50–200 juta per cycle audit.
2. **Estimasi performa bisnis** — laporan bulanan ke direksi yang menunjukkan "jumlah pesanan" akan underreport 11–12% setiap bulan. Keputusan kapasitas operasional (jumlah kurir, stok gudang, kapasitas customer service) yang diambil berdasar laporan ini berisiko under-allocated.
3. **Reputasi data** — jika diketahui internal bahwa dua sistem menunjukkan angka berbeda untuk hal yang seharusnya sama, kepercayaan tim ke data turun. Tim akan mulai bikin spreadsheet sendiri untuk re-cek, dan data warehouse jadi "tidak dipercaya" — investasi sistem terbuang.

**Pertanyaan untuk Pimpinan**

1. Untuk laporan bulanan ke regulator, manakah angka yang dipakai — sistem asal atau sistem laporan? Apakah perbedaan 11–12% ini sudah pernah dikomunikasikan ke regulator?
2. Apakah desain awal sistem laporan memang sengaja membuang pesanan yang batal/gagal, atau ini side-effect tidak terdokumentasi yang baru diketahui sekarang?
3. Siapa yang berwenang memutuskan apakah pesanan batal/gagal harus masuk ke sistem laporan? Tim Operasional, Tim Finance, atau Tim Compliance?

## Catatan Operasional

- **Angka friendly** — bulatkan ke ribuan/jutaan/persen 1 desimal. Pembaca awam tidak butuh presisi 6 digit.
- **Konsekuensi WAJIB konkret** — tidak boleh hanya "berisiko salah". WAJIB sebutkan unit konkret (Rp, hari, jumlah pelanggan, jumlah laporan).
- **Pertanyaan untuk Pimpinan** — format pertanyaan terbuka. JANGAN tulis dalam format "to-do" atau "action item". Pimpinan harus merasa terpanggil untuk MEMUTUSKAN, bukan merasa di-assign task.
- **Test kelayakan**: kalau Layer 2 ini dikirim ke seseorang yang baru join organisasi 1 minggu dan tidak pernah baca dokumen teknis, mereka harus bisa paham 80% isinya tanpa googling. Kalau tidak — tulis ulang lebih sederhana.
- **JANGAN ringkasan Layer 1** — Layer 2 berdiri sendiri. Pembaca Layer 2 tidak akan pernah baca Layer 1, dan sebaliknya. Setiap layer harus complete on its own.
