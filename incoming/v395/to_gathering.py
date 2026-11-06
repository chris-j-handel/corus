"""Living files back to main's; the opening, 1.1 and 1.2 and the Co-Chaining Logic Registry's renumbering waiting at gathering-value.
Run at the repository root after the living files are restored from main."""
import re, os
SP = os.path.dirname(os.path.abspath(__file__))

def rep(p, pairs, count=1):
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        n = t.count(a)
        assert (n == count if count else n >= 1), (p, a[:60], n)
        t = t.replace(a, b)
    open(p, 'w', encoding='utf-8').write(t)

OP = [l.rstrip('\n') for l in open(os.path.join(SP, 'opening_path44.txt'), encoding='utf-8') if l.strip()]
assert len(OP) == 61
best = open(os.path.join(SP, 'ni_11_12_best.md'), encoding='utf-8').read().strip()
b11, b12 = best.split('\n\n## 1.2 Prior, now and next\n\n')
b11 = b11.strip(); b12 = b12.strip()

# ---------- Natural Intelligence's gathering-value ----------
g = 'gathering-value/Natural_Intelligence.md'
G = open(g, encoding='utf-8').read()
main_11_12 = open(os.path.join(SP, 'gv_ni_11_12_main.md'), encoding='utf-8').read().rstrip('\n')
m = re.search(r'^### 1\.1 .*?(?=^### 1\.3 )', G, re.S | re.M)
WAIT = ' Both partners agreeing, it enters the living file at its own motion.'
s11 = ("- **Waiting to enter** · 1.1's best version, the person's concepts within it (now the universal set of all now-existing moments; the now-existing moments within all bi-couplings within it; the now-existing universe tri-bi-co-momentarying), its title *Now, one universal set of moments*." + WAIT + " The two paragraphs: " + ' / '.join(p.strip() for p in b11.split('\n\n')))
s12 = ("- **Waiting to enter** · 1.2's best version, the person's concept within it (each prior-existing thing and each non-living now-existing thing from prior living)." + WAIT + " The two paragraphs: " + ' / '.join(p.strip() for p in b12.split('\n\n')))
sec = main_11_12.split('\n### 1.2 ')
new_11_12 = sec[0].rstrip('\n') + '\n' + s11 + '\n\n### 1.2 ' + sec[1].rstrip('\n') + '\n' + s12 + '\n\n'
G = G[:m.start()] + new_11_12 + G[m.end():]
a = ("is word for word the Co-Chaining Logic Registry's steps 1 to 61 (v395, 4 November 2026). The former opening of 70 sentences is Natural Intelligence v391's.")
b = ("is agreed with the person (v395, 4 and 5 November 2026) and waits here to enter Natural Intelligence's opening and, word for word, the Co-Chaining Logic Registry's steps 1 to 61." + WAIT + " The opening in the living file is the former 70 sentences.")
assert G.count(a) == 1; G = G.replace(a, b)
L = G.split('\n')
i = L.index('## Opening'); j = i + 1
while not L[j].startswith('## '): j += 1
k = j
while L[k - 1].strip() == '': k -= 1
paras = [(1, 20), (21, 31), (32, 43), (44, 61)]
L[k:k] = ["- **Waiting to enter** · The opening, 61 sentences, agreed with the person, in four paragraphs, sentences 1 to 20, 21 to 31, 32 to 43 and 44 to 61; its sentence 55 waiting for its saying with *stable-forming*." + WAIT + " " + ' '.join('%d. %s' % (n + 1, s) for n, s in enumerate(OP))]
G = '\n'.join(L)
G = G.replace('and its two places at 1.2 are read,', "and its two places at 1.2 are read at 1.2's best version, waiting below,")
open(g, 'w', encoding='utf-8').write(G)

# ---------- the Co-Chaining Logic Registry's gathering-value ----------
rep('gathering-value/Co-Chaining_Logic_Registry.md', [
    ("- **An explaining** · Steps 1 to 61 are Natural Intelligence's opening, word for word (v395, 4 November 2026: momentary dissolved, a moment's sequence and momentarying at steps 8 and 9), and the former steps 71 to 755 are steps 62 to 746.",
     "- **Waiting to enter** · With Natural Intelligence's opening, agreed with the person and waiting at its gathering-value (v395, 4 and 5 November 2026: momentary dissolved, a moment's sequence and momentarying at steps 8 and 9), steps 1 to 61 are that opening word for word, each with an *Adding* line naming in the step's own words the concept it adds, each group's *Entering* line its *Adding* lines joined, the groups 1 to 20, 21 to 31, 32 to 43 and 44 to 61; and the steps 71 to 755 are steps 62 to 746." + WAIT),
    ("- **Possible incohering** · Twenty-six steps cite an opening step whose concept their own saying parts from,",
     "- **Possible incohering** · With the opening entered, step numbers as the map above gives them, twenty-six steps cite an opening step whose concept their own saying parts from,"),
])

# ---------- droplets saying the opening, 1.1 or 1.2 as in the living file ----------
import glob
for p in glob.glob('gathering-value/*.md'):
    t = open(p, encoding='utf-8').read(); t0 = t
    t = t.replace("(the person): one concept has one name. Natural Intelligence's opening says \"A **moment**",
                  "(the person): one concept has one name. Natural Intelligence's opening, agreed with the person and waiting at its gathering-value to enter, says \"A **moment**")
    t = t.replace("and its 1.1 \"**Now is the universal set of all now-existing moments**",
                  "and its 1.1's best version, waiting with it, \"**Now is the universal set of all now-existing moments**")
    t = t.replace("(the person), at Natural Intelligence 1.2: \"**Each prior-existing thing",
                  "(the person), at Natural Intelligence 1.2's best version, waiting at its gathering-value: \"**Each prior-existing thing")
    t = t.replace("as Natural Intelligence's opening says: \"A me observing a you is **self-other consciousness**.\"",
                  "as Natural Intelligence's opening, agreed and waiting at its gathering-value, says: \"A me observing a you is **self-other consciousness**.\"")
    t = t.replace("With Natural Intelligence's opening: \"For a me, an other's me",
                  "With Natural Intelligence's opening, agreed and waiting at its gathering-value: \"For a me, an other's me")
    t = t.replace("as Natural Intelligence's opening says: \"**Gathering** is",
                  "as Natural Intelligence's opening, agreed and waiting at its gathering-value, says: \"**Gathering** is")
    if t != t0: open(p, 'w', encoding='utf-8').write(t)

# ---------- Equilibria Registry and Natural Numbers: their citations wait with the renumbering ----------
def append(p, line):
    t = open(p, encoding='utf-8').read().rstrip('\n'); open(p, 'w', encoding='utf-8').write(t + '\n' + line + '\n')
append('gathering-value/Equilibria_Registry.md',
       "- **Waiting to enter** · With the Co-Chaining Logic Registry's steps 71 to 755 becoming 62 to 746 as Natural Intelligence's opening enters (its gathering-value's address map), each citation here of its steps re-points by 9 less: 584 to 575, 692 to 683, 104 to 95, 167 to 158, 510 and 518 to 501 and 509, 621 to 612, 484 to 475, 197 to 188, 199 to 190, 479 to 470, 142 to 133. *Living is from living, step 444* points at a step about a resolving with a bi-coupling; the step saying living from living is 485, and 476 after the renumbering." + WAIT + " *(an explaining)*")
append('gathering-value/Natural_Numbers.md',
       "- **Waiting to enter** · With the Co-Chaining Logic Registry's steps 71 to 755 becoming 62 to 746 as Natural Intelligence's opening enters (its gathering-value's address map), the citations here of its steps 740 to 742 and 746 to 751 re-point to 731 to 733 and 737 to 742." + WAIT + " *(an explaining)*")

# ---------- the kit's gathered value ----------
rep('kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/Living_Improving_Value.md', [
    ("is written word for word at Natural Intelligence and at the Co-Chaining Logic Registry's steps 1 to 61 (v395, 4 November 2026).**",
     "is agreed, and waits at Natural Intelligence's gathering-value to enter Natural Intelligence and, word for word, the Co-Chaining Logic Registry's steps 1 to 61 (v395, 4 and 5 November 2026), both partners agreeing at its entering.**"),
])
V = 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/Living_Improving_Value.md'
t = open(V, encoding='utf-8').read().rstrip('\n')
t += ("\n- *Living files change only with both partners agreeing, through gathering-value (the person, 5 November):* a change to a living file goes in through the gathering file method, never by a side method. The opening, 1.1 and 1.2 and the Co-Chaining Logic Registry's renumbering, first written into the living files, are back at main's living files and wait at their gathering-values to enter.\n")
open(V, 'w', encoding='utf-8').write(t)
print('done')
