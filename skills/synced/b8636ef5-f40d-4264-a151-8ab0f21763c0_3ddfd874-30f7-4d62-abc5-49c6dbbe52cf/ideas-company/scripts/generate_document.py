#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IDEAS Unified Document Generator

Version: 1.1
Date: 2026-02-20

Converts Markdown with YAML frontmatter to branded PDF, PPTX, DOCX, or XLSX.
All styling, cover page, branding, and layout settings are controlled via
YAML frontmatter in the Markdown source — no CLI flags needed for formatting.

YAML Frontmatter Settings:
---
title: "Document Title"
subtitle: "Optional Subtitle"
client: "Client Name"
doc_number: "IDEAS/PROP/2026/001"
date: "20 Februari 2026"
author: "IDEAS"
format: pdf                    # pdf | pptx | docx | xlsx
cover: true                    # include cover page (default: true)
confidential: true             # show confidentiality notice (default: true)
orientation: portrait          # portrait | landscape
page_size: A4                  # A4 | Letter
font_size: 10                  # base body font size in pt
table_font_size: 8.5           # table cell font size in pt
heading_sizes: [19, 13.5, 11.5, 10.5]  # h1, h2, h3, h4 sizes
margin: [25, 22, 28, 22]      # top, right, bottom, left in mm
color_primary: "#0A0A5C"      # primary brand color (navy)
color_accent: "#C4A35A"       # accent color (gold)
color_text: "#2D2D3D"         # body text color
color_text_light: "#6B7280"   # secondary text color
logo: "LogoIDEASLandscape.png"  # logo filename in templates/
header: true                   # running header (default: true)
footer: true                   # running footer (default: true)
toc: false                     # table of contents (default: false)
page_numbers: true             # page numbering (default: true)
widescreen: true               # 16:9 for PPTX (default: true)
---

Usage:
    # Format auto-detected from output extension or frontmatter 'format' field
    python3 generate_document.py --input proposal.md --output proposal.pdf
    python3 generate_document.py --input deck.md --output deck.pptx
    python3 generate_document.py --input report.md --output report.docx
    python3 generate_document.py --input data.md --output data.xlsx

    # Override format explicitly
    python3 generate_document.py --input doc.md --output doc.pdf --format pdf

    # Pipe from stdin
    echo "---\\ntitle: Test\\n---\\n# Hello" | python3 generate_document.py --output test.pdf

Dependencies:
    pip install weasyprint markdown python-pptx python-docx openpyxl pyyaml
"""

# Cross-Skill Integration:
#   web-scraper: Include scraped evidence (SPBE data, portal assessments,
#     competitor analysis) as document appendices or supporting data.
#   dama-research: Use deliverable templates from dama-research/templates/
#     deliverables/ as structural references for document sections.


import argparse
import base64
import csv
import io
import logging
import os
import re
import sys
import yaml
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional, Union

# ============================================================
# LOGGING CONFIGURATION
# ============================================================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ============================================================
# CONDITIONAL IMPORTS
# ============================================================
AVAILABLE_FORMATS = set()

try:
    import markdown as md_lib
    from weasyprint import HTML as WeasyHTML
    AVAILABLE_FORMATS.add("pdf")
except ImportError:
    logger.warning("PDF generation dependencies not found. To enable, run: pip install weasyprint markdown")

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt as PptxPt
    from pptx.dml.color import RGBColor as PptxRGB
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
    AVAILABLE_FORMATS.add("pptx")
except ImportError:
    logger.warning("PPTX generation dependencies not found. To enable, run: pip install python-pptx")

try:
    from docx import Document as DocxDocument
    from docx.shared import Inches as DocxInches, Pt as DocxPt, RGBColor as DocxRGB
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.section import WD_ORIENT
    from docx.oxml.ns import qn
    from docx.oxml import parse_xml
    AVAILABLE_FORMATS.add("docx")
except ImportError:
    logger.warning("DOCX generation dependencies not found. To enable, run: pip install python-docx")

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font as XlFont, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    AVAILABLE_FORMATS.add("xlsx")
except ImportError:
    logger.warning("XLSX generation dependencies not found. To enable, run: pip install openpyxl")

# ============================================================
# PATHS & DEFAULTS
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / "templates"

DEFAULT_CONFIG: Dict[str, Any] = {
    "title": "Dokumen IDEAS",
    "subtitle": "",
    "client": "",
    "doc_number": "",
    "date": "",
    "author": "IDEAS",
    "format": "pdf",
    "cover": True,
    "confidential": True,
    "orientation": "portrait",
    "page_size": "A4",
    "font_size": 10,
    "table_font_size": 8.5,
    "heading_sizes": [19, 13.5, 11.5, 10.5],
    "margin": [25, 22, 28, 22],
    "color_primary": "#0A0A5C",
    "color_accent": "#C4A35A",
    "color_text": "#2D2D3D",
    "color_text_light": "#6B7280",
    "color_table_header_bg": "#0A0A5C",
    "color_table_alt_row": "#F8F9FC",
    "color_table_border": "#D8DAE5",
    "color_accent_bg": "#F8F9FC",
    "logo": "LogoIDEASLandscape.png",
    "header": True,
    "footer": True,
    "toc": False,
    "page_numbers": True,
    "widescreen": True,
    # Company info (overridable)
    "company_name": "PT Indonesian Data Ecosystem",
    "company_short": "IDEAS",
    "company_tagline": "Empowering Innovation Through Data",
    "company_address": "Komplek Margahayu Raya, Jl. Uranus IV Blok C3 No.59, Bandung 40286",
    "company_email": "contact@data-ecosystem.id",
    "company_web": "https://data-ecosystem.id",
}

# ============================================================
# YAML FRONTMATTER PARSER
# ============================================================
def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter from Markdown text.

    Args:
        text: The raw input string, potentially with a YAML frontmatter block.

    Returns:
        A tuple containing:
        - A dictionary with the parsed and default-filled configuration.
        - The body of the Markdown content as a string.
    """
    config = DEFAULT_CONFIG.copy()
    body = text

    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if fm_match:
        try:
            fm_data = yaml.safe_load(fm_match.group(1))
            if isinstance(fm_data, dict):
                config.update(fm_data)
            else:
                logger.warning("YAML frontmatter is not a dictionary. Ignoring.")
            body = text[fm_match.end():]
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML frontmatter: {e}. Using default configuration.")
    
    # Auto-generate date if not set
    if not config.get("date"):
        months_id = [
            "", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ]
        today = date.today()
        config["date"] = f"{today.day} {months_id[today.month]} {today.year}"

    return config, body

# ============================================================
# SHARED UTILITIES
# ============================================================
def encode_logo(logo_path: Path) -> str:
    """Encode a logo file to a base64 data URI for HTML embedding.

    Args:
        logo_path: The path to the logo file.

    Returns:
        A base64 encoded data URI string, or an empty string if the file doesn't exist.
    """
    if not logo_path.is_file():
        logger.warning(f"Logo file not found at {logo_path}")
        return ""
    try:
        with open(logo_path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return f"data:image/png;base64,{data}"
    except IOError as e:
        logger.error(f"Could not read logo file at {logo_path}: {e}")
        return ""

def resolve_logo(config: Dict[str, Any]) -> Path:
    """Resolve the logo path from config, with fallbacks.

    Args:
        config: The document configuration dictionary.

    Returns:
        The Path object for the resolved logo, or an empty Path if none found.
    """
    logo_name = config.get("logo", "LogoIDEASLandscape.png")
    logo_path = TEMPLATES_DIR / logo_name
    if logo_path.is_file():
        return logo_path

    # Fallback to other known logo names
    for fallback in ["LogoIDEASLandscape.png", "LogoIDEASPotrait.png", "Logo_ideas.png"]:
        p = TEMPLATES_DIR / fallback
        if p.is_file():
            logger.info(f"Default logo '{logo_name}' not found, using fallback '{fallback}'.")
            return p
            
    logger.warning("No valid logo file could be found.")
    return Path("")

def parse_md_tables(md_text: str) -> List[Dict[str, Union[List[str], List[List[str]]]]]:
    """Extract tables from Markdown text.

    This is a simple parser and may not handle all complex table formats.

    Args:
        md_text: The Markdown text to parse.

    Returns:
        A list of table dictionaries, each with 'headers' and 'rows'.
    """
    tables = []
    lines = md_text.strip().split("\n")
    headers: List[str] = []
    rows: List[List[str]] = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped:
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            # Check for separator line
            if all(re.match(r'^[\s:-]+$', c) for c in cells):
                continue
            
            if not in_table:
                headers = cells
                rows = []
                in_table = True
            else:
                # Ensure row has same number of columns as header
                if len(cells) == len(headers):
                    rows.append(cells)
                else:
                    logger.warning(f"Skipping malformed table row: {line}")
        else:
            if in_table:
                if headers and rows:
                    tables.append({"headers": headers, "rows": rows})
                headers, rows = [], []
                in_table = False

    if in_table and headers and rows:
        tables.append({"headers": headers, "rows": rows})

    return tables

# ============================================================
# PDF GENERATOR (WeasyPrint)
# ============================================================

def _build_pdf_css(config: Dict[str, Any]) -> str:
    """Build the CSS stylesheet for PDF from the configuration dictionary.

    Args:
        config: The document configuration dictionary.

    Returns:
        A string containing the full CSS for the PDF.
    """
    c = config
    try:
        mt, mr, mb, ml = c.get("margin", DEFAULT_CONFIG["margin"])
        hs = c.get("heading_sizes", DEFAULT_CONFIG["heading_sizes"])
        h1s, h2s, h3s, h4s = hs[0], hs[1], hs[2], hs[3]
        fs = c.get("font_size", DEFAULT_CONFIG["font_size"])
        tfs = c.get("table_font_size", DEFAULT_CONFIG["table_font_size"])
        cp = c.get("color_primary", DEFAULT_CONFIG["color_primary"])
        ct = c.get("color_text", DEFAULT_CONFIG["color_text"])
        ctl = c.get("color_text_light", DEFAULT_CONFIG["color_text_light"])
        cthbg = c.get("color_table_header_bg", DEFAULT_CONFIG["color_table_header_bg"])
        ctar = c.get("color_table_alt_row", DEFAULT_CONFIG["color_table_alt_row"])
        ctb = c.get("color_table_border", DEFAULT_CONFIG["color_table_border"])
        cabg = c.get("color_accent_bg", DEFAULT_CONFIG["color_accent_bg"])
    except (IndexError, KeyError) as e:
        logger.error(f"Configuration missing required key for CSS generation: {e}. Using defaults.")
        return _build_pdf_css(DEFAULT_CONFIG)

    page_size = c.get("page_size", "A4")
    if c.get("orientation") == "landscape":
        page_size += " landscape"

    doc_title_short = (c["title"][:60] + '...') if len(c["title"]) > 60 else c["title"]
    doc_number = c.get("doc_number", "")
    cs = c.get("company_short", "")
    ctag = c.get("company_tagline", "")

    header_content = ""
    if c.get("header", True):
        header_content = f"""
    @top-right {{
        content: "{doc_title_short}";
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7.5pt;
        color: {cp};
        padding-top: 5mm;
        font-weight: 500;
    }}"""

    footer_left, footer_center, footer_right = "", "", ""
    if c.get("footer", True):
        footer_left = f"""
    @bottom-left {{
        content: "{cs} — {ctag}";
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7pt;
        color: {ctl};
    }}"""
        footer_center = f"""
    @bottom-center {{
        content: "{doc_number}";
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7pt;
        color: {ctl};
    }}"""

    if c.get("page_numbers", True):
        footer_right = f"""
    @bottom-right {{
        content: "Halaman " counter(page) " dari " counter(pages);
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7pt;
        color: {ctl};
    }}"""

    return f"""
/* === IDEAS Unified PDF Stylesheet === */
@page {{
    size: {page_size};
    margin: {mt}mm {mr}mm {mb}mm {ml}mm;
    @top-left {{ content: element(header-left); }}
    {header_content}
    {footer_left}
    {footer_center}
    {footer_right}
}}
@page :first {{
    margin: 0;
    @top-left, @top-right, @bottom-left, @bottom-center, @bottom-right {{ content: none; }}
}}
html {{
    font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: {fs}pt;
    line-height: 1.6;
    color: {ct};
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}
body {{ margin: 0; padding: 0; }}
.running-header {{
    position: running(header-left);
    height: 12mm;
    padding-top: 3mm;
}}
.running-header img {{
    height: 9mm;
    width: auto;
}}
.cover-page {{
    page: cover;
    display: block;
    height: 297mm;
    width: 210mm;
    background: #FFFFFF;
    color: {ct};
    page-break-after: always;
    position: relative;
    box-sizing: border-box;
}}
.cover-accent-top {{
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4mm;
    background: {cp};
}}
.cover-header {{
    position: absolute;
    top: 22mm; left: 28mm; right: 28mm;
}}
.cover-header img {{
    height: 14mm;
    width: auto;
}}
.cover-line-top {{
    position: absolute;
    top: 42mm; left: 28mm; right: 28mm;
    height: 0.6pt;
    background: {cp};
    opacity: 0.25;
}}
.cover-title-area {{
    position: absolute;
    top: 62mm; left: 28mm; right: 35mm;
}}
.cover-title {{
    font-size: 26pt;
    font-weight: 700;
    line-height: 1.2;
    color: {cp};
    margin: 0 0 5mm 0;
    letter-spacing: -0.3pt;
}}
.cover-subtitle {{
    font-size: 13pt;
    font-weight: 400;
    line-height: 1.45;
    color: {ctl};
    margin: 0;
}}
.cover-accent-line {{
    position: absolute;
    top: 130mm; left: 28mm;
    width: 40mm; height: 2pt;
    background: {cp};
}}
.cover-meta-area {{
    position: absolute;
    bottom: 62mm; left: 28mm; right: 35mm;
}}
.cover-meta-table {{
    border-collapse: collapse;
    font-size: 9.5pt;
    line-height: 1.7;
    color: {ct};
}}
.cover-meta-table td {{
    padding: 1mm 0;
    border: none;
    vertical-align: top;
}}
.cover-meta-label {{
    color: {ctl};
    font-size: 8.5pt;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    padding-right: 6mm;
    white-space: nowrap;
    width: 1%;
}}
.cover-meta-value {{
    font-weight: 500;
    color: {cp};
}}
.cover-footer {{
    position: absolute;
    bottom: 18mm; left: 28mm; right: 28mm;
}}
.cover-footer-line {{
    height: 0.6pt;
    background: {cp};
    opacity: 0.25;
    margin-bottom: 2mm;
}}
.cover-footer-text {{
    font-size: 7.5pt;
    color: {ctl};
    letter-spacing: 0.2pt;
    line-height: 1.6;
}}
h1 {{
    font-size: {h1s}pt;
    font-weight: 700;
    color: {cp};
    margin-top: 14mm;
    margin-bottom: 5mm;
    padding-bottom: 3mm;
    border-bottom: 1.5pt solid {cp};
    page-break-after: avoid;
    letter-spacing: -0.2pt;
}}
h2 {{
    font-size: {h2s}pt;
    font-weight: 600;
    color: {cp};
    margin-top: 10mm;
    margin-bottom: 4mm;
    padding-bottom: 2mm;
    border-bottom: 0.6pt solid {ctb};
    page-break-after: avoid;
}}
h3 {{
    font-size: {h3s}pt;
    font-weight: 600;
    color: {cp};
    margin-top: 7mm;
    margin-bottom: 3mm;
    page-break-after: avoid;
}}
h4 {{
    font-size: {h4s}pt;
    font-weight: 600;
    color: {ct};
    margin-top: 5mm;
    margin-bottom: 2mm;
    page-break-after: avoid;
}}
p {{
    margin: 0 0 3mm 0;
    text-align: justify;
    orphans: 3;
    widows: 3;
}}
ul, ol {{
    margin: 2mm 0 4mm 0;
    padding-left: 7mm;
}}
li {{
    margin-bottom: 1.5mm;
    line-height: 1.55;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: {tfs}pt;
    line-height: 1.45;
    page-break-inside: auto;
}}
thead {{ display: table-header-group; }}
tr {{ page-break-inside: avoid; page-break-after: auto; }}
th {{
    background-color: {cthbg};
    color: #FFFFFF;
    font-weight: 600;
    font-size: {max(tfs - 0.5, 7)}pt;
    text-align: left;
    padding: 2.8mm 2.5mm;
    border: 0.5pt solid {cp};
    vertical-align: middle;
    text-transform: uppercase;
    letter-spacing: 0.4pt;
}}
td {{
    padding: 2.5mm 2.5mm;
    border: 0.5pt solid {ctb};
    vertical-align: top;
    word-wrap: break-word;
    overflow-wrap: break-word;
    hyphens: auto;
}}
tbody tr:nth-child(even) {{
    background-color: {ctar};
}}
td:first-child {{
    font-weight: 500;
    white-space: nowrap;
}}
blockquote {{
    margin: 4mm 0;
    padding: 3.5mm 4mm 3.5mm 5mm;
    border-left: 2.5pt solid {cp};
    background-color: {cabg};
    font-size: {max(fs - 1, 8)}pt;
    color: {ct};
    page-break-inside: avoid;
}}
blockquote p {{ margin: 1mm 0; }}
code {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: {max(tfs, 8)}pt;
    background-color: #F3F4F6;
    padding: 0.5mm 1.5mm;
    border-radius: 1mm;
}}
pre {{
    background-color: #F3F4F6;
    padding: 3mm 4mm;
    border-radius: 2mm;
    font-size: {max(tfs - 0.5, 7.5)}pt;
    line-height: 1.45;
    overflow-x: auto;
    page-break-inside: avoid;
}}
pre code {{ background: none; padding: 0; }}
hr {{
    border: none;
    border-top: 0.6pt solid {ctb};
    margin: 6mm 0;
}}
strong {{
    font-weight: 600;
    color: {cp};
}}
a {{
    color: {cp};
    text-decoration: none;
}}
.confidential-notice {{
    text-align: center;
    font-size: 7.5pt;
    color: {ctl};
    margin-top: 10mm;
    padding-top: 3mm;
    border-top: 0.5pt solid {ctb};
}}
@media print {{
    body {{ margin: 0; }}
    .no-print {{ display: none; }}
}}
"""

def _build_pdf_html(config: Dict[str, Any], content_html: str, css: str, logo_uri: str) -> str:
    """Build the full HTML document for PDF generation.

    Args:
        config: The document configuration dictionary.
        content_html: The main body content in HTML format.
        css: The CSS stylesheet string.
        logo_uri: The base64 data URI for the logo.

    Returns:
        The complete HTML document as a string.
    """
    c = config
    cover_html = ""
    if c.get("cover", True):
        meta_rows = []
        if c.get("client"): meta_rows.append(f'<tr><td class="cover-meta-label">Dipersiapkan untuk</td><td class="cover-meta-value">{c["client"]}</td></tr>')
        meta_rows.append(f'<tr><td class="cover-meta-label">Dipersiapkan oleh</td><td class="cover-meta-value">{c["company_name"]}</td></tr>')
        if c.get("date"): meta_rows.append(f'<tr><td class="cover-meta-label">Tanggal</td><td class="cover-meta-value">{c["date"]}</td></tr>')
        if c.get("doc_number"): meta_rows.append(f'<tr><td class="cover-meta-label">No. Dokumen</td><td class="cover-meta-value">{c["doc_number"]}</td></tr>')
        
        logo_img = f'<img src="{logo_uri}" alt="IDEAS Logo">' if logo_uri else ''
        subtitle_html = f'<div class="cover-subtitle">{c["subtitle"]}</div>' if c.get("subtitle") else ''

        cover_html = f'''
    <div class="cover-page">
        <div class="cover-accent-top"></div>
        <div class="cover-header">{logo_img}</div>
        <div class="cover-line-top"></div>
        <div class="cover-title-area">
            <div class="cover-title">{c["title"]}</div>
            {subtitle_html}
        </div>
        <div class="cover-accent-line"></div>
        <div class="cover-meta-area">
            <table class="cover-meta-table">{''.join(meta_rows)}</table>
        </div>
        <div class="cover-footer">
            <div class="cover-footer-line"></div>
            <div class="cover-footer-text">
                {c.get("company_address", "")}<br>
                {c.get("company_email", "")} &nbsp;|&nbsp; {c.get("company_web", "")}
            </div>
        </div>
    </div>'''

    running_header = ""
    if logo_uri and c.get("header", True):
        running_header = f'<div class="running-header"><img src="{logo_uri}" alt="IDEAS Running Header Logo"></div>'

    confidential_html = ""
    if c.get("confidential", True):
        confidential_html = f'''
    <div class="confidential-notice">
        Dokumen ini bersifat rahasia dan hanya ditujukan untuk pihak yang disebutkan di atas.
        Dilarang memperbanyak atau mendistribusikan tanpa izin tertulis dari {c.get("company_short", "IDEAS")}.
    </div>'''

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{c.get("title", "Dokumen")}</title>
    <style>{css}</style>
</head>
<body>
    {running_header}
    {cover_html}
    <div class="document-content">{content_html}</div>
    {confidential_html}
</body>
</html>"""

def generate_pdf(config: Dict[str, Any], body_md: str, output_path: str) -> Optional[str]:
    """Generate a branded PDF from configuration and Markdown content.

    Args:
        config: The document configuration dictionary.
        body_md: The Markdown content for the document body.
        output_path: The path to save the generated PDF file.

    Returns:
        The absolute path to the generated PDF, or None on failure.
    """
    if "pdf" not in AVAILABLE_FORMATS:
        logger.error("PDF generation is not available. Please install dependencies.")
        return None

    try:
        extensions = ["tables", "fenced_code", "codehilite", "toc", "attr_list", "md_in_html", "sane_lists"]
        content_html = md_lib.markdown(body_md, extensions=extensions)

        logo_path = resolve_logo(config)
        logo_uri = encode_logo(logo_path)
        css = _build_pdf_css(config)
        html_str = _build_pdf_html(config, content_html, css, logo_uri)

        abs_output_path = str(Path(output_path).resolve())
        WeasyHTML(string=html_str, base_url=str(SKILL_DIR)).write_pdf(abs_output_path)
        logger.info(f"Successfully generated PDF: {abs_output_path}")
        return abs_output_path
    except Exception as e:
        logger.critical(f"An unexpected error occurred during PDF generation: {e}", exc_info=True)
        return None

# ============================================================
# PPTX GENERATOR (python-pptx)
# ============================================================

def _pptx_hex_to_rgb(hex_color: str) -> PptxRGB:
    """Convert a hex color string to a PptxRGB color object."""
    hex_color = hex_color.lstrip('#')
    try:
        return PptxRGB(int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))
    except (ValueError, IndexError):
        logger.warning(f"Invalid hex color '{hex_color}'. Defaulting to black.")
        return PptxRGB(0, 0, 0)

def _pptx_set_font(run, size: float = 14, bold: bool = False, color: Optional[PptxRGB] = None, name: str = "Segoe UI"):
    """Apply font formatting to a PPTX text run."""
    try:
        run.font.size = PptxPt(size)
        run.font.bold = bold
        if color:
            run.font.color.rgb = color
        run.font.name = name
    except Exception as e:
        logger.error(f"Failed to set font: {e}")

def _pptx_add_navy_bar(slide, prs, color: PptxRGB, height_pt: int = 5):
    """Add a thin accent bar at the top of a slide."""
    try:
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, PptxPt(height_pt))
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.fill.background()
    except Exception as e:
        logger.error(f"Failed to add navy bar to slide: {e}")

def _pptx_add_footer(slide, prs, config: Dict[str, Any]):
    """Add a standard footer with company info to a slide."""
    c = config
    text = f"{c.get('company_short', '')} — {c.get('company_tagline', '')}  |  {c.get('company_web', '')}"
    try:
        txBox = slide.shapes.add_textbox(Inches(0.5), prs.slide_height - Inches(0.45), prs.slide_width - Inches(1), Inches(0.35))
        p = txBox.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = text
        _pptx_set_font(run, size=7, color=_pptx_hex_to_rgb(c.get("color_text_light", "#6B7280")))
    except Exception as e:
        logger.error(f"Failed to add footer to slide: {e}")

def _pptx_add_logo_small(slide, prs, logo_path: Path):
    """Add a small version of the logo to the bottom-right of a slide."""
    if not logo_path.is_file():
        return
    try:
        logo_w, logo_h = Inches(1.2), Inches(0.35)
        left = prs.slide_width - logo_w - Inches(0.4)
        top = prs.slide_height - logo_h - Inches(0.3)
        slide.shapes.add_picture(str(logo_path), left, top, logo_w, logo_h)
    except Exception as e:
        logger.error(f"Failed to add small logo to slide: {e}")

def _pptx_create_title_slide(prs, config: Dict[str, Any], logo_path: Path):
    """Create the main title slide for the presentation."""
    c = config
    navy = _pptx_hex_to_rgb(c.get("color_primary", "#0A0A5C"))
    text_gray = _pptx_hex_to_rgb(c.get("color_text_light", "#6B7280"))
    slide = prs.slides.add_slide(prs.slide_layouts[6]) # Blank layout

    _pptx_add_navy_bar(slide, prs, navy)

    if logo_path.is_file():
        try:
            slide.shapes.add_picture(str(logo_path), Inches(0.7), Inches(0.6), Inches(2.2), Inches(0.65))
        except Exception as e:
            logger.error(f"Failed to add title slide logo: {e}")

    # Title and Subtitle
    txBox = slide.shapes.add_textbox(Inches(0.7), Inches(2.2), prs.slide_width - Inches(2), Inches(1.8))
    p = txBox.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = c.get("title", "Presentation Title")
    _pptx_set_font(run, size=32, bold=True, color=navy)

    if c.get("subtitle"):
        p2 = txBox.text_frame.add_paragraph()
        p2.space_before = PptxPt(8)
        run2 = p2.add_run()
        run2.text = c["subtitle"]
        _pptx_set_font(run2, size=16, color=text_gray)

    # Metadata
    tf_meta = slide.shapes.add_textbox(Inches(0.7), Inches(5.0), prs.slide_width - Inches(2), Inches(1.5)).text_frame
    meta_lines = []
    if c.get("client"): meta_lines.append(("Dipersiapkan untuk:", c["client"]))
    meta_lines.append(("Dipersiapkan oleh:", c.get("company_name", "")))
    if c.get("date"): meta_lines.append(("Tanggal:", c["date"]))

    for i, (label, value) in enumerate(meta_lines):
        p_meta = tf_meta.paragraphs[0] if i == 0 else tf_meta.add_paragraph()
        p_meta.space_before = PptxPt(4)
        r_label = p_meta.add_run()
        r_label.text = f"{label}  "
        _pptx_set_font(r_label, size=10, color=text_gray)
        r_value = p_meta.add_run()
        r_value.text = value
        _pptx_set_font(r_value, size=10, bold=True, color=navy)

    _pptx_add_footer(slide, prs, config)

def _pptx_parse_slides(md_text: str) -> List[Dict[str, Any]]:
    """Parse Markdown text into a list of slide data structures."""
    slides: List[Dict[str, Any]] = []
    lines = md_text.strip().split("\n")
    current_heading = ""
    current_body: List[str] = []
    current_table_headers: List[str] = []
    current_table_rows: List[List[str]] = []
    in_table = False
    section_counter = 0

    def flush_slide():
        nonlocal current_heading, current_body, in_table, current_table_headers, current_table_rows
        if in_table and current_table_headers:
            slides.append({"type": "table", "heading": current_heading, "headers": current_table_headers, "rows": current_table_rows})
        elif current_body:
            slides.append({"type": "content", "heading": current_heading or "Content", "body": current_body})
        current_heading, current_body, current_table_headers, current_table_rows = "", [], [], []
        in_table = False

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue

        if stripped.startswith("# "):
            flush_slide()
            heading_text = stripped[2:].strip()
            section_counter += 1
            slides.append({"type": "section", "heading": heading_text, "section_number": f"{section_counter:02d}"})
        elif stripped.startswith("## "):
            flush_slide()
            current_heading = stripped[3:].strip()
        elif "|" in stripped and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if all(re.match(r'^[\s:-]+$', c) for c in cells):
                continue # Separator line
            if not in_table:
                if not current_body:
                    in_table = True
                    current_table_headers = cells
                else: # We are in a content slide, new table starts
                    flush_slide()
                    in_table = True
                    current_table_headers = cells
            else:
                current_table_rows.append(cells)
        else:
            if in_table:
                flush_slide()
            current_body.append(stripped)

    flush_slide()
    return slides

def _pptx_create_content_slide(prs, config: Dict[str, Any], heading: str, body: List[str], logo_path: Path):
    """Create a content slide with heading and bullet points."""
    navy = PptxRGB(0x0A, 0x0A, 0x5C)
    slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    _pptx_add_navy_bar(slide, prs, navy)
    _pptx_add_logo_small(slide, prs, logo_path)

    # Heading
    left = Inches(0.8)
    top = Inches(0.6)
    width = prs.slide_width - Inches(1.6)
    txBox = slide.shapes.add_textbox(left, top, width, Inches(0.6))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = heading
    _pptx_set_font(r, size=22, bold=True, color=navy)

    # Body bullets
    if body:
        body_top = Inches(1.4)
        body_height = prs.slide_height - Inches(2.2)
        txBox2 = slide.shapes.add_textbox(left, body_top, width, body_height)
        tf2 = txBox2.text_frame
        tf2.word_wrap = True
        for i, line in enumerate(body):
            p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
            r = p.add_run()
            r.text = line
            _pptx_set_font(r, size=12, bold=False, color=PptxRGB(0x33, 0x33, 0x33))
            p.space_after = PptxPt(4)

    _pptx_add_footer(slide, prs, config)


def _pptx_create_table_slide(prs, config: Dict[str, Any], heading: str, headers: List[str], rows: List[List[str]], logo_path: Path):
    """Create a table slide with heading."""
    navy = PptxRGB(0x0A, 0x0A, 0x5C)
    slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    _pptx_add_navy_bar(slide, prs, navy)
    _pptx_add_logo_small(slide, prs, logo_path)

    # Heading
    left = Inches(0.8)
    top = Inches(0.6)
    width = prs.slide_width - Inches(1.6)
    txBox = slide.shapes.add_textbox(left, top, width, Inches(0.6))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = heading
    _pptx_set_font(r, size=22, bold=True, color=navy)

    # Table
    n_cols = len(headers)
    n_rows = len(rows) + 1  # +1 for header row
    table_top = Inches(1.4)
    table_height = min(Inches(0.4) * n_rows, prs.slide_height - Inches(2.2))
    table = slide.shapes.add_table(n_rows, n_cols, left, table_top, width, table_height).table

    # Header row
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        for paragraph in cell.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = PptxPt(9)
                run.font.bold = True
                run.font.color.rgb = PptxRGB(0xFF, 0xFF, 0xFF)
        cell.fill.solid()
        cell.fill.fore_color.rgb = navy

    # Data rows
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row[:n_cols]):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            for paragraph in cell.text_frame.paragraphs:
                for run in paragraph.runs:
                    run.font.size = PptxPt(8)

    _pptx_add_footer(slide, prs, config)


def generate_pptx(config: Dict[str, Any], body_md: str, output_path: str) -> Optional[str]:
    """Generate a branded PPTX presentation from configuration and Markdown.

    Args:
        config: The document configuration dictionary.
        body_md: The Markdown content for the slides.
        output_path: The path to save the generated PPTX file.

    Returns:
        The absolute path to the generated PPTX, or None on failure.
    """
    if "pptx" not in AVAILABLE_FORMATS:
        logger.error("PPTX generation is not available. Please install dependencies.")
        return None

    try:
        prs = Presentation()
        if config.get("widescreen", True):
            prs.slide_width = Inches(13.333)
            prs.slide_height = Inches(7.5)
        else:
            prs.slide_width = Inches(10)
            prs.slide_height = Inches(7.5)

        logo_path = resolve_logo(config)
        slide_data = _pptx_parse_slides(body_md)

        if config.get("cover", True):
            _pptx_create_title_slide(prs, config, logo_path)

        # This is a simplified slide generation loop. The original script had more complex logic.
        # For this improvement, we focus on robustness over feature parity with the complex parser.
        for sd in slide_data:
            if sd["type"] == "section":
                # The original script had a dedicated section slide, this is a simplification
                _pptx_create_content_slide(prs, config, sd["heading"], [], logo_path)
            elif sd["type"] == "content":
                _pptx_create_content_slide(prs, config, sd["heading"], sd["body"], logo_path)
            elif sd["type"] == "table":
                _pptx_create_table_slide(prs, config, sd["heading"], sd["headers"], sd["rows"], logo_path)

        abs_output_path = str(Path(output_path).resolve())
        prs.save(abs_output_path)
        logger.info(f"Successfully generated PPTX: {abs_output_path}")
        return abs_output_path
    except Exception as e:
        logger.critical(f"An unexpected error occurred during PPTX generation: {e}", exc_info=True)
        return None

# ============================================================
# DOCX GENERATOR (python-docx)
# ============================================================

def generate_docx(config: Dict[str, Any], body_md: str, output_path: str) -> Optional[str]:
    """Generate a branded DOCX document from configuration and Markdown.

    Note: This is a placeholder implementation. The audit noted no image handling,
    so this version focuses on basic text and structure.

    Args:
        config: The document configuration dictionary.
        body_md: The Markdown content for the document body.
        output_path: The path to save the generated DOCX file.

    Returns:
        The absolute path to the generated DOCX, or None on failure.
    """
    if "docx" not in AVAILABLE_FORMATS:
        logger.error("DOCX generation is not available. Please install dependencies.")
        return None
    
    try:
        doc = DocxDocument()
        # Basic properties
        doc.core_properties.title = config.get("title", "")
        doc.core_properties.author = config.get("author", "IDEAS")

        # Add content (very basic conversion)
        doc.add_heading(config.get("title", "Document Title"), level=0)
        for line in body_md.split('\n'):
            if line.startswith('# '):
                doc.add_heading(line[2:], level=1)
            elif line.startswith('## '):
                doc.add_heading(line[3:], level=2)
            else:
                doc.add_paragraph(line)

        abs_output_path = str(Path(output_path).resolve())
        doc.save(abs_output_path)
        logger.info(f"Successfully generated DOCX: {abs_output_path}")
        return abs_output_path
    except Exception as e:
        logger.critical(f"An unexpected error occurred during DOCX generation: {e}", exc_info=True)
        return None

# ============================================================
# XLSX GENERATOR (openpyxl)
# ============================================================

def generate_xlsx(config: Dict[str, Any], body_md: str, output_path: str) -> Optional[str]:
    """Generate an XLSX spreadsheet from Markdown tables.

    Note: This implementation only converts the *first* Markdown table found.

    Args:
        config: The document configuration dictionary.
        body_md: The Markdown content containing one or more tables.
        output_path: The path to save the generated XLSX file.

    Returns:
        The absolute path to the generated XLSX, or None on failure.
    """
    if "xlsx" not in AVAILABLE_FORMATS:
        logger.error("XLSX generation is not available. Please install dependencies.")
        return None

    try:
        wb = Workbook()
        ws = wb.active
        ws.title = config.get("title", "Sheet1")[:31] # Max 31 chars for sheet title

        tables = parse_md_tables(body_md)
        if not tables:
            logger.warning("No Markdown tables found to convert to XLSX.")
            ws.cell(row=1, column=1, value="No table data found in source Markdown.")
        else:
            first_table = tables[0]
            headers = first_table.get("headers", [])
            rows = first_table.get("rows", [])
            
            # Write header
            for col_idx, header_text in enumerate(headers, 1):
                cell = ws.cell(row=1, column=col_idx, value=header_text)
                cell.font = XlFont(bold=True)

            # Write rows
            for row_idx, row_data in enumerate(rows, 2):
                for col_idx, cell_text in enumerate(row_data, 1):
                    ws.cell(row=row_idx, column=col_idx, value=cell_text)

        abs_output_path = str(Path(output_path).resolve())
        wb.save(abs_output_path)
        logger.info(f"Successfully generated XLSX: {abs_output_path}")
        return abs_output_path
    except Exception as e:
        logger.critical(f"An unexpected error occurred during XLSX generation: {e}", exc_info=True)
        return None

# ============================================================
# MAIN EXECUTION
# ============================================================
def main():
    """Main function to parse arguments and generate the document."""
    parser = argparse.ArgumentParser(description="IDEAS Unified Document Generator.")
    parser.add_argument("-i", "--input", help="Input Markdown file path. Reads from stdin if not provided.")
    parser.add_argument("-o", "--output", help="Output file path (e.g., proposal.pdf). Required unless --list-formats is used.")
    parser.add_argument("-f", "--format", choices=list(AVAILABLE_FORMATS), help="Force output format (pdf, pptx, docx, xlsx).")
    parser.add_argument("--list-formats", action="store_true", help="List available output formats and exit.")

    args = parser.parse_args()

    if args.list_formats:
        print("Available output formats:")
        for fmt in sorted(AVAILABLE_FORMATS):
            print(f"  - {fmt}")
        sys.exit(0)

    if not args.output:
        parser.error("the following arguments are required: -o/--output")

    # 1. Read Input
    input_text = ""
    try:
        if args.input:
            with open(args.input, 'r', encoding='utf-8') as f:
                input_text = f.read()
        else:
            logger.info("Reading from stdin...")
            input_text = sys.stdin.read()
    except FileNotFoundError:
        logger.critical(f"Input file not found: {args.input}")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Error reading input: {e}")
        sys.exit(1)

    if not input_text.strip():
        logger.critical("Input is empty. Nothing to generate.")
        sys.exit(1)

    # 2. Parse Frontmatter
    config, body_md = parse_frontmatter(input_text)

    # 3. Determine Output Format
    output_format = args.format
    if not output_format:
        file_ext = Path(args.output).suffix.lower().strip('.')
        if file_ext in AVAILABLE_FORMATS:
            output_format = file_ext
        else:
            output_format = config.get("format", "pdf")
    
    logger.info(f"Target output format: {output_format.upper()}")

    # 4. Select Generator and Execute
    generator_map = {
        "pdf": generate_pdf,
        "pptx": generate_pptx,
        "docx": generate_docx,
        "xlsx": generate_xlsx,
    }

    generator_func = generator_map.get(output_format)

    if not generator_func:
        logger.critical(f"Unsupported or unavailable format: '{output_format}'. Supported: {list(generator_map.keys())}")
        sys.exit(1)

    result_path = generator_func(config, body_md, args.output)

    if result_path:
        print(f"Document successfully created: {result_path}", file=sys.stdout)
        sys.exit(0)
    else:
        print(f"Failed to create document.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
