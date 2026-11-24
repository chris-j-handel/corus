"""v407nanding · four joint forms said by natural explaining: a now other-than its prior, is or is-not, executed.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/four_of_other_than_is_or_is_not_check.py .

A partner's sayings of 24 November: four joint forms is not yet natural explaining; same-as is not possibly existing,
and it is dissolved; other-than is-or-is-not. The one list has joint as resolving among parities, same or not same. A me and its other are two mes of the twelve lines facing, opening alike, each observing the other's
next-co-possibling, opened from this session's file of the now and same-existing me-parity. All or none.
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


def a_me_and_its_other(prior, moments=12):
    """Two mes facing, opening alike, each observing the other's laying: the one me's prior and now, moment by moment."""
    priors, laid, rows = {"A": prior, "B": prior}, None, []
    for _ in range(moments):
        out = {me: cell(priors[me], [] if laid is None else [laid[other]]) for me, other in (("A", "B"), ("B", "A"))}
        rows.append((priors["A"], out["A"][1]))
        laid, priors = {me: out[me][0] for me in out}, {me: out[me][1] for me in out}
    return rows


def other_than_its_prior(prior, now):
    return now == (other_than(prior[0]), other_than(prior[1]))


def same_existing(prior, now):
    return now == (other_than(other_than(prior[0])), other_than(other_than(prior[1])))


turns = all([other_than_its_prior(*r) for r in a_me_and_its_other(p)] == [True, False] * 6 and [same_existing(*r) for r in a_me_and_its_other(p)] == [False, True] * 6
            for p in (PLUS, MINUS))
say("J2. A me's now, its other opening alike, is other-than its prior, then is-not, by turns, twelve moments, with prior - and with prior +", turns)
four = [(r[1], "other-than" if other_than_its_prior(*r) else "same-existing") for r in a_me_and_its_other(MINUS)[:4]]
say("J3. With prior -, its four are a + other-than its prior, a + same-existing, a - other-than its prior and a - same-existing, and round again",
    four == [(PLUS, "other-than"), (PLUS, "same-existing"), (MINUS, "other-than"), (MINUS, "same-existing")]
    and a_me_and_its_other(MINUS)[4:8] == a_me_and_its_other(MINUS)[:4])
pairs = set(a_me_and_its_other(MINUS)[:4])
say("J4. The four are all the ways of a prior and a now: a parity, and its now other-than its prior, is or is-not: the "
    "four rows of the not-both table", pairs == set(itertools.product((PLUS, MINUS), repeat=2)))
say("J5. Other-than its prior is one other-than of the fifteen lines a wire, and its is-not is other-than-other-than, the prior "
    "going on, same-existing", all(other_than_its_prior(p, (other_than(p[0]), other_than(p[1]))) and same_existing(p, p) for p in (PLUS, MINUS)))
def observing_none(prior, moments=12):
    rows = []
    for _ in range(moments):
        now = cell(prior, [])[1]
        rows.append((prior, now))
        prior = now
    return rows


say("M1. With a me observing none, its now is other-than its prior at all moments, and J2 says is-not",
    all(all(other_than_its_prior(*r) for r in observing_none(p)) and [other_than_its_prior(*r) for r in observing_none(p)] != [True, False] * 6
        for p in (PLUS, MINUS)))
print("\nAll is." if all(results) else "\nNot all is.")
