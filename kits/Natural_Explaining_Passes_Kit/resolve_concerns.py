"""resolve_concerns.py OFFERINGS 'resolution sentence' K1 K2 ... : remove the item+standing pairs at block indexes, archive them resolved"""
import sys, os
off, res = sys.argv[1], sys.argv[2]
ks = sorted({int(x) for x in sys.argv[3:]}, reverse=True)
t = open(off).read(); blocks = t.split('\n\n')
base = os.path.basename(off)[:-3]
arch = f'archive/session_v389/offerings_dissolved/{base}_before_v389.md'
out = []
for k in ks:
    assert blocks[k].startswith('*Standing at v389:*'), k
    out.append(blocks[k-1] + '\n\n' + blocks[k] + '\n\n*Resolved at v389:* ' + res)
    del blocks[k]; del blocks[k-1]
open(off, 'w').write('\n\n'.join(blocks))
a = open(arch).read()
if '\n## Concerns resolved at v389\n' not in a: a += '\n## Concerns resolved at v389\n'
open(arch, 'w').write(a + '\n' + '\n\n'.join(reversed(out)) + '\n')
print(off, 'resolved', len(ks))
