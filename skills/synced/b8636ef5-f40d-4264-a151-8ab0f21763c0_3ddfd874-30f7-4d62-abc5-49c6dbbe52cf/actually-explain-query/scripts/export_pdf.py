#!/usr/bin/env python3
"""
export_pdf.py — turn a query map into a PDF.

    python3 export_pdf.py spec.json  -o query_map.pdf      # renders the page first
    python3 export_pdf.py page.html  -o query_map.pdf      # uses an existing page

The page carries its own print stylesheet: printing swaps the dark screen
palette for the light one and lays the content out as a document — the diagram
first, then the summary, the row funnel as a table, every step written out, the
findings and the SQL. This script just drives a headless browser through that.

It looks for a browser engine in this order: Playwright, then any Chrome or
Chromium on the system. If it finds neither it says so and stops — the HTML is
still there, and printing it from a browser (Cmd/Ctrl+P → Save as PDF) produces
the same document.
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME_NAMES = ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable",
                "chrome", "microsoft-edge"]
CHROME_PATHS = ["/opt/pw-browsers/chromium",
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/Applications/Chromium.app/Contents/MacOS/Chromium",
                "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]


def find_chrome():
    for env in ("CHROME", "CHROMIUM", "CHROME_PATH", "PUPPETEER_EXECUTABLE_PATH"):
        v = os.environ.get(env)
        if v and os.path.exists(v):
            return v
    for n in CHROME_NAMES:
        p = shutil.which(n)
        if p:
            return p
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    for pat in ("/opt/pw-browsers/chromium*/chrome-linux/chrome",
                os.path.expanduser("~/.cache/ms-playwright/chromium*/chrome-linux/chrome")):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None


def via_playwright(url, out):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    exe = find_chrome()
    try:
        with sync_playwright() as pw:
            kw = {"args": ["--no-sandbox"]}
            if exe:
                kw["executable_path"] = exe
            b = pw.chromium.launch(**kw)
            page = b.new_page()
            page.goto(url)
            page.wait_for_timeout(2500)      # let fonts settle and the layout resolve
            page.pdf(path=out, format="A4", print_background=True,
                     margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
            b.close()
        return True
    except Exception as e:
        print(f"note: Playwright could not produce the PDF ({e}); trying a browser binary.",
              file=sys.stderr)
        return False


def via_chrome(url, out):
    exe = find_chrome()
    if not exe:
        return False
    with tempfile.TemporaryDirectory() as prof:
        cmd = [exe, "--headless=new", "--disable-gpu", "--no-sandbox",
               f"--user-data-dir={prof}", "--virtual-time-budget=6000",
               "--no-pdf-header-footer", f"--print-to-pdf={out}", url]
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=180)
        except Exception as e:
            print(f"note: could not run {exe} ({e}).", file=sys.stderr)
            return False
        if not os.path.exists(out) or os.path.getsize(out) < 1000:
            # older builds reject --headless=new
            cmd[1] = "--headless"
            subprocess.run(cmd, capture_output=True, timeout=180)
    return os.path.exists(out) and os.path.getsize(out) > 1000


def main():
    ap = argparse.ArgumentParser(description="Export a query map as a PDF.")
    ap.add_argument("source", help="spec JSON or an already rendered HTML page")
    ap.add_argument("-o", "--out", default="query_map.pdf")
    a = ap.parse_args()

    src = os.path.abspath(a.source)
    if src.lower().endswith(".json"):
        html = os.path.splitext(a.out)[0] + ".html"
        r = subprocess.run([sys.executable, os.path.join(HERE, "render_query_map.py"),
                            src, "-o", html, "--standalone"])
        if r.returncode != 0:
            raise SystemExit("could not render the page from the spec")
        src = os.path.abspath(html)
    url = "file://" + src
    out = os.path.abspath(a.out)

    if via_playwright(url, out) or via_chrome(url, out):
        kb = os.path.getsize(out) // 1024
        print(f"wrote {a.out}  ({kb} KB)")
        return

    raise SystemExit(
        "No browser engine found, so the PDF could not be produced here.\n"
        f"The page itself is ready at {src} — open it in any browser and print it "
        "(Cmd/Ctrl+P → Save as PDF). It carries a print stylesheet, so you get the same "
        "document: diagram, summary, row funnel, every step, findings and the SQL.\n"
        "To export from the command line instead, install a browser "
        "(`pip install playwright && playwright install chromium`) and run this again.")


if __name__ == "__main__":
    main()
