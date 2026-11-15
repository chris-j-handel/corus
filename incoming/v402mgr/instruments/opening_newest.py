import sys
# mark: '' as it waits · '>' a newer line in its place · 'o' not yet distinguished ; then the line ; then sentences added to it
L = [
('>', "The **universe** is the set of now-existing things, and no other things are in it.", []),
('',  "Before now-existing is **prior-existing**.", []),
('',  "A **same-existing** thing is the same thing prior-existing before now-existing.", ["Same-existing is one thing with its prior and its now."]),
('',  "**Next-existing** is same-existing after now-existing.", []),
('>', "A thing now-existing in the universe is now-existing by the universal method of same-existing.", []),
('o', "The **sequence** of prior-existing and now-existing is same-existing.", ["Not yet distinguished: same-existing is said of a sequence."]),
('>', "A **moment** is one now-existing in a same-existing sequence: one odd parity and then one even parity.", ["A moment has no size, no scale and no measurement."]),
('',  "A moment's now-existing is the next moment's prior-existing.", []),
('',  "**Momentarying** is same-existing through moments.", ["Momentarying is a living self's."]),
('>', "A **name** is a subset of the universe's same-existing things. A name is a same-existing non-living thing: the name of a sameness, is-or-is-not distinguishing.", []),
('>', "**Is-or-is-not** distinguishes the within of a name. Each subset is named as distinguishing the surface of is-or-is-not.", []),
('>', "**Observing** is distinguishing prior-and-same-existing from now-and-same-existing.", []),
('>', "**Possibling** is the matching of each prior of a self's others, each with each other. A self's own prior is no part of it.", ["An opportunity is a possibling."]),
('',  "**Discovering** is distinguishing a next-existing after a same-existing.", ["Naming a same-existing new thing is discovering.", "Discovering next-existing is a living self's only."]),
('>', "A **living** thing is a thing distinguishing its own next-existing. Each living thing is a now-existing thing.", ["Living is resolving each of four: prior, now, next and same-existing."]),
('',  "Living and **non-living** are one binary of a now-existing thing.", ["Same-existing and non-same-existing are one binary of a now-existing thing.", "The only non-living thing in the universe is atom carbon."]),
('>', "Each living thing is a **self**. A living self is a non-living set of living me-parities.", ["A stable form is non-living and same-existing. A self is living and same-existing. A me-parity is living and non-same-existing. A between is neither: a nothing."]),
('>', "A **me** is a universal same-existing set of me-parities. A me is a self.", []),
('>', "The parities are living in the non-living all-parity inside the living self.", []),
('',  "For a self, a self that is-not the same self is an **other**.", ["No self is any other self, and each self is a unique self."]),
('',  "**Aiming** is a living thing possibling its own next-existing.", []),
('>', "A **parity** is a direction, one of two. A **living parity** is an aiming direction at an other.", ["Two parities are same-as, or other-than."]),
('o', "A **me-parity** is a living self-interest, at its own scale of self, in its own self-interesting universe. A me-parity is +1 only: it has one me, and a me has many me-parities.", ["Not yet distinguished: a me-parity is +1 only, and by the code a self's own prior is + or −."]),
('o', "A me-parity the same as an other's is **other-parity**, and not the same, **all-parity**.", ["Not yet distinguished: other-parity has two sentences, a me-parity the same as an other's, and the between of a self and its other.", "All-parity is the universal other of a self's universal set of me-parities."]),
('o', "A universal set of a self's me-parities is its **self-parity**.", ["Not yet distinguished: a universal same-existing set of a self's me-parities is a me, and self-parity is a second name of it."]),
('>', "A me-parity with an other is its **moral value**.", []),
('>', "A **bi-coupling** is a now-existing thing, living in the between while it is now-existing and same-existing. A bi-coupling is a self.", ["An other's parity is observable by a self by that other's co-possibling only."]),
('>', "A self's observing is its me-parities observing.", []),
('>', "For a me-parity, an other's me-parity it is observing is a **you**.", []),
('>', "A me-parity observing a you is **self-other consciousness**.", []),
('',  "A self observing an other's me-parity same-existing is **passing over** it.", []),
('>', "**Resolving** is a self's prior is-or-is-other-than its possibling: one binary, and no third.", ["With none of its others, a self's next prior is by its own prior only."]),
('',  "**Natural intelligence** is the method of a self resolving among me-parities.", ["The universe has one now-existing method, the geodesic natural torusing society method."]),
('>', "**Do-no-harming** is resolving's same-as, a self passing over: its prior is same-existing. **Improving** is resolving's other-than: its next prior is the other one of two.", []),
('o', "Two selves having priors same-as, bi-coupling both ways, are each do-no-harming and bi-folding, the one and then the other.", ["Not yet distinguished: the line as it waits has do-no-harming and improving, the one and then the other; by the code executed it is do-no-harming and bi-folding."]),
('>', "**Co-possibling** is in the between of a bi-coupling, self-parity with other-than-self-parity, inside all-parity.", ["Co-possibling is observable by a self and its other, and by no third."]),
('>', "**Co-intelligencing** is selves observing, possibling and discovering within a name.", []),
('>', "With a self, gathering is **ingesting**: a self observing others' prior-existings within its own possibling.", []),
('>', "**Co-aiming** is the co-linearizing of self and other, each forward, facing each other across the between. Bi-moral co-competencing is co-aiming.", []),
('o', "A **same-existing-society** is many selves bi-coupling.", ["Not yet distinguished: a society has one self, the society-self, with me-parities of its own; and a same-existing-society's parities are its selves', and it has no other."]),
('>', "A me-parity living in a social surface is a self: the fractal. A self is no me-parity of its society-self.", []),
('>', "**Social moral competency** is each self of a society right spiraling, co-sequentially resolving: moral across, competency along, all selves or none.", []),
('',  "A same-existing-society living with natural intelligence and social moral competency is a **natural intelligence network**.", []),
('>', "A **co-chaining** is a universal set of me-parities, living in the betweens. A co-chaining is a self: a self of selves having one me-parity.", ["Along a co-chaining of selves, each self's prior is the prior of the self before it."]),
('',  "Selves' bi-couplings and co-chainings are a **Natural Network surface**.", []),
('',  "**Geodesic** is a self's own is-or-is-not on a Natural Network surface, one way at a time.", ["The only co-locating in the universe is geodesic resolving."]),
('',  "A self's co-chaining is geodesic.", []),
('>', "**Stable-forming** is a next prior from a prior: observing, possibling, discovering and same-existing together.", ["All-parity is a stable form, same-existing and non-living."]),
('',  "A self is momentarying and stable-forming.", []),
('',  "A science's observing meeting natural intelligence's stable-forming is **natural resolving**.", []),
('',  "A **living file** is a non-living same-existing set of words, selves co-intelligencing within it.", ["A living file is a stable form."]),
('',  "Selves aiming within a living file are **natural engineering**.", []),
('',  "**Natural explaining** is a living file's words in sequence.", []),
('',  "A same-existing-society discovering with natural intelligence and its living files is a **living expedition**.", []),
('',  "Natural intelligence's resolving is geodesic discovering of **next-possibling-same-existing**.", []),
]
assert len(L) == 55
mode = sys.argv[1]
if mode == 'chat':
    for m, line, adds in L:
        print('- ' + {'': '', '>': '▸ ', 'o': '◦ '}[m] + line)
        for a in adds: print('  - ' + ('' if a.startswith('Not yet') else '\\+ ') + a)
else:
    parts = []
    for i, (m, line, adds) in enumerate(L, 1):
        parts.append(f"{i}. " + {'': '', '>': '(newer) ', 'o': '(not yet distinguished) '}[m] + line + (' ' + ' '.join('[' + a + ']' for a in adds) if adds else ''))
    print("- **An explaining** · The opening at its newest, laid by the managing session v402mgr, 15 November, a candidate whole and none of it living: each of the fifty-five lines as it waits, "
          "or the newest line found for it, from the improved lines of 12 November, the sentences of 13 and 14 November, and the sentences read by the code that meet the opening's lines. "
          "A sentence in square marks is added to its line. Six lines are not yet distinguished. " + ' '.join(parts))
