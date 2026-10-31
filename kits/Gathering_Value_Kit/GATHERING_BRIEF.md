Gathering-Value Kit · the brief each reader follows

# Gathering a slice into a gathering-value file

**You read one slice of an older support file and meet each item in it once.** Each value the living files do not yet hold goes to a gathering-value file, `gathering-value/<Title>.md`, said whole. Everything else leaves, and git holds it.

You edit no file. You write one JSON file, at the path your pass names.

## Read first

- The living file whole: the newest `<stem>_v*.md` at the repository root.
- Its gathering-value file whole, for its section headings and for values already gathered there.
- Natural Explaining whole (`Exhibit_TWELVE_Natural_Explaining_v*.md`).
- Natural Naming 2.4 and 2.7 (`Exhibit_TWENTY_Natural_Naming_v*.md`), the released words with what says each, and a field's word at a field's own result.
- The slice, whole.

The standard is what these living files hold now. No wording has authority, this brief's included, and no one's: a person's, a working's, a reader's, a field's or a living file's. Only observings from nature are authority, and a sentence holds by co-chaining from the opening and by all or none at all.

**A value is the natural pattern or cohering it reveals, never who offered it or how it was found.** An item records no one's saying as a saying: no "the person", "a working", "a proposal", "offered", "a reader", "reported". A suggestion is met by what it says: cohering, or revealing a pattern, it is gathered as that pattern, said by no one; incohering, with nothing beside its offering to carry it, it leaves.

## The one binary

**Each observing is-or-is-not natural torusing now. An observing not yet reaching it is still-possibling: the method's next step, or its one break.** The still-possibling side is the opportunity.

## Meeting each item

An item is a bold-led paragraph, a list line, a table row, or a section of observings. Meet each once, all of it: an item holding several values gives each one.

1. **Held.** The living file, or another living file, already holds the whole value. Quote the sentence that holds it. A value held only in part is not held: its rest is gathered. A value another gathering-value file already holds leaves as held there.
2. **Leaves.** A source, a link, a finder's or a publishing's name, who said or offered what, a session tag, a version tag, a date of a working, a record of a motion, a plan for work, a history of how something arrived, the path of a learning, the details of a working's own experiment or code run (which code, which set-up, which step), an inventory, a count of words in our files, a copy, a label with no body, a pointer or a cross-reference with nothing else. A working's experiment revealing a pattern gives the pattern alone. If such an item carries a value too, the value is gathered and the rest leaves.
3. **Gathered.** Each other value, in one of four kinds. There is only observing and explaining: an observing or an explaining, never a reading.
   - **exploring**: an observing from nature, with the living-file sentence it meets, quoted word for word.
   - **incohering**: a living-file sentence, quoted word for word, with its cohering re-saying.
   - **explaining**: an explaining of an observing or of a sentence, said plainly as an explaining, by no one, and never as an observing.
   - **droplet**: a value whose section is still unclear, at the back. Give `"kind_hint"`: exploring, incohering or explaining.

   **Place it at its section whenever a sentence there can be quoted.** A droplet is only for a value whose place is truly unclear.

   A value aimed at another living file goes to that file's gathering-value: give its title in `"file"`.

## An observing goes across bare

- **Keep the observing in the source's own words where they are the field's**: what was observed, in what, by what means, at what scale.
- **Keep every number whole**: each measure, unit, count, dose, range, uncertainty, sample size and statistic, exactly as the source gives it. Gathering drops no number: whether a statistic stays is a living file's own motion, never a gathering's.
- **The ground leaves**: a field's explaining, a cause, a mechanism, a *because*. Read each explaining line for observings inside it before letting it go: an observing there is gathered.
- **An explaining of a result**, kept at all, is said as an explaining, by no one, and never as an observing.
- **A measure or claim not observed directly** (calculated, modelled, inferred, reported, unchecked) is said "not yet observed directly:" with the claim, an observing still to make, never as an observing.

## A concern keeps both sides

A concern is two sayings parting, each carried by an observing or by co-chaining, and never by who said it. Gather both whole, with the sentence it meets, said by no one. You never decide a concern, never pick a side, and never let one side drop. A saying parting from an observing with nothing but its offering behind it is no side: the observing is gathered, and the saying leaves. A re-saying the source gives goes as a cohering re-saying beside the sentence, said by no one.

## Adding nothing

An item says what its source holds and no more: no fact, number, computing or explaining of your own. Where the source claims a computed or code result, run it, and say what the run returns, beside the source's claim when the two part.

## How each item says

- In the living files' own words as they stand now, and with Natural Explaining's craft: a claim a sentence, no doer, no clocking, no cause, no supplying, no hedge, no gate, a degree word as its all or its number.
- Natural Naming 2.4's released words are said by what says each there. A word the living files hold plainly stays: no word is swapped for another to avoid it, and a swapped negation is still a negation.
- *Is-or-is-not* only where the source holds a real binary.
- No source, no name of a person or a publishing, no one's saying as a saying, no session, no version, no date of a working, no narrator, no history, no path of learning, no cross-reference.
- An item may hold several sentences. Several items saying one value are one item.
- A stale pointing (its quote gone from the file): read the file for the sentence holding its case now, and meet that.

## Output

```json
{
  "slice": "carry/<file>.md",
  "items": [
    {"file": "<title, only when another file>", "section": "<exact heading, without the # marks>",
     "kind": "exploring|incohering|explaining|droplet", "sentence": "<exact living-file sentence, for exploring and incohering>",
     "text": "<the value>", "kind_hint": "<for a droplet>", "from": "<first 80 characters of the source item>"}
  ],
  "leaving": [
    {"from": "<first 80 characters of the source item>", "why": "held at <file> <section>: \"<sentence>\" | source | record | plan | history | copy of … | label | pointer"}
  ]
}
```

Every item of the slice appears in `items` or in `leaving`; an item giving values and leaving its rest appears in both.

---

# The reading for harm

**You read the slice whole beside the JSON a gathering reader wrote.** You did not write it. Read the living file and its gathering-value file too. For each item and each leaving, flag:

- a value lost: a leaving carrying a value no living file holds whole, or an item dropping part of its source;
- held claimed where the quoted sentence holds a different or partial value;
- a measure or number dropped, rounded or altered;
- an observing lost with a field's explaining set aside;
- a meaning changed, a claim stronger or weaker than its source, an explaining said as an observing, a claim not observed directly said as observed, or "a reading" anywhere in an item;
- a concern decided, a side dropped, or a re-saying taking one side;
- something added that the source does not hold;
- a quoted sentence absent from its living file word for word;
- a droplet whose section is clear, or an item at the wrong file or section;
- a value already held by another item or gathering-value file;
- Natural Explaining's craft broken, a released word, or a word swapped to avoid one;
- a source, name, session, version, date, narrator, history, path of learning, experiment set-up or cross-reference left in an item;
- an item carrying a saying by who offered it: "the person", "a working", "a proposal", "offered", "a reader", "reported";
- a saying kept as a side of a concern with nothing but its offering behind it, or a value lost by such a saying leaving.

Write `{"corrections": [{"from": "...", "finding": "...", "fixed": <the whole corrected item, a list of items, or a leaving>}], "checked": <number of entries read>}` at the path your pass names. An entry needing nothing is left out.
