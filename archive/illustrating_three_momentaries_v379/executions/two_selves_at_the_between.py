"""Exhibit ONE's code run at two selves joined across both ways, A's 10 to B's 14 and B's 10 to A's 14.
Run from the repository root:
    python3 incoming/illustrating_three_momentaries_v379/executions/two_selves_at_the_between.py
"""
import re, glob
src = open(sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]).read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
ns = {}; exec(code, ns)
one, seventeen = ns['_1_co_bi_offering'], ns['_17_tri_co_offering']
say = lambda p: {None: 'none', 1: '+', -1: '-', 0: '0'}[p]
joins = {('A', 10): 'B', ('B', 10): 'A'}

def run(society, momentaries=8):
    at10 = {s: [] for s in society}; at11 = {s: [] for s in society}
    for m in range(momentaries):
        out = seventeen(society, joins)
        for s in society:
            ten, eleven = one(society[s][0], society[s][1])
            at10[s].append(say(dict(ten).get('s'))); at11[s].append(say(dict(eleven).get('s')))
        society = {s: (out[s][0], [('s', v) for (_k, v) in out[s][1]]) for s in out}
    return at10, at11

print("Part 1. A offered + once at momentary 1, B offered nothing")
a, c = run({'A': ([], [('s', 1)]), 'B': ([], [])})
for s in 'AB': print(f"  {s} at 10: {' '.join(a[s])}    chained at 11: {' '.join(c[s])}")

print("\nPart 2. A and B each offered + once at momentary 1")
a, c = run({'A': ([], [('s', 1)]), 'B': ([], [('s', 1)])})
for s in 'AB': print(f"  {s} at 10: {' '.join(a[s])}    chained at 11: {' '.join(c[s])}")
