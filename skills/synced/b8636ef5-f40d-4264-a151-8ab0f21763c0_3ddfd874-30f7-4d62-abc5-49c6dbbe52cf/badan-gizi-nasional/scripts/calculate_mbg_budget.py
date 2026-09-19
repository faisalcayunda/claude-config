#!/usr/bin/env python3
"""Proyeksi kebutuhan Bantuan Pemerintah SPPG per komposisi PM — acuan Juknis MBG 2026 (Kepka BGN 401.1/2025 Bab 3.1.6 & 4.7).

Angka acuan:
- Acuan dasar bahan baku: Rp8.000 (balita/PAUD/TK/RA/SD 1-3), Rp10.000 (SD 4-6 s.d. SMA/SMK/SLB, santri, pendidik, tendik, bumil, busui) — at cost, rujukan HET setempat.
- Pagu rata-rata Rp15.000/PM/hari (bahan baku + operasional + insentif); pagu maksimal kelompok balita-SD 1-3: Rp13.000.
- Insentif fasilitas SPPG: Rp6.000.000/hari, 6 hari/minggu, tak tergantung jumlah PM.
Contoh: python3 calculate_mbg_budget.py --kelompok-a 800 --kelompok-b 1500 --hari 6 --minggu 2
"""
import argparse

ACUAN_A = 8_000      # balita/PAUD/TK/RA/SD 1-3
ACUAN_B = 10_000     # SD 4-6, SMP, SMA/SMK/SLB, santri, pendidik, tendik, bumil, busui
PAGU_MAX_A = 13_000  # pagu maksimal kelompok A per hari
PAGU_AVG = 15_000    # rata-rata bantuan per PM per hari (all-in)
INSENTIF = 6_000_000 # per hari operasional

def fmt(n): return f"Rp{n:,.0f}".replace(",", ".")

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--kelompok-a", type=int, default=0, help="PM balita/PAUD/TK/RA/SD kelas 1-3")
    p.add_argument("--kelompok-b", type=int, default=0, help="PM SD 4-6/SMP/SMA/SMK/SLB/santri/pendidik/tendik/bumil/busui")
    p.add_argument("--hari", type=int, default=6, help="hari distribusi per minggu (Juknis: 6; kebijakan Mar 2026: 5 hari sekolah)")
    p.add_argument("--minggu", type=int, default=2, help="jumlah minggu proyeksi (default 2 = periode laporan)")
    a = p.parse_args()
    total_pm = a.kelompok_a + a.kelompok_b
    if total_pm == 0:
        p.error("isi --kelompok-a dan/atau --kelompok-b")
    if total_pm > 3000:
        print("⚠️  >3.000 PM melebihi kapasitas maksimal SPPG (2.500; 3.000 dgn Jurutama BNSP).")
    elif total_pm > 2500:
        print("ℹ️  2.501-3.000 PM hanya boleh bila ada Jurutama Masak bersertifikat BNSP.")
    hari_total = a.hari * a.minggu
    bahan_a = a.kelompok_a * ACUAN_A * hari_total
    bahan_b = a.kelompok_b * ACUAN_B * hari_total
    insentif = INSENTIF * hari_total
    pagu_atas = (a.kelompok_a * PAGU_MAX_A + a.kelompok_b * PAGU_AVG) * hari_total
    print(f"\n=== Proyeksi {a.minggu} minggu × {a.hari} hari = {hari_total} hari distribusi | {total_pm} PM ===")
    print(f"Bahan baku (acuan dasar, at cost):")
    print(f"  Kelompok A ({a.kelompok_a} PM × {fmt(ACUAN_A)}): {fmt(bahan_a)}")
    print(f"  Kelompok B ({a.kelompok_b} PM × {fmt(ACUAN_B)}): {fmt(bahan_b)}")
    print(f"  Subtotal bahan baku: {fmt(bahan_a + bahan_b)}")
    print(f"Insentif fasilitas ({hari_total} hari × {fmt(INSENTIF)}): {fmt(insentif)}")
    print(f"Estimasi total acuan (bahan baku + insentif): {fmt(bahan_a + bahan_b + insentif)}")
    print(f"Batas atas indikatif pagu (Rp13.000/Rp15.000 all-in): {fmt(pagu_atas)}")
    print("\nCatatan: bahan baku & operasional dipertanggungjawabkan AT COST (HET setempat / survei 3 penyedia);")
    print("angka di atas proyeksi acuan, bukan tagihan. Operasional riil belum termasuk (at cost).")

if __name__ == "__main__":
    main()
