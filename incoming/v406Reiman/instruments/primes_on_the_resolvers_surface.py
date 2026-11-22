"""Primes on the resolver's surface: what Exhibit ONE's code executes of them.

Three executings, each with the resolver as it is in its living file:

  1. A spiral of 2 to 13 selves, with all its openings of + and − priors:
     the moments to its parities again.
  2. A spiral of selves opened with a smaller spiral's pattern laid along it.
  3. Spirals of 2 to 61 selves, a spiral tested against the smaller spirals
     that no smaller spiral crossed.

And one page of arithmetic with no resolver in it, said as such: the same test
by division, from a span to its square.

    python3 -I incoming/v406Reiman/instruments/primes_on_the_resolvers_surface.py . [--to 61]
"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, moments_again, opening, resolver, spiral_couplings


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def every_opening(step, n):
    found = set()
    for pattern in itertools.product((1, -1), repeat=n):
        _, again = moments_again(step, opening(range(n), dict(enumerate(pattern))), spiral_couplings(n))
        found.add(again)
    return sorted(found)


def laid_along(step, n, q):
    """A spiral of n selves opened with a spiral of q's own opening, laid along it."""
    small = exhibit_spiral_priors(q)
    priors = {i: small[i % q] for i in range(n)}
    _, again = moments_again(step, opening(range(n), priors), spiral_couplings(n))
    return again


def own_again(step, q):
    _, again = moments_again(step, opening(range(q), exhibit_spiral_priors(q)), spiral_couplings(q))
    return again


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 61
    names, page = resolver(root)
    step = names["_17_next_existing"]
    all_is = True

    print("1. A spiral with all its openings of + and − priors: moments to its parities again")
    for n in range(2, 14):
        found = every_opening(step, n)
        by_division = sorted({(4 if n % 2 else 2) * d for d in divisors(n)})
        same = found == by_division
        all_is = all_is and same
        print(f"   {n:>2} selves · {found} · {'4' if n % 2 else '2'} times a number dividing {n}: {'is' if same else 'is-not'}")
    print()

    print("2. A spiral opened with a smaller spiral's own opening laid along it")
    for n, q in ((9, 3), (15, 3), (15, 5), (21, 3), (21, 7), (25, 5), (7, 3), (11, 3), (11, 5), (13, 5)):
        print(f"   {n:>2} selves, a spiral of {q} laid along · again with {laid_along(step, n, q)} moments · the spiral of {q}'s own: {own_again(step, q)}")
    print()

    print(f"3. Spirals of 2 to {to} selves, a spiral tested against the smaller uncrossed spirals")
    uncrossed = []
    for n in range(2, to + 1):
        crossing = [q for q in uncrossed if laid_along(step, n, q) == own_again(step, q)]
        by_division = [q for q in uncrossed if n % q == 0]
        all_is = all_is and crossing == by_division
        if not crossing:
            uncrossed.append(n)
    print("   uncrossed:", ", ".join(str(n) for n in uncrossed))
    primes = [n for n in range(2, to + 1) if all(n % d for d in range(2, int(n ** 0.5) + 1))]
    all_is = all_is and uncrossed == primes
    print(f"   the primes to {to}, by division: {'the same' if uncrossed == primes else 'other-than'}")
    print("   a crossing executed is a dividing, at all the spirals:", "is" if all_is else "is-not")
    print()

    print("4. By division, no resolver in it: from a span to its square")
    known = [2]
    span = 4
    while span <= 65536:
        new = [n for n in range(max(known) + 1, span) if all(n % q for q in known if q * q <= n)]
        known += new
        print(f"   spirals below {span:>6} · {len(new):>5} new · {len(known):>5} together")
        span = span * span
    print()
    print("All is." if all_is else "An is-not is above.")
    sys.exit(0 if all_is else 1)
