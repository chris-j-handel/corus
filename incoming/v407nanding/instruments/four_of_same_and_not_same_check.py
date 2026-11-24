"""v407nanding · four joint forms said by natural explaining: a prior and a now, same or not same, executed.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/four_of_same_and_not_same_check.py .

A partner's saying of 24 November: four joint forms is not yet natural explaining. The one list has joint as resolving
among parities, same or not same. A spiral of one is a me of the twelve lines observing its own next-co-possibling,
opened from this session's file of the now and same-existing me-parity. All or none.
"""
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
text = (root / "incoming/v407nanding/instruments/the_now_and_same_existing_me_parity_check.py").read_text(encoding="utf-8")
ns = {}
exec(re.search(r"CODE = '''(.*?)'''", text, re.S).group(1), ns)
cell, other_than = ns["now_and_same_existing_me_parity"], ns["other_than"]
PLUS, MINUS = (True, False), (False, True)
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


words = re.sub(r"\s+", " ", (root / "incoming/v404mgr/Words_of_no_natural_naming_with_their_natural_naming.md").read_text(encoding="utf-8"))
say("J1. The one list has joint as resolving among parities, same or not same",
    "| *joint*, *meeting* | resolving among parities: same or not same |" in words)


def spiral_of_one(prior, moments=12):
    laid, rows = None, []
    for _ in range(moments):
        out = cell(prior, [] if laid is None else [laid])
        rows.append((prior, out[1]))
        laid, prior = out[0], out[1]
    return rows


def same(prior, now):
    return now == prior


def not_same(prior, now):
    return now == (other_than(prior[0]), other_than(prior[1]))


turns = all([not_same(*r) for r in spiral_of_one(p)] == [True, False] * 6 and [same(*r) for r in spiral_of_one(p)] == [False, True] * 6
            for p in (PLUS, MINUS))
say("J2. A spiral of one's prior and now are not same, then same, by turns, twelve moments, with prior - and with prior +", turns)
four = [(r[1], "same" if same(*r) else "not same") for r in spiral_of_one(MINUS)[:4]]
say("J3. With prior -, its four are + not same, + same, - not same and - same, and round again",
    four == [(PLUS, "not same"), (PLUS, "same"), (MINUS, "not same"), (MINUS, "same")]
    and spiral_of_one(MINUS)[4:8] == spiral_of_one(MINUS)[:4])
pairs = set(spiral_of_one(MINUS)[:4])
say("J4. The four are all the ways a prior and a now are, a parity apiece, same or not same: the four rows of the "
    "not-both table", pairs == set(itertools.product((PLUS, MINUS), repeat=2)))
say("J5. Not same is the other-than of the prior, by the fifteen lines' other-than, a wire apiece, and same is the prior again",
    all(not_same(p, (other_than(p[0]), other_than(p[1]))) and same(p, p) for p in (PLUS, MINUS)))
def observing_none(prior, moments=12):
    rows = []
    for _ in range(moments):
        now = cell(prior, [])[1]
        rows.append((prior, now))
        prior = now
    return rows


say("M1. With a spiral of one observing none, its prior and now are not same at all moments, and J2 says is-not",
    all(all(not_same(*r) for r in observing_none(p)) and [not_same(*r) for r in observing_none(p)] != [True, False] * 6
        for p in (PLUS, MINUS)))
print("\nAll is." if all(results) else "\nNot all is.")
