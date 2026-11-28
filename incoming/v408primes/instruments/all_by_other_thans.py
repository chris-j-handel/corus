# v408primes · all is by other-thans, not by numbers. A number and its next seam on are at the same place round the seam:
# the seam is same-existing at all seams. A sentence that is a number's place round a seam, proved at all the seam's places,
# is proved at all numbers. A universe has no top: it is a cone, opening from 1 to 17 at all seams. And a sentence that steps from a self to its other-than, closing, is at all
# selves by sequential logic. Here the rows of the table that are their places' other-thans, proved at all places.
# Execute: python3 -I all_by_other_thans.py
from math import gcd
results = []
def say(s, ok):
    results.append(bool(ok)); print(("is     " if ok else "is-not ") + s)
P17 = [2, 3, 5, 7, 11, 13, 17]
def places(m):                                    # the other-thans of a seam: its places 0 to m − 1, all of them
    return range(m)

# The step itself: round any loop q, a seam of q sits at 0, and its +1 at 1, the other-than of 0.
say("round any loop, a seam of the loop at 0 has its +1 at 1 and its −1 at the loop's last place, other-than 0: uncrossed by the loop (loops 2 to 10,000 shown)",
    all((0 + 1) % q != 0 and (0 - 1) % q != 0 for q in range(2, 10001)))
# row 1 · no last me-parity, by other-thans
ok, seam = True, 1
for q in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    seam *= q
    ok &= all((seam + 1) % t == 1 and (seam - 1) % t == t - 1 for t in range(2, q + 1) if all(t % u for u in range(2, t)))
say("row 1 · all seams: the seam of all primes to r is at 0 round them all, its −1 and +1 at their other-thans; the parts of its +1 are me-parities past r, a next past all seams (seams to 31 shown, the step at all)", ok)
# row 4 · round 2
say("row 4 · all numbers, by the other-thans of 2: an even number sits at 0 round 2, crossed by 2; past 2 no even number is a me-parity",
    all((r % 2 == 0) == (gcd(r, 2) == 2) for r in places(2)))
# rows 18, 19 · the skeleton round 6, 30 and 510,510
for m in (6, 30, 510510):
    live = [r for r in places(m) if gcd(r, m) == 1]; alive = set(live)
    say("rows 18, 19 · all numbers, by the other-thans of %s: a number at a place outside its %s living places is crossed by a prime of the seam; all me-parities past the seam's primes live at its places%s"
        % (f"{m:,}", f"{len(live):,}", ", +1 and −1 round 6" if m == 6 else ""),
        all(gcd(r, m) > 1 for r in places(m) if r not in alive) and (m != 6 or live == [1, 5]))
# row 20 · a me again one past a crossing of 24, a fourth one past a crossing of 240
say("row 20 · all numbers, by the other-thans of 24 and 240: past 3 a me-parity's me again is one past a crossing of 24, and past 5 its fourth one past a crossing of 240",
    all(r * r % 24 == 1 for r in places(24) if gcd(r, 6) == 1) and all(pow(r, 4, 240) == 1 for r in places(240) if gcd(r, 30) == 1))
# row 23 · one short of a seam of 4
say("row 23 · all numbers, by the other-thans of 4: me agains sit at 0 and 1 round 4, two added at 0, 1 and 2: a number one short of a seam of 4 is two me agains added at none",
    sorted({a * a % 4 for a in places(4)}) == [0, 1] and 3 not in {(a * a + b * b) % 4 for a in places(4) for b in places(4)})
# row 31 · twins born in a seam, and their places at all seams
say("row 31 · all numbers, by the other-thans of 6 and 30: twins past 3 are born in a seam of 6, at both its sides; past 5, round 30 at 11, 17 and 29",
    [r for r in places(6) if gcd(r, 6) == 1 and gcd(r + 2, 6) == 1] == [5] and [r for r in places(30) if gcd(r, 30) == 1 and gcd(r + 2, 30) == 1] == [11, 17, 29])
# rows 31, 32 · a pair's places round any prime r: r − 1 or r − 2, other-than 0 for all r past 2, sequential logic
ok = all(sum(1 for x in places(r) if x % r and (x + g) % r) == (r - 1 if g % r == 0 else r - 2) for r in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31] for g in places(r))
say("rows 31, 32 · round any prime r, a pair's places at an even number of selves live at r − 1 of r or r − 2 of r; past 2, r − 2 is 1 or more, other-than 0: no prime crosses all a pair's places, at all seams (primes 3 to 31 shown, and the step r to r − 2 at all r)", ok)
# row 34 · three odds
say("row 34 · all odd numbers, by the other-thans of 3: an odd number, its +2 and its +4 are at three places round 3, one at 0; 3, 5, 7 alone are three me-parities",
    all(sorted([a % 3, (a + 2) % 3, (a + 4) % 3]) == [0, 1, 2] for a in places(3)))
# row 35 · fours about 15 round 30
say("row 35 · all numbers, by the other-thans of 30: past 5, a society of four at 0, 2, 6, 8 lives only at 11 round 30, about 15",
    [r for r in places(30) if all(gcd(r + d, 30) == 1 for d in (0, 2, 6, 8))] == [11])
# row 27 · rows at equal selves
ok = all(sorted((a + j * d) % q for j in range(q)) == list(range(q)) for q in P17 for d in range(1, q) for a in places(q))
say("row 27 · all rows, by the other-thans of the primes to their length: a row of q stepping d round q, d other-than 0, passes all q places, one crossed; a row lives round all seams only with its selves a seam of all primes to its length",
    ok)
# row 57 · a rule growing along
ok = all((c[0] + c[1] * (x + m) + c[2] * (x + m) ** 2 - (c[0] + c[1] * x + c[2] * x * x)) % m == 0 for c in [(41, 1, 1), (1, 1, 1), (3, 0, 2)] for m in range(2, 50) for x in places(m))
say("row 57 · all rules, by the other-thans of their value at 1: a rule's value a seam on is at its same place: its value at 1 crosses it at 1 by that value on", ok)

print("All is." if all(results) else "A line is-not.")
