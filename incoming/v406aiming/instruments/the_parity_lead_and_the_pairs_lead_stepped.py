"""The draft's parity lead and the pair's lead, stepped with whole numbers alone.

A number's + or -: + with an even number of primes multiplied, - with an odd one, 1 a +.
The parity lead: the + and - of 1 up to a number, added (Exhibit THIRTY-TWO's draft, 2.2).
The pair's lead: the + or - of n by that of n + 2, multiplied, added: the + or - of the
pair's product, n by n + 2, the parity Exhibit TWENTY-TWO's wall is of with twin primes.
It writes nothing and reaches no network.

Usage: python3 -I the_parity_lead_and_the_pairs_lead_stepped.py [TO, 1,000,000 unsaid]
"""
import sys
from math import isqrt
TO = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
N = TO + 2
spf = list(range(N + 1))
for i in range(2, isqrt(N) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j: spf[j] = i
sign = [1] * (N + 1)
for n in range(2, N + 1): sign[n] = -sign[n // spf[n]]
lead = pair = most_lead = most_pair = 0
for n in range(1, TO + 1):
    lead += sign[n]; pair += sign[n] * sign[n + 2]
    most_lead = max(most_lead, abs(lead)); most_pair = max(most_pair, abs(pair))
side = isqrt(TO)
print(f'to {TO:,}: the parity lead ends at {lead}, its most {most_lead}; the pair\'s lead ends at {pair}, its most {most_pair}; the side {side:,}')
print('the pair\'s lead within the side:', most_pair <= side, '| the parity lead within the side:', most_lead <= side)
