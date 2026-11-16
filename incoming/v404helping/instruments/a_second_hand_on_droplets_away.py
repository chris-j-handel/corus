"""A second hand on a slice having droplets away from gathering files: an other reading than the reading of
`incoming/v403cohering/instruments/each_droplet_said_more_than_once.py`. It reads each gathering file a slice
changes, as it was with the commit before and as it is with the slice's commit, and writes nothing.

Use: python3 -I incoming/v404helping/instruments/a_second_hand_on_droplets_away.py <root> <the commit before> <the slice's commit>

Its readings, each all or none at all, by each line:
  1. Each line away and each line new, by the two files' lines in order; each heading the same and in order.
  2. A line away with a new line of the same opening words is a droplet re-said, and no droplet away.
  3. With each droplet away: its heading; its label in italics, with one; each of its sentences after its kind's
     label and its label in italics, a sentence to its stop; and each longer droplet of the file as it is having
     each of those sentences with each letter and each mark the same, said with its line and its heading.
  4. With a droplet away having a label in italics: each line of the file as it is having that label, and each
     line having the words *sentence* and the label's number.
  5. With a droplet away under a heading with a number, a section of its living file: each longer droplet having
     its value, with or with no saying of that heading's number or of its words.

Returned at main, 16 November 2026, with the commit before a6d4e2f and the slice's commit ed2354c, the slice
*The managing session's rule for a droplet whole within a longer one, entered and executed: eight droplets away,
each value once*:
  Natural Intelligence's gathering file: fifty-three headings, the same and in order; eight lines away and one
  new; one droplet re-said, the droplet of the rule; seven droplets away, each sentence of each in a longer
  droplet with each letter the same. Two with a label, *The current understanding, 6x-v.* and *The current
  understanding, 7.*: each under *Opening*, each in two longer droplets, one under *Opening* and one under
  *Droplets*; each label in no line now; *sentence 6x-v* in four lines and *sentence 7* in one. Four under
  *6.5 Living and non-living things within one universe*, each in one longer droplet under *Droplets*, and no
  one of the four longer saying 6.5 or that heading's words. One under *Droplets*, in one longer under *Droplets*.
  Exhibit EIGHTEEN Natural Physics's gathering file: forty-eight headings, the same and in order; one line away
  and no line new; one droplet away, its one sentence in one longer droplet under *Droplets*, after it in its
  file's order.
"""
import difflib, re, subprocess, sys

ROOT, BEFORE, AFTER = sys.argv[1], sys.argv[2], sys.argv[3]


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True)
    assert r.returncode == 0, 'a git command failed, and this reading has nothing: ' + ' '.join(a)
    return r.stdout


def heading_of_each(lines):
    cur, out = 'no heading', []
    for l in lines:
        m = re.match(r'^#{2,3} (.*)$', l)
        if m:
            cur = m.group(1).strip()
        out.append(cur)
    return out


KIND = re.compile(r'^- \*\*[^*]+\*\* · ')
LABEL = re.compile(r'^\*([^*]+)\*\s+')


def parts(line):
    """a droplet's label in italics, with one, and its words after it"""
    t = KIND.sub('', line, count=1) if KIND.match(line) else line[2:]
    m = LABEL.match(t)
    return (m.group(1), t[m.end():]) if m else ('', t)


def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.?!])\s+', t) if s.strip()]


files = [f for f in git('diff', '--name-only', BEFORE, AFTER, '--', 'gathering-value').split('\n') if f.endswith('.md')]
print(f'{len(files)} gathering files changed with the slice')
for f in files:
    b = git('show', f'{BEFORE}:{f}').split('\n')
    a = git('show', f'{AFTER}:{f}').split('\n')
    hb, ha = heading_of_each(b), heading_of_each(a)
    heads_b = [l for l in b if re.match(r'^#{1,6} ', l)]
    heads_a = [l for l in a if re.match(r'^#{1,6} ', l)]
    away, new = [], []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=b, b=a, autojunk=False).get_opcodes():
        if tag != 'equal':
            away += list(range(i1, i2))
            new += list(range(j1, j2))
    print()
    print(f)
    print(f'  headings: {len(heads_b)} before, {len(heads_a)} after, the same and in order: {heads_b == heads_a}')
    print(f'  lines away: {len(away)}; lines new: {len(new)}')
    resaid = {i for i in away if any(a[j][:120] == b[i][:120] for j in new)}
    for i in sorted(resaid):
        print(f'  re-said, and no droplet away: {b[i][:110]}')
    for i in [i for i in away if i not in resaid]:
        line = b[i]
        label, t = parts(line)
        ss = sentences(t)
        print(f'  away, under *{hb[i]}*: {line[:130]}')
        longer = [j for j, l in enumerate(a) if l.startswith('- ') and len(l) > len(line) and all(s in l for s in ss)]
        print(f'      its sentences: {len(ss)}; longer droplets now having each with each letter the same: {len(longer)}')
        for j in longer:
            says = ''
            m = re.match(r'^(\d+\.\d+) (.*)$', hb[i])
            if m:
                number = re.search(r'(?<![0-9.])' + re.escape(m.group(1)) + r'(?![0-9])', a[j]) is not None
                says = f'; says {m.group(1)}: {number}; says that heading\'s words: {m.group(2) in a[j]}'
            print(f'        line {j + 1}, under *{ha[j]}*{says}: {a[j][:100]}')
        if label:
            whole = '*' + label + '*'
            number = label.rstrip('.').split(', ')[-1]
            with_label = [j + 1 for j, l in enumerate(a) if whole in l]
            naming = [j + 1 for j, l in enumerate(a) if re.search(r'\bsentence ' + re.escape(number) + r'(?![0-9a-z-])', l, re.I)]
            print(f'      its label {whole}: in {len(with_label)} lines now; *sentence {number}* in {len(naming)} lines now: {naming}')
        assert longer, 'a sentence of a droplet away is in no longer droplet of its file'
