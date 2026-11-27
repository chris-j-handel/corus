"""v408illustrating · the check of the 43rd drawing: the six and the ten round 30, a number at its place round 6 and its place round 10.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/check_the_six_and_the_ten_round_30.py .

The drawing is of v408primes' page for illustrating, incoming/v408primes/for_illustrating/the_six_and_the_ten_round_30.csv:
all numbers round 30 with a place round 6 and a place round 10, uncrossed or not, a prime or not, and its podal.
Its numbers are executed here by this check's own lines, and are v408primes' rows, a row for a row: opened from its branch
at b491784 on 25 November, all thirty rows the same; and opened here again from the set once its folder is in main.
Whole numbers alone. It writes none. All or none: with one line not is, the check is not.
"""
import csv, math, sys
from pathlib import Path

def the_thirty():
    """A number round 30: its place round 6, its place round 10, uncrossed by 2, 3 and 5, a prime, and its podal."""
    prime = lambda n: n > 1 and all(n % p for p in range(2, n))
    return [(n, n % 6, n % 10, math.gcd(n, 30) == 1, prime(n), (30 - n) % 30) for n in range(30)]

if __name__ == "__main__":
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    rows = the_thirty()
    cells = {(a, b): n for n, a, b, *_ in rows}

    line("thirty numbers, 0 to 29, are at thirty cells of a table of six by ten, one for one: a number at its place round 6 and its place round 10",
         len(cells) == 30)
    line("of the table's sixty cells the thirty reached are with both places odd or both even, and the thirty more, one place odd and one even, are open cells",
         set(cells) == {(a, b) for a in range(6) for b in range(10) if (a - b) % 2 == 0})
    line("+1 is one place on round 6 and one place on round 10, and 30 is the turn of the two together: the steps reach 0 again with 30, and with no number below it",
         all(((a + 1) % 6, (b + 1) % 10) == (rows[(n + 1) % 30][1], rows[(n + 1) % 30][2]) for n, a, b, *_ in rows) and [k for k in range(1, 31) if k % 6 == 0 and k % 10 == 0] == [30])
    eight = [n for n, a, b, open_, *_ in rows if open_]
    line("the eight uncrossed by 2, 3 and 5 are two columns by four rows: the places 1 and 5 round 6 by the places 1, 3, 7 and 9 round 10, all eight cells reached",
         eight == [1, 7, 11, 13, 17, 19, 23, 29] and {(n % 6, n % 10) for n in eight} == {(a, b) for a in (1, 5) for b in (1, 3, 7, 9)})
    primes = [n for n, *_, p, _ in rows if p]
    line("the primes below 30 are ten: 2, 3 and 5, and the eight less 1",
         primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] and primes[3:] == eight[1:])
    line("podal round 30 is podal round 6 and round 10 both, a place with its turn less it; the eight are four podal pairs, 1 with 29, 7 with 23, 11 with 19 and 13 with 17",
         all(((6 - a) % 6, (10 - b) % 10) == (rows[q][1], rows[q][2]) for n, a, b, _, _, q in rows) and sorted({tuple(sorted((n, 30 - n))) for n in eight}) == [(1, 29), (7, 23), (11, 19), (13, 17)])
    reach = lambda w, h: len({(n % w, n % h) for n in range(30)})
    line("is-not, explored: a table of six by five, and one of three by ten, are thirty cells all reached; the table of six by ten alone is with open cells, thirty of its sixty",
         (reach(6, 5), reach(3, 10), reach(6, 10)) == (30, 30, 30) and (6 * 5, 3 * 10, 6 * 10) == (30, 30, 60))
    page = root / "incoming/v408primes/for_illustrating/the_six_and_the_ten_round_30.csv"
    if page.exists():
        theirs = list(csv.reader(open(page, encoding="utf-8")))[1:]
        line("v408primes' page for illustrating is these thirty rows, a row for a row",
             [(int(r[0]), int(r[1]), int(r[2]), r[3] == "yes", r[4] == "yes", int(r[5])) for r in theirs] == rows)
    else:
        print("said apart: v408primes' page is not in the set at this main; opened from its branch at b491784, its thirty rows are these, a row for a row\n")

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
