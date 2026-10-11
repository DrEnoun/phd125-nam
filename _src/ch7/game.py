"""PHD125 Chapter 7 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
from figs import mol

LOS = [
    ['CH7-LO1', 'Describe amino acids, classify them by side chain, and explain why they are L'],
    ['CH7-LO2', 'Explain zwitterions, the effect of pH and the isoelectric point'],
    ['CH7-LO3', 'Describe peptide bonds and write peptide sequences'],
    ['CH7-LO4', 'Describe protein structure, hydrolysis and denaturation'],
    ['CH7-LO5', 'Explain how enzymes work, what affects them, and how inhibitors act'],
]


def ph_bench():
    W, H = 440, 300
    def emb(smi, x, y, w=170, h=80):
        return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{mol(smi, w, h)}"/>'
    lab = lambda x, y, s: f'<text x="{x}" y="{y}" text-anchor="middle" font-size="12.5" font-family="sans-serif" fill="#1B2A41">{s}</text>'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Four forms lettered A to D: alanine cation, alanine zwitterion, alanine anion, and lysine at pH 7">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>',
         '<text x="220" y="22" text-anchor="middle" font-size="13" font-weight="700" font-family="sans-serif" fill="#B86E00">at which pH does each form dominate?</text>',
         '<line x1="220" y1="34" x2="220" y2="290" stroke="#D7E0E8"/><line x1="10" y1="160" x2="430" y2="160" stroke="#D7E0E8"/>',
         emb('C[C@@H](C(=O)O)[NH3+]', 30, 50), lab(115, 146, 'alanine form A'),
         emb('C[C@@H](C(=O)[O-])[NH3+]', 250, 50), lab(335, 146, 'alanine form B'),
         emb('C[C@@H](C(=O)[O-])N', 30, 180), lab(115, 276, 'alanine form C'),
         emb('[NH3+]CCCC[C@H]([NH3+])C(=O)[O-]', 240, 180, 190), lab(335, 276, 'lysine form D'), '</svg>']
    return {
        'lo': 'CH7-LO2', 'title': 'Charge bench: match each form to its pH',
        'how': 'Each structure is one form of an amino acid. Drag the condition onto each letter, or tap a condition and then tap a letter. Two conditions do not belong anywhere.',
        'svg': ''.join(s),
        'zones': [{'id': 'A', 'x': 8.0, 'y': 18.0}, {'id': 'B', 'x': 56.0, 'y': 18.0}, {'id': 'C', 'x': 8.0, 'y': 62.0}, {'id': 'D', 'x': 56.0, 'y': 62.0}],
        'chips': [
            {'t': 'pH 1 (net +1)', 's': 'cation', 'z': 0},
            {'t': 'pH 6, its pI (net 0)', 's': 'zwitterion', 'z': 1},
            {'t': 'pH 12 (net −1)', 's': 'anion', 'z': 2},
            {'t': 'pH 7 (net +1)', 's': 'below its pI 9.8', 'z': 3},
            {'t': 'neutral, no charges at all', 's': 'never the main form in water', 'z': -1},
            {'t': 'pH 3.0 (net 0)', 's': "that is aspartic acid's pI", 'z': -1}],
        'why': 'In strong acid alanine is fully protonated: +1 (A). At its pI (6.0) it is the zwitterion (B). In strong base the –NH<sub>3</sub><sup>+</sup> loses H<sup>+</sup>: −1 (C). Lysine (pI 9.8) at pH 7 still has both amino groups protonated: net +1 (D).'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    q('CH7-LO1', 'Chemistry tutor', 'Structure', 'Every α-amino acid has:', ['–NH<sub>2</sub> and –COOH on the same carbon', 'two amine groups', 'a phosphate', 'an ester group'], 'Plus H and a side chain.')
    q('CH7-LO1', 'Chemistry tutor', 'Chirality', 'Which amino acid is not chiral?', ['glycine', 'alanine', 'valine', 'serine'], 'R = H.')
    q('CH7-LO1', 'Chemistry tutor', 'Side chains', 'Lysine has a side chain that is:', ['basic (positive at pH 7)', 'acidic', 'nonpolar', 'an alcohol'], '–(CH<sub>2</sub>)<sub>4</sub>NH<sub>2</sub>.')
    q('CH7-LO1', 'Dietitian', 'Essential', 'An essential amino acid is one that:', ['must come from the diet', 'is found only in meat', 'is not chiral', 'is a vitamin'], 'Nine for adults.')
    q('CH7-LO1', 'Neurology pharmacist', 'Levodopa', 'Levodopa for Parkinson\'s disease is:', ['an amino acid drug (L-DOPA)', 'a steroid', 'a sugar', 'a lipid'], 'Converted to dopamine in the brain.', rx=True)
    q('CH7-LO2', 'Chemistry tutor', 'Zwitterion', 'At its pI, an amino acid is:', ['a zwitterion with no net charge', 'fully positive', 'fully negative', 'an anion'], 'pI = isoelectric point.')
    q('CH7-LO2', 'Chemistry tutor', 'Low pH', 'In strong acid, glycine carries a net charge of:', ['+1', '0', '−1', '+2'], 'H<sub>3</sub>N<sup>+</sup>CH<sub>2</sub>COOH.')
    q('CH7-LO2', 'Lab technologist', 'Electrophoresis', 'At pH 6, lysine (pI 9.8) moves towards the:', ['negative electrode', 'positive electrode', 'it stays still', 'top of the gel'], 'It is positive below its pI.')
    q('CH7-LO2', 'Forensic chemist', 'Fingerprints', 'Ninhydrin reveals fingerprints by reacting with:', ['amino acids', 'fats', 'sugars', 'salt'], 'Purple colour (FGOB 18.4).')
    q('CH7-LO3', 'Chemistry tutor', 'Peptide bond', 'A peptide bond is a(n):', ['amide', 'ester', 'ether', 'glycoside'], '–CO–NH–.')
    q('CH7-LO3', 'Chemistry tutor', 'Terminal', 'In Lys-Val-Phe, the C-terminal residue is:', ['Phe', 'Lys', 'Val', 'none'], 'Written N → C.')
    q('CH7-LO3', 'Chemistry tutor', 'Water', 'Forming a tripeptide releases how many H<sub>2</sub>O?', ['2', '3', '1', '0'], 'One per peptide bond.')
    q('CH7-LO3', 'Endocrinology pharmacist', 'Insulin', 'Insulin has how many amino acids?', ['51', '9', '20', '300'], 'Two chains, three disulfides.', rx=True)
    q('CH7-LO3', 'Patient', 'Sweetener', '"Why does my diet drink warn about phenylketonurics?"', ['Aspartame releases phenylalanine', 'It contains lactose', 'It has caffeine', 'It is a steroid'], 'Asp-Phe methyl ester.', rx=True)
    q('CH7-LO4', 'Chemistry tutor', 'Primary', 'The primary structure of a protein is its:', ['amino acid sequence', 'α-helix', 'overall 3D shape', 'number of subunits'], 'Held by peptide bonds.')
    q('CH7-LO4', 'Chemistry tutor', 'α-Helix', 'An α-helix has how many residues per turn?', ['3.6', '2', '10', '6'], 'Pauling and Corey.')
    q('CH7-LO4', 'Chemistry tutor', 'Haemoglobin', 'Haemoglobin has quaternary structure because it has:', ['four polypeptide chains', 'one long chain', 'only α-helix', 'no disulfides'], 'Two α, two β.')
    q('CH7-LO4', 'Chemistry tutor', 'Denaturation', 'Denaturation does NOT break:', ['peptide bonds', 'hydrogen bonds', 'ionic bonds', 'hydrophobic interactions'], 'Primary structure survives.')
    q('CH7-LO4', 'Infection control nurse', 'Alcohol', '70% alcohol hand rub kills microbes by:', ['denaturing their proteins', 'hydrolysing their fats', 'oxidising sugar', 'freezing them'], 'FGOB 18.10.', rx=True)
    q('CH7-LO4', 'Cold-chain pharmacist', 'Vaccines', 'Vaccines and insulin are kept at 2–8 °C to prevent:', ['denaturation of proteins', 'saponification', 'esterification', 'crystallisation of sugar'], 'Do not freeze.', rx=True)
    q('CH7-LO5', 'Chemistry tutor', 'Catalyst', 'Enzymes speed up reactions by:', ['lowering the activation energy', 'raising the temperature', 'changing the equilibrium', 'being used up'], 'They are catalysts.')
    q('CH7-LO5', 'Chemistry tutor', 'Models', 'In the induced-fit model, the active site:', ['changes shape when the substrate binds', 'is rigid', 'is outside the enzyme', 'is made of sugar'], 'Hexokinase and glucose.')
    q('CH7-LO5', 'Chemistry tutor', 'pH', 'Pepsin works best at about pH:', ['2', '7', '10', '13'], 'In the stomach.')
    q('CH7-LO5', 'Chemistry tutor', 'Cofactors', 'NAD<sup>+</sup> is a coenzyme made from:', ['niacin (vitamin B<sub>3</sub>)', 'vitamin C', 'vitamin D', 'cholesterol'], 'FGOB 19.2.')
    q('CH7-LO5', 'Cardiology pharmacist', 'Statins', 'Atorvastatin is a(n):', ['competitive inhibitor of HMG-CoA reductase', 'irreversible COX inhibitor', 'allosteric activator', 'protease'], 'Lowers cholesterol.', rx=True)
    q('CH7-LO5', 'Rheumatology pharmacist', 'Gout', 'Allopurinol treats gout by inhibiting:', ['xanthine oxidase', 'lipase', 'amylase', 'trypsin'], 'Less uric acid is made.', rx=True)
    q('CH7-LO5', 'Toxicologist', 'Nerve agents', 'Organophosphate poisons irreversibly inhibit:', ['acetylcholinesterase', 'amylase', 'lactase', 'HMG-CoA reductase'], 'They bond to a serine.', rx=True)
    q('CH7-LO5', 'Chemistry tutor', 'Feedback', 'In feedback inhibition, the enzyme inhibited is usually:', ['the first in the pathway', 'the last in the pathway', 'any digestive enzyme', 'none'], 'The end product switches it off.')
    return B


def config():
    return {
        'topic': 'ch7', 'title': 'Chapter 7 game',
        'kicker': 'PHD125 · Chapter 7 · Amino Acids, Proteins and Enzymes',
        'blurb': 'You are the pharmacist on duty. Patients ask about insulin, vaccines, diet drinks, aspirin and statins. Every answer comes back to amino acids, proteins and enzymes. Five stations, about 9 minutes.',
        'hub': '../../#ch7', 'slides': '../slides/', 'board': '../../leaderboard/#ch7',
        'los': LOS,
        'levels': [
            {'id': 'aa', 'name': 'Amino acid shelf', 'blurb': 'Amino acids, side chains, essential amino acids.', 'intro': 'Sorting supplements, IV nutrition and amino acid drugs.', 'pool': ['CH7-LO1'], 'n': 5, 'secs': 30},
            {'id': 'charge', 'name': 'Charge lab', 'blurb': 'Zwitterions, pH and pI; peptides.', 'intro': 'The lab is running electrophoresis and peptide analysis today.', 'pool': ['CH7-LO2', 'CH7-LO3'], 'n': 6, 'secs': 30},
            {'id': 'bench', 'name': 'Charge bench', 'type': 'drag', 'blurb': 'Hands-on: which pH gives which form?', 'intro': 'Four forms of amino acids. Match each to its conditions.', 'secs': 75},
            {'id': 'enz', 'name': 'Protein and enzyme desk', 'blurb': 'Protein structure, denaturation and enzymes.', 'intro': 'Questions about cold chains, disinfectants and enzyme-blocking drugs.', 'pool': ['CH7-LO4', 'CH7-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': ph_bench(),
        'bank': bank(),
    }
