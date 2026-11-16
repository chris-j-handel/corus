"""The sixteen names as a surface, and the surface on by fours to 1 to 1,024: each two numbers next to each other,
along or across and round each edge, one parity apart. Reads Exhibit ONE Natural Resolver's table of names,
Exhibit THREE Natural Numbers and Exhibit FOUR Natural Mathematics; executes; writes no file; decides nothing.
Each answer is all or none at all.

Use: python3 -I incoming/v403mgr/instruments/the_names_as_a_surface.py <root>         each surface, and each check
     python3 -I incoming/v403mgr/instruments/the_names_as_a_surface.py <root> json    the surfaces, for a sheet

The logic, each a living sentence. Exhibit FOUR Natural Mathematics: one cycle reaching each form of n parities one
parity at a time, the reflected order; with two parities a cycle is four, a right spiral. Four parities part as two
and two three ways: each way is one surface of the sixteen names, two parities down and two across. The working
v401atom's four by four, gathered, is the first of the three.

Returned at main, 16 November 2026, each check is:
  Three surfaces, each two names next to each other one parity apart. With the first, each four-cycling is a line
  across and each bi-folding a line down. With the second and the third, each four-cycling is a square of four and
  each bi-folding a square of four; the second goes round each square by the right and the third by its other hand.
  With the second: 9 less, with each eight, is left with right; 17 less is top with bottom; 8 apart is through the
  centre. Each bi-folding is the square about one meeting of the four four-cyclings: 3-11-6-14 about the centre,
  1-9-8-16 about the corner, 2-15-7-10 about the top and bottom edge, 4-13-5-12 about the left and right edge.
  Its two outer lines down are the eight ends of four moments, and its two inner the eight inward names.
  On by fours to 1 to 1,024, thirty-two by thirty-two: each square of four is a four-cycling, each four by four a
  1 to 17, each eight by eight a 1 to 65, each sixteen by sixteen a 1 to 257; 1,025 less is top with bottom, 513
  less with each five hundred twelve is left with right, and 512 apart is through the centre.
  Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a going round an edge of the second surface.
  9 less and then 17 less, one and then the other, take each name round its bi-folding's square: by the right with
  the first and third four-cyclings, by its other hand with the second and fourth; with 17 less first, the other way.
  The surface folds in onto 1-now-existing by 1,025 less and on to 17 less, 9 less, 5 less and 3 less, a line across
  and a line down one and then the other, each with no number with itself; each going out, 1 up to 512 up, is a
  part's turn through its own centre.
  The second surface's four diagonals are four rings, of odd names and of even names one and then the other:
  1-3-11-9, 2-6-12-16, 7-5-13-15, 8-4-14-10. The routing 1, 3, 11, 9, 17, 19, 27, 25 is each number with a name
  1, 3, 11 or 9: 2 up, 8 up, 2 down, 8 up; each sixteen's four are one diagonal of its four by four.
  Prior two added comes to its names again with twenty-four numbers and with no fewer; 4, 6, 10, 12 and 14 are with
  none of them. A sunflower's 21 and 34 are a 5 and a 2, and its 34 and 55 a 2 and a 7.
"""
import glob, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers'); four = living('Exhibit_FOUR_Natural_Mathematics')
for text, said in ((four, 'the reflected binary code'), (four, 'With two parities a cycle is four'),
                   (three, 'Eight-cycle 1-9-5-13-4-12-8-16 is eight ends of four moments'), (three, 'eight-cycle 2-15-7-11-3-14-6-10 their eight inward names')):
    assert said in text, said
G = lambda n: (n - 1) ^ ((n - 1) >> 1)          # the reflected order: each number's parities, one changing with each number
def index(bits):                                # a line's place by its parities, itself in the reflected order
    i = 0
    for b in bits: i = i * 2 + (b ^ (i & 1))
    return i
def surface(m, down, across):                   # 2m parities, m of them down and m across; the numbers 1 to 4 to the m
    g = {}
    for n in range(1, 4 ** m + 1):
        b = [(G(n) >> k) & 1 for k in range(2 * m)]
        g[(index([b[k] for k in down]), index([b[k] for k in across]))] = n
    return g
def apart(g, size):
    return all(bin(G(g[(r, c)]) ^ G(g[(r, (c + 1) % size)])).count('1') == 1 and bin(G(g[(r, c)]) ^ G(g[((r + 1) % size, c)])).count('1') == 1
               for r in range(size) for c in range(size))
def lie(g, S):
    P = [rc for rc, n in g.items() if n in S]; rows = sorted({r for r, c in P}); cols = sorted({c for r, c in P})
    if len(rows) == 1: return 'a line across'
    if len(cols) == 1: return 'a line down'
    near = lambda a: len(a) == 2 and (a[1] - a[0]) % 4 in (1, 3)
    return 'a square of four' if near(rows) and near(cols) else 'other'
def fold(g, size, f):
    P = {n: rc for rc, n in g.items()}; z = size - 1
    for label, m in (('left with right', lambda r, c: (r, z - c)), ('top with bottom', lambda r, c: (z - r, c)), ('through the centre', lambda r, c: (z - r, z - c)),
                     ('two down', lambda r, c: ((r + size // 2) % size, c)), ('two across', lambda r, c: (r, (c + size // 2) % size))):
        if all(g[m(*P[n])] == f(n) for n in P): return label
    return 'no one fold of this surface'
CYC = [set(range(4 * k + 1, 4 * k + 5)) for k in range(4)]; BF = {'1-9-8-16': {1, 9, 8, 16}, '2-15-7-10': {2, 15, 7, 10}, '3-11-6-14': {3, 11, 6, 14}, '4-13-5-12': {4, 13, 5, 12}}
THREE = {'first, fourth and third parity down, second and first across': ((3, 2), (1, 0)),
         'second, fourth and second parity down, third and first across': ((3, 1), (2, 0)),
         'third, fourth and first parity down, third and second across': ((3, 0), (2, 1))}
S = {k: surface(2, *v) for k, v in THREE.items()}; B = S[list(THREE)[1]]
def hand(g):   # a four-cycling's going round its square, by the right or by its other hand
    P = {n: rc for rc, n in g.items()}; (r1, c1), (r2, c2) = P[1], P[2]
    return 'by the right' if (r2 - r1, c2 - c1) == (0, 1) else 'by its other hand'
big = surface(5, (9, 7, 5, 3, 1), (8, 6, 4, 2, 0))
if WHAT == 'json':
    json.dump({'three': {k: [[g[(r, c)] for c in range(4)] for r in range(4)] for k, g in S.items()},
               'on by fours': [[big[(r, c)] for c in range(32)] for r in range(32)]}, sys.stdout); sys.exit()
say = lambda ok, label: print(f'  {"is" if ok else "is-not"} · {label}')
print('Four parities part as two and two three ways, each one surface of the sixteen names:')
for k, g in S.items():
    print(f'  the {k}')
    for r in range(4): print('      ' + ' '.join(f'{g[(r, c)]:2d}' for c in range(4)))
    print(f'      each two next to each other one parity apart: {"is" if apart(g, 4) else "is-not"}; each four-cycling {" and ".join(sorted({lie(g, x) for x in CYC}))}; each bi-folding {" and ".join(sorted({lie(g, x) for x in BF.values()}))}' + (f'; round each square {hand(g)}' if lie(g, CYC[0]) == 'a square of four' else ''))
print('The second surface, each four-cycling a square gone round by the right, and the four squares by the right:')
say(fold(B, 4, lambda n: 9 - n if n < 9 else 25 - n) == 'left with right', '9 less, with each eight, is left with right')
say(fold(B, 4, lambda n: 17 - n) == 'top with bottom', '17 less is top with bottom')
say(fold(B, 4, lambda n: n + 8 if n < 9 else n - 8) == 'through the centre', '8 apart is through the centre: 9 less and then 17 less')
P = {n: rc for rc, n in B.items()}
about = {'3-11-6-14': {(1, 1), (1, 2), (2, 1), (2, 2)}, '1-9-8-16': {(0, 0), (0, 3), (3, 0), (3, 3)}, '2-15-7-10': {(0, 1), (0, 2), (3, 1), (3, 2)}, '4-13-5-12': {(1, 0), (2, 0), (1, 3), (2, 3)}}
say(all({P[n] for n in BF[k]} == v for k, v in about.items()),
    'each bi-folding is the square about one meeting of the four four-cyclings: 3-11-6-14 about the centre, 1-9-8-16 about the corner, 2-15-7-10 about the top and bottom edge, 4-13-5-12 about the left and right edge')
say({B[(r, c)] for r in range(4) for c in (0, 3)} == {1, 9, 5, 13, 4, 12, 8, 16} and {B[(r, c)] for r in range(4) for c in (1, 2)} == {2, 15, 7, 11, 3, 14, 6, 10},
    'its two outer lines down are the eight ends of four moments, and its two inner lines down the eight inward names')
say(all(sorted((abs(P[a][0] - P[b][0]), abs(P[a][1] - P[b][1]))) == [0, 3] for a, b in ((4, 5), (8, 9), (12, 13), (16, 1))),
    'each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a going round an edge of the surface')
print('The second surface on by fours, 1 to 1,024, thirty-two by thirty-two:')
say(apart(big, 32), 'each two numbers next to each other, along or across and round each edge, are one parity apart')
block = lambda k: all(len({(r // k, c // k) for (r, c), n in big.items() if (n - 1) // (k * k) == q}) == 1 for q in range(1024 // (k * k)))
say(block(2) and block(4) and block(8) and block(16), 'each square of four is a four-cycling, each four by four a 1 to 17, each eight by eight a 1 to 65, each sixteen by sixteen a 1 to 257')
say(fold(big, 32, lambda n: 1025 - n) == 'top with bottom', '1,025 less is top with bottom')
say(fold(big, 32, lambda n: 513 - n if n < 513 else 1537 - n) == 'left with right', '513 less, with each five hundred twelve, is left with right')
say(fold(big, 32, lambda n: n + 512 if n < 513 else n - 512) == 'through the centre', '512 apart is through the centre')
Pb = {n: rc for rc, n in big.items()}
chain = living('Exhibit_THIRTY_Co-Chaining_Logic_Registry'); physics = living('Exhibit_EIGHTEEN_Natural_Physics')
for text, s in ((chain, '8 up is third and fourth parities inverting, 9 less and 17 less in sequence'), (three, 'podaling with each span gives a span below it'),
                (four, 'Bi-inversioning-co-recursioning is two consecutive inversions on different axes'), (physics, 'A drying drop leaves concentric rings')): assert s in text, s
print('8 up, 9 less and 17 less on the second surface: its turn through the centre and its two folds:')
f9 = lambda n: 9 - n if n < 9 else 25 - n
f17 = lambda n: 17 - n
def round_by(n, first, second):   # one fold and then the other, four times: the names it reaches, and its hand
    seq = [n]
    for k in range(4): seq.append((first if k % 2 == 0 else second)(seq[-1]))
    (r0, c0), (r1, c1), (r2, c2) = P[seq[0]], P[seq[1]], P[seq[2]]
    across = 1 if c1 > c0 else -1 if c1 < c0 else 0; down = 1 if r2 > r1 else -1 if r2 < r1 else 0
    if across == 0: down = 1 if r1 > r0 else -1; across = 1 if c2 > c1 else -1; turn_ = -down * across
    else: turn_ = across * down
    return seq, 'by the right' if turn_ > 0 else 'by its other hand'
say(all(round_by(n, f9, f17)[0][4] == n and set(round_by(n, f9, f17)[0]) == next(v for v in BF.values() if n in v) for n in range(1, 17)),
    '9 less and then 17 less, one and then the other, take each name round its bi-folding\'s square, to its name again with the fourth')
say(all((round_by(n, f9, f17)[1] == 'by the right') == ((n - 1) // 4 in (0, 2)) and round_by(n, f17, f9)[1] != round_by(n, f9, f17)[1] for n in range(1, 17)),
    'by the right with each name of the first and third four-cyclings, and by its other hand with each name of the second and fourth; with 17 less first, each the other way')
say(all(len({next(k for k, v in BF.items() if n in v) for n in c}) == 4 for c in CYC), 'each four-cycling has one name with each of the four bi-foldings: corner, edge, centre, edge')
print('The surface folding in onto 1-now-existing, and opening out from it, on by fours:')
ok_fold = ok_turn = True; lines = []
for j in range(10, 0, -1):
    cells = [Pb[n] for n in range(1, 2 ** j + 1)]; rows = sorted({r for r, c in cells}); cols = sorted({c for r, c in cells})
    ok_fold &= len(rows) * len(cols) == 2 ** j and rows == list(range(rows[0], rows[0] + len(rows))) and cols == list(range(cols[0], cols[0] + len(cols)))
    about_across = all(Pb[2 ** j + 1 - n] == (rows[0] + rows[-1] - Pb[n][0], Pb[n][1]) for n in range(1, 2 ** j + 1))
    about_down = all(Pb[2 ** j + 1 - n] == (Pb[n][0], cols[0] + cols[-1] - Pb[n][1]) for n in range(1, 2 ** j + 1))
    ok_fold &= about_across != about_down; lines.append('across' if about_across else 'down')
    ok_turn &= all(Pb[n + 2 ** (j - 1)] == (rows[0] + rows[-1] - Pb[n][0], cols[0] + cols[-1] - Pb[n][1]) for n in range(1, 2 ** (j - 1) + 1)) if j > 1 else True
say(ok_fold and lines == ['across', 'down'] * 5, 'the numbers 1 to 1,024, to 512, to 256 and on to 1 to 2 are each one whole part of the surface about one corner, and 1,025 less, 513 less, 257 less and on to 17 less, 9 less, 5 less and 3 less each fold that part about its middle line, a line across and a line down one and then the other, with no number with itself')
say(ok_turn, 'each going out, 1 up, 2 up, 4 up, 8 up and on to 512 up, is that part\'s turn through its own centre: its two folds, one and then the other')
say([(2 ** j + 2) // 2 for j in range(10, 0, -1)] == [2 ** (j - 1) + 1 for j in range(10, 0, -1)], 'each span is the span outward of it folded: 1,025, 513, 257, 129, 65, 33, 17, 9, 5, 3 and 2, Exhibit THREE Natural Numbers\'s chain')
assert '8 up: 2 and 23 with 1 and 9 add to five squared, 5 and 31 with 3 and 11 to six squared, 17 and 47 with 7 and 15 to eight squared' in three
print('The second surface by its diagonals, each a ring round its edges:')
say(all((B[(r, c)] + B[(r, (c + 1) % 4)]) % 2 == 1 and (B[(r, c)] + B[((r + 1) % 4, c)]) % 2 == 1 for r in range(4) for c in range(4))
    and all((big[(r, c)] + big[(r, (c + 1) % 32)]) % 2 == 1 and (big[(r, c)] + big[((r + 1) % 32, c)]) % 2 == 1 for r in range(32) for c in range(32)),
    'each two numbers next to each other, along or across, are one odd and one even, with sixteen names and with 1,024 numbers')
DIAG = [[B[(k, (k + s) % 4)] for k in range(4)] for s in range(4)]
say(DIAG == [[1, 3, 11, 9], [2, 6, 12, 16], [7, 5, 13, 15], [8, 4, 14, 10]], f'its four diagonals are four rings, of odd names and of even names one and then the other: {DIAG}')
up8 = lambda n: n + 8 if n < 9 else n - 8
say(all({up8(n) for n in DIAG[s]} == set(DIAG[s]) for s in (0, 2)) and {up8(n) for n in DIAG[1]} == set(DIAG[3]),
    '8 apart brings each ring of odd names onto itself, 1 with 9 and 3 with 11, 5 with 13 and 7 with 15, and each ring of even names onto the other')
say({f9(n) for n in DIAG[0]} == {f17(n) for n in DIAG[0]} == {8, 6, 14, 16} == {B[(k, 3 - k)] for k in range(4)},
    '9 less and 17 less each bring the diagonal 1, 3, 11, 9 onto the square\'s other diagonal, 8, 6, 14, 16, the two crossing in the centre')
route = [n for n in range(1, 1025) if (n - 1) % 16 + 1 in (1, 3, 11, 9)]; route = [x for k in range(0, len(route), 4) for x in (route[k], route[k + 1], route[k + 3], route[k + 2])]
steps = [b - a for a, b in zip(route, route[1:])]
say(route[:8] == [1, 3, 11, 9, 17, 19, 27, 25] and steps[:4] * (len(steps) // 4) == steps[:len(steps) // 4 * 4] and steps[:4] == [2, 8, -2, 8],
    'the routing 1, 3, 11, 9, 17, 19, 27, 25 and on is each number with a name 1, 3, 11 or 9: 2 up, 8 up, 2 down, 8 up, and again')
diag_of_block = all(sorted((abs(Pb[route[k + i]][0] - Pb[route[k + i + 1]][0]), abs(Pb[route[k + i]][1] - Pb[route[k + i + 1]][1])) for i in range(3)) == [(1, 1)] * 3 for k in range(0, len(route), 4))
say(diag_of_block, 'with 1,024 numbers each sixteen\'s four of the routing are one diagonal of its four by four, each next to its next by one line down and one line across: two parities with each move')
say(all((big[(k, k)] - 1) % 16 + 1 in (1, 3, 9, 11) for k in range(32)), 'each number on the whole surface\'s diagonal, corner to corner, has a name 1, 3, 9 or 11')
biology = living('Exhibit_SEVENTEEN_Natural_Biology'); assert 'consecutive Fibonacci numbers, 21 and 34, 34 and 55' in biology
print('Prior two added, each by its name among seventeen, sixteen on:')
f = [1, 1]
while len(f) < 50: f.append(f[-1] + f[-2])
names = [(x - 1) % 16 + 1 for x in f]
say(names[:24] == names[24:48] and all(any(names[i] != names[i + k] for i in range(24)) for k in range(1, 24)), f'prior two added comes to its names again with twenty-four numbers, and with no fewer: {names[:24]}')
say(sorted(set(range(1, 17)) - set(names)) == [4, 6, 10, 12, 14], 'of sixteen names, 4, 6, 10, 12 and 14 are with none of them')
print('  a sunflower\'s two families, Exhibit SEVENTEEN Natural Biology: 21 and 34 are a', (21 - 1) % 16 + 1, 'and a', (34 - 1) % 16 + 1, '; 34 and 55 a', (34 - 1) % 16 + 1, 'and a', (55 - 1) % 16 + 1)
print('  360, 440 and 880, each by its line down and its line across of thirty-two:', {n: (Pb[n][0] + 1, Pb[n][1] + 1) for n in (360, 440, 880)})
