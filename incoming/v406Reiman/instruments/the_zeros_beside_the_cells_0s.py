"""The hypothesis's zeros beside the cell's 0s, a partner's asking of 22 November: what was executed with its reasons.

Nothing is proved here, and no tie of the two is shown. A reason the two are
not the same is an is-not, and its resolving its one inversion. By a field's
arithmetic, its exp and its ln, and by numbers' own arithmetic.

    python3 -I incoming/v406Reiman/instruments/the_zeros_beside_the_cells_0s.py
"""
import cmath
import math


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


def turns_added(height, to):
    """All numbers' turns at a height, added, a + and a - in turn, a field's own way to its hypothesis's function."""
    total = before = 0j
    for n in range(1, to + 1):
        before = total
        total += (-1) ** (n - 1) * cmath.exp(-complex(0.5, height) * math.log(n))
    return abs((total + before) / 2)


def its_primes(n):
    found, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            found[d] = found.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        found[n] = found.get(n, 0) + 1
    return found


if __name__ == "__main__":
    all_is = True
    print("1. A path on the primes' torus")
    height = 14.134725141734693
    its_turn = all(abs(cmath.exp(-1j * height * math.log(n)) - cmath.exp(-1j * sum(a * height * math.log(p) for p, a in its_primes(n).items()))) < 1e-9 for n in range(2, 5001))
    to_nothing = all(turns_added(h, 200000) < 1e-5 for h in (14.134725141734693, 21.022039638771555)) and all(turns_added(h, 200000) > 1 for h in (15.0, 20.0))
    all_is = all_is and its_turn and to_nothing
    print(f"   a number's turn is its primes' turns, one after another, numbers of 2 to 5000: {is_or_is_not(its_turn)}")
    print(f"   at the heights of the two lowest zeros all the numbers' turns added come to nothing, and at heights 15 and 20 they do not: {is_or_is_not(to_nothing)}")

    print("2. A + with a - to none")
    to = 100000
    parity, rest = [1] * (to + 1), list(range(to + 1))
    for p in range(2, to + 1):
        if rest[p] == p:
            for m in range(p, to + 1, p):
                while rest[m] % p == 0:
                    rest[m] //= p
                    parity[m] = -parity[m]
    multiplied = all(parity[a * b] == parity[a] * parity[b] for a in range(2, 300) for b in range(2, 300))
    parts = [0] * (to + 1)
    for d in range(1, to + 1):
        for m in range(d, to + 1, d):
            parts[m] += parity[d]
    a_zero = all(parts[n] == (1 if math.isqrt(n) ** 2 == n else 0) for n in range(1, to + 1))
    all_is = all_is and multiplied and a_zero
    print(f"   with a prime an inversion, two numbers multiplied have their parities multiplied: {is_or_is_not(multiplied)}")
    print(f"   the parities of a number's parts come to a 0 with all numbers of 1 to {to} but a number multiplied by its own, and to one + with that: {is_or_is_not(a_zero)}")

    print("4 and 5. Rates in no ratio")
    no_ratio = not any(2 ** a == 3 ** b for a in range(1, 201) for b in range(1, 201))
    all_is = all_is and no_ratio
    print(f"   two multiplied a times is three multiplied b times with no a and b of 1 to 200: {is_or_is_not(no_ratio)}")
    print("All is, of the numbers stepped." if all_is else "NOT ALL IS.")
