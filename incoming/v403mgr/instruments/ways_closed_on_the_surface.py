"""The sixteen ways of changing a name's four parities together, taken as sets closed by one way and then another,
read with a field's seventeen ways a pattern repeats on a surface; and the second surface's quarter turn.
Reads Exhibit ONE Natural Resolver, Exhibit THREE Natural Numbers and Exhibit FOUR Natural Mathematics; executes;
writes no file; decides nothing. Each answer is all or none at all, by each set of ways and by each name.

Use: python3 -I incoming/v403mgr/instruments/ways_closed_on_the_surface.py <root>         each check
     python3 -I incoming/v403mgr/instruments/ways_closed_on_the_surface.py <root> json    the nine kinds and a field's seventeen, for a sheet

The logic. Exhibit FOUR Natural Mathematics: two inversions whose lines are an angle apart are a turn by twice
the angle; an exchange of two parities and then one inverted is a right spiral step. On the second surface round
its edges a parity changing is a fold: the fourth and the second about lines across, the third and the first
about lines down. A field's words: a pattern repeating on a surface has one of seventeen sets of folds, turns,
slides and folds with slides, and a field numbers them 1 to 17; its table is written whole here, each with its
finest turn.

Returned at main, 16 November 2026, each check is:
  The sixteen ways have sixty-seven sets closed by one way and then another. By what each has, a fold, a fold
  with a slide not along a fold's line, a turn, they are of nine kinds, each of the nine found: a field's
  first nine of seventeen, each with no turn finer than a turn of two.
  A field's seventeen by its finest turn: nine with none or a turn of two, its 1 to 9; three with a quarter
  turn, its 10 to 12; five with a turn of a third or a sixth, its 13 to 17.
  The second surface's quarter turn is an exchange of the two parities down with the two across, one
  inverted: no way of the sixteen. It exchanges odd and even; twice, it is 8 up; four times, none. Its rings are
  four, 1-8-9-16, 3-6-11-14, 2-5-10-13 and 4-7-12-15, each going on by 7 and 1 or by 3 and 5, one and then the
  other, each two adding to 8.
  The thirty-two, the sixteen ways and the sixteen with the two kinds of parity exchanged: of the exchanged,
  eight are quarter turns, four are folds about a diagonal line and four such folds with a slide. Each name is
  with itself by one alone of the four folds about a diagonal: 1, 3, 9 and 11; 5, 7, 13 and 15; 2, 4, 10 and
  12; 6, 8, 14 and 16. Each set of the thirty-two with a quarter turn is one of a field's three, each found:
  twelve of a field's seventeen are found on the second surface.
  With its undoing first and the quarter turn after it, each fold about a line down is a fold about a line
  across. With the bi-foldings 1-9-8-16 and 3-11-6-14 the quarter turn is 9 less and 17 less, one and then the
  other; the bi-foldings 2-15-7-10 and 4-13-5-12 it brings each onto the other.
"""
import glob, itertools, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers'); four = living('Exhibit_FOUR_Natural_Mathematics')
for text, said in ((four, 'Two inversions whose fixed lines stand an angle a apart are a field\'s rotation by 2a'),
                   (four, 'an exchange of P and Q and then P inverted, their lines forty-five degrees apart, make a right spiral step'),
                   (three, 'two folds in sequence are no fold'), (three, 'each row is a bi-folding**: 1-9-8-16, 2-15-7-10, 3-11-6-14 and 4-13-5-12')):
    assert said in text, said

# --- the sixteen names on the second surface, by their four parities
N = range(1, 17)
G = lambda n: (n - 1) ^ ((n - 1) >> 1); par = lambda n, k: (G(n) >> (k - 1)) & 1
def index(bits):
    i = 0
    for b in bits: i = i * 2 + (b ^ (i & 1))
    return i
where = {n: (index([par(n, 4), par(n, 2)]), index([par(n, 3), par(n, 1)])) for n in N}; at = {v: n for n, v in where.items()}
assert [[at[(r, c)] for c in range(4)] for r in range(4)] == [[1, 2, 7, 8], [4, 3, 6, 5], [13, 14, 11, 12], [16, 15, 10, 9]]

# --- a way: its move of the lines down and its move of the lines across; i none, A and B the two folds, s a slide of two
LINE = {'i': lambda x: x, 'A': lambda x: (1 - x) % 4, 'B': lambda x: (3 - x) % 4, 's': lambda x: (x + 2) % 4}
TIMES = {(a, b): next(c for c in LINE if all(LINE[a](LINE[b](x)) == LINE[c](x) for x in range(4))) for a in LINE for b in LINE}
WAYS = [(r, c) for r in 'iABs' for c in 'iABs']
then = lambda u, v: (TIMES[(u[0], v[0])], TIMES[(u[1], v[1])])
def by_parities(ks):                                         # the way of the parities ks changing together
    def move(n):
        g = G(n)
        for k in ks: g ^= 1 << (k - 1)
        return next(m for m in N if G(m) == g)
    return next(w for w in WAYS if all(where[move(n)] == (LINE[w[0]](where[n][0]), LINE[w[1]](where[n][1])) for n in N))
OF = {by_parities(ks): ks for size in range(5) for ks in itertools.combinations((4, 3, 2, 1), size)}
assert len(OF) == 16 and OF[('i', 'i')] == () and OF[('B', 'B')] == (4, 3)

# --- each set of ways closed by one way and then another
def closed(gens):
    h = {('i', 'i')} | set(gens)
    while True:
        more = {then(u, v) for u in h for v in h} - h
        if not more: return frozenset(h)
        h |= more
SETS = {closed(g) for size in range(5) for g in itertools.combinations(WAYS, size)}
def kind(h):                                                 # by what a set has: a field's name for it
    turn = any(r in 'AB' and c in 'AB' for r, c in h)
    m_down = {c for r, c in h if r == 'i' and c in 'AB'}; g_down = {c for r, c in h if r == 's' and c in 'AB'}       # folds about lines down; such folds with a slide down
    m_across = {r for r, c in h if c == 'i' and r in 'AB'}; g_across = {r for r, c in h if c == 's' and r in 'AB'}
    down, across = bool(m_down or g_down), bool(m_across or g_across)
    apart = bool(g_down - m_down) or bool(g_across - m_across)   # a fold with a slide, its line no fold's line
    if not down and not across: return 'p2' if turn else 'p1'
    if down != across:
        m, g = (m_down, g_down) if down else (m_across, g_across)
        return 'pg' if not m else 'cm' if g - m else 'pm'
    if m_down and m_across: return 'cmm' if apart else 'pmm'
    return 'pmg' if (m_down or m_across) else 'pgg'
SAID = {'p1': 'no fold and no turn: slides alone, or none', 'p2': 'turns, and no fold', 'pm': 'folds one way', 'pg': 'folds with slides one way, and no fold',
        'cm': "folds one way, with folds with slides between their lines", 'pmm': 'folds both ways', 'pmg': 'folds one way, and folds with slides the other way',
        'pgg': 'folds with slides both ways, and no fold', 'cmm': 'folds both ways, with folds with slides between their lines'}
# --- a field's seventeen, by its own numbering, each with its finest turn: 1 none, 2 a turn of two, 4 a quarter turn, 3 a third, 6 a sixth
FIELD = [('p1', 1), ('p2', 2), ('pm', 1), ('pg', 1), ('cm', 1), ('pmm', 2), ('pmg', 2), ('pgg', 2), ('cmm', 2), ('p4', 4), ('p4m', 4), ('p4g', 4), ('p3', 3), ('p3m1', 3), ('p31m', 3), ('p6', 6), ('p6m', 6)]
kinds = {}
for h in SETS: kinds.setdefault(kind(h), []).append(h)

# --- the second surface's quarter turn
quarter = lambda n: at[(where[n][1], 3 - where[n][0])]
def rings(f):
    seen, out = set(), []
    for n in N:
        if n not in seen:
            ring = [n]
            while f(ring[-1]) != n: ring.append(f(ring[-1]))
            seen |= set(ring); out.append(ring)
    return out

if WHAT == 'json':
    json.dump({'kinds': [[i + 1, name, SAID.get(name, ''), len(kinds.get(name, [])), {1: 'none', 2: 'a turn of two', 4: 'a quarter turn', 3: 'a turn of a third', 6: 'a turn of a sixth'}[t]] for i, (name, t) in enumerate(FIELD)],
               'rings': rings(quarter)}, sys.stdout); sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print('The sixteen ways, as sets closed by one way and then another:')
say(len(SETS) == 67 and all(('i', 'i') in h and all(then(u, v) in h for u in h for v in h) for h in SETS), 'sixty-seven sets, each with none, each closed by one way and then another')
first_nine = [name for name, t in FIELD[:9]]
say(sorted(kinds) == sorted(first_nine) and all(t in (1, 2) for _, t in FIELD[:9]) and all(t in (3, 4, 6) for _, t in FIELD[9:]),
    "by what each has they are of nine kinds, each of the nine found: a field's first nine of seventeen by its own numbering, each with no turn finer than a turn of two")
for i, name in enumerate(first_nine, 1):
    eg = min(kinds[name], key=lambda h: (len(h), sorted(OF[w] for w in h)))
    print(f"      {i} · a field's {name}: {SAID[name]} · of the sixty-seven, {len(kinds[name])} · one of them, by parities: " + '; '.join(' and '.join(map(str, OF[w])) or 'none' for w in sorted(eg, key=lambda w: (len(OF[w]), OF[w]))))
say([sum(1 for _, t in FIELD if t in s) for s in ((1, 2), (4,), (3, 6))] == [9, 3, 5] and [i + 1 for i, (_, t) in enumerate(FIELD) if t == 4] == [10, 11, 12] and [i + 1 for i, (_, t) in enumerate(FIELD) if t in (3, 6)] == [13, 14, 15, 16, 17],
    "a field's seventeen by its finest turn: nine with none or a turn of two, its 1 to 9; three with a quarter turn, its 10 to 12; five with a turn of a third or a sixth, its 13 to 17")
print("The second surface's quarter turn:")
q_par = all((par(quarter(n), 4), par(quarter(n), 2), par(quarter(n), 3), par(quarter(n), 1)) == (par(n, 3), par(n, 1), 1 - par(n, 4), par(n, 2)) for n in N)
say(q_par and not any(all(where[quarter(n)] == (LINE[w[0]](where[n][0]), LINE[w[1]](where[n][1])) for n in N) for w in WAYS),
    'it is an exchange of the two parities down with the two across, the fourth inverted: the fourth to the third, the second to the first, the third to the fourth, the first to the second; no way of the sixteen')
q2 = lambda n: quarter(quarter(n))
say(all((quarter(n) - n) % 2 == 1 for n in N) and all(q2(n) == (n + 8 if n < 9 else n - 8) for n in N) and all(q2(q2(n)) == n for n in N),
    'it exchanges odd and even; twice, it is 8 up; four times, none')
rs = rings(quarter)
say(sorted(sorted(r) for r in rs) == [[1, 8, 9, 16], [2, 5, 10, 13], [3, 6, 11, 14], [4, 7, 12, 15]]
    and all(sorted({(quarter(n) - n) % 16 for n in r}) in ([1, 7], [3, 5]) for r in rs) and all((quarter(n) - n) % 16 + (q2(n) - quarter(n)) % 16 == 8 for n in N),
    'its rings are four, 1-8-9-16, 3-6-11-14, 2-5-10-13 and 4-7-12-15, each going on by 7 and 1 or by 3 and 5, one and then the other, each two adding to 8')
print('      ' + ' · '.join('-'.join(map(str, r)) for r in rs))
back = {quarter(n): n for n in N}
say(all(quarter(at[(where[back[m]][0], LINE[c](where[back[m]][1]))]) == at[(LINE[c](where[m][0]), where[m][1])] for c in 'AB' for m in N),
    'with its undoing first and the quarter turn after it, each fold about a line down is a fold about a line across: the first parity as the second, the third as the fourth')
less9 = lambda n: (9 if n < 9 else 25) - n; less17 = lambda n: 17 - n
say(all(quarter(n) == (less9(n) if n % 2 else less17(n)) for n in (1, 8, 9, 16, 3, 6, 11, 14)) and {quarter(n) for n in (2, 15, 7, 10)} == {4, 13, 5, 12} and {quarter(n) for n in (4, 13, 5, 12)} == {2, 15, 7, 10},
    'with the bi-foldings 1-9-8-16 and 3-11-6-14, about the corner and about the centre, the quarter turn is 9 less and 17 less, one and then the other, each gone round; the bi-foldings 2-15-7-10 and 4-13-5-12 it brings each onto the other')

print('The thirty-two: the sixteen ways, and the sixteen with the two kinds of parity exchanged, down with across:')
POS = [(r, c) for r in range(4) for c in range(4)]
def act(m):                                                  # a move by its three: exchanged or not, its move of the first line, of the second
    sw, fr, fc = m
    return tuple((LINE[fr](c), LINE[fc](r)) if sw else (LINE[fr](r), LINE[fc](c)) for r, c in POS)
MOVES32 = [(sw, fr, fc) for sw in (0, 1) for fr in 'iABs' for fc in 'iABs']
PERM = {act(m): m for m in MOVES32}; assert len(PERM) == 32
compose = lambda p, q: tuple(p[POS.index(q[i])] for i in range(16))        # q, and then p
assert all(compose(p, q) in PERM for p in PERM for q in PERM) and PERM[tuple((c, 3 - r) for r, c in POS)] == (1, 'i', 'B')
flips = lambda m: (m[1] in 'AB') + (m[2] in 'AB')
itself = lambda m: sorted(at[POS[i]] for i in range(16) if act(m)[i] == POS[i])
quarters = [m for m in MOVES32 if m[0] and flips(m) == 1]
diag_folds = [m for m in MOVES32 if m[0] and flips(m) != 1 and itself(m)]
diag_glides = [m for m in MOVES32 if m[0] and flips(m) != 1 and not itself(m)]
say(len(quarters) == 8 and len(diag_folds) == 4 and len(diag_glides) == 4 and all(not itself(m) for m in quarters) and all(len(itself(m)) == 4 for m in diag_folds),
    'of the sixteen exchanged, eight are quarter turns, one parity inverted; four are folds about a diagonal line, each with four names with itself; four are folds about a diagonal line with a slide along it, with none')
fixed = sorted(itself(m) for m in diag_folds)
say(fixed == [[1, 3, 9, 11], [2, 4, 10, 12], [5, 7, 13, 15], [6, 8, 14, 16]] and sorted(n for v in fixed for n in v) == list(N)
    and all(not itself((0, r, c)) for r in 'iABs' for c in 'iABs' if (r, c) != ('i', 'i')),
    'each name is with itself by one alone of the four folds about a diagonal: 1, 3, 9 and 11; 5, 7, 13 and 15; 2, 4, 10 and 12; 6, 8, 14 and 16; and by no way of the sixteen but none')
cyc = lambda n: (n - 1) // 4 + 1
say(all(len({n % 2 for n in v}) == 1 and {cyc(n) for n in v} in ({1, 3}, {2, 4}) for v in fixed),
    'each of the four is the odd names or the even names of the first and third four-cyclings, or of the second and fourth')
ident = act((0, 'i', 'i'))
def closure(gens):
    h = {ident} | set(gens)
    while True:
        more = {compose(p, q) for p in h for q in h} - h
        if not more: return frozenset(h)
        h |= more
ALL32, grow = {frozenset({ident})}, [frozenset({ident})]
while grow:
    h = grow.pop()
    for p in PERM:
        k = closure(h | {p})
        if k not in ALL32: ALL32.add(k); grow.append(k)
inverse = lambda p: next(q for q in PERM if compose(p, q) == ident)
FOLDS = {act(m) for m in MOVES32 if (not m[0] and flips(m) == 1 and 'i' in m[1:]) or m in diag_folds}
QUART = {act(m) for m in quarters}
def kind4(h):
    if not h & QUART: return None
    if not h & FOLDS: return 'p4'
    return 'p4m' if any(compose(m, compose(t, m)) == inverse(t) for m in h & FOLDS for t in h & QUART) else 'p4g'
with4 = {}
for h in ALL32:
    if kind4(h): with4.setdefault(kind4(h), []).append(h)
say(sorted(with4) == ['p4', 'p4g', 'p4m'] == sorted(name for name, t in FIELD if t == 4),
    "each set of the thirty-two with a quarter turn is one of a field's three with a quarter turn, its 10 to 12, and each of the three is found: quarter turns and no fold; folds, one through a quarter turn's point; folds, and none through a quarter turn's point")
print(f"      sets closed, of the thirty-two: {len(ALL32)} · with a quarter turn: " + ', '.join(f"a field's {k} {len(v)}" for k, v in sorted(with4.items())))
four_times = lambda p: compose(p, compose(p, compose(p, p)))
say(len({kind(h) for h in SETS} | set(with4)) == 12 and [name for name, t in FIELD if t in (3, 6)] == [name for name, _ in FIELD[12:]] and all(four_times(p) == ident for p in PERM),
    "twelve of a field's seventeen are found on the second surface, its 1 to 12; its 13 to 17 each have a turn of a third, and no move of the thirty-two is one: each comes to none with four times")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
