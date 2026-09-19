# Reference: Categorical vs Non-Categorical Detection

Saat profiling data (CSV atau database), tidak semua field dengan distinct count rendah adalah enum kategorikal. Gunakan **LLM reasoning** untuk klasifikasi yang akurat.

## Aturan Klasifikasi

### KATEGORIKAL (masuk Vocabulary sebagai enum)

Field bersifat kategorikal jika **SEMUA kondisi** ini terpenuhi:

1. **Distinct count terbatas dan stabil** — biasanya ≤ 50, tidak akan bertambah seiring data baru masuk
2. **Setiap value punya makna bisnis berbeda** — bukan sekedar nilai dari range continuous
3. **Tipe data string atau integer-encoded** — bukan float continuous
4. **Pengguna akan filter / group by field ini** — bukan untuk operasi aritmatika

**Contoh kategorikal:**
- `status_penyaluran`: 4 distinct → `terverifikasi`, `dalam_perjalanan`, `terdistribusi`, `gagal` ✅
- `jenis_kelamin`: 2 distinct → `L`, `P` ✅
- `tipe_sppg`: 3 distinct → `reguler`, `mitra`, `mandiri` ✅
- `kategori_paket`: 5 distinct → `sd`, `smp`, `sma`, `ibu_hamil`, `balita` ✅
- `kode_provinsi`: 38 distinct → `11`, `12`, ..., `94` ✅ (terbatas, masing-masing punya makna)

### NON-KATEGORIKAL (bukan enum — pakai validasi lain)

Field BUKAN kategorikal meskipun distinct count rendah jika:

1. **Continuous values** — distinct rendah hanya karena dataset kecil; akan berkembang
2. **Numeric identifier** atau **counter** — punya makna individu tapi tidak ada "kategori"
3. **String bebas** — nama, alamat, deskripsi
4. **Date/timestamp** — punya makna temporal, bukan kategori
5. **Code dengan jutaan possibility** — NIK, NPWP, no rekening

**Contoh false positive yang HARUS ditolak:**

| Field | Distinct | Kenapa BUKAN enum |
|---|---|---|
| `umur` di tabel 100 baris | 30 | Continuous numeric — pakai range validation 0–120 |
| `jumlah_paket` | 25 | Counter — pakai range validation ≥ 0 |
| `nik` di tabel sample kecil | 50 | Identifier unik per individu — pakai format `^[0-9]{16}$` |
| `tanggal_lahir` di tabel 50 baris | 50 | Date continuous — pakai DATE format + range |
| `nama_lengkap` di tabel 30 baris | 30 | String bebas — pakai length validation |
| `kode_pos` | 40 | Punya 80.000+ kemungkinan global; sample rendah ≠ enum |
| `id_transaksi` | 20 | Identifier unik — pakai format UUID/sequence |

## LLM Reasoning Checklist

Untuk **setiap** field dengan `distinct_count ≤ 50`, jawab pertanyaan berikut sebelum memutuskan:

1. **Nama field menunjukkan kategori atau identifier?**
   - "status_*", "tipe_*", "kategori_*", "jenis_*", "kelas_*", "tingkat_*", "kode_provinsi/kab/kec" → cenderung KATEGORIKAL
   - "*_id", "no_*", "nik", "npwp", "nama_*", "alamat", "deskripsi", "*_at", "tanggal_*", "umur", "jumlah_*", "nominal_*", "harga", "berat", "tinggi" → cenderung NON-KATEGORIKAL

2. **Jika data bertambah 10x lipat, apakah distinct values akan bertambah signifikan?**
   - Tidak (tetap kira-kira sama) → KATEGORIKAL
   - Ya (akan terus bertambah) → NON-KATEGORIKAL

3. **Apakah values terlihat seperti "label" atau "value"?**
   - Label diskret: `aktif`, `nonaktif`, `pending` → KATEGORIKAL
   - Value continuous: `25`, `26`, `27`, `28`, `30` → NON-KATEGORIKAL (numeric)
   - Pola format: `3171040000`, `3271050000` → bisa KATEGORIKAL (kode wilayah) **atau** NON-KATEGORIKAL (jika ribuan kemungkinan)

4. **Apakah field ini akan jadi axis dari pivot / group by?**
   - Ya → KATEGORIKAL
   - Tidak (lebih dijumlahkan / dirata-ratakan / difilter range) → NON-KATEGORIKAL

## Contoh Reasoning Lengkap

**Field**: `umur` di tabel `dim_penerima_manfaat`
**Distinct count**: 47 (umur 5 sampai 51)
**Sample values**: `5, 6, 7, 8, 10, 11, 12, ..., 51`

**Reasoning**:
1. Nama "umur" = ukuran numerik, BUKAN kategori → non-kategorikal
2. Jika data bertambah, distinct bisa 0-120 (rentang umur manusia) → non-kategorikal
3. Values continuous numeric → non-kategorikal
4. Field umur dipakai untuk filter range (e.g. anak vs dewasa), bukan group enum → non-kategorikal

**Kesimpulan**: NON-KATEGORIKAL. Buat validasi:
- `Range`: 0 ≤ umur ≤ 120
- Cross-field rule (jika ada `tanggal_lahir`): `umur = floor((CURRENT_DATE - tanggal_lahir) / 365)`

---

**Field**: `kode_provinsi` di tabel `dim_wilayah`
**Distinct count**: 38
**Sample values**: `11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 31, 32, 33, ..., 94`

**Reasoning**:
1. Nama "kode_provinsi" = kode, terlihat numerik tapi maknanya label → kategorikal
2. Indonesia hanya punya 38 provinsi, jika data bertambah distinct count tetap 38 → kategorikal
3. Values terlihat numerik tapi masing-masing punya nama provinsi → kategorikal (encoded label)
4. Field dipakai untuk group by / filter per provinsi → kategorikal

**Kesimpulan**: KATEGORIKAL. Masuk Vocabulary dengan referensi BPS sebagai daftar nilai valid.

---

**Field**: `jumlah_paket` di tabel `fct_penyaluran_mbg`
**Distinct count**: 23 (nilai 50, 100, 150, 200, ..., 5000)
**Sample values**: `50, 75, 100, 150, 200, 250, ..., 5000`

**Reasoning**:
1. Nama "jumlah_paket" = counter, ukuran numerik → non-kategorikal
2. Jika data bertambah, distinct akan bertambah (nilai bervariasi) → non-kategorikal
3. Values numeric continuous → non-kategorikal
4. Field di-SUM untuk total paket, bukan grouped → non-kategorikal

**Kesimpulan**: NON-KATEGORIKAL. Buat validasi:
- `Range`: jumlah_paket ≥ 0
- Cross-field rule: `jumlah_paket = SUM(paket_per_siswa * jumlah_siswa)` jika ada relasi

## Aturan Cepat

| Pola Nama Field | Default Klasifikasi |
|---|---|
| `status_*`, `tipe_*`, `jenis_*`, `kategori_*`, `kelas_*`, `tingkat_*` | KATEGORIKAL |
| `*_id`, `id_*`, `*_uuid`, `sk_*`, `nk_*` | NON-KATEGORIKAL (identifier) |
| `nik`, `npwp`, `no_*`, `kode_pos` | NON-KATEGORIKAL (format check) |
| `kode_provinsi`, `kode_kabupaten`, `kode_kecamatan`, `kode_negara` | KATEGORIKAL (lookup BPS/ISO) |
| `nama_*`, `alamat`, `deskripsi`, `keterangan`, `catatan` | NON-KATEGORIKAL (string bebas) |
| `tanggal_*`, `tgl_*`, `waktu_*`, `*_at` | NON-KATEGORIKAL (date/timestamp) |
| `jumlah_*`, `nominal_*`, `harga_*`, `total_*`, `nilai_*` | NON-KATEGORIKAL (numeric measure) |
| `umur`, `usia`, `lama_*`, `durasi_*` | NON-KATEGORIKAL (numeric range) |
| `is_*`, `*_flag`, `aktif` | KATEGORIKAL (boolean / 2 nilai) |
| `flag_*`, `indikator_*` | KATEGORIKAL (biasanya 2-5 nilai) |

**Tetap lakukan reasoning** meskipun ada quick rule — beberapa kasus tidak masuk pola di atas.
