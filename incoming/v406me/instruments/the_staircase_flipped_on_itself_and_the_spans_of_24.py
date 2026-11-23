#!/usr/bin/env python3
"""The primes' staircase flipped on itself in a section of 60, the span to 23, and the spans of 24.

Usage:  python3 -I incoming/v406me/instruments/the_staircase_flipped_on_itself_and_the_spans_of_24.py

A partner's sayings of 23 November, explored by executing, with whole numbers alone: no smooth
curve, no logarithm and no decimal measuring. Nothing is proved.

  1  The longest span of primes is to 23. One short and one past the multiples of six, in their
     order: 5, 7, 11, 13, 17, 19, 23.
  2  Out and back from 24. With the spirals of 2 to p side by side, the uncrossed numbers are
     primes as far as one short of the next prime multiplied by its own: a whole number of 24s.
  3  The staircase flipped upside down and backwards, laid on itself in a section of 60: a number
     with its number from the section's other end.
  4  The same fit, a spiral more and a section more.

The uncrossed numbers are by numbers' own dividing here. v406Reiman's surface has the same numbers
by Exhibit ONE Natural Resolver's code as it is. A field has all four: its sieve, its wheels of 6,
30 and 210, a prime multiplied by its own one past a multiple of 24, and its five-sided numbers.

It writes its lines to standard output. It writes no file, reaches no network and decides nothing.
"""
import sys

TO = 1200000
sieve = bytearray([1]) * (TO + 1)
sieve[0] = sieve[1] = 0
for i in range(2, int(TO ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))


def prime(n):
    return 0 <= n <= TO and sieve[n] == 1


def uncrossed_by(spirals):
    return lambda n: all(n % p for p in spirals)


def not_fitting(a, member, section):
    """A number with its number from the section's other end, the two not the same."""
    return [(a + r, a + section - r) for r in range(1, section // 2 + 1) if member(a + r) != member(a + section - r)]


def says(ok):
    return "is" if ok else "IS NOT"


def main():
    all_is = True

    print("1. One short and one past the multiples of six, in their order")
    runs, run, start, before = [], 0, None, None
    for k in range(1, TO // 6):
        for n in (6 * k - 1, 6 * k + 1):
            if prime(n):
                start = n if run == 0 else start
                run += 1
            else:
                if run >= 6:
                    runs.append((run, start, before))
                run = 0
            before = n
    ok = runs[0] == (7, 5, 23) and sum(1 for r in runs if r[0] >= 7) == 1
    one_turn = [n for n in range(7, 7 + 30) if n % 6 in (1, 5)]
    fives = [i for i, n in enumerate(one_turn) if n % 5 == 0]
    ok2 = len(one_turn) == 10 and fives == [6, 9]
    all_is = all_is and ok and ok2
    print(f"   5, 7, 11, 13, 17, 19, 23: seven in a row all primes, and 25 is 5 by 5; no other seven in a row to {TO}: {says(ok)}")
    print(f"   in a turn of 30 past 5 they are ten, 5's seam with the seventh and the tenth, six in a row at the most: no other seven with any number: {says(ok2)}")
    print(f"   six in a row, to {TO}: {[(a, b) for r, a, b in runs if r == 6]}")

    print("2. Spirals of 2 to p side by side: the uncrossed numbers are primes as far as a whole number of 24s")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    spans = []
    ok = True
    for i in range(1, len(primes) - 1):
        member = uncrossed_by(primes[:i + 1])
        the_next = primes[i + 1]
        lowest = next(n for n in range(2, TO) if member(n) and not prime(n))
        ok = ok and lowest == the_next * the_next and (lowest - 1) % 24 == 0
        spans.append((lowest - 1) // 24)
    ok = ok and spans == [1, 2, 5, 7, 12, 15, 22, 35, 40]
    all_is = all_is and ok
    print(f"   the lowest uncrossed number that is no prime is the next prime multiplied by its own, 25, 49, 121, 169 and on; one short of it is 24, 48, 120, 168 and on: {spans} of 24: {says(ok)}")

    print("3. The staircase flipped upside down and backwards, on itself, in a section of 60")
    member = uncrossed_by((2, 3, 5))
    its = [n for n in range(1, 60) if member(n)]
    sections = TO // 60 - 1
    ok = all(not not_fitting(60 * k, member, 60) for k in range(sections))
    ok_turn = all(member(r) == member(60 - r) for r in range(1, 60))
    all_is = all_is and ok and ok_turn
    print(f"   the numbers no spiral of 2, 3 or 5 crosses, 1 to 59: {its}")
    print(f"   a number with its number from the other end, both uncrossed or both crossed, in all {sections} sections of 60 to {TO}: {says(ok)}; and with all numbers, by one turn: {says(ok_turn)}")
    lowest = not_fitting(0, prime, 60)
    ok = lowest == [(1, 59), (2, 58), (3, 57), (5, 55), (11, 49)]
    all_is = all_is and ok
    print(f"   the primes, 0 to 60: all fit but 2, 3 and 5 themselves, 1 with 59, and 11 with 49, 7 by 7: {says(ok)}")
    fitting = [60 * k for k in range(1, sections) if not not_fitting(60 * k, prime, 60)]
    print(f"   the primes, the sections past it: {len(fitting)} of {sections - 1} fit themselves flipped, the lowest beginning at {fitting[:4]}; in the others a spiral of 7 or more crosses one of a pair")

    print("4. A spiral more, a section more")
    ok = True
    turn = 2
    for i in range(1, 5):
        turn *= primes[i]
        member = uncrossed_by(primes[:i + 1])
        ok = ok and all(not not_fitting(2 * turn * k, member, 2 * turn) for k in range(min(40, TO // (2 * turn) - 1)))
    all_is = all_is and ok
    print(f"   the uncrossed of 2 and 3 in sections of 12, of 2 to 5 in 60, of 2 to 7 in 420 and of 2 to 11 in 4620 fit themselves flipped: {says(ok)}")
    print("All is, of the numbers stepped." if all_is else "Not all is.")
    return 0 if all_is else 1


if __name__ == "__main__":
    sys.exit(main())
