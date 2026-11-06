"""Next version check, do-no-harm (Geodesic Improving Method 1.5: a split is safe when its parts reconstitute its whole).

A next version is its prior version improving at do-no-harm: the prior's value cohering further, its explaining
placed at the file it explains, and the droplets from the gathering co-chained in. This check reads the prior
version against the next version and the gathering-value files its passages went to, and lists:

  1. each word of the prior with zero across all of them (a real loss), the dissolved words aside;
  2. each sentence of the prior's prose found neither at the next version nor at a gathering-value file,
     each one to read by its claim: said again at the next version, or a loss to mend.

Usage, at the repository root:
  python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/next_version_check.py PRIOR NEXT [GATHERING ...] [--dissolved w1,w2,...]
"""
import re, sys, collections

args = sys.argv[1:]
dissolved = set()
if '--dissolved' in args:
    i = args.index('--dissolved'); dissolved = set(args[i + 1].split(',')); del args[i:i + 2]
prior, nxt, gathering = args[0], args[1], args[2:]
read = lambda p: open(p, encoding='utf-8').read()
words = lambda t: collections.Counter(re.findall(r"[a-z][a-z'-]*[a-z]|[a-z]", t.lower()))
norm = lambda s: re.sub(r'[*`]', '', s)

P = read(prior); N = read(nxt); G = '\n'.join(read(g) for g in gathering)
have = words(N) + words(G)
lost = sorted(w for w in words(P) if w not in have and w not in dissolved)
print('1. Words of the prior with zero across the next version and the gathering-value files:', len(lost))
for w in lost: print('   ', w)

Nn, Gn = norm(N), norm(G)
incode, missing = False, []
for n, s in enumerate(P.split('\n'), 1):
    if s.startswith('```'): incode = not incode; continue
    if incode or not s.strip() or s.startswith('|') or s.lstrip().startswith('- '): continue
    for sen in re.split(r'(?<=[.:])\s+', norm(s)):
        sen = sen.strip()
        if len(sen.split()) < 5: continue
        if sen.rstrip('.') in Nn or sen in Gn: continue
        missing.append((n, sen))
print('2. Sentences of the prior at neither, each to read by its claim:', len(missing))
for n, s in missing: print('    line %d: %s' % (n, s[:200]))
