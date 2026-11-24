"""Other-than-other-than-both, one moment after another, and bothbothing between alternating nand-nandings in both
directions: a partner's two sayings of 22 November, executed with the one gate. All cases, all or none.

Use, with the repository's top folder as its first word:
  python3 -I incoming/v406networking/instruments/bothbothing_between_alternating_nand_nandings_check.py .

The gate is read from this folder's first instrument, its one text. Here each gate takes one moment: what it gives
at a moment is of what reached it the moment before. Two gates coupled both ways go at once, each with each moment,
or by turns, one moment after another, one gate and then the other. Each opening and each order is read in sequence;
no case is drawn by chance. It writes no file and reaches no network.
"""
import itertools
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
CELL = re.search(r"CELL = '''(.*?)'''", open(os.path.join(ROOT, "incoming", "v406networking", "instruments",
                                                         "the_nand_cell_beside_exhibit_one_and_two_check.py"),
                                            encoding="utf-8").read(), re.S).group(1)
G = {}
exec(CELL, G)
not_both, other_than, both = G["not_both"], G["other_than"], G["both"]


def plain(*parts):
    return re.sub(r"\*\*", "", open(os.path.join(ROOT, *parts), encoding="utf-8").read())


def say(sentence, found):
    print(f"{sentence} ({'is' if found else 'is not'})")


TWO_WAYS = list(itertools.product((False, True), repeat=2))
print("code: the gate of the_nand_cell_beside_exhibit_one_and_two_check.py")

# ---- A ----------------------------------------------------------------------------------------------------------
print("\nA · Other-than-other-than-both, one moment after another")
say("A0. Exhibit THIRTY's step 334 has *each inversion a next*",
    "each inversion a next" in plain("Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md"))
one_after_another = True
for inputs in itertools.product(TWO_WAYS, repeat=6):
    first = second = True
    firsts, seconds = [], []
    for a, b in inputs:
        first, second = not_both(a, b), not_both(first, first)
        firsts.append(first)
        seconds.append(second)
    one_after_another = (one_after_another and all(firsts[t] == other_than(both(*inputs[t])) for t in range(6))
                         and all(seconds[t + 1] == both(*inputs[t]) for t in range(5)))
say("A1. Two gates one after the other, each a moment: at each moment the first gives the other-than-both of the two wires "
    "of the moment before, and the second gives their both of two moments before; with each going of two wires over six "
    "moments", one_after_another)
say("A2. The value of the cell's both, the other-than of its not-both, is the value of both, in each case: its value alone; "
    "the orthogonal between that the value misses is in A3 and A4",
    all(other_than(not_both(a, b)) == both(a, b) for a, b in TWO_WAYS))

PLUS, MINUS, NEITHER, VAULT = (True, False), (False, True), (False, False), (True, True)
FOUR = [NEITHER, PLUS, MINUS, VAULT]


def lists(items, longest):
    for n in range(longest + 1):
        for t in itertools.product(items, repeat=n):
            yield list(t)


class Wire:
    """A wire's value with the names of the wires it is of, for tracing the cell's own lines."""
    def __init__(self, value, of):
        self.value, self.of = value, frozenset(of)


def traced_cell():
    ns = {}
    exec(CELL, ns)
    table, meetings, inner_both = ns["NOT_BOTH"], [], ns["both"]

    def value(x):
        return x.value if isinstance(x, Wire) else x

    def of(x):
        return x.of if isinstance(x, Wire) else frozenset()

    ns["not_both"] = lambda a, b: Wire(table[(value(a), value(b))], of(a) | of(b))

    def recorded_both(a, b):
        meetings.append((of(a), of(b)))
        return inner_both(a, b)

    ns["both"] = recorded_both
    return ns["a_cell"], meetings


ALONG, ACROSS = {"its prior's plus", "its prior's minus"}, {"its others' plus", "its others' minus"}


def axis(names):
    return "along" if names and names <= ALONG else "across" if names and names <= ACROSS else "along with across"


traced, meetings = traced_cell()
met = set()
for prior in (PLUS, MINUS, NEITHER):
    for obs in ([PLUS], [MINUS], [PLUS, MINUS], [VAULT]):
        meetings.clear()
        traced((Wire(prior[0], {"its prior's plus"}), Wire(prior[1], {"its prior's minus"})),
               [(Wire(a, {"its others' plus"}), Wire(b, {"its others' minus"})) for a, b in obs])
        met.add(tuple(sorted((axis(a), axis(b)) for a, b in meetings)))
        met.add(("two wires each" if all(a != b for a, b in meetings) else "a wire with itself",))
say("A3. Each both of the cell meets two wires, and never one wire with itself: with others observed, two of its nine meet "
    "two wires across, its others' plus and minus; one meets two wires along, its own prior's plus and minus; and six meet "
    "its prior along with what surfaces from its others across; traced through its own lines, with each prior and each way "
    "its others surface",
    met == {tuple(sorted([("across", "across")] * 2 + [("along", "along")] + [("along", "across")] * 6)), ("two wires each",)})


def all_others(ws):
    a_plus = a_minus = False
    for plus, minus in ws:
        a_plus, a_minus = G["either"](a_plus, plus), G["either"](a_minus, minus)
    return a_plus, a_minus


one_of_two = True
for prior in (PLUS, MINUS):
    x = 0 if prior == PLUS else 1
    for obs in lists(FOUR, 4):
        A = all_others(obs)
        surfacing = (both(A[0], other_than(A[1])), both(A[1], other_than(A[0])))
        do_no_harm, improve = both(prior[x], surfacing[x]), both(prior[x], other_than(surfacing[x]))
        gives, nxt = G["a_cell"](prior, obs)
        one_of_two = (one_of_two and do_no_harm != improve and do_no_harm == (gives == NEITHER and nxt == prior)
                      and improve == (nxt != prior and gives == nxt))
say("A4. Within one moment, a self with a prior is one of two, all or none: do-no-harming, the both of its prior's wire and "
    "that wire surfacing alone, a 0 shared and its prior same-existing; or improving, the both of its prior's wire and the "
    "other-than of that surfacing, its prior inverting and the inverted parity shared; never both of the two and never "
    "neither; with each list of its others' wires, none to four", one_of_two)

# ---- B ----------------------------------------------------------------------------------------------------------
print("\nB · Two gates coupled both ways, at once and by turns")


def going(rule, order, x0, y0, first="x", moments=36):
    x, y = x0, y0
    seq = [(x, y)]
    for t in range(moments):
        x_turn = (t % 2 == 0) == (first == "x")
        if order == "at once":
            x, y = rule(y, x), rule(x, y)
        elif x_turn:
            x = rule(y, x)
        else:
            y = rule(x, y)
        seq.append((x, y))
    return seq


def not_both_of_the_other_and_its_own(other, own):
    return not_both(other, own)


def other_than_of_the_other(other, own):
    return not_both(other, other)


ROUND = [(False, True), (False, True), (True, True), (True, False), (True, False), (True, True)]


def goes_round(seq):
    """From moment 12 on, the pair goes round ROUND, from some place in it."""
    tail = seq[12:]
    return any(all(tail[i] == ROUND[(k + i) % 6] for i in range(len(tail))) for k in range(6))


say("B0. Its sentences, word for word: Exhibit EIGHT 1.4's *Both bothboth, one at a time, unrelationing sharing and testing "
    "receiving, and a self co-chains both sides with each observing.*; Exhibit FIVE's *Bounding-zeroing with co-changing, "
    "each side taking its own turn*; and Natural Physics's gathering file's *parity changing alternating, both-bothing, is "
    "where competency and living resolve it*",
    "Both bothboth, one at a time, unrelationing sharing and testing receiving, and a self co-chains both sides with each observing." in plain("Exhibit_EIGHT_Natural_Exploring_v402mgr.md")
    and "Bounding-zeroing with co-changing, each side taking its own turn" in plain("Exhibit_FIVE_Natural_Engineering_v402mgr.md")
    and "parity changing alternating, both-bothing, is where competency and living resolve it" in plain("gathering-value", "Natural_Physics.md"))
by_turns = [going(not_both_of_the_other_and_its_own, "by turns", x0, y0, first)
            for x0, y0 in TWO_WAYS for first in ("x", "y")]
say("B1. Two gates coupled both ways, each the not-both of the other's and its own, by turns, one moment after another: from "
    "each opening, either gate first, the two go round six moments: one gate dark two moments, then both lit, then the "
    "other gate dark two moments, then both lit; never both dark; each dark three moments apart from the other",
    all(goes_round(seq) and (False, False) not in seq[12:] for seq in by_turns))
at_once = [going(not_both_of_the_other_and_its_own, "at once", x0, y0) for x0, y0 in TWO_WAYS]
say("B2. The same two at once, each with each moment: from each opening, alike at each moment and both changing at each "
    "moment, with no one and then the other",
    all(all(x == y for x, y in seq[2:]) and all(a != b for a, b in zip(seq[2:], seq[3:])) for seq in at_once))
fixing = [going(other_than_of_the_other, "by turns", x0, y0, first) for x0, y0 in TWO_WAYS for first in ("x", "y")]
say("B3. Two gates each the other-than of the other alone, by turns: from each opening, either gate first, a not-changing "
    "still, the two unlike, the first fixing kept",
    all(all(p == seq[2] for p in seq[2:]) and seq[2][0] != seq[2][1] for seq in fixing))
print("   by turns, from both dark, each the not-both of the other's and its own:",
      " ".join("".join("1" if v else "0" for v in p) for p in by_turns[0][12:24]))

# ---- C ----------------------------------------------------------------------------------------------------------
print("\nC · Broken on purpose: an instrument that can say is-not")
say("C1. With each gate's own taken from its not-both, each the not-both of the other with itself, B1 says is-not",
    not all(goes_round(seq) for seq in fixing))
say("C2. With the turns made one moment for both, B1 says is-not", not all(goes_round(seq) for seq in at_once))
