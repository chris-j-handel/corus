"""The living sayings of primes, executed by numbers' own arithmetic.

Exhibit THREE Natural Numbers, outside its 11.1, and Exhibit FOUR Natural
Mathematics: their sayings of primes with a number in them, gone through one
with one. A saying is, or is not, by numbers' own arithmetic. No resolver is
in this page, and no line of a living file is altered. Natural Numbers 11.1,
its saying of each number of nought to four hundred forty, is not gone
through here.

    python3 -I incoming/v406Reiman/instruments/the_living_sayings_of_primes_executed.py
"""
import itertools
import math


def a_prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def closing(a, b):
    """A next as now with a and prior with b: its steps to all its openings again, or none to forty."""
    if b == 0:
        openings = [(1,)]
        on = lambda state: (a * state[0],)
    else:
        openings = [(1, 0), (0, 1)]
        on = lambda state: (a * state[0] + b * state[1], state[0])
    states = list(openings)
    for steps in range(1, 41):
        states = [on(state) for state in states]
        if states == openings:
            return steps
    return None


if __name__ == "__main__":
    seventeen = [p for p in range(2, 60) if a_prime(p)]
    gaps = [b - a for a, b in zip(seventeen, seventeen[1:])]
    phi = (1 + math.sqrt(5)) / 2
    sayings = []

    def say(where, saying, ok):
        sayings.append(ok)
        print(f"   {where} · {saying}: {'is' if ok else 'IS NOT'}")

    print("Exhibit THREE Natural Numbers")
    say("1.6", "a step of k round N reaches N over their greatest factor of both; round a prime all steps but nought reach all; nine with a step of two reaches all",
        all(len({(k * i) % n for i in range(n)}) == n // math.gcd(n, k) for n in range(2, 80) for k in range(1, n)) and len({(2 * i) % 9 for i in range(9)}) == 9)
    say("1.6", "no power of two above one is a power of three, to two hundred of them; two and three multiplied less two and three added is one",
        not ({2 ** a for a in range(1, 201)} & {3 ** b for b in range(1, 201)}) and 2 * 3 - (2 + 3) == 1)
    say("2.1", "phi cubed less one over phi cubed is four; fifty-five is couplings among eleven, the tenth triangle and the tenth of prior two added",
        abs(phi ** 3 - phi ** -3 - 4) < 1e-12 and math.comb(11, 2) == 55 == sum(range(1, 11)) and [1, 1, 2, 3, 5, 8, 13, 21, 34, 55][9] == 55)
    say("3.1", "phi squared is phi and one; ratios of prior two added are above phi and below it in turn",
        abs(phi * phi - phi - 1) < 1e-12 and all(((b / a) > phi) == (i % 2 == 0) for i, (a, b) in enumerate([(1, 2), (2, 3), (3, 5), (5, 8), (8, 13), (13, 21)])))
    cases = {(a, b): closing(a, b) for a, b in itertools.product((1, -1, 0), repeat=2)}
    say("3.4", "a next as now and prior added, with +1, -1 or none: now with +1 closes after one, with -1 after two; prior with +1 after two, with -1 after four; both with -1 after three; now +1 and prior -1 after six; and none after five",
        cases[(1, 0)] == 1 and cases[(-1, 0)] == 2 and cases[(0, 1)] == 2 and cases[(0, -1)] == 4 and cases[(-1, -1)] == 3 and cases[(1, -1)] == 6 and cases[(1, 1)] is None and 5 not in cases.values())
    say("6.3", "primes part about twenty-four as nine behind and eight ahead; fifteen of sixteen gaps among seventeen primes are even",
        sum(p < 24 for p in seventeen) == 9 and sum(p > 24 for p in seventeen) == 8 and sum(g % 2 == 0 for g in gaps) == 15 and len(gaps) == 16)
    say("6.4", "twenty-four is five squared less one, twenty-seven three cubed, thirty-two two to the fifth", 24 == 5 ** 2 - 1 and 27 == 3 ** 3 and 32 == 2 ** 5)
    say("7.1", "seventeen primes, two to fifty-nine; added they are four hundred forty, eight fifty-fives, twenty-one squared less one; sixty has no prime; sixty-one and sixty-seven are primes",
        len(seventeen) == 17 and seventeen[-1] == 59 and sum(seventeen) == 440 == 8 * 55 == 21 ** 2 - 1 and not a_prime(60) and a_prime(61) and a_prime(67) and seventeen[8] == 23)
    say("7.1", "5, 7, 11, 17 and 19 add to fifty-nine", 5 + 7 + 11 + 17 + 19 == 59)
    say("7.2", "two odd spirals of distinct primes come to their parities again together by four times the two multiplied; nine and twenty-five by 900, three and five by 60, nine and fifteen by 180",
        all(math.lcm(4 * p, 4 * q) == 4 * p * q for p in seventeen[1:] for q in seventeen[1:] if p != q) and math.lcm(36, 100) == 900 and math.lcm(12, 20) == 60 and math.lcm(36, 60) == 180)
    say("7.2", "sixteen odd prime spirals come to their parities again together by 3,845,520,700,308,425,278,140 moments, twice the seventeen multiplied",
        math.lcm(*[4 * p for p in seventeen[1:]]) == 3845520700308425278140 == 2 * math.prod(seventeen))
    twins = [(a, b) for a, b in zip(seventeen, seventeen[1:]) if b - a == 2]
    say("7.3", "sixteen gaps of four values, one, two, four and six; six gaps of two, 3 and 5, 5 and 7, 11 and 13, 17 and 19, 29 and 31, 41 and 43, and past 3 and 5 about a multiple of six",
        sorted(set(gaps)) == [1, 2, 4, 6] and twins == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)] and all((a + 1) % 6 == 0 for a, b in twins[1:]))
    say("7.3", "from five to fifty-three are fourteen primes; five to fifty-nine are fifteen, all odd", len([p for p in seventeen if 5 <= p <= 53]) == 14 and len(seventeen[2:]) == 15 and all(p % 2 for p in seventeen[2:]))
    about_thirty = [(p, 60 - p) for p in range(5, 30) if a_prime(p) and a_prime(60 - p)]
    say("7.4", "six prime pairs about thirty, 7 with 53, 13 with 47, 17 with 43, 19 with 41, 23 with 37, 29 with 31, of twelve primes; eleven is with forty-nine, seven squared",
        about_thirty == [(7, 53), (13, 47), (17, 43), (19, 41), (23, 37), (29, 31)] and 60 - 11 == 49 == 7 ** 2 and [30 - p for p, _ in about_thirty] == [23, 17, 13, 11, 7, 1])
    say("7.6", "prime pairs about one hundred twenty at seven, eleven, seventeen and nineteen; 111 is 3 by 37 and 129 is 3 by 43; 115 is 5 by 23 and 125 five cubed; 117 is 9 by 13 and 123 is 3 by 41; 127 is two to the seventh less one",
        all(a_prime(120 - d) and a_prime(120 + d) for d in (7, 11, 17, 19)) and 111 == 3 * 37 and 129 == 3 * 43 and 115 == 5 * 23 and 125 == 5 ** 3 and 117 == 9 * 13 and 123 == 3 * 41 and 127 == 2 ** 7 - 1)
    say("7.7", "primes by position about twenty-three make 61, 56, 52, 50, 52, 50, 48 and 48; a self's one to nine has primes adding to one hundred, and nine to seventeen to three hundred sixty-three, three by eleven squared",
        [seventeen[i] + seventeen[16 - i] for i in range(8)] == [61, 56, 52, 50, 52, 50, 48, 48] and sum(seventeen[:9]) == 100 and sum(seventeen[8:]) == 363 == 3 * 11 ** 2)
    say("7.7", "8 up: 2 and 23 add to five squared, 5 and 31 to six squared, 17 and 47 to eight squared, 3 and 29 to two to the fifth, 19 and 53 to seventy-two",
        2 + 23 == 25 and 5 + 31 == 36 and 17 + 47 == 64 and 3 + 29 == 32 and 19 + 53 == 72)
    say("9.3", "ten primes leave two by threes, and their far sides of four hundred forty three divides; three's far side is 19 by 23; 7, 19, 31 and 43 have prime far sides, 433, 421, 409 and 397; five's far side is fifteen primes added and couplings among thirty",
        [p for p in seventeen if p % 3 == 2] == [2, 5, 11, 17, 23, 29, 41, 47, 53, 59] and all((440 - p) % 3 == 0 for p in seventeen if p % 3 == 2) and 437 == 19 * 23 and all(a_prime(440 - p) for p in (7, 19, 31, 43)) and 435 == sum(seventeen[2:]) == math.comb(30, 2))
    say("9.4", "sixteen gaps step one ring once, two rings six times, four rings five times and six rings four times, fifty-seven rings together, fifty-nine less two",
        [gaps.count(g) for g in (1, 2, 4, 6)] == [1, 6, 5, 4] and sum(gaps) == 57 == 59 - 2)
    say("9.5", "fourteen primes five to fifty-three add to three hundred seventy-six, and two, three and fifty-nine to sixty-four, eight squared", sum(seventeen[2:16]) == 376 and 2 + 3 + 59 == 64 == 8 ** 2)

    print("Exhibit FOUR Natural Mathematics")
    say("its rounds", "two rounds of m and n stations stepped together reach m by n over their greatest factor of both of their pairs; with no factor of both, all their pairs",
        all(len({(i % m, i % n) for i in range(m * n)}) == m * n // math.gcd(m, n) for m in range(1, 31) for n in range(1, 31)))
    say("its roots", "the square roots of two, three and five are a square's diagonal, a cube's body diagonal and within a pentagon's diagonal over its side",
        abs(math.hypot(1, 1) - math.sqrt(2)) < 1e-12 and abs(math.sqrt(1 + 1 + 1) - math.sqrt(3)) < 1e-12 and abs(2 * math.cos(math.pi / 5) - phi) < 1e-12)
    monster = 808017424794512875886459904961710757005754368000000000
    its_primes = [p for p in range(2, 100) if a_prime(p) and monster % p == 0]
    left = monster
    for p in its_primes:
        while left % p == 0:
            left //= p
    say("its groups", "the largest sporadic group's order has fifteen primes, two to seventy-one: of the seventeen all but thirty-seven, forty-three and fifty-three, and seventy-one",
        left == 1 and its_primes == [p for p in seventeen if p not in (37, 43, 53)] + [71] and len(its_primes) == 15)
    say("Exhibit SEVEN Natural Societies", "a prime from five on is one before a multiple of six or one after it; of fourteen, five to fifty-three, eight are one before and six one after",
        all(p % 6 in (1, 5) for p in range(5, 100000) if a_prime(p)) and [sum(p % 6 == r for p in seventeen[2:16]) for r in (5, 1)] == [8, 6])

    print(f"All is, of the {len(sayings)} gone through." if all(sayings) else "NOT ALL IS.")
