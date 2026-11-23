"""v406geodesic2 · the check of the eighth drawing: the cube of 5, five selves on its line and 120 about it.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_cube_of_5_and_its_line.py .

The candidate laid on the drawing, beside the seventh drawing's rounds:
  the cube of 5, its selves the places of 0 to 4 three ways, from the corus, in the one triangle's own eighth;
  its shells 1, 7, 19, 37 and 61, a shell the selves of one greatest way, and their five corners its line, along (1, 1, 1);
  the 120 about the line as 1 to 120, round after round from the line, the line a 0.
Whole numbers alone, and the figure's own geometry. It opens the living files and writes none.
All or none: with one line not is, the check is not.
"""
import itertools, math, sys
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))

# ---------- the cube of 5, its shells and its line ----------
cube = lambda N: list(itertools.product(range(N), repeat=3))
selves = cube(5)
shell = lambda k: [p for p in selves if max(p) == k]
line("the cube of 5 is 125 selves, the shells 1, 7, 19, 37 and 61, a shell the selves of one greatest way, a cube of n + 1 less a cube of n",
     len(selves) == 125 and [len(shell(k)) for k in range(5)] == [1, 7, 19, 37, 61] == [(k + 1) ** 3 - k ** 3 for k in range(5)])
line("a shell is about the cube before it: a cube of n and its shell are the cube of n + 1, with n of 1 to 4",
     all(set(cube(k)) | {p for p in selves if max(p) == k} == set(cube(k + 1)) for k in range(1, 5)))
on_the_line = [p for p in selves if min(p) == max(p)]
line("the five shells' corners, the corus and four more, are one line along (1, 1, 1), a step a shell, and no other self of the cube is on it",
     on_the_line == [(k, k, k) for k in range(5)] and all(max(shell(k), key=sum) == (k, k, k) for k in range(5)))
about = [p for p in selves if min(p) != max(p)]
by_shell = [sum(1 for p in about if max(p) == k) for k in range(1, 5)]
by_round = [sum(1 for p in about if max(p) - min(p) == r) for r in range(1, 5)]
added_up = lambda xs: [sum(xs[:i + 1]) for i in range(len(xs))]
line("about the line are 120 selves; by shells they are 6, 18, 36 and 60: to 6, to 24, to 60 and to 120",
     len(about) == 120 and by_shell == [6, 18, 36, 60] and added_up(by_shell) == [6, 24, 60, 120])
line("by rounds about the line they are 24, 36, 36 and 24: to 24, to 60, to 96 and to 120", by_round == [24, 36, 36, 24] and added_up(by_round) == [24, 60, 96, 120])
line("a cube of 2, of 3, of 4 and of 5 is 2, 3, 4 and 5 selves on its line and 6, 24, 60 and 120 about it, a number with its prior and its next multiplied",
     [sum(1 for p in cube(N) if min(p) == max(p)) for N in (2, 3, 4, 5)] == [2, 3, 4, 5]
     and [sum(1 for p in cube(N) if min(p) != max(p)) for N in (2, 3, 4, 5)] == [6, 24, 60, 120] == [(N - 1) * N * (N + 1) for N in (2, 3, 4, 5)])
line("a cube is its selves about its line and its line: 27 is 24 and 3, 64 is 60 and 4, and 125 is 120 and 5",
     [(N ** 3, (N - 1) * N * (N + 1), N) for N in (3, 4, 5)] == [(27, 24, 3), (64, 60, 4), (125, 120, 5)] and all(N ** 3 == (N - 1) * N * (N + 1) + N for N in range(1, 1000)))

# ---------- observed along its line ----------
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
right = np.array([-1.0, 1.0, 0]) / np.sqrt(2); up = np.array([-1.0, -1.0, 2.0]) / np.sqrt(6)
observed = lambda v: np.array([v @ right, v @ up]); unit = lambda p: p / np.linalg.norm(p)
RAY = {6: unit(observed(A)), 1: unit(observed(-C)), 2: unit(observed(B)), 3: unit(observed(-A)), 4: unit(observed(C)), 5: unit(observed(-B))}
ray_of = lambda k: RAY[6 if k % 6 == 0 else k % 6]
def round_of(m):
    n = 0
    while 3 * n * (n + 1) < m: n += 1
    return n
def place(m):
    if m == 0: return np.zeros(2)
    n = round_of(m); j = m - 3 * n * (n - 1); side, step = divmod(j, n)
    if step == 0: side, step = side - 1, n
    return n * ray_of(side) + step * ray_of(side + 2)
e = [unit(observed(B)), unit(observed(C)), unit(observed(A))]
seen = lambda p: tuple(np.round(sum(c * v for c, v in zip(p, e)), 9) + 0.0)
under = {}
for p in selves: under.setdefault(seen(p), []).append(p)
seventh = {tuple(np.round(place(m), 9) + 0.0): m for m in range(61)}
line("observed along its line the cube of 5 is the hexagon of 61, the seventh drawing's 0 to 60, a place for a place", set(under) == set(seventh))
line("a place of round r is 5 less r selves deep, 5, 4, 3, 2 and 1, the selves under it a step apart along the line",
     all(len(ps) == 5 - round_of(seventh[q]) for q, ps in under.items())
     and all(tuple(np.subtract(b, a)) == (1, 1, 1) for ps in under.values() for a, b in zip(sorted(ps), sorted(ps)[1:])))
line("about the line the 120 are ten turns: four of 6, three of 12, two of 18 and one of 24",
     [(5 - r, 6 * r) for r in range(1, 5)] == [(4, 6), (3, 12), (2, 18), (1, 24)] and sum(5 - r for r in range(1, 5)) == 10 and sum((5 - r) * 6 * r for r in range(1, 5)) == 120)
line("with the hexagon of 37's corners at the six intersections, the shell of 37's three far corners are B, C and A, and the line is through the one triangle's centre, between the corners of the shells of 7 and of 19",
     all(np.allclose(np.array(p) / 3, v) for p, v in (((3, 0, 0), B), ((0, 3, 0), C), ((0, 0, 3), A)))
     and np.allclose(unit(A + B + C), unit(np.array([1.0, 1.0, 1.0]))) and np.linalg.norm(np.array([1, 1, 1]) / 3) < 1 < np.linalg.norm(np.array([2, 2, 2]) / 3))

# ---------- 0 to 120 by the four rounds, its primes and their podaling ----------
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
ends = [0] + added_up(by_round)
line("0 to 120 by the four rounds is podal about 60: its ends 0, 24, 60, 96 and 120 are 120 less one another, 24 with 96 and 60 with itself",
     ends == [0, 24, 60, 96, 120] and [120 - x for x in ends] == ends[::-1])
spans = [range(ends[i] + 1, ends[i + 1] + 1) for i in range(4)]
primes = [[m for m in s if prime(m)] for s in spans]
line("its primes by the four rounds are nine, eight, seven and six: 2 to 23, 29 to 59, 61 to 89 and 97 to 113",
     [len(x) for x in primes] == [9, 8, 7, 6] and [(x[0], x[-1]) for x in primes] == [(2, 23), (29, 59), (61, 89), (97, 113)])
podal = [[m for m in x if prime(120 - m)] for x in primes]
more = [[m for m in x if not prime(120 - m)] for x in primes]
line("six primes of a round are podal with a prime, the innermost round's with the outermost's and the two between with one another; and 3, 2, 1 and none more",
     [len(x) for x in podal] == [6, 6, 6, 6] and [120 - m for m in podal[0]] == podal[3][::-1] and [120 - m for m in podal[1]] == podal[2][::-1]
     and [len(x) for x in more] == [3, 2, 1, 0])
line("the more are 2, 3 and 5, the spirals of 120 itself, 2 by 2 by 2 by 3 by 5; 29 and 43, their podals 91 and 77, 7 by 13 and 7 by 11; and 71, its podal 49, 7 by 7",
     more == [[2, 3, 5], [29, 43], [71], []] and 2 * 2 * 2 * 3 * 5 == 120 and (120 - 29, 120 - 43, 120 - 71) == (7 * 13, 7 * 11, 7 * 7))
line("by shells 0 to 120 is to 6, to 24, to 60 and to 120: 60, the waist, is the cube of 4 whole, and the shell of 61 is its corner and the returning, 61 to 120",
     added_up(by_shell)[2] == 60 == sum(1 for p in cube(4) if min(p) != max(p)) and by_shell[3] == 60 and len(shell(4)) == 61)

# ---------- word for word, living ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
NUMBERS, THIRTY = text("Exhibit_THREE_*.md"), text("Exhibit_THIRTY_Co-*.md")
quotes = [
    (NUMBERS, "Primes part about twenty-four as nine behind and eight ahead"),
    (NUMBERS, "Behind its waist a span is twenty-four long and has nine primes; ahead it is thirty-six long and has eight"),
    (NUMBERS, "twenty-four is an apex of nought to sixty's bi-folding"),
    (NUMBERS, "Sixty parts as twenty-four and thirty-six with a five-fold too"),
    (NUMBERS, "sixty is a waist of a ring of one hundred twenty, its own far side"),
    (NUMBERS, "Twenty-four, twenty-seven and thirty-two pair on that ring with ninety-six, ninety-three and eighty-eight"),
    (NUMBERS, "From a self's own corus to a surface its going is one line"),
    (NUMBERS, "Twenty-three a vertex, twenty-five a centre of a face and fifty-nine a surface are on one line, a position, a scale and an orientation"),
    (NUMBERS, "Primes go from two to fifty-nine and return from sixty-one to one hundred eighteen"),
    (NUMBERS, "Twenty-seven, three cubed, on a route 24 → 27 → 32 from a seam"),
    (NUMBERS, "past fifty-nine sixty to sixty-eight are four moments across sixty-four"),
    (NUMBERS, "115 = 5 × 23 with 125 = 5³"),
    (THIRTY, "A right-hand turn of 120 degrees about a line from a corus along (1, 1, 1)"),
]
line("thirteen living sentences beside the drawing are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
