"""v407nanding · four bi-foldings into one bi-folding into one next me-parity, executed by the twelve lines' mes.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/four_bi_foldings_into_one_next_me_parity_check.py .

A partner's saying of 24 November: 4 bi foldings into one bi folding into one next me parity as other than other than all
or all. A podaling of a place is one me of the twelve lines, a prior - and the place observed on its minus wire. A fold
is the two podalings, the top place's other-than and all places' other-than, by turns. All or none.
"""
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


def podaling(name, at, k):
    places = [bool((name - 1) >> i & 1) for i in range(k)]
    places = [cell(MINUS, [(False, p)])[0][0] if i in at else p for i, p in enumerate(places)]
    return 1 + sum(1 << i for i, p in enumerate(places) if p)


def round_of(name, k):
    names = [name]
    for at in [{k - 1}, set(range(k))] * 2:
        names.append(podaling(names[-1], at, k))
    return names


def folded(k):
    return sorted({min(round_of(n, k)[:4]) for n in range(1, 2 ** k + 1)})


say("H1. The sixteen names fold into four bi-foldings, and a bi-folding's least name is 1, 2, 3 or 4", folded(4) == [1, 2, 3, 4])
say("H2. The four bi-foldings, as the names 1 to 4, fold by the same two podalings into one bi-folding: 1, 3, 2, 4, and 1 "
    "again", round_of(1, 2) == [1, 3, 2, 4, 1])
say("H3. The one bi-folding folds into one name, 1: sixteen into four and four into one, by the same two podalings at both spans",
    len(folded(4)) == 4 and folded(2) == [1])
say("H4. Inward, the one opens to four bi-foldings and they to the sixteen names, all of them, four rounds of four",
    sorted(n for m in folded(4) for n in round_of(m, 4)[:4]) == list(range(1, 17)))
say("H5. All places' other-than twice is a name again, at all spans of 2 to 64 names: other-than-other-than-all is all",
    all(podaling(podaling(n, set(range(k)), k), set(range(k)), k) == n for k in range(1, 7) for n in range(1, 2 ** k + 1)))


def spiral_of_one(prior, moments=8):
    laid, rows = None, []
    for _ in range(moments):
        out = cell(prior, [] if laid is None else [laid])
        rows.append((prior, out[1]))
        laid, prior = out[0], out[1]
    return rows


rows = spiral_of_one(MINUS)
say("H6. A spiral of one goes round one bi-folding of four joint forms, and a moment of it is one next me-parity: "
    "four forms, one next a moment", len(set(rows[:4])) == 4 and rows[4:8] == rows[:4] and all(n in (PLUS, MINUS) for p, n in rows))
say("H7. Two moments on, a spiral of one's next is the other-than of its next two moments before: other-than-other-than "
    "of it four moments on, the same again", all(rows[t + 2][1] == (rows[t][1][1], rows[t][1][0]) for t in range(6))
    and all(rows[t + 4][1] == rows[t][1] for t in range(4)))
say("M1. With the top place's podaling twice in a row, no fold goes round, and H2 says is-not",
    [1, podaling(1, {1}, 2), podaling(podaling(1, {1}, 2), {1}, 2)] != round_of(1, 2)[:3])
print("\nAll is." if all(results) else "\nNot all is.")
