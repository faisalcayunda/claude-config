#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: 1.1
# Last Modified: 2026-02-20
"""
IDEAS Professional PPTX Generator

Converts Markdown deck content to a branded PowerPoint presentation
with IDEAS visual identity (navy #0A0A5C, white, clean typography).

Features:
  - Title slide with IDEAS logo and navy accent
  - Section divider slides with navy background
  - Content slides with bullet points, tables, and images
  - Speaker notes support
  - Customizable closing slide
  - Consistent branding: navy headings, clean fonts
  - Auto-parses Markdown headings, lists, tables, blockquotes, and images

Usage:
    python3 generate_pptx.py --input deck.md --output deck.pptx \
        --title "Proposal Konsultansi Data" \
        --subtitle "Asesmen Kematangan Data" \
        --client "Pemerintah Provinsi Jawa Barat"

    python3 generate_pptx.py --input deck.md --output deck.pptx --widescreen

Dependencies:
    pip install python-pptx
"""

import argparse
import logging
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Union

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.slide import Slide
    from pptx.presentation import Presentation as PresentationObject
except ImportError as e:
    logger.error(f"Missing dependency: {e}. Please install it with 'pip install python-pptx'.")
    sys.exit(1)

# --- Constants ---
# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / "templates"
LOGO_LANDSCAPE = TEMPLATES_DIR / "LogoIDEASLandscape.png"
# Note: The filename is intentionally misspelled as 'Potrait' to match the actual file.
LOGO_PORTRAIT = TEMPLATES_DIR / "LogoIDEASPotrait.png"

# Branding
NAVY = RGBColor(0x0A, 0x0A, 0x5C)
NAVY_LIGHT = RGBColor(0x1A, 0x1A, 0x8C)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TEXT_DARK = RGBColor(0x2D, 0x2D, 0x3D)
TEXT_GRAY = RGBColor(0x6B, 0x72, 0x80)
ACCENT_BG = RGBColor(0xF8, 0xF9, 0xFC)
TABLE_BORDER = RGBColor(0xD8, 0xDA, 0xE5)

# Company Info
COMPANY_NAME = "PT Indonesian Data Ecosystem"
COMPANY_SHORT = "IDEAS"
COMPANY_TAGLINE = "Empowering Innovation Through Data"
COMPANY_WEB = "https://data-ecosystem.id"

# Slide Dimensions
WIDE_W, WIDE_H = Inches(13.333), Inches(7.5)
STD_W, STD_H = Inches(10), Inches(7.5)

# --- Helper Functions ---

def _set_font(run, size: int = 14, bold: bool = False, color: RGBColor = TEXT_DARK, name: str = "Segoe UI") -> None:
    """Apply font formatting to a text run."""
    try:
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
        run.font.name = name
    except Exception as e:
        logger.warning(f"Could not set font properties: {e}")

def _add_navy_bar(slide: Slide, prs: PresentationObject, height_pt: int = 6) -> None:
    """Add a thin navy accent bar at the top of a slide."""
    try:
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Pt(height_pt))
        shape.fill.solid()
        shape.fill.fore_color.rgb = NAVY
        shape.line.fill.background()
    except Exception as e:
        logger.warning(f"Could not add navy bar: {e}")

def _add_footer(slide: Slide, prs: PresentationObject, text: Optional[str] = None) -> None:
    """Add a subtle footer with company info."""
    if text is None:
        text = f"{COMPANY_SHORT} — {COMPANY_TAGLINE}  |  {COMPANY_WEB}"
    try:
        txBox = slide.shapes.add_textbox(Inches(0.5), prs.slide_height - Inches(0.45), prs.slide_width - Inches(1), Inches(0.35))
        p = txBox.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = text
        _set_font(run, size=7, color=TEXT_GRAY)
    except Exception as e:
        logger.warning(f"Could not add footer: {e}"
        )

def _add_logo_small(slide: Slide, prs: PresentationObject) -> None:
    """Add a small logo at the bottom-right of a slide."""
    if not LOGO_LANDSCAPE.exists():
        logger.warning(f"Small logo not found at {LOGO_LANDSCAPE}, skipping.")
        return
    try:
        logo_w, logo_h = Inches(1.2), Inches(0.35)
        left = prs.slide_width - logo_w - Inches(0.4)
        top = prs.slide_height - logo_h - Inches(0.3)
        slide.shapes.add_picture(str(LOGO_LANDSCAPE), left, top, logo_w, logo_h)
    except Exception as e:
        logger.warning(f"Could not add small logo: {e}")

# --- Slide Creation Functions ---

def create_title_slide(prs: PresentationObject, title: str, subtitle: str = "", client: str = "", doc_date: str = "") -> Slide:
    """Create an elegant minimalist title slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    _add_navy_bar(slide, prs, height_pt=5)

    if LOGO_LANDSCAPE.exists():
        slide.shapes.add_picture(str(LOGO_LANDSCAPE), Inches(0.7), Inches(0.6), Inches(2.2), Inches(0.65))
    else:
        logger.warning(f"Title slide logo not found at {LOGO_LANDSCAPE}")

    # Title and metadata logic...
    # (Rest of the function remains largely the same but with added try/except blocks if needed)
    # For brevity, the original robust logic is maintained.
    w = prs.slide_width
    line_shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45),
        w - Inches(1.4), Pt(0.8)
    )
    line_shape.fill.solid()
    line_shape.fill.fore_color.rgb = RGBColor(0xD8, 0xDA, 0xE5)
    line_shape.line.fill.background()

    txBox = slide.shapes.add_textbox(Inches(0.7), Inches(2.2), w - Inches(2), Inches(1.8))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title
    _set_font(run, size=32, bold=True, color=NAVY)

    if subtitle:
        p2 = tf.add_paragraph()
        p2.space_before = Pt(8)
        run2 = p2.add_run()
        run2.text = subtitle
        _set_font(run2, size=16, color=TEXT_GRAY)

    meta_box = slide.shapes.add_textbox(Inches(0.7), Inches(5.0), w - Inches(2), Inches(1.5))
    tf_meta = meta_box.text_frame
    meta_lines = []
    if client: meta_lines.append(f"Dipersiapkan untuk:  {client}")
    meta_lines.append(f"Dipersiapkan oleh:  {COMPANY_NAME}")
    if doc_date: meta_lines.append(f"Tanggal:  {doc_date}")

    for i, line in enumerate(meta_lines):
        p = tf_meta.paragraphs[0] if i == 0 else tf_meta.add_paragraph()
        parts = line.split(":  ", 1)
        if len(parts) == 2:
            r_label = p.add_run()
            r_label.text = parts[0] + ":  "
            _set_font(r_label, size=10, color=TEXT_GRAY)
            r_value = p.add_run()
            r_value.text = parts[1]
            _set_font(r_value, size=10, bold=True, color=NAVY)
        else:
            r = p.add_run()
            r.text = line
            _set_font(r, size=10, color=TEXT_DARK)

    _add_footer(slide, prs)
    return slide

def create_section_slide(prs: PresentationObject, section_title: str, section_number: str = "") -> Slide:
    """Create a section divider slide with a navy background."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = NAVY
    bg.line.fill.background()

    title_top = Inches(3.2) if section_number else Inches(2.8)
    if section_number:
        num_box = slide.shapes.add_textbox(Inches(0.7), Inches(2.2), Inches(2), Inches(0.8))
        r_num = num_box.text_frame.paragraphs[0].add_run()
        r_num.text = section_number
        _set_font(r_num, size=48, bold=True, color=WHITE)

    title_box = slide.shapes.add_textbox(Inches(0.7), title_top, prs.slide_width - Inches(2), Inches(1.5))
    r_title = title_box.text_frame.paragraphs[0].add_run()
    r_title.text = _strip_md(section_title)
    _set_font(r_title, size=28, bold=True, color=WHITE)

    return slide

def _strip_md(text: str) -> str:
    """Strip markdown formatting markers from text for plain display."""
    import re as _re
    text = _re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)   # bold+italic
    text = _re.sub(r'\*\*(.+?)\*\*', r'\1', text)         # bold
    text = _re.sub(r'\*(.+?)\*', r'\1', text)             # italic
    text = _re.sub(r'`(.+?)`', r'\1', text)               # code
    return text


def _add_md_runs(paragraph, text: str, base_size: int = 12, base_color=None):
    """Parse markdown inline formatting and add properly styled runs to a paragraph.
    
    Handles **bold**, *italic*, ***bold+italic***, and `code`.
    """
    import re as _re
    if base_color is None:
        base_color = TEXT_DARK

    # Split on formatting markers, keeping the delimiters
    parts = _re.split(r'(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*|`.+?`)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith("***") and part.endswith("***"):
            run = paragraph.add_run()
            run.text = part[3:-3]
            _set_font(run, size=base_size, bold=True, color=base_color)
            run.font.italic = True
        elif part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run()
            run.text = part[2:-2]
            _set_font(run, size=base_size, bold=True, color=base_color)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = paragraph.add_run()
            run.text = part[1:-1]
            _set_font(run, size=base_size, color=base_color)
            run.font.italic = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run()
            run.text = part[1:-1]
            _set_font(run, size=base_size - 1, color=RGBColor(0x4A, 0x4A, 0x4A), name="Consolas")
        else:
            run = paragraph.add_run()
            run.text = part
            _set_font(run, size=base_size, color=base_color)


def create_content_slide(prs: PresentationObject, heading: str, body_items: List[Dict[str, str]]) -> Slide:
    """Create a content slide with heading, text, and images.
    
    Properly handles markdown formatting: **bold**, *italic*, bullet lists.
    """
    import re as _re
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _add_navy_bar(slide, prs, height_pt=4)

    h_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), prs.slide_width - Inches(1.4), Inches(0.8))
    r_h = h_box.text_frame.paragraphs[0].add_run()
    r_h.text = _strip_md(heading)
    _set_font(r_h, size=22, bold=True, color=NAVY)

    body_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.6), prs.slide_width - Inches(1.4), prs.slide_height - Inches(2.5))
    tf_body = body_box.text_frame
    tf_body.word_wrap = True

    for i, item in enumerate(body_items):
        p = tf_body.paragraphs[0] if i == 0 else tf_body.add_paragraph()
        p.space_before = Pt(4)
        p.space_after = Pt(2)

        if item['type'] == 'text':
            content = item['content']

            # Detect bullet/numbered list
            is_bullet = content.startswith(("- ", "* "))
            num_match = _re.match(r'^(\d+)\.\s+', content)

            if is_bullet:
                content = content.lstrip("-* ")
                p.level = 1
                p.space_before = Pt(2)
                bullet_run = p.add_run()
                bullet_run.text = "• "
                _set_font(bullet_run, size=11, color=NAVY, bold=True)
                _add_md_runs(p, content, base_size=11)
            elif num_match:
                num = num_match.group(1)
                content = _re.sub(r'^\d+\.\s+', '', content)
                p.level = 1
                p.space_before = Pt(2)
                num_run = p.add_run()
                num_run.text = f"{num}. "
                _set_font(num_run, size=11, color=NAVY, bold=True)
                _add_md_runs(p, content, base_size=11)
            else:
                _add_md_runs(p, content, base_size=12)

        elif item['type'] == 'image':
            try:
                img_path = item['path']
                if not Path(img_path).exists():
                    logger.warning(f"Image not found at path: {img_path}")
                    continue
                slide.shapes.add_picture(img_path, Inches(1), Inches(2.5), height=Inches(3))
            except Exception as e:
                logger.error(f"Failed to add image {item['path']}: {e}")

    _add_footer(slide, prs)
    _add_logo_small(slide, prs)
    return slide

def create_table_slide(prs: PresentationObject, heading: str, headers: List[str], rows: List[List[str]]) -> Slide:
    """Create a slide with a formatted table."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _add_navy_bar(slide, prs, height_pt=4)

    # Heading
    h_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), prs.slide_width - Inches(1.4), Inches(0.8))
    r_h = h_box.text_frame.paragraphs[0].add_run()
    r_h.text = heading
    _set_font(r_h, size=22, bold=True, color=NAVY)

    # Table
    n_rows, n_cols = len(rows) + 1, len(headers)
    try:
        table_shape = slide.shapes.add_table(n_rows, n_cols, Inches(0.7), Inches(1.5), prs.slide_width - Inches(1.4), Inches(0.35) * n_rows)
        table = table_shape.table
        # Header
        for j, header in enumerate(headers):
            cell = table.cell(0, j)
            cell.text = _strip_md(header)
            cell.fill.solid()
            cell.fill.fore_color.rgb = NAVY
            _set_font(cell.text_frame.paragraphs[0].runs[0], size=9, bold=True, color=WHITE)
        # Rows
        for i, row_data in enumerate(rows):
            for j, cell_text in enumerate(row_data):
                cell = table.cell(i + 1, j)
                cell.text = _strip_md(cell_text)
                if i % 2 == 1: 
                    cell.fill.solid()
                    cell.fill.fore_color.rgb = ACCENT_BG
                _set_font(cell.text_frame.paragraphs[0].runs[0], size=9, color=TEXT_DARK)
    except Exception as e:
        logger.error(f"Failed to create table '{heading}': {e}")

    _add_footer(slide, prs)
    _add_logo_small(slide, prs)
    return slide

def create_closing_slide(prs: PresentationObject, content: Optional[List[str]] = None) -> Slide:
    """Create a customizable thank-you closing slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = NAVY
    bg.line.fill.background()

    if content:
        tx = slide.shapes.add_textbox(Inches(0.7), Inches(2.5), prs.slide_width - Inches(1.4), Inches(3.0))
        tf = tx.text_frame
        for i, line in enumerate(content):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = line
            size = 36 if i == 0 else 14
            color = WHITE if i == 0 else RGBColor(0xA0, 0xA0, 0xD0)
            _set_font(r, size=size, bold=(i==0), color=color)
    else: # Default closing slide
        tx = slide.shapes.add_textbox(Inches(0.7), Inches(2.5), prs.slide_width - Inches(1.4), Inches(1.5))
        p = tx.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = "TERIMA KASIH"
        _set_font(r, size=36, bold=True, color=WHITE)

    if LOGO_LANDSCAPE.exists():
        slide.shapes.add_picture(str(LOGO_LANDSCAPE), (prs.slide_width - Inches(2.0)) / 2, Inches(1.5), Inches(2.0), Inches(0.6))

    return slide

# --- Markdown Parsing ---

def parse_markdown_to_slides(md_text: str) -> List[Dict[str, Any]]:
    """Parse Markdown text into a list of slide data structures."""
    slides = []
    lines = md_text.strip().split("\n")
    current_slide = None

    def flush_slide():
        nonlocal current_slide
        if current_slide:
            slides.append(current_slide)
            current_slide = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue

        # Headings create new slides
        if stripped.startswith("#"):
            flush_slide()
            if stripped.startswith("## "):
                current_slide = {"type": "section", "heading": stripped[3:].strip(), "body": []}
            elif stripped.startswith("### "):
                current_slide = {"type": "content", "heading": stripped[4:].strip(), "body": []}
            elif stripped.startswith("# "):
                 current_slide = {"type": "section", "heading": stripped[2:].strip(), "body": []}
            continue

        # Image tag
        img_match = re.match(r'!\S+\[(.*?)\]\((.*?)\)', stripped)
        if img_match:
            if not current_slide: current_slide = {"type": "content", "heading": "", "body": []}
            current_slide['body'].append({'type': 'image', 'alt': img_match.group(1), 'path': img_match.group(2)})
            continue

        # Speaker Notes
        if stripped.lower().startswith("notes:"):
            if current_slide:
                current_slide.setdefault('notes', []).append(stripped[6:].strip())
            continue

        # Table
        if stripped.startswith("|"):
            # Simplified table parsing
            if not current_slide or current_slide['type'] != 'table':
                flush_slide()
                current_slide = {"type": "table", "heading": slides[-1]['heading'] if slides else "", "headers": [], "rows": []}
            
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if not current_slide['headers']:
                current_slide['headers'] = cells
            elif not all(re.match(r'[-:]+$', c) for c in cells):
                current_slide['rows'].append(cells)
            continue

        # Closing slide
        if stripped.upper() in ("TERIMA KASIH", "THANK YOU"):
            flush_slide()
            current_slide = {"type": "closing", "content": [stripped]}
            continue

        # Body content
        if not current_slide:
            current_slide = {"type": "content", "heading": "", "body": []}
        if 'body' in current_slide:
            current_slide['body'].append({'type': 'text', 'content': stripped})
        elif current_slide.get('type') == 'closing':
            current_slide.setdefault('content', []).append(stripped)

    flush_slide()
    return slides

# --- Main Generator Function ---

def generate_pptx(
    input_text: str,
    output_path: str,
    title: str = "Dokumen IDEAS",
    subtitle: str = "",
    client: str = "",
    doc_date: str = "",
    widescreen: bool = True,
) -> Optional[str]:
    """
    Generate a branded PPTX from Markdown text.
    Returns the absolute path to the generated file or None on failure.
    """
    try:
        prs = Presentation()
        prs.slide_width = WIDE_W if widescreen else STD_W
        prs.slide_height = WIDE_H if widescreen else STD_H

        if not doc_date:
            months_id = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
            today = date.today()
            doc_date = f"{today.day} {months_id[today.month]} {today.year}"

        create_title_slide(prs, title, subtitle, client, doc_date)

        slide_data = parse_markdown_to_slides(input_text)

        for sd in slide_data:
            slide_type = sd.get("type")
            if slide_type == "section":
                create_section_slide(prs, sd["heading"], sd.get("section_number", ""))
            elif slide_type == "content":
                create_content_slide(prs, sd["heading"], sd["body"])
            elif slide_type == "table":
                create_table_slide(prs, sd["heading"], sd["headers"], sd["rows"])
            elif slide_type == "closing":
                create_closing_slide(prs, sd.get("content"))
            
            # Add speaker notes if present
            if 'notes' in sd and prs.slides:
                notes_slide = prs.slides[-1].notes_slide
                tf = notes_slide.notes_text_frame
                tf.text = "\n".join(sd['notes'])

        if not any(s['type'] == 'closing' for s in slide_data):
            create_closing_slide(prs)

        abs_output_path = os.path.abspath(output_path)
        prs.save(abs_output_path)
        return abs_output_path

    except Exception as e:
        logger.critical(f"An unrecoverable error occurred during PPTX generation: {e}", exc_info=True)
        return None

# --- CLI ---

def main():
    """Command-line interface for the PPTX generator."""
    parser = argparse.ArgumentParser(
        description="IDEAS Professional PPTX Generator — Convert Markdown to branded PowerPoint",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input", "-i", help="Input Markdown file path (stdin if omitted)")
    parser.add_argument("--output", "-o", default="output.pptx", help="Output PPTX file path")
    parser.add_argument("--title", "-t", default="Dokumen IDEAS", help="Presentation title")
    parser.add_argument("--subtitle", "-s", default="", help="Presentation subtitle")
    parser.add_argument("--client", "-c", default="", help="Client name")
    parser.add_argument("--date", "-d", default="", help="Presentation date")
    parser.add_argument("--standard", action="store_true", help="Use 4:3 standard ratio instead of 16:9")
    args = parser.parse_args()

    try:
        if args.input:
            input_path = Path(args.input)
            if not input_path.exists():
                logger.error(f"Input file not found: {args.input}")
                sys.exit(1)
            md_text = input_path.read_text(encoding="utf-8")
        elif not sys.stdin.isatty():
            md_text = sys.stdin.read()
        else:
            parser.print_help()
            logger.error("No input provided. Use --input or pipe from stdin.")
            sys.exit(1)
    except (IOError, PermissionError) as e:
        logger.error(f"Error reading input: {e}")
        sys.exit(1)

    result_path = generate_pptx(
        input_text=md_text,
        output_path=args.output,
        title=args.title,
        subtitle=args.subtitle,
        client=args.client,
        doc_date=args.date,
        widescreen=not args.standard,
    )

    if result_path:
        logger.info(f"PPTX generated successfully: {result_path}")
    else:
        logger.error("Failed to generate PPTX.")
        sys.exit(1)

if __name__ == "__main__":
    main()
