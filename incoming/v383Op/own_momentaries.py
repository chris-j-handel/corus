"""Session v383Op, at its improving: each self's momentary opened at its arrivings, at each pacing.

Runs from the repository root: python3 incoming/v383Op/own_momentaries.py
Reads the newest Exhibit ONE at the root and executes its python block. Each self's entry is
Exhibit ONE's own 1-co-bi-tri-offering, unchanged. 17, the stepping of the selves together, is
set aside in the pacings and kept as the comparison.

The sentence examined, Natural Intelligence 4.13: "at each self's own pacing the relation is
carried", beside the Co-Chaining Logic Registry's step 91, "At each number, one side's completing
is the other side's opening", and its step 344, "with no coupling the method is at no two
existing things".

own_pacing.py, this session's first instrument, opened a self's momentary at a pace of its own
with an arriving missing. This instrument opens a self's momentary at its arrivings. Step 91 is
of one self and one other; the waiting for one arriving from each of two is this session's joining:
  - each releasing, a parity or a 0, is delivered to the self its join names and waits there,
    in the order it was released;
  - a self's first momentary opens with none arrived, as each table of Exhibit ONE opens;
  - each further momentary of a self opens when one releasing has arrived from EACH self
    releasing to it, and takes exactly those, one from each ("each"); or, for the comparison,
    opens at whatever has arrived when the pacing reaches the self, one arriving at least ("any");
  - which self enters next, among those whose momentary can open, is the pacing's: random, or by
    each self's own rate, a number between 1 and phi drawn for each self.
Compared: each self's own sequence of carrying next (11) and changing shared (10), momentary by
its own momentary, with the same society stepped together as 17 steps it.

The field's result this is an instance of (Kahn, 1974): selves each taking one arriving from
each of its own joins, the arrivings waiting first in first out, and releasing by a rule of its
own, give the same sequences at every order the waiting allows and every delay.

What the instrument carries of its own, to be read with each number:
  - a waiting place at each join, where an arriving waits, in order, for the self's momentary;
  - a 0 delivered as an arriving that opens a momentary, apart from nothing yet arrived, though
    at 14 an offered 0 surfaces none;
  - a self waiting, its carrying as it was, for as long as an arriving from each is not yet there;
  - the selves' rates one rate over many momentaries: reported below is the most momentaries one
    self is ahead of another at any entry, and the most arrivings waiting at one join.
It is the stepping said at each self, and it asks no stepping together.

Second part: a spiral read at each second momentary beside a ring of inverters, at EVERY opening
of rings of 3 to 8, and how many openings each ring is at rest from.
"""
import glob, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
PHI = (1 + 5 ** .5) / 2


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


def together(selves, joins, opening, momentaries):
    c = dict(opening)
    arriving = {s: [] for s in selves}
    seq = {s: [] for s in selves}
    for _ in range(momentaries):
        nxt = {s: [] for s in selves}
        for s in selves:
            shared, chained = _1([('k', c[s])], [('k', p) for p in arriving[s]])
            c[s] = dict(chained)['k']
            seq[s].append((c[s], shared[0][1]))
            for to in joins[s]:
                nxt[to].append(shared[0][1])
        arriving = nxt
    return seq


def own(selves, joins, opening, momentaries, take, pacing, seed):
    r = random.Random(seed)
    senders = {s: [u for u in selves if s in joins[u]] for s in selves}
    waiting = {s: {u: [] for u in senders[s]} for s in selves}      # in the order released
    c = dict(opening)
    seq = {s: [] for s in selves}
    rate = {s: r.uniform(1, PHI) for s in selves}
    clock = {s: 0.0 for s in selves}
    most = {'ahead': 0, 'waiting': 0}

    def can_open(s):
        if len(seq[s]) >= momentaries:
            return False
        if not seq[s]:
            return True                                            # the first momentary, none arrived
        if take == 'each':
            return all(waiting[s][u] for u in senders[s])
        return any(waiting[s][u] for u in senders[s])

    while True:
        ready = [s for s in selves if can_open(s)]
        if not ready:
            break
        s = r.choice(ready) if pacing == 'random' else min(ready, key=lambda x: (clock[x], str(x)))
        clock[s] += rate[s]
        if not seq[s]:
            offered = []
        elif take == 'each':
            offered = [waiting[s][u].pop(0) for u in senders[s]]
        else:
            offered = [waiting[s][u].pop(0) for u in senders[s] if waiting[s][u]]
        shared, chained = _1([('k', c[s])], [('k', p) for p in offered])
        c[s] = dict(chained)['k']
        seq[s].append((c[s], shared[0][1]))
        for to in joins[s]:
            waiting[to][s].append(shared[0][1])
            most['waiting'] = max(most['waiting'], len(waiting[to][s]))
        most['ahead'] = max(most['ahead'], max(len(q) for q in seq.values()) - min(len(q) for q in seq.values()))
    seq['most'] = most
    return seq


print('Exhibit ONE read at', exhibit_one)
print('\nEach self\'s own sequence, 40 of its own momentaries, beside the selves stepped together:')
print('  %-34s %-28s %s' % ('society', 'one arriving from each', 'whatever has arrived'))
cases = [('spiral of 3', spiral(3)), ('spiral of 5', spiral(5)), ('spiral of 8', spiral(8)),
         ('torus 2 by 3', torus(2, 3)), ('torus 3 by 3', torus(3, 3)), ('torus 3 by 7', torus(3, 7)),
         ('spirals of 3 and 5 crossed', crossed(3, 5)), ('spirals of 5 and 7 crossed', crossed(5, 7))]
for name, (selves, joins) in cases:
    r = random.Random(383)
    alike = {'each': 0, 'any': 0}
    runs = 0
    ahead = waited = 0
    for trial in range(60):
        opening = {s: r.choice((1, -1)) for s in selves}
        ref = together(selves, joins, opening, 40)
        for pacing in ('random', 'own rates'):
            runs += 1
            for take in ('each', 'any'):
                got = own(selves, joins, opening, 40, take, pacing, seed=trial)
                most = got.pop('most')
                if take == 'each':
                    ahead, waited = max(ahead, most['ahead']), max(waited, most['waiting'])
                alike[take] += all(got[s] == ref[s][:len(got[s])] and len(got[s]) == 40 for s in selves)
    print('  %-34s alike at %3d of %3d          alike at %3d of %3d    (one from each: most ahead %d, most waiting %d)'
          % (name, alike['each'], runs, alike['any'], runs, ahead, waited))

print('\nThe spiral read at each second momentary of each self, beside a ring of inverters,')
print('each giving its arriving inverted one delay on, v[j](t + 1) = -v[j-1](t), at every opening:')
import itertools
for n in range(3, 9):
    selves, joins = spiral(n)
    alike_all = rest = total = 0
    periods = set()
    for bits in itertools.product((1, -1), repeat=n):
        opening = dict(zip(selves, bits))
        seq = together(selves, joins, opening, 8 * n + 2)
        carry = [list(bits)] + [[seq[j][t][0] for j in selves] for t in range(8 * n + 2)]
        v, same = list(bits), True
        for k in range(4 * n):
            same = same and carry[2 * k] == v
            v = [-v[(j - 1) % n] for j in range(n)]
        T = next(T for T in range(1, 4 * n + 1) if all(carry[2 * (k + T)] == carry[2 * k] for k in range(2 * n)))
        total += 1
        alike_all += same
        rest += (T == 1)
        periods.add(T)
    print('  %d selves: alike with the ring of inverters at %3d of %3d openings; at rest from %3d; again at %s delays (2N is %d)'
          % (n, alike_all, total, rest, sorted(periods), 2 * n))
