"""v406geodesic2 · a partner's saying executed two ways: ten other-thans in a row, and 3, 2, 1 and 0 of 3.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_ten_rows_of_the_four_moments.py .

A partner's saying of 23 November, as said in the transcripts, pared. Re-said: ten other-thans in a row, of three pairs of moments,
self, other and all, a prior and a now; 3 of 3, 2 of 3, 1 of 3 and 0 of 3; same-existing is other-than the all of 3 and other-than
the none of 3; and next is 2 or 1, an other-than at a step.
One way: the four moments' three and-thens are the three pairs of moments, and the rows of the four are ten.
An other way: three is-or-is-nots, a prior or a now, are eight, and six of them are one round of six.
Whole numbers alone. It opens no file and writes none. All or none: with one line not is, the check is not.
"""
import itertools, sys
results = []
def line(name, ok): results.append((name, bool(ok)))
about = lambda st: (lambda n: 2 * st - n)
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
def kind(stations):
    moved = {by(n, stations) - n for n in range(-240, 241)}
    return ("me", moved.pop()) if len(moved) == 1 else ("other", {(by(n, stations) + n) // 2 for n in range(-240, 241)}.pop())

FOUR = (30, 60, 90, 120)                                  # other-than, all, other-than, all
rows = [FOUR[a:b] for a in range(4) for b in range(a + 1, 5)]
of_3 = lambda r: len(r) - 1                               # the and-thens a row is of, of the four's three
line("the four moments have three and-thens, three pairs of moments one after an other, and their rows in a row are ten: one of 3 of 3, two of 2 of 3, three of 1 of 3 and four of 0 of 3",
     len(rows) == 10 and [sum(of_3(r) == k for r in rows) for k in (3, 2, 1, 0)] == [1, 2, 3, 4])
line("3 of 3 is the four, 120 on, a me in its next universe; 0 of 3 is a podaling alone, an other, four of them",
     [kind(r) for r in rows if of_3(r) == 3] == [("me", 120)] and [kind(r) for r in rows if of_3(r) == 0] == [("other", s) for s in FOUR])
line("1 of 3 is two in a row, a me 60 on, three of them; 2 of 3 is three in a row, one podaling, an other, about 60 and about 90",
     [kind(r) for r in rows if of_3(r) == 1] == [("me", 60)] * 3 and [kind(r) for r in rows if of_3(r) == 2] == [("other", 60), ("other", 90)])
line("the rows other-than the 3 of 3 and other-than the 0 of 3 are five, of 2 and of 1; a row and the row one moment more are a me and an other in turn",
     sum(of_3(r) in (1, 2) for r in rows) == 5 and all(kind(FOUR[:k])[0] != kind(FOUR[:k + 1])[0] for k in (1, 2, 3)))

corners = list(itertools.product((0, 1), repeat=3))       # self, other and all: a prior, 0, or a now, 1
line("three is-or-is-nots, self, other and all, a prior or a now, are eight: one of 3 of 3, three of 2 of 3, three of 1 of 3 and one of 0 of 3",
     [sum(sum(c) == k for c in corners) for k in (3, 2, 1, 0)] == [1, 3, 3, 1])
six = [c for c in corners if sum(c) in (1, 2)]
step = lambda a, b: sum(x != y for x, y in zip(a, b)) == 1
round_ = [(1, 1, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 1), (0, 1, 0)]
line("the six other-than the all of 3 and other-than the none of 3 are one round of six, one other-than at a step, 2 of 3 and 1 of 3 in turn; a round is six other-thans, and no ten",
     sorted(round_) == sorted(six) and all(step(round_[i], round_[(i + 1) % 6]) and sum(round_[i]) != sum(round_[(i + 1) % 6]) for i in range(6))
     and all(sum(step(a, b) for b in six) == 2 for a in six))
along = lambda c: (c[0] - c[1], c[0] + c[1] - 2 * c[2])   # observed along (1, 1, 1)
line("observed along (1, 1, 1) the all of 3 and the none of 3 are at one place, the co-linear's own, and the six are about it at one distance, the seventh drawing's round of six",
     along((1, 1, 1)) == along((0, 0, 0)) == (0, 0) and len({along(c)[0] ** 2 * 3 + along(c)[1] ** 2 for c in six}) == 1 and len({along(c) for c in six}) == 6)

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
