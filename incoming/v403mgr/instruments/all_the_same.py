"""A self's prior going on the same, with each of its others the same as it: all or none at all, by Exhibit ONE's
code executed. Reads Exhibit ONE Natural Resolver's living version, executes its code, and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/all_the_same.py <root>

One self with one sharing and a prior of + or of -, and one, two and three others, each other's parity + or -:
each case by the parity the self is sharing and its next prior.

Returned at main, Merge #699, 15 November 2026:
  with one other, two cases; with two others, four; with three others, eight; each with a prior of + and of -.
  In each number of others, one case has the self's prior going on the same, the self sharing 0: each of its others
  the same as its prior. In each other case its prior is inverting, and the self is sharing its next.
  With its others parting, a + and a -, no parity is surfacing, and its prior is inverting.
"""
import glob, itertools, os, re, sys

R = sys.argv[1]
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')),
               key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
ns = {}; exec(one.split('```python', 1)[1].split('```', 1)[0], ns)
resolve = ns['_1_now_existing']
mark = {1: '+', -1: '-', 0: '0'}
for prior in (1, -1):
    for k in (1, 2, 3):
        same_cases = []
        for others in itertools.product((1, -1), repeat=k):
            sharing, nxt = resolve([('k', prior)], [('k', p) for p in others])
            sharing = dict(sharing)['k']; nxt = dict(nxt)['k']
            all_same = all(p == prior for p in others)
            assert (nxt == prior) == all_same and (sharing == 0) == all_same and (all_same or (nxt == -prior and sharing == nxt))
            if all_same: same_cases.append(others)
            print(f'   prior {mark[prior]}, others {" ".join(mark[p] for p in others):5s}: sharing {mark[sharing]}, next prior {mark[nxt]}')
        assert len(same_cases) == 1
        print(f'prior {mark[prior]}, {k} of its others: {2 ** k} cases, its prior going on the same in 1, each of its others {mark[prior]}')
