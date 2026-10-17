"""Session v383Op, at the all-or-none reading: a self's carrying named from its sharings alone.

Runs from the repository root: python3 incoming/v383Op/observer.py
Reads the newest Exhibit ONE at the root and executes its python block; each self's entry is
Exhibit ONE's own 1-co-bi-tri-offering, unchanged, the selves stepped together as 17 steps them.

The sentence examined: the scientific method is incompetent for discovering competency.
The Co-Chaining Logic Registry says competency is "the prior carried into now", along, and that
"Between selves pass the changings alone". So the question at the resolver, is or is not: can
one who receives only what a self shares, and never its carrying, name its carrying?

The observer here holds the cell's rule and the joins, and receives each self's sharings and
never a carrying. From a self's sharings it names the self's carrying at each momentary from
that self's first changing on: the parity shared, and after a 0 the parity last named. Counted:
how often the naming is the carrying. Also counted, the observer's next: from each self's named
carrying and the sharings in passage, by the rule, the next carrying of each self.

What it shows and what it does not: the selves are stepped together, the arm a common now gives.
The naming is the rule applied, no discovering of the rule; at the resolver a carrying is hidden
from no one who has the rule and the sharings.
"""
import glob, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']


def spiral(n):
    return list(range(n)), {j: [(j + 1) % n] for j in range(n)}


def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    return selves, {(i, j): [((i + 1) % p, j), (i, (j + 1) % q)] for i, j in selves}


def crossed(p, q):
    selves = [('P', i) for i in range(p)] + [('Q', i) for i in range(q)]
    joins = {('P', i): [('P', (i + 1) % p)] for i in range(p)}
    joins.update({('Q', i): [('Q', (i + 1) % q)] for i in range(q)})
    joins[('P', 0)].append(('Q', 0))
    joins[('Q', 0)].append(('P', 0))
    return selves, joins


def run(selves, joins, opening, momentaries):
    """Each self's carrying next and sharing, momentary by momentary."""
    c = dict(opening)
    arriving = {s: [] for s in selves}
    out = []
    for _ in range(momentaries):
        nxt = {s: [] for s in selves}
        row = {}
        for s in selves:
            shared, chained = _1([('k', c[s])], [('k', p) for p in arriving[s]])
            c[s] = dict(chained)['k']
            row[s] = (c[s], shared[0][1])
            for to in joins[s]:
                nxt[to].append(shared[0][1])
        arriving = nxt
        out.append(row)
    return out


print('Exhibit ONE read at', exhibit_one)
print('\nA self\'s carrying named from its sharings alone, and each self\'s next named one momentary ahead:')
cases = [('spiral of 5', spiral(5)), ('spiral of 8', spiral(8)), ('torus 3 by 3', torus(3, 3)),
         ('torus 3 by 7', torus(3, 7)), ('spirals of 3 and 5 crossed', crossed(3, 5))]
for name, (selves, joins) in cases:
    r = random.Random(383)
    named = right = unnamed = ahead = ahead_right = 0
    for trial in range(200):
        opening = {s: r.choice((1, -1)) for s in selves}
        rows = run(selves, joins, opening, 40)
        senders = {s: [u for u in selves if s in joins[u]] for s in selves}
        seen = {s: None for s in selves}                 # the observer's naming of each carrying
        for t, row in enumerate(rows):
            # the observer's next, said before this momentary's sharings are received
            if t and all(seen[s] is not None for s in selves):
                for s in selves:
                    offered = [rows[t - 1][u][1] for u in senders[s] if rows[t - 1][u][1]]
                    one = offered[0] if offered and len(set(offered)) == 1 else 0
                    said = one if one else -seen[s]
                    ahead += 1
                    ahead_right += (said == row[s][0])
            for s in selves:
                if row[s][1]:
                    seen[s] = row[s][1]
                if seen[s] is None:
                    unnamed += 1
                else:
                    named += 1
                    right += (seen[s] == row[s][0])
    print('  %-28s carrying named at %6d entries, the carrying at %6d; not yet named at %d; next said ahead at %6d, so at %6d'
          % (name, named, right, unnamed, ahead, ahead_right))
