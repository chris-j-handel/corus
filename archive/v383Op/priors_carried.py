"""Session v383Op: which couplings carry every prior on, and which bring two priors to one form.

Runs from the repository root: python3 incoming/v383Op/priors_carried.py
Reads the newest Exhibit ONE at the root and executes its python block.

Natural Intelligence 2.4 parts the sixteen ways by one test: "Twelve lose the prior, two joint
forms going to one", and "Four carry the prior whole". This script puts the same test to the
resolver's own societies: begin at EVERY opening (each self carrying + or -, nothing offered at
the first momentary, nothing from beyond), step the selves together as 17 does, and count the
different forms the society is at after m momentaries. A form here is each self's carrying and
what is arriving at it, the arrivals taken in no order, 14's surfacing being alike at each order.
If the count stays 2^n, each prior is carried whole; if it falls, two
openings have come to one form and no later momentary can tell them apart.

Part 2 checks 2.4's own counts: sixteen, twelve, four, and the 256.
"""
import glob, itertools, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_17 = ns['_17_co_bi_tri_offering']


def forms_after(selves, joins, momentaries):
    counts = []
    societies = [{s: ([('s', o[i])], []) for i, s in enumerate(selves)}
                 for o in itertools.product((1, -1), repeat=len(selves))]
    for m in range(momentaries + 1):
        seen = set()
        for soc in societies:
            seen.add(tuple((tuple(soc[s][0]), tuple(sorted(soc[s][1]))) for s in selves))
        counts.append(len(seen))
        nxt = []
        for soc in societies:
            out = _17(soc, joins)
            nxt.append({s: (out[s][0], out[s][1]) for s in selves})
        societies = nxt
    return counts


def ring(n):
    selves = list(range(n))
    return selves, {(i, 9): (i + 1) % n for i in selves}


def both_ways(n):
    selves = list(range(n))
    joins = {(i, 9): (i + 1) % n for i in selves}
    joins.update({(i, 10): (i - 1) % n for i in selves})
    return selves, joins


def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    joins = {}
    for i, j in selves:
        joins[((i, j), 9)] = ((i + 1) % p, j)
        joins[((i, j), 10)] = (i, (j + 1) % q)
    return selves, joins


print('Exhibit ONE read at', exhibit_one)
print('\n1. Different forms after m momentaries, from every opening (m = 0, 1, 2, 4, 8, 16, 24):')
for name, (selves, joins) in (('spiral of 3, one releasing to each', ring(3)),
                              ('spiral of 5, one releasing to each', ring(5)),
                              ('spiral of 8, one releasing to each', ring(8)),
                              ('3 selves, each coupled to both beside it', both_ways(3)),
                              ('torus 1 by 3', torus(1, 3)),
                              ('5 selves, each coupled to both beside it', both_ways(5)),
                              ('torus 2 by 2', torus(2, 2)),
                              ('torus 2 by 3', torus(2, 3)),
                              ('torus 3 by 3', torus(3, 3)),
                              ('torus 3 by 4', torus(3, 4))):
    counts = forms_after(selves, joins, 24)
    print('  %-42s openings %4d -> %s' % (name, counts[0], [counts[m] for m in (1, 2, 4, 8, 16, 24)]))

print("\n2. Natural Intelligence 2.4's counts:")
P = (1, -1)
ways = list(itertools.product(P, repeat=4))            # f(prior, now) at the four joint forms
joint = list(itertools.product(P, P))
whole, now_alone, half = [], 0, 0
for w in ways:
    f = dict(zip(joint, w))
    step = {(p, n): (n, f[(p, n)]) for p, n in joint}
    if len(set(step.values())) == 4:
        still = sum(1 for k, v in step.items() if k == v)
        cyc, seen = [], set()
        for k in joint:
            if k in seen or step[k] == k:
                continue
            length, x = 0, k
            while x not in seen:
                seen.add(x); x = step[x]; length += 1
            cyc.append(length)
        whole.append((w, still, cyc))
    elif all(f[(1, n)] == f[(-1, n)] for n in P):
        now_alone += 1
    else:
        half += 1
print('  ways: %d; carrying the prior whole: %d; losing it: %d (from now alone %d, at one value of now %d)'
      % (len(ways), len(whole), now_alone + half, now_alone, half))
for w, still, cyc in whole:
    f = dict(zip(joint, w))
    name = ('next as prior' if all(f[k] == k[0] for k in joint) else
            'next as prior inverted' if all(f[k] == -k[0] for k in joint) else
            'next as prior and now parting' if all(f[k] == -k[0] * k[1] for k in joint) else
            'next as prior and now agreeing')
    print('    %-32s joint forms still: %d; cycles: %s' % (name, still, cyc))
maps = 0
single = 0
for images in itertools.product(joint, repeat=4):
    maps += 1
    g = dict(zip(joint, images))
    if len(set(images)) != 4:
        continue
    if any(sum(a != b for a, b in zip(k, v)) != 1 for k, v in g.items()):
        continue
    x, n = joint[0], 0
    while True:
        x = g[x]; n += 1
        if x == joint[0]:
            break
    single += (n == 4)
print('  ways each joint form could go to a next: %d; one parity changing at each step and each joint form once in a cycle: %d' % (maps, single))


print("\n3. One other rule tried at a parting: + and - together carried on, 0 shared, the resolver's lines unchanged elsewhere.")
print('   Different forms after 24 momentaries, from every opening, by the plain rule of plain_rule.py with that one change:')


def other_rule_forms(p, q, carry_on_at_parting, momentaries=24):
    selves = [(i, j) for i in range(p) for j in range(q)]
    states = [(dict(zip(selves, o)), {s: 0 for s in selves}) for o in itertools.product((1, -1), repeat=len(selves))]
    for _ in range(momentaries):
        nxt = []
        for c, o in states:
            c2, o2 = {}, {}
            for i, j in selves:
                arrived = [x for x in (o[((i - 1) % p, j)], o[(i, (j - 1) % q)]) if x]
                parting = len(set(arrived)) == 2
                s = arrived[0] if arrived and not parting else 0
                n = c[(i, j)] if (parting and carry_on_at_parting) else (s if s else -c[(i, j)])
                c2[(i, j)] = n
                o2[(i, j)] = n if n != c[(i, j)] else 0
            nxt.append((c2, o2))
        states = nxt
    return len({(tuple(c.values()), tuple(o.values())) for c, o in states})


for p, q in ((1, 3), (2, 2), (2, 3), (3, 3)):
    print('   torus %d by %d: openings %3d; the resolver\'s rule %3d; the other rule %3d'
          % (p, q, 2 ** (p * q), other_rule_forms(p, q, False), other_rule_forms(p, q, True)))
