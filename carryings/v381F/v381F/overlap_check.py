"""Session v381F: a facing is the overlap of two momentaries, executed at Exhibit ONE's resolver.

Runs from the repository root: python3 incoming/v381F/overlap_check.py
Two selves A and B coupled across both ways, A carrying + and B carrying -, one sharing, none offered from beyond.
At each momentary: what A shares across at 10, its now completing, and what arrives at B's 2 at the next momentary,
B's next opening, the other's prior at B's now. The same number at two sides, one direction forward on both.
"""
import glob, re
exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}; exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_17 = ns['_17_co_bi_tri_offering']
S = {1: '+', -1: '−', 0: '0'}
society = {'A': ([('s', 1)], []), 'B': ([('s', -1)], [])}
across = {('A', 10): 'B', ('B', 10): 'A'}
print('momentary | A shares at 10, its now completing | arrives at B\'s 2 at the next momentary, B\'s next opening | B shares at 10 | arrives at A\'s 2 next')
prev = None
for m in range(1, 7):
    out = _17(society, across)
    a10 = out['B'][1][0][1] if out['B'][1] else None   # what arrives at B's 2 next is A's 10 now
    b10 = out['A'][1][0][1] if out['A'][1] else None
    arrivedB = S[society['B'][1][0][1]] if society['B'][1] else 'none'
    arrivedA = S[society['A'][1][0][1]] if society['A'][1] else 'none'
    print('%9d | %-35s | %-48s | %-14s | %s' % (m, S[a10], 'B\'s 2 at momentary %d: %s' % (m + 1, S[a10]), S[b10], 'A\'s 2 at %d: %s' % (m + 1, S[b10])))
    society = {k: (out[k][0], out[k][1]) for k in society}
print('\nAt each row the one parity is A\'s now completing, shared at 10, and B\'s next opening, arriving at 2: one number, two sides, forward on both.')
