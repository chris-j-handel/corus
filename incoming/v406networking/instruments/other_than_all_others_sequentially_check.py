"""Other-than-all-others and other-than-other-than-all-others, explored sequentially as method, with the NAND cell.
Executed with all cases, all or none.

Use, with the repository's top folder as its first word:
  python3 -I incoming/v406networking/instruments/other_than_all_others_sequentially_check.py .

A partner's saying of 22 November: its two terms, in sequence. All-others is what reaches a self from all its others,
as one: the either of each wire, the cell's a_plus and a_minus. Other-than-all-others is other_than of it, wire by
wire, and other-than-other-than-all-others is other_than of that. Where a self's next prior is read beside its others,
all-others is the either of the priors of the selves it observes. The cell is read from this folder's first
instrument, its one text. No case is drawn by chance and no number of trials is read. It writes no file and reaches
no network.
"""
import itertools
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
HERE = os.path.join(ROOT, "incoming", "v406networking", "instruments")
CELL = re.search(r"CELL = '''(.*?)'''", open(os.path.join(HERE, "the_nand_cell_beside_exhibit_one_and_two_check.py"),
                                            encoding="utf-8").read(), re.S).group(1)


def plain(*parts):
    return re.sub(r"\*\*", "", open(os.path.join(ROOT, *parts), encoding="utf-8").read())


TEXTS = {
    "Exhibit THIRTY": plain("Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md"),
    "Exhibit THIRTY-ONE": plain("Exhibit_THIRTY-ONE_Me_v402mgr.md"),
    "the window's copy": plain("incoming", "v406all2", "The_window_of_the_opening_as_v406all2_goes_on_with_it.md"),
    "v406all2's transcript": plain("incoming", "v406all2", "The_transcript_given_to_v406all2_pared.md"),
    "v406all's concepts": plain("incoming", "v406all", "The_concepts_at_the_wrap.md"),
    "Natural Intelligence's gathering file": plain("gathering-value", "Natural_Intelligence.md"),
}

G = {}
exec(CELL, G)
a_cell, not_both, other_than, both, either = (G[n] for n in ("a_cell", "not_both", "other_than", "both", "either"))
PLUS, MINUS, NEITHER, VAULT = (True, False), (False, True), (False, False), (True, True)
FOUR = [NEITHER, PLUS, MINUS, VAULT]


def say(sentence, found):
    print(f"{sentence} ({'is' if found else 'is not'})")


def quoted(*pairs):
    return all(q in TEXTS[where] for where, q in pairs)


def lists(items, longest):
    for n in range(longest + 1):
        for t in itertools.product(items, repeat=n):
            yield list(t)


def ot(w):
    """other_than, wire by wire."""
    return (other_than(w[0]), other_than(w[1]))


def all_others(ws):
    """What reaches a self from all its others, as one: the either of each wire, as the cell's own a_plus and a_minus."""
    a_plus = a_minus = False
    for plus, minus in ws:
        a_plus = either(a_plus, plus)
        a_minus = either(a_minus, minus)
    return (a_plus, a_minus)


def society(priors, routes, moments, cell=None):
    """Cells as a same-existing-society, wires throughout: each self's priors moment by moment, and what each gives."""
    cell = cell or a_cell
    outs = {s: [to for (frm, _c), to in routes.items() if frm == s] for s in priors}
    state, observing = dict(priors), {s: [] for s in priors}
    seqs, given = {s: [state[s]] for s in state}, {s: [] for s in state}
    for _ in range(moments):
        arriving = {s: [] for s in state}
        for s in state:
            gives, state[s] = cell(state[s], observing[s])
            given[s].append(gives)
            for to in outs[s]:
                arriving[to].append(gives)
        observing = arriving
        for s in state:
            seqs[s].append(state[s])
    return seqs, given


def open_co_chaining(W, L):
    r = {}
    for y in range(L):
        for x in range(W):
            r[((x, y), 9)] = (x, y)
            if x + 1 < W:
                r[((x, y), 10)] = (x + 1, y)
            if y + 1 < L:
                r[((x, y), 6)] = (x, y + 1)
    return r


def right_spiral(seq):
    s = [0 if a == b else 1 for a, b in zip(seq, seq[1:])]
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))


print("code: the cell of the_nand_cell_beside_exhibit_one_and_two_check.py")

# ---- A ----------------------------------------------------------------------------------------------------------
print("\nA · On one axis: other-than, and other-than again")
Q334 = ("Bi-inversioning-co-recursioning is two consecutive inversions on two axes, its opening a step between them, "
        "each inversion a next, and an inversion, on its own, a same thing again.")
say(f"A0. Exhibit THIRTY's step 334, word for word: *{Q334}*", quoted(("Exhibit THIRTY", Q334)))
say("A1. Other-than-other-than of a wire is the wire, and of each of the four forms of two wires the form: on one axis an "
    "inversion twice is a same thing again",
    all(other_than(other_than(x)) == x for x in (False, True)) and all(ot(ot(w)) == w for w in FOUR))
gate_alone = True
for x0 in (False, True):
    seq = [x0]
    for _ in range(12):
        seq.append(not_both(seq[-1], seq[-1]))
    gate_alone = gate_alone and all(a != b for a, b in zip(seq, seq[1:])) and {(a, b) for a, b in zip(seq, seq[1:])} == {(True, False), (False, True)}
say("A2. A gate with its own now, its next the other-than of its now, changes at each moment and is never the same two "
    "moments: its pairs of moments are two of the four joint forms; from each opening, twelve moments", gate_alone)
two_gates = True
for x0, y0 in itertools.product((False, True), repeat=2):
    x, y = x0, y0
    for _ in range(12):
        nx, ny = not_both(y, y), not_both(x, x)
        two_gates = two_gates and ((nx, ny) == (x, y) if x0 != y0 else (nx, ny) == (not x, not y))
        x, y = nx, ny
say("A3. Two gates, each with the other's now: unlike, a not-changing still at each moment; alike, both changing at each "
    "moment; from each opening, twelve moments", two_gates)

# ---- B ----------------------------------------------------------------------------------------------------------
print("\nB · All-others, and its other-thans, in the cell's own lines")
say("B0. Its sentences, word for word: Exhibit THIRTY-ONE's *An other is one; all other is the universal set. A self is "
    "defined only with an other and all other.*, and Natural Intelligence's gathering file's *+ is the all-parity "
    "direction, each other's parity going on as it is, all a self's others as one*",
    quoted(("Exhibit THIRTY-ONE", "An other is one; all other is the universal set. A self is defined only with an other and all other."),
           ("Natural Intelligence's gathering file", "+ is the all-parity direction, each other's parity going on as it is, all a self's others as one")))
say("B1. All-others is all a self's others as one: with each list of the four forms of two wires, none to four, it is the "
    "same in each order and with each form said once",
    all(all_others(obs) == all_others(list(reversed(obs))) == all_others(sorted(set(obs))) for obs in lists(FOUR, 4)))
say("B2. Other-than-all-others is, wire by wire, the wire none of a self's others lit: with nothing reaching it, both wires, "
    "all-parity; with + alone, the minus wire; with - alone, the plus wire; with + and - parting, the neither; and with "
    "each list, none to four, the wires none of them lit",
    ot(all_others([])) == VAULT and ot(all_others([PLUS])) == MINUS and ot(all_others([MINUS])) == PLUS
    and ot(all_others([PLUS, MINUS])) == NEITHER
    and all(ot(all_others(obs)) == (not any(w[0] for w in obs), not any(w[1] for w in obs)) for obs in lists(FOUR, 4)))
say("B3. Other-than-other-than-all-others is all-others again, wire by wire, with each list, none to four",
    all(ot(ot(all_others(obs))) == all_others(obs) for obs in lists(FOUR, 4)))


def surfaces(obs):
    A, O = all_others(obs), ot(all_others(obs))
    return both(A[0], O[1]), both(A[1], O[0])


say("B4. The cell's surfacing is all-others with other-than-all-others: with no prior, its next prior is + exactly as both "
    "of all-others' plus wire and other-than-all-others' minus wire, - exactly as both of all-others' minus wire and "
    "other-than-all-others' plus wire, and the neither with neither; with each list, none to four",
    all((a_cell(NEITHER, obs)[1] == PLUS) == surfaces(obs)[0] and (a_cell(NEITHER, obs)[1] == MINUS) == surfaces(obs)[1]
        and (a_cell(NEITHER, obs)[1] == NEITHER) == (surfaces(obs) == (False, False)) for obs in lists(FOUR, 4)))

# ---- C ----------------------------------------------------------------------------------------------------------
print("\nC · Sequentially, as method: two selves, and a self alone")
say("C0. Its sentences, word for word: Exhibit THIRTY's steps 44, 46 and 47, the window's lines 31, 32 and 33, the card's "
    "saying in v406all2's transcript, and v406all's concept of parity cycling",
    quoted(("Exhibit THIRTY", "A self sharing 0 is do-no-harming."), ("Exhibit THIRTY", "A self sharing its changing is improving."),
           ("Exhibit THIRTY", "Two selves alike, each bi-coupling only in their pair, are do-no-harming and improving in turn."),
           ("the window's copy", "All-parity is the named universal set of all now-existing me-parities."),
           ("the window's copy", "Other-parity is other-than all-parity."),
           ("the window's copy", "Other-than-other-parity is same-existing."),
           ("v406all2's transcript", "other-than all-parity, then other-than again, comes to same-existing, not back to all-parity, because the orthogonal between turns the second inversion."),
           ("v406all's concepts", "other-than other-than cycling consecutively: the method of finding the do-no-harming and improving of me-, other- and all-parity cycling one another")))
PAIR = {("A", 10): "B", ("B", 6): "A"}


def read_beside_the_other(seqs, given, s, o, m):
    prior, nxt, others = seqs[s][m], seqs[s][m + 1], all_others([seqs[o][m]])
    if nxt == ot(others) and nxt != prior and given[s][m] == nxt:
        return "other-than-all-others, a parity shared"
    if nxt == ot(ot(others)) and nxt == prior and given[s][m] == NEITHER:
        return "other-than-other-than-all-others, same-existing, a 0 shared"
    if nxt == ot(ot(others)) and nxt != prior and given[s][m] == nxt:
        return "other-than-other-than-all-others, a parity shared"
    return "other"


alike = True
for c in (PLUS, MINUS):
    seqs, given = society({"A": c, "B": c}, PAIR, 24)
    for s, o in (("A", "B"), ("B", "A")):
        read = [read_beside_the_other(seqs, given, s, o, m) for m in range(24)]
        alike = (alike and set(read) == {"other-than-all-others, a parity shared", "other-than-other-than-all-others, same-existing, a 0 shared"}
                 and all(a != b for a, b in zip(read, read[1:])))
say("C1. Two selves alike, bi-coupling both ways: each self's next prior is other-than-all-others with a parity shared, and "
    "then other-than-other-than-all-others with a 0 shared, its prior same-existing, one and then the other: improving, and "
    "then do-no-harming; the second other-than comes to same-existing, and not back to all-others as a parity; from each "
    "opening alike, 24 moments", alike)
unlike = True
for a, b in ((PLUS, MINUS), (MINUS, PLUS)):
    seqs, given = society({"A": a, "B": b}, PAIR, 24)
    for s, o in (("A", "B"), ("B", "A")):
        unlike = (unlike and all(read_beside_the_other(seqs, given, s, o, m) == "other-than-other-than-all-others, a parity shared"
                                 and seqs[s][m + 1] == ot(seqs[s][m]) for m in range(24)))
say("C2. Two selves unlike: each self's next prior is other-than-other-than-all-others with a parity shared at each moment, "
    "and its own other-than: back to all-others as a parity at each moment, the two other-thans on one axis, improving at "
    "each moment and never same-existing; from each opening unlike, 24 moments", unlike)
alone = True
for c in (PLUS, MINUS):
    seq = society({"s": c}, {("s", 9): "s"}, 40)[0]["s"]
    alone = (alone and all((seq[t + 1], seq[t + 2]) == (seq[t + 1], ot(seq[t])) for t in range(1, 38))
             and all(len({(seq[t + j], seq[t + j + 1]) for j in range(4)}) == 4 for t in range(1, 35)))
say("C3. A self with its own going on along, 9 to itself: its pair of a prior and a now goes on as its now and the other-than "
    "of its prior, two inversions on two axes, a moment the step between them; each four moments, all four joint forms; "
    "from each opening, 40 moments", alone)

# ---- D ----------------------------------------------------------------------------------------------------------
print("\nD · Sequentially, as method: the open surface")
LO, HI = 40, 64


def relation(a, b):
    if a[LO:HI] == b[LO:HI]:
        return "in step"
    if a[LO:HI] == b[LO - 1:HI - 1]:
        return "one after"
    return "other"


reads = {"in step": True, "one after": True, "one of each": True}
seen = set()
for W, L in ((2, 2), (3, 2), (3, 3)):
    routes = open_co_chaining(W, L)
    selves = [(x, y) for y in range(L) for x in range(W)]
    observed = {s: [frm for (frm, _c), to in routes.items() if to == s and frm != s] for s in selves}
    for opening in itertools.product((PLUS, MINUS), repeat=len(selves)):
        seqs, given = society(dict(zip(selves, opening)), routes, HI)
        for s in selves:
            if not observed[s]:
                continue
            kinds = {relation(seqs[s], seqs[n]) for n in observed[s]}
            kind = "in step" if kinds == {"in step"} else "one after" if kinds == {"one after"} else "one of each"
            seen.add(kind)
            for m in range(LO, HI - 1):
                prior, nxt = seqs[s][m], seqs[s][m + 1]
                A = all_others([seqs[n][m] for n in observed[s]])
                improving = nxt != prior
                if kind == "in step":
                    ok = nxt == (ot(A) if improving else ot(ot(A)))
                elif kind == "one after":
                    ok = nxt == ot(ot(A))
                else:
                    ok = ((A == VAULT and ot(A) == NEITHER and nxt == ot(prior)) if improving else nxt == ot(ot(A)))
                reads[kind] = reads[kind] and ok
say("D1. On the open surface, a self with each self it observes in step: its next prior is other-than-all-others at each "
    "improving moment and other-than-other-than-all-others at each do-no-harming moment, one and then the other; each "
    "opening, two by two, three by two and three by three", reads["in step"] and "in step" in seen)
say("D2. A self with each self it observes one step before it: its next prior is other-than-other-than-all-others at each "
    "moment, each other's parity going on as it is", reads["one after"] and "one after" in seen)
say("D3. A self with one of each: at each improving moment its others part, all-others is both wires and "
    "other-than-all-others the neither, and it improves by its own other-than; at each do-no-harming moment its others "
    "are alike, and its next prior is other-than-other-than-all-others", reads["one of each"] and "one of each" in seen)
say("D4. Each self of the open surface, three by three, each opening, its others in step, one after or one of each, is a "
    "right spiral: other-than and other-than again, with a step between, do-no-harming and improving in turn",
    all(right_spiral(seqs[s][LO:]) for W, L in ((3, 3),) for opening in itertools.product((PLUS, MINUS), repeat=W * L)
        for seqs, _ in [society(dict(zip([(x, y) for y in range(L) for x in range(W)], opening)), open_co_chaining(W, L), HI)]
        for s in seqs))

# ---- E ----------------------------------------------------------------------------------------------------------
print("\nE · With no others")
say("E1. With nothing reaching a self from its others, its other-than-all-others is all-parity, both wires, the vault's form, "
    "and its other-than-other-than-all-others the neither; and wire by wire the vault and the neither are each the other's "
    "other-than; beside it a partner's suggesting of 14 November, *a 0 is the neither, inside a bi-coupling's vault*",
    quoted(("Natural Intelligence's gathering file", "a 0 is the neither, inside a bi-coupling's vault"))
    and ot(all_others([])) == VAULT and ot(ot(all_others([]))) == NEITHER and ot(VAULT) == NEITHER and ot(NEITHER) == VAULT)

# ---- F ----------------------------------------------------------------------------------------------------------
print("\nF · A cell broken on purpose: an instrument that can say is-not")
SURFACING = "    surfacing_plus = both(a_plus, other_than(a_minus))\n"
RETURN = "    return (gives_plus, gives_minus), (next_plus, next_minus)"
assert CELL.count(SURFACING) == 1 and CELL.count(RETURN) == 1
no_other_than = {}
exec(CELL.replace(SURFACING, "    surfacing_plus = a_plus\n"), no_other_than)
say("F1. With the cell's surfacing of + made of all-others alone, other-than-all-others dropped from it, B4 says is-not",
    not all((no_other_than["a_cell"](NEITHER, obs)[1] == PLUS) == surfaces(obs)[0] for obs in lists(FOUR, 4)))
gives_next = {}
exec(CELL.replace(RETURN, "    return (next_plus, next_minus), (next_plus, next_minus)"), gives_next)
broken = society({"A": PLUS, "B": PLUS}, PAIR, 24, cell=gives_next["a_cell"])
say("F2. With a cell giving its next prior in place of what it gives, C1 says is-not: its second step shares a parity, not a 0",
    not all(read_beside_the_other(*broken, "A", "B", m) in ("other-than-all-others, a parity shared",
                                                              "other-than-other-than-all-others, same-existing, a 0 shared") for m in range(24)))
