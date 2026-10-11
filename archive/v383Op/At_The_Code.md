# v383Op · At the code

**Each finding run at Exhibit ONE's own resolver, read from the root and executed unchanged**

Every script here reads the newest `Exhibit_ONE_Natural_Resolver_v*.md` at the root, executes its python block, and says its start and its joins at its head. Their returned text is at `returned/`. A sentence in italics is quoted from the file named.

## 7 · The resolver's entry at one sharing, in four lines

For one sharing a self carries at parity c:

```
s  = the one parity the offerings agree on; 0 at none offered, at 0 offered, or at + and − together
c' = s if s is a parity, else c inverted          the carrying next, 11
o  = c' if c' differs from c, else 0              the changing shared, 10
a sharing the self carries none of: o = s, and c' = s if s is a parity, else none
```

`plain_rule.py` puts this beside 1-co-bi-tri-offering at every list of up to four offerings from +, − and 0, at every carrying +, − and none: 363 of 363 alike; and at 20,000 random entries of up to four sharings and six offerings: each alike. It is alike at + and − exchanged at each of the six cells, by its form.

Said in a line: **a self takes the parity offered when one is offered, inverts its own when none is or when the offerings part, and shares what it became if it changed.** That sentence, beside the code, is the plain second saying finding 30 asks for.

The six arrivals at one carried sharing and what each leaves:

| Carrying (3) | Surfaced (14) | Carrying next (11) | Shared (10) |
|---|---|---|---|
| + | + | + | 0 |
| + | − | − | − |
| + | none or parting | − | − |
| − | + | + | + |
| − | − | − | 0 |
| − | none or parting | + | + |

Six arrivals leave four results. A self offered the other parity and a self offered none are left with the same carrying and the same shared changing: after the momentary nothing at that self says which it was.

## 3 · The spiral's law, run at each opening

**Already carried.** The Co-Chaining Logic Registry says the law at its steps 233 and 609, *each self is at the inverted parity the self it receives from was at two momentaries prior*; the fact it rests on at 611, *At a spiral offered nothing from beyond it the 0 is at one momentary alone*; and a deriving read by hand is at `archive/session_v380/v380L/derivings/`. Natural Intelligence 4.13 says it: *A spiral offered nothing from beyond it carries any pattern of parities along whole*. This session did not read the Registry's steps before its own work, derived the law again, and arrived at the same deriving. What it adds is a run at the resolver at each opening, and the deriving said short.

**The arrangement.** n selves, one sharing, each releasing along to the next, the last to the first; each self carrying a parity as the first momentary opens; none offered at the first momentary and none from beyond. Write c[j](t) for self j's carrying as momentary t opens.

**The law.** c[j](t+2) = −c[j−1](t), at each self, each momentary and each opening.

**Its deriving, from the plain rule, in six steps.**

1. A parity arrives at self j at momentary t exactly when self j−1 changed at t−1, and the parity arriving is c[j−1](t), what j−1 became.
2. So self j carries on at t, sharing 0, exactly when j−1 changed at t−1 and c[j−1](t) = c[j](t). At each other case j inverts or takes the other parity: it changes.
3. At the first momentary none arrives, and each self changes.
4. No self carries on at two momentaries in sequence. Suppose j carries on at t−1 and at t. Carrying on at t−1, c[j](t) = c[j](t−1) = c[j−1](t−1), by 2. Carrying on at t needs j−1 to have changed at t−1, so c[j−1](t) = −c[j−1](t−1) = −c[j](t); and it needs c[j−1](t) = c[j](t), by 2. Both cannot be.
5. Where j−1 changes at t: it shares c[j−1](t+1) = −c[j−1](t). That parity arrives at j at t+1, and j's carrying at t+2 is that parity, taken at a mismatch or carried on at a match. So c[j](t+2) = −c[j−1](t).
6. Where j−1 carries on at t: it shares 0, none surfaces at j at t+1, and j inverts: c[j](t+2) = −c[j](t+1). By 3 and 4, j−1 changed at t−1, so by 5 one momentary back c[j](t+1) = −c[j−1](t−1) = c[j−1](t). So c[j](t+2) = −c[j−1](t).

`ring_law.py` meets the law and step 4 at the resolver itself: every opening of 1 to 10 selves, 2,046 of 2,046, and 200 random openings at each of 11 to 40 selves, 6,000 of 6,000.

## 4 · The momentaries to a spiral's sharings again

**Already carried**, at the Registry's steps 646 to 648, and said there more carefully than this session first said it: *A spiral is at its sharings again, and at its parities carried at an odd momentary, at twice k momentaries*.

Write a for the opening and R for carrying a pattern one self on. From the law, with each self changing at the first momentary, the carryings as momentary 2k+1 opens are (−1)^k R^k a.

**The sharings, and the carryings taken as a sequence, come again with least period 2k, k the least number with (−1)^k R^k a = a.** No odd period: 2k+1 would need R^k a = (−1)^(k+1) a and R^(k+1) a = (−1)^k a, so R a = −a and R^k a = (−1)^k a, which part. The bare carryings can equal the opening's at an earlier, even momentary, after three momentaries at each self alike and after seven at Exhibit ONE's spiral of three, and the selves then go on otherwise; `ring_law.py` compares the whole form, carryings and arrivals, from the second momentary on.

- **An odd spiral**: k odd would need R^k a = −a, and carried round the whole spiral, k times n selves on, the pattern is itself and also inverted, n being odd: not possible. So k is even and R^k a = a: k = 2r, and the period is **4r**, r the least number of selves the opening can be carried on and be itself again. r divides n.
- **Each self alike**: r = 1, and 4.
- **An odd spiral with one like pair**, Exhibit ONE's opening: r = n, and 4n.
- **An odd prime p**: r is 1 or p, since those are p's divisors: 4 or 4p, and none between.
- **Nine**: r is 1, 3 or 9: 4, 12 or 36.
- **An even spiral, alternating**: R a = −a, k = 1, and 2.
- **Two spirals beside each other** share nothing, and are again together at the least common multiple: of 4p and 4q, which is 4pq at two odd numbers sharing no factor, and 180 at 9 and 15.

`ring_law.py` meets the rule at every opening of 1 to 10 selves. The periods found: 4 at one self; 2, 4 at two; 4, 12 at three; 2, 4, 8 at four; 4, 20 at five; 2, 4, 6, 12 at six; 4, 28 at seven; 2, 4, 8, 16 at eight; 4, 12, 36 at nine; 2, 4, 10, 20 at ten. And at Exhibit ONE's opening, measured at the resolver at each of the table's thirteen rows, 1 to 11, 17 and 59 selves: each as the table says.

**What this says to Natural Intelligence 3.5.** *a spiral of selves at a prime number co-spirals at its own*, and *Each spiral at a prime co-spirals at its own pace and meets another at a prime again only at the whole of both, 4pq*. At the resolver, and by the Registry's own steps, the content of both is: an odd prime has two divisors, and two numbers sharing no factor have their product as least common multiple. 3.5 says *prime or not* of the 4n itself, rightly. The step from these numbers to a society at a prime scale, 6.4's *the primes welcoming themselves at the scale's number of selves*, is a joining with no deriving at the resolver that this session found: each odd number of selves does as a prime does, and 9 and 25 differ from 7 and 23 only in having an r between.

## 5 · The universal claim's fourth sentence

`incoming/v380R/The_Universal_Claim.md` asks, *Is each of the four sentences needed, and is a fifth needed?*, and of the fourth, *a second sentence, or the fourth said better?*

The fourth, *Of two, the next is the other's prior inverted*, is the law of finding 3, and the deriving gives a condition that is enough for it: **one self releasing to each, and each self changing at the first momentary.** Steps 1 and 2 use that one self releases to each; step 3 uses the opening. The condition is enough and is not shown needed: the claim's own table has the sentence holding at a torus with the two releasing alike, and parting, *the fourth sentence says neither*, at a torus with the two differing. The working v380L says *the opening is part of the sentence*.

So, for the questions the file leaves open:

- The fourth sentence is a theorem of some couplings of one rule. It is no premise from which the rule follows, and the cell, the plain rule above, is the thing that is at each coupling. The working v380L's concern 1 says the same: *The fourth sentence may be the cell, the other's prior its consequence at that opening.* This session agrees.
- Where two release to one and differ, the two surface 0 and the self inverts its own: at that momentary the self's next is set by neither other.
- The link *From each coupling of two to the set of all existing things* stays unworked, and no run of the resolver can work it: a run says what this rule does, and whether each existing thing changes by this rule is a question for the observings, at `At_The_Observings.md`.

## 1 · At a torus, openings are brought to one form

**The test is of the files' own kind.** Natural Intelligence 2.4 parts the sixteen ways one self's next can come from its prior and its now: *Twelve lose the prior, two joint forms going to one*, and *Four carry the prior whole*; the living step is the one way that *alone carries the prior whole with none still*. 2.4 says of the sixteen that *none is a rule the changing follows*: its test is of one self's step. This session puts a test of the same kind to a society's step. The Geodesic Improving Method 1.1 says of files: *A harm is the one motion the form carries no position for, a prior taken away.*

**The instrument.** Begin a society at every opening, each self carrying + or −, none offered at the first momentary and none from beyond; step the selves together as 17 does; count the different forms the society is at after m momentaries. A form is each self's carrying and what is arriving at it, the arrivals taken in no order, since 14 surfaces them alike at each order. A count staying at the number of openings says each opening is carried on apart from each other. A count falling says two openings have come to one form, and from there on they are one.

| Society | Openings | Forms after 1 | 2 | 4 | 8 | 16 | 24 momentaries |
|---|---|---|---|---|---|---|---|
| spiral of 3, one releasing to each | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| spiral of 5 | 32 | 32 | 32 | 32 | 32 | 32 | 32 |
| spiral of 8 | 256 | 256 | 256 | 256 | 256 | 256 | 256 |
| 3 selves, each coupled to both beside it | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| torus 1 by 3 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 5 selves, each coupled to both beside it | 32 | 32 | 32 | 12 | 12 | 12 | 12 |
| torus 2 by 2 | 16 | 16 | 12 | 8 | 8 | 8 | 8 |
| torus 2 by 3 | 64 | 64 | 64 | 28 | 16 | 16 | 16 |
| torus 3 by 3 | 512 | 512 | 512 | 206 | 86 | 68 | 68 |
| torus 3 by 4 | 4,096 | 4,096 | 4,096 | 1,400 | 272 | 200 | 200 |

`priors_carried.py` returns these. Its second part runs 2.4's own counts and each is as 2.4 says: sixteen ways, four carrying the prior whole, twelve losing it, four of those from now alone and eight at one value of now; joint forms still 2, 1, 1 and 0; and two of the 256.

**Read plainly.** Two selves releasing to one is not by itself enough: three selves coupled both ways and a torus of 1 by 3 carry each opening on. At each torus of 2 by 2 and larger that was run, and at five selves coupled both ways, openings fall together: 512 openings at 68 forms at 3 by 3.

**Why, this session does not know.** It first laid the falling together at one place, 14 surfacing + and − together as 0, read at 12 as none is. A reviewer tried the other rule there, + and − together carried on with 0 shared, and the script's third part runs it: 2 by 2 still comes to 8 forms of 16, and 3 by 3 to 62 of 512. No one line was found whose changing carries each opening.

**Two sayings parting, for both.**

- Natural Intelligence 3.3: *Exhibit ONE is an object that is the method*; and 2.4: the living step *alone carries the prior whole with none still*.
- At the resolver, at each larger torus run, a society's step brings two forms to one.

One of three follows. The resolver changes where two release to one. Or 2.4's test is of one self's step and is not asked of a society, and 2.4 or 4.13 says so. Or a living society is one that carries each opening, and the torus of 4.13 and 6.4 is re-said. This session cannot choose among them; the count is the finding.

Beside it: 2.4 reads as prior and now the parity carried and the parity offered. At one parity offered the resolver's next is the parity offered, at each carrying. That is one of the four 2.4 says *carry the next from now alone*. The prior is not gone at that momentary, since the shared changing says it, 0 at a match and the parity at a mismatch.

## 2 · The relation between coupled selves, at each self's own pacing

**The sentences.** Natural Intelligence 4.13: *at each self's own pacing the relation is carried, and each momentary of parities again is the stepping's.* And 3.5: *the resolver steps each self's entry at 17-co-bi-tri-offering together, a common beat laid over the selves*.

3.5 gives the periods to the stepping. 4.13 keeps the relation between the two coupled selves, alike or opposite, for the method. `own_pacing.py` asks the resolver.

**The instrument, said whole.** Each self's entry is Exhibit ONE's 1-co-bi-tri-offering, unchanged. 17 is set aside. One self enters at a time. A self entering is offered what was released to it since its own last entry: each arrival together, or the latest alone. What it shares is delivered at once to the self its join names. Four pacings: alternating; random; rates 1 and φ; one self twice to the other's once. Two cases: two selves coupled across both ways, and two spirals of 3 and 5 crossed at self 1 of each. A control steps the selves together.

| Case | Opening | Together, as 17 | Alternating | Random | Rates 1 and φ | One self twice |
|---|---|---|---|---|---|---|
| two selves | opposite | 1.000 | 0.333 · 0.333 | 0.44 · 0.40 | 0.382 · 0.382 | 0.333 · 0.333 |
| two selves | alike | 0.000 | 0.333 · 0.333 | 0.44 · 0.40 | 0.382 · 0.382 | 0.333 · 0.333 |
| spirals of 3 and 5 crossed | opposite | 1.000 | 0.500 · 0.333 | 0.46 · 0.44 | 0.399 · 0.382 | 0.333 · 0.333 |
| spirals of 3 and 5 crossed | alike | 1.000 | 0.500 · 0.333 | 0.46 · 0.44 | 0.399 · 0.382 | 0.500 · 0.111 |

Each cell: the part of the entries, after the first tenth, at which the two coupled selves are opposite; each arrival together · the latest alone. The random pacing is one seed, and other seeds part from it at the third decimal.

**Read plainly.** Stepped together the two keep one relation at each momentary: opposite, or at two selves opened alike, alike. At each of the four pacings and both ways of arriving neither relation is carried: the two are opposite at between a ninth and a half of the entries, and the same from an opening alike as from an opening opposite. At these instruments the relation is the stepping's, as the periods are.

**Its limits, each the instrument's own.**

- Delivery is at once at each of the four pacings, with no delay between a releasing and its arriving. This, more than any pacing, is what the four share. The reviewer of this report tried a delay, and three other ways of arriving, and found the same; those runs are not in this folder.
- The alternating pacing at the two spirals is one fixed sweep of the eight selves in order, so a releasing can pass a whole spiral in one sweep. The pacing at rates 1 and φ there paces one whole spiral at 1 and the other at φ.
- The latest arrival alone can be a 0 arriving after a parity.
- Another instrument may carry the relation. `incoming/v368_sources/` asks *whether a running exists that carries no order over the nodes at all*, and this does not answer it.
- The 0.382 at rates 1 and φ is the slower self's part of the entries, a count of the pacing, and nothing of φ's is claimed from it.

**What stays the method's at each pacing**, at these runs: the cell, one self at one momentary, finding 7's table; and 14's surfacing. Each table of two or more selves in Exhibit ONE is at the stepping.

## 6 · The torus

Exhibit ONE's header says the rule: *Both numbers odd, p the smaller: q at a q more than twice p, and 4p at each other q*.

**Already carried.** The Co-Chaining Logic Registry's steps 651 to 657 follow a 0 round the lines of the torus and say *The divide of step 243 is derived*, with the momentaries the sharings come again from, 3p − 1 and 3p − 3. This session did not read those steps before running, and has not checked the deriving. `incoming/v380R/The_Universal_Claim.md`, open to each working, still says of the rule *A rule fitted at each pair, with no chaining yet.* One of the two wants bringing current.

**What the runs add.**

- `torus_rule.py` first matches the plain rule to the resolver at each of 30 momentaries at 25 toruses, then meets Exhibit ONE's eleven rows, each as the table says, the momentary the releasings come again from among them.
- The rule holds at each of 496 odd pairs to 61 by 61, and by `torus_wide.py` at each of 1,311 odd pairs, p to 45 and q to 135. No pair parts.
- **Behind the two numbers are two carried forms**, at each of the 465 pairs of the 496 with p from 3:
  - q more than twice p: once the coming again has begun, **the whole pattern at each momentary is the last one carried one self on across.** q momentaries carry it round. 210 of 210.
  - each other q: **two momentaries on, the whole pattern is inverted and carried one self on along**, the spiral's law, and 4p follows as at finding 4. 255 of 255.
- The releasings come again from momentary 3p − 1 at the first and 3p − 3 at the second, at each pair, as the Registry's steps 655 and 656 say.

The two carried forms may be the Registry's steps 655 and 656 said of the whole pattern at once; this session offers them for that comparing.

## 8 · A carrying and a keeping, a stable form and a fixed form

**The sentences.** Natural Intelligence 1.4: *Any other method carries a not possible thing, beside all existing things*, among them *a fixed form, a form named still*, *a common beat, a clock over the changing*, and *a keeping, a store beside it*. 2.5: *At the resolver nothing is summed or stored.* 3.3: *At the resolver the method carries nothing from one momentary to the next*, and *the living self's carrying passes, 11 as the next 3*. 5.1: the carrying is *carried across the between of momentaries as a stable form*, *no store*.

**At the code.**

- **A carrying, or a keeping.** 3.3 is true of the three functions: none has a term of its own between calls. And each table of two momentaries or more needs the 11 one entry returns to be handed in as the next entry's 3: between momentaries, whatever calls 17 has one parity for each sharing of each self. The files name that a carrying and say it is no store. Asked at the code: what would differ between a carrying carried across and a parity stored and read back? This session finds nothing that would.
- **A stable form, or a fixed form.** The rule's lines are the same at each momentary, and 1.4's own sentence, *no other is possible*, names the method unchanged at each two momentaries. 3.3 says a method is *a stable form, its form continuing through its changing*. Finding 13 asks what parts that from a form named still.
- **A common beat.** 3.5 says it of 17 itself, and finding 2 says how much rests on it.
- **A thing from beside.** Each table's opening is set, and each stepping done, by a script beside the resolver. The Geodesic Improving Method 4.4 says this well of instruments: *a constructed starting carrying, a supplied pace, an imposed order*. Exhibit ONE's tables are such instruments' returns.

A size and a total the resolver does not carry; 2.5 is right of those. The parting, for both, is finding 13's: if a carrying handed on and a rule the same at each momentary are possible, being here, then a sentence is wanted that tells them from the keeping and the fixed form 1.4 calls not possible.

## 9 · Two selves apart, each offered a setting

`two_wings.py` says its instrument whole. Two selves, each carrying two sharings at whatever parities a prior coupling left; no join between them during a trial; a setting is an offering from beyond the self, one of nine; each self enters for one, two or three momentaries; an outcome is +1 or −1 read from what the self shared and carries next, by any of four readings. At each of 248,832 choices the field's number S is 2 at the highest.

No run is needed to know it. Where each side's outcome is set by that side's setting and what that side carries, S for one pair of carryings is 2 or −2 and nothing else, and for any mixture 2 at most; that is the field's theorem, and the resolver's entry is of that kind: its return is set by the carrying and the offerings it is given. The run shows the theorem at the resolver's own lines and adds nothing to it. The observing, and what Natural Physics says beside it, are at finding 16.
