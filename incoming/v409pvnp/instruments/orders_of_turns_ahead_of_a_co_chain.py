"""Orders of turns ahead of a co-chain: three layings, executed with all openings and all selves inverted in turn.

One other a moment, a self's couplings in turn, all living, the twelve lines by their table. One laying of 4 selves is
from all orders of turns gone through, the instrument beside this one. Two, of 4 and of 5 selves, are from a drawn
search of this session. A laying from a search is exact here: all its openings are executed. That no laying is sooner
is said by no search.

    python3 -I incoming/v409pvnp/instruments/orders_of_turns_ahead_of_a_co_chain.py .
"""
import itertools
import numpy as np
from pathlib import Path

src = (Path(__file__).resolve().parent / "an_other_than_carried_or_lost_all_openings.py").read_text()
exec(src[src.index("import itertools"):src.index("def society")])
out = [o for o in out if o[1].startswith("E0")]

def unparted(turns, S, T):
    """How many of a self inverted, an opening and an other self are with no parting by moment T."""
    openings = np.array(list(itertools.product((1, 2), repeat=S)), np.uint8); O = len(openings)
    s1 = np.broadcast_to(openings, (S, O, S)).copy(); s2 = s1.copy()
    for A in range(S): s2[A, :, A] = 3 - s2[A, :, A]
    l1 = np.zeros((S, O, S), np.uint8); l2 = l1.copy()
    parted = np.zeros((S, O, S), bool)
    for A in range(S): parted[A, :, A] = True
    for t in range(1, T + 1):
        col = [turns[s][(t - 1) % len(turns[s])] for s in range(S)]
        f1 = l1[:, :, col]; f2 = l2[:, :, col]
        s1, l1 = NEXT[s1, f1], LAYS[s1, f1]; s2, l2 = NEXT[s2, f2], LAYS[s2, f2]
        parted |= s1 != s2
    return int((~parted).sum())

for S in (3, 4, 5, 8):
    chain = [((s + 1) % S,) for s in range(S)]
    say(f"J a co-chain of {S} selves has one me's other-than in all other selves by moment {2 * (S - 1)}, twice its couplings along, and not a moment sooner",
        unparted(chain, S, 2 * (S - 1)) == 0 and unparted(chain, S, 2 * (S - 1) - 1) > 0)
for S, T, turns, source in (
        (4, 5, [(1, 2), (3, 2, 0), (0, 1, 3), (2, 1)], "from all orders of turns of 1 to 3"),
        (4, 5, [(2, 3, 2), (0, 0, 2), (3, 3, 0), (2, 0, 1)], "from a drawn search"),
        (5, 7, [(0, 3, 1, 0), (1, 3, 0, 2, 3), (0, 0, 4, 1, 0), (2, 0, 2, 2), (3, 0, 3, 1, 3)], "from a drawn search")):
    say(f"K {S} selves, {source}, the selves observed in turn {turns}: one me's other-than is in all other selves by moment {T}, "
        f"a co-chain's {2 * (S - 1)}, with all openings and all selves inverted in turn", unparted(turns, S, T) == 0)
    say(f"   by moment {T - 1}, of a self inverted, an opening and an other self, with no parting yet: {unparted(turns, S, T - 1):,}", "sized")

for mark, text in out: print(f"{text}: {mark}" if mark != "sized" else text)
print()
print(sum(m == "is" for m, _ in out), "lines is,", sum(m == "is-not" for m, _ in out), "is-not,", sum(m == "sized" for m, _ in out), "sized")
