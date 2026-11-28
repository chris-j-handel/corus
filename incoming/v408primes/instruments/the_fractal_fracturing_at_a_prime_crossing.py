# v408primes · a prime crossing as a fractal fracturing: a co-chaining bi-tunneling across it fracturing
# into a shorter-in-moments prime-length sequence and an exhausting parity. Whole numbers alone.
# Execute: python3 -I the_fractal_fracturing_at_a_prime_crossing.py

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

PRIMES = [n for n in range(2, 60) if is_prime(n)]
results = []

def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

def skeleton(ps):
    t = 1
    for p in ps:
        t *= p
    return t, [n for n in range(t) if all(n % p for p in ps)]

# 1. Resolver to resolver: the skeleton of the turn to p is inherited whole, lifted r ways, the turn apart.
#    A place's r lifts are a sequence of r moments, a prime length, shorter in moments than the turn.
# 2. The fracturing: of a place's r lifts, one is crossed by r, exhausted, and r - 1 go on.
# 3. The fractal: the places r crosses are the prior skeleton itself, stretched by r, whole.
ok1 = ok2 = ok3 = True
counts = [1]
for k in range(1, 7):
    t, s = skeleton(PRIMES[:k - 1]) if k > 1 else (1, [0])
    r = PRIMES[k - 1]
    t2, s2 = skeleton(PRIMES[:k])
    lifts = {a: [a + j * t for j in range(r)] for a in s}
    ok1 = ok1 and all(len(v) == r for v in lifts.values()) and t2 == t * r
    ok2 = ok2 and all(sum(1 for x in v if x % r == 0) == 1 for v in lifts.values())
    crossed = sorted(x for v in lifts.values() for x in v if x % r == 0)
    stretched = sorted(r * u for u in s) if k > 1 else [0]
    ok3 = ok3 and crossed == stretched
    counts.append(len(s2))
say("resolver to resolver, the prior skeleton is inherited whole, a place lifted r ways the turn apart, a prime-length sequence of r moments, turns 2 to 30,030", ok1)
say("of a place's r lifts, one is crossed by r and exhausted, and r - 1 go on: the skeleton's places %s" % counts[1:], ok2)
say("the places r crosses are the prior skeleton stretched by r, whole: at 7, %s" % sorted(7 * u for u in skeleton([2, 3, 5])[1]), ok3)

# 4. The fracturing opens at the prime's own square: below r x r the stretched skeleton crosses
#    no place the turn left uncrossed past r; at r x r it does.
ok = True
for k in range(2, 7):
    ps, r = PRIMES[:k - 1], PRIMES[k - 1]
    first = min(n for n in range(r + 1, r * r + 1) if n % r == 0 and all(n % p for p in ps))
    ok = ok and first == r * r
say("a new prime's fracturing of the skeleton opens at its own square: 9, 25, 49, 121, 169", ok)

# 5. The exhausting parity, read as a parity: a number fractured prime part by prime part inverts its parity
#    once at each part. Fractured in any order, the parts are the same and the parity is the same.
def all_fracturings(n):
    if n == 1:
        return {()}
    out = set()
    for p in range(2, n + 1):
        if n % p == 0 and is_prime(p):
            for rest in all_fracturings(n // p):
                out.add(tuple(sorted((p,) + rest)))
    return out

ok = all(len(all_fracturings(n)) == 1 for n in range(2, 600))
say("a crossed number fractured in any order comes to the same prime parts, one way alone, 2 to 599", ok)

# 6. The parities exhausted, summed over all numbers to a surface, stay close to the surface's side:
#    even and odd come out nearly half and half.
N = 4 ** 9
lam = [0, 1] + [0] * (N - 1)
spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
for n in range(2, N + 1):
    lam[n] = -lam[n // spf[n]]
even = sum(1 for n in range(1, N + 1) if lam[n] == 1)
odd = N - even
say("to the surface 262,144: %d numbers fracture to an even count of prime parts and %d to an odd, apart by %d, side 512" % (even, odd, odd - even), abs(odd - even) < 2 * 512)

print("All is." if all(results) else "A line is-not.")
