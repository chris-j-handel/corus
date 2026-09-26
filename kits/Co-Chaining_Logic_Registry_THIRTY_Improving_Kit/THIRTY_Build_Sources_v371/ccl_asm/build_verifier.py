"""Build the self-contained verifier of Exhibit THIRTY from the part check files."""
import json, re, subprocess, sys, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
OUT = os.path.join(os.environ.get('CCL_WORK', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'Co_Chaining_Logic_Registry_verifier_v371.py')
PARTS = [('core', None), ('num', 'PART THREE · NUMBERS'), ('math', 'PART FOUR · MATHEMATICS'),
         ('two', 'PART FIVE · NETWORKING'), ('eq', 'PART SIX · EQUILIBRIA'),
         ('x', 'PART SEVEN · EXPLAINING, NAMING AND THE METHOD'),
         ('o1', 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS'), ('o2', 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS'),
         ('o3', 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS')]

def patched(name):
    s = open(D + f'ccl_{name}_checks.py', encoding='utf-8').read()
    s = s[:s.index("\nif __name__ == '__main__':")] + '\n'
    if name == 'core':
        a = "SRC_MD = '/home/claude/work/Exhibit_ONE_Natural_Resolver_v371.md'\n"
        b = "code = re.search(r'```python\\n(.*?)```', open(SRC_MD).read(), re.S).group(1)\n"
        assert a in s and b in s
        s = s.replace(a, '').replace(b, 'code = RESOLVER_SRC\n')
    if name == 'two':
        a = 'with zipfile.ZipFile(KIT_ZIP) as z:'
        assert a in s
        s = s.replace(a, 'with zipfile.ZipFile(_ccl_path(KIT_ZIP)) as z:')
    assert "'''" not in s and not s.rstrip().endswith('\\')
    return s

resolver = open(D + 'resolver_v371.py', encoding='utf-8').read()
runs = json.load(open(D + 'ccl_asm/runs_all.json', encoding='utf-8'))
stats = json.load(open(D + 'ccl_asm/assembled_stats.json', encoding='utf-8'))
order = stats['order']

src = []
src.append('''#!/usr/bin/env python3
"""Co-Chaining Logic Registry verifier v371, the verifier of Exhibit THIRTY.

Runs each run link of the registry, Parts ONE to EIGHT, against the resolver's code (the first python
block of Exhibit_ONE_Natural_Resolver_v371.md, read from beside this file when it stands there, else the
copy carried below) and against the arithmetic, each check at its link's id. It prints, per Part, the
checks passed and failed, and a total.

A probe at a nye link returns True while the failure it names stands: it prints as a confirmed failure,
never as a verifier failure. A probe bounding a nye link prints as holding. A check needing a file not
found beside this file (or at a folder given with --repo) prints "needs <file>" and is skipped.

    python3 Co_Chaining_Logic_Registry_verifier_v371.py [--repo DIR]... [--timeout SECONDS] [-v]

--repo DIR adds a folder to look for the files some checks read (the repository's exhibits, the kit).
--timeout sets the time a check may run before it fails (120 s). -v prints each check with the run it
names. Exit status 0 when no check fails.
"""
import ast, io, json, linecache, os, re, sys, textwrap, time, types

HERE = os.path.dirname(os.path.abspath(__file__))
''')
src.append('RESOLVER_COPY = ' + repr(resolver) + '\n')
src.append('RUNS = ' + json.dumps(runs, ensure_ascii=False, indent=0) + '\n')
src.append('ORDER = ' + json.dumps(order) + '\n')
src.append('PART_SOURCES = {}\n')
for name, _ in PARTS:
    src.append(f"PART_SOURCES[{name!r}] = r'''" + patched(name) + "'''\n")
src.append('PART_LABELS = ' + repr({n: (l or 'PART ONE · FOUNDATION') for n, l in PARTS}) + '\n')
src.append(open(D + 'ccl_asm/verifier_main.py', encoding='utf-8').read())
open(OUT, 'w', encoding='utf-8').write('\n'.join(src))
print('written', OUT, sum(len(x) for x in src))
