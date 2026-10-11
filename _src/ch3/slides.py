"""PHD125 Chapter 3 · Organic Compounds that Contain Oxygen and Sulphur · lecture slide content.
Sources: Ball 14.1-14.11 and 14.E (CC BY-NC-SA 3.0); FGOB 14.4 (reactions of alcohols), 14.5 (phenols), 14.7 (ethers),
14.8 (thiols), 14.9 (haloalkanes, elimination), 15.1-15.5 (aldehydes and ketones), same licence.
Original material by Dr. NAM (no usable source page): SN1 and SN2, substitution vs elimination, Zaitsev, dichromate
colour test, Benedict's test, reduction of carbonyls, hemiacetals, and the pharmacy links."""
from figs import mol, row, scheme, stack


def mini(smi, hs=False, h=48):
    return f'<img src="{mol(smi, 190, 84, hs=hs)}" alt="" style="height:{h}px;display:block;background:#fff;border-radius:6px;padding:1px 4px">'


LO1, LO2, LO3, LO4, LO5 = 'CH3-LO1', 'CH3-LO2', 'CH3-LO3', 'CH3-LO4', 'CH3-LO5'

META = {
    "code": "CH3", "chapter": "Chapter 3", "title": "Organic Compounds that Contain Oxygen and Sulphur", "short": "Oxygen and Sulphur Compounds",
    "sub": "PHD125 Pharmaceutical Organic Chemistry",
    "src": "Core reference: Ball, Hill & Scott, The Basics of GOB Chemistry, chapter 14, with FGOB 14.4–14.9 and 15.1–15.5",
    "attrib": ("Adapted from <i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 14 and exercises 14.E, and <i>Fundamentals of General Organic and "
               "Biological Chemistry</i> 14.4–14.9 and 15.1–15.5, LibreTexts, CC BY-NC-SA 3.0. SN1 and SN2, substitution versus elimination, the dichromate and Benedict's "
               "tests, reduction of carbonyls, hemiacetals and the pharmacy links are original material by Dr. NAM. Structures drawn with RDKit. "
               "Shared under CC BY-NC-SA for non-commercial teaching."),
    "secmol": {"1": ["ethanol", "propanol", "glycerol"], "2": ["diethylether", "ethanethiol", "ethanol"], "3": ["acetone", "acetaldehyde", "formaldehyde"]},
    "titlemol": ["ethanol", "acetone", "diethylether", "ethanethiol"], "darkmol": "ethanol",
    "next": "Next chapter: Carboxylic Acid, Ester, Amines, Amide",
    "brand": "Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang",
}

OUTCOMES = [
    [LO1, "Name and classify alcohols (1°, 2°, 3°) and phenols, and relate their properties to hydrogen bonding"],
    [LO2, "Explain SN1 and SN2 reactions of haloalkanes that form alcohols, and predict which one occurs"],
    [LO3, "Predict the products of alcohol dehydration (alkene or ether) and oxidation (1°, 2° and 3° alcohols)"],
    [LO4, "Name ethers and thiols, compare their properties with alcohols, and describe disulfide formation"],
    [LO5, "Name aldehydes and ketones, explain their properties, and predict their oxidation, reduction and test results"],
]


def build():
    S = []
    add = S.append
    add({"t": "title", "title": "Organic Compounds that Contain Oxygen and Sulphur", "sub": "PHD125 Pharmaceutical Organic Chemistry · Chapter 3",
         "notes": "Chapter 3 of the course outline, in three subchapters: alcohols (with SN1 and SN2), ethers and thiols, and aldehydes and ketones."})
    add({"t": "outcomes", "title": "Learning outcomes", "items": OUTCOMES,
         "notes": "LO1–LO3: 3.1 Alcohols. LO4: 3.2 Ethers & Thiols. LO5: 3.3 Aldehydes & Ketones."})
    add({"t": "bullets", "title": "Lecture map", "items": [
        "<b>3.1 Alcohols</b> (Ball 14.2–14.7, FGOB 14.4–14.5): classes and names, properties, glycols, making alcohols, SN1 and SN2, dehydration, oxidation, phenols",
        "<b>3.2 Ethers &amp; Thiols</b> (Ball 14.8, 14.11; FGOB 14.7–14.8): the \"alcohol relatives\": names, properties, anaesthetics, disulfide bridges",
        "<b>3.3 Aldehydes &amp; Ketones</b> (Ball 14.9–14.10; FGOB 15.1–15.5): the carbonyl group, names, properties, oxidation and tests, reduction"],
         "notes": "Ethers and thiols are a short subchapter."})
    add({"t": "hook", "title": "Think first",
         "q": "Hand sanitiser, the gas in LPG that you can smell, the anaesthetic used in the first public surgery, and nail-polish remover. What links them?",
         "a": "Each contains <b>oxygen or sulphur</b> bonded into a carbon skeleton: an <b>alcohol</b> (ethanol, 2-propanol), a <b>thiol</b> (ethanethiol, added to LPG for its smell), an <b>ether</b> (diethyl ether, 1846) and a <b>ketone</b> (acetone). One O or S atom changes a hydrocarbon's properties completely.",
         "notes": "Pairs discuss for one minute."})

    # ================= 3.1 ALCOHOLS =================
    add({"t": "divider", "num": 1, "title": "Alcohols", "lo": "CH3-LO1 to LO3", "src": "Ball 14.2–14.7 · FGOB 14.4–14.5, 14.9",
         "blurb": "The –OH family: how to name and classify alcohols, how they are made from haloalkanes, and the reactions pharmacists rely on."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Classifying alcohols: 1°, 2°, 3°",
         "fig": {"cap": "Count the carbons bonded to the carbon that carries the –OH.",
                 "data": row([(mol("CCO", 210, 110), "1° · ethanol (RCH₂OH)"), (mol("CC(C)O", 210, 110), "2° · 2-propanol (R₂CHOH)"), (mol("CC(C)(C)O", 210, 110), "3° · 2-methyl-2-propanol (R₃COH)")], w=270, h=110)},
         "items": ["<b>Primary (1°)</b>: the C–OH carbon is bonded to <b>one</b> other carbon. <b>Secondary (2°)</b>: to <b>two</b>. <b>Tertiary (3°)</b>: to <b>three</b>.",
                   "The class decides how an alcohol is oxidised (later in this subchapter), and how its haloalkane reacts (SN1 or SN2).",
                   "An –OH on a benzene ring is a <b>phenol</b>, a separate family (end of this subchapter)."],
         "notes": "Ball 14.2. Methanol has no class (no other carbon)."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Naming alcohols",
         "head": ["Rule", "Example"],
         "rows": [["Parent = the longest chain that <b>contains the C–OH</b>. Change -e to <b>-ol</b>.", "CH<sub>3</sub>CH<sub>2</sub>OH is ethanol"],
                  ["Number from the end <b>nearest the –OH</b>; put its number before the name.", "CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub> is 2-butanol"],
                  ["Name and number other substituents as in alkanes.", "CH<sub>3</sub>CH(OH)CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub> is 3-methyl-2-pentanol"],
                  ["Rings: the C–OH carbon is C1 (no number needed).", "cyclohexanol"],
                  ["Two or three –OH: keep the -e and add <b>-diol</b>, <b>-triol</b>.", "HOCH<sub>2</sub>CH<sub>2</sub>OH is 1,2-ethanediol"]],
         "widths": [5.2, 4.0], "caption": "Common names: alkyl group + alcohol (ethyl alcohol, isopropyl alcohol, tert-butyl alcohol). Source: Ball 14.2.",
         "notes": "Ball 14.2 rules and examples."})
    add({"t": "tryit", "sec": 1, "lo": LO1, "title": "Try it · Name and classify",
         "q": "Name and classify: (a) CH<sub>3</sub>(CH<sub>2</sub>)<sub>5</sub>OH (b) CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (c) (CH<sub>3</sub>)<sub>3</sub>COH",
         "a": "(a) <b>1-hexanol</b>, primary (b) <b>3-hexanol</b>, secondary (c) <b>2-methyl-2-propanol</b>, tertiary (Ball 14.E).",
         "notes": "Ball 14.E, 14.2 exercise 1a, 1b; (c) from Ball table."})
    add({"t": "table", "sec": 1, "lo": LO1, "title": "Hydrogen bonding raises boiling points",
         "head": ["Compound", "Molar mass (g/mol)", "Boiling point (°C)", "Forces"],
         "rows": [["ethane, C<sub>2</sub>H<sub>6</sub>", "30", "−89", "dispersion"], ["methanol, CH<sub>3</sub>OH", "32", "65", "hydrogen bonds"],
                  ["propane, C<sub>3</sub>H<sub>8</sub>", "44", "−42", "dispersion"], ["ethanol, CH<sub>3</sub>CH<sub>2</sub>OH", "46", "78", "hydrogen bonds"],
                  ["butane, C<sub>4</sub>H<sub>10</sub>", "58", "−1", "dispersion"], ["1-propanol, CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH", "60", "97", "hydrogen bonds"]],
         "widths": [3.6, 2.0, 2.0, 2.2],
         "caption": "Source: Ball Table 14.3.1. Alcohols of 1–3 carbons mix completely with water (they hydrogen bond with it). Solubility falls as the chain grows; the borderline is about 4–5 carbons, and 1-decanol is insoluble.",
         "notes": "Ball 14.3."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "Alcohols in the pharmacy",
         "items": ["<b>Ethanol</b>: solvent in tinctures, elixirs and mouthwashes; hand rubs (60–80%).",
                   "<b>2-Propanol</b> (isopropyl alcohol): 70% rubbing alcohol and alcohol swabs. It cools the skin as it evaporates (sponge baths).",
                   "<b>Glycerol</b> (1,2,3-propanetriol): sweet, non-toxic humectant in creams, cough syrups and suppositories.",
                   "<b>Propylene glycol</b> (1,2-propanediol): drug solvent in oral and injectable products; non-toxic because it is metabolised to pyruvate.",
                   "<b>Ethylene glycol</b> (antifreeze) is poisonous: it is oxidised to oxalate, which forms calcium oxalate crystals in the kidneys."],
         "side": {"h": "Toxicity", "body": "Methanol is oxidised to formaldehyde and formic acid. About 15 mL can cause blindness; 100–150 mL is usually fatal (Ball 14.4)."},
         "notes": "Ball 14.4, 14.6; formulation uses are standard pharmacy knowledge."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO1, "title": "Making alcohols: three routes",
         "fig": {"cap": "Hydration of an alkene follows Markovnikov's rule (Chapter 2).",
                 "data": scheme([('m', 'C=CC', 'propene', 130), ('+',), ('t', 'H₂O', 60), ('>', 'H₂SO₄', ''), ('m', 'CC(O)C', '2-propanol', 150)], h=110)},
         "items": ["<b>Hydration of alkenes</b> with an acid catalyst: ethene → ethanol; propene → 2-propanol (Ball 14.4).",
                   "<b>Fermentation</b> of sugars and starch by yeast enzymes → ethanol (drinks and much industrial ethanol).",
                   "<b>Substitution of haloalkanes</b>: R–X + OH<sup>−</sup> → R–OH + X<sup>−</sup>. This is where SN1 and SN2 come in (next slides).",
                   "Industry also makes methanol from CO + 2 H<sub>2</sub> (ZnO/Cr<sub>2</sub>O<sub>3</sub>, 350 °C)."],
         "notes": "Ball 14.4; haloalkane route is original framing for SN1/SN2."})
    # ---- SN1 / SN2 (core)
    add({"t": "two", "sec": 1, "lo": LO2, "title": "Nucleophilic substitution: three key words",
         "lead": "In R–X + Nu<sup>−</sup> → R–Nu + X<sup>−</sup>, a <b>nucleophile</b> replaces a <b>leaving group</b> on a carbon.",
         "cols": [{"h": "Who's who", "tone": "cold", "items": [
             "<b>Nucleophile</b> (\"nucleus-lover\"): an electron-rich species with a lone pair that attacks a δ+ carbon. Examples: OH<sup>−</sup>, H<sub>2</sub>O, CN<sup>−</sup>, NH<sub>3</sub>",
             "<b>Leaving group</b>: the atom that leaves with the bonding electrons. Halide ions are good: I<sup>−</sup> > Br<sup>−</sup> > Cl<sup>−</sup>",
             "<b>Substrate</b>: the haloalkane. C–X is polar, so the carbon is δ+"]},
             {"h": "Carbocation", "tone": "heat", "items": [
                 "A <b>carbocation</b> is a carbon with only three bonds and a positive charge (C<sup>+</sup>)",
                 "Stability: <b>3° > 2° > 1°</b>. Alkyl groups push electron density towards C<sup>+</sup> and spread the charge",
                 "You met it in Markovnikov's rule: H<sup>+</sup> adds so the more stable carbocation forms",
                 "OH<sup>−</sup> is a <b>poor</b> leaving group, so alcohols need acid to react (dehydration, later)"]}],
         "notes": "Original core section (SN1/SN2 are not in the Ball or FGOB pages)."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO2, "title": "SN2: one step, backside attack",
         "fig": {"cap": "Bromoethane (1°) + OH<sup>−</sup> → ethanol + Br<sup>−</sup> (warm aqueous NaOH). Curly arrows show electron pairs moving.",
                 "data": sn2_svg()},
         "items": ["<b>S</b>ubstitution, <b>N</b>ucleophilic, <b>2</b> species in the rate-determining step: rate depends on <b>both</b> [R–X] and [Nu].",
                   "The nucleophile attacks the carbon from the side <b>opposite</b> the leaving group, as the C–Br bond breaks: a single step.",
                   "Best for <b>methyl and 1°</b> haloalkanes: the back of the carbon is not crowded. Very slow for 3° (blocked).",
                   "If the carbon is chiral, its configuration is <b>inverted</b>, like an umbrella turning inside out in the wind."],
         "notes": "Original. Inversion = Walden inversion (name not required)."})
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO2, "title": "SN1: two steps, through a carbocation",
         "fig": {"cap": "2-Bromo-2-methylpropane (3°) + water → 2-methyl-2-propanol.",
                 "data": scheme([('m', 'CC(C)(C)Br', '3° haloalkane', 150), ('>', 'step 1 (slow)', '− Br⁻'), ('m', 'C[C+](C)C', '3° carbocation', 140), ('>', 'step 2 (fast)', '+ H₂O, − H⁺'), ('m', 'CC(C)(C)O', '3° alcohol', 140)], h=110)},
         "items": ["<b>Step 1</b> (slow): the leaving group goes first, giving a carbocation. <b>Step 2</b> (fast): the nucleophile attacks the flat C<sup>+</sup>.",
                   "<b>1</b> species in the slow step: rate depends on [R–X] only, not on the nucleophile.",
                   "Best for <b>3°</b> haloalkanes, which form the most stable carbocations. Weak nucleophiles such as water are enough.",
                   "The flat carbocation can be attacked from <b>either face</b>, so a chiral product forms as a <b>mixture</b> of both mirror images."],
         "notes": "Original."})
    add({"t": "table", "sec": 1, "lo": LO2, "title": "SN1 or SN2?",
         "head": ["", "SN2", "SN1"],
         "rows": [["Steps", "one step", "two steps, via a carbocation"],
                  ["Rate depends on", "[R–X] and [Nu]", "[R–X] only"],
                  ["Best substrate", "methyl, <b>1°</b>", "<b>3°</b>"],
                  ["2° haloalkanes", "either (strong nucleophile → SN2)", "either (weak nucleophile, water → SN1)"],
                  ["Nucleophile", "strong (OH<sup>−</sup>, CN<sup>−</sup>)", "weak is enough (H<sub>2</sub>O)"],
                  ["Chiral carbon", "inverted", "mixture of both forms"]],
         "widths": [2.2, 3.6, 3.6],
         "caption": "Memory aid: SN<b>2</b> likes <b>uncrowded</b> carbons (1°); SN<b>1</b> likes <b>stable carbocations</b> (3°).",
         "notes": "Original summary table. Solvent effects and rate laws in detail are beyond diploma level."})
    add({"t": "example", "sec": 1, "lo": LO2, "title": "Example 3.1 · Predict the mechanism",
         "q": "Which mechanism, SN1 or SN2, is most likely for each? (a) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>Br with NaOH(aq) (b) (CH<sub>3</sub>)<sub>3</sub>CCl in water (c) CH<sub>3</sub>I with OH<sup>−</sup>",
         "steps": ["(a) 1-Bromopropane is <b>primary</b>, and OH<sup>−</sup> is a strong nucleophile → <b>SN2</b>. Product: 1-propanol.",
                   "(b) 2-Chloro-2-methylpropane is <b>tertiary</b>, and water is a weak nucleophile → <b>SN1</b>. Product: 2-methyl-2-propanol.",
                   "(c) Methyl iodide: methyl, uncrowded, excellent leaving group → <b>SN2</b>. Product: methanol."],
         "notes": "Original."})
    add({"t": "two", "sec": 1, "lo": LO2, "title": "Substitution or elimination?",
         "lead": "OH<sup>−</sup> can act as a <b>nucleophile</b> (substitution) or as a <b>base</b> (elimination). Conditions decide.",
         "cols": [{"h": "Substitution → alcohol", "tone": "cold", "items": [
             "NaOH or KOH in <b>water</b>, warm",
             "CH<sub>3</sub>CH<sub>2</sub>Br + OH<sup>−</sup> → CH<sub>3</sub>CH<sub>2</sub>OH + Br<sup>−</sup>",
             "Favoured by 1° haloalkanes"]},
             {"h": "Elimination → alkene", "tone": "heat", "items": [
                 "KOH in <b>ethanol</b>, <b>hot</b>",
                 "CH<sub>3</sub>CH<sub>2</sub>Br + OH<sup>−</sup> → CH<sub>2</sub>=CH<sub>2</sub> + H<sub>2</sub>O + Br<sup>−</sup>",
                 "H and X are removed from <b>adjacent</b> carbons (FGOB 14.9). Favoured by 3° haloalkanes",
                 "One-step (E2) or two-step via a carbocation (E1), mirroring SN2 and SN1"]}],
         "notes": "FGOB 14.9 (elimination with a strong base); conditions and E1/E2 labels original."})
    add({"t": "bullets", "sec": 1, "lo": LO2, "title": "SN2 in medicine: alkylating anticancer drugs",
         "items": ["<b>Nitrogen mustards</b> such as cyclophosphamide and chlorambucil contain C–Cl groups.",
                   "In the body they form a reactive group that is attacked by a nitrogen in <b>DNA</b> (on guanine): an SN2-type substitution that attaches the drug to DNA.",
                   "Each molecule can do this twice, <b>cross-linking</b> DNA strands so that cancer cells cannot divide.",
                   "The same chemistry explains their side effects: healthy fast-dividing cells (bone marrow, hair follicles) are also hit."],
         "notes": "Original pharmacy link; simplified (aziridinium intermediate not named)."})
    add({"t": "check", "sec": 1, "lo": LO2, "title": "Quick check",
         "q": "A haloalkane reacts at a rate that doubles when [OH<sup>−</sup>] doubles. It is most likely:",
         "opts": ["a 3° haloalkane reacting by SN1", "a 1° haloalkane reacting by SN2", "an alkene", "a carbocation"], "ans": 1,
         "why": "The rate depends on the nucleophile, so both species are in the slow step: SN2, typical of 1° haloalkanes.", "notes": "Answer B."})
    add({"t": "check", "sec": 1, "lo": LO2, "title": "Quick check",
         "q": "Why do 3° haloalkanes react by SN1 rather than SN2?",
         "opts": ["They have no leaving group", "Their carbon is too crowded for backside attack, and they form stable carbocations", "They are not polar", "They react only with acids"], "ans": 1,
         "why": "Three alkyl groups block the back of the carbon, and they stabilise the C<sup>+</sup>.", "notes": "Answer B."})
    # ---- reactions of alcohols
    add({"t": "figure", "pos": "top", "sec": 1, "lo": LO3, "title": "Dehydration: alkene or ether",
         "fig": {"cap": "Ethanol with concentrated H<sub>2</sub>SO<sub>4</sub>: the temperature decides the product (FGOB 14.4, Ball 14.E).",
                 "data": stack([scheme([('m', 'CCO', 'ethanol', 120), ('>', 'conc. H₂SO₄', '180 °C'), ('m', 'C=C', 'ethene', 110, True), ('+',), ('t', 'H₂O', 60)], h=100),
                                scheme([('t', '2', 30), ('m', 'CCO', 'ethanol', 120), ('>', 'conc. H₂SO₄', '140 °C, excess alcohol'), ('m', 'CCOCC', 'diethyl ether', 160), ('+',), ('t', 'H₂O', 60)], h=100)], w=760, row_h=130)},
         "items": ["<b>High temperature, excess acid</b>: –OH and an H on the <b>adjacent</b> carbon leave as water, giving an <b>alkene</b> (an elimination).",
                   "<b>Lower temperature, excess alcohol</b>: two molecules join, losing water, to give an <b>ether</b> (3.2).",
                   "When the H can come from either side, the <b>more substituted</b> alkene is the major product: 2-butanol gives mainly 2-butene (Zaitsev's rule)."],
         "notes": "FGOB 14.4; Zaitsev added (FGOB 14.9 notes a mixture of 1- and 2-butene). Dehydration of 2° and 3° alcohols goes through a carbocation (E1)."})
    add({"t": "table", "sec": 1, "lo": LO3, "title": "Oxidation depends on the class",
         "head": ["Alcohol", "With acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> [O]", "Colour"],
         "rows": [["<b>1°</b> RCH<sub>2</sub>OH", "→ <b>aldehyde</b> RCHO → (further) <b>carboxylic acid</b> RCOOH", "orange → green"],
                  ["<b>2°</b> R<sub>2</sub>CHOH", "→ <b>ketone</b> R<sub>2</sub>C=O (stops here)", "orange → green"],
                  ["<b>3°</b> R<sub>3</sub>COH", "<b>no reaction</b>: no H on the C–OH carbon", "stays orange"]],
         "widths": [2.4, 5.2, 2.0],
         "caption": "Oxidation removes two H atoms: one from –OH and one from the C–OH carbon. A 3° carbon has no H to lose. Orange Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> is reduced to green Cr<sup>3+</sup>: a quick lab test for 1° and 2° alcohols, and the basis of old breathalysers.",
         "notes": "FGOB 14.4 (oxidation by class, K2Cr2O7); colour change and breathalyser original."})
    add({"t": "figure", "pos": "leftwide", "sec": 1, "lo": LO3, "title": "Example 3.2 · Oxidise each alcohol",
         "fig": {"cap": "[O] = an oxidising agent such as acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>.",
                 "data": stack([scheme([('m', 'CCCCCO', '1-pentanol (1°)', 170), ('>', '[O]', ''), ('m', 'CCCCC=O', 'pentanal', 160), ('>', '[O]', ''), ('m', 'CCCCC(=O)O', 'pentanoic acid', 180)], h=95),
                                scheme([('m', 'CCCC(C)O', '2-pentanol (2°)', 170), ('>', '[O]', ''), ('m', 'CCCC(C)=O', '2-pentanone', 160)], h=95),
                                scheme([('m', 'CC(C)(C)O', '2-methyl-2-propanol (3°)', 210), ('>', '[O]', ''), ('t', 'no reaction', 140)], h=95)], w=640, row_h=140)},
         "items": ["<b>1°</b> → aldehyde → carboxylic acid. To stop at the aldehyde, distil it off as it forms.", "<b>2°</b> → ketone; ketones resist further oxidation.", "<b>3°</b> → no reaction.", "(FGOB 14.4 Example; Ball 14.E)"],
         "notes": "FGOB 14.4 Example a–c; Ball 14.E 14.5 exercise 3b."})
    add({"t": "bullets", "sec": 1, "lo": LO3, "title": "Oxidation in the body: ethanol and methanol",
         "items": ["Liver enzymes oxidise <b>ethanol</b> → acetaldehyde → acetic acid → CO<sub>2</sub> + H<sub>2</sub>O. Acetaldehyde causes the flushing and hangover.",
                   "<b>Methanol</b> is oxidised by the same enzyme (alcohol dehydrogenase) to <b>formaldehyde</b> and <b>formic acid</b>, which damage the optic nerve.",
                   "Treatment of methanol poisoning: <b>fomepizole</b> or ethanol, which block alcohol dehydrogenase so methanol is excreted unchanged.",
                   "Disulfiram (for alcohol dependence) blocks the next step, so acetaldehyde builds up and drinking feels very unpleasant."],
         "notes": "Ball 14.4 (metabolism); treatments are standard pharmacology (original)."})
    add({"t": "bullets", "sec": 1, "lo": LO1, "title": "Phenols: –OH on a benzene ring",
         "items": ["<b>Phenols</b> (ArOH) are weakly <b>acidic</b>, unlike alcohols: C<sub>6</sub>H<sub>5</sub>OH + H<sub>2</sub>O ⇌ C<sub>6</sub>H<sub>5</sub>O<sup>−</sup> + H<sub>3</sub>O<sup>+</sup>. They react with NaOH to form salts.",
                   "<b>Phenol</b> (carbolic acid) was the first antiseptic: Joseph <b>Lister</b>, 1867. It is toxic and burns skin.",
                   "Safer phenols: <b>4-hexylresorcinol</b> (throat lozenges), <b>thymol</b> (mouthwash), <b>chloroxylenol</b> (household antiseptic).",
                   "Paracetamol and salbutamol contain phenol groups (Chapter 1)."],
         "side": {"h": "Name it", "body": "Phenols are named as phenol derivatives: o-nitrophenol, p-bromophenol (Ball 14.E)."},
         "notes": "FGOB 14.5; Ball 14.7, 14.E. Chloroxylenol added (original)."})
    add({"t": "check", "sec": 1, "lo": LO3, "title": "Quick check",
         "q": "Which alcohol does NOT turn acidified dichromate from orange to green?",
         "opts": ["ethanol", "2-propanol", "2-methyl-2-propanol", "cyclohexanol"], "ans": 2,
         "why": "2-Methyl-2-propanol is tertiary: no H on the C–OH carbon, so it is not oxidised.", "notes": "Answer C."})
    add({"t": "check", "sec": 1, "lo": LO3, "title": "Quick check",
         "q": "What is the main product when 2-propanol is heated with excess concentrated H<sub>2</sub>SO<sub>4</sub> at 180 °C?",
         "opts": ["propene", "acetone", "diisopropyl ether", "propanal"], "ans": 0,
         "why": "High temperature and excess acid favour elimination of water → propene. (Acetone needs an oxidising agent.)", "notes": "Answer A. Note: the Ball 14.E answer key gives acetone here in error."})

    # ================= 3.2 ETHERS & THIOLS =================
    add({"t": "divider", "num": 2, "title": "Ethers & Thiols", "lo": "CH3-LO4", "src": "Ball 14.8, 14.11 · FGOB 14.7–14.8",
         "blurb": "Two relatives of alcohols: swap the O–H hydrogen for carbon (ether), or swap the O for S (thiol)."})
    add({"t": "figure", "pos": "top", "sec": 2, "lo": LO4, "title": "Alcohol, ether, thiol",
         "fig": {"cap": "Same skeleton, three families.",
                 "data": row([(mol("CCO", 170, 100), "ethanol · R–OH"), (mol("CCOCC", 200, 100), "diethyl ether · R–O–R′"), (mol("CCS", 170, 100), "ethanethiol · R–SH"), (mol("CCSSCC", 210, 100), "diethyl disulfide · R–S–S–R")], w=230, h=100)},
         "items": ["<b>Ethers</b> R–O–R′: an alcohol whose O–H hydrogen is replaced by a carbon group. Common names: the two groups + <b>ether</b> (methyl propyl ether, diethyl ether).",
                   "<b>Thiols</b> R–SH (mercaptans): the sulfur version of an alcohol. IUPAC: alkane + <b>-thiol</b> (ethanethiol).",
                   "<b>Sulfides</b> (thioethers) R–S–R′ and <b>disulfides</b> R–S–S–R′ are their relatives."],
         "notes": "Ball 14.8, 14.11; FGOB 14.7–14.8."})
    add({"t": "table", "sec": 2, "lo": LO4, "title": "Ethers have no O–H: low boiling points",
         "head": ["Compound", "Molar mass (g/mol)", "Boiling point (°C)", "H-bonds between molecules?"],
         "rows": [["pentane", "72", "36", "no"], ["diethyl ether", "74", "35", "no"], ["1-butanol", "74", "117", "yes"],
                  ["propane", "44", "−42", "no"], ["dimethyl ether", "46", "−25", "no"], ["ethanol", "46", "78", "yes"]],
         "widths": [2.6, 2.2, 2.2, 3.0],
         "caption": "Ethers boil like alkanes of similar mass. But their O can accept H-bonds <b>from water</b>, so an ether is about as soluble as its isomeric alcohol: dimethyl ether and ethanol (C<sub>2</sub>H<sub>6</sub>O) mix with water; diethyl ether and 1-butanol (C<sub>4</sub>H<sub>10</sub>O) dissolve only about 8 g/100 mL. Source: FGOB Table 14.7.1.",
         "notes": "FGOB 14.7."})
    add({"t": "bullets", "sec": 2, "lo": LO4, "title": "Ethers in pharmacy",
         "items": ["<b>Diethyl ether</b> was the first general anaesthetic (William Morton, Boston, 1846): wide safety margin, but highly flammable and nauseating.",
                   "It was replaced by halogenated ethers: <b>enflurane, isoflurane, sevoflurane</b>.",
                   "Ethers are <b>unreactive</b>, so they are good solvents for extractions in the lab.",
                   "Lab safety: diethyl ether is extremely flammable, and old bottles can form <b>explosive peroxides</b>. Date opened bottles and keep them away from flames."],
         "notes": "FGOB 14.7 (anaesthesia history); sevoflurane and peroxide note original."})
    add({"t": "bullets", "sec": 2, "lo": LO4, "title": "Thiols: smell and disulfide bridges",
         "items": ["Thiols have strong, unpleasant smells. <b>Ethanethiol</b> is added to odourless LPG so leaks can be smelled (FGOB 14.8).",
                   "Mild oxidation joins two thiols into a <b>disulfide</b>: 2 R–SH + [O] → R–S–S–R + H<sub>2</sub>O. Reduction splits it again.",
                   "The amino acid <b>cysteine</b> has an –SH. Disulfide bridges hold <b>proteins</b> such as insulin in shape (Chapter 7). Hair perming breaks and re-forms them.",
                   "Pharmacy link: the blood-pressure drug <b>captopril</b> has a thiol group; <b>N-acetylcysteine</b> (a thiol) is the antidote for paracetamol overdose."],
         "notes": "FGOB 14.8; drug examples original."})
    add({"t": "check", "sec": 2, "lo": LO4, "title": "Quick check",
         "q": "Why does 1-butanol (bp 117 °C) boil much higher than diethyl ether (bp 35 °C), although both are C<sub>4</sub>H<sub>10</sub>O?",
         "opts": ["Diethyl ether is heavier", "1-Butanol forms hydrogen bonds between its molecules; the ether has no O–H", "The ether is ionic", "1-Butanol is a thiol"], "ans": 1,
         "why": "Ether molecules cannot hydrogen bond to each other (Ball 14.E).", "notes": "Answer B."})
    add({"t": "check", "sec": 2, "lo": LO4, "title": "Quick check",
         "q": "What forms when two cysteine –SH groups are oxidised?",
         "opts": ["an ether", "a disulfide bridge (–S–S–)", "a sulfate", "a ketone"], "ans": 1,
         "why": "2 R–SH → R–S–S–R. These bridges hold protein chains together.", "notes": "Answer B."})

    # ================= 3.3 ALDEHYDES & KETONES =================
    add({"t": "divider", "num": 3, "title": "Aldehydes & Ketones", "lo": "CH3-LO5", "src": "Ball 14.9–14.10 · FGOB 15.1–15.5",
         "blurb": "The carbonyl group: names, polarity, and how one H atom makes aldehydes easy to oxidise."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO5, "title": "The carbonyl group, C=O",
         "fig": {"cap": "Aldehydes have C=O at the end of a chain; ketones have it inside.",
                 "data": row([(mol("C=O", 150, 100, hs=True), "methanal (formaldehyde)"), (mol("CC=O", 160, 100), "ethanal (acetaldehyde)"), (mol("CC(C)=O", 160, 100), "propanone (acetone)"), (mol("CCC(C)=O", 170, 100), "butanone (ethyl methyl ketone)")], w=230, h=100)},
         "items": ["<b>Aldehyde</b> RCHO: the carbonyl carbon has at least one <b>H</b>. <b>Ketone</b> RCOR′: it has <b>two carbon</b> groups.",
                   "C=O is very <b>polar</b>: O is δ−, C is δ+. The δ+ carbon is where nucleophiles attack.",
                   "The simplest ketone has three carbons."],
         "notes": "FGOB 15.1; Ball 14.9."})
    add({"t": "table", "sec": 3, "lo": LO5, "title": "Naming aldehydes and ketones",
         "head": ["Rule", "Example"],
         "rows": [["Parent = the longest chain containing the C=O. Aldehyde: -e → <b>-al</b>. Ketone: -e → <b>-one</b>.", "propanal; propanone"],
                  ["Aldehyde: the carbonyl carbon is always <b>C1</b>, so no number is needed.", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CHO is 2-methylpentanal"],
                  ["Ketone: number to give the C=O the <b>lowest number</b>.", "CH<sub>3</sub>COCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> is 2-pentanone"],
                  ["Cyclic ketones: the C=O carbon is C1.", "cyclohexanone"],
                  ["Common names: aldehydes from their acids (form-, acet-, propion-, butyr-); ketones: two groups + <b>ketone</b>.", "acetaldehyde; dimethyl ketone (acetone)"]],
         "widths": [5.4, 3.8], "caption": "Do not confuse <b>-al</b> (aldehyde) with <b>-ol</b> (alcohol). Source: FGOB 15.1–15.2.",
         "notes": "FGOB 15.2 rules."})
    add({"t": "tryit", "sec": 3, "lo": LO5, "title": "Try it · Name these",
         "q": "Name: (a) (CH<sub>3</sub>)<sub>2</sub>CHCOCH(CH<sub>3</sub>)<sub>2</sub> (b) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CHO (c) CH<sub>3</sub>CH<sub>2</sub>COCH<sub>2</sub>CH<sub>3</sub>",
         "a": "(a) <b>2,4-dimethyl-3-pentanone</b> (FGOB 15.2) (b) <b>butanal</b> (butyraldehyde) (c) <b>3-pentanone</b> (Ball 14.E).",
         "notes": "FGOB 15.2 Example b; Ball 14.E."})
    add({"t": "table", "sec": 3, "lo": LO5, "title": "Properties: between ethers and alcohols",
         "head": ["Compound", "Family", "Molar mass", "Forces", "bp (°C)"],
         "rows": [["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>", "alkane", "58", "dispersion only", "−1"],
                  ["CH<sub>3</sub>OCH<sub>2</sub>CH<sub>3</sub>", "ether", "60", "weak dipole", "6"],
                  ["CH<sub>3</sub>CH<sub>2</sub>CHO", "aldehyde", "58", "strong dipole", "49"],
                  ["CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH", "alcohol", "60", "hydrogen bonding", "97"]],
         "widths": [3.2, 1.6, 1.6, 2.4, 1.2],
         "caption": "The C=O oxygen accepts H-bonds from water, so formaldehyde, acetaldehyde and acetone dissolve in water; solubility ends at about 4 carbons per O. Source: FGOB Table 15.3.1.",
         "notes": "FGOB 15.3."})
    add({"t": "table", "sec": 3, "lo": LO5, "title": "Common aldehydes and ketones",
         "head": ["Compound", "Structure", "Where you meet it"],
         "rows": [["formaldehyde", mini("C=O", hs=True), "<b>formalin</b> (37–40% solution) preserves specimens: it denatures proteins"],
                  ["acetone", mini("CC(C)=O"), "solvent; nail-polish remover. Its smell on the breath signals <b>uncontrolled diabetes</b> (ketoacidosis)"],
                  ["vanillin", mini("COc1cc(C=O)ccc1O"), "vanilla flavouring in syrups and foods"],
                  ["cinnamaldehyde", mini("O=C/C=C/c1ccccc1"), "oil of cinnamon"],
                  ["progesterone, testosterone", "steroid hormones", "contain ketone groups (Chapter 6)"]],
         "widths": [2.4, 2.2, 5.2],
         "caption": "Source: FGOB 15.4.",
         "notes": "FGOB 15.4."})
    add({"t": "table", "sec": 3, "lo": LO5, "title": "Oxidation: telling aldehydes from ketones",
         "head": ["Test", "Reagent", "Aldehyde", "Ketone"],
         "rows": [["<b>Tollens'</b>", "Ag<sup>+</sup> in ammonia (colourless)", "<b>silver mirror</b> (Ag) forms", "no change"],
                  ["<b>Benedict's</b>", "Cu<sup>2+</sup> in alkaline citrate (<b>blue</b>)", "<b>brick-red</b> precipitate (Cu<sub>2</sub>O)", "stays blue"],
                  ["<b>Acidified dichromate</b>", "Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> (orange)", "turns green → carboxylic acid", "stays orange"]],
         "widths": [2.0, 3.2, 3.0, 1.6],
         "caption": "Aldehydes are oxidised to <b>carboxylic acids</b> very easily (even by air); ketones resist oxidation. Benedict's test detects <b>reducing sugars</b> such as glucose (Chapter 5), and was once used to test urine in diabetes.",
         "notes": "Tollens': FGOB 15.3, 15.5; Benedict's (aromatic aldehydes react poorly with Benedict's) and dichromate rows original."})
    add({"t": "figure", "pos": "top", "sec": 3, "lo": LO5, "title": "Reduction: back to alcohols",
         "fig": {"cap": "Reduction adds H<sub>2</sub> across the C=O.",
                 "data": stack([scheme([('m', 'CCC=O', 'propanal', 140), ('>', 'H₂, Ni (or NaBH₄)', ''), ('m', 'CCCO', '1-propanol (1°)', 150)], h=95),
                                scheme([('m', 'CC(C)=O', 'propanone', 140), ('>', 'H₂, Ni (or NaBH₄)', ''), ('m', 'CC(C)O', '2-propanol (2°)', 150)], h=95)], w=560, row_h=120)},
         "items": ["Aldehyde → <b>1° alcohol</b>; ketone → <b>2° alcohol</b>. Reduction is the reverse of the oxidation in 3.1.",
                   "Oxidation–reduction pairs: 1° alcohol ⇌ aldehyde; 2° alcohol ⇌ ketone.",
                   "Aldehydes also react with alcohols to form <b>hemiacetals</b>: this is how glucose closes into a ring (Chapter 5)."],
         "notes": "Original (FGOB 15.6 and 15.7 are empty placeholders)."})
    add({"t": "check", "sec": 3, "lo": LO5, "title": "Quick check",
         "q": "A compound gives a silver mirror with Tollens' reagent. It is most likely:",
         "opts": ["acetone", "propanal", "2-propanol", "diethyl ether"], "ans": 1,
         "why": "Only aldehydes are oxidised by the mild Tollens' reagent.", "notes": "Answer B."})
    add({"t": "check", "sec": 3, "lo": LO5, "title": "Quick check",
         "q": "Which alcohol is oxidised to cyclohexanone?",
         "opts": ["cyclohexanol", "cyclohexene", "1-hexanol", "phenol"], "ans": 0,
         "why": "Cyclohexanol is a 2° alcohol, so it oxidises to a ketone (Ball 14.E).", "notes": "Answer A."})

    # ================= wrap-up =================
    add({"t": "summary", "title": "Summary: key ideas", "rows": [
        ["Alcohols", "R–OH; 1°/2°/3° by carbons on C–OH; -ol; H-bonds → high bp, small ones water-soluble"],
        ["SN2", "one step, backside attack; 1°; rate ∝ [R–X][Nu]; inversion"],
        ["SN1", "two steps via carbocation; 3°; rate ∝ [R–X]; mixture of forms"],
        ["Elimination", "alcohol + conc. H<sub>2</sub>SO<sub>4</sub>, 180 °C → alkene; haloalkane + hot ethanolic KOH → alkene"],
        ["Oxidation", "1° → aldehyde → acid; 2° → ketone; 3° → none (dichromate orange → green)"],
        ["Phenols", "ArOH; weakly acidic; antiseptics"],
        ["Ethers &amp; thiols", "R–O–R′ low bp, anaesthetics; R–SH smelly, oxidise to –S–S– bridges"],
        ["Aldehydes &amp; ketones", "-al/-one; polar C=O; aldehydes give Tollens' and Benedict's; reduce back to alcohols"]],
         "notes": "One line per idea."})
    add({"t": "close", "title": "Before the next chapter",
         "items": ["Complete the after-class activity (about 30 min)", "Attempt the Chapter 3 tutorial",
                   "Play the Chapter 3 game to find your weak outcomes", "Next chapter: Carboxylic Acid, Ester, Amines, Amide"],
         "attrib": "Adapted from LibreTexts (Ball, Hill &amp; Scott; FGOB), CC BY-NC-SA 3.0. SN1/SN2, substitution vs elimination, the colour tests, carbonyl reduction and pharmacy links are original material by Dr. NAM.",
         "notes": "Full attribution: " + META["attrib"]})
    return S


def sn2_svg():
    """Hand-drawn SN2 mechanism: curly arrows, transition state, inversion (umbrella flip)."""
    import base64
    W, H = 980, 250
    t = lambda x, y, s, size=22, col='#1B2A41', w='600', anchor='middle': f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{col}" text-anchor="{anchor}" font-family="sans-serif">{s}</text>'
    ln = lambda x1, y1, x2, y2, dash='', col='#1B2A41', wd=2.5: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{wd}" {"stroke-dasharray=" + chr(34) + dash + chr(34) if dash else ""}/>'
    wedge = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1} L{x2-4} {y2-3} L{x2+4} {y2+3} Z" fill="#1B2A41"/>'
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>',
         '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#C2456A"/></marker></defs>']
    # reactants
    o += [t(60, 128, 'HO', 24), t(92, 116, '−', 18, '#C2456A'), t(78, 100, '··', 20)]
    cx, cy = 200, 120
    o += [t(cx, cy + 8, 'C', 26), ln(cx + 14, cy, cx + 70, cy), t(cx + 92, cy + 8, 'Br', 24, '#8B4A12'),
          ln(cx - 4, cy - 14, cx - 26, cy - 52), t(cx - 34, cy - 58, 'H', 20),
          wedge(cx - 6, cy + 12, cx - 30, cy + 50), t(cx - 40, cy + 70, 'H', 20),
          ln(cx + 4, cy + 14, cx + 22, cy + 52, '4 3'), t(cx + 30, cy + 74, 'CH₃', 18)]
    o.append(f'<path d="M84 104 C110 60 160 70 186 104" fill="none" stroke="#C2456A" stroke-width="2.5" marker-end="url(#ah)"/>')
    o.append(f'<path d="M248 112 C258 82 282 82 294 104" fill="none" stroke="#C2456A" stroke-width="2.5" marker-end="url(#ah)"/>')
    o.append(f'<line x1="340" y1="120" x2="390" y2="120" stroke="#1B2A41" stroke-width="2.5"/><path d="M388 113 L400 120 L388 127 Z" fill="#1B2A41"/>')
    # transition state
    tx, ty = 560, 120
    o += [t(tx - 100, ty + 8, 'HO', 22), ln(tx - 72, ty, tx - 18, ty, '6 5'), t(tx, ty + 8, 'C', 26), ln(tx + 18, ty, tx + 72, ty, '6 5'), t(tx + 96, ty + 8, 'Br', 22, '#8B4A12'),
          ln(tx, ty - 16, tx, ty - 56), t(tx, ty - 62, 'H', 20), ln(tx - 6, ty + 14, tx - 30, ty + 52), t(tx - 38, ty + 72, 'H', 20), ln(tx + 6, ty + 14, tx + 30, ty + 52), t(tx + 40, ty + 72, 'CH₃', 18),
          t(tx - 100, ty - 22, 'δ−', 16, '#C2456A', '400'), t(tx + 96, ty - 22, 'δ−', 16, '#C2456A', '400'), t(tx + 168, ty - 52, '‡', 26)]
    o.append(f'<path d="M{tx-136} 40 L{tx-146} 40 L{tx-146} 200 L{tx-136} 200" fill="none" stroke="#56657A" stroke-width="2"/><path d="M{tx+142} 40 L{tx+152} 40 L{tx+152} 200 L{tx+142} 200" fill="none" stroke="#56657A" stroke-width="2"/>')
    o.append(t(tx, 232, 'transition state: C–O forming as C–Br breaks', 15, '#56657A', '400'))
    o.append(f'<line x1="730" y1="120" x2="780" y2="120" stroke="#1B2A41" stroke-width="2.5"/><path d="M778 113 L790 120 L778 127 Z" fill="#1B2A41"/>')
    # product (inverted)
    px, py = 880, 120
    o += [t(px - 66, py + 8, 'HO', 24), ln(px - 44, py, px - 14, py), t(px, py + 8, 'C', 26),
          ln(px + 4, py - 14, px + 26, py - 52), t(px + 34, py - 58, 'H', 20),
          wedge(px + 6, py + 12, px + 30, py + 50), t(px + 40, py + 70, 'H', 20),
          ln(px - 4, py + 14, px - 22, py + 52, '4 3'), t(px - 30, py + 74, 'CH₃', 18), t(px + 60, py + 8, '+ Br⁻', 20, '#8B4A12')]
    o.append(t(200, 232, 'nucleophile attacks from the back', 15, '#56657A', '400'))
    o.append(t(870, 232, 'groups flipped (inversion)', 15, '#56657A', '400'))
    o.append('</svg>')
    return 'data:image/svg+xml;base64,' + base64.b64encode(''.join(o).encode()).decode()
