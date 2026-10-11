"""PHD125 Chapter 2 · activities: before class, after class, tutorial.
Items marked (Ball 12.E) adapt Dr. NAM's ALKANE EXERCISE file; (FGOB 13.x) adapt the supplied FGOB PDF; others are original."""
from figs import mol, scheme

TITLE = 'Saturated and Unsaturated Hydrocarbons'
ATTRIB = ("Adapted from LibreTexts <i>Introduction to Organic Chemistry – Alkanes</i> 12.3, 12.6–12.10 and exercises 12.E (Sharpe Elles, from Ball, Hill &amp; Scott), "
          "<i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 13 and <i>Fundamentals of General Organic and Biological Chemistry</i> 13.1–13.9, CC BY-NC-SA 3.0. "
          "Reaction mechanisms, Markovnikov items and pharmacy scenarios are original material by Dr. NAM. Shared under CC BY-NC-SA for non-commercial teaching.")


def img(smi, w=300, h=140, **k):
    return f'<img src="{mol(smi, w, h, **k)}" alt="structure" style="display:block;max-width:100%;height:auto;background:#fff;border-radius:10px;margin:8px 0">'


def rx(parts, h=110):
    return f'<img src="{scheme(parts, h=h)}" alt="reaction" style="display:block;max-width:100%;height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch2", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH2_PreLecture.pdf",
    "title": "Before class: chains, names and double bonds",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 2 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "Saturated and unsaturated",
             "html": "<p><b>Alkanes</b> have only single C–C bonds: every carbon holds as many hydrogens as it can, so they are <b>saturated</b>. <b>Alkenes</b> (C=C) and <b>alkynes</b> (C≡C) have fewer hydrogens: they are <b>unsaturated</b>. <b>Benzene</b> is a special ring of six carbons called an <b>aromatic</b> compound.</p>"},
            {"type": "read", "h": "Names come from counting carbons",
             "html": "<p>The first four stems are worth learning by heart: <b>meth</b>- (1 C), <b>eth</b>- (2), <b>prop</b>- (3), <b>but</b>- (4). Then pent-, hex-, hept-, oct-, non-, dec- (5 to 10). The ending tells the family: <b>-ane</b> (alkane), <b>-ene</b> (alkene), <b>-yne</b> (alkyne). So propane, propene and propyne all have three carbons.</p>"},
            {"type": "read", "h": "Why this matters in pharmacy",
             "html": "<p>Petroleum jelly and liquid paraffin are alkanes. IV bags and syringes are made from alkene polymers. Many drugs contain a benzene ring. And the gas cylinder in your kitchen holds propane and butane.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: Chapter 1 recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "How many bonds does each carbon form in a neutral organic molecule?", "opts": ["2", "3", "4", "6"], "ans": 2, "why": "Carbon is tetravalent."},
            {"type": "fill", "lo": "Recap", "q": "How many hydrogen atoms are on a carbon at the end of a zig-zag line (no other atom written)?", "acc": ["3", "three"], "ph": "a number", "why": "One bond to carbon, so 3 H: a CH<sub>3</sub> group."},
            {"type": "mcq", "lo": "Recap", "q": "What is the shape around a carbon with a C=C double bond?", "opts": ["tetrahedral, 109.5°", "trigonal planar, 120°", "linear, 180°", "bent, 104.5°"], "ans": 1, "why": "Three electron groups."},
            {"type": "mcq", "lo": "Recap", "q": "Which intermolecular force holds alkane molecules together?", "opts": ["hydrogen bonds", "ionic bonds", "dispersion (London) forces", "covalent bonds"], "ans": 2, "why": "Alkanes are nonpolar, so only dispersion forces act between them."},
            {"type": "match", "lo": "CH2-LO1", "q": "Match each stem to its number of carbons.", "left": ["meth-", "eth-", "prop-", "but-", "pent-"], "right": ["1", "2", "3", "4", "5", "6"], "ans": [0, 1, 2, 3, 4], "why": "Learn the first ten stems: they are used for every family."},
            {"type": "fill", "lo": "CH2-LO1", "q": "Alkanes have the general formula C<sub>n</sub>H<sub>2n+2</sub>. How many H atoms are in an alkane with 6 carbons?", "acc": ["14"], "ph": "a number", "why": "2(6) + 2 = 14: hexane, C<sub>6</sub>H<sub>14</sub>."},
            {"type": "mcq", "lo": "CH2-LO4", "q": "Which name belongs to an alkene?", "opts": ["propane", "propene", "propyne", "propanol"], "ans": 1, "why": "-ene means a C=C double bond."},
            {"type": "tf", "lo": "CH2-LO2", "q": "Oil floats on water because alkanes are nonpolar and less dense than water.", "ans": True, "why": "Most liquid alkanes have densities of about 0.6–0.7 g/mL."},
            {"type": "mcq", "lo": "CH2-LO3", "q": "What are the products of the complete combustion of an alkane?", "opts": ["CO and H<sub>2</sub>", "CO<sub>2</sub> and H<sub>2</sub>O", "C and H<sub>2</sub>O", "CH<sub>4</sub> and O<sub>2</sub>"], "ans": 1, "why": "With plenty of oxygen, alkanes burn to carbon dioxide and water."},
            {"type": "self", "lo": "CH2-LO5", "q": "Margarine is made by adding hydrogen to vegetable oil. Guess what happens to the C=C bonds in the oil.", "model": "Hydrogen adds across the C=C double bonds, turning them into C–C single bonds (hydrogenation). The oil becomes more saturated and more solid. You will meet this addition reaction in 2.2."}]}]}

POST = {
    "topic": "ch2", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH2_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the two subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH2-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "2.1 · Alkanes: structure and names", "items": [
            {"type": "fill", "lo": "CH2-LO1", "q": "What is the molecular formula of the member of the alkane series just above C<sub>8</sub>H<sub>18</sub>? Type it on one line, e.g. C4H10. (Ball 12.E)", "acc": ["C9H20"], "cs": True, "show": "C<sub>9</sub>H<sub>20</sub>", "ph": "e.g. C4H10", "why": "Add one CH<sub>2</sub>: C<sub>9</sub>H<sub>20</sub> (nonane)."},
            {"type": "mcq", "lo": "CH2-LO1", "q": "Name this compound." + img('CCC(C)CCC', 260, 110), "opts": ["3-methylhexane", "4-methylhexane", "2-ethylpentane", "heptane"], "ans": 0, "why": "Longest chain 6 C; number from the end nearer the branch: C3. (Ball 12.E 6a)"},
            {"type": "mcq", "lo": "CH2-LO1", "q": "Name CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub>.", "opts": ["2,5-dimethylheptane", "3,6-dimethylheptane", "2,5-methylheptane", "2-methyl-5-methylheptane"], "ans": 0, "why": "7-carbon chain; numbering from the left gives 2 and 5 (from the right, 3 and 6). Use di- for two methyls. (Ball 12.E 6b)"},
            {"type": "mcq", "lo": "CH2-LO1", "q": "Which name is <b>incorrect</b>?", "opts": ["2-ethylbutane", "3-methylpentane", "2,2-dimethylpropane", "2-methylbutane"], "ans": 0, "why": "In \"2-ethylbutane\" the ethyl extends the chain to five carbons: the correct name is 3-methylpentane."},
            {"type": "num", "lo": "CH2-LO1", "q": "How many carbon atoms are in 3-ethyl-2-methylheptane? (Ball 12.E)", "ans": 10, "tol": 0, "unit": "C", "why": "7 (heptane) + 2 (ethyl) + 1 (methyl) = 10."},
            {"type": "tf", "lo": "CH2-LO1", "q": "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> and a bent drawing of the same four-carbon chain are isomers.", "ans": False, "why": "Bending is rotation about C–C bonds: same compound (Ball 12.E 5a)."},
            {"type": "match", "lo": "CH2-LO1", "q": "Match each cycloalkane to its formula.", "left": ["cyclopropane", "cyclopentane", "methylcyclohexane"], "right": ["C<sub>3</sub>H<sub>6</sub>", "C<sub>5</sub>H<sub>10</sub>", "C<sub>7</sub>H<sub>14</sub>", "C<sub>6</sub>H<sub>14</sub>"], "ans": [0, 1, 2], "why": "Cycloalkanes are C<sub>n</sub>H<sub>2n</sub>. C<sub>6</sub>H<sub>14</sub> is hexane, an open chain."}]},
        {"h": "2.1 · Alkanes: properties and reactions", "items": [
            {"type": "mcq", "lo": "CH2-LO2", "q": "25 mL of hexane is added to 100 mL of water. What happens? (Ball 12.E)", "opts": ["Hexane dissolves", "Hexane does not dissolve and floats on top", "Hexane does not dissolve and sinks", "The two react"], "ans": 1, "why": "Hexane is nonpolar (insoluble) and less dense than water (0.66 g/mL)."},
            {"type": "match", "lo": "CH2-LO2", "q": "Which member of each pair has the higher boiling point? (Ball 12.E)", "left": ["pentane or butane", "heptane or nonane", "pentane or 2,2-dimethylpropane"], "right": ["first", "second"], "ans": [0, 1, 0], "why": "Longer chains boil higher; branching lowers the boiling point."},
            {"type": "fill", "lo": "CH2-LO3", "q": "Balance: C<sub>4</sub>H<sub>10</sub> + __ O<sub>2</sub> → 4 CO<sub>2</sub> + 5 H<sub>2</sub>O. Give the coefficient of O<sub>2</sub> as a number or fraction.", "acc": ["6.5", "13/2", "6 1/2"], "ph": "e.g. 3.5", "why": "O atoms on the right: 8 + 5 = 13, so 13/2 O<sub>2</sub>. Doubled: 2 C<sub>4</sub>H<sub>10</sub> + 13 O<sub>2</sub> → 8 CO<sub>2</sub> + 10 H<sub>2</sub>O."},
            {"type": "mcq", "lo": "CH2-LO3", "q": "Methane and chlorine are mixed and kept in the dark at room temperature. What happens?", "opts": ["CH<sub>3</sub>Cl forms quickly", "Nothing: UV light or heat is needed", "An explosion", "CCl<sub>4</sub> forms"], "ans": 1, "why": "Halogenation needs UV light or high temperature to split Cl<sub>2</sub> into radicals."},
            {"type": "match", "lo": "CH2-LO3", "q": "Match each step to its stage in the chlorination of methane.", "left": ["Cl<sub>2</sub> → 2 Cl•", "Cl• + CH<sub>4</sub> → •CH<sub>3</sub> + HCl", "•CH<sub>3</sub> + Cl• → CH<sub>3</sub>Cl"], "right": ["initiation", "propagation", "termination"], "ans": [0, 1, 2], "why": "Initiation makes radicals; propagation keeps the chain going; termination removes radicals."},
            {"type": "mcq", "lo": "CH2-LO3", "q": "Which halogen reacts least readily with alkanes? (Ball 12.E)", "opts": ["F<sub>2</sub>", "Cl<sub>2</sub>", "Br<sub>2</sub>", "I<sub>2</sub>"], "ans": 3, "why": "F<sub>2</sub> reacts explosively; I<sub>2</sub> is too unreactive."}]},
        {"h": "2.2 · Alkenes, alkynes and aromatics", "items": [
            {"type": "mcq", "lo": "CH2-LO4", "q": "Name CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH=CHCH<sub>3</sub>. (FGOB 13.2)", "opts": ["2-octene", "6-octene", "2-heptene", "octane"], "ans": 0, "why": "8-carbon chain; number from the right so the C=C starts at C2."},
            {"type": "mcq", "lo": "CH2-LO4", "q": "Which can exist as cis-trans isomers?", "opts": ["CH<sub>2</sub>=CHCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>", "CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub>", "(CH<sub>3</sub>)<sub>2</sub>C=CHCH<sub>3</sub>", "CH<sub>2</sub>=CH<sub>2</sub>"], "ans": 1, "why": "Each C=C carbon needs two different groups. 2-Pentene has H and CH<sub>3</sub> on one, H and C<sub>2</sub>H<sub>5</sub> on the other. (FGOB 13.3)"},
            {"type": "mcq", "lo": "CH2-LO4", "q": "Which carbon in CH<sub>3</sub>CH(Cl)CH<sub>2</sub>CH<sub>3</sub> is chiral?", "opts": ["C1", "C2", "C3", "none"], "ans": 1, "why": "C2 carries H, Cl, CH<sub>3</sub> and CH<sub>2</sub>CH<sub>3</sub>: four different groups."},
            {"type": "match", "lo": "CH2-LO5", "q": "Match each reagent with the product it gives with propene, CH<sub>2</sub>=CHCH<sub>3</sub>.", "left": ["H<sub>2</sub>, Ni", "Br<sub>2</sub>", "HBr", "H<sub>2</sub>O, H<sub>2</sub>SO<sub>4</sub>"], "right": ["propane", "1,2-dibromopropane", "2-bromopropane", "2-propanol", "1-propanol"], "ans": [0, 1, 2, 3], "why": "HBr and H<sub>2</sub>O follow Markovnikov's rule; 1-propanol is the minor product."},
            {"type": "mcq", "lo": "CH2-LO5", "q": "A few drops of red-brown bromine are added to two liquids. Liquid X stays red-brown; liquid Y turns colourless at once. Which is most likely?", "opts": ["X is cyclohexene, Y is hexane", "X is hexane, Y is cyclohexene", "Both are alkenes", "Both are alkanes"], "ans": 1, "why": "Alkenes add Br<sub>2</sub> and decolourise it; alkanes do not react in the dark."},
            {"type": "mcq", "lo": "CH2-LO5", "q": "Which monomer makes PVC, used for IV fluid bags?", "opts": ["CH<sub>2</sub>=CH<sub>2</sub>", "CH<sub>2</sub>=CHCH<sub>3</sub>", "CH<sub>2</sub>=CHCl", "CF<sub>2</sub>=CF<sub>2</sub>"], "ans": 2, "why": "Vinyl chloride (chloroethene) → polyvinyl chloride. (FGOB 13.7)"},
            {"type": "mcq", "lo": "CH2-LO4", "q": "Name this compound." + img('Cc1ccc(Br)cc1', 220, 110), "opts": ["p-bromotoluene (4-bromotoluene)", "m-bromotoluene", "o-bromotoluene", "1-bromo-3-methylbenzene"], "ans": 0, "why": "Br is opposite (1,4) to the CH<sub>3</sub>: para. (FGOB 13.9)"},
            {"type": "mcq", "lo": "CH2-LO5", "q": "Benzene reacts with Br<sub>2</sub> only when FeBr<sub>3</sub> is present. The products are:", "opts": ["1,2-dibromocyclohexane", "bromobenzene + HBr", "bromocyclohexane", "no reaction ever"], "ans": 1, "why": "Benzene undergoes substitution, keeping its aromatic ring; HBr is the by-product."}]},
        {"h": "Pharmacy scenario · The ointment bench", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>In the compounding room, you prepare an ointment using white soft paraffin as the base. A colleague suggests replacing it with olive oil \"because it is natural\". Olive oil is mostly triglycerides of oleic acid, which contains a <b>cis</b> C=C double bond. The label on the paraffin says <i>store below 25 °C, keep away from flames</i>.</p>"},
            {"type": "mcq", "lo": "CH2-LO2", "q": "Why is white soft paraffin a good ointment base?", "opts": ["It dissolves in water and washes off easily", "It is a nonpolar, unreactive alkane mixture that forms a water-repelling layer on the skin", "It contains a benzene ring", "It is ionic"], "ans": 1, "why": "Alkanes are inert and nonpolar, so they protect the skin and do not react with most drugs."},
            {"type": "mcq", "lo": "CH2-LO5", "q": "Olive oil slowly goes rancid in air; paraffin does not. Which structural feature explains this?", "opts": ["Olive oil's C=C double bonds can react (for example with oxygen)", "Paraffin has more double bonds", "Olive oil is an alkane", "Paraffin is aromatic"], "ans": 0, "why": "Unsaturated C=C bonds are reactive sites. Saturated alkanes have none."},
            {"type": "self", "lo": "CH2-LO3", "q": "Why does the paraffin label say \"keep away from flames\"? Write the type of reaction and its products.", "model": "Alkanes are flammable: they undergo combustion. With enough oxygen: CO<sub>2</sub> + H<sub>2</sub>O + heat; with limited oxygen: CO and soot too."}]}]}

TUT = {
    "topic": "ch2", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH2_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (34 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 46.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 2 game, or move on to Chapter 3.",
    "sections": []}
T = TITLE
A = [
    ("CH2-LO1", "The general formula of an alkane is:", ["C<sub>n</sub>H<sub>2n</sub>", "C<sub>n</sub>H<sub>2n+2</sub>", "C<sub>n</sub>H<sub>2n−2</sub>", "C<sub>n</sub>H<sub>n</sub>"], 1, "Saturated open chains: C<sub>n</sub>H<sub>2n+2</sub>."),
    ("CH2-LO1", "The IUPAC name of (CH<sub>3</sub>)<sub>3</sub>CCH<sub>2</sub>C(CH<sub>3</sub>)<sub>3</sub> is: (Ball 12.E)", ["2,2,4,4-tetramethylpentane", "2,4-dimethylpentane", "1,1,3,3-tetramethylpentane", "nonane"], 0, "Five-carbon chain with two methyls on C2 and two on C4."),
    ("CH2-LO1", "Which compound is an isomer of hexane?", ["2-methylpentane", "cyclohexane", "2-methylhexane", "hexene"], 0, "2-Methylpentane is C<sub>6</sub>H<sub>14</sub>, like hexane. Cyclohexane and hexene are C<sub>6</sub>H<sub>12</sub>."),
    ("CH2-LO2", "Which has the highest boiling point?", ["butane", "pentane", "2-methylbutane", "2,2-dimethylpropane"], 1, "Pentane: unbranched, so largest contact area among the C<sub>5</sub> isomers, and bigger than butane."),
    ("CH2-LO3", "Incomplete combustion of an alkane produces:", ["only CO<sub>2</sub> and H<sub>2</sub>O", "CO, soot and H<sub>2</sub>O", "an alkene", "a haloalkane"], 1, "Limited O<sub>2</sub> gives carbon monoxide and soot."),
    ("CH2-LO3", "In the free-radical chlorination of methane, the initiation step is:", ["Cl<sub>2</sub> → 2 Cl•", "Cl• + CH<sub>4</sub> → •CH<sub>3</sub> + HCl", "•CH<sub>3</sub> + Cl<sub>2</sub> → CH<sub>3</sub>Cl + Cl•", "2 •CH<sub>3</sub> → C<sub>2</sub>H<sub>6</sub>"], 0, "UV light splits Cl<sub>2</sub> homolytically."),
    ("CH2-LO4", "The correct IUPAC name of CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub> is:", ["3-pentene", "2-pentene", "2-pentyne", "pentane"], 1, "Number so the C=C gets the lower number."),
    ("CH2-LO4", "Which can show cis-trans isomerism?", ["1-butene", "2-methylpropene", "2-butene", "ethene"], 2, "Only 2-butene has two different groups on each double-bond carbon."),
    ("CH2-LO4", "A chiral carbon is bonded to:", ["two identical groups", "a double bond", "four different groups", "a benzene ring"], 2, "Four different groups give two non-superimposable mirror images."),
    ("CH2-LO5", "The major product of propene + HCl is:", ["1-chloropropane", "2-chloropropane", "1,2-dichloropropane", "propane"], 1, "Markovnikov: H to the CH<sub>2</sub> end, Cl to the middle carbon."),
    ("CH2-LO5", "Which reagent converts an alkene to an alkane?", ["H<sub>2</sub> with Ni", "Br<sub>2</sub>", "H<sub>2</sub>O with H<sub>2</sub>SO<sub>4</sub>", "HNO<sub>3</sub>"], 0, "Hydrogenation."),
    ("CH2-LO5", "Benzene typically undergoes:", ["addition with Br<sub>2</sub> at room temperature", "substitution, keeping its aromatic ring", "polymerisation", "no reactions at all"], 1, "Its delocalised ring is stable, so it substitutes rather than adds."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH2-LO1", "marks": 8, "level": "C3",
     "q": "(a) Draw the condensed structural formula of (i) 3-methylpentane, (ii) 2,2,5-trimethylhexane and (iii) 4-ethyl-3-methyloctane. (3 marks) (Ball 12.E) (b) Give the IUPAC name of each compound below. (3 marks)" + img('CC(C)CC(C)C', 240, 110) + img('CCC(CC)CCC', 240, 110) + img('CC1CCCC1', 160, 100) + "(c) A student names a compound \"2-ethylpentane\". Explain the mistake and give the correct name. (2 marks)",
     "hint": "In (b), find the longest chain first. In (c), follow the ethyl group: does it make the chain longer?",
     "work": "(a)(i) CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub> (ii) (CH<sub>3</sub>)<sub>3</sub>CCH<sub>2</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub> (iii) CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH(CH<sub>2</sub>CH<sub>3</sub>)CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>. (b) 2,4-dimethylpentane; 3-ethylhexane; methylcyclopentane. (c) The ethyl group on C2 extends the longest chain to six carbons, so the parent is hexane: the correct name is <b>3-methylhexane</b>.",
     "rubric": [["(a)(i) correct", 1], ["(a)(ii) correct", 1], ["(a)(iii) correct", 1], ["(b) 2,4-dimethylpentane", 1], ["(b) 3-ethylhexane", 1], ["(b) methylcyclopentane", 1], ["(c) Mistake: longest chain not used (ethyl extends it)", 1], ["(c) 3-methylhexane", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH2-LO2", "marks": 6, "level": "C4",
     "q": "Pentane (bp 36 °C) and 2,2-dimethylpropane (bp 9.5 °C) have the same molecular formula. (a) State the molecular formula and the relationship between them. (2 marks) (b) Explain the difference in boiling points. (2 marks) (c) Explain why both are insoluble in water but float on it. (2 marks)",
     "hint": "Think about molecular shape, contact area and the type of intermolecular force.",
     "work": "(a) C<sub>5</sub>H<sub>12</sub>; they are structural isomers. (b) Both have only dispersion forces. Pentane is unbranched, with a larger surface area and more contact between molecules, so its dispersion forces are stronger and more energy is needed to separate the molecules. 2,2-Dimethylpropane is compact and nearly spherical, so it has less contact. (c) Alkanes are nonpolar and cannot form hydrogen bonds with water, so they do not dissolve; their densities (about 0.6 g/mL) are lower than water's (1.0 g/mL), so they float.",
     "rubric": [["C<sub>5</sub>H<sub>12</sub>", 1], ["Structural isomers", 1], ["Dispersion forces only", 1], ["Branching reduces surface contact / weaker forces", 1], ["Nonpolar, so insoluble", 1], ["Less dense than water", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH2-LO3", "marks": 7, "level": "C3",
     "q": "(a) Write a balanced equation for the complete combustion of propane. (2 marks) (b) State one danger of incomplete combustion in a poorly ventilated room. (1 mark) (c) Methane reacts with chlorine in UV light. Write equations for the initiation step, the two propagation steps and one termination step. (4 marks)",
     "hint": "In (c), the radicals are Cl• and •CH<sub>3</sub>. Each propagation step uses one radical and makes another.",
     "work": "(a) C<sub>3</sub>H<sub>8</sub> + 5 O<sub>2</sub> → 3 CO<sub>2</sub> + 4 H<sub>2</sub>O. (b) Carbon monoxide forms; it binds to haemoglobin and stops oxygen transport (CO poisoning). (c) Initiation: Cl<sub>2</sub> → 2 Cl• (UV). Propagation: Cl• + CH<sub>4</sub> → •CH<sub>3</sub> + HCl; •CH<sub>3</sub> + Cl<sub>2</sub> → CH<sub>3</sub>Cl + Cl•. Termination (any one): Cl• + Cl• → Cl<sub>2</sub>; •CH<sub>3</sub> + Cl• → CH<sub>3</sub>Cl; •CH<sub>3</sub> + •CH<sub>3</sub> → C<sub>2</sub>H<sub>6</sub>.",
     "rubric": [["Correct formulas of reactants and products", 1], ["Balanced (1 : 5 : 3 : 4)", 1], ["CO poisoning stated", 1], ["Initiation", 1], ["Propagation 1", 1], ["Propagation 2", 1], ["Any valid termination", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH2-LO4", "marks": 6, "level": "C3",
     "q": "(a) Name: (i) CH<sub>3</sub>CH=C(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub> (ii) CH≡CCH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>3</sub> (2 marks) (b) Draw and name the cis and trans isomers of 2-pentene. (2 marks) (c) Explain why 1-pentene cannot show cis-trans isomerism. (1 mark) (d) Identify the chiral carbon in 2-butanol, CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>3</sub>, and explain why it is chiral. (1 mark)",
     "hint": "Number from the end nearer the multiple bond. For cis-trans, look at the groups on each double-bond carbon.",
     "work": "(a)(i) 3-methyl-2-pentene (ii) 4-methyl-1-pentyne. (b) cis-2-pentene: CH<sub>3</sub> and CH<sub>2</sub>CH<sub>3</sub> on the same side; trans-2-pentene: on opposite sides." + img('C/C=C\\CC', 200, 100) + img('C/C=C/CC', 200, 100) + "(c) C1 of 1-pentene carries two H atoms (two identical groups), so swapping sides gives the same molecule. (d) C2: it carries four different groups: H, OH, CH<sub>3</sub> and CH<sub>2</sub>CH<sub>3</sub>.",
     "rubric": [["3-methyl-2-pentene", 1], ["4-methyl-1-pentyne", 1], ["cis isomer drawn and named", 1], ["trans isomer drawn and named", 1], ["Two identical H on C1", 1], ["C2 with four different groups listed", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH2-LO5", "marks": 7, "level": "C4",
     "q": "Starting from propene, CH<sub>2</sub>=CHCH<sub>3</sub>: (a) give the structure and name of the major product with (i) H<sub>2</sub>/Ni, (ii) Br<sub>2</sub>, (iii) HBr, (iv) H<sub>2</sub>O/H<sub>2</sub>SO<sub>4</sub>. (4 marks) (b) State the rule used in (iii) and (iv). (1 mark) (c) Draw three repeating units of the polymer formed from propene and name it. (2 marks)",
     "hint": "Each reagent adds one part to each double-bond carbon. Which carbon already has more H atoms?",
     "work": "(a)(i) CH<sub>3</sub>CH<sub>2</sub>CH<sub>3</sub>, propane (ii) CH<sub>2</sub>BrCHBrCH<sub>3</sub>, 1,2-dibromopropane (iii) CH<sub>3</sub>CHBrCH<sub>3</sub>, 2-bromopropane (iv) CH<sub>3</sub>CH(OH)CH<sub>3</sub>, 2-propanol. (b) Markovnikov's rule: H adds to the double-bond carbon that already has more H atoms. (c) –CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH(CH<sub>3</sub>)–, polypropylene." + img('*CC(C)CC(C)CC(C)*', 320, 120),
     "rubric": [["(i) propane", 1], ["(ii) 1,2-dibromopropane", 1], ["(iii) 2-bromopropane", 1], ["(iv) 2-propanol", 1], ["Markovnikov's rule stated", 1], ["Correct repeating unit (CH<sub>3</sub> on alternate C)", 1], ["Named polypropylene", 1]]}]})
