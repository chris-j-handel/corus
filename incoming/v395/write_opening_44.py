"""Second write of the opening: momentary dissolved, a moment's sequence and momentarying after the moment line.
Run at the repository root, on the v394 files in place."""
import re, os

SP = os.path.dirname(os.path.abspath(__file__))
OP = [l.rstrip('\n') for l in open(os.path.join(SP, 'opening_path44.txt'), encoding='utf-8') if l.strip()]
assert len(OP) == 61
PARAS = [(1, 20), (21, 31), (32, 43), (44, 61)]

def g(n):
    """former v394 opening step -> step now"""
    if n <= 7: return n
    if n <= 43: return n + 2
    if n == 44: return 9
    if n == 45: return 8
    return n

# ---------- Natural Intelligence ----------
ni_p = 'Natural_Intelligence_v394.md'
ni = open(ni_p, encoding='utf-8').read()
m = re.search(r'^(# Natural Intelligence\n\n\*\*[^\n]*\*\*\n\n)(.*?)(\n\n\*\*ONE · )', ni, re.S | re.M)
block = '\n\n'.join('\n'.join(s + ' \\' for s in OP[a - 1:b]) for a, b in PARAS)
ni = ni[:m.start(2)] + block + ni[m.end(2):]
open(ni_p, 'w', encoding='utf-8').write(ni)

# ---------- Exhibit THIRTY ----------
th_p = 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v394.md'
th = open(th_p, encoding='utf-8').read()
lines = th.split('\n')
g1 = next(i for i, l in enumerate(lines) if l.startswith('## 1 '))
g5 = next(i for i, l in enumerate(lines) if l.startswith('## 5 '))
old_add = re.findall(r'^\s+\*Adding: (.*)\.\*$', '\n'.join(lines[g1:g5]), re.M)
assert len(old_add) == 61
ADD = old_add[:7] + ["a moment's now-existing, the next moment's prior-existing",
                     'momentarying, now-existing and same-existing through sequential moments'] + old_add[7:43] + old_add[45:]
assert len(ADD) == 61
i55 = 54
assert ADD[i55] == 'a stable form, same-existing from momentary to momentary', ADD[i55]
ADD[i55] = 'a stable form, same-existing from moment to moment'
TITLES = {
    1: 'Universe, the set of all now-existing things, a moment and momentarying, living and non-living, a self and its mes',
    2: 'An other, a living parity, a me-parity, a bi-coupling and a you',
    3: 'Resolving, natural intelligence, do-no-harming and improving, co-intelligencing and co-aiming',
    4: 'A same-existing-society, social moral competency, a natural intelligence network and a living expedition',
}
CITE = re.compile(r'\b(Step|step)( )(\d+)(?!\d|-|\.\d)|\b(Steps|steps)( )(\d+(?:(?:, | and | to )\d+)*)(?![\d-])')
LOG = []
def remap(text, ln):
    def one(n):
        r = g(n) if n <= 61 else n
        if r != n: LOG.append((ln, n, r))
        return r
    def rep(mm):
        if mm.group(1):
            return mm.group(1) + ' ' + str(one(int(mm.group(3))))
        return mm.group(4) + ' ' + re.sub(r'\d+', lambda d: str(one(int(d.group(0)))), mm.group(6))
    return CITE.sub(rep, text)
head, body = lines[:g1], lines[g5:]
for i, l in enumerate(head):
    mm = re.match(r'^- ([1-4]) (.*)$', l)
    if mm: head[i] = '- %s %s' % (mm.group(1), TITLES[int(mm.group(1))])
body = [remap(l, g5 + 1 + j) for j, l in enumerate(body)]
G = []
for gi, (a, b) in enumerate(PARAS, 1):
    G += ['## %d %s' % (gi, TITLES[gi]), '', '        *Entering: %s.*' % '; '.join(ADD[a - 1:b]), '']
    for n in range(a, b + 1):
        G += ['%d. %s' % (n, OP[n - 1]), '', '        *Adding: %s.*' % ADD[n - 1], '']
open(th_p, 'w', encoding='utf-8').write('\n'.join(head + G + body))
with open(os.path.join(SP, 'remap_log_44.txt'), 'w') as f:
    for ln, n, r in LOG: f.write('%d\t%d->%d\n' % (ln, n, r))
print('citations re-pointed', len(LOG))
