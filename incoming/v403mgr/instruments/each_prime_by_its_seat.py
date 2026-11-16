"""Each prime among the numbers 1 to 1,024, by its name sixteen on, its seat and its place on the surface.
Reads Exhibit ONE Natural Resolver's table of names, Exhibit THREE Natural Numbers, Exhibit FOUR Natural
Mathematics and Exhibit TWENTY-TWO Resolving the Hard Problem Registry; executes; writes no file; decides nothing.
Each answer is all or none at all: by each prime of the 1,024, or by a rule's own lines, each two numbers by
their names sixteen on.

Use: python3 -I incoming/v403mgr/instruments/each_prime_by_its_seat.py <root>        each check
     python3 -I incoming/v403mgr/instruments/each_prime_by_its_seat.py <root> csv    one line with each prime

The logic. A number's name sixteen on is its number with sixteens away, 1 to 16. 8 up brings each name onto
the name 8 apart, its seat's other name, Exhibit TWENTY-TWO Resolving the Hard Problem Registry: 1 with 9,
3 with 11, 5 with 13, 7 with 15. A field's words, of each whole number x and y: a prime past two is a square and
a square, x² + y², with one more than a four; a square and two of a square, x² + 2y², with one or three more
than an eight; a square less two of a square, x² − 2y², with one more or one less than an eight. Here each is
read by a name and a seat, and executed.

Returned at main, 16 November 2026, each check is:
  By a rule's own lines, each two numbers by their names sixteen on: an odd number a square and a square has
  a name 1, 5, 9 or 13, a name of root existing or discovering; an odd number a square and two of a square has
  a name 1, 3, 9 or 11, the routing's ring; an odd number a square less two of a square has a name 1, 7, 9 or 15.
  By each prime of the 1,024: each prime with a name 1, 5, 9 or 13 is a square and a square; each with a name
  1, 3, 9 or 11 a square and two of a square; each with a name 1, 7, 9 or 15 a square less two of a square.
  Each such prime is a square and a square one way alone, the squares of one square drawn corner to corner on a
  surface's lines, x along and y across; and a square and two of a square one way alone.
  Each seat of two odd names has its own forms, and no two seats the same: 1 and 9 each of the three; 3 and 11 a
  square and two of a square alone; 5 and 13 a square and a square alone; 7 and 15 a square less two of a
  square alone. 8 up brings each prime onto a number of its own seat, with its own forms.
  Each square has a name 1, 4, 9 or 16, itself a square, and each odd square a name 1 or 9, one seat.
  On the surface of 1,024 each line of diagonals of odd names, round the edges, is of one ring's names, and each
  line of even names between two of them has each of the eight even names; each prime past two is on a line of odd
  names; each prime on the routing's lines is a square and two of a square, and no prime on the other lines of
  odd names is.
  Each fold of the surface, 3 less to 1,025 less, brings each prime past two onto an even number; each turn, 2 up
  to 512 up, brings it onto an odd number.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers')
four = living('Exhibit_FOUR_Natural_Mathematics'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
for text, said in ((four, 'the reflected binary code'),
                   (three, '8 up and down, keeping odd or even; 17 less, podal within 1 to 16, exchanging odd and even'),
                   (three, '8 up: 2 and 23 with 1 and 9 add to five squared, 5 and 31 with 3 and 11 to six squared, 17 and 47 with 7 and 15 to eight squared')):
    assert said in text, said

# --- the seventeen names and their roots, Exhibit ONE Natural Resolver's table
NAME, ROOT = {}, {}
for n, name, root in re.findall(r'^\| (\d+) \| \*\*([^*]+)\*\* \| ([^|]+?) \|', one, re.M):
    NAME[int(n)], ROOT[int(n)] = name, root.split(',')[0]
assert sorted(NAME) == list(range(1, 18)) and all(NAME[n].startswith(f'{n}-') for n in NAME)
name_of = lambda n: (n - 1) % 16 + 1          # a number's name, sixteen on

# --- the ten unchangeables, each seated with a name and that name 8 up, Exhibit TWENTY-TWO
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
assert 'its name with now and that name 8 up with next, a 0, not changing' in seat
SEAT = {n: [] for n in range(1, 17)}
for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat):
    assert int(b) == int(a) + 8; SEAT[int(a)].append(what); SEAT[int(b)].append(what)
assert sum(len(v) for v in SEAT.values()) == 20

# --- the surface of 1,024, the reflected order, five parities down and five across
G = lambda n: (n - 1) ^ ((n - 1) >> 1)
def index(bits):
    i = 0
    for b in bits: i = i * 2 + (b ^ (i & 1))
    return i
PLACE = {}
for n in range(1, 1025):
    b = [(G(n) >> k) & 1 for k in range(10)]
    PLACE[n] = (index([b[k] for k in (9, 7, 5, 3, 1)]), index([b[k] for k in (8, 6, 4, 2, 0)]))
assert len(set(PLACE.values())) == 1024
RING = {0: '1-3-11-9', 2: '7-5-13-15'}
line = lambda n: (PLACE[n][1] - PLACE[n][0]) % 4      # a number's line of diagonals, of four

# --- each prime of the 1,024, and its forms
prime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
P = [n for n in range(1, 1025) if prime(n)]
root = lambda v: int(v ** 0.5 + 0.5) if v >= 0 and int(v ** 0.5 + 0.5) ** 2 == v else None
def two_squares(p):        # x² + y², x no less than y
    return next(((x, y) for y in range(0, int(p ** 0.5) + 1) for x in [root(p - y * y)] if x is not None and x >= y), None)
def square_and_two(p):     # x² + 2y²
    return next(((x, y) for y in range(0, int((p / 2) ** 0.5) + 1) for x in [root(p - 2 * y * y)] if x is not None), None)
def square_less_two(p):    # x² − 2y², its least
    return next(((x, y) for y in range(0, p + 1) for x in [root(p + 2 * y * y)] if x is not None), None)
FORMS = (('a square and a square', two_squares, {1, 5, 9, 13}, lambda x, y: f'{x}² + {y}²'),
         ('a square and two of a square', square_and_two, {1, 3, 9, 11}, lambda x, y: f'{x}² + 2 · {y}²'),
         ('a square less two of a square', square_less_two, {1, 7, 9, 15}, lambda x, y: f'{x}² − 2 · {y}²'))

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['prime', 'its position among primes', 'its name, sixteen on', 'its root', 'the unchangeable seated with its name and that name 8 apart',
                "its ring of the second surface's diagonals", 'a square and a square', 'a square and two of a square', 'a square less two of a square',
                'its line down, of thirty-two', 'its line across, of thirty-two', '8 up from it, a prime of its seat', '2 up from it, a prime'])
    for i, p in enumerate(P, 1):
        n = name_of(p)
        w.writerow([p, i, NAME[n], ROOT[n], ' · '.join(SEAT[n]), RING.get(line(p), '2-6-12-16' if n in (2, 6, 12, 16) else '8-4-14-10')]
                   + [(lambda s: show(*s) if s else '')(find(p)) for _, find, _, show in FORMS]
                   + [PLACE[p][0] + 1, PLACE[p][1] + 1, p + 8 if p + 8 <= 1024 and prime(p + 8) else '', p + 2 if p + 2 <= 1024 and prime(p + 2) else ''])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')

print(f'Each prime among the numbers 1 to 1,024, {len(P)} primes, by its name sixteen on:')
print("By a rule's own lines, each two numbers by their names sixteen on:")
by_rule = {what: {name_of(v) for x in range(16) for y in range(16) for v in [f(x, y) % 16] if v % 2}
           for what, f in (('a square and a square', lambda x, y: x * x + y * y), ('a square and two of a square', lambda x, y: x * x + 2 * y * y),
                           ('a square less two of a square', lambda x, y: x * x - 2 * y * y))}
say(by_rule['a square and a square'] == {1, 5, 9, 13} and {ROOT[n] for n in (1, 5, 9, 13)} == {'existing', 'discovering'}
    and all(ROOT[n] not in ('existing', 'discovering') for n in range(1, 17) if n not in (1, 5, 9, 13)),
    'an odd number a square and a square has a name 1, 5, 9 or 13: each name of root existing or discovering, and no other')
say(by_rule['a square and two of a square'] == {1, 3, 9, 11}, "an odd number a square and two of a square has a name 1, 3, 9 or 11, the routing's ring")
say(by_rule['a square less two of a square'] == {1, 7, 9, 15}, 'an odd number a square less two of a square has a name 1, 7, 9 or 15')
print('By each prime of the 1,024:')
for what, find, names, show in FORMS:
    say(all((find(p) is not None) == (name_of(p) in names) for p in P if p > 2) and all(f(*find(p)) == p for p in P if find(p) for f in [
        {'a square and a square': lambda x, y: x * x + y * y, 'a square and two of a square': lambda x, y: x * x + 2 * y * y, 'a square less two of a square': lambda x, y: x * x - 2 * y * y}[what]]),
        f'each prime past two with a name {", ".join(map(str, sorted(names)))} is {what}, and no other prime past two is')
say(all(find(2) for _, find, _, _ in FORMS), 'two is each of the three: 1² + 1², 0² + 2 · 1² and 2² − 2 · 1²')
ways = lambda p, k: [(x, y) for y in range(1, int((p / k) ** 0.5) + 1) for x in [root(p - k * y * y)] if x is not None and (k > 1 or x >= y)]
say(all(len(ways(p, 1)) == 1 for p in P if name_of(p) in (1, 5, 9, 13)) and all(len(ways(p, 2)) == 1 for p in P if p > 2 and name_of(p) in (1, 3, 9, 11)),
    'each such prime is a square and a square one way alone, and a square and two of a square one way alone')
say(all(x * x + y * y == p and x > y > 0 for p in P if name_of(p) in (1, 5, 9, 13) for x, y in ways(p, 1)),
    'a square with its side x along and y across, corner to corner on the lines of a surface, has x² + y² of its squares: each prime with a name 1, 5, 9 or 13 is one such square, and no prime with a name 3, 7, 11 or 15 is one')
forms_of = lambda n: tuple(what for what, _, names, _ in FORMS if n in names)
seats = {(a, a + 8): forms_of(a) for a in (1, 3, 5, 7)}
say(all(forms_of(a) == forms_of(a + 8) for a in (1, 3, 5, 7)) and len(set(seats.values())) == 4 and seats[(1, 9)] == tuple(w for w, *_ in FORMS)
    and all(len(seats[k]) == 1 for k in ((3, 11), (5, 13), (7, 15))),
    'each seat of two odd names has its own forms, and no two seats the same: 1 and 9 each of the three; 3 and 11 a square and two of a square alone; 5 and 13 a square and a square alone; 7 and 15 a square less two of a square alone')
for (a, b), f in seats.items():
    print(f'      {NAME[a]} and {NAME[b]}, {" and ".join(SEAT[a])}: {"; ".join(f)}')
say({name_of(x * x) for x in range(1, 33)} == {1, 4, 9, 16} and {name_of(x * x) for x in range(1, 33, 2)} == {1, 9} and SEAT[1] == SEAT[9],
    'each square has a name 1, 4, 9 or 16, itself a square, and each odd square a name 1 or 9, one seat: by a rule\'s own lines, a number by its name sixteen on and sixteen further')
say(all(name_of(n + 8) == (name_of(n) + 7) % 16 + 1 and SEAT[name_of(n + 8)] == SEAT[name_of(n)] for n in range(1, 1017)),
    '8 up brings each number onto a number of its own seat, and each prime with it')
print('On the surface of 1,024, thirty-two by thirty-two:')
lines = {s: {name_of(n) for n in PLACE if line(n) == s} for s in range(4)}
say(lines[0] == {1, 3, 9, 11} and lines[2] == {5, 7, 13, 15} and lines[1] | lines[3] == {2, 4, 6, 8, 10, 12, 14, 16},
    "each line of diagonals of odd names, round the edges, is of one ring's names: 1, 3, 11, 9, and 7, 5, 13, 15, with a line of even names between each two")
say(lines[1] == lines[3] == {2, 4, 6, 8, 10, 12, 14, 16}, 'each line of even names between two of them has each of the eight even names')
say(all(line(p) in (0, 2) for p in P if p > 2), 'each prime past two is on a line of odd names')
say(all((square_and_two(p) is not None) == (line(p) == 0) for p in P if p > 2),
    "each prime on the routing's lines is a square and two of a square, and no prime on the other lines of odd names is")
say(all((n % 2) != ((c - n) % 2) for c in (3, 5, 9, 17, 33, 65, 129, 257, 513, 1025) for n in P if 2 < n < c)
    and all((n + 2 ** k) % 2 == 1 for k in range(1, 10) for n in P if n > 2),
    'each fold of the surface, 3 less to 1,025 less, brings each prime past two onto an even number; each turn, 2 up to 512 up, brings it onto an odd number')
pairs8 = [(p, p + 8) for p in P if p + 8 <= 1024 and prime(p + 8)]
print(f'      primes 8 up from a prime, each two of one seat, the first of them: {pairs8[:8]}')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
