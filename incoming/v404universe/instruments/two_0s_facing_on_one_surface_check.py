"""Two 0s facing on one surface: their own ways, a passing, a turning, and a zone.

This reads no file and writes none. Each count is by whole numbers and their ratios.

Said in the session: two 0s with forward facing arrows on a common surface; up, down, right,
left, next, prior, six one ways; a zone in next direction, same-existing enough; two wandering
toward each other on one line, passing, handing off their priors, a now living between.

  1  a 0's three own ways, next, right and up, and an other's, facing it
  2  three half turns, each inverting two of three
  3  two on one line: each one's prior and next, before a passing and after
  4  a passing with priors handed off, and a turning with each its own prior
  5  two round one line at two rates: the places of passing
  6  a zone of thirty each side

Run:  python3 -I two_0s_facing_on_one_surface_check.py
"""
from fractions import Fraction as Fr
from itertools import permutations, product
from math import gcd

WAYS = ("next", "right", "up")


def hand(table):
    total = 0
    for order in permutations(range(3)):
        term = 1
        for i, j in enumerate(order):
            term *= table[i][j]
        if term:
            swaps = sum(1 for x in range(3) for y in range(x + 1, 3) if order[x] > order[y])
            total += term * (-1) ** swaps
    return total


def tables():
    """each way of an other's three own ways lying along a 0's three lines."""
    out = []
    for order in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            table = [[0] * 3 for _ in range(3)]
            for i in range(3):
                table[i][order[i]] = signs[i]
            out.append(table)
    return out


def say(table):
    parts = []
    for i, row in enumerate(table):
        j = next(k for k in range(3) if row[k])
        parts.append(f"its {WAYS[i]} is {'' if row[j] > 0 else 'opposite '}{WAYS[j]}")
    return ", ".join(parts)


def main():
    fails = 0
    print("1  a 0's three own ways and an other's, facing it")
    every = tables()
    kept = [t for t in every if hand(t) > 0]
    facing = [t for t in kept if t[0] == [-1, 0, 0]]
    on_surface = [t for t in facing if abs(t[2][2]) == 1]
    same_side = [t for t in on_surface if t[2][2] == 1]
    print(f"  ways an other's three lie along a 0's three lines: {len(every)}; with one hand: {len(kept)}")
    print(f"  with its next opposite, facing: {len(facing)}; and on the one surface: {len(on_surface)}; and on its one side: {len(same_side)}")
    for t in on_surface:
        opposite = sum(1 for i in range(3) if t[i][i] == -1)
        print(f"    {say(t)}: {opposite} of three opposite")
        fails += opposite != 2
    all_three = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    print(f"  each of three opposite: a hand {'as it was' if hand(all_three) > 0 else 'reversed'}, a mirror")
    own = {(WAYS[i], 1) for i in range(3)}
    t = same_side[0]
    others = {(WAYS[j], t[i][j]) for i in range(3) for j in range(3) if t[i][j]}
    neither = sorted(w for w, s in {(w, -1) for w in WAYS} - (own | others))
    print(f"  own ways of the two on one side: {len(own) + len(others)}; not the same: {len(own | others)}; "
          f"neither's own: opposite {neither[0]}, down")
    fails += (len(kept), len(facing), len(on_surface), len(same_side), len(own | others)) != (24, 4, 2, 1, 5)
    fails += hand(all_three) != -1

    print("\n2  three half turns, each inverting two of three")
    half = {"about up": (-1, -1, 1), "about right": (-1, 1, -1), "about next": (1, -1, -1)}
    same = (1, 1, 1)
    together = lambda a, b: tuple(x * y for x, y in zip(a, b))
    for name, h in half.items():
        print(f"  {name}: next {'opposite' if h[0] < 0 else 'same'}, right {'opposite' if h[1] < 0 else 'same'}, "
              f"up {'opposite' if h[2] < 0 else 'same'}; with its own, same: {together(h, h) == same}")
    names = list(half)
    for a in range(3):
        b, c = (a + 1) % 3, (a + 2) % 3
        ok = together(half[names[a]], half[names[b]]) == half[names[c]]
        print(f"  {names[a]} and {names[b]} together: {names[c]}: {ok}")
        fails += not ok
    all_together = together(together(*list(half.values())[:2]), list(half.values())[2])
    print(f"  the three together: same: {all_together == same}")
    print(f"  a turn about right and then a turn about next is a turn about up: "
          f"{together(half['about right'], half['about next']) == half['about up']}")
    nine_less = all(9 - n == 17 - (n + 8) for n in range(1, 9))
    print(f"  beside it, names 1 to 8: 9 less is 8 up and 17 less together: {nine_less}")
    fails += not nine_less

    print("\n3  two on one line, facing: A going up the numbers, B going down")
    line = range(-12, 13)
    for a, b, when in ((-3, 3, "before a passing"), (3, -3, "after it")):
        a_prior, a_next = {x for x in line if x < a}, {x for x in line if x > a}
        b_prior, b_next = {x for x in line if x > b}, {x for x in line if x < b}
        between = {x for x in line if min(a, b) < x < max(a, b)}
        print(f"  {when}: each one's prior within its other's next: {b_prior <= a_next and a_prior <= b_next}; "
              f"each one's next within its other's prior: {a_next <= b_prior and b_next <= a_prior}")
        print(f"    the between: in both nexts {between <= (a_next & b_next)}; in both priors {between <= (a_prior & b_prior)}")
        if when == "before a passing":
            fails += not (b_prior <= a_next and a_prior <= b_next and between <= (a_next & b_next))
        else:
            fails += not (a_next <= b_prior and b_next <= a_prior and between <= (a_prior & b_prior))
    print("  with a passing, each one's next is its other's prior")

    print("\n4  a passing with priors handed off, and a turning with each its own prior")

    def run(kind, moments=9):
        a = {"at": -4, "going": 1, "prior": ("A's",)}
        b = {"at": 4, "going": -1, "prior": ("B's",)}
        seen = []
        for _ in range(moments):
            a["at"] += a["going"]; b["at"] += b["going"]
            if a["at"] == b["at"]:
                if kind == "passing, priors handed off":
                    a["prior"], b["prior"] = b["prior"], a["prior"]
                else:
                    a["going"], b["going"] = -a["going"], -b["going"]
            seen.append(frozenset((x["at"], x["going"], x["prior"]) for x in (a, b)))
        return seen

    one, two = run("passing, priors handed off"), run("turning, each its own prior")
    print(f"  place, facing and prior of the two, moment by moment, the same in both: {one == two}")
    fails += one != two

    ring = 12

    def round_run(kind, moments=40):
        a = {"at": 0, "going": 1, "prior": "A's", "been": set()}
        b = {"at": 6, "going": -1, "prior": "B's", "been": set()}
        meetings, seen = [], []
        for _ in range(moments):
            for x in (a, b):
                x["at"] = (x["at"] + x["going"]) % ring
                x["been"].add(x["at"])
            if a["at"] == b["at"]:
                meetings.append(a["at"])
                if kind == "passing":
                    a["prior"], b["prior"] = b["prior"], a["prior"]
                else:
                    a["going"], b["going"] = -a["going"], -b["going"]
            seen.append(frozenset((x["at"], x["going"], x["prior"]) for x in (a, b)))
        return seen, meetings, len(a["been"]), len(b["been"])

    s1, m1, a1, b1 = round_run("passing")
    s2, m2, a2, b2 = round_run("turning")
    print(f"  on a line coming round, 12 places: the same in both: {s1 == s2}; meetings in 40 moments: {len(m1)}, at places {sorted(set(m1))}")
    print(f"    passing: each goes the whole round, {a1} and {b1} places; turning: each its own stretch, {a2} and {b2} places")
    fails += s1 != s2 or sorted(set(m1)) != [3, 9]
    print("  on an open line, two alone: one meeting")

    print("\n5  two round one line, opposite ways, at rates p and q: the places of passing")
    for p, q in ((1, 1), (1, 2), (2, 3), (3, 5), (5, 8), (8, 13)):
        places = {Fr(k * p, p + q) % 1 for k in range(p + q)}
        print(f"  rates {p} and {q}: {len(places)} places; from one passing to its next the one goes {Fr(p, p + q)} of the round "
              f"and the other {Fr(q, p + q)}, and the place moves on {Fr(p, p + q)}")
        fails += len(places) != (p + q) // gcd(p, q)
    print("  the places are p and q together, each next count its prior two together")
    print("  the place moves on toward 0.3819... of a round, 137.5... of 360, with φ; with a ratio of no two whole numbers no place is twice")

    print("\n6  a zone of thirty each side: six same ones around a 0, sixty apart")
    lines = [60 * k for k in range(6)]

    def nearest(heading):
        apart = lambda x: min((heading - x) % 360, (x - heading) % 360)
        least = min(apart(x) for x in lines)
        return [x for x in lines if apart(x) == least]

    zone = [h for h in range(-90, 91) if nearest(h % 360) == [0]]
    right = [h for h in range(-90, 91) if nearest(h % 360) == [60]]
    left = [h for h in range(-90, 91) if nearest(h % 360) == [300]]
    two = [h for h in range(-90, 91) if len(nearest(h % 360)) == 2]
    print(f"  headings from {zone[0]} to {zone[-1]}: the one ahead, 0; from {right[0]} to {right[-1]}: an other, +1; from {left[0]} to {left[-1]}: an other, −1")
    print(f"  at {two}: two as near, neither")
    fails += (zone[0], zone[-1]) != (-29, 29) or two != [-90, -30, 30, 90]

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
