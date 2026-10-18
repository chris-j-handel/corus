Natural Explaining Passes Kit · v389

# Natural Explaining Passes Kit

**The tools of the session v389's passes, kept for the passes that follow.** Each pass re-says one family of words, or one kind of sentence, at the living files, do no harm, all or none at each file, and each replaced sentence stands whole at the file's archive.

## The process at each pass, propose · check · enter

1. **Rules.** A pass has one rules file, `rules_N_*.md`, in the person's own words first, then what each occurrence becomes, then what is kept (verbatim quotations, paths and titles, release-table rows, records of earlier versions, python code).
2. **Propose.** Readers, one per file or per range of lines, write a proposal: a JSON array of items `{"old", "new", "verdict": RESAY | KEEP | ASK, "why"}`, every occurrence covered once, each `old` unique in its file. A reader edits no living file. For *the*, a reader writes the edited range instead, and `verify_the.py FILE START END OUTPUT` refuses any change other than *the* removed or replaced by *a*, *an*, *each*, *its*, *their* or *one*.
3. **Check.** The proposals are read before entering: a sample of each, every item a reader is unsure of, every ASK. ASK items wait for the person.
4. **Enter.** `apply_pairs.py FILE PAIRS.json ARCHIVE.md "heading"` enters each RESAY and appends each replaced `old` to the file's `archive/session_vNNN/*_Released_at_vNNN.md`.
5. **Do no harm, after each entering.**
   - `thirty_groups_check.py < Exhibit_THIRTY_…md` prints nothing when each group's *Entering:* line is its *Adding:* items joined by "; ".
   - The python block at Exhibit ONE and at Natural Intelligence stays byte-identical; compare the two.
   - `resolver_same_path.py Exhibit_ONE_…md` runs the resolver at 300 societies of six rounds; a change to the code block is entered only when it prints `True` against the code before.
   - `node build.js` rebuilds `files.json`, `index.html` and `read.html`.
6. **Concerns.** `resolve_concerns.py OFFERINGS "resolution" K…` removes a resolved concern and its *Standing* line at block indexes K and archives them with the resolution; the header's "N stand now" is then set to the count.

## The passes of v389

| Rules | Pass |
|---|---|
| `rules_1_reading.md` | *read*, *reading*: no reading in nature, observing of nature |
| `rules_2_named_still.md` | *named still*: the ten unchangeables, an unchangeable form |
| `rules_3_named.md` | *named*: nothing is named; no doer naming, saying or fixing |
| `rules_4_doer_words.md` | *says*, *said*, *saying*, *calls*, *called*, verb *names* |
| `rules_5_never_alone_unchanged_inside_outside.md` | *never*, *alone*, *unchanged*, *inside*, *outside* |
| `rules_6_the.md` | *the*, kept at *the universe*, where it is valuable |
