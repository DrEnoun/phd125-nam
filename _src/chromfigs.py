"""Schematic figures for PHD125 Chapter 8 (SVG data URIs): TLC tank and plate, column separation,
chromatogram, normal and reversed phase, ion exchangers, HPLC and GC instruments. Drawn by Dr. NAM."""
import math
from proteinfigs import _uri, _t, _svg, INK, MUTED, C1, C2, C3, C4, SOFT, FONT

AMBER = '#F0B24A'


def _arrow(x1, y1, x2, y2, col=INK, w=2, head=8):
    a = math.atan2(y2 - y1, x2 - x1)
    hx1, hy1 = x2 - head * math.cos(a - .45), y2 - head * math.sin(a - .45)
    hx2, hy2 = x2 - head * math.cos(a + .45), y2 - head * math.sin(a + .45)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"/>'
            f'<path d="M{x2:.1f} {y2:.1f} L{hx1:.1f} {hy1:.1f} L{hx2:.1f} {hy2:.1f} Z" fill="{col}"/>')


def _dim(x, y1, y2, label, col=INK, side='left'):
    """Vertical dimension line with arrows at both ends."""
    o = _arrow(x, (y1 + y2) / 2, x, y1 + 1, col, 1.6, 7) + _arrow(x, (y1 + y2) / 2, x, y2 - 1, col, 1.6, 7)
    dx = -8 if side == 'left' else 8
    anc = 'end' if side == 'left' else 'start'
    return o + _t(x + dx, (y1 + y2) / 2 + 5, label, 14, col, anc, '700')


def tlc():
    """(a) developing tank with plate; (b) developed plate with the distances used for Rf."""
    o = []
    # ---- (a) tank
    o.append(f'<rect x="40" y="50" width="190" height="220" rx="8" fill="#F4F8FB" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<rect x="32" y="40" width="206" height="14" rx="4" fill="{MUTED}"/>')
    o.append(_t(135, 34, 'lid (keeps the tank saturated)', 12, MUTED))
    o.append(f'<rect x="42" y="236" width="186" height="32" fill="#CFE3F3"/>')
    o.append(_t(135, 288, 'solvent (mobile phase)', 12, C1))
    # plate leaning
    o.append(f'<rect x="95" y="70" width="80" height="190" fill="#fff" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<line x1="95" y1="226" x2="175" y2="226" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    for x, c in ((112, C2), (135, C3), (158, C1)):
        o.append(f'<circle cx="{x}" cy="226" r="4.5" fill="{c}"/>')
    o.append(f'<rect x="95" y="160" width="80" height="76" fill="#CFE3F3" opacity=".45"/>')
    o.append(_arrow(190, 200, 190, 165, C1, 2))
    o.append(_t(198, 186, 'solvent', 11, C1, 'start') + _t(198, 199, 'rises', 11, C1, 'start'))
    o.append(_t(250, 228, 'origin above', 11, MUTED, 'start') + _t(250, 241, 'the solvent', 11, MUTED, 'start'))
    o.append(_t(135, 318, '(a) Developing the plate', 15, INK, weight='700'))
    # ---- (b) developed plate
    X = 420
    o.append(f'<rect x="{X}" y="40" width="190" height="250" fill="#fff" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<line x1="{X}" y1="70" x2="{X + 190}" y2="70" stroke="{C1}" stroke-width="2" stroke-dasharray="6 4"/>')
    o.append(_t(X + 196, 74, 'solvent front', 12, C1, 'start'))
    o.append(f'<line x1="{X}" y1="262" x2="{X + 190}" y2="262" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    o.append(_t(X + 196, 266, 'origin (pencil)', 12, MUTED, 'start'))
    lanes = [(X + 45, [(150, C2)], 'S'), (X + 95, [(150, C2), (205, C3)], 'T'), (X + 145, [(150, C2), (205, C3)], 'C')]
    for x, spots, lab in lanes:
        for y, c in spots:
            o.append(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="8" fill="{c}" opacity=".9"/>')
        o.append(_t(x, 284, lab, 13, INK, weight='700'))
    o.append(_dim(X - 18, 150, 262, 'a'))
    o.append(_dim(X - 52, 70, 262, 'b'))
    o.append(_t(X + 95, 318, '(b) Developed plate:  R<tspan baseline-shift="sub" font-size="11">f</tspan> = a ÷ b', 15, INK, weight='700'))
    o.append(_t(X + 95, 340, 'S = standard drug · T = test sample · C = co-spot (S + T)', 12, MUTED))
    return _svg(720, 352, ''.join(o))


def column():
    """A mixture separating as it moves down a column (three moments in time)."""
    o = []
    xs = (90, 250, 410)
    bands = [[], [(105, 22, C2), (150, 22, C1)], [(150, 22, C2), (240, 22, C1)]]
    labels = ['load the sample', 'bands begin to separate', 'A elutes first']
    for i, x in enumerate(xs):
        o.append(f'<rect x="{x - 26}" y="40" width="52" height="250" rx="6" fill="#F7F2E6" stroke="{INK}" stroke-width="2"/>')
        o.append(f'<path d="M{x - 26} 290 L{x - 6} 312 L{x + 6} 312 L{x + 26} 290" fill="#F7F2E6" stroke="{INK}" stroke-width="2"/>')
        if i == 0:
            o.append(f'<rect x="{x - 25}" y="56" width="50" height="22" fill="{C4}" opacity=".85"/>')
        else:
            for (y, h, c) in bands[i]:
                o.append(f'<rect x="{x - 25}" y="{y}" width="50" height="{h}" fill="{c}" opacity=".85"/>')
        o.append(_t(x, 336, labels[i], 13, INK))
    o.append(_arrow(520, 60, 520, 260, C1, 3, 12))
    o.append(_t(532, 130, 'mobile phase', 13, C1, 'start', '700') + _t(532, 148, 'flows down', 13, C1, 'start'))
    o.append(f'<rect x="530" y="190" width="14" height="14" fill="{C1}"/>' + _t(550, 202, 'A: weakly held', 12, INK, 'start'))
    o.append(f'<rect x="530" y="214" width="14" height="14" fill="{C2}"/>' + _t(550, 226, 'B: strongly held', 12, INK, 'start'))
    o.append(_t(537, 254, 'stationary phase packed', 12, MUTED, 'start') + _t(537, 270, 'in the column (beige)', 12, MUTED, 'start'))
    return _svg(720, 350, ''.join(o))


def _gauss(x0, tr, w, hgt, base, sx):
    sd = w / 4
    pts = []
    for k in range(-60, 61):
        t = tr + k * sd * 4 / 60
        pts.append((x0 + t * sx, base - hgt * math.exp(-((t - tr) ** 2) / (2 * sd * sd))))
    return pts


def chromatogram():
    """Detector signal against time with the void time, retention times and peak widths."""
    x0, base, sx = 70, 250, 60
    o = [f'<line x1="{x0}" y1="{base}" x2="{x0 + 600}" y2="{base}" stroke="{INK}" stroke-width="2"/>',
         f'<line x1="{x0}" y1="{base}" x2="{x0}" y2="40" stroke="{INK}" stroke-width="2"/>',
         _t(x0 + 300, base + 44, 'time after injection (min)', 13, MUTED),
         f'<text x="30" y="150" transform="rotate(-90 30 150)" text-anchor="middle" font-size="13" fill="{MUTED}" {FONT}>detector signal</text>']
    peaks = [(1.0, .35, 50, MUTED), (4.0, .8, 170, C1), (7.0, 1.0, 130, C2)]
    allp = []
    t = 0
    while t <= 10:
        y = base
        for tr, w, h, c in peaks:
            sd = w / 4
            y -= h * math.exp(-((t - tr) ** 2) / (2 * sd * sd))
        allp.append((x0 + t * sx, y))
        t += 0.02
    o.append('<polyline fill="none" stroke="%s" stroke-width="2.5" points="%s"/>' % (INK, ' '.join(f'{x:.1f},{y:.1f}' for x, y in allp)))
    o.append(_t(x0 + 1.0 * sx, base - 58, 't<tspan baseline-shift="sub" font-size="10">m</tspan>', 14, MUTED, weight='700'))
    o.append(_t(x0 + 1.0 * sx, base - 76, 'unretained', 11, MUTED))
    # retention times
    for tr, w, h, c, nm in ((4.0, .8, 170, C1, 'A'), (7.0, 1.0, 130, C2, 'B')):
        x = x0 + tr * sx
        o.append(f'<line x1="{x}" y1="{base - h}" x2="{x}" y2="{base}" stroke="{c}" stroke-width="1.4" stroke-dasharray="4 3"/>')
        o.append(_t(x + 16, base - h + 6, f'peak {nm}', 14, c, 'start', '700'))
        # width at base
        o.append(f'<line x1="{x - w / 2 * sx}" y1="{base + 8}" x2="{x + w / 2 * sx}" y2="{base + 8}" stroke="{c}" stroke-width="2"/>')
        o.append(_t(x, base + 24, f'w<tspan baseline-shift="sub" font-size="10">{nm}</tspan>', 13, c, weight='700'))
    # tr arrows from injection
    for tr, y, c, nm in ((4.0, 50, C1, 'A'), (7.0, 28, C2, 'B')):
        o.append(_arrow(x0 + 2, y, x0 + tr * sx - 2, y, c, 1.6, 7))
        o.append(_t(x0 + tr * sx + 8, y + 5, f't<tspan baseline-shift="sub" font-size="10">r</tspan>({nm})', 13, c, 'start', '700'))
    o.append(_t(x0, base + 24, 'inject', 11, MUTED))
    return _svg(700, 300, ''.join(o))


def phases():
    """Normal phase (polar silica) and reversed phase (C18) side by side."""
    o = []
    for i, (x, title, sub, kind) in enumerate(((20, 'Normal phase', 'polar stationary phase, less polar solvent', 'np'),
                                                (370, 'Reversed phase', 'nonpolar stationary phase, polar solvent', 'rp'))):
        o.append(f'<rect x="{x}" y="160" width="330" height="40" fill="#E9E2D0" stroke="{INK}" stroke-width="1.5"/>')
        o.append(_t(x + 165, 186, 'silica particle surface', 12, MUTED))
        for k in range(6):
            sx = x + 30 + k * 54
            if kind == 'np':
                o.append(f'<line x1="{sx}" y1="160" x2="{sx}" y2="140" stroke="{INK}" stroke-width="2"/>')
                o.append(_t(sx, 134, 'OH', 13, C2, weight='700'))
            else:
                pts = ' '.join(f'{sx + (5 if j % 2 else -5)},{160 - j * 9}' for j in range(8))
                o.append(f'<polyline points="{pts}" fill="none" stroke="{MUTED}" stroke-width="2"/>')
        o.append(_t(x + 165, 30, title, 17, C1 if kind == 'np' else C3, weight='700'))
        o.append(_t(x + 165, 50, sub, 12, MUTED))
        o.append(_t(x + 165, 226, 'Si–OH (silica gel)' if kind == 'np' else 'Si–C18 chains (octadecyl, ODS)', 13, INK, weight='700'))
        o.append(_t(x + 165, 248, 'polar solutes held longer' if kind == 'np' else 'nonpolar solutes held longer', 13, INK))
        o.append(_t(x + 165, 268, 'less polar solutes elute first' if kind == 'np' else 'more polar solutes elute first', 13, C2, weight='700'))
        o.append(_t(x + 165, 288, 'e.g. TLC on silica with hexane–ethyl acetate' if kind == 'np' else 'e.g. HPLC with water–methanol or acetonitrile', 12, MUTED))
    o.append(f'<line x1="355" y1="20" x2="355" y2="295" stroke="#D5DCE4" stroke-width="1.5"/>')
    # solute dots
    o.append(f'<circle cx="80" cy="96" r="10" fill="{C2}"/>' + _t(96, 100, 'polar', 11, C2, 'start'))
    o.append(f'<circle cx="230" cy="82" r="10" fill="{C1}"/>' + _t(246, 86, 'nonpolar', 11, C1, 'start'))
    o.append(f'<circle cx="430" cy="70" r="10" fill="{C2}"/>' + _t(446, 74, 'polar', 11, C2, 'start'))
    o.append(f'<circle cx="590" cy="76" r="10" fill="{C1}"/>' + _t(606, 80, 'nonpolar', 11, C1, 'start'))
    return _svg(720, 300, ''.join(o))


def ion_exchange():
    """Cation-exchange and anion-exchange beads with their fixed groups and exchangeable counter-ions."""
    o = []
    for cx, title, fixed, ion, inc, col, sub in ((180, 'Cation exchanger', 'SO₃⁻', 'Na⁺', 'Ca²⁺', C1, 'strong acid: –SO₃⁻   weak acid: –COO⁻'),
                                                 (540, 'Anion exchanger', 'NR₃⁺', 'Cl⁻', 'SO₄²⁻', C2, 'strong base: –N(CH₃)₃⁺   weak base: –NH₃⁺')):
        o.append(f'<circle cx="{cx}" cy="185" r="78" fill="#F7F2E6" stroke="{INK}" stroke-width="2.5"/>')
        o.append(_t(cx, 189, 'resin bead', 12, MUTED))
        o.append(_t(cx, 205, '(polystyrene–DVB)', 11, MUTED))
        for k in range(8):
            a = k * math.pi / 4 + .2
            x1, y1 = cx + 78 * math.cos(a), 185 + 78 * math.sin(a)
            x2, y2 = cx + 98 * math.cos(a), 185 + 98 * math.sin(a)
            o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="1.5"/>')
            o.append(_t(x2 + 8 * math.cos(a), y2 + 8 * math.sin(a) + 4, fixed, 11, col, weight='700'))
        o.append(_t(cx, 30, title, 17, col, weight='700'))
        o.append(_t(cx, 318, sub, 12, INK))
        # exchange arrows
        o.append(f'<rect x="{cx + 102}" y="44" width="54" height="22" rx="11" fill="{AMBER}"/>' + _t(cx + 129, 60, inc, 13, INK, weight='700'))
        o.append(_arrow(cx + 129, 68, cx + 92, 112, INK, 1.5, 7))
        o.append(f'<rect x="{cx - 160}" y="44" width="50" height="22" rx="11" fill="#DCE8F2"/>' + _t(cx - 135, 60, ion, 13, INK, weight='700'))
        o.append(_arrow(cx - 90, 112, cx - 126, 68, INK, 1.5, 7))
        o.append(_t(cx + 129, 38, 'binds', 11, MUTED) + _t(cx - 135, 38, 'released', 11, MUTED))
    return _svg(720, 330, ''.join(o))


def _blocks(items, y=70, h=70, gap=22, w=None, x0=20):
    o = []
    n = len(items)
    w = w or (680 - gap * (n - 1)) / n
    for i, (name, sub, col) in enumerate(items):
        x = x0 + i * (w + gap)
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="10" fill="{col}" opacity=".16" stroke="{col}" stroke-width="2"/>')
        o.append(_t(x + w / 2, y + 30, name, 14, INK, weight='700'))
        for j, s in enumerate(sub):
            o.append(_t(x + w / 2, y + h + 18 + j * 16, s, 11, MUTED))
        if i < n - 1:
            o.append(_arrow(x + w + 2, y + h / 2, x + w + gap - 2, y + h / 2, INK, 2, 7))
    return o


def hplc():
    o = _blocks([('Solvent', ['mobile phase,', 'filtered, degassed'], C1),
                 ('Pump', ['high pressure,', 'steady flow'], C4),
                 ('Injector', ['loop: fixed', 'volume (µL)'], C3),
                 ('Column', ['C18, 3–10 µm', 'silica, 5–30 cm'], C2),
                 ('Detector', ['UV/Vis, fluorescence,', 'RI, MS'], C1),
                 ('Data', ['chromatogram:', 'tᵣ and peak area'], MUTED)])
    o.append(_t(360, 34, 'High-performance liquid chromatography (HPLC): liquid mobile phase pushed through a packed column', 13, INK, weight='700'))
    return _svg(720, 190, ''.join(o))


def gc():
    o = _blocks([('Carrier gas', ['He, N₂ or Ar', '(inert)'], C1),
                 ('Injector', ['heated; sample', 'vaporised (µL)'], C3),
                 ('Column', ['in a heated oven;', 'capillary 15–100 m'], C2),
                 ('Detector', ['FID, TCD,', 'ECD, MS'], C4),
                 ('Data', ['chromatogram:', 'tᵣ and peak area'], MUTED)])
    o.append(f'<rect x="282" y="56" width="164" height="136" rx="12" fill="none" stroke="{C2}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    o.append(_t(364, 50, 'oven (temperature programme)', 11, C2))
    o.append(_t(360, 22, 'Gas chromatography (GC): gas mobile phase; sample must be volatile and heat-stable', 13, INK, weight='700'))
    return _svg(720, 200, ''.join(o))


def rf_example():
    """A worked-example plate: front at 8.0 cm, spots at 2.0 and 5.6 cm."""
    o = []
    X, top, org = 260, 40, 290
    cm = (org - top) / 8.0
    o.append(f'<rect x="{X}" y="{top - 14}" width="200" height="{org - top + 40}" fill="#fff" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<line x1="{X}" y1="{top}" x2="{X + 200}" y2="{top}" stroke="{C1}" stroke-width="2" stroke-dasharray="6 4"/>')
    o.append(f'<line x1="{X}" y1="{org}" x2="{X + 200}" y2="{org}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    for d, c, nm in ((2.0, C2, 'P'), (5.6, C3, 'Q')):
        y = org - d * cm
        o.append(f'<ellipse cx="{X + 100}" cy="{y:.1f}" rx="14" ry="9" fill="{c}"/>')
        o.append(_t(X + 124, y + 5, nm, 14, c, 'start', '700'))
    o.append(_dim(X - 20, org - 2.0 * cm, org, '2.0 cm', C2))
    o.append(_dim(X - 100, org - 5.6 * cm, org, '5.6 cm', C3))
    o.append(_dim(X + 240, top, org, '8.0 cm', C1, 'right'))
    o.append(_t(X + 206, top + 4, 'front', 11, C1, 'start') + _t(X + 206, org + 4, 'origin', 11, MUTED, 'start'))
    return _svg(720, 340, ''.join(o))
