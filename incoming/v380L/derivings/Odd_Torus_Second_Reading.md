# T2 — second, independent reading of Registry steps 652 to 657

Read only. The resolver was not executed and not simulated. The grid below was stepped by hand from the cells.
One allowance was used and only that: `rule653.py` (beside this file) evaluates the max-and-add rule of step 653 on
momentaries of 0s, and counts a self's parity from the number of its 0s. It steps no self through the cells.

## 0. Cells as used

Self (i, j), i along 0..2 (down the page), j across 0..6. Priors: (i−1, j) along, (i, j−1) across, round 3 and round 7.
c = carried, s = shared (0 if it carried on, else its next parity). Offerings at t = the two priors' s at t−1, 0 passed over.
At a changing that is not ("0", "hold") exactly when the surfacing is the self's own parity.
Read from the python block of Exhibit ONE: a surfacing of both parities stays 0; an own-parity surfacing gives 0 shared and
the parity kept; every other surfacing (other parity, 0, none) gives −c shared and carried. Agrees with cells.md.

Working aid, derived here and not taken from T1: put v = c·(−1)^t. An inverting self keeps v, a holding self flips v.
A prior that inverted at t−1 offers its parity at t; one that held offers 0. So a self holds at t exactly when, among its
priors that did not hold at t−1, there is at least one and each has the self's v. I kept the v grid, listed every like
along edge (A) and like across edge (B) at each momentary, and tested every self that had any like edge or any prior at a 0.

## 1. Torus 3 along · 7 across, momentaries 1 to 16

```
t    c                  s                  at a 0 (H)
1    − + − + − + −      + − + − + − +      none
     + − + − + − +      − + − + − + −
     − + − + − + −      + − + − + − +
2    + − + − + − +      0 + − + − + −      (0,0)
     − + − + − + −      + − + − + − +
     + − + − + − +      − + − + − + −
3    + + − + − + −      − 0 + − + − +      (0,1) (1,0)
     + − + − + − +      0 + − + − + −
     − + − + − + −      + − + − + − +
4    − + + − + − +      + − 0 + − + −      (0,2) (2,0)
     + + − + − + −      − − + − + − +
     + − + − + − +      0 + − + − + −
5    + − + + − + −      − + − 0 + − +      (0,3) (1,1)
     − − + − + − +      + 0 − + − + −
     + + − + − + −      − − + − + − +
6    − + − + + − +      + − + − 0 + −      (0,4) (1,2) (2,1)
     + − − + − + −      − + 0 − + − +
     − − + − + − +      + 0 − + − + −
7    + − + − + + −      − + − + − 0 +      (0,5) (1,3)
     − + − − + − +      + − + 0 − + −
     + − − + − + −      − + + − + − +
8    − + − + − + +      + − + − + − 0      (0,6) (1,4) (2,2)
     + − + − − + −      − + − + 0 − +
     − + + − + − +      + − 0 + − + −
9    + − + − + − +      0 + − + − + −      (0,0) (1,5) (2,3)
     − + − + − − +      + − + − + 0 −
     + − + + − + −      − + − 0 + − +
10   + + − + − + −      − 0 + − + − +      (0,1) (1,6) (2,4)
     + − + − + − −      − + − + − + 0
     − + − + + − +      + − + − 0 + −
11   − + + − + − +      + − 0 + − + −      (0,2) (1,0) (2,5)
     − + − + − + −      0 − + − + − +
     + − + − + + −      − + − + − 0 +
12   + − + + − + −      − + − 0 + − +      (0,3) (1,1) (2,6)
     − − + − + − +      + 0 − + − + −
     − + − + − + +      + − + − + − 0
13   − + − + + − +      + − + − 0 + −      (0,4) (1,2) (2,0)
     + − − + − + −      − + 0 − + − +
     + − + − + − +      0 + − + − + −
14   + − + − + + −      − + − + − 0 +      (0,5) (1,3) (2,1)
     − + − − + − +      + − + 0 − + −
     + + − + − + −      − 0 + − + − +
15   − + − + − + +      + − + − + − 0      (0,6) (1,4) (2,2)
     + − + − − + −      − + − + 0 − +
     − + + − + − +      + − 0 + − + −
16   + − + − + − +      0 + − + − + −      (0,0) (1,5) (2,3)
     − + − + − − +      + − + − + 0 −
     + − + + − + −      − + − 0 + − +
```

Cells shown self by self at the turning places:
- t=2 (0,0): own +, along (2,0) shared +, across (0,6) shared + → + → a 0. Every other (0,j): along own parity, across the
  other → + and − → changing. (1,0), (2,0): along other, across own → changing. The rest: both the other parity.
- t=3 (1,0): own +, along (0,0) shared 0 (passed over), across (1,6) shared + → a 0. (0,1): along +, across 0 → a 0.
- t=4 (1,1): both priors (0,1), (1,0) shared 0 at 3 → none → changing. Line 1 waits.
- t=5 (2,1): own +, along (1,1) shared − (it inverted at 4), across (2,0) shared 0 → − → changing. Line 2 waits: the 0 of
  line 1 has not yet been at (1,1).
- t=7 (2,2): both priors (1,2), (2,1) shared 0 at 6 → none → changing. Line 2 waits.
- t=8 (2,2): own +, along (1,2) +, across (2,1) + → a 0 (neither prior at a 0 the momentary before).
- t=9 (0,0): own +, along (2,0) +, across (0,6) 0 → a 0. t=11 (1,0): own −, along (0,0) −, across (1,6) 0 → a 0.
  t=13 (2,0): own +, along (1,0) +, across (2,6) 0 → a 0.

Every self at a changing that is not, by line (momentary of the k-th 0 of the line, at column k−1 round 7):
- line 0: 2 3 4 5 6 7 8 | 9 10 11 12 13 14 15 | 16
- line 1: 3 5 6 7 8 9 10 | 11 12 13 14 15 16
- line 2: 4 6 8 9 10 11 12 | 13 14 15 16
At most one 0 in a line at a momentary, always at the self next across after the line's last 0. Waits: line 1 at 4; line 2 at
5 and 7; none after.

Compare with Exhibit ONE, row 3 · 7 (7, from 8): c(15) = c(8), c(16) = c(9), s(15) = s(8), s(16) = s(9); the pair
(c(16), s(15)) fixes all that follows, so s(t+7) = s(t) for every t from 8. Not from 7: s(14) has 0 at (2,1), s(7) has −.
Not sooner than 7: line 0's one 0 needs 7 momentaries round. **Agrees: 7, from momentary 8.**

Compare with step 653's rule (python used here for the arithmetic only; also done by hand for these three lines):
line 0 [2..17], line 1 [3,5,6,..], line 2 [4,6,8,9,..] — identical to the list above at every one of the 39 0s to
momentary 16. By hand: τ1(2): a=3, b=3 equal → 5. τ2(2): a=4, b=5 → 6. τ2(3): a=6, b=6 → 8. τ0(8): a=8, b=τ2(1)=4 → 9.
First-0 formula i + j + 2 + min(i, j): all 21 selves agree (2..8 / 3,5,6,7,8,9,10 / 4,6,8,9,10,11,12).

## 2. Lemma 1 re-derived

State kept after each momentary (my own check of T1's S1–S3 against V2..V16 of the grid above: it held at every one):
each line i has exactly one like across edge, into (i, x+1), x the column of its last 0 (x = q−1 before any); the like along
edges into line i are a run starting at x+1; a 0 at this momentary can only be at (i, x).

A self not next across after its line's last 0: its across prior did not hold and is unlike it → offered across the parity
other than its own → changing. **Exact, from the second momentary** (at the first nothing is offered).

The self next across, (i, x+1), across edge like. Cases:
| along edge | along prior at a 0 before | across prior at a 0 before | offerings | result |
| like | no | no | own, own | a 0 |
| like | no | yes | own, 0 | a 0 |
| like | yes | no | 0, own | a 0 |
| like | yes | yes | 0, 0 → none | changing |
| unlike | no | no / yes | other + own, or other | changing |
(unlike with the along prior at a 0 cannot be: that prior's 0 has just made the edge like.)
So: a 0 exactly when the along edge is like and the two priors were not both at a 0. **The move rule is exact.**
Along edge like ⇔ the prior line's 0 has been at the self's along prior since the line's own 0 was last at this self — or,
for the first line's first round, by the opening's along seam. T1's g_0 = q carries that; Registry 652's words do not.

The invariant under a hold at (i, y): across edges into (i, y) and (i, y+1) toggle (one like edge, moved one on); along
edges into (i, y) (leaves the front of line i's run) and into (i+1, y) (joins the end of line i+1's run, which ends exactly
there). Kept in every case, including both lines moving at once and the run of all q (both toggles on one edge).

Cases the proof passes over, checked here:
- **p = 1.** The self is its own along prior; that edge is always like and is not toggled; the candidate is never its own
  held prior. The rule gives a 0 at each momentary. By hand at 1 · 3: c(1) = − + −; 0s at (0,0) 2, (0,1) 3, (0,2) 4,
  (0,0) 5: 3, from 2, as Exhibit ONE. Lemma 1's proof words ("toggles A(i,·) … and A(i+1,·)") do not fit p = 1; the
  conclusion does.
- **p = q.** Nothing special in Lemma 1. In the recursion, the first line's own last 0 and the last line's first 0 fall at
  one momentary (q + 1 = p + 1): two after. Covered.
- **A line catching the line before it** (gap 0): along edge unlike, prior not at a 0, changing; it moves the momentary after
  the prior line moves (3·7: line 2 at 5 and 6). Covered by "has passed".
- 1 · 1 (outside 655 and 656): the rule gives 2, 4, 6, …; 4, from 1.

Lemmas 2, 3 and Theorems A, B, C re-read line by line: each step follows. Points confirmed: Theorem A needs i + 1 ≤ p ≤ q
and is for lines i ≥ 1 only; Theorem B's from-momentary 3p − 1 and Theorem C's 3p − 3 are both exact ("not before" shown by
line p−1's wait at 3p − 2, and by line p−2's 0 at 3p − 4 with none at 7p − 4).

## 3. The rule of 653 as arithmetic at the ten rows (python, arithmetic only)

| row | rule gives | table |
| 1·3 | 3, from 2 | 3, 2 |
| 1·5 | 5, from 2 | 5, 2 |
| 3·3 | 12, from 6 | 12, 6 |
| 3·5 | 12, from 6 | 12, 6 |
| 3·7 | 7, from 8 | 7, 8 |
| 3·13 | 13, from 8 | 13, 8 |
| 5·7 | 20, from 12 | 20, 12 |
| 5·11 | 11, from 14 | 11, 14 |
| 7·17 | 17, from 20 | 17, 20 |
| 17·59 | 59, from 50 | 59, 50 |
All ten agree in both columns. Needed beside the rule: the first 0 at momentary 2 (651), the absent-term cases, and that a
self inverts at each momentary it is not at a 0. T1 itself worked the rule at four rows only (3·3, 3·5, 3·7, 5·7).

## 4. Step by step

**652 — FALSE as worded at one case; true once said.** "Exactly at these two" fails at the first line's first round: 3·7,
(0,1) is at a 0 at momentary 3, and the last line's 0 is first at (2,1) at momentary 6. Also "its last 0" has no meaning
before a line's first 0, and "inverts" for the other selves is from the second momentary. Replacement:
> 652. At a torus of two odd numbers, opened as step 651 says, each line of selves across carries one 0 at most at a
> momentary, at the self next across after its last 0, before its first at its self of the along seam. That self is at a
> changing that is not exactly at these two: the 0 of the line along prior to it has been at its along prior since its own
> last 0, at the first line's first round the opening's along seam standing for it; and its two priors were not both at a 0
> the momentary before. Each other self, from the second momentary, is offered across the parity other than its own and
> inverts.

**653 — TRUE BUT INCOMPLETE** (the rule cannot be worked from its words: the absent cases and the start are missing).
> 653. The momentary of a line's next 0 is one after the later of two, the line's own last 0 and the 0 of the line along
> prior to it at that place, and two after them at the two at one momentary, step 652; one after the one where the other is
> none, a line's first 0 and the first line's first round; the first line's along prior is the last line, one round of the
> q before; the first 0 of all at the second momentary, step 651.

**654 — first clause PROVED AS SAID (all odd p ≤ q; all 21 selves of 3·7). Second clause FALSE at i = 0** (the first line
is not two behind the last line: 3·7, 5, 4, 3, 3, … behind). "At each momentary on" is unclear. Replacement of the clause:
> … and each line i along after the first, from its 0 next after its first i, is at each 0 of the line prior to it two
> momentaries later, without end.

**655 — result PROVED (p = 1 included). "Each line two momentaries behind its prior" FALSE at the first line** (q − 2p + 2
behind the last, 3 or more). Replacement: "… and waits at none, each line after the first two momentaries behind its prior,
the first more than two behind the last, steps 653 and 654: …".

**656 — PROVED AS SAID.** p = q is inside it (3·3; rule at 5·5: 20, from 12). "Comes two momentaries behind" is at once only
at p = q; at q more it is at the (q − p)-th place. p = 1 is outside it: 1 · q is in 655; 1 · 1 is said in none of 652 to 657.
Add: "The first line comes two momentaries behind the last at its place q − p of the second round, at p = q its first; … One
self alone, p and q both 1, is at a 0 at each second momentary, step 653: 4, from the first, Exhibit ONE's spiral of 1."

**657 — first sentence PROVED (with 655's correction: "each after the first"). Second sentence TRUE BUT SAID MORE THAN WAS
WORKED** in T1 (four rows by the rule, six by the theorems' values); now worked at all ten here, all agree. Replacement:
> The rule of step 653, from the first 0 of step 651 and each self inverting at each momentary it is not at a 0, worked as
> arithmetic at each of Exhibit ONE's ten rows of two odd numbers, gives each row's number and the momentary it is from.

No step of 652 to 657 cites a greater step number.
