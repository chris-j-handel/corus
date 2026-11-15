"""v402mgr: carrying. Each parting tracked of the current understanding for the opening, from one incoming page
to Natural Intelligence's gathering file, at its Opening. A value located word for word there already enters no second time."""
import sys, re
R = sys.argv[1]
src = open(R + '/incoming/V400mgrB/Partings_Tracked.md', encoding='utf-8').read().split('\n')
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
    if sec == 1 and s.startswith('|') and not set(s) <= set('|-: '):
        c = [x.strip() for x in s.strip('|').split('|')]
        if len(c) < 4 or c[1].startswith('The living file'): continue
        t = f"*A living sentence, of {c[3]}:* {italics(c[1])}. *The current understanding:* {italics(c[2])}."
        k = 'Possible incohering'
    elif sec in (2, 3) and s.startswith('- '):
        t = italics(s[2:]); k = 'Possible incohering'
    elif sec in (4, 5) and s.startswith('- '):
        t = italics(s[2:]); k = 'Possible exploring'
    else: continue
    if located(t): skipped += 1; continue
    lab = {1: 'A parting tracked, the current understanding from a living sentence.', 2: 'A parting tracked, two sentences of the current understanding.',
           3: "A parting tracked, a reading of Exhibit ONE Natural Resolver's code from a sentence.", 4: 'With no reading yet.', 5: 'Not yet in natural naming.'}[sec]
    out.append(f"- **{k}** · *{lab}* {t}"); counts[sec] = counts.get(sec, 0) + 1
lead = ("- **An explaining** · The droplets after this one, to this section's end, are each parting tracked of the current understanding for this file's opening, "
        "carried whole by the managing session v402mgr, 15 November, from `incoming/V400mgrB/Partings_Tracked.md`. Each is for resolving here; none is living. "
        "A parting of an other living file's sentence is in this gathering file with the understanding it is of, and is a value for that file's own session.")
anchor = '\n## ONE · NATURAL'
assert g.count(anchor) == 1
g = g.replace(anchor, '\n' + lead + '\n' + '\n'.join(out) + '\n' + anchor)
open(gp, 'w', encoding='utf-8').write(g)
print('carried, by its part:', counts, '· in already:', skipped)
