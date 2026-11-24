#!/usr/bin/env python3
"""The spirals lining up at a turn, and one past a turn none of them: stepped with the resolver's own code.

Usage:  python3 -I incoming/v406other2/instruments/the_spirals_lining_up_at_a_turn_by_the_resolver_executed.py [ROOT]

It reads Exhibit ONE's code by incoming/v406Reiman/instruments/resolver_as_it_is.py and steps spirals of
selves a moment after a moment. A spiral is again at a moment with all its selves as at the moment it is stepped from.
A line is a saying, ending is or is-not. Nothing is decided: a line says is of what it stepped. It writes
no file.
"""
import sys
from itertools import product
from math import lcm
from pathlib import Path

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[3]
sys.path.insert(0, str(root / "incoming" / "v406Reiman" / "instruments"))
from resolver_as_it_is import frozen, moments_again, opening, resolver, spiral_couplings  # noqa: E402

names, _ = resolver(str(root))
step = names["_17_next_existing"]
out = []


def say(text, ok):
    out.append(("is" if ok else "is-not", text))


def a_spiral(n):
    """a spiral of n selves at a moment it comes again to, from its opening of the most moments to again"""
    best = None
    for pri in product((1, -1), repeat=n):
        society = opening(range(n), dict(enumerate(pri)))
        begun, span = moments_again(step, society, spiral_couplings(n))
        if best is None or span > best[1]:
            best = (begun, span, society)
    begun, span, society = best
    for _ in range(begun):
        society = step(society, spiral_couplings(n))
    return society


def again_moments(n, moments):
    """the moments, 1 to moments, at which a spiral of n selves is again as at the moment it is stepped from"""
    society = a_spiral(n)
    first = frozen(society)
    at = set()
    for t in range(1, moments + 1):
        society = step(society, spiral_couplings(n))
        if frozen(society) == first:
            at.add(t)
    return at


SPAN = 1700
at = {n: again_moments(n, SPAN) for n in (2, 3, 5, 7)}
say("spirals of 2, 3, 5 and 7 selves are again with all 4, 12, 20 and 28 moments, and at no moment between",
    all(at[n] == set(range(span, SPAN + 1, span)) for n, span in ((2, 4), (3, 12), (5, 20), (7, 28))))
together = sorted(at[2] & at[3] & at[5])
say("spirals of 2, 3 and 5 selves, side by side, are again together with all 60 moments, and at no moment between: "
    "with a number two moments, all 30 numbers, their turn", together == list(range(60, SPAN + 1, 60)))
together7 = sorted(at[2] & at[3] & at[5] & at[7])
say("with a spiral of 7 selves they are again together with all 420 moments, and at no moment between: "
    "all 210 numbers, their turn", together7 == [420, 840, 1260, 1680])
say("a number past their together, two moments, none of them is again: at 62 and 122 moments with 2, 3 and 5, "
    "and at 422 and 842 with 7 more", all(t not in at[n] for t in (62, 122) for n in (2, 3, 5))
    and all(t not in at[n] for t in (422, 842) for n in (2, 3, 5, 7)))


def lowest_part(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n


ok = True
turn = 1
for m in range(2, 24):
    turn = lcm(turn, m)
    ok = ok and all(turn % k == 0 for k in range(2, m + 1))
    ok = ok and all((turn + 1) % k == 1 for k in range(2, m + 1)) and lowest_part(turn + 1) > m
say("with whole numbers: all spirals of 2 to m are at their seam at their turn, and one past their turn none of them "
    "is, its lowest part past m, a prime born: m of 2 to 23", ok)
say("one past the turns of 2, 3, 5 and of 2, 3, 5, 7 are 31 and 211, both primes",
    lowest_part(31) == 31 and lowest_part(211) == 211)

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not.")
