"""Exhibit ONE's code run at a society: an odd spiral of five selves joined along at 9, the last to the first,
one + offered once at self 1; and a torus of selves, p = 3 along at 9 and q = 5 across at 10.
Run from the repository root:
    python3 incoming/illustrating_three_momentaries_v379/executions/society_spiral_and_torus.py
"""
import re, glob
src = open(sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]).read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
ns = {}; exec(code, ns)
one, seventeen = ns['_1_co_bi_offering'], ns['_17_tri_co_offering']
say = lambda p: {None: '.', 1: '+', -1: '-', 0: '0'}[p]

def run(selves, joins, offered_at, momentaries):
    society = {s: ([], [('s', 1)] if s in offered_at else []) for s in selves}
    rows = {s: [] for s in selves}
    for m in range(momentaries):
        out = seventeen(society, joins)
        for s in selves:
            ten, _ = one(society[s][0], society[s][1]); rows[s].append(say(dict(ten).get('s')))
        society = {s: (out[s][0], [('s', v) for (_k, v) in out[s][1]]) for s in out}
    return rows

print("Part 1. A spiral of five, each self's 9 to the next self, the last to the first; + once at self 1; momentaries 1 to 24")
selves = [1, 2, 3, 4, 5]
joins = {(s, 9): selves[i % 5] for i, s in enumerate(selves, start=1)}
rows = run(selves, joins, {1}, 24)
for s in selves: print(f"  self {s}: {''.join(rows[s])}")
print("  the 0 at 10, the between, at one self at each second momentary, moving one self on: the tunneling")

print("\nPart 2. A torus, p = 3 along at 9 and q = 5 across at 10: selves (i, j), 9 to (i+1, j), 10 to (i, j+1); + once at (1, 1); momentaries 1 to 24")
p, q = 3, 5
selves = [(i, j) for i in range(p) for j in range(q)]
joins = {}
for (i, j) in selves:
    joins[((i, j), 9)] = ((i + 1) % p, j)
    joins[((i, j), 10)] = (i, (j + 1) % q)
rows = run(selves, joins, {(0, 0)}, 24)
for s in selves: print(f"  self {s}: {''.join(rows[s])}")
