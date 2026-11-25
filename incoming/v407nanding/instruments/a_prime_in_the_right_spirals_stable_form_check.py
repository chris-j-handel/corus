"""v407nanding · a prime in the right spiral's stable form: a round of four points, its two projections an even and an odd.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/a_prime_in_the_right_spirals_stable_form_check.py .

A partner's saying of 24 November: an atom has a prime numbering relation to c in right spiral stable form projecting of
possibly even parity. A point is (a, b), whole numbers; its right spiral step is (b, -a), v406geodesic2's; its number is
a by a and b by b. The part of numbers alone is executed here; atom and c are not shown. All or none.
"""
import sys
from pathlib import Path

root = Path(sys.argv[1])
HORIZON = 20000
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def step(p):
    return (p[1], -p[0])


def round_of(p):
    out = [p]
    for _ in range(4):
        out.append(step(out[-1]))
    return out


primes = [n for n in range(2, HORIZON + 1) if all(n % d for d in range(2, int(n ** 0.5) + 1))]
points = {}
for a in range(0, int(HORIZON ** 0.5) + 1):
    for b in range(0, int(HORIZON ** 0.5) + 1):
        points.setdefault(a * a + b * b, []).append((a, b))
say("P1. A right spiral step is a quarter turn: a point goes round four points and back, all points of a prime's number",
    all(round_of(pt)[4] == pt and len(set(round_of(pt)[:4])) == 4 for p in primes for pt in points.get(p, [])))
four_up = [p for p in primes if p % 4 == 1]
three_up = [p for p in primes if p % 4 == 3]
say(f"P2. A prime one more than a number of fours has a point, a by a and b by b: all {len(four_up):,} of them to {HORIZON:,} (a field's, Fermat's, stepped)",
    all(p in points for p in four_up))
say(f"P3. A prime three more than a number of fours has no point: all {len(three_up):,} of them to {HORIZON:,} (a field's, stepped)",
    all(p not in points for p in three_up))
say("P4. 2 has a point, (1, 1), its two projections both odd",
    points.get(2) == [(1, 1)])
say("P5. An odd prime's point has its two projections an even and an odd, at all points to the horizon: an even projection",
    all((a % 2) != (b % 2) for p in four_up for a, b in points[p]))
say("P6. An odd prime's points are eight, two rounds of four, and its mirror (a, -b) takes the one round to the other: a bi-folding",
    all(len({(x, y) for a, b in points[p] for x, y in round_of((a, b))[:4] + round_of((a, -b))[:4]}) == 8 for p in four_up))
say("M1. With the step (b, a) in place of (b, -a), a point is round in two steps and not four, and P1 says is-not",
    all(((p[1], p[0])[1], (p[1], p[0])[0]) == p for p in [(1, 2), (3, 4)]))
print("\nAll is." if all(results) else "\nNot all is.")
