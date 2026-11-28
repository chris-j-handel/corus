# v408primes · inherited DNA a mixture of two parental me-parities; double bi-inversioning from mating bi-coupling to
# birthing me-parity. All combinations counted whole, a turn closing; nothing simulated.
# Execute: python3 -I double_bi_inversioning_mating_to_birthing.py
from itertools import product
from collections import Counter

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. A parent is a bi-coupling of two inherited copies at every gene: one from its mother, one from its father.
#    Each parent passes one of its two; two parents, two by two: four births at a gene, the me again of 2.
mother, father = ("A", "a"), ("A", "a")
births = [tuple(sorted(m + f)) for m, f in product(mother, father)]
c = Counter("".join(b) for b in births)
say("at a gene, two parents of two copies give four births, the me again of 2: %s" % dict(c), len(births) == 4 and c == {"AA": 1, "Aa": 2, "aa": 1})

# 2. Across a self's paired copies, a parent's passing is one of 2 to the n, every pair parted one way or the other;
#    for a human's 23 pairs, 8,388,608; two parents, their product.
n = 23
one = 2 ** n
say("a parent's passing over %d paired copies is one of %d; two parents' births %d, before any crossing" % (n, one, one * one), one == 8388608)

# 3. Along a copy, the crossings over invert its origin once at each crossing: from a grandmother's to a grandfather's
#    and back. An even count of crossings ends at the same origin, an odd count at the other.
def ends_other(pattern):
    return sum(pattern) % 2 == 1
ok, rows = True, []
for k in range(1, 16):
    pats = list(product((0, 1), repeat=k))
    other = sum(1 for p in pats if ends_other(p))
    rows.append((k, len(pats) - other, other))
    ok = ok and other == len(pats) - other
say("over all crossing patterns at k places, the copy ends at the same origin and at the other exactly half and half, k of 1 to 15: %s ..." % rows[:4], ok)

# 4. Along a copy, the origin at a place is its crossings before it, odd or even: the inversion's count, as a number's
#    odd or even is its prime parts' count.
pattern = (0, 1, 0, 0, 1, 1, 0, 1)
origin, run = [], 0
for x in pattern:
    run ^= x
    origin.append("other" if run else "same")
say("a copy crossed at places %s carries its origin %s, inverting once at each crossing" % ([i for i, x in enumerate(pattern) if x], origin),
    origin == ["same", "other", "other", "other", "same", "other", "other", "same"])

# 5. Double: the first parting parts a self's two others, its mother's copy and its father's, crossed; the second parts
#    the two sisters of each. Two partings, four gametes from one cell, all four places of the me again of 2.
cell = [("m", "m"), ("f", "f")]                     # after copying: two sisters of the mother's, two of the father's
first = [cell[0], cell[1]]                           # the first parting: other from other
second = [s for pair in first for s in pair]         # the second parting: sister from sister
say("two partings give four gametes from one cell: %s" % second, len(second) == 4 and sorted(second) == ["f", "f", "m", "m"])

# 6. A birth is a new bi-coupling, one copy from each parent at every gene: its pair is in neither parent alone.
say("a birth's pair at a gene is one from each parent, a +1 in neither self alone, at all four births",
    all(len(b) == 2 for b in births))

print("All is." if all(results) else "A line is-not.")
