"""opening70_v391.py: the motion entering Natural Intelligence's 70-line opening at v391 (me, co-intelligencing defined before living, other after the bi-coupling, receiving, inward and outward, a living file a non-living same-existing set of words).
Reads the new opening from incoming/v391/Opening_Resolved_v391.md; ADD gives each line's Adding text or the old step whose Adding it keeps; MAP old step to new step.
Writes NI's opening, THIRTY's groups 1 to 4 word for word with Entering rebuilt from Adding, renumbers THIRTY's later steps, re-points step references at THIRTY, Equilibria and Numbers.
Run with --dry first and read the re-pointings it prints."""
import re, os, sys, shutil
os.chdir(os.environ.get('CORUS', '.'))
DRY = '--dry' in sys.argv
NI = 'Natural_Intelligence_v391.md'; TH = 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v391.md'
EQ = 'Exhibit_TWENTY-EIGHT_Equilibria_Registry_v391.md'; NU = 'Exhibit_THREE_Natural_Numbers_v391.md'
SRC = 'incoming/v391/Opening_Resolved_v391.md'
A = 'archive/session_v391/prior_to_opening70'
src = open(SRC).read()
s = src.index('1. The **universe**'); e = src.index('\n\n## Read for harm')
L = [re.sub(r'^\d+\. ', '', x) for x in src[s:e].split('\n')]
assert len(L) == 70, len(L)
# new line -> old step whose Adding stays, or a new Adding text
ADD = {i: None for i in range(1, 71)}
keep = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,10:9,11:10,12:11,18:14,19:15,21:18,22:19,23:20,25:22,29:24,30:25,31:26,33:28,36:30,37:31,38:32,41:34}
for o in range(36, 65):  # old 36..64 -> new +6, except those re-said below
    keep[o + 6] = o
new_add = {
 9: 'only one universe possibly same-existing',
 13: "a me, a self's universal set",
 14: "each now-existing thing within a self's me, is-or-is-not",
 15: 'co-intelligencing, selves observing, possibling and discovering within a universal set',
 16: 'living, co-intelligencing',
 17: 'each self living',
 20: 'living and non-living, one binary of each now-existing thing',
 24: 'a bi-coupling, two selves; sharing',
 26: 'an other, a self a self bi-couples with',
 27: "parity, a self's changing direction relative to a thing within its me",
 28: "+ and −, a parity's two directions",
 32: "a living parity's me within the self's me",
 34: 'receiving, the parities its others share',
 35: 'agreeing and parting, one binary of parities received',
 39: 'a prior-existing parity inverting, its possibling an empty set',
 40: 'a prior-existing parity inverting, the parities received parting',
 47: 'two selves alike, each bi-coupling only in their pair, do-no-harming and improving in turn',
 48: 'co-possibling, each self sharing its possibling within its me',
 61: 'inward and outward',
 64: 'a living file, a non-living same-existing set of words, selves co-intelligencing within it',
 67: 'natural explaining, the dividing of a living file',
}
for k in new_add: keep.pop(k, None)
# old -> new for references
MAP = {}
for n, o in keep.items(): MAP[o] = n
MAP.update({12: 26, 13: 17, 16: 15, 17: 20, 21: 24, 23: 27, 27: 32, 29: 35, 33: 39, 35: 15, 41: 47, 42: 48, 55: 61, 58: 64, 61: 67})
for o in range(1, 65): assert o in MAP, o
for o in range(65, 3000): MAP[o] = o + 6
PARA = [11, 23, 51, 70]
th = open(TH).read(); ni = open(NI).read()
oldadd = {}
for m in re.finditer(r'^(\d+)\. .*?\n\n\s*\*Adding: (.*?)\.\*\n', th, re.M | re.S):
    n = int(m.group(1))
    if n <= 64: oldadd[n] = m.group(2)
assert len(oldadd) == 64
adds = [new_add[i] if i in new_add else oldadd[keep[i]] for i in range(1, 71)]
g = [m.start() for m in re.finditer(r'^## [1-5] ', th, re.M)]
titles = [th[x:th.index('\n', x)] for x in g[:4]]
head = th[:g[0]]; rest = th[g[4]:]
out = ''; start = 0
for gi, end in enumerate(PARA):
    out += '%s\n\n        *Entering: %s.*\n\n' % (titles[gi], '; '.join(adds[start:end]))
    for i in range(start, end):
        out += '%d. %s\n\n        *Adding: %s.*\n\n' % (i + 1, L[i], adds[i])
    start = end
rest = re.sub(r'^(\d+)\. ', lambda m: '%d. ' % MAP[int(m.group(1))], rest, flags=re.M)
REF = re.compile(r'\b([Ss]teps? )(\d+)((?:(?:, | and | or | to )\d+(?!\d|\.\d|-))*)(?! up| less| on\b)')
log = []
def remap(t, tag):
    def rep(m):
        g0 = m.group(0)
        if g0 == 'step 1 to 3 to 5 to 6': return g0
        mm = re.match(r'step (\d+), 17$', g0)
        if mm and int(mm.group(1)) > 200:
            r = 'step %d, 17' % MAP[int(mm.group(1))]; log.append((tag, g0, r)); return r
        nums = re.findall(r'\d+', m.group(2) + m.group(3)); it = iter([MAP[int(x)] for x in nums])
        r = m.group(1) + re.sub(r'\d+', lambda _: str(next(it)), m.group(2) + m.group(3))
        if r != g0: log.append((tag, g0, r))
        return r
    return REF.sub(rep, t)
th2 = head + out + remap(rest, 'TH')
# NI opening
s = ni.index('The **universe** is the set of all now-existing things. \\')
endline = 'Natural intelligence is geodesic discovering of **next-possibling-same-existing** within the universe. \\\n'
e = ni.index(endline) + len(endline)
blocks = []; start = 0
for end in PARA:
    blocks.append('\n'.join(x + ' \\' for x in L[start:end])); start = end
ni2 = ni[:s] + '\n\n'.join(blocks) + '\n' + ni[e:]
others = {f: remap(open(f).read(), f[:24]) for f in (EQ, NU)}
print('steps', len(re.findall(r'^\d+\. ', th2, re.M)), 'refs', len(log))
for x in log[:20]: print(x)
if not DRY:
    os.makedirs(A, exist_ok=True)
    for f in (NI, TH, EQ, NU): shutil.copy(f, os.path.join(A, f))
    open(TH, 'w').write(th2); open(NI, 'w').write(ni2)
    for f, t in others.items(): open(f, 'w').write(t)
