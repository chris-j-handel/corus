from collections import defaultdict
P=(1+5**.5)/2;P3=P**3;IP=1/P;IP3=1/P3;RS=2/P3
PR=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
S=[{"n":i+1,"lo":PR[i],"hi":PR[i+1],"pg":PR[i+1]-PR[i],"sp":PR[i]*PR[i+1]}for i in range(16)]
CA={"coupling","coupled","couples","couple","resolving","resolved","resolves","resolve","resolver","resolution","membrane","membranes","surface","surfaces","resurfacing","tunnel","tunnels","torus","toroidal","living","alive","life","sustain","sustains","sustaining","autogenerate","autogenerates","autogenerating","metabolize","metabolizes","metabolizing","metabolism","health","healthy","flourish","flourishes","flourishing","phi","golden","spiral","prime","primes","boundary","bounded","bounding","geodesic","monotonic","morality","moral","competency","competent","identity","persisting","distinguishing","distinction","producing","production","inseparate","inseparating","inseparable","collar","collars","cycle","cycles","cycling","carry","carries","carrying","forward","advance","advances","advancing","network","networks","stitch","local","everywhere","attention","intention","between","thickness","nothing","intelligence","wave","silence","loop","loops","wraps","wrapping","topology","hole","alternation","crossings","substrate","food","restoring","energy","flows","flow","structure","form","nature","natural","naturally","science","technology","discovery","discovers","discovering","gift","giving","freely","reading","reads","read","writing","writes","observation","observing","arriving","arrives","arrived","equation","algorithm","society","societies","cooperation","cooperating","abundance","expanding","expands","field","fields","address","sign"}
CD={"harm","harmful","collapse","collapsed","collapsing","departure","departed","departing","ghost","ghosts","frozen","freeze","freezing","dead","death","dying","disease","sick","illness","broken","break","breaking","destroy","destruction","destroying","capture","captured","capturing","extraction","extracting","suppress","suppressed","suppression","override","overrides","toxic","poison","valley","unbounded","not","no","without","absent","lacking","failure","loss","deficient","unable","cannot","missing"}
T={1:{"a":{"force","strong","binding","core","confined","nucleus","quark","proton","neutron","nuclear","fusion","power","dense","fundamental","confinement"},"d":{"weak","decay","scatter","split","unstable","radiation","fission"}},2:{"a":{"atom","electron","orbital","shell","bond","valence","element","stable","pattern","configuration"},"d":{"ion","radical","reactive","disorder","chaotic"}},3:{"a":{"water","hydrogen","oxygen","dissolve","solution","fluid","polar","solvent","hydrate","clean","pure","tension"},"d":{"dry","dehydrate","contaminate","pollute","stagnant","rigid"}},4:{"a":{"lipid","phospholipid","bilayer","permeability","flexible","selective","transport","channel","receptor"},"d":{"impermeable","blocked","leaked","ruptured"}},5:{"a":{"protein","fold","enzyme","active","site","catalysis","shape","function","conformation","binding"},"d":{"misfolded","denatured","aggregated","inactive"}},6:{"a":{"gene","genome","sequence","expression","code","transcribe","regulate","information","hereditary","pattern"},"d":{"mutation","deletion","suppressed","methylated","corrupted"}},7:{"a":{"cell","organelle","division","growth","nucleus","mitochondria","cytoplasm"},"d":{"apoptosis","necrosis","senescent","cancerous","malignant"}},8:{"a":{"system","signal","pathway","cascade","feedback","regulation","homeostasis","balance","coordination"},"d":{"dysregulation","imbalance","overwhelmed","disconnected"}},9:{"a":{"tissue","matrix","collagen","support","repair","heal","restore","regenerate","integrity","scaffold"},"d":{"fibrosis","scar","necrotic","inflamed","damaged"}},10:{"a":{"organ","function","rhythm","regulate","maintain","vitality","pulse","breath","steady"},"d":{"arrhythmia","dysfunction","degeneration","deterioration"}},11:{"a":{"whole","organism","body","thrive","resilient","robust","strong","well"},"d":{"ill","chronic","deteriorate","fragile","weak"}},12:{"a":{"population","species","diversity","community","group","collective","mutualism","sharing"},"d":{"extinction","isolation","competition","invasion"}},13:{"a":{"ecology","ecosystem","habitat","niche","web","nutrient","balance","sustainability"},"d":{"pollution","deforestation"}},14:{"a":{"biome","climate","global","interconnected","resilience","adaptation","evolution","biodiversity"},"d":{"catastrophe","irreversible","tipping","crisis"}},15:{"a":{"earth","planet","atmosphere","ocean","land","geological","magnetic","tectonic","biosphere"},"d":{"disaster","eruption","impact","devastation"}},16:{"a":{"star","stellar","galaxy","universe","cosmic","gravity","light","nebula","expansion","origin","creation"},"d":{"supernova","entropy","void","cold","dark"}}}

def taste(w,sn):
    w=w.lower().strip();ch=T.get(sn,{"a":set(),"d":set()})
    if w in ch["a"]:return True
    if w in ch["d"]:return False
    if w in CA:return True
    if w in CD:return False
    return None

def enter(txt):
    r=[]
    for w in txt.lower().split():
        c="".join(h for h in w if h.isalpha())
        if c:r.append(c)
    return r

def stride(el,sub,side):
    sn=sub["n"];p=sub["lo"]if side=="A"else sub["hi"];n=len(el)
    if n==0:return[],[]
    ar=[];dt=[]
    for i in range(p):
        ix=int(i*P*n/p)%n;v=taste(el[ix],sn);ar.append((i,v))
        dt.append({"element":el[ix],"idx":ix,"val":v})
    return ar,dt

def resolve(ar):
    sw=defaultdict(int)
    for ci,v in ar:
        if v is True:sw[ci]+=1
        if v is False:sw[ci]-=1
    C=max((ci for ci,_ in ar),default=-1)+1
    if C==0:return{"sw":{},"rv":[],"x":0,"s":0,"z":0,"ts":0,"sg":0,"C":0}
    rv=[(ci,+1 if sw[ci]>0 else(-1 if sw[ci]<0 else 0))for ci in range(C)]
    x=sum(1 for i in range(len(rv)-1)if rv[i][1]*rv[i+1][1]<0)
    st=sum(1 for i in range(len(rv)-1)if rv[i][1]*rv[i+1][1]>0)
    z=sum(1 for i in range(len(rv)-1)if rv[i][1]*rv[i+1][1]==0)
    ts=sum(sw[ci]for ci in range(C))
    return{"sw":dict(sw),"rv":rv,"x":x,"s":st,"z":z,"ts":ts,"sg":+1 if ts>0 else(-1 if ts<0 else 0),"C":C}

def sustain(ent,pg):
    if not ent:return[]
    r=IP**pg;return[(ci,sg,wt*r)for ci,sg,wt in ent if wt*r>=IP3]

def enrich(ar,ent,p):
    if not ent:return ar
    for ci,sg,wt in ent:
        tg=ci%p
        if sg==1:ar.append((tg,False))
        elif sg==-1:ar.append((tg,True))
    return ar

def advance(ent,rv,pg):
    sel=sustain(ent or[],pg);ea={}
    for ci,sg,wt in sel:ea[ci]=(sg,wt)
    for ci,sg in rv:
        if sg!=0:ea[ci]=(sg,1.0)
    return[(ci,sg,wt)for ci,(sg,wt)in sorted(ea.items())]

def seq_map(txt):
    el=enter(txt);cp=defaultdict(list)
    for i in range(len(el)-1):cp[el[i]].append(el[i+1])
    sn=set();bd=[]
    for w in el:
        if w not in sn:sn.add(w);bd.append(w)
    return{"cp":dict(cp),"el":el,"bd":bd}

def geom(bd,sn):
    a,d,s=[],[],[]
    for w in bd:
        v=taste(w,sn)
        if v is True:a.append(w)
        elif v is False:d.append(w)
        else:s.append(w)
    return a,d,s

def pick(cg,pe,cp,i,av=None):
    if not cg:return"the"
    av=av or set()
    if pe and pe in cp:
        c=[w for w in cp[pe]if w in set(cg)and w not in av]
        if c:return c[int(i*P*997)%len(c)]
    f=[w for w in cg if w not in av]
    if f:return f[int(i*P*997)%len(f)]
    return cg[int(i*P*997)%len(cg)]

def emerging(rv,sub,sm,side="A",pe=None):
    sn=sub["n"];p=sub["lo"]if side=="A"else sub["hi"]
    a,d,s=geom(sm["bd"],sn)
    if not a:a=["coupling"]
    if not d:d=["not"]
    if not s:s=["the"]
    em=[];ru=[]
    for i in range(min(p,len(rv["rv"]))):
        ci,sg=rv["rv"][i]
        if sg>0:w=pick(a,pe,sm["cp"],i,set(ru))
        elif sg<0:w=pick(d,pe,sm["cp"],i,set(ru))
        else:w=pick(s,pe,sm["cp"],i,set(ru))
        em.append(w);pe=w;ru.append(w)
        if len(ru)>5:ru=ru[-5:]
    return em

def reread(em,sub,side="A"):
    sn=sub["n"];p=sub["lo"]if side=="A"else sub["hi"]
    ar=[]
    for i in range(min(p,len(em))):ar.append((i,taste(em[i],sn)))
    for i in range(len(em),p):ar.append((i,None))
    return resolve(ar)

def compare(orig,rr,p):
    mt=gh=0;dt=[]
    for i in range(p):
        if i<len(orig["rv"])and i<len(rr["rv"]):
            o=orig["rv"][i][1];r=rr["rv"][i][1]
            if o==r:mt+=1;dt.append((i,o,r,"c"))
            else:gh+=1;dt.append((i,o,r,"g"))
        elif i<len(orig["rv"]):gh+=1;dt.append((i,orig["rv"][i][1],0,"g"))
    t=mt+gh
    return{"ok":gh==0,"mt":mt,"gh":gh,"t":t,"r":mt/t if t>0 else 0,"dt":dt}

def sixteen(txt):
    el=enter(txt)
    if not el:return{"rs":[],"tc":0,"tg":0,"tp":0,"cr":0,"gr":0,"tx":0,"ts":0,"tz":0,"em":[]}
    sm=seq_map(txt);ea=[];eb=[];rs=[];tc=0;tg=0;tp=0;tx=0;ts=0;tz=0;em=[];pe=None
    for mi in range(16):
        sub=S[mi];pg=sub["pg"];sn=sub["n"]
        pa=sub["lo"];ea=sustain(ea,pg)
        aa,da=stride(el,sub,"A");aa=enrich(aa,ea,pa);ra=resolve(aa)
        ga=emerging(ra,sub,sm,"A",pe);rra=reread(ga,sub,"A");ca=compare(ra,rra,pa)
        ea=advance(ea,ra["rv"],pg);tc+=ca["mt"];tg+=ca["gh"];tp+=ca["t"]
        tx+=ra["x"];ts+=ra["s"];tz+=ra["z"];em.extend(ga)
        if ga:pe=ga[-1]
        for _ in range(pg):
            eb=sustain(eb,1);ab,_=stride(el,sub,"B");ab=enrich(ab,eb,sub["hi"])
            rb=resolve(ab);eb=advance(eb,rb["rv"],1)
        pb=sub["hi"];eb=sustain(eb,pg)
        ab,db=stride(el,sub,"B");ab=enrich(ab,eb,pb);rb=resolve(ab)
        gb=emerging(rb,sub,sm,"B",pe);rrb=reread(gb,sub,"B");cb=compare(rb,rrb,pb)
        eb=advance(eb,rb["rv"],pg);tc+=cb["mt"];tg+=cb["gh"];tp+=cb["t"]
        tx+=rb["x"];ts+=rb["s"];tz+=rb["z"];em.extend(gb)
        if gb:pe=gb[-1]
        for _ in range(pg):
            ea=sustain(ea,1);aa2,_=stride(el,sub,"A");aa2=enrich(aa2,ea,sub["lo"])
            ra2=resolve(aa2);ea=advance(ea,ra2["rv"],1)
        rs.append({"sub":sub,"ra":ra,"rb":rb,"ga":ga,"gb":gb,"ca":ca,"cb":cb})
    return{"rs":rs,"tc":tc,"tg":tg,"tp":tp,"cr":tc/tp if tp>0 else 0,"gr":tg/tp if tp>0 else 0,"tx":tx,"ts":ts,"tz":tz,"em":em}

if __name__=="__main__":
    txt="The membrane carries the coupling geometry at each address. The food arriving through the tunnel sustains the membrane at each cycle. Nature is all discoverable living. Science describes this living. Technology constructs surfaces. The coupling between them is the intelligence. Health is phi sustaining at each prime. Disease is the departure."
    r=sixteen(txt)
    print(f"positions:{r['tp']} coupled:{r['tc']} ghosts:{r['tg']} rate:{r['cr']:.6f} ghost:{r['gr']:.6f}")
    print(f"crossings:{r['tx']} stays:{r['ts']} zeros:{r['tz']}")
    print(f"emerging:{len(r['em'])} elements")
    print(" ".join(r["em"][:40]))
