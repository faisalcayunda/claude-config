# Reference: Aturan Pengisian Metadata

Dokumen ini berisi aturan baku untuk mengisi setiap field metadata di Data Vocabulary (G-01) dan Data Dictionary (G-03). **Setiap nilai harus berasal dari business context yang user berikan. Jika tidak ada, kosongkan atau tanyakan — jangan halusinasi.**

## 1. Klasifikasi Data

Gunakan **TEPAT** salah satu dari 4 level berikut:

| Level | Frontmatter | Emoji (Body) | Kapan Dipakai |
|---|---|---|---|
| Public | `PUBLIC` | 🟢 Public | Data publik, dirilis BPS, KemenkeuRI, bisa diakses bebas. Contoh: kode wilayah BPS, kurs BI |
| Internal | `INTERNAL` | 🔵 Internal | Default untuk data operasional non-sensitif. Hanya internal organisasi. Contoh: ID transaksi, status, timestamp |
| Restricted | `RESTRICTED` | 🟡 Restricted | PII standar — nama, email, alamat, no telp. Memerlukan justifikasi akses |
| Confidential | `CONFIDENTIAL` | 🔴 Confidential | PII sensitif/kategori khusus — NIK, data kesehatan, biometrik, finansial detail. Akses sangat ketat |

**Aturan inferensi:**
- Field PII personal identifier (nama, NIK, email, no HP, alamat) → minimum Restricted
- NIK, biometrik, data kesehatan, data anak → selalu Confidential (UU PDP Pasal 4)
- Timestamp, ID surrogate, status enum → Internal
- Kode publik (BPS, ISO) → Public

## 2. pii_flag

- `true` jika tabel/dokumen mengandung **minimal satu field** ber-klasifikasi Restricted atau Confidential
- `false` jika hanya Public/Internal

## 3. Kategori PII

Berdasarkan UU 27/2022 (UU PDP) Pasal 4:

| Kategori | Penjelasan | Contoh |
|---|---|---|
| `NULL` | Bukan PII | status, kode wilayah, jumlah |
| `pii-umum` | Data pribadi umum | nama, alamat, email, no HP, tanggal lahir |
| `pii-sensitif-kesehatan` | Data kesehatan | diagnosis, riwayat penyakit, BPJS |
| `pii-sensitif-biometrik` | Biometrik | sidik jari, retina, wajah |
| `pii-sensitif-finansial` | Finansial spesifik personal | saldo rekening, no kartu kredit |
| `pii-sensitif-anak` | Data anak (< 17 tahun) | NIK anak, data sekolah anak |
| `pii-sensitif-keagamaan` | Pandangan/identitas religi | agama (jika sensitif konteksnya) |
| `pii-sensitif-politik` | Pandangan politik | afiliasi partai |
| `pii-sensitif-genetik` | Data genetik | hasil tes DNA |
| `pii-identitas-khusus` | Identitas unik nasional | NIK, NPWP |

## 4. Tipe Data PostgreSQL (Standar)

| Tipe | Kapan Dipakai |
|---|---|
| `UUID` | Surrogate key, ID internal |
| `VARCHAR(N)` | String dengan panjang maksimum diketahui — selalu sebutkan N |
| `TEXT` | String panjang variabel (deskripsi, alamat panjang) |
| `BIGINT` | Counter besar, ID auto-increment, nominal Rupiah (penuh) |
| `INTEGER` | Counter standar, < 2 miliar |
| `SMALLINT` | Nilai kecil, kode 0-32767 |
| `NUMERIC(p,s)` | Uang/rasio yang butuh presisi desimal — `NUMERIC(15,2)` untuk Rupiah |
| `BOOLEAN` | Flag true/false |
| `DATE` | Tanggal saja, tanpa waktu |
| `TIMESTAMP` | Tanggal + waktu, tanpa timezone |
| `TIMESTAMPTZ` | Tanggal + waktu + timezone — **DEFAULT untuk semua audit timestamp** |
| `JSONB` | Data semi-terstruktur yang sering di-query |

## 5. SCD Type

| Type | Penjelasan | Kapan Dipakai |
|---|---|---|
| `0` | Tidak pernah berubah | Tanggal lahir, ID generated |
| `1` | Overwrite | Field yang riwayatnya tidak penting (email kontak) |
| `2` | Track history dengan `valid_from`/`valid_to`/`is_current` | Atribut bisnis penting yang riwayatnya dibutuhkan (alamat, harga, status) |
| `3` | Limited history (prev_value column) | Jarang dipakai |

## 6. Field Metadata Standar (selalu ada di tabel Gold)

| Field | Tipe | Tujuan |
|---|---|---|
| `_source_system` | `VARCHAR(50) NOT NULL` | Sistem asal data untuk lineage |
| `_loaded_at` | `TIMESTAMPTZ NOT NULL DEFAULT NOW()` | Kapan pipeline insert record ini |
| `created_at` | `TIMESTAMPTZ NOT NULL` | Kapan record dibuat di sumber |
| `updated_at` | `TIMESTAMPTZ NOT NULL` | Kapan record terakhir diupdate |

## 7. Layer Medallion

| Layer | Penjelasan |
|---|---|
| `Bronze` | Raw ingestion, minim transformasi |
| `Silver` | Cleansed, validated, conformed |
| `Gold` | Business-ready, agregat & dimensional model |
| `API Layer` | Disajikan via REST/GraphQL |

## 8. Aturan Quality Rule (Section 3 di Data Dictionary)

Setiap field punya minimal 1 rule. Pattern umum:

| Pattern Field | Rule Wajib |
|---|---|
| Primary Key | `unique`, `not_null`, threshold 100% |
| Foreign Key | `relationships`, `not_null`, threshold 100% |
| Enum field | `accepted_values` (refer ke G-01) |
| Tanggal | `not in future`, `range valid` |
| Nilai nominal | `>= 0` jika tidak boleh negatif |
| Format string (NIK, kode wilayah) | `regex match` |
| Timestamp audit | `monotonically increasing` per entity |

Tool kolom: `dbt`, `Great Expectations`, `Soda Core`, atau `custom test`.

## 9. Konvensi Penamaan

| Objek | Convention | Contoh |
|---|---|---|
| Schema | lowercase, snake_case | `bgn_gold`, `kependudukan` |
| Tabel fakta | `fct_<entity>` | `fct_penyaluran_mbg` |
| Tabel dimensi | `dim_<entity>` | `dim_sppg`, `dim_sekolah` |
| Staging | `stg_<source>` | `stg_dapodik_sekolah` |
| View | `v_<purpose>` | `v_penyaluran_harian` |
| Surrogate key | `sk_<entity>` atau `<entity>_id` | `sk_sppg`, `sppg_id` |
| Natural key | `nk_<entity>` atau kode bisnis asli | `nk_sppg`, `kode_sppg` |
| Foreign key | `<dim>_id` atau `dim_<entity>_id` | `dim_sppg_id` |
| Constraint | `chk_<field>`, `pk_<table>`, `fk_<table>_<ref>` | `chk_status`, `pk_fct_penyaluran` |

## 10. doc_id Pattern

- Data Vocabulary: `{PROJECT_CODE}-{PRODUCT_SLUG}-G-01` atau hanya `G-01` jika tidak ada project code
- Data Dictionary: `{PROJECT_CODE}-{PRODUCT_SLUG}-G-03` atau hanya `G-03`
- Vocabulary entry per atribut: `VOC-{DOMAIN_UPPER}-{FIELD_UPPER}`

Jika user tidak memberikan project code, gunakan format pendek `G-01` / `G-03`.

## 11. Aturan Khusus dari User

- **Author dan Owner**: SELALU dikosongkan (`''`), jangan diisi nama apapun
- **Profil Domain (Vocabulary)**: Optional — kalau info tidak ada, hilangkan seluruh seksi
- **Header Identifikasi (Data Dictionary)**: Optional — kalau info tidak ada, hilangkan seluruh seksi
- **Referensi Regulasi (Vocabulary)**: Optional — kalau tidak ada regulasi spesifik, hilangkan seluruh seksi
- **Section 3 Enum Values di Data Dictionary**: SELALU DILEWATKAN (informasi enum sudah ada di Vocabulary, jadi di Data Dictionary section 3 langsung "Aturan Kualitas per Field")
