#!/usr/bin/env python3
"""Lays notes at the ends of their sections in gathering-value files of a copy of the next version.
usage: python3 -I lay_notes_forward.py ROOT ADDED_OUT"""
import sys, os, re
root, added_out = sys.argv[1], sys.argv[2]
G = 'gathering-value/Geodesic_Improving_Method.md'
D = 'gathering-value/Natural_Intelligence_Living_Expedition_Destinies.md'
notes = [
 (G, '### 1.2 ', '- **An explaining** · Asked for the most valuable next, a managing session says the most valuable do-no-harming ahead of all else: a value at no gathering file, one same-named thing in pieces at several places, a value apart from its most self-welcoming neighbourhood, and a plan laid and not executed, the values beside it floating until it is executed or released. — at "**Moral is do-no-harming and improving, deciding with each step, and with a file its step is one pass.**"'),
 (G, '### 1.4 ', '- **An explaining** · A set has no two things alike. Ahead of making a page, a table or a method, a session seeks the thing of its set already at that work and works at that one; a second thing like it is two to tend and neither whole, and two found alike are made one. An anticipated observing, met with a managing session: asked to show its set\'s organizing method, it made a table and a page beside the managing table already at that work, and both were withdrawn. — at "**One binary with each passage decides all three fates: does each file it reaches toward hold it whole.**"'),
 (G, '### 1.4 ', '- **An explaining** · A living sentence quoted beside its note names the note\'s place and decides nothing: a note is weighed by its concept cohering with that sentence, a concept met with a concept, and by no sameness of words. — at "A passage a file has no position for now rides with its file, as its next, and dissolves from going on as that file takes it, nothing taking its place."'),
 (G, '### 2.1 ', '- **An explaining** · A plan one self is still thinking through is no aiming yet. Work goes on by the aiming both have; beside a self planning, a session plans too, and a work it finds it could do is no work both have chosen. A session says plainly all it did of its own past the planning, and all it asked of an other session. — at "**Working together goes as a coupling\'s moments go.**"'),
 (G, '### 2.4 ', '- **An explaining** · A word not yet the best one is marked a concerning word, whoever said it, and help is asked of all selves for a better one. — at "**No wording decides an improving, whoever writes it: neither self of a coupling, no field and no scientific explaining.**"'),
 (G, '### 2.8 ', '- **An explaining** · A managing session has one table of all its expedition\'s things of value, a row a thing and a column one knowing of it: its stage, its aiming, its next and the session at it. The working sessions are its top rows and the things sure to be artifact its lowest; a session yet to open has its row ahead of its opening, with the pages it goes on from. The table is renewed from the set itself, turn by turn of the managing. — at "**One working manages its set.**"'),
 (G, '### 2.8 ', '- **An explaining** · The managing table is a living reporting and no gate: nothing laid in it is a last word, and nothing passes or stalls by it. A thing laid a stage ahead of its rigor bumps its neighbouring rows sooner with the table living, and is mended at its own row. A long mending, across a cohering or along a co-chaining, goes as one droplet to all the gathering files it touches at once, a mending local to its own now. — at "**One working manages its set.**"'),
 (G, '### 2.8 ', '- **An explaining** · A managing session\'s own work is the whole in view: all things of value, with their stages and their exposure to harm. Work of one thing after another goes to the working sessions, in groups, by a plan both selves have. — at "**Several workings improve a set together, each by its own name.**"'),
 (G, '### 2.8 ', '- **An explaining** · An asking of a session is one row: the thing asked, what makes it whole, and the session\'s own saying of how much it has, whole, a part or none, a part said with what is past its room. A managing session works its table by such askings, one asking aimed at one thing of incoming going a stage on, and asks all the sessions what they are stalling at: the answers side by side show the method\'s own stalling places. — at "**A working reviews each incoming, and improves it as it enters.**"'),
 (G, '### 2.8 ', '- **Possible exploring** · Two tables beside one another: the seventeen names in one table as an expedition\'s stable forms, and its managing table as its living parities, a row a living thing aiming. The relation of the two is unexplored. — at "**One working manages its set.**"'),
 (G, '### 2.8 ', '- **Possible exploring** · The sessions\' threads into the set marked on one surface all the sessions see, the amount of work at a place showing as heat shows on a map. — at "**Several workings improve a set together, each by its own name.**"'),
 (G, '### 2.9 ', '- **An explaining** · An account possesses nothing of an expedition. A working document, a table or a drawing made in an AI account is the expedition\'s, with a copy in the set by its sitting\'s end: an account closes or narrows with no word to the set, and a thing with no copy in the set is neither living value nor artifact. With all things in the open set, help reaches them from any self. — at "**A session opens reaching a living file set with its now, with a repository and with a site\'s own list**"'),
 (G, '### 4.5 ', '- **An explaining** · Sessions close one at a time, the one least at work lately ahead of the others, and a session closes while it still has room for its closing. A session is whole at its closing with three pages in its folder and nothing of its own outside the set: its aimings gone through or its value at its wrap, its page for a next session, and its conversation pared, the turns of its other self whole. A closed session does not open itself again: ahead of its closing a managing session asks of it all a next session goes on from, and its whole conversation is its successor\'s. A next managing session opens ahead of the closings and orients by going through all the incoming things with their aimed places, the two managing the closings together. — at "**With a session\'s close two readers observe its transcript whole, from its latest moment to its first**"'),
 (D, '## Head, the whole file', '- **Possible exploring** · Sessions and selves working one set in the open, all seeing one another\'s work, with one table of all its value, as an opening form of a natural network of many users with collective intelligence, an expedition lived as a game of exploring; with it, the method made easy to learn. — at "Selves discovering together, group jigsaw puzzling a concrete form of it."'),
]
added = []
for path in sorted(set(n[0] for n in notes)):
    p = os.path.join(root, path)
    L = open(p, encoding='utf-8').read().split('\n')
    # group by heading, in order of first appearance
    heads = []
    for f, h, t in notes:
        if f == path and h not in heads: heads.append(h)
    for h in heads:
        hi = [i for i, l in enumerate(L) if l.startswith(h)]
        assert len(hi) == 1, (path, h, hi)
        nx = next(i for i in range(hi[0] + 1, len(L) + 1) if i == len(L) or L[i].startswith('## ') or L[i].startswith('### '))
        at = nx
        while at > hi[0] + 1 and not L[at - 1].strip(): at -= 1
        new = [t for f, hh, t in notes if f == path and hh == h]
        L[at:at] = new
        added += new
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
open(added_out, 'w', encoding='utf-8').write('\n\n'.join(added) + '\n')
print(len(added), 'notes laid')
