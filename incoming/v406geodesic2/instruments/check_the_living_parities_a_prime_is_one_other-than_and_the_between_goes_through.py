"""The living parities: a prime is one other-than, and the between goes through (session v406geodesic2).

A partner's word of 24 November, re-said: go on, and with no equilibria side, the curve as an existing thing to be fitted.
The curve is a non-existing between going through the fractured fractal stable form geodesic surface of living parities.

No curve is in this instrument. A number's living parity is a + with an even number of primes multiplied in it and a −
with an odd number, 1 a +: v406other2's naming, a prime an inversion. Executed here, all or none, from the numbers alone:
  1  a number's parity by this session's lean line, one nand a prime;      2  all a number's backs surface one parity;
  3  a prime's own path, a me alone: next is other-than now;               4  by +1: its is-not, a measuring;
  5  the between, at no number of its own: the numbers it goes through;    6  the −s the more at all other numbers, to a number;
  7  the walk's straying beside the square's side, a measuring;            8  a number's parts, a part and its other.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_living_parities_a_prime_is_one_other-than_and_the_between_goes_through.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import importlib.util, math, sys
sys.dont_write_bytecode = True
TO = 4_194_304                                                                    # v406other2's surface, 2 doubled 22 times
OTHER = bytes([1, 0]) + bytes(range(2, 256))                                      # a byte's other-than: a 0 a 1, a 1 a 0


def the_living_parities(to):
    """All numbers' parities to a number, by the primes alone: a 0 a +, a 1 a −; a prime multiplied in, an other-than."""
    crossed = bytearray(to + 1); primes = []
    for n in range(2, to + 1):
        if not crossed[n]:
            primes.append(n)
            if n * n <= to: crossed[n * n::n] = b"\x01" * len(range(n * n, to + 1, n))
    parity = bytearray(to + 1)
    for p in primes:
        power = p
        while power <= to:
            parity[power::power] = parity[power::power].translate(OTHER); power *= p
    return parity, primes


def the_walk(parity, to):
    """The +s less the −s, from 1 to a number, number by number."""
    walk, at = [0] * (to + 1), 0
    for n in range(1, to + 1):
        at += 1 - 2 * parity[n]; walk[n] = at
    return walk


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", sys.argv[1])
    its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    parity, primes = the_living_parities(TO)
    least = {}                                                                    # a number's least prime, to 100,000
    for p in primes:
        if p > 100_000: break
        for n in range(p, 100_001, p): least.setdefault(n, p)
    by_nand, nands = {1: True}, 0                                                 # a + an is
    for n in range(2, 100_001):
        by_nand[n] = its.other_than(by_nand[n // least[n]]); nands += 1
    line("A number's living parity is this session's lean line on the numbers: a number's parity is the other-than of the parity of the number back of it, with one prime less, and 1 is a +. By nand alone, one nand a number, it is the parity of its primes multiplied, with all numbers of 1 to 100,000",
         all(by_nand[n] == (parity[n] == 0) for n in range(1, 100_001)) and nands == 99_999)
    backs = all(len({by_nand[n // p] for p in primes[:25] if n % p == 0} | {by_nand[n // least[n]]}) == 1 for n in range(2, 100_001))
    line("All a number's backs surface one parity: with all primes of 2 to 97 multiplied in a number, the number with that prime less has one parity, 2 to 100,000. A + and a − surface together at no number", backs)
    alone = all([parity[p ** k] for k in range(0, int(math.log(TO, p)) + 1)] == [k % 2 for k in range(0, int(math.log(TO, p)) + 1)] for p in primes[:25])
    line("A prime's own path, 1, the prime, its square and on, is a me alone: next is other-than now, now is other-than prior, and next is its prior again, with the primes of 2 to 97", alone)

    steps = sum(1 for n in range(1, TO) if parity[n] != parity[n + 1])
    line(f"By +1, next is other-than now at {steps:,} of {TO - 1:,} steps, one step in two to a part in a thousand: along multiplying it is at all steps, and along +1 it is a measuring, with no line of a me alone",
         abs(steps / (TO - 1) - 0.5) < 0.001 and steps == 2_096_902)

    walk = the_walk(parity, TO)
    through = [n for n in range(1, TO + 1) if walk[n] == 0]
    line("The between is at no number of its own. It goes through the numbers with the +s and the −s to them the same: 2, 4, 6, 10, 16, 26, 40, 96 and 586, nine numbers to 4,194,304", through == [2, 4, 6, 10, 16, 26, 40, 96, 586])
    line("At all other numbers of 2 to 4,194,304 the −s are the more. A field has this sentence's is-not at 906,150,257, Pólya's of 1919 broken: stepped to a number is no saying with all numbers",
         max(walk[2:]) == 0 and walk[1] == 1)
    farthest = max(range(2, TO + 1), key=lambda n: -walk[n] / math.sqrt(n))
    line(f"The walk's straying from its between, beside the square's side: it is at the most {-walk[farthest] / math.sqrt(farthest):.2f} sides, at {farthest:,}, and at 4,194,304 the −s are {-walk[TO]:,} the more, with a side of 2,048. A measuring, and no bound",
         farthest == 96_862 and 1.325 < -walk[farthest] / math.sqrt(farthest) < 1.335 and walk[TO] == -582)
    parts = lambda n: [d for d in range(1, n + 1) if n % d == 0]
    line("A number's parts, v406other2's sentence executed again by the lean line's parities: a part has its other, the number by it less; with a number of a − a part and its other are a + and a −; and the parts' parities added are 1 with a square and 0 with all else, 1 to 2,000",
         all(sum(1 - 2 * parity[d] for d in parts(n)) == (1 if math.isqrt(n) ** 2 == n else 0) for n in range(1, 2001))
         and all(parity[d] != parity[n // d] for n in range(2, 2001) if parity[n] for d in parts(n)))

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
