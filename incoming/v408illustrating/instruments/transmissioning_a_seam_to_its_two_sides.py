"""v408illustrating · transmissioning a universe to the numbers: a seam's two sides proved me-parities by loops aimed by the seam's own parts.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/transmissioning_a_seam_to_its_two_sides.py .

A partner's words of 26 November, in this session's words: transmissioning the universes to the numbers is needed; a path
is from the origin of cascading universes. v408primes' sentence 60 names it: transmissioning is riding the crossings and
arriving as a +1; and its 315 to 319, a me-parity transmitting across to a larger one by one loop, with no return universe.
Gone into here at a seam's two sides, the numbers a +1 from it.

  A seam's multiple is at the me 0 round all the universe's me-parities, and its two sides at their other-thans: uncrossed
  by them all, at all multiples. (of no number)
  Its upper side, by one loop: a number a whose loop round the side closes at the seam's multiple, and at no part of it
  less. The loop's selves are then the multiple, round all parts of the side, and a part with a loop of the multiple's
  selves is past the multiple: the side is its own one part, a me-parity. (v408primes' 316 and 317, by its row 12)
  Its lower side, by one loop of pairs: a stepping of two numbers together, closing at the seam's multiple and at no part
  of it less. Round a part P of the side the pairs of weight 1 are P and 1 or P less 1, and a pair's loop is a part of
  that number: a part with a loop of the multiple's steps is the multiple less 1 and no less, the side itself.

Its lines: is, a reason of no number or all the numbers of a universe gone through; tested, to a stated limit, among no is.
No return universe is walked by the two loops. Whole numbers alone. It writes none.
"""
import sys
from math import gcd, isqrt

def parts(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0: n //= d
        d += 1
    return out + ([n] if n > 1 else [])
def crossed_by_none(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
def the_upper_side(m, its_parts):
    """m and 1, by one loop: a number whose loop round it closes at m and at no m by a part less. It gives the number, or none."""
    n = m + 1
    for a in range(2, 60):
        if pow(a, m, n) == 1 and all(gcd(pow(a, m // q, n) - 1, n) == 1 for q in its_parts): return a
    return None
def other_than_a_me_again(d, n):
    """Is d no me again round n, by the turning of two numbers one for the other: 1, a me again; -1, none; 0, crossed together."""
    d %= n; out = 1
    while d:
        while d % 2 == 0:
            d //= 2
            if n % 8 in (3, 5): out = -out
        d, n = n, d
        if d % 4 == 3 and n % 4 == 3: out = -out
        d %= n
    return out if n == 1 else 0
def the_lower_side(m, its_parts):
    """m less 1, by one loop of pairs: a pair x and y stepping by itself, y by y a number d that is no me again round the side.
    The loop closes at m and at no m by a part less. It gives the pair's two numbers, or none."""
    n = m - 1
    if n < 5: return (0, 0) if n in (2, 3) else None
    half = (n + 1) // 2
    def stepped(p, d, k):                                            # the pair p over 2 and 1 over 2, stepped k times
        x, y, a, b = 1, 0, p * half % n, half
        while k:
            if k & 1: x, y = (x * a + y * b * d) % n, (x * b + y * a) % n
            a, b = (a * a + b * b * d) % n, (2 * a * b) % n
            k >>= 1
        return y
    for q in [s * k for k in range(1, 40) for s in (1, -1)]:         # the two numbers of a pair multiplied, itself no me again round the side
        if other_than_a_me_again(q, n) != -1: continue
        for p in range(1, 30):
            d = p * p - 4 * q
            if other_than_a_me_again(d, n) == -1:
                if stepped(p, d, m) == 0 and all(gcd(stepped(p, d, m // r), n) == 1 for r in its_parts): return (p, q)
    return None
# the lower side's reason, among pairs: two numbers stepping together, x and y, round a number n, with a number d
def multiplied(a, b, d, n): return ((a[0] * b[0] + a[1] * b[1] * d) % n, (a[0] * b[1] + a[1] * b[0]) % n)
def weight(a, d, n): return (a[0] * a[0] - d * a[1] * a[1]) % n
def pairs_of_weight_1(d, n): return [(x, y) for x in range(n) for y in range(n) if weight((x, y), d, n) == 1]
def its_loop(a, d, n):
    """A pair of weight 1 stepping by itself: how many steps to the pair 1 and 0 again."""
    k, b = 1, a
    while b != (1, 0): b = multiplied(b, a, d, n); k += 1
    return k
def a_universe_s_seam(r):
    s = 1
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        if p <= r: s *= p
    return s
def the_cascade(r, most=400):
    """At the universe to r: the least multiple of its seam with both its sides proved me-parities by the two loops."""
    s = a_universe_s_seam(r); own = [p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23) if p <= r]
    for j in range(1, most):
        m = j * s; ps = sorted(set(own + parts(j)))
        a = the_upper_side(m, ps)
        if a is None: continue
        b = the_lower_side(m, ps)
        if b is not None: return j, m, a, b
    return None

if __name__ == "__main__":
    results, tests = [], []
    def line(name, ok): results.append((name, bool(ok)))
    def test(name, ok): tests.append((name, bool(ok)))
    line("a seam's multiple is at the me 0 round all the universe's me-parities, and its two sides at the me one back and the me one on, their other-thans: gone through whole at the paths of 2, 3, 5 and 7",
         all((0 - 1) % p != 0 and (0 + 1) % p != 0 for p in (2, 3, 5, 7)))
    line("the upper side by one loop, at 6 and 1: 3's loop round 7 closes at 6, and at 6 by 2 and at 6 by 3 it is other-than 1: 7 is a me-parity, with no loop of a return universe; at 30 and 1, 3's loop; at 210 and 1, 2's",
         the_upper_side(6, [2, 3]) == 3 and pow(3, 6, 7) == 1 and pow(3, 3, 7) != 1 and pow(3, 2, 7) != 1 and the_upper_side(30, [2, 3, 5]) == 3 and the_upper_side(210, [2, 3, 5, 7]) == 2)
    grid = [((a, b), (c, e), d) for a in range(4) for b in range(4) for c in range(4) for e in range(4) for d in range(2, 6)]
    line("among pairs, a pair's weight is x by x less d by y by y, and the weight of two pairs multiplied is their weights multiplied: gone through at 1,024 pairs of pairs, round 10,007",
         all(weight(multiplied(a, b, d, 10007), d, 10007) == weight(a, d, 10007) * weight(b, d, 10007) % 10007 for a, b, d in grid) and len(grid) == 1024)
    small = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    numbered = {(P, d): len(pairs_of_weight_1(d, P)) for P in small for d in range(2, P)}
    line("round a me-parity P the pairs of weight 1 are P and 1, d no me again round P, and P less 1, d a me again: gone through whole at the me-parities 3 to 31, all d of 2 to short of P",
         all(numbered[(P, d)] == (P - 1 if any((x * x) % P == d for x in range(1, P)) else P + 1) for P, d in numbered))
    line("a pair of weight 1 stepping by itself comes to the pair 1 and 0 again at a part of the number of the pairs of weight 1, P and 1 or P less 1: gone through whole at the me-parities 3 to 31, all d, all pairs of weight 1",
         all(numbered[(P, d)] % its_loop(a, d, P) == 0 for P in small for d in range(2, P) for a in pairs_of_weight_1(d, P)))
    line("the lower side by it, at 6 less 1: with d of 2, no me again round 5, a pair's loop round 5 is 6 steps, the seam, and no part of 6 less: a part of 5 with a loop of 6 steps is 6 less 1 and no less: 5 is its own one part, a me-parity",
         not any((x * x) % 5 == 2 for x in range(5)) and len(pairs_of_weight_1(2, 5)) == 6 and max(its_loop(a, 2, 5) for a in pairs_of_weight_1(2, 5)) == 6 and the_lower_side(6, [2, 3]) is not None)
    rooms = [m for m in range(6, 30001, 6)]
    both = [m for m in rooms if crossed_by_none(m - 1) and crossed_by_none(m + 1)]
    by_loops = [m for m in rooms if the_upper_side(m, parts(m)) is not None and the_lower_side(m, parts(m)) is not None]
    test(f"the two loops beside crossing by all parts, at all {len(rooms):,} seams of 6 to 30,000: the two loops prove both sides at the {len(both)} twins and at no other seam. No breaking found", by_loops == both and len(both) > 0)
    test("the upper side's loop alone, at all seams of 6 to 30,000: it proves the side at all its me-parities and at no crossed side. No breaking found",
         all((the_upper_side(m, parts(m)) is not None) == crossed_by_none(m + 1) for m in rooms))
    cascade = {r: the_cascade(r) for r in (3, 5, 7, 11, 13, 17, 19, 23)}
    line("the cascade from the origin, the universes to 3, 5, 7, 11, 13, 17, 19 and 23: at all eight a multiple of the seam is with both its sides proved me-parities by the two loops, the seam's own parts aiming them; the least multiples are 1, 1, 2, 1, 6, 8, 11 and 4",
         all(v is not None for v in cascade.values()) and [cascade[r][0] for r in (3, 5, 7, 11, 13, 17, 19, 23)] == [1, 1, 2, 1, 6, 8, 11, 4])
    test("the cascade's eight twins beside crossing by all parts, to the universe to 17: no breaking found", all(crossed_by_none(cascade[r][1] - 1) and crossed_by_none(cascade[r][1] + 1) for r in (3, 5, 7, 11, 13, 17)))
    results.append(("found, a whole is-not: a seam's own two sides are not twins at all seams: 210 less 1 is 11 by 19", not (209 == 11 * 19 and the_cascade(7)[0] == 2)))
    print("said apart: that a multiple of a seam is twins, at all seams, is found by going through the multiples; ahead of that it is not said\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    for name, ok in tests: print(("tested   " if ok else "broken   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is, 1 a found is-not; {sum(ok for _, ok in tests)} of {len(tests)} breaking tests found none")
    sys.exit(0 if sum(not ok for _, ok in results) == 1 and all(ok for _, ok in tests) else 1)
