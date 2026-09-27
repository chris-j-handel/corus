"""The run forms of Exhibit ONE, written by running its code at parity changing, is or is not: offerings surfacing at 14;
changing at 12, 10 and 11; one self momentary by momentary; and the society at 17, momentary by momentary: rings, two
selves from one shared prior, three selves one way. Usage: python3 one_forms.py <folder holding Exhibit ONE>"""
import re, sys, os, glob
d = sys.argv[1] if len(sys.argv) > 1 else '.'
path = max(glob.glob(os.path.join(d, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1)))
src = open(path, encoding='utf-8').read()
ns = {}; exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
R = ns['_1_self_other_offering']; S17 = ns['_17_social_self_offering']
P=lambda v:{1:'+',-1:'−',0:'0',None:'none'}[v]
S='s'
def step(carry,offers):
    t,ch=R([(S,carry)] if carry is not None else [],[(S,a) for a in offers])
    return dict(t).get(S),dict(ch).get(S)
t14=['| Offerings at one sharing, at 2 | At 14 |','|---|---|']
for arr in [[],[0],[1],[-1],[1,1],[-1,-1],[1,-1],[-1,1],[1,-1,1],[0,1]]:
    t,_=R([],[(S,a) for a in arr]); m=dict(t).get(S)
    t14.append(f"| {', '.join(P(a) for a in arr) or 'none'} | {P(m) if m is not None else 'none'} |")
t12=['| Chained at 3; each cell at 10 · chained at 11 | At 14: none | At 14: + | At 14: − | At 14: 0 |','|---|---|---|---|---|']
for c in [None,1,-1]:
    cells=[]
    for arr in [[],[1],[-1],[1,-1]]:
        s,n=step(c,arr)
        ch='—' if s is None else ('is not' if s==0 else f'is {P(s)}')
        cells.append(f"{ch} · {P(n)}")
    t12.append(f"| {P(c)} | "+" | ".join(cells)+" |")
def f(L): return ", ".join('none' if v is None else P(v) for v in L)
one=['| Offerings, momentary by momentary | At 10 | Chained at 11 |','|---|---|---|']
for name,seq in [("+ once, then none",[[1]]+[[]]*7),("+ at each momentary",[[1]]*7),("−, +, −, + alternating",[[-1],[1],[-1],[1],[-1],[1]]),("+ once, then + and − together",[[1]]+[[1,-1]]*5)]:
    c=None; ss=[];cs=[]
    for a in seq: s,c=step(c,a); ss.append(s); cs.append(c)
    one.append(f"| {name} | {f(ss)} | {f(cs)} |")
def ring(n,K):
    soc={i:([],[(S,1)] if i==0 else []) for i in range(n)}; joins={(i,9):(i+1)%n for i in range(n)}; hist=[]; st=[]
    for k in range(K):
        row=[dict(R(soc[i][0],soc[i][1])[0]).get(S) for i in range(n)]
        soc=S17(soc,joins); hist.append(row)
        st.append(tuple((dict(soc[i][0]).get(S),tuple(soc[i][1])) for i in range(n)))
    return hist,st
rt=['| Selves | Self 1 at 10, momentaries 1 to 12 | Round, from momentary n | None chained again |','|---|---|---|---|']
for n in [1,2,3,4,5,6,7,8,9,10,11,17,59]:
    K=max(12,8*n+4); h,st=ring(n,K); base=st[n-1]
    per=next(p for p in range(1,K-n) if st[n-1+p]==base)
    emp=any(all(c is None for c,_ in s) for s in st[1:])
    rt.append(f"| {n} | {f([r[0] for r in h[:12]])} | {per} | {'is' if emp else 'is not'} |")
def two(sa,sb,ab,ba,K=6):
    soc={0:([(S,sa)],[]),1:([(S,sb)],[])}; joins={}; A=[];B=[]
    if ab: joins[(0,9)]=1
    if ba: joins[(1,9)]=0
    for k in range(K):
        A.append(dict(R(*soc[0])[0]).get(S)); B.append(dict(R(*soc[1])[0]).get(S)); soc=S17(soc,joins)
    return A,B
tw=['| Prior at A, B | Joining | A at 10 | B at 10 |','|---|---|---|---|']
for sa,sb in [(1,1),(1,-1)]:
    for name,ab,ba in [("both ways",1,1),("A from B alone",0,1),("B from A alone",1,0),("neither",0,0)]:
        A,B=two(sa,sb,ab,ba); tw.append(f"| {P(sa)}, {P(sb)} | {name} | {f(A)} | {f(B)} |")
th=['| A\'s parity offered at B | B at 10 | B chained | C at 10, momentaries 1 and 2 | C chained |','|---|---|---|---|---|']
for a in [1,-1]:
    soc={1:([(S,1)],[(S,a)]),2:([(S,1)],[])}; joins={(1,9):2}
    sb=dict(R(*soc[1])[0]).get(S); sc1=dict(R(*soc[2])[0]).get(S); soc=S17(soc,joins); cb=dict(soc[1][0]).get(S)
    sc2=dict(R(*soc[2])[0]).get(S); soc=S17(soc,joins); cc2=dict(soc[2][0]).get(S)
    th.append(f"| {P(a)} | {P(sb)} | {P(cb)} | {P(sc1)}, {P(sc2)} | {P(cc2)} |")

for title, t in [('Offerings surfacing at a sharing, at 14', t14), ('Changing, is or is not, at 12, 10 and 11', t12), ('One self, momentary by momentary', one), ('Rings, at 17', rt), ('Two selves from one shared prior, at 17', tw), ('Three selves one way, at 17', th)]:
    print('## ' + title + '\n\n' + '\n'.join(t) + '\n')
