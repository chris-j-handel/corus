"""A match, and no deciding. Each passage of each paper of the past not yet read whole, matched with the full text
of the living files and the gathering files. A passage each of whose concept sentences is word for word in one of them
has its fate, dissolving; each other passage is written out by cluster for a reading, and reading decides its fate:
placing, carrying or dissolving, Exhibit TWENTY-FOUR Geodesic Improving Method 1.4.

Before it, once, the papers of the past unpacked beside the repository:
    git fetch -q origin archive:refs/remotes/origin/archive
    mkdir -p /tmp/past && git archive refs/remotes/origin/archive | tar -x -C /tmp/past
Use, from the repository's root:
    python3 -I incoming/v404mgr/instruments/each_passage_of_the_past_matched.py /tmp/past size
    python3 -I incoming/v404mgr/instruments/each_passage_of_the_past_matched.py /tmp/past write <a folder outside the repository>
The second writes one paper for each cluster, each passage not word for word in the living zone, for a reading."""
import re,os,json,collections,subprocess,glob,sys
def sh(c,t=200): return subprocess.run(c,capture_output=True,text=True,timeout=t,errors='replace').stdout
A=sys.argv[1].rstrip('/')
strip=lambda s: re.sub(r'[*_`>#|\\\[\]()]',' ',s)
norm=lambda s: re.sub(r'\s+',' ',strip(s)).strip().lower()
W=re.compile(r"[a-z][a-z'\-]{3,}")
LG=[]
for f in json.load(open('files.json'))+sorted(glob.glob('gathering-value/*.md')):
    LG.append(norm(open(f,encoding='utf-8',errors='replace').read()))
LGtext='\n'.join(LG)
post=collections.Counter()
for l in LGtext.split('\n'):
    pass
vocab=collections.Counter(W.findall(LGtext))
CUR=set('parity parities self selves universe universal moment resolver geodesic torus corus society societies prior intelligence stable surface binary involution podal prime primes dimension dimensions orthogonal spiral helix fractal carbon atom equilibrium equilibria horizon destiny observer naming'.split())
CON={w for w,n in vocab.items() if n>=40 and (('-' in w and len(w)>=7) or (w.endswith('ing') and len(w)>=8))}|CUR
def sents(p): return [s for s in re.split(r'(?<=[.?!;:])\s+',re.sub(r'\s+',' ',strip(p)).strip()) if len(s.split())>=6]
def keep(p):
    b=os.path.basename(p).lower()
    if 'transcript' in b: return False                       # a transcript is a session's own telling
    if re.match(r'(exhibit_|natural_)[a-z-]+.*_v\d+\w*\.md$',b) and not re.search(r'explor|propos|report|gathering|opening',b): return False   # a living file's own prior version
    return b.endswith('.md')
def folder(*rel):
    out=[]
    for r in rel:
        for top in ('archive','incoming'):
            base=os.path.join(A,top,r)
            if os.path.isdir(base):
                for dp,_,fns in sorted(os.walk(base)):
                    for fn in sorted(fns):
                        p=os.path.join(dp,fn)
                        if keep(p): out.append((p.replace(A+'/',''),open(p,encoding='utf-8',errors='replace').read()))
    return out
def offer(n):
    out=[]
    o=sh(['gh','api',f'repos/chris-j-handel/corus/pulls/{n}/files?per_page=100','--jq','.[]|select(.status=="added")|.filename'])
    if not sh(['git','rev-parse','-q','--verify',f'refs/remotes/pull/{n}']).strip(): sh(['git','fetch','-q','origin',f'refs/pull/{n}/head:refs/remotes/pull/{n}'])
    for fn in o.split('\n'):
        if fn.strip() and keep(fn): out.append((fn,sh(['git','show',f'refs/remotes/pull/{n}:{fn}'])))
    return out
C=collections.OrderedDict()
C['Carbon']=[('Carbon Dating Explaining',folder('carbon-dating-explaining-20261103')),('v396 · Carbon Co-Chaining Understanding',folder('v396')),('Atom and carbon with primes',folder('atom-carbon-prime-correspondence')),('Carbon scale existing things and ghosts',folder('carbon_scale_existing_things_and_ghosts')),('Atomic fractal exploring',offer(155))]
C['Chemistry']=[('Chemistry and water',folder('chemistry-water-20261022')),('v392chem · living learning from the chemistry exploring',folder('v392chem','session_v392chem'))]
C['Health, biology and medicine']=[('v397Med · Natural Medicine, gathering observings',folder('v397Med')),('v382A · health, biology and medicine in logical sequence',folder('session_v382A'))]
C['Physics']=[('v376 and v377 · physics observings and natural torusing, the proposed Natural Physics and its reviews',folder('review_physics_observings_v376','review_natural_physics_improving_v376','natural_physics_v377','review_natural_physics_v377','physics_for_other_files_v377','physics_at_the_code_v376'))]
C['Method and logic']=[('Self Competency Binary Logic and Method Explaining',folder('self-competency-method-20261028')),('v383Op · two logics, each followed alone',folder('session_v383Op')),('v385A · comparisons',folder('session_v385A_comparisons')),('v385R · universal claims and logical cohering',offer(128))]
C['Networking and transmissioning']=[('v384A · proposal for Exhibit SIX Natural Transmissioning',folder('session_v384A')),('v380 · Natural Networking explorings',folder('session_v380'))]
C['Forms']=[('Vault bi-folding',folder('vault-bi-folding')),('Plane coloring and natural torusing',offer(136)),('v386F · living at scales, the lean set, bi-coupling as possibling',offer(134))]
C['The dossiers of open value']=[('v392F · dossiers of open value',folder('v392F'))]
C['Bubbling']=[('v403bubble · bubbling',[(p,open(p,encoding='utf-8',errors='replace').read()) for p in sorted(glob.glob('incoming/v403bubble/*.md'))])]
mode=sys.argv[2]; seen=set(); T=collections.Counter(); OUT={}
for cl,items in C.items():
    ct=collections.Counter(); body=[]
    for name,fl in items:
        for path,t in fl:
            m=re.search(r'^#\s+(.+)$',t,re.M); title=(m.group(1).strip() if m else os.path.basename(path))
            keepers=[]
            for para in re.split(r'\n\s*\n|\n(?=[-*] |\d+\. |#)',t):
                p=para.strip()
                if len(p)<60 or p.startswith(('http','!','```','|')): continue
                ss=sents(p)
                cs=[s for s in ss if len([w for w in set(W.findall(s.lower())) if w in CON])>=2]
                if not cs: ct['plain or working']+=1; continue
                k=re.sub(r'\W+','',p.lower())[:200]
                if k in seen: continue
                seen.add(k)
                held=[norm(s) in LGtext for s in cs]
                ct['concept passages']+=1; ct['concept sentences']+=len(cs); ct['held sentences']+=sum(held)
                if all(held): ct['dissolved']+=1
                else: ct['staying']+=1; ct['staying words']+=len(p.split()); keepers.append(re.sub(r'\s*\n\s*',' ',p))
            if keepers: body.append((name,title,keepers))
    OUT[cl]=body
    print(f"{cl:32s} concept passages {ct['concept passages']:5d} · held whole, dissolving {ct['dissolved']:5d} · staying {ct['staying']:5d} ({ct['staying words']:6d} words) · concept sentences {ct['concept sentences']:5d}, held word for word {ct['held sentences']:5d}")
    T.update(ct)
print(f"{'ALL':32s} concept passages {T['concept passages']:5d} · held whole, dissolving {T['dissolved']:5d} · staying {T['staying']:5d} ({T['staying words']:6d} words) · concept sentences {T['concept sentences']:5d}, held word for word {T['held sentences']:5d}")
if mode=='write':
    d=sys.argv[3]; os.makedirs(d,exist_ok=True)
    for cl,body in OUT.items():
        L=[f"Not yet artifact · {cl}","",f"# {cl}: each passage no living file and no gathering file has word for word","",
           "**No word here has authority.** These passages are as their papers have them, in the naming of their own time. Each is waiting for one of three fates by Exhibit TWENTY-FOUR Geodesic Improving Method: placing, with the living file welcoming it; carrying, with no living file having a position for it; or dissolving. A passage leaves this paper with its fate. This paper is artifact with no passage in it.",""]
        for name,title,keepers in body:
            L+= [f"## {name} · {title[:110]}",""]+[f"- {k}" for k in keepers]+[""]
        open(os.path.join(d,re.sub(r'[^A-Za-z]+','_',cl).strip('_')+'.md'),'w',encoding='utf-8').write('\n'.join(L))
    print('written',len(OUT),'papers')
