# v408primes · following is: the side of a surface is its same-existing me's, the squares.
# Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I the_side_its_same_existing_mes.py   (about a minute)
from math import isqrt

N = 4 ** 11
results = []

def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

spf = list(range(N + 1))
for i in range(2, isqrt(N) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
across = [0, 1] + [0] * (N - 1)   # odd or even by the count of prime parts
along = [0, 1] + [0] * (N - 1)    # a prime part twice exhausted to 0
for n in range(2, N + 1):
    p, m = spf[n], n // spf[n]
    across[n] = -across[m]
    along[n] = 0 if m % p == 0 else -along[m]
L = [0] * (N + 1)
M = [0] * (N + 1)
for n in range(1, N + 1):
    L[n] = L[n - 1] + across[n]
    M[n] = M[n - 1] + along[n]

# 1. The me's of a surface are a whole count on every surface, square or not.
say("the me's on a surface are a whole count on every surface, square or not: 1,000 has 31 me's, 1,024 has 32, surfaces to 1,500",
    all(sum(1 for s in range(1, 40) if s * s <= X) == isqrt(X) for X in range(1, 1500)) and isqrt(1000) == 31)

# 2. Every number is a me again multiplied by a number with no prime part twice, one way alone.
def me_and_rest(n):
    s = 1
    m = n
    while m > 1:
        p = spf[m]; c = 0
        while m % p == 0:
            m //= p; c += 1
        s *= p ** (c // 2)
    return s * s, n // (s * s)
ok = True
for n in range(1, 100001):
    a, q = me_and_rest(n)
    ways = [(d * d, n // (d * d)) for d in range(1, isqrt(n) + 1) if n % (d * d) == 0 and along[n // (d * d)] != 0]
    ok = ok and ways == [(a, q)]
say("every number is a me again multiplied by a number with no prime part twice, one way alone: 72 = %d x %d, 50 = %d x %d, to 100,000"
    % (me_and_rest(72) + me_and_rest(50)), ok)

# 3. A number's odd or even is its no-square part's: the me again adds no inversion.
say("a number's odd or even is the odd or even of its part with no prime part twice, to 4,194,304",
    all(across[n] == along[me_and_rest(n)[1]] for n in range(1, 200001)) and
    all(across[n] == along[me_and_rest(n)[1]] for n in range(N - 200000, N + 1)))

# 4. Across: all the spirals' seams on a surface, each seam carrying its spiral's odd or even, add to its me's.
cum, run, ok = [0] * (N + 1), 0, True
tot = [0] * (N + 1)
for d in range(1, N + 1):
    if across[d]:
        for mm in range(d, N + 1, d):
            tot[mm] += across[d]
for n in range(1, N + 1):
    run += tot[n]
    ok = ok and run == isqrt(n)
say("across, all the spirals' seams on a surface, each carrying its spiral's odd or even, add to the surface's me's, every surface to 4,194,304", ok)

# 5. Along: all the seams carrying the exhausted parity add to 1, one me.
tot = [0] * (N + 1)
for d in range(1, N + 1):
    if along[d]:
        for mm in range(d, N + 1, d):
            tot[mm] += along[d]
run, ok = 0, True
for n in range(1, N + 1):
    run += tot[n]
    ok = ok and run == 1
say("along, all the seams carrying the exhausted parity add to 1, one me, every surface to 4,194,304", ok)

# 6. The across lead is the along lead of the surface and of its shrunk copies at every me: X, X/4, X/9 ...
ok = all(L[X] == sum(M[X // (k * k)] for k in range(1, isqrt(X) + 1)) for X in list(range(1, 30001)) + [4 ** k for k in range(8, 12)])
say("the across lead is the along leads of the surface and of its copies shrunk at every me, added: L(X) = M(X) + M(X/4) + M(X/9) + ..., to 30,000 and the surfaces to 4,194,304", ok)

# 7. The numbers with no prime part twice are counted by the me's carrying the exhausted parity.
nosq = [0] * (N + 1)
for n in range(1, N + 1):
    nosq[n] = nosq[n - 1] + (1 if along[n] else 0)
ok = all(nosq[X] == sum(along[d] * (X // (d * d)) for d in range(1, isqrt(X) + 1)) for X in list(range(1, 20001)) + [4 ** k for k in range(8, 12)])
say("the numbers with no prime part twice on a surface are the me's, each carrying its side's exhausted parity, times the surface shrunk by it: %d of 4,194,304" % nosq[N], ok)

# 8. Odd leads, and it is the large me's: the copies shrunk smaller than 100 carry the opening numbers'
#    along lead, which leans odd, and they lean the across lead odd by about half the side.
rows = []
for k in range(6, 12):
    X = 4 ** k
    small = sum(M[X // (j * j)] for j in range(1, isqrt(X) + 1) if X // (j * j) < 100)
    rows.append((X, isqrt(X), L[X], small))
for X, s, lx, sm in rows:
    print("        surface %9d  me's %5d  lead %5d  from the copies smaller than 100 %5d" % (X, s, lx, sm))
say("the along lead of the opening numbers leans odd, %s, and the copies at the large me's lean the across lead odd by between a third and a half of the me's on all surfaces 4,096 to 4,194,304" % [M[y] for y in range(1, 14)],
    all(-s // 2 <= sm <= -s // 3 for X, s, lx, sm in rows))

# 9. The hair said with whole numbers: for a whole k, the lead multiplied by itself 2k times beside the
#    surface multiplied by itself k + 2 times. Stepped: the last surface where the lead reaches it.
lasts = {}
for k in (10, 20, 50, 100):
    last = 1
    for n in range(2, N + 1):
        a = abs(L[n])
        if a * a >= n and a >= n ** ((k + 2) / (2 * k)) * 0.999 and a ** (2 * k) >= n ** (k + 2):
            last = n
    lasts[k] = last
say("the lead multiplied by itself 2k times passes the surface multiplied by itself k + 2 times last at: %s, of surfaces to 4,194,304" % lasts,
    lasts[10] == 1 and lasts[20] == 1 and lasts[50] < 100000)

print("All is." if all(results) else "A line is-not.")
