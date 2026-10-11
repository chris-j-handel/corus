"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/one_other_drawn.py
"""
import re, itertools, random, sys
t=open('Exhibit_ONE_Natural_Resolver_v380R.md').read()
ns={}
exec(re.search(r"```python\n(.*?)```", t, re.S).group(1), ns)
_1=ns['_1_co_bi_tri_offering']
def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]
def together(selves, joins, opening, T):
    c = dict(opening); arriving = {s: [] for s in selves}; C = {s: [c[s]] for s in selves}
    for _ in range(T):
        nxt = {s: [] for s in selves}
        for s in selves:
            c[s], o = entry(c[s], arriving[s]); C[s].append(c[s])
            for to in joins[s]: nxt[to].append(o)
        arriving = nxt
    return C
# Part A: does "next = other's prior inverted wherever exactly one releases to a self" hold in random graphs under stepping together?
rng=random.Random(5)
bad=0; tot=0; example=None
for trial in range(300):
    n=rng.randint(3,7)
    selves=list(range(n))
    joins={s: rng.sample([u for u in selves if u!=s], rng.randint(0,min(4,n-1))) for s in selves}
    senders={s:[u for u in selves if s in joins[u]] for s in selves}
    for op in itertools.islice(itertools.product((1,-1),repeat=n),64):
        C=together(selves,joins,dict(zip(selves,op)),30)
        for s in selves:
            if len(senders[s])==1:
                u=senders[s][0]
                for t_ in range(2,30):
                    tot+=1
                    if C[s][t_+1]!=-C[u][t_-1]:
                        bad+=1
                        if example is None: example=(joins,op,s,u,t_)
print("one-sender selves, general graphs, together:",tot,"entries; failures",bad, example)
