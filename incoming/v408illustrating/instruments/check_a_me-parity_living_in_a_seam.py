"""v408illustrating · the check of the 52nd drawing: a me-parity living in a seam, even, odd, even; v408primes' sentences 172 to 187, executed apart.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_a_me-parity_living_in_a_seam.py .

v408primes laid, on 25 November, a me-parity's three parts and a me-parity living in a seam, and said them to this session
at the exchange for drawing. They are executed here apart, by this check's own lines, to 4,000,000, that session's own span.
v408primes' word of a prime is a me-parity; a seam of n is a number n crosses; a me again is a number by itself; a
me-parity's aim is its even that is a seam of 4. What is with all numbers is said apart from what is stepped.
Its is and its is-not are both executed. Whole numbers alone. It writes none.
"""
import sys
from math import gcd, isqrt

N = 4_000_000
def stepped():
    sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
    for n in range(2, isqrt(N) + 1):
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, N + 1, n)))
    two = bytearray(N + 1)                                           # a number that is two me agains added, both past 0
    for a in range(1, isqrt(N) + 1):
        aa = a * a
        for b in range(a, isqrt(N - aa) + 1): two[aa + b * b] = 1
    return sieve, two
def parts(n):
    """A number's parts, its primes multiplied, the least ahead."""
    out, d = [], 2
    while d * d <= n:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out + ([n] if n > 1 else [])
def a_seam_of_all_primes_to(r, sieve):
    seam = 1
    for p in range(2, r + 1):
        if sieve[p]: seam *= p
    return seam
def the_numbers():
    sieve, two = stepped()
    mes = [p for p in range(3, N + 1) if sieve[p]]                   # the me-parities past 2
    prior = [p for p in mes if (p - 1) % 4 == 0]; nxt = [p for p in mes if (p + 1) % 4 == 0]
    past3 = [p for p in mes if p > 3]
    seam = {p: (p - 1 if (p - 1) % 6 == 0 else p + 1) for p in past3}
    twins = [p for p in mes if p + 2 <= N and sieve[p + 2]]          # a twin's lower me-parity
    sides = {0: [], 1: [], 2: []}                                     # a seam of 6, with a me-parity at none of its sides, at one, at both
    for s in range(6, N, 6): sides[sieve[s - 1] + sieve[s + 1]].append(s)
    one = [p for p in past3 if seam[p] % 4 == 0]                     # its aim and its seam are one even, a seam of 12
    return dict(sieve=sieve, two=two, mes=mes, prior=prior, nxt=nxt, past3=past3, seam=seam, twins=twins, sides=sides, one=one)

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    d = the_numbers(); sieve, two, mes, seam = d["sieve"], d["two"], d["mes"], d["seam"]
    line("three parts, even, odd, even: all 283,145 me-parities past 2 to 4,000,000 are odd, with their prior even and their next even, v408primes' 172 executed apart; it is with all odd numbers",
         len(mes) == 283145 and all(p % 2 == 1 and (p - 1) % 2 == 0 and (p + 1) % 2 == 0 for p in mes))
    line("is-not, explored: 2 is odd, even, odd, 1, 2 and 3, the one me-parity with odd at both its sides, v408primes' 173", sieve[2] and [n % 2 for n in (1, 2, 3)] == [1, 0, 1] and not any(sieve[e] for e in range(4, N + 1, 2)))
    line("a me-parity's two evens, by 2, are a +1 apart, one odd and one even, v408primes' 174; one alone of its two evens is a seam of 4, its aim, v408primes' 175: all 283,145",
         all((p + 1) // 2 - (p - 1) // 2 == 1 and ((p - 1) % 4 == 0) != ((p + 1) % 4 == 0) for p in mes))
    line("aiming prior, 141,502 me-parities, all two me agains added; aiming next, 141,643, two me agains added at none, v408primes' 176 and 177 executed apart; stepped to 4,000,000",
         len(d["prior"]) == 141502 and len(d["nxt"]) == 141643 and all(two[p] for p in d["prior"]) and not any(two[p] for p in d["nxt"]) and two[5] and two[13] and 5 == 1 + 4 and 13 == 4 + 9)
    line("past 3, a me-parity lives in a seam of 6, its prior or its next: all 283,144, v408primes' 178; with all numbers, of the six mes of a path of 6 closing, the me one on and the me one back alone are uncrossed by 2 and by 3",
         len(d["past3"]) == 283144 and all(seam[p] % 6 == 0 and abs(p - seam[p]) == 1 for p in d["past3"]) and [a for a in range(6) if a % 2 and a % 3] == [1, 5])
    line("a seam and its me-parity: no prime crosses both, v408primes' 180; round the seam its me-parity is at one step, and round the me-parity the seam is at one step the other way, v408primes' 181: all 283,144",
         all(gcd(p, seam[p]) == 1 and p % seam[p] == (p - seam[p]) % seam[p] and seam[p] % p == (seam[p] - p) % p for p in d["past3"]))
    seams = [(r, a_seam_of_all_primes_to(r, sieve)) for r in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)]
    line("a seam of all primes to r, r of 2 to 31, is crossed by them all, and its -1 and its +1 by none: their parts are past r, v408primes' 183; 29 and 31, 30,029, and 30,031, 59 by 509, v408primes' 184; 209 is 11 by 19",
         all(all(s % p == 0 for p in range(2, r + 1) if sieve[p]) and all(q > r for side in (s - 1, s + 1) for q in parts(side)) for r, s in seams)
         and dict(seams)[13] == 30030 and parts(29) == [29] and parts(31) == [31] and parts(30029) == [30029] and parts(30031) == [59, 509] and parts(209) == [11, 19])
    past = [p for p in d["twins"] if p > 3]
    line("twins past 3 are two me-parities living in one seam of 6, at both its sides, all 26,859, v408primes' 185; they aim together at a middle that is a seam of 12 at 13,468, and apart at 13,391, v408primes' 186 and 187",
         len(past) == 26859 == len(d["sides"][2]) and all((p + 1) % 6 == 0 for p in past) and sum((p + 1) % 12 == 0 for p in past) == 13468 and sum((p + 1) % 12 == 6 for p in past) == 13391)
    one = set(d["one"])
    line("found by drawing it: a me-parity's aim and its seam are one even, a seam of 12, at 141,460 me-parities past 3, and its two evens at 141,684; twins aim together at the seams where both twins' aim and seam are one even, and at no other",
         len(one) == 141460 and len(d["past3"]) - len(one) == 141684 and all(((p + 1) % 12 == 0) == (p in one and p + 2 in one) for p in past))
    line("is-not, explored: a seam of 6 is with a me-parity at both its sides at 26,859 seams, at one side alone at 229,426, the least 24, 25 being 5 by 5, and at none at 410,381, the least 120, 7 by 17 and 11 by 11",
         [len(d["sides"][k]) for k in (2, 1, 0)] == [26859, 229426, 410381] and d["sides"][1][0] == 24 and parts(25) == [5, 5] and d["sides"][0][0] == 120 and parts(119) == [7, 17] and parts(121) == [11, 11])
    print("said apart: v408primes' pages are not in the set at this main; its sentences 172 to 187 are opened from its branch at 598b836\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
