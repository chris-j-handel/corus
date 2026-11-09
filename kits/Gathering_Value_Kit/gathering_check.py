"""Reads a gathering-value file against its living file and says what it finds, deciding nothing.

Usage: python3 -I kits/Gathering_Value_Kit/gathering_check.py <Title> [base]
  <Title>  the gathering-value's name, as gathering-value/<Title>.md, for example Natural_Naming
  [base]   the commit its added lines are read against, origin/main if not given

It says four things:
  1. each numbered section of the living file, in order, with its heading at the gathering-value, word for word
  2. each quoted living-file sentence, a possible incohering's "..." and a possible exploring's — at "...",
     found word for word in the living file (bold and italic marks passed over)
  3. released words among the lines added beyond base, italics, code and quotes passed over as mentions
  4. the number of items, at base and now
A heading renamed at the living file with its gathering-value following shows at 1 until both are one;
a quote at 2 is a sentence the living file no longer has, its droplet resolved or needing its sentence again.
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
title = sys.argv[1]
base = sys.argv[2] if len(sys.argv) > 2 else 'origin/main'
gpath = os.path.join(ROOT, 'gathering-value', title + '.md')
gather = open(gpath, encoding='utf-8').read()
prior = subprocess.run(['git', '-C', ROOT, 'show', f'{base}:gathering-value/{title}.md'],
                       capture_output=True, text=True).stdout
found = 0

def say(msg):
    global found
    found += 1
    print('  FOUND', msg)

def ver(p):
    m = re.search(r'_v(\d+)[A-Za-z]?\.md$', p)
    return int(m.group(1)) if m else 0

cands = [p for p in glob.glob(os.path.join(ROOT, '*.md'))
         if re.match(r'^(Exhibit_[A-Z-]+_)?' + re.escape(title) + r'_v\d+[A-Za-z]?\.md$', os.path.basename(p))]
if not cands:
    sys.exit(f'no living file at root for {title}')
living_path = max(cands, key=ver)
living = open(living_path, encoding='utf-8').read()
print('living file:', os.path.basename(living_path))

def norm(s):
    s = s.replace('*', '').replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s).strip()
living_n = norm(living)

# 1 numbered sections, in order
lh = re.findall(r'^## (\d+\.\d+ .*)$', living, re.M)
gh = re.findall(r'^### (\d+\.\d+ .*)$', gather, re.M)
if lh == gh:
    print(f'  sections: {len(lh)}, in order, word for word')
else:
    for i, (a, b) in enumerate(zip(lh, gh)):
        if a != b:
            say(f'section {i + 1}: living {a!r}, gathering-value {b!r}')
            break
    if len(lh) != len(gh):
        say(f'sections: living {len(lh)}, gathering-value {len(gh)}')

# 2 quotes
items = [l for l in gather.splitlines() if l.startswith('- ')]
nq = 0
for l in items:
    qs = []
    m = re.match(r'- \*\*Possible incohering\*\* · "(.*?)" →', l)
    if m: qs.append(m.group(1))
    m = re.search(r' — at "(.*)"\s*$', l)
    if m: qs.append(m.group(1))
    for q in qs:
        nq += 1
        if norm(q) not in living_n:
            say('a quote not word for word at the living file: ' + q[:110])
print(f'  quotes read: {nq}')

# 3 released words among added lines
rw = set()
for l in open(os.path.join(ROOT, 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt'), encoding='utf-8'):
    l = l.strip()
    if l and not l.startswith('#'):
        rw.add(l.lower())
plines = set(prior.splitlines())
for l in gather.splitlines():
    if l in plines or not l.strip():
        continue
    plain = re.sub(r'`[^`]*`', ' ', l)
    plain = re.sub(r'(?<!\*)\*(?!\*)[^*]+?(?<!\*)\*(?!\*)', ' ', plain)
    plain = re.sub(r'"[^"]*"', ' ', plain)
    for w in re.findall(r"[A-Za-z]+", plain):
        if w.lower() in rw:
            say(f'released word {w!r} in an added line: {l[:100]}')

# 4 items
pi = sum(1 for l in prior.splitlines() if l.startswith('- '))
print(f'  items: {pi} at {base}, {len(items)} now')
print('nothing found' if not found else f'{found} found')
