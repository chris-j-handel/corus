# A reader at the session's close: each exploring script kept at no file, executed again and looked for at the folder

**A record, whole as it arrived.** Its marks are its own. What this working did with it is at `Records.md`.

# Review B: scratch results not carried by the committed v383Op folders

**Result.** Most exploratory results are carried. The clear gaps are alt.py's drawn-joins count, the exhaustive-order and 200,000-changing checks (bfs/bfs2/big), several tori breakdowns (tori.py, torinv.py, three_four.py, twice.py, explore_prior.py), the extra delivery modes in test3.py, the numeric extension of the step-611 test (test2.py), chk1/chk2 detail, and most of report.txt. The notes files carry no new reviewer feedback. v384A_offering.md may hold droplets the committed folder does not answer.

## 0. Method and caveats

- **Missing path.** `/home/claude/corus/carryings/v383Op/` does not exist. The first-report copy is `/home/claude/corus-u/carryings/v383Op/`. It has the same six md and eight py files as `/home/claude/corus/incoming/v383Op/`, except `At_The_Code.md` differs. I searched three roots: A = `corus-u/incoming/v383Op`, B = `corus/incoming/v383Op`, C = `corus-u/carryings/v383Op`. I also searched `corus-u/carry/` (committed droplets, 26 files tagged v383Op). Every NOT CARRIED item below was grepped by its numbers in all four places.
- **Run mechanics.** All scripts were run from `/home/claude/corus-u`. Outputs are saved in `/tmp/claude-0/-home-claude-corus/fb33d5a3-b8e6-5358-aeca-12dbe438030a/scratchpad/review_b/` (`<script>.out`; `.out2` for single re-runs; `still_alone.out3`).
- **Timeouts.** Launching 22 scripts together on 2 cores caused 120 s timeouts. I re-ran those singly.
  - Finished on re-run: big (64 s), explore_cell (26 s), explore_cell2 (22 s), loops2 (20 s), test3 (25 s).
  - `bfs.py` still timed out at 120 s. It had printed rings 2 to 6 and torus 2x2; torus 2x3 and crossed(2,3) were not reached.
  - `still_alone.py` needs 134 s. I let it finish under a 600 s limit.
  - All scripts are seeded, so results are deterministic.
- **Released instrument records.** Network_Surface.md:89-94 and Unresolveds E8/E9 released the one-slot, waiting-queue and absent-self runs as "an instrument's own storage and ordering", kept only "as a test's record". Uncarried extras from oneslot, test3 and hole are therefore partly deliberate omissions.

## 1. Per-script table

Status key: C = CARRIED, P = PARTLY, N = NOT CARRIED. File:line refers to the committed returned text unless stated.

| Script | What it computes | Key results | Status |
|---|---|---|---|
| alt.py | Reuses meeting_v382A.py's `a_self_still` to ask whether the cell that differs from Exhibit ONE's only at parting offerings (ALT: parting keeps the carrying and shares 0; match keep/0, mismatch invert/-, none invert/-) leaves a self at one parity. Tried at 10 named societies and at 160 drawn joins. | (1) ALT leaves a self still at "two lone selves releasing to a third", crossed(3,4), crossed(2,3). (2) ALT leaves none still at torus 3x3, 2x3, 3x4, 4x4, 2x2, crossed(2,2), crossed(4,4). (3) Exhibit ONE's cell is still at none of the 10. (4) Drawn joins, n = 4 to 7, 40 seeds each = 160 societies, each self receives from at least one and releases to 1 to 3, window T=80: ALT still at 131 of 160; Exhibit ONE at 0 of 160. | (1) and the five-society part of (3): C, `returned/meeting_v382A.txt:80-81`. (2) torus 3x3 and 2x3: implied. Torus 3x4, 4x4, 2x2, crossed(2,2), crossed(4,4): N. (4): N. |
| bfs.py | Non-deterministic search over all orders of delivery. Per-coupling FIFO queues; a self taking a parity that equals its carrying shares nothing, otherwise it takes it and shares it on. Opening c = -opening after the first momentary. Asks whether a rest (all queues empty) is reachable. | Rings 2 to 6, cap never hit: 0 non-alike openings can reach rest; 0 alike openings cannot reach rest. Torus 2x2 (queue cap 14): same, but cap hit, so not exhaustive. Torus 2x3 and crossed(2,3) not reached in 120 s. | P, see consolidated list item 2 |
| bfs2.py | Same search at torus 2x2 with a count-only state per channel. | Cap 2: 104,284 states; cap 3: 2,183,616 states. 0 non-alike openings reach rest; "capped" True. Ran 97 s under load. | N |
| big.py | no_common_now.py's `run`, random orders, bound 200,000 changings, non-alike openings only (30 drawn per society, alike ones skipped). | Torus 2x3: 29 non-alike openings, 0 at rest. Crossed(3,5): 30, 0 at rest. Spiral 5: 29, 0 at rest. | N. Committed bound is 4,000 changings. |
| chk1.py | Early (5 Oct). Event-driven, self-paced re-implementation of Exhibit ONE's cell (own `rule`, independent of `_1`), compared with Exhibit ONE's own `_17` stepping. 10 societies x 40 openings x 3 delivery orders. Also a rate-lock lead measurement. | All alike to the beat: 1,200 of 1,200. Max waiting queue: spiral 3 = 3, spiral 4 = 4, spiral 7 = 7, torus 2x3 = 3, 3x3 = 3, 3x5 = 5, 1x3 = 3, crossed(3,5) = 5, crossed(2,3) = 3, crossed(5,7) = 7. `_17` delivers exactly one item per sender per step from the second, 0s included. Rates uniform in [1, 1.618]: largest lead 4 (spiral 5), 4 (torus 3x3), 7 (crossed(3,5)) over 400 momentaries; picks where the self due by its own rate could not open: 15,621 of 20,000, 31,415 of 36,000, 27,335 of 32,000. | P |
| chk2.py | Cycle counting of the stepping together at tori, and a ring-of-inverters law check at every opening. | Distinct cycles of (carrying, shared): torus 3x3: 27 (2:21, 3:4, 4:1, 12:1); 3x5: 123 (2:105, 3:2, 4:6, 5:2, 12:5, 20:3); 2x3: 7; 1x3: 3. Ring law holds at every opening for n = 1 to 12. Openings per period are in item 4 below. | Cycles: C, `returned/stable_forms.txt:1-6`. Ring law to n=10: C, `corus/.../returned/ring_law.txt:2`. Rest: P/N, item 4. |
| cq.py | Checks italic spans in `git diff HEAD -- carry` against the corpus. | Prints nothing now (diff is empty, tree committed). Superseded by committed `quotes_check.py`; scratch `qc.txt` ends "quoted spans found: 420; not found: 0". | utility |
| rw.py | Checks offered sentences and Improving.md blockquotes against the Living File Registry's 59 released words. | Prints the count and no hits. Run against `18889e0..HEAD` it again gives no hit in offered sentences. | utility |
| verify.py, step.py | verify.py checks `file@@line@@codes@@sentence` quotes against Exhibit TWO and its carry/offer files. step.py prints Registry steps (661 found). | verify.py: c1 35 of 35, o1 112 of 112, final 322 of 322, e2 and e3 all, add 2 of 2. e1 has 2 misquotes (Ex2 871 and 957), superseded. | utility |
| explore_cell.py | Counts all 1,296 cells at conditions A (spiral of one passes all four joint forms of (carrying t, carrying t+1) in one cycle at both openings), B (living step at one other), C (no self still at torus 3x3). Then groups survivors by what each self carries. | A = 228. B = 96. A and B = 96, so B is inside A. A, B and C = 68, Exhibit ONE's cell among them. The 68 fall into 33 distinct carrying behaviours (one class of 4, 32 classes of 2) at ring 1, 2, 3, torus 2x3, 3x3, first 64 openings, 16 momentaries. | 96 and 68: C, `meeting_v382A.txt:64-72`. 228, "B inside A", and 33: N. |
| explore_cell2.py | Intersects B with "no self still" society by society, then adds D (a sharing is a changing shared). | B 96. After torus 3x3: 68; 2x3: 50; two lone selves releasing to a third: 24; crossed(3,4): 22; crossed(2,3): 22. D alone 16. B and D = 2 cells. All three = 1, Exhibit ONE's. The 22 without D differ in carrying as 10. | C, `meeting_v382A.txt:64-80`; Meeting_v382A.md item 4. |
| explore_prior.py | Which prior the next inverts. Per society, counts entries where the next equals the other's prior inverted, the all-or-none surfacing of the others' priors, own prior inverted, own now inverted. Then counts forms met by "next" from combinations of priors and nows. | Spirals 1 to 7 and two selves both ways: other's prior inverted at every entry (76, 304, 912, 2,432, 6,080, 14,592, 34,048). Tori: see item 6. | Spiral part and four forms columns: C, `meeting_v382A.txt:30-49`. Torus entry counts and two "nows" columns: N, item 6. |
| five.py | Two selves coupled both ways, stepped together, each opening. The "five" along the bounce line (O C O C O), Exhibit ONE's five (C O C O C), and the self's own five. | See item 7. | N |
| hole.py | One self absent after a common 40-momentary prior, 200 openings drawn by seeds 0 to 199, 60 momentaries on, tori 3x3, 4x5, 5x5. | See item 8. | P: earlier variant of network_surface.py part 4 |
| inturn.py | Two selves in turn, each opening, A first: entries (3,2,12,10,11), X/. marks. Spirals 1 to 8 entered in turn around: cycle length and number of changings that are not. | Identical to in_turn.txt parts 2 to 4 (e.g. spiral 5: 20 entries/10 not at 2 openings, 60/10 at 30; spiral 8: 24/8:4, 72/8:184, 72/24:68). | C, `returned/in_turn.txt:9-47` |
| loops.py | Spiral traces stepped together (R/T/. kinds), and per momentary counts of zeros, own releasings and takings for spirals 2 to 8, by opening class. | Takings = the opening's partings. Zeros and releasings alternate 0 and (n - w). Opening counts per w are 2*C(n,w): n=5: 2/20/10; n=6: 2/30/30/2; n=7: 2/42/70/14; n=8: 2/56/140/56/2. | C in substance, `returned/two_lines.txt:1-30`. Per-w counts are derivable. |
| loops2.py | Spirals 2 to 10 stepped together: takings equal the opening's partings and the rest alternate all still possibling / all releasing. Tori: is each count one number through the cycle. | Spirals: 2,044 of 2,044. Tori: takings and partings one number at all of 64/512/4,096. Still possiblings and releasings one number at 62, 126, 2,870. | C, `two_lines.txt:1-13` and `37-40` |
| oneslot.py | Prototype of network_surface.py part 3, column 1: one sharing resting per coupling, order drawn. | 120 of 120 runs at each of torus 2x3, 3x3, 3x4, 3x7, 5x5 reach 40 momentaries and equal the beat. | C, `network_surface.txt:19-24` |
| pair.py | Two selves, A entering first, each opening; then a "6.12-like" start. | First half: A's shares (-1,-1): -1,0,+1 repeating (period 3), B's -1,+1,0. Other openings analogous. Second half raises TypeError ('>' not supported between NoneType and int) because the script passes `('k', None)` as an empty carrying. | First half: C, `in_turn.txt:21-37`. Second half is a script error, not a finding about the resolver. See my addition below. |
| still_alone.py | Counts "no self still at the five societies" alone, then with the sharing and the living-step conditions, then the one-sender test at drawn joins. | 328 (Exhibit ONE's cell among them); sharing and no still 3; living and no still 22; drawn joins 101 societies, 245,632 of 245,632. | C, `meeting_v382A.txt:38-39, 78-79`. Needs 134 s. |
| test3.py | Network surface delivery modes, 600 runs over five tori (60 openings x 2 seeds). Also a "any" mode with 0 not delivered, a lockstep ordering and shuffled rounds. | See item 9. | P |
| three_four.py | "At 3 and 4": two selves each sharing to the other, and the tori. | Tables, 2,349,096 of 2,349,096, 3,426 of 3,426 and 299,484 as committed. Breakdown of takings in item 10. | P. Rest: C, `network_surface.txt:57-66`, Network_Surface.md:63-72. |
| tori.py | Tori 2x3, 3x3, 3x4, stationary window momentaries 21 to 60 (committed window is 2 to 60): kind mix, what the two sides offered, runs of still possibling, what follows. | See item 11. | P |
| torinv.py | Tori: momentary from which takings (k), and takings plus parting offerings (k2), are one number; second-momentary identity. | Second-momentary identity true at 64/64, 512/512, 4,096/4,096. Per-torus k and k2 in item 12. | Identity and aggregate k: C, `network_surface.txt:8-10`. Rest: N. |
| twice.py | Longest run of a self sharing 0 at consecutive momentaries, stepped together, random openings, larger tori. | Item 13. | N |
| ways.py | The sixteen ways of a next from a prior and a now. | 16 ways: 12 lose the prior, 4 carry it. Stills and cycles of the four: (2; 2+1+1), (1; 3+1), (1; 3+1), (0; 4). Inversion alone has no still. 4 ways independent of prior. "Injective in prior given now" gives the same four. Of 256 maps on four joint forms, 2 are single-parity four-cycles. | C, `corus/.../returned/priors_carried.txt` section 2. "Injective given now" equivalence not stated (minor). |
| t/test1.py | One-sender selves in 300 random graphs (3 to 7 selves, joins 0 to 4), first 64 openings, 30 momentaries. | 462,784 entries, 0 failures: next = the other's prior inverted. | C in statement, `meeting_v382A.txt:38-39`; Meeting_v382A.md item 2. Different sample. |
| t/test2.py | Step-611 bound under random-order asynchronous entry taking everything waiting, random graphs, self-loops allowed. Then with offerings preloaded before the first entry. | Item 14. | P |
| share.py | Fetches a claude.ai /share/ page. `share.txt` is "Can't reach Claude". | No content. | skipped |
| mend*.py, lay_*.py | Droplet-laying and mending scripts. | Skipped as instructed. | skipped |

## 2. Consolidated NOT CARRIED and PARTLY items (record-ready)

**1. alt.py: ALT cell at drawn joins and five more societies** [N]
- Cell ALT is `{'match': (1,0), 'mismatch': (-1,-1), 'parting': (1,0), 'none': (-1,-1)}`, using meeting_v382A.py's `a_self_still`.
- At drawn joins ALT leaves a self still at 131 of 160 societies; Exhibit ONE's cell at 0 of 160.
- Drawn joins: n = 4, 5, 6, 7; seeds 0 to 39 each; each self receives from at least one and releases to 1 to 3 others; T=80.
- ALT is not still at torus 3x4, 4x4, 2x2, crossed(2,2), crossed(4,4); Exhibit ONE's cell is still at none of these.

**2. bfs.py, bfs2.py, big.py: no order of delivery rests a non-alike opening** [P: statement carried, evidence not]
- Carried: Unresolveds.md:125 (E2) says "each other opening goes on". `returned/no_common_now.txt` has random orders to 4,000 changings, with only alike openings at rest.
- Exhaustive over all orders of delivery: spirals of 2, 3, 4, 5, 6 selves (4, 8, 16, 32, 64 openings, cap never hit). No non-alike opening can reach rest; every alike opening can.
- Torus 2x2, all 16 openings, queue cap 14: same result, but the cap was hit, so not exhaustive.
- bfs2.py, torus 2x2, per-channel count cap 2: 104,284 states; cap 3: 2,183,616 states. 0 non-alike openings reach rest; capped.
- Random orders to 200,000 changings (seeded Random(5); 30 drawn per society, alike ones skipped): torus 2x3, 29 non-alike, none at rest; crossed(3,5), 30, none; spiral 5, 29, none.

**3. chk1.py: pacing detail** [P]
- Carried: "alike at 120 of 120" and the "most ahead" leads (4 at spiral 5 and torus 3x3, 7 at crossed(3,5)): `returned/own_momentaries.txt:5-12`.
- Not carried: three delivery orders (random; always the lowest-index ready self; always the highest), 1,200 of 1,200 runs alike to Exhibit ONE's own `_17`.
- Not carried: max queue per society (spiral 3 = 3, spiral 4 = 4, spiral 7 = 7, torus 2x3 = 3, 3x3 = 3, 3x5 = 5, 1x3 = 3, crossed(3,5) = 5, crossed(2,3) = 3, crossed(5,7) = 7).
- Not carried: with rates uniform in [1, 1.618], the picks where the self due by its own rate could not open: spiral 5, 15,621 of 20,000; torus 3x3, 31,415 of 36,000; crossed(3,5), 27,335 of 32,000.
- Not carried: a worked trace "spiral 3, opening -+-... self 0 shared: 1,0,-1,1,-1,1,-1,0,1,-1,1,-1".

**4. chk2.py: rings of inverters, all openings to n = 12** [P]
- Carried: periods per n to 10 (ring_law.txt) and cycle counts (stable_forms).
- Not carried: law c(t+2) = -c[j-1](t) at every opening for n = 11 (2,048) and n = 12 (4,096).
- Not carried: openings per period in delays T (momentaries = 2T), as T:openings.

| n | T:openings |
|---|---|
| 1 | 2:2 |
| 2 | 1:2, 2:2 |
| 3 | 2:2, 6:6 |
| 4 | 1:2, 2:2, 4:12 |
| 5 | 2:2, 10:30 |
| 6 | 1:2, 2:2, 3:6, 6:54 |
| 7 | 2:2, 14:126 |
| 8 | 1:2, 2:2, 4:12, 8:240 |
| 9 | 2:2, 6:6, 18:504 |
| 10 | 1:2, 2:2, 5:30, 10:990 |
| 11 | 2:2, 22:2,046 |
| 12 | 1:2, 2:2, 3:6, 4:12, 6:54, 12:4,020 |

**5. explore_cell.py** [N for these]
- Condition A (spiral of one passes all four joint forms in one cycle, both openings): 228 of 1,296 cells. All 96 living-step cells are in A.
- The 68 cells that pass A, B and "no self still at torus 3x3" fall into 33 distinct carrying behaviours (one class of 4, 32 of 2). Societies: ring 1, 2, 3, torus 2x3, 3x3; first 64 openings; 16 momentaries.
- The 4-class is `{'match':(1,-1),'mismatch':(-1,-1),'parting':(-1,-1),'none':(-1,-1)}`. Exhibit ONE's cell sits in a class of 2.

**6. explore_prior.py at tori and two extra columns** [P]

| Torus | Entries | All-or-none of the two others' priors | Own prior inverted | Own now inverted |
|---|---|---|---|---|
| 3x3 | 129,024 | 125,460 | 36,126 | 111,150 |
| 2x3 | 10,752 | 10,404 | 1,128 | 10,224 |
| 3x4 | 884,736 | 824,328 | 179,424 | 798,840 |

- "Other's prior inverted" does not apply at a torus: 0 entries.
- Columns "others' nows" and "others' nows with own now" are not in meeting_v382A.txt:43-49.
  - Two selves and spiral of 5: nows alone give 2 forms, 2 at both nexts; nows plus own now give 4 forms, 2 at both nexts.
  - Torus 3x3 and 3x4: nows alone give 3 forms, 3 at both; nows plus own now give 6 forms, 2 at both.
  - So the others' nows never determine the next, while the others' priors do at one other (0 at both).

**7. five.py: the five, two selves stepped together** [N]
- Forms met by five-tuples, written as a string of +, -, 0.
- Bounce line (A's sharing at t, B's carrying at t+1, B's sharing at t+1, A's carrying at t+2, A's sharing at t+2):
  - Alike openings: 4 forms, `++0+-`, `--0-+`, `0+--0`, `0-++0`.
  - Parting openings: 2 forms, `+-+-+`, `-+-+-`.
- Exhibit ONE's five (other's 3 and 10 at t-1, self's 3, 10, 11 at t):
  - Alike: `+--0-`, `+0+--`, `-++0+`, `-0-++`.
  - Parting: `+-+--`, `-+-++`.
- Self's own five (offered at prior, carrying at prior, offered now, carrying now, offered at next):
  - Alike: same four as the bounce.
  - Parting: `+--++`, `-++--`.
- In all of these the fifth is the first inverted.
- Closest committed text, Two_Logics.md:244-262, says "two forms, by the opening" of the changing pattern, not of the five.

**8. hole.py: absent self, profile** [P]
- Committed in network_surface.txt part 4 (lines 28-55): "no present self ever carries otherwise" 172, 135, 180, 185 of 200; "sharing nothing twice: 0".
- hole.py uses a different draw (seeds 0 to 199) and no 7x7.
- Not carried: mean number of present selves differing from the intact run at momentaries 1, 2, 3, 5, 8, 12, 20, 40, 60.
  - 3x3 (8 present): 0.0, 0.2, 0.4, 0.7, 0.7, 0.4, 0.7, 0.6, 0.4.
  - 4x5 (19 present): 0.0, 0.2, 0.5, 0.8, 1.0, 1.1, 1.5, 2.1, 1.0.
  - 5x5 (24 present): 0.0, 0.1, 0.1, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3.
- Not carried: at momentary 60, differing at no present self in 158, 139, 183 of 200 openings; at every present self in 0.
- Not carried: kind mix per 1,000 entries, hole versus intact.

| Torus | With hole (. / P / R / T) | Intact (. / P / R / T) |
|---|---|---|
| 3x3 | 139 / 97 / 137 / 628 | 130 / 188 / 117 / 566 |
| 4x5 | 24 / 191 / 8 / 776 | 27 / 205 / 4 / 764 |
| 5x5 | 80 / 78 / 79 / 762 | 80 / 91 / 78 / 751 |

- `rerun.txt` (earlier network_surface.py output) adds, for the two selves the absent one released to, per 1,000 entries (taking / still possibling / releasing). The committed script computes it but does not print it.
  - 3x3: 712 / 145 / 143
  - 4x5: 935 / 33 / 32
  - 5x5: 843 / 79 / 78
  - 7x7: 892 / 54 / 54
- Unsure: whether the 158 versus the committed 172 at 3x3 is only the draw. The measures differ (momentary 60 versus ever), but 172 > 158 cannot be the same sample.

**9. test3.py: delivery modes, 600 runs over five tori** [P]
- Carried: each-side waiting equals the beat 600 of 600; whatever-has-come 0 of 600 (`network_surface.txt:19-24`); 0 not laid 106 of 600 equal, 526 complete.
- Not carried: whatever-has-come in lockstep (ready[0], round by round): 24 of 600 equal the beat.
- Not carried: whatever-has-come with 0 not delivered: 0 of 600 equal, 453 of 600 complete.
- Not carried: whatever-has-come in shuffled rounds (every self once per round in random order, FIFO queue per coupling): 600 of 600 equal the beat.
- Not carried: whatever-has-come, random order, one run per trial (300 runs): mean fraction of entries equal to the beat 0.466 (min 0.25, max 0.821); first diverging momentary mean 2.55 (min 2, max 7).

**10. three_four.py: after a still possibling** [P]
- Carried: 3,426 releasing at both and 299,484 taking.
- Not carried: the 299,484 splits by how many of the self's two sharing others it is then at one parity with: 0 of them 215,292; 1 of them 78,780; 2 of them 5,412. The 3,426 releasing are all at 2.

**11. tori.py: stationary window, momentaries 21 to 60** [P]
- Entries per 1,000 (. / P / R / T): 2x3: 47 / 344 / 16 / 594; 3x3: 135 / 156 / 127 / 582; 3x4: 87 / 229 / 29 / 655.
- Still possibling runs of 1 only (696 / 24,066 / 166,704). Next after one (R / T): 2x3 228 / 468; 3x3 342 / 23,724; 3x4 456 / 166,248.
- Sides offered by kind, per torus:

| Kind and sides | 2x3 | 3x3 | 3x4 |
|---|---|---|---|
| R, none/none | 240 | 23,400 | 56,160 |
| ., own/own | 240 | 23,400 | 56,160 |
| T, none/other | 480 | 1,440 | 115,200 |
| ., none/own | 480 | 1,440 | 115,200 |
| P, other/own | 5,280 | 28,800 | 451,200 |
| T, other/other | 8,640 | 105,840 | 1,172,160 |

- At the stationary window each releasing (none, none) is matched exactly by a still possibling (own, own), and each taking (none, other) by a still possibling (none, own). This is not stated in the committed folder; committed counts use window 2 to 60 and are summed over three tori.
- A one-opening 3x3 trace (opening -+-+-+-++) with T/./R/P counts per momentary 1 to 10 is also in `tori.out`.

**12. torinv.py: when the counts settle, per torus** [P]
- Takings one number from momentary k (k: openings), per torus:
  - 2x3: 1:4, 2:6, 3:18, 4:12, 5:12, 6:12.
  - 3x3: 1:2, 2:48, 3:30, 4:72, 5:54, 6:72, 7:72, 8:126, 9:36.
  - 3x4: 1:4, 2:66, 3:130, 4:240, 5:560, 6:768, 7:864, 8:744, 9:552, 10:144, 11:24.
- The sums over three tori match the committed aggregate at `network_surface.txt:10`.
- Takings plus parting offerings one number from momentary (k2), not carried:
  - 2x3: 1:2, 2:14, 3:24, 4:12, 5:12.
  - 3x3: 1:2, 2:60, 3:90, 5:54, 6:72, 7:72, 8:126, 9:36.
  - 3x4: 1:2, 2:194, 3:372, 4:384, 5:840, 6:864, 7:744, 8:528, 9:168.

**13. twice.py: longest run of a self sharing 0** [N]
- Stepped together, random openings. Longest run is 1 at every shape; it is 0 only where no 0 is ever shared.
- Shapes and openings drawn: (3,5), 300; (5,7), 300; (3,13), 300; (5,13), 40; (13,15), 40; (1,5), 300; (3,3), 300; (1,7), 300. T = 120 for small shapes and 200 for the 40-opening ones.
- No 0 ever shared: 3 of 300 at 3x5 and 26 of 300 at 3x3.
- Committed network_surface.txt:6 gives "0" at 2x3, 3x3, 3x4 only. The Registry's step-611 bound is two at a torus.

**14. t/test2.py: step-611 bound, other pacing** [P]
- Carried: the bound itself and "with offerings laid waiting before the opening it does not hold; the fresh reader ran that" (Meeting_v382A.md:87); 28 societies at 40 openings (`meeting_v382A.txt` part 5).
- Not carried: random-order entries, each taking everything waiting, random graphs of 1 to 6 selves with self-loops allowed, 4,000 graphs: 13,755 selves, 0 violations of "kept more than k+1".
- Not carried: with 0 to 3 offerings from {-1, 0, +1} waiting at each self before the first entry (no self-loops, 11,938 selves): 853 violations. Example: joins `{0:[2],1:[],2:[],3:[4,0,2],4:[3,2,0]}`, opening `{0:-1,1:-1,2:-1,3:1,4:1}`, preload `{0:[1,1,-1],1:[-1,-1],2:[1,1,0],3:[0],4:[]}`; self 1 has k=0 and is kept 2 entries.

**15. ways.py** [minor]
- "Carry the prior whole" is the same four ways as "injective in prior at each value of now". Not stated in the committed folder.

**16. report.txt** [P, see section 3]

**17. v384A feedback** [unsure scope, see section 3]

**My addition (not in scratch).** Exhibit ONE's resolver accepts an empty carrying as `[]`, not `[('k', None)]`. I re-ran pair.py's second half that way (both selves empty, each first receiving -1, then alternating A, B).
- A shares -,0,+,-,0,+,... and B shares -,+,0,-,+,0,...
- This is the same cycle as Exhibit TWO 6.12's "+,-,0,+,-,0". Unresolveds E6 states that trace's form from reading the file, not from a run.

## 3. Notes and output files

| File | What it is | Findings or feedback not carried? |
|---|---|---|
| report.txt (6 Oct 06:10) | A fresh reader's audit of Registry steps 1 to 68. Table of 67 step marks (F, N, G, B), attention points with counter-models, premises (a) to (e) for steps 51 to 57, a "short derivation", and nine minimal added givens. | **Partly.** Carried: counts 26 follow, 18 name, 20 add, 3 take one side (`Is_Or_Is_Not.md:16`), a nine-row "what the chain takes" table (lines 20-30), and the 16/4/12/256/2 arithmetic (`priors_carried.txt`). Not carried: the per-step table; the counter-models at steps 4 to 6 (flips at times 1/2, 3/4 or a dense order satisfy 1 to 4), 8 against 28 and 46 (a common now used while listed as not possible), 12 and 13, 31 to 40 (a->b->c->a; synchronous update fits 34 and 35), 42, 45 to 48 (an internal three-form cycle needs no outside thing; a fixed form is barred by 4, not by "beside"); premises (a) to (e) and the note that the short derivation needs turn-taking and fails under synchronous update; the report's own nine givens. Its items "carrying/not, both kinds exist, kind persists (12, 15, 23, 24)" and "prior and now independent inputs (52)" are in neither the committed nine nor Unresolveds. The committed nine instead include "a set, any set, an existing thing" and "which self releases to which", which are not in report.txt's nine. |
| rerun.txt (6 Oct 15:37) | Earlier output of network_surface.py. | **Yes.** Per-1,000 kind mix of the two selves downstream of the absent self (item 8). |
| mom.txt, pacing.txt, stable.txt, add.txt | mom.txt is returned/own_momentaries.txt plus a `time` line (8.3 s). pacing.txt is first-report `own_pacing.txt`. stable.txt is `stable_forms.txt`. add.txt is two Exhibit TWO sentence lines (1099, 1100). | None; first three identical to committed. add.txt is a quote index and is not in final.txt. |
| o1.txt, c1.txt, final.txt, e1 to e3 | Sentence indexes of Exhibit TWO (v371) and its carry and offering files, formatted `file@@line@@codes@@sentence`. e1 is the first draft (285 lines, two misquotes), e2 and e3 later drafts, final 322 lines, o1 and c1 the offering and carry sections. | No findings or reviewer feedback. The A to F code legend is not in the scratch directory, so I could not decode it. The index itself is in none of the committed folders. |
| share.txt, rerun_time.txt, time.txt | share.txt is the failed fetch of a claude.ai /share/ page. The others are timings (40.8 s and 30.1 s). | None. |
| c123.md, c123b.md, c126.md, pr_body.md, pr1_cur.md, pr2_body.md | PR comment and description drafts to v382A and v384A. | None; they restate README.md, Meeting_v382A.md and Meeting_v384A.md. |
| qc.txt, qc2.txt, quotes.txt, registry_steps.txt, ni_own.txt, carry_added.txt, added.json, diff.txt, cc_before.txt, cc_after.txt | Working data. qc ends "found 420, not found 0". | None. |
| no_common_now.out, observer.out, own_momentaries.out, stable_forms.out | Identical to committed returned text. | None. |
| v382A/*.md, hbm.md, phys_head.md | Copies of v382A's files and the Natural Physics offerings. | v382A/Meeting_v383Op.md is the file Meeting_v382A.md answers. The part I read (lines 1-140) is addressed there. I did not read lines 140-249. |
| v384A_dorm.md, v384A_offering.md | v384A's files, dated 7 Oct. | **Possibly.** The offering file has 22 droplets and a pointer to Concernings_v384A_v382A_v383Op.md. Meeting_v384A.md answers the dormancy questions and droplets 7 to 14 and 19 to 21 in substance. These do not appear in it. Droplet 15: the shared ten concernings. Droplets 16, 17 and 22: v384A's own withdrawals (offering/arriving framing, the abundancing "largest concern", a Values 5.3 inference). Droplet 18: pass 70 and the seed comparison. I am unsure whether answers were meant. |

## 4. Where I am unsure

- Whether uncarried extras from oneslot, test3 and hole were dropped on purpose as an instrument's records (Network_Surface.md:89-94).
- The meaning of "released" for hole.py's 158 against the committed 172 at torus 3x3 (see item 8).
- bfs.py semantics: "rest" means all per-coupling FIFO queues empty. This is my reading of the script, consistent with no_common_now.py's `run`.
- The A to F letters in the quote indexes.
- I did not read v382A/Meeting_v383Op.md beyond line 140.
