"""apply_aimed.py: enter readers' pairs at Natural Intelligence (ni_pairs), Exhibit ONE (one_pairs) and the Co-Chaining Logic Registry (thirty_pairs, by step), all checked before entering.
Refuses a pair that brings a dissolved word or a new -ed form, unbalances ** or *, is not unique, lies in the opening, or touches steps 1 to 64.
Rebuilds each THIRTY group's Entering line from its Adding lines. Archives the three files first.
Usage, from the repository root: python3 apply_aimed.py [--dry] [--tag=NAME] PAIRS.json ...
After: python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/cohere_one.py, check_set.py, ni_thirty_check.py, thirty_groups_check.py < THIRTY."""
import json, re, os, shutil, sys
os.chdir(os.environ.get('CORUS', '.'))
NI = 'Natural_Intelligence_v391.md'
TH = 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v391.md'
DRY = '--dry' in sys.argv
tag = [a for a in sys.argv[1:] if a.startswith('--tag=')]
A = 'archive/session_v391/prior_to_aimed_' + (tag[0][6:] if tag else 'droplets')
BAN = re.compile(r'\bnever\b|parity-chang|alternat|offer|arriv|\bcarr|\bcontinu(?:e|es|ing|ed)\b|\bcross|differ(?!encing)|still-possibl|stilling|owned by neither|neither reaches|third living|odd,? existing|even,? possibling', re.I)
OKED = {'need', 'seed', 'speed', 'red', 'shed', 'bed', 'feed', 'indeed', 'proceed', 'hundred', 'sacred', 'embed', 'breed', 'kindred', 'naked', 'sided', 'squared', 'cubed'}
ONE = 'Exhibit_ONE_Natural_Resolver_v391.md'
ni, th, one = open(NI).read(), open(TH).read(), open(ONE).read()
op_end = ni.index('\n**ONE · ') if '\n**ONE · ' in ni else 0
rej, done = [], 0
kinds = {}


def bad(old, new):
    nb = len(BAN.findall(new))
    if nb and nb >= len(BAN.findall(old)):
        return 'dissolved ' + BAN.search(new).group(0)
    ne = [w for w in re.findall(r'\b[a-z-]+ed\b', new, re.I) if w.lower() not in OKED and not w.lower().endswith('-sided')]
    oe = re.findall(r'\b[a-z-]+ed\b', old, re.I)
    if [w for w in ne if w not in oe]:
        return 'new -ed ' + str([w for w in ne if w not in oe])
    if new.count('**') != old.count('**') or new.count('*') % 2 != old.count('*') % 2:
        return 'markers'
    return ''


for jp in [a for a in sys.argv[1:] if not a.startswith('--')]:
    for r in json.load(open(jp)):
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
        for p in r.get('ni_pairs') or []:
            o, n = p['old'], p['new']
            w = bad(o, n) or ('count %d' % ni.count(o) if ni.count(o) != 1 else '')
            if not w and ni.index(o) < op_end:
                w = 'in the opening'
            if w:
                rej.append(('NI', r['droplet'][:40], w, o[:60]))
                continue
            ni = ni.replace(o, n)
            done += 1
        for p in r.get('one_pairs') or []:
            o, n = p['old'], p['new']
            w = bad(o, n) or ('count %d' % one.count(o) if one.count(o) != 1 else '')
            if '```' in o or 'def _' in o:
                w = w or 'code block'
            if w:
                rej.append(('ONE', r['droplet'][:40], w, o[:60]))
                continue
            one = one.replace(o, n)
            done += 1
        for p in r.get('thirty_pairs') or []:
            o, n, st = p['old'], p['new'], int(p['step'])
            m = re.search(r'^%d\. ' % st, th, re.M)
            w = bad(o, n)
            if st <= 64:
                w = w or 'opening step'
            if not m:
                w = w or 'no step'
            else:
                e = m.start() + re.search(r'\*Adding: .*?\*\n', th[m.start():], re.S).end()
                seg = th[m.start():e]
                if seg.count(o) != 1:
                    w = w or 'count in step %d' % seg.count(o)
            if w:
                rej.append(('TH', r['droplet'][:40], w, o[:60]))
                continue
            th = th[:m.start()] + seg.replace(o, n) + th[e:]
            done += 1
parts = re.split(r'(\n## \d+ [^\n]*\n)', th)
out = [parts[0]]
for k in range(1, len(parts), 2):
    head, body = parts[k], parts[k + 1]
    adds = [x for y in re.findall(r'\*Adding: (.*?)\.\*', body) for x in y.split('; ')]
    if re.search(r'\*Entering: (.*?)\.\*', body) and adds:
        body = re.sub(r'\*Entering: (.*?)\.\*', lambda m: '*Entering: ' + '; '.join(adds) + '.*', body, count=1)
    out += [head, body]
th = ''.join(out)
print('kinds', kinds, 'pairs applied', done, 'rejected', len(rej))
for x in rej:
    print('  REJ', x)
if not DRY:
    os.makedirs(A, exist_ok=True)
    for f in (NI, TH, ONE):
        if not os.path.exists(os.path.join(A, f)):
            shutil.copy(f, os.path.join(A, f))
    open(NI, 'w').write(ni)
    open(TH, 'w').write(th)
    open(ONE, 'w').write(one)
