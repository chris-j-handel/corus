"""Session v383Op: two selves apart, each offered a setting, at Exhibit ONE's resolver.

Runs from the repository root: python3 incoming/v383Op/two_wings.py
Reads the newest Exhibit ONE at the root and executes its python block.

The field's observing (Hensen and others, 2015, arXiv:1508.05949): two electron spins 1.3 km
apart; at each a setting, one of two, chosen at random after the spins were prepared and too late
for any signal at light speed to reach the other; at each an outcome, +1 or -1. Over 245 trials
the number S = E(0,0) + E(0,1) + E(1,0) - E(1,1), E the average of the two outcomes multiplied,
came to 2.42 +/- 0.20. The field's theorem (Clauser, Horne, Shimony and Holt, after Bell): where
each outcome is set by that side's own setting and whatever that side carries, S is 2 at most.

The instrument here, said whole:
  - two selves, A and B, each carrying two sharings, 'k' and 'm', each at a parity; the two
    carryings are whatever a prior coupling left, every one of the 16 pairs tried;
  - no join between them during a trial: nothing passes from one to the other;
  - a setting is an offering at 2 from beyond the self: one of nine, none, + or - at each sharing;
    each side's two settings are any two of the nine;
  - each self enters 1-co-bi-tri-offering for 1, 2 or 3 momentaries, offered its setting each time;
  - an outcome is +1 or -1, read from what that self shared at 'k' at its last momentary (10)
    and its carrying next (11), by any of four readings.
Each choice is tried. For every one, S is computed for each pair of carryings; a mixture of
carryings can come no higher than the highest of them.
"""
import glob, itertools, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']

SETTINGS = [[(key, p) for key, p in (('k', a), ('m', b)) if p is not None]
            for a in (None, 1, -1) for b in (None, 1, -1)]
READINGS = (
    lambda shared, nxt: nxt['k'],                              # the carrying next at k
    lambda shared, nxt: shared['k'] if shared['k'] else 1,     # the parity shared at k, + at 0
    lambda shared, nxt: 1 if shared['k'] else -1,              # a changing is or is not
    lambda shared, nxt: nxt['k'] * nxt['m'],                   # the two carryings, alike or parting
)


def outcome(carrying, setting, momentaries, reading):
    c = list(carrying.items())
    for _ in range(momentaries):
        shared, c = _1(c, setting)
    return reading(dict(shared), dict(c))


carryings = [dict(k=a, m=b) for a in (1, -1) for b in (1, -1)]
highest, tried = 0, 0
for momentaries in (1, 2, 3):
    for reading in READINGS:
        # each side's outcome at each carrying and each setting
        table = {(i, s): outcome(carryings[i], SETTINGS[s], momentaries, reading)
                 for i in range(4) for s in range(9)}
        for a0, a1 in itertools.combinations(range(9), 2):
            for b0, b1 in itertools.combinations(range(9), 2):
                for i in range(4):
                    for j in range(4):
                        A0, A1, B0, B1 = table[(i, a0)], table[(i, a1)], table[(j, b0)], table[(j, b1)]
                        S = A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1
                        highest = max(highest, abs(S))
                        tried += 1
print('Exhibit ONE read at', exhibit_one)
print('choices tried: %d; highest S at any of them: %d' % (tried, highest))
print("the field's bound for outcomes set at each side alone: 2; the field's observing: 2.42 +/- 0.20")
