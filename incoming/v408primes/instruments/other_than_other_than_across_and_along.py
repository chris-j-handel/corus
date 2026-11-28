# v408primes · other-than-other-than across and along: multiplied, a me again; added, a 0.
# Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I other_than_other_than_across_and_along.py

N = 100000
results = []

def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
across = [0, 1] + [0] * (N - 1)   # other-than-other-than multiplied: a me again
along = [0, 1] + [0] * (N - 1)    # a prime part twice exhausted: a 0
for n in range(2, N + 1):
    p, m = spf[n], n // spf[n]
    across[n] = -across[m]
    along[n] = 0 if m % p == 0 else -along[m]

def parts(n):
    return [d for d in range(1, n + 1) if n % d == 0]

say("across, multiplied, two inversions are a me again: -1 by -1 is +1", (-1) * (-1) == 1)
say("along, added, a self and its other-than are a 0: +1 and -1 is 0", 1 + (-1) == 0)
say("a prime part twice, across, is a me again: 4, 9, 25, 49 are +1", all(across[p * p] == 1 for p in (2, 3, 5, 7)))
say("along, the parities of 12's parts %s are %s, added 0" % (parts(12), [along[d] for d in parts(12)]),
    sum(along[d] for d in parts(12)) == 0)
say("along, the parities of all a number's parts add to 0, at every number past 1, to 100,000",
    all(sum(along[d] for d in parts(n)) == 0 for n in range(2, 3001)) and
    all(sum(along[d] for d in range(1, int(n ** 0.5) + 1) if n % d == 0) +
        sum(along[n // d] for d in range(1, int(n ** 0.5) + 1) if n % d == 0 and d * d != n) == 0
        for n in range(3001, N + 1)))
say("across, the parities of a number's parts add to 1 at a square and to 0 at all others, to 100,000",
    all((sum(across[d] for d in range(1, int(n ** 0.5) + 1) if n % d == 0) +
         sum(across[n // d] for d in range(1, int(n ** 0.5) + 1) if n % d == 0 and d * d != n))
        == (1 if int(n ** 0.5) ** 2 == n else 0) for n in range(1, N + 1)))

print("All is." if all(results) else "A line is-not.")
