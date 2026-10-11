"""PHD125 Chapter 2 · Saturated and Unsaturated Hydrocarbons · lecture slide content.
2.1 Alkanes: NAM-ALKANE note (LibreTexts 12.3, 12.6-12.10, Sharpe Elles remix of Ball, CC BY-NC-SA 3.0).
2.2 Alkenes, Alkynes & Aromatics: Ball Ch 13 (CC BY-NC-SA 3.0) and FGOB 13.1-13.4, 13.6-13.9 (same licence).
Added by Dr. NAM (original text; the source pages FGOB 13.5 and 13.10 are empty placeholders): types of organic
reactions, free-radical mechanism, HX addition and Markovnikov's rule, alkyne addition, benzene substitution,
the brief introduction to chirality, and the pharmacy links."""
from figs import mol, row, scheme, stack


def mini(smi, hs=False, h=54):
    return f'<img src="{mol(smi, 190, 84, hs=hs)}" alt="" style="height:{h}px;display:block;background:#fff;border-radius:6px;padding:1px 4px">'


LO1, LO2, LO3, LO4, LO5 = 'CH2-LO1', 'CH2-LO2', 'CH2-LO3', 'CH2-LO4', 'CH2-LO5'

META = {
    "code": "CH2", "chapter": "Chapter 2", "title": "Saturated and Unsaturated Hydrocarbons", "short": "Saturated and Unsaturated Hydrocarbons",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: Dr. NAM's NAM-ALKANE note (LibreTexts 12.3, 12.6–12.10) and Ball, Hill & Scott, The Basics of GOB Chemistry, chapter 13",
    "attrib": ("Adapted from LibreTexts <i>Introduction to Organic Chemistry – Alkanes</i> 12.3, 12.6–12.10 (Lisa Sharpe Elles, remixed from Ball, Hill &amp; Scott), "
               "<i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 13 and <i>Fundamentals of General Organic and Biological Chemistry</i> 13.1–13.4 and 13.6–13.9, "
               "all CC BY-NC-SA 3.0. Reaction types, the free-radical mechanism, Markovnikov's rule, alkyne addition, benzene substitution, chirality and the pharmacy links "
               "are original material by Dr. NAM. Structures drawn with RDKit. Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["butane", "methylpropane", "cyclohexane"], "2": ["ethene", "benzene", "ethyne"]},
    "titlemol": ["butane", "ethene", "benzene", "ethyne"], "darkmol": "benzene",
    "next": "Next chapter: Organic Compounds that Contain Oxygen and Sulphur",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Name and draw alkanes and cycloalkanes using IUPAC rules, and recognise structural isomers"],
    [LO2, "Relate the physical properties of hydrocarbons (boiling point, solubility, density) to their structure"],
    [LO3, "Write equations for the combustion and halogenation of alkanes, and describe the free-radical mechanism"],
    [LO4, "Name and draw alkenes, alkynes and benzene derivatives, and identify cis-trans isomers and chiral carbons"],
    [LO5, "Predict the products of addition reactions of alkenes and alkynes (including Markovnikov's rule), addition polymerisation and substitution of benzene"],
]


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Saturated and Unsaturated Hydrocarbons", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 2",
         "notes": "Chapter 2 of the course outline, in two subchapters: alkanes, then alkenes, alkynes and aromatic compounds."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1–LO3 belong to 2.1 Alkanes; LO4–LO5 to 2.2. The same outcomes are used in every Chapter 2 activity."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>2.1 Alkanes</b> (NAM-ALKANE 12.3, 12.6–12.10): structure and isomers, IUPAC names, cycloalkanes, physical properties, combustion and halogenation",
        "<b>2.2 Alkenes, Alkynes &amp; Aromatics</b> (Ball Ch 13): names, cis-trans isomers and chirality, addition reactions, polymers, benzene and its substitution reactions"],
         "notes": "Jump to either subchapter from here."})
    add({"t": "hook", "title": "Think first",
         "q": "A natural-gas leak in a kitchen is cleared by opening a high window. A leak from an LPG cylinder is far more dangerous. Why?",
         "a": "Natural gas is mostly <b>methane</b> (about 0.67 g/L), lighter than air (about 1.2 g/L), so it rises and escapes. LPG is <b>propane and butane</b> (about 1.9–2.5 g/L), heavier than air, so it collects near the floor. Small structural changes in alkanes change their properties. (NAM-ALKANE 12.7, Looking Closer)",
         "notes": "Pairs discuss for one minute."})

    # ================= 2.1 ALKANES =================
    add({"t": "divider", "num": 1, "title": "Alkanes", "lo": "CH2-LO1 to LO3", "src": "NAM-ALKANE 12.3, 12.6–12.10",
         "blurb": "Saturated hydrocarbons: how to name them, why they behave as they do, and the two reactions they undergo."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "Alkanes are saturated hydrocarbons",
         "items": ["<b>Alkanes</b> contain only C–C and C–H <b>single bonds</b>. Each carbon is bonded to four other atoms, the most possible, so alkanes are <b>saturated</b>.",
                   "Methane (CH<sub>4</sub>), ethane (C<sub>2</sub>H<sub>6</sub>) and propane (C<sub>3</sub>H<sub>8</sub>) start a series in which each member differs from the next by one <b>CH<sub>2</sub></b> unit (methylene). This is a <b>homologous series</b>.",
                   "General formula: <b>C<sub>n</sub>H<sub>2n+2</sub></b>. An alkane with 8 carbons is C<sub>8</sub>H<sub>(2×8)+2</sub> = <b>C<sub>8</sub>H<sub>18</sub></b>.",
                   "Saturated fats contain long alkane-like chains with no C=C double bonds."],
         "side": {"h": "Quick check", "body": "The alkane with 12 carbons is C<sub>12</sub>H<sub>26</sub> (Ball 12.E)."},
         "notes": "NAM-ALKANE 12.3."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "The first ten straight-chain alkanes",
         "head": ["C atoms", "Parent stem", "Name", "Molecular formula", "Condensed formula"],
         "rows": [["1", "meth-", "methane", "CH<sub>4</sub>", "CH<sub>4</sub>"], ["2", "eth-", "ethane", "C<sub>2</sub>H<sub>6</sub>", "CH<sub>3</sub>CH<sub>3</sub>"],
                  ["3", "prop-", "propane", "C<sub>3</sub>H<sub>8</sub>", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>3</sub>"], ["4", "but-", "butane", "C<sub>4</sub>H<sub>10</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>2</sub>CH<sub>3</sub>"],
                  ["5", "pent-", "pentane", "C<sub>5</sub>H<sub>12</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>3</sub>CH<sub>3</sub>"], ["6", "hex-", "hexane", "C<sub>6</sub>H<sub>14</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>4</sub>CH<sub>3</sub>"],
                  ["7", "hept-", "heptane", "C<sub>7</sub>H<sub>16</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>5</sub>CH<sub>3</sub>"], ["8", "oct-", "octane", "C<sub>8</sub>H<sub>18</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>6</sub>CH<sub>3</sub>"],
                  ["9", "non-", "nonane", "C<sub>9</sub>H<sub>20</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>7</sub>CH<sub>3</sub>"], ["10", "dec-", "decane", "C<sub>10</sub>H<sub>22</sub>", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>8</sub>CH<sub>3</sub>"]],
         "widths": [1.2, 1.6, 1.8, 2.2, 3.2], "caption": "Source: NAM-ALKANE Table 12.6.1. Learn the ten stems: every family in this course reuses them.",
         "notes": "NAM-ALKANE 12.6 table. (CH2)n shorthand added for space."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Structural isomers",
         "fig": {"cap": "The three isomers of C<sub>5</sub>H<sub>12</sub>, with their boiling points (NAM-ALKANE 12.3).",
                 "data": row([(mol("CCCCC", 230, 120), "pentane · 36.1 °C"), (mol("CCC(C)C", 230, 120), "isopentane · 27.7 °C"), (mol("CC(C)(C)C", 230, 120), "neopentane · 9.5 °C")], w=260, h=120)},
         "items": ["<b>Isomers</b> have the <b>same molecular formula</b> but a <b>different arrangement</b> of atoms. They are different compounds with different properties. (IUPAC names: 2-methylbutane, 2,2-dimethylpropane.)",
                   "From four carbons up, chains can <b>branch</b>: butane and 2-methylpropane are both C<sub>4</sub>H<sub>10</sub>.",
                   "Tip: trace the carbon chain with your pencil. Bending a chain does <b>not</b> make an isomer; only a different connection does."],
         "notes": "NAM-ALKANE 12.3. Isomer counts: 3 pentanes, 5 hexanes, 9 heptanes, 18 octanes (12.6)."})
    add({"t": "tryit", "sec": 1, "lo": LO1, "title": "Try it · Same or isomers?",
         "q": "Do these represent the same compound or isomers? (a) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> and CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>3</sub> (b) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> and the same chain drawn with a bend",
         "a": "(a) <b>Isomers</b>: both C<sub>5</sub>H<sub>12</sub>, but the second has a branch (2-methylbutane). (b) <b>The same compound</b>: a bend is just rotation about a C–C bond (Ball 12.E).",
         "notes": "Ball 12.E, section 12.3 exercise 5."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Alkyl groups",
         "head": ["Group", "Condensed formula", "Structure", "From"],
         "rows": [["methyl", "–CH<sub>3</sub>", mini("[CH3]*", h=36), "methane"], ["ethyl", "–CH<sub>2</sub>CH<sub>3</sub>", mini("*CC", h=36), "ethane"],
                  ["propyl", "–CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>", mini("*CCC", h=36), "propane"], ["isopropyl", "–CH(CH<sub>3</sub>)<sub>2</sub>", mini("*C(C)C", h=36), "propane"],
                  ["butyl", "–CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>", mini("*CCCC", h=36), "butane"], ["tert-butyl", "–C(CH<sub>3</sub>)<sub>3</sub>", mini("*C(C)(C)C", h=36), "2-methylpropane"]],
         "widths": [1.6, 3.0, 2.0, 2.0],
         "caption": "An alkane minus one H (* = attachment point): change <b>-ane</b> to <b>-yl</b>. sec-Butyl and isobutyl: NAM-ALKANE Table 12.6.2.",
         "notes": "NAM-ALKANE 12.6, Common Alkyl Groups."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Naming alkanes: four IUPAC steps",
         "head": ["Step", "What to do"],
         "rows": [["1 · Parent chain", "Find the <b>longest continuous chain</b> (it may bend). Name it from the stem + <b>-ane</b>."],
                  ["2 · Number", "Number the chain from the end that gives the substituents the <b>lowest numbers</b>."],
                  ["3 · Substituents", "Name each branch and its position. Repeated groups use <b>di-, tri-, tetra-</b> and give every position (2,2- or 2,3-)."],
                  ["4 · Write it", "Substituents in <b>alphabetical order</b> (ignore di-, tri-), then the parent. Numbers–letters: hyphen. Numbers–numbers: comma."]],
         "widths": [2.0, 7.0], "caption": "Structure of a name: <b>prefix (substituents) + parent (number of carbons) + suffix (family)</b>, e.g. 2-methylpropane.",
         "notes": "NAM-ALKANE 12.6 simplified IUPAC rules."})
    add({"t": "example", "sec": 1, "lo": LO1, "title": "Example 2.1 · Name it",
         "q": "Name this alkane.",
         "fig": {"cap": "", "data": mol("CCCC(C)(CC)CCCC", 360, 200)},
         "steps": ["Longest chain: <b>8 carbons</b> → octane.",
                   "Both branches sit on the same carbon. Number from the left so that carbon is <b>C4</b> (from the right it would be C5).",
                   "Substituents: an <b>ethyl</b> and a <b>methyl</b> on C4.",
                   "Alphabetical order (e before m): <b>4-ethyl-4-methyloctane</b>."],
         "notes": "NAM-ALKANE 12.6 Example, part 3."})
    add({"t": "example", "sec": 1, "lo": LO1, "title": "Example 2.2 · Draw it",
         "q": "Draw the structure of <b>4-ethyl-2-methylheptane</b>.",
         "fig": {"cap": "", "data": mol("CC(C)CC(CC)CCC", 360, 200)},
         "steps": ["Start with the parent: <b>hept</b>ane, a chain of 7 carbons. Number it 1 to 7.",
                   "Put a <b>methyl</b> on C2 and an <b>ethyl</b> on C4.",
                   "Fill in hydrogens so every carbon has four bonds: CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH(CH<sub>2</sub>CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>.",
                   "Check: C<sub>10</sub>H<sub>22</sub> fits C<sub>n</sub>H<sub>2n+2</sub>."],
         "notes": "NAM-ALKANE 12.6 drawing example (b)."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "Common naming mistakes",
         "items": ["<b>Missing the longest chain.</b> \"2-ethylbutane\" is wrong: the ethyl extends the chain, so the name is <b>3-methylpentane</b>.",
                   "<b>Numbering from the wrong end.</b> \"4-methylpentane\" is wrong: number from the other end → <b>2-methylpentane</b>.",
                   "<b>Alphabetising with the prefix.</b> Write 4-ethyl-2,3-dimethylhexane: <b>e</b>thyl comes before <b>m</b>ethyl; the di- is ignored.",
                   "<b>Forgetting a number.</b> Two groups need two numbers: <b>2,2-dimethylpropane</b>, not 2-dimethylpropane."],
         "side": {"h": "Self-check", "body": "Count the carbons in your name and in the structure. They must match."},
         "notes": "Original teaching slide, using the rules from NAM-ALKANE 12.6."})
    add({"t": "tryit", "sec": 1, "lo": LO1, "title": "Try it · Name these",
         "q": "Name: (a) CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (b) (CH<sub>3</sub>)<sub>3</sub>CCH<sub>2</sub>C(CH<sub>3</sub>)<sub>3</sub>",
         "a": "(a) <b>3-methylhexane</b> (six-carbon chain, methyl on C3). (b) <b>2,2,4,4-tetramethylpentane</b> (five-carbon chain, two methyls on C2 and two on C4).",
         "notes": "Ball 12.E, section 12.5 exercises 6a and 7a."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Cycloalkanes",
         "fig": {"cap": "Cycloalkanes as line structures: each corner is a CH<sub>2</sub>.",
                 "data": row([(mol("C1CC1", 160, 110), "cyclopropane · 60°"), (mol("C1CCC1", 160, 110), "cyclobutane · ~90°"), (mol("C1CCCC1", 160, 110), "cyclopentane · ~108°"), (mol("C1CCCCC1", 160, 110), "cyclohexane · 109.5°")], w=230, h=110)},
         "items": ["Cycloalkanes are saturated rings: general formula <b>C<sub>n</sub>H<sub>2n</sub></b>. Name them with <b>cyclo-</b> + the alkane name.",
                   "Angles far from 109.5° cause <b>ring strain</b>: cyclopropane is unstable and reactive. Cyclohexane puckers to reach about 109.5° and is very stable.",
                   "Rings cannot rotate freely about their C–C bonds (<b>restricted rotation</b>), so they are more rigid than open chains."],
         "notes": "NAM-ALKANE 12.9–12.10. Cyclopropane was once a fast-acting anaesthetic but forms explosive mixtures with air."})
    add({"t": "tryit", "sec": 1, "lo": LO1, "title": "Try it · Draw rings",
         "q": "Draw (a) methylcyclobutane and (b) ethylcyclohexane. Write their molecular formulas.",
         "afig": {"data": row([(mol("CC1CCC1", 170, 100), "methylcyclobutane"), (mol("CCC1CCCCC1", 170, 100), "ethylcyclohexane")], w=200, h=100)},
         "a": "(a) A square with a CH<sub>3</sub> on one corner: <b>C<sub>5</sub>H<sub>10</sub></b>. (b) A hexagon with a CH<sub>2</sub>CH<sub>3</sub> on one corner: <b>C<sub>8</sub>H<sub>16</sub></b>. A single substituent needs no number.",
         "notes": "NAM-ALKANE 12.10 example and exercise."})
    add({"t": "table", "sec": 1, "lo": LO2, "title": "Physical properties of alkanes",
         "head": ["Alkane", "Formula", "Melting point (°C)", "Boiling point (°C)", "State at 20 °C"],
         "rows": [["methane", "CH<sub>4</sub>", "−182", "−164", "gas"], ["propane", "C<sub>3</sub>H<sub>8</sub>", "−190", "−42", "gas"],
                  ["butane", "C<sub>4</sub>H<sub>10</sub>", "−138", "−1", "gas"], ["pentane", "C<sub>5</sub>H<sub>12</sub>", "−130", "36", "liquid"],
                  ["hexane", "C<sub>6</sub>H<sub>14</sub>", "−95", "69", "liquid"], ["octane", "C<sub>8</sub>H<sub>18</sub>", "−57", "125", "liquid"],
                  ["decane", "C<sub>10</sub>H<sub>22</sub>", "−30", "174", "liquid"]],
         "widths": [1.8, 1.6, 2.0, 2.0, 1.8], "caption": "Source: NAM-ALKANE Table 12.7.1. Liquid alkanes have densities of about 0.63–0.73 g/mL, less than water.",
         "notes": "NAM-ALKANE 12.7."})
    add({"t": "bullets", "sec": 1, "lo": LO2, "title": "Why alkanes behave this way",
         "items": ["Alkanes are <b>nonpolar</b>, so they are <b>insoluble in water</b> but dissolve fats, oils and waxes. They are less dense than water, so oil floats.",
                   "Boiling points <b>rise with chain length</b>: bigger molecules have larger surfaces and stronger <b>dispersion forces</b>.",
                   "<b>Branching lowers</b> the boiling point: pentane 36.1 °C, neopentane 9.5 °C. Compact molecules touch less.",
                   "Pharmacy link: <b>white soft paraffin</b> (petroleum jelly) is a common ointment base, and <b>liquid paraffin</b> is used as an emollient and laxative. Both are alkane mixtures: inert, water-repelling and non-irritant."],
         "notes": "NAM-ALKANE 12.7. Pharmacy link is original."})
    add({"t": "check", "sec": 1, "lo": LO2, "title": "Quick check",
         "q": "Without a table, which has the higher boiling point: hexane or octane? (Ball 12.E)",
         "opts": ["Hexane, because it is smaller", "Octane, because larger molecules have stronger dispersion forces", "They are the same: both are alkanes", "Hexane, because it is branched"],
         "ans": 1, "why": "Octane has the greater molar mass and surface area, so stronger dispersion forces (125 °C vs 69 °C).", "notes": "Answer B."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO3, "title": "Reaction 1 · Combustion",
         "fig": {"cap": "Complete combustion of methane (NAM-ALKANE 12.8).",
                 "data": scheme([('m', 'C', 'CH₄', 120, True), ('+',), ('t', '2 O₂', 80), ('>', 'flame or spark', ''), ('t', 'CO₂ + 2 H₂O + heat', 260)], h=120)},
         "items": ["Alkanes are so unreactive they were called <b>paraffins</b> (Latin: \"little affinity\"). Heat or light is needed to start their two reactions.",
                   "<b>Complete combustion</b> (plenty of O<sub>2</sub>): CO<sub>2</sub> + H<sub>2</sub>O + a lot of heat. This is why alkanes are fuels: natural gas, LPG, petrol, diesel.",
                   "<b>Incomplete combustion</b> (limited O<sub>2</sub>): <b>carbon monoxide</b> (CO) and soot form. CO binds haemoglobin over 200 times more strongly than O<sub>2</sub>; badly ventilated heaters kill people every year."],
         "notes": "NAM-ALKANE 12.8 Combustion. CO affinity figure is standard (about 200–250×). CO poisoning is treated with 100% oxygen."})
    add({"t": "example", "sec": 1, "lo": LO3, "title": "Example 2.3 · Balance a combustion",
         "q": "Write a balanced equation for the complete combustion of propane, C<sub>3</sub>H<sub>8</sub>, the main gas in LPG.",
         "steps": ["Products: CO<sub>2</sub> and H<sub>2</sub>O. Balance C: 3 C → <b>3 CO<sub>2</sub></b>.",
                   "Balance H: 8 H → <b>4 H<sub>2</sub>O</b>.",
                   "Balance O: 3×2 + 4×1 = 10 O atoms → <b>5 O<sub>2</sub></b>.",
                   "<b>C<sub>3</sub>H<sub>8</sub> + 5 O<sub>2</sub> → 3 CO<sub>2</sub> + 4 H<sub>2</sub>O</b>. Shortcut: C<sub>n</sub>H<sub>2n+2</sub> needs (3n+1)/2 O<sub>2</sub>."],
         "notes": "Original worked example; PHD115 balancing skills."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO3, "title": "Reaction 2 · Halogenation (substitution)",
         "fig": {"cap": "Chlorination of methane: a Cl atom replaces an H atom (NAM-ALKANE 12.8).",
                 "data": scheme([('m', 'C', 'CH₄', 110, True), ('+',), ('t', 'Cl₂', 60), ('>', 'UV light or heat', ''), ('m', 'CCl', 'CH₃Cl (chloromethane)', 180, True), ('+',), ('t', 'HCl', 60)], h=120)},
         "items": ["With <b>UV light</b> or high temperature, Cl<sub>2</sub> or Br<sub>2</sub> <b>substitutes</b> for hydrogen. In the dark at room temperature, nothing happens.",
                   "With more chlorine, a <b>mixture</b> forms: CH<sub>3</sub>Cl, CH<sub>2</sub>Cl<sub>2</sub>, CHCl<sub>3</sub> and CCl<sub>4</sub>. Excess methane favours CH<sub>3</sub>Cl.",
                   "Reactivity: F<sub>2</sub> (explosive) > Cl<sub>2</sub> > Br<sub>2</sub> > I<sub>2</sub> (too unreactive)."],
         "notes": "NAM-ALKANE 12.8 Halogenation; Ball 12.E answer: F2 most, I2 least reactive."})
    add({"t": "table", "sec": 1, "lo": LO3, "title": "How it happens: the free-radical mechanism",
         "head": ["Stage", "Equation", "What happens"],
         "rows": [["Initiation", "Cl–Cl → <b>Cl•</b> + <b>Cl•</b>", "UV light splits Cl<sub>2</sub> evenly: each Cl keeps one electron. Cl• is a <b>free radical</b> (an unpaired electron)."],
                  ["Propagation 1", "Cl• + CH<sub>4</sub> → <b>•CH<sub>3</sub></b> + HCl", "The radical takes an H atom, making a methyl radical."],
                  ["Propagation 2", "•CH<sub>3</sub> + Cl<sub>2</sub> → CH<sub>3</sub>Cl + <b>Cl•</b>", "The methyl radical takes a Cl atom and releases a new Cl•: a <b>chain reaction</b>."],
                  ["Termination", "Cl• + Cl• → Cl<sub>2</sub> · •CH<sub>3</sub> + Cl• → CH<sub>3</sub>Cl · •CH<sub>3</sub> + •CH<sub>3</sub> → C<sub>2</sub>H<sub>6</sub>", "Two radicals meet and pair up, ending the chain."]],
         "widths": [1.6, 3.6, 4.4],
         "caption": "Why a mixture forms: Cl• also attacks CH<sub>3</sub>Cl, CH<sub>2</sub>Cl<sub>2</sub> and CHCl<sub>3</sub>. Traces of ethane in the product show that •CH<sub>3</sub> radicals exist.",
         "notes": "Original summary of the standard mechanism (not in the source note, which names the reaction only)."})
    add({"t": "table", "sec": 1, "lo": LO3, "title": "Halogenated alkanes in pharmacy and everyday life",
         "head": ["Formula", "Name", "Use"],
         "rows": [["CH<sub>3</sub>CH<sub>2</sub>Cl", "chloroethane (ethyl chloride)", "spray-on <b>local anaesthetic</b>: evaporates fast and cools the skin"],
                  ["CF<sub>3</sub>CHBrCl", "halothane", "inhaled <b>general anaesthetic</b> (now largely replaced by safer agents)"],
                  ["CHCl<sub>3</sub>", "trichloromethane (chloroform)", "historic anaesthetic; now an industrial solvent (toxic to the liver)"],
                  ["CH<sub>2</sub>Cl<sub>2</sub>", "dichloromethane", "laboratory and industrial solvent"],
                  ["CCl<sub>2</sub>F<sub>2</sub>", "CFC-12", "old refrigerant and aerosol propellant; destroys ozone, now phased out"]],
         "widths": [2.0, 2.8, 5.0],
         "caption": "Many chlorinated hydrocarbons are toxic or suspected carcinogens; CCl<sub>4</sub> is no longer used in fire extinguishers (NAM-ALKANE 12.8).",
         "notes": "NAM-ALKANE 12.8 table and health notes; halothane added (original)."})
    add({"t": "check", "sec": 1, "lo": LO3, "title": "Quick check",
         "q": "In the chlorination of methane, which step uses UV light to split a Cl<sub>2</sub> molecule into two chlorine radicals?",
         "opts": ["Termination", "Initiation", "Propagation 1", "Combustion"], "ans": 1,
         "why": "Initiation: Cl–Cl → 2 Cl•. Propagation then keeps the chain going; termination pairs radicals up.", "notes": "Answer B."})
    add({"t": "check", "sec": 1, "lo": LO3, "title": "Quick check",
         "q": "Why is a gas heater in a closed room dangerous?",
         "opts": ["It produces too much water", "Incomplete combustion produces carbon monoxide", "Alkanes are toxic to touch", "It produces chlorine"], "ans": 1,
         "why": "With limited oxygen, CO forms. It binds haemoglobin far more strongly than oxygen does.", "notes": "Answer B."})

    # ================= 2.2 ALKENES, ALKYNES & AROMATICS =================
    add({"t": "divider", "num": 2, "title": "Alkenes, Alkynes & Aromatics", "lo": "CH2-LO4, LO5", "src": "Ball Ch 13 · FGOB 13",
         "blurb": "Unsaturated hydrocarbons: their names and shapes, cis-trans isomers, and the reactions that make them useful."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO4, "title": "Unsaturated hydrocarbons",
         "fig": {"cap": "The simplest alkene and alkyne, and benzene, the simplest aromatic compound.",
                 "data": row([(mol("C=C", 200, 110, hs=True), "ethene (ethylene) · 120°"), (mol("C#C", 200, 110, hs=True), "ethyne (acetylene) · 180°"), (mol("c1ccccc1", 200, 110), "benzene")], w=240, h=110)},
         "items": ["<b>Alkenes</b> have a C=C double bond: C<sub>n</sub>H<sub>2n</sub>. <b>Alkynes</b> have a C≡C triple bond: C<sub>n</sub>H<sub>2n−2</sub>. Both have fewer H than the alkane: they are <b>unsaturated</b>.",
                   "Ethene is the raw material for polyethylene, and ripening fruit gives it off. Ethyne burns in oxyacetylene welding torches.",
                   "Ethene is made by <b>cracking</b>: breaking long petroleum alkanes into smaller molecules."],
         "notes": "Ball 13.1, 13.6; FGOB 13.1."})
    add({"t": "table", "sec": 2, "lo": LO4, "title": "Naming alkenes and alkynes",
         "head": ["Rule", "Example"],
         "rows": [["The parent is the longest chain <b>containing the C=C</b>. Change -ane to <b>-ene</b> (alkene) or <b>-yne</b> (alkyne).", "CH<sub>2</sub>=CHCH<sub>3</sub> is propene"],
                  ["Number so the multiple bond gets the <b>lowest number</b> (the number of its first carbon). It beats substituents.", "CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub> is 2-pentene, not 3-pentene"],
                  ["Name and number substituents as for alkanes.", "(CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>CH=CHCH<sub>3</sub> is 5-methyl-2-hexene"],
                  ["Rings: add <b>cyclo-</b>.", "a hexagon with one C=C is cyclohexene"]],
         "widths": [5.2, 4.0], "caption": "Source: FGOB 13.2 (Ball 13.1). Newer IUPAC style writes the number before the ending (pent-2-ene); either is accepted in this course.",
         "notes": "FGOB 13.2 rules 1–3 and cycloalkenes."})
    add({"t": "example", "sec": 2, "lo": LO4, "title": "Example 2.4 · Name the alkene",
         "q": "Name CH<sub>3</sub>CH=CHCH(CH<sub>3</sub>)CH<sub>3</sub>.",
         "fig": {"cap": "", "data": mol("CC=CC(C)C", 300, 150)},
         "steps": ["Longest chain containing the C=C: <b>5 carbons</b> → pentene.",
                   "Number from the left so the double bond starts at C2: <b>2-pentene</b>.",
                   "A methyl group sits on C4.",
                   "Name: <b>4-methyl-2-pentene</b>."],
         "notes": "FGOB 13.2 Example (a)."})
    add({"t": "tryit", "sec": 2, "lo": LO4, "title": "Try it · Alkynes",
         "q": "Name (a) CH≡CCH<sub>2</sub>CH<sub>3</sub> and (b) CH<sub>3</sub>C≡CCH<sub>3</sub>. What is the shape around the triple-bond carbons?",
         "a": "(a) <b>1-butyne</b> (b) <b>2-butyne</b>. The triple-bond carbons are <b>linear</b> (180°); the CH<sub>3</sub> and CH<sub>2</sub> carbons are tetrahedral (109.5°).",
         "notes": "FGOB 13.2 alkyne naming and geometry."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO4, "title": "Cis-trans isomers",
         "fig": {"cap": "2-Butene exists as two isomers because the double bond cannot rotate.",
                 "data": row([(mol("C/C=C\\C", 220, 120), "cis-2-butene (same side)"), (mol("C/C=C/C", 220, 120), "trans-2-butene (opposite sides)")], w=280, h=120)},
         "items": ["Groups rotate freely about a C–C single bond, but <b>not about a C=C</b> double bond without breaking it.",
                   "Two requirements: <b>restricted rotation</b>, and <b>two different groups on each</b> double-bond carbon.",
                   "So C=CH<sub>2</sub> units and C=CR<sub>2</sub> units (two identical groups) cannot show cis-trans isomerism. Rings can: groups on the same or opposite faces."],
         "notes": "FGOB 13.3. Cis-trans isomers have different physical and biological properties."})
    add({"t": "example", "sec": 2, "lo": LO4, "title": "Example 2.5 · Cis-trans or not?",
         "q": "Which can exist as cis-trans isomers? (a) CHCl=CHBr (b) CH<sub>2</sub>=CBrCH<sub>3</sub> (c) (CH<sub>3</sub>)<sub>2</sub>C=CHCH<sub>2</sub>CH<sub>3</sub> (d) CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub>",
         "steps": ["(a) H and Cl on one carbon, H and Br on the other: two different groups on each → <b>yes</b>.",
                   "(b) One carbon carries two H atoms → <b>no</b>.",
                   "(c) One carbon carries two CH<sub>3</sub> groups → <b>no</b>.",
                   "(d) H and CH<sub>3</sub> on one carbon, H and C<sub>2</sub>H<sub>5</sub> on the other → <b>yes</b>."],
         "notes": "FGOB 13.3 Example."})
    add({"t": "bullets", "sec": 2, "lo": LO4, "title": "Why shape matters: trans fats",
         "items": ["Natural unsaturated fats have <b>cis</b> double bonds, which put a bend in the chain: the oil stays liquid.",
                   "Partly hydrogenating vegetable oil to make solid margarine can flip some bonds to <b>trans</b>. Trans chains are straighter and pack like saturated fats.",
                   "<b>Trans fats</b> raise LDL (\"bad\") cholesterol and heart-disease risk, so many countries now limit them in food.",
                   "The same atoms, arranged differently in space, behave differently in the body."],
         "notes": "Original pharmacy and nutrition link. Hydrogenation is covered below and in Chapter 6."})
    add({"t": "two", "sec": 2, "lo": LO4, "title": "A first look at chirality",
         "lead": "Another kind of isomerism arises from <b>handedness</b>. Chapter 5 (Carbohydrates) covers it in depth.",
         "cols": [{"h": "Chiral carbon", "tone": "cold", "items": [
             "A carbon bonded to <b>four different groups</b> is a <b>chiral carbon</b> (stereocentre)",
             "Its molecule has two <b>mirror-image forms</b> that cannot be superimposed, like your left and right hands",
             "The two forms are <b>enantiomers</b>",
             "Example: 2-butanol, CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub>: C2 carries H, OH, CH<sub>3</sub> and C<sub>2</sub>H<sub>5</sub>"]},
             {"h": "Why pharmacists care", "tone": "heat", "items": [
                 "Enzymes and receptors are chiral too, so two enantiomers can act differently in the body",
                 "<b>Thalidomide</b> (1950s–60s): one form eased morning sickness; the other was linked to severe birth defects",
                 "The body converts one form into the other, so even a pure form would not have been safe",
                 "Many modern drugs are sold as a single enantiomer, such as esomeprazole"]}],
         "notes": "Original brief introduction (FGOB 14.10 is an empty placeholder). Thalidomide enantiomers interconvert in vivo."})
    add({"t": "tryit", "sec": 2, "lo": LO4, "title": "Try it · Find the chiral carbon",
         "q": "Which compound has a chiral carbon? (a) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (b) CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>3</sub> (c) CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>",
         "a": "Only <b>(c)</b>, 3-methylhexane: C3 carries H, CH<sub>3</sub>, CH<sub>2</sub>CH<sub>3</sub> and CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>, four different groups. In (a) and (b) every carbon has at least two identical groups.",
         "notes": "Original."})
    add({"t": "table", "sec": 2, "lo": LO5, "title": "Four types of organic reaction",
         "head": ["Type", "What happens", "Example in this course"],
         "rows": [["<b>Addition</b>", "two reactants join to make one product; a multiple bond becomes a single bond", "alkene + Br<sub>2</sub> → dibromoalkane"],
                  ["<b>Substitution</b>", "one atom or group replaces another", "CH<sub>4</sub> + Cl<sub>2</sub> → CH<sub>3</sub>Cl + HCl; benzene + Br<sub>2</sub>"],
                  ["<b>Elimination</b>", "a small molecule (H<sub>2</sub>O, HX) is removed, forming a multiple bond", "alcohol → alkene + H<sub>2</sub>O (Chapter 3)"],
                  ["<b>Polymerisation</b>", "many small monomers join into one large polymer", "ethene → polyethylene"]],
         "widths": [1.8, 4.2, 3.6], "caption": "Addition and elimination are opposites: hydration adds water to an alkene; dehydration removes it.",
         "notes": "Original summary (FGOB 13.5 is an empty placeholder)."})
    add({"t": "table", "sec": 2, "lo": LO5, "title": "Addition reactions of alkenes",
         "head": ["Reaction", "Reagent and condition", "Product"],
         "rows": [["<b>Hydrogenation</b>", "H<sub>2</sub>, Ni or Pt catalyst", "alkane"],
                  ["<b>Halogenation</b>", "Br<sub>2</sub> or Cl<sub>2</sub>, room temperature", "dihaloalkane (a halogen on each carbon)"],
                  ["<b>Hydrohalogenation</b>", "HCl or HBr", "haloalkane"],
                  ["<b>Hydration</b>", "H<sub>2</sub>O, strong acid catalyst (H<sub>2</sub>SO<sub>4</sub>)", "alcohol"]],
         "widths": [2.4, 3.6, 3.6],
         "caption": "In each case one bond of the C=C breaks and a new atom or group adds to <b>each</b> carbon. Test for unsaturation: <b>bromine</b> (red-brown) is <b>decolourised</b> by an alkene; an alkane does not decolourise it in the dark.",
         "notes": "Ball 13.4 and FGOB 13.6 (hydrogenation, halogenation, hydration, bromine test). Hydrohalogenation added (original)."})
    add({"t": "figure", "pos": "leftwide", "sec": 2, "lo": LO5, "title": "Example 2.6 · Three additions to 2-butene",
         "fig": {"cap": "The reagent adds across the double bond in each case (FGOB 13.6 Example).",
                 "data": stack([scheme([('m', 'CC=CC', '2-butene', 150), ('+',), ('t', 'H₂', 50), ('>', 'Ni', ''), ('m', 'CCCC', 'butane', 150)], h=110),
                                scheme([('m', 'CC=CC', '2-butene', 150), ('+',), ('t', 'Br₂', 50), ('>', '', ''), ('m', 'CC(Br)C(Br)C', '2,3-dibromobutane', 190)], h=110),
                                scheme([('m', 'CC=CC', '2-butene', 150), ('+',), ('t', 'H₂O', 50), ('>', 'H₂SO₄', ''), ('m', 'CC(O)CC', '2-butanol', 150)], h=110)], w=520, row_h=150)},
         "items": ["Hydrogenation gives the alkane with the same carbon skeleton.",
                   "Bromine adds one Br to each carbon; the red-brown colour disappears.",
                   "Hydration gives an alcohol (Chapter 3). For 2-butene both carbons are alike, so only one product forms."],
         "notes": "FGOB 13.6 Example (a)–(c)."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO5, "title": "Markovnikov's rule",
         "fig": {"cap": "Propene + HBr: two products are possible, but one is major.",
                 "data": scheme([('m', 'C=CC', 'propene', 130), ('+',), ('t', 'HBr', 60), ('>', '', ''), ('m', 'CC(Br)C', '2-bromopropane (major)', 190), ('t', 'not', 50), ('m', 'BrCCC', '1-bromopropane', 160)], h=120)},
         "items": ["When HX or H<sub>2</sub>O adds to an <b>unsymmetrical</b> alkene, the <b>H</b> goes to the double-bond carbon that <b>already has more H atoms</b>.",
                   "The X (or OH) goes to the other carbon. Memory aid: \"the rich get richer\". Why: H<sup>+</sup> adds first so that the more stable <b>carbocation</b> (C<sup>+</sup> on the more substituted carbon) forms. You will meet carbocations again in Chapter 3.",
                   "Propene + H<sub>2</sub>O (acid) gives mainly <b>2-propanol</b> (isopropyl alcohol, the rubbing alcohol in hand rubs and swabs)."],
         "notes": "Original (Markovnikov's rule is not in Ball 13). Reason: the more stable carbocation forms; mention only if students ask."})
    add({"t": "tryit", "sec": 2, "lo": LO5, "title": "Try it · Predict the product",
         "q": "Give the major product: (a) CH<sub>3</sub>CH<sub>2</sub>CH=CH<sub>2</sub> + HCl (b) CH<sub>3</sub>CH=CH<sub>2</sub> + Cl<sub>2</sub> (c) CH<sub>3</sub>CH<sub>2</sub>CH=CH<sub>2</sub> + H<sub>2</sub> (Ni)",
         "a": "(a) <b>2-chlorobutane</b>, CH<sub>3</sub>CH<sub>2</sub>CHClCH<sub>3</sub> (Markovnikov). (b) <b>1,2-dichloropropane</b>, CH<sub>3</sub>CHClCH<sub>2</sub>Cl. (c) <b>butane</b>.",
         "notes": "(b) and (c) from Ball 13.4 Exercise 1; (a) original."})
    add({"t": "bullets", "sec": 2, "lo": LO5, "title": "Alkynes add twice",
         "items": ["A triple bond has two bonds that can break, so alkynes take up <b>two</b> molecules of reagent.",
                   "HC≡CH + 2 H<sub>2</sub> (Ni) → CH<sub>3</sub>CH<sub>3</sub> (ethane). With a specially weakened catalyst, the reaction stops at the alkene.",
                   "HC≡CH + 2 Br<sub>2</sub> → CHBr<sub>2</sub>CHBr<sub>2</sub> (1,1,2,2-tetrabromoethane): alkynes also decolourise bromine.",
                   "Physical properties of alkenes and alkynes are like those of alkanes: nonpolar, insoluble in water, boiling points rising with size."],
         "notes": "Original summary; Ball 13.6 states alkynes undergo the typical addition reactions of alkenes."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO5, "title": "Addition polymers",
         "fig": {"cap": "Ethene molecules join end to end: n CH<sub>2</sub>=CH<sub>2</sub> → –[CH<sub>2</sub>–CH<sub>2</sub>]<sub>n</sub>–",
                 "data": scheme([('t', 'n', 30), ('m', 'C=C', 'ethene (monomer)', 150, True), ('>', 'catalyst', ''), ('m', '*CCCCCC*', 'polyethylene (polymer)', 300)], h=110)},
         "items": ["In <b>addition polymerisation</b>, every atom of each monomer ends up in the polymer.",
                   "Pharmacy uses: <b>polypropylene</b> (syringes, containers), <b>PVC</b> (IV fluid bags and tubing), <b>polyethylene</b> (bottles, bags), <b>PTFE</b> (non-stick coatings).",
                   "To draw a polymer: turn each C=C into C–C and join the monomer units in a chain."],
         "notes": "Ball 13.5; FGOB 13.7 table of addition polymers (PVC bags for IV solutions)."})
    add({"t": "example", "sec": 2, "lo": LO5, "title": "Example 2.7 · Draw a polymer",
         "q": "Draw three repeating units of the polymer made from propene, CH<sub>2</sub>=CHCH<sub>3</sub>.",
         "fig": {"cap": "", "data": mol("*CC(C)CC(C)CC(C)*", 380, 150)},
         "steps": ["Open each double bond: CH<sub>2</sub>=CH(CH<sub>3</sub>) → –CH<sub>2</sub>–CH(CH<sub>3</sub>)–.",
                   "Join three units head to tail: –CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH(CH<sub>3</sub>)–.",
                   "The CH<sub>3</sub> groups hang off every second carbon. This is <b>polypropylene</b>."],
         "notes": "Original example based on FGOB 13.7."})
    add({"t": "bullets", "sec": 2, "lo": LO4, "title": "Benzene: unsaturated but unusually stable",
         "items": ["Benzene, C<sub>6</sub>H<sub>6</sub>, is a flat hexagon of six carbons, each with one H.",
                   "It can be drawn with alternating double bonds, but all six C–C bonds are <b>identical</b>: the electrons are <b>delocalised</b> around the ring, often drawn as a circle.",
                   "Despite its formula, benzene does <b>not</b> decolourise bromine and does <b>not</b> undergo addition readily. It reacts by <b>substitution</b>, which keeps the stable ring.",
                   "Benzene is <b>toxic</b>: long exposure damages the bone marrow and is linked to leukaemia. Compounds with a benzene ring are called <b>aromatic</b>."],
         "side": {"h": "Pharmacy link", "body": "Aspirin, paracetamol, ibuprofen and benzocaine all contain an aromatic ring (Chapter 1)."},
         "notes": "Ball 13.7; FGOB 13.8."})
    add({"t": "table", "sec": 2, "lo": LO4, "title": "Naming aromatic compounds",
         "head": ["Compound", "Formula", "Structure", "Use"],
         "rows": [["toluene (methylbenzene)", "C<sub>6</sub>H<sub>5</sub>–CH<sub>3</sub>", mini("Cc1ccccc1"), "solvent"],
                  ["phenol", "C<sub>6</sub>H<sub>5</sub>–OH", mini("Oc1ccccc1"), "disinfectant; drug synthesis"],
                  ["aniline", "C<sub>6</sub>H<sub>5</sub>–NH<sub>2</sub>", mini("Nc1ccccc1"), "dyes and drugs"],
                  ["benzoic acid", "C<sub>6</sub>H<sub>5</sub>–COOH", mini("OC(=O)c1ccccc1"), "food preservative"],
                  ["chlorobenzene", "C<sub>6</sub>H<sub>5</sub>–Cl", mini("Clc1ccccc1"), "synthesis starting material"]],
         "widths": [2.6, 2.2, 1.8, 2.8],
         "caption": "Name substituents in front of <b>benzene</b> (chlorobenzene, ethylbenzene, nitrobenzene). The C<sub>6</sub>H<sub>5</sub>– group is called <b>phenyl</b>. Source: FGOB 13.9.",
         "notes": "FGOB 13.9 table of representative aromatic compounds."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO4, "title": "Two substituents: ortho, meta, para",
         "fig": {"cap": "The three dichlorobenzenes (FGOB 13.9).",
                 "data": row([(mol("Clc1ccccc1Cl", 200, 120), "1,2- · ortho (o-)"), (mol("Clc1cccc(Cl)c1", 200, 120), "1,3- · meta (m-)"), (mol("Clc1ccc(Cl)cc1", 200, 120), "1,4- · para (p-)")], w=240, h=120)},
         "items": ["Number from one substituent towards the other by the shortest path; list substituents alphabetically.",
                   "If the ring is named as toluene, phenol, aniline or benzoic acid, that group's carbon is C1: Br para to CH<sub>3</sub> is <b>p-bromotoluene</b> (4-bromotoluene).",
                   "Pharmacy link: paracetamol is a <b>para</b>-disubstituted benzene: the –OH and the –NHCOCH<sub>3</sub> are 1,4."],
         "notes": "FGOB 13.9 disubstituted benzenes and examples."})
    add({"t": "table", "sec": 2, "lo": LO5, "title": "Reactions of benzene: substitution",
         "head": ["Reaction", "Reagents", "Product (+ by-product)"],
         "rows": [["<b>Halogenation</b>", "Br<sub>2</sub> with FeBr<sub>3</sub> catalyst (or Cl<sub>2</sub>/FeCl<sub>3</sub>)", "bromobenzene + HBr"],
                  ["<b>Nitration</b>", "conc. HNO<sub>3</sub> with conc. H<sub>2</sub>SO<sub>4</sub>", "nitrobenzene + H<sub>2</sub>O"],
                  ["<b>Sulfonation</b>", "SO<sub>3</sub> in conc. H<sub>2</sub>SO<sub>4</sub> (fuming sulfuric acid)", "benzenesulfonic acid"],
                  ["<b>Alkylation</b>", "CH<sub>3</sub>Cl with AlCl<sub>3</sub> catalyst", "toluene + HCl"]],
         "widths": [2.2, 4.2, 3.4],
         "caption": "An H on the ring is <b>replaced</b>, so the stable aromatic ring survives. Unlike alkenes, benzene needs a catalyst to react with bromine. Pharmacy route: nitrobenzene → aniline → many drugs; sulfonation leads to the sulfonamide (sulfa) antibiotics.",
         "notes": "Original summary (FGOB 13.10 is an empty placeholder). Mechanism (electrophilic aromatic substitution) not required at diploma level."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO5, "title": "Example 2.8 · Nitration of benzene",
         "fig": {"cap": "Substitution: –NO<sub>2</sub> replaces one H.",
                 "data": scheme([('m', 'c1ccccc1', 'benzene', 140), ('+',), ('t', 'HNO₃', 70), ('>', 'conc. H₂SO₄', ''), ('m', '[O-][N+](=O)c1ccccc1', 'nitrobenzene', 170), ('+',), ('t', 'H₂O', 60)], h=130)},
         "items": ["Compare: an alkene + Br<sub>2</sub> <b>adds</b> (no by-product); benzene + Br<sub>2</sub>/FeBr<sub>3</sub> <b>substitutes</b> (HBr by-product).",
                   "The by-product (HBr, H<sub>2</sub>O, HCl) is the H that left the ring plus part of the reagent."],
         "notes": "Original example."})
    add({"t": "bullets", "sec": 2, "lo": LO4, "title": "Fused rings: polycyclic aromatics",
         "items": ["Some aromatic compounds have <b>fused rings</b> that share a side: naphthalene (two rings, mothballs), anthracene and phenanthrene (three rings).",
                   "Polycyclic aromatic hydrocarbons (PAHs) form when coal, tobacco or food are heated strongly. Several are <b>carcinogens</b>, for example in cigarette smoke and charred food.",
                   "Steroids (Chapter 6) have a related four-ring skeleton, though it is not aromatic."],
         "notes": "FGOB 13.9, Polycyclic Aromatic Hydrocarbons."})
    add({"t": "check", "sec": 2, "lo": LO5, "title": "Quick check",
         "q": "Propene reacts with water and an acid catalyst. The main product is:",
         "opts": ["1-propanol", "2-propanol", "propane", "1,2-propanediol"], "ans": 1,
         "why": "Markovnikov: H adds to CH<sub>2</sub> (more H already), OH adds to the middle carbon → 2-propanol.", "notes": "Answer B."})
    add({"t": "check", "sec": 2, "lo": LO5, "title": "Quick check",
         "q": "How can you tell cyclohexene from benzene in the lab?",
         "opts": ["Benzene decolourises bromine; cyclohexene does not", "Cyclohexene decolourises bromine; benzene does not (without a catalyst)", "Both decolourise bromine", "Neither reacts with anything"], "ans": 1,
         "why": "Cyclohexene adds Br<sub>2</sub> across its C=C. Benzene's delocalised ring resists addition.", "notes": "Answer B."})
    add({"t": "check", "sec": 2, "lo": LO4, "title": "Quick check",
         "q": "Which alkene can exist as cis and trans isomers?",
         "opts": ["CH<sub>2</sub>=CHCH<sub>2</sub>CH<sub>3</sub>", "(CH<sub>3</sub>)<sub>2</sub>C=CH<sub>2</sub>", "CH<sub>3</sub>CH<sub>2</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub>", "CH<sub>2</sub>=CH<sub>2</sub>"], "ans": 2,
         "why": "3-Hexene has H and C<sub>2</sub>H<sub>5</sub> on each double-bond carbon. The others have two identical groups on one carbon.", "notes": "Answer C (FGOB 13.3 exercise c)."})

    # ================= wrap-up =================
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Alkanes", "C<sub>n</sub>H<sub>2n+2</sub>; saturated; homologous series; isomers from C<sub>4</sub>"],
        ["IUPAC", "longest chain → lowest numbers → substituents alphabetical (ignore di-, tri-)"],
        ["Cycloalkanes", "C<sub>n</sub>H<sub>2n</sub>; cyclo-; ring strain in small rings"],
        ["Properties", "nonpolar, insoluble, float; bp rises with size, falls with branching"],
        ["Alkane reactions", "combustion (CO if O<sub>2</sub> is limited); halogenation by free radicals with UV light"],
        ["Alkenes/alkynes", "-ene/-yne; lowest number to the multiple bond; cis-trans needs two different groups on each C"],
        ["Addition", "H<sub>2</sub>, X<sub>2</sub>, HX, H<sub>2</sub>O; Markovnikov; Br<sub>2</sub> test; addition polymers"],
        ["Benzene", "delocalised and stable; substitution (halogenation, nitration, sulfonation); o-, m-, p-"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 25 min)", "Attempt the Chapter 2 tutorial",
                   "Play the Chapter 2 game to find your weak outcomes", "Next chapter: Organic Compounds that Contain Oxygen and Sulphur"],
         "attrib": "Adapted from LibreTexts (Sharpe Elles; Ball, Hill &amp; Scott; FGOB), CC BY-NC-SA 3.0. Reaction types, mechanisms, Markovnikov's rule, benzene substitution, chirality and pharmacy links are original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"]})
    return S
