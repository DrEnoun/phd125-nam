"""PHD125 Chapter 5 · Carbohydrates · lecture slide content.
Sources: Ball, Hill & Scott, The Basics of GOB Chemistry, chapter 16 (16.1-16.7), and FGOB 20.3-20.7,
LibreTexts, CC BY-NC-SA 3.0.
Original material by Dr. NAM (FGOB 14.10, 20.1 and 20.2 are empty placeholders): chirality in depth (the 2^n rule,
racemic mixtures, chiral drugs), pyranose and furanose, the reactions of monosaccharides beyond the Benedict's test
(sugar alcohols, glycosides, phosphate esters, amino sugars), and the pharmacy links (excipients, glucose meters,
mannitol, digoxin, heparin, dextran). Fischer and Haworth projections are drawn by _src/sugars.py."""
from figs import mol, row, scheme, stack
from sugars import (fischer, fischer_row, haworth, haworth_row, disaccharide, sucrose, GLC, GAL, FRU, RIB,
                    D_GLUCOSE, D_GALACTOSE, D_FRUCTOSE, D_RIBOSE, L_GLUCOSE, D_GLYC, L_GLYC)

LO1, LO2, LO3, LO4, LO5 = 'CH5-LO1', 'CH5-LO2', 'CH5-LO3', 'CH5-LO4', 'CH5-LO5'

META = {
    "code": "CH5", "chapter": "Chapter 5", "title": "Carbohydrates", "short": "Carbohydrates",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: Ball, Hill & Scott, The Basics of GOB Chemistry, chapter 16, with FGOB 20.3–20.7",
    "attrib": ("Adapted from <i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 16, and <i>Fundamentals of General Organic and "
               "Biological Chemistry</i> 20.3–20.7, LibreTexts, CC BY-NC-SA 3.0. Chirality in depth, pyranose and furanose rings, sugar alcohols, "
               "glycosides and the pharmacy links are original material by Dr. NAM. Fischer and Haworth projections drawn by Dr. NAM; other structures drawn with RDKit. "
               "Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["glyceraldehyde", "glucose", "water"], "2": ["glucose", "fructose", "glyceraldehyde"], "3": ["glucose", "fructose", "ethanol"],
               "4": ["glucose", "sorbitol", "glycerol"], "5": ["glucose", "fructose", "water"], "6": ["glucose", "glycerol", "water"]},
    "titlemol": ["glucose", "fructose", "glyceraldehyde", "sorbitol"], "darkmol": "glucose",
    "next": "Next chapter: Lipids",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Classify carbohydrates, identify chiral carbons and enantiomers, and explain why chirality matters for drugs"],
    [LO2, "Classify monosaccharides, draw Fischer projections, and assign them as D or L"],
    [LO3, "Draw the cyclic (Haworth) forms of monosaccharides, identify α and β anomers, and explain mutarotation"],
    [LO4, "Describe the reactions of monosaccharides: oxidation (reducing sugars), reduction to sugar alcohols, and glycoside formation"],
    [LO5, "Describe the units, glycosidic linkages and properties of the common disaccharides and polysaccharides"],
]

GLU_OPEN = 'O=C[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO'


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Carbohydrates", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 5",
         "notes": "Chapter 5 of the course outline, in six subchapters following the lesson plan: introduction (with chirality), monosaccharides, cyclic forms, reactions, disaccharides, polysaccharides."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1: 5.1. LO2: 5.2. LO3: 5.3. LO4: 5.4. LO5: 5.5–5.6."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>5.1 Introduction</b> (Ball 16.1–16.2): what carbohydrates are, and <b>chirality in depth</b> (from the Chapter 2 preview)",
        "<b>5.2 Monosaccharides</b> (Ball 16.2–16.3; FGOB 20.4): aldoses and ketoses, Fischer projections, D and L, glucose, galactose, fructose",
        "<b>5.3 Cyclic forms</b> (Ball 16.4; FGOB 20.3): hemiacetal rings, Haworth projections, α and β anomers, mutarotation",
        "<b>5.4 Reactions of monosaccharides</b> (Ball 16.5): reducing sugars, sugar alcohols, glycosides",
        "<b>5.5 Disaccharides</b> (Ball 16.6; FGOB 20.6): maltose, lactose, sucrose",
        "<b>5.6 Polysaccharides</b> (Ball 16.7; FGOB 20.7): starch, glycogen, cellulose"],
         "notes": "Ties back to Chapter 3 (aldehydes, ketones, hemiacetals) and Chapter 2 (chirality)."})
    add({"t": "hook", "title": "Think first",
         "q": "Rice, a cotton shirt, the filler in a paracetamol tablet and the sugar in your teh tarik are all made of the same building block. What is it, and why can you digest only some of them?",
         "a": "All are made from <b>glucose</b>. Starch (rice) links glucose with <b>α</b> bonds that our enzymes can break; cellulose (cotton, many tablet fillers) uses <b>β</b> bonds that we cannot. One small change in 3D shape decides whether a carbohydrate is food or fibre. Sucrose is glucose joined to fructose.",
         "notes": "Pairs discuss for one minute. Teh tarik: sweetened condensed milk contains sucrose and lactose."})

    # ================= 5.1 INTRODUCTION & CHIRALITY =================
    add({"t": "divider", "num": 1, "title": "Introduction", "lo": "CH5-LO1", "src": "Ball 16.1–16.2",
         "blurb": "What carbohydrates are, how plants make them, and why their 3D shape (chirality) matters so much in the body and in drugs."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "What is a carbohydrate?",
         "items": ["Carbohydrates are <b>polyhydroxy aldehydes or ketones</b>, or compounds that can be hydrolysed to them. They contain only C, H and O.",
                   "The name comes from \"carbon hydrate\": glucose, C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>, looks like C<sub>6</sub>(H<sub>2</sub>O)<sub>6</sub>. (It contains no water molecules.)",
                   "Plants make them by <b>photosynthesis</b>: 6 CO<sub>2</sub> + 6 H<sub>2</sub>O + 686 kcal (sunlight) → C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub>.",
                   "Uses: energy (food), structure (cellulose in plants), parts of nucleic acids, proteins and lipids; cotton, paper and wood. They are about 60–65% of the average diet."],
         "notes": "Ball 16.1."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Classifying carbohydrates by size",
         "fig": {"cap": "All higher saccharides can be hydrolysed back to monosaccharides.",
                 "data": row([(haworth(GLC('b')), "monosaccharide: glucose"), (disaccharide(GLC('a'), GLC('a'), 'a'), "disaccharide: maltose (glucose + glucose)")], w=380, h=230)},
         "items": ["<b>Monosaccharides</b>: one sugar unit; cannot be hydrolysed further (glucose, fructose, galactose).",
                   "<b>Disaccharides</b>: two units (maltose, lactose, sucrose). <b>Oligosaccharides</b>: a few units.",
                   "<b>Polysaccharides</b>: hundreds to thousands of units (starch, glycogen, cellulose).",
                   "Names ending in <b>-ose</b> are sugars."],
         "notes": "Ball 16.1. Oligosaccharide added."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Chirality: hands that do not match",
         "fig": {"cap": "The two forms of 2-butanol (Chapter 2): mirror images that cannot be placed on top of each other.",
                 "data": row([(mol("C[C@@H](O)CC", 220, 150), "one enantiomer"), (mol("C[C@H](O)CC", 220, 150), "its mirror image")], w=260, h=150)},
         "items": ["A <b>chiral carbon</b> (stereocentre) is bonded to <b>four different groups</b>. Chapter 2 introduced it; here we go further.",
                   "A molecule with one chiral carbon exists as two <b>enantiomers</b>: non-superimposable mirror images, like left and right hands.",
                   "Enantiomers are <b>stereoisomers</b>: same atoms, same bonds, different 3D arrangement (cis-trans isomers are another kind).",
                   "Wedge = towards you; dashes = away from you."],
         "notes": "Ball 16.2. Builds on Ch2 slide 36."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Spotting chiral carbons",
         "head": ["Compound", "Carbon checked", "Its four groups", "Chiral?"],
         "rows": [["glyceraldehyde, HOCH<sub>2</sub>CH(OH)CHO", "C2", "H, OH, CHO, CH<sub>2</sub>OH", "<b>yes</b>"],
                  ["dihydroxyacetone, HOCH<sub>2</sub>COCH<sub>2</sub>OH", "C2", "C=O (no H), two identical CH<sub>2</sub>OH", "no"],
                  ["2-propanol, CH<sub>3</sub>CH(OH)CH<sub>3</sub>", "C2", "H, OH, CH<sub>3</sub>, CH<sub>3</sub>", "no (two CH<sub>3</sub>)"],
                  ["lactic acid, CH<sub>3</sub>CH(OH)COOH", "C2", "H, OH, CH<sub>3</sub>, COOH", "<b>yes</b>"],
                  ["glucose (open chain)", "C2, C3, C4, C5", "each has four different groups", "<b>4 chiral carbons</b>"]],
         "widths": [3.8, 1.8, 3.4, 1.6],
         "caption": "Quick rules: a CH<sub>2</sub>, CH<sub>3</sub> or C=O carbon can never be chiral. Look for carbons with one H and three different other groups.",
         "notes": "Glyceraldehyde and dihydroxyacetone: Ball 16.2. Others original."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "How many stereoisomers?",
         "items": ["A molecule with <b>n</b> chiral carbons can have up to <b>2<sup>n</sup></b> stereoisomers.",
                   "Glyceraldehyde: 1 chiral carbon → 2<sup>1</sup> = <b>2</b> (D and L). An aldotetrose: 2 → <b>4</b>.",
                   "An <b>aldohexose</b> (glucose): 4 chiral carbons → 2<sup>4</sup> = <b>16</b> stereoisomers: 8 D-sugars and 8 L-sugars. Glucose, galactose and mannose are three of them.",
                   "Each stereoisomer has a different shape, so a different name and different biological behaviour."],
         "notes": "Original (2^n rule)."})
    add({"t": "two", "sec": 1, "lo": LO1, "title": "Optical activity",
         "lead": "Enantiomers have the <b>same</b> melting point, boiling point and solubility. They differ in one physical property: how they rotate <b>plane-polarised light</b>.",
         "cols": [{"h": "Measuring it", "tone": "cold", "items": [
             "A <b>polarimeter</b> passes plane-polarised light through a solution",
             "<b>Dextrorotatory (+)</b>: rotates the plane clockwise (right)",
             "<b>Levorotatory (−)</b>: anticlockwise (left)",
             "Enantiomers rotate by the same amount, in opposite directions: glyceraldehyde +8.7° and −8.7°"]},
             {"h": "Names that come from it", "tone": "heat", "items": [
                 "Glucose is also called <b>dextrose</b> (+); fructose is <b>levulose</b> (−92.4°)",
                 "A <b>racemic mixture</b> (racemate) is 50:50: the rotations cancel, so it is optically inactive",
                 "D and L (next subchapter) describe <b>structure</b>; + and − describe the <b>measured rotation</b>. They are not linked"]}],
         "notes": "Ball 16.2 (Looking Closer: polarized light), 16.3. Racemic mixture and the D/L vs +/− warning are original."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Why pharmacists care: chiral drugs",
         "head": ["Drug", "What the enantiomers do"],
         "rows": [["<b>thalidomide</b>", "one enantiomer sedates; the other causes birth defects. They interconvert in the body, so even the \"safe\" one is not safe (Chapter 2)"],
                  ["<b>ibuprofen</b>", "the S form relieves pain; the body converts much of the R form to S. Sold as the racemate, and as dexibuprofen (S only)"],
                  ["<b>omeprazole → esomeprazole</b>", "esomeprazole is the single S enantiomer (\"es-\" = S)"],
                  ["<b>cetirizine → levocetirizine</b>", "levocetirizine is the active R enantiomer: half the dose for the same effect"],
                  ["<b>salbutamol → levosalbutamol</b>", "the R enantiomer relaxes the airways"],
                  ["<b>levodopa</b> (L-DOPA)", "only the L form is used for Parkinson's disease"]],
         "widths": [3.0, 7.0],
         "caption": "Receptors and enzymes are themselves chiral (made of L-amino acids), so they fit one enantiomer like a right glove fits a right hand. Prefixes such as <b>lev-</b>, <b>dex-</b> and <b>es-</b> in drug names signal a single enantiomer.",
         "notes": "Original pharmacy examples. R/S naming is beyond this course; it is mentioned only to explain drug names."})
    add({"t": "check", "sec": 1, "lo": LO1, "title": "Quick check",
         "q": "How many chiral carbons are in CH<sub>3</sub>CH(OH)CH(NH<sub>2</sub>)CH<sub>3</sub>?",
         "opts": ["0", "1", "2", "3"], "ans": 2,
         "why": "C2 (H, OH, CH<sub>3</sub>, rest of chain) and C3 (H, NH<sub>2</sub>, CH<sub>3</sub>, rest of chain). The two end CH<sub>3</sub> carbons are not chiral.", "notes": "Answer C."})
    add({"t": "check", "sec": 1, "lo": LO1, "title": "Quick check",
         "q": "A 50:50 mixture of two enantiomers is placed in a polarimeter. What is observed?",
         "opts": ["No rotation: the mixture is racemic", "Rotation to the right", "Rotation to the left", "Twice the rotation of one enantiomer"], "ans": 0,
         "why": "Equal and opposite rotations cancel.", "notes": "Answer A."})

    # ================= 5.2 MONOSACCHARIDES =================
    add({"t": "divider", "num": 2, "title": "Monosaccharides", "lo": "CH5-LO2", "src": "Ball 16.2–16.3 · FGOB 20.4",
         "blurb": "Aldoses and ketoses, how to draw sugars as Fischer projections, and how to tell a D sugar from an L sugar."})
    add({"t": "table", "sec": 2, "lo": LO2, "title": "Classifying monosaccharides",
         "head": ["By the carbonyl group", "By the number of carbons", "Put together"],
         "rows": [["<b>aldose</b>: an aldehyde (C1)", "<b>triose</b> 3 C, <b>tetrose</b> 4 C", "glyceraldehyde: an aldotriose"],
                  ["<b>ketose</b>: a ketone (usually C2)", "<b>pentose</b> 5 C, <b>hexose</b> 6 C", "ribose: an aldopentose"],
                  ["", "natural sugars have 3–7 carbons", "glucose: an <b>aldohexose</b>; fructose: a <b>ketohexose</b>"]],
         "widths": [3.2, 3.2, 3.6],
         "caption": "Every other carbon carries an –OH. Monosaccharides are crystalline solids that dissolve well in water (many –OH groups to hydrogen bond). Source: Ball 16.2, 16.5.",
         "notes": "Ball 16.2."})
    add({"t": "figure", "pos": "leftwide", "sec": 2, "lo": LO2, "title": "Fischer projections",
         "fig": {"cap": "D-glucose drawn as a Fischer projection.", "data": fischer(*D_GLUCOSE)},
         "items": ["The carbon chain is drawn <b>vertically</b>, with the carbonyl group at the <b>top</b> (C1 for aldoses).",
                   "Each cross is a chiral carbon. <b>Horizontal</b> bonds point <b>towards</b> you; <b>vertical</b> bonds point <b>away</b>.",
                   "H and OH are written to the left or right. Glucose: all OH on the right except C3.",
                   "Fischer projections may be turned 180° in the page, but not flipped over or turned 90°."],
         "notes": "Ball 16.2; FGOB 20.4. The rotation rule is original."})
    add({"t": "figure", "pos": "leftwide", "sec": 2, "lo": LO2, "title": "D and L sugars",
         "fig": {"cap": "The reference compounds: D- and L-glyceraldehyde.", "data": fischer_row([D_GLYC + ('D-glyceraldehyde', 0), L_GLYC + ('L-glyceraldehyde', 0)])},
         "items": ["Look at the <b>chiral carbon furthest from the carbonyl</b> (the penultimate carbon, next to the bottom CH<sub>2</sub>OH).",
                   "–OH on the <b>right</b> → <b>D</b> sugar. –OH on the <b>left</b> → <b>L</b> sugar.",
                   "Almost all natural sugars are <b>D</b>. (Most natural amino acids are L: Chapter 7.)",
                   "D-glucose and L-glucose are enantiomers: every OH is on the opposite side."],
         "notes": "Ball 16.2."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO2, "title": "Three important hexoses (and a pentose)",
         "fig": {"cap": "The shaded row decides D or L. Glucose and galactose differ only at C4; fructose matches glucose from C3 to C6.",
                 "data": fischer_row([D_GLUCOSE + ('D-glucose', 3), D_GALACTOSE + ('D-galactose', 3), D_FRUCTOSE + ('D-fructose', 3), D_RIBOSE + ('D-ribose', 2)])},
         "items": ["Glucose and galactose are <b>aldohexoses</b>; fructose is a <b>ketohexose</b> (C=O at C2); ribose is an <b>aldopentose</b> (in RNA and ATP)."],
         "notes": "Ball 16.3; FGOB 20.4. Ribose added."})
    add({"t": "table", "sec": 2, "lo": LO2, "title": "Glucose, galactose, fructose",
         "head": ["Sugar", "Also called", "Where you meet it"],
         "rows": [["<b>D-glucose</b>", "dextrose, blood sugar, corn sugar", "the most abundant sugar; fuel for every cell. Normal blood level 70–105 mg/dL. IV dextrose 5% (D5W) drips"],
                  ["<b>D-galactose</b>", "\"brain sugar\"", "not free in nature; comes from lactose (milk). Part of glycolipids in the brain and nerve myelin"],
                  ["<b>D-fructose</b>", "levulose, fruit sugar", "honey (~40%) and fruit. The sweetest sugar: 1.7 times sweeter than sucrose"]],
         "widths": [2.0, 3.0, 5.4],
         "caption": "Source: Ball 16.3; FGOB 20.4. IV dextrose added.",
         "notes": "Ball 16.3."})
    add({"t": "tryit", "sec": 2, "lo": LO2, "title": "Try it · Classify and assign",
         "q": "For D-ribose (CHO at the top, three H–C–OH rows, CH<sub>2</sub>OH at the bottom): (a) classify it by carbonyl group and size (b) how many chiral carbons does it have, and how many stereoisomers are possible? (c) draw its enantiomer and name it",
         "a": "(a) <b>aldopentose</b> (b) <b>3</b> chiral carbons (C2, C3, C4) → 2<sup>3</sup> = <b>8</b> stereoisomers (c) <b>L-ribose</b>: every OH moves to the left side.",
         "afig": {"data": fischer_row([D_RIBOSE + ('D-ribose', 2), ('CHO', [('HO', 'H'), ('HO', 'H'), ('HO', 'H')], 'CH₂OH', 'L-ribose', 2)])},
         "notes": "Original, applying Ball 16.2."})
    add({"t": "check", "sec": 2, "lo": LO2, "title": "Quick check",
         "q": "In a Fischer projection, the OH on the chiral carbon furthest from the C=O is on the left. The sugar is:",
         "opts": ["an L sugar", "a D sugar", "dextrorotatory", "a ketose"], "ans": 0,
         "why": "Left = L. Whether it rotates light to the left must be measured.", "notes": "Answer A."})
    add({"t": "check", "sec": 2, "lo": LO2, "title": "Quick check",
         "q": "Fructose is best described as a:",
         "opts": ["ketohexose", "aldohexose", "ketopentose", "aldopentose"], "ans": 0,
         "why": "Six carbons, ketone at C2.", "notes": "Answer A."})

    # ================= 5.3 CYCLIC FORMS =================
    add({"t": "divider", "num": 3, "title": "Cyclic Forms of Monosaccharides", "lo": "CH5-LO3", "src": "Ball 16.4 · FGOB 20.3",
         "blurb": "In water, sugars curl up into rings. The ring can close two ways, α and β, and the two keep swapping."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO3, "title": "Rings form from a hemiacetal",
         "fig": {"cap": "The C5–OH of glucose adds to its own C1=O (Chapter 3: aldehyde + alcohol → hemiacetal).",
                 "data": scheme([('m', GLU_OPEN, 'D-glucose (open chain)', 280), ('>', 'C5–OH adds to C1=O', ''), ('m', 'OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O', 'β-D-glucose (ring)', 240)], h=160)},
         "items": ["Sugars with 5 or more carbons form rings in water, because <b>5- and 6-membered rings</b> are the most stable.",
                   "Glucose: C5–OH + C1 aldehyde → a <b>six-membered ring</b> (5 C + 1 O), called a <b>pyranose</b>.",
                   "Fructose: C5–OH + C2 ketone → a <b>five-membered ring</b> (4 C + 1 O), a <b>furanose</b>.",
                   "C1 (C2 in fructose) becomes the <b>anomeric carbon</b>: a new chiral carbon carrying a new –OH."],
         "notes": "FGOB 20.3; pyranose/furanose names original."})
    add({"t": "figure", "pos": "leftwide", "sec": 3, "lo": LO3, "title": "Haworth projections",
         "fig": {"cap": "Fischer (left) to Haworth (right): right → down, left → up.",
                 "data": row([(fischer(*D_GLUCOSE, nums=True), "D-glucose (Fischer)"), (haworth(GLC('b')), "β-D-glucose (Haworth)")], w=260, h=320)},
         "items": ["Draw the ring as a flat hexagon seen edge-on: thick bonds are <b>nearest you</b>; the ring O is at the back right.",
                   "Groups on the <b>right</b> in the Fischer projection go <b>down</b>; groups on the <b>left</b> go <b>up</b>.",
                   "In D sugars, the CH<sub>2</sub>OH (C6) points <b>up</b>.",
                   "H atoms are usually left off for clarity."],
         "notes": "FGOB 20.3 (Haworth rules)."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO3, "title": "Anomers: α and β",
         "fig": {"cap": "The only difference is the –OH on the anomeric carbon (C1).",
                 "data": haworth_row([(GLC('a'), 'pyr', 'α-D-glucose: C1–OH down'), (GLC('b'), 'pyr', 'β-D-glucose: C1–OH up')], w=300)},
         "items": ["When the ring closes, the new –OH on C1 can point <b>down</b> (<b>α</b>) or <b>up</b> (<b>β</b>), relative to CH<sub>2</sub>OH up.",
                   "α and β forms are stereoisomers called <b>anomers</b>. They have different properties: α-glucose melts at 146 °C (+112°), β at 150 °C (+18.7°).",
                   "The difference matters: starch is built from α-glucose (we digest it); cellulose from β-glucose (we cannot)."],
         "notes": "FGOB 20.3; Ball 16.4."})
    add({"t": "bullets", "sec": 3, "lo": LO3, "title": "Mutarotation",
         "items": ["Dissolve pure α-glucose (or pure β) in water: the rings <b>open and close</b> again and again, so the rotation changes until it settles.",
                   "At equilibrium: about <b>36% α</b>, <b>64% β</b> and less than <b>0.02%</b> open chain. Rotation settles at <b>+52.7°</b>.",
                   "This change in optical rotation is <b>mutarotation</b> (Latin <i>mutare</i>, to change).",
                   "The tiny open-chain fraction still reacts like an aldehyde: as it is used up, more rings open (Le Chatelier). This is why glucose is a reducing sugar (5.4)."],
         "side": {"h": "Why more β?", "body": "In β-glucose every bulky group (–OH and –CH<sub>2</sub>OH) can sit in the roomier positions of the ring, so it is slightly more stable."},
         "notes": "FGOB 20.3; Ball 16.4. Side box original."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO3, "title": "Other rings: galactose, fructose, ribose",
         "fig": {"cap": "Galactose differs from glucose only at C4 (OH up). Fructose and ribose form five-membered (furanose) rings.",
                 "data": haworth_row([(GAL('b'), 'pyr', 'β-D-galactose'), (FRU('b'), 'fur', 'β-D-fructose'), (RIB('b'), 'fur', 'β-D-ribose')], w=270)},
         "items": ["In fructose the anomeric carbon is <b>C2</b>, which carries both the anomeric –OH and C1 (a CH<sub>2</sub>OH).",
                   "β-D-Ribose (and 2-deoxyribose, with no –OH on C2) are the sugars in RNA and DNA (Beyond the syllabus: Nucleic Acids)."],
         "notes": "Ball 16.4 (Figure 2b for fructose); ribose original."})
    add({"t": "tryit", "sec": 3, "lo": LO3, "title": "Try it · From Fischer to Haworth",
         "q": "D-Mannose differs from D-glucose only at C2 (its C2–OH is on the left). (a) In the Haworth form of β-D-mannose, does the C2–OH point up or down? (b) Where does the C1–OH point? (c) Is mannose an epimer or an anomer of glucose?",
         "a": "(a) <b>Up</b> (left in Fischer → up in Haworth) (b) <b>Up</b>: it is the β anomer (c) An <b>epimer</b>: sugars that differ at one chiral carbon other than the anomeric carbon are epimers. Anomers differ only at the anomeric carbon.",
         "afig": {"data": haworth([('OH', 'H'), ('OH', 'H'), ('OH', 'H'), ('H', 'OH'), ('CH₂OH', 'H')], caption='β-D-mannose')},
         "notes": "Original. Epimer is an extra term; galactose is the C4 epimer of glucose."})
    add({"t": "check", "sec": 3, "lo": LO3, "title": "Quick check",
         "q": "In the Haworth projection of a D-aldohexose, the –OH on C1 points down. This is the:",
         "opts": ["α anomer", "β anomer", "L sugar", "open-chain form"], "ans": 0,
         "why": "C1–OH down (opposite the CH<sub>2</sub>OH) = α.", "notes": "Answer A."})
    add({"t": "check", "sec": 3, "lo": LO3, "title": "Quick check",
         "q": "Why does a fresh solution of pure α-glucose slowly change its optical rotation?",
         "opts": ["The ring opens and recloses, forming an α/β mixture (mutarotation)", "Glucose is oxidised by air", "Glucose turns into fructose", "The solution evaporates"], "ans": 0,
         "why": "Equilibrium: about 36% α, 64% β, +52.7°.", "notes": "Answer A."})

    # ================= 5.4 REACTIONS =================
    add({"t": "divider", "num": 4, "title": "Reactions of Monosaccharides", "lo": "CH5-LO4", "src": "Ball 16.5 · FGOB 20.5",
         "blurb": "A sugar is an aldehyde (or ketone) and an alcohol at once: it can be oxidised, reduced and joined to other molecules."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO4, "title": "Oxidation: reducing sugars",
         "fig": {"cap": "The aldehyde of open-chain glucose is oxidised to a carboxylic acid (gluconic acid); Cu<sup>2+</sup> is reduced to Cu<sub>2</sub>O.",
                 "data": scheme([('m', GLU_OPEN, 'D-glucose', 270), ('>', "Benedict's (Cu²⁺, blue)", 'brick-red Cu₂O'), ('m', 'OC(=O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO', 'gluconic acid', 280)], h=150)},
         "items": ["A <b>reducing sugar</b> reduces a mild oxidising agent (Tollens', Benedict's) without first being hydrolysed. <b>All monosaccharides</b> are reducing sugars.",
                   "Benedict's test: <b>blue</b> Cu<sup>2+</sup> → <b>brick-red</b> Cu<sub>2</sub>O precipitate. Tollens': silver mirror.",
                   "Fructose (a ketose) also gives a positive test: in the basic reagent it rearranges to an aldose form (tautomerism)."],
         "notes": "Ball 16.5."})
    add({"t": "bullets", "sec": 4, "lo": LO4, "title": "Testing for glucose: then and now",
         "items": ["<b>Clinitest</b> tablets for urine sugar contain Cu<sup>2+</sup> (Benedict's chemistry): green = very little sugar; brick-red = more than 2 g/100 mL (Ball 16.5).",
                   "Benedict's reacts with <b>any</b> reducing sugar, so lactose or galactose also give a positive result.",
                   "Modern <b>glucometer strips</b> use the enzyme <b>glucose oxidase</b>, which oxidises only glucose (to gluconic acid and H<sub>2</sub>O<sub>2</sub>); the strip turns this into an electric signal.",
                   "Normal fasting blood glucose is about 70–105 mg/dL (3.9–5.8 mmol/L)."],
         "notes": "Ball 16.5 (Clinitest); FGOB 20.4 (range). Glucose oxidase and mmol/L conversion are original."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO4, "title": "Reduction: sugar alcohols",
         "fig": {"cap": "Reducing the C=O of glucose gives sorbitol (glucitol), a polyalcohol.",
                 "data": scheme([('m', GLU_OPEN, 'D-glucose', 270), ('>', 'H₂, Ni (or NaBH₄)', ''), ('m', 'OC[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO', 'sorbitol', 270)], h=150)},
         "items": ["Aldehyde → 1° alcohol, exactly as in Chapter 3. The products are <b>sugar alcohols</b> (alditols): names end in <b>-itol</b>.",
                   "<b>Sorbitol</b>: sweetener in sugar-free syrups and lozenges; large amounts are laxative.",
                   "<b>Mannitol</b> (from mannose): an IV <b>osmotic diuretic</b> to reduce pressure in the brain; also a tablet filler.",
                   "<b>Xylitol</b>: sugar-free gum; bacteria in the mouth cannot ferment it, so it does not cause tooth decay."],
         "notes": "Original (Ball 16.5 does not cover reduction)."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO4, "title": "Glycosides: locking the ring",
         "fig": {"cap": "The anomeric –OH reacts with an alcohol (acid catalyst) to form a glycoside (an acetal).",
                 "data": scheme([('m', 'OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O', 'α-D-glucose', 220), ('+',), ('t', 'CH₃OH', 80), ('>', 'H⁺', '− H₂O'), ('m', 'CO[C@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O', 'methyl α-D-glucoside', 240)], h=150)},
         "items": ["The C–O–C bond from the anomeric carbon is a <b>glycosidic bond</b>. It joins sugars into di- and polysaccharides (5.5–5.6).",
                   "A glycoside cannot open into a chain, so it does <b>not</b> mutarotate and is <b>not</b> a reducing sugar (unless another free anomeric –OH remains).",
                   "Drug glycosides: <b>digoxin</b> (heart failure, from foxglove) and <b>sennosides</b> (senna laxatives): sugars attached to a non-sugar part."],
         "notes": "FGOB 20.5 (glycosidic linkage). Glycoside chemistry and drug examples original."})
    add({"t": "bullets", "sec": 4, "lo": LO4, "title": "Other sugar derivatives",
         "items": ["<b>Phosphate esters</b>: glucose 6-phosphate is the first step of glucose metabolism; ribose phosphates build ATP, DNA and RNA (Chapter 4: phosphate esters).",
                   "<b>Amino sugars</b>: an –OH replaced by –NH<sub>2</sub>. <b>Glucosamine</b> is in cartilage and is sold as a joint supplement; N-acetylglucosamine builds chitin (crab shells).",
                   "<b>Deoxy sugars</b>: an –OH replaced by H. <b>2-Deoxyribose</b> is the sugar of DNA.",
                   "<b>Uronic acids</b>: the CH<sub>2</sub>OH oxidised to –COOH. The liver joins drugs to <b>glucuronic acid</b> to make them water-soluble for excretion (paracetamol glucuronide)."],
         "notes": "Original summary of monosaccharide derivatives."})
    add({"t": "check", "sec": 4, "lo": LO4, "title": "Quick check",
         "q": "Which compound gives a NEGATIVE Benedict's test?",
         "opts": ["methyl α-D-glucoside", "glucose", "fructose", "galactose"], "ans": 0,
         "why": "A glycoside's anomeric carbon is locked, so the ring cannot open to an aldehyde.", "notes": "Answer A."})
    add({"t": "check", "sec": 4, "lo": LO4, "title": "Quick check",
         "q": "Reduction of D-glucose with H<sub>2</sub>/Ni gives:",
         "opts": ["sorbitol", "gluconic acid", "fructose", "glycogen"], "ans": 0,
         "why": "Aldehyde → alcohol: the sugar alcohol sorbitol (glucitol).", "notes": "Answer A."})

    # ================= 5.5 DISACCHARIDES =================
    add({"t": "divider", "num": 5, "title": "Disaccharides", "lo": "CH5-LO5", "src": "Ball 16.6 · FGOB 20.5–20.6",
         "blurb": "Two sugars joined by a glycosidic bond: malt sugar, milk sugar and table sugar."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO5, "title": "Maltose: glucose α(1→4) glucose",
         "fig": {"cap": "The bond from C1 of the first glucose points down (α) to C4 of the second.",
                 "data": disaccharide(GLC('a'), GLC('a'), 'a', labels=('α-D-glucose', 'D-glucose'))},
         "items": ["Two D-glucose units joined by an <b>α-1,4-glycosidic</b> linkage. C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>, like all three disaccharides.",
                   "The second glucose still has a free anomeric –OH (α or β), so maltose <b>mutarotates</b> and is a <b>reducing sugar</b>.",
                   "\"Malt sugar\": formed when starch is partly hydrolysed (germinating barley, digestion). About 30% as sweet as sucrose.",
                   "Hydrolysis (enzyme <b>maltase</b>, or dilute acid and heat) → 2 glucose."],
         "notes": "FGOB 20.6; Ball 16.6."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO5, "title": "Lactose: galactose β(1→4) glucose",
         "fig": {"cap": "The bond from C1 of galactose points up (β) to C4 of glucose.",
                 "data": disaccharide(GAL('b'), GLC('b'), 'b', labels=('β-D-galactose', 'D-glucose'))},
         "items": ["D-galactose + D-glucose joined by a <b>β-1,4-glycosidic</b> linkage. Glucose's anomeric –OH is free → <b>reducing sugar</b>.",
                   "\"Milk sugar\": human milk about 7.5%, cow's milk about 4.5%. Only about one-sixth as sweet as sucrose.",
                   "Hydrolysed by the enzyme <b>lactase</b>. Bacteria ferment lactose to lactic acid, which sours milk.",
                   "<b>Pharmacy</b>: lactose is the most common <b>tablet filler</b> (diluent)."],
         "notes": "Ball 16.6. Tablet filler original."})
    add({"t": "two", "sec": 5, "lo": LO5, "title": "Lactose intolerance and galactosemia",
         "lead": "Two different problems, both about lactose and galactose.",
         "cols": [{"h": "Lactose intolerance", "tone": "cold", "items": [
             "Too little <b>lactase</b> in adults: about 70% of the world's adults have some deficiency",
             "Undigested lactose draws water into the colon; bacteria make acid and gas → cramps, bloating, diarrhoea",
             "Manage: smaller amounts, lactose-free or fermented dairy (yoghurt), <b>lactase tablets</b> with meals",
             "The small amount of lactose in most tablets is usually tolerated; check if the patient is very sensitive"]},
             {"h": "Galactosemia", "tone": "heat", "items": [
                 "A <b>genetic</b> disease: an enzyme that converts galactose to glucose is missing",
                 "Galactose builds up in blood and urine; infants fail to thrive, with jaundice",
                 "Untreated: liver damage, cataracts, intellectual disability, death",
                 "Treatment: remove milk and all galactose sources from the diet from birth"]}],
         "notes": "Ball 16.6 (Looking Closer). Tablet note original."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO5, "title": "Sucrose: glucose α(1→2) fructose",
         "fig": {"cap": "The fructose ring is drawn turned over, so its C2 sits next to glucose's C1.",
                 "data": sucrose()},
         "items": ["α-D-glucose C1 joined to β-D-fructose C2: an <b>α-1,β-2-glycosidic</b> linkage, \"head to head\".",
                   "<b>Both</b> anomeric carbons are used in the bond: no free anomeric –OH, so sucrose does <b>not</b> mutarotate and is a <b>non-reducing sugar</b> (Benedict's stays blue).",
                   "Table sugar, from sugar cane and sugar beet (14–20% of their juice). Molasses is what is left after crystallising it."],
         "notes": "Ball 16.6."})
    add({"t": "bullets", "sec": 5, "lo": LO5, "title": "Invert sugar, health and syrups",
         "items": ["Hydrolysis of sucrose (acid, or the enzyme <b>sucrase/invertase</b>) gives a 1:1 mixture of glucose and fructose: <b>invert sugar</b>. It rotates light the opposite way (fructose's −92° wins).",
                   "Invert sugar is sweeter (fructose) and does not crystallise easily: used in jams and sweets; bees make honey this way.",
                   "Too much sucrose → obesity (excess is stored as fat) and tooth decay (it feeds plaque bacteria) (Ball 16.6).",
                   "<b>Pharmacy</b>: sucrose syrup is the classic vehicle for oral liquids (Syrup BP is about 67% sucrose). Diabetic patients may need sugar-free versions sweetened with sorbitol or artificial sweeteners."],
         "notes": "Ball 16.6; syrup vehicle original."})
    add({"t": "table", "sec": 5, "lo": LO5, "title": "How sweet? (sucrose = 100)",
         "head": ["Sugar or sweetener", "Relative sweetness", "Note"],
         "rows": [["lactose", "16", "milk sugar"], ["maltose", "32", "malt sugar"], ["glucose", "74", "dextrose"], ["sucrose", "100", "reference"],
                  ["fructose", "173", "sweetest sugar"], ["aspartame", "18 000", "not heat-stable; avoid in phenylketonuria (PKU)"],
                  ["acesulfame K", "20 000", "heat-stable"], ["saccharin", "30 000", "bitter aftertaste"], ["sucralose", "60 000", "sucrose with 3 –OH replaced by Cl"]],
         "widths": [2.8, 2.2, 5.0],
         "caption": "Source: Ball 16.3 (table and Looking Closer: Artificial Sweeteners).",
         "notes": "Ball 16.3."})
    add({"t": "table", "sec": 5, "lo": LO5, "title": "The three disaccharides compared",
         "head": ["", "Maltose", "Lactose", "Sucrose"],
         "rows": [["Units", "glucose + glucose", "galactose + glucose", "glucose + fructose"],
                  ["Linkage", "α-1,4", "β-1,4", "α-1,β-2"],
                  ["Free anomeric –OH?", "yes", "yes", "no"],
                  ["Reducing sugar?", "<b>yes</b>", "<b>yes</b>", "<b>no</b>"],
                  ["Enzyme", "maltase", "lactase", "sucrase (invertase)"],
                  ["Source", "germinating grain, starch digestion", "milk", "cane and beet sugar"]],
         "widths": [2.6, 2.6, 2.6, 2.6],
         "caption": "Source: Ball 16.6.",
         "notes": "Ball 16.6 summary."})
    add({"t": "check", "sec": 5, "lo": LO5, "title": "Quick check",
         "q": "Which disaccharide is NOT a reducing sugar?",
         "opts": ["sucrose", "maltose", "lactose", "all three are reducing"], "ans": 0,
         "why": "Both anomeric carbons are tied up in the α-1,β-2 bond.", "notes": "Answer A."})
    add({"t": "check", "sec": 5, "lo": LO5, "title": "Quick check",
         "q": "Hydrolysis of lactose gives:",
         "opts": ["galactose + glucose", "glucose + glucose", "glucose + fructose", "galactose + fructose"], "ans": 0,
         "why": "By the enzyme lactase (or acid).", "notes": "Answer A."})

    # ================= 5.6 POLYSACCHARIDES =================
    add({"t": "divider", "num": 6, "title": "Polysaccharides", "lo": "CH5-LO5", "src": "Ball 16.7 · FGOB 20.7",
         "blurb": "Thousands of glucose units: energy stores in plants (starch) and animals (glycogen), and the fibre of plants (cellulose)."})
    add({"t": "bullets", "sec": 6, "lo": LO5, "title": "Polysaccharides: big, not sweet, non-reducing",
         "items": ["Tens to thousands of monosaccharides joined by glycosidic bonds. Starch, glycogen and cellulose are <b>homopolymers</b>: all glucose.",
                   "They are <b>not sweet</b>, do <b>not</b> mutarotate, and are <b>non-reducing</b> (only one free anomeric end in a huge molecule).",
                   "Complete hydrolysis gives glucose: starch → dextrins → maltose → glucose (enzymes: <b>amylases</b>).",
                   "Heteropolymers (gums, pectins, heparin) contain other units too."],
         "notes": "FGOB 20.7."})
    add({"t": "two", "sec": 6, "lo": LO5, "title": "Starch: amylose and amylopectin",
         "lead": "Starch is the plant's energy store and more than 50% of our dietary carbohydrate (rice 75%, corn 65%, wheat 55%, potato 15%).",
         "cols": [{"h": "Amylose (10–30%)", "tone": "cold", "items": [
             "<b>Unbranched</b> chain of glucose, <b>α-1,4</b> links (like maltose)",
             "Coils into a <b>helix</b>, 6 glucose per turn",
             "Iodine fits inside the helix: <b>deep blue-black</b> colour (the starch–iodine test)"]},
             {"h": "Amylopectin (70–90%)", "tone": "heat", "items": [
                 "<b>Branched</b>: α-1,4 chains with an <b>α-1,6</b> branch every 25–30 glucose units",
                 "Branching breaks up the helix: iodine gives only a <b>red-brown</b> colour",
                 "Thousands of glucose units per molecule"]}],
         "notes": "FGOB 20.7."})
    add({"t": "figure", "pos": "top", "sec": 6, "lo": LO5, "title": "α-1,4 versus β-1,4: starch versus cellulose",
         "fig": {"cap": "In cellulose each glucose is turned over relative to the next, which gives straight chains.",
                 "data": row([(disaccharide(GLC('a'), GLC('a'), 'a', labels=('α-glucose', 'glucose')), "α-1,4: starch, glycogen"), (disaccharide(GLC('b'), GLC('b'), 'b', labels=('β-glucose', 'glucose')), "β-1,4: cellulose")], w=430, h=215)},
         "items": ["Same glucose units, different link. Our <b>amylases</b> break α-1,4 links but <b>no human enzyme breaks β-1,4</b>.",
                   "That is why we digest rice but not grass or cotton."],
         "notes": "FGOB 20.3, 20.7."})
    add({"t": "two", "sec": 6, "lo": LO5, "title": "Glycogen and cellulose",
         "lead": "Two very different jobs for the same glucose units.",
         "cols": [{"h": "Glycogen: animal starch", "tone": "cold", "items": [
             "Like amylopectin, but <b>more branched</b> (every 8–12 units) with shorter branches",
             "Stored in <b>liver</b> (4–8% of its weight) and <b>muscle</b>; about 70% of the total is in muscle",
             "Used up in the first day of fasting to keep blood glucose steady",
             "Iodine: red-brown"]},
             {"h": "Cellulose: plant structure", "tone": "heat", "items": [
                 "<b>Unbranched</b>, <b>β-1,4</b> links: straight chains",
                 "Neighbouring chains <b>hydrogen bond</b> into strong fibres: insoluble in water",
                 "The most abundant carbohydrate: cotton ~95%, wood ~50%. No iodine colour",
                 "Cows and termites digest it only with the help of microbes that make <b>cellulase</b>"]}],
         "notes": "FGOB 20.7."})
    add({"t": "table", "sec": 6, "lo": LO5, "title": "Polysaccharides in the pharmacy",
         "head": ["Material", "Made from", "Use"],
         "rows": [["starch (maize, potato)", "starch", "tablet <b>disintegrant</b> (swells and breaks the tablet) and binder"],
                  ["dextrins", "partly hydrolysed starch", "binders for tablets and pills, adhesives on labels (FGOB 20.7)"],
                  ["microcrystalline cellulose (MCC)", "cellulose", "the most common tablet filler and binder"],
                  ["methylcellulose, HPMC, CMC", "cellulose with –OH groups converted to ethers", "tablet coatings, capsule shells (vegetarian), bulk laxatives, artificial tears"],
                  ["dextran", "bacterial glucose polymer", "IV plasma expander"],
                  ["heparin", "sulfated polysaccharide", "injectable anticoagulant"]],
         "widths": [3.2, 3.2, 4.4],
         "caption": "Cellulose derivatives are useful because their –OH groups are partly turned into ethers, which lets them dissolve or swell in water instead of forming fibres.",
         "notes": "Original pharmacy table (dextrins from FGOB 20.7)."})
    add({"t": "check", "sec": 6, "lo": LO5, "title": "Quick check",
         "q": "A solution turns deep blue-black with iodine. It contains:",
         "opts": ["amylose (starch)", "cellulose", "glucose", "sucrose"], "ans": 0,
         "why": "Iodine fits inside the amylose helix. Glycogen and amylopectin give red-brown; cellulose gives no colour.", "notes": "Answer A."})
    add({"t": "check", "sec": 6, "lo": LO5, "title": "Quick check",
         "q": "Humans cannot digest cellulose because:",
         "opts": ["we have no enzyme that hydrolyses β-1,4-glycosidic bonds", "cellulose contains fructose", "cellulose is a reducing sugar", "cellulose has α-1,6 branches"], "ans": 0,
         "why": "Amylases only break α links.", "notes": "Answer A."})

    # ================= wrap-up =================
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Carbohydrates", "polyhydroxy aldehydes or ketones; mono-, di-, polysaccharides"],
        ["Chirality", "chiral C = 4 different groups; enantiomers; up to 2<sup>n</sup> stereoisomers; +/− rotation; racemate"],
        ["Monosaccharides", "aldose/ketose + triose…hexose; Fischer: lowest chiral C, OH right = D"],
        ["Cyclic forms", "hemiacetal ring; Haworth: right → down; α = C1–OH down, β = up; mutarotation 36% α : 64% β"],
        ["Reactions", "reducing sugars (Benedict's blue → brick-red); reduction → sugar alcohols; glycosides are non-reducing"],
        ["Disaccharides", "maltose α-1,4 and lactose β-1,4 (reducing); sucrose α-1,β-2 (non-reducing)"],
        ["Polysaccharides", "amylose α-1,4; amylopectin and glycogen α-1,4 + α-1,6; cellulose β-1,4"],
        ["Pharmacy", "chiral drugs; lactose, starch, MCC and HPMC as excipients; glucose testing"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 30 min)", "Attempt the Chapter 5 tutorial",
                   "Play the Chapter 5 game to find your weak outcomes", "Next chapter: Lipids"],
         "attrib": "Adapted from LibreTexts (Ball, Hill &amp; Scott; FGOB), CC BY-NC-SA 3.0, with original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"]})
    return S
