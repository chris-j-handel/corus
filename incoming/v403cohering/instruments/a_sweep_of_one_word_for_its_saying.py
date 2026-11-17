"""One sweep of the next version's copy: a word Exhibit TWENTY Natural Naming has dissolved, said by its own
saying, with each plain place of the first aim's living files, and with each quotation of their gathering files
that is word for word a living sentence. One kind of improving with one sweep, all or none at all.
Reads Exhibit TWENTY Natural Naming's entry of the word; the set's list of living files; the newest at the root
of Natural Intelligence, Exhibit ONE Natural Resolver, Exhibit TWENTY Natural Naming and Exhibit THIRTY
Co-Chaining Logic Registry; and each one's gathering file. Executes; decides nothing.
With *apply* it writes a living file only as a copy: a file at the root that is not of the set's list of living
files. A living file of the list is read, each of its places said, and never written.

Use: python3 -I incoming/v403cohering/instruments/a_sweep_of_one_word_for_its_saying.py <root> <word> <its saying>          each place as it is and as re-said, and nothing written
     python3 -I incoming/v403cohering/instruments/a_sweep_of_one_word_for_its_saying.py <root> <word> <its saying> apply    the sweep, written with each copy

What it reads. The saying is one of the entry's own, in italics after its *a*, with the word in italics before it:
with an other saying it halts. A plain place is the word whole, capital or small, with no hyphen joining it, as
`each_dissolved_word_with_its_saying.py` reads a place: a code's lines, code marks, italics, a quotation and a
file's version line are each passed over as a mention. A heading and its line of the contents are an address,
and each is passed over and said: an address is re-said with each place naming it together. A capital opening
the word is a capital opening its saying. A place its saying would be beside its own word again, as *each each*,
is passed over and said: its sentence is for its own reading. A place within a longer word Exhibit TWENTY
Natural Naming has dissolved, as *another* within *one another*, is that longer word's place and no place of
this sweep: it is passed over and said, with each executing, and two sweeps have one answer in either order.
A quotation of a gathering file is a possible incohering's opening one and a droplet's closing one, as the
set's gathering check reads them: one word for word a living sentence, with the word in it, is re-said with its
sentence, and is word for word after or the sweep halts with nothing written. With a possible incohering's
opening quotation re-said, each plain place of the word in that droplet's own words after it, its re-saying of
that sentence, is re-said too.

Returned with the next version's draft, 16 November 2026, each applied, one sweep each:
  *one another* said by *each other*: one place, of Exhibit THIRTY Co-Chaining Logic Registry; a heading of that
  file and its line of the contents are as they are.
  *another* said by *an other*: forty-four places, nineteen of Natural Intelligence, one of them Exhibit ONE
  Natural Resolver's own inside it, one of Exhibit ONE Natural Resolver and twenty-four of Exhibit THIRTY
  Co-Chaining Logic Registry; nine quotations of their gathering files with their sentences.
  *every* said by *each*: eight places, six of Natural Intelligence and two of Exhibit THIRTY Co-Chaining Logic
  Registry; one sentence of that file is as it is, its saying beside its own word again.
  With each: check_set ALL PASS, Exhibit ONE Natural Resolver one and its code executing, and each gathering
  check no more found than at main.
"""
import glob, json, os, re, sys

R, WORD, SAYING = sys.argv[1], sys.argv[2], sys.argv[3]; APPLY = len(sys.argv) > 4 and sys.argv[4] == 'apply'
ver = lambda p: int(re.search(r'_v(\d+)', p).group(1))
def newest(stem):
    return max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver)
FIRST = [('Natural_Intelligence', 'Natural_Intelligence'), ('Exhibit_ONE_Natural_Resolver', 'Natural_Resolver'),
         ('Exhibit_TWENTY_Natural_Naming', 'Natural_Naming'), ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'Co-Chaining_Logic_Registry')]
LISTED = set(json.load(open(os.path.join(R, 'files.json'), encoding='utf-8')))

# the saying is the entry's own
ITALIC = re.compile(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)')
naming = open(newest('Exhibit_TWENTY_Natural_Naming'), encoding='utf-8').read().split('\n')
entry = None
for i, l in enumerate(naming):
    if l.startswith('- ') and WORD.lower() in [w.strip().lower() for w in ITALIC.findall(l.split(' · *a* ')[0])]:
        said = l.split(' · *a* ', 1)[1] if ' · *a* ' in l else (naming[i + 1][len('  - *a* '):] if naming[i + 1].startswith('  - *a* ') else '')
        entry = (l, [w.strip().lower() for w in ITALIC.findall(said)])
assert entry, f'Exhibit TWENTY Natural Naming has no entry with *{WORD}* dissolved'
assert SAYING.lower() in entry[1], f'*{SAYING}* is no saying of the entry: {entry[1]}'
print(f"Exhibit TWENTY Natural Naming's entry: {entry[0][:120]}")

whole = lambda w: re.compile(r'(?<![\w-])' + re.escape(w).replace(r'\ ', r'\s+') + r'(?![\w-])', re.I)
PAT = whole(WORD)
# each longer word the file has dissolved with this word whole within it: its places are its own sweep's
dissolved = set()
for i, l in enumerate(naming):
    if not l.startswith('- '): continue
    left = l.split(' · *a* ')[0] if ' · *a* ' in l else l if i + 1 < len(naming) and naming[i + 1].startswith('  - *a* ') else ''
    dissolved |= {re.sub(r'\s+', ' ', w.strip().lower()) for w in ITALIC.findall(left)}
LONGER = sorted(w for w in dissolved if w != re.sub(r'\s+', ' ', WORD.lower()) and PAT.search(w))
LONG = [(w, whole(w)) for w in LONGER]
WITHIN = []                                   # a place within a longer dissolved word: passed over, that word's own place
TWICE = []                                    # a place its saying would be beside its own word again, as each each: passed over, for its own reading
def said_by(m):
    w = m.group(0); s = m.string
    for lw, rx in LONG:
        if any(x.start() <= m.start() and m.end() <= x.end() for x in rx.finditer(s)):
            WITHIN.append((lw, s[max(0, m.start() - 70):m.end() + 50])); return w
    before = re.search(r'([\w-]+)\W*$', s[:m.start()]); after = re.match(r'\W*([\w-]+)', s[m.end():])
    if (before and before.group(1).lower() == SAYING.split()[0].lower()) or (after and after.group(1).lower() == SAYING.split()[-1].lower()):
        TWICE.append(s[max(0, m.start() - 70):m.end() + 50]); return w
    return SAYING[0].upper() + SAYING[1:] if w[0].isupper() else SAYING
MENTION = re.compile(r'`[^`]*`|(?<!\*)\*(?!\*)[^*\n]+?(?<!\*)\*(?!\*)|"[^"]*"|“[^”]*”')
def sweep_line(l):
    """a line with each plain place re-said, and its number of places: each mention as it is"""
    out = []; at = 0; n = 0
    for m in MENTION.finditer(l):
        seg, k = PAT.subn(said_by, l[at:m.start()]); out.append(seg); n += k; out.append(m.group(0)); at = m.end()
    seg, k = PAT.subn(said_by, l[at:]); out.append(seg); n += k
    new = ''.join(out)
    return new, len(PAT.findall(l)) - len(PAT.findall(new))          # the places re-said: a mention and a place passed over are in both
norm = lambda s: re.sub(r'\s+', ' ', s.replace('*', '').replace('’', "'").replace('‘', "'")).strip()
def sweep_text(text):
    L = text.split('\n'); fence = False; changed = []; passed = []
    heads = {norm(re.sub(r'^#+\s*', '', l)) for l in L if l.startswith('#')}
    for k, l in enumerate(L):
        if l.startswith('```'): fence = not fence; continue
        if fence or k == 0: continue
        if l.startswith('#') or (l.startswith('- ') and norm(l[2:]) in heads):       # a heading, and its line of the contents: an address
            if PAT.search(l): passed.append(l)
            continue
        new, n = sweep_line(l)
        if n: changed.append((k, l, new, n)); L[k] = new
    return '\n'.join(L), changed, passed
def sentence_at(l, new):
    """the sentences of a line having a place, as they are and as re-said"""
    a = re.split(r'(?<=[.?!:])\s+', l); b = re.split(r'(?<=[.?!:])\s+', new)
    return [(x, y) for x, y in zip(a, b) if x != y] if len(a) == len(b) else [(l[:160], new[:160])]

writes = {}; total = 0
for stem, gtitle in FIRST:
    p = newest(stem); name = os.path.basename(p); copy = name not in LISTED
    before = open(p, encoding='utf-8').read(); after, changed, passed = sweep_text(before)
    n = sum(c[3] for c in changed); total += n if copy else 0
    print(f"\n{name} · {'a copy' if copy else 'a living file of the list, read and not written'} · {n} places")
    for k, l, new, _ in changed:
        for x, y in sentence_at(l, new): print(f'    as it is:  {x[:230]}\n    re-said:   {y[:230]}')
    for l in passed: print(f'    an address, a heading or its line of the contents, as it is: {l[:150]}')
    if not (copy and n): continue
    writes[p] = after
    # its gathering file's quotations, word for word before and word for word after
    g = os.path.join(R, 'gathering-value', gtitle + '.md'); G = open(g, encoding='utf-8').read().split('\n'); q = 0; own = 0
    b_n, a_n = norm(before), norm(after)
    for k, l in enumerate(G):
        if not l.startswith('- '): continue
        for rx in (r'(- \*\*Possible incohering\*\* · ")(.*?)(" →)', r'( — at ")(.*)("\s*$)'):
            m = re.search(rx, l) if rx.startswith('( ') else re.match(rx, l)
            if m and PAT.search(m.group(2)) and norm(m.group(2)) in b_n:
                new_q = PAT.sub(said_by, m.group(2))
                assert norm(new_q) in a_n, f'a quotation of {gtitle} is not word for word after the sweep: {m.group(2)[:90]}'
                rest, r = sweep_line(l[m.end(2):]) if rx.startswith('(- ') else (l[m.end(2):], 0)     # the droplet's own re-saying of that sentence, with it
                l = l[:m.start(2)] + new_q + rest; q += 1; own += r
        G[k] = l
    if q: writes[g] = '\n'.join(G)
    print(f"    quotations of its gathering file re-said with their sentences: {q}; places of those droplets' own words after a quotation, re-said with it: {own}")

print(f"\n*{WORD}* said by *{SAYING}*: {total} places with the copy's files")
if LONGER: print('  a longer word dissolved with this word whole within it, its places its own sweep\'s: ' + ', '.join(f'*{w}*' for w in LONGER))
for lw, x in sorted(set(WITHIN)): print(f"  as it is, a place of *{lw}* and no place of this sweep: \u2026{x}\u2026")
for x in sorted(set(TWICE)): print(f"  as it is, its saying beside its own word again, for its own reading: \u2026{x}\u2026")
if APPLY and writes:
    for p, t in writes.items(): open(p, 'w', encoding='utf-8').write(t)
    print('written: ' + ', '.join(os.path.basename(p) for p in writes))
else:
    print('nothing written')
