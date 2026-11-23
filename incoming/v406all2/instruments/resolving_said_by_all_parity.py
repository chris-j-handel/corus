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

It writes its lines to standard output. It writes no file and decides nothing.
"""
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
print("\n" + ("All is" if not parted and again else "NOT ALL"))
