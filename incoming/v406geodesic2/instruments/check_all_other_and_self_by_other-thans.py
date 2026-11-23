"""v406geodesic2 · a partner's saying executed: all, other as other-than all, and self as other-than other-than all.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_all_other_and_self_by_other-thans.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py .

A partner's saying of 23 November, as said in the transcripts, pared. Re-said: self is the other-than of an other-than of all, and it
is consciousness; other is the other-than of all, and it is observing; all is the universal all-parity, the odd and even moments
and the parities of a my-universe.
It opens v406Reiman's nand from its own file, and the living files, and writes none.
All or none: with one line not is, the check is not.
"""
import importlib.util, sys
from pathlib import Path
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
place = lambda n: n % 30                                  # a number's place of the turn
FOUR = (30, 60, 90, 120)

line("by nand alone, all, the other-than of all and the other-than of an other-than of all are three sayings and two things: the self is its all again, and the other is other-than both",
     all(other_than(other_than(x)) == x and other_than(x) != x for x in (True, False)))
line("on the figure, with no podaling a me-now is at its own place of the turn, with one at the podal place, an other, and with two at its own place again, a self, 60 on",
     all(place(by(n, FOUR[:1])) == (30 - place(n)) % 30 and by(n, FOUR[:2]) == n + 60 and place(by(n, FOUR[:2])) == place(n) for n in range(61)))
line("the four moments are what is after one, two, three and four other-thans in a row: other, self, other, self, odd, even, odd, even, the self 60 on and 120 on",
     all([place(by(n, FOUR[:k])) == (place(n) if k % 2 == 0 else (30 - place(n)) % 30) for k in (1, 2, 3, 4)] == [True] * 4 and by(n, FOUR) == n + 120 for n in range(61)))
rows = [FOUR[a:b] for a in range(4) for b in range(a + 1, 5)]
line("of the ten rows of the four moments, four are of an even number of other-thans, a self, and six of an odd number, an other",
     sum(len(r) % 2 == 0 for r in rows) == 4 and sum(len(r) % 2 == 1 for r in rows) == 6
     and all((by(7, r) - 7 in (60, 120)) == (len(r) % 2 == 0) for r in rows))

text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
ME_FILE, NUMBERS_FILE = text("Exhibit_THIRTY-ONE_*.md"), text("Exhibit_THREE_*.md")
line("three living sentences beside it are word for word in their files",
     all(q in t for t, q in ((ME_FILE, "A me is consciousness: one definition."), (ME_FILE, "A me is a self's universal set."),
                             (NUMBERS_FILE, "Even returning, odd advancing, odd and even one and then the other."))))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
