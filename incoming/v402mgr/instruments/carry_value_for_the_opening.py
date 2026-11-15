"""v402mgr: carrying. Each value of incoming/V400mgrB/Value_for_the_opening.md to the gathering file of the living file it meets.
A value located word for word in that gathering file already enters no second time. A carried sentence has italics and no quotation marks."""
import sys, re, os, glob
R = sys.argv[1]
src = open(R + '/incoming/V400mgrB/Value_for_the_opening.md', encoding='utf-8').read().split('\n')
GV = R + '/gathering-value/'
titles = sorted((os.path.basename(p)[:-3] for p in glob.glob(GV + '*.md')), key=len, reverse=True)
alias = {'Exhibit ONE': 'Natural_Resolver', 'Exhibit TWENTY-TWO': 'Resolving_the_Hard_Problem_Registry', 'the Living File Registry': 'Living_File_Registry'}
text = {t: open(GV + t + '.md', encoding='utf-8').read() for t in titles}
def norm(s): return re.sub(r'[\s*_`"“”‘’\']+', ' ', s).strip().lower()
N = {t: norm(text[t]) for t in titles}
def located(t, tgt):
    n = norm(t)
    if len(n) < 50: return n in N[tgt]
    a = n[len(n)//3: len(n)//3 + 60]; b = n[max(0, len(n)//2 - 30): len(n)//2 + 30]
    return a in N[tgt] or b in N[tgt]
def italics(t): return re.sub(r'"([^"]+)"', r'*\1*', t)
def target_of(lead):
    for a, t in alias.items():
        if a in lead: return t
    for t in titles:
        if t.replace('_', ' ') in lead: return t
    return None
add = {}     # target -> (place, [droplets])
skipped = {}
def put(tgt, place, kind, t):
    if located(t, tgt): skipped[tgt] = skipped.get(tgt, 0) + 1; return
    add.setdefault((tgt, place), []).append(f"- **{kind}** · {italics(t)}")
def cell_line(s):
    c = [x.strip() for x in s.strip('|').split('|')]
    return ' · '.join(x for x in c if x)
sec, sub, buf = 0, None, []
def flush5():
    global sub, buf
    if sub and buf:
        put('Natural_Intelligence', 'back', 'An explaining', f"*{sub}.* " + ' '.join(buf))
    sub, buf = None, []
for l in src:
    s = l.strip()
    m = re.match(r'^## (\d) ', s)
    if m:
        flush5(); sec = int(m.group(1)); sub = None; continue
    m = re.match(r'^### [\d.]+ (.+)$', s)
    if m:
        if sec == 5: flush5()
        sub = m.group(1); continue
    if not s or s == '---' or set(s) <= set('|-: '): continue
    if sec == 5:
        if sub is None: sub = "Social moral competency's eight"
        buf.append(cell_line(s) if s.startswith('|') else re.sub(r'^- ', '', s)); continue
    if not s.startswith('- '): continue
    t = s[2:]
    if sec == 1: put('Natural_Intelligence', 'opening', 'An explaining', (f"*{sub}.* " if sub else '') + t)
    elif sec == 2: put('Natural_Resolver', 'back', 'An explaining', "*Read from the code's lines.* " + t)
    elif sec == 3: put('Natural_Intelligence', 'opening', 'Possible incohering', "*Of the opening as it waits.* " + t)
    elif sec == 4:
        m = re.match(r'^\*\*([^*]+)\*\* · (.+)$', t)
        tgt = target_of(m.group(1)) if m else None
        if tgt: put(tgt, 'back', 'Possible incohering', f"*Of {m.group(1)}.* " + m.group(2))
        else: put('Natural_Intelligence', 'back', 'Possible incohering', t)
    elif sec == 6: put('Natural_Intelligence', 'back', 'Possible exploring', "*Open, one binary.* " + t)
flush5()
lead = ("- **An explaining** · The droplets after this one, to the next droplet of this kind or to this part's end, are carried whole by the managing session v402mgr, 15 November, "
        "from `incoming/V400mgrB/Value_for_the_opening.md`. Each is for resolving here; none is living.")
report = []
for (tgt, place), ds in sorted(add.items()):
    g = text[tgt]
    block = lead + '\n' + '\n'.join(ds) + '\n'
    if place == 'opening':
        anchor = '\n## ONE · NATURAL'; assert g.count(anchor) == 1
        g = g.replace(anchor, '\n' + block + anchor)
    else:
        g = g.rstrip('\n') + '\n' + block
    text[tgt] = g
    open(GV + tgt + '.md', 'w', encoding='utf-8').write(g)
    report.append(f"{tgt} ({place}): {len(ds)}")
print('carried ·', ' · '.join(report)); print('in already ·', skipped)
