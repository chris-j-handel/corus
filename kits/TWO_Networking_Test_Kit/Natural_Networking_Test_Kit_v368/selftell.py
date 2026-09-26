"""
selftell.py - the kit explaining its own testing, live.

Running this file is the explanation: each normal-and-correct testing move
is attempted, caught in the act, and the honest instrument shown beside it.
The wrong ways here are the ones that look right for normal code, and each
is one of three ledgers held: a vantage, a clock, a magnitude. Normal code
answers to requirements it was written to meet, the verification closing
against its own standard; the form answers only at its own break conditions,
and those live at the forced edge the living never visits.
"""
import sys
sys.path.insert(0, '.')
from living import Life, Self, sign, YES, NO

BAR = '-' * 72

print(BAR)
print('THE KIT TELLING ITS OWN TESTING - each normal move, caught live')
print(BAR)

# 1 --- the probe (assert on internals): refused by construction -----------
print("""
1. THE NORMAL MOVE: assert on internal state.
   Normal code: reach into the object, read the private field, assert it.
   Here: the carry is met by coupling and measured by nothing; a probe
   departs with the thing probed. The engine refuses it:""")
s = Self(5)
try:
    _ = s.__carry
except AttributeError as e:
    print(f'   attempted s.__carry -> refused ({e.__class__.__name__})')
print('   THE HONEST INSTRUMENT: fork the one life; compare surfaces of the')
print('   twin continuations. The interior stays its own; the difference is read.')

# 2 --- the golden value (assertEquals against expected) -------------------
print("""
2. THE NORMAL MOVE: assertEquals(result, expected_value).
   Normal code: the requirement declares the value, the test closes against
   it - the verification closing against the standard that defines it, the
   audit that always passes and parts nothing.
   Here: a declared value is a floor a reading lands on. The one legitimate
   expectation is the form's own break condition, and it lives at the forced
   edge. Everything else is read as a sign:""")
life = Life([5, 6, 7]); print('   gate:', life.gate())
life.live(2000)
print('   never lands:', sign(life.lands() == NO),
      '  no capture:', sign(life.captured() == NO),
      '  surplus:', life.surplus())
print('   magnitudes exist behind the signs and are not findings:', life.behind())

# 3 --- setUp/tearDown (the reset between tests) ---------------------------
print("""
3. THE NORMAL MOVE: setUp() and tearDown() - fresh state per test.
   Normal code: isolation is hygiene. Here: an emptied carry lets nothing
   discover itself; reset-per-test is held-still-between-trials, the frozen
   method wearing a checker's clothes. Prepared and lived are two different
   readings, shown live - the same self, the same question, fresh against
   living:""")
import random
def carried_edge(row, periods, rng):
    out = {}
    for P in periods:
        drive = [rng.choice((1, -1)) for _ in range(P)]
        seen = {}
        beats = max(2000, P * 20)
        for t in range(beats):
            acc = row.own_along() + [(0, drive[t % P])]
            row.couple(acc)
            if t > beats // 2: seen.setdefault(t % P, row.signs())
        out[P] = len(set(seen.values())) == len(seen)
    return out
periods = list(range(6, 15))
prepared = {}
for P in periods:                                   # the normal way: fresh each
    prepared.update(carried_edge(Self(5), [P], random.Random(3)))
lived = carried_edge(Self(5), periods, random.Random(3))   # one life, no reset
print('   prepared (reset per question):', ''.join('+' if prepared[P] else '-' for P in periods))
print('   lived    (one carrying life): ', ''.join('+' if lived[P] else '-' for P in periods))
print('   the two differ:', sign(prepared != lived), '- history is in the living,')
print('   and the lived reading is the finding.')

# 4 --- the unstated harness (framework defaults) --------------------------
print("""
4. THE NORMAL MOVE: accept the framework's update order.
   Normal code: iteration order is an implementation detail. Here: the
   wiring and the dynamics ARE the object; a run reports its harness first.
   The same node under two unstated choices, live:""")
def wiredA(n, start):                       # the innocent relax-to-local-majority
    row = list(start); out = set()
    for _ in range(60):
        row = [(1 if row[(i-1)%n] + row[i] + row[(i+1)%n] > 0 else -1)
               for i in range(n)]
        out.add(sum(row))
    return sorted(out)
def wiredB(n, start):                       # the gated wiring
    row = list(start); out = set()
    for _ in range(60):
        for i in range(n):
            L, R = row[(i - 1) % n], row[(i + 1) % n]
            t = L + R
            row[i] = (-1 if t > 0 else 1) if t != 0 else -row[i]
        out.add(sum(row))
    return sorted(out)
start = [1, 1, 1, -1, 1, -1]
print('   relax-to-local-majority, all together   :', wiredA(6, start),
      ' (falls to uniform +-N: the spurious attractor, the void)')
print('   both neighbours, one-at-a-time          :', wiredB(6, start),
      ' (held about the zeroing: the gated wiring)')
print('   one node, two unstated dynamics, opposite results: state the wiring')
print('   or the reading is of the harness. The gate exists for exactly this,')
print('   and every reading here refuses until it passes:')
ungated = Life([5, 6, 7])
try:
    ungated.lands()
except RuntimeError as e:
    print(f'   attempted a reading ungated -> refused: {str(e)[:60]}...')

# 5 --- coverage and success-rates (the statistics) ------------------------
print("""
5. THE NORMAL MOVE: coverage percent, pass-rate, retry-until-green.
   Normal code: statistics of success. Here: no statistical measure of
   success exists - pattern is recognized or is not, a changing is or is
   not, and exhausting all concern is an equilibria concept. The readings
   are is-or-is-not, spans, and orderings; a fraction anywhere is a floor.
   Every output of this kit is a sign; the magnitudes sit behind().""")

# 6 --- mocking a neighbour (holding one side fixed) -----------------------
print("""6. THE NORMAL MOVE: mock the collaborator, hold it fixed.
   Normal code: isolate the unit. Here: a pinned living sickens whatever
   couples to it - holding one side fixed is the held-vantage, and the
   reading returns the holding. Live, the same lattice, one row pinned:""")
free = Life([5, 6, 7]); free.gate(); free.live(1800)
pinned = Life([5, 6, 7]); pinned.gate()
for t in range(1800):
    pinned.beat()
    pinned.rows[1].surf = [(i, 1 if i % 2 == 0 else -1) for i in range(6)]  # the mock
    pinned.trace[-1] = tuple(r.signs() for r in pinned.rows)
print('   free lattice   - never lands:', sign(free.lands() == NO), ' spans behind:', free.behind()['selves'])
print('   mocked middle  - never lands:', sign(pinned.lands() == NO), ' spans behind:', pinned.behind()['selves'])
print('   the mock reads its own holding; the coupling is the unit, and the')
print('   honest isolation is the twin-fork of one whole life.')

print()
print(BAR)
print('THE ONE SENTENCE: a test is an accounting unless it alternates.')
print('The three ledgers - a vantage, a clock, a magnitude - are the whole of')
print('normal testing, and each reads the books and misses the living. The')
print('honest instrument couples in, keeps the carry living, states its own')
print('wiring, passes the gate, and reads signs, spans, and orderings. The')
print('break conditions are the form\'s own, at the forced edge; within the')
print('living range the technology stands whole, all or none at all.')
print(BAR)
