# v408primes · all-parity is odd even odd; unrelationing other-thans from all-parity is the method of me-parity;
# odd even odd is local global local. Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I odd_even_odd_all_parity_and_me_parity.py
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

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. Along, the +1 is odd even odd: every +1 inverts odd and even.
say("along, every +1 inverts odd and even: 1 odd, 2 even, 3 odd, ... to 1,000,000",
    all((n % 2) != ((n + 1) % 2) for n in range(1, 1000001)))

# 2. Across, odd by odd is odd and an even part makes even: across holds what along alternates.
say("across, odd by odd is odd, and a number with an even part is even, to 1,000 by 1,000",
    all(((a * b) % 2 == 1) == (a % 2 == 1 and b % 2 == 1) for a in range(1, 1001) for b in range(1, 1001)))

# 3. Unrelationing other-thans from all-parity: from all the numbers, the other-thans of 2, then of 3, then of 5 ...
#    unrelationed; what is left past the prior primes and short of the next prime's square is the primes,
#    the me-parities.
left, steps, ok = list(range(2, 10000)), [], True
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
    left = [n for n in left if n == p or n % p]
    nxt = min(n for n in left if n > p)
    ok = ok and all(is_prime(n) for n in left if n < nxt * nxt)
    if p <= 7:
        steps.append((p, len([n for n in left if n < 210])))
say("unrelationing the other-thans of 2, 3, 5, 7 ... from all the numbers leaves the me-parities, the primes, to the next prime's square: below 210, left after 2, 3, 5, 7: %s" % steps,
    ok and left == [n for n in range(2, 10000) if is_prime(n)])

# 4. Odd even odd, local global local: a prime's across tree read down alternates odd, a prime, and even, its
#    across loop, to the one me, 1, odd.
def chain(p):
    # odd, a prime; even, its across loop p - 1; odd, the loop's largest odd prime part, or the one me, 1,
    # when the loop is all 2's.
    out = [p]
    while p > 1:
        p = p - 1
        out.append(p)
        odd = [q for q in prime_parts(p) if q % 2]
        p = max(odd) if odd else 1
        out.append(p)
    return out
c31, c97, c1999 = chain(31), chain(97), chain(1999)
alt = all(all((a % 2) != (b % 2) for a, b in zip(chain(p), chain(p)[1:])) and chain(p)[-1] == 1
          for p in range(3, 5000) if is_prime(p))
say("a prime's across tree read down by its largest odd part alternates odd and even to the one me: 31 %s; 97 %s; 1,999 %s; primes to 5,000"
    % (c31, c97, c1999), alt)

print("All is." if all(results) else "A line is-not.")
