"""PHD125 Chapter 4 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
from figs import mol

LOS = [
    ['CH4-LO1', 'Name carboxylic acids, describe how they form, and explain their boiling points and solubility'],
    ['CH4-LO2', 'Explain why carboxylic acids are weak acids, and write ionisation and neutralisation equations'],
    ['CH4-LO3', 'Name esters, and write equations for esterification and hydrolysis'],
    ['CH4-LO4', 'Classify and name amines, explain their basicity, and describe amine salts and alkaloids'],
    ['CH4-LO5', 'Name amides, explain their properties, and write equations for their formation and hydrolysis'],
]


def hydrolysis_bench():
    W, H = 440, 300
    def emb(smi, x, y, w=150, h=80):
        return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{mol(smi, w, h)}"/>'
    lab = lambda x, y, s: f'<text x="{x}" y="{y}" text-anchor="middle" font-size="12.5" font-family="sans-serif" fill="#1B2A41">{s}</text>'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Four compounds lettered A to D, each hydrolysed: ethyl acetate with NaOH, methyl benzoate with acid, acetamide with acid, and aspirin with moisture">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>',
         '<text x="220" y="22" text-anchor="middle" font-size="13" font-weight="700" font-family="sans-serif" fill="#B86E00">each compound is hydrolysed</text>',
         '<line x1="220" y1="34" x2="220" y2="290" stroke="#D7E0E8"/><line x1="10" y1="160" x2="430" y2="160" stroke="#D7E0E8"/>',
         emb('CCOC(C)=O', 50, 50), lab(125, 146, 'ethyl acetate + NaOH'),
         emb('COC(=O)c1ccccc1', 270, 50), lab(345, 146, 'methyl benzoate + H₂O, H⁺'),
         emb('CC(N)=O', 50, 180), lab(125, 276, 'acetamide + H₂O, H⁺'),
         emb('CC(=O)Oc1ccccc1C(=O)O', 270, 180), lab(345, 276, 'aspirin + moisture'), '</svg>']
    return {
        'lo': 'CH4-LO3', 'title': 'Hydrolysis bench: what does each compound give?',
        'how': 'Each compound is split by water under the conditions shown. Drag the products onto each letter, or tap a result and then tap a letter. Two results do not belong anywhere.',
        'svg': ''.join(s),
        'zones': [{'id': 'A', 'x': 8.0, 'y': 18.0}, {'id': 'B', 'x': 56.0, 'y': 18.0}, {'id': 'C', 'x': 8.0, 'y': 62.0}, {'id': 'D', 'x': 56.0, 'y': 62.0}],
        'chips': [
            {'t': 'sodium acetate + ethanol', 's': 'saponification', 'z': 0},
            {'t': 'benzoic acid + methanol', 's': 'acidic hydrolysis', 'z': 1},
            {'t': 'acetic acid + NH₄⁺', 's': 'amide in acid', 'z': 2},
            {'t': 'salicylic acid + acetic acid', 's': 'vinegar smell', 'z': 3},
            {'t': 'acetic acid + ethanol', 's': 'needs acid, not NaOH', 'z': -1},
            {'t': 'methyl acetate + ammonia', 's': 'an ester and a base', 'z': -1}],
        'why': 'With NaOH an ester gives the carboxylate salt and the alcohol: sodium acetate + ethanol (A). With acid, methyl benzoate gives benzoic acid + methanol (B). An amide in acid gives the acid and an ammonium ion (C). Moisture splits aspirin\'s ester into salicylic acid and acetic acid, which is why old tablets smell of vinegar (D).'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    q('CH4-LO1', 'Chemistry tutor', 'Naming', 'The IUPAC name of CH<sub>3</sub>COOH is:', ['ethanoic acid', 'methanoic acid', 'ethanol', 'ethanal'], 'Two carbons, -oic acid.')
    q('CH4-LO1', 'Chemistry tutor', 'Naming', 'Name CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>COOH.', ['pentanoic acid', 'butanoic acid', 'pentanal', 'hexanoic acid'], 'Count the carboxyl carbon too.')
    q('CH4-LO1', 'Chemistry tutor', 'Greek letters', 'In β-chloropropionic acid, the Cl is on:', ['C3', 'C2', 'C1', 'the oxygen'], 'α = C2, β = C3.')
    q('CH4-LO1', 'Chemistry tutor', 'Boiling point', 'Why does acetic acid boil higher than 1-propanol?', ['Acid molecules form hydrogen-bonded dimers', 'It is ionic', 'It is heavier', 'It has a benzene ring'], 'Two H-bonds hold each pair together.')
    q('CH4-LO1', 'Food scientist', 'Smell', 'Rancid butter smells of:', ['butyric (butanoic) acid', 'ethyl acetate', 'trimethylamine', 'acetone'], 'Latin <i>butyrum</i>, butter (Ball 15.1).')
    q('CH4-LO2', 'Chemistry tutor', 'Strength', 'Which acid is strongest?', ['trichloroacetic acid (pK<sub>a</sub> 0.64)', 'acetic acid (pK<sub>a</sub> 4.74)', 'propanoic acid (pK<sub>a</sub> 4.89)', 'benzoic acid (pK<sub>a</sub> 4.19)'], 'Smallest pK<sub>a</sub> = strongest.')
    q('CH4-LO2', 'Chemistry tutor', 'Salts', 'Acetic acid + NaOH gives:', ['sodium acetate + water', 'ethyl acetate + water', 'acetamide', 'acetaldehyde'], 'Neutralisation: a salt and water.')
    q('CH4-LO2', 'Store manager', 'Preservative', 'Which salt preserves syrups and pickles?', ['sodium benzoate', 'sodium chloride only', 'ammonium chloride', 'ethyl acetate'], 'It stops bacteria and fungi (FGOB 17.2).', rx=True)
    q('CH4-LO2', 'Patient', 'Fizzing', '"Why does my vitamin C tablet fizz?"', ['An acid reacts with sodium bicarbonate, releasing CO<sub>2</sub>', 'It contains an ester', 'Water boils', 'It is an amine salt'], 'Effervescent tablets.', rx=True)
    q('CH4-LO3', 'Chemistry tutor', 'Naming', 'Name CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>.', ['ethyl acetate (ethyl ethanoate)', 'methyl propanoate', 'acetyl ethanol', 'ethyl formate'], 'The group on the O first.')
    q('CH4-LO3', 'Flavour chemist', 'Banana', 'Which ester smells of banana?', ['isopentyl acetate', 'ethyl butyrate', 'methyl salicylate', 'octyl acetate'], 'Ethyl butyrate is pineapple; octyl acetate orange.')
    q('CH4-LO3', 'Chemistry tutor', 'Esterification', 'Esterification needs:', ['a carboxylic acid, an alcohol, an acid catalyst and heat', 'an amine and NaOH', 'an alkene and water', 'an aldehyde and Tollens\''], 'And it is reversible.')
    q('CH4-LO3', 'Chemistry tutor', 'Saponification', 'Boiling a fat with NaOH gives:', ['soap (carboxylate salts) and glycerol', 'esters and water', 'amides', 'alkenes'], 'Basic hydrolysis of esters.')
    q('CH4-LO3', 'Cardiology nurse', 'Angina', 'Glyceryl trinitrate is an ester of glycerol and:', ['nitric acid', 'acetic acid', 'phosphoric acid', 'ammonia'], 'Sublingual spray for angina.', rx=True)
    q('CH4-LO3', 'Clinical pharmacist', 'Prodrugs', 'Enalapril is an ester prodrug. In the body it is:', ['hydrolysed by esterases to the active acid', 'oxidised to a ketone', 'converted to an amide', 'excreted unchanged'], 'Enalapril → enalaprilat.', rx=True)
    q('CH4-LO4', 'Chemistry tutor', 'Classes', '(CH<sub>3</sub>)<sub>2</sub>NH is a:', ['secondary amine', 'primary amine', 'tertiary amine', 'quaternary ion'], 'Two carbon groups on N.')
    q('CH4-LO4', 'Chemistry tutor', 'Naming', 'Name CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>.', ['propylamine', 'propanamide', 'propanoic acid', 'trimethylamine'], 'Alkyl group + -amine.')
    q('CH4-LO4', 'Fishmonger', 'Smell', 'The smell of old fish is mainly due to:', ['amines such as trimethylamine', 'esters', 'carboxylic acids', 'alcohols'], 'FGOB 16.3.')
    q('CH4-LO4', 'Chemistry tutor', 'Basicity', 'Amines are basic because nitrogen has:', ['a lone pair that accepts H<sup>+</sup>', 'a positive charge', 'a double bond', 'an –OH group'], 'Like ammonia.')
    q('CH4-LO4', 'Hospital pharmacist', 'Salts', 'Why is morphine given as morphine sulfate?', ['The salt dissolves in water', 'The salt is stronger', 'Sulfate is the active part', 'It makes it an ester'], 'Amine salts are ionic.', rx=True)
    q('CH4-LO4', 'Pharmacognosist', 'Alkaloids', 'Caffeine, nicotine and morphine are:', ['alkaloids (basic plant amines)', 'esters', 'carboxylic acids', 'amides only'], '"Like alkalis" (FGOB 16.4).')
    q('CH4-LO4', 'Eye-clinic pharmacist', 'Preservative', 'Benzalkonium chloride in eye drops is a:', ['quaternary ammonium salt', 'tertiary amine', 'carboxylic acid', 'ester'], 'R<sub>4</sub>N<sup>+</sup>, an antiseptic.', rx=True)
    q('CH4-LO5', 'Chemistry tutor', 'Naming', 'CH<sub>3</sub>CONH<sub>2</sub> is:', ['acetamide (ethanamide)', 'methylamine', 'acetic acid', 'ethylamine'], '-ic acid → -amide.')
    q('CH4-LO5', 'Chemistry tutor', 'Basicity', 'Amides are:', ['neutral, not basic', 'strong bases', 'strong acids', 'ionic salts'], 'The N lone pair is held by the C=O.')
    q('CH4-LO5', 'Chemistry tutor', 'Formation', 'Acetic acid + ammonia, heated, gives:', ['acetamide + water', 'ethylamine + water', 'ethyl acetate', 'methylamine'], 'Condensation.')
    q('CH4-LO5', 'Microbiologist', 'Resistance', 'β-Lactamase makes bacteria resistant to penicillin by:', ['hydrolysing the β-lactam amide', 'oxidising the drug', 'forming an ester', 'adding a methyl group'], 'The four-membered ring amide is opened.', rx=True)
    q('CH4-LO5', 'Anaesthetist', 'Duration', 'Lidocaine lasts longer than procaine because lidocaine is:', ['an amide, which resists hydrolysis', 'an ester', 'a carboxylic acid', 'a salt'], 'Procaine (ester) is hydrolysed fast by plasma esterases.', rx=True)
    q('CH4-LO5', 'Chemistry tutor', 'Polymers', 'Adipic acid + hexanediamine gives:', ['nylon-66, a polyamide', 'PET, a polyester', 'polyethylene', 'a protein'], 'Condensation polymer (FGOB 17.5).')
    return B


def config():
    return {
        'topic': 'ch4', 'title': 'Chapter 4 game',
        'kicker': 'PHD125 · Chapter 4 · Carboxylic Acid, Ester, Amines, Amide',
        'blurb': 'You are the pharmacist on duty. Patients ask about fizzy tablets, smelly aspirin, fishy smells, eye drops and anaesthetics. Every answer comes back to acids, esters, amines and amides. Five stations, about 9 minutes.',
        'hub': '../../#ch4', 'slides': '../slides/', 'board': '../../leaderboard/#ch4',
        'los': LOS,
        'levels': [
            {'id': 'acid', 'name': 'Acid shelf', 'blurb': 'Names, properties and salts of carboxylic acids.', 'intro': 'Sorting the shelf of acids, salts and preservatives.', 'pool': ['CH4-LO1', 'CH4-LO2'], 'n': 5, 'secs': 30},
            {'id': 'ester', 'name': 'Flavour lab', 'blurb': 'Ester names, smells, esterification and hydrolysis.', 'intro': 'The formulation lab is choosing flavours for a children\'s syrup. Help with esters.', 'pool': ['CH4-LO3'], 'n': 5, 'secs': 30},
            {'id': 'bench', 'name': 'Hydrolysis bench', 'type': 'drag', 'blurb': 'Hands-on: what each ester or amide breaks into.', 'intro': 'Four samples, four sets of conditions. Predict the products of each hydrolysis.', 'secs': 75},
            {'id': 'amine', 'name': 'Amine and amide counter', 'blurb': 'Amine classes and salts, alkaloids, amides in drugs.', 'intro': 'Questions from the dispensary and the wards about amine salts, alkaloids and amide drugs.', 'pool': ['CH4-LO4', 'CH4-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': hydrolysis_bench(),
        'bank': bank(),
    }
