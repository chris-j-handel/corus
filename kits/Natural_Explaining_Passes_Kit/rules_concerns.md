# Explaining each standing concern, for a next session (v389)

The person: "the concerns should be well explained and they can stay incoming for the next session." A concern stands at an offerings file as two blocks: the concern itself (as it was laid), then a line beginning `*Standing at v389:*` with a short reason. Leave the concern block whole. Re-say each `*Standing at v389:*` line as a readable explanation that a person opening the next session can act on, in natural explaining (no *the* unless valuable, no doer naming or saying, none of: reading, named, said, never, alone, unchanged, inside, outside, our):

`*Standing at v389:* <one or two sentences: what parts — quote the two sentences that part, each with its file and section (look them up in the living files at v389 so each quote is exact and current); or, if nothing parts, what the value needs before it can rise>. **To resolve:** <the decision or the observing it waits on, as one question or two plain options>.`

If the concern is already resolved at the living file at v389 (both sentences now agree, or the value is now carried), write `*Standing at v389:* carried at v389 at <file and section>, "<short quote>"; ready to dissolve.` so the next session can dissolve it at once.

Keep each explanation under about 90 words. Do not edit living files. Output: a JSON array of {"old": the exact existing `*Standing at v389:* …` line, "new": the re-said line, "verdict": "RESAY"} at the given path; cover every `*Standing at v389:*` line in the file; each old unique in the file. Verify with python. Reply with counts: re-explained, ready to dissolve.
