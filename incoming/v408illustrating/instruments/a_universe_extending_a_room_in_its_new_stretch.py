"""v408illustrating · a universe extending, and a room in its new stretch: rows 28, 29, 31 and 36 of v408primes' table in one frame.

Usage, from the repository's root (about half a minute):
  python3 -I incoming/v408illustrating/instruments/a_universe_extending_a_room_in_its_new_stretch.py .

A partner's saying of 26 November, in this session's words: one thing; a universe extends; in it me-parities find each
other in bi-couplings; traveling to them, it extends to new bi-couplings; the same thing at all extendings.
A universe to r is the me-parities to r, and the path of their seam. Its bound is the next me-parity's me again: short
of it, a number past 1 uncrossed by the universe is a me-parity, by the side. A living me is a me uncrossed by the
universe; a room is a between with both its sides living. Its new stretch is from its prior bound, r by r, to its own.
Small numbers: the universes to 19, their turns gone through whole. Its lines are of the 55th's kinds:
  is       a path closing, gone through whole; or all the numbers of a bound gone through.
  is-not   a found number, whole.
Whole numbers alone. It writes none.
"""
import sys

P = [2, 3, 5, 7, 11, 13, 17, 19, 23]
def is_me(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def a_turn(k):
    """The universe to P[k], its turn gone through whole: its seam, its living mes, its rooms, and the widest from one to its next."""
    seam = 1
    for p in P[:k + 1]: seam *= p
    live = bytearray([1]) * seam
    for p in P[:k + 1]: live[0::p] = bytearray(len(range(0, seam, p)))
    mes = [a for a in range(seam) if live[a]]
    rooms = [m for m in range(seam) if live[m - 1] and live[(m + 1) % seam]]
    widest = lambda xs: max(b - a for a, b in zip(xs, xs[1:] + [xs[0] + seam]))
    return dict(r=P[k], q=P[k + 1], seam=seam, living=len(mes), rooms=len(rooms), run=widest(mes), gap=widest(rooms))
def uncrossed(n, r): return all(n % p for p in P if p <= r)
def rooms_in_the_new_stretch(k):
    r, q = P[k], P[k + 1]
    return [m for m in range(r * r + 1, q * q - 1) if uncrossed(m - 1, r) and uncrossed(m + 1, r)]

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    turns = [a_turn(k) for k in range(8)]
    line("the extending, one thing at all eight: a turn's living mes are its prior's by r less 1, and its rooms its prior's by r less 2, past the universe to 2: 1, 2, 8, 48 and on living; 1, 1, 3, 15, 135 and on rooms",
         [t["living"] for t in turns[:4]] == [1, 2, 8, 48] and [t["rooms"] for t in turns[:5]] == [1, 1, 3, 15, 135] and all(b["living"] == a["living"] * (b["r"] - 1) and b["rooms"] == a["rooms"] * (b["r"] - 2) for a, b in zip(turns[1:], turns[2:])))
    stretches = [rooms_in_the_new_stretch(k) for k in range(8)]
    line("short of its bound a room is a bi-coupling: at the eight universes to 19, all rooms in the new stretch are two me-parities about a between; 6; 12 and 18; 30 and 42; 60, 72, 102 and 108; 138 and 150",
         stretches[:5] == [[6], [12, 18], [30, 42], [60, 72, 102, 108], [138, 150]] and all(is_me(m - 1) and is_me(m + 1) for s in stretches for m in s) and all(s for s in stretches))
    line("row 29, by the path alone, at the eight universes to 19: the widest from a living me to its next, 2, 4, 6, 10, 14, 22, 26 and 34, is short of the stretch from a me again to its next past the universe's last, twice it and 1: a me-parity is between a me again and its next, at all me agains of 1 to 22",
         [t["run"] for t in turns] == [2, 4, 6, 10, 14, 22, 26, 34] and all(t["run"] <= 2 * t["r"] for t in turns) and all(any(is_me(x) for x in range(n * n + 1, (n + 1) * (n + 1))) for n in range(1, 23)))
    by_path = [t["r"] for t in turns if t["gap"] <= t["q"] ** 2 - t["r"] ** 2 - 2]
    line("row 31, by the path alone, at seven of the eight: the widest from a room to its next, 2, 6, 12, 30, 42, 66 and 150, is short of the new stretch at the universes to 2, 3, 5, 7, 11, 13 and 19: a new bi-coupling is in the new stretch",
         [t["gap"] for t in turns] == [2, 6, 12, 30, 42, 66, 108, 150] and by_path == [2, 3, 5, 7, 11, 13, 19])
    results.append(("found, a whole is-not of the path alone: at the universe to 17 the widest from a room to its next is 108, and its new stretch, 289 to 361, is 72; the rooms 312 and 348 are in it, gone through, and the path's widest does not say them",
                    not (turns[6]["gap"] == 108 and 361 - 289 == 72 and stretches[6] == [312, 348])))
    line("row 36, the bound of the universe to 19 gone through: about all betweens of 2 to 264, two me-parities face one another, the between's selves from it at both its sides",
         all(any(is_me(n - d) and is_me(n + d) for d in range(0, n - 1)) for n in range(2, 265)) and 2 * 264 < 23 * 23)
    results.append(("found, a whole is-not of row 28 at all new stretches: at the universe to 11 the me agains of 11 and of 12, and 1, are 122 and 145, 2 by 61 and 5 by 29: no me-parity one past a me again is in that stretch",
                    not (11 * 11 + 1 == 122 == 2 * 61 and 12 * 12 + 1 == 145 == 5 * 29 and [n for n in range(11, 13) if is_me(n * n + 1)] == [])))
    print("said apart: past the universe to 19 a turn is not gone through here\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is; {sum(not ok for _, ok in results)} are found is-nots, whole")
    sys.exit(0 if sum(not ok for _, ok in results) == 2 else 1)
