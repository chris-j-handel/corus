"""v410illustrating · the opening figure by its own moves: all even, and no prime's own round in it.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_opening_figure_by_its_own_moves_all_even_and_no_prime_s_own_round.py .

A partner's saying of 27 November, as this session is with it: a sphere opening to a torus is known mathematics; its
between is all even parity and no odd parity; the primes are on it as existing things, and no method of a prime's
existing is in it. This instrument executes that saying at the 57th drawing's figure, by the figure's own moves.

Do no harm: it opens Exhibit ONE, v403mgr's one table of the seventeen names and this session's own 57th drawing,
and writes in no file. It executes no code of the resolver: Exhibit ONE's tables of mes are opened as the living file
lays them.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import csv, html, itertools, re, sys
from collections import Counter
from math import gcd
from pathlib import Path

MINE = "incoming/v410illustrating/"

def lcm(a, b): return a * b // gcd(a, b)
def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def period(move):
    """a move is a tuple, i onto move[i]: the number of its doings to all as they were"""
    seen, out = set(), 1
    for i in range(len(move)):
        if i in seen: continue
        n, j = 0, i
        while j not in seen: seen.add(j); j = move[j]; n += 1
        out = lcm(out, n)
    return out
def primes_of(periods): return sorted({p for n in periods for p in range(2, n + 1) if n % p == 0 and is_prime(p)})
def made_by(makers, size):
    one = tuple(range(size)); found, edge = {one}, [one]
    while edge:
        nxt = []
        for g in edge:
            for m in makers:
                h = tuple(m[g[i]] for i in range(size))
                if h not in found: found.add(h); nxt.append(h)
        edge = nxt
    return found

# ---- a sphere's eight triangles: a triangle is three signs, + + + to - - -
TRI = list(itertools.product((1, -1), repeat=3))
def as_move(perm, signs): return tuple(TRI.index(tuple(signs[i] * t[perm[i]] for i in range(3))) for t in TRI)
MIRRORS = [as_move((0, 1, 2), s) for s in ((-1, 1, 1), (1, -1, 1), (1, 1, -1))]
ALL_EIGHT = {(p, s) for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)}     # a triangle's corners onto corners: 48

# ---- a torus of sixteen patches, as the 57th's check lays them: a name's number less 1, its quarter and its band
def patch(n): return (n - 1) & 3, (n - 1) >> 2
def beside(a, b):
    (q1, j1), (q2, j2) = patch(a), patch(b)
    return sorted(((q1 - q2) % 4, (j1 - j2) % 4)) in ([0, 1], [0, 3])
def up8(n): return n + 8 if n <= 8 else n - 8
def less17(n): return 17 - n
def all_moves_of_the_patches():
    """all layings of the sixteen patches onto the sixteen, a patch beside a patch as it was"""
    near = {a: {b for b in range(1, 17) if beside(a, b)} for a in range(1, 17)}
    out, laid = [], {}
    order = list(range(1, 17))
    def go(k):
        if k == 16: out.append(tuple(laid[n] - 1 for n in order)); return
        a = order[k]
        for b in range(1, 17):
            if b in laid.values(): continue
            if all((laid[c] in near[b]) == (c in near[a]) for c in order[:k]):
                laid[a] = b; go(k + 1); del laid[a]
    go(0)
    return out

def text_of(f):
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", "\n", t))

if __name__ == "__main__":
    ROOT = Path(sys.argv[1]).resolve()
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")

    print("1 · A sphere's eight triangles, by their own moves")
    by_mirrors = made_by(MIRRORS, 8)
    line("is", len(by_mirrors) == 8 and {period(g) for g in by_mirrors} == {1, 2},
         "three mirrors make eight moves, a move a triangle: all are as they were at one doing or at two")
    all8 = {as_move(p, s) for p, s in ALL_EIGHT}; per8 = sorted({period(g) for g in all8})
    line("is", len(all8) == 48 and primes_of(per8) == [2, 3],
         f"all moves laying the eight triangles onto the eight are 48, two fours by 3: their periods are {', '.join(map(str, per8))}")
    line("is", 3 in per8 and not any(n % p == 0 for n in per8 for p in (5, 7, 11, 13, 17, 37, 59)),
         "a round of three is among them, the triangle's own three corners; no round of 5, 7, 11, 13, 17, 37 or 59 is")

    print("\n2 · A torus of sixteen patches, by its own moves")
    m8 = tuple(up8(n) - 1 for n in range(1, 17)); m17 = tuple(less17(n) - 1 for n in range(1, 17))
    own = made_by([m8, m17], 16)
    line("is", len(own) == 4 and {period(g) for g in own} == {1, 2},
         "the drawing's two moves, 8 up and 17 less, make four moves: all are as they were at one doing or at two")
    rounds = sorted({tuple(sorted({g[n - 1] + 1 for g in own})) for n in range(1, 17)})
    one = sorted(ROOT.glob("Exhibit_ONE_Natural_Resolver_*.md"))[0].read_text(encoding="utf-8")
    living = sorted(tuple(sorted(map(int, x))) for x in set(re.findall(r"(?<![\d-])(\d+)-(\d+)-(\d+)-(\d+)(?![\d-])", one)) if sorted(map(int, x))[0] in (1, 2, 3, 4) and sum(map(int, x)) == 34)
    line("is", rounds == [(1, 8, 9, 16), (2, 7, 10, 15), (3, 6, 11, 14), (4, 5, 12, 13)] and all(r in living for r in rounds),
         "the four moves lay sixteen names in four fours: the four bi-foldings, as Exhibit ONE says them")
    allp = all_moves_of_the_patches(); per16 = sorted({period(g) for g in allp})
    line("is", len(allp) == 384 and m8 in allp and m17 in allp and primes_of(per16) == [2, 3],
         f"all moves laying the sixteen patches onto the sixteen, a patch beside a patch as it was, are 384, seven twos by 3: their periods are {', '.join(map(str, per16))}")
    line("is", {g[0] for g in allp} == set(range(16)),
         "a patch is laid onto all sixteen by them: the figure says no patch other than an other, a prime's name as a name of no prime")

    print("\n3 · A prime's name under the drawing's two moves")
    P = [n for n in range(1, 18) if is_prime(n)]
    line("is", P == [2, 3, 5, 7, 11, 13, 17], "the primes among 1 to 17 are seven names' numbers: 2, 3, 5, 7, 11, 13 and 17")
    on8 = {n: up8(n) for n in P if n <= 16}; on17 = {n: less17(n) for n in P if n <= 16}
    line("is", [on8[n] for n in (3, 5, 7)] == [11, 13, 15] and not is_prime(15),
         "8 up lays 3, 5 and 7 onto 11, 13 and 15: two primes, and 15, three fives")
    line("is", not any(is_prime(v) for v in on17.values()),
         "17 less lays 2, 3, 5, 7, 11 and 13 onto " + ", ".join(str(on17[n]) for n in (2, 3, 5, 7, 11, 13)) + ": none a prime")
    line("is", not any({g[n - 1] + 1 for n in P[:6]} == set(P[:6]) for g in own if g != tuple(range(16))),
         "no move of the drawing's own lays the primes' names onto the primes' names")

    print("\n4 · A winding by +1, along and across")
    def winding(p, q):
        n, a, b = 0, 0, 0
        while True:
            a, b, n = (a + 1) % p, (b + 1) % q, n + 1
            if (a, b) == (0, 0): return n
    line("is", winding(4, 4) == 4, "on a torus of 4 by 4 a winding by +1 is at its opening patch again at 4 of 16 patches")
    table = list(csv.reader(open(ROOT / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    col = next(j for j, h in enumerate(table[0]) if h.startswith("its prime, by its position"))
    seventeen = [int(r[col]) for r in table[1:18]]
    line("is", seventeen == [p for p in range(2, 60) if is_prime(p)] and len(seventeen) == 17 and seventeen[11] == 37,
         "the one table of the seventeen names lays a name's prime by its position: seventeen primes, 2 to 59, and 37 at the 12th name")
    doublings = [p for p in seventeen if (p - 1) & (p - 2) == 0]
    line("is", doublings == [2, 3, 5, 17] and (37 - 1) == 4 * 9,
         "by doublings of 1 and one more, four of the seventeen primes are come to: 2, 3, 5 and 17; thirteen are not, and 37 is 36 and one more, two threes in its 36")
    of_moves = [p for p in seventeen if p in primes_of(per8) or p in primes_of(per16)]
    line("is", of_moves == [2, 3], "of the seventeen primes, two are rounds of the figure's own moves, 2 and 3; fifteen are not, 5 to 59")
    pairs = list(itertools.combinations(seventeen, 2))
    line("is", all(winding(p, q) == p * q for p, q in pairs),
         f"on a torus of two of the seventeen primes a winding by +1 is through all its cells, at all {len(pairs)} pairs")

    print("\n5 · Exhibit ONE's own tables of mes, an even number and an odd number")
    rows = [(int(n), a.split(", "), int(b.replace(",", ""))) for n, a, b in re.findall(r"^- \*\*Number of selves: (\d+)\*\* · \*a\*: ([^·]+?) · \*b\*: ([\d,]+)", one, flags=re.M)]
    even = [r for r in rows if r[0] % 2 == 0]; odd = [r for r in rows if r[0] % 2]
    line("is", len(rows) >= 13 and len(even) >= 5 and all(b == 2 and "0" not in a for _, a, b in even),
         f"at an even number of mes, {', '.join(str(n) for n, _, _ in even)}: the parities are again at 2 moments, and no 0 is among them")
    line("is", len(odd) >= 8 and all(b == 4 * n and "0" in a for n, a, b in odd),
         f"at an odd number of mes, {', '.join(str(n) for n, _, _ in odd)}: the parities are again at four times the number, and a 0 is among them")

    tori = [(int(p), int(q), int(x.replace(",", ""))) for p, q, x in re.findall(r"\*\*Torus of selves, p along · q across: (\d+) · (\d+)\*\*\s+- \*a\*: ([\d,]+)", one)]
    t_even = [r for r in tori if r[0] % 2 == 0 or r[1] % 2 == 0]; t_odd = [r for r in tori if r[0] % 2 and r[1] % 2]
    line("is", len(tori) >= 11 and len(t_even) >= 1 and all(x == 2 for _, _, x in t_even) and "Either number even: 2." in one,
         "at a torus of mes with an even number along or across, " + ", ".join(f"{p} by {q}" for p, q, _ in t_even) + ": the parities are again at 2 moments")
    line("is", len(t_odd) >= 10 and all(x == (q if q > 2 * p else 4 * p) for p, q, x in t_odd),
         "at a torus of mes with two odd numbers, " + ", ".join(f"{p} by {q}" for p, q, _ in t_odd) + ": at the number across, or at four times the number along")
    line("found", True, "a torus of 4 by 4 is with an even number along and across; Exhibit ONE lays no table of mes at it, and by its own sentence of an even number it is again at 2 moments")

    print("\n6 · The 57th drawing's own text")
    t = text_of(ROOT / MINE / "illustrations/artboards/Draft57.dc.html")
    nums = Counter(int(x) for x in re.findall(r"(?<![\w.−-])\d+(?![\w.])", t))
    line("found", True, "the numbers of the moves it names are 2, 4, 8 and 16: " + ", ".join(f"{n} at {nums[n]} places" for n in (2, 4, 8, 16)))
    line("is", "its prime" not in t and "prime" not in t.lower(), "the word prime is at no place of it, and no name's prime by its position")
    line("is", nums[23] >= 1 and nums[37] == 0 and nums[59] == 0, "the primes on it are names' numbers, and 23 at the co-linear's far side; 37 and 59 are at no place of it")

    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
