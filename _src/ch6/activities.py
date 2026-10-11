"""PHD125 Chapter 6 · activities: before class, after class, tutorial.
(FGOB 23.x) items adapt that source; reactions of fats, phospholipid and drug items are original.
Tutorial weighting: fatty acids and triacylglycerols about 45%, hydrolysis about 20%, phospholipids and membranes about 20%, steroids about 15%."""
from figs import mol
from lipidfigs import triglyceride

TITLE = 'Lipids'
ATTRIB = ("Adapted from <i>Fundamentals of General Organic and Biological Chemistry</i> 23.1, 23.2, 23.6 and 23.7 (remixed from Ball, Hill &amp; Scott, chapter 17), "
          "LibreTexts, CC BY-NC-SA 3.0. Questions on reactions of fats, phospholipids and pharmacy scenarios are original material by Dr. NAM. "
          "Shared under CC BY-NC-SA for non-commercial teaching.")


def pic(uri, maxw=420):
    return f'<img src="{uri}" alt="structure" style="display:block;max-width:min(100%,{maxw}px);height:auto;background:#fff;border-radius:10px;margin:8px 0">'


MIXED = triglyceride(['(CH₂)₁₄CH₃', '(CH₂)₇CH=CH(CH₂)₇CH₃', '(CH₂)₁₆CH₃'])
TRISTEARIN = triglyceride(['(CH₂)₁₆CH₃'] * 3)

PRE = {
    "topic": "ch6", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH6_PreLecture.pdf",
    "title": "Before class: the molecules that hate water",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 6 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "Defined by what they avoid",
             "html": "<p>Lipids are not one functional group. They are the molecules in living things that dissolve in oily, nonpolar solvents but not in water: fats and oils, waxes, the phospholipids of cell membranes, and steroids such as cholesterol.</p>"},
            {"type": "read", "h": "Esters again",
             "html": "<p>Most lipids are <b>esters</b> (Chapter 4). A fat is glycerol (a triol, Chapter 3) joined to three long-chain carboxylic acids called <b>fatty acids</b>. Boil a fat with NaOH and the esters split: you get glycerol and soap. That is saponification, which you met in Chapter 4.</p>"},
            {"type": "read", "h": "Kinks and walls",
             "html": "<p>A cis C=C (Chapter 2) puts a kink in a fatty acid chain, so oils are liquid and butter is solid. Phospholipids have a water-loving head and two water-fearing tails; in water they line up into a double layer, the <b>cell membrane</b>. Every drug you swallow has to cross it.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "Glycerol, HOCH<sub>2</sub>CH(OH)CH<sub>2</sub>OH, is a:", "opts": ["triol (alcohol with three –OH groups)", "carboxylic acid", "ester", "ketone"], "ans": 0, "why": "Chapter 3."},
            {"type": "mcq", "lo": "Recap", "q": "Basic hydrolysis of an ester with NaOH gives:", "opts": ["a carboxylate salt and an alcohol", "an amide", "an alkene", "a ketone"], "ans": 0, "why": "Saponification (Chapter 4)."},
            {"type": "mcq", "lo": "Recap", "q": "Adding H<sub>2</sub> (Ni catalyst) to C=C bonds is called:", "opts": ["hydrogenation", "hydration", "hydrolysis", "halogenation"], "ans": 0, "why": "Chapter 2 addition reactions."},
            {"type": "mcq", "lo": "CH6-LO1", "q": "Lipids are best described as compounds that:", "opts": ["dissolve in nonpolar solvents but not in water", "contain nitrogen", "are always solids", "are sugars"], "ans": 0, "why": "They are defined by solubility."},
            {"type": "tf", "lo": "CH6-LO1", "q": "Fats provide more energy per gram than carbohydrates.", "ans": True, "why": "About 9 kcal/g versus 4 kcal/g."},
            {"type": "mcq", "lo": "CH6-LO2", "q": "Why is olive oil liquid but butter solid?", "opts": ["Olive oil has more unsaturated (kinked) fatty acids", "Olive oil has no glycerol", "Butter is a wax", "Butter contains water"], "ans": 0, "why": "Kinked chains pack poorly."},
            {"type": "match", "lo": "CH6-LO1", "q": "Match each lipid to its class.", "left": ["palm oil", "beeswax", "cholesterol", "lecithin"], "right": ["triacylglycerol", "wax", "steroid", "phospholipid"], "ans": [0, 1, 2, 3], "why": "Four of the classes in this chapter."},
            {"type": "mcq", "lo": "CH6-LO4", "q": "Cell membranes are mainly made of:", "opts": ["a double layer of phospholipids", "cellulose", "triglycerides", "waxes"], "ans": 0, "why": "The lipid bilayer."},
            {"type": "mcq", "lo": "CH6-LO5", "q": "Hydrocortisone cream contains a:", "opts": ["steroid", "wax only", "phospholipid", "sugar"], "ans": 0, "why": "A corticosteroid."},
            {"type": "self", "lo": "CH6-LO3", "q": "Why does an opened bottle of cooking oil eventually smell bad, even with the cap on?", "model": "Oxygen in the air (and light and warmth) slowly attacks the C=C bonds in the unsaturated fatty acids, breaking them into small smelly aldehydes and acids: the oil turns rancid. Moisture can also hydrolyse the esters, releasing smelly free fatty acids."}]}]}

POST = {
    "topic": "ch6", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH6_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH6-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "6.1–6.2 · Lipids and fatty acids", "items": [
            {"type": "match", "lo": "CH6-LO1", "q": "Give the shorthand for each fatty acid.", "left": ["stearic acid", "oleic acid", "linoleic acid", "palmitic acid"], "right": ["C18:0", "C18:1", "C18:2", "C16:0", "C18:3"], "ans": [0, 1, 2, 3], "why": "Carbons : double bonds (FGOB 23.2)."},
            {"type": "mcq", "lo": "CH6-LO1", "q": "Which statement about natural unsaturated fatty acids is correct?", "opts": ["Their double bonds are usually cis, which kinks the chain", "They are usually trans", "They have odd numbers of carbons", "They are branched"], "ans": 0, "why": "FGOB 23.2."},
            {"type": "fill", "lo": "CH6-LO1", "q": "Name one of the two essential fatty acids.", "acc": ["linoleic acid", "linoleic", "alpha-linolenic acid", "α-linolenic acid", "linolenic acid", "alpha-linolenic", "linolenic"], "ph": "name", "why": "The body cannot make linoleic or α-linolenic acid."},
            {"type": "mcq", "lo": "CH6-LO1", "q": "EPA and DHA in fish oil are:", "opts": ["ω-3 fatty acids", "ω-6 fatty acids", "saturated fatty acids", "steroids"], "ans": 0, "why": "First C=C at the third carbon from the CH<sub>3</sub> end."}]},
        {"h": "6.3–6.4 · Waxes and triacylglycerols", "items": [
            {"type": "mcq", "lo": "CH6-LO2", "q": "Carnauba wax is used in pharmacy to:", "opts": ["polish coated tablets", "make soap", "lower cholesterol", "make suppositories melt"], "ans": 0, "why": "It gives tablets a shine."},
            {"type": "mcq", "lo": "CH6-LO2", "q": "Identify this compound." + pic(MIXED, 360), "opts": ["a mixed triacylglycerol", "a simple triacylglycerol", "a wax", "a phospholipid"], "ans": 0, "why": "Glycerol with three different fatty acids."},
            {"type": "match", "lo": "CH6-LO3", "q": "Match each process to what happens.", "left": ["hydrogenation", "oxidative rancidity", "hydrolytic rancidity"], "right": ["H<sub>2</sub> adds to C=C", "O<sub>2</sub> breaks chains at C=C into aldehydes", "water splits esters, releasing free fatty acids", "fat turns into a steroid"], "ans": [0, 1, 2], "why": "Vitamin E and BHT slow oxidation."},
            {"type": "mcq", "lo": "CH6-LO2", "q": "An oil with a higher iodine value has:", "opts": ["more C=C bonds", "longer chains", "more glycerol", "fewer ester groups"], "ans": 0, "why": "Iodine adds across C=C."}]},
        {"h": "6.5 · Hydrolysis", "items": [
            {"type": "mcq", "lo": "CH6-LO3", "q": "Pancreatic lipase hydrolyses a triglyceride to:", "opts": ["glycerol and fatty acids", "glycerol and soap", "cholesterol", "glucose"], "ans": 0, "why": "With water; base would give soap."},
            {"type": "fill", "lo": "CH6-LO3", "q": "How many moles of NaOH are needed to saponify one mole of a triacylglycerol?", "acc": ["3", "three"], "ph": "a number", "why": "One per ester bond."},
            {"type": "tf", "lo": "CH6-LO3", "q": "In a soap micelle, the nonpolar tails point outwards into the water.", "ans": False, "why": "Tails point inwards into the grease; heads face the water."}]},
        {"h": "6.6–6.7 · Phospholipids and membranes", "items": [
            {"type": "mcq", "lo": "CH6-LO4", "q": "Lecithin is:", "opts": ["phosphatidylcholine", "a steroid", "a wax", "a triglyceride"], "ans": 0, "why": "An emulsifier from soy or egg."},
            {"type": "match", "lo": "CH6-LO4", "q": "Match each transport mode to an example.", "left": ["simple diffusion", "facilitated diffusion", "active transport"], "right": ["O<sub>2</sub> entering a cell", "glucose through a GLUT protein", "the Na<sup>+</sup>/K<sup>+</sup> pump", "a protein swallowed whole"], "ans": [0, 1, 2], "why": "Only active transport uses ATP."},
            {"type": "mcq", "lo": "CH6-LO4", "q": "Which drug form crosses lipid membranes most easily?", "opts": ["the uncharged free base", "the hydrochloride ion", "a large protein", "a sugar"], "ans": 0, "why": "Ions do not dissolve in the hydrophobic core."}]},
        {"h": "6.8 · Steroids", "items": [
            {"type": "mcq", "lo": "CH6-LO5", "q": "The steroid nucleus has:", "opts": ["three six-membered rings and one five-membered ring, fused", "four benzene rings", "a glycerol backbone", "two fatty acids"], "ans": 0, "why": "Rings A, B, C, D."},
            {"type": "match", "lo": "CH6-LO5", "q": "Match each steroid to its role.", "left": ["cortisol", "aldosterone", "testosterone", "cholic acid"], "right": ["raises blood glucose; anti-inflammatory", "makes kidneys keep Na<sup>+</sup>", "male sex hormone", "bile acid for fat digestion"], "ans": [0, 1, 2, 3], "why": "FGOB 23.6."},
            {"type": "mcq", "lo": "CH6-LO5", "q": "\"Good\" cholesterol refers to:", "opts": ["HDL, which carries cholesterol back to the liver", "LDL", "triglycerides", "bile salts"], "ans": 0, "why": "High HDL lowers heart-disease risk."}]},
        {"h": "Pharmacy scenario · Fats at the counter", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Puan Rosnah, 58, has just been prescribed <b>simvastatin</b>. She asks whether she should switch from palm oil to olive oil, whether fish-oil capsules will help, and whether her old hydrocortisone cream is \"the same kind of steroid that bodybuilders use\".</p>"},
            {"type": "mcq", "lo": "CH6-LO5", "q": "How does simvastatin lower her cholesterol?", "opts": ["It blocks HMG-CoA reductase, so her liver makes less cholesterol", "It dissolves fat in the gut", "It is a bile salt", "It hydrogenates fats"], "ans": 0, "why": "Statins lower LDL."},
            {"type": "mcq", "lo": "CH6-LO2", "q": "Compared with palm oil, olive oil contains:", "opts": ["more unsaturated (oleic) and less saturated (palmitic) acid", "more saturated fat", "more trans fat", "more cholesterol"], "ans": 0, "why": "Olive oil is about 71% oleic acid; palm oil about 45% palmitic."},
            {"type": "mcq", "lo": "CH6-LO5", "q": "Hydrocortisone and anabolic steroids are:", "opts": ["both steroids, but different classes with different actions", "exactly the same drug", "both phospholipids", "both waxes"], "ans": 0, "why": "Hydrocortisone is a corticosteroid; anabolic steroids are androgens."},
            {"type": "self", "lo": "CH6-LO5", "q": "Summarise your advice to Puan Rosnah.", "model": "Take simvastatin as prescribed (it blocks cholesterol synthesis in the liver). Replacing some saturated fat with unsaturated oils such as olive oil, limiting fried and processed foods with trans fats, and regular exercise help. Fish oil (ω-3) mainly lowers triglycerides; check with her doctor before adding it. Hydrocortisone is a corticosteroid for inflammation, not an anabolic (androgen) steroid; use it thinly for short periods."}]}]}

TUT = {
    "topic": "ch6", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH6_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (38 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 50.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 6 game, or move on to Chapter 7.",
    "sections": []}
T = TITLE
A = [
    ("CH6-LO1", "Fatty acids usually contain:", ["an even number of carbons in an unbranched chain", "an odd number of carbons", "a benzene ring", "a branched chain"], 0, "Typically 12–20 carbons (FGOB 23.2)."),
    ("CH6-LO1", "Oleic acid (C18:1) is:", ["monounsaturated", "saturated", "polyunsaturated", "a trans fatty acid"], 0, "One cis C=C."),
    ("CH6-LO1", "Arachidonic acid is the starting material for:", ["prostaglandins", "cholesterol", "glycogen", "waxes"], 0, "Blocked by NSAIDs via COX."),
    ("CH6-LO2", "A wax is an ester of:", ["a long-chain fatty acid and a long-chain alcohol", "glycerol and three fatty acids", "phosphoric acid and choline", "cholesterol and glucose"], 0, "FGOB 23.2."),
    ("CH6-LO2", "Most animal fats are solid because they contain mainly:", ["saturated fatty acids", "cis-unsaturated fatty acids", "glycerol", "water"], 0, "Straight chains pack closely."),
    ("CH6-LO3", "Partial hydrogenation of vegetable oil can produce:", ["trans fatty acids", "phospholipids", "cholesterol", "glycerol"], 0, "Some cis C=C are isomerised to trans."),
    ("CH6-LO3", "Which slows oxidative rancidity?", ["vitamin E (tocopherol)", "water", "light", "copper ions"], 0, "An antioxidant."),
    ("CH6-LO3", "Saponification of a fat produces glycerol and:", ["salts of fatty acids (soap)", "free fatty acids", "fatty alcohols", "trans fats"], 0, "Basic hydrolysis."),
    ("CH6-LO4", "A molecule with both a hydrophilic and a hydrophobic part is:", ["amphipathic", "hydrophobic", "saturated", "nonsaponifiable"], 0, "Soaps and phospholipids."),
    ("CH6-LO4", "Sphingomyelin is rich in:", ["the myelin sheath around nerves", "adipose tissue", "tooth enamel", "blood plasma only"], 0, "A sphingolipid."),
    ("CH6-LO5", "Which is a nonsaponifiable lipid?", ["cholesterol", "tristearin", "lecithin", "carnauba wax"], 0, "Steroids have no ester bonds."),
    ("CH6-LO5", "Bile salts aid digestion by:", ["emulsifying fats into small droplets", "hydrolysing proteins", "oxidising glucose", "forming cholesterol"], 0, "They are amphipathic (FGOB 23.6)."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH6-LO1", "marks": 8, "level": "C3",
     "q": "Three C18 fatty acids: stearic acid (mp 70 °C), oleic acid (mp 16 °C) and linoleic acid (mp −5 °C). (a) Classify each as saturated, monounsaturated or polyunsaturated, and give its shorthand notation. (3 marks) (b) Explain the trend in melting points. (2 marks) (c) Explain what is meant by an essential fatty acid, and name one ω-3 fatty acid. (2 marks) (d) State how aspirin is linked to fatty acid chemistry. (1 mark)",
     "hint": "Count the C=C bonds. Think about how kinked chains pack.",
     "work": "(a) Stearic acid: saturated, C18:0. Oleic acid: monounsaturated, C18:1. Linoleic acid: polyunsaturated, C18:2. (b) Each cis C=C puts a kink in the chain, so the chains cannot pack closely; dispersion forces are weaker and the melting point falls as the number of C=C increases. (c) A fatty acid the body cannot make, so it must come from the diet. ω-3: α-linolenic acid (or EPA or DHA). (d) Aspirin blocks cyclooxygenase, the enzyme that converts arachidonic acid (a fatty acid) into prostaglandins.",
     "rubric": [["Stearic: saturated, C18:0", 1], ["Oleic: monounsaturated, C18:1", 1], ["Linoleic: polyunsaturated, C18:2", 1], ["Cis C=C kinks the chain; poor packing", 1], ["Weaker dispersion forces → lower mp", 1], ["Essential: cannot be made by the body", 1], ["Correct ω-3 example", 1], ["Aspirin blocks COX / prostaglandin synthesis", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH6-LO2", "marks": 8, "level": "C4",
     "q": "The structure of a triacylglycerol is shown." + pic(MIXED, 380) + "(a) Name the functional group that joins each fatty acid to the backbone, and name the alcohol that forms the backbone. (2 marks) (b) Is this a simple or a mixed triglyceride? Give a reason. (2 marks) (c) It is completely hydrogenated with H<sub>2</sub>/Ni. Which fatty acid chain changes, and what does it become? Explain the effect on the melting point. (2 marks) (d) Explain how partial hydrogenation can produce trans fats, and why these are a health concern. (2 marks)",
     "hint": "Look at the three tails: are they all the same? Which one has a C=C?",
     "work": "(a) Ester groups; glycerol. (b) Mixed: it contains three different fatty acids (palmitic, oleic and stearic). (c) The oleic acid chain (with the C=C) gains H<sub>2</sub> and becomes a stearic acid chain; the product has only saturated chains, which pack closely, so its melting point rises. (d) During partial hydrogenation some cis C=C bonds that are not hydrogenated are converted to the trans form; trans fats raise LDL cholesterol and the risk of heart disease.",
     "rubric": [["Ester groups", 1], ["Glycerol", 1], ["Mixed", 1], ["Reason: three different fatty acids", 1], ["Oleic chain → stearic chain", 1], ["Higher melting point (saturated, packs well)", 1], ["Cis → trans during partial hydrogenation", 1], ["Raise LDL / heart disease risk", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH6-LO3", "marks": 8, "level": "C3",
     "q": "Tristearin is shown." + pic(TRISTEARIN, 360) + "(a) Write a balanced equation (condensed formulas or words with formulas) for the saponification of tristearin with sodium hydroxide, and name the products. (3 marks) (b) Explain how the soap formed removes grease from skin. (3 marks) (c) Explain why this soap forms a scum in hard water. (1 mark) (d) Give the products when tristearin is hydrolysed by pancreatic lipase in the gut. (1 mark)",
     "hint": "One NaOH per ester bond. Draw the soap anion as a head and a tail.",
     "work": "(a) Tristearin + 3 NaOH → glycerol + 3 CH<sub>3</sub>(CH<sub>2</sub>)<sub>16</sub>COO<sup>−</sup>Na<sup>+</sup>; the products are glycerol and sodium stearate (soap). (b) The stearate anion is amphipathic: a long nonpolar tail and an ionic –COO<sup>−</sup> head. The tails dissolve in the grease, the heads face the water, forming micelles; the charged micelles repel each other and are rinsed away. (c) Ca<sup>2+</sup> and Mg<sup>2+</sup> ions in hard water form insoluble calcium and magnesium stearate. (d) Glycerol and stearic acid.",
     "rubric": [["Reactants: tristearin + 3 NaOH", 1], ["Products: glycerol + 3 sodium stearate", 1], ["Products named", 1], ["Amphipathic: nonpolar tail, ionic head", 1], ["Tails in grease, heads in water: micelle", 1], ["Micelles rinsed away (repel each other)", 1], ["Ca<sup>2+</sup>/Mg<sup>2+</sup> form insoluble salts", 1], ["Glycerol + stearic acid", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH6-LO4", "marks": 8, "level": "C4",
     "q": "(a) Compare the structure of phosphatidylcholine (lecithin) with that of a triacylglycerol. (2 marks) (b) Explain why phospholipids form a bilayer when placed in water. (2 marks) (c) Name two components of a cell membrane other than phospholipids, and give the role of each. (2 marks) (d) Lidocaine is injected as lidocaine hydrochloride, but it must cross nerve membranes as the free base. Explain why the free base crosses more easily. (2 marks)",
     "hint": "How many fatty acids does each have, and what is on the third carbon of glycerol?",
     "work": "(a) Both have a glycerol backbone with ester-linked fatty acids. A triacylglycerol has three fatty acids; phosphatidylcholine has two, and its third –OH carries a phosphate joined to choline, a charged polar head. (b) Phospholipids are amphipathic: the polar heads face the water on both sides, while the nonpolar tails turn inwards away from water, forming a double layer. (c) Any two: cholesterol (keeps membrane fluidity in range); integral proteins (channels, carriers, receptors); peripheral proteins (signalling, support); sugar chains (cell recognition). (d) The free base is uncharged, so it can dissolve in and pass through the hydrophobic core of the bilayer; the protonated (charged) form cannot.",
     "rubric": [["Triglyceride: 3 fatty acids", 1], ["Phospholipid: 2 fatty acids + phosphate–choline head", 1], ["Amphipathic: heads to water", 1], ["Tails inside, away from water → bilayer", 1], ["First component and role", 1], ["Second component and role", 1], ["Free base is uncharged", 1], ["Can pass through hydrophobic core; ion cannot", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH6-LO5", "marks": 6, "level": "C2",
     "q": "(a) Describe the steroid nucleus. (1 mark) (b) Give three roles of cholesterol in the body. (3 marks) (c) Explain why HDL is called \"good\" cholesterol. (1 mark) (d) Explain how statins lower blood cholesterol. (1 mark)",
     "hint": "Cholesterol is the starting material for several important molecules.",
     "work": "(a) Four fused rings: three six-membered (A, B, C) and one five-membered (D). (b) Any three: component of cell membranes; starting material for bile acids/salts; for steroid hormones (cortisol, aldosterone, sex hormones); for vitamin D. (c) HDL carries excess cholesterol from tissues back to the liver for removal, lowering heart-disease risk. (d) They inhibit HMG-CoA reductase, an enzyme the liver needs to make cholesterol.",
     "rubric": [["Four fused rings (3 six-, 1 five-membered)", 1], ["Role 1", 1], ["Role 2", 1], ["Role 3", 1], ["HDL carries cholesterol to the liver", 1], ["Statins inhibit HMG-CoA reductase", 1]]}]})
