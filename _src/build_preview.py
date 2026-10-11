"""Copy the built site into a preview folder, with links rewritten to explicit index.html files
(the private review preview cannot serve folder URLs). Usage: python3 -I _src/build_preview.py <out_dir>
Prints the files map for publishing."""
import json, re, shutil, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(sys.argv[1]) / 'site'
if out.exists():
    shutil.rmtree(out)
out.mkdir(parents=True)
for item in ['index.html', 'js', 'img', 'leaderboard', 'downloads'] + sorted(p.name for p in ROOT.glob('ch[1-8]')) + sorted(p.name for p in ROOT.glob('x[1-3]')):
    src = ROOT / item
    if src.is_dir():
        shutil.copytree(src, out / item)
    elif src.exists():
        shutil.copy(src, out / item)
pat = re.compile(r'''(["'`])((?:\.\./)+(?:[a-z0-9-]+/)*|(?:ch[1-8]|x[1-3]|leaderboard)/(?:[a-z0-9-]+/)*)(#[A-Za-z0-9]*)?\1''')
for f in list(out.rglob('*.html')) + [out / 'js/track.js', out / 'js/shift.js']:
    s = f.read_text()
    s = pat.sub(lambda m: m.group(1) + m.group(2) + 'index.html' + (m.group(3) or '') + m.group(1), s)
    s = s.replace('href="../../#${DATA.topic}"', 'href="../../index.html#${DATA.topic}"')
    f.write_text(s)
files = {str(p.relative_to(out.parent)): str(p.relative_to(out.parent)) for p in sorted(out.rglob('*')) if p.is_file()}
print(json.dumps(files))
