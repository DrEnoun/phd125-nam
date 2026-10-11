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


def _split(html, seq, pat, minlen=1):
    # accept only labels that continue the sequence (a, b, c ...); a later "see (a)" stays as text
    pieces, stem, last = [], None, 0
    for m in re.finditer(pat, html):
        if len(pieces) < len(seq) and m.group(1) == seq[len(pieces)]:
            if stem is None:
                stem = html[:m.start()]
            else:
                pieces[-1][1] = html[last:m.start()]
            pieces.append([m.group(1), ''])
            last = m.end()
    if len(pieces) < 2:
        return None
    pieces[-1][1] = html[last:]
    # prose such as "in (a) and (b) ..." is not a list of parts
    for _, t in pieces:
        plain = re.sub(r'<[^>]+>', '', t).strip()
        if not plain or (minlen > 1 and re.match(r'(and|or|to|of|nor|,)\b', plain)):
            return None
    return stem.strip(), [tuple(p) for p in pieces]


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
    r = _split(html, [chr(97 + i) for i in range(8)], r'(?:^|(?<=[\s>]))\(([a-h])\)\s*(?=\S)', minlen=8)
    if not r:
        return html
    stem, pieces = r
    return (f'<div class="stem">{stem}</div>' if stem else '') + f'<div class="tier">{_rows(pieces, True)}</div>'
