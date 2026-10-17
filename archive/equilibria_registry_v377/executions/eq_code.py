"""The Equilibria Registry's sayings at Exhibit ONE v376's code. Run from the repository root."""
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read(); ns={}
exec(body.split('```python',1)[1].split('```',1)[0],ns)
O=ns['_1_co_bi_offering']; F=ns['_17_tri_co_offering']
def spiral(n,steps,seed_self=0):
    # one + offered once at one self, the others at none, as Exhibit ONE's table of selves, lines 263-277
    comp={(i,9):(i+1)%n for i in range(n)}
    soc={i:([],[('s',1)] if i==seed_self else []) for i in range(n)}
    rel=[];ch=[]
    for t in range(steps):
        # the changings released at 10 this momentary, per self, read from _1 directly
        r=[]
        for i in range(n):
            t10,_=O(*soc[i]); r.append(dict(t10).get('s'))
        soc=F(soc,comp); rel.append(r); ch.append(tuple(dict(soc[i][0]).get('s',0) for i in range(n)))
    return rel,ch
print('1. spirals, one + offered once at one self and the others at none')
for n in [1,2,3,4,5,6,7]:
    rel,ch=spiral(n,12)
    print(f'  n={n} released at 10 by self 0, momentaries 1-12:',[ {1:'+',-1:'-',0:'0',None:'.'}[r[0]] for r in rel])
print('   the 0 at 10 in a spiral of five, momentary by momentary, at which self:')
rel,ch=spiral(5,24)
print('  ',[ [i for i,x in enumerate(r) if x==0] for r in rel[4:24]])
print('2. rest: does any spiral of 1 to 11 come to every self releasing nothing or 0, in 5,000 momentaries; does each self change within 40')
for n in range(1,12):
    rel,ch=spiral(n,5000)
    # rest: no self's changing is, at each of the last 100 of the 5,000 momentaries
    rest= all(all(x in (0,None) for x in r) for r in rel[-100:])
    first=[next((t for t,r in enumerate(rel) if r[i] not in (0,None)),None) for i in range(n)]
    print(f'  n={n}: rest met {rest}; each self first changes by momentary {max(first)+1}')
print('3. a carrying named unchanged: chained +, offered + at five momentaries, then nothing')
c=[('s',1)];out=[]
for off in [[1]]*5+[[]]*5:
    t,c=O(c,[('s',p) for p in off]); out.append((dict(t).get('s'),dict(c).get('s')))
print('  (released at 10, chained at 11):',out)
print('4. 6 and 10 at the code: the same changing released at both')
import inspect
src=body.split('```python',1)[1].split('```',1)[0]
print('  ', [l.strip() for l in src.split('\n') if '_6_bi_moralizing =' in l])
print('5. a carrying once chained is never none again (Exhibit ONE, "None chained again: is not")')
c=[];seen=[]
for off in [[1]]+[[]]*9+[[1,-1]]*5:
    t,c=O(c,[('s',p) for p in off]); seen.append(dict(c).get('s'))
print('  chained at 11:',seen)
print('6. a carried sharing whose offerings part to 0 at 14 at each momentary')
c=[('s',1)];out=[]
for k in range(6):
    t,c=O(c,[('s',1),('s',-1)]); out.append((dict(t).get('s'),dict(c).get('s')))
print('  (released at 10, chained at 11):',out)
print('7. at the numbers: maps on the four pairs whose square is J(c,t)=(-c,-t)')
import itertools
P=[(1,1),(1,-1),(-1,1),(-1,-1)]
J={p:(-p[0],-p[1]) for p in P}
found=[]
for perm in itertools.product(P,repeat=4):
    f=dict(zip(P,perm))
    if all(f[f[p]]==J[p] for p in P): found.append(f)
print('  maps from the four pairs to themselves with f(f(p)) = J(p):',len(found))
Fm={p:(-p[1],p[0]) for p in P}; Gm={p:(p[1],-p[0]) for p in P}
print('  F(c,t)=(-t,c) among them:',Fm in found,'  G(c,t)=(t,-c) among them:',Gm in found)
print('8. at the numbers: F(P,Q)=(-Q,P) leaves each nonempty proper subset of the four pairs')
ok=True
for r in range(1,4):
    for S in itertools.combinations(P,r):
        S=set(S)
        if all(Fm[p] in S for p in S): ok=False
print('  no nonempty proper subset carried into itself:',ok)
print('9. at the numbers: advancing the overlapping triple, 010 to 101 and 101 to 010')
adv=lambda s: ''.join('1' if ch=='0' else '0' for ch in s)
print('  ',adv('010'),adv('101'))
print("10. an odd spiral: the whole, each self's chained parity and its offerings, inverted at 2n momentaries and met again first at 4n, from the nth")
def spiral_states(n,steps):
    comp={(i,9):(i+1)%n for i in range(n)}
    soc={i:([],[('s',1)] if i==0 else []) for i in range(n)}
    st=[]
    for t in range(steps):
        soc=F(soc,comp)
        st.append(tuple((dict(soc[i][0]).get('s',0), tuple(p for _,p in soc[i][1])) for i in range(n)))
    return st
inv=lambda state: tuple((-c, tuple(-p for p in offs)) for c,offs in state)
for n in [3,5,7,9,11]:
    st=spiral_states(n,20*n); b=st[n]
    first=next(k for k in range(1,10*n) if st[n+k]==b)
    print(f'  n={n}: at n+2n inverted {st[n+2*n]==inv(b)}; first met again after {first} momentaries')
print('11. a self offered nothing: its release at 10 and its carrying chained at 11 are one changing')
c=[('s',1)];rows=[]
for k in range(6):
    t,c=O(c,[]); rows.append((dict(t).get('s'),dict(c).get('s')))
print('  (released at 10, chained at 11):',rows)
print('12. a changing released along at 9 arrives at the receiving self as its offering at the next momentary')
comp={(0,9):1}
soc={0:([],[('s',1)]),1:([],[])}
for t in range(3):
    print(f'  momentary {t+1}: self 1 offered {soc[1][1]}')
    soc=F(soc,comp)
