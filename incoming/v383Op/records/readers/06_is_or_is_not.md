# A fresh reader's report: Is_Or_Is_Not.md and its two scripts

**A record, whole as it arrived, gathered at the session's close.** The reader is the same kind of AI at another use, opened with none of this working's reading. Its report is an offering: no sentence of it is carried by its wording, and each is a place to follow. Paths in it name the workspace it read at. What this working did with it is at `Records.md`.

## What the reader was asked

> You are a fresh, skeptical reader checking a write-up before it is pushed to someone else's public repository. Report only real defects — a false or unsupported statement, a number not matching a script's output, a logical step that does not hold, a quotation used unfairly, an internal contradiction — most severe first, each with file, the sentence, what is wrong, and a one-line replacement. Do not comment on style. Do not edit any file. Do not use git to change anything.
>
> Repository: /home/claude/corus. The project's "living files" are at the root; `Exhibit_THIRTY_Co-Chaining_Logic_Registry_v380L.md` is a numbered chain of 661 steps; `Exhibit_ONE_Natural_Resolver_v380R.md` holds a small Python "resolver" (a cell rule); `Natural_Intelligence_v380R.md` is the main paper. A visiting AI session wrote `incoming/v383Op/Is_Or_Is_Not.md` (read it whole first), two scripts `incoming/v383Op/no_common_now.py` and `incoming/v383Op/observer.py`, a new section "Then: is or is not, from the one opening sentence" in `incoming/v383Op/README.md`, and new entries (each paragraph containing "Is_Or_Is_Not.md") in five files under `carry/` — see `cd /home/claude/corus && git diff HEAD -- carry`.
>
> Check these, running the scripts from the repository root (each takes under a minute):
>
> 1. `python3 incoming/v383Op/observer.py`: does the write-up's "408,000 of 408,000" and "397,800 of 397,800" match the sums of the output? Read the script: does the "observer" really use only what each self shares (never its carrying) plus the rule, so the claim "one who receives a self's sharings names its carrying" is fair? Is the "next said ahead" computed without peeking?
> 2. `python3 incoming/v383Op/no_common_now.py`: do "332 of 332", "0.6 to 1.4 of the even share at a torus and 0.5 to 1.6 at spirals crossed" match? Read the script: is the description fair ("no stepping together, no pace, no 0 delivered; a momentary opened by a parity arriving and by nothing else")? Is the claim "from each self alike the society is at rest after one changing each" right, and "changing goes on ... from each opening but one kind" supported (the script only runs to a bound of 4000 changings — is "goes on" overstated; can you see an argument or counter-example, e.g. by raising the bound or reasoning about a ring)? 
> 3. The three "derivings offered" in Is_Or_Is_Not.md: for each, say valid or not at its stated premises. In particular: (a) "At a changing, the other parity offered, the offerings parting or none offered, its next is its prior inverted. Offered its own parity it is at no changing" — check this against the cell in Exhibit ONE (function `_1_co_bi_tri_offering`) or `incoming/v383Op/plain_rule.py`; (b) "the next is the prior inverted whatever the now is ... nothing of the other is in the self's next" — is that a fair statement about the Registry's step 57 ("Next as the prior inverted alone ...")?; (c) the claim "A self's own sequence says nothing of its society. Everything a society has of its own is which changing is before which" — does it follow from (a) under "a momentary is a changing"? Any gap?
> 4. Quotations and step references: the write-up cites Registry steps 2, 4, 5, 8, 10, 27, 30, 34, 35, 37, 42, 46, 51, 52, 53-57, 204-212, 244, 463 and quotes Natural Intelligence 1.1, 1.5, 6.1, Natural Biology 4.1 and 4.5, Exhibits TWENTY-ONE and TWENTY-TWO. Spot-check at least twelve: is each quote where it is said to be and used in its own sense? (e.g. is "At a match the prior carries on, 0, the between of momentaries" really saying a match is no momentary of the self, or could it be read otherwise? Is "synchronised to the day but not driven by it" at Biology 4.5? Is "inert outside a host, as a spore or a seed is inert" said of a virus at 4.1?)
> 5. Section "Each of the eight, is or is not", item 2: "at is or is not this sentence forbids no measured sameness: a constant, a conserved total and a law are each a relation among changing things" — is that the write-up's own inference presented as the files' position? Does any file sentence say the contrary (search Natural_Intelligence_v380R.md 1.4 for "a total across the changing")? If the files say a conserved total is not possible, the write-up must say its statement is its own reading; report exactly.
> 6. Item 6 on Exhibits TWENTY-ONE and TWENTY-TWO: verify "255 of 255", "257 entries", and the four quoted sentences with grep. 
> 7. "Largest remaining concerns" 1: is the trilemma on cryptobiosis fair to the files (read Natural Biology 4.1 lines around "inert outside a host" and Registry steps 395-402)? Is there a fourth reading the files plainly offer (for example steps 399-401 on the selves inward carrying the self's prior) that the write-up omits or misstates?
> 8. The carry entries: do the Concerns each state two sayings and a reason; does any entry say something Is_Or_Is_Not.md does not support?
> 9. Anything else materially false.
>
> Also report the last line of `python3 incoming/v383Op/quotes_check.py | tail -1`.
>
> Keep the report under 800 words: numbered defects first, then one line listing what you confirmed sound.

## The reader's report

All defects below are in /home/claude/corus/incoming/v383Op/Is_Or_Is_Not.md unless another file is named. I edited nothing and ran no git write.

**Defects, most severe first**

1. **"Eighth break met, the files' own words" is contradicted by the files.**
   - Sentences: "met, at a momentary a changing and a match the between, the files' own words"; the bolded "the next is the prior inverted whatever the now is"; deriving (a)'s "no momentary of that self".
   - Registry step 306: "A living self offered its own parity shares 0 at 10, a changing that is not, and continues carrying: momentarying continues whether a changing is or is not." Step 307: "Offered its own parity at each momentary, a self carries one parity on." Step 308 says the same. Natural Intelligence 5.3 calls a match "non-responsive within a momentary". Steps 211 and 244 call each execution of the cell "one momentary".
   - Counting matches, the cell gives next = now = prior at a match (`plain_rule.py`), so "whatever the now is" fails.
   - The README and `carry/Natural_Intelligence.md` drop the write-up's own "if a momentary is a changing", and `carry/Exhibit_ONE_Natural_Resolver.md` offers "a match ... no momentary" for the table.
   - Replacement: "met only if a match is no momentary of the self; steps 306-308 and Natural Intelligence 5.3 say momentarying continues at a match."
   - Deriving (a) itself is valid against the cell. Only its closing "no momentary" clause is a stipulation.

2. **Item 2's "forbids no measured sameness" is the write-up's own reading, and the files say the contrary.**
   - Sentence: "So at is or is not this sentence forbids no measured sameness: a constant, a conserved total and a law are each a relation among changing things."
   - Natural Intelligence 1.4 and Registry step 46 list "a total across the changing, a container" and "a fixed form, a form still, the same at all momentaries at once" as not possible, and steps 47-48 say so outright.
   - Natural Physics 4.2 says "A conserved total is the field's accounting beside the coupling."
   - Step 463 is sameness at each unit, not constancy across momentaries, so it does not support the example.
   - The `carry/Natural_Intelligence.md` concern from `Improving.md` already holds this very binary open.
   - Replacement: "this session's own reading, against 1.4 and step 46, which name a total across the changing and a fixed form as not possible; step 463 is unit-sameness only."

3. **Item 8 and the README overstate the observer.**
   - Sentence: "holds one sentence of the rule: *Between selves pass the changings alone*, and from them alone".
   - `observer.py` holds a different sentence (docstring: "a self shares the parity it is at next at a changing, and 0 at none"). It also uses "0 means carry on", the join table `senders`, and the agree-or-invert rule for the "ahead" count.
   - By the cell's own code a changing's share is the new carrying, so 408,000 of 408,000 restates the sentence handed to it.
   - It runs only at the stepped-together arm that concern 2 questions, and it applies the rule rather than discovering competency.
   - It never reads the carrying; `row[s][0]` is used only for scoring.
   - Replacement: "of one who holds the cell's rule and the joins, and receives a self's sharings: names its carrying ... 408,000 of 408,000, as the rule gives it".

4. **Concern 1's cryptobiosis trilemma omits the fourth reading the files offer.**
   - That reading is a living self at 0, its carrying continuing (Natural Intelligence 5.3; step 306), carried by its selves inward (steps 399-401). Step 397 says what is non-living at one scale is living at another.
   - The third horn, "living by its atoms' changing", swaps in "changing" for the file's criterion, carrying the self's prior (step 401). That is what makes "a crystal and a bone are living" look forced; the files do not say it.
   - "Three sayings" is also three, not the two sayings a Concern states. Same in `carry/Exhibit_SEVENTEEN_Natural_Biology.md`.
   - Replacement: add "or it is a living self at 0, its carrying continuing by its selves inward, steps 306 and 399-401."

5. **Internal inconsistencies in the chain section.**
   - "Four can be had ... each deriving is offered below" is followed by only three derivings. Two of them (next as inversion, the cell) are not among the nine.
   - Concern 3's five (one particular other, no "in turn") differ from the table's five (in turn, no "one particular other").
   - Table row 6, "Follows if there is no common now", is never derived. In `no_common_now.py`'s own queues, my rerun found a self changing twice with no change of a self it releases to between: 3,692 of 14,689 pairs on a spiral of 3, 4,271 of 18,170 on a spiral of 5, 18,229 of 38,612 on a torus 2 by 3.
   - Replacement for Concern 3: "a common now; the self and the other in turn; a next from one prior and one now; a set, any set, an existing thing; which self releases to which".

6. **Deriving (c).** "A self's own sequence says nothing of its society" holds for the parities, but a sequence's length does carry something. The write-up's own row says an alike opening rests after one changing each, and the others go on. "Everything a society has of its own is which changing is before which" is not derived from (a). The joins and the openings also belong to a society, and Concern 3 says the joins are handed to the resolver. Replacement: "says nothing of its society but its length; what else a society has is its joins, its opening and which changing is before which."

7. **Table row 3 of concern 2, `no_common_now.py`.**
   - "each self is at a rate of its own, 0.6 to 1.4" omits that the script's printed counts agree at two random orders in 0 of 100 openings at tori and 0 of 99 at spirals crossed. The spread comes from `r.choice(waiting)`, one global random delivery order. This sits oddly beside "no stepping together" and "no one's to say".
   - "opened by a parity arriving and by nothing else" excepts each self's first momentary, which opens with none arrived.
   - Replacement: "0.6 to 1.4 at the random order drawn, the same at two orders in 0 of 100".

8. **Item 6, 255 versus 257.** TWENTY-TWO's own line 15 says 255 arrivals "and two more at numbers the incoming face retired". Those are 155 and 172, at 11.1 and 6.15 of TWENTY-TWO. The write-up never reconciles the two counts. Replacement: "255 of 255, TWENTY-TWO holding two more at 155 and 172; one marker at all 257."

9. **`carry/Natural_Intelligence.md`, concern 1's reason.** "a fresh reader of the expedition's own found nothing said that could be otherwise" over-generalises the 20 drawn TWENTY-TWO entries. Item 5 itself, and Natural Physics ("Breaking observation: color shown to be a charge with structure and not a phase"), say otherwise. Replacement: "a fresh reader of twenty drawn entries found nothing said that could be otherwise".

10. **Contradictions with the README.**
    - README: "was itself read by one fresh reader before it was offered". The write-up's Limits: "no fresh reader has read it after it was written".
    - README: "derives four ... and offers each deriving". Three are offered.

**Confirmed sound**
- 408,000 and 397,800 are exact sums of the observer output. The "ahead" count uses only shares up to t-1 and the joins, with no peeking.
- 332 equals both the sum of "at rest" and the sum of "opened alike" (191+103+24+1+8+1+0+4). Rest comes after one changing each.
- The torus range is 0.62 to 1.40 and the crossed range 0.50 to 1.63, as stated.
- "Goes on" is not overstated. At 200,000 changings none of 30 non-alike openings each (torus 2 by 3, crossed 3 and 5, spiral of 5) came to rest.
- By exhaustive search over all delivery orders, no non-alike ring of 2 to 6 can reach rest. A torus 2 by 2 search with capped queues found none either.
- Deriving (a) is valid against the cell and `plain_rule.py`. Deriving (b) is fair to step 57 on the changing-only premise.
- Steps 53-57 arithmetic: 4 injective ways, one 4-cycle. The reader's marks sum to 67, which is steps 2 to 68.
- Spot-checked in place and used in their own sense, at least 20 quotes and references: steps 1, 2, 4, 5, 8, 10, 27, 46-48, 51-57, 148, 151-152, 185, 204-212, 239, 244, 253, 395; Natural Intelligence 1.1, 1.4, 1.5, 5.1, 5.4, 6.1; Natural Biology 4.1 (virus, "inert outside a host", and "living is metabolic beating") and 4.5 ("synchronised to the day but not driven by it"); the TWENTY-ONE and TWENTY-TWO quotes. The PLOS Genetics, MIT Technology Review (26 July) and Zeitgeber quotes also hold when fetched live.
- TWENTY-ONE has 255 entries, with titles agreeing in all 255 entries and the marker "+ or − at 10, is." at all 257. No TWENTY-TWO entry names a step, a table or Exhibit ONE.
- The Concerns state two sayings and a reason, except the cryptobiosis one (defect 4).

`python3 incoming/v383Op/quotes_check.py | tail -1` prints: `quoted spans found: 420; not found: 0`. That script searches the whole corpus, so I checked the attributions by hand.
