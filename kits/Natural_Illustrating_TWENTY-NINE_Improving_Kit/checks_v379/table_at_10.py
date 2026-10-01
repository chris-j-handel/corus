"""Exhibit ONE's code run at the table 'Chained at 3; each cell at 10 · chained at 11',
and one self momentary by momentary. Run from the repository root:
    python3 kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/checks_v379/table_at_10.py
"""
import re, glob
src = open(sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]).read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
ns = {}; exec(code, ns)
one = ns['_1_co_bi_offering']

def say(p):
    return {None: 'none', 1: '+', -1: '-', 0: '0'}[p]

print("Part 1. Chained at 3 (none, +, -) by surfacing at 14 (none, +, -, 0): at 10 / chained at 11")
for prior in [None, 1, -1]:
    cells = []
    for offered in [[], [('s', 1)], [('s', -1)], [('s', 1), ('s', -1)]]:
        carrying = [] if prior is None else [('s', prior)]
        ten, eleven = one(carrying, offered)
        at10 = dict(ten).get('s'); at11 = dict(eleven).get('s')
        cells.append(f"{say(at10) if at10 is not None else '-- '} . {say(at11)}")
    print(f"  chained {say(prior):>4}: " + " | ".join(f"{c:>9}" for c in cells))

print("\nPart 2. One self offered + once and then nothing, twelve momentaries")
carrying, offered, t10 = [], [('s', 1)], []
for m in range(12):
    ten, carrying = one(carrying, offered); t10.append(say(dict(ten)['s'])); offered = []
print("  at 10:", ' '.join(t10))

print("\nPart 3. One self offered + at each momentary, eight momentaries")
carrying, t10 = [], []
for m in range(8):
    ten, carrying = one(carrying, [('s', 1)]); t10.append(say(dict(ten)['s']))
print("  at 10:", ' '.join(t10), "  chained at 11 throughout:", say(dict(carrying)['s']))
