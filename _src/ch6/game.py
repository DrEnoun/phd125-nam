"""PHD125 Chapter 6 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
from lipidfigs import triglyceride

LOS = [
    ['CH6-LO1', 'Define and classify lipids, and describe fatty acids'],
    ['CH6-LO2', 'Describe waxes and triacylglycerols, and relate melting points to fatty acids'],
    ['CH6-LO3', 'Explain hydrolysis, saponification, hydrogenation and rancidity of fats'],
    ['CH6-LO4', 'Describe phospholipids and cell membranes, and how substances cross them'],
    ['CH6-LO5', 'Describe cholesterol, steroid hormones, bile salts and steroid drugs'],
]


def fat_bench():
    W, H = 440, 300
    ts = triglyceride(['(CH₂)₁₆CH₃'] * 3)
    to = triglyceride(['(CH₂)₇CH=CH(CH₂)₇CH₃'] * 3)
    def emb(uri, x, y, w=180, h=78):
        return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{uri}"/>'
    lab = lambda x, y, s: f'<text x="{x}" y="{y}" text-anchor="middle" font-size="12.5" font-family="sans-serif" fill="#1B2A41">{s}</text>'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Four flasks lettered A to D: tristearin boiled with NaOH, triolein with hydrogen and nickel, triolein left in air and light, and tristearin with pancreatic lipase">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>',
         '<text x="220" y="22" text-anchor="middle" font-size="13" font-weight="700" font-family="sans-serif" fill="#B86E00">what does each flask give?</text>',
         '<line x1="220" y1="34" x2="220" y2="290" stroke="#D7E0E8"/><line x1="10" y1="160" x2="430" y2="160" stroke="#D7E0E8"/>',
         emb(ts, 20, 52), lab(115, 148, 'tristearin + NaOH, boil'),
         emb(to, 240, 52), lab(335, 148, 'triolein + H₂, Ni'),
         emb(to, 20, 182), lab(115, 278, 'triolein in air and light'),
         emb(ts, 240, 182), lab(335, 278, 'tristearin + lipase, water'), '</svg>']
    return {
        'lo': 'CH6-LO3', 'title': 'Fat lab: what does each flask give?',
        'how': 'Each fat is treated as shown. Drag the result onto each letter, or tap a result and then tap a letter. Two results do not belong anywhere.',
        'svg': ''.join(s),
        'zones': [{'id': 'A', 'x': 8.0, 'y': 18.0}, {'id': 'B', 'x': 56.0, 'y': 18.0}, {'id': 'C', 'x': 8.0, 'y': 62.0}, {'id': 'D', 'x': 56.0, 'y': 62.0}],
        'chips': [
            {'t': 'glycerol + sodium stearate', 's': 'saponification: soap', 'z': 0},
            {'t': 'tristearin (a solid fat)', 's': 'hydrogenation', 'z': 1},
            {'t': 'smelly aldehydes and acids', 's': 'oxidative rancidity', 'z': 2},
            {'t': 'glycerol + stearic acid', 's': 'enzyme hydrolysis', 'z': 3},
            {'t': 'cholesterol', 's': 'a steroid', 'z': -1},
            {'t': 'phosphatidylcholine', 's': 'a phospholipid', 'z': -1}],
        'why': 'NaOH splits the three ester bonds: glycerol and sodium stearate (soap) (A). H<sub>2</sub>/Ni adds to the C=C of oleic chains, giving tristearin (B). Oxygen attacks the C=C of unsaturated chains, breaking them into smelly aldehydes and acids (C). Lipase with water gives glycerol and the free fatty acid (D).'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    q('CH6-LO1', 'Chemistry tutor', 'Definition', 'Lipids are classified by their:', ['solubility in nonpolar solvents', 'functional group', 'colour', 'molar mass'], 'Not by a functional group.')
    q('CH6-LO1', 'Dietitian', 'Energy', 'Fat supplies about how many kcal per gram?', ['9', '4', '2', '17'], 'Carbohydrate supplies 4.')
    q('CH6-LO1', 'Chemistry tutor', 'Shorthand', 'C18:2 describes:', ['linoleic acid', 'stearic acid', 'oleic acid', 'palmitic acid'], '18 carbons, 2 C=C.')
    q('CH6-LO1', 'Chemistry tutor', 'Cis', 'A cis double bond in a fatty acid chain:', ['puts a kink in the chain', 'straightens the chain', 'adds a branch', 'makes it a steroid'], 'Lower melting point.')
    q('CH6-LO1', 'Nutrition pharmacist', 'Omega-3', 'Which is an ω-3 fatty acid?', ['DHA', 'arachidonic acid', 'stearic acid', 'linoleic acid'], 'EPA and DHA from fish oil.', rx=True)
    q('CH6-LO1', 'Patient', 'Painkillers', '"How does ibuprofen stop my pain?"', ['It blocks COX, so fewer prostaglandins are made', 'It dissolves fat', 'It is a steroid', 'It blocks lipase'], 'NSAIDs inhibit cyclooxygenase.', rx=True)
    q('CH6-LO2', 'Chemistry tutor', 'Waxes', 'Beeswax is mainly an ester of:', ['a long-chain acid and a long-chain alcohol', 'glycerol and three acids', 'choline and phosphate', 'cholesterol'], 'Myricyl palmitate.')
    q('CH6-LO2', 'Formulation pharmacist', 'Coating', 'Which wax polishes coated tablets?', ['carnauba wax', 'lanolin', 'spermaceti', 'cholesterol'], 'From a Brazilian palm.', rx=True)
    q('CH6-LO2', 'Chemistry tutor', 'Fats vs oils', 'An oil differs from a fat in having more:', ['unsaturated fatty acids', 'glycerol', 'saturated fatty acids', 'ester bonds'], 'Kinks keep it liquid.')
    q('CH6-LO2', 'Chemistry tutor', 'Iodine value', 'Which oil has the highest iodine value?', ['linseed oil', 'coconut oil', 'butter', 'tallow'], 'Most C=C bonds.')
    q('CH6-LO2', 'Formulation pharmacist', 'Suppositories', 'Cocoa butter (theobroma oil) suits suppositories because it:', ['melts at about body temperature', 'dissolves in water', 'is a steroid', 'is a wax'], 'Solid at room temperature, melts in the body.', rx=True)
    q('CH6-LO3', 'Chemistry tutor', 'Saponification', 'Moles of NaOH to saponify one mole of fat:', ['3', '1', '2', '6'], 'One per ester bond.')
    q('CH6-LO3', 'Food chemist', 'Margarine', 'Margarine is made from vegetable oil by:', ['partial hydrogenation', 'saponification', 'oxidation', 'esterification with cholesterol'], 'Adds H<sub>2</sub> to some C=C.')
    q('CH6-LO3', 'Food chemist', 'Trans fats', 'Trans fats are a concern because they:', ['raise LDL cholesterol', 'are sugars', 'contain no carbon', 'are vitamins'], 'Formed during partial hydrogenation.')
    q('CH6-LO3', 'QC pharmacist', 'Antioxidant', 'Which is added to oily products to slow rancidity?', ['BHT or vitamin E', 'water', 'iron salts', 'NaOH'], 'Antioxidants stop oxidation.', rx=True)
    q('CH6-LO3', 'Obesity clinic pharmacist', 'Orlistat', 'Orlistat reduces fat absorption by blocking:', ['lipase', 'amylase', 'HMG-CoA reductase', 'COX'], 'Undigested fat is excreted.', rx=True)
    q('CH6-LO3', 'Chemistry tutor', 'Soap', 'Soap removes grease by forming:', ['micelles', 'bilayers', 'crystals', 'waxes'], 'Tails in the grease, heads in water.')
    q('CH6-LO4', 'Chemistry tutor', 'Phospholipids', 'A phospholipid has how many fatty acid tails?', ['2', '3', '1', '4'], 'Plus a phosphate head.')
    q('CH6-LO4', 'Chemistry tutor', 'Bilayer', 'In a membrane bilayer, the hydrophobic tails point:', ['towards each other, inside the bilayer', 'out into the water', 'into the cytoplasm only', 'nowhere'], 'Heads face water on both sides.')
    q('CH6-LO4', 'Chemistry tutor', 'Fluidity', 'Which keeps membrane fluidity in a useful range?', ['cholesterol', 'glycogen', 'triglycerides', 'waxes'], 'It sits between the tails.')
    q('CH6-LO4', 'Anaesthetist', 'Propofol', 'The white propofol emulsion is stabilised by:', ['egg lecithin', 'cholesterol', 'beeswax', 'starch'], 'Lecithin is an emulsifier.', rx=True)
    q('CH6-LO4', 'Clinical pharmacist', 'Liposomes', 'Liposomal amphotericin B is used because it:', ['reduces kidney toxicity', 'is cheaper', 'is a steroid', 'is taken by mouth'], 'Phospholipid spheres carry the drug.', rx=True)
    q('CH6-LO4', 'Chemistry tutor', 'Transport', 'Moving ions against their gradient with ATP is:', ['active transport', 'simple diffusion', 'facilitated diffusion', 'osmosis'], 'The Na<sup>+</sup>/K<sup>+</sup> pump.')
    q('CH6-LO5', 'Chemistry tutor', 'Steroid nucleus', 'The steroid nucleus has:', ['four fused rings', 'a glycerol backbone', 'two fatty acids', 'a phosphate group'], 'A, B, C (6) and D (5).')
    q('CH6-LO5', 'Cardiology pharmacist', 'Statins', 'Atorvastatin works by inhibiting:', ['HMG-CoA reductase', 'lipase', 'COX', 'amylase'], 'Less cholesterol is made.', rx=True)
    q('CH6-LO5', 'Dermatology pharmacist', 'Creams', 'Hydrocortisone cream is a:', ['corticosteroid', 'sex hormone', 'bile salt', 'wax'], 'Reduces inflammation.', rx=True)
    q('CH6-LO5', 'Chemistry tutor', 'Bile salts', 'Bile salts are made from:', ['cholesterol', 'glycogen', 'lecithin', 'fatty acids only'], 'In the liver.')
    q('CH6-LO5', 'Chemistry tutor', 'Lipoproteins', 'LDL is called "bad" cholesterol because it:', ['carries cholesterol to tissues and arteries', 'carries it to the liver', 'is a steroid hormone', 'is a phospholipid'], 'High LDL raises heart-disease risk.')
    return B


def config():
    return {
        'topic': 'ch6', 'title': 'Chapter 6 game',
        'kicker': 'PHD125 · Chapter 6 · Lipids',
        'blurb': 'You are the pharmacist on duty. Patients ask about cooking oils, fish oil, painkillers, statins and steroid creams. Every answer comes back to lipids. Five stations, about 9 minutes.',
        'hub': '../../#ch6', 'slides': '../slides/', 'board': '../../leaderboard/#ch6',
        'los': LOS,
        'levels': [
            {'id': 'acids', 'name': 'Oil shelf', 'blurb': 'Fatty acids, waxes, fats and oils.', 'intro': 'Sorting cooking oils, supplements and waxes on the shelf.', 'pool': ['CH6-LO1', 'CH6-LO2'], 'n': 6, 'secs': 30},
            {'id': 'react', 'name': 'Reaction desk', 'blurb': 'Hydrolysis, saponification, hydrogenation, rancidity.', 'intro': 'Questions about soap, margarine and oils that have gone off.', 'pool': ['CH6-LO3'], 'n': 5, 'secs': 30},
            {'id': 'bench', 'name': 'Fat lab', 'type': 'drag', 'blurb': 'Hands-on: four fats, four treatments.', 'intro': 'Predict what comes out of each flask.', 'secs': 75},
            {'id': 'cell', 'name': 'Membranes and steroids', 'blurb': 'Phospholipids, membranes, cholesterol and steroid drugs.', 'intro': 'Ward and counter questions about liposomes, statins and creams.', 'pool': ['CH6-LO4', 'CH6-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': fat_bench(),
        'bank': bank(),
    }
