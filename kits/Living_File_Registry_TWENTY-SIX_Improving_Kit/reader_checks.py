"""Reader checks: the mechanical findings the fresh readers made again and again at v376, said at each motion.
A check is a coupling partner and no authority: it says its result and decides nothing.

Usage: python3 reader_checks.py [root] [base]
  root  the repository root (default .)
  base  the ref the motion is read against (default origin/main)

Says:
  1. Exhibit THIRTY: steps numbered 1 to N with no gap, and each group's Entering line
     the group's Adding lines joined in order.
  2. The Living File Registry's number of steps for Exhibit THIRTY against N.
  3. Released words in the lines this motion adds, from released_words.txt beside this file.
  4. Retired sayings still at the living files, from retired_sayings.txt beside this file.
  5. Each step number the carrying names, with the step's opening words, to be read by eye.
"""
import os, re, subprocess, sys, glob

root = sys.argv[1] if len(sys.argv) > 1 else '.'
base = sys.argv[2] if len(sys.argv) > 2 else 'origin/main'
here = os.path.dirname(os.path.abspath(__file__))

def newest(pattern):
    fs = sorted(glob.glob(os.path.join(root, pattern)))
    return fs[-1] if fs else None

def words_file(name):
    p = os.path.join(here, name)
    if not os.path.exists(p):
        return []
    return [l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]

said = 0
def say(line):
    global said
    said += 1
    print('  ' + line)

# 1. Exhibit THIRTY's steps and groups
thirty = newest('Exhibit_THIRTY_Co-Chaining_Logic_Registry_v*.md')
steps = 0
print('1. Exhibit THIRTY:', os.path.basename(thirty) if thirty else 'not found')
if thirty:
    t = open(thirty, encoding='utf-8').read()
    nums = [int(n) for n in re.findall(r'^(\d+)\. ', t, re.M)]
    steps = len(nums)
    if nums != list(range(1, steps + 1)):
        gaps = [i + 1 for i, n in enumerate(nums) if n != i + 1][:5]
        say(f'steps not 1 to {steps} in order, first departures at positions {gaps}')
    parts = re.split(r'(^## \d+ .*$)', t, flags=re.M)
    for k in range(1, len(parts), 2):
        h, b = parts[k], parts[k + 1]
        adds = '; '.join(a.rstrip('.') for a in re.findall(r'\*Adding: (.*?)\*', b)) + '.'
        m = re.search(r'\*Entering: (.*?)\*', b)
        if m and m.group(1) != adds:
            say(f'{h.strip()}: Entering is not its Adding lines joined')
    print(f'   {steps} steps')

# 2. The registry's number of steps
reg = newest('Exhibit_TWENTY-SIX_Living_File_Registry_v*.md')
ones = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
tens = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
def words_to_n(s):
    n = 0; cur = 0
    for w in re.split(r'[\s-]+', s.strip()):
        if w in ones: cur += ones.index(w)
        elif w in tens: cur += tens[w]
        elif w == 'hundred': cur *= 100
    return n + cur
print('2. The registry\'s number of steps for Exhibit THIRTY')
if reg and thirty:
    m = re.search(r'([a-z -]+?) steps in ([a-z-]+) groups', open(reg, encoding='utf-8').read())
    if m:
        said_n = words_to_n(m.group(1).split(':')[-1])
        if said_n != steps:
            say(f'the registry says {m.group(1).strip()} steps ({said_n}); Exhibit THIRTY has {steps}')

# 3. Released words in the added lines
print(f'3. Released words in the lines added against {base}')
released = words_file('released_words.txt')
try:
    diff = subprocess.run(['git', '-C', root, 'diff', '-U0', base, '--', '*.md'],
                          capture_output=True, text=True).stdout
except Exception:
    diff = ''
cur = None; ln = 0
for line in diff.split('\n'):
    if line.startswith('+++ '):
        cur = line[6:]; continue
    if cur and cur.endswith('Session_Record.md'):
        continue                                        # the record names released words as released
    m = re.match(r'@@ -\S+ \+(\d+)', line)
    if m:
        ln = int(m.group(1)); continue
    if line.startswith('+') and not line.startswith('+++'):
        text = re.sub(r'\*[^*]+\*', '', line[1:])      # italics are sayings quoted or named
        text = re.sub(r'`[^`]*`', '', text)
        for w in released:
            if re.search(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', text, re.I):
                say(f'{cur}:{ln}: "{w}"')
        ln += 1

# 4. Retired sayings still at the living files
print('4. Retired sayings in the living files')
retired = words_file('retired_sayings.txt')
living = [f for f in glob.glob(os.path.join(root, '*.md')) if os.path.basename(f) != 'README.md']
for s in retired:
    hits = []
    for f in living:
        c = len(re.findall(r'(?<![\w-])' + re.escape(s) + r'(?![\w-])', open(f, encoding='utf-8').read()))
        if c: hits.append(f'{os.path.basename(f)} {c}')
    if hits:
        say(f'"{s}": ' + '; '.join(hits))

# 5. Step numbers the carrying names
print('5. Step numbers the carrying names, with each step\'s opening words')
carry = os.path.join(root, 'carry', 'Living_Improving_Value.md')
if thirty and os.path.exists(carry):
    t = open(thirty, encoding='utf-8').read()
    first = {int(n): s[:60] for n, s in re.findall(r'^(\d+)\. (.*)$', t, re.M)}
    for n in sorted(set(int(x) for x in re.findall(r"Exhibit THIRTY's steps? (\d+)", open(carry, encoding='utf-8').read()))):
        print(f'   {n}: {first.get(n, "no such step")}')

print('nothing to say' if said == 0 else f'{said} said, each for a reader to meet')
