"""Re-pointing check: the registry's own map for the opening entering, executed.

Usage:  python3 repointing_check.py <repository>

What it does: reads the map out of the Co-Chaining Logic Registry's
gathering-value, the one its waiting entry gives for the fifty-five entering as
steps 1 to 55, and executes it against every step of the living registry. It
returns: how many of the 70 former opening steps the map covers; how many steps
carry a citation; and, re-pointed by the map, each citation pointing at or
after its own step, which co-chaining's rule has no position for.

Its refusings, each with its consequence:
 · It reads a citation as the numbers after *step* or *steps* alone; a citation
   said in words, or a step named by its concept, is passed over and returned
   in no count.
 · It passes over the former opening steps' own citations: those steps become
   the opening, whose sentences carry no citation.
 · A number after *step* that names something other than a step of this
   registry is read as a step; none above 755 is taken.
 · It says nothing of whether a citing step's saying still holds with the
   concept at its new step: that is one binary per step, for a working to meet.
"""
import re, sys

repo = sys.argv[1].rstrip('/')
gvr = open(repo + '/gathering-value/Co-Chaining_Logic_Registry.md', encoding='utf-8').read()
line = [l for l in gvr.split('\n') if l.startswith('- **Waiting to enter** ·')][0]
seg = line.split('former to now:')[1].split('. A citing sentence naming another concept')[0]
m = {}
for part in seg.split(';'):
    mm = re.match(r'^([\d, and]+) to (\d+)$', part.strip().rstrip('.'))
    if mm:
        for f in re.findall(r'\d+', mm.group(1)): m[int(f)] = int(mm.group(2))
shift = re.search(r'the steps (\d+) to (\d+) are steps (\d+) to (\d+), (\d+) less', line)
first, last, less = int(shift.group(1)), int(shift.group(2)), int(shift.group(5))

e30 = [f for f in __import__('os').listdir(repo) if f.startswith('Exhibit_THIRTY_')][0]
text = open(repo + '/' + e30, encoding='utf-8').read()
steps = {int(n): t for n, t in re.findall(r'^(\d+)\.\s(.+)$', text, re.M)}

print(f'the map covers former opening steps: {len(m)} of 70')
print(f'  former steps with no entry: {[n for n in range(1, 71) if n not in m] or "none"}')
print(f'the rest: steps {first} to {last} are {less} less')
print(f'the registry read: {len(steps)} steps, highest {max(steps)}')

def repoint(n): return m[n] if n <= 70 else n - less

forward, citing = [], 0
for s, t in steps.items():
    found = set()
    for mm in re.finditer(r'steps?\s+((?:\d+(?:\s*,\s*|\s+and\s+|\s+to\s+)?)+)', t):
        for n in re.findall(r'\d+', mm.group(1)):
            if 1 <= int(n) <= max(steps): found.add(int(n))
    if found: citing += 1
    if s <= 70: continue
    for n in sorted(found):
        if repoint(n) >= repoint(s): forward.append((s, repoint(s), n, repoint(n)))
print(f'steps carrying a citation: {citing}')
print(f'citations pointing at or after their own step, re-pointed: {len(forward)}')
for s, rs, n, rn in sorted(forward):
    print(f'  · step {s} (new {rs}) cites step {n} (new {rn})')
