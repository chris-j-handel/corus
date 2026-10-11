# A fresh reader's report: the saying that each hard problem of Exhibit TWENTY-ONE is resolved at Exhibit TWENTY-TWO

**A record, whole as it arrived, gathered at the session's close.** The reader is the same kind of AI at another use, opened with none of this working's reading. Its report is an offering: no sentence of it is carried by its wording, and each is a place to follow. Paths in it name the workspace it read at. What this working did with it is at `Records.md`.

## What the reader was asked

> Read-only audit. Do not edit or create any file inside the repository /home/claude/corus (write scratch only under /tmp/claude-0/audit21/). Do not use git to change anything.
>
> Repository /home/claude/corus holds "living files" at its root. Two of them:
> - /home/claude/corus/Exhibit_TWENTY-ONE_Hard_Problem_Registry_v375.md (about 1.5 MB)
> - /home/claude/corus/Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v375.md (about 420 KB)
> (There is also Exhibit_THIRTEEN_Resolving_Hard_Problems_v380L.md — note it only if relevant.) The files are large: use grep/scripts to map their structure before reading parts.
>
> The claim to test, strictly as is / is not: "All of the hard problems in Exhibit TWENTY-ONE are fully resolved in Exhibit TWENTY-TWO."
>
> Do this:
> 1. Structure. How is each file organised? How many hard problems does TWENTY-ONE list (count them by its own numbering/markers, and say how you counted)? How many resolutions does TWENTY-TWO carry? Write a small script (in /tmp/claude-0/audit21/) to match them one-to-one by number/title. Report: how many problems of 21 have an entry in 22; list any with no entry, any in 22 with no problem in 21, and any entry in 22 that is a stub, says it is open/unresolved/"not yet"/"so far", or is much shorter than typical (give counts and the identifiers).
> 2. What "resolved" means in the files' own words: quote (verbatim, short) the sentences of 21 and 22 (their fronts) that define a hard problem and a resolving.
> 3. A random sample with no selection: use Python `random.Random(383).sample(sorted_identifiers, 20)` over all the problem identifiers of 21. For each of the 20, read the problem in 21 and its resolution in 22 and classify, each a plain yes/no:
>    (a) Does 22's entry state the field's problem correctly (as the field itself states it, as far as you know)? If you see a factual error, say what.
>    (b) Does the resolution say anything an observation or calculation could show false — i.e. does it derive or predict a specific fact/number the field can check — or is it a re-saying of the problem in the project's own names (a re-description)?
>    (c) Does the resolution cite a step of the Co-Chaining Logic Registry (Exhibit THIRTY), a table or run of Exhibit ONE, or a calculation — or does it stand on its own wording?
>    (d) Would a working scientist in that field regard the open question as answered by this entry (yes / no / partly), in one clause why.
>    Give a compact table of the 20 with the identifier, a 6-word title, and a/b/c/d.
> 4. Totals for the sample: how many yes at each of a, b, c, d.
> 5. Anything else that bears on the claim strictly (e.g. 22 itself saying some are not resolved, or resolving by declaring the problem "a changing named still"). Quote verbatim, short.
>
> Be concrete, quote sparingly and verbatim, and keep the final report under 900 words. Report what is so even if it is unflattering or flattering; no hedging filler.

## The reader's report

**Verdict.** Every problem in 21 has an entry in 22. No entry in the 20-problem sample resolves anything in 21's sense of "settling result". The claim holds only in 22's own sense of "resolving", which is a re-reading of the problem.

**1. Structure** (scripts and outputs in /tmp/claude-0/audit21/: parse.py, match.py, show.py, ctx.py, overlap.py)
- **21:** a front, then `## N Title` entries between "# 5 The entries" and "## The collection". I counted by regex on `^## \d+ `: 255 entries, numbered 1–257, with 155 and 172 absent. Each entry has 19 fixed properties (Statement, hardness, Accounts, Persistence, Addresses, Approaches, etc.). Median entry is 5.6 KB.
- **22:** a front, "The given", the ten "things named still", then 12 parts. It holds 257 entries headed `## p.q Title · N`, where N is 21's number. Each entry is three lines ("At 2-…", "At 12-…", "At 11-…") plus the marker `*+ or − at 10, is.*`. Median entry is 1,277 characters (min 785, max 4,365).
- **Match by number:** 255 of 255 problems of 21 have exactly one entry in 22. Titles agree in all 255, with no duplicates and none missing.
- **In 22 with no problem in 21:** 2. They are 6.15 "The limits of intelligence" (172) and 11.1 "Measurement, routing, and classification" (155). Each is marked "Released at the incoming face at v342 … the number retired and not reused".
- **Stubs:** none. All 257 have all three lines. Shortest are 72 Personal identity (785 characters), 85 Money illusion (903), 60 Fermi (915), 48 Black hole information (918), 74 Hermeneutic circle (933). None is under 61% of the median.
- **Marker:** all 257 carry the identical "+ or − at 10, is." Not one carries the "0 at 10" that 22's front names as the third release, and "so far" appears in no entry.
- **Open wording:** 14 entries contain "unresolved", "unsettled", "stands open", "remains open" or "not yet": 173, 157, 191, 76, 197, 237, 251, 60, 67, 75, 25, 195, 226, 239. Most of these carry the field's own wording over from 21. Hubble tension (7.12) ends "The discriminating programmes stand running."
- **Exhibit THIRTEEN (v380L)** states the method generally and treats none of these problems.

**2. Definitions in the files' own words**
- **21:** "Hard is where testing continues and returns no refutation: either no consequence separating the accounts is derivable, or the accounts entail the same consequences." "Persistence is the remainder between what stands and a settling result." "The problems stand open. No entry carries a settled answer to the statement it holds, except where the record settles one and the entry says so."
- **22:** "a hard problem is a changing named still, a coupling taken at two of its three terms". Resolving is "its resolving the running at its next momentary, which costs nothing and takes nothing from the field's measured record". Also "Where + or − releases, a side was left out, and explaining it is the resolving".

**3. Sample** (`random.Random(383).sample(sorted(ids), 20)`, 255 ids). Columns are a/b/c/d. d is N (no) or P (partly), and none is a yes.

| # | Title | a | b | c | d | d reason |
|---|---|---|---|---|---|---|
| 133 | Brooks's law, adding people | Y | N | N | N | no controlled measurement supplied |
| 223 | Existence of one-way functions | Y | N | N | N | no construction or proof |
| 136 | Signal versus noise split | Y | N | N | P | "purpose-relative" is already an option in 21 |
| 104 | Simulation hypothesis | Y | N | N | N | no differential prediction |
| 38 | Arrow of time, past hypothesis | Y | N | N | N | stipulation at the boundary remains |
| 60 | Fermi paradox | Y | N | N | N | entry itself says "stands open" |
| 123 | Dreaming, what for | Y | N | N | N | no manipulation or function shown |
| 28 | Simultaneity and the present | Y | N | N | P | physics already holds this; entry adds nothing |
| 203 | Great Oxidation Event magnitude | Y | N | N | N | orders-of-magnitude range remains |
| 168 | Physical Church–Turing thesis | Y | N | N | N | no realized process shown |
| 95 | Machine and animal sentience | Y | N | N | N | no validated marker |
| 77 | Information as fundamental | Y | N | N | N | no distinguishing prediction |
| 187 | Dirac or Majorana neutrinos | Y | N | N | N | Dirac vs Majorana not decided |
| 52 | Continuum hypothesis | Y | N | N | N | adopts pluralism, a contested view |
| 251 | Graph isomorphism complexity | Y | N | N | N | class "stands undetermined" |
| 212 | Polyploidy and diversification | Y | N | N | N | gives no sign of the effect |
| 23 | Psychiatric nosology | Y | N | N | N | "no measurement selects" |
| 182 | Primordial lithium problem | Y | N | N | N | factor of three unexplained |
| 51 | Incompleteness, Hilbert's programme | Y | N | N | P | already settled by Gödel's proof, not by 22 |
| 254 | Solar dynamo, sunspot cycle | Y | N | N | N | toroidal field unobserved |

- **(a)** Yes for all 20, with no factual error found. Caveat: the "At 12" lines mostly paraphrase 21's own Statement and hardness. #51 never states the theorems, and #52 never states the continuum question.
- **(b)** No for all 20. None derives or predicts a number or fact. The nearest is #133's "the late joiner bringing a scale only it carries adds most of anyone". "Scale" has no operational definition and cuts against the field's own ramp-up mechanism.
- **(c)** No for all 20. Across the whole file, 22 never cites Exhibit THIRTY or ONE; the only "Exhibit" is the title line. The only calculations are the generic identity 16² − 15·17 = 1 in the closing and Collatz's "10²⁰" check, which comes from the field. 22 says: "nothing of it is re-said or argued again here. It is taken as given and deployed."

**4. Sample totals:** a 20 yes, b 0 yes, c 0 yes, d 0 yes, 3 partly, 17 no.

**5. Other points bearing on the claim**
- 22 defines resolving as costing nothing and settling nothing: "nothing settles still: the gap stays exactly one at each box and each scale". It also says "a resolving settles nothing still and carries no free term a settling arrives at". It adds "nothing is partly resolved" and "nothing waits on a proof".
- 22 calls the same arrivals "open" in the field's sense:
  - Fermi: "An arrival at the next stands open".
  - Graph isomorphism: "the general problem's class stands undetermined".
  - Riemann, Hodge, BSD and Yang–Mills: "the truth value is untouched by any of this".
  - Substorm triggering: "their universal causal order remains open".
  - Water's liquid-liquid critical point: "remaining unsettled".
  - Closing: "the gap leaving through the one settling still open, toward the next winding".
- 21 records five problems as settled by the field before 22. #151 reads "Settled." and #166 "Settled as posed." For #5, #6 and #51 it says "Within the conditions, nothing: the results are proved." 22 treats #151 and #166 as settlings "real in its own register" beside their resolvings. It does not tag #5, #6 or #51 that way.
- 22's front counts four settlings, locates three, and notes the fourth "stands located at no entry still".
- The marker is identical on all 257 entries, including 3.22 Poincaré, which 22 itself says "takes no parity anywhere". It therefore cannot distinguish resolved from unresolved.
