// ---- Site content: give an activity a path when it is ready (missing = coming soon)
// Virtual Secret Lab (hand-gesture games)
const LAB='https://drenoun.github.io/dr-nam-virtual-secret-lab/';
// Lab results (best score) are saved on this device by the Lab itself
const labBest=id=>{try{const v=JSON.parse(localStorage.getItem('phd115:lab:'+id)||'null');return v&&v.best?v.best:0}catch(e){return 0}};
const ACTS=[
 {k:'pre',  name:'Before class', desc:'A short reading and readiness check to do before the lecture.'},
 {k:'slides',name:'Slides',     desc:'The complete lecture, organised by subchapter: figures, worked examples and quick checks.'},
 {k:'post', name:'After class', desc:'Questions and a pharmacy scenario to check your understanding.'},
 {k:'tut',  name:'Tutorial',    desc:'Exam-style questions with hints and full worked solutions.'},
 {k:'game', name:'Game',        desc:'A timed quick-fire game that shows which outcomes to revise.'}
];
// ---- Cute 3D icons per chapter (inline SVG; ids get a suffix so each copy has its own gradients)
const ICON=(()=>{
 const rg=(id,a,b)=>`<radialGradient id="${id}" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="${a}"/><stop offset="1" stop-color="${b}"/></radialGradient>`;
 const lg=(id,st)=>`<linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1">${st.map((c,i)=>`<stop offset="${i/(st.length-1)}" stop-color="${c}"/>`).join('')}</linearGradient>`;
 const shine=(x,y,r)=>`<ellipse cx="${x}" cy="${y}" rx="${r*.3}" ry="${r*.17}" fill="#fff" opacity=".6" transform="rotate(-28 ${x} ${y})"/>`;
 const ball=(id,x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="url(#${id})"/>${shine(x-r*.38,y-r*.45,r)}`;
 const face=(x,y,k)=>`<circle cx="${x-5*k}" cy="${y}" r="${2.3*k}" fill="#1B2A41"/><circle cx="${x+5*k}" cy="${y}" r="${2.3*k}" fill="#1B2A41"/><circle cx="${x-4.2*k}" cy="${y-.9*k}" r="${.85*k}" fill="#fff"/><circle cx="${x+5.8*k}" cy="${y-.9*k}" r="${.85*k}" fill="#fff"/><path d="M${x-2.6*k} ${y+3.6*k} Q${x} ${y+6.4*k} ${x+2.6*k} ${y+3.6*k}" stroke="#1B2A41" stroke-width="${1.5*k}" fill="none" stroke-linecap="round"/><ellipse cx="${x-8.3*k}" cy="${y+3.4*k}" rx="${2.1*k}" ry="${1.2*k}" fill="#FF6F8E" opacity=".5"/><ellipse cx="${x+8.3*k}" cy="${y+3.4*k}" rx="${2.1*k}" ry="${1.2*k}" fill="#FF6F8E" opacity=".5"/>`;
 const shadow=w=>`<ellipse cx="32" cy="60.5" rx="${w}" ry="2.8" fill="#1B2A41" opacity=".15"/>`;
 const stick=(a,b,c,d)=>`<path d="M${a} ${b} L${c} ${d}" stroke="#C9D3DC" stroke-width="4.5" stroke-linecap="round"/>`;
 const D={
  // carbon atom with four bonds
  ch1:u=>`<defs>${rg('c'+u,'#9FB0C4','#3E4E63')}${rg('h'+u,'#FFFFFF','#B9C6D3')}</defs>${shadow(24)}
   ${stick(32,32,10,14)}${stick(32,32,54,14)}${stick(32,32,10,52)}${stick(32,32,54,52)}
   ${ball('h'+u,10,14,6.5)}${ball('h'+u,54,14,6.5)}${ball('h'+u,10,52,6.5)}${ball('h'+u,54,52,6.5)}${ball('c'+u,32,32,15)}${face(32,33,.95)}`,
  // zig-zag carbon chain
  ch2:u=>`<defs>${rg('c'+u,'#9FB0C4','#3E4E63')}</defs>${shadow(26)}
   <path d="M8 40 L20 26 L32 40 L44 26 L56 40" stroke="#C9D3DC" stroke-width="4.5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
   ${ball('c'+u,8,40,7)}${ball('c'+u,20,26,7)}${ball('c'+u,44,26,7)}${ball('c'+u,56,40,7)}${ball('c'+u,32,40,12)}${face(32,41,.75)}`,
  // O-H drop with a sulfur buddy
  ch3:u=>`<defs>${rg('o'+u,'#FFB3A8','#D2372B')}${rg('s'+u,'#FFF1A8','#D7A80F')}${rg('h'+u,'#FFFFFF','#B9C6D3')}</defs>${shadow(24)}
   ${stick(28,34,50,18)}${ball('h'+u,50,18,7)}${ball('s'+u,50,46,8.5)}${ball('o'+u,26,35,16)}${face(26,36,.95)}`,
  // capsule pill
  ch4:u=>`<defs>${lg('p1'+u,['#FFC7A8','#E2672E'])}${lg('p2'+u,['#FFFFFF','#D7E0E8'])}</defs>${shadow(22)}
   <g transform="rotate(-30 32 34)"><rect x="8" y="22" width="48" height="24" rx="12" fill="url(#p2${u})" stroke="#A9BDCC" stroke-width="1.5"/>
   <path d="M20 22 H32 V46 H20 A12 12 0 0 1 20 22 Z" fill="url(#p1${u})"/></g>${face(36,36,.8)}`,
  // sugar cube
  ch5:u=>`<defs>${lg('q'+u,['#FFFFFF','#E3ECF3'])}</defs>${shadow(22)}
   <path d="M32 10 L54 21 L54 45 L32 56 L10 45 L10 21 Z" fill="url(#q${u})" stroke="#A9BDCC" stroke-width="2" stroke-linejoin="round"/>
   <path d="M10 21 L32 32 L54 21 M32 32 V56" stroke="#C9D3DC" stroke-width="2" fill="none"/>
   <circle cx="20" cy="17" r="1.4" fill="#C9D3DC"/><circle cx="40" cy="15" r="1.2" fill="#C9D3DC"/>${face(21,42,.7)}`,
  // oil droplet
  ch6:u=>`<defs>${lg('l'+u,['#FFF0A6','#E0A11B'])}</defs>${shadow(17)}
   <path d="M32 5 C40 18 50 28 50 40 C50 51 42 58 32 58 C22 58 14 51 14 40 C14 28 24 18 32 5 Z" fill="url(#l${u})"/>${shine(24,32,16)}${face(32,43,.9)}`,
  // enzyme pac-man with substrate
  ch7:u=>`<defs>${rg('e'+u,'#C9F0D5','#2E9E62')}${rg('s'+u,'#FFD1DC','#C2456A')}</defs>${shadow(22)}
   <path d="M30 32 L52 20 A24 24 0 1 0 52 44 Z" fill="url(#e${u})"/>${ball('s'+u,55,32,6)}${face(22,30,.9)}`,
  // TLC plate with spots
  ch8:u=>`<defs>${lg('t'+u,['#FFFFFF','#E3ECF3'])}</defs>${shadow(16)}
   <rect x="18" y="5" width="28" height="52" rx="3" fill="url(#t${u})" stroke="#A9BDCC" stroke-width="2"/>
   <path d="M18 48 H46" stroke="#A9BDCC" stroke-width="1.5" stroke-dasharray="3 2"/>
   <ellipse cx="26" cy="16" rx="4" ry="2.6" fill="#7A4FD0"/><ellipse cx="38" cy="24" rx="4" ry="2.6" fill="#2F6F9F"/><ellipse cx="26" cy="31" rx="4" ry="2.6" fill="#E2672E"/>${face(32,40,.6)}`,
  // DNA ladder
  x1:u=>`${shadow(18)}<path d="M20 6 C44 18 20 30 44 42 C52 46 44 54 44 58" stroke="#2F6F9F" stroke-width="4" fill="none" stroke-linecap="round"/>
   <path d="M44 6 C20 18 44 30 20 42 C12 46 20 54 20 58" stroke="#C2456A" stroke-width="4" fill="none" stroke-linecap="round"/>
   <g stroke="#C9D3DC" stroke-width="2.5" stroke-linecap="round"><path d="M25 10 H39 M28 24 H36 M25 36 H39"/></g>${face(32,49,.6)}`,
  // fatty-acid flame
  x2:u=>`<defs>${lg('f'+u,['#FFE08A','#F7A23B','#D3561C'])}</defs>${shadow(17)}
   <path d="M32 4 C39 15 50 22 49 38 C48 51 40 58 32 58 C23 58 15 51 15 39 C15 29 22 25 25 15 C28 20 29 23 31 25 C34 18 35 11 32 4 Z" fill="url(#f${u})"/>
   <path d="M22 50 L28 44 L34 50 L40 44" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" opacity=".8"/>${face(32,36,.85)}`,
  // tetrahedron
  x3:u=>`<defs>${rg('c'+u,'#B6F3EA','#0F6A80')}</defs>${shadow(22)}
   <path d="M32 6 L56 50 L32 58 L8 50 Z M32 6 L32 58" stroke="#0F6A80" stroke-width="2" fill="rgba(47,179,168,.18)" stroke-linejoin="round"/>
   <path d="M8 50 L56 50" stroke="#0F6A80" stroke-width="1.5" stroke-dasharray="3 3"/>${ball('c'+u,32,36,10)}${face(32,37,.62)}`
 };
 let n=0;return c=>D[c]?`<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">${D[c]('_'+(n++))}</svg>`:'';
})();
// Chapter colours: [stripe and text, soft background]
const TC={ch1:['#2F6F9F','#E1EEF7'],ch2:['#1F7A86','#DFF1F2'],ch3:['#B3412F','#FBE6E2'],ch4:['#B86E00','#FBEFD9'],ch5:['#5B6B7F','#E8EEF4'],ch6:['#9A7A00','#FBF3D6'],
 ch7:['#2E7D4F','#E3F3E9'],ch8:['#7A4E9C','#EFE6F5'],x1:['#A23B54','#F8E4E9'],x2:['#C0581C','#FBE9DC'],x3:['#0F6A80','#DDF1F4']};
const tc=c=>`--tc:${TC[c][0]};--ts:${TC[c][1]}`;
const EXTRA=['slides','tut','game'];
const TOPICS=[
 {code:'ch1',label:'Chapter 1',title:'Introduction to Organic Molecule',blurb:'What makes carbon special, how to draw organic molecules, functional groups, and organic chemistry in pharmacy and everyday life.',
  subs:[['s1','1.1 What is organic chemistry'],['s2','1.2 Features of organic compounds'],['s3','1.3 Drawing organic molecules'],['s4','1.4 Functional groups'],['s5','1.5 Pharmacy and everyday life']],
  a:{pre:'ch1/pre/',slides:'ch1/slides/',post:'ch1/post/',tut:'ch1/tutorial/',game:'ch1/game/'}},
 {code:'ch2',label:'Chapter 2',title:'Saturated and Unsaturated Hydrocarbons',blurb:'Alkanes, alkenes, alkynes and aromatic compounds: naming, isomers, properties and reactions.',
  subs:[['s1','2.1 Alkanes'],['s2','2.2 Alkenes, Alkynes & Aromatics']],
  a:{pre:'ch2/pre/',slides:'ch2/slides/',post:'ch2/post/',tut:'ch2/tutorial/',game:'ch2/game/'}},
 {code:'ch3',label:'Chapter 3',title:'Organic Compounds that Contain Oxygen and Sulphur',blurb:'Alcohols and phenols, ethers and thiols, aldehydes and ketones.',
  subs:[['s1','3.1 Alcohols'],['s2','3.2 Ethers & Thiols'],['s3','3.3 Aldehydes & Ketones']],
  a:{pre:'ch3/pre/',slides:'ch3/slides/',post:'ch3/post/',tut:'ch3/tutorial/',game:'ch3/game/'}},
 {code:'ch4',label:'Chapter 4',title:'Carboxylic Acid, Ester, Amines, Amide',blurb:'Acids and bases of organic chemistry and their derivatives, with the drugs that contain them.',
  subs:[['s1','4.1 Carboxylic Acids'],['s2','4.2 Esters'],['s3','4.3 Amines'],['s4','4.4 Amides']],a:{pre:'ch4/pre/',slides:'ch4/slides/',post:'ch4/post/',tut:'ch4/tutorial/',game:'ch4/game/'}},
 {code:'ch5',label:'Chapter 5',title:'Carbohydrates',blurb:'Monosaccharides, chirality, cyclic sugars, disaccharides and polysaccharides.',a:{}},
 {code:'ch6',label:'Chapter 6',title:'Lipids',blurb:'Fatty acids, waxes, fats and oils, phospholipids, cell membranes and steroids.',a:{}},
 {code:'ch7',label:'Chapter 7',title:'Amino Acids, Proteins and Enzymes',blurb:'Amino acids, peptides, protein structure, and how enzymes work and are inhibited by drugs.',a:{}},
 {code:'ch8',label:'Chapter 8',title:'Application of Chromatographic Methods in Pharmaceutical Analysis',blurb:'Principles of chromatography, stationary and mobile phases, TLC, HPLC and GC in pharmacy.',a:{}},
 {code:'x1',label:'Extra',extra:true,only:EXTRA,title:'Nucleic Acids',blurb:'DNA and RNA: structure, base pairing, replication and protein synthesis.',a:{}},
 {code:'x2',label:'Extra',extra:true,only:EXTRA,title:'Lipid Metabolism',blurb:'How the body digests, transports, burns and builds fats.',a:{}},
 {code:'x3',label:'Extra',extra:true,only:EXTRA,title:'VSEPR Theory',blurb:'Why molecules have the shapes they do, from methane to drug molecules.',a:{},
  lab:[['lewis','Lewis Structure Builder'],['hybrid','Hybridization Lab'],['shooter','Molecule Shooter']]},
];
