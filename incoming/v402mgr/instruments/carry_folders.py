"""v402mgr: carrying. Each page of value in incoming/v401mgr/, incoming/V401atom/ and incoming/v401de/,
each value to the gathering file of the living file it meets: the living file a line names first, or its page's own.
Carried whole: the risk of carrying an incohering is less than the risk of losing a valuable cohering.
A value located word for word in that gathering file already enters no second time. A carried sentence has italics, no quotation marks."""
import sys, re, os, glob
R = sys.argv[1]; GV = R + '/gathering-value/'
titles = sorted((os.path.basename(p)[:-3] for p in glob.glob(GV + '*.md')), key=len, reverse=True)
text = {t: open(GV + t + '.md', encoding='utf-8').read() for t in titles}
def norm(s): return re.sub(r'[\s*_`"“”‘’\']+', ' ', s).strip().lower()
N = {t: norm(text[t]) for t in titles}
def located(t, tgt):
    n = norm(t)
    a = n[len(n)//3: len(n)//3 + 60]; b = n[max(0, len(n)//2 - 30): len(n)//2 + 30]
    return a in N[tgt] or b in N[tgt]
def italics(t): return re.sub(r'"([^"]+)"', r'*\1*', t)
alias = {'Exhibit ONE': 'Natural_Resolver'}
def named_first(t):
    m = re.match(r'^\*\*([^*]{3,90})\*\*', t)
    if not m: return None
    lead = m.group(1)
    for name in titles:
        if lead.startswith(name.replace('_', ' ')) or lead.startswith('Exhibit') and name.replace('_', ' ') in lead: return name
    for a, name in alias.items():
        if lead.startswith(a): return name
    return None
E, I, X = 'An explaining', 'Possible incohering', 'Possible exploring'
NI, NN, NR, CC, GM, NP, NC, NM = 'Natural_Intelligence', 'Natural_Naming', 'Natural_Resolver', 'Co-Chaining_Logic_Registry', 'Geodesic_Improving_Method', 'Natural_Physics', 'Natural_Chemistry', 'Natural_Mathematics'
# page, default target, default kind, {section number: (target, kind)}, tables, paragraphs
pages = [
 ('v401mgr/The_sentences_of_13_and_14_November.md', NI, E, {7: (NI, E), 8: (NI, X), 9: (NI, I)}, False, False),
 ('v401mgr/The_concerns_by_their_root.md', NI, I, {21: (GM, E), 13: (GM, E)}, True, True),
 ('v401mgr/Two_selves_meeting_the_chain.md', NI, E, {}, True, True),
 ('v401mgr/A_three_cycling_laid_on_the_threes.md', NN, E, {}, True, True),
 ('v401mgr/Scale_three_things_laid_on_each_other.md', NN, E, {}, True, True),
 ('v401mgr/parts/Part_one_17_no_next_1.md', NN, I, {}, True, True),
 ('v401mgr/parts/Part_two_a_podal_no_less.md', NN, I, {}, True, True),
 ('v401mgr/parts/Part_three_a_moment_no_momentary.md', NN, I, {}, False, True),
 ('v401mgr/parts/Part_four_a_names_three_in_its_name.md', NN, I, {}, True, True),
 ('v401mgr/placing/Natural_Naming_each_droplet_placed.md', NN, E, {}, False, False),
 ('v401mgr/placing/Natural_Resolver_each_droplet_placed.md', NR, E, {}, False, False),
 ('v401mgr/placing/The_persons_sentences_each_placed.md', NI, E, {}, False, False),
 ('v401mgr/placing/The_Placing_first_reading.md', NI, E, {}, False, False),
 ('v401mgr/The_three_sessions_gathered_read_first.md', GM, E, {}, False, False),
 ('V401atom/Value_since_the_gathering.md', NI, E, {3: (GM, E), 4: (NI, I), 5: (NP, E), 6: (NR, E)}, False, False),
 ('V401atom/Podaling_out_from_the_opening_to_the_vault.md', NI, E, {}, False, True),
 ('V401atom/The_Value_Droplets.md', CC, E, {}, False, False),
 ('V401atom/The_Concerns_of_the_Sequence.md', CC, I, {}, False, True),
 ('V401atom/The_Gatherings_Droplets_each_placed.md', CC, E, {}, False, False),
 ('V401atom/Value_for_the_vault.md', NP, E, {}, False, True),
 ('V401atom/Five_items_at_carbon_read_again.md', NC, E, {}, False, True),
 ('V401atom/The_Atoms_Form.md', NP, E, {}, False, True),
 ('V401atom/Natural_Mathematics_and_Natural_Numbers_read.md', NM, E, {}, False, True),
 ('V401atom/The_Session_Gathered.md', NI, E, {}, False, False),
 ('v401de/Living_sentences_by_name.md', NN, I, {}, False, True),
 ('v401de/Part_one_read_for_harm.md', NN, I, {}, False, False),
 ('v401de/The_Session_Gathered.md', NI, E, {}, False, False),
]
skipline = re.compile(r'^(\*\*)?(No word here has authority|This page changes no|What this page is|Incoming ·|The working v40|Relied on by nothing)')
add, skipped, per_page = {}, 0, {}
for page, dtgt, dkind, secs, tables, paras in pages:
    sec, group = 0, None
    for l in open(R + '/incoming/' + page, encoding='utf-8').read().split('\n'):
        s = l.strip()
        m = re.match(r'^## (\d+)\b', s)
        if m: sec = int(m.group(1)); group = re.sub(r'^## [\d.]+ ?', '', s); continue
        m = re.match(r'^#{3,4} [\d.]* ?(.+)$', s)
        if m: group = m.group(1); continue
        if not s or s == '---' or s.startswith('#') or set(s) <= set('|-: ') or skipline.match(s): continue
        m = re.match(r'^\*\*([^*]+)\*\*$', s)
        if m: group = m.group(1).rstrip('.:'); continue
        if s.startswith('|'):
            if not tables: continue
            c = [x.strip() for x in s.strip('|').split('|')]; t = ' · '.join(x for x in c if x)
        elif s.startswith('- '): t = s[2:]
        elif re.match(r'^\d+[a-z-]*\. ', s): t = re.sub(r'^(\d+[a-z-]*)\. ', r'*\1.* ', s)
        elif s.startswith('>'): continue
        elif paras: t = s
        else: continue
        if len(norm(t)) < 60: continue
        tgt, kind = secs.get(sec, (dtgt, dkind))
        tgt = named_first(t) or tgt
        if located(t, tgt): skipped += 1; continue
        g = f"*{group}.* " if group and not t.startswith('**') else ''
        add.setdefault((tgt, page), []).append(f"- **{kind}** · {g}{italics(t)}")
        per_page[page] = per_page.get(page, 0) + 1
by_tgt = {}
for (tgt, page), ds in sorted(add.items()):
    lead = (f"- **An explaining** · The droplets after this one, to the next droplet of this kind or to this part's end, are carried whole by the managing session v402mgr, 15 November, "
            f"from `incoming/{page}`. Each is for resolving here; none is living.")
    text[tgt] = text[tgt].rstrip('\n') + '\n' + lead + '\n' + '\n'.join(ds) + '\n'
    by_tgt[tgt] = by_tgt.get(tgt, 0) + len(ds)
for tgt in by_tgt: open(GV + tgt + '.md', 'w', encoding='utf-8').write(text[tgt])
print('by page:'); [print(f"  {n:5d}  {p}") for p, n in per_page.items()]
print('by gathering file:', dict(sorted(by_tgt.items(), key=lambda kv: -kv[1])))
print('carried', sum(by_tgt.values()), '· in already', skipped)
