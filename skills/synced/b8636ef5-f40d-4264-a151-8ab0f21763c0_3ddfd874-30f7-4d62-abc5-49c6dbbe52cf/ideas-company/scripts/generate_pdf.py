_#_ coding: utf-8
# v2.1.0

"""
IDEAS Professional PDF Generator (v2.1 — Robust & Enhanced)

Converts Markdown documents to branded PDF with IDEAS visual identity.
Uses WeasyPrint (HTML/CSS → PDF) for high-quality typographic output.

Features:
  - Elegant minimalist white cover page with navy accent
  - IDEAS navy branding (#0A0A5C) with logo header/footer
  - Clean, small readable fonts (10pt body, 8.5pt tables)
  - Responsive tables that fit within margins
  - Page numbers, running headers, professional layout
  - Auto-converts Markdown tables to styled HTML tables
  - Syntax highlighting for code blocks
  - Robust error handling and logging

Usage:
    python3 generate_pdf.py --input proposal.md --output proposal.pdf \
        --title "Proposal Konsultansi Data" \
        --subtitle "Asesmen Kematangan Data & Roadmap Strategis" \
        --client "Pemerintah Provinsi Jawa Barat" \
        --doc-number "IDEAS/PROP/2026/001"

    python3 generate_pdf.py --input report.md --output report.pdf --no-cover
    python3 generate_pdf.py --input matrix.md --output matrix.pdf --landscape
    echo "# Hello" | python3 generate_pdf.py --output hello.pdf

Dependencies:
    pip install weasyprint markdown Pygments
"""

import argparse
import base64
import logging
import os
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

# --- Dependency Check ---
try:
    import markdown
    from weasyprint import HTML
    from pygments.formatters import HtmlFormatter
except ImportError as e:
    logger.error(f"Error: Missing dependency - {e}")
    logger.error("Please install required packages with: pip install weasyprint markdown Pygments")
    sys.exit(1)

# --- Constants ---

# Version
VERSION = "2.1.0"

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / "templates"

# Logo files (Corrected spelling from Potrait to Portrait)
LOGO_LANDSCAPE = TEMPLATES_DIR / "LogoIDEASLandscape.png"
LOGO_PORTRAIT = TEMPLATES_DIR / "LogoIDEASPortrait.png" # Corrected spelling
LOGO_ICON = TEMPLATES_DIR / "Logo_ideas.png"

# Branding Colors
NAVY = "#0A0A5C"
NAVY_LIGHT = "#1A1A8C"
NAVY_LIGHTER = "#2D3A8C"
ACCENT_BG = "#F8F9FC"
TABLE_HEADER_BG = "#0A0A5C"
TABLE_ALT_ROW = "#F8F9FC"
TABLE_BORDER = "#D8DAE5"
TEXT_COLOR = "#2D2D3D"
TEXT_LIGHT = "#6B7280"
WHITE = "#FFFFFF"

# Company Info
COMPANY_NAME = "PT Indonesian Data Ecosystem"
COMPANY_SHORT = "IDEAS"
COMPANY_TAGLINE = "Empowering Innovation Through Data"
COMPANY_ADDRESS = "Komplek Margahayu Raya, Jl. Uranus IV Blok C3 No.59, Bandung 40286"
COMPANY_EMAIL = "contact@data-ecosystem.id"
COMPANY_WEB = "https://data-ecosystem.id"

# --- Helper Functions ---

def encode_logo(logo_path: Path) -> str:
    """
    Encodes a logo image file to a base64 data URI for embedding in HTML/CSS.

    Args:
        logo_path: The Path object pointing to the logo file.

    Returns:
        A string containing the base64 data URI, or an empty string if the file
        does not exist.
    """
    if not logo_path.exists():
        logger.warning(f"Logo file not found at: {logo_path}. It will be omitted.")
        return ""
    try:
        with open(logo_path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return f"data:image/png;base64,{data}"
    except (IOError, OSError) as e:
        logger.error(f"Could not read logo file {logo_path}: {e}")
        return ""

def md_to_html(md_text: str) -> str:
    """
    Converts a Markdown string to an HTML string.

    This function uses the python-markdown library with several extensions enabled
    to support features like tables, fenced code blocks with syntax highlighting,
    and more.

    Args:
        md_text: The Markdown content as a string.

    Returns:
        The converted HTML content as a string.
    """
    extensions = [
        "tables",
        "fenced_code",
        "codehilite",
        "toc",
        "attr_list",
        "md_in_html",
        "sane_lists",
    ]
    extension_configs = {
        "codehilite": {
            "css_class": "code-block",
            "pygments_style": "default",
            "noclasses": True,
        },
        "toc": {"permalink": False},
    }
    try:
        return markdown.markdown(
            md_text, extensions=extensions, extension_configs=extension_configs
        )
    except Exception as e:
        logger.error(f"Failed to convert Markdown to HTML: {e}")
        return f"<p><strong>Error converting Markdown:</strong> {e}</p>"

def _get_code_css() -> str:
    """Generates CSS for Pygments syntax highlighting."""
    return HtmlFormatter(style="default").get_style_defs(".code-block")

def _build_css(page_size: str, doc_title_short: str, doc_number: str) -> str:
    """
    Builds the complete CSS stylesheet for the PDF document.

    This includes page layout, typography, cover page styles, content styles,
    and syntax highlighting themes.

    Args:
        page_size: The CSS page size (e.g., "A4", "A4 landscape").
        doc_title_short: A shortened document title for the running header.
        doc_number: The document reference number for the footer.

    Returns:
        A string containing the full CSS stylesheet.
    """
    code_css = _get_code_css()
    return f"""
/* === IDEAS Professional PDF Stylesheet v2.1 === */

/* --- Page Setup --- */
@page {{
    size: {page_size};
    margin: 25mm 22mm 28mm 22mm;

    @top-left {{
        content: element(header-left);
    }}
    @top-right {{
        content: "{doc_title_short}";
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7.5pt;
        color: {NAVY};
        padding-top: 5mm;
        font-weight: 500;
    }}
    @bottom-left {{
        content: "{COMPANY_SHORT} — {COMPANY_TAGLINE}";
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7pt;
        color: {TEXT_LIGHT};
    }}
    @bottom-center {{
        content: "{doc_number}";
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7pt;
        color: {TEXT_LIGHT};
    }}
    @bottom-right {{
        content: "Halaman " counter(page) " dari " counter(pages);
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        font-size: 7pt;
        color: {TEXT_LIGHT};
    }}
}}

@page :first {{
    margin: 0;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-center {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

/* --- Base Typography --- */
html {{
    font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: {TEXT_COLOR};
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

body {{ margin: 0; padding: 0; }}

/* --- Running Header Element --- */
.running-header {{
    position: running(header-left);
    height: 12mm;
    padding-top: 3mm;
}}
.running-header img {{
    height: 9mm;
    width: auto;
}}

/* ============================================ */
/* === COVER PAGE — Elegant Minimalist White === */
/* ============================================ */
.cover-page {{
    page: cover;
    display: block;
    height: 297mm;
    width: 210mm;
    background: {WHITE};
    color: {TEXT_COLOR};
    page-break-after: always;
    position: relative;
    box-sizing: border-box;
}}

/* Navy accent strip at very top */
.cover-accent-top {{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4mm;
    background: {NAVY};
}}

/* Logo area — top left */
.cover-header {{
    position: absolute;
    top: 22mm;
    left: 28mm;
    right: 28mm;
}}
.cover-header img {{
    height: 14mm;
    width: auto;
}}

/* Thin line under logo */
.cover-line-top {{
    position: absolute;
    top: 42mm;
    left: 28mm;
    right: 28mm;
    height: 0.6pt;
    background: {NAVY};
    opacity: 0.25;
}}

/* Title area — upper third */
.cover-title-area {{
    position: absolute;
    top: 62mm;
    left: 28mm;
    right: 35mm;
}}

.cover-title {{
    font-size: 26pt;
    font-weight: 700;
    line-height: 1.2;
    color: {NAVY};
    margin: 0 0 5mm 0;
    letter-spacing: -0.3pt;
}}

.cover-subtitle {{
    font-size: 13pt;
    font-weight: 400;
    line-height: 1.45;
    color: {TEXT_LIGHT};
    margin: 0;
}}

/* Short accent line below subtitle */
.cover-accent-line {{
    position: absolute;
    top: 130mm;
    left: 28mm;
    width: 40mm;
    height: 2pt;
    background: {NAVY};
}}

/* Metadata area — lower third */
.cover-meta-area {{
    position: absolute;
    bottom: 62mm;
    left: 28mm;
    right: 35mm;
}}

.cover-meta-table {{
    border-collapse: collapse;
    font-size: 9.5pt;
    line-height: 1.7;
    color: {TEXT_COLOR};
}}

.cover-meta-table td {{
    padding: 1mm 0;
    border: none;
    vertical-align: top;
}}

.cover-meta-label {{
    color: {TEXT_LIGHT};
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
    color: {NAVY};
}}

/* Footer — bottom */
.cover-footer {{
    position: absolute;
    bottom: 18mm;
    left: 28mm;
    right: 28mm;
}}

.cover-footer-line {{
    height: 0.6pt;
    background: {NAVY};
    opacity: 0.2;
    margin-bottom: 4mm;
}}

.cover-footer-text {{
    font-size: 7.5pt;
    color: {TEXT_LIGHT};
    letter-spacing: 0.2pt;
    line-height: 1.6;
}}

/* ============================================ */
/* === CONTENT PAGES                         === */
/* ============================================ */

/* --- Headings --- */
h1 {{
    font-size: 19pt;
    font-weight: 700;
    color: {NAVY};
    margin-top: 14mm;
    margin-bottom: 5mm;
    padding-bottom: 3mm;
    border-bottom: 1.5pt solid {NAVY};
    page-break-after: avoid;
    letter-spacing: -0.2pt;
}}

h2 {{
    font-size: 13.5pt;
    font-weight: 600;
    color: {NAVY};
    margin-top: 10mm;
    margin-bottom: 4mm;
    padding-bottom: 2mm;
    border-bottom: 0.6pt solid {TABLE_BORDER};
    page-break-after: avoid;
}}

h3 {{
    font-size: 11.5pt;
    font-weight: 600;
    color: {NAVY_LIGHT};
    margin-top: 7mm;
    margin-bottom: 3mm;
    page-break-after: avoid;
}}

h4 {{
    font-size: 10.5pt;
    font-weight: 600;
    color: {TEXT_COLOR};
    margin-top: 5mm;
    margin-bottom: 2mm;
    page-break-after: avoid;
}}

/* --- Paragraphs --- */
p {{
    margin: 0 0 3mm 0;
    text-align: justify;
    orphans: 3;
    widows: 3;
}}

/* --- Lists --- */
ul, ol {{
    margin: 2mm 0 4mm 0;
    padding-left: 7mm;
}}
li {{
    margin-bottom: 1.5mm;
    line-height: 1.55;
}}

/* --- Tables --- */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 8.5pt;
    line-height: 1.45;
    page-break-inside: auto;
}}

thead {{ display: table-header-group; }}
tr {{ page-break-inside: avoid; page-break-after: auto; }}

th {{
    background-color: {TABLE_HEADER_BG};
    color: {WHITE};
    font-weight: 600;
    font-size: 8pt;
    text-align: left;
    padding: 2.8mm 2.5mm;
    border: 0.5pt solid {NAVY};
    vertical-align: middle;
    text-transform: uppercase;
    letter-spacing: 0.4pt;
}}

td {{
    padding: 2.5mm 2.5mm;
    border: 0.5pt solid {TABLE_BORDER};
    vertical-align: top;
    word-wrap: break-word;
    overflow-wrap: break-word;
    hyphens: auto;
}}

tbody tr:nth-child(even) {{
    background-color: {TABLE_ALT_ROW};
}}

td:first-child {{
    font-weight: 500;
    white-space: nowrap;
}}

/* --- Blockquotes --- */
blockquote {{
    margin: 4mm 0;
    padding: 3.5mm 4mm 3.5mm 5mm;
    border-left: 2.5pt solid {NAVY};
    background-color: {ACCENT_BG};
    font-size: 9pt;
    color: {TEXT_COLOR};
    page-break-inside: avoid;
}}
blockquote p {{ margin: 1mm 0; }}

/* --- Code --- */
code {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #F3F4F6;
    padding: 0.5mm 1.5mm;
    border-radius: 1mm;
}}

pre {{
    page-break-inside: avoid;
    margin: 4mm 0;
}}

pre code {{ background: none; padding: 0; }}

/* --- Syntax Highlighting (Pygments) --- */
{code_css}

.code-block {{
    background-color: #f8f8f8;
    border: 1px solid #ddd;
    padding: 1em;
    line-height: 1.4;
    overflow-x: auto;
    font-size: 8pt;
    border-radius: 2mm;
}}

/* --- Horizontal Rules --- */
hr {{
    border: none;
    border-top: 0.6pt solid {TABLE_BORDER};
    margin: 6mm 0;
}}

/* --- Strong/Bold --- */
strong {{
    font-weight: 600;
    color: {NAVY};
}}

/* --- Links --- */
a {{
    color: {NAVY_LIGHT};
    text-decoration: none;
}}

/* --- Confidentiality Notice --- */
.confidential-notice {{
    text-align: center;
    font-size: 7.5pt;
    color: {TEXT_LIGHT};
    margin-top: 10mm;
    padding-top: 3mm;
    border-top: 0.5pt solid {TABLE_BORDER};
}}

/* --- Print --- */
@media print {{
    body {{ margin: 0; }}
    .no-print {{ display: none; }}
}}
"""

def _build_html(
    title: str,
    subtitle: str,
    client: str,
    doc_date: str,
    doc_number: str,
    show_cover: bool,
    show_confidential: bool,
    content_html: str,
    css: str,
    logo_landscape_uri: str,
) -> str:
    """
    Builds the full HTML document string, ready for PDF conversion.

    This function assembles the cover page, running header, main content, and
    confidentiality notice into a single HTML structure.

    Args:
        title: The main document title.
        subtitle: The document subtitle.
        client: The client's name.
        doc_date: The formatted document date string.
        doc_number: The document reference number.
        show_cover: Flag to include the cover page.
        show_confidential: Flag to include the confidentiality notice.
        content_html: The main body content (already converted from Markdown).
        css: The full CSS stylesheet.
        logo_landscape_uri: The base64 data URI for the landscape logo.

    Returns:
        A string containing the complete HTML document.
    """
    # Build cover page HTML
    cover_html = ""
    if show_cover:
        meta_rows = []
        if client:
            meta_rows.append(f'''<tr>
                <td class="cover-meta-label">Dipersiapkan untuk</td>
                <td class="cover-meta-value">{client}</td>
            </tr>''')
        meta_rows.append(f'''<tr>
            <td class="cover-meta-label">Dipersiapkan oleh</td>
            <td class="cover-meta-value">{COMPANY_NAME}</td>
        </tr>''')
        if doc_date:
            meta_rows.append(f'''<tr>
                <td class="cover-meta-label">Tanggal</td>
                <td class="cover-meta-value">{doc_date}</td>
            </tr>''')
        if doc_number:
            meta_rows.append(f'''<tr>
                <td class="cover-meta-label">No. Dokumen</td>
                <td class="cover-meta-value">{doc_number}</td>
            </tr>''')

        meta_table = "\n".join(meta_rows)

        logo_img = ""
        if logo_landscape_uri:
            logo_img = f'<img src="{logo_landscape_uri}" alt="IDEAS Logo">'

        cover_html = f'''
    <div class="cover-page">
        <div class="cover-accent-top"></div>
        <div class="cover-header">{logo_img}</div>
        <div class="cover-line-top"></div>
        <div class="cover-title-area">
            <div class="cover-title">{title}</div>
            {"<div class='cover-subtitle'>" + subtitle + "</div>" if subtitle else ""}
        </div>
        <div class="cover-accent-line"></div>
        <div class="cover-meta-area">
            <table class="cover-meta-table">{meta_table}</table>
        </div>
        <div class="cover-footer">
            <div class="cover-footer-line"></div>
            <div class="cover-footer-text">
                {COMPANY_ADDRESS}<br>
                {COMPANY_EMAIL} &nbsp;|&nbsp; {COMPANY_WEB}
            </div>
        </div>
    </div>
'''

    # Running header
    running_header = ""
    if logo_landscape_uri:
        running_header = f'''
    <div class="running-header">
        <img src="{logo_landscape_uri}" alt="IDEAS Running Header Logo">
    </div>'''

    # Confidential notice
    confidential_html = ""
    if show_confidential:
        confidential_html = f'''
    <div class="confidential-notice">
        Dokumen ini bersifat rahasia dan hanya ditujukan untuk pihak yang disebutkan di atas.
        Dilarang memperbanyak atau mendistribusikan tanpa izin tertulis dari {COMPANY_SHORT}.
    </div>'''

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{css}</style>
</head>
<body>
    {running_header}
    {cover_html}
    <div class="document-content">{content_html}</div>
    {confidential_html}
</body>
</html>
"""

def _format_date(date_obj: date, locale: str = "id") -> str:
    """
    Formats a date object into a string based on a locale.

    Args:
        date_obj: The date object to format.
        locale: The locale to use for formatting (currently only "id" supported).

    Returns:
        A formatted date string (e.g., "20 Februari 2026").
    """
    if locale == "id":
        months_id = [
            "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ]
        return f"{date_obj.day} {months_id[date_obj.month - 1]} {date_obj.year}"
    # Default to ISO format for other locales
    return date_obj.isoformat()

def generate_pdf(
    input_text: str,
    output_path: str,
    title: str = "Dokumen IDEAS",
    subtitle: str = "",
    client: str = "",
    doc_date: str = "",
    doc_number: str = "",
    show_cover: bool = True,
    show_confidential: bool = True,
    landscape: bool = False,
) -> Optional[str]:
    """
    Generates a branded PDF from a Markdown string.

    This is the main function that orchestrates the conversion process, from
    Markdown to HTML, building the CSS, and finally rendering the PDF.

    Args:
        input_text: The Markdown content as a string.
        output_path: The destination path for the output PDF file.
        title: The document title for the cover page and metadata.
        subtitle: The document subtitle for the cover page.
        client: The client's name for the cover page.
        doc_date: A specific date string. If empty, today's date is used.
        doc_number: The document reference number.
        show_cover: If True, a cover page is prepended to the document.
        show_confidential: If True, a confidentiality notice is appended.
        landscape: If True, the document is rendered in landscape orientation.

    Returns:
        The absolute path to the generated PDF file, or None if an error occurred.
    """
    logger.info(f"Starting PDF generation for output: {output_path}")

    # Convert main content from Markdown to HTML
    content_html = md_to_html(input_text)

    # Encode logo for embedding
    logo_landscape_uri = encode_logo(LOGO_LANDSCAPE)

    # Determine page orientation
    page_size = "A4 landscape" if landscape else "A4"
    logger.info(f"Page orientation set to: {page_size}")

    # Truncate long titles for the running header
    doc_title_short = (title[:57] + "...") if len(title) > 60 else title

    # Format date if not provided
    if not doc_date:
        doc_date = _format_date(date.today(), locale="id")

    # Build the CSS and HTML documents
    css = _build_css(page_size, doc_title_short, doc_number or "")
    html_str = _build_html(
        title, subtitle, client, doc_date, doc_number,
        show_cover, show_confidential, content_html,
        css, logo_landscape_uri,
    )

    # Write PDF
    try:
        output_abs_path = Path(output_path).resolve()
        output_abs_path.parent.mkdir(parents=True, exist_ok=True)
        HTML(string=html_str).write_pdf(str(output_abs_path))
        logger.info(f"PDF generated successfully: {output_abs_path}")
        return str(output_abs_path)
    except Exception as e:
        logger.error(f"Failed to write PDF file to {output_path}: {e}")
        # For more detailed debugging, you could re-raise or handle specific exceptions
        return None

def main():
    """Main function to handle command-line interface (CLI) execution."""
    parser = argparse.ArgumentParser(
        description="IDEAS Professional PDF Generator — Convert Markdown to branded PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 generate_pdf.py -i proposal.md -o proposal.pdf -t "Proposal A" -c "Client B"
  echo "# Test" | python3 generate_pdf.py -o test.pdf --no-cover
        """,
    )

    parser.add_argument("--input", "-i", help="Input Markdown file path (reads from stdin if omitted)")
    parser.add_argument("--output", "-o", default="output.pdf", help="Output PDF file path (default: output.pdf)")
    parser.add_argument("--title", "-t", default="Dokumen IDEAS", help="Document title")
    parser.add_argument("--subtitle", "-s", default="", help="Document subtitle")
    parser.add_argument("--client", "-c", default="", help="Client name")
    parser.add_argument("--date", "-d", default="", help="Document date (e.g., 'YYYY-MM-DD')")
    parser.add_argument("--doc-number", default="", help="Document reference number")
    parser.add_argument("--no-cover", action="store_true", help="Do not include a cover page")
    parser.add_argument("--no-confidential", action="store_true", help="Do not include the confidentiality notice")
    parser.add_argument("--landscape", action="store_true", help="Use landscape page orientation")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

    args = parser.parse_args()

    # --- Read Input ---
    md_text = ""
    try:
        if args.input:
            input_path = Path(args.input)
            if not input_path.exists():
                logger.error(f"Input file not found: {args.input}")
                sys.exit(1)
            md_text = input_path.read_text(encoding="utf-8")
            logger.info(f"Successfully read input from {args.input}")
        elif not sys.stdin.isatty():
            md_text = sys.stdin.read()
            logger.info("Successfully read input from stdin")
        else:
            logger.error("No input provided. Use --input or pipe from stdin.")
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to read input: {e}")
        sys.exit(1)

    # --- Generate PDF ---
    result_path = generate_pdf(
        input_text=md_text,
        output_path=args.output,
        title=args.title,
        subtitle=args.subtitle,
        client=args.client,
        doc_date=args.date,
        doc_number=args.doc_number,
        show_cover=not args.no_cover,
        show_confidential=not args.no_confidential,
        landscape=args.landscape,
    )

    if not result_path:
        logger.error("PDF generation failed. See logs above for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
