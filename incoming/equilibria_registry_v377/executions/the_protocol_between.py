"""The between as the bi-moral-co-competencing protocol at Exhibit ONE's code: the four corner dots 2, 6, 14 and 10 across, the along 9 and 17 through the empty centre, unchanging, between momentaries and between the parity changings inside each momentary. Run from the repository root."""
import copy
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read(); ns={}
exec(body.split('```python',1)[1].split('```',1)[0],ns)
O=ns['_1_co_bi_offering']; F=ns['_17_tri_co_offering']
print('1. the protocol at the code, CONNECTORS and JOINS:')
for k,v in sorted(ns['CONNECTORS'].items()): print(f'   {k}: {v[0]}, {v[1]}, {v[2]}', '· across, a corner dot' if k in (2,6,10,14) else '· along, through the empty centre')
print('   JOINS:',ns['JOINS'])
n=5
comp={}
for i in range(n): comp[(i,9)]=(i+1)%n; comp[(i,6)]=(i+2)%n; comp[(i,10)]=(i+3)%n
soc0={i:([],[('s',1)] if i==0 else []) for i in range(n)}
before=copy.deepcopy((ns['CONNECTORS'],ns['JOINS'],comp))
soc=soc0; pat=[]
for t in range(100):
    soc=F(soc,comp); pat.append(tuple(dict(soc[i][0]).get('s',0) for i in range(n)))
print('2. across 100 momentaries the protocol is unchanged, CONNECTORS, JOINS and the society\'s joins:', before==(ns['CONNECTORS'],ns['JOINS'],comp),'; the carryings changed at',sum(pat[t]!=pat[t-1] for t in range(1,100)),'of 99 momentaries')
print('3. inside one momentary each self makes its own changing at its own 12, and a changing reaches another self only through a join at 6, 10 or 9:')
soc={i:([('s',1 if i%2 else -1)],[]) for i in range(n)}
routes={}
for i,(c3,o2) in soc.items():
    t10,_=O(c3,o2)
    for c in (6,10,9):
        j=comp.get((i,c))
        if j is not None: routes.setdefault(j,[]).append((i,c,dict(t10).get('s')))
nxt=F(soc,comp)
ok=all(sorted(p for _,p in nxt[j][1])==sorted(v for _,_,v in routes.get(j,[])) for j in range(n))
print('   each self\'s offerings at the next momentary are exactly the changings arriving through its joins:',ok)
for j in range(n): print(f'   self {j} offered {[p for _,p in nxt[j][1]]} from {[(i,c) for i,c,_ in routes.get(j,[])]}')
print('4. the protocol taken away, no joins: each self carries its prior inverted alone, and no self\'s changing reaches another')
soc=soc0; alone=[]
for t in range(8):
    soc=F(soc,{}); alone.append(tuple(dict(soc[i][0]).get('s',0) for i in range(n)))
print('  ',alone)
