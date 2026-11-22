#!/usr/bin/env python3
"""Chain a destiny sentence back through the opening's named concepts.

Usage: python3 -I chain_back.py OPENING.md WINDOW.json DESTINIES.json WORDS.py
  OPENING the next version's Natural Intelligence; WORDS incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py
The opening's head lines with a bold concept each name that concept. A
destiny's concepts are the named concepts its words carry; the path is their
closure through the sentences naming them. Each concept is marked by whether
the window's lines name it, and each sentence on the path is read for words
of no natural naming. It sizes a path and decides nothing.
"""
import json, re, sys, importlib.util

op, win, des, wordsmod = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('w', wordsmod)
w = importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
WORDS = [(n, re.compile(p, re.I)) for n, p in w.WORDS]

names = {}
for line in open(op, encoding='utf-8').read().split('\n')[:80]:
    s = line.rstrip(' \\').strip()
    for b in re.findall(r'\*\*([^*]+)\*\*', s):
        b = b.strip()
        if b[0].isupper() and ' ' in b and len(b) > 30:
            continue
        key = b.lower()
        if key not in names:
            names[key] = s
window = {k.lower(): v for k, v in json.load(open(win)).items()}
keys = sorted(names, key=len, reverse=True)

def concepts(text):
    t = ' ' + text.lower() + ' '
    found = []
    for k in keys:
        pat = r'(?<![\w-])' + re.escape(k) + r'(?![\w-])'
        if re.search(pat, t):
            found.append(k)
            t = re.sub(pat, ' ', t)
    return found

def listed(text):
    return sorted({n for n, rx in WORDS if rx.search(text)})

out = []
for d in json.load(open(des)):
    seen, todo = [], concepts(d['sentence'])
    while todo:
        k = todo.pop(0)
        if k in seen:
            continue
        seen.append(k)
        if k in window:
            continue
        todo += [c for c in concepts(names[k]) if c != k]
    path = []
    for k in seen:
        if k in window:
            path.append({'concept': k, 'window': window[k]})
        else:
            path.append({'concept': k, 'sentence': names[k], 'words': listed(names[k])})
    out.append({'destiny': d['name'], 'path': path,
                'outside': [p['concept'] for p in path if 'window' not in p],
                'words': sorted({x for p in path for x in p.get('words', [])} | set(listed(d['sentence'])))})
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
