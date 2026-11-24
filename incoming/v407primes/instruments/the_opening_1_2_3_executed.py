"""The opening's 1, 2 and 3, rigorized by the living resolver: spirals of 1, 2 and 3 selves.

Usage: python3 -I incoming/v407primes/instruments/the_opening_1_2_3_executed.py .
The resolver is Exhibit ONE's code as it is, opened by v406Reiman's resolver_as_it_is.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "v406Reiman" / "instruments"))
from resolver_as_it_is import resolver, opening, spiral_couplings, moments_again, exhibit_spiral_priors, S

names, _ = resolver(sys.argv[1] if len(sys.argv) > 1 else ".")
step = names["_17_next_existing"]
sign = {1: "+", -1: "−", 0: "0"}
said = []


def run(n, moments=13):
    soc = opening(range(n), exhibit_spiral_priors(n))
    c = spiral_couplings(n)
    rows = []
    for _ in range(moments):
        rows.append([dict(soc[i][0]).get(S, 0) for i in range(n)])
        soc = step(soc, c)
    return rows, moments_again(step, opening(range(n), exhibit_spiral_priors(n)), c)[1]


def say(text, ok):
    said.append(ok)
    print(("is     " if ok else "is-not ") + text)


r1, a1 = run(1)
say(f"1: one self comes again with 4 alone, 4 and 4 by 1 one: {''.join(sign[r[0]] for r in r1)}", a1 == 4)
r2, a2 = run(2)
say(f"2: two selves, each the other's other-than at all moments, again with 2, two inversions: {' '.join(''.join(sign[v] for v in r) for r in r2)}",
    a2 == 2 and all(r[0] == -r[1] for r in r2))
say("2: their parities sum to 0 at all moments, an all-parity of 0", all(sum(r) == 0 for r in r2))
r3, a3 = run(3)
pairs = []
for r in r3:
    like = [i for i in range(3) if r[i] == r[(i + 1) % 3]]
    pairs.append(like[0] if like else None)
say(f"3: three selves, again with 12; a like pair at all moments from the opening's next, its place by moment {pairs[1:]}",
    a3 == 12 and all(p is not None for p in pairs[1:]))
moves = [pairs[t] for t in range(1, 13, 2)]
say(f"3: the like pair goes along one self with a second moment: {moves}",
    all((moves[k + 1] - moves[k]) % 3 == 1 for k in range(len(moves) - 1)))
print("All is." if all(said) else "Not all is.")
