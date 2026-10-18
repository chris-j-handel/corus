"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/three_and_four.py
"""
import itertools, collections
src = open('incoming/v383Op/network_surface.py').read().split("TORI = ((2, 3)")[0]
exec(src)
S = {1: '+', -1: '-', 0: '0'}
# two selves, each sharing to the other
print('two selves, each sharing to the other, each opening, momentaries 1 to 8: each self its carrying at 3, the offering at its sharing 4, 0 or a changing at 12')
for op in itertools.product((1, -1), repeat=2):
    c = list(op); last = [None, None]; line = []
    for t in range(8):
        new, sh, cell = [0, 0], [0, 0], []
        for s in (0, 1):
            off = [] if last[1 - s] is None else [last[1 - s]]
            k = kind(c[s], off); new[s], sh[s] = entry(c[s], off)
            cell.append('%s|%s|%s' % (S[c[s]], 'none' if not [x for x in off if x] else S[off[0]], '0' if k == '.' else S[sh[s]]))
        c, last = new, sh; line.append(' '.join(cell))
    print('  opened %s %s:  ' % (S[op[0]], S[op[1]]) + '   '.join(line))
# tori: at each is-still-possibling, and at the momentary after
TORI = ((2, 3), (3, 3), (3, 4))
same_after = collections.Counter(); tot_single = single_same = 0
for p, q in TORI:
    selves = [(i, j) for i in range(p) for j in range(q)]
    for op in itertools.product((1, -1), repeat=p * q):
        c = dict(zip(selves, op)); last = {}; prev_kinds = None
        for t in range(1, 61):
            before = dict(c)
            c, shared, kinds = beat(p, q, c, last)
            if t >= 2:
                for s in selves:
                    offs = [last[u] for u in senders(p, q, s) if last[u]]
                    if offs and len(set(offs)) == 1:
                        tot_single += 1; single_same += c[s] == offs[0]
                    if prev_kinds and prev_kinds[s] == '.':
                        # after an is-still-possibling: which, and is the self then at the parity each sharing other is at
                        others_now = [c[u] for u in senders(p, q, s)]
                        same_after[(kinds[s], sum(c[s] == x for x in others_now))] += 1
            last, prev_kinds = shared, kinds
print('one parity surfaced at 14: %d; the self next at that parity, its sharing other\'s: %d' % (tot_single, single_same))
print('the momentary after an is-still-possibling: (what is at 12, how many of its two sharing others the self is then at one parity with):')
for k, v in sorted(same_after.items()): print('  ', k, v)
