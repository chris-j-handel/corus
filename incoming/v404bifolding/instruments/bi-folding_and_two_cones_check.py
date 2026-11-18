"""Bi-folding by folding, and two cones crossing at an empty 0, by whole numbers.

1. Folding 1 to 16 at its middle, 17 less, and again at its half's middle,
   9 less: which numbers lie together, and whether a move of 8 is the two
   folds together. The middle eight, 5 to 12, folded by 17 less and 13 less.
2. Natural Intelligence's right spiral step, each parity one place along and
   the first coming round inverted, with three parities as a cube's eight
   corners: the loop of two at the long diagonal's two ends, each the apex
   of a cone of itself and the three forms one parity apart from it, and the
   loop of six, going one and then the other cone's base.
3. The same step with 1 to 8 parities, each form placed in the plane of the
   slowest spiraling: its distance from that plane's 0 for each loop, and
   which forms lie at the 0 itself.
4. A corner of a surface of flat faces, as a cone: what its faces leave
   short of a whole round, for a cube, a tetrahedron and an octahedron.

It reads no file and writes none.

Run:  python3 -I incoming/v404bifolding/instruments/bi-folding_and_two_cones_check.py
"""
from cmath import exp, pi
from itertools import product

LIVING_BI_FOLDINGS = [{1, 9, 8, 16}, {2, 15, 7, 10}, {3, 11, 6, 14}, {4, 13, 5, 12}]
LIVING_MIDDLE = [{9, 5, 12, 8}, {7, 11, 6, 10}]


def fold(numbers):
    """Fold a strip at its middle: each first-half number lies on its podal."""
    half = len(numbers) // 2
    return [[numbers[i], numbers[-1 - i]] for i in range(half)]


def fold_again(layers):
    """Fold a strip of layers at its middle: two layers lie as one."""
    half = len(layers) // 2
    return [sorted(layers[i] + layers[-1 - i]) for i in range(half)]


def part_one():
    print("1. Folding 1 to 16")
    four = fold_again(fold(list(range(1, 17))))
    print("   lying together after two folds:", four)
    print("   each is a living bi-folding:", sorted(map(sorted, four)) == sorted(map(sorted, LIVING_BI_FOLDINGS)))
    print("   17 less after 9 less is 8 up, for 1 to 8:", all(17 - (9 - n) == n + 8 for n in range(1, 9)))
    print("   9 less after 17 less is 8 down, for 9 to 16:", all(9 - (17 - n) == n - 8 for n in range(9, 17)))
    middle = fold_again(fold(list(range(5, 13))))
    print("   the middle eight, 5 to 12, after two folds:", middle)
    print("   each is a living middle bi-folding:", sorted(map(sorted, middle)) == sorted(map(sorted, LIVING_MIDDLE)))
    print("   17 less after 13 less is 4 up, for 5 to 8:", all(17 - (13 - n) == n + 4 for n in range(5, 9)))
    place = {n: exp(2j * pi * (n - 0.5) / 16) for n in range(1, 17)}
    axis_17 = all(abs(place[17 - n] - place[n].conjugate()) < 1e-9 for n in range(1, 17))
    axis_9 = all(abs(place[(9 - n - 1) % 16 + 1] + place[n].conjugate()) < 1e-9 for n in range(1, 17))
    print("   1 to 16 as a circle: 17 less inverts across one axis:", axis_17,
          "; 9 less across the axis orthogonal to it:", axis_9)
    half = all(abs(place[(n + 7) % 16 + 1] + place[n]) < 1e-9 for n in range(1, 17))
    print("   the two together, 8 up round the circle, carry each place to its opposite:", half)
    bits = lambda n: n - 1
    print("   names as n - 1 in binary: 17 less inverts all four parities:",
          all(bits(17 - n) == bits(n) ^ 0b1111 for n in range(1, 17)))
    print("   8 up or down inverts the parity of now and next alone:",
          all(bits((n + 7) % 16 + 1) == bits(n) ^ 0b1000 for n in range(1, 17)))
    print("   9 less, for 1 to 8, inverts the other three:", all(bits(9 - n) == bits(n) ^ 0b0111 for n in range(1, 9)))
    print("   the pairs of 9 less, in binary:", [(format(bits(n), '03b'), format(bits(9 - n), '03b')) for n in range(1, 5)])


def step(form):
    """Each parity one place along, the first coming round inverted."""
    return form[1:] + (-form[0],)


def show(form):
    return "".join("+" if p > 0 else "-" for p in form)


def loops(n):
    seen, found = set(), []
    for start in product((1, -1), repeat=n):
        if start in seen:
            continue
        loop, form = [], start
        while form not in seen:
            seen.add(form)
            loop.append(form)
            form = step(form)
        found.append(loop)
    return found


def apart(a, b):
    return sum(x != y for x, y in zip(a, b))


def part_two():
    print("2. Three parities, a cube's eight corners")
    six = next(l for l in loops(3) if len(l) == 6)
    two = next(l for l in loops(3) if len(l) == 2)
    print("   the loop of two:", [show(f) for f in two], "parities apart:", apart(*two))
    cones = {show(a): [b for b in six if apart(a, b) == 1] for a in two}
    for apex, base in cones.items():
        print("   cone of apex", apex, "its base:", [show(b) for b in base])
    which = [next(a for a, base in cones.items() if f in base) for f in six]
    print("   the loop of six:", [show(f) for f in six])
    print("   its forms' apexes in order:", which)
    print("   one and then the other cone, each step:", all(which[i] != which[(i + 1) % 6] for i in range(6)))
    print("   each step one parity:", all(apart(six[i], six[(i + 1) % 6]) == 1 for i in range(6)))


def placed(form):
    """The form in the plane of the slowest spiraling, a whole number pair at no scale."""
    n = len(form)
    w = exp(1j * pi / n)
    return sum(p * w ** k for k, p in enumerate(form))


def part_three():
    print("3. One to eight parities, each loop's distance from the plane's 0")
    for n in range(1, 9):
        rows = []
        for loop in loops(n):
            r = abs(placed(loop[0]))
            same = all(abs(abs(placed(f)) - r) < 1e-9 for f in loop)
            rows.append((len(loop), round(r, 3), same))
        at_zero = [(size, r) for size, r, _ in rows if r < 1e-9]
        sizes = sorted(size for size, _, _ in rows)
        print(f"   {n}: loops {sizes}; at the 0: {len(at_zero)} loop(s) of {[s for s, _ in at_zero]}; "
              f"each loop at one distance: {all(s for _, _, s in rows)}")
    for n in (2, 3, 5):
        f = tuple([1] * n)
        a, b = placed(f), placed(step(f))
        print(f"   {n}: each step moves a form 1/{2 * n} of a round the one way:",
              abs(b - a * exp(-1j * pi / n)) < 1e-9)


def part_four():
    print("4. A corner as a cone: what its faces leave short of 360")
    for name, faces_at_corner, face_angle, corners in (
        ("cube", 3, 90, 8), ("tetrahedron", 3, 60, 4), ("octahedron", 4, 60, 6)):
        short = 360 - faces_at_corner * face_angle
        print(f"   {name}: each corner {faces_at_corner * face_angle}, short {short}; all {corners} corners short {short * corners}")


if __name__ == "__main__":
    part_one()
    part_two()
    part_three()
    part_four()
