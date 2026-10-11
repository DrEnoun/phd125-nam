"""PHD125 Chapter 7 · activities: before class, after class, tutorial.
(FGOB 18.x/19.x) items adapt that source; drug and pharmacy items are original.
Tutorial weighting: amino acids and acid–base about 40%, peptides and proteins about 35%, enzymes about 25%."""
from figs import mol

TITLE = 'Amino Acids, Proteins and Enzymes'
ATTRIB = ("Adapted from <i>Fundamentals of General Organic and Biological Chemistry</i> 18.1–18.10 and 19.2–19.7 (remixed from Ball, Hill &amp; Scott, chapter 18), "
          "LibreTexts, CC BY-NC-SA 3.0. Drug questions and pharmacy scenarios are original material by Dr. NAM. "
          "Shared under CC BY-NC-SA for non-commercial teaching.")


def pic(uri, maxw=320):
    return f'<img src="{uri}" alt="structure" style="display:block;max-width:min(100%,{maxw}px);height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch7", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH7_PreLecture.pdf",
    "title": "Before class: twenty building blocks",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 7 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "An acid and a base in one",
             "html": "<p>An <b>amino acid</b> has an amine (–NH<sub>2</sub>, a base) and a carboxylic acid (–COOH) on the same carbon, plus a side chain. In water the acid gives its proton to the amine of the same molecule, so amino acids carry both a + and a − charge.</p>"},
            {"type": "read", "h": "The amide bond, again",
             "html": "<p>In Chapter 4 an acid and an amine joined, losing water, to make an <b>amide</b>. Amino acids do the same, over and over: the chain of amide (peptide) bonds is a <b>protein</b>. Insulin has 51 amino acids; many proteins have hundreds.</p>"},
            {"type": "read", "h": "Shape is everything",
             "html": "<p>A protein chain folds into a precise 3D shape. Heat, alcohol or heavy metals can unfold it (<b>denaturation</b>), as when an egg white turns solid. <b>Enzymes</b> are proteins whose shape lets them speed up one reaction; many drugs work by blocking an enzyme.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "A carboxylic acid + an amine, heated, gives:", "opts": ["an amide + water", "an ester + water", "an ether", "a ketone"], "ans": 0, "why": "Chapter 4."},
            {"type": "mcq", "lo": "Recap", "q": "Which group is basic?", "opts": ["–NH<sub>2</sub>", "–COOH", "–OH", "–CHO"], "ans": 0, "why": "The N lone pair accepts H<sup>+</sup> (Chapter 4)."},
            {"type": "mcq", "lo": "Recap", "q": "Two cysteine –SH groups can be oxidised to form a:", "opts": ["disulfide bridge", "peptide bond", "ester", "glycosidic bond"], "ans": 0, "why": "Chapter 3."},
            {"type": "mcq", "lo": "CH7-LO1", "q": "How many different amino acids are commonly found in proteins?", "opts": ["20", "4", "64", "100"], "ans": 0, "why": "The same 20 in all living things."},
            {"type": "tf", "lo": "CH7-LO1", "q": "All amino acids in human proteins are the L form.", "ans": True, "why": "Glycine is not chiral; all the others are L."},
            {"type": "mcq", "lo": "CH7-LO2", "q": "A molecule with both a + and a − charge but no overall charge is a:", "opts": ["zwitterion", "radical", "racemate", "polymer"], "ans": 0, "why": "Amino acids in water."},
            {"type": "mcq", "lo": "CH7-LO3", "q": "Proteins are polymers of:", "opts": ["amino acids", "glucose", "fatty acids", "nucleotides"], "ans": 0, "why": "Joined by peptide bonds."},
            {"type": "mcq", "lo": "CH7-LO4", "q": "Frying an egg turns the white solid because the protein is:", "opts": ["denatured", "hydrolysed to amino acids", "oxidised to sugar", "saponified"], "ans": 0, "why": "Its 3D shape is destroyed."},
            {"type": "mcq", "lo": "CH7-LO5", "q": "Enzymes are best described as:", "opts": ["biological catalysts, mostly proteins", "hormones made of fat", "sugars", "vitamins"], "ans": 0, "why": "They speed reactions without being used up."},
            {"type": "self", "lo": "CH7-LO5", "q": "Many medicines work by blocking an enzyme. Name one you have heard of, or suggest why blocking an enzyme could treat a disease.", "model": "Examples: statins block HMG-CoA reductase to lower cholesterol; aspirin blocks COX to reduce pain and inflammation; penicillin blocks a bacterial enzyme that builds the cell wall. Blocking the enzyme stops the harmful product (or the microbe's essential product) being made."}]}]}

POST = {
    "topic": "ch7", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH7_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH7-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "7.1–7.2 · Proteins and amino acids", "items": [
            {"type": "match", "lo": "CH7-LO1", "q": "Classify each amino acid by its side chain.", "left": ["leucine", "serine", "glutamic acid", "lysine"], "right": ["nonpolar", "polar, uncharged", "acidic", "basic"], "ans": [0, 1, 2, 3], "why": "FGOB Table 18.3.1."},
            {"type": "fill", "lo": "CH7-LO1", "q": "Which amino acid is the only one that is not chiral?", "acc": ["glycine", "gly", "g"], "ph": "name", "why": "R = H, so the α-carbon has two H atoms."},
            {"type": "mcq", "lo": "CH7-LO1", "q": "Which is an essential amino acid?", "opts": ["lysine", "glycine", "alanine", "serine"], "ans": 0, "why": "His, Ile, Leu, Lys, Met, Phe, Thr, Trp, Val."},
            {"type": "match", "lo": "CH7-LO1", "q": "Match each protein to its function.", "left": ["insulin", "haemoglobin", "keratin", "amylase"], "right": ["hormone", "transport", "structural", "enzyme"], "ans": [0, 1, 2, 3], "why": "FGOB Table 18.2.1."}]},
        {"h": "7.3 · Acid–base behaviour", "items": [
            {"type": "mcq", "lo": "CH7-LO2", "q": "Glycine at pH 1 exists mainly as:", "opts": ["H<sub>3</sub>N<sup>+</sup>CH<sub>2</sub>COOH (charge +1)", "H<sub>3</sub>N<sup>+</sup>CH<sub>2</sub>COO<sup>−</sup> (0)", "H<sub>2</sub>NCH<sub>2</sub>COO<sup>−</sup> (−1)", "H<sub>2</sub>NCH<sub>2</sub>COOH"], "ans": 0, "why": "In acid the carboxylate is protonated."},
            {"type": "fill", "lo": "CH7-LO2", "q": "What is the pH called at which an amino acid has no net charge? (two words or its abbreviation)", "acc": ["isoelectric point", "pi", "pI", "isoelectric pH"], "ph": "term", "why": "pI."},
            {"type": "match", "lo": "CH7-LO2", "q": "At pH 6, which way does each amino acid move in electrophoresis?", "left": ["aspartic acid (pI 3.0)", "alanine (pI 6.0)", "lysine (pI 9.8)"], "right": ["towards the + electrode", "does not move", "towards the − electrode"], "ans": [0, 1, 2], "why": "Above the pI it is negative; below it, positive."},
            {"type": "mcq", "lo": "CH7-LO2", "q": "Ninhydrin is used to detect amino acids because it:", "opts": ["reacts with the amino group to give a purple colour", "dissolves proteins", "is an enzyme", "measures pH"], "ans": 0, "why": "Also used for fingerprints (FGOB 18.4)."}]},
        {"h": "7.4 · Peptides", "items": [
            {"type": "mcq", "lo": "CH7-LO3", "q": "In the tripeptide Ala-Gly-Ser, the N-terminal amino acid is:", "opts": ["alanine", "glycine", "serine", "it has none"], "ans": 0, "why": "Written N- to C-terminal, left to right."},
            {"type": "fill", "lo": "CH7-LO3", "q": "How many water molecules are released when four amino acids join into a tetrapeptide?", "acc": ["3", "three"], "ph": "a number", "why": "One per peptide bond: 3 bonds."},
            {"type": "tf", "lo": "CH7-LO3", "q": "Gly-Ala and Ala-Gly are the same compound.", "ans": False, "why": "Different N- and C-terminals: they are isomers."},
            {"type": "mcq", "lo": "CH7-LO3", "q": "Sickle cell anaemia results from:", "opts": ["one wrong amino acid (Val for Glu) in haemoglobin", "too little glucose", "a missing disulfide in insulin", "a lipid disorder"], "ans": 0, "why": "Sequence decides function (FGOB 18.5)."}]},
        {"h": "7.5–7.6 · Proteins, hydrolysis and denaturation", "items": [
            {"type": "match", "lo": "CH7-LO4", "q": "Match each level of structure to what holds it.", "left": ["primary", "secondary", "tertiary", "quaternary"], "right": ["peptide bonds", "backbone hydrogen bonds", "side-chain interactions in one chain", "interactions between chains"], "ans": [0, 1, 2, 3], "why": "FGOB 18.6–18.9."},
            {"type": "mcq", "lo": "CH7-LO4", "q": "Which interaction is covalent?", "opts": ["disulfide bridge", "hydrogen bond", "ionic bond", "dispersion forces"], "ans": 0, "why": "–S–S– between two cysteines."},
            {"type": "mcq", "lo": "CH7-LO4", "q": "Complete hydrolysis of a protein gives:", "opts": ["amino acids", "glucose", "fatty acids and glycerol", "nucleotides"], "ans": 0, "why": "All peptide bonds are broken."},
            {"type": "mcq", "lo": "CH7-LO4", "q": "70% alcohol disinfects skin because it:", "opts": ["denatures microbial proteins", "hydrolyses DNA", "is an enzyme", "is a strong acid"], "ans": 0, "why": "It disrupts the proteins' hydrogen bonds (FGOB 18.10)."}]},
        {"h": "7.7 · Enzymes", "items": [
            {"type": "match", "lo": "CH7-LO5", "q": "Match each enzyme to its class.", "left": ["lipase", "alcohol dehydrogenase", "kinase", "isomerase"], "right": ["hydrolase", "oxidoreductase", "transferase", "isomerase class"], "ans": [0, 1, 2, 3], "why": "FGOB 19.3."},
            {"type": "mcq", "lo": "CH7-LO5", "q": "The rate of an enzyme reaction levels off at high [substrate] because:", "opts": ["all active sites are occupied (saturated)", "the enzyme is denatured", "the substrate runs out", "the product inhibits nothing"], "ans": 0, "why": "Like a fixed number of taxis (FGOB 19.5)."},
            {"type": "mcq", "lo": "CH7-LO5", "q": "A competitive inhibitor:", "opts": ["resembles the substrate and binds the active site", "binds an allosteric site only", "forms a covalent bond permanently", "denatures the enzyme"], "ans": 0, "why": "More substrate can outcompete it."},
            {"type": "mcq", "lo": "CH7-LO5", "q": "Nerve gases are lethal because they:", "opts": ["irreversibly inhibit acetylcholinesterase", "denature haemoglobin", "hydrolyse DNA", "activate amylase"], "ans": 0, "why": "They bond to a serine in the active site (FGOB 19.6)."}]},
        {"h": "Pharmacy scenario · The diabetic patient's fridge", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Encik Azman has type 2 diabetes. He injects <b>insulin</b>, takes <b>atorvastatin</b> and a daily <b>low-dose aspirin</b>. He asks why insulin must be kept in the fridge but not frozen, why he cannot take insulin as a tablet, and why his doctor says aspirin \"lasts longer than it stays in the blood\".</p>"},
            {"type": "mcq", "lo": "CH7-LO4", "q": "Why must insulin be kept at 2–8 °C and not frozen?", "opts": ["Heat or freezing can denature the protein so it no longer works", "Cold makes it sweeter", "It is a lipid that melts", "Freezing hydrolyses it to glucose"], "ans": 0, "why": "Protein shape must be preserved."},
            {"type": "mcq", "lo": "CH7-LO3", "q": "Why is insulin injected rather than swallowed?", "opts": ["Proteases in the gut would hydrolyse its peptide bonds", "It is too sweet", "It is insoluble in water", "Tablets denature in light"], "ans": 0, "why": "Most protein drugs are injected."},
            {"type": "mcq", "lo": "CH7-LO5", "q": "Low-dose aspirin protects against clots for days because it:", "opts": ["irreversibly acetylates COX in platelets, which cannot make new enzyme", "stays in the blood for weeks", "is a competitive inhibitor", "denatures platelets"], "ans": 0, "why": "Irreversible inhibition."},
            {"type": "self", "lo": "CH7-LO5", "q": "Explain to Encik Azman, in plain words, how atorvastatin works.", "model": "His liver makes cholesterol using an enzyme called HMG-CoA reductase. Atorvastatin looks enough like that enzyme's normal substrate to sit in its active site and block it (competitive inhibition), so the liver makes less cholesterol and his LDL ('bad') cholesterol falls. It must be taken regularly because the blocking wears off."}]}]}

TUT = {
    "topic": "ch7", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH7_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (38 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 50.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 7 game, or move on to Chapter 8.",
    "sections": []}
T = TITLE
A = [
    ("CH7-LO1", "The α-carbon of an amino acid carries:", ["–NH<sub>2</sub>, –COOH, –H and a side chain", "two –COOH groups", "a phosphate", "a benzene ring always"], 0, "FGOB 18.3."),
    ("CH7-LO1", "Which amino acid has a side chain that forms disulfide bridges?", ["cysteine", "serine", "alanine", "lysine"], 0, "–CH<sub>2</sub>SH."),
    ("CH7-LO1", "Amino acids in human proteins are:", ["L", "D", "racemic", "achiral"], 0, "Except glycine, which is not chiral."),
    ("CH7-LO2", "At a pH above its pI, an amino acid carries a net:", ["negative charge", "positive charge", "zero charge", "double positive charge"], 0, "It has lost H<sup>+</sup>."),
    ("CH7-LO2", "Which amino acid has the highest pI?", ["arginine", "aspartic acid", "alanine", "serine"], 0, "Basic side chain: pI 10.8."),
    ("CH7-LO3", "The bond joining amino acids in a protein is a(n):", ["amide (peptide) bond", "ester bond", "glycosidic bond", "disulfide bond"], 0, "–CO–NH–."),
    ("CH7-LO3", "How many different dipeptides can be made from one alanine and one glycine?", ["2", "1", "4", "3"], 0, "Ala-Gly and Gly-Ala."),
    ("CH7-LO4", "β-Pleated sheets are held together by hydrogen bonds:", ["between neighbouring chain segments", "within one turn of a helix", "between side chains only", "with water only"], 0, "FGOB 18.7."),
    ("CH7-LO4", "Heavy metal ions such as Hg<sup>2+</sup> denature proteins by binding:", ["–SH and –COO<sup>−</sup> groups", "peptide bonds", "sugars", "phosphates"], 0, "FGOB 18.10."),
    ("CH7-LO5", "An enzyme that hydrolyses fats is a:", ["lipase", "kinase", "isomerase", "ligase"], 0, "A hydrolase."),
    ("CH7-LO5", "Above about 50 °C, most enzyme reactions slow down because the enzyme:", ["denatures", "becomes saturated", "is hydrolysed to amino acids", "turns into a cofactor"], 0, "FGOB 19.5."),
    ("CH7-LO5", "Most coenzymes are made from:", ["water-soluble vitamins", "fatty acids", "cholesterol", "glucose"], 0, "FGOB 19.2."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH7-LO1", "marks": 7, "level": "C2",
     "q": "(a) Draw the general structure of an α-amino acid and label the α-carbon and the two functional groups. (2 marks) (b) Classify serine, leucine, aspartic acid and lysine according to their side chains. (2 marks) (c) Explain why glycine is not chiral but alanine is. (1 mark) (d) State which form, D or L, is found in human proteins, and name two essential amino acids. (2 marks)",
     "hint": "Look at the four groups on the α-carbon. Side chains: hydrocarbon, –OH, –COOH or –NH<sub>2</sub>?",
     "work": "(a) H<sub>2</sub>N–CH(R)–COOH: the α-carbon carries the amino group (–NH<sub>2</sub>), the carboxyl group (–COOH), H and the side chain R." + pic(mol('NC(C)C(=O)O', 220, 110)) + "(b) Serine: polar, uncharged (–CH<sub>2</sub>OH). Leucine: nonpolar. Aspartic acid: acidic. Lysine: basic. (c) In glycine R = H, so the α-carbon has two identical H atoms; in alanine it carries four different groups (H, CH<sub>3</sub>, NH<sub>2</sub>, COOH). (d) L. Any two of His, Ile, Leu, Lys, Met, Phe, Thr, Trp, Val.",
     "rubric": [["Correct general structure", 1], ["α-carbon, amino and carboxyl groups labelled", 1], ["Serine polar; leucine nonpolar", 1], ["Aspartic acid acidic; lysine basic", 1], ["Glycine has two H on the α-carbon", 1], ["L form", 1], ["Two correct essential amino acids", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH7-LO2", "marks": 8, "level": "C3",
     "q": "(a) Explain what a zwitterion is, and use it to explain why alanine is a high-melting solid that dissolves in water. (2 marks) (b) Draw the main form of alanine at pH 1, pH 6 and pH 12, and give the net charge of each. (3 marks) (c) Define the isoelectric point, and predict the direction of movement of aspartic acid (pI 3.0), alanine (pI 6.0) and lysine (pI 9.8) during electrophoresis at pH 6. (3 marks)",
     "hint": "Low pH adds H<sup>+</sup> to –COO<sup>−</sup>; high pH removes H<sup>+</sup> from –NH<sub>3</sub><sup>+</sup>.",
     "work": "(a) A zwitterion has a + charge (–NH<sub>3</sub><sup>+</sup>) and a − charge (–COO<sup>−</sup>) on the same molecule, formed when the acid gives H<sup>+</sup> to its own amine. Strong ionic attractions between zwitterions give a high melting point, and the charges interact well with water, like a salt. (b) pH 1: H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>3</sub>)–COOH, +1. pH 6: H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>3</sub>)–COO<sup>−</sup>, 0. pH 12: H<sub>2</sub>N–CH(CH<sub>3</sub>)–COO<sup>−</sup>, −1. (c) The pI is the pH at which the amino acid is a zwitterion with no net charge. At pH 6: aspartic acid (negative) moves to the positive electrode; alanine (neutral) does not move; lysine (positive) moves to the negative electrode.",
     "rubric": [["Zwitterion defined (+ and − on one molecule)", 1], ["Ionic attractions → high mp; salt-like → soluble", 1], ["pH 1 form, +1", 1], ["pH 6 zwitterion, 0", 1], ["pH 12 form, −1", 1], ["pI defined", 1], ["Asp → + electrode; Ala does not move", 1], ["Lys → − electrode", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH7-LO3", "marks": 7, "level": "C3",
     "q": "(a) Write an equation, using structural formulas, for the formation of the dipeptide Gly-Ser. Circle the peptide bond and name the type of reaction. (3 marks) (b) Explain why Gly-Ser and Ser-Gly are different compounds, and identify the N-terminal amino acid in each. (2 marks) (c) Explain how a single change in amino acid sequence causes sickle cell anaemia. (2 marks)",
     "hint": "Glycine's –COOH reacts with serine's –NH<sub>2</sub>.",
     "work": "(a) H<sub>2</sub>N–CH<sub>2</sub>–COOH + H<sub>2</sub>N–CH(CH<sub>2</sub>OH)–COOH → H<sub>2</sub>N–CH<sub>2</sub>–<b>CO–NH</b>–CH(CH<sub>2</sub>OH)–COOH + H<sub>2</sub>O. The CO–NH is the peptide (amide) bond; it is a condensation reaction." + pic(mol('NCC(=O)N[C@@H](CO)C(=O)O', 260, 110)) + "(b) The peptide bond joins different groups: in Gly-Ser glycine's –COOH is joined to serine's –NH<sub>2</sub>; in Ser-Gly it is the other way round, so the structures differ. N-terminal: glycine in Gly-Ser; serine in Ser-Gly. (c) In the haemoglobin β chain, valine (nonpolar) replaces glutamic acid (charged). The haemoglobin molecules stick together into long fibres, distorting red blood cells into a sickle shape that blocks small vessels.",
     "rubric": [["Correct reactants and products with water", 1], ["Peptide bond identified", 1], ["Condensation reaction", 1], ["Different groups joined → different compounds", 1], ["Correct N-terminals", 1], ["Val replaces Glu in haemoglobin", 1], ["Haemoglobin aggregates; sickled cells", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH7-LO4", "marks": 8, "level": "C3",
     "q": "(a) Describe the four levels of protein structure, stating the bonds or interactions that hold each. (4 marks) (b) Distinguish between protein hydrolysis and denaturation. (2 marks) (c) Explain why (i) 70% ethanol is used to disinfect skin, and (ii) insulin must be stored at 2–8 °C. (2 marks)",
     "hint": "Which levels does denaturation destroy? Which bonds does hydrolysis break?",
     "work": "(a) Primary: the amino acid sequence, held by peptide bonds. Secondary: α-helix and β-sheet, held by hydrogen bonds between backbone C=O and N–H. Tertiary: the overall fold of one chain, held by side-chain ionic bonds, hydrogen bonds, disulfide bridges and hydrophobic/dispersion interactions. Quaternary: the arrangement of two or more chains, held by the same side-chain interactions (e.g. haemoglobin). (b) Hydrolysis breaks peptide bonds (needs strong acid or proteases) and gives amino acids; denaturation unfolds the 2°, 3° and 4° structure but leaves the peptide bonds (primary structure) intact. (c)(i) Ethanol denatures microbial proteins by disrupting their hydrogen bonds. (ii) Heat (or freezing) can denature insulin, a protein, so it would stop working.",
     "rubric": [["Primary: sequence, peptide bonds", 1], ["Secondary: helix/sheet, backbone H-bonds", 1], ["Tertiary: side-chain interactions (named)", 1], ["Quaternary: several chains", 1], ["Hydrolysis breaks peptide bonds → amino acids", 1], ["Denaturation unfolds; primary structure kept", 1], ["Ethanol denatures microbial proteins", 1], ["Heat/freezing denatures insulin", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH7-LO5", "marks": 8, "level": "C4",
     "q": "(a) Explain what the active site of an enzyme is, and compare the lock-and-key and induced-fit models. (2 marks) (b) Explain why the rate of an enzyme reaction levels off at high substrate concentration, and why it falls above about 50 °C. (2 marks) (c) Atorvastatin is a competitive inhibitor of HMG-CoA reductase. Explain what this means and what happens if the concentration of the natural substrate rises. (2 marks) (d) Aspirin irreversibly inhibits cyclooxygenase (COX) in platelets. Explain why one low dose affects platelets for several days. (2 marks)",
     "hint": "Think of a fixed number of taxis. For (d), can a platelet make new enzyme?",
     "work": "(a) The active site is the pocket on the enzyme where the substrate binds and reacts. Lock and key: a rigid site that exactly fits the substrate. Induced fit: the site changes shape when the substrate binds, to fit it closely. (b) At high [S] all active sites are occupied (the enzyme is saturated), so adding substrate cannot increase the rate. Above about 50 °C the enzyme denatures and the active site loses its shape. (c) Atorvastatin resembles the substrate and binds reversibly to the active site, competing with the substrate; if [substrate] rises, more substrate wins the site and the rate recovers towards normal. (d) Aspirin forms a covalent bond (acetylates a serine) in COX, permanently inactivating it; platelets have no nucleus and cannot make new COX, so the effect lasts for the platelet's life (days), until new platelets are made.",
     "rubric": [["Active site defined", 1], ["Lock-and-key vs induced fit", 1], ["Saturation of active sites", 1], ["Denaturation above ~50 °C", 1], ["Competitive: resembles substrate, binds active site", 1], ["More substrate overcomes the inhibition", 1], ["Covalent, permanent inactivation", 1], ["Platelets cannot make new COX", 1]]}]})
