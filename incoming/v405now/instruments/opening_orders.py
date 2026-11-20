"""The order in which each opening names its concepts, and the working document's lines with each concept
they lean on that no line before them names. Prints markdown; writes nothing in the repository.

Usage: python3 -I opening_orders.py <rows.json>...
"""
import importlib.util, json, re, sys

import os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'opening_by_concept.py'), encoding='utf-8').read()
head = src.split("rows = []")[0]
ns = {}
exec(compile(head.replace("args = sys.argv[1:]\npage = args[args.index('--page') + 1]\njout = args[args.index('--json') + 1]\ninputs = [a for a in args[:args.index('--page')]]", ''), 'obc', 'exec'), ns)
concept_of, USE, clean = ns['concept_of'], ns['USE'], ns['clean']

rows = []
for f in sys.argv[1:]:
    rows += json.load(open(f, encoding='utf-8'))

want = ['NI v391 head', 'NI v395 head', 'NI v403mgr head', 'THIRTY v380 steps 1–70', 'THIRTY v391 steps 1–70',
        'THIRTY v395 steps 1–70', 'THIRTY v403mgr steps 1–70', 'window copy 11-19 12:27', 'window copy 11-19 18:43', 'document 20 Nov']
print('## The order an opening names its concepts in, by its drafts\n')
for lab in want:
    seq = []
    for l, n, raw in rows:
        if l != lab:
            continue
        k, d = concept_of(raw)
        if k and d and k not in seq:
            seq.append(k)
    print(f'- **{lab}:** ' + ' → '.join(seq[:28]) + (' → …' if len(seq) > 28 else ''))

print('\n## The working document now: what its lines lean on that no line before them names\n')
named, out = [], []
doc = [(n, raw) for l, n, raw in rows if l == 'document 20 Nov']
skip = {'The set of all now-existing moments in the universe is named now.', 'For a bi-coupling, **all-parity** is all-other-than-own-parity.'}
for n, raw in doc:
    if raw in skip:
        continue
    k, d = concept_of(raw)
    t = clean(raw)
    used = []
    for kk, rx in USE:
        if kk == k:
            continue
        tt = t
        if kk in ('now', 'prior', 'next'):
            tt = re.sub(r'(?<![\w-])' + kk + r'-(?:existing|and)', ' ', tt, flags=re.I)
        if kk == 'parity':
            tt = re.sub(r'(?:own|all|me|self|other|social|bi|co|both)-parit(?:y|ies)', ' ', tt, flags=re.I)
        if rx.search(tt):
            used.append(kk)
    ahead = [u for u in used if u not in named]
    print(f"- *{t}*" + (f" · leans on: {', '.join(ahead)}" if ahead else ' · all its concepts named before it'))
    if k and k not in named:
        named.append(k)
