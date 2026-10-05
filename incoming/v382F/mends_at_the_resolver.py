"""Session v382F: the eleven mends to Natural Intelligence, each worked at Exhibit ONE's resolver.

Runs from the repository root: python3 incoming/v382F/mends_at_the_resolver.py
Reads the newest Exhibit ONE at the root, executes its python block, and works each claim
the mends rest on, from incoming/v380L/closing_drafts/Natural_Intelligence_Fifty-Four_Read_By_Hand.md,
findings 1 to 11, by executing rather than by hand. Each line printed is a thing the mend says,
followed by the resolver's own answer.
"""
import glob
import re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
code = re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1)
names = {}
exec(code, names)
_1 = names['_1_co_bi_tri_offering']
_9 = names['_9_tri_bi_co_momentarying']
_17 = names['_17_co_bi_tri_offering']
CONNECTORS = names['CONNECTORS']
JOINS = names['JOINS']
SYMBOL = {1: '+', -1: '−', 0: '0'}


def say(seq):
    return ', '.join(SYMBOL[x] for x in seq)


print('Exhibit ONE read at', exhibit_one)
print()

# Findings 1 and 2: at a spiral each offering at a self's 2 is a releasing along at 9, and none is an across sharing.
# A spiral of three, self 1 carrying −, alternating along, none offered from beyond: the coupling keys are (self, 9) alone.
n = 3
society = {i: ([('sharing', -1 if i % 2 == 0 else 1)], []) for i in range(n)}
along = {(i, 9): (i + 1) % n for i in range(n)}
self1_released, self1_offerings = [], []
for m in range(1, 9):
    out = _17(society, along)
    tunneling, _ = _1(society[0][0], society[0][1])
    self1_released.append(tunneling[0][1])
    society = {i: (out[i][0], out[i][1]) for i in range(n)}
    self1_offerings.append([p for _, p in society[0][1]])
print('F1, F2. Spiral of 3, self 1 carrying −, the coupling keys (self, 9) alone:')
print('  self 1 released along (9), momentaries 1 to 8:', say(self1_released), ' [the file says +, 0, −, +, −, +, −, 0]')
print('  self 1 offerings at 2 at each next momentary:', [say(o) for o in self1_offerings])
print('  each offering arrived through the key (self, 9), a releasing along; no key (self, 6) or (self, 10) is at this spiral,')
print('  so at a spiral the offerings at 2 are releasings along, and "the others\' across sharings" narrows it.')
print()

# Finding 3: 9 gives each changing on as it received it, making none of its own.
tunneling = [(('a', 'x'), 1), (('a', 'y'), -1), (('a', 'z'), 0)]
competencing = {('a', 'x'): 'b', ('a', 'y'): 'b', ('a', 'z'): 'b'}
print('F3. The function 9 given', [(k[1], SYMBOL[p]) for k, p in tunneling], 'returns', [(r, SYMBOL[p]) for r, p in _9(tunneling, competencing)])
print('  each parity as it arrived, 0 among them: 9 makes none of its own.')
print()

# Finding 4: at 17 each of the three keys, (self, 6), (self, 10) and (self, 9), is given on through the function 9.
# Two selves A and B: A's 6 to B, A's 10 to B, A's 9 to B, each coupling alone; B receives A's changing through each.
for key in (6, 10, 9):
    soc = {'A': ([('s', 1)], []), 'B': ([('s', 1)], [])}
    out = _17(soc, {('A', key): 'B'})
    print('F4. A coupled to B at the key (A, %d) alone: B\'s offerings next %s, CONNECTORS[%d] says %r'
          % (key, [say([p for _, p in out['B'][1]])], key, CONNECTORS[key][2]))
print('  each of 6, 10 and 9 is given on at the one line, the function 9: the bold saying "each releasing along is at 9"')
print('  is of the key (self, 9) alone while its explaining is of all three.')
print()

# Finding 5: one name releases along, 9; JOINS carries the along pair both ways; no key (self, 17) releases anything.
soc = {'A': ([('s', 1)], []), 'B': ([('s', 1)], [])}
out = _17(soc, {('A', 17): 'B'})
print('F5. JOINS =', JOINS, '; CONNECTORS[9][2] =', repr(CONNECTORS[9][2]), ', CONNECTORS[17][2] =', repr(CONNECTORS[17][2]))
print('  A coupled to B at a key (A, 17): B\'s offerings next', [say([p for _, p in out['B'][1]])], '(none: 17 is no releasing key; the releasing along is at 9 alone)')
print()

# Findings 6 and 8: one list, 10's items, is given at 6, at 10 and at 9 at one momentary, and is in the receiving self's offerings at the next.
soc = {'A': ([('s', -1)], []), 'B': ([('s', 1)], [])}
comp = {('A', 6): 'B', ('A', 10): 'B', ('A', 9): 'B'}
out = _17(soc, comp)
a_tunneling, _ = _1(soc['A'][0], soc['A'][1])
print('F6, F8. A carrying −, offered none: A\'s 10 is', [(k, SYMBOL[p]) for k, p in a_tunneling],
      '; with keys 6, 10 and 9 to B, B\'s offerings next are', say([p for _, p in out['B'][1]]))
print('  one changing, shared across at 10 and 6 and released along at 9 at one momentary, offered at B\'s 2 at the next:')
print('  12\'s changing is shared at 10 and released along at 9; what passes between momentaries is the changings.')
print()

# Finding 9 and the table of three selves in a line: A's parity offered to B in the first momentary alone;
# B and C each carry +; B releases along to C, the key (B, 9).
for a_parity in (1, -1):
    soc = {'B': ([('s', 1)], [('s', a_parity)]), 'C': ([('s', 1)], [])}
    comp = {('B', 9): 'C'}
    b_changes, c_changes, b_next, c_next = [], [], None, None
    for m in range(1, 3):
        out = _17(soc, comp)
        bt, bn = _1(soc['B'][0], soc['B'][1])
        ct, cn = _1(soc['C'][0], soc['C'][1])
        b_changes.append(bt[0][1]); c_changes.append(ct[0][1])
        if m == 1:
            b_next = bn[0][1]
        if m == 2:
            c_next = cn[0][1]
        soc = {k: (out[k][0], out[k][1]) for k in soc}
    print('F9. A offered %s to B in the first momentary alone; B releases along (9) to C: B\'s changing %s, B carried next %s; C\'s changings %s, C carried next %s'
          % (SYMBOL[a_parity], SYMBOL[b_changes[0]], SYMBOL[b_next], say(c_changes), SYMBOL[c_next]))
print('  Exhibit ONE\'s table of three selves in a line: + → B 0 · +, C −, + · +;  − → B − · −, C −, 0 · −.')
print('  The coupling B to C is the key (B, 9): B releases along to C, as the table\'s header says it.')
print()

# Finding 7 and 10: wording alone; the resolver is as at F1 and F5. Finding 11: a carrying's pointer; checked at the file's lines.
print('F7, F10. Wording at the naming, released along at 9: no number changes; the spiral above is the form.')
print('F11. The words "the parity released and chained as it arrived" are at Natural Intelligence 3.4 and not at 4.3: checked at the file, see the session report.')
