"""Build a chapter's activity pages from the PHD115 activity engines.
Usage (repo root):  python3 -I _src/build_acts.py ch1
Reads _src/<ch>/activities.py (PRE, POST, TUT, ATTRIB) and _src/<ch>/game.py (config()),
writes <ch>/pre, <ch>/post, <ch>/tutorial and <ch>/game. Extras (x1-x3) define only TUT and the game."""
import json, re, sys, importlib, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_src'))
ch = sys.argv[1]
acts = importlib.import_module(f'{ch}.activities')
game = importlib.import_module(f'{ch}.game')
TPL = ROOT / '_src/templates'
from tiering import tier, CSS as TIER_CSS


def tier_all(data):
    # every question, worked solution and explanation: stem, then one row per part
    for sec in data.get('sections', []):
        for it in sec.get('items', []):
            for k in ('q', 'work', 'why'):
                if k in it:
                    it[k] = tier(it[k])
    return data
num = ch.upper()


def course(t):
    # rename the course in the engine only; applied BEFORE content is inserted
    return (t.replace('phd115', 'phd125').replace('PHD115', 'PHD125').replace('Fundamentals of Chemistry', 'Pharmaceutical Organic Chemistry')
             .replace('A periodic table and the answer key are at the back.', 'The answer key is at the back.'))


def write(folder, html):
    out = ROOT / ch / folder / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print(out.relative_to(ROOT), len(html))


for name, folder, label in [('PRE', 'pre', 'Before class'), ('POST', 'post', 'After class'), ('TUT', 'tutorial', 'Tutorial')]:
    data = getattr(acts, name, None)
    if not data:
        continue
    t = course((TPL / f'{folder}.html').read_text())
    i = t.index('const DATA=') + len('const DATA=')
    j = t.index(';\n', i)
    t = t[:i] + json.dumps(tier_all(data), ensure_ascii=False) + t[j:]
    t = t.replace('</style>', ':root{--tier-accent:var(--cold)}' + TIER_CSS + '\n</style>', 1)
    t = re.sub(r'<title>.*?</title>', f'<title>PHD125 · {num} · {label}</title>', t, count=1)
    write(folder, t)

# game
t = course((TPL / 'game.html').read_text())
i = t.index('NAMSHIFT.start(')
j = t.index('});\n</script>', i) + len('});\n')
cfg = game.config()
t = t[:i] + 'NAMSHIFT.start(' + json.dumps(cfg, ensure_ascii=False) + ');\n' + t[j:]
t = re.sub(r'<title>.*?</title>', f'<title>Game · {cfg["kicker"].split(" · ")[-1]} · PHD125 Study Hub</title>', t, count=1)
# footer credit line in the game page
t = re.sub(r'<p>Adapted from <i>The Basics of GOB Chemistry</i>.*?</p>', '<p>' + acts.ATTRIB + '</p>', t, count=1, flags=re.S)
t = re.sub(r'/\* Ionic & Covalent Compounds I content.*?\*/', f'/* {cfg["kicker"]} content for the Pharmacy Shift engine. */', t, count=1, flags=re.S)
write('game', t)
