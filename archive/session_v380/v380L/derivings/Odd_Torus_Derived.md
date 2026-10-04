# T1 — steps 650, 651 and the odd torus's number, worked by hand

Nothing was executed. Every grid below was stepped by hand from the cells; every law is reasoned from the cells.
Labels: PROVED (reasoning given), CHECKED BY HAND AT (cases), CONJECTURED. Nothing below is labelled CONJECTURED: no guess is used.

## 0. Cells and notation

Self (i, j), i along (0..p−1, written down the page), j across (0..q−1, written left to right).
Priors of (i, j): (i−1, j) along and (i, j−1) across, indices round p and round q.
c(i,j,t) = parity carried at momentary t. Opening c(i,j,1) = −(−1)^(i+j), self (0,0) carrying −.
s(i,j,t) = what the self shares/releases at t: 0 if it carried on ("hold"), else its next parity −c(i,j,t).
Offerings at t are the priors' s at t−1, 0 passed over. Hold exactly when the surfacing is the self's own parity.
H(t) = set of selves that hold at t. H(1) = ∅ (nothing offered, each inverts).

The cells are unchanged by inverting every parity, and by exchanging along with across.

## PART ONE

### Step 650 (even number along, opened alternating along)

Induction. Claim P(t), t ≥ 2: H(t−1) = ∅ and each self is unlike its along prior at t.
- t = 1: none offered, each inverts, so H(1) = ∅; each self and its along prior both invert, so they stay unlike. P(2).
- P(t) ⇒ P(t+1): the along prior inverted at t−1, so it offers its parity at t, which is not the self's own. The across prior
  offers either parity (it inverted too, so it offers something). Surfacing = the other parity, or 0. A changing. So H(t) = ∅,
  every self inverts, every along pair stays unlike. P(t+1).
So each self inverts at each momentary; c(t+2) = c(t) and s(t+2) = s(t) from momentary 1. PROVED.
The across parities are never used: **the opening alternating across is not needed**; any parities across do. What is needed is
that every along pair, the last-to-first pair included, is unlike, which the even number gives.
Only looseness in 650's words: "each self's along offering is the parity other than its own" is so from the second momentary;
at the first none is offered (and none is a changing too).

CHECKED BY HAND AT 2 along · 3 across:
```
t=1 c: − + −    s: + − +        t=2 c: + − +    s: − + −        t=3 c = t=1 c
       + − +       − + −               − + −       + − +
```
t=2 self by self: (0,0) own +, along − , across + → 0, changing. (0,1) own −, along +, across + → +, changing.
(0,2) own +, along −, across − → −, changing. (1,0) own −, along +, across − → 0. (1,1) own +, along −, across − → −.
(1,2) own −, along +, across + → +. All invert. Again at 2 from momentary 1 = Exhibit ONE's row 2 · 3 (2, from 1).

CHECKED BY HAND AT 3 along · 2 across (the even number across, the along seam alike):
```
t=1 c: − +   s: + −     t=2 c: + −   s: − +     t=3 c = t=1 c
       + −      − +            − +      + −
       − +      + −            + −      − +
```
t=2: (0,0) own +, along (2,0) +, across (0,1) − → 0, changing. (0,1) own −, along −, across + → 0. (1,0) own −, along +,
across + → +. (1,1) own +, − and − → −. (2,0) own +, − and − → −. (2,1) own −, + and + → +. All invert; 2 from 1.
"The same at an even number across" holds, and the alike seam along does not disturb it.

**650: no clause is false.**

### Step 651, torus 3 · 3, momentaries 1 to 13

c = carried, s = shared, H = holds. Rows i = 0,1,2 down; columns j = 0,1,2.
```
t   c           s           H
1   − + −       + − +       none
    + − +       − + −
    − + −       + − +
2   + − +       0 + −       (0,0)
    − + −       + − +
    + − +       − + −
3   + + −       − 0 +       (0,1) (1,0)
    + − +       0 + −
    − + −       + − +
4   − + +       + − 0       (0,2) (2,0)
    + + −       − − +
    + − +       0 + −
5   + − +       − + −       (1,1)
    − − +       + 0 −
    + + −       − − +
6   − + −       0 − +       (0,0) (1,2) (2,1)
    + − −       − + 0
    − − +       + 0 −
7   − − +       + + −       none
    − + −       + − +
    + − −       − + +
8   + + −       − 0 +       (0,1) (1,0) (2,2)
    + − +       0 + −
    − + +       + − 0
9   − + +       + − −       none
    + + −       − − +
    + − +       − + −
10  + − −       − + 0       (0,2) (1,1) (2,0)
    − − +       + 0 −
    − + −       0 − +
11  − + −       + − +       none
    + − −       − + +
    − − +       + + −
12  + − +       0 + −       (0,0) (1,2) (2,1)
    − + +       + − 0
    + + −       − 0 +
13  + + −   = −c(7)
    + − +
    − + +
```
Sample of the cell rule: t=5 (0,0) own +, both priors shared 0 at 4 → none → changing. t=6 (0,0) own −, along (2,0) shared −,
across (0,2) shared − → − = own → hold. t=6 (1,2) own −, along (0,2) −, across (1,1) 0 passed over → − → hold.
s(12) = −s(6) and c(13) = −c(7), H(12) = H(6): by the inverting symmetry s(t+6) = −s(t), s(t+12) = s(t) for t ≥ 6.
Not from 5: H(5) = {(1,1)}, H(17) = H(11) = ∅. So 12, from 6 = Exhibit ONE's row 3 · 3. CHECKED BY HAND.

### Step 651, torus 3 · 5, momentaries 1 to 13

```
t   c               s               H
1   − + − + −       + − + − +       none
    + − + − +       − + − + −
    − + − + −       + − + − +
2   + − + − +       0 + − + −       (0,0)
    − + − + −       + − + − +
    + − + − +       − + − + −
3   + + − + −       − 0 + − +       (0,1) (1,0)
    + − + − +       0 + − + −
    − + − + −       + − + − +
4   − + + − +       + − 0 + −       (0,2) (2,0)
    + + − + −       − − + − +
    + − + − +       0 + − + −
5   + − + + −       − + − 0 +       (0,3) (1,1)
    − − + − +       + 0 − + −
    + + − + −       − − + − +
6   − + − + +       + − + − 0       (0,4) (1,2) (2,1)
    + − − + −       − + 0 − +
    − − + − +       + 0 − + −
7   + − + − +       0 + − + −       (0,0) (1,3)
    − + − − +       + − + 0 −
    + − − + −       − + + − +
8   + + − + −       − 0 + − +       (0,1) (1,4) (2,2)
    + − + − −       − + − + 0
    − + + − +       + − 0 + −
9   − + + − +       + − − + −       (1,0) (2,3)
    − + − + −       0 − + − +
    + − + + −       − + − 0 +
10  + − − + −       − + 0 − +       (0,2) (1,1) (2,4)
    − − + − +       + 0 − + −
    − + − + +       + − + − 0
11  − + − − +       + − + 0 −       (0,3) (2,0)
    + − − + −       − + + − +
    + − + − +       0 + − + −
12  + − + − −       − + − + 0       (0,4) (1,2) (2,1)
    − + + − +       + − 0 + −
    + + − + −       − 0 + − +
13  − + − + −   = −c(7)
    + − + + −
    − + + − +
```
Sample: t=7 (0,0) own +, along (2,0) shared +, across (0,4) shared 0 → + = own → hold. t=7 (2,2) own −, both priors shared 0
→ none → changing. t=9 (0,2) both priors held at 8 → none → changing (the 0 of the line across waits one momentary).
s(12) = −s(6), c(13) = −c(7), H(12) = H(6): s(t+12) = s(t) for t ≥ 6. Not from 5: H(5) = {(0,3),(1,1)}, H(11) = H(17) =
{(0,3),(2,0)}. So 12, from 6 = Exhibit ONE's row 3 · 5. CHECKED BY HAND.

### 651 clause by clause

1. "at the first momentary each self inverts": holds (3·3, 3·5; PROVED: none offered).
2. "at the second one self alone is at a changing that is not, the self alike with both its along prior and its across prior,
   each other self offered the parity other than its own or + and − together": holds (3·3, 3·5; PROVED: only (0,0) has both
   edges like; seam selves get + and −, the rest the other parity).
3. "a 0 passes one self on at each momentary along each of the two lines ... the self i on at momentary i + 2": holds.
   3·3: (1,0),(0,1) at 3; (2,0),(0,2) at 4. 3·5: also (0,3) at 5, (0,4) at 6. PROVED at every odd p ≤ q (Theorem A below).
4. "to the last self of the line": holds along (the short line): after (p−1,0) at p+1 the self (0,0) does not hold at p+2
   (3·3: inverts at 5, holds at 6; 3·5: inverts at 5 and 6, holds at 7). **False across at q more than p**: the 0 passes on
   round the line. 3·5: (0,4) at 6, (0,0) at 7, (0,1) at 8, the selves 5 and 6 on at momentaries 7 and 8, still "j on at
   j + 2"; it first waits before (0,2) (at 10, not 9). PROVED in general: the self j on at j + 2 for every j ≤ 2q − p − 1 at
   q less than twice p, and for every j, without end, at q more than twice p.
5. "derived at no step": superseded by Part Two.

## PART TWO

### 2.0 The start, checked

v = c·(−1)^t. An inverting self keeps v, a holding self flips v. PROVED (c(t+1) = −c(t) or c(t)).
For t ≥ 2 a prior y that did not hold at t−1 offers at t its parity c(y,t); a prior that held offers 0. So with N = priors not
in H(t−1): self x holds at t ⇔ N is not empty and each y in N has c(y,t) = c(x,t) ⇔ v(y,t) = v(x,t). PROVED.
Opening v(i,j,1) = (−1)^(i+j): like edges are exactly the along edges into (0,j) and the across edges into (i,0). PROVED.
A hold flips one v, toggling the four edges at that self. PROVED.

### 2.1 Lemma 1 (one 0 in each line across). PROVED

Write A(i,j) for the along edge (i−1,j)→(i,j) and B(i,j) for the across edge (i,j−1)→(i,j).
Claim: after every momentary t ≥ 1 there are, for each i, a column x_i, a gap g_i with 0 ≤ g_i ≤ q and x_(i−1) ≡ x_i + g_i
(mod q), and a flag h_i, such that
- (S1) B(i,j) is like exactly at j = x_i + 1;
- (S2) A(i,j) is like exactly at j = x_i + 1, ..., x_i + g_i (none at g_i = 0, all at g_i = q);
- (S3) H(t) = { (i, x_i) : h_i = 1 }.
Opening: x_i = q − 1 for all i, g_0 = q, g_i = 0 otherwise, h = 0. (S1)–(S3) are the two seams and H(1) = ∅.

Step t → t+1. Self (i,j) with j ≠ x_i + 1: its across prior (i,j−1) is not (i,x_i), so it did not hold, is in N, and B(i,j)
is unlike: no hold. Self (i, x_i + 1): B like; A like iff g_i ≥ 1; the across prior is out of N iff h_i = 1; the along prior
(i−1, x_i+1) is out of N iff it is (i−1, x_(i−1)) with h_(i−1) = 1, i.e. g_i = 1 and h_(i−1) = 1. Hence

**Move rule.** (i, x_i+1) holds at t+1 ⇔ g_i ≥ 2, or g_i = 1 and not (h_i = 1 and h_(i−1) = 1).
(g_i = 0: along prior in N and unlike, no hold. g_i = 1 with both flags: N empty, none surfaces, a changing.)

The hold at (i, x_i+1) toggles B(i,x_i+1) to unlike, B(i,x_i+2) to like (S1 with x_i + 1); toggles A(i,x_i+1) to unlike
(g_i − 1) and A(i+1, x_i+1) to like (g_(i+1) + 1); if both i−1 and i move, g_i is unchanged. g_i never passes q (a self with
g ≥ 2 moves) nor falls below 0 (a move needs g ≥ 1). (S1)–(S3) hold after t+1. ∎
So: at every momentary each line across carries at most one 0, at the self next across after its last 0.
CHECKED BY HAND AT 3·5, t = 7: likes B(0,0), B(1,3), B(2,2); A(1,·) like at 3,4; A(2,·) at 2; A(0,·) at 0,1; x = (4,2,1).

### 2.2 Lemma 2 (the recursion). PROVED

Let τ_i(k) = momentary of the k-th hold in line i (it is at column k − 1 round q). Let a = τ_i(k−1) (none at k = 1) and
b = τ_(i−1)(k) for i ≥ 1; for i = 0, b = τ_(p−1)(k − q) (none at k ≤ q). From the move rule (g_i ≥ 1 ⇔ b ≤ t; g_i = 1 with
h_(i−1) = 1 ⇔ b = t; h_i = 1 ⇔ a = t):

  τ_i(k) = max(a, b) + 1 if a ≠ b,  = a + 2 if a = b;  τ_0(1) = 2.

### 2.3 Lemma 3 (the offset). PROVED

Let inc_i(k) = τ_i(k) − τ_i(k−1) and δ = τ_i(k) − τ_(i−1)(k) ≥ 1, d = inc of the prior line at k+1. From Lemma 2:
- δ > d: next δ = δ − d + 1, the line moves on at once (inc 1);
- δ = d: next δ = 2, the line waits one (inc 2);
- δ < d: next δ = 1, inc = d + 1 − δ.
With d in {1,2}: δ = 1 → 2 (d=1) or 1 (d=2), inc 2 both; **δ = 2 → 2 always, inc = d (locked: the line copies its prior
line two momentaries later, for ever)**; δ ≥ 3 → δ (d=1) or δ − 1 (d=2), inc 1. So every inc is 1 or 2 (induction along the
order of the recursion, line 0 starting with inc 1).

### 2.4 Theorem A (first sweep and locking), odd p ≤ q. PROVED

τ_0(k) = k + 1 for k ≤ q (no prior constraint on the first lap). δ_i(1) = 1 for i ≥ 1. By induction on i with Lemma 3:
δ_i(k) = 1 for k ≤ i, and δ_i(k) = 2 for every k ≥ i + 1, for ever; inc_i(k) = 2 for 2 ≤ k ≤ i+1 and inc_i(k) = inc_0(k) for
k ≥ i+2. (At k = i+1 the prior line's inc is inc_0(i+1) = 1 since i + 1 ≤ p ≤ q.) Therefore, for all time,

  τ_i(k) = τ_0(k) + 2i − max(0, i − k + 1).

On the first lap this is τ_i(j+1) = i + j + min(i,j) + 2: **the first hold of every self (i,j), with no exception and no
"until the sweeps meet"**: the later sweeps never disturb a first hold.
CHECKED BY HAND AT 3·3 (all nine selves: 2,3,4 / 3,5,6 / 4,6,8) and 3·5 (all fifteen: 2,3,4,5,6 / 3,5,6,7,8 / 4,6,8,9,10).

Second holds on the line (i,0): τ_i(q+1) = τ_0(q+1) + 2i. At p < q, τ_0(q+1) = q + 2 (a = q+1 > b = p+1), so (i,0) holds
again at q + 2 + 2i, one momentary after (i, q−1)'s first hold at q + 2i + 1. PROVED; 3·5: 7, 9, 11.
Corrections to the start as given: at p = q the self (0,0) holds again at q + 3, not q + 2 (a = b; 3·3: at 6), and (i,0) at
q + 3 + 2i (3·3: 8, 10); and at p < q the second wave also runs across, (0,1) at q + 3 coming before (1,0) at q + 4.

### 2.5 Theorem B (q more than twice p). PROVED

Let m = q − p (even). Offset of line 0's second lap from line p−1: Δ(k) = τ_0(q+k) − τ_(p−1)(k), Δ(1) = (q+2) − (p+1) =
m + 1. Line p−1 has inc 2 at k = 2..p, so Δ falls by one each step: Δ(p) = m + 2 − p = q − 2p + 2 ≥ 3. From there line p−1
copies inc_0, which is 1, so Δ stays ≥ 3 and inc_0 stays 1, by induction for ever. Hence for all time
  τ_i(k) = i + k + 1 + min(i, k−1): line i holds at each momentary from 3i + 2 on, each line two momentaries behind its prior.
Each self then holds once in each q momentaries: v(t+q) = −v(t), and q is odd, so c(t+q) = c(t): sharings again at q, and not
sooner (line 0's single 0 needs q momentaries round). Line i waits at 3i + 1 and holds at 3i + 1 + q, so the pattern is
again from 3i + 2 and not before: over all lines, **from momentary 3p − 1**.
Table: 1·3 (3, 2), 1·5 (5, 2), 3·7 (7, 8), 3·13 (13, 8), 5·11 (11, 14), 7·17 (17, 20), 17·59 (59, 50): all seven agree in both
columns. Steps at 3·7: τ_0 = k+1; τ_1 = 3, then k+3; τ_2 = 4, 6, then k+5; Δ = 5, 4, 3, 3, ...; H(8) = (0,6),(1,4),(2,2);
H(7) has no 0 in line 2 while H(14) has (2,1): from 8.

### 2.6 Theorem C (p ≤ q less than twice p, p ≥ 3). PROVED

m = q − p, 0 ≤ m ≤ p − 1. If m ≥ 2: Δ(1) = m + 1 ≥ 3 and falls by one each step to Δ(m) = 2, line 0 moving on at once
meanwhile: τ_0(q+k) = q + k + 1 for k ≤ m. If m = 0: Δ(1) = 2 at once (τ_0(q+1) = q + 3). Then Δ = 2 is locked for ever:
  τ_0(q+k) = τ_(p−1)(k) + 2 for every k ≥ max(m,1).
With τ_(p−1)(k) = p + 2k − 1 for k ≤ p and τ_(p−1)(k) = τ_0(k) + 2p − 2 for k ≥ p:
- τ_0(q+k) = p + 2k + 1 for max(m,1) ≤ k ≤ p: line 0 waits before each of the columns m, ..., p − 1, which are 2p − q columns;
- τ_0(k + q) = τ_0(k) + 2p for every k ≥ p, and so τ_i(k + q) = τ_i(k) + 2p for every line and every k ≥ p.
So each line's 0 goes round its q selves in 2p momentaries (q moves and 2p − q waits, each wait before one of the fixed columns
m..p−1, each line two momentaries behind its prior, 2p momentaries round the p lines). H(t + 2p) = H(t), least period 2p
(a shorter one, dividing 2p, would carry each 0 a whole number of rounds in less than a round's time). Each self holds once in
2p: v(t+2p) = −v(t), 2p even, so c(t+2p) = −c(t), s(t+2p) = −s(t): **sharings again at 4p**, not at 2p.
From-momentary: line i ≤ p − 2 holds at p + 2i (its (p−1)-th hold) but waits at 3p + 2i, and is again from p + 2i + 1; line
p − 1 is again from p + 2·max(m,1) − 1 ≤ 3p − 3. Largest: line p − 2: **from momentary 3p − 3**, and not before.
Table: 3·3 (12, 6), 3·5 (12, 6), 5·7 (20, 12): agree in both columns.
Steps at 3·5 (m = 2): τ_0 = 2,3,4,5,6 | 7,8,10,11,12 | 13,14,16,..; τ_1 = 3,5,6,7,8 | 9,10,12,13,14; τ_2 = 4,6,8,9,10 |
11,12,14,..; Δ = 3, 2, 2, ...; the one wait column is 2: (0,2) at 10, (1,2) at 12, (2,2) at 8 and 14. All as the grids.
Steps at 5·7 (m = 2), by the recursion: τ_0 = 2..8 | 9, 10, 12, 14, 16, 17, 18 | 19, ...; τ_4 = 6, 8, 10, 12, 14, 15, 16, 17.

Gaps in the settled state: 2p − q lines one column behind their prior line, q − p lines two behind; the ones pass one line on
each two momentaries.

### 2.7 The number, derived

For odd p ≤ q, opened as Exhibit ONE opens it:
- q > 2p: sharings again at q, from momentary 3p − 1. PROVED.
- q < 2p (p ≥ 3): sharings again at 4p, from momentary 3p − 3. PROVED.
(q = 2p cannot be, q odd. One self alone, p = q = 1, is Exhibit ONE's spiral of 1: 4.)
Reason for the divide: one 0 per line across, each line's 0 at least two momentaries behind the prior line's; round p lines
that is 2p momentaries, round the line it is q. The larger rules; an odd count of holds over an even time inverts, hence 4p.

CHECKED BY HAND AT: 3·3 and 3·5 (grids to 13, every self), 3·7 and 5·7 (recursion only). Agrees with all ten odd rows of
Exhibit ONE in both columns. No grid was stepped for the predictions below; they are the theorems' values.

Predictions (momentaries to the sharings again, from momentary):
- 3 · 9: 9, from 8.     3 · 11: 11, from 8.
- 5 · 9: 20, from 12.   5 · 13: 13, from 14.
- 7 · 9: 28, from 18.   7 · 15: 15, from 20.
- 9 · 9: 36, from 24.
- q = 2p − 1: 4p, from 3p − 3 (5·9: 20, 12; 7·13: 28, 18; 9·17: 36, 24), one wait column, p − 1.
- q = 2p + 1: q, from 3p − 1 (7·15: 15, 20; 9·19: 19, 26; 11·23: 23, 32), the settled gaps 2, ..., 2, 3.
Finer tests: 5·9 line 0 second lap 11, 12, 13, 14, 16, 17, 18, 19, 20 (wait before column 4 only);
7·9 line 0 second lap 11, 12, 14, 16, 18, 20, 22, 23, 24 (waits before columns 2..6).

### 2.8 Where certainty rests

Everything rests on Lemma 1 (the cells give the move rule). It was reasoned from the cells and checked against every hold in
the two grids (3·3: 18 holds to momentary 12; 3·5: 25 holds). It has not been checked on a grid with p ≥ 5.
