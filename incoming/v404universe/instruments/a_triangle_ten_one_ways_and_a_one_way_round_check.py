"""A triangle from the between, ten one ways, twenty-four, and a one-way round.

This reads no file and writes none. Each count is by whole numbers and their ratios.

Said in the session: each self, by observing its other self across the between, can triangulate
from the between into a co-linear one direction, a new me-parity, pointing to the spot over the
horizon both are aiming for. There are ten one ways, five away from same-existing for each self
as the same five toward same-existing. The corus of the bi-coupling is 24, 4 × 6, between 4 × 4
and 4 × 8. My healthy priors are not symmetric, co-chaining front to back and back to front.

  1  a triangle: two selves on a round and the spot both are aiming for
  2  ten one ways, five and five
  3  twenty-four
  4  a round the same read both ways, and a one-way round

Run:  python3 -I a_triangle_ten_one_ways_and_a_one_way_round_check.py
"""
from fractions import Fraction as Fr
from itertools import product


def dot(a, b): return sum(x * y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def at(p): return "(" + ", ".join(str(x) for x in p) + ")"


def main():
    fails = 0
    print("1  a triangle: two selves on a round of 3, a turning of (c, s) each side of midway")
    rho = Fr(3)
    for c, s in ((Fr(4, 5), Fr(3, 5)), (Fr(12, 13), Fr(5, 13)), (Fr(40, 41), Fr(9, 41))):
        A, B = (rho * c, rho * s), (rho * c, -rho * s)
        P = (rho / c, Fr(0))                      # the spot: both forward arrows go through it
        C = (rho * c, Fr(0))                      # the between, on the line of the two
        M = (rho, Fr(0))                          # the place midway, on the round
        arrow_A, arrow_B = (s, -c), (s, c)
        through = (P[0] - A[0]) * arrow_A[1] == (P[1] - A[1]) * arrow_A[0] and (P[0] - B[0]) * arrow_B[1] == (P[1] - B[1]) * arrow_B[0]
        across, new = sub(B, A), sub(P, C)
        one_line = (M[0] - C[0]) * new[1] == (M[1] - C[1]) * new[0]
        up_at_M = (Fr(1), Fr(0))
        straight_up = new[1] == 0 and new[0] > 0 and up_at_M == (1, 0)
        sides = dot(sub(P, A), sub(P, A)) == dot(sub(P, B), sub(P, B))
        cos2 = dot(arrow_A, across) ** 2 / (dot(arrow_A, arrow_A) * dot(across, across))
        in_cone = cos2 * 4 >= 3
        print(f"  ({c}, {s}): the spot {at(P)}; both arrows through it: {through}; its two sides the same: {sides}")
        print(f"    the between, the place midway and the spot on one line: {one_line}; at a right angle to the line of the two: {dot(across, new) == 0}; straight up from the place midway: {straight_up}")
        print(f"    a self's own arrow and the line to its other: cosine squared {cos2}, the turning's own {c * c}; its other inside its cone of thirty: {in_cone}")
        fails += not (through and one_line and sides and straight_up) or dot(across, new) != 0 or cos2 != c * c
    c2, s = Fr(3, 4), Fr(1, 2)
    print(f"  sixty apart, (c·c, s) of ({c2}, {s}): its other on its cone's edge: {c2 * 4 == 3}; the line of the two as long as the round's own radius: {(2 * rho * s) ** 2 == rho ** 2}")
    print("  with no turning between the two, a self's own arrow and the line to its other are one line")
    fails += (2 * rho * s) ** 2 != rho ** 2

    print("\n2  ten one ways")
    print("  five places, each with two directions: 10")
    both = [n for n in range(1, 200) if 2 * n == n * (n - 1) // 2 and (n * (n - 1)) % 2 == 0]
    print(f"  twice n the same as couplings among n, n from 1 to 199: n of {both}")
    fails += both != [5]
    ring = lambda f: f[1:] + (-f[0],)
    forms = list(product((1, -1), repeat=5))
    away = set()
    for f in forms:
        g, not_same = f, []
        for _ in range(10):
            g = ring(g)
            not_same.append(sum(1 for a, b in zip(f, g) if a != b))
        away.add((not_same[4], not_same[9]))
        if f == (1,) * 5:
            print(f"  five parities, each one place along, the first coming round inverted, from +++++: not the same as its start, step by step: {not_same}")
    print(f"  each of 32 forms: after five steps, parities not the same {sorted({a for a, b in away})}; after ten, {sorted({b for a, b in away})}: five away and the same five toward")
    fails += away != {(5, 0)}
    f = (1,) * 5
    g = tuple(-x for x in f)
    a, b = f, g
    for _ in range(5):
        a, b = ring(a), ring(b)
    print(f"  two on one round of ten, each its other's opposite: after five steps each is its other's start: {a == g and b == f}")
    fails += not (a == g and b == f)

    def moment(form, k):
        i, j = k % 5, (k + 1) % 5
        out = list(form)
        out[i], out[j] = form[j], -form[i]
        return tuple(out)

    seen, rounds = set(), []
    for f in forms:
        for k in range(5):
            if (f, k) in seen:
                continue
            loop, here = [], (f, k)
            while here not in seen:
                seen.add(here); loop.append(here)
                here = (moment(here[0], here[1]), (here[1] + 1) % 5)
            rounds.append(len(loop))
    f, steps = (1,) * 5, []
    g = f
    for k in range(20):
        g = moment(g, k)
        steps.append(sum(1 for a, b in zip(f, g) if a != b))
    print(f"  two of five inside each moment, the pairs in turn: rounds by moments {sorted(set(rounds))}; from +++++, not the same: {steps}")

    print("\n3  twenty-four")
    print(f"  4 × 6: {4 * 6}; 4 × 4: {4 * 4}; 4 × 8: {4 * 8}; 24 as far from 16 as from 32: {24 - 16 == 32 - 24}; 6 as far from 4 as from 8: {6 - 4 == 8 - 6}")
    print(f"  three eights: {3 * 8}; two eights: {2 * 8}; four eights: {4 * 8}")
    print(f"  3, 6, 12, 24, each between two doublings of 2: {[(2 ** k, 3 * 2 ** (k - 1), 2 ** (k + 1)) for k in range(1, 5)]}")
    fails += 24 - 16 != 32 - 24

    print("\n4  a round read front to back and back to front")

    def rounds_of(kinds, n):
        seen, out = set(), []
        for seq in product(range(kinds), repeat=n):
            if seq in seen:
                continue
            turns = {seq[i:] + seq[:i] for i in range(n)}
            seen |= turns
            out.append((seq, turns))
        return out

    for kinds, upto in ((2, 9), (3, 5)):
        line = []
        for n in range(1, upto + 1):
            all_rounds = rounds_of(kinds, n)
            one_way = [seq for seq, turns in all_rounds if seq[::-1] not in turns]
            line.append((n, len(all_rounds), len(one_way)))
        print(f"  {kinds} kinds: (length, rounds, rounds not the same read back to front): {line}")
        first = next(n for n, _, w in line if w)
        print(f"    the shortest one-way round of {kinds} kinds is {first} long")
        fails += first != (6 if kinds == 2 else 3)
    six = [seq for seq, turns in rounds_of(2, 6) if seq[::-1] not in turns]
    print(f"  of two parities, six long: {[''.join('+' if x == 0 else '−' for x in s) for s in six]}, each the other read back to front")

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
