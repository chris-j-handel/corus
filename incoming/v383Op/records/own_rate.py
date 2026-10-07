"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/own_rate.py
"""
import re, random, itertools, sys
src = open('Exhibit_ONE_Natural_Resolver_v380R.md').read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']; _17 = ns['_17_co_bi_tri_offering']

def spiral(n):
    S = list(range(n)); comp = {(j,9):(j+1)%n for j in S}; return S, comp
def torus(p,q):
    S=[(i,j) for i in range(p) for j in range(q)]
    comp={}
    for i,j in S:
        comp[((i,j),9)] = ((i+1)%p,j); comp[((i,j),10)] = (i,(j+1)%q)
    return S, comp
def crossed(p,q):
    S=[('P',i) for i in range(p)]+[('Q',i) for i in range(q)]
    comp={(('P',i),9):('P',(i+1)%p) for i in range(p)}
    comp.update({(('Q',i),9):('Q',(i+1)%q) for i in range(q)})
    comp[(('P',0),10)] = ('Q',0); comp[(('Q',0),10)] = ('P',0)
    return S, comp

def real17(S, comp, opening, T):
    state = {s: ([('k', opening[s])], []) for s in S}
    seq = {s: [] for s in S}
    arrivals_log = {s: [] for s in S}
    for t in range(T):
        # shared value: recompute by _1 on a copy
        sh = {s: _1(list(state[s][0]), list(state[s][1]))[0] for s in S}
        for s in S: arrivals_log[s].append(list(state[s][1]))
        state = _17(state, comp)
        for s in S:
            seq[s].append((dict(state[s][0])['k'], dict(sh[s])['k']))
    return seq, arrivals_log

# my own rule, independent of _1
def rule(c, offered):
    nz = [p for p in offered if p != 0]
    if nz and all(p == nz[0] for p in nz):
        surf = nz[0]
    else:
        surf = 0 if nz else None
    if surf is not None and surf != 0 and surf == c:
        return c, 0
    return -c, -c

def event(S, comp, opening, T, seed, mode='random'):
    r = random.Random(seed)
    out = {s: [comp[(s,k)] for k in (6,10,9) if (s,k) in comp] for s in S}
    senders = {s: [u for u in S for v in out[u] if v == s] for s in S}
    q = {(u,s): [] for s in S for u in senders[s]}
    c = dict(opening); seq = {s: [] for s in S}
    maxq = 0
    while True:
        ready = [s for s in S if len(seq[s]) < T and (not seq[s] or all(q[(u,s)] for u in senders[s]))]
        if not ready: break
        if mode == 'random': s = r.choice(ready)
        elif mode == 'greedy': s = ready[0]       # always lowest-index ready self: extreme unfairness
        else: s = ready[-1]
        off = [] if not seq[s] else [q[(u,s)].pop(0) for u in senders[s]]
        c[s], sh = rule(c[s], off)
        seq[s].append((c[s], sh))
        for v in out[s]: q[(s,v)].append(sh)
        maxq = max(maxq, max(len(x) for x in q.values()))
    return seq, maxq

ok = True; n = 0
for name,(S,comp) in [('sp3',spiral(3)),('sp4',spiral(4)),('sp7',spiral(7)),('t23',torus(2,3)),('t33',torus(3,3)),('t35',torus(3,5)),('t13',torus(1,3)),('x35',crossed(3,5)),('x23',crossed(2,3)),('x57',crossed(5,7))]:
    r = random.Random(1)
    mq = 0
    for trial in range(40):
        op = {s: r.choice((1,-1)) for s in S}
        ref, alog = real17(S, comp, op, 50)
        # check arrivals: exactly one item from each sender per step after the first, including 0s
        out = {s: [comp[(s,k)] for k in (6,10,9) if (s,k) in comp] for s in S}
        nsend = {s: sum(1 for u in S for v in out[u] if v == s) for s in S}
        for s in S:
            assert alog[s][0] == []
            for t in range(1,50): assert len(alog[s][t]) == nsend[s], (name, s, t, alog[s][t])
        for mode in ('random','greedy','last'):
            got, m = event(S, comp, op, 50, trial, mode); mq = max(mq, m)
            n += 1
            if got != ref: ok = False; print('DIFF', name, trial, mode)
    print(name, 'ok', 'max queue', mq)
print('all alike:', ok, n)

# zeros delivered as items by the real _17?
S, comp = spiral(3)
op = {0:-1,1:1,2:-1}
ref, alog = real17(S, comp, op, 12)
print('spiral 3 self0 shared:', [x[1] for x in ref[0]])
print('arrivals at self 1 by step:', alog[1])
# rate lock under the "each" rule: largest lead of one self over another during a run
def lead(S, comp, opening, T, seed):
    r = random.Random(seed)
    out = {s: [comp[(s,k)] for k in (6,10,9) if (s,k) in comp] for s in S}
    senders = {s: [u for u in S for v in out[u] if v == s] for s in S}
    q = {(u,s): [] for s in S for u in senders[s]}
    c = dict(opening); n = {s: 0 for s in S}; rate = {s: r.uniform(1, 1.618) for s in S}; clock = {s: 0.0 for s in S}
    worst = 0; blocked = 0; picks = 0
    while True:
        ready = [s for s in S if n[s] < T and (n[s] == 0 or all(q[(u,s)] for u in senders[s]))]
        if not ready: break
        want = min((s for s in S if n[s] < T), key=lambda x: clock[x])   # the self whose own rate says it is next
        s = min(ready, key=lambda x: clock[x]); picks += 1; blocked += (want != s)
        clock[s] += rate[s]
        off = [] if n[s] == 0 else [q[(u,s)].pop(0) for u in senders[s]]
        c[s], sh = rule(c[s], off); n[s] += 1
        for v in out[s]: q[(s,v)].append(sh)
        worst = max(worst, max(n.values()) - min(n.values()))
    return worst, blocked, picks
for name,(S,comp) in [('sp5',spiral(5)),('t33',torus(3,3)),('x35',crossed(3,5))]:
    w = [lead(S, comp, {s: random.Random(i).choice((1,-1)) for s in S}, 400, i) for i in range(10)]
    print(name, 'selves', len(S), 'largest lead in momentaries over 400:', max(x[0] for x in w), 'picks where the self due by its own rate was not able to open:', sum(x[1] for x in w), 'of', sum(x[2] for x in w))
