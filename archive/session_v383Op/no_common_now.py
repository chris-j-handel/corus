"""Session v383Op, at the all-or-none reading: the resolver's cell with no common now at all.

Runs from the repository root: python3 incoming/v383Op/no_common_now.py
Reads the newest Exhibit ONE at the root and executes its python block; each self's entry is
Exhibit ONE's own 1-co-bi-tri-offering, unchanged.

The binary examined: a common now is, or is not.
  - own_momentaries.py is the first arm said at each self: a 0 is delivered as an arriving and a
    self waits for one from each, so the selves are at one rate.
  - own_pacing.py gives each self a pace of its own, a clock for each self.
  - This instrument is the second arm with nothing added but the order of delivery, which is
    drawn at random, one arriving at a time: no stepping together, no pace, and no 0 delivered. A self's first momentary opens with none arrived, as each table of Exhibit ONE
    opens. After it, a self's momentary opens at a parity arriving and at nothing else, the
    arrivings taken one at a time in the order each join released them; which arriving in
    passage is delivered next is drawn at random.
By the cell, a self offered its own parity shares 0, a match, and a 0 is not delivered: the
arriving ends there. A self offered the other parity is at a changing and shares it on.

Counted, at random openings: how many societies come to no arriving in passage, each self at one
parity with nothing offered, which the Co-Chaining Logic Registry names as a form of the
method's break; after how many changings; how many are still changing at the bound; and how
many of those opened with each self alike.

Said second, and it needs no count: at this arm each self's own sequence is its parity
inverted at each of its changings, + and - in turn, at each society and each order of delivery.
A self's own sequence then says nothing of its society; what a society has of its own is how
many changings each self is at beside the others, and which before which.

Counted second: one opening run at two orders of delivery to sixty changings a self, and each
self's number of changings: the least and the most a self is at as a part of the even share,
and whether the selves' numbers are the same at the two orders.
"""
import collections, glob, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
BOUND = 4000


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


def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]


def run(selves, joins, opening, r, bound=BOUND):
    c = dict(opening)
    received = {s: [] for s in selves}               # here: each self's own shared parities, in sequence
    passage = collections.OrderedDict(((s, to), collections.deque()) for s in selves for to in joins[s])
    changings = 0
    for s in selves:                                  # the first momentary, none arrived
        c[s], shared = entry(c[s], [])
        changings += 1
        received[s].append(shared)
        for to in joins[s]:
            if shared:
                passage[(s, to)].append(shared)
    while changings < bound:
        waiting = [k for k, q in passage.items() if q]
        if not waiting:
            return 'rest', changings, received
        s, to = r.choice(waiting)
        parity = passage[(s, to)].popleft()
        c[to], shared = entry(c[to], [parity])
        if shared:
            changings += 1
            received[to].append(shared)
            for on in joins[to]:
                passage[(to, on)].append(shared)
    return 'changing', changings, received


print('Exhibit ONE read at', exhibit_one)
print('\nNo stepping together, no pace and no 0 delivered: 400 random openings of each society')
cases = [('two selves', spiral(2)), ('spiral of 3', spiral(3)), ('spiral of 5', spiral(5)), ('spiral of 8', spiral(8)),
         ('torus 2 by 3', torus(2, 3)), ('torus 3 by 3', torus(3, 3)), ('torus 3 by 7', torus(3, 7)),
         ('spirals of 3 and 5 crossed', crossed(3, 5))]
for name, (selves, joins) in cases:
    r = random.Random(383)
    rest, counts, alike_opening, rest_alike, same, compared = 0, [], 0, 0, 0, 0
    least, most = 9.0, 0.0
    for trial in range(400):
        opening = {s: r.choice((1, -1)) for s in selves}
        all_alike = len(set(opening.values())) == 1
        alike_opening += all_alike
        how, n, _ = run(selves, joins, opening, r)
        if how == 'rest':
            rest += 1
            rest_alike += all_alike
            counts.append(n)
        elif trial < 100:
            one = run(selves, joins, opening, random.Random(1000 + trial), bound=60 * len(selves))[2]
            two = run(selves, joins, opening, random.Random(2000 + trial), bound=60 * len(selves))[2]
            compared += 1
            same += all(len(one[s]) == len(two[s]) for s in selves)
            for got in (one, two):
                least, most = min(least, min(len(q) for q in got.values()) / 60), max(most, max(len(q) for q in got.values()) / 60)
    counts.sort()
    said = ('each after %d to %d changings' % (counts[0], counts[-1])) if counts else ''
    print('  %-28s at rest: %3d of 400, %3d of them opened each self alike (%d opened so); still changing at %d changings: %3d   %s'
          % (name, rest, rest_alike, alike_opening, BOUND, 400 - rest, said))
    print('  %-28s a self\'s changings as a part of the even share: least %.2f, most %.2f; each self\'s number the same at two orders of delivery: %d of %d'
          % ('', least, most, same, compared))
