"""v402mgr: carrying. Each sentence of the current understanding for the opening, each reading of it by the code,
and each place a pattern can be filled, from one incoming page to Natural Intelligence's gathering file, at its Opening.
A value located word for word in the gathering file already enters no second time."""
import sys, re
R = sys.argv[1]
src = open(R + '/incoming/V400mgrB/The_Frontier_Current.md', encoding='utf-8').read().split('\n')
gp = R + '/gathering-value/Natural_Intelligence.md'
g = open(gp, encoding='utf-8').read()
def norm(s): return re.sub(r'[\s*_`"“”‘’\']+', ' ', s).strip().lower()
G = norm(g)
def located(t):
    n = norm(t)
    if len(n) < 50: return n in G
    a = n[len(n)//3: len(n)//3 + 60]; b = n[max(0, len(n)//2 - 30): len(n)//2 + 30]
    return a in G or b in G
def italics(t):
    # a sentence in quotation marks is word for word living: a carried sentence has italics
    return re.sub(r'"([^"]+)"', r'*\1*', t).replace('“', '*').replace('”', '*')
i1 = next(i for i, l in enumerate(src) if l.startswith('## 1 '))
i2 = next(i for i, l in enumerate(src) if l.startswith('## 2 '))
i3 = next(i for i, l in enumerate(src) if l.startswith('## 3 '))
out, skipped, counts = [], 0, [0, 0, 0]
for l in src[i1:i2]:
    m = re.match(r'^(\d+[a-z-]*)\. (.+)$', l.strip())
    if not m: continue
    if located(m.group(2)): skipped += 1; continue
    out.append(f"- **An explaining** · *The current understanding, {m.group(1)}.* {italics(m.group(2))}"); counts[0] += 1
for l in src[i2:i3]:
    m = re.match(r'^- \*\*Beside ([^*]+?)\.?\*\* (.+)$', l.strip())
    if not m: continue
    if located(m.group(2)): skipped += 1; continue
    out.append(f"- **An explaining** · *By Exhibit ONE Natural Resolver's code, of {m.group(1)}.* {italics(m.group(2))}"); counts[1] += 1
title, buf = None, []
def flush():
    global title, buf
    if title and buf:
        t = ' '.join(buf)
        if located(t): 
            globals()['skipped'] += 1
        else:
            out.append(f"- **Possible exploring** · *A place a pattern can be filled: {title}.* {italics(t)}"); counts[2] += 1
    title, buf = None, []
for l in src[i3 + 1:]:
    s = l.strip()
    if s.startswith('## '): flush(); break
    m = re.match(r'^### [\d.]+ (.+)$', s)
    if m: flush(); title = m.group(1); continue
    if s and s != '---' and title: buf.append(s)
flush()
lead = ("- **An explaining** · The droplets after this one, to this section's end, are the current understanding for this file's opening, "
        "carried whole by the managing session v402mgr, 15 November, from `incoming/V400mgrB/The_Frontier_Current.md`: its sentences in their sequence, "
        "each reading of them by Exhibit ONE Natural Resolver's code, and each place a pattern can be filled. Each is for resolving here; none is living. "
        "A mark of letters and numbers is a sentence's own in that sequence.")
anchor = '\n## ONE · NATURAL'
assert g.count(anchor) == 1
g = g.replace(anchor, '\n' + lead + '\n' + '\n'.join(out) + '\n' + anchor)
open(gp, 'w', encoding='utf-8').write(g)
print('carried: sentences', counts[0], '· readings by the code', counts[1], '· places', counts[2], '· in already, entering no second time', skipped)
