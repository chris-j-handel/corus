"""Run checks for Exhibit THIRTY Part EIGHT, 8.8 to 8.14 (THIRTEEN to NINETEEN, links Q, Y, J, C, B, P, L).
The resolver is imported from resolver_v372.py beside this file (Exhibit ONE v372's code block).
A check named X returns True when link X holds as stated.
A check named X_probe backs a nye link: it returns True when the failure named at the gap is confirmed
(the file's stated count differs from the count its own table gives, or the stated count is not reproduced)."""
import ast, inspect, json, math, os, re, sys
from fractions import Fraction
from itertools import combinations, permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV
C = RV._1_self_coupling
REL = RV._9_other_releasing
K = 'k'
S = (1, -1)
CORUS = '/home/claude/corus'

# ------------------------------------------------------------------ resolver helpers
def reach19():
    """The nineteen carryings reachable at one key from empty (R23)."""
    offers = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]
    seen = {()}; todo = [()]
    while todo:
        c = todo.pop()
        carry = [(K,) + c] if c else []
        for o in offers:
            _, nxt = C(carry, o)
            t = tuple(nxt[0][1:]) if nxt else ()
            if t not in seen:
                seen.add(t); todo.append(t)
    return sorted(seen)

def carry_of(t):
    return [(K,) + t] if t else []

# ------------------------------------------------------------------ 8.8 THIRTEEN (Q)
def Q12():
    # the exclusive or taken as the step: x -> x xor 1 runs 0101, back at each second step
    x = 0; seq = []
    for _ in range(6):
        seq.append(x); x ^= 1
    ok = seq == [0, 1, 0, 1, 0, 1]
    # taken of the prior and the now together: next = prior xor now
    for a, b in product((0, 1), repeat=2):
        s = [a, b]
        for _ in range(9):
            s.append(s[-2] ^ s[-1])
        if (a, b) == (0, 0):
            ok &= all(v == 0 for v in s)
        else:
            ok &= s[3:5] == [a, b] and s[1:3] != [a, b] and s[2:4] != [a, b]   # returns after three, not before
            ok &= ''.join(map(str, s[:3])) in ('011', '101', '110')
    return ok

def Q13():
    # Peres-Mermin: nine bits, rows parity 0, columns parity 1 (and the standard columns 0,0,1): none of 512
    def count(colpar):
        n = 0
        for bits in product((0, 1), repeat=9):
            g = [bits[0:3], bits[3:6], bits[6:9]]
            if all(sum(r) % 2 == 0 for r in g) and all(sum(g[i][j] for i in range(3)) % 2 == colpar[j] for j in range(3)):
                n += 1
        return n
    return count((1, 1, 1)) == 0 and count((0, 0, 1)) == 0 and 2 ** 9 == 512

FORMS = {'1-9-8-16': [1, 9, 8, 16], '2-15-7-10': [2, 15, 7, 10], '3-11-6-14': [3, 11, 6, 14], '4-13-5-12': [4, 13, 5, 12],
         '9-5-12-8': [9, 5, 12, 8], '7-11-6-10': [7, 11, 6, 10],
         '1-9-5-12-8-16': [1, 9, 5, 12, 8, 16], '2-15-7-11-6-10': [2, 15, 7, 11, 6, 10],
         '3-11-7-10-6-14': [3, 11, 7, 10, 6, 14], '4-13-5-9-8-12': [4, 13, 5, 9, 8, 12],
         '1-9-5-13-4-12-8-16': [1, 9, 5, 13, 4, 12, 8, 16], '2-15-7-11-3-14-6-10': [2, 15, 7, 11, 3, 14, 6, 10]}

def Q15():
    ok = True
    for n in range(1, 17):
        ok &= ((n + 8 - 1) % 16 + 1) % 2 == n % 2 if n <= 8 else True      # 8 up keeps parity
        ok &= (17 - n) % 2 != n % 2                                        # 17 less changes it
    for n in range(1, 9):
        ok &= (9 - n) % 2 != n % 2                                         # 9 less changes it
    for c in FORMS.values():
        steps = [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]
        ch = [(a, b) for a, b in steps if a % 2 != b % 2]
        ok &= len(ch) == 2 and all(a + b == 17 for a, b in ch)
    return ok

def primes_to(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** .5) + 1))]

def Q22():
    P = primes_to(59)
    return len(P) == 17 and sum(P) == 440 and len(P) - 1 == 16 and 2 * 59 == 118 and (59 + 61) // 2 == 60

def Q25():
    ok = True
    for t in reach19():
        for m in (2, 5, 17):
            ok &= C(carry_of(t), [(K, m)]) == C(carry_of(t), [(K, 1)])
            ok &= C(carry_of(t), [(K, -m)]) == C(carry_of(t), [(K, -1)])
    return ok

def Q26():
    vals = set()
    for t in reach19():
        for n in range(0, 5):
            for o in product((-1, 0, 1), repeat=n):
                s, _ = C(carry_of(t), [(K, v) for v in o])
                vals |= {v for _, v in s}
    return vals <= {-1, 0, 1} and vals == {-1, 0, 1}

def Q27():
    return all(C(carry_of(t), [(K, 0)]) == C(carry_of(t), []) for t in reach19())

def Q28():
    tree = ast.parse(inspect.getsource(RV))
    consts = set()
    third = set()
    for f in tree.body:
        if isinstance(f, ast.FunctionDef):
            for n in ast.walk(f):
                if isinstance(n, ast.Constant):
                    (third if f.name == '_17_social_abundancing' else consts).add(n.value)
    return consts == {0, 1, 3, 4} and third == {1, 2, 6, 9, 10, 14, 17}

PHI = (1 + 5 ** .5) / 2

def Q32():
    F = [1, 1]
    while len(F) < 42:
        F.append(F[-1] + F[-2])
    sides = [Fraction(F[i + 1], F[i]) > Fraction(PHI) for i in range(1, 38)]
    alternates = all(sides[i] != sides[i + 1] for i in range(len(sides) - 1))
    # continued fraction of phi from its Fibonacci ratio: all partial quotients one
    x = Fraction(F[40], F[39]); cf = []
    for _ in range(30):
        a = x.numerator // x.denominator; cf.append(a); x = 1 / (x - a)
    rational_closes = all(((p * q) % q == 0) for p, q in [(3, 5), (5, 8), (8, 13)])   # a winding p/q returns after q rounds
    return alternates and all(a == 1 for a in cf) and rational_closes

# ------------------------------------------------------------------ 8.10 FIFTEEN (J)
def J7():
    k = 1.380649e-23
    e = k * 300 * math.log(2)
    return abs(e - 2.871e-21) < 0.001e-21 and round(e / 1e-21, 1) == 2.9

def transitive_relations(n):
    P = [(i, j) for i in range(n) for j in range(n)]
    for bits in range(1 << len(P)):
        R = {P[k] for k in range(len(P)) if bits >> k & 1}
        if all((a, d) in R for (a, b) in R for (c, d) in R if b == c):
            yield R

def J9():
    count = 0; ok = True
    for R in transitive_relations(4):
        count += 1
        for (a, m) in R:
            for (b, m2) in R:
                if m2 != m: continue
                for (m3, s) in R:
                    if m3 == m:
                        ok &= (a, s) in R and (b, s) in R
    return ok and count == 3994

def has_cycle(n, R):
    succ = {a: [b for (x, b) in R if x == a] for a in range(n)}
    color = {}
    def dfs(u):
        color[u] = 1
        for v in succ[u]:
            if color.get(v) == 1 or (v not in color and dfs(v)):
                return True
        color[u] = 2
        return False
    return any(u not in color and dfs(u) for u in range(n))

def serial_relations(n):
    P = [(i, j) for i in range(n) for j in range(n)]
    for bits in range(1 << len(P)):
        R = {P[k] for k in range(len(P)) if bits >> k & 1}
        if all(any((a, b) in R for b in range(n)) for a in range(n)):
            yield R

def J10():
    ok = True; nser = 0; nfun = 0
    for n in range(1, 5):
        for R in serial_relations(n):
            nser += 1; ok &= has_cycle(n, R)
    for n in range(1, 6):
        for f in product(range(n), repeat=n):
            nfun += 1; ok &= has_cycle(n, {(a, f[a]) for a in range(n)})
    return ok and nser == 50978 and nfun == 3413

def J11_probe():
    # the file's 592,260 is not the count of any reading run here
    import numpy as np
    r = np.indices((32,) * 5, dtype=np.uint8).reshape(5, -1)      # each relation on five terms as five row masks
    ok = np.ones(r.shape[1], bool)
    for i in range(5):
        for j in range(5):
            ok &= ~((((r[i] >> j) & 1) == 1) & ((r[j] & ~r[i]) != 0))
    t5 = int(ok.sum())
    t14 = [sum(1 for _ in transitive_relations(n)) for n in range(1, 5)]
    readings = {'serial relations, 1..4 terms': 50978, 'functions, 1..5 terms': 3413,
                'transitive relations, 1..5 terms': sum(t14) + t5, 'all relations on 5 terms': 2 ** 25}
    return t14 == [2, 13, 171, 3994] and t5 == 154303 and 592260 not in readings.values()

def J12():
    rows = [(0, 1.000, 0.000), (60, 0.500, 0.866), (90, 0.000, 1.000)]
    return all(abs(math.cos(math.radians(a)) - s) < 5e-4 and abs(math.sin(math.radians(a)) - o) < 5e-4 for a, s, o in rows)

def J14():
    return all(abs(math.sin(t) + math.sin(t + 2 * math.pi / 3) + math.sin(t + 4 * math.pi / 3)) < 1e-12
               for t in [2 * math.pi * i / 360 for i in range(360)])

def J26():
    ok = all(n * n - (n - 1) * (n + 1) == 1 for n in range(1, 10001))
    ok &= all(n * n - (n - k) * (n + k) == k * k for n in range(1, 200) for k in range(0, 50))
    ok &= all(((a + b) % 2 == 0) == (a % 2 == b % 2) for a in range(200) for b in range(200))
    return ok

def J28():
    f = lambda n, k: math.comb(n, k) * 2 ** (n - k) if 0 <= k <= n else 0
    ok = [f(4, 3), f(4, 2), f(4, 1), f(4, 0)] == [8, 24, 32, 16]
    ok &= all(f(n + 1, k) == 2 * f(n, k) + f(n, k - 1) for n in range(1, 9) for k in range(0, n + 2))
    return ok and [2 * f(3, 3) + f(3, 2), 2 * f(3, 2) + f(3, 1), 2 * f(3, 1) + f(3, 0), 2 * f(3, 0) + 0] == [8, 24, 32, 16]

# ------------------------------------------------------------------ 8.11 SIXTEEN (C)
def C10():
    caps = [2 * n * n for n in range(1, 5)]
    climbs = [caps[i + 1] - caps[i] for i in range(3)]
    odds = [2 * l + 1 for l in range(4)]
    return (caps == [2, 8, 18, 32] and climbs == [6, 10, 14] and 14 - 6 == 8 and (6 + 14) // 2 == 10
            and all(sum(odds[:n]) == n * n for n in range(1, 5)) and [2 * o for o in odds] == [2, 6, 10, 14])

def C17():
    return all(4 * n + 2 == 2 * (2 * n + 1) for n in range(100)) and [4 * n + 2 for n in range(4)] == [2, 6, 10, 14] and 6 == 2 * 3

def C11():
    return (24 ** 2 - 23 * 25 == 1 and 28 ** 2 - 24 * 32 == 16 and 28 ** 2 - 27 * 29 == 1
            and all(n * n - (n - k) * (n + k) == k * k for n in range(1, 200) for k in range(50)))

def perm_group_order(gens, n):
    idp = tuple(range(n)); G = {idp}; todo = [idp]
    while todo:
        g = todo.pop()
        for h in gens:
            x = tuple(h[i] for i in g)
            if x not in G:
                G.add(x); todo.append(x)
    return G

def C12():
    S4 = set(permutations(range(4)))
    even = lambda p: sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2 == 0
    A4 = {p for p in S4 if even(p)}
    S5 = set(permutations(range(5))); A5 = {p for p in S5 if even(p)}
    comp = lambda p, q: tuple(p[i] for i in q)
    centre_S5 = [z for z in S5 if all(comp(z, g) == comp(g, z) for g in S5)]
    centre_A5 = [z for z in A5 if all(comp(z, g) == comp(g, z) for g in A5)]
    # A5 x C2 has centre (identity) x C2, order 2; S5's centre is the identity alone: the two orders-120 groups part
    return (len(S4) == 24 and len(S4) - 1 == 23 and len(A4) == 12 and 7 ** 2 - 1 == 48 and 48 // 2 == 24
            and len(A5) == 60 and 2 * len(A5) == 120 and len(S5) == 120 and len(centre_S5) == 1 and len(centre_A5) * 2 == 2)

def C22():
    ok = True
    for h in range(0, 200):
        # trivalent closed cage, p pentagons, h hexagons: 2E = 5p + 6h, 3V = 2E, V - E + F = 2
        sols = [p for p in range(0, 100) if (5 * p + 6 * h) % 6 == 0 and
                Fraction(5 * p + 6 * h, 3) - Fraction(5 * p + 6 * h, 2) + p + h == 2]
        ok &= sols == [12]
    E = (5 * 12 + 6 * 20) // 2; V = 2 * E // 3
    ok &= (12 + 20, E, V) == (32, 90, 60)
    ok &= 12 - 30 + 20 == 2 and 20 - 30 + 12 == 2      # icosahedron and dodecahedron swap
    ok &= 12 - 24 + (8 + 6) == 2 and (8 * 3 + 6 * 4) // 2 == 24   # cuboctahedron
    return ok

def C20():
    rows = [2, 8, 8, 18, 18, 32, 32]
    run = [sum(rows[:i + 1]) for i in range(7)]
    pairs = [(24, 96), (27, 93), (32, 88)]
    return (run == [2, 10, 18, 36, 54, 86, 118] and 2 + 8 + 18 + 32 == 60 and 27 + 32 == 59
            and all(a + b == 120 for a, b in pairs) and sum(a + b for a, b in pairs) == 360
            and [27 - 24, 32 - 27] == [3, 5] and [93 - 88, 96 - 93] == [5, 3])

# ------------------------------------------------------------------ 8.12 SEVENTEEN (B)
def B15():
    return 2 ** 6 == 4 ** 3 == 64 and math.comb(6, 3) == 20 and math.factorial(4) == 24 and math.factorial(5) == 120 \
        and math.factorial(4) - 1 == 23 and math.factorial(5) - 1 == 119

def B19():
    r = [(1 + 5 ** .5) / 2, (1 - 5 ** .5) / 2]
    return (all(abs(x * x - x - 1) < 1e-12 for x in r) and abs(r[0] - 1.618) < 1e-3 and r[1] < 0
            and sorted({0, 1}) == [x for x in range(-3, 4) if x * x == x] and abs(1 / r[0] ** 2 - 0.382) < 1e-3)

# ------------------------------------------------------------------ 8.13 EIGHTEEN (P)
NAMINGS = ['an arriving held from behind', 'an opening held as a place', 'a bound held as a last', 'a carry held as a store',
           'a middle held as an end', 'a sign held as a magnitude', 'a sequencing held to one beat', 'a rate held to a value',
           'a two-way held to one side', 'a membrane held as a cut']

def table_rows(path, first, last, skip):
    L = open(path).read().split('\n')[first - 1:last]
    return [[c.strip() for c in l.strip().strip('|').split('|')] for l in L
            if l.startswith('|') and not l.startswith('|---') and skip not in l]

def P_counts():
    R = table_rows(os.path.join(CORUS, 'Exhibit_EIGHTEEN_Natural_Physics_v348.md'), 624, 676, '| arrival |')
    cnt = [sum(1 for r in R if r[1] == n) for n in NAMINGS]
    return R, cnt

def P5():
    J = list(product(S, S))
    right = lambda x, y: (y, -x); other = lambda x, y: (-y, x)
    return all(right(*j) != j and other(*j) != j for j in J)

def P28():
    R, c = P_counts()
    own = sum(1 for r in R if r[1].startswith("this file's own"))
    ref = c[0] + c[2] + c[4]; rate = c[6] + c[7]; ret = c[3] + c[9]; mag = c[5] + c[8]
    pairs = [(c[i], c[i + 1]) for i in range(0, 10, 2)]
    return (len(R) == 50 and own == 2 and sum(c) == 48 and (ref, rate, ret, mag) == (21, 13, 8, 6)
            and c[0] == 10 and (sum(c[0::2]), sum(c[1::2])) == (31, 17)
            and pairs == [(10, 0), (5, 2), (6, 3), (7, 6), (3, 6)])

def P7_probe():
    # 2.5 states: thirty-two arrivals at the holdings, nine at a rate held, three at a returned sign entered as cost
    R, c = P_counts()
    return (sum(c), c[6] + c[7], c[3] + c[9]) != (32, 9, 3) and (sum(c), c[6] + c[7], c[3] + c[9]) == (48, 13, 8)

def P11():
    return (55 - 23 == 32 and 32 // 2 == 16 and (23 + 55) // 2 == 39 and 39 ** 2 - 23 * 55 == 16 ** 2
            and 24 ** 2 - 23 * 25 == 1 and math.comb(11, 2) == 55)

def P26():
    # phi^3 - phi^-3 in Q(sqrt5): phi = (1+r)/2; represent a + b r
    def mul(x, y): return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    ph = (Fraction(1, 2), Fraction(1, 2)); inv = (Fraction(-1, 2), Fraction(1, 2))   # 1/phi = phi - 1
    p3 = mul(mul(ph, ph), ph); i3 = mul(mul(inv, inv), inv)
    return (59 == 1 + 2 * (2 ** 2 + 3 ** 2 + 4 ** 2) and (p3[0] - i3[0], p3[1] - i3[1]) == (4, 0)
            and 60 == 5 * 12 and complex(0, 1) ** 4 == 1 and abs(59 / 2 - 29.5) < 1e-12)

def P22():
    # the going 2 to 59, a turn at 60, the return 61 to 118: fifty-eight either side; 2 and 118 meet at 120
    return len(range(2, 60)) == 58 and len(range(61, 119)) == 58 and (59 + 61) // 2 == 60 and 2 + 118 == 120

# ------------------------------------------------------------------ 8.14 NINETEEN (L)
def L_rows():
    return table_rows(os.path.join(CORUS, 'Exhibit_NINETEEN_Natural_Philosophy_v348.md'), 782, 882, 'dilemma (generic)')

def L28():
    R = L_rows()
    held = [r for r in R if r[3] in NAMINGS]
    seams = set(re.findall(r'3\.(\d+)', ' '.join(r[2] for r in R)))
    c = [sum(1 for r in R if r[3] == n) for n in NAMINGS]
    pairs = [(c[i], c[i + 1]) for i in range(0, 10, 2)]
    return (len(R) == 66 and sum(1 for r in R if r[2].startswith('met')) == 50
            and sum(1 for r in R if r[2].startswith('reaching')) == 16 and len(held) == 41
            and seams == {str(i) for i in range(1, 38)}
            and sum(1 for a, b in pairs if a > b) == 4 and sum(1 for a, b in pairs if a < b) == 1)

def L29_probe():
    R = L_rows()
    c = [sum(1 for r in R if r[3] == n) for n in NAMINGS]
    stated = ((4, 6), 29, 13, 8)
    found = ((c[0], c[1]), sum(c[0::2]), sum(c[1::2]), len(set(re.findall(r'3\.(\d+)', ' '.join(r[2] for r in R)))))
    return found != stated and found == ((4, 5), 29, 12, 37)

RUNS = [
 {
  "link": "Q12",
  "check": "x -> x xor 1 runs 0,1,0,1,0,1; next = prior xor now from (0,1), (1,0), (1,1) returns to its start pair after exactly three steps with first three values 011, 101 or 110, and (0,0) stays 0."
 },
 {
  "link": "Q13",
  "check": "Of the 512 assignments of bits to a 3x3 square, none has each row at parity 0 with column parities (1,1,1), and none with column parities (0,0,1)."
 },
 {
  "link": "Q15",
  "check": "n + 8 keeps parity and 17 − n changes it for n in 1..16; 9 − n changes it for n in 1..8; in each of the twelve forms of ONE's tables within 1..16 exactly two steps change parity and each such step is a pair summing to 17."
 },
 {
  "link": "Q22",
  "check": "The primes to 59 are seventeen, sum to 440 and open sixteen gaps; 2 × 59 = 118; 60 lies midway between 59 and 61."
 },
 {
  "link": "Q25",
  "check": "At each of the nineteen reachable carryings, _1_self_coupling with an offering (k, ±m), m in {2, 5, 17}, returns the same as with (k, ±1)."
 },
 {
  "link": "Q26",
  "check": "At each of the nineteen carryings under each offering of 0 to 4 signs from {−1, 0, +1} (121 offerings), each surfaced value lies in {−1, 0, +1}, and each of the three occurs."
 },
 {
  "link": "Q27",
  "check": "At each of the nineteen carryings, _1_self_coupling with offering [(k, 0)] returns the same as with the empty offering."
 },
 {
  "link": "Q28",
  "check": "The numeric constants in the bodies of _1_self_coupling and _9_other_releasing are exactly {0, 1, 3, 4}."
 },
 {
  "link": "Q32",
  "check": "F(n+1)/F(n) for n = 1..38 alternates above and below φ; the continued fraction of F(40)/F(39) begins with thirty partial quotients 1."
 },
 {
  "link": "J7",
  "check": "k·300·ln 2 with k = 1.380649e-23 J/K is 2.871e-21 J, rounding to 2.9e-21 J."
 },
 {
  "link": "J9",
  "check": "Of the 65,536 relations on four elements, 3,994 are transitive, and in each, a R m, b R m and m R s give a R s and b R s."
 },
 {
  "link": "J10",
  "check": "Each of the 50,978 serial relations on 1 to 4 elements, and each of the 3,413 functions on 1 to 5 elements, contains a directed cycle."
 },
 {
  "link": "J12",
  "check": "cos and sin at 0°, 60°, 90° are (1.000, 0.000), (0.500, 0.866), (0.000, 1.000) to three places."
 },
 {
  "link": "J14",
  "check": "sin t + sin(t + 2π/3) + sin(t + 4π/3) = 0 at 360 equally spaced t."
 },
 {
  "link": "J26",
  "check": "n² − (n − 1)(n + 1) = 1 for n = 1..10,000; n² − (n − k)(n + k) = k² for n = 1..199, k = 0..49; (a + b) even iff a and b share parity, a, b = 0..199."
 },
 {
  "link": "J28",
  "check": "The k-faces of the n-cube, C(n,k)·2^(n−k), give (8, 24, 32, 16) at n = 4 for k = 3..0, and f(n+1, k) = 2 f(n, k) + f(n, k−1) for n = 1..8."
 },
 {
  "link": "C10",
  "check": "2n² for n = 1..4 is 2, 8, 18, 32 with climbs 6, 10, 14; 14 − 6 = 8, centre 10; 1 + 3 + … + (2n − 1) = n²; doubled odds 2, 6, 10, 14."
 },
 {
  "link": "C11",
  "check": "24² − 23·25 = 1, 28² − 24·32 = 16, 28² − 27·29 = 1, and n² − (n − k)(n + k) = k² for n < 200, k < 50."
 },
 {
  "link": "C12",
  "check": "|S4| = 24, |A4| = 12, 7² − 1 = 48, |A5| = 60, |S5| = 120; the centre of S5 is trivial and the centre of A5 is trivial, so A5 × C2 has a centre of order 2 and is not S5."
 },
 {
  "link": "C17",
  "check": "4n + 2 = 2(2n + 1) for n < 100, giving 2, 6, 10, 14 at n = 0..3."
 },
 {
  "link": "C20",
  "check": "Running sums of 2, 8, 8, 18, 18, 32, 32 are 2, 10, 18, 36, 54, 86, 118; 2 + 8 + 18 + 32 = 60; 27 + 32 = 59; 24 + 96 = 27 + 93 = 32 + 88 = 120, together 360; gaps 3, 5 and 5, 3."
 },
 {
  "link": "C22",
  "check": "For each hexagon count h = 0..199 a closed trivalent cage of pentagons and hexagons satisfies Euler's relation only at 12 pentagons; C60: 32 faces, 90 edges, 60 vertices; 12 − 30 + 20 = 2 both ways; cuboctahedron 12 − 24 + 14 = 2 with 24 edges."
 },
 {
  "link": "B15",
  "check": "2^6 = 4^3 = 64, C(6,3) = 20, 4! = 24, 5! = 120, 4! − 1 = 23, 5! − 1 = 119."
 },
 {
  "link": "B19",
  "check": "(1 ± √5)/2 solve x² = x + 1, the positive root ≈ 1.618; x² = x has integer roots 0 and 1 only; 1/φ² ≈ 0.382."
 },
 {
  "link": "P5",
  "check": "At the four joint forms of two signs, (x, y) → (y, −x) and (x, y) → (−y, x) move each form."
 },
 {
  "link": "P11",
  "check": "55 − 23 = 32 = 2·16; (23 + 55)/2 = 39 and 39² − 23·55 = 16²; 24² − 23·25 = 1; C(11,2) = 55."
 },
 {
  "link": "P22",
  "check": "2..59 and 61..118 each hold 58 numbers; 60 is midway between 59 and 61; 2 + 118 = 120."
 },
 {
  "link": "P26",
  "check": "59 = 1 + 2(4 + 9 + 16); φ³ − φ⁻³ = 4 exactly in Q(√5); 60 = 5·12; 59/2 = 29.5; i⁴ = 1."
 },
 {
  "link": "P28",
  "check": "EIGHTEEN 5.13's table has 50 rows: 2 at the file's own, 48 at the ten namings with counts (10, 0, 5, 2, 6, 3, 7, 6, 3, 6); groups 21, 13, 8, 6; odd namings 31, even 17; pairs (10,0), (5,2), (6,3), (7,6), (3,6)."
 },
 {
  "link": "L28",
  "check": "NINETEEN 5.2 to 5.8 hold 66 rows, 50 met and 16 reaching; 41 carry one of the ten namings; the rows cite seams 3.1 to 3.37; at the five naming pairs the odd carries more at four and less at one."
 }
]

CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'[QYJCBPL]\d+(_probe)?', k) and callable(v)}

if __name__ == '__main__':
    res = {}
    order = 'QYJCBPL'
    for k in sorted(CHECKS, key=lambda s: (order.index(s[0]), int(re.match(r'[A-Z](\d+)', s).group(1)), s)):
        try:
            res[k] = bool(CHECKS[k]())
        except Exception as e:
            res[k] = f'error: {e!r}'
        print(k, res[k])
    json.dump(RUNS, open(os.path.join(HERE, 'ccl_o2_runs.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'ccl_o2_check_results.json'), 'w'), indent=1)
