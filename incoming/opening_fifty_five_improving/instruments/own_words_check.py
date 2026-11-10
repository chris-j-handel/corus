"""Own-words check: a session's own words read against Natural Naming 2.4's
dissolved words, one binary per word. Usage:
  python3 own_words_check.py <repository> <file to read> [<file> ...]
Quoted sentences and code are left out: a quotation is the file it is from,
and this reads the session's own voice alone."""
import re, sys, collections

repo = sys.argv[1].rstrip('/')
nn = open(repo + '/Exhibit_TWENTY_Natural_Naming_v393.md', encoding='utf-8').read()
sec = nn.split('## 2.4 Dissolved words')[1].split('## 2.5')[0]

# each entry of 2.4: its dissolved terms, and the saying that replaces them
entries = []
for block in re.split(r'\n- ', sec)[1:]:
    head = block.split('\n')[0]
    said = ''
    m = re.search(r'\*a\*\s(.+)', block, re.S)
    if m: said = ' '.join(m.group(1).split())[:150]
    terms = [t.strip() for t in re.findall(r'\*([a-z][a-z \-\']*?)\*', head)]
    for t in terms:
        # 2.4's own structure: a term standing as its entry's replacement is the
        # saying, not the dissolved word; it does not flag.
        if t and not re.search(r'(?<![a-z\-])' + re.escape(t) + r'(?![a-z\-])', said.lower()):
            entries.append((t, head.replace('*',''), said))

GRAMMAR = {'a','as','at','in','is','has','so','with','each','every','next','now','out',
           'more','less','half','halves','since','when','where','what','how','would',
           'neither','never','same','not same','our','read','give','gives','take','takes',
           'taken','keep','keeps','hold','holding','stand','stands','start','begin',
           'call','tell','run','runs','going','goes on','has','there','right','left',
           'one at a time','all or none at all','binary','observing','discovering',
           'opening','completing','sharing','agreeing','parting','living','moment',
           'momentary','momentarying','society','same-existing','same-existing-society',
           'stable-forming','stable form','co-intelligencing','method','aiming','across',
           'along','podal','key','kind','natural torusing','still-possibling','exhausting',
           'ingesting','fixing','harm','free','exploring','seam','artifact','artifacts',
           'emanation','code','complete','forward','backward','differing','sign','signs'}

def own_voice(text):
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)          # code, not own voice
    text = re.sub(r'"[^"]*"', ' ', text)                         # a quotation is its file's
    text = re.sub(r'\*"[^"]*"\*', ' ', text)
    return text

for path in sys.argv[2:]:
    text = own_voice(open(path, encoding='utf-8').read())
    low = text.lower()
    strong, sense = [], []
    for term, head, said in entries:
        if term in GRAMMAR: continue
        pat = r'(?<![a-z\-])' + re.escape(term) + r'(?![a-z\-])'
        hits = len(re.findall(pat, low))
        if not hits: continue
        (strong if (' ' in term or len(term) > 5) else sense).append((hits, term, head, said))
    seen = set(); strong = [e for e in strong if not (e[1] in seen or seen.add(e[1]))]
    print('\n==', path.split('/')[-1])
    print('   dissolved words in this file\'s own voice:',
          len(strong), 'to meet,', len(sense), 'to read for sense')
    for hits, term, head, said in sorted(strong, reverse=True):
        print('   ·', term, '×', hits, '\n       2.4:', head[:110])
        if said: print('       said by:', said[:110])
    if sense:
        print('   for sense:', ', '.join(t for _, t, _, _ in sorted(sense, reverse=True)))
