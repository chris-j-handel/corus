"""Exploring passes about verifying, a partner's saying of 22 November: along, across and wide.

Nothing is proved here. Three passes, a print of all or none with all the cases
or numbers stepped.

1. A turn closes an all. A society come again has all its moments, and a saying
   of spirals with one turn is an executing's with all numbers. The surface has
   no turn: a spiral opens in a turn of the spirals before it.
2. A society of the living code's cells, gating. Exhibit ONE Natural Resolver's
   code as it is in its living file: cases of a question, a cell a case, and one
   cell over them, two moments. Its inputs are given with their other-thans.
3. A field's whole-number saying of the hypothesis, by Davis, Matijasevic and
   Robinson, 1976, with reciprocals added, multiplying and less, and with no exp
   and no ln: by nand alone with n of 1 to 4, and by numbers' own arithmetic past.

    python3 -I incoming/v406Reiman/instruments/passes_about_verifying_with_nand.py .
"""
import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, frozen, moments_again, resolver
from the_resolver_with_nand_alone import (PLACES, a_cell, adding_with_nand, both, either, multiplying_with_nand, nand,
                                          other_than, step_with_nand)


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


def a_prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def by_cells(step, is_nots, given):
    """A question by a society of cells: a cell a case with which its answer is not, and one cell over them. Two moments."""
    society, couplings = {}, {}
    for k, case in enumerate(is_nots):
        observed = [(S, 1) for place, with_case in zip(given, case) if place != with_case]
        society[("case", k)] = ([(S, 1)], observed)
        couplings[(("case", k), 9)] = "over"
    society["over"], society["answer"] = ([(S, 1)], []), ([], [])
    couplings[("over", 9)] = "answer"
    society = step(step(society, couplings), couplings)
    return (S, 1) in society["answer"][1]


def gated(step, question, wide):
    """All cases of a question of so many places in, a list of places out: the society's answers are the question's."""
    cases = list(itertools.product((False, True), repeat=wide))
    answers = {case: question(case) for case in cases}
    same = True
    for out in range(len(answers[cases[0]])):
        is_nots = [case for case in cases if not answers[case][out]]
        same = same and all(by_cells(step, is_nots, case) == answers[case][out] for case in cases)
    return same


def number_of(places):
    return sum(PLACES[place] << i for i, place in enumerate(places))


def places_of(n, wide=None):
    wide = wide if wide is not None else max(1, n.bit_length())
    return [(n >> i) % 2 == 1 for i in range(wide)]


def trimmed(places):
    return places_of(number_of(places))


def level(a, b):
    wide = max(len(a), len(b))
    return a + [False] * (wide - len(a)), b + [False] * (wide - len(b))


def added(a, b):
    return trimmed(adding_with_nand(*level(a, b)))


def multiplied(a, b):
    return trimmed(multiplying_with_nand(a, b))


def less_with_nand(a, b):
    """Is a less than b, place with place: the last place apart says it."""
    less = False
    for one, other in zip(*level(a, b)):
        apart = both(either(one, other), nand(one, other))
        less = either(both(apart, other), both(other_than(apart), less))
    return less


def eta(j):
    """The prime of a prime's power, and 1 with all other numbers."""
    for p in range(2, j + 1):
        if a_prime(p):
            power = p
            while power < j:
                power *= p
            if power == j:
                return p
    return 1


def delta(n):
    made = 1
    for m in range(1, n):
        for j in range(1, m + 1):
            made *= eta(j)
    return made


if __name__ == "__main__":
    root = sys.argv[1]
    names, page = resolver(root)
    step = names["_17_next_existing"]
    all_is = True

    print("1. A turn closes an all")
    again_is = True
    for q in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59):
        along = {(i, 9): (i + 1) % q for i in range(q)}
        opened = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
        living, with_nand = moments_again(step, dict(opened), along), moments_again(step_with_nand, dict(opened), along)
        again_is = again_is and living == with_nand and living[0] is not None
        society, seen = dict(opened), []
        for _ in range(living[0] + 3 * living[1]):
            seen.append(frozen(society))
            society = step(society, along)
        again_is = again_is and all(seen[t] == seen[t + living[1]] for t in range(living[0], living[0] + 2 * living[1]))
    all_is = all_is and again_is
    print(f"   a spiral of 3 to 59 selves comes again, the living code and the cell by nand alone the same, and its moments past are its moments before, a turn on: {is_or_is_not(again_is)}")
    six = [r for r in range(6) if r % 2 and r % 3] == [1, 5]
    three = all(any((r + d) % 3 == 0 for d in (0, 2, 4)) for r in range(3))
    twenty_four = all(r * r % 24 == 1 for r in range(24) if r % 2 and r % 3)
    ten = [r for r in range(10) if r % 2 and r % 5] == [1, 3, 7, 9]
    primes = [n for n in range(2, 10001) if a_prime(n)]
    beside = (all(p % 6 in (1, 5) for p in primes if p > 3) and all(p * p % 24 == 1 for p in primes if p > 3)
              and all(p % 10 in (1, 3, 7, 9) for p in primes if p > 5)
              and not any(a_prime(n) and a_prime(n + 2) and a_prime(n + 4) for n in range(4, 10001)))
    turns = six and three and twenty_four and ten and beside
    all_is = all_is and turns
    print(f"   one turn has all numbers: of six, a prime past three is one short of or one past its multiple; of three, one of three odd numbers two apart is at three's seam; of twenty-four, such a prime multiplied by its own is one past its multiple; of ten, a prime past five ends in 1, 3, 7 or 9; and the primes to 10000 beside them: {is_or_is_not(turns)}")
    no_turn = True
    for p in (3, 5, 7, 11, 13, 17):
        spirals = [q for q in range(2, p + 1) if a_prime(q)]
        turn = math.prod(spirals)
        no_turn = no_turn and any(all(m % q for q in spirals) for m in range(p + 1, turn))
    all_is = all_is and no_turn
    print(f"   the surface has no turn: in a turn of the spirals of 2 to p side by side, p of 3 to 17, a number past p is at no seam of them, and a spiral opens with it: {is_or_is_not(no_turn)}")

    print("2. A society of the living code's cells, gating")
    one_moment = True
    for others in range(4):
        for given in itertools.product((False, True), repeat=others):
            giving, _ = names["_1_now_existing"]([(S, 1)], [(S, 1) for place in given if place])
            one_moment = one_moment and (giving == [(S, 0)]) == any(given) and (giving == [(S, -1)]) == (not any(given))
    all_is = all_is and one_moment
    print(f"   a cell with a prior + gives - with none of its others giving +, and nothing with one of them giving, none to three others: {is_or_is_not(one_moment)}")

    def a_nand(case):
        return [nand(case[0], case[1])]

    def a_place_added(case):
        once = adding_with_nand([case[0]], [case[1]])
        twice = adding_with_nand([once[0]], [case[2]])
        return [twice[0], either(once[1], twice[1])]

    def two_added(case):
        return adding_with_nand(list(case[:2]), list(case[2:]))

    def two_multiplied(case):
        return places_of(number_of(case[:2]) * number_of(case[2:]), 4)

    def the_cell(case):
        (gives_plus, gives_minus), (next_plus, next_minus), _, _ = a_cell((both(case[0], other_than(case[1])), both(case[1], other_than(case[0]))), [case[2:4], case[4:6]])
        return [gives_plus, gives_minus, next_plus, next_minus]

    for said, question, wide in (("a nand of two", a_nand, 2), ("a place added, with a carry in and a carry out", a_place_added, 3),
                                 ("two numbers of 0 to 3 added", two_added, 4), ("two numbers of 0 to 3 multiplied", two_multiplied, 4),
                                 ("the cell by nand alone, a prior and two observed", the_cell, 6)):
        living, with_nand = gated(step, question, wide), gated(step_with_nand, question, wide)
        all_is = all_is and living and with_nand
        print(f"   {said}: the society's answer is the question's with all its cases, two moments, by the living code and by the cell by nand alone: {is_or_is_not(living and with_nand)}")

    print("3. A field's whole-number saying of the hypothesis")
    deltas = [delta(n) for n in range(1, 9)]
    made = deltas == [1, 1, 2, 12, 144, 8640, 518400, 217728000]
    all_is = all_is and made
    print(f"   its delta with n of 1 to 8, made of the primes of the primes' powers: 1, 1, 2, 12, 144, 8640, 518400 and 217728000: {is_or_is_not(made)}")
    by_nand = same = True
    for n in range(1, 5):
        p, q = places_of(0), places_of(1)
        for j in range(1, deltas[n - 1] + 1):
            p, q = added(multiplied(p, places_of(j)), q), multiplied(q, places_of(j))
        its_n = places_of(n)
        n2 = multiplied(its_n, its_n)
        n3, n4, q2 = multiplied(n2, its_n), multiplied(n2, n2), multiplied(q, q)
        one = added(multiplied(places_of(4), multiplied(p, p)), multiplied(n4, q2))
        other = added(multiplied(multiplied(places_of(144), n3), q2), multiplied(multiplied(multiplied(places_of(4), p), n2), q))
        h = sum(Fraction(1, k) for k in range(1, deltas[n - 1] + 1))
        by_nand = by_nand and less_with_nand(one, other)
        same = same and Fraction(number_of(p), number_of(q)) == h and ((h - Fraction(n * n, 2)) ** 2 < 36 * n ** 3)
    all_is = all_is and by_nand and same
    print(f"   with n of 1 to 4, by nand alone, reciprocals of 1 to delta added, multiplying and less: {is_or_is_not(by_nand)}; the same as numbers' own arithmetic: {is_or_is_not(same)}")
    past = True
    for n in (5, 6):
        h = sum(Fraction(1, k) for k in range(1, deltas[n - 1] + 1))
        past = past and (h - Fraction(n * n, 2)) ** 2 < 36 * n ** 3
    h7 = math.fsum(1 / k for k in range(1, deltas[6] + 1))
    past = past and (h7 - 24.5) ** 2 + 1 < 36 * 7 ** 3
    all_is = all_is and past
    print(f"   with n of 5 and 6 by numbers' own arithmetic, and of 7 by a field's rounding: {is_or_is_not(past)}")

    print("All is, of the cases and numbers stepped." if all_is else "NOT ALL IS.")
