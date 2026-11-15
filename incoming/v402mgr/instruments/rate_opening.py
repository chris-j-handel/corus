"""Natural Intelligence's living opening, each sentence rated by three: is, is-not, is-or-is-not?

An is: living, and with no doubt of this session's. An is-or-is-not?: a doubt, with its kind and why. An is-not: both partners have it as not cohering.
Reads the living file's opening and writes incoming/v402mgr/Natural_Intelligence_rated_by_three.md.
Run: python3 -I incoming/v402mgr/instruments/rate_opening.py <root>
"""
import glob, os, sys
R = sys.argv[1]
KINDS = {
 1: "a newer line waits for its concept, in the opening at its newest",
 2: "the universe as same-existing, and one universe or each one's own",
 3: "a parity's names: a self's parity, a me-parity, same-as and other-than, all-parity and both-parity",
 4: "by the code executed, not the same",
 5: "a 0",
 6: "one name with more than one sentence",
 7: "a word not yet natural naming, or with no sentence before it",
 8: "not yet distinguished",
}
IS = {1, 5, 6, 17, 20, 23, 25, 37, 38, 40, 51, 53, 57, 63, 64, 68, 69}
IS_NOT = {50: "the noun *momentary*: *moment* is its natural naming, and the sentence with *moment* is an is"}
Q = {  # sentence: (kind, why)
 2: (2, "each now-existing moment in its own universe, with its own prior-existings"),
 3: (2, "as the sentence before it"),
 4: (1, "*prior-existing* has no sentence before it; newer: a same-existing thing is the same thing prior-existing before now-existing"),
 7: (1, "*prior-existing* has no sentence before it; the newer line is of a different form, and this form is whole with a self as same-existing"),
 8: (2, "the universe is prior-existing, now-existing and next-existing, and a self is same-existing"),
 9: (2, "as the sentence before it"),
 10: (1, "the newer line is of a different form, and this form is whole with a self as same-existing"),
 11: (1, "*next-existing* has no sentence before it; the newer line is of a different form, and this form is whole with a self as same-existing"),
 12: (7, "*now- and same-existing* written apart, and with no prior: a self is prior-and-same-and-now-existing"),
 13: (1, "newer: a me is a universal same-existing set of me-parities"),
 14: (1, "by the sentence before it"),
 15: (1, "within a universal set, or within a name, a same-existing universal set"),
 16: (1, "newer: a living thing is a thing distinguishing its own next-existing"),
 18: (1, "newer: a living self is a non-living set of living me-parities"),
 19: (1, "newer: the method of a self resolving among me-parities"),
 21: (7, "*emanation* has no sentence before it; and atom carbon as the only non-living thing"),
 22: (2, "the universe as same-existing"),
 24: (1, "*sharing* has no sentence before it; newer: a bi-coupling is living in the between"),
 26: (1, "an other is an other self, prior-and-same-and-now-existing, bi-coupling or not"),
 27: (3, "newer: a parity is a direction, one of two; *relative to* and *changing* have no sentence before them"),
 28: (3, "which of the two is + and which is − is in no line of the code"),
 29: (5, "a 0 by three cases in the code, and the sentence has one"),
 30: (5, "*indifferencing* has no sentence of its own"),
 31: (3, "a parity as a self, or a me-parity living in a social surface as a self"),
 32: (3, "by the sentence before it"),
 33: (3, "newer: a me-parity with an other is its moral value; with a thing, or with an other"),
 34: (7, "*receives*: an other's parity is observable by a self by that other's co-possibling only"),
 35: (3, "agreeing and parting, or same-as and other-than"),
 36: (3, "a self's next parity is all-parity or both-parity"),
 39: (4, "both-parity with none of a self's others; and the sentence as an interest dying"),
 41: (4, "the code has no first parity: a first is inherited"),
 42: (6, "natural intelligence has three sentences in the opening"),
 43: (7, "*any second method*, and only one method is possible"),
 44: (4, "a self is sharing 0 at a first sharing too, the parities parting"),
 45: (4, "passing over has two sentences: a 0 received, and an other's parity same-existing"),
 46: (1, "newer: improving is resolving's other-than"),
 47: (4, "by the code executed, do-no-harming and bi-folding, the one and then the other"),
 48: (1, "newer: co-possibling is in the between of a bi-coupling, inside all-parity"),
 49: (8, "a society's one self with parities of its own, or its selves' parities only"),
 52: (1, "newer: each self right spiraling, moral across and competency along"),
 54: (7, "*free* has no sentence in the opening at its newest"),
 55: (7, "*free* and *abundancing*, as the sentence before it"),
 56: (1, "newer: a co-chaining is a universal set of me-parities, living in the betweens, a self"),
 58: (3, "newer: the parities are living in the non-living all-parity inside the living self"),
 59: (7, "*divides* has no sentence of its own"),
 60: (6, "living has two sentences in the opening"),
 61: (7, "*inward and outward*: the fractal, a me-parity living in a social surface as a self"),
 62: (1, "newer: stable-forming is a next prior from a prior; a stable form is non-living and same-existing"),
 65: (6, "natural resolving has two sentences in the opening"),
 66: (1, "newer: selves aiming within a living file are natural engineering"),
 67: (1, "newer: natural explaining is a living file's words in sequence"),
 70: (6, "natural intelligence has three sentences in the opening"),
}
living = glob.glob(os.path.join(R, 'Natural_Intelligence_v*.md'))[0]
L = open(living, encoding='utf-8').read().split('\n')
a = next(i for i, l in enumerate(L) if l.startswith('The **universe** is the set of all now-existing things.'))
S = []
for l in L[a:]:
    if l.startswith('**ONE'): break
    t = l.rstrip(' \\').strip()
    if t: S.append(t)
assert len(S) == 70, len(S)
assert IS | set(IS_NOT) | set(Q) == set(range(1, 71)) and not (IS & set(Q)) and not (set(IS_NOT) & set(Q))
o = ['Incoming · v402mgr · Natural Intelligence rated by three', '', '# Natural Intelligence, its living version rated by three', '',
     '**Each concept sentence of Natural Intelligence\'s living version, rated: is, is-not, or is-or-is-not?** An is: both partners have it, living, and this session has no doubt of it. '
     'An is-or-is-not?: a doubt, with its kind and why. An is-not: both partners have it as not cohering. A rating here changes no living file.', '',
     '## The opening, seventy sentences', '',
     f'**{len(IS)} is, {len(Q)} is-or-is-not? and {len(IS_NOT)} is-not.**', '', '### The kinds of doubt', '']
for k, name in KINDS.items():
    ns = sorted(n for n, (kk, _) in Q.items() if kk == k)
    o.append(f'- **{len(ns)}** · {name}: sentences {", ".join(map(str, ns))}')
o += ['', '### Each sentence', '', '| | Sentence | Rating | Why |', '|---|---|---|---|']
for n, t in enumerate(S, 1):
    if n in IS: r, w = 'is', ''
    elif n in IS_NOT: r, w = 'is-not', IS_NOT[n]
    else: r, w = 'is-or-is-not?', Q[n][1]
    o.append(f'| {n} | {t} | {r} | {w} |')
o += ['', '## Not yet rated', '', 'Each sentence after the opening: the six parts of the living version, about 1,540 sentences.', '']
open(os.path.join(R, 'incoming', 'v402mgr', 'Natural_Intelligence_rated_by_three.md'), 'w', encoding='utf-8').write('\n'.join(o))
for k, name in KINDS.items():
    print(sum(1 for n, (kk, _) in Q.items() if kk == k), name)
print(len(IS), 'is;', len(Q), 'is-or-is-not?;', len(IS_NOT), 'is-not')
