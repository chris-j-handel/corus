"""Session v383Op: a self in bi-coupling with an other, the two stepped together and the two in turn.

Runs from the repository root: python3 incoming/v383Op/in_turn.py

The self's saying examined: "prior offering, prior carrying, now offering, still possibling, next
offering ... the even of this is odd from the side of other and the same five are on both sides
alternating offering and possibling each other as co-parity-changing".

Exhibit ONE steps each self at one momentary with each other, which the Co-Chaining Logic Registry's
step 244 calls the executing's own common beat. Its step 37 says the two change one and then the
other. Both are run here at Exhibit ONE's 1-co-bi-tri-offering, unchanged.

  1  Two selves coupled both ways, stepped together, each opening.
  2  The same two, in turn: one enters, taking what the other last shared, then the other.
  3  The five at one side, read off the cycle of part 2.
  4  Spirals of 1 to 8 entered in turn around, each opening: how far part 2 goes.
  5  The saying's words, counted at the living files.

What this instrument carries of its own: in turn, a sharing waits at the other until the other's
next entry, and is taken once; which self enters first is this instrument's, and both are run.
"""
import glob, itertools, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
S = {1: '+', -1: '-', 0: '0', None: 'none'}


def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]


def marks(xs):
    return ' '.join('X' if x else '.' for x in xs)


print('1  Two selves coupled both ways, stepped together: a changing is, X, or is not, .')
for op in itertools.product((1, -1), repeat=2):
    c = list(op)
    arriving = [[], []]
    shared = [[], []]
    for t in range(12):
        nxt = [[], []]
        for s in (0, 1):
            c[s], o = entry(c[s], arriving[s])
            shared[s].append(o)
            nxt[1 - s].append(o)
        arriving = nxt
    print('   opened %s %s   the self: %s    the other: %s' % (S[op[0]], S[op[1]], marks(shared[0]), marks(shared[1])))
print('   opened alike, each is still possibling at each second momentary, the two at the same momentaries;')
print('   opened parting, a changing is at each momentary of each, and neither is ever still possibling.')


def in_turn(op, first, T):
    c = list(op)
    waiting = [[], []]
    line = []
    for i in range(T):
        s = (first + i) % 2
        offered, waiting[s] = waiting[s], []
        was = c[s]
        c[s], o = entry(c[s], offered)
        line.append((s, was, offered[0] if offered else None, o, c[s]))
        waiting[1 - s].append(o)
    return line


print()
print('2  The same two in turn')
forms = set()
for op in itertools.product((1, -1), repeat=2):
    for first in (0, 1):
        line = in_turn(op, first, 48)
        tail = line[12:]
        sh = [o for s, was, off, o, new in tail]
        cycle = next(p for p in range(1, 13) if all(sh[i] == sh[i + p] for i in range(len(sh) - p)))
        per_side = [sum(1 for s, was, off, o, new in tail[:cycle] if s == side) for side in (0, 1)]
        nots = [(i, s) for i, (s, was, off, o, new) in enumerate(tail) if o == 0]
        alternate = all(nots[i][1] != nots[i + 1][1] for i in range(len(nots) - 1))
        third = all(nots[i + 1][0] - nots[i][0] == 3 for i in range(len(nots) - 1))
        inverted = all(sh[i + 3] == -sh[i] for i in range(len(sh) - 3))
        forms.add((cycle, tuple(per_side), alternate, third, inverted))
        print('   opened %s %s, %s entering first:  %s' % (S[op[0]], S[op[1]], ('the self', 'the other')[first],
                                                            ' '.join(('s' if s == 0 else 'o') + ('X' if o else '.') for s, was, off, o, new in line[:18])))
print('   from each of the eight: (entries in the cycle, entries at each side, the changing that is not alternating sides,')
print('   at each third entry, each sharing the inversion of the sharing three entries before): %s' % sorted(forms))

print()
print('3  The cycle of six, opened + +, the self first, entries 13 to 24; each entry its carrying arriving (3), the offering')
print('   arriving (2), a changing is or is not (12), its sharing (10), its carrying next (11)')
line = in_turn((1, 1), 0, 24)[12:]
for i, (s, was, off, o, new) in enumerate(line):
    print('   %-9s 3 %s   2 %-4s   12 %-6s   10 %s   11 %s' % (('the self', 'the other')[s], S[was], S[off], 'is' if o else 'is not', S[o], S[new]))
print('   read from the self at its entry where a changing is not: the offering it made two entries before; the other\'s')
print('   carrying taking it; the other\'s offering of it, arriving; the self\'s carrying kept, still possibling; and the')
print('   other\'s next offering, the inversion. From the other the same five stand three entries on.')

print()
print('4  Spirals of 1 to 8 entered in turn around, each opening: entries in the cycle, changings that are not in it, openings')
for n in range(1, 9):
    found = {}
    for op in itertools.product((1, -1), repeat=n):
        c = list(op)
        waiting = [[] for _ in range(n)]
        seen, seq = {}, []
        for i in range(6000):
            s = i % n
            offered, waiting[s] = waiting[s], []
            c[s], o = entry(c[s], offered)
            waiting[(s + 1) % n].append(o)
            seq.append(o)
            if s == n - 1:
                key = (tuple(c), tuple(tuple(w) for w in waiting))
                if key in seen:
                    cyc = seq[seen[key] + 1:i + 1]
                    k = (len(cyc), cyc.count(0))
                    found[k] = found.get(k, 0) + 1
                    break
                seen[key] = i
    print('   spiral of %d: %s' % (n, ', '.join('%d entries, %d not: %d openings' % (a, b, v) for (a, b), v in sorted(found.items()))))
print('   one cycle from each opening at spirals of 1 to 4; more than one from 5 on.')

print()
print('5  The saying\'s words at the living files, counted')
files = sorted(glob.glob('Natural_Intelligence_v*.md')) + sorted(glob.glob('Exhibit_*.md')) + sorted(glob.glob('Natural_Arriving_v*.md')) + ['README.md']
text = '\n'.join(open(f, encoding='utf-8').read().lower() for f in files)
for w in ('prior offering', 'prior carrying', 'now offering', 'still possibling', 'next offering', 'co-parity-changing', 'moral cooperation',
          'bi-moral-co-competencing', 'five dimensions', 'six one-way', 'four momentaries'):
    print('   %-26s %d' % (w, len(re.findall(re.escape(w), text))))
