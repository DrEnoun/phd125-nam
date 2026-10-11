"""Schematic figures for PHD125 Chapter 7 (SVG data URIs): protein structure levels, tertiary interactions,
enzyme models, rate curves, inhibition and feedback control. Drawn by Dr. NAM."""
import base64
import math

INK, MUTED = '#1B2A41', '#56657A'
C1, C2, C3, C4 = '#2F6F9F', '#E4572E', '#2E7D4F', '#B86E00'
SOFT = '#EAF2F8'
FONT = 'font-family="Helvetica,Arial,sans-serif"'


def _uri(svg):
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


def _t(x, y, s, size=14, col=INK, anchor='middle', weight='400'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{col}" {FONT}>{s}</text>'


def _svg(w, h, body, bg='#fff'):
    return _uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def levels():
    """Primary, secondary, tertiary, quaternary structure side by side."""
    o = []
    # primary: beads on a string
    cols = [C1, C2, C3, C4, C1, C3, C2, C4]
    for i in range(8):
        x = 30 + i * 22
        if i:
            o.append(f'<line x1="{x - 22 + 8}" y1="100" x2="{x - 8}" y2="100" stroke="{INK}" stroke-width="2"/>')
        o.append(f'<circle cx="{x}" cy="100" r="9" fill="{cols[i]}"/>')
    o.append(_t(108, 70, 'Gly–Ala–Ser–Lys…', 12, MUTED))
    o.append(_t(108, 180, '1° primary', 15, INK, weight='700') + _t(108, 198, 'amino acid sequence', 12, MUTED))
    # secondary: helix + sheet
    pts = []
    for k in range(0, 121):
        t = k / 120
        pts.append((250 + 30 * math.sin(t * 6 * math.pi), 40 + 110 * t))
    o.append('<polyline fill="none" stroke="%s" stroke-width="5" stroke-linecap="round" points="%s"/>' % (C1, ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)))
    for k in range(3):
        y = 60 + k * 30
        o.append(f'<path d="M300 {y} L356 {y} L356 {y - 7} L372 {y + 4} L356 {y + 15} L356 {y + 8} L300 {y + 8} Z" fill="{C3}" opacity=".85"/>')
    o.append(_t(310, 180, '2° secondary', 15, INK, weight='700') + _t(310, 198, 'α-helix and β-sheet', 12, MUTED))
    # tertiary: folded chain
    path = 'M430 70 C 470 20, 520 40, 500 80 S 440 130, 470 150 S 540 160, 530 110 S 470 60, 520 60'
    o.append(f'<path d="{path}" fill="none" stroke="{C1}" stroke-width="6" stroke-linecap="round"/>')
    o.append(_t(480, 180, '3° tertiary', 15, INK, weight='700') + _t(480, 198, 'whole chain folded in 3D', 12, MUTED))
    # quaternary: four subunits
    for (cx, cy, c) in ((610, 75, C1), (660, 75, C2), (610, 125, C3), (660, 125, C4)):
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="26" ry="23" fill="{c}" opacity=".85"/>')
    o.append(_t(635, 180, '4° quaternary', 15, INK, weight='700') + _t(635, 198, 'several chains (haemoglobin)', 12, MUTED))
    return _svg(720, 210, ''.join(o))


def tertiary():
    """Folded chain with the four kinds of side-chain interaction."""
    g = [f'<path d="M40 60 C 160 -10, 300 40, 300 110 S 160 200, 80 160 S 60 80, 200 90 S 360 190, 460 130" fill="none" stroke="{C1}" stroke-width="7" stroke-linecap="round"/>']
    g.append(f'<circle cx="160" cy="34" r="11" fill="{C2}"/><text x="160" y="39" text-anchor="middle" font-size="15" fill="#fff" {FONT}>–</text>')
    g.append(f'<circle cx="168" cy="84" r="11" fill="{C1}" stroke="#fff"/><text x="168" y="89" text-anchor="middle" font-size="15" fill="#fff" {FONT}>+</text>')
    g.append(f'<line x1="161" y1="46" x2="166" y2="72" stroke="{C2}" stroke-width="2" stroke-dasharray="3 3"/>')
    g.append(f'<line x1="290" y1="88" x2="236" y2="92" stroke="{C3}" stroke-width="2.5" stroke-dasharray="5 4"/>')
    g.append(f'<line x1="102" y1="160" x2="104" y2="112" stroke="{C4}" stroke-width="4"/>')
    g.append(f'<ellipse cx="225" cy="140" rx="34" ry="18" fill="#F4C95D" opacity=".75"/>' + _t(225, 145, 'nonpolar', 12))
    o = [f'<g transform="translate(70,10)">{"".join(g)}</g>']
    o.append(_t(150, 22, 'ionic (Asp⁻ ··· Lys⁺)', 13, C2))
    o.append(_t(420, 86, 'hydrogen bond', 13, C3))
    o.append(_t(184, 146, 'S–S', 13, C4, 'start', '700') + _t(184, 162, '(Cys–Cys)', 11, C4, 'start'))
    o.append(_t(300, 222, 'dispersion forces / hydrophobic core', 12, '#8B6510'))
    return _svg(560, 232, ''.join(o))


def enzyme_models():
    """Lock-and-key (left) and induced fit (right)."""
    def enzyme(x, y, open_=True, col=C1):
        if open_:
            d = f'M{x} {y} h120 v80 h-120 v-28 h46 l14 -12 l-14 -12 h-46 Z'
        else:
            d = f'M{x} {y} h120 v80 h-120 v-28 h36 q20 -12 0 -24 h-36 Z'
        return f'<path d="{d}" fill="{col}" opacity=".9"/>'
    o = []
    # lock and key
    o.append(enzyme(40, 60) + f'<path d="M-6 0 h40 l14 12 l-14 12 h-40 Z" transform="translate(40,82)" fill="{C2}"/>')
    o.append(_t(150, 132, 'enzyme', 12, '#fff', 'end'))
    o.append(_t(60, 50, 'substrate', 12, C2))
    o.append(_t(100, 180, 'Lock and key', 15, INK, weight='700') + _t(100, 198, 'rigid active site fits the substrate', 12, MUTED))
    # induced fit: before and after
    o.append(f'<path d="M300 60 h120 v80 h-120 v-28 h30 q26 -12 0 -24 h-30 Z" fill="{C3}" opacity=".9"/>')
    o.append(f'<path d="M0 0 h40 l14 12 l-14 12 h-40 Z" transform="translate(250,82)" fill="{C2}"/>')
    o.append(f'<line x1="440" y1="100" x2="470" y2="100" stroke="{INK}" stroke-width="2"/><path d="M466 94 L476 100 L466 106 Z" fill="{INK}"/>')
    o.append(f'<path d="M490 60 h120 v80 h-120 v-28 h46 l14 -12 l-14 -12 h-46 Z" fill="{C3}" opacity=".9"/>')
    o.append(f'<path d="M0 0 h40 l14 12 l-14 12 h-40 Z" transform="translate(490,82)" fill="{C2}"/>')
    o.append(_t(455, 180, 'Induced fit', 15, INK, weight='700') + _t(455, 198, 'the active site changes shape as the substrate binds', 12, MUTED))
    return _svg(640, 210, ''.join(o))


def _axes(x0, y0, w, h, xl, yl):
    return (f'<line x1="{x0}" y1="{y0}" x2="{x0 + w}" y2="{y0}" stroke="{INK}" stroke-width="1.6"/>'
            f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 - h}" stroke="{INK}" stroke-width="1.6"/>'
            + _t(x0 + w / 2, y0 + 20, xl, 12, MUTED) + f'<text x="{x0 - 10}" y="{y0 - h / 2}" text-anchor="middle" font-size="12" fill="{MUTED}" {FONT} transform="rotate(-90 {x0 - 10} {y0 - h / 2})">{yl}</text>')


def rate_curves():
    """Rate against [substrate], temperature and pH."""
    o = []
    # [S]
    x0, y0, W, H = 40, 160, 180, 120
    o.append(_axes(x0, y0, W, H, '[substrate]', 'rate'))
    pts = [(x0 + W * t, y0 - H * 0.9 * (t * 4) / (1 + t * 4)) for t in [i / 40 for i in range(41)]]
    o.append('<polyline fill="none" stroke="%s" stroke-width="3" points="%s"/>' % (C1, ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)))
    o.append(f'<line x1="{x0}" y1="{y0 - H * 0.9 * 0.8}" x2="{x0 + W}" y2="{y0 - H * 0.9 * 0.8}" stroke="{MUTED}" stroke-dasharray="4 4"/>' + _t(x0 + W - 4, y0 - H * 0.9 * 0.8 - 8, 'enzyme saturated', 11, MUTED, 'end'))
    # temperature
    x1 = 280
    o.append(_axes(x1, y0, W, H, 'temperature (°C)', 'rate'))
    pts = []
    for i in range(41):
        T = i * 70 / 40
        r = (2 ** ((T - 37) / 10)) * (1 / (1 + math.exp((T - 45) / 2.5)))
        pts.append((x1 + W * T / 70, y0 - H * 0.85 * r / 1.05))
    o.append('<polyline fill="none" stroke="%s" stroke-width="3" points="%s"/>' % (C2, ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)))
    o.append(_t(x1 + W * 37 / 70, y0 - H - 4, 'optimum ≈ 37 °C', 11, C2) + _t(x1 + W * 60 / 70, y0 - 50, 'denatured', 11, MUTED))
    # pH
    x2 = 520
    o.append(_axes(x2, y0, W, H, 'pH', 'rate'))
    for opt, col, lab in ((2, C3, 'pepsin'), (8, C4, 'trypsin')):
        pts = [(x2 + W * p / 12, y0 - H * 0.85 * math.exp(-((p - opt) / 1.3) ** 2)) for p in [i * 12 / 60 for i in range(61)]]
        o.append('<polyline fill="none" stroke="%s" stroke-width="3" points="%s"/>' % (col, ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)))
        o.append(_t(x2 + W * opt / 12, y0 - H * 0.85 - 8, f'{lab} (pH {opt})', 11, col))
    return _svg(730, 190, ''.join(o))


def inhibition():
    """Competitive (inhibitor in the active site) vs noncompetitive (inhibitor elsewhere changes the site)."""
    o = []
    # competitive
    o.append(f'<path d="M40 50 h130 v90 h-130 v-32 h48 l14 -13 l-14 -13 h-48 Z" fill="{C1}" opacity=".9"/>')
    o.append(f'<path d="M0 0 h42 l14 13 l-14 13 h-42 Z" transform="translate(40,82)" fill="{C4}"/>' + _t(22, 100, 'I', 15, C4, weight='700'))
    o.append(f'<path d="M0 0 h42 l14 13 l-14 13 h-42 Z" transform="translate(190,40)" fill="{C2}" opacity=".85"/>' + _t(214, 30, 'substrate (blocked)', 11, C2))
    o.append(_t(110, 170, 'Competitive', 15, INK, weight='700') + _t(110, 188, 'looks like the substrate; same site', 12, MUTED) + _t(110, 204, 'more substrate overcomes it', 12, MUTED))
    # noncompetitive
    o.append(f'<path d="M330 50 h130 v90 h-130 v-32 h40 q20 -13 0 -26 h-40 Z" fill="{C3}" opacity=".9"/>')
    o.append(f'<circle cx="440" cy="50" r="14" fill="{C4}"/>' + _t(440, 55, 'I', 14, '#fff', weight='700'))
    o.append(f'<path d="M0 0 h42 l14 13 l-14 13 h-42 Z" transform="translate(270,82)" fill="{C2}" opacity=".85"/>' + _t(296, 74, 'no fit', 11, C2))
    o.append(_t(400, 170, 'Noncompetitive', 15, INK, weight='700') + _t(400, 188, 'binds elsewhere (allosteric site)', 12, MUTED) + _t(400, 204, 'changes the active site shape', 12, MUTED))
    return _svg(520, 214, ''.join(o))


def feedback():
    """A → B → C → D, with D inhibiting enzyme 1."""
    o = []
    xs = [40, 190, 340, 490]
    for x, lab in zip(xs, 'ABCD'):
        o.append(f'<circle cx="{x}" cy="90" r="24" fill="{SOFT}" stroke="{C1}" stroke-width="2"/>' + _t(x, 96, lab, 18, C1, weight='700'))
    for i in range(3):
        a, b = xs[i] + 28, xs[i + 1] - 28
        o.append(f'<line x1="{a}" y1="90" x2="{b - 6}" y2="90" stroke="{INK}" stroke-width="2"/><path d="M{b - 8} 84 L{b} 90 L{b - 8} 96 Z" fill="{INK}"/>')
        o.append(_t((a + b) / 2, 78, f'enzyme {i + 1}', 12, MUTED))
    o.append(f'<path d="M490 118 C 490 175, 115 175, 115 104" fill="none" stroke="{C2}" stroke-width="2.4" stroke-dasharray="6 4"/>')
    o.append(f'<line x1="104" y1="104" x2="126" y2="104" stroke="{C2}" stroke-width="4"/>')
    o.append(_t(300, 172, 'too much D switches off enzyme 1', 13, C2))
    return _svg(540, 190, ''.join(o))
