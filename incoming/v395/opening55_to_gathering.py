"""The opening of 55 sentences, agreed, into its waiting places at gathering-value; quotes of changed sentences re-said. Run at repo root."""
import re, os, glob
SP = os.path.dirname(os.path.abspath(__file__))
OP = [l.rstrip('\n') for l in open(os.path.join(SP, 'opening_path47.txt'), encoding='utf-8') if l.strip()]
OLD = [l.rstrip('\n') for l in open(os.path.join(SP, 'opening_path44.txt'), encoding='utf-8') if l.strip()]
assert len(OP) == 55 and len(OLD) == 61
PARAS = [(1, 19), (20, 30), (31, 39), (40, 55)]
WAIT = ' Both partners agreeing, it enters the living file at its own motion.'

def rep(p, pairs):
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        assert t.count(a) == 1, (p, a[:70], t.count(a))
        t = t.replace(a, b)
    open(p, 'w', encoding='utf-8').write(t)

# ---- path44 (61) -> path47 (55)
H = {}
seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,33,34,34,35,36,37,37,38,39,40,41,42,43,43,43,44,45,45,46,47,48,50,51,52,53,54,55]
# path44 index: 1..61 (line 55 stable form -> 48, 56 natural resolving -> 50)
assert len(seq) == 61
H = {i + 1: v for i, v in enumerate(seq)}
# former v391 -> path41 (first write) -> path44 (g) -> path47 (H)
MAP = {1: 1, 2: 1, 3: 1, 4: 3, 5: 8, 6: 9, 7: 10, 8: 5, 9: 5, 10: 11, 11: 12, 12: 16, 13: 17, 14: 17, 15: 38,
       16: 39, 17: 16, 18: 16, 19: 32, 20: 14, 21: 14, 22: 15, 23: 15, 24: 26, 25: 26, 26: 19, 27: 21, 28: 23,
       29: 23, 30: 23, 31: 22, 32: 24, 33: 25, 34: 26, 35: 31, 36: 31, 37: 34, 38: 35, 39: 35, 40: 35, 41: 31,
       42: 32, 43: 33, 44: 34, 45: 30, 46: 35, 47: 36, 48: 37, 49: 42, 50: 44, 51: 45, 52: 46, 53: 47, 54: 48,
       55: 49, 56: 50, 57: 51, 58: 52, 59: 53, 60: 53, 61: 43, 62: 55, 63: 56, 64: 57, 65: 56, 66: 58, 67: 59,
       68: 60, 69: 45, 70: 61}
def g(n):
    if n <= 7: return n
    if n <= 43: return n + 2
    if n == 44: return 9
    if n == 45: return 8
    return n
F = {o: H[g(t)] for o, t in MAP.items()}
by = {}
for o, n in F.items(): by.setdefault(n, []).append(o)
lst = lambda xs: (lambda s: s[0] if len(s) == 1 else ', '.join(s[:-1]) + ' and ' + s[-1])([str(x) for x in sorted(xs)])
pairs = '; '.join('%s to %d' % (lst(v), k) for k, v in sorted(by.items(), key=lambda kv: min(kv[1])))

# ---- Natural Intelligence's gathering-value: the waiting opening
g_ni = 'gathering-value/Natural_Intelligence.md'
t = open(g_ni, encoding='utf-8').read()
m = re.search(r"^- \*\*Waiting to enter\*\* · The opening, 61 sentences, agreed with the person,[^\n]*$", t, re.M)
assert m
t = t[:m.start()] + ("- **Waiting to enter** · The opening, 55 sentences, agreed with the person (v395, 4 and 5 November 2026), no word staying unless the logic stays living only with it (the person), in four paragraphs, sentences 1 to 19, 20 to 30, 31 to 39 and 40 to 55." + WAIT + " " + ' '.join('%d. %s' % (n + 1, s) for n, s in enumerate(OP))) + t[m.end():]
open(g_ni, 'w', encoding='utf-8').write(t)
rep(g_ni, [
    ("- **An explaining** · The opening, 61 sentences, each defining only from the sentences before it,",
     "- **An explaining** · The opening, 55 sentences, each defining only from the sentences before it,"),
    ("Co-Chaining Logic Registry's steps 1 to 61. Both partners agreeing,", "Co-Chaining Logic Registry's steps 1 to 55. Both partners agreeing,"),
    ("The opening says \"A form same-existing from moment to moment is a **stable form**.\", waiting for its saying with *stable-forming*;",
     "The opening now says \"**Stable-forming** is observing, possibling, discovering and same-existing together.\" and \"A self is momentarying and stable-forming.\" (the person: stable-forming the four together, Exhibit ONE's stable-forming bi-folding method);"),
    ("— at \"A form same-existing from moment to moment is a **stable form**.\"", "— at \"**Stable-forming** is observing, possibling, discovering and same-existing together.\""),
])

# ---- quotes of changed opening sentences, re-said across gathering-value and the kit's value
QUOTE = {
    OLD[0]: OP[0], OLD[4]: OP[4], OLD[5]: OP[5], OLD[6]: OP[6], OLD[8]: OP[8], OLD[9]: OP[9], OLD[11]: OP[11],
    OLD[12]: OP[12], OLD[13]: OP[13], OLD[14]: OP[14], OLD[21]: OP[20], OLD[22]: OP[21], OLD[24]: OP[23],
    OLD[26]: OP[25], OLD[31]: OP[30], OLD[33]: OP[32],
}
files = glob.glob('gathering-value/*.md') + ['kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/Living_Improving_Value.md']
n = 0
for p in files:
    s = open(p, encoding='utf-8').read(); s0 = s
    for a, b in QUOTE.items():
        if a != b: s = s.replace(a, b)
    s = s.replace('"The universe is a non-living same-existing set." is outside the opening, carried by two sentences together, all or none. — at "Only living things are within a living set." with "Within the universe are living and non-living things."',
                  '"The universe is a non-living same-existing set." is outside the opening, carried by sentences together, all or none. — at "Only living things are within a living set." with "The **universe** is the set of now-existing things." and "Living and **non-living** are one binary of a now-existing thing."')
    s = s.replace("(the person's sentence); and the now-existing universe is tri-bi-co-momentarying",
                  "(the person's sentence, *now-existing and* and *sequential* since leaving it, the logic living without them); and the now-existing universe is tri-bi-co-momentarying")
    if s != s0: open(p, 'w', encoding='utf-8').write(s); n += 1
print('files with quotes re-said:', n)

# ---- the Co-Chaining Logic Registry's gathering-value
cl = 'gathering-value/Co-Chaining_Logic_Registry.md'
L = open(cl, encoding='utf-8').read().split('\n')
i = next(k for k, l in enumerate(L) if l.startswith("- **Waiting to enter** · With Natural Intelligence's opening, agreed with the person and waiting at its gathering-value"))
L[i] = ("- **Waiting to enter** · With Natural Intelligence's opening, agreed with the person and waiting at its gathering-value (v395, 4 and 5 November 2026), steps 1 to 55 are that opening word for word, each with an *Adding* line naming in the step's own words the concept it adds, each group's *Entering* line its *Adding* lines joined, the groups 1 to 19, 20 to 30, 31 to 39 and 40 to 55; and the steps 71 to 755 are steps 56 to 740, 15 less. A former step 1 to 70 cited at a later step goes to the step with its concept, former to now: " + pairs +
        ". A citing sentence naming another concept of the former step goes to the step with that concept: at former step 80, *living, step 18*, to 15; at former steps 117 and 504, *each self living with others, step 15*, to 37; and at former step 504, *a self living, step 31*, to 17. Each citation of this registry's steps at a gathering-value file, this one too, or at the improving kit, written before 4 November, says the former numbering, and is re-pointed by this map at its file's improving." + WAIT)
inc = L[i + 1]; assert inc.startswith('- **Possible incohering** · With the opening entered, step numbers as the map above gives them, twenty-six steps')
def conv(m):
    nums = m.group(2)
    def one(d):
        x = int(d.group(0))
        return str(x + 9) if x > 61 else str(H[x])
    return m.group(1) + ' ' + re.sub(r'\d+', one, nums)
inc = re.sub(r'\b(steps?) (\d+(?:(?:, | and )\d+)*)', conv, inc)
inc = inc.replace('With the opening entered, step numbers as the map above gives them, twenty-six steps cite an opening step',
                  'Twenty-six steps, numbered as the living registry now numbers them, cite a former opening step, its concept now at the waiting opening\'s step named,')
L[i + 1] = inc
open(cl, 'w', encoding='utf-8').write('\n'.join(L))

# ---- the Equilibria Registry's and Natural Numbers' waiting citations
rep('gathering-value/Equilibria_Registry.md', [(
    "With the Co-Chaining Logic Registry's steps 71 to 755 becoming 62 to 746 as Natural Intelligence's opening enters (its gathering-value's address map), each citation here of its steps re-points by 9 less: 584 to 575, 692 to 683, 104 to 95, 167 to 158, 510 and 518 to 501 and 509, 621 to 612, 484 to 475, 197 to 188, 199 to 190, 479 to 470, 142 to 133. *Living is from living, step 444* points at a step about a resolving with a bi-coupling; the step saying living from living is 485, and 476 after the renumbering.",
    "With the Co-Chaining Logic Registry's steps 71 to 755 becoming 56 to 740 as Natural Intelligence's opening of 55 sentences enters (its gathering-value's address map), each citation here of its steps re-points by 15 less: 584 to 569, 692 to 677, 104 to 89, 167 to 152, 510 and 518 to 495 and 503, 621 to 606, 484 to 469, 197 to 182, 199 to 184, 479 to 464, 142 to 127. *Living is from living, step 444* points at a step about a resolving with a bi-coupling; the step saying living from living is 485, and 470 after the renumbering.")])
rep('gathering-value/Natural_Numbers.md', [(
    "With the Co-Chaining Logic Registry's steps 71 to 755 becoming 62 to 746 as Natural Intelligence's opening enters (its gathering-value's address map), the citations here of its steps 740 to 742 and 746 to 751 re-point to 731 to 733 and 737 to 742.",
    "With the Co-Chaining Logic Registry's steps 71 to 755 becoming 56 to 740 as Natural Intelligence's opening of 55 sentences enters (its gathering-value's address map), the citations here of its steps 740 to 742 and 746 to 751 re-point to 725 to 727 and 731 to 736.")])

# ---- the kit
V = 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/Living_Improving_Value.md'
rep(V, [("Natural Intelligence's opening, 61 sentences, agreed with the person line by line, is agreed, and waits at Natural Intelligence's gathering-value to enter Natural Intelligence and, word for word, the Co-Chaining Logic Registry's steps 1 to 61",
         "Natural Intelligence's opening, 55 sentences, agreed with the person line by line, is agreed, and waits at Natural Intelligence's gathering-value to enter Natural Intelligence and, word for word, the Co-Chaining Logic Registry's steps 1 to 55")])
s = open(V, encoding='utf-8').read().rstrip('\n')
s += ("\n- *No word stays unless the logic stays living only with it (the person, 5 November):* applied to each sentence of the opening, 62 sentences to 55. *Free* dissolves, its meaning, no one paying money, outside the logic; *social abundancing* dissolves, a natural intelligence network with nothing beyond it; *a second method* leaves, saying again natural intelligence's resolving; do-no-harming and improving are resolving's is and is-not. *Stable-forming* is observing, possibling, discovering and same-existing together, Exhibit ONE's stable-forming bi-folding method, and a self is momentarying and stable-forming (the person): momentarying the sequential along, stable-forming the geometric across with it, the competency neither physics' state-flow-state nor chemistry's flow-state-flow accounting has discovered (the person).\n")
open(V, 'w', encoding='utf-8').write(s)
P = 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/Living_Improving_Plan.md'
t = open(P, encoding='utf-8').read()
t = t.replace("Its 61 sentences each define only from the sentences before it", "Its 55 sentences each define only from the sentences before it")
t = t.replace("A session gathering it for its own possibling is co-aiming (its lines 42 and 43)", "A session gathering it for its own possibling is co-aiming (its sentences 38 and 39)")
open(P, 'w', encoding='utf-8').write(t)
print('ok')
