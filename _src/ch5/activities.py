"""PHD125 Chapter 5 · activities: before class, after class, tutorial.
(Ball 16.x) and (FGOB 20.x) items adapt those sources; chirality-in-drugs, sugar alcohols and pharmacy items are original.
Tutorial weighting: chirality and monosaccharides about 30%, cyclic forms and reactions about 35%, di- and polysaccharides about 35%."""
from figs import mol
from sugars import fischer, haworth, GLC, D_GALACTOSE

TITLE = 'Carbohydrates'
ATTRIB = ("Adapted from <i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 16, and <i>Fundamentals of General Organic and "
          "Biological Chemistry</i> 20.3–20.7, LibreTexts, CC BY-NC-SA 3.0. Chirality and drug questions, sugar alcohols and pharmacy scenarios are original "
          "material by Dr. NAM. Shared under CC BY-NC-SA for non-commercial teaching.")


def pic(uri, maxw=260):
    return f'<img src="{uri}" alt="structure" style="display:block;max-width:min(100%,{maxw}px);height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch5", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH5_PreLecture.pdf",
    "title": "Before class: sugars, rings and mirror images",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 5 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "One building block",
             "html": "<p>Glucose, C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>, is an aldehyde with an –OH on almost every carbon. Plants make it from CO<sub>2</sub> and water using sunlight, then join glucose units into <b>starch</b> (food store) and <b>cellulose</b> (fibre). Table sugar is glucose joined to fructose.</p>"},
            {"type": "read", "h": "Left and right hands",
             "html": "<p>In Chapter 2 you met the <b>chiral carbon</b>: a carbon with four different groups. Such a molecule has a mirror image that cannot be placed on top of it, like your hands. Glucose has four chiral carbons. Enzymes and drug receptors can tell the mirror images apart.</p>"},
            {"type": "read", "h": "Sugars curl up",
             "html": "<p>In Chapter 3 you saw that an aldehyde reacts with an alcohol to form a <b>hemiacetal</b>. Glucose contains both groups in one molecule, so in water it bends round and forms a <b>ring</b>. The ring can close in two ways, called α and β, and that small difference decides whether we can digest a carbohydrate.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "A chiral carbon is bonded to:", "opts": ["four different groups", "two identical groups", "a double bond", "four hydrogen atoms"], "ans": 0, "why": "Chapter 2."},
            {"type": "mcq", "lo": "Recap", "q": "An aldehyde reacts with an alcohol to form a:", "opts": ["hemiacetal", "ketone", "carboxylic acid", "ether"], "ans": 0, "why": "Chapter 3: this is how sugar rings form."},
            {"type": "mcq", "lo": "Recap", "q": "Benedict's reagent turns brick-red with:", "opts": ["aldehydes", "ketones such as acetone", "alcohols", "ethers"], "ans": 0, "why": "Cu<sup>2+</sup> is reduced to Cu<sub>2</sub>O (Chapter 3)."},
            {"type": "mcq", "lo": "CH5-LO1", "q": "The molecular formula of glucose is:", "opts": ["C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>", "C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>", "C<sub>6</sub>H<sub>6</sub>", "CH<sub>2</sub>O"], "ans": 0, "why": "C<sub>12</sub>H<sub>22</sub>O<sub>11</sub> is a disaccharide such as sucrose."},
            {"type": "match", "lo": "CH5-LO5", "q": "Match each carbohydrate to its type.", "left": ["glucose", "sucrose", "starch"], "right": ["monosaccharide", "disaccharide", "polysaccharide"], "ans": [0, 1, 2], "why": "One, two or many sugar units."},
            {"type": "tf", "lo": "CH5-LO1", "q": "Two mirror-image forms of a drug always have the same effect in the body.", "ans": False, "why": "Thalidomide is the famous example: receptors and enzymes are chiral."},
            {"type": "mcq", "lo": "CH5-LO2", "q": "Glucose contains an aldehyde group. It is therefore called an:", "opts": ["aldose", "ketose", "alditol", "acetal"], "ans": 0, "why": "Aldehyde → aldose; ketone → ketose."},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Which sugar is in milk?", "opts": ["lactose", "sucrose", "maltose", "fructose"], "ans": 0, "why": "Lactose, milk sugar."},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Which do humans NOT digest?", "opts": ["cellulose", "starch", "sucrose", "glycogen"], "ans": 0, "why": "We lack an enzyme for its β links."},
            {"type": "self", "lo": "CH5-LO5", "q": "Many tablets contain lactose or starch as fillers. Suggest one reason a pharmacist might check the filler before dispensing.", "model": "A patient may be lactose intolerant, have galactosemia, follow a diet, or have diabetes and want to avoid sugars; some patients also avoid certain starches (for example gluten-containing wheat starch). Fillers are part of what the patient swallows."}]}]}

POST = {
    "topic": "ch5", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH5_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the six subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH5-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "5.1 · Introduction and chirality", "items": [
            {"type": "mcq", "lo": "CH5-LO1", "q": "Which compound has a chiral carbon?", "opts": ["CH<sub>3</sub>CH(OH)COOH", "CH<sub>3</sub>CH(OH)CH<sub>3</sub>", "HOCH<sub>2</sub>COCH<sub>2</sub>OH", "HOCH<sub>2</sub>CH(OH)CH<sub>2</sub>OH"], "ans": 0, "why": "Lactic acid C2: H, OH, CH<sub>3</sub>, COOH."},
            {"type": "fill", "lo": "CH5-LO1", "q": "How many stereoisomers are possible for a molecule with 3 chiral carbons?", "acc": ["8", "eight"], "ph": "a number", "why": "2<sup>3</sup> = 8."},
            {"type": "match", "lo": "CH5-LO1", "q": "Match each term to its meaning.", "left": ["enantiomers", "racemic mixture", "dextrorotatory", "levorotatory"], "right": ["non-superimposable mirror images", "50:50 mixture of enantiomers", "rotates light clockwise (+)", "rotates light anticlockwise (−)"], "ans": [0, 1, 2, 3], "why": "Ball 16.2."},
            {"type": "mcq", "lo": "CH5-LO1", "q": "Esomeprazole and levocetirizine are examples of:", "opts": ["single-enantiomer versions of racemic drugs", "sugar alcohols", "disaccharides", "glycosides"], "ans": 0, "why": "es- (S) and levo- prefixes mark one enantiomer."}]},
        {"h": "5.2 · Monosaccharides", "items": [
            {"type": "mcq", "lo": "CH5-LO2", "q": "Classify this sugar." + pic(fischer('CH₂OH', [('C=O',), ('H', 'OH'), ('H', 'OH')], 'CH₂OH'), 180), "opts": ["ketopentose", "aldopentose", "ketohexose", "aldotetrose"], "ans": 0, "why": "Five carbons; the C=O is at C2 (ketone)."},
            {"type": "mcq", "lo": "CH5-LO2", "q": "Is the sugar above D or L?", "opts": ["D: the OH on C4 is on the right", "L: the C=O is at C2", "D: the C=O is at the top", "neither: it has no chiral carbon"], "ans": 0, "why": "Look at the chiral carbon furthest from the C=O (C4): OH right → D. It is D-ribulose."},
            {"type": "match", "lo": "CH5-LO2", "q": "Match each sugar to its other name.", "left": ["glucose", "fructose", "galactose"], "right": ["dextrose (blood sugar)", "levulose (fruit sugar)", "brain sugar", "malt sugar"], "ans": [0, 1, 2], "why": "Malt sugar is maltose (Ball 16.3)."},
            {"type": "tf", "lo": "CH5-LO2", "q": "D-glucose and D-galactose differ only in the position of the –OH on C4.", "ans": True, "why": "They are C4 epimers."}]},
        {"h": "5.3 · Cyclic forms", "items": [
            {"type": "mcq", "lo": "CH5-LO3", "q": "Identify this structure." + pic(haworth(GLC('a')), 240), "opts": ["α-D-glucose", "β-D-glucose", "β-D-galactose", "α-D-fructose"], "ans": 0, "why": "Six-membered ring, C4–OH down (glucose), C1–OH down (α)."},
            {"type": "mcq", "lo": "CH5-LO3", "q": "In a Haworth projection, a group that was on the right in the Fischer projection points:", "opts": ["down", "up", "into the ring", "it disappears"], "ans": 0, "why": "Right → down, left → up (FGOB 20.3)."},
            {"type": "fill", "lo": "CH5-LO3", "q": "What is the name for the slow change in optical rotation as α- and β-glucose interconvert in water?", "acc": ["mutarotation"], "ph": "one word", "why": "Equilibrium about 36% α, 64% β."},
            {"type": "mcq", "lo": "CH5-LO3", "q": "Fructose forms a five-membered ring because:", "opts": ["the C5–OH adds to the C2 ketone", "the C6–OH adds to C1", "it has no carbonyl group", "it is an L sugar"], "ans": 0, "why": "Ring of four carbons and one oxygen: a furanose."}]},
        {"h": "5.4 · Reactions of monosaccharides", "items": [
            {"type": "match", "lo": "CH5-LO4", "q": "Give the product of each reaction of D-glucose.", "left": ["Benedict's reagent (oxidation)", "H<sub>2</sub>/Ni (reduction)", "methanol, H<sup>+</sup>"], "right": ["gluconic acid", "sorbitol", "methyl glucoside", "fructose"], "ans": [0, 1, 2], "why": "Oxidation of –CHO; reduction of C=O; glycoside formation."},
            {"type": "tf", "lo": "CH5-LO4", "q": "Fructose gives a positive Benedict's test even though it is a ketose.", "ans": True, "why": "In the basic reagent it rearranges to an aldose form (Ball 16.5)."},
            {"type": "mcq", "lo": "CH5-LO4", "q": "Mannitol given by IV infusion acts as:", "opts": ["an osmotic diuretic", "an anticoagulant", "a laxative glycoside", "a sweetener only"], "ans": 0, "why": "It draws water and reduces pressure in the brain."}]},
        {"h": "5.5 · Disaccharides", "items": [
            {"type": "match", "lo": "CH5-LO5", "q": "Match each disaccharide to its linkage.", "left": ["maltose", "lactose", "sucrose"], "right": ["α-1,4", "β-1,4", "α-1,β-2", "α-1,6"], "ans": [0, 1, 2], "why": "α-1,6 is the branch link in amylopectin."},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Sucrose is a non-reducing sugar because:", "opts": ["both anomeric carbons are used in the glycosidic bond", "it contains fructose", "it is too sweet", "it has no –OH groups"], "ans": 0, "why": "Neither ring can open to an aldehyde."},
            {"type": "fill", "lo": "CH5-LO5", "q": "What is the name of the 1:1 glucose–fructose mixture made by hydrolysing sucrose?", "acc": ["invert sugar", "invert syrup"], "ph": "two words", "why": "It rotates light the opposite way to sucrose."}]},
        {"h": "5.6 · Polysaccharides", "items": [
            {"type": "match", "lo": "CH5-LO5", "q": "Match each polysaccharide to its structure.", "left": ["amylose", "amylopectin", "glycogen", "cellulose"], "right": ["unbranched, α-1,4", "branched every 25–30 units", "branched every 8–12 units", "unbranched, β-1,4"], "ans": [0, 1, 2, 3], "why": "FGOB 20.7."},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Iodine gives a red-brown colour with:", "opts": ["glycogen", "amylose", "cellulose", "glucose"], "ans": 0, "why": "Branching breaks up the helix; amylose gives blue-black."},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Which is used as an injectable anticoagulant?", "opts": ["heparin", "dextrin", "cellulose", "amylopectin"], "ans": 0, "why": "A sulfated polysaccharide."}]},
        {"h": "Pharmacy scenario · Sugar at the counter", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Encik Hafiz has type 2 diabetes and needs a cough syrup. His daughter, who is lactose intolerant, asks whether the lactose in her antihistamine tablets will upset her. Hafiz also asks why his glucometer strips must only be used for blood glucose.</p>"},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Which syrup is most suitable for Hafiz?", "opts": ["a sugar-free syrup sweetened with sorbitol or an artificial sweetener", "Syrup BP (about 67% sucrose)", "a honey-based syrup", "any syrup: sucrose is not a sugar"], "ans": 0, "why": "Sucrose and honey raise blood glucose."},
            {"type": "mcq", "lo": "CH5-LO5", "q": "Lactose intolerance is caused by:", "opts": ["too little of the enzyme lactase", "a missing enzyme that converts galactose to glucose", "an allergy to milk protein", "too much sucrase"], "ans": 0, "why": "The missing galactose enzyme is galactosemia, a different condition."},
            {"type": "mcq", "lo": "CH5-LO4", "q": "Glucometer strips measure only glucose because they use:", "opts": ["the enzyme glucose oxidase", "Benedict's reagent", "iodine", "Tollens' reagent"], "ans": 0, "why": "Enzymes are specific; Benedict's reacts with any reducing sugar."},
            {"type": "self", "lo": "CH5-LO5", "q": "What would you tell Hafiz's daughter about the lactose in her tablets?", "model": "The amount of lactose in a tablet is usually very small, and most people with lactose intolerance tolerate it without symptoms. If she is very sensitive, a lactose-free brand can be chosen, or she can take the tablet with food. (Galactosemia would be different: that needs strict avoidance.)"}]}]}

TUT = {
    "topic": "ch5", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH5_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (38 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 50.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 5 game, or move on to Chapter 6.",
    "sections": []}
T = TITLE
A = [
    ("CH5-LO1", "Carbohydrates are best defined as:", ["polyhydroxy aldehydes or ketones, or compounds that hydrolyse to them", "compounds of carbon and water molecules", "esters of glycerol", "polymers of amino acids"], 0, "Ball 16.1."),
    ("CH5-LO1", "Enantiomers differ in their:", ["direction of rotation of plane-polarised light", "boiling points", "molecular formulas", "solubility in water"], 0, "All other physical properties are the same."),
    ("CH5-LO2", "An aldohexose has how many chiral carbons in its open-chain form?", ["4", "3", "5", "6"], 0, "C2–C5; 2<sup>4</sup> = 16 stereoisomers."),
    ("CH5-LO2", "A sugar is assigned D or L by the –OH on:", ["the chiral carbon furthest from the carbonyl group", "C1", "C2", "the anomeric carbon"], 0, "The penultimate carbon (Ball 16.2)."),
    ("CH5-LO3", "Anomers differ only at:", ["the anomeric carbon", "C4", "the CH<sub>2</sub>OH group", "every chiral carbon"], 0, "C1 for aldoses, C2 for fructose."),
    ("CH5-LO3", "At equilibrium in water, D-glucose is mostly:", ["β-D-glucose (about 64%)", "α-D-glucose (about 64%)", "open-chain glucose", "fructose"], 0, "About 36% α, 64% β, under 0.02% open chain."),
    ("CH5-LO4", "A reducing sugar is one that:", ["reduces Benedict's or Tollens' reagent", "is reduced to a sugar alcohol", "cannot be hydrolysed", "has no –OH groups"], 0, "Cu<sup>2+</sup> → Cu<sub>2</sub>O."),
    ("CH5-LO4", "Sorbitol is formed from glucose by:", ["reduction", "oxidation", "hydrolysis", "glycoside formation"], 0, "C=O → CH–OH."),
    ("CH5-LO5", "Maltose is hydrolysed to:", ["two glucose", "glucose + fructose", "glucose + galactose", "two fructose"], 0, "Maltase or dilute acid."),
    ("CH5-LO5", "The glycosidic linkage in lactose is:", ["β-1,4", "α-1,4", "α-1,β-2", "α-1,6"], 0, "Galactose C1 (β) to glucose C4."),
    ("CH5-LO5", "Glycogen differs from amylopectin in being:", ["more highly branched", "unbranched", "made of fructose", "linked β-1,4"], 0, "Branches every 8–12 units instead of 25–30."),
    ("CH5-LO5", "Which statement about cellulose is correct?", ["Its glucose units are joined by β-1,4 links", "It is a reducing sugar", "It gives a blue-black colour with iodine", "Humans digest it with amylase"], 0, "FGOB 20.7."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH5-LO1", "marks": 6, "level": "C3",
     "q": "(a) Define a chiral carbon and explain what enantiomers are. (2 marks) (b) State whether each compound has a chiral carbon, and identify it if so: (i) CH<sub>3</sub>CH(OH)COOH (lactic acid) (ii) CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub> (iii) HOCH<sub>2</sub>CH(OH)CH<sub>2</sub>OH (glycerol). (3 marks) (c) Ibuprofen is sold as a racemic mixture. Explain why a racemic mixture does not rotate plane-polarised light. (1 mark)",
     "hint": "Check each carbon for four different groups. Two identical CH<sub>2</sub>OH groups rule a carbon out.",
     "work": "(a) A chiral carbon is bonded to four different groups. Enantiomers are a pair of stereoisomers that are non-superimposable mirror images of each other. (b)(i) Yes: C2 (H, OH, CH<sub>3</sub>, COOH) (ii) Yes: C2 (H, OH, CH<sub>3</sub>, CH<sub>2</sub>CH<sub>3</sub>) (iii) No: C2 carries two identical CH<sub>2</sub>OH groups. (c) It contains equal amounts of the two enantiomers, which rotate light by equal amounts in opposite directions, so the rotations cancel.",
     "rubric": [["Chiral carbon: four different groups", 1], ["Enantiomers: non-superimposable mirror images", 1], ["Lactic acid: yes, C2", 1], ["2-Butanol: yes, C2", 1], ["Glycerol: no (two identical CH<sub>2</sub>OH)", 1], ["Equal and opposite rotations cancel", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH5-LO2", "marks": 8, "level": "C3",
     "q": "The Fischer projection of a monosaccharide is shown." + pic(fischer(*D_GALACTOSE), 200) + "(a) Classify it by its carbonyl group and by the number of carbons. (2 marks) (b) How many chiral carbons does it have, and what is the maximum number of stereoisomers with this skeleton? (2 marks) (c) Is it a D or an L sugar? Explain. (2 marks) (d) Name the sugar, and state how it differs from D-glucose. (2 marks)",
     "hint": "Count carbons and find the C=O. For D or L, look only at the chiral carbon nearest the bottom CH<sub>2</sub>OH.",
     "work": "(a) Aldose (aldehyde at C1); hexose (6 carbons): an aldohexose. (b) Four chiral carbons (C2–C5); 2<sup>4</sup> = 16 stereoisomers. (c) D: the –OH on C5, the chiral carbon furthest from the carbonyl group, is on the right. (d) D-galactose. It differs from D-glucose only at C4, where its –OH is on the left.",
     "rubric": [["Aldose", 1], ["Hexose", 1], ["4 chiral carbons", 1], ["16 stereoisomers", 1], ["D sugar", 1], ["Reason: C5–OH on the right", 1], ["D-galactose", 1], ["Differs at C4 (OH on the left)", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH5-LO3", "marks": 8, "level": "C3",
     "q": "(a) Explain how D-glucose forms a six-membered ring in water, and name the functional group formed. (2 marks) (b) Draw the Haworth projections of α-D-glucose and β-D-glucose, and label the anomeric carbon. (4 marks) (c) A freshly made solution of pure α-D-glucose has a specific rotation of +112°, which changes to +52.7°. Explain. (2 marks)",
     "hint": "Which –OH reaches the C1 aldehyde to make a six-membered ring? In Haworth projections, right → down.",
     "work": "(a) The –OH on C5 adds to the C1 aldehyde (C=O) in the same molecule, giving a ring of five carbons and one oxygen; the new group is a hemiacetal. (b)" + pic(haworth(GLC('a'), caption='α-D-glucose'), 240) + pic(haworth(GLC('b'), caption='β-D-glucose'), 240) + "In both: ring O at the back right; C2–OH down, C3–OH up, C4–OH down, CH<sub>2</sub>OH up on C5. α: C1–OH down; β: C1–OH up. C1 is the anomeric carbon. (c) In water the ring opens and recloses (mutarotation), forming an equilibrium mixture of about 36% α and 64% β (plus a trace of open chain), whose rotation is +52.7°.",
     "rubric": [["C5–OH adds to the C1 aldehyde", 1], ["Hemiacetal", 1], ["Correct ring with O and CH<sub>2</sub>OH up", 1], ["C2, C3, C4 –OH positions correct", 1], ["α: C1–OH down; β: C1–OH up", 1], ["Anomeric carbon (C1) labelled", 1], ["Ring opens and recloses: mutarotation", 1], ["Equilibrium ≈ 36% α, 64% β", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH5-LO4", "marks": 8, "level": "C4",
     "q": "Four solutions are warmed with Benedict's reagent: glucose, fructose, sucrose and methyl α-D-glucoside. (a) Predict the result for each and give a reason. (4 marks) (b) The sucrose solution is warmed with dilute HCl, neutralised, and tested again. It now turns brick-red. Explain, naming the products. (2 marks) (c) Name the product of reducing glucose with H<sub>2</sub>/Ni, and give one pharmaceutical use of it. (2 marks)",
     "hint": "Can the ring open to give an aldehyde? Look for a free anomeric –OH.",
     "work": "(a) Glucose: brick-red; its ring opens to an aldehyde (reducing sugar). Fructose: brick-red; in the basic reagent it rearranges to an aldose form. Sucrose: stays blue; both anomeric carbons are in the glycosidic bond, so it cannot open (non-reducing). Methyl α-D-glucoside: stays blue; the anomeric carbon is locked as a glycoside. (b) Acid hydrolyses sucrose to glucose and fructose (invert sugar), which are reducing sugars. (c) Sorbitol (glucitol); a sweetener in sugar-free syrups and lozenges (or a laxative).",
     "rubric": [["Glucose: brick-red, reducing (opens to aldehyde)", 1], ["Fructose: brick-red (rearranges in base)", 1], ["Sucrose: blue, both anomeric C used", 1], ["Glycoside: blue, anomeric C locked", 1], ["Hydrolysis of sucrose", 1], ["Glucose + fructose (invert sugar) are reducing", 1], ["Sorbitol", 1], ["A valid use", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH5-LO5", "marks": 8, "level": "C4",
     "q": "(a) Compare maltose and lactose in terms of their monosaccharide units and glycosidic linkage. (2 marks) (b) A patient gets bloating and diarrhoea after drinking milk. Name the condition and explain its cause. (2 marks) (c) Compare amylose, amylopectin and cellulose in terms of linkage and branching. (3 marks) (d) Microcrystalline cellulose is a common tablet filler. Explain why it passes through the gut undigested. (1 mark)",
     "hint": "Look at both the type of link (α or β) and where it joins (1,4 or 1,6).",
     "work": "(a) Maltose: two glucose units joined α-1,4. Lactose: galactose + glucose joined β-1,4. (b) Lactose intolerance: too little of the enzyme lactase, so lactose is not hydrolysed; it draws water into the colon and bacteria ferment it, producing acid and gas. (c) Amylose: α-1,4, unbranched (helix). Amylopectin: α-1,4 with α-1,6 branches every 25–30 units. Cellulose: β-1,4, unbranched straight chains that hydrogen bond into fibres. (d) Humans have no enzyme that hydrolyses β-1,4-glycosidic bonds.",
     "rubric": [["Maltose: glucose + glucose, α-1,4", 1], ["Lactose: galactose + glucose, β-1,4", 1], ["Lactose intolerance", 1], ["Too little lactase (cause and effect)", 1], ["Amylose: α-1,4 unbranched", 1], ["Amylopectin: α-1,4 + α-1,6 branches", 1], ["Cellulose: β-1,4 unbranched", 1], ["No human enzyme for β-1,4", 1]]}]})
