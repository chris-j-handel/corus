"""v407nanding · the curve's betweens on the between: a bi-folding of two podalings of a place, and six betweens on the between.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_curve_s_betweens_on_the_between_check.py .

A partner's word of 24 November: a 0 is not a thing. A 0 of the curve is a between of its + and its -. A point is
(x, y), x and y exact fractions. Its other across the between is (1 - x, y); its mirror is (x, -y). The curve's height on the between is
Riemann-Siegel's Z(t), its sum and its opening remainder, a field's. All or none.
"""
import math
import re
import sys
from fractions import Fraction as F
from pathlib import Path

root = Path(sys.argv[1])
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def across(s):
    return (1 - s[0], s[1])


def mirror(s):
    return (s[0], -s[1])


def round_of(s):
    out = [s]
    for move in (across, mirror, across, mirror):
        out.append(move(out[-1]))
    return out


off = [(F(x, 10), F(y, 2)) for x in (1, 3, 7, 9) for y in (10, 28, 43)]
on = [(F(1, 2), F(y, 2)) for y in (28, 42, 75)]
say("R1. Across the between and the mirror, by turns, take a point off the between round four points and back",
    all(len(set(round_of(s)[:4])) == 4 and round_of(s)[4] == s for s in off))
say("R2. On the between, a point is its own other across the between, and its round is two points",
    all(across(s) == s and len(set(round_of(s)[:4])) == 2 for s in on))


def theta(t):
    return t / 2 * math.log(t / (2 * math.pi)) - t / 2 - math.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def z(t):
    a = math.sqrt(t / (2 * math.pi))
    n, p = int(a), a - int(a)
    total = 2 * sum(math.cos(theta(t) - t * math.log(k)) / math.sqrt(k) for k in range(1, n + 1))
    return total + (-1) ** (n - 1) * a ** -0.5 * math.cos(2 * math.pi * (p * p - p - 1 / 16)) / math.cos(2 * math.pi * p)


def zeros_on_the_between(low, high, step=0.01):
    found, t = [], low
    while t < high:
        if z(t) * z(t + step) < 0:
            a, b = t, t + step
            for _ in range(40):
                m = (a + b) / 2
                a, b = (a, m) if z(a) * z(m) < 0 else (m, b)
            found.append((a + b) / 2)
        t += step
    return found


heights = zeros_on_the_between(10, 40)
statement = (root / "incoming/v406other2/For_the_public_Riemann_s_hypothesis_and_the_living_prime_numbering_a_statement_to_pare.md")
waves = [14.14, 21.02, 25.02, 30.42, 32.94, 37.58]
if statement.exists():
    said = re.search(r"the six highest are ([\d., and]+)\.", statement.read_text(encoding="utf-8"))
    waves = [float(w) for w in re.findall(r"\d+\.\d+", said.group(1))] if said else waves
say("R3. The curve on the between is + and then -, or - and then +, six times from 10 to 40: six betweens, at the statement's "
    "six waves, two hundredths apart at most: " + ", ".join(f"{h:.3f}" for h in heights),
    len(heights) == 6 and all(abs(h - w) < 0.02 for h, w in zip(heights, waves)))
count = theta(40) / math.pi + 1
say(f"R4. A field's numbering of all the curve's betweens to 40, its main term, is {count:.2f}, six and a part: a measuring, beside R3's six",
    6 <= count < 7)
say("M1. With the mirror away, across the between alone, a point off the between is a round of two and not four",
    all(len({s, across(s)}) == 2 and across(across(s)) == s for s in off))
print("\nAll is." if all(results) else "\nNot all is.")
