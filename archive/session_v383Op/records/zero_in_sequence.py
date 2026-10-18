"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/zero_in_sequence.py
"""
import glob, re, random, collections
exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]
def senders(p,q,s):
    i,j=s
    return ((i-1)%p,j),(i,(j-1)%q)
def run(p,q,op,T):
    selves=[(i,j) for i in range(p) for j in range(q)]
    c=dict(zip(selves,op)); last={}
    mx=0; run_len={s:0 for s in selves}
    for t in range(T):
        new={};sh={}
        for s in selves:
            two=[last.get(u,0) for u in senders(p,q,s)]
            new[s],sh[s]=entry(c[s],two)
        c,last=new,sh
        for s in selves:
            run_len[s]=run_len[s]+1 if last[s]==0 else 0
            mx=max(mx,run_len[s])
    return mx
r=random.Random(5)
for (p,q) in ((3,5),(5,7),(3,13),(5,13),(13,15),(1,5),(3,3),(1,7)):
    res=collections.Counter()
    for _ in range(40 if p*q>60 else 300):
        op=[r.choice((1,-1)) for _ in range(p*q)]
        res[run(p,q,op,200 if p*q>60 else 120)]+=1
    print((p,q),dict(res))
