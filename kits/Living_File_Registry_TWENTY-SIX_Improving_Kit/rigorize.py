"""The binary rigorizer's instrument: it sizes and seats, and decides nothing.

Two faces, each the either/or resolving's first steps at the code's names:

  sayings <naming> [root]   2 and 14: gathers each bold saying of one naming across the living files, whole, with its
                            file and its section, so two sayings arriving at one sharing are met side by side; agreeing
                            they are one, parting they are the concern, either this or that and not both.
  beside <file> [more ...]  the six binaries: seats each sentence of a file, living or incoming, at the six things beside
                            all things its words may carry, and at the released words. A seat is a place to meet, and a
                            sentence seated may carry none: each is met by the working at the resolving, one at a time.

The six things beside all things: a size, a ground, floor or scale a partway is measured against; a fixed form, a form
named still; a total across the changing, a container; a common beat, a clock over the changing; a keeping, a store
beside it; and a doer applying from outside. A sentence carrying none is the method's at its subject; a sentence
carrying one is re-said at parity changing, a field's own result kept exact at its own subject.

Usage: python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/rigorize.py sayings carrying
       python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/rigorize.py beside incoming/some_field.md"""
import glob, os, re, sys

SIX = {
    'size': r'magnitude|amount|degree|level|larger|smaller|greater|lesser|grows?|growing|rises?|rising|band|range|width|threshold|gradient|partway|more than|less than|increase|decrease',
    'fixed form': r'fixed|static|constant|equilibri\w*|steady state|stable state|settled|at rest|stationary|invariant',
    'total': r'total|sums?|summing|summed|conserv\w*|budget|ledger|accumulat\w*|compound\w*|cumulative|reservoir|container',
    'common beat': r'clock|schedul\w*|synchroni[sz]\w*|tick|global time|simultaneous|lockstep',
    'keeping': r'stor(?:e|ed|es|age|ing)|memor(?:y|ies)|record(?:s|ed)?|retain\w*|keeps?|kept|archiv\w*|cache|encod\w*|representation',
    'doer': r'select\w*|decides?|decided|controls?|controlled|govern\w*|regulat\w*|drives?|driven|causes?|caused|chooses?|chose|sorts?|prefer\w*|operator|agent|mechanism|signal\w*|message\w*|communicat\w*',
}
RELEASED = r'cost|costs|free|run|runs|running|runner|take|takes|taken|taking|taker|source|hold|holds|return|returns|every|stand|stands|surplus|uni-exchanging|bi-co-orthogonalizing|geodesic-method'


def living_files(root):
    names = {}
    for f in glob.glob(os.path.join(root, '*.md')):
        m = re.match(r'(.+)_v(\d+)[A-Za-z]?\.md$', os.path.basename(f))
        if m and (m.group(1) not in names or int(m.group(2)) > names[m.group(1)][0]):
            names[m.group(1)] = (int(m.group(2)), f)
    return sorted(f for _, f in names.values())


def sentences(path):
    section = ''
    in_code = False
    for line in open(path, encoding='utf-8'):
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code or line.startswith('|'):
            continue
        if line.startswith('#'):
            section = line.strip('# \n')
            continue
        for s in re.split(r'(?<=[.!?])\s+(?=[*A-Z])', line.strip()):
            if len(s) > 3:
                yield section, s


def sayings(naming, root):
    pat = re.compile(r'\*\*[^*]*\b' + re.escape(naming) + r'\b[^*]*\*\*', re.I)
    n = 0
    for f in living_files(root):
        for section, s in sentences(f):
            if pat.search(s):
                n += 1
                print('%s · %s\n  %s\n' % (os.path.basename(f), section, s))
    print('%d bold sayings of *%s* across the living files: met side by side, agreeing one, parting the concern' % (n, naming))


def beside(paths):
    six = {k: re.compile(r'\b(?:' + v + r')\b', re.I) for k, v in SIX.items()}
    released = re.compile(r'\b(?:' + RELEASED + r')\b', re.I)
    for path in paths:
        seats = 0
        for section, s in sentences(path):
            hits = [k for k, p in six.items() if p.search(s)]
            words = sorted(set(w.lower() for w in released.findall(s)))
            if hits or words:
                seats += 1
                print('%s · %s\n  seated at: %s%s\n  %s\n' % (os.path.basename(path), section, ', '.join(hits) or '—',
                      ('; released words: ' + ', '.join(words)) if words else '', s))
        print('%s: %d sentences seated, each met at the resolving; a seat decides nothing\n' % (os.path.basename(path), seats))


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'sayings':
        sayings(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '.')
    elif len(sys.argv) >= 3 and sys.argv[1] == 'beside':
        beside(sys.argv[2:])
    else:
        sys.exit(__doc__)
