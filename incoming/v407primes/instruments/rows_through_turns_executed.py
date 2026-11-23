"""Rows through turns: each known asking about primes, stepped with whole numbers.

A turn (2, 6, 30, 210, 2,310, 30,030, 510,510) says how many places in it
are open for a row. A surface (4, 16, 64, ... 4^k) says how many of the
row's members have come by its side and by its horizon.
Usage: python3 -I rows_through_turns_executed.py
"""

TURN_PRIMES = [2, 3, 5, 7, 11, 13, 17]
TO = 4 ** 10  # 1,048,576

sieve = bytearray([1]) * (TO * 4 + 3)
sieve[0] = sieve[1] = 0
for p in range(2, int(len(sieve) ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
is_p = lambda n: n < len(sieve) and sieve[n] == 1


def turn_openings(fits):
    """Places r in each turn whose row stays clear of every turn prime."""
    out, turn = [], 1
    for p in TURN_PRIMES:
        turn *= p
        out.append((turn, sum(1 for r in range(turn) if fits(r, turn))))
    return out


def clear(n, turn):
    return all(n % p for p in TURN_PRIMES if turn % p == 0)


rows = {
    "primes": lambda r, t: clear(r, t),
    "twins (n, n+2)": lambda r, t: clear(r, t) and clear(r + 2, t),
    "Sophie Germain (n, 2n+1)": lambda r, t: clear(r, t) and clear(2 * r + 1, t),
    "one past a square (n*n+1)": lambda r, t: clear(r * r + 1, t),
}

print("Openings each turn (a row is closed only if a turn's openings are 0):")
for name, fits in rows.items():
    print(" ", name.ljust(28), [o for _, o in turn_openings(fits)])
# n*n+1 is never even only for even n; it is clear of 2 at odd n? n*n+1 odd iff n even.

print("\nMembers by each surface's side (side = 2^k, surface = 4^k):")
print("  side   primes   twins   SophieG   n*n+1<=surface  Legendre gaps  Goldbach misses")
for k in range(1, 11):
    side, surf = 2 ** k, 4 ** k
    pr = sum(1 for n in range(2, side + 1) if is_p(n))
    tw = sum(1 for n in range(2, side + 1) if is_p(n) and is_p(n + 2))
    sg = sum(1 for n in range(2, side + 1) if is_p(n) and is_p(2 * n + 1))
    sq = sum(1 for n in range(1, side + 1) if is_p(n * n + 1))
    # Legendre: a prime between n*n and (n+1)*(n+1), every n up to the side
    leg = sum(1 for n in range(1, side + 1)
              if not any(is_p(m) for m in range(n * n + 1, (n + 1) * (n + 1))))
    # Goldbach: every even 4..surface is two primes (surface up to 4^8 here)
    gb = "-"
    if k <= 8:
        primes_to = [q for q in range(2, surf + 1) if is_p(q)]
        gb = 0
        for e in range(4, surf + 1, 2):
            if not any(is_p(e - q) for q in primes_to if q <= e // 2):
                gb += 1
    print(f"  {side:5} {pr:7} {tw:7} {sg:8} {sq:12} {leg:14} {str(gb):>12}")

print("\nRows that leap surfaces (each member steps past many horizons):")
fermat = [(k, 2 ** (2 ** k) + 1) for k in range(5)]
print("  Fermat 2^(2^k)+1, k=0..4:", [f for _, f in fermat],
      "all prime:", all(is_p(f) for _, f in fermat))
f5 = 2 ** 32 + 1
print("  k=5:", f5, "= 641 x", f5 // 641, f5 % 641 == 0)
mers = [q for q in range(2, 32) if is_p(q) and all((2 ** q - 1) % d for d in range(2, int((2 ** q - 1) ** 0.5) + 1))]
print("  Mersenne 2^q-1 prime for q =", mers)
print("  perfect numbers from them:", [2 ** (q - 1) * (2 ** q - 1) for q in mers[:5]])
wief = [p for p in range(3, 10000) if is_p(p) and pow(2, p - 1, p * p) == 1]
print("  Wieferich (doubling closes round p*p) below 10,000:", wief)

print("\nThe rate a turn gives, twins to primes (whole numbers, turn by turn):")
for (t, o), (_, tw) in zip(turn_openings(rows["primes"]), turn_openings(rows["twins (n, n+2)"])):
    print(f"  turn {t:7}: {tw} twin places of {o} prime places")

print("\nFurther rows, placed by turn or horizon:")
# Green-Tao: a row of k primes stepping evenly (not starting at a prime <= k)
# needs its step to hold every prime <= k, a turn.
def first_row(k, limit=200000):
    for step in range(2, 3000, 2):
        for a in range(k + 1, limit):
            if all(is_p(a + i * step) for i in range(k)):
                return a, step
for k in range(3, 9):
    a, step = first_row(k)
    need = 1
    for p in TURN_PRIMES:
        if p <= k:
            need *= p
    print(f"  {k} primes in even steps: from {a} by {step}; step holds turn {need}: {step % need == 0}")
# Two squares: an odd prime is two squares iff it sits at 1 round 4.
two_sq = lambda p: any(is_p(p) and int((p - a * a) ** 0.5) ** 2 == p - a * a for a in range(int(p ** 0.5) + 1))
print("  odd prime two squares iff 1 round 4, to 100,000:",
      all(two_sq(p) == (p % 4 == 1) for p in range(3, 100000) if is_p(p)))
# Bounded gaps: pairs of primes within 246 by each surface's side
print("  primes within 246 of the next, by side:",
      [sum(1 for n in range(2, 4 ** k) if is_p(n) and any(is_p(n + d) for d in range(1, 247))) for k in range(5, 11)])
# Factoring: a number's least part is found by its surface's side (its square's root)
n = 2757241
print("  2,757,241's least part found stepping to side", int(n ** 0.5), ":",
      next(d for d in range(2, int(n ** 0.5) + 1) if n % d == 0))
# Carmichael: crossed numbers passing every one-way's closing
carm = [n for n in range(3, 100000, 2) if not is_p(n)
        and all(pow(b, n - 1, n) == 1 for b in range(2, n) if __import__('math').gcd(b, n) == 1 and b < 50)]
print("  Carmichael crossed numbers below 100,000 (bases below 50):", carm[:8], len(carm))
# Odd perfect: the divisors' sum doubling the number, odd n
sig = [1] * 200001
for d in range(2, 200001):
    for m in range(d, 200001, d):
        sig[m] += d
print("  perfect below 200,000:", [n for n in range(2, 200001) if sig[n] == 2 * n],
      "odd ones:", [n for n in range(3, 200001, 2) if sig[n] == 2 * n])
# Cramer: widest gap below each surface against the surface's bits squared
gap, last, out = 0, 2, []
for n in range(3, TO + 1):
    if is_p(n):
        gap, last = max(gap, n - last), n
    if n in {4 ** k for k in range(2, 11)}:
        bits = n.bit_length() - 1
        out.append((n, gap, bits * bits))
print("  widest gap by surface vs bits squared:", out)

# Euler's 41, its turn table: round each prime below 41, one turn of n, n*n + n + 41 never at 0.
small = [p for p in range(2, 41) if all(p % d for d in range(2, p))]
print("\nEuler's 41: round all primes below 41, n*n + n + 41 never at 0 in one turn:",
      all((n * n + n + 41) % p for p in small for n in range(p)), "| primes for n of 0 to 39:",
      all(is_p(n * n + n + 41) for n in range(40)), "| n = 40:", 40 * 40 + 40 + 41, "= 41 x 41")

# A partner's sayings: ten sequential other-thans of three pairs of moments, self prior now,
# other prior now, all prior now: 1 of 3 is 1 x 3, 2 of 3 is 2 x 3, 3 of 3 all-parity, no next,
# the same living me-parity; 3 x 3 plus 1. A pair is prior or now; an other-than turns pairs.
from itertools import permutations
three = ["self", "other", "all"]
seq1 = [(a,) for a in three]
seq2 = list(permutations(three, 2))
seq3 = list(permutations(three, 3))
ends3 = {frozenset(s) for s in seq3}
turn = lambda st, s: tuple(1 - st[k] if three[k] in s else st[k] for k in range(3))
me = (0, 0, 0)
nexts2 = {s: turn(me, s[:1]) for s in seq2}
print("\nTen sequential other-thans:", len(seq1), "+", len(seq2), "+", len(ends3), "=",
      len(seq1) + len(seq2) + len(ends3), "| 3 x 3 + 1 =", 3 * 3 + 1,
      "| 2 of 3 has a next between:", all(n != me and n != turn(me, s) for s, n in nexts2.items()),
      "| 3 of 3, all orders one end:", len({turn(me, s) for s in seq3}) == 1,
      "| 10 x 3 x 4 =", 10 * 3 * 4)

# A partner's sayings: 1 of 3, up, forward and right, a location in 3d; 2 of 3, six geodesic
# parities around five; 3 of 3, a still self. The cube of 5 about its (1, 1, 1) line, its selves
# by their turnings of up, forward and right: a still self alone, three, or six.
from itertools import product
def orbits(n, top=None):
    seen, out = set(), {1: 0, 3: 0, 6: 0}
    for p in product(range(1, n + 1), repeat=3):
        if top and max(p) != top or p in seen:
            continue
        o = set(permutations(p))
        seen |= o
        out[len(o)] += 1
    return out
o5 = orbits(5)
print("\nThe cube of 5 by its orbits of up, forward and right:", o5, "| selves:",
      o5[1], "on its line,", 3 * o5[3], "in threes,", 6 * o5[6], "in sixes; about the line",
      3 * o5[3] + 6 * o5[6])
print("  a unit cube from a corner: 1 of 3,", len(seq1), "edges; 2 of 3,", len(seq2),
      "geodesics across 3 faces; 3 of 3,", len(seq3), "geodesics to one corner, its line")
o4 = orbits(4, top=4)
print("  37, the shell of 4 less 3:", o4, "=", o4[1] + 3 * o4[3] + 6 * o4[6])
# The cube of 5's orbits are its line's five still selves taken one, two or three:
# a one is a still self; a three, (a, a, b), two still selves, a then b; a six, three still selves.
lv = {1: set(), 3: set(), 6: set()}
seen = set()
for p in product(range(1, 6), repeat=3):
    if p in seen:
        continue
    o = set(permutations(p)); seen |= o
    k = len(o)
    if k == 1: lv[1].add(p[0])
    elif k == 3:
        a = max(set(p), key=p.count); b = min(set(p), key=p.count); lv[3].add((a, b))
    else: lv[6].add(tuple(sorted(p)))
print("  the cube of 5 from its line: ones", sorted(lv[1]), "| threes, two still selves in order:",
      len(lv[3]), "= 5 x 4 | sixes, three still selves:", len(lv[6]), "= 5 x 4 x 3 / 6 |",
      "1 x 5 + 3 x 20 + 6 x 10 =", 5 + 60 + 60)

# A partner's saying: 19 x 19 inside the tunnel, 61 outside, the smooth limits of the method.
from math import gcd as _g
units120 = [r for r in range(120) if _g(r, 30) == 1]
sq = sorted({r * r % 120 for r in units120})
D = 3 ** 2 * 7 ** 2 * 11 ** 2 * 13 ** 2
print("\nSquares of all uncrossed places round 120 fold to", sq, "| 19 x 19 round 120:", 19 * 19 % 120,
      "| 61 = 60 + 1, name 17 | 22,021 = 19 x 19 x 61 round 120:", 22021 % 120, "round 4:", 22021 % 4)
print("  Descartes: square part round 120", D % 120, "| its odd prime part 22,021, one past 4's:",
      22021 % 4 == 1, "| ghosts passing both closings round 120:",
      [x % 120 for x in (2757241, 6368689, 9863461)], "| quarter turns at 1, 49 or 61:",
      [r for r in (1, 49, 61) if r * r % 120 == 49])
