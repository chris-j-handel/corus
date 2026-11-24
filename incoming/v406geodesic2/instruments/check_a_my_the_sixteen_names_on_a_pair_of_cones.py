"""v406geodesic2 · the check of the fourteenth drawing: a my, the sixteen names on a pair of cones, 0 and 17.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_my_the_sixteen_names_on_a_pair_of_cones.py .

A partner's saying of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said:
  my-now-universe is 0, me 1, the me-parities on, to 17, my next universe;
  a my is prior odd, then prior even, then now odd, then now even.
  in my-now-universe all-parity is odd, even, odd.
The candidate laid on the drawing: the names 1 to 16 are the sixteen places of a pair of cones, 0 to 60, in their order;
0 is its vertex, and 17 is 61, a next 1; prior and now are its cone opening and its cone closing, and odd and even a name's own.
Whole numbers alone. It opens the living files and writes none.
All or none: with one line not is, the check is not.
"""
import math, sys
from pathlib import Path

root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
PLACES = [n for n in range(1, 60) if math.gcd(n, 30) == 1]            # the sixteen places of a pair of cones
place = lambda k: PLACES[k - 1]                                        # a name's place
NAMES = range(1, 17)

line("a pair of cones, 0 to 60, is sixteen places no spiral of 2, 3 or 5 crosses, 1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53 and 59: in their order, the names 1 to 16, and name 1 at 1",
     PLACES == [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59] and len(PLACES) == 16 and place(1) == 1)
line("0, the vertex, is before name 1, and 17 is 61, 60 on from 1, a next 1, past the vertex 60: the names go on, name k with 16 at its place with 60",
     0 < place(1) and place(16) < 60 < 61 == place(1) + 60 and math.gcd(61, 30) == 1 and [n for n in range(61, 120) if math.gcd(n, 30) == 1] == [p + 60 for p in PLACES])
line("the living files' three moves on the names are the figure's own on the places: 8 up is 30 on; 9 less, within 1 to 8, is 30 less, a podaling about 15; and 17 less is 60 less, a podaling about 30",
     all(place(k + 8) == place(k) + 30 and place(9 - k) == 30 - place(k) for k in range(1, 9)) and all(place(17 - k) == 60 - place(k) for k in NAMES))
line("9 less and then 17 less is 8 up, as a podaling about 15 and then one about 30 is 30 on, a going on by twice their stations' distance",
     all(17 - (9 - k) == k + 8 and 60 - (30 - place(k)) == place(k) + 30 == place(k + 8) for k in range(1, 9)))
line("the names 1 to 8 are in the cone opening, 0 to 30, a self's span, and 9 to 16 in the cone closing, 30 to 60",
     all(0 < place(k) < 30 for k in range(1, 9)) and all(30 < place(k) < 60 for k in range(9, 17)))

# ---------- a my: prior or now, odd or even ----------
top = lambda k: (k - 1) >> 3 & 1                                       # the top place of a name less one: prior, or now
odd = lambda k: k % 2 == 1
MY = {("prior", "odd"): [1, 3, 5, 7], ("prior", "even"): [2, 4, 6, 8], ("now", "odd"): [9, 11, 13, 15], ("now", "even"): [10, 12, 14, 16]}
line("a my is two is-or-is-nots of a name, prior or now and odd or even: four fours of the sixteen names, in a partner's order prior odd, prior even, now odd, now even",
     all([k for k in NAMES if ("now" if top(k) else "prior") == a and ("odd" if odd(k) else "even") == b] == names for (a, b), names in MY.items())
     and list(MY) == [("prior", "odd"), ("prior", "even"), ("now", "odd"), ("now", "even")])
line("their places: prior odd at 1, 11, 17 and 23; prior even at 7, 13, 19 and 29; now odd at 31, 41, 47 and 53; now even at 37, 43, 49 and 59",
     [[place(k) for k in names] for names in MY.values()] == [[1, 11, 17, 23], [7, 13, 19, 29], [31, 41, 47, 53], [37, 43, 49, 59]])
line("the three moves are the three other-thans of the two: 8 up of prior or now alone, 9 less of odd or even alone, and 17 less of both",
     all(top(k + 8) != top(k) and odd(k + 8) == odd(k) and top(9 - k) == top(k) and odd(9 - k) != odd(k) for k in range(1, 9))
     and all(top(17 - k) != top(k) and odd(17 - k) != odd(k) for k in NAMES))
line("the four places about the pair's widest, 23, 29, 31 and 37, are the names 7, 8, 9 and 10: prior odd, prior even, now odd and now even, a my in its order",
     [place(k) for k in (7, 8, 9, 10)] == [23, 29, 31, 37] and [(("now" if top(k) else "prior"), ("odd" if odd(k) else "even")) for k in (7, 8, 9, 10)] == list(MY))
line("the twelfth drawing's four stations are the same four: station 1 prior odd, 2 prior even, 3 now odd and 4 now even, a station less one in two places",
     [(("now" if (j - 1) >> 1 & 1 else "prior"), ("odd" if j % 2 else "even")) for j in (1, 2, 3, 4)] == list(MY))
about = lambda st: (lambda n: 2 * st - n)
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
line("in a my at the stations, all-parity is odd, even, odd: stations 1, 2 and 3 in a row are one podaling, about station 2, the all itself, at 60; and with the fourth, now even, the four are 120 on, the next universe",
     all(by(n, (30, 60, 90)) == about(60)(n) and by(n, (30, 60, 90, 120)) == n + 120 for n in range(-240, 241)))
SCALES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
line("fourteen of the sixteen places are primes, all but 1 and 49, and thirteen of the fourteen prime scales are among them, all but 5: a self at prime scale 37 is name 10",
     [p for p in PLACES if not prime(p)] == [1, 49] and [p for p in SCALES if p not in PLACES] == [5] and PLACES.index(37) + 1 == 10)

# ---------- word for word, living ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
NI, NUMBERS_FILE = text("Natural_Intelligence_v*.md"), text("Exhibit_THREE_*.md")
quotes = [
    (NI, "8 up, each name with now to its name with next; 17 less, podal within 1 to 16; and 9 less, podal within 1 to 8, two together."),
    (NI, "8 up alone, twice, is 17, a next 1."),
    (NI, "Both podals exchange possibling and observing, 9 less within a self's span, 1 to 8."),
    (NI, "17 less exchanges now and next."),
    (NUMBERS_FILE, "8 up and down, keeping odd or even; 17 less, podal within 1 to 16, exchanging odd and even"),
]
line("five living sentences beside the drawing are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
