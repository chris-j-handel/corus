"""thirty_opening_build.py [--write]
T5 and T6, v390: Natural Intelligence's opening, its 47 sentences word for word, becomes Exhibit THIRTY's first four
groups, steps 1 to 47, each with an Adding line naming its one advance. THIRTY's own step 1, the same sentence,
is one step with opening step 1, its Adding line carried whole. THIRTY's steps 2 to 661 follow as steps 48 to 707,
and its groups 1 to 42 as groups 5 to 46: one sequence from one opening sentence, renumbered once.
Each reference to a THIRTY step or group is re-pointed: within THIRTY, at the living files, and at carry's
offerings, possiblings and carryings. Records stay as their record: Session_Record, Living_Improving_Value, archive/
and incoming/. Without --write it builds to the scratch path given by SCRATCH or prints counts only."""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NI = os.path.join(ROOT, 'Natural_Intelligence_v390.md')
TH = os.path.join(ROOT, 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v390.md')
SHIFT_STEP, SHIFT_GROUP, OLD_LAST = 46, 4, 661
IND = '\u2003' * 8

GROUPS = [
    ('Universe, the set of all now-existing things', [
        'the universe, the set of all now-existing things, inception, now-existing one naming; each step after it a step from it, and nothing brought to it',
        'observing; same-as, is or is not',
        'one universal set, by our observing',
        'no other universe',
        'same-existing; all prior observings',
        "a set's is or is not same-existing-as its prior-existing",
        'parity-changing',
        'next-existing, continuing',
        'an other',
        'each same-existing thing not any other',
        'sharing; sequential momentarying',
        'the universe, the same-existing set']),
    ('Observing, possibling and discovering, self and other', [
        'observing, now with prior',
        'possibling, next with now',
        'discovering, prior with next',
        'a self',
        'two priors possibling each other',
        'one and two',
        'a momentarying opening and completing',
        'within, one to two; self-possibling',
        'between, two to three; self-discovering, along',
        "across, a self's between an other's within"]),
    ('A living self, a living set', [
        'a self, a living-thing',
        'a living set; universal momentarying; a same-existing-universe',
        'a living self, a universal same-existing set',
        'a set of living selves',
        'a set of living selves, a living self',
        'a non-living-thing',
        'living-things and non-living-things']),
    ('A bi-coupling, a third living self, one method', [
        'a bi-coupling; co-sequentially',
        'offering',
        'a third living self',
        'stable-forming between',
        'entraining',
        "a third living self's intelligence, neither self's",
        'a same-existing-society',
        'same or not-same',
        'continuing or inverting',
        'parity, self-moral-value or other-moral-value; a 0, bothboth, betweening',
        'inverting',
        'alternating',
        'a self still-possibling',
        'staying still-possibling',
        'improving; next-existing same self',
        'consciousness',
        'one method',
        'no other method']),
]
OLD1_ADDING = GROUPS[0][1][0]


def opening():
    t = open(NI, encoding='utf-8').read()
    body = re.search(r'^## 1\.1 .*?\n\n(.*?)\n\n## 1\.2', t, re.S | re.M).group(1)
    paras = [[l.rstrip(' \\') for l in p.split('\n')] for p in body.split('\n\n')]
    return paras


def new_step(n):
    return n if n == 1 else n + SHIFT_STEP if 2 <= n <= OLD_LAST else None


NUMS = re.compile(r'\b([Ss]teps?) (\d+(?:(?:, and |, | and | to | or |–)\d+)*)')
SKIP = ('steps 1 to 3 to 5 to 7',)


def remap_nums(m):
    if m.group(0) in SKIP:
        return m.group(0)
    def one(x):
        v = new_step(int(x.group(0)))
        assert v is not None, m.group(0)
        return str(v)
    return m.group(1) + ' ' + re.sub(r'\d+', one, m.group(2))


def remap_thirty_body(t):
    return NUMS.sub(remap_nums, t)


MENTION = re.compile(r"(?:THIRTY|Co-Chaining Logic Registry|Co-Chaining)(?:'s)?")
EXT_GROUP = re.compile(r'(Co-Chaining Logic Registry|from) (\d+), (steps? )')
PROTECT = ('with step 4 of the deriving',)
SKIP_EXT = ("Exhibit THIRTY's steps 1 to 50 meet session v390's learnings",)


def remap_external(t):
    """Each sentence naming THIRTY has each of its step numbers re-pointed, from its naming to its end; a version
    named between them (v385R, say) marks an earlier registry's numbering, and that sentence stays."""
    out, last = [], 0
    for m in MENTION.finditer(t):
        if m.start() < last:
            continue
        end = len(t)
        e = re.compile(r'\.(?=\s+[A-Z*])|\n').search(t, m.end())
        if e:
            end = e.start()
        span = t[m.start():end]
        if re.search(r'\bv\d', span) or any(span.startswith(x) or x in t[max(0, m.start() - 20):end] for x in SKIP_EXT):
            continue
        out.append(t[last:m.start()])
        for k, x in enumerate(PROTECT):
            span = span.replace(x, '\x00%d\x00' % k)
        span = re.sub(r'(at step \d+ and section )(\d+)', lambda g: g.group(1) + str(int(g.group(2)) + SHIFT_GROUP), span)
        span = EXT_GROUP.sub(lambda g: '%s %d, %s' % (g.group(1), int(g.group(2)) + SHIFT_GROUP, g.group(3)),
                                 NUMS.sub(remap_nums, span))
        for k, x in enumerate(PROTECT):
            span = span.replace('\x00%d\x00' % k, x)
        out.append(span)
        last = end
    out.append(t[last:])
    return ''.join(out)


def build():
    paras = opening()
    assert [len(p) for p in paras] == [len(g[1]) for g in GROUPS], [len(p) for p in paras]
    t = open(TH, encoding='utf-8').read()
    head, rest = t.split('\n## 1 ', 1)
    rest = '## 1 ' + rest
    # contents lines
    def contents(m):
        return '- %d %s' % (int(m.group(1)) + SHIFT_GROUP, m.group(2))
    head = re.sub(r'^- (\d+) (.*)$', contents, head, flags=re.M)
    first = head.index('\n- %d ' % (1 + SHIFT_GROUP))
    head = head[:first] + ''.join('\n- %d %s' % (k + 1, g[0]) for k, g in enumerate(GROUPS)) + head[first:]
    # group headings
    rest = re.sub(r'^## (\d+) ', lambda m: '## %d ' % (int(m.group(1)) + SHIFT_GROUP), rest, flags=re.M)
    # THIRTY's own step 1, one with opening step 1
    m = re.search(r'\n1\. The universe is the set of all now-existing things\.\n\n +\*Adding: ' + re.escape(OLD1_ADDING) + r'\.\*\n', rest)
    assert m, 'step 1'
    rest = rest[:m.start()] + rest[m.end():]
    ent = re.search(r'\*Entering: (.*?)\.\*', rest)
    items = ent.group(1).split('; ')
    for x in OLD1_ADDING.split('; '):
        items.remove(x)
    rest = rest[:ent.start()] + '*Entering: ' + '; '.join(items) + '.*' + rest[ent.end():]
    # step numbers and references
    rest = re.sub(r'^(\d+)\. ', lambda m: '%d. ' % new_step(int(m.group(1))), rest, flags=re.M)
    rest = remap_thirty_body(rest)
    head = remap_thirty_body(head)
    # four groups from the opening
    out, n = [], 0
    for k, ((title, adds), para) in enumerate(zip(GROUPS, paras)):
        ent = '; '.join(adds)
        out.append(('## %d %s\n\n' + IND + '*Entering: %s.*\n') % (k + 1, title, ent))
        for s, a in zip(para, adds):
            n += 1
            out.append(('%d. %s\n\n' + IND + '*Adding: %s.*\n') % (n, s, a))
    return head + '\n' + '\n'.join(out) + '\n' + rest


def check(t):
    ok = True
    paras = opening()
    sent = [s for p in paras for s in p]
    steps = re.findall(r'^(\d+)\. (.*)$', t, re.M)
    nums = [int(a) for a, _ in steps]
    ok &= nums == list(range(1, len(nums) + 1))
    ok &= [b for _, b in steps[:47]] == sent
    print('steps', len(nums), 'contiguous and opening word for word:', ok)
    return ok


if __name__ == '__main__':
    t = build()
    assert check(t)
    if '--write' in sys.argv:
        open(TH, 'w', encoding='utf-8').write(t)
        files = [f for f in glob.glob(os.path.join(ROOT, '*_v390.md')) if f != TH]
        files += [f for f in glob.glob(os.path.join(ROOT, 'carry', '*.md'))
                  if re.search(r'(Offerings|Possibling|Carryings)', os.path.basename(f))]
        for f in files:
            s = open(f, encoding='utf-8').read()
            u = remap_external(s)
            if u != s:
                open(f, 'w', encoding='utf-8').write(u)
                print('re-pointed', os.path.relpath(f, ROOT))
    elif os.environ.get('SCRATCH'):
        open(os.environ['SCRATCH'], 'w', encoding='utf-8').write(t)
