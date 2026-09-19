---
name: npsn-finder
description: >
  Temukan dan isi NPSN (Nomor Pokok Sekolah Nasional) secara otomatis dengan mencocokkan
  data sekolah input ke file referensi data_list_sekolah_kita.csv menggunakan teknik LLM
  matching berbasis lokasi (provinsi → kabupaten → kecamatan). Gunakan skill ini SETIAP KALI
  pengguna mengunggah daftar sekolah yang kosong NPSN-nya dan perlu dicocokkan ke database
  referensi, menyebut "cari NPSN", "isi NPSN", "cocokkan NPSN", "data sekolah", "lookup NPSN",
  "data_list_sekolah_kita", atau meminta proses matching/entry data sekolah berbasis lokasi.
  Skill ini menggunakan filter bertingkat untuk membatasi kandidat ke tingkat kecamatan
  sebelum LLM melakukan pencocokan — memastikan zero hallucination dengan hanya mereferensikan
  data dari file yang diberikan.
---

# NPSN Data Finder & Entry

Skill untuk mencocokkan dan mengisi NPSN sekolah secara akurat dengan cara:
1. Menyaring data referensi ke tingkat kecamatan menggunakan script Python
2. Menyerahkan kandidat tersaring ke LLM untuk pencocokan berbasis nama
3. Menulis NPSN hasil pencocokan ke file output

**Prinsip utama: Zero Hallucination** — LLM hanya boleh memilih NPSN dari kandidat yang telah difilter. Tidak ada penebakan di luar data referensi.

---

## Struktur File Skill

```
npsn-finder/
├── SKILL.md                          ← File ini
├── scripts/
│   ├── filter_sekolah.py             ← Filter CSV referensi berdasarkan lokasi
│   ├── process_npsn.py               ← Proses batch semua baris input
│   └── write_npsn.py                 ← Tulis NPSN hasil LLM ke output
└── references/
    └── llm_matching_guide.md         ← Prompt, contoh, dan panduan pencocokan LLM
```

---

## Alur Kerja Lengkap

```
[User upload]                         [Referensi]
File input sekolah          +         data_list_sekolah_kita.csv
(ada kolom NPSN kosong)               (provinsi, kabupaten, kecamatan,
                                       nama, npsn, bentuk_pendidikan, ...)
         │                                           │
         └──────────────┬────────────────────────────┘
                        │
                        ▼
              FASE 1: BACA & SETUP
              • Deteksi kolom otomatis
              • Identifikasi baris yang perlu NPSN
              • Siapkan direktori candidates/
                        │
                        ▼
              FASE 2: FILTER PER BARIS (script)
              Untuk tiap baris:
              • Ekstrak provinsi/kabupaten/kecamatan
              • Jalankan filter_sekolah.py
              • Simpan kandidat ke row_XXXX_candidates.json
                        │
                        ▼
              FASE 3: LLM MATCHING (per baris)
              Untuk tiap file kandidat:
              • Baca file kandidat
              • LLM pilih yang paling cocok
              • Validasi format NPSN (8 digit)
              • Catat hasil + confidence
                        │
                        ▼
              FASE 4: TULIS OUTPUT
              • Isi kolom NPSN di file output
              • Baris tidak ditemukan → tetap kosong + catatan
              • Tampilkan ringkasan hasil
```

---

## Instruksi Langkah demi Langkah

### Langkah 0: Persiapan

Pertama, salin script ke direktori kerja dan install dependensi jika perlu:

```bash
# Salin script ke direktori kerja
cp /mnt/skills/user/npsn-finder/scripts/*.py /home/claude/

# Install dependensi opsional (untuk Excel)
pip install openpyxl --break-system-packages 2>/dev/null || true
```

### Langkah 1: Baca File Input

Gunakan bash/Python untuk membaca file input yang diunggah user. Identifikasi:
- Path file input: biasanya di `/mnt/user-data/uploads/`
- Path file referensi: `data_list_sekolah_kita.csv` (dari upload user)
- Kolom-kolom yang tersedia
- Jumlah baris yang perlu diproses

```bash
# Lihat isi direktori upload
ls /mnt/user-data/uploads/

# Lihat header file input (CSV)
head -3 /mnt/user-data/uploads/[nama_file_input].csv

# Lihat header file referensi
head -2 /mnt/user-data/uploads/data_list_sekolah_kita.csv
```

### Langkah 2: Jalankan Pemrosesan Batch

Gunakan `process_npsn.py` untuk memfilter semua baris dan menyiapkan kandidat:

```bash
python /home/claude/process_npsn.py \
  --input /mnt/user-data/uploads/[nama_file_input].csv \
  --referensi /mnt/user-data/uploads/data_list_sekolah_kita.csv \
  --output /home/claude/output_with_npsn.csv \
  --candidates-dir /home/claude/candidates/
```

Jika nama kolom tidak standar, tambahkan mapping:
```bash
python /home/claude/process_npsn.py \
  --input /mnt/user-data/uploads/[file].csv \
  --referensi /mnt/user-data/uploads/data_list_sekolah_kita.csv \
  --output /home/claude/output_with_npsn.csv \
  --candidates-dir /home/claude/candidates/ \
  --col-nama "Nama Sekolah" \
  --col-provinsi "Provinsi" \
  --col-kabupaten "Kabupaten/Kota" \
  --col-kecamatan "Kecamatan" \
  --col-npsn "NPSN"
```

### Langkah 3: LLM Matching (INTI — Baca panduan di references/llm_matching_guide.md)

**BACA `references/llm_matching_guide.md` sebelum memulai fase ini.**

Untuk setiap file `candidates/row_XXXX_candidates.json`:

```bash
# Lihat daftar file kandidat
ls /home/claude/candidates/row_*_candidates.json | head -20

# Baca satu file kandidat
cat /home/claude/candidates/row_0001_candidates.json
```

Setelah membaca setiap file kandidat, lakukan pencocokan menggunakan panduan di `llm_matching_guide.md`. Simpan semua hasil ke `matches.json`:

```python
# Format matches.json yang harus dibuat
[
  {
    "row_index": 1,
    "matched_npsn": "20234567",
    "matched_nama": "SD NEGERI CIBINONG 1",
    "confidence": "HIGH",
    "reason": "Nama cocok, singkatan SDN = SD NEGERI"
  },
  {
    "row_index": 2,
    "matched_npsn": null,
    "matched_nama": null,
    "confidence": "LOW",
    "reason": "Tidak ada kandidat yang cukup mirip"
  }
]
```

**Cara membuat matches.json dalam Python:**
```python
import json, os

candidates_dir = '/home/claude/candidates/'
matches = []

for fname in sorted(os.listdir(candidates_dir)):
    if not fname.startswith('row_') or not fname.endswith('_candidates.json'):
        continue
    with open(os.path.join(candidates_dir, fname)) as f:
        data = json.load(f)
    
    target = data['target']['nama_sekolah']
    candidates = data['candidates']
    row_index = data['row_index']
    
    # === LAKUKAN PENCOCOKAN DI SINI ===
    # Gunakan logika dari references/llm_matching_guide.md
    # Pilih kandidat yang paling cocok dengan target
    # JANGAN mengarang NPSN — hanya gunakan dari candidates
    
    best = None  # Ganti dengan kandidat terpilih
    
    matches.append({
        "row_index": row_index,
        "matched_npsn":      best['npsn'] if best else None,
        "matched_nama":      best['nama'] if best else None,
        "matched_kecamatan": best['kecamatan'] if best else None,   # BARU
        "confidence": "HIGH",  # atau MEDIUM / LOW
        "reason": "Penjelasan detail: sebutkan bukti spesifik (nama, alamat_jalan, bentuk_pendidikan, dll)"
    })

with open('/home/claude/matches.json', 'w', encoding='utf-8') as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)
```

### Langkah 4: Tulis NPSN ke Output

```bash
python /home/claude/write_npsn.py \
  --output /home/claude/output_with_npsn.csv \
  --matches /home/claude/matches.json \
  --col-npsn "npsn"
```

Script ini **secara otomatis** menambahkan 4 kolom audit trail di paling kanan output (tidak perlu argumen tambahan):
- `npsn_confidence` — HIGH / MEDIUM / LOW / NOT_FOUND
- `npsn_catatan` — penjelasan detail LLM: bukti konkret yang mendasari keputusan
- `ref_nama_sekolah` — nama sekolah persis sesuai `data_list_sekolah_kita.csv`
- `ref_kecamatan` — kecamatan sesuai `data_list_sekolah_kita.csv`

### Langkah 5: Verifikasi dan Presentasikan

```bash
# Cek baris yang berhasil diisi
python3 -c "
import csv
with open('/home/claude/output_with_npsn.csv') as f:
    rows = list(csv.DictReader(f))
filled = sum(1 for r in rows if r.get('npsn','').strip().isdigit())
empty = len(rows) - filled
print(f'Total: {len(rows)} | NPSN terisi: {filled} | Masih kosong: {empty}')
"

# Salin ke output
cp /home/claude/output_with_npsn.csv /mnt/user-data/outputs/output_with_npsn.csv
```

---

## Panduan Anti-Hallucination (WAJIB DIPATUHI)

### ✅ Yang BOLEH dilakukan LLM
- Memilih NPSN dari daftar `candidates` yang sudah difilter
- Menormalisasi nama sekolah (singkatan, huruf besar/kecil, variasi ejaan umum)
- Menyimpulkan kecocokan berdasarkan kesamaan nama + konteks (bentuk_pendidikan, status)
- Mengembalikan `null` jika tidak ada kandidat yang cukup meyakinkan

### ❌ Yang DILARANG KERAS
- Membuat atau menebak NPSN berdasarkan pengetahuan umum
- Menggunakan NPSN dari memori training data
- Memilih NPSN yang tidak ada dalam daftar `candidates`
- Mengisi NPSN jika hanya ada 1 kandidat tapi namanya tidak mirip sama sekali
- Memaksakan pencocokan jika confidence terlalu rendah

### 🚦 Aturan Confidence
| Kondisi | Confidence | Tindakan |
|---------|-----------|----------|
| Nama cocok exact atau singkatan baku | HIGH | Isi NPSN |
| Nama mirip dengan perbedaan kecil | MEDIUM | Isi NPSN + tandai untuk review |
| Nama mirip tapi ada banyak kandidat lain yang sama mirip | LOW | Set null + minta konfirmasi |
| Tidak ada kandidat yang namanya mirip | LOW | Set null |
| Ada kandidat tapi NPSN tidak 8 digit | ERROR | Set null + log error |

---

## Penanganan Error Umum

### File referensi tidak bisa dibaca
```bash
# Cek encoding file
file /mnt/user-data/uploads/data_list_sekolah_kita.csv
python3 -c "
import chardet
with open('/mnt/user-data/uploads/data_list_sekolah_kita.csv','rb') as f:
    print(chardet.detect(f.read(10000)))
"
```

### Kolom tidak terdeteksi otomatis
- Gunakan argumen `--col-nama`, `--col-provinsi`, dst.
- Periksa nama kolom dengan `head -1 [file]`

### 0 kandidat untuk semua baris
- Periksa ejaan nama provinsi/kabupaten di file input vs referensi
- Coba jalankan filter manual:
```bash
python3 /home/claude/filter_sekolah.py \
  --referensi /mnt/user-data/uploads/data_list_sekolah_kita.csv \
  --provinsi "JAWA BARAT" \
  --format table
```

### File input adalah XLSX
- Pastikan `openpyxl` terinstall: `pip install openpyxl --break-system-packages`
- Script `process_npsn.py` sudah mendukung XLSX secara otomatis

---

## Format Output

File output CSV berisi semua kolom dari file input ditambah **4 kolom audit trail wajib di paling kanan**:

| Kolom | Isi |
|-------|-----|
| `npsn` | NPSN 8 digit hasil pencocokan (kosong = tidak ditemukan) |
| `npsn_confidence` | HIGH / MEDIUM / LOW / NOT_FOUND / INVALID_FORMAT |
| `npsn_catatan` | Penjelasan detail LLM: bukti spesifik yang mendasari keputusan (nama, alamat, jenis sekolah) |
| `ref_nama_sekolah` | Nama sekolah persis sesuai `data_list_sekolah_kita.csv` |
| `ref_kecamatan` | Kecamatan sesuai `data_list_sekolah_kita.csv` |

**Kolom referensi (`data_list_sekolah_kita.csv`) yang didukung:**
`provinsi`, `kabupaten`, `kecamatan`, `nama_dusun`, `nama`, `npsn`, `bentuk_pendidikan`, `status_sekolah`, **`alamat_jalan`** *(baru)*

Baris dengan NPSN kosong di output menandakan:
- Tidak ada kandidat yang cukup mirip (perlu verifikasi manual)
- Tidak ada info lokasi yang cukup
- Ambiguous (terlalu banyak kandidat mirip, perlu disambiguasi manual)

---

## Catatan Teknis

- Script `filter_sekolah.py` menggunakan **fuzzy matching berbasis token** — tidak perlu ejaan sempurna
- Fallback otomatis: jika filter kecamatan menghasilkan 0 hasil, coba filter ke kabupaten
- NPSN divalidasi wajib 8 digit angka — format lain otomatis ditolak
- File kandidat disimpan di `candidates/` untuk audit trail dan debugging
- Semua log diagnostik ditulis ke stderr, bukan stdout
