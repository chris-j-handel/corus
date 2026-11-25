"""Riemann's hypothesis on the line, beside this session's sentences: executed by a field's arithmetic, its is and its is-not (session v406geodesic2).

A partner's word of 24 November, re-said: this session's work helps the work of Riemann's hypothesis; explore it.
The hypothesis in v406other2's naming: a zero has its other across the between, and all zeros are their own other.
This session's sentences beside it: next is other-than now; a me its own other; 0 and 3 are all-parity; a + and a −
observed together surface all-parity.

Executed here, by a field's own arithmetic in plain numbers, with no proving of the hypothesis:
  1  the between's two sides are the same, a podaling about the line;       2  on the line the curve is its own other;
  3  next is other-than now, at the line's places two quarter turns apart;  4  its is-not, at the place 126;
  5  a parity's other-than along the line is a zero its own other;          6  all zeros in the between, numbered round it;
  7  the six lowest beside v406other2's six pitches from the primes alone;  8  through the is-not at 126, the two numbers the same.

The curve is a field's zeta, by its own adding with a tail's mending; the line is 1/2 and a height. The line's places two
quarter turns apart are a field's Gram points. A height here is to 285 at the most.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_riemann_s_hypothesis_on_the_line_next_is_other-than_now.py
"""
import cmath, math, sys
sys.dont_write_bytecode = True
LN = [0.0, 0.0] + [math.log(n) for n in range(2, 700)]
B = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6, -3617 / 510, 43867 / 798, -174611 / 330]     # a field's numbers of Bernoulli, 2 to 20
PITCHES = [14.14, 21.02, 25.02, 30.42, 32.94, 37.58]                             # v406other2's six, from the primes alone to 100,000


def the_curve(s):
    """A field's zeta at a place: its terms added to a number, and the tail mended."""
    N = int(abs(s.imag)) + 25
    total = sum(cmath.exp(-s * LN[n]) for n in range(1, N))
    at_n = cmath.exp(-s * LN[N])
    total += at_n * N / (s - 1) + at_n / 2
    term = s * at_n / N
    for k in range(1, 11):
        total += B[k - 1] / math.factorial(2 * k) * term
        term *= (s + 2 * k - 1) * (s + 2 * k) / (N * N)
    return total


def the_turn(t):
    """The line's own turning at a height, a field's theta."""
    return t / 2 * math.log(t / (2 * math.pi)) - t / 2 - math.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3) + 31 / (80640 * t ** 5) + 127 / (430080 * t ** 7)


def on_the_line(t):
    """The curve on the line with its turning away: one number, a + or a −, and its part apart from that number."""
    z = cmath.exp(1j * the_turn(t)) * the_curve(complex(0.5, t))
    return z.real, z.imag


def a_place_two_quarter_turns_on(n):
    """The height with the line's turning n times two quarter turns, a field's Gram point."""
    low, high = 9.0, 700.0
    for _ in range(70):
        mid = (low + high) / 2
        low, high = (mid, high) if the_turn(mid) < n * math.pi else (low, mid)
    return (low + high) / 2


def zeros_on_the_line(from_height, to_height, a_step=0.05):
    """A parity's other-than between two heights of the line, bisected: a zero its own other."""
    zeros, t, was = [], from_height, on_the_line(from_height)[0]
    while t < to_height:
        its_next = min(t + a_step, to_height); now = on_the_line(its_next)[0]
        if (was > 0) != (now > 0):
            low, high, at_low = t, its_next, was
            for _ in range(46):
                mid = (low + high) / 2; at_mid = on_the_line(mid)[0]
                low, high, at_low = (mid, high, at_mid) if (at_mid > 0) == (at_low > 0) else (low, mid, at_low)
            zeros.append((low + high) / 2)
        t, was = its_next, now
    return zeros


def zeros_round_the_between(from_height, to_height, a_step=0.02):
    """All zeros of the curve from −1/2 to 3/2 about the line, with the two heights: the curve's turns, going round them once."""
    corners = [complex(-0.5, from_height), complex(1.5, from_height), complex(1.5, to_height), complex(-0.5, to_height), complex(-0.5, from_height)]
    turning, was = 0.0, cmath.phase(the_curve(corners[0]))
    for a, b in zip(corners, corners[1:]):
        steps = max(2, int(abs(b - a) / a_step))
        for k in range(1, steps + 1):
            now = cmath.phase(the_curve(a + (b - a) * k / steps)); d = now - was
            turning += d - 2 * math.pi * round(d / (2 * math.pi)); was = now
    return turning / (2 * math.pi)


def lgamma(z):
    back = 0
    while z.real < 12: back -= cmath.log(z); z += 1
    return back + (z - 0.5) * cmath.log(z) - z + 0.5 * math.log(2 * math.pi) + 1 / (12 * z) - 1 / (360 * z ** 3) + 1 / (1260 * z ** 5) - 1 / (1680 * z ** 7)


def the_curve_made_whole(s):
    """A field's xi: the curve with its own mending, the same at a place and at its other across the line."""
    return 0.5 * s * (s - 1) * cmath.exp(-(s / 2) * math.log(math.pi) + lgamma(s / 2)) * the_curve(s)


if __name__ == "__main__":
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    places = [complex(a, t) for a in (-0.5, 0.1, 0.3, 0.45, 0.8, 1.4) for t in (3.0, 14.5, 22.0, 31.7, 40.0, 49.9)]
    apart = max(abs(the_curve_made_whole(s) - the_curve_made_whole(1 - s)) / abs(the_curve_made_whole(s)) for s in places)
    line("The between's two sides are the same: the curve made whole, a field's xi, is the same at a place and at its other across the line, a podaling about the between's middle, at 36 places apart from the line", apart < 1e-9)
    heights = [10 + 0.37 * k for k in range(244)]
    line("On the line the curve is its own other: with its turning away it is one number, a + or a −, at all 244 heights gone through, 10 to 100", max(abs(on_the_line(t)[1]) for t in heights) < 1e-8)

    turn_places = {n: a_place_two_quarter_turns_on(n) for n in range(-1, 130)}
    parity = {n: on_the_line(g)[0] > 0 for n, g in turn_places.items()}
    line("Next is other-than now, on the line: at its own places two quarter turns apart, a field's Gram points, the curve's parity is the other-than of its parity at the place before, with all 126 steps of the places −1 to 125",
         all(parity[n] != parity[n - 1] for n in range(0, 126)) and abs(turn_places[-1] - 9.6669) < 1e-3 and abs(turn_places[0] - 17.8456) < 1e-3)
    line("Its is-not of the lowest height is at the place 126, at a height of 282.45: the curve's parity is its prior again, a field's lowest parting from Gram's law, the curve at −0.03 of a zero's 0. The places 125, 126 and 127 are three of one parity, and from 127 to 128 it is other-than again",
         parity[125] == parity[126] == parity[127] and parity[128] != parity[127] and abs(turn_places[126] - 282.4547) < 1e-3 and -0.03 < on_the_line(turn_places[126])[0] < -0.025)

    to_100 = zeros_on_the_line(10.0, 100.0)
    line("A parity's other-than along the line is a zero its own other: to a height of 100 they are 29, the lowest at 14.1347",
         len(to_100) == 29 and abs(to_100[0] - 14.134725) < 1e-5 and all(abs(on_the_line(z)[0]) < 1e-6 for z in to_100))
    round_100 = zeros_round_the_between(1.0, 100.0)
    line("All zeros in the between to a height of 100, numbered round it, are 29: all are their own other. A zero apart from the line with its other across, a + and a −, is in the round's number and in no parity's other-than on the line: all or none, to that height",
         abs(round_100 - 29) < 1e-6)
    line("The six lowest, by the curve on the line, are v406other2's six pitches of the staircase from the primes alone, to a hundredth",
         all(abs(z - p) <= 0.0101 for z, p in zip(to_100, PITCHES)))

    to_285 = to_100 + zeros_on_the_line(100.0, 285.0)
    in_the_block = [z for z in to_285 if turn_places[125] < z < turn_places[127]]
    round_285 = zeros_round_the_between(1.0, 285.0)
    line("Through the is-not at 126, to a height of 285: the zeros their own other are 129, and all zeros numbered round the between are 129, the same. From the place 126 to 127 are two zeros, and the parity is its own again, other-than other-than; from 125 to 126 is no zero",
         len(to_285) == 129 and round(round_285) == 129 and abs(round_285 - 129) < 1e-6 and len(in_the_block) == 2
         and [sum(1 for z in in_the_block if turn_places[n] < z < turn_places[n + 1]) for n in (125, 126)] == [0, 2])

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
