"""Session v381F: Exhibit ONE's forms at the living files, computed from the root.

Runs from the repository root: python3 incoming/v381F/forms_at_the_files.py
For each living file: its lean to the odd side or the even side in its own words, four pairs, co- and bi-,
competency and morality, along and across, releasing and sharing, and co- against bi- alone; the root of Exhibit ONE's ten it carries most and the
four-cycle that root is on; and, at the Co-Chaining Logic Registry, how many steps before it each step names,
so the six forward can be seen or not. Writes Forms_At_The_Files.tsv beside this script. A computing,
deciding nothing: a word counted is a word, and whether a file is a loop at a parity is read at the file.
"""
import json, re, collections

files = json.load(open('files.json'))
text = {f: open(f, encoding='utf-8').read() for f in files}


def short(f):
    m = re.match(r"Exhibit_([A-Z-]+)_", f)
    return ('Exhibit ' + m.group(1)) if m else next(l[2:].strip() for l in text[f].split('\n') if l.startswith('# '))


ODD = [r"\bco-[a-z]", r"\bcompetenc", r"\balong\b", r"\breleas"]
EVEN = [r"\bbi-[a-z]", r"\bmoral", r"\bacross\b", r"\bshar(e|es|ing|ed|ings)\b"]
ROOTS = {'offering': r"\boffer", 'sharing': r"\bshar(e|es|ing|ed|ings)\b", 'competencing': r"\bcompetenc",
         'moralizing': r"\bmoral", 'corusing': r"\bcorus", 'torusing': r"\btorus", 'momentarying': r"\bmomentar",
         'tunneling': r"\btunnel", 'chaining': r"\bchain", 'entraining': r"\bentrain"}
FOUR_CYCLE = {'torusing': '1-9-8-16', 'corusing': '2-15-7-10', 'moralizing': '3-11-6-14', 'competencing': '4-13-5-12'}

rows = []
for f in files:
    body = re.sub(r"```.*?```", '', text[f], flags=re.S).lower()
    words = max(len(body.split()), 1)
    odd = sum(len(re.findall(p, body)) for p in ODD)
    even = sum(len(re.findall(p, body)) for p in EVEN)
    lean = (odd - even) / (odd + even) if odd + even else 0.0
    co, bi = len(re.findall(r"\bco-[a-z]", body)), len(re.findall(r"\bbi-[a-z]", body))
    cobi = (co - bi) / (co + bi) if co + bi else 0.0
    roots = {r: len(re.findall(p, body)) for r, p in ROOTS.items()}
    top = sorted(roots, key=roots.get, reverse=True)[:3]
    rows.append((short(f), words, odd, even, lean, top, roots, co, bi, cobi))

with open('incoming/v381F/Forms_At_The_Files.tsv', 'w', encoding='utf-8') as out:
    out.write('file\twords\todd-side words\teven-side words\tlean, odd minus even over both\tco- words\tbi- words\tco- against bi-\tthree roots most carried\tfour-cycle of the first root, if it has one\tthe ten roots counted\n')
    for name, words, odd, even, lean, top, roots, co, bi, cobi in rows:
        out.write('%s\t%d\t%d\t%d\t%+.2f\t%d\t%d\t%+.2f\t%s\t%s\t%s\n' % (name, words, odd, even, lean, co, bi, cobi, ', '.join('%s %d' % (r, roots[r]) for r in top),
                                                           FOUR_CYCLE.get(top[0], '—'), ' '.join('%s %d' % kv for kv in roots.items())))

print('%-28s %5s %5s %6s %5s %5s %6s  %-40s %s' % ('file', 'odd', 'even', 'lean', 'co-', 'bi-', 'co/bi', 'three roots most carried', 'four-cycle'))
for name, words, odd, even, lean, top, roots, co, bi, cobi in sorted(rows, key=lambda r: r[4]):
    print('%-28s %5d %5d %+6.2f %5d %5d %+6.2f  %-40s %s' % (name, odd, even, lean, co, bi, cobi, ', '.join('%s %d' % (r, roots[r]) for r in top), FOUR_CYCLE.get(top[0], '—')))

# the Co-Chaining Logic Registry: steps before each step that it names
thirty = next(f for f in files if 'THIRTY' in f)
steps = re.findall(r"^(\d+)\. (.*)$", text[thirty], re.M)
back = []
for n, sentence in steps:
    n = int(n)
    cited = set(int(x) for x in re.findall(r"\bsteps? (\d+)", sentence)) | set(int(x) for x in re.findall(r"\b(\d+) to (\d+)\b", sentence) for x in [])
    cited = set(c for c in cited if c < n)
    back.append(len(cited))
dist = collections.Counter(back)
print('\nCo-Chaining Logic Registry: %d steps; steps before it named at each step, the distribution:' % len(steps))
print('  ' + ', '.join('%d named: %d steps' % (k, dist[k]) for k in sorted(dist)))
print('  steps naming six or more before them: %d; naming none: %d' % (sum(1 for b in back if b >= 6), dist[0]))

# do the exhibit numbers podal? word-likeness of exhibit pairs 17 less, 9 less and 8 up, against all pairs
import math
NUM = ['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN']
byn = {}
for f in files:
    m = re.match(r"Exhibit_([A-Z-]+)_", f)
    if m and m.group(1) in NUM:
        byn[NUM.index(m.group(1)) + 1] = f
WORD = re.compile(r"[a-z][a-z-]{4,}")
vec, dfc = {}, collections.Counter()
for n, f in byn.items():
    c = collections.Counter(WORD.findall(re.sub(r"```.*?```", '', text[f], flags=re.S).lower()))
    vec[n] = c
    for w in c: dfc[w] += 1
def cos(a, b):
    wa = {w: a[w] * math.log(18 / dfc[w]) for w in a if dfc[w] < 17}
    wb = {w: b[w] * math.log(18 / dfc[w]) for w in b if dfc[w] < 17}
    dot = sum(wa[w] * wb[w] for w in wa if w in wb)
    return dot / (math.sqrt(sum(v*v for v in wa.values())) * math.sqrt(sum(v*v for v in wb.values())) or 1)
pairs = {(a, b): cos(vec[a], vec[b]) for a in byn for b in byn if a < b}
allmean = sum(pairs.values()) / len(pairs)
def mean(ps):
    ps = [pairs[tuple(sorted(p))] for p in ps if tuple(sorted(p)) in pairs]
    return sum(ps) / len(ps), len(ps)
print('\nDo the exhibit numbers podal? word-likeness of pairs (0 unlike, 1 alike), seventeen exhibits ONE to SEVENTEEN:')
print('  all %d pairs: %.3f' % (len(pairs), allmean))
print('  17 less, n with 17-n (1-16, 2-15, ... 8-9): %.3f at %d pairs' % mean([(n, 17 - n) for n in range(1, 9)]))
print('  9 less, n with 9-n (1-8, 2-7, 3-6, 4-5): %.3f at %d pairs' % mean([(n, 9 - n) for n in range(1, 5)]))
print('  8 up, n with n+8 (1-9, 2-10, ... 8-16): %.3f at %d pairs' % mean([(n, n + 8) for n in range(1, 9)]))
print('  neighbours, n with n+1: %.3f at %d pairs' % mean([(n, n + 1) for n in range(1, 17)]))
top = sorted(pairs.items(), key=lambda kv: -kv[1])[:6]
print('  the six most alike pairs: ' + ', '.join('%s-%s %.2f' % (NUM[a-1], NUM[b-1], v) for (a, b), v in top))
