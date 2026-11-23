#!/usr/bin/env python3
"""The prime numbers story, executed: each sentence of the story that numbers can execute.

Usage:  python3 -I incoming/v407primes/instruments/the_prime_numbers_story_executed.py .

With whole numbers alone, by a partner's word of 23 November: no smooth curve, no logarithm and
no decimal measuring. The numbers here are crossed by numbers' own dividing. v406Reiman's
`primes_on_the_resolvers_surface.py` finds the same uncrossed numbers, to 3,720, with Exhibit ONE
Natural Resolver's code as it is. Nothing is proved: a line here says is of the numbers it stepped.

It writes its lines to standard output. It writes no file, reaches no network and decides nothing.
"""
import random
import re
import sys
from math import isqrt, prod
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "v406Reiman" / "instruments"))
from resolver_as_it_is import moments_again, opening, resolver, spiral_couplings, exhibit_spiral_priors  # noqa: E402

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


def ladder_fold(text):
    m = re.search(r"- \*\*24\*\*\n(.*?)(?=\n- \*\*\d+\*\*|\n\n)", text, re.S)
    return bool(m) and "the fold" in m.group(1)


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

    # A partner's 120, bothboth: by Exhibit ONE Natural Resolver's code as it is.
    names, _ = resolver(sys.argv[1] if len(sys.argv) > 1 else ".")
    step = names["_17_next_existing"]
    again = lambda n, pri: moments_again(step, opening(range(n), pri), spiral_couplings(n))[1]
    line(36, "a self alone, by the living code, comes again with 4 moments: the quarter turn's four", again(1, {0: 1}) == 4)
    random.seed(23)
    from itertools import product as all_openings
    def by_its_span(pat):
        n = len(pat)
        for h in range(1, n, 2):
            if n % (2 * h) == 0 and all(pat[(i + h) % n] == -pat[i] for i in range(n)):
                return 2 * h
        d = next(d for d in range(1, n + 1) if n % d == 0 and all(pat[i] == pat[(i + d) % n] for i in range(n)))
        return 4 * d if d % 2 else 2 * d
    ok = all(again(n, dict(enumerate(pat))) == by_its_span(pat) for n in range(1, 11) for pat in all_openings((1, -1), repeat=n))
    line(37, "said again: by the living code a spiral comes again with its opening's own span, four times an odd span, twice an even span, "
             "and twice an odd span its opening inverts after: all 2,046 openings of 1 to 10 selves", ok)
    c = {**{(("a", i), 9): ("a", (i + 1) % 15) for i in range(15)}, **{(("b", i), 9): ("b", (i + 1) % 4) for i in range(4)}}
    pri = {**{("a", i): (-1 if i % 2 == 0 else 1) for i in range(15)}, **{("b", i): v for i, v in enumerate((1, 1, -1, 1))}}
    line(38, "a partner's 120: a spiral of 60 selves comes again with 120 moments, and a spiral of 15 beside a spiral of 4, one society, with 120",
         again(60, {i: random.choice((1, -1)) for i in range(60)}) == 120 and moments_again(step, opening(list(pri), pri), c)[1] == 120)
    line(39, "numbers' own quarter turn: five's doubling 2, 4, 3, 1, and ten's 3, 9, 7, 1, two quarter turns one short of five and of ten",
         [pow(2, k, 5) for k in range(1, 5)] == [2, 4, 3, 1] and [pow(3, k, 10) for k in range(1, 5)] == [3, 9, 7, 1])
    U = [r for r in range(1, 120) if r % 2 and r % 3 and r % 5]
    flips, quarters = [r for r in U if r * r % 120 == 1], [r for r in U if r * r % 120 == 49]
    line(40, "in 120 the uncrossed numbers are two pieces of 16, squared 1 or 49, and four quarter turns close all",
         len(flips) == len(quarters) == 16 and all(pow(r, 4, 240) == 1 for r in U))
    line(41, "a prime ending in 1 or 9 is a flip, and ending in 3 or 7 a quarter turn, primes 7 to 1,000,000",
         all((p * p % 120 == 1) == (p % 10 in (1, 9)) for p in PRIMES[3:]))
    line(42, "a quarter turn, 7, lays the flips onto the quarter turns, and two lay them back: the two pieces lock",
         sorted(7 * r % 120 for r in flips) == quarters and sorted(49 * r % 120 for r in flips) == flips)
    from math import gcd
    def closes_all(m, k):
        return all(pow(x, k, m) == 1 for x in range(1, m) if gcd(x, m) == 1)
    line(43, "two multiplyings close all uncrossed numbers with 24 at the widest, and four with 240",
         max(m for m in range(2, 2000) if closes_all(m, 2)) == 24 and max(m for m in range(2, 2000) if closes_all(m, 4)) == 240)

    def doubling_lengths(n):
        seen, lengths = set(), set()
        for i in range(1, n):
            if i not in seen:
                j, k = i, 0
                while j not in seen:
                    seen.add(j)
                    j, k = 2 * j % n, k + 1
                lengths.add(k if j == i else -1)
        return lengths
    ok = all(len(doubling_lengths(p)) == 1 and (p - 1) % next(iter(doubling_lengths(p))) == 0 for p in PRIMES[1:] if p < 10_000)
    lying = [n for n in range(9, 10_001, 2) if not prime(n) and len(doubling_lengths(n)) == 1]
    stepped = True
    random.seed(5)
    for q, length in ((7, 3), (11, 10), (13, 12), (23, 11)):
        cq = {(i, 9): 2 * i % q for i in range(q)}
        a = moments_again(step, opening(range(q), {i: random.choice((1, -1)) for i in range(q)}), cq)[1]
        stepped = stepped and a == (4 * length if length % 2 else 2 * length)
    ok = ok and stepped
    line(44, f"doubling as couplings round a prime steps spirals of one length, one short of the prime a whole number of them, primes to 10,000, and the living code steps them with no line multiplying, round 7, 11, 13 and 23; "
             f"crossed numbers with one length to 10,000: {lying}", ok and lying == [2047, 3277, 4033, 8321])

    def phi_closing(n):
        x, y, k = 0, 1, 0
        while True:
            x, y, k = y, (x + y) % n, k + 1
            if (x, y) == (0, 1):
                return k
    def phis_piece(n):
        return (n - 1) % phi_closing(n) == 0 if n % 10 in (1, 9) else (2 * (n + 1)) % phi_closing(n) == 0
    line(45, "phi's pair step on a torus round a prime closes by one short of it as a flip, and by twice one past it as a quarter turn, primes 7 to 20,000",
         all(phis_piece(p) for p in PRIMES[3:] if p < 20_000))
    from math import lcm
    def closing_of(q):
        x, y, k = 0, 1, 0
        while True:
            x, y, k = y, (x + y) % q, k + 1
            if (x, y) == (0, 1):
                return k
    def ord2(q):
        k, x = 1, 2 % q
        while x != 1:
            x, k = x * 2 % q, k + 1
        return k
    breaks = {2757241: (461, 5981), 6368689: (1129, 5641), 9863461: (2221, 4441)}
    ok = all(a * b == n and prime(a) and prime(b) and ord2(a) == ord2(b) and pow(2, n - 1, n) == 1 and n % 10 in (1, 9)
             and (n - 1) % lcm(closing_of(a), closing_of(b)) == 0 for n, (a, b) in breaks.items())
    quarter = [n for n in range(9, TO, 2) if n % 10 in (3, 7) and not prime(n) and pow(2, n - 1, n) == 1 and phis_piece(n)]
    line(46, f"said again: crossed flips with doubling's one length and phi's closing of their piece, {sorted(breaks)}; "
             f"a crossed quarter turn closing by doubling and by phi's piece, to 1,000,000: {quarter}", ok and quarter == [])

    from math import lcm
    random.seed(45)
    def phis_torus(n):
        sel = [(x, y) for x in range(n) for y in range(n)]
        cn = {((x, y), 9): (y, (x + y) % n) for x, y in sel}
        return moments_again(step, opening(sel, {v: random.choice((1, -1)) for v in sel}), cn, most=5000)[1]
    tori = {n: phis_torus(n) for n in (3, 5, 7, 9, 11, 13, 15, 19, 21)}
    pieces = lambda n: 2 * (n - 1) if n % 10 in (1, 9) else 4 * (n + 1)
    ok = all(tori[n] == 2 * phi_closing(n) and pieces(n) % tori[n] == 0 for n in (7, 11, 13, 19))
    ok = ok and all(pieces(n) % tori[n] for n in (9, 21))
    line(47, "phi's couplings on a torus of n by n selves, stepped by the living code, come again with twice phi's closing, "
             "a prime's piece's closing a whole number of it round 7, 11, 13 and 19, and not round 9 and 21", ok)
    line(48, "a crossed number's torus is its parts' tori side by side, 15 and 21, and a prime's torus parts into none",
         tori[15] == lcm(tori[3], tori[5]) and tori[21] == lcm(tori[3], tori[7]))

    import glob
    import re
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    soc = open(glob.glob(str(Path(root) / "Exhibit_SEVEN_Natural_Societies_*.md"))[0], encoding="utf-8").read()
    ladder = {}
    for q in range(5, 60):
        m = re.search(r"- \*\*%d\*\*\n(.*?)(?=\n- \*\*\d+\*\*|\n\n)" % q, soc, re.S)
        if m and prime(q):
            ladder[q] = [x.strip()[6:] for x in m.group(1).strip().split("\n")]
    living = [q for q in ladder if q >= 7]
    pairs = [(q, 60 - q) for q in living if q < 30]
    ok = living == [q for q in range(7, 59) if prime(q)]
    ok = ok and all({ladder[a][0], ladder[b][0]} == {"before", "after"} for a, b in pairs if b in ladder)
    ok = ok and [a for a, b in pairs if b not in ladder] == [11] and ladder[23][1] == "cell" and ladder[37][1] == "organism"
    ok = ok and ladder[29][1] == "tissue" and ladder[31][1] == "organ" and ladder[5][1] == "atom"
    line(53, "Natural Societies' living prime scales, 7 to 53, are the section of 60 flipped about 30: six podal pairs, one before six and one after, "
             "and 11 alone, its pair 49; cell 23 with organism 37, tissue 29 with organ 31", ok)

    U24 = [q for q in range(1, 24) if q % 2 and q % 3]
    line(54, "at the fold, 24, all its uncrossed numbers are their own podal by multiplying, 1, 5, 7, 11, 13, 17, 19 and 23",
         all(q * q % 24 == 1 for q in U24) and ladder_fold(soc))
    line(55, "23, 22, 21, 20 and 19 are 24 less a self's five, 1 to 5: 19 and 23 living scales, and 20, 21 and 22 crossed",
         [24 - k for k in range(1, 6)] == [23, 22, 21, 20, 19] and prime(19) and prime(23) and not any(prime(n) for n in (20, 21, 22)))
    named = {1: ("after", "the origin"), **{q: (ladder[q][0], ladder[q][1]) for q in ladder}}
    ok = all({named[a][0], named[24 - a][0]} == {"before", "after"} for a in (1, 5, 7, 11))
    ok = ok and [(named[a][1], named[24 - a][1]) for a in (1, 5, 7, 11)] == [
        ("the origin", "cell"), ("atom", "organelle"), ("molecule", "gene"), ("macromolecule", "protein-fold")]
    line(56, "below the fold the scales are podal about it: the origin with cell, atom with organelle, molecule with gene, macromolecule with protein-fold, "
             "one before six and one after", ok)

    U120 = [q for q in range(120) if q % 2 and q % 3 and q % 5]
    line(60, "all primes past 5 to 1,000,000 are on the 32 places of 120, and all 32 places have primes",
         all(q % 120 in U120 for q in PRIMES[3:]) and all(any(prime(n) for n in range(q, TO, 120)) for q in U120))
    row = (0, 4, 6, 10, 12, 16, 22)
    allowed = [q for q in U120 if all((q + d) % 2 and (q + d) % 3 and (q + d) % 5 for d in row)]
    found = [n for n in range(2, TO - 22) if all(prime(n + d) for d in row)]
    line(61, f"the row {row}: the 120 leaves it uncrossed from {allowed[:3]} and more, and the spiral of 7 crosses one of its seven places from all starts; all primes once, from 7: {found}",
         len({d % 7 for d in row}) == 7 and allowed and found == [7])
    found5 = [n for n in range(2, TO - 18) if all(prime(n + d) for d in (0, 2, 6, 8, 12, 14, 18))]
    line(62, f"one scale before: the row 5 to 23 one short and one past six, the spiral of 5 crossing one of its seven from all starts; all primes once, from 5: {found5}",
         len({d % 5 for d in (0, 2, 6, 8, 12, 14, 18)}) == 5 and found5 == [5])
    line(63, "four quarter turns close all primes past 5 with 240, two 120s, and not with 480",
         all(pow(q, 4, 240) == 1 for q in PRIMES[3:]) and not all(pow(q, 4, 480) == 1 for q in PRIMES[3:]))

    rounds = [3 * k * (k + 1) + 1 for k in range(6)]
    line(73, "a self and rounds of six, 1, 7, 19, 37, 61: in the ladder 7 molecule, 19 organelle and 37 organism, 37 with three rounds, 1 + 6 + 12 + 18",
         [q for q in living if q in rounds] == [7, 19, 37] and ladder[7][1] == "molecule" and ladder[19][1] == "organelle" and ladder[37][1] == "organism")
    k = 3
    cells = {(a, b) for a in range(-k, k + 1) for b in range(-k, k + 1) if max(abs(a), abs(b), abs(a + b)) <= k}
    v1, v2 = (2 * k + 1, -k), (k, k + 1)
    def home(a, b):
        return [c for x in range(-4, 5) for y in range(-4, 5)
                for c in [(a - x * v1[0] - y * v2[0], b - x * v1[1] - y * v2[1])] if c in cells]
    near = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    ok = len(cells) == 37 and all(len(home(a, b)) == 1 for a in range(-12, 13) for b in range(-12, 13))
    ok = ok and all(len({home(a + da, b + db)[0] for da, db in near}) == 6 for a, b in cells)
    line(74, "the hexagon of 37 wraps into a torus with no seam, all 37 selves with six others about them: no self its centre more than another", ok)
    line(75, "37 is 4 cubed less 3 cubed, three faces of a cube of 4 about a corner, and 4 by 4 and 4 by 3 and 3 by 3 added",
         4 ** 3 - 3 ** 3 == 37 == 16 + 12 + 9)

    from itertools import product as cube_of
    def shell(n):
        out = {1: 0, 2: 0, 3: 0}
        for c in cube_of(range(n + 1), repeat=3):
            k = sum(1 for x in c if x == n)
            if k:
                out[k] += 1
        return out
    sh = shell(3)
    line(76, "4 cubed less 3 cubed, by how many ways a self is other-than the inner cube: once 27, twice 9, thrice 1; faces, edges and corner 48 - 12 + 1",
         sh == {1: 27, 2: 9, 3: 1} and 3 * 16 - 3 * 4 + 1 == 37)
    line(77, "37 is the one shell whose other-thans are its inner cube's own again, once its cube and twice its square, n of 1 to 10,000: n = 3",
         [n for n in range(1, 10_001) if 3 * n * n == n ** 3 and 3 * n == n * n] == [3] and all(shell(n)[1] != n ** 3 for n in (1, 2, 4, 5)))

    shell37 = [c for c in cube_of(range(4), repeat=3) if max(c) == 3]
    onto = {(x - y, y - z, z - x): (x, y, z) for x, y, z in shell37}
    by_round = {}
    for hx, c in onto.items():
        r_ = max(abs(v) for v in hx)
        by_round.setdefault(r_, {1: 0, 2: 0, 3: 0})[sum(1 for v in c if v == 3)] += 1
    line(80, "observed along (1, 1, 1) the 37 of the shell are the 37 of the hexagon one to one, the corner its centre; a round of it has three selves other-than twice, one on a way's line, and 3, 9 and 15 other-than once",
         len(onto) == 37 and onto[(0, 0, 0)] == (3, 3, 3) and by_round == {0: {1: 0, 2: 0, 3: 1}, 1: {1: 3, 2: 3, 3: 0}, 2: {1: 9, 2: 3, 3: 0}, 3: {1: 15, 2: 3, 3: 0}})
    def hex_torus(k):
        cl = sorted({(a, b) for a in range(-k, k + 1) for b in range(-k, k + 1) if max(abs(a), abs(b), abs(a + b)) <= k})
        w1, w2, cset = (2 * k + 1, -k), (k, k + 1), set(cl)
        def hm(a, b):
            return next(c for x in range(-4, 5) for y in range(-4, 5)
                        for c in [(a - x * w1[0] - y * w2[0], b - x * w1[1] - y * w2[1])] if c in cset)
        return cl, {**{((a, b), 9): hm(a + 1, b) for a, b in cl}, **{((a, b), 10): hm(a, b + 1) for a, b in cl}}
    from itertools import product as openings_of
    cl7, ch7 = hex_torus(1)
    seven = {}
    for pat in openings_of((1, -1), repeat=7):
        m7 = moments_again(step, opening(cl7, dict(zip(cl7, pat))), ch7)[1]
        seven[m7] = seven.get(m7, 0) + 1
    random.seed(80)
    found_ = {}
    for k, tries in ((2, 20), (3, 20)):
        cl, ch = hex_torus(k)
        found_[len(cl)] = {}
        for _ in range(tries):
            m_ = moments_again(step, opening(cl, {v: random.choice((1, -1)) for v in cl}), ch, most=4000)[1]
            found_[len(cl)][m_] = found_[len(cl)].get(m_, 0) + 1
    ok = seven == {4: 2, 7: 126} and set(found_[19]) <= {2, 76} and set(found_[37]) <= {2, 37, 148}
    ok = ok and max(found_[37], key=found_[37].get) == 37 and max(found_[19], key=found_[19].get) == 76
    line(81, f"the hexagon tori stepped by the living code, couplings 9 and 10 along two of its lines, from most openings: 7 and 37 come again with their own number of moments, 19 with four times its; "
             f"7, all 128 openings, {seven}; 19, {found_[19]}; 37, {found_[37]}", ok)

    print("All is, of the numbers stepped." if all_is else "Not all is.")
    return 0 if all_is else 1


if __name__ == "__main__":
    sys.exit(main())
