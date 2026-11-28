# v408primes · two primes added at every even number, said as the between: every between past 1 has two living
# co-possiblings at some distance, podal about it. Stepped. Execute: python3 -I every_between_has_living_co_possiblings.py
from math import isqrt
N = 2000000
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
widest, at = 0, 0
ok = True
for c in range(2, N // 2 + 1):
    d = 0
    while not (sieve[c - d] and sieve[c + d]):
        d += 1
        if d >= c - 1:
            ok = False; break
    if d > widest: widest, at = d, c
print(("is     " if ok else "is-not ") + "every between from 2 to 1,000,000 has two living co-possiblings podal about it, at some distance; the farthest nearest pair is %d from its between, at %d" % (widest, at))
