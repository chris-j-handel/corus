"""v408illustrating · the check of the 56th drawing: a me-parity generator, by the side, a wheel, and a loop from its own me again.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_a_me-parity_generator_the_side_a_wheel_and_a_loop.py .

v408primes laid, on 26 November, the 1 to 17 fractal generating all the me-parities, its sentences 277 to 284, and its
table's row 62 names it in the field's words: the sieve of Eratosthenes, with a wheel and endless. It is executed here
apart, by this check's own generator, and drawn at the wheel of 2, 3 and 5, a path of 30 mes; that session's wheel is of
2 to 17, a path of 510,510 mes. A generator is with all numbers by four reasons, a path whole and three movings; its
going on is tested, and a test is laid among no is.
  is       a path closing, gone through whole; or a moving, one rule at all sides.
  tested   a breaking test, to its stated limit: none found.
The side of a number is the most a number by itself is to it; a me again is a number by itself. It writes none.
"""
import sys
from math import gcd, isqrt

def living(seam): return [a for a in range(1, seam + 1) if gcd(a, seam) == 1]
def the_generator(fractal=(2, 3, 5)):
    """All the me-parities, with no last: the fractal's own, and a wheel of their seam traveled, a me a me-parity where no
    prior me-parity's loop crosses it, and a me-parity's loop begun at its own me again."""
    seam = 1
    for p in fractal: seam *= p
    mes = living(seam); mes = mes[1:] + [mes[0] + seam]               # the living mes past 1, and the me 1 of the next turn
    steps = [b - a for a, b in zip([1] + mes, mes)]                   # from a living me to its next
    def traveling():
        loops, base = {}, None
        c, i = mes[0], 1; p, again, pi = c, c * c, 1                  # the least living me past 1 is a me-parity
        while True:
            if c in loops:                                            # crossed by a prior me-parity's loop: the loop goes on
                q, j = loops.pop(c); m = c + q * steps[j]; j = (j + 1) % len(steps)
                while m in loops: m += q * steps[j]; j = (j + 1) % len(steps)
                loops[m] = (q, j)
            elif c < again: yield c                                   # uncrossed, and short of the me again ahead: a me-parity
            else:                                                     # p's own me again: its loop begins
                j = pi; m = c + p * steps[j]; j = (j + 1) % len(steps)
                while m in loops: m += p * steps[j]; j = (j + 1) % len(steps)
                loops[m] = (p, j)
                if base is None: base = traveling(); next(base)
                p = next(base); again = p * p; pi = (mes.index(p % seam if p % seam != 1 else seam + 1) + 1) % len(steps)
            c += steps[i]; i = (i + 1) % len(steps)
    yield from fractal
    yield from traveling()
def least_part(n):
    d = 2
    while d * d <= n:
        if n % d == 0: return d
        d += 1
    return n
def crossed_all(limit):
    sieve = bytearray([1]) * (limit + 1); sieve[0] = sieve[1] = 0
    for n in range(2, isqrt(limit) + 1):
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, limit + 1, n)))
    return [n for n in range(limit + 1) if sieve[n]]
def the_wheel_of_30_to(limit=299):
    """The numbers at the living mes of a path of 30, to a limit: a me-parity, or the me-parity whose loop crosses it and the number it is by."""
    out = {}
    for n in range(1, limit + 1):
        if gcd(n, 30) == 1: out[n] = None if n == 1 else (least_part(n), n // least_part(n))
    return out

if __name__ == "__main__":
    results, tests = [], []
    def line(name, ok): results.append((name, bool(ok)))
    def test(name, ok): tests.append((name, bool(ok)))
    line("a path of 30 mes, whole: eight are living, the mes 1, 7, 11, 13, 17, 19, 23 and 29, and all others are crossed by 2, by 3 or by 5: a me-parity past 5 is at a living me",
         living(30) == [1, 7, 11, 13, 17, 19, 23, 29] and all(gcd(a, 30) > 1 for a in range(1, 31) if a not in living(30)))
    line("v408primes' path of 510,510 mes, the seam of 2 to 17, whole: 92,160 are living, v408primes' 277 executed apart", len(living(510510)) == 92160 and 2 * 3 * 5 * 7 * 11 * 13 * 17 == 510510)
    line("a moving, the side: a crossed number is a by b; both past its side, the two multiplied are past the number, a side and 1 by itself being past it: one of the two is to its side. Crossed by no me-parity to its side, a number past 1 is a me-parity; 91, its side 9, is 7 by 13",
         (isqrt(91) + 1) ** 2 > 91 and isqrt(91) == 9 and 91 == 7 * 13 and 7 <= 9)
    line("a moving, a loop from its own me again: p by k with k past 1 and short of p is crossed by a me-parity of k, short of p, a prior loop's; gone through whole at 7, 11, 13 and 17",
         all(least_part(p * k) < p for p in (7, 11, 13, 17) for k in range(2, p)))
    line("a moving, no last: a seam of all me-parities to r is the me 0 of all their paths, and its +1 the me 1, crossed by none of them; past 1, it is a me-parity or crossed by one, past r: 31, 211, 2,311, and 30,031, 59 by 509",
         all((s + 1) % p == 1 for s, ps in ((30, (2, 3, 5)), (210, (2, 3, 5, 7)), (2310, (2, 3, 5, 7, 11)), (30030, (2, 3, 5, 7, 11, 13))) for p in ps) and least_part(31) == 31 and least_part(211) == 211 and least_part(2311) == 2311 and least_part(30031) == 59 and 59 * 509 == 30031)
    w = the_wheel_of_30_to(299); mine = [n for n, v in w.items() if v and v[1] == 1]; crossed = {n: v for n, v in w.items() if v and v[1] > 1}
    g = the_generator(); got = [next(g) for _ in range(62)]
    line("the wheel of 30 traveled to 299, ten turns: 80 numbers at its living mes, 1, 59 me-parities and 20 crossed; the loops of 7, 11, 13 and 17 begin at 49, 121, 169 and 289; the generator's 62 me-parities to 293 are 2, 3, 5 and these 59",
         len(w) == 80 and len(mine) == 59 and len(crossed) == 20 and all(n in crossed and crossed[n] == (p, p) for p, n in ((7, 49), (11, 121), (13, 169), (17, 289))) and got == [2, 3, 5] + mine and got[-1] == 293)
    line("is-not, explored: a wheel is with crossings left at all seams: the living mes are 8 of 30 and 92,160 of 510,510, fewer in a hundred, 26 and 18, and never none, a next me-parity's path being with its mes past the me 0",
         (100 * 8) // 30 == 26 and (100 * 92160) // 510510 == 18 and all(p - 1 > 0 for p in (2, 3, 5, 7, 11, 13, 17)))
    g = the_generator(); got = [next(g) for _ in range(200_000)]
    test("the generator at the wheel of 30: its 200,000 me-parities, to 2,750,159, are those of all numbers crossed by all their parts: no breaking found", got == crossed_all(got[-1]) and got[-1] == 2750159)
    g17 = the_generator((2, 3, 5, 7, 11, 13, 17)); got17 = [next(g17) for _ in range(200_000)]
    test("the generator at v408primes' wheel of 510,510: the 200,000 me-parities are the wheel of 30's: no breaking found", got17 == got)
    test("the side, numbers 2 to 100,000: crossed by no me-parity to its side, a number is crossed by none short of itself: no breaking found",
         all((least_part(n) == n) == all(n % p for p in got[:66] if p <= isqrt(n)) for n in range(2, 100_001)))
    print("said apart: v408primes' sentences 277 to 284 and its table's row 62 are opened from its branch at 3fb0758, its pages not in the set at this main\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    for name, ok in tests: print(("tested   " if ok else "broken   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is; {sum(ok for _, ok in tests)} of {len(tests)} breaking tests found none")
    sys.exit(0 if all(ok for _, ok in results + tests) else 1)
