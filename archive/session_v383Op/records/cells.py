"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/cells.py
"""
"""Exploring: each cell at two parities, inversion kept, beside the living step at one other. Scratch."""
import itertools

S_VALUES = ('match', 'mismatch', 'parting', 'none')
OUT = [(c, o) for c in (1, -1) for o in (1, -1, 0)]
FILES = {'match': (1, 0), 'mismatch': (-1, -1), 'parting': (-1, -1), 'none': (-1, -1)}


def surf(ps):
    ps = [p for p in ps if p != 0]
    if not ps:
        return None
    return ps[0] if all(p == ps[0] for p in ps) else 0


def step(rule, c, offered):
    s = surf(offered)
    key = 'none' if s is None else 'parting' if s == 0 else 'match' if s == c else 'mismatch'
    c2, o = rule[key]
    return c * c2, c * o          # the rule is said at a carrying of +; at - each parity inverted


def run(rule, selves, joins, opening, T):
    c = dict(opening); arriving = {s: [] for s in selves}
    C = {s: [c[s]] for s in selves}
    for _ in range(T):
        nxt = {s: [] for s in selves}
        for s in selves:
            c[s], o = step(rule, c[s], arriving[s])
            C[s].append(c[s])
            for to in joins[s]:
                nxt[to].append(o)
        arriving = nxt
    return C


def ring(n):
    return list(range(n)), {j: [(j + 1) % n] for j in range(n)}


def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    return selves, {(i, j): [((i + 1) % p, j), (i, (j + 1) % q)] for i, j in selves}


def cond_A(rule):
    """spiral of one: its chained parities at two momentaries in sequence are all four joint forms in one cycle"""
    for op in (1, -1):
        C = run(rule, [0], {0: [0]}, {0: op}, 24)[0][8:]
        if len({(C[i], C[i + 1]) for i in range(len(C) - 1)}) != 4:
            return False
    return True


def cond_B(rule, ns=(2, 3, 4, 5), T=24):
    """one other releasing to each self: the next is the other's prior inverted, each entry, each opening"""
    for n in ns:
        selves, joins = ring(n)
        for op in itertools.product((1, -1), repeat=n):
            C = run(rule, selves, joins, dict(zip(selves, op)), T)
            for s in selves:
                u = (s - 1) % n
                for t in range(2, T):
                    if C[s][t + 1] != -C[u][t - 1]:
                        return False
    return True


def cond_C(rule, p=3, q=3, T=80):
    """two others releasing to each self: no self at one parity from some momentary on, at any opening"""
    selves, joins = torus(p, q)
    for op in itertools.product((1, -1), repeat=p * q):
        C = run(rule, selves, joins, dict(zip(selves, op)), T)
        for s in selves:
            tail = C[s][T // 2:]
            if len(set(tail)) == 1:
                return False
    return True


rules = [dict(zip(S_VALUES, combo)) for combo in itertools.product(OUT, repeat=4)]
print('cells:', len(rules))
A = [r for r in rules if cond_A(r)]
B = [r for r in rules if cond_B(r)]
AB = [r for r in A if r in B]
print('A, spiral of one at all four joint forms:', len(A), '| files cell in:', FILES in A)
print('B, next the other prior inverted at one other:', len(B), '| files cell in:', FILES in B)
print('A and B:', len(AB))
ABC = [r for r in AB if cond_C(r)]
print('A and B and C (no self still at a torus 3 by 3):', len(ABC), '| files cell in:', FILES in ABC)
for r in ABC[:40]:
    print('  ', r, '<- files' if r == FILES else '')
# behaviour classes: do the survivors differ at any society?
if len(ABC) > 1:
    import collections
    sig = collections.defaultdict(list)
    for r in ABC:
        key = []
        for selves, joins in (ring(1), ring(2), ring(3), torus(2, 3), torus(3, 3)):
            for op in list(itertools.product((1, -1), repeat=len(selves)))[:64]:
                C = run(r, selves, joins, dict(zip(selves, op)), 16)
                key.append(tuple(tuple(C[s]) for s in selves))
        sig[tuple(key)].append(r)
    print('distinct in what each self carries, at these societies:', len(sig))
    for k, v in sig.items():
        print('  class of', len(v), ':', v[0], '...' if len(v) > 1 else '', '<- files' if FILES in v else '')
