"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/bound_611.py
"""
import re, itertools, random
t=open('Exhibit_ONE_Natural_Resolver_v380R.md').read()
ns={}
exec(re.search(r"```python\n(.*?)```", t, re.S).group(1), ns)
_1=ns['_1_co_bi_tri_offering']
def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]

def run_async(selves, joins, opening, entries, rng, preload=None, selfloops=True):
    c=dict(opening); waiting={s:[] for s in selves}
    if preload:
        for s,l in preload.items(): waiting[s]=list(l)
    run={s:1 for s in selves}; most={s:1 for s in selves}
    for i in range(entries):
        s=rng.choice(selves)
        offered, waiting[s] = waiting[s], []
        new,o=entry(c[s],offered)
        run[s]= run[s]+1 if new==c[s] else 1
        most[s]=max(most[s],run[s]); c[s]=new
        for to in joins[s]: waiting[to].append(o)
    return most

rng=random.Random(11)
viol=0; tot=0; ex=None
for trial in range(4000):
    n=rng.randint(1,6)
    selves=list(range(n))
    # allow self-loops, allow no multi-edges
    joins={s: rng.sample(selves, rng.randint(0,min(4,n))) for s in selves}
    k={s:sum(s in joins[u] for u in selves) for s in selves}
    op={s:rng.choice((1,-1)) for s in selves}
    most=run_async(selves,joins,op,400*n,rng)
    for s in selves:
        tot+=1
        if most[s]>k[s]+1:
            viol+=1
            if ex is None: ex=(joins,op,s,most[s],k[s])
print("async, self-loops allowed, random graphs:",tot,"selves; violations",viol,ex)

# Gap probe: preloaded offerings waiting from before the first entry
viol=0; tot=0; ex=None
for trial in range(4000):
    n=rng.randint(1,5)
    selves=list(range(n))
    joins={s: rng.sample([u for u in selves if u!=s], rng.randint(0,min(3,n-1))) for s in selves}
    k={s:sum(s in joins[u] for u in selves) for s in selves}
    op={s:rng.choice((1,-1)) for s in selves}
    preload={s:[rng.choice((1,-1,0)) for _ in range(rng.randint(0,3))] for s in selves}
    most=run_async(selves,joins,op,400*n,rng,preload=preload)
    for s in selves:
        tot+=1
        if most[s]>k[s]+1:
            viol+=1
            if ex is None: ex=(joins,op,preload,s,most[s],k[s])
print("preloaded offerings from before first entry:",tot,"selves; violations",viol,ex)
