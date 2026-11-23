"""The world's interests in the primes, one at a time, a partner's asking of 22 November: what was executed with them.

Nothing is proved here. Four of the world's observings, a print of all or none
with the numbers and moments stepped: the rows of the number spiral; the 0s on
a torus of two prime spirals, beside the primes' zeros; the two closings a
prime has, one short of it and one past it; and the between of two numbers.

    python3 -I incoming/v406Reiman/instruments/one_at_a_time_executed.py .
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_torus_priors, moments_again, resolver, torus_couplings


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


def a_prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def its_primes(n):
    found, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            found.add(d)
            n //= d
        d += 1
    return found | ({n} if n > 1 else set())


def doubling_round(q):
    x, moments = 2 % q, 1
    while x != 1:
        x, moments = 2 * x % q, moments + 1
    return moments


def prior_two_round(q):
    a, b, moments = 1, 1 % q, 1
    while a % q:
        a, b, moments = b, (a + b) % q, moments + 1
    return moments


def prior_two_closes(n):
    a, b = 0, 1
    for place in bin(n + 1)[2:]:
        a, b = (a * ((2 * b - a) % n)) % n, (a * a + b * b) % n
        if place == "1":
            a, b = b, (a + b) % n
    return a == 0


if __name__ == "__main__":
    names, page = resolver(sys.argv[1])
    step, now = names["_17_next_existing"], names["_1_now_existing"]
    all_is = True

    print("1. The rows of the number spiral")
    small = [q for q in range(2, 41) if a_prime(q)]
    no_seam = all((n * n + n + 41) % q for q in small for n in range(q))
    all_is = all_is and no_seam
    print(f"   with all n, by one turn of a spiral of 2 to 37, n multiplied by its own with n and 41 added is at no seam of them: {is_or_is_not(no_seam)}")

    print("2. The 0s on a torus of two prime spirals")
    apart = again = True
    for p, q in ((3, 5), (5, 7), (7, 11)):
        society = {one: ([(S, v)], []) for one, v in exhibit_torus_priors(p, q).items()}
        across = torus_couplings(p, q)
        opened, moments = moments_again(step, dict(society), across)
        again = again and moments == 4 * p
        for _ in range(opened + moments):
            zeros = {one for one, (prior, received) in society.items() if now(prior, received)[0] == [(S, 0)]}
            apart = apart and not any(((a + 1) % p, b) in zeros or (a, (b + 1) % q) in zeros for a, b in zeros)
            society = step(society, across)
    all_is = all_is and apart and again
    print(f"   3 by 5, 5 by 7 and 7 by 11 selves, by the living code: two 0s are side by side at no now, and the 0s come again with four moments a self of the smaller spiral: {is_or_is_not(apart and again)}")

    print("3. The two closings, one short and one past")
    two_alone = all(math.gcd(n - 1, n + 1) == 2 for n in range(3, 200002, 2))
    a_primes_own = all((q - 1) % doubling_round(q) == 0 and (q + 1) % prior_two_round(q) == 0 for q in range(3, 20000, 2) if q % 10 in (3, 7) and a_prime(q))
    to = 2000000
    closing = [n for n in range(3, to, 2) if n % 10 in (3, 7) and pow(2, n - 1, n) == 1 and not a_prime(n)]
    none_both = not any(prior_two_closes(n) for n in closing)
    by_rounds = all(all((n - 1) % doubling_round(q) == 0 for q in its_primes(n)) and any((n + 1) % prior_two_round(q) for q in its_primes(n)) for n in closing)
    all_is = all_is and two_alone and a_primes_own and len(closing) == 92 and none_both and by_rounds
    print(f"   one short of an odd number and one past it have no part in both but two, odd numbers of 3 to 200001: {is_or_is_not(two_alone)}")
    print(f"   a prime ending in 3 or 7, to 20000: its doubling round is a part of one short of it, and its prior-two round a part of one past it: {is_or_is_not(a_primes_own)}")
    print(f"   of the numbers of no prime ending in 3 or 7, to {to}, ninety-two close with doubling and none of them with prior two added: {is_or_is_not(len(closing) == 92 and none_both)}")
    print(f"   in all ninety-two, the smaller spirals' doubling rounds are parts of one short, and one smaller spiral's prior-two round is no part of one past: {is_or_is_not(by_rounds)}")

    print("4. The between of two numbers")
    primes = [q for q in range(2, 300) if a_prime(q)]
    between = all(((n - m) % q == 0) == (n % q == 0) for m in range(1, 300) for n in range(m + 1, 300) for q in primes if m % q == 0)
    a_turn_on = all((n % q == 0) == ((n + 210) % q == 0) for n in range(1, 501) for q in (2, 3, 5, 7))
    all_is = all_is and between and a_turn_on
    print(f"   with two numbers of 1 to 299 and a prime spiral at its seam with the one: it is at its seam with the other with it at its seam with their between, and with no other: {is_or_is_not(between)}")
    print(f"   about a number and about the number a turn of 210 on, the seams of the spirals of 2, 3, 5 and 7 are the same: {is_or_is_not(a_turn_on)}")

    print("All is, of the numbers and moments stepped." if all_is else "NOT ALL IS.")
