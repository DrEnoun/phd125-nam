"""Lay out multi-part questions as a stem, then one row per part: (a) ... (b) ... ; (i) (ii) nest inside a part.
Used by build_deck.py (slides) and build_acts.py (pre, post, tutorial), so every page looks the same."""
import re

ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii']
MARKS = re.compile(r'\s*\((\d+ marks?)\)\s*[.;]?\s*$')
CSS = ('.tier{display:grid;gap:8px;margin-top:10px}'
       '.tier>div{display:grid;grid-template-columns:2.4em 1fr auto;align-items:baseline;column-gap:6px}'
       '.tier>div>b{color:var(--tier-accent,inherit)}'
       '.tier .mk{white-space:nowrap;font-size:.85em;opacity:.75}'
       '.tier .tier{margin-top:4px;gap:4px}.tier .tier>div{grid-template-columns:2.2em 1fr auto}'
       '.stem{margin-bottom:2px}')


def _split(html, seq, pat):
    parts = re.split(pat, html)
    if len(parts) < 5:
        return None
    labels = parts[1::2]
    if labels != seq[:len(labels)]:
        return None
    return parts[0].strip(), list(zip(labels, parts[2::2]))


def _rows(pieces, inner):
    out = ''
    for l, txt in pieces:
        txt = txt.strip()
        mk = ''
        m = MARKS.search(txt)
        if m:
            mk, txt = m.group(1), txt[:m.start()].strip()
        txt = re.sub(r'[;,]\s*$', '', txt)
        if inner and txt[:1].islower():
            txt = txt[0].upper() + txt[1:]
        if inner:
            txt = tier(txt, roman=True, wrap=False)
        out += f'<div><b>({l})</b><span>{txt}</span>' + (f'<span class="mk">({mk})</span>' if mk else '<span></span>') + '</div>'
    return out


def tier(html, roman=False, wrap=True):
    if not isinstance(html, str):
        return html
    if roman:
        r = _split(html, ROMAN, r'(?:^|(?<=[\s>]))\((i{1,3}|iv|v|vi{0,3})\)\s*')
        if not r:
            return html
        stem, pieces = r
        return (stem + ' ' if stem else '') + f'<div class="tier">{_rows(pieces, False)}</div>'
    r = _split(html, [chr(97 + i) for i in range(8)], r'(?:^|(?<=[\s>]))\(([a-h])\)\s*(?=\S)')
    if not r:
        return html
    stem, pieces = r
    return (f'<div class="stem">{stem}</div>' if stem else '') + f'<div class="tier">{_rows(pieces, True)}</div>'
