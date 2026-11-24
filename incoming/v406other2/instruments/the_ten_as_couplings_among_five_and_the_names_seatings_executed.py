#!/usr/bin/env python3
"""For Exhibit THIRTY-TWO's draft, its 3.3, 3.4, 3.5 and 4.5 beside Exhibit THIRTY's steps: the ten as
couplings among a self's five, and two seatings of the names, with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/the_ten_as_couplings_among_five_and_the_names_seatings_executed.py

A line is a saying, ending is or is-not; a line ending sized gives numbers alone. Nothing is proved and
nothing is decided: a line says is of what it stepped. It opens no file and writes no file.
"""
from itertools import combinations, permutations

out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


# A self's five, Exhibit THIRTY's step 143 and the draft's 1.6 and 3.5.
five = ["prior opening", "prior completing", "now opening", "now completing", "next opening"]
openings = [f for f in five if f.endswith("opening")]
completings = [f for f in five if f.endswith("completing")]
couplings = list(combinations(five, 2))
say("a self's five are three openings and two completings", (len(openings), len(completings)) == (3, 2))
say("couplings among five are ten, step 608", len(couplings) == 10)
kinds = {"two openings": [c for c in couplings if all(x in openings for x in c)],
         "an opening with a completing": [c for c in couplings if (c[0] in openings) != (c[1] in openings)],
         "the two completings": [c for c in couplings if all(x in completings for x in c)]}
say("the ten part as three of two openings, six of an opening with a completing, and one of the two completings: "
    "three, six and one, the draft's 3.4", [len(v) for v in kinds.values()] == [3, 6, 1])
later = [sum(1 for c in couplings if c[1] == f) for f in five[1:]]
say("by the later one of a coupling, the five in their order, the ten part as one, two, three and four: "
    "the four moments' rows of v406geodesic2's seventeenth drawing", later == [1, 2, 3, 4])
still = [tuple(f for f in five if f not in c) for c in couplings]
say("a coupling keeps the other three still, step 608, and the ten threes are all the threes of five",
    sorted(still) == sorted(combinations(five, 3)))
say("three have six orders: ten sixes, 60; two in order, 5 by 4, by three, 60; 60 and 60, 120, the draft's 3.5",
    len(list(permutations(range(3)))) == 6 and 10 * 6 == 60 and 5 * 4 * 3 == 60)

# The ten's names: the draft's 4.5 beside step 616.
draft = [{"a first behind it", "a last", "an end"}, {"a store"},
         {"a place", "a magnitude", "a beat", "a value", "a side", "a cut"}]
step616 = [{"a first behind it", "a last", "an end"}, {"a beat", "a value"}, {"a magnitude", "a side"},
           {"a place", "a store", "a cut"}]
both = sorted({frozenset(a & b) for a in draft for b in step616 if a & b}, key=lambda s: (-len(s), sorted(s)))
say("the draft's three, a first behind it, a last and an end, is step 616's three", draft[0] == step616[0])
say("the draft's three, one and six and step 616's three, two, two and three are one parting", sorted(map(sorted, draft)) == sorted(map(sorted, step616)))
say(f"  said as one they are five kinds, {[len(s) for s in both]}: {[sorted(s) for s in both]}", "sized")

# Two seatings of the names: the draft's 3.3 beside step 370.
places = [n for n in range(1, 60) if n % 2 and n % 3 and n % 5]
primes = [n for n in range(2, 60) if all(n % q for q in range(2, n))]
say("the sixteen places of 0 to 60 no spiral of 2, 3 or 5 crosses, the draft's 3.3", len(places) == 16)
say("with the sixteen places the names' three moves are one move of numbers: 9 less, 30 less; 8 up, 30 on; 17 less, 60 less",
    all(places[8 - k] == 30 - places[k - 1] for k in range(1, 9))
    and all(places[k + 7] == places[k - 1] + 30 for k in range(1, 9))
    and all(places[16 - k] == 60 - places[k - 1] for k in range(1, 17)))
up = [primes[k + 8] - primes[k] for k in range(9)]
say("with step 370's seventeen primes, 2 to 59, 8 up is one move of numbers", len(primes) == 17 and len(set(up)) == 1)
say(f"  with them 8 up is on by {up}, and 18 less adds to {[primes[k] + primes[16 - k] for k in range(9)]}", "sized")
say("37 is the tenth of the sixteen places and the twelfth of the seventeen primes", places.index(37) + 1 == 10 and primes.index(37) + 1 == 12)

# 60 to 68 and 69, steps 349 and 523 to 528, beside the draft's 61.
is_prime = lambda n: n > 1 and all(n % q for q in range(2, n))
say("of 60 to 68, 61 and 67 are primes, the places 1 and 7 one 60 on, a pair about 64 as step 524 has them",
    [n for n in range(60, 69) if is_prime(n)] == [61, 67] and 61 + 67 == 2 * 64)
say("69 is 3 by 23, crossed", 69 == 3 * 23)

# The draft's 4.5, twin names about the vertex.
twins = [(11, 13), (17, 19), (29, 31), (41, 43), (59, 61)]
say("the five twin pairs of 4.5 are about a vertex, 0, 60 or 120", all((a + 1) % 60 == 0 for a, _ in twins))
say(f"  about a vertex: {[t for t in twins if (t[0] + 1) % 60 == 0]}; about a cone's widest, 30: "
    f"{[t for t in twins if (t[0] + 1) % 60 == 30]}; all five about a multiple of six: {all((a + 1) % 6 == 0 for a, _ in twins)}", "sized")

for r, text in out:
    print(f"{r:>6} | {text}")
print(f"{sum(1 for o in out if o[0] == 'is')} is; {sum(1 for o in out if o[0] == 'is-not')} is-not; {sum(1 for o in out if o[0] == 'sized')} sized.")
