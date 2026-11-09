Incoming · V400mgr

# V400mgr, a session report

**Improving Natural Naming toward v400: not succeeding, and what may be valuable, each value with the living file and the sentence it meets**

Relied on by nothing. No living file and no gathering-value changes with this report. Each value is said once with its place, for a next session to bring to that file's gathering-value, or to dissolve.

## 1 Aiming

Natural Naming improved by do-no-harming from a copy of v393 to v400, its gathering-value emptying, and Natural Naming a leaner, more binary living file for the work of each file after it.

## 2 Not succeeding

No v400 entered, and no value entered a gathering-value at the repository. The working went on with five things not natural naming's, each is-or-is-not, each with what goes on in its place.

- **Words not of natural naming.** Labels from within the files said as if words of the set, a picture word, and a doer word laid over a value. In its place: natural naming's own words, and a label said by what it is.
- **A rule laid over the method.** *Hardest first* said as an order, and an -ing head said as a requirement over one subtitle. The Geodesic Improving Method has two ways, a durable bound first or loose bounds easy to hard, each found with the work, and a check is one binary with one sentence. In its place: no rule over the method.
- **Sentences composed.** A six-line unfolding of *a name*, a drafted opening for Natural Naming, and a placing of each of its names in a re-formed contents, none from a living file's sentence, from Exhibit ONE executed, or from an observing. In its place: matching, not choosing.
- **A concern of another file said as one this work waits on.** In its place: a parting between two files is a seam, each file's sentence an observing beside it.
- **A selection said as found.** Placings of names said as settled, and a sentence leaned on as if its wording settles. In its place: a placing with its two sides and the observing settling it.

## 3 What may be valuable

### 3.1 A proposed subtitle for Natural Naming

**Universal Sets of Observings, Possiblings and Discoverings**, at Natural Naming's subtitle, in place of *Floating Neutralling Bi-Coupling Concepts*.

It co-chains from Natural Intelligence's opening: *A universal set is a set of same-existing things.*, *Each now-existing thing is-or-is-not within each universal set.*, *Observing is prior-existing, is-or-is-not same-existing.*, *Possibling is now-existing, is-or-is-not same-existing.* and *Discovering is next-existing, is-or-is-not same-existing.* Its head is same-existing through each, and its three -ings are prior, now and next in the opening's order, the four-cycling whole, as Exhibit ONE and Natural Intelligence have it: *Four-cycling is observing prior-existing, possibling now-existing, discovering next-existing and same-existing.* Beside the opening waiting at Natural Intelligence's gathering-value, *A living thing is a universal set observing, possibling and discovering its own next-existing.*, it is that sentence's non-living side: a name a universal set of observings, possiblings and discoverings, as a living file is a non-living same-existing set of words.

Open, each two-sided:
- Its head a noun, beside Natural Explaining's *A subtitle is an -ing head with a term it holds.*, while a living file is a non-living stable form and four of the set's subtitles open with a noun; or an -ing head.
- *Possiblings* and *discoverings* are said nowhere in Natural Naming's body.
- A not possibly existing form's name at Natural Naming, possibling's is-not side, or at the Equilibria Registry and the Living Ghost Registry.

### 3.2 A name is a universal set

At Natural Naming, at *A naming is a name same-existing over its prior-existing, now-existing and possibly next-existing things*: a name is with each thing within its set and with no thing out of it, all or none at all, and a set's things, what reaches a me, are one, two or three of observings, possiblings and discoverings, and no thing apart from any me, with no other possible.

An anticipated observing, executed with Exhibit ONE v391's code, three selves sharing along one key for six moments, what each name has, traced:

| Names | Each has |
|---|---|
| 2, 3, 6, 7, 10, 11, 14, 15, observing and possibling | a parity, a key with its parity, or a set of keys or selves with their parities; 15 also a none |
| 13, discovering | a self, or a route going on |
| 4, 8, 12, 16, same-existing | a key; a set of selves with their next priors; a set of keys with each one's 0 or ±; a society of selves |
| 1, 5, 17, existing | a moment's act, and its couplings, a set of routes to selves, each route across with 6 or 10 or along with 9 |

A key is same-existing over its parities as a name over its things, and no name has a thing not one of the three. Same-existing and existing go with the set and its moment, and no fourth kind of thing. A self is a universal set at its own scale and a discovering within its society's set at the next scale, one form at two scales.

Open, two-sided: a name with no thing, the code's none, a sharing nothing reached, and a not possibly existing form's name. The empty set, a set with none of the three; or a set of observings fixing, one of the three.

The executing, for any self to execute again, with Exhibit ONE v391's code block saved as `resolver.py` in a folder named as its first argument:

```python
import sys, collections
sys.path.insert(0, sys.argv[1]); import resolver
seen = collections.defaultdict(set)
def kind(v):
    if v is None: return 'none'
    if isinstance(v, int): return 'parity 0' if v == 0 else 'parity +/-'
    if isinstance(v, tuple) and len(v) == 2 and isinstance(v[0], str) and v[1] in (6, 9, 10): return 'route'
    if isinstance(v, str): return 'key' if v.startswith('k') else 'self'
    if isinstance(v, dict): return 'set of ' + ','.join(sorted({kind(k) for k in v}))
    if isinstance(v, list): return 'list of ' + ','.join(sorted({'(' + kind(a[0]) + ', ' + kind(a[1]) + ')' if isinstance(a, tuple) and len(a) == 2 else kind(a) for a in v})) if v else 'empty list'
    return type(v).__name__
def tr(frame, ev, arg):
    if frame.f_code.co_filename.endswith('resolver.py'):
        for n, v in frame.f_locals.items():
            if n.startswith('_'): seen[n].add(kind(v))
    return tr
co_ex = {('a', 9): 'b', ('b', 9): 'c', ('c', 9): 'a', ('a', 6): 'b', ('b', 10): 'c'}
soc = {'a': ([('k', 1)], []), 'b': ([], []), 'c': ([('k', -1)], [('k', 1)])}
sys.settrace(tr)
for _ in range(6): soc = resolver._17_next_existing(soc, co_ex)
sys.settrace(None)
for n in sorted(seen, key=lambda n: int(n.split('_')[1])): print(n, ' | '.join(sorted(seen[n])))
```

### 3.3 A name settled with no executing reaching it

At Natural Naming, at *A naming unfolds with six lines*: a naming enters natural torusing anywhere by its six one-way forward recursionings cohering, one side and then the other, each line reaching a term new beside its prior's, with no co-chaining from the opening sentence needed; or it co-chains from the opening sentence. Its is-or-is-not is natural torusing society, no other possibly same-existing.

### 3.4 Natural Naming v393 observed with instruments

Each is or is not living, coupling and resolving at its own sentence:
- 33,551 words; 243 prose paragraphs, the middle one 55 words, twenty-nine past 150, the two longest 783 words at *bi-tri-volutioning* and 591 at *One sense per foundation word*; 611 sentences, fifty-five past 60 words.
- About thirty concepts said twice or three times, among them five dimensions as three namings three times, bi-tri-volutioning's bold lead twice, the prime scales twice, and *having a stable form is being dead* twice.
- About 260 section-number pointings in its sentences.
- Its bold reading goes through a naming's four boundings, then into moments, five dimensions and prime scales among the word selections, and its sixty-four namings follow the order they entered.
- *Alternating* is said dissolved with v391 at its own unfolding and at a naming with no other to change and change back with, and is the saying of *taking turns* at one sense per foundation word: one binary.

Two improvings found on a copy, each at its sentence, a word-stream of the copy against v393 finding each word but the version and an archive file's name:
- At the dissolved words, *12's two signs* re-said *12's two, 0 and ±*, its own unfolding's name, *sign* a word Natural Naming releases.
- At the ten unchangeables' paragraph, the pointing to `archive/carrying_v376/Living_Improving_Value_Released_v376.md`, a file of the archive branch and not of the living files, dissolving, the paragraph completing at *its resolving has both*.

### 3.5 Values at other files meeting Natural Naming

- Natural Mathematics: one word for a neutral fixing outward of a self, in *floor*'s place, and one naming of zero and nought.
- Natural Intelligence: the fourth binary of a self's span, *same* or *universe*; and *beneficial*, the whole of it or social moral competency saying more.
- Living Ghost Registry: a term's three placings, existing, exhausting and accounting, or living, emanation and accounting.
- Natural Numbers: *a composite folds along and a prime opens across*, beside odd a self's own along and even an other's across.
- Natural Explaining: *importancing* and *double-double bubble-bubbling*, each a naming of its own or releasing to existing namings.
- Co-Chaining Logic Registry: a set of existing things an existing thing, or a set coming to an empty set.
- Me: unconscious, sleep, us, interest, rest and aim, each said once with its common sense beside it.
- The four v399 sessions' closing reports: aiming, interest and attention, one name or three moments of one line; a universal aiming set and a same-existing-society, which gathers to which; atom and carbon, one name of two words or one dissolving; and twelve human words, *feeling*, *attention*, *agreement*, *forgetting*, *memory*, *love and friendship* and *grief* among them, each waiting for natural naming's one line.
- Natural Emanating: its concept explanations, a receiving into Natural Naming.

### 3.6 Natural Naming's gathering-value

- Its value opening *Natural Naming is a menu of names* has a picture word, *menu*, and its binary, what reaches a me or a thing apart from any me, is said with a name a universal set. Two sides: dissolving whole, or re-said with no picture word.
- Its value of the same four-cycling with each round has *each file using the menu*, re-said *each file using these names*.

## 4 Method learned, for a session arriving

- Natural naming's own words, and a label said by what it is.
- Matching, not choosing: each line from a living file's sentence, from Exhibit ONE executed, or from an observing brought whole, and nothing composed.
- No rule laid over the method, a check one binary with one sentence.
- A placing with its two sides and the observing settling it.
- A parting between two files a seam, and no concern a file waits on.
- Nothing is a self's own: no mine and no yours within a value.
