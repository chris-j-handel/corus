"""v408illustrating · a partner's saying gone into: a me-parity is never the same, new and unique, and from its own priors.

Usage, from the repository's root (a moment):
  python3 -I incoming/v408illustrating/instruments/a_me-parity_from_its_own_priors.py .

A number's own priors are the me-parities whose me again is not past it. The page beside this instrument lays the co-chain,
of no number. Here its sentences are gone through whole at the numbers 2 to 400: a going through of the sentences' own
saying at those numbers, and the reason at all numbers is the co-chain's.
  is       a sentence gone through whole at the numbers named.
Whole numbers alone. It writes none.
"""
import sys

TO = 400
def crossed_by(q, n): return n % q == 0 and n != q                    # q's loop crosses n: n is on it, past q itself
def a_me_parity(n): return n > 1 and all(n % d for d in range(2, n))   # by all the numbers short of it, the long saying
ME_PARITIES = [n for n in range(2, TO + 2) if a_me_parity(n)]
def own_priors(n): return [q for q in ME_PARITIES if q * q <= n]
def twins(n): return a_me_parity(n - 1) and a_me_parity(n + 1)
def uncrossed_by_its_own_priors(n): return all(n % q for q in own_priors(n))
def a_between_by_its_own_priors(n):
    """Round all the own priors of the upper side, the between is not a +1 after a crossing and not a +1 before one."""
    return all(n % q not in (1, q - 1) for q in own_priors(n + 1))

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    line("a crossed number is a by b, a not past b, and a by a is not past the number: at all crossed numbers of 4 to 400",
         all(any(n % a == 0 and a * a <= n for a in range(2, n)) for n in range(4, TO + 1) if not a_me_parity(n)))
    line("the least part past 1 of a crossed number is a me-parity, and a prior of the number's own: at all crossed numbers of 4 to 400",
         all(next(a for a in range(2, n) if n % a == 0) in own_priors(n) for n in range(4, TO + 1) if not a_me_parity(n)))
    line("from its own priors: a number is a me-parity with all its own priors' loops leaving it uncrossed, and with that alone, at all numbers of 2 to 400",
         all(a_me_parity(n) == uncrossed_by_its_own_priors(n) for n in range(2, TO + 1)))
    line("new: a me-parity is on no prior me-parity's loop, at all me-parities to 400; unique: its own loop begins at it, and no two me-parities are with one loop",
         all(not crossed_by(q, p) for p in ME_PARITIES for q in ME_PARITIES if q < p) and len(set(ME_PARITIES)) == len(ME_PARITIES))
    line("twins from the between's own priors: a between is twins with, round all its own priors, the between not a +1 after a crossing and not a +1 before one, and with that alone, at all betweens of 4 to 400",
         all(twins(n) == a_between_by_its_own_priors(n) for n in range(4, TO + 1)))
    line("12's own priors are 2 and 3, 5 by 5 past 13, and 11 and 13 are twins; 24's are 2, 3 and 5, and 24 is a +1 before 5's crossing at 25; 222's are 2, 3, 5, 7, 11 and 13, and 222 is a +1 after 13's crossing at 221, 13 by 17",
         own_priors(13) == [2, 3] and twins(12) and own_priors(25) == [2, 3, 5] and 25 == 5 * 5 and not twins(24)
         and own_priors(223) == [2, 3, 5, 7, 11, 13] and 221 == 13 * 17 and not twins(222))
    line("a between further on is with all a nearer between's own priors, and with more or as many: at all two betweens of 4 to 400",
         all(own_priors(n + 1) == own_priors(m + 1)[:len(own_priors(n + 1))] for n in range(4, TO + 1) for m in (n + 6, 2 * n, TO)))
    print("said apart: a sentence gone through at the numbers 2 to 400 is gone through at them; its reason at all numbers is the co-chain in the page beside this instrument\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
