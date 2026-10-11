"""PHD125 Chapter 6 · Lipids · lecture slide content.
Sources: FGOB 23.1, 23.2 (fatty acids, waxes, triacylglycerols), 23.6 (steroids) and 23.7 (cell membranes),
LibreTexts, CC BY-NC-SA 3.0 (adapted from Ball, Hill & Scott, chapter 17).
Original material by Dr. NAM, because FGOB 23.3 (properties of fats and oils), 23.4 (reactions of triacylglycerols) and
23.5 (phospholipids and glycolipids) are empty placeholders: physical properties, hydrolysis, saponification and soaps,
hydrogenation and trans fats, rancidity and antioxidants, iodine value, phospholipids, sphingolipids and glycolipids,
plus omega notation and the pharmacy links. Membrane and micelle schematics are drawn by _src/lipidfigs.py."""
from figs import mol, row, scheme, stack
from lipidfigs import amphipathic_parts, soap_micelle, lipid_shapes, membrane, steroid_rings, triglyceride
from rdkit.Chem import rdDepictor


def mol_cg(smi, w, h, **k):
    """RDKit drawing with CoordGen layout (tidier for long branched lipids)."""
    rdDepictor.SetPreferCoordGen(True)
    try:
        return mol(smi, w, h, **k)
    finally:
        rdDepictor.SetPreferCoordGen(False)

LO1, LO2, LO3, LO4, LO5 = 'CH6-LO1', 'CH6-LO2', 'CH6-LO3', 'CH6-LO4', 'CH6-LO5'

STEARIC = 'CCCCCCCCCCCCCCCCCC(=O)O'
OLEIC = 'CCCCCCCC/C=C\\CCCCCCCC(=O)O'
ELAIDIC = 'CCCCCCCC/C=C/CCCCCCCC(=O)O'
LINOLEIC = 'CCCCC/C=C\\C/C=C\\CCCCCCCC(=O)O'
ALA = 'CC/C=C\\C/C=C\\C/C=C\\CCCCCCCC(=O)O'
TRISTEARIN = 'CCCCCCCCCCCCCCCCCC(=O)OCC(COC(=O)CCCCCCCCCCCCCCCCC)OC(=O)CCCCCCCCCCCCCCCCC'
TRIOLEIN = 'CCCCCCCC/C=C\\CCCCCCCC(=O)OCC(COC(=O)CCCCCCC/C=C\\CCCCCCCC)OC(=O)CCCCCCC/C=C\\CCCCCCCC'
CETYL_PALMITATE = 'CCCCCCCCCCCCCCCC(=O)OCCCCCCCCCCCCCCCC'
DPPC = 'CCCCCCCCCCCCCCCC(=O)OC[C@H](COP(=O)([O-])OCC[N+](C)(C)C)OC(=O)CCCCCCCCCCCCCCC'
CHOLESTEROL = 'C[C@H](CCCC(C)C)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CC=C4[C@@]3(CC[C@@H](C4)O)C)C'
TESTOSTERONE = 'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=CC(=O)CC[C@]34C'
CORTISOL = 'C[C@]12CCC(=O)C=C1CC[C@@H]3[C@@H]2[C@H](C[C@]4([C@H]3CC[C@@]4(C(=O)CO)O)C)O'
ESTRADIOL = 'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=C3C=CC(=C4)O'
PROGESTERONE = 'CC(=O)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CCC4=CC(=O)CC[C@]34C)C'
CHOLIC = 'C[C@H](CCC(=O)O)[C@H]1CC[C@@H]2[C@@]1([C@H](C[C@H]3[C@H]2[C@@H](C[C@H]4[C@@]3(CC[C@H](C4)O)C)O)O)C'

ESTER = ('[CX3](=O)[OX2][#6]', 'ester')
ACID = ('[CX3](=O)[OX2H1]', 'acid')
CC = ('[CX3]=[CX3]', 'ring')

META = {
    "code": "CH6", "chapter": "Chapter 6", "title": "Lipids", "short": "Lipids",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: FGOB 23.1–23.7 (adapted from Ball, Hill & Scott, chapter 17)",
    "attrib": ("Adapted from <i>Fundamentals of General Organic and Biological Chemistry</i> 23.1, 23.2, 23.6 and 23.7 (remixed from Ball, Hill &amp; Scott, "
               "<i>The Basics of GOB Chemistry</i>, chapter 17), LibreTexts, CC BY-NC-SA 3.0. Properties and reactions of fats and oils, phospholipids, "
               "sphingolipids, omega notation and the pharmacy links are original material by Dr. NAM, because those source pages are empty. "
               "Structures drawn with RDKit; membrane schematics by Dr. NAM. Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["glycerol", "butyricacid", "cholesterol"], "2": ["butyricacid", "aceticacid", "glycerol"], "3": ["ethylacetate", "glycerol", "butyricacid"],
               "4": ["glycerol", "ethylacetate", "butyricacid"], "5": ["glycerol", "butyricacid", "water"], "6": ["glycerol", "water", "ethanol"],
               "7": ["cholesterol", "water", "glycerol"], "8": ["cholesterol", "glycerol", "water"]},
    "titlemol": ["cholesterol", "glycerol", "butyricacid", "water"], "darkmol": "glycerol",
    "next": "Next chapter: Amino Acids, Proteins and Enzymes",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Define and classify lipids, and describe fatty acids: saturated or unsaturated, cis or trans, omega-3 and omega-6"],
    [LO2, "Describe waxes and triacylglycerols, and relate the melting points of fats and oils to their fatty acids"],
    [LO3, "Write equations for the hydrolysis, saponification and hydrogenation of triacylglycerols, and explain soaps and rancidity"],
    [LO4, "Describe phospholipids and glycolipids, and explain how they form cell membranes and control transport"],
    [LO5, "Recognise the steroid nucleus, and describe cholesterol, steroid hormones, bile salts and steroid drugs"],
]


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Lipids", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 6",
         "notes": "Chapter 6 of the course outline, in eight subchapters: the seven in the lesson plan, plus steroids."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1: 6.1–6.2. LO2: 6.3–6.4. LO3: 6.4–6.5. LO4: 6.6–6.7. LO5: 6.8."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>6.1 Introduction</b> and <b>6.2 Fatty Acids</b> (FGOB 23.1–23.2): what makes a lipid, saturated and unsaturated chains",
        "<b>6.3 Waxes</b> (FGOB 23.2): long-chain esters that waterproof leaves, feathers and tablets",
        "<b>6.4 Triacylglycerols</b> and <b>6.5 Their Hydrolysis</b>: fats and oils, hydrogenation, rancidity, saponification and soap",
        "<b>6.6 Phospholipids</b> and <b>6.7 Cell Membranes</b> (FGOB 23.7): the bilayer, and how molecules and drugs cross it",
        "<b>6.8 Steroids</b> (FGOB 23.6): cholesterol, hormones, bile salts and steroid medicines"],
         "notes": "6.3 Waxes is a short subchapter."})
    add({"t": "hook", "title": "Think first",
         "q": "Palm oil, a bar of soap, the coating on a shiny tablet, the wall around every cell in your body, and a hydrocortisone cream. What do they have in common?",
         "a": "All are <b>lipids</b> or made from them: palm oil is a <b>triacylglycerol</b>; soap is made by <b>hydrolysing</b> it; carnauba <b>wax</b> polishes tablets; cell membranes are <b>phospholipid</b> bilayers; hydrocortisone is a <b>steroid</b>. They look nothing alike, but none of them dissolves well in water.",
         "notes": "Pairs discuss for one minute. Malaysia is a leading palm oil producer."})

    # ================= 6.1 INTRODUCTION =================
    add({"t": "divider", "num": 1, "title": "Introduction to Lipids", "lo": "CH6-LO1", "src": "FGOB 23.1",
         "blurb": "A family defined by a property, not a functional group: lipids dissolve in nonpolar solvents, not in water."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "What is a lipid?",
         "items": ["Lipids are defined by <b>solubility</b>: they dissolve in nonpolar organic solvents (such as dichloromethane or ether) far better than in water.",
                   "So the family is varied: fats and oils, waxes, phospholipids, steroids, prostaglandins.",
                   "Energy store: fats give about <b>9 kcal/g</b> when oxidised, carbohydrates only <b>4 kcal/g</b>. We store energy as fat because it packs more energy into less space.",
                   "Other jobs: cell membranes, padding and insulation around organs, hormones, and carrying the fat-soluble vitamins <b>A, D, E and K</b>."],
         "notes": "FGOB 23.1."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Classifying lipids",
         "head": ["Class", "Built from", "Examples"],
         "rows": [["<b>Waxes</b>", "long-chain fatty acid + long-chain alcohol (ester)", "beeswax, carnauba wax"],
                  ["<b>Triacylglycerols</b> (triglycerides)", "glycerol + 3 fatty acids (esters)", "fats and oils"],
                  ["<b>Glycerophospholipids</b>", "glycerol + 2 fatty acids + phosphate + amino alcohol", "lecithin (cell membranes)"],
                  ["<b>Sphingolipids</b>", "sphingosine + fatty acid (amide) + phosphate or sugar", "sphingomyelin, glycolipids"],
                  ["<b>Steroids</b>", "four fused rings; <b>no fatty acid</b>", "cholesterol, hormones"],
                  ["<b>Eicosanoids</b>", "made from a C20 fatty acid", "prostaglandins"]],
         "widths": [3.0, 4.2, 2.8],
         "caption": "Lipids with ester bonds react with NaOH (<b>saponifiable</b>); steroids do not (<b>nonsaponifiable</b>). Source: FGOB 23.1, 23.6.",
         "notes": "FGOB 23.1 classification; saponifiable terms from FGOB 23.6."})
    add({"t": "check", "sec": 1, "lo": LO1, "title": "Quick check",
         "q": "Lipids are grouped together because they:",
         "opts": ["are more soluble in nonpolar solvents than in water", "all contain ester groups", "all contain glycerol", "are all solids"], "ans": 0,
         "why": "Steroids, for example, have no ester or glycerol.", "notes": "Answer A."})

    # ================= 6.2 FATTY ACIDS =================
    add({"t": "divider", "num": 2, "title": "Fatty Acids", "lo": "CH6-LO1", "src": "FGOB 23.1–23.2",
         "blurb": "Long-chain carboxylic acids: the building blocks of most lipids. One cis double bond changes everything."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO1, "title": "Saturated and unsaturated fatty acids",
         "fig": {"cap": "The cis double bond in oleic acid puts a kink in the chain.",
                 "data": stack([mol(STEARIC, 760, 110, highlight=[ACID]), mol(OLEIC, 760, 150, highlight=[ACID, CC])], w=760, row_h=135)},
         "items": ["Fatty acids are long, <b>unbranched</b> carboxylic acids, usually with an <b>even</b> number of carbons (12–20).",
                   "<b>Saturated</b>: only C–C single bonds (stearic acid, top). <b>Monounsaturated</b>: one C=C (oleic acid, bottom). <b>Polyunsaturated</b>: two or more.",
                   "Natural unsaturated fatty acids are almost all <b>cis</b>, which bends the chain."],
         "notes": "FGOB 23.2."})
    add({"t": "table", "sec": 2, "lo": LO1, "title": "Common fatty acids",
         "head": ["Name", "Shorthand", "Condensed formula", "mp (°C)", "Source"],
         "rows": [["lauric acid", "C12:0", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>10</sub>COOH", "44", "palm kernel oil"],
                  ["myristic acid", "C14:0", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>12</sub>COOH", "58", "nutmeg oil"],
                  ["palmitic acid", "C16:0", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>14</sub>COOH", "63", "palm oil"],
                  ["stearic acid", "C18:0", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>16</sub>COOH", "70", "cocoa butter"],
                  ["oleic acid", "C18:1", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>7</sub>CH=CH(CH<sub>2</sub>)<sub>7</sub>COOH", "16", "olive oil"],
                  ["linoleic acid", "C18:2", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>3</sub>(CH<sub>2</sub>CH=CH)<sub>2</sub>(CH<sub>2</sub>)<sub>7</sub>COOH", "−5", "canola oil"],
                  ["α-linolenic acid", "C18:3", "CH<sub>3</sub>(CH<sub>2</sub>CH=CH)<sub>3</sub>(CH<sub>2</sub>)<sub>7</sub>COOH", "−11", "flaxseed"],
                  ["arachidonic acid", "C20:4", "CH<sub>3</sub>(CH<sub>2</sub>)<sub>4</sub>(CH<sub>2</sub>CH=CH)<sub>4</sub>(CH<sub>2</sub>)<sub>2</sub>COOH", "−50", "liver"]],
         "widths": [2.2, 1.3, 4.6, 1.0, 1.8],
         "caption": "Shorthand: <b>carbons : double bonds</b>, so oleic acid is C18:1. Source: FGOB Table 23.2.1.",
         "notes": "FGOB 23.2 table."})
    add({"t": "two", "sec": 2, "lo": LO1, "title": "Why double bonds lower the melting point",
         "lead": "Compare the C18 acids: stearic (0 C=C) 70 °C, oleic (1) 16 °C, linoleic (2) −5 °C, α-linolenic (3) −11 °C.",
         "cols": [{"h": "Saturated chains", "tone": "cold", "items": [
             "Straight, zigzag chains pack <b>closely</b> side by side",
             "Many contacts → strong <b>dispersion forces</b>",
             "High melting points: solid at room temperature",
             "Longer chains melt higher (lauric 44 °C → stearic 70 °C)"]},
             {"h": "Cis-unsaturated chains", "tone": "heat", "items": [
                 "Each cis double bond puts a <b>kink</b> in the chain",
                 "Kinked chains cannot pack closely → weaker forces",
                 "More C=C → lower melting point: liquid oils",
                 "Trans double bonds keep the chain fairly straight, so trans fats pack like saturated ones"]}],
         "notes": "FGOB 23.2 (data); packing explanation original."})
    add({"t": "bullets", "sec": 2, "lo": LO1, "title": "Omega-3 and omega-6; essential fatty acids",
         "items": ["Count from the <b>methyl (CH<sub>3</sub>) end</b>, called omega (ω): the position of the first C=C gives the family.",
                   "<b>ω-3</b>: α-linolenic acid (flaxseed), and EPA and DHA (fish oils). <b>ω-6</b>: linoleic acid and arachidonic acid.",
                   "<b>Essential fatty acids</b>: linoleic and α-linolenic acids. The body cannot make them, so they must come from food (about 4–6 g a day).",
                   "Linoleic acid is the starting point for arachidonic acid, which is turned into <b>prostaglandins</b>."],
         "side": {"h": "Pharmacy shelf", "body": "Fish-oil capsules (EPA + DHA) are among the most sold supplements; prescription omega-3 products lower blood triglycerides."},
         "notes": "Essential fatty acids: FGOB 23.2. Omega notation and supplements original."})
    add({"t": "bullets", "sec": 2, "lo": LO1, "title": "Prostaglandins and NSAIDs",
         "items": ["<b>Prostaglandins</b> are C20 fatty acid derivatives with a five-membered ring, made from arachidonic acid in almost every tissue.",
                   "They cause smooth-muscle contraction, inflammation, pain and fever, and affect blood pressure and clotting.",
                   "<b>Aspirin</b> and <b>ibuprofen</b> (NSAIDs) block <b>cyclooxygenase (COX)</b>, the enzyme for the first step from arachidonic acid. That is how they relieve pain and inflammation.",
                   "Prostaglandin drugs: PGE<sub>2</sub> derivatives to induce labour; misoprostol protects the stomach; latanoprost eye drops for glaucoma."],
         "notes": "FGOB 23.1 (To Your Health: Prostaglandins). Misoprostol and latanoprost original."})
    add({"t": "check", "sec": 2, "lo": LO1, "title": "Quick check",
         "q": "Which fatty acid has the lowest melting point?",
         "opts": ["α-linolenic acid (C18:3)", "stearic acid (C18:0)", "oleic acid (C18:1)", "palmitic acid (C16:0)"], "ans": 0,
         "why": "Three cis double bonds: the most kinks and the poorest packing (−11 °C).", "notes": "Answer A."})
    add({"t": "check", "sec": 2, "lo": LO1, "title": "Quick check",
         "q": "Aspirin reduces inflammation by blocking the synthesis of:",
         "opts": ["prostaglandins", "cholesterol", "phospholipids", "triglycerides"], "ans": 0,
         "why": "It inhibits cyclooxygenase.", "notes": "Answer A."})

    # ================= 6.3 WAXES =================
    add({"t": "divider", "num": 3, "title": "Waxes", "lo": "CH6-LO2", "src": "FGOB 23.2",
         "blurb": "Esters of a long-chain acid and a long-chain alcohol: nature's waterproofing."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO2, "title": "Waxes: long-chain esters",
         "fig": {"cap": "Cetyl palmitate (C16 acid + C16 alcohol), the main ester of spermaceti wax.",
                 "data": mol(CETYL_PALMITATE, 820, 130, highlight=[ESTER])},
         "items": ["A wax is an <b>ester</b> of a long-chain fatty acid and a long-chain alcohol. Natural waxes are mixtures of such esters.",
                   "Both ends are long hydrocarbon chains, so waxes are very <b>water-repellent</b> and solid at room temperature.",
                   "Plants coat leaves and fruit with wax against water loss and microbes; birds' feathers and our skin and hair are protected by waxes."],
         "notes": "FGOB 23.2 (Waxes); cetyl palmitate example original."})
    add({"t": "table", "sec": 3, "lo": LO2, "title": "Waxes you will meet",
         "head": ["Wax", "Source", "Uses"],
         "rows": [["<b>carnauba wax</b>", "leaves of a Brazilian palm (mainly myricyl cerotate)", "car and floor polish; <b>polishing coated tablets</b> to a shine"],
                  ["<b>beeswax</b>", "honeycomb", "ointments, lip balms, creams (white and yellow beeswax)"],
                  ["<b>lanolin</b> (wool fat)", "sheep's wool", "ointment bases and nipple creams; can cause skin allergy"],
                  ["<b>spermaceti</b>", "sperm whale (now replaced by synthetic cetyl esters)", "historical cream base"]],
         "widths": [2.2, 3.8, 4.0],
         "caption": "Waxes are hydrolysed only slowly, which is why they last as protective coatings. Source: FGOB 23.2 (carnauba); pharmacy uses added.",
         "notes": "FGOB 23.2 for carnauba; others original."})
    add({"t": "check", "sec": 3, "lo": LO2, "title": "Quick check",
         "q": "A wax is formed from:",
         "opts": ["a long-chain fatty acid and a long-chain alcohol", "glycerol and three fatty acids", "a fatty acid and an amine", "four fused rings"], "ans": 0,
         "why": "It is a single ester with long chains on both sides.", "notes": "Answer A."})

    # ================= 6.4 TRIACYLGLYCEROLS =================
    add({"t": "divider", "num": 4, "title": "Triacylglycerols", "lo": "CH6-LO2 to LO3", "src": "FGOB 23.2 (23.3–23.4 are empty)",
         "blurb": "Fats and oils: glycerol carrying three fatty acids. Why palm oil is semi-solid, how margarine is made, and why oils go rancid."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO2, "title": "Triacylglycerols (triglycerides)",
         "fig": {"cap": "Glycerol + 3 fatty acids → triacylglycerol + 3 H<sub>2</sub>O.",
                 "data": row([(triglyceride(['(CH₂)₁₆CH₃'] * 3), "tristearin: a simple triglyceride"), (triglyceride(['(CH₂)₁₄CH₃', '(CH₂)₇CH=CH(CH₂)₇CH₃', '(CH₂)₁₆CH₃']), "a mixed triglyceride (palmitic, oleic, stearic)")], w=520, h=230)},
         "items": ["Each –OH of <b>glycerol</b> forms an <b>ester</b> with a fatty acid (Chapter 4).",
                   "<b>Simple</b> triglyceride: three identical fatty acids (rare in nature). <b>Mixed</b>: two or three different ones (most natural fats).",
                   "Natural fats and oils are complex <b>mixtures</b> of triglycerides, so no single formula describes them."],
         "notes": "FGOB 23.2."})
    add({"t": "two", "sec": 4, "lo": LO2, "title": "Fats versus oils",
         "lead": "A triacylglycerol that is solid at 25 °C is a <b>fat</b>; one that is liquid is an <b>oil</b>.",
         "cols": [{"h": "Fats", "tone": "cold", "items": [
             "Mostly <b>saturated</b> fatty acids",
             "Usually from <b>animals</b>: butter, lard, tallow",
             "Exceptions: coconut and palm kernel oils are highly saturated plant fats"]},
             {"h": "Oils", "tone": "heat", "items": [
                 "Mostly <b>unsaturated</b> (cis) fatty acids",
                 "Usually from <b>plants</b>: olive, canola, corn, soybean",
                 "Fish oils are rich in polyunsaturated ω-3 acids"]}],
         "notes": "FGOB 23.2."})
    add({"t": "table", "sec": 4, "lo": LO2, "title": "Fatty acids in common fats and oils (%)",
         "head": ["Source", "Lauric C12:0", "Myristic C14:0", "Palmitic C16:0", "Stearic C18:0", "Oleic C18:1", "Linoleic C18:2", "Linolenic C18:3"],
         "rows": [["butter", "3", "11", "27", "12", "29", "2", "1"], ["lard", "—", "2", "26", "14", "44", "10", "—"],
                  ["coconut oil", "47", "18", "9", "3", "6", "2", "—"], ["olive oil", "—", "—", "13", "3", "71", "10", "1"],
                  ["corn oil", "—", "—", "11", "2", "28", "58", "1"], ["canola oil", "—", "—", "4", "2", "62", "22", "10"],
                  ["soybean oil", "—", "—", "11", "4", "24", "54", "7"]],
         "widths": [2.0, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2],
         "caption": "Palmitic is the most common saturated acid, oleic the most common unsaturated one. (Palm oil, not in the source table, is about 45% palmitic and 40% oleic acid.) Source: FGOB Table 23.2.2.",
         "notes": "FGOB 23.2 table; palm oil note original (approximate)."})
    add({"t": "bullets", "sec": 4, "lo": LO2, "title": "Physical properties of fats and oils",
         "items": ["<b>Insoluble in water</b>: long nonpolar chains, and no –OH or –COOH left. They dissolve in nonpolar solvents.",
                   "<b>Less dense than water</b> (about 0.9 g/mL), so oil floats.",
                   "Pure fats are colourless and odourless; colours and flavours come from small amounts of other compounds.",
                   "Melting points rise with chain length and fall with the number of cis double bonds (6.2).",
                   "<b>Pharmacy</b>: oils are vehicles for oily injections and drops (arachis/peanut oil, sesame oil, castor oil); fats such as cocoa butter (theobroma oil) make <b>suppositories</b> that melt at body temperature."],
         "notes": "Original (FGOB 23.3 is empty)."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO3, "title": "Hydrogenation: oils into solid fats",
         "fig": {"cap": "Adding H<sub>2</sub> across each C=C turns oleic acid chains into stearic acid chains.",
                 "data": scheme([('m', OLEIC, 'oleic acid (C18:1, mp 16 °C)', 380), ('>', 'H₂, Ni, heat', ''), ('m', STEARIC, 'stearic acid (C18:0, mp 70 °C)', 380)], h=130)},
         "items": ["The same addition reaction as alkenes in Chapter 2. Fewer C=C → higher melting point.",
                   "<b>Partial</b> hydrogenation turns liquid oils into spreadable <b>margarine</b> and shortening.",
                   "Side effect: some cis C=C bonds that are not hydrogenated are turned into <b>trans</b> bonds: <b>trans fats</b>.",
                   "Trans fats raise LDL (\"bad\") cholesterol and heart-disease risk; many countries now limit them."],
         "notes": "Original (FGOB 23.4 is empty). FGOB 23.6 recommends reducing trans fatty acids."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO3, "title": "Cis versus trans",
         "fig": {"cap": "Oleic acid (cis, natural) and elaidic acid (trans, formed in partial hydrogenation): same formula, different shape.",
                 "data": stack([mol(OLEIC, 760, 150, highlight=[CC]), mol(ELAIDIC, 760, 110, highlight=[CC])], w=760, row_h=135)},
         "items": ["Trans chains are straighter, so trans fats pack like saturated fats and are solid at room temperature (elaidic acid melts at about 45 °C).",
                   "Cis-trans isomerism was introduced with alkenes in Chapter 2."],
         "notes": "Original; elaidic acid mp about 43–45 °C."})
    add({"t": "two", "sec": 4, "lo": LO3, "title": "Rancidity: why fats go off",
         "lead": "Rancid fats smell and taste unpleasant. There are two causes.",
         "cols": [{"h": "Oxidative rancidity", "tone": "cold", "items": [
             "O<sub>2</sub> attacks the carbons next to C=C bonds in <b>unsaturated</b> chains",
             "The chains break into smelly short <b>aldehydes and acids</b>",
             "Speeded up by light, heat and metal ions",
             "Prevented by <b>antioxidants</b>: vitamin E (tocopherol), BHA, BHT"]},
             {"h": "Hydrolytic rancidity", "tone": "heat", "items": [
                 "Water and microbial <b>lipases</b> hydrolyse the ester bonds",
                 "Short free fatty acids are released: <b>butyric acid</b> in rancid butter",
                 "Speeded up by moisture and warmth",
                 "Prevented by keeping fats dry and cool"]}],
         "notes": "Original. Butyric acid in rancid butter: Ball 15.1 (Chapter 4)."})
    add({"t": "bullets", "sec": 4, "lo": LO2, "title": "Measuring unsaturation: the iodine value",
         "items": ["Iodine (as ICl or IBr) adds across C=C bonds, just as Br<sub>2</sub> does with alkenes.",
                   "<b>Iodine value</b> = grams of iodine taken up by 100 g of fat. More C=C → higher iodine value.",
                   "Coconut oil is low (about 10); olive oil about 80; soybean oil about 130; linseed (flaxseed) oil about 180.",
                   "Pharmacopoeias set iodine-value limits to check the identity and quality of oils used in medicines."],
         "notes": "Original; iodine values approximate typical ranges."})
    add({"t": "check", "sec": 4, "lo": LO2, "title": "Quick check",
         "q": "Olive oil is liquid but butter is solid at 25 °C mainly because olive oil contains:",
         "opts": ["more cis-unsaturated fatty acids", "more glycerol", "longer fatty acid chains", "trans fatty acids"], "ans": 0,
         "why": "71% oleic acid; the cis kinks prevent close packing.", "notes": "Answer A."})
    add({"t": "check", "sec": 4, "lo": LO3, "title": "Quick check",
         "q": "Which change happens during the partial hydrogenation of a vegetable oil?",
         "opts": ["Some C=C bonds gain H<sub>2</sub> and some cis bonds become trans", "Ester bonds are hydrolysed", "Glycerol is oxidised", "The oil becomes a wax"], "ans": 0,
         "why": "This is how margarine is made, and how trans fats form.", "notes": "Answer A."})

    # ================= 6.5 HYDROLYSIS =================
    add({"t": "divider", "num": 5, "title": "Hydrolysis of Triacylglycerols", "lo": "CH6-LO3", "src": "original (FGOB 23.4 is empty)",
         "blurb": "Splitting the three ester bonds: how we digest fat, and how soap is made."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO3, "title": "Hydrolysis: digestion of fats",
         "fig": {"cap": "Triacylglycerol + 3 H<sub>2</sub>O → glycerol + 3 fatty acids (acid or enzyme).",
                 "data": scheme([('m', 'CCCC(=O)OCC(COC(=O)CCC)OC(=O)CCC', 'tributyrin (a small triglyceride)', 300), ('+',), ('t', '3 H₂O', 70), ('>', 'lipase (or H⁺)', ''), ('m', 'OCC(O)CO', 'glycerol', 130), ('+',), ('t', '3', 26), ('m', 'CCCC(=O)O', 'butyric acid', 130)], h=150)},
         "items": ["The reverse of ester formation (Chapter 4): water splits each of the three ester bonds.",
                   "In the small intestine, <b>pancreatic lipase</b> does this. <b>Bile salts</b> first break fat into tiny droplets (emulsify it) so the enzyme can reach it (6.8).",
                   "<b>Orlistat</b>, an anti-obesity drug, blocks lipase, so about a third of dietary fat is not absorbed."],
         "notes": "Original. Orlistat reduces fat absorption by about 30%."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO3, "title": "Saponification: making soap",
         "fig": {"cap": "Triacylglycerol + 3 NaOH → glycerol + 3 sodium carboxylates (soap).",
                 "data": scheme([('m', 'CCCC(=O)OCC(COC(=O)CCC)OC(=O)CCC', 'a triglyceride', 300), ('+',), ('t', '3 NaOH', 80), ('>', 'heat', ''), ('m', 'OCC(O)CO', 'glycerol', 130), ('+',), ('t', '3', 26), ('m', 'CCCC(=O)[O-].[Na+]', 'sodium carboxylate', 170)], h=150)},
         "items": ["Basic hydrolysis of esters (Chapter 4) applied to fats: it goes to <b>completion</b>, and the base is used up.",
                   "Sodium salts give hard bar soaps; <b>potassium</b> salts give soft and liquid soaps.",
                   "Glycerol is a by-product, used as a humectant in creams (Chapter 3).",
                   "<b>Saponification value</b>: mg of KOH to saponify 1 g of fat. Shorter chains → more ester groups per gram → higher value."],
         "notes": "Original (FGOB 23.4 empty); builds on Chapter 4 saponification."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO3, "title": "How soap cleans",
         "fig": {"cap": "Left: soap is amphipathic. Right: soap anions surround a grease droplet, forming a micelle that water can rinse away.",
                 "data": row([(amphipathic_parts(), ""), (soap_micelle(), "")], w=440, h=230)},
         "items": ["A soap anion has a <b>polar, ionic head</b> (–COO<sup>−</sup>) and a long <b>nonpolar tail</b>.",
                   "The tails dissolve in the grease; the heads face the water. The coated droplets (<b>micelles</b>) repel each other and wash away.",
                   "In <b>hard water</b>, Ca<sup>2+</sup> and Mg<sup>2+</sup> form insoluble salts with soap: scum. Synthetic detergents (sulfonates) do not.",
                   "The same idea lets <b>emulsifiers</b> stabilise creams and lotions."],
         "notes": "Original."})
    add({"t": "example", "sec": 5, "lo": LO3, "title": "Example 6.1 · Products of saponification",
         "q": "Tripalmitin (glycerol esterified with three palmitic acids, C16:0) is boiled with KOH solution. (a) Name the products (b) State how many moles of KOH react with one mole of fat (c) Is the soap hard or soft?",
         "steps": ["Each of the three ester bonds is split by one OH<sup>−</sup>.",
                   "(a) <b>Glycerol</b> and <b>potassium palmitate</b>, CH<sub>3</sub>(CH<sub>2</sub>)<sub>14</sub>COO<sup>−</sup>K<sup>+</sup>.",
                   "(b) <b>3 mol</b> of KOH per mole of triglyceride.",
                   "(c) Potassium soaps are <b>soft</b> (liquid soaps); sodium soaps are hard."],
         "notes": "Original example."})
    add({"t": "check", "sec": 5, "lo": LO3, "title": "Quick check",
         "q": "The products of saponifying a fat with NaOH are:",
         "opts": ["glycerol and sodium salts of fatty acids", "glycerol and fatty acids", "fatty alcohols and water", "cholesterol and glycerol"], "ans": 0,
         "why": "Basic hydrolysis gives carboxylate salts (soap).", "notes": "Answer A."})
    add({"t": "check", "sec": 5, "lo": LO3, "title": "Quick check",
         "q": "Why does soap form scum in hard water?",
         "opts": ["Ca<sup>2+</sup> and Mg<sup>2+</sup> form insoluble salts with the fatty acid anions", "Hard water oxidises the soap", "Hard water is acidic", "The soap becomes a wax"], "ans": 0,
         "why": "Calcium and magnesium carboxylates precipitate.", "notes": "Answer A."})

    # ================= 6.6 PHOSPHOLIPIDS =================
    add({"t": "divider", "num": 6, "title": "Phospholipids", "lo": "CH6-LO4", "src": "original (FGOB 23.5 is empty)",
         "blurb": "Lipids with a charged phosphate head: the molecules that make every cell membrane."})
    add({"t": "figure", "pos": "top", "sec": 6, "lo": LO4, "title": "Glycerophospholipids",
         "fig": {"cap": "Phosphatidylcholine (a lecithin): two fatty acid tails, and a phosphate joined to choline as the polar head.",
                 "data": mol_cg(DPPC, 820, 250, highlight=[ESTER])},
         "items": ["Glycerol carries <b>two fatty acids</b> (C1, C2) and a <b>phosphate</b> (C3), which is joined to a small amino alcohol.",
                   "<b>Phosphatidylcholine</b> (lecithin): choline head. <b>Phosphatidylethanolamine</b> (cephalin): ethanolamine head.",
                   "Two nonpolar tails + an ionic head: they are <b>amphipathic</b>, like soaps but with two tails."],
         "notes": "Original (FGOB 23.1 mentions glycerophospholipids; 23.5 empty)."})
    add({"t": "table", "sec": 6, "lo": LO4, "title": "Phospholipids and glycolipids",
         "head": ["Lipid", "Backbone", "Head group", "Where"],
         "rows": [["phosphatidylcholine (lecithin)", "glycerol + 2 fatty acids", "phosphate + choline", "all membranes; egg yolk, soybeans"],
                  ["phosphatidylethanolamine (cephalin)", "glycerol + 2 fatty acids", "phosphate + ethanolamine", "membranes; brain tissue"],
                  ["sphingomyelin", "sphingosine + 1 fatty acid (amide)", "phosphate + choline", "<b>myelin sheath</b> around nerves"],
                  ["cerebrosides, gangliosides (glycolipids)", "sphingosine + 1 fatty acid", "one or more sugars", "brain and nerve cell surfaces; cell recognition"]],
         "widths": [3.2, 2.8, 2.4, 2.6],
         "caption": "<b>Sphingolipids</b> use the amino alcohol <b>sphingosine</b> instead of glycerol; the fatty acid is joined by an <b>amide</b>. In <b>Tay-Sachs disease</b>, a missing enzyme lets gangliosides build up in the brain.",
         "notes": "Original (FGOB 23.1 introduces sphingolipids; 23.5 empty)."})
    add({"t": "bullets", "sec": 6, "lo": LO4, "title": "Phospholipids in pharmacy",
         "items": ["<b>Lecithin</b> (from soy or egg) is an <b>emulsifier</b> in foods, creams and the egg-lecithin emulsion of the anaesthetic <b>propofol</b>.",
                   "<b>Liposomes</b>: hollow phospholipid spheres that carry drugs: liposomal amphotericin B (less kidney toxicity) and liposomal doxorubicin. Some mRNA vaccines use related lipid nanoparticles.",
                   "<b>Lung surfactant</b>: mainly dipalmitoylphosphatidylcholine. Premature babies who lack it are given surfactant into the lungs.",
                   "Phospholipids are also a source of choline and of arachidonic acid for prostaglandins."],
         "notes": "Original pharmacy links."})
    add({"t": "check", "sec": 6, "lo": LO4, "title": "Quick check",
         "q": "How does a phospholipid differ from a triacylglycerol?",
         "opts": ["One fatty acid is replaced by a phosphate with a polar head group", "It has four fatty acids", "It has no glycerol or sphingosine", "It is a steroid"], "ans": 0,
         "why": "Two tails + a charged head makes it amphipathic.", "notes": "Answer A."})

    # ================= 6.7 CELL MEMBRANES =================
    add({"t": "divider", "num": 7, "title": "Cell Membranes", "lo": "CH6-LO4", "src": "FGOB 23.7",
         "blurb": "A double layer of phospholipids, studded with cholesterol and proteins, that decides what enters and leaves every cell."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO4, "title": "Amphipathic lipids in water",
         "fig": {"cap": "Heads face the water; tails hide from it.", "data": lipid_shapes()},
         "items": ["<b>Hydrophilic</b> heads (\"water-loving\") and <b>hydrophobic</b> tails (\"water-fearing\"): molecules with both are <b>amphipathic</b>.",
                   "In water they cluster on their own: <b>micelles</b> (one tail, such as soaps), <b>bilayers</b> (two tails, such as phospholipids) and <b>liposomes</b> (closed bilayers)."],
         "notes": "FGOB 23.7."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO4, "title": "The fluid mosaic model",
         "fig": {"cap": "A phospholipid bilayer with cholesterol, proteins and sugar chains.", "data": membrane()},
         "items": ["Inside the bilayer, tails attract by dispersion forces. Unsaturated tails keep it <b>fluid</b>: lipids and proteins drift sideways.",
                   "<b>Cholesterol</b> sits between the tails and keeps fluidity in a useful range.",
                   "<b>Integral proteins</b> span the bilayer (channels, carriers, receptors); <b>peripheral proteins</b> sit on the surface.",
                   "Sugar chains on the outer surface act as identity tags (blood groups, cell recognition)."],
         "notes": "FGOB 23.7. Fluid mosaic name (Singer and Nicolson, 1972) added."})
    add({"t": "table", "sec": 7, "lo": LO4, "title": "How substances cross the membrane",
         "head": ["Mode", "Energy?", "Direction", "Examples"],
         "rows": [["<b>simple diffusion</b>", "no", "high → low concentration", "O<sub>2</sub>, CO<sub>2</sub>, small nonpolar molecules, many <b>uncharged</b> drugs"],
                  ["<b>facilitated diffusion</b>", "no", "high → low, through a protein", "glucose (GLUT transporters), ions through channels"],
                  ["<b>active transport</b>", "yes (ATP)", "low → high (against the gradient)", "the Na<sup>+</sup>/K<sup>+</sup> pump; uptake of some drugs"]],
         "widths": [2.4, 1.4, 3.0, 4.0],
         "caption": "Passive transport needs no energy; active transport uses ATP. Cells spend most of their energy keeping Na<sup>+</sup> and K<sup>+</sup> unequal. Source: FGOB 23.7.",
         "notes": "FGOB 23.7; GLUT and drug examples original."})
    add({"t": "bullets", "sec": 7, "lo": LO4, "title": "Membranes and drugs",
         "items": ["To be absorbed from the gut, most drugs must <b>dissolve in water</b> and then <b>cross lipid membranes</b>: they need a balance of both.",
                   "<b>Uncharged</b> (unionised) molecules cross the hydrophobic core easily; <b>ions</b> do not. This links to Chapter 4: an amine is absorbed as the free base, not as RNH<sub>3</sub><sup>+</sup>.",
                   "Very fat-soluble drugs (such as the anaesthetic propofol) enter the brain quickly.",
                   "Some antifungals act on membranes: amphotericin B binds ergosterol (the fungal version of cholesterol) and punches holes in fungal membranes."],
         "notes": "Original pharmacy links."})
    add({"t": "check", "sec": 7, "lo": LO4, "title": "Quick check",
         "q": "Which crosses a cell membrane by simple diffusion most easily?",
         "opts": ["a small, uncharged, fat-soluble molecule", "Na<sup>+</sup> ions", "glucose", "a large protein"], "ans": 0,
         "why": "It dissolves in the hydrophobic core. Ions and glucose need proteins.", "notes": "Answer A."})
    add({"t": "check", "sec": 7, "lo": LO4, "title": "Quick check",
         "q": "The Na<sup>+</sup>/K<sup>+</sup> pump moves ions against their concentration gradients. This is:",
         "opts": ["active transport", "simple diffusion", "facilitated diffusion", "osmosis"], "ans": 0,
         "why": "It uses energy from ATP.", "notes": "Answer A."})

    # ================= 6.8 STEROIDS =================
    add({"t": "divider", "num": 8, "title": "Steroids", "lo": "CH6-LO5", "src": "FGOB 23.6",
         "blurb": "Four fused rings and no fatty acids: cholesterol, the hormones made from it, bile salts and a whole shelf of medicines."})
    add({"t": "figure", "pos": "leftwide", "sec": 8, "lo": LO5, "title": "The steroid nucleus",
         "fig": {"cap": "Rings A, B and C are six-membered; ring D is five-membered.", "data": steroid_rings()},
         "items": ["All steroids share <b>four fused rings</b> (A, B, C, D).",
                   "Small changes to the groups on the rings give very different biological effects.",
                   "Steroids are lipids (insoluble in water) but are <b>nonsaponifiable</b>: no ester bonds for NaOH to split.",
                   "Found in plants, animals and fungi, but not in bacteria."],
         "notes": "FGOB 23.6."})
    add({"t": "figure", "pos": "top", "sec": 8, "lo": LO5, "title": "Cholesterol",
         "fig": {"cap": "Cholesterol: the steroid nucleus with an –OH on ring A, a C=C in ring B and a hydrocarbon tail.",
                 "data": mol(CHOLESTEROL, 600, 260)},
         "items": ["The most abundant steroid in the body (about 240 g). Not found in plants. About half is in <b>cell membranes</b>.",
                   "The starting material for <b>bile acids</b>, <b>steroid hormones</b> and <b>vitamin D</b>.",
                   "The liver makes about 1 g a day; we also eat it in animal foods. Cholesterol can precipitate in the gallbladder as <b>gallstones</b> (Greek <i>chole</i>, bile + <i>stereos</i>, solid)."],
         "notes": "FGOB 23.6."})
    add({"t": "two", "sec": 8, "lo": LO5, "title": "Cholesterol, lipoproteins and heart disease",
         "lead": "Cholesterol is insoluble in blood, so it travels inside protein–lipid particles called <b>lipoproteins</b>.",
         "cols": [{"h": "LDL: \"bad\" cholesterol", "tone": "cold", "items": [
             "<b>Low-density</b> lipoprotein: more lipid, less protein",
             "Carries cholesterol <b>to</b> tissues",
             "High LDL increases the risk of <b>atherosclerosis</b> (fatty plaques in arteries)"]},
             {"h": "HDL: \"good\" cholesterol", "tone": "heat", "items": [
                 "<b>High-density</b> lipoprotein: more protein",
                 "Carries excess cholesterol <b>back to the liver</b>",
                 "High HDL lowers risk; the LDL:HDL ratio predicts risk better than total cholesterol"]}],
         "notes": "FGOB 23.6 (To Your Health). Statins: next slide."})
    add({"t": "bullets", "sec": 8, "lo": LO5, "title": "Lowering cholesterol",
         "items": ["Diet: replace saturated fat with unsaturated fat; cut trans fats; exercise improves the LDL:HDL ratio (FGOB 23.6).",
                   "<b>Statins</b> (simvastatin, atorvastatin) block <b>HMG-CoA reductase</b>, a key enzyme the liver uses to make cholesterol. LDL falls.",
                   "<b>Ezetimibe</b> blocks cholesterol absorption in the gut.",
                   "<b>Bile acid sequestrants</b> (cholestyramine) bind bile acids in the gut, so the liver uses more cholesterol to make new ones."],
         "notes": "Diet: FGOB 23.6. Drugs original."})
    add({"t": "figure", "pos": "top", "sec": 8, "lo": LO5, "title": "Steroid hormones",
         "fig": {"cap": "All made from cholesterol. Note how few changes separate them.",
                 "data": row([(mol(CORTISOL, 260, 170), "cortisol"), (mol(TESTOSTERONE, 240, 170), "testosterone"), (mol(ESTRADIOL, 240, 170), "estradiol"), (mol(PROGESTERONE, 250, 170), "progesterone")], w=250, h=170)},
         "items": ["<b>Adrenocortical hormones</b>: <b>cortisol</b> (raises blood glucose, suppresses inflammation) and <b>aldosterone</b> (makes the kidneys keep Na<sup>+</sup> and water).",
                   "<b>Sex hormones</b>: androgens (testosterone), estrogens (estradiol) and progesterone (prepares the uterus and maintains pregnancy).",
                   "Both sexes make androgens and estrogens, in different amounts."],
         "notes": "FGOB 23.6 table."})
    add({"t": "table", "sec": 8, "lo": LO5, "title": "Steroid medicines",
         "head": ["Group", "Examples", "Used for"],
         "rows": [["<b>corticosteroids</b> (cortisol analogues)", "hydrocortisone cream, prednisolone, dexamethasone, beclomethasone and budesonide inhalers", "inflammation, asthma, eczema, autoimmune disease, after transplants"],
                  ["<b>estrogens and progestins</b>", "ethinylestradiol + levonorgestrel", "oral contraceptives (prevent ovulation); hormone replacement"],
                  ["<b>androgens</b>", "testosterone", "hormone replacement (misused as anabolic steroids in sport)"],
                  ["<b>cardiac glycosides</b>", "digoxin", "heart failure, atrial fibrillation (a steroid joined to sugars: Chapter 5)"],
                  ["<b>vitamin D</b>", "cholecalciferol, calcitriol", "made from cholesterol in skin with UV light; bone health"]],
         "widths": [2.8, 4.0, 3.6],
         "caption": "Long-term oral corticosteroids have serious side effects (raised blood glucose, weak bones, infections), which follow from cortisol's normal actions. Source: FGOB 23.6 (uses of cortisol analogues and oral contraceptives); other rows original.",
         "notes": "FGOB 23.6 plus original pharmacy table."})
    add({"t": "figure", "pos": "top", "sec": 8, "lo": LO5, "title": "Bile salts: the body's emulsifiers",
         "fig": {"cap": "Cholic acid: three –OH groups on one face, a –COOH on the side chain.", "data": mol(CHOLIC, 560, 230)},
         "items": ["The liver makes <b>bile acids</b> such as cholic acid from cholesterol, joins them to glycine or taurine (an amide), and stores them in the gallbladder as sodium salts.",
                   "They are <b>amphipathic</b>: one polar face, one nonpolar face. They break fat into tiny droplets (emulsify), so lipase can work.",
                   "Ursodeoxycholic acid, a bile acid, is used to dissolve some cholesterol gallstones."],
         "notes": "FGOB 23.6 (bile salts); ursodeoxycholic acid original."})
    add({"t": "check", "sec": 8, "lo": LO5, "title": "Quick check",
         "q": "Which lipid is NOT saponifiable?",
         "opts": ["cholesterol", "tristearin", "beeswax", "lecithin"], "ans": 0,
         "why": "Steroids have no ester bonds for NaOH to split.", "notes": "Answer A."})
    add({"t": "check", "sec": 8, "lo": LO5, "title": "Quick check",
         "q": "Statins lower blood cholesterol by:",
         "opts": ["inhibiting HMG-CoA reductase in the liver", "binding bile acids", "blocking lipase", "dissolving gallstones"], "ans": 0,
         "why": "Less cholesterol is made, so LDL falls.", "notes": "Answer A."})

    # ================= wrap-up =================
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Lipids", "defined by solubility; 9 kcal/g; saponifiable (esters) vs nonsaponifiable (steroids)"],
        ["Fatty acids", "C12–C20, even, unbranched; cis C=C → kink → lower mp; ω-3, ω-6; essential: linoleic, α-linolenic"],
        ["Waxes", "long-chain acid + long-chain alcohol ester; carnauba, beeswax, lanolin"],
        ["Triacylglycerols", "glycerol + 3 fatty acids; fats (saturated, solid) vs oils (unsaturated, liquid)"],
        ["Reactions", "hydrogenation (margarine, trans fats); rancidity (oxidation, hydrolysis); iodine value"],
        ["Hydrolysis", "lipase → glycerol + fatty acids; NaOH → glycerol + soap; micelles clean grease"],
        ["Membranes", "phospholipid bilayer + cholesterol + proteins; diffusion, facilitated, active transport"],
        ["Steroids", "4 fused rings; cholesterol → hormones, bile salts, vitamin D; corticosteroid drugs, statins"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 30 min)", "Attempt the Chapter 6 tutorial",
                   "Play the Chapter 6 game to find your weak outcomes", "Next chapter: Amino Acids, Proteins and Enzymes"],
         "attrib": "Adapted from LibreTexts (FGOB, remixed from Ball, Hill &amp; Scott), CC BY-NC-SA 3.0, with original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"]})
    return S
