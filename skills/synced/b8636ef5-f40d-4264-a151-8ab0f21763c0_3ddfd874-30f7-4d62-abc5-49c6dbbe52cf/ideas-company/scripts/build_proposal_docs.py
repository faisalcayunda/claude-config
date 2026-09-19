#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IDEAS Proposal Document Builder v3.

Builds PPTX and DOCX directly from structured proposal data.
- PPTX: native bullets, logo embedding, section accents, dynamic tables
- DOCX: proper Word styles, fixed-layout tables, branded cover
"""

import logging
import os
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

_SKILL_DIR = Path(__file__).resolve().parent.parent
_LOGO_LANDSCAPE = _SKILL_DIR / "templates" / "LogoIDEASLandscape.png"
_LOGO_SQUARE = _SKILL_DIR / "templates" / "Logo_ideas.png"

_NAVY = "0A0A5C"; _NAVY_L = "1F4E79"; _ICE = "D6E4F0"; _ACCENT = "E8F0FE"
_WHITE = "FFFFFF"; _DARK = "2D2D2D"; _GRAY = "888888"


def build_pptx(data: Dict[str, Any], output_path: str) -> Optional[str]:
    try:
        from pptx import Presentation
        from pptx.util import Inches, Pt, Emu
        from pptx.dml.color import RGBColor
        from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
        from pptx.enum.shapes import MSO_SHAPE
        from pptx.oxml.ns import qn
        from lxml import etree
    except ImportError as e:
        logger.error("Missing: %s. pip install python-pptx lxml --break-system-packages", e)
        return None

    NAVY = RGBColor.from_string(_NAVY)
    NAVY_L = RGBColor.from_string(_NAVY_L)
    WHITE = RGBColor.from_string(_WHITE)
    DARK = RGBColor.from_string(_DARK)
    ICE = RGBColor.from_string(_ICE)
    GRAY = RGBColor.from_string(_GRAY)

    prs = Presentation()
    prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    SW, SH = prs.slide_width, prs.slide_height

    logo_path = str(_LOGO_LANDSCAPE) if _LOGO_LANDSCAPE.exists() else None

    # ─── Helpers ───

    def _f(run, sz=14, bold=False, color=DARK, name="Segoe UI"):
        run.font.size = Pt(sz); run.font.bold = bold
        run.font.color.rgb = color; run.font.name = name

    def _bar(slide, h=5, clr=NAVY):
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, Pt(h))
        s.fill.solid(); s.fill.fore_color.rgb = clr; s.line.fill.background()

    def _rect(slide, l, t, w, h, clr_hex):
        c = RGBColor.from_string(clr_hex)
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
        s.fill.solid(); s.fill.fore_color.rgb = c; s.line.fill.background()
        return s

    def _rrect(slide, l, t, w, h, clr_hex):
        c = RGBColor.from_string(clr_hex)
        s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
        s.fill.solid(); s.fill.fore_color.rgb = c; s.line.fill.background()
        return s

    def _txt(slide, l, t, w, h, text, sz=14, bold=False, color=DARK, align=PP_ALIGN.LEFT):
        box = slide.shapes.add_textbox(l, t, w, h)
        box.text_frame.word_wrap = True
        p = box.text_frame.paragraphs[0]; p.alignment = align
        r = p.add_run(); r.text = str(text); _f(r, sz, bold, color)
        return box

    def _set_native_bullet(para, char="●", color_hex=_NAVY_L, sz=10):
        """Set native PowerPoint bullet on a paragraph using XML."""
        pPr = para._p.get_or_add_pPr()
        nsmap = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
        for old in pPr.findall(qn('a:buNone')): pPr.remove(old)
        for old in pPr.findall(qn('a:buChar')): pPr.remove(old)
        for old in pPr.findall(qn('a:buFont')): pPr.remove(old)
        for old in pPr.findall(qn('a:buSzPct')): pPr.remove(old)
        for old in pPr.findall(qn('a:buClr')): pPr.remove(old)

        # Bullet color
        buClr = etree.SubElement(pPr, qn('a:buClr'))
        srgb = etree.SubElement(buClr, qn('a:srgbClr'))
        srgb.set('val', color_hex)

        # Bullet size
        buSz = etree.SubElement(pPr, qn('a:buSzPct'))
        buSz.set('val', str(sz * 10000))

        # Bullet char
        buFont = etree.SubElement(pPr, qn('a:buFont'))
        buFont.set('typeface', 'Arial')
        buCh = etree.SubElement(pPr, qn('a:buChar'))
        buCh.set('char', char)

    def _add_logo(slide, left=None, top=None, height=Inches(0.4)):
        if logo_path and os.path.exists(logo_path):
            l = left if left is not None else (SW - Inches(2.5))
            t = top if top is not None else Inches(6.9)
            try:
                slide.shapes.add_picture(logo_path, l, t, height=height)
            except Exception:
                pass

    # ─── Slide builders ───

    def _slide_bullets(heading, items, section_num=None, note=None):
        """Content slide with native PowerPoint bullets. Items: list of (label, desc) or str."""
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        _bar(slide)

        # Left accent stripe
        _rect(slide, 0, Inches(0.8), Pt(4), SH - Inches(1.6), _NAVY_L)

        # Section badge + heading
        h_left = Inches(0.7)
        if section_num is not None:
            _rrect(slide, Inches(0.5), Inches(0.25), Inches(0.55), Inches(0.55), _NAVY)
            _txt(slide, Inches(0.5), Inches(0.27), Inches(0.55), Inches(0.55),
                 str(section_num).zfill(2), sz=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
            h_left = Inches(1.2)

        _txt(slide, h_left, Inches(0.25), Inches(10), Inches(0.6),
             heading, sz=24, bold=True, color=NAVY)

        # Bullets body
        box = slide.shapes.add_textbox(Inches(0.9), Inches(1.2), Inches(11.2), SH - Inches(2.2))
        tf = box.text_frame; tf.word_wrap = True

        for idx, item in enumerate(items):
            if isinstance(item, tuple) and len(item) == 2:
                label, desc = str(item[0]), str(item[1])
            elif isinstance(item, dict):
                label = item.get("name", item.get("label", ""))
                desc = item.get("desc", item.get("description", ""))
            else:
                label, desc = "", str(item)

            p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
            p.space_before = Pt(6); p.space_after = Pt(3)
            p.level = 0

            # Native bullet
            _set_native_bullet(p, char="▸", color_hex=_NAVY_L, sz=8)

            if label and desc:
                r1 = p.add_run(); r1.text = label + "  "; _f(r1, 12, True, NAVY)
                r2 = p.add_run(); r2.text = desc; _f(r2, 12, False, DARK)
            else:
                r1 = p.add_run(); r1.text = label or desc; _f(r1, 12, False, DARK)

        if note:
            _txt(slide, Inches(0.7), Inches(6.7), Inches(10), Inches(0.4), note, sz=9, color=GRAY)
        _add_logo(slide)
        return slide

    def _slide_table(heading, headers, rows, col_pcts=None, section_num=None, note=None):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        _bar(slide)
        _rect(slide, 0, Inches(0.8), Pt(4), SH - Inches(1.6), _NAVY_L)

        h_left = Inches(0.7)
        if section_num is not None:
            _rrect(slide, Inches(0.5), Inches(0.25), Inches(0.55), Inches(0.55), _NAVY)
            _txt(slide, Inches(0.5), Inches(0.27), Inches(0.55), Inches(0.55),
                 str(section_num).zfill(2), sz=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
            h_left = Inches(1.2)
        _txt(slide, h_left, Inches(0.25), Inches(10), Inches(0.6), heading, sz=24, bold=True, color=NAVY)

        n_cols = len(headers); display = rows[:11]; n_rows = len(display) + 1
        tbl_w = Inches(11.5)
        tbl_shape = slide.shapes.add_table(n_rows, n_cols, Inches(0.7), Inches(1.2), tbl_w, Pt(26) * n_rows)
        tbl = tbl_shape.table

        if col_pcts and len(col_pcts) == n_cols:
            for j, pct in enumerate(col_pcts):
                tbl.columns[j].width = int(tbl_w * pct / 100)

        for j, h in enumerate(headers):
            cell = tbl.cell(0, j); cell.text = ""
            cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
            r = cell.text_frame.paragraphs[0].add_run()
            r.text = str(h); _f(r, 9, True, WHITE)

        for i, row in enumerate(display):
            for j, val in enumerate(row):
                cell = tbl.cell(i + 1, j); cell.text = ""
                if i % 2 == 1:
                    cell.fill.solid(); cell.fill.fore_color.rgb = ICE
                r = cell.text_frame.paragraphs[0].add_run()
                r.text = str(val)[:80]; _f(r, 9, False, DARK)

        if note:
            _txt(slide, Inches(0.7), Inches(6.7), Inches(10), Inches(0.4), note, sz=9, color=GRAY)
        _add_logo(slide)
        return slide

    # ═══════════ BUILD ═══════════

    # 1 — Title
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _rect(s, 0, 0, SW, SH, _NAVY)  # full bg
    _rect(s, 0, 0, Pt(6), SH, "4FC3F7")  # left accent
    _rect(s, Inches(1), Inches(1.2), Inches(2), Pt(4), "4FC3F7")  # top accent line
    _txt(s, Inches(1), Inches(1.6), Inches(11), Inches(2.5),
         data["project_title"], sz=28, bold=True, color=WHITE)
    _txt(s, Inches(1), Inches(4.3), Inches(5), Inches(0.4), "Disiapkan untuk:", sz=11, color=ICE)
    _txt(s, Inches(1), Inches(4.7), Inches(8), Inches(0.6),
         data["client"], sz=20, bold=True, color=WHITE)
    _txt(s, Inches(1), Inches(5.8), Inches(10), Inches(0.4),
         data["date"], sz=12, color=ICE)
    if logo_path:
        try: s.shapes.add_picture(logo_path, Inches(1), Inches(6.4), height=Inches(0.5))
        except: pass
    _txt(s, Inches(1), Inches(7.0), Inches(10), Inches(0.3),
         "RAHASIA — Hak milik intelektual PT Indonesian Data Ecosystem", sz=8, color=GRAY)

    # 2 — Agenda
    _slide_bullets("Agenda", [
        "Latar Belakang dan Konteks",
        "Tujuan Proyek (SMART)",
        "Ruang Lingkup dan Deliverables",
        "Metodologi dan Pendekatan",
        "Rencana Kerja dan Timeline",
        "Tim Proyek",
        "Investasi dan Struktur Biaya",
        "Manajemen Risiko dan Kepatuhan",
        "Tentang IDEAS",
    ])

    # 3 — Konteks
    _slide_bullets("Latar Belakang dan Konteks",
        [(c, "") for c in data["challenges"]],
        section_num=1,
        note=f"{data['total_services']} layanan · {data['total_mandays']:.0f} man-days · {data['months']} bulan")

    # 4 — SMART
    _slide_bullets("Tujuan Proyek (SMART)", [
        ("Specific —", data["smart"]["specific"]),
        ("Measurable —", data["smart"]["measurable"]),
        ("Achievable —", data["smart"]["achievable"]),
        ("Relevant —", data["smart"]["relevant"]),
        ("Time-Bound —", data["smart"]["timebound"]),
    ], section_num=2)

    # 5 — Scope
    scope = []
    for item in data["inscope"]:
        n = item["name"] if isinstance(item, dict) else str(item)
        d = item.get("desc", "") if isinstance(item, dict) else ""
        scope.append(("✓ " + n, d))
    for item in data["outscope"]:
        scope.append(("✗ " + (str(item) if not isinstance(item, dict) else item.get("name", "")), ""))
    _slide_bullets("Ruang Lingkup Proyek", scope, section_num=3)

    # 6-7 — Deliverables
    dr = [[str(i+1), d["service"][:22], d["name"], d["format"]]
          for i, d in enumerate(data["deliverables"])]
    _slide_table("Deliverables Utama", ["No", "Layanan", "Deliverable", "Format"],
                 dr[:11], col_pcts=[5, 22, 58, 15], section_num=4)
    if len(dr) > 11:
        _slide_table("Deliverables (lanjutan)", ["No", "Layanan", "Deliverable", "Format"],
                     dr[11:], col_pcts=[5, 22, 58, 15])

    # 8 — Metodologi
    _slide_bullets("Pendekatan dan Metodologi", [
        ("DAMA-DMBOK —", "Basis pengetahuan manajemen data: tata kelola, kualitas, arsitektur, keamanan"),
        ("Agile / CRISP-DM —", "Pengelolaan proyek adaptif, iteratif, dan fokus pada hasil"),
        ("PMBOK 6th & 7th —", "Disiplin manajemen proyek terstruktur dan tata kelola kuat"),
        ("End-to-End Frameworks —", "BMC, VPC, BSC, Shipley, BABOK untuk keselarasan bisnis"),
    ], section_num=5)

    # 9 — Timeline
    tl = [[a["month"], a["phase"], a["service_id"], a["activities"][:50]]
          for a in data["monthly_activities"]]
    _slide_table("Rencana Kerja", ["Bulan", "Fase", "Layanan", "Aktivitas"],
                 tl, col_pcts=[8, 18, 12, 62], section_num=6,
                 note=f"Durasi: {data['months']} bulan · {data['total_mandays']:.0f} man-days")

    # 10 — Tim
    tr = [[str(i+1), f"{t['role']} ({t['count']})", t["desc"][:50]]
          for i, t in enumerate(data["team"])]
    _slide_table("Tim Proyek", ["#", "Peran", "Tanggung Jawab"],
                 tr, col_pcts=[5, 35, 60], section_num=7,
                 note=f"Total: {data['headcount']} tenaga ahli")

    # 11 — Investasi
    c = data["costs"]
    cr = [
        [f"A. Jasa Profesional ({data['headcount']} orang × {data['months']} bulan)", f"Rp {c['personnel']:,.0f}"],
        ["B. Biaya Operasional", f"Rp {c['operational']:,.0f}"],
        ["C. Manajemen Risiko (10%)", f"Rp {c['risk']:,.0f}"],
        ["D. Total Sebelum PPN", f"Rp {c['total']:,.0f}"],
        ["E. PPN 11%", f"Rp {c['vat']:,.0f}"],
        ["F. TOTAL INVESTASI", f"Rp {c['grand_total']:,.0f}"],
    ]
    _slide_table("Investasi dan Struktur Biaya", ["Komponen", "Biaya (Rp)"],
                 cr, col_pcts=[65, 35], section_num=8)

    # 12 — Risiko
    _slide_table("Risiko dan Mitigasi", ["Risiko", "Dampak", "Prob.", "Mitigasi"], [
        ["Keterlambatan data", "Sedang", "Sedang", "Komunikasi proaktif & eskalasi"],
        ["Perubahan prioritas klien", "Tinggi", "Rendah", "Manajemen perubahan formal"],
        ["Keterbatasan SDM klien", "Sedang", "Tinggi", "Capacity building intensif"],
    ], col_pcts=[28, 12, 12, 48], section_num=9)

    # 13 — Regulasi
    rg = [[r["name"], r["relevance"]] for r in data["regulations"]]
    _slide_table("Kepatuhan Regulasi", ["Regulasi / Standar", "Relevansi"],
                 rg, col_pcts=[35, 65], section_num=10)

    # 14 — IDEAS
    _slide_bullets("Tentang IDEAS", [
        ("Advisory & Governance (S1.1–S1.5) —", "Fondasi strategis: peta jalan, valuasi data, tata kelola AI"),
        ("Platform & Implementation (S2.1–S2.6) —", "Implementasi teknis: arsitektur data, portal, GenAI"),
        ("Empowerment & Services (S3.1–S3.4) —", "Keberlanjutan: kapasitas SDM, layanan terkelola"),
    ], note="PT Indonesian Data Ecosystem · https://data-ecosystem.id · contact@data-ecosystem.id")

    # 15 — Closing
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _rect(s, 0, 0, SW, SH, _NAVY)
    _rect(s, 0, 0, Pt(6), SH, "4FC3F7")
    _rect(s, Inches(5.2), Inches(3.0), Inches(3), Pt(4), "4FC3F7")
    _txt(s, Inches(1), Inches(3.2), Inches(11.3), Inches(1.2),
         "Terima Kasih", sz=44, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    _txt(s, Inches(1), Inches(4.6), Inches(11.3), Inches(0.5),
         "PT Indonesian Data Ecosystem (IDEAS)", sz=16, color=ICE, align=PP_ALIGN.CENTER)
    _txt(s, Inches(1), Inches(5.2), Inches(11.3), Inches(0.4),
         "contact@data-ecosystem.id  ·  https://data-ecosystem.id", sz=12, color=ICE, align=PP_ALIGN.CENTER)
    if logo_path:
        try: s.shapes.add_picture(logo_path, Inches(5.4), Inches(6.2), height=Inches(0.5))
        except: pass

    try:
        prs.save(output_path)
        logger.info("PPTX: %s (%d slides)", output_path, len(prs.slides))
        return output_path
    except IOError as e:
        logger.error("PPTX save failed: %s", e); return None


# ═══════════════════════════════════════════════════════════════════════
# DOCX BUILDER (kept stable — verified correct)
# ═══════════════════════════════════════════════════════════════════════
def build_docx(data: Dict[str, Any], output_path: str) -> Optional[str]:
    try:
        from docx import Document
        from docx.shared import Pt, Inches, Cm, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.enum.table import WD_TABLE_ALIGNMENT
        from docx.oxml.ns import qn, nsdecls
        from docx.oxml import parse_xml
    except ImportError:
        logger.error("python-docx required"); return None

    NAVY = RGBColor(0x0A, 0x0A, 0x5C); NAVY_L = RGBColor(0x1F, 0x4E, 0x79)
    DARK = RGBColor(0x2D, 0x2D, 0x2D); FONT = "Segoe UI"
    logo = str(_LOGO_LANDSCAPE) if _LOGO_LANDSCAPE.exists() else None

    doc = Document()
    for sec in doc.sections:
        sec.page_width = Cm(21); sec.page_height = Cm(29.7)
        sec.top_margin = Cm(2.5); sec.bottom_margin = Cm(2.5)
        sec.left_margin = Cm(2.5); sec.right_margin = Cm(2.0)

    style = doc.styles['Normal']
    style.font.name = FONT; style.font.size = Pt(10); style.font.color.rgb = DARK
    style.paragraph_format.space_after = Pt(6); style.paragraph_format.line_spacing = 1.15
    for lv in range(1, 5):
        hs = doc.styles[f'Heading {lv}']
        hs.font.name = FONT; hs.font.color.rgb = NAVY; hs.font.bold = True
        hs.font.size = Pt([0, 18, 14, 12, 11][lv])
        hs.paragraph_format.space_before = Pt([0, 24, 18, 12, 8][lv])

    def _p(text, bold=False, italic=False, sz=10, color=DARK, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph(); p.alignment = align
        r = p.add_run(text); r.font.name = FONT; r.font.size = Pt(sz)
        r.font.bold = bold; r.font.italic = italic; r.font.color.rgb = color
        return p

    def _b(text, label=None):
        p = doc.add_paragraph(style='List Bullet')
        if label:
            r1 = p.add_run(label + "  "); r1.font.name = FONT; r1.font.size = Pt(10)
            r1.font.bold = True; r1.font.color.rgb = NAVY
        r2 = p.add_run(text); r2.font.name = FONT; r2.font.size = Pt(10); r2.font.color.rgb = DARK

    def _n(text, label=None):
        p = doc.add_paragraph(style='List Number')
        if label:
            r1 = p.add_run(label + " — "); r1.font.name = FONT; r1.font.size = Pt(10)
            r1.font.bold = True; r1.font.color.rgb = NAVY
        r2 = p.add_run(text); r2.font.name = FONT; r2.font.size = Pt(10); r2.font.color.rgb = DARK

    def _tbl(headers, rows, widths_cm=None):
        t = doc.add_table(rows=len(rows) + 1, cols=len(headers))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.style = 'Table Grid'
        t.autofit = False
        tblPr = t._tbl.find(qn('w:tblPr'))
        if tblPr is None:
            tblPr = parse_xml(f'<w:tblPr {nsdecls("w")}/>'); t._tbl.insert(0, tblPr)
        tblPr.append(parse_xml(f'<w:tblLayout {nsdecls("w")} w:type="fixed"/>'))

        for j, h in enumerate(headers):
            c = t.rows[0].cells[j]; c.text = ""
            r = c.paragraphs[0].add_run(h); r.font.name = FONT; r.font.size = Pt(9)
            r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            c._tc.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{_NAVY_L}"/>'))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                c = t.rows[i + 1].cells[j]; c.text = ""
                r = c.paragraphs[0].add_run(str(val)); r.font.name = FONT; r.font.size = Pt(9); r.font.color.rgb = DARK
                if i % 2 == 1:
                    c._tc.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{_ACCENT}"/>'))
        if widths_cm:
            for j, w in enumerate(widths_cm):
                wd = int(w * 567)
                for row in t.rows:
                    tcPr = row.cells[j]._tc.get_or_add_tcPr()
                    old = tcPr.find(qn('w:tcW'))
                    if old is not None: tcPr.remove(old)
                    tcPr.append(parse_xml(f'<w:tcW {nsdecls("w")} w:w="{wd}" w:type="dxa"/>'))
        doc.add_paragraph()

    # ═══ COVER ═══
    for _ in range(4): doc.add_paragraph()
    if logo:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(logo, width=Cm(8))
    for _ in range(2): doc.add_paragraph()
    _p(data["project_title"], bold=True, sz=22, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_paragraph()
    _p("Disiapkan untuk:", sz=11, color=DARK, align=WD_ALIGN_PARAGRAPH.CENTER)
    _p(data["client"], bold=True, sz=16, color=NAVY_L, align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_paragraph()
    _p(data["date"], sz=12, color=DARK, align=WD_ALIGN_PARAGRAPH.CENTER)
    for _ in range(4): doc.add_paragraph()
    _p("PT Indonesian Data Ecosystem (IDEAS)", bold=True, sz=11, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
    _p("contact@data-ecosystem.id  ·  https://data-ecosystem.id", sz=9, color=DARK, align=WD_ALIGN_PARAGRAPH.CENTER)
    _p("RAHASIA — Hak milik intelektual PT Indonesian Data Ecosystem",
       sz=8, italic=True, color=RGBColor(0x88, 0x88, 0x88), align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_page_break()

    # ═══ 1. KONTEKS ═══
    doc.add_heading("Latar Belakang dan Tujuan", level=1)
    doc.add_heading("Konteks Proyek", level=2)
    _p(f"{data['client']} menghadapi tantangan transformasi digital yang membutuhkan "
       f"pengelolaan data secara terstruktur, terstandar, dan berkelanjutan.")
    for c in data["challenges"]: _b(c)
    _p(f"Proyek ini mencakup {data['total_services']} layanan terintegrasi dengan total "
       f"{data['total_mandays']:.0f} man-days selama {data['months']} bulan.")

    doc.add_heading("Tujuan Proyek (SMART)", level=2)
    for k in ["specific", "measurable", "achievable", "relevant", "timebound"]:
        _b(data["smart"][k], label=k.capitalize() + ":")
    doc.add_page_break()

    # ═══ 2. SCOPE ═══
    doc.add_heading("Ruang Lingkup dan Hasil", level=1)
    doc.add_heading("Ruang Lingkup Proyek", level=2)
    _p("In-Scope (Termasuk dalam Lingkup):", bold=True, color=NAVY)
    for item in data["inscope"]:
        if isinstance(item, dict):
            _n(item.get("desc", ""), label=item.get("name", ""))
        else: _n(str(item))
    doc.add_paragraph()
    _p("Out-of-Scope (Tidak Termasuk dalam Lingkup):", bold=True, color=NAVY)
    for item in data["outscope"]:
        _n(str(item) if not isinstance(item, dict) else item.get("name", ""))

    doc.add_heading("Deliverables Utama", level=2)
    dr = [[str(i+1), d["service"], d["name"], d["description"], d["format"]]
          for i, d in enumerate(data["deliverables"])]
    _tbl(["No", "Layanan", "Deliverable", "Deskripsi", "Format"], dr,
         widths_cm=[1, 3.5, 3.5, 5, 2])
    doc.add_page_break()

    # ═══ 3. METODOLOGI ═══
    doc.add_heading("Pendekatan dan Metodologi", level=1)
    _p("Kerangka kerja kami menyatukan praktik terbaik global:")
    _b("Basis pengetahuan manajemen data: tata kelola, kualitas, arsitektur, keamanan.", label="DAMA-DMBOK:")
    _b("Pengelolaan proyek adaptif, iteratif, dan fokus pada hasil.", label="Agile / CRISP-DM:")
    _b("Disiplin manajemen proyek terstruktur dan tata kelola kuat.", label="PMBOK 6th & 7th:")
    _b("BMC, VPC, BSC, Shipley, BABOK untuk keselarasan bisnis.", label="End-to-End Frameworks:")

    # ═══ 4. TIMELINE ═══
    doc.add_heading("Rencana Kerja dan Jadwal", level=1)
    ar = [[a["month"], a["phase"], a["service_id"], a["activities"]] for a in data["monthly_activities"]]
    _tbl(["Bulan", "Fase", "Layanan", "Aktivitas Utama"], ar, widths_cm=[1.5, 3, 2, 9.5])
    doc.add_page_break()

    # ═══ 5. TIM ═══
    doc.add_heading("Tim Proyek", level=1)
    tr = [[str(i+1), f"{t['role']} ({t['count']} orang)", t["desc"]] for i, t in enumerate(data["team"])]
    _tbl(["#", "Peran", "Tanggung Jawab"], tr, widths_cm=[1, 5, 10])

    # ═══ 6. INVESTASI ═══
    doc.add_heading("Investasi dan Struktur Biaya", level=1)
    co = data["costs"]
    cr = [
        [f"A. Jasa Profesional ({data['headcount']} orang × {data['months']} bulan)", f"Rp {co['personnel']:,.0f}"],
        ["B. Biaya Operasional", f"Rp {co['operational']:,.0f}"],
        ["C. Manajemen Risiko (10%)", f"Rp {co['risk']:,.0f}"],
        ["D. Total Sebelum PPN", f"Rp {co['total']:,.0f}"],
        ["E. PPN 11%", f"Rp {co['vat']:,.0f}"],
        ["F. Total Investasi", f"Rp {co['grand_total']:,.0f}"],
    ]
    _tbl(["Komponen", "Biaya"], cr, widths_cm=[10.5, 5.5])

    # ═══ 7. RISIKO ═══
    doc.add_heading("Asumsi, Risiko, dan Kepatuhan", level=1)
    doc.add_heading("Asumsi Proyek", level=2)
    _n("Ketersediaan stakeholder klien untuk wawancara dan diskusi sesuai jadwal.")
    _n("Akses ke sistem, data, dan dokumentasi diberikan tepat waktu.")
    _n("Lingkup pekerjaan tidak berubah signifikan selama proyek.")

    doc.add_heading("Risiko dan Mitigasi", level=2)
    _tbl(["Risiko", "Dampak", "Prob.", "Mitigasi"], [
        ["Keterlambatan data", "Sedang", "Sedang", "Komunikasi proaktif & eskalasi"],
        ["Perubahan prioritas klien", "Tinggi", "Rendah", "Manajemen perubahan formal"],
        ["Keterbatasan SDM klien", "Sedang", "Tinggi", "Capacity building intensif"],
    ], widths_cm=[4.5, 2, 2, 7.5])

    doc.add_heading("Kepatuhan Regulasi", level=2)
    _tbl(["Regulasi / Standar", "Relevansi"],
         [[r["name"], r["relevance"]] for r in data["regulations"]],
         widths_cm=[5.5, 10.5])
    doc.add_page_break()

    # ═══ 8. CHANGE MGMT ═══
    doc.add_heading("Manajemen Perubahan dan Pemberdayaan", level=1)
    _tbl(["Fase", "Aktivitas", "Output"], [
        ["Awareness", "Sosialisasi stakeholder", "Dukungan dan pemahaman"],
        ["Knowledge", "Workshop dan pelatihan", "Peningkatan kompetensi"],
        ["Adoption", "Pendampingan implementasi", "Proses baru diadopsi"],
        ["Sustainability", "Monitoring berkelanjutan", "Kemandirian"],
    ], widths_cm=[3, 7, 6])
    doc.add_heading("Rencana Capacity Building", level=2)
    _tbl(["Program", "Target", "Durasi", "Output"],
         [[p["program"], p["target"], p["duration"], p["output"]] for p in data["capacity_building"]],
         widths_cm=[4.5, 4, 2.5, 5])

    # ═══ 9. IDEAS ═══
    doc.add_heading("Tentang IDEAS", level=1)
    _p("PT Indonesian Data Ecosystem (IDEAS) adalah firma konsultansi dan implementasi "
       "yang berfokus pada ekosistem data.")
    _n("Fondasi strategis: peta jalan, valuasi data, tata kelola AI.", label="Advisory & Governance (S1.1–S1.5)")
    _n("Implementasi teknis: arsitektur data, portal, GenAI.", label="Platform & Implementation (S2.1–S2.6)")
    _n("Keberlanjutan: kapasitas SDM, layanan terkelola.", label="Empowerment & Services (S3.1–S3.4)")
    doc.add_paragraph()
    _p("PT Indonesian Data Ecosystem (IDEAS)", bold=True, sz=9, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
    _p("contact@data-ecosystem.id  ·  https://data-ecosystem.id", sz=8, color=DARK, align=WD_ALIGN_PARAGRAPH.CENTER)

    try:
        doc.save(output_path); logger.info("DOCX: %s", output_path); return output_path
    except IOError as e:
        logger.error("DOCX save failed: %s", e); return None
