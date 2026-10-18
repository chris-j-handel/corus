# Re-saying doer words at one living file (v389): says, said, saying, sayings, calls, called, so-called, and *names* as a verb

The person: "why does there need to be a character naming or saying something. the thing is a concept and we explain the thing." Also: "nothing is named. there is natural naming and explaining. the concepts are living and explaining." *Named* is already re-said everywhere.

Re-say each occurrence so no doer (a file, a line, a section, a field, a person, a sentence, a self, "we", "one") is saying, calling or naming. Explain the thing itself:
- a file or section saying: "Natural Naming 4.9 says X" → "X, Natural Naming 4.9" or "at Natural Naming 4.9, X"; "as 2.4 says" → "at 2.4"; "the line at 9 says bi-…" → "the line at 9 is bi-…".
- a field saying: "as the field says" / "the field's own saying" → "in the field's own words" (KEEP is fine where it is plainly the field's quoted words); "the field calls it X" → "the field's X" or "X, in the field's words".
- passive with no subject: "it is said at" → "it is at"; "X is said as Y" → "X is Y"; "said once" (a concept said once at its file) → "at one place" or "once"; "so-called X" → "X".
- noun *saying(s)* meaning a sentence of a file: "two sayings part" → "two sentences part"; "a saying at 3.2" → "a sentence at 3.2".
- *names* as a verb: "A names B" → "A is B" / "B, at A" / "A, B" — whichever explains the thing. *names* as a noun (the seventeen names, its name, the resolver's names) STAYS — do not touch.
- *calls* as a resolver/code call (function calls) STAYS.
Keep each sentence otherwise identical; no added "the"; do not introduce named, unchanged, never, alone, gives, takes, inside, outside, our, held, holding, read, reading, says, said, called. Grammar whole.

RESOLVED at v389: "said beyond" / "said between" drops *said*: "nothing is beyond or between things of the universe" (the person approved).

KEEP only: verbatim quotations; paths, file names, URLs, outside titles; Natural Naming 2.4/6.3/6.4 release-table right-column released words; the Living File Registry's version-history records of earlier versions; code blocks of python.

Output: JSON array at the given path, items {"old": exact substring unique in the whole file (≤400 chars), "new", "verdict": "RESAY"|"KEEP"|"ASK", "why"}. Cover every occurrence of (?i)\b(says|said|saying|sayings|calls|called|so-called)\b exactly once, plus every verb use of \bnames\b you re-say (noun uses need no item); no overlaps. Verify with python (uniqueness, coverage of the regex, no overlap). Do not edit the living file. Reply with counts and unsure items.
