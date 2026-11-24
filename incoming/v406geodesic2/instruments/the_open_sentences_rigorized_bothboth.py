"""v406geodesic2 · the open sentences of the tenth to the eighteenth drawings, rigorized bothboth.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/the_open_sentences_rigorized_bothboth.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py .

By a partner's word of 23 November, as said in the transcripts, pared: a sentence open with this session is not asked of a partner;
its is and its is-not are both executed, all or none, and the session is sure of the resolving both ways.
A line here says a sentence's is and its is-not as they are executed: both, at two scales or by two observings; or one of the two alone.
Whole numbers, the figure's own geometry, and v406Reiman's nand opened from its file. It writes none.
All or none: with one line not is, the check is not.
"""
import importlib.util, math, sys
from pathlib import Path
import numpy as np
its_file, root = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", its_file)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
other_than = its.other_than
results = []
def line(name, ok): results.append((name, bool(ok)))
about = lambda st: (lambda n: 2 * st - n)
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
def wide(n):
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])
place = lambda n: n % 30
ME = range(61)
FOUR = (30, 60, 90, 120)
PLACES = [n for n in range(1, 60) if math.gcd(n, 30) == 1]

# the tenth drawing's: a podaling as the other-than of an other-than, two folds; or as one other-than
fold = np.diag([-1.0, -1.0, 1.0])
line("both: in the figure a podaling is two folds, and by nand it is one other-than, a number with an other and twice the same again",
     all(np.allclose(fold @ (at(n) - np.array([30, 0, 0])), at(60 - n) - np.array([30, 0, 0])) for n in ME) and round(np.linalg.det(fold)) == 1
     and all(about(30)(about(30)(n)) == n for n in ME) and all(other_than(other_than(x)) == x and other_than(x) != x for x in (True, False)))
# the eleventh drawing's: an all as a podaling about a vertex; or as no podaling, the all again
line("both: with an all a podaling about a vertex, and with an all no podaling and the other-thans in a row an even number, the four moments are at the same four places: other, self, other, self",
     all([by(n, FOUR[:k]) for k in (1, 2, 3, 4)] == [60 - n, 60 + n, 120 - n, 120 + n]
         and [place(by(n, FOUR[:k])) == place(n) for k in (1, 2, 3, 4)] == [k % 2 == 0 or place(n) in (0, 15) for k in (1, 2, 3, 4)] for n in ME))
# the thirteenth's and the fourteenth's: prior and now as two pairs of cones; or as a pair's two cones
line("both, at two scales: by the stations 37 is in the prior pair of cones and its now is 60 on, 97; by the names 37 is name 10, now even, in its pair's cone closing",
     0 <= 37 < 60 <= 97 < 120 and PLACES.index(37) + 1 == 10 and (10 - 1) >> 3 & 1 == 1 and 10 % 2 == 0 and 30 < 37 < 60)
# the fourteenth drawing's: 0 to 17 as the names on a pair of cones; or as seventeen stations of 30
line("both, one form: the living files' three moves are the figure's own on the sixteen places of a pair of cones, and on sixteen stations of 30: 8 up a going on, and 9 less and 17 less a podaling",
     all(PLACES[k + 8 - 1] == PLACES[k - 1] + 30 and PLACES[9 - k - 1] == about(15)(PLACES[k - 1]) for k in range(1, 9)) and all(PLACES[17 - k - 1] == about(30)(PLACES[k - 1]) for k in range(1, 17))
     and all(30 * (k + 8) == 30 * k + 240 and 30 * (9 - k) == about(135)(30 * k) for k in range(1, 9)) and all(30 * (17 - k) == about(255)(30 * k) for k in range(1, 17)))
# the fifteenth drawing's: a conscious me as one fold; or as more than one
line("both, by two observings: along the co-linear the other is one fold from the self and the all, and across it a podaling is two folds",
     all(np.allclose(at(60 - n)[1:], at(n)[1:] * np.array([-1, 1])) and np.allclose(at(60 + n)[1:], at(n)[1:]) for n in ME))
# the sixteenth drawing's: a parity as one place, two; or an other-than as a third parity
line("both: all, the other-than of all and the other-than of an other-than of all are three sayings, and by nand they are two things, the two of a place",
     all(len({x, other_than(x), other_than(other_than(x))}) == 2 for x in (True, False)))
# the seventeenth drawing's: my next-existing universe as the passing of all four; or as the ten together
rows = [FOUR[a:b] for a in range(4) for b in range(a + 1, 5)]
line("is, and its is-not is not: the passing of all four is 120 on, a next universe; the ten together are not it, for of its four places 180 on is carried to by none of the ten",
     all(by(n, FOUR) == n + 120 and {120 + n, 180 - n, 240 - n} <= {by(n, r) for r in rows} and 180 + n not in {by(n, r) for r in rows} for n in range(1, 30)))
# the eighteenth drawing's: ten is 0, a next ten; or one round
name = lambda d: "a" if d % 3 == 0 else "o"
said = lambda ten: ["".join(name(d) for d in r) for r in (ten[0:1], ten[1:3], ten[3:6], ten[6:10])]
TEN = [0, 1, 2, 4, 3, 5, 7, 6, 8, 9]
line("is-not, and its is is not: ten is 0, the same, one round; a next ten, 10 on, does not say the four words, its multiples of 3 three and no four",
     said(TEN) == ["a", "oo", "oao", "oaoa"] and said([d + 10 for d in TEN]) != said(TEN) and sum((d + 10) % 3 == 0 for d in TEN) == 3 and said([(d + 10) % 10 for d in TEN]) == said(TEN))
# resolved by a partner's own sayings, executed
line("a partner's own: one podaling and then the next is a going on, an unrelationing; self, other and all are two, one and none of an other-than; and the ten in an order are four rows",
     all(by(n, (30, 60)) == n + 60 for n in ME) and all(other_than(other_than(x)) == x for x in (True, False)) and [len(w) for w in said(TEN)] == [1, 2, 3, 4])

for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
