#!/usr/bin/env python3
"""Resolve each aim's homes against the next version: file, section, and a short excerpt.

Usage: python3 -I homes.py BANDS.md NEXT_ROOT [band-number] [excerpt-chars]
Prints, per aim, each home part with what it reaches, or UNRESOLVED.
"""
import glob, os, re, sys

bands_md, root = sys.argv[1:3]
only = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != 'all' else None
N = int(sys.argv[4]) if len(sys.argv) > 4 else 220

def title_of(path):
    b = os.path.basename(path)[:-3]
    b = re.sub(r'_v[0-9a-z]+$', '', b)
    b = re.sub(r'^Exhibit_[A-Z-]+_', '', b)
    return b.replace('_', ' ')

files = {}
ALIAS = {'Exhibit ONE': 'Natural Resolver'}
for p in glob.glob(os.path.join(root, '*.md')):
    if os.path.basename(p) == 'README.md':
        continue
    files[title_of(p)] = p
gfiles = {os.path.basename(p)[:-3].replace('_', ' '): p for p in glob.glob(os.path.join(root, 'gathering-value', '*.md'))}

def sections(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    secs, cur, buf = {}, None, []
    heads = []
    for i, l in enumerate(lines):
        m = re.match(r'^(#{1,4}) (.+)', l)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip()))
    for k, (i, lev, h) in enumerate(heads):
        j = next((i2 for i2, lev2, _ in heads[k + 1:] if lev2 <= lev), len(lines))
        body = ' '.join(x.strip() for x in lines[i + 1:j] if x.strip() and not x.startswith('|'))
        m = re.match(r'^(?:PART )?([0-9]+(?:\.[0-9]+)?)\b', h)
        key = m.group(1) if m else h
        secs.setdefault(key, (h, body))
        secs.setdefault(h, (h, body))
    return secs

cache = {}
def secs_of(path):
    if path not in cache:
        cache[path] = sections(path)
    return cache[path]

thirty = files['Co-Chaining Logic Registry']
steps, groups, g = {}, {}, None
for l in open(thirty, encoding='utf-8'):
    m = re.match(r'^## (\d+) (.+)', l)
    if m:
        g = m.group(1); groups[g] = [m.group(2).strip(), []]
        continue
    m = re.match(r'^(\d+)\. (.+)', l)
    if m:
        steps[int(m.group(1))] = (g, m.group(2).strip())
        if g:
            groups[g][1].append(int(m.group(1)))

def nums(s):
    out = []
    for a, b in re.findall(r'(\d+)\s+to\s+(\d+)', s):
        out += list(range(int(a), int(b) + 1))
    s2 = re.sub(r'(\d+)\s+to\s+(\d+)', ' ', s)
    out += [int(x) for x in re.findall(r'\d+', s2)]
    return sorted(set(out))

def cut(t):
    t = re.sub(r'\s+', ' ', t)
    return t[:N] + ('…' if len(t) > N else '')

def resolve(part):
    part = part.strip().rstrip('.')
    for a, b in ALIAS.items():
        if part.startswith(a):
            part = b + part[len(a):]
    out = []
    m = re.match(r"Exhibit THIRTY(?:'s gathering)?,? (.*)", part)
    if m:
        rest = m.group(1)
        if 'whole registry' in rest:
            return [('THIRTY whole', f'{len(steps)} steps')]
        sm = re.match(r'(steps?) (.+?)(?: and (?:its gathering|groups?).*)?$', rest)
        gm = re.search(r'groups? ([\d ,toand]+)', rest)
        if sm and not rest.startswith('group'):
            for n in nums(re.split(r' and (?:its|groups?)', sm.group(2))[0]):
                if n in steps:
                    out.append((f'THIRTY step {n} (group {steps[n][0]})', cut(steps[n][1])))
                else:
                    out.append((f'THIRTY step {n}', 'UNRESOLVED'))
        if gm:
            for n in nums(gm.group(1)):
                gg = groups.get(str(n))
                out.append((f'THIRTY group {n}', (gg[0] + f' (steps {gg[1][0]}-{gg[1][-1]})') if gg else 'UNRESOLVED'))
        if 'gathering' in part:
            out.append(('THIRTY gathering', 'named'))
        return out or [(part, 'UNRESOLVED')]
    m = re.match(r"(.+?)'s gathering(?:,| at)? ?(.*)", part)
    if m:
        t = m.group(1).strip()
        t = {'Natural Intelligence': 'Natural Intelligence', 'Living File Registry': 'Living File Registry'}.get(t, t)
        gp = gfiles.get(t)
        if not gp:
            return [(part, 'UNRESOLVED gathering file')]
        rest = m.group(2)
        txt = open(gp, encoding='utf-8').read()
        cu = re.findall(r'(\d[a-z](?:-[a-z])?|\d[a-z]?)(?=\b)', rest) if 'understanding' in rest else []
        if cu:
            for k in re.findall(r'\b(\d[a-z](?:-[a-z])?|\d)\b', rest):
                mm = re.search(r'\*The current understanding, ' + re.escape(k) + r'\.\*\s*(.+)', txt)
                out.append((f'{t} gathering CU {k}', cut(mm.group(1)) if mm else 'UNRESOLVED'))
            return out
        if rest.startswith('head'):
            return [(f'{t} gathering head', 'named')]
        sec = re.findall(r'\d+(?:\.\d+)?', rest)
        s = secs_of(gp)
        for k in sec:
            hit = s.get(k)
            out.append((f'{t} gathering {k}', cut(hit[0] + ': ' + hit[1]) if hit else 'UNRESOLVED'))
        return out or [(f'{t} gathering', 'named' + (' ' + rest if rest else ''))]
    m = re.match(r"The window", part, re.I)
    if m or part.startswith("the window") or 'working document' in part.lower():
        return [(part, 'the window (checked against the window as it stands)')]
    for t in sorted(files, key=len, reverse=True):
        if part.startswith(t):
            rest = part[len(t):].strip(' ,')
            s = secs_of(files[t])
            if not rest:
                return [(t, 'whole file')]
            if rest.startswith("'s opening") or rest.startswith('opening'):
                return [(t + ' opening', 'named')]
            ks = []
            for a, b in re.findall(r'(\d+\.\d+) to (\d+\.\d+)', rest):
                a1, a2 = a.split('.'); b2 = b.split('.')[1]
                ks += [f'{a1}.{i}' for i in range(int(a2), int(b2) + 1)]
            rest2 = re.sub(r'(\d+\.\d+) to (\d+\.\d+)', ' ', rest)
            ks += re.findall(r'\d+\.\d+', rest2)
            pm = re.findall(r'parts? (one|two|three|four|five|six|seven|eight|nine|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN)', rest2)
            ks += re.findall(r'(?<![\d.])(\d+)(?![\d.])', re.sub(r'\d+\.\d+', ' ', rest2))
            for k in ks:
                hit = s.get(k)
                out.append((f'{t} {k}', cut(hit[0] + ': ' + hit[1]) if hit else 'UNRESOLVED'))
            for w in pm:
                out.append((f'{t} part {w}', 'named'))
            if not ks and not pm:
                out.append((f'{t} {rest}', 'named, not a number'))
            return out
    return [(part, 'UNRESOLVED file')]

band, bi = None, 0
for l in open(bands_md, encoding='utf-8'):
    m = re.match(r'^## (.+)', l)
    if m:
        band = m.group(1).strip(); bi += 1
        if only is None or only == bi:
            print(f'\n=== {bi} {band}')
        continue
    m = re.match(r'^- \*\*(.+?)\*\*\s*(.*?)\s*(?:\*([^*]+)\*)?\s*$', l.strip())
    if m and (only is None or only == bi):
        aim, words, homes = m.group(1), m.group(2), m.group(3) or ''
        print(f'\n* {aim} | {words}')
        for part in re.split(r';', homes):
            for k, v in resolve(part):
                print(f'    {k}: {v}')
