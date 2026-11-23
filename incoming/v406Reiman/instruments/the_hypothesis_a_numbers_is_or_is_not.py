"""The Riemann hypothesis as one is-or-is-not with a number, a field's own saying, executed number with number.

Nothing is proved here. A field's, by Lagarias, 2002, after Robin, 1984: the
hypothesis is, with all numbers n, the numbers dividing n, added, being no more
than H + exp(H) ln(H), H being the reciprocals of 1 to n added. Here it is
executed with the numbers of 1 to a bound, by a field's arithmetic, its exp and
its ln, and by no line of the resolver.

An executing is of the numbers stepped and of no number past them. The numbers
have no last, and no executing has all of them. A field's proof is a thing with
an end, said of numbers with none.

    python3 -I incoming/v406Reiman/instruments/the_hypothesis_a_numbers_is_or_is_not.py [--to 100000]
"""
import math
import sys


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


if __name__ == "__main__":
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 100000
    dividing_added = [0] * (to + 1)
    for d in range(1, to + 1):
        for n in range(d, to + 1, d):
            dividing_added[n] += d
    h, no_more, the_same, clear = 0.0, True, [], True
    for n in range(1, to + 1):
        h += 1 / n
        beside = h + math.exp(h) * math.log(h)
        no_more = no_more and dividing_added[n] <= beside
        if dividing_added[n] == beside:
            the_same.append(n)
        elif n > 1:
            clear = clear and beside - dividing_added[n] > 1e-6
    all_is = no_more and the_same == [1] and clear
    print("1. A field's saying of the hypothesis, one is-or-is-not with a number")
    print(f"   with all numbers of 1 to {to} the numbers dividing a number, added, are no more than H + exp(H) ln(H): {is_or_is_not(no_more)}")
    print(f"   the two are the same with 1 alone, and apart by more than this arithmetic's own rounding with all others: {is_or_is_not(the_same == [1] and clear)}")
    print("All is, of the numbers stepped." if all_is else "NOT ALL IS.")
