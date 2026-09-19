#!/usr/bin/env python3
"""Generate checklist 22+1 dokumen kontrol SIPGN per modul/submodul (markdown).
Pakai: python3 sipgn_doc_checklist.py "Modul 3 - Penerima Manfaat" [--submodul "3.1 Pendaftaran & Pengelolaan Data Penerima"]
"""
import argparse

DOCS_PER_SUBMODUL = [
    "PRD (Product Requirement Document)", "FSD (Functional Specification Document)",
    "TSD (Technical Specification Document)", "Implementation Plan", "ERD",
    "API Specification", "Environment Setup", "UI/UX Design", "Security Risk Analysis",
    "Playbook/User Manual (per role pengguna)", "Release Note", "Version Control Records",
    "Root Cause Analysis", "System Integration Testing (SIT)", "Bug Fix Report",
    "Incident/Bugs Report Log", "Test Plan", "UAT Report", "Performance Test Report",
    "Change Request Document (CRD)",
]
DOCS_PER_MODUL = ["Penetration Test Report", "Security Test Report"]
DOC_PROYEK = "Laporan Final Proyek (PMO/LFP/SIPGN/{bulan-romawi}/{tahun})"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("modul", help='nama modul, mis. "Modul 3 - Penerima Manfaat"')
    p.add_argument("--submodul", default=None, help="nama submodul (opsional)")
    a = p.parse_args()
    scope = f"{a.modul}" + (f" › {a.submodul}" if a.submodul else "")
    print(f"# Checklist Dokumen Kontrol SIPGN — {scope}\n")
    print(f"Format nomor: `{{TYPE}}/{{KODE-SUBMODUL}}/SIPGN/{{BULAN-ROMAWI}}/{{TAHUN}}` | Klasifikasi: Terbatas\n")
    print("## Per submodul (20 jenis)\n")
    for d in DOCS_PER_SUBMODUL:
        print(f"- [ ] {d}")
    print("\n## Per modul (2 jenis)\n")
    for d in DOCS_PER_MODUL:
        print(f"- [ ] {d}")
    print(f"\n## Per proyek\n\n- [ ] {DOC_PROYEK}")
    print("\n> Verifikasi: header dokumen (Nomor, Versi, Tanggal, Klasifikasi) + tabel DOKUMEN KONTROL")
    print("> (Nama | Versi | Tanggal | Log | Oleh | Relasi Dokumen) terisi, dan relasi antar dokumen konsisten.")

if __name__ == "__main__":
    main()
