"""v408illustrating · a partner's saying gone into: a gap followed along the path to its own place, beside the universe now at that place.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/a_gap_followed_to_its_own_place.py .

With the me-parities to B as priors, a between is uncrossed with the number before it and the number after it both made by
no multiplying of a prior. The longest gap is the most +1s from an uncrossed between to its next. Here it is followed to
its place nearest the origin, and the universe now at that place is the me again to the me again about it.
  is       a sentence gone through whole at the numbers named.
Whole numbers alone. It writes none.
"""
import sys
from math import prod, isqrt

def a_me_parity(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
ME = [p for p in range(2, 1000) if a_me_parity(p)]
def a_gap_of_2(n): return a_me_parity(n - 1) and a_me_parity(n + 1)
def the_longest_gap(B):
    """With priors to B: the most +1s from an uncrossed between to its next, and its place nearest the origin."""
    pri = [p for p in ME if p <= B]; S = prod(pri); K = S // 6
    live = bytearray([1]) * (K + 1)                       # index k is the between 6 by k
    for r in pri[2:]:
        inv = pow(6, -1, r)
        for a in (inv % r, (-inv) % r): live[a::r] = bytes(len(range(a, K + 1, r)))
    live[0] = 0
    best, place, pos = 0, None, live.find(1)
    while True:
        nxt = live.find(1, pos + 1)
        if nxt < 0: return 6 * best, place
        if nxt - pos > best: best, place = nxt - pos, (6 * pos, 6 * nxt)
        pos = nxt
def the_universe_now(a, b):
    """The me again to the me again about the numbers a to b."""
    p = max(x for x in ME if x * x <= a); q = min(x for x in ME if x * x >= b)
    return p, q

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    said = {5: (12, (18, 30), (3, 7)), 7: (30, (72, 102), (7, 11)), 11: (42, (900, 942), (29, 31)),
            13: (66, (732, 798), (23, 29)), 17: (108, (702, 810), (23, 29)), 19: (150, (660, 810), (23, 29))}
    for B, (gap, place, now) in said.items():
        g, pl = the_longest_gap(B); p, q = the_universe_now(*pl)
        in_it = [n for n in range(p * p + 2, q * q - 1) if a_gap_of_2(n)]
        line(f"priors to {B}: the longest gap is {gap}, nearest the origin from {place[0]} to {place[1]}; the universe now at its place is {p} by {p} to {q} by {q}, {q*q - p*p} numbers, more than the gap; gaps of 2 in it: {len(in_it)}",
             (g, pl, (p, q)) == (gap, place, now) and q * q - p * p > g and in_it)
    line("B's own universe beside it: with priors to 17 the gap of 108 is from 702 to 810, and 17 by 17 to 19 by 19 is 289 to 361; the gap is no number of it",
         the_longest_gap(17)[1][0] > 19 * 19)
    line("the place about 735, 3 by 5 by 7 by 7: the gap is 66 with priors to 13; 731 is 17 by 43 and 799 is 17 by 47, and it is 108 with 17; 703 is 19 by 37, and it is 150 with 19; 659 with 661 and 809 with 811 are me-parities, and it is 150 with 23 and with all priors after",
         735 == 3 * 5 * 7 * 7 and 731 == 17 * 43 and 799 == 17 * 47 and 703 == 19 * 37 and a_gap_of_2(660) and a_gap_of_2(810)
         and not any(a_gap_of_2(n) for n in range(662, 809)))
    born = [n for n in range(661, 810) if a_me_parity(n)]
    line(f"a gap of gaps: from 661 to 809 are {len(born)} me-parities, their gaps {', '.join(str(b - a) for a, b in zip(born, born[1:]))}: no one of them 2",
         len(born) == 20 and 2 not in [b - a for a, b in zip(born, born[1:])])
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
