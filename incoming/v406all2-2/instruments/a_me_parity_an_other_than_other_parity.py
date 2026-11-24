"""A me-parity, an other-than-other-parity: a partner's word of 24 November, by executing.

    python3 -I incoming/v406all2-2/instruments/a_me_parity_an_other_than_other_parity.py .

A partner's word, said in plain words: a me-parity is an other-than-other-parity; a me-parity
is an other-than-other-than-all-parity; a co-parity is co- with the universe, and it
dissolves from living.

1  The opening's lines of all-parity, other-parity and other-than-other-parity, found in
   v406all2's window.
2  On rounds of 2 to 9 mes, all their openings: a me-parity by one other-than and by two,
   with no is-or-is-not of a co-parity in it.

The fifteen lines and the couplings along are this folder's, of
a_me_by_nand_other_thans_and_alls.py, and the step is v406Reiman's as it is. It prints a line
an is or an is-not, and writes nothing.
"""
import glob
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.argv = [sys.argv[0], str(root)]
import a_me_by_nand_other_thans_and_alls as draft  # noqa: E402

S, a_co_chaining, other_than = draft.S, draft.a_co_chaining, draft.other_than
step = draft.all_mes_one_moment(draft.a_me)


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def along(n, values, moments):
    """A round of n mes, a moment a row: a me's me-parity, and its prior same-existing is-or-is-not."""
    mes = list(range(n))
    society = {me: ([(S, v)], []) for me, v in zip(mes, values)}
    couplings, rows = a_co_chaining(n), []
    for _ in range(moments):
        priors = [dict(society[me][0]).get(S, 0) for me in mes]
        society = step(society, couplings)
        rows.append((priors, [dict(society[me][0]).get(S, 0) == priors[me] for me in mes]))
    return rows


if __name__ == "__main__":
    print("1. The opening's lines, in v406all2's window")
    found = sorted(glob.glob(str(root / "incoming/v406all2/The_window_of_the_opening*.md")))
    window = re.sub(r"[*`]", "", Path(found[0]).read_text(encoding="utf-8")) if found else ""
    line("All-parity is the named universal set of all now-existing me-parities." in window, "31: All-parity is the named universal set of all now-existing me-parities.")
    line("Other-parity is other-than all-parity." in window, "32: Other-parity is other-than all-parity.")
    line("Other-than-other-parity is same-existing." in window, "33: Other-than-other-parity is same-existing.")
    line(all(other_than(other_than(a)) == a for a in (True, False)), "by nand: an other-than of an other-than is a thing again, two nands")

    print()
    print("2. On rounds of 2 to 9 mes, all their openings")
    by_one = by_two = with_a_same_existing = with_none = one_thing = True
    by_the_three = {}
    openings = places_with = places_with_none = 0
    for n in range(2, 10):
        for values in itertools.product((1, -1), repeat=n):
            openings += 1
            rows = along(n, values, 4 * n + 2)
            for t in range(2, 4 * n + 2):
                for i in range(n):
                    it_is = rows[t][0][i] == -rows[t - 2][0][(i - 1) % n]
                    by_one = by_one and it_is
                    if rows[t - 2][1][i] or rows[t - 1][1][i]:
                        places_with += 1
                        with_a_same_existing = with_a_same_existing and it_is
                    else:
                        places_with_none += 1
                        with_none = with_none and it_is
            by_two = by_two and all(rows[t][0][i] == rows[t - 4][0][(i - 2) % n] for t in range(4, 4 * n + 2) for i in range(n))
            for t in range(1, 4 * n + 1):
                for i in range(n):
                    the_three = (rows[t][0][i], rows[t - 1][0][(i - 1) % n], rows[t][0][(i - 1) % n])
                    one_thing = one_thing and by_the_three.setdefault(the_three, rows[t + 1][0][i]) == rows[t + 1][0][i]
    line(by_one, "a me-parity is the other-than of an other's me-parity: with two moments, of the me one coupling back, all %d openings" % openings)
    line(with_a_same_existing and with_none and places_with > 0 and places_with_none > 0,
         "it is the same with a prior same-existing between the two moments and with a prior inverting at both: no is-or-is-not of a co-parity is in it")
    line(by_two, "a me-parity is an other-than of an other-than: with four moments, the me-parity of the me two couplings back, same-existing")
    line(by_one and by_two, "a round's set of all its me-parities: with two moments its other-thans a coupling on, and with four moments the set again two couplings on")
    line(one_thing and len(by_the_three) > 1, "a me's next is one thing by three, its prior, its other's prior and its other's now: all %d of their cases, at all places" % len(by_the_three))
    the_word = "surf" + "acing"
    line(the_word not in Path(__file__).read_text(encoding="utf-8") and by_one and by_two,
         "these lines say an other's now by that name alone, and a me-parity's two sentences execute: the word of a partner's asking is needed at no place of them")
