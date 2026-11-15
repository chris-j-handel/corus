"""v402mgr: carrying. The opening's fifty-five lines as they wait, each with its improved line, and the session's value
by its areas and its things not distinguished, from one incoming page to Natural Intelligence's gathering file, at its Opening."""
import sys, re
R = sys.argv[1]
src = open(R + '/incoming/V400mgrB/The_Session_Gathered.md', encoding='utf-8').read().split('\n')
gp = R + '/gathering-value/Natural_Intelligence.md'
g = open(gp, encoding='utf-8').read()
def norm(s): return re.sub(r'[\s*_`"“”‘’\']+', ' ', s).strip().lower()
G = norm(g)
def located(t):
    n = norm(t)
    if len(n) < 50: return n in G
    a = n[len(n)//3: len(n)//3 + 60]; b = n[max(0, len(n)//2 - 30): len(n)//2 + 30]
    return a in G or b in G
def italics(t): return re.sub(r'"([^"]+)"', r'*\1*', t)
sec, out, skipped, counts = 0, [], 0, {}
for l in src:
    s = l.strip()
    m = re.match(r'^## (\d) ', s)
    if m: sec = int(m.group(1)); continue
    if sec == 2 and s.startswith('|') and not set(s) <= set('|-: '):
        c = [x.strip() for x in s.strip('|').split('|')]
        if len(c) < 3 or not c[0].isdigit(): continue
        if c[2].rstrip('.') == 'As it waits': continue          # no improved line: nothing to carry
        t = f"*The opening's line {c[0]} as it waits:* {italics(c[1])} *Its improved line, a candidate:* {italics(c[2])}"
        if located(c[2]): skipped += 1; continue
        k = 'An explaining'
    elif sec in (3, 4) and (s.startswith('- ') or (s.startswith('|') and not set(s) <= set('|-: '))):
        if s.startswith('|'):
            c = [x.strip() for x in s.strip('|').split('|')]
            if len(c) < 2 or len(' '.join(c)) < 60 or c[0] in ('', 'n') and False: continue
            t = italics(' · '.join(x for x in c if x))
        else: t = italics(s[2:])
        if len(norm(t)) < 60: continue
        if located(t): skipped += 1; continue
        k = 'An explaining' if sec == 3 else 'Possible exploring'
    else: continue
    out.append(f"- **{k}** · {t}"); counts[sec] = counts.get(sec, 0) + 1
lead = ("- **An explaining** · The droplets after this one, to this section's end, are the opening's lines as they wait, each with its improved line, a candidate, "
        "and that session's value by its areas and its things not distinguished, carried whole by the managing session v402mgr, 15 November, "
        "from `incoming/V400mgrB/The_Session_Gathered.md`. Each is for resolving here; none is living.")
anchor = '\n## ONE · NATURAL'
assert g.count(anchor) == 1
g = g.replace(anchor, '\n' + lead + '\n' + '\n'.join(out) + '\n' + anchor)
open(gp, 'w', encoding='utf-8').write(g)
print('carried, by its part:', counts, '· in already:', skipped)
