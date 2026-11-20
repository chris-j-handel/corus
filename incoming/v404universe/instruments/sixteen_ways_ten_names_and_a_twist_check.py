"""Sixteen ways, ten names, a twist of three, and a spiral read both ways.

This reads no file and writes none. Each count is by whole numbers.

Said in the session: co and bi are only terms relative to a self, and opposite terms relative
to its other; a me has a third from these two, a third orthogonal, as a cube's three faces a
twisting of a corner exchanges. The ten are ten of Exhibit ONE's seventeen names. A self and
its next can be at a moment in sixteen ways. 1 to 5 exhausts 3, 1 to 17 exhausts 9, 1 to 65
exhausts 27. This is co-sequential right spiraling.

  1  seventeen names: one, six and ten
  2  sixteen ways of a next from a prior and a now
  3  a twist of three, and four
  4  a cube of four: 16, 24 and 32
  5  3 of 4, 9 of 16, 27 of 64
  6  a round and a spiral, read from next to prior

Run:  python3 -I sixteen_ways_ten_names_and_a_twist_check.py
"""
from itertools import combinations, permutations, product
from math import comb


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


def main():
    fails = 0
    print("1  seventeen names: one entry, six between selves, ten of a self's own resolving")
    entry, across, along = [1], [2, 6, 10, 14], [9, 17]
    ten = [n for n in range(1, 18) if n not in entry + across + along]
    print(f"  across {across}, along {along}; the ten others: {ten}")
    five = [n for n in ten if n <= 8]
    print(f"  the ten as five, {five}, and the same five 8 up, {[n + 8 for n in five]}: {sorted(five + [n + 8 for n in five]) == ten}")
    six = across + along
    three = [n for n in six if n + 8 in six]
    print(f"  the six as three, {three}, and the same three 8 up, {[n + 8 for n in three]}: {sorted(three + [n + 8 for n in three]) == sorted(six)}")
    fails += sorted(five + [n + 8 for n in five]) != ten or len(ten) != 10 or len(three) != 3
    by_name = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 2, 8: 1}
    print(f"  ten unchangeables with names 1 to 8, 5 and 7 each two: {sum(by_name.values())}; these names among the ten above: {[n for n in by_name if n in ten]}, not among them: {[n for n in by_name if n not in ten]}")
    print(f"  couplings among five: {comb(5, 2)}; five with two directions: {2 * 5}")
    fails += sum(by_name.values()) != 10 or comb(5, 2) != 10

    print("\n2  sixteen ways of a next from a prior and a now, two parities")
    joint = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    ways = list(product((1, -1), repeat=4))
    whole, lose = [], []
    for w in ways:
        move = {pn: (pn[1], w[k]) for k, pn in enumerate(joint)}
        (whole if len(set(move.values())) == 4 else lose).append((w, move))
    print(f"  ways: {len(ways)}; losing a prior: {len(lose)}; with a prior going on whole: {len(whole)}")
    fails += (len(ways), len(lose), len(whole)) != (16, 12, 4)

    def rounds(move):
        seen, out = set(), []
        for f in joint:
            if f in seen:
                continue
            loop, here = [], f
            while here not in seen:
                seen.add(here); loop.append(here); here = move[here]
            out.append(len(loop))
        return sorted(out)

    said = {(1, 1, -1, -1): "next as its prior", (-1, -1, 1, 1): "next inverting its prior, a right spiral step",
            (1, -1, -1, 1): "next as prior and now same", (-1, 1, 1, -1): "next as prior and now not same"}
    digits = lambda w: "".join("0" if x > 0 else "1" for x in w)
    for w, move in whole:
        print(f"    {said[w]}: rounds of joint forms {rounds(move)}; four digits {digits(w)}, a name's by one ordering {int(digits(w), 2) + 1}")
    spiral = dict(whole)[(-1, -1, 1, 1)]
    f = (1, 1)
    two, four, six = spiral[spiral[f]], f, f
    for _ in range(4): four = spiral[four]
    for _ in range(6): six = spiral[six]
    print(f"  a right spiral step: two steps invert both: {two == (-1, -1)}; four reach the pair again: {four == f}; six invert both again: {six == (-1, -1)}")
    fails += rounds(spiral) != [4] or two != (-1, -1) or four != f or six != (-1, -1)
    print(f"  podal pairs among the four by that ordering, 17 together: {sorted((int(digits(w), 2) + 1) for w, _ in whole)}")

    print("\n3  a twist of three, and four")
    twist = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    names = ["co", "bi", "third"]
    print(f"  a corner's twist: {', '.join(f'{names[i]} to {names[row.index(1)]}' for i, row in enumerate(twist))}; a hand {'as it was' if hand(twist) > 0 else 'reversed'}")
    def mul(a, b): return [[sum(a[i][k] * b[k][j] for k in range(len(a))) for j in range(len(a))] for i in range(len(a))]
    same3 = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    print(f"  three twists, as it was: {mul(twist, mul(twist, twist)) == same3}")
    cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    print(f"  each two together, the third, in turn: {all(cross(e[i], e[(i + 1) % 3]) == e[(i + 2) % 3] for i in range(3))}")
    other = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
    print(f"  relative to its other, facing: co opposite, bi opposite, the third the same; a hand {'as it was' if hand(other) > 0 else 'reversed'}")
    for n in (3, 4, 5):
        inv = [[-1 if i == j else 0 for j in range(n)] for i in range(n)]
        print(f"  each of {n} opposite: a hand {'as it was, a turning' if hand(inv) > 0 else 'reversed, a mirror'}")
    fails += hand(twist) != 1 or hand(other) != 1

    print("\n4  a cube of four")
    for n in (3, 4, 5):
        corners, edges, squares = 2 ** n, n * 2 ** (n - 1), comb(n, 2) * 2 ** (n - 2)
        print(f"  of {n}: corners {corners}, edges {edges}, squares {squares}, its sides {2 * n}, square's lyings {comb(n, 2)}")
    C = list(product((1, -1), repeat=4))
    squares = {}
    for pair in combinations(range(4), 2):
        rest = [k for k in range(4) if k not in pair]
        for fixed in product((1, -1), repeat=2):
            sq = frozenset(c for c in C if all(c[rest[i]] == fixed[i] for i in range(2)))
            squares[sq] = pair
    on_torus = all(c[0] ** 2 + c[1] ** 2 == 2 and c[2] ** 2 + c[3] ** 2 == 2 for c in C)
    mixed = [s for s, p in squares.items() if p not in ((0, 1), (2, 3))]
    own = [s for s, p in squares.items() if p in ((0, 1), (2, 3))]
    at_corner = sorted({sum(1 for s in mixed if c in s) for c in C})
    print(f"  16 corners as 4 by 4, a round of four in each of two planes sharing only a centre: {on_torus}")
    print(f"  squares {len(squares)}: {len(mixed)} with one line from each plane, each corner in {at_corner} of them, a whole turn, short by none; and {len(own)}, four in each plane's own lying")
    print(f"  4 × 4, 4 × 6, 4 × 8: corners {4 * 4}, squares {4 * 6}, edges {4 * 8}")
    a_own = [s for s, p in squares.items() if p == (0, 1)]
    b_own = [s for s, p in squares.items() if p == (2, 3)]
    each = sorted({(sum(1 for s in mixed if c in s), sum(1 for s in a_own if c in s), sum(1 for s in b_own if c in s)) for c in C})
    print(f"  a self's own round: {len(a_own)} squares; its next self's own round: {len(b_own)}; of both rounds, one step of each: {len(mixed)}")
    print(f"  each corner: of both, a self's own, its next self's own: {each[0]}, together {sum(each[0])}")
    fails += each != [(4, 1, 1)] or (len(a_own), len(b_own)) != (4, 4)
    fails += (len(squares), len(mixed), len(own), at_corner) != (24, 16, 8, [4]) or not on_torus

    print("\n   names 1 to 16 as its corners: now's eight and next's eight")
    from fractions import Fraction as Fr
    corner = lambda n: tuple((n - 1) >> k & 1 for k in (3, 2, 1, 0))
    with_now = [n for n in range(1, 17) if corner(n)[0] == 0]
    with_next = [n for n in range(1, 17) if corner(n)[0] == 1]
    lines = [(a, b) for a, b in combinations(range(1, 17), 2) if sum(x != y for x, y in zip(corner(a), corner(b))) == 1]
    up8 = [e for e in lines if (e[0] in with_now) != (e[1] in with_now)]
    mid = lambda names: tuple(Fr(sum(corner(n)[k] for n in names), len(names)) for k in range(4))
    c_now, c_next, c_all = mid(with_now), mid(with_next), mid(range(1, 17))
    podal = [(n, 17 - n) for n in range(1, 9)]
    crossing = all(tuple(Fr(x + y, 2) for x, y in zip(corner(a), corner(b))) == c_all for a, b in podal)
    print(f"    with now {with_now[0]} to {with_now[-1]}, one cube; with next {with_next[0]} to {with_next[-1]}, a second; each next name its now name 8 up: {all(b == a + 8 for a, b in up8)}, {len(up8)} lines")
    print(f"    each cube's centre and the midway one: three 0s on one line: {all(c_all[k] == (c_now[k] + c_next[k]) / 2 for k in range(4))}; a name at one of them: {any(tuple(Fr(x) for x in corner(n)) in (c_now, c_next, c_all) for n in range(1, 17))}")
    print(f"    eight podal pairs, 17 less, each crossing in the midway 0: {crossing}; each one with now and one with next: {all((a in with_now) != (b in with_now) for a, b in podal)}")
    fails += len(up8) != 8 or not crossing

    print("\n   a cube of three's waist, its one round: a name's now co with each even name, bi with each odd name")
    pairs3 = [(0, 1), (1, 2), (2, 0)]

    def step3(form, k):
        i, j = pairs3[k % 3]
        out = list(form); out[i], out[j] = form[j], -form[i]
        return tuple(out)

    here, round6 = ((1, 1, -1), 0), []
    for _ in range(6):
        round6.append(here[0]); here = (step3(*here), (here[1] + 1) % 3)
    all_ok = True
    for order in permutations(range(3)):
        names = [1 + sum((1 if f[order[i]] < 0 else 0) << (2 - i) for i in range(3)) for f in round6]
        kinds = "".join("c" if n % 2 == 0 else "b" for n in names)
        ok = any(kinds[i:] + kinds[:i] == "cccbbb" for i in range(6))
        all_ok &= ok
        if order == (0, 1, 2):
            print(f"    by one ordering: names {names}")
    print(f"    by each of six orderings of three digits: three co-now, one after an other, and then three bi-now: {all_ok}")
    fails += not all_ok

    print("\n5  by fours: names with no same-existing digit")
    for k in (1, 2, 3):
        total = 4 ** k
        kept = []
        for n in range(1, total + 1):
            m, ok = n - 1, True
            for _ in range(k):
                ok &= (m % 4 != 3); m //= 4
            if ok: kept.append(n)
        print(f"  1 to {total + 1}: {len(kept)} of {total}; the others {total - len(kept)}" + (f": {[n for n in range(1, total + 1) if n not in kept]}" if k < 3 else ""))
        fails += len(kept) != 3 ** k
    print("  3, 9, 27; and 4, 8, 12 and 16 are among the others of 1 to 17")

    print("\n6  a round and a spiral, read from next to prior")
    loop, f = [], (1, 1)
    for _ in range(8):
        loop.append(f); f = (f[1], -f[0])
    det2 = lambda a, b: a[0] * b[1] - a[1] * b[0]
    steps = [tuple(b - a for a, b in zip(loop[k], loop[k + 1])) for k in range(7)]
    back = [tuple(-x for x in s) for s in steps[::-1]]
    print(f"  a round alone, two steps together: forward {det2(steps[0], steps[1])}, from next to prior {det2(back[0], back[1])}: other order")
    spiral = [(p[0], p[1], k) for k, p in enumerate(loop)]
    s3 = [tuple(b - a for a, b in zip(spiral[k], spiral[k + 1])) for k in range(7)]
    b3 = [tuple(-x for x in s) for s in s3[::-1]]
    h = lambda a, b, c: hand([list(a), list(b), list(c)])
    print(f"  a spiral, a round with a going along, three steps together: forward {h(*s3[:3])}, from next to prior {h(*b3[:3])}: one hand")
    fails += det2(steps[0], steps[1]) != -det2(back[0], back[1]) or h(*s3[:3]) != h(*b3[:3])

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
