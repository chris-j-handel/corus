#!/usr/bin/env python3
"""The prime numbers story, executed: each sentence of the story that numbers can execute.

Usage:  python3 -I incoming/v407primes/instruments/the_prime_numbers_story_executed.py

With whole numbers alone, by a partner's word of 23 November: no smooth curve, no logarithm and
no decimal measuring. The numbers here are crossed by numbers' own dividing. v406Reiman's
`primes_on_the_resolvers_surface.py` finds the same uncrossed numbers, to 3,720, with Exhibit ONE
Natural Resolver's code as it is. Nothing is proved: a line here says is of the numbers it stepped.

It writes its lines to standard output. It writes no file, reaches no network and decides nothing.
"""
import sys
from math import isqrt, prod

TO = 1_000_000
crossed = bytearray(TO + 1)
crossed[0] = crossed[1] = 1
for i in range(2, isqrt(TO) + 1):
    if not crossed[i]:
        crossed[i * i::i] = b"\x01" * len(crossed[i * i::i])


def prime(n):
    return 0 <= n <= TO and not crossed[n]


PRIMES = [n for n in range(2, TO + 1) if prime(n)]
all_is = True


def line(n, saying, ok):
    global all_is
    all_is = all_is and ok
    print(f"{n:>2}. {saying}: {'is' if ok else 'IS NOT'}")


def uncrossed_by(spirals):
    return lambda n: all(n % p for p in spirals)


def parts(n):
    found, p = [], 2
    while p * p <= n:
        while n % p == 0:
            found.append(p)
            n //= p
        p += 1
    return found + ([n] if n > 1 else [])


def main():
    # The staircase: one up at a prime, across at a crossed number.
    steps, up = [], 0
    for n in range(0, 61):
        up += prime(n)
        steps.append(up)
    line(5, "the staircase, one up at a prime and across at a crossed number, is 17 up at 60, and 25 at 100",
         steps[60] == 17 and sum(prime(n) for n in range(101)) == 25)

    # A turn: spirals side by side come again together.
    turns = [prod(PRIMES[:k]) for k in range(1, 6)]
    line(6, f"the spirals of 2 to 11 side by side come again together with turns of {turns[1:]} numbers, "
            f"and the odd spirals' living coming again, four times their product in moments, is {[4 * t // 2 for t in turns[1:]]}",
         turns[1:] == [6, 30, 210, 2310])

    # The flip: a turn's uncrossed numbers fit themselves upside down and backwards.
    ok = True
    for k in range(2, 6):
        t, member = turns[k - 1], uncrossed_by(PRIMES[:k])
        ok = ok and all(member(a + r) == member(a + t - r) for a in range(0, 40 * t, t) for r in range(1, t))
        ok = ok and not all(member(r) == member(t // 2 - r) for r in range(1, t // 2))
    line(7, "in a turn, the numbers its spirals leave uncrossed fit themselves flipped, a number with its number from the turn's other end, "
            "with turns of 6, 30, 210 and 2310, and with no shorter turn", ok)

    member, t = uncrossed_by((2, 3, 5)), 30
    total = sum(member(r) for r in range(1, t))
    ok = all(sum(member(a + i) for i in range(1, r + 1)) == total - sum(member(a + i) for i in range(1, t - r))
             for a in range(0, 30 * 200, 30) for r in range(1, t))
    line(8, "the staircase of a turn's uncrossed numbers, flipped upside down and backwards, is the same staircase, all 200 turns of 30 stepped", ok)

    off = [(r, 30 - r) for r in range(1, 15) if prime(r) != prime(30 - r)]
    off60 = [(r, 60 - r) for r in range(1, 30) if prime(r) != prime(60 - r)]
    line(9, f"the primes themselves fit flipped in the turn of 30 but the turn's own spirals and 1, {off}; in 60 also 11 with 49, 7 by 7, {off60[-1]}",
         off == [(1, 29), (2, 28), (3, 27), (5, 25)] and off60[-1] == (11, 49))

    # Six's rows.
    run, best, start = 0, (0, 0), 0
    for n in range(5, TO, 2):
        if n % 6 in (1, 5):
            if prime(n):
                start = n if run == 0 else start
                run += 1
                best = max(best, (run, start))
            else:
                run = 0
    line(10, f"one short and one past the multiples of six, the longest row all primes is 5 to 23, {best[0]} in a row, to {TO}", best == (7, 5))
    line(11, "a prime from 5 on, multiplied by its own, is one past a whole number of 24s, all primes to 1,000,000",
         all((p * p - 1) % 24 == 0 for p in PRIMES[2:]))

    # No last prime.
    ok, opened = True, []
    for k in range(1, 11):
        m = prod(PRIMES[:k]) + 1
        q = parts(m)[0]
        opened.append(q)
        ok = ok and q not in PRIMES[:k]
    line(12, f"the primes had, multiplied, with one added, is crossed by none of them: its least part is new, {opened}", ok)

    ok = all(sorted(parts(n)) == parts(n) and prod(parts(n)) == n for n in range(2, 20001))
    line(13, "a number is its primes multiplied, numbers of 2 to 20,000", ok)

    # Between primes.
    t = turns[2]
    member = uncrossed_by((2, 3, 5))
    uncr = [n for n in range(1, t + 2) if member(n)]
    gaps = [b - a for a, b in zip(uncr, uncr[1:])]
    line(14, f"in a turn of 30 the spacings of the uncrossed numbers are {gaps}, podal about its middle, and a 2 across to the next turn",
         gaps == [6, 4, 2, 4, 2, 4, 6, 2] and gaps[:7] == gaps[:7][::-1])
    m = prod(range(1, 11))
    line(15, "a row of crossed numbers is as long as asked: multiplying 1 to 10 and adding 2 to 10, all nine are crossed",
         all(n % k == 0 for k, n in ((k, m + k) for k in range(2, 11))))
    pairs = []
    for k in range(1, 5):
        tt, mm = turns[k], uncrossed_by(PRIMES[:k + 1])
        pairs.append(sum(1 for n in range(1, tt + 1) if mm(n) and mm(n + 2)))
    line(16, f"pairs two apart in a turn, its spirals' places less two, multiplied, never none: {pairs}", pairs == [1, 3, 15, 135])
    line(17, "between two squares of numbers one apart is a prime, squares to 1,000", all(any(prime(n) for n in range(k * k + 1, (k + 1) ** 2)) for k in range(1, 1000)))
    line(18, "between a number and its double is a prime, numbers of 2 to 500,000",
         all(any(prime(n) for n in range(k + 1, 2 * k)) for k in range(2, 30)) and
         all(b < 2 * a for a, b in zip(PRIMES, PRIMES[1:]) if a <= 500_000))
    ok = all(any(prime(h - d) and prime(h + d) for d in range(0, h - 1)) for h in range(2, 20001))
    line(19, "from all numbers of 2 to 20,000, a distance with both sides primes: an even number twice it is two primes added", ok)

    # Rows and closings.
    rows = [r for r in range(1, 30) if member(r)]
    line(20, f"all rows of a turn of 30 with no part of the turn, {rows}, have primes past 999,000",
         all(any(prime(n) for n in range(999_000 + r, TO, 30)) for r in rows))
    line(21, "doubling, round a prime above two, closes by one short of it, all primes to 1,000,000; 341 closes too, 11 by 31",
         all(pow(2, p - 1, p) == 1 for p in PRIMES[1:]) and pow(2, 340, 341) == 1 and parts(341) == [11, 31])
    squares = {a * a for a in range(1, 1001)}
    ok = all(any((p - a * a) in squares for a in range(1, isqrt(p) + 1)) == (p % 4 != 3) for p in PRIMES[1:] if p < 100_000)
    line(22, "a prime one past a multiple of four is two squares added, and one short of it never, primes to 100,000", ok)
    def lucas_lehmer(q):
        m, v = 2 ** q - 1, 4
        for _ in range(q - 2):
            v = (v * v - 2) % m
        return q == 2 or v == 0
    mer = [n for n in range(2, 128) if prime(n) and lucas_lehmer(n)]
    ok = all((2 ** n - 1) % (2 ** a - 1) == 0 for n in range(4, 128) if not prime(n) for a in [parts(n)[0]])
    ok = ok and mer == [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127] and 2 ** 11 - 1 == 23 * 89
    line(23, f"two multiplied by itself n times, one short, is crossed with n crossed, and a prime only with n a prime, n to 127: {mer}; with 11 it is 23 by 89", ok)
    ok = True
    for n in range(2, 3001):
        f = 1
        for k in range(2, n):
            f = f * k % n
        ok = ok and (((f + 1) % n == 0) == prime(n))
    line(24, "all numbers below a number multiplied, with one added, is a multiple of it only with it a prime, numbers to 3,000", ok)

    # A prime an inversion, and the lead.
    least = list(range(TO + 1))
    for i in range(2, isqrt(TO) + 1):
        if least[i] == i:
            for j in range(i * i, TO + 1, i):
                if least[j] == j:
                    least[j] = i
    parity = [0, 1] + [0] * (TO - 1)
    for n in range(2, TO + 1):
        parity[n] = -parity[n // least[n]]
    sq = {k * k for k in range(1, isqrt(20000) + 1)}
    ok = all(sum(parity[d] for d in range(1, n + 1) if n % d == 0) == (1 if n in sq else 0) for n in range(1, 2001))
    line(25, "a prime an inversion, a number's parts' parities come to a 0, all but a number multiplied by its own, numbers to 2,000", ok)
    lead, most, minus_lead = 0, 0, True
    for n in range(1, TO + 1):
        lead += parity[n]
        most = max(most, lead * lead * 9 // n) if n > 1 else most
        minus_lead = minus_lead and (lead <= 0 or n == 1)
    line(26, f"stepped to {TO:,}, the −s have the lead, and the lead multiplied by its own is short of twice the number: "
             f"the lead is of the square's side", minus_lead and most < 18)
    line(27, "Ulam's row n·n + n + 41 is at no seam of the spirals 2 to 37 with all n by one turn, and is all primes for n of 0 to 39",
         all(prime(n * n + n + 41) for n in range(40)) and not prime(40 * 40 + 40 + 41) and
         all((n * n + n + 41) % p for p in PRIMES[:12] for n in range(p)))

    line(28, "primes evenly apart, as many in a row as asked: seven, 7 to 907 by 150; ten, 199 to 2089 by 210",
         all(prime(7 + 150 * k) for k in range(7)) and all(prime(199 + 210 * k) for k in range(10)))

    print("All is, of the numbers stepped." if all_is else "Not all is.")
    return 0 if all_is else 1


if __name__ == "__main__":
    sys.exit(main())
