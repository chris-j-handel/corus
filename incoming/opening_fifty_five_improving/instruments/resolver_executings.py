"""Resolver executings: Exhibit ONE's own code, executed at named cases.

Usage:  python3 resolver_executings.py <repository>

What it does: reads Exhibit ONE's code block out of the living file as it
stands, writes it to a folder of its own, and executes it at the cases the
gathering-value of Natural Intelligence names, returning each self's sharing
with 10 at each momentary. Each returned row stands at a sentence of the
gathering-value, quoted beside it here.

Its refusings, each with its consequence:
 · It reads the first python code block of Exhibit ONE; a file of another shape
   is not read, and it says so.
 · It returns a self's sharing with 10 by executing 1-now-existing alone at each
   momentary beside the whole society's 17-next-existing; a reading of any other
   name of the seventeen is not returned.
 · It executes six momentaries by default, eight at the one case whose gathered
   sentence names eight; a longer running is a working's own.
"""
import re, sys, os, tempfile

repo = sys.argv[1].rstrip('/')
one = [f for f in os.listdir(repo) if f.startswith('Exhibit_ONE_')][0]
text = open(repo + '/' + one, encoding='utf-8').read()
FENCE = chr(96) * 3
m = re.search(FENCE + r'python\n(.*?)\n' + FENCE, text, re.S)
if not m:
    print('no python code block at', one); sys.exit(0)
d = tempfile.mkdtemp()
open(os.path.join(d, 'resolver.py'), 'w').write(m.group(1))
sys.path.insert(0, d)
import resolver
print(f'Exhibit ONE read: {one}, its code {len(m.group(1).splitlines())} lines')

def sharings(soc, co_ex, n):
    out = {k: [] for k in soc}
    for _ in range(n):
        for k, (obs, pos) in soc.items():
            ten, _ = resolver._1_now_existing(obs, pos)
            out[k].append(dict(ten).get('k'))
        soc = resolver._17_next_existing(soc, co_ex)
    return out

both = {('a', 10): 'b', ('b', 10): 'a'}
cases = [
 ('two selves alike, prior +, bi-coupling both ways',
  lambda: sharings({'a': ([('k', 1)], []), 'b': ([('k', 1)], [])}, both, 6),
  'returns −, 0, +, 0, −, 0 for each'),
 ('two selves, priors + and −, bi-coupling both ways',
  lambda: sharings({'a': ([('k', 1)], []), 'b': ([('k', -1)], [])}, both, 6),
  'each sharing its changing with each momentary, −, +, −, + and +, −, +, −, with no 0'),
 ('one self, prior +, a 0 alone received',
  lambda: resolver._1_now_existing([('k', 1)], [('k', 0)]),
  'sharing its own prior inverting, as with its possibling an empty set'),
 ('one self, prior +, nothing received',
  lambda: sharings({'a': ([('k', 1)], [])}, {}, 6),
  'a self with nothing received sharing −, +, −, + with no 0'),
 ('two selves alike, prior +, one way only',
  lambda: sharings({'a': ([('k', 1)], []), 'b': ([('k', 1)], [])}, {('a', 10): 'b'}, 6),
  'the sender −, +, −, +, −, + and the receiver −, 0, +, −, +, −'),
 ('one self, prior +, its own 9 along to itself',
  lambda: sharings({'a': ([('k', 1)], [])}, {('a', 9): 'a'}, 8),
  'one self whose own 9-next-co-discovering reaches it along, −, 0, +, 0, −, 0, +, 0'),
]
for label, run, said in cases:
    print(f'\n· {label}\n    returns: {run()}\n    at the gathered sentence: {said}')
