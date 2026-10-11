"""PHD125 Chapter 1 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

LOS = [
    ['CH1-LO1', 'Explain why carbon forms so many compounds, and how organic and inorganic compounds differ'],
    ['CH1-LO2', 'Draw and convert between molecular, expanded, condensed and line-angle formulas'],
    ['CH1-LO3', 'Identify the main functional groups in a structure, including common drugs'],
    ['CH1-LO4', 'Explain why a natural and a synthetic sample of the same compound behave identically'],
    ['CH1-LO5', 'Give examples of how organic compounds and their functional groups matter in medicines and consumer products'],
]


def aspartame_hands():
    smi = 'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O'
    m = Chem.MolFromSmiles(smi); AllChem.Compute2DCoords(m)
    W, H = 440, 300
    d = rdMolDraw2D.MolDraw2DSVG(W, H); o = d.drawOptions(); o.bondLineWidth = 2; o.minFontSize = 15
    o.setBackgroundColour((1, 1, 1, 0))
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing()
    svg = d.GetDrawingText().replace("<?xml version='1.0' encoding='iso-8859-1'?>", '').strip()
    svg = svg.replace("<svg version='1.1'", "<svg role='img' aria-label='Structure of aspartame with five functional groups lettered A to E' version='1.1'", 1)
    groups = [('acid', '[CX3](=O)[OX2H1]'), ('amine', '[CX4][NX3H2]'), ('amide', '[NX3][CX3](=O)'), ('ester', '[CX3](=O)[OX2][CH3]'), ('ring', 'c1ccccc1')]
    zones = []
    for i, (k, sm) in enumerate(groups):
        mt = m.GetSubstructMatches(Chem.MolFromSmarts(sm))[0]
        pts = [d.GetDrawCoords(a) for a in mt]
        zones.append({'id': 'ABCDE'[i], 'x': round(100 * sum(p.x for p in pts) / len(pts) / W, 1), 'y': round(100 * sum(p.y for p in pts) / len(pts) / H, 1)})
    return {
        'lo': 'CH1-LO3', 'title': 'Label the functional groups in aspartame',
        'how': 'Aspartame is the sweetener in many diet drinks. Drag a label onto each lettered group, or tap a label and then tap a letter. Two labels do not belong anywhere.',
        'svg': svg, 'zones': zones,
        'chips': [
            {'t': 'carboxylic acid', 's': '–COOH', 'z': 0},
            {'t': 'amine', 's': '–NH₂, no C=O', 'z': 1},
            {'t': 'amide', 's': 'N bonded to C=O', 'z': 2},
            {'t': 'ester', 's': '–COO–CH₃', 'z': 3},
            {'t': 'aromatic ring', 's': 'benzene ring', 'z': 4},
            {'t': 'aldehyde', 's': '–CHO', 'z': -1},
            {'t': 'ether', 's': 'C–O–C', 'z': -1}],
        'why': 'Aspartame has five functional groups: a carboxylic acid (A), an amine (B), an amide linking its two amino acids (C), a methyl ester (D) and an aromatic ring (E). It has no aldehyde or ether. The ester and amide can be hydrolysed, which is why diet drinks lose sweetness over time.'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    # LO1
    q('CH1-LO1', 'Chemistry tutor', 'What is organic?', 'Organic chemistry today is the study of:', ['Compounds that contain carbon', 'Compounds made only by living things', 'Compounds grown without pesticides', 'Compounds that contain oxygen'], 'Since Wöhler (1828), "organic" means carbon-based, whatever the source.')
    q('CH1-LO1', 'Encik Lim', 'Antacid shelf', '"Sodium bicarbonate has carbon in it. So it is organic, right?"', ['No: carbonates and bicarbonates are treated as inorganic', 'Yes: anything with carbon is organic', 'Yes, because it is a medicine', 'No, because it has no hydrogen'], 'CO, CO<sub>2</sub>, carbonates, bicarbonates and cyanides are the conventional exceptions.')
    q('CH1-LO1', 'Chemistry tutor', 'History', 'What did Wöhler make in 1828 from ammonium cyanate?', ['Urea', 'Aspirin', 'Methane', 'Glucose'], 'Urea, an organic compound found in urine, made from an inorganic salt: the start of the end of vitalism.')
    q('CH1-LO1', 'Chemistry tutor', 'Carbon bonds', 'How many covalent bonds does carbon form in a neutral molecule?', ['4', '2', '3', '6'], 'Four valence electrons → four bonds (single, double or triple, adding up to four).')
    q('CH1-LO1', 'Lab assistant', 'Mystery powder', 'A white powder melts at 150 °C and burns with a smoky flame. It is most likely:', ['Organic', 'Ionic', 'A metal', 'Inorganic salt'], 'Low melting and flammable: typical organic properties.')
    q('CH1-LO1', 'Pharmacy student', 'Solubility', 'Why does petrol not mix with water?', ['Hydrocarbons are nonpolar', 'Petrol is ionic', 'Water is nonpolar', 'Petrol is a metal'], 'C–H bonds are nonpolar, so hydrocarbons do not mix with polar water.')
    # LO2
    q('CH1-LO2', 'Chemistry tutor', 'Formulas', 'What is the molecular formula of CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>?', ['C<sub>4</sub>H<sub>10</sub>', 'C<sub>4</sub>H<sub>8</sub>', 'C<sub>3</sub>H<sub>10</sub>', 'C<sub>4</sub>H<sub>12</sub>'], '4 C; 3 + 2 + 2 + 3 = 10 H.')
    q('CH1-LO2', 'Chemistry tutor', 'Line structures', 'In a line structure, what does each corner and line end stand for?', ['A carbon atom', 'A hydrogen atom', 'An oxygen atom', 'A lone pair'], 'Ends and bends are carbons; H on carbon is hidden.')
    q('CH1-LO2', 'Chemistry tutor', 'Hidden hydrogens', 'A carbon in a line structure has three lines meeting at it. How many H does it carry?', ['1', '0', '2', '3'], '4 − 3 bonds = 1 H.')
    q('CH1-LO2', 'Chemistry tutor', 'Shapes', 'What is the bond angle around a carbon with four single bonds?', ['109.5°', '90°', '120°', '180°'], 'Four electron groups → tetrahedral.')
    q('CH1-LO2', 'Chemistry tutor', 'Shapes', 'What shape is the carbon in ethyne, HC≡CH?', ['Linear, 180°', 'Tetrahedral, 109.5°', 'Trigonal planar, 120°', 'Bent, 104.5°'], 'A triple bond + one single bond = two electron groups → linear.')
    q('CH1-LO2', 'Chemistry tutor', 'Ring', 'A hexagon on its own in a line structure is:', ['Cyclohexane, C<sub>6</sub>H<sub>12</sub>', 'Benzene, C<sub>6</sub>H<sub>6</sub>', 'Hexane, C<sub>6</sub>H<sub>14</sub>', 'Six hydrogen atoms'], 'Six CH<sub>2</sub> groups. Benzene would show alternating double bonds.')
    # LO3
    q('CH1-LO3', 'Chemistry tutor', 'Functional groups', 'Which family contains –OH on a carbon chain?', ['Alcohol', 'Carboxylic acid', 'Ether', 'Aldehyde'], 'R–OH is an alcohol. –OH on a benzene ring would be a phenol.')
    q('CH1-LO3', 'Chemistry tutor', 'C=O families', 'C=O with an H on the carbonyl carbon is:', ['An aldehyde', 'A ketone', 'An ester', 'An amide'], '–CHO = aldehyde.')
    q('CH1-LO3', 'Pharmacist', 'Aspirin', 'Which pair of groups does aspirin contain besides its aromatic ring?', ['Carboxylic acid and ester', 'Amide and phenol', 'Amine and ketone', 'Alcohol and ether'], 'Aspirin = acetylsalicylic acid: –COOH and an ester.', rx=True)
    q('CH1-LO3', 'Pharmacist', 'Paracetamol', 'Paracetamol contains an aromatic ring, a phenol and:', ['An amide', 'An ester', 'A carboxylic acid', 'An aldehyde'], 'The N is bonded to a C=O: an amide.', rx=True)
    q('CH1-LO3', 'Chemistry tutor', 'Amine or amide?', 'An –NH<sub>2</sub> with no C=O beside it is:', ['An amine', 'An amide', 'A nitrile', 'An ester'], 'An amide needs the N bonded to a carbonyl carbon.')
    q('CH1-LO3', 'Chemistry tutor', 'Sulfur', 'The –SH group is called a:', ['Thiol', 'Sulfide', 'Disulfide', 'Sulfate'], 'R–SH = thiol (Chapter 3).')
    q('CH1-LO3', 'Chemistry tutor', 'Ketone', 'CH<sub>3</sub>COCH<sub>3</sub> (acetone) is a:', ['Ketone', 'Aldehyde', 'Ester', 'Ether'], 'C=O between two carbons.')
    # LO4
    q('CH1-LO4', 'Puan Aisyah', 'Vitamin C', '"Is natural vitamin C better than the synthetic one?"', ['They are the same molecule and work the same way', 'Natural is always stronger', 'Synthetic is a different molecule', 'Natural vitamin C is not organic'], 'Ascorbic acid is ascorbic acid, from an orange or a factory.')
    q('CH1-LO4', 'Encik Ravi', 'Herbal tea', '"It is natural, so it cannot harm me, right?"', ['Not necessarily: safety depends on the molecules and doses, not the source', 'Yes, natural products are always safe', 'Yes, plants contain no chemicals', 'No, natural products never work'], 'Digoxin (foxglove) is natural and toxic in overdose.')
    q('CH1-LO4', 'Pharmacy student', 'Purity', 'What <b>can</b> differ between a natural extract and a pure synthetic drug?', ['The other compounds present and the dose', 'The structure of the active molecule', 'The number of bonds to carbon', 'The molecular formula of the active molecule'], 'An extract contains many compounds; the active molecule itself is identical.')
    q('CH1-LO4', 'Chemistry tutor', 'Identity', 'What defines a compound?', ['Its structure', 'Where it was made', 'Its price', 'Its colour of packaging'], 'Same structure = same compound = same properties.')
    # LO5
    q('CH1-LO5', 'Encik Hafiz', 'Flu remedies', '"I take Panadol and a flu tablet with paracetamol 500 mg. Is that fine?"', ['No: both contain paracetamol, so check the total dose', 'Yes: they are different brands', 'Yes: paracetamol is natural', 'No: flu tablets never contain paracetamol'], 'Always check generic names. Usual adult maximum: 4 g in 24 hours.')
    q('CH1-LO5', 'Pharmacist', 'Old tablets', 'Old aspirin smells of vinegar because its ester has been:', ['Hydrolysed by moisture, releasing acetic acid', 'Oxidised to an aldehyde', 'Turned into an amide', 'Evaporated'], 'Aspirin + water → salicylic acid + acetic acid.', rx=True)
    q('CH1-LO5', 'Pharmacist', 'Drug names', 'Which is the generic name?', ['Paracetamol', 'Panadol', 'N-(4-hydroxyphenyl)acetamide', 'Tylenol'], 'Generic = the official non-brand name used in prescribing.', rx=True)
    q('CH1-LO5', 'Pharmacy student', 'Drugs from nature', 'Artemisinin, used against malaria, comes from:', ['Sweet wormwood', 'The opium poppy', 'Penicillium mould', 'Willow bark'], 'Artemisia annua; Tu Youyou received the 2015 Nobel Prize for this discovery.')
    q('CH1-LO5', 'Mak Cik Zaleha', 'Diet drinks', '"Why does my diet drink say it contains phenylalanine?"', ['Its sweetener, aspartame, breaks down to phenylalanine, which PKU patients must avoid', 'It contains sugar', 'It contains caffeine', 'It is a legal requirement for all drinks'], 'Aspartame is a dipeptide methyl ester of aspartic acid and phenylalanine.')
    q('CH1-LO5', 'Pharmacy student', 'Willow bark', 'Aspirin was made gentler than salicylic acid by changing:', ['The phenol –OH into an ester', 'The ring into a chain', 'The acid into an amine', 'Nothing: they are the same'], 'Acetylation of the –OH gave acetylsalicylic acid (1897).')
    return B


def config():
    return {
        'topic': 'ch1', 'title': 'Chapter 1 game',
        'kicker': 'PHD125 · Chapter 1 · Introduction to Organic Molecule',
        'blurb': 'You are the pharmacist on duty. Patients bring questions about natural remedies, drug names, old tablets and diet drinks. Every answer comes back to carbon and its functional groups. Five stations, about 8 minutes.',
        'hub': '../../#ch1', 'slides': '../slides/', 'board': '../../leaderboard/#ch1',
        'los': LOS,
        'levels': [
            {'id': 'counter', 'name': 'Front counter', 'blurb': 'Organic or not, and why carbon is special.', 'intro': 'The morning queue. Customers ask what "organic" really means and why some carbon compounds are not organic.', 'pool': ['CH1-LO1'], 'n': 5, 'secs': 30},
            {'id': 'board', 'name': 'Drawing board', 'blurb': 'Formulas, line structures and shapes.', 'intro': 'The new intern is learning to read structures in the drug reference. Help with formulas, hidden hydrogens and shapes.', 'pool': ['CH1-LO2'], 'n': 5, 'secs': 35},
            {'id': 'label', 'name': 'Label check', 'type': 'drag', 'blurb': 'Hands-on: label the functional groups in a sweetener.', 'intro': 'A customer with phenylketonuria asks about the sweetener in her drink. Label the functional groups in aspartame.', 'secs': 75},
            {'id': 'shelf', 'name': 'Remedies shelf', 'blurb': 'Functional groups, natural vs synthetic, drug names.', 'intro': 'Questions from the shelves: natural or synthetic, which group is where, and what the label really says.', 'pool': ['CH1-LO3', 'CH1-LO4', 'CH1-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': aspartame_hands(),
        'bank': bank(),
    }
