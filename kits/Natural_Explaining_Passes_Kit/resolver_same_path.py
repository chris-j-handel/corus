import re, random, sys
src = open(sys.argv[1]).read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
bare = re.sub(r'\nCONNECTORS = \{.*?\n\}\nJOINS = \{[^\n]*\}\n', '\n', code, flags=re.S)
assert 'CONNECTORS' not in bare and 'JOINS' not in bare
def run(c, seed):
    ns = {}; exec(c, ns); R = random.Random(seed)
    n = R.randint(2, 7); selves = list(range(n))
    soc = {s: ([((s, k), R.choice([1, -1])) for k in range(3)], [((R.choice(selves), R.randint(0, 2)), R.choice([1, -1, 0])) for _ in range(R.randint(0, 6))]) for s in selves}
    five = {}
    for s in selves:
        for name in (6, 10, 9):
            if R.random() < .8: five[(s, name)] = R.choice(selves)
    out = []
    for _ in range(6):
        res = next(v for k, v in ns.items() if k.startswith('_17_') and callable(v))(soc, five); out.append(repr(sorted(res.items())))
        soc = {s: (res[s][0], [((k, 0), v) for k, v in res[s][1]]) for s in selves}
    return out
same = all(run(code, i) == run(bare, i) for i in range(300))
print('same resolving with and without the two lists, 300 societies x 6 rounds:', same)
