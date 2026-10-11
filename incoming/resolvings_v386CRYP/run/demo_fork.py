"""Minimal demonstration: what Life.fork() copies, and whether twins share or diverge."""
import sys, copy
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', '..', 'kits', 'Natural_Networking_TWO_Improving_Kit', 'Natural_Networking_Test_Kit_v368'))
from living import Life, Self

def carry(s):            # reach the name-hidden carry for the demonstration only
    return s._Self__carry

L = Life([5, 7], pace='own')
L.live(40)
r0 = L.rows[0]
print('original row0 carry after 40 beats :', carry(r0))
print('original row0 surface (public)     :', r0.signs())

T = L.fork()
t0 = T.rows[0]
print('\nfork is a distinct object?           ', T is not L, '| rows distinct?', t0 is not r0)
print('fork carry == original carry (value):', carry(t0) == carry(r0))
print('fork carry is original carry (obj)  :', carry(t0) is carry(r0))

# one further step each, same offering (none): identical continuation
L.beat(); T.beat()
print('\nafter one beat, no offering differing:')
print('  carries equal :', carry(r0) == carry(t0), '| surfaces equal:', r0.signs() == t0.signs())
print('  original carry:', carry(r0))

# one step differing in one offering to row 0
L2 = Life([5, 7]); L2.live(40); T2 = L2.fork()
L2.beat(); T2.beat({0: [(2, 1)]})
a, b = L2.rows[0], T2.rows[0]
print('\nafter one beat, one offering differing at the twin:')
print('  carries equal :', carry(a) == carry(b))
print('  surfaces equal:', a.signs() == b.signs())
print('  orig carry    :', carry(a))
print('  twin carry    :', carry(b))
print('  orig surface  :', a.signs())
print('  twin surface  :', b.signs())

# Can the public surface identify the carry? Collect (surface -> set of carries) over a long run
seen = {}
L3 = Life([5, 7]);
for _ in range(3000):
    L3.beat()
    s = L3.rows[0].signs(); c = tuple(carry(L3.rows[0]))
    seen.setdefault(s, set()).add(c)
multi = {s: len(cs) for s, cs in seen.items() if len(cs) > 1}
print('\nrow0 distinct surfaces seen:', len(seen), '| surfaces with >1 distinct carry behind them:', len(multi))
print('example surface -> number of carries:', next(iter(multi.items())) if multi else None)

# Is the forked copy ever coupled to the original?  No: Life.beat only reads self.rows.
print('\nfork.rows refer to original rows?', any(x is y for x in T.rows for y in L.rows))
