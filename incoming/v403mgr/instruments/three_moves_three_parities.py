"""8 up, 9 less and 17 less among the sixteen names: three moves, three parities, three lines through one point.
Reads Exhibit ONE Natural Resolver, Exhibit THREE Natural Numbers, Exhibit FOUR Natural Mathematics and Exhibit
EIGHTEEN Natural Physics; executes; writes no file; decides nothing. Each answer is all or none at all, by each
name of sixteen, or by each number of 1,024.

Use: python3 -I incoming/v403mgr/instruments/three_moves_three_parities.py <root>         each check
     python3 -I incoming/v403mgr/instruments/three_moves_three_parities.py <root> json    the sixteen ways, for a sheet

The logic, each a living sentence. Exhibit THREE Natural Numbers: bi-inversioning-co-recursioning is one move
of three, 8 up and down, 17 less, and 9 less, 17 less and 8 down together. Exhibit FOUR Natural Mathematics: two
parities P inverted and Q inverted, their lines ninety degrees apart, make both inverted with one step; the
reflected order has one parity changing with each number. Exhibit EIGHTEEN Natural Physics: two cones through a
vertex, a 0, not changing; six one-way recursionings, three with each of two sides. A partner's suggesting: 8 up,
9 less and 17 less are three parities and three cones, six one-way unrelationings into a point.

Returned at main, 16 November 2026, each check is:
  Each of the three comes to its name again after two, with no name with itself; each two of them, one and then
  the other, either first, are the third. A name with the names it reaches by them is its bi-folding's four; the
  four have six pairings, two by each of the three.
  With the reflected order 9 less changes the third parity alone, 17 less the fourth alone, and 8 up the two
  together: Exhibit FOUR Natural Mathematics's P inverted, Q inverted, and both with one step. None changes the
  second or the first.
  Three parities, the fourth, the third, and the two the same or not, are the three partings of the four
  four-cyclings two and two. Each of the three moves changes two of them and not the third, and each parity is
  unchanged by one move alone.
  By their three parities the four four-cyclings are four corners of a cube, each two of them two parities apart,
  no two along one edge. Each move is a turn about one of the cube's three lines through its centre; the three
  lines meet in the centre, a point with no four-cycling; going out from it each way, the six goings are through
  the middles of the six pairings, one each.
  Each fold's middle is a between of Exhibit ONE Natural Resolver: 9 less between 4 and 5 and between 12 and 13,
  17 less between 8 and 9 and between 16 and 17.
  With 1,024 numbers each fold, 3 less to 1,025 less, with each of its span, changes one parity alone, the first
  to the tenth; each turn, 2 apart to 512 apart, changes two parities next to each other together.
  The sixteen ways of changing a name's four parities together, on the second surface round its edges: each name
  is reached from 1-now-existing by one way alone. One parity is a fold; two are a slide of two lines or a turn;
  three are a fold with a slide along its own line, Exhibit FOUR Natural Mathematics's three inverting together;
  four are a slide both ways. One and three exchange odd and even, and two and four do not. No way but none has
  a name with itself.
"""
import glob, itertools, os, re, sys
from fractions import Fraction as F

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
if WHAT == 'json': out = sys.stdout; sys.stdout = open(os.devnull, 'w')      # the sixteen ways alone, for a sheet
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers')
four = living('Exhibit_FOUR_Natural_Mathematics'); physics = living('Exhibit_EIGHTEEN_Natural_Physics')
for text, said in ((three, 'Bi-inversioning-co-recursioning is one move of three steps: 8 up and down, keeping odd or even; 17 less, podal within 1 to 16, exchanging odd and even; and 9 less, podal within 1 to 8, 17 less and 8 down together, exchanging odd and even.'),
                   (three, 'each row is a bi-folding**: 1-9-8-16, 2-15-7-10, 3-11-6-14 and 4-13-5-12'),
                   (three, "each podaling's middle between two stations of its span, four and a half, twelve and a half and twenty-four and a half"),
                   (four, 'With two parities P inverted and Q inverted, their lines ninety degrees apart, make both inverted with one step'),
                   (four, 'the reflected binary code'),
                   (one, 'Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a discovering'),
                   (physics, 'Double-cone is two cones through a vertex'),
                   (physics, 'as six one-way recursionings, three own-forward steps with each of two sides')):
    assert said in text, said

N = range(1, 17)
MOVES = {'9 less': lambda n: (9 if n < 9 else 25) - n,      # with each eight
         '17 less': lambda n: 17 - n,
         '8 up': lambda n: n + 8 if n < 9 else n - 8}       # 8 up and down, 8 apart
G = lambda n: (n - 1) ^ ((n - 1) >> 1)                       # the reflected order
par = lambda n, k: (G(n) >> (k - 1)) & 1                     # a number's k-th parity, the first to the tenth
cyc = lambda n: (n - 1) // 4 + 1                             # a name's four-cycling, first to fourth
PARITIES = {'the fourth': lambda n: par(n, 4), 'the third': lambda n: par(n, 3), 'the two, the same or not': lambda n: par(n, 4) ^ par(n, 3)}
ordinal = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth'}

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')

print('8 up, 9 less and 17 less among the sixteen names:')
say(all(m(m(n)) == n and m(n) != n for m in MOVES.values() for n in N), 'each of the three comes to its name again after two, and none has a name with itself')
say(all({a, b, c} == set(MOVES) and all(MOVES[b](MOVES[a](n)) == MOVES[c](n) for n in N) for a, b, c in itertools.permutations(MOVES)),
    'each two of them, one and then the other, either first, are the third')
BI = [tuple(map(int, b.split('-'))) for b in ('1-9-8-16', '2-15-7-10', '3-11-6-14', '4-13-5-12')]
say(all({n} | {m(n) for m in MOVES.values()} == set(b) for b in BI for n in b), "a name with the names it reaches by them is its bi-folding's four")
pairings = {b: {name: {frozenset((n, m(n))) for n in b} for name, m in MOVES.items()} for b in BI}
say(all(len(p[name]) == 2 and not frozenset.intersection(*p[name]) for p in pairings.values() for name in MOVES)
    and all(set().union(*p.values()) == {frozenset(c) for c in itertools.combinations(b, 2)} for b, p in pairings.items()),
    "a bi-folding's four names have six pairings, two by each of the three, each move's two with no name of both")
print(f'      1-9-8-16: ' + '; '.join(f'{name}, {" and ".join(sorted("-".join(map(str, sorted(q))) for q in pairings[BI[0]][name]))}' for name in MOVES))

print('By parities, the reflected order:')
changes = {name: {k for k in (1, 2, 3, 4) if any(par(m(n), k) != par(n, k) for n in N)} for name, m in MOVES.items()}
whole = all(all(par(m(n), k) != par(n, k) for n in N) for name, m in MOVES.items() for k in changes[name])
say(whole and changes == {'9 less': {3}, '17 less': {4}, '8 up': {3, 4}},
    '9 less changes the third parity alone, with each name; 17 less the fourth alone; 8 up the two together; none changes the second or the first')
partings = {p: frozenset(frozenset(c for c in (1, 2, 3, 4) if f(4 * c) == v) for v in (0, 1)) for p, f in PARITIES.items()}
say(all(len({f(n) for n in N if cyc(n) == c}) == 1 for f in PARITIES.values() for c in (1, 2, 3, 4))
    and set(partings.values()) == {frozenset((frozenset(a), frozenset({1, 2, 3, 4} - set(a)))) for a in ((1, 2), (1, 3), (1, 4))},
    'three parities, the fourth, the third, and the two the same or not, are the three partings of the four four-cyclings two and two')
for p, q in partings.items():
    print(f'      {p}: ' + ' from '.join(' and '.join(ordinal[c] for c in sorted(s)) for s in sorted(q, key=min)))
unchanged = {name: [p for p, f in PARITIES.items() if all(f(m(n)) == f(n) for n in N)] for name, m in MOVES.items()}
say(all(len(v) == 1 for v in unchanged.values()) and len({v[0] for v in unchanged.values()}) == 3
    and all(all(f(m(n)) != f(n) for n in N) for name, m in MOVES.items() for p, f in PARITIES.items() if p not in unchanged[name]),
    'each move changes two of the three and not the third, and each parity is unchanged by one move alone')
exchanges = {name: {frozenset((cyc(n), cyc(m(n)))) for n in N} for name, m in MOVES.items()}
say(exchanges == {'9 less': {frozenset((1, 2)), frozenset((3, 4))}, '17 less': {frozenset((1, 4)), frozenset((2, 3))}, '8 up': {frozenset((1, 3)), frozenset((2, 4))}},
    'each move exchanges the four four-cyclings two and two: 9 less first with second and third with fourth; 17 less first with fourth and second with third; 8 up first with third and second with fourth')
for name in MOVES:
    print(f'      {name}: not changing {unchanged[name][0]}; ' + ', '.join(' with '.join(ordinal[c] for c in sorted(e)) for e in sorted(exchanges[name], key=min)))

print('By their three parities, the four four-cyclings as corners of a cube:')
corner = {c: tuple(f(4 * c) for f in PARITIES.values()) for c in (1, 2, 3, 4)}
say(len(set(corner.values())) == 4 and all(sum(a != b for a, b in zip(corner[c], corner[d])) == 2 for c, d in itertools.combinations(corner, 2)),
    'the four four-cyclings are four corners of a cube, each two of them two parities apart, no two along one edge; its other four corners have no four-cycling')
half = F(1, 2); centre = tuple(sum(F(v[i]) for v in corner.values()) / 4 for i in range(3))
mid = lambda c, d: tuple((F(corner[c][i]) + corner[d][i]) / 2 for i in range(3))
axis_of = {name: list(PARITIES).index(unchanged[name][0]) for name in MOVES}        # the line a move turns about
say(centre == (half, half, half) and centre not in [tuple(map(F, v)) for v in corner.values()]
    and all(tuple(corner[cyc(m(4 * c))][i] for i in range(3)) == tuple(v if i == axis_of[name] else 1 - v for i, v in enumerate(corner[c])) for name, m in MOVES.items() for c in corner),
    "each move is a turn about one of the cube's three lines through its centre, and the three lines meet in the centre, a point with no four-cycling")
mids = {frozenset(e): mid(*sorted(e)) for name in MOVES for e in exchanges[name]}
say(len(set(mids.values())) == 6 and all(all(m[i] == half for i in range(3) if i != axis_of[name]) and m[axis_of[name]] in (0, 1) for name in MOVES for e in exchanges[name] for m in [mids[frozenset(e)]])
    and all({mids[frozenset(e)][axis_of[name]] for e in exchanges[name]} == {0, 1} for name in MOVES),
    "going out from the centre each way along the three lines, the six goings are through the middles of the six pairings, one each: each line through its own move's two")

print("Each fold's middle, a between:")
say({F(9, 2), F(25, 2)} == {F(4 + 5, 2), F(12 + 13, 2)} and {F(17, 2), F(33, 2)} == {F(8 + 9, 2), F(16 + 17, 2)}
    and all(MOVES['9 less'](a) == b for a, b in ((4, 5), (12, 13))) and all(MOVES['17 less'](a) == b for a, b in ((8, 9), (16, 1))),
    '9 less has its middle between 4 and 5 and, with the second eight, between 12 and 13; 17 less between 8 and 9 and, round the ring, between 16 and 17: the four betweens of Exhibit ONE Natural Resolver, two with each fold')

print('With 1,024 numbers, each fold and each turn:')
fold = lambda n, j: ((n - 1) ^ (2 ** j - 1)) + 1           # 2 to the j and one, less, with each 2 to the j
turn = lambda n, j: ((n - 1) ^ 2 ** j) + 1                 # 2 to the j apart
say(all(fold(n, j) == (2 ** j) * (2 * ((n - 1) >> j)) + 2 ** j + 1 - n for j in range(1, 11) for n in range(1, 1025))
    and all({k for k in range(1, 11) if par(fold(n, j), k) != par(n, k)} == {j} for j in range(1, 11) for n in range(1, 1025)),
    'each fold, 3 less to 1,025 less, with each of its span, changes one parity alone, the first to the tenth: a fold is one parity')
say(all({k for k in range(1, 11) if par(turn(n, j), k) != par(n, k)} == {j, j + 1} for j in range(1, 10) for n in range(1, 1025))
    and all(turn(n, j) == fold(fold(n, j), j + 1) for j in range(1, 10) for n in range(1, 1025)),
    'each turn, 2 apart to 512 apart, changes two parities next to each other together: its two folds, one and then the other')

print("The sixteen ways of changing a name's four parities together, on the second surface round its edges:")
assert 'Bi-tri-involutioning is an emanating from right spiral stable-forming, three inverting together, as an opposite form to its stable-forming' in four
assert 'A fold about a lays n on 2a less n, and a fold about a and then about b lays n on n more by twice b less a: two folds in sequence are no fold' in three
def index(bits):
    i = 0
    for b in bits: i = i * 2 + (b ^ (i & 1))
    return i
where = {n: (index([par(n, 4), par(n, 2)]), index([par(n, 3), par(n, 1)])) for n in N}; at = {v: n for n, v in where.items()}
assert [[at[(r, c)] for c in range(4)] for r in range(4)] == [[1, 2, 7, 8], [4, 3, 6, 5], [13, 14, 11, 12], [16, 15, 10, 9]]
def way(n, ks):                                              # a name with the parities ks changing together
    g = G(n)
    for k in ks: g ^= 1 << (k - 1)
    return next(m for m in N if G(m) == g)
def line(xs):                                                # one line's move of four places: none, a fold, or a slide of two
    if all(v == x for x, v in xs.items()): return 'none'
    if all(v == (x + 2) % 4 for x, v in xs.items()): return 'slide'
    assert any(all(v == (c - x) % 4 for x, v in xs.items()) for c in (1, 3)); return 'fold'
SAID = {('none', 'none'): 'none', ('fold', 'none'): 'a fold about a line across', ('none', 'fold'): 'a fold about a line down',
        ('slide', 'none'): 'a slide of two lines down', ('none', 'slide'): 'a slide of two lines across', ('fold', 'fold'): 'a turn about a meeting of four names',
        ('fold', 'slide'): 'a fold about a line across with a slide of two along it', ('slide', 'fold'): 'a fold about a line down with a slide of two along it',
        ('slide', 'slide'): 'a slide of two lines both ways'}
WAYS = []
for size in range(5):
    for ks in itertools.combinations((4, 3, 2, 1), size):
        down = line({where[n][0]: where[way(n, ks)][0] for n in N}); across = line({where[n][1]: where[way(n, ks)][1] for n in N})
        assert all(where[way(n, ks)] == (({'none': r, 'slide': (r + 2) % 4}.get(down, None) if down != 'fold' else where[way(n, ks)][0]), where[way(n, ks)][1]) for n in N for r in [where[n][0]])
        WAYS.append(dict(parities=ks, said=SAID[(down, across)], onto=way(1, ks), odd_even=all((way(n, ks) - n) % 2 == 1 for n in N), itself=any(way(n, ks) == n for n in N)))
if WHAT == 'json':
    import json
    ordinal_k = {4: 'fourth', 3: 'third', 2: 'second', 1: 'first'}
    json.dump([[' and '.join(ordinal_k[k] for k in w['parities']) or 'none', len(w['parities']), w['said'], w['onto'], 'exchanges odd and even' if w['odd_even'] else 'odd to odd, even to even'] for w in WAYS], out); sys.exit()
say(sorted(w['onto'] for w in WAYS) == list(N), 'each name is reached from 1-now-existing by one way alone of the sixteen')
kinds = lambda size: sorted(w['said'].split(' about ')[0].split(' of two')[0] + (' with a slide' if 'with a slide' in w['said'] else '') for w in WAYS if len(w['parities']) == size)
say(kinds(1) == ['a fold'] * 4 and kinds(2) == ['a slide'] * 2 + ['a turn'] * 4 and kinds(3) == ['a fold with a slide'] * 4 and kinds(4) == ['a slide'] and kinds(0) == ['none'],
    'one parity is a fold; two are a slide of two lines, the third with the first or the fourth with the second, or a turn, one parity of each way; three are a fold with a slide of two along its own line; four are a slide of two lines both ways')
say(all(w['odd_even'] == (len(w['parities']) % 2 == 1) for w in WAYS) and all(all((way(n, w['parities']) - n) % 2 == 0 for n in N) for w in WAYS if len(w['parities']) % 2 == 0),
    'one parity and three parities changing exchange odd and even, an opposite form; two and four do not')
say(all(not w['itself'] for w in WAYS if w['parities']), 'no way but none has a name with itself: each fold about a line between two lines of names, each turn about a meeting of four names')
turns = {w['parities']: {tuple(sorted({n, way(n, w['parities'])})) for n in N} for w in WAYS if w['said'].startswith('a turn')}
say(all(way(n, (4, 3)) == MOVES['8 up'](n) for n in N) and all(way(n, (2, 1)) == ((n - 1) ^ 2) + 1 for n in N),
    "of the four turns, the fourth with the third is 8 up, about the middle of each bi-folding's square, and the second with the first is 2 apart, about the middle of each four-cycling's square")
for w in WAYS: print(f"      {' and '.join(map(str, w['parities'])) or 'none'}: {w['said']}; 1 onto {w['onto']}")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
