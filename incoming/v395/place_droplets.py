"""Place the droplets gathered while the opening resolved, each at its partner gathering-value file. Run at the repository root."""
import re, importlib.util, os

SP = os.path.dirname(os.path.abspath(__file__))

def insert_end_of(path, heading, items):
    """Insert items at the end of the section opened by the line `heading` (exact), before the next heading."""
    L = open(path, encoding='utf-8').read().split('\n')
    i = L.index(heading)
    j = i + 1
    while j < len(L) and not L[j].startswith('#'):
        j += 1
    k = j
    while k > i + 1 and L[k - 1].strip() == '':
        k -= 1
    L[k:k] = items
    open(path, 'w', encoding='utf-8').write('\n'.join(L))

def insert_after(path, heading, items):
    L = open(path, encoding='utf-8').read().split('\n')
    i = L.index(heading)
    L[i + 2:i + 2] = items + ['']
    open(path, 'w', encoding='utf-8').write('\n'.join(L))

def append(path, items):
    t = open(path, encoding='utf-8').read().rstrip('\n')
    open(path, 'w', encoding='utf-8').write(t + '\n' + '\n'.join(items) + '\n')

# ---------- Natural Intelligence's gathering-value, at its opening ----------
NI = [
"- **An explaining** · The opening, 61 sentences, each defining only from the sentences before it, binary, all or none, and in natural naming, is word for word the Co-Chaining Logic Registry's steps 1 to 61 (v394, 4 November 2026). The former opening of 70 sentences is Natural Intelligence v391's. Each item above meeting a former sentence is read against this opening at Natural Intelligence's improving, section by section, and goes to the section it meets.",
"- **Possible exploring** · \"Each non-living thing is a **stable-forming emanation**.\" left the opening: *stable-forming* came before a stable form entered, and *emanation* says not from what, so neither side is held all or none, and no sentence after it in the opening needs it. Natural Intelligence's later sections say it at 14 places, each read at its own section, beside the carbon value gathering at Natural Chemistry's and Natural Biology's gathering-values.",
"- **An explaining** · \"The universe is a non-living same-existing set.\" left the opening, carried by two sentences together, all or none. — at \"Only living things are within a living set.\" with \"Within the universe are living and non-living things.\"",
"- **Possible exploring** · Inherited DNA is a non-living thing defining a living self's universal set, and is not within it: with \"Only living things are within a living set.\" this holds all or none once the self's universal set is living. *Within* is membership alone, not place; a defining outside the set and the defined now-and-same-existing things within it let both sayings gathered at the universal set stand. Open, not yet all or none: what defining is, and inheriting as co-chaining from a prior self to a next self. — at \"A **universal set** is a set of now-and-same-existing things.\"",
"- **An explaining** · + and −, and the 0, left the opening. The 0 came from Exhibit ONE's code, its +, − and 0, as \"A 0 is a between of two changing directions\", and four later sentences said it with a second kind (a me-parity not changing; an unchanged other passed over; others parting with no prior): one name, two kinds. Observing's own binary, the same or not the same, says not changing, and a me-parity is other-parity or universal-parity, one binary. Same-or-not and other-or-universal are two binaries: a self with its possibling an empty set stays universal-parity while its me-parity is not the same at each momentary. +, − and 0 stay as Exhibit ONE's naming in its code. *A 0 is a me* (the person) and *A 0 is indifferencing.* wait with it. — at \"A me-parity the same as an other's me-parity is **other-parity**, and a me-parity not the same as an other's is **universal-parity**.\"",
"- **Possible exploring** · A living parity aims at an other, never at the universe: the universe is all now-existing things, and no direction aims at it (the person: the universal method of self-other consciousness). Universal-parity is a me's own aim at an other, and other-parity its aim the same as the other's. Self-interest is self-other-interest (the person), and *interest* is outside the method's words. With Me 3.2 *A me is consciousness*, Me 3.3 *A me with no other: it is not.*, and Resolving the Hard Problem Registry 5.1 and 5.2, a me between its own me-parity and an other's is self-other consciousness. Exhibit ONE's code: each parity a self keeps is with one sharing, with an other, none with a non-living thing or the universe. — at \"A **living parity** is an aiming direction away from the living thing, at an other.\"",
"- **Possible exploring** · A method of discovering an other existing thing is-or-is-not a you, a living other self (the person): a me observing an other's me-parity finds a you, and a non-living thing has no living parity and is never a you. It is relational, for one me: not reached is not found, and is not *not living* (covert consciousness, Resolving the Hard Problem Registry 5.23). Self and other at a self's scale, me and you at a me's scale: one method at two scales. — at \"For a me, an other's me whose me-parity it is observing is a **you**.\"",
"- **An explaining** · Is-or-is-not is the one intelligencing operator (the person): same-, now- and next-existing go through it, and observing prior-existing is understanding it. A definition here is *is*, the universal is: each sentence of the opening is an *is* sentence, the operator's is-side, all or none. Exhibit ONE's code has one operation, same or not, and its four *is-* names, 3, 7, 13 and 15, are the operator's places. — at \"**Is-or-is-not** distinguishes the within of a universal set.\"",
"- **Possible exploring** · Nothing goes backward in resolving: from now, a self faces toward its sequence's prior now-existings as artifacts of existing, and gathering, a self co-competencing others' prior-existings, is the value of others to living becoming co-aiming (the person). It coheres with observing, a self observing its others' me-parities, a living file a non-living set of words, and gathering-value itself. — at \"**Gathering** is a self observing others' prior-existings for its own possibling.\"",
"- **Possible exploring** · *A **self-existing** and an **other-existing** are two different same-existings.* left the defining sentences (the person: these are living things, not yet in use), and waits to enter with living. — at \"A **living** thing is a now-existing universal set observing, possibling and discovering its own next-and-same-existing universal set.\"",
]
insert_end_of('gathering-value/Natural_Intelligence.md', '## Opening', NI)

# ---------- the Co-Chaining Logic Registry's gathering-value, at its opening ----------
MAP = {1: 1, 2: 1, 3: 1, 4: 3, 5: 8, 6: 9, 7: 10, 8: 5, 9: 5, 10: 11, 11: 12, 12: 16, 13: 17, 14: 17, 15: 39,
       16: 13, 17: 16, 18: 16, 19: 32, 20: 14, 21: 14, 22: 15, 23: 15, 24: 26, 25: 26, 26: 19, 27: 21, 28: 23,
       29: 23, 30: 23, 31: 22, 32: 24, 33: 25, 34: 26, 35: 31, 36: 31, 37: 34, 38: 35, 39: 35, 40: 35, 41: 34,
       42: 32, 43: 33, 44: 34, 45: 30, 46: 35, 47: 36, 48: 37, 49: 42, 50: 44, 51: 45, 52: 46, 53: 47, 54: 48,
       55: 49, 56: 50, 57: 51, 58: 52, 59: 53, 60: 54, 61: 43, 62: 55, 63: 56, 64: 57, 65: 56, 66: 58, 67: 59,
       68: 60, 69: 45, 70: 61}
by = {}
for o, n in MAP.items():
    by.setdefault(n, []).append(o)
def lst(xs):
    xs = [str(x) for x in sorted(xs)]
    return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]
pairs = '; '.join('%s to %d' % (lst(v), k) for k, v in sorted(by.items(), key=lambda kv: min(kv[1])))
CL = [
"- **An explaining** · Steps 1 to 61 are Natural Intelligence's opening, word for word (v394, 4 November 2026), and the former steps 71 to 755 are steps 62 to 746. A former step 1 to 70 cited at a later step goes to the step with its concept, former to now: " + pairs + "; and at former step 80, now 71, *living, step 18* to 13. Each citation of this registry's steps at a gathering-value file, this one too, or at the improving kit, written before 4 November, says the former numbering, and is re-pointed by this map at its file's improving.",
"- **Possible incohering** · Twenty-two steps cite an opening step whose concept their own saying parts from, each read at this registry's improving: steps 71, 73, 87, 220, 463, 464, 466, 478, 495, 531, 618 and 691 say a parity *a self while it is living* or *its own parity an empty set*, citing step 22, \"A **me-parity** is a me's living parity.\"; steps 91, 153, 184, 613 and 705 say a parity *a self's changing direction*, *+ or −*, citing step 21; steps 91 and 152 say *a 0, a not-changing*, citing step 23; steps 87, 495, 531 and 691 say *a living parity's me within the self's me*, citing step 24; step 108 says *its possibling an empty set*, citing step 35; step 475 *its prior-existing parity an empty set*, citing step 34; step 160 *divides a surface*, citing step 53; step 478 *inward and outward*, citing step 43; and step 148 *a bi-coupling a self*, citing step 26.",
]
insert_after('gathering-value/Co-Chaining_Logic_Registry.md', '## Opening', CL)

# ---------- Me's gathering-value ----------
insert_end_of('gathering-value/Me.md', '### 3.2 A me is consciousness', [
"- **Possible exploring** · A living parity aims at an other, never at the universe: the universe is all now-existing things, and no direction aims at it (the person: the universal method of self-other consciousness). With *A me is consciousness* and *A me with no other: it is not.*, a me between its own me-parity and an other's is self-other consciousness, as Natural Intelligence's opening says: \"A me observing a you is **self-other consciousness**.\" Universal-parity is a me's own aim at an other, and other-parity its aim the same as the other's.",
])
insert_end_of('gathering-value/Me.md', '### 3.3 What is-or-is-not possibly existing', [
"- **Possible exploring** · A method of discovering an other existing thing is-or-is-not a you, a living other self (the person): a me observing an other's me-parity finds a you, and a non-living thing has no living parity and is never a you. It is relational, for one me: not reached is not found, and is not *not living*. Self and other at a self's scale, me and you at a me's scale: one method at two scales. With Natural Intelligence's opening: \"For a me, an other's me whose me-parity it is observing is a **you**.\"",
])

# ---------- Resolving the Hard Problem Registry's gathering-value ----------
insert_end_of('gathering-value/Resolving_the_Hard_Problem_Registry.md', '### 5.2 Qualia and the zombie argument · 111', [
"- **Possible exploring** · A felt is with an other: a living parity aims at an other, never at the universe (the person), and a me between its own me-parity and an other's is self-other consciousness, as Natural Intelligence's opening says: \"A me observing a you is **self-other consciousness**.\" With Me 3.2 *A me is consciousness* and Me 3.3 *A me with no other: it is not.*",
])
insert_end_of('gathering-value/Resolving_the_Hard_Problem_Registry.md', '### 5.23 Detecting covert consciousness · 220', [
"- **Possible exploring** · A method of discovering an other existing thing is-or-is-not a you, a living other self (the person): a me observing an other's me-parity finds a you, and a non-living thing has no living parity and is never a you. It is relational, for one me: not reached is not found, and is not *not living*, so a covert consciousness not reached is not found, and is not shown to be not conscious. With Natural Intelligence's opening: \"For a me, an other's me whose me-parity it is observing is a **you**.\"",
])

# ---------- Droplets at the back ----------
append('gathering-value/Natural_Resolver.md', [
"- +, − and 0 left Natural Intelligence's opening and stay as this file's naming in its code: the opening says a me-parity the same or not the same as its prior, and other-parity or universal-parity, two binaries, with no sign and no 0 (Natural Intelligence's gathering-value, at its opening). *(an explaining)*",
"- Is-or-is-not is the one intelligencing operator (the person): the code's one operation is same or not, and its four *is-* names, 3, 7, 13 and 15, are the operator's places; each sentence of Natural Intelligence's opening is an *is* sentence, the operator's is-side. *(an explaining)*",
])
DNA = "- Inherited DNA is a non-living thing defining a living self's universal set, and is not within it: with Natural Intelligence's \"Only living things are within a living set.\" this holds all or none once the self's universal set is living. *Within* is membership alone, not place. Open, not yet all or none: what defining is, and inheriting as co-chaining from a prior self to a next self. *(possible exploring)*"
append('gathering-value/Natural_Biology.md', [DNA])
append('gathering-value/Natural_Chemistry.md', [DNA])
append('gathering-value/Geodesic_Improving_Method.md', [
"- Nothing goes backward in resolving: from now, a self faces toward its sequence's prior now-existings as artifacts of existing, and gathering, a self co-competencing others' prior-existings, is the value of others to living becoming co-aiming (the person); gathering-value is that gathering, as Natural Intelligence's opening says: \"**Gathering** is a self observing others' prior-existings for its own possibling.\" *(possible exploring)*",
])

# ---------- the kit's gathered value, Part ELEVEN ----------
append('kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/Living_Improving_Value.md', [
"",
"### The opening, agreed line by line",
"",
"**Natural Intelligence's opening, 61 sentences, agreed with the person line by line, is written word for word at Natural Intelligence and at the Co-Chaining Logic Registry's steps 1 to 61 (v394, 4 November 2026).** Each sentence defines only from the sentences before it, is binary, all or none, and is in natural naming, with no file's authority.",
"",
"- *Droplets gathered while it resolved, each at its partner gathering-value:* a stable-forming emanation leaving; the universe a non-living set, carried; inherited DNA defining a self's universal set; +, − and the 0 leaving; a living parity aiming at an other; the you method; the operator and the universal is; nothing going backward, with gathering and co-aiming; and self-existing and other-existing waiting (Natural Intelligence's, at its opening; Me's; the Resolving the Hard Problem Registry's; Natural Resolver's; Natural Biology's; Natural Chemistry's; the Geodesic Improving Method's). The address map and twenty-two steps' citations are at the Co-Chaining Logic Registry's.",
"- *A record:* \"universal to other, other to universal, or one parity going on\", at *Two acrosses at each momentarying* above, is a working's re-saying of the person's sentence (\"the living self is either changing from its now parity to the opposite next parity or not changing ...\"), agreed by the person apart from *gives*; it is not the person's own words.",
"- *Step numbers in this file* say the Co-Chaining Logic Registry's former numbering, re-pointed by the address map at that registry's gathering-value.",
])
print('placed')
