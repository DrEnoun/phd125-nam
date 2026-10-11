"""PHD125 Chapter 1 · activities: before class, after class, tutorial (DATA for the PHD115 activity engine).
Tutorial Part A/B adapts Ball 12.E (Dr. NAM's ALKANE EXERCISE file) where noted; other items are original."""
from figs import mol

TITLE = 'Introduction to Organic Molecule'
ATTRIB = ("Adapted from LibreTexts <i>Introduction to Organic Chemistry – Alkanes</i> 12.1–12.5 (Sharpe Elles, from Ball, Hill &amp; Scott) and "
          "<i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) 12.1, 12.4 and exercises 12.E, CC BY-NC-SA 3.0. Pharmacy items are original material by Dr. NAM. "
          "Shared under CC BY-NC-SA for non-commercial teaching.")


def img(smi, w=300, h=150, **k):
    return f'<img src="{mol(smi, w, h, **k)}" alt="structure" style="display:block;max-width:100%;height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch1", "act": "pre", "topicTitle": TITLE,
    "title": "Before class: carbon, the builder", "pdf": "../../downloads/PHD125_CH1_PreLecture.pdf",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 1 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "Carbon makes four bonds",
             "html": "<p>Carbon has <b>four valence electrons</b>, so it shares electrons to form <b>four covalent bonds</b>. It bonds strongly to other carbon atoms, so it builds chains, branches and rings, and it also bonds to H, O, N, S and the halogens.</p><p>Compounds built on carbon are called <b>organic compounds</b>. There are millions of them, from methane (CH<sub>4</sub>) to DNA.</p>"},
            {"type": "read", "h": "Chemists draw molecules in shorthand",
             "html": "<p>Ethanol can be written as C<sub>2</sub>H<sub>6</sub>O, as CH<sub>3</sub>CH<sub>2</sub>OH, or as a zig-zag line ending in OH. In the zig-zag (line) drawing, every corner and end is a carbon and the hydrogens on carbon are hidden. You will learn to read all of these in the lecture.</p>" + img('CCO', 240, 100)},
            {"type": "read", "h": "Why this matters in pharmacy",
             "html": "<p>Almost every medicine you will dispense is an organic compound: paracetamol, aspirin, antibiotics, vitamins. Small groups of atoms in these molecules, called <b>functional groups</b>, decide whether a drug dissolves in water, how it is absorbed and how long it lasts on the shelf.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: PHD115 basics you need today, and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "How many valence electrons does a carbon atom (Group 4A) have?", "opts": ["2", "4", "6", "8"], "ans": 1, "why": "Group 4A → 4 valence electrons."},
            {"type": "mcq", "lo": "Recap", "q": "A covalent bond is:", "opts": ["a transfer of electrons from a metal to a nonmetal", "a shared pair of electrons between two atoms", "the attraction between two ions", "a bond between two metal atoms"], "ans": 1, "why": "Covalent bonds form when atoms share electrons."},
            {"type": "match", "lo": "Recap", "q": "How many covalent bonds does each atom usually form?", "left": ["H", "O", "N", "C"], "right": ["1", "2", "3", "4"], "ans": [0, 1, 2, 3], "why": "H 1, O 2, N 3, C 4: each reaches a duet or an octet."},
            {"type": "tf", "lo": "Recap", "q": "A C–O bond is polar because oxygen is more electronegative than carbon.", "ans": True, "why": "Oxygen pulls the shared electrons towards itself, giving O a partial negative charge."},
            {"type": "mcq", "lo": "Recap", "q": "Which property is typical of an ionic compound such as NaCl?", "opts": ["Low melting point", "Burns easily", "High melting point", "Insoluble in water"], "ans": 2, "why": "Strong attractions between ions give ionic compounds high melting points (NaCl melts at 801 °C)."},
            {"type": "mcq", "lo": "CH1-LO1", "q": "Organic chemistry is now defined as the chemistry of compounds that contain:", "opts": ["oxygen", "carbon", "nitrogen", "living cells"], "ans": 1, "why": "Today 'organic' means carbon-containing, whatever the source."},
            {"type": "tf", "lo": "CH1-LO1", "q": "Carbon dioxide (CO<sub>2</sub>) is classed as an organic compound.", "ans": False, "why": "CO<sub>2</sub>, CO, carbonates and bicarbonates are treated as inorganic, by convention."},
            {"type": "fill", "lo": "CH1-LO2", "q": "Write the molecular formula of CH<sub>3</sub>CH<sub>2</sub>OH. Type it on one line, e.g. C2H6 for C<sub>2</sub>H<sub>6</sub>.", "acc": ["C2H6O", "C2H5OH"], "cs": True, "show": "C<sub>2</sub>H<sub>6</sub>O", "ph": "e.g. C2H6", "why": "2 C, 6 H, 1 O. (C<sub>2</sub>H<sub>5</sub>OH is also accepted.)"},
            {"type": "mcq", "lo": "CH1-LO3", "q": "Which is the functional group of an alcohol?", "opts": ["–OH", "–COOH", "–NH<sub>2</sub>", "C=C"], "ans": 0, "why": "Alcohols contain an –OH group on a carbon chain."},
            {"type": "self", "lo": "CH1-LO5", "q": "Name one medicine or everyday product you think is made of organic compounds, and say why.", "model": "Any carbon-based product is right: paracetamol, aspirin, vitamin C, soap, cooking oil, plastic bottles. They are built on carbon skeletons."}]}]}

POST = {
    "topic": "ch1", "act": "post", "topicTitle": TITLE,
    "title": "After class: check your understanding", "pdf": "../../downloads/PHD125_CH1_PostLecture.pdf",
    "sub": "About 25 minutes. Questions follow the five subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH1-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "1.1–1.2 · Organic compounds and their features", "items": [
            {"type": "mcq", "lo": "CH1-LO1", "q": "Wöhler's 1828 experiment made urea from ammonium cyanate. Why did this matter?", "opts": ["It showed organic compounds need a vital force", "It made an organic compound from an inorganic one, with no living thing", "It was the first ionic compound made", "It proved urea is inorganic"], "ans": 1, "why": "It weakened vitalism, the idea that organic compounds can only come from living things."},
            {"type": "match", "lo": "CH1-LO1", "q": "Classify each compound (Ball 12.E).", "left": ["C<sub>3</sub>H<sub>8</sub>O", "CaCl<sub>2</sub>", "CH<sub>3</sub>NH<sub>2</sub>", "NaHCO<sub>3</sub>", "C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>"], "right": ["organic", "inorganic"], "ans": [0, 1, 0, 1, 0], "why": "Carbon compounds are organic, except CO, CO<sub>2</sub>, carbonates, bicarbonates and cyanides. CaCl<sub>2</sub> has no carbon."},
            {"type": "mcq", "lo": "CH1-LO1", "q": "In which pair does the <b>first</b> compound have the higher melting point? (Ball 12.E)", "opts": ["NaOH, then CH<sub>3</sub>OH", "CH<sub>3</sub>Cl, then KCl", "C<sub>2</sub>H<sub>6</sub>, then CoCl<sub>2</sub>", "CH<sub>4</sub>, then LiH"], "ans": 0, "why": "Ionic compounds (NaOH, KCl, CoCl<sub>2</sub>, LiH) melt at higher temperatures than the covalent organic compounds."},
            {"type": "tf", "lo": "CH1-LO1", "q": "Every carbon atom in a neutral organic molecule forms four bonds.", "ans": True, "why": "Carbon is tetravalent: count single, double and triple bonds; they always add up to four."},
            {"type": "mcq", "lo": "CH1-LO1", "q": "Why are hydrocarbons insoluble in water?", "opts": ["They are ionic", "C–H bonds are nonpolar, so the molecules are nonpolar", "They are too heavy", "They react with water"], "ans": 1, "why": "Carbon and hydrogen have similar electronegativity. Nonpolar molecules do not mix with polar water."}]},
        {"h": "1.3 · Drawing organic molecules", "items": [
            {"type": "fill", "lo": "CH1-LO2", "q": "Write the molecular formula of the compound below. Type it on one line, e.g. C4H10." + img('CC(C)CC', 260, 110), "acc": ["C5H12"], "cs": True, "show": "C<sub>5</sub>H<sub>12</sub>", "ph": "e.g. C4H10", "why": "Five corners and ends = 5 C. Hydrogens: 3 + 1 + 3 + 2 + 3 = 12."},
            {"type": "num", "lo": "CH1-LO2", "q": "In a line structure, a carbon at a corner with exactly two lines meeting there carries how many hydrogen atoms?", "ans": 2, "tol": 0, "unit": "H", "why": "4 − 2 bonds = 2 H: a CH<sub>2</sub> group."},
            {"type": "mcq", "lo": "CH1-LO2", "q": "Which is the condensed formula of the compound drawn here?" + img('CCCO', 240, 100), "opts": ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH", "CH<sub>3</sub>OCH<sub>2</sub>CH<sub>3</sub>", "CH<sub>3</sub>CH(OH)CH<sub>3</sub>", "CH<sub>3</sub>CH<sub>2</sub>OH"], "ans": 0, "why": "Three carbons in a chain with OH on the end carbon: 1-propanol."},
            {"type": "match", "lo": "CH1-LO2", "q": "Match each description to the shape around carbon.", "left": ["four single bonds", "one double bond", "one triple bond"], "right": ["tetrahedral, 109.5°", "trigonal planar, 120°", "linear, 180°"], "ans": [0, 1, 2], "why": "4, 3 or 2 electron groups around carbon."},
            {"type": "self", "lo": "CH1-LO2", "q": "Draw the line structure and the expanded structure of CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>3</sub> on paper. Then compare.", "model": "Line structure: a 'Y' shape (three lines from one central carbon). Expanded: a central C bonded to one H and three CH<sub>3</sub> groups, every H drawn. It is 2-methylpropane, C<sub>4</sub>H<sub>10</sub>." + img('CC(C)C', 200, 110)}]},
        {"h": "1.4 · Functional groups", "items": [
            {"type": "match", "lo": "CH1-LO3", "q": "Match each functional group to its family.", "left": ["–OH on a chain", "–COOH", "–CHO", "C–O–C", "–CONH<sub>2</sub>", "–SH"], "right": ["alcohol", "carboxylic acid", "aldehyde", "ether", "amide", "thiol", "ketone"], "ans": [0, 1, 2, 3, 4, 5], "why": "Ketone is the extra option: C=O between two carbons."},
            {"type": "mcq", "lo": "CH1-LO3", "q": "Which functional groups are in paracetamol?" + img('CC(=O)Nc1ccc(O)cc1', 280, 120), "opts": ["Aromatic ring, phenol, amide", "Aromatic ring, alcohol, amine", "Aromatic ring, carboxylic acid, ester", "Alkene, phenol, ketone"], "ans": 0, "why": "The –OH sits on the ring (phenol), and the N is bonded to a C=O (amide)."},
            {"type": "tf", "lo": "CH1-LO3", "q": "A C=O group with an –O–C attached to the carbonyl carbon is an ester.", "ans": True, "why": "R–COO–R′ is an ester. With –OH instead it would be a carboxylic acid."},
            {"type": "mcq", "lo": "CH1-LO3", "q": "Benzocaine has an –NH<sub>2</sub> on its ring and no C=O next to the N. That group is:", "opts": ["an amide", "an amine", "a nitrile", "an alcohol"], "ans": 1, "why": "An amide needs N bonded to C=O. Without it, –NH<sub>2</sub> is an amine."}]},
        {"h": "1.5 · Pharmacy and everyday life", "items": [
            {"type": "tf", "lo": "CH1-LO4", "q": "Vitamin C extracted from oranges works better than vitamin C made in a factory because it is natural.", "ans": False, "why": "Both are ascorbic acid: the same molecule with the same properties. Only purity, dose and other compounds present can differ."},
            {"type": "mcq", "lo": "CH1-LO4", "q": "A customer says a herbal product must be safe because it is natural. The best reply is:", "opts": ["Agree: natural products have no side effects", "Explain that safety depends on the molecules and doses present, not on the source", "Say natural products never work", "Say only synthetic drugs contain chemicals"], "ans": 1, "why": "Digoxin from foxglove is natural and toxic in overdose. Everything is made of chemicals."},
            {"type": "match", "lo": "CH1-LO5", "q": "Match each name type for paracetamol.", "left": ["N-(4-hydroxyphenyl)acetamide", "paracetamol", "Panadol"], "right": ["chemical (IUPAC) name", "generic name", "brand name"], "ans": [0, 1, 2], "why": "The IUPAC name describes the structure; the generic name is used in prescribing; the brand name belongs to a manufacturer."},
            {"type": "mcq", "lo": "CH1-LO5", "q": "Why does an old bottle of aspirin smell of vinegar?", "opts": ["The aromatic ring breaks open", "The ester group is hydrolysed by moisture, releasing acetic acid", "Aspirin turns into ethanol", "The carboxylic acid evaporates"], "ans": 1, "why": "Aspirin + water → salicylic acid + acetic acid. Acetic acid is the acid in vinegar."},
            {"type": "mcq", "lo": "CH1-LO5", "q": "Morphine and quinine are examples of:", "opts": ["synthetic polymers", "alkaloids from plants", "inorganic salts", "esters from animals"], "ans": 1, "why": "Both are nitrogen-containing plant compounds: alkaloids."}]},
        {"h": "Pharmacy scenario · The cold-and-flu shelf", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Encik Hafiz buys Panadol for a fever. He also picks up a cold-and-flu tablet whose label reads: <i>paracetamol 500 mg, phenylephrine 5 mg, chlorphenamine 2 mg</i>. He plans to take both, the full dose of each, for three days.</p>"},
            {"type": "mcq", "lo": "CH1-LO5", "q": "What is the main problem with his plan?", "opts": ["Phenylephrine is an organic compound", "Both products contain paracetamol, so he could take a double dose", "Chlorphenamine is a brand name", "Panadol does not work for fever"], "ans": 1, "why": "Reading the generic names of all active ingredients shows the duplication."},
            {"type": "num", "lo": "CH1-LO5", "q": "If he takes 2 Panadol tablets (500 mg each) four times a day plus 1 flu tablet four times a day, how many grams of paracetamol is that per day?", "ans": 6, "tol": 0, "unit": "g", "why": "(2 × 500 + 1 × 500) × 4 = 6000 mg = 6 g, well above the usual adult maximum of 4 g in 24 hours."},
            {"type": "self", "lo": "CH1-LO5", "q": "Write two sentences of advice for Encik Hafiz.", "model": "Take only one paracetamol-containing product at a time, and do not take more than the label dose (no more than 4 g of paracetamol in 24 hours). Always check the generic names of the active ingredients on every medicine label."}]}]}

TUT = {
    "topic": "ch1", "act": "tut", "topicTitle": TITLE,
    "title": "Tutorial: exam-style practice", "pdf": "../../downloads/PHD125_CH1_Tutorial.pdf",
    "sub": "Part A: 10 multiple-choice questions (1 mark each). Part B: 4 structured questions (25 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 35.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 1 game, or move on to Chapter 2.",
    "sections": []}
T = 'Introduction to Organic Molecule'
A = [
    ("CH1-LO1", "Which compound is <b>inorganic</b>? (Ball 12.E)", ["C<sub>6</sub>H<sub>10</sub>", "C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>", "CoCl<sub>2</sub>", "CH<sub>3</sub>NH<sub>2</sub>"], 2, "CoCl<sub>2</sub> contains no carbon."),
    ("CH1-LO1", "Which carbon compound is classed as <b>inorganic</b>?", ["CH<sub>3</sub>OH", "CaCO<sub>3</sub>", "C<sub>2</sub>H<sub>6</sub>", "CH<sub>3</sub>COOH"], 1, "Carbonates are treated as inorganic by convention."),
    ("CH1-LO1", "A compound burns easily, melts at −20 °C and does not dissolve in water. It is most likely:", ["ionic", "organic", "a metal", "a salt"], 1, "Flammable, low-melting and insoluble in water: typical organic properties (Ball 12.E)."),
    ("CH1-LO1", "Carbon forms a huge number of compounds mainly because it:", ["forms four strong covalent bonds, including to other carbon atoms", "is the most abundant element on Earth", "forms ions easily", "is a metal"], 0, "Catenation and tetravalency give carbon its diversity."),
    ("CH1-LO2", "The molecular formula of CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> is:", ["C<sub>4</sub>H<sub>8</sub>", "C<sub>4</sub>H<sub>10</sub>", "C<sub>3</sub>H<sub>10</sub>", "C<sub>4</sub>H<sub>12</sub>"], 1, "4 C and 3 + 2 + 2 + 3 = 10 H."),
    ("CH1-LO2", "In a line-angle structure, which atoms are <b>not</b> written as symbols?", ["oxygen atoms", "carbon atoms and the hydrogens on them", "nitrogen atoms", "chlorine atoms"], 1, "Ends and bends are carbons; H on carbon is implied."),
    ("CH1-LO2", "The H–C–H bond angle in methane is about:", ["90°", "109.5°", "120°", "180°"], 1, "Four electron groups → tetrahedral, 109.5°."),
    ("CH1-LO3", "The functional group –COOH is called:", ["an ester", "an aldehyde", "a carboxylic acid", "a ketone"], 2, "C=O with an OH on the carbonyl carbon."),
    ("CH1-LO3", "CH<sub>3</sub>COCH<sub>3</sub> belongs to which family?", ["aldehyde", "ketone", "ether", "ester"], 1, "C=O between two carbons: a ketone (propanone, acetone)."),
    ("CH1-LO4", "Synthetic and natural samples of the same pure compound:", ["have different melting points", "behave identically", "have different formulas", "differ in the number of bonds to carbon"], 1, "A compound is defined by its structure, not its source."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH1-LO1", "marks": 5, "level": "C2",
     "q": "(a) Explain what <i>vitalism</i> was and how Wöhler's 1828 experiment challenged it. (3 marks) (b) Give two reasons why carbon can form so many different compounds. (2 marks)",
     "hint": "What did people believe organic compounds needed? What did Wöhler start from, and what did he make?",
     "work": "(a) Vitalism was the belief that organic compounds could only be made by living organisms because they need a 'vital force'. Wöhler heated ammonium cyanate, an inorganic salt, and obtained urea, an organic compound found in urine. No living thing was involved, so organic compounds could be made in the laboratory. (b) Any two: carbon forms four covalent bonds; it bonds strongly to other carbon atoms, forming chains, branches and rings; it bonds strongly to other elements such as H, O, N; it forms single, double and triple bonds.",
     "rubric": [["Vitalism: organic compounds thought to need a vital force from living things", 1], ["Wöhler made urea from ammonium cyanate (inorganic)", 1], ["Conclusion: organic compound made without a living organism", 1], ["First valid reason", 1], ["Second valid reason", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH1-LO1", "marks": 6, "level": "C4",
     "q": "Two white solids are labelled X and Y. X melts at 801 °C, does not burn and its aqueous solution conducts electricity. Y melts at 186 °C, chars and burns when heated, and its aqueous solution does not conduct. (a) Classify X and Y as organic or inorganic, giving <b>two</b> reasons for each. (4 marks) (b) State the type of bonding in each. (2 marks)",
     "hint": "Compare each property with the table of organic vs inorganic compounds.",
     "work": "(a) X is inorganic: very high melting point; nonflammable; solution conducts (ions present). Y is organic: low melting point; flammable; solution does not conduct. (b) X: ionic bonding (X is in fact NaCl). Y: covalent bonding (Y is sucrose).",
     "rubric": [["X inorganic with first reason", 1], ["X second reason", 1], ["Y organic with first reason", 1], ["Y second reason", 1], ["X: ionic bonding", 1], ["Y: covalent bonding", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH1-LO2", "marks": 7, "level": "C3",
     "q": "For the compound CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>OH: (a) write its molecular formula (1 mark); (b) draw its expanded structural formula (2 marks); (c) draw its line-angle structure (2 marks); (d) state the shape and bond angle around the carbon that carries the CH<sub>3</sub> branch (2 marks).",
     "hint": "Count every C, H and O first. In the line structure, remember to write OH but not the H on carbon.",
     "work": "(a) C<sub>4</sub>H<sub>10</sub>O. (b) Four carbons: C1 (3 H) bonded to C2; C2 has 1 H and a CH<sub>3</sub> branch; C2 bonded to C3 (2 H), which carries the O–H. Every H drawn. (c) A three-line 'Y' with one arm extended to end in OH:" + img('CC(C)CO', 220, 110) + "(d) That carbon has four single bonds: tetrahedral, about 109.5°.",
     "rubric": [["C<sub>4</sub>H<sub>10</sub>O", 1], ["Expanded: correct carbon skeleton with branch", 1], ["Expanded: all 10 H and the O–H shown", 1], ["Line: correct zig-zag with branch", 1], ["Line: OH written, H on carbon omitted", 1], ["Tetrahedral", 1], ["109.5°", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH1-LO3", "marks": 7, "level": "C4",
     "q": "Aspirin and paracetamol are both used for pain and fever." + img('CC(=O)Oc1ccccc1C(=O)O', 260, 140) + img('CC(=O)Nc1ccc(O)cc1', 260, 110) + "(a) Name all the functional groups in aspirin (top) and in paracetamol (bottom). (5 marks) (b) A patient's aspirin tablets, kept in a humid bathroom, smell of vinegar. Explain why, naming the functional group involved. (2 marks)",
     "hint": "Look at every C=O and see what is attached to it. Is the –OH on a chain or on the ring?",
     "work": "(a) Aspirin: aromatic ring, carboxylic acid, ester. Paracetamol: aromatic ring, phenol (–OH on the ring), amide. (b) The ester group in aspirin is hydrolysed by moisture, forming salicylic acid and acetic acid; acetic acid gives the vinegar smell. The tablets should be discarded and medicines stored in a dry place.",
     "rubric": [["Aspirin: aromatic ring", 1], ["Aspirin: carboxylic acid and ester (both)", 1], ["Paracetamol: aromatic ring", 1], ["Paracetamol: phenol", 1], ["Paracetamol: amide", 1], ["Ester hydrolysed by water", 1], ["Acetic acid formed (vinegar smell)", 1]]}]})
