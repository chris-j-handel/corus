"""v408illustrating · the check of the 45th drawing: two primes are a torus, the +1 winding through all their places.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/check_two_primes_are_a_torus.py .

The drawing is of v408primes' sentence 41, the one it goes on with ahead of all others, said at the exchange on 25 November:
two primes are a torus, the +1 winding through all their places, p one way and q the other, and again at their turn.
Drawn with 5 and 7, and stepped here with all pairs of primes below 100. Beside the 43rd drawing, the six and the ten.
Its is and its is-not are both executed. Whole numbers alone. It writes none. All or none.
"""
import itertools, sys
from pathlib import Path

def the_torus(p, q):
    """The +1 from 0, a number at its place round p and its place round q, until its two places are 0 and 0 again."""
    cells, n = {}, 0
    while True:
        cells.setdefault((n % p, n % q), n); n += 1
        if (n % p, n % q) == (0, 0): return cells, n
prime = lambda n: n > 1 and all(n % d for d in range(2, n))

if __name__ == "__main__":
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    cells, again = the_torus(5, 7)
    line("5 and 7: the +1 winds through all their places, thirty-five numbers at thirty-five cells, one for one, and is at 0 and 0 again at 35, their turn, and at no number below it",
         len(cells) == 35 == again and sorted(cells.values()) == list(range(35)))
    line("in one turn the +1 goes round the 5 seven times and round the 7 five times: p one way and q the other", (again // 5, again // 7) == (7, 5))
    primes = [n for n in range(2, 100) if prime(n)]
    line("stepped with all pairs of two primes below 100, three hundred pairs: p by q cells, all reached, and the +1 again at p by q alone",
         all((len(c), t) == (p * q, p * q) for p, q in itertools.combinations(primes, 2) for c, t in [the_torus(p, q)]) and len(list(itertools.combinations(primes, 2))) == 300)
    by5 = [n for (a, b), n in cells.items() if a == 0]; by7 = [n for (a, b), n in cells.items() if b == 0]
    line("its two primes are its two directions: the numbers crossed by 5 are one line of seven cells, the numbers crossed by 7 one line of five, 0 at both; the cells of neither line are 24, four by six",
         sorted(by5) == list(range(0, 35, 5)) and sorted(by7) == list(range(0, 35, 7)) and len([1 for (a, b) in cells if a and b]) == 24 == 4 * 6)
    line("podal round 35 is podal round 5 and round 7 both: a number with its turn less it, a place with its turn less it",
         all(cells[((5 - a) % 5, (7 - b) % 7)] == (35 - n) % 35 for (a, b), n in cells.items()))
    line("beside the 43rd drawing: the six is the torus of 2 and 3 and the ten the torus of 2 and 5, all their cells reached; 6 and 10 are with 2 in both, and the +1 reaches thirty of their sixty",
         [len(the_torus(*x)[0]) for x in ((2, 3), (2, 5), (6, 10))] == [6, 10, 30])
    line("is-not, explored: a prime with itself is no torus of two: with 5 and 5 the +1 reaches five of twenty-five cells, and is again at 5",
         (len(the_torus(5, 5)[0]), the_torus(5, 5)[1]) == (5, 5))
    below = [n for n in range(30) if prime(n)]
    line("v408primes' saying, executed apart: the ten primes of the turn of 30 are 3 and 6 and 1: 2, 3 and 5; three podal pairs, 7 with 23, 11 with 19 and 13 with 17; and 29, the turn less 1; 209, the turn of 210 less 1, is 11 by 19",
         below[:3] == [2, 3, 5] and [(n, 30 - n) for n in below if 5 < n < 15] == [(7, 23), (11, 19), (13, 17)] and all(prime(30 - n) for n in (7, 11, 13)) and below[-1] == 29 and 209 == 11 * 19)
    form = (root / "incoming/v407primes/The_prime_resolving_form.md").read_text(encoding="utf-8")
    line("the form's column of it is in v407primes' page, word for word: two primes' spirals locking as one torus", "two primes' spirals locking as one torus" in form)
    page = root / "incoming/v408primes/The_co-chain_of_v408primes_from_source_to_destiny.md"
    S41 = "Two primes are a **torus**: the +1 winds through all their places, p one way and q the other, and comes again at their turn."
    if page.exists(): line("v408primes' sentence 41 is in its co-chain, word for word", S41 in page.read_text(encoding="utf-8"))
    else: print("said apart: v408primes' co-chain is not in the set at this main; opened from its branch at b491784, its sentence 41 is word for word\n")

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
