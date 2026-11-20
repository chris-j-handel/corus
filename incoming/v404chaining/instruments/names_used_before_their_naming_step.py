"""The opening's seventy sentences: a named word used at a step before the step naming it, and the hyphened
words no step names. All or none at all, by one opening read at one git ref. Executes; writes no file; decides
nothing.

Use: python3 -I incoming/v404chaining/instruments/names_used_before_their_naming_step.py <git ref>
         with the ref of the next version's copy branch, 19 November 2026 it returned no named word used
         before its step, and nine hyphened words no step names: bi-couplings, co-chainings, next-existing,
         now-existing, other-than, prior-existing, prior-existings, same-named, stable-forming

What it reads. Natural_Intelligence_v403mgr.md at the ref, its lines 7 to 80, the seventy sentences. A named
word is a bold word. Its naming step is the step it is first bold at. A use is the word whole, with no case.
"""
import re, subprocess, sys

ref = sys.argv[1]
text = subprocess.run(['git', 'show', ref + ':Natural_Intelligence_v403mgr.md'],
                      capture_output=True, text=True, check=True).stdout.split('\n')
steps = [l.rstrip(' \\').strip() for l in text[6:80] if l.strip()]
assert len(steps) == 70, len(steps)
named = {}
for i, s in enumerate(steps, 1):
    for b in re.findall(r'\*\*(.+?)\*\*', s):
        named.setdefault(b.lower(), i)
def plain(s):
    return re.sub(r'\*\*', '', s).lower()
early = 0
for name, at in sorted(named.items(), key=lambda x: x[1]):
    pat = re.compile(r'(?<![\w-])' + re.escape(name) + r'(?![\w-])')
    for i, s in enumerate(steps[:at - 1], 1):
        if pat.search(plain(s)):
            early += 1
            print(f'{name!r} named at step {at}, used at step {i}: {s}')
print('named words used before their naming step:', early)
hyphened = sorted({w for s in steps for w in re.findall(r'[a-z]+(?:-[a-z]+)+', plain(s))} - set(named))
print('hyphened words no step names:', len(hyphened), hyphened)
