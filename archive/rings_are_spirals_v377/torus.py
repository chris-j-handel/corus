body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']
def torus(p,q,steps):
    ks=[(i,j) for i in range(p) for j in range(q)]
    comp={}
    for i,j in ks: comp[((i,j),9)]=((i+1)%p,j); comp[((i,j),10)]=(i,(j+1)%q)
    soc={k:([('s',1)] if k==(0,0) else [],[]) for k in ks}
    seq=[]
    for t in range(steps):
        soc=F(soc,comp); seq.append(tuple(dict(soc[k][0]).get('s',0) for k in ks))
    return seq
def rnd(seq):
    n=len(seq)
    for start in range(0,n//2):
        for p in range(1,(n-start)//2):
            if all(seq[t]==seq[t+p] for t in range(start,n-p)): return p,start
for p,q,st in [(3,5,200),(5,3,200),(3,7,200),(5,7,300),(17,59,400)]:
    print(p,q,rnd(torus(p,q,st)))
