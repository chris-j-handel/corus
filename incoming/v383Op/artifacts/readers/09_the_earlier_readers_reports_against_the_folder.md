# A reader at the session's close: the earlier readers' reports against the folder

**A record, whole as it arrived.** The reader read each earlier reader's report and looked for each item of it at the folder as it was at commit `0779a54`. Its marks are its own. What this working did with it is at `Records.md`.

# Review A: value in the sub-agent reports that the v383Op folder does not carry today

Read-only. I edited nothing in any repository. My scripts and extracts are only under `/tmp/claude-0/-home-claude-corus/fb33d5a3-b8e6-5358-aeca-12dbe438030a/scratchpad/review_a/`. `extract2.py` is the extractor. `out/agent-<id>.txt` holds each agent's first user message and final report in full. `work/droplets.txt` holds the 181 carry lines ending "— v383Op". Foreign files already in that directory are untouched.

## Scope notes (read first)

- **Transcripts.** There are 19 in `/root/.claude/projects/-home-claude-corus/fb33d5a3-b8e6-5358-aeca-12dbe438030a/subagents/`.
  - Four are newer than 05:00 local on 7 October 2026 and are ignored: `a182c7c3763aa1827`, `a22f54ae904a6fe19`, `a3d68f3ae25e4ed8d`, `ae8cef5e39550c8c6`.
  - Fifteen remain. Ten have a final report (A1 to A10). Five died on "API Error: 529 Overloaded" and have no report (listed at the end). Your brief said thirteen. The count is fifteen.
- **Where reports live.** Eight of the ten reports are not "last assistant text". They are in a `SubagentHandback` tool_use block, so the first extraction printed None. `extract2.py` also captures that block. A9 and A10 ended in plain text.
- **What I searched.**
  - The eight folder `.md` files: README, Unresolveds, Two_Logics, Improving, Is_Or_Is_Not, Meeting_v382A, Meeting_v384A, Network_Surface.
  - The folder `.py` files and `returned/*.txt` where a number was at issue.
  - The 181 carry-offerings lines ending "— v383Op". These include the earlier v381R droplets as well as this session's 53 distinct droplets in 90 placings.
  - `carryings/v383Op/` (the frozen first report), only as a note.
- **How statuses were judged.**
  - The folder has been heavily revised since the agents ran. Improving.md line 12 ("the second … brought fourteen smaller defects. Each is mended here"), README line 99 and Is_Or_Is_Not's Limits all say a review round was followed by mends.
  - Statuses are by reading today's text at the place named, not by re-running scripts.
  - The eleven `carry/` entries A3 and A4 reviewed no longer exist in that form. They were re-laid as droplets at offerings. Per-entry replacement wordings are therefore marked "by supersession", and where I could not match one I say so.
- **Legend.**
  - (a) mended or addressed.
  - (b) recorded open, with the row named.
  - (c) not carried anywhere.
  - ND means could not determine.
  - C-n points to the verbatim (c) block in that agent's section, then to the ranked list at the end.

---

## A1 — `a10faeff1305c4630` (6 Oct 12:46Z)

**Asked:** a read-only audit of the claim "All of the hard problems in Exhibit TWENTY-ONE are fully resolved in Exhibit TWENTY-TWO". It covered structure and one-to-one matching, the files' own definitions of "hard problem" and "resolving", a seeded sample of 20 (`random.Random(383)`) classified a to d, totals, and anything else bearing on the claim.

| # | Item | Status | Where / note |
|---|---|---|---|
| 1 | 255 of 255 problems matched, titles agree, no duplicates, none missing | (a) | Is_Or_Is_Not item 6; droplets at the 21 and 22 offerings ("each of the 255 problems has its entry, the titles agreeing, none a stub") |
| 2 | 21 is numbered 1–257 with 155 and 172 absent; 22 holds two entries (6.15 and 11.1) for them | (a) in part | Is_Or_Is_Not: "TWENTY-TWO holds two more, at numbers TWENTY-ONE retired". The numbers 155 and 172 and the entry ids are not given: C-13 |
| 3 | Structure counts (19 fixed properties per entry, median sizes, min and max, five shortest, none under 61% of median) | (c) low | C-13 |
| 4 | No stubs | (a) | as 1 |
| 5 | Marker "+ or − at 10, is." identical at all 257 entries | (a) | Is_Or_Is_Not item 6 ("One marker is at each of TWENTY-TWO's 257 entries alike"); droplet |
| 6 | No entry carries the "0 at 10" that 22's front names as the third release; "so far" in no entry | (c) | C-3 |
| 7 | 14 entries with open wording (ids listed); Hubble tension ends "The discriminating programmes stand running." | (c) | C-1 |
| 8 | Exhibit THIRTEEN states the method generally and treats none of these problems | (c) trivial | C-13 |
| 9 | Definitions in the files' own words | (a) in part | 22's "a hard problem is a changing named still" and "a resolving settles nothing still…", and 21's "The problems stand open." and "No entry carries a settled answer…", are in Is_Or_Is_Not item 6 and the droplets. The rest is C-13 |
| 10 | Sample of 20: the aggregate result (all a=Y; b none; c none; d none yes, three partly) | (a) | Is_Or_Is_Not item 6: "each states the field's problem rightly; none says a thing an observing or a reckoning could show other; none names a step…; none answers the field's own question whole, three in part" |
| 11 | The 20 ids, titles, per-row a to d and the reason for each d | (c) | C-13. The folder says only "seeded draw", with no seed and no ids |
| 12 | Caveat to (a): the "At 12" lines mostly paraphrase 21's Statement; #51 and #52 do not state their problem | (c) | C-13 |
| 13 | Nearest to (b): #133 | (c) | C-13 |
| 14 | (c): 22 never cites THIRTY or ONE; only calculations are 16² − 15·17 = 1 and Collatz's 10²⁰ | (a) in part | "none names a step" and "taken as given and deployed" are carried. The two calculations are not: C-13 |
| 15 | 22 itself says field arrivals "stand open" and that its resolving settles nothing | (c) | **C-1** |
| 16 | 21 records five problems as settled by the field; 22's front counts four settlings and locates three | (c) | **C-2** |
| 17 | The marker is identical even at 3.22, which 22 says "takes no parity anywhere"; so it cannot distinguish resolved from unresolved | (b) by reference, plus (c) | Meeting_v382A.md line 43 names "the marker beside a nought at Resolving the Hard Problem Registry 3.22" as one of v382A's own relations, "at no row here". A1's quote and conclusion are not carried: **C-3** |
| 18 | Verdict: holds at 22's meaning, not at 21's | (a), (b) | Is_Or_Is_Not item 6 and concern 5; row N1; droplets at both files |

### C-1 (A1 §5 and §1), verbatim

> 22 calls the same arrivals "open" in the field's sense:
> - Fermi: "An arrival at the next stands open".
> - Graph isomorphism: "the general problem's class stands undetermined".
> - Riemann, Hodge, BSD and Yang–Mills: "the truth value is untouched by any of this".
> - Substorm triggering: "their universal causal order remains open".
> - Water's liquid-liquid critical point: "remaining unsettled".
> - Closing: "the gap leaving through the one settling still open, toward the next winding".

> 22 defines resolving as costing nothing and settling nothing: "nothing settles still: the gap stays exactly one at each box and each scale". It also says "a resolving settles nothing still and carries no free term a settling arrives at". It adds "nothing is partly resolved" and "nothing waits on a proof".

> Open wording: 14 entries contain "unresolved", "unsettled", "stands open", "remains open" or "not yet": 173, 157, 191, 76, 197, 237, 251, 60, 67, 75, 25, 195, 226, 239. Most of these carry the field's own wording over from 21. Hubble tension (7.12) ends "The discriminating programmes stand running."

Why uncarried:
- The folder and the 181 droplet lines carry only 22's general sentence ("a resolving settles nothing still…") and the verdict "resolved by being read".
- None carries the places where 22 itself says a field arrival remains open. I grepped for Fermi, Riemann, Hodge, untouched, undetermined, discriminating, "partly resolved" and "stands open" (the last appears only at Is_Or_Is_Not line 87, about 21). Nothing relevant came back.
- I confirmed that all 13 phrases above exist in the 22 file today.

### C-2 (A1 §5), verbatim

> 21 records five problems as settled by the field before 22. #151 reads "Settled." and #166 "Settled as posed." For #5, #6 and #51 it says "Within the conditions, nothing: the results are proved." 22 treats #151 and #166 as settlings "real in its own register" beside their resolvings. It does not tag #5, #6 or #51 that way.
>
> 22's front counts four settlings, locates three, and notes the fourth "stands located at no entry still".

Why uncarried:
- Is_Or_Is_Not item 6 quotes 21's "except where the record settles one and the entry says so" but never says whether 22 honours it.
- I confirmed in the files that 21 has "Settled." (line 6249) and "Within the conditions, nothing: the results are proved." (lines 409 and 2257).
- I also confirmed that 22 line 802 reads "four arrivals stand as settlings … Three are located: the proof register at 3.22, the measurement register at 12.1, and the one still open at 7.12 … the fourth stands located at no entry still".
- Row N1 and the droplets are about the word "resolved", not about the settled arrivals.

### C-3 (A1 §1 and §5), verbatim

> Marker: all 257 carry the identical "+ or − at 10, is." Not one carries the "0 at 10" that 22's front names as the third release, and "so far" appears in no entry.

> The marker is identical on all 257 entries, including 3.22 Poincaré, which 22 itself says "takes no parity anywhere". It therefore cannot distinguish resolved from unresolved.

Why uncarried:
- The folder carries only "one marker at each alike".
- Meeting_v382A.md line 43 mentions the 3.22 marker as v382A's own relation, with "no row here".
- Not carried: that 22's front names a "0 at 10" release that no entry uses, and A1's conclusion that the marker discriminates nothing.
- 22 line 794 does say an arrival "settled by proof … takes no parity anywhere".

### C-13 (A1, remaining low-value items), verbatim

> **21:** a front, then `## N Title` entries between "# 5 The entries" and "## The collection". I counted by regex on `^## \d+ `: 255 entries, numbered 1–257, with 155 and 172 absent. Each entry has 19 fixed properties (Statement, hardness, Accounts, Persistence, Addresses, Approaches, etc.). Median entry is 5.6 KB.
> **22:** … It holds 257 entries headed `## p.q Title · N`, where N is 21's number. Each entry is three lines ("At 2-…", "At 12-…", "At 11-…") plus the marker `*+ or − at 10, is.*`. Median entry is 1,277 characters (min 785, max 4,365).
> In 22 with no problem in 21: 2. They are 6.15 "The limits of intelligence" (172) and 11.1 "Measurement, routing, and classification" (155). Each is marked "Released at the incoming face at v342 … the number retired and not reused".
> Shortest are 72 Personal identity (785 characters), 85 Money illusion (903), 60 Fermi (915), 48 Black hole information (918), 74 Hermeneutic circle (933). None is under 61% of the median.
> Exhibit THIRTEEN (v380L) states the method generally and treats none of these problems.

> 21: "Hard is where testing continues and returns no refutation: either no consequence separating the accounts is derivable, or the accounts entail the same consequences." "Persistence is the remainder between what stands and a settling result." …
> 22: "a hard problem is a changing named still, a coupling taken at two of its three terms". Resolving is "its resolving the running at its next momentary, which costs nothing and takes nothing from the field's measured record". Also "Where + or − releases, a side was left out, and explaining it is the resolving".

Sample, `random.Random(383).sample(sorted(ids), 20)` over 255 ids. Columns are a/b/c/d. d is N (no) or P (partly), and none is a yes:

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

> (a) Yes for all 20, with no factual error found. Caveat: the "At 12" lines mostly paraphrase 21's own Statement and hardness. #51 never states the theorems, and #52 never states the continuum question.
> (b) No for all 20. None derives or predicts a number or fact. The nearest is #133's "the late joiner bringing a scale only it carries adds most of anyone". "Scale" has no operational definition and cuts against the field's own ramp-up mechanism.
> (c) No for all 20. Across the whole file, 22 never cites Exhibit THIRTY or ONE; the only "Exhibit" is the title line. The only calculations are the generic identity 16² − 15·17 = 1 in the closing and Collatz's "10²⁰" check, which comes from the field. 22 says: "nothing of it is re-said or argued again here. It is taken as given and deployed."

Why uncarried: the folder gives only the aggregate and "seeded draw". It gives no seed, no ids, no per-row reasons, and none of the three caveats (paraphrase of 21, #133, the two calculations). The three "in part" ids (136, 28, 51) are nowhere named.

---

## A2 — `ad6537e4bcd88ca20` (6 Oct 12:52Z)

**Asked:** a strict logic audit of Registry steps 1–68 against "follows from sentence 1 plus the binary rule alone". Each step was marked F, N, G or B. It was to give special attention to steps 2–3, 4–6, 8 vs 28/46, 12–13, 31–40, 42, 45–48 and 51–57 (arithmetic run in Python), and to try a shorter derivation. It was to return a 68-row table, counts, the minimal list of added givens, and for each given whether it can be derived.

| # | Item | Status | Where / note |
|---|---|---|---|
| 1 | Counts F 26, N 18, G 20, B 3 (steps 2–68) | (a) | Is_Or_Is_Not: "26 follow, 18 name what is already there, 20 add something, and 3 take one side" |
| 2 | The 68-line mark table | (c) | **C-5** |
| 3 | Steps 2–3: step 2 holds for the universe, not any set; step 3 follows; step 52 needs 2 general | (a), (b) | Is_Or_Is_Not table row "A set, any set"; C4, P3 |
| 4 | Steps 4–6: members changing holds only under reading R (changing said of each thing) | (a) | table row 1 ("Is, at one reading") |
| 5 | Steps 4–6: discreteness is not derived; counter-model with flips at 1/2, 3/4… or a dense order | (c) | **C-4**. The folder gives a different, conditional verdict |
| 6 | Step 8 vs 28/46: a universe-wide now is used while a common beat is excluded; compatible only if the now is the universe's own momentary | (a), (b) | table row "A now of the whole universe … the files say both"; concern 2; P1, C1 |
| 7 | Steps 12–13: 13 is labels; that both arms are inhabited and kind persists (23, 24) is not derived | (c) | **C-4** |
| 8 | Steps 31–40: reciprocity does not follow (counter-model a→b→c→a) | (a) | table row 3: "three things each arriving from the next are at every earlier step"; C13 |
| 9 | Steps 31–40: alternating-not-both does not follow (synchronous update fits 34–35) | (a), (b) | table row 6; C2 |
| 10 | "Parity" is a momentary's class in 40 and a form's value in 42 and 52 | (c) | **C-6** |
| 11 | Step 42: the proposed argument is valid only for a thing that is exactly one binary; counter-model of one thing cycling four forms; silence about a third form shows none derived | (a) in part | row "Two forms" and C7 ("a set of two is at four"); "forms are parities" is (c), **C-6** |
| 12 | Steps 45–48: the five things of step 46 are not shown exhaustive | (b) | C9 ("a list, not shown each thing … gathered; nothing added") |
| 13 | Steps 45–48: the internal three-form cycle counter-model; a fixed form is barred by step 4 and not by "beside"; step 49's "another's opening" is inside | (c) | **C-6** |
| 14 | Steps 51–57 arithmetic verified (16 ways; 4 one-to-one, 12 not; fixed joint forms 2,1,1,0; unique one-to-one map with none still) | (a) | Is_Or_Is_Not item 1 ("twenty-four, six and two"; "run again by this session and by the fresh reader") |
| 15 | Premises (a) two values, (b) next from one prior and one now, (d) no form still | (a), (b) | table rows 4, 7, 1; C3, C7 |
| 16 | Premise (c): carrying the prior whole equals one-to-one, derivable from 13 with all-or-none | (a) in part | table row 7 says "Of the living alone, carrying the prior whole gives it". The 13 derivation is (c): **C-6** |
| 17 | Premise (e): prior and now independent inputs; step 34 makes the other's now depend on the self's prior | (c) | **C-4** |
| 18 | Short derivation valid given turn-taking, two forms and change at each own momentary; it makes next independent of the other's now, so 35's arrival is idle | (a) in part | the deriving is offered in Is_Or_Is_Not; the "whatever the now is" overread is corrected in its header note and at C8. "35's arrival is idle" is (c) low: **C-6** |
| 19 | Minimal list of nine added givens, each with derivable or independent verdict and counter-model | (a) in part | The folder has its own nine rows. They differ: see **C-4** |
| 20 | G marks at steps 15, 18, 19, 23, 24, 36, 46, 48, 49, 51, 68 and what each adds | (c) | **C-5** (only in the 68-row table) |

### C-4 (A2 attention points and part (3)/(4)), verbatim

> 4-6. Members changing follows only under R; else members static, membership changing. "Sequentially" is analytic. Discreteness is not derived: the binary rule bars a partway form, not a partway time; flips at times 1/2, 3/4, ... or on a dense order satisfy 1-4. 27 repeats 5.

> 12-13. 13 is labels. 12: carrying as own now depending on own prior, binary, gives two arms; that both are inhabited and kind persists (23, 24) are not derived. Sentence 1's "both" gives two nonempty classes, not their basis.

> (e) prior and now independent: no step; 34 makes the other's now depend on the self's prior, leaving two joint forms reachable in a two-thing universe.

> 2. Discrete, unbounded succession (5, 6, 10, 27). Independent: dense or accumulating flip times.
> 5. Carrying/not, both kinds exist, kind persists (12, 15, 23, 24). Partition derivable as at 12; persistence independent: a living thing dying.
> 9. Prior and now independent inputs (52). Independent: other's now a copy of self's prior.

Why uncarried:
- The folder's nine rows in Is_Or_Is_Not are: each thing changing; one momentary then a next; a self and its other; two forms; a now of the whole; the self and other in turn; a next from one prior and one now; a set, any set; which self releases to which.
- There is no row for kind persisting, for both kinds being inhabited, or for prior and now being independent inputs.
- The folder's row 2 gives a different verdict on discreteness: "Is, if a span with no changing in it is no existing thing". A2 says "Independent" and gives the dense or accumulating counter-model.
- I grepped the folder and the droplets for persist, dying, independent, discrete, dense and partway. Nothing relevant came back.

### C-5 (A2 part (1)), verbatim: the 68-row mark table

> R = reading "changing" as said of each existing thing, all-or-none distributing over a set that is nothing beyond its members.
> 1 P premise / 2 G every set a thing, not only the universe / 3 F from 1: universe exists, "all" includes it / 4 G changing extended to each member (F under R) / 5 B discrete momentaries vs dense/continuous / 6 N names three consecutive momentaries / 7 F from 6 / 8 G one universe-wide now, a cut across all things / 9 F binary applied to existing at a momentary / 10 G now depends on prior; alt: unrelated states / 11 F from 10, 8: all-or-none reaches each member / 12 G new relation "carrying"; both arms inhabited / 13 N living/non-living labels for carry/not / 14 N label stable-forming / 15 G non-carrier fixed jointly with others at now / 16 N lists sentence-1 terms / 17 N bi/co labels / 18 G assigns bi/co to kinds; "intelligencing" undefined / 19 G new members each momentary, never repeating / 20 F from 1: set is its things / 21 N "possible" names what arrives / 22 F from 21 / 23 G living at now is living at next / 24 G non-living passes nothing on; kind persists / 25 N prior/now/next relabeled places / 26 F from 4, 7, 10 / 27 F from 5, 9: nothing exists between / 28 G entraining across things; "own momentary" vs 8 / 29 N cut, place-moment / 30 F 8 at prior / 31 F from 11, 30 / 32 N coupling names arrival from another / 33 N self/other role labels / 34 B other from self first, or self from other / 35 G self's next from the same other / 36 G prior non-living; living needs others living / 37 G turn-taking; F only as dependence chain / 38 N opening/completing = source/target / 39 F from 34, 35, 38 / 40 N parity names classes S/O / 41 F from 14, 36, 37 / 42 G one thing = one binary; parity equivocation / 43 B method is a non-living thing, or none / 44 F from 43, 15, 24 / 45 F from 42, 43 (inherits 42) / 46 G "second method needs outside thing" unshown / 47 F from 1: nothing beside "all" / 48 G first clause F; "one possible" needs 46 / 49 G dichotomy unshown exhaustive / 50 N technology label / 51 G next a function of one prior, one now / 52 F from 42, 51: 2x2 / 53 F 2^4=16, verified / 54 F 4 one-to-one, 12 not, verified / 55 F three have fixed joint forms, verified / 56 F counts, cycles verified / 57 F unique one-to-one map, none still / 58 F cycle ++,+-,--,-+ / 59 F s^2 inverts both, s^4 identity / 60 N s=i, imported labels / 61 F s^6 = s^2; relation alternates / 62 N reverse order; "right" label / 63 F binary applied to changing / 64 N names self's next / 65 F from 63 / 66 N labels 65 "not-more-than" / 67 N labels 38 "once-ing" / 68 G cancellation of opposed arrivals; "accumulating"

Why uncarried:
- Only the four totals and nine merged rows are in the folder.
- The per-step marks are not. They are the evidence behind "Steps 69 to 661 were not read at this standard" (row C10).
- Several G steps (15, 18, 19, 23, 36, 46, 48, 49, 68) appear in no folder row individually.

### C-6 (A2 attention points), verbatim

> 31-40. Reciprocity does not follow: 34 is a chosen orientation, 35 adds return to the same partner; counter-model a->b->c->a. Alternating-not-both does not follow: 34-35 give the chain S(t-1)->O(t)->S(t+1), which fits synchronous update (both change every momentary, two interleaved chains). Turn-taking, "the self has no momentary at t", is added. "Parity" is a momentary's class in 40, a form's value in 42, 52.

> 42. Valid for a thing that is exactly one is-or-is-not changing at each own momentary: it alternates two forms. Gaps: "second is-or-is-not, so two things" equates a binary with a thing; a thing with two binaries is a thing (step 2; 52 uses it); counter-model: one thing cycling four forms. Silence about a third form shows none derived, not none existing. Equating forms with parities (40) is added.

> 45-48. Not shown exhaustive. Nothing derives that a second method needs an outside thing; an internal rule (a three-form cycle) needs no ground, container, clock or store. A fixed form is barred by 4 (a constant thing is inside), not by "beside". 47 follows; 48's second clause and 49 lean on 46; 49's "another's opening" is another existing thing's changing, inside.

> (c) carry whole = one-to-one: derivable from 13 with all-or-none (the eight partial ways are not all-or-none), unstated in 54; read as "depends on prior" the count is 12/4 reversed.

> Short derivation. Valid given: the self's consecutive own momentaries are prior and next (needs turn-taking; fails under synchronous update), two forms (G), change at each own momentary (R). It skips the sixteen ways and kills the three other carriers directly, dropping (b), (c), (e) but no other premise. It makes next independent of the other's now, so 35's arrival is idle.

Why uncarried:
- Reciprocity and turn-taking are carried (rows 3 and 6). The "parity" equivocation, the internal three-form-cycle counter-model for step 46, the "fixed form is barred by 4" point, the 13-derivation of premise (c) and the "35 idle" remark are not.
- Grep of the folder and droplets for equivocat, "three-form" and idle returned nothing.
- Improving.md lines 106–108 say "Three forms are set apart by nothing and are carried, by three selves". That answers the step-42 counter-model, not the step-46 one.

---

## A3 — `a5ebfb504043c439a` (6 Oct 00:36Z)

**Asked:** a sceptical fresh-reader review, before pushing, of the uncommitted "improving" pass in seven numbered points. These were the pacing script and the Kahn claim, the ring-of-inverters claim, the set-theory claim, finding 1's withdrawal, the standing table and the seven misreadings, the eleven carry entries, and the numbers.

Every item below is (a) unless marked. The two earlier readers' defects are said to be mended in Improving.md line 12 ("conceding too much at two findings and saying too much at several more"), and I checked each at its place.

| # | Item | Status | Where / note |
|---|---|---|---|
| 1 | Even rings: resolver and field part but text said they agree; "said ahead" false in time; N=1 or low-gain rests at mid-level | (a), (b) | Improving "At an even ring the resolver and the field part"; "Said by the field ahead of its measuring, and by the resolver after"; the mid-level remark is there, marked unopened; row E3 (b) |
| 2 | Pacing overstated ("each table is the same at each pacing … no beat is over the selves"): FIFO store, 0 as a distinct thing, rates locked, Registry steps joined | (a), (b) | Improving "Finding 2, narrowed" lines 65–86; Is_Or_Is_Not concern 2; droplet at Exhibit ONE offerings ("each order the waiting allows … a waiting place at each join"). "A self two release to waits for both is this session's joining" is stated. Rows P1, E1 open |
| 3 | "The answer was in the Registry each time, and in the white paper at none" is false (NI 2.2, 2.4, 1.5, 5.1, 1.3) | (a) | Improving line 34 and misreading 5; row N4 ("in passing or nowhere") |
| 4 | Finding 1: 2.4's test is not met at the cell; the withdrawal conceded too much | (a), (b) | Improving "Finding 1, withdrawn as a break, and what stays"; row P7 |
| 5 | Set theory: "V ∈ V" is NF, "kindred" misleads; the weakly compact premise; Natural Values' carrying already holds the concern | (a) | Improving "The second · the set" (positive comprehension, NF named, "a large cardinal", "Natural Values' carrying already has the parting … from v378") |
| 6 | "Regular rate": arXiv:2005.14694 is three different species; the "coupling" is this session's joining | (a) | row O6 ("this session's joining") |
| 7 | "The Registry names breaks ahead at four steps" | (a) | Improving lines 51 and 140 ("names the break's forms at one step") |
| 8 | "Brought ten observings … each met by the first" | (a) | phrase absent from folder and droplets |
| 9 | External quotes italicised as project text | (a) | Improving uses double quotes with "opened here"; droplets say "(Kahn, 1974)" without italics |
| 10 | Dates ("two days before" against the commit date) | (a) | Improving line 16 "the session closed the day before" |
| 11 | README "each tagged with its standing now" false; At_The_Code §8 untagged | (a) in folder; ND for At_The_Code | README rewritten; At_The_Code is in `carryings/v383Op/`, frozen |
| 12 | Evidence gaps: 27 and 123 not returned by any script; "carry ONE each table's sequences" is a run against random openings | (a); ND for the carry ONE wording | `stable_forms.py` and `returned/stable_forms.txt` now exist; Improving line 94 |
| 13 | Smaller: breaks "3 and 4" should be "2 and 3"; "27 in a hundred"; released words "half" and "keeping"; Ready/Concern form of the carry entries | (a); ND for form | Improving line 18 "second and third"; droplet reads "the risk of death by 27 per cent"; "half its delay" absent. "keeping" still appears at Improving line 45 as 1.4's own word. The carry-entry form is superseded by droplets |

Nothing uncarried from A3 beyond the "spiral rows are vacuous (one sender)" remark, which is implicit. The folder restricts the "whatever has arrived" figure to "toruses and crossed spirals" (README and Improving). `returned/own_momentaries.txt` shows spirals alike at 120 of 120 under both rules.

---

## A4 — `a8c799c4c483c201d` (6 Oct 01:11Z)

**Asked:** to verify the mended write-up against 11 specific checks: pacing numbers, even/odd rings, finding 1, set theory wording, the seven misreadings, break numbering, `stable_forms.py`, dates, table vs README, labels against the Ready/Concern rule, and anything else.

Improving.md line 12 states "the second read the mended writing and brought fourteen smaller defects. Each is mended here". I spot-checked each.

| # | Defect | Status | Where |
|---|---|---|---|
| 1 | TWENTY-SIX entering sentence cites a file that lacks the breaks | (a) | No droplet today contains "universal claim's open file" |
| 2 | `own_pacing.py` docstring says SUPERSEDED (pre-mend overshoot) | (a) | docstring in `carryings/v383Op/own_pacing.py` no longer says it |
| 3 | "4.13's sentence is borne at the second way" | (a) | README and Improving say instead "no pacing with both"; Improving line 84 |
| 4 | "Registry says each plainly" counts misreading 2 | (a) | Improving line 34: "says five plainly; of the second it says an opening at a completing, of one self and one other" |
| 5 | NI 4.10 and 5.1 do say the universe is an existing thing | (a) | Improving misreading 5 and line 34 |
| 6 | "once, in passing" | (a) | now "a sentence said in passing" without "once" |
| 7 | "Five findings among the thirteen" | (a) | Improving line 18 "Four of this session's findings" |
| 8 | Table row 27 | (a) | Improving line 61 "incoming at four files, ready and mechanical at two" |
| 9 | Labels against the Ready/Concern rule | (a) by supersession | carry entries became droplets |
| 10 | Dates | (a) | "the session closed the day before" |
| 11 | "each order of the selves" | (a) | "each order the waiting allows" |
| 12 | Odd-ring wording "alike" | (a) | Improving: "An odd spiral opened with one like pair…" and "opened with each self alike is again at 2 delays, a form a made ring does not hold" |
| 13 | Italic sentence attributed to GIM 5.3 and NM 6.1 | (a), ND | droplet and row P5 name both; I did not re-grep the Improving "Smaller" wording |
| 14 | Step 246 quoted as "a coupling among them" | (a) | Improving line 79 and row O6 give "a clock over them or a coupling among them" |

No (c).

---

## A5 — `a6abd15a30b91cba8` (6 Oct 15:05Z)

**Asked:** to check `Unresolveds.md` and its 22 droplets at 41 placings. Citations (25 or more spot-checks), the partings against v382A's tests (same subject, relation, scope, momentary), duplicates and gaps, counts, droplet form and quotes, the "earlier droplets" table, the "common way of working", and `carry_check.py`.

| # | Defect | Status | Where / note |
|---|---|---|---|
| 1 | D1 not at Natural Physics' offerings; opening words of rows 1, 3, 5; the "none is first" wording rests on a step about scales | (a) in Unresolveds; a residue is (c) | Unresolveds "earlier droplets" table now names the GIM, LFR and Arriving offerings and says "which is of scales and not of a first in time; that withdrawal is taken back". Improving.md still says "withdrawn here" and "the files say none is first": **C-10** |
| 2 | "Every row is at a droplet": P8 and F3 have none; P8 overstated (At_The_Code line 72 says 3.5 "rightly") | (a) | P8 now reads "beside 3.5, rightly said … The two may be of different subjects"; F3 "gathered at the Living File Registry". The intro no longer claims every row has a droplet. ND whether P8 has one |
| 3 | README "Twenty-two droplets" vs 24 distinct | (a) | README now "Fifty-three droplets … ninety placings" |
| 4 | P2 and D4 take step 307 as one subject | (a) | P2 row quotes 307's own separation, "for following first" |
| 5 | E2, D7, D3: the no-common-now rest called the break's own form | (a) | E2: "a rest like the break's form, though at this arm a self with nothing arriving opens no momentary" |
| 6 | D17 (R1): "a thing found the same is … a living self" widens NI 5.3's extent | (c) low | R1 is released, but the sentence remains at Is_Or_Is_Not item 4: **C-11** |
| 7 | C8 and D14: "nothing of the other is in the self's next" vs Registry 609 | (a) | C8 row "Corrected at Meeting_v382A.md … the prior is the other's"; Is_Or_Is_Not header note |
| 8 | C3 and D12: "each existing thing" vs step 51 "at a living thing" | (a) | C3 and table row 7 "of the living, carrying the prior whole gives it" |
| 9 | P3 has no one-subject hedge | (a) | P3: "Whether the sentences are of one set and one relation is for following first" |
| 10 | E4 and D24 cite NI 5.4 only; "incompetent for" is at 6.4 and Registry 155, 491 | (a) | E4 place now "Natural Intelligence 5.4 and 6.4; the Registry 155, 185, 239, 253" |
| 11 | "Common way": item 3 omits "at the file's own motion"; item 4 "an insertlet"; item 6 "largest first"; item 2 lacks the branch and commit | (a) | all four fixed in the text; commit `f64a5f6` given |
| 12 | Finding 22 (hydrogen sulphide) has no row | (a) | row O10 |
| 13 | C1 repeats P1; C6 repeats P3's first side | (b) | still two rows, cross-referenced ("one thing with P1"; "it turns on P3's first side") |
| 14 | Vague places; D23 says "three files" but omits Registry 311 | (a); ND for D23 | O3 to O5 now name sections; F2 path given; P5 row cites 311. The droplet at the Natural Intelligence offerings now says "The Co-Chaining Logic Registry says the older with this file". I could not match it conclusively to D23 |

---

## A6 — `ace47188aa591783d` (6 Oct 13:22Z)

**Asked:** to check Is_Or_Is_Not.md, `observer.py`, `no_common_now.py`, the README section and the five carry entries. That meant sums, script fairness, the three derivings, twelve or more quotations, whether "forbids no measured sameness" is the write-up's own reading, the 255/257 count, and the cryptobiosis trilemma.

| # | Defect | Status | Where / note |
|---|---|---|---|
| 1 | "Eighth break met" contradicted by steps 306–308 and NI 5.3 | (a), (b) | Is_Or_Is_Not concern 3 and "Not resolved: the expedition's eighth break"; header note; row P2 |
| 2 | "Forbids no measured sameness" is its own reading; the files say otherwise | (a), (b) | item 2: "this session's own reading … against 1.4"; row P4 |
| 3 | The observer restates the rule handed to it | (a), (b) | item 8: "That is the rule applied and no discovering of it"; row E4 |
| 4 | Cryptobiosis trilemma omits the fourth reading (a living self at 0 carried inward, steps 399–401) | (a), (b) | concern 1 now lists four sayings including both; row O1 |
| 5 | "Four can be had" followed by three derivings; concern 3's five differ from the table's; row 6 "follows if no common now" never derived | (a) | text now "Four are had … Three shorter derivings"; concern 4 matches the table's five; row 6 now "Is not" |
| 5b | Measured counts of a self changing twice with no change of a self it releases to | (c) | **C-7** |
| 6 | Deriving (c): "says nothing of its society" | (a) | now "but how many changings it is at … joins, opening, and which changing is before which" |
| 7 | Concern 2 row 3: spread comes from one global random order; "opened by a parity arriving and by nothing else" omits each self's first momentary | (a) | "by the order drawn, the selves' numbers the same at two orders at none of 100"; "after each self's first momentary" |
| 8 | 255 vs 257 | (a) | "TWENTY-TWO holds two more, at numbers TWENTY-ONE retired" |
| 9 | "A fresh reader … found nothing said that could be otherwise" over-generalises 20 entries | (a) | now "Of twenty entries drawn"; sentence absent from droplets |
| 10 | README vs Limits contradictions ("read by one fresh reader"; "four" vs three derivings) | (a) | README limits and Is_Or_Is_Not Limits agree |
| 11 | Confirmed sound: "goes on" is not overstated at 200,000 changings; exhaustive delivery orders | (c) | **C-7**. The folder gives the 4000-changing bound only in `returned/no_common_now.txt` |

### C-7 (A6 §2.5 and the "Confirmed sound" list), verbatim

> "Goes on" is not overstated. At 200,000 changings none of 30 non-alike openings each (torus 2 by 3, crossed 3 and 5, spiral of 5) came to rest.
> By exhaustive search over all delivery orders, no non-alike ring of 2 to 6 can reach rest. A torus 2 by 2 search with capped queues found none either.

> Table row 6, "Follows if there is no common now", is never derived. In `no_common_now.py`'s own queues, my rerun found a self changing twice with no change of a self it releases to between: 3,692 of 14,689 pairs on a spiral of 3, 4,271 of 18,170 on a spiral of 5, 18,229 of 38,612 on a torus 2 by 3.

Why uncarried:
- The folder states "changing goes on … from each opening but one kind" and "332 of 332", and its only evidence is a run bounded at 4000 changings. I grepped the .md files for 4000, 4,000, 200,000 and "every order". Nothing was found.
- The 200,000-changing and exhaustive-order results turn a bounded run into a stronger statement for rings of 2 to 6 and the other cases tested.
- The 3,692, 4,271 and 18,229 pair counts support row C2 ("which is first among changings not so joined"). They are not in the folder.

---

## A7 — `aa6cd02ae2f419813` (6 Oct 20:11Z)

**Asked:** to check `Meeting_v382A.md` against v382A's own files: attributions and double-quoted phrases, every number against `returned/meeting_v382A.txt`, item 5's short argument for validity, the "claim at its largest" section, whether parts 3 and 4 of the script implement the stated conditions, and anything else.

| # | Defect | Status | Where / note |
|---|---|---|---|
| 1 | "Same link … reached separately" | (a) | line 23 ("Two readings are tried as both, and neither is called a refutation"); Limits line 121 records the overstatement |
| 2 | v382A's question quoted in part and called "executed" | (a) | line 38 gives it whole; "The executing does not answer it" |
| 3 | "That is the first of v382A's two readings" | (a) | removed (grep finds only line 23) |
| 4 | "The files' sentences" for three conditions that are this session's wording | (a) | lines 63 and 75 "each this session's wording" |
| 5 | "Bound met at one to four others" | (a) | line 87 "met at one to four others and not reached at five and six; stepped together no self is kept more than once" |
| 6 | Item 5's argument: nonzero sharings only; unstated premises (nothing waiting at the opening, none from beyond the k) | (a) | line 87 now states the premises |
| 7 | "Claim at its largest" overstated ("enlarges the claim and reduces none of it") | (a) | line ~100 "offered to v382A's pass and not yet read by it … a count of 1,296 cells against three conditions this session chose is not one" |
| 7b | Extra simulations: 853 of 11,938 selves exceeded k+1 with preloaded queues, and 0 violations in 13,755 selves without them; random one-sender graphs 0 failures in 462,784 entries | (c) low | **C-12** |
| 8 | "Exact wherever one releases to a self" run only on small cases | (a) | now "Joins drawn among 5 to 8 selves … 101 societies" and "stepped together" |
| 9 | Evidential weight (304 counted twice; 76 matches true by definition) | (a), ND | "the weight is the openings and societies"; "two selves both ways are the spiral of 2"; "A count at small societies establishes nothing at each society". ND whether the by-definition remark is carried |
| 10 | "Each count given alone and together" not so | ND | |
| 11 | "The nets differ in mesh, not in aim" | (a) | phrase gone |
| 12 | Minor characterisations (125, Natural Destinies, runtime) | (a), ND | runtime now "about two minutes" in both; others not re-checked |
| 13 | Limits omit sizes and windows | (a) | Limits line 122 now states them |

### C-12 (A7 item 6 and item 8), verbatim

> Test: with preloaded queues, 853 of 11,938 selves exceeded k+1 (e.g. joins {0:[2],1:[],2:[],3:[4,0,2],4:[3,2,0]}, preload {1:[-1,-1]} gives run 2 at k=0). Without preloading, async entry, self-loops allowed: 0 violations in 13,755 selves.

> Extra test: random graphs, one-sender selves, stepped together, 0 failures in 462,784 entries, so likely true under stepping together.

Why uncarried: Meeting_v382A.md line 87 states the premises (nothing waiting, nothing from beyond) but gives neither counterexample counts nor the corroborating count. Low value.

---

## A8 — `a46b3fadab9193e64` (6 Oct 22:36Z)

**Asked:** to check the second writing of `Network_Surface.md` and its script for something v383Op had twice before presented as its own that the repository already held. That meant searching for earlier statements of five findings, checking quotations, every number against the script output, the script's parts 3 and 4, and overstatement.

The folder now holds a third writing of Network_Surface.md. It has dropped the own-turn-equals-beat finding, the hole run and the torusing remark, and its foot lists what is released. Most of A8's defects are therefore moot or mended.

| # | Defect | Status | Where / note |
|---|---|---|---|
| 1 | The "whatever has come" arm still delivers the 0; "0 of 600" is a scheduler artefact | (a) in this file; (c) elsewhere | The claim is gone from Network_Surface.md. The same kind of arm survives at Improving line 84 and Is_Or_Is_Not concern 2 ("0 to 10 of 120"): **C-8** |
| 2 | "Answers a question the file's offerings hold open" overstated; the run supplies the queue and store the repository sets aside | (a), (b) | row E8: "Narrowed by a run and not answered … whether one sharing resting at a coupling is the store it sets aside … a completion counter". Released as a saying of the surface |
| 3 | "Or nothing … is the file's own sentence" over-read; the identity already at NI 1083, 1018 and Registry 212, 231, 610, 611; counts already in `two_lines.txt` | (a) | foot: "What the two writings carried that is at a file already is at that file: a 0 shared as its self still possibling, at Natural Intelligence and the Registry" |
| 4 | The "already in the repository" pattern recurs; near-miss addresses not cited | (a) in part, (c) | R61 and R62 are at row E9; E6 cites Natural Networking 6.12. The rest are **C-9** |
| 5 | Part six models the hole as a delivered 0 | (a) | row E9: "Released as a saying. The test entered a resolver absent as none offered"; E8: "at a self absent, each run stops" |
| 6 | "Change spreads … from none to nearly every present self" | (a) | E9: "at the others from one self to most" |
| 7 | "The two surrounding paths of the file's study" mischaracterised | (a), moot | claim removed |
| 8 | "The file does not say its surface closed" too strong | (a), moot | removed. The current file says only that the 2-D surface is not closed |
| 9 | "Torusing" twenty-seven times, "torus" at none | (a), moot | removed. Nothing equivalent in the folder |
| 10 | Table row 1 does not match 6.12's setup | (a) | E6: "a trace of the same form is already at Natural Networking 6.12, one finite study of two selves at one opening and one order … with its bound" |
| 11 | "Defect = like pair/possibling" loose | (a), moot | removed |
| 12 | "The travelling part is the 0" asserted, not run | (a), moot | removed |
| 13 | "Collective … at the common beat" vs step 46 | (a), moot | the file now says "Still possibling is abundancing: is, as one side of it" |
| 14 | Smaller (eleven momentaries off by one; "787 sentences"; docstring minutes) | (a) | docstring now "about a minute"; other claims removed |

### C-8 (A8 defect 1), verbatim

> In network_surface.py the 'any' arm still delivers the 0. Lines 142-143 append o to waiting[to][s] unconditionally. The cell treats [0] the same as [] (checked: entry(c,[0]) == entry(c,[]) for both parities). The two arms differ only in readiness (wait for one release from each side, or open on any pending one). They do not differ in whether the nothing is an arrival or an absence.
> "Another network at every run" really means "differs under every one of the random orders drawn". I re-ran the 'any' rule with every self opening once per round in shuffled order: 600 of 600 equal the beat. Under the script's random choice the 'any' arm still matches about 47% of entries, and first diverges at momentary 2 to 7. So 0 of 600 comes from the random scheduler plus an all-or-nothing comparison, not from "another network".
> I also ran a genuine absence arm (0 not queued). 'any': 0/600 equal and only 453/600 complete. 'each': 106/600 equal, and 74 runs stall. That arm is not what the file ran.

Why uncarried:
- Network_Surface.md no longer claims the 0 of 600, but Improving.md line 84 still says "opened at whichever arrives, the sequences are Exhibit ONE's at 0 to 10 of 120".
- `own_momentaries.py` (docstring line 21) describes the same kind of arm: "opens at whatever has arrived when the pacing reaches the self".
- The shuffled-round 600 of 600, the 47% and the 0 of 600 diagnosis are carried nowhere.
- **ND:** whether the artefact transfers to `own_momentaries.py`'s 0-to-10-of-120 figure. A8 tested only `network_surface.py`.
- Row E8's "106 of 600 where a 0 is not laid" (not in A8's genuine-absence arm, which has its own count) does match A8's 'each' figure of 106/600.

### C-9 (A8 defect 4), verbatim

> (A1) own turn vs one beat, no earlier statement of the exact finding. Near-misses not cited:
> - v380A: offerings 151 ("A changed-arrival-only driver suppresses that continuing"); Surface_Construction.md:23.
> - Exhibit_TWO 6.2 line 959: "Taken front-first, the sequences run on at all three selves; taken back-first, one self opens once and never again; taken at random, a third pattern arrives".
> - carry/Session_Record.md:215 (R60): "the order within a momentary carries nothing, 150 comparisons".
> - v383Op's own earlier carryings/v383Op/At_The_Code.md:120-143 (own_pacing.py, one self at a time, "at each of the four pacings … neither relation is carried").

> (A3) hole with signs flowing at an open 3x3. … Also offerings line 65, and carry/Session_Record.md:215, 255, 257. … v380A, Perturbing_Cases.md:43/45: "No zero entry is manufactured to stand for the absent join"; Surface_Receiving_Map.md:33: "The missing entry is not a zero substituted for a quiet release". The script does that substitution (`0 if u == absent`).

> (A4) second momentary read off the opening: Registry 651 (line 2860) says it for alternating openings … Part Five and droplet 3 do not cite it. Generalising to all 4,672 openings and "settles within 11" are new.

Verification and status:
- I confirmed these addresses.
  - Exhibit TWO line 959 contains the quoted sentence.
  - Session_Record line 215 contains "the order within a momentary carries nothing, 150 comparisons at a society of seven (R60)".
  - Surface_Receiving_Map.md line 33 contains "The missing entry is not a zero substituted for a quiet release".
  - Registry step 651 is at line 2860.
  - The "No zero entry is manufactured…" sentence is at Perturbing_Cases.md line 41, not 43 or 45.
- Not carried:
  - The folder's E8, E9 and N12 name Natural Networking 6.12, v380A's Surface_Arriving_Plan and R61/R62.
  - They do not name Exhibit TWO 6.2's front-first, back-first and random sentence, Session_Record R60, the two v380A files, or Registry 651.
  - `grep` of the folder for "front-first", "651" (outside F2), "R60", "Perturbing" and "Receiving_Map" finds nothing relevant.
- These are exactly the "address for work already gathered" that v382A's method asks for.

---

## A9 — `a2e26283b2346fdd4` (6 Oct 22:16Z)

**Asked:** an extraction, with no evaluation. It was to quote verbatim, with line numbers, every sentence in `Exhibit_TWO_Natural_Networking_v371.md` lines 1–770 in categories A to F (surface, what passes between selves, not-changing, numbers and runs, society, open or unsure). It was then to list what the text names that it relies on, and to give a 12-sentence summary of Part One. The final report is a list of 463 machine-checked quotes plus those two closing parts. It is not a findings report.

| # | Observation in the report | Status | Note |
|---|---|---|---|
| 1 | "mesh" does not occur; "torus" only as "torusing" and "corusing"; "wrap" only in the contents (line 129); "ring" at 135, 451, 636; "geodesic" at 7 and 208 | (c) low | The folder carries Natural Networking's "older words" (Network_Surface.md line 80) but not these word counts. The torusing 27 and torus 0 counts A8 gave for the second writing are gone |
| 2 | No other file, exhibit, script or `.py`/`.md` is named in lines 1–770; "Python code or expression" is unnamed; the only unlabelled computed table is lines 491–494 | (c) low | not in folder |
| 3 | Forward references only to Part Four to Part Six instruments, not described in lines 1–770 | (c) low | not in folder |
| 4 | The text itself flags as open: the correspondence of the fifteen prime lengths with the network (443, 447), whether "fold" and "scatter" exhaust the breaks (701), the "proposed" hole-mending route (608–620) | (c) low | the folder's rows E8, E9 and N12 are about the surface and the nothing, not these |
| 5 | 12-sentence summary of Part One, with "unsure" marks | n/a | an extraction of the repository's own text |

I judge A9 to carry no defect or suggestion of its own. Every item is a report of what Exhibit TWO says or does not say.

## A10 — `ae68c5e9303059f03` (6 Oct 22:16Z)

**Asked:** the same extraction for Exhibit TWO lines 771–1109, `carry/Exhibit_TWO_Carryings_of_Natural_Networking.md` (55 lines) and `carry/Exhibit_TWO_Offerings_to_Natural_Networking.md` (231 lines). It was to give the structure of the Offerings file: sections, insertlets and the sections each is aimed at, droplets by session tag. It was to list what each file relies on and to summarise. This too is an extraction report, not a findings report.

| # | Observation | Status | Note |
|---|---|---|---|
| 1 | Offerings structure: 25 insertlets (aimed at 1.1, 1.2 ×8, 1.3 ×2, 1.4, 1.6, 1.8, 3.1, 4.2, 4.7, 4.8, 5.1, 6.1, 6.2, 6.3, 6.5, 6.10, 6.12); 84 droplet paragraphs by tag (v373 ×3, v375 ×1, review 2026-09-30 ×2, v380A ×2, v380R ×3, resettling_v373 ×21, v368_sources ×39, illustrating_v366 ×5, v381R scan ×7, v381R close ×1) | (c) low | **C-14** |
| 2 | Line 231 says "46 droplets"; that matches 84 minus the 38 "re-aimed from" other exhibits' Offerings; several texts repeat, so there are 70 distinct texts | (c) low | **C-14** |
| 3 | The living file contains none of the ring-size runs (rings 3–16, 131,064 seeds, 32,764 seeds, ring of 59, 26 windows); they are only in the Offerings (lines 183, 191) from Kit_Exhibits_ONE_and_TWO_v365.md | (c) low | **C-14** |
| 4 | Part Six's six hidden clocks (pace, running order, record, membrane, taking, refusing) and its only numbers (19 carryings within 6 receivings; the 440 form with waist at 220; each added self adding 220; ring parity) | n/a | repository text, not a finding |
| 5 | The carry files' own open items: order-invariance by construction at 6.9; the 2.3 sentence found in no file; whether a membrane whose far side is the whole counts at the surplus's meeting; the counting-register passages at 4.1–4.3; the kit's engine being the old code; the v380A candidate having "no authority"; the unresolved own-turn vs one-beat question; the "quiet releasing" question | (b) in part | own-turn vs one-beat and the zero at the release are row E8 (open); the rest are the repository's own open items, carried at those files |
| 6 | Unsure items: the 440-fold (441 less n vs 440 less k), four-versus-six protections, the along-join arrangement at a hole | n/a | repository's own open items |

### C-14 (A10), verbatim

> DROPLETS: 84 paragraphs, odd lines 65 to 231. … Line 231 says "46 droplets"; that matches 84 minus the 38 paragraphs "re-aimed from" other exhibits' Offerings at v381R (lines 141-215). The 46 originals are lines 65-139 (38, all prefixed "A plan, not yet final, gathered here at v381R:") plus 217-231 (8). Several texts repeat (same text at 87/153; 93/143/155/215; 99/209; 103/159; 113/163; 115/121/167; 125/139; 129/141; 131/193; 135/199; 149/211), so there are 70 distinct texts.

> The living file contains none of the ring-size runs (rings 3-16, 131,064 seeds, 32,764 seeds, ring of 59, 26 windows); those are only in the Offerings (lines 183, 191) and come from Kit_Exhibits_ONE_and_TWO_v365.md.

Status:
- The folder mentions none of this. It is housekeeping for the Exhibit TWO offerings and carryings, not a v383Op claim.
- **ND:** I re-checked the file today. It has 235 lines and 86 paragraphs from line 63. Exact-text duplicates are only lines 115/121 and 125/139. The other pairs A10 listed differ in their prefix. A10's "70 distinct" is therefore not reproduced; I find 84 distinct.

---

## The five agents with no report (all died on "API Error: 529 Overloaded")

| Agent | Asked | Result |
|---|---|---|
| `a129eaf5b5d481cc9` and `ab664d50150fd1cd2` | the Exhibit 21 vs 22 audit (A1's task), found by filename glob | no report, nothing to compare |
| `a3d287ba4d38441cc` and `acfaf8021f372fbb8` | the 68-step logic audit (A2's task), found by filename glob | no report |
| `afab8e2521a76d927` | an earlier version of A2's audit, "opening steps" | no report |

---

## Consolidated list of (c) items, most valuable first

1. **C-1 (A1).** 22 itself says field arrivals "stand open" in the field's sense (Fermi, graph isomorphism, Riemann, Hodge, BSD, Yang–Mills, substorm, water's critical point, the closing) and that a resolving "settles nothing". It also lists 14 entries with open wording. It bears directly on "fully resolved". The folder carries only the general sentence. All 13 phrases confirmed in the 22 file today.
2. **C-2 (A1).** 21 records five problems as settled by the field (#151, #166, #5, #6, #51). 22 treats two of them as settlings "real in its own register" and its front counts four, locates three, and leaves the fourth at "no entry still". It is the one place where 21's "except where the record settles one and the entry says so" is tested. Confirmed in both files.
3. **C-4 (A2).** Three of A2's nine givens have no row in Is_Or_Is_Not: kind persists and both arms are inhabited, prior and now are independent inputs, and discreteness. For discreteness the folder's verdict ("Is, if…") differs from A2's ("Independent": dense or accumulating flip times). It changes the folder's "four are had, five stay".
4. **C-3 (A1).** The marker cannot discriminate (identical at 3.22, which 22 says "takes no parity anywhere"). 22's front names a "0 at 10" release that no entry uses. Partly (b) by reference at Meeting_v382A.md line 43, as v382A's own relation with "no row here".
5. **C-7 (A6).** Evidence strengthening "goes on": 200,000 changings on 30 non-alike openings each, exhaustive delivery orders for rings of 2 to 6, and the pair counts (3,692 of 14,689; 4,271 of 18,170; 18,229 of 38,612) behind row C2. The folder carries only the 4000-changing bound.
6. **C-8 (A8).** The 'any' arm still delivers the 0 and differs only in readiness. Shuffled-round order gives 600 of 600, and the 0 of 600 is a scheduler artefact. **ND** whether the same holds for the "0 to 10 of 120" at Improving.md line 84 and Is_Or_Is_Not concern 2.
7. **C-9 (A8).** Addresses already in the repository for E8, E9 and N12: Exhibit TWO 6.2 line 959, `carry/Session_Record.md` R60, v380A Perturbing_Cases line 41 (A8 gave 43/45) and Surface_Receiving_Map line 33, and Registry 651. Verified.
8. **C-6 (A2).** The "parity" equivocation (steps 40, 42, 52), the internal three-form-cycle counter-model for step 46, "a fixed form is barred by 4, not by beside", the derivation of premise (c) from step 13, and "35's arrival is idle" under the short derivation.
9. **C-5 (A2).** The 68-row per-step mark table. Several G steps (15, 18, 19, 23, 36, 46, 48, 49, 68) appear nowhere individually. It is the evidence under C10.
10. **C-10 (A5).** Improving.md row 23 still says "withdrawn here" and line 32 still says "the files say none is first". Unresolveds' "earlier droplets" table takes that withdrawal back (the step is "of scales and not of a first in time"). The two files disagree and Improving.md is untagged.
11. **C-11 (A5).** Is_Or_Is_Not item 4 still says "a thing found the same is, at Natural Intelligence 5.3, *the self at the between, its carrying continuing, a living self*". A5 says NI 5.3 says that of a living self at 0, and NI 1.3 gives a non-living thing a stable form carrying none. A5's replacement is "a living self found at one parity". Low.
12. **C-13 (A1).** Low items: structure counts, the sample's seed, ids and per-row a to d reasons (including which three are "in part": 136, 28, 51), the three caveats (paraphrase of 21; #133; 16² − 15·17 = 1 and the Collatz check), and 21's and 22's longer definitions.
13. **C-12 (A7).** Counterexample and corroboration counts for the bound at item 5 (853 of 11,938 selves with preloaded queues; 0 of 13,755 without; 0 of 462,784 on random graphs). Low.
14. **C-14 (A10) and the A9 notes.** Structural observations about the Exhibit TWO offerings and word counts of Exhibit TWO. Housekeeping at the repository, not claims.

**Could not determine:**
- (i) Whether A8's 'any'-arm artefact transfers to `own_momentaries.py`.
- (ii) Whether D23 (A5 item 14) is exactly the droplet now at the Natural Intelligence offerings that cites Registry 311.
- (iii) A3's per-entry replacement wordings, since the eleven carry entries no longer exist in that form.
- (iv) A7 items 9 (by-definition remark), 10 and 12 in part.
- (v) Whether A10's "70 distinct texts" figure can be reproduced. Today I find 84 distinct.
