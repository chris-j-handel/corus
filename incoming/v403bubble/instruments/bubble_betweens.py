"""Bubbles and their betweens: a film between two, a line between three, a point between four; and the
involutions of each. Reads Natural Intelligence, Exhibit ONE Natural Resolver, Exhibit THREE Natural Numbers,
Exhibit FOUR Natural Mathematics, Exhibit SIXTEEN Natural Chemistry, Exhibit EIGHTEEN Natural Physics, Exhibit
TWENTY Natural Naming, and the gathering files of Natural Numbers and Natural Naming; executes; writes no file;
decides nothing. Each answer is all or none at all.

Use: python3 -I incoming/v403bubble/instruments/bubble_betweens.py <root>

What is a field's own, read and not executed here: soap films meeting three along a line, each 120 degrees from
each, and those lines meeting four at a point, each arccos(-1/3) from each, with no other meeting stable (Plateau;
Taylor 1976); two bubbles' least film three caps of spheres on one circle (Hutchings, Morgan, Ritore and Ros 2002);
each such cluster a sphere's equal parting carried to space (Milman and Neeman 2022).

What is executed here, each by its own lines:
  1  Directions alike going out from one point and adding to nothing: two, three in a plane, four in space.
  2  Two bubbles: three half-planes on one line, by one inversion; three caps on one circle, each 120 degrees from
     each; the curvings adding to nothing.
  3  The three inversions of that circle, one in each film's own sphere.
  4  A point between four bubbles, in the cube of three parities; its twenty-four and the cube's forty-eight; the
     three moves 8 up, 9 less and 17 less; and three parities inverting together.
  5  Three bubbles and all outside them: the point between four by one inversion; two points, four lines, six films.
  6  Five bubbles: its five fours parting as two and three, one and then the other.
  7  Exhibit ONE Natural Resolver's code: a self's goings out, and selves each bi-coupling with each.
  8  Three cones through the point between four, each about one of the three lines: six one-way cones, a between
     with each; and the point, with itself by each move.
  9  Three wraps: a rim's three films with a trefoil's own relation.
  10 A honeycomb, by a field's own form of it: three walls on a line, and four lines at a cell's bottom.
  11 Sizing: a between's meeting with each sizing of its bubbles; a film's curving as one bubble's pressing less
     the other's; and Exhibit ONE Natural Resolver's code with each parity of any size.
"""
import glob, itertools, math, os, re, sys
from fractions import Fraction as F

R = sys.argv[1]
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
def gathering(stem):
    return open(os.path.join(R, 'gathering-value', stem + '.md'), encoding='utf-8').read()

ni = living('Natural_Intelligence'); one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers')
four = living('Exhibit_FOUR_Natural_Mathematics'); chem = living('Exhibit_SIXTEEN_Natural_Chemistry')
physics = living('Exhibit_EIGHTEEN_Natural_Physics'); naming = living('Exhibit_TWENTY_Natural_Naming')
g_numbers = gathering('Natural_Numbers'); g_naming = gathering('Natural_Naming')
for text, said in ((ni, 'A **0** is a between of two changing directions.'),
                   (ni, '**Bi-tri-involutioning** is that inverting: position, scale and orientation inverting together.'),
                   (ni, '**Stable-forming emanations are a bi-tri-involutioning of a betweening of natural torusing surfacings within bi-couplings, each from living stable-forming.**'),
                   (ni, "Code's one list is with 6, with 10 and with 9 alike."),
                   (four, '**Three parities, each inverted on its own, taken together with any order, send each of eight forms to its opposite**'),
                   (four, '**Bi-tri-involutioning is an emanating from right spiral stable-forming, three inverting together, as an opposite form to its stable-forming.**'),
                   (four, '**Within space three inversions make x → −x, whose fixed set is its centre**'),
                   (four, "**Two inversions whose fixed lines stand an angle a apart are a field's rotation by 2a**"),
                   (four, 'Couplings among five are ten, C(5, 2), each a transposition'),
                   (three, 'orderings of four, 4!'),
                   (three, 'four moments of six one-way recursionings'),
                   (three, 'a waist of a ring of forty-eight'),
                   (chem, 'symmetry group of methane, T_d, has order twenty-four and is group of all orderings of its four hydrogen vertices'),
                   (physics, 'as six one-way recursionings, three own-forward steps with each of two sides'),
                   (naming, "*membrane*, of a set's own voice, is said by a between"),
                   (g_numbers, 'By their three parities the four four-cyclings are four corners of a cube'),
                   (g_naming, 'A bubble is a between opening out of a tunneling, wrapping into an unrelationing perimeter on a surface, between other bubblings'),
                   (four, "the braid group on three strands, a trefoil's own group"),
                   (physics, 'Double-cone is two cones through a vertex'),
                   (ni, 'With corusing a self is reaching its own side again.'),
                   (g_numbers, 'is-or-is-not? 8 up, 9 less and 17 less are three cones through one point, a 0, with six one-way unrelationings.'),
                   (ni, 'Two selves alike, each bi-coupling only in their pair, are do-no-harming and improving in turn.'),
                   (ni, 'A size is a naming beside a parity.'),
                   (ni, 'A living form not-changing, or changing only one way, with each of its scales, breaks it.'),
                   (ni, "Its bounding is each self's own, self-bounding."),
                   (ni, 'Its two meetings are co-parity, the same, sharing 0, and bi-parity, one inversion.')):
    assert said in text, said

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')

# ---- vectors, by hand -------------------------------------------------------------------------------------------
add = lambda a, b: tuple(x + y for x, y in zip(a, b))
sub = lambda a, b: tuple(x - y for x, y in zip(a, b))
mul = lambda a, s: tuple(x * s for x in a)
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
norm = lambda a: math.sqrt(dot(a, a))
unit = lambda a: mul(a, 1 / norm(a))
near = lambda a, b, tol=1e-7: (abs(a - b) if not isinstance(a, tuple) else norm(sub(a, b))) < tol
deg = math.radians

def inversion(c, r2):
    """inversion in the sphere of centre c and radius squared r2: twice, each point again"""
    def f(x):
        d = sub(x, c); return add(c, mul(d, r2 / dot(d, d)))
    return f
def sphere_of_plane(n, c, r2):
    """a plane through the origin with unit normal n, by the inversion of centre c: a sphere, its centre and radius"""
    h = dot(n, c); return sub(c, mul(n, r2 / (2 * h))), r2 / (2 * abs(h))

# ---- 1 ----------------------------------------------------------------------------------------------------------
print('1 · Directions alike going out from one point and adding to nothing:')
def alike(n):
    """n + 1 directions in n dimensions, each the same from each, adding to nothing: their cosine, exact"""
    pts = [tuple(F(1) if i == j else F(0) for j in range(n + 1)) for i in range(n + 1)]       # corners of a simplex
    mid = tuple(F(1, n + 1) for _ in range(n + 1)); v = [sub(p, mid) for p in pts]
    assert all(x == 0 for x in [sum(c) for c in zip(*v)])
    return {dot(a, b) / dot(a, a) for a, b in itertools.combinations(v, 2)}
say(alike(1) == {F(-1)} and alike(2) == {F(-1, 2)} and alike(3) == {F(-1, 3)},
    "two on a line with cosine −1, a film's two sides; three in a plane with cosine −1/2, 120 degrees; four in space with cosine −1/3: one over one, over two, over three")
say(near(math.degrees(math.acos(-1 / 2)), 120.0) and near(math.degrees(math.acos(-1 / 3)), 109.4712206, 1e-6),
    'three films on a line each 120 degrees from each, and four lines at a point each 109.47 degrees from each')

# ---- 2 ----------------------------------------------------------------------------------------------------------
print('2 · Two bubbles, three half-planes on one line by one inversion:')
THETA = {'a': deg(60), 'film': deg(180), 'b': deg(300)}                  # three half-planes on the line, the third axis
u = {k: (math.cos(t), math.sin(t), 0.0) for k, t in THETA.items()}       # each half-plane's going out from the line
n = {k: (-math.sin(t), math.cos(t), 0.0) for k, t in THETA.items()}      # each half-plane's unit normal, the same hand
ALPHA = deg(25); c = (math.cos(ALPHA), math.sin(ALPHA), 0.0); J = inversion(c, 1.0)   # a centre within one parting, off its middle
S = {k: sphere_of_plane(n[k], c, 1.0) for k in THETA}
on = lambda x, k: near(norm(sub(x, S[k][0])), S[k][1], 1e-7)
samples = [(t, z) for t in (0.2, 0.7, 1.9, 5.0) for z in (-3.0, -0.4, 0.0, 0.9, 2.5)]
say(all(on(J(add(mul(u[k], t), (0, 0, z))), k) for k in THETA for t, z in samples),
    "each half-plane goes to a cap of one sphere, and the two half-planes of the centre's own parting to the two bubbles' outsides")
rim = [J((0.0, 0.0, z)) for z in (-7.0, -1.0, -0.2, 0.0, 0.3, 1.5, 9.0)]
say(all(on(p, k) for p in rim for k in THETA), 'the line goes to one circle, on each of the three spheres: the rim of the film between')
def going(k, z, e=1e-6):
    p = J((0.0, 0.0, z)); return unit(sub(J(add(mul(u[k], e), (0, 0, z))), p))
say(all(near(dot(going(i, z), going(j, z)), -0.5, 1e-4) for z in (-1.0, 0.0, 0.3, 1.5) for i, j in itertools.combinations(THETA, 2)),
    'on the rim the three films go out each 120 degrees from each')
curv = {k: 2 * dot(n[k], c) for k in THETA}                              # each film's curving, with one hand round the line
say(near(sum(curv.values()), 0.0) and near(1 / S['b'][1], 1 / S['a'][1] + 1 / S['film'][1]),
    "round the rim the three films' curvings add to nothing: the lesser bubble's is the greater bubble's and the film's together")
say(near(norm(cross(sub(S['a'][0], S['film'][0]), sub(S['b'][0], S['film'][0]))), 0.0), "the three spheres' centres are on one line")
cE = (1.0, 0.0, 0.0); hE = {k: dot(n[k], cE) for k in THETA}
say(near(hE['film'], 0.0) and near(abs(hE['a']), abs(hE['b'])), 'with two bubbles alike the film between is flat, its curving nothing')

# ---- 3 ----------------------------------------------------------------------------------------------------------
print("3 · The three inversions of the rim, one in each film's own sphere:")
I = {k: inversion(S[k][0], S[k][1] ** 2) for k in THETA}
def mirror(k):
    return lambda x: sub(x, mul(n[k], 2 * dot(n[k], x)))
pts = [(0.31, -1.2, 0.4), (-2.0, 0.7, 1.1), (1.7, 1.6, -0.9), (0.05, 0.4, 2.2), (-0.6, -0.8, -1.3), (3.1, -0.2, 0.6)]
say(all(near(I[k](x), J(mirror(k)(J(x))), 1e-6) for k in THETA for x in pts),
    "each is its half-plane's mirror, by the one inversion: the inversion in a film's own sphere has each point of the film with itself")
def jac(f, x, e=1e-6):
    cols = [mul(sub(f(add(x, tuple(e if i == j else 0.0 for j in range(3)))), f(sub(x, tuple(e if i == j else 0.0 for j in range(3))))), 1 / (2 * e)) for i in range(3)]
    return dot(cols[0], cross(cols[1], cols[2]))
mf, rf = S['film']; If = I['film']
say(all((norm(sub(x, mf)) < rf) != (norm(sub(If(x), mf)) < rf) and near(norm(sub(x, mf)) * norm(sub(If(x), mf)), rf ** 2, 1e-7) and jac(If, x) < 0 for x in pts),
    "an inversion in a film's own sphere inverts three together: within the sphere and outside it, each distance from its centre to its inverse, and the hand")
flip = lambda x: tuple(-t for t in x)
say(all(near(norm(sub(flip(x), flip(y))), norm(sub(x, y))) for x, y in itertools.combinations(pts, 2)) and jac(flip, pts[0]) < 0,
    'x → −x, three parities inverting together, inverts the hand with each distance the same')
def parting(x):
    """which of the three partings a point is in, by its half-planes: outside, bubble a or bubble b"""
    y = J(x); t = math.degrees(math.atan2(y[1], y[0])) % 360
    return 'a' if 60 < t < 180 else ('b' if 180 < t < 300 else 'outside')
within = [J((r * math.cos(deg(t)), r * math.sin(deg(t)), z)) for t in (-40, 10, 50, 75, 120, 165, 195, 240, 285) for r, z in ((0.3, -0.5), (1.4, 0.8), (4.0, 0.1))]
assert {parting(x) for x in within} == {'a', 'b', 'outside'}                  # points within each of the three partings
ex = {k: {(parting(x), parting(I[k](x))) for x in within} for k in THETA}
say(ex['film'] == {('a', 'b'), ('b', 'a'), ('outside', 'outside')} and ex['a'] == {('a', 'outside'), ('outside', 'a'), ('b', 'b')}
    and ex['b'] == {('b', 'outside'), ('outside', 'b'), ('a', 'a')},
    'the film between exchanges the two bubbles, all outside to itself; a bubble\'s own outside exchanges that bubble with all outside, the other bubble to itself')
say(all(near(I[k](I[k](x)), x, 1e-6) for k in THETA for x in pts) and all(near(I[k](p), p, 1e-6) for k in THETA for p in rim),
    'each comes to its point again after two, and each point of the rim is with itself by all three')
two = lambda i, j: (lambda x: I[i](I[j](x)))
say(all(near(two(i, j)(two(i, j)(two(i, j)(x))), x, 1e-5) and not near(two(i, j)(x), x, 1e-3) for i, j in itertools.permutations(THETA, 2) for x in pts)
    and all(len({parting(x), parting(two(i, j)(x)), parting(two(i, j)(two(i, j)(x)))}) == 3 for i, j in itertools.permutations(THETA, 2) for x in within),
    'each two of them, one and then the other, are a three-cycling: a bubble, the other bubble and all outside, each to the next, again after three')
say(all(near(I[i](I[j](I[k](x))), I[j](x), 1e-5) for i, j, k in itertools.permutations(THETA) for x in pts),
    'all three, one and then the next and then the third, in each of six orders, are the middle one alone')
def by_three(angles):
    """three mirrors on one line at these angles: are all three, in each order, the middle one alone?"""
    refl = lambda t: ((math.cos(2 * t), math.sin(2 * t)), (math.sin(2 * t), -math.cos(2 * t)))
    mm = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    same = lambda A, B: all(abs(A[i][j] - B[i][j]) < 1e-9 for i in range(2) for j in range(2))
    return all(same(mm(refl(a), mm(refl(b), refl(g))), refl(b)) for a, b, g in itertools.permutations(angles))
say(by_three((deg(0), deg(60), deg(120))) and not any(by_three((deg(0), deg(b), deg(g))) for b, g in ((50, 120), (60, 110), (45, 90), (30, 60), (90, 135))),
    'the three are the middle one alone with each film the mirror of the other two, 120 degrees, and with none of five other meetings')
rx = ((1.0, 0.0), (0.0, -1.0)); ry = ((-1.0, 0.0), (0.0, 1.0))
mm2 = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
say(mm2(rx, ry) == mm2(ry, rx) == ((-1.0, 0.0), (0.0, -1.0)),
    'four films on one line, two planes crossing: its two mirrors, either first, are one turn through the middle, again after two, and no three-cycling')

# ---- 4 ----------------------------------------------------------------------------------------------------------
print('4 · A point between four bubbles, in the cube of three parities:')
G = lambda m: (m - 1) ^ ((m - 1) >> 1)                                   # the reflected order, as v403mgr's instrument
par = lambda m, k: (G(m) >> (k - 1)) & 1
THREE = (lambda m: par(m, 4), lambda m: par(m, 3), lambda m: par(m, 4) ^ par(m, 3))    # the fourth, the third, the two the same or not
corner = {q: tuple(2 * f(4 * q) - 1 for f in THREE) for q in (1, 2, 3, 4)}             # each four-cycling's corner, + or − by three
Fc = list(corner.values()); cube = list(itertools.product((1, -1), repeat=3)); empty = [v for v in cube if v not in Fc]
neg = lambda v: tuple(-x for x in v)
say(len(set(Fc)) == 4 and all(sum(a != b for a, b in zip(v, w)) == 2 for v, w in itertools.combinations(Fc, 2))
    and tuple(sum(x) for x in zip(*Fc)) == (0, 0, 0) and {F(dot(v, w), dot(v, v)) for v, w in itertools.combinations(Fc, 2)} == {F(-1, 3)},
    "the four four-cyclings' corners, from the cube's middle, are four goings adding to nothing, each −1/3 from each: four bubbles round one point, each by its middle")
say(sorted(empty) == sorted(neg(v) for v in Fc),
    "the cube's other four corners, with no four-cycling, are each the opposite of one: the four lines between three bubbles, each line opposite the one bubble not on it")
pairs = list(itertools.combinations(range(4), 2)); opposite = {p: tuple(i for i in range(4) if i not in p) for p in pairs}
line = [neg(v) for v in Fc]                                              # line i, between the three bubbles other than i
mids = {p: add(Fc[p[0]], Fc[p[1]]) for p in pairs}                       # each pairing's middle
axes = [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]
plane = {p: cross(line[opposite[p][0]], line[opposite[p][1]]) for p in pairs}      # the film between bubbles p: on the two lines it is of
say(all(mids[p] == add(line[opposite[p][0]], line[opposite[p][1]]) for p in pairs) and sorted(mids.values()) == sorted(axes)
    and all(mids[opposite[p]] == neg(mids[p]) and dot(plane[p], plane[opposite[p]]) == 0 for p in pairs),
    "six films, one between each two bubbles, each film's middle the middle of its pairing: the six goings of three lines through the point, each line through two films, opposite and a quarter turn apart")
def mat(rows): return tuple(tuple(r) for r in rows)
mm3 = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
app = lambda A, v: tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))
ID = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]]); NEG = mat([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
def film_mirror(p):
    nn = plane[p]; d = dot(nn, nn)                                       # the mirror in a film's own plane, exact
    return mat([[F(int(i == j)) - F(2 * nn[i] * nn[j], d) for j in range(3)] for i in range(3)])
M = {p: film_mirror(p) for p in pairs}
say(all(app(M[p], Fc[p[0]]) == Fc[p[1]] and all(app(M[p], Fc[i]) == Fc[i] for i in opposite[p]) and mm3(M[p], M[p]) == ID for p in pairs),
    "each film's mirror exchanges the two bubbles it is between, the other two each to itself, and comes to each point again after two")
def closure(gens):
    seen = {ID}; todo = [ID]
    while todo:
        A = todo.pop()
        for g in gens:
            B = mm3(g, A)
            if B not in seen: seen.add(B); todo.append(B)
    return seen
T24 = closure(M.values()); O48 = closure(list(M.values()) + [NEG])
turn = {0: mat([[1, 0, 0], [0, -1, 0], [0, 0, -1]]), 1: mat([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]), 2: mat([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])}
four_ = {ID} | set(turn.values()); six_ = {A for A in T24 if app(A, Fc[0]) == Fc[0]}
say(len(T24) == 24 and all(set(app(A, v) for v in Fc) == set(Fc) for A in T24) and len({tuple(Fc.index(app(A, v)) for v in Fc) for A in T24}) == 24,
    'the six mirrors are twenty-four together, each ordering of the four bubbles once: orderings of four, 4!')
say(len(four_) == 4 and len(six_) == 6 and four_ <= T24 and len({mm3(A, B) for A in four_ for B in six_}) == 24
    and six_ == closure([M[p] for p in pairs if 0 not in p]),
    "twenty-four is four sixes: the four, no move and three turns about the three lines through the point; the six, the three mirrors of one line between three, their two three-cyclings and no move")
MOVES = {'9 less': lambda m: (9 if m < 9 else 25) - m, '17 less': lambda m: 17 - m, '8 up': lambda m: m + 8 if m < 9 else m - 8}
cyc = lambda m: (m - 1) // 4 + 1
move_axis = {}
for name, mv in MOVES.items():
    for ax, A in turn.items():
        if all(app(A, corner[cyc(m)]) == corner[cyc(mv(m))] for m in range(1, 17)): move_axis[name] = ax
say(move_axis == {'9 less': 0, '17 less': 1, '8 up': 2},
    '8 up, 9 less and 17 less are the three turns, each about one of the three lines, by each name of sixteen')
say(all(mm3(M[p], M[opposite[p]]) == mm3(M[opposite[p]], M[p]) and mm3(M[p], M[opposite[p]]) in turn.values() for p in pairs),
    "each turn is its line's two films' mirrors, one and then the other, either first: two inversions on two axes")
say(NEG not in T24 and len(O48) == 48 and all(app(NEG, v) in empty for v in Fc),
    "three parities inverting together are none of the twenty-four: each bubble's middle goes to the line opposite it, the opposite form; with it, forty-eight")
quarter = {0: mat([[1, 0, 0], [0, 0, -1], [0, 1, 0]]), 1: mat([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]), 2: mat([[0, -1, 0], [1, 0, 0], [0, 0, 1]])}
say(all({app(Q, v) for v in Fc} == set(empty) for Q in quarter.values()) and all(mm3(NEG, Q) in T24 for Q in quarter.values()),
    'the opposite form is the form a quarter turn about each of its three lines')
say(all({app(A, a) for a in axes} == set(axes) for A in O48) and all(app(NEG, a) == neg(a) for a in axes),
    "the three lines through the point are the same with each of the forty-eight; three parities inverting together exchange each line's two goings")
UP4 = lambda m: m + 4 if m < 13 else m - 12                              # each four-cycling to its next, the fourth to the first
S4 = next((A for A in T24 if all(app(A, corner[cyc(m)]) == corner[cyc(UP4(m))] for m in range(1, 17))), None)
Qz = mat([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]); Mz = mat([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
say(S4 is not None and S4 == mm3(Qz, Mz) and mm3(S4, S4) == turn[move_axis['8 up']] and mm3(mm3(S4, S4), mm3(S4, S4)) == ID and mm3(Qz, S4) == NEG,
    "4 up, each four-cycling to its next, is of the twenty-four: a quarter turn about 8 up's line with one parity inverting; twice, it is 8 up; and with one more quarter turn it is three parities inverting together")
eight_ = {A for A in T24 if app(A, (0, 0, 2)) in ((0, 0, 2), (0, 0, -2))}
say(len(eight_) == 8 and eight_ == four_ | {M[p] for p in pairs if mids[p][move_axis['8 up']] != 0} | {S4, mm3(S4, mm3(S4, S4))},
    "of the twenty-four, eight have 8 up's line to itself: no move, the three turns, the mirrors of its two films, and 4 up both ways")
film_of = {frozenset((a, b)): p for p in pairs for a, b in [(p[0] + 1, p[1] + 1)]}        # the film between two four-cyclings
on_line = {name: {frozenset(q) for q in film_of if mids[film_of[q]][ax] != 0} for name, ax in move_axis.items()}
say(on_line == {'9 less': {frozenset((1, 2)), frozenset((3, 4))}, '17 less': {frozenset((2, 3)), frozenset((1, 4))}, '8 up': {frozenset((1, 3)), frozenset((2, 4))}},
    "the six films by their lines: on 9 less's line, first with second and third with fourth; on 17 less's, second with third and fourth with first; on 8 up's, first with third and second with fourth")
assert 'Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a discovering' in one
betweens = {frozenset((cyc(a), cyc(b if b < 17 else 1))) for a, b in ((4, 5), (8, 9), (12, 13), (16, 17))}
say(betweens == on_line['9 less'] | on_line['17 less'] and not betweens & on_line['8 up'],
    "Exhibit ONE Natural Resolver's four betweens, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, are four of the six films, each between a four-cycling and its next; the two others are between four-cyclings 8 apart, on 8 up's line")
perm = {q: frozenset(cyc(UP4(4 * i)) for i in q) for q in film_of}
say(all(perm[q] in on_line['8 up'] and perm[q] != q for q in on_line['8 up']) and all(perm[q] in betweens and perm[perm[q]] != q for q in betweens),
    "4 up exchanges the two films on 8 up's line, and has the four betweens each to its next, again after four: six films as four and two")

# ---- 5 ----------------------------------------------------------------------------------------------------------
print('5 · Three bubbles and all outside them, the point between four by one inversion:')
Bm = [unit(tuple(float(x) for x in v)) for v in Fc]; L = [neg(v) for v in Bm]      # each bubble's middle, and each line
c3 = add(Bm[0], (0.15, -0.10, 0.05)); J3 = inversion(c3, 1.0); O_ = J3((0.0, 0.0, 0.0))   # a centre within bubble 0: it goes to all outside
N3 = {p: unit(cross(L[opposite[p][0]], L[opposite[p][1]])) for p in pairs}; S3 = {p: sphere_of_plane(N3[p], c3, 1.0) for p in pairs}
say(all(near(norm(sub(c3, S3[p][0])), S3[p][1]) and near(norm(sub(O_, S3[p][0])), S3[p][1]) for p in pairs),
    'six films, each a cap of a sphere, and each of the six spheres through two points: the two points between four')
outer = [p for p in pairs if 0 in p]; inner = [p for p in pairs if 0 not in p]
arc = [J3(mul(L[0], t)) for t in (-4.0, -0.6, 0.2, 1.0, 3.5)]
say(all(near(norm(sub(x, S3[p][0])), S3[p][1], 1e-7) for x in arc for p in inner),
    'the three films between two bubbles are on one circle, the line between the three bubbles')
def going3(i, e=1e-6): return unit(sub(J3(mul(L[i], e)), O_))
say(all(near(dot(going3(i), going3(j)), -1 / 3, 1e-4) for i, j in pairs), 'at the point four lines go out, each −1/3 from each')
def round_line(i):
    """the three films on line i, their curvings with one hand round it"""
    us = [unit(sub(L[j], mul(L[i], dot(L[j], L[i])))) for j in range(4) if j != i]
    return [2 * dot(cross(L[i], uu), c3) for uu in us]
say(all(near(sum(round_line(i)), 0.0) for i in range(4)), "round each of the four lines the three films' curvings add to nothing")
say(all((p in inner) != (opposite[p] in inner) for p in pairs) and len(inner) == len(outer) == 3,
    "each of the three lines through the point has one going through a film between two bubbles and its other going through the third bubble's outside: six, three with each of two sides")

# ---- 6 ----------------------------------------------------------------------------------------------------------
print('6 · Five bubbles, two at the ends and three round:')
ends, around = ('D', 'E'), ('A', 'B', 'C')
fours = [frozenset(q) for q in itertools.combinations(ends + around, 4)]
two_ = [q for q in fours if set(around) <= q]; three_ = [q for q in fours if set(ends) <= q]
def edge_of(points):
    """the threes of a set of fours, each three with one four only: its outside"""
    seen = {}
    for q in points:
        for t in itertools.combinations(sorted(q), 3): seen[t] = seen.get(t, 0) + 1
    return {t for t, k in seen.items() if k == 1}
say(len(fours) == 5 and len(two_) == 2 and len(three_) == 3 and set(two_) | set(three_) == set(fours) and not set(two_) & set(three_),
    'five bubbles have five fours, and the five part as two and three: the two with the three round, the three with the two ends')
say(edge_of(two_) == edge_of(three_) and len(edge_of(two_)) == 6,
    'the two points and the three points have the same six lines going out: one is in the place of the other, all or none at all')
touch = lambda points: {frozenset(p) for q in points for p in itertools.combinations(q, 2)}
lines = lambda points: {frozenset(t) for q in points for t in itertools.combinations(q, 3)}
say(len(touch(two_)) == 9 and len(touch(three_)) == 10 and touch(three_) - touch(two_) == {frozenset(ends)}
    and lines(two_) - lines(three_) == {frozenset(around)} and len(lines(three_) - lines(two_)) == 3,
    'with two points nine of ten couplings are films and one line is between the three round; with three points the tenth film opens between the two ends, a triangle, and that line is none')

# ---- 7 ----------------------------------------------------------------------------------------------------------
print("7 · Exhibit ONE Natural Resolver's code, executed:")
ns = {}; exec(re.search(r'```python\n(.*?)```', one, re.S).group(1), ns)
seventeen = ns['_17_next_existing']
say(sorted(set(re.findall(r'\(_13_next_discovering, (\d+)\)', one))) == ['10', '6', '9'],
    "a self has three goings out, with 6, with 10 and with 9, each to one receiving self: selves each bi-coupling with each are four and no more")
def reaches(g):
    soc = {'A': ([('s', 1)], []), 'B': ([('s', 1)], [])}
    return bool(seventeen(soc, {('A', g): 'B'})['B'][1])
say([g for g in range(1, 18) if reaches(g)] == [6, 9, 10], 'executed with each number 1 to 17 as a going: a parity reaches its receiving self with 6, with 9 and with 10 only')
def round_of(k, priors):
    selves = 'ABCDE'[:k]
    routes = {(s, g): t for s in selves for g, t in zip((10, 9, 6), [t for t in selves if t != s])}
    soc = {s: ([('s', p)], []) for s, p in zip(selves, priors)}; seen = {}; zeros = []
    for m in range(64):
        key = tuple((tuple(sorted(soc[s][0])), tuple(sorted(soc[s][1]))) for s in selves)
        if key in seen: return m - seen[key], zeros[seen[key]:]
        seen[key] = m
        zeros.append(sum(v == 0 for s in selves for _, v in ns['_1_now_existing'](*soc[s])[0]))
        soc = seventeen(soc, routes)
rounds = {k: {pr: round_of(k, pr) for pr in itertools.product((1, -1), repeat=k)} for k in (2, 3, 4)}
say(all((rd[0] == 4 and sorted(rd[1]) == [0, 0, k, k]) if len(set(pr)) == 1 else (rd[0] == 2 and rd[1] == [0, 0]) for k, v in rounds.items() for pr, rd in v.items()),
    'two, three and four selves each bi-coupling with each, one sharing: all alike, a round of four with each self sharing a 0 with each second moment; any not alike, each self inverting with each moment, a round of two')

# ---- 8 ----------------------------------------------------------------------------------------------------------
print('8 · Three cones through the point between four, each about one of the three lines:')
CONE = {0: (2, -1, -1), 1: (-1, 2, -1), 2: (-1, -1, 2)}                 # about a line: two of its own square less the other two squares
on_cone = lambda ax, v: sum(c * x * x for c, x in zip(CONE[ax], v)) == 0
say(all(on_cone(ax, v) for ax in CONE for v in cube) and all(not on_cone(ax, a) for ax in CONE for a in axes),
    "each cone has each of the cube's eight corners on it: the four lines between three bubbles and the four bubbles' middles, and no line of the three")
say(tuple(sum(c) for c in zip(*CONE.values())) == (0, 0, 0) and {F(dot(CONE[i], CONE[j]), dot(CONE[i], CONE[i])) for i, j in itertools.combinations(CONE, 2)} == {F(-1, 2)}
    and all(tuple(a + b for a, b in zip(CONE[i], CONE[j])) == tuple(-c for c in CONE[k]) for i, j, k in itertools.permutations(CONE)),
    'the three cones add to nothing, each −1/2 from each, as three films on a line; each two of them together are the third, inverted')
say(all(sub(CONE[i], CONE[j]) == tuple(3 * (int(k == i) - int(k == j)) for k in range(3)) for i, j in itertools.permutations(CONE, 2))
    and [v for v in itertools.product(range(-3, 4), repeat=3) if any(v) and on_cone(0, v) and on_cone(1, v)] == [v for v in itertools.product(range(-3, 4), repeat=3) if any(v) and abs(v[0]) == abs(v[1]) == abs(v[2])],
    'each two cones meet in the four lines through the eight corners and in no other line, and the third is through the same four')
half2 = F(dot((1, 0, 0), (1, 1, 1)) ** 2, 3)                             # the square of the cosine from a cone's line to a line on it
say(half2 == F(1, 3) and 2 * half2 - 1 == F(-1, 3) and near(math.degrees(math.acos(math.sqrt(1 / 3))), 54.7356103, 1e-6),
    "a cone's opening from its line is 54.74 degrees: twice that is 109.47 degrees, a film's opening between its two edges")
def one_way(a):
    """the corners on the one-way cone about a going: by a quarter turn each, in their order round it"""
    ax = [i for i in range(3) if a[i]][0]; o = [i for i in range(3) if i != ax]
    vs = [v for v in cube if dot(a, v) > 0]
    return sorted(vs, key=lambda v: math.atan2(v[o[1]], v[o[0]]))
say(all(set(one_way(mids[p])) == {line[opposite[p][0]], line[opposite[p][1]], Fc[p[0]], Fc[p[1]]}
        and all((one_way(mids[p])[i] in Fc) != (one_way(mids[p])[(i + 1) % 4] in Fc) for i in range(4)) for p in pairs),
    "six one-way cones, a between with each: on the one-way cone about a film's middle are the film's two edges and the middles of the two bubbles it is between, a quarter turn apart, a line and a bubble one and then the other")
say(all(dot(cross(line[opposite[p][0]], line[opposite[p][1]]), mids[p]) == 0 for p in pairs),
    "each film is flat through its one-way cone's line, from one of the cone's lines to the opposite one")
alone = {ax: mat([[-1 if i == j == ax else int(i == j) for j in range(3)] for i in range(3)]) for ax in range(3)}
say(all(A not in T24 and A in O48 and {app(A, v) for v in Fc} == set(empty) for A in alone.values())
    and all(app(alone[ax], a) == a for ax in alone for a in axes if a[ax] == 0),
    "a cone's two one-ways part at a plane across its line, with the other two lines in it; one parity inverting alone has each point of that plane with itself, and is none of the twenty-four: it has the opposite form")
say(all(app(A, (0, 0, 0)) == (0, 0, 0) for A in O48) and [v for v in itertools.product(range(-2, 3), repeat=3) if app(NEG, v) == v] == [(0, 0, 0)],
    'the point is with itself by each of the forty-eight, and it is the one point with itself by three parities inverting together: all eight corners go out from it')

# ---- 9 ----------------------------------------------------------------------------------------------------------
print("9 · Three wraps, a rim's three films:")
say(all(near(I[i](I[j](I[i](x))), I[j](I[i](I[j](x))), 1e-5) and near(I[i](I[j](I[i](x))), I[k](x), 1e-5) for i, j, k in itertools.permutations(THETA) for x in pts),
    "a film's inversion, a second's and the first's again are the second's, the first's and the second's again: each is the third film's inversion")
def wraps(t):
    """two mirrors on one line, t apart: is one, the other and the one again the same as the other, the one and the other again?"""
    refl = lambda u: ((math.cos(2 * u), math.sin(2 * u)), (math.sin(2 * u), -math.cos(2 * u)))
    s_, t_ = refl(0.0), refl(t)
    return all(abs(mm2(s_, mm2(t_, s_))[i][j] - mm2(t_, mm2(s_, t_))[i][j]) < 1e-9 for i in range(2) for j in range(2))
say(wraps(deg(60)) and wraps(deg(120)) and not any(wraps(deg(t)) for t in (30, 45, 50, 72, 90, 100)),
    "that relation, a trefoil's own, is with two mirrors 60 degrees apart, three films each 120 degrees from each, and with none of six other meetings tried")
inside = lambda x, k: norm(sub(x, S[k][0])) < S[k][1]
def direct(x):
    """which parting a point is in, by the three spheres themselves and no inversion"""
    if inside(x, 'a') and not inside(x, 'film'): return 'a'
    if inside(x, 'b') and inside(x, 'film'): return 'b'
    return 'outside'
assert all(direct(x) == parting(x) for x in within)
round_ = [direct(J((0.4 * math.cos(deg(t)), 0.4 * math.sin(deg(t)), 0.3))) for t in range(0, 360, 5)]
say([k for k, g in itertools.groupby(round_)] in (['outside', 'a', 'b', 'outside'], ['outside', 'a', 'b']),
    'one round about the rim is through the three films, one each: from all outside to a bubble, to the other bubble, and to all outside again')

# ---- 10 ---------------------------------------------------------------------------------------------------------
print("10 · A honeycomb, by a field's own form of it:")
RD3 = list(itertools.product((1, -1), repeat=3)); RD4 = [a for a in axes]            # a cell's corners of three and its corners of four
centres = [v for v in itertools.product((-2, 0, 2), repeat=3) if sorted(map(abs, v)) == [0, 2, 2]] + [(0, 0, 0)]
corners_of = lambda cn: {add(cn, v) for v in RD3 + RD4}
def edges_at(pt):
    """each line going out from a corner, by each cell with that corner: a corner of three to a corner of four"""
    out = set()
    for cn in centres:
        if pt in corners_of(cn):
            rel = sub(pt, cn)
            for w in (RD4 if rel in RD3 else RD3):
                if sum(abs(a - b) for a, b in zip(rel, w)) == 3 and all(abs(a - b) == 1 for a, b in zip(rel, w)): out.add(sub(w, rel))
    return out
apex = (1, 1, 1)
say(sum(apex in corners_of(cn) for cn in centres) == 4 and edges_at(apex) == {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)} and edges_at(apex) == set(line),
    "a cell's bottom corner, three rhombi and the facing three cells' own line: four cells and four lines, each −1/3 from each, the cube's four lines between three")
rh = [(1, -1, -1), (-1, 1, -1)]
say(F(dot(*rh), dot(rh[0], rh[0])) == F(-1, 3) and near(math.degrees(math.acos(-1 / 3)), 109 + 28 / 60, 0.01) and near(math.degrees(math.acos(1 / 3)), 70 + 32 / 60, 0.01),
    "a bottom rhombus's wide corner is 109 degrees 28 minutes and its other 70 degrees 32 minutes, a field's own measures")
walls = [(math.cos(deg(t)), math.sin(deg(t))) for t in (90, 210, 330)]
say(near(sum(w[0] for w in walls), 0.0) and near(sum(w[1] for w in walls), 0.0) and all(near(dot(a, b), -0.5) for a, b in itertools.combinations(walls, 2))
    and [360 - 60 * k for k in (3, 4, 5, 6, 7, 8)] == [180, 120, 60, 0, -60, -120],
    "three walls on each line, each 120 degrees from each; a cell of six such corners has its walls' curvings adding to nothing, and a cell of fewer or more has not")

# ---- 11 ---------------------------------------------------------------------------------------------------------
print('11 · Sizing:')
def two_bubbles(alpha, d=1.0):
    """two bubbles by a centre at this place within its parting: the inversion, the centre, and each film's curving"""
    cc = (d * math.cos(alpha), d * math.sin(alpha), 0.0)
    return inversion(cc, 1.0), cc, {k: 2 * abs(dot(n[k], cc)) for k in THETA}
def meeting(JJ, z, e=1e-6):
    g = {k: unit(sub(JJ(add(mul(u[k], e), (0, 0, z))), JJ((0.0, 0.0, z)))) for k in THETA}
    return all(near(dot(g[i], g[j]), -0.5, 1e-4) for i, j in itertools.combinations(THETA, 2))
SIZINGS = [(deg(a), d) for a in range(-57, 58, 3) for d in (0.5, 1.0, 2.5)]
assert any(a == 0 for a, d in SIZINGS)
say(all(meeting(two_bubbles(a, d)[0], z) for a, d in SIZINGS for z in (-0.8, 0.0, 0.6)),
    f"with each of {len(SIZINGS)} sizings of two bubbles, from one much the greater to the two alike to the other much the greater, the rim's three films are each 120 degrees from each: a between's meeting is of no size")
say(all(near(cv['film'], abs(cv['b'] - cv['a']), 1e-9 * max(1.0, cv['a'] + cv['b'])) for a, d in SIZINGS for cv in [two_bubbles(a, d)[2]]),
    "each bubble has one pressing, its own outside's curving, and the film between two has the one's less the other's: a film is by its two bubbles and no third")
def bulges_into_the_lesser_pressing(a, d):
    JJ, cc, cv = two_bubbles(a, d)
    if a == 0: return near(cv['film'], 0.0, 1e-12) and near(cv['a'], cv['b'], 1e-12)   # the two alike: the film flat
    more = 'b' if cv['b'] > cv['a'] else 'a'                             # the bubble with more pressing, the lesser bubble
    t = 240 if more == 'b' else 120; x = JJ((0.6 * math.cos(deg(t)), 0.6 * math.sin(deg(t)), 0.2))       # a point within it
    centre, radius = sphere_of_plane(n['film'], cc, 1.0)
    return norm(sub(x, centre)) < radius                                 # within the film's own sphere: the film curves round it
say(all(bulges_into_the_lesser_pressing(a, d) for a, d in SIZINGS),
    "a film curves round the bubble of more pressing, the lesser bubble, and into the bubble of less; with the two alike it is flat: one side or the other, or a 0 between")
outs = lambda a, d: [dot(n[k], (d * math.cos(a), d * math.sin(a), 0.0)) for k in ('a', 'b')]
say(all(outs(a, d)[0] < 0 < outs(a, d)[1] for a, d in SIZINGS),
    "each bubble's outside film curves one way with each sizing, round its own bubble and to all outside")
def three_bubbles(off):
    c_ = add(Bm[0], off); J_ = inversion(c_, 1.0); O2 = J_((0.0, 0.0, 0.0))
    cv = {p: 2 * abs(dot(N3[p], c_)) for p in pairs}                     # each film's curving
    lines_ok = all(near(dot(unit(sub(J_(mul(L[i], 1e-6)), O2)), unit(sub(J_(mul(L[j], 1e-6)), O2))), -1 / 3, 1e-4) for i, j in pairs)
    def films_ok(i, t=0.7, e=1e-6):
        x0 = mul(L[i], t); us = [unit(sub(L[j], mul(L[i], dot(L[j], L[i])))) for j in range(4) if j != i]
        g = [unit(sub(J_(add(x0, mul(uu, e))), J_(x0))) for uu in us]
        return all(near(dot(a, b), -0.5, 1e-4) for a, b in itertools.combinations(g, 2))
    diff_ok = all(near(cv[(i, j)], abs(cv[(0, i)] - cv[(0, j)]), 1e-9) for i, j in ((1, 2), (1, 3), (2, 3)))
    return lines_ok and all(films_ok(i) for i in range(4)) and diff_ok and all(cv[(0, i)] > 0 for i in (1, 2, 3))
OFFS = [(0.0, 0.0, 0.0)] + [(0.18 * a, 0.18 * b, 0.18 * c) for a, b, c in itertools.product((-1, 0, 1), repeat=3) if (a, b, c) != (0, 0, 0)]
say(all(three_bubbles(o) for o in OFFS),
    f"with each of {len(OFFS)} sizings of three bubbles: at the point four lines each −1/3 from each, round each line three films each 120 degrees from each, and each film between two with the one's pressing less the other's")
c_alike = Bm[0]
say(all(near(dot(N3[p], c_alike), 0.0) for p in inner) and len({round(2 * abs(dot(N3[p], c_alike)), 9) for p in outer}) == 1,
    'with three bubbles alike each film between two is flat, a 0 with each between, and the three outsides curve alike')
body = re.search(r'def _1_now_existing.*?(?=\ndef )', one, re.S).group(0)
order = [body.index(w) for w in ('_14_next_possibling = {}', '_12_next_co_same_existing = dict(', '_10_next_co_possibling = list(', '_11_next_co_observing = dict(')]
say(order == sorted(order), "one moment of a self in the code's own order: each parity it receives surfacing with 14, then is-or-is-not the same as its prior with 12, then its sharing with 10 and its next prior with 11")
ONE_ = ns['_1_now_existing']
def outcome(prior, recv, size=1.0):
    out, nxt = ONE_([('s', prior * size)], [('s', r * size) for r in recv])
    sg = lambda v: (v > 0) - (v < 0)
    return sg(dict(out)['s']), sg(dict(nxt)['s'])
RECV = [r for k in range(0, 4) for r in itertools.product((1, -1), repeat=k)]
kinds = {}
for prior in (1, -1):
    for r in RECV:
        kind = 'none' if not r else ('parting' if len(set(r)) == 2 else ('the same' if r[0] == prior else 'not the same'))
        kinds.setdefault(kind, set()).add((outcome(prior, r)[0] * prior, outcome(prior, r)[1] * prior))
say(kinds == {'the same': {(0, 1)}, 'not the same': {(-1, -1)}, 'parting': {(-1, -1)}, 'none': {(-1, -1)}},
    "by what a self receives for one sharing, each case to three received: all the same as its prior, it shares a 0 and its prior goes on; all agreeing and not its prior's, it shares that parity, its next prior; parting or none, its prior inverts")
say(all(outcome(prior, r, size) == outcome(prior, r) for prior in (1, -1) for r in RECV for size in (0.001, 0.37, 5.0, 1e6)),
    'the code with each parity of any size has each sharing and each next prior the same: of no size')
def shares_by_moment(k, priors, moments=8):
    selves = 'ABCD'[:k]; routes = {(s_, g): t for s_ in selves for g, t in zip((10, 9, 6), [t for t in selves if t != s_])}
    soc = {s_: ([('s', p_)], []) for s_, p_ in zip(selves, priors)}; seq = []
    for m in range(moments):
        seq.append(tuple(dict(ONE_(*soc[s_])[0]).get('s') for s_ in selves)); soc = seventeen(soc, routes)
    return seq
say(all(all((all(v == 0 for v in mo)) != (all(v == 0 for v in seq[i + 1])) and len(set(mo)) == 1 for i, mo in enumerate(seq[1:-1], 1))
        for k in (2, 3, 4) for pr in ((1,) * k, (-1,) * k) for seq in [shares_by_moment(k, pr)]),
    'selves alike, each bi-coupling with each, two, three and four: each self shares a 0 and then a parity, one and then the other, each moment after the first')

print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
