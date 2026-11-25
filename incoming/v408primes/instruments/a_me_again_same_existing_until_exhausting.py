# v408primes · a me again is same-existing me, until a me is exhausting into all-parity.
# Across: a number's parity, odd or even by its prime parts. Its parts' parities added: a me or all-parity.
# Whole numbers alone. Execute: python3 -I a_me_again_same_existing_until_exhausting.py
N = 4 ** 10
spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
par = [0, 1] + [0] * (N - 1)
for n in range(2, N + 1):
    par[n] = -par[n // spf[n]]
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
def parts(n):
    return [d for d in range(1, n + 1) if n % d == 0]
say("a square is a me again at all its prime parts, two inversions a part: 36 = 2 x 2 x 3 x 3, parity %+d" % par[36], par[36] == 1)
say("36's parts %s, parities %s, added %d: a me" % (parts(36), [par[d] for d in parts(36)], sum(par[d] for d in parts(36))), sum(par[d] for d in parts(36)) == 1)
say("12's parts %s, parities %s, added %d: all-parity" % (parts(12), [par[d] for d in parts(12)], sum(par[d] for d in parts(12))), sum(par[d] for d in parts(12)) == 0)
# The parts' parities added, number by number: 1 at a square, 0 elsewhere (a sieve, to 1,048,576).
tot = [0] * (N + 1)
for d in range(1, N + 1):
    if par[d]:
        for m in range(d, N + 1, d):
            tot[m] += par[d]
say("a number's parts' parities add to 1 at a square, a me, and to 0 at all others, all-parity, to 1,048,576",
    all(tot[n] == (1 if int(n ** 0.5) ** 2 == n else 0) for n in range(1, N + 1)))
# All of a surface: every number's parts' parities added is the surface's side.
run, k, ok, rows = 0, 1, True, []
for n in range(1, N + 1):
    run += tot[n]
    if n == 4 ** k:
        rows.append((n, run)); ok = ok and run == 2 ** k; k += 1
say("all of a surface, every number's parts' parities added, is its side, the me's same-existing on it: %s" % rows, ok)
print("All is." if all(results) else "A line is-not.")
