"""PHD125 Chapter 8 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""

LOS = [
    ['CH8-LO1', 'Explain the principle of chromatography and read a chromatogram'],
    ['CH8-LO2', 'Choose stationary and mobile phases and predict elution order'],
    ['CH8-LO3', 'Carry out TLC and calculate and interpret R<sub>f</sub>'],
    ['CH8-LO4', 'Describe ion exchange, HPLC and GC'],
    ['CH8-LO5', 'Apply chromatography to pharmaceutical analysis'],
]


def tlc_bench():
    """A developed plate: front at 10.0 cm, four spots with their distances. Students drop the R_f on each."""
    W, H = 440, 300
    org, top = 272, 42
    cm = (org - top) / 10.0
    spots = [(140, 2.0, '#E4572E'), (200, 4.5, '#2E7D4F'), (260, 6.0, '#2F6F9F'), (320, 8.5, '#B86E00')]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="A developed TLC plate with the solvent front at 10.0 cm and four spots, A to D, at 2.0, 4.5, 6.0 and 8.5 cm">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>',
         '<text x="220" y="22" text-anchor="middle" font-size="13" font-weight="700" font-family="sans-serif" fill="#B86E00">what is the R<tspan baseline-shift="sub" font-size="10">f</tspan> of each spot?</text>',
         f'<rect x="105" y="{top - 8}" width="270" height="{org - top + 22}" fill="#FBFBF7" stroke="#1B2A41" stroke-width="2"/>',
         f'<line x1="105" y1="{top}" x2="375" y2="{top}" stroke="#2F6F9F" stroke-width="2" stroke-dasharray="6 4"/>',
         f'<line x1="105" y1="{org}" x2="375" y2="{org}" stroke="#56657A" stroke-width="1.5" stroke-dasharray="4 3"/>',
         f'<text x="381" y="{top + 4}" font-size="11" font-family="sans-serif" fill="#2F6F9F">front</text>',
         f'<text x="381" y="{org + 4}" font-size="11" font-family="sans-serif" fill="#56657A">origin</text>',
         f'<line x1="80" y1="{top}" x2="80" y2="{org}" stroke="#2F6F9F" stroke-width="1.6"/>',
         f'<text x="74" y="{(top + org) / 2 + 4:.0f}" text-anchor="end" font-size="12" font-weight="700" font-family="sans-serif" fill="#2F6F9F">10.0 cm</text>']
    for x, d, c in spots:
        y = org - d * cm
        s.append(f'<ellipse cx="{x}" cy="{y:.1f}" rx="11" ry="7" fill="{c}"/>')
        s.append(f'<line x1="{x + 16}" y1="{y:.1f}" x2="{x + 16}" y2="{org}" stroke="{c}" stroke-width="1.2" stroke-dasharray="3 3"/>')
        s.append(f'<text x="{x + 20}" y="{(y + org) / 2 + 4:.0f}" font-size="11.5" font-weight="700" font-family="sans-serif" fill="{c}">{d:.1f}</text>')
    s.append('</svg>')
    zones = []
    for (x, d, c), z in zip(spots, 'ABCD'):
        y = org - d * cm
        zones.append({'id': z, 'x': round((x - 26) / W * 100, 1), 'y': round((y - 16) / H * 100, 1)})
    return {
        'lo': 'CH8-LO3', 'title': 'TLC bench: read the plate',
        'how': 'Distances (cm) are measured from the origin. Drag the correct R<sub>f</sub> onto each letter, or tap a value and then tap a letter. Two values do not belong anywhere.',
        'svg': ''.join(s),
        'zones': zones,
        'chips': [
            {'t': 'R<sub>f</sub> 0.20', 'z': 0},
            {'t': 'R<sub>f</sub> 0.45', 'z': 1},
            {'t': 'R<sub>f</sub> 0.60', 'z': 2},
            {'t': 'R<sub>f</sub> 0.85', 'z': 3},
            {'t': 'R<sub>f</sub> 5.0', 'z': -1},
            {'t': 'R<sub>f</sub> 1.20', 'z': -1}],
        'why': 'R<sub>f</sub> = distance moved by the spot ÷ distance moved by the solvent front, both from the origin, so it is always between 0 and 1. On silica the most polar compound is A (lowest R<sub>f</sub>) and the least polar is D.'}


def bank():
    B = []

    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx:
            it['rx'] = True
        B.append(it)
    q('CH8-LO1', 'Chemistry tutor', 'Phases', 'The phase that stays fixed in chromatography is the:', ['stationary phase', 'mobile phase', 'eluent', 'carrier gas'], 'The mobile phase moves.')
    q('CH8-LO1', 'Chemistry tutor', 'Principle', 'A component that prefers the stationary phase:', ['moves more slowly', 'moves faster', 'does not move at all', 'leaves first'], 'It is held back.')
    q('CH8-LO1', 'Chemistry tutor', 'Chromatogram', 'Peak area in a chromatogram tells you the:', ['amount of the component', 'identity of the component', 'void time', 'column length'], 'Retention time helps identify.')
    q('CH8-LO1', 'Chemistry tutor', 'Resolution', 'Baseline separation needs a resolution of at least:', ['1.5', '0.5', '0.1', '15'], 'Harvey 12.2.')
    q('CH8-LO1', 'Chemistry tutor', 'Retention factor', 't<sub>r</sub> = 6.0 min, t<sub>m</sub> = 1.0 min. k = ?', ['5.0', '6.0', '7.0', '0.17'], '(6.0 − 1.0) ÷ 1.0.')
    q('CH8-LO1', 'Chemistry tutor', 'History', 'Tswett first separated:', ['coloured plant pigments on a chalk column', 'amino acids on paper', 'gases in a capillary', 'proteins by size'], 'Hence "colour writing".')
    q('CH8-LO2', 'Chemistry tutor', 'Silica', 'Silica gel holds polar compounds by:', ['hydrogen bonding to its –OH groups', 'covalent bonds', 'ionic exchange of Na<sup>+</sup>', 'size exclusion'], 'Si–OH surface.')
    q('CH8-LO2', 'QC analyst', 'Reversed phase', 'On a C18 column with water–methanol, which comes out first?', ['the most polar compound', 'the least polar compound', 'the largest molecule', 'the most volatile'], 'C18 holds nonpolar compounds.', rx=True)
    q('CH8-LO2', 'Chemistry tutor', 'Polarity index', 'Which solvent is the most polar?', ['water', 'methanol', 'acetonitrile', 'hexane'], 'P′ = 10.2.')
    q('CH8-LO2', 'QC analyst', 'Gradient', 'Gradient elution in reversed phase usually:', ['increases the organic solvent during the run', 'increases the water during the run', 'keeps the solvent the same', 'heats the column only'], 'Late peaks come out sooner.', rx=True)
    q('CH8-LO2', 'Chemistry tutor', 'Weak solvent', 'Spots on silica all stay near the origin. Use a solvent that is:', ['more polar', 'less polar', 'more viscous', 'coloured'], 'A stronger eluent on silica.')
    q('CH8-LO3', 'Lab demonstrator', 'Origin', 'The TLC origin line is drawn in:', ['pencil', 'ink', 'marker pen', 'crayon'], 'Ink would run.')
    q('CH8-LO3', 'Lab demonstrator', 'Rf value', 'Spot 3.6 cm, front 9.0 cm. R<sub>f</sub> = ?', ['0.40', '2.5', '0.36', '5.4'], '3.6 ÷ 9.0.')
    q('CH8-LO3', 'Lab demonstrator', 'Visualising', 'Under UV 254 nm on an F<sub>254</sub> plate, aromatic compounds appear as:', ['dark spots on a green glow', 'purple spots', 'brown spots', 'invisible'], 'They quench the fluorescence.')
    q('CH8-LO3', 'Lab demonstrator', 'Co-spot', 'A co-spot of standard and sample gives two separate spots. This means:', ['they are different compounds', 'they are the same compound', 'the plate is wet', 'the solvent is too weak'], 'Same compounds would merge.')
    q('CH8-LO3', 'Lab demonstrator', 'Tank', 'The TLC tank has a lid to:', ['keep the air saturated with solvent vapour', 'keep out light', 'cool the plate', 'stop the spots fading'], 'Gives even, reproducible runs.')
    q('CH8-LO4', 'Chemistry tutor', 'Cation exchanger', 'A strong acid cation exchanger carries:', ['–SO<sub>3</sub><sup>−</sup>', '–COO<sup>−</sup>', '–N(CH<sub>3</sub>)<sub>3</sub><sup>+</sup>', '–NH<sub>3</sub><sup>+</sup>'], 'Sulfonic acid.')
    q('CH8-LO4', 'Chemistry tutor', 'Ion charge', 'On a cation exchanger, which is held most strongly?', ['Ca<sup>2+</sup>', 'Na<sup>+</sup>', 'K<sup>+</sup>', 'Li<sup>+</sup>'], 'Higher charge.')
    q('CH8-LO4', 'Renal pharmacist', 'Resin drug', 'Sodium polystyrene sulfonate lowers blood potassium by:', ['exchanging Na<sup>+</sup> for K<sup>+</sup> in the gut', 'binding bile acids', 'blocking an enzyme', 'denaturing proteins'], 'A cation-exchange resin.', rx=True)
    q('CH8-LO4', 'QC analyst', 'HPLC detector', 'The most common HPLC detector for drugs is:', ['UV/Vis', 'FID', 'ECD', 'TCD'], 'Most drugs absorb UV.', rx=True)
    q('CH8-LO4', 'QC analyst', 'Degassing', 'The HPLC mobile phase is degassed to:', ['avoid bubbles in the pump and detector', 'make it polar', 'cool it', 'remove the drug'], 'Bubbles cause noise and false peaks.', rx=True)
    q('CH8-LO4', 'Chemistry tutor', 'GC carrier', 'The GC carrier gas is:', ['inert, such as helium or nitrogen', 'oxygen', 'hydrogen chloride', 'steam'], 'It only carries the sample.')
    q('CH8-LO4', 'Chemistry tutor', 'GC sample', 'A GC sample must be:', ['volatile and stable when heated', 'a protein', 'an ionic salt', 'coloured'], 'It is vaporised in a hot injector.')
    q('CH8-LO5', 'QC manager', 'Assay', 'The amount of drug in each tablet is usually measured by:', ['HPLC', 'paper chromatography', 'iodine vapour', 'size exclusion'], 'Peak area against a standard.', rx=True)
    q('CH8-LO5', 'QC manager', 'Residual solvents', 'Traces of manufacturing solvents are measured by:', ['headspace GC', 'TLC with ninhydrin', 'ion exchange', 'UV only'], 'They are volatile.', rx=True)
    q('CH8-LO5', 'Forensic toxicologist', 'Blood alcohol', 'Blood alcohol is measured by:', ['GC', 'paper chromatography', 'ion exchange', 'size exclusion'], 'Ethanol is volatile.', rx=True)
    q('CH8-LO5', 'Regulatory officer', 'Adulteration', 'A hidden drug in a herbal product is confirmed by:', ['LC–MS or GC–MS', 'a smell test', 'colour of the capsule', 'paper chromatography alone'], 'MS identifies the molecule.', rx=True)
    q('CH8-LO5', 'Hospital pharmacist', 'TDM', 'Before HPLC of a drug in serum, the sample is cleaned up to:', ['remove proteins that would clog the column', 'make it volatile', 'colour it', 'raise the pH'], 'Solid-phase extraction (fluoxetine).', rx=True)
    q('CH8-LO5', 'QC manager', 'Stability', 'An HPLC run of old aspirin shows a growing salicylic acid peak. This shows:', ['the aspirin has hydrolysed', 'the aspirin is purer', 'a residual solvent', 'the column is new'], 'Ester hydrolysis (Chapter 4).', rx=True)
    return B


def config():
    return {
        'topic': 'ch8', 'title': 'Chapter 8 game',
        'kicker': 'PHD125 · Chapter 8 · Chromatographic Methods in Pharmaceutical Analysis',
        'blurb': 'You are on duty in the quality-control lab. Tablets, capsules, blood samples and a suspicious slimming product all need testing. Choose the method, read the plate, explain the result. Five stations, about 9 minutes.',
        'hub': '../../#ch8', 'slides': '../slides/', 'board': '../../leaderboard/#ch8',
        'los': LOS,
        'levels': [
            {'id': 'prin', 'name': 'Principles desk', 'blurb': 'Phases, chromatograms, k and resolution; choosing solvents.', 'intro': 'New analysts are being trained on how separations work.', 'pool': ['CH8-LO1', 'CH8-LO2'], 'n': 6, 'secs': 30},
            {'id': 'tlc', 'name': 'TLC corner', 'blurb': 'Running and reading TLC plates.', 'intro': 'Plates for identity tests are coming off the bench.', 'pool': ['CH8-LO3'], 'n': 5, 'secs': 30},
            {'id': 'bench', 'name': 'TLC bench', 'type': 'drag', 'blurb': 'Hands-on: calculate Rf for four spots.', 'intro': 'A developed plate is waiting. Measure each spot against the front.', 'secs': 75},
            {'id': 'inst', 'name': 'Instrument room', 'blurb': 'Ion exchange, HPLC, GC and pharmacy applications.', 'intro': 'Questions about columns, detectors and which method to use.', 'pool': ['CH8-LO4', 'CH8-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick samples, one from every outcome. Points ×1.5.', 'intro': 'An urgent batch has to be released today. One question per outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': tlc_bench(),
        'bank': bank(),
    }
