"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/five.py
"""
import glob, re, itertools
ns = {}
exec(re.search(r"```python\n(.*?)```", open(sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
S = {1: '+', -1: '-', 0: '0'}
def run(op, T=14):
    c = {0: op[0], 1: op[1]}; arr = {0: [], 1: []}
    rows = []
    for t in range(T):
        nxt = {0: [], 1: []}; row = {}
        for s in (0, 1):
            shared, chained = _1([('k', c[s])], [('k', p) for p in arr[s]])
            new, o = dict(chained)['k'], shared[0][1]
            row[s] = (c[s], (arr[s] or [None])[0], o, new)   # carrying in (3), offered (2), shared (10), chained (11)
            c[s] = new; nxt[1 - s].append(o)
        rows.append(row); arr = nxt
    return rows
for op in itertools.product((1, -1), repeat=2):
    rows = run(op)
    print('opening', S[op[0]], S[op[1]])
    for s in (0, 1):
        print('  self %s: ' % 'AB'[s] + '  '.join('[3 %s | 2 %-4s 10 %s | 11 %s]' % (S[r[s][0]], 'none' if r[s][1] is None else S[r[s][1]], S[r[s][2]], S[r[s][3]]) for r in rows[:8]))
    # the bounce line: A's sharing at t, B's carrying entering t+1, B's sharing at t+1, A's carrying entering t+2, A's sharing at t+2
    tot = f5 = 0; fives = set()
    for s in (0, 1):
        for t in range(2, 11):
            five = (rows[t][s][2], rows[t + 1][1 - s][0], rows[t + 1][1 - s][2], rows[t + 2][s][0], rows[t + 2][s][2])
            fives.add(five); tot += 1
    print('  the five O C O C O along the bounce, forms met:', sorted(''.join(S[x] for x in f) for f in fives))
    # Exhibit ONE's five: other's 3 at t-1, other's 10 at t-1, self's 3 at t, self's 10 at t, self's 11 at t
    fives = set()
    for s in (0, 1):
        for t in range(2, 11):
            fives.add((rows[t - 1][1 - s][0], rows[t - 1][1 - s][2], rows[t][s][0], rows[t][s][2], rows[t][s][3]))
    print("  Exhibit ONE's five C O C O C, forms met:", sorted(''.join(S[x] for x in f) for f in fives))
    # within one entry: offering arriving (the other's 10 at prior), carrying in 3, surfaced now, changing 12 is/is not, shared 10
    fives = set()
    for s in (0, 1):
        for t in range(2, 11):
            fives.add((rows[t - 1][s][1] if rows[t - 1][s][1] is not None else 9, rows[t - 1][s][0], rows[t][s][1], rows[t][s][0], rows[t + 1][s][1]))
    print("  the self's own five, offered at prior, carrying at prior, offered now, carrying now, offered at next:", sorted(''.join(S.get(x, 'n') for x in f) for f in fives))
