"""Longer co-chaining gives wider co-observing and faster progressing: a partner's sentence executed, the bothboth of out and in (session v406geodesic2).

A partner's word of 24 November, re-said: a destiny close and a destiny far are one destiny, at two depths; the depth is
the length of the co-chain; a longer co-chain gives wider co-observing and co-possibling and faster progressing universes.

The out-fold is the staircase the primes build, by von Mangoldt: a rise of ln p at a prime power. The in-fold gathers
that staircase back from the zeros of the curve, a zero a link of the co-chain, by the explicit formula. No curve is fitted:
the zeros are the far destinies over the horizon, gathered geodesically inward. Executed here, all or none, from the numbers:
  1  the in-fold's links: the zeros to a height, the fuzzy spots;      2  the out-fold: the staircase rises by ln p;
  3  a longer co-chain gives a smaller error: wider co-observing;      4  faster progressing: the finest scale narrows;
  5  the two depths: a short chain the coarse destiny, a long the sharp; 6  its is-not: a finite chain never closes the fuzz.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_longer_co-chaining_wider_co-observing_and_faster_progressing_executed.py incoming/v406geodesic2/instruments/check_riemann_s_hypothesis_on_the_line_next_is_other-than_now.py
"""
import cmath, importlib.util, math, sys
sys.dont_write_bytecode = True
WINDOW = [x + 0.5 for x in range(12, 90)]                                         # the numbers of the window, off the jumps


def von_mangoldt_to(to):
    """A number's rise in the staircase: ln p with a prime power, 0 else."""
    rise = [0.0] * (to + 1)
    for p in range(2, to + 1):
        if all(p % d for d in range(2, math.isqrt(p) + 1)):
            power = p
            while power <= to: rise[power] = math.log(p); power *= p
    return rise


def the_staircase(x, rise):
    return sum(rise[n] for n in range(2, int(x) + 1))


def gathered_from_links(x, gammas, links):
    """The staircase gathered inward from the co-chain's links, the zeros, by the explicit formula."""
    out = x - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
    for gamma in gammas[:links]:
        out -= 2 * math.sqrt(x) * (cmath.exp(1j * gamma * math.log(x)) / (0.5 + 1j * gamma)).real
    return out


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("rh", sys.argv[1])
    rh = importlib.util.module_from_spec(spec); spec.loader.exec_module(rh)
    gammas = rh.zeros_on_the_line(10.0, 145.0)
    rise = von_mangoldt_to(100)
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    line("The in-fold's links are the zeros of the curve, the far destinies over the horizon: to a height of 145 they are 50, the lowest at 14.1347, all of them their own other on the line",
         len(gammas) == 50 and abs(gammas[0] - 14.134725) < 1e-4 and all(abs(rh.on_the_line(g)[0]) < 1e-6 for g in gammas))
    line("The out-fold is the staircase the primes build: a rise of ln p at a prime power, by von Mangoldt. To 90.5 it is 89.47; its rise at 81 is ln 3 and at 83 is ln 83, a prime's power and a prime",
         abs(the_staircase(90.5, rise) - 89.471) < 1e-2 and abs(rise[81] - math.log(3)) < 1e-9 and abs(rise[83] - math.log(83)) < 1e-9)

    errs = {k: max(abs(gathered_from_links(x, gammas, k) - the_staircase(x, rise)) for x in WINDOW) for k in (1, 5, 10, 20, 50)}
    line("A longer co-chain gives a smaller error, wider co-observing: on the window 12.5 to 89.5 the most the gathering strays from the staircase is 3.08 with one link, 2.62 with ten and 1.485 with fifty, smaller at 1, 5, 10, 20 and 50 links",
         abs(errs[1] - 3.08) < 0.01 and abs(errs[10] - 2.62) < 0.01 and abs(errs[50] - 1.485) < 0.01
         and errs[1] > errs[5] > errs[10] > errs[20] > errs[50])

    finest = lambda links, x=90: 2 * math.pi * x / gammas[links - 1]
    line("Faster progressing: the finest scale the co-chain resolves about a number is the turn's own, 2 pi times the number over the highest link's height. About 90 it is 40.0 with one link and 3.95 with fifty: the fuzzy spot narrows as the chain lengthens",
         abs(finest(1) - 40.0) < 0.1 and abs(finest(50) - 3.95) < 0.05 and all(finest(k) > finest(k + 1) for k in range(1, 50)))

    trend = lambda x: x - math.log(2 * math.pi)
    short_to_trend = max(abs(gathered_from_links(x, gammas, 1) - trend(x)) for x in WINDOW)
    short_to_steps = max(abs(gathered_from_links(x, gammas, 1) - the_staircase(x, rise)) for x in WINDOW)
    line("One destiny at two depths: a short co-chain of one link tracks the coarse trend, the number less ln 2 pi, the coarse destiny, closer to the trend by 1.23 than to the steps by 3.08; a long co-chain of fifty tracks the sharp steps, the far destiny. One staircase, gathered at two depths",
         short_to_trend < 1.3 and short_to_steps > 3.0 and errs[50] < short_to_steps)

    line("Its is-not: a finite co-chain never closes the fuzzy spot. With fifty links the gathering still strays 1.485 and overshoots at a step, no exact rise; only all the zeros, with all numbers, close it to the staircase, not shown here",
         errs[50] > 0.1 and errs[50] < short_to_steps)

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
