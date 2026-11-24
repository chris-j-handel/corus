#!/usr/bin/env python3
"""The fit of a turn's places, up and down and round its quarter turns, and its fracturing by a prime
born: executed with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/the_fit_of_a_turn_s_places_up_and_down_and_round_its_quarter_turns_executed.py

A turn's places are its numbers no spiral of the turn's primes crosses. A line is a saying, ending is or
is-not. Nothing is decided: a line says is of what it stepped. It opens no file and writes no file.
"""
from math import gcd

out = []


def say(text, ok):
    out.append(("is" if ok else "is-not", text))


def places(turn):
    return [k for k in range(1, turn + 1) if gcd(k, turn) == 1]


def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


TURNS = (6, 30, 210, 2310, 30030)
ok_flip = ok_stair = ok_round = ok_other = True
for t in TURNS:
    ps = places(t)
    pset = set(ps)
    ok_flip = ok_flip and all((t - k) in pset for k in ps)
    upto = [0] * (t + 1)
    for k in range(1, t + 1):
        upto[k] = upto[k - 1] + (k in pset)
    ok_stair = ok_stair and all(upto[k] + upto[t - 1 - k] == len(ps) for k in range(t))
    if t <= 2310:
        ok_round = ok_round and all((a * b) % t in pset for a in ps for b in ps)
        ok_other = ok_other and all(sum(1 for b in ps if (a * b) % t == 1) == 1 for a in ps)
say("a turn's places are the same up and down, k a place with the turn less k a place: the turns of 6, 30, 210, "
    "2,310 and 30,030", ok_flip)
say("a turn's staircase of places, flipped upside down and backwards, is the same staircase: the same turns", ok_stair)
say("a place by a place is a place, round its turn: the turns of 6 to 2,310", ok_round)
say("a place has one other, the two multiplied 1 round its turn: the turns of 6 to 2,310", ok_other)

p30 = places(30)
own = [a for a in p30 if (a * a) % 30 == 1]
say("round 30 the places their own other are 1, 11, 19 and 29, and 7 is with 13 and 17 with 23",
    own == [1, 11, 19, 29] and (7 * 13) % 30 == 1 and (17 * 23) % 30 == 1)
quarter = [pow(7, i, 30) for i in range(5)]
say("round 30 a place by 7 is a quarter turn: 1 to 7 to 19 to 13 to 1, four of them the place again",
    quarter == [1, 7, 19, 13, 1])
say("the eight places of 30 are the four of the quarter turns, 1, 7, 19 and 13, and their four flips, "
    "29, 23, 11 and 17, 30 less each", sorted(quarter[:4] + [30 - k for k in quarter[:4]]) == p30)
say("round 10 the endings turn the same: 1 to 3 to 9 to 7 to 1 by 3, and their own others are 1 and 9",
    [pow(3, i, 10) for i in range(5)] == [1, 3, 9, 7, 1] and [a for a in (1, 3, 7, 9) if a * a % 10 == 1] == [1, 9])

ok = True
for t, p in ((2, 3), (6, 5), (30, 7), (210, 11), (2310, 13)):
    for k in places(t):
        lifts = [k + j * t for j in range(p)]
        ok = ok and sum(1 for n in lifts if n % p == 0) == 1
say("a place of a turn is p times in the next turn, once crossed by the prime born and p less 1 times a place: "
    "the turns of 2, 6, 30, 210 and 2,310 with 3, 5, 7, 11 and 13", ok)

p60 = places(60)
pairs = [(k, 60 - k) for k in p60 if k < 30]
say("the sixteen places of 60 are eight pairs about 30: 1 with 59, 7 with 53, 11 with 49, 13 with 47, 17 with 43, "
    "19 with 41, 23 with 37 and 29 with 31",
    pairs == [(1, 59), (7, 53), (11, 49), (13, 47), (17, 43), (19, 41), (23, 37), (29, 31)])
say("all sixteen are primes but 1 and 49, and 49 is 7 by 7, a prime born with its own square",
    [k for k in p60 if not prime(k)] == [1, 49])
p120 = places(120)
say("the 32 places of 120 are primes but 1, 49, 77, 91 and 119, and the four crossed are 7 by 7, by 11, by 13 "
    "and by 17: one prime born fractures all of 0 to 120",
    [k for k in p120 if not prime(k)] == [1, 49, 77, 91, 119] and [7 * 7, 7 * 11, 7 * 13, 7 * 17] == [49, 77, 91, 119])
ok = True
for t, nxt in ((6, 5), (30, 7), (210, 11), (2310, 13), (30030, 17)):
    ps = [k for k in range(2, nxt * nxt + 1) if gcd(k, t) == 1]
    crossed = [k for k in ps if not prime(k)]
    ok = ok and crossed == [nxt * nxt]
say("past a turn's own primes, its places are all primes to the square of the prime born next, and that square is "
    "the lowest place crossed: 25, 49, 121, 169 and 289", ok)


# Six from a self, four and two: the shape of the eight places of 30, beside the six names between selves.
def turns_to_again(k, t=30):
    n, x = 1, k % t
    while x != 1:
        x = (x * k) % t
        n += 1
    return n


shape = {k: turns_to_again(k) for k in p30}
say("of the eight places of 30, 1 is again with one turn of its own, 11, 19 and 29 with two, and 7, 13, 17 and 23 "
    "with four", shape == {1: 1, 7: 4, 11: 2, 13: 4, 17: 4, 19: 2, 23: 4, 29: 2})
six = [k for k in p30 if k not in (1, 29)]
say("past 1 and its flip 29, the places are six: four quarter turns in two pairs about 15, 7 with 23 and 13 with 17, "
    "and two their own other in one pair, 11 with 19: four and two",
    six == [7, 11, 13, 17, 19, 23] and sorted(k for k in six if shape[k] == 4) == [7, 13, 17, 23]
    and sorted(k for k in six if shape[k] == 2) == [11, 19] and 7 + 23 == 13 + 17 == 11 + 19 == 30)
side = sorted(set(quarter[:4]) - {1})
other_side = sorted(30 - k for k in side)
say("three of the six are with 1 in its four of quarter turns, 7, 13 and 19, and three are their flips, 11, 17 and "
    "23: a three is two quarter turns, the other of one another, and one its own other",
    side == [7, 13, 19] and other_side == [11, 17, 23] and (7 * 13) % 30 == 1 and (17 * 23) % 30 == 1
    and (19 * 19) % 30 == 1 and (11 * 11) % 30 == 1)
say("2, 6, 10 and 14 are twice 1, 3, 5 and 7; 1, 3, 5 and 7 added a number after a number are 1, 4, 9 and 16, "
    "the numbers multiplied by their own of a surface of 16",
    [2 * k for k in (1, 3, 5, 7)] == [2, 6, 10, 14] and [sum((1, 3, 5, 7)[:i]) for i in range(1, 5)] == [1, 4, 9, 16])
say("2 and 6 are 8, the places of 30; 1, 3, 5 and 7 are 16, the places of 60; 2, 6, 10 and 14 are 32, the places "
    "of 120", 2 + 6 == len(p30) and 1 + 3 + 5 + 7 == len(p60) and 2 + 6 + 10 + 14 == len(p120))
say("1, 9 and 17 are 8 apart, and 1 and 9 are the odd numbers multiplied by their own of a surface of 16, 17 its "
    "next 1", [9 - 1, 17 - 9] == [8, 8] and [k * k for k in (1, 3)] == [1, 9] and 16 + 1 == 17)
rounds = [2, 2 + 6, 2 + 6, 2 + 6 + 10, 2 + 6 + 10, 2 + 6 + 10 + 14, 2 + 6 + 10 + 14]
say("a field's table of the elements has rows of 2, 8, 8, 18, 18, 32 and 32, each 2, 6, 10 and 14 added from 2 on, "
    "and 118 in all, 120 less 2", rounds == [2, 8, 8, 18, 18, 32, 32] and sum(rounds) == 118 == 120 - 2)
ok = True
for prime_born in (7, 11, 13):
    for k in p30:
        rows = [j for j in range(prime_born) if (k + 30 * j) % prime_born == 0]
        ok = ok and len(rows) == 1
    step = [j for j in range(prime_born) if (1 + 30 * j) % prime_born == 0][0]
    ok = ok and all((k + 30 * ((step * k) % prime_born)) % prime_born == 0 for k in p30)
say("laid in rows of 30, a prime born crosses one spot a place in its own number of rows, and the spots are on one "
    "slant, a row's number the place's by one number round the prime: 7, 11 and 13", ok)

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not.")
