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

A line here is all or none: is, or is not, of all the numbers the surface
stepped. No line is an average, a measuring or a statistic.

    python3 -I incoming/v406Reiman/instruments/podalings_about_an_odd_number.py . [--to 3720]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, resolver
from a_number_by_its_spirals import priors_of


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
    print(f"   the surface: 2 to {to}, a self alone and {len(odd_spirals)} odd spirals, all its numbers and all their distances gone through")
    rule_at = rule_off = places = True
    for q in odd_spirals:
        for c in range(q, to + 1):
            at = c in seam[q]
            for d in range(1, min(c - q, to - c) + 1):
                prior_side, next_side = (c - d) in seam[q], (c + d) in seam[q]
                if at:
                    rule_at = rule_at and prior_side == next_side
                else:
                    rule_off = rule_off and not (prior_side and next_side)
            if c >= 2 * q and c + q <= to:
                living = sum(1 for d in range(1, q + 1) if (c - d) not in seam[q] and (c + d) not in seam[q])
                places = places and living == (q - 1 if at else q - 2)
    two = all(((c - d) in seam[2]) == ((c + d) in seam[2]) for c in range(4, to) for d in range(1, min(c - 2, to - c) + 1))
    all_is = all_is and rule_at and rule_off and places and two
    print(f"   at its seam with a number, a spiral crosses the number's two sides together or neither: {is_or_is_not(rule_at)}")
    print(f"   off its seam, a spiral crosses one side with a distance and never both: {is_or_is_not(rule_off)}")
    print(f"   of one turn of a spiral's distances, all but one are with neither side crossed at its seam, and all but two off it: {is_or_is_not(places)}")
    print(f"   the self alone, two, crosses a number's two sides together or neither, from all numbers: {is_or_is_not(two)}")

    print("2. From an odd number, by the surface's uncrossed numbers and its seams alone")
    fives = range(5, to - 3, 2)
    one_of_three = all(sum(1 for m in (n, n + 2, n + 4) if m in seam[3]) == 1 for n in fives)
    most_two = all(sum(1 for m in (n, n + 2, n + 4) if m in U) <= 2 for n in fives)
    all_is = all_is and one_of_three and most_two
    print(f"   a five opening with an odd number: three odd numbers and two even, and of its three odd numbers one is at three's seam: {is_or_is_not(one_of_three)}")
    print(f"   a five above 3 has two uncrossed at the most, two apart or four apart: {is_or_is_not(most_two)}")

    pairs = (2, 4, 6, 8)
    centres = range(15, to - 7, 2)
    def crossed_sides(c, d, q):
        return ((c - d) in seam[q]) + ((c + d) in seam[q])
    three_at = all([crossed_sides(c, d, 3) for d in pairs] == [0, 0, 2, 0] for c in centres if c in seam[3])
    three_off = all([crossed_sides(c, d, 3) for d in pairs] == [1, 1, 0, 1] for c in centres if c not in seam[3])
    five_at = all(all(crossed_sides(c, d, 5) == 0 for d in pairs) for c in centres if c in seam[5])
    five_off = all(sorted(crossed_sides(c, d, 5) for d in pairs) == [0, 0, 1, 1] for c in centres if c not in seam[5])
    all_is = all_is and three_at and three_off and five_at and five_off
    print("   a 1 to 17 with its 9 on an odd number: its odd names two and two about 9 are four podal pairs, at 2, 4, 6 and 8")
    print(f"   three, at its seam with the number, crosses neither side at 2, 4 and 8, and both sides at 6: {is_or_is_not(three_at)}")
    print(f"   three, off its seam, crosses one side at 2, at 4 and at 8, and neither side at 6: {is_or_is_not(three_off)}")
    print(f"   five, at its seam with the number, crosses no side of the four: {is_or_is_not(five_at)}")
    print(f"   five, off its seam, crosses one side of two of the four, and no side of its other two: {is_or_is_not(five_off)}")

    living = {c: [d for d in pairs if c - d in U and c + d in U] for c in centres}
    diamonds = [c for c in centres if 2 in living[c] and 4 in living[c]]
    diamond_is = all(c in seam[3] and c in seam[5] for c in diamonds)
    six_primes = [c for c in centres if living[c] == [2, 4, 8]]
    six_is = all(c in seam[3] and c in seam[5] for c in six_primes)
    about_a_prime = all(set(living[c]) <= {6} for c in centres if c in U)
    primes_with_none = [c for c in centres if c in U and not living[c]]
    primes_with_six = [c for c in centres if c in U and living[c] == [6]]
    none_rule = all(not living[c] for c in centres
                    if c not in seam[3] and ((c - 1) in seam[5] or (c + 1) in seam[5]))
    all_is = all_is and diamond_is and six_is and about_a_prime and none_rule
    print(f"   with 2 and 4 both living about an odd number, the number is at the seam of three and of five: {is_or_is_not(diamond_is)} · found: {', '.join(map(str, diamonds))}")
    print(f"   with 2, 4 and 8 all living, six primes about a number: found {' and '.join(map(str, six_primes))}, at the seam of three and of five: {is_or_is_not(six_is)}")
    print(f"   about an uncrossed odd number, a prime, a living podal pair of its 1 to 17 is at 6 and at no other: {is_or_is_not(about_a_prime)}")
    print(f"   primes with it living at 6, from 17 on: {', '.join(map(str, primes_with_six[:6]))} · and with none: {', '.join(map(str, primes_with_none[:6]))}")
    print(f"   an odd number off three's seam, and one past or one short of five's seam, has no living podal pair in its 1 to 17: {is_or_is_not(none_rule)}")

    outward = all(any(c - d in U and c + d in U for d in range(0, c - 1)) for c in range(4, to // 2 + 1))
    all_is = all_is and outward
    print(f"   stepping outward from a number, 4 to {to // 2}, a distance with both sides uncrossed is found, short of the number: {is_or_is_not(outward)}")

    print("3. By numbers' own arithmetic, with no resolver in it")
    turn = 3 * 5 * 7
    by_places_is = never_none = True
    for c in range(1, 2 * turn, 2):
        found = sum(1 for e in range(turn) if all((c - 2 * e) % q and (c + 2 * e) % q for q in (3, 5, 7)))
        by_places = 1
        for q in (3, 5, 7):
            by_places *= q - 1 if c % q == 0 else q - 2
        by_places_is = by_places_is and found == by_places
        never_none = never_none and found > 0
    all_is = all_is and by_places_is and never_none
    print(f"   a closed turn of three, five and seven: the pairs uncrossed by all three are a spiral's places less one at its seam and less two off it, multiplied: {is_or_is_not(by_places_is)}")
    print(f"   about an odd number, a closed turn has a pair uncrossed by all three, never none: {is_or_is_not(never_none)}")

    print("All is." if all_is else "NOT ALL IS.")
