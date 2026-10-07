"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/tori_settling.py
"""
import itertools, collections
src = open('incoming/v383Op/two_lines.py').read().split("print('1  Spirals")[0]
exec(src)
for p, q in ((2, 3), (3, 3), (3, 4)):
    selves, joins = torus(p, q)
    first = collections.Counter(); tot = 0; byopen = collections.Counter(); TP = collections.Counter()
    for op in itertools.product((1, -1), repeat=p * q):
        rows = together(selves, joins, op, 80)
        T = [sum(1 for s in selves if r[s][0] == 'T') for r in rows]
        P = [sum(1 for s in selves if r[s][0] == 'P') for r in rows]
        TPs = [a + b for a, b in zip(T, P)]
        k = next(i for i in range(80) if len(set(T[i:])) == 1)
        k2 = next(i for i in range(80) if len(set(TPs[i:])) == 1)
        first[(k + 1, k2 + 1)] += 1; tot += 1
        # opening counts: along partings, across partings
        c = dict(zip(selves, op))
        al = sum(c[(i, j)] != c[((i - 1) % p, j)] for i, j in selves); ac = sum(c[(i, j)] != c[(i, (j - 1) % q)] for i, j in selves)
        both = sum(c[(i, j)] != c[((i - 1) % p, j)] and c[(i, j)] != c[(i, (j - 1) % q)] for i, j in selves)
        one = sum((c[(i, j)] != c[((i - 1) % p, j)]) != (c[(i, j)] != c[(i, (j - 1) % q)]) for i, j in selves)
        TP[(T[1] == both, P[1] == one)] += 1
    print(p, q, 'openings', tot, '| momentary from which takings are one number, and takings with partings one number:', dict(sorted(first.items())))
    print('      at the second momentary: takings == selves parting from both sides at the opening, partings == selves parting from one side:', dict(TP))
