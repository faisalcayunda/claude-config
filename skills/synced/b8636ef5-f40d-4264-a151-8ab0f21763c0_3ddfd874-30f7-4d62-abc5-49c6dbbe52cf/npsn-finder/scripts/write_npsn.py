#!/usr/bin/env python3
"""
write_npsn.py
-------------
Script untuk menulis hasil pencocokan NPSN dari LLM ke dalam file output.
Dijalankan setelah LLM selesai mencocokkan semua kandidat.

Kolom yang SELALU ditambahkan di paling kanan output (urut):
  1. npsn            — NPSN 8 digit hasil pencocokan (atau kosong)
  2. npsn_confidence — HIGH / MEDIUM / LOW / NOT_FOUND
  3. npsn_catatan    — Alasan/penjelasan LLM mengapa yakin dengan pencocokan ini
  4. ref_nama_sekolah — Nama sekolah persis sesuai data referensi (data_list_sekolah_kita.csv)
  5. ref_kecamatan   — Kecamatan sekolah sesuai data referensi

Penggunaan:
  python write_npsn.py \
    --output hasil_npsn.csv \
    --matches matches.json \
    --col-npsn "NPSN"

Format matches.json:
[
  {
    "row_index": 1,
    "matched_npsn": "20234567",
    "matched_nama": "SD NEGERI 1 CIBINONG",
    "matched_kecamatan": "CIBINONG",
    "confidence": "HIGH",
    "reason": "Nama cocok persis setelah normalisasi, alamat_jalan sesuai"
  },
  {
    "row_index": 2,
    "matched_npsn": null,
    "matched_nama": null,
    "matched_kecamatan": null,
    "confidence": "LOW",
    "reason": "Tidak ditemukan kandidat yang cocok"
  }
]
"""

import argparse
import csv
import json
import sys
import os
from pathlib import Path

# Kolom tambahan yang SELALU ditulis di paling kanan, urut
TRAILING_COLS = [
    ('npsn_confidence', 'npsn_confidence'),
    ('npsn_catatan',    'npsn_catatan'),
    ('ref_nama_sekolah','ref_nama_sekolah'),
    ('ref_kecamatan',   'ref_kecamatan'),
]


def write_npsn_to_output(
    output_path: str,
    matches: list[dict],
    col_npsn: str = 'npsn',
) -> None:
    """
    Update file output CSV dengan NPSN + kolom audit trail hasil pencocokan LLM.

    Kolom yang ditambahkan di paling kanan (selalu):
      npsn_confidence, npsn_catatan, ref_nama_sekolah, ref_kecamatan

    Args:
        output_path: Path ke file output CSV yang akan diupdate
        matches: List hasil pencocokan dari LLM
        col_npsn: Nama kolom NPSN di file output (default: 'npsn')
    """
    match_lookup = {m['row_index']: m for m in matches}

    # Baca file output
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    content = None
    for enc in encodings:
        try:
            with open(output_path, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue

    if content is None:
        print(f"[ERROR] Tidak bisa membaca file output: {output_path}", file=sys.stderr)
        sys.exit(1)

    first_line = content.split('\n')[0]
    delimiter = ';' if first_line.count(';') > first_line.count(',') else ','

    reader = csv.DictReader(content.splitlines(), delimiter=delimiter)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

    # Pastikan kolom NPSN utama ada
    if col_npsn not in fieldnames:
        fieldnames.append(col_npsn)

    # Tambahkan kolom trailing di paling kanan (jika belum ada)
    trailing_names = [c for _, c in TRAILING_COLS]
    for col in trailing_names:
        if col not in fieldnames:
            fieldnames.append(col)

    # Update baris
    updated = 0
    not_found = 0
    already_filled = 0

    for i, row in enumerate(rows):
        row_index = i + 1
        match = match_lookup.get(row_index)

        if match is None:
            continue

        existing_npsn = str(row.get(col_npsn, '')).strip()
        if existing_npsn and existing_npsn not in ('', '-', 'N/A', 'None', 'nan'):
            already_filled += 1
            # Tetap isi kolom audit meski NPSN sudah ada, untuk konsistensi
            row['npsn_confidence']  = match.get('confidence', '')
            row['npsn_catatan']     = match.get('reason', '')
            row['ref_nama_sekolah'] = match.get('matched_nama', '')
            row['ref_kecamatan']    = match.get('matched_kecamatan', '')
            continue

        matched_npsn = match.get('matched_npsn')
        confidence   = match.get('confidence', 'LOW')
        reason       = match.get('reason', '')
        ref_nama     = match.get('matched_nama', '')
        ref_kecamatan= match.get('matched_kecamatan', '')

        # Selalu isi kolom audit trail
        row['npsn_confidence']  = confidence
        row['npsn_catatan']     = reason
        row['ref_nama_sekolah'] = ref_nama
        row['ref_kecamatan']    = ref_kecamatan

        if matched_npsn is None:
            not_found += 1
            row['npsn_confidence'] = 'NOT_FOUND'
            continue

        # Validasi: NPSN harus 8 digit angka
        npsn_str = str(matched_npsn).strip()
        if not npsn_str.isdigit() or len(npsn_str) != 8:
            print(f"[WARNING] Row {row_index}: NPSN '{npsn_str}' tidak valid (bukan 8 digit). Skip.", file=sys.stderr)
            not_found += 1
            row['npsn_confidence'] = 'INVALID_FORMAT'
            row['npsn_catatan']    = f"NPSN '{npsn_str}' bukan 8 digit — tidak ditulis. " + reason
            continue

        row[col_npsn] = npsn_str
        updated += 1
        print(
            f"[ROW {row_index}] ✓ NPSN={npsn_str} | {confidence} | "
            f"ref: {ref_nama} ({ref_kecamatan}) | {reason[:60]}",
            file=sys.stderr
        )

    # Tulis kembali file
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n[SUMMARY WRITE]", file=sys.stderr)
    print(f"  NPSN berhasil ditulis   : {updated}", file=sys.stderr)
    print(f"  Sudah terisi sebelumnya : {already_filled}", file=sys.stderr)
    print(f"  Tidak ditemukan/null    : {not_found}", file=sys.stderr)
    print(f"  Kolom audit trail       : npsn_confidence, npsn_catatan, ref_nama_sekolah, ref_kecamatan", file=sys.stderr)
    print(f"  File diperbarui         : {output_path}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Tulis hasil pencocokan NPSN dari LLM ke file output (+ kolom audit trail)'
    )
    parser.add_argument('--output', required=True, help='Path file output CSV untuk diupdate')
    parser.add_argument('--matches', required=True, help='Path ke file JSON hasil pencocokan LLM')
    parser.add_argument('--col-npsn', default='npsn', help='Nama kolom NPSN di file output (default: npsn)')

    args = parser.parse_args()

    with open(args.matches, 'r', encoding='utf-8') as f:
        matches = json.load(f)

    write_npsn_to_output(
        output_path=args.output,
        matches=matches,
        col_npsn=args.col_npsn,
    )


if __name__ == '__main__':
    main()
