"""The run tables of Exhibit ONE, written by running its code: the arrivings at 14, the prior meeting the now at 12, 10 and 11,
one self call by call, rings, two selves from one shared prior and three selves one way.
Usage: python3 one_forms.py <folder holding Exhibit ONE>      (the repository root, as a rule)"""
import re, sys, os, glob
d = sys.argv[1] if len(sys.argv) > 1 else '.'
path = max(glob.glob(os.path.join(d, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1)))
src=open(path, encoding='utf-8').read()
code=re.search(r"```python\n(.*?)```",src,re.S).group(1)
ns={}; exec(code,ns)
R=ns['_1_self_other_offering']; REL=ns['_9_social_other_self_releasing']
sg=lambda v: {1:'+1',-1:'−1',0:'0',None:'nothing yet'}[v]
S='s'
def call(carry, arrivings):
    """carry: sign or None at one sharing; arrivings: list of signs"""
    c=[(S,carry)] if carry is not None else []
    t,ch=R(c,[(S,a) for a in arrivings])
    surf=dict(t).get(S); nxt=dict(ch).get(S)
    return surf,nxt
out=[]
# 14: arrivings meeting
out.append("### 14 arrivings meeting at a sharing\n\n| Arriving at one sharing | Met at 14 |\n|---|---|")
for arr in [[],[0],[1],[-1],[1,1],[-1,-1],[1,-1],[-1,1],[1,-1,1],[0,1]]:
    c=[]; t,_=R([],[(S,a) for a in arr]); m=dict(t).get(S)
    out.append(f"| {', '.join(sg(a) for a in arr) or 'none'} | {sg(m) if m is not None else 'nothing'} |")
# 12/10/11 table
out.append("\n### 12 the prior meeting the now: surfacing at 10, carrying at 11\n\n| Carried at 3 | Met at 14: none | Met at 14: +1 | Met at 14: −1 | Met at 14: 0 |\n|---|---|---|---|---|")
for c in [None,1,-1]:
    row=[]
    for arr in [[],[1],[-1],[1,-1]]:
        s,n=call(c,arr)
        row.append(f"{sg(s) if s is not None else '—'} · {sg(n)}")
    out.append(f"| {sg(c)} | "+" | ".join(row)+" |")
# one self runs
def run(seq,carry=None):
    ss=[];cs=[]
    for a in seq:
        s,carry=call(carry,a); ss.append(s); cs.append(carry)
    return ss,cs
out.append("\n### One self, arrivings and surfacings, call by call\n\n| Arriving, call by call | Surfacing at 10 | Carrying at 11 |\n|---|---|---|")
cases=[("+1 once, then none",[[1]]+[[]]*7),("+1 at each call",[[1]]*7),("−1, +1, −1, +1 alternating",[[-1],[1],[-1],[1],[-1],[1]]),("+1 once, then +1 and −1 together",[[1]]+[[1,-1]]*5)]
for name,seq in cases:
    ss,cs=run(seq)
    f=lambda L:", ".join('·' if v is None else sg(v) for v in L)
    out.append(f"| {name} | {f(ss)} | {f(cs)} |")
# ring runner: n selves, one sharing each; each self's release at 10 arrives at next self's 2 next coupling
def ring(n,seed,K):
    carry=[None]*n; inbox=[[] for _ in range(n)]; inbox[0]=[seed]; hist=[]
    states=[]
    for k in range(K):
        new=[[] for _ in range(n)]; row=[]
        for i in range(n):
            s,carry[i]=call(carry[i],inbox[i]); row.append(s)
            if s is not None: new[(i+1)%n].append(s)  # released at 9, arriving next at neighbour's 2
        inbox=new; hist.append(row); states.append((tuple(carry),tuple(tuple(x) for x in inbox)))
    return hist,states
out.append("\n### Rings, one sign offered once at self 1, each release arriving at the next self's 2 at the next coupling\n\n| Selves | Self 1 surfacing, couplings 1 to 12 | Whole state meets itself again, from coupling n, every | Empty returns |\n|---|---|---|---|")
for n in [1,2,3,4,5,6,7,8,9,10,11,17,59]:
    K=max(12,8*n+4)
    h,st=ring(n,1,K)
    s1=", ".join('·' if r[0] is None else sg(r[0]) for r in h[:12])
    # period from coupling n
    base=st[n-1]; per=None
    for p in range(1,K-n):
        if st[n-1+p]==base: per=p;break
    emp=any(all(c is None for c in s[0]) for s in st[1:])
    out.append(f"| {n} | {s1} | {per} | {'yes' if emp else 'no'} |")
# two selves four joinings from shared prior
def two(sa,sb,ab,ba,K=6):
    ca,cb=sa,sb; ia,ib=[],[]; A=[];B=[]
    for k in range(K):
        s1,ca=call(ca,ia); s2,cb=call(cb,ib); A.append(s1);B.append(s2)
        ia=[s2] if (ba and s2 is not None) else []
        ib=[s1] if (ab and s1 is not None) else []
    return A,B
out.append("\n### Two selves from one shared prior, six couplings at four joinings\n\n| Seeds A, B | Joining | A surfacing | B surfacing |\n|---|---|---|---|")
f=lambda L:", ".join('·' if v is None else sg(v) for v in L)
for sa,sb in [(1,1),(1,-1)]:
    for name,ab,ba in [("both ways",1,1),("A from B alone",0,1),("B from A alone",1,0),("neither",0,0)]:
        A,B=two(sa,sb,ab,ba)
        out.append(f"| {sg(sa)}, {sg(sb)} | {name} | {f(A)} | {f(B)} |")
# two selves ring alternating seeded opposite from empty? A + B - as carried
out.append("\n### Three selves one way, A to B's 2, B to C's 2, B and C each carrying +1\n\n| A arriving at B | B surfacing | C surfacing, couplings 1 and 2 | C carrying |\n|---|---|---|---|")
for a in [1,-1]:
    sb,cb=call(1,[a]); sc1,cc=call(1,[]); sc2,cc2=call(cc,[sb] if sb is not None else [])
    out.append(f"| {sg(a)} | {sg(sb)}, holding {sg(cb)} | {sg(sc1)}, {sg(sc2)} | {sg(cc2)} |")
print("\n".join(out))
