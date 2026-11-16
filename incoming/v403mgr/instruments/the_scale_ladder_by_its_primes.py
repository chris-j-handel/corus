"""Exhibit SEVEN Natural Societies in the table: the fourteen rungs of its scale-ladder, each prime with its
scale as it is written, its name sixteen on, its place round a ring of twenty-four, and its forms as squares.
Reads Exhibit SEVEN Natural Societies and Exhibit ONE Natural Resolver; executes; writes no file; decides
nothing. Each answer is all or none at all, by each rung, by each prime of the 1,024, and by a rule's own lines.

Use: python3 -I incoming/v403mgr/instruments/the_scale_ladder_by_its_primes.py <root>          each check
     python3 -I incoming/v403mgr/instruments/the_scale_ladder_by_its_primes.py <root> csv      one line with each rung

A field's words, of whole numbers x and y: a square and a square, x² + y²; a square and two of a square,
x² + 2y²; a square less two of a square, x² − 2y²; a square and three of a square, x² + 3y².

Returned at main, 16 November 2026, each check is:
  Fifteen entries: fourteen rungs with the primes 5 to 53, each prime of position 3 to 16 among primes, and the
  fold, twenty-four, between 23 and 29, no rung; each rung before or after
  as its prime is one before or one after a six; seven and seven across twenty-four, four before a six and
  three after with each seven. The second list has the same fourteen primes with the same scales.
  Each prime past three has one of eight places round a ring of twenty-four, 1, 5, 7, 11, 13, 17, 19 or 23, and
  its forms of four are by its place, no two places the same: by each prime of the 1,024.
  The ladder's first seven rungs, 5 to 23, are one prime with each place but 1: the fold at twenty-four is one
  round of the ring. Its next seven are with 5, 7, 13, 17, 19, 23 and 5 again; 25 and 35 are no primes.
  Each rung one after a six is a square and three of a square, and no rung one before a six is.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
soc = living('Exhibit_SEVEN_Natural_Societies'); one = living('Exhibit_ONE_Natural_Resolver')
for said in ('Before it, four one before a six and three one after, 5, 11, 17, 23 and 7, 13, 19; after it likewise, 29, 41, 47, 53 and 31, 37, 43: **seven and seven across the fold',
             '**The fold is twenty-four, six times four, no rung\'s number'):
    assert said in soc, said
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
def entries(head):
    body = soc.split(head, 1)[1]; out = []
    for l in body.split('\n')[1:]:
        m = re.match(r'- \*\*(\d+)\*\*\s*$', l); c = re.match(r'  - \*([a-e])\* (.*)$', l)
        if m: out.append({'prime': int(m.group(1))})
        elif c and out: out[-1][c.group(1)] = c.group(2)
        elif l.startswith(('#', 'Each entry:')) or (l.startswith('**') and out): break
    return out
A = entries('Each entry: **prime** · *a* one before or after six · *b* scale'); B = entries('Each entry: **prime** · *a* scale · *b* total')
prime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
P = [n for n in range(1, 1025) if prime(n)]
ALL_A, ALL_B = A, B; A = [e for e in ALL_A if prime(e['prime'])]; B = [e for e in ALL_B if prime(e['prime'])]      # the rungs; the fold, twenty-four, is an entry and no rung
root = lambda v: int(v ** 0.5 + 0.5) if v >= 0 and int(v ** 0.5 + 0.5) ** 2 == v else None
def form(p, k):                                              # x² + k y², or with k of −2, x² − 2 y²: its x and y, or none
    ys = range(0, p + 1) if k < 0 else range(0, int((p / k) ** 0.5) + 1)
    return next(((x, y) for y in ys for x in [root(p - k * y * y)] if x is not None), None)
FORMS = (('a square and a square', 1), ('a square and two of a square', 2), ('a square less two of a square', -2), ('a square and three of a square', 3))
has = lambda p: tuple(name for name, k in FORMS if form(p, k))
show = lambda p, k: (lambda s: '' if not s else f'{s[0]}² {"−" if k < 0 else "+"} {"" if abs(k) == 1 else str(abs(k)) + " · "}{s[1]}²')(form(p, k))

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['prime', 'its position among primes', 'one before or after a six', 'its scale', 'its side', 'its status', 'a self observing its closing', 'its name, sixteen on',
                'its place round a ring of twenty-four'] + [name for name, _ in FORMS] + ['its total, by a field', 'its level', 'its direction'])
    for e in A:
        p = e['prime']; b = next(x for x in B if x['prime'] == p)
        w.writerow([p, P.index(p) + 1, e['a'], e['b'], e['c'], e['d'], e['e'], NAME[(p - 1) % 16 + 1], p % 24] + [show(p, k) for _, k in FORMS] + [b['b'], b['c'], b['d']])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
rungs = [e['prime'] for e in A]
print(f"Exhibit SEVEN Natural Societies, its scale-ladder: {len(A)} rungs, and the fold")
say(rungs == P[2:16] and len(rungs) == 14 and [e['prime'] for e in ALL_A if not prime(e['prime'])] == [24] and [e['prime'] for e in ALL_A].index(24) == 7,
    'fifteen entries: fourteen rungs with the primes 5 to 53, each prime of position 3 to 16 among primes, and the fold, twenty-four, between 23 and 29, no rung')
say(all((e['a'].startswith('before')) == (e['prime'] % 6 == 5) and (e['a'].startswith('after')) == (e['prime'] % 6 == 1) for e in A), 'each rung is before or after, as its prime is one before or one after a six')
lo = [p for p in rungs if p < 24]; hi = [p for p in rungs if p > 24]
say(len(lo) == len(hi) == 7 and all([sum(1 for p in s if p % 6 == 5), sum(1 for p in s if p % 6 == 1)] == [4, 3] for s in (lo, hi)), 'seven and seven across twenty-four, four one before a six and three one after with each seven')
say([(x['prime'], x['a']) for x in B] == [(e['prime'], e['b']) for e in A], 'the second list, each prime with its total, level and direction, has the same fourteen primes with the same scales')
print('      ' + ' · '.join(f"{e['prime']} {e['b']}" for e in A))
places = sorted({p % 24 for p in P if p > 3}); by = {r: {has(p) for p in P if p > 3 and p % 24 == r} for r in places}
say(places == [1, 5, 7, 11, 13, 17, 19, 23] and all(len(v) == 1 for v in by.values()) and len({next(iter(v)) for v in by.values()}) == 8,
    'each prime past three has one of eight places round a ring of twenty-four, and its forms of four are by its place, no two places the same: by each prime of the 1,024')
for r in places: print(f'      {r:2}: ' + ('; '.join(next(iter(by[r]))) or 'none of the four'))
rule = {k: {v % 24 for x in range(24) for y in range(24) for v in [x * x + k * y * y] if v % 2 and v % 3} for _, k in FORMS}
say(all(rule[k] == {r for r in places if name in next(iter(by[r]))} for name, k in FORMS),
    "by a rule's own lines, each two numbers by their places round twenty-four: a number with no two and no three in it, of one of the four forms, has a place of that form's primes")
say(sorted(p % 24 for p in lo) == [5, 7, 11, 13, 17, 19, 23] and lo == [5, 7, 11, 13, 17, 19, 23],
    "the ladder's first seven rungs, 5 to 23, are one prime with each place round twenty-four but 1: the fold at twenty-four is one round of the ring")
say([p % 24 for p in hi] == [5, 7, 13, 17, 19, 23, 5] and not prime(25) and not prime(35) and 25 == 5 * 5 and 35 == 5 * 7,
    'its next seven, 29 to 53, are with the places 5, 7, 13, 17, 19, 23 and 5 again; 25, five squared, and 35, five sevens, are no primes')
say(all((form(p, 3) is not None) == (p % 6 == 1) for p in rungs) and all((form(p, 3) is not None) == (p % 6 == 1) for p in P if p > 3),
    'each rung one after a six is a square and three of a square, and no rung one before a six is; and each prime past three of the 1,024 alike')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
