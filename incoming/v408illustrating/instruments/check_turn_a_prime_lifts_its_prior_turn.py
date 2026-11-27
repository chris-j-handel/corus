"""v408illustrating · the check of the 46th drawing: Turn, one prime living, a prime lifting its prior turn p ways, with six fixings marked on it once.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_turn_a_prime_lifts_its_prior_turn.py .

The drawing is of the column Turn of v407primes' prime resolving form: its six cells named, a row's fixing a mark on the
one living. The living's numbers are executed here by this check's own lines: a turn's places, a twin place, a turn's
widest gap, a turn's places by its numbers, Euler's 41, and the primes a row of 30. A seat is the page's own placing.
Its is and its is-not are both executed. Whole numbers alone. It opens the page, and writes none. All or none.
"""
import importlib.util, math, os, sys
from fractions import Fraction
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("the_form", os.path.join(HERE, "check_the_prime_resolving_form_one_face.py"))
f = importlib.util.module_from_spec(spec); spec.loader.exec_module(f)

TURNS = (2, 6, 30, 210, 2310, 30030)
places = lambda t: [n for n in range(1, t + 1) if math.gcd(n, t) == 1]          # a turn's places, uncrossed by its primes
twins = lambda t: [n for n in places(t) if math.gcd(n + 2, t) == 1]             # a place with the place 2 on a place too
def widest(t):
    p = places(t); return max(b - a for a, b in zip(p, p[1:] + [p[0] + t]))
prime = lambda n: n > 1 and all(n % d for d in range(2, n) if d * d <= n)      # crossed from a square on, and no root
LIFTED = [[p + 30 * k for p in places(30)] for k in range(7)]                    # the turn of 30's eight places, lifted seven ways

if __name__ == "__main__":
    root = Path(sys.argv[1]); page = (root / f.PAGE).read_text(encoding="utf-8"); rows = f.the_table(page)
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    line("the turns of 2, 6, 30, 210, 2310 and 30030 are with 1, 2, 8, 48, 480 and 5760 places",
         [len(places(t)) for t in TURNS] == [1, 2, 8, 48, 480, 5760])
    flat = [n for r in LIFTED for n in r]
    line("a prime lifts its prior turn p ways, p less 1 uncrossed and one crossed: the turn of 30's eight places lifted seven ways are 56 numbers, eight of them crossed by 7, and 48 the places of the turn of 210",
         len(flat) == 56 and [n for n in flat if n % 7 == 0] == [7, 49, 77, 91, 119, 133, 161, 203] and sorted(n for n in flat if n % 7) == places(210)
         and all(len(places(t * p)) == len(places(t)) * (p - 1) for t, p in zip(TURNS, (3, 5, 7, 11, 13))))
    line("a completing fixing as a last, twins: a prime past 3 lifts a twin place p less 2 ways uncrossed; the twin places of the turns of 6 to 30030 are 1, 3, 15, 135 and 1485, at no turn stepped 0",
         [len(twins(t)) for t in TURNS[1:]] == [1, 3, 15, 135, 1485] == [1, 1 * 3, 3 * 5, 15 * 9, 135 * 11])
    line("a sequencing fixing to one beat, gaps: the gaps of the turn of 30's places are 2, 4 and 6 alone, and a turn's widest gap goes on, 2, 4, 6, 10, 14 and 22: no one beat is at all turns",
         sorted({b - a for a, b in zip(places(30), places(30)[1:] + [31])}) == [2, 4, 6] and [widest(t) for t in TURNS] == [2, 4, 6, 10, 14, 22])
    rates = [Fraction(len(places(t)), t) for t in TURNS]
    line("a rate fixing as a value: a turn's places by its numbers are 1/2, 1/3, 4/15, 8/35, 16/77 and 192/1001, the page's own, less at all turns on, and at no turn one value",
         [str(r) for r in rates] == ["1/2", "1/3", "4/15", "8/35", "16/77", "192/1001"] and "1/2, 1/3, 4/15, 8/35, 16/77, 192/1001" in page and all(a > b for a, b in zip(rates, rates[1:])))
    line("an observing fixing from behind, Euler's 41: n by n and n and 41 is a prime at n of 0 to 39, forty primes, and at 40 it is 41 by 41",
         all(prime(n * n + n + 41) for n in range(40)) and 40 * 40 + 40 + 41 == 41 * 41)
    to = 1_000_020; sieve = bytearray([1]) * (to + 1); sieve[0] = sieve[1] = 0; n = 2
    while n * n <= to:
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, to + 1, n)))
        n += 1
    a_row = sorted({sum(sieve[30 * k + p] for p in places(30)) for k in range(1, to // 30)})
    line("a two-way fixing to one side, random or ordered: a turn's places are podal, a place with the turn less it; and the primes a row of 30 are 0 to 7, stepped to 1,000,000",
         all(t - p in places(t) for t in TURNS[1:4] for p in places(t)) and a_row == list(range(8)))
    turn = [(i + 1, r[0], r[3][0]) for i, r in enumerate(rows) if r[3][0]]
    line("the column Turn is six cells named, at the rows 1, 3, 6, 7, 8 and 9 of the page's table, and two of its interests are not yet resolving by the page: bounded gaps, and Brun",
         [t[0] for t in turn] == [1, 3, 6, 7, 8, 9] and [i for i, r, c, _ in f.NOT_YET if c == "Turn"] == ["bounded gaps", "Brun"])
    line("is-not, said: the parity wall is a naming in the page, and no line here executes it; Brun's adding is a decimal with no last, the page's own saying",
         "the parity wall" in rows[5][3][0] and "Brun's sum is a decimal with no last" in page)
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
