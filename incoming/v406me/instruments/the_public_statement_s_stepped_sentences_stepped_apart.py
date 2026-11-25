#!/usr/bin/env python3
"""The public statement's stepped sentences, stepped apart: a second observing, with whole numbers alone.

    python3 -I incoming/v406me/instruments/the_public_statement_s_stepped_sentences_stepped_apart.py

The statement is v406other2's, `incoming/v406other2/For_the_public_Riemann_s_hypothesis_and_the_living_prime_numbering_a_statement_to_pare.md`.
This instrument opens no instrument of that session. It steps a sentence by its own code, and says is or is-not,
with the number it stepped to. A line marked found says a thing the stepping found beside a sentence.
It writes no file.
"""
import sys
from math import gcd, isqrt

out = []
def say(ok, sentence, to):
    out.append(ok)
    print(("is      " if ok else "is-not  ") + sentence + " · stepped, " + to)
def found(what):
    print("found   " + what)

# the primes, by crossing alone
N = 4194304
crossed = bytearray(N + 1)
lam = [1] * (N + 1)      # a number's parity: a + with an even number of primes multiplied, a - with an odd number
primes = []
for i in range(2, N + 1):
    if not crossed[i]:
        primes.append(i)
        lam[i] = -1
    for p in primes:
        if i * p > N:
            break
        crossed[i * p] = 1
        lam[i * p] = -lam[i]
        if i % p == 0:
            break
is_prime = lambda n: n >= 2 and not crossed[n]

# A number, by +1; along and across
H = 5000
made = set(a * b for a in range(2, H) for b in range(a, H // a + 1))
no_two = set(n for n in range(2, H + 1) if all(n % a for a in range(2, n)))
say(all((n in made) != (n in no_two) for n in range(2, H + 1)),
    "Come by +1, a number is of two kinds, and is of one of them alone", "2 to 5,000")
say(made == set(n for n in range(2, H + 1) if crossed[n]) and no_two == set(p for p in primes if p <= H),
    "Multiplying makes the crossed numbers, all of them, and no other number", "2 to 5,000")
small = [p for p in primes if p <= H]
def one_way(n):
    # the number of ways a number is primes multiplied, its parts from small to large
    def go(m, least):
        if m == 1:
            return 1
        return sum(go(m // p, p) for p in small if least <= p <= m and m % p == 0)
    return go(n, 2)
say(all(one_way(n) == 1 for n in range(2, H + 1)),
    "A crossed number is primes multiplied, one way alone", "2 to 5,000")
T = 400000
past3 = [p for p in primes if 3 < p <= T]
say(all(crossed[p - 1] and crossed[p + 1] for p in past3),
    "A prime past 3 is a +1 from the crossed number below it and a -1 from the crossed number above it", "to 400,000")
six = all(((p - 1) % 6 == 0) != ((p + 1) % 6 == 0) for p in past3)
four = all(((p - 1) % 4 == 0) != ((p + 1) % 4 == 0) for p in past3)
one_number = sum(1 for p in past3 if any(q % 12 == 0 for q in (p - 1, p + 1)))
say(six and four, "Of the two numbers beside a prime past 3, one is a seam of 6, and one is a seam of 4", "to 400,000")
found(f"the seam of 6 and the seam of 4 are one number at {one_number:,} of the {len(past3):,} primes past 3 to 400,000, "
      f"and two numbers at {len(past3) - one_number:,}: at 13 the two are 12 and 14, and 12 is both seams")

# No ending
turn, ok = 1, True
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    turn *= p
    below = [q for q in primes if q <= p]
    ok = ok and all(turn % q == 0 for q in below) and all((turn + 1) % q for q in below)
say(ok, "At their turn, spirals all line up, and one past it none of them does", "the turns of 2 to 23")
say(30 % 2 == 0 and 30 % 3 == 0 and 30 % 5 == 0 and is_prime(31), "2, 3 and 5 line up at 30, and 31, one past, is a prime", "30 and 31")
upto = [0] * (2 * 200000 + 1)
for n in range(1, len(upto)):
    upto[n] = upto[n - 1] + (1 if is_prime(n) else 0)
say(all(upto[2 * n] > upto[n] for n in range(2, 200001)),
    "A number has a prime in its cone forward, past it and to its double", "2 to 200,000")

# Two faces
turns = [6, 30, 210, 2310, 30030]
places = {m: [k for k in range(1, m) if gcd(k, m) == 1] for m in turns}
say(all(set(m - k for k in places[m]) == set(places[m]) for m in turns),
    "A turn's places are the same up and down", "the turns of 6 to 30,030")
quarters = {}
for m in turns:
    quarters[m] = sum(1 for k in places[m] if pow(k, 4, m) == 1 and pow(k, 2, m) != 1)
say(all(quarters[m] > 0 for m in turns[1:]) and [pow(7, i, 30) for i in range(5)] == [1, 7, 19, 13, 1],
    "A turn has a quarter turn, a place four of which are the place again and two of which are other-than it", "the turns of 30 to 30,030")
found("the turn of 6 has no quarter turn: its places are 1 and 5, and two of 5 are the place again. "
      + "Places that are quarter turns: " + ", ".join(f"{quarters[m]:,} of the turn of {m:,}" for m in turns))
ok, m = True, 1
for p, nxt in [(2, 3), (3, 5), (5, 7), (7, 11), (11, 13)]:
    m *= p
    pl = [k for k in range(1, m + 1) if gcd(k, m) == 1]
    for k in pl:
        lifts = [k + j * m for j in range(nxt)]
        ok = ok and sum(1 for x in lifts if x % nxt == 0) == 1 and sum(1 for x in lifts if gcd(x, m * nxt) == 1) == nxt - 1
say(ok, "A place of a turn is p times in the next turn: once crossed, and p less 1 times a place", "5 turns, of 2 to 2,310")
ok = True
for p in [5, 7, 11, 13, 17]:
    below = [q for q in primes if q < p]
    x = next(n for n in range(2 * p, p * p + 1, p) if all(n % q for q in below))
    ok = ok and x == p * p
say(ok, "A prime born crosses places from its own square on: 25, 49, 121, 169, 289", "the primes 5 to 17")

# A test
def parts(n):
    r, m = [], n
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            r.append(p)
            while m % p == 0:
                m //= p
    if m > 1:
        r.append(m)
    return r
def from_below(n):
    qs = parts(n - 1)
    return any(pow(a, n - 1, n) == 1 and all(pow(a, (n - 1) // q, n) != 1 for q in qs) for a in range(2, n))
say(all(from_below(n) == is_prime(n) for n in range(3, 2001)),
    "A number is tested from the number below it, with that number's primes beside it", "3 to 2,000")
def from_above(n):
    qs = parts(n + 1)
    for P in range(1, n):
        for Q in range(1, n):
            if gcd(Q, n) != 1 or gcd(P * P - 4 * Q, n) != 1:
                continue
            u = [0, 1]
            for _ in range(n):
                u.append((P * u[-1] - Q * u[-2]) % n)
            if u[n + 1] == 0 and all(gcd(u[(n + 1) // q], n) == 1 for q in qs):
                return True
    return False
A = 100
say(all(from_above(n) == is_prime(n) for n in range(3, A + 1, 2)),
    "An odd number is tested from the number above it, with that number's primes beside it", f"3 to {A}")
def tree(p, seen):
    for q in parts(p - 1):
        if q not in seen:
            seen.add(q)
            tree(q, seen)
    return seen
say(all(all(is_prime(q) and q < p for q in tree(p, set())) and (p == 2 or 2 in tree(p, set())) for p in primes if p <= 2000),
    "A prime's test is of primes below it, to 2", "the primes to 2,000")

# Riemann's hypothesis: all or none on a surface
ok, n = True, 4
while n <= N:
    ok = ok and sum(lam[d] * (n // d) for d in range(1, n + 1)) == isqrt(n)
    n *= 4
say(ok, "On a surface, all parts' parities are its squares, one for one", "the surfaces of 4 to 4,194,304")

# The largest known prime, with the number written at no place
E = 136279841
carried = [p for p in primes if p <= 2000000]
res = [(pow(2, E, p) - 1) % p for p in carried]
def crossing(d):
    return any((r + d) % p == 0 for p, r in zip(carried, res))
say(not crossing(0) and pow(2, E, 17) == 2, "The record prime has no crossing of the spirals carried, and round 17 it is 1", "the spirals to 2,000,000")
down = next(d for d in range(1, 400) if not crossing(-d))
up = next(d for d in range(1, 400) if not crossing(d))
say(down + up - 1 == 69, "In 69 numbers in a row the record prime alone has no crossing", "the spirals to 2,000,000")
found(f"the numbers with no crossing beside it are {down} below it and {up} above it")

print(f"\n{sum(out)} of {len(out)} sentences stepped apart are is.")
sys.exit(0 if all(out) else 1)
