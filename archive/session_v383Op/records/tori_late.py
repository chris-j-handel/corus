"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/tori_late.py
"""
import itertools, collections
src = open('incoming/v383Op/two_lines.py').read().split("print('1  Spirals")[0]
exec(src)
def run(p, q, op, T):
    selves, joins = torus(p, q)
    c = dict(zip(selves, op)); arr = {s: {} for s in selves}; rows = []
    for t in range(T):
        nxt = {s: {} for s in selves}; row = {}
        for s in selves:
            al, ac = arr[s].get('along', 0), arr[s].get('across', 0)
            offered = [x for x in (al, ac)]
            k = kind(c[s], offered); was = c[s]
            c[s], o = entry(c[s], offered)
            def side(x): return 'own' if x == was else ('none' if x == 0 else 'other')
            row[s] = (k, side(al), side(ac), o)
            i, j = s
            nxt[((i + 1) % p, j)]['along'] = o
            nxt[(i, (j + 1) % q)]['across'] = o
        rows.append(row); arr = nxt
    return selves, rows
# what the two sides offered at each kind, and what follows a still possibling
for p, q in ((2, 3), (3, 3), (3, 4)):
    sides = collections.Counter(); after = collections.Counter(); runs = collections.Counter(); kinds = collections.Counter()
    n_open = 0
    for op in itertools.product((1, -1), repeat=p * q):
        n_open += 1
        selves, rows = run(p, q, op, 60)
        rows = rows[20:]
        for s in selves:
            run_len = 0
            for i, r in enumerate(rows):
                k, al, ac, o = r[s]
                kinds[k] += 1
                sides[(k, tuple(sorted((al, ac))))] += 1
                if k == '.':
                    run_len += 1
                    if i + 1 < len(rows): after[rows[i + 1][s][0]] += 1
                else:
                    if run_len: runs[run_len] += 1
                    run_len = 0
    tot = sum(kinds.values())
    print('torus %d by %d, %d openings, momentaries 21 to 60' % (p, q, n_open))
    print('   of each 1000 entries:', {k: round(1000 * v / tot) for k, v in sorted(kinds.items())})
    print('   what the two sides offered, by what the self met:')
    for (k, sd), v in sorted(sides.items()): print('      %s  %-18s %d' % (k, ' and '.join(sd), v))
    print('   still possibling how many momentaries in sequence:', dict(sorted(runs.items())))
    print('   after a still possibling, the next momentary the self meets:', dict(sorted(after.items())))
# one small trace
selves, rows = run(3, 3, (-1, 1, -1, 1, -1, 1, -1, 1, 1), 10)
print('torus 3 by 3, one opening, what each self met, momentary by momentary (rows of the torus side by side)')
for t, r in enumerate(rows, 1):
    print('   %2d   ' % t + '   '.join(' '.join(r[(i, j)][0] for j in range(3)) for i in range(3)) + '      T %d  . %d  R %d  P %d' % tuple(sum(1 for s in selves if r[s][0] == k) for k in 'T.RP'))
