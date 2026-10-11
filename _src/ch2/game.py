"""PHD125 Chapter 2 · Pharmacy Shift game content (bank items: o[0] is always the correct option)."""
import base64

LOS = [
    ['CH2-LO1', 'Name and draw alkanes and cycloalkanes using IUPAC rules, and recognise structural isomers'],
    ['CH2-LO2', 'Relate the physical properties of hydrocarbons to their structure'],
    ['CH2-LO3', 'Write equations for the combustion and halogenation of alkanes, and describe the free-radical mechanism'],
    ['CH2-LO4', 'Name and draw alkenes, alkynes and benzene derivatives, and identify cis-trans isomers and chiral carbons'],
    ['CH2-LO5', 'Predict the products of addition reactions, addition polymerisation and substitution of benzene'],
]


def reaction_map():
    """Hands-on round: propene in the middle, four reagent arrows lettered A to D; drop the product on each."""
    W, H = 440, 300
    import sys
    from figs import mol
    def emb(smi, x, y, w, h):
        u = mol(smi, w, h)
        return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{u}"/>'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Propene in the centre with four reagent arrows lettered A to D: hydrogen with nickel, bromine, hydrogen bromide, and water with acid">',
         f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/>', emb('C=CC', 165, 115, 110, 70),
         '<text x="220" y="200" text-anchor="middle" font-size="13" font-family="sans-serif" fill="#1B2A41">propene</text>',
         '<g stroke="#2F6F9F" stroke-width="2.5" fill="none">',
         '<path d="M165 130 L80 70"/><path d="M275 130 L360 70"/><path d="M165 175 L80 235"/><path d="M275 175 L360 235"/></g>',
         '<g fill="#2F6F9F"><path d="M80 70 l12 2 l-6 7 z"/><path d="M360 70 l-12 2 l6 7 z"/><path d="M80 235 l12 -2 l-6 -7 z"/><path d="M360 235 l-12 -2 l6 -7 z"/></g>',
         '<g font-family="sans-serif" font-size="12.5" fill="#1B2A41">',
         '<text x="140" y="82" text-anchor="middle">H₂, Ni</text><text x="300" y="82" text-anchor="middle">Br₂</text>',
         '<text x="100" y="196" text-anchor="middle">HBr</text><text x="352" y="196" text-anchor="middle">H₂O, H₂SO₄</text></g></svg>']
    svg = ''.join(s)
    return {
        'lo': 'CH2-LO5', 'title': 'Complete the reaction map for propene',
        'how': 'Each arrow is a reagent added to propene. Drag the major product onto each letter, or tap a product and then tap a letter. Two products do not belong anywhere.',
        'svg': svg,
        'zones': [{'id': 'A', 'x': 14.0, 'y': 16.0}, {'id': 'B', 'x': 86.0, 'y': 16.0}, {'id': 'C', 'x': 14.0, 'y': 84.0}, {'id': 'D', 'x': 86.0, 'y': 84.0}],
        'chips': [
            {'t': 'propane', 's': 'CH₃CH₂CH₃', 'z': 0},
            {'t': '1,2-dibromopropane', 's': 'CH₂BrCHBrCH₃', 'z': 1},
            {'t': '2-bromopropane', 's': 'CH₃CHBrCH₃', 'z': 2},
            {'t': '2-propanol', 's': 'CH₃CH(OH)CH₃', 'z': 3},
            {'t': '1-bromopropane', 's': 'CH₂BrCH₂CH₃', 'z': -1},
            {'t': '1-propanol', 's': 'CH₂(OH)CH₂CH₃', 'z': -1}],
        'why': 'Hydrogenation gives propane (A); bromine adds to both carbons (B). For HBr and H₂O, Markovnikov\'s rule puts the H on the CH₂ end and the Br or OH on the middle carbon: 2-bromopropane (C) and 2-propanol (D). 1-Bromopropane and 1-propanol are only minor products.'}


def bank():
    B = []
    def q(lo, who, role, text, opts, why, rx=False):
        it = {'lo': lo, 'who': who, 'role': role, 'q': text, 'o': opts, 'why': why}
        if rx: it['rx'] = True
        B.append(it)
    # LO1
    q('CH2-LO1', 'Chemistry tutor', 'Formula', 'What is the molecular formula of heptane?', ['C<sub>7</sub>H<sub>16</sub>', 'C<sub>7</sub>H<sub>14</sub>', 'C<sub>6</sub>H<sub>14</sub>', 'C<sub>7</sub>H<sub>12</sub>'], 'C<sub>n</sub>H<sub>2n+2</sub> with n = 7.')
    q('CH2-LO1', 'Chemistry tutor', 'Naming', 'Name CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub>.', ['2-methylbutane', '3-methylbutane', '2-ethylpropane', 'pentane'], 'Four-carbon chain, methyl on C2.')
    q('CH2-LO1', 'Chemistry tutor', 'Naming', 'Name (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub>.', ['2,4-dimethylpentane', '2,4-methylpentane', '1,1,3,3-tetramethylpropane', '2,4-dimethylhexane'], 'Five-carbon chain with methyls on C2 and C4.')
    q('CH2-LO1', 'Chemistry tutor', 'Isomers', 'Which pair are structural isomers?', ['butane and 2-methylpropane', 'butane and butene', 'ethane and ethene', 'propane and cyclopropane'], 'Both C<sub>4</sub>H<sub>10</sub>, arranged differently.')
    q('CH2-LO1', 'Chemistry tutor', 'Rings', 'What is the formula of cyclohexane?', ['C<sub>6</sub>H<sub>12</sub>', 'C<sub>6</sub>H<sub>14</sub>', 'C<sub>6</sub>H<sub>6</sub>', 'C<sub>6</sub>H<sub>10</sub>'], 'Cycloalkanes are C<sub>n</sub>H<sub>2n</sub>.')
    q('CH2-LO1', 'Intern', 'Spot the error', '"2-ethylbutane" should be named:', ['3-methylpentane', '2-ethylbutane is correct', '2-methylpentane', 'hexane'], 'The ethyl extends the longest chain to five carbons.')
    # LO2
    q('CH2-LO2', 'Puan Lina', 'Gas leak', '"Why does a leak from my LPG cylinder stay near the floor?"', ['Propane and butane are denser than air', 'LPG is lighter than air', 'LPG is a liquid', 'LPG dissolves in air'], 'LPG (about 1.9–2.5 g/L) is heavier than air (about 1.2 g/L).')
    q('CH2-LO2', 'Chemistry tutor', 'Boiling points', 'Which has the higher boiling point?', ['octane', 'hexane', 'butane', 'methane'], 'Longer chain, stronger dispersion forces.')
    q('CH2-LO2', 'Chemistry tutor', 'Branching', 'Pentane boils at 36 °C. Its branched isomer neopentane boils at:', ['9.5 °C', '36 °C', '69 °C', '125 °C'], 'Branching lowers the boiling point: less surface contact.')
    q('CH2-LO2', 'Compounding pharmacist', 'Ointment base', 'Why is white soft paraffin used as an ointment base?', ['It is an inert, water-repelling alkane mixture', 'It dissolves in water', 'It is an acid', 'It is aromatic'], 'Alkanes are nonpolar and unreactive.', rx=True)
    q('CH2-LO2', 'Chemistry tutor', 'Solubility', 'Hexane is a good solvent for:', ['soybean oil', 'sodium chloride', 'water', 'sugar'], 'Like dissolves like: nonpolar dissolves nonpolar (Ball 12.E).')
    # LO3
    q('CH2-LO3', 'Encik Azman', 'Heater', '"My gas heater gives me a headache in a closed room. Why?"', ['Incomplete combustion makes carbon monoxide', 'It makes too much water', 'Alkanes are acids', 'It makes oxygen'], 'Ventilate and get the heater checked: CO is deadly.')
    q('CH2-LO3', 'Chemistry tutor', 'Balancing', 'How many O<sub>2</sub> are needed to burn one CH<sub>4</sub> completely?', ['2', '1', '3', '4'], 'CH<sub>4</sub> + 2 O<sub>2</sub> → CO<sub>2</sub> + 2 H<sub>2</sub>O.')
    q('CH2-LO3', 'Chemistry tutor', 'Halogenation', 'What starts the reaction between methane and chlorine?', ['UV light (or high temperature)', 'A nickel catalyst', 'Water', 'Darkness'], 'Light splits Cl<sub>2</sub> into radicals.')
    q('CH2-LO3', 'Chemistry tutor', 'Mechanism', 'Cl• + CH<sub>4</sub> → •CH<sub>3</sub> + HCl is which step?', ['Propagation', 'Initiation', 'Termination', 'Addition'], 'A radical reacts and makes a new radical.')
    q('CH2-LO3', 'Chemistry tutor', 'Radicals', 'What is a free radical?', ['A species with an unpaired electron', 'A positive ion', 'A double bond', 'A noble gas'], 'Radicals are very reactive.')
    q('CH2-LO3', 'Pharmacy student', 'Local anaesthetic', 'Which haloalkane is sprayed on skin as a quick local anaesthetic?', ['chloroethane', 'carbon tetrachloride', 'methane', 'CFC-12'], 'It evaporates fast and cools the skin (NAM-ALKANE 12.8).')
    # LO4
    q('CH2-LO4', 'Chemistry tutor', 'Naming', 'Name CH<sub>2</sub>=CHCH<sub>2</sub>CH<sub>3</sub>.', ['1-butene', '2-butene', '3-butene', 'butyne'], 'Lowest number to the double bond.')
    q('CH2-LO4', 'Chemistry tutor', 'Alkynes', 'CH<sub>3</sub>C≡CCH<sub>3</sub> is:', ['2-butyne', '2-butene', '1-butyne', 'butane'], '-yne = triple bond, starting at C2.')
    q('CH2-LO4', 'Chemistry tutor', 'Cis-trans', 'Which shows cis-trans isomerism?', ['CH<sub>3</sub>CH=CHCH<sub>3</sub>', 'CH<sub>2</sub>=CHCH<sub>3</sub>', '(CH<sub>3</sub>)<sub>2</sub>C=CH<sub>2</sub>', 'CH<sub>2</sub>=CH<sub>2</sub>'], 'Each C=C carbon needs two different groups.')
    q('CH2-LO4', 'Pharmacy student', 'Chirality', 'Why do pharmacists care about chiral drugs such as thalidomide?', ['Mirror-image forms can act differently in the body', 'Chiral drugs are always inactive', 'Chiral drugs cannot dissolve', 'They have no carbon'], 'Receptors and enzymes are chiral too.')
    q('CH2-LO4', 'Chemistry tutor', 'Aromatic names', 'Two groups at positions 1 and 4 on a benzene ring are:', ['para', 'ortho', 'meta', 'cis'], 'o- = 1,2; m- = 1,3; p- = 1,4.')
    q('CH2-LO4', 'Nutrition talk', 'Trans fats', 'Trans fats differ from natural cis fats because their chains are:', ['straighter, so they pack like saturated fats', 'more bent', 'aromatic', 'shorter'], 'Trans fats raise LDL cholesterol.')
    # LO5
    q('CH2-LO5', 'Lab assistant', 'Bromine test', 'Bromine turns colourless when shaken with a liquid. The liquid most likely contains:', ['a C=C double bond', 'only single bonds', 'a benzene ring', 'water only'], 'Alkenes add Br<sub>2</sub> across the C=C.')
    q('CH2-LO5', 'Chemistry tutor', 'Hydrogenation', 'Which catalyst is used to add H<sub>2</sub> to an alkene?', ['Ni or Pt', 'H<sub>2</sub>SO<sub>4</sub>', 'FeBr<sub>3</sub>', 'UV light'], 'Hydrogenation needs a metal catalyst.')
    q('CH2-LO5', 'Chemistry tutor', 'Markovnikov', 'Propene + HBr gives mainly:', ['2-bromopropane', '1-bromopropane', '1,2-dibromopropane', 'propane'], 'H goes to the carbon with more H.')
    q('CH2-LO5', 'Store manager', 'IV bags', 'IV fluid bags are often made of PVC. Its monomer is:', ['chloroethene (vinyl chloride)', 'ethene', 'propene', 'benzene'], 'CH<sub>2</sub>=CHCl → polyvinyl chloride.')
    q('CH2-LO5', 'Chemistry tutor', 'Benzene', 'Benzene + HNO<sub>3</sub> (conc. H<sub>2</sub>SO<sub>4</sub>) gives:', ['nitrobenzene + H<sub>2</sub>O', 'an addition product', 'cyclohexane', 'no reaction'], 'Nitration is a substitution.')
    q('CH2-LO5', 'Chemistry tutor', 'Alkynes', 'How many molecules of H<sub>2</sub> does ethyne take up to become ethane?', ['2', '1', '3', '4'], 'A triple bond adds twice.')
    return B


def config():
    return {
        'topic': 'ch2', 'title': 'Chapter 2 game',
        'kicker': 'PHD125 · Chapter 2 · Saturated and Unsaturated Hydrocarbons',
        'blurb': 'You are the pharmacist on duty. Customers ask about gas leaks, ointment bases, IV bags and margarine. Every answer comes back to hydrocarbons. Five stations, about 9 minutes.',
        'hub': '../../#ch2', 'slides': '../slides/', 'board': '../../leaderboard/#ch2',
        'los': LOS,
        'levels': [
            {'id': 'names', 'name': 'Naming desk', 'blurb': 'IUPAC names, isomers and rings.', 'intro': 'The intern is checking labels in the solvent store. Help with names, formulas and isomers.', 'pool': ['CH2-LO1'], 'n': 5, 'secs': 35},
            {'id': 'store', 'name': 'Gas and solvent store', 'blurb': 'Properties and reactions of alkanes.', 'intro': 'Questions about gas cylinders, heaters, solvents and ointment bases.', 'pool': ['CH2-LO2', 'CH2-LO3'], 'n': 6, 'secs': 30},
            {'id': 'map', 'name': 'Reaction map', 'type': 'drag', 'blurb': 'Hands-on: products of four additions to propene.', 'intro': 'The lab needs four propene derivatives. Put the right major product at the end of each arrow.', 'secs': 75},
            {'id': 'lab', 'name': 'Unsaturated lab', 'blurb': 'Alkenes, alkynes, aromatics, isomers and reactions.', 'intro': 'Bromine tests, cis and trans fats, chiral drugs and the plastics on the shelf.', 'pool': ['CH2-LO4', 'CH2-LO5'], 'n': 6, 'secs': 30},
            {'id': 'rush', 'name': 'Rush hour', 'blurb': 'Five quick patients, one from every outcome. Points ×1.5.', 'intro': 'The queue is out the door. One patient for each outcome, less time each, and every right answer earns 1.5 times the points.', 'pool': [l[0] for l in LOS], 'n': 5, 'secs': 15, 'mult': 1.5}],
        'hands': reaction_map(),
        'bank': bank(),
    }
