"""v402mgr: carrying. What each of the three closed helping sessions left open or in a note only, from its closing page,
to the gathering file of the living file it names first, or of the session's own living file. In already: no second time."""
import sys, re, os, glob
R = sys.argv[1]; GV = R + '/gathering-value/'
titles = sorted((os.path.basename(p)[:-3] for p in glob.glob(GV + '*.md')), key=len, reverse=True)
text = {t: open(GV + t + '.md', encoding='utf-8').read() for t in titles}
norm = lambda s: re.sub(r'[\s*_`"“”‘’\']+', ' ', s).strip().lower()
N = {t: norm(text[t]) for t in titles}
def located(t, tgt):
    n = norm(t); a = n[len(n)//3: len(n)//3 + 60]; b = n[max(0, len(n)//2 - 30): len(n)//2 + 30]
    return a in N[tgt] or b in N[tgt]
italics = lambda t: re.sub(r'"([^"]+)"', r'*\1*', t)
def named_first(t):
    lead = t[:140]; best = None
    for name in titles:
        i = lead.find(name.replace('_', ' '))
        if i >= 0 and (best is None or i < best[0]): best = (i, name)
    return best[1] if best else None
pages = [('v402living/v402living_gathered.md', 'Natural_Naming', ('What is open', 'Values of other living files')),
         ('v402reading/The_session_gathered_at_its_closing.md', 'Natural_Intelligence', ('Open', 'Observings')),
         ('v402code/The_session_gathered_at_its_closing.md', 'Natural_Resolver', ('Open', 'What is open', 'Observings'))]
add, skipped = {}, 0
for page, dtgt, secs in pages:
    on = False
    for l in open(R + '/incoming/' + page, encoding='utf-8').read().split('\n'):
        s = l.strip()
        if s.startswith('## '): on = any(x in s for x in secs); kind = 'An explaining' if 'Observings' in s else 'Possible exploring'; continue
        if not on or not s.startswith('- '): continue
        t = s[2:]
        if len(norm(t)) < 60: continue
        tgt = 'Geodesic_Improving_Method' if kind == 'An explaining' else (named_first(t) or dtgt)
        if located(t, tgt): skipped += 1; continue
        add.setdefault((tgt, page), []).append(f"- **{kind}** · {italics(t)}")
for (tgt, page), ds in sorted(add.items()):
    lead = (f"- **An explaining** · The droplets after this one, to the next droplet of this kind or to this part's end, are what a helping session left open at its closing, carried whole by the managing session v402mgr, 15 November, "
            f"from `incoming/{page}`. Each is for resolving here; none is living.")
    text[tgt] = text[tgt].rstrip('\n') + '\n' + lead + '\n' + '\n'.join(ds) + '\n'
    open(GV + tgt + '.md', 'w', encoding='utf-8').write(text[tgt]); print(f"{tgt} from {page.split('/')[0]}: {len(ds)}")
print('in already:', skipped)
