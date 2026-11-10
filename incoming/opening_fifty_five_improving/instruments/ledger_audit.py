"""Ledger audit: a derivings ledger met against the registry's own specification.

Usage:  python3 ledger_audit.py <repository> <ledger.md>

What it does: the Co-Chaining Logic Registry's gathering-value specifies these
steps, "each with an *Adding* line naming in the step's own words the concept it
adds, each group's *Entering* line its *Adding* lines joined". This meets a
ledger against both halves: each adding line's words against its own sentence's
words and the ledger's own form words, and each entering line against its
group's adding lines joined. It also returns each word of a sentence standing at
no line of its own step or of a step before it, which is the opening's own rule,
no word staying unless the logic stays living only with it.

Its refusings, each with its consequence:
 · It holds a list of the ledger's own form words, articles, order words and the
   set's roots; a word of that list is passed over in both directions.
 · It matches a word to its sentence by stem alone, so a word differing from the
   sentence's by more than a plural or a possessive is returned as a stray, and
   a reader meets whether it is the sentence's word said living.
 · It reads a group's bounds from the ledger's own gatherings; a ledger of other
   bounds is read with those.
"""
import re, sys

repo = sys.argv[1].rstrip('/')
der = open(sys.argv[2], encoding='utf-8').read()
FORM = {'adding','entering','a','an','the','its','it','with','and','or','of','at','in',
        'each','no','not','one','two','three','four','own','by','to','from','as','is',
        'are','that','this','before','after','only','within','whose','what','which',
        'said','naming','step','steps','concept','concepts','inception','nothing',
        'brought','them','their','both','same','all','none','other','others','line',
        'lines','for','on','side','sides','order','together','through','out','s'}
def words(s): return [w for w in re.split(r"[^a-z0-9-]+", s.lower()) if w]

sents = {int(n): t.strip() for n, t in re.findall(r'^(\d+)\.\s(.+)$', der, re.M)}
adds = {int(n): a for n, a in re.findall(r'^(\d+)\.\s.+?\n\n\s+\*Adding: (.+?)\*', der, re.M | re.S)}
ents = re.findall(r'\*Entering: (.+?)\*', der, re.S)
print(f'the ledger read: {len(sents)} steps, {len(adds)} adding lines, {len(ents)} entering lines')

nums = sorted(sents)
bounds, start = [], nums[0]
for i, n in enumerate(nums):
    if i + 1 == len(nums) or nums[i + 1] - n > 1 or len(bounds) + 1 == len(ents) and i + 1 == len(nums):
        pass
# groups by the ledger's own gatherings: each entering line precedes its steps
parts = re.split(r'\*Entering: .+?\*', der, flags=re.S)[1:]
groups = [[int(n) for n, _ in re.findall(r'^(\d+)\.\s(.+)$', p, re.M)] for p in parts]

print('\n== adding lines: a word at neither its sentence nor the ledger\'s form')
strays = 0
for n in nums:
    sw = set(words(sents[n]))
    for w in words(adds.get(n, '')):
        if w in FORM or w in sw: continue
        if w.rstrip('s') in sw or (w + 's') in sw: continue
        strays += 1
        print(f'   · {n}: "{w}"  ·  {adds[n][:70]}')
print(f'   strays: {strays}')

print('\n== entering lines: each its group\'s adding lines joined')
for i, g in enumerate(groups):
    joined = set()
    for n in g: joined |= set(words(adds.get(n, '')))
    extra = sorted(w for w in set(words(ents[i])) - joined if w not in FORM)
    print(f'   · group {i+1} ({g[0]} to {g[-1]}): words at no adding line of it: {extra or "none"}')

print('\n== each sentence\'s words at a line of its own step or a step before it')
allowed = set()
for i, g in enumerate(groups): allowed |= set(words(ents[i]))
missing = {}
for n in nums:
    allowed |= set(words(adds.get(n, '')))
    for w in words(sents[n]):
        if w in FORM or w in allowed: continue
        if w.rstrip('s') in allowed or (w + 's') in allowed or w.rstrip("'s") in allowed: continue
        missing.setdefault(n, []).append(w)
for n, ws in missing.items(): print(f'   · sentence {n}: {ws}')
print(f'   sentences with a word at no line: {len(missing)}')
