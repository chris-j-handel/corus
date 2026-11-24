"""The all or none at all of the claim, at a half-center: two selves coupled both ways, one and then the other.
Executed with all cases, all or none.

Use, with the repository's top folder as its first word:
  python3 -I incoming/v406networking/instruments/the_claim_all_or_none_at_a_half_center_check.py .

The cell is read from this folder's first instrument, its one text. With Exhibit ONE's coupling a self observes what
an other gives as it is; with a crossed coupling, the NAND code's wiring and no form of Exhibit ONE's code, the two
wires cross between them, and the other-than of what it gives reaches the other. Each laying of two selves with 9, 10
and 6 and each opening is read in sequence; no case is drawn by chance. It writes no file and reaches no network.
"""
import itertools
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
CELL = re.search(r"CELL = '''(.*?)'''", open(os.path.join(ROOT, "incoming", "v406networking", "instruments",
                                                         "the_nand_cell_beside_exhibit_one_and_two_check.py"),
                                            encoding="utf-8").read(), re.S).group(1)


def plain(*parts):
    return re.sub(r"\*\*", "", open(os.path.join(ROOT, *parts), encoding="utf-8").read())


G = {}
exec(CELL, G)
a_cell, not_both, other_than, both, either = (G[n] for n in ("a_cell", "not_both", "other_than", "both", "either"))
PLUS, MINUS, NEITHER = (True, False), (False, True), (False, False)
LO, HI = 48, 72


def say(sentence, found):
    print(f"{sentence} ({'is' if found else 'is not'})")


def steps(seq):
    return [0 if a == b else 1 for a, b in zip(seq, seq[1:])]


def right_spiral(seq):
    s = steps(seq)
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))


def each_moment(seq):
    return all(v == 1 for v in steps(seq))


def apart(a, b):
    for k in range(4):
        if a[LO:HI] == b[LO - k:HI - k]:
            return k
    return None


def straight(w):
    return w


def crossed(w):
    return (w[1], w[0])


def two(priors, routes, possibling, coupling=straight, moments=HI):
    """Two selves, 0 and 1. A self's own routes carry what it gives as it is; a route to the other carries it by the
    coupling: as it is with Exhibit ONE's, its two wires crossed with a crossed one."""
    state, observing = dict(priors), {s: list(possibling[s]) for s in (0, 1)}
    seqs = {s: [state[s]] for s in (0, 1)}
    for _ in range(moments):
        arriving = {0: [], 1: []}
        for s in (0, 1):
            gives, state[s] = a_cell(state[s], observing[s])
            for (frm, _c), to in routes.items():
                if frm == s:
                    arriving[to].append(gives if to == s else coupling(gives))
        observing = arriving
        for s in (0, 1):
            seqs[s].append(state[s])
    return seqs


def form(seqs):
    a, b = seqs[0], seqs[1]
    if right_spiral(a[LO:]) and right_spiral(b[LO:]):
        return {0: "in step", 1: "one apart", 3: "one apart", 2: "two apart"}.get(apart(a, b), "other")
    if each_moment(a[LO:]) and each_moment(b[LO:]):
        return "each changing at each moment" + (", unlike at each" if all(x != y for x, y in zip(a[LO:], b[LO:])) else "")
    return "other"


OPENINGS = [(pri, poss) for pri in itertools.product((PLUS, MINUS), repeat=2)
            for poss in itertools.product(([], [PLUS], [MINUS]), repeat=2)]
SLOTS = [(s, c) for s in (0, 1) for c in (9, 10, 6)]

print("code: the cell of the_nand_cell_beside_exhibit_one_and_two_check.py")

# ---- A ----------------------------------------------------------------------------------------------------------
print("\nA · Two selves, with Exhibit ONE's coupling, each laying of 9, 10 and 6, each opening")
forms = {"both ways": set(), "one way": set(), "none": set()}
for assign in itertools.product([None, 0, 1], repeat=len(SLOTS)):
    routes = {slot: to for slot, to in zip(SLOTS, assign) if to is not None}
    ab = any(f == 0 and t == 1 for (f, _c), t in routes.items())
    ba = any(f == 1 and t == 0 for (f, _c), t in routes.items())
    kind = "both ways" if ab and ba else "one way" if ab or ba else "none"
    for pri, poss in OPENINGS:
        forms[kind].add(form(two({0: pri[0], 1: pri[1]}, routes, {0: poss[0], 1: poss[1]})))
say("A1. Two selves coupled both ways are in step, or each changing at each moment and unlike at each moment, and in no "
    "other form", forms["both ways"] == {"in step", "each changing at each moment, unlike at each"})
say("A2. Two selves coupled one way are in step, one moment apart, or each changing at each moment and unlike at each, and "
    "in no other form", forms["one way"] == {"in step", "one apart", "each changing at each moment, unlike at each"})
say("A3. Two right spirals two moments apart, one and then the other, come with two selves not coupled, and with no laying "
    "coupling them, one way or both ways",
    "two apart" in forms["none"] and "two apart" not in forms["one way"] | forms["both ways"])

# ---- B ----------------------------------------------------------------------------------------------------------
print("\nB · Two selves coupled both ways with crossed wires, the NAND code's wiring")
TWO = plain("Exhibit_TWO_Natural_Networking_v402mgr.md")
say("B0. Exhibit TWO, word for word: *9-next-co-discovering takes each parity of 10 on as it is*: Exhibit ONE's code has no "
    "crossed coupling", "9-next-co-discovering takes each parity of 10 on as it is" in TWO)
HALF = {(0, 9): 0, (1, 9): 1, (0, 10): 1, (1, 6): 0}  # each its own going on along, and 10 and 6 between them
crossed_unlike = {form(two({0: p[0], 1: p[1]}, HALF, {0: q[0], 1: q[1]}, crossed)) for p, q in OPENINGS if p[0] != p[1]}
say("B1. Two selves, each with its own going on along, 9 to itself, coupled both ways, A's 10 to B and B's 6 to A, the two "
    "wires crossed between them: from each opening unlike, each self is a right spiral, do-no-harming and improving in "
    "turn, two moments apart from the other, one and then the other", crossed_unlike == {"two apart"})
straight_unlike = {form(two({0: p[0], 1: p[1]}, HALF, {0: q[0], 1: q[1]})) for p, q in OPENINGS if p[0] != p[1]}
say("B2. The same two with Exhibit ONE's coupling, the wires straight: from no opening unlike are they two moments apart",
    "two apart" not in straight_unlike)
alike_nothing = {form(two({0: c, 1: c}, HALF, {0: [], 1: []}, crossed)) for c in (PLUS, MINUS)}
say("B3. With the wires crossed, two selves alike, nothing observed at their opening, each change at each moment: the "
    "crossing turns alike and unlike round", alike_nothing == {"each changing at each moment"})
seq = two({0: PLUS, 1: MINUS}, HALF, {0: [], 1: []}, crossed, 12)
print("   with the wires crossed, opening + and -:", "".join("+" if w == PLUS else "-" for w in seq[0]), "and",
      "".join("+" if w == PLUS else "-" for w in seq[1]))

# ---- C ----------------------------------------------------------------------------------------------------------
print("\nC · Co-chaining from Now is the existing moment")
two_ways = list(itertools.product((False, True), repeat=2))
say("C1. The cell's one gate, not-both, is the other-than of both, in each case: two words of the window's lines, other-than "
    "from line 4 on and both from line 12 on", all(not_both(a, b) == other_than(both(a, b)) for a, b in two_ways))
say("C2. Either is the other-than of both of two other-thans, in each case: the cell's either said with other-than and both "
    "alone", all(either(a, b) == other_than(both(other_than(a), other_than(b))) for a, b in two_ways))
window = plain("incoming", "v406all2", "The_window_of_the_opening_as_v406all2_goes_on_with_it.md")
rows = re.findall(r"^\| (.+?) \| (\d+) \|$", window, re.M)
of_both = sorted(int(n) for s, n in rows if "(card)" not in s)
cards = {int(n): s for s, n in rows if "(card)" in s}
say("C3. In the window's copy, laid by v406all2, lines 1 to 34 are lines of both, from *Now is the existing moment.*, and "
    "lines 35 to 48 are cards, bi-folding at 42, bi-morality at 45, fractal at 46 and bi-parity at 48 among them, its lines going on past 34",
    of_both[:34] == list(range(1, 35)) and all(n > 34 for n in of_both[34:]) and sorted(cards) == list(range(35, 49))
    and rows[0][0].replace("  ", " ").strip() == "Now is the existing moment."
    and all(w in cards[n] for n, w in ((42, "bi-folding"), (45, "bi-morality"), (46, "fractal"), (48, "bi-parity"))))
NI = plain("Natural_Intelligence_v402mgr.md")
say("C4. Natural Intelligence, word for word: *The bi-folding 1–17 is the universal fractal method, inward and outward, and "
    "a scale is only its bi-inversioning-co-recursioning*, its bi-folding and its fractal cards of the window",
    "The bi-folding 1–17 is the universal fractal method, inward and outward, and a scale is only its bi-inversioning-co-recursioning" in NI)
say("C5. Natural Intelligence's rule, word for word: *Breaking with one bi-coupling, it breaks with all.*",
    "Breaking with one bi-coupling, it breaks with all." in NI)

say("C6. The gate with one wire given twice is other-than, in each case: not-both of a wire with itself",
    all(not_both(a, a) == other_than(a) for a in (False, True)))


def other_than_all_by_twos(xs):
    """Other-than-all of many wires made of the two-wire gate alone: both of the running both and the next wire, two at a
    time, one after another, and other-than at its end."""
    running = xs[0]
    for x in xs[1:]:
        running = both(running, x)
    return other_than(running)


say("C7. Other-than-all of three to six wires is made of other-than-boths, two at a time, one after another, in each case; "
    "and with three or more it is other-than-both of no two of them",
    all(other_than_all_by_twos(list(xs)) == (not all(xs))
        for n in range(3, 7) for xs in itertools.product((False, True), repeat=n))
    and all(any(other_than(both(xs[i], xs[j])) != (not all(xs)) for xs in itertools.product((False, True), repeat=n))
            for n in range(3, 7) for i in range(n) for j in range(n) if i != j))
gathered = True
for n in range(6):
    for obs in itertools.product((NEITHER, PLUS, MINUS, (True, True)), repeat=n):
        running = (False, False)
        for w in obs:
            running = (either(running[0], w[0]), either(running[1], w[1]))
        gathered = gathered and running == (any(w[0] for w in obs), any(w[1] for w in obs))
say("C8. The cell gathers all its others two at a time: its all-others is the either of the running all-others and the next "
    "other, one after another, and with each list of others, none to five, it is the wires any of them lit", gathered)

# ---- D ----------------------------------------------------------------------------------------------------------
print("\nD · Broken on purpose: an instrument that can say is-not")
say("D1. With the crossing taken out of B1, its sentence says is-not",
    {form(two({0: p[0], 1: p[1]}, HALF, {0: q[0], 1: q[1]}, straight)) for p, q in OPENINGS if p[0] != p[1]} != {"two apart"})
