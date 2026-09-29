"""Reader checks: the mechanical findings the fresh readers made again and again at v376, said at each motion.
A check is a coupling partner and no authority: it says its result and decides nothing.
A check saying nothing is no agreement unless it says what it read: each check below says what it read.

Usage: python3 reader_checks.py [root] [base]
  root  the repository root (default .), with the branch under review checked out at it
  base  the ref the motion is read against (default origin/main); the words compared are those
        added since the branch's merge-base with it, word by word, working-tree changes included
        (a new file is read once it is added with git add or git add -N)

Says:
  1. Exhibit THIRTY: steps numbered 1 to N with no gap; each group with an Entering line and
     Adding lines, and its Entering line the group's Adding lines joined in order.
  2. The Living File Registry's number of steps and of groups for Exhibit THIRTY against its own.
  3. Released words among the words this motion adds, from released_words.txt beside this file,
     outside italics and code; bold is read.
  4. Retired sayings still at the living files, from retired_sayings.txt beside this file, a sentence
     saying the retiring itself (dissolved, released, re-said, retired) passed over.
  5. Each step number the carrying names, with the step's opening words, to be read by eye.
Kinds 1 and 5 of the reviewer's brief, a concept before its entering step and meaning drift,
and section numbers, are a reader's.
"""
import os, re, subprocess, sys, glob

root = sys.argv[1] if len(sys.argv) > 1 else '.'
base = sys.argv[2] if len(sys.argv) > 2 else 'origin/main'
here = os.path.dirname(os.path.abspath(__file__))

def version(path):
    m = re.search(r'_v(\d+)([a-z]?)\.md$', path)
    return (int(m.group(1)), m.group(2)) if m else (0, '')

def newest(pattern):
    fs = glob.glob(os.path.join(root, pattern))
    return max(fs, key=version) if fs else None

def words_file(name):
    p = os.path.join(here, name)
    if not os.path.exists(p):
        return []
    return [l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]

ITALIC = re.compile(r'(?<!\*)\*(?!\*)[^*\n]+?(?<!\*)\*(?!\*)')
def unquoted(text):
    text = ITALIC.sub('', text)
    return re.sub(r'`[^`]*`', '', text)

said = 0
def say(line):
    global said
    said += 1
    print('  ' + line)

# 1. Exhibit THIRTY's steps and groups
thirty = newest('Exhibit_THIRTY_Co-Chaining_Logic_Registry_v*.md')
steps = groups = 0
print('1. Exhibit THIRTY:', os.path.basename(thirty) if thirty else 'not found')
if thirty:
    t = open(thirty, encoding='utf-8').read()
    nums = [int(n) for n in re.findall(r'^(\d+)\. ', t, re.M)]
    steps = len(nums)
    if nums != list(range(1, steps + 1)):
        gaps = [i + 1 for i, n in enumerate(nums) if n != i + 1][:5]
        say(f'steps not 1 to {steps} in order, first departures at positions {gaps}')
    parts = re.split(r'(^## \d+ .*$)', t, flags=re.M)
    groups = (len(parts) - 1) // 2
    for k in range(1, len(parts), 2):
        h, b = parts[k].strip(), parts[k + 1]
        adds_list = re.findall(r'\*Adding: (.*?)\*', b)
        m = re.search(r'\*Entering: (.*?)\*', b)
        if not m:
            say(f'{h}: no Entering line')
        elif not adds_list:
            say(f'{h}: no Adding lines')
        elif m.group(1) != '; '.join(a.rstrip('.') for a in adds_list) + '.':
            say(f'{h}: Entering is not its Adding lines joined')
    print(f'   read {steps} steps in {groups} groups')

# 2. The registry's numbers
reg = newest('Exhibit_TWENTY-SIX_Living_File_Registry_v*.md')
ones = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
tens = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
def words_to_n(s):
    total = cur = 0
    for w in re.split(r'[\s-]+', s.strip()):
        if w in ones: cur += ones.index(w)
        elif w in tens: cur += tens[w]
        elif w == 'hundred': cur *= 100
        elif w == 'thousand': total += cur * 1000; cur = 0
        elif w.isdigit(): cur += int(w)
    return total + cur
print("2. The registry's numbers for Exhibit THIRTY")
if reg and thirty:
    m = re.search(r'((?:[a-z]+[ -])*[a-z0-9]+) steps in ([a-z0-9-]+) groups', open(reg, encoding='utf-8').read())
    if not m:
        say("the registry's number of steps not found")
    else:
        n_steps, n_groups = words_to_n(m.group(1)), words_to_n(m.group(2))
        print(f'   read "{m.group(0).strip()}"')
        if n_steps != steps: say(f'the registry says {n_steps} steps; Exhibit THIRTY has {steps}')
        if n_groups != groups: say(f'the registry says {n_groups} groups; Exhibit THIRTY has {groups}')

# 3. Released words among the words added
def git(*args):
    return subprocess.run(['git', '-C', root] + list(args), capture_output=True, text=True).stdout
mb = git('merge-base', base, 'HEAD').strip() or base
print(f'3. Released words among the words added since {mb[:10]}, the merge-base with {base}')
released = words_file('released_words.txt')
diff = git('diff', '--word-diff=porcelain', '-U0', mb, '--', '*.md')
cur = None; ln = 0; words_read = 0
for line in diff.split('\n'):
    if line.startswith('+++ '):
        cur = line[6:]; continue
    if line.startswith(('--- ', 'diff ', 'index ', 'new file', 'deleted file')):
        continue
    m = re.match(r'@@ -\S+ \+(\d+)', line)
    if m:
        ln = int(m.group(1)); continue
    if line == '~':
        ln += 1; continue
    if line.startswith('+') and cur and not cur.endswith('Session_Record.md'):   # the record names released words as released
        text = unquoted(line[1:]); words_read += len(text.split())
        for w in released:
            if re.search(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', text, re.I):
                say(f'{cur}:{ln}: "{w}" in "{line[1:81].strip()}"')
print(f'   read {words_read} added words')

# 4. Retired sayings still at the living files
print('4. Retired sayings at the living files')
retired = words_file('retired_sayings.txt')
living = [f for f in glob.glob(os.path.join(root, '*.md')) if os.path.basename(f) != 'README.md']
RETIRING = re.compile(r'dissolv|releas|re-said|retir', re.I)
for s in retired:
    pat = re.compile(r'(?<![\w-])' + re.escape(s) + r'(?![\w-])')
    hits = []
    for f in living:
        c = 0
        for sentence in re.split(r'(?<=[.;:|])\s+', open(f, encoding='utf-8').read()):
            if pat.search(sentence) and not RETIRING.search(sentence):
                c += len(pat.findall(sentence))
        if c: hits.append(f'{os.path.basename(f)} {c}')
    if hits:
        say(f'"{s}": ' + '; '.join(hits))
print(f'   read {len(retired)} sayings at {len(living)} files')

# 5. Step numbers the carrying names
print("5. Step numbers the carrying names, with each step's opening words")
carry = os.path.join(root, 'carry', 'Living_Improving_Value.md')
if thirty and os.path.exists(carry):
    t = open(thirty, encoding='utf-8').read()
    first = {int(n): s[:60] for n, s in re.findall(r'^(\d+)\. (.*)$', t, re.M)}
    named = set()
    for lst in re.findall(r"Exhibit THIRTY's steps? (\d+(?:(?:, | and | to )\d+)*)", open(carry, encoding='utf-8').read()):
        named.update(int(x) for x in re.findall(r'\d+', lst))
    for n in sorted(named):
        print(f'   {n}: {first.get(n, "no such step")}')

print('nothing to say' if said == 0 else f'{said} said, each for a reader to meet')
