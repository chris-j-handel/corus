"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/whose_prior.py
"""
"""Exploring: whose prior is inverted at the next. Run from the worktree root."""
import glob, itertools, re

ns = {}
exec(re.search(r"```python\n(.*?)```", open(sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']


def run(selves, joins, opening, T):
    c = dict(opening)
    arriving = {s: [] for s in selves}
    C = {s: [c[s]] for s in selves}      # C[s][0] the opening carrying, C[s][t] the carrying chained at momentary t
    O = {s: [None] for s in selves}
    for _ in range(T):
        nxt = {s: [] for s in selves}
        for s in selves:
            shared, chained = _1([('k', c[s])], [('k', p) for p in arriving[s]])
            c[s] = dict(chained)['k']
            C[s].append(c[s]); O[s].append(shared[0][1])
            for to in joins[s]:
                nxt[to].append(shared[0][1])
        arriving = nxt
    return C, O


def ring(n):
    return list(range(n)), {j: [(j + 1) % n] for j in range(n)}


def both(n=2):
    return [0, 1], {0: [1], 1: [0]}


def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    return selves, {(i, j): [((i + 1) % p, j), (i, (j + 1) % q)] for i, j in selves}


def surf(ps):
    ps = [p for p in ps if p != 0]
    if not ps:
        return None
    return ps[0] if all(p == ps[0] for p in ps) else 0


def test(name, selves, joins, T=40):
    senders = {s: [u for u in selves if s in joins[u]] for s in selves}
    tot = other = own = allsurf = now = 0
    bad_open = set()
    for op in itertools.product((1, -1), repeat=len(selves)):
        C, O = run(selves, joins, dict(zip(selves, op)), T)
        ok_o = True
        for s in selves:
            for t in range(2, T):
                tot += 1
                # the prior the other's: each sender's carrying two momentaries prior, surfaced all or none
                sp = surf([C[u][t - 1] for u in senders[s]])
                if sp is not None and sp != 0 and C[s][t + 1] == -sp:
                    allsurf += 1
                elif sp == 0 and C[s][t + 1] == -C[s][t]:
                    allsurf += 1
                if len(senders[s]) == 1 and C[s][t + 1] == -C[senders[s][0]][t - 1]:
                    other += 1
                if C[s][t + 1] == -C[s][t - 1]:
                    own += 1
                if C[s][t + 1] == -C[s][t]:
                    now += 1
    print('%-22s entries %7d | next = other prior inverted %7d | all-or-none of others priors %7d | own prior inverted %7d | own now inverted %7d' % (name, tot, other, allsurf, own, now))


test('two selves both ways', *both())
for n in range(1, 8):
    test('spiral of %d' % n, *ring(n))
test('torus 3 by 3', *torus(3, 3), T=30)
test('torus 2 by 3', *torus(2, 3), T=30)
test('torus 3 by 4', *torus(3, 4), T=20)


def determined(name, selves, joins, T=24):
    senders = {s: [u for u in selves if s in joins[u]] for s in selves}
    keys = {'others priors': {}, 'others priors, own now': {}, 'others priors, own now, own prior': {}, 'others nows': {}, 'others nows, own now': {}, 'others priors and nows, own now': {}}
    for op in itertools.product((1, -1), repeat=len(selves)):
        C, O = run(selves, joins, dict(zip(selves, op)), T)
        for s in selves:
            for t in range(2, T):
                pr = tuple(sorted(C[u][t - 1] for u in senders[s])); nw = tuple(sorted(C[u][t] for u in senders[s]))
                pn = tuple(sorted((C[u][t - 1], C[u][t]) for u in senders[s]))
                for k, v in (('others priors', pr), ('others priors, own now', (pr, C[s][t])), ('others priors, own now, own prior', (pr, C[s][t], C[s][t - 1])),
                             ('others nows', nw), ('others nows, own now', (nw, C[s][t])), ('others priors and nows, own now', (pn, C[s][t]))):
                    keys[k].setdefault(v, set()).add(C[s][t + 1])
    print(name)
    for k, d in keys.items():
        print('   next from %-36s: %d forms, %d of them at both nexts' % (k, len(d), sum(len(x) > 1 for x in d.values())))


determined('two selves both ways', *both())
determined('spiral of 5', *ring(5))
determined('torus 3 by 3', *torus(3, 3))
determined('torus 3 by 4', *torus(3, 4), T=16)
