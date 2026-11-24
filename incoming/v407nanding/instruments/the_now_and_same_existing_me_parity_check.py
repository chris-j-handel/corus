"""v407nanding · the cell named now-and-same-existing-me-parity, its places named by natural naming, executed.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_now_and_same_existing_me_parity_check.py .

A partner's sayings of 24 November: cell is the now moment, and its natural naming is now-and-same-existing-me-parity;
now is four universal moments of same-existing, me-prior, me-now, other-prior and other-now;
the names over-prefixed where all or none at all binary clarity needs it. CODE is a partner's twelve lines and the lines
they need, its gate, its three words and its return, with all places named again. GIVEN is a partner's twelve lines as
given, with the same added lines, from this session's file. All or none: with one line not is, the check is not.
"""
import ast
import io
import itertools
import re
import sys
import tokenize
from pathlib import Path

CODE = '''
NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def not_both(one, other):
    return NOT_BOTH[(one, other)]


def other_than(one):
    return not_both(one, one)


def both(one, other):
    return other_than(not_both(one, other))


def either(one, other):
    return not_both(other_than(one), other_than(other))


def now_and_same_existing_me_parity(me_prior, others_now_other_than_their_prior):
    an_other_now_is_plus = an_other_now_is_minus = False
    for this_other_now_is_plus, this_other_now_is_minus in others_now_other_than_their_prior:
        an_other_now_is_plus = either(an_other_now_is_plus, this_other_now_is_plus)
        an_other_now_is_minus = either(an_other_now_is_minus, this_other_now_is_minus)
    surfacing_is_plus = both(an_other_now_is_plus, other_than(an_other_now_is_minus))
    surfacing_is_minus = both(an_other_now_is_minus, other_than(an_other_now_is_plus))
    me_prior_is_plus, me_prior_is_minus = me_prior
    me_prior_is_none = both(other_than(me_prior_is_plus), other_than(me_prior_is_minus))
    me_now_other_than_me_prior_is_plus = either(both(me_prior_is_none, surfacing_is_plus),
                                                both(me_prior_is_minus, other_than(surfacing_is_minus)))
    me_now_other_than_me_prior_is_minus = either(both(me_prior_is_none, surfacing_is_minus),
                                                 both(me_prior_is_plus, other_than(surfacing_is_plus)))
    me_now_is_plus = either(me_now_other_than_me_prior_is_plus, both(me_prior_is_plus, surfacing_is_plus))
    me_now_is_minus = either(me_now_other_than_me_prior_is_minus, both(me_prior_is_minus, surfacing_is_minus))
    return ((me_now_other_than_me_prior_is_plus, me_now_other_than_me_prior_is_minus),
            (me_now_is_plus, me_now_is_minus))
'''

root = Path(sys.argv[1])
first = (root / "incoming/v406networking/instruments/the_nand_cell_beside_exhibit_one_and_two_check.py").read_text(encoding="utf-8")
GIVEN = re.search(r"CELL = '''(.*?)'''", first, re.S).group(1)
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


ns, given = {}, {}
exec(CODE, ns)
exec(GIVEN, given)
cell = ns["now_and_same_existing_me_parity"]
PLUS, MINUS, NONE, VAULT = (True, False), (False, True), (False, False), (True, True)
FOUR, THREE = (PLUS, MINUS, NONE, VAULT), (PLUS, MINUS, NONE)


def lists(values, most):
    for k in range(most + 1):
        yield from itertools.product(values, repeat=k)


CASES = [(p, list(o)) for p in FOUR for o in lists(THREE, 4)] + [(p, list(o)) for p in FOUR for o in lists(FOUR, 3)]
say("A1. The lines named again give the same moments as a partner's twelve lines with the lines they need, all cases: "
    "four priors, none to four others, and none to three with the vault among them",
    all(cell(p, o) == given["a_cell"](p, o) for p, o in CASES))
tokens = list(tokenize.generate_tokens(io.StringIO(CODE).readline))
tree = ast.parse(CODE)
say("A2. The code carries no story, no docstring and no comment, and the cell calls the gate and its three words alone",
    not any(t.type == tokenize.COMMENT for t in tokens)
    and not any(isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) for n in ast.walk(tree))
    and {c.func.id for c in ast.walk(tree) if isinstance(c, ast.Call)} <= {"not_both", "other_than", "both", "either"})


def surfacing(o):
    return cell(NONE, o)[1]


prior_on = all(cell(p, o)[1] in (PLUS, MINUS) for p in (PLUS, MINUS) for o in lists(THREE, 4))
say("B1. Now: a me-parity with a prior has a next at all its moments, a + or a -, never none: it is same-existing "
    "through its now as a me-parity, none to four others", prior_on)
say("B2. Its value is same-existing at its same-existing moments alone, what surfaces the same as its prior, and "
    "other-than its prior at all else: the name's same-existing is the me-parity's, and not its value's at all moments",
    all(cell(p, o) == ((NONE, p) if surfacing(o) == p else ((p[1], p[0]), (p[1], p[0]))) for p in (PLUS, MINUS)
        for o in lists(THREE, 4)))
born = all(cell(NONE, o)[1] == surfacing(o) for o in lists(THREE, 4))
say("B3. The is-not of the name: with no prior, a me-parity is born with a surfacing, and is none with none surfacing; "
    "with no prior no me-parity is same-existing", born and any(cell(NONE, o)[1] == NONE for o in lists(THREE, 2))
    and any(cell(NONE, o)[1] == PLUS for o in lists(THREE, 2)))
say("B4. With both wires lit, the vault, and none surfacing, the next is the vault again: an all-parity, and no me-parity",
    cell(VAULT, [])[1] == VAULT and cell(VAULT, [NONE])[1] == VAULT)
def facing(a0, b0, moments=12):
    priors, seen, rows = {"A": a0, "B": b0}, {"A": [], "B": []}, []
    for _ in range(moments):
        out = {me: cell(priors[me], seen[me]) for me in ("A", "B")}
        rows.append([(priors[me], out[me][1], out[me][0]) for me in ("A", "B")])
        priors = {me: out[me][1] for me in ("A", "B")}
        seen = {"A": [out["B"][0]], "B": [out["A"][0]]}
    return rows


say("D1. Two mes facing, all four openings, twelve moments: a me lays its now with its now other-than its prior, "
    "and none with its now its prior",
    all(laid == (NONE if now == prior else now) for a0 in (PLUS, MINUS) for b0 in (PLUS, MINUS)
        for row in facing(a0, b0) for prior, now, laid in row))


def four(me_prior, other_prior, other_now):
    return cell(me_prior, [NONE if other_now == other_prior else other_now])[1]


say("D2. Now is four moments, a me-prior, a me-now, an other-prior and an other-now: a me's now is its prior again with "
    "its other's now other-than its other's prior and the same as the me's prior, and other-than its prior at all else; all eight",
    all(four(mp, op, on) == (mp if (on != op and on == mp) else (mp[1], mp[0]))
        for mp in (PLUS, MINUS) for op in (PLUS, MINUS) for on in (PLUS, MINUS)))
say("C1. The gate and its three words have no order: one and other in both orders give the same, all cases",
    all(ns[w](x, y) == ns[w](y, x) for w in ("not_both", "both", "either") for x in (True, False) for y in (True, False)))
names = sorted({t.string for t in tokens if t.type == tokenize.NAME} - {"def", "for", "in", "return", "True", "False"})
WORDS = {"not", "both", "other", "than", "one", "either", "now", "and", "same", "existing", "me", "parity", "prior",
         "others", "their", "an", "is", "plus", "minus", "this", "surfacing", "none"}
say("C2. All names are said in natural words, and in these alone: now, same, existing, me, parity, prior, surfacing, an, "
    "other, others, their, this, one, is, plus, minus, none, not, both, either, than and and",
    set(w for n in names for w in n.lower().split("_")) == WORDS)
mutant = CODE.replace("an_other_now_is_plus = either(an_other_now_is_plus, this_other_now_is_plus)",
                      "an_other_now_is_plus = both(an_other_now_is_plus, this_other_now_is_plus)")
broken = {}
exec(mutant, broken)
say("M1. With the cell's line 3 saying both in the place of either, A1 says is-not",
    not all(broken["now_and_same_existing_me_parity"](p, o) == given["a_cell"](p, o) for p, o in CASES))
print("\nAll is." if all(results) else "\nNot all is.")
