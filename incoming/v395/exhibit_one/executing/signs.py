import importlib.util, random, itertools, collections
spec=importlib.util.spec_from_file_location('r','resolver.py'); r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
neg=lambda L:[(k,-v) for k,v in L]
# 1) every case of one sharing: flipping each sign flips each output, and changing / not changing is the same
same=0;tot=0
for prior in (1,-1,None):
    for n in range(4):
        for rec in itertools.product((1,-1,0),repeat=n):
            th=[('s',prior)] if prior else []; tw=[('s',p) for p in rec]
            a=r._1_now_existing(th,tw); b=r._1_now_existing(neg(th),neg(tw))
            tot+=1; same+= (neg(a[0])==b[0] and neg(a[1])==b[1])
print("one sharing, every case: outputs inverting with each sign inverting:",same,"of",tot)
# 2) a society bi-coupling at random, many momentaries: each self's changing / not changing, run and its sign-inverted run
rng=random.Random(7); agree=0; runs=0
for t in range(300):
    n=rng.randint(2,7); edges={i:rng.sample([j for j in range(n) if j!=i],rng.randint(1,min(3,n-1))) for i in range(n)}
    pri={i:[('s',rng.choice((1,-1)))] for i in range(n)}
    def run(pri):
        P=dict(pri); inbox={i:[] for i in range(n)}; trace=[]
        for m in range(10):
            out={}; nxt={}
            for i in range(n): out[i],nxt[i]=r._1_now_existing(P[i],inbox[i])
            trace.append(tuple('same' if dict(P[i]).get('s')==dict(nxt[i]).get('s') else 'changing' for i in range(n)))
            inbox={i:[] for i in range(n)}
            for i in range(n):
                for j in edges[i]: inbox[j]+= out[i]
            P=nxt
        return trace
    a=run(pri); b=run({i:neg(v) for i,v in pri.items()}); runs+=1; agree+=(a==b)
print("societies of 2 to 7 selves, 10 momentaries: each self's same / changing alike in a run and its sign-inverted run:",agree,"of",runs)
# 3) one self's signs alone inverted: same / changing parts
part=0
for t in range(300):
    n=4; edges={i:[(i+1)%n,(i+2)%n] for i in range(n)}
    pri={i:[('s',rng.choice((1,-1)))] for i in range(n)}
    a=run(pri); p2=dict(pri); p2[0]=neg(p2[0]); b=run(p2); part+=(a!=b)
print("one self's sign alone inverted, a society's same / changing parting:",part,"of 300")
