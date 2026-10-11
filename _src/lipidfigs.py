"""Schematic lipid figures for PHD125 Chapter 6: amphipathic lipids, micelle, bilayer, liposome, membrane (SVG data URIs)."""
import base64
import math

HEAD, TAIL, INK, MUTED, WATER = '#E4572E', '#1B2A41', '#1B2A41', '#56657A', '#DCEEFB'
FONT = 'font-family="Helvetica,Arial,sans-serif"'


def _uri(svg):
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


def _lipid(x, y, ang, r=7, L=34, two=True, head=HEAD):
    """One amphipathic lipid: head at (x, y), tails pointing in direction ang (degrees)."""
    a = math.radians(ang)
    dx, dy = math.cos(a), math.sin(a)
    px, py = -dy, dx
    o = []
    offs = (-3.2, 3.2) if two else (0,)
    for off in offs:
        sx, sy = x + dx * r + px * off, y + dy * r + py * off
        pts = []
        for i in range(7):
            t = i / 6
            w = 2.2 * (1 if i % 2 else -1) if 0 < i < 6 else 0
            pts.append((sx + dx * L * t + px * w, sy + dy * L * t + py * w))
        o.append('<polyline fill="none" stroke="%s" stroke-width="1.6" stroke-linejoin="round" points="%s"/>' % (TAIL, ' '.join(f'{u:.1f},{v:.1f}' for u, v in pts)))
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{head}" stroke="#fff" stroke-width="1"/>')
    return ''.join(o)


def _txt(x, y, s, size=15, col=INK, anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{col}" {FONT}>{s}</text>'


def micelle_svg(cx, cy, R=58, n=22, two=False, L=None):
    o = []
    for i in range(n):
        a = 360 * i / n
        x = cx + R * math.cos(math.radians(a))
        y = cy + R * math.sin(math.radians(a))
        o.append(_lipid(x, y, a + 180, L=L or (R - 14), two=two))
    return ''.join(o)


def amphipathic_parts():
    """A soap anion and a phospholipid with labels: polar head, nonpolar tail(s)."""
    W, H = 520, 210
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>']
    o.append(_lipid(60, 70, 0, r=13, L=150, two=False))
    o.append(_txt(60, 40, 'polar head', 14, HEAD) + _txt(150, 112, 'nonpolar tail', 14, MUTED) + _txt(130, 150, 'soap anion (RCOO⁻ Na⁺)', 15))
    o.append(_lipid(340, 70, 0, r=13, L=150, two=True))
    o.append(_txt(340, 40, 'polar head', 14, HEAD) + _txt(430, 116, 'two nonpolar tails', 14, MUTED) + _txt(420, 150, 'phospholipid', 15))
    o.append(_txt(260, 192, 'hydrophilic head (\"water-loving\") + hydrophobic tails (\"water-fearing\") = amphipathic', 13, MUTED))
    o.append('</svg>')
    return _uri(''.join(o))


def soap_micelle():
    """Soap micelle holding a grease droplet in water."""
    W, H = 360, 260
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{WATER}"/>',
         micelle_svg(180, 125, R=88, n=26, two=False, L=40), f'<circle cx="180" cy="125" r="42" fill="#F4C95D" opacity=".92"/>',
         _txt(180, 130, 'grease', 15), _txt(180, 250, 'water', 14, MUTED), _txt(60, 24, 'soap micelle', 15), '</svg>']
    return _uri(''.join(o))


def lipid_shapes():
    """Micelle, bilayer and liposome side by side in water."""
    W, H = 760, 270
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{WATER}"/>']
    o.append(micelle_svg(120, 120, R=62, n=20, two=False))
    o.append(_txt(120, 240, 'micelle (soaps, bile salts)', 15))
    # bilayer
    for i in range(9):
        x = 270 + i * 22
        o.append(_lipid(x, 60, 90, L=36))
        o.append(_lipid(x, 148, 270, L=36))
    o.append(_txt(358, 240, 'bilayer (cell membranes)', 15))
    # liposome: two concentric rings, inner tails outward, outer tails inward
    cx, cy = 620, 120
    for i in range(26):
        a = 360 * i / 26
        o.append(_lipid(cx + 92 * math.cos(math.radians(a)), cy + 92 * math.sin(math.radians(a)), a + 180, L=22))
    for i in range(14):
        a = 360 * i / 14
        o.append(_lipid(cx + 36 * math.cos(math.radians(a)), cy + 36 * math.sin(math.radians(a)), a, L=18))
    o.append(_txt(cx, 240, 'liposome (water inside)', 15))
    o.append('</svg>')
    return _uri(''.join(o))


def membrane():
    """Fluid mosaic membrane: bilayer, cholesterol, integral and peripheral proteins, sugar chains."""
    W, H = 760, 270
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>',
         _txt(20, 24, 'outside the cell', 14, MUTED, 'start'), _txt(20, 260, 'inside the cell (cytoplasm)', 14, MUTED, 'start')]
    prot = [(250, 110), (520, 110)]
    for i in range(30):
        x = 40 + i * 23
        if any(abs(x - px) < 40 for px, _ in prot):
            continue
        o.append(_lipid(x, 92, 90, L=40))
        o.append(_lipid(x, 190, 270, L=40))
    # cholesterol (small yellow plates in the outer leaflet)
    for x in (130, 400, 650):
        o.append(f'<rect x="{x - 5}" y="104" width="10" height="44" rx="4" fill="#F4C95D" stroke="#B88A17"/>')
    o.append(_txt(130, 62, 'cholesterol', 12, '#8B6510'))
    # integral proteins
    for px, _ in prot:
        o.append(f'<rect x="{px - 30}" y="68" width="60" height="146" rx="26" fill="#8FD3C7" stroke="#2A8C7C" stroke-width="2"/>')
    o.append(_txt(250, 136, 'integral', 13) + _txt(250, 152, 'protein', 13))
    o.append(_txt(520, 136, 'channel /', 13) + _txt(520, 152, 'carrier', 13))
    # peripheral protein
    o.append('<ellipse cx="370" cy="222" rx="40" ry="16" fill="#B5C7F2" stroke="#4A63B5" stroke-width="2"/>' + _txt(370, 227, 'peripheral', 12))
    # glycocalyx sugar chains on the outside
    for sx in (240, 520, 700):
        pts = ' '.join(f'{sx + (8 if k % 2 else -8)},{68 - 12 * k}' for k in range(4))
        o.append(f'<polyline fill="none" stroke="#7A4E9C" stroke-width="2" points="{pts}"/>')
        for k in range(4):
            o.append(f'<circle cx="{sx + (8 if k % 2 else -8)}" cy="{68 - 12 * k}" r="4" fill="#C9A6E4"/>')
    o.append(_txt(400, 40, 'sugar chains (glycolipids, glycoproteins)', 13, '#7A4E9C'))
    o.append('</svg>')
    return _uri(''.join(o))


def steroid_rings():
    """The steroid nucleus: four fused rings labelled A, B, C, D."""
    W, H = 360, 230
    s = 38  # hexagon side
    h = s * math.sqrt(3) / 2

    def hexagon(cx, cy):
        return [(cx + s * math.cos(math.radians(30 + 60 * k)), cy + s * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
    A = (80, 150); B = (80 + 2 * h, 150); C = (80 + 3 * h, 150 - 1.5 * s)
    rings = [hexagon(*A), hexagon(*B), hexagon(*C)]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>']
    for r in rings:
        o.append('<polygon fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round" points="%s"/>' % (INK, ' '.join(f'{x:.1f},{y:.1f}' for x, y in r)))
    # ring D: pentagon fused to ring C's right edge (vertices 0 and 5 of C)
    c = rings[2]
    p1, p2 = c[0], c[5]
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    q1 = (p1[0] + s * 0.95, p1[1] + 0.2 * s)
    q2 = (p2[0] + s * 0.95, p2[1] - 0.2 * s)
    tip = (mx + s * 1.45, my)
    o.append('<polygon fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round" points="%s"/>' % (INK, ' '.join(f'{x:.1f},{y:.1f}' for x, y in [p1, q1, tip, q2, p2])))
    for lab, (x, y) in zip('ABC', (A, B, C)):
        o.append(_txt(x, y + 6, lab, 20, '#B86E00'))
    o.append(_txt(mx + s * 0.72, my + 6, 'D', 20, '#B86E00'))
    o.append(_txt(W / 2, 222, 'three six-membered rings + one five-membered ring', 13, MUTED))
    o.append('</svg>')
    return _uri(''.join(o))


def triglyceride(chains, caption='', w=560):
    """Textbook condensed drawing of a triacylglycerol: glycerol backbone down the left, ester groups shaded.
    chains = three acyl tails as text, e.g. '(CH₂)₁₆CH₃'."""
    H = 250 if caption else 228
    rows = [('CH₂', 52), ('CH', 128), ('CH₂', 204)]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" viewBox="0 0 {w} {H}"><rect width="{w}" height="{H}" fill="#fff"/>']
    for (c, y), tail in zip(rows, chains):
        o.append(f'<rect x="80" y="{y - 44}" width="46" height="58" rx="8" fill="#FFE08A"/>')
        o.append(_txt(40, y + 6, c, 20, INK))
        o.append(f'<text x="70" y="{y + 6}" font-size="20" fill="{INK}" {FONT}>–<tspan fill="#C8102E">O</tspan>–C–{tail}</text>')
        o.append(f'<text x="112" y="{y - 24}" text-anchor="middle" font-size="18" fill="#C8102E" {FONT}>O</text>')
        o.append(f'<line x1="109" y1="{y - 21}" x2="109" y2="{y - 10}" stroke="{INK}" stroke-width="1.6"/><line x1="115" y1="{y - 21}" x2="115" y2="{y - 10}" stroke="{INK}" stroke-width="1.6"/>')
    for y1, y2 in ((60, 108), (136, 184)):
        o.append(f'<line x1="40" y1="{y1}" x2="40" y2="{y2}" stroke="{INK}" stroke-width="2"/>')
    o.append(_txt(w - 10, 222, 'shaded: ester groups', 12, MUTED, 'end'))
    if caption:
        o.append(_txt(w / 2, H - 6, caption, 15))
    o.append('</svg>')
    return _uri(''.join(o))
