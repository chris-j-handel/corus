#!/usr/bin/env python3
"""The cell by nand alone, gone through apart: a second session's own writing of it beside the living code.

Usage:  python3 -I incoming/v406me/instruments/the_cell_by_nand_alone_gone_through_apart.py LIVE

LIVE is a checkout of the set. Exhibit ONE Natural Resolver's code is the python block of its living
file there, executed as it is. No line of it is written here, and no line of it moves.

What is gone through, a session apart from v406Reiman and from v406all2:

  1  v406Reiman's cell, `a_cell` of `incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py`,
     written here again from its fifteen lines with one is-or-is-not alone, nand, not both: a prior +,
     a prior - and no prior, with none to four observed of +, - and 0, beside 1-now-existing.
  2  v406all2's way of a finite all, of the exchange on 22 November: the parities a self is observing
     come to one of four states, none, a +, a - and both; a state with a value is a state, twelve
     steps; and all lists come to the state of their state with their last.
  3  v406all2's lines beside their names, of the exchange on 22 November: in the twelve cases of a
     prior with a state, the cell's lines 3 to 14 beside the living code's own named things at its
     return, 14-next-possibling, 12-next-co-same-existing and 11-next-co-observing.

A field has all gating written with nand alone. That the two codes are the same is no finding by
itself. What is this explaining's own is the cell's one is-or-is-not said in the living names.

It writes its lines to standard output. It writes no file, reaches no network and decides nothing.
"""
import itertools
import re
import sys
from pathlib import Path

S = "one sharing"


def nand(a, b):
    return not (a and b)


def other_than(a):
    return nand(a, a)


def both(a, b):
    return other_than(nand(a, b))


def either(a, b):
    return nand(other_than(a), other_than(b))


def cell(prior, observing):
    """The fifteen lines, a line's number beside its value."""
    at = {}
    a_plus = a_minus = False                                  # 1
    for plus, minus in observing:                             # 2
        a_plus = either(a_plus, plus)                         # 3
        a_minus = either(a_minus, minus)                      # 4
    at[3], at[4] = a_plus, a_minus
    surfacing_plus = both(a_plus, other_than(a_minus))        # 5
    surfacing_minus = both(a_minus, other_than(a_plus))       # 6
    at[5], at[6] = surfacing_plus, surfacing_minus
    prior_plus, prior_minus = prior                           # 7
    no_prior = both(other_than(prior_plus), other_than(prior_minus))   # 8
    at[8] = no_prior
    gives_plus = either(both(no_prior, surfacing_plus), both(prior_minus, other_than(surfacing_minus)))   # 9
    gives_minus = either(both(no_prior, surfacing_minus), both(prior_plus, other_than(surfacing_plus)))   # 10
    at[9], at[10] = gives_plus, gives_minus
    next_plus = either(gives_plus, both(prior_plus, surfacing_plus))      # 11
    next_minus = either(gives_minus, both(prior_minus, surfacing_minus))  # 12
    at[11], at[12] = next_plus, next_minus
    at[13] = either(other_than(no_prior), either(a_plus, a_minus))        # 13
    at[14] = either(next_plus, next_minus)                                # 14
    return at                                                             # 15


TWO = {1: (True, False), -1: (False, True), 0: (False, False), None: (False, False)}


def one(plus, minus):
    return {(True, False): 1, (False, True): -1}.get((plus, minus), 0)


def living(root):
    page = next(Path(root).glob("Exhibit_ONE_Natural_Resolver_*.md"))
    code = re.search(r"```python\n(.*?)```", page.read_text(encoding="utf-8"), re.S).group(1)
    names = {}
    exec(compile(code, str(page), "exec"), names)
    return names["_1_now_existing"], page.name


def at_its_return(now, its_prior, its_observing):
    """1-now-existing executed as it is, with its own named things as they are at its return."""
    seen = {}

    def a_call(frame, event, arg):
        if frame.f_code.co_name != "_1_now_existing":
            return None

        def a_line(a_frame, an_event, an_arg):
            if an_event == "return":
                seen.update({k: (dict(v) if isinstance(v, dict) else v) for k, v in a_frame.f_locals.items()})
            return a_line
        return a_line

    sys.settrace(a_call)
    try:
        returned = now(its_prior, its_observing)
    finally:
        sys.settrace(None)
    return returned, seen


def says(ok):
    return "is" if ok else "IS NOT"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    now, page = living(argv[1])
    all_is = True
    print(f"The living code: {page}, executed as it is")

    cases = same = 0
    for prior in (1, -1, None):
        for n in range(5):
            for observed in itertools.product((1, -1, 0), repeat=n):
                its_prior = [(S, prior)] if prior else []
                giving, next_prior = now(its_prior, [(S, v) for v in observed])
                at = cell(TWO[prior], [TWO[v] for v in observed])
                mine_giving = [(S, one(at[9], at[10]))] if at[13] else []
                mine_next = [(S, one(at[11], at[12]))] if at[14] else []
                cases += 1
                same += sorted(giving) == sorted(mine_giving) and sorted(next_prior) == sorted(mine_next)
    print(f"1. the cell written again from its fifteen lines, {cases} cases, its giving and its next prior the living code's: {says(cases == same)}")
    all_is = all_is and cases == same

    def state(observed):
        giving = now([], [(S, v) for v in observed])[0]
        return "none" if not giving else {1: "+", -1: "-", 0: "both"}[giving[0][1]]

    of = {"none": [], "+": [1], "-": [-1], "both": [1, -1]}
    four = all(state(v) == k for k, v in of.items())
    steps = True
    for a_state, its in of.items():
        for value in (1, -1, 0):
            at = cell(TWO[None], [TWO[v] for v in its + [value]])
            mine = "none" if not (at[3] or at[4]) else "both" if (at[3] and at[4]) else "+" if at[3] else "-"
            steps = steps and state(its + [value]) == mine
    lists = all(state(list(o)) == state(of[state(list(o[:-1]))] + [o[-1]])
                for n in range(1, 7) for o in itertools.product((1, -1, 0), repeat=n))
    print(f"2. four states of the parities a self is observing: {says(four)} · twelve steps, a state with a value, living and by nand: {says(steps)} · all lists of one to six observed come to the state of their state with their last: {says(lists)}")
    all_is = all_is and four and steps and lists

    lines = True
    for prior in (1, -1, None):
        for a_state, its in of.items():
            _, seen = at_its_return(now, [(S, prior)] if prior else [], [(S, v) for v in its])
            at = cell(TWO[prior], [TWO[v] for v in its])
            n14, n12, n11 = seen["_14_next_possibling"], seen["_12_next_co_same_existing"], seen["_11_next_co_observing"]
            lines = lines and all([
                (S in n14) == (at[3] or at[4]),           # 3 and 4, a parity observed: 15-next-observing
                n14.get(S, 0) == one(at[5], at[6]),       # 5 and 6, the parity surfacing: 14-next-possibling
                (prior is None) == at[8],                 # 8, no prior: a birth
                n12.get(S, 0) == one(at[9], at[10]),      # 9 and 10, its giving: 12-next-co-same-existing
                n11.get(S, 0) == one(at[11], at[12]),     # 11 and 12, its next prior: 11-next-co-observing
                (S in n12) == at[13],                     # 13, a giving is: 10-next-co-possibling
                (S in n11) == at[14],                     # 14, a next prior is: 11-next-co-observing
            ])
    print(f"3. twelve cases of a prior with a state, lines 3 to 14 beside the living code's own 14, 12 and 11 at its return: {says(lines)}")
    all_is = all_is and lines
    print("All is." if all_is else "Not all is.")
    return 0 if all_is else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
