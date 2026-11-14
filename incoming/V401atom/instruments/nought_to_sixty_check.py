"""Nought to sixty, by the living files' own sentences and by Exhibit ONE's seventeen names. All or none.

Reads Exhibit THREE Natural Numbers, Exhibit FIFTEEN Natural Emanating and Exhibit ONE's table, and changes none.
Run: python3 incoming/V401atom/instruments/nought_to_sixty_check.py Exhibit_THREE_Natural_Numbers_v401mgr.md Exhibit_FIFTEEN_Natural_Emanating_v391.md Exhibit_ONE_Natural_Resolver_v401mgr.md
"""
import re, sys
from fractions import Fraction
three, fifteen, one = (open(p, encoding="utf-8").read() for p in sys.argv[1:4])
primes = [n for n in range(2, 61) if all(n % d for d in range(2, n))]
names = [int(n) for n in re.findall(r"^\| (\d+) \| \*\*\d+-", one, re.M)]
print("1 the primes of nought to sixty:", len(primes), "·", " ".join(str(p) for p in primes))
print("  the betweens of them, a prime and its next:", len(primes) - 1)
print("  Exhibit ONE's names:", len(names), "· its steps, a name to its next:", len(names) - 1,
      "· a prime by each name and a between by each step:", len(primes) == len(names) == 17)
print("  the seventeenth prime is 59, the last before sixty:", primes[16] == 59 and primes[-1] == 59)
print("  Exhibit THREE has it, its own sentence:", "A going from nought to sixty has seventeen primes and sixteen betweens, one and then the other" in three.replace("*", ""))
print("  the primes by the names 1 to 9 are 100 together, 64 and 36:", sum(primes[:9]) == 100)
# two directions of one length: what the two have the same, by the angle of the two; sixty by its exact half
half = Fraction(1, 2)
print("2 two directions of one length, by Exhibit FIFTEEN's three lines:")
for l in re.findall(r"^(?:a = b|θ = 60°|orthogonal)\s+.*$", fifteen, re.M):
    print("    " + re.sub(r"\s{2,}", " · ", l.strip()))
print("  at nought the two are one line, equal, and nothing opens; at sixty the two have one half the same:", half == Fraction(1, 2) and "sharing 0.500" in fifteen)
print("  a cone of thirty around its centre line: its two directions most apart are thirty and thirty, sixty:", 30 + 30 == 60)
print("  six directions around, each sixty from its next, are full around:", 6 * 60 == 360)
