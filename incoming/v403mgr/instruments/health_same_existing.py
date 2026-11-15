"""v403mgr: the health of Natural Intelligence's gathering file, its opening's part, one concept: same-existing.
The droplets of the concept are read together. The value is once. Two sentences parting are one concern, by its two
sides. Each droplet leaving is named with the droplet now having its value. All or none: with one droplet not found
as it was read, nothing is written.

Use: python3 -I incoming/v403mgr/instruments/health_same_existing.py <root> [--dry]

Applied at main after Merge #713, 15 November 2026: 21 droplets by the grouping, 12 of same-existing and 9 of an
other concept, each of the 9 as it was. Of the 12: 4 of this session's, as they were; 2 as they were; 4 re-said;
2 leaving, each with the droplet having its value. 21 before and 19 after.
"""
import sys
R = sys.argv[1]; DRY = '--dry' in sys.argv
p = R + '/gathering-value/Natural_Intelligence.md'
L = open(p, encoding='utf-8').read().split('\n')
def one(start):
    h = [i for i, l in enumerate(L) if l.startswith(start)]
    assert len(h) == 1, (start[:70], len(h)); return h[0]

H1 = ("- **An explaining** · *The opening's line 3 as it waits:* A **same-existing** thing is the same thing prior-existing before now-existing. "
      "Its *before* is unhelpful in natural defining, and its re-saying by *after* is a candidate in this part. "
      "Each same-existing thing is a now-and-prior-and-same-existing thing, or a prior-and-same-existing thing.")
H2 = ("- **An explaining** · Same-existing and same as are two kinds of same. Same-existing is one thing with its prior and its now, along. "
      "Same as is a self's parity with an other's, with one moment, across. Each *same* has its *as*: its own prior, or an other's. "
      "The opening as it waits has same-existing of a thing in its line 3, and *the same* of one thing with an other in its lines 20, 24 and 32, named in none of them.")
C1 = ("- **Possible incohering** · *A parting, a same-existing thing and next.* One side: each same-existing thing is a now-and-prior-and-same-existing thing "
      "or a prior-and-same-existing thing, with no next in it. Its other side: 12-next-co-same-existing and 16-next-same-existing are each a same-existing name with next; "
      "and an is, newer: next-existing is same-existing after now-existing. The newer goes on: same-existing is with prior, with now and with next.")
C2 = ("- **Possible incohering** · *A parting, each now-existing thing and same-existing.* One side: each now-existing thing is a same-existing thing, and a non-living thing is same-existing. "
      "Its other side, living in Natural Intelligence: each now-existing thing is-or-is-not same-existing by its own; and a suggesting, floating: "
      "other-than-same-existing in the universe is other-than-all-parity. Resolved by neither yet.")
re_said = [
    ("- **An explaining** · *The opening's line 3 as it waits:* A **same-existing** thing is the same thing prior-existing before now-existing. *Its improved line, a candidate:* As it waits.", H1),
    ("- **An explaining** · Same-existing and same as are two kinds of same.", H2),
    ("- **Possible incohering** · *A parting tracked, two sentences of the current understanding.* **2.71 *Next*, with a same-existing name.**", C1),
    ("- **An explaining** · *The universe, a set, a thing.* Each now-existing thing is a same-existing thing. A non-living thing is same-existing.", C2),
]
leaving = [
    ("- **An explaining** · *The current understanding, 6y-u.* All same-existing things are now-and-prior-and-same-existing things, or prior-and-same-existing things.", 'H1'),
    ("- **Possible incohering** · *Of the opening as it waits.* **Sentence 3**, *A **same-existing** thing is the same thing prior-existing before now-existing.* → It says same-existing of a thing.", 'H2'),
]
at = [(one(a), b) for a, b in re_said]; out = [(one(a), b) for a, b in leaving]
print('| Re-said, by its first words | Now |'); print('|---|---|')
for (i, b), name in zip(at, ('H1', 'H2', 'C1', 'C2')): print(f'| {L[i][:92]} | {name} |')
print('| Leaving, by its first words | Its value is in |'); print('|---|---|')
for i, b in out: print(f'| {L[i][:92]} | {b} |')
for i, b in at: L[i] = b
for i, _ in sorted(out, reverse=True): del L[i]
if not DRY: open(p, 'w', encoding='utf-8').write('\n'.join(L))
print('written' if not DRY else 'not written, --dry')
