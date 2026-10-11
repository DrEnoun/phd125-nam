"""PHD125 Chapter 3 · activities: before class, after class, tutorial.
(Ball 14.E) and (FGOB 14.x/15.x) items adapt those sources; SN1/SN2 and pharmacy items are original.
Tutorial weighting: about 40% alcohols (incl. SN1/SN2), 20% ethers and thiols, 40% aldehydes and ketones."""
from figs import mol

TITLE = 'Organic Compounds that Contain Oxygen and Sulphur'
ATTRIB = ("Adapted from <i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 14 and exercises 14.E, and <i>Fundamentals of General Organic and "
          "Biological Chemistry</i> 14.4–14.9 and 15.1–15.5, LibreTexts, CC BY-NC-SA 3.0. SN1 and SN2 items, colour tests and pharmacy scenarios are original "
          "material by Dr. NAM. Shared under CC BY-NC-SA for non-commercial teaching.")


def img(smi, w=260, h=120, **k):
    return f'<img src="{mol(smi, w, h, **k)}" alt="structure" style="display:block;max-width:100%;height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch3", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH3_PreLecture.pdf",
    "title": "Before class: one oxygen changes everything",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 3 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "Four families, one atom",
             "html": "<p>Put an <b>–OH</b> on a carbon chain and you have an <b>alcohol</b> (ethanol). Put an O <b>between</b> two carbons: an <b>ether</b>. Swap the O of an alcohol for S: a <b>thiol</b>. Join C and O with a double bond: a <b>carbonyl</b> group, found in <b>aldehydes</b> and <b>ketones</b>.</p>"},
            {"type": "read", "h": "Hydrogen bonds again",
             "html": "<p>An –OH group lets molecules hydrogen bond to each other and to water. That is why ethanol (46 g/mol) is a liquid that mixes with water, while propane (44 g/mol) is a gas that does not. Watch for this idea all chapter.</p>"},
            {"type": "read", "h": "A new kind of reaction",
             "html": "<p>In Chapter 2, reagents <b>added</b> to C=C bonds. In this chapter you meet <b>substitution</b> by a <b>nucleophile</b>: an electron-rich particle such as OH<sup>−</sup> swaps places with a halogen. This is how a haloalkane becomes an alcohol, and how some anticancer drugs attach to DNA.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "Which intermolecular force is strongest?", "opts": ["dispersion", "dipole–dipole", "hydrogen bonding", "they are all equal"], "ans": 2, "why": "Hydrogen bonds (O–H, N–H, F–H) are the strongest intermolecular forces."},
            {"type": "mcq", "lo": "Recap", "q": "Propene + H<sub>2</sub>O (acid catalyst) gives mainly:", "opts": ["1-propanol", "2-propanol", "propane", "propanal"], "ans": 1, "why": "Markovnikov's rule (Chapter 2)."},
            {"type": "mcq", "lo": "Recap", "q": "Which bond is polar?", "opts": ["C–H", "C–C", "C–O", "H–H"], "ans": 2, "why": "O is more electronegative than C."},
            {"type": "match", "lo": "CH3-LO1", "q": "Match each functional group to its family.", "left": ["R–OH", "R–O–R′", "R–SH", "R–CHO"], "right": ["alcohol", "ether", "thiol", "aldehyde", "ketone"], "ans": [0, 1, 2, 3], "why": "Ketone is the extra option: R–CO–R′."},
            {"type": "fill", "lo": "CH3-LO1", "q": "Which ending do alcohol names have? Type it with a hyphen, e.g. -ane.", "acc": ["-ol", "ol"], "ph": "e.g. -ane", "why": "Ethanol, propanol. Do not confuse with -al (aldehydes)."},
            {"type": "tf", "lo": "CH3-LO1", "q": "Ethanol dissolves in water because it can hydrogen bond with water molecules.", "ans": True, "why": "Small alcohols (1–3 C) mix completely with water."},
            {"type": "mcq", "lo": "CH3-LO2", "q": "A nucleophile is:", "opts": ["an electron-rich species that attacks a δ+ carbon", "a positive ion that removes electrons", "a catalyst", "a noble gas"], "ans": 0, "why": "Examples: OH<sup>−</sup>, H<sub>2</sub>O, CN<sup>−</sup>."},
            {"type": "mcq", "lo": "CH3-LO3", "q": "Which is in hand sanitiser?", "opts": ["ethanol", "ethanal", "ethane", "ethanethiol"], "ans": 0, "why": "60–80% ethanol or 2-propanol."},
            {"type": "mcq", "lo": "CH3-LO5", "q": "Acetone (nail-polish remover) belongs to which family?", "opts": ["alcohol", "aldehyde", "ketone", "ether"], "ans": 2, "why": "C=O between two carbons: propanone."},
            {"type": "self", "lo": "CH3-LO4", "q": "LPG and natural gas have no smell, yet you can smell a leak. Guess what is added and why.", "model": "A small amount of a thiol such as ethanethiol, which has a very strong smell, is added so leaks can be detected. Thiols are the sulfur relatives of alcohols (3.2)."}]}]}

POST = {
    "topic": "ch3", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH3_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the three subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH3-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "3.1 · Alcohols: names, classes, properties", "items": [
            {"type": "match", "lo": "CH3-LO1", "q": "Classify each alcohol.", "left": ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH", "CH<sub>3</sub>CH(OH)CH<sub>3</sub>", "(CH<sub>3</sub>)<sub>3</sub>COH", "cyclohexanol"], "right": ["1°", "2°", "3°"], "ans": [0, 1, 2, 1], "why": "Count the carbons bonded to the C–OH carbon."},
            {"type": "mcq", "lo": "CH3-LO1", "q": "Name this alcohol." + img('CC(O)C(C)CC', 240, 110), "opts": ["3-methyl-2-pentanol", "3-methyl-4-pentanol", "2-ethyl-1-butanol", "hexanol"], "ans": 0, "why": "Five-carbon chain numbered from the end nearer –OH: OH on C2, CH<sub>3</sub> on C3 (Ball 14.2)."},
            {"type": "mcq", "lo": "CH3-LO1", "q": "Arrange in order of increasing water solubility: 1-butanol, methanol, 1-octanol. (Ball 14.E)", "opts": ["1-octanol < 1-butanol < methanol", "methanol < 1-butanol < 1-octanol", "1-butanol < methanol < 1-octanol", "all equal"], "ans": 0, "why": "Longer chains make alcohols more hydrocarbon-like."},
            {"type": "mcq", "lo": "CH3-LO1", "q": "Why is propylene glycol, but not ethylene glycol, used as a drug solvent?", "opts": ["Propylene glycol is metabolised to harmless pyruvate; ethylene glycol to toxic oxalate", "Ethylene glycol has no –OH", "Propylene glycol is insoluble in water", "They are the same compound"], "ans": 0, "why": "Ball 14.6."}]},
        {"h": "3.1 · SN1 and SN2", "items": [
            {"type": "match", "lo": "CH3-LO2", "q": "Match each feature to SN1 or SN2.", "left": ["one step", "goes through a carbocation", "best for 1° haloalkanes", "best for 3° haloalkanes", "rate depends on [R–X] only", "inverts a chiral carbon"], "right": ["SN1", "SN2"], "ans": [1, 0, 1, 0, 0, 1], "why": "SN2: one step, backside attack, 1°, both species in the rate. SN1: carbocation, 3°, rate on R–X only."},
            {"type": "mcq", "lo": "CH3-LO2", "q": "Which haloalkane reacts fastest by SN2?", "opts": ["CH<sub>3</sub>CH<sub>2</sub>Br", "(CH<sub>3</sub>)<sub>3</sub>CBr", "(CH<sub>3</sub>)<sub>2</sub>CHBr", "they are equal"], "ans": 0, "why": "Primary: least crowded for backside attack."},
            {"type": "mcq", "lo": "CH3-LO2", "q": "Which is the best leaving group?", "opts": ["I<sup>−</sup>", "Cl<sup>−</sup>", "F<sup>−</sup>", "OH<sup>−</sup>"], "ans": 0, "why": "I<sup>−</sup> > Br<sup>−</sup> > Cl<sup>−</sup>; OH<sup>−</sup> is poor."},
            {"type": "fill", "lo": "CH3-LO2", "q": "Name the alcohol formed when (CH<sub>3</sub>)<sub>3</sub>CBr is warmed with water.", "acc": ["2-methyl-2-propanol", "2-methylpropan-2-ol", "tert-butyl alcohol", "t-butyl alcohol", "tert-butanol"], "ph": "IUPAC or common name", "why": "SN1: carbocation (CH<sub>3</sub>)<sub>3</sub>C<sup>+</sup>, then water attacks."},
            {"type": "mcq", "lo": "CH3-LO2", "q": "Bromoethane is heated with KOH dissolved in ethanol. The main organic product is:", "opts": ["ethene", "ethanol", "diethyl ether", "ethanal"], "ans": 0, "why": "Hot ethanolic KOH favours elimination; aqueous OH<sup>−</sup> would give ethanol."}]},
        {"h": "3.1 · Dehydration and oxidation", "items": [
            {"type": "match", "lo": "CH3-LO3", "q": "Give the product of each alcohol with acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>.", "left": ["2-pentanol", "cyclohexanol", "2-methyl-2-propanol", "ethanol (excess oxidant)"], "right": ["2-pentanone", "cyclohexanone", "no reaction", "ethanoic acid", "ethanal"], "ans": [0, 1, 2, 3], "why": "2° → ketone; 3° → none; 1° with excess oxidant → acid (Ball 14.E)."},
            {"type": "mcq", "lo": "CH3-LO3", "q": "2-Methyl-2-propanol with excess conc. H<sub>2</sub>SO<sub>4</sub> at 180 °C gives: (Ball 14.E)", "opts": ["2-methylpropene (isobutylene)", "2-methylpropanal", "di-tert-butyl ether", "no reaction"], "ans": 0, "why": "Dehydration (elimination of water) to the alkene."},
            {"type": "tf", "lo": "CH3-LO3", "q": "C<sub>4</sub>H<sub>10</sub>O → C<sub>4</sub>H<sub>8</sub>O is an oxidation. (Ball 14.E)", "ans": True, "why": "Two H atoms are removed."},
            {"type": "mcq", "lo": "CH3-LO3", "q": "Why is methanol far more dangerous to drink than ethanol?", "opts": ["It is oxidised to formaldehyde and formic acid", "It is a thiol", "It cannot be metabolised", "It is an alkane"], "ans": 0, "why": "These products damage the optic nerve (Ball 14.4)."}]},
        {"h": "3.2 · Ethers and thiols", "items": [
            {"type": "mcq", "lo": "CH3-LO4", "q": "Name CH<sub>3</sub>OCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>. (Ball 14.E)", "opts": ["methyl propyl ether", "butanol", "propyl methanol", "methoxyethane"], "ans": 0, "why": "Name both groups, then add 'ether'."},
            {"type": "mcq", "lo": "CH3-LO4", "q": "Diethyl ether (bp 35 °C) and 1-butanol (bp 117 °C) are isomers. Which statement is true?", "opts": ["Both dissolve in water to a similar small extent (about 8 g/100 mL)", "The ether hydrogen bonds to itself", "1-Butanol is insoluble in water", "The ether boils higher"], "ans": 0, "why": "Both can accept hydrogen bonds from water (FGOB 14.7)."},
            {"type": "fill", "lo": "CH3-LO4", "q": "Write the condensed formula of tert-butyl mercaptan, a natural-gas odorant. (FGOB 14.8)", "acc": ["(CH3)3CSH"], "cs": True, "show": "(CH<sub>3</sub>)<sub>3</sub>CSH", "ph": "e.g. CH3CH2SH", "why": "A tert-butyl group bonded to –SH."},
            {"type": "mcq", "lo": "CH3-LO4", "q": "Mild oxidation of two thiol molecules gives:", "opts": ["a disulfide R–S–S–R", "an ether", "a sulfate", "an alkene"], "ans": 0, "why": "2 R–SH + [O] → R–S–S–R + H<sub>2</sub>O."}]},
        {"h": "3.3 · Aldehydes and ketones", "items": [
            {"type": "mcq", "lo": "CH3-LO5", "q": "Name this compound." + img('CCCC(C)C=O', 240, 110), "opts": ["2-methylpentanal", "4-methylpentanal", "2-methylpentanone", "hexanal"], "ans": 0, "why": "The aldehyde carbon is C1, so the methyl is on C2 (FGOB 15.2)."},
            {"type": "mcq", "lo": "CH3-LO5", "q": "Which has the highest boiling point? (similar molar masses)", "opts": ["propanal", "butane", "methoxyethane", "1-propanol"], "ans": 3, "why": "Hydrogen bonding (alcohol) > dipole (aldehyde) > weak dipole (ether) > dispersion (alkane)."},
            {"type": "match", "lo": "CH3-LO5", "q": "Predict each test result for propanal and propanone.", "left": ["propanal + Tollens'", "propanone + Tollens'", "propanal + Benedict's", "propanone + Benedict's"], "right": ["silver mirror", "brick-red precipitate", "no change"], "ans": [0, 2, 1, 2], "why": "Only the aldehyde is oxidised."},
            {"type": "mcq", "lo": "CH3-LO5", "q": "Reduction of butanone with H<sub>2</sub>/Ni gives:", "opts": ["2-butanol", "1-butanol", "butanal", "butanoic acid"], "ans": 0, "why": "Ketone → 2° alcohol."}]},
        {"h": "Pharmacy scenario · The diabetic patient", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Encik Faizal has type 1 diabetes and has missed his insulin for two days. His wife notices a fruity, nail-polish-remover smell on his breath. At the pharmacy counter he asks for something for nausea. You also know that old urine-sugar tests used <b>Benedict's reagent</b>.</p>"},
            {"type": "mcq", "lo": "CH3-LO5", "q": "Which compound causes the smell on his breath?", "opts": ["acetone (a ketone)", "ethanol", "diethyl ether", "ethanethiol"], "ans": 0, "why": "In uncontrolled diabetes, ketone bodies including acetone build up (FGOB 15.4)."},
            {"type": "mcq", "lo": "CH3-LO5", "q": "Benedict's reagent detected glucose in urine because glucose behaves like:", "opts": ["an aldehyde (a reducing sugar)", "a ketone that resists oxidation", "an ether", "a thiol"], "ans": 0, "why": "Glucose's aldehyde group reduces blue Cu<sup>2+</sup> to brick-red Cu<sub>2</sub>O (Chapter 5)."},
            {"type": "self", "lo": "CH3-LO5", "q": "What should the pharmacist do, and why?", "model": "Refer him urgently to a doctor or emergency department: the smell of acetone with nausea in a person with type 1 diabetes who has missed insulin suggests diabetic ketoacidosis, a medical emergency. Do not just sell an anti-nausea product."}]}]}

TUT = {
    "topic": "ch3", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH3_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (36 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 48.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 3 game, or move on to Chapter 4.",
    "sections": []}
T = TITLE
A = [
    ("CH3-LO1", "Which alcohol is tertiary?", ["2-methyl-2-propanol", "2-propanol", "1-butanol", "2-methyl-1-propanol"], 0, "The C–OH carbon is bonded to three carbons."),
    ("CH3-LO1", "Arrange in order of increasing boiling point: ethanol, methanol, 1-propanol. (Ball 14.E)", ["methanol < ethanol < 1-propanol", "1-propanol < ethanol < methanol", "ethanol < methanol < 1-propanol", "all equal"], 0, "Larger molecules, stronger dispersion forces in addition to H-bonding."),
    ("CH3-LO2", "In an SN2 reaction, the nucleophile attacks:", ["from the side opposite the leaving group", "a carbocation", "the leaving group", "the hydrogen atoms"], 0, "Backside attack, one step."),
    ("CH3-LO2", "Which statement about SN1 is correct?", ["Its rate depends only on [haloalkane]", "It occurs in one step", "It is fastest for 1° haloalkanes", "It inverts a chiral carbon completely"], 0, "The slow step is formation of the carbocation."),
    ("CH3-LO3", "Oxidation of 2-propanol gives:", ["propanone", "propanal", "propanoic acid", "propene"], 0, "2° → ketone."),
    ("CH3-LO3", "Ethanol with conc. H<sub>2</sub>SO<sub>4</sub> at 140 °C and excess ethanol gives mainly:", ["diethyl ether", "ethene", "ethanal", "ethanoic acid"], 0, "Intermolecular dehydration (Ball 14.E)."),
    ("CH3-LO4", "Ethers have lower boiling points than isomeric alcohols because they:", ["cannot hydrogen bond to each other", "are ionic", "are heavier", "contain sulfur"], 0, "No O–H in ethers."),
    ("CH3-LO4", "The functional group of a thiol is:", ["–SH", "–S–S–", "–OH", "–SO<sub>4</sub>"], 0, "R–SH (mercaptans)."),
    ("CH3-LO5", "The IUPAC name of CH<sub>3</sub>CH<sub>2</sub>CHO is:", ["propanal", "propanone", "propanol", "1-propanal"], 0, "Aldehyde: -al; C1 needs no number."),
    ("CH3-LO5", "Which reagent gives a silver mirror with aldehydes?", ["Tollens'", "Benedict's", "bromine water", "conc. H<sub>2</sub>SO<sub>4</sub>"], 0, "Ag<sup>+</sup> is reduced to Ag."),
    ("CH3-LO5", "Which alcohol is oxidised to 3-pentanone?", ["3-pentanol", "1-pentanol", "2-methyl-2-butanol", "pentanal"], 0, "2° alcohol at C3."),
    ("CH3-LO5", "Formalin, used to preserve specimens, is a solution of:", ["methanal (formaldehyde)", "ethanal", "propanone", "methanol"], 0, "37–40% formaldehyde in water (FGOB 15.4)."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH3-LO1", "marks": 6, "level": "C3",
     "q": "(a) Name and classify (1°, 2° or 3°) each alcohol: (i) CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>3</sub> (ii) (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>OH (iii) (CH<sub>3</sub>)<sub>2</sub>C(OH)CH<sub>2</sub>CH<sub>3</sub>. (3 marks) (b) Methanol (32 g/mol) boils at 65 °C but ethane (30 g/mol) boils at −89 °C. Explain. (2 marks) (c) Explain why 1-octanol is much less soluble in water than ethanol. (1 mark)",
     "hint": "For names, the longest chain must contain the C–OH carbon. For (b), name the intermolecular forces.",
     "work": "(a)(i) 2-butanol, 2° (ii) 2-methyl-1-propanol, 1° (iii) 2-methyl-2-butanol, 3°. (b) Methanol molecules form hydrogen bonds through their –OH groups, which need much more energy to break than the weak dispersion forces between nonpolar ethane molecules. (c) The long nonpolar C<sub>8</sub> chain dominates, so 1-octanol behaves more like a hydrocarbon; ethanol's single OH is enough for its short chain.",
     "rubric": [["(i) 2-butanol, 2°", 1], ["(ii) 2-methyl-1-propanol, 1°", 1], ["(iii) 2-methyl-2-butanol, 3°", 1], ["Methanol: hydrogen bonding", 1], ["Ethane: only weak dispersion forces", 1], ["Long nonpolar chain in 1-octanol", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH3-LO2", "marks": 9, "level": "C4",
     "q": "Two haloalkanes are converted into alcohols: <b>P</b> = 1-bromobutane with warm aqueous NaOH; <b>Q</b> = 2-bromo-2-methylpropane with water. (a) State the mechanism (SN1 or SN2) for each and give one reason for each choice. (4 marks) (b) Draw the structure of the alcohol formed in each case and name it. (2 marks) (c) For <b>Q</b>, draw the intermediate and name its type. (2 marks) (d) What would you expect if 1-bromobutane were heated with KOH in ethanol instead? (1 mark)",
     "hint": "Look at the class of each haloalkane and at the strength of the nucleophile. Think about which carbocation is stable.",
     "work": "(a) P: SN2: it is a primary haloalkane (uncrowded for backside attack) with a strong nucleophile (OH<sup>−</sup>). Q: SN1: it is tertiary (too crowded for SN2) and forms a stable 3° carbocation; water is a weak nucleophile. (b) P → CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH, 1-butanol. Q → (CH<sub>3</sub>)<sub>3</sub>COH, 2-methyl-2-propanol." + img('C[C+](C)C', 160, 100) + "(c) (CH<sub>3</sub>)<sub>3</sub>C<sup>+</sup>, a tertiary carbocation (drawn above). (d) Elimination: but-1-ene, CH<sub>2</sub>=CHCH<sub>2</sub>CH<sub>3</sub>, forms instead of the alcohol.",
     "rubric": [["P: SN2", 1], ["Reason for P (1° or strong nucleophile)", 1], ["Q: SN1", 1], ["Reason for Q (3°, stable carbocation)", 1], ["1-butanol", 1], ["2-methyl-2-propanol", 1], ["Carbocation drawn correctly", 1], ["Named tertiary carbocation", 1], ["Elimination to an alkene (1-butene)", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH3-LO3", "marks": 7, "level": "C3",
     "q": "Three unlabelled bottles contain 1-propanol, 2-propanol and 2-methyl-2-propanol. (a) Describe what you would see when each is warmed with acidified potassium dichromate, and name any organic product. (5 marks) (b) Write an equation for the dehydration of 2-propanol to an alkene, stating the conditions. (2 marks)",
     "hint": "Which class has no H on the C–OH carbon? What colour is dichromate before and after reacting?",
     "work": "(a) 1-Propanol: orange → green; product propanal (then propanoic acid with excess oxidant). 2-Propanol: orange → green; product propanone. 2-Methyl-2-propanol: stays orange, no reaction (3°). (b) CH<sub>3</sub>CH(OH)CH<sub>3</sub> → CH<sub>3</sub>CH=CH<sub>2</sub> + H<sub>2</sub>O, with excess concentrated H<sub>2</sub>SO<sub>4</sub> at about 180 °C.",
     "rubric": [["Orange → green for 1° and 2°", 1], ["1-propanol → propanal (or propanoic acid)", 1], ["2-propanol → propanone", 1], ["3° stays orange", 1], ["Reason: no H on the C–OH carbon", 1], ["Correct equation to propene", 1], ["Conditions: conc. H<sub>2</sub>SO<sub>4</sub>, ~180 °C", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH3-LO4", "marks": 6, "level": "C2",
     "q": "(a) Draw and give the common name of the ether CH<sub>3</sub>CH<sub>2</sub>OCH(CH<sub>3</sub>)<sub>2</sub>. (2 marks) (b) Explain why diethyl ether was replaced as an anaesthetic. (1 mark) (c) Write an equation for the oxidation of ethanethiol to diethyl disulfide. (2 marks) (d) State why disulfide bridges are important in proteins. (1 mark)",
     "hint": "Name the two groups on the oxygen. In (c), two thiols lose two H atoms.",
     "work": "(a) Ethyl isopropyl ether (Ball 14.E)." + img('CCOC(C)C', 180, 100) + "(b) It is highly flammable and causes nausea; halogenated ethers are safer to use. (c) 2 CH<sub>3</sub>CH<sub>2</sub>SH + [O] → CH<sub>3</sub>CH<sub>2</sub>S–SCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O. (d) They link parts of protein chains (between cysteine residues), holding the protein in its shape.",
     "rubric": [["Correct structure", 1], ["Ethyl isopropyl ether", 1], ["Flammable / nausea", 1], ["Correct reactants and product", 1], ["Balanced with H<sub>2</sub>O and [O]", 1], ["Holds protein shape (cysteine links)", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH3-LO5", "marks": 8, "level": "C4",
     "q": "Compounds <b>X</b> and <b>Y</b> both have the formula C<sub>3</sub>H<sub>6</sub>O. X gives a silver mirror with Tollens' reagent; Y does not. (a) Identify X and Y, giving their structures and IUPAC names. (2 marks) (b) Explain the Tollens' results. (2 marks) (c) Name the product when X is oxidised. (1 mark) (d) Give the products when X and Y are reduced with H<sub>2</sub>/Ni, and classify each alcohol. (2 marks) (e) Explain why propanal (bp 49 °C) boils higher than butane (bp −1 °C). (1 mark)",
     "hint": "C<sub>3</sub>H<sub>6</sub>O fits both an aldehyde and a ketone. Which one has an H on the carbonyl carbon?",
     "work": "(a) X = propanal, CH<sub>3</sub>CH<sub>2</sub>CHO; Y = propanone, CH<sub>3</sub>COCH<sub>3</sub>." + img('CCC=O', 160, 90) + img('CC(C)=O', 160, 90) + "(b) The aldehyde has an H on its carbonyl carbon, so it is easily oxidised; it reduces Ag<sup>+</sup> to Ag (silver mirror). The ketone resists oxidation. (c) Propanoic acid. (d) X → 1-propanol (1°); Y → 2-propanol (2°). (e) The polar C=O gives strong dipole–dipole forces; butane has only dispersion forces.",
     "rubric": [["X propanal (structure)", 1], ["Y propanone (structure)", 1], ["Aldehyde easily oxidised (H on C=O carbon)", 1], ["Ag<sup>+</sup> reduced to Ag; ketone does not react", 1], ["Propanoic acid", 1], ["1-propanol, 1°", 1], ["2-propanol, 2°", 1], ["Dipole–dipole vs dispersion", 1]]}]})
