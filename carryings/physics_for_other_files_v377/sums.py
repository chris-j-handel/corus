"""Societies of 6 to 12 selves, each joined along at 9 to one random self and across at 10 to another, carryings at random + or -: does the sum of the carried parities stay the same momentary by momentary? Run from the repository root."""
import random
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']
random.seed(377); stays=changes=0; stay_sym=0
for trial in range(500):
    n=random.randint(6,12); ks=list(range(n)); comp={}
    for i in ks:
        comp[(i,9)]=random.choice([k for k in ks if k!=i]); comp[(i,10)]=random.choice([k for k in ks if k!=i])
    soc={i:([('s',random.choice([1,-1]))],[]) for i in ks}
    sums=[]
    for t in range(60):
        soc=F(soc,comp); sums.append(sum(dict(soc[i][0]).get('s',0) for i in ks))
    if len(set(sums[10:]))==1: stays+=1
    else: changes+=1
print(f"500 societies: the sum changes at {changes}, stays at {stays}")
for n in [4,5,6,7]:
    ks=list(range(n)); comp={(i,9):(i+1)%n for i in ks}
    soc={i:([('s',1)] if i==0 else [],[]) for i in ks}; s=[]
    for t in range(4*n+n): soc=F(soc,comp); s.append(sum(dict(soc[i][0]).get('s',0) for i in ks))
    print(f"spiral of {n}: sums {s[n:n+8]}")
