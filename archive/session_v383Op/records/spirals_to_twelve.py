"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/spirals_to_twelve.py
"""
import itertools, collections
def rule(c, offered):
    nz = [p for p in offered if p != 0]
    if nz and all(p == nz[0] for p in nz) and nz[0] == c:
        return c, 0
    return -c, -c
def step(state, senders):
    c, sh = state
    nc = []; ns = []
    for s in range(len(c)):
        off = [] if sh is None else [sh[u] for u in senders[s]]
        a, b = rule(c[s], off); nc.append(a); ns.append(b)
    return (tuple(nc), tuple(ns))
def torus(p,q):
    idx = {(i,j): i*q+j for i in range(p) for j in range(q)}
    senders = {idx[(i,j)]: [idx[((i-1)%p,j)], idx[(i,(j-1)%q)]] for i in range(p) for j in range(q)}
    return p*q, senders
def ring(n): return n, {j: [(j-1)%n] for j in range(n)}
def cycles(n, senders, canon=False):
    seen = {}  # full state (c, sh) -> cycle id
    cyc = {}
    for op in itertools.product((1,-1), repeat=n):
        st = (op, None); path = []; local = {}
        while st not in seen and st not in local:
            local[st] = len(path); path.append(st); st = step(st, senders)
        if st in seen: cid = seen[st]
        else:
            cyclestates = path[local[st]:]
            cid = min(cyclestates); cyc[cid] = len(cyclestates)
        for x in path: seen[x] = cid
    return cyc
for p,q in ((3,3),(3,5),(2,3),(1,3)):
    n, snd = torus(p,q)
    cyc = cycles(n, snd)
    print('torus', p, q, 'openings', 2**n, 'distinct cycles (full state c+shared):', len(cyc), sorted(collections.Counter(cyc.values()).items()))
    # by carrying-and-shared sequence per self period? also count cycles by carrying only
    # cycles distinct as sets of carrying patterns
# ring-of-inverters check, every opening
for n in range(1, 13):
    N, snd = ring(n)
    allok = True; rest = 0; per = collections.Counter()
    for op in itertools.product((1,-1), repeat=n):
        st = (op, None); carry = [op]
        for t in range(8*n+2):
            st = step(st, snd); carry.append(st[0])
        v = list(op)
        for k in range(4*n):
            if list(carry[2*k]) != v: allok = False
            v = [-v[(j-1)%n] for j in range(n)]
        T = next(T for T in range(1, 4*n+1) if all(carry[2*(k+T)] == carry[2*k] for k in range(2*n)))
        per[T] += 1
    print('ring', n, 'law at every opening:', allok, 'periods in delays:', sorted(per.items()))
