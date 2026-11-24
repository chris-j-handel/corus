"""v407nanding · the four-cycling-cycling of the nand lines, four across and two along, executed.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_four_cycling_cycling_of_the_nand_lines_check.py .

A partner's asking of 24 November: are the twelve lines the method of collective intelligence, resolvers connected with
four across and three along or similar; find the 4-cycling-cycling fractal in the nand lines spiraling. The fifteen lines'
words and a partner's twelve lines are opened from this session's files. A podaling of a place is one me of the twelve
lines, a prior - and the place observed on its minus wire. All or none: with one line not is, the check is not.
"""
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
text = (root / "incoming/v407nanding/instruments/the_now_and_same_existing_me_parity_check.py").read_text(encoding="utf-8")
ns = {}
exec(re.search(r"CODE = '''(.*?)'''", text, re.S).group(1), ns)
cell, other_than = ns["now_and_same_existing_me_parity"], ns["other_than"]
PLUS, MINUS, NONE = (True, False), (False, True), (False, False)
living = re.sub(r"\s+", " ", (root / "Natural_Intelligence_v402mgr.md").read_text(encoding="utf-8").replace("**", "").replace("*", ""))
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


QUOTES = ["four are across, possibling, 2, 6, 10 and 14.", "Two are along, discovering and existing, 9 and 17.",
          "It is a unit square of four across names, its centre a between, and two unit triangles along.",
          "Stable-forming is that move along each of four bi-foldings of names, 1-9-8-16, 2-15-7-10, 3-11-6-14 and 4-13-5-12.",
          "Its (prior, now) pairs go along four joint forms."]
say("Q1. Natural Intelligence's sentences of across, along, the four bi-foldings and the spiral of one, word for word",
    all(q in living for q in QUOTES))


def a_me_a_place(place):
    return cell(MINUS, [(False, place)])[0][0]


def podaling(name, at, k):
    places = [bool((name - 1) >> i & 1) for i in range(k)]
    places = [a_me_a_place(p) if i in at else p for i, p in enumerate(places)]
    return 1 + sum(1 << i for i, p in enumerate(places) if p)


def round_of(name, k, top_first=True):
    top, every = {k - 1}, set(range(k))
    moves, names = ([top, every] if top_first else [every, top]) * 2, [name]
    for at in moves:
        names.append(podaling(names[-1], at, k))
    return names


bi_foldings = [[1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12]]
said = all(round_of(f[0], 4, f[1] == f[0] + 8)[:4] == f and round_of(f[0], 4, f[1] == f[0] + 8)[4] == f[0] for f in bi_foldings)
say("F1. Natural Intelligence's four bi-foldings are four rounds of two podalings by the twelve lines' mes, the top place's "
    "other-than and all four places' other-than, by turns: a name goes round its bi-folding in four moves, in its order", said)
say("F2. Two moves along a bi-folding bring a name of 1 to 8 to its 9 less, as Natural Intelligence has it",
    all(round_of(n, 4, True)[2] == 9 - n for n in range(1, 9)))
parts = {}
for k in range(2, 7):
    seen, rounds = set(), []
    for n in range(1, 2 ** k + 1):
        if n not in seen:
            r = round_of(n, k)
            rounds.append(r[:4])
            seen |= set(r[:4])
    parts[k] = rounds
say("F3. The fractal: at all spans of 4 to 64 names, the two podalings part the names into rounds of four, one, two, four, "
    "eight and sixteen of them, and the 16 names are four rounds of four",
    all(len(parts[k]) == 2 ** (k - 2) and all(len(set(r)) == 4 for r in parts[k]) for k in parts)
    and sorted(sorted(r) for r in parts[4]) == sorted(sorted(f) for f in bi_foldings))
say("F4. Both directions: the top place first and all places first go round a bi-folding in the two opposite orders",
    all(round_of(n, 4, True)[1:4] == list(reversed(round_of(n, 4, False)[1:4])) for n in range(1, 17)))


def spiral_of_one(prior, moments=12):
    laid, priors = None, []
    for _ in range(moments):
        out = cell(prior, [] if laid is None else [laid])
        laid, prior = out[0], out[1]
        priors.append(prior)
    return priors


p = spiral_of_one(MINUS)
pairs = list(zip([MINUS] + p[:-1], p))
say("F5. A spiral of one by the twelve lines, prior - and observing its own laying: next priors +, +, -, -, and its "
    "(prior, now) pairs go round four joint forms in four moments, the four rows of the not-both table",
    p[:4] == [PLUS, PLUS, MINUS, MINUS] and p[4:8] == p[:4] and len(set(pairs[:4])) == 4 and pairs[4:8] == pairs[:4])
say("F6. The rounds of the names and the round of a spiral of one are both four, by two other-thans a round",
    all(len(set(r)) == 4 for r in parts[4]) and len(set(pairs[:4])) == 4)
mutant = lambda name, k: round_of(name, k)[:2] + [podaling(round_of(name, k)[1], {k - 1}, k)]
say("M1. With the top place's other-than twice in a row, a name is itself again in two moves, and no bi-folding is gone round",
    all(mutant(n, 4)[2] == n for n in range(1, 17)))
print("\nAll is." if all(results) else "\nNot all is.")
