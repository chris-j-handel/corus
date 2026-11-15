"""v402mgr: carrying. Three pages of incoming/V400mgrB/, each value to the gathering file of the living file it names,
or to the page's own first living file. A value located there already enters no second time."""
import sys, re, os, glob
R = sys.argv[1]; GV = R + '/gathering-value/'
titles = sorted((os.path.basename(p)[:-3] for p in glob.glob(GV + '*.md')), key=len, reverse=True)
alias = [("Exhibit ONE", 'Natural_Resolver'), ("the registry", 'Co-Chaining_Logic_Registry'), ("The registry", 'Co-Chaining_Logic_Registry'), ("the fifty-five", 'Natural_Intelligence'), ("The fifty-five", 'Natural_Intelligence')]
text = {t: open(GV + t + '.md', encoding='utf-8').read() for t in titles}
def norm(s): return re.sub(r'[\s*_`"“”‘’\']+', ' ', s).strip().lower()
N = {t: norm(text[t]) for t in titles}
def located(t, tgt):
    n = norm(t)
    a = n[len(n)//3: len(n)//3 + 60]; b = n[max(0, len(n)//2 - 30): len(n)//2 + 30]
    return a in N[tgt] or b in N[tgt]
def italics(t): return re.sub(r'"([^"]+)"', r'*\1*', t)
def target_of(t, default):
    best = None
    for name in titles:
        i = t.find(name.replace('_', ' '))
        if i >= 0 and (best is None or i < best[0]): best = (i, name)
    for a, name in alias:
        i = t.find(a)
        if i >= 0 and (best is None or i < best[0]): best = (i, name)
    return best[1] if best else default
pages = [
 ('Sessions_resolved.md', {1: ('Natural_Intelligence', 'Possible exploring'), 2: ('Natural_Intelligence', 'An explaining'), 3: ('Natural_Resolver', 'An explaining'),
                           4: ('Natural_Networking', 'An explaining'), 5: ('Natural_Chemistry', 'An explaining'), 6: ('Living_File_Registry', 'An explaining')}, True),
 ('The_One_Question_Method.md', {1: ('Geodesic_Improving_Method', 'An explaining'), 2: ('Geodesic_Improving_Method', 'An explaining'),
                                 3: ('Geodesic_Improving_Method', 'An explaining'), 4: ('Geodesic_Improving_Method', 'An explaining')}, False),
 ('The_Share_Current.md', {4: ('Living_File_Registry', 'Possible exploring')}, True),
]
add, skipped = {}, 0
for page, secs, by_name in pages:
    sec = 0
    for l in open(R + '/incoming/V400mgrB/' + page, encoding='utf-8').read().split('\n'):
        s = l.strip()
        m = re.match(r'^## (\d) ', s)
        if m: sec = int(m.group(1)); continue
        if sec not in secs or not s or set(s) <= set('|-: '): continue
        if s.startswith('- '): t = s[2:]
        elif s.startswith('|'):
            c = [x.strip() for x in s.strip('|').split('|')]; t = ' · '.join(x for x in c if x)
            if c and c[0] in ('motion', 'n', '') : continue
        elif page == 'The_One_Question_Method.md' and not s.startswith('#') and not s.startswith('**No word'): t = s
        else: continue
        if len(norm(t)) < 60: continue
        default, kind = secs[sec]
        tgt = target_of(t, default) if by_name else default
        if located(t, tgt): skipped += 1; continue
        add.setdefault((tgt, page), []).append(f"- **{kind}** · {italics(t)}")
rep = []
for (tgt, page), ds in sorted(add.items()):
    lead = (f"- **An explaining** · The droplets after this one, to the next droplet of this kind or to this part's end, are carried whole by the managing session v402mgr, 15 November, "
            f"from `incoming/V400mgrB/{page}`. Each is for resolving here; none is living.")
    text[tgt] = text[tgt].rstrip('\n') + '\n' + lead + '\n' + '\n'.join(ds) + '\n'
    open(GV + tgt + '.md', 'w', encoding='utf-8').write(text[tgt]); rep.append(f"{tgt} from {page[:-3]}: {len(ds)}")
print('\n'.join(rep)); print('in already:', skipped)
