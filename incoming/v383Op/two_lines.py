"""Session v383Op: the offerings and the possiblings, two lines through one co-momentarying.

Runs from the repository root: python3 incoming/v383Op/two_lines.py     (about half a minute)

The self's saying examined: "the offerings are living through the co-momentaryings as are the
possiblings living through the same co-momentaryings the two are looping through the
co-momentarying and never mixing with each other still possibling until one or other releases a
self parity changing".

At Exhibit ONE's 1-co-bi-tri-offering, unchanged, a self carrying a parity meets one of four:
  T  a taking: the other parity offered; it is chained and shared on as it arrived;
  .  still possibling: its own parity offered; a changing that is not, 0 shared;
  R  a releasing: nothing offered; its own parity inverted, and shared;
  P  parting offerings: 0 surfaced; its own parity inverted, and shared.

  1  Spirals of 2 to 10 stepped together, every opening: the takings at each momentary beside the
     opening's parting neighbours; and the rest, still possibling or releasing.
  2  One spiral followed, so the two lines can be seen.
  3  Two selves in turn: each offering followed from its releasing to its end.
  4  Tori stepped together: whether the takings are one number through the cycle.

The Co-Chaining Logic Registry already says much of it: step 233, a spiral carries any pattern
whole; 231, the 0 at the one like pair, one self on at each second momentary; 238 and 610, the
two patterns; 611, a self shares 0 no more momentaries in sequence than selves release to it.
What is run here is the count at each number of like pairs.
"""
import glob, itertools, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
S = {1: '+', -1: '-', 0: '0'}


def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]


def kind(c, offered):
    ps = [p for p in offered if p]
    if not ps:
        return 'R'
    if len(set(ps)) > 1:
        return 'P'
    return '.' if ps[0] == c else 'T'


def together(selves, joins, opening, T):
    c = dict(zip(selves, opening))
    arriving = {s: [] for s in selves}
    rows = []
    for _ in range(T):
        nxt = {s: [] for s in selves}
        row = {}
        for s in selves:
            k = kind(c[s], arriving[s])
            c[s], o = entry(c[s], arriving[s])
            row[s] = (k, o)
            for to in joins[s]:
                nxt[to].append(o)
        rows.append(row)
        arriving = nxt
    return rows


def ring(n):
    return list(range(n)), {j: [(j + 1) % n] for j in range(n)}


def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    return selves, {(i, j): [((i + 1) % p, j), (i, (j + 1) % q)] for i, j in selves}


print('1  Spirals stepped together, every opening, each momentary from the second to the fortieth')
print('   %-13s %9s %44s %48s' % ('', 'openings', 'takings at each momentary the opening\'s', 'the rest all still possibling at one momentary'))
print('   %-13s %9s %44s %48s' % ('', '', 'parting neighbours', 'and all releasing at the next'))
total = [0, 0, 0]
for n in range(2, 11):
    selves, joins = ring(n)
    tot = same = alt = 0
    for op in itertools.product((1, -1), repeat=n):
        rows = together(selves, joins, op, 40)[1:]
        parting = sum(op[s] != op[(s - 1) % n] for s in range(n))
        tot += 1
        same += all(sum(1 for s in selves if r[s][0] == 'T') == parting for r in rows)
        rest = [{r[s][0] for s in selves if r[s][0] != 'T'} for r in rows]
        alt += all(len(x) <= 1 for x in rest) and (parting == n or all(rest[i] != rest[i + 1] for i in range(len(rest) - 1)))
    total = [a + b for a, b in zip(total, (tot, same, alt))]
    print('   spiral of %-3d %9d %44d %48d' % (n, tot, same, alt))
print('   %-13s %9d %44d %48d' % ('together', *total))

print()
print('2  A spiral of 7 opened + + - - - + -, three like pairs and four parting: what each self shares, and which of the four it met')
selves, joins = ring(7)
for t, r in enumerate(together(selves, joins, (1, 1, -1, -1, -1, 1, -1), 12), 1):
    print('   momentary %2d   shared  %s      met  %s' % (t, ' '.join(S[r[s][1]] for s in selves), ' '.join(r[s][0] for s in selves)))
print('   each offering taken is one self on at each momentary; each like pair, a 0 at one momentary and a releasing at')
print('   the next, is one self on at each second momentary; and the number of each is the opening\'s at each momentary.')

print()
print('3  Two selves in turn, each opening and each first entering: each offering from its releasing to its end')
lives, home, released = {}, 0, 0
for op in itertools.product((1, -1), repeat=2):
    for first in (0, 1):
        c = list(op)
        waiting = [[], []]              # each waiting sharing with the self that released it and the entries it has lived
        for i in range(60):
            s = (first + i) % 2
            offered, waiting[s] = waiting[s], []
            k = kind(c[s], [p for p, who, n in offered])
            c[s], o = entry(c[s], [p for p, who, n in offered])
            if i >= 12:
                if k == 'R':
                    released += 1
                elif k == '.':
                    for p, who, n in offered:
                        if p:
                            lives[n] = lives.get(n, 0) + 1
                            home += who == s
            if k == 'R':
                waiting[1 - s].append((o, s, 0))
            elif k == 'T':
                waiting[1 - s].append((o, offered[0][1], offered[0][2] + 1))
            else:
                waiting[1 - s].append((0, None, 0))
print('   offerings released: %d; ended at a self still possibling: %d; takings each had lived before its end: %s;' % (
    released, sum(lives.values()), ', '.join('%d: %d offerings' % kv for kv in sorted(lives.items()))))
print('   ended at the self that released it: %d' % home)
print('   each offering is released by one self with nothing offered, taken once by the other, and ends back at its')
print('   releaser, still possibling; then the other, offered nothing, releases.')

print()
print('4  Tori stepped together, every opening, momentaries 81 to 160: each of the four one number at each momentary')
for p, q in ((2, 3), (3, 3), (3, 4)):
    selves, joins = torus(p, q)
    tot = 0
    one = {k: 0 for k in 'T.RP'}
    for op in itertools.product((1, -1), repeat=p * q):
        rows = together(selves, joins, op, 160)[80:]
        tot += 1
        for k in 'T.RP':
            one[k] += len({sum(1 for s in selves if r[s][0] == k) for r in rows}) == 1
    print('   torus %d by %d: %5d openings; takings one number: %5d; parting offerings: %5d; still possiblings: %5d; releasings: %5d' % (
        p, q, tot, one['T'], one['P'], one['.'], one['R']))
