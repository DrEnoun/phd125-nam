"""Build the PHD125 Study Hub home page (index.html) from the PHD115 hub template.
Run from the repo root:  python3 -I _src/build_hub.py
Edit CHAPTERS in _src/hub_chapters.js to switch on an activity (give it a path)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
t = (ROOT / '_src/templates/hub.html').read_text()
chapters_js = (ROOT / '_src/hub_chapters.js').read_text()

css_end = t.index('</style>')
head = t[:css_end]
head = head.replace('<title>PHD115 Study Hub · Chemistry with Dr. NAM</title>',
                    '<title>PHD125 Study Hub · Chemistry with Dr. NAM</title>')
extra_css = """
.aims{margin:30px 0 8px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.aims h2{margin:0}
.aims small{color:var(--muted);font-size:.85rem}
.subs{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px;padding:0;list-style:none}
.subs a{display:inline-block;font-size:.8rem;text-decoration:none;color:var(--tc,var(--cold));background:var(--ts,var(--cold-soft));border-radius:999px;padding:3px 10px}
.subs a:hover{text-decoration:underline}
.topic.soon{opacity:.75}
.draft{background:#FFF4CC;border:1px solid #E8C33A;color:#5B4500;border-radius:12px;padding:10px 14px;font-size:.88rem;margin:0 0 14px}
"""
tail = t[t.index('// ---- Progress'):]

# Progress, last-visited and reset already use phd125 keys after the rename below.
tail = tail.replace('phd115', 'phd125')

body = r"""</style>
</head>
<body>
<header><div class="in">
<p class="kick">PHD125 Pharmaceutical Organic Chemistry · Diploma in Pharmacy</p>
<h1>Chemistry with Dr. NAM · Study Hub</h1>
<p class="brand">Dr. Nur 'Ainun Mokhtar (Dr. NAM) · Faculty of Pharmacy, UiTM Bertam, Penang</p>
<p class="sub">Self-instructional materials for PHD125, chapter by chapter, following the course outline. Study at your own pace, in any order, as often as you like. Every activity can be reset and tried again.</p>
</div></header>

<main><div class="in">
<p class="draft" id="draftNote"><b>Draft for review.</b> Chapters 1 and 2 are ready to try. Other chapters are being built. Sign-in and the leaderboard are switched off in this draft.</p>
<div id="cont" class="card continue" hidden></div>

<h2>Suggested study path for each chapter</h2>
<ol class="path">
 <li><span class="n">1</span><b>Before class</b>15-min warm-up</li>
 <li><span class="n">2</span><b>Slides</b>the full lecture</li>
 <li><span class="n">3</span><b>After class</b>check your understanding</li>
 <li><span class="n">4</span><b>Tutorial</b>exam-style practice</li>
 <li><span class="n">5</span><b>Game</b>quick-fire revision</li>
</ol>

<div class="seg" role="group" aria-label="Browse">
 <button id="vTopic" aria-pressed="true">By chapter</button>
 <button id="vAct" aria-pressed="false">By activity</button>
</div>
<p class="small"><a href="leaderboard/">Game leaderboard</a>: best score per chapter, open all semester.</p>
<p class="small">On a phone or tablet, turn it sideways for slides. Tap the right side of a slide for next, the left side to go back.</p>

<section id="byTopic"></section>
<section id="byAct" hidden></section>

<section class="card lab" aria-labelledby="labTitle">
 <div>
  <p class="k">Hand-gesture games</p>
  <h2 id="labTitle">Dr. NAM Virtual Secret Lab</h2>
  <p>Play chemistry with your hands in front of the webcam, or just use a mouse or touch. Build Lewis structures and watch molecules snap into their 3D shapes: a good warm-up for the VSEPR chapter.</p>
 </div>
 <div style="display:grid;gap:6px;justify-items:end"><a class="btn" href="https://drenoun.github.io/dr-nam-virtual-secret-lab/?hub" target="_blank" rel="noopener">Open the Virtual Lab ↗</a></div>
</section>

<footer>
 <div class="foot-row"><span>Your progress is saved on this device only. Nothing is sent anywhere.</span><button class="btn warn" id="reset">Reset my progress</button></div>
 <p class="brand">Dr. NAM · Faculty of Pharmacy, UiTM Bertam, Penang</p>
 <p>Adapted from <i>The Basics of General, Organic, and Biological Chemistry</i> (Ball, Hill &amp; Scott) and <i>Fundamentals of General Organic and Biological Chemistry</i>, LibreTexts, CC BY-NC-SA 3.0, with other open sources credited on each page. Shared under the same licence for non-commercial teaching.</p>
</footer>
</div></main>

<script>
""" + chapters_js + r"""
// ---- Rendering (by chapter, grouped under AIMS chapters; extras last)
const esc=s=>s.replace(/&(?!amp;)/g,'&amp;');
const actsOf=t=>ACTS.filter(A=>(t.only||ACTS.map(a=>a.k)).includes(A.k));
function goEl(t,A){const path=t.a[A.k];if(!path)return `<span class="go"><span class="t">${A.name}</span><span class="st">Coming soon</span></span>`;
 const s=status(t.code,A.k);return `<a class="go" href="${path}" data-t="${t.code}" data-a="${A.k}"><span class="t">${A.name}</span><span class="st ${s.cls}">${s.txt}</span></a>`}
function card(t){const av=actsOf(t).filter(A=>t.a[A.k]);const pct=av.length?Math.round(av.reduce((s,A)=>s+status(t.code,A.k).pct,0)/av.length):0;
 const subs=t.subs?`<ul class="subs">${t.subs.map(([id,name])=>t.a.slides?`<li><a href="${t.a.slides}#${id}" data-t="${t.code}" data-a="slides">${name}</a></li>`:`<li><a aria-disabled="true" style="pointer-events:none">${name}</a></li>`).join('')}</ul>`:'';
 return `<article class="card topic${av.length?'':' soon'}" id="${t.code}" style="${tc(t.code)}"><div class="th"><span class="ico">${ICON(t.code)}</span><div><span class="tag">${t.label}</span><h3>${esc(t.title)}</h3></div></div>
  <p class="b">${t.blurb}</p>${subs}${av.length?`<div class="bar" aria-label="Progress ${pct}%"><i style="width:${pct}%"></i></div>`:''}
  <div class="acts">${actsOf(t).map(A=>goEl(t,A)).join('')}</div>
  ${t.lab?`<p class="labl">🎯 Virtual Lab: ${t.lab.map(([id,name])=>{const b=labBest(id);return `<a href="${LAB}?hub#/play/${id}" target="_blank" rel="noopener">${name}</a>${b?` <span class="st done">best ${b} ✓</span>`:''}`}).join(' · ')}</p>`:''}</article>`}
function renderTopics(){const g=[['Course chapters','Following the PHD125 course outline',TOPICS.filter(t=>!t.extra)],['Beyond the syllabus','Not examined. For curious students.',TOPICS.filter(t=>t.extra)]];
 document.getElementById('byTopic').innerHTML=g.map(([h,s,list])=>`<div class="aims"><h2>${h}</h2><small>${s}</small></div><div class="grid">${list.map(card).join('')}</div>`).join('')}
function renderActs(){document.getElementById('byAct').innerHTML=ACTS.map(A=>`<div class="act"><h2 style="margin-top:22px">${A.name}</h2><p class="desc">${A.desc}</p><div class="rows">${
  TOPICS.filter(t=>actsOf(t).includes(A)).map(t=>{const path=t.a[A.k];const s=path?status(t.code,A.k):{txt:'Coming soon',cls:''};
   return `<div class="row tp" style="${tc(t.code)}"><div class="l"><span class="ico">${ICON(t.code)}</span><span><b>${t.label} · ${esc(t.title)}</b><span class="st ${s.cls}">${s.txt}</span></span></div>${path?`<a class="btn" href="${path}" data-t="${t.code}" data-a="${A.k}">Open</a>`:`<span class="btn" aria-disabled="true">Soon</span>`}</div>`}).join('')}</div></div>`).join('')}
function renderCont(){const l=LS.get('phd125:last');const el=document.getElementById('cont');if(!l){el.hidden=true;return}
 const t=TOPICS.find(x=>x.code===l.topic),A=ACTS.find(x=>x.k===l.act);if(!t||!A||!t.a[A.k]){el.hidden=true;return}
 el.hidden=false;el.innerHTML=`<div><p><b>Continue where you left off</b></p><p>${t.label} · ${esc(t.title)} · ${A.name}</p><small>${status(t.code,A.k).txt}</small></div><a class="btn" href="${t.a[A.k]}" data-t="${t.code}" data-a="${A.k}">Continue</a>`}
"""

# Keep the template's progress/status helpers but drop its own render functions (replaced above).
prog = tail
cut = prog.index('const esc=')
helpers = prog[:cut]
rest = prog[prog.index('function view('):]
rest = rest.replace("try{localStorage.setItem('phd125:view',t?'topic':'act')}catch(e){}", "try{localStorage.setItem('phd125:view',t?'topic':'act')}catch(e){}")
out = head + extra_css + body + helpers + rest
# The Virtual Secret Lab saves its own scores under phd115:lab:<id>; that key is intentional.
assert 'phd115' not in out.replace('phd115:lab:','') and 'PHD115' not in out, 'leftover PHD115 text'
(ROOT / 'index.html').write_text(out)
print('index.html', len(out))
