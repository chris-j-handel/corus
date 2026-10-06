"""Session v383Op: the relation between two coupled selves at each self's own pacing.

Runs from the repository root: python3 incoming/v383Op/own_pacing.py
Reads the newest Exhibit ONE at the root and executes its python block. Each self's entry is
Exhibit ONE's own 1-co-bi-tri-offering, unchanged; 17, the stepping of the selves together, is
the one thing set aside, since the question is what the stepping brings.

The sentence examined, Natural Intelligence 4.13: "at each self's own pacing the relation is
carried, and each momentary of parities again is the stepping's."

The instrument, said whole (Geodesic Improving Method 4.4: an instrument's order and queue are
the instrument's own):
  - one self enters at a time, in an order the pacing gives;
  - a self entering is offered what was released to it since its own last entry, either each
    arrival together ("all") or the latest alone ("latest");
  - what it shares or releases is delivered at once to the self its join names;
  - a control steps the selves together as 17 does.
Four pacings: alternating; random, each self as likely; rates 1 and phi; one self twice to the
other's once. Two cases: two selves coupled across both ways; two spirals of 3 and 5 selves,
each releasing along, crossed at self 1 of each, both ways.

Reported: at how many entries the two coupled selves are opposite in parity.

The instrument's own, to be read with each number: delivery is at once at each pacing, with no
delay between a releasing and its arriving; 'alternating' at the two spirals is one fixed sweep
of the selves in list order, so a releasing can pass a whole spiral in one sweep; 'rates 1 and
phi' there paces one whole spiral at 1 and the other at phi; 'latest' can be a 0 arriving after a
parity; 'one self twice' makes more entries than the others; 'random' is one seed, and other
seeds part from it at the third decimal.
"""
import glob, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
PHI = (1 + 5 ** .5) / 2


def network(kind):
    """Returns (selves, joins: self -> list of receiving selves, the two coupled selves)."""
    if kind == 'two selves':
        return ['A', 'B'], {'A': ['B'], 'B': ['A']}, ('A', 'B')
    p, q = 3, 5
    selves = [('P', i) for i in range(p)] + [('Q', i) for i in range(q)]
    joins = {('P', i): [('P', (i + 1) % p)] for i in range(p)}
    joins.update({('Q', i): [('Q', (i + 1) % q)] for i in range(q)})
    joins[('P', 0)].append(('Q', 0))
    joins[('Q', 0)].append(('P', 0))
    return selves, joins, (('P', 0), ('Q', 0))


def opening(kind, selves, alike):
    if kind == 'two selves':
        return {'A': 1, 'B': 1 if alike else -1}
    return {s: (-1 if s[1] % 2 == 0 else 1) * (-1 if (s[0] == 'Q' and not alike) else 1) for s in selves}


def orders(name, selves, pair, entries, seed=383):
    r = random.Random(seed)
    if name == 'alternating':
        for i in range(entries):
            yield selves[i % len(selves)]
    elif name == 'random':
        for _ in range(entries):
            yield r.choice(selves)
    elif name == 'rates 1 and phi':
        # the selves of the first coupled self's side at rate 1, the others at rate 1/phi
        clock = {s: 0.0 for s in selves}
        rate = {s: (1.0 if (s == pair[0] or (isinstance(s, tuple) and s[0] == pair[0][0])) else PHI) for s in selves}
        for _ in range(entries):
            s = min(selves, key=lambda x: (clock[x], str(x)))
            clock[s] += rate[s]
            yield s
    elif name == 'one self twice':
        for i in range(entries):
            s = selves[i % len(selves)]
            yield s
            if s == pair[0]:
                yield s


def own_pacing(kind, pacing, arrive, alike, entries=30000):
    selves, joins, pair = network(kind)
    c = opening(kind, selves, alike)
    inbox = {s: [] for s in selves}
    opposite = n = 0
    for who in orders(pacing, selves, pair, entries):
        offered = inbox[who] if arrive == 'all' else inbox[who][-1:]
        shared, chained = _1([('s', c[who])], [('s', p) for p in offered])
        inbox[who] = []
        c[who] = dict(chained)['s']
        for to in joins[who]:
            inbox[to].append(shared[0][1])
        n += 1
        if n > entries // 10:
            opposite += c[pair[0]] != c[pair[1]]
    return opposite / (n - entries // 10)


def together(kind, alike, momentaries=3000):
    selves, joins, pair = network(kind)
    c = opening(kind, selves, alike)
    inbox = {s: [] for s in selves}
    opposite = n = 0
    for m in range(momentaries):
        nxt = {s: [] for s in selves}
        for who in selves:
            shared, chained = _1([('s', c[who])], [('s', p) for p in inbox[who]])
            c[who] = dict(chained)['s']
            for to in joins[who]:
                nxt[to].append(shared[0][1])
        inbox = nxt
        if m >= momentaries // 10:
            n += 1
            opposite += c[pair[0]] != c[pair[1]]
    return opposite / n


print('Exhibit ONE read at', exhibit_one)
for kind in ('two selves', 'spirals of 3 and 5 crossed'):
    print('\n' + kind + ': the two coupled selves opposite, as a part of the entries after the first tenth')
    for alike in (False, True):
        start = 'opening alike' if alike else 'opening opposite'
        print('  %-16s  stepped together, as 17: %.3f' % (start, together(kind, alike)))
        for pacing in ('alternating', 'random', 'rates 1 and phi', 'one self twice'):
            row = ['%s %.3f' % (a, own_pacing(kind, pacing, a, alike)) for a in ('all', 'latest')]
            print('  %-16s  %-16s %s' % (start, pacing, '   '.join(row)))
