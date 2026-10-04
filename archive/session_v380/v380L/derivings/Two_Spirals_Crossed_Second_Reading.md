# X2 — second reader's hand grids, two spirals crossed (steps 658 to 661)

Worked by hand from the cells; nothing executed. Written before X1.md was opened (comparison at the end).

Reading of a row. Momentary t: `carried` is each self's parity going into t; `offered at self 1` is (along from the last self, across from the other self 1), each what was shared at t − 1; `shares` is what each self shares at t (0 = a changing that is not; otherwise its next parity). The carried of t + 1 is the carried of t with every non-0 share's self inverted. A non-crossing self k is at a changing that is not exactly when self k − 1 shared, at t − 1, the parity k carries.

## 1. Spirals of 3 and 7 crossed (A = a1 a2 a3, B = b1 … b7), to momentary 18

| t | A carried | B carried | a1 offered (along, across) | b1 offered (along, across) | A shares | B shares | at a changing that is not | a1 · b1 | like pair A · B |
|---|---|---|---|---|---|---|---|---|---|
| 1 | − + − | − + − + − + − | none | none | + − + | + − + − + − + | — | alike | 3,1 · 7,1 |
| 2 | + − + | + − + − + − + | +, + | +, + | 0 + − | 0 + − + − + − | a1, b1 | alike | 3,1 · 7,1 |
| 3 | + + − | + + − + − + − | −, 0 | −, 0 | − − + | − − + − + − + | — | alike | 1,2 · 1,2 |
| 4 | − − + | − − + − + − + | +, − | +, − | + 0 − | + 0 − + − + − | a2, b2 | alike | 1,2 · 1,2 |
| 5 | + − − | + − − + − + − | −, + | −, + | − + + | − + + − + − + | — | alike | 2,3 · 2,3 |
| 6 | − + + | − + + − + − + | +, − | +, − | + − 0 | + − 0 + − + − | a3, b3 | alike | 2,3 · 2,3 |
| 7 | + − + | + − + + − + − | 0, + | −, + | 0 + − | − + − − + − + | a1 | alike | 3,1 · 3,4 |
| 8 | + + − | − + − − + − + | −, − | +, 0 | − − + | + − + 0 − + − | b4 | opposite | 1,2 · 3,4 |
| 9 | − − + | + − + − − + − | +, + | −, − | + 0 − | − + − + + − + | a2 | opposite | 1,2 · 4,5 |
| 10 | + − − | − + − + + − + | −, − | +, + | − + + | + − + − 0 + − | b5 | opposite | 2,3 · 4,5 |
| 11 | − + + | + − + − + + − | +, + | −, − | + − 0 | − + − + − − + | a3 | opposite | 2,3 · 5,6 |
| 12 | + − + | − + − + − − + | 0, − | +, + | − + − | + − + − + 0 − | b6 | opposite | 3,1 · 5,6 |
| 13 | − + − | + − + − + − − | −, + | −, − | + − + | − + − + − + + | — | opposite | 3,1 · 6,7 |
| 14 | + − + | − + − + − + + | +, − | +, + | − + − | + − + − + − 0 | b7 | opposite | 3,1 · 6,7 |
| 15 | − + − | + − + − + − + | −, + | 0, − | + − + | − + − + − + − | — | opposite | 3,1 · 7,1 |
| 16 | + − + | − + − + − + − | +, − | −, + | − + − | + − + − + − + | — | opposite | 3,1 · 7,1 |
| 17 | − + − | + − + − + − + | −, + | +, − | + − + | − + − + − + − | — | opposite | 3,1 · 7,1 |
| 18 | + − + | − + − + − + − | +, − | −, + | − + − | + − + − + − + | — | opposite | 3,1 · 7,1 |

Record, 3 · 7:
- Shares 0: 2 (a1, b1), 4 (a2, b2), 6 (a3, b3), 7 (a1), 8 (b4), 9 (a2), 10 (b5), 11 (a3), 12 (b6), 14 (b7).
- Crossing selves alike going into momentaries 1 to 7, opposite going into 8 and every momentary after.
- Last momentary carrying a 0: 14 (b7). A's last 0: 11 (a3).
- Sharings again at 2 from momentary 15 (the shares of 14 carry a 0 where the shares of 16 carry +; 15 = 17, 16 = 18).
- Each self of A inverts at every momentary from 12; each self of B from 15.
- a1 offered 0 along and the other parity across at 12 (a changing); a1 with its like pair at the seam offered both parities first at 13. b1 offered 0 along and the other across at 15; seam offered both parities first at 16.

## 2. Spirals of 5 and 7 crossed (A = a1 … a5, B = b1 … b7), to momentary 23

| t | A carried | B carried | a1 offered (along, across) | b1 offered (along, across) | A shares | B shares | at a changing that is not | a1 · b1 | like pair A · B |
|---|---|---|---|---|---|---|---|---|---|
| 1 | − + − + − | − + − + − + − | none | none | + − + − + | + − + − + − + | — | alike | 5,1 · 7,1 |
| 2 | + − + − + | + − + − + − + | +, + | +, + | 0 + − + − | 0 + − + − + − | a1, b1 | alike | 5,1 · 7,1 |
| 3 | + + − + − | + + − + − + − | −, 0 | −, 0 | − − + − + | − − + − + − + | — | alike | 1,2 · 1,2 |
| 4 | − − + − + | − − + − + − + | +, − | +, − | + 0 − + − | + 0 − + − + − | a2, b2 | alike | 1,2 · 1,2 |
| 5 | + − − + − | + − − + − + − | −, + | −, + | − + + − + | − + + − + − + | — | alike | 2,3 · 2,3 |
| 6 | − + + − + | − + + − + − + | +, − | +, − | + − 0 + − | + − 0 + − + − | a3, b3 | alike | 2,3 · 2,3 |
| 7 | + − + + − | + − + + − + − | −, + | −, + | − + − − + | − + − − + − + | — | alike | 3,4 · 3,4 |
| 8 | − + − − + | − + − − + − + | +, − | +, − | + − + 0 − | + − + 0 − + − | a4, b4 | alike | 3,4 · 3,4 |
| 9 | + − + − − | + − + − − + − | −, + | −, + | − + − + + | − + − + + − + | — | alike | 4,5 · 4,5 |
| 10 | − + − + + | − + − + + − + | +, − | +, − | + − + − 0 | + − + − 0 + − | a5, b5 | alike | 4,5 · 4,5 |
| 11 | + − + − + | + − + − + + − | 0, + | −, + | 0 + − + − | − + − + − − + | a1 | alike | 5,1 · 5,6 |
| 12 | + + − + − | − + − + − − + | −, − | +, 0 | − − + − + | + − + − + 0 − | b6 | opposite | 1,2 · 5,6 |
| 13 | − − + − + | + − + − + − − | +, + | −, − | + 0 − + − | − + − + − + + | a2 | opposite | 1,2 · 6,7 |
| 14 | + − − + − | − + − + − + + | −, − | +, + | − + + − + | + − + − + − 0 | b7 | opposite | 2,3 · 6,7 |
| 15 | − + + − + | + − + − + − + | +, + | 0, − | + − 0 + − | − + − + − + − | a3 | opposite | 2,3 · 7,1 |
| 16 | + − + + − | − + − + − + − | −, − | −, + | − + − − + | + − + − + − + | — | opposite | 3,4 · 7,1 |
| 17 | − + − − + | + − + − + − + | +, + | +, − | + − + 0 − | − + − + − + − | a4 | opposite | 3,4 · 7,1 |
| 18 | + − + − − | − + − + − + − | −, − | −, + | − + − + + | + − + − + − + | — | opposite | 4,5 · 7,1 |
| 19 | − + − + + | + − + − + − + | +, + | +, − | + − + − 0 | − + − + − + − | a5 | opposite | 4,5 · 7,1 |
| 20 | + − + − + | − + − + − + − | 0, − | −, + | − + − + − | + − + − + − + | — | opposite | 5,1 · 7,1 |
| 21 | − + − + − | + − + − + − + | −, + | +, − | + − + − + | − + − + − + − | — | opposite | 5,1 · 7,1 |
| 22 | + − + − + | − + − + − + − | +, − | −, + | − + − + − | + − + − + − + | — | opposite | 5,1 · 7,1 |
| 23 | − + − + − | + − + − + − + | −, + | +, − | + − + − + | − + − + − + − | — | opposite | 5,1 · 7,1 |

Record, 5 · 7:
- Shares 0: 2 (a1, b1), 4 (a2, b2), 6 (a3, b3), 8 (a4, b4), 10 (a5, b5), 11 (a1), 12 (b6), 13 (a2), 14 (b7), 15 (a3), 17 (a4), 19 (a5).
- Crossing selves alike going into momentaries 1 to 11, opposite going into 12 and every momentary after.
- Last momentary carrying a 0: 19 (a5). B's last 0: 14 (b7).
- Sharings again at 2 from momentary 20, the crossing selves opposite: Exhibit ONE's row 5 · 7 agrees.
- Each self of B inverts at every momentary from 15; each self of A from 20.
- b1 offered 0 along and the other parity across at 15, seam offered both parities first at 16. a1 offered 0 along and the other across at 20, seam offered both parities first at 21.

## 3. Spirals of 3 and 3 crossed, to momentary 14

B is alike A self for self at every momentary (written once; the across offering at a1 is b1's share = a1's own last share: 0 or a1's own parity, never the other parity).

| t | A = B carried | self 1 offered (along, across) | A = B shares | at a changing that is not | like pair |
|---|---|---|---|---|---|
| 1 | − + − | none | + − + | — | 3,1 |
| 2 | + − + | +, + | 0 + − | self 1 | 3,1 |
| 3 | + + − | −, 0 | − − + | — | 1,2 |
| 4 | − − + | +, − | + 0 − | self 2 | 1,2 |
| 5 | + − − | −, + | − + + | — | 2,3 |
| 6 | − + + | +, − | + − 0 | self 3 | 2,3 |
| 7 | + − + | 0, + | 0 + − | self 1 | 3,1 |
| 8 | + + − | −, 0 | − − + | — | 1,2 |
| 9 | − − + | +, − | + 0 − | self 2 | 1,2 |
| 10 | + − − | −, + | − + + | — | 2,3 |
| 11 | − + + | +, − | + − 0 | self 3 | 2,3 |
| 12 | + − + | 0, + | 0 + − | self 1 | 3,1 |
| 13 | + + − | −, 0 | − − + | — | 1,2 |
| 14 | − − + | +, − | + 0 − | self 2 | 1,2 |

Record, 3 · 3: alike self for self at every momentary, crossing selves alike throughout; the 0 goes on (2, 4, 6, 7, 9, 11, 12, 14 …); carried and shares of 7 are those of 2, so the sharings come again at 5 = 2m − 1 from momentary 2, never at 2.

## Extra, 2 · 3 (for 660's "m even and n odd" clause), to momentary 8

| t | A carried | B carried | A shares | B shares | 0 at | a1 · b1 |
|---|---|---|---|---|---|---|
| 1 | − + | − + − | + − | + − + | — | alike |
| 2 | + − | + − + | − + | 0 + − | b1 | alike |
| 3 | − + | + + − | + − | − − + | — | opposite |
| 4 | + − | − − + | − + | + 0 − | b2 | opposite |
| 5 | − + | + − − | + − | − + + | — | opposite |
| 6 | + − | − + + | − + | + − 0 | b3 | opposite |
| 7 | − + | + − + | + − | − + − | — | opposite |
| 8 | + − | − + − | − + | + − + | — | opposite |

Opposite from 3, last 0 at 6, again at 2 from 7 = 2n + 1.

## The steps against the grids

658. The nine cells of a crossing self (along × across, each own / other / 0): own·own not, own·other changing, own·0 not, other·own changing, other·other changing, other·0 changing, 0·own not, 0·other changing, 0·0 changing. Against the lone spiral (along alone: own not, other changing, 0 changing) exactly two differ: own·other and 0·own. Seen: own·other at 13+ (3·7 a1), 16+ (b1); 0·own at 7 (3·7 a1), 11 (5·7 a1), 7 and 12 (3·3). HOLDS.

659. From 15 (3·7) and 20 (5·7) each spiral alternates first to last, last and first alike, a1 and b1 opposite, and every self inverts. Converse by the cells: a non-crossing self inverts after an inverting prior exactly when it differs from it; a crossing self of an odd alternating spiral is offered its own parity along, so it inverts exactly when the across is the other parity. A like pair is present in each spiral at every momentary of all three grids (last column), at the seam from 12/13 (A, 3·7), 15 (B), 20 (A, 5·7). HOLDS.

660. 3·7: 7, 8, 13, 16, 15 all met. 5·7: 11, 12, 21, 16, 20 all met. 2·3: 7, opposite from 3. HOLDS, with one precision: each self of a spiral already inverts one momentary before its seam is offered both parities (lesser from 4m: 12, 20; greater from 2n + 1: 15), the crossing self there offered a 0 along and the other parity across. 4m + 1 and 2n + 2 are the first momentaries of "both parities at the seam", not the first of "each self inverts".

661. 3·3 grid: alike self for self, crossing alike, 0 never ends. Two even spirals: each self offered the other parity along, the crossing self too (last and first opposite), so all invert from momentary 1. HOLDS.

## My own deriving for every odd m < n (m from 3)

Along a spiral, when self 1 is at a changing that is not at T and the rest alternate, self k is at a changing that is not at T + 2(k − 1) and at no momentary between (the like pair k − 1, k rests two momentaries: at the first self k is offered the 0 and inverts with k − 1, at the second it is offered k − 1's parity, its own). So the last self's 0 is at T + 2(L − 1), L the length.
- Momentary 2: both self 1 offered own along and own across: not. T = 2 in both. Momentary 3: along other, across 0: changing. 4 to 2m: along other (like pair not at the seam), so a changing whatever the across; both invert together, alike.
- 2m + 1: a_m shared 0 at 2m; b1 inverted at 2m and is alike, so across is a1's own: cell 0·own, not. b1: B's like pair is at (m, m + 1), not the seam since m < n; along other: changing. Opposite going into 2m + 2. T = 2m + 1 for A: a_m's 0 at 4m − 1.
- Joint induction on t ≥ 2m + 2, both inverted at every momentary since 2m + 2 and opposite: a1 is offered along other (t ≤ 4m − 1), 0 (t = 4m), own (t ≥ 4m + 1) and across b1's last share, non-0 and other: changing in each. b1 is offered along other (t ≤ 2n), 0 (t = 2n + 1), own (t ≥ 2n + 2); across 0 at t = 2m + 2 alone (2m + 2 ≤ 2n, along other), else non-0 and other: changing in each.
- Last 0 at the greater of 4m − 1 and 2n; again at 2 from the greater of 4m and 2n + 1; n odd, so n < 2m gives 2n + 1 ≤ 4m − 1 and n > 2m gives 2n + 1 ≥ 4m + 3.

## Comparison with X1.md

Written after reading X1.md.

- Grids: X1's 3 · 7 grid (momentaries 1 to 16) is mine cell for cell, carried and shared. X1's 2 · 3 grid is mine cell for cell. X1 stepped no 5 · 7 grid (arithmetic against the row only) and no 3 · 3 grid (symmetry only); mine supply both and agree with its formula and its symmetry argument.
- X1 §1 (six rows, D1 and D2) is my nine cells; step 658 follows.
- X1 §3.1 (the closed all-inverting set) is a proof for every pair of spirals, one at least odd; step 659 follows. "The like pair is still there" is cited at the grids but is proved by step 649's count (an odd ring's like pairs are odd in number), so it does not rest on the grids.
- X1 §3.2 is a proof for every odd 3 ≤ m < n. I followed each line: c_1(2 + 2k) = (−1)^k · c_{m+1−k}(2) = − (m + 1 even); E1 at 2m + 1; A's rhythm moved one momentary (the state going into 2m + 2 is the state going into 3, moved 2m − 1 on); the checks at 4m, 4m + 1, 2n + 1, 2n + 2. One thing left unwritten: "so long as the other crossing self goes on inverting and opposite" is a mutual condition, closed only by induction on the momentary. It closes: each check uses the other crossing self's share one momentary earlier, which is unconditional (along the other parity) up to 4m − 1 for A1 and 2n for B1, and at n = 2m − 1 B1's check at 4m uses A1's share at 4m − 1, A1's check at 4m uses B1's at 4m − 1 = 2n + 1, itself resting on A1's at 4m − 2. No circle. A thin place, not a gap.
- X1 §3.3 (one even) is a proof; my 2 · 3 grid agrees.
- X1 §5 "a 0 recurs for ever at m = n" is proved (never opposite, so never in §3.1's set); my 3 · 3 grid shows it and adds: the sharings come again at 5 = 2m − 1 from momentary 2.
- Resting on grids alone in X1: the lesser a spiral of one self (1 · 3, 2 · 1). Step 660 says "m the lesser from 3", so the step does not lean on it.
- Not shown anywhere (X1 says so itself): step 237's "from each carried pattern"; only the one opening is derived.
- Reading needed for 660's numbers: "alike to momentary 2m + 1 / opposite from 2m + 2" counts the parity a self carries into a momentary. Counted as Exhibit ONE's "Carried next" column the same facts read alike to 2m, opposite from 2m + 1.
- Precision (not a falsity): each self of the lesser inverts from 4m and of the greater from 2n + 1, one momentary before 660's 4m + 1 and 2n + 2; at that earlier momentary the crossing self is offered a 0 along and the other parity across. 660's own closing clause (again at 2 from 4m, from 2n + 1) already uses the earlier pair.
