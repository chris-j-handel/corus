"""v406geodesic2 · a partner's asking executed: is a logic other than the fifteen lines of nand in this window's work.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/is_a_logic_other_than_nand_in_this_window.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py .

It opens v406Reiman's cell from its own file, with its nand, its other-than, both and either, and its adding and multiplying with nand,
and writes them in no second place. Then the steps this window's drawings go by are executed by nand alone, beside the whole numbers'
own answers: an other-than twice; the living files' three moves on a name; a podaling; a going on; a prime; a place of the turn.
What is with the nand in them is said in the session's page: a name said again and a row, one after an other, and they are no logic.
All or none: with one line not is, the check is not.
"""
import ast, importlib.util, itertools, math, sys
from pathlib import Path
import numpy as np

its_file, root = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", its_file)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
nand, other_than, both, either, a_cell = its.nand, its.other_than, its.both, its.either, its.a_cell
adding, multiplying = its.adding_with_nand, its.multiplying_with_nand
results = []
def line(name, ok): results.append((name, bool(ok)))
IS, NOT = True, False
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))

# ---------- the cell: nand, names and one row ----------
tree = ast.parse(its_file.read_text(encoding="utf-8"))
defs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
called = lambda name: {c.func.id for c in ast.walk(defs[name]) if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)}
its_lines = [n for n in ast.walk(defs["a_cell"]) if isinstance(n, (ast.Assign, ast.For, ast.Return))]
line("the cell's fifteen lines call other-than, both and either alone, and these three call nand alone: no other logic is in the cell",
     len(its_lines) == 15 and called("a_cell") == {"other_than", "both", "either"} and all(called(f) == {"nand"} for f in ("other_than", "both", "either")))
line("with the nand the cell's lines are names said again and one row, one after an other: thirteen givings of a name, one row and one giving back",
     [sum(type(n).__name__ == kind for n in its_lines) for kind in ("For", "Return", "Assign")] == [1, 1, 13])
def of_one_cell(x, y):
    """All a cell gives with two is-or-is-nots at its four places, a place an is, an is-not, the one or the other."""
    out = {}
    for places in itertools.product((IS, NOT, "x", "y"), repeat=4):
        p_plus, p_minus, plus, minus = [x if p == "x" else y if p == "y" else p for p in places]
        (g_plus, g_minus), (n_plus, n_minus), giving, nxt = a_cell((p_plus, p_minus), [(plus, minus)])
        for name, v in (("gives +", g_plus), ("gives -", g_minus), ("next +", n_plus), ("next -", n_minus), ("a giving", giving), ("a next", nxt)):
            out[(places, name)] = v
    return out
cases = [(x, y) for x in (IS, NOT) for y in (IS, NOT)]
tables = [of_one_cell(x, y) for x, y in cases]
makes = lambda f: [k for k in tables[0] if all(tables[i][k] == f(x, y) for i, (x, y) in enumerate(cases))]
one_giving = lambda prior, plus, minus: a_cell(prior, [(plus, minus)])[0][0]
two_in_a_row = lambda x, y: one_giving((NOT, IS), one_giving((NOT, IS), NOT, y), x)
line("one cell alone makes an other-than, a both and an either of two is-or-is-nots, and no nand; two cells in a row make a nand: cells with cells, wired, are all the logic the nand is",
     all(len(makes(f)) > 0 for f in (lambda x, y: other_than(x), both, either)) and len(makes(nand)) == 0 and all(two_in_a_row(x, y) == nand(x, y) for x, y in cases))

# ---------- the rigor's even and odd: an other-than twice ----------
def in_a_row(x, k):
    for _ in range(k): x = other_than(x)
    return x
line("an other-than twice is the same again: an even number of other-thans in a row is a me, and an odd number an other, the twelfth drawing's rigor by one line of nand",
     all(in_a_row(x, k) == (x if k % 2 == 0 else other_than(x)) for x in (IS, NOT) for k in range(9)))

# ---------- numbers as places, a row of is-or-is-nots ----------
def places_of(n, wide): return [bool((n >> i) & 1) for i in range(wide)]      # a naming: a number said by its places
def same(a, b):
    """Two rows the same, place with place, by nand alone."""
    ok = IS
    for one, other in zip(a, b): ok = both(ok, other_than(both(either(one, other), nand(one, other))))
    return ok
others = lambda a: [other_than(x) for x in a]

# ---------- the living files' three moves on a name: other-thans alone, no adding ----------
def moved(n, which):
    m = places_of(n - 1, 4)                               # a name less one, in four places
    return {"8 up": m[:3] + [other_than(m[3])], "17 less": others(m), "9 less": others(m[:3]) + [m[3]]}[which]
line("the living files' three moves on a name less one, in four places, are other-thans alone: 8 up and down of its top place, 17 less of all four, and 9 less of its three low places",
     all(same(moved(n, "8 up"), places_of((n + 8 if n <= 8 else n - 8) - 1, 4)) and same(moved(n, "17 less"), places_of(17 - n - 1, 4)) for n in range(1, 17))
     and all(same(moved(n, "9 less"), places_of(9 - n - 1, 4)) for n in range(1, 9)))

# ---------- a podaling and a going on, by the nand's adding ----------
WIDE = 10
ONE_ = places_of(1, WIDE)
def less(a, b):
    """a less b, in a row of places: a, the other-thans of b, and one, added."""
    return adding(adding(a, others(b))[:WIDE], ONE_)[:WIDE]
def podaling(n, s):
    twice = [NOT] + places_of(s, WIDE)[:WIDE - 1]         # twice a station: its places one place on
    return less(twice, places_of(n, WIDE))
STATIONS = range(0, 241, 30)
line("a podaling, twice its station less a number, is the nand's adding alone, for all the drawings' numbers: the stations 0 to 240 and the numbers of the line from 0 to twice a station",
     all(same(podaling(n, s), places_of(2 * s - n, WIDE)) for s in STATIONS for n in range(0, 2 * s + 1)))
line("a going on, 60 on and 120 on, is the nand's adding alone, and two podalings in a row are that going on, place with place",
     all(same(adding(places_of(n, WIDE), places_of(d, WIDE))[:WIDE], places_of(n + d, WIDE)) for n in range(0, 181) for d in (60, 120))
     and all(same(podaling(int(sum(v << i for i, v in enumerate(podaling(n, 30)))), 60), places_of(n + 60, WIDE)) for n in range(0, 61)))

# ---------- a prime, by the nand's multiplying ----------
crossed = [multiplying(places_of(a, 4), places_of(b, 7)) for a in range(2, 16) for b in range(2, 121) if a * b <= 240]
def a_prime(m):
    row = places_of(m, 11)
    none = IS
    for c in crossed: none = both(none, other_than(same(c, row)))
    return both(none, other_than(either(same(row, places_of(0, 11)), same(row, places_of(1, 11)))))
line("a prime among 0 to 240 is the nand's multiplying alone: a number no two numbers past 1, multiplied, are; the 52 primes the drawings' checks have",
     all(a_prime(m) == prime(m) for m in range(241)) and sum(a_prime(m) for m in range(241)) == 52)

# ---------- the figure's turning says whole numbers ----------
def wide(n):
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])
def about_it(k, r):
    t = math.radians(12 * k)
    return np.array([-r * math.sin(t), r * math.cos(t)])
line("the figure's winding says whole numbers alone: a number's place of the turn is its place of 30, its distance is the cone's own, and its podal place is 30 less its place",
     all(np.allclose(at(n)[1:], about_it(n % 30, wide(n))) for n in range(241))
     and all(np.allclose(at(2 * s - n)[1:], about_it((30 - n % 30) % 30, wide(n))) for s in range(30, 211, 30) for n in range(max(0, 2 * s - 240), min(240, 2 * s) + 1)))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
