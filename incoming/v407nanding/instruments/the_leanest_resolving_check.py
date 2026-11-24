"""v407nanding · the leanest resolving, is-or-is-not changing next, executed beside a partner's twelve lines.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_leanest_resolving_check.py .

A partner's saying of 24 November: the leanest expression of resolving, with less length, names and functions than now,
and no more things than is-or-is-not changing next; v406geodesic2's draft 31, names by their nands, a me-now a moment on
on a single path, two nands. LEAN is v406geodesic2's single path, a parity one is-or-is-not: a moment on, a me's prior is
its now, and its now is the other-than of the prior of the me back of it. The twelve lines are a partner's, with the
lines they need, from this session's file of the now and same-existing me-parity. All or none.
"""
import ast
import io
import itertools
import re
import sys
import tokenize
from pathlib import Path

LEAN = '''
NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def now_and_same_existing_me_parity(me_now, other_prior):
    return me_now, NOT_BOTH[(other_prior, other_prior)]
'''

root = Path(sys.argv[1])
text = (root / "incoming/v407nanding/instruments/the_now_and_same_existing_me_parity_check.py").read_text(encoding="utf-8")
cells, lean = {}, {}
exec(re.search(r"CODE = '''(.*?)'''", text, re.S).group(1), cells)
exec(LEAN, lean)
cell, step = cells["now_and_same_existing_me_parity"], lean["now_and_same_existing_me_parity"]
PLUS, MINUS, NONE = (True, False), (False, True), (False, False)
WIRES = {True: PLUS, False: MINUS}
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def by_the_twelve_lines(opening, moments):
    """A path of mes closing, a me observing what the me back of it laid: a me's priors, moment by moment."""
    priors, laid, rows = [WIRES[p] for p in opening], None, []
    for _ in range(moments):
        out = [cell(priors[i], [] if laid is None else [laid[i - 1]]) for i in range(len(priors))]
        laid, priors = [o[0] for o in out], [o[1] for o in out]
        rows.append(priors)
    return rows


def by_the_lean_line(opening, moments):
    """The same path: a me's prior and its now, a moment on its now the other-than of the prior of the me back of it."""
    priors, nows, rows = list(opening), [step(None, p)[1] for p in opening], []
    rows.append([WIRES[n] for n in nows])
    for _ in range(moments - 1):
        pairs = [step(nows[i], priors[i - 1]) for i in range(len(priors))]
        priors, nows = [p for p, n in pairs], [n for p, n in pairs]
        rows.append([WIRES[n] for n in nows])
    return rows


same = all(by_the_twelve_lines(o, 4 * n + 4) == by_the_lean_line(o, 4 * n + 4)
           for n in range(1, 8) for o in itertools.product((True, False), repeat=n))
say("L1. On a path of mes closing, all with priors, a me's now by the lean line is its prior by the twelve lines at all "
    "moments: one to seven mes, all openings, four moments a me and four more", same)
tree = ast.parse(LEAN)
fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef))
names = {t.string for t in tokenize.generate_tokens(io.StringIO(LEAN).readline) if t.type == tokenize.NAME}
say("L2. The lean line is one function of one line, one nand a me a moment, and its names are four: the table, the "
    "function, a me's now and an other's prior",
    len(fn.body) == 1 and sum(isinstance(n, ast.Subscript) for n in ast.walk(fn)) == 1
    and names - {"def", "return", "True", "False"} == {"NOT_BOTH", "now_and_same_existing_me_parity", "me_now", "other_prior"})
say("L3. Its things are an is-or-is-not changing next and no more: no surfacing, no giving, no list and no other word",
    not any(isinstance(n, (ast.For, ast.If, ast.BoolOp, ast.Compare, ast.Call)) for n in ast.walk(fn)))
twelve = sum(1 for _ in re.finditer(r"\b(not_both|other_than|both|either)\(", re.search(r"def now_and.*", re.search(r"CODE = '''(.*?)'''", text, re.S).group(1), re.S).group(0)))
say("L4. The twelve lines call the gate's words at many places with one other observed; the lean line calls the gate once",
    twelve > 20)
broken = {}
exec(LEAN.replace("NOT_BOTH[(other_prior, other_prior)]", "other_prior"), broken)
step_saved = step
step = broken["now_and_same_existing_me_parity"]
say("M1. With the other's prior carried with no other-than, L1 says is-not",
    not all(by_the_twelve_lines(o, 12) == by_the_lean_line(o, 12) for o in itertools.product((True, False), repeat=3)))
step = step_saved
print("\nAll is." if all(results) else "\nNot all is.")
