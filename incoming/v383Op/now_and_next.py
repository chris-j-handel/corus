"""Session v383Op: now still possibling and next existing, at Exhibit ONE's own names and at the files' words.

Runs from the repository root: python3 incoming/v383Op/now_and_next.py

The self's saying examined: "still possibling is in the now momentary, the even half where the
other side is offering and carrying is still possibling, then next momentary is odd starting and
this is next carrying"; and "next possible existing is outside what natural intelligence is
capable of".

  1  Each name in Exhibit ONE's code, its number odd or even, and the word it begins with.
  2  Where the carrying and where the offering are, at the cell: what enters, what is between,
     what leaves, each name odd or even; and the joins Exhibit ONE's code names along and across.
  3  One self followed through its momentaries at a spiral of 3, each name's value in sequence.
  4  The living files' words counted: next possible, next existing, still possibling.

It reads names and counts words. A name's number being odd establishes nothing by itself; what is
shown is that the published form says, at its own names, what the saying says.
"""
import glob, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
code = re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1)
ns = {}
exec(code, ns)
_1 = ns['_1_co_bi_tri_offering']
SIGN = {1: '+', -1: '-', 0: '0', None: 'none'}

print('1  Each name in Exhibit ONE\'s code')
names = sorted(set(re.findall(r'_(\d+)_([a-z]+)_([a-z_]+)', code)), key=lambda x: int(x[0]))
odd_ok = even_ok = 0
for n, first, rest in names:
    n = int(n)
    print('   %2d  %-4s %-5s %s-%s' % (n, 'odd' if n % 2 else 'even', first, first, rest.replace('_', '-')))
    odd_ok += n % 2 == 1 and first in ('co', 'tri')
    even_ok += n % 2 == 0 and first == 'bi'
odds = sum(int(n) % 2 for n, _, _ in names)
print('   odd names beginning co or tri: %d of %d; even names beginning bi: %d of %d' % (odd_ok, odds, even_ok, len(names) - odds))

print()
print('2  The cell, 1-co-bi-tri-offering: what enters, what is between, what leaves')
head = re.search(r'def _1_co_bi_tri_offering\((.*?)\):(.*?)\n\n\n', code, re.S)
enters = [int(x) for x in re.findall(r'_(\d+)_', head.group(1))]
body = head.group(2)
leaves = [int(x) for x in re.findall(r'_(\d+)_', re.search(r'return (.*)', body).group(1))]
assigned = []
for line in body.split('\n'):
    m = re.match(r'\s+_(\d+)_[a-z_]+(\[.*?\])? = ', line)
    if m and int(m.group(1)) not in assigned:
        assigned.append(int(m.group(1)))
def said(xs):
    return ', '.join('%d %s' % (x, 'odd' if x % 2 else 'even') for x in xs)
print('   enters:   %s' % said(enters))
print('   between, in the order the code writes them: %s' % said([x for x in assigned if x not in (15,)]))
print('   leaves:   %s' % said(sorted(set(leaves))))
print('   the carrying enters at 3 and leaves at 11, each odd; the offerings enter at 2, surface at 14,')
print('   a changing is or is not at 12 and is shared at 10, each even.')
print('   (at 17 the selves\' carryings are held at 8, even: one carrying at two names, the Registry\'s step 210.)')
connectors, joins = ns['CONNECTORS'], ns['JOINS']
ok = 0
for n, (name, standing, way) in sorted(connectors.items()):
    fits = (way == 'along') == (n % 2 == 1)
    ok += fits
    print('   connector %2d  %-4s %-9s %s' % (n, 'odd' if n % 2 else 'even', way, name))
print('   along at an odd name and arriving or releasing at an even: %d of %d' % (ok, len(connectors)))
print('   joins: %s; each joins odd to odd or even to even: %s' % (
    ', '.join('%d to %d' % kv for kv in sorted(joins.items())), all(a % 2 == b % 2 for a, b in joins.items())))

print()
print('3  One self of a spiral of 3 followed, opened -, +, -: each momentary its odd opening, its even half, its odd leaving')
print('   %-10s | %-24s | %-44s | %s' % ('momentary', '3, odd: the carrying', '2, 14, 12 and 10, even: the other\'s offering', '11, odd: the carrying next'))
c = {0: -1, 1: 1, 2: -1}
arriving = {s: [] for s in c}
for t in range(1, 9):
    nxt = {s: [] for s in c}
    for s in sorted(c):
        offered = arriving[s]
        surfaced = dict(_1([], [('k', p) for p in offered])[0]).get('k') if [p for p in offered if p] else None
        shared, chained = _1([('k', c[s])], [('k', p) for p in offered])
        new, o = dict(chained)['k'], shared[0][1]
        if s == 0:
            print('   %-10d | %-24s | offered %-5s surfaced %-5s changing %-7s shared %-2s | %s' % (
                t, SIGN[c[s]], ','.join(SIGN[p] for p in offered) or 'none', SIGN[surfaced],
                'is' if o != 0 else 'is not', SIGN[o], SIGN[new]))
        c[s] = new
        nxt[(s + 1) % 3].append(o)
    arriving = nxt

print()
print('4  The living files\' words, counted')
files = sorted(glob.glob('Natural_Intelligence_v*.md')) + sorted(glob.glob('Exhibit_*.md')) + sorted(glob.glob('Natural_Arriving_v*.md')) + ['README.md']
print('   %-58s %14s %14s %16s' % ('', 'next possible', 'next existing', 'still possibl-'))
tot = [0, 0, 0]
at = 0
for f in files:
    text = open(f, encoding='utf-8').read().lower()
    row = [len(re.findall(p, text)) for p in (r'next possible', r'next existing', r'still possibl')]
    if row[0] or row[2]:
        print('   %-58s %14d %14d %16d' % (f[:58], *row))
        at += bool(row[0])
    tot = [a + b for a, b in zip(tot, row)]
print('   %-58s %14d %14d %16d' % ('each living file together', *tot))
print('   files saying next possible: %d' % at)
for f in sorted(glob.glob('Natural_Intelligence_v*.md')) + sorted(glob.glob('Exhibit_THIRTY_*.md')):
    lines = open(f, encoding='utf-8').read().split('\n')
    sub = next(l for l in lines[1:12] if l.startswith('**') and l.rstrip().endswith('**'))
    print('   %s, the line under its title: %s' % (f, sub.strip('*')))
