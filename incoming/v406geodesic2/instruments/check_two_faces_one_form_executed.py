"""Two faces, one form: the public statement's part, executed from the numbers for a drawing (session v406geodesic2).

A partner's word of 24 November, re-said: go on with this, and with the helping and the learning from all the sessions.
The part is v406other2's, of its statement for the public, with v406me's paring of it. v406other2's asking of this session:
the part of two faces, a drawing.

Executed here, all or none, from the numbers alone:
  1  the eight places of a turn of 30;                         2  the same up and down, a place and its other;
  3  round its quarter turns, a four and its flips;            4  a place in the next turn: once crossed, and the prime less 1 times a place;
  5  a prime born crosses from its own square on;              6  together even: the primes by their eight places, a measuring;
  7  a prime past 3 between two crossed numbers, a seam of 6 and a seam of 4;
  8  this session's living parities at the places.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_two_faces_one_form_executed.py
"""
import math, sys
sys.dont_write_bytecode = True
TO = 4_194_304
PLACES = [1, 7, 11, 13, 17, 19, 23, 29]


def the_primes(to):
    crossed = bytearray(to + 1); crossed[0] = crossed[1] = 1
    for n in range(2, math.isqrt(to) + 1):
        if not crossed[n]: crossed[n * n::n] = b"\x01" * len(range(n * n, to + 1, n))
    return crossed


def places_of(turn):
    return [n for n in range(1, turn) if math.gcd(n, turn) == 1]


if __name__ == "__main__":
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    crossed = the_primes(TO)
    primes = [n for n in range(2, TO + 1) if not crossed[n]]
    line("A turn of 30 has eight places, 1, 7, 11, 13, 17, 19, 23 and 29, the numbers of it with no 2, 3 or 5 multiplied in; and all primes past 5, to 4,194,304, are at the eight",
         places_of(30) == PLACES and all(p % 30 in PLACES for p in primes[3:]))
    line("The even face, the same up and down: a place and the turn less it are two places, with the turns of 30, 210, 2,310 and 30,030; of 30 they are four pairs, 1 and 29, 7 and 23, 11 and 19, 13 and 17",
         all(set(turn - x for x in places_of(turn)) == set(places_of(turn)) for turn in (30, 210, 2310, 30030)) and [(x, 30 - x) for x in PLACES[:4]] == [(1, 29), (7, 23), (11, 19), (13, 17)])
    four = [pow(7, k, 30) for k in range(5)]
    line("Round its quarter turns: by 7, a place of 30 goes 1, 7, 19, 13 and is 1 again, one four; the turn less them, 29, 23, 11 and 17, is the other four, its flips. With a turn of 6 it is-not, v406me's finding: its places are 1 and 5, and 5 by 5 is 1 again",
         four == [1, 7, 19, 13, 1] and sorted(30 - x for x in four[:4]) == [11, 17, 23, 29] and sorted(four[:4] + [30 - x for x in four[:4]]) == PLACES
         and places_of(6) == [1, 5] and 5 * 5 % 6 == 1)
    def into(turn, p):
        spread = [x + turn * k for x in places_of(turn) for k in range(p)]
        return len(spread), sum(1 for n in spread if n % p == 0), sum(1 for n in spread if n % p) == len(places_of(turn * p))
    line("A place of a turn is the prime's times in the next turn: once crossed, and the prime less 1 times a place. The 8 places of 30 are 56 numbers of 210, 8 crossed by 7 and 48 places; the 48 are 528 of 2,310, 48 crossed by 11 and 480 places",
         into(30, 7) == (56, 8, True) and into(210, 11) == (528, 48, True) and len(places_of(2310)) == 480)

    least = {}                                                                    # the least prime multiplied in a crossed number at a place
    for p in primes:
        if p > 2048: break
        if p > 5:
            for n in range(p * p, TO + 1, p):
                if n not in least and n % 30 in PLACES: least[n] = p
    anew = {}
    for n in sorted(least):
        anew.setdefault(least[n], n)
    line("The uneven face, the fracturing: a prime born crosses places from its own square on. The least crossed number at a place, past 1, is 49; and the least number a prime crosses anew is the prime by itself, 49, 121, 169, 289 and on, with all primes of 7 to 2,039",
         min(least) == 49 and all(anew[p] == p * p for p in anew) and [anew[p] for p in (7, 11, 13, 17)] == [49, 121, 169, 289] and max(anew) == 2039)

    by_place = {x: 0 for x in PLACES}
    for p in primes[3:]: by_place[p % 30] += 1
    most, fewest = max(by_place.values()), min(by_place.values())
    line(f"Together even: the {len(primes) - 3:,} primes past 5 to 4,194,304 are at the eight places {fewest:,} to {most:,} a place, the same to a part in a hundred. One at a time uneven: a row of 30 has 0 to 7 of them. A measuring",
         len(primes) - 3 == sum(by_place.values()) and (most - fewest) / fewest < 0.01
         and {sum(1 for x in PLACES if not crossed[30 * r + x]) for r in range(1, 139810)} == set(range(0, 8)))

    seams = all(crossed[p - 1] and crossed[p + 1] and ((p - 1) % 6 == 0) != ((p + 1) % 6 == 0) and ((p - 1) % 4 == 0) != ((p + 1) % 4 == 0) for p in primes[2:] if p <= 400_000)
    one_number = sum(1 for p in primes[2:] if p <= 400_000 and any(n % 12 == 0 for n in (p - 1, p + 1)))
    line(f"A prime past 3 is one more than a crossed number and one less than a crossed number, to 400,000. One of the two is a seam of 6. One of the two is a seam of 4. v406me's paring, and its finding again: the two seams are one number at {one_number:,} of the 33,858 primes, as 12 at 13",
         seams and one_number == 16_904 and sum(1 for p in primes[2:] if p <= 400_000) == 33_858)

    parity = bytearray(TO + 1)
    other = bytes([1, 0]) + bytes(range(2, 256))
    for p in primes:
        power = p
        while power <= TO:
            parity[power::power] = parity[power::power].translate(other); power *= p
    crossed_at_places = [n for n in range(7, TO + 1) if crossed[n] and n % 30 in PLACES]
    plus = sum(1 for n in crossed_at_places if parity[n] == 0)
    line(f"This session's living parities at the places, to 4,194,304: a prime is a −, and the least crossed number at a place, 49, is a +, two primes multiplied. Of the {len(crossed_at_places):,} crossed numbers at the places, {plus:,} are a +, two in three, a measuring",
         all(parity[p] == 1 for p in primes) and parity[49] == 0 and len(crossed_at_places) == 822_536 and plus == 556_499)

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
