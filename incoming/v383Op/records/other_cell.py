"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/other_cell.py
"""
import re, sys, io, contextlib, itertools, random
src = open('incoming/v383Op/meeting_v382A.py').read()
head = src.split("# ---------------------------------------------------------------------------------------------")[0]
part4 = src.split("print('4  The cell")[1].split("rules = [dict(zip(KINDS")[0]
exec(head)
exec("KINDS = ('match', 'mismatch', 'parting', 'none')\n" + part4.split("KINDS = ('match', 'mismatch', 'parting', 'none')")[1].replace("print(", "(lambda *a: None)("))
ALT = {'match': (1, 0), 'mismatch': (-1, -1), 'parting': (1, 0), 'none': (-1, -1)}
for name, (selves, joins) in STILL_AT + [('torus 3 by 4', torus(3,4)), ('torus 4 by 4', torus(4,4)), ('torus 2 by 2', torus(2,2)), ('spirals 2 and 2 crossed', crossed(2,2)), ('spirals 4 and 4 crossed', crossed(4,4))]:
    print('%-40s a self still at the other cell: %s ; at Exhibit ONE cell: %s' % (name, a_self_still(ALT, selves, joins), a_self_still(FILES, selves, joins)))
# joins drawn, each self receiving from one at least and releasing to one at least
def drawn(n, seed):
    r = random.Random(seed); selves = list(range(n))
    while True:
        joins = {s: r.sample([u for u in selves if u != s], r.randint(1, min(3, n - 1))) for s in selves}
        if all(any(s in joins[u] for u in selves) for s in selves):
            return selves, joins
hit = 0; tot = 0
for n in (4, 5, 6, 7):
    for seed in range(40):
        selves, joins = drawn(n, seed); tot += 1
        a = a_self_still(ALT, selves, joins, T=80); f = a_self_still(FILES, selves, joins, T=80)
        hit += a
        if f: print('EXHIBIT ONE STILL at', n, seed)
print('joins drawn, each self receiving from one at least: the other cell leaves a self still at %d of %d societies' % (hit, tot))
