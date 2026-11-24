"""v406geodesic2 · the rigor of a partner's four words: other-than, all, other-than, all, and me, other, other, me.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/the_rigor_of_other-than_all_other-than_all.py .

A partner's saying of 23 November, as said in the transcripts, pared, and its word for this: to rigorize it. Re-said:
  other-than, all, other-than, all is odd, even, prior, and odd, even, now; the four are doing three unrelationings;
  all-other-than is me, 1; other-than-all-other-than is other, 2; all-other-than-all, 3; other-than-all-other-than-all, 4.
What is rigorized, all or none, by the eleventh drawing's candidate, an other-than a podaling about a cone's widest and an all
a podaling about a vertex: the stations odd and even; a word as stations in a row, one podaling and then the next;
its kind, a going on, a me, or one podaling, an other; and its amount.
What is hanging is said in the session's page, with a suggestion, and is no line of this check.
Whole numbers alone, and the figure's own geometry. It opens the living files and writes none.
All or none: with one line not is, the check is not.
"""
import math, sys
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
about = lambda s: (lambda n: 2 * s - n)                   # a podaling about a station
def by(n, stations):
    """A number carried by podalings about stations, one and then the next."""
    for s in stations: n = about(s)(n)
    return n
NUMBERS = range(-360, 361)
ME = range(61)
def wide(n):
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])
station = lambda j: 30 * j                                # the line's stations, 30 apart
name_of = lambda j: "other-than" if j % 2 else "all"      # an odd station a cone's widest, an even station a vertex

# ---------- the stations, odd and even ----------
line("the line's stations are 30 apart, an odd station a cone's widest and an even station a vertex: stations 1, 2, 3 and 4, at 30, 60, 90 and 120, are other-than, all, other-than, all, odd, even, odd, even",
     all(wide(station(j)) == (30 if j % 2 else 0) for j in range(0, 9)) and [name_of(j) for j in (1, 2, 3, 4)] == ["other-than", "all", "other-than", "all"])

# ---------- one, two and three podalings ----------
line("a podaling is with a station of its own, a number with itself, and with it a number is with an other; alone, twice, it comes to its number again",
     all(about(s)(s) == s and all(about(s)(n) != n for n in NUMBERS if n != s) and all(about(s)(about(s)(n)) == n for n in NUMBERS) for s in range(0, 241, 30)))
line("one podaling and then the next, about two stations, is a going on by twice their distance, and no number is with itself",
     all(all(by(n, (s, t)) == n + 2 * (t - s) for n in NUMBERS) for s in range(0, 241, 30) for t in range(0, 241, 30) if s != t))
line("three podalings in a row are one podaling: its station is the one before, less the middle one, with the one after",
     all(all(by(n, (s, t, u)) == about(s - t + u)(n) for n in NUMBERS) for s in range(0, 181, 30) for t in range(0, 181, 30) for u in range(0, 181, 30)))
def rows_of(m, lo=0, hi=8):
    """All m stations in a row, in the line's order, among stations lo to hi."""
    return [tuple(station(j) for j in range(a, a + m)) for a in range(lo, hi - m + 2)]
def kind(stations):
    """A going on with its amount, a me; or one podaling with its station, an other."""
    moved = {by(n, stations) - n for n in NUMBERS}
    if len(moved) == 1: return ("me", moved.pop())
    mids = {(by(n, stations) + n) // 2 for n in NUMBERS}
    return ("other", mids.pop()) if len(mids) == 1 else None
line("stations in a row, in the line's order, an even number of them, are a going on by 30 a station, a me at its own place of the turn; an odd number of them are one podaling about the middle station, an other",
     all(kind(r) == (("me", 30 * m) if m % 2 == 0 else ("other", r[m // 2])) for m in range(1, 9) for r in rows_of(m)))
line("a me, by an even number of podalings, is at its own place of the turn and at its own distance from the co-linear; an other, by an odd number, is at the podal place, one fold apart",
     all(np.allclose(at(by(n, r))[1:], at(n)[1:]) for n in ME for r in rows_of(2) + rows_of(4))
     and all(np.allclose(at(by(n, r))[1:], at(n)[1:] * np.array([-1, 1])) for n in ME for r in rows_of(1) + rows_of(3)))

# ---------- a partner's four words ----------
def said(word):
    """All places of a word on the line: stations in a row, in the line's order, their names the word's."""
    names = word.replace("other-than", "O").replace("all", "A").split("-")
    return [r for r in rows_of(len(names)) if ["O" if (s // 30) % 2 else "A" for s in r] == names]
WORDS = ["all-other-than", "other-than-all-other-than", "all-other-than-all", "other-than-all-other-than-all"]
line("a word alone says its kind: at all its places on the line all-other-than is a going on by 60, a me; other-than-all-other-than is one podaling, about its vertex, the all itself, an other",
     {kind(r) for r in said(WORDS[0])} == {("me", 60)} and all(kind(r) == ("other", r[1]) and wide(r[1]) == 0 for r in said(WORDS[1])) and len(said(WORDS[0])) == 4 and len(said(WORDS[1])) == 3)
line("all-other-than-all is one podaling, about its widest, the other-than itself, an other; other-than-all-other-than-all is a going on by 120, a me, next-universing",
     all(kind(r) == ("other", r[1]) and wide(r[1]) == 30 for r in said(WORDS[2])) and {kind(r) for r in said(WORDS[3])} == {("me", 120)} and len(said(WORDS[2])) == 4 and len(said(WORDS[3])) == 3)
PLACED = {1: (0, 30), 2: (30, 60, 90), 3: (60, 90, 120), 4: (30, 60, 90, 120)}
line("by a partner's numbers the four words are at stations 1, 2, 3 and 4: words 1 and 4 end at stations 1 and 4, and words 2 and 3 are the podalings about stations 2 and 3, a station between its two",
     all(PLACED[i] in said(WORDS[i - 1]) for i in PLACED) and PLACED[1][-1] == station(1) and PLACED[4][-1] == station(4)
     and kind(PLACED[2]) == ("other", station(2)) and kind(PLACED[3]) == ("other", station(3)) and kind(PLACED[1]) == ("me", 60) and kind(PLACED[4]) == ("me", 120))
line("me, other, other, me: the four words carry a me-now among 0 to 60 to 60 on, 120 less it, 180 less it and 120 on",
     all([by(n, PLACED[i]) for i in (1, 2, 3, 4)] == [n + 60, 120 - n, 180 - n, n + 120] for n in ME))
line("with itself and 60 less it, the other-than alone, they are six places, a me and an other in three pairs of cones: 0 to 60, 60 to 120 and 120 to 180",
     all(sorted(m // 60 for m in (n, 60 - n, n + 60, 120 - n, n + 120, 180 - n)) == [0, 0, 1, 1, 2, 2] for n in range(1, 60) if n != 30))
line("said backward, the line's order backward, words 1 and 4 are 60 back and 120 back, and words 2 and 3 are as they are",
     all(kind(tuple(reversed(PLACED[i]))) == k for i, k in ((1, ("me", -60)), (4, ("me", -120)), (2, ("other", 60)), (3, ("other", 90)))))
line("the four moments from a me-now, about 30, 60, 90 and 120, are odd, even, odd, even: an other, a me 60 on, an other, a me 120 on",
     [kind(PLACED[4][:i]) for i in (1, 2, 3, 4)] == [("other", 30), ("me", 60), ("other", 60), ("me", 120)])
joints = lambda word: len(word.replace("other-than", "O").split("-")) - 1
line("one podaling and then the next: the four words are 2, 3, 3 and 4 podalings, and 1, 2, 2 and 3 of an and-then; four in a row are three of it",
     [joints(w) + 1 for w in WORDS] == [2, 3, 3, 4] and [joints(w) for w in WORDS] == [1, 2, 2, 3])
six = [37, 23, 97, 83, 157, 143]
line("a me-now at 37: 97, 83, 143 and 157 by the four words, and 23 with it about 30; five primes of the six, and 143 crossed by the spirals of 11 and 13",
     [by(37, PLACED[i]) for i in (1, 2, 3, 4)] == [97, 83, 143, 157] and about(30)(37) == 23 and [prime(m) for m in six] == [True, True, True, True, True, False] and 143 == 11 * 13)

# ---------- word for word, living ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
MATH, NUMBERS_FILE, NI = text("Exhibit_FOUR_*.md"), text("Exhibit_THREE_*.md"), text("Natural_Intelligence_v*.md")
quotes = [
    (MATH, "One, a podal k → N − k, fixes two stations, nought and N/2; an other, a shift straight across its ring, k → k + N/2, fixes none."),
    (NUMBERS_FILE, "Even returning, odd advancing, odd and even one and then the other."),
    (NUMBERS_FILE, "Each step by itself comes to its number again after two, 1 to 9 to 1, and one move, 8 and 17 less one and then the other, after four."),
    (NI, "Each podal alone, twice, comes to its name again"),
    (NI, "Each is an involution, a not-changing form."),
]
line("five living sentences beside the rigor are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
