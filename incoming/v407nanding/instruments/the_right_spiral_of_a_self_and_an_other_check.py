"""v407nanding · a partner's sayings of the right spiral of a self and an other, executed step by step.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_right_spiral_of_a_self_and_an_other_check.py .

A partner's sayings of 24 November: is-not-other-than-other-than-all-other, is-same; is-not-other-than-other,
is-not-other-than, is-same; near, not correct and not in order, and resolving in this right spiraling co-sequencing of
self and other. A right spiral step is v406geodesic2's, a pair (x, y) to (y, -x): the self takes the other's place, and
the other takes the self's other-than. The other-than is the fifteen lines' own, opened from this session's file of
their natural naming. A saying is said of the self's place: is-W, the place is W; is-not-other-than-W, the place is not
W's other-than. With one other, all other is the other. A saying is is at a step with all four openings, all or none.
"""
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
text = (root / "incoming/v407nanding/instruments/the_fifteen_lines_by_their_natural_naming_check.py").read_text(encoding="utf-8")
ns = {}
exec(re.search(r"NATURAL_CODE = '''(.*?)'''", text, re.S).group(1), ns)
other_than, now_existing = ns["other_than"], ns["now_existing"]
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def step(self_, other):
    return other, other_than(self_)


def places(x, y, k):
    s, o = x, y
    for _ in range(k):
        s, o = step(s, o)
    return s, o


OPENINGS = list(itertools.product((True, False), repeat=2))
SAYINGS = {
    "is-not-other-than-other": lambda s, x, y: s != other_than(y),
    "is-other-than": lambda s, x, y: s == other_than(x),
    "is-not-other-than-other-than-all-other": lambda s, x, y: s != other_than(other_than(y)),
    "is-not-other-than": lambda s, x, y: s != other_than(x),
    "is-same": lambda s, x, y: s == x,
}


def at(k):
    return [name for name, said in SAYINGS.items() if all(said(places(x, y, k)[0], x, y) for x, y in OPENINGS)]


table = {k: at(k) for k in (1, 2, 3, 4)}
say("S1. A right spiral step is one exchange and one other-than: four steps on, the self and the other are as they opened, "
    "all openings", all(places(x, y, 4) == (x, y) for x, y in OPENINGS))
say("S2. One step on, the self is-not-other-than-other: the self is the other, all openings", table[1] == ["is-not-other-than-other"])
say("S3. Two steps on, the self is-other-than: the self is its own other-than, all openings", table[2] == ["is-other-than"])
say("S4. Three steps on, the self is-not-other-than-other-than-all-other: with one other, the self is the other's other-than, "
    "all openings", table[3] == ["is-not-other-than-other-than-all-other"])
say("S5. Four steps on, the self is-not-other-than and is-same: the two are one, all openings",
    table[4] == ["is-not-other-than", "is-same"])
say("S6. The other is the self one step on: the other's place at all steps is the self's place at the next, eight steps",
    all(places(x, y, k)[1] == places(x, y, k + 1)[0] for x, y in OPENINGS for k in range(8)))
partners = ["is-not-other-than-other-than-all-other", "is-same", "is-not-other-than-other", "is-not-other-than", "is-same"]
say("S7. The partner's sayings, five with is-same twice, are is at the steps 1, 3 and 4; the second step's saying, "
    "is-other-than, is said by none of them",
    sorted(sum(table.values(), [])) == sorted(SAYINGS) and all(n in table[1] + table[3] + table[4] for n in partners)
    and "is-other-than" not in partners and table[2] == ["is-other-than"])

PLUS, MINUS = (True, False), (False, True)


def facing(opening_a, opening_b, moments):
    priors, seen, nexts = {"A": opening_a, "B": opening_b}, {"A": [], "B": []}, []
    for _ in range(moments):
        gave, its = {}, {}
        for me in ("A", "B"):
            gives, its_next, _, _ = now_existing(priors[me], seen[me])
            gave[me], its[me] = gives, its_next
        nexts.append(dict(its))
        priors = its
        seen = {"A": [gave["B"]], "B": [gave["A"]]}
    return nexts


def turned(p):
    return (other_than(p[0]), other_than(p[1]))


def spirals(opening_a, opening_b, moments=12):
    p = [{"A": opening_a, "B": opening_b}] + facing(opening_a, opening_b, moments)
    return all((p[t + 1]["A"], p[t + 2]["B"]) == (p[t + 1]["B"], turned(p[t]["A"])) for t in range(moments - 1))


say("S8. By the fifteen lines, two mes facing, a self and an other opening alike: the self's prior and the other's next "
    "prior step by the right spiral, twelve moments, opening as + and as -", spirals(PLUS, PLUS) and spirals(MINUS, MINUS))
say("S9. Opening unlike, they step by no right spiral: the is-not, both ways", not spirals(PLUS, MINUS) and not spirals(MINUS, PLUS))

print("\nAll is." if all(results) else "\nNot all is.")
