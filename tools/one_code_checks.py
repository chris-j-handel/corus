import random
"""Checks at Exhibit ONE's code: the society at 17, momentary by momentary, gives exactly what each self's 1 and 9
composed by hand give, at rings of 1 to 59 joined along at 9 and across at 10 and 6, at two selves at each prior and
joining, and at 3,000 societies of one to seven selves at several sharings. Usage: python3 one_code_checks.py <folder>"""
import re, sys, os, glob
d = sys.argv[1] if len(sys.argv) > 1 else '.'
path = max(glob.glob(os.path.join(d, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1)))
ns={}; exec(re.search(r"```python\n(.*?)```", open(path, encoding='utf-8').read(), re.S).group(1), ns)
R=ns['_1_self_other_offering']; S17=ns['_17_social_self_offering']; REL=ns['_9_social_other_self_releasing']
def sfc(t): return dict(t).get('s')
# flat hand composition: each self's 10 passed to receivers' 2 at next momentary
def hand(n, joins, carry0, offers0, K):
    carry=list(carry0); inbox=[list(x) for x in offers0]; H=[]
    for k in range(K):
        new=[[] for _ in range(n)]; row=[]
        for i in range(n):
            t,c=R(carry[i],inbox[i]); carry[i]=c; row.append(sfc(t))
            for (a,conn),b in joins.items():
                if a==i: new[b].extend(t)
        inbox=new; H.append((row,[tuple(c) for c in carry]))
    return H
def soc(n, joins, carry0, offers0, K):
    st={i:(list(carry0[i]),list(offers0[i])) for i in range(n)}; H=[]
    for k in range(K):
        # surfacing seen by running each self's 1 as 17 does
        row=[sfc(R(st[i][0],st[i][1])[0]) for i in range(n)]
        st=S17(st,joins)
        H.append((row,[tuple(st[i][0]) for i in range(n)]))
    return H
ok=True
# rings, along at 9
for n in [1,2,3,4,5,6,7,8,9,10,11,17,59]:
    j={(i,9):(i+1)%n for i in range(n)}
    c0=[[] for _ in range(n)]; o0=[[('s',1)]]+[[] for _ in range(n-1)]
    a=hand(n,j,c0,o0,8*n+4); b=soc(n,j,c0,o0,8*n+4); ok&=(a==b)
    # across at 10 and at 6 alike
    for conn in (10,6):
        j2={(i,conn):(i+1)%n for i in range(n)}; ok&=(soc(n,j2,c0,o0,8*n+4)==a)
print('rings identical, along 9 and across 10 and 6:',ok)
# two selves, four joinings, priors alike and opposite, all seeds
ok2=True
for sa in (1,-1):
  for sb in (1,-1):
    for j in [{(0,9):1,(1,9):0},{(1,9):0},{(0,9):1},{}, {(0,10):1,(1,6):0}]:
        c0=[[('s',sa)],[('s',sb)]]; o0=[[],[]]
        ok2&=hand(2,j,c0,o0,6)==soc(2,j,c0,o0,6)
print('two selves identical:',ok2)
# random societies: random joins over 6 connectors-ish, random priors and offerings, several sharings
random.seed(7); ok3=True; runs=0
for trial in range(3000):
    n=random.randint(1,7); conns=[6,9,10]
    j={}
    for i in range(n):
        for c in conns:
            if random.random()<0.5: j[(i,c)]=random.randrange(n)
    sh=['a','b','c']
    c0=[[(s,random.choice([1,-1])) for s in sh if random.random()<0.5] for _ in range(n)]
    o0=[[(random.choice(sh),random.choice([1,-1,0])) for _ in range(random.randint(0,3))] for _ in range(n)]
    def hand2(K):
        carry=[list(c) for c in c0]; inbox=[list(o) for o in o0]; H=[]
        for k in range(K):
            new=[[] for _ in range(n)]
            for i in range(n):
                t,c=R(carry[i],inbox[i]); carry[i]=c
                for (a,conn),b in j.items():
                    if a==i: new[b].extend(t)
            inbox=new; H.append([sorted(c) for c in carry])
        return H
    def soc2(K):
        st={i:(list(c0[i]),list(o0[i])) for i in range(n)}; H=[]
        for k in range(K):
            st=S17(st,j); H.append([sorted(st[i][0]) for i in range(n)])
        return H
    ok3&=hand2(12)==soc2(12); runs+=1
print('random societies identical to composing by hand:',ok3, runs)
