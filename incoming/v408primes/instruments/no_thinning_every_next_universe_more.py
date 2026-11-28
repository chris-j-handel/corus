# v408primes · there is no thinning: every next universe carries the living me-parities of its prior whole, and more.
# Whole counts alone. Execute: python3 -I no_thinning_every_next_universe_more.py
from math import isqrt
N = 2 ** 22
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
# 1. Turn to turn, the skeleton is carried whole and its living places multiply: 1, 2, 8, 48, 480, 5,760, 92,160.
places, t, rows = 1, 1, []
for p in (2, 3, 5, 7, 11, 13, 17):
    places *= p - 1; t *= p; rows.append(places)
say("turn to turn, the living places are carried whole and multiply: %s" % rows, all(b > a for a, b in zip(rows[1:], rows[2:])))
# 2. Span to span, doubling to doubling, the me-parities are never fewer, and from 16 on more at every span.
spans = [sum(sieve[n] for n in range(2 ** k + 1, 2 ** (k + 1) + 1)) for k in range(1, 22)]
say("doubling to doubling, the me-parities of a span are never fewer than the span before: %s" % spans[:12],
    all(b >= a for a, b in zip(spans, spans[1:])) and all(b > a for a, b in zip(spans[3:], spans[4:])))
# 3. Surface to surface, by 4, more at every span: and every span carries more than all the spans before it together.
four = [sum(sieve[n] for n in range(4 ** (k - 1) + 1, 4 ** k + 1)) for k in range(1, 12)]
say("surface to surface by 4, the me-parities of a span: %s, every span more than all the spans before it together, from 16 on" % four,
    all(four[k] > sum(four[:k]) for k in range(2, len(four))))
print("All is." if all(results) else "A line is-not.")
