"""One sweep of the next version's copy: *an other* with no thing named after it, of a thing that is no self,
said with its thing after it, as *each as resolving as an other resolving*. One kind of improving with one
sweep, all or none at all, by each place.
Its ground: Exhibit ONE Natural Resolver has each place of *an other* a self a self is bi-coupling with, and
its gathering file has *An other is an other self prior-and-same-and-now-existing*.
Reads the set's list of living files; the newest at the root of Natural Intelligence and of Exhibit THIRTY
Co-Chaining Logic Registry; and each one's gathering file. Executes; decides nothing.
With *apply* it writes a living file only as a copy: a file at the root that is not of the set's list of
living files. A living file of the list is read, each of its places said, and never written.

Use: python3 -I incoming/v404helping/instruments/a_sweep_of_an_other_with_its_thing.py <root>          each place as it is and as re-said, and nothing written
     python3 -I incoming/v404helping/instruments/a_sweep_of_an_other_with_its_thing.py <root> apply    the sweep, written with each copy

What it reads. A place is a line of PLACES below: its living file, its gathering file, its words as the sweep
of *another* has them, and its thing. A living file of the list has the place with *another*, and a copy with
*an other*: the place is found once in its file by one of the two, or this instrument halts with nothing
written. A place re-said already, its thing after it, is said and passed over.
A droplet of the place's gathering file with the place's words is re-said with it, its quotation and its own
re-saying of that sentence: each quotation of such a droplet, a possible incohering's opening one and a
droplet's closing one, is word for word a sentence of the copy after, bold and italic marks passed over, or
this instrument halts with nothing written.

Returned with a scratch folder of the next version's draft as it was after Merge #842, 16 November 2026,
applied: eleven places, four of Natural Intelligence and seven of Exhibit THIRTY Co-Chaining Logic Registry;
five droplets of their gathering files re-said with them, two of Natural Intelligence's and three of Exhibit
THIRTY Co-Chaining Logic Registry's. With it: check_set ALL PASS, the opening's seventy sentences word for
word in Exhibit THIRTY Co-Chaining Logic Registry; Exhibit ONE Natural Resolver one and its code executing;
the reader check's first reading 755 and 46, as before; and each of the two gathering checks the same answer
as with the draft before. Nothing of it is in the draft: the scratch folder is away.
With main's living files, after Merge #842: eleven places, each with *another*, each said, and nothing written.
"""
import glob, json, os, re, sys

R = sys.argv[1]; APPLY = len(sys.argv) > 2 and sys.argv[2] == 'apply'
ver = lambda p: int(re.search(r'_v(\d+)', p).group(1))
newest = lambda stem: max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver)
LISTED = set(json.load(open(os.path.join(R, 'files.json'), encoding='utf-8')))
NI, CC = ('Natural_Intelligence', 'Natural_Intelligence'), ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'Co-Chaining_Logic_Registry')

# a place: (its living file and its gathering file, its words as the sweep of *another* has them, its words with its thing, its thing)
PLACES = [
    (NI, 'of no size against an other', 'of no size against an other resolving', 'resolving'),
    (NI, 'each as resolving as an other', 'each as resolving as an other resolving', 'resolving'),
    (NI, 'repeating or replacing an other', 'repeating or replacing an other numbering', 'numbering'),
    (NI, 'receiving + for an other', 'receiving + for an other sharing', 'sharing'),
    (CC, 'its size against an other', 'its size against an other resolving', 'resolving'),
    (CC, 'scaling by rate an other', 'scaling by rate an other operation', 'operation'),
    (CC, 'step 258, is an other', 'step 258, is an other relation', 'relation'),
    (CC, 'each leaving an other whole', 'each leaving an other opening whole', 'opening'),
    (CC, "one scale sizing an other's", "one scale sizing an other scale's", 'scale'),
    (CC, "sentences reaching an other's sections", "sentences reaching an other file's sections", 'file'),
    (CC, 'receiving + with an other', 'receiving + with an other sharing', 'sharing'),
]
norm = lambda s: re.sub(r'\s+', ' ', s.replace('*', '').replace('’', "'").replace('‘', "'")).strip()


def pattern(words, thing):
    """the place's words, with its thing not after them already"""
    tail = '' if words.endswith(' whole') or words.endswith(' sections') or words.endswith("'s") else r'(?!\s+' + re.escape(thing) + r'\b)'
    return re.compile(re.escape(words) + tail + r'(?![\w-])')


def sentence_with(text, at):
    a = max(text.rfind('. ', 0, at), text.rfind('\n', 0, at)); z = [x for x in (text.find('. ', at), text.find('\n', at)) if x != -1]
    return text[a + 1:(min(z) + 1) if z else len(text)].strip()


texts, gathers, writes, said_places, said_droplets = {}, {}, {}, 0, 0
for (stem, gtitle), copy_words, new_words, thing in PLACES:
    p = newest(stem); name = os.path.basename(p); is_copy = name not in LISTED
    t = texts.setdefault(p, open(p, encoding='utf-8').read())
    main_words = copy_words.replace('an other', 'another'); main_new = new_words
    done = len(re.findall(re.escape(new_words) + r'(?![\w-])', t))
    found = [(w, m) for w in (copy_words, main_words) for m in pattern(w, thing).finditer(t)]
    if done == 1 and not found:
        print(f'{name} · re-said already, its thing after it: {new_words}'); continue
    assert len(found) == 1 and done == 0, f'{name}: the place is found {len(found)} times and re-said {done} times, and nothing is written: {copy_words}'
    w, m = found[0]
    assert not (is_copy and w == main_words), f'{name}: a copy has the place with *another*, the sweep of *another* not yet with it, and nothing is written: {main_words}'
    print(f"{name} · {'a copy' if is_copy else 'a living file of the list, read and not written'}")
    print(f'    as it is:  {sentence_with(t, m.start())[:260]}')
    new_t = t[:m.start()] + new_words + t[m.end():]
    print(f'    re-said:   {sentence_with(new_t, m.start())[:260]}')
    said_places += 1
    if not is_copy:
        continue
    texts[p] = new_t; writes[p] = new_t
    # its gathering file: each droplet with the place's words, its quotation and its own re-saying of that sentence
    g = os.path.join(R, 'gathering-value', gtitle + '.md')
    G = gathers.setdefault(g, open(g, encoding='utf-8').read().split('\n'))
    for k, l in enumerate(G):
        if l.startswith('- ') and pattern(w, thing).search(l):
            G[k] = pattern(w, thing).sub(new_words, l); said_droplets += 1
            print(f'    its gathering file, a droplet re-said with it: {l[:110]}')
            writes[g] = None

# each quotation of a droplet re-said is word for word a sentence of the copy after
for g, G in gathers.items():
    if g not in writes: continue
    stem = next(s for (s, gt), _, _, _ in PLACES if os.path.join(R, 'gathering-value', gt + '.md') == g)
    living = norm(texts[newest(stem)])
    before = open(g, encoding='utf-8').read().split('\n')
    for k, l in enumerate(G):
        if l == before[k]: continue
        for rx in (r'^- \*\*Possible incohering\*\* · "(.*?)" →', r' — at "(.*)"\s*$'):
            q = re.search(rx, l)
            assert not q or norm(q.group(1)) in living, f'a quotation is not word for word after the sweep, and nothing is written: {q.group(1)[:100]}'
    writes[g] = '\n'.join(G)

print(f"\n*an other* said with its thing: {said_places} places said; {sum(1 for p in writes if not p.endswith(os.sep) and 'gathering-value' not in p)} copies and {said_droplets} droplets of their gathering files re-said")
if APPLY and writes:
    for p, t in writes.items(): open(p, 'w', encoding='utf-8').write(t)
    print('written: ' + ', '.join(os.path.relpath(p, R) for p in writes))
else:
    print('nothing written')
