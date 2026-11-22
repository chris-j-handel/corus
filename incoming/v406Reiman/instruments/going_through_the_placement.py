"""Going through v406geodesic's placement of the sixteen names on a torus.

The placement, as `incoming/v406geodesic/instruments/check_bifolding_and_torus.py`
has it: of n − 1 in four parities, the two of a name's four-cycling go round
the small opening, outer upper, inner upper, inner lower, outer lower, and the
two of its root go round the large opening. Nothing of that page is altered
here. Exhibit ONE's own relations are set on the placement, and what they are
on it is printed.

    python3 -I incoming/v406Reiman/instruments/going_through_the_placement.py
"""
BAND = ["outside, upper", "inner, upper", "inner, lower", "outside, lower"]


def place(n):
    k = (n - 1) % 16
    return k >> 2, k & 3  # round the small opening, round the large opening


def outside(n):
    return place(n)[0] in (0, 3)


def upper(n):
    return place(n)[0] in (0, 1)


def degrees(n):
    """By the direction a place faces: +90 on the outside surface, −90 on the inner."""
    return 90 if outside(n) else -90


if __name__ == "__main__":
    print("1. 4 apart, a name with the name 4 on")
    for n in range(1, 13):
        a, b = place(n), place(n + 4)
        one_height = upper(n) == upper(n + 4)
        outer_inner = outside(n) != outside(n + 4)
        print(f"   {n:>2} with {n + 4:>2} · {BAND[a[0]]} with {BAND[b[0]]} · outer with inner at one height: {'is' if one_height and outer_inner else 'is-not'}")
    print()
    print("2. Exhibit ONE's four betweens, the winding passing from one band to its next")
    for a, b in ((4, 5), (8, 9), (12, 13), (16, 17)):
        print(f"   {a} )( {b} · {BAND[place(a)[0]]} to {BAND[place(b)[0]]}")
    print("   and no other two names one apart are of two bands:",
          "is" if all(place(n)[0] == place(n + 1)[0] for n in range(1, 17) if n % 4) else "is-not")
    print()
    print("3. Exhibit ONE's bi-foldings, a name's place by the direction it faces")
    for label, names in (("bi-folding", (1, 9, 8, 16)), ("bi-folding", (2, 15, 7, 10)), ("bi-folding", (3, 11, 6, 14)),
                         ("bi-folding", (4, 13, 5, 12)), ("middle bi-folding", (9, 5, 12, 8)), ("middle bi-folding", (7, 11, 6, 10))):
        d = [degrees(n) for n in names]
        print(f"   {label} {'-'.join(map(str, names))} · {', '.join(('+' if x > 0 else '−') + '90°' for x in d)} · together {("−" + str(-sum(d))) if sum(d) < 0 else str(sum(d))}°")
    print()
    print("4. Exhibit ONE's two podals")
    seventeen = all(place(17 - n) == (3 - place(n)[0], 3 - place(n)[1]) for n in range(1, 17))
    nine = all(place(9 - n) == (1 - place(n)[0], 3 - place(n)[1]) for n in range(1, 9))
    print("   17 less, 1 to 16: both rounds inverting, a place onto a place facing the same way, outside onto outside:",
          "is" if seventeen and all(outside(n) == outside(17 - n) for n in range(1, 17)) else "is-not")
    print("   9 less, 1 to 8: round the large opening inverting, and outside with inner at one height:",
          "is" if nine and all(outside(n) != outside(9 - n) and upper(n) == upper(9 - n) for n in range(1, 9)) else "is-not")
