"""The torus of selves at the code, and the white paper 4.13's waist rule. Run from the repository root."""
from math import gcd
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
def again(seq):
    n=len(seq)
    for start in range(0,n//2):
        for p in range(1,(n-start)//2):
            if all(seq[t]==seq[t+p] for t in range(start,n-p)): return p
for p,q in [(1,3),(1,5),(1,9),(3,5),(3,7),(3,9),(3,11),(3,13),(3,15),(3,27),(5,7),(5,11),(5,15),(5,21),(5,25),(9,15)]:
    r=again(torus(p,q,8*max(p,q)+60)); rule=4*p if q<2*p else q
    print(f"{p} by {q}: gcd {gcd(p,q)}, parities again every {r} momentaries; the waist rule says {rule}; {'meets' if r==rule else 'parts'}")
