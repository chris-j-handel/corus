"""Exhibit ONE Natural Resolver's sentence of a spiral of selves, gone on along the spiral, by the living code as it is.

The living sentence, under *Two moments before, inverting.*: with a spiral opening with a prior for all its selves,
a self's prior from its third moment on is a prior of the self it receives from, two moments before, inverting.

Gone on along the spiral, at one now: the self j couplings ahead has, inverting j times, a self's prior of 2j
moments before; and the self j couplings back has, inverting j times, a self's prior of 2j moments next.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_two_moments_before_inverting_gone_on_along_a_spiral.py incoming/v406Reiman/instruments/resolver_as_it_is.py .
The second path is the root with Exhibit ONE Natural Resolver, whose own code is executed.
"""
import importlib.util, sys
from itertools import product
sys.dont_write_bytecode = True


def opened(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def priors_by_moment(it, step, n, openings, moments):
    society, out = it.opening(range(n), dict(enumerate(openings))), []
    couplings = it.spiral_couplings(n)
    for _ in range(moments):
        out.append([dict(society[a][0]).get(it.S) for a in range(n)])
        society = step(society, couplings)
    return out


if __name__ == "__main__":
    it = opened(sys.argv[1], "the_code_as_it_is")
    names, _ = it.resolver(sys.argv[2])
    step = names["_17_next_existing"]
    found = 0

    def line(sentence, it_is):
        global found
        found += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    one, ahead, back, societies, with_a_prior = True, True, True, 0, True
    for n in range(1, 9):
        for openings in product((1, -1), repeat=n):
            societies += 1
            p = priors_by_moment(it, step, n, openings, 4 * n + 8)
            with_a_prior = with_a_prior and all(x in (1, -1) for row in p for x in row)
            for t in range(2, len(p)):
                for a in range(n):
                    one = one and p[t][a] == -p[t - 2][(a - 1) % n]
            for t in range(len(p)):
                for a in range(n):
                    for j in range(0, 2 * n + 1):
                        if t - 2 * j >= 0:
                            ahead = ahead and p[t][(a + j) % n] == (-1) ** j * p[t - 2 * j][a]
                        if t + 2 * j < len(p):
                            back = back and p[t][(a - j) % n] == (-1) ** j * p[t + 2 * j][a]
    line(f"The spirals executed are of 1 to 8 selves, all {societies} openings of a prior + or − for all selves, by the living code's own lines; a self is with a prior, + or −, at all their moments", societies == 510 and with_a_prior)
    line("The living sentence: a self's prior, from its third moment on, is the prior of the self it receives from, two moments before, inverting", one)
    line("Gone on along the spiral, at one now: the self j couplings ahead has, inverting j times, a self's prior of 2j moments before, j of 0 to twice round", ahead)
    line("And the self j couplings back has, inverting j times, a self's prior of 2j moments next: a self's sequence along moments is its spiral at one now, gone round from it", back)
    print(f"\n{4 - found} of 4 are is")
    sys.exit(1 if found else 0)
