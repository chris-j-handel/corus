"""Reads Exhibit TWENTY Natural Naming's living file and lays each dissolving word with the natural naming it is said by, deciding nothing.

Usage: python3 -I dissolving_words_by_natural_naming.py <repository root> [--page]

It reads four places of the living file, each by its own form:
  - Dissolved words, each with its saying: each entry's words, and the italic namings of its saying
  - One family of words: each of the three, and a doer or a built form, with its words
  - One sense per foundation word: each sense of *turn* and each word dissolving with it
  - Set namings gathering: each one name with the similar namings it gathers
and the namings of its part FIVE, each by its heading, and the seventeen names.
It says: each natural naming with each dissolving word said by it; each entry said by no naming in italics;
each word in more than one entry; and each dissolving word in the file's own sentences outside those four places.
A recorded result, 15 November 2026, at the living file v401mgr: see the page it writes with --page.
"""
import glob, os, re, sys
ROOT = sys.argv[1]
path = sorted(glob.glob(os.path.join(ROOT, 'Exhibit_TWENTY_Natural_Naming_v*.md')))[-1]
L = open(path, encoding='utf-8').read().split('\n')

def span(start, end):
    i = next(k for k, l in enumerate(L) if l.startswith(start))
    j = next(k for k in range(i + 1, len(L)) if L[k].startswith(end))
    return i, j

ital = lambda s: [w.strip() for w in re.findall(r'(?<!\*)\*([^*]+)\*(?!\*)', s) if w.strip() and w.strip() != 'a']
names17 = re.compile(r'\b\d{1,2}-(?:now|next)-[a-z-]+')

def said_by(said):
    """the namings a saying opens with: its italics and names of the seventeen before its first colon, or each of them with no colon"""
    first = said.split(':', 1)[0]
    first = re.sub(r' for \*[^*]+\*', ' ', first)      # "*winds on* for *closes*": the second is the dissolving word
    return ital(first) + names17.findall(first)

def entries(i, j):
    """each '- head' with its said-by, one line with ' · *a* ' or two lines"""
    out = []
    k = i
    while k < j:
        l = L[k]
        if l.startswith('- '):
            head, said = l[2:], ''
            if ' · *a* ' in head:
                head, said = head.split(' · *a* ', 1)
            elif k + 1 < j and L[k + 1].lstrip().startswith('- *a* '):
                said = L[k + 1].lstrip()[6:]
                k += 1
            out.append((head, said))
        k += 1
    return out

i24, j24 = span('## 2.4 ', '## 2.5 ')
i23, j23 = span('## 2.3 ', '## 2.4 ')
i25, j25 = span('## 2.5 ', '## 2.6 ')
i63, j63 = span('## 6.3 ', '## 6.4 ')
i5, j5 = span('# FIVE ', '# SIX ')

dissolved = []          # (words, said-by text, namings, place)
for head, said in entries(i24, j24):
    ws = ital(head) or [re.sub(r'\*', '', head).strip()]
    dissolved.append((ws, said, [n for n in said_by(said) if n.lower() not in {w.lower() for w in ws}], 'Dissolved words'))
for head, said in entries(i25, j25):
    ws = ital(head) or [re.sub(r'\*', '', head).strip()]
    dissolved.append((ws, said, said_by(said), 'One sense per foundation word'))
family = [(re.sub(r'\*', '', h).strip(), ital(s)) for h, s in entries(i23, j23)]
gathers = []
for head, said in entries(i63, j63):
    one = re.findall(r'\*\*([^*]+)\*\*', head)
    if one:
        gathers.append((one, said))
part5 = [re.sub(r' — binary$', '', l.split(' ', 2)[2]) for l in L[i5:j5] if l.startswith('## 5.')]

clusters = {}
for ws, said, ns, place in dissolved:
    for n in dict.fromkeys(ns):
        clusters.setdefault(n, []).extend(ws)
none = [(ws, said) for ws, said, ns, place in dissolved if not ns]
seen = {}
for ws, said, ns, place in dissolved:
    for w in ws:
        seen.setdefault(w.lower(), []).append(place)
twice = {w: p for w, p in seen.items() if len(p) > 1}

# each dissolving word in the file's own sentences outside the four places, italics and code and quotes passed over
body = [l for k, l in enumerate(L) if not (i23 <= k < j25 or i63 <= k < j63) and not l.startswith('#')]
def plain(l):
    l = re.sub(r'`[^`]*`', ' ', l)
    l = re.sub(r'(?<!\*)\*(?!\*)[^*]+?(?<!\*)\*(?!\*)', ' ', l)
    return re.sub(r'"[^"]*"', ' ', l)
text = ' '.join(plain(l) for l in body).lower()
living_use = {}
for ws, said, ns, place in dissolved:
    for w in ws:
        w0 = w.lower()
        if re.fullmatch(r"[a-z][a-z' -]*", w0) and len(w0) > 2:
            n = len(re.findall(r'(?<![a-z-])' + re.escape(w0) + r'(?![a-z-])', text))
            if n:
                living_use[w0] = n

print('living file:', os.path.basename(path))
print('entries of dissolving words:', len(dissolved), '| words in them:', sum(len(d[0]) for d in dissolved))
print('natural namings said-by, in italics or of the seventeen:', len(clusters))
print('entries said by no naming in italics:', len(none))
print('words in more than one entry:', len(twice))
print('dissolving words in the file\'s own sentences outside the four places:', len(living_use), '| places:', sum(living_use.values()))
print('namings of part FIVE:', len(part5), '| one names of Set namings gathering:', len(gathers), '| the family of words:', len(family))

if '--page' in sys.argv:
    o = []
    o.append('## 1 Each natural naming, with each dissolving word said by it\n')
    o.append('A naming here is in italics in an entry\'s saying, or is one of the seventeen names. The most first.\n')
    for n, ws in sorted(clusters.items(), key=lambda x: (-len(set(x[1])), x[0].lower())):
        o.append(f'- **{n}** ← ' + ' · '.join(f'*{w}*' for w in dict.fromkeys(ws)))
    o.append('\n## 2 Each entry said by no naming in italics\n')
    for ws, said in none:
        o.append('- ' + ', '.join(f'*{w}*' for w in ws) + ' → ' + (said[:160] + ('…' if len(said) > 160 else '')))
    o.append('\n## 3 Each word in more than one entry\n')
    for w, p in sorted(twice.items()):
        o.append(f'- *{w}*: {len(p)} entries')
    o.append('\n## 4 Each dissolving word in the file\'s own sentences, outside the four places\n')
    o.append('A word in italics, in code or in quotation marks is passed over as a mention. A word with one sense that is and one that is not is here too: the instrument matches a word, and no sense.\n')
    for w, n in sorted(living_use.items(), key=lambda x: (-x[1], x[0])):
        o.append(f'- *{w}*: {n}')
    o.append('\n## 5 The family of words, each with its words\n')
    for h, ws in family:
        o.append(f'- **{h}** ← ' + ' · '.join(f'*{w}*' for w in ws))
    o.append('\n## 6 Each one name of Set namings gathering, with the similar namings it gathers\n')
    for one, said in gathers:
        o.append('- ' + ', '.join(f'**{x}**' for x in one) + ' ← ' + said)
    o.append('\n## 7 Each naming of part FIVE, in its order\n')
    o.append(' · '.join(part5))
    sys.stdout.write('\n=====PAGE=====\n' + '\n'.join(o) + '\n')
