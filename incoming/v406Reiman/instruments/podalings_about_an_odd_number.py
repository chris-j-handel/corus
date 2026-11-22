"""Podalings: a self and an other from their between, a partner's suggesting explored by executing.

Nothing is proved here. By a partner's word a podal pair has no prior side and
no next side: its sides are a self and an other, and a number is their
between. Exhibit ONE Natural Resolver has it, of its names: Sides, self and
other, each sharing between them.

Part 1 is Exhibit ONE Natural Resolver's code as it is in its living file. A
spiral of selves at a number is a between. From it a self goes the
spiral one way, 9 along to its next self, and an other goes it its other way,
9 along to the self before. A between self is across from both, 10 from a self
and 10 from an other. Parts 2 and 3 are the surface of
a_number_by_its_spirals.py, a self alone and odd prime spirals side by side,
two moments a number. No dividing is in parts 1 to 3. Part 4 is by numbers'
own arithmetic, with no resolver in it, and says so.

A line here is all or none: is, or is not, of all the numbers stepped. No line
is an average, a measuring or a statistic.

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


def a_spiral_alone(step, q, to):
    """A spiral of q selves from its opening, its society number by number, two moments a number."""
    society = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
    along = {(i, 9): (i + 1) % q for i in range(q)}
    by_number = {q: society}
    for k in range(q + 1, to + 1):
        for _ in range(2):
            society = step(society, along)
        by_number[k] = society
    return by_number


def its_priors(society, q, ring=None):
    return tuple(dict(society[i if ring is None else (ring, i)][0]).get(S, 0) for i in range(q))


def self_and_other_from_their_between(step, q):
    """A self one way and an other its other way from a between, a between self across from both."""
    by_number = a_spiral_alone(step, q, 4 * q)
    opening = its_priors(by_number[q], q)

    def at_seam(p):
        return p == opening or p == tuple(-x for x in opening)

    goings = together = fold = same_on_the_line = like_pair = True
    for c in range(2 * q, 3 * q + 1):
        between = by_number[c]
        was = its_priors(between, q)
        pairs = [i for i in range(q) if was[i] == was[(i + 1) % q]]
        like_pair = like_pair and len(pairs) == 1
        line = (2 * pairs[0] + 1) % q            # the fold through the between's own like pair: i with line - i
        on_the_line = line * (q + 1) // 2 % q    # the self the fold brings onto itself
        society, couplings = {}, {}
        for i in range(q):
            society[("self", i)] = (list(between[i][0]), list(between[i][1]))
            society[("other", i)] = (list(between[i][0]), list(between[i][1]))
            society[("between", i)] = ([], [])
            couplings[(("self", i), 9)] = ("self", (i + 1) % q)
            couplings[(("other", i), 9)] = ("other", (i - 1) % q)
            couplings[(("self", i), 10)] = ("between", i)
            couplings[(("other", i), 10)] = ("between", i)
        for d in range(1, q + 1):
            for _ in range(2):
                society = step(society, couplings)
            a_self, an_other = its_priors(society, q, "self"), its_priors(society, q, "other")
            goings = goings and a_self == its_priors(by_number[c + d], q) and an_other == its_priors(by_number[c - d], q)
            if at_seam(was):
                together = together and at_seam(a_self) == at_seam(an_other)
            else:
                together = together and not (at_seam(a_self) and at_seam(an_other))
            fold = fold and all(a_self[i] == an_other[(line - i) % q] for i in range(q))
            received = [v for s, v in society[("between", on_the_line)][1] if s == S]
            same_on_the_line = same_on_the_line and len(received) == 2 and received[0] == received[1]
    return goings, together, fold, same_on_the_line, like_pair


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 3720
    names, page = resolver(root)
    step = names["_17_next_existing"]
    uncrossed, seam = the_surface_with_its_seams(step, to)
    U = set(uncrossed)
    odd_spirals = sorted(q for q in seam if q > 2)
    all_is = True

    print("1. A self and an other from their between, with Exhibit ONE Natural Resolver's code as it is")
    print(f"   {len(odd_spirals)} odd spirals, 3 to 59 selves, a spiral alone; a turn of betweens, and a turn of distances from a between")
    goings = together = fold = same = like = True
    for q in odd_spirals:
        g, t, f, s, l = self_and_other_from_their_between(step, q)
        goings, together, fold, same, like = goings and g, together and t, fold and f, same and s, like and l
    all_is = all_is and goings and together and fold and same and like
    print(f"   an other, going the spiral its other way from a between, is as the spiral was with the number as far short of the between; a self, going on, as the number as far past it: {is_or_is_not(goings)}")
    print(f"   from a between at the spiral's seam, a self and an other are at the seam together or neither; from a between off it, never together: {is_or_is_not(together)}")
    print(f"   a spiral at a number has one like pair: {is_or_is_not(like)} · one fold through the between's own like pair exchanges a self and an other, at all distances: {is_or_is_not(fold)}")
    print(f"   the between self on the fold's line receives the same from a self and from an other, at all distances, and never a parting: {is_or_is_not(same)}")

    print("2. The surface, all spirals side by side: a between, a number, with a self and an other at one distance from it")
    print(f"   2 to {to}, a self alone and {len(odd_spirals)} odd spirals, all its numbers and all their distances gone through")
    rule_at = rule_off = places = True
    for q in odd_spirals:
        for c in range(q, to + 1):
            at = c in seam[q]
            for d in range(1, min(c - q, to - c) + 1):
                an_other, a_self = (c - d) in seam[q], (c + d) in seam[q]
                if at:
                    rule_at = rule_at and an_other == a_self
                else:
                    rule_off = rule_off and not (an_other and a_self)
            if c >= 2 * q and c + q <= to:
                living = sum(1 for d in range(1, q + 1) if (c - d) not in seam[q] and (c + d) not in seam[q])
                places = places and living == (q - 1 if at else q - 2)
    two = all(((c - d) in seam[2]) == ((c + d) in seam[2]) for c in range(4, to) for d in range(1, min(c - 2, to - c) + 1))
    all_is = all_is and rule_at and rule_off and places and two
    print(f"   at its seam with their between, a spiral crosses a self and an other together or neither: {is_or_is_not(rule_at)}")
    print(f"   off its seam with their between, a spiral crosses one of the two and never both: {is_or_is_not(rule_off)}")
    print(f"   of one turn of a spiral's distances, all but one are with neither crossed at its seam, and all but two off it: {is_or_is_not(places)}")
    print(f"   the self alone, two, crosses a self and an other together or neither, with all betweens: {is_or_is_not(two)}")

    print("3. An odd number a between, by the surface's uncrossed numbers and its seams alone")
    fives = range(5, to - 3, 2)
    one_of_three = all(sum(1 for m in (n, n + 2, n + 4) if m in seam[3]) == 1 for n in fives)
    most_two = all(sum(1 for m in (n, n + 2, n + 4) if m in U) <= 2 for n in fives)
    all_is = all_is and one_of_three and most_two
    print(f"   a five opening with an odd number: three odd numbers and two even, and of its three odd numbers one is at three's seam: {is_or_is_not(one_of_three)}")
    print(f"   a five above 3 has two uncrossed at the most, two apart or four apart: {is_or_is_not(most_two)}")

    pairs = (2, 4, 6, 8)
    centres = range(15, to - 7, 2)

    def crossed_of_the_two(c, d, q):
        return ((c - d) in seam[q]) + ((c + d) in seam[q])

    three_at = all([crossed_of_the_two(c, d, 3) for d in pairs] == [0, 0, 2, 0] for c in centres if c in seam[3])
    three_off = all([crossed_of_the_two(c, d, 3) for d in pairs] == [1, 1, 0, 1] for c in centres if c not in seam[3])
    five_at = all(all(crossed_of_the_two(c, d, 5) == 0 for d in pairs) for c in centres if c in seam[5])
    five_off = all(sorted(crossed_of_the_two(c, d, 5) for d in pairs) == [0, 0, 1, 1] for c in centres if c not in seam[5])
    all_is = all_is and three_at and three_off and five_at and five_off
    print("   a 1 to 17 with its 9 on an odd number, the between: its odd names two and two about 9 are four podal pairs, a self and an other at 2, 4, 6 and 8")
    print(f"   three, at its seam with the between, crosses neither of the two at 2, 4 and 8, and both at 6: {is_or_is_not(three_at)}")
    print(f"   three, off its seam, crosses one of the two at 2, at 4 and at 8, and neither at 6: {is_or_is_not(three_off)}")
    print(f"   five, at its seam with the between, crosses neither of the two at all four: {is_or_is_not(five_at)}")
    print(f"   five, off its seam, crosses one of the two at two of the four, and neither at its other two: {is_or_is_not(five_off)}")

    living = {c: [d for d in pairs if c - d in U and c + d in U] for c in centres}
    diamonds = [c for c in centres if 2 in living[c] and 4 in living[c]]
    diamond_is = all(c in seam[3] and c in seam[5] for c in diamonds)
    six_primes = [c for c in centres if living[c] == [2, 4, 8]]
    six_is = all(c in seam[3] and c in seam[5] for c in six_primes)
    a_prime_between = all(set(living[c]) <= {6} for c in centres if c in U)
    primes_with_none = [c for c in centres if c in U and not living[c]]
    primes_with_six = [c for c in centres if c in U and living[c] == [6]]
    none_rule = all(not living[c] for c in centres
                    if c not in seam[3] and ((c - 1) in seam[5] or (c + 1) in seam[5]))
    all_is = all_is and diamond_is and six_is and a_prime_between and none_rule
    print(f"   with 2 and 4 both living, the between is at the seam of three and of five: {is_or_is_not(diamond_is)} · found: {', '.join(map(str, diamonds))}")
    print(f"   with 2, 4 and 8 all living, six primes with one between: found {' and '.join(map(str, six_primes))}, at the seam of three and of five: {is_or_is_not(six_is)}")
    print(f"   with a prime the between, a living podal pair of its 1 to 17 is at 6 and at no other: {is_or_is_not(a_prime_between)}")
    print(f"   primes with it living at 6, from 17 on: {', '.join(map(str, primes_with_six[:6]))} · and with none: {', '.join(map(str, primes_with_none[:6]))}")
    print(f"   a between off three's seam, and one past or one short of five's seam, has no living podal pair in its 1 to 17: {is_or_is_not(none_rule)}")

    outward = all(any(c - d in U and c + d in U for d in range(0, c - 1)) for c in range(4, to // 2 + 1))
    all_is = all_is and outward
    print(f"   a number, 4 to {to // 2}, is the between of a self and an other both uncrossed, found stepping outward from it: {is_or_is_not(outward)}")

    print("4. By numbers' own arithmetic, with no resolver in it")
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
    print(f"   with an odd between, a closed turn has a pair uncrossed by all three, never none: {is_or_is_not(never_none)}")

    print("All is." if all_is else "NOT ALL IS.")
