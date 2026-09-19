#!/usr/bin/env python3
"""
process_npsn.py
---------------
Script untuk memproses file daftar sekolah input (yang belum ada NPSN-nya)
dan menghasilkan kandidat NPSN dari data referensi berdasarkan lokasi.

Script ini TIDAK melakukan pencocokan nama — itu tugas LLM.
Script ini hanya:
1. Membaca file input baris per baris
2. Untuk tiap baris, mengekstrak info lokasi
3. Memfilter data referensi berdasarkan kecamatan
4. Menyimpan hasil filter per baris ke folder temp
5. Menghasilkan laporan JSON yang bisa dibaca LLM

Penggunaan:
  python process_npsn.py \
    --input daftar_sekolah_input.csv \
    --referensi data_list_sekolah_kita.csv \
    --output hasil_npsn.csv \
    --candidates-dir ./candidates/

  # Dengan kolom mapping kustom:
  python process_npsn.py \
    --input data.xlsx \
    --referensi data_list_sekolah_kita.csv \
    --output hasil.csv \
    --col-nama "Nama Sekolah" \
    --col-provinsi "Provinsi" \
    --col-kabupaten "Kota/Kabupaten" \
    --col-kecamatan "Kecamatan" \
    --col-npsn "NPSN"
"""

import argparse
import csv
import json
import os
import sys
import re
from pathlib import Path
from filter_sekolah import filter_data, normalize


def detect_columns(fieldnames: list[str]) -> dict:
    """
    Auto-detect kolom berdasarkan nama yang umum digunakan.
    Returns mapping: {'nama': col_name, 'provinsi': col_name, ...}
    """
    mapping = {}
    patterns = {
        'nama': [r'nama.*sekolah', r'^nama$', r'school.*name', r'nama_sekolah'],
        'provinsi': [r'provinsi', r'province', r'prov'],
        'kabupaten': [r'kabupaten', r'kota', r'kab', r'city', r'regency'],
        'kecamatan': [r'kecamatan', r'kec', r'district', r'subdistrict'],
        'npsn': [r'^npsn$', r'npsn', r'national.*principal'],
        'bentuk_pendidikan': [r'bentuk.*pendidikan', r'jenjang', r'tingkat', r'level'],
        'status_sekolah': [r'status.*sekolah', r'status', r'negeri.*swasta'],
    }
    
    for field, pats in patterns.items():
        for col in fieldnames:
            col_norm = col.lower().strip().replace(' ', '_')
            for pat in pats:
                if re.search(pat, col_norm):
                    mapping[field] = col
                    break
            if field in mapping:
                break
    
    return mapping


def read_input_file(path: str) -> tuple[list[dict], list[str]]:
    """Baca file input (CSV atau XLSX), return (rows, fieldnames)."""
    ext = Path(path).suffix.lower()
    
    if ext in ('.xlsx', '.xls'):
        try:
            import openpyxl
            wb = openpyxl.load_workbook(path, data_only=True)
            ws = wb.active
            rows = list(ws.iter_rows(values_only=True))
            if not rows:
                return [], []
            headers = [str(h).strip() if h else f'col_{i}' for i, h in enumerate(rows[0])]
            data = []
            for row in rows[1:]:
                if any(v is not None for v in row):  # skip empty rows
                    data.append(dict(zip(headers, [str(v).strip() if v is not None else '' for v in row])))
            return data, headers
        except ImportError:
            print("[ERROR] openpyxl tidak terinstall. Gunakan: pip install openpyxl", file=sys.stderr)
            sys.exit(1)
    else:
        # CSV
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
        for enc in encodings:
            try:
                with open(path, 'r', encoding=enc) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        else:
            print("[ERROR] Tidak bisa membaca file input.", file=sys.stderr)
            sys.exit(1)
        
        first_line = content.split('\n')[0]
        delimiter = ';' if first_line.count(';') > first_line.count(',') else ','
        reader = csv.DictReader(content.splitlines(), delimiter=delimiter)
        rows = list(reader)
        return rows, list(reader.fieldnames or [])


def process_rows(
    input_path: str,
    referensi_path: str,
    output_path: str,
    candidates_dir: str,
    col_nama: str = None,
    col_provinsi: str = None,
    col_kabupaten: str = None,
    col_kecamatan: str = None,
    col_npsn: str = None,
    skip_filled: bool = True,
) -> None:
    """
    Proses semua baris dari file input:
    1. Deteksi kolom
    2. Filter data referensi per baris
    3. Simpan kandidat ke file JSON per baris
    4. Output laporan untuk LLM
    """
    os.makedirs(candidates_dir, exist_ok=True)
    
    rows, fieldnames = read_input_file(input_path)
    if not rows:
        print("[ERROR] File input kosong atau tidak bisa dibaca.", file=sys.stderr)
        sys.exit(1)
    
    print(f"[INFO] {len(rows)} baris ditemukan di file input.", file=sys.stderr)
    
    # Auto-detect kolom jika tidak ditentukan
    auto_map = detect_columns(fieldnames)
    col_nama = col_nama or auto_map.get('nama')
    col_provinsi = col_provinsi or auto_map.get('provinsi')
    col_kabupaten = col_kabupaten or auto_map.get('kabupaten')
    col_kecamatan = col_kecamatan or auto_map.get('kecamatan')
    col_npsn = col_npsn or auto_map.get('npsn')
    
    print(f"[INFO] Mapping kolom yang digunakan:", file=sys.stderr)
    print(f"  nama       -> {col_nama}", file=sys.stderr)
    print(f"  provinsi   -> {col_provinsi}", file=sys.stderr)
    print(f"  kabupaten  -> {col_kabupaten}", file=sys.stderr)
    print(f"  kecamatan  -> {col_kecamatan}", file=sys.stderr)
    print(f"  npsn       -> {col_npsn}", file=sys.stderr)
    
    if not col_nama:
        print("[ERROR] Kolom nama sekolah tidak ditemukan. Gunakan --col-nama.", file=sys.stderr)
        sys.exit(1)
    
    # Tambahkan kolom npsn jika belum ada
    if col_npsn and col_npsn not in fieldnames:
        fieldnames.append(col_npsn)
    elif not col_npsn:
        col_npsn = 'npsn'
        if col_npsn not in fieldnames:
            fieldnames.append(col_npsn)
    
    report = {
        'total_rows': len(rows),
        'processed': 0,
        'skipped_filled': 0,
        'no_location': 0,
        'no_candidates': 0,
        'rows': []
    }
    
    output_rows = []
    
    for i, row in enumerate(rows):
        nama = row.get(col_nama, '').strip() if col_nama else ''
        provinsi = row.get(col_provinsi, '').strip() if col_provinsi else ''
        kabupaten = row.get(col_kabupaten, '').strip() if col_kabupaten else ''
        kecamatan = row.get(col_kecamatan, '').strip() if col_kecamatan else ''
        existing_npsn = row.get(col_npsn, '').strip() if col_npsn else ''
        
        row_report = {
            'row_index': i + 1,
            'nama_sekolah': nama,
            'provinsi': provinsi,
            'kabupaten': kabupaten,
            'kecamatan': kecamatan,
            'existing_npsn': existing_npsn,
            'status': None,
            'candidates_file': None,
            'candidates_count': 0,
        }
        
        # Skip jika NPSN sudah ada
        if skip_filled and existing_npsn and existing_npsn not in ('', '-', 'N/A', 'None', 'nan'):
            row_report['status'] = 'SKIPPED_FILLED'
            report['skipped_filled'] += 1
            output_rows.append(dict(row))
            report['rows'].append(row_report)
            continue
        
        if not nama:
            row_report['status'] = 'SKIPPED_NO_NAME'
            output_rows.append(dict(row))
            report['rows'].append(row_report)
            continue
        
        if not provinsi and not kabupaten and not kecamatan:
            row_report['status'] = 'NO_LOCATION'
            report['no_location'] += 1
            output_rows.append(dict(row))
            report['rows'].append(row_report)
            print(f"[ROW {i+1}] '{nama}' - Tidak ada info lokasi, skip.", file=sys.stderr)
            continue
        
        # Filter data referensi
        print(f"[ROW {i+1}] '{nama}' | {kecamatan}, {kabupaten}, {provinsi}", file=sys.stderr)
        
        candidates = filter_data(
            referensi_path=referensi_path,
            provinsi=provinsi if provinsi else None,
            kabupaten=kabupaten if kabupaten else None,
            kecamatan=kecamatan if kecamatan else None,
            strict=False,
        )
        
        # Jika kecamatan tidak menghasilkan hasil, coba level kabupaten
        if not candidates and kecamatan:
            print(f"[ROW {i+1}] Kecamatan tidak cocok, coba fallback ke kabupaten...", file=sys.stderr)
            candidates = filter_data(
                referensi_path=referensi_path,
                provinsi=provinsi if provinsi else None,
                kabupaten=kabupaten if kabupaten else None,
                strict=False,
            )
            if candidates:
                row_report['fallback_level'] = 'kabupaten'
        
        if not candidates:
            row_report['status'] = 'NO_CANDIDATES'
            report['no_candidates'] += 1
            output_rows.append(dict(row))
            report['rows'].append(row_report)
            print(f"[ROW {i+1}] Tidak ada kandidat ditemukan.", file=sys.stderr)
            continue
        
        # Simpan kandidat ke file JSON
        candidates_file = os.path.join(candidates_dir, f"row_{i+1:04d}_candidates.json")

        # Prioritaskan kolom informatif (termasuk alamat_jalan jika ada di referensi)
        priority_cols = ['nama', 'npsn', 'bentuk_pendidikan', 'status_sekolah',
                         'kecamatan', 'kabupaten', 'provinsi', 'alamat_jalan', 'nama_dusun']
        trimmed_candidates = []
        for c in candidates:
            entry = {}
            for col in priority_cols:
                if col in c:
                    entry[col] = c[col]
            # Sertakan kolom tambahan yang mungkin ada
            for k, v in c.items():
                if k not in entry:
                    entry[k] = v
            trimmed_candidates.append(entry)

        candidate_payload = {
            'row_index': i + 1,
            'target': {
                'nama_sekolah': nama,
                'provinsi': provinsi,
                'kabupaten': kabupaten,
                'kecamatan': kecamatan,
                'other_info': {k: v for k, v in row.items()
                               if k not in [col_nama, col_provinsi, col_kabupaten, col_kecamatan, col_npsn]
                               and v and str(v).strip()}
            },
            'candidates': trimmed_candidates,
            'total_candidates': len(trimmed_candidates),
            'instruction': (
                "Dari daftar \'candidates\' di atas, tentukan sekolah mana yang paling cocok "
                "dengan \'target.nama_sekolah\'. Gunakan HANYA data yang ada dalam \'candidates\'. "
                "Gunakan semua info yang tersedia: nama, bentuk_pendidikan, status_sekolah, "
                "alamat_jalan, nama_dusun untuk memperkuat keputusan. "
                "JANGAN mengarang NPSN — hanya pilih dari daftar kandidat yang diberikan. "
                "Jika tidak yakin, set matched_npsn ke null dan beri alasan jelas. "
                "Respons HANYA dalam format JSON tanpa teks lain: "
                "{\"matched_npsn\": \"...\", \"matched_nama\": \"...\", "
                "\"matched_kecamatan\": \"...\", "
                "\"confidence\": \"HIGH|MEDIUM|LOW\", "
                "\"reason\": \"Penjelasan detail mengapa ini sekolah yang dimaksud\"}"
            )
        }
        
        with open(candidates_file, 'w', encoding='utf-8') as f:
            json.dump(candidate_payload, f, ensure_ascii=False, indent=2)
        
        row_report['status'] = 'READY_FOR_MATCHING'
        row_report['candidates_file'] = candidates_file
        row_report['candidates_count'] = len(candidates)
        report['processed'] += 1
        
        output_rows.append(dict(row))
        report['rows'].append(row_report)
        print(f"[ROW {i+1}] {len(candidates)} kandidat disimpan ke {candidates_file}", file=sys.stderr)
    
    # Simpan report
    report_path = os.path.join(candidates_dir, 'processing_report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # Simpan output (dengan kolom NPSN kosong yang akan diisi LLM nanti)
    if output_path:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(output_rows)
        print(f"[INFO] Output awal disimpan ke: {output_path}", file=sys.stderr)
    
    print(f"\n[SUMMARY]", file=sys.stderr)
    print(f"  Total baris       : {report['total_rows']}", file=sys.stderr)
    print(f"  Siap dicocokkan   : {report['processed']}", file=sys.stderr)
    print(f"  Sudah ada NPSN    : {report['skipped_filled']}", file=sys.stderr)
    print(f"  Tidak ada lokasi  : {report['no_location']}", file=sys.stderr)
    print(f"  Tidak ada kandidat: {report['no_candidates']}", file=sys.stderr)
    print(f"  Report disimpan ke: {report_path}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Proses file daftar sekolah dan siapkan kandidat NPSN dari data referensi'
    )
    parser.add_argument('--input', required=True, help='Path ke file input (CSV atau XLSX)')
    parser.add_argument('--referensi', required=True, help='Path ke data_list_sekolah_kita.csv')
    parser.add_argument('--output', required=True, help='Path untuk file output CSV')
    parser.add_argument('--candidates-dir', default='./candidates', help='Direktori untuk file kandidat (default: ./candidates)')
    parser.add_argument('--col-nama', default=None, help='Nama kolom "nama sekolah" di file input')
    parser.add_argument('--col-provinsi', default=None, help='Nama kolom "provinsi" di file input')
    parser.add_argument('--col-kabupaten', default=None, help='Nama kolom "kabupaten/kota" di file input')
    parser.add_argument('--col-kecamatan', default=None, help='Nama kolom "kecamatan" di file input')
    parser.add_argument('--col-npsn', default=None, help='Nama kolom "npsn" di file input')
    parser.add_argument('--no-skip-filled', action='store_true', help='Proses baris meski sudah ada NPSN')
    
    args = parser.parse_args()
    
    process_rows(
        input_path=args.input,
        referensi_path=args.referensi,
        output_path=args.output,
        candidates_dir=args.candidates_dir,
        col_nama=args.col_nama,
        col_provinsi=args.col_provinsi,
        col_kabupaten=args.col_kabupaten,
        col_kecamatan=args.col_kecamatan,
        col_npsn=args.col_npsn,
        skip_filled=not args.no_skip_filled,
    )


if __name__ == '__main__':
    main()
