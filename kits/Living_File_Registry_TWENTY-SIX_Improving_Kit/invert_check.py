"""Executes Exhibit ONE's code with each parity inverted and says whether each output inverts with it, deciding nothing.

Usage: python3 -I kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/invert_check.py [repository root] [inputs]

The code is read from the newest Exhibit_ONE_Natural_Resolver_v*.md at root, its first ```python block.
Random inputs, one to three keys, routes 6, 10 and 9, parities from + and -, and then with 0 as well:
each input parity is inverted, + to - and - to +, and nothing else, and each output parity is read against
the first output inverted. An output that is not the first inverted is a parting, and the first parting is shown.

A recorded result, Exhibit ONE v391: with + and - only, zero partings at _1_now_existing and _17_next_existing;
with a 0 at _3_now_co_observing, the prior, partings, as two tests read a 0 as a -,
(_15 > 0) == (_7 > 0) and -1 if _7 > 0 else 1. At Natural Resolver's gathering-value, Parities to one sharing, surfacing.
"""
import glob, os, random, re, sys, types

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 20000

def ver(p):
    m = re.search(r'_v(\d+)[A-Za-z]*\.md$', p)
    return int(m.group(1)) if m else 0

path = max(glob.glob(os.path.join(ROOT, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=ver)
src = re.search(r'```python\n(.*?)```', open(path, encoding='utf-8').read(), re.S).group(1)
code = types.ModuleType('exhibit_one')
exec(compile(src, path, 'exec'), code.__dict__)
print('code:', os.path.basename(path))

def inv(items):
    return [(k, -p) for k, p in items]

def build(rnd, P):
    keys = list(range(rnd.randint(1, 3)))
    routes = {(k, r): rnd.choice(keys) for k in keys for r in (6, 10, 9)}
    selves = {}
    for k in keys:
        prior = [((j, r), rnd.choice(P)) for j in keys for r in (6, 10, 9) if rnd.random() < 0.5]
        now = [((j, r), rnd.choice(P)) for j in keys for r in (6, 10, 9) if rnd.random() < 0.5]
        selves[k] = (prior, now)
    return selves, routes

def run(P, label):
    rnd = random.Random(11)
    n1 = b1 = n17 = b17 = 0
    first = None
    for _ in range(N):
        selves, routes = build(rnd, P)
        for prior, now in selves.values():
            a = code._1_now_existing(prior, now)
            b = code._1_now_existing(inv(prior), inv(now))
            n1 += 1
            if (inv(a[0]), inv(a[1])) != b:
                b1 += 1
                first = first or ('_1_now_existing', prior, now, a, b)
        try:
            a = code._17_next_existing(selves, routes)
            b = code._17_next_existing({k: (inv(p), inv(q)) for k, (p, q) in selves.items()}, routes)
        except Exception:
            continue
        n17 += 1
        if {k: (inv(x), inv(y)) for k, (x, y) in a.items()} != b:
            b17 += 1
    print(f'{label}: _1_now_existing {n1} inputs, {b1} partings; _17_next_existing {n17} inputs, {b17} partings')
    if first:
        f, prior, now, a, b = first
        print(f'  first parting at {f}: prior {prior}, now {now}')
        print(f'    output {a}, output with inputs inverted {b}')

run([1, -1], 'parities + and -')
run([1, -1, 0], 'parities +, - and 0')
