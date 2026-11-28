# v408primes · a prime is a loop p moments long, coming again after the same prime length every time;
# the +1 me living in it while the loop returns around enough on its surface. Whole numbers alone.
# Execute: python3 -I a_prime_loop_and_the_me_living_in_it.py
from math import isqrt, gcd

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

def comes_again(n, k):
    place, moments = 0, 0
    while True:
        place = (place + k) % n
        moments += 1
        if place == 0:
            return moments

# 1-2. A prime's loop stepped by any k from 1 to p - 1 comes again after p moments, every time.
say("a prime's loop, stepped by any k from 1 to p - 1, comes again after p moments, the same prime length every time, primes to 500",
    all(comes_again(p, k) == p for p in range(2, 500) if is_prime(p) for k in range(1, p)))

# 3. A crossed number's loop stepped by a part comes again short: a shorter, prime-length sequence.
say("a crossed loop stepped by a part comes again short: 15 by 5 after %d, by 3 after %d; 30 by 10 after %d, by 6 after %d, by 15 after %d"
    % (comes_again(15, 5), comes_again(15, 3), comes_again(30, 10), comes_again(30, 6), comes_again(30, 15)),
    all(any(comes_again(n, k) < n for k in range(1, n)) for n in range(4, 500) if not is_prime(n)))

# 4. The steppings that keep a loop whole are its skeleton places.
whole30 = [k for k in range(1, 30) if comes_again(30, k) == 30]
say("the steppings that keep the loop of 30 whole are its skeleton places: %s" % whole30,
    whole30 == [1, 7, 11, 13, 17, 19, 23, 29] and
    all([k for k in range(1, n) if comes_again(n, k) == n] == [k for k in range(1, n) if gcd(n, k) == 1] for n in range(2, 300)))

# 5. Along, a loop's places added are 0 round it, for every odd length: all-parity.
say("along, a loop's places 0 to n - 1 added are 0 round n, for every odd n to 2,001",
    all(sum(range(n)) % n == 0 for n in range(1, 2002, 2)))

# 6. Across, a prime loop's places multiplied are -1 round it, other-than; a crossed loop's, past 4, are 0, exhausted.
def all_multiplied(n):
    r = 1
    for k in range(1, n):
        r = r * k % n
    return r
say("across, a prime loop's places 1 to p - 1 multiplied are p - 1, a -1 round p; a crossed loop's past 4 are 0; 4's are %d; to 2,000"
    % all_multiplied(4),
    all(all_multiplied(n) == (n - 1 if is_prime(n) else 0) for n in range(5, 2001)) and all_multiplied(4) == 2)

# 7. The +1 me lives in the loop of p while the loop returns around p times on its surface: p to the side.
ok = all([p for p in range(2, n + 1) if is_prime(p) and n // p >= p] == [p for p in range(2, isqrt(n) + 1) if is_prime(p)]
         for n in range(2, 5000))
say("on a surface n, a prime's loop returns around its own length of times only for the primes to its side, its me's, to 5,000", ok)

# 8. A number is a prime when no loop returning around its own length of times on its surface crosses it.
say("a number is a prime when no prime loop returning around its own length of times on its surface crosses it, 2 to 20,000",
    all(is_prime(n) == all(n % p for p in range(2, isqrt(n) + 1) if is_prime(p)) for n in range(2, 20001)))

# 9. Across, a prime's loop is p - 1 long: a stepping by multiplying comes again after a part of p - 1.
def comes_again_across(p, a):
    x, m = a % p, 1
    while x != 1:
        x = x * a % p
        m += 1
    return m
say("across, round a prime, a stepping by multiplying comes again after a part of p - 1: round 7, 2 after %d, 3 after %d, 6 after %d; primes to 500"
    % (comes_again_across(7, 2), comes_again_across(7, 3), comes_again_across(7, 6)),
    all((p - 1) % comes_again_across(p, a) == 0 for p in range(3, 500) if is_prime(p) for a in range(1, p)))

# 10. Some multiplying passes all p - 1 places, and their count is the skeleton count of p - 1.
ok = True
for p in range(3, 500):
    if is_prime(p):
        full = [a for a in range(1, p) if comes_again_across(p, a) == p - 1]
        ok = ok and len(full) == sum(1 for k in range(1, p) if gcd(p - 1, k) == 1) and len(full) > 0
say("round a prime, the multiplyings passing all p - 1 places are as many as the skeleton places of p - 1: round 7, %s; primes to 500"
    % [a for a in range(1, 7) if comes_again_across(7, a) == 6], ok)

print("All is." if all(results) else "A line is-not.")
