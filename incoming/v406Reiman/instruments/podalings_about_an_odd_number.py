"""Podalings about an odd number: a partner's suggesting explored by executing.

Nothing is proved here. A podal pair about a number is its prior side and its
next side at one distance, as Exhibit THREE Natural Numbers 5.6 has podaling:
a going one way to k and a going other way to N - k on a ring of N. A podal
pair is living here once both its sides are uncrossed.

Part 1 is Exhibit ONE Natural Resolver's code as it is in its living file: the
surface of a_number_by_its_spirals.py, a self alone and odd prime spirals side
by side, two moments a number, with the spirals at their seam said number by
number. No dividing is in parts 1 and 2. Part 3 is by numbers' own arithmetic,
with no resolver in it, and says so.

    python3 -I incoming/v406Reiman/instruments/podalings_about_an_odd_number.py . [--to 3720]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, resolver
from a_number_by_its_spirals import its_own_closings, priors_of


def the_surface_with_its_seams(step, to, open_to=59):
    """The surface of a_number_by_its_spirals.py, saying with a number the spirals at their seam with it."""
    society = {(1, 0): ([(S, exhibit_spiral_priors(1)[0])], [])}
    couplings = {((1, 0), 9): (1, 0)}
    opened = {1: (exhibit_spiral_priors(1)[0],)}
    uncrossed, seam = [], {2: set()}
    for k in range(2, to + 1):
        for _ in range(2):
            society = step(society, couplings)
        if priors_of(society, 1) == tuple(-x for x in opened[1]):
            seam[2].add(k)
        crossed = k in seam[2] and k > 2
        for q, was in opened.items():
            if q == 1:
                continue
            now = priors_of(society, q)
            if now == was or now == tuple(-x for x in was):
                seam[q].add(k)
                crossed = True
        if crossed:
            continue
        uncrossed.append(k)
        if k % 2 and k <= open_to:
            start = exhibit_spiral_priors(k)
            for i in range(k):
                society[(k, i)] = ([(S, start[i])], [])
                couplings[((k, i), 9)] = (k, (i + 1) % k)
            opened[k] = tuple(start[i] for i in range(k))
            seam[k] = {k}
    return uncrossed, seam


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 3720
    names, page = resolver(root)
    uncrossed, seam = the_surface_with_its_seams(names["_17_next_existing"], to)
    U = set(uncrossed)
    odd_spirals = sorted(q for q in seam if q > 2)
    all_is = True

    print("1. A spiral at its seam with a number, and its two sides, with Exhibit ONE Natural Resolver's code as it is")
    print(f"   the surface: 2 to {to}, a self alone and {len(odd_spirals)} odd spirals, uncrossed {len(uncrossed)}")
    together = apart = at_seam = off_seam = 0
    rule = places = True
    for q in odd_spirals:
        for c in range(q, to + 1):
            at = c in seam[q]
            for d in range(1, min(c - q, to - c) + 1):
                prior_side, next_side = (c - d) in seam[q], (c + d) in seam[q]
                if at:
                    together += 1
                    rule = rule and prior_side == next_side
                else:
                    apart += 1
                    rule = rule and not (prior_side and next_side)
            if c >= 2 * q and c + q <= to:
                living = sum(1 for d in range(1, q + 1) if (c - d) not in seam[q] and (c + d) not in seam[q])
                places = places and living == (q - 1 if at else q - 2)
                at_seam += at
                off_seam += not at
    two = all(((c - d) in seam[2]) == ((c + d) in seam[2]) for c in range(4, 400) for d in range(1, c - 1) if c + d <= to)
    all_is = all_is and rule and places and two
    print(f"   at its seam with a number, a spiral crosses the number's two sides together or neither, {together:,} distances gone through: {is_or_is_not(rule)}")
    print(f"   off its seam, a spiral crosses one side with a distance and never both, {apart:,} distances gone through: {is_or_is_not(rule)}")
    print(f"   of a spiral's q distances in a row, q - 1 are with neither side crossed at its seam, {at_seam:,} numbers, and q - 2 off it, {off_seam:,} numbers: {is_or_is_not(places)}")
    print(f"   the self alone, two, crosses a number's two sides together or neither, from all numbers: {is_or_is_not(two)}")

    print("2. From an odd number, by the surface's uncrossed numbers and its seams alone")
    fives = range(5, to - 3, 2)
    one_of_three = all(sum(1 for m in (n, n + 2, n + 4) if m in seam[3]) == 1 for n in fives)
    most_two = all(sum(1 for m in (n, n + 2, n + 4) if m in U) <= 2 for n in fives)
    two_apart = sum(1 for n in fives if (n in U and n + 2 in U) or (n + 2 in U and n + 4 in U))
    four_apart = sum(1 for n in fives if n in U and n + 4 in U)
    all_is = all_is and one_of_three and most_two
    print(f"   a five opening with an odd number, 5 to {to - 4}: three odd numbers and two even, and of its three odd numbers one is at three's seam: {is_or_is_not(one_of_three)}")
    print(f"   two uncrossed at the most in a five above 3: {is_or_is_not(most_two)} · fives with two uncrossed two apart: {two_apart}, and four apart: {four_apart}")

    centres = range(11, to - 7, 2)
    living = {c: [d for d in (2, 4, 6, 8) if c - d in U and c + d in U] for c in centres}
    by_number = [sum(1 for c in centres if len(living[c]) == k) for k in range(5)]
    print(f"   a 1 to 17 with its 9 on an odd number, 11 to {to - 8}: its odd names two and two about 9 are four podal pairs, at 2, 4, 6 and 8")
    print(f"   odd numbers with 0, 1, 2 and 3 living podal pairs in their 1 to 17: {by_number[0]}, {by_number[1]}, {by_number[2]} and {by_number[3]} · with all four: {by_number[4]}")
    by_class = {}
    steady = True
    for c in range(61, to - 7, 2):
        clear = tuple(d for d in (2, 4, 6, 8) if not ({c - d, c + d} & (seam[3] | seam[5])))
        steady = steady and by_class.setdefault(c % 30, clear) == clear
    shape = [sum(1 for v in by_class.values() if len(v) == k) for k in range(5)]
    both_seams = by_class[15]
    at_three = all(set(v) <= {2, 4, 8} for r, v in by_class.items() if r % 3 == 0)
    off_three = all(set(v) <= {6} for r, v in by_class.items() if r % 3)
    all_is = all_is and steady and shape == [4, 8, 2, 1, 0] and both_seams == (2, 4, 8) and at_three and off_three
    print(f"   by three and five alone, the same with a turn of 30: {is_or_is_not(steady)} · of 15 odd numbers in a turn, with 0, 1, 2 and 3 pairs uncrossed by both: {shape[0]}, {shape[1]}, {shape[2]} and {shape[3]}")
    print(f"   at three's seam the pairs uncrossed by three are 2, 4 and 8, and off it 6 alone: {is_or_is_not(at_three and off_three)} · at the seam of both, 2, 4 and 8: {is_or_is_not(both_seams == (2, 4, 8))}")
    diamonds = [c for c in centres if 2 in living[c] and 4 in living[c]]
    three_living = [c for c in centres if living[c] == [2, 4, 8]]
    none_about_a_prime = [c for c in centres if c in U and not living[c]]
    primes_gone = [c for c in centres if c in U]
    diamond_is = all(c % 30 == 15 for c in diamonds)
    all_is = all_is and diamond_is
    print(f"   with 2 and 4 both living, four primes about a number: {', '.join(map(str, diamonds))} · all at the seam of three and of five: {is_or_is_not(diamond_is)}")
    print(f"   with 2, 4 and 8 all living, six primes about a number: {', '.join(map(str, three_living))}")
    print(f"   about an uncrossed number, a prime, with no living podal pair in its 1 to 17: {len(none_about_a_prime)} of {len(primes_gone)}")

    half = to // 2
    stations = range(101, half, 2)
    pairs = {c: sum(1 for d in range(2, c - 1, 2) if c - d in U and c + d in U) for c in stations}
    print(f"   living podal pairs at all distances, about the odd numbers 101 to {half - 1}: the fewest {min(pairs.values())}, about {min(pairs, key=pairs.get)}; the most {max(pairs.values())}, about {max(pairs, key=pairs.get)}")
    for q in (3, 5, 7, 11, 13):
        at = [pairs[c] for c in stations if c in seam[q]]
        off = [pairs[c] for c in stations if c not in seam[q]]
        ratio = (sum(at) / len(at)) / (sum(off) / len(off))
        print(f"   at the seam of {q} over off it, living podal pairs: {ratio:.2f} · by its places, {q - 1} over {q - 2}: {(q - 1) / (q - 2):.2f}")
    richest = sorted(stations, key=lambda c: -pairs[c])[:5]
    poorest = sorted(stations, key=lambda c: pairs[c])[:5]
    print(f"   the five with the most: {', '.join(f'{c} ({pairs[c]})' for c in richest)} · the five with the fewest: {', '.join(f'{c} ({pairs[c]})' for c in poorest)}")
    prime_mean = sum(pairs[c] for c in stations if c in U) / sum(1 for c in stations if c in U)
    crossed_mean = sum(pairs[c] for c in stations if c not in U) / sum(1 for c in stations if c not in U)
    print(f"   living podal pairs about an uncrossed odd number, a prime, {prime_mean:.1f} · about a crossed odd number, {crossed_mean:.1f}")

    print("3. By numbers' own arithmetic, with no resolver in it")
    turn = 3 * 5 * 7
    formula = True
    fewest = turn
    for c in range(1, 2 * turn, 2):
        found = sum(1 for e in range(turn) if all((c - 2 * e) % q and (c + 2 * e) % q for q in (3, 5, 7)))
        by_places = 1
        for q in (3, 5, 7):
            by_places *= q - 1 if c % q == 0 else q - 2
        formula = formula and found == by_places
        fewest = min(fewest, found)
    all_is = all_is and formula and fewest > 0
    print(f"   a closed turn of three, five and seven, 105 even distances: the pairs uncrossed by all three are a spiral's places less one at its seam and less two off it, multiplied: {is_or_is_not(formula)} · the fewest {fewest}, never none")
    for low, high in ((11, 99), (101, 999), (1001, to - 8)):
        inside = [c for c in range(low, high + 1, 2)]
        share = sum(1 for c in inside if living[c]) / len(inside)
        print(f"   odd numbers {low} to {high} with a living podal pair in their 1 to 17: {share:.0%}")
    for far in (10 ** 6, 10 ** 9, 10 ** 12):
        primes_about = {n for n in range(far - 3009, far + 3010, 2) if its_own_closings(n)}
        inside = range(far - 2999, far + 3000, 2)
        share = sum(1 for c in inside if any(c - d in primes_about and c + d in primes_about for d in (2, 4, 6, 8))) / len(inside)
        print(f"   about {far:,}, 3,000 on both sides, by a number's own closings: {share:.1%}")

    print("All is." if all_is else "NOT ALL IS.")
