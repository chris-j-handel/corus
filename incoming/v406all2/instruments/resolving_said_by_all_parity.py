#!/usr/bin/env python3
"""Resolving said by all-parity, the twelve cases of a cell, with the living code as it is.

    python3 -I incoming/v406all2/instruments/resolving_said_by_all_parity.py .

A partner's saying of 23 November: resolving is of other-than other-than all-parity universes.
Exhibit ONE Natural Resolver's code is the python block of its living file, as it is, and no line
of it is written here.

Said, and gone through in a prior with a state, three priors and four states:

  - All-parity is the parity surfacing of all a self is observing: a + or a -, and not both.
  - With an all-parity surfacing, a self's next prior is that all-parity.
  - With none surfacing, its next prior is other-than its prior, and two nows in a row are its
    prior again, other-than other-than.
  - Its giving is its next prior once other-than its prior, and a 0 once its prior.

And a cell's parity now by now, with a partner's asking of 23 November, is a cell a
me-now-existing-parity: from a prior of none, a + and a -, all it is observing of one to six nows,
none, a +, a - or both a now. With no prior its parity is none until a parity is surfacing, and that
parity is its own with the next now; once with a parity it is with one parity, a + or a -, at all its
next nows.

And a partner's saying of 23 November: a cell with no prior is not same-existing, and this is a
method of same-existing prior, now and next cycling sequentially. Same-existing is the opening's
line 12, existing both as now is beginning and as the next moment is beginning: here, a cell with a
parity at both. Gone through in the same nows: a now of a cell with no prior, and a now of a cell with
a prior. Then the living code's own lines of a prior, its is-or-is-not same, 12 with 3: gone through
once with a prior and at no now with none. Then the cycling, with societies of one to three selves
facing round: a self's next prior with a now is its prior with the next now.

It writes its lines to standard output. It writes no file and decides nothing.
"""
import itertools
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "v406Reiman" / "instruments"))
from resolver_as_it_is import S, resolver

names, page = resolver(sys.argv[1])
cell = names["_1_now_existing"]
STATES = {"none": [], "+": [1], "-": [-1], "both": [1, -1]}
ALL_PARITY = {"none": None, "+": 1, "-": -1, "both": None}

parted = []
for prior in (None, 1, -1):
    for state, observed in STATES.items():
        giving, next_prior = cell([(S, prior)] if prior else [], [(S, v) for v in observed])
        its_giving, its_next = dict(giving).get(S), dict(next_prior).get(S)
        surfacing = ALL_PARITY[state]
        said_next = surfacing if surfacing else (-prior if prior else None)
        if prior is None and state == "none":
            said_giving = None
        else:
            said_giving = 0 if said_next == prior or said_next is None else said_next
        if (its_next, its_giving) != (said_next, said_giving):
            parted.append((prior, state, (its_next, its_giving), (said_next, said_giving)))
print(f"a next prior the all-parity surfacing, or other-than its prior; a giving its next prior once other-than its prior: 12 gone through, {len(parted)} parting")
for p in parted:
    print("   parts at", p)

prior, row = [(S, 1)], []
for now in range(6):
    giving, prior = cell(prior, [])
    row.append(dict(prior)[S])
print("a self observing none, its prior now by now, from a +:", row)
again = all(row[n] == (1 if n % 2 else -1) for n in range(6))
print("two nows in a row are its prior again:", "is" if again else "is-not")
gone = partings = births = 0
for prior in (None, 1, -1):
    for nows in range(1, 7):
        for observings in itertools.product(STATES, repeat=nows):
            its_prior, was = [(S, prior)] if prior else [], prior
            gone += 1
            for state in observings:
                giving, its_prior = cell(its_prior, [(S, v) for v in STATES[state]])
                now = dict(its_prior).get(S)
                if was is None:
                    as_said = now == ALL_PARITY[state]          # none until a parity is surfacing, then that parity
                    births += now is not None
                else:
                    as_said = now in (1, -1)                    # once a parity, one parity at all next nows
                partings += not as_said
                was = now
print(f"a cell's parity now by now: {gone} gone through, {partings} parting; a parity opening from no prior, {births} of them")

# ---- same-existing, the opening's line 12: a parity both as now is beginning and as the next moment is beginning
with_none = with_none_same = with_a_prior = with_a_prior_same = 0
for prior in (None, 1, -1):
    for nows in range(1, 7):
        for observings in itertools.product(STATES, repeat=nows):
            its_prior, was = [(S, prior)] if prior else [], prior
            for state in observings:
                giving, its_prior = cell(its_prior, [(S, v) for v in STATES[state]])
                now = dict(its_prior).get(S)
                same_existing = was in (1, -1) and now in (1, -1)
                if was is None:
                    with_none += 1
                    with_none_same += same_existing
                else:
                    with_a_prior += 1
                    with_a_prior_same += same_existing
                was = now
print(f"a now of a cell with no prior: {with_none} gone through, {with_none_same} same-existing")
print(f"a now of a cell with a prior: {with_a_prior} gone through, {with_a_prior - with_a_prior_same} not same-existing")

# ---- the living code's own lines of a prior, its is-or-is-not same: gone through with a prior alone
text = (Path(sys.argv[1]) / page).read_text(encoding="utf-8")
block = re.search(r"```python\n(.*?)```", text, re.S).group(1).splitlines()
of_a_prior = [n for n, line in enumerate(block, 1) if "_14_next_possibling.get(_4_now_co_same_existing, 0)" in line]
goings = {}


def tracer(frame, event, arg):
    if frame.f_code is cell.__code__:
        if event == "line" and frame.f_lineno == of_a_prior[0]:
            goings[key] = goings.get(key, 0) + 1
        return tracer


for prior in (None, 1, -1):
    for state, observed in STATES.items():
        key = (prior, state)
        goings[key] = 0
        sys.settrace(tracer)
        try:
            cell([(S, prior)] if prior else [], [(S, v) for v in observed])
        finally:
            sys.settrace(None)
of_none = sum(n for (prior, state), n in goings.items() if prior is None)
of_one = [n for (prior, state), n in goings.items() if prior is not None]
lines_as_said = len(of_a_prior) == 1 and of_none == 0 and of_one == [1] * 8
print(f"the living code's is-or-is-not same, 12 with 3: gone through {of_none} with no prior, four states, and once with a prior, {len(of_one)} of them: "
      + ("is" if lines_as_said else "is-not"))

# ---- cycling: a self's next prior with a now is its prior with the next now
step = names["_17_next_existing"]
cycled = uncycled = 0
for selves in (1, 2, 3):
    couplings = {(s, 9): (s + 1) % selves for s in range(selves)} if selves > 1 else {}
    for priors in itertools.product((None, 1, -1), repeat=selves):
        society = {s: ([(S, priors[s])] if priors[s] else [], []) for s in range(selves)}
        for now in range(12):
            next_priors = {s: sorted(cell(*society[s])[1]) for s in society}
            society = step(society, couplings)
            for s in society:
                cycled += 1
                uncycled += sorted(society[s][0]) != next_priors[s]
print(f"a self's next prior with a now is its prior with the next now: {cycled} gone through, {uncycled} parting")

same_as_said = with_none_same == 0 and with_a_prior_same == with_a_prior and lines_as_said and uncycled == 0
print("\n" + ("All is" if not parted and again and not partings and same_as_said else "NOT ALL"))
