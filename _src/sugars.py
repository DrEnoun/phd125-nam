"""Hand-drawn sugar figures for PHD125 Chapter 5: Fischer projections and Haworth projections (SVG data URIs).
RDKit cannot draw these conventions, so they are drawn here from simple specifications.

fischer(top, rows, bottom)        rows = [(left, right), ...]; a row ('C=O',) draws a ketone carbon
haworth(subs, ring='pyr')         subs = [(up, down), ...] for ring carbons in order from the anomeric carbon
disaccharide(a, b, link)          two pyranose rings joined 1->4 by an alpha or beta glycosidic link
sucrose()                         alpha-D-glucose (1->2) beta-D-fructose, fructose ring turned over"""
import base64

INK, RED, MUTED, HI = '#1B2A41', '#C8102E', '#56657A', '#FFE58A'
FONT = 'font-family="Helvetica,Arial,sans-serif"'


def _uri(svg):
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


def _lab(x, y, s, size=17, anchor='middle', weight='400'):
    col = RED if ('O' in s and s not in ('C=O',)) else INK
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{col}" {FONT}>{s}</text>'


def _line(x1, y1, x2, y2, w=2.2, col=INK):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'


# ---------------- Fischer projections ----------------
def fischer_svg(top, rows, bottom, caption='', hi=None, nums=True, x0=0, y0=0, w=230):
    """Returns (svg fragment, width, height). hi = index of a row to shade (e.g. the D/L carbon)."""
    cx, rh = x0 + w / 2, 46
    o, y = [], y0 + 30
    o.append(_lab(cx, y, top, 18))
    n = 1
    if nums:
        o.append(_lab(x0 + 14, y, str(n), 12, weight='400').replace(RED, MUTED))
    yprev = y + 6
    for i, r in enumerate(rows):
        y += rh
        n += 1
        if hi == i:
            o.insert(0, f'<rect x="{cx - 95:.1f}" y="{y - 22:.1f}" width="190" height="34" rx="9" fill="{HI}"/>')
        if len(r) == 1:  # carbonyl carbon of a ketose
            o.append(_line(cx, yprev, cx, y - 16))
            o.append(_lab(cx, y + 6, 'C', 18))
            o.append(_line(cx + 10, y - 2, cx + 34, y - 2) + _line(cx + 10, y + 4, cx + 34, y + 4))
            o.append(_lab(cx + 46, y + 7, 'O', 18))
            yprev = y + 12
        else:
            o.append(_line(cx, yprev, cx, y + 20))
            o.append(_line(cx - 54, y, cx + 54, y))
            l, rr = r
            o.append(_lab(cx - 60, y + 6, l, 17, 'end'))
            o.append(_lab(cx + 60, y + 6, rr, 17, 'start'))
            yprev = y
        if nums:
            o.append(_lab(x0 + 14, y + 6, str(n), 12).replace(RED, MUTED))
    y += rh
    o.append(_line(cx, yprev, cx, y - 18))
    o.append(_lab(cx, y + 6, bottom, 18))
    if nums:
        o.append(_lab(x0 + 14, y + 6, str(n + 1), 12).replace(RED, MUTED))
    if caption:
        y += 40
        o.append(f'<text x="{cx:.1f}" y="{y:.1f}" text-anchor="middle" font-size="16" fill="{INK}" {FONT}>{caption}</text>')
    return ''.join(o), w, y - y0 + 16


def fischer(top, rows, bottom, caption='', hi=None, nums=True):
    frag, w, h = fischer_svg(top, rows, bottom, caption, hi, nums)
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#fff"/>{frag}</svg>')


def fischer_row(items, gap=10):
    """Several Fischer projections side by side: items = [(top, rows, bottom, caption, hi), ...]."""
    frags, x, H = [], 0, 0
    for it in items:
        top, rows, bottom = it[:3]
        cap = it[3] if len(it) > 3 else ''
        hi = it[4] if len(it) > 4 else None
        f, w, h = fischer_svg(top, rows, bottom, cap, hi, nums=False, x0=x)
        frags.append(f)
        x += w + gap
        H = max(H, h)
    W = x - gap
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>{"".join(frags)}</svg>')


# ---------------- Haworth projections ----------------
PYR = {'O': (120, 0), 'C': [(160, 35), (120, 70), (40, 70), (0, 35), (40, 0)]}           # C1 C2 C3 C4 C5
FUR = {'O': (75, -8), 'C': [(150, 30), (115, 72), (35, 72), (0, 30)]}                    # anomeric C, then round the ring


def ring_svg(subs, ring='pyr', ox=0, oy=0, mirror=False, stub=34, showH=False):
    """Draw one Haworth ring. subs[i] = (up, down) for ring carbon i (None = draw nothing there).
    Returns (svg fragment, list of carbon (x, y) positions)."""
    geo = PYR if ring == 'pyr' else FUR
    W = 160 if ring == 'pyr' else 150
    tx = (lambda x: ox + (W - x)) if mirror else (lambda x: ox + x)
    C = [(tx(x), oy + y) for x, y in geo['C']]
    O = (tx(geo['O'][0]), oy + geo['O'][1])
    # ring bonds: order O - C(anomeric) - ... - last C - O
    pts = [O] + C + [O]
    o = []
    front = {(1, 2)} if ring == 'pyr' else {(1, 2)}
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        ci = i - 1  # carbon index of a (if a is a carbon)
        if (ci, ci + 1) in front:
            w = 8
        elif ring == 'pyr' and (ci, ci + 1) in {(0, 1), (2, 3)}:
            w = 4.5
        elif ring == 'fur' and (ci, ci + 1) in {(0, 1), (2, 3)}:
            w = 4.5
        else:
            w = 2.2
        # shorten bonds at the ring O so the label is readable
        if a == O:
            a = (a[0] + (b[0] - a[0]) * 0.28, a[1] + (b[1] - a[1]) * 0.28)
        if b == O:
            b = (b[0] + (a[0] - b[0]) * 0.28, b[1] + (a[1] - b[1]) * 0.28)
        o.append(_line(*a, *b, w=w))
    o.append(f'<text x="{O[0]:.1f}" y="{O[1] + 6:.1f}" text-anchor="middle" font-size="18" fill="{RED}" {FONT}>O</text>')
    for (x, y), sd in zip(C, subs):
        if sd is None:
            continue
        up, down = sd
        if not showH:
            up = None if up == 'H' else up
            down = None if down == 'H' else down
        if up:
            o.append(_line(x, y, x, y - stub))
            o.append(_lab(x, y - stub - 6, up, 16 if up != 'H' else 14))
        if down:
            o.append(_line(x, y, x, y + stub))
            o.append(_lab(x, y + stub + 17, down, 16 if down != 'H' else 14))
    return ''.join(o), C


def haworth(subs, ring='pyr', caption='', w=260, h=235, mirror=False):
    frag, _ = ring_svg(subs, ring, ox=(w - 160) / 2, oy=74, mirror=mirror)
    cap = f'<text x="{w / 2}" y="{h - 10}" text-anchor="middle" font-size="16" fill="{INK}" {FONT}>{caption}</text>' if caption else ''
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#fff"/>{frag}{cap}</svg>')


def haworth_row(items, w=250, h=238):
    """items = [(subs, ring, caption), ...] side by side."""
    o = []
    for i, (subs, ring, cap) in enumerate(items):
        frag, _ = ring_svg(subs, ring, ox=i * w + (w - 160) / 2, oy=74)
        o.append(frag)
        o.append(f'<text x="{i * w + w / 2}" y="{h - 10}" text-anchor="middle" font-size="16" fill="{INK}" {FONT}>{cap}</text>')
    W = w * len(items)
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}"><rect width="{W}" height="{h}" fill="#fff"/>{"".join(o)}</svg>')


# ring substituents (up, down) from the anomeric carbon round the ring
GLC = lambda a: [(('H', 'OH') if a == 'a' else ('OH', 'H')), ('H', 'OH'), ('OH', 'H'), ('H', 'OH'), ('CH₂OH', 'H')]
GAL = lambda a: [(('H', 'OH') if a == 'a' else ('OH', 'H')), ('H', 'OH'), ('OH', 'H'), ('OH', 'H'), ('CH₂OH', 'H')]
FRU = lambda a: [(('CH₂OH', 'OH') if a == 'a' else ('OH', 'CH₂OH')), ('OH', 'H'), ('H', 'OH'), ('CH₂OH', 'H')]
RIB = lambda a: [(('H', 'OH') if a == 'a' else ('OH', 'H')), ('H', 'OH'), ('H', 'OH'), ('CH₂OH', 'H')]


def disaccharide(a_subs, b_subs, link='a', caption='', labels=('', ''), w=560, h=275):
    """Ring A's C1 joined to ring B's C4 through O. link 'a' = bond down from C1; 'b' = bond up from C1."""
    oy, gap = 96, 110
    ax, bx = 20, 20 + 160 + gap
    a_subs = list(a_subs)
    b_subs = list(b_subs)
    up, down = a_subs[0]
    a_subs[0] = (up, None) if link == 'a' else (None, down)
    bu, bd = b_subs[3]
    b_subs[3] = (bu, None)
    fa, Ca = ring_svg(a_subs, 'pyr', ox=ax, oy=oy)
    fb, Cb = ring_svg(b_subs, 'pyr', ox=bx, oy=oy)
    c1, c4 = Ca[0], Cb[3]
    o = [fa, fb]
    if link == 'a':
        ylink = c1[1] + 46
        mx = (c1[0] + c4[0]) / 2
        o.append(_line(c1[0], c1[1], c1[0] + 8, ylink - 8) + _line(c1[0] + 8, ylink - 8, mx - 10, ylink - 2))
        o.append(_lab(mx, ylink + 4, 'O', 18))
        o.append(_line(mx + 10, ylink - 2, c4[0], c4[1]))
    else:
        yo = c1[1] - 40
        mx = (c1[0] + c4[0]) / 2
        o.append(_line(c1[0], c1[1], mx - 10, yo + 2))
        o.append(_lab(mx, yo + 6, 'O', 18))
        o.append(_line(mx + 9, yo + 4, c4[0], c4[1]))
    o.append(f'<text x="{ax + 80}" y="{oy - 72}" text-anchor="middle" font-size="14" fill="{MUTED}" {FONT}>{labels[0]}</text>')
    o.append(f'<text x="{bx + 80}" y="{oy - 72}" text-anchor="middle" font-size="14" fill="{MUTED}" {FONT}>{labels[1]}</text>')
    if caption:
        o.append(f'<text x="{w / 2}" y="{h - 10}" text-anchor="middle" font-size="16" fill="{INK}" {FONT}>{caption}</text>')
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#fff"/>{"".join(o)}</svg>')


def sucrose(caption='', w=560, h=280):
    """alpha-D-glucopyranose C1 (down) - O - C2 of beta-D-fructofuranose. The fructose ring is turned over
    (rotated 180 degrees in the page), so its C2 is on the left and up/down are swapped."""
    oy = 98
    g = GLC('a')
    g[0] = ('H', None)
    fa, Ca = ring_svg(g, 'pyr', ox=20, oy=oy)
    # beta-fructose turned over: C2 (CH2OH up, link down), C3 (H up, OH down), C4 (OH up, H down), C5 (H up, CH2OH down)
    fr = [('CH₂OH', None), ('H', 'OH'), ('OH', 'H'), ('H', 'CH₂OH')]
    fb, Cb = ring_svg(fr, 'fur', ox=330, oy=oy, mirror=True)
    c1, c2 = Ca[0], Cb[0]
    yl = c1[1] + 50
    mx = (c1[0] + c2[0]) / 2
    o = [fa, fb, _line(c1[0], c1[1], c1[0] + 10, yl - 8), _line(c1[0] + 10, yl - 8, mx - 10, yl - 2), _lab(mx, yl + 4, 'O', 18),
         _line(mx + 10, yl - 2, c2[0], c2[1] + 4)]
    o.append(f'<text x="100" y="{oy - 72}" text-anchor="middle" font-size="14" fill="{MUTED}" {FONT}>α-D-glucose</text>')
    o.append(f'<text x="405" y="{oy - 72}" text-anchor="middle" font-size="14" fill="{MUTED}" {FONT}>β-D-fructose</text>')
    if caption:
        o.append(f'<text x="{w / 2}" y="{h - 10}" text-anchor="middle" font-size="16" fill="{INK}" {FONT}>{caption}</text>')
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#fff"/>{"".join(o)}</svg>')


# Fischer data
D_GLUCOSE = ('CHO', [('H', 'OH'), ('HO', 'H'), ('H', 'OH'), ('H', 'OH')], 'CH₂OH')
D_GALACTOSE = ('CHO', [('H', 'OH'), ('HO', 'H'), ('HO', 'H'), ('H', 'OH')], 'CH₂OH')
D_FRUCTOSE = ('CH₂OH', [('C=O',), ('HO', 'H'), ('H', 'OH'), ('H', 'OH')], 'CH₂OH')
D_RIBOSE = ('CHO', [('H', 'OH'), ('H', 'OH'), ('H', 'OH')], 'CH₂OH')
L_GLUCOSE = ('CHO', [('HO', 'H'), ('H', 'OH'), ('HO', 'H'), ('HO', 'H')], 'CH₂OH')
D_GLYC = ('CHO', [('H', 'OH')], 'CH₂OH')
L_GLYC = ('CHO', [('HO', 'H')], 'CH₂OH')
