"""v408illustrating · the fractal followed along the path: a gap of 2 at a prior's birth, going on or ended, and made by no birth.

Usage, from the repository's root (a moment):
  python3 -I incoming/v408illustrating/instruments/a_gap_of_2_at_a_prior_s_birth.py .

A prior's birth crosses the numbers it multiplies. An uncrossed number is made by no multiplying of a prior. A gap is the
+1s from an uncrossed number to its next. The page beside this instrument lays the co-chain, of no number; here its
sentences are gone through at small numbers.
  is       a sentence gone through whole at the numbers named.
Whole numbers alone. It writes none.
"""
import sys
from math import gcd, prod, isqrt

def a_me_parity(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
ME = [p for p in range(2, 400) if a_me_parity(p)]
def uncrossed(S, to): return [n for n in range(1, to + 2) if gcd(n, S) == 1]
def ends(q, n): return n % q in (1, q - 1)                 # the between n is a +1 after or before a number q multiplies
def most_ended(q, L): return 2 * -(-L // q)                # of L multiples of 6 one after the other, q ends 2 of q, and no more than this
def the_universe(r):
    """r by r to the next me-parity's me again: its multiples of 6 with the numbers before and after both in it."""
    nxt = ME[ME.index(r) + 1]
    return [n for n in range(r * r + 2, nxt * nxt - 1) if n % 6 == 0], nxt

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    ok_made, ok_same, numbers = True, True, []
    for i in range(2, 6):                                  # the births of 5, 7, 11 and 13
        S, r = prod(ME[:i]), ME[i]
        old, new = uncrossed(S, S * r), uncrossed(S * r, S * r)
        old_set = set(old)
        old_2 = sum(b - a == 2 for a, b in zip(uncrossed(S, S), uncrossed(S, S)[1:]))
        new_2 = [(a, b) for a, b in zip(new, new[1:]) if b - a == 2]
        joined = [(a, b) for a, b in zip(new, new[1:]) if any(m in old_set for m in range(a + 1, b))]
        ok_made &= all(b - a >= 6 for a, b in joined)
        ok_same &= len(new_2) == old_2 * (r - 2) and all(a in old_set and b in old_set for a, b in new_2)
        numbers.append(f"{old_2} by {r - 2} are {len(new_2)}")
    line("a birth makes no gap of 2: at the births of 5, 7, 11 and 13, a gap joined of two is 6 or more, at all joinings of a whole seam", ok_made)
    line(f"a gap of 2 after a birth is a gap of 2 before it, laid again and going on, r less 2 of r: {'; '.join(numbers)}", ok_same)
    line("all gaps of 2 of me-parities past 3 and 5, to 2,000, are about a multiple of 6: the gap of 2 about 6 laid again",
         all(n % 6 == 0 for n in range(6, 2000) if a_me_parity(n - 1) and a_me_parity(n + 1)))
    line("at a birth, of r multiples of 6 one after the other, 2 are ended, at all r of 5 to 31 and all rows of a seam of r",
         all(sum(ends(r, 6 * (k + j)) for j in range(r)) == 2 for r in ME[2:11] for k in range(r)))
    def newly(r):
        row, nxt = the_universe(r)
        return [n for n in row if ends(r, n) and not any(ends(q, n) for q in ME[2:ME.index(r)])], nxt
    line("in its own universe, a between ended by r and by no prior before r is beside r by a me-parity from r on: at all r of 5 to 97",
         all(any(a_me_parity(m // r) and m // r >= r for m in (n - 1, n + 1) if m % r == 0) for r in ME[2:25] for n in newly(r)[0]))
    def the_adding(r):
        row, _ = the_universe(r); pri = ME[2:ME.index(r) + 1]
        going = [n for n in row if not any(ends(q, n) for q in pri)]
        return len(row), [most_ended(q, len(row)) for q in pri], going
    L5, m5, k5 = the_adding(5); L7, m7, k7 = the_adding(7); L11, m11, k11 = the_adding(11)
    line(f"no between looked at, 25 to 49: {L5} multiples of 6, 5 ends {m5[0]} at most, fewer; a gap of 2 goes on. Looked at after: {k5}",
         (L5, m5) == (3, [2]) and sum(m5) < L5 and k5 == [30, 42])
    line(f"no between looked at, 49 to 121: {L7} multiples of 6, 5 ends {m7[0]} at most and 7 ends {m7[1]}, {sum(m7)} together, fewer; a gap of 2 goes on. Looked at after: {k7}",
         (L7, m7) == (11, [6, 4]) and sum(m7) < L7 and k7 == [60, 72, 102, 108])
    line(f"121 to 169: {L11} multiples of 6, and 5, 7 and 11 end {m11[0]}, {m11[1]} and {m11[2]} at most, {sum(m11)} together, not fewer: the adding says no gap of 2 and no none. Looked at: {k11} go on; 144 is ended by 5 and by 11, two endings at one between",
         (L11, m11) == (7, [4, 2, 2]) and sum(m11) >= L11 and k11 == [138, 150] and ends(5, 144) and ends(11, 144))
    line("the most a prior ends is said from the row alone: of L multiples of 6 one after the other, q ends no more than 2 by L over q, the next whole number: at q of 5 to 31, L of 1 to 60, all rows",
         all(sum(ends(q, 6 * (k + j)) for j in range(L)) <= most_ended(q, L) for q in ME[2:11] for L in range(1, 61) for k in range(q)))
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
