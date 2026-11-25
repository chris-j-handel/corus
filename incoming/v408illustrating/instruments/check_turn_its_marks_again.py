"""v408illustrating · the check of the 49th drawing: Turn's marks again, by v408primes' lines of twins, of a next no more than 246 apart, of a seam's numbers by its places, and of odd and even across.

Usage, from the repository's root (about a minute):
  python3 -I incoming/v408illustrating/instruments/check_turn_its_marks_again.py .

The 46th drawing marked the form's page: bounded gaps and Brun not yet resolving, the parity wall a naming. v408primes
laid lines of all three on 25 November, its sentences 132, 153, 156, 162, 163 and 166, said to this session at the
exchange. They are executed here apart, by this check's own lines, to 4,194,304, a span by 4 whole.
v408primes' word of a prime is a me-parity. Its is and its is-not are both executed. Whole numbers alone. It writes none.
"""
import bisect, sys
from array import array

N = 4 ** 11
def stepped():
    sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0; least = array("l", [0]) * (N + 1); n = 2
    while n <= N:
        if sieve[n]:
            least[n] = n
            if n * n <= N:
                for k in range(n * n, N + 1, n):
                    if not least[k]: least[k] = n
                sieve[n * n::n] = bytearray(len(range(n * n, N + 1, n)))
        n += 1
    primes = [n for n in range(N + 1) if sieve[n]]
    across = array("b", [0]) * (N + 1); across[1] = 1                 # a number's parity across: +1 with an even number of primes multiplied in it, -1 with an odd
    for n in range(2, N + 1): across[n] = -across[n // least[n]]
    return sieve, primes, across
SPANS = [(4 ** k, 4 ** (k + 1)) for k in range(2, 11)]

def the_numbers():
    sieve, primes, across = stepped()
    twins = [sum(1 for p in primes[bisect.bisect_left(primes, a):bisect.bisect_left(primes, b)] if p + 2 < b and sieve[p + 2]) for a, b in SPANS]
    near = [sum(1 for k in range(bisect.bisect_left(primes, a), bisect.bisect_left(primes, b) - 1) if primes[k + 1] - primes[k] <= 246) for a, b in SPANS]
    widest = max((primes[k + 1] - primes[k], primes[k]) for k in range(bisect.bisect_left(primes, 4_000_000) - 1))
    num, den, past = 1, 1, {}
    for p in primes:
        num *= p; den *= p - 1
        for m in (2, 10, 20):
            if m not in past and num > m * den: past[m] = p
        if len(past) == 3: break
    apart = max((abs(sum(across[a if a else m::m])) * 100 * m / N, m, a) for m in range(3, 31) for a in range(m))   # the more of odd or even, in a hundred of a loop's numbers
    return twins, near, widest, past, apart

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    twins, near, widest, past, apart = the_numbers()
    line("a last, twins: a span by 4, 16 to 64 and on to 4,194,304, is with 4, 10, 19, 71, 183, 570, 1,819, 5,856 and 19,460 twins: at no span fewer than the span before, v408primes' 163 executed apart",
         twins == [4, 10, 19, 71, 183, 570, 1819, 5856, 19460] and all(a < b for a, b in zip(twins, twins[1:])))
    line("a beat, a next no more than 246 apart: a prime with its next no more than 246 apart, a span by 4: 11, 35, 117, 391, 1,335, 4,641, 16,457, 59,024 and 213,921, at no span fewer, v408primes' 156 executed apart",
         near == [11, 35, 117, 391, 1335, 4641, 16457, 59024, 213921] and all(a < b for a, b in zip(near, near[1:])))
    line("is-not, of one beat: the widest from a prime to its next below 4,000,000 is 148, after 2,010,733, v408primes' 153; a widest goes on with the spans", widest == (148, 2010733))
    line("a value, a seam's numbers by its places: past 2 at 3, past 10 at 257 and past 20 at 75,037, at no seam settled, v408primes' 162 executed apart", past == {2: 3, 10: 257, 20: 75037})
    line("odd and even across, v408primes' 166 executed apart: round all loops of 3 to 30, with all their numbers to 4,194,304, the odd and the even across are apart by short of 1 in 100 of a loop's numbers",
         apart[0] < 1)
    print(f"said apart: the most apart is {apart[0]:.3f} in 100, round the loop of {apart[1]} at {apart[2]} · v408primes' pages are not in the set at this main; its sentences are opened from its branch at 89c3839\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
