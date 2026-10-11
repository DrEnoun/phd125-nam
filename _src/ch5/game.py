"""PHD125 Chapter 5 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
from sugars import haworth, disaccharide, sucrose, GLC

LOS = [
    ['CH5-LO1', 'Classify carbohydrates, identify chiral carbons and enantiomers, and explain why chirality matters for drugs'],
    ['CH5-LO2', 'Classify monosaccharides, draw Fischer projections, and assign them as D or L'],
    ['CH5-LO3', 'Draw Haworth projections, identify α and β anomers, and explain mutarotation'],
    ['CH5-LO4', 'Describe the reactions of monosaccharides: reducing sugars, sugar alcohols, glycosides'],
    ['CH5-LO5', 'Describe the common disaccharides and polysaccharides'],
]


def test_bench():
    W, H = 440, 300
    def emb(uri, x, y, w=170, h=82):
        return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{uri}"/>'
    lab = lambda x, y, s: f'<text x="{x}" y="{y}" text-anchor="middle" font-size="12.5" font-family="sans-serif" fill="#1B2A41">{s}</text>'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Four samples lettered A to D: glucose with Benedict\'s reagent, sucrose with Benedict\'s reagent, starch (amylose) with iodine, and cotton (cellulose) with iodine">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>',
         '<text x="220" y="22" text-anchor="middle" font-size="13" font-weight="700" font-family="sans-serif" fill="#B86E00">what colour do you see?</text>',
         '<line x1="220" y1="34" x2="220" y2="290" stroke="#D7E0E8"/><line x1="10" y1="160" x2="430" y2="160" stroke="#D7E0E8"/>',
         emb(haworth(GLC('b')), 30, 52), lab(115, 148, 'glucose + Benedict\'s, warm'),
         emb(sucrose(), 250, 52), lab(335, 148, 'sucrose + Benedict\'s, warm'),
         emb(disaccharide(GLC('a'), GLC('a'), 'a'), 30, 182), lab(115, 278, 'starch (amylose) + iodine'),
         emb(disaccharide(GLC('b'), GLC('b'), 'b'), 250, 182), lab(335, 278, 'cotton (cellulose) + iodine'), '</svg>']
    return {
        'lo': 'CH5-LO4', 'title': 'Test bench: predict each colour',
        'how': 'Each sample is tested as shown. Drag the result onto each letter, or tap a result and then tap a letter. Two results do not belong anywhere.',
        'svg': ''.join(s),
        'zones': [{'id': 'A', 'x': 8.0, 'y': 18.0}, {'id': 'B', 'x': 56.0, 'y': 18.0}, {'id': 'C', 'x': 8.0, 'y': 62.0}, {'id': 'D', 'x': 56.0, 'y': 62.0}],
        'chips': [
            {'t': 'brick-red precipitate', 's': 'reducing sugar', 'z': 0},
            {'t': 'stays blue', 's': 'non-reducing', 'z': 1},
            {'t': 'deep blue-black', 's': 'iodine in the helix', 'z': 2},
            {'t': 'no colour change', 's': 'no helix', 'z': 3},
            {'t': 'silver mirror', 's': "that is Tollens'", 'z': -1},
            {'t': 'orange to green', 's': "that is dichromate", 'z': -1}],
        'why': 'Glucose opens to an aldehyde and reduces Cu<sup>2+</sup> to brick-red Cu<sub>2</sub>O (A). Sucrose has no free anomeric –OH, so it stays blue (B). Iodine fits inside the amylose helix: blue-black (C). Cellulose has straight β-1,4 chains and no helix, so no colour (D).'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    q('CH5-LO1', 'Chemistry tutor', 'Definition', 'Carbohydrates are:', ['polyhydroxy aldehydes or ketones', 'esters of glycerol', 'polymers of amino acids', 'hydrocarbons'], 'Or compounds that hydrolyse to them.')
    q('CH5-LO1', 'Chemistry tutor', 'Chiral carbon', 'A chiral carbon has:', ['four different groups', 'two identical groups', 'a double bond', 'no hydrogen'], 'Like a hand: no mirror symmetry.')
    q('CH5-LO1', 'Chemistry tutor', 'Count', 'Glucose (open chain) has how many chiral carbons?', ['4', '6', '2', '5'], 'C2 to C5.')
    q('CH5-LO1', 'Chemistry tutor', 'Racemate', 'A racemic mixture is:', ['a 50:50 mixture of two enantiomers', 'a pure enantiomer', 'a mixture of α and β anomers', 'a sugar alcohol'], 'Optically inactive.')
    q('CH5-LO1', 'Clinical pharmacist', 'Chiral drugs', 'Esomeprazole is:', ['the single S enantiomer of omeprazole', 'a sugar', 'a racemic mixture', 'an ester prodrug of glucose'], '"es-" = S.', rx=True)
    q('CH5-LO1', 'Pharmacology lecturer', 'Thalidomide', 'Why was the "safe" enantiomer of thalidomide still unsafe?', ['The enantiomers interconvert in the body', 'It was the wrong drug', 'It contains lactose', 'It is a sugar'], 'Chapter 2 revisited.', rx=True)
    q('CH5-LO2', 'Chemistry tutor', 'Classes', 'Ribose (5 C, aldehyde) is an:', ['aldopentose', 'ketopentose', 'aldohexose', 'ketohexose'], 'Aldehyde + five carbons.')
    q('CH5-LO2', 'Chemistry tutor', 'D or L', 'In a Fischer projection, D sugars have the lowest chiral –OH on the:', ['right', 'left', 'top', 'bottom'], 'Ball 16.2.')
    q('CH5-LO2', 'Chemistry tutor', 'Fischer', 'In a Fischer projection, horizontal bonds point:', ['towards the viewer', 'away from the viewer', 'into the page and up', 'nowhere'], 'Vertical bonds point away.')
    q('CH5-LO2', 'Dietitian', 'Sweetest', 'The sweetest natural sugar is:', ['fructose', 'glucose', 'lactose', 'maltose'], '1.7 times sucrose (Ball 16.3).')
    q('CH5-LO2', 'Ward nurse', 'IV fluids', 'Dextrose 5% infusion contains:', ['D-glucose', 'fructose', 'sucrose', 'starch'], 'Dextrose = glucose.', rx=True)
    q('CH5-LO3', 'Chemistry tutor', 'Ring', 'Glucose forms a ring when its C5–OH adds to:', ['the C1 aldehyde', 'the C6 carbon', 'C2', 'another glucose'], 'A hemiacetal; a six-membered ring.')
    q('CH5-LO3', 'Chemistry tutor', 'Anomers', 'In α-D-glucose (Haworth), the C1–OH points:', ['down', 'up', 'into the ring', 'sideways'], 'β points up.')
    q('CH5-LO3', 'Chemistry tutor', 'Haworth', 'Right in Fischer becomes ____ in Haworth.', ['down', 'up', 'left', 'right'], 'Left → up.')
    q('CH5-LO3', 'Chemistry tutor', 'Mutarotation', 'Glucose at equilibrium in water is about:', ['36% α, 64% β', '64% α, 36% β', '50% open chain', '100% β'], 'FGOB 20.3.')
    q('CH5-LO3', 'Chemistry tutor', 'Fructose', 'Fructose forms a ring with:', ['five members (furanose)', 'six members (pyranose)', 'four members', 'no ring'], 'C5–OH adds to the C2 ketone.')
    q('CH5-LO4', 'Lab technologist', 'Benedict\'s', 'A positive Benedict\'s test is:', ['blue → brick-red', 'orange → green', 'colourless → silver', 'yellow → purple'], 'Cu<sup>2+</sup> → Cu<sub>2</sub>O.')
    q('CH5-LO4', 'Diabetes educator', 'Glucometer', 'Glucometer strips use which enzyme?', ['glucose oxidase', 'lactase', 'amylase', 'invertase'], 'Specific for glucose.', rx=True)
    q('CH5-LO4', 'Formulation pharmacist', 'Sugar-free', 'Sorbitol in sugar-free syrups is made by:', ['reducing glucose', 'oxidising glucose', 'hydrolysing starch', 'esterifying glucose'], 'A sugar alcohol.', rx=True)
    q('CH5-LO4', 'Neurosurgery pharmacist', 'Mannitol', 'IV mannitol is used to:', ['reduce pressure in the brain (osmotic diuretic)', 'thin the blood', 'sweeten syrups only', 'treat lactose intolerance'], 'A sugar alcohol from mannose.', rx=True)
    q('CH5-LO4', 'Chemistry tutor', 'Glycosides', 'A glycoside is formed when the anomeric –OH reacts with:', ['an alcohol', 'water', 'an amine salt', 'iodine'], 'Acid catalyst; the ring is locked.')
    q('CH5-LO4', 'Cardiology pharmacist', 'Digoxin', 'Digoxin from foxglove is a:', ['glycoside', 'polysaccharide', 'sugar alcohol', 'disaccharide'], 'Sugars attached to a steroid-like part.', rx=True)
    q('CH5-LO5', 'Chemistry tutor', 'Maltose', 'Maltose = glucose + glucose joined:', ['α-1,4', 'β-1,4', 'α-1,β-2', 'α-1,6'], 'Malt sugar.')
    q('CH5-LO5', 'Chemistry tutor', 'Sucrose', 'Which is a non-reducing sugar?', ['sucrose', 'maltose', 'lactose', 'glucose'], 'Both anomeric carbons are bonded.')
    q('CH5-LO5', 'Patient', 'Milk', '"Milk gives me cramps." The likely cause is too little:', ['lactase', 'amylase', 'sucrase', 'insulin'], 'Lactose intolerance.', rx=True)
    q('CH5-LO5', 'Chemistry tutor', 'Iodine', 'Starch turns iodine blue-black because:', ['iodine fits inside the amylose helix', 'starch is a reducing sugar', 'starch contains fructose', 'iodine oxidises glucose'], 'FGOB 20.7.')
    q('CH5-LO5', 'Chemistry tutor', 'Cellulose', 'Cellulose is made of glucose joined:', ['β-1,4, unbranched', 'α-1,4, branched', 'α-1,6 only', 'β-1,6'], 'Straight chains, H-bonded fibres.')
    q('CH5-LO5', 'Formulation pharmacist', 'Excipients', 'Which is the most common tablet filler made from cellulose?', ['microcrystalline cellulose (MCC)', 'heparin', 'glycogen', 'dextran'], 'Filler and binder.', rx=True)
    q('CH5-LO5', 'Chemistry tutor', 'Glycogen', 'Glycogen is stored mainly in:', ['liver and muscle', 'bone', 'blood plasma', 'the brain'], 'About 70% in muscle.')
    return B


def config():
    return {
        'topic': 'ch5', 'title': 'Chapter 5 game',
        'kicker': 'PHD125 · Chapter 5 · Carbohydrates',
        'blurb': 'You are the pharmacist on duty. Patients ask about sugar-free syrups, glucometers, milk cramps and chiral drugs. Every answer comes back to sugars. Five stations, about 9 minutes.',
        'hub': '../../#ch5', 'slides': '../slides/', 'board': '../../leaderboard/#ch5',
        'los': LOS,
        'levels': [
            {'id': 'mirror', 'name': 'Mirror room', 'blurb': 'Chiral carbons, enantiomers and chiral drugs.', 'intro': 'A new batch of single-enantiomer drugs has arrived. Sort out the lefts from the rights.', 'pool': ['CH5-LO1'], 'n': 5, 'secs': 30},
            {'id': 'sugar', 'name': 'Sugar shelf', 'blurb': 'Monosaccharides, Fischer and Haworth projections.', 'intro': 'Questions on drawing and naming sugars from the intern\'s revision notes.', 'pool': ['CH5-LO2', 'CH5-LO3'], 'n': 6, 'secs': 30},
            {'id': 'bench', 'name': 'Test bench', 'type': 'drag', 'blurb': "Hands-on: Benedict's and iodine results.", 'intro': "Four samples, two reagents. Predict every colour.", 'secs': 75},
            {'id': 'counter', 'name': 'Counter questions', 'blurb': 'Sugar reactions, disaccharides and polysaccharides.', 'intro': 'Patients and colleagues ask about glucometers, syrups, milk and fillers.', 'pool': ['CH5-LO4', 'CH5-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': test_bench(),
        'bank': bank(),
    }
