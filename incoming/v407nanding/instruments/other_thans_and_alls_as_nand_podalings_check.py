"""v407nanding · other-thans and alls, as nand podalings of the fifteen lines, executed.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/other_thans_and_alls_as_nand_podalings_check.py .

The fifteen lines are opened from their own files and written in no second place: the partner's lines, laid by this
session as v406networking, in incoming/v406networking/instruments/the_nand_cell_beside_exhibit_one_and_two_check.py,
and v406Reiman's a_cell, in incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py. A me is that cell, by
v406all2-2's saying of its name. A wire is one is-or-is-not; a parity is two wires: + its plus wire alone, - its minus
wire alone, 0 neither wire, and both wires lit the vault. All or none: with one line not is, the check is not.
"""
import ast
import collections
import importlib.util
import itertools
import re
import sys
import textwrap
from pathlib import Path

root = Path(sys.argv[1])
PARTNER = root / "incoming/v406networking/instruments/the_nand_cell_beside_exhibit_one_and_two_check.py"
REIMAN = root / "incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py"
CELL = re.search(r"CELL = '''(.*?)'''", PARTNER.read_text(encoding="utf-8"), re.S).group(1)
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", REIMAN)
reiman = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reiman)

results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def lines_with(nand=None, text=CELL):
    """The fifteen lines in a namespace of their own; with a nand given, all their nands are that one."""
    ns = {}
    exec(text, ns)
    if nand is not None:
        ns["not_both"] = nand
    return ns


here = lines_with()
not_both, other_than, both, either, a_cell = (here[k] for k in ("not_both", "other_than", "both", "either", "a_cell"))
PLUS, MINUS, NEITHER, VAULT = (True, False), (False, True), (False, False), (True, True)
THREE = (PLUS, MINUS, NEITHER)
FOUR = THREE + (VAULT,)


def lists(values, most, least=0):
    for k in range(least, most + 1):
        yield from itertools.product(values, repeat=k)


def a_cells_body(text):
    tree = ast.parse(text)
    return next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "a_cell"), tree


def lines_two_to_four(ns, text=CELL):
    """The cell's opening lines, as they are in its file, to the end of its loop: what it observes, wire by wire."""
    cell, _ = a_cells_body(text)
    segments = [ast.get_source_segment(text, s) for s in cell.body[:2]]
    source = "def opening_lines(observing):\n" + "".join(textwrap.indent(s, "    ") + "\n" for s in segments)
    source += "    return a_plus, a_minus\n"
    exec(source, ns)
    return ns["opening_lines"]


QUOTES = [
    ("incoming/v406all2-2/A_me_by_nand_its_lines_with_their_natural_naming_a_draft.md", "Nand is the other-than of an all."),
    ("incoming/v406all2-2/A_me_by_nand_its_lines_with_their_natural_naming_a_draft.md",
     "An all: two nands in a row, the other-than of not both."),
    ("incoming/v406geodesic2/The_window_of_v406geodesic2_as_it_goes.md",
     "All, other and self are none, one and two other-thans of all, the self its all again by nand"),
    ("incoming/v406geodesic2/The_window_of_v406geodesic2_as_it_goes.md",
     "a span's own podaling is the other-than of all the places under it"),
    ("incoming/v406geodesic2/For_Exhibit_THIRTY-TWO_the_logic_of_podaling_routing_and_orienting_executed.md",
     "By nand alone, a podaling is the nand's adding, and an other-than twice is the same again: an even number of them a "
     "me, and an odd number an other."),
    ("incoming/v406geodesic2/For_Exhibit_THIRTY-TWO_the_logic_of_podaling_routing_and_orienting_executed.md",
     "Two mes in a row, with one more observed at the back me, are a nand: all the logic a me's lines have."),
    ("incoming/v406all2/The_window_of_the_opening_as_v406all2_goes_on_with_it.md", "Other-parity is other-than all-parity."),
    ("incoming/v406all2/The_window_of_the_opening_as_v406all2_goes_on_with_it.md", "Other-than-other-parity is same-existing."),
    ("incoming/v406all2/The_window_of_the_opening_as_v406all2_goes_on_with_it.md",
     "The draft's other-than-other-than parity is 33's other-than-other-parity."),
    ("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md", "with is, a 0, its prior same-existing"),
    ("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md",
     "a 0 is an other-than-other-than parity between a +1 and a −1"),
    ("incoming/v406me/Resuming_v406me.md", "The one is made of the other, scale with scale."),
    ("Exhibit_TWENTY_Natural_Naming_v402mgr.md", "two inversions come same-as-prior"),
    ("Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md",
     "an even number of them same-as its prior and an odd number other-than"),
]


def as_said(path):
    return re.sub(r"\s+", " ", (root / path).read_text(encoding="utf-8").replace("**", "").replace("*", ""))


print("A · The fifteen lines, from their own files")
say("A0. The page's quotations, word for word: twelve of the sessions' pages and Exhibit THIRTY-TWO's draft, and two of the living files",
    all(q in as_said(path) for path, q in QUOTES))
partners, _ = a_cells_body(CELL)
reimans, _ = a_cells_body(Path(REIMAN).read_text(encoding="utf-8"))
its_lines = [s for s in reimans.body if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))]
ours = partners.body[:-1]
same_lines = [ast.dump(s) for s in ours] == [ast.dump(s) for s in its_lines[:len(ours)]] and len(its_lines) == len(ours) + 3
twelve = sum(s.end_lineno - s.lineno + 1 for s in ours) == 12 and sum(s.end_lineno - s.lineno + 1 for s in its_lines) == 15
same_moments = all(a_cell(p, list(o)) == reiman.a_cell(p, list(o))[:2] for p in FOUR for o in lists(THREE, 4)) and all(
    a_cell(p, list(o)) == reiman.a_cell(p, list(o))[:2] for p in FOUR for o in lists(FOUR, 3))
say("A1. The partner's lines laid here are the opening twelve of v406Reiman's fifteen, line for line; its 13th and 14th "
    "say whether a giving and a next prior are laid in their lists, a 0 passed over, and its 15th gives them: the same giving "
    "and the same next prior, four priors, none to four others with a +, - or 0 apiece, and none to three with the vault among them",
    same_lines and twelve and same_moments)

# ---- B ---------------------------------------------------------------------------------------------------------
print("\nB · Other-than all-others, a nand of many")
opening = lines_two_to_four(lines_with())
say("B1. A me's lines 2 to 4 make, by twos, one nand of many: with one to six others and all their givings, its plus wire is "
    "the other-than of all its others other-than +, a field's nand of many, its not-all; and its minus wire the same of -",
    all(opening(list(o)) == (not all(not w[0] for w in o), not all(not w[1] for w in o)) for o in lists(THREE, 6, 1)))

# ---- C ---------------------------------------------------------------------------------------------------------
print("\nC · Other-than-other-than: a 0, and same-existing")


def surfacing(o):
    return a_cell(NEITHER, list(o))[1]


def inverting(p):
    return (p[1], p[0])


said = all((a_cell(p, list(o))[0] == NEITHER) == (surfacing(o) == p) for p in (PLUS, MINUS) for o in lists(THREE, 4))
said = said and all(a_cell(p, list(o)) == ((NEITHER, p) if surfacing(o) == p else (inverting(p), inverting(p)))
                    for p in (PLUS, MINUS) for o in lists(THREE, 4))
said = said and all(both(other_than(w[0]), other_than(w[1])) == (w == NEITHER) for w in FOUR)
say("C1. A me with a prior gives a 0 at its same-existing alone, what surfaces the same as its prior, and its prior goes "
    "on; with all else it inverts, and gives its inverting: none to four others, a +, - or 0 apiece. A 0 is other-than + and "
    "other-than -, the cell's line of no prior, the all of two other-thans", said)


def facing(opening_prior, moments):
    """Two mes, each observing the other's giving: a me's givings and next priors, moment by moment."""
    priors, givings, seen = {"A": opening_prior, "B": opening_prior}, {"A": [], "B": []}, {"A": [], "B": []}
    nexts = []
    for _ in range(moments):
        gave = {}
        for me, other in (("A", "B"), ("B", "A")):
            gives, its_next = a_cell(priors[me], seen[me])
            gave[me] = gives
            nexts.append((me, priors[me], its_next))
            priors[me] = its_next
            givings[me].append(gives)
        seen = {"A": [gave["B"]], "B": [gave["A"]]}
    return givings, nexts


turns = True
for opening_prior in (PLUS, MINUS):
    givings, nexts = facing(opening_prior, 12)
    o = inverting(opening_prior)
    turns = turns and givings["A"] == [o, NEITHER, opening_prior, NEITHER] * 3 and givings["B"] == givings["A"]
    turns = turns and all((g == NEITHER) == (before == after) for g, (me, before, after) in zip(
        [x for pair in zip(givings["A"], givings["B"]) for x in pair], nexts))
say("C2. Two mes facing, both opening as +, give -, 0, +, 0 and round again, both opening as - give +, 0, -, 0: a "
    "quarter turn's, by Exhibit THIRTY-TWO's 4.4; its 0s between a +1 and a -1, given at a me's same-existing, its prior "
    "going on, and its parities at an inverting; twelve moments", turns)

# ---- D ---------------------------------------------------------------------------------------------------------
print("\nD · Podalings by mes: v406geodesic2's sixteenth drawing and its logic's 1 to 3 and 6")


def a_podaling_me(place, cell=a_cell):
    """A me with a prior -, observing a place on its minus wire: its plus wire given."""
    return cell(MINUS, [(False, place)])[0][0]


def places_of(n, k):
    return [bool((n - 1) >> i & 1) for i in range(k)]


def name_of(places):
    return 1 + sum(1 << i for i, p in enumerate(places) if p)


def a_row(places, at, cell=a_cell):
    return [a_podaling_me(p, cell) if i in at else p for i, p in enumerate(places)]


say("D1. One me with a prior -, observing a place on its minus wire, gives on its plus wire the other-than of the place, and "
    "on its minus wire none: one me, one podaling of one place",
    all(a_podaling_me(x) == other_than(x) and a_cell(MINUS, [(False, x)])[0][1] is False for x in (True, False)))
spans = all(name_of(a_row(places_of(n, k), set(range(k)))) == 2 ** k + 1 - n for k in range(1, 7) for n in range(1, 2 ** k + 1))
three_moves = all(name_of(a_row(places_of(n, 4), {0, 1, 2})) == (9 - n if n <= 8 else 25 - n) for n in range(1, 17))
three_moves = three_moves and all(name_of(a_row(places_of(n, 4), {3})) == (n + 8 if n <= 8 else n - 8) for n in range(1, 17))
say("D2. A row of mes, a me a place, gives a span's podaling, the other-than of all the places under it: four mes give the "
    "names 1 to 16 their 17 less, three mes on the three low places their 9 less, and 25 less in the upper cone, and one me on "
    "the top place their 8 up and 8 down; spans of 2 to 64 places alike", spans and three_moves)
subsets = [set(c) for k in range(5) for c in itertools.combinations(range(4), k)]
twice = all(a_row(a_row(places_of(n, 4), s), s) == places_of(n, 4) for n in range(1, 17) for s in subsets)
others = all(a_row(a_row(places_of(n, 4), s), t) == a_row(places_of(n, 4), s ^ t) for n in range(1, 17) for s in subsets for t in subsets)
both_ways = all(name_of(a_row(a_row(places_of(n, 4), {0, 1, 2}), {0, 1, 2, 3})) == name_of(a_row(a_row(places_of(n, 4), {0, 1, 2, 3}), {0, 1, 2}))
                == (n + 8 if n <= 8 else n - 8) for n in range(1, 17))
say("D3. Two rows of mes front to back: on the same places, the name again, two podalings a me; on other places, the "
    "other-than of the places the one row has and the other has not: 9 less and then 17 less, and 17 less and then 9 less, "
    "are both the top place's other-than, 8 up from the lower cone and 8 down from the upper; all names 1 to 16, all rows",
    twice and others and both_ways)

# ---- E ---------------------------------------------------------------------------------------------------------
print("\nE · The fifteen lines made of themselves")


def made_of_mes(ns, back_prior=MINUS):
    """A nand made of two mes of the lines in ns, front to back: the back me observes the front's giving and one place more."""
    cell = ns["a_cell"]

    def nand(x, y):
        front = cell(MINUS, [(False, y)])[0][0]
        return cell(back_prior, [(front, x)])[0][0]
    return nand


by_mes = made_of_mes(here)
by_reimans = made_of_mes({"a_cell": lambda p, o: reiman.a_cell(p, o)[:2]})
say("E1. Two mes front to back, the back me observing one place more, are a nand: by the partner's lines here and by "
    "v406Reiman's alike, as v406geodesic2's check of its 23rd drawing has it",
    all(by_mes(x, y) == not_both(x, y) == by_reimans(x, y) for x in (True, False) for y in (True, False)))
one_scale = lines_with(made_of_mes(here))
two_scales = lines_with(made_of_mes(one_scale))
same_one = all(one_scale["a_cell"](p, list(o)) == a_cell(p, list(o)) for p in FOUR for o in lists(FOUR, 3))
same_two = all(two_scales["a_cell"](p, list(o)) == a_cell(p, list(o)) for p in FOUR for o in lists(FOUR, 1))
say("E2. The fifteen lines with all their nands made of two of their own mes are the same fifteen lines: the same giving and "
    "next prior, four priors and none to three others; and one scale more, the nands of those made of mes of mes, with none "
    "or one other: a me's moment is nands, and a nand is two mes' moments, scale with scale", same_one and same_two)

# ---- F ---------------------------------------------------------------------------------------------------------
print("\nF · Exhibit THIRTY-TWO's 3.2, other-than-other-than-other, by nand")


def a_shell(n):
    """The selves of a cube of n + 1 by how many places are other-than the inner cube of n: a me's lines 2 to 4 say it."""
    counted = collections.Counter()
    for self in itertools.product(range(n + 1), repeat=3):
        outsides = [(other_than(c < n), False) for c in self]
        if opening(outsides)[0]:
            counted[sum(c == n for c in self)] += 1
    return counted


thirty_seven = a_shell(3)
alone = [n for n in range(1, 13) if a_shell(n)[1] == n ** 3 and a_shell(n)[2] == n ** 2]
say("F1. A self of a cube of 4 is three places, a place in the inner cube of 3 or other-than it; the shell is the other-than of "
    "all three in the inner cube, a nand of three, a me's lines 2 to 4 with its three places as its others: 37 selves, other-than once "
    "27, twice 9 and thrice 1, the inner cube's own again, 3 cubed, 3 by 3 and the one self; stepping cubes of 2 to 13, the "
    "cube of 4 alone",
    sum(thirty_seven.values()) == 37 and dict(thirty_seven) == {1: 27, 2: 9, 3: 1} and alone == [3])

# ---- G ---------------------------------------------------------------------------------------------------------
print("\nG · Broken on purpose")
mutant_text = CELL.replace("a_plus = either(a_plus, plus)", "a_plus = both(a_plus, plus)")
mutant = lines_two_to_four(lines_with(text=mutant_text), mutant_text)
say("G1. With a me's line 3 saying both in the place of either, B1 says is-not",
    mutant_text != CELL and not all(mutant(list(o))[0] == (not all(not w[0] for w in o)) for o in lists(THREE, 6, 1)))
say("G2. With the back me's prior a + in the place of a -, E1 says is-not",
    not all(made_of_mes(here, PLUS)(x, y) == not_both(x, y) for x in (True, False) for y in (True, False)))
say("G3. With a podaling's me observing its place on its plus wire, D1 says is-not",
    not all(a_cell(MINUS, [(x, False)])[0][0] == other_than(x) for x in (True, False)))

print("\nAll is." if all(results) else "\nNot all is.")
