#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: 1.1
# Last Modified: 2026-02-20
"""
IDEAS Professional DOCX Generator

Converts Markdown documents to branded Word (DOCX) with IDEAS visual identity.
Uses python-docx for high-quality document generation.

Features:
  - Cover page with IDEAS logo and navy accent
  - Consistent branding: navy headings, clean fonts
  - Professional tables with navy headers
  - Running header with logo, footer with page numbers
  - Auto-parses Markdown headings, lists, tables, blockquotes

Usage:
    python3 generate_docx.py --input proposal.md --output proposal.docx \\
        --title "Proposal Konsultansi Data" \\
        --subtitle "Asesmen Kematangan Data" \\
        --client "Pemerintah Provinsi Jawa Barat"

    python3 generate_docx.py --input report.md --output report.docx --no-cover

Dependencies:
    pip install python-docx
"""

import argparse
import logging
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

try:
    from docx import Document
    from docx.document import Document as DocumentObject
    from docx.shared import Inches, Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.section import WD_ORIENT
    from docx.oxml.ns import qn, nsdecls
    from docx.oxml import OxmlElement, parse_xml
    from docx.table import _Cell
    from docx.text.paragraph import Paragraph
except ImportError as e:
    print(f"Error: Missing dependency - {e}", file=sys.stderr)
    print("Install with: pip install python-docx", file=sys.stderr)
    sys.exit(1)

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Constants ---
# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / "templates"
LOGO_LANDSCAPE = TEMPLATES_DIR / "LogoIDEASLandscape.png"
LOGO_PORTRAIT = TEMPLATES_DIR / "LogoIDEASPotrait.png"  # Corrected spelling in var name, path is intentionally misspelled

# Branding
NAVY = RGBColor(0x0A, 0x0A, 0x5C)
NAVY_LIGHT = RGBColor(0x1A, 0x1A, 0x8C)
TEXT_DARK = RGBColor(0x2D, 0x2D, 0x3D)
TEXT_GRAY = RGBColor(0x6B, 0x72, 0x80)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TABLE_ALT = RGBColor(0xF8, 0xF9, 0xFC)
TABLE_BORDER_COLOR = "D8DAE5"

# Company Info
COMPANY_NAME = "PT Indonesian Data Ecosystem"
COMPANY_SHORT = "IDEAS"
COMPANY_TAGLINE = "Empowering Innovation Through Data"
COMPANY_ADDRESS = "Komplek Margahayu Raya, Jl. Uranus IV Blok C3 No.59, Bandung 40286"
COMPANY_EMAIL = "contact@data-ecosystem.id"
COMPANY_WEB = "https://data-ecosystem.id"


def _set_cell_shading(cell: _Cell, color_hex: str) -> None:
    """Set cell background color.

    Args:
        cell: The table cell to modify.
        color_hex: The hex code for the background color.
    """
    try:
        shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}" w:val="clear"/>')
        cell._tc.get_or_add_tcPr().append(shading_elm)
    except Exception as e:
        logger.warning(f"Failed to set cell shading: {e}")

def _set_cell_borders(cell: _Cell, color: str = "0A0A5C", size: str = "4") -> None:
    """Set cell borders.

    Args:
        cell: The table cell to modify.
        color: The hex color for the border.
        size: The size of the border.
    """
    try:
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        border_xml = (
            f'<w:tcBorders {nsdecls("w")}>'
            f'  <w:top w:val="single" w:sz="{size}" w:space="0" w:color="{color}"/>'
            f'  <w:left w:val="single" w:sz="{size}" w:space="0" w:color="{color}"/>'
            f'  <w:bottom w:val="single" w:sz="{size}" w:space="0" w:color="{color}"/>'
            f'  <w:right w:val="single" w:sz="{size}" w:space="0" w:color="{color}"/>'
            f'</w:tcBorders>'
        )
        borders = parse_xml(border_xml)
        tcPr.append(borders)
    except Exception as e:
        logger.warning(f"Failed to set cell borders: {e}")

def _add_run(paragraph: Paragraph, text: str, size: float = 10, bold: bool = False, color: RGBColor = TEXT_DARK, font_name: str = "Segoe UI"):
    """Add a formatted run to a paragraph. Returns the run."""
    run = paragraph.add_run(text)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:eastAsia'), font_name)
    return run

def _setup_styles(doc: DocumentObject) -> None:
    """Configure document styles for IDEAS branding.

    Args:
        doc: The main Document object.
    """
    try:
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Segoe UI'
        font.size = Pt(10)
        font.color.rgb = TEXT_DARK

        pf = style.paragraph_format
        pf.space_after = Pt(6)
        pf.line_spacing = 1.15

        # Heading styles
        for level, (size, is_bold) in enumerate([(19, True), (14, True), (12, True), (10.5, True)], 1):
            style_name = f'Heading {level}'
            if style_name in doc.styles:
                h_style = doc.styles[style_name]
                h_style.font.name = 'Segoe UI'
                h_style.font.size = Pt(size)
                h_style.font.bold = is_bold
                h_style.font.color.rgb = NAVY if level <= 3 else TEXT_DARK
                h_style.paragraph_format.space_before = Pt(12 if level <= 2 else 8)
                h_style.paragraph_format.space_after = Pt(6)
                h_style.paragraph_format.keep_with_next = True
    except Exception as e:
        logger.error(f"Failed to set up document styles: {e}")

def _add_header_footer(doc: DocumentObject) -> None:
    """Add running header with logo and footer with page numbers.

    Args:
        doc: The main Document object.
    """
    section = doc.sections[0] if doc.sections else doc.add_section()

    # Header
    header = section.header
    header.is_linked_to_previous = False
    h_para = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    h_para.alignment = WD_ALIGN_PARAGRAPH.LEFT

    if LOGO_LANDSCAPE.exists():
        try:
            run = h_para.add_run()
            run.add_picture(str(LOGO_LANDSCAPE), width=Inches(1.3))
        except Exception as e:
            logger.warning(f"Could not add landscape logo to header: {e}")
    else:
        logger.warning(f"Header logo not found at {LOGO_LANDSCAPE}, skipping.")

    # Footer with page numbers
    footer = section.footer
    footer.is_linked_to_previous = False
    f_para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    f_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    _add_run(f_para, f"{COMPANY_SHORT} — {COMPANY_TAGLINE}  |  ", size=7, color=TEXT_GRAY)

    # Add page number field using complex field
    try:
        run = f_para.add_run()
        run.font.size = Pt(7)
        run.font.color.rgb = TEXT_GRAY
        fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
        run._element.append(fldChar1)

        run2 = f_para.add_run()
        run2.font.size = Pt(7)
        run2.font.color.rgb = TEXT_GRAY
        instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
        run2._element.append(instrText)

        run3 = f_para.add_run()
        run3.font.size = Pt(7)
        fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
        run3._element.append(fldChar2)
    except Exception as e:
        logger.warning(f"Failed to add page number field to footer: {e}")

def _create_cover_page(doc: DocumentObject, title: str, subtitle: Optional[str], client: Optional[str], doc_date: str, doc_number: Optional[str]) -> None:
    """Create an elegant minimalist cover page.

    Args:
        doc: The main Document object.
        title: The main title of the document.
        subtitle: The subtitle of the document.
        client: The client's name.
        doc_date: The date of the document.
        doc_number: The document reference number.
    """
    section = doc.sections[0]
    section.different_first_page_header_footer = True

    # Logo
    if LOGO_PORTRAIT.exists():
        try:
            logo_para = doc.add_paragraph()
            logo_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = logo_para.add_run()
            run.add_picture(str(LOGO_PORTRAIT), height=Inches(1.5))
        except Exception as e:
            logger.warning(f"Could not add portrait logo to cover page: {e}")
    else:
        logger.warning(f"Cover page logo not found at {LOGO_PORTRAIT}, skipping.")
        doc.add_paragraph()

    # Spacing
    for _ in range(2):
        doc.add_paragraph()

    # Title
    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(title_para, title.upper(), size=24, bold=True, color=NAVY)

    # Subtitle
    if subtitle:
        sub_para = doc.add_paragraph()
        sub_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _add_run(sub_para, subtitle, size=14, color=TEXT_GRAY)

    # Spacing
    for _ in range(8):
        doc.add_paragraph()

    # Metadata table
    meta_data = []
    if client:
        meta_data.append(("DIPERSIAPKAN UNTUK", client))
    meta_data.append(("DIPERSIAPKAN OLEH", COMPANY_NAME))
    if doc_date:
        meta_data.append(("TANGGAL", doc_date))
    if doc_number:
        meta_data.append(("NO. DOKUMEN", doc_number))

    if meta_data:
        meta_table = doc.add_table(rows=len(meta_data), cols=2)
        meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, (label, value) in enumerate(meta_data):
            cell_label = meta_table.cell(i, 0)
            cell_value = meta_table.cell(i, 1)
            p_label = cell_label.paragraphs[0]
            p_label.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            _add_run(p_label, label, size=9, color=TEXT_GRAY, bold=True)
            p_value = cell_value.paragraphs[0]
            p_value.alignment = WD_ALIGN_PARAGRAPH.LEFT
            _add_run(p_value, value, size=10, bold=True, color=NAVY)
            cell_label.width = Inches(3.0)
            cell_value.width = Inches(4.0)

    # Footer info
    doc.add_paragraph() # Spacer
    footer_para = doc.add_paragraph()
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(footer_para, f"{COMPANY_ADDRESS} | {COMPANY_EMAIL} | {COMPANY_WEB}", size=8, color=TEXT_GRAY)

    doc.add_page_break()

def _add_table(doc: DocumentObject, headers: List[str], rows: List[List[str]]) -> None:
    """Add a formatted table to the document.

    Args:
        doc: The main Document object.
        headers: A list of strings for the table header.
        rows: A list of lists, where each inner list is a row.
    """
    if not headers or not rows:
        logger.warning("Attempted to add a table with no headers or rows.")
        return

    try:
        table = doc.add_table(rows=1, cols=len(headers))
        table.style = 'Table Grid'
        table.autofit = True

        # Header row
        for i, header_text in enumerate(headers):
            cell = table.cell(0, i)
            cell.text = ""
            _set_cell_shading(cell, "0A0A5C")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            _add_run(p, header_text.upper(), size=9, bold=True, color=WHITE)

        # Data rows
        for i, row_data in enumerate(rows):
            row_cells = table.add_row().cells
            for j, cell_text in enumerate(row_data):
                cell = row_cells[j]
                cell.text = str(cell_text)
                if (i + 1) % 2 == 0:
                    _set_cell_shading(cell, "F8F9FC")

        doc.add_paragraph()  # Spacing after table
    except Exception as e:
        logger.error(f"Failed to create table: {e}")

def _add_blockquote(doc: DocumentObject, text: str) -> None:
    """Add a styled blockquote paragraph.

    Args:
        doc: The main Document object.
        text: The text for the blockquote.
    """
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Add left border via paragraph properties
    pPr = para._element.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:left w:val="single" w:sz="18" w:space="4" w:color="0A0A5C"/></w:pBdr>')
    pPr.append(pBdr)

    # Add indentation
    ind = parse_xml(f'<w:ind {nsdecls("w")} w:left="360"/>')
    pPr.append(ind)

    clean_text = re.sub(r'\*+\s*', '', text).strip()
    run = para.add_run(clean_text)
    run.font.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = TEXT_DARK

def parse_and_build_docx(doc: DocumentObject, md_text: str) -> None:
    """Parse Markdown and build document content.

    Args:
        doc: The main Document object.
        md_text: The string containing Markdown text.
    """
    lines = md_text.strip().split("\n")
    table_headers: List[str] = []
    table_rows: List[List[str]] = []
    in_table = False

    def flush_table() -> None:
        nonlocal table_headers, table_rows, in_table
        if in_table and table_headers and table_rows:
            _add_table(doc, table_headers, table_rows)
        table_headers = []
        table_rows = []
        in_table = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            flush_table()
            continue

        if stripped.startswith("#"):
            flush_table()
            level = len(stripped) - len(stripped.lstrip("#"))
            heading_text = stripped.lstrip("# ").strip()
            if 1 <= level <= 4:
                doc.add_heading(heading_text, level=level)
            else:
                doc.add_paragraph(stripped) # Treat as normal text if heading level is > 4
            continue

        if "|" in stripped and stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if all(re.match(r'[-: ]+$', c) for c in cells):
                continue # Skip separator line
            if not table_headers:
                table_headers = cells
                in_table = True
            else:
                table_rows.append(cells)
            continue

        flush_table()

        if stripped.startswith(">"):
            _add_blockquote(doc, stripped[1:].lstrip())
        elif stripped.startswith("- ") or stripped.startswith("* "):
            para = doc.add_paragraph(style='List Bullet')
            _apply_md_inline(para, stripped[2:])
        elif re.match(r'^\d+\.\s+', stripped):
            para = doc.add_paragraph(style='List Number')
            _apply_md_inline(para, re.sub(r'^\d+\.\s+', '', stripped))
        else:
            para = doc.add_paragraph()
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            _apply_md_inline(para, stripped)

    flush_table()


def _apply_md_inline(para, text: str) -> None:
    """Parse markdown inline formatting and add properly styled runs.

    Handles: ***bold+italic***, **bold**, *italic*, `code`, plain text.
    """
    parts = re.split(r'(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*|`.+?`)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith("***") and part.endswith("***"):
            run = _add_run(para, part[3:-3], bold=True, color=NAVY)
            run.italic = True
        elif part.startswith("**") and part.endswith("**"):
            _add_run(para, part[2:-2], bold=True, color=NAVY)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = _add_run(para, part[1:-1])
            run.italic = True
        elif part.startswith("`") and part.endswith("`"):
            _add_run(para, part[1:-1], size=9, font_name="Consolas")
        else:
            _add_run(para, part)

def generate_docx(
    input_text: str,
    output_path: str,
    title: str = "Dokumen IDEAS",
    subtitle: str = "",
    client: str = "",
    doc_date: str = "",
    doc_number: str = "",
    show_cover: bool = True,
    landscape: bool = False,
) -> str:
    """Generate a branded DOCX from Markdown text.

    Args:
        input_text: Markdown content string.
        output_path: Path for the output DOCX file.
        title: Document title.
        subtitle: Document subtitle.
        client: Client name.
        doc_date: Document date string.
        doc_number: Document reference number.
        show_cover: Whether to show cover page.
        landscape: Use landscape orientation.

    Returns:
        Absolute path to the generated DOCX file.

    Raises:
        IOError: If the file cannot be written.
    """
    doc = Document()

    # Page setup
    section = doc.sections[0]
    if landscape:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width, section.page_height = Inches(11.69), Inches(8.27)
    else:
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width, section.page_height = Inches(8.27), Inches(11.69)

    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(0.87)
    section.right_margin = Inches(0.87)

    _setup_styles(doc)

    if not doc_date:
        months_id = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        today = date.today()
        doc_date = f"{today.day} {months_id[today.month]} {today.year}"

    if show_cover:
        _create_cover_page(doc, title, subtitle, client, doc_date, doc_number)

    _add_header_footer(doc)
    parse_and_build_docx(doc, input_text)

    # Confidentiality notice
    doc.add_paragraph()
    conf_para = doc.add_paragraph()
    conf_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(conf_para, f"Dokumen ini bersifat rahasia. Dilarang memperbanyak tanpa izin tertulis dari {COMPANY_SHORT}.", size=8, color=TEXT_GRAY)

    abs_output_path = os.path.abspath(output_path)
    try:
        doc.save(abs_output_path)
        logger.info(f"DOCX generated successfully: {abs_output_path}")
        return abs_output_path
    except (IOError, PermissionError) as e:
        logger.error(f"Error saving DOCX file to {abs_output_path}: {e}")
        raise

def main() -> None:
    """Main function to parse arguments and generate the document."""
    parser = argparse.ArgumentParser(
        description="IDEAS Professional DOCX Generator — Convert Markdown to branded Word document",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--input", "-i", type=str, help="Input Markdown file path (stdin if omitted)")
    parser.add_argument("--output", "-o", type=str, default="output.docx", help="Output DOCX file path")
    parser.add_argument("--title", "-t", type=str, default="Dokumen IDEAS", help="Document title")
    parser.add_argument("--subtitle", "-s", type=str, default="", help="Document subtitle")
    parser.add_argument("--client", "-c", type=str, default="", help="Client name")
    parser.add_argument("--date", "-d", type=str, default="", help="Document date (e.g., '20 Februari 2026')")
    parser.add_argument("--doc-number", type=str, default="", help="Document reference number")
    parser.add_argument("--no-cover", action="store_true", help="Skip cover page generation")
    parser.add_argument("--landscape", action="store_true", help="Set page orientation to landscape")

    args = parser.parse_args()

    md_text = ""
    if args.input:
        try:
            input_path = Path(args.input)
            if not input_path.exists():
                logger.error(f"Input file not found: {args.input}")
                sys.exit(1)
            md_text = input_path.read_text(encoding="utf-8")
        except (IOError, UnicodeDecodeError) as e:
            logger.error(f"Error reading input file {args.input}: {e}")
            sys.exit(1)
    elif not sys.stdin.isatty():
        md_text = sys.stdin.read()
    else:
        parser.print_help(sys.stderr)
        logger.error("No input provided. Use --input or pipe from stdin.")
        sys.exit(1)

    try:
        generate_docx(
            input_text=md_text,
            output_path=args.output,
            title=args.title,
            subtitle=args.subtitle,
            client=args.client,
            doc_date=args.date,
            doc_number=args.doc_number,
            show_cover=not args.no_cover,
            landscape=args.landscape,
        )
    except Exception as e:
        logger.critical(f"An unexpected error occurred during DOCX generation: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
