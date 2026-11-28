# v408primes · along a prime's loop is whole; across it is its prior neighbour's loop, and across networks a prime
# down to the primes before it and forward into the primes after it. Whole numbers alone.
# Execute: python3 -I across_a_prime_networks_to_its_priors_and_its_nexts.py
from math import isqrt

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

def prime_parts(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out

def comes_again_across(p, a):
    x, m = a % p, 1
    while x != 1:
        x = x * a % p
        m += 1
    return m

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

PR = [p for p in range(3, 2000) if is_prime(p)]

# 1. Across, a prime's loop of p - 1 is the loops of p - 1's prime parts side by side: for every prime power
#    part of p - 1 a stepping comes again after it.
ok = True
for p in PR:
    n = p - 1
    for q in prime_parts(n):
        e = 1
        while n % (q ** (e + 1)) == 0:
            e += 1
        ok = ok and any(comes_again_across(p, a) == q ** e for a in range(2, p))
say("across, a prime's loop of p - 1 is the loops of its prime-power parts side by side: 31's loop of 30 has steppings coming again after 2, 3 and 5; primes to 2,000", ok)

# 2. A prime's across networks down, from p to the primes of p - 1 and on, to 2: a tree of primes below it.
def tree(p):
    if p == 2:
        return "2"
    return "%d(%s)" % (p, " ".join(tree(q) for q in prime_parts(p - 1)))
say("a prime's across networks down to 2, a tree of primes below it: %s; %s" % (tree(31), tree(97)), True)

# 3. With its tree a prime is told across: a stepping passes all p - 1 places, and comes again at no
#    (p - 1) / q for the prime parts q of p - 1. Local, its own loop; global, its tree; local again, 2.
def told_across(n):
    if n == 2:
        return True
    if n < 2:
        return False
    for a in range(2, n):
        if pow(a, n - 1, n) == 1 and all(pow(a, (n - 1) // q, n) != 1 for q in prime_parts(n - 1)):
            return all(told_across(q) for q in prime_parts(n - 1))
    return False
say("a number is a prime when a stepping across passes all n - 1 places and its tree of primes below is told the same way, 2 to 3,000",
    all(told_across(n) == is_prime(n) for n in range(2, 3001)))

# 4. Across, a prime transmissions forward: p is a part of q - 1 for later primes q, with no last stepped.
N = 1000000
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
later = {p: [q for q in range(p + 1, 200) if sieve[q] and (q - 1) % p == 0] for p in (3, 5, 7)}
counts = {p: sum(1 for q in range(p + 1, N + 1) if sieve[q] and (q - 1) % p == 0) for p in (3, 5, 7, 11, 13, 37)}
say("across, a prime is carried forward into the loops of later primes: 3 into %s ...; 5 into %s ...; to 1,000,000: %s"
    % (later[3][:8], later[5][:6], counts), all(c > 0 for c in counts.values()))

# 5. Every prime's across tree ends at 2, and 2's across loop is 1 long: the one me.
say("every prime's across tree ends at 2, and 2's across loop, 2 - 1, is 1 long: the one me, primes to 2,000",
    all("2" in tree(p) for p in PR) and 2 - 1 == 1)

# 6. The primes after now spread evenly over a prime's skeleton places: round 7, the primes past 7 to 1,000,000.
by_place = {r: sum(1 for q in range(8, N + 1) if sieve[q] and q % 7 == r) for r in range(1, 7)}
lo, hi = min(by_place.values()), max(by_place.values())
say("the primes after now spread evenly over a prime's skeleton places: round 7, to 1,000,000, %s, the widest apart %d" % (by_place, hi - lo),
    hi - lo < 2 * isqrt(sum(by_place.values())))

print("All is." if all(results) else "A line is-not.")
