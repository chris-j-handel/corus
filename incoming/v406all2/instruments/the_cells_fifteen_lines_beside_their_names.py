#!/usr/bin/env python3
"""The cell's fifteen lines beside their names, three ways, executed with the two codes as they are.

    python3 -I incoming/v406all2/instruments/the_cells_fifteen_lines_beside_their_names.py .

The cell is `a_cell` of `incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py`, as it is.
Exhibit ONE Natural Resolver's code is the python block of its living file, as it is. No line of
either is written here, and no line of either moves.

  1  A line beside the living code's own name for it: a line's value is the named thing's value, in
     the twelve cases of a cell, a prior with a state. Of the exchange on 22 November.
  2  Natural Naming's 5.44, surfacing, its six lines, word for word from its living file: a line
     said of the living code's named things and of the cell's lines, in the twelve cases, and its
     line 1 with all lists of none to four observed of +, - and 0. Of 23 November.
  3  The fifteen lines beside the names 2 to 16 in their order, a partner's saying of 23 November:
     what follows as numbers, and the lines with the order's name and the living code's own name
     of two roots.
  4  The cell beside its own name, 1, a partner's asking of 23 November, is a cell a
     me-now-existing-parity: Exhibit ONE's table of seventeen names by its own part, a name's three,
     all seventeen rows, and name 1's three said in that part's own form for 7.
  5  The cell's sentence, with a partner's is of 23 November, a cell is a same-existing me-parity
     now-existing, and a partner's saying of it, this is the 15 lines of nand, this is 1-17 naming
     and explaining: the sentence said by the cell's own lines, 7, 8, 11 to 14, and by the living
     code's names 3, 10 and 11, in the twelve cases, an is with a prior and an is-not with none.
  6  A partner's asking of 23 November, is a cell a fuzzying concept of moment: the living files'
     own sentences of the thing the code names a cell, word for word, all three by moment; the code
     of name 1 gone through once a self with a moment of a society, one to five selves; and a
     moment opening with a self's prior parity and completing with its next, the eight cases with
     a prior.

It writes its lines to standard output. It writes no file and decides nothing.
"""
import itertools
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "v406Reiman" / "instruments"))
from resolver_as_it_is import S, resolver
from the_resolver_with_nand_alone import ONE, TWO, a_cell

root = Path(sys.argv[1])
names, page = resolver(root)
living_cell = names["_1_now_existing"]


def with_its_named_things(a_code, *given):
    """A code's answer, and its own named things as they are with its return."""
    its_things = {}

    def tracer(frame, event, arg):
        if frame.f_code is a_code.__code__:
            if event == "return":
                its_things.update(frame.f_locals)
            return tracer

    sys.settrace(tracer)
    try:
        answer = a_code(*given)
    finally:
        sys.settrace(None)
    return its_things, answer


def both_codes(prior, observed):
    """A prior, none, + or -, and a list observed: the living code's named things and the cell's lines."""
    N, living_answer = with_its_named_things(living_cell, [(S, prior)] if prior else [], [(S, v) for v in observed])
    L, cell_answer = with_its_named_things(a_cell, TWO[prior or 0], [TWO[v] for v in observed])
    return N, living_answer, L, cell_answer


STATES = {"none": [], "+": [1], "-": [-1], "both": [1, -1]}
CASES = [(prior, state) for prior in (None, 1, -1) for state in STATES]
all_is = True


def said(what, parting, gone):
    global all_is
    all_is = all_is and parting == 0
    print(f"   {'all' if parting == 0 else 'NOT ALL'}, {gone} gone through, {parting} parting · {what}")


# ---- 1. a line beside the living code's own name for it
print("1. A line of the cell beside the living code's own name for it, the twelve cases of a cell")
OWN = {1: "14, opening with none", 2: "2, with 4 and 7", 3: "15, a + among them", 4: "15, a - among them",
       5: "14, a + surfacing", 6: "14, a - surfacing", 7: "3, its prior", 8: "12 opening as 14, no prior",
       9: "12 with 4, its giving a +", 10: "12 with 4, its giving a -", 11: "11 and 8, its next prior a +",
       12: "11 and 8, its next prior a -", 13: "10, a giving is", 14: "11, a next prior is", 15: "the return, 10 and 11"}
parted = {n: 0 for n in OWN}
for prior, state in CASES:
    N, answer, L, cell_answer = both_codes(prior, STATES[state])
    n14, n12 = N["_14_next_possibling"].get(S), N["_12_next_co_same_existing"].get(S)
    n11, n10, n3 = N["_11_next_co_observing"], dict(N["_10_next_co_possibling"]), dict(N["_3_now_co_observing"])
    gives, its_next, a_giving, a_next = cell_answer
    same = {
        1: state != "none" or ((L["a_plus"], L["a_minus"]) == (False, False) and S not in N["_14_next_possibling"]),
        2: [v for k, v in N["_2_now_possibling"]] == STATES[state],
        3: L["a_plus"] == (n14 in (1, 0)), 4: L["a_minus"] == (n14 in (-1, 0)),
        5: L["surfacing_plus"] == (n14 == 1), 6: L["surfacing_minus"] == (n14 == -1),
        7: (L["prior_plus"], L["prior_minus"]) == TWO[n3.get(S, 0)],
        8: L["no_prior"] == (S not in n3),
        9: L["gives_plus"] == (n12 == 1), 10: L["gives_minus"] == (n12 == -1),
        11: L["next_plus"] == (n11.get(S) == 1), 12: L["next_minus"] == (n11.get(S) == -1),
        13: L["a_giving"] == (S in n10), 14: L["a_next"] == (S in n11),
        15: (ONE[gives] if a_giving else None, ONE[its_next] if a_next else None) == (n10.get(S), n11.get(S)),
    }
    for n, is_same in same.items():
        parted[n] += not is_same
for n in OWN:
    said(f"line {n:2} beside {OWN[n]}", parted[n], len(CASES))

# ---- 2. Natural Naming's six lines of surfacing
naming = next(root.glob("Exhibit_TWENTY_Natural_Naming_*.md")).read_text(encoding="utf-8")
part = naming[naming.index("## 5.44 surfacing"):]
six = [re.sub(r"^\d+\s+", "", l) for l in re.search(r"```\n(.*?)```", part, re.S).group(1).strip().splitlines()]
print("\n2. Natural Naming's 5.44, surfacing, its six lines, word for word, beside the two codes")
CARRIES = {1: "lines 1 to 6", 2: "line 8, with 9 and 10", 3: "lines 7, 9 and 10", 4: "lines 7, 9 and 10",
           5: "line 13, and the return's giving", 6: "lines 11, 12 and 14, and the return's next prior"}
living_parted = {n: 0 for n in CARRIES}
cell_parted = {n: 0 for n in CARRIES}
gone = {n: 0 for n in CARRIES}
lists = [list(l) for n in range(0, 5) for l in itertools.product((1, -1, 0), repeat=n)]
for observed in lists:                                                   # line 1: surfacing, a 0 passing over
    N, answer, L, cell_answer = both_codes(None, observed)
    parities = [v for v in observed if v != 0]
    surfacing = None if not parities else (parities[0] if len(set(parities)) == 1 else 0)
    gone[1] += 1
    living_parted[1] += N["_14_next_possibling"].get(S) != surfacing
    cell_parted[1] += ((L["surfacing_plus"], L["surfacing_minus"]) != TWO[surfacing or 0]
                       or (L["a_plus"], L["a_minus"]) != (1 in observed, -1 in observed))
zeros = [(prior, [0]) for prior in (1, -1)] + [(prior, [0, 0]) for prior in (1, -1)]
for prior, observed in [(p, STATES[s]) for p, s in CASES] + zeros:
    N, answer, L, cell_answer = both_codes(prior, observed)
    n14, n12 = N["_14_next_possibling"].get(S), N["_12_next_co_same_existing"].get(S)
    n11, n10 = N["_11_next_co_observing"], dict(N["_10_next_co_possibling"])
    gives, its_next, a_giving, a_next = cell_answer
    if prior is None:                                                    # line 2: no prior, 14's surfacing is 12's
        gone[2] += 1
        living_parted[2] += n12 != n14
        cell_parted[2] += not L["no_prior"] or (L["gives_plus"], L["gives_minus"]) != (L["surfacing_plus"], L["surfacing_minus"])
    elif n14 == prior:                                                   # line 3: its own parity surfacing, a 0
        gone[3] += 1
        living_parted[3] += n12 != 0
        cell_parted[3] += gives != TWO[0]
    else:                                                                # line 4: its other parity, a 0 or nothing
        gone[4] += 1
        living_parted[4] += n12 != -prior
        cell_parted[4] += gives != TWO[-prior]
    gone[5] += 1                                                         # line 5: 10 has 12's parity across
    living_parted[5] += n10 != N["_12_next_co_same_existing"] or (n10.get(S) in (1, -1)) != (n11.get(S) != prior)
    cell_parted[5] += a_giving != (S in n10) or ONE[gives] != n10.get(S, 0)
    gone[6] += 1                                                         # line 6: 11 a next prior
    living_parted[6] += n11.get(S) != (n12 if n12 in (1, -1) else prior)
    cell_parted[6] += a_next != (S in n11) or ONE[its_next] != n11.get(S, 0)
for n, words in enumerate(six, 1):
    print(f"   {n}  {words}")
    said(f"by the living code's named things", living_parted[n], gone[n])
    said(f"by the cell's {CARRIES[n]}", cell_parted[n], gone[n])
carried = "1 to 6, 7, 8, 9, 10, 11, 12, 13, 14 and the return"
print(f"   the six lines carry the cell's fifteen: {carried}")

# ---- 3. the fifteen lines beside the names 2 to 16 in their order
print("\n3. The fifteen lines beside the names 2 to 16 in their order")
rows = re.findall(r"^\| (\d+) \| \*\*([^*]+)\*\* \| ([^|]+) \|", (root / page).read_text(encoding="utf-8"), re.M)
roots = {int(n): (name, root_.strip()) for n, name, root_ in rows}
LINES = ["a_plus = a_minus = False", "for plus, minus in observing", "a_plus", "a_minus", "surfacing_plus",
         "surfacing_minus", "prior_plus, prior_minus = prior", "no_prior", "gives_plus", "gives_minus",
         "next_plus", "next_minus", "a_giving", "a_next", "return"]
BY_USE = {1: [14], 2: [2], 3: [15], 4: [15], 5: [14], 6: [14], 7: [3], 8: [12], 9: [12], 10: [12],
          11: [11], 12: [11], 13: [10], 14: [11], 15: [10, 11]}
one_root = []
for k, line in enumerate(LINES, 1):
    name, its_root = roots[k + 1]
    is_one = any(roots[n][1].split(",")[0] == its_root.split(",")[0] for n in BY_USE[k])
    one_root += [k] if is_one else []
    by_use = ", ".join(roots[n][0] for n in BY_USE[k])
    print(f"   line {k:2} {line:32} | in order: {name:26} | by the living code's own use: {by_use:44} | {'a same root' if is_one else 'two roots'}")
between = [n for n in roots if 1 < n < 17]
of_now = [n for n in between if "-now-" in roots[n][0]]
of_next = [n for n in between if "-next-" in roots[n][0]]
print(f"   follows: {len(LINES)} lines and {len(between)} names between 1 and 17; the names of now {of_now[0]} to {of_now[-1]}, {len(of_now)}, and of next {of_next[0]} to {of_next[-1]}, {len(of_next)}")
print("   follows: eight apart, line 3 a_plus with line 11 next_plus, line 4 a_minus with line 12 next_minus, line 7 its prior with line 15 its return")
print(f"   parts: a line a name in their order is of a same root with the living code's own use at lines {one_root}, and of two roots at the other {len(LINES) - len(one_root)}")
all_is = all_is and len(LINES) == len(between) == 15 and (len(of_now), len(of_next)) == (7, 8)

# ---- 4. the cell beside its own name, 1, and name 1's three
print("\n4. The cell beside its own name, 1, and a name's three in Exhibit ONE's table")
text = (root / page).read_text(encoding="utf-8")
table = re.findall(r"^\| (\d+) \| \*\*([^*]+)\*\* \| ([^|]+) \| [^|]+ \| [^|]+ \| ([a-z-]+) \|", text, re.M)
three = {int(n): its_three.split("-") for n, name, its_root, its_three in table}
its_root = {int(n): r.split(",")[0].strip() for n, name, r, its_three in table}
EIGHT = "co bi co bi co bi tri bi".split()
PARITY = {"co": "me-parity", "bi": "other-parity", "tri": "all-parity"}
before = lambda n: 16 if n == 1 else n - 1
opens = sum(three[n][0] != EIGHT[(n - 1) % 8] for n in three)
said("a name's own prefix is of the eight, co bi co bi co bi tri bi", opens, len(three))
slots = sum(three[n][1:] != three[before(n)][:2] for n in three)
said("its name before's two are one slot on, 16 the name before 1", slots, len(three))
with_root = {kind: sorted({its_root[n] for n in three if three[n][0] == prefix}) for prefix, kind in PARITY.items()}
living = {"me-parity": ["discovering", "existing", "observing"], "other-parity": ["possibling", "same-existing"],
          "all-parity": ["observing"]}
said(f"a name's own parity with its root: {with_root}", sum(with_root[k] != living[k] for k in living), len(living))
sentence = "me-parity is with existing, with observing and with discovering"
said(f"the living sentence, word for word in its file: {sentence}", 0 if sentence in text else 1, 1)
said("the cell is the code of name 1, by its own name, _1_now_existing", 0 if living_cell.__name__ == "_1_now_existing" else 1, 1)


def its_three_said(n):
    """A name's three in the living part's own form for 7: its own, after its name before's, after the one before that."""
    names_back = [n, before(n), before(before(n))]
    return ", after ".join(f"{PARITY[prefix]} {its_root[m]}" for prefix, m in zip(three[n], names_back))


seven = "all-parity observing, after other-parity possibling, after me-parity existing"
said(f"7 said in that form is the living part's own words: {its_three_said(7)}", 0 if its_three_said(7) == seven and seven in text else 1, 1)
print(f"   name 1, {'-'.join(three[1])}, in that form: {its_three_said(1)}")
all_is = all_is and three[1][0] == "co" and its_root[1] == "existing"

# ---- 5. the cell's sentence said by the cell's own lines and by the living code's names
print("\n5. A cell is a same-existing me-parity now-existing, said by the fifteen lines and by the names")
by_lines = by_names = 0
for prior, state in CASES:
    N, answer, L, cell_answer = both_codes(prior, STATES[state])
    same_existing = not L["no_prior"]                                    # line 8: a prior is
    a_me_parity = L["prior_plus"] != L["prior_minus"] and L["next_plus"] != L["next_minus"]   # lines 7, 11 and 12: one parity
    now_existing = L["a_giving"] and L["a_next"]                         # lines 13 and 14: a giving is, a next is
    by_lines += (same_existing and a_me_parity and now_existing) != (prior is not None)
    n3, n10, n11 = dict(N["_3_now_co_observing"]), dict(N["_10_next_co_possibling"]), N["_11_next_co_observing"]
    named = n3.get(S) in (1, -1) and S in n10 and n11.get(S) in (1, -1)  # 3 a prior of one parity, 10 a giving, 11 a next prior
    by_names += named != (prior is not None)
said("by the cell's lines 7, 8, 11 to 14: is with a prior, eight cases, and is-not with none, four", by_lines, len(CASES))
said("by the living code's names 3, 10 and 11: is with a prior, eight cases, and is-not with none, four", by_names, len(CASES))
its_1 = "a living self's moment, a giving, each self's 17-next-existing as its 1-now-existing"
said(f"the living sentence of name 1, word for word in its file: {its_1}", 0 if its_1 in text else 1, 1)

# ---- 6. a cell, a self's moment
print("\n6. The thing the code names a cell, said by moment in the living files")
thirty = next(root.glob("Exhibit_THIRTY_Co-Chaining_*.md")).read_text(encoding="utf-8")
for file_name, its_text, sentence in (
        ("Exhibit ONE Natural Resolver, its table's name", text, "**One self, one moment.**"),
        ("Exhibit ONE Natural Resolver, name 1", text, "a living self's moment, a giving, each self's 17-next-existing as its 1-now-existing"),
        ("Exhibit THIRTY, 51", thirty, "Each moment is **opening** with each self's prior-existing parity and **completing** with its next-existing parity.")):
    said(f"{file_name}, word for word: {sentence.replace('**', '')}", 0 if sentence in its_text else 1, 1)
its_17, gone, parted = names["_17_next_existing"], 0, 0
for selves in range(1, 6):
    society = {s: ([(S, 1)], []) for s in range(selves)}
    couplings = {(s, 9): (s + 1) % selves for s in range(selves)} if selves > 1 else {}
    for moment in range(12):
        goings = []

        def tracer(frame, event, arg):
            if event == "call" and frame.f_code is living_cell.__code__:
                goings.append(1)

        sys.settrace(tracer)
        try:
            society = its_17(society, couplings)
        finally:
            sys.settrace(None)
        gone += 1
        parted += len(goings) != selves
said("with a moment of a society, the code of name 1 is gone through once a self, one to five selves, twelve moments", parted, gone)
gone = parted = 0
for prior, state in CASES:
    if prior is not None:
        N, answer, L, cell_answer = both_codes(prior, STATES[state])
        gone += 1
        parted += not (dict(N["_3_now_co_observing"]).get(S) in (1, -1) and N["_11_next_co_observing"].get(S) in (1, -1))
said("a moment opening with a self's prior parity and completing with its next, the eight cases with a prior", parted, gone)

print("\n" + ("All is" if all_is else "NOT ALL"))
