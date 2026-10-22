"""ni_thirty_check.py: is each bold concept of Natural Intelligence's body held by a Co-Chaining Logic Registry step?

A bold concept is held when one step, its text with its Adding line, carries at least 80 percent of the
concept's content words (four letters or more, a short list of joining words set aside). The Exhibit ONE
copy inside Natural Intelligence is not read; Exhibit ONE's own concepts are read from its standalone file
only when --one is given.

Usage: python3 ni_thirty_check.py [NI.md] [THIRTY.md] [--list] [--one ONE.md]
Exit 0 when all are held; 1 otherwise. --list prints each unheld concept with its section.
"""
import re, sys

STOP = {'with', 'from', 'that', 'this', 'each', 'its', 'their', 'them', 'they', 'into', 'than', 'then',
        'what', 'when', 'where', 'which', 'while', 'only', 'also', 'both', 'none', 'more', 'other', 'others',
        'every', 'there', 'here', 'have', 'has', 'is', 'are', 'and', 'not', 'one', 'two', 'its own', 'own'}


def words(s):
    return {w for w in re.findall(r'[\w−+φ-]{4,}', s.lower()) if w not in STOP}


def steps_of(th):
    out = []
    for m in re.finditer(r'^(\d+)\. (.*?)\n\n\s*\*Adding: (.*?)\*', th, re.M | re.S):
        out.append((int(m.group(1)), words(m.group(2) + ' ' + m.group(3))))
    return out


def concepts(ni):
    body = ni[ni.index('\n## 1.1 '):]
    if '# EXHIBIT ONE' in body:
        a = body.index('# EXHIBIT ONE')
        b = body.index('\n## 4.1 ')
        body = body[:a] + body[b:]
    sec = None
    for line in body.split('\n'):
        h = re.match(r'## (\d\.\d+) ', line)
        if h:
            sec = h.group(1)
            continue
        for c in re.findall(r'(?:^|(?<=\s))\*\*([^*\n]{20,}?)\*\*', line):
            yield sec, c.strip(' :;,.')


def held(c, steps):
    w = words(c)
    if not w:
        return 0
    best = 0
    for n, s in steps:
        r = len(w & s) / len(w)
        if r > best:
            best, at = r, n
    return at if best >= 0.8 else 0


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    ni_f = args[0] if args else 'Natural_Intelligence_v391.md'
    th_f = args[1] if len(args) > 1 else 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v391.md'
    ni, th = open(ni_f).read(), open(th_f).read()
    steps = steps_of(th)
    rows = list(concepts(ni))
    if '--one' in argv:
        one = open(argv[argv.index('--one') + 1]).read()
        for line in one.split('\n'):
            for c in re.findall(r'(?:^|(?<=\s))\*\*([^*\n]{20,}?)\*\*', line):
                rows.append(('ONE', c.strip(' :;,.')))
    un = [(s, c) for s, c in rows if not held(c, steps)]
    print('bold concepts', len(rows), 'held by a step', len(rows) - len(un), 'unheld', len(un))
    if '--list' in argv:
        for s, c in un:
            print(' ', s, '|', c)
    return 1 if un else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
