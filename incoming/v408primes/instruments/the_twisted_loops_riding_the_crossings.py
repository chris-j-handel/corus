# v408primes · the prime skeleton on natural torusing: a prime's twisted loop round 24 and round 60,
# riding the crossings and arriving as a +1. Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I the_twisted_loops_riding_the_crossings.py

N = 100000

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

PRIMES = [n for n in range(2, N) if is_prime(n)]
results = []

def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

def places(turn):
    return [n for n in range(turn) if n % 2 and n % 3 and n % 5] if turn % 5 == 0 else \
           [n for n in range(turn) if n % 2 and n % 3]

S24, S60, S120 = places(24), places(60), places(120)

# 1. The skeleton: round 24 the small direction, round 60 the large, round 120 both.
say("the skeleton's places: round 24 %s, round 60 %d places, round 120 %d places" % (S24, len(S60), len(S120)),
    len(S24) == 8 and len(S60) == 16 and len(S120) == 32)
say("all primes past 5 are at the skeleton's places round 120, primes to 100,000",
    all(p % 120 in S120 for p in PRIMES if p > 5))

# 2. A prime is the between of its two podal neighbours, p - 1 and p + 1, both crossed, past 3.
say("a prime past 3 is the between of p - 1 and p + 1, both crossed, primes to 100,000",
    all(not is_prime(p - 1) and not is_prime(p + 1) for p in PRIMES if p > 3))

# 3. Two priors crossing, and a +1 next: the two neighbours multiplied are a crossing of 24,
#    and the +1 from it is the prime's square, at 1 round 24. The small direction, out and back in two.
say("(p - 1) x (p + 1) is a crossing of 24, and the +1 from it is p x p, at 1 round 24, primes 5 to 100,000",
    all(((p - 1) * (p + 1)) % 24 == 0 and (p * p) % 24 == 1 for p in PRIMES if p > 3))

# 4. A second bi-folding: the square's two neighbours multiplied are a crossing of 240, and so of 60 and
#    of 120, and the +1 from it is the prime's fourth, at 1 round 60 and round 120. The large direction.
say("(p x p - 1) x (p x p + 1) is a crossing of 240, and the +1 from it is p to the fourth, at 1 round 60 and 120, primes 7 to 100,000",
    all(((p * p - 1) * (p * p + 1)) % 240 == 0 and pow(p, 4, 120) == 1 for p in PRIMES if p > 5))

# 5. The twisted loop: round 24 a prime is back at 1 in two multiplyings; round 60 in four, or in two
#    for a prime one more or one less than a number of fives. On the torus of 24 and 60, 7 goes
#    (7, 7), (1, 49), (7, 43), (1, 1): out and back twice in the small direction, once round the large.
def loop(p):
    out, x = [], p
    while True:
        out.append((x % 24, x % 60))
        if x % 24 == 1 and x % 60 == 1:
            return out
        x = x * p

ok = True
for p in PRIMES:
    if p <= 5:
        continue
    l = loop(p)
    want = 1 if p % 120 == 1 else (2 if p % 5 in (1, 4) else 4)
    ok = ok and len(l) == want and all(a == 1 for a, b in l[1::2])
say("a prime's twisted loop on the torus of 24 and 60 is four places, two for one more or one less than a number of fives, one for a prime at 1 round 120, at 1 in the small direction at every second place; 7: %s" % loop(7), ok)

# 6. The loop rides the skeleton: a skeleton place multiplied by a skeleton place is a skeleton place.
say("a skeleton place multiplied by a skeleton place is a skeleton place, round 24, 60 and 120",
    all((a * b) % t in set(s) for t, s in ((24, S24), (60, S60), (120, S120)) for a in s for b in s))

# 7. Co-possibling, the between of the podalings: the skeleton's places fold about the half, n and turn - n,
#    and the pair nearest the fold is the -1 and the +1 of the fold's crossing: 11 and 13 about 12,
#    29 and 31 about 30, 59 and 61 about 60.
ok = all((24 - n) in S24 for n in S24) and all((60 - n) in S60 for n in S60) and all((120 - n) in S120 for n in S120)
near = [(max(n for n in s if n < t // 2), min(n for n in s if n > t // 2)) for t, s in ((24, S24), (60, S60), (120, S120))]
say("the skeleton folds onto itself about its half, and the pair nearest the fold is its crossing's -1 and +1: %s" % near,
    ok and near == [(11, 13), (29, 31), (59, 61)])

print("All is." if all(results) else "A line is-not.")
