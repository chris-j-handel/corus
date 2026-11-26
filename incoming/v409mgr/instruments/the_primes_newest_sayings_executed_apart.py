# v409mgr · the primes session's newest sayings, executed apart by this session's own short program.
# It opens no file of the set. Execute: python3 -I the_primes_newest_sayings_executed_apart.py
from math import gcd, isqrt
import random, time

t0 = time.time()
def say(name, ok, more=""):
    print(("is      " if ok else "IS-NOT  ") + name + ((" · " + more) if more else ""))

def sieve(n):
    b = bytearray([1]) * (n + 1); b[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if b[i]:
            b[i*i::i] = bytearray(len(range(i*i, n + 1, i)))
    return b

# 1. the seam of the primes to 17 and its living places
seam = 2*3*5*7*11*13*17
places = sum(1 for k in range(seam) if gcd(k, seam) == 1)
say("the seam of the primes to 17 is 510,510", seam == 510510)
say("its places crossed by none of them are 92,160", places == 92160, str(places))

# 2. the millionth prime, and the primes to 200,000
N = 16_000_000
b = sieve(N)
count = 0; millionth = None; to200k = 0
for i in range(N + 1):
    if b[i]:
        count += 1
        if i <= 200_000: to200k += 1
        if count == 1_000_000: millionth = i; break
say("the millionth prime is 15,485,863", millionth == 15_485_863, str(millionth))
say("the primes to 200,000 are 17,984", to200k == 17_984, str(to200k))

# 3. the largest prime seen to now, never written out whole: 2^E - 1
E = 136_279_841
say("its number of doublings is one past a seam of 4", E % 4 == 1)
say("it is at the place 409,531 round 510,510", (pow(2, E, seam) - 1) % seam == 409_531, str((pow(2, E, seam) - 1) % seam))
say("the place 409,531 is crossed by none of the primes to 17", gcd(409_531, seam) == 1)
say("it is 1 round 30 and 1 round 6", (pow(2, E, 30) - 1) % 30 == 1 and (pow(2, E, 6) - 1) % 6 == 1)
claimed = {2: 3, 6: 37, 10: 11, 12: 43, 16: 17, 28: 2099, 30: 31}
for t, q in claimed.items():
    say(f"+{t} is crossed by {q:,}", (pow(2, E, q) - 1 + t) % q == 0)

# 4. the places about it uncrossed by all primes to 10,000,000, within 100 back and 100 on
P = sieve(10_000_000)
primes = [i for i in range(2, 10_000_001) if P[i]]
left = set(t for t in range(-100, 101) if t != 0)
least = {}
for q in primes:
    r = (pow(2, E, q) - 1) % q
    for t in list(left):
        if (r + t) % q == 0:
            least[t] = q; left.discard(t)
on = sorted(t for t in left if t > 0); back = sorted((t for t in left if t < 0), reverse=True)
say("on from it, uncrossed to 10,000,000: +22, +70 and +100", on == [22, 70, 100], str(on))
say("back from it, uncrossed to 10,000,000: -48, -72 and -90", back == [-48, -72, -90], str(back))
by17 = [t for t in range(1, 101) if all((pow(2, E, q) - 1 + t) % q for q in (2, 3, 5, 7, 11, 13, 17))]
say("the primes to 17 leave 19 places on from it to +100", len(by17) == 19, str(len(by17)))

# 5. the smaller primes one less than a doubling, and their next primes
def strong(n, a):
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    x = pow(a, d, n)
    if x in (1, n - 1): return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1: return True
    return False
def by_trial(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
say("8,191 + 18 is a prime, by all its loops to its side", by_trial(8191 + 18) and not any(by_trial(8191 + k) for k in range(1, 18)))
say("131,071 + 30 is a prime, by all its loops to its side", by_trial(131071 + 30) and not any(by_trial(131071 + k) for k in range(1, 30)))
random.seed(409)
def likely(n, rounds=40):
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    return all(strong(n, random.randrange(2, n - 1)) for _ in range(rounds))
for e, t in ((89, 30), (521, 888), (2281, 310)):
    m = 2**e - 1
    nxt = next(k for k in range(1, 5000) if likely(m + k))
    say(f"past 2^{e} - 1 the next number passing a test of 40 drawn bases is at +{t}", nxt == t, f"+{nxt} · tested, not whole: no loop to its side is gone through")

# 6. a row of 14 primes at equal steps, and doubling closing round a prime's own square
row = [31_385_539 + 420_420 * n for n in range(14)]
say("31,385,539 + 420,420 n is 14 primes, its last 36,850,999", all(by_trial(x) for x in row) and row[-1] == 36_850_999)
w = [q for q in primes if pow(2, q - 1, q * q) == 1]
say("to 10,000,000, doubling closes round a prime's own square at 1,093 and 3,511 alone", w == [1093, 3511], str(w))

# 7. the twins' parts of one, in 1 to 17
from fractions import Fraction
tw = [(p, p + 2) for p in range(3, 16) if by_trial(p) and by_trial(p + 2) and p + 2 <= 17]
s = sum(Fraction(1, a) + Fraction(1, c) for a, c in tw)
say("the twins' parts of one in 1 to 17 are 15,676/15,015", s == Fraction(15676, 15015), f"{s} of {tw}")
print(f"executed in {time.time() - t0:.0f} seconds")
