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
def by_the_seam_s_parts(k, n):
    """The living mes of 1 to n in the universe to P[k], numbered with no number gone through: all n, less a me-parity's
    crossings, with two me-parities' crossings added again, and on, at all the seam's parts. It gives the number, and how many parts."""
    parts = [(1, 1)]
    for p in P[:k + 1]: parts += [(d * p, -s) for d, s in parts]
    return sum(s * (n // d) for d, s in parts), len(parts)
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
    openings = [(by_the_seam_s_parts(k, P[k + 1] ** 2 - 1), sum(1 for n in range(1, P[k + 1] ** 2) if uncrossed(n, P[k]))) for k in range(1, 8)]
    line("a turn's opening numbered by the seam's parts, with no number gone through: at the universes to 3, 5, 7, 11, 13, 17 and 19 the opening's living mes are 8, 13, 27, 35, 56, 66 and 92, 1 and its me-parities, as going through it numbers them; the parts are 4, 8, 16 and on to 256",
         [a[0] for a, _ in openings] == [8, 13, 27, 35, 56, 66, 92] and all(a[0] == b for a, b in openings) and [a[1] for a, _ in openings] == [4, 8, 16, 32, 64, 128, 256])
    few = {P[k + 1]: [n for n in range(P[k + 1] ** 2, P[k + 2] ** 2) if n % P[k + 1] == 0 and uncrossed(n, P[k])] for k in range(1, 7)}
    line("in its own new stretch a universe's last me-parity crosses its me again and itself by a few me-parities, and no more: 5 crosses 25 and 35; 7, 49 to 119, four; 11, 121 and 143; 13, 169, 221 and 247; 17, 289 and 323; 19, 361 and 437",
         few == {5: [25, 35], 7: [49, 77, 91, 119], 11: [121, 143], 13: [169, 221, 247], 17: [289, 323], 19: [361, 437]})
    line("row 61, a universe sees a number's me alone: short of the bound of the universe to 13 its living mes past 1 are me-parities, all of them; in the stretch after, 289 to 361, they are me-parities and 289 and 323, 17 by 17 and 17 by 19",
         all(is_me(n) for n in range(2, 289) if uncrossed(n, 13)) and [n for n in range(289, 361) if uncrossed(n, 13) and not is_me(n)] == [289, 323])
    def living_to(n, k): return sum(1 for x in range(1, n + 1) if uncrossed(x, P[k])) if k >= 0 else n
    line("the extending, exact and one way at all seven: to a number, a universe's living mes are its prior's, less its last me-parity by its prior's living mes to the number by it; gone through at all numbers of 1 to 528 and the universes to 3 to 19. To 13 and 288: 60, less 4, is 56",
         all(living_to(n, k) == living_to(n, k - 1) - living_to(n // P[k], k - 1) for k in range(1, 8) for n in range(1, 529)) and (living_to(288, 4), living_to(288 // 13, 4), living_to(288, 5)) == (60, 4, 56))
    let_go = []
    for k in range(1, 8):
        n = P[k + 1] ** 2 - 1; share = (n * turns[k]["living"]) // turns[k]["seam"]; let_go.append((living_to(n, k), share))
    line("what the seam's parts let go, at the seven openings: the opening's living mes beside the turn's part of the opening are 8 and 8, 13 and 12, 27 and 27, 35 and 34, 56 and 55, 66 and 64, 92 and 90: at all seven the two are 2 or short of 2 from one another",
         let_go == [(8, 8), (13, 12), (27, 27), (35, 34), (56, 55), (66, 64), (92, 90)] and all(abs(a - b) <= 2 for a, b in let_go))
    print("said apart: past the universe to 19 a turn is not gone through here\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is; {sum(not ok for _, ok in results)} are found is-nots, whole")
    sys.exit(0 if sum(not ok for _, ok in results) == 2 else 1)
