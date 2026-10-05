# Kit · Ramsey Societies · v365

**Complete binary societies, the fixed blocks the whole forces, and R(5, 5) as the method claim's test**

---

**Standing.** Opened at v365, ready to end at any pass. No living file is edited here. The kit carries the project the third pass opened: Ramsey numbers read as what relating every pair at once forces, the constructions the method's own step gives, what a script returned, and the passes toward the prediction that R(5, 5), the hardest of these, will be the easiest to resolve. It stands apart from the Living Improving Value and Method Improving Value baskets, and each points here.

**The aim.** R(5, 5) resolved at all five of what the claim names, with the concerns kept visible: what counts as resolving it, which counts are so far and which structural, and where the method's symmetric construction stops.

&nbsp;

**PART ONE · WHAT THE KIT HOLDS**

**PART TWO · WHAT THE SCRIPT RETURNED**

**PART THREE · THE CLAIM AT R(5, 5)**

**PART FOUR · PASSES TO RUN**

**PART FIVE · THE NOTES**

&nbsp;

---

# PART ONE · WHAT THE KIT HOLDS

| File | What it is |
|---|---|
| `ramsey_societies_v365.py` | Standard library only. Parts 1 to 3 run in seconds; `--search` adds part 4, every circulant society on 40, 41 and 42 members tested for a fixed five, in about three minutes. |
| `data/ramsey_societies_returned.txt` | What the script returned on the twenty-first of September. |

**The words the kit uses, each a counted thing.** A **society** of `n` is `n` members with every pair related at once, each relation one of two signs: a two-colouring of the complete graph on `n`. A **fixed block** of `k` is `k` members whose `k(k − 1)/2` relations all carry one sign. **R(k, k)** is the least `n` at which every such society holds a fixed block of `k`. A **circulant** society is one in which the sign of a relation depends only on the distance round a ring, so every member stands as every other, with no hub.

&nbsp;

---

# PART TWO · WHAT THE SCRIPT RETURNED

| Fives, fours, threes | What was run | Returned | The field's standing |
|---|---|---|---|
| R(3, 3) = 6 | five members, neighbours one sign, the rest the other | no fixed three in either sign | the pentagon and pentagram, the unique largest such society |
| R(4, 4) = 18 | seventeen members, the doubling distances `1, 2, 4, 8, 16, 15, 13, 9` one sign, three times them the other | no fixed four in either sign | the Paley graph of order 17, *the unique largest graph G such that neither G nor its complement contains a complete 4-vertex subgraph* |
| R(5, 5), the doubling | forty-one members, the doubling distances (the Paley graph of order 41) | a fixed five in both signs | the doubling construction does not carry to fives |
| R(5, 5), every circulant | every circulant society on 40, 41, 42 | 12 at 40; 10 at 41, one society up to multiplying the distances; none at 42 | R(5, 5) is between 43 and 46 (Exoo 1989; Angeltveit and McKay 2024), conjectured 43 (McKay and Radziszowski 1997), with 656 non-circulant societies of 42 known |

&nbsp;

---

# PART THREE · THE CLAIM AT R(5, 5)

**The whole enters R(5, 5) as every pair related at once.** A society in this sense is complete and simultaneous: every one of its relations is fixed together, as one thing. Ramsey's theorem says that once such a whole is large enough, a fixed block must stand in it. So a Ramsey number measures exactly what *considered as a whole* forces: the size at which relating every pair at once makes an equilibrium of `k` unavoidable. Without completeness and simultaneity, members relating one pair at a time and alternating, no theorem forces a block, and the question is not posed (Living Improving Value, GGG03).

**A fixed block of five is ten relations held at one sign.** Five members carry `C(5, 2) = 10` relations (Natural Numbers 5.13, *the couplings among five*). A fixed five is those ten held still at one sign together, which is the conserving Numbers 9.10 describes: *a conserving takes both at once … anything conserved across an alternating pair has taken the turning out*.

**What resolving R(5, 5) would be, both faces kept visible.**

| Face | What it asks | Standing so far |
|---|---|---|
| Why the number exists | where the whole enters | resolved: completeness and simultaneity, the whole, force the block |
| What the number is | 43, 44, 45 or 46 | open; the claim's prediction is that it will be the easiest of the hard problems to resolve (Method Improving Value, FFF03) |
| Which societies reach it | the largest society with no fixed five | the method's symmetric construction, every member standing as every other, reaches 41 and stops; the 42-member societies known are not symmetric |
| *All five dimensions* | where the five enters | as the five members of a block and its ten relations; not as `2⁵ = 32` binary states, which hold fewer members than the 42 reached (HHH03) |

**Two facts beside it, exact.** Seventeen's unique four-free society is the doubling ring, and the doubling from one round seventeen reaches nine last before it closes to one again, since `2 × 9 = 18 ≡ 1` (Living Improving Value, GGG02). And the doubling that builds it at seventeen builds a society holding fixed fives at forty-one (HHH02).

&nbsp;

---

# PART FOUR · PASSES TO RUN

1. Run `ramsey_societies_v365.py --search` at any change, and carry its returns here.
2. Name what the method would produce for R(5, 5): a society of 43 with no fixed five (which would move the lower bound), or an argument that every society of 43 holds one (which would close it at 43), and which step of the method yields either (FFF03).
3. Test societies built from the method's own steps beyond the circulant: the journey's two hands, the reflected Gray code at five signs, and the parity-alternating relatings, each on 42 and 43 members, for fixed fives.
4. Read the 656 known societies of 42 (McKay and Radziszowski's collection) for the pattern the method predicts in them, parity changing, a mirror, a fixed centre, before any number is coupled to a count in the living files (FFF04).
5. Keep every count marked so far or structural: the bounds 43 and 46 are so far, the circulant threshold 41 is structural, and no living-file count is coupled to R(5, 5) until its value is structural.

&nbsp;

---

# PART FIVE · THE NOTES

### HHH01 · The largest society with no fixed five in which every member stands as every other has forty-one members, one up to symmetry; at forty-two there is none · along

**The file's standing.** This kit, Part Two. The Hard Problem Registry v342, no Ramsey entry. Method Improving Value, CCC03: R(5, 5) as the claim's control.

**The session's standing.** *Ramsey number is going to be all five dimensions of resolving stable forming.*

**The coupling.** Every circulant society on 42 members holds a fixed five in one sign or the other: all `2²⁰` distance choices were run. On 41 there are ten with distance one at the first sign, twenty with both sign choices, and all twenty are one society up to multiplying the distances. On 40 there are twelve. So the symmetric construction, no member a hub and every member relating as every other, stops at 41, and the field's societies of 42 break that symmetry.

**The surplus.** **So the method's own symmetry meets the Ramsey threshold at forty-one**: one symmetric society, unique, and beyond it only societies with members standing differently. Whatever R(5, 5) is, its last good societies are not rotation-symmetric.

**The next opening.** The 41-member society carried as the kit's symmetric edge, and the 42-member societies read for the asymmetry they carry (Part Four, pass 4).

### HHH02 · Doubling builds the unique largest society with no fixed four on seventeen, and not one with no fixed five on forty-one · along

**The file's standing.** This kit, Part Two. Kit · The Concentric Rings in Motion, EEE01 to EEE04, the double angle.

**The session's standing.** *tan(2x) = 2*tan(x) / 1-tan^2(x).*

**The coupling.** On seventeen, the distances reached by doubling, `1, 2, 4, 8, 16, 15, 13, 9`, carry one sign and three times them carry the other, and no fixed four stands: the Paley graph of order 17, the unique largest society for fours. On forty-one the same construction, the distances doubling reaches, holds a fixed five in both signs, so the unique symmetric society of 41 (HHH01) is not the doubling one.

**The surplus.** **So doubling carries the fours whole and does not carry the fives**: the pattern at seventeen is exact and the step to forty-one is not the same step. A method claiming the fives must name the step that builds 41 and beyond, which doubling is not.

**The next opening.** The 41-member society's distances read for the step that builds them (Part Four, pass 3).

### HHH03 · The five-dimensional binary space holds thirty-two states, fewer than the forty-two members a society without a fixed five reaches · across

**The files' standing.** Natural Numbers v346c 9.10: *State-flow fives-run is the five-dimensional binary changing … Five the dimensions the co-changing turns in … binary the changing, the is-or-is-not at each position.* This kit, Part Three.

**The session's standing.** *Ramsey number is going to be all five dimensions of resolving stable forming.*

**The coupling.** Five binary positions make `2⁵ = 32` states. Societies with no fixed five are known on 42 members, and the circulant ones reach 41. A society built on the five-dimensional binary states alone, one member at each state, has at most 32 members.

**The surplus.** **So *all five dimensions* reaches R(5, 5) through the five members and ten relations of a block, and not through thirty-two states**: counted as states, the five dimensions hold ten members fewer than the societies already known. The claim's five enters Ramsey as the block's five.

**The next opening.** *All five dimensions* named at the block's five and ten at this kit and at Numbers 9.10, before any state-count is coupled to R(5, 5).
