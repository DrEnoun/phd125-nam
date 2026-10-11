"""PHD125 Chapter 8 · activities: before class, after class, tutorial.
Items on principles, HPLC, GC and ion exchange adapt Harvey (Analytical Chemistry 2.1 ch. 12; Instrumental Analysis 28.6);
TLC items, drug questions and pharmacy scenarios are original.
Tutorial weighting: principles and phases about 30%, TLC about 15%, instrumental methods about 30%, applications about 25%."""
from figs import mol

TITLE = 'Application of Chromatographic Methods in Pharmaceutical Analysis'
ATTRIB = ("Adapted from David Harvey, <i>Analytical Chemistry 2.1</i>, chapter 12, and <i>Instrumental Analysis</i> 28.6, LibreTexts, CC BY-NC-SA 4.0. "
          "TLC questions, drug questions and pharmacy scenarios are original material by Dr. NAM. "
          "Shared under CC BY-NC-SA for non-commercial teaching.")

PARA = 'CC(=O)Nc1ccc(O)cc1'
IBU = 'CC(C)Cc1ccc(cc1)C(C)C(=O)O'


def pic(uri, maxw=320):
    return f'<img src="{uri}" alt="structure" style="display:block;max-width:min(100%,{maxw}px);height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch8", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH8_PreLecture.pdf",
    "title": "Before class: a race between two phases",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 8 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "Like dissolves like, again",
             "html": "<p>Polar molecules attract polar molecules; nonpolar ones mix with nonpolar ones (Chapter 1). Groups such as –OH, –NH<sub>2</sub> and –COOH make a molecule more polar; long hydrocarbon chains make it less polar. Chromatography uses exactly this idea.</p>"},
            {"type": "read", "h": "A race between two phases",
             "html": "<p>In chromatography a <b>mobile phase</b> (a liquid or a gas) flows over a <b>stationary phase</b> (often a solid such as silica). A compound that sticks to the stationary phase moves slowly; one that prefers the mobile phase moves quickly. So a mixture spreads out into separate spots or peaks.</p>"},
            {"type": "read", "h": "Why it matters in pharmacy",
             "html": "<p>Every batch of medicine is tested: is it the right drug, is it pure, and is the dose correct? Hospitals measure drug levels in blood. Regulators look for hidden drugs in 'herbal' products. Most of these tests use <b>TLC</b>, <b>HPLC</b> or <b>GC</b>.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "Which molecule is the most polar?", "opts": ["methanol, CH<sub>3</sub>OH", "hexane, C<sub>6</sub>H<sub>14</sub>", "methane, CH<sub>4</sub>", "benzene, C<sub>6</sub>H<sub>6</sub>"], "ans": 0, "why": "The –OH group makes it polar and able to hydrogen bond."},
            {"type": "mcq", "lo": "Recap", "q": "Which group can form hydrogen bonds?", "opts": ["–OH", "–CH<sub>3</sub>", "–C≡C–", "–Cl"], "ans": 0, "why": "O–H is polar with a lone pair on O (Chapter 3)."},
            {"type": "mcq", "lo": "Recap", "q": "Above its pI, an amino acid carries a net:", "opts": ["negative charge", "positive charge", "zero charge", "it depends on temperature"], "ans": 0, "why": "Chapter 7."},
            {"type": "mcq", "lo": "CH8-LO1", "q": "In chromatography, the phase that moves is called the:", "opts": ["mobile phase", "stationary phase", "solid phase", "fixed phase"], "ans": 0, "why": "It carries the sample."},
            {"type": "tf", "lo": "CH8-LO1", "q": "A compound that sticks strongly to the stationary phase travels faster.", "ans": False, "why": "It is held back, so it travels slower."},
            {"type": "mcq", "lo": "CH8-LO2", "q": "Silica gel is:", "opts": ["polar", "nonpolar", "a gas", "an ion"], "ans": 0, "why": "Its surface is covered in –OH groups."},
            {"type": "mcq", "lo": "CH8-LO3", "q": "TLC stands for:", "opts": ["thin layer chromatography", "total liquid chromatography", "thermal layer chemistry", "test for liquid content"], "ans": 0, "why": "A thin layer of adsorbent on a plate."},
            {"type": "mcq", "lo": "CH8-LO4", "q": "In gas chromatography, the sample must be:", "opts": ["able to become a vapour without breaking down", "a solid salt", "a protein", "coloured"], "ans": 0, "why": "It is carried by a gas."},
            {"type": "mcq", "lo": "CH8-LO5", "q": "Which question does a pharmacy quality-control lab NOT need chromatography for?", "opts": ["the price of the tablet", "the identity of the drug", "the amount of drug", "the impurities present"], "ans": 0, "why": "The other three are standard tests."},
            {"type": "self", "lo": "CH8-LO1", "q": "Have you seen ink or food colouring spread out on wet paper or tissue? Describe what happened and suggest why the colours separated.", "model": "The water climbed up the paper and carried the dyes with it. Each dye is attracted to the paper and to the water by different amounts, so some dyes moved further than others and the colours spread into separate bands. That is paper chromatography."}]}]}

POST = {
    "topic": "ch8", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH8_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH8-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "8.1–8.2 · Principles", "items": [
            {"type": "match", "lo": "CH8-LO1", "q": "Match each type of chromatography to how the solute is held.", "left": ["adsorption", "partition", "ion exchange", "size exclusion"], "right": ["sticks to a solid surface", "dissolves in a liquid film", "attracted to fixed charges", "large molecules come out first"], "ans": [0, 1, 2, 3], "why": "Harvey 12.1."},
            {"type": "mcq", "lo": "CH8-LO1", "q": "'Gas chromatography' tells you that the:", "opts": ["mobile phase is a gas", "stationary phase is a gas", "sample is a gas only", "detector uses gas"], "ans": 0, "why": "If only one phase is named, it is the mobile phase."},
            {"type": "fill", "lo": "CH8-LO1", "q": "A peak has t<sub>r</sub> = 5.0 min and t<sub>m</sub> = 1.0 min. What is its retention factor k?", "acc": ["4", "4.0"], "ph": "a number", "why": "k = (5.0 − 1.0) ÷ 1.0 = 4.0."},
            {"type": "mcq", "lo": "CH8-LO1", "q": "Two peaks are fully (baseline) separated when the resolution R is at least:", "opts": ["1.5", "0.5", "1.0", "10"], "ans": 0, "why": "Harvey 12.2."}]},
        {"h": "8.3 · Stationary and mobile phases", "items": [
            {"type": "match", "lo": "CH8-LO2", "q": "Match each stationary phase to its polarity or use.", "left": ["silica gel", "C18 bonded silica", "cellulose paper", "sulfonated resin"], "right": ["polar adsorbent", "nonpolar, reversed phase", "holds water, partition", "cation exchanger"], "ans": [0, 1, 2, 3], "why": "8.3 and 8.5."},
            {"type": "mcq", "lo": "CH8-LO2", "q": "In reversed-phase HPLC, which elutes first?", "opts": ["the more polar compound", "the less polar compound", "the larger molecule", "the compound with the highest boiling point"], "ans": 0, "why": "The nonpolar C18 holds less polar compounds longer."},
            {"type": "fill", "lo": "CH8-LO2", "q": "Calculate P′ for a 50:50 water–methanol mobile phase (water 10.2, methanol 5.1). Give one decimal place.", "acc": ["7.7", "7.65", "7.6"], "ph": "a number", "why": "0.5(10.2) + 0.5(5.1) = 7.65 ≈ 7.7."},
            {"type": "tf", "lo": "CH8-LO2", "q": "In gradient elution, the composition of the mobile phase changes during the run.", "ans": True, "why": "Isocratic elution keeps it the same."}]},
        {"h": "8.4 · Thin layer chromatography", "items": [
            {"type": "fill", "lo": "CH8-LO3", "q": "A spot moves 2.4 cm and the solvent front moves 8.0 cm. What is R<sub>f</sub>?", "acc": ["0.3", "0.30"], "ph": "a number", "why": "2.4 ÷ 8.0 = 0.30."},
            {"type": "mcq", "lo": "CH8-LO3", "q": "Why must the solvent level in the tank be below the origin line?", "opts": ["so the spots are not washed off into the solvent pool", "so the plate dries faster", "so the R<sub>f</sub> is higher", "to save solvent"], "ans": 0, "why": "The spots would dissolve into the solvent instead of travelling up."},
            {"type": "match", "lo": "CH8-LO3", "q": "Match each way of showing spots to what it reveals.", "left": ["UV light, 254 nm", "ninhydrin spray", "iron(III) chloride spray", "Dragendorff's reagent"], "right": ["compounds that absorb UV (dark spots)", "amino acids (purple)", "phenols (coloured)", "alkaloids (orange)"], "ans": [0, 1, 2, 3], "why": "8.4."},
            {"type": "mcq", "lo": "CH8-LO3", "q": "A co-spot of a test sample with the standard gives one single spot. This:", "opts": ["supports that the test drug is the same as the standard", "proves the sample is 100% pure", "means the solvent was wrong", "means the sample contains no drug"], "ans": 0, "why": "Different compounds would usually split into two spots."}]},
        {"h": "8.5–8.7 · Ion exchange, HPLC and GC", "items": [
            {"type": "mcq", "lo": "CH8-LO4", "q": "A weak acid cation exchanger carries which group?", "opts": ["–COO<sup>−</sup>", "–SO<sub>3</sub><sup>−</sup>", "–N(CH<sub>3</sub>)<sub>3</sub><sup>+</sup>", "–NH<sub>3</sub><sup>+</sup>"], "ans": 0, "why": "Carboxylic acid: weak; sulfonic acid: strong."},
            {"type": "match", "lo": "CH8-LO4", "q": "Match each part of an HPLC to its job.", "left": ["pump", "loop injector", "C18 column", "UV detector"], "right": ["pushes the mobile phase at high pressure", "delivers an exact volume of sample", "separates the components", "signals each compound as it leaves"], "ans": [0, 1, 2, 3], "why": "Harvey 12.5."},
            {"type": "match", "lo": "CH8-LO4", "q": "Match each GC detector to what it is best for.", "left": ["FID", "ECD", "TCD", "MS"], "right": ["almost all organic compounds", "halogenated compounds", "everything, but less sensitive", "identifying unknowns"], "ans": [0, 1, 2, 3], "why": "Harvey 12.4."},
            {"type": "mcq", "lo": "CH8-LO4", "q": "Temperature programming in GC means:", "opts": ["the oven heats up during the run", "the injector is cooled", "the carrier gas is changed", "the sample is frozen first"], "ans": 0, "why": "Low- and high-boiling compounds both give sharp peaks."}]},
        {"h": "Pharmacy scenario · The slimming capsule", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Puan Rosnah brings a 'natural slimming' capsule bought online and says it makes her heart race. The pharmacist reports it to the regulator, whose lab suspects a hidden drug. The lab also tests a returned bottle of <b>paracetamol tablets</b> that were stored in a hot car.</p>"},
            {"type": "mcq", "lo": "CH8-LO5", "q": "The quickest, cheapest first screen for a hidden drug in the capsule is:", "opts": ["TLC against reference standards of suspected drugs", "GC of the capsule shell", "ion-exchange chromatography", "size-exclusion chromatography"], "ans": 0, "why": "Many samples and standards on one plate."},
            {"type": "mcq", "lo": "CH8-LO5", "q": "To confirm the identity of the hidden drug beyond doubt, the lab would use:", "opts": ["LC–MS or GC–MS", "paper chromatography", "a melting point only", "iodine vapour"], "ans": 0, "why": "MS gives the mass and fragments of the molecule."},
            {"type": "mcq", "lo": "CH8-LO5", "q": "For the paracetamol tablets, which test shows whether the drug has broken down?", "opts": ["HPLC: less paracetamol and new breakdown peaks", "GC residual solvents", "a co-spot only", "ion chromatography of chloride"], "ans": 0, "why": "A stability-indicating HPLC method."},
            {"type": "self", "lo": "CH8-LO5", "q": "Explain to Puan Rosnah, in plain words, how the lab can tell what is inside her capsule.", "model": "The lab dissolves the capsule contents and puts a tiny spot on a plate, next to spots of known drugs. A solvent rises up the plate and carries each substance a different distance. If a spot from her capsule travels exactly as far as a known slimming drug, that drug is probably inside. Then a more powerful machine (LC–MS) confirms it and measures how much there is."}]}]}

TUT = {
    "topic": "ch8", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH8_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (38 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 50.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 8 game, then Lab Practical 4 (TLC).",
    "sections": []}
T = TITLE
PAIR = '<div style="display:flex;gap:10px;flex-wrap:wrap">' + pic(mol(PARA, 220, 120), 220) + pic(mol(IBU, 260, 120), 260) + '</div>'
A = [
    ("CH8-LO1", "In all forms of chromatography, separation depends on:", ["different distribution of components between two phases", "different colours of the components", "the mass of the column", "evaporation of the mobile phase"], 0, "Harvey 12.1."),
    ("CH8-LO1", "In a chromatogram, the retention time is used mainly to:", ["help identify a component", "measure the amount", "calculate the pressure", "find the column length"], 0, "Peak area measures amount."),
    ("CH8-LO1", "Separation by molecular size uses:", ["size-exclusion chromatography", "ion-exchange chromatography", "adsorption TLC", "gas–liquid chromatography"], 0, "Porous gel; large molecules out first."),
    ("CH8-LO2", "Normal-phase chromatography uses:", ["a polar stationary phase and a less polar mobile phase", "a nonpolar stationary phase and a polar mobile phase", "a gas mobile phase", "a charged resin"], 0, "Silica with, for example, hexane–ethyl acetate."),
    ("CH8-LO2", "On a silica TLC plate, all spots stay near the origin. The best change is to:", ["use a more polar solvent", "use a less polar solvent", "use a longer plate", "spray with ninhydrin"], 0, "A more polar eluent moves spots further on silica."),
    ("CH8-LO2", "Which solvent has the highest polarity index?", ["acetonitrile", "toluene", "n-hexane", "diethyl ether"], 0, "5.8, versus 2.4, 0.1 and 2.8."),
    ("CH8-LO3", "R<sub>f</sub> values always lie between:", ["0 and 1", "1 and 10", "−1 and 1", "0 and 100"], 0, "The spot cannot pass the front."),
    ("CH8-LO3", "In paper chromatography, the stationary phase is:", ["water held in the cellulose", "the solvent", "silica gel", "air"], 0, "Separation is mainly by partition."),
    ("CH8-LO4", "A strong base anion exchanger carries:", ["–N(CH<sub>3</sub>)<sub>3</sub><sup>+</sup>", "–SO<sub>3</sub><sup>−</sup>", "–COO<sup>−</sup>", "–OH only"], 0, "Quaternary amine stays charged."),
    ("CH8-LO4", "Which detector is used in GC but not in HPLC?", ["flame ionisation detector", "UV/Vis detector", "refractive index detector", "fluorescence detector"], 0, "The FID burns the gas stream."),
    ("CH8-LO5", "Residual solvents left from drug manufacture are measured by:", ["headspace GC", "paper chromatography", "ion exchange", "size exclusion"], 0, "They are volatile."),
    ("CH8-LO5", "An internal standard is added in HPLC of blood samples to:", ["correct for losses during sample preparation and injection", "make the drug fluorescent", "increase the pressure", "remove proteins"], 0, "Harvey 12.5 (fluoxetine)."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH8-LO1", "marks": 7, "level": "C3",
     "q": "(a) Define chromatography and state the role of the stationary and mobile phases. (2 marks) (b) Explain why two components of a mixture leave a column at different times. (1 mark) (c) On an HPLC column, t<sub>m</sub> = 0.50 min. Peak A: t<sub>r</sub> = 3.50 min, w = 0.40 min. Peak B: t<sub>r</sub> = 4.10 min, w = 0.50 min. (i) Calculate the retention factor of each peak. (ii) Calculate the resolution and state whether the peaks are fully separated. (4 marks)",
     "hint": "k = (t<sub>r</sub> − t<sub>m</sub>) ÷ t<sub>m</sub>; R = 2Δt<sub>r</sub> ÷ (w<sub>A</sub> + w<sub>B</sub>).",
     "work": "(a) Chromatography separates the components of a mixture as a mobile phase (liquid or gas) carries them over a stationary phase (solid, or a liquid film on a solid). (b) Each component distributes itself between the phases differently: the one held more strongly by the stationary phase moves more slowly. (c)(i) k<sub>A</sub> = (3.50 − 0.50) ÷ 0.50 = <b>6.0</b>; k<sub>B</sub> = (4.10 − 0.50) ÷ 0.50 = <b>7.2</b>. (ii) R = 2(4.10 − 3.50) ÷ (0.40 + 0.50) = 1.20 ÷ 0.90 = <b>1.33</b>. This is below 1.5, so the peaks overlap slightly: not baseline separated.",
     "rubric": [["Definition: separation of mixture components", 1], ["Roles of mobile and stationary phases", 1], ["Different distribution between phases", 1], ["k<sub>A</sub> = 6.0", 1], ["k<sub>B</sub> = 7.2", 1], ["R = 1.33", 1], ["Below 1.5: not fully separated", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH8-LO2", "marks": 8, "level": "C3",
     "q": "(a) Distinguish between normal-phase and reversed-phase chromatography, giving one example of a stationary phase and a mobile phase for each. (2 marks) (b) Paracetamol (left) and ibuprofen (right) are analysed on a C18 column with water–methanol. Predict which elutes first and explain why." + PAIR + " (2 marks) (c) (i) Calculate the polarity index of 70:30 methanol–water (methanol 5.1, water 10.2). (ii) State the effect on retention times if the mobile phase is changed to 50:50. (2 marks) (d) Distinguish between isocratic and gradient elution. (2 marks)",
     "hint": "Like holds like. Which drug has more polar groups and which has a long hydrocarbon part?",
     "work": "(a) Normal phase: polar stationary phase (silica gel) with a less polar mobile phase (hexane–ethyl acetate); less polar compounds elute first. Reversed phase: nonpolar stationary phase (C18 bonded silica) with a polar mobile phase (water–methanol or water–acetonitrile); more polar compounds elute first. (b) <b>Paracetamol</b> elutes first. It has a phenol –OH and an amide group and is more polar; ibuprofen has a large nonpolar hydrocarbon part and is held longer by the nonpolar C18. (c)(i) P′ = 0.70(5.1) + 0.30(10.2) = 3.57 + 3.06 = <b>6.6</b>. (ii) 50:50 has P′ = 7.65, a more polar (weaker) mobile phase in reversed phase, so compounds are held longer: retention times increase. (d) Isocratic: the mobile phase composition stays the same throughout. Gradient: the composition changes during the run (in reversed phase, from more water to more organic solvent), so late peaks come out sooner and sharper.",
     "rubric": [["Normal phase described with example", 1], ["Reversed phase described with example", 1], ["Paracetamol elutes first", 1], ["Reason: more polar, less held by C18", 1], ["P′ = 6.6", 1], ["Retention times increase", 1], ["Isocratic defined", 1], ["Gradient defined", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH8-LO3", "marks": 7, "level": "C3",
     "q": "A pharmacist tests a white powder labelled 'paracetamol'. A paracetamol standard (S) and the test sample (T) are run side by side on a silica gel F<sub>254</sub> plate. (a) Describe how the plate is prepared, developed and visualised. (3 marks) (b) The solvent front moved 8.0 cm. Spot S moved 3.2 cm. Sample T gave two spots, at 3.2 cm and 5.6 cm. Calculate the R<sub>f</sub> of each spot. (2 marks) (c) Interpret the result, and state how you would confirm the identity of the main spot. (2 marks)",
     "hint": "R<sub>f</sub> = spot ÷ front. What does a second spot mean?",
     "work": "(a) Draw a pencil origin line about 1 cm from the bottom and apply small spots of S and T; let them dry. Place the plate in a closed, solvent-saturated tank with the solvent below the origin, and develop until the front is about 1 cm from the top. Remove, mark the front immediately, dry, and view under UV light at 254 nm: spots appear dark on a green background; circle them in pencil. (b) S: 3.2 ÷ 8.0 = <b>0.40</b>. T: 3.2 ÷ 8.0 = <b>0.40</b> and 5.6 ÷ 8.0 = <b>0.70</b>. (c) T contains a compound with the same R<sub>f</sub> as paracetamol, plus a second substance (an impurity or another drug), so it is not pure paracetamol. Confirm with a co-spot (S + T in one lane gives a single spot at 0.40) or by HPLC retention time or MS.",
     "rubric": [["Pencil origin, small spots", 1], ["Closed saturated tank, solvent below origin; mark the front", 1], ["Visualise under UV 254 nm", 1], ["R<sub>f</sub>(S) = 0.40", 1], ["R<sub>f</sub> of T spots 0.40 and 0.70", 1], ["Contains paracetamol plus another substance", 1], ["Confirm by co-spot, HPLC or MS", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH8-LO4", "marks": 8, "level": "C2",
     "q": "(a) Describe a cation exchanger and an anion exchanger, naming the functional group on a strong and a weak example of each. (3 marks) (b) Na<sup>+</sup>, Al<sup>3+</sup> and Ca<sup>2+</sup> are loaded on a cation-exchange column. State the order in which they are held, from most to least strongly, and explain how they can be washed off. (2 marks) (c) Name the four main parts of an HPLC instrument after the solvent reservoir, and state the job of any two. (2 marks) (d) Explain why ethanol in blood can be measured by GC but insulin cannot. (1 mark)",
     "hint": "Higher charge, stronger hold. GC needs a sample that can become a vapour.",
     "work": "(a) A cation exchanger has fixed negative groups that hold and exchange cations: strong, –SO<sub>3</sub><sup>−</sup> (sulfonic acid); weak, –COO<sup>−</sup> (carboxylic acid). An anion exchanger has fixed positive groups that exchange anions: strong, –N(CH<sub>3</sub>)<sub>3</sub><sup>+</sup> (quaternary amine); weak, –NH<sub>3</sub><sup>+</sup> (amine). Both are usually polystyrene–divinylbenzene resins. (b) Al<sup>3+</sup> > Ca<sup>2+</sup> > Na<sup>+</sup> (higher charge is held more strongly). Elute by raising the concentration of a competing cation in the mobile phase (for example, more HCl or NaCl) or by changing the pH. (c) Pump (pushes the mobile phase through at high pressure, steady flow); injector (loop, delivers an exact sample volume); column (separates the components); detector (for example UV, produces a signal as each compound leaves). (d) Ethanol is volatile and stable when heated, so it can be vaporised; insulin is a large, non-volatile protein that would decompose in the hot injector.",
     "rubric": [["Cation exchanger: negative fixed groups, exchanges cations", 1], ["Anion exchanger: positive fixed groups, exchanges anions", 1], ["Strong and weak groups named for both", 1], ["Al<sup>3+</sup> > Ca<sup>2+</sup> > Na<sup>+</sup>", 1], ["Elute with more competing ion or pH change", 1], ["Pump, injector, column, detector named", 1], ["Jobs of two parts", 1], ["Ethanol volatile; insulin non-volatile", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH8-LO5", "marks": 8, "level": "C4",
     "q": "A regulator's lab suspects that a 'herbal' slimming capsule contains sibutramine. (a) Explain how TLC could be used as a quick screen. (2 marks) (b) The capsule contents are extracted and diluted 1 in 20. By HPLC, the calibration line is: peak area = 1200 + 5400 × C (C in mg/L). The diluted extract gives a peak area of 28 200. Calculate the sibutramine concentration in the diluted extract and in the original extract. (2 marks) (c) Suggest a method to measure traces of dichloromethane left in a capsule from manufacture, with a reason. (2 marks) (d) When measuring a drug in a patient's blood by HPLC, explain why (i) the sample is cleaned up first and (ii) an internal standard is added. (2 marks)",
     "hint": "C = (area − intercept) ÷ slope, then multiply by the dilution factor.",
     "work": "(a) Spot the capsule extract and a sibutramine reference standard side by side (and a co-spot) on a silica plate, develop and visualise (UV 254 nm or a spray). A spot in the extract with the same R<sub>f</sub> and colour as the standard suggests sibutramine is present. (b) C = (28 200 − 1200) ÷ 5400 = 27 000 ÷ 5400 = <b>5.0 mg/L</b> in the diluted extract; × 20 = <b>100 mg/L</b> in the original extract. (c) Headspace <b>GC</b> (with FID or MS): dichloromethane is volatile, so it vaporises into the headspace and can be separated in the gas phase. (d)(i) Blood proteins and other material would clog the column, bind to it and give interfering peaks, so they are removed (for example, by solid-phase extraction). (ii) The internal standard is carried through every step, so it corrects for small, variable losses during extraction and injection.",
     "rubric": [["Extract and standard run on the same plate", 1], ["Same R<sub>f</sub> and colour → suggests sibutramine", 1], ["5.0 mg/L in diluted extract", 1], ["100 mg/L in original extract", 1], ["Headspace GC", 1], ["Reason: volatile", 1], ["Clean-up protects column, removes interferences", 1], ["Internal standard corrects for losses", 1]]}]})
