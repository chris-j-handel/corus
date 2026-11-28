# v408primes · ahead from co-resolving me-parities: societies of me-parities, kept or let go resolver to resolver,
# and back to the source. Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I societies_of_me_parities.py
from math import isqrt

N = 2000000
sieve = bytearray([1]) * (N + 20); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N + 19) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
PR = [p for p in range(2, 60) if sieve[p]]

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. The twin's between's me again arrives as a +1 round both co-possiblings.
say("a between's me again is 1 round both its co-possiblings: 144 round 11 and round 13 is 1, every even between to 1,000,000",
    all((c * c) % (c - 1) == 1 % (c - 1) and (c * c) % (c + 1) == 1 for c in range(4, 1000001, 2)) and 144 % 11 == 1 and 144 % 13 == 1)

# 2. A society of me-parities is a form of places: one at 0; a twin at 0 and 2; and on. Resolver to resolver, a
#    society's place is lifted r ways and the r-loop's seams cross as many of them as the society takes places round r.
def kept(form, primes):
    t, count = 1, 1
    rows = []
    for r in primes:
        taken = len({(-d) % r for d in form})          # lifts whose society has a place at r's seam
        count *= (r - taken)
        t *= r
        rows.append((t, count))
    return rows
one = kept([0], PR[:6])
twin = kept([0, 2], PR[1:6])
say("resolver to resolver, one me-parity keeps r - 1 of r: %s" % [c for t, c in one], [c for t, c in one] == [1, 2, 8, 48, 480, 5760])
say("a twin's places, lifted r ways, keep r - 2 of r, two crossed: round 6, 30, 210, 2,310, 30,030: %s" % [c for t, c in kept([0, 2], [3, 5, 7, 11, 13])],
    [c for t, c in kept([0, 2], [3, 5, 7, 11, 13])] == [1, 3, 15, 135, 1485])

# 3. Counted whole: round 210, the betweens whose co-possiblings no loop of 2, 3, 5, 7 crosses are 15.
tw210 = [c for c in range(210) if all((c - 1) % p and (c + 1) % p for p in (2, 3, 5, 7))]
say("round 210, the betweens with both co-possiblings uncrossed are %d: %s" % (len(tw210), tw210), len(tw210) == 15)

# 4. Three in a row two apart: one of any three odd numbers two apart is at 3's seam, so 3, 5, 7 is the one society of
#    three two apart, the opening round's last three. With all numbers, by the loop of 3.
say("of any three odds two apart, one is at 3's seam, round 3 all three places taken: 3, 5, 7 is the one such society, to 2,000,000",
    len({(-d) % 3 for d in (0, 2, 4)}) == 3 and [p for p in range(3, N, 2) if sieve[p] and sieve[p + 2] and sieve[p + 4]] == [3])

# 5. Societies of three kept: (0, 2, 6) and (0, 4, 6) keep places at every resolver; (0, 2, 4) keeps none past 3.
say("a society of three at 0, 2, 4 keeps %s, and at 0, 2, 6 keeps %s, at 0, 4, 6 %s, round 3 to 13"
    % ([c for t, c in kept([0, 2, 4], [3, 5, 7, 11, 13])], [c for t, c in kept([0, 2, 6], [3, 5, 7, 11, 13])], [c for t, c in kept([0, 4, 6], [3, 5, 7, 11, 13])]),
    kept([0, 2, 4], [3])[0][1] == 0 and all(c > 0 for t, c in kept([0, 2, 6], [3, 5, 7, 11, 13])))

# 6. Two twins co-resolving, a society of four at 0, 2, 6, 8, the closest four past 5, sit about 15 round 30, the fold of 30.
quads = [p for p in range(7, N) if sieve[p] and sieve[p + 2] and sieve[p + 6] and sieve[p + 8]]
say("two twins co-resolving, at p, p + 2, p + 6, p + 8: %d to 2,000,000, from %s, every one's between p + 4 at 15 round 30, the fold of 30"
    % (len(quads), quads[:5]), all((p + 4) % 30 == 15 for p in quads))

# 7. Stepped with no last: one, two, three and four co-resolving, counted between surfaces of 4 to the k.
def per_surface(form):
    out = []
    for k in range(5, 11):
        lo, hi = 4 ** (k - 1), 4 ** k
        out.append(sum(1 for p in range(max(lo, 7), hi) if all(sieve[p + d] for d in form)))
    return out
forms = {"one": [0], "twin": [0, 2], "three at 0, 2, 6": [0, 2, 6], "four": [0, 2, 6, 8]}
rows = {name: per_surface(f) for name, f in forms.items()}
for name, r in rows.items():
    print("        %-17s between the surfaces 256 to 1,048,576: %s" % (name, r))
say("one, two, three and four co-resolving, more at every span between surfaces 256 to 1,048,576", all(all(b > a for a, b in zip(r, r[1:])) for r in rows.values()))

# 8. Back to the source: the twins' betweens are seams of 6, the turn of the opening's 2 and 3; the one three is 3, 5, 7,
#    the opening round; the four sit about the fold of 30, the turn of 2, 3 and 5. The societies are shaped by the
#    opening's loops alone.
say("back to the source: the societies' places are set by the loops of 2, 3 and 5, the opening round's",
    all(c % 6 == 0 for c in range(6, N, 2) if sieve[c - 1] and sieve[c + 1]) and all((p + 4) % 30 == 15 for p in quads))

print("All is." if all(results) else "A line is-not.")
