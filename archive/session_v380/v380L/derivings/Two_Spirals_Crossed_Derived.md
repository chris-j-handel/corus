# X1. Two spirals crossed: the eight rows, derived from the cells

Read only; nothing executed; no simulation. Every grid below was stepped by hand from the cells of `cells.md` (checked against lines 13 to 60 of Exhibit ONE: 17 routes the one list `_10_bi_tri_bi_tunneling` along (9) and across (6, 10), so the changing given across is the changing released along).

Labels: PROVED (reasoned from the cells), CHECKED BY HAND AT (cases), CONJECTURED / NOT SHOWN.

## 0. Notation and the one-spiral law (re-checked)

- Spirals A (m selves) and B (n selves). c_i(t) is the parity self i carries at momentary t; x_i(t) what it shares/releases at t. x_i(t) = 0 if it carried on, = c_i(t+1) = −c_i(t) if it inverted.
- a(t) = c of A1, b(t) = c of B1 (the two crossing selves).
- Opening (table head): self 1 carries −, alternating along, last and first alike at an odd number. Momentary 1: none surfaces, every self inverts.

One spiral alone (PROVED, re-derived):
- If every self inverted at t−1 then x_{i−1}(t−1) = c_{i−1}(t). At t self i is offered its prior's parity: alike with it (a like pair, i the receiver) it carries on and shares 0; unlike, it inverts. Either way c_i(t+1) = c_{i−1}(t). Call such a t a *carry momentary*.
- At the next momentary self i is offered 0 (prior carried on: none surfaces, inverts) or c_{i−1}(t+1) = c_{i−2}(t) = −c_{i−1}(t) = −c_i(t+1) (inverts). So every self inverts: an *invert momentary*. Then the next is a carry momentary again.
- Hence c_i(t+2) = −c_{i−1}(t) at carry momentaries t; a like pair moves one self on each two momentaries. From the opening the carry momentaries are the even ones, and the receiver of the one like pair of an odd spiral is self k at momentary 2k (k = 1..n), self 1 again at 2n+2.
- Checked against Exhibit ONE row n = 3 (self 1: +, 0, −, +, −, +, −, 0, …): my hand steps give x_1 = +, 0, −, + at t = 1..4. Agrees.

## 1. What the crossing self receives (PROVED, from lines 15 to 28)

Two offerings at momentary t: o1 = x of its along prior (the last self of its own spiral) at t−1, and o2 = x of the other spiral's crossing self at t−1. Every other self has one offering.

| o1, o2 | surfaces | crossing self carrying c |
|---|---|---|
| both parity c | c | a changing that is not: shares 0, carries c |
| both parity −c | −c | inverts, shares −c |
| + and − together | 0 | inverts, shares −c |
| one a 0, the other c | c | carries on, shares 0 |
| one a 0, the other −c | −c | inverts |
| both 0 | none | inverts |

So: **the crossing self carries on exactly when at least one offering is not 0 and every offering that is not 0 is its own parity.** Compared with the same self in its spiral alone, the across offering changes the outcome in two cells only:

- **D1**: o1 = c (alone: carry on), o2 = −c: + and − together, surfaces 0, it inverts.
- **D2**: o1 = 0 (alone: invert), o2 = c: surfaces c, it carries on.

In every other cell the crossing self does what it would do alone. o1 = c happens only at a carry momentary when the like pair is (last, first), the crossing self its receiver; o1 = 0 only at the momentary after the last self carried on. So the across offering can act only when the like pair is at the seam.

## 2. Grids by hand

Left: carried c(t). Right: shared x(t). A | B.

### 2 · 3, momentaries 1 to 12 (CHECKED BY HAND)

| t | A1 A2 | B1 B2 B3 | x: A1 A2 | x: B1 B2 B3 | note |
|---|---|---|---|---|---|
| 1 | − + | − + − | + − | + − + | all invert |
| 2 | + − | + − + | − + | 0 + − | A1: − and + together, inverts. B1: + and +, carries on |
| 3 | − + | + + − | + − | − − + | crossing selves opposite from here |
| 4 | + − | − − + | − + | + 0 − | B2 carries on |
| 5 | − + | + − − | + − | − + + | |
| 6 | + − | − + + | − + | + − 0 | B3 carries on: the last 0 |
| 7 | − + | + − + | + − | − + − | B1: 0 and −, carrying +: inverts (no D2) |
| 8 | + − | − + − | − + | + − + | B1: − from B3 (its own) and + from A1: 0, inverts (D1) |
| 9 | − + | + − + | + − | − + − | = x(7) |
| 10 | + − | − + − | − + | + − + | = x(8) |
| 11 | − + | + − + | + − | − + − | |
| 12 | + − | − + − | − + | + − + | |

x(t+2) = x(t) for every t ≥ 7; x(6) ≠ x(8) (B3: 0 against +). **From momentary 7, again at 2, crossing selves opposite: the row 2 · 3 holds.** Crossing selves are in fact opposite from momentary 3 on.

### 3 · 5, momentaries 1 to 16 (CHECKED BY HAND)

| t | A1 A2 A3 | B1 B2 B3 B4 B5 | x: A | x: B | note |
|---|---|---|---|---|---|
| 1 | − + − | − + − + − | + − + | + − + − + | all invert |
| 2 | + − + | + − + − + | 0 + − | 0 + − + − | A1, B1 carry on (both offerings own parity) |
| 3 | + + − | + + − + − | − − + | − − + − + | |
| 4 | − − + | − − + − + | + 0 − | + 0 − + − | |
| 5 | + − − | + − − + − | − + + | − + + − + | |
| 6 | − + + | − + + − + | + − 0 | + − 0 + − | A3 carries on |
| 7 | + − + | + − + + − | 0 + − | − + − − + | **A1: 0 from A3, + from B1, carrying +: carries on (D2)** |
| 8 | + + − | − + − − + | − − + | + − + 0 − | crossing selves opposite from here |
| 9 | − − + | + − + − − | + 0 − | − + − + + | A's carry momentaries are now the odd ones |
| 10 | + − − | − + − + + | − + + | + − + − 0 | B5 carries on: B's last 0 |
| 11 | − + + | + − + − + | + − 0 | − + − + − | A3 carries on: the last 0. B1: 0 and −, carrying +: inverts |
| 12 | + − + | − + − + − | − + − | + − + − + | B1: − from B5 and + from A1: 0, inverts (D1). A1: 0 and −, carrying +: inverts |
| 13 | − + − | + − + − + | + − + | − + − + − | A1: − from A3 and + from B1: 0, inverts (D1) |
| 14 | + − + | − + − + − | − + − | + − + − + | = x(12) |
| 15 | − + − | + − + − + | + − + | − + − + − | = x(13) |
| 16 | + − + | − + − + − | − + − | + − + − + | |

x(t+2) = x(t) for every t ≥ 12; x(11) ≠ x(13) (A3: 0 against +). **From momentary 12: the row 3 · 5 holds.**

### 3 · 7, momentaries 1 to 16 (CHECKED BY HAND; not a table row; chosen to test n > 2m)

| t | A | B | x: A | x: B |
|---|---|---|---|---|
| 1 | − + − | − + − + − + − | + − + | + − + − + − + |
| 2 | + − + | + − + − + − + | 0 + − | 0 + − + − + − |
| 3 | + + − | + + − + − + − | − − + | − − + − + − + |
| 4 | − − + | − − + − + − + | + 0 − | + 0 − + − + − |
| 5 | + − − | + − − + − + − | − + + | − + + − + − + |
| 6 | − + + | − + + − + − + | + − 0 | + − 0 + − + − |
| 7 | + − + | + − + + − + − | 0 + − | − + − − + − + |
| 8 | + + − | − + − − + − + | − − + | + − + 0 − + − |
| 9 | − − + | + − + − − + − | + 0 − | − + − + + − + |
| 10 | + − − | − + − + + − + | − + + | + − + − 0 + − |
| 11 | − + + | + − + − + + − | + − 0 | − + − + − − + |
| 12 | + − + | − + − + − − + | − + − | + − + − + 0 − |
| 13 | − + − | + − + − + − − | + − + | − + − + − + + |
| 14 | + − + | − + − + − + + | − + − | + − + − + − 0 |
| 15 | − + − | + − + − + − + | + − + | − + − + − + − |
| 16 | + − + | − + − + − + − | − + − | + − + − + − + |

D2 at A1 at t = 7; A parks at t = 13 (D1); last 0 is B7 at t = 14; B1 parks at t = 16. Again at 2 from **15 = 2·7 + 1**, not from 4·3 = 12.

### Small ends (CHECKED BY HAND)
- 2 · 1 (B the one self): x_B1 = +, 0, −, +, −, …; x of A alternating throughout. Again at 2 from 3 = 2·1 + 1.
- 1 · 3 (A the one self, offered by itself along and by B1 across): x_A1 = +, 0, −, 0, +, −, +, …; B's zeros at B1 (2), B2 (4), B3 (6). Again at 2 from 7 = 2·3 + 1. Here there is no D2 at momentary 3 (the across offering is itself a 0), so the route differs from §3 though the number agrees; §3's proof is for m ≥ 3.

## 3. Why the 0s end

### 3.1 The states in which every self inverts at every momentary (PROVED)

Suppose every self inverted at t−1, so each offering at t is the offerer's parity at t. A self not at the crossing inverts iff it is unlike its along prior. A crossing self inverts iff it is unlike its along prior **or** unlike the other crossing self (§1). If all invert at t, c(t+1) = −c(t), the same relations hold, and all invert at t+1. So the set is closed, and it is exactly:

> each spiral alternating from its self 1 along to its last self; and, at each crossing self, the seam (last, first) unlike or the two crossing selves opposite.

Along a ring the partings are even in number, so an odd spiral has an odd number of like pairs, one at least (step 649): its seam cannot be unlike. Hence, **one spiral at least odd: the all-inverting states are exactly "each spiral alternating from self 1 to its last, the odd spiral's seam alike, and the two crossing selves opposite".** In such a state x(t+1) = −x(t), so the releasings are again at 2 and carry no 0.

Consequences (PROVED):
- "The two crossing selves opposite" is forced in the end state by the odd spiral's seam: it is the only way the crossing self of an odd spiral can invert at each momentary.
- **The seam is not healed and the like pair is not undone.** It is still there at every momentary in the grids (2 · 3: B3 and B1 alike from 7 on; 3 · 5: A3, A1 alike and B5, B1 alike from 13 on). An odd spiral cannot alternate all round, alone or crossed. What ends is the 0.
- What the crossing offering supplies at the seam: the other parity. The crossing self is offered its own parity along (its last self, alike with it) and the other parity across (the other crossing self, opposite): + and − together, 0 surfaces, a changing (cell D1). Alone it would be offered its own parity only: a changing that is not, a 0.
- Why the pair then stays: a pattern moves along a spiral only by the carrying on at carry momentaries (c_i(t+1) = c_{i−1}(t)). Once every self inverts at every momentary the pattern no longer moves; the like pair rests at the seam with the crossing self as its receiver, and D1 is the cell at every momentary after.

### 3.2 Both odd, 3 ≤ m < n: the course of events (PROVED)

**Until 2m+1 both run as alone and the crossing selves are alike.** By §1 a crossing self can depart from its spiral alone only at D1 or D2, i.e. only with the like pair at the seam: for B at 2 and then not before 2n+1; for A at 2 and then not before 2m+1. At 2 both are offered + along and + across (a(2) = b(2) = +, seams alike): both carry on, as alone. From c_1(2+2k) = (−1)^k · c_{m+1−k}(2) and c_j(2) = + at odd j, − at even j (m+1 even, so m+1−k has the parity of k): c_1(2+2k) = −, k = 1..m. So alone, self 1 carries − at even momentaries 4..2m+2 and + at odd momentaries 3..2m+1; the same for B to 2n+2. Hence a(t) = b(t) for t ≤ 2m+1.

**Event E1, momentary 2m+1 (D2 at A1).** A_m carried on at 2m (receiver k = m): A1's along offering is 0. B1 inverted at 2m (2 < 2m < 2n+1), so the across offering is b(2m+1) = + = a(2m+1). + surfaces, A1's own parity: A1 carries on. (Grids: t = 7.)

After E1:
- a(2m+2) = + while b(2m+2) = −: **the crossing selves are opposite from momentary 2m+2 on.**
- c(2m+2) of A is (+, +, −, +, −, …): like pair (1, 2), A1 having shared 0. At 2m+2: A2 is offered 0, inverts; each later self is offered the unlike parity, inverts; A1 is offered − (A_m) and − (B1), carrying +, inverts. All invert; 2m+3 is a carry momentary with A2 the receiver. So **A's rhythm is moved by one momentary**: its carry momentaries are now odd, receiver A_k at 2m−1+2k, A_m at 4m−1, the pair at the seam (A1 receiver) at 4m+1. By the same count as above, a = + at even momentaries 2m+2..4m and − at odd momentaries 2m+3..4m+1, the opposite of B alone (− even, + odd).
- A1 can next depart at 4m (D2?) and 4m+1 (D1?); B1 at 2n+1 (D2?) and 2n+2 (D1?).

**At the momentary after a last self's 0 (4m for A1, 2n+1 for B1):** along 0, across the other crossing self's parity, which is opposite: the other parity surfaces, it inverts, as alone. No D2.

**Event E2 (D1), at 4m+1 for A1 and 2n+2 for B1:** the like pair is at the seam, the along offering is its own parity, the across offering is the opposite parity: + and − together, 0, it inverts. Every self of that spiral inverts at that momentary and, by §3.1, at every momentary after, so long as the other crossing self goes on inverting and opposite. The spiral is *parked*; its crossing self now alternates each momentary, continuing the same even/odd parities, so the opposition is kept.

Order of the two parkings (n odd, so n ≠ 2m):
- n < 2m: 2n+2 ≤ 4m. B parks first (A1 inverts at every momentary of 2m+2..4m+1, so B1 is offered a(t) = −b(t) throughout); then A's checks at 4m and 4m+1 meet b = −, + as required. Last 0s: B_n at 2n, A_m at 4m−1 > 2n. (3 · 5 grid: n = 2m−1, the two meet at momentary 12.)
- n > 2m: 4m+1 < 2n+1. A parks first while B still runs as alone (b = − even, + odd); then B's checks at 2n+1 and 2n+2 meet a = −, +. Last 0s: A_m at 4m−1, B_n at 2n > 4m−1. (3 · 7 grid.)

After both are parked the state is in the set of §3.1, closed: every self inverts at every momentary.

### 3.3 One even, one odd (m even, n odd ≥ 1) (PROVED)

A alternates all round. By induction every self of A inverts at every momentary whatever comes across: each is offered along the parity other than its own, and A1's surfacing is then that parity or 0. So a = + at even, − at odd momentaries. At 2: A1 is offered − (A_m) and + (B1): 0, inverts; B1 is offered + and +: carries on. **Opposite from momentary 3.** B then runs as alone (− even, + odd from 3), opposite to A; at 2n+1 B1 is offered 0 and −, inverts; at 2n+2 it is offered its own parity along and the other across: D1, parked. Last 0: B_n at 2n.

## 4. The from-momentary

"Again from this momentary on" = the least T with x(t+2) = x(t) for all t ≥ T = one more than the momentary of the last 0 (the momentary T−1 carries a 0 that T+1 does not).

**PROVED:**
- both odd, 3 ≤ m < n: **T = max(4m, 2n+1)** — 4m at n < 2m, 2n+1 at n > 2m;
- m even, n odd (either the larger): **T = 2n+1**.

Arithmetic against the eight rows:

| row | 4m | 2n+1 | formula | table |
|---|---|---|---|---|
| 2 · 3 (even · odd) | — | 7 | 7 | 7 |
| 3 · 5 | 12 | 11 | 12 | 12 |
| 5 · 7 | 20 | 15 | 20 | 20 |
| 7 · 11 | 28 | 23 | 28 | 28 |
| 11 · 13 | 44 | 27 | 44 | 44 |
| 13 · 17 | 52 | 35 | 52 | 52 |
| 17 · 59 | 68 | 119 | 119 | 119 |
| 9 · 15 | 36 | 31 | 36 | 36 |

All eight agree. Seven rows fall on the 4m or even branch; only 17 · 59 tests 2n+1 at both odd, so 3 · 7 was stepped by hand as well (15). The threshold n > 2m is the torus's threshold of step 243 (q more than twice p), here derived.

"Again at 2" and "opposite from it on" are PROVED for the same cases; opposite holds earlier than the table says: from 2m+2 (both odd), from 3 (one even).

## 5. What the deriving needs, and what it does not show

- **Prime: not needed.** Only the parities of m and n and which is the smaller enter. 9 · 15 obeys the same formula. PROVED.
- **Different: needed.** At m = n with the same opening, exchanging the two spirals leaves the cells and the opening unchanged, so a(t) = b(t) at every momentary: never opposite, and at an odd number D1 can never occur, so a 0 recurs for ever. PROVED (by the symmetry; no grid).
- **One at least odd: needed for "opposite", not for "again at 2".** Both even, opened alternating: A1 and B1 are each offered − along and + across at 2, invert, and every self inverts at every momentary; again at 2 from momentary 1, the crossing selves alike for ever. PROVED.
- Both odd with m = 1: CHECKED BY HAND AT 1 · 3 only (7); the proof of §3.2 assumes m ≥ 3.
- **Step 237's "from each carried pattern other than all selves at one parity": NOT SHOWN.** Everything above is from the one opening of the table's column head (one like pair in each odd spiral, crossing selves alike at first). §3.1 shows what the end state must be from any pattern if it is reached; it does not show that it is reached from patterns with several like pairs or with other first parities at the crossing. All selves at one parity is rightly excepted: every self then does the same at every momentary (+, 0, −, 0, as the one self).
- Step 631 as worded (the eight rows) is derived in full: no row breaks.

## 6. The three sayings, what is exactly true at the cells

(a) *One odd spiral alone is two rounds, the second the first inverted.* PROVED: c_i(t+2) = −c_{i−1}(t) at even t, so after n such steps (2n momentaries, the like pair once round) every self carries its own parity inverted and releases its releasings inverted, and after 4n its own again — the table's row 3 reads +, 0, −, +, −, + then −, 0, +, −, +, −.

(b) *Two spirals crossed at one self of each are two loops at one crossing.* PROVED as to structure only: the cells are two rings of along offerings joined by one pair of across offerings between two selves (one self of each, not one self common to both), and in the end state nothing of either ring's pattern passes into the other — the across offering does one thing, turning the seam's own-parity surfacing into + and − together.

(c) *"The prime loops are twisted figure 8's going both routings."* What is true at the cells is that each odd spiral, prime or not, is a single loop of 2n places passed in two rounds with an inversion (a), and that the across sharing goes both ways between the two crossing selves; that primes are distinguished at the crossing, or that a pattern is routed through the crossing from one loop round the other, is shown by no cell here (9 · 15 follows the same law, and the like pair of each spiral stays in its own spiral).
