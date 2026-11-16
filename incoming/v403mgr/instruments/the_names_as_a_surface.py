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
biology = living('Exhibit_SEVENTEEN_Natural_Biology'); assert 'consecutive Fibonacci numbers, 21 and 34, 34 and 55' in biology
print('Prior two added, each by its name among seventeen, sixteen on:')
f = [1, 1]
while len(f) < 50: f.append(f[-1] + f[-2])
names = [(x - 1) % 16 + 1 for x in f]
say(names[:24] == names[24:48] and all(any(names[i] != names[i + k] for i in range(24)) for k in range(1, 24)), f'prior two added comes to its names again with twenty-four numbers, and with no fewer: {names[:24]}')
say(sorted(set(range(1, 17)) - set(names)) == [4, 6, 10, 12, 14], 'of sixteen names, 4, 6, 10, 12 and 14 are with none of them')
print('  a sunflower\'s two families, Exhibit SEVENTEEN Natural Biology: 21 and 34 are a', (21 - 1) % 16 + 1, 'and a', (34 - 1) % 16 + 1, '; 34 and 55 a', (34 - 1) % 16 + 1, 'and a', (55 - 1) % 16 + 1)
print('  360, 440 and 880, each by its line down and its line across of thirty-two:', {n: (Pb[n][0] + 1, Pb[n][1] + 1) for n in (360, 440, 880)})
