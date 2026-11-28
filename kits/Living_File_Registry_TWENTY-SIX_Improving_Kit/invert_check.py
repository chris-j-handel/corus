"""Executes Exhibit ONE's code with each parity inverted and says, all or none, whether each output inverts with it.

Usage: python3 -I kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/invert_check.py [repository root]

The code is read from the newest Exhibit_ONE_Natural_Resolver_v*.md at root, its first ```python block.
Each case of a finite domain is read in sequence, none drawn by chance and no number of trials:
  _1_now_existing: one self, two sharing names; each name's prior absent or a parity; parities a self is
  observing, each sequence of up to three, each of either name and each parity.
  _17_next_existing: one self and two selves; each of 6, 10 and 9 absent or to a self; each prior absent or
  a parity; parities a self is observing, none or one.
First with parities + and -, then with 0 as well. Each input parity is inverted, + to - and - to +, and
nothing else, and each output is read against the first output inverted: each case inverting with it is
"is", and one case parting is "is not", its first parting shown.
At Natural Resolver's gathering-value, Parities to one sharing, surfacing.
"""
import glob, itertools, os, re, sys, types

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'

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

def priors_of(names, P):
    for choice in itertools.product([None] + P, repeat=len(names)):
        yield [(n, c) for n, c in zip(names, choice) if c is not None]

def sequences(names, P, longest):
    items = [(n, p) for n in names for p in P]
    for length in range(longest + 1):
        yield from (list(s) for s in itertools.product(items, repeat=length))

def one_self(P):
    names = ['a', 'b']
    for prior in priors_of(names, P):
        for now in sequences(names, P, 3):
            a = code._1_now_existing(prior, now)
            b = code._1_now_existing(inv(prior), inv(now))
            if (inv(a[0]), inv(a[1])) != b:
                return ('_1_now_existing', prior, now, a, b)
    return None

def societies(P):
    for selves in ([0], [0, 1]):
        targets = [None] + selves
        for chosen in itertools.product(targets, repeat=3 * len(selves)):
            routes = {(s, r): t for (s, r), t in zip(itertools.product(selves, (6, 10, 9)), chosen) if t is not None}
            per_self = [(prior, now) for prior in priors_of(['x'], P) for now in sequences(['x'], P, 1)]
            for states in itertools.product(per_self, repeat=len(selves)):
                yield dict(zip(selves, states)), routes

def networks(P):
    for society, routes in societies(P):
        a = code._17_next_existing(society, routes)
        b = code._17_next_existing({k: (inv(p), inv(q)) for k, (p, q) in society.items()}, routes)
        if {k: (inv(x), inv(y)) for k, (x, y) in a.items()} != b:
            return ('_17_next_existing', society, routes, a, b)
    return None

def read(P, label):
    for name, fn in (('_1_now_existing', one_self), ('_17_next_existing', networks)):
        parting = fn(P)
        if parting is None:
            print(f'{label}: {name}, each case inverting with its inputs: is')
        else:
            print(f'{label}: {name}: is not; first parting: inputs {parting[1]}, {parting[2]}')
            print(f'    output {parting[3]}, output with inputs inverted {parting[4]}')

read([1, -1], 'parities + and -')
read([1, -1, 0], 'parities +, - and 0')
