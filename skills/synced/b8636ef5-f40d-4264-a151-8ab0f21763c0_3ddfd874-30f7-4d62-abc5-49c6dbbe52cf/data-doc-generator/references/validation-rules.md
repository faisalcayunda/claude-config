# Reference: Validation Rules for Non-Categorical Fields

Vocabulary (G-01) bukan hanya untuk enum kategorikal. Ia juga jadi **panduan standarisasi data baku** untuk field non-kategorikal. Setiap field non-kategorikal di Vocabulary punya satu atau lebih dari 5 jenis validasi:

1. **Format** — regex/pattern
2. **Range** — batas nilai numeric/date
3. **Panjang** — min/max length string
4. **Referential Integrity** — FK ke tabel lain
5. **Cross-field Business Rule** — relasi antar kolom

## 1. Format Validation

Untuk field yang punya **pattern terstruktur**. Tulis sebagai regex PostgreSQL.

| Pattern Nama Field | Regex | Penjelasan |
|---|---|---|
| `nik` | `^[0-9]{16}$` | NIK 16 digit, sesuai UU Adminduk |
| `npwp` | `^[0-9]{15,16}$` | NPWP 15 (lama) atau 16 (baru NIK-based) digit |
| `no_kk` | `^[0-9]{16}$` | No Kartu Keluarga 16 digit |
| `email` | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | RFC 5322 simplified |
| `no_hp` | `^(\+62\|0)[0-9]{8,12}$` | No HP Indonesia |
| `no_telp` | `^(\+62\|0)[0-9]{6,11}$` | Telp fixed line |
| `kode_pos` | `^[0-9]{5}$` | Kode pos Indonesia 5 digit |
| `kode_wilayah_bps` | `^[0-9]{10}$` | BPS 10 digit (prov+kab+kec+desa) |
| `kode_kab` | `^[0-9]{4}$` | BPS kab/kota 4 digit |
| `kode_prov` | `^[0-9]{2}$` | BPS provinsi 2 digit |
| `kode_negara_iso` | `^[A-Z]{3}$` | ISO 3166-1 alpha-3 |
| `kode_mata_uang` | `^[A-Z]{3}$` | ISO 4217 |
| `iban` | `^[A-Z]{2}[0-9]{2}[A-Z0-9]+$` | IBAN |
| `uuid` | `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` | UUID v4/v7 |
| `plat_nomor` | `^[A-Z]{1,2}\s?[0-9]{1,4}\s?[A-Z]{1,3}$` | Plat nomor kendaraan Indonesia |

**Format di Vocabulary entry:**

```markdown
| **Tipe Validasi** | Format (regex) |
| **Pattern** | `^[0-9]{16}$` |
| **Contoh Valid** | `3171040501010001` |
| **Contoh Invalid** | `12345`, `3171-0405-0101-0001`, `abcd1234efgh5678` |
```

## 2. Range Validation

Untuk field **numeric** atau **date/time** dengan batas valid.

| Pola Field | Range Default | Catatan |
|---|---|---|
| `umur`, `usia` | 0 – 120 | Manusia |
| `jumlah_*`, `nominal_*`, `total_*`, `harga_*` | ≥ 0 | Kalau tidak boleh negatif |
| `persentase_*`, `*_pct`, `*_rate` | 0 – 100 | Atau 0–1 jika decimal |
| `latitude` | -90 – 90 | Geographic |
| `longitude` | -180 – 180 | Geographic |
| `tahun` | 1900 – CURRENT_YEAR | Konteks bisnis |
| `tanggal_lahir` | ≥ 1900-01-01 AND ≤ CURRENT_DATE | Tidak di masa depan |
| `tanggal_transaksi`, `tanggal_*` | ≥ epoch awal data product AND ≤ CURRENT_DATE | Default |
| `berat_kg` | 0 – 500 | Manusia/produk normal |
| `tinggi_cm` | 0 – 250 | Manusia |
| `suhu_celcius` (badan) | 30 – 45 | Suhu tubuh manusia |
| `kalori_per_porsi` | 0 – 5000 | Makanan |

**Format di Vocabulary entry:**

```markdown
| **Tipe Validasi** | Range (numeric) |
| **Min** | 0 |
| **Max** | 120 |
| **Boundary** | Inclusive [0, 120] |
| **Implementasi** | `CHECK (umur >= 0 AND umur <= 120)` |
```

## 3. Length Validation

Untuk field **string bebas** yang punya batas panjang masuk akal.

| Pola Field | Min – Max Length | Catatan |
|---|---|---|
| `nama_lengkap`, `nama_*` | 2 – 255 | Default VARCHAR(255) |
| `alamat` | 5 – 500 | TEXT, biasanya panjang |
| `deskripsi`, `keterangan` | 0 – 1000 | TEXT, optional |
| `catatan` | 0 – 2000 | TEXT panjang |
| `judul_*`, `nama_*_pendek` | 2 – 100 | VARCHAR(100) |
| `username` | 3 – 50 | Alphanumeric |
| `password_hash` | 60 – 60 | bcrypt fixed |
| `slug`, `kode_*` | 3 – 50 | VARCHAR(50) |

**Format di Vocabulary entry:**

```markdown
| **Tipe Validasi** | Length (string) |
| **Min Length** | 2 |
| **Max Length** | 255 |
| **Implementasi** | `CHECK (LENGTH(nama_lengkap) >= 2 AND LENGTH(nama_lengkap) <= 255)` |
```

## 4. Referential Integrity

Untuk field **foreign key** ke tabel lain.

**Format di Vocabulary entry:**

```markdown
| **Tipe Validasi** | Referential Integrity (FK) |
| **Reference Table** | `bgn_gold.dim_sppg` |
| **Reference Column** | `sk_sppg` |
| **Cardinality** | Many-to-One (banyak penyaluran → satu SPPG) |
| **On Delete** | RESTRICT |
| **On Update** | CASCADE |
| **Implementasi** | `FOREIGN KEY (dim_sppg_id) REFERENCES bgn_gold.dim_sppg(sk_sppg)` |
```

**Catatan untuk SCD2**: jika FK ke dimensi SCD Type 2, jelaskan apakah point-in-time atau current-only:

```markdown
| **Resolusi Versi** | Point-in-time (FK menunjuk versi SPPG saat penyaluran terjadi) |
```

## 5. Cross-field Business Rule

Untuk relasi **antar kolom** dalam tabel yang sama atau antar tabel.

**Contoh-contoh cross-field rule umum:**

| Rule | Implementasi |
|---|---|
| `valid_to >= valid_from` (SCD2) | `CHECK (valid_to IS NULL OR valid_to >= valid_from)` |
| `jumlah_paket = paket_per_siswa * jumlah_siswa` | Trigger atau materialized check |
| `total_harga = harga_satuan * kuantitas` | Trigger |
| `tanggal_selesai >= tanggal_mulai` | `CHECK (tanggal_selesai >= tanggal_mulai)` |
| `umur = floor((CURRENT_DATE - tanggal_lahir)/365.25)` | Trigger atau computed column |
| `is_current = TRUE` hanya tepat satu per natural key (SCD2) | Unique partial index `WHERE is_current = TRUE` |
| `nominal_diskon <= nominal_total` | `CHECK (nominal_diskon <= nominal_total)` |
| `tanggal_kadaluwarsa > tanggal_produksi` | `CHECK (tanggal_kadaluwarsa > tanggal_produksi)` |
| `status='terdistribusi' MAKA tanggal_distribusi IS NOT NULL` | `CHECK (status <> 'terdistribusi' OR tanggal_distribusi IS NOT NULL)` |

**Format di Vocabulary entry:**

```markdown
| **Tipe Validasi** | Cross-field Business Rule |
| **Rule** | `umur` harus konsisten dengan `tanggal_lahir`: `umur = FLOOR((CURRENT_DATE - tanggal_lahir) / 365.25)` |
| **Field Terkait** | `tanggal_lahir` |
| **Implementasi** | Computed/generated column atau trigger BEFORE INSERT/UPDATE |
| **Toleransi** | Boleh selisih ±1 hari karena pembulatan tahun |
```

---

## Bagaimana 5 Validasi Ini Muncul di Vocabulary?

Vocabulary entry untuk field non-kategorikal menggunakan **dua lapisan** — Aturan Bisnis (plain language, untuk tim produk) dan Implementasi Teknis (SQL, untuk engineer).

### Cara menyusun "Aturan Bisnis" dari 5 tipe validasi

Setiap tipe validasi perlu diterjemahkan ke kalimat bisnis yang bisa dipahami orang non-teknis:

| Tipe Validasi | Contoh Implementasi Teknis | Terjemahan ke Aturan Bisnis |
|---|---|---|
| Format | `CHECK (nik ~ '^[0-9]{16}$')` | "NIK harus terdiri dari tepat 16 digit angka" |
| Range | `CHECK (umur >= 0 AND umur <= 120)` | "Usia harus antara 0 dan 120 tahun" |
| Length | `CHECK (LENGTH(nama) >= 2)` | "Nama minimal harus 2 karakter" |
| Referential Integrity | `FOREIGN KEY (sppg_id) REFERENCES dim_sppg(sk)` | "Setiap pengiriman harus terhubung ke SPPG yang terdaftar di sistem" |
| Cross-field Rule | `CHECK (tgl_kirim <= tgl_terima)` | "Tanggal pengiriman tidak boleh lebih dari tanggal penerimaan" |

### Contoh lengkap entry: `nik`

```markdown
### `nik`: Nomor Induk Kependudukan

**Document ID:** `VOC-KEPENDUDUKAN-NIK`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `nik` |
| **Nama Bisnis** | Nomor Induk Kependudukan |
| **Deskripsi** | Identifikasi unik penduduk Indonesia sesuai e-KTP |
| **Tipe Data** | `VARCHAR(16)` |
| **Sifat Field** | Non-Kategorikal (Identifier dengan Format) |
| **Klasifikasi** | confidential |
| **Kategori PII** | pii-identitas-khusus |
| **Referensi Regulasi Utama** | UU No. 24 Tahun 2013 (Adminduk) Pasal 58 |
| **Sumber Otoritatif** | SIAK Kemendagri |
| **Digunakan di Tabel** | `kependudukan.dim_warga`, `bgn_gold.dim_penerima_manfaat` |

#### Aturan Bisnis

| ID | Aturan | Field Terkait |
|---|---|---|
| `BVR-001` | NIK harus terdiri dari tepat 16 digit angka | — |
| `BVR-002` | 2 digit pertama NIK harus sesuai dengan kode provinsi yang terdaftar | `dim_wilayah.kode_prov` |

#### Implementasi Teknis

**1. Format (Regex)** — BVR-001

| Atribut | Nilai |
|---|---|
| Pattern | `^[0-9]{16}$` |
| Contoh Valid | `3171040501010001` |
| Contoh Invalid | `12345`, `3171-0405-0101-0001` |

**2. Cross-field Business Rule** — BVR-002

Komposisi semantik NIK terhadap `dim_wilayah`:
- Digit 1-2: kode provinsi (harus exist di `dim_wilayah.kode_prov`)
- Digit 3-4: kode kabupaten/kota (harus exist di `dim_wilayah.kode_kab`)
- Digit 5-6: kode kecamatan (harus exist di `dim_wilayah.kode_kec`)
- Digit 7-12: tanggal lahir DDMMYY (untuk perempuan, DD+40)
- Digit 13-16: nomor urut

```sql
-- BVR-001: NIK harus 16 digit angka
ALTER TABLE kependudukan.dim_warga
    ADD CONSTRAINT chk_nik_format CHECK (nik ~ '^[0-9]{16}$');

-- BVR-002: Kode provinsi pada NIK harus terdaftar
ALTER TABLE kependudukan.dim_warga
    ADD CONSTRAINT chk_nik_provinsi_exist CHECK (
        EXISTS (SELECT 1 FROM bgn_gold.dim_wilayah w
                WHERE w.kode_prov = SUBSTRING(nik, 1, 2))
    );
```
```

## Bagaimana untuk Field yang KATEGORIKAL?

Field kategorikal tetap pakai format **Nilai yang Valid (Enum)** seperti template original. Sifat field di tabel metadata ditandai sebagai `Kategorikal (Enum)`. Pastikan kolom **"Makna untuk Tim Produk"** terisi dengan penjelasan awam untuk setiap nilai enum.

## Bagaimana Field yang Punya MULTIPLE Validasi?

Field bisa punya beberapa validasi sekaligus. Tampilkan semua ID di tabel "Aturan Bisnis", lalu detail teknis di "Implementasi Teknis" masing-masing dengan referensi BVR-nya:

```markdown
#### Aturan Bisnis

| ID | Aturan | Field Terkait |
|---|---|---|
| `BVR-005` | Kode wilayah harus terdiri dari tepat 10 digit angka | — |
| `BVR-006` | Kode wilayah harus sesuai dengan kode wilayah resmi BPS | `dim_wilayah.kode_wilayah` |
| `BVR-007` | 2 digit pertama kode wilayah harus cocok dengan kode provinsi penduduk | `kode_prov_warga` |

#### Implementasi Teknis

**1. Format (Regex)** — BVR-005
- Pattern: `^[0-9]{10}$`

**4. Referential Integrity (FK)** — BVR-006
- FK ke `dim_wilayah.kode_wilayah`

**5. Cross-field Business Rule** — BVR-007
- 2 digit pertama harus match `kode_prov_warga`
```
