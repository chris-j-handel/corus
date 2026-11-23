"""The hypothesis's zeros beside the cell's 0s, a partner's asking of 22 November: what was executed with its reasons.

Nothing is proved here, and no tie of the two is shown. A reason the two are
not the same is an is-not, and its resolving its one inversion. By a field's
arithmetic, its exp and its ln, and by numbers' own arithmetic.

    python3 -I incoming/v406Reiman/instruments/the_zeros_beside_the_cells_0s.py .
"""
import cmath
import itertools
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, exhibit_torus_priors, moments_again, resolver, torus_couplings


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
    names, page = resolver(sys.argv[1])
    step, now = names["_17_next_existing"], names["_1_now_existing"]

    def zeros_a_moment(society, couplings, moments):
        row = []
        for _ in range(moments):
            row.append(sum(1 for prior, received in society.values() if now(prior, received)[0] == [(S, 0)]))
            society = step(society, couplings)
        return row

    print("7. A spiral more, a 0 more")
    more = True
    for p, q in ((3, 5), (5, 7), (7, 11)):
        society = {one: ([(S, v)], []) for one, v in exhibit_torus_priors(p, q).items()}
        opened, moments = moments_again(step, dict(society), torus_couplings(p, q))
        more = more and max(zeros_a_moment(society, torus_couplings(p, q), opened + moments)) == p
    all_is = all_is and more
    print(f"   on a torus of 3 by 5, 5 by 7 and 7 by 11 selves the most 0s at a now are the smaller spiral's selves, three, five and seven: {is_or_is_not(more)}")

    print("9. A 0 a second step")
    second = True
    for q in (3, 5, 7, 11, 13, 17, 19, 23):
        society = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
        row = zeros_a_moment(society, {(i, 9): (i + 1) % q for i in range(q)}, 4 * q + 8)
        second = second and row == [n % 2 for n in range(4 * q + 8)]
    all_is = all_is and second
    print(f"   on an odd spiral of 3 to 23 selves one 0 is given with a second moment, and none with the moment between: {is_or_is_not(second)}")

    print("10. A between with its two sides the same")
    same_sides = True
    for prior in (1, -1):
        for wide in range(4):
            for given in itertools.product((1, -1, 0), repeat=wide):
                giving, its_next = now([(S, prior)], [(S, v) for v in given])
                same_sides = same_sides and (its_next == [(S, prior)] if giving == [(S, 0)] else its_next == [(S, -prior)])
    all_is = all_is and same_sides
    print(f"   with a prior, a 0 is given with its next prior its prior, and with all else its next prior is its prior inverted, none to three others: {is_or_is_not(same_sides)}")

    print("The tie, by a field's arithmetic")
    to = 30000
    a_prime = bytearray([1]) * (to + 1)
    a_prime[0] = a_prime[1] = 0
    for i in range(2, math.isqrt(to) + 1):
        if a_prime[i]:
            a_prime[i * i::i] = bytearray(len(a_prime[i * i::i]))
    turns = []
    for p in range(2, to + 1):
        if a_prime[p]:
            power, times = p, 1
            while power <= to:
                turns.append((math.log(p) / math.sqrt(power), times * math.log(p)))
                power, times = power * p, times + 1
    heights = [13.5 + i * 0.02 for i in range(1326)]
    added = [-sum(weight * math.cos(h * rate) for weight, rate in turns) for h in heights]
    peaks = sorted(((added[i], heights[i]) for i in range(1, len(heights) - 1) if added[i] > added[i - 1] and added[i] > added[i + 1]), reverse=True)[:6]
    zeros = (14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178)
    tied = all(abs(peak - zero) < 0.25 for peak, zero in zip(sorted(h for _, h in peaks), zeros))
    all_is = all_is and tied
    print(f"   the primes' turns alone, added, primes and their powers to {to}: of its peaks of heights 13.5 to 40 the six highest are at the six lowest zeros' heights, to a quarter: {is_or_is_not(tied)}")
    print("All is, of the numbers stepped." if all_is else "NOT ALL IS.")
