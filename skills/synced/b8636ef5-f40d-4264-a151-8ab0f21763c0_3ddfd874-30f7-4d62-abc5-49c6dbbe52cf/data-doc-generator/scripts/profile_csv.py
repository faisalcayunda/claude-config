#!/usr/bin/env python3
"""
profile_csv.py - Profile CSV file with memory-efficient chunked reading.

Usage:
    python profile_csv.py <csv_path> [--max-distinct N] [--chunksize N] [--output PATH]

Output: JSON with per-column statistics for categorical detection and validation rules.

Statistics per column:
- total_count, null_count, distinct_count
- distinct_values (if <= max_distinct), frequency of each
- For numeric: min, max, mean, std
- For string: min_len, max_len, avg_len, sample regex hint
- is_categorical_candidate flag (preliminary; needs LLM reasoning to confirm)
- inferred_type: 'numeric_int', 'numeric_float', 'string', 'date', 'boolean'
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import pandas as pd


def infer_type(series: pd.Series) -> str:
    """Best-effort type inference from a sample."""
    non_null = series.dropna()
    if len(non_null) == 0:
        return 'unknown'
    if pd.api.types.is_bool_dtype(non_null):
        return 'boolean'
    if pd.api.types.is_integer_dtype(non_null):
        return 'numeric_int'
    if pd.api.types.is_float_dtype(non_null):
        return 'numeric_float'
    if pd.api.types.is_datetime64_any_dtype(non_null):
        return 'date'
    # Try parsing as date
    try:
        pd.to_datetime(non_null.head(20), errors='raise')
        return 'date'
    except Exception:
        pass
    return 'string'


def detect_format_hint(samples: list) -> str | None:
    """Try to detect format pattern from sample values."""
    if not samples:
        return None
    samples_str = [str(s) for s in samples if s is not None]
    if not samples_str:
        return None

    # All same length numeric (NIK, kode pos, etc)
    lengths = {len(s) for s in samples_str}
    if len(lengths) == 1:
        L = lengths.pop()
        if all(s.isdigit() for s in samples_str):
            return f'^[0-9]{{{L}}}$'
        if all(s.isalpha() and s.isupper() for s in samples_str):
            return f'^[A-Z]{{{L}}}$'

    # Email-like
    if all('@' in s and '.' in s for s in samples_str[:5]):
        return 'email-like'

    # UUID-like
    if all(re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-', s, re.I) for s in samples_str[:5]):
        return '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'

    return None


def profile_csv(csv_path: str, max_distinct: int = 50, chunksize: int = 50_000) -> dict:
    """Profile a CSV file using chunked reading."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    # First pass: get column names + a sample for type inference
    df_sample = pd.read_csv(csv_path, nrows=1000, low_memory=False)
    columns = df_sample.columns.tolist()

    # Initialize accumulators
    stats = {}
    for col in columns:
        stats[col] = {
            'name': col,
            'inferred_type': infer_type(df_sample[col]),
            'total_count': 0,
            'null_count': 0,
            'distinct_values_set': set(),  # collect up to max_distinct + 1
            'distinct_overflow': False,
            'value_frequency': Counter(),
            'min_val': None,
            'max_val': None,
            'sum_val': 0.0,
            'min_len': None,
            'max_len': None,
            'sum_len': 0,
            'non_null_count': 0,
        }

    # Full scan with chunks
    chunk_iter = pd.read_csv(csv_path, chunksize=chunksize, low_memory=False)
    chunk_num = 0
    for chunk in chunk_iter:
        chunk_num += 1
        for col in columns:
            if col not in chunk.columns:
                continue
            s = stats[col]
            series = chunk[col]
            s['total_count'] += len(series)
            null_count = int(series.isna().sum())
            s['null_count'] += null_count

            non_null = series.dropna()
            non_null_count = len(non_null)
            s['non_null_count'] += non_null_count
            if non_null_count == 0:
                continue

            # Distinct collection (cap at max_distinct + 1)
            if not s['distinct_overflow']:
                as_str = non_null.astype(str)
                unique_in_chunk = as_str.unique()
                for v in unique_in_chunk:
                    if len(s['distinct_values_set']) <= max_distinct:
                        s['distinct_values_set'].add(v)
                    else:
                        s['distinct_overflow'] = True
                        break
                # Also keep frequency counter (only if not overflowed)
                if not s['distinct_overflow']:
                    s['value_frequency'].update(as_str.tolist())

            # Numeric stats
            if s['inferred_type'] in ('numeric_int', 'numeric_float'):
                try:
                    nv = pd.to_numeric(non_null, errors='coerce').dropna()
                    if len(nv) > 0:
                        cmin, cmax = float(nv.min()), float(nv.max())
                        s['min_val'] = cmin if s['min_val'] is None else min(s['min_val'], cmin)
                        s['max_val'] = cmax if s['max_val'] is None else max(s['max_val'], cmax)
                        s['sum_val'] += float(nv.sum())
                except Exception:
                    pass

            # String length stats
            if s['inferred_type'] == 'string':
                lengths = non_null.astype(str).str.len()
                lmin, lmax = int(lengths.min()), int(lengths.max())
                s['min_len'] = lmin if s['min_len'] is None else min(s['min_len'], lmin)
                s['max_len'] = lmax if s['max_len'] is None else max(s['max_len'], lmax)
                s['sum_len'] += int(lengths.sum())

    # Finalize per column
    result = {
        'file': str(csv_path),
        'columns': {},
        'total_rows': sum(stats[c]['total_count'] for c in columns) // max(1, len(columns)) if columns else 0,
        'chunks_processed': chunk_num,
    }
    # Use total_count from first column (all should be same since CSV has fixed rows)
    if columns:
        result['total_rows'] = stats[columns[0]]['total_count']

    for col in columns:
        s = stats[col]
        distinct_count = len(s['distinct_values_set'])
        if s['distinct_overflow']:
            distinct_count_display = f'>{max_distinct}'
            distinct_values_display = None
        else:
            distinct_count_display = distinct_count
            # Sort values; if numeric, sort numerically
            values_list = list(s['distinct_values_set'])
            try:
                values_list = sorted(values_list, key=lambda x: float(x))
            except (ValueError, TypeError):
                values_list = sorted(values_list)
            distinct_values_display = values_list

        # Top frequencies (most common values)
        top_freq = s['value_frequency'].most_common(min(20, max_distinct))

        # Compute avg
        avg_val = None
        if s['non_null_count'] > 0 and s['inferred_type'] in ('numeric_int', 'numeric_float'):
            avg_val = s['sum_val'] / s['non_null_count']
        avg_len = None
        if s['non_null_count'] > 0 and s['inferred_type'] == 'string':
            avg_len = s['sum_len'] / s['non_null_count']

        # Preliminary categorical flag (LLM will refine)
        is_cat_candidate = (
            not s['distinct_overflow']
            and 2 <= distinct_count <= max_distinct
            and s['inferred_type'] != 'numeric_float'
            and s['inferred_type'] != 'date'
        )

        # Format hint from samples
        format_hint = None
        if distinct_values_display:
            format_hint = detect_format_hint(distinct_values_display[:10])

        result['columns'][col] = {
            'name': col,
            'inferred_type': s['inferred_type'],
            'total_count': s['total_count'],
            'null_count': s['null_count'],
            'null_pct': round(100 * s['null_count'] / max(1, s['total_count']), 2),
            'non_null_count': s['non_null_count'],
            'distinct_count': distinct_count_display,
            'distinct_values': distinct_values_display,
            'top_values': [{'value': v, 'freq': f} for v, f in top_freq],
            'min_val': s['min_val'],
            'max_val': s['max_val'],
            'avg_val': avg_val,
            'min_len': s['min_len'],
            'max_len': s['max_len'],
            'avg_len': avg_len,
            'is_categorical_candidate': is_cat_candidate,
            'format_hint': format_hint,
        }

    return result


def main():
    parser = argparse.ArgumentParser(description='Profile CSV file for data documentation.')
    parser.add_argument('csv_path', help='Path to CSV file')
    parser.add_argument('--max-distinct', type=int, default=50,
                        help='Threshold for categorical candidate (default: 50)')
    parser.add_argument('--chunksize', type=int, default=50_000,
                        help='Pandas chunk size (default: 50000)')
    parser.add_argument('--output', '-o', help='Output JSON path (default: stdout)')
    args = parser.parse_args()

    result = profile_csv(args.csv_path, max_distinct=args.max_distinct, chunksize=args.chunksize)
    json_str = json.dumps(result, indent=2, default=str, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(json_str, encoding='utf-8')
        print(f"Profile saved to: {args.output}", file=sys.stderr)
        print(f"Total rows scanned: {result['total_rows']}", file=sys.stderr)
        print(f"Columns profiled: {len(result['columns'])}", file=sys.stderr)
        cat_count = sum(1 for c in result['columns'].values() if c['is_categorical_candidate'])
        print(f"Categorical candidates: {cat_count}", file=sys.stderr)
    else:
        print(json_str)


if __name__ == '__main__':
    main()
