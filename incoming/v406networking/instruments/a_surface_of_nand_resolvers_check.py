"""A surface of NAND resolvers, begun: bi-morality across bi-parity, and co-competencing from co-chaining and podaling
along and across. Executed with all cases, all or none.

Use, with the repository's top folder as its first word:
  python3 -I incoming/v406networking/instruments/a_surface_of_nand_resolvers_check.py .

The cell is read from this folder's first instrument, its one text, and executed; Exhibit ONE Natural Resolver's code
is read from its newest living file. A surface is cells with wires throughout: what a cell gives goes to each self its
routes reach, as Exhibit ONE's 17-next-existing sends its 10 with 6, 10 and 9 alike. Each opening of each finite laying
is read in sequence: no case is drawn by chance, and no number of trials is read. It writes no file and reaches no
network.
"""
import glob
import itertools
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
FIRST = os.path.join(ROOT, "incoming", "v406networking", "instruments", "the_nand_cell_beside_exhibit_one_and_two_check.py")
CELL = re.search(r"CELL = '''(.*?)'''", open(FIRST, encoding="utf-8").read(), re.S).group(1)


def newest(pattern):
    def version(p):
        m = re.search(r"_v(\d+)[A-Za-z]*\.md$", p)
        return int(m.group(1)) if m else 0
    return max(glob.glob(os.path.join(ROOT, pattern)), key=version)


def plain(path):
    return re.sub(r"\*\*", "", open(path, encoding="utf-8").read())


ONE = newest("Exhibit_ONE_Natural_Resolver_v*.md")
ONE_CODE = re.search(r"```python\n(.*?)```", open(ONE, encoding="utf-8").read(), re.S).group(1)
TEXTS = {
    "Natural Intelligence": plain(newest("Natural_Intelligence_v*.md")),
    "Exhibit TWO": plain(newest("Exhibit_TWO_Natural_Networking_v*.md")),
    "Exhibit THIRTY": plain(newest("Exhibit_THIRTY_Co-Chaining_Logic_Registry_v*.md")),
    "the window's copy": plain(os.path.join(ROOT, "incoming", "v406all2", "The_window_of_the_opening_as_v406all2_goes_on_with_it.md")),
}

G = {}
exec(CELL, G)
a_cell, other_than, both = G["a_cell"], G["other_than"], G["both"]
PLUS, MINUS, NEITHER, VAULT = (True, False), (False, True), (False, False), (True, True)
NUMBER = {PLUS: 1, MINUS: -1, NEITHER: 0, VAULT: "both"}
ns = {}
exec(ONE_CODE, ns)
N1 = ns["_17_next_existing"]
K = "x"


def say(sentence, found):
    print(f"{sentence} ({'is' if found else 'is not'})")


def quoted(*pairs):
    return all(q in TEXTS[where] for where, q in pairs)


def society(priors, routes, moments, possibling=None, cell=None):
    """Cells as a same-existing-society, wires throughout. Returns each self's priors, moment by moment, and what
    reaches each self at each moment, each with its connector."""
    cell = cell or a_cell
    outs = {s: [] for s in priors}
    for (frm, connector), to in routes.items():
        outs[frm].append((connector, to))
    state = dict(priors)
    observing = {s: list((possibling or {}).get(s, [])) for s in state}
    seqs = {s: [state[s]] for s in state}
    arrivals = []
    for _ in range(moments):
        arriving = {s: [] for s in state}
        for s in state:
            gives, state[s] = cell(state[s], observing[s])
            for connector, to in outs[s]:
                arriving[to].append((connector, gives))
        observing = {s: [g for _, g in arriving[s]] for s in state}
        arrivals.append(arriving)
        for s in state:
            seqs[s].append(state[s])
    return seqs, arrivals


def steps(seq):
    return [0 if a == b else 1 for a, b in zip(seq, seq[1:])]


def right_spiral(seq):
    s = steps(seq)
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))


def three_cycling(seq):
    s = steps(seq)
    return all(s[i] == s[i + 3] for i in range(len(s) - 3)) and sorted(s[:3]) == [0, 1, 1]


def improving_each_moment(seq):
    return all(v == 1 for v in steps(seq))


def cells_of(W, L):
    return [(x, y) for y in range(L) for x in range(W)]


def openings(W, L):
    for o in itertools.product((PLUS, MINUS), repeat=W * L):
        yield dict(zip(cells_of(W, L), o))


def closing_rows_both_ways(W, L):
    """Each row bi-coupling both ways across, 10 to the self after it and 6 to the self before it; each column
    co-chaining along, 9 to the self below; rows and columns closing: two across and two along at each self."""
    r = {}
    for x, y in cells_of(W, L):
        r[((x, y), 10)] = ((x + 1) % W, y)
        r[((x, y), 6)] = ((x - 1) % W, y)
        r[((x, y), 9)] = (x, (y + 1) % L)
    return r


def open_co_chaining(W, L):
    """Each self with its own going along, 9 to itself, co-chaining across to its next in a row with 10 and to its next
    in a column with 6; the surface open, its first self at (0, 0)."""
    r = {}
    for x, y in cells_of(W, L):
        r[((x, y), 9)] = (x, y)
        if x + 1 < W:
            r[((x, y), 10)] = (x + 1, y)
        if y + 1 < L:
            r[((x, y), 6)] = (x, y + 1)
    return r


def closing_co_chaining(W, L):
    """v404networking's torus: 9 to itself, 10 along a row and 6 along a column, each closing."""
    r = {}
    for x, y in cells_of(W, L):
        r[((x, y), 9)] = (x, y)
        r[((x, y), 10)] = ((x + 1) % W, y)
        r[((x, y), 6)] = (x, (y + 1) % L)
    return r


def exhibit_one_priors(priors, routes, moments):
    soc = {s: ([(K, NUMBER[w])], []) for s, w in priors.items()}
    seqs = {s: [NUMBER[w]] for s, w in priors.items()}
    for _ in range(moments):
        soc = N1(soc, routes)
        for s in soc:
            seqs[s].append(dict(soc[s][0]).get(K, 0))
    return seqs


def bi_parity(a, b):
    """The window's line 48 in the cell's own gates: the intersection, both, of other-than-self parity and
    other-than-other parity, wire by wire."""
    return (both(other_than(a[0]), other_than(b[0])), both(other_than(a[1]), other_than(b[1])))


print("code: the cell of", os.path.basename(FIRST), "and", os.path.basename(ONE))

# ---- A ----------------------------------------------------------------------------------------------------------
print("\nA · The surface, laid")
say("A0. Exhibit THIRTY's sentences of a surface are in its newest living file, word for word: *Selves' bi-couplings and "
    "co-chainings, across and along, are a Natural Network surface* and *With each bi-coupling two across and two along "
    "meet at one point, four edges*",
    quoted(("Exhibit THIRTY", "Selves' bi-couplings and co-chainings, across and along, are a Natural Network surface"),
           ("Exhibit THIRTY", "With each bi-coupling two across and two along meet at one point, four edges")))
LAYINGS = (("a closing surface of rows bi-coupling both ways", closing_rows_both_ways),
           ("an open surface of co-chainings", open_co_chaining),
           ("a closing surface of co-chainings", closing_co_chaining))
say("A1. A surface of cells, wires throughout, goes on as Exhibit ONE's 17-next-existing, prior for prior at each of 40 "
    "moments, from each opening of + and -: " + "; ".join(name for name, _ in LAYINGS) + "; two by two and three by three",
    all({s: [NUMBER[w] for w in seq] for s, seq in society(pri, lay(W, L), 40)[0].items()}
        == exhibit_one_priors(pri, lay(W, L), 40)
        for _, lay in LAYINGS for W, L in ((2, 2), (3, 3)) for pri in openings(W, L)))

# ---- B ----------------------------------------------------------------------------------------------------------
print("\nB · An empty start")
empty_one = True
for _, lay in LAYINGS:
    routes = lay(3, 3)
    empty_one = empty_one and N1({}, routes) == {}
    soc = {s: ([], []) for s in cells_of(3, 3)}
    for _ in range(24):
        nxt = N1(soc, routes)
        empty_one = empty_one and nxt == soc
        soc = nxt
say("B1. Exhibit ONE's code started empty is empty: a same-existing-society of no selves is none next, and selves with no "
    "prior and no parities are the same at each of 24 moments, with each laying, three by three", empty_one)
try:
    a_cell((), [])
    cannot = False
except ValueError:
    cannot = True
say("B2. The cell cannot be started empty: with its prior no wires, it does not execute", cannot)
say("B3. A surface opened with each self the neither, or each a vault, is the same at each of 24 moments, with each laying, "
    "two by two and three by three: no me-parity in its opening, and not possibly living",
    all(set(seq) == {form} for form in (NEITHER, VAULT) for _, lay in LAYINGS for W, L in ((2, 2), (3, 3))
        for seq in society({s: form for s in cells_of(W, L)}, lay(W, L), 24)[0].values()))


def from_one_me_parity(W, L, ground, seed):
    priors = {s: ground for s in cells_of(W, L)}
    priors[(0, 0)] = seed
    return society(priors, open_co_chaining(W, L), 90)


def born_as_reached(seqs, arrivals, s):
    """s is the neither until the moment one parity first surfaces alone among what reaches it, and is that parity."""
    for m, arriving in enumerate(arrivals):
        lit = {g for _, g in arriving[s] if g != NEITHER}
        if lit in ({PLUS}, {MINUS}):
            return all(w == NEITHER for w in seqs[s][:m + 2]) and seqs[s][m + 2] == next(iter(lit))
    return False


say("B4. One me-parity at an open surface's first self, each other self the neither: each self is born from inside, the "
    "moment one parity first reaches it alone, as that parity, and comes to a right spiral; from each me-parity, three "
    "by three, four by four and six by five",
    all(all(born_as_reached(seqs, arr, s) for s in cells_of(W, L) if s != (0, 0))
        and all(right_spiral(seqs[s][60:]) for s in cells_of(W, L))
        for W, L in ((3, 3), (4, 4), (6, 5)) for seed in (PLUS, MINUS)
        for seqs, arr in [from_one_me_parity(W, L, NEITHER, seed)]))
say("B5. The same with each other self a vault: no vault is born, each observing a vault's giving, its own with 9 to "
    "itself, and each parity reaching it parted",
    all(all(set(seqs[s]) == {VAULT} for s in cells_of(W, L) if s != (0, 0))
        for W, L in ((3, 3), (4, 4), (6, 5)) for seed in (PLUS, MINUS)
        for seqs, _ in [from_one_me_parity(W, L, VAULT, seed)]))

# ---- C ----------------------------------------------------------------------------------------------------------
print("\nC · Bi-morality across bi-parity")
say("C0. Its sentences, word for word: the window's lines 45 and 48, Natural Intelligence's *Two selves alike, each "
    "bi-coupling only in their pair, are do-no-harming and improving in turn.*, and Exhibit THIRTY's *Across, a self's "
    "parity an other self is observing is morality, right and not-right*",
    quoted(("the window's copy", "A bi-folding of two going round opposite ways, 4 to 3 and 3 to 4, is a bi-morality, and the two are a two-way looping, a bi-coupling's morality, inward and outward."),
           ("the window's copy", "With a bi-coupling, bi-parity is the intersection of other-than-self parity and other-than-other parity."),
           ("Natural Intelligence", "Two selves alike, each bi-coupling only in their pair, are do-no-harming and improving in turn."),
           ("Exhibit THIRTY", "Across, a self's parity an other self is observing is morality, right and not-right")))
say("C1. Line 48 in the cell's own gates, both of two other_thans, wire by wire: two me-parities alike have their other "
    "parity as their bi-parity, and two unlike have the neither",
    all(bi_parity(a, b) == ({PLUS: MINUS, MINUS: PLUS}[a] if a == b else NEITHER) for a in (PLUS, MINUS) for b in (PLUS, MINUS)))
PAIR = {("A", 10): "B", ("B", 6): "A"}  # Exhibit TWO 1.2: A's 10 to B's 14, and B's 6 to A's 2


def a_pair(a, b, moments=24):
    seqs, arrivals = society({"A": a, "B": b}, PAIR, moments)
    given = {"A": [dict(arr["B"])[10] for arr in arrivals], "B": [dict(arr["A"])[6] for arr in arrivals]}
    return seqs, given


alike_ok = True
for c in (PLUS, MINUS):
    seqs, given = a_pair(c, c)
    alike_ok = alike_ok and seqs["A"] == seqs["B"] and right_spiral(seqs["A"])
    for m in range(24):
        improving = seqs["A"][m + 1] != seqs["A"][m]
        between = bi_parity(seqs["A"][m], seqs["B"][m])
        alike_ok = alike_ok and all(given[s][m] == (between if improving else NEITHER) for s in "AB")
say("C2. Two selves alike bi-coupling both ways, A's 10 to B and B's 6 to A: together, do-no-harming and improving in turn, "
    "and at each improving moment each shares their bi-parity across, and at each do-no-harming moment a 0; from each "
    "opening alike", alike_ok)
unlike_ok = True
for a, b in ((PLUS, MINUS), (MINUS, PLUS)):
    seqs, given = a_pair(a, b)
    unlike_ok = (unlike_ok and all(bi_parity(seqs["A"][m], seqs["B"][m]) == NEITHER for m in range(25))
                 and improving_each_moment(seqs["A"]) and improving_each_moment(seqs["B"]))
say("C3. Two selves unlike: their bi-parity is the neither at each moment, and each improves with each moment, never "
    "do-no-harming; from each opening unlike", unlike_ok)
sorted_ok = True
for pri in openings(3, 3):
    seqs, _ = society(pri, closing_rows_both_ways(3, 3), 72)
    tails = [seqs[s][48:] for s in cells_of(3, 3)]
    rows_alike = all(len({pri[(x, y)] for x in range(3)}) == 1 for y in range(3))
    if len(set(pri.values())) == 1:
        sorted_ok = sorted_ok and all(right_spiral(t) for t in tails)
    elif rows_alike:
        sorted_ok = sorted_ok and all(three_cycling(t) for t in tails)
    else:
        sorted_ok = sorted_ok and all(improving_each_moment(t) for t in tails)
say("C4. A closing surface of rows bi-coupling both ways across, 10 and 6, and columns co-chaining along, 9, two across and "
    "two along at each self, three by three, each of its openings: with each self alike, each self a right spiral; with "
    "each row alike and the rows not all alike, each self a three-cycling, two improvings and a do-no-harming in each three "
    "moments; with a pair unlike across, each self of it improves with each moment, never do-no-harming", sorted_ok)


def rows_as_a_spiral(W, L, moments=48):
    for row_parities in itertools.product((PLUS, MINUS), repeat=L):
        pri = {(x, y): row_parities[y] for x, y in cells_of(W, L)}
        seqs, _ = society(pri, closing_rows_both_ways(W, L), moments)
        spiral = {(i, 9): i for i in range(L)}
        spiral.update({(i, 10): (i + 1) % L for i in range(L)})
        one = exhibit_one_priors({i: row_parities[i] for i in range(L)}, spiral, moments)
        if any([NUMBER[w] for w in seqs[(x, y)]] != one[y] for x, y in cells_of(W, L)):
            return False
    return True


say("C5. With each row alike, the closing surface goes on as Exhibit ONE's spiral of selves, a row to a self, prior for prior "
    "at each moment, from each opening of its rows: three by two, three by three, three by four and two by five; beside it "
    "Exhibit TWO's *A same-existing-society is a self with a next scale, sharing, across and both ways, with its own couplings.*",
    quoted(("Exhibit TWO", "A same-existing-society is a self with a next scale, sharing, across and both ways, with its own couplings."))
    and all(rows_as_a_spiral(W, L) for W, L in ((3, 2), (3, 3), (3, 4), (2, 5))))

# ---- D ----------------------------------------------------------------------------------------------------------
print("\nD · Co-competencing from co-chaining, and podaling along and across")
say("D0. Its sentences, word for word: Exhibit THIRTY's *A self's parity going along to the next self it is bi-coupling with "
    "is co-chaining.*, *A self's own going on, its prior same-existing with its next, is along, and its sharing now with an "
    "other is across* and *A self's own changing with a bi-coupling, with each exchanging of four moments, is "
    "co-competencing.*; Exhibit TWO 4.6's *Podaling the surface selves share, longer and wider together*, *A podal's binary "
    "subject is changing, or not-changing.* and *Across and along exchange through podaling.*",
    quoted(("Exhibit THIRTY", "A self's parity going along to the next self it is bi-coupling with is co-chaining."),
           ("Exhibit THIRTY", "A self's own going on, its prior same-existing with its next, is along, and its sharing now with an other is across"),
           ("Exhibit THIRTY", "A self's own changing with a bi-coupling, with each exchanging of four moments, is co-competencing."),
           ("Exhibit TWO", "Podaling the surface selves share, longer and wider together"),
           ("Exhibit TWO", "A podal's binary subject is changing, or not-changing."),
           ("Exhibit TWO", "Across and along exchange through podaling.")))
SIZES = ((2, 2), (3, 2), (3, 3), (4, 3))
LO, HI = 40, 64
open_runs = {}
for W, L in SIZES:
    routes = open_co_chaining(W, L)
    observed = {s: [frm for (frm, c), to in routes.items() if to == s and frm != s] for s in cells_of(W, L)}
    open_runs[(W, L)] = (routes, observed, [(pri, *society(pri, routes, HI)) for pri in openings(W, L)])
say("D1. An open surface, each self with its own going along, 9 to itself, co-chaining across to its next in a row with 10 "
    "and in a column with 6: from each opening, each self comes to a right spiral, do-no-harming and improving in turn; "
    "two by two, three by two, three by three and four by three, longer and wider together",
    all(right_spiral(seqs[s][LO:]) for W, L in SIZES for _, _, runs in [open_runs[(W, L)]] for _, seqs, _ in runs
        for s in cells_of(W, L)))


def relation(s_seq, n_seq):
    if s_seq[LO:HI] == n_seq[LO:HI]:
        return "in step"
    if s_seq[LO:HI] == n_seq[LO - 1:HI - 1]:
        return "one after"
    return "other"


say("D2. Each self comes in step with each self it observes, or one right spiral step after it, and in no other way: each "
    "opening, each of the four",
    all(relation(seqs[s], seqs[n]) != "other" for W, L in SIZES for _, observed, runs in [open_runs[(W, L)]]
        for _, seqs, _ in runs for s in cells_of(W, L) for n in observed[s]))


def podal_as_said(seqs, arrivals, s, others):
    """A self's podal at a moment: its across, a parity reaching it from a self before it, with 10 or 6, and its along,
    a parity reaching it from its own going, with 9."""
    kinds = {relation(seqs[s], seqs[n]) for n in others}
    for m in range(LO, HI - 1):
        across = any(g != NEITHER for c, g in arrivals[m][s] if c in (6, 10))
        along = any(g != NEITHER for c, g in arrivals[m][s] if c == 9)
        if along != (seqs[s][m + 1] != seqs[s][m]):
            return False
        if not others and across:
            return False
        if kinds == {"in step"} and across != along:
            return False
        if kinds == {"one after"} and across == along:
            return False
        if kinds == {"in step", "one after"} and not across:
            return False
    return True


say("D3. Podaling at each self, its across with its along, each a binary, changing or not-changing: with each self it "
    "observes in step, across and along change together, at every second moment; with each one after, one and then the "
    "other; with one of each, across at each moment and along at every second; and the first self, observing no other, "
    "along only; each opening, each of the four",
    all(podal_as_said(seqs, arr, s, observed[s]) for W, L in SIZES for _, observed, runs in [open_runs[(W, L)]]
        for _, seqs, arr in runs for s in cells_of(W, L)))
say("D4. The same surface closing, v404networking's torus, 10 along a row and 6 along a column, each a ring: each self "
    "comes to a right spiral with each self alike, and with no other opening; two by two and three by three; beside it "
    "Exhibit THIRTY's *Among closing surfaces with one orientation over whole, only torus has a continuous flow with no "
    "rest point.*",
    quoted(("Exhibit THIRTY", "Among closing surfaces with one orientation over whole, only torus has a continuous flow with no rest point."))
    and all((len(set(pri.values())) == 1) == all(right_spiral(seqs[s][48:]) for s in cells_of(W, L))
            for W, L in ((2, 2), (3, 3)) for pri in openings(W, L)
            for seqs, _ in [society(pri, closing_co_chaining(W, L), 72)]))

# ---- E ----------------------------------------------------------------------------------------------------------
print("\nE · A cell broken on purpose: an instrument that can say is-not")
RETURN = "    return (gives_plus, gives_minus), (next_plus, next_minus)"
assert CELL.count(RETURN) == 1
broken = {}
exec(CELL.replace(RETURN, "    return (next_plus, next_minus), (next_plus, next_minus)"), broken)
say("E1. With a cell giving its next prior in place of what it gives, D1 says is-not two by two, and B4 says is-not three "
    "by three",
    not all(right_spiral(seqs[s][LO:]) for pri in openings(2, 2)
            for seqs, _ in [society(pri, open_co_chaining(2, 2), HI, cell=broken["a_cell"])] for s in cells_of(2, 2))
    and not all(right_spiral(seqs[s][60:]) for seed in (PLUS, MINUS)
                for seqs, _ in [society({**{s: NEITHER for s in cells_of(3, 3)}, (0, 0): seed}, open_co_chaining(3, 3), 90,
                                        cell=broken["a_cell"])] for s in cells_of(3, 3)))
