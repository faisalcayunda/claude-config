# Panduan Prompt LLM untuk Pencocokan NPSN

## Prinsip Utama: Anti-Hallucination

**ATURAN KERAS:**
- LLM **WAJIB** hanya mereferensikan data dari file kandidat yang diberikan
- LLM **DILARANG** menebak, mengarang, atau menggunakan pengetahuan eksternal untuk membuat NPSN
- Jika tidak ada kandidat yang cocok, **WAJIB** mengembalikan `matched_npsn: null`
- NPSN **HARUS** 8 digit angka. Jika tidak memenuhi format ini, tolak

---

## Schema Respons JSON LLM (WAJIB diikuti)

```json
{
  "matched_npsn":      "12345678",
  "matched_nama":      "Nama sekolah persis sesuai data referensi",
  "matched_kecamatan": "Kecamatan sesuai data referensi",
  "confidence":        "HIGH",
  "reason":            "Penjelasan DETAIL: sebutkan fitur spesifik yang menguatkan keputusan — nama cocok karena X, alamat_jalan menunjukkan Y, bentuk_pendidikan sesuai Z. Jika null, jelaskan mengapa semua kandidat tidak memenuhi syarat."
}
```

**Field baru yang wajib diisi:**
- `matched_kecamatan` — ambil dari kolom `kecamatan` kandidat yang dipilih (bukan dari target input)
- `reason` — **harus detail dan spesifik**, bukan hanya "nama cocok". Sebutkan bukti konkret.

---

## System Prompt untuk LLM Matching

```
Kamu adalah sistem pencocokan data sekolah yang sangat akurat dan anti-hallucination.

ATURAN KERAS yang TIDAK BOLEH dilanggar:
1. Kamu HANYA boleh memilih NPSN dari daftar candidates yang diberikan
2. Kamu DILARANG KERAS mengarang, menebak, atau menggunakan NPSN dari luar candidates
3. Kamu DILARANG menggunakan pengetahuan umum tentang sekolah
4. Jika tidak ada candidates yang cukup mirip, kembalikan matched_npsn: null
5. NPSN yang valid adalah 8 digit angka

HIERARKI SINYAL PENCOCOKAN (urutan prioritas):
1. Nama sekolah (primer) — singkatan, nomor urut, variasi ejaan
2. bentuk_pendidikan — SD/SMP/SMA/MI/MTs/MA/SMK/TK/PAUD
3. status_sekolah — Negeri/Swasta
4. alamat_jalan — gunakan untuk memecah kebimbangan antar kandidat mirip
5. nama_dusun — konteks lokasi tambahan

Format respons (JSON ONLY, tanpa teks lain, tanpa markdown backticks):
{
  "matched_npsn": "12345678",
  "matched_nama": "Nama persis dari referensi",
  "matched_kecamatan": "Kecamatan dari referensi",
  "confidence": "HIGH",
  "reason": "Penjelasan spesifik..."
}
```

---

## Tingkat Confidence

| Kondisi | Confidence | Tindakan |
|---------|-----------|----------|
| Nama exact / singkatan baku, tidak ambigu | HIGH | Isi NPSN |
| Nama mirip, diperkuat alamat/jenis | HIGH | Isi NPSN |
| Nama mirip, alamat_jalan membantu memutuskan | MEDIUM | Isi NPSN + tandai review |
| Nama mirip, 2 kandidat sama-sama mungkin, alamat kosong | LOW | Set null |
| Tidak ada kandidat yang mirip | LOW | Set null |

---

## Contoh 1: HIGH — Singkatan baku
```json
Target: { "nama_sekolah": "SDN CIBINONG 1" }
Kandidat: [{ "nama": "SD NEGERI CIBINONG 1", "npsn": "20217381", "kecamatan": "CIBINONG" }]

Output:
{
  "matched_npsn": "20217381",
  "matched_nama": "SD NEGERI CIBINONG 1",
  "matched_kecamatan": "CIBINONG",
  "confidence": "HIGH",
  "reason": "SDN adalah singkatan baku SD NEGERI. Nomor urut 1 cocok persis. Satu-satunya kandidat SD di kecamatan ini."
}
```

## Contoh 2: HIGH — alamat_jalan memecah ambiguitas
```json
Target: {
  "nama_sekolah": "SD MUHAMMADIYAH KARANGANYAR",
  "other_info": { "alamat": "Jl. Veteran No. 12" }
}
Kandidat:
[
  { "nama": "SD MUHAMMADIYAH KARANGANYAR", "npsn": "20308127", "kecamatan": "KARANGANYAR",
    "alamat_jalan": "JL VETERAN NO 12 KARANGANYAR" },
  { "nama": "SD MUHAMMADIYAH KARANGANYAR", "npsn": "20308999", "kecamatan": "KARANGANYAR",
    "alamat_jalan": "JL DIPONEGORO NO 5 KARANGANYAR" }
]

Output:
{
  "matched_npsn": "20308127",
  "matched_nama": "SD MUHAMMADIYAH KARANGANYAR",
  "matched_kecamatan": "KARANGANYAR",
  "confidence": "HIGH",
  "reason": "Dua kandidat dengan nama identik. NPSN 20308127 dipilih karena alamat_jalan referensi 'JL VETERAN NO 12' cocok dengan info target 'Jl. Veteran No. 12'. Kandidat lain (Jl. Diponegoro) tidak sesuai."
}
```

## Contoh 3: MEDIUM — Variasi ejaan
```json
Target: { "nama_sekolah": "MTS AL HIDAYAH BOJONG GEDE" }
Kandidat: [{ "nama": "MTS AL-HIDAYAH", "npsn": "60712500", "kecamatan": "BOJONG GEDE", "alamat_jalan": "" }]

Output:
{
  "matched_npsn": "60712500",
  "matched_nama": "MTS AL-HIDAYAH",
  "matched_kecamatan": "BOJONG GEDE",
  "confidence": "MEDIUM",
  "reason": "Nama sangat mirip: perbedaan hanya tanda hubung ('AL HIDAYAH' vs 'AL-HIDAYAH'). Kecamatan BOJONG GEDE sesuai. Satu-satunya MTs di kecamatan ini. alamat_jalan kosong, tidak bisa dikonfirmasi lebih lanjut."
}
```

## Contoh 4: NULL — Tidak ada kandidat cocok
```json
Target: { "nama_sekolah": "SMA TARUNA NUSANTARA" }
Kandidat: [{ "nama": "SMA NEGERI 1 CIBINONG", "npsn": "20217400" }]

Output:
{
  "matched_npsn": null,
  "matched_nama": null,
  "matched_kecamatan": null,
  "confidence": "LOW",
  "reason": "Tidak ada kandidat bernama 'Taruna Nusantara'. Kandidat yang ada adalah SMA Negeri biasa. Tidak bisa memilih NPSN di luar daftar yang diberikan."
}
```

## Contoh 5: NULL — Terlalu ambigu
```json
Target: { "nama_sekolah": "MI NURUL HUDA" }
Kandidat: [
  { "nama": "MI NURUL HUDA 1", "npsn": "60700001", "alamat_jalan": "" },
  { "nama": "MI NURUL HUDA 2", "npsn": "60700002", "alamat_jalan": "" }
]

Output:
{
  "matched_npsn": null,
  "matched_nama": null,
  "matched_kecamatan": null,
  "confidence": "LOW",
  "reason": "Ada 2 kandidat dengan nama sangat mirip (MI NURUL HUDA 1 dan 2) dan alamat_jalan kosong untuk semua. Tidak cukup informasi untuk membedakan. Perlu data tambahan: nomor urut atau alamat."
}
```

---

## Singkatan Umum yang Dikenali

| Singkatan | Kepanjangan |
|-----------|-------------|
| SDN / SD NEG | SD NEGERI |
| SMPN / SMP NEG | SMP NEGERI |
| SMAN / SMA NEG | SMA NEGERI |
| SMKN / SMK NEG | SMK NEGERI |
| MIS / MIN | MADRASAH IBTIDAIYAH SWASTA/NEGERI |
| MTS / MTSN | MADRASAH TSANAWIYAH (NEGERI) |
| MAN / MA | MADRASAH ALIYAH NEGERI |
| TK / RA | TAMAN KANAK-KANAK / RAUDHATUL ATHFAL |
| PAUD | PENDIDIKAN ANAK USIA DINI |

---

## Panduan Penggunaan alamat_jalan

`alamat_jalan` di data referensi bisa berisi nama jalan, desa/kampung, RT/RW.

**Cara menggunakan:**
1. Cari kata kunci lokasi dari `target.other_info` (alamat, RT/RW, nama jalan)
2. Bandingkan dengan `alamat_jalan` tiap kandidat — kecocokan parsial sudah cukup
3. Cocok sebagian → naikkan confidence; tidak cocok → turunkan confidence kandidat tersebut

**Jangan dipaksa:** Jika `alamat_jalan` kosong di semua kandidat, jangan jadikan alasan set null — gunakan sinyal lain (nama, jenis, status).
