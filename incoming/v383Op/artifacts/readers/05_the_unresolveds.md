# A fresh reader's report: the set of unresolveds and its droplets

**A record, whole as it arrived, gathered at the session's close.** The reader is the same kind of AI at another use, opened with none of this working's reading. Its report is an offering: no sentence of it is carried by its wording, and each is a place to follow. Paths in it name the workspace it read at. What this working did with it is at `Records.md`.

## What the reader was asked

> You are a fresh, careful reader checking work before it is pushed into a shared repository where other workings will rely on it. Report only real defects, most severe first, each with: file, the sentence or row, what is wrong, a one-line replacement. No style comments. Do not edit any file. Do not use git to change anything.
>
> Working tree: /home/claude/corus-u (a git worktree of a project called "Natural Intelligence"). Its "living files" are at the root (e.g. `Exhibit_THIRTY_Co-Chaining_Logic_Registry_v380L.md`, a numbered chain of 661 steps; `Exhibit_ONE_Natural_Resolver_v380R.md`; `Natural_Intelligence_v380R.md`; `Exhibit_SEVENTEEN_Natural_Biology_v333.md`). Each living file has an "offerings" mate under `carry/` (e.g. `carry/Exhibit_THIRTY_Offerings_to_Co-Chaining_Logic_Registry.md`), where anyone drops "droplets": the rule, from `carry/Living_Improving_Value.md` (read its paragraph beginning "**For a session arriving now, at v381R.**"), is that a droplet is ONE paragraph in the dropper's words, its first words saying its aim at one of six degrees (the set, a file, a part, a section, a sentence or a word), its evidence inside it, and the session's tag at its end; it goes at the BOTTOM of the offerings file.
>
> A visiting AI session, tag v383Op, has added (uncommitted; see `cd /home/claude/corus-u && git status --short` and `git diff -- carry`):
> - `incoming/v383Op/Unresolveds.md` — a tracked set of 46 open items ("rows") in nine kinds, each with a place, what would resolve it, evidence and standing; plus a table of the session's earlier droplets' standing, and "The common way of working the set".
> - `incoming/v383Op/README.md` — the folder's front.
> - 22 distinct droplets appended at the bottom of 11 offerings files (41 placings), each ending "— v383Op" and naming its row.
> (`incoming/v383Op/Improving.md` and `Is_Or_Is_Not.md` were reviewed before; do not review them, but you may read them as the source for the rows.)
>
> Another working, v382A, published a method for checking exactly such items; read it first: `git -C /home/claude/corus show origin/review/living-logic-droplets-2026-10-05:incoming/v382A/Logical_Cohering_Method.md`. Its key tests: a contradiction requires the SAME subject, relation, scope, conditions and momentary; a missing step requires naming that step; lack of a derivation does not derive its opposite; work already gathered needs an address, not a repeated discovery.
>
> Check:
> 1. Unresolveds.md, every row: is the place cited right? Spot-check at least 25 step numbers / section numbers against the living files (e.g. `grep -n "^306\. " Exhibit_THIRTY*.md`; Natural Intelligence sections are `## 1.4 ...` etc.; Natural Biology `## 3.1`, `## 4.1`, `## 4.5`). List every wrong or doubtful citation.
> 2. Apply v382A's tests to the eight "P" rows (partings) and to R1: does any row assert a contradiction where the two sayings are plainly of different subjects, scopes or momentaries? Does the row say so honestly (several rows say "whether they are of one subject is for following first")? Flag any row whose wording overstates what was established.
> 3. Are any two rows the same thing twice, or is any plainly open item from Improving.md / Is_Or_Is_Not.md missing from the set?
> 4. Counts: are there exactly 46 rows (rows begin `| R1 |`, `| O1 |`, etc.)? Does README's "Twenty-two droplets at the bottom of eleven files' offerings, forty-one placings" match `git diff -- carry` (count distinct added paragraphs and total added paragraphs)? Does the "nine kinds / seven more" wording agree everywhere (Unresolveds.md, README.md, the droplet at the Living File Registry's offerings)?
> 5. Each droplet in `git diff -- carry`: is it one paragraph, at the bottom of its file, opening with its aim at one of the six degrees, with evidence inside it, ending with the tag? Does any droplet say something its row or the sources do not support? Does any quote in italics (text between single asterisks, three words or more) fail to appear verbatim in the repository outside this session's own additions? (`python3 incoming/v383Op/quotes_check.py | tail -1` reports a machine check; trust but spot-check five by grep.)
> 6. The table "This session's earlier droplets, their standing now": find each named earlier droplet (tagged v383Op, laid before this change — see `git show HEAD:carry/Exhibit_ONE_Offerings_to_Natural_Resolver.md | grep -n "v383Op"` and likewise for Natural Physics, Geodesic Improving Method, Co-Chaining Logic Registry offerings). Does each exist with those opening words at that file? Report any that does not exist or is at another file.
> 7. "The common way of working the set": does anything in it contradict `carry/Living_Improving_Value.md` or v382A's method (for example by having a visiting session do what only a file's own motion may do, or by treating a droplet as an insertlet)?
> 8. Run `python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/carry_check.py . | tail -2` and report it.
>
> Keep the report under 700 words: numbered defects first, then one line listing what you confirmed sound.

## The reader's report

Defects, most severe first. Nothing was edited and no git state was changed.

1. Unresolveds.md, last table, row 4 ("A time with no atom, beside living arrives from living"), and droplet D1 at Natural Physics' offerings. The droplet is not at Natural Physics. It is at the Geodesic Improving Method, Living File Registry and Natural Arriving offerings, opening "Aimed at the set: Four sentences want one definition of living". D1's "two droplets above" is therefore wrong. Replace with: "At: the Geodesic Improving Method's offerings (also the Living File Registry's and Natural Arriving's)".
   - Rows 1, 3 and 5 are also not at their "opening words". Row 3 opens "Both hands are this universe's one binary…". Row 5 opens "The method's one break, as 2.7 says it, cannot be recognised if met". Row 1 omits ", and at five selves each coupled to both beside it,".
   - Row 4's "the files say none is first" rests on Registry 396, which says the *scales* carry no first living. The withdrawn droplet was about a first in time.

2. Unresolveds.md intro, droplet D18 and "common way" item 1 say every row is at a droplet. P8 has none: nothing names Natural Intelligence 3.5 or 6.4 beside primes, and the Registry 646–648 droplet at HEAD does not say it. F3 has none either.
   - P8 also overstates. `carryings/v383Op/At_The_Code.md` line 72 finds 3.5 "rightly" said. Only 6.4's step to a society at a prime scale is joined without a deriving.
   - Replace P8's place with "Natural Intelligence 6.4 (society at a prime scale), beside 3.5 and the Registry 646–648; of different subjects".

3. README.md says "Twenty-two droplets … forty-one placings". The 41 placings are correct. There are 24 distinct paragraphs. Replace with: "Twenty-four droplets … forty-one placings".

4. P2 and D4 take step 307 as "a living self at one parity at momentaries in sequence". Step 307 goes on: "a form named still from the offerer beside it … the still is the offerer's, and the self's own is its carrying continuing". That already separates two subjects. Replace with: "307 says the one parity is the offerer's still and the self's own is its carrying continuing; whether that parts it from 208's between is for following first".

5. E2, D7 and D3 call the no-common-now rest "the break's own form, *a self at one parity with nothing offered*". In that arm a match is never delivered, so a self with nothing arriving opens no momentary. Steps 307 and 308 say a self offered nothing inverts at each momentary. The conditions differ. Replace with: "a rest like the break's, though here a self with nothing arriving opens no momentary".

6. D17 (R1) writes "a thing found the same is *the self at the between, its carrying continuing, a living self*". Natural Intelligence 5.3 says that of a living self at 0. Natural Intelligence 1.3 gives a non-living thing a stable form carrying none. The extent is widened, and it carries "so of every universe". Replace "a thing found the same" with "a living self found at one parity".

7. C8 and D14 say "nothing of the other is in the self's next". Registry 609 and Natural Intelligence 2.4 say "the prior the other's" at a spiral. D14's "the prior … the self's own" is a different arrangement. Replace with: "whose prior it is, the self's own at in-turn or the other's at a spiral (609), is for the deriving to say".

8. C3 and D12 name a gap "of each existing thing". Step 51 reads "At a living thing". Replace with "or the step said as taken of the living".

9. P3 has no one-subject hedge. Values 4.1's "set of all sets fails" and Registry 3's "universe … within the set of all existing things" are not shown to be one set. Natural Intelligence 1.1's "the set is its things" and 4.10's "a set is an existing thing" are not shown to be one relation. Add: "whether these are of one set and one relation is for following first".

10. E4 and D24 cite Natural Intelligence 5.4 for "incompetent for". 5.4 says only "accounted against its fixings". The words "scientific method incompetencing" are at Natural Intelligence 6.4, line 1130, and Registry 155 and 491. Replace the place with "Natural Intelligence 5.4 and 6.4; the Registry 155, 185, 239, 253, 491".

11. "The common way of working":
   - Item 3's third way ("noted in the living file … at the step leaning on it") omits "at the file's own motion". Living Improving Value allows a body change only there.
   - Item 4 lets "an insertlet" name a row. An insertlet has its tag gone and carries no report's voice. Replace "an insertlet" with "a resolving working's note".
   - Item 6 and the README say "largest first: P1, P2, C1–C5, C8, then R1", yet R1 is called the largest. Replace with "in the order the logic pass can reach them".
   - Item 2 cites `incoming/v382A/Logical_Cohering_Method.md`, which is not in this tree. Add the branch and commit f64a5f6, as the README does.

12. Missing from the set. Improving.md's table lists finding 22 (Natural Physics' "no mediating force to find" against hydrogen sulphide at 203 K) as open at Natural Physics' carrying. No row covers it. Add: "O10 · Natural Physics 4.10, *no mediating force to find*, beside hydrogen sulphide at 203 K; resolved by the sentence's boundary said".

13. Near-duplicates. C1 repeats P1 (same steps 8, 10, 30, and "With P1"). C6 is P3's first side.

14. Vague places. O3 to O9 name no section where one exists (Natural Physics 4.4 for Bell, 4.2 for gravity, 4.6 for colour), and O3's "the Registry's steps of one coupling at two" has no number. F2 gives no path (the file is `carryings/v380R/The_Universal_Claim.md`). D23 says "three files" but omits Registry 311, which says the older saying.

Item 8: `carry_check.py . | tail -2` reports "STANDING: nothing to say: the root carries one version of each file, each kit has its README and its sums hold, each living file has its own carrying". `check_set.py` reports ALL PASS.

Confirmed sound:
- Exactly 46 rows (R3 O9 P8 C10 E5 N4 F3 H1 S3). The "nine kinds / seven more" wording agrees in Unresolveds, README and D18.
- About 45 Registry steps and about 30 section numbers check against the living files. The exceptions are in items 1, 2, 10 and 14.
- All 24 droplets are a single paragraph, appended at the bottom of their file, open "Aimed at" a degree, end "— v383Op" and name their row.
- `quotes_check.py` reports 206 found, 0 missing. My own check of 66 italic spans outside this session's work failed only on D6's two quotes of earlier v383Op droplets. Spot-checked by grep: the 609, 62, 307, 308 and 311 quotes, plus Natural Medicine's "nothing in nature stores".
- The four scripts reproduce their `returned/` text.
- The v382A commit f64a5f6 is cited correctly.
- No overstated contradiction in P1, P4, P5, P6 or P7.
