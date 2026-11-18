"""Of three parities, two inside each moment.

This reads no file and writes none. Each count is by whole numbers.

Said in the session: only two parities are inside each moment, co-sequentially among the three.
Two readings are executed, each a reading and no more.

  1  the pairs in turn, each pair a right spiral step of its two, (a, b) to (b, −a)
  2  Natural Intelligence's "Each next number is its prior two together", as parities

Beside them, the step of each of three at once, the first coming round inverted.

Run:  python3 -I two_of_three_inside_each_moment_check.py
"""
from itertools import permutations, product

PAIRS = [(0, 1), (1, 2), (2, 0)]
FORMS = list(product((1, -1), repeat=3))


def show(form):
    return "".join("+" if p > 0 else "−" for p in form)


def name(form):
    """names 1 to 8 as n − 1 in binary, + as 0 and − as 1."""
    return 1 + sum((1 if p < 0 else 0) << (2 - i) for i, p in enumerate(form))


def moment(form, k):
    i, j = PAIRS[k % 3]
    out = list(form)
    out[i], out[j] = form[j], -form[i]
    return tuple(out)


def hand(table):
    n, total = len(table), 0
    for order in permutations(range(n)):
        term = 1
        for i, j in enumerate(order):
            term *= table[i][j]
        if term:
            swaps = sum(1 for x in range(n) for y in range(x + 1, n) if order[x] > order[y])
            total += term * (-1) ** swaps
    return total


def table_of(k):
    i, j = PAIRS[k]
    table = [[1 if r == c else 0 for c in range(3)] for r in range(3)]
    table[i] = [0, 0, 0]; table[j] = [0, 0, 0]
    table[i][j] = 1; table[j][i] = -1
    return table


def main():
    fails = 0
    print("1  the pairs in turn, each a right spiral step of its two")
    changing = sorted({sum(1 for a, b in zip(f, moment(f, k)) if a != b) for f in FORMS for k in range(3)})
    print(f"  parities changing with each moment: {changing}")
    hands = [hand(table_of(k)) for k in range(3)]
    print(f"  a hand with each moment: {['as it was' if h > 0 else 'reversed' for h in hands]}")
    fails += changing != [1] or hands != [1, 1, 1]
    print(f"  the third, inside no moment, moment by moment: {[next(x for x in range(3) if x not in PAIRS[k % 3]) for k in range(6)]}")

    seen, loops = set(), []
    for f in FORMS:
        for k in range(3):
            if (f, k) in seen:
                continue
            loop, at = [], (f, k)
            while at not in seen:
                seen.add(at); loop.append(at)
                at = (moment(at[0], at[1]), (at[1] + 1) % 3)
            loops.append(loop)
    print(f"  rounds, by moments: {sorted(len(l) for l in loops)}")
    for loop in loops:
        print("    " + "  ".join(f"{show(f)} {name(f)}" for f, _ in loop))

    steps = {}
    for loop in loops:
        for x in range(len(loop)):
            a, b = loop[x][0], loop[(x + 1) % len(loop)][0]
            steps[(a, b)] = steps.get((a, b), 0) + 1
    edges = {frozenset(s) for s in steps}
    both = [e for e in edges if all(s in steps for s in (tuple(e), tuple(e)[::-1]))]
    one = [e for e in edges if e not in both]
    top, bottom = (1, 1, 1), (-1, -1, -1)
    print(f"  a cube's edges gone along: {len(edges)} of 12")
    print(f"    both ways: {len(both)}, each with {show(top)} or {show(bottom)}: {all(top in e or bottom in e for e in both)}")
    print(f"    one way only: {len(one)}, none with {show(top)} or {show(bottom)}: {all(top not in e and bottom not in e for e in one)}")
    near_top = {f for f in FORMS if sum(1 for p in f if p < 0) == 1}
    up = sum(1 for (a, b) in steps if frozenset((a, b)) in one and a in near_top)
    down = sum(1 for (a, b) in steps if frozenset((a, b)) in one and b in near_top)
    print(f"    of the six one way: {up} from {show(top)}'s three to {show(bottom)}'s three, {down} from {show(bottom)}'s three to {show(top)}'s")
    fails += (len(edges), len(both), len(one), up, down) != (12, 6, 6, 3, 3)
    print("  names: 1's three are 2, 3 and 5; 8's three are 4, 6 and 7; the round of six is the six others")

    print("\n2  each next its prior two together, as parities")
    numbers = [1, 1]
    while len(numbers) < 13:
        numbers.append(numbers[-1] + numbers[-2])
    kinds = ["odd" if n % 2 else "even" for n in numbers]
    print(f"  {numbers}")
    print(f"  {kinds}")
    fails += kinds != ["odd", "odd", "even"] * 4 + ["odd"]
    windows = []
    for i in range(3):
        windows.append((kinds[i], kinds[i + 1], kinds[i + 2]))
    for a, b, c in windows:
        print(f"    inside a moment: {a} and {b}; their two together, the third: {c}")
    print("  three round: each of the three is the third once, and with two odd inside, the third is even, nought by two")
    print("  even and even together are even: not moving")

    print("\nbeside them: each of three at once, the first coming round inverted")
    ring = lambda f: f[1:] + (-f[0],)
    table = [[0, 1, 0], [0, 0, 1], [-1, 0, 0]]
    print(f"  a hand: {'as it was' if hand(table) > 0 else 'reversed'}")
    seen, found = set(), []
    for f in FORMS:
        if f in seen:
            continue
        loop, at = [], f
        while at not in seen:
            seen.add(at); loop.append(at); at = ring(at)
        found.append(loop)
    for loop in sorted(found, key=len):
        print(f"  a round of {len(loop)}: " + "  ".join(f"{show(f)} {name(f)}" for f in loop))
    two = sorted(name(f) for f in min(found, key=len))
    fails += hand(table) != -1 or two != [3, 6]
    print(f"  its round of two is names {two[0]} and {two[1]}")

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
