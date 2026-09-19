#!/usr/bin/env python3
"""
generate_pdf.py
===============

Generate PDF report dari Markdown narrative + PNG charts.
PDF mencakup: cover page, narasi lengkap, charts disisipkan pada posisi relevan.

Penggunaan:
    python generate_pdf.py \
        --markdown <path>/<name>_profile.md \
        --charts-dir <path>/charts/ \
        --out <path>/<name>_profile.pdf

Dependencies: reportlab, Pillow
    pip install reportlab Pillow --break-system-packages
"""

from __future__ import annotations
import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Try to import reportlab
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Image,
        Table, TableStyle, PageBreak, HRFlowable
    )
    from reportlab.platypus.flowables import KeepTogether
    HAVE_REPORTLAB = True
except ImportError:
    HAVE_REPORTLAB = False

try:
    from PIL import Image as PILImage
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False


# ─── Colors ──────────────────────────────────────────────────────
COLOR_PRIMARY   = colors.HexColor("#1565C0")
COLOR_ACCENT    = colors.HexColor("#FF6F00")
COLOR_DANGER    = colors.HexColor("#C62828")
COLOR_SUCCESS   = colors.HexColor("#2E7D32")
COLOR_NEUTRAL   = colors.HexColor("#424242")
COLOR_LIGHT_BG  = colors.HexColor("#F5F5F5")
COLOR_HEADER_BG = colors.HexColor("#1565C0")


# ─── Styles ──────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()
    styles = {}
    
    styles["title"] = ParagraphStyle(
        "title", parent=base["Title"],
        fontSize=22, textColor=COLOR_PRIMARY,
        spaceAfter=6, alignment=TA_CENTER, fontName="Helvetica-Bold"
    )
    styles["subtitle"] = ParagraphStyle(
        "subtitle", parent=base["Normal"],
        fontSize=13, textColor=COLOR_NEUTRAL,
        spaceAfter=4, alignment=TA_CENTER, fontName="Helvetica"
    )
    styles["h1"] = ParagraphStyle(
        "h1", parent=base["Heading1"],
        fontSize=14, textColor=COLOR_PRIMARY,
        spaceBefore=16, spaceAfter=6, fontName="Helvetica-Bold",
        borderPad=4, leading=18
    )
    styles["h2"] = ParagraphStyle(
        "h2", parent=base["Heading2"],
        fontSize=12, textColor=COLOR_PRIMARY,
        spaceBefore=12, spaceAfter=4, fontName="Helvetica-Bold", leading=15
    )
    styles["h3"] = ParagraphStyle(
        "h3", parent=base["Heading3"],
        fontSize=10, textColor=COLOR_NEUTRAL,
        spaceBefore=8, spaceAfter=3, fontName="Helvetica-Bold", leading=13
    )
    styles["body"] = ParagraphStyle(
        "body", parent=base["Normal"],
        fontSize=9, textColor=COLOR_NEUTRAL,
        leading=14, spaceAfter=4, fontName="Helvetica", alignment=TA_JUSTIFY
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", parent=base["Normal"],
        fontSize=9, textColor=COLOR_NEUTRAL,
        leading=13, spaceAfter=2, leftIndent=16,
        bulletIndent=6, fontName="Helvetica"
    )
    styles["code"] = ParagraphStyle(
        "code", parent=base["Code"],
        fontSize=8, textColor=COLOR_NEUTRAL,
        fontName="Courier", leading=12,
        backColor=COLOR_LIGHT_BG, borderPad=4, spaceAfter=4
    )
    styles["caption"] = ParagraphStyle(
        "caption", parent=base["Normal"],
        fontSize=8, textColor=colors.grey,
        alignment=TA_CENTER, fontName="Helvetica-Oblique", spaceAfter=8
    )
    return styles


# ─── Helpers ─────────────────────────────────────────────────────

# NOTE: _score_color() di versi sebelumnya dipakai untuk pewarnaan badge
# "Data Quality Score" di cover PDF. Skill ini tidak lagi melaporkan skor
# kualitas data, jadi helper tersebut dihapus. Cover PDF hanya menampilkan
# metadata kondisi (rows/cols/duplicates) tanpa pewarnaan berbasis skor.


def _markdown_to_flowables(md_text: str, styles: dict, page_width: float) -> list:
    """Convert Markdown text to reportlab flowables (simplified parser)."""
    flowables = []
    lines = md_text.split("\n")
    i = 0
    
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Skip YAML frontmatter
        if line == "---" and i == 0:
            i += 1
            while i < len(lines) and lines[i].rstrip() != "---":
                i += 1
            i += 1
            continue
        
        # H1
        if line.startswith("# ") and not line.startswith("## "):
            flowables.append(Spacer(1, 4))
            flowables.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
            flowables.append(Paragraph(_clean(line[2:]), styles["h1"]))
            flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_LIGHT_BG))
            i += 1
            continue
        
        # H2
        if line.startswith("## "):
            flowables.append(Paragraph(_clean(line[3:]), styles["h2"]))
            i += 1
            continue
        
        # H3
        if line.startswith("### "):
            flowables.append(Paragraph(_clean(line[4:]), styles["h3"]))
            i += 1
            continue
        
        # Table (markdown | style)
        if "|" in line and line.strip().startswith("|"):
            table_lines = []
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            tbl_flowable = _parse_md_table(table_lines, styles, page_width)
            if tbl_flowable:
                flowables.append(tbl_flowable)
                flowables.append(Spacer(1, 6))
            continue
        
        # Bullet
        if line.startswith("- ") or line.startswith("* "):
            flowables.append(Paragraph(f"• {_clean(line[2:])}", styles["bullet"]))
            i += 1
            continue
        
        # Numbered list
        if re.match(r"^\d+\.", line):
            flowables.append(Paragraph(_clean(line), styles["bullet"]))
            i += 1
            continue
        
        # Code block
        if line.startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            if code_lines:
                code_text = "<br/>".join(code_lines[:20])  # limit to 20 lines
                flowables.append(Paragraph(code_text, styles["code"]))
                flowables.append(Spacer(1, 4))
            continue
        
        # Blockquote
        if line.startswith("> "):
            flowables.append(Paragraph(f"<i>{_clean(line[2:])}</i>", styles["body"]))
            i += 1
            continue
        
        # Horizontal rule
        if line.strip() in ("---", "***", "___") and len(line.strip()) >= 3:
            flowables.append(Spacer(1, 4))
            flowables.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
            flowables.append(Spacer(1, 4))
            i += 1
            continue
        
        # Empty line
        if not line.strip():
            flowables.append(Spacer(1, 4))
            i += 1
            continue
        
        # Normal paragraph
        flowables.append(Paragraph(_clean(line), styles["body"]))
        i += 1
    
    return flowables


def _clean(text: str) -> str:
    """Convert markdown inline formatting to reportlab XML."""
    # Bold **text** and __text__
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"__(.+?)__", r"<b>\1</b>", text)
    # Italic *text* and _text_
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"(?<!\*|\w)_(.+?)_(?!\*|\w)", r"<i>\1</i>", text)
    # Inline code `text`
    text = re.sub(r"`([^`]+)`", r'<font name="Courier" size="8">\1</font>', text)
    # Links [text](url) → just text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Escape &
    text = text.replace("&", "&amp;")
    # Escape < and > that are not already XML tags
    text = re.sub(r"<(?![a-zA-Z/])", "&lt;", text)
    return text


def _parse_md_table(lines: list[str], styles: dict, page_width: float):
    """Parse markdown table into reportlab Table."""
    try:
        rows = []
        for line in lines:
            if re.match(r"^\|[-: ]+\|", line):
                continue  # separator row
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells:
                rows.append(cells)
        
        if len(rows) < 2:
            return None
        
        # Header + data
        header = [Paragraph(f"<b>{_clean(c)}</b>", styles["body"]) for c in rows[0]]
        data = [[Paragraph(_clean(c), styles["body"]) for c in row] for row in rows[1:]]
        
        table_data = [header] + data
        col_count = max(len(r) for r in table_data)
        col_width = (page_width - 2 * cm) / col_count
        
        tbl = Table(table_data, colWidths=[col_width] * col_count, repeatRows=1)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), COLOR_HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG]),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        return tbl
    except Exception:
        return None


def _insert_image(img_path: Path, page_width: float, caption: str = "") -> list:
    """Create image flowable with optional caption."""
    flowables = []
    try:
        if not img_path.exists():
            return flowables
        
        # Get image dimensions
        max_w = page_width - 2 * cm
        max_h = 12 * cm
        
        if HAVE_PIL:
            with PILImage.open(img_path) as im:
                orig_w, orig_h = im.size
            scale = min(max_w / orig_w, max_h / orig_h, 1.0)
            display_w = orig_w * scale
            display_h = orig_h * scale
        else:
            display_w = max_w
            display_h = 8 * cm
        
        img = Image(str(img_path), width=display_w, height=display_h)
        img.hAlign = "CENTER"
        flowables.append(Spacer(1, 6))
        flowables.append(img)
        if caption:
            styles = build_styles()
            flowables.append(Paragraph(caption, styles["caption"]))
        flowables.append(Spacer(1, 6))
    except Exception as e:
        print(f"[warn] Could not insert image {img_path}: {e}", file=sys.stderr)
    return flowables


# ─── Main PDF builder ─────────────────────────────────────────────

def build_pdf(md_path: Path, charts_dir: Path, out_path: Path) -> None:
    if not HAVE_REPORTLAB:
        print("[error] reportlab not installed. Run: pip install reportlab --break-system-packages", file=sys.stderr)
        sys.exit(1)
    
    styles = build_styles()
    md_text = md_path.read_text(encoding="utf-8")
    
    # Find dataset name from markdown title
    title_match = re.search(r"^# Data Profiling Report —\s*(.+)$", md_text, re.MULTILINE)
    dataset_name = title_match.group(1).strip() if title_match else md_path.stem
    
    # Collect available charts
    charts = sorted(charts_dir.glob("*.png")) if charts_dir.exists() else []
    chart_map = {p.stem: p for p in charts}
    
    # Document setup
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2.5 * cm, bottomMargin=2 * cm,
        title=f"Data Profiling Report — {dataset_name}",
        author="data-profiling-baseline",
        subject="Data Quality Profiling Report"
    )
    
    page_width = A4[0] - 4 * cm
    story = []
    
    # ── Cover Page ──────────────────────────────────────────────
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("📊 Data Profiling Report", styles["title"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(dataset_name, styles["subtitle"]))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%d %B %Y, %H:%M')}", styles["subtitle"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(HRFlowable(width="60%", thickness=2, color=COLOR_PRIMARY, hAlign="CENTER"))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "Profiler: <b>data-profiling-baseline</b> | "
        "Mode: <b>Deskriptif kondisi data (apa adanya), tanpa scoring kualitas data</b>",
        styles["caption"]
    ))
    story.append(Spacer(1, 0.5 * cm))

    # ── Cover info card: ringkasan kondisi (rows/cols/duplicates) ──
    # CATATAN: Skill ini TIDAK menampilkan badge "Data Quality Score".
    # Yang ditampilkan adalah info card berisi metrik kondisi deskriptif
    # yang diekstrak dari markdown (jika ada), tanpa pewarnaan score-based.
    info_lines = []
    rows_m = re.search(r"Total baris\s*\|\s*\*\*([\d\.,]+)\*\*", md_text)
    cols_m = re.search(r"Total kolom\s*\|\s*\*\*([\d\.,]+)\*\*", md_text)
    dup_m = re.search(r"[Bb]aris duplikat[^|]*\|\s*\*\*([\d\.,]+)\*\*", md_text)
    null_m = re.search(r"Persentase sel null[^|]*\|\s*\*\*([\d\.,]+)%?\*\*", md_text)
    if rows_m:
        info_lines.append(f"Total baris: <b>{rows_m.group(1)}</b>")
    if cols_m:
        info_lines.append(f"Total kolom: <b>{cols_m.group(1)}</b>")
    if dup_m:
        info_lines.append(f"Baris duplikat penuh: <b>{dup_m.group(1)}</b>")
    if null_m:
        info_lines.append(f"Sel null keseluruhan: <b>{null_m.group(1)}%</b>")

    if info_lines:
        info_tbl = Table(
            [[Paragraph(
                "<b>Ringkasan Kondisi Dataset</b><br/>" + " &nbsp;·&nbsp; ".join(info_lines),
                ParagraphStyle(
                    "ic", fontSize=11, textColor=colors.white,
                    fontName="Helvetica", alignment=TA_CENTER, leading=15,
                ),
            )]],
            colWidths=[12 * cm],
        )
        info_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), COLOR_PRIMARY),
            ("ROWPADDING", (0, 0), (-1, -1), 12),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))
        story.append(info_tbl)

    story.append(PageBreak())

    # ── Narrative Content ──────────────────────────────────────
    flowables = _markdown_to_flowables(md_text, styles, page_width)

    # Insert Condition Snapshot chart after Dataset Condition section
    CHART_INSERTION_MAP = {
        "Dataset Condition Snapshot": "10_condition_snapshot",
        "Dataset Summary": "10_condition_snapshot",  # fallback untuk template lama
        "Column Profiling Highlights": "04_numeric_distributions",
        "Missing": "03_missing_pattern",
        "Correlation": "06_correlation_heatmap",
    }
    
    # Insert charts at natural breakpoints
    inserted_charts = set()
    for fl in flowables:
        story.append(fl)
        # Check if we should insert a chart after this flowable
        if hasattr(fl, "text"):
            txt = getattr(fl, "text", "")
            for keyword, chart_stem in CHART_INSERTION_MAP.items():
                if keyword.lower() in txt.lower() and chart_stem in chart_map and chart_stem not in inserted_charts:
                    story.extend(_insert_image(chart_map[chart_stem], page_width,
                                               f"Fig: {chart_stem.replace('_', ' ').title()}"))
                    inserted_charts.add(chart_stem)
    
    # Append remaining charts after main content
    story.append(PageBreak())
    story.append(Paragraph("Appendix: Visualization Gallery", styles["h1"]))
    story.append(Spacer(1, 0.3 * cm))
    
    for chart_path in sorted(charts):
        stem = chart_path.stem
        caption = stem.replace("_", " ").title().replace("  ", " ")
        story.extend(_insert_image(chart_path, page_width, f"Chart: {caption}"))
    
    story.append(PageBreak())
    story.append(Paragraph("Report generated by data-profiling-baseline skill.", styles["caption"]))
    story.append(Paragraph(
        "Method sources: DAMA-DMBOK 2nd Ed., Abedjan et al. (VLDB 2015), "
        "Clauset-Shalizi-Newman (SIAM 2009), ISO 8000, Great Expectations, ydata-profiling.",
        styles["caption"]
    ))
    
    doc.build(story)
    print(f"[done] PDF generated: {out_path}")


def main() -> int:
    p = argparse.ArgumentParser(description="Generate PDF report from profiling Markdown + charts.")
    p.add_argument("--markdown", required=True, help="Path to _profile.md")
    p.add_argument("--charts-dir", required=True, help="Directory containing PNG charts")
    p.add_argument("--out", required=True, help="Output PDF path")
    args = p.parse_args()
    
    md_path = Path(args.markdown)
    charts_dir = Path(args.charts_dir)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not md_path.exists():
        print(f"[error] Markdown not found: {md_path}", file=sys.stderr)
        return 2
    
    build_pdf(md_path, charts_dir, out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
