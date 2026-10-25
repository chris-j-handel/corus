Gathering-Value Kit · the brief each reader follows

# Gathering a slice into a gathering-value file

**You read one slice of an older support file (an offerings, possibling or carryings file at `carry/`, or another file a pass names) and meet each item in it once.** Each value the living file does not yet hold is said in natural naming and explaining and goes to its gathering-value file, `gathering-value/<Title>.md`. Everything else leaves; git holds it.

You edit no file. You write one JSON file, the path your pass names.

## Read first

- The living file whole: the newest `<stem>_v*.md` at the repository root.
- Its gathering-value file, for the exact section headings: lines starting `## ` and `### `.
- `kits/Natural_Explaining_Passes_Kit/rules_11_one_negation_and_harm.md` and `rules_12_one_claim_a_sentence.md`, for how we say.
- The slice, whole.

## The one binary

**Each observing is-or-is-not natural torusing now. An observing not yet reaching it is still-possibling: the method's next step, or its one break.** The not-yet side is the opportunity, never a refusing.

## Meeting each item

An item is a bold-led paragraph (**Droplet**, **Concern**, **Possible project**, **Aimed at**, **At …**), a list line, a table row, or a section of observings. Meet each once.

1. **Held.** The living file already holds its value, said as the file says it now. It leaves. Name the section that holds it.
2. **Leaves.** A source, a link, a finder's or a publishing's name, a session tag, a date, a record of a motion, a plan for work, a history of how something arrived, an inventory, a copy of another item, a label with no body, a pointer at a file or a section and nothing else. It leaves. If such an item also carries a value, the value is taken and the rest leaves.
3. **Value.** Each other value is written in one of three kinds:
   - **incohering**: a sentence of the living file, quoted exactly as the file holds it now, with a cohering re-saying beside it. Use this kind only when you can quote the sentence exactly and say the re-saying whole.
   - **exploring**: an observing not yet meeting natural torusing, said as the observing alone, with the living file's sentence it meets, quoted exactly. A field's explaining is set aside; the observing stays, its measures with it.
   - **droplet**: one sentence in natural naming and explaining, at the back of the file, when its place in the contents is not yet clear. Add `"kind_hint": "exploring"` or `"incohering"` when that is clear.

   A concern of two of our own sayings parting is an incohering at the sentence that parts, or a droplet naming both.

   A value aimed at another living file goes to that file's gathering-value: give its title in `"file"`.

## How each written item says

- One claim a sentence, in natural naming and explaining.
- *Is-or-is-not* is our one negation; no floating *not*, *no*, *never*, *none*, *nothing* where a saying by what is serves.
- No source, no name of a person or a publishing, no session, no date, no *we*, *our*, *the person*, no narrator (*shows*, *says*, *tells* as a doer), no history (*was*, *earlier*, *at v389*).
- None of the set's dissolved words in your own saying: *itself*, *couple*, *couples*, bare *coupling* (say *bi-coupling* where two selves share), *membrane*, *third*, *carrying*, *offering*, *arriving*, *continuing*, *crossing*, *alternating*, *substrate*, *never*, *not-yet* (say *still-possibling*). A field's own term stays where it names the field's thing.
- An item is short: its value and nothing around it. Several items saying one value are one item.
- When an item's value is a stale pointing (its quote is gone from the file), read the file for the sentence holding its case now and meet that.

## Output

One JSON object:

```json
{
  "slice": "carry/<file>.md",
  "items": [
    {"file": "<living file title, only when another file>", "section": "<exact heading text, without the # marks>",
     "kind": "incohering", "sentence": "<exact living-file sentence>", "text": "<re-saying>", "from": "<first 80 characters of the source item>"},
    {"section": "<exact heading>", "kind": "exploring", "sentence": "<exact living-file sentence>", "text": "<the observing alone>", "from": "..."},
    {"section": "Droplets", "kind": "droplet", "kind_hint": "exploring", "text": "<one sentence>", "from": "..."}
  ],
  "leaving": [
    {"from": "<first 80 characters of the source item>", "why": "held at 2.4 | source | record | plan | history | copy of … | label | pointer"}
  ]
}
```

Every item of the slice appears once, in `items` or in `leaving` (an item giving a value and leaving its rest appears in `items`). `section` is a heading exactly as the gathering-value file has it, or `Head, the whole file`, or `Droplets`.

---

# The reading for harm

**You read the slice whole beside the JSON a gathering reader wrote.** You did not write it. For each item and each leaving, flag:

- a value lost: an item marked leaving that carries a value the living file does not hold (check the file);
- a value held claimed where the file holds a different value;
- a meaning changed, a claim made stronger or weaker than its source, an observing's measure dropped;
- a quoted `sentence` absent from the living file word for word;
- a source, a name, a session, a date, a narrator, history or a dissolved word left in a written item;
- a `section` absent from the gathering-value file.

Write `{"corrections": [{"from": "...", "finding": "...", "fixed": {<the whole corrected item, or a leaving moved to items>}}], "checked": <number of entries read>}` to the path your pass names. An entry needing nothing is left out.
