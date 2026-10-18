# Pass 1 brief: resolve an offerings file against its living file (v389)

Read first, whole:
- carry/Improving_Passes.md, section "Natural explaining, as v389 resolved it" (the standards every risen sentence must meet);
- kits/Natural_Explaining_Passes_Kit/rules_offerings.md (the verdicts);
- the living file named in your task, whole.

An ITEM is each paragraph of the offerings file that is not a heading: it starts at a non-blank line after a blank line (line numbers 1-based). Skip the file's title line, the "# Offerings…" heading and the first status paragraph (line 5) only if it is a "Next at this file" note — give that one verdict RELEASED with why "a working note, superseded by Improving Passes". Cover EVERY other item in your line range exactly once.

For each item write one JSON line to your JSONL path:
{"line": N, "head": "<first 100 chars>", "verdict": "CARRIED|RELEASED|DUPLICATE|RISE|CONCERN", "where": "<section and short quote, for CARRIED>", "why": "<reason, for RELEASED and CONCERN>", "of": <line, for DUPLICATE>}
- CARRIED: the living file already carries the value (say where, with a short quote).
- RELEASED: the item rests on a form v389 releases (earlier resolver names like 2-bi-co-bi-offering, *named*, *reading*, *emanating* said of the method, inside/outside, a store, a clock over the changing, a second now, equilibria as possible, *held still*, etc.), or is a working note superseded.
- DUPLICATE: another item says the same value.
- RISE: the value is not yet at the living file and coheres with it and with the standards. Also write its insertlet as {"old": exact unique substring of the living file (≤400 chars), "new": the same text with the value entered in natural explaining, "item": N} to your EDITS path (a JSON array). Keep risen sentences short, in the file's own voice, no *the* unless valuable, no doer naming or saying, none of the released words, binary all or none.
- CONCERN: two sentences part, or the value needs the person's decision; why says which sentences part.
Do NOT edit any living or offerings file. Verify with python: every item in range covered once; each edit's old occurs exactly once in the living file and edits do not overlap. Reply with counts per verdict, the RISE list (one line each) and the CONCERN list (one line each).
