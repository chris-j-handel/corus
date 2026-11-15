"""v402mgr: the health of Natural Intelligence's gathering file, its opening's part, two concepts: the universe, and a moment.
The droplets of one concept are read together. The value is once. Two sentences parting are one concern, by its two sides.
Each droplet leaving is named with the droplet now having its value."""
import sys, json, re
R = sys.argv[1]; p = R + '/gathering-value/Natural_Intelligence.md'
L = open(p, encoding='utf-8').read().split('\n'); J = json.load(open('/tmp/opening_groups.json')); idx = J['idx']
d = lambda k: L[idx[k]]
U1 = ("- **An explaining** · The universe is the set of now-existing things, and no other things are in it. No now-existing thing is outside it, and nothing enters it or leaves it. "
      "*Set* and *thing* are its givens, with no line before them. The first sentence here is the improved line for the opening as it waits, a candidate.")
U3 = ("- **An explaining** · Science has the universe as an existing thing; natural intelligence has it as the set of now-existing things. The universe has one now-existing method, of now-existing things now-existing: "
      "the geodesic natural torusing society method, and no other is possible. The universe is a fractal set method.")
U4 = ("- **Possible incohering** · \"The universe is a non-living same-existing set.\" → A concern by its two sides, of the universe as same-existing, resolved by neither yet. "
      "One side, living in this file: this sentence, outside the opening and carried by its sentences together; and *By observing, the universe is a same-existing set.* "
      "Other side: the universe is not a same-existing thing; same-existing said of the universe is said of a set; and what is known is of each now-existing thing in it: "
      "a thing now-existing in the universe is now-existing by the universal method of same-existing, the improved line for the opening as it waits, whose own line has the universe as same-existing and next-existing, not knowable from the lines before it. "
      "Out, by the sentences read by the code: the universe as a third living self. The universe is its things, living and its involution, and no non-living set apart from them.")
U5 = ("- **Possible incohering** · \"Only one universe is possibly now-existing.\" → A concern by its two sides, of one universe or each one's own, resolved by neither yet. "
      "One side: this sentence; and *the universe* is one name, of one set, and no other set has it. "
      "Other side: a named subset is the universe to a bi-coupling, a self, its other and all other-than the two: a society, in the universe of more than this; "
      "a self is in the same-existing universe it has with the other selves of its society; every three is in a fourth, its universe, a self, its other and all of one same scale and their universe one scale larger; "
      "each now-existing moment has its own prior-existing; and Exhibit TWENTY Natural Naming has, living in it: *Universes of each size and scale share moments of co-sequential changing, and neither a moment nor a universe is possibly existing as a thing apart from its existing things.* "
      "One universe, or each society's own, is in no sentence yet.")
U6 = ("- **An explaining** · A moment is one resolving, together. It has no size, no scale and no measurement: it is neither a duration on a clock nor a common beat. "
      "Its one now-existing is one odd parity and then one even parity.")
leaving = {  # droplet: (its first words, the droplet now having its value)
 32: ('**Possible incohering** · "The universe is a non-living same-existing set." → Two sayings part', 'U4'),
 123: ('**An explaining** · "The universe is a non-living same-existing set." is outside the opening', 'U4'),
 191: ("**Possible incohering** · The waiting opening's sentence 1, with the working's session", 'U1'),
 192: ("**Possible incohering** · The waiting opening's sentence 5, with the working's session", 'U4'),
 233: ('**An explaining** · *The current understanding, 5b.* A named subset is the universe to a bi-coupling', 'U5'),
 282: ('**An explaining** · *The current understanding, 6y-c.* The universe has one now-existing method', 'U3'),
 516: ('**Possible incohering** · *A parting tracked, two sentences of the current understanding.* **2.27', 'U5'),
 645: ('**An explaining** · *The universe, a set, a thing.* The universe is the set of now-existing things. By naming', 'U1'),
 647: ('**An explaining** · *The universe, a set, a thing.* Science: the universe is an existing thing', 'U3'),
 648: ('**An explaining** · *The universe, a set, a thing.* The universe is a fractal set method.', 'U3'),
 649: ('**An explaining** · *The universe, a set, a thing.* The universe is not a same-existing thing.', 'U4'),
 650: ('**An explaining** · *The universe, a set, a thing.* No thing can enter or leave the universe', 'U1'),
 655: ('**An explaining** · *The universe, a set, a thing.* Every three is in a fourth, its universe.', 'U5'),
 762: ('**Possible incohering** · *Of the opening as it waits.* **Sentence 1**', 'U1'),
 764: ('**Possible incohering** · *Of the opening as it waits.* **Sentence 5**', 'U4'),
 64: ('**An explaining** · A momentary is one resolving, together', 'U6'),
}
for k, (first, _) in leaving.items(): assert d(k)[2:].startswith(first), (k, d(k)[:120])
assert d(31).startswith('- **Possible incohering** · "The universe is the set of all now-existing things." → A re-saying')
at = idx[31]
gone = sorted(idx[k] for k in leaving)
new = []
for i, l in enumerate(L):
    if i == at: new += [U1, U3, U4, U5, U6]
    if i in gone: continue
    new.append(l)
open(p, 'w', encoding='utf-8').write('\n'.join(new))
print('leaving', len(leaving), '· entering', 5)
for k, (first, u) in sorted(leaving.items()): print(f"| {re.sub(r'[|]', '/', first[:95])}… | {u} |")
