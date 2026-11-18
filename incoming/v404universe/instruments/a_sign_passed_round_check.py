"""A right spiral step on two parities, three, and more, by whole numbers.

Natural Intelligence has a right spiral step of two parities: a pair (x, y)
going to (y, -x) with each moment. Each parity moves one place along, and the
first comes round to the last place inverted.

This instrument does the same step with three parities and with more, and
says which loops the forms part into, and how many parities change with each
step. It also tries Natural Mathematics' round of eight, inverting parity
0, 1, 0, 2, 0, 1, 0, 2, and two loops of six each stepping at its own rate.

It reads no file and writes none.

Run:  python3 -I incoming/v404universe/instruments/a_sign_passed_round_check.py
"""
from itertools import product
from math import gcd


def step(form):
    """Each parity one place along, the first coming round inverted."""
    return form[1:] + (-form[0],)


def show(form):
    return "".join("+" if p > 0 else "-" for p in form)


def loops(n):
    seen, found = set(), []
    for form in product((1, -1), repeat=n):
        if form in seen:
            continue
        loop, at = [], form
        while at not in seen:
            seen.add(at)
            loop.append(at)
            at = step(at)
        found.append(loop)
    return sorted(found, key=len, reverse=True)


def changes(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]


def main():
    print("a right spiral step: each parity one place along, the first coming round inverted")
    for n in (2, 3, 4, 5):
        found = loops(n)
        print(f"\n{n} parities, {2 ** n} forms, loops of {[len(l) for l in found]}")
        if n > 3:
            continue
        for loop in found:
            line, places = [], []
            for i, form in enumerate(loop):
                nxt = loop[(i + 1) % len(loop)]
                line.append(show(form))
                places.append(changes(form, nxt))
            each = sorted({len(p) for p in places})
            print(f"  loop of {len(loop)}: {' '.join(line)}")
            print(f"    parities changing with each step: {each}")
            if each == [1]:
                print(f"    the place changing, step by step: {[p[0] for p in places]}")
            if len(loop) == 2:
                opposite = all(a == -b for a, b in zip(loop[0], loop[1]))
                print(f"    each form its other's opposite: {opposite}")

    print("\nNatural Mathematics' round of eight, inverting parity 0, 1, 0, 2, 0, 1, 0, 2")
    form, reached = [1, 1, 1], []
    for place in (0, 1, 0, 2, 0, 1, 0, 2):
        reached.append(tuple(form))
        form[place] = -form[place]
    print(f"  forms reached: {len(set(reached))} of 8, and at its start again: {tuple(form) == reached[0]}")

    print("\ntwo loops of six, the one stepping once each p moments and the other once each q,")
    print("p and q two numbers one after one of 1, 1, 2, 3, 5, 8, 13, 21, 34:")
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    for p, q in zip(fib, fib[1:]):
        together = 6 * p * q // gcd(p, q)
        print(f"  each {p} and each {q}: both at their start again after {together} moments, q over p {q / p:.4f}")
    print("  each pair of whole numbers comes round together, later with each pair;")
    print("  q over p goes toward 1.6180..., a ratio of no two whole numbers, and with it")
    print("  no whole number of moments is tried here, there being none.")
    print("\nthree parities, three other steps, beside the right spiral step")
    forms = list(product((1, -1), repeat=3))

    def loops_of(move):
        seen, found = set(), []
        for form in forms:
            if form in seen:
                continue
            loop, at = [], form
            while at not in seen:
                seen.add(at)
                loop.append(at)
                at = move(at)
            found.append(len(loop))
        return sorted(found, reverse=True)

    round_only = lambda f: f[1:] + (f[0],)
    print(f"  each parity one place along, the first coming round as it is: loops of {loops_of(round_only)}")
    still = [show(f) for f in forms if round_only(f) == f]
    print(f"    forms not moving: {still}")
    moved = sorted({len(changes(f, round_only(f))) for f in forms if round_only(f) != f})
    print(f"    parities changing with each step of a loop of three: {moved}")
    plus_in = lambda f: f[1:] + (1,)
    reached = {plus_in(f) for f in forms}
    print(f"  each parity one place along, the first away and a + brought in: {len(forms)} forms go to {len(reached)}")
    print("    two forms to one: a prior is away")

    print("\na hand, by the count of parities: the right spiral step as a turning of places and one inverting")
    from itertools import permutations

    def hand_of(n):
        """the step as a table of n by n, and its determinant by each ordering of n."""
        table = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            table[i][i + 1] = 1
        table[n - 1][0] = -1
        total = 0
        for order in permutations(range(n)):
            term = 1
            for i, j in enumerate(order):
                term *= table[i][j]
            if term:
                swaps = sum(1 for x in range(n) for y in range(x + 1, n) if order[x] > order[y])
                total += term * (-1) ** swaps
        return total

    for n in range(1, 7):
        print(f"  {n} parities: {'a hand as it was' if hand_of(n) > 0 else 'a hand reversed'}")


if __name__ == "__main__":
    main()
