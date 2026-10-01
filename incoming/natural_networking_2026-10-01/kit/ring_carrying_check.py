"""A ring of selves joined along at 17 carries any pattern of parities round whole: at every momentary the ring's
chained parities are the pattern shifted, or shifted and inverted, for every pattern at rings of 3 to 8.
Usage: python3 ring_carrying_check.py <Exhibit ONE, or its candidate>"""
import re, sys, itertools
src = open(sys.argv[1], encoding='utf-8').read()
ns = {}; exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns); S17 = next(v for k,v in ns.items() if k.startswith('_17_') and callable(v))
def rot(p, s): return tuple(p[-s % len(p):] + p[:-s % len(p)])
for n in range(3, 9):
    whole = 0
    for pat in itertools.product((1, -1), repeat=n):
        soc = {i: ([('x', v)], []) for i, v in enumerate(pat)}; joins = {(i, 9): (i + 1) % n for i in range(n)}
        forms = {rot(pat, s) for s in range(n)} | {tuple(-x for x in rot(pat, s)) for s in range(n)}
        ok = True
        for k in range(4 * n):
            soc = S17(soc, joins); ok &= tuple(dict(soc[i][0])['x'] for i in range(n)) in forms
        whole += ok
    print(f'ring of {n}: {whole} of {2 ** n} patterns carried round whole at every momentary')
