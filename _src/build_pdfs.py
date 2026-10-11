"""Printable PDFs for a chapter: the print view of each activity followed by its answer key.
Usage (repo root, with a local server on port 8125: python3 -m http.server 8125):
    python3 -I _src/build_pdfs.py ch1
Writes downloads/PHD125_<CH>_PreLecture.pdf, _PostLecture.pdf, _Tutorial.pdf."""
import io, sys, pathlib
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader

ROOT = pathlib.Path(__file__).resolve().parent.parent
ch = sys.argv[1]
BASE = 'http://localhost:8125'
M = {'top': '14mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'}
(ROOT / 'downloads').mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for folder, name in [('pre', 'PreLecture'), ('post', 'PostLecture'), ('tutorial', 'Tutorial')]:
        if not (ROOT / ch / folder / 'index.html').exists():
            continue
        w = PdfWriter()
        for q in ('?print', '?print&key'):
            pg = b.new_page()
            pg.goto(f'{BASE}/{ch}/{folder}/{q}')
            pg.wait_for_timeout(1200)
            for page in PdfReader(io.BytesIO(pg.pdf(format='A4', print_background=True, margin=M))).pages:
                w.add_page(page)
            pg.close()
        out = ROOT / 'downloads' / f'PHD125_{ch.upper()}_{name}.pdf'
        with open(out, 'wb') as f:
            w.write(f)
        print(out.relative_to(ROOT), len(w.pages), 'pages')
    b.close()
