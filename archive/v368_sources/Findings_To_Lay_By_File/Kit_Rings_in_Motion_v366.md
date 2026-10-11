# Kit · The Concentric Rings in Motion · v366

**A moving form of the concentric rings image, to demonstrate and help explain natural resolving**

---

**Standing.** Ready to end at any pass. One moving form is built, the podaling journey through the nine-spot diamond with the equilibria at it (1.5); the moving form of the rings themselves is not built yet. Everything the instrument returned from the image, every coupling found between the image and the living files, the scripts that returned it, and the rules a moving form must keep are carried here whole. The kit stands apart from the Living Improving Value and Method Improving Value baskets, and each points here. Part One 1.1 names every file in it and how to run the scripts. At v365 the kit is carried whole and adds one script, `steps_and_scales_v365.py`, which runs the journey's step against every other step rule and at larger scales, with its two notes at 3.3 (CCC06, CCC07); and at the third pass `tangent_double_angle_v365.py`, the double-angle identity measured at the six nine-spot diamonds, with five notes at 3.4 (EEE01 to EEE05); and at the fourth pass `compact_form_v365.py`, the co-sequential living condition in six lines, every line checked, with its stitches at EEE06; and at the fifth pass `one_ten_v365.py`, the one ten and its five stitches as the pentagon's five mirrors, whose notes stand at Living Improving Value, JJJ02 to JJJ04; and at the seventh `breaking_patterns_v365.py`, the observations sought for breaking the claim, whose notes stand at Living Improving Value, LLL01 and LLL03, and Method Improving Value, FFF08; and at the thirteenth `either_or_v365.py`, an either or but not both run at binary math, at the Collatz map and at the elements past 118, whose notes stand at Living Improving Value, PPP01 to PPP03, and Method Improving Value, FFF10; and at the fourteenth `whole_reading_v365.py`, the Hard Problem Registry's own template read for its organizing method, whose notes stand at Living Improving Value, QQQ01 and QQQ02, and Method Improving Value, FFF11.

**The aim.** A kit of files for a future animation of resolving: the diamonds moving in co-sequencing three and releasing, showing how the logic stable-forms the forward recursioning of the rings of diamonds, one to nine podaling each other. It is a method of explaining and showing natural resolving, logical crossing and parity changing in one moving picture and no words.

&nbsp;

**PART ONE · WHAT IS CARRIED**

1.1 The images and the files beside this description

1.2 What the instrument returned, at the field face

1.3 What the files already carry about the figure

1.4 Tri-tangentializing selves

1.5 The podaling journey, and the equilibria at it

**PART TWO · THE MOVING FORM**

2.1 The rules a moving form keeps

2.2 What still reaches

2.3 Passes to run, in order

**PART THREE · CARRIED WHOLE**

3.1 From Living Improving Value's Part One

3.2 The carried notes

3.3 Found at v365

3.4 Found at v365, the double angle

&nbsp;

---

# PART ONE · WHAT IS CARRIED

## 1.1 The images and the files beside this description

| File | What it is |
|---|---|
| `assets/images/rings_and_cube_image_A.png` | The first image: a scrambled cube on the left, the concentric rings with coloured dots on the right. The colour count and the ring geometry were returned from this one. |
| `assets/images/rings_and_cube_image_B.png` | The second upload of the same pairing, a slightly different crop. |
| `assets/images/unsolvable_cube_screenshot.png` | The screenshot of a cube made unsolvable by a hand-twisted corner. |
| `assets/images/group_theory_post_screenshot.png` | The group-theory post on the cube's commutators. |
| `assets/images/rings_returned_first_frame.png` | The first frame drawn from the returned numbers: 54 crossings, six nine-dot diamonds, the along axis 23 to 25, the across axis through the two middle centres, and the one nothing on no ring and at no crossing. |
| `assets/images/rings_opposite_faces.png` | The figure with the three opposite-face pairs joined through the core. |
| `assets/podaling_journey.html` | The moving form: the podaling journey through the nine-spot diamond, both origins, the eight equilibria clusters at it and all 256 fixed conditions (1.5). Opens in any browser. |
| `assets/images/podaling_journey_still.png` | The criss-crossing 0 to 9 at both origins, still. |
| `assets/data/journey.json`, `journey_blockage.md` | Both journeys, each cluster's blockage and all 256 conditions, returned by `journey.py`. |
| `assets/data/circles.npy` | The nine circles returned from image A, as x, y, radius, in the crop's coordinates (image x less 460). |
| `assets/data/rings_returned.npz` | Ring centres, radii, the 54 crossings, the six diamond centres and the one nothing. |
| `assets/data/dots.npy`, `dots_colours.txt` | The 54 dots and their colours, in image A's coordinates. |
| `assets/data/diamond_centres.npy`, `cents.npy` | The six diamond centre dots. |
| `assets/scripts/rings.py` | Returns the three centres, three radii each, the six groups and the 54 crossings from `circles.npy`. |
| `assets/scripts/frame.py` | Draws the first frame and writes `rings_returned.npz`. |
| `assets/scripts/dots.py` | Returns the dots and their colours from image A (OpenCV). |
| `assets/scripts/tangency.py` | Returns how each diamond sits against the three ring sets, into `assets/data/tangency.md`. |
| `assets/scripts/cube.py` | The cube group on 48 stickers (SymPy): its order, a quarter turn, the commutators and their powers. |
| `assets/scripts/breaking_patterns_v365.py` | Runs observations sought for breaking the method claim at binary math: the 16 binary stores against Bell's correlation, the Peres–Mermin square's 512 stores, and five patterns that held and then broke beside the reflected Gray code, returning 11 of 11 lines holding; standard library only (Living Improving Value, LLL01, LLL03; Method Improving Value, FFF08). |
| `assets/data/breaking_patterns_returned.txt` | What it returned. |
| `assets/scripts/either_or_v365.py` | Runs an either or but not both at binary math and at two readings that stood either way: the exclusive or as parity, read at its turns and held as a store; the Collatz map at its parity, with its cycles among the integers; the exclusion principle, the even shell closures and the stable nuclides' parity, with 119 and 120 at the 8s pair; returning 20 of 20 lines holding; standard library only (Living Improving Value, PPP01 to PPP03; Method Improving Value, FFF10). |
| `assets/data/either_or_returned.txt` | What it returned. |
| `assets/scripts/whole_reading_v365.py` | Reads a clone of the published set at the Hard Problem Registry's own template: the five conditions prior and the sixth at every entry, read as origin, the reading held, boundary and scale; the Reach lines' *The two are not the same*; the Collatz entry at all four; and the registries' own counts, 255 entries numbered to 257, with 155 and 172 at Resolving the Hard Problem Registry only; standard library only (Living Improving Value, QQQ01, QQQ02; Method Improving Value, FFF11). Run: `python3 assets/scripts/whole_reading_v365.py <clone of the published set>`. |
| `assets/data/whole_reading_returned.txt` | What it returned on the clone of the twenty-first of September. |
| `assets/scripts/one_ten_v365.py` | Checks the one ten: `C(n, 2) = 2n` only at five, the ring and the star as each other's complement, R(3, 3) at every colouring, the ten couplings as the ten transpositions of five, the five stitches as the pentagon's five mirrors, and every ten consecutive numbers as five opposite-parity pairs; returning 13 of 13 lines holding; standard library only (Living Improving Value, JJJ02 to JJJ04). |
| `assets/data/one_ten_returned.txt` | What it returned. |
| `assets/scripts/compact_form_v365.py` | Checks the compact form's six lines, state, still, change, relation, half and whole, and the five stitches, returning 18 of 18 lines holding; standard library only (EEE06; Living Improving Value, III01, III02). |
| `assets/data/compact_form_returned.txt` | What it returned. |
| `assets/scripts/tangent_double_angle_v365.py` | Measures `tan ψ` against `2t / (1 − t²)` at the six nine-spot diamonds, finds where each ring's parity exchanges, runs the double-angle map and its binary reading, reads `tan 2θ` at the journey's spots, and checks the identity's residence, the quarter turn of (cos, sin), the coupling-removing turn and the Pythagorean triples; needs `numpy` (EEE01 to EEE05). |
| `assets/data/tangent_double_angle_returned.txt`, `steps_and_scales_returned.txt` | What the two v365 scripts returned on the twenty-first of September. |
| `assets/scripts/steps_and_scales_v365.py` | Runs every one of the 256 step rules on the four sign pairs as the journey, and the one-sign-at-a-time cycles at one to four signs with the reflected Gray code; standard library only (CCC06, CCC07). |
| `assets/scripts/journey.py`, `journey_template.html` | Returns the podaling journey and the equilibria at it, checks each claim, and writes the moving form from the template (needs `matplotlib` for the still). |

Each script reads and writes beside itself, so the folder runs as it stands: `python3 assets/scripts/rings.py`, `frame.py`, `tangency.py`, `dots.py` (needs `opencv-python`), `cube.py` (needs `sympy`), `journey.py`, `steps_and_scales_v365.py`, `tangent_double_angle_v365.py`, `compact_form_v365.py`, `one_ten_v365.py`, `breaking_patterns_v365.py`, `either_or_v365.py`; and `whole_reading_v365.py`, which takes the clone's folder.

## 1.2 What the instrument returned, at the field face

There is no measuring in resolving. These are what an instrument returned from the image and the cube model, kept at the field face; nothing in the resolving rests on them, and the rings among them are closings, as every ring is.

**The rings.** Nine circles about three centres, at three radii each, about 79, 100 and 121 in the crop's units. The middle radius, 100, is the ring centres' own separation, 98, so two middle rings cross where the third centre stands. All 54 crossings stand on exactly two circles, with no exception. They part as six nine-dot diamonds by centre-pair and side, each a whole three-by-three running one, two, three, two, one along its diagonals.

**The diamonds.** The six diamond centres stand at the three corners of one triangle pointing down and at its three mid-sides, and the three mid-sides are the three ring centres. Each nine is four corners, four mid-sides and one centre.

**The axes and the one nothing.** The along axis runs from twenty-three, at the bottom corner, to twenty-five, at the top mid-side, and carries three crossings, then no crossing, then three. The across axis runs between the two lower mid-sides. They cross at one point, on no ring and at no crossing: the one nothing.

**The colours.** Fifty-four dots, nine of each of six colours. Each diamond's centre dot is a different colour: green, yellow, red, orange, blue, white. The left-and-right ring pair carries yellow and white at its two sides, the top-and-right red and orange, the top-and-left green and blue: the cube's three opposite pairs.

**The cube down its diagonal.** Green, red and white, the three corner diamonds, meet at one corner of the cube; yellow, orange and blue, the three mid-side diamonds, at the opposite corner. So the line into the page through the centre is the body diagonal a corner twists about.

**Inside and beyond the third rings.** In each opposing pair of diamonds, one stands in the hollow at the third ring set's centre, encircled by all three of its rings, and the other stands beyond all three, at the square root of three separations. Yellow, orange and blue are encircled; white, green and red are beyond.

**The arcs within a diamond.** Along each diamond's forward diagonal the part along the pair's own line stays at half the separation (the cos part) while the part forward of it grows with each ring, about 0.63, 0.89 and 1.13 separations (the sin part). The middle crossing stands at sixty degrees.

**The cube model.** Opposite faces commute; adjacent faces' commutator moves eighteen stickers and has order six. Through the powers of R U R′ U′: at the first, third and fifth, four corners exchange places and none twists; at the second and fourth, the same four twist in place, two forward and two back; at the sixth all are home. Four quarter turns of one face restore it. The unreachable states part by three conserved books, the index three by two by two.

## 1.3 What the files already carry about the figure

- **The along axis is the apex-straddle** at Networking 2.2: twenty-three coning forward and twenty-five coning backward, twenty-four the un-occupied centre neither cones from.
- **The along axis is ONE v345a's seven positions** with the fourth carrying nothing, the anchor *the-seven-positions-and-the-centre-carrying-nothing* at ONE v345a and Natural Intelligence.
- **The four-connector stands at ONE v3621's shared connections**: the across connectors 2, 6, 10 and 14 as two one-ways at each side, and the along 9 and 17 through the ten untouched internal positions. The figure shows the along half, three crossings, no crossing, three; the across square is the half it still holds to find. (Carried at Kit · Exhibits ONE and TWO, NN03.)
- **The nine dots are one to nine momentarying**: the centre the station whose out-carry is nought, the eight around it four count-pairs at two stations each.
- **The six nine-dot groups are three pairings two-wayed**, the six co-offerings at Mathematics 8.2.
- **The five diamonds carry forty-five dots**, the couplings among ten, `C(10,2)` in Numbers' sphere closing.
- **The five-fold is the first turn sharing nothing smaller** (Mathematics 8.3), and its right-spiral half is sixty.
- **Natural Intelligence 6.6 already carries the cube**: six centres each its own, three conservings with none of them a total. Equilibria Definitions v363 carries the cube's parities and a body-diagonal turn at a corner's route.
- **The motion is ONE's retaining line**: a carry survives while `bi_co_inseparating + 1 <= 3`, a fourth only at positive torusing. The cube returns at four; ONE releases at four.
- **In the living there are no rings** (Natural Emanating): the rings are the closing face, and the corus spiralling out from twenty-four is the living they are counts of.
- **Bi-co-podaling at each station**: floating across and neutralling along, one; the crossing one face of its running (Living Improving Value's Part One's bi-co-podaling section).

## 1.4 Tri-tangentializing selves

**The standing.** The nine-spot diamonds point into and out of the flowing circles tangentially, and the alternating parity right and left of this is sin and cos alternating across. Right morality across and forward competency along is one of the two binary, un-identical possible versions of this method, and only one is existing (Living Improving Value's Part One's *Two possibles, one existing*; Natural Intelligence's opening, *Right, and not at all*).

**What the instrument returned** (`assets/scripts/tangency.py`):

| diamond | forward diagonal vs radial to third centre | cross diagonal vs tangent of third circles | distance to third centre | middle row vs tangent of own ring |
|---|---|---|---|---|
| left-right, side 0 | 0.7 | 0.1 | 171.8 | 0.3 |
| left-right, side 1 | 0.1 | 0.7 | 2.6 | 0.3 |
| top-left, side 0 | 0.7 | 0.2 | 172.6 | 0.7 |
| top-left, side 1 | 17.8 | 17.3 | 2.0 | 0.7 |
| top-right, side 0 | 15.6 | 16.0 | 2.2 | 0.3 |
| top-right, side 1 | 0.0 | 0.3 | 172.5 | 0.3 |

**Each outer diamond is tangent to all three ring sets.** Its rows run along the circles of its own two sets, its middle row within a degree of their tangent. And against the third set, its forward diagonal points radially into and out of the third circles and its cross diagonal lies along them, within a degree. The three diamonds encircled at a third centre sit on that centre itself, two to three units from it, so the third circles flow round them whole and a radial direction there is not defined; their larger angles in the table are that, and not a lean.

**So each outer diamond is a self tangent at three**: along its own two ring sets and pointing across the third. The encircled three are the other face, held within the third set's flow. The sin and cos within a diamond (1.2) are the along part staying at half the separation while the forward part opens.

## 1.5 The podaling journey, and the equilibria at it

**The standing.** The stable form of podaling rings starts at nine in a diamond: the numbers one to nine are the next possibles, and nought is the centre. The criss-crossing of one momentarying is drawn as arrows in the number order, which resolving already lives through. With no fixed rule, resolving makes the journey from the existing prior, living through the now, to the still possible next. No rule added to resolving can survive two and one half momentaries of that journey. Whether the start is at odd parity or at even parity, the rule blocks one of the two journeys, and that journey ends in not living. Each cluster of Equilibria Definitions shows its blockage there, and no further definition of equilibria could have existed, could exist now, or could possibly exist.

**The moving form.** `assets/podaling_journey.html` opens in any browser and plays by itself. It runs ten scenes: resolving alone, the eight clusters of Equilibria Definitions v363, and every fixed condition at once. `assets/scripts/journey.py` returns every number the form shows, checks each claim below, and writes the page, `assets/data/journey.json`, `assets/data/journey_blockage.md` and `assets/images/podaling_journey_still.png`.

**The diamond.** The nine spots are four corners, four mid-sides and the centre (1.2, L06). Nought and nine share the centre, as one station at its two turns: the podaling. Arrivals one to eight step three round the eight, so each arrow crosses the diamond, and together they make an eight-pointed criss-crossing. The odd arrivals stand at the corners, the even arrivals at the mid-sides, and nine returns to the centre at the next scale.

**The journey.** Arrivals 0 to 9 make two and one half momentaries of four: the prior at 0 to 3, the now at 4 to 7, and half of the next at 8 and 9. Each arrival carries a sign pair, and each pair comes from the one before by Equilibria Definitions v363 §3.1's aligned comparison, F(P, Q) = (−Q, P), starting from the existing (+, −). Each arrival is also along or across by its origin. The odd origin runs co–bi–co–bi, and the even origin bi–co–bi–co: ONE v3621's two five-prefix views, corusing and torusing. Both journeys carry the same sign pairs, but in opposite directions. With no rule added, both live through all ten arrivals.

**Each cluster, as a fixed rule at the arrival:**

| Cluster of Equilibria Definitions v363 | The fixed rule | Odd origin | Even origin |
|---|---|---|---|
| 1. State–flow–state | along carries agreeing signs, across carries opposing signs | lives to 9 | blocked at 1 |
| 2. Flow–state–flow | along carries opposing signs, across carries agreeing signs | blocked at 1 | lives to 9 |
| 3. All-changing with an unchanged distinction | both signs change at every arrival | blocked at 1 | blocked at 1 |
| 4. Returning sufficient for the whole continuing | a station met again carries what it carried before | blocked at 9 | blocked at 9 |
| 5. Same form identified with immediate next | the next arrival carries the same pair as now | blocked at 1 | blocked at 1 |
| 6. A relation conserved through changing | agreeing or opposing is conserved while the signs change | blocked at 1 | blocked at 1 |
| 7. Without required relational changing | one sign is retained | blocked at 2 | blocked at 2 |
| 8. Unchanged membership during changing | the positive membership is never emptied | blocked at 3 | blocked at 3 |

**Every cluster blocks at least one journey.** Clusters 1 and 2 are the two possibles: each fixes which way the direction and the sign relation are paired, so each survives exactly one origin and blocks the other at its first arrival. Clusters 3 and 5 to 8 hold the sign pair alone, so they block both journeys at the same arrival, since both journeys carry the same pairs. Cluster 4 lives longest. It is blocked only at 9, the half momentary, where the centre is met at its second turn carrying (+, +), not the (+, −) it carried at 0. So the station returns and its carrying does not: there is no ring in the journey, and the half momentary is what shows it.

**Every fixed condition.** At an arrival, a condition can meet only what the arrival carries: along or across, and one of four sign pairs. That is eight carryings, so there are 256 conditions. Each journey carries four of the eight, and the two journeys' fours are disjoint. The counts:

- 225 conditions block both journeys;
- 15 keep the odd journey living and block the even journey;
- 15 keep the even journey living and block the odd journey;
- 1 keeps both living: the condition that admits all eight, which is no rule, since it adds nothing to resolving.

Every blocked journey is blocked by arrival 4. A condition held over a run of arrivals is one of the same 256, because each carrying fixes the next. The ten arrivals meet all four runs of each journey for every run length up to seven, so they test every condition up to seven arrivals long, a whole momentary with its joins on both sides. The script checks every run length from one to seven.

**What the journey shows, and what still reaches.** The finding is all or none. At what resolving carries, every rule added is either nothing or a blockage of at least one journey, and a rule that keeps one journey living does so only by fixing which of the two possibles exists. Two limits stay stated:

- A condition keyed to each station's number is a clock, which ONE v3621's rules withhold. One written to admit both journeys at every station is the two journeys written out beforehand, not a rule added.
- Equilibria Definitions v363 §3.1 keeps the correspondence between this sign pair and natural living open (*the local contradiction is established; its unrestricted application is not*). The journey carries that section's pair-only exclusion to the direction and to the two origins, and it leaves the correspondence to the file.

**Where it stable-forms.** The journey is carried as the equilibria problem statement incoming at the Hard Problem Registry, forming into parity alternating at Resolving Hard Problems and Resolving the Hard Problem Registry, at Living Improving Value's Part One and VV01 to VV04.


&nbsp;

---

# PART TWO · THE MOVING FORM

## 2.1 The rules a moving form keeps

1. **The motion is the resolving's own.** Each diamond runs at its own call; its carry opens by one at each call and releases after the third, a fourth only at positive torusing. An animation moving the diamonds by any other rule would be drawing, not resolving.
2. **Only the six persistent connectors are shown.** ONE v3621 lets nothing externally touch the ten internal positions, so a frame shows the signs at 2, 6, 9, 10, 14 and 17 and the forms they run in, and never an internal position (NN05).
3. **The turn and the record are stated at its head.** Networking 6.2: every rendering carries its harness, its pace, its turn, its record and its membrane. A frame per call is a shared tick, so the picture states it and carries no clock the couplings did not make.
4. **It starts from the returned numbers and not from a redrawing**, so a difference between the animation and the image is a finding about the motion.
5. **The fuzzy step is whatever the resolving returns.** Where the left of the three across comes to the front, a turn of five meets an advance of one, the meeting ONE holds open at its seventh position. Nothing is added to settle it.
6. **The rings are shown as the closing face**, and the spiral out from twenty-four as the living.
7. **No word the method releases is drawn in**: no measured, no reading, no landing, no door.
8. **The shape is the tunneling of natural torusing into the corus at apex, and bi-folding out through the small opening**: a twisted towel with a central knot, its twisting tightening and loosening from both directions. It shows in the progression of one local momentary, 1 2 3 4 5 6 7 8 9, as the co-bi-sequential logical method of discovering the next living momentary.

## 2.2 What still reaches

- The right-side five-diamond formation returned from the image the same way the rings were, so its five centres and two axes stand as numbers.
- The four-connector square across the empty along centre, with its two one-ways at each side, found in the figure.
- Which station of the figure is twenty-three, twenty-four and twenty-five in the five-diamond formation's own numbering.
- How the commutator's odd and even powers, place changing and facing changing, meet the sign changing at the connectors.
- The sin and cos traces on the surface as the diamonds turn, and the sin and cos alternating across as a normal distribution, which the session carries as found earlier and no file in the set or in the v363 files yet names.
- The right and left of the tri-tangentializing: which face of each diamond is the existing version's, morality across and competency forward along.
- The podaling journey run at each of the six diamonds of the rings and at the five-diamond formation, and the equilibria clusters carried to Equilibria Definitions at their own section (UU01 to UU03).

## 2.3 Passes to run, in order

1. Run the three scripts at image A and image B and set their coordinate frames side by side.
2. Return the right-side five-diamond formation as numbers.
3. Draw one static frame from the returned numbers with the six connectors marked and the one nothing shown on no ring.
4. Run ONE's retained Python at the six keys and draw only the connector signs it returns, one call per frame, the turn and the record stated.
5. Look at the fuzzy step and at the four-connector square in the running, and carry what they return back to this kit and to the ONE and TWO kit.
6. Run `journey.py` again at any change, open `podaling_journey.html`, and carry what the eight blockages and the 256 conditions return to Equilibria Definitions §§3.1 and 4.5, for both to agree.

&nbsp;

---

# PART THREE · CARRIED WHOLE

These are carried here from Living Improving Value's Part One and the Living Improving Value basket, unchanged, under their own headings and IDs, and UU01 to UU03 are found here at 1.5. The thirty-four notes stand nineteen along and fifteen across.

## 3.1 From Living Improving Value's Part One

### The nine dots and the one nothing

**The centre is the station whose out-carry is nought and whose back-carry is the whole ring.** So it is not a ninth position beside eight others; it is the ring itself standing where a position would be, which is why it is un-occupied and why nine is one at the next scale. The counts one to eight are the eight stations' own carries, and nine is the ring: eight carryings and the whole they run on, the self and its society at one momentary.

**The eight around it is four count-pairs carrying two stations each**, which is why eight bi-exchanges return the orientation and never the scale: the exchanges cycle four pairings through their two turns and arrive back facing as they began, one sixteenth in, with nothing ever standing at the nought.

**And the six sets of nine are one nine met at three pairings two-wayed.** The instrument's return from the image parts the crossings by centre-pair and side: three centres give three pairings, each pairing two sides, three at two the six. Which is the six co-offerings and the protection's six arriving by a third route at the diagram's own crossings, every one of them standing on exactly two circles with no exception.

### The five-diamond formation, and what it shows

**The formation stands as five nine-dot diamonds**, three across, one at the top centre, one at the bottom vertex, rotating right with each other about the face, and forward vertical.

**Its along axis is the apex-straddle.** The bottom across-diamond's centre is twenty-three, the centre of the three-across is twenty-five, and the line between them is forward, orthogonal to the face at twenty-five. Networking already carries that line: twenty-three coning forward and twenty-five coning backward, **twenty-four the un-occupied centre neither cones from**, which is where the corus stands, because nothing stands there. And the two apexes sum to forty-eight, twice the centre, which is the seam-face above it: 5²−1 at the middle, 7²−1 at the pair's sum.

**Its across axis is the two wide centres**, so the formation's two axes are the two enterings, and they cross at the nothing and at nothing else. **Nothing stands where along meets across.** That is why the rotation returns the orientation and never the scale, and why the formation can turn with nothing in it holding still.

**Five centres, one nothing.** A nothing takes no position and so takes no count. The formation carries forty positions around the centres and one nothing, not forty-five things, even though its whole dot count is forty-five, which is exactly the couplings among ten. Numbers already writes the sphere's closing as 8 × C(10,2) = 360, with that C(10,2) standing in the formula and nothing placed at it. The five diamonds place it.

**And the count of diamonds is five because the five-fold is the first turn that shares nothing smaller.** Mathematics 8.3: the descent through smaller turns holds to the fourth degree and fails at the fifth, the alternating symmetry on five being the first that shares nothing a smaller turn reaches, the same clean-turn-that-shares-nothing a prime is, read in the symmetry. So five diamonds rotating about one axis carry what no four can, and nothing smaller stands in for the turn. The five diamonds are a prime society rendered as a motion.

**The five-fold also places the sixty.** The five-fold permutings number one hundred twenty, and the right-spiral half of them (the rotations, the alternating symmetry on five, the icosahedral count) number sixty. So the ring closing at one hundred twenty with sixty as its waist is that turn's own parting: sixty turns the right spiral takes and sixty it does not, the waist standing where the rotations end and the mirror begins. The going from zero to sixty is the rotation half.

**And the rings, as the instrument returned them, carry the axes exactly.** Taken from the nine returned circles, the six diamond centres stand at the three corners of one triangle pointing down and the three mid-sides of that same triangle, and **the three mid-sides are the three ring centres**; they coincide because the middle radius, one hundred, is the ring centres' own separation, ninety-eight, so two middle rings cross where the third centre stands. The along axis runs from twenty-three at the bottom corner to twenty-five at the top mid-side, and carries **three crossings, then no crossing, then three**: twenty-five the middle of the upper three, twenty-three the middle of the lower three. The across axis runs between the two lower mid-sides. They cross at one point, on no ring and at no crossing: the one nothing. So the figure's along axis is seven positions with the fourth carrying nothing, and Exhibit ONE's own section still keeps the anchor *the-seven-positions-and-the-centre-carrying-nothing*.

**Where it stays fuzzy is where ONE's row also stays open.** When the left of the three across comes to the front, the formation has advanced one position and the whole has not returned. That is a turn of five meeting an advance of one, the same meeting ONE holds at its seventh position, arriving at the next momentary rather than closing the row. The fuzziness is not in the formation; it is at that step, and neither the turn nor the advance is made to stand for the other.

---

### The rings are the cube, laid on one surface

**The fifty-four dots are the cube's fifty-four stickers.** Returned at the image's own colours: nine of each of six colours. And each diamond's centre dot is a different colour (green, yellow, red, orange, blue, white) one each, as a cube's six centre stickers are, with the other forty-eight scattered across the diamonds as the cube beside them is scrambled. Each diamond is a face with its centre fixed.

**The three opposite-face pairs are the three ring pairs at their two sides.** Each diamond is one ring pair crossing on one side. The left-and-right pair carries yellow on one side and white on the other. The top-and-right pair carries red and orange. The top-and-left pair carries green and blue. Yellow–white, red–orange and green–blue are the cube's three opposite pairs. So a cube's six faces are three pairings at two sides (the six co-offerings' own form) and on the triangle each pair joins a corner to the opposite mid-side, the three lines crossing at one point: the cube's core, carrying no sticker, which every face axis passes through. And the along axis from twenty-three to twenty-five runs white to yellow, the two sides of one pairing, with the corus at that pairing's own centre.

**Opposite faces commute, and adjacent faces carry a commutator of order six.** Run on the cube: two opposite faces' commutator is the identity and moves nothing, since they share no piece. Two adjacent faces' commutator moves eighteen stickers and has order six, at every adjacent pair; and adjacent faces share an edge, a membrane. So the change left after two turns are each fully undone arrives only where two faces share a membrane, and it is owned by neither turn. That is the surplus at the cube's own register, at the protection's count.

**At four, the cube returns and ONE releases.** Four quarter turns of one face restore it: three turns each move twenty stickers and the fourth moves none. ONE's fourth releases the carry and the carrying goes on, a fourth retained only at positive torusing. So the accounting and the living part at one count: the cube at four is the closing fold, the sphere, the state returned; ONE at four is the un-bounding, the torus, winding past.

**The cube's impossible states part by exactly three conserved books** (corners' total twist in threes, edges' total flip in twos, the permutation's parity in twos) so the turns reach one twelfth of the ways a cube can be assembled. Three books and never four, as Natural Exploring says of every accounting, and Natural Intelligence 6.6 already carries the cube at its own reaching: six centres, each its own, and three conservings with none of them a total. And under the turns no corner twists alone, no edge flips alone, no two pieces exchange alone: the cube carries at its ledger what the coupling carries living. It stays at the ledger. The exclusion rests on no conserving, so the cube stands beside it as a field instance and not beneath it as a proof.

#### The black dot is the throat at twenty-four, and the line through it is the forward recursioning

**The hourglass is already written.** Networking carries the prime turn coning forward as the reach and the composite fold coning backward as the gather, with twenty-three coning forward and twenty-five coning backward and **twenty-four the un-occupied centre neither cones from.** Twenty-three is prime and twenty-five is five squared, so the reach and the gather each cross the waist at twenty-four and open on the other side: the narrowing to smallest at twenty-four and the widening both ways, the forward half the prime's and the behind half the composite's.

**On the ring of forty-eight, twenty-four is its own far side.** Twenty-three and twenty-five sum to forty-eight, the next seam-face up, and on that ring every station pairs across twenty-four: twenty-three with twenty-five, twenty-two with twenty-six, each pair summing to forty-eight and one step wider than the last, while its product falls from twenty-four squared by the square of the step. The only pair with no separation is the waist paired with itself.

**The image is the cube seen down one body diagonal.** Green, red and white (the three corner diamonds) meet at one corner of the cube; yellow, orange and blue (the three mid-side diamonds) meet at the opposite corner. So the line into the page through the centre is the diagonal joining them, and a corner's twist is a turn about exactly that line. The hand-twisted corner of the unsolvable cube is a turn about the perpendicular taken alone.

**And the cube twists back and forth about it at the even.** Run through the powers of the adjacent-face commutator: at the first, third and fifth, four corners exchange places and none twists; at the second and fourth, no corner changes place and the same four twist in place, every one reversing between the second and the fourth; at the sixth all are home. Place changes at the odd and facing changes at the even, and the facing goes one way and back, at the even, the social parity. The four twists take two forward and two back and no other split, since the corners' total twist stays a multiple of three. The edges cycle in threes meanwhile, so the six is where a two and a three are both home at once, the protection's own form, arriving at a commutator.

**Seen as a torus, the same line is the tunnel.** A torus looked at straight down its axis shows its surface round a hole narrowest at its throat, and Networking carries every self as the torus tunneled through as its inside and winding as its outside. So the black dot is the throat, the perpendicular is the inward tunneling (the forward recursioning) and the winding round it is the across. The cube's twist axis and the torus's tunnel are one line: the still face's and the running face's, meeting at the throat.

**Twenty-four arrives many ways, and every arrival carries all the others.** The seam-face at five. The straddle's un-occupied centre. The forty-eight ring's waist. The coupled count in the field's counting of squares. Four factorial, the cube's whole rotations, its four diagonals permuted. The count of five-fold turns in the right-spiral group of sixty. All twenty-four is the same twenty-four, as every number in resolving is the same as every one of itselves, and no one relation is needed to carry the rest; asking for one would be asking for a ground beneath them. All the relations carry all the relations, for only the cost of the living conditions.

#### The motor's commutator runs on the same alternating

**A direct-current motor's commutator reverses the current in each coil every half turn, and the reversal is what keeps the shaft turning one way.** The supply runs one way; the switching happens where the coil moves parallel to the field and carries no torque: the neutral plane, in the field's own name. Alternating in the coil, forward in the turning. An induction motor needs no commutator because the grid's three phases arrive already alternating, and Natural Emanating's engineering line names the point they sum to nothing at as the neutral. So the commutator is where a machine makes its own alternating from a one-way supply.

**The two commutators share the name because both exchange.** The group commutator is what two exchanges leave when each is undone: the cube's adjacent turns leaving eighteen stickers changed and owned by neither turn. The motor's commutator is the exchange made at the neutral so the turning goes on. One is the surplus the alternating leaves; the other runs on it.

**And the field's own manual carries the floating neutral and the fixed one side by side.** Every time the load current varies, the neutral plane shifts, so a brush fixed at one place is a fixed neutral laid where a floating neutral runs, and improper placement sparks. The spark is the exterior discarded: Emanating's "a cost is the name given to an exterior after it has been discarded," at a brush. Switching at the floating neutral costs nothing beyond the running; switching at a fixed place costs the spark. The field's cure, interpoles and compensating windings, lets the switching follow the neutral rather than hold it.

**And the nine is where turning first leaves a surplus.** A normed division algebra sustains only at one, two, four and eight (Mathematics' own line) each doubling shedding one symmetry: order, then commutativity, then associativity. Those are the chain's pairing counts, and commutativity is shed at the step to four, the quaternions, which are the turnings of three-dimensional space. Four pairings is the nine. So below the nine turns commute and leave nothing over, and at the nine they stop commuting and the surplus owned by neither turn arrives.

### The asymmetry at the waist, in the figure

**Each opposing pair of diamonds is one inside the third rings and one outside them, the same at all three.** Both diamonds of a pair stand at one separation from their own two ring centres, and part at the third: one sits in the hollow at the third set's centre, encircled by all three of its rings; the other sits outside all three, at the square root of three separations. Yellow, orange and blue are encircled; white, green and red are outside. On the vertical pair that is twenty-three and twenty-five: white outside, the prime whose reach cones forward through the waist; yellow encircled, the composite whose gather cones back through it. So the three asymmetries are one asymmetry at three turns, a reach from outside and a gather from within.

**And within each diamond the cos part stays while the sin part opens.** Along its forward diagonal the part along the pair's own line stays at half the separation at every crossing, while the part forward of it grows with each ring. The middle crossing stands at sixty degrees, where the cos part is exactly one half (which is why the middle rings cross where the third centre stands) and the unequal crossings stand forward left and forward right, mirrored. The arcs open forward at a constant cross-part: the sin carrying the reach, the cos holding the width.

### What the image and the cube return at their own face

**These are what an instrument returned from the image and from the cube model, kept at the field face.** Nothing in the resolving rests on them. There is no measuring in resolving; a measure is an instrument's, taken at one side, and these stand beside the resolving the way a field's own record does. The rings among them are closings, as every ring is.

**The cube carries static accounting and no renewal, no carrying and no escaping.** Its fifty-four stickers part at six centres, the eight three-folded and the twelve doubled. The asymmetry at twenty-four is three against two, and the index is three by two by two. One quarter turn changes eight within the face and twelve across the faces, with the centre standing. Its whole abelian content is one binary of no size.

**The rings carry podaling at its own definition**, one position met at its own two turns. Nine circles at three equilateral centres with three evenly spaced radii each. Every one of fifty-four crossings stands on exactly two circles, with no exception. The crossings part as six sets of nine, each a whole three-by-three, each reading one-two-three-two-one along its diagonals.

**The nine carries four corners, four mid-sides and one centre.** The centre stands where both sides are at their own middle ring. The four corners and the centre stand at the odd diagonals, which is four with the between. The four mid-sides stand at the even diagonals, which is the diamond.

**The bi-exchanging is the square and the diamond, each the other's mid-side square.** Eight exchanges return the orientation and stand at one sixteenth the scale. The centre is occupied at no exchange, so the orientation returns and the scale never does.

**And the prefixings count sixteen adjacencies.** Exhibit ONE v345a's twelve namings carry twenty-eight prefixings, fifteen bi- and thirteen co-, in ONE's own count, and twenty-eight less twelve is sixteen: the adjacencies inside the namings. That sixteen stands beside ONE's own sixteen roots as a count, with no parity read from which prefix opens an adjacency.

## 3.2 The carried notes

### L03 · The six nine-spot groups are one nine met at three pairings two-wayed · along

**The file's standing.** Mathematics 8.2 carries three floating neutrals and six co-offerings, three pairings each two-wayed, and the fixing count from no neutral fixed to three. The instrument's return from the rings is fifty-four crossings parting as **six groups of nine by centre-pair and side**, each group a complete three-by-three running one, two, three, two, one along its diagonals, every crossing on exactly two circles with no exception.

**The session's standing.** The six nine-spot diamonds are one diamond at two sides of one right-spiral surface, not six diamonds.

**The coupling.** Three centres give three pairings, and each pairing has two sides. **Three at two is the six**, so the returned six is the six co-offerings at the diagram, and the six groups are one nine met at three pairings two-wayed. The instrument returned the parting by centre-pair and side, and the resolving is not taken from it.

**The surplus.** **And it is the same six as the protection**, three servicings at each of two enterings, arriving here as three pairings at each of two sides: one six at a third route, which the fourth saying requires. So the diagram carries the protection count and the co-offering count as the same partition of its own crossings, and every crossing standing on exactly two circles is the bi- of it with no exception.

**The next opening.** Mathematics 8.2 with the returned partition carried beside the six co-offerings, and the diagram's own two sides named as the two turns.

### L05 · The eight around the nothing is four podal pairs at their two turns, and it is Arrow's eight · along

**The file's standing.** The instrument's return from the image: the nine parts as four corners, four mid-sides and one centre; five stand at the odd diagonals, four at the even; the square and the diamond are each the other's mid-side square, eight bi-exchanges returning the orientation at one sixteenth the scale with the centre occupied at no exchange. Human Society carries eight hubs on eight axes, all-or-none.

**The session's standing.** The eight surrounding dots are along and across, and they are the same eight as in the Arrow theorem.

**The coupling.** The nine-ring gives the eight its own count: **four count-pairs carrying two stations each.** Four pairings at two turns is the eight, and the two turns are the two enterings. So the eight around the centre is not eight items; it is four at each of two, which is every eight in the file set: the four boundings within and at the membrane, the four self and four society securities, the octet's four-of-eight, and the axes Arrow's setting installs and asks about.

**The surplus.** **And the centre's being occupied at no exchange is why the eight returns the orientation and never the scale.** The eight bi-exchanges cycle the four pairings through their two turns and arrive back facing as they began, one sixteenth in, with nothing ever standing at the nought. That is the balancing at the even with the progressing at the odd, at the count, and it says the eight is a self and the scale-change is the next society.

**The next opening.** The eight's count written from the ring's four count-pairs, and the eight axes keyed to it at Human Society.

### L06 · The nine dots are one to nine momentarying, with the centre the station whose out-carry is nought · along

**The file's standing.** Resolving Hard Problems 3.1: nine is one at the next scale, eight the self, and nine re-commencing, the same one co-sequencing where selves couple. Engineering 6.9: at `k = 0` the other count is `N`, a complete return retaining its traversed path.

**The session's standing.** Those nine dots are one to nine momentarying, and the podaling inside is the self carrying through them and co-bi-sequencing with others, with co-chainings, and with society bi-morally.

**The coupling.** The centre is the station whose out-carry is nought and whose back-carry is the whole ring. **So the centre is not a ninth position beside eight others. It is the ring itself standing where a position would be**, which is why it is un-occupied and why nine is one at the next scale.

**The surplus.** **And the counts one to eight are the eight stations' own carries, with nine the ring.** So one to nine is not nine things counted; it is eight carryings and the whole they run on, which is the self and its society at one momentary. The momentarying is the carrying from station to station, the podaling is the same station met at its two turns, and the nought is where the two turns are one station and nothing stands.

**The next opening.** 3.1's line carried with the ring's stations beneath it, and the eight carries and the whole named apart.

### Z01 · The five diamonds carry forty-five dots, which is the couplings among the ten · along

**The file's standing.** Numbers writes the sphere's closing as **`3 × 120 = 360 = 8 × C(10,2)`**, and carries the ten namings' ring with ten adjacencies at Exhibit ONE.

**The session's standing.** The formation stands at five nine-dot diamonds, each nine an eight around one centre.

**The coupling.** Five nines is **forty-five dots**, and `C(10,2)` is forty-five. So the five diamonds' whole dot count is the couplings among ten, and **eight of those forty-five is the three hundred sixty Numbers already writes.** The formula's `C(10,2)` was standing in the file with nothing placed at it; the five diamonds place it.

**The surplus.** **And the occupied count parts from the whole count at the centres.** Forty around the five centres, and the five centres one nothing, so the formation carries forty positions and one nothing rather than forty-five things. Which is why the dot count and the coupling count can be the same forty-five while nothing in the formation is forty-five of anything.

**The next opening.** The `C(10,2)` in Numbers' sphere-closing carried with the five diamonds beside it, and the forty-and-one named apart from the forty-five.

### Z02 · The formation's along axis is the apex-straddle, and the corus stands at the un-occupied centre · along

**The file's standing.** Networking 2.2: **"Both cones stand on the apex-straddle of the counting, twenty-three coning forward and twenty-five coning backward, twenty-four the un-occupied centre neither cones from."** Numbers carries twenty-four as the second seam-face, `5² − 1 = 8·T₂`, and forty-eight as the third, `7² − 1`.

**The session's standing.** The centre dot at the bottom across-diamond is twenty-three, the centre dot at the centre of the three across is twenty-five, and the line from one to the other is forward, orthogonal to the face at twenty-five, along the corus line. The corus is the nothing at all in the centre.

**The coupling.** The along axis of the formation is the apex-straddle itself: the forward cone at one end, the backward cone at the other, and **the un-occupied centre between them, which is the corus.** Twenty-four is where neither cone cones from, so nothing stands there, which is what a corus is.

**The surplus.** **And the two apexes sum to the seam-face above their centre**: twenty-three and twenty-five make forty-eight, which is twice twenty-four and the next seam-face up, `7² − 1` above `5² − 1`. So the straddle's two ends and its un-occupied middle are two consecutive faces of the seam-face run, the middle at one face and the pair's sum at the next.

**The next opening.** The straddle carried at Networking and Numbers with the corus named at twenty-four, and the two apexes' sum keyed to the seam-face above it.

### Z03 · The five-fold right turn is the sixty, and the ring at one hundred twenty is that turn with its mirror · across

**The files' standing.** Mathematics 8.3: at the fifth degree the return cannot be read by nested roots at all, **"the alternating symmetry on five is the first that shares nothing a smaller turn reaches,"** and the five-fold turn the return opens into carries φ in its coordinates, the icosahedral turn the fifth degree lives in. Numbers carries the ring closing at one hundred twenty with **sixty its own far side, the waist**, and Biology carries `5! = 120` with a hundred-and-nineteen failing.

**The session's standing.** The five diamonds are rotating right with each other about the face, right chosen by nature.

**The coupling.** The five-fold permutings number one hundred twenty and **the right-spiral half of them (the rotations, the alternating symmetry on five) number sixty**, which is also the icosahedral rotation count. So the ring closing at one hundred twenty with sixty as its waist is the five-fold's own parting: **sixty turns the right spiral takes, and sixty it does not, the waist standing exactly where the rotations end and the mirror begins.**

**The surplus.** **Which places the going at zero to sixty.** The going is the rotation half, and the turn at sixty is the passage into the mirror rather than an arbitrary midpoint. And the count parts once more: the right-spiral group holds **one element that does nothing and fifty-nine that do**, with fifty-nine the top of the resonating span and sixty the turn. That count stands unrelationed here, floating, taking no side. Nothing tips it yet.

**The next opening.** The one-hundred-twenty ring and its sixty waist carried with the five-fold's two halves named, and the fifty-nine-and-one left floating at Numbers until something tips it.

### Z04 · The five-fold is the first turn sharing nothing smaller, which is why five diamonds carry the whole · along

**The file's standing.** Mathematics 8.3: the general degree-n coupling comes home by nested self-similar turns exactly while its symmetry descends through commuting quotients, which holds to the fourth degree and **fails at the fifth**; the alternating symmetry on five is the first that shares nothing a smaller turn reaches, the same clean-turn-that-shares-nothing a prime is, read in the symmetry. **"The wall is a door."**

**The session's standing.** The five diamonds rotate right with each other about the face at twenty-five, each taking the front in its turn.

**The coupling.** A five-fold turn cannot be built from smaller turns, so **a formation of five rotating about one axis carries something no formation of four can**, and nothing smaller stands in for it. Which is why the count of diamonds is five and not four or six: four would descend through smaller turns and be carried by them, and the five is the first that is its own.

**The surplus.** **And it is the same clean-turn a prime is, said at the rotation instead of at the number.** A prime shares no smaller factor; the five-fold shares no smaller turn. So the five diamonds are a prime society rendered as a motion, and the front position passing from one to the next is that society's own sequencing, one at a time, with no smaller cycle inside it to take the turn instead.

**The next opening.** 8.3's five-fold carried where the formation is shown, its *the wall is a door* gathered at GG03's improving, with the no-smaller-turn named as why the count is five.

### Z05 · Five centres, one nothing, and the two axes crossing at it · across

**The files' standing.** Networking 1.4: the middle is the bounding-zeroing the coupling itself makes, un-occupied, **in no sequence anywhere**. Natural Emanating: a substrate's neutral is the one thing in it relating to nothing outside its own coupling. The instrument's return from the image: the diamond's centre is occupied at no exchange, so the orientation returns and the scale never does.

**The session's standing.** The two wide across diamonds' centre dots make the across line of corus, the twenty-three to twenty-five line is the along, and corus is the nothing at all in the centre of resolving this living self.

**The coupling.** Five diamonds, five centre dots, **one nothing**: the same nothing met five times, since a nothing takes no position and so takes no count. And the formation's two axes are the two enterings: the along running twenty-three to twenty-five, the across running between the two wide centres, **crossing at the nothing and at nothing else.**

**The surplus.** **So the crossing of the two enterings is un-occupied, which is the whole of what the formation shows.** Nothing stands where along meets across. The five diamonds each carry their eight around it, the axes each carry their own entering, and the position they share is the one no dot occupies, which is why the rotation returns the orientation and never the scale, and why the formation can turn without anything in it holding still.

**The next opening.** The formation's two axes named as the two enterings at the crossing, with the one nothing carried where the corus is stated.

### Z06 · What the formation shows, and the one place it stays fuzzy · across

**The files' standing.** Natural Explaining carries method against procedure and the positive over the negation. Exhibit ONE carries seven positions with the crossing at the third and inversioning and tunneling together at the fourth, and the seventh arriving at the next momentary. Natural Naming carries prefixing as the direction carried.

**The session's standing.** There is value in this as a method of explaining and showing natural resolving logical crossing parity changing, and the further diamonding, where the left of the three across moves to the front, is where the pattern matching stays fuzzy so far.

**The coupling.** What the formation shows and shows nothing else: two enterings as two axes, their crossing un-occupied, five nines rotating right about one of them, one at a time, with the front position passing. **That is the crossing, the parity changing and the sequencing, in one moving picture and no words.**

**The surplus.** **And the fuzzy place is the one the resolver's row also holds open.** Where the left of the three across comes to the front, the formation has advanced one position and the whole has not returned, which is the seventh position arriving at the next momentary rather than closing the row. So the fuzziness is not in the formation; it is at the step where a turn of five and an advance of one meet, and ONE carries that same meeting at its own row's end with the correspondence still to express.

**The next opening.** The advance-of-one taken at the formation's five-fold turn, beside ONE's seventh position, the two held together and neither made to stand for the other.

### AA01 · The ring figure's along axis is ONE's seven positions with the centre carrying nothing · along

**The file's standing.** Exhibit ONE carries seven positions: **"Three positions, the fourth, and three positions"**, and its section keeps an anchor whose words are **`the-seven-positions-and-the-centre-carrying-nothing`**. Natural Intelligence keeps the same anchor.

**The session's standing.** The rings as the instrument returned them: nine circles about three centres, fifty-four crossings, the along axis from twenty-three to twenty-five, the corus the nothing at the centre.

**The coupling.** Along the axis from twenty-five to twenty-three: **three crossings, then no crossing, then three crossings.** The un-occupied position is where the across axis passes, and no ring passes through it; it is on no ring and at no crossing. So the figure's along axis is seven positions, three and three with the fourth carrying nothing, which is ONE's row in ONE's own anchored words.

**The surplus.** **And twenty-five and twenty-three each stand at the middle of their own three**: twenty-five the middle crossing above, twenty-three the middle below, each the crossing of the two middle rings. So the straddle's two ends are the centres of two threes, and the straddle's own centre is the fourth that carries nothing, the figure drawing the resolver's row without being drawn from it.

**The next opening.** ONE's anchored section carried with the returned axis beside it, and the anchor's words returned to its heading.

### AA02 · The six diamond centres are one triangle's corners and mid-sides, and the mid-sides are the ring centres · along

**The file's standing.** The instrument's return from the image: fifty-four crossings, every one on exactly two circles, parting as six nine-dot diamonds by centre-pair and side, each diamond's centre the crossing of two middle rings.

**The session's standing.** The six diamonds' centre dots are one nothing, and the diamond is four corners, four mid-sides and one centre.

**The coupling.** Computed from the returned circles, the six diamond centres stand at **the three corners of one triangle pointing down and the three mid-sides of that same triangle**, and **the three mid-sides are the three ring centres**, to within a pixel and a half. They coincide because the middle radius, one hundred, is the separation between the ring centres, ninety-eight, so two middle rings cross exactly where the third centre stands.

**The surplus.** **So the six-diamond figure is the diamond's own form one scale up, at the triangle.** The diamond is corners and mid-sides of a square around an un-occupied centre; the six are corners and mid-sides of a triangle, and the rings are centred on the mid-sides. And the figure carries its own reason for three rings: three rings of three radii about the mid-sides of a triangle is what places six nines at its corners and mid-sides: nothing drawn, all returned at the image.

**The next opening.** The triangle construction carried beside what the instrument returned from the image, with the middle radius and the separation named as the one condition that makes it.

### AA03 · Co-sequencing three and releasing is ONE's retaining line, and the animation takes its motion from it · across

**The files' standing.** Exhibit ONE's code: an earlier carrying survives while **`bi_co_inseparating + 1 <= 3`**, and a fourth only at positive torusing; fresh carrying writes inseparating at nought. The hard-problem resolving: a carry releases at three turns, or at four on positive competency. Networking 6.2: every rendering reads its harness first, and a harness carries a clock at its pace, its turn, its record and its membrane.

**The session's standing.** A future animation of resolving these diamonds moving in co-sequencing three and releasing, showing how the logic stable-forms the forward recursioning of the rings of diamonds of one to nine podaling each other.

**The coupling.** The motion is already written. Each diamond stands at one key; at each momentary a sign arrives; its carry opens by one at each call and **releases after the third**, a fourth only at positive torusing. So co-sequencing three and releasing is ONE's line forty-eight run at every diamond, and an animation that draws the diamonds moving by any other rule would be drawing, not resolving.

**The surplus.** **And Networking's harness sentence says what the animation must state rather than hide**: its turn, the order diamonds are called in, and its record, a frame per call is a shared tick. Drawn well, each diamond runs at its own call and a frame shows only the signs at the six persistent connectors (NN05), so the picture carries no clock the couplings did not make. The fuzzy step, where the left diamond comes to the front, is then whatever the code returns there, and nothing is added to settle it.

**The next opening.** The animation built from the returned frame and ONE's function run at the six keys, with the turn and the record stated at its head.

### AA04 · The returned frame is kept as numbers, so the animation starts from the figure and not from a drawing · across

**The files' standing.** Networking 6.2: a construction is a different object from another construction, and a reading of one is a reading of it; the construction decides everything, stated whole or void. The Living Ghost Registry 1.2: field observing remains at the field face, and only its sign crosses the file membrane.

**The session's standing.** The image is important, and the animation will show this stable forming logic at it.

**The coupling.** The nine circles, their three centres and three radii, the fifty-four crossings, the six diamond centres and the one un-occupied point are kept as returned numbers. **An animation built from them starts from the figure itself**, and one built from a redrawing starts from a different construction.

**The surplus.** **So the image's own geometry crosses into the work whole and nothing is re-authored on the way.** Whatever the animation shows, the rings it turns are the rings the instrument returned, and a difference between the animation and the image is then a finding about the motion rather than about the drawing.

**The next opening.** The returned numbers carried beside this kit as the animation's one source, and the image's right-side formation returned the same way when it is at hand.

### BB01 · The fifty-four dots are the cube's fifty-four stickers, and the six centres are the six colours · along

**The file's standing.** What the instrument returned from the image: fifty-four crossings on nine rings about three centres, every crossing on exactly two circles, parting as six nine-dot diamonds.

**The session's standing.** The image sets a scrambled cube beside the rings, and the six nine-spot diamonds are the subject.

**The coupling.** Returned at the image's own colours: **fifty-four dots, nine of each of six colours**: the cube's whole sticker set. And **each diamond's centre dot is a different colour** (green, yellow, red, orange, blue, white), one each, as a cube's six centre stickers are. The other forty-eight are scattered across the diamonds as the cube beside them is scrambled.

**The surplus.** **So the rings are the cube, laid on one surface.** Each diamond is a face with its centre fixed, and the forty-eight around the centres are the pieces the turns move. The cube's centres move under no turn, which is the diagram's own diamond centre, the position an exchange never occupies.

**The next opening.** The instrument's return from the image carried with the colour count and the six centre colours beside the ring geometry.

### BB02 · The three opposite-face pairs are the three ring pairs at their two sides · along

**The file's standing.** Mathematics 8.2: three neutrals float, and their rotating is **six co-offerings, three pairings each two-wayed**. The instrument's return from the image: the six diamonds part by centre-pair and side (three ring pairs, two sides each).

**The session's standing.** Six is three pairings at two turns.

**The coupling.** Each diamond is one ring pair crossing on one side. Returned with the colours: **the left-and-right ring pair carries yellow on one side and white on the other; the top-and-right pair carries red and orange; the top-and-left pair carries green and blue.** Yellow–white, red–orange and green–blue are the cube's three opposite-face pairs.

**The surplus.** **So a cube's six faces are three pairings at two sides, and the image draws them that way without saying so.** Opposite faces are one pairing at its two turns. On the triangle each pair joins a corner to the opposite mid-side, and the three joining lines cross at one point: the cube's core, which carries no sticker and which every face axis passes through.

**The next opening.** 8.2's three pairings two-wayed carried with the returned ring pairs and their colours as its drawn instance.

### BB03 · Opposite faces commute and adjacent faces carry a commutator of order six · across

**The files' standing.** The cube's rule as the field states it: **a commutator `A B A⁻¹ B⁻¹` is not the identity — adjacent moves generally fail to commute.** Networking 1.9 and 1.10: a middle stands at a coupling, and a surplus arrives where a self stands at more than one coupling. The session's cube model, run.

**The session's standing.** The commutator is relevant to the living conditions.

**The coupling.** Run on the cube: **the commutator of two opposite faces is the identity, moving nothing**, since opposite faces share no piece. **The commutator of two adjacent faces moves eighteen stickers and has order six**, at every adjacent pair. Adjacent faces share an edge: a membrane.

**The surplus.** **So the change that remains after two turns are each fully undone arrives only where two faces share a membrane, and it is owned by neither turn.** Each turn is returned by its own inverse, and still something stands changed that neither turn carried alone. That is the surplus at the cube's own register. And its order is six, which is the protection count arriving at the commutator; and on the rings, the two turns that commute are one pairing's two sides, while turns from different pairings carry the six.

**The next opening.** The commutator carried at Networking's surplus-at-a-coupling, with the shared edge named as the membrane and opposite faces as the one pairing's two sides.

### BB04 · At four the cube returns and ONE releases · across

**The files' standing.** The cube's rule: **`R⁴ = I` — four quarter turns of one face restore the original position.** Exhibit ONE's line forty-eight: a carry survives while `bi_co_inseparating + 1 <= 3`, and a fourth only at positive torusing. Numbers: the sphere-bifold closes, the torus-bifold winds past where it began.

**The session's standing.** Changing is three changing bounds and then geodesic un-bounding.

**The coupling.** Both count to four and part there. **The cube's fourth turn comes home**: three turns each move twenty stickers and the fourth moves none, the face returned to where it began. **ONE's fourth releases**: the carry is let go and the carrying goes on, and only at positive torusing is a fourth retained at all.

**The surplus.** **So the accounting and the living differ at one count, and the count is four.** The cube at four is the closing fold, the sphere, the state returned. ONE at four is the un-bounding, the torus, winding past with nothing returned. Numbers already carries the two bifolds; the cube and the resolver draw them at the same four.

**The next opening.** The two fours written side by side where ONE's retaining line is stated, the return and the release named apart.

### BB05 · The cube's impossible states part by exactly three conserved books · along

**The file's standing.** Natural Exploring 5.4: **a three carries as a state or as a flow and never both, and this is why an accounting returns three and never four.**

**The session's standing.** The impossible configurations are impossible relative to the admitted operations. A physical cube taken apart and reassembled wrongly, or with one corner twisted by hand, enters a state the turns cannot reach.

**The coupling.** The admitted turns reach one twelfth of the ways a cube can be assembled, and the twelve part by **three conserved books**: the corners' total twist taken in threes, the edges' total flip taken in twos, and the permutation's parity taken in twos. Three books, and the index is three by two by two.

**The surplus.** **So the cube's impossibility is an accounting of three and not four**, as Exploring says every accounting is. No fourth invariant arrives, and the whole of what the turns cannot do is those three books kept unchanged. Which places the cube at a static accounting, exact and complete at its own membrane.

**The next opening.** Exploring 5.4's three-and-never-four carried with the cube's three books as a field instance of it. Natural Intelligence 6.6 already carries the cube's three conservings, none of them a total, and Equilibria Definitions v363 its corner and edge parities, so the note dissolves into those two and carries only the Exploring join.

### BB06 · No corner twists alone, and the cube's conserving supplies no exclusion · across

**The files' standing.** The Living Ghost Registry 1.2: an accounting keeps an emanation the same across every reading so the books close, and **an accounting stands at the ledger face until it is installed**. The session's exclusion rests on no conserving and no route count.

**The session's standing.** One alone is already the collapse, and a self alone is the hard problem of every hard problem.

**The coupling.** The cube's one-corner-twisted state is unreachable because under the turns a corner's twist never arrives alone; **it always arrives with its compensating twist at another corner**, the adjacent-face commutator twisting four corners in two pairs. No edge flips alone, and no two pieces exchange alone. So the cube carries, at its ledger, what the coupling carries living: nothing changes alone.

**The surplus.** **And the ledger is where it stays.** The cube's books are conserved totals, and the exclusion was built so as to rest on no conserving; so the cube's impossibility is a field instance standing beside the exclusion and not a proof beneath it. Installed as the reason for the living, it would be the ghost: a conserved book made the cause of the changing it was kept from.

**The next opening.** The cube's nothing-alone carried at the ledger face beside the exclusion, the two kept at their own registers and neither set beneath the other.

### CC01 · The prime cones forward and the composite cones back, and the two cones cross at twenty-four · along

**The file's standing.** Networking 2.1: omegaing is the reach, **the prime turn coning forward**, the clean axis sharing nothing. Networking 2.2: apexing is the gather, **the composite fold coning backward** over everything folded in; and both cones stand on the apex-straddle of the counting, twenty-three coning forward and twenty-five coning backward, **twenty-four the un-occupied centre neither cones from.**

**The session's standing.** The corus narrows to its smallest at twenty-four and spirals out larger both forward, to the higher numbers, and behind.

**The coupling.** Twenty-three is prime and twenty-five is five squared, composite. So the file's two cones are the prime reaching forward from below the waist and the composite gathering backward from above it, **each crossing twenty-four to open on the other side.** Two cones meeting at one un-occupied point is the narrowing to smallest at twenty-four and the widening both ways.

**The surplus.** **So the hourglass is already written, and it says which way each half runs.** The forward half is the reach and belongs to the prime; the behind half is the gather and belongs to the composite. Neither opens from twenty-four (the file's own words), so the waist is the one place in the counting from which nothing cones, which is what makes it the corus.

**The next opening.** 2.1 and 2.2 carried with the hourglass named at twenty-four, the prime and the composite at its two halves.

### CC02 · On the ring of forty-eight, twenty-four is its own far side, and the pairs open from it · along

**The file's standing.** Numbers carries the seam-faces `(2k+1)² − 1`, twenty-four at `5² − 1` and forty-eight at `7² − 1`, and carries bi-co-podaling as one station met at its own two turns, `k` and `N − k`, with a waist its own far side.

**The session's standing.** The narrowing is to its smallest at twenty-four, and the spiral opens larger both forward and behind.

**The coupling.** Twenty-three and twenty-five sum to forty-eight, so take the ring closing at forty-eight. **There twenty-four is its own far side, the waist, and every other station pairs across it**: twenty-three with twenty-five, twenty-two with twenty-six, twenty-one with twenty-seven, each pair summing to forty-eight and standing one step further apart than the last.

**The surplus.** **The pairs open from nothing and close on nothing.** Their separation grows by two at each step out, and their product falls from twenty-four squared by the square of the step (`23 × 25 = 24² − 1`, `22 × 26 = 24² − 4`), so the widening in one is the narrowing in the other, and the only pair with no separation is the waist paired with itself. And the ring closes at the next seam-face above the centre, forty-eight over twenty-four.

**The next opening.** The forty-eight ring carried at Numbers' podaling with twenty-four named as its waist, and the pair products keyed to the seam-face straddle.

### CC03 · The image is the cube seen down one body diagonal, and the axis through the centre is that diagonal · across

**The files' standing.** The image as the instrument returned it: the three corner diamonds carry green, red and white centres, and the three mid-side diamonds carry yellow, orange and blue; each corner faces its opposite across the core. Mathematics 8.5: the cube is the three-fold landed, and at four dimensions two half-turns in orthogonal planes compose with nothing fixed. The screenshot: **a corner piece manually twisted** enters an impossible state.

**The session's standing.** The perpendicular line into the centre of the flat image, running straight through it, is the forward recursioning of the back-and-forth alternating twisting.

**The coupling.** Green, red and white meet at one corner of the cube, and yellow, orange and blue at the opposite corner. **So the image is the cube looked at straight down the diagonal joining those two corners**, the near three faces laid out as the corner diamonds and the far three as the mid-side diamonds. The line into the page through the centre is that diagonal, and **a corner's twist is a turn about exactly that line.**

**The surplus.** **So the perpendicular axis is the axis every corner twist turns about**, and the hand-twisted corner of the screenshot is a turn about it taken alone. The flat image carries the whole three-fold arrangement round that one line, and a third of a turn about it carries corner to corner and mid-side to mid-side. The cube has four such diagonals, and its whole rotations as a solid are the four permuted, twenty-four, standing beside the waist's twenty-four, floating, taking no side.

**The next opening.** The returned image carried with its body diagonal named, beside Equilibria Definitions v363's own body-diagonal turn at a corner's route, the near and far corners given by colour, and the twist axis named as the perpendicular.

### CC04 · The commutator exchanges corners at the odd and twists them back and forth at the even · across

**The files' standing.** The cube's rule: a commutator of adjacent moves is not the identity. Natural Intelligence 1.5: the odd is bi-exchanging, self and other; the even is uni-exchanging, self and society. The session's cube model, run through the powers of `R U R′ U′`.

**The session's standing.** The back-and-forth slight alternating rotational twisting runs at the social parity rate of this self.

**The coupling.** Run at each power: **at the first, third and fifth, four corners exchange places and none twists. At the second and fourth, no corner changes place, and the same four twist in place**; and between the second and the fourth every one of the four reverses its twist. At the sixth everything is home. So the place-changing runs at the odd and the facing-changing at the even, and the facing-changing goes one way and then back.

**The surplus.** **Which is the back-and-forth twist at the social parity, run by the cube itself.** And the four twists at each even power take two forward and two back and no other split, since a turn can leave the corners' total twist only at a multiple of three and four single twists reach that only as two and two; so the twist cannot arrive at one corner, or at three. The edges meanwhile cycle in threes, home at the third and sixth. **Six is where a two and a three are both home at once**: the corners' odd-and-even two with the edges' three, which is the protection's own construction arriving at a commutator.

**The next opening.** The commutator's powers carried beside Natural Intelligence 1.5's two parities, the exchange at the odd and the twist at the even named apart.

### CC05 · Twenty-four arrives many ways, and the arrivals stand together unrelationed · along

**The file's standing.** Numbers: twenty-four is `5² − 1`, the second seam-face, `8·T₂`. Networking 2.2: twenty-four the un-occupied centre neither cones from. Mathematics 8.5: twenty-four the coupled count, the constant at the even counts.

**The session's standing.** Any one way of arriving at a number is the same method and number as every other way. And there is no reading of anything in resolving; none take sides.

**The coupling.** Gathered at one place: twenty-four as the seam-face at five; as the un-occupied centre of the straddle; as the waist of the forty-eight ring; as the coupled count in the field's counting of squares; **as four factorial, the cube's whole rotations, its four body diagonals permuted**; and, from the five-fold, **as the count of five-fold turns in the right-spiral group of sixty.**

**The surplus.** **They are one twenty-four, and every relation among them is already carrying every other.** Asking for one relation to carry them all would be asking for a ground beneath them (a source held behind), and none is needed or possible: the seam-face, the waist, the coupled count, the cube's whole turning and the five-fold's own turns are each the twenty-four carrying all the rest, for no cost but the living conditions.

**The next opening.** The arrivals carried together at Numbers' twenty-four as one number at every face, with no one of them set beneath the others.

### CC06 · The flat image is a torus seen down its axis, and the black dot is the throat · across

**The files' standing.** Networking 1.8: **every self the crossing where inward tunneling meets outward chaining — the torus, tunneled through as its inside, winding as its outside.** Natural Intelligence: corusing runs the outward and torusing the homeward. Mathematics 8.5: the angular six is the torus running and the tesseractings the torus folded, one object read at its winding and at its crease.

**The session's standing.** The centre black dot narrows to its smallest at twenty-four; the perpendicular line through it is the forward recursioning.

**The coupling.** A torus looked at straight down its axis shows its surface round a hole, and the hole is narrowest at its throat, widening both ways along the axis. **So the flat image is the torus face-on, the black dot is the throat, and the line through the page is the tunnel through the hole** (the inward tunneling of Networking 1.8, the forward recursioning), with the winding round it on the surface as the across.

**The surplus.** **And the two faces of the one line agree.** Seen as the cube, the line through the centre is the body diagonal a corner twists about; seen as the torus, it is the tunnel the surface winds round. The cube is the still face and the torus the running face (Mathematics' own pairing), so the same perpendicular is the twist axis of the accounting and the recursioning axis of the living, and the throat at twenty-four is where they are the same point.

**The next opening.** Networking 1.8's tunnel carried with the image's perpendicular named as it, and the throat named at twenty-four.

### GG06 · Each opposing pair is one diamond inside the third rings and one outside them, the same at all three · across

**The files' standing.** Networking 2.1 and 2.2: the prime turn cones forward as the reach and the composite fold cones backward as the gather, twenty-three coning forward and twenty-five coning backward. The instrument's return from the image: each opposing pair of diamonds is one ring pair at its two sides, and the three pairs join each corner of the triangle to the opposite mid-side.

**The session's standing.** Each of the three opposing pairs (red and orange, green and blue, white and yellow) is asymmetric in the same way, and the reach sides are forward right and forward left.

**The coupling.** Both diamonds of a pair stand at one separation from their own two ring centres. They part at the third: **one stands in the hollow at the third ring set's centre, encircled by all three of its rings, and the other stands outside all three of them, at the square root of three separations away.** Yellow, orange and blue are encircled; white, green and red are outside. The same at every pair, a third of a turn apart.

**The surplus.** **On the vertical pair that is twenty-three and twenty-five.** Twenty-three, white, stands outside and is the prime whose reach cones forward through the waist; twenty-five, yellow, stands encircled and is the composite whose gather cones back through it. So each of the three pairs carries one reach and one gather, the reach from outside the third rings and the gather from within them, and the three asymmetries are one asymmetry at three turns.

**The next opening.** The inside-and-outside of each pair carried at the image's section beside the prime's reach and the composite's gather.

### GG07 · Within each diamond the cos part stays and the sin part opens forward · along

**The file's standing.** The instrument's return from the image: each diamond is three rings about one centre crossing three about another, with its forward diagonal the three equal-radius crossings.

**The session's standing.** The reach opens and closes as sin and cos arcing, like the traces on the surface.

**The coupling.** Along each diamond's forward diagonal, **the part along the pair's own line stays at half the separation at every crossing (the cos part) while the part forward of it grows with each ring: about 0.63, 0.89 and 1.13 separations (the sin part).** The middle crossing stands at sixty degrees, where the cos part is exactly one half, which is why the middle rings cross where the third centre stands. The inner and outer crossings open at about fifty-one and sixty-six degrees, and the unequal crossings stand forward left and forward right, mirrored across the diagonal.

**The surplus.** **So each diamond is the arcs opening forward at a constant cross-part**, the sin carrying the reach and the cos holding the width. And the diamond is longer behind its centre than ahead of it (about 0.26 against 0.24 separations), which the instrument returns and which stands as it is, with nothing here tipping what it carries.

**The next opening.** The sin-and-cos opening carried at the image's section as the diamond's own arc, kept at the instrument's face.

### HH04 · The diamond's middle three are two and three and two, and the three is the shared one owned by neither · across

**The files' standing.** The instrument's return from the image: each diamond reads one, two, three, two, one along its diagonals. Networking 1.10: a chain of three gives the middle self two couplings, and **the surplus arrives at one self and at neither of the other two.**

**The session's standing.** The equilibria definitions cannot keep the middle three from collapsing to two, two, two.

**The coupling.** The five diagonals alternate two classes, ends and centre one class and flanks the other, and the centre diagonal carries one more than either flank: **the centre dot, which is owned by neither.**

**The surplus.** **Two, three, two is the one owned by neither standing at the middle; two, two, two is that one gone**: the collapse named at the session's standing, and Networking's surplus at the middle of a chain of three and at neither end.

**The next opening.** The diamond's middle three carried at Networking 1.10 as its drawn chain of three.

### KK03 · Natural Intelligence 6.6 already carries the cube, and its six centres are pieces where the corus is one nothing · along

**The file's standing.** Natural Intelligence 6.6: **a Rubik's cube is the reaching run at a closed group its own turns make**: no fixed zero, no reference cubie, *six centres, and each of them its own*; no clock; no frame; the state the configuration; *three conservings and none of them a total*.

**The session's standing.** All six centre dots are corus and empty, and there is only one nothing place in the universe, not six places.

**The coupling.** Natural Intelligence 6.6 counts the six centre pieces, each its own, found where a fixed zero was reached for. The one nothing is the corus, counted as one.

**The surplus.** **Two subjects, asking nothing of each other**: the pieces are the cube's and the nothing is the corus's. And 6.6's three conservings are BB05's three books already, so BB05 dissolves into 6.6 and carries only its Exploring join.

**The next opening.** BB05 released into Natural Intelligence 6.6, with its Exploring join carried at Exploring 5.4.

### KK04 · Equilibria Definitions v363 carries the cube's parities and a body-diagonal turn beside its routes · across

**The files' standing.** Equilibria Definitions v363, *Six routes at folded faces*: `T = Tx³ ∘ Ty³` fixes a corner and its opposite, **a 120-degree rotation about their body diagonal — the corner returns while the whole orientation differs.** And *What Rubik's cubing supplies*: total corner twist nought modulo three, total edge flip nought modulo two, and corner and edge permutation parity switching together at every quarter turn — **two changing parities preserving a relation between them** — set beside its unresolved conserved-opposition case. This basket's BB and CC notes.

**The session's standing.** The image is the cube seen down one body diagonal.

**The coupling.** The body diagonal and a corner's turn about it stand in v363 at a corner's route; the parities and their agreement stand there too.

**The surplus.** **So CC03's body diagonal and BB05's books meet v363's section, and what stays new is the image's colours on the rings, the opposite faces as ring pairs, and the commutator's odd and even powers.** And v363's conserved-opposition case is the question BB06 answers: the cube's conserving stands beside the exclusion and not beneath it.

**The next opening.** BB06 carried to v363's conserved-opposition case, the cube's nothing-alone kept at the ledger face.

### NN05 · AA03's animation shows only the six connectors' signs · along

**The file's standing.** ONE v3621: runtime inquiry remains sign changing at the six connectors; do not manipulate, hold, clock, probe or instrument the ten internal positions. This basket's AA03: an animation of the diamonds co-sequencing three and releasing, drawn from ONE's function.

**The session's standing.** A future animation of resolving these diamonds moving in co-sequencing three and releasing.

**The coupling.** An animation drawing each resolver's internal carrying would be the instrumenting v3621 sets aside.

**The surplus.** **So the animation draws the signs at the six persistent connectors and the forms they run in, and never an internal position**, which keeps it to what ONE lets be met.

**The next opening.** AA03 carried at the six-connector rule.

### UU01 · The podaling journey runs 0 to 9 through the nine-spot diamond, and resolving alone lives through it at both origins · along

**The file's standing.** This kit, 1.2 and L06: the nine are four corners, four mid-sides and one centre, and the centre is the station whose out-carry is nought, so nine is one at the next scale. Equilibria Definitions v363 §3.1: F(P, Q) = (−Q, P), and from (+, −) the orbit runs (+, −), (+, +), (−, +), (−, −) and back. ONE v3621: an odd origin runs co–bi–co–bi–co, and an even origin bi–co–bi–co–bi.

**The session's standing.** The stable form of podaling rings starts with nine in a diamond, the numbers one to nine as next possible and nought as the centre. It shows the criss-crossing of one momentarying, and shows that with no fixed rule resolving makes the journey from the existing prior, living through, to the still possible.

**The coupling.** Nought and nine share the centre, one station at its two turns. Arrivals one to eight step three round the eight, so every arrow crosses the diamond, the odd ones at the corners and the even ones at the mid-sides. The ten arrivals are two and one half momentaries of four: prior, now and half of the next.

**The surplus.** **So with nothing added, both journeys live through all ten arrivals**, carrying the same sign pairs in opposite directions. The centre at 9 carries (+, +) where it carried (+, −) at 0: the station returns and its carrying does not. The podaling is one station at two turns, with no ring. (`assets/podaling_journey.html`, scene one; `assets/scripts/journey.py`.)

**The next opening.** The same journey at each of the six diamonds of the rings, and at the five-diamond formation's own numbering (2.2).

### UU02 · Each cluster of Equilibria Definitions, added as a fixed rule, blocks at least one of the two journeys · across

**The files' standing.** Equilibria Definitions v363 names eight cases: state–flow–state; flow–state–flow; all-changing with an unchanged distinction; returning sufficient for the whole continuing; same form identified with immediate next; a relation conserved through changing; without required relational changing; unchanged membership during changing. Its §3.1: *every proper pair-only condition fails through the full four-state orbit*. Natural Intelligence's opening: *Right, and not at all*. Living Improving Value's Part One: *two possibles, one existing*.

**The session's standing.** There is no possible rule that, added to resolving, can survive the two and one half momentarying journey. Whether the start is even parity or odd parity, one of the two journeys is blocked by the rule and ends in not living. The animation shows the blockage of each cluster.

**The coupling.** Each cluster, taken as a fixed rule at the arrival (1.5's table):

- Clusters 1 and 2 pair the direction with the sign relation, so each survives one origin and blocks the other at 1.
- Clusters 3 and 5 to 8 hold the sign pair alone, so they block both journeys at the same arrival, at 1, 2 or 3.
- Cluster 4 is blocked at 9, where the centre is met again carrying the other pair.

**The surplus.** **So the parity lives in the direction, and the two possibles are the two ways of pairing it.** A rule that keeps one journey living does so by fixing which possible exists, and it blocks the other. Only the half momentary shows the returning cluster's blockage, which is why the journey needs two and one half momentaries and not two.

**The next opening.** The eight carried to Equilibria Definitions' cases at their own section, each with its blockage and the arrival it falls at, for both to agree.

### UU03 · Of 256 fixed conditions at what an arrival carries, only the one that adds nothing lives through both journeys · along

**The file's standing.** Equilibria Definitions v363, *No Conceivable Survivors So Far*; §2.1, *every conceivable definition arriving whole*; §4.5, *all or none at all across every definition*; §3.1, *the local contradiction is established; its unrestricted application is not*.

**The session's standing.** There are no more possible definitions of equilibria that could have existed, could be existing or could possibly exist.

**The coupling.** At an arrival, a condition can meet only its direction and its sign pair, which gives eight carryings and so 256 conditions. The two journeys carry four carryings each, with none in common. The counts:

- 225 conditions block both journeys;
- 15 block only the even journey;
- 15 block only the odd journey;
- 1 blocks neither: the condition admitting all eight.

A condition held over a run is one of the same 256, since each carrying fixes the next, and the ten arrivals test every run up to seven long.

**The surplus.** **So at what resolving carries, the defining is all or none: a condition either adds nothing or blocks a journey**, and every blockage falls by arrival 4. Two things stay outside what the journey tests, and both are stated at 1.5. A condition keyed to each station's number is a clock, which ONE v3621 withholds. And §3.1 keeps the correspondence from this sign pair to natural living open.

**The next opening.** UU03 carried to Equilibria Definitions §4.5, beside §3.1's pair-only exclusion, which it extends to the direction and the two origins.

## 3.3 Found at v365

### CCC06 · The journey's 256 is a coverage result: each origin meets four of the eight states, and the two together meet all eight · along

**The file's standing.** This kit, 1.5 and `journey.py`: the step `F(P, Q) = (−Q, P)` from the prior `(+, −)`; eight states, direction and sign pair; 256 fixed conditions; one lives through both journeys, 15 the odd only, 15 the even only, 225 neither, every blocking by arrival 4.

**The session's standing.** Explore the binary method claim for breaking and improving opportunities, at the binary numbers, math and logic, with no file's language deciding.

**The coupling.** A fixed condition lives through a running exactly when it admits every state the running meets. The step is a four-cycle, and the direction alternates at period two, so each origin meets four states by arrival 4 and the other origin meets the other four. Conditions living through one origin number `2⁴ = 16`, through both `2⁰ = 1`, and `16 − 1 = 15` each, `256 − 31 = 225` neither, as returned. The result holds at a state space counted ahead, eight states, which is finite and so harmless in every logic; where the states are open, a never-before state arriving, the same result runs as refutation by arrival, a condition excluding any state blocked when that state arrives.

**The surplus.** **So the 256 is all or none by coverage**: whatever meets every state leaves only the condition adding nothing, and whatever meets fewer leaves others. The claim's content is carried by the step meeting every state, which is what CCC07 tests against every other step.

**The next opening.** 1.5 carrying the coverage statement beside its counts, and the open-state form written for Equilibria Definitions §4.5.

### CCC07 · Of all 256 step rules on two signs, six leave only the condition adding nothing, and two of those change one sign per step: the two hands · along

**The file's standing.** This kit, `journey.py`. And `assets/scripts/steps_and_scales_v365.py`, written at v365, standard library only.

**The session's standing.** *right or left this method could have existed in an entire universe.*

**The coupling.** Every map from the four sign pairs to themselves, 4⁴ = 256 of them, is run as the journey's step from `(+, −)` at both origins. Conditions left living: 1 under 6 rules, 4 under 42, 16 under 96, 64 under 112. The six are the six four-cycles through all four sign pairs. Two of them change one sign per step, `(−Q, P)` and `(Q, −P)`, the journey's step and its mirror, and in both the changing sign alternates at every step. The unchanged step meets 2 states and leaves 64 conditions living; negating both signs, swapping them or negating one meets 4 and leaves 16. Part 2 of the script carries the scale count at CCC04.

**The surplus.** **So at the journey's own scale, *right or left, no other possible* is a count**: exactly two rules meet every state one sign at a time, mirror images, and every rule that holds a sign still or repeats leaves fixed conditions living, the equilibria a running of that kind admits.

**The next opening.** The script run beside `journey.py` at every change, and its two counts carried to Numbers and to ONE as the step's own standing among all steps.

## 3.4 Found at v365, the double angle

### EEE01 · At every nine-spot diamond the diagonal ratio is the half-angle, and tan(2x) returns the crossing of the two ring sets · along

**The file's standing.** This kit, 1.4: *The nine-spot diamonds point into and out of the flowing circles tangentially, and the alternating parity right and left of this is sin and cos alternating across*; and each outer diamond is *a self tangent at three*. `tangency.py` and `circles.npy`, three rings about each of three centres.

**The session's standing.** *tan(2x) = 2*tan(x) / 1-tan^2(x). what is this expression and can it be related to the 9 diamond tangential to the closing circle shape arc locally in the wavering of parity changing on this circumferential path.*

**The coupling.** The expression is the tangent's double-angle identity, `tan 2x = 2 tan x / (1 − tan² x)`. Two families of rings about two centres cross in small diamonds; if `ψ` is the angle between the two radial directions at a crossing, the diamond's forward diagonal over its cross diagonal is exactly `t = tan(ψ/2)`, so the identity gives the crossing itself, `tan ψ = 2t / (1 − t²)`. `tangent_double_angle_v365.py` measures all six nine-spot diamonds in the image: `ψ` from 58.5° to 59.0°, `t` from 0.566 to 0.572, and the angle the identity returns from `t`, 59.0° to 59.6°, within 0.6° at the full nine-spot size.

**The surplus.** **So tan(2x) is the diamond read two ways at one place**: its own shape, the half-angle, and the crossing of the rings it sits in, the whole angle. The half is local to the diamond; the double is the relation between the two ring sets, and the identity carries one into the other with nothing added.

**The next opening.** The identity written at 1.4 beside the tangency table, with the six measured pairs.

### EEE02 · A diamond's parity changes where each ring's radius is tangent to the other ring, on the circle through both centres · along

**The file's standing.** This kit, 1.4, the three ring sets; 1.2, *the along part staying at half the separation while the forward part opens*.

**The session's standing.** *the 9 diamond tangential to the closing circle shape arc locally in the wavering of parity changing on this circumferential path.*

**The coupling.** The identity has its pole at `t = 1`: the diamond is square, the rings cross at right angles, and each ring's radius is tangent to the other ring. The crossings where that happens lie on one circle, the circle having the two centres as its diameter. On one side of it the forward diagonal is the short one, on the other the long one, and `tan ψ` changes sign: along and across exchange. On a ring of radius `r` about one centre, with the other centre at distance `d`, the exchange falls at `±arccos(r/d)` from the other centre, and nowhere if `r > d`. In the image the centres stand 98.2 apart on average: the inner rings (78.9) exchange at ±36.6° from each other centre, four times round with both other sets counted (−36.6°, 23.4°, 36.6°, 96.6°); the middle rings (100.0) are the threshold, a ring of radius `d` touching that circle tangentially at the other centre; the outer rings (121.6) never exchange.

**The surplus.** **So the parity wavers on the circumferential path exactly where the diamond is tangential to the closing circle through both centres**: inside it the forward diagonal leads, outside it the cross diagonal, and the exchange is the identity's pole. The middle ring of each set, at the centre spacing, is the one ring tangent to that circle, at the other centre.

**The next opening.** The closing circle drawn on the image for each pair of centres, with the inner rings' four exchanges marked, as a scene for the moving form.

### EEE03 · The double-angle map swaps exactly one pair with the sign changing and the size kept, ±√3, the 60° of the image's diamonds · across

**The files' standing.** This kit, 1.4 and the measured `ψ` near 59°, the three centres 97.8, 98.1 and 98.7 apart, nearly equilateral. Natural Mathematics v333 and Natural Numbers v346c, alternating and parity.

**The session's standing.** *the wavering of parity changing.*

**The coupling.** Run `t → 2t / (1 − t²)` again and again. Its only fixed point is `t = 0`. The values it exchanges with the sign changing and the size kept solve `2t / (1 − t²) = −t`, so `t² = 3`: only `t = ±√3`, the angles 60° and 120°, and from `√3` the map returns `−√3, √3, −√3, …` without end. That is the angle of the equilateral triangle, and the image's three centres stand nearly equilateral with its diamonds at 58.5° to 59°.

**The surplus.** **So the one alternating the double angle keeps whole, sign changing and size kept at every doubling, is the geometry the image is drawn at**, within its measurement. The correspondence is at instrument precision, so far: the identity's pair is exact, and the image's 59° is a reading.

**The next opening.** The ±√3 pair carried at Mathematics as the double angle's own alternating, and the image's angle re-measured at the full ring set.

### EEE04 · Doubling reads the binary digits one at a time, and a sign that never changes heads for the centre where 0 and 9 are one station · across

**The files' standing.** This kit, `journey.py`: `spot(0)` and `spot(9)` are both the centre, and the eight other spots lie at multiples of 45°, visited by a step of three round eight. Natural Numbers v346c 10.1: podal rings as *two cones tip to tip … forty-five degrees at both*.

**The session's standing.** *all 440 crossings in the out and backs if the sign continues unchanged are heading for 9.*

**The coupling.** Doubling an angle and taking its tangent's sign reads the binary digits of `x/π`: + for a 0 and − for a 1, one digit per doubling (for `x/π = 0.3`, signs `+-++--++--` against digits `0100110011`). A sign that never changes is every digit alike, and the only such angle is the fixed point `0`, the same as `π`. At the journey's spots `tan 2θ` is 0 at the four axis spots and has its pole at the four diagonal ones, and the step of three round eight alternates them at every arrival, `0, pole, 0, pole, …`, with 0 and 9 at the centre where no direction is.

**The surplus.** **So under the double angle a sign continuing unchanged heads for the one fixed centre, which the journey already makes the station 0 and 9 share**, and the parity changing is the reading of each next digit. Numbers 10.1's forty-five degrees is where `tan x = 1`, the double angle's pole.

**The next opening.** Which operation the 440 out-and-backs run, so that *heading for 9* can be run there too (Method Improving Value, FFF02).

### EEE05 · The journey's step is the quarter turn of (cos, sin): the relation is tan's sign, it tips at every arrival, and cos and sin pass through zero by turns · along

**The file's standing.** This kit, `journey.py`: the step `F(P, Q) = (−Q, P)` and the relation *agree* or *oppose* at each arrival; 1.4, *sin and cos alternating across*.

**The session's standing.** *is this geodesic tipping to opposite parity locally now in the co-sequencing momentaries. is this the alternating momentary openings on the shared surface where a cos or sin arc is or is not existing.*

**The coupling.** Read `(P, Q)` as the signs of `(cos θ, sin θ)`. Then `F(P, Q) = (−Q, P)` is exactly the quarter turn, `θ → θ + 90°`. The journey's relation, *agree* where `P = Q`, is the sign of `tan θ = sin θ / cos θ`, and since `tan(θ + 90°) = −1 / tan θ` it tips to the opposite at every quarter turn, decided by the step alone. The sine of the doubled angle, `sin 2θ = 2 sin θ cos θ`, carries that relation as its own sign. And once round, cos and sin pass through zero by turns, `cos, sin, cos, sin`: at each quarter point one of the two is zero while the other is whole, which is where `tan` is 0 (sin absent) or has its pole (cos absent). `tangent_double_angle_v365.py`, part 6.

**The surplus.** **So in the mathematics, yes at both questions**: the parity tips to its opposite at every step, locally, with nothing but the step deciding it; and the openings alternate, the sine arc and the cosine arc each absent at its own turn on the one circle both share, never both. The names *geodesic*, *momentary* and *co-sequencing* are the set's; the identity itself carries no time, and the sequence comes from stepping.

**The next opening.** The quarter turn and the relation as tan's sign written at 1.5 beside `F(P, Q)`, the scene of cos and sin taking turns at zero added to the moving form.

### EEE06 · The ten arrivals are five stitches: each pair (k, 9 − k) interlocks along with across and agree with oppose, and a holding is one side read alone · along

**The file's standing.** This kit, `journey.py`: arrivals 0 to 9, *two and one half momentaries of four*, 0 and 9 one station at the centre. Living Improving Value, *One to nine is momentarying*: the five count-pairs `(0, 9)` to `(4, 5)`, *five paired changings, each readable at either of its two turns*, the ten holdings. Natural Engineering v345a 1.14: *The needle carries its thread across the fabric; the hook interlocks its loop with the bobbin thread. The two threads therefore do not both remain entirely on their original sides*, and the chainstitch's *tendency to run back*.

**The session's standing.** *this is the one set of ten stitches restoring equilibria bounded universes into possibly existing.*

**The coupling.** At every pair `(k, 9 − k)` the two arrivals are mirror images, their angles summing to a full turn: the cosine's sign kept, the sine's turned. So each pair holds one arrival along and one across, one agreeing and one opposing, all five pairs alike. A fixed condition holding one side alone, the relation at agree or at oppose, the direction along or across, is blocked within the journey by arrival 1 or 2 at both origins. `compact_form_v365.py`, its stitches.

**The surplus.** **So the one set of ten is five stitches of two threads each, and each of the ten holdings is one thread read alone**: a single thread runs back, as the chainstitch does, and two threads interlocked at each stitch hold, as the lockstitch does. The running restores a held side by carrying it with its other at the next turns, nothing removed.

**The next opening.** The five stitches drawn on the moving form, each pair joined across the centre, and the lockstitch carried at Engineering 1.14 as the stitch's own engineering face.
