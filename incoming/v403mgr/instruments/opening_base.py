"""An is and the names in it. Reads Natural Intelligence's living version with its gathering file, and writes none;
it decides nothing. A sentence of the living opening is an is-or-is-not? with a droplet of it in the gathering file,
the sentence with why it is open; an is-not by the noun *momentary*; and an is with neither: a sentence's one of
three is its place.

Use: python3 -I incoming/v403mgr/instruments/opening_base.py <root>

It says three things:
  1. each name the opening has in bold, by the one of three of the sentence first having it in bold, its own sentence
  2. each sentence rated is, with each name in it whose own sentence is an is-or-is-not? or an is-not
  3. each prose sentence of the living version after the opening, Exhibit ONE read at Exhibit ONE, by the names in it
     whose own sentence is an is-or-is-not? or an is-not; and each such name by the sentences having it
A name is found by its word forms: a number of 3 is a number of sentences to read, and no reading of them.
*momentary* is found with *moment*: sentence 50 is an is-not by the noun, and its sentence with *moment* is an is.

Returned at main, Merge #714, 15 November 2026:
  1. 46 names: 11 with their own sentence an is, 34 an is-or-is-not?, 1 an is-not
  2. of the 18 with an is, 1 and 6 have each name's own sentence an is; 69 has *moment* only; each other of the 18,
     fifteen, has a name whose own sentence is an is-or-is-not?
  3. about 1,405 sentences after the opening: 384 with no such name, 393 with one, 278 with two, 203 with three,
     147 with four or more; a self 570, a parity 286, a moment 211, living 143, same-existing 138, a bi-coupling 129,
     a 0 96, an other 88, a same-existing-society 87, receives 83, possibling 67, observing 65, discovering 54
     with *moment* an is: 439 with no such name, 966 with one or more
"""
import collections, glob, os, re, sys

R = sys.argv[1]
ni = open(max(glob.glob(os.path.join(R, 'Natural_Intelligence_v*.md')),
              key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
op = re.search(r'^# Natural Intelligence\n\n\*\*[^\n]*\*\*\n\n(.*?)\n\n\*\*ONE · ', ni, re.S | re.M).group(1)
sent = {n: l.rstrip(' \\') for n, l in enumerate([l for l in op.split('\n') if l.strip()], 1)}
assert len(sent) == 70, len(sent)
gathered = open(os.path.join(R, 'gathering-value', 'Natural_Intelligence.md'), encoding='utf-8').read()
open_at = set(re.findall(r'^- \*\*Possible exploring\*\* · is-or-is-not\? .*— at "(.*?)"$', gathered, re.M))
unbold = lambda s: re.sub(r'\*\*', '', s)
three = {n: 'is-not' if '**momentary**' in s else 'is-or-is-not?' if unbold(s) in open_at else 'is' for n, s in sent.items()}

name_at = {}
for n in sorted(sent):
    for b in re.findall(r'\*\*(.+?)\*\*', sent[n]): name_at.setdefault(b.lower(), n)

def forms(name):
    n = re.escape(name)
    if name == '0': return r'(?<![\w.+-])0(?![\w.])'
    if name == 'me': return r'\bmes?\b(?!-)'
    if name == 'self': return r'\bsel(f|ves)\b(?!-)'
    if name == 'other': return r'\bothers?\b(?!-)'
    if name == 'receives': return r'\breceiv(es|e|ing)\b'
    if name == 'momentary': return r'\bmoments?\b|\bmomentary\b'
    if name == 'parity': return r'(?<![\w-])parit(y|ies)(?![\w-])'
    if name in ('opening', 'completing', 'free', 'living', 'observing', 'possibling', 'discovering', 'improving',
                'agreeing', 'parting', 'geodesic', 'universe'):
        return r'(?<![\w-])' + n + r'(?![\w-])'
    return r'(?<![\w-])' + n.replace(r'\ ', r'[ -]') + r's?(?![\w-])'

pats = {k: re.compile(forms(k), re.I) for k in name_at}
plain = lambda s: re.sub(r'\*\*|\*', '', s)

print('1. names the opening has in bold, each with its own sentence:', len(name_at))
print('   by its own sentence:', dict(collections.Counter(three[v] for v in name_at.values())))
print('2. each sentence rated is, with each name in it whose own sentence is an is-or-is-not? or an is-not')
whole = []
for n in sorted(k for k, r in three.items() if r == 'is'):
    body = plain(sent[n])
    doubt = sorted({(k, v) for k, v in name_at.items() if v != n and pats[k].search(body) and three[v] != 'is'}, key=lambda x: x[1])
    if not doubt: whole.append(n)
    print(f'   {n:2d}  ' + ('each name\'s own sentence an is' if not doubt else ', '.join(f'{k} ({v}, {three[v]})' for k, v in doubt)))
print('   with each name\'s own sentence an is:', whole)

a = ni.find('\n---\n'); body = ni[a:]
x = body.find('# EXHIBIT ONE · NATURAL RESOLVER'); y = body.find('\n# FOUR · RESOLVING')
if 0 < x < y: body = body[:x] + body[y:]
S = []; fence = False
for l in body.split('\n'):
    if l.startswith('```'): fence = not fence; continue
    if fence or l.startswith('#') or l.startswith('|') or not l.strip() or l.strip() == '---': continue
    s = plain(re.sub(r'^[-*]\s+|^\d+\.\s+', '', l.strip()))
    S += [p for p in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(])', s) if len(p.split()) >= 4]
open_names = {k: v for k, v in name_at.items() if three[v] != 'is'}
by_number = collections.Counter(); reach = collections.Counter()
for s in S:
    ks = [k for k in open_names if pats[k].search(s)]
    by_number[min(len(ks), 4)] += 1
    for k in ks: reach[k] += 1
print('3. prose sentences after the opening, about', len(S))
print('   with no such name:', by_number[0], ' with one:', by_number[1], ' two:', by_number[2], ' three:', by_number[3], ' four or more:', by_number[4])
for k, c in reach.most_common(14): print(f'   {c:5d}  {k}  (sentence {name_at[k]}, {three[name_at[k]]})')
with_moment_an_is = {k: v for k, v in open_names.items() if k != 'momentary'}
none = sum(1 for s in S if not any(pats[k].search(s) for k in with_moment_an_is))
print('   with *moment* an is: with no such name', none, ' with one or more', len(S) - none)
