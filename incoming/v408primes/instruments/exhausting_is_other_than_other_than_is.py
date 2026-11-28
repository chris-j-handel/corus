# v408primes · exhausting is other-than-other-than-is: a prime part fractured twice, exhausted to a 0,
# beside the reading of other-than-other-than as is again. Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I exhausting_is_other_than_other_than_is.py

N = 4 ** 11
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

# again[n]: parity with other-than-other-than read as is again (a me again).
# exhausted[n]: parity with a prime part fractured twice exhausted to 0.
again = [0, 1] + [0] * (N - 1)
exhausted = [0, 1] + [0] * (N - 1)
for n in range(2, N + 1):
    p, m = spf[n], n // spf[n]
    again[n] = -again[m]
    exhausted[n] = 0 if m % p == 0 else -exhausted[m]

def show(n):
    parts, m = [], n
    while m > 1:
        parts.append(spf[m]); m //= spf[m]
    return "%d = %s: again %+d, exhausted %+d" % (n, " x ".join(map(str, parts)), again[n], exhausted[n])

say("a fracturing is one other-than, and a prime part twice is other-than-other-than: %s; %s; %s; %s"
    % (show(30), show(12), show(36), show(49)),
    (again[30], exhausted[30], again[12], exhausted[12], again[36], exhausted[36]) == (-1, -1, -1, 0, 1, 0))

# Every new prime's fracturing of the skeleton opens at its own square, an other-than-other-than: a 0.
say("the opening of every new prime's fracturing, its own square, is exhausted: 4, 9, 25, 49, 121, 169 are 0s",
    all(exhausted[p * p] == 0 and again[p * p] == 1 for p in (2, 3, 5, 7, 11, 13)))

zeros = sum(1 for n in range(1, N + 1) if exhausted[n] == 0)
plus = sum(1 for n in range(1, N + 1) if exhausted[n] == 1)
minus = N - zeros - plus
say("to the surface 4,194,304: %d exhausted to 0, %d is, %d other-than" % (zeros, plus, minus), zeros + plus + minus == N)

# The two leads on the surfaces of 4 to the k, beside the side.
A = E = 0; maxA = maxE = 0; k = 1; side = 2; rows = []; returns = 0; returns_by_surface = []
for n in range(1, N + 1):
    A += again[n]; E += exhausted[n]
    if E == 0:
        returns += 1
    maxA = max(maxA, abs(A)); maxE = max(maxE, abs(E))
    if n == 4 ** k:
        rows.append((n, side, maxA, maxE))
        returns_by_surface.append(returns)
        k += 1; side *= 2
for n, s, a, e in rows:
    print("        surface %9d  side %5d  lead, again %5d%s  lead, exhausted %4d" % (n, s, a, "  past the side" if a > s else "", e))
say("with other-than-other-than exhausted, the lead stays short of the side on all surfaces to 4,194,304",
    all(e < s for n, s, a, e in rows))
say("with other-than-other-than read as is again, the lead passes the side from the surface of 4,096 on",
    [n for n, s, a, e in rows if a > s][0] == 4096 and all(a > s for n, s, a, e in rows if n >= 4096))
say("the exhausted lead comes back to 0, more the farther out: returns by surface %s" % returns_by_surface,
    all(b > a for a, b in zip(returns_by_surface[2:], returns_by_surface[3:])))

# Both readings carry one another: a number's again-parity is the exhausted parities of it with its square
# parts taken out, added.
ok = True
for n in range(1, 20001):
    s, d = 0, 1
    while d * d <= n:
        if n % (d * d) == 0:
            s += exhausted[n // (d * d)]
        d += 1
    ok = ok and s == again[n]
say("a number's again-parity is the exhausted parities of the number with its square parts taken out, added, 1 to 20,000", ok)

print("All is." if all(results) else "A line is-not.")
