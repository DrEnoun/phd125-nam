"""PHD125 Chapter 8 · Application of Chromatographic Methods in Pharmaceutical Analysis · lecture slide content.
Sources: Harvey, Analytical Chemistry 2.1, chapter 12 (12.1-12.5) and Instrumental Analysis (LibreTexts) 28.6
(Ion-Exchange Chromatography, by Harvey), LibreTexts, CC BY-NC-SA 4.0. Kept to diploma level.
Original material by Dr. NAM: TLC and paper chromatography (8.4), the pharmacy links, ion-exchange medicines and
purified water, and the applications subchapter (8.8). Schematics drawn by _src/chromfigs.py."""
from figs import mol, row
from chromfigs import tlc, column, chromatogram, phases, ion_exchange, hplc, gc, rf_example

LO1, LO2, LO3, LO4, LO5 = 'CH8-LO1', 'CH8-LO2', 'CH8-LO3', 'CH8-LO4', 'CH8-LO5'

META = {
    "code": "CH8", "chapter": "Chapter 8", "title": "Application of Chromatographic Methods in Pharmaceutical Analysis",
    "short": "Chromatographic Methods",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: Harvey, Analytical Chemistry 2.1, chapter 12 (LibreTexts)",
    "attrib": ("Adapted from David Harvey, <i>Analytical Chemistry 2.1</i>, chapter 12 (12.1–12.5), and <i>Instrumental Analysis</i> 28.6 "
               "(Ion-Exchange Chromatography, by Harvey), LibreTexts, CC BY-NC-SA 4.0. TLC and paper chromatography, the pharmacy links, "
               "ion-exchange medicines and the applications subchapter are original material by Dr. NAM. Structures drawn with RDKit; "
               "chromatography schematics by Dr. NAM. Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["caffeine", "paracetamol", "water"], "2": ["caffeine", "aspirin", "water"], "3": ["hexane", "methanol", "water"],
               "4": ["paracetamol", "aspirin", "ethylacetate"], "5": ["water", "nacl", "glycine"], "6": ["caffeine", "acetonitrile", "methanol"],
               "7": ["ethanol", "methane", "hexane"], "8": ["paracetamol", "caffeine", "aspirin"]},
    "titlemol": ["caffeine", "paracetamol", "aspirin", "acetonitrile"], "darkmol": "caffeine",
    "next": "Extra chapters: Nucleic Acids, Lipid Metabolism and VSEPR Theory",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Explain the principle of chromatography (stationary and mobile phases, partition and adsorption), name the main types, and read a chromatogram"],
    [LO2, "Choose a suitable stationary phase (adsorbent) and solvent, and predict the order of elution in normal and reversed phase"],
    [LO3, "Describe how TLC and paper chromatography are carried out, and calculate and interpret R<sub>f</sub> values"],
    [LO4, "Describe ion-exchange chromatography, HPLC and GC: their phases, parts of the instrument and detectors"],
    [LO5, "Apply chromatography to pharmaceutical analysis: identity, purity, assay, stability and drugs in body fluids"],
]

PARA = 'CC(=O)Nc1ccc(O)cc1'
ASP = 'CC(=O)Oc1ccccc1C(=O)O'
SAL = 'OC(=O)c1ccccc1O'
CAF = 'Cn1cnc2c1c(=O)n(C)c(=O)n2C'


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Chromatographic Methods in Pharmaceutical Analysis", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 8: Application of Chromatographic Methods in Pharmaceutical Analysis",
         "notes": "Chapter 8, kept as one deck. Lesson plan week 13."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1: 8.1–8.2. LO2: 8.3. LO3: 8.4. LO4: 8.5–8.7. LO5: 8.8 (and links throughout)."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>8.1 Introduction</b> · <b>8.2 Basic Principles</b> · <b>8.3 Stationary and Mobile Phases</b> · <b>8.4 Thin Layer Chromatography</b>",
        "<b>8.5 Ion-Exchange Chromatography</b> · <b>8.6 HPLC</b> · <b>8.7 Gas Chromatography</b> · <b>8.8 Applications in Pharmaceutical Analysis</b>",
        "Links back: polarity and intermolecular forces (Chapter 1), functional groups (Chapters 2–4), amino acid charge and pI (Chapter 7).",
        "Lab Practical 4 (Thin Layer Chromatography) puts 8.4 into practice."],
         "notes": "Lesson plan: basic principles incl. ion exchange, HPLC and GC; stationary and mobile phases, choice of adsorbent and solvent; applications."})
    add({"t": "hook", "title": "Think first",
         "q": "A patient brings in a 'herbal slimming' capsule bought online. The pharmacist suspects it contains a hidden drug. A tablet of paracetamol has sat in a hot car for a year. How could you find out what is really inside each one?",
         "a": "Separate the mixture first, then identify and measure each part. <b>TLC</b> gives a quick yes or no against a standard drug; <b>HPLC</b> measures how much paracetamol is left and shows any breakdown products; <b>GC–MS</b> or <b>LC–MS</b> confirms the identity of an unknown. That is chromatography.",
         "notes": "Pairs discuss for one minute. Adulterated slimming products are a real problem flagged by drug regulators."})

    # ================= 8.1 INTRODUCTION =================
    add({"t": "divider", "num": 1, "title": "Introduction", "lo": LO1, "src": "Harvey 12.1",
         "blurb": "Most samples in pharmacy are mixtures. Chromatography pulls them apart so each part can be identified and measured."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "What is chromatography?",
         "items": ["A family of methods that <b>separate</b> the components of a mixture.",
                   "Two phases: a <b>stationary phase</b> that stays put (a solid, or a liquid film on a solid) and a <b>mobile phase</b> that moves (a liquid or a gas).",
                   "The sample is carried by the mobile phase over the stationary phase. Each component shares itself between the two phases.",
                   "A component that prefers the <b>stationary</b> phase moves <b>slowly</b>; one that prefers the <b>mobile</b> phase moves <b>quickly</b>. So they separate."],
         "notes": "Harvey 12.1."})
    add({"t": "two", "sec": 1, "lo": LO1, "title": "A short history",
         "lead": "The name comes from the Greek for 'colour' and 'to write'.",
         "cols": [{"h": "Tswett, 1906", "tone": "cold", "items": [
             "Mikhail Tswett separated coloured plant pigments (chlorophylls, carotenes) on a column of chalk.",
             "The pigments appeared as coloured bands down the column, hence 'colour writing'."]},
             {"h": "Martin and Synge, 1940s", "tone": "heat", "items": [
                 "Developed partition chromatography and the theory of 'plates' (8.2), and won the 1952 Nobel Prize in Chemistry.",
                 "Their work led to paper chromatography, GC and, later, HPLC."]}],
         "notes": "Harvey 12.1 (Tswett, Martin and Synge); Nobel year is general knowledge."})
    add({"t": "bullets", "sec": 1, "lo": LO5, "title": "Why pharmacists need chromatography",
         "items": ["<b>Identity</b>: is this really the drug on the label?",
                   "<b>Purity</b>: are there impurities, breakdown products or hidden adulterants?",
                   "<b>Assay</b>: how much drug is in each tablet, syrup or injection?",
                   "<b>Body fluids</b>: drug levels in blood or urine (therapeutic drug monitoring, poisoning, doping).",
                   "Pharmacopoeia monographs (BP, USP) specify TLC, HPLC or GC tests for most medicines."],
         "notes": "Original pharmacy framing; developed in 8.8."})

    # ================= 8.2 BASIC PRINCIPLES =================
    add({"t": "divider", "num": 2, "title": "Basic Principles", "lo": LO1, "src": "Harvey 12.1–12.2",
         "blurb": "How components share themselves between two phases, the main types of chromatography, and how to read a chromatogram."})
    add({"t": "figure", "pos": "leftwide", "sec": 2, "lo": LO1, "title": "Separation on a column",
         "fig": {"cap": "A (blue) spends more time in the mobile phase, so it moves ahead of B (red) and leaves the column first.", "data": column()},
         "items": ["Each component moves back and forth between the phases many times as it travels.",
                   "The <b>distribution ratio</b> D compares how much is in each phase. A large D for the stationary phase means strong holding and slow movement.",
                   "Even small differences in D add up over the length of the column, so similar compounds can be separated."],
         "notes": "Harvey 12.1–12.2. D is introduced qualitatively only."})
    add({"t": "table", "sec": 2, "lo": LO1, "title": "Ways to classify chromatography",
         "head": ["Based on", "Types", "Notes"],
         "rows": [["how the phases meet", "<b>planar</b> (paper, TLC); <b>column</b> (HPLC, GC)", "planar: solvent moves by capillary action; column: by gravity or pressure"],
                  ["the mobile phase", "<b>liquid</b> chromatography; <b>gas</b> chromatography", "named mobile phase first: gas–liquid chromatography"],
                  ["how solutes are held", "adsorption, partition, ion exchange, size exclusion, affinity", "see next slide"]],
         "widths": [2.4, 4.0, 4.0],
         "caption": "If a name gives only one phase, it is the mobile phase: 'gas chromatography' means a gas mobile phase. Source: Harvey 12.1.",
         "notes": "Harvey 12.1."})
    add({"t": "table", "sec": 2, "lo": LO1, "title": "Five ways a stationary phase holds a solute",
         "head": ["Type", "Stationary phase", "Solutes separate by", "Example"],
         "rows": [["adsorption", "solid surface (silica gel, alumina)", "how strongly they stick to the surface (polarity)", "TLC on silica"],
                  ["partition", "liquid film on a solid support", "how they dissolve in the film vs the mobile phase", "paper, GC, reversed-phase HPLC"],
                  ["ion exchange", "resin with fixed charged groups (–SO<sub>3</sub><sup>−</sup>, –N(CH<sub>3</sub>)<sub>3</sub><sup>+</sup>)", "electrostatic attraction (charge)", "metal ions, amino acids"],
                  ["size exclusion", "porous particles or gel", "size: large molecules come out first", "proteins, polymers"],
                  ["affinity", "a ligand bonded to the support", "a specific fit (antigen–antibody, enzyme–substrate)", "purifying antibodies"]],
         "widths": [2.0, 3.0, 3.2, 2.4],
         "caption": "Most real separations combine more than one effect. Source: Harvey 12.1.",
         "notes": "Harvey 12.1 classification."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO1, "title": "Reading a chromatogram",
         "fig": {"cap": "A chromatogram: detector signal against time. One peak per component.", "data": chromatogram()},
         "items": ["<b>Retention time, t<sub>r</sub></b>: time from injection to the top of a peak. Under fixed conditions it helps <b>identify</b> a compound.",
                   "<b>Void time, t<sub>m</sub></b>: time for an unretained substance to pass through. <b>Peak area</b> is proportional to the <b>amount</b>, so it is used to measure."],
         "notes": "Harvey 12.2."})
    add({"t": "bullets", "sec": 2, "lo": LO1, "title": "Three numbers that describe a separation",
         "items": ["<b>Retention factor</b>: k = (t<sub>r</sub> − t<sub>m</sub>) ÷ t<sub>m</sub>. A larger k means the solute is held more strongly.",
                   "<b>Selectivity factor</b>: α = k<sub>B</sub> ÷ k<sub>A</sub> (B elutes later). α = 1 means the two peaks come out together.",
                   "<b>Resolution</b>: R = 2(t<sub>r,B</sub> − t<sub>r,A</sub>) ÷ (w<sub>A</sub> + w<sub>B</sub>). <b>R ≥ 1.5</b> is taken as complete (baseline) separation.",
                   "<b>Efficiency</b>: the number of theoretical plates, N = 16(t<sub>r</sub>/w)<sup>2</sup>. More plates give narrower peaks."],
         "notes": "Harvey 12.2. Harvey notes R = 1.50 gives about 0.13% overlap."})
    add({"t": "example", "sec": 2, "lo": LO1, "title": "Example 8.1 · Retention factor and resolution",
         "q": "(a) Butyric acid has t<sub>r</sub> = 7.63 min on a column with t<sub>m</sub> = 0.31 min. Calculate k (b) Limonene (t<sub>r</sub> = 8.36 min, w = 0.96 min) and γ-terpinene (t<sub>r</sub> = 9.54 min, w = 0.64 min). Calculate R. Are they fully separated?",
         "steps": ["(a) k = (7.63 − 0.31) ÷ 0.31 = <b>23.6</b>.",
                   "(b) R = 2(9.54 − 8.36) ÷ (0.96 + 0.64) = 2.36 ÷ 1.60 = <b>1.48</b>.",
                   "1.48 is just below 1.5, so the peaks overlap very slightly; not quite baseline separation."],
         "notes": "Harvey 12.2 worked examples."})
    add({"t": "bullets", "sec": 2, "lo": LO1, "title": "Improving a separation",
         "items": ["<b>Change selectivity (α)</b> first: a different mobile phase or its pH (LC), or a different stationary phase (GC). This usually helps most.",
                   "<b>Adjust retention (k)</b>: a weaker mobile phase (LC) or a lower column temperature (GC) holds solutes longer. Little gain once k is above about 10.",
                   "<b>Increase efficiency (N)</b>: smaller, more even particles, a suitable flow rate, a longer or capillary column."],
         "notes": "Harvey 12.3."})
    add({"t": "check", "sec": 2, "lo": LO1, "title": "Quick check",
         "q": "In a chromatogram, the peak area is used to find:",
         "opts": ["the amount of the component", "the identity of the component", "the void time", "the polarity of the solvent"], "ans": 0,
         "why": "Retention time helps identify; area measures amount.", "notes": "Answer A."})
    add({"t": "check", "sec": 2, "lo": LO1, "title": "Quick check",
         "q": "Two peaks have a resolution of 0.8. This means they:",
         "opts": ["overlap, so they are not fully separated", "are fully separated", "are the same compound", "have the same peak area"], "ans": 0,
         "why": "R ≥ 1.5 is needed for baseline separation.", "notes": "Answer A."})

    # ================= 8.3 STATIONARY AND MOBILE PHASES =================
    add({"t": "divider", "num": 3, "title": "Stationary and Mobile Phases", "lo": LO2, "src": "Harvey 12.4–12.5",
         "blurb": "Like dissolves like. Choose the adsorbent and solvent so the components are held by different amounts."})
    add({"t": "table", "sec": 3, "lo": LO2, "title": "Choosing the stationary phase (adsorbent)",
         "head": ["Stationary phase", "Polarity", "Used in", "Good for"],
         "rows": [["silica gel (Si–OH)", "polar, slightly acidic", "TLC, columns, normal-phase HPLC", "most drugs and organic compounds"],
                  ["alumina (Al<sub>2</sub>O<sub>3</sub>)", "polar", "TLC, columns", "bases and less polar compounds"],
                  ["cellulose (paper)", "polar, holds water", "paper chromatography, TLC", "sugars, amino acids, dyes"],
                  ["C18 (octadecyl, ODS) bonded silica", "nonpolar", "reversed-phase HPLC", "most drugs in tablets and blood"],
                  ["ion-exchange resin", "charged", "ion-exchange chromatography", "ions, amino acids, proteins"],
                  ["polysiloxane liquid film", "nonpolar to polar", "GC capillary columns", "volatile compounds"]],
         "widths": [3.0, 2.2, 2.8, 2.6],
         "caption": "Silica gel is the most used adsorbent. Its surface –OH groups form hydrogen bonds with polar groups (–OH, –NH<sub>2</sub>, –COOH) in the solutes. Sources: Harvey 12.4–12.5; table by Dr. NAM.",
         "notes": "Mostly original table built on Harvey."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO2, "title": "Normal phase and reversed phase",
         "fig": {"cap": "The same rule, opposite results: a solute is held by the phase that is most like it.", "data": phases()},
         "items": ["<b>Normal phase</b>: polar stationary phase (silica), less polar mobile phase. Less polar solutes leave first.",
                   "<b>Reversed phase</b>: nonpolar stationary phase (C18), polar mobile phase (water with methanol or acetonitrile). More polar solutes leave first. Most HPLC in pharmacy is reversed phase."],
         "notes": "Harvey 12.5."})
    add({"t": "table", "sec": 3, "lo": LO2, "title": "Choosing the mobile phase (solvent)",
         "head": ["Solvent", "Polarity index P′", "Solvent", "Polarity index P′"],
         "rows": [["n-hexane", "0.1", "ethanol", "4.3"], ["toluene", "2.4", "ethyl acetate", "4.4"],
                  ["diethyl ether", "2.8", "methanol", "5.1"], ["tetrahydrofuran", "4.0", "acetonitrile", "5.8"],
                  ["", "", "water", "10.2"]],
         "widths": [3.0, 2.0, 3.0, 2.0],
         "caption": "A higher P′ means a more polar solvent. On silica, a more polar solvent moves all the spots further (it is a 'stronger' eluent). In reversed phase it is the opposite: adding water makes the solvent 'weaker'. Source: Harvey Table 12.5.1.",
         "notes": "Harvey 12.5 polarity index table (selected)."})
    add({"t": "bullets", "sec": 3, "lo": LO2, "title": "Mixing solvents",
         "items": ["Mixtures let you fine-tune polarity: P′<sub>mix</sub> = Φ<sub>A</sub>P′<sub>A</sub> + Φ<sub>B</sub>P′<sub>B</sub> (Φ = volume fraction).",
                   "Example: 60:40 water–methanol: P′ = 0.60(10.2) + 0.40(5.1) = <b>8.2</b>.",
                   "Rule of thumb (HPLC): a change of 2 units in P′ changes k about 10-fold.",
                   "TLC: start with hexane–ethyl acetate and change the ratio until the spots sit in the middle of the plate."],
         "notes": "Harvey 12.5 (mixing rule, worked example, rule of thumb); TLC tip original."})
    add({"t": "two", "sec": 3, "lo": LO2, "title": "Isocratic and gradient elution",
         "lead": "Keep the mobile phase the same, or change it during the run.",
         "cols": [{"h": "Isocratic", "tone": "cold", "items": [
             "Same mobile phase composition throughout.",
             "Simple and reproducible; good when the components have similar retention.",
             "Early peaks may crowd together while late peaks come out broad and slow."]},
             {"h": "Gradient", "tone": "heat", "items": [
                 "Composition changes during the run. Reversed phase: start rich in water, end rich in methanol or acetonitrile.",
                 "Speeds up the late peaks and sharpens them.",
                 "GC uses the same idea with <b>temperature programming</b> (8.7)."]}],
         "notes": "Harvey 12.4–12.5."})
    add({"t": "tryit", "sec": 3, "lo": LO2, "title": "Try it · Predict the order",
         "q": "A mixture of aspirin, salicylic acid and caffeine is analysed. (a) On a silica TLC plate with a fairly nonpolar solvent, which phase holds the more polar compounds longer? (b) In reversed-phase HPLC (C18, water–methanol), which comes out first: the more polar or the less polar compound? (c) The spots on a silica plate all stay near the origin. How would you change the solvent?",
         "a": "(a) The polar <b>silica</b> holds the more polar compounds, so they have lower R<sub>f</sub>. (b) The <b>more polar</b> compound comes out first, because the nonpolar C18 holds less polar compounds. (c) Make the solvent <b>more polar</b> (for example, more ethyl acetate in hexane) so it carries the spots further.",
         "notes": "Original."})
    add({"t": "check", "sec": 3, "lo": LO2, "title": "Quick check",
         "q": "Which mobile phase is the most polar?",
         "opts": ["water", "methanol", "ethyl acetate", "n-hexane"], "ans": 0,
         "why": "Water has P′ = 10.2.", "notes": "Answer A."})
    add({"t": "check", "sec": 3, "lo": LO2, "title": "Quick check",
         "q": "A C18 HPLC column with a water–acetonitrile mobile phase is an example of:",
         "opts": ["reversed-phase chromatography", "normal-phase chromatography", "ion-exchange chromatography", "size-exclusion chromatography"], "ans": 0,
         "why": "Nonpolar stationary phase, polar mobile phase.", "notes": "Answer A."})

    # ================= 8.4 TLC =================
    add({"t": "divider", "num": 4, "title": "Thin Layer Chromatography", "lo": LO3, "src": "original (Lab Practical 4)",
         "blurb": "Quick, cheap, and many samples side by side. The workhorse for identity tests and for following a reaction."})
    add({"t": "bullets", "sec": 4, "lo": LO3, "title": "Planar chromatography: TLC and paper",
         "items": ["<b>TLC</b>: a thin layer (about 0.25 mm) of adsorbent, usually <b>silica gel</b>, on a glass, aluminium or plastic plate. Separation is mainly by <b>adsorption</b>.",
                   "<b>Paper chromatography</b>: the stationary phase is <b>water held in the cellulose</b> of the paper. Separation is mainly by <b>partition</b>.",
                   "The mobile phase rises up the plate or paper by <b>capillary action</b>.",
                   "TLC is faster, gives sharper spots, and can use strong reagents to show spots; paper is cheaper and suits very polar compounds (sugars, amino acids)."],
         "notes": "Original summary (Harvey 12.1 classifies planar methods)."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO3, "title": "Running a TLC plate",
         "fig": {"cap": "Spot the samples on a pencil line, develop in a closed tank, then measure the distances.", "data": tlc()},
         "items": ["Draw the <b>origin</b> about 1 cm from the bottom in <b>pencil</b> (ink would run). Spot small, concentrated spots; let them dry.",
                   "Stand the plate in a closed tank with solvent <b>below</b> the origin (or the spots dissolve into the pool). Remove when the solvent is about 1 cm from the top; <b>mark the front at once</b>."],
         "notes": "Original procedure, matches Lab Practical 4."})
    add({"t": "two", "sec": 4, "lo": LO3, "title": "Making the spots visible",
         "lead": "Most drugs are colourless, so the spots must be revealed.",
         "cols": [{"h": "Non-destructive", "tone": "cold", "items": [
             "<b>UV light, 254 nm</b>: plates with a fluorescent indicator (F<sub>254</sub>) glow green; compounds that absorb UV (aromatic rings) show as <b>dark spots</b>. Circle them in pencil.",
             "Some compounds fluoresce under <b>365 nm</b> UV.",
             "<b>Iodine vapour</b>: many organic compounds give brown spots that fade."]},
             {"h": "Spray reagents", "tone": "heat", "items": [
                 "<b>Ninhydrin</b>: purple spots with amino acids (Chapter 7).",
                 "<b>Dragendorff's reagent</b>: orange spots with alkaloids.",
                 "<b>Iron(III) chloride</b>: coloured spots with phenols (Chapter 3), such as salicylic acid.",
                 "Spraying changes the compounds, so do it last."]}],
         "notes": "Original."})
    add({"t": "bullets", "sec": 4, "lo": LO3, "title": "The retardation factor, R<sub>f</sub>",
         "items": ["R<sub>f</sub> = distance moved by the spot ÷ distance moved by the solvent front, both measured from the <b>origin</b> (to the centre of the spot).",
                   "R<sub>f</sub> is always between <b>0</b> and <b>1</b> and has no units. Aim for values of about 0.2 to 0.8.",
                   "A polar compound on silica sticks more: <b>low R<sub>f</sub></b>. A less polar compound moves further: <b>high R<sub>f</sub></b>.",
                   "R<sub>f</sub> changes with the solvent, the plate, the temperature and tank saturation, so always run the <b>standard on the same plate</b>."],
         "notes": "Original."})
    add({"t": "figure", "pos": "leftwide", "sec": 4, "lo": LO3, "title": "Example 8.2 · Calculating R<sub>f</sub>",
         "fig": {"cap": "Distances are measured from the origin line.", "data": rf_example()},
         "items": ["Spot P: R<sub>f</sub> = 2.0 ÷ 8.0 = <b>0.25</b>.",
                   "Spot Q: R<sub>f</sub> = 5.6 ÷ 8.0 = <b>0.70</b>.",
                   "On silica, <b>P is the more polar</b> compound: it is held more strongly by the stationary phase."],
         "notes": "Original example."})
    add({"t": "two", "sec": 4, "lo": LO3, "title": "What TLC tells a pharmacist",
         "lead": "Compare the test sample with a reference standard on the same plate.",
         "cols": [{"h": "Identity", "tone": "cold", "items": [
             "The test spot matches the standard in <b>R<sub>f</sub>, colour and size</b>.",
             "<b>Co-spot</b> (standard and test in one lane): one single spot supports the identity; two spots mean they are different."]},
             {"h": "Purity", "tone": "heat", "items": [
                 "<b>Extra spots</b> mean impurities or breakdown products.",
                 "Aspirin that smells of vinegar has hydrolysed: a second spot for <b>salicylic acid</b> appears (and turns violet with FeCl<sub>3</sub>).",
                 "Also used to follow a reaction: the starting material spot fades as the product spot grows."]}],
         "notes": "Original; aspirin hydrolysis links to Chapter 4."})
    add({"t": "figure", "pos": "top", "sec": 4, "lo": LO3, "title": "Aspirin and its breakdown product",
         "fig": {"cap": "Moisture hydrolyses the ester in aspirin to salicylic acid and acetic acid (Chapter 4).",
                 "data": row([(mol(ASP, 230, 150), "aspirin (ester + acid)"), (mol(SAL, 210, 150), "salicylic acid (phenol + acid)"), (mol('CC(=O)O', 150, 110), "acetic acid")], w=240, h=160)},
         "items": ["Salicylic acid has a free phenol –OH where aspirin has an ester, so the two give <b>separate spots</b> with different R<sub>f</sub> values. Run pure salicylic acid alongside to locate its spot.",
                   "Its phenol gives a violet colour with FeCl<sub>3</sub>; aspirin does not. A quick TLC check of old tablets."],
         "notes": "Original."})
    add({"t": "check", "sec": 4, "lo": LO3, "title": "Quick check",
         "q": "A spot moves 3.0 cm and the solvent front moves 6.0 cm. R<sub>f</sub> is:",
         "opts": ["0.50", "2.0", "3.0", "0.33"], "ans": 0,
         "why": "3.0 ÷ 6.0 = 0.50.", "notes": "Answer A."})
    add({"t": "check", "sec": 4, "lo": LO3, "title": "Quick check",
         "q": "Why is the origin line drawn in pencil, not ink?",
         "opts": ["ink would dissolve and run with the solvent", "pencil absorbs UV light", "pencil reacts with silica", "ink makes the solvent move faster"], "ans": 0,
         "why": "Ink dyes are themselves separated by the solvent.", "notes": "Answer A."})

    # ================= 8.5 ION EXCHANGE =================
    add({"t": "divider", "num": 5, "title": "Ion-Exchange Chromatography", "lo": LO4, "src": "Harvey, Instrumental Analysis 28.6",
         "blurb": "A resin with fixed charges holds ions of the opposite charge. Separation by charge."})
    add({"t": "figure", "pos": "top", "sec": 5, "lo": LO4, "title": "Cation and anion exchangers",
         "fig": {"cap": "Fixed charged groups on the resin hold mobile counter-ions that can be swapped for other ions of the same charge.", "data": ion_exchange()},
         "items": ["Stationary phase: a cross-linked <b>polystyrene–divinylbenzene</b> resin (or coated silica) with ionic groups bonded to it.",
                   "A <b>cation exchanger</b> has negative groups and swaps <b>cations</b>; an <b>anion exchanger</b> has positive groups and swaps <b>anions</b>."],
         "notes": "Instrumental Analysis 28.6 (Harvey)."})
    add({"t": "table", "sec": 5, "lo": LO4, "title": "Properties of cation and anion exchangers",
         "head": ["Type", "Fixed group", "Exchanges", "Useful pH range"],
         "rows": [["strong acid cation exchanger", "sulfonic acid, –SO<sub>3</sub><sup>−</sup>", "cations (Na<sup>+</sup>, Ca<sup>2+</sup>, protonated amines)", "stays charged even in strong acid"],
                  ["weak acid cation exchanger", "carboxylic acid, –COO<sup>−</sup>", "cations", "protonated and loses capacity below about pH 4"],
                  ["strong base anion exchanger", "quaternary amine, –N(CH<sub>3</sub>)<sub>3</sub><sup>+</sup>", "anions (Cl<sup>−</sup>, SO<sub>4</sub><sup>2−</sup>, carboxylates)", "stays charged even in strong base"],
                  ["weak base anion exchanger", "amine, –NH<sub>3</sub><sup>+</sup>", "anions", "loses its charge in basic solution"]],
         "widths": [3.0, 2.8, 3.0, 2.6],
         "caption": "'Strong' and 'weak' follow the acid–base strength of the fixed group, just like strong and weak acids. Source: Instrumental Analysis 28.6 (Harvey).",
         "notes": "28.6."})
    add({"t": "bullets", "sec": 5, "lo": LO4, "title": "What decides how strongly an ion is held",
         "items": ["<b>Higher charge</b> binds more strongly: Al<sup>3+</sup> > Ca<sup>2+</sup> > Na<sup>+</sup>.",
                   "For the same charge, a <b>smaller hydrated ion</b> binds more strongly: K<sup>+</sup> > Na<sup>+</sup> > Li<sup>+</sup>.",
                   "To <b>elute</b> (wash off) the held ions: increase the <b>concentration</b> of the competing ion in the mobile phase (for example, more HCl or NaCl), or change the <b>pH</b>.",
                   "pH also changes the charge of the sample: an amino acid is + below its pI and − above it (Chapter 7)."],
         "notes": "28.6 selectivity series and elution; amino acid link original."})
    add({"t": "bullets", "sec": 5, "lo": LO4, "title": "Ion chromatography",
         "items": ["An ion-exchange column, often with a <b>conductivity detector</b>, which responds to any ion.",
                   "A <b>suppressor</b> after the column turns the eluent ions into water or carbonic acid, so only the sample ions are 'seen'.",
                   "Measures F<sup>−</sup>, Cl<sup>−</sup>, Br<sup>−</sup>, NO<sub>2</sub><sup>−</sup>, NO<sub>3</sub><sup>−</sup>, PO<sub>4</sub><sup>3−</sup> and SO<sub>4</sub><sup>2−</sup> in water in about 15 minutes.",
                   "Also used for amino acids, sugars, nucleotides, proteins and drugs."],
         "notes": "28.6."})
    add({"t": "two", "sec": 5, "lo": LO4, "title": "Ion exchange in the pharmacy",
         "lead": "The same chemistry, used to clean water and as medicines.",
         "cols": [{"h": "Purified water and protein drugs", "tone": "cold", "items": [
             "<b>Deionised water</b>: a cation exchanger in the H<sup>+</sup> form and an anion exchanger in the OH<sup>−</sup> form; H<sup>+</sup> + OH<sup>−</sup> → H<sub>2</sub>O.",
             "Ion-exchange columns purify <b>insulin</b>, antibodies and other protein medicines."]},
             {"h": "Resins as medicines", "tone": "heat", "items": [
                 "<b>Sodium polystyrene sulfonate</b> (cation exchanger): swaps Na<sup>+</sup> for K<sup>+</sup> in the gut to treat high blood potassium.",
                 "<b>Cholestyramine</b> (anion exchanger): binds bile acids in the gut, which lowers blood cholesterol (Chapter 6)."]}],
         "notes": "Original pharmacy links."})
    add({"t": "check", "sec": 5, "lo": LO4, "title": "Quick check",
         "q": "A resin carrying –SO<sub>3</sub><sup>−</sup> groups is a:",
         "opts": ["strong acid cation exchanger", "weak acid cation exchanger", "strong base anion exchanger", "weak base anion exchanger"], "ans": 0,
         "why": "Sulfonic acid is a strong acid and holds cations.", "notes": "Answer A."})
    add({"t": "check", "sec": 5, "lo": LO4, "title": "Quick check",
         "q": "On a cation exchanger, which ion is held most strongly?",
         "opts": ["Al<sup>3+</sup>", "Ca<sup>2+</sup>", "Na<sup>+</sup>", "Li<sup>+</sup>"], "ans": 0,
         "why": "Higher charge binds more strongly.", "notes": "Answer A."})

    # ================= 8.6 HPLC =================
    add({"t": "divider", "num": 6, "title": "High-Performance Liquid Chromatography", "lo": LO4, "src": "Harvey 12.5",
         "blurb": "A liquid pumped at high pressure through a column of tiny particles. The main tool for testing medicines."})
    add({"t": "figure", "pos": "top", "sec": 6, "lo": LO4, "title": "The HPLC instrument",
         "fig": {"cap": "Solvent → pump → injector → column → detector → computer.", "data": hplc()},
         "items": ["The mobile phase is <b>filtered</b> and <b>degassed</b> (bubbles upset the detector). The pump pushes it at several hundred atmospheres.",
                   "A <b>loop injector</b> delivers an exact volume of sample every time, which gives good precision."],
         "notes": "Harvey 12.5."})
    add({"t": "bullets", "sec": 6, "lo": LO4, "title": "HPLC columns",
         "items": ["Stainless steel, 2.1–4.6 mm wide and 30–300 mm long, packed with porous <b>silica</b> particles of 3–10 µm.",
                   "Most are <b>C18 (ODS)</b> bonded phases used in <b>reversed phase</b>; C8, phenyl and cyano phases are also used.",
                   "Smaller particles give sharper peaks but need higher pressure.",
                   "A short <b>guard column</b> in front traps particles and strongly held material, protecting the costly analytical column. Silica dissolves in base, so keep the mobile phase below about pH 7.5."],
         "notes": "Harvey 12.5."})
    add({"t": "table", "sec": 6, "lo": LO4, "title": "HPLC detectors",
         "head": ["Detector", "Detects", "Strengths", "Limits"],
         "rows": [["UV/Vis (incl. diode array)", "compounds that absorb UV or visible light", "most used; diode array gives a spectrum for each peak", "solvent must not absorb at that wavelength"],
                  ["fluorescence", "fluorescent compounds", "very sensitive and selective", "few compounds fluoresce"],
                  ["refractive index (RI)", "almost anything", "universal (sugars, polymers)", "poor sensitivity; no gradient elution"],
                  ["electrochemical", "compounds that are easily oxidised or reduced", "sensitive", "only for those compounds"],
                  ["mass spectrometer (LC–MS)", "ions by mass", "identifies the compound; very sensitive", "costly; needs an internal standard"]],
         "widths": [2.6, 3.0, 3.2, 2.8],
         "caption": "Most drugs have aromatic rings, so UV detection works for them. Source: Harvey 12.5.",
         "notes": "Harvey 12.5 detectors (simplified)."})
    add({"t": "bullets", "sec": 6, "lo": LO5, "title": "Measuring a drug by HPLC",
         "items": ["Make <b>standards</b> of known concentration and plot <b>peak area</b> against concentration: a straight-line calibration curve.",
                   "Inject the sample under the same conditions; read its concentration from the line.",
                   "An <b>internal standard</b> (a similar compound added in the same amount to every solution) corrects for losses during sample preparation.",
                   "Tablet assay: powder tablets, extract the drug into the mobile phase, filter, inject."],
         "notes": "Harvey 12.5 quantitative applications."})
    add({"t": "example", "sec": 6, "lo": LO5, "title": "Example 8.3 · Caffeine by HPLC",
         "q": "A calibration line for caffeine is: peak area = 16 715 + 4318 × C, where C is in mg/L. A drink sample gives a peak area of 424 195. (a) Find the caffeine concentration (b) The drink was diluted 1 in 10 before injection. What is the concentration in the drink?",
         "steps": ["(a) C = (424 195 − 16 715) ÷ 4318 = 407 480 ÷ 4318 = <b>94.4 mg/L</b>.",
                   "(b) Multiply by the dilution factor: 94.4 × 10 = <b>944 mg/L</b> in the drink."],
         "notes": "Part (a) from Harvey 12.5 exercise; part (b) original."})
    add({"t": "bullets", "sec": 6, "lo": LO5, "title": "Case: an antidepressant in blood",
         "items": ["<b>Fluoxetine</b> (Prozac) in serum. Serum is about 92% water and 6–8% protein, which would clog the column.",
                   "<b>Sample clean-up</b>: pass the serum through a small C18 cartridge (solid-phase extraction), wash, then wash the drug off.",
                   "<b>Internal standard</b>: protriptyline, added to every sample and standard.",
                   "<b>Column</b>: C8, 15 cm × 4.6 mm, isocratic acetonitrile–water. <b>Detector</b>: fluorescence, chosen because many other drugs in the blood do not fluoresce."],
         "notes": "Harvey 12.5 representative method."})
    add({"t": "check", "sec": 6, "lo": LO4, "title": "Quick check",
         "q": "The most common HPLC detector for drugs is:",
         "opts": ["UV/Vis absorbance", "refractive index", "flame ionisation", "electron capture"], "ans": 0,
         "why": "Most drugs absorb UV. FID and ECD are GC detectors.", "notes": "Answer A."})
    add({"t": "check", "sec": 6, "lo": LO4, "title": "Quick check",
         "q": "The mobile phase is degassed before HPLC to:",
         "opts": ["stop bubbles forming in the detector", "make it more polar", "remove dissolved drug", "lower the column temperature"], "ans": 0,
         "why": "Bubbles give false peaks and noise.", "notes": "Answer A."})

    # ================= 8.7 GC =================
    add({"t": "divider", "num": 7, "title": "Gas Chromatography", "lo": LO4, "src": "Harvey 12.4",
         "blurb": "A gas carries the vaporised sample through a long, heated column. For anything that can be turned into a vapour."})
    add({"t": "figure", "pos": "top", "sec": 7, "lo": LO4, "title": "The GC instrument",
         "fig": {"cap": "Carrier gas → heated injector → column in an oven → detector → computer.", "data": gc()},
         "items": ["<b>Carrier gas</b> (mobile phase): an inert gas such as He, N<sub>2</sub> or Ar. It only carries the sample; it does not interact with it.",
                   "The injector is hot (at least 50 °C above the boiling point of the least volatile component) so the sample vaporises at once."],
         "notes": "Harvey 12.4."})
    add({"t": "two", "sec": 7, "lo": LO4, "title": "GC columns and stationary phases",
         "lead": "The stationary phase is usually a thin liquid film (gas–liquid chromatography).",
         "cols": [{"h": "Packed columns", "tone": "cold", "items": [
             "2–6 m long, 2–4 mm wide, packed with coated particles.",
             "Take larger samples; fewer plates (a few thousand)."]},
             {"h": "Capillary columns", "tone": "heat", "items": [
                 "15–100 m long, 0.15–0.3 mm wide, fused silica with the film on the inside wall.",
                 "Many more plates (over 100 000): best for complex mixtures. Most GC today is capillary."]}],
         "notes": "Harvey 12.4. Stationary phases: polydimethylsiloxane (nonpolar), add phenyl or cyanopropyl groups for more polarity, polyethylene glycol (polar)."})
    add({"t": "bullets", "sec": 7, "lo": LO4, "title": "What can go into a GC?",
         "items": ["The sample must be <b>volatile</b> and <b>stable when heated</b>.",
                   "Compounds usually come out roughly in order of <b>boiling point</b>; like dissolves like: nonpolar phases for nonpolar solutes, polar phases for polar solutes.",
                   "Non-volatile compounds (amino acids, sugars, many drugs with –OH, –NH<sub>2</sub>, –COOH) are first turned into volatile <b>derivatives</b>.",
                   "<b>Temperature programming</b>: the oven starts cool and heats up during the run, so both low- and high-boiling compounds give sharp peaks in a short time."],
         "notes": "Harvey 12.4. Derivatisation example in Harvey: valine to a volatile ester."})
    add({"t": "table", "sec": 7, "lo": LO4, "title": "GC detectors",
         "head": ["Detector", "How it works", "Detects", "Notes"],
         "rows": [["flame ionisation (FID)", "burns compounds in a H<sub>2</sub>/air flame; measures the ions", "almost all organic compounds", "most common; sensitive; destroys the sample"],
                  ["thermal conductivity (TCD)", "measures a change in how the gas conducts heat", "everything", "universal, not destructive, less sensitive"],
                  ["electron capture (ECD)", "electronegative atoms capture electrons from a radioactive source", "halogens, nitro groups", "very sensitive; pesticides, halogenated solvents"],
                  ["mass spectrometer (GC–MS)", "ionises and sorts fragments by mass", "everything", "identifies unknowns from a spectral library"]],
         "widths": [2.7, 3.3, 2.4, 3.0],
         "caption": "GC–MS is the reference method in forensic and doping laboratories. Source: Harvey 12.4.",
         "notes": "Harvey 12.4."})
    add({"t": "bullets", "sec": 7, "lo": LO5, "title": "GC in pharmacy and health",
         "items": ["<b>Blood alcohol</b> and drugs in clinical and forensic samples (Harvey: clinical uses of GC).",
                   "<b>Residual solvents</b>: traces of solvents (methanol, dichloromethane…) left from manufacture; measured by headspace GC against ICH limits.",
                   "<b>Essential oils and herbal products</b>: fingerprints of volatile components (limonene, menthol, eugenol).",
                   "<b>Doping control</b>: GC–MS screens urine for anabolic steroids and stimulants."],
         "notes": "Harvey 12.4 applications list (clinical: drugs, blood alcohol); residual solvents and doping original."})
    add({"t": "two", "sec": 7, "lo": LO4, "title": "HPLC or GC?",
         "lead": "The sample decides.",
         "cols": [{"h": "Choose HPLC", "tone": "cold", "items": [
             "Non-volatile or heat-sensitive compounds: most drugs, proteins, sugars, salts.",
             "Larger injection volumes; very good precision with a loop injector."]},
             {"h": "Choose GC", "tone": "heat", "items": [
                 "Volatile, heat-stable compounds: solvents, alcohols, essential oils, gases.",
                 "Capillary columns give more plates, so very complex mixtures separate well."]}],
         "notes": "Harvey 12.5 evaluation (HPLC vs GC)."})
    add({"t": "check", "sec": 7, "lo": LO4, "title": "Quick check",
         "q": "The mobile phase in GC is:",
         "opts": ["an inert gas such as helium or nitrogen", "a liquid film on the column wall", "methanol and water", "hydrogen and air"], "ans": 0,
         "why": "H<sub>2</sub> and air feed the FID flame; the carrier gas is inert.", "notes": "Answer A."})
    add({"t": "check", "sec": 7, "lo": LO4, "title": "Quick check",
         "q": "Which sample is best suited to GC?",
         "opts": ["ethanol in a blood sample", "insulin in an injection", "sodium chloride in saline", "starch in a tablet"], "ans": 0,
         "why": "Ethanol is volatile and stable when heated.", "notes": "Answer A."})

    # ================= 8.8 APPLICATIONS =================
    add({"t": "divider", "num": 8, "title": "Applications in Pharmaceutical Analysis", "lo": LO5, "src": "original, with Harvey 12.4–12.5",
         "blurb": "From the raw material to the patient's blood: where each method fits."})
    add({"t": "table", "sec": 8, "lo": LO5, "title": "Quality control of a medicine",
         "head": ["Question", "Test", "Usual method"],
         "rows": [["Is it the right drug?", "identification", "TLC against a standard; HPLC retention time; spectrum from a diode-array or MS detector"],
                  ["Is it pure enough?", "related substances (impurities)", "TLC or HPLC: extra spots or peaks must stay below set limits"],
                  ["How much drug is present?", "assay; content uniformity", "HPLC peak area against a standard"],
                  ["Is it released from the tablet?", "dissolution", "HPLC or UV of samples taken over time"],
                  ["Is anything left from manufacture?", "residual solvents", "headspace GC"],
                  ["Is it still good?", "stability", "HPLC: drug falls, breakdown peaks grow"]],
         "widths": [3.0, 2.8, 4.8],
         "caption": "Pharmacopoeias (BP, USP) give the exact method, column, solvent and limits for each medicine. Table by Dr. NAM.",
         "notes": "Original."})
    add({"t": "two", "sec": 8, "lo": LO5, "title": "Drugs in the body",
         "lead": "Biological samples are messy: clean up first, then separate.",
         "cols": [{"h": "Therapeutic drug monitoring", "tone": "cold", "items": [
             "Narrow-margin drugs (such as antiepileptics and some antibiotics) are measured in blood by HPLC or LC–MS to adjust the dose.",
             "Sample clean-up removes proteins: protein precipitation or solid-phase extraction (the fluoxetine case, 8.6)."]},
             {"h": "Toxicology and forensics", "tone": "heat", "items": [
                 "Overdose and poisoning: screen urine or blood by TLC, GC–MS or LC–MS.",
                 "Blood alcohol by GC; drugs of abuse by GC–MS."]}],
         "notes": "Original, building on Harvey 12.4–12.5."})
    add({"t": "bullets", "sec": 8, "lo": LO5, "title": "Herbal and natural products",
         "items": ["A <b>TLC or HPLC fingerprint</b> shows the pattern of compounds in a plant extract, so the correct plant and the batch quality can be checked.",
                   "<b>Marker compounds</b> are measured by HPLC (for example, a known active or characteristic compound of the plant).",
                   "<b>Adulteration</b>: hidden drugs (such as steroids, sibutramine or sildenafil) in 'herbal' slimming or energy products are found by TLC, then confirmed by HPLC or LC–MS.",
                   "Column chromatography is also how chemists <b>isolate</b> new active compounds from plants."],
         "notes": "Original pharmacy links. Back to the 'Think first' slide."})
    add({"t": "table", "sec": 8, "lo": LO5, "title": "Choosing a method",
         "head": ["Method", "Separates by", "Best for", "Speed and cost"],
         "rows": [["paper", "partition (water in cellulose)", "very polar: amino acids, sugars, dyes", "slow; very cheap"],
                  ["TLC", "adsorption (silica)", "quick identity and purity checks; many samples at once", "fast; cheap"],
                  ["ion exchange", "charge", "ions, amino acids, proteins; purified water", "moderate"],
                  ["HPLC", "partition (C18), adsorption, ion exchange", "assay of most drugs; impurities; blood levels", "minutes per sample; costly instrument"],
                  ["GC", "partition (liquid film); boiling point", "volatile compounds: solvents, alcohol, essential oils", "minutes per sample; costly instrument"]],
         "widths": [1.8, 3.0, 3.8, 2.6],
         "caption": "TLC screens; HPLC and GC measure; MS detectors confirm. Table by Dr. NAM.",
         "notes": "Original summary table."})
    add({"t": "tryit", "sec": 8, "lo": LO5, "title": "Try it · Pick the method",
         "q": "Choose a suitable method and give one reason. (a) Checking whether a bottle of paracetamol powder is really paracetamol, quickly and cheaply (b) Measuring the amount of paracetamol in each tablet (c) Finding traces of methanol left in a drug from manufacture (d) Separating Na<sup>+</sup> and Ca<sup>2+</sup> ions",
         "a": "(a) <b>TLC</b> against a paracetamol standard on the same plate: fast and cheap. (b) <b>HPLC</b> with UV detection: peak area against a calibration curve. (c) <b>Headspace GC</b>: methanol is volatile. (d) <b>Ion-exchange</b> on a cation exchanger: Ca<sup>2+</sup> (higher charge) is held more strongly.",
         "notes": "Original."})
    add({"t": "check", "sec": 8, "lo": LO5, "title": "Quick check",
         "q": "An HPLC test of a 2-year-old aspirin batch shows a growing peak for salicylic acid. This test is part of:",
         "opts": ["stability testing", "residual solvent testing", "dissolution testing", "identification by co-spotting"], "ans": 0,
         "why": "Breakdown products rise over time.", "notes": "Answer A."})
    add({"t": "check", "sec": 8, "lo": LO5, "title": "Quick check",
         "q": "Before HPLC of a drug in blood, the sample is first passed through a C18 cartridge mainly to:",
         "opts": ["remove proteins and other material that would clog the column", "make the drug volatile", "turn the drug into ions", "increase the peak width"], "ans": 0,
         "why": "Sample clean-up protects the column (the fluoxetine method).", "notes": "Answer A."})

    # ================= wrap-up =================
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Principle", "stationary vs mobile phase; components that prefer the stationary phase move slowly"],
        ["Types", "planar or column; liquid or gas; adsorption, partition, ion exchange, size exclusion, affinity"],
        ["Chromatogram", "t<sub>r</sub> identifies, area measures; k, α, R (≥ 1.5 = baseline), plates N"],
        ["Phases", "like holds like; normal phase (silica): less polar first; reversed phase (C18): more polar first; P′"],
        ["TLC", "pencil origin, closed tank, UV 254 / iodine / sprays; R<sub>f</sub> = spot ÷ front; run the standard alongside"],
        ["Ion exchange", "cation exchangers –SO<sub>3</sub><sup>−</sup> (strong), –COO<sup>−</sup> (weak); anion –NR<sub>3</sub><sup>+</sup> (strong), –NH<sub>3</sub><sup>+</sup> (weak)"],
        ["HPLC and GC", "HPLC: pump, loop, C18 column, UV; GC: inert gas, heated oven, FID or MS; volatile samples only"],
        ["Pharmacy", "identity, impurities, assay, dissolution, stability, residual solvents, drugs in blood, herbal fingerprints"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next session",
         "items": ["Complete the after-class activity (about 30 min)", "Attempt the Chapter 8 tutorial",
                   "Play the Chapter 8 game to find your weak outcomes", "Lab Practical 4: Thin Layer Chromatography"],
         "attrib": "Adapted from LibreTexts (Harvey, Analytical Chemistry 2.1 and Instrumental Analysis), CC BY-NC-SA 4.0, with original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"] + " Further reading on TLC technique: Nichols, Organic Chemistry Lab Techniques, section 2.3 (LibreTexts)."})
    return S
