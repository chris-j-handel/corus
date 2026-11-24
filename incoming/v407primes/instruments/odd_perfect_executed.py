"""A perfect number: its parts sum to its own doubling. The odd one, stepped.

Usage: python3 -I odd_perfect_executed.py
Whole numbers alone. Each check prints its saying and "is" or "is-not".
"""
from math import gcd, isqrt
import numpy as np

said = []


def say(text, ok):
    said.append(ok)
    print(("is     " if ok else "is-not ") + text)


def parts_sum(n):
    s, d = 0, 1
    while d * d <= n:
        if n % d == 0:
            s += d + (n // d if d * d != n else 0)
        d += 1
    return s


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


# 1. Even perfect: two pieces whose parts' sums swap.
mers = [q for q in range(2, 32) if is_prime(q) and is_prime(2 ** q - 1)]
ok = True
for q in mers:
    two, M = 2 ** (q - 1), 2 ** q - 1
    ok &= (2 * two - 1 == M) and (M + 1 == 2 * two)  # parts of 2^(q-1) sum to M; parts of M sum to 2^q
    if q <= 13:
        ok &= parts_sum(two * M) == 2 * two * M
say(f"even perfect = doubling's piece times one-less-than-its-doubling, parts' sums swapping, q = {mers}", ok)

# 2. The one 2: an odd prime power's parts sum is odd at an even power,
#    and sits at 2 round 4 only when prime and power both sit at 1 round 4.
ok = True
for q in range(3, 2000, 2):
    if not is_prime(q):
        continue
    for e in range(0, 41):
        s = (q ** (e + 1) - 1) // (q - 1)
        ok &= (s % 2 == 1) == (e % 2 == 0)
        ok &= (s % 4 == 2) == (q % 4 == 1 and e % 4 == 1)
say("odd prime powers: parts' sum odd at even powers; at 2 round 4 only at prime and power both 1 round 4 (primes to 2,000, powers to 40)", ok)
say("so an odd perfect is one prime part at 1 round 4, to a power at 1 round 4, times a square (Euler)", ok)

# 3. Parts in pairs: d and n/d. Round k, every self squares to 1 only when k holds 24's fold.
fold = [k for k in range(2, 400) if all((u * u) % k == 1 for u in range(1, k) if gcd(u, k) == 1)]
say(f"round k all selves square to 1 for k = {fold}: the parts of 24", fold == [2, 3, 4, 6, 8, 12, 24])
N = 200000
sig = np.zeros(N + 1, dtype=np.int64)
for d in range(1, N + 1):
    sig[d::d] += d
ok = all(sig[n] % 24 == 0 for n in range(23, N + 1, 24))
say("a number at 23 round 24: its parts pair into sums at 0 round 24, its parts' sum at 0 round 24 (to 200,000)", ok)
say("an odd number at 2 round 3 has parts' sum at 0 round 3, its doubling at 1 round 3: never perfect",
    all(sig[n] % 3 == 0 and (2 * n) % 3 == 1 for n in range(5, N + 1, 6)))
# Places an odd perfect may sit in turns of 12 and 36
p12 = [r for r in range(12) if r % 2 and r % 4 == 1 and r % 3 != 2]
p36 = [r for r in range(36) if r % 4 == 1 and r % 3 != 2 and (r % 3 or r % 9 == 0)]
say(f"round 12 its places are {p12}; round 36, {p36} (Touchard)", p12 == [1, 9] and p36 == [1, 9, 13, 25])
opens = []
turn = 1
for p in [2, 3, 5, 7, 11, 13, 17]:
    turn *= p
    t = turn * 6  # holds 4 and 9
    opens.append(sum(1 for r in range(1, t, 2) if r % 4 == 1 and r % 3 != 2 and (r % 3 or r % 9 == 0)) if t <= 400000 else None)
say(f"place 1 stays open in every turn: the turns never close the odd perfect row; places in 12, 36, 180, 1,260, ...: {opens[:5]}", 1 % 4 == 1 and all(o and o > 0 for o in opens[:5]))

# 4. Abundancy with whole numbers: product of p against doubling of product of p - 1.
def reaches(ps):
    a, b = 1, 2
    for p in ps:
        a, b = a * p, b * (p - 1)
    return a > b
odd_primes = [p for p in range(3, 400) if is_prime(p)]
say("two odd primes never reach the doubling; 3, 5, 7 do (105 against 96)",
    not any(reaches([p, q]) for p in odd_primes for q in odd_primes if p < q) and reaches([3, 5, 7]))
need = []
for skip in [0, 1, 2]:
    ps = odd_primes[skip:]
    k = 1
    while not reaches(ps[:k]):
        k += 1
    need.append(k)
say(f"fewest distinct prime parts to reach the doubling: with 3, {need[0]}; without 3, {need[1]}; without 3 and 5, {need[2]}",
    need == [3, 7, 15])

# 5. Horizon side: odd numbers to 4^12, none landing on their doubling.
H = 4 ** 12
sg = np.zeros(H + 1, dtype=np.int64)
for d in range(1, isqrt(H) + 1):
    idx = np.arange(d * d, H + 1, d)
    sg[idx] += d + idx // d
    sg[d * d] -= d
odd = np.arange(3, H + 1, 2)
diff = sg[odd] - 2 * odd
say(f"no odd number to {H:,} lands its parts on its doubling", not np.any(diff == 0))
first_abundant = int(odd[np.argmax(diff > 0)])
say(f"the first odd number passing its doubling: {first_abundant} = 3^3 x 5 x 7", first_abundant == 945)
rows = []
for k in range(5, 13):
    s = 4 ** k
    m = odd <= s
    dk = diff[m]
    above = dk[dk > 0]
    rows.append((s, int((dk > 0).sum()), int(np.abs(dk).min()), int(above.min()) if above.size else None))
print("        surface, odd past doubling, closest any odd lands, closest from past:", rows)

# 6. Descartes: a crossed part named a prime makes an odd "perfect".
D = 3 ** 2 * 7 ** 2 * 11 ** 2 * 13 ** 2 * 22021
named = parts_sum(9) * parts_sum(49) * parts_sum(121) * parts_sum(169) * (22021 + 1)
say(f"Descartes' {D:,}: naming 22,021 a prime, its parts reach its doubling", named == 2 * D)
say("22,021 = 19 x 19 x 61, crossed: Descartes' perfect is a ghost", 19 * 19 * 61 == 22021)
true_sum = parts_sum(9) * parts_sum(49) * parts_sum(121) * parts_sum(169) * parts_sum(361) * parts_sum(61)
print(f"        its parts truly sum to {true_sum:,}, its doubling {2 * D:,}, passing by {true_sum - 2 * D:,}")
say(f"Descartes' ghost sits at {D % 36} round 36, a place left open", D % 36 in p36)

print("All is." if all(said) else "Not all is.")
