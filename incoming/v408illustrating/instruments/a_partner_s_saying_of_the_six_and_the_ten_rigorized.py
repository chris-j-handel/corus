"""v408illustrating · a partner's saying of 25 November, of the six and the ten, rigorized: its is and its is-not, executed.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/a_partner_s_saying_of_the_six_and_the_ten_rigorized.py .

The saying, in this session's words: the six view of the prime resolving form is the changing; the ten view is the stable
forming; and the both of the two is same-existing with prior, now, next and other-prior.
Executed here: the form's own table from its page; four things' six pairs and five things' ten pairs; the ten as the six
and four more, and as 6 and 3 and 1; a partner's ten of 23 November beside it; and the sentences beside it, word for word.
A seating, which column is which pair and which row is which pair, is a naming: no line here executes it.
Whole numbers alone. It opens the living files and two sessions' pages, and writes none. All or none.
"""
import itertools, re, sys
from pathlib import Path

FOUR = ("prior", "now", "next", "other-prior")                    # a partner's four; the lean line's moments are a me's now and its other's prior, and a moment on its prior and its now
NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}
def lean(me_now, other_prior):                                    # the lean line, v407nanding's, as it is
    return me_now, NOT_BOTH[(other_prior, other_prior)]
BOTH_NOW = "now, a second observing"                              # a fifth: a now both, co-momentarying and bi-momentarying
pairs = lambda things: list(itertools.combinations(things, 2))
def turned(orders, things):
    """The rounds of a set of things turned by orders of three: a thing with all it is turned to."""
    seen, rounds = set(), []
    for t in things:
        if t not in seen:
            r = {o(t) for o in orders}; seen |= r; rounds.append(len(r))
    return sorted(rounds)

if __name__ == "__main__":
    root = Path(sys.argv[1])
    text = lambda f: (root / f).read_text(encoding="utf-8")
    results = []
    def line(name, ok): results.append((name, bool(ok)))

    # ---------- the form's own table, from its page ----------
    form = text("incoming/v407primes/The_prime_resolving_form.md")
    rows = [[c.strip() for c in l.strip("|").split("|")] for l in form.split("\n") if l.startswith("| **")]
    named = sum(bool(c) for r in rows for c in r[1:7])
    line("the form's table, from its page: ten rows and six columns, 34 cells named and 26 with none named",
         len(rows) == 10 and all(len(r) == 7 for r in rows) and (named, 60 - named) == (34, 26))
    line("by the form's own words a column is a prime living and a row is one of ten unchangeables: the six are three pairs, and the ten are five bi-couplings",
         all(s in form for s in ("Columns: six prime livings, three pairs.", "Five bi-couplings, two faces", "Resolving the Hard Problem Registry's ten unchangeables",
                                 "An interest is one of the ten fixing on one prime living.")))

    # ---------- four, and their six ----------
    six = pairs(FOUR)
    away = {p: [q for q in six if not set(p) & set(q)] for p in six}
    line("four have six pairs, and the six are three pairs: a pair with the one pair of the other two",
         len(six) == 6 and all(len(v) == 1 for v in away.values()) and len({frozenset((p, v[0])) for p, v in away.items()}) == 3)

    # ---------- the lean line's four moments, and their six pairs ----------
    def the_six(me_now, other_prior):
        prior_on, now_on = lean(me_now, other_prior)
        four = {"a me's now": me_now, "its other's prior": other_prior, "its prior a moment on": prior_on, "its now a moment on": now_on}
        return {frozenset(p): four[p[0]] == four[p[1]] for p in itertools.combinations(four, 2)}
    openings = [the_six(a, b) for a in (True, False) for b in (True, False)]
    carried, othered = frozenset(("a me's now", "its prior a moment on")), frozenset(("its other's prior", "its now a moment on"))
    line("the lean line's moments are four, a me's now and its other's prior, and a moment on its prior and its now: of their six pairs one is one thing carried at all openings, one is other-than at all, and four are by turns",
         all(o[carried] and not o[othered] for o in openings) and all(len({o[k] for o in openings}) == 2 for k in openings[0] if k not in (carried, othered)))
    line("at all openings three of the six pairs are other-than and three are not, and of a pair with its far pair one is other-than and one is not: three pairs",
         all(sum(o.values()) == 3 for o in openings) and all(o[k] != o[frozenset(set().union(*o) - k)] for o in openings for k in o))

    # ---------- five, and their ten ----------
    five = FOUR + (BOTH_NOW,)
    ten = pairs(five)
    round_of = lambda order: ({frozenset((order[i], order[(i + 1) % 5])) for i in range(5)})
    sides = round_of(five); diagonals = {frozenset(p) for p in ten} - sides
    far = {s: [d for d in diagonals if not s & d] for s in sides}
    line("five have ten pairs: in a round's order five sides and five diagonals, a side with its one diagonal away from it, five pairs",
         len(ten) == 10 and len(sides) == len(diagonals) == 5 and all(len(v) == 1 for v in far.values()) and len({v[0] for v in far.values()}) == 5)
    line("only with five are the pairs twice the number, stepped to 10,000; with four they are six, the number and two more",
         [n for n in range(1, 10_001) if n * (n - 1) == 4 * n] == [5] and 4 * 3 // 2 == 6)

    # ---------- the ten, by the six ----------
    more = [p for p in ten if BOTH_NOW in p]
    line("the ten are the six and four more: the fifth with prior, with now, with next and with other-prior",
         [p for p in ten if BOTH_NOW not in p] == six and [p[0] for p in more] == list(FOUR) and len(six) + len(more) == 10)
    line("the four more are three and one: the fifth with the three other-than now, and with now; the ten are 6 and 3 and 1",
         (len([p for p in more if "now" not in p[:1]]), len([p for p in more if p[0] == "now"])) == (3, 1))

    # ---------- beside a partner's ten of 23 November, v407primes' form: a unit cube from a corner ----------
    ways = ("up", "forward", "right")
    one, two = [(w,) for w in ways], list(itertools.permutations(ways, 2))
    three = {frozenset(o) for o in itertools.permutations(ways, 3)}
    line("a partner's ten of 23 November, by a unit cube from a corner: three ways of one, six of two in their order, and all orders of three ending at one place: 3 and 6 and 1, number for number",
         (len(one), len(two), len(three)) == (3, 6, 1) and "3 of 3 is the six orders to the far corner ending at one" in form)
    orders = [dict(zip(ways, o)) for o in itertools.permutations(ways)]
    cube_six = turned([lambda t, o=o: tuple(o[w] for w in t) for o in orders], two)
    m = dict(zip(ways, ("prior", "next", "other-prior")))          # the three other-than now, turned as the three ways are
    pair_six = turned([lambda t, o=o: frozenset(m[o[k]] if (k := next((w for w in ways if m[w] == x), None)) else x for x in t) for o in orders], [frozenset(p) for p in six])
    line("is-not, explored: turned by the six orders of three, the cube's six are one round of six, and the pairs' six are two rounds of three; the two sixes are one for one as numbers alone",
         cube_six == [6] and pair_six == [3, 3])

    # ---------- the sentences beside the saying, word for word in their files ----------
    beside = [("Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v402mgr.md", "a hard problem is a changing fixing unchangeable"),
              ("Exhibit_FOUR_Natural_Mathematics_v402mgr.md", "Only with five are couplings twice its number, n(n − 1)/2 = 2n for n = 5, and its ten part as a pentagon's five sides and five diagonals"),
              ("Natural_Intelligence_v402mgr.md", "Same-existing changes in five dimensions, five of a side with its next numbering"),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "its five dimensions, self prior, other prior, co-momentarying now, bi-momentarying now and self next"),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "a face draws one seating, and seatings part with files"),
              ("incoming/v407nanding/The_leanest_resolving.md", "A moment on, a me's prior is its now."),
              ("incoming/v407nanding/The_leanest_resolving.md", "A moment on, a me's now is the other-than of its other's prior.")]
    line("seven sentences beside the saying are word for word in their files: five living, and the lean line's two, v407nanding's",
         all(s in text(f) for f, s in beside))
    registry = text("Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v402mgr.md")
    line("is-not, explored: the ten's seatings part with files: five places 2 to 6 by one, and eight names by another, 5 and 13 with two of the ten and 7 and 15 with two",
         "ten pair with five names 2 to 6" in text("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md")
         and all(s in registry for s in ("a rate fixing as a value, with 7 and 15", "a between fixing as a cut, with 5 and 13", "with 7-now-observing and 15-next-observing", "with 5-now-co-existing and 13-next-discovering")))

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
