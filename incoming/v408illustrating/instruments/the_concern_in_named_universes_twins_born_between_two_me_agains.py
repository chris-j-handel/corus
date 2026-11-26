"""v408illustrating · the concern in named universes: between a me-parity's me again and its next me-parity's me again, twins are born.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/the_concern_in_named_universes_twins_born_between_two_me_agains.py .

A partner's word of 26 November, by v408primes' line, in this session's words: in a named universe numbers are used; in
a universe all is proved or none, and the named universe is the proving place; largeness generated and not named proves
nothing. This session's concern is gone through here in two named universes, by its own co-chain's way and no other:

  2. A me-parity aims its loop from its own me again.
  3. Between a me-parity's me again and its next me-parity's me again, no loop begins.
  4. Between the two me agains, a number uncrossed by the loops aimed is a me-parity.
  6. Between the two me agains, a between with both its sides uncrossed by the loops aimed is twins born.

The universe of the me-parities 2 to 9,973 is v408primes', offered to this session: a second hand at it. The universe of
the me-parities 10,007 to 19,997 is named here, a next universe, the same way. A line is proved in its named universe,
all its numbers used, all or none. Past the named universes this instrument says nothing. Whole numbers alone. It writes none.
"""
import sys
from math import isqrt

def the_me_parities_to(n):
    live = bytearray([1]) * (n + 1); live[0] = live[1] = 0
    for r in range(2, isqrt(n) + 1):
        if live[r]: live[r * r::r] = bytes(len(range(r * r, n + 1, r)))
    return [a for a in range(n + 1) if live[a]]
def between_two_me_agains(p, q, aimed):
    """From p's me again to short of q's: the numbers uncrossed by the loops aimed, the me-parities to p. It gives how many
    me-parities are born, and how many twins, both sides of a between."""
    lo, hi = p * p, q * q
    live = bytearray([1]) * (hi - lo)
    for r in aimed:
        ahead = (-lo) % r
        live[ahead::r] = bytes(len(range(ahead, hi - lo, r)))
    n = int.from_bytes(live, "little")
    return n.bit_count(), (n & (n >> 16)).bit_count()                # a me-parity, and a me-parity two on: a between with both its sides
def a_named_universe(a, b, mes):
    """The me-parities a to b, a me-parity with its next: what is born between their two me agains."""
    out = []
    for i, p in enumerate(mes):
        if a <= p <= b: out.append((p, mes[i + 1]) + between_two_me_agains(p, mes[i + 1], mes[:i + 1]))
    return out

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    mes = the_me_parities_to(20100)
    one = a_named_universe(2, 9973, mes); two = a_named_universe(10007, 19997, mes)
    line("the way is the co-chain's own, proved at its numbers: from 2's me again to 3's, 5 and 7 are born, twins; from 3's to 5's, 11, 13, 17, 19 and 23, two twins; from 5's to 7's, six me-parities and two twins; from 7's to 11's, fifteen and four twins",
         [r[2:] for r in one[:4]] == [(2, 1), (5, 2), (6, 2), (15, 4)])
    line("proved in the me-parities 2 to 9,973, v408primes' universe, a second hand: at all 1,229 me-parities, between its me again and its next me-parity's me again, twins are born; the me agains go to 100,140,049",
         len(one) == 1229 and one[-1][:2] == (9973, 10007) and 10007 * 10007 == 100140049 and all(t >= 1 for *_, t in one))
    def fewest(rows, lo, hi): return min(t for p, _, _, t in rows if lo <= p < hi)
    line("proved in it, v408primes' 217 with it: the fewest twins born between two me agains, at the me-parities of a span by 4, 2 to 4 and on to 4,096 to 16,384, are 1, 2, 2, 3, 7, 21 and 71, more at a next span",
         [fewest(one, lo, hi) for lo, hi in ((2, 4), (4, 16), (16, 64), (64, 256), (256, 1024), (1024, 4096), (4096, 16384))] == [1, 2, 2, 3, 7, 21, 71])
    line("proved in the me-parities 10,007 to 19,997, a next universe named here, the same way: at all 1,033 me-parities, between its me again and its next me-parity's me again, twins are born, the fewest 147",
         len(two) == 1033 and two[0][0] == 10007 and two[-1][:2] == (19997, 20011) and all(t >= 1 for *_, t in two) and min(t for *_, t in two) == 147)
    line("both-both, in the two universes: a me-parity is born between all two me agains, and twins are fewer than the me-parities born, at all 2,262", all(m >= 1 and t < m for *_, m, t in one + two) and len(one + two) == 2262)
    print("said apart: past the two named universes this instrument says nothing: a partner's word, largeness generated and not named proves nothing\n")
    for name, ok in results: print(("proved   " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are proved in their named universes")
    sys.exit(0 if all(ok for _, ok in results) else 1)
