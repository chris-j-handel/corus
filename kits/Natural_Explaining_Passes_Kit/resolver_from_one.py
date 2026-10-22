"""resolver_from_one.py: write Exhibit ONE's code block to a runnable resolver.py, so a reader runs the code that decides.
Usage, from the repository root: python3 resolver_from_one.py OUT_DIR
It writes OUT_DIR/resolver.py and OUT_DIR/ring.py, a harness: ring.run(priors, edges, steps) steps a society of selves,
each self ([('s', prior)], []), edges as (from, via, to) with via 6, 10 or 9, and gives each self's prior at each momentary."""
import re, sys, os, glob
out = sys.argv[1] if len(sys.argv) > 1 else '.'
one = max(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'), key=lambda f: int(re.search(r'_v(\d+)', f).group(1)))
code = [b for b in re.findall(r'```python\n(.*?)```', open(one).read(), re.S) if 'def _17_next_existing' in b][0]
os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'resolver.py'), 'w').write(code)
open(os.path.join(out, 'ring.py'), 'w').write('''import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolver import _17_next_existing
def run(priors, edges, steps):
    n = len(priors)
    soc = {i: ([('s', p)], []) for i, p in enumerate(priors)}
    five = {(s, v): d for s, v, d in edges}
    out = []
    for t in range(steps):
        res = _17_next_existing(soc, five)
        out.append([dict(res[i][0]).get('s') for i in range(n)])
        soc = {i: (res[i][0], res[i][1]) for i in range(n)}
    return out
if __name__ == '__main__':
    print('spiral of one', run([1], [(0, 9, 0)], 6))
    print('two alike, both ways', run([1, 1], [(0, 9, 1), (1, 9, 0)], 6))
''')
print('written', os.path.join(out, 'resolver.py'), os.path.join(out, 'ring.py'), 'from', one)
