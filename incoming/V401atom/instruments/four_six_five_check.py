"""Four-cycling and six-cycling about five, by natural numbers, primes, their gaps and podaling. Each an identity, all or none.

No measuring and no number of trials: each line is one identity of whole numbers. Reads Exhibit THREE for its own sentences.
Run: python3 incoming/V401atom/instruments/four_six_five_check.py Exhibit_THREE_Natural_Numbers_v401mgr.md
"""
import sys
three = open(sys.argv[1], encoding="utf-8").read().replace("*", "")
P = [n for n in range(2, 60) if all(n % d for d in range(2, n))]          # seventeen primes, a prime by each name
g = {k: P[k] - P[k - 1] for k in range(1, 17)}                             # the gap of the step from name k to name k + 1
print("1 four and six are either side of five: 4 x 6 = 5 x 5 - 1:", 4 * 6 == 5 * 5 - 1, "· 4 + 6 = 10 = 2 x 5 = the couplings among five:", 4 + 6 == 10 == 2 * 5 == 5 * 4 // 2)
print("  Exhibit THREE's own: an adding closes after one, two, three, four and six, and none closes after five:", "no adding closes after five" in three)
print("2 a right spiral step: four steps, as it was, same-as; six steps, both its parities their other, other-than; ten steps, other-than; twelve, same-as:",
      (1j ** 4, 1j ** 6, 1j ** 10, 1j ** 12) == (1, -1, -1, 1))
print("3 a four-cycling's fourths, 4, 8, 12 and 16, and a six-cycling's sixths, 6 and 12: the two are one name at 12, and next at 24, 36, 48 and 60:",
      sorted(set(range(4, 61, 4)) & set(range(6, 61, 6))) == [12, 24, 36, 48, 60])
print("4 the prime gaps by the steps of the names, 1 to 2 and on:", " ".join(str(g[k]) for k in range(1, 17)))
print("  by the eight now names, steps 1 to 8: one, and twos and fours in turn, and no six:", [g[k] for k in range(1, 9)] == [1, 2, 2, 4, 2, 4, 2, 4])
print("  each gap of six is by the next names, the first by the step from 9 to 10:", [k for k in g if g[k] == 6] == [9, 11, 15, 16])
print("  the names having a gap of four at its one side and a gap of six at its other:", [n for n in range(2, 17) if {g[n - 1], g[n]} == {4, 6}])
print("  primes 2 to 23, by the now names, are 21 apart; primes 23 to 59, by the next names, 36, six sixes:", P[8] - P[0] == 21 and P[16] - P[8] == 36)
pairs = [(p, 60 - p) for p in P if p < 30 and (60 - p) in P and p > 5]
print("5 podaling about thirty: six prime pairs, each two sixty together:", pairs, len(pairs) == 6)
print("  three names to an other, 6, 9 and 10, and three from an other, 2, 14 and 17: their primes", [P[n - 1] for n in (6, 9, 10)], "and", [P[n - 1] for n in (2, 14, 17)],
      "·", sum(P[n - 1] for n in (6, 9, 10)), "and", sum(P[n - 1] for n in (2, 14, 17)))
