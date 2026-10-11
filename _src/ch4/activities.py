"""PHD125 Chapter 4 · activities: before class, after class, tutorial.
(Ball 15.x) and (FGOB 16.x/17.x) items adapt those sources; drug and pharmacy items are original.
Tutorial weighting: about a quarter each for carboxylic acids, esters, amines and amides, plus one drug question."""
from figs import mol

TITLE = 'Carboxylic Acid, Ester, Amines, Amide'
ATTRIB = ("Adapted from <i>The Basics of GOB Chemistry</i> (Ball, Hill &amp; Scott) chapter 15, and <i>Fundamentals of General Organic and "
          "Biological Chemistry</i> 16.1–16.7 and 17.2–17.6, LibreTexts, CC BY-NC-SA 3.0. Drug questions and pharmacy scenarios are original "
          "material by Dr. NAM. Shared under CC BY-NC-SA for non-commercial teaching.")

PROCAINE = 'CCN(CC)CCOC(=O)c1ccc(N)cc1'
LIDOCAINE = 'CCN(CC)CC(=O)Nc1c(C)cccc1C'


def img(smi, w=260, h=120, **k):
    return f'<img src="{mol(smi, w, h, **k)}" alt="structure" style="display:block;max-width:100%;height:auto;background:#fff;border-radius:10px;margin:8px 0">'


PRE = {
    "topic": "ch4", "act": "pre", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH4_PreLecture.pdf",
    "title": "Before class: the organic acids and bases",
    "sub": "About 15 minutes. Read the three short cards, then try the readiness check. Wrong answers are fine: they show what to listen for in the lecture.",
    "how": "Read the cards first. Each question checks itself as soon as you answer. Press <b>Finish</b> at the end to see your score. You can reset and try again as often as you like.",
    "howPrint": "Read the cards first, then answer the questions without notes.",
    "attrib": ATTRIB, "next": "Next: open the Chapter 4 slides.",
    "sections": [
        {"h": "1 · Read first (5 min)", "items": [
            {"type": "read", "h": "Two parents",
             "html": "<p>A <b>carboxylic acid</b> has a –COOH group: a C=O and an –OH on the same carbon. Vinegar is acetic acid. An <b>amine</b> is ammonia (NH<sub>3</sub>) with carbon groups in place of H atoms. Acids give away H<sup>+</sup>; amines pick it up. They are the acids and bases of organic chemistry.</p>"},
            {"type": "read", "h": "Two children",
             "html": "<p>An acid can join to an <b>alcohol</b>, losing water, to make an <b>ester</b> (–COO–). It can join to an <b>amine</b>, also losing water, to make an <b>amide</b> (–CONH–). Esters smell of fruit; amides hold proteins together. Water can split both apart again: <b>hydrolysis</b>.</p>"},
            {"type": "read", "h": "Why a pharmacist cares",
             "html": "<p>Aspirin is an ester and an acid. Paracetamol is an amide. Most medicines that act on the brain and heart are amines, sold as <b>hydrochloride</b> salts so they dissolve in water. Knowing these four groups tells you how a drug dissolves, how it breaks down on the shelf, and how the body handles it.</p>"}]},
        {"h": "2 · Readiness check", "intro": "Ten quick questions: recap and a preview.", "items": [
            {"type": "mcq", "lo": "Recap", "q": "Oxidation of a primary alcohol with excess acidified dichromate gives:", "opts": ["a ketone", "a carboxylic acid", "an ether", "an alkene"], "ans": 1, "why": "1° alcohol → aldehyde → carboxylic acid (Chapter 3)."},
            {"type": "mcq", "lo": "Recap", "q": "Ammonia, NH<sub>3</sub>, acts as a base because it:", "opts": ["has a lone pair that accepts H<sup>+</sup>", "gives away H<sup>+</sup>", "contains oxygen", "is a gas"], "ans": 0, "why": "The lone pair on N accepts a proton to form NH<sub>4</sub><sup>+</sup>."},
            {"type": "mcq", "lo": "Recap", "q": "Which can form hydrogen bonds between its own molecules?", "opts": ["CH<sub>3</sub>CH<sub>2</sub>OH", "CH<sub>3</sub>OCH<sub>3</sub>", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>3</sub>", "CH<sub>3</sub>COCH<sub>3</sub>"], "ans": 0, "why": "It needs an O–H (or N–H) group."},
            {"type": "match", "lo": "CH4-LO1", "q": "Match each group to its family.", "left": ["–COOH", "–COOR′", "–NH<sub>2</sub>", "–CONH<sub>2</sub>"], "right": ["carboxylic acid", "ester", "amine", "amide", "ketone"], "ans": [0, 1, 2, 3], "why": "Ketone (R–CO–R′) is the extra option."},
            {"type": "fill", "lo": "CH4-LO1", "q": "What is the common name of CH<sub>3</sub>COOH, the acid in vinegar?", "acc": ["acetic acid", "ethanoic acid", "acetic", "ethanoic"], "ph": "name", "why": "Acetic acid (IUPAC: ethanoic acid)."},
            {"type": "tf", "lo": "CH4-LO2", "q": "Carboxylic acids are strong acids that ionise completely in water.", "ans": False, "why": "They are weak acids: only a small fraction ionises."},
            {"type": "mcq", "lo": "CH4-LO3", "q": "Which family gives bananas and pineapples their smell?", "opts": ["esters", "amines", "carboxylic acids", "amides"], "ans": 0, "why": "Isopentyl acetate (banana) and ethyl butyrate (pineapple)."},
            {"type": "mcq", "lo": "CH4-LO4", "q": "Which smell comes from amines?", "opts": ["rotting fish", "vinegar", "bananas", "nail-polish remover"], "ans": 0, "why": "Trimethylamine, putrescine and cadaverine."},
            {"type": "mcq", "lo": "CH4-LO5", "q": "Which drug contains an amide group?", "opts": ["paracetamol", "ethanol", "glycerol", "acetone"], "ans": 0, "why": "Paracetamol is N-(4-hydroxyphenyl)acetamide."},
            {"type": "self", "lo": "CH4-LO3", "q": "An old bottle of aspirin tablets smells of vinegar. Suggest what has happened.", "model": "Moisture has slowly split (hydrolysed) the ester group in aspirin, giving salicylic acid and acetic acid. Acetic acid is the vinegar smell. The tablets have degraded and should be discarded (4.2)."}]}]}

POST = {
    "topic": "ch4", "act": "post", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH4_PostLecture.pdf",
    "title": "After class: check your understanding",
    "sub": "About 30 minutes. Questions follow the four subchapters of the lecture and end with a pharmacy scenario.",
    "how": "Answer each question, then check it. At the end press <b>Finish</b> to see your score for each learning outcome (CH4-LO1 to LO5) and which ones to revise.",
    "howPrint": "Answer without notes first, then use the slides to check.",
    "attrib": ATTRIB, "next": "Next: try the tutorial.",
    "sections": [
        {"h": "4.1 · Carboxylic acids", "items": [
            {"type": "mcq", "lo": "CH4-LO1", "q": "Name this acid." + img('CC(C)CC(=O)O', 220, 110), "opts": ["3-methylbutanoic acid", "2-methylbutanoic acid", "3-methylpropanoic acid", "pentanoic acid"], "ans": 0, "why": "Four-carbon chain including the carboxyl carbon (C1); the methyl is on C3."},
            {"type": "match", "lo": "CH4-LO1", "q": "Match each common name to its IUPAC name.", "left": ["formic acid", "acetic acid", "propionic acid", "butyric acid"], "right": ["methanoic acid", "ethanoic acid", "propanoic acid", "butanoic acid", "pentanoic acid"], "ans": [0, 1, 2, 3], "why": "Pentanoic acid is valeric acid (Ball 15.1)."},
            {"type": "mcq", "lo": "CH4-LO2", "q": "Which is the strongest acid? (pK<sub>a</sub> in brackets)", "opts": ["chloroacetic acid (2.85)", "acetic acid (4.74)", "benzoic acid (4.19)", "formic acid (3.74)"], "ans": 0, "why": "Smallest pK<sub>a</sub> = strongest acid (FGOB 17.2)."},
            {"type": "fill", "lo": "CH4-LO2", "q": "Name the salt formed when propanoic acid reacts with sodium hydroxide.", "acc": ["sodium propanoate", "sodium propionate"], "ph": "salt name", "why": "Cation first; -ic acid → -ate."},
            {"type": "tf", "lo": "CH4-LO2", "q": "Acetic acid reacts with sodium bicarbonate to release carbon dioxide gas.", "ans": True, "why": "RCOOH + NaHCO<sub>3</sub> → RCOO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O + CO<sub>2</sub>."}]},
        {"h": "4.2 · Esters", "items": [
            {"type": "mcq", "lo": "CH4-LO3", "q": "Name CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>.", "opts": ["propyl ethanoate (propyl acetate)", "ethyl propanoate", "methyl butanoate", "propyl methanoate"], "ans": 0, "why": "Propyl on the O; acetate (2 C) acid part."},
            {"type": "mcq", "lo": "CH4-LO3", "q": "Which acid and alcohol make methyl butanoate (apple smell)?", "opts": ["butanoic acid + methanol", "methanoic acid + 1-butanol", "butanoic acid + ethanol", "propanoic acid + methanol"], "ans": 0, "why": "The alkyl on the O comes from the alcohol."},
            {"type": "match", "lo": "CH4-LO3", "q": "Give the products of ethyl acetate under each condition.", "left": ["water + acid catalyst, heat", "NaOH solution, heat"], "right": ["acetic acid + ethanol", "sodium acetate + ethanol", "acetamide + ethanol"], "ans": [0, 1], "why": "Acidic hydrolysis gives the acid; basic hydrolysis (saponification) gives the salt."},
            {"type": "tf", "lo": "CH4-LO3", "q": "Esters boil higher than carboxylic acids of the same molar mass.", "ans": False, "why": "Esters cannot hydrogen bond to each other; methyl acetate 57 °C vs propanoic acid 141 °C."}]},
        {"h": "4.3 · Amines", "items": [
            {"type": "match", "lo": "CH4-LO4", "q": "Classify each amine.", "left": ["CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>", "(CH<sub>3</sub>)<sub>2</sub>NH", "(CH<sub>3</sub>)<sub>3</sub>N", "(CH<sub>3</sub>)<sub>2</sub>CHNH<sub>2</sub>"], "right": ["1°", "2°", "3°"], "ans": [0, 1, 2, 0], "why": "Count the carbon groups on the nitrogen."},
            {"type": "fill", "lo": "CH4-LO4", "q": "Name CH<sub>3</sub>CH<sub>2</sub>NHCH<sub>2</sub>CH<sub>3</sub>.", "acc": ["diethylamine", "N-ethylethanamine", "n-ethylethanamine"], "ph": "name", "why": "Two ethyl groups on N (FGOB 16.2)."},
            {"type": "mcq", "lo": "CH4-LO4", "q": "Which has the highest boiling point? (all about 73–74 g/mol)", "opts": ["butyl alcohol", "butylamine", "diethylamine", "diethyl ether"], "ans": 0, "why": "O–H hydrogen bonds are stronger than N–H (FGOB 16.3)."},
            {"type": "mcq", "lo": "CH4-LO4", "q": "Many amine drugs are sold as hydrochlorides because the salt:", "opts": ["is ionic and water-soluble", "is a stronger drug", "is an ester", "evaporates more easily"], "ans": 0, "why": "Amine salts dissolve in water and are stable, odourless solids."},
            {"type": "mcq", "lo": "CH4-LO4", "q": "Alkaloids are extracted from plants with dilute acid because:", "opts": ["they are bases that form water-soluble salts", "they are acids", "acid destroys the plant", "they are esters"], "ans": 0, "why": "Adding base afterwards frees the alkaloid again (FGOB 16.7)."}]},
        {"h": "4.4 · Amides", "items": [
            {"type": "mcq", "lo": "CH4-LO5", "q": "Name CH<sub>3</sub>CH<sub>2</sub>CONH<sub>2</sub>.", "opts": ["propanamide", "propylamine", "propanoic acid", "ethanamide"], "ans": 0, "why": "-oic acid → -amide."},
            {"type": "mcq", "lo": "CH4-LO5", "q": "Acetic acid + methylamine, heated, gives:", "opts": ["N-methylacetamide + water", "methyl acetate + ammonia", "methylammonium acetate only, never an amide", "acetamide + methanol"], "ans": 0, "why": "The –OH of the acid and an H on N are lost as water (FGOB 17.3)."},
            {"type": "tf", "lo": "CH4-LO5", "q": "Amides are bases, like amines.", "ans": False, "why": "The N lone pair is drawn towards the C=O, so amide solutions are neutral (Ball 15.14)."},
            {"type": "match", "lo": "CH4-LO5", "q": "Give the products of hydrolysing butyramide under each condition.", "left": ["acid (H<sub>3</sub>O<sup>+</sup>), heat", "base (OH<sup>−</sup>), heat"], "right": ["butyric acid + NH<sub>4</sub><sup>+</sup>", "butyrate ion + NH<sub>3</sub>", "butanol + NH<sub>3</sub>"], "ans": [0, 1], "why": "In acid the ammonia is protonated; in base the acid is deprotonated (FGOB 17.4)."}]},
        {"h": "Pharmacy scenario · The medicine cabinet", "items": [
            {"type": "read", "h": "Scenario", "html": "<p>Puan Salmah brings in a bag from her late father's medicine cabinet: an old bottle of <b>aspirin</b> that smells of vinegar, a tube of <b>lidocaine hydrochloride</b> gel, and some <b>effervescent</b> vitamin C tablets that fizz in water. She asks which ones are still safe to use.</p>"},
            {"type": "mcq", "lo": "CH4-LO3", "q": "What has happened to the aspirin?", "opts": ["Its ester group has hydrolysed to salicylic acid and acetic acid", "It has oxidised to an aldehyde", "It has turned into an amide", "Nothing; the smell is normal"], "ans": 0, "why": "Moisture hydrolyses the ester; acetic acid is the vinegar smell."},
            {"type": "mcq", "lo": "CH4-LO2", "q": "The tablets fizz in water because:", "opts": ["an acid reacts with sodium bicarbonate to release CO<sub>2</sub>", "an ester is hydrolysed", "an amine is protonated", "the water boils"], "ans": 0, "why": "RCOOH + NaHCO<sub>3</sub> → RCOO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O + CO<sub>2</sub>."},
            {"type": "mcq", "lo": "CH4-LO4", "q": "Lidocaine is supplied as the hydrochloride because the salt forms at its:", "opts": ["amine nitrogen", "amide C=O", "benzene ring", "methyl groups"], "ans": 0, "why": "The 3° amine accepts H<sup>+</sup>; the amide nitrogen is not basic."},
            {"type": "self", "lo": "CH4-LO3", "q": "What would you advise Puan Salmah?", "model": "Do not use the aspirin: it has degraded by hydrolysis and may also be past its expiry date; return it to the pharmacy for safe disposal. Check the expiry dates of the lidocaine gel and the effervescent tablets and use them only if in date and stored properly. Store medicines in a cool, dry place, not a humid bathroom."}]}]}

TUT = {
    "topic": "ch4", "act": "tut", "topicTitle": TITLE, "pdf": "../../downloads/PHD125_CH4_Tutorial.pdf",
    "title": "Tutorial: exam-style practice",
    "sub": "Part A: 12 multiple-choice questions (1 mark each). Part B: 5 structured questions (38 marks). Same format as the final exam.",
    "how": "Part A marks itself. For Part B, write your full answer on paper first, then open <b>Worked solution and self-marking</b> and tick each marking step you earned. Use the hint only if you are stuck. Press <b>Finish</b> for your total out of 50.",
    "howPrint": "Answer Part A by circling one option. Answer Part B in full, showing your working.",
    "attrib": ATTRIB, "next": "Next: play the Chapter 4 game, or move on to Chapter 5.",
    "sections": []}
T = TITLE
A = [
    ("CH4-LO1", "The IUPAC name of CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH is:", ["butanoic acid", "propanoic acid", "butanal", "1-butanol"], 0, "Four carbons, including the carboxyl carbon."),
    ("CH4-LO1", "In the common name α-chlorobutyric acid, the Cl is on:", ["C2, the carbon next to –COOH", "C1, the carboxyl carbon", "C3", "C4"], 0, "Greek letters start next to the carboxyl carbon (Ball 15.1)."),
    ("CH4-LO2", "Which reaction of a carboxylic acid produces CO<sub>2</sub> gas?", ["with NaHCO<sub>3</sub>", "with NaOH", "with ethanol and H<sup>+</sup>", "with water"], 0, "Carbonates and bicarbonates release CO<sub>2</sub>."),
    ("CH4-LO3", "The ester formed from ethanoic acid and 1-propanol is:", ["propyl ethanoate", "ethyl propanoate", "propyl propanoate", "ethyl ethanoate"], 0, "Alcohol part (propyl) first, then the acid part (-ate)."),
    ("CH4-LO3", "Saponification is:", ["basic hydrolysis of an ester", "acidic hydrolysis of an amide", "the formation of an ester", "oxidation of an alcohol"], 0, "It gives a carboxylate salt (soap from fats)."),
    ("CH4-LO3", "Which is an ester of an inorganic acid used to relieve angina?", ["glyceryl trinitrate", "aspirin", "ethyl acetate", "methyl salicylate"], 0, "An ester of glycerol and nitric acid (FGOB 17.6)."),
    ("CH4-LO4", "(CH<sub>3</sub>CH<sub>2</sub>)<sub>3</sub>N is:", ["a tertiary amine", "a secondary amine", "a primary amine", "an amide"], 0, "Three ethyl groups on N."),
    ("CH4-LO4", "Methylamine reacts with HCl to form:", ["methylammonium chloride", "methyl chloride + NH<sub>3</sub>", "N-methylformamide", "chloromethane"], 0, "CH<sub>3</sub>NH<sub>2</sub> + HCl → CH<sub>3</sub>NH<sub>3</sub><sup>+</sup>Cl<sup>−</sup>."),
    ("CH4-LO4", "Tertiary amines boil lower than primary amines of the same molar mass because they:", ["have no N–H, so cannot hydrogen bond to each other", "are ionic", "are heavier", "contain oxygen"], 0, "Their boiling points are similar to ethers (FGOB 16.3)."),
    ("CH4-LO5", "The functional group in paracetamol that links the ring to the acetyl group is:", ["an amide", "an ester", "an amine", "a ketone"], 0, "N-(4-hydroxyphenyl)acetamide."),
    ("CH4-LO5", "Which cannot form an amide with acetic acid?", ["trimethylamine", "ammonia", "methylamine", "dimethylamine"], 0, "A 3° amine has no H on N; it only forms a salt (FGOB 17.3)."),
    ("CH4-LO5", "Nylon-66 is a:", ["polyamide made from a diacid and a diamine", "polyester made from a diacid and a diol", "addition polymer of ethene", "natural protein"], 0, "Adipic acid + hexanediamine (FGOB 17.5)."),
]
TUT["sections"].append({"h": "Part A · Multiple choice", "intro": "Choose one answer for each question.",
                        "items": [{"type": "mcq", "label": f"A{i+1}", "topic": T, "lo": lo, "q": q, "opts": o, "ans": a, "why": w} for i, (lo, q, o, a, w) in enumerate(A)]})
TUT["sections"].append({"h": "Part B · Structured questions", "intro": "Write your answers on paper, then self-mark with the worked solution.", "items": [
    {"type": "partb", "label": "B1", "topic": T, "lo": "CH4-LO2", "marks": 8, "level": "C3",
     "q": "(a) Give the IUPAC names of (i) (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>COOH (ii) BrCH<sub>2</sub>CH<sub>2</sub>COOH. (2 marks) (b) Acetic acid (60 g/mol) boils at 118 °C, but 1-propanol (60 g/mol) boils at 97 °C. Explain. (2 marks) (c) Chloroacetic acid has pK<sub>a</sub> 2.85 and acetic acid has pK<sub>a</sub> 4.74. State which is the stronger acid and explain why. (2 marks) (d) Write an equation for the reaction of benzoic acid with aqueous sodium bicarbonate and name the organic product. (2 marks)",
     "hint": "Number from the carboxyl carbon (C1). For (b), think about how many hydrogen bonds hold two acid molecules together. For (c), smaller pK<sub>a</sub> means what?",
     "work": "(a)(i) 3-methylbutanoic acid (ii) 3-bromopropanoic acid. (b) Both form hydrogen bonds, but two acid molecules are held together by two hydrogen bonds (a dimer), using both the C=O and the O–H, so more energy is needed to separate them. (c) Chloroacetic acid is stronger (smaller pK<sub>a</sub>): the electronegative Cl pulls electron density away and stabilises the carboxylate ion. (d) C<sub>6</sub>H<sub>5</sub>COOH + NaHCO<sub>3</sub> → C<sub>6</sub>H<sub>5</sub>COO<sup>−</sup>Na<sup>+</sup> + H<sub>2</sub>O + CO<sub>2</sub>; sodium benzoate.",
     "rubric": [["(i) 3-methylbutanoic acid", 1], ["(ii) 3-bromopropanoic acid", 1], ["Acids form hydrogen-bonded dimers (two H-bonds)", 1], ["More energy needed than for the alcohol", 1], ["Chloroacetic acid is stronger (smaller pK<sub>a</sub>)", 1], ["Cl withdraws electrons, stabilising the anion", 1], ["Correct balanced equation with CO<sub>2</sub>", 1], ["Sodium benzoate", 1]]},
    {"type": "partb", "label": "B2", "topic": T, "lo": "CH4-LO3", "marks": 8, "level": "C3",
     "q": "Ethyl butanoate gives pineapple flavour to syrups. (a) Write an equation for its preparation from a carboxylic acid and an alcohol, naming both reactants and stating the conditions. (3 marks) (b) Give two ways to increase the yield of the ester. (2 marks) (c) Write an equation for the hydrolysis of ethyl butanoate with sodium hydroxide and name both products. (3 marks)",
     "hint": "The part on the O comes from the alcohol. Esterification is reversible: think about Le Chatelier.",
     "work": "(a) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH + CH<sub>3</sub>CH<sub>2</sub>OH ⇌ CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O; butanoic acid and ethanol; heat with a little concentrated H<sub>2</sub>SO<sub>4</sub>. (b) Use excess ethanol; remove the water (or the ester) as it forms. (c) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub> + NaOH → CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COO<sup>−</sup>Na<sup>+</sup> + CH<sub>3</sub>CH<sub>2</sub>OH; sodium butanoate and ethanol.",
     "rubric": [["Butanoic acid and ethanol named", 1], ["Correct equation with water (reversible)", 1], ["Conc. H<sub>2</sub>SO<sub>4</sub> catalyst, heat", 1], ["Excess alcohol (or acid)", 1], ["Remove water or ester", 1], ["Correct equation", 1], ["Sodium butanoate", 1], ["Ethanol", 1]]},
    {"type": "partb", "label": "B3", "topic": T, "lo": "CH4-LO4", "marks": 8, "level": "C3",
     "q": "(a) Name and classify (1°, 2° or 3°) each amine: (i) CH<sub>3</sub>CH<sub>2</sub>NHCH<sub>3</sub> (ii) (CH<sub>3</sub>CH<sub>2</sub>)<sub>3</sub>N (iii) (CH<sub>3</sub>)<sub>2</sub>CHNH<sub>2</sub>. (3 marks) (b) Propylamine and trimethylamine are both C<sub>3</sub>H<sub>9</sub>N. Propylamine boils at 48 °C; trimethylamine boils at 3 °C. Explain. (2 marks) (c) Write an equation for the reaction of methylamine with hydrochloric acid and name the product. (2 marks) (d) Give one reason why amine drugs are formulated as hydrochloride salts. (1 mark)",
     "hint": "Count the carbon groups on N. Which of the two amines has an N–H bond?",
     "work": "(a)(i) ethylmethylamine, 2° (ii) triethylamine, 3° (iii) isopropylamine, 1°. (b) Propylamine (1°) has N–H bonds and forms hydrogen bonds between its molecules; trimethylamine (3°) has no H on N, so it cannot. (c) CH<sub>3</sub>NH<sub>2</sub> + HCl → CH<sub>3</sub>NH<sub>3</sub><sup>+</sup>Cl<sup>−</sup>; methylammonium chloride. (d) Any one: the salt is ionic and dissolves in water; it is a stable, odourless solid.",
     "rubric": [["(i) ethylmethylamine, 2°", 1], ["(ii) triethylamine, 3°", 1], ["(iii) isopropylamine, 1°", 1], ["Propylamine forms H-bonds (N–H)", 1], ["Trimethylamine has no N–H", 1], ["Correct equation", 1], ["Methylammonium chloride", 1], ["Water-soluble (or stable/odourless)", 1]]},
    {"type": "partb", "label": "B4", "topic": T, "lo": "CH4-LO5", "marks": 8, "level": "C3",
     "q": "(a) Write an equation for the reaction of acetic acid with ethylamine on heating, and name the organic product. (2 marks) (b) Acetamide melts at 82 °C, but is not basic, while ethylamine is a base. Explain both facts. (2 marks) (c) Give the products of hydrolysing propanamide (i) in acid (ii) in sodium hydroxide. (2 marks) (d) Explain why trimethylamine does not form an amide with acetic acid, and say what forms instead. (2 marks)",
     "hint": "Water is lost from the –OH of the acid and an H on the nitrogen. In an amide, where is the N lone pair?",
     "work": "(a) CH<sub>3</sub>COOH + CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub> → CH<sub>3</sub>CONHCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O; N-ethylacetamide (N-ethylethanamide). (b) Amide molecules form many hydrogen bonds (N–H···O=C), so acetamide is a solid with a high melting point. The N lone pair is pulled towards the C=O, so it does not accept H<sup>+</sup>; in ethylamine the lone pair is free. (c)(i) propanoic acid + ammonium ion (NH<sub>4</sub><sup>+</sup>) (ii) sodium propanoate + ammonia. (d) A 3° amine has no H on the nitrogen to lose with the –OH as water; an acid–base reaction gives the salt trimethylammonium acetate instead.",
     "rubric": [["Correct equation with water", 1], ["N-ethylacetamide (N-ethylethanamide)", 1], ["H-bonding network → high mp", 1], ["Lone pair delocalised towards C=O → not basic", 1], ["Acid: propanoic acid + NH<sub>4</sub><sup>+</sup>", 1], ["Base: propanoate salt + NH<sub>3</sub>", 1], ["No H on N in a 3° amine", 1], ["Forms a salt (trimethylammonium acetate)", 1]]},
    {"type": "partb", "label": "B5", "topic": T, "lo": "CH4-LO5", "marks": 6, "level": "C4",
     "q": "Procaine (top) and lidocaine (bottom) are local anaesthetics." + img(PROCAINE, 320, 120) + img(LIDOCAINE, 320, 120) + "(a) Identify the functional group that links the two halves of each molecule. (2 marks) (b) Procaine acts for a short time, lidocaine for longer. Explain using your answer to (a). (2 marks) (c) Both are injected as hydrochloride salts. Identify the group that forms the salt, and explain why the salt is used. (2 marks)",
     "hint": "Look at the atom next to the C=O in the middle of each molecule: O or N? Which of the two groups is hydrolysed more easily?",
     "work": "(a) Procaine: an ester (–COO–). Lidocaine: an amide (–CONH–). (b) Esters are hydrolysed quickly by esterase enzymes in the blood, so procaine is inactivated fast. Amides resist hydrolysis and are broken down slowly in the liver, so lidocaine lasts longer. (c) The tertiary amine group (the N with two ethyl groups) accepts H<sup>+</sup> from HCl. The salt is ionic, so it dissolves in water for an injection.",
     "rubric": [["Procaine: ester", 1], ["Lidocaine: amide", 1], ["Esters hydrolysed quickly by plasma esterases", 1], ["Amides resist hydrolysis → longer action", 1], ["Tertiary amine forms the salt", 1], ["Salt is ionic → water-soluble injection", 1]]}]})
