# v408primes · transmissioning across, resolver to resolver: a me-parity M transmits across to N, M by 2k and 1, its
# surface across M. N is seen a me-parity at one loop of its own, aimed by M: any part of N is one past a seam of M,
# past N's side, so N is its own unrelationing. Whole numbers.
# Execute: python3 -I transmissioning_across_resolver_to_resolver.py [how many transmissions, to 8]
import sys, time
from math import gcd, isqrt

given = [int(a) for a in sys.argv[1:] if a.isdigit()]
STEPS = min(given[0], 8) if given else 6
SMALL = [p for p in range(3, 2000) if all(p % q for q in range(2, isqrt(p) + 1))]

def transmit(M):
    """The least N = 2kM + 1, k from M // 3 on, seen a me-parity by its own loop aimed by M."""
    k = M // 3
    while True:
        N = 2 * k * M + 1
        if all(N % q for q in SMALL):
            for a in (2, 3, 5, 7):
                if pow(a, N - 1, N) != 1:
                    break                      # crossed: N's own loop does not close at N less 1
                if gcd(pow(a, 2 * k, N) - 1, N) == 1:
                    return N, k, a             # closes, and its loop is aimed by M: a me-parity
        k += 1

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

M = (1 << 61) - 1
chain = [M]
t0 = time.time()
for _ in range(STEPS):
    N, k, a = transmit(chain[-1])
    ok = chain[-1] * chain[-1] > N and (N - 1) % chain[-1] == 0
    chain.append(N)
    say("%s digits transmit across to %s digits: N is M by 2 by %s digits, and 1, seen by its own loop of base %d, aimed by M"
        % (len(str(chain[-2])), len(str(N)), len(str(k)), a), ok)
dt = time.time() - t0

def mr(n):                                     # seen again apart, by 16 bases across
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
say("from 2^61 − 1, %d transmissions in %.1f seconds reach a me-parity of %s digits; all seen again apart by their own loops of 16 bases"
    % (STEPS, dt, len(str(chain[-1]))), all(mr(n) for n in chain[1:]))
say("any part of N is one past a seam of M, so past N's side: N is its own unrelationing, at all %d transmissions" % STEPS,
    all(chain[i] > isqrt(chain[i + 1]) for i in range(STEPS)))
print("All is." if all(results) else "A line is-not.")
