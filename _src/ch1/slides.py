"""PHD125 Chapter 1 · Introduction to Organic Molecule · lecture slide content.
Sources: NAM-INTRO (LibreTexts 12.1-12.2, Sharpe Elles remix of Ball/McMurry, CC BY-NC-SA 3.0),
NAM-ALKANE 12.4-12.5, Ball 12.1 and 12.4, FGOB 16.7, Soderberg Ch 1 (CC BY-NC-SA 4.0).
Subchapter 1.5 and the history in 1.1 are Dr. NAM's own material (written for this hub)."""
from figs import mol, grid, row


def mini(smi):
    hs = smi in ('C=C', 'C#C')
    return f'<img src="{mol(smi, 190, 84, hs=hs)}" alt="" style="height:54px;display:block;background:#fff;border-radius:6px;padding:1px 4px">'


HL_KEY = ('Shading: <span style="background:#8CB8FF;color:#0A1628;padding:0 4px;border-radius:4px">aromatic ring</span> '
          '<span style="background:#FF997A;color:#0A1628;padding:0 4px;border-radius:4px">carboxylic acid</span> '
          '<span style="background:#FFCC40;color:#0A1628;padding:0 4px;border-radius:4px">ester</span> '
          '<span style="background:#8CD98C;color:#0A1628;padding:0 4px;border-radius:4px">amide</span> '
          '<span style="background:#BF99FF;color:#0A1628;padding:0 4px;border-radius:4px">–OH</span> '
          '<span style="background:#66D9EB;color:#0A1628;padding:0 4px;border-radius:4px">amine</span>')
RING = ('c1ccccc1', 'ring')
ACID = ('[CX3](=O)[OX2H1]', 'acid')
ESTER = ('[CX3](=O)[OX2][#6]', 'ester')
AMIDE = ('[NX3][CX3](=O)', 'amide')
OH = ('c[OX2H1]', 'oh')
AMINE = ('c[NX3H2]', 'amine')

ASPIRIN = 'CC(=O)Oc1ccccc1C(=O)O'
SALICYLIC = 'OC(=O)c1ccccc1O'
PARACETAMOL = 'CC(=O)Nc1ccc(O)cc1'
IBUPROFEN = 'CC(C)Cc1ccc(cc1)C(C)C(=O)O'
BENZOCAINE = 'CCOC(=O)c1ccc(N)cc1'

LO = {
    1: 'CH1-LO1', 2: 'CH1-LO1', 3: 'CH1-LO2', 4: 'CH1-LO3', 5: 'CH1-LO4, LO5',
}

META = {
    "code": "CH1", "chapter": "Chapter 1", "title": "Introduction to Organic Molecule", "short": "Introduction to Organic Molecule",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: Dr. NAM's NAM-INTRO and NAM-ALKANE notes (LibreTexts 12.1–12.5), with Ball 12.1 and 12.4",
    "attrib": ("Adapted from LibreTexts <i>Introduction to Organic Chemistry – Alkanes</i> 12.1–12.5 (Lisa Sharpe Elles, remixed from Ball, Hill &amp; Scott), "
               "<i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) 12.1 and 12.4, and <i>Fundamentals of General Organic and Biological Chemistry</i> 16.7, "
               "all CC BY-NC-SA 3.0; and Soderberg, <i>Organic Chemistry with a Biological Emphasis</i>, CC BY-NC-SA 4.0. Subchapter 1.5 is original material by Dr. NAM. "
               "Structures drawn with RDKit. Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["urea", "methane"], "2": ["ethane", "ethene", "ethyne"], "3": ["butane", "propanol", "cyclohexane"],
               "4": ["ethanol", "acetone", "aceticacid"], "5": ["aspirin", "paracetamol", "ascorbic"]},
    "titlemol": ["aspirin", "methane", "ethanol", "paracetamol"], "darkmol": "aspirin",
    "next": "Next chapter: Saturated and Unsaturated Hydrocarbons",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    ["CH1-LO1", "Explain why carbon forms so many compounds, and how organic and inorganic compounds differ"],
    ["CH1-LO2", "Draw and convert between molecular, expanded, condensed and line-angle (skeletal) formulas"],
    ["CH1-LO3", "Identify the main functional groups in a structure, including common drugs such as aspirin and paracetamol"],
    ["CH1-LO4", "Explain why a natural and a synthetic sample of the same compound behave identically"],
    ["CH1-LO5", "Give examples of how organic compounds and their functional groups matter in medicines and consumer products"],
]


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Introduction to Organic Molecule", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 1",
         "notes": "Chapter 1 of the course outline. Five subchapters: what organic chemistry is, the features of organic compounds, drawing molecules, functional groups, and organic chemistry in pharmacy and everyday life."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "The same five outcomes appear in the before-class and after-class activities, the tutorial and the game."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>1.1 What is organic chemistry</b> (NAM-INTRO 12.1): from vitalism to the chemistry of carbon, and why carbon is special",
        "<b>1.2 Features of organic compounds</b> (NAM-INTRO 12.1): four bonds, chains and rings, organic vs inorganic, polarity",
        "<b>1.3 Drawing organic molecules</b> (NAM-ALKANE 12.4–12.5): molecular, expanded, condensed and line structures, and 3D shapes",
        "<b>1.4 Functional groups</b> (NAM-INTRO 12.2): the families of organic compounds, and spotting them in drugs",
        "<b>1.5 Pharmacy and everyday life</b> (new): natural vs synthetic, drugs from nature, drug names, stability, consumer products"],
         "notes": "Use the menu to jump to any subchapter. Each subchapter ends with a quick check."})
    add({"t": "hook", "title": "Think first",
         "q": "Paracetamol, the sugar in your teh tarik, the plastic of your phone case and the DNA in your cells. What do they have in common?",
         "a": "All four are built on <b>carbon skeletons</b>: they are <b>organic compounds</b>. Most of the millions of known compounds contain carbon, and almost every medicine you will dispense is organic. This chapter shows why carbon is so special.",
         "notes": "Pairs discuss for one minute. Accept any answer about carbon, molecules or covalent bonds."})

    # ---------------- 1.1 ----------------
    add({"t": "divider", "num": 1, "title": "What is organic chemistry", "lo": LO[1], "src": "NAM-INTRO 12.1 · Ball 12.1",
         "blurb": "How a theory about a 'vital force' fell, and why one element gets a whole branch of chemistry."})
    add({"t": "two", "sec": 1, "lo": LO[1], "title": "From 'living things' to 'carbon'",
         "lead": "The meaning of <b>organic</b> changed in the early 1800s.",
         "cols": [{"h": "Before 1828: vitalism", "tone": "heat", "items": [
             "<b>Organic</b> meant compounds made by living organisms (sugar, urea, oils)",
             "<b>Vitalism</b>: chemists believed these needed a <b>vital force</b> found only in living things",
             "So organic compounds could never be made in a laboratory from minerals"]},
             {"h": "After 1828: chemistry of carbon", "tone": "cold", "items": [
                 "Friedrich <b>Wöhler</b> heated <b>ammonium cyanate</b>, a mineral salt, and obtained <b>urea</b>, a compound found in urine",
                 "No living thing was involved: vitalism began to collapse",
                 "Today, <b>organic chemistry</b> is the study of <b>carbon-containing compounds</b>, whatever their source"]}],
         "notes": "History written for this hub. Wöhler's 1828 synthesis is the classic turning point; vitalism faded over the following decades as more organic compounds were made from inorganic starting materials."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO[1], "title": "Wöhler's urea synthesis (1828)",
         "fig": {"cap": "Ammonium cyanate (inorganic salt) → urea (organic compound). Same atoms, rearranged by heating.",
                 "data": row([(mol("[NH4+].[O-]C#N", 300, 150), "ammonium cyanate"), (mol("NC(N)=O", 300, 150), "urea")], w=300, h=150)},
         "items": ["Both compounds have the formula CH<sub>4</sub>N<sub>2</sub>O: only the <b>arrangement</b> of atoms changes.",
                   "Pharmacy link: urea is still used today in creams for very dry skin (it helps skin hold water)."],
         "notes": "Urea creams (10–40%) are common emollients and keratolytics; a nice bridge to pharmacy."})
    add({"t": "bullets", "sec": 1, "lo": LO[1], "title": "Why carbon is special",
         "items": ["Carbon atoms bond <b>strongly to other carbon atoms</b>, forming long chains, branches and rings.",
                   "Carbon atoms bond <b>strongly to atoms of other elements</b>: H, O, N, S and the halogens.",
                   "Carbon makes a <b>large number of covalent bonds: four</b>. It can share electrons in single, double or triple bonds.",
                   "Together, these give carbon a chemical diversity <b>unrivalled</b> by any other element: millions of different compounds."],
         "side": {"h": "Did you know?", "body": "Elemental carbon is not even among the most common elements in the Earth's crust. Yet every living thing is made of organic compounds."},
         "notes": "NAM-INTRO 12.1, first paragraph."})
    add({"t": "bullets", "sec": 1, "lo": LO[1], "title": "Carbon, but not organic",
         "items": ["By convention, a few carbon compounds are treated as <b>inorganic</b>:",
                   "<b>Carbon dioxide</b> (CO<sub>2</sub>) and <b>carbon monoxide</b> (CO)",
                   "<b>Carbonates</b> such as calcium carbonate (CaCO<sub>3</sub>) and <b>bicarbonates</b> such as sodium bicarbonate (NaHCO<sub>3</sub>)",
                   "<b>Cyanides</b> such as potassium cyanide (KCN)",
                   "Pharmacy link: the antacids <b>calcium carbonate</b> and <b>sodium bicarbonate</b> contain carbon but are <b>inorganic</b> (ionic) compounds."],
         "notes": "NAM-INTRO 12.1 names carbonate and bicarbonate ions, CO2 and CO. Cyanides added as the other usual exception."})
    add({"t": "tryit", "sec": 1, "lo": LO[1], "title": "Try it · Classify",
         "q": "Classify each as organic or inorganic: (a) CH<sub>3</sub>CH<sub>2</sub>OH (ethanol) (b) NaHCO<sub>3</sub> (c) CH<sub>4</sub> (methane) (d) CO<sub>2</sub>",
         "a": "(a) <b>organic</b> (b) <b>inorganic</b>: a bicarbonate (c) <b>organic</b> (d) <b>inorganic</b>: carbon dioxide is one of the exceptions",
         "notes": "Style of Ball 12.E, exercises 1 and 3."})
    add({"t": "check", "sec": 1, "lo": LO[1], "title": "Quick check",
         "q": "Why was Wöhler's synthesis of urea so important?",
         "opts": ["It was the first compound ever made in a laboratory", "It made an organic compound from an inorganic one, with no living thing involved",
                  "It proved that urea is an inorganic compound", "It showed that carbon forms five bonds"],
         "ans": 1, "why": "Vitalism said organic compounds needed a vital force from living things. Wöhler made urea from a mineral salt.",
         "notes": "Answer B."})

    # ---------------- 1.2 ----------------
    add({"t": "divider", "num": 2, "title": "Characteristic features of organic compounds", "lo": LO[2], "src": "NAM-INTRO 12.1",
         "blurb": "Four bonds per carbon, chains and rings, and the properties that set organic compounds apart."})
    add({"t": "bullets", "sec": 2, "lo": LO[2], "title": "Carbon is tetravalent",
         "items": ["A carbon atom has <b>four valence electrons</b>. It is <b>tetravalent</b>: it forms <b>four covalent bonds</b> to complete its octet.",
                   "The simplest organic compounds contain only carbon and hydrogen: the <b>hydrocarbons</b>.",
                   "<b>Methane</b>, CH<sub>4</sub>, is the simplest hydrocarbon: one carbon bonded to four hydrogen atoms.",
                   "From VSEPR (PHD115), methane is <b>tetrahedral</b>: four electron groups, no lone pairs, H–C–H angles of <b>109.5°</b>."],
         "side": {"h": "Rule to remember", "body": "In every neutral organic molecule, <b>each carbon makes four bonds</b>. Use this to check every structure you draw."},
         "notes": "NAM-INTRO 12.1, Structural Properties of Carbon Compounds."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO[2], "title": "Single, double and triple bonds",
         "fig": {"cap": "Two carbons joined by a single bond (ethane), a double bond (ethene) or a triple bond (ethyne).",
                 "data": row([(mol("CC", 250, 160, hs=True), "ethane"), (mol("C=C", 250, 160, hs=True), "ethene"), (mol("C#C", 250, 160, hs=True), "ethyne")], w=250, h=160)},
         "items": ["Each carbon still makes <b>four bonds in total</b>. As C–C bonds increase, the number of H atoms <b>decreases</b>.",
                   "Shapes around carbon: four single bonds → <b>tetrahedral</b>; one double bond → <b>trigonal planar</b>; one triple bond → <b>linear</b>."],
         "notes": "NAM-INTRO Figure 12.1.2. The naming endings -ane, -ene, -yne come in Chapter 2."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO[2], "title": "Chains, branches and rings",
         "fig": {"cap": "Four carbon skeletons drawn as line structures (1.3 explains how to read them).",
                 "data": row([(mol("CCCC", 200, 130), "butane"), (mol("CC(C)C", 200, 130), "2-methylpropane"), (mol("C1CCCCC1", 200, 130), "cyclohexane"), (mol("c1ccccc1", 200, 130), "benzene")], w=200, h=130)},
         "items": ["Carbon–carbon bonds are strong, so carbon atoms link into <b>straight chains</b>, <b>branched chains</b> and <b>rings</b>.",
                   "Butane and 2-methylpropane share the formula <b>C<sub>4</sub>H<sub>10</sub></b> but differ in arrangement: they are <b>isomers</b> (Chapter 2).",
                   "This is a major reason there are so many organic compounds."],
         "notes": "Isomers are covered fully in Chapter 2 (NAM-ALKANE 12.3)."})
    add({"t": "table", "sec": 2, "lo": LO[2], "title": "Organic vs inorganic compounds",
         "head": ["Organic (typical)", "Example: hexane", "Inorganic (typical)", "Example: NaCl"],
         "rows": [["low melting point", "−95 °C", "high melting point", "801 °C"],
                  ["low boiling point", "69 °C", "high boiling point", "1413 °C"],
                  ["insoluble in water, soluble in nonpolar solvents", "insoluble in water; soluble in petrol", "soluble in water, insoluble in nonpolar solvents", "soluble in water; insoluble in petrol"],
                  ["flammable", "highly flammable", "nonflammable", "nonflammable"],
                  ["solutions do not conduct electricity", "nonconductive", "aqueous solutions conduct", "conducts in solution"],
                  ["covalent bonding", "covalent bonds", "ionic bonding", "ionic bonds"]],
         "widths": [2.6, 2.2, 2.6, 2.2],
         "caption": "Source: NAM-INTRO Table 12.1.1. Every category has exceptions: sugar and ethanol are organic yet dissolve in water.",
         "notes": "NAM-INTRO Table 12.1.1."})
    add({"t": "bullets", "sec": 2, "lo": LO[2], "title": "Polar or nonpolar?",
         "items": ["Carbon and hydrogen have similar electronegativity, so <b>C–H bonds are nonpolar</b>. Hydrocarbons are nonpolar: they do not mix with water.",
                   "When carbon bonds to <b>oxygen, nitrogen or a halogen</b>, the bond is <b>polar</b>. These atoms change how the molecule dissolves and reacts.",
                   "Pharmacy link: polarity decides whether a drug dissolves in water (an injection, a syrup) or in fats (an ointment, a cell membrane)."],
         "side": {"h": "Link back to PHD115", "body": "Review electronegativity and bond polarity from Ionic &amp; Covalent Compounds II. They explain most of the properties in this course."},
         "notes": "NAM-INTRO 12.1, paragraph after Figure 12.1.2."})
    add({"t": "example", "sec": 2, "lo": LO[2], "title": "Example 1.1 · Organic or inorganic?",
         "q": "A white solid melts at 186 °C, dissolves in water, burns when heated strongly in air, and its solution does not conduct electricity. Is it more likely organic or inorganic?",
         "steps": ["Melting point 186 °C is <b>low</b> compared with ionic salts (often above 600 °C).",
                   "It <b>burns</b>: flammability is typical of organic compounds.",
                   "Its solution <b>does not conduct</b>: no ions, so covalent bonding.",
                   "Dissolving in water is less typical, but sugars and other polar organic compounds do. Conclusion: <b>organic</b>. (It is sucrose, table sugar.)"],
         "notes": "Sucrose decomposes around 186 °C. Style of Ball 12.E exercise 2."})
    add({"t": "check", "sec": 2, "lo": LO[2], "title": "Quick check",
         "q": "Which property is typical of organic compounds?",
         "opts": ["High melting point", "Aqueous solutions conduct electricity", "Flammable", "Ionic bonding"],
         "ans": 2, "why": "Organic compounds are usually flammable, low-melting and covalent. The other three describe ionic compounds.",
         "notes": "Answer C."})

    # ---------------- 1.3 ----------------
    add({"t": "divider", "num": 3, "title": "Drawing organic molecules and their shapes", "lo": LO[3], "src": "NAM-ALKANE 12.4–12.5 · Ball 12.4",
         "blurb": "Four ways to write the same molecule, and why carbon chains zig-zag."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO[3], "title": "Four ways to write butane",
         "fig": {"cap": "Butane two ways: expanded structural formula (left) and line-angle structure (right).",
                 "data": row([(mol("CCCC", 330, 170, hs=True), "expanded"), (mol("CCCC", 330, 170), "line-angle")], w=330, h=170)},
         "items": ["<b>Molecular formula</b> C<sub>4</sub>H<sub>10</sub>: which atoms and how many, but not how they are joined.",
                   "<b>Expanded structural formula</b>: every atom and every bond drawn.",
                   "<b>Condensed structural formula</b> CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>: each carbon written with its hydrogens; bonds are implied.",
                   "<b>Line-angle (skeletal) structure</b>: a zig-zag line. Each end and each bend is a carbon. H atoms on carbon are not shown."],
         "notes": "NAM-ALKANE 12.4, expanded, condensed and line structures."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO[3], "title": "Expanded structures show every atom",
         "fig": {"cap": "Propane and butane, with every hydrogen drawn.",
                 "data": row([(mol("CCC", 300, 170, hs=True), "propane, CH₃CH₂CH₃"), (mol("CCCC", 300, 170, hs=True), "butane, CH₃CH₂CH₂CH₃")], w=300, h=170)},
         "items": ["Expanded structures are clear but slow to draw, and big molecules quickly become crowded.",
                   "Chemists use condensed and line structures for everyday work. You must be able to switch between all four."],
         "notes": "NAM-ALKANE 12.4."})
    add({"t": "table", "sec": 3, "lo": LO[3], "title": "Rules for reading line structures",
         "head": ["Rule", "What it means"],
         "rows": [["Ends and bends", "every end of a line and every corner is a <b>carbon atom</b>"],
                  ["Hidden hydrogens", "each carbon has enough H to make <b>four bonds</b>; these H are not drawn"],
                  ["Other atoms are drawn", "O, N, S and halogens are written as symbols, <b>with</b> their H (–OH, –NH<sub>2</sub>)"],
                  ["Multiple bonds", "a double bond is two lines; a triple bond is three lines drawn in a straight line"],
                  ["Rings", "a polygon: a hexagon is six carbons (cyclohexane)"]],
         "widths": [2.2, 5.0],
         "note": "Count H on any carbon: <b>4 − (number of lines to that carbon)</b>.",
         "notes": "NAM-ALKANE 12.4, rules for line structures."})
    add({"t": "example", "sec": 3, "lo": LO[3], "title": "Example 1.2 · Count the atoms",
         "q": "How many carbon and hydrogen atoms are in this line structure? Write its molecular formula and condensed formula.",
         "fig": {"cap": "", "data": mol("CCC(C)C", 360, 200)},
         "steps": ["Count ends and bends: <b>5 carbons</b>.",
                   "Fill each carbon to four bonds: the three end carbons have 3 H each (9), the CH<sub>2</sub> has 2, and the branch carbon has 1.",
                   "Total H = 9 + 2 + 1 = <b>12</b>. Molecular formula <b>C<sub>5</sub>H<sub>12</sub></b>.",
                   "Condensed formula: <b>CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub></b> (2-methylbutane)."],
         "notes": "NAM-ALKANE 12.4 practice."})
    add({"t": "example", "sec": 3, "lo": LO[3], "title": "Example 1.3 · Condensed to line structure",
         "q": "Draw the line structure of 1-propanol, CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH.",
         "fig": {"cap": "", "data": mol("CCCO", 340, 170)},
         "steps": ["Three carbons in a chain: draw a zig-zag with <b>two lines</b> (three points).",
                   "The OH is on the last carbon: draw a third line ending in <b>OH</b>. Oxygen and its H are always shown.",
                   "Check: each carbon has four bonds (the H are hidden). Molecular formula <b>C<sub>3</sub>H<sub>8</sub>O</b>."],
         "notes": "Ball 12.4 style."})
    add({"t": "tryit", "sec": 3, "lo": LO[3], "title": "Try it · Rings",
         "q": "A hexagon is drawn on its own, with no other atoms. Name it and write its molecular formula.",
         "afig": {"data": mol("C1CCCCC1", 260, 150)},
         "a": "Six carbons, each with two lines, so each carries <b>2 H</b>: <b>cyclohexane, C<sub>6</sub>H<sub>12</sub></b>.",
         "notes": "NAM-ALKANE 12.10 previews cycloalkanes, covered in Chapter 2."})
    add({"t": "table", "sec": 3, "lo": LO[3], "title": "The shapes of organic molecules",
         "head": ["Bonds around carbon", "Electron groups", "Shape", "Bond angle", "Example"],
         "rows": [["four single bonds", "4", "tetrahedral", "109.5°", "methane, CH<sub>4</sub>"],
                  ["one double + two single", "3", "trigonal planar", "120°", "ethene, C<sub>2</sub>H<sub>4</sub>"],
                  ["one triple + one single", "2", "linear", "180°", "ethyne, C<sub>2</sub>H<sub>2</sub>"]],
         "widths": [2.6, 1.6, 1.8, 1.3, 2.0],
         "caption": "Because each saturated carbon is tetrahedral, carbon chains are not straight but <b>zig-zag</b>: that is why we draw line structures as zig-zags.",
         "notes": "NAM-ALKANE 12.5. See the extra chapter on VSEPR and the Virtual Secret Lab for 3D practice."})
    add({"t": "check", "sec": 3, "lo": LO[3], "title": "Quick check",
         "q": "In a line structure, a carbon at the very end of a line, with no atom written, carries how many hydrogen atoms?",
         "opts": ["1", "2", "3", "4"], "ans": 2,
         "why": "It has one line (one bond to carbon), so it needs 4 − 1 = 3 hydrogens: a CH<sub>3</sub> group.",
         "notes": "Answer C."})
    add({"t": "check", "sec": 3, "lo": LO[3], "title": "Quick check",
         "q": "What is the molecular formula of CH<sub>3</sub>CH<sub>2</sub>OH (ethanol)?",
         "opts": ["C<sub>2</sub>H<sub>5</sub>O", "C<sub>2</sub>H<sub>6</sub>O", "C<sub>2</sub>H<sub>4</sub>O", "CH<sub>3</sub>O"], "ans": 1,
         "why": "Count all atoms: 2 C, 3 + 2 + 1 = 6 H, 1 O.", "notes": "Answer B."})

    # ---------------- 1.4 ----------------
    add({"t": "divider", "num": 4, "title": "Functional groups", "lo": LO[4], "src": "NAM-INTRO 12.2 · Soderberg Ch 1",
         "blurb": "The small groups of atoms that decide how a whole molecule behaves."})
    add({"t": "bullets", "sec": 4, "lo": LO[4], "title": "What is a functional group?",
         "items": ["Organic molecules are sorted into <b>families</b>. Members of a family have similar physical properties and predictable reactions.",
                   "What defines a family is its <b>functional group</b>: a specific arrangement of atoms or bonds.",
                   "<b>Alkanes</b> have only C–C and C–H single bonds and <b>no functional group</b>.",
                   "<b>R</b> stands for the rest of the molecule (a carbon chain). For example, an alcohol is <b>R–OH</b>.",
                   "Know the functional group, and you can predict how a medicine, a sugar or a fat will behave."],
         "notes": "NAM-INTRO 12.2, opening paragraphs."})
    add({"t": "table", "sec": 4, "lo": LO[4], "title": "Hydrocarbon and halogen families",
         "head": ["Family", "Functional group", "Example", "Structure", "Name"],
         "rows": [["alkane", "none (C–C, C–H only)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>3</sub>", mini("CCC"), "propane"],
                  ["alkene", "C=C", "H<sub>2</sub>C=CH<sub>2</sub>", mini("C=C"), "ethene (ethylene)"],
                  ["alkyne", "C≡C", "HC≡CH", mini("C#C"), "ethyne (acetylene)"],
                  ["aromatic", "benzene ring", "C<sub>6</sub>H<sub>6</sub>", mini("c1ccccc1"), "benzene"],
                  ["alkyl halide", "C–X (X = F, Cl, Br, I)", "CH<sub>3</sub>CH<sub>2</sub>Cl", mini("CCCl"), "chloroethane"]],
         "widths": [1.6, 2.4, 2.0, 1.8, 2.0], "caption": "Source: NAM-INTRO Table 12.2.1. Studied in Chapter 2.",
         "notes": "NAM-INTRO Table 12.2.1, first rows."})
    add({"t": "table", "sec": 4, "lo": LO[4], "title": "Oxygen families",
         "head": ["Family", "Functional group", "Example", "Structure", "Name"],
         "rows": [["alcohol", "–OH on a carbon chain", "CH<sub>3</sub>CH<sub>2</sub>OH", mini("CCO"), "ethanol"],
                  ["ether", "C–O–C", "CH<sub>3</sub>CH<sub>2</sub>OCH<sub>2</sub>CH<sub>3</sub>", mini("CCOCC"), "diethyl ether"],
                  ["aldehyde", "–CHO (C=O with an H)", "CH<sub>3</sub>CHO", mini("CC=O"), "ethanal"],
                  ["ketone", "C=O between two carbons", "CH<sub>3</sub>COCH<sub>3</sub>", mini("CC(C)=O"), "propanone (acetone)"],
                  ["carboxylic acid", "–COOH", "CH<sub>3</sub>COOH", mini("CC(=O)O"), "ethanoic acid (acetic acid)"],
                  ["ester", "–COO–C", "CH<sub>3</sub>COOCH<sub>3</sub>", mini("CC(=O)OC"), "methyl ethanoate"]],
         "widths": [1.6, 2.2, 2.4, 1.8, 2.2], "caption": "Source: NAM-INTRO Table 12.2.1. Alcohols, ethers, aldehydes and ketones: Chapter 3. Acids and esters: Chapter 4.",
         "notes": "NAM-INTRO Table 12.2.1. Anhydrides are in the table too but are not in the syllabus."})
    add({"t": "table", "sec": 4, "lo": LO[4], "title": "Nitrogen and sulfur families",
         "head": ["Family", "Functional group", "Example", "Structure", "Name"],
         "rows": [["amine", "C–N (–NH<sub>2</sub>, –NHR, –NR<sub>2</sub>)", "CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>", mini("CCN"), "ethylamine"],
                  ["amide", "–CONH<sub>2</sub> (C=O bonded to N)", "CH<sub>3</sub>CONH<sub>2</sub>", mini("CC(N)=O"), "acetamide"],
                  ["thiol", "–SH", "CH<sub>3</sub>CH<sub>2</sub>SH", mini("CCS"), "ethanethiol"],
                  ["sulfide", "C–S–C", "CH<sub>3</sub>CH<sub>2</sub>SCH<sub>3</sub>", mini("CCSC"), "ethyl methyl sulfide"],
                  ["disulfide", "–S–S–", "CH<sub>3</sub>SSCH<sub>3</sub>", mini("CSSC"), "dimethyl disulfide"]],
         "widths": [1.5, 2.6, 2.2, 1.8, 2.0], "caption": "Source: NAM-INTRO Table 12.2.1. Thiols: Chapter 3. Amines and amides: Chapter 4.",
         "notes": "NAM-INTRO Table 12.2.1."})
    add({"t": "bullets", "sec": 4, "lo": LO[4], "title": "Telling the C=O families apart",
         "items": ["C=O is the <b>carbonyl group</b>. Look at what is attached to the carbonyl carbon:",
                   "an <b>H</b> → <b>aldehyde</b> · two <b>carbons</b> → <b>ketone</b>",
                   "an <b>–OH</b> → <b>carboxylic acid</b> · an <b>–O–C</b> → <b>ester</b>",
                   "a <b>nitrogen</b> → <b>amide</b>",
                   "Careful: an –OH on a benzene ring is a <b>phenol</b>, not an ordinary alcohol (Chapter 3). An –NH<sub>2</sub> without C=O is an <b>amine</b>, not an amide."],
         "side": {"h": "Exam tip", "body": "Do not stop at the first group you see. Most drugs have <b>two or more</b> functional groups."},
         "notes": "Teaching summary; families from NAM-INTRO Table 12.2.1."})
    add({"t": "figure", "pos": "leftwide", "sec": 4, "lo": LO[4], "title": "Functional groups in two everyday drugs",
         "fig": {"cap": HL_KEY,
                 "data": row([(mol(ASPIRIN, 280, 220, highlight=[RING, ACID, ESTER]), "aspirin"), (mol(PARACETAMOL, 280, 220, highlight=[RING, OH, AMIDE]), "paracetamol")])},
         "items": ["<b>Aspirin</b> (acetylsalicylic acid): an <b>aromatic ring</b>, a <b>carboxylic acid</b> and an <b>ester</b>.",
                   "<b>Paracetamol</b>: an <b>aromatic ring</b>, a <b>phenol</b> (–OH on the ring) and an <b>amide</b>.",
                   "Both relieve pain and fever, but their different groups give them different side effects and stabilities."],
         "notes": "Structures from PubChem (aspirin CID 2244, paracetamol CID 1983), drawn with RDKit."})
    add({"t": "example", "sec": 4, "lo": LO[4], "title": "Example 1.4 · Spot the groups",
         "q": "Identify every functional group in aspirin.",
         "fig": {"cap": HL_KEY, "data": mol(ASPIRIN, 380, 240, highlight=[RING, ACID, ESTER])},
         "steps": ["Find the hexagon with alternating double bonds: an <b>aromatic (benzene) ring</b>.",
                   "Find C=O groups and look at their neighbours. One C=O has an –OH: <b>carboxylic acid</b>.",
                   "The other C=O is bonded to an O that is bonded to the ring: <b>ester</b>.",
                   "Answer: aromatic ring, carboxylic acid, ester."],
         "notes": "Teaching example."})
    add({"t": "tryit", "sec": 4, "lo": LO[4], "title": "Try it · Ibuprofen",
         "q": "Name the functional groups in ibuprofen.",
         "afig": {"data": mol(IBUPROFEN, 380, 200, highlight=[RING, ACID])},
         "a": "An <b>aromatic ring</b> and a <b>carboxylic acid</b>. The rest is alkane-like chains (no functional group).",
         "notes": "Ibuprofen, PubChem CID 3672."})
    add({"t": "tryit", "sec": 4, "lo": LO[4], "title": "Try it · Benzocaine",
         "q": "Benzocaine is the local anaesthetic in some sore-throat lozenges. Name its functional groups.",
         "afig": {"data": mol(BENZOCAINE, 380, 200, highlight=[RING, ESTER, AMINE])},
         "a": "An <b>aromatic ring</b>, an <b>ester</b> (–COO–CH<sub>2</sub>CH<sub>3</sub>) and an <b>amine</b> (–NH<sub>2</sub> on the ring, with no C=O, so not an amide).",
         "notes": "Benzocaine, PubChem CID 2337."})
    add({"t": "check", "sec": 4, "lo": LO[4], "title": "Quick check",
         "q": "A compound has a C=O group whose carbon is also bonded to an H atom. Which family is it?",
         "opts": ["Ketone", "Aldehyde", "Carboxylic acid", "Ester"], "ans": 1,
         "why": "C=O with H on the carbonyl carbon = aldehyde (–CHO).", "notes": "Answer B."})
    add({"t": "check", "sec": 4, "lo": LO[4], "title": "Quick check",
         "q": "Which functional group do aspirin and ibuprofen both contain?",
         "opts": ["Amide", "Ester", "Carboxylic acid", "Amine"], "ans": 2,
         "why": "Both have –COOH. Aspirin also has an ester; neither has an amide or amine.", "notes": "Answer C."})

    # ---------------- 1.5 ----------------
    add({"t": "divider", "num": 5, "title": "Organic chemistry in pharmacy and everyday life", "lo": LO[5], "src": "Dr. NAM · FGOB 16.7 · PubChem",
         "blurb": "Natural or synthetic, drugs from plants, one drug with three names, and the chemistry on every shelf."})
    add({"t": "bullets", "sec": 5, "lo": "CH1-LO4", "title": "Natural or synthetic: does it matter?",
         "items": ["A compound is defined by its <b>structure</b>, not by where it came from.",
                   "Vitamin C from an orange and vitamin C made in a factory are the <b>same molecule</b> (ascorbic acid). They have identical properties and the body cannot tell them apart.",
                   "What <b>can</b> differ: purity, the dose, and the <b>other</b> compounds present. A plant extract contains many compounds, not just one.",
                   "\"Natural\" does not mean \"safe\": digoxin from the foxglove plant is a life-saving heart drug but toxic in overdose."],
         "side": {"h": "Pharmacist's view", "body": "When a customer asks whether a natural product is safer, think about the <b>molecules and doses</b>, not the label."},
         "notes": "Original material. Vitamin C = L-ascorbic acid; synthetic and natural forms are chemically identical."})
    add({"t": "figure", "pos": "leftwide", "sec": 5, "lo": "CH1-LO5", "title": "From willow bark to aspirin",
         "fig": {"cap": "Changing one functional group: the –OH of salicylic acid becomes an ester in aspirin. " + HL_KEY,
                 "data": row([(mol(SALICYLIC, 270, 210, highlight=[RING, ACID, OH]), "salicylic acid"), (mol(ASPIRIN, 270, 210, highlight=[RING, ACID, ESTER]), "aspirin")], w=270)},
         "items": ["Willow bark has been used for pain and fever since ancient times. Its active compound, <b>salicin</b>, was isolated in the 19th century.",
                   "The body turns it into <b>salicylic acid</b>: it works, but it irritates the stomach badly.",
                   "In 1897 chemists at Bayer made <b>acetylsalicylic acid</b> by turning the –OH into an <b>ester</b>. It was sold as <b>aspirin</b> from 1899.",
                   "A small change in one functional group made a gentler, more useful medicine."],
         "notes": "Original summary of well-documented history (Felix Hoffmann, Bayer, 1897; trademark 1899)."})
    add({"t": "table", "sec": 5, "lo": "CH1-LO5", "title": "Medicines from nature",
         "head": ["Medicine", "Natural source", "Used for"],
         "rows": [["morphine", "opium poppy", "severe pain"],
                  ["quinine", "cinchona tree bark", "malaria (historically); still used in some cases"],
                  ["artemisinin", "sweet wormwood (<i>Artemisia annua</i>)", "malaria; its discovery earned Tu Youyou the 2015 Nobel Prize"],
                  ["paclitaxel", "Pacific yew tree bark", "several cancers"],
                  ["digoxin", "foxglove plant", "heart failure, irregular heartbeat"],
                  ["penicillin", "<i>Penicillium</i> mould", "bacterial infections"]],
         "widths": [1.8, 3.0, 4.0],
         "caption": "Morphine and quinine are <b>alkaloids</b>: nitrogen-containing plant compounds (FGOB 16.7; amines in Chapter 4). Many modern drugs come from, or are modelled on, natural products.",
         "notes": "Well-established examples; FGOB 16.7 Amines in Plants: Alkaloids."})
    add({"t": "two", "sec": 5, "lo": "CH1-LO5", "title": "One drug, three names",
         "lead": "Every medicine has a <b>chemical name</b>, a <b>generic name</b> and one or more <b>brand names</b>.",
         "cols": [{"h": "Paracetamol", "tone": "cold", "items": [
             "<b>Chemical (IUPAC) name</b>: N-(4-hydroxyphenyl)acetamide. It describes the structure: an amide on a phenol ring",
             "<b>Generic name</b>: paracetamol (called acetaminophen in the USA). Used on prescriptions and in pharmacy references",
             "<b>Brand names</b>: Panadol and many others, chosen by each manufacturer"]},
             {"h": "Why it matters", "tone": "heat", "items": [
                 "Many cold and flu remedies <b>also</b> contain paracetamol",
                 "A patient taking two brands may not realise both contain the same drug",
                 "Always read the <b>generic</b> name of the active ingredients to avoid a double dose",
                 "The IUPAC name lets a chemist draw the exact structure"]}],
         "notes": "Original pharmacy content. IUPAC name per PubChem CID 1983."})
    add({"t": "bullets", "sec": 5, "lo": "CH1-LO5", "title": "Structure decides how a drug behaves",
         "items": ["<b>Polar groups</b> (–OH, –COOH, –NH<sub>2</sub>) help a drug dissolve in water: in the blood, or in a syrup or injection.",
                   "<b>Nonpolar parts</b> (rings, carbon chains) help a drug cross fatty cell membranes. Most drugs need a balance of both.",
                   "<b>Acidic and basic groups</b> let a drug be made as a <b>salt</b> that dissolves better (Chapter 4).",
                   "Some groups <b>break down</b> on storage. An ester reacts slowly with water, so moisture shortens shelf life."],
         "notes": "Original material linking functional groups to solubility, absorption and stability."})
    add({"t": "example", "sec": 5, "lo": "CH1-LO5", "title": "Example 1.5 · The vinegar smell",
         "q": "A customer says an old bottle of aspirin smells of vinegar. Explain why, using functional groups.",
         "steps": ["Aspirin contains an <b>ester</b> group.",
                   "In moist air, the ester slowly reacts with water (<b>hydrolysis</b>, Chapter 4).",
                   "The products are <b>salicylic acid</b> and <b>acetic acid</b>. Acetic acid is the acid in vinegar, so the bottle smells of vinegar.",
                   "Advice: the tablets have lost strength and should be discarded. Store medicines in a cool, <b>dry</b> place with the cap closed."],
         "notes": "Classic stability example; ester hydrolysis is taught in Chapter 4."})
    add({"t": "table", "sec": 5, "lo": "CH1-LO5", "title": "Organic chemistry on the shelf",
         "head": ["Product", "Organic compounds inside", "Chapter"],
         "rows": [["soap", "sodium salts of long-chain fatty acids", "6"],
                  ["cosmetics", "<b>parabens</b> (esters) as preservatives; oils and waxes", "4, 6"],
                  ["sunscreen", "aromatic compounds that absorb UV light, such as avobenzone", "2"],
                  ["plastic bottles and bags", "polymers made from alkenes, such as polyethylene", "2"],
                  ["diet drinks", "<b>aspartame</b> (an ester and an amide); labels warn it contains phenylalanine", "4, 7"],
                  ["food preservative", "sodium benzoate (salt of an aromatic carboxylic acid)", "4"]],
         "widths": [2.0, 5.0, 1.0],
         "caption": "Pharmacy link: patients with phenylketonuria (PKU) must avoid aspartame. Reading ingredient labels is chemistry in action.",
         "notes": "Original material. Aspartame is the methyl ester of the dipeptide Asp-Phe."})
    add({"t": "tryit", "sec": 5, "lo": "CH1-LO5", "title": "Try it · Read the label",
         "q": "A patient takes Panadol for a headache, and also a flu tablet whose label reads: <i>Each tablet contains paracetamol 500 mg, phenylephrine 5 mg</i>. What is the risk, and what should the pharmacist advise?",
         "a": "Both products contain <b>paracetamol</b>, so the patient could exceed the safe daily dose (usually no more than <b>4 g in 24 hours</b> for a healthy adult), risking liver damage. Advise taking only <b>one</b> paracetamol-containing product and checking generic names on every label.",
         "notes": "Original scenario. Standard adult maximum 4 g/24 h; lower limits apply to some patients."})
    add({"t": "check", "sec": 5, "lo": "CH1-LO4", "title": "Quick check",
         "q": "Which statement about natural and synthetic vitamin C is correct?",
         "opts": ["Natural vitamin C is a different molecule", "Synthetic vitamin C is always less effective",
                  "They are the same molecule with identical properties", "Only natural vitamin C is organic"], "ans": 2,
         "why": "A compound is defined by its structure, not its source.", "notes": "Answer C."})
    add({"t": "check", "sec": 5, "lo": "CH1-LO5", "title": "Quick check",
         "q": "Which functional group in aspirin breaks down when tablets are stored in damp conditions?",
         "opts": ["Aromatic ring", "Ester", "Carboxylic acid", "Amide"], "ans": 1,
         "why": "The ester is hydrolysed by water, giving salicylic acid and acetic acid.", "notes": "Answer B."})

    # ---------------- wrap-up ----------------
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Organic chemistry", "the chemistry of carbon compounds; Wöhler's urea (1828) ended vitalism"],
        ["Not organic", "CO, CO<sub>2</sub>, carbonates, bicarbonates and cyanides"],
        ["Carbon", "4 valence electrons, 4 covalent bonds; chains, branches, rings; single, double, triple bonds"],
        ["Organic vs inorganic", "organic: low melting, flammable, covalent, non-conducting (with exceptions)"],
        ["Drawing", "molecular · expanded · condensed · line-angle; ends and bends are carbons; H on C hidden"],
        ["Shapes", "tetrahedral 109.5° · trigonal planar 120° · linear 180°"],
        ["Functional groups", "decide the family, properties and reactions; most drugs have two or more"],
        ["Pharmacy", "same molecule = same properties; check generic names; esters hydrolyse in moisture"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 25 min)", "Attempt the Chapter 1 tutorial",
                   "Play the Chapter 1 game to find your weak outcomes", "Next chapter: Saturated and Unsaturated Hydrocarbons"],
         "attrib": "Adapted from LibreTexts (Sharpe Elles; Ball, Hill &amp; Scott; FGOB), CC BY-NC-SA 3.0, and Soderberg, CC BY-NC-SA 4.0. Subchapter 1.5 is original material by Dr. NAM. Full credits on the title slide notes and the Study Hub.", "notes": "Point students to the Study Hub. Full attribution: " + META["attrib"]})
    return S
