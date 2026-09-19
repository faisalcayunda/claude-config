# Reference: Worked Examples

Contoh konkret hasil generate untuk berbagai skenario. Gunakan ini sebagai pola saat user kasih context serupa.

---

## Contoh 1: Vocabulary Entry untuk Field KATEGORIKAL

**Context:** Field `status_penyaluran` di tabel `bgn_gold.fct_penyaluran_mbg`. Hasil profiling: 4 distinct values di full table scan 5.2M baris.

```markdown
### `status_penyaluran`: Status Penyaluran MBG

**Document ID:** `VOC-BGN-STATUS_PENYALURAN`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `status_penyaluran` |
| **Nama Bisnis** | Status Penyaluran MBG |
| **Deskripsi** | Status proses penyaluran paket Makan Bergizi Gratis dari SPPG ke titik distribusi |
| **Tipe Data** | `VARCHAR(20)` |
| **Sifat Field** | Kategorikal (Enum) |
| **Nullable** | Tidak — Setiap event penyaluran wajib memiliki status |
| **Masked (PII)** | Tidak |
| **Klasifikasi** | internal |
| **Kategori PII** | NULL |
| **Referensi Regulasi Utama** | Aturan internal SIPGN |
| **Sumber Otoritatif** | SIPGN — modul Penyaluran |
| **SCD Type** | 1 |
| **Digunakan di Tabel** | `bgn_gold.fct_penyaluran_mbg` |

#### Nilai yang Valid (Enum)

Berdasarkan profiling full table scan (5.234.567 baris):

| Kode | Display Name | Frekuensi | % | Definisi Bisnis | Referensi |
|---|---|---|---|---|---|
| `terdistribusi` | Terdistribusi | 4.512.890 | 86.2% | Paket sudah diterima oleh penerima manfaat | Aturan internal SIPGN |
| `dalam_perjalanan` | Dalam Perjalanan | 412.300 | 7.9% | Paket sedang dikirim dari SPPG ke titik distribusi | Aturan internal SIPGN |
| `terverifikasi` | Terverifikasi | 234.567 | 4.5% | Paket lolos QC organoleptik, siap distribusi | Aturan internal SIPGN |
| `gagal` | Gagal | 74.810 | 1.4% | Penyaluran gagal — paket rusak, penerima tidak hadir | Aturan internal SIPGN |

**Implementasi PostgreSQL:**

```sql
ALTER TABLE bgn_gold.fct_penyaluran_mbg
    ADD CONSTRAINT chk_status_penyaluran
    CHECK (status_penyaluran IN ('terverifikasi', 'dalam_perjalanan', 'terdistribusi', 'gagal'));
```

---

## Contoh 2: Vocabulary Entry untuk Field NON-KATEGORIKAL (Format)

**Context:** Field `nik` di tabel `kependudukan.dim_warga` dan `bgn_gold.dim_penerima_manfaat`. Hasil profiling: 4.8M distinct values (jelas bukan kategorikal). Min/max length = 16. Semua digit.

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
| **Nullable** | Ya — untuk penerima manfaat yang belum punya KTP (anak < 17 thn) |
| **Masked (PII)** | Ya — Display 6 digit pertama saja untuk role non-privileged |
| **Klasifikasi** | confidential |
| **Kategori PII** | pii-identitas-khusus |
| **Referensi Regulasi Utama** | UU No. 24 Tahun 2013 tentang Adminduk Pasal 58 |
| **Sumber Otoritatif** | SIAK Kemendagri |
| **SCD Type** | 0 — NIK tidak pernah berubah seumur hidup |
| **Digunakan di Tabel** | `kependudukan.dim_warga`, `bgn_gold.dim_penerima_manfaat` |

#### Aturan Validasi

Field ini non-kategorikal. Validasi yang diterapkan:

**1. Format (Regex)**

| Atribut | Nilai |
|---|---|
| Pattern | `^[0-9]{16}$` |
| Contoh Valid | `3171040501010001` |
| Contoh Invalid | `12345`, `3171-0405-0101-0001`, `abcd1234efgh5678` |

**2. Panjang (Length)**

| Atribut | Nilai |
|---|---|
| Min Length | 16 |
| Max Length | 16 |

**3. Cross-field Business Rule**

NIK punya komposisi semantik yang harus konsisten dengan atribut lain:

| Posisi Digit | Makna | Harus Match Dengan |
|---|---|---|
| 1-2 | Kode provinsi | `kode_prov` di `dim_wilayah` |
| 3-4 | Kode kabupaten/kota | `kode_kab` di `dim_wilayah` |
| 5-6 | Kode kecamatan | `kode_kec` di `dim_wilayah` |
| 7-12 | DDMMYY tanggal lahir (perempuan: DD+40) | `tanggal_lahir` |
| 13-16 | Nomor urut | (tidak ada cross-field rule) |

**Implementasi PostgreSQL:**

```sql
ALTER TABLE kependudukan.dim_warga
    ADD CONSTRAINT chk_nik_format CHECK (nik ~ '^[0-9]{16}$'),
    ADD CONSTRAINT chk_nik_provinsi CHECK (
        SUBSTRING(nik, 1, 2) IN (SELECT kode_prov FROM bgn_gold.dim_wilayah)
    );

-- Cross-field rule via trigger:
CREATE OR REPLACE FUNCTION validate_nik_birthdate()
RETURNS TRIGGER AS $$
DECLARE
    nik_day INT;
    nik_month INT;
    nik_year INT;
    actual_day INT;
    actual_month INT;
    actual_year INT;
BEGIN
    nik_day := SUBSTRING(NEW.nik, 7, 2)::INT;
    IF nik_day > 40 THEN nik_day := nik_day - 40; END IF;  -- perempuan
    nik_month := SUBSTRING(NEW.nik, 9, 2)::INT;
    nik_year := SUBSTRING(NEW.nik, 11, 2)::INT;

    actual_day := EXTRACT(DAY FROM NEW.tanggal_lahir);
    actual_month := EXTRACT(MONTH FROM NEW.tanggal_lahir);
    actual_year := EXTRACT(YEAR FROM NEW.tanggal_lahir) % 100;

    IF nik_day != actual_day OR nik_month != actual_month OR nik_year != actual_year THEN
        RAISE EXCEPTION 'NIK birthdate digits do not match tanggal_lahir';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

## Contoh 3: Vocabulary Entry untuk Field NON-KATEGORIKAL (Range)

**Context:** Field `jumlah_paket` di tabel `bgn_gold.fct_penyaluran_mbg`. Hasil profiling: numeric int, min=50, max=5000, distinct=23 (tetap continuous — counter).

```markdown
### `jumlah_paket`: Jumlah Paket MBG Disalurkan

**Document ID:** `VOC-BGN-JUMLAH_PAKET`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `jumlah_paket` |
| **Nama Bisnis** | Jumlah Paket MBG Disalurkan |
| **Deskripsi** | Banyaknya paket Makan Bergizi Gratis yang disalurkan dalam satu event penyaluran |
| **Tipe Data** | `INTEGER` |
| **Sifat Field** | Non-Kategorikal (Numeric Measure / Counter) |
| **Nullable** | Tidak |
| **Klasifikasi** | internal |
| **Kategori PII** | NULL |
| **Referensi Regulasi Utama** | Juknis MBG 2026 |
| **Sumber Otoritatif** | SIPGN — modul Penyaluran |
| **Digunakan di Tabel** | `bgn_gold.fct_penyaluran_mbg` |

#### Aturan Validasi

**1. Range**

| Atribut | Nilai |
|---|---|
| Min | 0 |
| Max | 10.000 (batas operasional satu event) |
| Boundary | Inclusive [0, 10000] |

**2. Cross-field Business Rule**

Jumlah paket harus konsisten dengan kapasitas SPPG dan jumlah penerima:

| Rule | Implementasi |
|---|---|
| `jumlah_paket <= dim_sppg.kapasitas_produksi_harian` | Trigger pada INSERT |
| `jumlah_paket = SUM(rincian_paket.kuantitas)` | Trigger / materialized check |

**Implementasi PostgreSQL:**

```sql
ALTER TABLE bgn_gold.fct_penyaluran_mbg
    ADD CONSTRAINT chk_jumlah_paket_range CHECK (jumlah_paket >= 0 AND jumlah_paket <= 10000);
```

---

## Contoh 4: Vocabulary Entry untuk Field NON-KATEGORIKAL (Referential Integrity)

**Context:** Field `dim_sppg_id` di tabel `bgn_gold.fct_penyaluran_mbg`. UUID FK ke dim_sppg (SCD2).

```markdown
### `dim_sppg_id`: Referensi ke Dimensi SPPG (Versi Saat Event)

**Document ID:** `VOC-BGN-DIM_SPPG_ID`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `dim_sppg_id` |
| **Nama Bisnis** | Foreign Key ke SPPG |
| **Deskripsi** | Referensi ke versi SPPG yang berlaku saat event penyaluran terjadi |
| **Tipe Data** | `BIGINT` |
| **Sifat Field** | Non-Kategorikal (Foreign Key) |
| **Nullable** | Tidak |
| **Klasifikasi** | internal |
| **Digunakan di Tabel** | `bgn_gold.fct_penyaluran_mbg` |

#### Aturan Validasi

**1. Referential Integrity**

| Atribut | Nilai |
|---|---|
| Reference Table | `bgn_gold.dim_sppg` |
| Reference Column | `sk_sppg` |
| Cardinality | Many-to-One |
| On Delete | RESTRICT |
| On Update | CASCADE |
| Resolusi Versi | Point-in-time — menunjuk versi SPPG yang aktif saat `tanggal_penyaluran` |

**Implementasi PostgreSQL:**

```sql
ALTER TABLE bgn_gold.fct_penyaluran_mbg
    ADD CONSTRAINT fk_dim_sppg
    FOREIGN KEY (dim_sppg_id) REFERENCES bgn_gold.dim_sppg(sk_sppg)
    ON DELETE RESTRICT ON UPDATE CASCADE;
```

---

## Contoh 5: Data Dictionary Multi-Tabel (struktur Section 1 dan 2)

**Context:** 1 database dengan 4 tabel di schema `bgn_gold`.

```markdown
## 1. Inventori Tabel dan Objek

| Objek | Tipe | Layer | Baris Tipikal | Diperbarui |
|---|---|---|---|---|
| `bgn_gold.fct_penyaluran_mbg` | Table | Gold | `5.234.567` | Harian |
| `bgn_gold.dim_sppg` | Table (SCD2) | Gold | `35.270` | Harian |
| `bgn_gold.dim_wilayah` | Table | Gold | `84.000` | Bulanan |
| `bgn_gold.v_penyaluran_harian` | View | Gold | (derived) | Real-time |

---

## 2. Data Dictionary per Objek

> **Legenda Klasifikasi:**
> - `🟢 Public` — Tidak ada pembatasan
> - `🔵 Internal` — Hanya akses internal organisasi
> - `🟡 Restricted` — Memerlukan justifikasi; PII standar
> - `🔴 Confidential` — Data sangat sensitif; PII kategori khusus

---

### 2.1 `bgn_gold.fct_penyaluran_mbg`

**Deskripsi:** Tabel fakta granular yang mencatat setiap event penyaluran paket MBG.

| # | Nama Field | Tipe Data | Nullable | Klasifikasi | Kunci | Default | Deskripsi Teknis | Makna Bisnis | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `penyaluran_id` | `UUID` | `NOT NULL` | 🔵 Internal | PK | `gen_random_uuid()` | Surrogate key | Identifier event | Generated |
| ... | | | | | | | | | |

### 2.2 `bgn_gold.dim_sppg` (SCD Type 2)

**Deskripsi:** Tabel dimensi SPPG dengan riwayat perubahan.

| # | Nama Field | Tipe Data | Nullable | Klasifikasi | SCD Role | Deskripsi |
|---|---|---|---|---|---|---|
| 1 | `sk_sppg` | `BIGINT` | `NOT NULL` | 🔵 Internal | Surrogate Key | PK auto-increment |
| ... | | | | | | |

### 2.3 `bgn_gold.dim_wilayah`

**Deskripsi:** Master data wilayah administratif berdasarkan kode BPS.

| # | Nama Field | Tipe Data | Nullable | Klasifikasi | Kunci | Default | Deskripsi Teknis | Makna Bisnis | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| ... | | | | | | | | | |

### 2.4 `bgn_gold.v_penyaluran_harian`

**Deskripsi:** View agregasi harian dari fct_penyaluran_mbg.

**Definisi SQL:**

```sql
CREATE VIEW bgn_gold.v_penyaluran_harian AS
SELECT
    tanggal_penyaluran,
    kode_wilayah,
    status_penyaluran,
    COUNT(*) AS jumlah_event,
    SUM(jumlah_paket) AS total_paket
FROM bgn_gold.fct_penyaluran_mbg
GROUP BY 1, 2, 3;
```

| # | Nama Field | Tipe Data | Klasifikasi | Deskripsi | Sumber |
|---|---|---|---|---|---|
| 1 | `tanggal_penyaluran` | `DATE` | 🔵 Internal | Tanggal bisnis | `fct_penyaluran_mbg.tanggal_penyaluran` |
| ... | | | | | |
```

---

## Contoh 6: Field Digunakan di Banyak Tabel

**Context:** Field `kode_wilayah` muncul di tabel `fct_penyaluran_mbg` dan `dim_sppg`.

```markdown
### `kode_wilayah`: Kode Wilayah Administratif BPS

| Metadata | Nilai |
|---|---|
| **Digunakan di Tabel** | `bgn_gold.fct_penyaluran_mbg` (lokasi penyaluran), `bgn_gold.dim_sppg` (lokasi SPPG) |
```

Catat semua tabel di kolom "Digunakan di Tabel" — satu entry Vocabulary bisa cover banyak tabel.

---

## Contoh 7: LLM Reasoning Output ke User

Saat menampilkan summary di Tahap 3 (konfirmasi inferensi), tampilkan reasoning untuk field uncertain:

```
FIELD UNCERTAIN (perlu konfirmasi):

1. `dim_sppg.kapasitas_kategori`
   - Distinct: 5 values [kecil, sedang, besar, sangat_besar, micro]
   - Sample frequency: kecil(15k), sedang(12k), besar(7k), sangat_besar(800), micro(450)
   - Reasoning: Terlihat kategorikal (label diskret), tapi nama field "kategori" ambigu.
   - Question: Apakah ini enum dengan 5 nilai tetap, atau klasifikasi yang bisa berkembang?

2. `dim_sekolah.tingkat_pendidikan`
   - Distinct: 4 values [sd, smp, sma, smk]
   - Reasoning: Jelas kategorikal — tingkat pendidikan dasar/menengah.
   - Question: Konfirmasi nilai valid sudah lengkap? Tidak ada TK / SLB / kejar paket?
```

User akan jawab, lalu lanjutkan dengan list yang sudah disetujui.
