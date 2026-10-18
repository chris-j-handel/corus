"""Session v381F: Exhibit ONE's resolver executed at the table of a spiral of selves.

Runs from the repository root: python3 incoming/v381F/spiral_check.py
Reads the newest Exhibit ONE at the root, executes its python block, and for spirals of
1, 2, 3, 4, 5, 6, 7, 9, 11 and 17 selves prints self 1's releasings along (9) at momentaries 1 to 12
and the momentary at which each self's carrying and offerings are as they were at the first momentary.
Opening as the table says it: one sharing, self 1 carrying -, the selves alternating along, none offered from beyond.
A count is said with its script, its start and its joins: the momentaries again are counted from the
first momentary's completing, so a spiral whose forms are the same after momentary 13 as after momentary 1 is said at 12.
"""
import glob, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
code = re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1)
names = {}
exec(code, names)
_1 = names['_1_co_bi_tri_offering']
_17 = names['_17_co_bi_tri_offering']
SYMBOL = {1: '+', -1: '−', 0: '0'}


def spiral(n, momentaries=12):
    parity = {i: (1 if i % 2 == 0 else -1) for i in range(n)}  # self 1 carries -, written as index 0
    parity = {i: -p for i, p in parity.items()}
    society = {i: ([('sharing', parity[i])], []) for i in range(n)}
    along = {(i, 9): (i + 1) % n for i in range(n)}
    releasings, first, again = [], None, None
    for m in range(1, max(4 * n + 3, momentaries + 1)):
        out = _17(society, along)
        tunneling, _ = _1(society[0][0], society[0][1])
        releasings.append(tunneling[0][1])
        society = {i: (out[i][0], out[i][1]) for i in range(n)}
        form = tuple((tuple(sorted(society[i][0])), tuple(sorted(society[i][1]))) for i in range(n))
        if first is None:
            first = form
        elif again is None and form == first:
            again = m - 1
    return ', '.join(SYMBOL[x] for x in releasings[:momentaries]), again


print('Exhibit ONE read at', exhibit_one)
print('selves | self 1 released along (9), momentaries 1 to 12 | momentaries to each self\'s releasings again')
for n in (1, 2, 3, 4, 5, 6, 7, 9, 11, 17):
    sequence, again = spiral(n)
    print('%2d | %s | %s' % (n, sequence, again))
