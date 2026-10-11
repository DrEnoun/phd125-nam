"""PHD125 Chapter 7 · Amino Acids, Proteins and Enzymes · lecture slide content.
Sources: FGOB 18.1-18.10 and 19.2-19.7 (remixed from Ball, Hill & Scott, chapter 18), LibreTexts, CC BY-NC-SA 3.0.
Original material by Dr. NAM: protein hydrolysis conditions (FGOB 18.10 gives headings only), what enzymes do as catalysts
(FGOB 19.1 is empty), electrophoresis, the pharmacy links (amino acid and peptide drugs, protein storage, enzyme-inhibitor
drugs, enzyme medicines). Protein and enzyme schematics are drawn by _src/proteinfigs.py."""
from figs import mol, row, scheme, stack
from sugars import fischer_row
from proteinfigs import tertiary, enzyme_models, rate_curves, inhibition, feedback

LO1, LO2, LO3, LO4, LO5 = 'CH7-LO1', 'CH7-LO2', 'CH7-LO3', 'CH7-LO4', 'CH7-LO5'

ACID = ('[CX3](=O)[OX1H0-,OX2H1]', 'acid')
AMINE = ('[$([NX3;H2;!$(NC=O)]),$([NX4+;H3])]', 'amine')
AMIDE = ('[NX3][CX3](=O)', 'amide')
ASPARTAME = 'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O'

META = {
    "code": "CH7", "chapter": "Chapter 7", "title": "Amino Acids, Proteins and Enzymes", "short": "Amino Acids, Proteins, Enzymes",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: FGOB 18.1–18.10 and 19.2–19.7 (adapted from Ball, Hill & Scott, chapter 18)",
    "attrib": ("Adapted from <i>Fundamentals of General Organic and Biological Chemistry</i> 18.1–18.10 and 19.2–19.7 (remixed from Ball, Hill &amp; Scott, "
               "<i>The Basics of GOB Chemistry</i>, chapter 18), LibreTexts, CC BY-NC-SA 3.0. Protein hydrolysis conditions, enzymes as catalysts, "
               "electrophoresis and the pharmacy links are original material by Dr. NAM. Structures drawn with RDKit; protein and enzyme schematics by Dr. NAM. "
               "Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["glycine", "alanine", "water"], "2": ["alanine", "glycine", "serine"], "3": ["glycine", "alanine", "water"],
               "4": ["glycylglycine", "alanine", "glycine"], "5": ["glycylglycine", "water", "alanine"], "6": ["glycylglycine", "ethanol", "water"],
               "7": ["urea", "glycine", "water"]},
    "titlemol": ["alanine", "glycine", "glycylglycine", "serine"], "darkmol": "alanine",
    "next": "Next chapter: Application of Chromatographic Methods in Pharmaceutical Analysis",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Describe the structure of amino acids, classify them by their side chains, and explain why they are L and chiral"],
    [LO2, "Explain the acid–base behaviour of amino acids: zwitterions, the effect of pH and the isoelectric point"],
    [LO3, "Describe how peptide bonds form, and write and interpret peptide sequences"],
    [LO4, "Describe the four levels of protein structure, and explain protein hydrolysis and denaturation"],
    [LO5, "Explain how enzymes work, the factors that affect their activity, and how inhibitors (including drugs) act"],
]


def aa(smi, w=200, h=120):
    return mol(smi, w, h, highlight=[ACID, AMINE])


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Amino Acids, Proteins and Enzymes", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 7",
         "notes": "Chapter 7, taught in two lectures (Part I: 7.1–7.4; Part II: 7.5–7.7) but kept as one deck, as requested."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1: 7.1–7.2. LO2: 7.3. LO3: 7.4. LO4: 7.5–7.6. LO5: 7.7."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>Part I</b>: <b>7.1 Introduction</b> · <b>7.2 Amino Acids</b> · <b>7.3 Acid–Base Behaviour</b> · <b>7.4 Peptides</b> (FGOB 18.1–18.5)",
        "<b>Part II</b>: <b>7.5 Proteins</b> · <b>7.6 Hydrolysis and Denaturation</b> · <b>7.7 Enzymes</b> (FGOB 18.6–18.10, 19.2–19.7)",
        "Links back: amines and carboxylic acids (Chapter 4) make amino acids; the amide bond (Chapter 4) is the peptide bond; chirality (Chapter 5); disulfides (Chapter 3).",
        "Lab Practical 3 (Enzyme) puts 7.7 into practice."],
         "notes": "Lesson plan: Part I week 11, Part II week 12."})
    add({"t": "hook", "title": "Think first",
         "q": "Insulin injections, a hair perm, a fried egg, the fingerprint powder used by police, and a statin tablet. Where is the chemistry of this chapter in each one?",
         "a": "<b>Insulin</b> is a protein of 51 amino acids. A <b>perm</b> breaks and re-forms disulfide bridges in hair keratin. <b>Frying</b> denatures egg-white protein. <b>Ninhydrin</b> turns amino acids in fingerprints purple. A <b>statin</b> inhibits an enzyme. All of it rests on amino acids joined by amide (peptide) bonds.",
         "notes": "Pairs discuss for one minute."})

    # ================= 7.1 INTRODUCTION =================
    add({"t": "divider", "num": 1, "title": "Introduction", "lo": "CH7-LO1", "src": "FGOB 18.1–18.2",
         "blurb": "Proteins do almost every job in the cell. All of them are built from the same 20 amino acids."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "Proteins: the most versatile biomolecules",
         "items": ["The four main kinds of biomolecule: <b>carbohydrates</b> (Chapter 5), <b>lipids</b> (Chapter 6), <b>proteins</b> and <b>nucleic acids</b>.",
                   "Proteins are more than <b>50%</b> of the dry mass of a cell; the human body has over a million different kinds.",
                   "Each is a polymer of amino acids with its own sequence, usually 6 000 to 1 000 000 g/mol.",
                   "<b>Fibrous</b> proteins: long parallel chains, tough and insoluble (hair, tendons). <b>Globular</b>: folded into compact, water-soluble shapes (enzymes, antibodies, haemoglobin). <b>Membrane</b> proteins sit in the lipid bilayer (Chapter 6)."],
         "notes": "FGOB 18.1–18.2."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "What proteins do",
         "head": ["Type", "Function", "Example"],
         "rows": [["enzymes", "catalyse biochemical reactions", "amylase digests starch"],
                  ["hormones", "regulate and coordinate cell functions", "insulin controls blood glucose"],
                  ["storage", "store and release substances", "myoglobin stores O<sub>2</sub> in muscle"],
                  ["transport", "carry substances through the body", "haemoglobin carries O<sub>2</sub>"],
                  ["structural", "shape and support", "keratin (hair, nails), collagen"],
                  ["defence", "protect against invaders", "immunoglobulins (antibodies)"],
                  ["contractile", "movement", "actin and myosin in muscle"]],
         "widths": [2.0, 4.0, 4.0],
         "caption": "Many medicines are proteins too: insulin, vaccines' antigens, and monoclonal antibodies. Source: FGOB Table 18.2.1.",
         "notes": "FGOB 18.2 table; medicines note original."})

    # ================= 7.2 AMINO ACIDS =================
    add({"t": "divider", "num": 2, "title": "Amino Acids", "lo": "CH7-LO1", "src": "FGOB 18.3",
         "blurb": "An amine and a carboxylic acid on the same carbon, plus a side chain that gives each one its character."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO1, "title": "The α-amino acid",
         "fig": {"cap": "–NH<sub>2</sub> (blue shading) and –COOH (red shading) on the same carbon, the α-carbon.",
                 "data": row([(aa('NCC(=O)O'), "glycine (R = H)"), (aa('N[C@@H](C)C(=O)O'), "alanine (R = CH₃)"), (aa('N[C@@H](CO)C(=O)O'), "serine (R = CH₂OH)"), (aa('N[C@@H](Cc1ccccc1)C(=O)O', 230), "phenylalanine")], w=230, h=130)},
         "items": ["Every amino acid has an <b>amino group</b>, a <b>carboxyl group</b>, an H and a <b>side chain (R)</b>, all on the <b>α-carbon</b>.",
                   "The amine and carboxylic acid are the groups from Chapter 4, so amino acids are both bases and acids (7.3).",
                   "Only the R group differs. It sets the size, shape, polarity and charge of each amino acid."],
         "notes": "FGOB 18.3."})
    add({"t": "table", "sec": 2, "lo": LO1, "title": "Amino acids with nonpolar side chains",
         "head": ["Name", "Codes", "Side chain (R)", "Note"],
         "rows": [["glycine", "Gly, G", "–H", "simplest; not chiral"], ["alanine", "Ala, A", "–CH<sub>3</sub>", ""],
                  ["valine", "Val, V", "–CH(CH<sub>3</sub>)<sub>2</sub>", "essential"], ["leucine", "Leu, L", "–CH<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub>", "essential"],
                  ["isoleucine", "Ile, I", "–CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub>", "essential"], ["phenylalanine", "Phe, F", "–CH<sub>2</sub>C<sub>6</sub>H<sub>5</sub>", "essential; avoid in PKU"],
                  ["tryptophan", "Trp, W", "–CH<sub>2</sub>–indole ring", "essential"], ["methionine", "Met, M", "–CH<sub>2</sub>CH<sub>2</sub>SCH<sub>3</sub>", "essential"],
                  ["proline", "Pro, P", "ring joined back to the N", "a secondary amine"]],
         "widths": [2.2, 1.4, 3.8, 2.6],
         "caption": "Nonpolar side chains are hydrophobic: they end up inside folded proteins, away from water. Source: FGOB Table 18.3.1.",
         "notes": "FGOB 18.3 table."})
    add({"t": "table", "sec": 2, "lo": LO1, "title": "Polar, acidic and basic side chains",
         "head": ["Class", "Name (codes)", "Side chain (R)"],
         "rows": [["polar, uncharged", "serine (Ser, S); threonine (Thr, T)", "–CH<sub>2</sub>OH; –CH(OH)CH<sub>3</sub>"],
                  ["", "cysteine (Cys, C)", "–CH<sub>2</sub><b>SH</b> (forms disulfides)"],
                  ["", "tyrosine (Tyr, Y)", "–CH<sub>2</sub>C<sub>6</sub>H<sub>4</sub>OH (a phenol)"],
                  ["", "asparagine (Asn, N); glutamine (Gln, Q)", "–CH<sub>2</sub>CONH<sub>2</sub>; –CH<sub>2</sub>CH<sub>2</sub>CONH<sub>2</sub> (amides)"],
                  ["<b>acidic</b> (– at pH 7)", "aspartic acid (Asp, D); glutamic acid (Glu, E)", "–CH<sub>2</sub>COOH; –CH<sub>2</sub>CH<sub>2</sub>COOH"],
                  ["<b>basic</b> (+ at pH 7)", "lysine (Lys, K)", "–(CH<sub>2</sub>)<sub>4</sub>NH<sub>2</sub>"],
                  ["", "arginine (Arg, R); histidine (His, H)", "guanidino group; imidazole ring"]],
         "widths": [2.4, 4.0, 4.0],
         "caption": "Three-letter codes are mostly the first three letters; one-letter codes are mostly the first letter (F = Phe, W = Trp, R = Arg). Source: FGOB Table 18.3.1.",
         "notes": "FGOB 18.3."})
    add({"t": "bullets", "sec": 2, "lo": LO1, "title": "Essential amino acids",
         "items": ["We can make about half of the 20 amino acids. The <b>essential</b> ones must come from food.",
                   "The nine essential amino acids for adults: <b>His, Ile, Leu, Lys, Met, Phe, Thr, Trp, Val</b>.",
                   "\"Complete\" proteins (meat, fish, eggs, soy) contain all nine; many single plant foods are low in one (rice in lysine), so combining foods helps.",
                   "<b>Pharmacy</b>: amino acid infusions for parenteral (IV) nutrition; amino acid drugs and derivatives such as <b>levodopa</b> (Parkinson's) and <b>levothyroxine</b> (a tyrosine derivative)."],
         "notes": "FGOB 18.3 (about half are essential); list and pharmacy links original."})
    add({"t": "figure", "pos": "leftwide", "sec": 2, "lo": LO1, "title": "Amino acids are chiral: L and D",
         "fig": {"cap": "Fischer projections of alanine. Proteins use only the L form.",
                 "data": fischer_row([('COO⁻', [('H₃N⁺', 'H')], 'CH₃', 'L-alanine', 0), ('COO⁻', [('H', 'NH₃⁺')], 'CH₃', 'D-alanine', 0)])},
         "items": ["The α-carbon has four different groups (except in <b>glycine</b>, R = H), so amino acids are <b>chiral</b> (Chapter 5).",
                   "Fischer projection with COO<sup>−</sup> at the top: NH<sub>3</sub><sup>+</sup> on the <b>left</b> = <b>L</b>; on the right = D.",
                   "All amino acids in human proteins are <b>L</b>. (Natural sugars, by contrast, are D.)",
                   "Some bacteria use D-amino acids in their cell walls, which is part of how antibiotics such as vancomycin target them."],
         "notes": "FGOB 18.3; vancomycin note original."})
    add({"t": "check", "sec": 2, "lo": LO1, "title": "Quick check",
         "q": "Which amino acid has no chiral carbon?",
         "opts": ["glycine", "alanine", "serine", "cysteine"], "ans": 0,
         "why": "Its α-carbon carries two H atoms.", "notes": "Answer A."})
    add({"t": "check", "sec": 2, "lo": LO1, "title": "Quick check",
         "q": "Which amino acid has an acidic side chain?",
         "opts": ["glutamic acid", "lysine", "leucine", "serine"], "ans": 0,
         "why": "–CH<sub>2</sub>CH<sub>2</sub>COOH, negatively charged at pH 7.", "notes": "Answer A."})

    # ================= 7.3 ACID-BASE BEHAVIOUR =================
    add({"t": "divider", "num": 3, "title": "Acid–Base Behaviour of Amino Acids", "lo": "CH7-LO2", "src": "FGOB 18.4",
         "blurb": "An internal salt: the acid gives its proton to the amine on the same molecule."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO2, "title": "Zwitterions",
         "fig": {"cap": "In water near pH 6, glycine exists as a zwitterion: +NH<sub>3</sub> and –COO<sup>−</sup> on one molecule.",
                 "data": scheme([('m', 'NCC(=O)O', 'glycine (drawn neutral)', 170), ('>', 'internal H⁺ transfer', ''), ('m', '[NH3+]CC(=O)[O-]', 'glycine zwitterion', 190)], h=120)},
         "items": ["The –COOH (acid) gives H<sup>+</sup> to the –NH<sub>2</sub> (base) of the <b>same</b> molecule: a <b>zwitterion</b> (German, \"hybrid ion\").",
                   "It has both charges but is neutral overall.",
                   "That is why amino acids are crystalline solids with high melting points and dissolve in water, but not in nonpolar solvents: they behave like salts."],
         "notes": "FGOB 18.4; properties original."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO2, "title": "The effect of pH",
         "fig": {"cap": "Glycine in acid, at its isoelectric point, and in base.",
                 "data": scheme([('m', '[NH3+]CC(=O)O', 'low pH: cation (+1)', 180), ('>', '+ OH⁻', '+ H⁺'), ('m', '[NH3+]CC(=O)[O-]', 'pI ≈ 6: zwitterion (0)', 190), ('>', '+ OH⁻', '+ H⁺'), ('m', 'NCC(=O)[O-]', 'high pH: anion (−1)', 170)], h=120)},
         "items": ["<b>Add acid</b>: –COO<sup>−</sup> picks up H<sup>+</sup> → the amino acid becomes <b>positive</b>.",
                   "<b>Add base</b>: –NH<sub>3</sub><sup>+</sup> loses H<sup>+</sup> → it becomes <b>negative</b>.",
                   "Either way it removes the added H<sup>+</sup> or OH<sup>−</sup>, so amino acids and proteins act as <b>buffers</b> in the body."],
         "notes": "FGOB 18.4."})
    add({"t": "table", "sec": 3, "lo": LO2, "title": "The isoelectric point (pI)",
         "head": ["Amino acid", "Side chain", "pI"],
         "rows": [["alanine, valine", "nonpolar", "6.0"], ["serine", "polar, uncharged", "5.7"], ["threonine", "polar, uncharged", "6.5"],
                  ["aspartic acid", "acidic", "3.0"], ["glutamic acid", "acidic", "3.2"],
                  ["histidine", "basic", "7.6"], ["lysine", "basic", "9.8"], ["arginine", "basic", "10.8"]],
         "widths": [3.0, 3.0, 1.6],
         "caption": "The <b>pI</b> is the pH at which the amino acid is a zwitterion with no net charge. Neutral side chains: pI 5.0–6.5; acidic: low; basic: high. Below its pI an amino acid is positive; above it, negative. Source: FGOB Table 18.4.1.",
         "notes": "FGOB 18.4."})
    add({"t": "bullets", "sec": 3, "lo": LO2, "title": "Using charge: electrophoresis and ninhydrin",
         "items": ["<b>Electrophoresis</b>: in an electric field at a chosen pH, positive species move to the negative electrode and negative ones to the positive electrode; at its pI a molecule does not move. This separates amino acids and proteins (blood serum protein tests).",
                   "A protein is <b>least soluble at its pI</b>, because molecules with no net charge do not repel each other. This is used to purify and precipitate proteins.",
                   "<b>Ninhydrin</b> reacts with the amino group of α-amino acids to give a <b>purple</b> colour: used to detect amino acids on TLC plates (Chapter 8) and fingerprints on paper (FGOB 18.4)."],
         "notes": "Ninhydrin: FGOB 18.4. Electrophoresis and solubility at pI original."})
    add({"t": "tryit", "sec": 3, "lo": LO2, "title": "Try it · Charge at different pH",
         "q": "Give the main form and overall charge of (a) alanine at pH 1 (b) alanine at pH 6 (c) alanine at pH 12 (d) lysine (pI 9.8) at pH 7",
         "a": "(a) <b>+1</b>: H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>3</sub>)–COOH (b) <b>0</b>: the zwitterion H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>3</sub>)–COO<sup>−</sup> (c) <b>−1</b>: H<sub>2</sub>N–CH(CH<sub>3</sub>)–COO<sup>−</sup> (d) <b>positive</b>: pH 7 is below its pI, so the side-chain –NH<sub>3</sub><sup>+</sup> keeps its charge.",
         "notes": "Original, applying FGOB 18.4."})
    add({"t": "check", "sec": 3, "lo": LO2, "title": "Quick check",
         "q": "At pH 2, aspartic acid (pI 3.0) carries a net charge that is:",
         "opts": ["positive", "negative", "zero", "it depends on temperature only"], "ans": 0,
         "why": "Below the pI → net positive.", "notes": "Answer A."})

    # ================= 7.4 PEPTIDES =================
    add({"t": "divider", "num": 4, "title": "Peptides", "lo": "CH7-LO3", "src": "FGOB 18.5",
         "blurb": "Amino acids joined head to tail by amide bonds, in a sequence that decides everything."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO3, "title": "The peptide bond",
         "fig": {"cap": "Glycine + alanine → glycylalanine (Gly-Ala) + water. The new C–N amide bond (green) is the peptide bond.",
                 "data": scheme([('m', 'NCC(=O)O', 'glycine', 140), ('+',), ('m', 'N[C@@H](C)C(=O)O', 'alanine', 150), ('>', '− H₂O', ''), ('m', 'NCC(=O)N[C@@H](C)C(=O)O', 'Gly-Ala (a dipeptide)', 230), ('+',), ('t', 'H₂O', 60)], h=120)},
         "items": ["The –COOH of one amino acid and the –NH<sub>2</sub> of the next form an <b>amide</b>, losing water: a condensation (Chapter 4).",
                   "The product still has a free –NH<sub>2</sub> at one end and a free –COOH at the other, so the chain can keep growing.",
                   "Dipeptide (2), tripeptide (3), polypeptide; about 50 or more units is usually called a <b>protein</b>. Each unit in a chain is a <b>residue</b>."],
         "notes": "FGOB 18.5."})
    add({"t": "bullets", "sec": 4, "lo": LO3, "title": "Writing peptides: N-terminal to C-terminal",
         "items": ["By convention a peptide is written with the <b>N-terminal</b> amino acid (free –NH<sub>3</sub><sup>+</sup>) on the <b>left</b> and the <b>C-terminal</b> (free –COO<sup>−</sup>) on the <b>right</b>.",
                   "So <b>Gly-Ala</b> and <b>Ala-Gly</b> are different compounds (isomers).",
                   "Three different amino acids can make 3! = <b>6</b> different tripeptides; 20 amino acids allow 20<sup>n</sup> sequences for a chain of n.",
                   "Example: in Lys-Val-Phe-Gly-Arg-Cys, Lys is N-terminal and Cys is C-terminal (FGOB 18.5)."],
         "notes": "FGOB 18.5; counting original."})
    add({"t": "two", "sec": 4, "lo": LO3, "title": "Sequence decides function",
         "lead": "Like letters in a word: the same amino acids in a different order give a different molecule.",
         "cols": [{"h": "Bradykinin", "tone": "cold", "items": [
             "A nine-residue peptide in blood: Arg-Pro-Pro-Gly-Phe-Ser-Pro-Phe-Arg",
             "Lowers blood pressure, increases capillary permeability, causes pain",
             "The same residues in reverse order have <b>none</b> of this activity"]},
             {"h": "Sickle cell anaemia", "tone": "heat", "items": [
                 "One wrong residue in the haemoglobin β chain: <b>valine</b> replaces <b>glutamic acid</b>",
                 "A nonpolar residue where a charged one should be makes haemoglobin stick together in long fibres",
                 "Red cells become sickle-shaped and block small blood vessels"]}],
         "notes": "FGOB 18.5; Glu→Val mechanism simplified (original)."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO3, "title": "Peptides as medicines",
         "fig": {"cap": "Aspartame: Asp-Phe methyl ester, a dipeptide sweetener about 180–200 times sweeter than sucrose.",
                 "data": mol(ASPARTAME, 460, 200, highlight=[AMIDE])},
         "items": ["<b>Insulin</b>: 51 residues in two chains joined by disulfide bridges; injected for diabetes.",
                   "<b>Oxytocin</b> (9 residues) induces labour; <b>GLP-1 analogues</b> (semaglutide) treat diabetes and obesity.",
                   "Most peptide drugs are <b>injected</b>, because digestive enzymes (proteases) would hydrolyse them in the gut.",
                   "Aspartame releases phenylalanine, so products carry a warning for people with <b>phenylketonuria (PKU)</b>."],
         "notes": "Original pharmacy links; aspartame sweetness from Ball 16.3 (Chapter 5)."})
    add({"t": "tryit", "sec": 4, "lo": LO3, "title": "Try it · Peptides",
         "q": "(a) Draw the dipeptide Ala-Gly and circle the peptide bond (b) Identify the N- and C-terminal amino acids of Asp-Arg-Val-Tyr-Ile-His-Pro-Phe (c) How many different tripeptides can be made using one each of Gly, Ala and Ser?",
         "a": "(a) H<sub>2</sub>N–CH(CH<sub>3</sub>)–<b>CO–NH</b>–CH<sub>2</sub>–COOH (alanine's –COOH is joined to glycine's –NH<sub>2</sub>) (b) N-terminal: <b>Asp</b>; C-terminal: <b>Phe</b> (FGOB 18.5) (c) <b>6</b>: Gly-Ala-Ser, Gly-Ser-Ala, Ala-Gly-Ser, Ala-Ser-Gly, Ser-Gly-Ala, Ser-Ala-Gly.",
         "afig": {"data": mol('N[C@@H](C)C(=O)NCC(=O)O', 300, 120, highlight=[AMIDE])},
         "notes": "FGOB 18.5 exercises 2 and 4 (adapted); (c) original."})
    add({"t": "check", "sec": 4, "lo": LO3, "title": "Quick check",
         "q": "The peptide bond is the same functional group as a(n):",
         "opts": ["amide", "ester", "ether", "amine salt"], "ans": 0,
         "why": "–CO–NH– (Chapter 4).", "notes": "Answer A."})

    # ================= 7.5 PROTEINS =================
    add({"t": "divider", "num": 5, "title": "Proteins", "lo": "CH7-LO4", "src": "FGOB 18.6–18.9",
         "blurb": "Four levels of structure: the sequence, local folding, the whole 3D shape, and how several chains fit together."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO4, "title": "Four levels of protein structure",
         "fig": {"cap": "1° sequence (peptide bonds) → 2° α-helix, β-sheet (backbone H-bonds) → 3° one chain in 3D (side chains) → 4° subunits. Image supplied by Dr. NAM; tap to zoom.", "data": "../../img/ch7/protein-levels.jpg"},
         "items": [],
         "notes": "FGOB 18.6–18.9. Figure supplied by Dr. NAM (replaces the earlier schematic)."})
    add({"t": "two", "sec": 5, "lo": LO4, "title": "Secondary structure",
         "lead": "Linus Pauling and Robert Corey used X-ray data to describe two regular shapes of the backbone.",
         "cols": [{"h": "α-Helix", "tone": "cold", "items": [
             "A right-handed coil, <b>3.6</b> residues per turn",
             "Each C=O hydrogen bonds to the N–H four residues along, <b>within the same chain</b>",
             "Side chains point outwards",
             "α-Keratin in hair and wool is all α-helix"]},
             {"h": "β-Pleated sheet", "tone": "heat", "items": [
                 "Extended chains lying <b>side by side</b>, parallel or antiparallel",
                 "Hydrogen bonds <b>between</b> neighbouring chains",
                 "Side chains alternate above and below the sheet",
                 "Silk fibroin; parts of many enzymes"]}],
         "notes": "FGOB 18.7."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO4, "title": "Tertiary structure: what holds the fold",
         "fig": {"cap": "Four interactions between side chains.", "data": tertiary()},
         "items": ["<b>Ionic bonds</b>: between charged side chains, e.g. Asp<sup>−</sup> and Lys<sup>+</sup>.",
                   "<b>Hydrogen bonds</b>: between polar side chains (–OH, –NH, C=O).",
                   "<b>Disulfide bridges</b>: two cysteine –SH groups oxidised to –S–S– (Chapter 3). Strong covalent links; insulin has three.",
                   "<b>Dispersion forces / hydrophobic interactions</b>: nonpolar side chains cluster inside, away from water."],
         "notes": "FGOB 18.8."})
    add({"t": "bullets", "sec": 5, "lo": LO4, "title": "Quaternary structure, fibrous and globular",
         "items": ["<b>Haemoglobin</b>: four chains (two α, two β), each carrying a haem group that binds O<sub>2</sub>. Held together by the same forces as tertiary structure.",
                   "Insulin has two chains linked by disulfides; antibodies have four.",
                   "<b>Fibrous</b> proteins (keratin, collagen, silk) are long and tough; <b>globular</b> proteins (enzymes, haemoglobin, insulin) fold into compact soluble balls.",
                   "Shape decides function: a protein that loses its shape loses its job (7.6)."],
         "notes": "FGOB 18.9; insulin and antibody details original."})
    add({"t": "check", "sec": 5, "lo": LO4, "title": "Quick check",
         "q": "An α-helix is held together mainly by:",
         "opts": ["hydrogen bonds between backbone C=O and N–H groups", "disulfide bridges", "peptide bonds only", "ionic bonds between side chains"], "ans": 0,
         "why": "Within the same chain, four residues apart.", "notes": "Answer A."})
    add({"t": "check", "sec": 5, "lo": LO4, "title": "Quick check",
         "q": "Which level of structure does haemoglobin have that myoglobin (one chain) does not?",
         "opts": ["quaternary", "primary", "secondary", "tertiary"], "ans": 0,
         "why": "Four subunits fitted together.", "notes": "Answer A."})

    # ================= 7.6 HYDROLYSIS & DENATURATION =================
    add({"t": "divider", "num": 6, "title": "Protein Hydrolysis and Denaturation", "lo": "CH7-LO4", "src": "FGOB 18.10",
         "blurb": "Two ways to destroy a protein: break the peptide bonds, or just unfold the shape."})
    add({"t": "figure", "pos": "top", "sec": 6, "lo": LO4, "title": "Hydrolysis: breaking peptide bonds",
         "fig": {"cap": "Gly-Ala + H<sub>2</sub>O → glycine + alanine: the reverse of peptide bond formation.",
                 "data": scheme([('m', 'NCC(=O)N[C@@H](C)C(=O)O', 'Gly-Ala', 220), ('+',), ('t', 'H₂O', 60), ('>', 'H⁺ or enzyme', ''), ('m', 'NCC(=O)O', 'glycine', 140), ('+',), ('m', 'N[C@@H](C)C(=O)O', 'alanine', 150)], h=120)},
         "items": ["Peptide (amide) bonds are very stable (Chapter 4): chemical hydrolysis needs strong acid, e.g. 6 M HCl at about 110 °C for 24 hours.",
                   "In digestion, <b>proteases</b> do it at body temperature: <b>pepsin</b> in the stomach, <b>trypsin</b> and <b>chymotrypsin</b> from the pancreas.",
                   "Complete hydrolysis gives free amino acids, which are absorbed. This is why most protein drugs cannot be swallowed."],
         "notes": "Original (FGOB 18.10 gives the heading only)."})
    add({"t": "table", "sec": 6, "lo": LO4, "title": "Denaturation: losing the shape",
         "head": ["Cause", "What it disrupts"],
         "rows": [["<b>heat</b> above about 50 °C, or UV light", "atoms vibrate faster; hydrogen bonds and dispersion forces break"],
                  ["<b>organic solvents</b> such as ethanol", "they hydrogen bond to the protein, breaking its own internal hydrogen bonds"],
                  ["<b>strong acids and bases</b> (pH change)", "change the charges on side chains, breaking ionic bonds"],
                  ["<b>heavy metal ions</b> (Hg<sup>2+</sup>, Ag<sup>+</sup>, Pb<sup>2+</sup>)", "bind –COO<sup>−</sup> and –SH groups, breaking ionic bonds and disulfides"],
                  ["<b>alkaloid reagents</b> such as tannic acid", "bind –NH<sub>3</sub><sup>+</sup> groups (used to tan leather)"]],
         "widths": [3.6, 6.2],
         "caption": "<b>Denaturation</b> changes the secondary, tertiary and quaternary structure; the <b>primary</b> structure (peptide bonds) is not broken. A fried egg white turns opaque as albumin denatures. Some gently unfolded proteins can refold (renature). Source: FGOB 18.10.",
         "notes": "FGOB 18.10 table (acid/base row added)."})
    add({"t": "bullets", "sec": 6, "lo": LO4, "title": "Denaturation in the pharmacy",
         "items": ["<b>Disinfection</b>: 70% alcohol swabs and hand rubs denature microbial proteins; <b>autoclaves</b> (121 °C steam) and boiling sterilise equipment (FGOB 19.5).",
                   "<b>Silver</b> compounds (silver sulfadiazine cream for burns) kill bacteria by binding their proteins.",
                   "<b>Storing protein medicines</b>: insulin, vaccines and antibodies are kept at 2–8 °C (the cold chain), must not be frozen, and should not be shaken hard; heat or freezing can denature them and they stop working.",
                   "Hair perms: thiols break the disulfides in keratin, the hair is reshaped, then an oxidant re-forms new disulfides (Chapter 3)."],
         "notes": "Original pharmacy links."})
    add({"t": "check", "sec": 6, "lo": LO4, "title": "Quick check",
         "q": "Which level of protein structure is NOT changed by denaturation?",
         "opts": ["primary", "secondary", "tertiary", "quaternary"], "ans": 0,
         "why": "Peptide bonds are not broken; hydrolysis is needed for that.", "notes": "Answer A."})
    add({"t": "check", "sec": 6, "lo": LO4, "title": "Quick check",
         "q": "Why must insulin vials not be left in a hot car?",
         "opts": ["Heat denatures the protein, so it stops working", "Heat hydrolyses it to glucose", "Heat makes it a lipid", "Insulin evaporates"], "ans": 0,
         "why": "Store at 2–8 °C (in-use vials at room temperature for a limited time).", "notes": "Answer A."})

    # ================= 7.7 ENZYMES =================
    add({"t": "divider", "num": 7, "title": "Enzymes", "lo": "CH7-LO5", "src": "FGOB 19.2–19.7 (19.1 is empty)",
         "blurb": "Protein catalysts: how they work, what slows them down, and how many drugs work by blocking them."})
    add({"t": "bullets", "sec": 7, "lo": LO5, "title": "Enzymes are biological catalysts",
         "items": ["A <b>catalyst</b> speeds up a reaction without being used up, by lowering the <b>activation energy</b>. It does not change the products or the equilibrium.",
                   "Enzymes can speed reactions by a factor of a million or more, at 37 °C and near pH 7.",
                   "They are very <b>specific</b>: <b>urease</b> hydrolyses only urea; others act on a group of similar molecules; some tell D from L isomers.",
                   "Most enzymes are globular proteins, so anything that denatures proteins also destroys enzyme activity."],
         "notes": "Original (FGOB 19.1 is empty); urease and specificity from FGOB 19.4."})
    add({"t": "table", "sec": 7, "lo": LO5, "title": "Naming and classifying enzymes",
         "head": ["Class", "Reaction catalysed", "Example"],
         "rows": [["1 <b>oxidoreductases</b>", "oxidation–reduction", "alcohol dehydrogenase (Chapter 3)"],
                  ["2 <b>transferases</b>", "move a group (amino, phosphate) to another molecule", "transaminases; kinases"],
                  ["3 <b>hydrolases</b>", "break bonds with water", "lipases, proteases, amylases, nucleases"],
                  ["4 <b>lyases</b>", "add or remove groups without water (e.g. –CO<sub>2</sub>)", "decarboxylases; fumarase"],
                  ["5 <b>isomerases</b>", "convert a compound to its isomer", "triose phosphate isomerase"],
                  ["6 <b>ligases</b>", "join two molecules, using ATP", "pyruvate carboxylase"]],
         "widths": [2.8, 4.2, 3.4],
         "caption": "Most enzyme names end in <b>-ase</b> and say what they act on and what they do: alcohol de-hydrogen-ase removes H from alcohols. Older names (pepsin, papain from papaya) do not. Each enzyme has an EC number: alcohol dehydrogenase is EC 1.1.1.1. Source: FGOB 19.3.",
         "notes": "FGOB 19.3."})
    add({"t": "table", "sec": 7, "lo": LO5, "title": "Cofactors and vitamins",
         "head": ["Vitamin", "Coenzyme or role", "Deficiency"],
         "rows": [["B<sub>1</sub> thiamine", "thiamine pyrophosphate (decarboxylation)", "beriberi"],
                  ["B<sub>2</sub> riboflavin", "FMN, FAD (redox)", "—"],
                  ["B<sub>3</sub> niacin", "NAD<sup>+</sup>, NADP<sup>+</sup> (redox)", "pellagra"],
                  ["B<sub>12</sub> cobalamin", "rearrangements", "pernicious anaemia"],
                  ["folic acid", "tetrahydrofolate (one-carbon groups)", "anaemia"],
                  ["C ascorbic acid", "antioxidant; collagen formation", "scurvy"],
                  ["A, D, E, K (fat-soluble)", "vision; Ca<sup>2+</sup> absorption; antioxidant; blood clotting", "night blindness; rickets; —; slow clotting"]],
         "widths": [2.6, 4.6, 2.8],
         "caption": "Some enzymes need a non-protein <b>cofactor</b>: a metal ion (Zn<sup>2+</sup>, Cu<sup>+</sup>) or an organic <b>coenzyme</b>, usually made from a water-soluble vitamin. Source: FGOB 19.2.",
         "notes": "FGOB 19.2 tables (condensed)."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO5, "title": "How enzymes work",
         "fig": {"cap": "E + S ⇌ ES → E + P", "data": enzyme_models()},
         "items": ["The substrate (S) binds the <b>active site</b>, a pocket on the enzyme, forming an <b>enzyme–substrate complex</b> (ES), held by hydrogen bonds and ionic attractions.",
                   "<b>Lock and key</b>: a rigid active site that fits only its substrate. <b>Induced fit</b> (the current model): the site changes shape as the substrate binds (hexokinase and glucose).",
                   "Side chains in the active site act as acids, bases or binding groups; the product (P) leaves and the enzyme is free to work again."],
         "notes": "FGOB 19.4."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO5, "title": "Factors that affect enzyme activity",
         "fig": {"cap": "Rate against substrate concentration, temperature and pH.", "data": rate_curves()},
         "items": ["<b>[Substrate]</b>: rate rises, then levels off when every active site is busy (saturation; like a fixed number of taxis). <b>[Enzyme]</b>: rate rises in proportion when substrate is in excess.",
                   "<b>Temperature</b>: rate roughly doubles every 10 °C, until the enzyme <b>denatures</b> (often 45–55 °C). Fridges slow enzymes; boiling destroys them.",
                   "<b>pH</b>: each enzyme has an <b>optimum pH</b>, usually 6–8; pepsin works best at about pH 2 in the stomach."],
         "notes": "FGOB 19.5. Trypsin optimum about 8 (original)."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO5, "title": "Reversible inhibition",
         "fig": {"cap": "Malonate (−OOC–CH<sub>2</sub>–COO−) mimics succinate (−OOC–CH<sub>2</sub>CH<sub>2</sub>–COO−) and competes for succinate dehydrogenase (FGOB 19.6).", "data": inhibition()},
         "items": ["<b>Competitive</b>: the inhibitor looks like the substrate and binds the <b>active site</b>. Raising [substrate] can win back the normal maximum rate.",
                   "<b>Noncompetitive</b>: the inhibitor binds <b>elsewhere</b> and changes the shape of the active site; more substrate does not help.",
                   "Reversible inhibitors bind without covalent bonds and can come off again."],
         "notes": "FGOB 19.6 (uncompetitive inhibition is mentioned in the source but not needed at this level)."})
    add({"t": "bullets", "sec": 7, "lo": LO5, "title": "Irreversible inhibition",
         "items": ["An <b>irreversible</b> inhibitor forms a <b>covalent bond</b> with a group in the active site, so the enzyme is permanently inactivated.",
                   "Nerve gases and organophosphate insecticides (such as DIFP) bond to a <b>serine</b> in <b>acetylcholinesterase</b>: nerve signals cannot be switched off (FGOB 19.6).",
                   "Other poisons: arsenate, iodoacetate (binds a cysteine). Heavy metals such as Hg<sup>2+</sup> bind –SH groups.",
                   "<b>Aspirin</b> is an irreversible inhibitor too: it transfers its acetyl group to a serine in COX. Platelets cannot make new COX, so one low dose protects against clots for days."],
         "notes": "FGOB 19.6 table; aspirin mechanism original."})
    add({"t": "table", "sec": 7, "lo": LO5, "title": "Drugs that are enzyme inhibitors",
         "head": ["Drug", "Enzyme blocked", "Use"],
         "rows": [["simvastatin, atorvastatin", "HMG-CoA reductase (competitive)", "lower cholesterol (Chapter 6)"],
                  ["captopril, enalapril", "angiotensin-converting enzyme (ACE)", "high blood pressure"],
                  ["penicillins", "bacterial transpeptidase (irreversible)", "bacterial infections"],
                  ["allopurinol", "xanthine oxidase", "gout (less uric acid)"],
                  ["methotrexate", "dihydrofolate reductase (competitive)", "cancer, rheumatoid arthritis"],
                  ["neostigmine", "acetylcholinesterase (reversible)", "myasthenia gravis"],
                  ["fomepizole", "alcohol dehydrogenase (competitive)", "methanol poisoning (Chapter 3)"]],
         "widths": [3.0, 4.0, 3.2],
         "caption": "Drug designers copy the shape of the natural substrate, then change it so the enzyme cannot turn it into product, just as malonate mimics succinate. FGOB 19.6 notes that many drugs work this way, including HIV medicines.",
         "notes": "Original pharmacy table built on FGOB 19.3, 19.6."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO5, "title": "Allosteric control and feedback inhibition",
         "fig": {"cap": "In bacteria, isoleucine (D) switches off threonine deaminase (enzyme 1) when enough has been made (FGOB 19.7).", "data": feedback()},
         "items": ["<b>Allosteric enzymes</b> have a second, regulatory site. An <b>activator</b> binding there opens up the active site; an <b>inhibitor</b> closes it.",
                   "<b>Feedback inhibition</b>: the final product of a pathway inhibits the first enzyme, so the cell does not waste materials and energy.",
                   "Like an assembly line telling the first worker to slow down when the boxes pile up."],
         "notes": "FGOB 19.7."})
    add({"t": "bullets", "sec": 7, "lo": LO5, "title": "Enzymes as medicines and tools",
         "items": ["<b>Pancreatic enzymes</b> (pancreatin: lipase, protease, amylase) for patients who cannot make their own, such as in cystic fibrosis.",
                   "<b>Lactase</b> tablets for lactose intolerance (Chapter 5).",
                   "<b>Alteplase</b> (clot-busting enzyme) after a heart attack or stroke.",
                   "<b>Diagnostics</b>: glucose oxidase in glucometer strips (Chapter 5); raised blood levels of enzymes such as the liver transaminases (ALT, AST) signal tissue damage."],
         "notes": "Original pharmacy links."})
    add({"t": "check", "sec": 7, "lo": LO5, "title": "Quick check",
         "q": "Increasing [substrate] restores the normal maximum rate when an enzyme is blocked by a:",
         "opts": ["competitive inhibitor", "noncompetitive inhibitor", "irreversible inhibitor", "heavy metal ion"], "ans": 0,
         "why": "Substrate and inhibitor compete for the same site.", "notes": "Answer A."})
    add({"t": "check", "sec": 7, "lo": LO5, "title": "Quick check",
         "q": "Pepsin works in the stomach. Its optimum pH is about:",
         "opts": ["2", "7", "9", "12"], "ans": 0,
         "why": "Most enzymes prefer pH 6–8; pepsin is an exception.", "notes": "Answer A."})

    # ================= wrap-up =================
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Amino acids", "–NH<sub>2</sub> + –COOH + R on the α-carbon; 20 in proteins; 9 essential; all L (Gly not chiral)"],
        ["Acid–base", "zwitterion; + below pI, − above; pI: acidic low, basic high; buffers; ninhydrin purple"],
        ["Peptides", "amide (peptide) bond, −H<sub>2</sub>O; written N- to C-terminal; sequence decides function"],
        ["Structure", "1° sequence; 2° α-helix, β-sheet (H-bonds); 3° ionic, H-bond, S–S, hydrophobic; 4° subunits"],
        ["Hydrolysis", "breaks peptide bonds → amino acids (strong acid, or proteases)"],
        ["Denaturation", "heat, alcohol, pH, heavy metals unfold the protein; primary structure kept"],
        ["Enzymes", "-ase; six classes; cofactors and vitamins; active site; lock and key vs induced fit"],
        ["Activity and inhibition", "[S] saturates; optimum T and pH; competitive, noncompetitive, irreversible; feedback; many drugs"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 30 min)", "Attempt the Chapter 7 tutorial",
                   "Play the Chapter 7 game to find your weak outcomes", "Next chapter: Chromatographic Methods in Pharmaceutical Analysis"],
         "attrib": "Adapted from LibreTexts (FGOB, remixed from Ball, Hill &amp; Scott), CC BY-NC-SA 3.0, with original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"]})
    return S
