"""An experiment in learning which past papers add value. For each paper: what can be known of it without reading it."""
import re,os,sys,json,glob,collections,subprocess,pickle
src=open('incoming/v404mgr/instruments/each_passage_of_the_past_matched.py',encoding='utf-8').read()
src=src[:src.index('mode=sys.argv[2]')]
sys.argv=['x',sys.argv[1],'size']   # the folder the papers of the past are unpacked in
exec(src)                                   # gives C (clusters → papers), LGtext, norm, sents, W, CON
LF=json.load(open('files.json')); GF=sorted(glob.glob('gathering-value/*.md'))
lines=[l.lower() for f in LF+GF for l in open(f,encoding='utf-8',errors='replace').read().split('\n') if len(l)>40]
W5=re.compile(r"[a-z][a-z'\-]{4,}")
idx=collections.defaultdict(set); freq=collections.Counter()
for i,l in enumerate(lines):
    for w in set(W5.findall(l)): idx[w].add(i); freq[w]+=1
LGl=' '.join(lines)
G0=''
Gall=' '.join(open(f,encoding='utf-8').read() for f in GF)
WORK=re.compile(r"\b(pull request|merge[ds]?|branch|commit|snapshot|session report|this report|this page|this contribution|this review|this session|the reviewer|the coordinator|reader checks|check_set|\.py\b|\.md\b|incoming/|carry/|archive/|v3\d\d[a-z]*\b|proposal|proposed section|draft|read-only|was read|were read|not read|rerun|re-read|standing at|pass \d|droplet|offerings|insertlet|the kit|registry row|line \d+|lines \d+)",re.I)
STOP=set('The A An It Its This That These Those Each No In At With By For And But Or Of To As If On From When Where What Which Who How Why Natural Intelligence Exhibit Physics Numbers Mathematics Networking Naming Explaining Resolver Living NI ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN Method Geodesic Improving Session Report Record Registry Value Chemistry Biology Medicine Health Section README Corus Societies Society Engineering Transmissioning Philosophy Values Destinies Emanating Exploring Illustrating Ghost Equilibria Hard Problem Problems Resolving Co-Chaining Logic Carbon Self Competency Binary Droplet Concern Possible Aimed Insertlet Standing Rigor Part Step Steps Anchor Correction Preserve Issue Check Core Command'.split())
def anchors(p):
    a=set()
    for m in re.finditer(r'(?<![.?!:]\s)(?<!^)(?<!\*\*)\b([A-Z][a-z]{3,})\b',p):
        if m.group(1) not in STOP: a.add(m.group(1))
    for m in re.finditer(r'\b\d+(?:\.\d+)?\s?(?:%|keV|MeV|GeV|eV|km|nm|Hz|kHz|MHz|K\b|ms\b|degrees|°|kcal|kJ|ppm|mV)',p): a.add(m.group(0))
    return a
allsent=collections.Counter()
P=[]
for cl,items in C.items():
    for name,fl in items:
        for path,t in fl:
            ss=[s for s in re.split(r'(?<=[.?!])\s+',re.sub(r'\s+',' ',strip(t))) if len(s.split())>=7]
            P.append(dict(cl=cl,name=name,path=path,t=t,ss=ss))
            for s in set(norm(x) for x in ss): allsent[s]+=1
rows=[]
for p in P:
    ss=p['ss']; t=p['t']; n=len(ss) or 1
    work=sum(1 for s in ss if WORK.search(s))/n
    wfw=sum(1 for s in ss if norm(s) in LGtext)/n
    tog=0; cs=0
    for s in ss:
        ws=set(W5.findall(s.lower()))
        if len([w for w in ws if w in CON])<2: continue
        cs+=1
        known=sorted([w for w in ws if w in freq],key=lambda w:freq[w])[:3]
        if len(known)==3 and idx[known[0]]&idx[known[1]]&idx[known[2]]: tog+=1
    a=anchors(t); newa=sorted(x for x in a if x.lower() not in LGl)
    q=len(re.findall(r'is-or-is-not\?|still to be (?:said|named|explained)|remains open|still open',t))
    dup=sum(1 for s in ss if allsent[norm(s)]>1)/n
    sess=re.search(r'\bv(\d{3}[A-Za-z]*)\b',p['path']+' '+p['name']); sn=sess.group(0) if sess else ''
    notes=(len(re.findall(r'\b'+re.escape(sn)+r'\b',Gall,re.I))+len(re.findall(r'\b'+re.escape(sn)+r'\b',G0,re.I)*0)) if sn else 0
    b=os.path.basename(p['path']).lower()
    kind=('a page about pages' if re.search(r'readme|check|standing|plan|record|index|measure|sums|carrying',b) else 'a proposal or its review' if re.search(r'propos|review|before',b) else 'a session\'s report' if re.search(r'report|session',b) else 'a reading or a paper')
    rows.append(dict(cl=p['cl'],name=p['name'],path=p['path'],words=len(t.split()),sent=len(ss),work=round(work,2),wfw=round(wfw,2),tog=round(tog/(cs or 1),2),cs=cs,newa=len(newa),newa_list=newa[:12],q=q,dup=round(dup,2),sess=sn,notes=notes,kind=kind))
pickle.dump(rows,open(sys.argv[2] if len(sys.argv)>2 else 'papers.pkl','wb'))   # one row for each paper: its words, its share telling of the working, its field's records no file has, its questions
print(len(rows),'papers ·',sum(r['words'] for r in rows),'words')
k=collections.Counter(r['kind'] for r in rows); print(dict(k))
