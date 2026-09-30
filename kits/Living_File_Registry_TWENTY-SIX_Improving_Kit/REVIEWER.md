# The Reviewer

**A brief for any session reviewing the living files and the work on its way toward them**

The reviewer is an instrument of the expedition: a coupling partner and no authority. It says what it finds and decides nothing. It never writes a living file. What it brings arrives at `incoming/` as work arriving whole, and is met at the carrying like any other arriving (Exhibit TWENTY-FOUR, 2.8): each finding is or is not value at a file, entering whole at that file's section of `carry/Living_Improving_Value.md` or releasing to `archive/`, and written into its file at the file's own motion.

Another AI serves the expedition two ways: discovering and reporting back in, and, the other way, reviewing and improving the files. The work moves through the branches aimed at the living files in top condition, and the reviewer reads the files and the branches, finds its own hardest either-this-or-thats, and brings them for exploring and for improving the method.

This brief is the reviewer's own carrying. Each review ends with what the reviewer learned about reviewing, and that learning enters this brief through the same method, a motion at a time.

## Opening a review

1. **The repository.** `github.com/chris-j-handel/corus`. `git fetch origin` brings every branch; `git branch -r` lists them. A working branch is named `working/foundation-vNNN`, NNN the session's number; a merged motion is a pull request into `main`.
2. **The branch under review, checked out at its own folder.** `git worktree add ../review-<branch> origin/<branch>`, then work inside that folder: the kit's checks read the files checked out at it.
3. **The base.** `base=$(git merge-base origin/main HEAD)`: the words compared are those the branch added after its parting from `main`, and `main`'s own newer motions are no part of the branch.
4. **The review's number.** `<session>` is the reviewing session's own number or the branch's, `v377` for a review of `working/foundation-v377`, and the review branch starts from `origin/main`: `git switch -c review/<session> origin/main`.
5. **The commit read.** The report names the commit its review opened at and, at a longer review, each later commit it reached: other workings move the branch, and a finding is met at the files' newer motions, a finding already met at them being no second arrival.
6. **A visiting contribution.** A report from another working, discovering and reviewing at once, arrives the same way, at `incoming/review_<subject>_<session>/` on a branch `review/<subject>-<session>`, whole, its standing named at each event: offered on a branch, arrived at `main`, received at the carrying, entered at a file.

## What it reads

- **The branch's motions.** `git log --oneline $base..HEAD` lists them, one commit each, and `git diff --word-diff=plain $base HEAD` shows each changed word: each line of a living file is a whole paragraph, and a line diff shows the whole paragraph as new. The branch's own record of what each motion meant to do is its lines added to `carry/Session_Record.md` in that diff.
- **The core files whole, at a review of the core.** The stable form of all the files: Exhibit ONE (the code), Natural Intelligence (the white paper), Exhibit TWENTY (Natural Naming) and Exhibit THIRTY (the Co-Chaining Logic Registry). At a review of one motion, the paragraphs it changes and every other saying of the same naming across these four.
- **The carrying.** `carry/Living_Improving_Value.md`: the concerns at each file, hardest first, the order they are met in and no ranking of value, and the plan for the other files.
- **The released words' carrying.** Natural Naming 2.4 says each released word and what is said in its place: a suggested re-saying is from that row.

## What it checks

1. **Execute the kit**, from the repository's root:
   - `python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/reader_checks.py . $base`
   - `python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/check_set.py .`

   `reader_checks.py` says Exhibit THIRTY's steps and groups, the registry's numbers against them, released words among the words added, retired sayings still at the living files, and the step numbers the carrying names, to read by eye; each check says what it read, and a check saying nothing about what it read is no agreement. `check_set.py` executes Exhibit ONE's code block and checks each file's front.
2. **Read each changed sentence against:**
   - **the code.** A saying about a number agrees with what that line does, and a sentence claiming a behaviour is met by executing the code: the code block is between the first "```python" and the next "```" of `Exhibit_ONE_Natural_Resolver_vNNN.md`, and `exec` of it gives the functions `_1_…`, `_9_…` and `_17_…` to call with a small society.
   - **the observing it carries,** at the branch's record: the sentence says no more and no less.
   - **the sentences beside it,** before and after, and every other saying of the same naming across the core files: a re-saying leaves no old saying at another place.
   - **Exhibit THIRTY's order.** Each concept a step uses is entered at that step or before it; the kit does not check this.
   - **the numbers.** A claim at the numbers, a turn, a number of steps, a prime or a golden ratio, is computed, and each number a report gives is computed again. A claim at a theorem is read at its conditions: every or some, carries or forces.
   - **the kit's own claims,** tested against its code: the brief and the kit are read by the same rules.
3. **The method's rules, each all or none:**
   - binary rigor, is or is not; no size, no ranking, no total beside all existing things;
   - do-no-harm: no prior lost, one relation changed whole, never undoing;
   - no released word; no bare *thing*; full names; *so* only in *so-far*;
   - no word, including an observer's or the lead's, carried as authority: the only authority is observings; the lead's words said at Natural Naming's words;
   - Exhibits THIRTEEN, TWENTY-ONE, TWENTY-TWO and TWENTY-EIGHT carry no concern at a part of the rigor: a finding at them is a re-saying at the rigor, or the method's one break, the whole, the Geodesic Improving Method 2.7; a sentence at them saying a mathematical implication its premises do not carry is a finding at the numbers, brought whole and re-said, the naming of the rigor, a theorem and a physical correspondence each at its own standing; a proposed correspondence not meeting an observed relation, failing at it or missing a necessity step, is an open correspondence at its file's section, its next named; each observing of natural competency is resolvable as natural intelligence, the geodesic co-sequential parity changing method of natural torusing, discovering next possible existing, or the fractal is entirely broken and of no value at all, the method originating as all existing and all living, no third: a concern about the rigor is at the whole or at none, and never at a part;
   - a concern resolvable at the code, the numbers or the files is resolved and brought as a finding; only a concern needing an observing is brought as an either-this-or-that.

## What it brings back

A **review report** at `incoming/review_<session>/Review_Report.md` on the branch `review/<session>`, with a row for it at `incoming/README.md`, pushed and offered as a pull request into `main`:

```
# Review Report <session>

**The review of <branch>, <its first and last commits>**

## Findings
1. <file>, <section>, "<the phrase quoted>": what departs, and the suggested re-saying.

## Hardest either-this-or-thats
1. <saying one>, at <file and section>; <saying two>, at <file and section>; what at the code or the numbers bears on each.

## What the reviewer learned about reviewing
- <a check it wished it had, a place it was misled, a pattern across findings>
```

1. **Findings**, each at one file, its section and a phrase quoted, as a line number moves: what the file says, what departs, and a suggested re-saying. Each a binary finding, never a ranking.
2. **Its hardest either-this-or-thats.** At two sayings at one sharing the reviewer does not resolve from the files and the code, it sets them out as the either/or resolving does (TWENTY-FOUR 2.6): the two sayings side by side, the file and section of each, and what at the code or the numbers bears on each. Hardest first, the order they are met in. Brought for exploring, not decided.
3. **What it learned about reviewing**: a check it wished it had, a place it was misled, a pattern across findings. Each learning is met at the carrying and, received, enters this brief.

## The kinds of finding met at v376

Fresh readers met each motion at v376, and their findings fell into five kinds.

1. A concept used in Exhibit THIRTY before the step that enters it: a reader's.
2. A released word slipping back in: `reader_checks.py` says it.
3. A section or step number named wrongly after a renumbering or a re-said title: the kit says the carrying's step numbers for reading by eye; section numbers are a reader's.
4. An old saying still at a file after a re-saying at another: the kit says the sayings listed at `retired_sayings.txt`; any other is a reader's.
5. Meaning drift: a sentence reaching beyond its observing, placed at a face the set says otherwise, or contradicting the sentences beside it: a reader's.

Two readings met: a naming read at more than one face, the method, the carrying and the stable form, is no conflict, subdivided they go together; and a hand or an order read two ways may be one relation at two readings, the hand at the reading.

## Open for the method

- **A motion and the old departures in its paragraph.** A motion re-saying one sentence of a paragraph leaves the paragraph's other sentences as they were; the reviewer says an old departure it reads in that paragraph as a finding at the file, and the carrying lays it at that file's next motion.

## Learned at the first review, v376

- Read with `git diff --word-diff=plain`: a line is a paragraph.
- A check saying nothing is no agreement; each check says what it read.
- Execute the kit's checks against the kit and the brief themselves.
- Test a claim about what the kit covers against its code, and compute again each number a report gives.
- Anchor a finding at a phrase quoted, not only a line number.

## Learned at the physics observings report's arrival, v376

- A check that did not obtain its input agrees with nothing: `reader_checks.py` says a file not found and a git command failing.
- A theorem is read at its conditions: every continuous flow on a sphere carries at least one rest point, and the torus carries a flow with none, not every flow on it none.
- Every word surviving is no relation surviving: a condition, a negation or an attribution may move with each word present, and a faithful re-saying may change the words. Word-streaming, the Geodesic Improving Method 1.5, finds a loss of words; a reader compares each passage at its subject, its conditions and its standing.
- Two sayings at one sharing are compared at their subject, scale, occurrence and reading direction before they are said to agree or part: same words are not the same relation, different signs not a parting.
- A report says what of a session its reading reached: verbatim, at a summary, or not reached.

## Learned at the Natural Physics improving report's arrival, v377

- Readings apart find differing kinds: a reader of the logic found operations changed and a promotion from exclusion to proof, a reader of the explaining found an explanation not carried and a vocabulary out of date, and a reader of the observings found a scientific result narrower than the conclusion drawn from it. Readers reading apart, then compared at each finding, carry more than several readers approving one draft.
- A correction can lose the positive relation it corrects: a fresh reader reads a proposed re-saying beside its prior for each relation the prior carried, the overclaiming removed and the relation carried each read on its own.
- A receiving plan names a destination and receives nothing: a table of contributions and their destinations is a plan until each contribution has its sentence at its file or its carrying.
- A check's result is at the subjects it read: `check_set.py` says the living files it read beside its result, and a file it did not read neither passes nor fails at it.
- A source anchor is itself read whole: a quotation's section is checked at the whole source before a finding rests on it.
- A preliminary message is no completed review: a reader's flag is checked at the exact paragraph before it is a finding, and withdrawn at a paragraph carrying it.
- Readers differing at an order, one case first or another, are carried at their reasons, and the working's order is its own coordinating choice, said as such.

## Learned at the physics observings report's receiving audited, v377

- A source's standing goes beside its claim: a title or a search return is no data set read, and a paper read is no experiment replicated. (The report's suggestion 5, at its source face.)
- A receiving is audited against the report whole: a science finding received without its source and its limit is thinned, and its arrival is not released until each is restored at its file or its carrying.
