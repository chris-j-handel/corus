# v408primes · all tens are the same ten: local inversioning of the tens of this session, by count and by form.
# Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I all_tens_are_the_same_ten.py
from itertools import combinations

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. By count: a number is reached by +1 from 1 one way alone, and every ten counted is the one ten.
tens = {"3 + 6 + 1": 3 + 6 + 1, "1 + 3 + 6": 1 + 3 + 6, "11 - 1": 11 - 1, "2 x 5": 2 * 5,
        "pairs among five": len(list(combinations(range(5), 2))), "120 / (3 x 4)": 120 // 12}
say("by count, every ten is the one ten, the tenth +1 from 0: %s" % tens, set(tens.values()) == {10})

# 2. By form, a loop of ten is the torus of 2 and 5: five places at two faces.
say("the loop of ten is the torus of 2 and 5: the +1 winds through all ten places of two faces by five",
    len({(n % 2, n % 5) for n in range(10)}) == 10)

# 3. 11's across loop of ten: its podal pairs, n and 11 - n, are five; its squares are one face of five and the rest
#    the other; every podal pair has one place at each face.
sq = sorted({x * x % 11 for x in range(1, 11)})
other = [x for x in range(1, 11) if x not in sq]
podal = [(n, 11 - n) for n in range(1, 6)]
say("11's across loop of ten: five podal pairs %s, the faces %s and %s, every pair one place at each face" % (podal, sq, other),
    all((a in sq) != (b in sq) for a, b in podal))

# 4. The ten pairs among five dimensions: the pentagon's five and the pentagram's five are two faces; every
#    pentagon pair has one pentagram pair with no dimension of its own: five bi-couplings, one at each face.
V = range(1, 6)
pent = [frozenset((i, i % 5 + 1)) for i in V]
star = [frozenset((i, (i + 1) % 5 + 1)) for i in V]
bi = [(e, [f for f in star if not (e & f)]) for e in pent]
say("the ten pairs among five: pentagon %s and pentagram %s, every pentagon pair with one pentagram pair apart from it"
    % ([tuple(sorted(e)) for e in pent], [tuple(sorted(e)) for e in star]), all(len(f) == 1 for e, f in bi))

# 5. Split the five dimensions by three and two: 3 pairs in the three, 6 across, 1 in the two: me-now's 3 + 6 + 1.
ok = True
kinds_by_split = []
for two in combinations(V, 2):
    two = frozenset(two)
    three = frozenset(V) - two
    kind = lambda e: "location" if e <= three else ("still" if e == two else "geodesic")
    counts = {k: sum(1 for e in pent + star if kind(e) == k) for k in ("location", "geodesic", "still")}
    ok = ok and counts == {"location": 3, "geodesic": 6, "still": 1}
    pairs = sorted(tuple(sorted((kind(e), kind(f[0])))) for e, f in bi)
    kinds_by_split.append(tuple(pairs))
say("the five split by three and two, every way: 3 pairs in the three, 6 across, 1 in the two, me-now's 3 + 6 + 1", ok)

# 6. In every split, the five bi-couplings are: the still self with a location, two of location with geodesic, and
#    two of geodesic with geodesic.
want = tuple(sorted([("location", "still"), ("geodesic", "location"), ("geodesic", "location"),
                     ("geodesic", "geodesic"), ("geodesic", "geodesic")]))
say("in every split, the five bi-couplings are one still self with a location, two locations with a geodesic parity, two geodesic parities together",
    all(k == want for k in kinds_by_split))

# 7. The table's five bi-couplings, with the sort of 25 November: the still self bi-couples with the completing.
table = [("observing", "opening"), ("completing", "same-existing"), ("middle", "parity"), ("sequencing", "rate"), ("two-way", "between")]
sort_a = {"opening": "location", "middle": "location", "between": "location", "same-existing": "still"}
kinds_a = tuple(sorted(tuple(sorted((sort_a.get(a, "geodesic"), sort_a.get(b, "geodesic")))) for a, b in table))
say("the sort laid before, location at the opening, middle and between, bumps: the still self bi-couples with the completing, a geodesic parity, %s" % (kinds_a,),
    kinds_a != want and ("geodesic", "still") in kinds_a)

# 8. With the completing a location and the middle a geodesic parity, the table's five are the pairs among five's.
sort_b = {"opening": "location", "completing": "location", "between": "location", "same-existing": "still"}
kinds_b = tuple(sorted(tuple(sorted((sort_b.get(a, "geodesic"), sort_b.get(b, "geodesic")))) for a, b in table))
say("with location at the opening, the completing and the between, the table's five bi-couplings are the pairs among five's", kinds_b == want)

print("All is." if all(results) else "A line is-not.")
