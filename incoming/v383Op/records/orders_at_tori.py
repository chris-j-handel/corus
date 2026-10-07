"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/orders_at_tori.py
"""
import glob, re, random, itertools, collections
exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]
# 0 vs none equivalence
for c in (1,-1):
    for offs in ([],[0],[0,0],[1],[-1],[0,1],[0,-1],[1,-1],[1,1],[1,0]):
        print(c,offs,entry(c,offs))

def senders(p, q, s):
    i, j = s
    return ((i - 1) % p, j), (i, (j - 1) % q)

def beat(p,q,c,last):
    new=dict(c); shared={}
    for s in c:
        two=[last.get(u,0) for u in senders(p,q,s)]
        new[s],shared[s]=entry(c[s],two)
    return new,shared

def one_at_a_time(p,q,opening,momentaries,take,seed,deliver_zero=True,lockstep=False):
    r=random.Random(seed)
    selves=[(i,j) for i in range(p) for j in range(q)]
    waiting={s:{u:[] for u in senders(p,q,s)} for s in selves}
    c=dict(opening); seq={s:[] for s in selves}
    def can(s):
        if len(seq[s])>=momentaries: return False
        if not seq[s]: return True
        ready=[bool(waiting[s][u]) for u in senders(p,q,s)]
        return all(ready) if take=='each' else any(ready)
    rounds=0
    while True:
        ready=[s for s in selves if can(s)]
        if not ready: break
        if lockstep:
            # run every ready self once in list order per round
            s=ready[0]
        else:
            s=r.choice(ready)
        if not seq[s]: offered=[]
        elif take=='each': offered=[waiting[s][u].pop(0) for u in senders(p,q,s)]
        else: offered=[waiting[s][u].pop(0) for u in senders(p,q,s) if waiting[s][u]]
        c[s],o=entry(c[s],offered)
        seq[s].append((c[s],o))
        i,j=s
        if deliver_zero or o!=0:
            for to in (((i+1)%p,j),(i,(j+1)%q)):
                waiting[to][s].append(o)
    return seq

res=collections.Counter()
for (p,q) in ((2,3),(3,3),(3,4),(3,7),(5,5)):
    selves=[(i,j) for i in range(p) for j in range(q)]
    r=random.Random(383)
    for trial in range(60):
        opening={s:r.choice((1,-1)) for s in selves}
        c,last,ref=dict(opening),{},{s:[] for s in selves}
        for _ in range(40):
            c,last=beat(p,q,c,last)
            for s in selves: ref[s].append((c[s],last[s]))
        for seed in (trial,1000+trial):
            res['runs']+=1
            for take in ('each','any'):
                got=one_at_a_time(p,q,opening,40,take,seed)
                res[take]+=all(got[s]==ref[s] for s in selves)
                # same completeness
                res[take+'_complete']+=all(len(got[s])==40 for s in selves)
            # any with lockstep
            got=one_at_a_time(p,q,opening,40,'any',seed,lockstep=True)
            res['any_lockstep']+=all(got[s]==ref[s] for s in selves)
            # absence: zero not delivered, 'any'
            got=one_at_a_time(p,q,opening,40,'any',seed,deliver_zero=False)
            res['any_zero_absent']+=all(got[s]==ref[s] for s in selves)
            res['any_zero_absent_complete']+=all(len(got[s])==40 for s in selves)
            # absence, 'each' (blocking)
            got=one_at_a_time(p,q,opening,40,'each',seed,deliver_zero=False)
            res['each_zero_absent']+=all(got[s]==ref[s] for s in selves)
            res['each_zero_absent_complete']+=all(len(got[s])==40 for s in selves)
print(dict(res))

def rounds_run(p,q,opening,momentaries,take,order_seed):
    r=random.Random(order_seed)
    selves=[(i,j) for i in range(p) for j in range(q)]
    waiting={s:{u:[] for u in senders(p,q,s)} for s in selves}
    c=dict(opening); seq={s:[] for s in selves}
    for t in range(momentaries):
        order=selves[:]; r.shuffle(order)
        for s in order:
            if not seq[s]: offered=[]
            else: offered=[waiting[s][u].pop(0) for u in senders(p,q,s) if waiting[s][u]]
            c[s],o=entry(c[s],offered)
            seq[s].append((c[s],o))
            i,j=s
            for to in (((i+1)%p,j),(i,(j+1)%q)):
                waiting[to][s].append(o)
    return seq
res2=collections.Counter()
for (p,q) in ((2,3),(3,3),(3,4),(3,7),(5,5)):
    selves=[(i,j) for i in range(p) for j in range(q)]
    r=random.Random(383)
    for trial in range(60):
        opening={s:r.choice((1,-1)) for s in selves}
        c,last,ref=dict(opening),{},{s:[] for s in selves}
        for _ in range(40):
            c,last=beat(p,q,c,last)
            for s in selves: ref[s].append((c[s],last[s]))
        for seed in (trial,1000+trial):
            res2['runs']+=1
            got=rounds_run(p,q,opening,40,'any',seed)
            res2['any_in_shuffled_rounds']+=all(got[s]==ref[s] for s in selves)
print(dict(res2))

# fraction of entries matching under 'any' random order, and first divergence
import statistics
fr=[];first=[]
for (p,q) in ((2,3),(3,3),(3,4),(3,7),(5,5)):
    selves=[(i,j) for i in range(p) for j in range(q)]
    r=random.Random(383)
    for trial in range(60):
        opening={s:r.choice((1,-1)) for s in selves}
        c,last,ref=dict(opening),{},{s:[] for s in selves}
        for _ in range(40):
            c,last=beat(p,q,c,last)
            for s in selves: ref[s].append((c[s],last[s]))
        got=one_at_a_time(p,q,opening,40,'any',trial)
        tot=sum(1 for s in selves for k in range(40) if got[s][k]==ref[s][k])
        fr.append(tot/(40*len(selves)))
        fd=min((k for s in selves for k in range(40) if got[s][k]!=ref[s][k]),default=40)
        first.append(fd+1)
print('mean fraction of entries equal under any:',statistics.mean(fr),'min',min(fr),'max',max(fr))
print('first diverging momentary: mean',statistics.mean(first),'min',min(first),'max',max(first))
