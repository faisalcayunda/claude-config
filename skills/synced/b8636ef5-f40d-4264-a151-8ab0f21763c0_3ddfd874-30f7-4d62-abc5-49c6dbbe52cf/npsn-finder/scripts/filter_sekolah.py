#!/usr/bin/env python3
"""
filter_sekolah.py
-----------------
Script untuk memfilter data referensi sekolah (data_list_sekolah_kita.csv)
berdasarkan provinsi, kabupaten/kota, dan kecamatan.

Penggunaan:
  python filter_sekolah.py \
    --referensi data_list_sekolah_kita.csv \
    --provinsi "JAWA BARAT" \
    --kabupaten "KABUPATEN BOGOR" \
    --kecamatan "CIBINONG" \
    --output filtered_kecamatan.csv

  # Bisa juga filter hingga kabupaten saja (jika kecamatan tidak diketahui):
  python filter_sekolah.py \
    --referensi data_list_sekolah_kita.csv \
    --provinsi "JAWA BARAT" \
    --kabupaten "KABUPATEN BOGOR" \
    --output filtered_kabupaten.csv
"""

import argparse
import csv
import sys
import re
import os


def normalize(text: str) -> str:
    """Normalisasi teks: uppercase, strip spasi, hapus karakter non-alfanumerik berlebih."""
    if not text:
        return ""
    text = text.upper().strip()
    # Hapus karakter khusus yang tidak relevan, pertahankan spasi
    text = re.sub(r'[^A-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def fuzzy_match(query: str, candidate: str, threshold: float = 0.6) -> bool:
    """
    Fuzzy match sederhana berbasis token overlap.
    Cocok jika semua token query ada di dalam candidate, atau sebaliknya.
    """
    q_tokens = set(normalize(query).split())
    c_tokens = set(normalize(candidate).split())
    if not q_tokens or not c_tokens:
        return False
    overlap = q_tokens & c_tokens
    # Hitung rasio overlap terhadap token yang lebih pendek
    ratio = len(overlap) / min(len(q_tokens), len(c_tokens))
    return ratio >= threshold


def filter_data(
    referensi_path: str,
    provinsi: str = None,
    kabupaten: str = None,
    kecamatan: str = None,
    output_path: str = None,
    strict: bool = False,
) -> list[dict]:
    """
    Filter data referensi sekolah berdasarkan lokasi.

    Args:
        referensi_path: Path ke file CSV referensi
        provinsi: Nama provinsi (opsional)
        kabupaten: Nama kabupaten/kota (opsional)
        kecamatan: Nama kecamatan (opsional)
        output_path: Path untuk menyimpan hasil filter (opsional)
        strict: Jika True, gunakan exact match; jika False, gunakan fuzzy match

    Returns:
        List of dict berisi baris yang cocok
    """
    if not os.path.exists(referensi_path):
        print(f"[ERROR] File referensi tidak ditemukan: {referensi_path}", file=sys.stderr)
        sys.exit(1)

    results = []
    skipped = 0
    total = 0

    # Coba beberapa encoding umum untuk file CSV Indonesia
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
    
    file_content = None
    used_encoding = None
    for enc in encodings:
        try:
            with open(referensi_path, 'r', encoding=enc) as f:
                file_content = f.read()
            used_encoding = enc
            break
        except UnicodeDecodeError:
            continue
    
    if file_content is None:
        print(f"[ERROR] Tidak bisa membaca file dengan encoding yang tersedia.", file=sys.stderr)
        sys.exit(1)

    # Deteksi delimiter (koma atau titik koma)
    first_line = file_content.split('\n')[0]
    delimiter = ';' if first_line.count(';') > first_line.count(',') else ','

    reader = csv.DictReader(file_content.splitlines(), delimiter=delimiter)
    
    # Validasi kolom yang dibutuhkan
    required_cols = {'provinsi', 'kabupaten', 'kecamatan', 'nama', 'npsn'}
    available_cols = set(c.strip().lower().replace(' ', '_') for c in (reader.fieldnames or []))
    
    # Remap fieldnames jika perlu
    fieldnames_map = {}
    for fn in (reader.fieldnames or []):
        fieldnames_map[fn] = fn.strip().lower().replace(' ', '_')

    for row in reader:
        total += 1
        # Normalisasi key
        norm_row = {fieldnames_map.get(k, k): v for k, v in row.items()}
        
        # Ambil nilai lokasi dari baris
        row_provinsi = norm_row.get('provinsi', '') or ''
        row_kabupaten = norm_row.get('kabupaten', '') or norm_row.get('kota', '') or ''
        row_kecamatan = norm_row.get('kecamatan', '') or ''

        match = True

        # Filter provinsi
        if provinsi:
            if strict:
                if normalize(row_provinsi) != normalize(provinsi):
                    match = False
            else:
                if not fuzzy_match(provinsi, row_provinsi):
                    match = False

        # Filter kabupaten
        if match and kabupaten:
            if strict:
                if normalize(row_kabupaten) != normalize(kabupaten):
                    match = False
            else:
                if not fuzzy_match(kabupaten, row_kabupaten):
                    match = False

        # Filter kecamatan
        if match and kecamatan:
            if strict:
                if normalize(row_kecamatan) != normalize(kecamatan):
                    match = False
            else:
                if not fuzzy_match(kecamatan, row_kecamatan):
                    match = False

        if match:
            results.append(norm_row)
        else:
            skipped += 1

    print(f"[INFO] Encoding: {used_encoding} | Delimiter: '{delimiter}'", file=sys.stderr)
    print(f"[INFO] Total baris referensi: {total}", file=sys.stderr)
    print(f"[INFO] Baris cocok dengan filter: {len(results)}", file=sys.stderr)
    print(f"[INFO] Baris tidak cocok: {skipped}", file=sys.stderr)

    if not results:
        print("[WARNING] Tidak ada data yang cocok dengan filter lokasi yang diberikan.", file=sys.stderr)
        print("[WARNING] Coba periksa ejaan provinsi/kabupaten/kecamatan.", file=sys.stderr)

    # Simpan output jika diminta
    if output_path and results:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
            writer.writeheader()
            writer.writerows(results)
        print(f"[INFO] Hasil filter disimpan ke: {output_path}", file=sys.stderr)

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Filter data referensi sekolah berdasarkan lokasi (provinsi/kabupaten/kecamatan)'
    )
    parser.add_argument('--referensi', required=True, help='Path ke file CSV referensi (data_list_sekolah_kita.csv)')
    parser.add_argument('--provinsi', default=None, help='Nama provinsi untuk filter')
    parser.add_argument('--kabupaten', default=None, help='Nama kabupaten/kota untuk filter')
    parser.add_argument('--kecamatan', default=None, help='Nama kecamatan untuk filter')
    parser.add_argument('--output', default=None, help='Path file output CSV hasil filter')
    parser.add_argument('--strict', action='store_true', help='Gunakan exact match (default: fuzzy match)')
    parser.add_argument('--format', choices=['csv', 'json', 'table'], default='table',
                        help='Format output ke stdout (default: table)')
    args = parser.parse_args()

    results = filter_data(
        referensi_path=args.referensi,
        provinsi=args.provinsi,
        kabupaten=args.kabupaten,
        kecamatan=args.kecamatan,
        output_path=args.output,
        strict=args.strict,
    )

    if not results:
        sys.exit(0)

    # Output ke stdout
    if args.format == 'json':
        import json
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif args.format == 'csv':
        writer = csv.DictWriter(sys.stdout, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    else:  # table
        cols = ['nama', 'npsn', 'bentuk_pendidikan', 'status_sekolah', 'kecamatan', 'kabupaten', 'provinsi']
        available = [c for c in cols if c in results[0]]
        # Lebar kolom
        widths = {c: max(len(c), max(len(str(r.get(c, ''))) for r in results)) for c in available}
        widths = {c: min(w, 50) for c, w in widths.items()}  # cap at 50

        header = ' | '.join(c.upper().ljust(widths[c]) for c in available)
        sep = '-+-'.join('-' * widths[c] for c in available)
        print(header)
        print(sep)
        for row in results:
            line = ' | '.join(str(row.get(c, '')).ljust(widths[c])[:widths[c]] for c in available)
            print(line)

    print(f"\n[TOTAL] {len(results)} sekolah ditemukan.", file=sys.stderr)


if __name__ == '__main__':
    main()
