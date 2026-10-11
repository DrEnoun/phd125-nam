"""PHD125 Chapter 4 · Carboxylic Acid, Ester, Amines, Amide · lecture slide content.
Sources: Ball, Hill & Scott, The Basics of GOB Chemistry, chapter 15 (15.1-15.16), and FGOB 16.1-16.7 and 17.2-17.6,
LibreTexts, CC BY-NC-SA 3.0.
Original material by Dr. NAM (no usable source page: FGOB 16.6 and 17.1 are empty placeholders): acid dimers, the effect
of Cl on acidity, amide naming with N-, why amides are not basic, aspirin and paracetamol synthesis, and the pharmacy links
(drug salts, effervescent tablets, ester prodrugs, local anaesthetics, quaternary ammonium antiseptics, penicillin, sutures)."""
from figs import mol, row, scheme, stack

RING = ('c1ccccc1', 'ring')
ACID = ('[CX3](=O)[OX2H1]', 'acid')
ESTER = ('[CX3](=O)[OX2][#6]', 'ester')
AMIDE = ('[NX3][CX3](=O)', 'amide')
AMINE = ('[NX3;!$(N-C=O)]', 'amine')
OH = ('c[OX2H1]', 'oh')
HL_KEY = ('Shading: <span style="background:#FF9A7A;color:#0A1628;padding:0 4px;border-radius:4px">carboxylic acid</span> '
          '<span style="background:#FFCC40;color:#0A1628;padding:0 4px;border-radius:4px">ester</span> '
          '<span style="background:#66E0EB;color:#0A1628;padding:0 4px;border-radius:4px">amine</span> '
          '<span style="background:#8CD98C;color:#0A1628;padding:0 4px;border-radius:4px">amide</span>')

ASPIRIN = 'CC(=O)Oc1ccccc1C(=O)O'
SALICYLIC = 'OC(=O)c1ccccc1O'
PARACETAMOL = 'CC(=O)Nc1ccc(O)cc1'
AMINOPHENOL = 'Nc1ccc(O)cc1'
ANHYDRIDE = 'CC(=O)OC(C)=O'
PROCAINE = 'CCN(CC)CCOC(=O)c1ccc(N)cc1'
LIDOCAINE = 'CCN(CC)CC(=O)Nc1c(C)cccc1C'
PENICILLIN_G = 'CC1(C)S[C@@H]2[C@H](NC(=O)Cc3ccccc3)C(=O)N2[C@H]1C(=O)O'
CAFFEINE = 'Cn1cnc2c1c(=O)n(C)c(=O)n2C'
NICOTINE = 'CN1CCC[C@H]1c1cccnc1'
MORPHINE = 'CN1CC[C@]23c4c5ccc(O)c4O[C@H]2[C@@H](O)C=C[C@H]3[C@H]1C5'


def mini(smi, hs=False, h=48):
    return f'<img src="{mol(smi, 190, 84, hs=hs)}" alt="" style="height:{h}px;display:block;background:#fff;border-radius:6px;padding:1px 4px">'


LO1, LO2, LO3, LO4, LO5 = 'CH4-LO1', 'CH4-LO2', 'CH4-LO3', 'CH4-LO4', 'CH4-LO5'

META = {
    "code": "CH4", "chapter": "Chapter 4", "title": "Carboxylic Acid, Ester, Amines, Amide", "short": "Acids, Esters, Amines, Amides",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: Ball, Hill & Scott, The Basics of GOB Chemistry, chapter 15, with FGOB 16.1–16.7 and 17.2–17.6",
    "attrib": ("Adapted from <i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 15, and <i>Fundamentals of General Organic and "
               "Biological Chemistry</i> 16.1–16.7 and 17.2–17.6, LibreTexts, CC BY-NC-SA 3.0. Acid dimers, amide naming with N-, aspirin and paracetamol "
               "synthesis and the pharmacy links are original material by Dr. NAM. Structures drawn with RDKit. "
               "Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["aceticacid", "formicacid", "aspirin"], "2": ["ethylacetate", "aspirin", "aceticacid"],
               "3": ["methylamine", "trimethylamine", "ammonia"], "4": ["acetamide", "paracetamol", "urea"]},
    "titlemol": ["aceticacid", "ethylacetate", "methylamine", "acetamide"], "darkmol": "aceticacid",
    "next": "Next chapter: Carbohydrates",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Name carboxylic acids, describe how they form, and explain their boiling points and solubility"],
    [LO2, "Explain why carboxylic acids are weak acids, and write ionisation and neutralisation equations with salt names"],
    [LO3, "Name esters, and write equations for esterification and for acidic and basic hydrolysis (saponification)"],
    [LO4, "Classify and name amines, explain their properties and basicity, and describe amine salts and alkaloids"],
    [LO5, "Name amides, explain their properties, and write equations for their formation and hydrolysis"],
]


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Carboxylic Acid, Ester, Amines, Amide", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 4",
         "notes": "Chapter 4 of the course outline, in four subchapters: carboxylic acids, esters, amines and amides."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1–LO2: 4.1 Carboxylic Acids. LO3: 4.2 Esters. LO4: 4.3 Amines. LO5: 4.4 Amides."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>4.1 Carboxylic Acids</b> (Ball 15.1–15.4; FGOB 17.2): the –COOH group, names, properties, acidity and salts",
        "<b>4.2 Esters</b> (Ball 15.5–15.9; FGOB 17.3–17.4, 17.6): names, smells, esterification, hydrolysis and soap, phosphate esters",
        "<b>4.3 Amines</b> (Ball 15.10–15.12; FGOB 16.1–16.7): the organic bases: classes, names, properties, salts, alkaloids",
        "<b>4.4 Amides</b> (Ball 15.13–15.16; FGOB 17.3–17.5): acid + amine, the bond in proteins and in many drugs, nylon"],
         "notes": "One story: acids (4.1) react with alcohols to give esters (4.2) and with amines (4.3) to give amides (4.4)."})
    add({"t": "hook", "title": "Think first",
         "q": "Vinegar, the smell of ripe bananas, the smell of old fish, and a paracetamol tablet. What links them?",
         "a": "Each is one of this chapter's four families: <b>acetic acid</b> (a carboxylic acid), <b>isopentyl acetate</b> (an ester), <b>trimethylamine</b> (an amine) and <b>paracetamol</b> (an amide). Acids and amines are the organic acids and bases; esters and amides are made from them.",
         "notes": "Pairs discuss for one minute."})

    # ================= 4.1 CARBOXYLIC ACIDS =================
    add({"t": "divider", "num": 1, "title": "Carboxylic Acids", "lo": "CH4-LO1 to LO2", "src": "Ball 15.1–15.4 · FGOB 17.2",
         "blurb": "The –COOH group: how to name the acids, why they boil so high, and how they react with bases to form salts."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "The carboxyl group, –COOH",
         "fig": {"cap": "A carbonyl (C=O) and a hydroxyl (–OH) on the same carbon.",
                 "data": row([(mol("OC=O", 170, 110, highlight=[ACID]), "formic acid"), (mol("CC(=O)O", 170, 110, highlight=[ACID]), "acetic acid"),
                              (mol("OC(=O)c1ccccc1", 200, 110, highlight=[ACID]), "benzoic acid"), (mol(ASPIRIN, 220, 110, highlight=[ACID]), "aspirin")], w=230, h=110)},
         "items": ["General formula <b>RCOOH</b>. R can be H, an alkyl group or an aryl (benzene ring) group.",
                   "The C=O and O–H together behave differently from either alone: the group is <b>acidic</b>.",
                   "Fats, oils and waxes are built from long-chain carboxylic acids (Chapter 6). Many drugs carry –COOH: aspirin, ibuprofen, penicillin."],
         "notes": "Ball 15.0–15.1."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Common and IUPAC names",
         "head": ["Formula", "Common name", "Where the name comes from", "IUPAC name"],
         "rows": [["HCOOH", "formic acid", "ants (Latin <i>formica</i>); in ant and bee stings", "methanoic acid"],
                  ["CH<sub>3</sub>COOH", "acetic acid", "vinegar (Latin <i>acetum</i>), 4–10% acetic acid", "ethanoic acid"],
                  ["CH<sub>3</sub>CH<sub>2</sub>COOH", "propionic acid", "\"first fat\" (Greek)", "propanoic acid"],
                  ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH", "butyric acid", "rancid butter (Latin <i>butyrum</i>)", "butanoic acid"],
                  ["CH<sub>3</sub>(CH<sub>2</sub>)<sub>3</sub>COOH", "valeric acid", "valerian root", "pentanoic acid"],
                  ["C<sub>6</sub>H<sub>5</sub>COOH", "benzoic acid", "gum benzoin", "benzoic acid"]],
         "widths": [2.6, 1.9, 3.6, 2.0],
         "caption": "Pure acetic acid freezes at 16.6 °C into ice-like crystals, so it is called <b>glacial</b> acetic acid. Source: Ball 15.1.",
         "notes": "Ball 15.1. Name origins for propionic and valeric acids are added (original)."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Naming carboxylic acids",
         "head": ["Rule", "Example"],
         "rows": [["IUPAC: the parent is the longest chain that <b>contains the –COOH</b>. Change -e to <b>-oic acid</b>.", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>COOH is pentanoic acid"],
                  ["The carboxyl carbon is always <b>C1</b>, so it needs no number.", "ClCH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>COOH is 4-chlorobutanoic acid"],
                  ["Common names use <b>Greek letters</b> instead: the carbon next to –COOH is <b>α</b>, then β, γ, δ.", "the same compound is γ-chlorobutyric acid"],
                  ["Never mix the systems: Greek letters with common names, numbers with IUPAC names.", "α-bromobutyric acid = 2-bromobutanoic acid"]],
         "widths": [5.4, 3.8], "caption": "Note that α is C2, not C1: the Greek letters start on the carbon <b>next to</b> the carboxyl carbon. Source: Ball 15.1.",
         "notes": "Ball 15.1 Examples 1–2."})
    add({"t": "tryit", "sec": 1, "lo": LO1, "title": "Try it · Name and draw",
         "q": "(a) Name ClCH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>COOH (b) Name (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>CHBrCOOH (c) Write the condensed formula of β-chloropropionic acid",
         "a": "(a) <b>5-chloropentanoic acid</b> (b) <b>2-bromo-4-methylpentanoic acid</b> (c) <b>ClCH<sub>2</sub>CH<sub>2</sub>COOH</b>: β is the second carbon from the carboxyl carbon (Ball 15.1).",
         "notes": "Ball 15.1 exercises 1, 2 and Example 2."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Where carboxylic acids come from: oxidation",
         "fig": {"cap": "Oxidation of a 1° alcohol goes through the aldehyde to the acid (Chapter 3).",
                 "data": scheme([('m', 'CCO', 'ethanol', 120), ('>', '[O]', ''), ('m', 'CC=O', 'acetaldehyde', 130), ('>', '[O]', ''), ('m', 'CC(=O)O', 'acetic acid', 130)], h=105)},
         "items": ["Oxidising a <b>primary alcohol</b> or an <b>aldehyde</b> gives a carboxylic acid (for example with acidified dichromate).",
                   "The same two steps happen in your <b>liver</b>, catalysed by dehydrogenase enzymes; acetic acid is then oxidised to CO<sub>2</sub> and water.",
                   "This is why wine left open turns to vinegar: bacteria oxidise its ethanol to acetic acid."],
         "notes": "Ball 15.2; the wine example is original."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Very high boiling points",
         "head": ["Compound", "Family", "Molar mass", "bp (°C)"],
         "rows": [["CH<sub>3</sub>CH<sub>2</sub>CHO, propanal", "aldehyde", "58", "49"],
                  ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH, 1-propanol", "alcohol", "60", "97"],
                  ["CH<sub>3</sub>COOH, acetic acid", "carboxylic acid", "60", "118"],
                  ["CH<sub>3</sub>CH<sub>2</sub>COOH, propanoic acid", "carboxylic acid", "74", "141"],
                  ["C<sub>6</sub>H<sub>5</sub>COOH, benzoic acid", "carboxylic acid", "122", "249 (solid, mp 122)"]],
         "widths": [4.0, 2.2, 1.6, 2.2],
         "caption": "Two acid molecules hold each other by <b>two</b> hydrogen bonds (C=O···H–O both ways), forming a <b>dimer</b>, so acids boil even higher than alcohols. Acids with 1–4 carbons mix completely with water; hexanoic acid dissolves only about 1 g/100 g. Sources: Ball 15.3 (acids), Chapter 3 (propanal, 1-propanol).",
         "notes": "Ball 15.3 table. Dimer explanation original. Acids with 5–10 carbons smell 'goaty' (Limburger cheese, locker rooms)."})
    add({"t": "two", "sec": 1, "lo": LO2, "title": "Carboxylic acids are weak acids",
         "lead": "In water, only a small fraction of acid molecules give up H<sup>+</sup>: RCOOH + H<sub>2</sub>O ⇌ RCOO<sup>−</sup> + H<sub>3</sub>O<sup>+</sup>",
         "cols": [{"h": "Naming the anion", "tone": "cold", "items": [
             "Drop <b>-ic acid</b>, add <b>-ate</b>: acetic acid → acetate; ethanoic acid → ethanoate",
             "CH<sub>3</sub>COOH + H<sub>2</sub>O ⇌ CH<sub>3</sub>COO<sup>−</sup> + H<sub>3</sub>O<sup>+</sup> (acetate ion)",
             "Vinegar is acidic, but far less than the same concentration of HCl"]},
             {"h": "Measuring strength", "tone": "heat", "items": [
                 "<b>K<sub>a</sub></b>: larger K<sub>a</sub> = stronger acid",
                 "<b>pK<sub>a</sub> = −log K<sub>a</sub></b>: <b>smaller</b> pK<sub>a</sub> = stronger acid",
                 "Each 1 pK<sub>a</sub> unit is a <b>10-fold</b> change in acidity",
                 "Carboxylic acids are more acidic than alcohols and phenols"]}],
         "notes": "FGOB 17.2."})
    add({"t": "table", "sec": 1, "lo": LO2, "title": "pK<sub>a</sub> values of some acids",
         "head": ["Acid", "Formula", "K<sub>a</sub>", "pK<sub>a</sub>"],
         "rows": [["trichloroacetic acid", "Cl<sub>3</sub>CCOOH", "2.3 × 10<sup>−1</sup>", "0.64"],
                  ["chloroacetic acid", "ClCH<sub>2</sub>COOH", "1.4 × 10<sup>−3</sup>", "2.85"],
                  ["formic acid", "HCOOH", "1.8 × 10<sup>−4</sup>", "3.74"],
                  ["benzoic acid", "C<sub>6</sub>H<sub>5</sub>COOH", "6.5 × 10<sup>−5</sup>", "4.19"],
                  ["acetic acid", "CH<sub>3</sub>COOH", "1.8 × 10<sup>−5</sup>", "4.74"],
                  ["propanoic acid", "CH<sub>3</sub>CH<sub>2</sub>COOH", "1.3 × 10<sup>−5</sup>", "4.89"]],
         "widths": [3.0, 2.8, 2.2, 1.4],
         "caption": "Electronegative Cl atoms pull electron density away from the –COO<sup>−</sup> and stabilise it, so each Cl makes the acid stronger: trichloroacetic acid is about 10 000 times stronger than acetic acid. Source: FGOB Table 17.2.",
         "notes": "FGOB 17.2 table; the inductive explanation is original."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO2, "title": "Neutralisation: acids + bases → salts",
         "fig": {"cap": "Acetic acid + sodium hydroxide → sodium acetate + water.",
                 "data": scheme([('m', 'CC(=O)O', 'acetic acid', 130), ('+',), ('t', 'NaOH', 80), ('>', '', ''), ('m', 'CC(=O)[O-].[Na+]', 'sodium acetate', 180), ('+',), ('t', 'H₂O', 60)], h=100)},
         "items": ["RCOOH + NaOH → RCOO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O",
                   "2 RCOOH + Na<sub>2</sub>CO<sub>3</sub> → 2 RCOO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O + <b>CO<sub>2</sub></b>",
                   "RCOOH + NaHCO<sub>3</sub> → RCOO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O + <b>CO<sub>2</sub></b> (fizzing: a test for –COOH)",
                   "Name the salt like an inorganic salt: cation, then the <b>-ate</b> anion: sodium acetate, potassium benzoate. Salts of long-chain acids are <b>soaps</b>."],
         "notes": "FGOB 17.2; the bicarbonate test is original."})
    add({"t": "example", "sec": 1, "lo": LO2, "title": "Example 4.1 · Write the equations",
         "q": "Write an equation for the reaction of decanoic acid with (a) aqueous sodium hydroxide (b) aqueous sodium bicarbonate",
         "steps": ["Decanoic acid has 10 carbons: CH<sub>3</sub>(CH<sub>2</sub>)<sub>8</sub>COOH.",
                   "(a) CH<sub>3</sub>(CH<sub>2</sub>)<sub>8</sub>COOH + NaOH(aq) → CH<sub>3</sub>(CH<sub>2</sub>)<sub>8</sub>COO<sup>−</sup>Na<sup>+</sup>(aq) + H<sub>2</sub>O(ℓ): <b>sodium decanoate</b> and water.",
                   "(b) CH<sub>3</sub>(CH<sub>2</sub>)<sub>8</sub>COOH + NaHCO<sub>3</sub>(aq) → CH<sub>3</sub>(CH<sub>2</sub>)<sub>8</sub>COO<sup>−</sup>Na<sup>+</sup>(aq) + H<sub>2</sub>O(ℓ) + CO<sub>2</sub>(g)."],
         "notes": "FGOB 17.2 Example."})
    add({"t": "bullets", "sec": 1, "lo": LO2, "title": "Acid salts in the pharmacy",
         "items": ["Salts are <b>ionic</b>, so they dissolve in water far better than the acids. Many acidic drugs are sold as sodium salts: <b>diclofenac sodium</b>, <b>naproxen sodium</b>.",
                   "<b>Preservatives</b> that stop bacteria and fungi: sodium benzoate (syrups, pickles), calcium propionate (bread), potassium sorbate (juices) (FGOB 17.2).",
                   "<b>Effervescent tablets</b>: citric acid + sodium bicarbonate react when dropped into water, releasing CO<sub>2</sub> that breaks up the tablet.",
                   "In the acidic stomach, a salt such as RCOO<sup>−</sup> takes back H<sup>+</sup> and returns to RCOOH."],
         "side": {"h": "Read the label", "body": "\"Sodium\" or \"potassium\" in a drug name usually means the salt of an acid; \"hydrochloride\" means the salt of a base (4.3)."},
         "notes": "FGOB 17.2 preservatives; drug salts and effervescence are original."})
    add({"t": "check", "sec": 1, "lo": LO1, "title": "Quick check",
         "q": "Which has the highest boiling point? (similar molar masses)",
         "opts": ["propanal", "1-propanol", "acetic acid", "methoxyethane"], "ans": 2,
         "why": "Acetic acid molecules form hydrogen-bonded dimers: 118 °C, versus 97 °C for 1-propanol.", "notes": "Answer C."})
    add({"t": "check", "sec": 1, "lo": LO2, "title": "Quick check",
         "q": "A white powder fizzes when it is added to sodium bicarbonate solution. It most likely contains:",
         "opts": ["an alcohol", "a carboxylic acid", "an ester", "an alkane"], "ans": 1,
         "why": "RCOOH + NaHCO<sub>3</sub> → RCOO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O + CO<sub>2</sub>.", "notes": "Answer B."})

    # ================= 4.2 ESTERS =================
    add({"t": "divider", "num": 2, "title": "Esters", "lo": "CH4-LO3", "src": "Ball 15.5–15.9 · FGOB 17.3–17.4, 17.6",
         "blurb": "Replace the H of –COOH with a carbon group: the smells of fruit, aspirin, fats, and the bonds in DNA."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO3, "title": "The ester group, –COOR′",
         "fig": {"cap": HL_KEY,
                 "data": row([(mol("CCOC(C)=O", 190, 120, highlight=[ESTER]), "ethyl acetate"), (mol("COC(=O)c1ccccc1O", 200, 120, highlight=[ESTER]), "methyl salicylate"),
                              (mol(ASPIRIN, 220, 120, highlight=[ESTER, ACID]), "aspirin"), (mol(PROCAINE, 260, 120, highlight=[ESTER]), "procaine")], w=250, h=120)},
         "items": ["General formula <b>RCOOR′</b>: R may be H, alkyl or aryl; R′ must be a carbon group (if R′ were H, it would be an acid).",
                   "Esters give fruits and flowers their smells, and fats and oils are esters of glycerol (Chapter 6).",
                   "Drugs with esters: aspirin, the local anaesthetic procaine, and methyl salicylate (oil of wintergreen) in muscle rubs."],
         "notes": "Ball 15.5; drug examples original."})
    add({"t": "table", "sec": 2, "lo": LO3, "title": "Naming esters: alkyl group + -ate",
         "head": ["Formula", "Common name", "IUPAC name"],
         "rows": [["HCOOCH<sub>3</sub>", "methyl formate", "methyl methanoate"],
                  ["CH<sub>3</sub>COOCH<sub>3</sub>", "methyl acetate", "methyl ethanoate"],
                  ["CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>", "ethyl acetate", "ethyl ethanoate"],
                  ["CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub>", "ethyl propionate", "ethyl propanoate"],
                  ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH(CH<sub>3</sub>)<sub>2</sub>", "isopropyl butyrate", "isopropyl butanoate"],
                  ["C<sub>6</sub>H<sub>5</sub>COOCH<sub>2</sub>CH<sub>3</sub>", "ethyl benzoate", "ethyl benzoate"]],
         "widths": [4.2, 2.6, 2.8],
         "caption": "Two words: first the group on the <b>O</b> (R′), then the acid part with -ic acid → <b>-ate</b>. Careful: in CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub> the ethyl is written <b>last</b> but named <b>first</b>. Source: Ball Table 15.5.1.",
         "notes": "Ball 15.5."})
    add({"t": "tryit", "sec": 2, "lo": LO3, "title": "Try it · Esters",
         "q": "(a) Name CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (b) Name HCOOCH<sub>2</sub>CH<sub>3</sub> (c) Write the condensed formula of ethyl pentanoate",
         "a": "(a) <b>butyl propanoate</b> (butyl propionate) (b) <b>ethyl methanoate</b> (ethyl formate; it smells of rum) (c) <b>CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub></b>: the five-carbon pentanoate includes the carboxyl carbon (Ball 15.5).",
         "notes": "Ball 15.5 Examples 1–2; 15.6 for ethyl formate."})
    add({"t": "table", "sec": 2, "lo": LO3, "title": "Properties: no O–H, so lower boiling points",
         "head": ["Compound (all C<sub>3</sub>–C<sub>4</sub>, molar mass 74)", "Family", "bp (°C)"],
         "rows": [["CH<sub>3</sub>COOCH<sub>3</sub>, methyl acetate", "ester", "57"],
                  ["HCOOCH<sub>2</sub>CH<sub>3</sub>, ethyl formate", "ester", "54"],
                  ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH, 1-butanol", "alcohol", "117"],
                  ["CH<sub>3</sub>CH<sub>2</sub>COOH, propanoic acid", "carboxylic acid", "141"]],
         "widths": [5.0, 2.4, 1.4],
         "caption": "Esters are polar but cannot hydrogen bond to each other, so they boil far lower than their isomeric acids. They can accept H-bonds from water: small esters are somewhat soluble (borderline at 3–5 carbons). Ethyl acetate is a solvent for extracting caffeine and in nail-polish remover. Sources: Ball 15.6, 15.3.",
         "notes": "Ball 15.6."})
    add({"t": "table", "sec": 2, "lo": LO3, "title": "Esters you can smell",
         "head": ["Ester", "Formula", "Smell"],
         "rows": [["methyl butyrate", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>3</sub>", "apple"],
                  ["ethyl butyrate", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub>", "pineapple"],
                  ["pentyl acetate", "CH<sub>3</sub>COO(CH<sub>2</sub>)<sub>4</sub>CH<sub>3</sub>", "pear"],
                  ["isopentyl acetate", "CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub>", "banana"],
                  ["benzyl acetate", "CH<sub>3</sub>COOCH<sub>2</sub>C<sub>6</sub>H<sub>5</sub>", "jasmine"],
                  ["octyl acetate", "CH<sub>3</sub>COO(CH<sub>2</sub>)<sub>7</sub>CH<sub>3</sub>", "orange"],
                  ["methyl salicylate", mini("COC(=O)c1ccccc1O"), "wintergreen (muscle rubs)"]],
         "widths": [2.6, 4.6, 2.4],
         "caption": "Flavour chemists copy these natural esters to flavour syrups and chewable tablets. Source: Ball 15.6 (methyl salicylate added).",
         "notes": "Ball 15.6 table."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO3, "title": "Making esters: esterification",
         "fig": {"cap": "Acid + alcohol ⇌ ester + water. The –OH of the acid and the H of the alcohol leave as water.",
                 "data": scheme([('m', 'CC(=O)O', 'acetic acid', 130), ('+',), ('m', 'CCO', 'ethanol', 110), ('>', 'H⁺, heat', 'reversible'), ('m', 'CCOC(C)=O', 'ethyl acetate', 150), ('+',), ('t', 'H₂O', 60)], h=105)},
         "items": ["Heat a carboxylic acid with an alcohol and a little <b>concentrated H<sub>2</sub>SO<sub>4</sub></b> (catalyst).",
                   "The reaction is <b>reversible</b> and reaches equilibrium with similar amounts of reactants and products.",
                   "To get more ester (Le Chatelier): use <b>excess alcohol</b>, or <b>remove the water or ester</b> as it forms.",
                   "Esterification is a <b>condensation</b>: two molecules join and a small molecule (water) is lost."],
         "notes": "FGOB 17.3."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO3, "title": "Making aspirin",
         "fig": {"cap": "The phenol –OH of salicylic acid is esterified. Industry uses acetic anhydride because it reacts faster and completely.",
                 "data": scheme([('m', SALICYLIC, 'salicylic acid', 160), ('+',), ('m', ANHYDRIDE, 'acetic anhydride', 170), ('>', 'H⁺, warm', ''), ('m', ASPIRIN, 'aspirin', 180), ('+',), ('m', 'CC(=O)O', 'acetic acid', 120)], h=115)},
         "items": ["Salicylic acid (from willow bark) relieves pain but irritates the mouth and stomach.",
                   "Turning its phenol into an <b>ester</b> gives acetylsalicylic acid, aspirin (Bayer, 1899): better tolerated.",
                   "The reverse reaction, hydrolysis, is why old aspirin tablets smell of <b>vinegar</b> (next slides)."],
         "notes": "Original (standard synthesis); links to Chapter 1."})
    add({"t": "example", "sec": 2, "lo": LO3, "title": "Example 4.2 · Predict the ester",
         "q": "Write the condensed formula and name of the ester formed from (a) propanoic acid and methanol (b) acetic acid and 3-methyl-1-butanol",
         "steps": ["Join the acid part (RCO–) to the alkoxy part (–OR′) of the alcohol; water is lost.",
                   "(a) CH<sub>3</sub>CH<sub>2</sub>COOH + CH<sub>3</sub>OH ⇌ CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub> + H<sub>2</sub>O: <b>methyl propanoate</b>.",
                   "(b) CH<sub>3</sub>COOH + HOCH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub> ⇌ CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub> + H<sub>2</sub>O: <b>isopentyl acetate</b>, the banana smell."],
         "notes": "Original example using Ball 15.6 esters."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO3, "title": "Hydrolysis: splitting esters with water",
         "fig": {"cap": "Top: acidic hydrolysis (reversible). Bottom: basic hydrolysis, saponification (goes to completion).",
                 "data": stack([scheme([('m', 'CCOC(C)=O', 'ethyl acetate', 150), ('+',), ('t', 'H₂O', 60), ('>', 'H⁺, heat', 'reversible'), ('m', 'CC(=O)O', 'acetic acid', 130), ('+',), ('m', 'CCO', 'ethanol', 110)], h=100),
                                scheme([('m', 'CCOC(C)=O', 'ethyl acetate', 150), ('+',), ('t', 'NaOH', 80), ('>', 'heat', 'complete'), ('m', 'CC(=O)[O-].[Na+]', 'sodium acetate', 180), ('+',), ('m', 'CCO', 'ethanol', 110)], h=100)], w=820, row_h=130)},
         "items": ["<b>Acidic hydrolysis</b> is esterification in reverse: excess water and an acid catalyst give the <b>acid + alcohol</b>.",
                   "<b>Basic hydrolysis</b> (NaOH or KOH) gives the <b>carboxylate salt + alcohol</b>. The base is a reactant, not a catalyst.",
                   "It is called <b>saponification</b> (Latin <i>sapo</i>, soap): boiling fats with NaOH makes soap and glycerol (Chapter 6)."],
         "notes": "FGOB 17.4."})
    add({"t": "example", "sec": 2, "lo": LO3, "title": "Example 4.3 · Hydrolyse these esters",
         "q": "Give the products of (a) the acidic hydrolysis of ethyl butyrate, CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub> (b) the hydrolysis of methyl benzoate in KOH solution",
         "steps": ["Water splits the C–O bond between the C=O and the OR′: the OH goes to the carbonyl carbon, the H to the OR′ oxygen.",
                   "(a) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O ⇌ CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH + CH<sub>3</sub>CH<sub>2</sub>OH: <b>butanoic acid</b> and <b>ethanol</b>.",
                   "(b) C<sub>6</sub>H<sub>5</sub>COOCH<sub>3</sub> + KOH → C<sub>6</sub>H<sub>5</sub>COO<sup>−</sup>K<sup>+</sup> + CH<sub>3</sub>OH: <b>potassium benzoate</b> and <b>methanol</b>."],
         "notes": "FGOB 17.4 Examples."})
    add({"t": "bullets", "sec": 2, "lo": LO3, "title": "Ester hydrolysis in the body and on the shelf",
         "items": ["<b>Shelf life</b>: aspirin slowly hydrolyses in moist air to salicylic acid + acetic acid. Store it dry and discard tablets that smell of vinegar.",
                   "<b>Ester prodrugs</b>: some drugs are given as esters that absorb better, then <b>esterase</b> enzymes release the active acid: enalapril → enalaprilat; oseltamivir → its active carboxylate.",
                   "<b>Ester local anaesthetics</b> (procaine, benzocaine) are quickly hydrolysed by plasma esterases, so they act briefly.",
                   "<b>Dissolvable stitches</b> are polyesters (polyglycolic and polylactic acid) that slowly hydrolyse in the body."],
         "notes": "Original pharmacy links."})
    add({"t": "bullets", "sec": 2, "lo": LO3, "title": "Esters of inorganic acids",
         "items": ["Phosphoric acid (H<sub>3</sub>PO<sub>4</sub>) forms mono-, di- and triesters with alcohols. Phosphate esters are in every cell.",
                   "<b>ATP</b> stores energy in its phosphoanhydride bonds; hydrolysing them releases energy for muscle contraction.",
                   "Phosphate esters form the backbone of <b>DNA and RNA</b> and are part of <b>phospholipids</b> in cell membranes.",
                   "<b>Glyceryl trinitrate</b> (nitroglycerin), an ester of glycerol and nitric acid, is a sublingual tablet or spray that relieves angina."],
         "notes": "FGOB 17.6; Ball 15.9."})
    add({"t": "check", "sec": 2, "lo": LO3, "title": "Quick check",
         "q": "What is the IUPAC name of CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub>?",
         "opts": ["methyl propanoate", "propyl methanoate", "ethyl ethanoate", "methyl butanoate"], "ans": 0,
         "why": "The group on the O (methyl) comes first; the acid part has 3 carbons (propanoate).", "notes": "Answer A."})
    add({"t": "check", "sec": 2, "lo": LO3, "title": "Quick check",
         "q": "Saponification of an ester with NaOH gives:",
         "opts": ["a carboxylic acid and an alcohol", "a sodium carboxylate and an alcohol", "an ether and water", "an amide"], "ans": 1,
         "why": "Basic hydrolysis gives the salt of the acid; it goes to completion.", "notes": "Answer B."})

    # ================= 4.3 AMINES =================
    add({"t": "divider", "num": 3, "title": "Amines", "lo": "CH4-LO4", "src": "Ball 15.10–15.12 · FGOB 16.1–16.7",
         "blurb": "Ammonia with carbon groups: the organic bases, found in most drugs and in many plant poisons."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO4, "title": "Classifying amines: 1°, 2°, 3°",
         "fig": {"cap": "Count the carbon groups on the nitrogen atom.",
                 "data": row([(mol("N", 120, 100, hs=True), "ammonia NH₃"), (mol("CN", 140, 100, hs=True), "1° · methylamine"),
                              (mol("CNC", 160, 100), "2° · dimethylamine"), (mol("CN(C)C", 160, 100), "3° · trimethylamine")], w=210, h=100)},
         "items": ["An amine is ammonia with one, two or three H atoms replaced by carbon groups: <b>1°</b> RNH<sub>2</sub>, <b>2°</b> R<sub>2</sub>NH, <b>3°</b> R<sub>3</sub>N.",
                   "Careful: for alcohols you count carbons on the C–OH <b>carbon</b>; for amines you count carbons on the <b>nitrogen</b>.",
                   "So isopropylamine, (CH<sub>3</sub>)<sub>2</sub>CHNH<sub>2</sub>, is a <b>1° amine</b>, although isopropyl alcohol is a 2° alcohol."],
         "notes": "FGOB 16.1."})
    add({"t": "table", "sec": 3, "lo": LO4, "title": "Naming amines",
         "head": ["Rule", "Example"],
         "rows": [["Simple amines: name the carbon groups on N in <b>alphabetical order</b>, then add <b>-amine</b> (one word).", "CH<sub>3</sub>CH<sub>2</sub>NHCH<sub>3</sub> is ethylmethylamine"],
                  ["Use di- or tri- for identical groups.", "(CH<sub>3</sub>CH<sub>2</sub>)<sub>3</sub>N is triethylamine"],
                  ["In complicated molecules, –NH<sub>2</sub> is named as the substituent <b>amino</b>.", "CH<sub>3</sub>CH(NH<sub>2</sub>)CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub> is 2-amino-3-methylpentane"],
                  ["NH<sub>2</sub> on a benzene ring: <b>aniline</b>; name substituted ones as anilines.", "m-bromoaniline (3-bromoaniline)"],
                  ["Ions: name the groups, then <b>ammonium</b>.", "CH<sub>3</sub>NH<sub>3</sub><sup>+</sup> is methylammonium; (CH<sub>3</sub>)<sub>4</sub>N<sup>+</sup> is tetramethylammonium"]],
         "widths": [5.2, 4.2], "caption": "Source: FGOB 16.2.",
         "notes": "FGOB 16.1–16.2."})
    add({"t": "tryit", "sec": 3, "lo": LO4, "title": "Try it · Name and classify",
         "q": "Name and classify each amine: (a) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> (b) CH<sub>3</sub>CH<sub>2</sub>N(CH<sub>3</sub>)<sub>2</sub> (c) CH<sub>3</sub>CH<sub>2</sub>NHCH<sub>2</sub>CH<sub>3</sub> (d) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>NHCH<sub>3</sub>",
         "a": "(a) <b>propylamine</b>, 1° (b) <b>ethyldimethylamine</b>, 3° (c) <b>diethylamine</b>, 2° (d) <b>methylpropylamine</b>, 2° (FGOB 16.2).",
         "notes": "FGOB 16.2 Example."})
    add({"t": "table", "sec": 3, "lo": LO4, "title": "Properties: weaker hydrogen bonds than alcohols",
         "head": ["Compound", "Class", "Molar mass", "bp (°C)", "Solubility (g/100 g water)"],
         "rows": [["butylamine, CH<sub>3</sub>(CH<sub>2</sub>)<sub>3</sub>NH<sub>2</sub>", "1°", "73", "78", "miscible"],
                  ["diethylamine, (CH<sub>3</sub>CH<sub>2</sub>)<sub>2</sub>NH", "2°", "73", "55", "miscible"],
                  ["butyl alcohol, CH<sub>3</sub>(CH<sub>2</sub>)<sub>3</sub>OH", "—", "74", "118", "8"],
                  ["dipropylamine, (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>)<sub>2</sub>NH", "2°", "101", "111", "4"],
                  ["triethylamine, (CH<sub>3</sub>CH<sub>2</sub>)<sub>3</sub>N", "3°", "101", "90", "14"],
                  ["dipropyl ether, (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>)<sub>2</sub>O", "—", "102", "91", "0.25"]],
         "widths": [4.4, 1.0, 1.4, 1.2, 2.4],
         "caption": "1° and 2° amines hydrogen bond (N–H), but N is less electronegative than O, so they boil lower than alcohols. 3° amines have no N–H and boil like ethers. All can accept H-bonds from water: small amines dissolve (borderline 5–6 carbons). Source: FGOB Table 16.3.",
         "notes": "FGOB 16.3."})
    add({"t": "bullets", "sec": 3, "lo": LO4, "title": "Amines you can smell (and avoid)",
         "items": ["Small amines smell like ammonia; larger ones smell of <b>rotting fish</b>. Trimethylamine is the smell of old fish.",
                   "<b>Putrescine</b> and <b>cadaverine</b>, two diamines, form when bacteria break down proteins in dead tissue (FGOB 16.3).",
                   "Aromatic amines are often <b>toxic</b> and absorbed through skin; some, such as β-naphthylamine, cause cancer. Wear gloves.",
                   "Useful amines: adrenaline, dopamine, salbutamol and most antihistamines and antidepressants contain an amine group."],
         "notes": "FGOB 16.3; drug list original."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO4, "title": "Amines are bases",
         "fig": {"cap": "The lone pair on nitrogen accepts a proton, just as in ammonia.",
                 "data": stack([scheme([('m', 'CN', 'methylamine', 120), ('+',), ('t', 'H₂O', 60), ('>', '⇌', ''), ('m', 'C[NH3+]', 'methylammonium ion', 170), ('+',), ('t', 'OH⁻', 60)], h=90),
                                scheme([('m', 'CN', 'methylamine', 120), ('+',), ('t', 'HCl', 60), ('>', '', ''), ('m', 'C[NH3+].[Cl-]', 'methylammonium chloride', 220)], h=90)], w=700, row_h=120)},
         "items": ["In water amines are <b>weak bases</b>: RNH<sub>2</sub> + H<sub>2</sub>O ⇌ RNH<sub>3</sub><sup>+</sup> + OH<sup>−</sup>.",
                   "With strong acids they form <b>amine salts</b>, which are ionic and water-soluble, even when the amine itself is not.",
                   "Name salts like inorganic salts: cation then anion. Drug names use the older style: aniline + HCl → anilinium chloride, or \"aniline <b>hydrochloride</b>\"."],
         "notes": "FGOB 16.5."})
    add({"t": "example", "sec": 3, "lo": LO4, "title": "Example 4.4 · Which acid and base?",
         "q": "What are the formulas of the acid and base that react to form [CH<sub>3</sub>NH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>]<sup>+</sup>CH<sub>3</sub>COO<sup>−</sup>?",
         "steps": ["The cation has a methyl and an ethyl group on N plus two H, so it came from <b>ethylmethylamine</b>, CH<sub>3</sub>NHCH<sub>2</sub>CH<sub>3</sub> (the base), which gained one H<sup>+</sup>.",
                   "The anion is acetate, so the acid was <b>acetic acid</b>, CH<sub>3</sub>COOH.",
                   "CH<sub>3</sub>NHCH<sub>2</sub>CH<sub>3</sub> + CH<sub>3</sub>COOH → [CH<sub>3</sub>NH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>]<sup>+</sup>CH<sub>3</sub>COO<sup>−</sup> (ethylmethylammonium acetate)."],
         "notes": "FGOB 16.5 Example."})
    add({"t": "two", "sec": 3, "lo": LO4, "title": "Amine salts as medicines",
         "lead": "Many drugs are amines, and most are sold as <b>hydrochloride</b> (or sulfate) salts.",
         "cols": [{"h": "Why use the salt?", "tone": "cold", "items": [
             "Ionic: <b>dissolves in water</b>, so it can be an injection, syrup or eye drop",
             "Solid, stable and <b>odourless</b>; free amines are often oily and smelly",
             "Examples: lidocaine hydrochloride injection, diphenhydramine hydrochloride syrup, morphine sulfate"]},
             {"h": "Free base vs salt", "tone": "heat", "items": [
                 "A base (OH<sup>−</sup>) converts the salt back to the free amine: RNH<sub>3</sub><sup>+</sup> + OH<sup>−</sup> → RNH<sub>2</sub> + H<sub>2</sub>O",
                 "The free amine is uncharged and crosses fatty cell membranes more easily",
                 "Cocaine hydrochloride is water-soluble; the free base (\"crack\") is volatile and can be smoked (FGOB 16.4)"]}],
         "notes": "FGOB 16.4–16.5; drug examples original."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO4, "title": "Heterocyclic amines and alkaloids",
         "fig": {"cap": "Nitrogen inside a ring: heterocyclic amines. Basic plant amines are called alkaloids (\"like alkalis\").",
                 "data": row([(mol(CAFFEINE, 220, 150), "caffeine"), (mol(NICOTINE, 200, 150), "nicotine"), (mol(MORPHINE, 230, 150), "morphine")], w=250, h=150)},
         "items": ["<b>Caffeine</b> (coffee, tea; ~200 mg = two strong cups) blocks adenosine receptors. <b>Nicotine</b> mimics acetylcholine; ~50 mg can kill.",
                   "<b>Morphine</b> and codeine come from the opium poppy. Other alkaloid drugs: quinine (malaria), atropine (eye drops).",
                   "Alkaloids are <b>extracted</b> from plants with dilute acid (forming water-soluble salts), then freed again by adding a base."],
         "notes": "FGOB 16.4, 16.7; quinine and atropine added (original)."})
    add({"t": "bullets", "sec": 3, "lo": LO4, "title": "Quaternary ammonium salts",
         "items": ["Four carbon groups on N give a permanent positive ion, R<sub>4</sub>N<sup>+</sup>: tetramethylammonium, (CH<sub>3</sub>)<sub>4</sub>N<sup>+</sup>.",
                   "They have no lone pair and no N–H, so they are <b>not bases</b> and stay charged at any pH.",
                   "<b>Benzalkonium chloride</b> is a quaternary ammonium antiseptic and the preservative in many eye drops and nasal sprays.",
                   "<b>Choline</b> and the neurotransmitter <b>acetylcholine</b> are quaternary ammonium ions (and acetylcholine is also an ester)."],
         "notes": "FGOB 16.2 (naming); applications original."})
    add({"t": "check", "sec": 3, "lo": LO4, "title": "Quick check",
         "q": "(CH<sub>3</sub>)<sub>2</sub>CHNH<sub>2</sub> is classified as a:",
         "opts": ["1° amine", "2° amine", "3° amine", "quaternary ammonium ion"], "ans": 0,
         "why": "Only one carbon group is bonded to the nitrogen (FGOB 16.1).", "notes": "Answer A."})
    add({"t": "check", "sec": 3, "lo": LO4, "title": "Quick check",
         "q": "Why is lidocaine injection made with lidocaine hydrochloride rather than lidocaine itself?",
         "opts": ["The salt is ionic and dissolves in water", "The salt is a stronger anaesthetic", "The free amine is an acid", "Hydrochlorides are esters"], "ans": 0,
         "why": "Amine salts are water-soluble; free amines often are not.", "notes": "Answer A."})

    # ================= 4.4 AMIDES =================
    add({"t": "divider", "num": 4, "title": "Amides", "lo": "CH4-LO5", "src": "Ball 15.13–15.16 · FGOB 17.3–17.5",
         "blurb": "Acid + amine: the very stable bond that holds proteins together, and is found in paracetamol, penicillin and nylon."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO5, "title": "The amide group, –CONH–",
         "fig": {"cap": HL_KEY,
                 "data": row([(mol("CC(N)=O", 160, 120, highlight=[AMIDE]), "acetamide"), (mol("CNC(C)=O", 170, 120, highlight=[AMIDE]), "N-methylacetamide"),
                              (mol(PARACETAMOL, 220, 120, highlight=[AMIDE]), "paracetamol"), (mol(LIDOCAINE, 250, 120, highlight=[AMIDE, AMINE]), "lidocaine")], w=240, h=120)},
         "items": ["An <b>amide</b> has a nitrogen bonded to a carbonyl carbon. <b>Simple</b> amides: –CONH<sub>2</sub>; <b>substituted</b> amides have carbon groups on N.",
                   "The C–N bond is the <b>amide linkage</b>; in proteins it is called the <b>peptide bond</b> (Chapter 7).",
                   "Lidocaine has both an amide and an amine: the amine makes the hydrochloride salt possible (4.3)."],
         "notes": "Ball 15.13."})
    add({"t": "table", "sec": 4, "lo": LO5, "title": "Naming amides",
         "head": ["Rule", "Example"],
         "rows": [["Name from the acid: <b>-ic acid</b> (common) or <b>-oic acid</b> (IUPAC) → <b>-amide</b>.", "CH<sub>3</sub>CONH<sub>2</sub>: acetamide (ethanamide)"],
                  ["Benzoic acid → benzamide.", "C<sub>6</sub>H<sub>5</sub>CONH<sub>2</sub>: benzamide"],
                  ["Groups on the nitrogen get the locant <b>N-</b>.", "CH<sub>3</sub>CONHCH<sub>3</sub>: N-methylacetamide (N-methylethanamide)"],
                  ["Two groups on N: N,N-.", "HCON(CH<sub>3</sub>)<sub>2</sub>: N,N-dimethylformamide (DMF), a lab solvent"]],
         "widths": [5.2, 4.4], "caption": "Do not confuse an amide (N on a C=O) with an amine (N on ordinary carbons). Sources: Ball 15.13 (simple amides); N- naming added.",
         "notes": "Ball 15.13; N-substituted naming is original (standard IUPAC)."})
    add({"t": "tryit", "sec": 4, "lo": LO5, "title": "Try it · Amide or amine?",
         "q": "Name each compound and say whether it is an amide or an amine: (a) CH<sub>3</sub>CH<sub>2</sub>CONH<sub>2</sub> (b) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> (c) HCONH<sub>2</sub> (d) CH<sub>3</sub>CH<sub>2</sub>CONHCH<sub>3</sub>",
         "a": "(a) <b>propanamide</b> (propionamide), amide (b) <b>propylamine</b>, amine (c) <b>methanamide</b> (formamide), amide (d) <b>N-methylpropanamide</b>, amide.",
         "notes": "Original, based on Ball 15.13–15.16."})
    add({"t": "table", "sec": 4, "lo": LO5, "title": "Properties: high melting points, but not basic",
         "head": ["Amide", "Formula", "mp (°C)", "bp (°C)", "In water"],
         "rows": [["formamide", "HCONH<sub>2</sub>", "2", "193", "soluble"],
                  ["acetamide", "CH<sub>3</sub>CONH<sub>2</sub>", "82", "222", "soluble"],
                  ["butyramide", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CONH<sub>2</sub>", "115", "216", "soluble"],
                  ["benzamide", "C<sub>6</sub>H<sub>5</sub>CONH<sub>2</sub>", "132", "290", "slightly soluble"]],
         "widths": [2.4, 3.0, 1.4, 1.4, 2.2],
         "caption": "Amides with N–H form networks of hydrogen bonds, so all simple amides except formamide are solids, and they boil far higher than alcohols. Unlike amines they are <b>not basic</b>: the N lone pair is pulled towards the C=O, so it does not accept H<sup>+</sup>. Their solutions are neutral. Source: Ball 15.14.",
         "notes": "Ball 15.14 table; the reason amides are not basic is original."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO5, "title": "Making amides",
         "fig": {"cap": "Acid + ammonia or a 1° or 2° amine → amide + water (heat).",
                 "data": stack([scheme([('m', 'CC(=O)O', 'acetic acid', 130), ('+',), ('t', 'NH₃', 60), ('>', 'heat', ''), ('m', 'CC(N)=O', 'acetamide (1° amide)', 170), ('+',), ('t', 'H₂O', 60)], h=95),
                                scheme([('m', 'CC(=O)O', 'acetic acid', 130), ('+',), ('m', 'CN', 'methylamine', 110), ('>', 'heat', ''), ('m', 'CNC(C)=O', 'N-methylacetamide', 170), ('+',), ('t', 'H₂O', 60)], h=95)], w=760, row_h=125)},
         "items": ["Like esterification, the –OH of the acid and an H on the nitrogen leave as water: a <b>condensation</b>.",
                   "Ammonia → 1° (simple) amide; 1° amine → 2° amide; 2° amine → 3° amide.",
                   "A <b>3° amine</b> has no H on N, so it cannot form an amide: it just forms a salt (acid–base reaction).",
                   "In industry and the body, more reactive acid derivatives (anhydrides, activated esters) are used."],
         "notes": "FGOB 17.3."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO5, "title": "Making paracetamol",
         "fig": {"cap": "The amine of 4-aminophenol reacts with acetic anhydride; the phenol stays.",
                 "data": scheme([('m', AMINOPHENOL, '4-aminophenol', 160), ('+',), ('m', ANHYDRIDE, 'acetic anhydride', 170), ('>', 'warm', ''), ('m', PARACETAMOL, 'paracetamol', 190), ('+',), ('m', 'CC(=O)O', 'acetic acid', 120)], h=115)},
         "items": ["The same reagent as in the aspirin synthesis: aspirin is an <b>ester</b> made at an –OH; paracetamol is an <b>amide</b> made at an –NH<sub>2</sub>.",
                   "Paracetamol's chemical name is N-(4-hydroxyphenyl)acetamide, or <b>acetaminophen</b> in the USA.",
                   "4-Aminophenol is also a breakdown product of paracetamol, so pharmacopoeias limit it as an impurity."],
         "notes": "Original (standard synthesis)."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO5, "title": "Hydrolysis of amides",
         "fig": {"cap": "Butyramide hydrolysis. In acid the ammonia forms an ammonium salt; in base the acid forms a carboxylate salt.",
                 "data": stack([scheme([('m', 'CCCC(N)=O', 'butyramide', 140), ('+',), ('t', 'H₂O', 60), ('>', 'H⁺, heat', ''), ('m', 'CCCC(=O)O', 'butyric acid', 140), ('+',), ('t', 'NH₄⁺', 60)], h=95),
                                scheme([('m', 'CCCC(N)=O', 'butyramide', 140), ('+',), ('t', 'OH⁻', 60), ('>', 'heat', ''), ('m', 'CCCC(=O)[O-]', 'butyrate', 140), ('+',), ('t', 'NH₃', 60)], h=95)], w=720, row_h=125)},
         "items": ["Amides <b>resist hydrolysis</b>: plain water does nothing, even with long heating. Acid or base (or an enzyme) is needed.",
                   "<b>Acidic</b>: carboxylic acid + ammonium salt. <b>Basic</b>: carboxylate salt + ammonia or amine.",
                   "Digestion of proteins is enzyme-catalysed amide (peptide) hydrolysis (Chapter 7)."],
         "notes": "FGOB 17.4 (Example: butyramide)."})
    add({"t": "bullets", "sec": 4, "lo": LO5, "title": "Amides in medicine",
         "items": ["<b>Penicillins</b> contain a strained four-membered ring amide, the <b>β-lactam</b>. It reacts with an enzyme bacteria need to build their cell walls.",
                   "Resistant bacteria make <b>β-lactamase</b>, an enzyme that hydrolyses the β-lactam amide and inactivates the drug.",
                   "<b>Amide local anaesthetics</b> (lidocaine) are stable in plasma and broken down slowly in the liver, so they last longer than esters such as procaine.",
                   "Other amide drugs: paracetamol, many barbiturates, and peptide drugs such as insulin."],
         "side": {"h": "Ester or amide?", "body": "An extra \"i\" before -caine means amide: l<b>i</b>docaine, bup<b>i</b>vacaine. No extra \"i\": ester (procaine, benzocaine)."},
         "notes": "Original pharmacy links."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO5, "title": "Condensation polymers: nylon and polyester",
         "fig": {"cap": "Repeating units. Each link forms with loss of water.",
                 "data": stack([scheme([('m', 'OC(=O)CCCCC(=O)O', 'adipic acid', 180), ('+',), ('m', 'NCCCCCCN', 'hexanediamine', 180), ('>', '− H₂O', ''), ('m', '*NCCCCCCNC(=O)CCCCC(=O)*', 'nylon-66 (polyamide)', 300)], h=90),
                                scheme([('m', 'OC(=O)c1ccc(cc1)C(=O)O', 'terephthalic acid', 200), ('+',), ('m', 'OCCO', 'ethylene glycol', 120), ('>', '− H₂O', ''), ('m', '*OCCOC(=O)c1ccc(cc1)C(=O)*', 'PET (polyester)', 260)], h=90)], w=860, row_h=125)},
         "items": ["Monomers with <b>two</b> functional groups link again and again. Diacid + diamine → <b>polyamide</b> (nylon); diacid + diol → <b>polyester</b> (PET).",
                   "Nylon: sutures, ropes, toothbrush bristles. PET: drink bottles, fabrics, and knitted tubes that replace damaged blood vessels.",
                   "Silk, wool and proteins are natural polyamides."],
         "notes": "FGOB 17.3, 17.5."})
    add({"t": "check", "sec": 4, "lo": LO5, "title": "Quick check",
         "q": "Which compound is an amide?",
         "opts": ["CH<sub>3</sub>CONHCH<sub>3</sub>", "CH<sub>3</sub>CH<sub>2</sub>NHCH<sub>3</sub>", "CH<sub>3</sub>COOCH<sub>3</sub>", "CH<sub>3</sub>COO<sup>−</sup>NH<sub>4</sub><sup>+</sup>"], "ans": 0,
         "why": "N bonded to a carbonyl carbon: N-methylacetamide. (B is an amine, C an ester, D a salt.)", "notes": "Answer A."})
    add({"t": "check", "sec": 4, "lo": LO5, "title": "Quick check",
         "q": "Why are amides not basic, while amines are?",
         "opts": ["The N lone pair is pulled towards the C=O and does not accept H<sup>+</sup>", "Amides have no nitrogen", "Amides are ionic", "Amides are insoluble in water"], "ans": 0,
         "why": "In amines the lone pair is free to accept a proton; in amides it is shared with the carbonyl group.", "notes": "Answer A."})

    # ================= wrap-up =================
    add({"t": "table", "title": "Four families side by side",
         "head": ["Family", "Group", "H-bonds to each other?", "Acid or base?", "Key reactions"],
         "rows": [["Carboxylic acid", "–COOH", "yes (dimers), very high bp", "weak acid", "+ base → salt; + alcohol → ester; + amine → amide"],
                  ["Ester", "–COOR′", "no", "neutral", "hydrolysis (acid ⇌; base → salt = saponification)"],
                  ["Amine", "RNH<sub>2</sub>, R<sub>2</sub>NH, R<sub>3</sub>N", "1°, 2° yes; 3° no", "weak base", "+ acid → amine salt"],
                  ["Amide", "–CONH–", "yes (if N–H), very high mp", "neutral", "hydrolysis needs acid, base or enzyme"]],
         "widths": [2.0, 1.8, 2.6, 1.4, 4.0],
         "caption": "Acids and amines are the parents; esters and amides are their condensation products.",
         "notes": "Original comparison."})
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Carboxylic acids", "RCOOH; -oic acid; C1 = carboxyl carbon; α = C2; dimers → high bp"],
        ["Acidity", "weak acids; smaller pK<sub>a</sub> = stronger; Cl increases acidity; + NaOH/NaHCO<sub>3</sub> → -ate salts (+ CO<sub>2</sub>)"],
        ["Esters", "RCOOR′; alkyl + -ate; fruity smells; acid + alcohol ⇌ ester + water (H<sup>+</sup>)"],
        ["Ester hydrolysis", "acid: reversible → acid + alcohol; base: saponification → salt + alcohol"],
        ["Amines", "1°/2°/3° by groups on N; alkyl groups + -amine; weak bases; HCl salts are water-soluble"],
        ["Alkaloids", "basic plant amines: caffeine, nicotine, morphine; extracted with acid"],
        ["Amides", "RCONH<sub>2</sub>; -amide, N- for groups on N; not basic; acid + amine → amide + water"],
        ["Polymers", "diacid + diamine → nylon; diacid + diol → polyester"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 30 min)", "Attempt the Chapter 4 tutorial",
                   "Play the Chapter 4 game to find your weak outcomes", "Next chapter: Carbohydrates"],
         "attrib": "Adapted from LibreTexts (Ball, Hill &amp; Scott; FGOB), CC BY-NC-SA 3.0. Acid dimers, amide naming with N-, the aspirin and paracetamol syntheses and the pharmacy links are original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"]})
    return S
