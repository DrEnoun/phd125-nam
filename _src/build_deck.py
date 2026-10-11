"""Build one chapter's slide deck from the PHD115 "Dr. NAM Science Decks" (v2) engine.
Usage (repo root):  python3 -I _src/build_deck.py ch1
Reads _src/<ch>/slides.py (META, build()) and writes <ch>/slides/index.html.
Changes from the PHD115 engine: AIMS chapter title on every slide, subchapter chip and dividers
("1.3 of 1.5"), deep links (#s3 jumps to subchapter 3), PHD125 storage keys, organic molecules in 3D."""
import json, re, sys, importlib, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_src'))
ch = sys.argv[1]
mod = importlib.import_module(f'{ch}.slides')
from figs import coords3d

t = (ROOT / '_src/templates/slides-v2.html').read_text()
# rename the course in the engine BEFORE inserting content, so content can still mention PHD115
t = t.replace('phd115', 'phd125').replace('PHD115', 'PHD125').replace('Fundamentals of Chemistry', 'Pharmaceutical Organic Chemistry')

# ---- swap content: the S array and META (keep the LOGO line from the template)
a = t.index('const S=[')
b = t.index('const META=')
b_end = t.index(';\n', b) + 2
S = mod.build()
META = dict(mod.META)
META.setdefault('hero', 'mol')
num = re.sub(r'\D', '', META['code'])
t = t[:a] + 'const S=' + json.dumps(S, ensure_ascii=False) + ';\n' + 'const META=' + json.dumps(META, ensure_ascii=False) + ';\n' + t[b_end:]


def sub(old, new, count=1):
    global t
    assert t.count(old) >= 1, ('missing', old[:80])
    t = t.replace(old, new) if count == 0 else t.replace(old, new, count)


# ---- page title, home link, storage keys
t = re.sub(r'<title>.*?</title>', f'<title>PHD125 · {META["chapter"]} · {META["title"]} · Slides</title>', t, count=1)
sub('href="../../#ic1"', f'href="../../#{ch}"')
sub("'phd125-ic1-deck-'", f"'phd125-{ch}-deck-'", 0)

# ---- chapter header on every slide; subchapter as a chip
sub("const foot=`<div class=\"foot\">PHD125 · ${META.short.replace(/&/g,'&amp;')} · <span>Dr. NAM</span> · Faculty of Pharmacy, UiTM Bertam, Penang</div>`;",
    "const foot=`<div class=\"foot\">PHD125 · ${META.chapter} · ${META.short.replace(/&/g,'&amp;')} · <span>Dr. NAM</span></div>`;\n"
    f"const CH='{num}';const CHAP=`${{META.chapter}} · ${{META.title}}`;")
sub("return `<div class=\"eyb\">${p?`<span class=\"eyebrow\">Part ${d.sec} · ${plain(p.title)}</span>`:`<span class=\"eyebrow\">${plain(META.title)}</span>`}",
    "return `<div class=\"eyb\"><span class=\"eyebrow\">${CHAP}</span>${p?`<span class=\"chip sub\">${CH}.${d.sec} ${plain(p.title)}</span>`:''}")
sub('aria-label="Lecture parts"', 'aria-label="Subchapters"')
sub('title="Part ${n}: ${plain(PARTS[n].title)}"', 'title="${CH}.${n} ${plain(PARTS[n].title)}"')
# dividers
sub('<div class="hero" style="top:104px;left:120px"><div class="divn">0${d.num}</div><div class="divp">PART ${d.num} OF ${Object.keys(PARTS).length}</div>',
    '<div class="hero" style="top:96px;left:120px"><span class="eyebrow">${CHAP}</span><div class="divn">${CH}.${d.num}</div><div class="divp">SUBCHAPTER ${d.num} OF ${Object.keys(PARTS).length}</div>')
# contents (lecture map)
sub('<span class="n">0${k}</span>', '<span class="n">${CH}.${k}</span>')
sub('<div class="k">0${k}</div>', '<div class="k">${CH}.${k}</div>')
sub('Go to Part ${k} →', 'Go to ${CH}.${k} →')
sub('Part buttons on the left: jump to a part', 'Number buttons on the left: jump to a subchapter')
# deep link to a subchapter: #s3
sub("const h=parseInt(location.hash.slice(1),10);cur=h?Math.min(h-1,slides.length-1):(+store.get('cur')||0);paint();",
    "const sm=location.hash.match(/^#s(\\d+)$/);const h=parseInt(location.hash.slice(1),10);"
    "cur=sm&&DIVIDX[sm[1]]!=null?DIVIDX[sm[1]]:(h?Math.min(h-1,slides.length-1):(+store.get('cur')||0));paint();")

# 3D molecules: fall back to this chapter's molecules, and shrink big molecules to fit their spot
sub("const m=SEC[d.sec||d.num]||['nacl','water'];", "const m=SEC[d.sec||d.num]||META.titlemol;")
sub("[m[2]||(m[0]==='nacl'?'water':'nacl'),1190,430,m[2]?30:26,.9]", "[m[2]||m[0],1190,430,30,.9]")
sub("g.scale.setScalar(sz);", "const at=MOL.DEF[n].atoms;const rr=Math.max(...at.map(q=>Math.hypot(q[1],q[2],q[3])));g.scale.setScalar(sz*Math.min(1,1.9/rr));")
# chip style for the subchapter tag
# divider: subchapter TITLE is the hero; the number becomes a small label above it
sub('</style>', '.divn{font:800 54px/1 var(--font-display)!important;letter-spacing:0!important;color:var(--title-accent)!important;text-shadow:none!important;margin-top:18px}'
    '.divt{font:800 118px/.95 var(--font-display)!important;letter-spacing:-3px!important;color:var(--spark-400)!important;max-width:820px!important;text-shadow:0 0 40px rgba(212,255,79,.3);text-wrap:balance}'
    '.divp{margin:6px 0 14px!important}\n</style>')
# shrink long divider titles so they fit (max 3 lines, about 330 px tall)
sub("function fitTitle(s){", "function fitDiv(s){const h=s.querySelector('.divt');if(!h||h.dataset.fit)return;let f=118;while((h.scrollHeight>300||h.scrollWidth>h.clientWidth+1)&&f>56){f-=6;h.style.setProperty('font-size',f+'px','important')}h.dataset.fit=1}\nfunction fitTitle(s){fitDiv(s);")
sub('</style>', '.chip.sub{background:rgba(212,255,58,.14);color:var(--spark-400);border:1px solid rgba(212,255,58,.45)}\n</style>')

# ---- 3D molecules: add organic molecules, and draw triple bonds
EXTRA = {
    'urea': 'NC(N)=O', 'ethane': 'CC', 'ethene': 'C=C', 'ethyne': 'C#C', 'butane': 'CCCC', 'propanol': 'CCCO',
    'cyclohexane': 'C1CCCCC1', 'aceticacid': 'CC(=O)O', 'aspirin': 'CC(=O)Oc1ccccc1C(=O)O',
    'paracetamol': 'CC(=O)Nc1ccc(O)cc1', 'methylpropane': 'CC(C)C', 'benzene': 'c1ccccc1', 'glycerol': 'OCC(O)CO', 'diethylether': 'CCOCC', 'ethanethiol': 'CCS', 'acetaldehyde': 'CC=O', 'formaldehyde': 'C=O', 'ascorbic': 'OC[C@H](O)[C@H]1OC(=O)C(O)=C1O',
}
extra = ''.join(f'    {k}: {json.dumps(coords3d(v))},\n' for k, v in EXTRA.items())
sub('    waterpair:', extra + '    waterpair:')
sub("if (order === 2) {", "if (order === 3) { const dir = new THREE.Vector3(b[0] - a[0], b[1] - a[1], b[2] - a[2]).normalize(); let perp = new THREE.Vector3(0, 0, 1).cross(dir); if (perp.length() < 0.1) perp = new THREE.Vector3(1, 0, 0).cross(dir); perp.normalize().multiplyScalar(0.15);\n        cyl(a, b, 0.055); cyl(a, b, 0.055, perp); cyl(a, b, 0.055, perp.clone().negate()); } else if (order === 2) {")

for m in re.finditer(r'.{40}\bic1\b.{40}', t): print('NOTE ic1:', m.group(0))
out = ROOT / ch / 'slides' / 'index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(t)
print(out, len(t), 'slides:', len(S))
