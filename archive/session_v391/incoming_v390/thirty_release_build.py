"""thirty_release_build.py [--write]
Agreed bothboth, v390: Exhibit THIRTY's steps that Natural Intelligence's opening, now its steps 1 to 47, says better
are released whole to archive: 48, a second inception; 52, three sequential universes beside one; 62, four binaries
as an opening's terms; 67 to 71, a possibling thing and three places; 75, a place-moment. Their Adding items leave
their groups' Entering lines. The steps after them are renumbered once; each reference is re-pointed, within THIRTY
and at each sentence naming THIRTY at the living files and at carry's offerings, possiblings and carryings.
Three steps resting on a released step are re-said: 372 and 591 rest on possibling, step 14; 622's three places
are observing, possibling and discovering, steps 13 to 15. Group 5 is titled by its own Adding items, and group 7,
its three places released, is titled by what stays. Without --write it builds to SCRATCH and checks."""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TH = os.path.join(ROOT, 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v390.md')
ARCH = os.path.join(ROOT, 'archive', 'session_v390', 'prior_to_thirty_release')
REL = [48, 52, 62, 67, 68, 69, 70, 71, 75]
IND = ' ' * 8
TITLES = {('5', 'The universe, the set of all now-existing things'): 'Four binaries, one now, parity-changing and discovering',
          ('7', 'Three places and a between'): 'One relation, a between and entraining'}
RESAY = [
    ('A term posted to close an account is a possibling thing with prior, step 67, and its closing',
     'A term posted to close an account is possibling, step 14, and its closing'),
    ('A destiny is next living possibling as words ahead of its coupling, a possibling thing, step 67, arriving',
     'A destiny is next living possibling as words ahead of its coupling, step 14, arriving'),
    ('Value reaching living expedition passes three places, step 71: arriving, a possibling thing with prior, whole as it arrived;',
     'Value reaching living expedition is observing, possibling and discovering, steps 13 to 15: arriving, observed whole as it arrived;'),
]
# numbers after a step reference that are no step, kept as they are
PROTECT = ['step 246, and 25, centre of face', 'step 563, 3-7-2-6', 'step 566, 3-11-6-14', 'step 121, and 17 next now',
           'step 298, and 1 is self', 'steps 1 to 3 to 5 to 7']


def new(n):
    assert n not in REL, n
    return n - sum(1 for r in REL if r < n)


NUMS = re.compile(r'\b([Ss]teps?) (\d+(?:(?:, and |, | and | to | or |–)\d+)*)')


def protect_renumbered():
    # PROTECT phrases name steps too; their step numbers renumber, their other numbers stay
    out = []
    for x in PROTECT:
        m = re.match(r'(steps? )(\d+)(.*)', x)
        if x.startswith('steps 1 to 3'):
            out.append(x)
        else:
            out.append(m.group(1) + str(new(int(m.group(2)))) + m.group(3))
    return out


def build():
    t = open(TH, encoding='utf-8').read()
    for o, n in RESAY:
        assert t.count(o) == 1, o
        t = t.replace(o, n)
    released = []
    for r in REL:
        m = re.search(r'\n%d\. [^\n]*\n\n%s\*Adding: (.*?)\.\*\n' % (r, IND), t)
        assert m, r
        released.append(m.group(0).strip('\n'))
        items = m.group(1).split('; ')
        # its group's Entering line
        ent = list(re.finditer(r'\*Entering: (.*?)\.\*', t[:m.start()]))[-1]
        e = ent.group(1).split('; ')
        for x in items:
            e.remove(x)
        t = t[:ent.start()] + '*Entering: ' + '; '.join(e) + '.*' + t[ent.end():m.start()] + t[m.end():]
    for (g, old), newt in TITLES.items():
        assert t.count('## %s %s\n' % (g, old)) == 1 and t.count('- %s %s\n' % (g, old)) == 1, old
        t = t.replace('## %s %s\n' % (g, old), '## %s %s\n' % (g, newt)).replace('- %s %s\n' % (g, old), '- %s %s\n' % (g, newt))
    t = re.sub(r'^(\d+)\. ', lambda m: '%d. ' % new(int(m.group(1))), t, flags=re.M)
    prot_new = protect_renumbered()
    for k, x in enumerate(PROTECT):
        t = t.replace(x, '\x00%d\x00' % k)
    t = NUMS.sub(lambda m: m.group(1) + ' ' + re.sub(r'\d+', lambda d: str(new(int(d.group(0)))), m.group(2)), t)
    for k, x in enumerate(prot_new):
        t = t.replace('\x00%d\x00' % k, x)
    return t, released


MENTION = re.compile(r"(?:THIRTY|Co-Chaining Logic Registry|Co-Chaining)(?:'s)?")


def remap_external(t):
    """Each sentence naming THIRTY has its step numbers re-pointed; a released step is said by its name and the
    archive. A sentence naming a version (v385R, say) keeps an earlier registry's numbering."""
    names = {48: 'a second inception', 52: 'three sequential universes', 62: "four binaries, an opening's terms",
             67: 'a possibling thing', 68: 'a now-existing thing arriving', 69: "living's momentarying",
             70: "non-living's momentarying", 71: 'three places', 75: 'a place-moment'}
    out, last = [], 0
    for m in MENTION.finditer(t):
        if m.start() < last:
            continue
        e = re.compile(r'\.(?=\s+[A-Z*])|\n').search(t, m.end())
        end = e.start() if e else len(t)
        span = t[m.start():end]
        if re.search(r'\bv\d', span):
            continue

        def f(mm):
            toks = re.findall(r'\d+|, and |, | and | to | or |–', mm.group(2))
            nums, i = [], 0
            while i < len(toks):
                if i + 2 < len(toks) and toks[i + 1] in (' to ', '–'):
                    nums += list(range(int(toks[i]), int(toks[i + 2]) + 1)); i += 3
                elif toks[i].isdigit():
                    nums.append(int(toks[i])); i += 1
                else:
                    i += 1
            if not any(n in REL for n in nums):
                return mm.group(1) + ' ' + re.sub(r'\d+', lambda d: str(new(int(d.group(0)))), mm.group(2))
            kept = [new(n) for n in nums if n not in REL]
            gone = ['*%s*' % names[n] for n in nums if n in REL]
            s = ''
            if kept:
                s = ('step %d' % kept[0]) if len(kept) == 1 else 'steps ' + ', '.join(map(str, kept[:-1])) + ' and %d' % kept[-1]
                s += ', and '
            return s + 'released ' + ('step ' if len(gone) == 1 else 'steps ') + ', '.join(gone) + ', archived at v390'
        out.append(t[last:m.start()])
        out.append(NUMS.sub(f, span))
        last = end
    out.append(t[last:])
    return ''.join(out)


def check(t):
    steps = [int(a) for a in re.findall(r'^(\d+)\. ', t, re.M)]
    ok = steps == list(range(1, len(steps) + 1)) and len(steps) == 707 - len(REL)
    print('steps', len(steps), 'one sequence:', ok)
    return ok


if __name__ == '__main__':
    t, released = build()
    assert check(t)
    if '--write' in sys.argv:
        os.makedirs(ARCH, exist_ok=True)
        open(os.path.join(ARCH, os.path.basename(TH)), 'w', encoding='utf-8').write(open(TH, encoding='utf-8').read())
        open(os.path.join(ARCH, 'Exhibit_THIRTY_released_steps_v390.md'), 'w', encoding='utf-8').write(
            '# Exhibit THIRTY, steps released at v390\n\nAgreed bothboth: Natural Intelligence\'s opening, THIRTY\'s steps 1 to 47, says each better. Numbered as they stood after the opening motion.\n\n'
            + '\n\n'.join(released) + '\n')
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
