#!/usr/bin/env python3
"""The hypothesis's zeros and the living code's own 0s, both ways, and a zero's inversion.

Usage:  python3 -I incoming/v406me/instruments/the_zeros_and_the_living_codes_0s_both_ways.py LIVE

LIVE is a checkout of the set. A partner's saying of 22 November, of the one tie v406Reiman's primes
report has as not executed, from the zeros to the living code's own 0s: it is bothbothing, and its
inversions are natural torusing. Explored here by executing. Nothing is proved.

  1  The zeros' heights, from the hypothesis's function itself, to height 500, with no table.
  2  Out. The uncrossed numbers of 2 to 2,000, by Exhibit ONE Natural Resolver's code as it is, a
     number crossed with a smaller spiral's 0 at its seam with it, by v406Reiman's surface. Their
     turns added, and its highest peaks beside the lowest zeros.
  3  Back. The zeros' turns added, and its highest peaks beside the uncrossed numbers.
  4  A zero's inversion. A zero is a height the turns added come to nothing at; its inversion is a
     height they come together at. Those heights beside whole rounds of two, of three and of five,
     tori of whole selves, and beside the widest places with no zero.

A field has these already: the primes from the zeros and the zeros from the primes, by Riemann and
von Mangoldt; and the comings together beside equal parts of a doubling, in a field of tuning. A
turn and a prime's rate are numbers' own arithmetic here, a field's measurings, and no cell's.
This explaining's own beside them: the primes are the living code's own, and the reading of the
two tori as one, of whole selves stepping by adding and of rates in no ratio by multiplying.

It imports v406Reiman's instruments as they are. It writes no file and reaches no network.
"""
import cmath
import math
import sys
from fractions import Fraction
from pathlib import Path

TERMS, TOP, STEP = 560, 500.0, 0.05
A_FIELDS_SIX = (14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178)


def weights(n):
    term, d = Fraction(1), [Fraction(1)]
    for i in range(1, n + 1):
        term = term * 4 * (n + i - 1) * (n - i + 1) / ((2 * i) * (2 * i - 1))
        d.append(d[-1] + term)
    return [float((-1) ** k * (d[k] - d[n]) / d[n]) for k in range(n)]


W = weights(TERMS)
LN = [math.log(k + 1) for k in range(TERMS)]


def the_function(s):
    """The hypothesis's function, by its alternating adding, Borwein's weights."""
    return -sum(w * cmath.exp(-s * l) for w, l in zip(W, LN)) / (1 - 2 ** (1 - s))


def its_turn(t):
    return t / 2 * math.log(t / (2 * math.pi)) - t / 2 - math.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def on_its_row(t):
    """The function at the between of nought and one, at a height, turned to one side: a + or a -."""
    return (cmath.exp(1j * its_turn(t)) * the_function(complex(0.5, t))).real


def peaks(values, places):
    return sorted(((values[i], places[i]) for i in range(1, len(places) - 1)
                   if values[i] > values[i - 1] and values[i] > values[i + 1]), reverse=True)


def says(ok):
    return "is" if ok else "IS NOT"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    root = argv[1]
    sys.path.insert(0, str(Path(root) / "incoming" / "v406Reiman" / "instruments"))
    from resolver_as_it_is import resolver
    from podalings_about_an_odd_number import the_surface_with_its_seams
    all_is = True

    print("1. The zeros' heights, from the function itself")
    heights = [10 + i * STEP for i in range(int((TOP - 10) / STEP) + 1)]
    row = [on_its_row(t) for t in heights]
    zeros = []
    for i in range(len(heights) - 1):
        if row[i] * row[i + 1] < 0:
            a, b, at_a = heights[i], heights[i + 1], row[i]
            for _ in range(34):
                m = (a + b) / 2
                at_m = on_its_row(m)
                if at_a * at_m <= 0:
                    b = m
                else:
                    a, at_a = m, at_m
            zeros.append((a + b) / 2)
    ok = (all(abs(z - f) < 1e-5 for z, f in zip(zeros, A_FIELDS_SIX))
          and abs(len(zeros) - (its_turn(TOP) / math.pi + 1)) < 1)
    all_is = all_is and ok
    print(f"   {len(zeros)} zeros to height {TOP:.0f}, a + to a - or a - to a +; the six lowest are a field's own to five places: {says(ok)}")

    print("2. Out: from the living code's own 0s to the zeros")
    names, page = resolver(root)
    to = 2000
    uncrossed = the_surface_with_its_seams(names["_17_next_existing"], to)[0]
    turns = []
    for p in uncrossed:
        q, k = p, 1
        while q <= to:
            turns.append((math.log(p) / math.sqrt(q), k * math.log(p)))
            q, k = q * p, k + 1
    hs = [13.5 + i * 0.01 for i in range(4651)]
    added = [-sum(w * math.cos(h * r) for w, r in turns) for h in hs]
    low = [z for z in zeros if z < 60]
    top = sorted(h for _, h in peaks(added, hs)[:len(low)])
    apart = max(abs(a - b) for a, b in zip(top, low))
    ok = len(top) == len(low) and apart < 0.2
    all_is = all_is and ok
    print(f"   {page}, as it is: {len(uncrossed)} uncrossed numbers of 2 to {to}")
    print(f"   their turns added, heights 13.5 to 60: its {len(low)} highest peaks are at the {len(low)} lowest zeros' heights, apart {apart:.2f} at the most: {says(ok)}")

    print("3. Back: from the zeros to the uncrossed numbers")
    xs = [1.5 + i * 0.005 for i in range(12101)]
    back = [-sum(math.cos(g * l) for g in zeros) for l in (math.log(x) for x in xs)]
    found = peaks(back, xs)
    small = [p for p in uncrossed if p <= 61]
    highest = sorted(x for _, x in found[:len(small)])
    ok = len(highest) == len(small) and all(abs(x - p) < 0.03 for x, p in zip(highest, small))
    its_own = sorted(round(x) for _, x in found[len(small):len(small) + 7])
    near = all(abs(x - round(x)) < 0.03 for _, x in found[len(small):len(small) + 7])
    ok2 = near and its_own == [4, 8, 9, 16, 25, 27, 49]
    all_is = all_is and ok and ok2
    print(f"   the zeros' turns added, numbers of 1.5 to 62: its {len(small)} highest peaks are at the {len(small)} uncrossed numbers of 2 to 61: {says(ok)}")
    print(f"   its seven next are at an uncrossed number multiplied by its own, 4, 8, 9, 16, 25, 27 and 49: {says(ok2)}")

    print("4. A zero's inversion: the heights the turns come together at")
    two = math.log(2) / (2 * math.pi)
    rounds = lambda t, p: t * math.log(p) / (2 * math.pi)
    whole = lambda x: abs(x - round(x))
    together = peaks([abs(v) for v in row], heights)
    twelve = [t for _, t in together[:12]]
    ok = all(whole(t * two) < 0.1 for t in twelve)
    all_is = all_is and ok
    print(f"   the twelve highest, heights 10 to {TOP:.0f}, are at whole rounds of two: {sorted(round(t * two) for t in twelve)}: {says(ok)}")
    best, before_all = 0.0, []
    for i in range(1, len(heights) - 1):
        a = abs(row[i])
        if a > abs(row[i - 1]) and a > abs(row[i + 1]) and a > best:
            best = a
            if heights[i] > zeros[0]:
                before_all.append(heights[i])
    at = [round(t * two) for t in before_all]
    ok = all(whole(t * two) < 0.1 for t in before_all) and at == [2, 3, 4, 5, 7, 10, 12, 19, 22, 27, 31, 41, 53]
    all_is = all_is and ok
    print(f"   a coming together higher than all before it, past the lowest zero, is at whole rounds of two: {at}: {says(ok)}")
    tori = {round(t * two): (round(rounds(t, 3)), round(rounds(t, 5))) for t in before_all}
    ok = tori[12] == (19, 28) and tori[41][0] == 65 and tori[53] == (84, 123)
    all_is = all_is and ok
    print(f"   with them rounds of three and of five nearly whole, tori of whole selves: 12 by {tori[12][0]} by {tori[12][1]}, 41 by {tori[41][0]}, 53 by {tori[53][0]} by {tori[53][1]}; v406Reiman's 19 with 12, 65 with 41 and 84 with 53: {says(ok)}")
    usual = lambda t: 2 * math.pi / math.log(t / (2 * math.pi))
    wide = sorted((((b - a) / usual((a + b) / 2)), (a + b) / 2) for a, b in zip(zeros, zeros[1:]))[-8:]
    ok = all(whole(m * two) < 0.1 for _, m in wide) and all(g > 1.7 for g, _ in wide)
    all_is = all_is and ok
    print(f"   the eight widest places with no zero, by the usual at their height, are at whole rounds of two: {sorted(round(m * two) for _, m in wide)}, the widest twice the usual: {says(ok)}")
    print("All is, of the heights and numbers stepped." if all_is else "Not all is.")
    return 0 if all_is else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
