"""PHD125 Chapter 3 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
from figs import mol

LOS = [
    ['CH3-LO1', 'Name and classify alcohols and phenols, and relate their properties to hydrogen bonding'],
    ['CH3-LO2', 'Explain SN1 and SN2 reactions of haloalkanes that form alcohols, and predict which one occurs'],
    ['CH3-LO3', 'Predict the products of alcohol dehydration and oxidation'],
    ['CH3-LO4', 'Name ethers and thiols, compare their properties with alcohols, and describe disulfide formation'],
    ['CH3-LO5', 'Name aldehydes and ketones, explain their properties, and predict oxidation, reduction and test results'],
]


def oxidation_bench():
    W, H = 440, 300
    def emb(smi, x, y, w=150, h=80):
        return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{mol(smi, w, h)}"/>'
    lab = lambda x, y, s: f'<text x="{x}" y="{y}" text-anchor="middle" font-size="12.5" font-family="sans-serif" fill="#1B2A41">{s}</text>'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Four compounds lettered A to D, each to be warmed with acidified potassium dichromate: cyclohexanol, 2-methyl-2-propanol, ethanal and 2-butanol">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>',
         '<text x="220" y="22" text-anchor="middle" font-size="13" font-weight="700" font-family="sans-serif" fill="#B86E00">each warmed with acidified K₂Cr₂O₇ [O]</text>',
         '<line x1="220" y1="34" x2="220" y2="290" stroke="#D7E0E8"/><line x1="10" y1="160" x2="430" y2="160" stroke="#D7E0E8"/>',
         emb('OC1CCCCC1', 50, 50), lab(125, 146, 'cyclohexanol'),
         emb('CC(C)(C)O', 270, 50), lab(345, 146, '2-methyl-2-propanol'),
         emb('CC=O', 50, 180), lab(125, 276, 'ethanal'),
         emb('CCC(C)O', 270, 180), lab(345, 276, '2-butanol'), '</svg>']
    return {
        'lo': 'CH3-LO3', 'title': 'Oxidation bench: what does each compound give?',
        'how': 'Each compound is warmed with acidified dichromate. Drag the result onto each letter, or tap a result and then tap a letter. Two results do not belong anywhere.',
        'svg': ''.join(s),
        'zones': [{'id': 'A', 'x': 8.0, 'y': 18.0}, {'id': 'B', 'x': 56.0, 'y': 18.0}, {'id': 'C', 'x': 8.0, 'y': 62.0}, {'id': 'D', 'x': 56.0, 'y': 62.0}],
        'chips': [
            {'t': 'cyclohexanone', 's': '2° alcohol → ketone', 'z': 0},
            {'t': 'no reaction', 's': 'stays orange', 'z': 1},
            {'t': 'ethanoic acid', 's': 'aldehyde → acid', 'z': 2},
            {'t': 'butanone', 's': '2° alcohol → ketone', 'z': 3},
            {'t': 'cyclohexene', 's': 'an alkene', 'z': -1},
            {'t': 'butanal', 's': 'an aldehyde', 'z': -1}],
        'why': 'Cyclohexanol and 2-butanol are secondary, so they give ketones: cyclohexanone (A) and butanone (D). 2-Methyl-2-propanol is tertiary, with no H on the C–OH carbon: no reaction (B). Ethanal is an aldehyde and is oxidised easily to ethanoic acid (C). Alkenes come from dehydration, not oxidation.'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    q('CH3-LO1', 'Chemistry tutor', 'Classes', '2-Propanol is a:', ['secondary alcohol', 'primary alcohol', 'tertiary alcohol', 'phenol'], 'The C–OH carbon carries two carbons.')
    q('CH3-LO1', 'Chemistry tutor', 'Naming', 'Name CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>3</sub>.', ['2-butanol', '3-butanol', '1-methyl-1-propanol', 'butanal'], 'Number from the end nearer the –OH.')
    q('CH3-LO1', 'Store manager', 'Swabs', 'Which alcohol is in 70% alcohol swabs?', ['2-propanol (isopropyl alcohol)', 'methanol', 'ethylene glycol', 'glycerol'], 'Isopropyl rubbing alcohol (Ball 14.4).', rx=True)
    q('CH3-LO1', 'Formulation pharmacist', 'Humectant', 'Which non-toxic triol keeps creams moist?', ['glycerol', 'ethylene glycol', 'methanol', 'phenol'], '1,2,3-Propanetriol (Ball 14.6).')
    q('CH3-LO1', 'Chemistry tutor', 'Phenols', 'How does phenol differ from ethanol?', ['Phenol is weakly acidic and reacts with NaOH', 'Phenol has no –OH', 'Phenol is an ether', 'Ethanol is aromatic'], 'The aromatic ring makes phenol\'s O–H more acidic.')
    q('CH3-LO1', 'Chemistry tutor', 'Boiling point', 'Why does ethanol boil far higher than propane?', ['Hydrogen bonding between –OH groups', 'It is heavier', 'It is ionic', 'It has a double bond'], 'Both have similar molar masses.')
    q('CH3-LO2', 'Chemistry tutor', 'SN2', 'SN2 works best for:', ['primary haloalkanes', 'tertiary haloalkanes', 'alkenes', 'benzene'], 'An uncrowded carbon allows backside attack.')
    q('CH3-LO2', 'Chemistry tutor', 'SN1', 'What forms in the first step of an SN1 reaction?', ['a carbocation', 'a radical', 'an alkene', 'an ether'], 'The leaving group goes first.')
    q('CH3-LO2', 'Chemistry tutor', 'Nucleophile', 'Which is a nucleophile?', ['OH<sup>−</sup>', 'H<sup>+</sup>', 'Na<sup>+</sup>', 'CH<sub>4</sub>'], 'Electron-rich, with a lone pair.')
    q('CH3-LO2', 'Chemistry tutor', 'Rate', 'Doubling [OH<sup>−</sup>] doubles the rate. The mechanism is:', ['SN2', 'SN1', 'free radical', 'addition'], 'Both species are in the slow step.')
    q('CH3-LO2', 'Oncology pharmacist', 'Alkylating drugs', 'Cyclophosphamide damages cancer-cell DNA mainly by:', ['an SN2-type alkylation that cross-links DNA', 'oxidising DNA', 'adding H<sub>2</sub>', 'forming a disulfide'], 'Nitrogen mustards attach to guanine.', rx=True)
    q('CH3-LO2', 'Chemistry tutor', 'Conditions', 'Bromoethane + KOH in hot ethanol gives mainly:', ['ethene (elimination)', 'ethanol', 'ethanal', 'diethyl ether'], 'Aqueous OH<sup>−</sup> substitutes; hot ethanolic KOH eliminates.')
    q('CH3-LO3', 'Chemistry tutor', 'Oxidation', 'A primary alcohol is oxidised first to:', ['an aldehyde', 'a ketone', 'an ether', 'an alkene'], 'Then further to a carboxylic acid.')
    q('CH3-LO3', 'Chemistry tutor', 'Test', 'Which alcohol leaves acidified dichromate orange?', ['2-methyl-2-propanol', 'ethanol', '2-propanol', '1-butanol'], '3° alcohols are not oxidised.')
    q('CH3-LO3', 'Chemistry tutor', 'Dehydration', 'Ethanol + conc. H<sub>2</sub>SO<sub>4</sub> at 180 °C gives:', ['ethene + water', 'ethanal', 'diethyl ether', 'ethanoic acid'], 'High temperature, excess acid → alkene.')
    q('CH3-LO3', 'A&amp;E doctor', 'Poisoning', 'Methanol poisoning can be treated with fomepizole because it:', ['blocks alcohol dehydrogenase', 'oxidises methanol faster', 'is a thiol', 'neutralises acid'], 'Less formaldehyde and formic acid form.')
    q('CH3-LO3', 'Chemistry tutor', 'Body chemistry', 'In the liver, ethanol is first oxidised to:', ['acetaldehyde', 'acetone', 'methanol', 'diethyl ether'], 'Then to acetic acid, CO<sub>2</sub> and water.')
    q('CH3-LO4', 'Chemistry tutor', 'Ethers', 'Name CH<sub>3</sub>CH<sub>2</sub>OCH<sub>2</sub>CH<sub>3</sub>.', ['diethyl ether', 'ethyl ethanol', 'butanol', 'dimethyl ether'], 'Two ethyl groups on O.')
    q('CH3-LO4', 'Anaesthetist', 'History', 'The first general anaesthetic used in surgery (1846) was:', ['diethyl ether', 'ethanol', 'acetone', 'ethanethiol'], 'William Morton, Boston (FGOB 14.7).')
    q('CH3-LO4', 'Lab safety officer', 'Ether bottles', 'Why must old diethyl ether bottles be handled with care?', ['They can form explosive peroxides and are very flammable', 'Ether turns into acid', 'Ether is radioactive', 'Ether freezes'], 'Date opened bottles.')
    q('CH3-LO4', 'Puan Rohana', 'Gas smell', '"Why does my LPG smell?"', ['A thiol (ethanethiol) is added so leaks can be detected', 'Propane smells strongly', 'It contains ether', 'It is an aldehyde'], 'FGOB 14.8.')
    q('CH3-LO4', 'Chemistry tutor', 'Disulfides', 'Two cysteine –SH groups oxidise to form:', ['a disulfide bridge', 'an ether', 'a ketone', 'an ester'], 'R–S–S–R holds proteins in shape.')
    q('CH3-LO5', 'Chemistry tutor', 'Naming', 'CH<sub>3</sub>COCH<sub>2</sub>CH<sub>3</sub> is:', ['butanone', 'butanal', '2-butanol', 'propanone'], 'Ketone, 4 carbons.')
    q('CH3-LO5', 'Chemistry tutor', 'Tollens\'', 'Which gives a silver mirror?', ['ethanal', 'propanone', 'ethanol', 'diethyl ether'], 'Only aldehydes reduce Tollens\' reagent.')
    q('CH3-LO5', 'Chemistry tutor', 'Benedict\'s', 'A positive Benedict\'s test is:', ['blue → brick-red precipitate', 'orange → green', 'colourless → silver mirror', 'red-brown → colourless'], 'Cu<sup>2+</sup> reduced to Cu<sub>2</sub>O.')
    q('CH3-LO5', 'Diabetes educator', 'Breath', 'A fruity smell on a diabetic patient\'s breath is due to:', ['acetone', 'ethanol', 'formaldehyde', 'ethanethiol'], 'Possible ketoacidosis: refer urgently.')
    q('CH3-LO5', 'Chemistry tutor', 'Reduction', 'Reducing propanal with H<sub>2</sub>/Ni gives:', ['1-propanol', '2-propanol', 'propanoic acid', 'propene'], 'Aldehyde → 1° alcohol.')
    q('CH3-LO5', 'Lab assistant', 'Formalin', 'Formalin preserves specimens because formaldehyde:', ['denatures proteins', 'is a sugar', 'is an alcohol', 'evaporates'], 'FGOB 15.4.')
    return B


def config():
    return {
        'topic': 'ch3', 'title': 'Chapter 3 game',
        'kicker': 'PHD125 · Chapter 3 · Organic Compounds that Contain Oxygen and Sulphur',
        'blurb': 'You are the pharmacist on duty. Patients ask about hand rubs, gas smells, anaesthetics, anticancer drugs and a fruity breath. Every answer comes back to O and S in carbon compounds. Five stations, about 9 minutes.',
        'hub': '../../#ch3', 'slides': '../slides/', 'board': '../../leaderboard/#ch3',
        'los': LOS,
        'levels': [
            {'id': 'alc', 'name': 'Alcohol shelf', 'blurb': 'Classes, names and properties of alcohols and phenols.', 'intro': 'Sorting the antiseptic and solvent shelf: swabs, rubs, glycerin and phenols.', 'pool': ['CH3-LO1'], 'n': 5, 'secs': 30},
            {'id': 'sn', 'name': 'Mechanism desk', 'blurb': 'SN1, SN2 and elimination.', 'intro': 'The intern is revising for an exam on substitution reactions. Help with nucleophiles, carbocations and conditions.', 'pool': ['CH3-LO2'], 'n': 5, 'secs': 35},
            {'id': 'bench', 'name': 'Oxidation bench', 'type': 'drag', 'blurb': 'Hands-on: dichromate results for four compounds.', 'intro': 'Four unlabelled samples, one bottle of acidified dichromate. Predict what each gives.', 'secs': 75},
            {'id': 'lab', 'name': 'Reactions lab', 'blurb': 'Oxidation, dehydration, ethers, thiols, aldehydes and ketones.', 'intro': 'Questions from the lab and the ward: poisonings, anaesthetics, gas smells and sugar tests.', 'pool': ['CH3-LO3', 'CH3-LO4', 'CH3-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': oxidation_bench(),
        'bank': bank(),
    }
