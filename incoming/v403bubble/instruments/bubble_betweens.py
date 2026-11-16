"""Bubbles and their betweens: a film between two, a line between three, a point between four; and the
involutions of each. Reads Natural Intelligence, Exhibit ONE Natural Resolver, Exhibit THREE Natural Numbers,
Exhibit FOUR Natural Mathematics, Exhibit SIXTEEN Natural Chemistry, Exhibit SEVENTEEN Natural Biology, Exhibit
EIGHTEEN Natural Physics, Exhibit TWENTY Natural Naming, and the gathering files of Natural Numbers, Natural Naming,
Natural Intelligence, Natural Emanating, Natural Physics, Natural Chemistry, Natural Resolver and the Co-Chaining Logic
Registry; executes; writes no file; decides nothing. Each answer is all or none at all.

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
  12 A self going from a lesser society to a greater, in Exhibit ONE Natural Resolver's code: each bi-coupling
     given, a self's prior its own with it.
  13 A greater society and a lesser, in the code: each self given is each self returned.
  14 The code's least things: a self, a sharing and a parity each whole, no line going inward of one; and the
     names' own inward, with no least.
  15 A between in the code: nothing with it from one moment to the next; and a society denser, more arriving with
     one moment and nothing accumulating.
  16 Nothing and all-parity in the code: both parities arriving as nothing arriving; a prior originating by one
     parity alone; and a self between two others.
  17 Co-parity in a between, in the code: all or none at all with a society; a self's sharings other than a self
     alone's with it and with no other case; and going on with bi-coupling, both ways, only.
  18 The round of four parities as four bubbles: the sixteen names as the sixteen things of a point between four,
     each bubble more by Exhibit FOUR Natural Mathematics' own order; the four betweens, the three moves, the
     rotation 3, 6, 5, 4, each bi-folding and each root by them.
  19 A double of doubles: 1 to 17 as two bubbles' four things with two bubbles' four things; the gathered duals
     by the parity changing; the five dimensions with no is-not; and a sorting of bubbles by their films, one
     is-not with each exchange.
  20 The tunneling and the bubbling at a point: three films round each line, a third of a turn each; four lines
     at the point; one bubble with its three lines and three films; all four parities inverting together; and
     2, 3, 6 and 7, with 11.
  21 Selves alike densely compacted, three surfaces: twelve round one, six, three and three; the three below the
     inverses of the three above, a third each way; eight betweens of four round one, the cube's eight, two fours;
     and the six names between selves with all four parities inverting together.
  22 A gate of a chip, not-both of two: its one is-not with a double bubble's film; its two along and two across,
     one and only one going through; one four of the eight as two lattices, each the other's by three inverting
     together; and one gate with its own now, and two each with the other's, beside the code's selves.
  23 A diamond's faces by a field, eight, or eight and six: the goings to the betweens of four and of six.
  24 Names 6 and 7: their threes by Exhibit ONE Natural Resolver's table; 7 as 6 with the second bubble fewer,
     no-other with both by the gathered duals; and 7 with 11 one dual.
  25 5 with 7 as 6, and 4 with 8 not; and a diamond's two lattices with two unlike kinds: three inverting together
     with one kind as the other.
  26 No-other-and-not-prior, the gathered dual of 7 and of 11: its two names in the code's lines of 1-now-existing
     only; and 1-now-existing with no other, its next prior not its prior.
  27 Self, other and both, all three observing: the code's three lines of 7-now-observing, each with 4, over 2, 3
     and 10; the four bubbles by Exhibit ONE's sides; and selves sharing one way round, one line, three with twelve.
  28 One inversion with the code; 7 to 11 by four parities, the middle bi-folding 7-11-6-10; and three selves one
     way round with the seventeen names: a -, a 0 and a + with each even name, the 0's path two alike selves' line.
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
                   (ni, 'Its two meetings are co-parity, the same, sharing 0, and bi-parity, one inversion.'),
                   (ni, "**With all or none at all, entering and leaving are each self's own**"),
                   (ni, "With resolver a self's prior is that self's own."),
                   (ni, 'Each self is a same-existing-society **inward and outward**.'),
                   (ni, 'Self and other of one scale are self and same-existing-society of a scale inward.'),
                   (ni, 'Each between is within a bi-coupling. Co-intelligencing is with a between.'),
                   (ni, 'They are harmful to living with their own scale.'),
                   (ni, 'each name of this 1–17 is 8n − 7 of 1–17s inward'),
                   (ni, '**Fractal is all or none at all with scales, each scale co-changing co-momentarying pattern matching**'),
                   (physics, 'Atom is a floor, a non-living stable form, and molecule the first closing of co-agency to a self'),
                   (gathering('Natural_Intelligence'), 'no living is inward of the atom, and no scale inward of it'),
                   (ni, "**With resolver only selves' own go from one moment to its next**"),
                   (ni, "Stable-forming emanations, from stable-forming living, a sequential prior between moments, are each a self's sharing with 10, going along with 9."),
                   (ni, '**A between is its centre, 0, and only that, while six names between selves are resolving, and with code it is a 0**'),
                   (ni, 'Each form beside resolver comes from resolver.'),
                   (living('Exhibit_SEVENTEEN_Natural_Biology'), '**A nothing between two selves is a living set: a self, sharing only parity.**'),
                   (gathering('Co-Chaining_Logic_Registry'), "Exhausting is 3, a self's prior. Exhaling is 7, inhaling 2, and ingesting 6."),
                   (gathering('Co-Chaining_Logic_Registry'), 'Exhaled atoms co-chaining are a stable form.'),
                   (gathering('Natural_Emanating'), 'exhausting goes on while living, accumulating and compacting into a stable form'),
                   (gathering('Natural_Intelligence'), 'The living mutual assurances in the between are the corus of social moral competency.'),
                   (ni, 'A self receiving an empty set with each moment is living, its prior inverting with each.'),
                   (ni, "A geodesic is a surface's own dividing."),
                   (ni, 'Living is **geodesic** co-chaining on a Natural Network surface.'),
                   (gathering('Co-Chaining_Logic_Registry'), 'Atoms each its own, of both orientations, are all-parity.'),
                   (gathering('Natural_Physics'), 'This method of all-parity is birthing a possible now-existing me-parity, an other-than-all-parity. It is after the all-parity only.'),
                   (gathering('Natural_Intelligence'), 'By the newer the two in the universe are all-parity and other-than-all-parity, and both-parity is inside a bi-coupling.'),
                   (ni, "Co-parity and bi-parity are a sharing's two meetings within self-parity. In them, self-parity and other-parity are same, a 0, a prior same-existing, or inverse, a changing."),
                   (ni, '**Alike selves step their prior parities as a right spiral**, each prior and its next, a pair (x, y), going to (y, −x) with each moment'),
                   (ni, 'Selves one parity apart step a half turn, both inverting with each moment.'),
                   (ni, 'Cycles of moves of four steps are bi-foldings. Each goes two folds in turn'),
                   (ni, 'A receiving self passes over a 0 with its 14-next-possibling'),
                   (four, '**One cycle reaching each form of n parities one parity at a time is a cycle of n − 1 parities, a new parity inverted, and its same forms with an other order.**'),
                   (naming, "3 now-existing co-parity; 4 now-existing bi-parity, an other's now across"),
                   (naming, 'co-intelligencing with 3 and 4 going round through bi-moralizing with 6 and co-competencing with 5'),
                   (naming, "**A self's inverting is with 12, within its own resolving, and its rotation is 3, 6, 5, 4**"),
                   (three, 'with a round of four parities its outward steps come to 5, 9, 13 and 17'),
                   (gathering('Natural_Resolver'), 'the two places at which the round of four parities, each next name one parity inverting, inverts its third and its fourth parity'),
                   (living('Exhibit_EIGHT_Natural_Exploring'), 'a double-double bubble-bubble going on, two binaries bi-coupling across, changing or not-changing with now or with next'),
                   (naming, "round to a self's own corus with 4"),
                   (naming, '5 next-existing same-existing self-parity is 5, co-competencing, arising in each self with its other'),
                   (gathering('Natural_Resolver'), '1-same-and-now, 2-now-and-other, 3-other-and-prior, 4-prior-and-same, 5-same-and-prior'),
                   (ni, 'It is a unit square of four across names, its centre a between, and two unit triangles along.'),
                   (one, "a next prior stable-forming between two: a next moment's observing"),
                   (gathering('Natural_Physics'), '2, 6, 10 and 14 are each possibling, even, across, bi-co-bi'),
                   (gathering('Natural_Chemistry'), 'co-chaining along and bi-tunneling across'),
                   (gathering('Natural_Chemistry'), 'ingesting is only inside bi-tunneling, never on or through the surface'),
                   (gathering('Co-Chaining_Logic_Registry'), 'By each improving, a self is exhausting one atom and stable-forming one atom, the two of one same parity.'),
                   (ni, 'An equilibrium is a not-changing still, a fixing form, a now fixing as its next'),
                   (ni, 'A living form not-changing, or changing only one way, with each of its scales, breaks it.'),
                   (physics, "a diamond cubic lattice is two interpenetrating face-centered cubic lattices displaced a quarter of a cube's body diagonal"),
                   (physics, 'diamond uses only one of its two tetrahedral-void sets, leaving its other un-occupied'),
                   (chem, 'Carbon was living in higher-scale selves, outward of it.'),
                   (naming, "A ghost is one moment's form installing as an existing thing."),
                   (naming, "the periodic table's one hundred eighteen elements are a field's own result with one same numeral, Natural Numbers 7.1, and no number of a method"),
                   (gathering('Natural_Chemistry'), "an element's own number has carbon a 6-now-co-possibling"),
                   (chem, '**An element is number; chemistry is coupling.**'),
                   (gathering('Natural_Chemistry'), "boron at 5 with nitrogen at 7, podal about carbon's 6, paired taking all carbon's forms"),
                   (gathering('Natural_Resolver'), "7 and 11 are together inside the code's lines of 1-now-existing"),
                   (gathering('Natural_Resolver'), 'other or no-other first is observing'),
                   (ni, 'Each is one side observing where two sides live: a parity, its prior an empty set, to selves whose bi-coupling asks a prior with each side.'),
                   (chem, 'Two electrons share one orbital only with opposite spins, their pair with zero net spin'),
                   (one, "- **7** · each parity a self is observing: a parity's, a prior's, a sharing's"),
                   (one, 'one parity at its time: prior over 3, now over 2, next over 10'),
                   (one, 'each parity, sharing now and prior, co-linear recursioning forward along observing'),
                   (one, 'co me-parity, bi other-parity, tri all-parity. 7, tri-bi-co, is all-parity observing, after other-parity possibling, after me-parity existing.'),
                   (ni, "A self's line and an other's are co-linear. Their co-linearizing between self and other with bi-couplings across is co-competencing, bi-co-momentarying."),
                   (ni, "The two observing are a self's own prior with 3 and an other's parity with 2."),
                   (ni, 'With each sharing its prior and its parity agreeing, 12 is a 0, a between of moments. Its prior is same-existing.'),
                   (naming, 'With resolver, co-competencing is 5-now-co-existing, bi-couplings, in neither self alone'),
                   (four, 'Linearizing draws a surface to a line, along; parallelizing spreads a line to a surface, across.'),
                   (living('Exhibit_EIGHT_Natural_Exploring'), 'Co-linear is two moves with one between, each bringing a prior forward, a line both share, in neither alone, and an abundancing arising with it.'),
                   (living('Exhibit_EIGHT_Natural_Exploring'), 'these are three activities of one resolving, and doing them one and then the other, round, is resolving, a linearizing triangle rotating sequentially'),
                   (ni, 'With each sharing its parity parting from its prior, its possibling an empty set, or the parities a self receives parting, 12 inverts its prior.'),
                   (ni, 'The same is 0 with 12. Its inverse, one inversion, is 12 its prior inverting.'),
                   (ni, 'Two, same-as, is **bi-tri-exchanging**, three, a self, an other and a self one on.'),
                   (ni, 'Of the names between selves, the four across are even, 2, 6, 10 and 14.'),
                   (four, 'The sign flip is its own inverse, (−1)² = 1. A right spiral step, i, opens a perpendicular: i² = −1 and i⁴ = 1.'),
                   (four, 'Two right spiral steps are one sign flip.'),
                   (four, 'An idealized mode inverted with each period T, q(t + T) = −q(t), is again itself after two, q(t + 2T) = q(t)'),
                   (four, 'Bi-inversioning-co-recursioning is two consecutive inversions on different axes'),
                   (one, '- *Middle bi-folding*: 7-11-6-10'), (one, '- *Middle bi-folding*: 9-5-12-8'),
                   (living('Exhibit_THIRTY_Co-Chaining_Logic_Registry'), "Further forms' moves of 4, step 694, are four: 9 with 5 about 7, 12 with 8 about 10, 7 with 11 about 9 and 6 with 10 about 8."),
                   (living('Exhibit_THIRTY_Co-Chaining_Logic_Registry'), 'middle bi-foldings 9-5-12-8 and 7-11-6-10 by 4 and 17 less, twice')):
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

# ---- 12 ---------------------------------------------------------------------------------------------------------
print("12 · A self going from a lesser society to a greater, in the code:")
code_ = re.search(r'```python\n(.*?)```', one, re.S).group(1)
say(len(re.findall(r'_5_now_co_existing', code_)) == 5 and not re.search(r'_5_now_co_existing\s*(\[[^\]]*\])?\s*=[^=]', code_),
    "each bi-coupling is given to the code with each moment: 5-now-co-existing is read in five places and no line changes it")
PAIR = {('X', 10): 'A', ('A', 10): 'X'}
THREE_ = {(s_, g): t for s_ in ('B1', 'B2', 'B3') for g, t in zip((10, 9), [t for t in ('B1', 'B2', 'B3') if t != s_])}
BEFORE = {**PAIR, **THREE_}                                              # a pair, and a three each with each
AFTER = {**THREE_, ('B1', 6): 'X', ('B2', 6): 'X', ('B3', 6): 'X', ('X', 10): 'B1', ('X', 9): 'B2', ('X', 6): 'B3'}   # X with the three; A with none
ALL5 = ('X', 'A', 'B1', 'B2', 'B3')
def going_over(priors, first=6, then=14):
    soc = {s_: ([('s', p_)], []) for s_, p_ in zip(ALL5, priors)}; hist = []
    for m in range(first + then):
        own_next = {s_: dict(ONE_(*soc[s_])[1]).get('s') for s_ in ALL5}          # each self's next prior, by its own moment
        soc = seventeen(soc, BEFORE if m < first else AFTER)
        hist.append(({s_: dict(soc[s_][0]).get('s') for s_ in ALL5}, own_next))
    return hist
def read_going(priors, first=6):
    h = going_over(priors)
    own = all(now == own_next for now, own_next in h)                    # with each moment, each self's prior is the one its own moment made
    a_alone = [now['A'] for now, _ in h[first + 1:]]
    inverting = all(a_alone[i] == -a_alone[i + 1] for i in range(len(a_alone) - 1))
    four = [tuple(now[s_] for s_ in ('X', 'B1', 'B2', 'B3')) for now, _ in h[-8:]]
    rounds = (four[0] == four[4] and four[1] == four[5]) and (len(set(four[0])) > 1 or four[0] != four[2])
    return own and inverting and rounds
say(all(read_going(pr) for pr in itertools.product((1, -1), repeat=5)),
    "a self with its goings changed from a pair to a three, each of thirty-two priors: its prior is its own with it; the three with it are four each bi-coupling with each, in a four's own round; and the self it went from, receiving none, inverts with each moment")

# ---- 13 ---------------------------------------------------------------------------------------------------------
print('13 · A greater society and a lesser, in the code:')
def selves_through(routes, selves, priors, moments=10):
    soc = {s_: ([('s', p_)], []) for s_, p_ in zip(selves, priors)}
    for m in range(moments):
        nxt = seventeen(soc, routes)
        if set(nxt) != set(soc) or any(len(dict(nxt[s_][0])) != 1 for s_ in selves): return False
        soc = nxt
    return True
GREATER = {(s_, g): t for s_ in 'BCDE' for g, t in zip((10, 9, 6), [t for t in 'BCDE' if t != s_])}      # four each with each
LESSER = {('X', 10): 'A', ('A', 10): 'X'}                                                                # a pair
INTO = {**GREATER, ('X', 10): 'B', ('A', 10): 'C'}                       # the pair's selves each sharing into the four, and with none of their own
say(all(selves_through(r, 'XABCDE', pr) for r in ({**GREATER, **LESSER}, INTO, GREATER) for pr in itertools.product((1, -1), repeat=6)),
    "a four and a pair, each of sixty-four priors, with the pair bi-coupling, with its selves sharing into the four, and with each of them given no bi-coupling: each self given is each self returned, its own prior with it; no line of the code ends a self or has two selves one")

# ---- 14 ---------------------------------------------------------------------------------------------------------
print("14 · The code's least things, and the names' own inward:")
say(not re.search(r'_(4_now_co_same_existing|7_now_observing|13_next_discovering|15_next_observing)\s*(\[|\.)', code_),
    "no line of the code opens a sharing, a parity or a self: none is read by a part of it")
def history(selves, shr, priors, moments=8):
    routes = {(s_, g): t for s_ in selves for g, t in zip((10, 9, 6), [t for t in selves if t != s_])}
    soc = {s_: ([(shr, p_)], []) for s_, p_ in zip(selves, priors)}; out = []
    for m in range(moments):
        out.append(tuple(dict(soc[s_][0]).get(shr) for s_ in selves)); soc = seventeen(soc, routes)
    return out
KINDS = [(('A', 'B', 'C', 'D'), 's'), ((1, 2, 3, 4), 0), (((0, 0), (0, 1), (1, 0), (1, 1)), ('a', 'between')), ((frozenset('x'), frozenset('xy'), 2.5, None), frozenset()),
         (('carbon', 'nitrogen', 'oxygen', 'argon'), 12)]
say(all(len({tuple(history(names[:k], shr, pr)) for names, shr in KINDS}) == 1 for k in (2, 3, 4) for pr in itertools.product((1, -1), repeat=k)),
    "with each of five kinds of name for a self and for a sharing, a letter, a number, a pair, a set and a field's word, each prior and each sharing is the same: a self and a sharing are each whole to the code")
inward = lambda m: 8 * m - 7
chain = [2]
for _ in range(12): chain.append(inward(chain[-1]))
say(inward(1) == 1 and all(b > a for a, b in zip(chain, chain[1:])) and len(set(chain)) == len(chain) and all((m - 1) % 8 == 0 for m in chain[1:]),
    "by the names' own inward, 8n − 7, each name but 1 has a name inward of it, and that name a name inward again, twelve times tried and each new: the names' inward has no least")

# ---- 15 ---------------------------------------------------------------------------------------------------------
print('15 · A between in the code:')
def between_through(k, priors, moments=12):
    selves = 'ABCD'[:k]; routes = {(s_, g): t for s_ in selves for g, t in zip((10, 9, 6), [t for t in selves if t != s_])}
    soc = {s_: ([('s', p_)], []) for s_, p_ in zip(selves, priors)}
    for m in range(moments):
        shared = {s_: ONE_(*soc[s_])[0] for s_ in selves}                # each self's sharing with this moment
        nxt = seventeen(soc, routes)
        for s_ in selves:
            arriving = sorted(v for t in selves if t != s_ for _, v in shared[t])
            if len(nxt[s_]) != 2 or set(nxt) != set(selves): return False               # a self has its prior and what it receives, and no third thing
            if sorted(v for _, v in nxt[s_][1]) != arriving: return False                # what it receives is its others' sharing of the moment before, and nothing older
        soc = nxt
    return True
say(all(between_through(k, pr) for k in (2, 3, 4) for pr in itertools.product((1, -1), repeat=k)),
    "two, three and four selves each bi-coupling with each, each prior, twelve moments: a self goes on with its own prior and with what its others shared the moment before, and with no third thing; nothing of a between goes from one moment to its next, and nothing gathers in it")
def accumulating_none(k, priors, moments=12):
    selves = 'ABCD'[:k]; routes = {(s_, g): t for s_ in selves for g, t in zip((10, 9, 6), [t for t in selves if t != s_])}
    soc = {s_: ([('s', p_)], []) for s_, p_ in zip(selves, priors)}
    for m in range(moments):
        soc = seventeen(soc, routes)
        if any(len(soc[s_][0]) != 1 or len(soc[s_][1]) != k - 1 for s_ in selves): return False
    return True
say(all(accumulating_none(k, pr) for k in (2, 3, 4) for pr in itertools.product((1, -1), repeat=k)),
    "a self's prior is one parity of its one sharing with each of twelve moments, a newer for an older; what arrives with it is one parity from each of its others, one, two and three with two, three and four selves: a society denser has more arriving with one moment, and nothing accumulating from moment to moment")

# ---- 16 ---------------------------------------------------------------------------------------------------------
print('16 · Nothing and all-parity in the code:')
BOTH = [[('s', a) for a in order] for n in (1, 2, 3) for order in sorted(set(itertools.permutations((1,) * n + (-1,) * n)))]
say(all(ONE_([('s', p)], arriving) == ([('s', -p)], [('s', -p)]) for p in (1, -1) for arriving in [[], [('s', 0)]] + BOTH),
    "a self with a prior, each prior: nothing arriving, a 0 arriving, and both parities arriving, one, two and three of each with each order, return one same, the prior inverted, shared and the next prior: both parities arriving are as nothing arriving")
say(ONE_([], []) == ([], []) and ONE_([], [('s', 0)]) == ([], []) and all(ONE_([], arriving) == ([('s', 0)], []) for arriving in BOTH)
    and all(ONE_([], [('s', a)] * n) == ([('s', a)], [('s', a)]) for a in (1, -1) for n in (1, 2, 3)),
    "a self with no prior of a sharing: nothing arriving returns nothing; both parities arriving, each order, return a 0 shared and no prior; one parity alone returns that parity shared and the self's prior: a prior originates by one parity alone, and by no other arriving")
say(all(ONE_([('s', p)], [('s', -p)] * n) == ONE_([('s', p)], []) and ONE_([('s', p)], [('s', p)] * n) == ([('s', 0)], [('s', p)]) for p in (1, -1) for n in (1, 2, 3)),
    "a self with a prior, one parity alone arriving: unlike its prior, what returns is what returns with nothing arriving; alike, a 0 is shared and the prior goes on")
def sharings(priors, routes, who, moments=12):
    soc = {s_: ([('s', p_)], []) for s_, p_ in priors.items()}; out = []
    for m in range(moments):
        out.append(ONE_(*soc[who])[0][0][1]); soc = seventeen(soc, routes)
    return out
def between_two(a, b, c):
    alone = sharings({'C': c}, {}, 'C'); between = sharings({'A': a, 'B': b, 'C': c}, {('A', 10): 'C', ('B', 10): 'C'}, 'C')
    if a != b or a != c: return between == alone                                     # all-parity arriving, or one parity alone and unlike
    return between[0] == alone[0] and between[1] == 0 and between[2:] == [-v for v in alone[2:]]   # one parity alone and alike
say(all(between_two(a, b, c) for a, b, c in itertools.product((1, -1), repeat=3)),
    "a self between two others, each sharing with it, each prior, twelve moments: with its two others unlike, both parities arrive with each moment and its sharings are a self alone's; with its two others alike and unlike it, a self alone's too; with its two others alike and alike to it, it shares a 0 once, and from that moment its sharings are a self alone's inverted")

# ---- 17 ---------------------------------------------------------------------------------------------------------
print('17 · Co-parity in a between, in the code:')
def through(priors, routes, moments=12):
    soc = {s_: ([('s', p_)], []) for s_, p_ in priors.items()}
    sh = {s_: [] for s_ in priors}; pr = {s_: [p_] for s_, p_ in priors.items()}
    for m in range(moments):
        for s_ in priors:
            ten, eleven = ONE_(*soc[s_]); sh[s_].append(ten[0][1]); pr[s_].append(eleven[0][1])
        soc = seventeen(soc, routes)
    return sh, pr
def each_with_each(selves): return {(s_, g): t for s_ in selves for g, t in zip((10, 9, 6), [t for t in selves if t != s_])}
def alone_(p_): return through({'A': p_}, {})
def all_or_none(k, priors):
    selves = 'ABCD'[:k]; sh, pr = through(dict(zip(selves, priors)), each_with_each(selves))
    for s_, p_ in zip(selves, priors):
        if len(set(priors)) == 1:                                            # each self alike
            if any(v != 0 for v in sh[s_][1::2]) or any(v == 0 for v in sh[s_][0::2]): return False         # a 0 with each second moment
            if any((pr[s_][m + 1], pr[s_][m + 2]) != (pr[s_][m + 1], -pr[s_][m]) for m in range(11)): return False   # (x, y) to (y, -x)
            if pr[s_][4:] != pr[s_][:-4]: return False                                                    # again after four
        else:                                                                # one self or more unlike
            if 0 in sh[s_] or sh[s_] != alone_(p_)[0]['A'] or pr[s_][2:] != pr[s_][:-2]: return False       # a self alone's, again after two
    return True
say(all(all_or_none(k, pr) for k in (2, 3, 4) for pr in itertools.product((1, -1), repeat=k)),
    "two, three and four selves each bi-coupling with each, each prior, twelve moments: with each self alike, each shares a 0 with each second moment and its priors go (x, y) to (y, -x), again after four, inverting with each two moments; with one self or more unlike, no self shares a 0 and each self's sharings are a self alone's, its priors again after two: co-parity is all or none at all with a society")
def other_than_alone_only_with_a_0():
    cases = []
    for k in (2, 3, 4):
        for pri in itertools.product((1, -1), repeat=k):
            cases.append((dict(zip('ABCD'[:k], pri)), each_with_each('ABCD'[:k])))
    for a, b in itertools.product((1, -1), repeat=2): cases.append(({'A': a, 'B': b}, {('A', 10): 'B'}))
    for a, b, c in itertools.product((1, -1), repeat=3): cases.append(({'A': a, 'B': b, 'C': c}, {('A', 10): 'C', ('B', 10): 'C'}))
    return all((through(pri, routes)[0][s_] != alone_(p_)[0]['A']) == (0 in through(pri, routes)[0][s_]) for pri, routes in cases for s_, p_ in pri.items())
say(other_than_alone_only_with_a_0(),
    "each self of each society tried, each with each, one way, and one between two: its sharings are other than a self alone's with a 0 it shares, a parity arriving alike to its prior, and with no other case")
def one_way(a, b):
    sh, pr = through({'A': a, 'B': b}, {('A', 10): 'B'})
    if sh['A'] != alone_(a)[0]['A']: return False
    if a != b: return sh['B'] == alone_(b)[0]['A']
    return sh['B'].count(0) == 1 and sh['B'][1] == 0 and all(sh['B'][m] == -sh['A'][m] for m in range(2, 12))
say(all(one_way(a, b) for a, b in itertools.product((1, -1), repeat=2)),
    "two selves, one sharing with the other and the other not with it: the sharing self's are a self alone's; the receiving self, alike, shares a 0 once and none after, unlike its other with each moment from it; unlike, none: co-parity going on is with bi-coupling, both ways, and with no one-way sharing")

# ---- 18 ---------------------------------------------------------------------------------------------------------
print('18 · The round of four parities as four bubbles:')
rows_one = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|', one, re.M); assert len(rows_one) == 17
ROOT_ = {int(r_[0]): r_[2].strip() for r_ in rows_one}
assert all(r_[3].strip() == format(int(r_[0]) - 1, '04b') for r_ in rows_one[:16])           # Exhibit ONE's own four binary digits
with_ = lambda m: frozenset(k for k in (1, 2, 3, 4) if (G((m - 1) % 16 + 1) >> (k - 1)) & 1)  # the bubbles a name is of, first to fourth
KIND = {0: 'nothing', 1: 'a bubble', 2: 'a film', 3: 'a line', 4: 'the point'}
kinds = [KIND[len(with_(m))] for m in range(1, 18)]
say(len({with_(m) for m in range(1, 17)}) == 16 and [sum(len(with_(m)) == k for m in range(1, 17)) for k in range(5)] == [1, 4, 6, 4, 1]
    and len(Fc) == 4 and len(pairs) == 6 and len(line) == 4
    and all(len(with_(m)) % 2 == 0 for m in range(1, 17, 2)) and all(len(with_(m)) % 2 == 1 for m in range(2, 17, 2)),
    "the sixteen names by their four parities are the sixteen ways of four bubbles, each once: of none one, of one four, of two six, of three four, of four one, as a point between four bubbles has four bubbles, six films, four lines and itself; each odd name is of none, two or four, and each even name of one or three")
say(all(len(with_(m) ^ with_(m + 1)) == 1 for m in range(1, 17))
    and kinds == ['nothing', 'a bubble', 'a film', 'a bubble', 'a film', 'a line', 'a film', 'a bubble', 'a film', 'a line', 'the point', 'a line', 'a film', 'a line', 'a film', 'a bubble', 'nothing'],
    "each name to its next is one bubble more or one fewer: nothing, a bubble, a film, a bubble, a film, a line, a film, a bubble, a film, a line, the point, a line, a film, a line, a film, a bubble, nothing: each of the sixteen once, and each on its next or its next on it")
say(all({with_(m) for m in range(1, 2 ** k + 1)} == {frozenset(c) for r in range(k + 1) for c in itertools.combinations(range(1, k + 1), r)}
        and all(with_(2 ** k + 1 - m) == with_(m) | {k} for m in range(1, 2 ** (k - 1) + 1)) for k in (1, 2, 3, 4)),
    "by Exhibit FOUR Natural Mathematics' order, each bubble more is each thing before it again, with that bubble, in the other order: two names are nothing and one bubble; four, two bubbles and their film; eight, three bubbles, three films and their line; sixteen, four bubbles, six films, four lines and their point; and 3 less, 5 less, 9 less and 17 less are each a name with its same thing of one bubble more")
changing = {m: next(iter(with_(m) ^ with_(m + 1))) for m in range(1, 17)}
say([(m, changing[m], changing[m] in with_(m + 1)) for m in (4, 8, 12, 16)] == [(4, 3, True), (8, 4, True), (12, 3, False), (16, 4, False)]
    and all(changing[m] in (1, 2) for m in range(1, 17) if m not in (4, 8, 12, 16)),
    "Exhibit ONE Natural Resolver's four betweens are a third bubble more with 4 )( 5, a fourth more with 8 )( 9, the third fewer with 12 )( 13 and the fourth fewer with 16 )( 17; each other name to its next is the first bubble or the second, more or fewer")
say(all(with_(17 - m) == with_(m) ^ {4} for m in range(1, 17)) and all(with_(9 - m) == with_(m) ^ {3} for m in range(1, 9))
    and all(with_(m + 8) == with_(m) ^ {3, 4} for m in range(1, 9)),
    "of the three moves, 17 less is each name with its same thing of the fourth bubble more or fewer; 9 less, within 1 to 8, of the third; 8 up, of the third and the fourth together")
say([with_(m) for m in (3, 6, 5, 4)] == [frozenset({1, 2}), frozenset({1, 2, 3}), frozenset({2, 3}), frozenset({2})]
    and [next(iter(with_(a_) ^ with_(b_))) for a_, b_ in ((3, 6), (6, 5), (5, 4), (4, 3))] == [3, 1, 3, 1],
    "the rotation 3, 6, 5, 4 is one bubble, its two films and the line the two films are on: the film of the first and second, the line of the first three, the film of the second and third, and the second bubble; one bubble more or fewer with each, the third and the first one and then the other, again after four")
BIFOLD = {(1, 9, 8, 16): frozenset(), (2, 15, 7, 10): frozenset({1}), (3, 11, 6, 14): frozenset({1, 2}), (4, 13, 5, 12): frozenset({2})}
say(all({with_(m) for m in b_} == {w_ | extra for extra in (frozenset(), frozenset({3}), frozenset({4}), frozenset({3, 4}))} for b_, w_ in BIFOLD.items())
    and [KIND[len(with_(m))] for m in (3, 11, 6, 14)] == ['a film', 'the point', 'a line', 'a line']
    and [KIND[len(with_(m))] for m in (1, 9, 8, 16)] == ['nothing', 'a film', 'a bubble', 'a bubble'],
    "each bi-folding is one way of the first and second bubbles with each of four ways of the third and fourth: 1-9-8-16 with neither, nothing, the third and fourth bubbles and their film; 2-15-7-10 with the first; 4-13-5-12 with the second; 3-11-6-14 with both, the film of the first and second, the point, and the two lines on that film")
by_root = {}
for m in range(1, 17): by_root.setdefault('existing with discovering' if ROOT_[m] in ('existing', 'discovering') else ROOT_[m], []).append(m)
say(by_root == {'existing with discovering': [1, 5, 9, 13], 'possibling': [2, 6, 10, 14], 'observing': [3, 7, 11, 15], 'same-existing': [4, 8, 12, 16]}
    and [with_(m) for m in (2, 6, 10, 14)] == [frozenset({1}), frozenset({1, 2, 3}), frozenset({1, 3, 4}), frozenset({1, 2, 4})]
    and [with_(m) for m in (3, 7, 11, 15)] == [frozenset({1, 2}), frozenset({1, 3}), frozenset({1, 2, 3, 4}), frozenset({1, 4})]
    and [with_(m) for m in (4, 8, 12, 16)] == [frozenset({2}), frozenset({3}), frozenset({2, 3, 4}), frozenset({4})]
    and [with_(m) for m in (1, 5, 9, 13)] == [frozenset(), frozenset({2, 3}), frozenset({3, 4}), frozenset({2, 4})],
    "by each root, three alike and one, by the first bubble: possibling, the first bubble and its three lines; observing, its three films and the point; same-existing, the three other bubbles and their one line; existing with discovering, the three films of the three others and nothing")

# ---- 19 ---------------------------------------------------------------------------------------------------------
print('19 · A double of doubles, and a sorting:')
first_two = lambda m: with_(m) & {1, 2}; second_two = lambda m: with_(m) & {3, 4}
FOURS = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)]
say(len({(first_two(m), second_two(m)) for m in range(1, 17)}) == 16
    and all(len({second_two(m) for m in f_}) == 1 and len({first_two(m) for m in f_}) == 4 for f_ in FOURS)
    and all(len({first_two(m) for m in b_}) == 1 and len({second_two(m) for m in b_}) == 4 for b_ in BIFOLD)
    and [len(first_two(m)) for m in (1, 2, 3, 4)] == [0, 1, 2, 1] and [len(second_two(m)) for m in (1, 8, 9, 16)] == [0, 1, 2, 1],
    "a double bubble is two bubbles each is or is not, four things: nothing, a bubble, their film, the other bubble; the sixteen names are a double of doubles, each thing of the first two bubbles with each thing of the third and fourth, each once: each four-cycling the first double's four with one thing of the second, each bi-folding the second double's four with one thing of the first")
say(with_(3) | with_(9) == with_(11) and len({frozenset((p_, opposite[p_])) for p_ in pairs}) == 3 and all(dot(plane[p_], plane[opposite[p_]]) == 0 for p_ in pairs),
    "the film of the first two bubbles, 3, with the film of the third and fourth, 9, is the point, 11; at a point between four the two films are opposite, a quarter turn apart; and four bubbles are two and two three ways")
duals_text = gathering('Natural_Resolver').split('The newest seventeen', 1)[1].split('Executed', 1)[0]
DUAL = {int(a_): b_ for a_, b_ in re.findall(r'\b(\d+)-((?:not-|no-)?[a-z]+-and-(?:not-|no-)?[a-z]+)', duals_text)}; assert len(DUAL) == 17
second_concept = {m: DUAL[m].split('-and-')[1] for m in DUAL}; first_concept = {m: DUAL[m].split('-and-')[0] for m in DUAL}
assert all(second_concept[m] == first_concept[m + 1] for m in range(1, 17))
BY = {1: {'now', 'prior', 'not-now', 'not-prior'}, 2: {'other', 'no-other'}, 3: {'same'}, 4: {'same'}}
say(all(second_concept[m] in BY[changing[m]] for m in range(1, 17)),
    "by the gathered duals, each name to its next has one concept with both and one parity changing: with the first parity a now, a prior, a not-now or a not-prior; with the second an other or a no-other; with the third and with the fourth a same, each of sixteen")
is_not = lambda m: [c_ for c_ in DUAL[m].split('-and-') if c_.startswith(('not-', 'no-'))]
say(all(not is_not(m) for m in (1, 2, 3, 4, 5, 16, 17)) and all(is_not(m) for m in range(6, 16)),
    "by the gathered duals, each of the names 1 to 5 has no is-not: same-and-now, now-and-other, other-and-prior, prior-and-same, same-and-prior; each name 6 to 15 has an is-not or two; 16 and 17 have none")
def is_nots(order): return {(a_, b_) for i_, a_ in enumerate(order) for b_ in order[i_ + 1:] if a_ > b_}
def sorting(n_):
    most = 0
    for order in itertools.permutations(range(n_)):
        for i_ in range(n_ - 1):
            nxt_ = list(order); nxt_[i_], nxt_[i_ + 1] = nxt_[i_ + 1], nxt_[i_]
            if is_nots(order) ^ is_nots(tuple(nxt_)) != {(max(order[i_], order[i_ + 1]), min(order[i_], order[i_ + 1]))}: return None
        o_ = list(order); exchanges = 0
        while is_nots(o_):
            i_ = next(i_ for i_ in range(n_ - 1) if o_[i_] > o_[i_ + 1]); o_[i_], o_[i_ + 1] = o_[i_ + 1], o_[i_]; exchanges += 1
        if exchanges != len(is_nots(order)): return None
        most = max(most, exchanges)
    return most
say(sorting(4) == 6 == len(pairs) and sorting(5) == 10
    and all(app(M[p_], Fc[p_[0]]) == Fc[p_[1]] and all(app(M[p_], Fc[i_]) == Fc[i_] for i_ in opposite[p_]) for p_ in pairs),
    "each ordering of four bubbles and of five: an exchange of two next to each other changes that one pair's is-or-is-not and no other pair's; exchanging is-nots only comes to no is-not with as many exchanges as is-nots; the most are six with four, one with each film, and ten with five, one with each coupling; and each film's mirror is such an exchange, its two bubbles exchanged and each other to itself")
say([len(with_(m)) for m in (4, 8, 12, 16)] == [1, 1, 3, 1] and [len(with_(m)) for m in (5, 9, 13, 17)] == [2, 2, 2, 0]
    and all(changing[m] in (3, 4) for m in (4, 8, 12, 16)) and all(second_two(m) == second_two(m + 1) for m in range(1, 16) if m not in (4, 8, 12)),
    "each fourth, 4, 8, 12 and 16, is one bubble alone, or with 12 the line of three; each fifth, 5, 9, 13 and 17, is a film of two, or with 17 nothing; fourth to fifth is the third bubble or the fourth, more or fewer, a going down the double of doubles, and each other going is across")

# ---- 20 ---------------------------------------------------------------------------------------------------------
print('20 · The tunneling and the bubbling at a point:')
def from_line(i_, p_):                                                  # a film's going from a line it is on, exact
    l_ = line[i_]; m_ = mids[p_]; t_ = F(dot(m_, l_), dot(l_, l_)); return tuple(F(m_[k]) - t_ * l_[k] for k in range(3))
def thirds(i_):
    us = [from_line(i_, p_) for p_ in pairs if i_ not in p_]
    return len(us) == 3 and all(dot(u_, v_) < 0 and 4 * dot(u_, v_) ** 2 == dot(u_, u_) * dot(v_, v_) for u_, v_ in itertools.combinations(us, 2))
LINES = [m for m in range(1, 17) if len(with_(m)) == 3]; FILMS = [m for m in range(1, 17) if len(with_(m)) == 2]
name_of = {with_(m): m for m in range(1, 17)}
say(all(thirds(i_) for i_ in range(4)) and LINES == [6, 10, 12, 14]
    and {m: sorted(name_of[with_(m) - {k}] for k in with_(m)) for m in LINES} == {6: [3, 5, 7], 10: [7, 9, 15], 12: [5, 9, 13], 14: [3, 13, 15]}
    and all(name_of[with_(m) | {1, 2, 3, 4}] == 11 for m in LINES),
    "round each line three films, each a third of a turn from each; by four parities each line's three films are the line with one bubble fewer, 3, 5 and 7 round 6, 7, 9 and 15 round 10, 5, 9 and 13 round 12, 3, 13 and 15 round 14, and each line with one bubble more is the point, 11")
say({F(dot(v_, w_), dot(v_, v_)) for v_, w_ in itertools.combinations(line, 2)} == {F(-1, 3)}
    and [m for m in LINES if 1 in with_(m)] == [6, 10, 14] and by_root['possibling'] == [2, 6, 10, 14]
    and (name_of[with_(6) & with_(14)], name_of[with_(6) & with_(10)], name_of[with_(10) & with_(14)]) == (3, 7, 15) and by_root['observing'] == [3, 7, 11, 15],
    "at the point four lines, each −1/3 from each: from each line three others; the four across names, 2, 6, 10 and 14, are the first bubble and its three lines, and between each two of the three lines is one film of that bubble, 3 between 6 and 14, 7 between 6 and 10, 15 between 10 and 14: with the point, the observing names")
comp = lambda m: name_of[frozenset({1, 2, 3, 4}) - with_(m)]
say([(m, comp(m)) for m in LINES] == [(6, 16), (10, 4), (12, 2), (14, 8)] and [(m, comp(m)) for m in (3, 5, 7)] == [(3, 9), (5, 15), (7, 13)] and comp(11) == 1
    and line == [neg(v_) for v_ in Fc] and all(mids[opposite[p_]] == neg(mids[p_]) for p_ in pairs),
    "all four parities inverting together: each line with the one bubble not on it, 6 with 16, 10 with 4, 12 with 2, 14 with 8; each film with its opposite film, 3 with 9, 5 with 15, 7 with 13; the point with nothing, 11 with 1; and from the point each line's going is the inverse of that bubble's middle, each film's of its opposite film's: the tunneling and the bubbling are each the other's inverse about the point")
say((with_(2), with_(3), with_(7), with_(6)) == (frozenset({1}), frozenset({1, 2}), frozenset({1, 3}), frozenset({1, 2, 3})) and with_(3) | with_(7) == with_(6),
    "by the gathered 2 inhaling, 3 exhausting, 6 ingesting and 7 exhaling: 2 is the first bubble, 3 and 7 its films with the second and with the third, and 6 the line the two films are on")
say(3 + 8 == 11 and with_(11) == with_(3) | {3, 4} and 17 - 6 == 11 and with_(11) == with_(6) | {4} and DUAL[7] == DUAL[11] and with_(11) == with_(10) | {2},
    "11, the point, is 3 by 8 up, the film of the first two with the third and fourth bubbles; it is 6 by 17 less, the line of the first three with the fourth; it is 10's next, one bubble more; and by the gathered duals 7 and 11 are one dual")

# ---- 21 ---------------------------------------------------------------------------------------------------------
print('21 · Selves alike densely compacted, three surfaces:')
NB = sorted({q_ for s1 in (1, -1) for s2 in (1, -1) for q_ in itertools.permutations((s1, s2, 0))})    # the twelve round one self
UP = (1, 1, 1)                                                                                        # the surface's own line
in_surface = [v_ for v_ in NB if dot(v_, UP) == 0]; above = [v_ for v_ in NB if dot(v_, UP) == 2]; below = [v_ for v_ in NB if dot(v_, UP) == -2]
over = lambda v_: tuple(F(v_[k]) - F(dot(v_, UP), 3) * UP[k] for k in range(3))                       # a self's place over the surface
third_turn = lambda us: all(dot(u_, v_) < 0 and 4 * dot(u_, v_) ** 2 == dot(u_, u_) * dot(v_, v_) for u_, v_ in itertools.combinations(us, 2))
surface_goings = {add(a_, b_) for a_ in in_surface for b_ in in_surface} | set(in_surface)
say(len(NB) == 12 and all(dot(v_, v_) == 2 for v_ in NB) and (len(in_surface), len(above), len(below)) == (6, 3, 3)
    and sorted(below) == sorted(neg(v_) for v_ in above) and set(in_surface) == {neg(v_) for v_ in in_surface}
    and third_turn([over(v_) for v_ in above]) and sorted(over(v_) for v_ in below) == sorted(tuple(-x_ for x_ in over(v_)) for v_ in above)
    and all(tuple(3 * x_ for x_ in over(v_)) in surface_goings and over(v_) not in surface_goings for v_ in above),
    "twelve round one self, each as far: six in its surface, three pairs each the other's inverse; three above and three below, the three below the inverses of the three above; over the surface the three above are a third of a turn from each other and each a third of a surface's own going, and the three below their inverses: a surface, the one above and the one below are three places, a third one way and a third the other")
mirror = lambda v_: tuple(F(v_[k]) - 2 * F(dot(v_, UP), 3) * UP[k] for k in range(3))                 # by the surface
below_as_above = [mirror(v_) for v_ in above]                                                         # the surface below at the place of the surface above
say(all(dot(v_, v_) == 2 for v_ in below_as_above) and all(dot(sub(u_, v_), sub(u_, v_)) == 2 for u_, v_ in itertools.combinations(below_as_above, 2))
    and not any(tuple(-x_ for x_ in v_) in [tuple(F(x_) for x_ in w_) for w_ in above] for v_ in below_as_above),
    "with the surface below at the place of the surface above, two places and no third, the three below are the three above's mirrors by the surface, each as far, and no one of them an above's inverse")
def of_four(c_): return [v_ for v_ in NB if dot(v_, c_) == 2]                                       # the three of twelve as far from a corner's middle as the self
say(all(len(of_four(c_)) == 3 and all(dot(sub(u_, v_), sub(u_, v_)) == 2 for u_, v_ in itertools.combinations(of_four(c_), 2)) for c_ in cube)
    and sorted(cube) == sorted(Fc + empty) and sorted(empty) == sorted(neg(v_) for v_ in Fc)
    and sorted(of_four(UP)) == sorted(above) and sorted(of_four(neg(UP))) == sorted(below)
    and sorted(len([v_ for v_ in of_four(c_) if v_ in in_surface]) for c_ in cube) == [0, 0, 2, 2, 2, 2, 2, 2],
    "round one self are eight betweens of four, each between it and three of its twelve, the four each with each: the cube's eight corners, two fours, each four each −1/3 from each and the one four the other's inverse; one is between the self and its three above, one between it and its three below, and each of six others between it, two in its surface and one above or below")
of_six = [e_ for e_ in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)) if len([v_ for v_ in NB if dot(v_, v_) - 2 * dot(v_, e_) == 0]) == 4]
say(len(of_six) == 6 and F(8, 4) == 2 and F(6, 6) == 1,
    "round one self are six betweens of six, each between it, four of its twelve and one more: with each self two betweens of four and one of six")
one_four = [c_ for c_ in cube if c_[0] * c_[1] * c_[2] == 1]
say(len(one_four) == 4 and {F(dot(u_, v_), dot(u_, u_)) for u_, v_ in itertools.combinations(one_four, 2)} == {F(-1, 3)}
    and all(sorted([neg(c_)] + [sub(tuple(2 * x_ for x_ in v_), c_) for v_ in of_four(c_)]) == sorted(neg(d_) for d_ in one_four) for c_ in one_four),
    "one four of the eight, and its inverse four not: the self has four round it each −1/3 from each, and each of the four has four selves round it each −1/3 from each, the inverse four's goings")
between_selves = [2, 6, 10, 14, 9, 17]
say(sorted(comp((m - 1) % 16 + 1) for m in between_selves) == [3, 4, 8, 11, 12, 16] and by_root['same-existing'] == [4, 8, 12, 16]
    and (comp(2), comp(3), comp(6), comp(7)) == (12, 9, 16, 13),
    "all four parities inverting together: the six names between selves, 2, 6, 10 and 14 across and 9 and 17 along, are with the four same-existing names, 4, 8, 12 and 16, and with 3 and 11; inhaling's 2 is with 12, exhausting's 3 with 9, ingesting's 6 with 16 and exhaling's 7 with 13")

# ---- 22 ---------------------------------------------------------------------------------------------------------
print('22 · A gate of a chip, not-both of two:')
not_both = lambda *ins: 0 if all(ins) else 1
say([not_both(1 in with_(m), 2 in with_(m)) for m in (1, 2, 3, 4)] == [1, 1, 0, 1]
    and [m for m in range(1, 17) if not_both(*[k in with_(m) for k in (1, 2, 3, 4)]) == 0] == [11],
    "not-both of two, with a double bubble's four things, nothing, a bubble, their film and the other bubble: is, is, is-not, is: its one is-not is with their film, the between of the two; not-all of four, with the sixteen, is is-not with the point, 11, and with no other")
def gate(a_, b_):
    along = bool(a_ and b_)                 # two, one after the other: going through with both is
    across = bool((not a_) or (not b_))     # two, one beside the other: going through with either is-not
    return along, across
say(all(sum(gate(a_, b_)) == 1 and (0 if gate(a_, b_)[0] else 1) == not_both(a_, b_) for a_ in (0, 1) for b_ in (0, 1)),
    "a gate of two along and two across, each of two inputs with one of each: with each of four ways one of the two goes through and only one, the two along with both is and the two across with each other way; and what it gives is not-both")
quarter = (1, 1, 1)
say(all(tuple(F(c_[k] - quarter[k], 2) for k in range(3)) in [tuple(F(x_) for x_ in v_) for v_ in NB] + [(0, 0, 0)] for c_ in one_four)
    and all(tuple(F(c_[k] - d_[k], 2) for k in range(3)) in [tuple(F(x_) for x_ in v_) for v_ in NB] + [(0, 0, 0)] for c_ in one_four for d_ in one_four),
    "one four of the eight betweens of four, filled: the filled betweens are the selves' own lattice again, a quarter along the cube's long line; and three inverting together about the middle of a self and one of its four has each of the four as a self, and that self as one of them: two lattices, each the other's")
def ring(states, moments=12):
    out = [tuple(states)]
    for m in range(moments): states = [not_both(x_, x_) for x_ in (states[1:] + states[:1] if len(states) > 1 else states)]; out.append(tuple(states))
    return out
plus = lambda x_: 1 if x_ else -1
say(all([plus(st[0]) for st in ring([x_])][1:] == alone_(plus(x_))[0]['A'] for x_ in (0, 1)),
    "one gate with its own now as its two inputs: its next is its now inverted, with each of twelve moments, as the code's self alone, its prior inverting with each")
two_code = {pr_: through({'A': pr_[0], 'B': pr_[1]}, each_with_each('AB'))[0] for pr_ in itertools.product((1, -1), repeat=2)}
say(all(len(set(ring([x_, 1 - x_]))) == 1 for x_ in (0, 1)) and all(ring([x_, x_])[m + 1] == tuple(1 - y_ for y_ in ring([x_, x_])[m]) for x_ in (0, 1) for m in range(12))
    and all(0 not in two_code[pr_]['A'] and two_code[pr_]['A'] == alone_(pr_[0])[0]['A'] for pr_ in ((1, -1), (-1, 1)))
    and all(two_code[pr_]['A'][1::2] == [0] * 6 for pr_ in ((1, 1), (-1, -1))),
    "two gates, each with the other's now: the two unlike, each is not-changing with each of twelve moments; the two alike, both invert with each moment; beside them the code's two selves bi-coupling: the two unlike, each inverting with each moment, a self alone's; the two alike, a 0 with each second moment")

# ---- 23 ---------------------------------------------------------------------------------------------------------
print("23 · A diamond's faces:")
say(len(cube) == 8 and sorted(one_four + [neg(c_) for c_ in one_four]) == sorted(cube) and all(len(of_four(c_)) == 3 for c_ in cube)
    and len(of_six) == 6 and all(dot(e_, c_) != 0 for e_ in of_six for c_ in cube) and len(cube) + len(of_six) == 14,
    "a field's eight faces of a diamond of the earth are by the cube's eight corners, each a going to a between of four round a self: the one four of the lattice and its inverse four, all eight, with one four only inside; a field's eight and six faces of a diamond grown by pressing are by the eight and by the six goings to the betweens of six: fourteen")

# ---- 24 ---------------------------------------------------------------------------------------------------------
print('24 · Names 6 and 7:')
THREE_ = {int(r_[0]): r_[5].strip() for r_ in rows_one}
say(THREE_[7] == 'tri-bi-co' and THREE_[6] == 'bi-co-bi' and ROOT_[7] == 'observing' and ROOT_[6] == 'possibling',
    "by Exhibit ONE Natural Resolver's table 7-now-observing has its three tri-bi-co, next, now and prior, and 6-now-co-possibling bi-co-bi")
say(with_(7) == with_(6) - {2} and KIND[len(with_(6))] == 'a line' and KIND[len(with_(7))] == 'a film' and changing[6] == 2
    and DUAL[6].endswith('-and-no-other') and DUAL[7].startswith('no-other-and-') and DUAL[7] == DUAL[11]
    and with_(5) == with_(6) - {1} and sorted(name_of[with_(6) - {k}] for k in with_(6)) == [3, 5, 7],
    "by four parities 7 is 6 with the second bubble fewer, a line to one of its three films, and by the gathered duals 6 and 7 have no-other with both; 5 is 6 with the first fewer; the three films round 6 are 3, 5 and 7; and 7 and 11, the point, are one dual")

# ---- 25 ---------------------------------------------------------------------------------------------------------
print('25 · 5 with 7, and two unlike kinds:')
say(with_(5) | with_(7) == with_(6) and with_(5) & with_(7) == with_(8) and with_(4) | with_(8) == with_(5) and with_(4) | with_(8) != with_(6)
    and (THREE_[5], THREE_[6], THREE_[7]) == ('co-bi-co', 'bi-co-bi', 'tri-bi-co'),
    "by four parities 5 with 7 is 6: the two films together are the line, and what the two films have alike is 8; 4 with 8 is 5, and is not 6; by Exhibit ONE Natural Resolver's table their threes are co-bi-co with 5, bi-co-bi with 6 and tri-bi-co with 7")
first_lattice = [(0, 0, 0)] + [tuple(F(x_) for x_ in v_) for v_ in NB]                           # selves, as far as the twelve
second_lattice = [tuple(F(c_[k], 2) for k in range(3)) for c_ in one_four]                       # the one four filled, round the self
def through_middle(c_, x_): return tuple(F(c_[k], 2) - x_[k] for k in range(3))                  # three inverting together about the middle of a self and one of its four
say(all(through_middle(c_, (0, 0, 0)) == tuple(F(c_[k], 2) for k in range(3)) and all(through_middle(c_, d_) in first_lattice for d_ in second_lattice) for c_ in one_four)
    and not any(through_middle(c_, x_) == x_ for c_ in one_four for x_ in first_lattice + second_lattice),
    "three inverting together about the middle of a self and one of its four: each place tried of the one lattice is with a place of the other, and no place tried of either is with itself; with one kind on both lattices the form is itself again, and with two unlike kinds, one on each, the one kind is with the other")

# ---- 26 ---------------------------------------------------------------------------------------------------------
print('26 · No-other-and-not-prior:')
code_text = one.split('```python', 1)[1].split('```', 1)[0]
bodies = {name_: body_ for name_, body_ in re.findall(r'def (_\d+_\w+)\((.*?)(?=\ndef |\Z)', code_text, re.S)}
say(sorted(m for m in DUAL if DUAL[m] == 'no-other-and-not-prior') == [7, 11] and ROOT_[7] == ROOT_[11] == 'observing'
    and (THREE_[7], THREE_[11]) == ('tri-bi-co', 'co-bi-co') and with_(11) == with_(7) | {2, 4} and 7 + 4 == 11
    and all(n_ in bodies['_1_now_existing'] for n_ in ('_7_now_observing', '_11_next_co_observing'))
    and not any(n_ in bodies[f_] for n_ in ('_7_now_observing', '_11_next_co_observing') for f_ in ('_9_next_co_discovering', '_17_next_existing')),
    "by the gathered duals no-other-and-not-prior is with 7 and with 11 and with no other name, each observing by its root; their threes are tri-bi-co and co-bi-co, alike but with next; by four parities 7 is a film and 11 the point, 7 with the second and fourth bubbles more; and 7 and 11 are in the code's lines of 1-now-existing, and in no line of its two other functions")
say(all(ONE_([('s', p_)], [])[1] == [('s', -p_)] and ONE_([('s', p_)], [('s', p_)])[1] == [('s', p_)] for p_ in (1, -1)),
    "1-now-existing with no other, nothing arriving: its next prior, its 11, is not its prior, each prior; with an other alike arriving, its next prior is its prior")

# ---- 27 ---------------------------------------------------------------------------------------------------------
print('27 · Self, other and both, all three observing, and one line:')
import ast
tree_ = ast.parse(code_text); fn_ = {f_.name: f_ for f_ in tree_.body if isinstance(f_, ast.FunctionDef)}
bound_ = [([e_.id for e_ in n_.target.elts], n_.iter.id) for n_ in fn_['_1_now_existing'].body if isinstance(n_, ast.For)]
binds7 = [n_ for n_ in ast.walk(tree_) if isinstance(n_, ast.Name) and n_.id == '_7_now_observing' and isinstance(n_.ctx, ast.Store)]
made_ = [int(n_.targets[0].id.split('_')[1]) for n_ in fn_['_1_now_existing'].body if isinstance(n_, ast.Assign)]
say(bound_ == [(['_4_now_co_same_existing', '_7_now_observing'], x_) for x_ in ('_2_now_possibling', '_3_now_co_observing', '_10_next_co_possibling')]
    and len(binds7) == 3 and made_ == [14, 12, 10, 11]
    and all([len(o_), len([('s', p_)]), len(ONE_([('s', p_)], o_)[0])] == [len(o_), 1, 1] for p_ in (1, -1) for o_ in ([], [('s', 1)], [('s', -1)])),
    "the code has 7-now-observing in three lines and no other, each with 4-now-co-same-existing, each within 1-now-existing: over 2-now-possibling, an other's parities; over 3-now-co-observing, a self's prior; over 10-next-co-possibling, the sharing of the two; one and then the next, making 14, 12, 10 and 11; with no other its first is over nothing, two of three")
say([KIND[len(with_(m))] for m in (2, 3, 10, 7)] == ['a bubble', 'a film', 'a line', 'a film']
    and with_(2) < with_(7) < with_(10) and with_(7) == with_(2) | with_(8) and with_(3) | with_(7) == with_(6)
    and [m for m in range(1, 17) if len(with_(m)) == 3 and 4 in with_(m)] == sorted(made_[:3]) and len(with_(made_[3])) == 4,
    "by four parities the three are one of each: 2 a bubble, 3 a film, 10 a line; 7 is the film of 2's bubble and 8's, 10 one of its two lines, and 3 a film with it on its other line, 6; and the four made are the three lines of the fourth bubble, 14, 12 and 10, and then the point, 11")
SIDE_ = {}
for l_ in one.split('\n'):
    h_ = re.match(r'\*\*(\d+)\*\* · \d+-', l_)
    if h_: cur_ = int(h_.group(1))
    elif l_.startswith('- *Sides*: '): SIDE_[cur_] = l_[len('- *Sides*: '):]
assert sorted(SIDE_) == list(range(1, 18))
starts_ = lambda *w_: [m for m in range(1, 17) if SIDE_[m].startswith(w_)]
say([m for m in range(1, 17) if len(with_(m)) == 1] == [2, 4, 8, 16]
    and SIDE_[2].startswith('others to self:') and SIDE_[4].startswith('self and other:') and SIDE_[8].startswith('self:') and SIDE_[16].startswith('a same-existing-society:')
    and starts_('other to self', 'others to self') == [2, 7, 14, 15] and all(with_(2) <= with_(m) for m in (2, 7, 14, 15))
    and starts_('self and other') == [4, 5] and all(with_(4) <= with_(m) for m in (4, 5))
    and starts_('self to other') == [6, 9, 10] and all(with_(8) <= with_(m) for m in (6, 9, 10))
    and [m for m in range(1, 17) if 'same-existing-society' in SIDE_[m]] == [13, 16] and all(with_(16) <= with_(m) for m in (13, 16))
    and starts_('self:') == [1, 3, 8, 11, 12] and [with_(8) <= with_(m) for m in (1, 3, 8, 11, 12)] == [False, False, True, True, True]
    and with_(6) == with_(2) | with_(4) | with_(8) and with_(3) == with_(2) | with_(4) and with_(5) == with_(4) | with_(8)
    and (ROOT_[3], ROOT_[7], ROOT_[5]) == ('observing', 'observing', 'existing'),
    "by Exhibit ONE Natural Resolver's sides each bubble alone has its own: 2 others to self, 4 self and other, 8 self, 16 a same-existing-society; each name other to self or others to self, 2, 7, 14 and 15, is of 2's bubble; each self and other or self and others, 4 and 5, of 4's; each self to other, 6, 9 and 10, of 8's; each of a same-existing-society within 1 to 16, 13 and 16, of 16's; the names with self alone first, 1, 3, 8, 11 and 12, are not each of 8's; and round 6, the line of 2's, 4's and 8's, the film of 2's and 8's is 7 and of 2's and 4's is 3, each observing by its root, and of 4's and 8's is 5, existing")
def round_(priors, moments):
    s_ = 'ABCDEFG'[:len(priors)]; sh, pr = through(dict(zip(s_, priors)), {(s_[i], 10): s_[(i + 1) % len(s_)] for i in range(len(s_))}, moments)
    return [sh[x_] for x_ in s_], [pr[x_] for x_ in s_]
def one_line(priors):
    n_ = len(priors); L_, P_ = round_(priors, 16 * n_)
    if not all(L_[(i + 1) % n_][m] == -L_[i][m - 2] for i in range(n_) for m in range(2, 16 * n_)): return False        # each next self: two moments on, inverted
    once = all(l_[2 * n_ + 2:] == [(-v if n_ % 2 else v) for v in l_[2:-2 * n_]] for l_ in L_)                       # once round: inverted with an odd ring
    return once and all(l_[4 * n_:] == l_[:-4 * n_] for l_ in L_)                                                   # twice round: again
say(all(one_line(p_) for n_ in (2, 3, 4, 5, 6, 7) for p_ in itertools.product((1, -1), repeat=n_)),
    "selves each sharing with its next, one way round, two to seven of them, each start: from its third moment each self's sharing is its prior self's of two moments before, inverted, one line each shares; once round, an odd ring's line is inverted and an even ring's is its own; twice round, each is its own again: three with twelve moments, five with twenty, seven with twenty-eight")
def of_three(priors):
    L_, P_ = round_(priors, 48); zs = [[i for i in range(3) if L_[i][m] == 0] for m in range(48)]
    if not all(P_[i][m + 1] == (P_[i][m] if L_[i][m] == 0 else -P_[i][m]) for i in range(3) for m in range(48)): return False   # at a 0 a prior is its next prior
    if len(set(priors)) == 1: return all(len(zs[m]) == (3 if m % 2 else 0) for m in range(48))
    return (all(len(zs[m]) == (1 if m % 2 else 0) for m in range(48)) and all(zs[m + 2][0] == (zs[m][0] + 1) % 3 for m in range(1, 45, 2))
            and all(l_[m] == -l_[m - 1] for l_ in L_ for m in range(1, 48) if l_[m] and l_[m - 1]))
say(all(of_three(p_) for p_ in itertools.product((1, -1), repeat=3))
    and all(0 not in l_ for a_ in (1, -1) for l_ in round_((a_, -a_), 48)[0]),
    "three selves one way round, each start not all alike: a 0 is with one self at each second moment and with none between, with one self and then its next, the way of the sharing; at its 0 a self's prior is its next prior, and with each other sharing its prior inverts; with three alike the 0 is with all three together; and two unlike, each with the other, have no 0")

# ---- 28 ---------------------------------------------------------------------------------------------------------
print('28 · One inversion, 7 to 11, and three selves one way round with the seventeen names:')
arrivings = [list(o_) for n_ in range(4) for o_ in itertools.product((1, -1, 0), repeat=n_)]
def alike_only(p_, o_): nz_ = [v for v in o_ if v]; return bool(nz_) and all(v == p_ for v in nz_)
say(len(arrivings) == 40 and all(ONE_([('s', p_)], [('s', v) for v in o_]) == ([('s', 0 if alike_only(p_, o_) else -p_)], [('s', p_ if alike_only(p_, o_) else -p_)])
                                  for p_ in (1, -1) for o_ in arrivings),
    "one place, each prior, each of forty arrivings of none to three: a self's next prior is its prior, and its sharing a 0, only with each parity arriving alike to it; with no other, with a 0 arriving, with an other unlike, and with both parities arriving, its next prior is not its prior, one inversion")
e24 = [frozenset(c) for r in range(3) for c in itertools.combinations((2, 4), r)]
say(with_(7) ^ with_(11) == {2, 4} == with_(6) ^ with_(10) and all(len(with_(a_) ^ with_(b_)) == 1 for a_ in (7, 11) for b_ in (6, 10))
    and {with_(m) for m in (7, 11, 6, 10)} == {frozenset({1, 3}) | e for e in e24} and {with_(m) for m in (9, 5, 12, 8)} == {frozenset({3}) | e for e in e24}
    and [m for m in range(1, 17) if 3 in with_(m)] == list(range(5, 13))
    and all(with_(m) ^ with_(m + 4) == ({2, 3} if (m - 1) // 4 % 2 == 0 else {2, 4}) for m in range(1, 17))
    and DUAL[7] == DUAL[11] == '-and-'.join({'other': 'no-other', 'prior': 'not-prior'}[c] for c in DUAL[3].split('-and-')),
    "Exhibit ONE Natural Resolver's middle bi-folding 7-11-6-10 is by four parities the film of the first and third bubbles with each of four ways of the second and fourth: 7 to 11 is two parities inverting, the second and the fourth, by 6 or by 10, the two co-possiblings, each one inversion from 7 and one from 11; its other middle bi-folding, 9-5-12-8, is the third bubble with the same four; the two are each name of the third bubble, 5 to 12; each name to its fourth next is two parities inverting, the second with the third from 1 to 4 and from 9 to 12, the second with the fourth from 5 to 8 and from 13 to 16; and by the gathered duals 7's and 11's one dual is 3's, other-and-prior, with each of its two inverted")
starts3 = [p_ for p_ in itertools.product((1, -1), repeat=3) if len(set(p_)) == 2]
def named(priors):
    L_, P_ = round_(priors, 17); return lambda i, m: L_[i][m - 1]                    # a self's sharing with each name, one moment each
def zero_self(nm, m): return next(i for i in range(3) if nm(i, m) == 0)
def even_and_odd(priors):
    nm = named(priors)
    return (all(sorted(nm(i, m) for i in range(3)) == [-1, 0, 1] for m in range(2, 17, 2))
            and all(0 not in [nm(i, m) for i in range(3)] and abs(sum(nm(i, m) for i in range(3))) == 1 for m in range(1, 18, 2))
            and all(nm(zero_self(nm, m - 1), m) == nm(zero_self(nm, m + 1), m) for m in range(3, 16, 2)))
say(all(even_and_odd(p_) for p_ in starts3),
    "three selves one way round, each start not all alike, the seventeen names one moment each: with each even name the three are a −, a 0 and a +, each once; with each odd name two are alike and one unlike, the two alike the self from its 0 and the self to its 0")
def right_spiral(priors):
    nm = named(priors); z = {m: zero_self(nm, m) for m in range(2, 17, 2)}; most = 1 if sum(priors) > 0 else -1
    path = [0 if m % 2 == 0 else nm(z[m + 1] if m < 17 else z[16], m) for m in range(1, 18)]
    by_root_ = {'existing': -most, 'discovering': -most, 'possibling': 0, 'observing': most, 'same-existing': 0}
    return (path == round_((most, most), 17)[0][0] and path[4:] == path[:-4] and path[2:] == [-v for v in path[:-2]]
            and all(path[m - 1] == by_root_[ROOT_[m].split(',')[0]] for m in range(1, 18))                 # 17 is existing, a next 1
            and all((nm(z[m], m - 1), nm(z[m], m + 1)) == ((-most, most) if ROOT_[m] == 'possibling' else (most, -most)) for m in range(2, 17, 2))
            and all(z[m + 2] == (z[m] + 1) % 3 for m in range(2, 15, 2)) and all(z[m + 8] == (z[m] + 1) % 3 for m in range(2, 9, 2)))
say(all(right_spiral(p_) for p_ in starts3),
    "the 0 followed from self to self through the seventeen names is the line of two selves alike, each with the other, of the prior two of the three have: one parity, a 0, its inverse, a 0, inverted after two and again after four; by root, each existing and each discovering name has the one parity, each possibling name a 0, each observing name the inverse, each same-existing name a 0; with each possibling name the 0's self has the one parity prior and its inverse next, with each same-existing name the other order; the 0 is with the next self with each second name, and with a name's 8 up")
def of_seventeen(priors):
    nm = named(priors); most = 1 if sum(priors) > 0 else -1; unlike = next(i for i in range(3) if priors[i] != most)
    if [i for i in range(3) if nm(i, 6) == 0 and nm(i, 12) == 0] != [(unlike + 1) % 3]: return False
    l_ = [nm((unlike + 1) % 3, m) for m in range(1, 18)]
    if not (l_[0:5] == [-most, most, -most, most, -most] and l_[6:11] == [-v for v in l_[0:5]] and l_[12:17] == l_[0:5]): return False
    L_, P_ = round_(priors, 24)
    for l12 in L_:
        plus = [m for m in range(12) if l12[m] == 1]
        if len(plus) != 5 or sorted(tuple(l12[(plus[k] + d) % 12] for d in range(1, (plus[(k + 1) % 5] - plus[k]) % 12)) for k in range(5)) != [(-1,), (-1,), (-1,), (-1, 0), (0, -1)]: return False
    return all(L_[(i + 2) % 3][m] == L_[i][m - 4] and L_[i][m] == -L_[i][m - 6] for i in range(3) for m in range(6, 24))
say(all(of_seventeen(p_) for p_ in starts3),
    "one self of the three has its 0s with 6 and with 12, the self the unlike one shares with: its seventeen are five parities one and then its inverse, a 0, the five inverted, a 0, and the five again, its 7 to 11 its 1 to 5 inverted; each self's twelve from one + to its next are three of two and two of three, one with − prior to 0 and one with 0 prior to −; and each self's sharing is its second next self's four moments on, and its own six moments on inverted")

print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
