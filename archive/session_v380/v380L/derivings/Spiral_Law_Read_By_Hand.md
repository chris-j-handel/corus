# S1: steps 646 to 649 read fresh, by hand

Read only. Nothing executed, no simulation. Each table below is written by hand from the cells
(resolver lines 13 to 34 for one self, 42 to 60 for the passing on).

Notation. c_i(t): the parity self i carries entering momentary t. o_i(t): what is offered to self i
at t, which is s_(i-1)(t-1), what its prior self shared at t-1 (self 1's prior is the last self).
s_i(t): what self i shares at t. S: the pattern carried one self on, (S c)_i = c_(i-1).

Cells used: o none or 0 -> none surfaces -> the self inverts and shares its next parity.
o = the other parity -> inverts, shares its next parity. o = own parity -> carries on, shares 0.

---

## 1. The base law (step 233), as an induction

Claim, for any number of selves n >= 1 and any opening pattern, each self at a parity, none offered
from beyond:

- (O) at each odd momentary each self inverts, and so shares its next parity (never 0);
- (E) at each even momentary each self's next parity is the parity its prior self carries at that
  momentary: c_i(2m+1) = c_(i-1)(2m). The self shares 0 if it was alike with its prior self at that
  momentary, and shares its next parity (= the prior self's parity) if it was not.

Induction.

Base, momentary 1. Nothing has been shared: none surfaces at each self; each inverts and shares its
next parity. (O) at 1.

Step A, (O) at 2m-1 gives (E) at 2m. At 2m-1 the prior self inverted and shared its next parity, so
o_i(2m) = s_(i-1)(2m-1) = c_(i-1)(2m): the offering at an even momentary is the parity the prior
self carries at that momentary, never 0, never none.
  - If c_(i-1)(2m) = c_i(2m): the surfacing is the self's own parity, a changing that is not; it
    carries on, shares 0, c_i(2m+1) = c_i(2m) = c_(i-1)(2m).
  - If not: there are only two parities, so the offering is the other one; it inverts,
    c_i(2m+1) = -c_i(2m) = c_(i-1)(2m), and shares that.
  Either way c_i(2m+1) = c_(i-1)(2m). (E) at 2m.

Step B, (E) at 2m gives (O) at 2m+1. The offering at 2m+1 is s_(i-1)(2m), which by step A is one of
two things:
  - 0, if the prior self carried on at 2m. A 0 is passed over; none surfaces; the self inverts.
  - the prior self's next parity c_(i-1)(2m+1), if the prior self inverted at 2m. The prior self
    inverted, so c_(i-1)(2m+1) = -c_(i-1)(2m). The self's own parity at 2m+1 is, by (E),
    c_i(2m+1) = c_(i-1)(2m). So the offering is -c_i(2m+1): the other parity. The self inverts.
  Neither is the self's own parity: the 0 is no parity, and the prior self's next parity is the
  inverse of the very parity the self has just taken from it. (O) at 2m+1.

The induction uses only: each self is at a parity; each self has exactly one offering, from one
prior self; nothing arrives at momentary 1. It uses nothing of n and nothing of the pattern. At
n = 1 the prior self is the self; at n = 2 each is the other's prior. No case fails.

Consequences used below:
- c(2) = -c(1); c(3) = -S c(1); and in general
  c(2j+1) = (-1)^j S^j c(1),  c(2j+2) = (-1)^(j+1) S^j c(1).
- c_(i+1)(t+2) = -c_i(t) at each t, odd or even (odd t: invert then carry on; even t: carry on then
  invert).
- s(2j+1) = c(2j+2) (all non-0); s_i(2j+2) = 0 at the receiving self of a like pair of c(2j+2),
  else c_i(2j+3).

### Hand tables (carried parities c(t), then sharings s(t))

**Spiral of 1, opened -.**
t1: none -> invert, s +, next +. t2: offered + (its own sharing), carries + -> on, s 0.
t3: offered 0 -> invert, s -, next -. t4: offered -, carries - -> on, s 0. t5 as t1.
Carried 1..5: -, +, +, -, -. Sharings: +, 0, -, 0. Exhibit ONE row 1: +, 0, -, 0, ... : agrees. Again at 4.
(E) at n = 1 reads c(2m+1) = c(2m): true.

**Spiral of 2 opened alike (+,+).**
c1 ++ ; t1 s --; c2 --; t2 each offered -, carries - -> on, s 00; c3 --; t3 offered 0 -> invert,
s ++; c4 ++; t4 on, s 00; c5 ++. Again at 4. Exhibit ONE "Two selves, +,+ both ways": -,0,+,0: agrees.

**Spiral of 2 opened opposite (+,-).**
c1 +-; t1 s -+; c2 -+; t2 self 1 offered + carries - -> invert, s +; self 2 offered - carries + ->
invert, s -; c3 +-. Again at 2. Exhibit ONE row 2 (2) and "+,- both ways": agree.

**Spiral of 3 opened -,+,-.**

| t | carried c(t) | offered (to 1,2,3) | shared s(t) |
|---|---|---|---|
| 1 | - + - | none | + - + |
| 2 | + - + | + + - | 0 + - |
| 3 | + + - | - 0 + | - - + |
| 4 | - - + | + - - | + 0 - |
| 5 | + - - | - + 0 | - + + |
| 6 | - + + | + - + | + - 0 |
| 7 | + - + | 0 + - | - + - |
| 8 | - + - | - - + | 0 - + |
| 9 | - - + | + 0 - | + + - |
| 10 | + + - | - + + | - 0 + |
| 11 | - + + | + - 0 | + - - |
| 12 | + - - | - + - | - + 0 |
| 13 | - + - | | |

Self 1 shares +,0,-,+,-,+,-,0,+,-,+,- : Exhibit ONE row 3 exactly. Again at 12.
Note c(8) = - + - is the opening pattern at an even momentary (7 on); the selves then go otherwise
(c(9) is not c(2)). See section 3, the note on "at itself again".

**Spiral of 3 all alike (-,-,-).**
c1 ---; s1 +++; c2 +++; t2 each offered own parity -> on, s 000; c3 +++; t3 offered 0 -> invert,
s ---; c4 ---; t4 on, s 000; c5 ---. Again at 4. (c(4) = c(1) bare, 3 on.)

**Spiral of 4 opened -,-,+,+.**

| t | carried | offered (to 1,2,3,4) | shared |
|---|---|---|---|
| 1 | - - + + | none | + + - - |
| 2 | + + - - | - + + - | - 0 + 0 |
| 3 | - + + - | 0 - 0 + | + - - + |
| 4 | + - - + | + + - - | 0 + 0 - |
| 5 | + + - - | - 0 + 0 | - - + + |
| 6 | - - + + | + - - + | + 0 - 0 |
| 7 | + - - + | 0 + 0 - | - + + - |
| 8 | - + + - | - - + + | 0 - 0 + |
| 9 | - - + + | | |

Self 1 shares +,-,+,0,-,+,-,0. First as they were at 8 (carried at momentary 9 = momentary 1, and
each sharing from 9 as from 1). At 4 on (momentary 5) the pattern is the opening inverted, + + - -,
not itself. The bare opening parities are also carried at momentary 6 (5 on), an even momentary,
and the selves then go otherwise (sharings + 0 - 0, not + + - -).

**Spiral of 4 opened -,+,+,+.**

| t | carried | offered | shared |
|---|---|---|---|
| 1 | - + + + | none | + - - - |
| 2 | + - - - | - + - - | - + 0 0 |
| 3 | - + - - | 0 - + 0 | + - + + |
| 4 | + - + + | + + - + | 0 + - 0 |
| 5 | + + - + | 0 0 + - | - - + - |
| 6 | - - + - | - - - + | 0 0 - + |
| 7 | - - - + | + 0 0 - | + + + - |
| 8 | + + + - | - + + + | - 0 0 + |
| 9 | - + + + | | |

Again at 8. Each odd row: every self inverted. Each even row: next parity = prior self's parity.

**Spiral of 5 opened -,+,-,+,- (Exhibit ONE's opening), 20 momentaries.**

| t | carried (1..5) | offered (to 1..5) | shared |
|---|---|---|---|
| 1 | - + - + - | none | + - + - + |
| 2 | + - + - + | + + - + - | 0 + - + - |
| 3 | + + - + - | - 0 + - + | - - + - + |
| 4 | - - + - + | + - - + - | + 0 - + - |
| 5 | + - - + - | - + 0 - + | - + + - + |
| 6 | - + + - + | + - + + - | + - 0 + - |
| 7 | + - + + - | - + - 0 + | - + - - + |
| 8 | - + - - + | + - + - - | + - + 0 - |
| 9 | + - + - - | - + - + 0 | - + - + + |
| 10 | - + - + + | + - + - + | + - + - 0 |
| 11 | + - + - + | 0 + - + - | - + - + - |
| 12 | - + - + - | - - + - + | 0 - + - + |
| 13 | - - + - + | + 0 - + - | + + - + - |
| 14 | + + - + - | - + + - + | - 0 + - + |
| 15 | - + + - + | + - 0 + - | + - - + - |
| 16 | + - - + - | - + - - + | - + 0 - + |
| 17 | - + - - + | + - + 0 - | + - + + - |
| 18 | + - + + - | - + - + + | - + - 0 + |
| 19 | - + - + + | + - + - 0 | + - + - - |
| 20 | + - + - - | - + - + - | - + - + 0 |
| 21 | - + - + - | | |

Self 1's sharings 1..20: +,0,-,+,-,+,-,+,-,+,-,0,+,-,+,-,+,-,+,-.
Exhibit ONE row 5, momentaries 1 to 12: +,0,-,+,-,+,-,+,-,+,-,0. Agrees at each of the twelve.
Again at 20 (c(21) = c(1); no earlier odd momentary carries the opening pattern: c(3), c(5), ..., c(19)
are all other, c(11) the opening inverted). The one 0 at each even momentary sits at self 1, 2, 3,
4, 5, 1, 2, 3, 4, 5: one self on at each second momentary. c(12) = c(1) bare at the even momentary 12.

Base law: holds at every row of every table. No failure found; none possible by the induction.

---

## 2. Step 646

"a parity at a self is two momentaries on at the next self at the other parity": this is
c_(i+1)(t+2) = -c_i(t), a consequence of (O) and (E) at every t (shown above), for every pattern.
At a like pair it says no more than the base law: at the even momentary the receiving self of a
like pair carries on (shares 0) and yet its next parity is its prior self's parity, because the two
were alike. The saying is of parities carried, not of changings shared, and it is true there too. It
is a true saying of the base law and no more.

The counting. Places: (self i, parity s), 2n of them. The move (i, s) -> (i+1, -s) is adding (1, 1)
in (selves round n) x (two parities). After m moves a place is at itself iff n divides m and m is
even: the least m is 2n at n odd and n at n even. Every place lies on a loop of that one length, so:
- n odd: 2n places / 2n = one loop of 2n places; each self is passed twice, n moves apart, n odd, so
  once at each parity. 2n moves at two momentaries each = 4n momentaries. n = 1: the two places
  (self, -) and (self, +), one loop of 2, again at 4. Correct.
- n even: 2n / n = two loops of n places; each self once on each; (i, s) and (i, -s) on different
  loops (a loop holds self i only at the parity fixed by whether i is odd or even from its opening).
  The move never leaves a loop: neither reaches the other. n = 2: (1,-)->(2,+)->(1,-) and
  (1,+)->(2,-)->(1,+): two loops of 2. Correct.

646: PROVED for every n and every pattern (the move does not depend on the pattern).
Wording only: "at four times the number of momentaries" reads as four times a number of momentaries;
meant: "at four times the number of selves, in momentaries". Not said and true: at an even number
each loop is at its opening place again at twice the number.

---

## 3. Step 647

First sentence, any n. From c(2j+1) = (-1)^j S^j c(1): the carried pattern at momentary 1+2k is the
opening pattern iff c_i = (-1)^k c_(i-k) for each i: "each self's parity is that of the self k
prior, inverted at an odd k". The least such k gives the first odd momentary 1+2k at which the
pattern is the opening pattern; from it each momentary goes as from 1. So 2k momentaries.

The step does not say why no odd number of momentaries can be a coming again. It cannot: a coming
again at an odd T would make the sharings of an even momentary equal those of an odd one, all non-0,
so no like pair, so the spiral alternates along and is at 2 (s(1) = -c, s(2) = c, not alike), an
even number. So the period is even always, and it is 2k. This closes the first sentence for every n.

Second sentence, n odd. If k is odd, c_i = -c_(i-k); carried n times round, c_i = (-1)^n c_i = -c_i:
no pattern. So k is even and c_i = c_(i-k). The shifts at which a pattern is alike with itself are
exactly the multiples of the least one, d, and d divides n; n odd so d odd; the least even multiple
is 2d. k = 2d, 4d momentaries. PROVED.

Checks:
- 3 all alike: d = 1, 4. Hand: 4. Agrees.
- 3 selves -,+,-: d = 3, 12. Hand: 12. Agrees (and Exhibit ONE: 12).
- 5 selves -,+,-,+,-: d = 5, 20. Hand: 20. Agrees.
- 9 selves -,+,-,-,+,-,-,+,-: d = 3, 12. Hand, 12 momentaries (self 1's prior is self 9, which
  carries and shares as self 3; each self goes as the self 3 prior, alike carried and alike offered
  at each momentary):

| t | carried | shared |
|---|---|---|
| 1 | -+- -+- -+- | +-+ +-+ +-+ |
| 2 | +-+ +-+ +-+ | 0+- 0+- 0+- |
| 3 | ++- ++- ++- | --+ --+ --+ |
| 4 | --+ --+ --+ | +0- +0- +0- |
| 5 | +-- +-- +-- | -++ -++ -++ |
| 6 | -++ -++ -++ | +-0 +-0 +-0 |
| 7 | +-+ +-+ +-+ | -+- -+- -+- |
| 8 | -+- -+- -+- | 0-+ 0-+ 0-+ |
| 9 | --+ --+ --+ | ++- ++- ++- |
| 10 | ++- ++- ++- | -0+ -0+ -0+ |
| 11 | -++ -++ -++ | +-- +-- +-- |
| 12 | +-- +-- +-- | -+0 -+0 -+0 |
| 13 | -+- -+- -+- | |

  Again at 12, three like pairs, three 0s at each even momentary. Agrees.
- 4 selves alternating: k = 1 (each self the inverse of its prior, odd k inverts): 2. Hand
  (Exhibit ONE row 4): 2. Agrees.
- 4 selves -,-,+,+: k = 1? self 2 is not the inverse of self 1: no. k = 2? k even, so each self must
  be ALIKE with the self 2 prior; self 3 (+) and self 1 (-) are not: no. k = 3? self 1 (-) against
  self 2 inverted (+): no. k = 4: yes. The law gives k = 4, 8 momentaries. The hand gives 8.
  "k = 2, 4 momentaries" is a misreading of the law: at a shift of 2 this pattern is inverted, and
  the law inverts only at an odd k. At 4 on the pattern is the opening inverted. The earlier readers'
  "first as they were at 8" is right, and it is what the law gives.
- 4 selves -,+,+,+: k = 4, 8. Hand: 8. Agrees.
- 2 selves alike: k = 1 no (alike, not inverse); k = 2 yes: 4. Hand: 4. Agrees.
- 2 selves opposite: k = 1: 2. Hand: 2.
- 6 selves -,+,-,-,+,-: k = 1 no (selves 3, 4 alike); k = 2 no (self 5 +, self 3 -); k = 3 no (each
  self is ALIKE with the self 3 prior, and odd k asks the inverse); k = 4 no (self 5 +, self 1 -);
  k = 5 no (self 3 - against self 4 inverted +); k = 6 yes. The law gives 12. Each self goes as
  the self 3 prior, so the table is the 3-spiral's twice over: 12 by hand.
- one more, 6 selves -,-,-,+,+,+: k = 3 (each self the inverse of the self 3 prior, k odd): 6.
  By hand, carried at odd momentaries: ---+++, -+++--, ++---+, ---+++ at momentary 7. Self 1's
  sharings +,-,+,0,-,0. Again at 6. Agrees.

The law does not fail at an even number: the first sentence is the law there. The second sentence
speaks only of an odd number. Said out for every number, with d the least alike shift:
- d odd: four times d (any number of selves, odd or even: 2 alike at 4, 6 selves -,+,-,-,+,- at 12);
- d even, each self the inverse of the self half-of-d prior, that shift odd: d momentaries
  (alternating: d = 2, at 2; -,-,-,+,+,+: d = 6, at 6);
- d even otherwise: twice d (-,-,+,+ and -,+,+,+: d = 4, at 8).

**"The pattern at itself again": carried parities, sharings, or both?** As a coming again (each
momentary from it on as from the first) both, at the same number 2k: the sharings at odd momentaries
are the carried parities of the even ones, and one self's sharings alone give the whole pattern
(s_1(2j+1) = (-1)^(j+1) c_(1-j)), so each self's sharings, the spiral's sharings, and the carried
parities all have the one period 2k. The sharings are FIRST as at momentary 1 at exactly 2k.
But the bare carried parities equal the opening pattern earlier, at an even momentary 2j+2, j the
least at which each self's parity is that of the self j prior inverted at an EVEN j: at an odd
spiral j = d, momentary 2d+2 (3 alike: momentary 4; -,+,-: momentary 8; 5 selves: momentary 12);
at -,-,+,+ momentary 6. There the selves do not go as at momentary 1 (an even momentary carries
on, an odd inverts). So the step is true said of the sharings, or of the parities "carried at an
odd momentary"; said of the bare carried parities, "at the least" and 648's "at none between" are
not true. Exact words to add to 647: "at itself again: each self's sharings again, the parities
carried at an odd momentary again".

647: PROVED for every case, with the even-period line supplied above and "at itself again" read as
the sharings.

---

## 4. Step 648

Odd prime p: d divides p, so d = 1 (all alike) or p; 4 or 4p, exactly, none between. PROVED from 647.

The prime 2: d = 1, two alike: k = 2, at 4 (hand: 4). d = 2, two opposite: k = 1, at 2 (hand: 2;
Exhibit ONE row 2: 2; "Two selves +,- both ways"). 2 is neither 4 nor four times the prime (8).
648 as worded, "At a prime number of selves", is FALSE at the prime 2, the pattern opposite. The
step cites 647, whose odd law does not cover 2.

Replacement: "At an odd prime number of selves the least alike shift is one, each self alike, or the
prime, step 647: each pattern is again at 4 momentaries or at four times the prime, and at none
between. At two selves the two alike are again at 4 and the two opposite at 2."
Adding: "an odd prime spiral at 4 or at four times the prime, none between; two selves at 4 or at 2."
The section's Entering line carries the same words and wants the same "odd".

Second sentence: true. A pattern alike at a factor f's shift has d dividing f, and is again at 4f;
it is FIRST again at 4f only when f is its least alike shift. Tighter: "a pattern whose least alike
shift is the factor". Nine selves: d = 1, 3, 9: 4, 12, 36. Step 230 says "nine selves, each pattern
at its own, at 4, at 12 or at 36": the citation is right.

---

## 5. Step 649

Round the spiral there are n pairs (a self and the self it receives from). Going once round and
coming to the first parity again, the partings are even in number (each - to + met by one + to -).
Like pairs = n less an even number: odd at n odd, even at n even. PROVED, any pattern.
The number is the same at each momentary: the carried pattern is always the opening pattern carried
on and perhaps inverted, and neither alters which neighbours are alike.

n = 1: one pair, the self with itself (it receives from itself); no parting (0, even); one like
pair (odd). And it is one in the cells: at each even momentary the self is offered its own sharing,
its own parity, and shares 0 (row 1: +, 0, -, 0). So yes, the one self is a like pair with itself.
n = 2: two pairs (2 to 1, 1 to 2): alike 2, opposite 0. Even.

"An odd spiral carries a like pair at each momentary": odd, so at least one. "and a 0 at each even
momentary": by (E) the receiving self of each like pair shares 0 at each even momentary. "an even
spiral alternating along carries none": no like pair, so no 0 at any momentary; each self inverts at
each. All three PROVED. Tables: 5 selves one 0 at each even row; 9 selves three; 4 selves -,-,+,+ and
-,+,+,+ two; 4 alternating none.

---

## 6. Citations, Adding lines, words

| Step | Cites | Right? | Greater number cited? | Adding says what the step says? |
|---|---|---|---|---|
| 646 | 233 | Yes: 233 says the pattern inverted at each odd momentary and carried one self on at each even | No | Yes |
| 647 | 646 | Yes: k moves of 646, 2k momentaries | No | Yes, of the second sentence (the odd law); the first, general sentence is not in it |
| 648 | 647, 230 | Yes both (230: nine selves at 4, 12 or 36) | No | Says the step's first sentence, and is false with it at the prime 2 |
| 649 | 630 | Right for the second sentence (630: the like pair, the 0 at each even momentary). The first sentence, odd or even in number, is step 232's ("its like pairs odd or even in number with it"); 630 says only "one pair or more". Better: "steps 232 and 630" | No | Yes |

Words: none of there, count, hold, running, runs, left, begun, where, what, how, turn, return, half,
near, face, connector, join, change, changes, changed is in steps 646 to 649, their Adding lines, the
section head or the Entering line (searched as whole words; "changing" is not on the list).

---

## 7. Plainly

- **646: PROVED** for every number of selves and every pattern. Induction (O)/(E) of section 1 gives
  c_(i+1)(t+2) = -c_i(t); the loop count is exact arithmetic on 2n places. A proof, not an estimate.
- **647: PROVED** for every case: first sentence at every n (from c(2j+1) = (-1)^j S^j c(1), plus the
  line that no coming again is at an odd number of momentaries, which the step leaves out); second
  sentence at every odd n. Needs "at itself again" fixed to the sharings (or the parities carried at
  an odd momentary), since the bare carried parities equal the opening earlier, at momentary 2d+2.
- **648: FALSE** at the prime 2, two selves opposite: again at 2, not at 4 or 8. PROVED at each odd
  prime. Second sentence true.
- **649: PROVED** for every case, n = 1 and n = 2 among them.
