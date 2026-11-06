import importlib.util, itertools, collections
spec=importlib.util.spec_from_file_location('r','resolver.py'); r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
# 1) during possibling: with a parity surfacing, is the next prior that parity? with none or parting, what?
c=collections.Counter()
for prior in (1,-1,None):
    for n in range(4):
        for rec in itertools.product((1,-1,0),repeat=n):
            surf=None
            for p in rec:
                if p!=0:
                    if surf is None: surf=1 if p>0 else -1
                    elif (surf>0)!=(p>0): surf=0
            th=[('s',prior)] if prior else []
            ten,el=r._1_now_existing(th,[('s',p) for p in rec]); nx=dict(el).get('s')
            if surf in (1,-1): c[('a parity surfacing','next prior same as it' if nx==surf else 'next prior other than it')]+=1
            elif prior: c[('parting or none, with a prior','next prior its prior inverting' if nx==-prior else '?')]+=1
            else: c[('parting or none, no prior','next prior '+('empty' if nx is None else str(nx)))]+=1
for k,v in sorted(c.items()): print(v,k)
# 2) two selves bi-coupling across both ways: each self's changing per momentary, inversionings at the across, their relation
def pair(pa,pb,m=8):
    a=[('s',pa)]; b=[('s',pb)]; ta=[]; tb=[]; rows=[]
    for _ in range(m):
        na,ea=r._1_now_existing(a,tb); nb,eb=r._1_now_existing(b,ta)
        ca=dict(a)['s']!=dict(ea)['s']; cb=dict(b)['s']!=dict(eb)['s']
        rel='alike' if dict(ea)['s']==dict(eb)['s'] else 'opposite'
        rows.append((int(ca)+int(cb),rel)); a,b,ta,tb=ea,eb,na,nb
    return rows
print("opposite priors:",pair(1,-1)); print("alike priors:   ",pair(1,1))
import random
rng=random.Random(3); cnt=collections.Counter(); closed=collections.Counter()
for t in range(300):
    n=rng.randint(3,7); edges={i:set() for i in range(n)}
    a0,b0=0,1; edges[0].add(1); edges[1].add(0)            # one across both ways
    for i in range(n):
        for j in rng.sample(range(n),rng.randint(0,2)):
            if j!=i: edges[i].add(j)
    only_pair = all(0 not in edges[k] and 1 not in edges[k] for k in range(2,n))
    P={i:[('s',rng.choice((1,-1)))] for i in range(n)}; inbox={i:[] for i in range(n)}
    for m in range(10):
        out={}; nx={}
        for i in range(n): out[i],nx[i]=r._1_now_existing(P[i],inbox[i])
        k=int(dict(P[0])['s']!=dict(nx[0])['s'])+int(dict(P[1])['s']!=dict(nx[1])['s'])
        (closed if (only_pair and not (edges[0]-{1}) and not (edges[1]-{0})) else cnt)[k]+=1
        inbox={i:[] for i in range(n)}
        for i in range(n):
            for j in edges[i]: inbox[j]+=out[i]
        P=nx
print("an across both ways within a society, inversionings at its two sides per momentary:",dict(cnt))
print("an across both ways, its two selves bi-coupling with no further self:",dict(closed))
