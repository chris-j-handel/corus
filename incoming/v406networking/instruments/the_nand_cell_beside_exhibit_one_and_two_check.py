"""The NAND cell beside Exhibit ONE Natural Resolver and Exhibit TWO Natural Networking, executed with all cases, all or none.

Use, with the repository's top folder as its first word:
  python3 -I incoming/v406networking/instruments/the_nand_cell_beside_exhibit_one_and_two_check.py .

It reads Exhibit ONE Natural Resolver's newest living file, Exhibit TWO Natural Networking's newest, and the
v404networking instrument, and executes each as it is. The cell is a partner's code of 22 November, its lines as
given, with one line added: its return. Its one gate is not-both, given as its four cases; other_than, both and
either are made of it, and the cell does nothing else with its parities. A parity is two wires: + is the plus wire
lit alone, - the minus wire lit alone, and a 0 neither. No case is drawn by chance and no number of trials is read:
each case of a finite laying is read in sequence, and each sentence says is or is not.

To execute the v404networking instrument with cells, it writes one page, Exhibit ONE's code with the cell after it,
into a temporary folder, removed after. It writes nothing in the repository and reaches no network.
"""
import glob
import io
import itertools
import os
import re
import subprocess
import sys
import tempfile
import tokenize

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."


def newest(pattern):
    def version(p):
        m = re.search(r"_v(\d+)[A-Za-z]*\.md$", p)
        return int(m.group(1)) if m else 0
    return max(glob.glob(os.path.join(ROOT, pattern)), key=version)


ONE = newest("Exhibit_ONE_Natural_Resolver_v*.md")
TWO = newest("Exhibit_TWO_Natural_Networking_v*.md")
ONE_CODE = re.search(r"```python\n(.*?)```", open(ONE, encoding="utf-8").read(), re.S).group(1)
TWO_TEXT = open(TWO, encoding="utf-8").read()
NETWORKING = os.path.join(ROOT, "incoming", "v404networking", "instruments", "each_case_of_a_self_and_its_others_check.py")

# ---- The one gate and the cell. One text, executed here and inside the v404networking instrument. ----
CELL = '''
NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def not_both(a, b):
    return NOT_BOTH[(a, b)]


def other_than(a):
    return not_both(a, a)


def both(a, b):
    return other_than(not_both(a, b))


def either(a, b):
    return not_both(other_than(a), other_than(b))


def a_cell(prior, observing):
    a_plus = a_minus = False
    for plus, minus in observing:
        a_plus = either(a_plus, plus)
        a_minus = either(a_minus, minus)
    surfacing_plus = both(a_plus, other_than(a_minus))
    surfacing_minus = both(a_minus, other_than(a_plus))
    prior_plus, prior_minus = prior
    no_prior = both(other_than(prior_plus), other_than(prior_minus))
    gives_plus = either(both(no_prior, surfacing_plus), both(prior_minus, other_than(surfacing_minus)))
    gives_minus = either(both(no_prior, surfacing_minus), both(prior_plus, other_than(surfacing_plus)))
    next_plus = either(gives_plus, both(prior_plus, surfacing_plus))
    next_minus = either(gives_minus, both(prior_minus, surfacing_minus))
    return (gives_plus, gives_minus), (next_plus, next_minus)  # the one line added: what it gives, and its next prior
'''

# ---- Exhibit ONE's 1-now-existing by cells: the same lists in and out, each 4-now-co-same-existing its own cell. ----
# Numbers become wires at the edge and wires become numbers at the edge; every parity between is the cell's.
BY_CELLS = '''
WIRES = {1: (True, False), -1: (False, True), 0: (False, False)}
PARITY = {(True, False): 1, (False, True): -1, (False, False): 0, (True, True): "both"}
NONE = (False, False)


def wires(v):
    return WIRES[1 if v > 0 else -1 if v < 0 else 0]


def now_existing_by_cells(_3_now_co_observing, _2_now_possibling):
    prior = dict(_3_now_co_observing)
    observing, surfacing_order = {}, []
    for key, v in _2_now_possibling:
        observing.setdefault(key, []).append(wires(v))
        if wires(v) != NONE and key not in surfacing_order:
            surfacing_order.append(key)
    keys = surfacing_order + [key for key in prior if key not in surfacing_order]
    gives, nexts = {}, {}
    for key in keys:
        gives[key], nexts[key] = a_cell(wires(prior[key]) if key in prior else NONE, observing.get(key, []))
    ten = [(key, PARITY[gives[key]]) for key in keys]
    eleven = [(key, PARITY[nexts[key]]) for key in prior]
    eleven += [(key, PARITY[nexts[key]]) for key in keys if key not in prior and nexts[key] != NONE]
    return ten, eleven
'''


def exhibit_one():
    ns = {}
    exec(ONE_CODE, ns)
    return ns


def by_cells(cell=CELL):
    """Exhibit ONE's own 9-next-co-discovering and 17-next-existing, its wiring as it is, each self resolved by cells."""
    ns = {}
    exec(ONE_CODE, ns)
    exec(cell, ns)
    exec(BY_CELLS, ns)
    ns["_1_now_existing"] = ns["now_existing_by_cells"]
    return ns


def say(sentence, found):
    print(f"{sentence} ({'is' if found else 'is not'})")


def lists(items, longest):
    """Each list of the items, none to longest, in each order."""
    for n in range(longest + 1):
        for t in itertools.product(items, repeat=n):
            yield list(t)


G = {}
exec(CELL, G)
exec(BY_CELLS, G)
a_cell, WIRES, PARITY, NONE = G["a_cell"], G["WIRES"], G["PARITY"], G["NONE"]
PLUS, MINUS, BOTH = (True, False), (False, True), (True, True)
FOUR = [NONE, PLUS, MINUS, BOTH]
NAMES = {NONE: "none", PLUS: "+", MINUS: "-", BOTH: "both"}
K = "x"


def inverse(w):
    return {PLUS: MINUS, MINUS: PLUS}[w]


def lit(ws):
    """Python's own operators, outside the cell, as a second hand: is a plus and is a minus wire lit in any of ws."""
    return any(w[0] for w in ws), any(w[1] for w in ws)


print("code:", os.path.basename(ONE), "and", os.path.basename(TWO))

# ---- A ----------------------------------------------------------------------------------------------------------
print("\nA · One gate")
two = list(itertools.product((False, True), repeat=2))
say("A1. not-both is lit with each way of two wires but one, both lit",
    [G["not_both"](a, b) for a, b in two] == [True, True, True, False])
say("A2. other_than, not-both of a wire with itself, is its other",
    all(G["other_than"](a) is (not a) for a in (False, True)))
say("A3. both, other_than of not-both, is lit with both lit and with no other way",
    all(G["both"](a, b) is (a and b) for a, b in two))
say("A4. either, not-both of two other_thans, is lit with one or both lit, and dark with both dark",
    all(G["either"](a, b) is (a or b) for a, b in two))
cell_lines = CELL[CELL.index("def a_cell"):]
words = {t.string for t in tokenize.generate_tokens(io.StringIO(cell_lines).readline) if t.type in (tokenize.NAME, tokenize.OP)}
say("A5. The cell's own lines do nothing with a parity but the gate: no and, or, not, if, else, is, comparing or counting",
    not words & {"and", "or", "not", "if", "else", "is", "==", "!=", "<", ">", "<=", ">=", "+", "-", "*", "~", "&", "|", "^"})

# ---- B ----------------------------------------------------------------------------------------------------------
print("\nB · The cell beside Exhibit ONE's 1-now-existing")
E1 = exhibit_one()["_1_now_existing"]
C1 = by_cells()["_1_now_existing"]


def one_sharing_the_same(now):
    return all(E1(prior, received) == now(prior, received)
               for prior in ([], [(K, 1)], [(K, -1)])
               for received in lists([(K, 1), (K, -1), (K, 0)], 5))


say("B1. With one 4-now-co-same-existing, a prior +, - or none, and each list of received parities +, - and 0, none to five, "
    "in each order: the cell's two returns are Exhibit ONE's two, 10-next-co-possibling and 11-next-co-observing, item for item and in order",
    one_sharing_the_same(C1))
priors_of_two = ([[]] + [[(k, v)] for k in "xy" for v in (1, -1)]
                 + [[(a, u), (b, w)] for a, b in (("x", "y"), ("y", "x")) for u in (1, -1) for w in (1, -1)])
say("B2. With two 4-now-co-same-existings, each prior of each, in both orders, and each list of received parities none to four: "
    "the same, each sharing its own cell",
    all(E1(prior, received) == C1(prior, received)
        for prior in priors_of_two
        for received in lists([(k, v) for k in "xy" for v in (1, -1, 0)], 4)))
print("B3. The cell's sixteen ways: a prior, by what surfaces from its observing, with what it gives and its next prior")
SEEN = {"nothing": [], "+ alone": [PLUS], "- alone": [MINUS], "+ and - parting": [PLUS, MINUS]}
for prior in FOUR:
    row = " · ".join(f"{seen}: gives {NAMES[g]}, next {NAMES[n]}" for seen, obs in SEEN.items() for g, n in [a_cell(prior, obs)])
    print(f"   prior {NAMES[prior]:4} | {row}{'   (a prior Exhibit ONE has no form of)' if prior == BOTH else ''}")

# ---- C ----------------------------------------------------------------------------------------------------------
print("\nC · Cells as a network beside Exhibit ONE's 17-next-existing")
N1 = exhibit_one()["_17_next_existing"]
NC = by_cells()["_17_next_existing"]


def chain(n):
    r = {(i, 9): i for i in range(n)}
    r.update({(i, 10): i + 1 for i in range(n - 1)})
    return r


def spiral(n, own=True):
    r = {(i, 9): i for i in range(n)} if own else {}
    r.update({(i, 10): (i + 1) % n for i in range(n)})
    return r


def torus(side):
    r = {}
    for s in range(side * side):
        x, y = s % side, s // side
        r[(s, 9)] = s
        r[(s, 10)] = y * side + (x + 1) % side
        r[(s, 6)] = ((y + 1) % side) * side + x
    return r


def goes_on_the_same(n, routes, moments, next_by_cells=None):
    """From each opening, Exhibit ONE's same-existing-society and the cells' go on, each its own, the same at each moment."""
    next_by_cells = next_by_cells or NC
    for opening in itertools.product((1, -1), repeat=n):
        one = {i: ([(K, opening[i])], []) for i in range(n)}
        cells = {i: ([(K, opening[i])], []) for i in range(n)}
        for _ in range(moments):
            one, cells = N1(one, routes), next_by_cells(cells, routes)
            if one != cells:
                return False
    return True


say("C1. A self with 9-next-co-discovering to itself and with none of its others: from each opening, the same at each of forty moments",
    goes_on_the_same(1, {(0, 9): 0}, 40))
say("C2. Two selves bi-coupling both ways, 6-now-co-possibling each to the other: the same, each opening, forty moments",
    goes_on_the_same(2, {(0, 6): 1, (1, 6): 0}, 40))
say("C3. A chain of one to eight selves, 9 to itself and 10 to its next: the same, each opening, each moment",
    all(goes_on_the_same(n, chain(n), 2 * n + 24) for n in range(1, 9)))
say("C4. A spiral of two to eight selves, 10 to its next and its last to its first, with 9 to itself and with none: the same",
    all(goes_on_the_same(n, spiral(n, own), 2 * n + 24) for n in range(2, 9) for own in (True, False)))
say("C5. A torus of two by two and of three by three selves, 9 to itself, 10 along a row and 6 along a column: the same",
    all(goes_on_the_same(s * s, torus(s), 2 * s * s + 24) for s in (2, 3)))


def its_sentences(root):
    out = subprocess.run([sys.executable, "-I", NETWORKING, root], capture_output=True, text=True, check=True).stdout
    return out.splitlines()[1:]  # its first line names the code it read


with tempfile.TemporaryDirectory() as there:
    with open(os.path.join(there, "Exhibit_ONE_Natural_Resolver_v999cells.md"), "w", encoding="utf-8") as f:
        f.write("```python\n" + ONE_CODE + CELL + BY_CELLS + "\n_1_now_existing = now_existing_by_cells\n```\n")
    with_one, with_cells = its_sentences(ROOT), its_sentences(there)
say("C6. The v404networking instrument, executed with cells in Exhibit ONE's place, says each of its sentences, "
    "and the same is or is not of each, as with Exhibit ONE's code",
    bool(with_one) and with_one == with_cells)
found = [m.groups() for m in (re.match(r"(\d+(?:\.\d+)?)\.? .*\((is|is not)\)$", line) for line in with_cells) if m]
print("   with cells: " + " · ".join(f"{n} {v}" for n, v in found))

# ---- D ----------------------------------------------------------------------------------------------------------
print("\nD · Exhibit TWO's sentences of a self's resolving, executed with the cell")
QUOTES = {
    "D1": "with a prior + and no parity a self is observing, each shares −",
    "D2": "with a prior +1 and a +1 a self is observing, ten shares 0, its prior same-existing +1 with 11, and six shares one same 0",
    "D3a": "One parity a self is observing agrees with its prior** · *a* 0 · *b* Its prior, same-existing",
    "D3b": "One parity a self is observing, one inversion apart from its prior",
    "D3c": "No parity a self is observing, a prior** · *a* Its prior inverting · *b* Its prior inverting",
    "D3d": "One parity a self is observing, no prior** · *a* That parity · *b* That parity",
    "D4": "two + surface as one + with 14, and against that prior give a 0 alike",
    "D5": "With a 0 a self shares its prior is same-existing; with none and with a 0 it is observing, a self's prior inverts; and parities stay two",
    "D6": "Zero is positive and negative parting, or a prior and a parity same, an empty centre",
    "D7a": "its next priors go two by two, c, c, −c, −c",
    "D7b": "Its (prior, now) pairs are (c, c), (c, −c), (−c, −c), (−c, c)",
    "D8": "map (x,y) → (y,−x) follows consecutive overlapping pairs",
    "D9": "Only parities go across",
}
say("D0. Each quotation below is in Exhibit TWO's newest living file, word for word",
    all(q in TWO_TEXT for q in QUOTES.values()))
say(f"D1. 1.2: *{QUOTES['D1']}*", a_cell(PLUS, [])[0] == MINUS)
say(f"D2. 1.2: *{QUOTES['D2']}*", a_cell(PLUS, [PLUS]) == (NONE, PLUS))
say("D3. 1.4's four ways with one prior, each with what 10 shares and the next prior with 11: agreeing, 0 and its prior; "
    "one inversion apart, that parity twice; no parity, its prior inverting twice; no prior, that parity twice",
    all(a_cell(c, [c]) == (NONE, c) and a_cell(c, [inverse(c)]) == (inverse(c), inverse(c))
        and a_cell(c, []) == (inverse(c), inverse(c)) and a_cell(NONE, [c]) == (c, c) for c in (PLUS, MINUS)))
say(f"D4. 1.4: *{QUOTES['D4']}*; and each list of + and -, one to five, is as its parities said once",
    a_cell(PLUS, [PLUS, PLUS]) == a_cell(PLUS, [PLUS]) == (NONE, PLUS)
    and all(a_cell(p, obs) == a_cell(p, sorted(set(obs))) for p in (NONE, PLUS, MINUS) for obs in lists([PLUS, MINUS], 5) if obs))
say(f"D5. 1.4: *{QUOTES['D5']}*",
    all((g == NONE) == (n == c) and n in (PLUS, MINUS)
        for c in (PLUS, MINUS) for obs in lists([PLUS, MINUS, NONE], 4) for g, n in [a_cell(c, obs)])
    and all(a_cell(c, obs)[1] == inverse(c) for c in (PLUS, MINUS) for obs in ([], [NONE], [NONE, NONE])))
say(f"D6. 1.6: *{QUOTES['D6']}*: with a prior, it gives nothing exactly with the prior's own parity surfacing alone; "
    "with no prior and parities observed, exactly with + and - parting",
    all((a_cell(c, obs)[0] == NONE) == ({w for w in obs if w != NONE} == {c}) for c in (PLUS, MINUS) for obs in lists([PLUS, MINUS, NONE], 4))
    and all((a_cell(NONE, obs)[0] == NONE) == ({w for w in obs if w != NONE} == {PLUS, MINUS})
            for obs in lists([PLUS, MINUS, NONE], 4) if any(w != NONE for w in obs)))
spiral_of_one = []
for c in (1, -1):
    soc, seq = {0: ([(K, c)], [])}, [c]
    for _ in range(40):
        soc = NC(soc, {(0, 9): 0})
        seq.append(dict(soc[0][0])[K])
    spiral_of_one.append(seq)
say(f"D7. Smaller fold within one through nine: *{QUOTES['D7a']}*, and *{QUOTES['D7b']}*: cells, from each opening",
    all(all(s[i] == s[i + 1] != s[i + 2] for i in range(1, 38, 2))
        and all(len({(s[i + j], s[i + j + 1]) for j in range(4)}) == 4 for i in range(1, 36)) for s in spiral_of_one))
say(f"D8. Binary stable-forming: *{QUOTES['D8']}*: with cells, each (prior, now) pair goes on as (now, the prior's other)",
    all((s[i + 1], s[i + 2]) == (s[i + 1], -s[i]) for s in spiral_of_one for i in range(1, 38)))
say(f"D9. 1.4: *{QUOTES['D9']}*: from a prior of none, + or -, with each list of the four ways of two wires, none to four, "
    "what a cell gives is a +, a - or nothing, and never both",
    all(a_cell(p, obs)[0] != BOTH for p in (NONE, PLUS, MINUS) for obs in lists(FOUR, 4)))

# ---- E ----------------------------------------------------------------------------------------------------------
print("\nE · What the cell opens")
everything = [(p, obs) for p in FOUR for obs in lists(FOUR, 3)]


def surfacing(obs):
    a_plus, a_minus = lit(obs)
    return a_plus and not a_minus, a_minus and not a_plus


say("E1. Each wire of the next prior is chosen by the prior's other wire: next plus is, with the prior's minus wire lit, "
    "the other of surfacing minus, and else surfacing plus; next minus is, with the prior's plus wire lit, the other of "
    "surfacing plus, and else surfacing minus; each prior of four, each list of the four ways of two wires, none to three",
    all(a_cell(p, obs)[1] == ((not sm) if p[1] else sp, (not sp) if p[0] else sm)
        for p, obs in everything for sp, sm in [surfacing(obs)]))
say("E2. From a prior of none, + or -, with each list of the four ways of two wires, none to four, no next prior is both wires lit",
    all(a_cell(p, obs)[1] != BOTH for p in (NONE, PLUS, MINUS) for obs in lists(FOUR, 4)))
say("E3. A prior of both wires gives and goes on as a prior + and a prior - at once, each wire the either of the two: "
    "with each list of the four ways of two wires, none to three",
    all(a_cell(BOTH, obs) == tuple(lit([a_cell(PLUS, obs)[i], a_cell(MINUS, obs)[i]]) for i in (0, 1)) for obs in lists(FOUR, 3)))
say("E4. A prior of both wires is both until one parity surfaces alone, and then it is that parity; with none surfacing "
    "it gives both wires, and a self observing them has + and - parting",
    all(a_cell(BOTH, obs)[1] == (PLUS if surfacing(obs)[0] else MINUS if surfacing(obs)[1] else BOTH) for obs in lists(FOUR, 3))
    and a_cell(BOTH, [])[0] == BOTH and a_cell(NONE, [BOTH]) == a_cell(NONE, [PLUS, MINUS])
    and all(a_cell(c, [BOTH]) == a_cell(c, [PLUS, MINUS]) for c in (PLUS, MINUS)))


def alone(c, wired_with_next, moments=24):
    """One cell with its own wiring to itself: what it gives, or its next prior, is what it observes next."""
    prior, observing, seq = WIRES[c], [], [c]
    for _ in range(moments):
        gives, nxt = a_cell(prior, observing)
        observing, prior = [nxt if wired_with_next else gives], nxt
        seq.append(PARITY[prior])
    return seq


say("E5. What goes across is what a cell gives: wired with what it gives, a cell with its own wiring to itself goes two by two, "
    "as Exhibit ONE's self with 9-next-co-discovering to itself; wired with its next prior, it is the same with each moment "
    "after its first, a not-changing still; from each opening",
    all(alone(c, False) == spiral_of_one[i][:25] and len(set(alone(c, True)[1:])) == 1 for i, c in enumerate((1, -1))))
counted, tally = {}, [0]
exec(CELL, counted)
gate = counted["not_both"]


def counting(a, b):
    tally[0] += 1
    return gate(a, b)


counted["not_both"] = counting


def gates(k):
    tally[0] = 0
    counted["a_cell"](PLUS, [PLUS] * k)
    return tally[0]


say("E6. As written, a cell is 36 not-both gates, and 6 more with each parity it observes: none to eight",
    all(gates(k) == 36 + 6 * k for k in range(9)))

# ---- F ----------------------------------------------------------------------------------------------------------
print("\nF · The instrument with a cell broken on purpose: an instrument that can say is-not")
HELD = "    next_plus = either(gives_plus, both(prior_plus, surfacing_plus))\n"
RETURN = "    return (gives_plus, gives_minus), (next_plus, next_minus)"
assert CELL.count(HELD) == 1 and CELL.count(RETURN) == 1
BROKEN = {
    "the same-existing of + wired to its prior's minus wire": CELL.replace(HELD, HELD.replace("prior_plus", "prior_minus")),
    "giving its next prior in place of what it gives": CELL.replace(RETURN, "    return (next_plus, next_minus), (next_plus, next_minus)"),
}
for i, (what, broken) in enumerate(BROKEN.items(), 1):
    ns = by_cells(broken)
    say(f"F{i}. With a cell broken on purpose, {what}, B1 says is-not and C3 says is-not",
        not one_sharing_the_same(ns["_1_now_existing"])
        and not all(goes_on_the_same(n, chain(n), 2 * n + 24, ns["_17_next_existing"]) for n in range(1, 9)))

# ---- G ----------------------------------------------------------------------------------------------------------
print("\nG · A partner's saying of 22 November, re-said: all birthing of me-parities is from inside all-parity vaults,"
      " and the vault is not possibly living")
CCL = open(os.path.join(ROOT, "gathering-value", "Co-Chaining_Logic_Registry.md"), encoding="utf-8").read()
NI = open(os.path.join(ROOT, "gathering-value", "Natural_Intelligence.md"), encoding="utf-8").read()
BESIDE = {
    "81": (CCL, "Inside, a conceiving is in a bi-coupling of two of the society's selves: the vault, all-parity now, a 0, bi-tri-bi, 8 and 16."),
    "82": (CCL, "A new self's birthing is its inheriting, by its two same-as. By its two other-than nothing is inherited: a 0, an opening."),
    "84": (CCL, "A new me-parity is one of the ingesting society's selves, one scale inward: living, an other-than-all-parity, after all-parity only."),
    "14 November": (NI, "a 0 is the neither, inside a bi-coupling's vault"),
}
VAULT, NEITHER = BOTH, NONE


def society(priors, routes, moments, possibling=None):
    """Cells as a same-existing-society, wires throughout, each self's prior two wires. What a cell gives goes to each
    self its routes reach, as Exhibit ONE's 17-next-existing sends its 10 with 6, 10 and 9 alike."""
    state = dict(priors)
    observing = {s: list((possibling or {}).get(s, [])) for s in state}
    seqs = {s: [state[s]] for s in state}
    for _ in range(moments):
        arriving = {s: [] for s in state}
        for s in list(state):
            gives, state[s] = a_cell(state[s], observing[s])
            for (frm, _connector), to in routes.items():
                if frm == s:
                    arriving[to].append(gives)
        observing = arriving
        for s in state:
            seqs[s].append(state[s])
    return seqs


def exhibit_one_priors(opening, routes, moments):
    soc = {i: ([(K, opening[i])], []) for i in range(len(opening))}
    seqs = {i: [opening[i]] for i in range(len(opening))}
    for _ in range(moments):
        soc = N1(soc, routes)
        for i in soc:
            seqs[i].append(dict(soc[i][0]).get(K, 0))
    return seqs


def changing_and_changing_back(seq):
    same = [a == b for a, b in zip(seq, seq[1:])]
    return all(same[i] != same[i + 1] for i in range(len(same) - 1))


say("G0. Each quotation of this part is in its gathering file word for word: the Co-Chaining Logic Registry's 81, 82 and 84, "
    "and Natural Intelligence's, of a partner's suggesting of 14 November",
    all(q in text for text, q in BESIDE.values()))
say("G1. A society of cells with wires throughout goes on as Exhibit ONE's, prior for prior at each moment, from each opening "
    "of + and -: a chain and a spiral of one to six selves",
    all({i: [PARITY[w] for w in seq] for i, seq in society({i: WIRES[o] for i, o in enumerate(opening)}, routes, 30).items()}
        == exhibit_one_priors(opening, routes, 30)
        for n in range(1, 7) for routes in [chain(n)] + ([spiral(n)] if n > 1 else [])
        for opening in itertools.product((1, -1), repeat=n)))
quiet = [obs for obs in lists(FOUR, 3) if surfacing(obs) == (False, False)]
layings = [(1, {(0, 9): 0}), (1, {})] + [(n, chain(n)) for n in (2, 3, 4)] + [(n, spiral(n)) for n in (2, 3, 4)] + [(4, torus(2))]
say("G2. The vault, both wires lit, and the neither, both wires dark, are each a not-changing still while no parity surfaces "
    "alone, not possibly living: with each list of the four ways of two wires, none to three, with no parity alone in it, "
    "the vault gives both wires, a 0 at each self observing it, and is the vault, and the neither gives nothing and is the "
    "neither; and a self with its own wiring to itself or with none, a chain, a spiral and a torus, each self of it a vault, "
    "or each the neither, is the same at each of 24 moments",
    all(a_cell(VAULT, obs) == (BOTH, BOTH) and a_cell(NEITHER, obs) == (NONE, NONE) for obs in quiet)
    and all(set(seq) == {form} for form in (VAULT, NEITHER) for n, routes in layings
            for seq in society({i: form for i in range(n)}, routes, 24).values()))
say("G3. A me-parity comes from the vault or the neither only by one parity surfacing alone, and is that parity as it is; "
    "with no parity alone, each is itself: with each list of the four ways of two wires, none to four",
    all(a_cell(p, obs)[1] == (PLUS if surfacing(obs)[0] else MINUS if surfacing(obs)[1] else p)
        for p in (VAULT, NEITHER) for obs in lists(FOUR, 4)))


def its_two(obs):
    return a_cell(PLUS, obs)[1], a_cell(MINUS, obs)[1]


say(f"G4. 82: *{BESIDE['82'][1]}*: the vault is a prior + and a prior - at once; with each list of the four ways of two "
    "wires, none to four, its two come to the same exactly with one parity surfacing alone, and the vault is then that "
    "me-parity; with its two other-than it gives both wires, a 0, and is the vault again, an opening",
    all((a_cell(VAULT, obs)[1] == its_two(obs)[0]) == (its_two(obs)[0] == its_two(obs)[1])
        and (its_two(obs)[0] == its_two(obs)[1]) == (surfacing(obs) != (False, False))
        and (its_two(obs)[0] == its_two(obs)[1] or a_cell(VAULT, obs) == (BOTH, BOTH)) for obs in lists(FOUR, 4)))
born = True
for c in (PLUS, MINUS):
    for poss in ([], [PLUS], [MINUS]):
        seqs = society({"self": c, "vault": VAULT}, {("self", 9): "self", ("self", 10): "vault"}, 40, {"self": poss})
        own, inside = seqs["self"], seqs["vault"]
        t = next((i for i, w in enumerate(inside) if w in (PLUS, MINUS)), None)
        gave = next(m for m in range(1, len(own)) if own[m] != own[m - 1])  # the self gives a parity first as it inverts
        born = (born and t == gave + 1 and inside[t] == own[gave] and all(w == VAULT for w in inside[:t])
                and inside[t:] == own[t:] and changing_and_changing_back(inside[t:]))
say(f"G5. 84: *{BESIDE['84'][1]}*: a vault observing a self with its own wiring to itself is the vault until a parity "
    "reaches it alone, is born that moment as that parity, and from then on is in step with that self, a right spiral, "
    "its prior changing and changing back; from each opening of the self, its prior + or - with nothing, + or - observed", born)
say("G6. A vault observing its own giving is never born: its own both wires part each parity reaching it, with each list of "
    "others' wires, none to three; and observing itself and a self beside it, it is the vault at each of forty moments, "
    "from each opening of that self",
    all(a_cell(VAULT, [BOTH] + obs) == (BOTH, BOTH) for obs in lists(FOUR, 3))
    and all(set(society({"self": c, "vault": VAULT}, {("self", 9): "self", ("self", 10): "vault", ("vault", 9): "vault"}, 40)["vault"]) == {VAULT}
            for c in (PLUS, MINUS)))
say("G7. No me-parity goes back into a vault, or to the neither: from + or -, with each list of the four ways of two wires, "
    "none to four, the next prior is + or -",
    all(a_cell(c, obs)[1] in (PLUS, MINUS) for c in (PLUS, MINUS) for obs in lists(FOUR, 4)))
say("G8. Exhibit ONE's code has no vault: each prior of a chain and a spiral of one to six selves, from each opening of + and -, "
    "at each of 30 moments, is + or -; and its only first prior is "
    "at a 4 with no item in 3, the neither: with one 4-now-co-same-existing and each list of received parities, none to "
    "five, a first prior comes exactly with one parity surfacing alone, as it is",
    all(set(v for seq in exhibit_one_priors(opening, routes, 30).values() for v in seq) <= {1, -1}
        for n in range(1, 7) for routes in [chain(n)] + ([spiral(n)] if n > 1 else [])
        for opening in itertools.product((1, -1), repeat=n))
    and all((dict(E1([], received)[1]).get(K) is not None) == (len({v for _, v in received if v}) == 1)
            and dict(E1([], received)[1]).get(K) in (None, *{v for _, v in received if v})
            for received in lists([(K, 1), (K, -1), (K, 0)], 5)))
