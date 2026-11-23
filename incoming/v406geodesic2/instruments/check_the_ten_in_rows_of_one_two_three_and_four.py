"""v406geodesic2 · a partner's saying executed: the ten, 0124357689, in rows of one, two, three and four.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_ten_in_rows_of_one_two_three_and_four.py .

A partner's saying of 23 November, as said in the transcripts, pared. Re-said: 1 by 3 and 2 by 3 are 9, and ten is 0, the same; and
the ten in an order, 0, 1, 2, 4, 3, 5, 7, 6, 8, 9.
The candidate executed: a multiple of 3 is an all and a number other-than one an other-than; the ten in a partner's order, in rows
of one, two, three and four, are four words of a partner's sayings before it.
Whole numbers alone. It opens no file and writes none. All or none: with one line not is, the check is not.
"""
import sys
results = []
def line(name, ok): results.append((name, bool(ok)))
about = lambda st: (lambda n: 2 * st - n)
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
TEN = [0, 1, 2, 4, 3, 5, 7, 6, 8, 9]
name = lambda d: "all" if d % 3 == 0 else "other-than"
rows = [TEN[0:1], TEN[1:3], TEN[3:6], TEN[6:10]]
line("a partner's ten are the ten numbers 0 to 9, one of a kind, and in rows of one, two, three and four they are 0; 1, 2; 4, 3, 5; and 7, 6, 8, 9",
     sorted(TEN) == list(range(10)) and rows == [[0], [1, 2], [4, 3, 5], [7, 6, 8, 9]])
line("the multiples of 3 among them are four, 0, 1 by 3, 2 by 3 and 9, and the others six: as of the ten rows of the four moments four are a self and six an other",
     [d for d in range(10) if d % 3 == 0] == [0, 1 * 3, 2 * 3, 9] and sum(d % 3 != 0 for d in TEN) == 6 and 1 * 3 + 2 * 3 == 9)
words = ["-".join(name(d) for d in r) for r in rows]
line("with a multiple of 3 an all, the four rows say: all; other-than, other-than; other-than, all, other-than; and other-than, all, other-than, all",
     words == ["all", "other-than-other-than", "other-than-all-other-than", "other-than-all-other-than-all"])
line("they are four words of a partner's sayings before it: the all; the self's two other-thans of all; all-parity, odd, even, odd; and the four moments, a my",
     words[2] == "other-than-all-other-than" and words[3] == "other-than-all-other-than-all" and [len(r) for r in rows] == [1, 2, 3, 4] and sum(len(r) for r in rows) == 10)
line("on the figure, the row of three is one podaling about 60, the all itself, and the row of four is 120 on, a next universe; the row of two, two other-thans, is a self again",
     all(by(n, (30, 60, 90)) == about(60)(n) and by(n, (30, 60, 90, 120)) == n + 120 and (by(n, (30, 90)) - n) % 30 == 0 for n in range(61)))
threes = [TEN[0:3], TEN[3:6], TEN[6:9], TEN[9:]]
line("in threes the all is ahead of two other-thans, in 0, 1, 2; between them, in 4, 3, 5 and in 7, 6, 8; and by itself, 9: with 7, 8, 6 it is after them, a partner's three words of the eleventh drawing",
     [[name(d)[0] for d in t] for t in threes] == [["a", "o", "o"], ["o", "a", "o"], ["o", "a", "o"], ["a"]] and [name(d)[0] for d in (7, 8, 6)] == ["o", "o", "a"])
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
