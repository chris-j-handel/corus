#!/usr/bin/env python3
"""A chat of two by the living code: two selves facing, a giving an observing, and the two as one cell.

    python3 -I incoming/v406all2/instruments/a_chat_of_two_by_the_living_code.py .

A partner's sayings, of 22 and 23 November: the transcript of two is their co-possibling, a self's
next observing its other's prior discovering, both ways; one is-or-is-not a number a now; and a chat
is a cell. Exhibit ONE Natural Resolver's code is the python block of its living file, as it is,
and no line of it is written here.

  1  Two selves facing, all their priors and the names 6, 9 and 10: a self's giving with a now is
     its other's observing with the next now, both ways.
  2  A number as a spiral of selves, Exhibit ONE's own opening, 3 to 33: the selves with an is,
     a giving of 0 with a prior, now by now.
  3  Two selves facing with one prior or none, both observing one other, its giving the same two
     nows in a row: beside one cell with that other's givings, one a moment. The two's giving of a
     moment is the parity among their two nows' givings, and their prior is the prior of both.
     Gone through with a prior of none, a + and a -, and all the other's givings of one to six
     moments: of one parity or none; then, with a prior, + and - together; then two priors not alike,
     beside a cell of any prior.

It writes its lines to standard output. It writes no file and decides nothing.
"""
import itertools
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "v406Reiman" / "instruments"))
from resolver_as_it_is import S, exhibit_spiral_priors, opening, resolver, spiral_couplings

names, page = resolver(sys.argv[1])
step, cell = names["_17_next_existing"], names["_1_now_existing"]
all_is = True

# ---- 1. a self's giving is its other's next observing, both ways
parted = gone = 0
for pa, pb in itertools.product((None, 1, -1), repeat=2):
    for keys in itertools.product((6, 9, 10), repeat=2):
        couplings = {(0, keys[0]): 1, (1, keys[1]): 0}
        society = {0: ([(S, pa)] if pa else [], []), 1: ([(S, pb)] if pb else [], [])}
        for now in range(12):
            givings = {s: cell(*society[s])[0] for s in society}
            society = step(society, couplings)
            gone += 2
            parted += (sorted(society[1][1]) != sorted(givings[0])) + (sorted(society[0][1]) != sorted(givings[1]))
print(f"1. A self's giving is its other's next observing, both ways: {gone} gone through, {parted} parting")
all_is = all_is and parted == 0

# ---- 2. a spiral of n selves: the selves with an is, now by now
print("2. A spiral of n selves: the selves with an is, now by now, once it is going round")
for n in range(3, 34, 2):
    society, couplings, numbers = opening(range(n), exhibit_spiral_priors(n)), spiral_couplings(n), []
    for now in range(12 * n):
        numbers.append(sum(1 for prior, observed in society.values() if prior and dict(cell(prior, observed)[0]).get(S) == 0))
        society = step(society, couplings)
    tail = numbers[4 * n:]
    print(f"   {n:2} selves: with an is at a now, {sorted(set(tail))}; a round of {n} nows, {sum(tail[:n])} of them")
    all_is = all_is and set(tail) <= {0, 1}

# ---- 3. two selves facing, both observing one other: one cell at two nows a moment
GIVEN = {"none": [], "+": [1], "-": [-1], "both": [1, -1]}


def one_cell(prior, givings):
    its_prior, row = [(S, prior)] if prior else [], []
    for given in givings:
        giving, its_prior = cell(its_prior, [(S, v) for v in GIVEN[given]])
        row.append((dict(giving).get(S, "none"), dict(its_prior).get(S)))
    return row


def two_facing(priors, givings, name):
    couplings = {(0, name): 1, (1, name): 0}
    society = {s: ([(S, priors[s])] if priors[s] else [], []) for s in (0, 1)}
    row = []
    for given in givings:
        two_nows = []
        for now in range(2):
            society = {s: (society[s][0], society[s][1] + [(S, v) for v in GIVEN[given]]) for s in society}
            two_nows.append(dict(cell(*society[1])[0]).get(S, "none"))
            society = step(society, couplings)
        parities = [g for g in two_nows if g in (1, -1)]
        if all(g == "none" for g in two_nows):
            giving = "none"
        else:
            giving = parities[0] if parities and len(set(parities)) == 1 else 0
        its_priors = tuple(dict(society[s][0]).get(S) for s in society)
        row.append((giving, its_priors[0] if its_priors[0] == its_priors[1] else its_priors))
    return row


opening_with_none = []


def beside(kinds, pairs_of_priors, name):
    """The two beside one cell of the prior of both; with two priors not alike, beside a cell of any prior."""
    gone = parted = 0
    parting = None
    opening_with_none.clear()
    for priors in pairs_of_priors:
        its_cells = [priors[0]] if priors[0] == priors[1] else [None, 1, -1]
        for moments in range(1, 7):
            for givings in itertools.product(kinds, repeat=moments):
                gone += 1
                the_two = two_facing(priors, givings, name)
                if any(one_cell(prior, givings) == the_two for prior in its_cells):
                    continue
                parted += 1
                opening_with_none.append(givings[0] == "none")
                parting = parting or (priors, givings, one_cell(priors[0], givings), the_two)
    return gone, parted, parting


print("3. Two selves facing, both observing one other, beside one cell, two nows a moment")
ALIKE = [(None, None), (1, 1), (-1, -1)]
for name in (9, 10):
    gone, parted, parting = beside(("none", "+", "-"), ALIKE, name)
    print(f"   name {name}, one prior or none, one parity or none observed: {gone} gone through, {parted} parting")
    all_is = all_is and parted == 0
gone, parted, parting = beside(("both",), [(1, 1), (-1, -1)], 9)
print(f"   with a prior, and + and - together observed: {gone} gone through, {parted} parting; the two invert two nows in a row, their prior again")
print(f"      at {parting[1]} from a prior {parting[0][0]}: one cell {parting[2]}, the two {parting[3]}")
all_is = all_is and parted == gone
gone, parted, parting = beside(("none", "+", "-"), [(1, -1), (-1, 1)], 9)
with_none = sum(3 ** (moments - 1) for moments in range(1, 7)) * 2
print(f"   with two priors not alike, beside a cell of any prior: {gone} gone through, {parted} parting")
print(f"      the partings are the {with_none} with none observed at the opening moment, all of them and no other: "
      + ("is" if all(opening_with_none) and parted == with_none else "is-not"))
print(f"      at {parting[1]} from the priors {parting[0]}: the two {parting[3]}")
all_is = all_is and all(opening_with_none) and parted == with_none

print("\n" + ("All is" if all_is else "NOT ALL"))
