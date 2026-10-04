# Filing inventory: incoming/v380A, v380G, v380L, v380R

Read-only inventory at `main` 6976bcd, 4 October 2026. Nothing in the repository was edited. Word counts are `wc -w`.

**Classing rule used.** LAID: a carry entry names the file (or its folder) and itself carries the section and the saying, so the file is a source. OPEN: the body a later working needs (a draft, a list, a living place for conferring, a candidate file) is only in the incoming file, whether or not a carry entry points at it; "NOT LAID" marks the ones no carry entry names. DONE: entered, superseded, duplicated or a returned output. INSTRUMENT: a script a later working would run. "Probable" marks a class decided from the folder's own account and the absence of any carry pointer, not from reading the file sentence by sentence.

## Totals

| Folder | Files | Words | OPEN | LAID | DONE | INSTRUMENT |
|---|---|---|---|---|---|---|
| `incoming/v380A/` | 141 | 310,541 | 2 | 10 | 121 | 8 |
| `incoming/v380G/` | 6 | 3,564 | 0 | 1 | 5 | 0 |
| `incoming/v380L/` | 47 | 243,072 | 5 | 28 | 12 | 2 |
| `incoming/v380R/` | 27 | 79,306 | 9 | 13 | 5 | 0 |
| **All four** | 221 | 636,483 | 16 | 52 | 143 | 10 |

## Part 1. Each file

### `incoming/v380A/`

| File | Words | Class | What it is | Laid at / aims at / note |
|---|---|---|---|---|
| `Baseline_Manifest.json` | 485 | **DONE** | Source identities of the duplicated Exhibit TWO and kit at the first preservation commit |  |
| `Candidate_Changes.patch` | 7,276 | **DONE** | Complete diff of the candidate against root Exhibit TWO v371 | record, but companion of the OPEN candidate; keep beside it |
| `Candidate_Manifest.json` | 24 | **DONE** | Hash identity of the candidate; names `incoming/v380A/...` paths inside | record, companion of the OPEN candidate; its stored paths go stale if the candidate moves |
| `Exhibit_TWO_Natural_Networking_candidate.md` | 24,334 | **OPEN** | The working Exhibit TWO candidate, whole file, submitted for further improving | aims at Exhibit TWO Natural Networking; not entered (root is v371). Body is here; carry points via Manager_Handoff: `carry/TWENTY-FOUR_Geodesic_Improving_Method.md`:80 “Concern and offered paragraph, from archive/session_v380/v380A/Manager_Handoff.md, “Why this session…” (+1 more entries) |
| `Exhibit_TWO_Natural_Networking_working.md` | 24,334 | **DONE** | Working copy of Exhibit TWO; byte-identical to the candidate | duplicate (cmp equal) |
| `Handoff_Readiness.md` | 386 | **DONE** | Close standing of the handoff: review and check reach |  |
| `Improving_Passes.md` | 4,533 | **DONE** | Proposed passes for Natural Networking | superseded by the managing gathering `incoming/v380R/Natural_Networking_From_v380A.md` |
| `Manager_Handoff.md` | 2,739 | **LAID** | Full session handoff: findings, limits, communication failures, offered paragraph | `carry/TWENTY-FOUR_Geodesic_Improving_Method.md`:80 “Concern and offered paragraph, from archive/session_v380/v380A/Manager_Handoff.md, “Why this session…” (+1 more entries) |
| `Momentarying_Sequence_Offering.md` | 1,244 | **LAID** | The session's correction of the six-pair reading: changing or no changing through self-momentarying | `carry/ONE_Natural_Resolver.md`:132 “Concern, from archive/session_v380/v380A/Momentarying_Sequence_Offering.md, beside “The binary, at each of…” (+2 more entries) |
| `Pair_Public_Reading.json` | 439 | **DONE** | Returned public reading of the participating pair run |  |
| `Participating_Pair.md` | 1,333 | **DONE** | First bounded participating pair, executed once, its return and scope | gathered at `incoming/v380R/Natural_Networking_From_v380A.md`; no carry entry names it |
| `Perturbing_Cases.md` | 1,418 | **LAID** | Three bounded perturbing constructions, each executed once | `carry/ONE_Natural_Resolver.md`:144 “Concern, from archive/session_v380/v380A/Perturbing_Cases.md, at the across and along arrivings…” (+1 more entries) |
| `Perturbing_Cases_Checks.json` | 44 | **DONE** | Check results for the perturbing cases |  |
| `Prior_Passages.md` | 7,359 | **DONE** | Replaced Exhibit TWO passages preserved whole |  |
| `Progress.md` | 7,551 | **LAID** | v380A progress, concerns, opportunities, commits read; the improving question for Exhibit ONE | `carry/ONE_Natural_Resolver.md`:147 “Concern clarified, from archive/session_v380/v380A/Progress.md, “Improving question for Exhibit ONE,…” |
| `README.md` | 2,142 | **DONE** | Front of the folder: handoff banners, contents, record table | front/record; the 21 folder-level pointers `incoming/v380A/` resolve to this folder |
| `Session_Report.md` | 25,874 | **LAID** | Full session report: discoveries, opportunities, value and concerns, name by name 1-17 | laid by folder-level entries, e.g. `carry/ONE_Natural_Resolver.md`:105 “Concern, from incoming/v380A/, at the entry's own prior, “the…” (+17 more entries) |
| `Shared_Receiving_Learnings.md` | 795 | **LAID** | Receiving the shared learning at the concern (precision of the receiving concern) | `carry/ONE_Natural_Resolver.md`:151 “Further precision of the preceding receiving concern, from archive/session_v380/v380A/Shared_Receiving_Learnings.md.…” |
| `Six_Cycling_Offering.md` | 727 | **LAID** | Offered naming: self, bi and tri each arriving and releasing, the six cycling | `carry/ONE_Natural_Resolver.md`:113 “Concern, from archive/session_v380/v380A/Six_Cycling_Offering.md, beside connector dissolving and tri arriving:…” |
| `Surface_Arriving_Plan.md` | 1,093 | **LAID** | Preparation for beginning a surface through arriving | `carry/ONE_Natural_Resolver.md`:109 “Concern, from incoming/v380A/, beside “not releasing or releasing” and…” (+1 more entries) |
| `Surface_Changed_Coupling_Public_Reading.json` | 9,055 | **DONE** | Returned public reading, changed-coupling surface |  |
| `Surface_Construction.md` | 1,117 | **LAID** | The participating surface at the existing society expression, executed once | `carry/TWO_Natural_Networking.md`:35 “Ready, from archive/session_v380/v380A/Surface_Construction.md, for “Each self continuing through its…” |
| `Surface_Distinct_Arriving_Public_Reading.json` | 8,914 | **DONE** | Returned public reading, distinct-arriving surface |  |
| `Surface_Meeting_Arrivals_Public_Reading.json` | 9,090 | **DONE** | Returned public reading, meeting-arrivals surface |  |
| `Surface_Public_Reading.json` | 8,914 | **DONE** | Returned public reading, first surface |  |
| `Surface_Receiving_Map.json` | 397 | **DONE** | Data of the receiving map |  |
| `Surface_Receiving_Map.md` | 763 | **LAID** | One completing followed at its public arrivals (source-and-record correspondence) | `carry/ONE_Natural_Resolver.md`:144 “Concern, from archive/session_v380/v380A/Perturbing_Cases.md, at the across and along arrivings…” |
| `illustrating/Concept_And_Consistency.md` | 2,692 | **OPEN** | Consistency reading of Natural Illustrating v379 beside main and v380L: eleven passage-level opportunities | aims at Exhibit TWENTY-NINE Natural Illustrating; not entered. `carry/TWENTY-NINE_Natural_Illustrating.md`:33 “Ready, from the working v380A, its reading at incoming/v380A/illustrating/Concept_And_Consistency.md:…”; also linked from 4 kit files (5 links, sums-covered) |
| `illustrating/Illustrating_Findings.md` | 1,881 | **DONE** | Earlier findings and the next illustration proposed, preserved | superseded by Concept_And_Consistency |
| `illustrating/Origin_Study.md` | 1,239 | **DONE** | First origin study, continued | record; linked from kit START_HERE.md (sums-covered) |
| `illustrating/Progress.md` | 2,455 | **DONE** | Illustrating progress, 3 October |  |
| `illustrating/README.md` | 761 | **DONE** | Front of the illustrating contribution | linked from kit START_HERE.md (sums-covered) and `incoming/README.md` |
| `illustrating/Teaching_Exploration.md` | 1,172 | **DONE** | A discovery before the number names (teaching exploration) | record; linked from kit START_HERE.md (sums-covered) |
| `illustrating/Version_And_Workings.md` | 1,717 | **DONE** | Fixed session identity and value from the workings | record; linked from 3 kit files (sums-covered) |
| `illustrating/angle_correspondence.py` | 175 | **INSTRUMENT** | Angle correspondence check; "run from the repository root: python3 incoming/v380A/illustrating/angle_correspondence.py" |  |
| `illustrating/origin_pairs.py` | 350 | **INSTRUMENT** | Origin pairs computation; run from the repository root at its incoming path |  |
| `kit/INSTRUMENT_STANDING.md` | 1,066 | **DONE** | Source inspection of each networking instrument at its actual standing | record; value gathered at `incoming/v380R/Natural_Networking_From_v380A.md` ("a kit of no executing as ground") |
| `kit/Natural_Networking_Test_Kit_v368/README.md` | 3,111 | **DONE** | Duplicated Test Kit v368 file (differs from the copy in `kits/`: the working's edit) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/RingPureV265.java` | 490 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/SHA256SUMS` | 80 | **DONE** | Duplicated Test Kit v368 file (differs from the copy in `kits/`: the working's edit) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/allothers.py` | 706 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/STANDING.md` | 457 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/carrying.py` | 945 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/coattending.py` | 1,090 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/colinear.py` | 920 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/retake_signs.py` | 77 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/runs_v333/nesting_at_address.txt` | 592 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/runs_v333/nesting_at_sequencing.txt` | 594 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/runs_v333/nesting_at_sign.txt` | 516 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/runs_v333/signs_at_three_crossings.txt` | 543 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/artifacts/transmissioning.py` | 641 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/crt_counter_v265.py` | 185 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/diamond.py` | 322 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/doors.py` | 3,239 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/elsewhere.py` | 170 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/living.py` | 1,426 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/membrane.py` | 1,037 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/nesting.py` | 2,236 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/reach.py` | 263 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/recognition.py` | 290 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/resolver.py` | 219 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/resolver_pure_v265.c` | 706 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/resolver_pure_v265.js` | 286 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/resolver_pure_v265.ml` | 440 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/retell.py` | 209 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/ring_crossval_v265.py` | 92 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/ring_driver_v265.ml` | 315 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/ring_pure_v265.c` | 170 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/ring_pure_v265.js` | 81 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/ring_ref_v265.py` | 83 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/selftell.py` | 1,095 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/sensing.py` | 1,243 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/signs.py` | 1,525 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/society.py` | 262 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/stable_forms.py` | 542 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/stable_forms_returned.txt` | 271 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/test_resolver.py` | 811 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/Natural_Networking_Test_Kit_v368/unrelated.py` | 785 | **DONE** | Duplicated Test Kit v368 file (identical to the copy in `kits/Natural_Networking_TWO_Improving_Kit/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/README.md` | 754 | **DONE** | Front of the working kit (differs from `kits/Natural_Networking_TWO_Improving_Kit/README.md`) |  |
| `kit/SHA256SUMS` | 128 | **DONE** | Sums of the working kit, 64 relative paths | valid only while the kit folder moves whole |
| `kit/instruments_waiting/SHA256SUMS` | 22 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/own_turn_seam_returned_v366.txt` | 971 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/own_turn_seam_v366.py` | 921 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/resolver.py` | 219 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/returned_at_the_earlier_naming/ring_turns_returned.txt` | 2,111 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/returned_at_the_earlier_naming/ring_window_returned_v366.txt` | 253 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/returned_at_the_earlier_naming/window_scope_returned_v366.txt` | 48 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/ring_turns_at_v366_rings_3_to_13_returned.txt` | 1,986 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/ring_window_returned_v366.txt` | 261 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/ring_window_v366.py` | 1,265 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/window_scope_returned_v366.txt` | 66 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/instruments_waiting/window_scope_v366.py` | 437 | **DONE** | Duplicated waiting instrument / returned text (identical to the copy in `kits/`) | duplicate of the published kit; covered by `incoming/v380A/kit/SHA256SUMS` |
| `kit/one_code_checks.py` | 439 | **DONE** | Kit script, identical to `kits/Natural_Networking_TWO_Improving_Kit/one_code_checks.py` | duplicate of the published kit |
| `kit/one_forms.py` | 570 | **DONE** | Kit script, identical to `kits/Natural_Networking_TWO_Improving_Kit/one_forms.py` | duplicate of the published kit |
| `kit/participating_pair.py` | 347 | **INSTRUMENT** | First participating pair construction; only in this folder (not in `kits/`) | finds the root by `parents[3]` and opens `Exhibit_ONE_Natural_Resolver_v379.md`, which is no longer at the root: does not run as it stands, and a deeper folder breaks `parents[3]` |
| `kit/participating_surface.py` | 415 | **INSTRUMENT** | Participating surface construction; only in this folder (not in `kits/`) | finds the root by `parents[3]` and opens `Exhibit_ONE_Natural_Resolver_v379.md`, which is no longer at the root: does not run as it stands, and a deeper folder breaks `parents[3]` |
| `kit/resolver.py` | 218 | **INSTRUMENT** | Resolver reference expression pinned at Natural Resolver v378; imported by the working scripts | only in this folder at kit top level |
| `kit/ring_carrying_check.py` | 181 | **DONE** | Kit script, identical to `kits/Natural_Networking_TWO_Improving_Kit/ring_carrying_check.py` | duplicate of the published kit |
| `kit/surface_changed_coupling.py` | 449 | **INSTRUMENT** | Surface, changed coupling construction; only in this folder (not in `kits/`) | finds the root by `parents[3]` and opens `Exhibit_ONE_Natural_Resolver_v379.md`, which is no longer at the root: does not run as it stands, and a deeper folder breaks `parents[3]` |
| `kit/surface_distinct_arriving.py` | 415 | **INSTRUMENT** | Surface, distinct arriving construction; only in this folder (not in `kits/`) | finds the root by `parents[3]` and opens `Exhibit_ONE_Natural_Resolver_v379.md`, which is no longer at the root: does not run as it stands, and a deeper folder breaks `parents[3]` |
| `kit/surface_meeting_arrivals.py` | 428 | **INSTRUMENT** | Surface, meeting arrivals construction; only in this folder (not in `kits/`) | finds the root by `parents[3]` and opens `Exhibit_ONE_Natural_Resolver_v379.md`, which is no longer at the root: does not run as it stands, and a deeper folder breaks `parents[3]` |
| `living_ai_link/README.md` | 827 | **DONE** | Living AI link, first offering (pull request 119) | received and placed on the home page at commit 6976bcd |
| `reviews/Fresh_Reading_Local_Carrying.md` | 2,120 | **DONE** | Fresh reading of the proceeding "Local Carrying" | review record of the candidate |
| `reviews/Fresh_Reading_Participating_Pair.md` | 1,970 | **DONE** | Fresh reading of the proceeding "Participating Pair" | review record of the candidate |
| `reviews/Fresh_Reading_Perturbing_Cases.md` | 1,883 | **DONE** | Fresh reading of the proceeding "Perturbing Cases" | review record of the candidate |
| `reviews/Fresh_Reading_Routing.md` | 1,579 | **DONE** | Fresh reading of the proceeding "Routing" | review record of the candidate |
| `reviews/Fresh_Reading_Session_Handoff.md` | 1,951 | **DONE** | Fresh reading of the proceeding "Session Handoff" | review record of the candidate |
| `reviews/Fresh_Reading_Surface_Arriving.md` | 1,022 | **DONE** | Fresh reading of the proceeding "Surface Arriving" | review record of the candidate |
| `reviews/Fresh_Reading_Surface_Construction.md` | 1,428 | **DONE** | Fresh reading of the proceeding "Surface Construction" | review record of the candidate |
| `reviews/Fresh_Reading_Travelling.md` | 1,520 | **DONE** | Fresh reading of the proceeding "Travelling" | review record of the candidate |
| `reviews/Harm_Reading_Local_Carrying.md` | 2,315 | **DONE** | Harm reading of the proceeding "Local Carrying" | review record of the candidate |
| `reviews/Harm_Reading_Participating_Pair.md` | 1,918 | **DONE** | Harm reading of the proceeding "Participating Pair" | review record of the candidate |
| `reviews/Harm_Reading_Perturbing_Cases.md` | 1,613 | **DONE** | Harm reading of the proceeding "Perturbing Cases" | review record of the candidate |
| `reviews/Harm_Reading_Routing.md` | 1,957 | **DONE** | Harm reading of the proceeding "Routing" | review record of the candidate |
| `reviews/Harm_Reading_Session_Handoff.md` | 1,608 | **DONE** | Harm reading of the proceeding "Session Handoff" | review record of the candidate |
| `reviews/Harm_Reading_Surface_Arriving.md` | 1,307 | **DONE** | Harm reading of the proceeding "Surface Arriving" | review record of the candidate |
| `reviews/Harm_Reading_Surface_Construction.md` | 1,304 | **DONE** | Harm reading of the proceeding "Surface Construction" | review record of the candidate |
| `reviews/Harm_Reading_Travelling.md` | 1,931 | **DONE** | Harm reading of the proceeding "Travelling" | review record of the candidate |
| `reviews/carry_check_before_managing_merge.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/carry_check_final.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/carry_check_returned.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/check_set_returned.txt` | 59 | **DONE** | Returned output of `check_set.py` | review record of the candidate |
| `reviews/handoff_carry_check.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/handoff_check_set.txt` | 59 | **DONE** | Returned output of `check_set.py` | review record of the candidate |
| `reviews/handoff_reader_checks.txt` | 21,784 | **DONE** | Returned output of `reader_checks.py` | review record of the candidate |
| `reviews/local_carrying_prior.md` | 171 | **DONE** | Prior passage, preserved for the review | review record of the candidate |
| `reviews/local_carrying_proposed.md` | 448 | **DONE** | Proposed passage, as reviewed | review record of the candidate |
| `reviews/pair_carry_check.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/perturbing_cases_carry_check.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/quiet_releasing_prior.md` | 1,127 | **DONE** | Prior passage, preserved for the review | review record of the candidate |
| `reviews/quiet_releasing_proposed.md` | 1,195 | **DONE** | Proposed passage, as reviewed | review record of the candidate |
| `reviews/reader_checks_before_managing_merge.txt` | 13,184 | **DONE** | Returned output of `reader_checks.py` | review record of the candidate |
| `reviews/reader_checks_final.txt` | 13,275 | **DONE** | Returned output of `reader_checks.py` | review record of the candidate |
| `reviews/reader_checks_first_attempt.txt` | 235 | **DONE** | Returned output of `reader_checks.py` | review record of the candidate |
| `reviews/reader_checks_returned.txt` | 12,577 | **DONE** | Returned output of `reader_checks.py` | review record of the candidate |
| `reviews/routing_first_proposed.md` | 262 | **DONE** | Proposed passage, as reviewed | review record of the candidate |
| `reviews/routing_prior.md` | 221 | **DONE** | Prior passage, preserved for the review | review record of the candidate |
| `reviews/routing_proposed.md` | 276 | **DONE** | Proposed passage, as reviewed | review record of the candidate |
| `reviews/surface_arriving_carry_check.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/surface_construction_carry_check.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |
| `reviews/travelling_carry_check.txt` | 1,062 | **DONE** | Returned output of `carry_check.py` | review record of the candidate |

### `incoming/v380G/`

| File | Words | Class | What it is | Laid at / aims at / note |
|---|---|---|---|---|
| `Prompts_For_v380G.md` | 600 | **DONE** | Six prompts offered to the session v380G | the session ended; replies received |
| `README.md` | 1,091 | **LAID** | The record read part by part; carrying value estimated; three replies read | `carry/SEVENTEEN_Natural_Biology.md`:61 “Concern, at v380m, from archive/session_v380/v380G/README.md, for this file.…” (+1 more entries) |
| `Session_Record_2_v380G.md` | 378 | **DONE** | Second record / reply from the session v380G |  |
| `Session_Record_v380G.md` | 1,207 | **DONE** | The session v380G record as uploaded, 1,202 words |  |
| `v380G_3_Three_Replaced.md` | 154 | **DONE** | Third reply: three replaced |  |
| `v380G_4_Fourth_Sentence.md` | 134 | **DONE** | Fourth reply: the fourth sentence |  |

### `incoming/v380L/`

| File | Words | Class | What it is | Laid at / aims at / note |
|---|---|---|---|---|
| `Carrying_Of_Exhibit_ONE_Sorted.md` | 3,501 | **LAID** | Exhibit ONE's carrying, each of ninety entries read beside the file: entered, withdrawn, in part, open | still the working list for dissolving that carrying; use it before filing; `carry/ONE_Natural_Resolver.md`:43 “Ready, at v380R, from archive/session_v380/v380L/Carrying_Of_Exhibit_ONE_Sorted.md, for the working v380R…” (+1 more entries) |
| `Carrying_Of_Natural_Intelligence_Sorted.md` | 2,585 | **LAID** | Natural Intelligence's carrying, each entry read beside the file | still the working list for dissolving that carrying; `carry/Natural_Intelligence.md`:5 “Next at this file, at v380L: the conferring on…” (+1 more entries) |
| `Carrying_Of_The_Registry_Sorted.md` | 1,995 | **LAID** | The Registry's carrying sorted; that carrying already dissolved (`archive/carrying_v380L/`) | `carry/THIRTY_Co-Chaining_Logic_Registry.md`:15 “Ready, at v380L, from archive/session_v380/v380L/Carrying_Of_The_Registry_Sorted.md: this file at v380L,…” (+1 more entries) |
| `Chaining_A_Selfs_Changing.md` | 12,167 | **LAID** | A self's changing chained at the Registry's own steps; a sharing as a place with a value; two arrivings | `carry/ONE_Natural_Resolver.md`:33 “Ready, at v380, from archive/session_v380/v380L/Chaining_A_Selfs_Changing.md, its part on a…” (+2 more entries) |
| `Dissolving_Offered.md` | 1,566 | **LAID** | Offer: each entry entered or withdrawn, ready to leave its carrying | `carry/TWENTY-FOUR_Geodesic_Improving_Method.md`:35 “Ready, at v380R, from archive/session_v380/v380L/For_The_Managing.md, its twenty-fourth part: this…” |
| `Each_Break_Inverted.md` | 3,008 | **LAID** | Each break of the claim listed with its inversion | `carry/THIRTY_Co-Chaining_Logic_Registry.md`:51 “Concern, at v380L, from archive/session_v380/v380L/The_Claim_Broken_Further.md, for both and for…” |
| `Exhibit_ONE_Forms_At_The_Registry.md` | 2,788 | **LAID** | Exhibit ONE's diagram and twenty-two tables, each at the Registry's steps | `carry/ONE_Natural_Resolver.md`:35 “Ready, at v380, from archive/session_v380/v380L/For_The_Managing.md and archive/session_v380/v380L/Exhibit_ONE_Forms_At_The_Registry.md, for the…” |
| `For_Natural_Naming.md` | 877 | **LAID** | Offering for the conferring on Natural Naming beside the managing's gathering | `carry/TWENTY_Natural_Naming.md`:35 “Ready, at v380l, from archive/session_v380/v380L/For_Natural_Naming.md, beside incoming/v380R/Natural_Naming_Gathering.md, for the…” |
| `For_The_Managing.md` | 8,541 | **LAID** | Advice for the managing in 24 parts: the round, tables read by hand, improvings of ONE, Naming, TWENTY-FOUR, TWENTY-SIX | `carry/ONE_Natural_Resolver.md`:35 “Ready, at v380, from archive/session_v380/v380L/For_The_Managing.md and archive/session_v380/v380L/Exhibit_ONE_Forms_At_The_Registry.md, for the…” (+9 more entries) |
| `Gathered_Value_1.md` | 4,978 | **LAID** | Transcript lines 1-720: each piece of value and where the repository carries it | laid by range "Gathered_Value_1.md to 4.md": `carry/ELEVEN_Natural_Medicine.md`:25 “Concern, at v380L, from incoming/v380L/Progress.md, its closing account: sentences…” (+5 more entries) |
| `Gathered_Value_2.md` | 4,115 | **LAID** | Transcript lines 721-1440: each piece of value and where the repository carries it | laid by range "Gathered_Value_1.md to 4.md": `carry/ELEVEN_Natural_Medicine.md`:25 “Concern, at v380L, from incoming/v380L/Progress.md, its closing account: sentences…” (+5 more entries) |
| `Gathered_Value_3.md` | 4,848 | **LAID** | Transcript lines 1441-2160: each piece of value and where the repository carries it | laid by range "Gathered_Value_1.md to 4.md": `carry/ELEVEN_Natural_Medicine.md`:25 “Concern, at v380L, from incoming/v380L/Progress.md, its closing account: sentences…” (+5 more entries) |
| `Gathered_Value_4.md` | 6,871 | **LAID** | Transcript lines 2161-2888: each piece of value and where the repository carries it | laid by range "Gathered_Value_1.md to 4.md": `carry/ELEVEN_Natural_Medicine.md`:25 “Concern, at v380L, from incoming/v380L/Progress.md, its closing account: sentences…” (+5 more entries) |
| `Gathering_For_Numbers_Mathematics_Intelligence.md` | 2,833 | **DONE** | Gathering for Natural Numbers, Mathematics and Intelligence | an "earlier paper, as it was" (Progress line 172); the three files then moved at v380L/v380R; no carry entry names it — probable, verify |
| `Group_Twenty_At_The_Three.md` | 2,351 | **DONE** | The Registry's seventy-two steps on sharing and the seventeen names, each at the three | earlier paper; Registry entered at v380L; no carry entry names it — probable |
| `Incoherings_For_The_Subject.md` | 2,577 | **LAID** | Each thing parting, sorted at the numbers: ONE's tables matched to the resolver's lines | `carry/ONE_Natural_Resolver.md`:37 “Ready, at v380, from archive/session_v380/v380L/Incoherings_For_The_Subject.md, for the working v380R…” |
| `Naming_And_Chaining_At_Exhibit_ONE.md` | 1,193 | **DONE** | Three things open at the Registry said at ONE's row, the step and Naming's sentence | earlier paper; no carry entry names it — probable |
| `Progress.md` | 17,825 | **LAID** | v380L progress with its closing account and the part *Now*; the source 42 pointers name | `carry/EIGHTEEN_Natural_Physics.md`:118 “Ready, at v379, from incoming/v380L/Progress.md, its part *Now*: one…” (+40 more entries) |
| `README.md` | 5,256 | **LAID** | The report whole: 22 findings, entries at the carryings, instruments | laid by folder-level entries "from `incoming/v380L/`, finding N": `carry/THREE_Natural_Numbers.md`:40 “Concern, at v380, from incoming/v380L/, finding 10, for both:…” (+2 more entries) |
| `Registry_Beside_Exhibit_ONE_Naming.md` | 1,018 | **DONE** | The Registry beside Exhibit ONE's naming and explaining (cohering at v380l) | entered at the Registry v380l; no carry entry names it |
| `Registry_Negations_Sorted.md` | 3,635 | **OPEN** | The Registry's 146 negating sentences, sorted | aims at Exhibit THIRTY; the list is the body of the file's next: `carry/THIRTY_Co-Chaining_Logic_Registry.md`:5 “Next at this file, at v380L: seventeen unsure lines,…” |
| `Session_Transcript_v380L.txt` | 49,269 | **DONE** | The session transcript whole, 2,888 lines |  |
| `The_Claim_Broken_Further.md` | 2,096 | **LAID** | Five more readers at the claim, beside the managing's eleven breaks | `carry/THIRTY_Co-Chaining_Logic_Registry.md`:51 “Concern, at v380L, from archive/session_v380/v380L/The_Claim_Broken_Further.md, for both and for…” (+1 more entries) |
| `closing_drafts/Natural_Intelligence_Fifty-Four_Read_By_Hand.md` | 5,569 | **OPEN** | Draft: the fifty-four re-sayings of sharing across / releasing along read by hand, eight mends | aims at Natural Intelligence; entered at no file. `carry/Natural_Intelligence.md`:36 “Ready, at v380R, from incoming/v380L/Progress.md, its closing account: the…” |
| `closing_drafts/Registry_Cause_And_Twins.md` | 14,181 | **OPEN** | Draft: the Registry gathered at cause, and the twins of the newest namings | aims at Exhibit THIRTY; entered at no step. `carry/THIRTY_Co-Chaining_Logic_Registry.md`:25 “Ready, at v380L, from incoming/v380L/Progress.md, its closing account: three…” |
| `closing_drafts/Registry_Negations_At_The_Purpose.md` | 8,501 | **OPEN** | Draft: the Registry's 146 negations read at Natural Naming's purpose | aims at Exhibit THIRTY; entered at no step. `carry/THIRTY_Co-Chaining_Logic_Registry.md`:25 “Ready, at v380L, from incoming/v380L/Progress.md, its closing account: three…” |
| `closing_drafts/Round_At_Four_Parities_Deriving.md` | 6,752 | **OPEN** | Draft: the round at four parities, the deriving and the exact place it stops | aims at Exhibit ONE; entered at no file. `carry/ONE_Natural_Resolver.md`:55 “Ready, at v380R, from incoming/v380L/Progress.md, its closing account: the…” |
| `derivings/Odd_Torus_Derived.md` | 3,980 | **DONE** | T1: steps 650-651 and the odd torus worked by hand | steps 646-661 are entered at the Registry v380L; record of the deriving |
| `derivings/Odd_Torus_Second_Reading.md` | 3,009 | **DONE** | T2: second reading of steps 652-657 | steps 646-661 are entered at the Registry v380L; record of the deriving |
| `derivings/Spiral_Law_Read_By_Hand.md` | 4,469 | **DONE** | S1: steps 646-649 read by hand | steps 646-661 are entered at the Registry v380L; record of the deriving |
| `derivings/The_Cells_For_Working_By_Hand.md` | 447 | **DONE** | A helper's brief: the resolver's cells for working by hand | steps 646-661 are entered at the Registry v380L; record of the deriving |
| `derivings/Two_Spirals_Crossed_Derived.md` | 4,125 | **DONE** | X1: two spirals crossed, eight rows derived | steps 646-661 are entered at the Registry v380L; record of the deriving |
| `derivings/Two_Spirals_Crossed_Second_Reading.md` | 4,144 | **DONE** | X2: second reader, steps 658-661 | steps 646-661 are entered at the Registry v380L; record of the deriving |
| `derivings/torus_rule_arithmetic.py` | 256 | **INSTRUMENT** | Torus rule arithmetic; "from the repository root: python3 archive/session_v380/v380L/derivings/torus_rule_arithmetic.py" |  |
| `instruments.py` | 4,312 | **INSTRUMENT** | Sixteen instruments at the newest Exhibit ONE resolver (globs the root); "python3 incoming/v380L/instruments.py" | named in `incoming/README.md`-style instructions and in `incoming/v380R/For_The_Workings.md` |
| `instruments_returned.txt` | 3,059 | **DONE** | Returned text of instruments.py | regenerable |
| `readings/Natural_Mathematics_Reading_MA.md` | 2,760 | **LAID** | MA: Natural Mathematics v378 lines 1-184 worked | laid through the Progress / folder pointer, not by filename: `carry/FOUR_Natural_Mathematics.md`:22 “Ready, at v380L, from incoming/v380L/Progress.md, its closing account: the…” |
| `readings/Natural_Mathematics_Reading_MB.md` | 3,655 | **LAID** | MB: lines 185-316 | laid through the Progress / folder pointer, not by filename: `carry/FOUR_Natural_Mathematics.md`:22 “Ready, at v380L, from incoming/v380L/Progress.md, its closing account: the…” |
| `readings/Natural_Mathematics_Reading_MC.md` | 2,959 | **LAID** | MC: lines 317-460 | laid through the Progress / folder pointer, not by filename: `carry/FOUR_Natural_Mathematics.md`:22 “Ready, at v380L, from incoming/v380L/Progress.md, its closing account: the…” |
| `readings/Natural_Mathematics_Reading_RM.md` | 2,427 | **LAID** | RM: fresh reading of Natural Mathematics v380L against its diff | laid through the Progress / folder pointer, not by filename: `carry/FOUR_Natural_Mathematics.md`:22 “Ready, at v380L, from incoming/v380L/Progress.md, its closing account: the…” |
| `readings/Natural_Numbers_Reading_A.md` | 3,693 | **LAID** | A: Natural Numbers v380R lines 96-230 | laid through the Progress / folder pointer, not by filename: `carry/THREE_Natural_Numbers.md`:13 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: this file at v380L…” (bullets hold the findings) and :42 |
| `readings/Natural_Numbers_Reading_B.md` | 4,077 | **LAID** | B: lines 231-334 | laid through the Progress / folder pointer, not by filename: `carry/THREE_Natural_Numbers.md`:13 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: this file at v380L…” (bullets hold the findings) and :42 |
| `readings/Natural_Numbers_Reading_C.md` | 3,609 | **LAID** | C: lines 335-419 | laid through the Progress / folder pointer, not by filename: `carry/THREE_Natural_Numbers.md`:13 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: this file at v380L…” (bullets hold the findings) and :42 |
| `readings/Natural_Numbers_Reading_D.md` | 3,163 | **LAID** | D: lines 420-559 | laid through the Progress / folder pointer, not by filename: `carry/THREE_Natural_Numbers.md`:13 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: this file at v380L…” (bullets hold the findings) and :42 |
| `readings/Natural_Numbers_Reading_E.md` | 2,800 | **LAID** | E: lines 1-95 and 560-1010 | laid through the Progress / folder pointer, not by filename: `carry/THREE_Natural_Numbers.md`:13 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: this file at v380L…” (bullets hold the findings) and :42 |
| `readings/Natural_Numbers_Reading_R.md` | 2,608 | **LAID** | R: Natural Numbers v380L, the altered places | laid through the Progress / folder pointer, not by filename: `carry/THREE_Natural_Numbers.md`:13 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: this file at v380L…” (bullets hold the findings) and :42 |
| `readings/Sharing_Across_Releasing_Along_Reading.md` | 2,624 | **LAID** | R2: THIRTY, THIRTEEN and a third file re-said to sharing across / releasing along | laid through the Progress / folder pointer, not by filename: `carry/THIRTY_Co-Chaining_Logic_Registry.md`:19 “Ready, at v380L, from incoming/v380L/Progress.md, its part Now: sharing across and releasing along…” |

### `incoming/v380R/`

| File | Words | Class | What it is | Laid at / aims at / note |
|---|---|---|---|---|
| `Concerns_Of_The_Three_Workings.md` | 865 | **LAID** | The concerns of the three workings, each met or open | `carry/ONE_Natural_Resolver.md`:153 “Concern, at v380, from archive/session_v380/v380R/Concerns_Of_The_Three_Workings.md, for both, the hardest…” (+1 more entries) |
| `Exhibit_ONE_First_Motion_Draft.md` | 1,441 | **DONE** | Draft of Exhibit ONE's first motion: opening, data, each table at title and conditions | entered at Exhibit ONE v380 (Session Record, "Exhibit ONE at v380, a first motion"); pointed only from the front's history paragraph |
| `Exhibit_ONE_Improving.md` | 2,003 | **LAID** | Each thing an improving of Exhibit ONE meets, gathered from three workings | `carry/ONE_Natural_Resolver.md`:21 “Ready, at v380, from archive/session_v380/v380R/Exhibit_ONE_Improving.md, three workings' findings gathered,…” (+5 more entries) |
| `For_The_Workings.md` | 9,584 | **LAID** | The managing report to the workings: the plan, the resolver as bi-coupling, the few things parting | the plan is entered at the Geodesic Improving Method v380R 2.8; also named in kit `swimmers_v380A/README.md` (sums-covered); `carry/ONE_Natural_Resolver.md`:167 “Concern, at v380, from archive/session_v380/v380R/Two_Parities_Gathered_And_Worked.md, its last two parts,…” (+11 more entries) |
| `Natural_Naming_Beside_Receiving_Exhibits.md` | 8,038 | **OPEN** | Each section another exhibit could carry, read beside that exhibit: 68 already, 39 in part, 55 only here | aims at Natural Naming (and the receiving exhibits); unreviewed, "for conferring"; NOT LAID — no carry entry names it |
| `Natural_Naming_Conferring.md` | 2,427 | **OPEN** | The conferring gathered: ten namings decided, eight open | aims at Natural Naming; body is here. `carry/TWENTY_Natural_Naming.md`:148 “Next, at v380l: this file's conferring gathered at incoming/v380R/Natural_Naming_Conferring.md.…” |
| `Natural_Naming_Each_Section_Read.md` | 6,276 | **OPEN** | Each of 110 sections read at one test: 9 carry, 55 mixed, 48 add little | aims at Natural Naming; only Part Four was reduced from it; NOT LAID — no carry entry names it |
| `Natural_Naming_Gathering.md` | 1,020 | **OPEN** | Improving opportunities gathered: twelve themes, twenty-three partings, an order for conferring | aims at Natural Naming; "nothing enters until conferred". `carry/TWENTY_Natural_Naming.md`:140 “Next, at v380l: the gathering for this file's improving,…” |
| `Natural_Naming_Negations_Sorted.md` | 10,111 | **DONE** | Each negating word of Natural Naming v380R sorted, with drafted re-sayings | the sorting entered at Natural Naming v380R (Session Record line 2249); what remains is in Negations_Yet |
| `Natural_Naming_Negations_Yet.md` | 2,700 | **OPEN** | Ninety-four clauses still said by a negation, each with a reviewer's reason | aims at Natural Naming; the list is the body. `carry/TWENTY_Natural_Naming.md`:152 “Next: the facts yet said by a negation, each…” (+2 more entries) |
| `Natural_Naming_Part_Four_Released.md` | 2,066 | **DONE** | The seventy-eight things released from Part Four at its reducing | record of a motion done; pointed from the Session Record; pairs with `archive/Natural_Naming_v380R_Part_Four_before_reducing.md` |
| `Natural_Naming_Second_Reading.md` | 2,165 | **OPEN** | Twenty-five sections a first reader found nothing in, read again: one may leave, fifteen said whole elsewhere | aims at Natural Naming; NOT LAID — no carry entry names it |
| `Natural_Naming_Value_Sorted.md` | 596 | **OPEN** | Natural Naming's value sorted at its purpose (which sections are another exhibit's) | aims at Natural Naming; NOT LAID — no carry entry names it |
| `Natural_Networking_From_v380A.md` | 826 | **OPEN** | The carrying value of v380A gathered for a new Natural Networking and kit: five motions offered | aims at Exhibit TWO; body is here. `carry/TWO_Natural_Networking.md`:39 “Next at this file, at v380, from incoming/v380R/Natural_Networking_From_v380A.md, the…” |
| `One_Self_Followed.md` | 626 | **LAID** | One self followed through one momentary at Exhibit ONE's names | `carry/ONE_Natural_Resolver.md`:23 “Ready, at v380, from archive/session_v380/v380R/One_Self_Followed.md, meeting the working v380A's…” |
| `Premise_Alternating_Followed.md` | 1,908 | **LAID** | The premise followed: the carrying alternating, an arriving a second changing | `carry/ONE_Natural_Resolver.md`:35 “Ready, at v380, from archive/session_v380/v380L/For_The_Managing.md and archive/session_v380/v380L/Exhibit_ONE_Forms_At_The_Registry.md, for the…” (+3 more entries) |
| `Progress.md` | 3,530 | **LAID** | v380R progress and what was learned about working at the three workings | `carry/TWENTY-FOUR_Geodesic_Improving_Method.md`:25 “Ready, at v380, from archive/session_v380/v380R/Progress.md, its sections on what…” (+2 more entries) |
| `README.md` | 733 | **LAID** | v380R opening report: four findings on the names, three learnings | `carry/ONE_Natural_Resolver.md`:77 “Concern, at v380, from incoming/v380R/README.md, its second and fourth…” (+4 more entries) |
| `Registry_Beside_Exhibit_ONE_v380l.md` | 951 | **DONE** | The Registry v380f beside Exhibit ONE v380R, an offering to v380L | v380L ended and answered it at the Registry v380L; no carry entry names it |
| `Rigor_A_Fresh_Reading_And_Three_Workings.md` | 2,861 | **LAID** | The tour met for rigor by a fresh reader at each of the seventeen; three workings exchanged | `carry/ONE_Natural_Resolver.md`:136 “Concern, at v380, from archive/session_v380/v380R/Rigor_A_Fresh_Reading_And_Three_Workings.md, for both: the picture…” (+8 more entries) |
| `The_Claim_Broken.md` | 1,422 | **LAID** | The claim and each place it broke (headed Withdrawn); concerns still cite its last part | `carry/ONE_Natural_Resolver.md`:197 “Concern, at v380l, from archive/session_v380/v380R/The_Claim_Broken.md, its last part, for…” (+2 more entries) |
| `The_Claim_To_Break.md` | 401 | **DONE** | The claim set out to be broken (headed Withdrawn) | superseded by The_Universal_Claim_Gathered |
| `The_Universal_Claim.md` | 3,159 | **OPEN** | The universal claim, open for examining: four sentences, links not yet worked, a table for a better fourth | aims at Natural Intelligence and Exhibit THIRTY; a living place, "nothing entered until conferred". `carry/THIRTY_Co-Chaining_Logic_Registry.md`:43 “Next, at v380l: the universal claim living for each…” (+1 more entries) |
| `The_Universal_Claim_Gathered.md` | 1,464 | **LAID** | The universal claim gathered link by link from the files that carry it | `carry/TWENTY_Natural_Naming.md`:142 “Concern, at v380l, from the session, for this file's…” (+2 more entries) |
| `Three_Workings_Combined.md` | 1,112 | **LAID** | Three workings combined: one going, said at three files | `carry/ONE_Natural_Resolver.md`:116 “Concern, at v380, from archive/session_v380/v380R/Three_Workings_Combined.md, for both: three workings…” (+2 more entries) |
| `Tour_A_Living_Self_Is_A_Carrying.md` | 8,089 | **LAID** | A living self is a carrying, followed through each stable form of Exhibit ONE | `carry/ONE_Natural_Resolver.md`:87 “Concern, at v380, from archive/session_v380/v380R/Tour_A_Living_Self_Is_A_Carrying.md, for both: a living…” (+25 more entries) |
| `Two_Parities_Gathered_And_Worked.md` | 2,932 | **LAID** | Two parities at a self: gathered from v380L, worked again, added to | `carry/ONE_Natural_Resolver.md`:161 “Ready, at v380, from archive/session_v380/v380R/Two_Parities_Gathered_And_Worked.md, gathering the working v380L's…” (+4 more entries) |

## Part 2. Pointers

Searched every tracked file outside `archive/` and `.git` for `incoming/v380[AGLR]…`, plus relative markdown links (`](../../../incoming/v380R/v380X/…)`, `](../../../incoming/v380X/…)`) in `incoming/` files outside the four folders. `README.md` at the root, `build.js`, `files.json`, `index.html`, `read.html` and `corus.js` carry none.

### 2a. Pointing files outside the four folders (28 files)

| Pointing file | `incoming/v380…` paths | Relative links | Covered by a kit `SHA256SUMS` |
|---|---|---|---|
| `carry/Exhibit_ONE_Natural_Resolver.md` | 73 | 0 | no |
| `carry/Exhibit_TWENTY_Natural_Naming.md` | 32 | 0 | no |
| `carry/Exhibit_THIRTY_Co-Chaining_Logic_Registry.md` | 20 | 0 | no |
| `carry/Exhibit_TWO_Natural_Networking.md` | 18 | 0 | no |
| `carry/Natural_Intelligence.md` | 16 | 0 | no |
| `carry/Living_Improving_Value.md` | 14 | 0 | no |
| `carry/Exhibit_TWENTY-FOUR_Geodesic_Improving_Method.md` | 13 | 0 | no |
| `carry/Session_Record.md` | 13 | 0 | no |
| `incoming/README.md` | 0 | 12 | no |
| `Exhibit_TWENTY-SIX_Living_File_Registry_v380R.md` | 10 | 0 | no (living file: an edit is a motion of the file) |
| `carry/Exhibit_TWENTY-NINE_Natural_Illustrating.md` | 7 | 0 | no |
| `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/START_HERE.md` | 6 | 0 | **yes**, `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/SHA256SUMS` (renew sums on edit) |
| `carry/Exhibit_TWENTY-SIX_Living_File_Registry.md` | 5 | 0 | no |
| `incoming/natural_networking_2026-10-01/README.md` | 1 | 4 | no |
| `carry/Exhibit_THREE_Natural_Numbers.md` | 4 | 0 | no |
| `carry/Exhibit_FOUR_Natural_Mathematics.md` | 3 | 0 | no |
| `carry/Exhibit_EIGHTEEN_Natural_Physics.md` | 2 | 0 | no |
| `carry/Exhibit_ELEVEN_Natural_Medicine.md` | 2 | 0 | no |
| `carry/Exhibit_SEVENTEEN_Natural_Biology.md` | 2 | 0 | no |
| `carry/Exhibit_TEN_Natural_Health.md` | 2 | 0 | no |
| `carry/Exhibit_THIRTEEN_Resolving_Hard_Problems.md` | 2 | 0 | no |
| `carry/Exhibit_TWENTY-EIGHT_Equilibria_Registry.md` | 2 | 0 | no |
| `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/origin_v380A/README.md` | 2 | 0 | **yes**, `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/SHA256SUMS` (renew sums on edit) |
| `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/swimmers_v380A/README.md` | 2 | 0 | **yes**, `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/SHA256SUMS` (renew sums on edit) |
| `carry/Exhibit_SEVEN_Natural_Societies.md` | 1 | 0 | no |
| `carry/Exhibit_TWELVE_Natural_Explaining.md` | 1 | 0 | no |
| `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/README.md` | 1 | 0 | **yes**, `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/SHA256SUMS` (renew sums on edit) |
| `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/continuity_v380A/README.md` | 1 | 0 | **yes**, `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/SHA256SUMS` (renew sums on edit) |
| **Total** | **255** | **16** | 5 sums-covered files, all in `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/` |

### 2b. Pointing files inside the four folders (they move or stay with their folder)

| Folder | Files carrying repository-root `incoming/v380…` paths | Path mentions |
|---|---|---|
| `incoming/v380A/` | 19 | 3,939 |
| `incoming/v380G/` | 2 | 7 |
| `incoming/v380L/` | 23 | 171 |
| `incoming/v380R/` | 8 | 25 |
| **Total** | **52** | **4,142** |

Of the v380A mentions, about 3,890 are in four returned `reader_checks` outputs under `reviews/`. None of the pointer-carrying files inside `incoming/v380A/kit/` is listed in that kit's own `SHA256SUMS`; the three inner `SHA256SUMS` hold relative paths and stay valid only if `kit/` moves whole. `incoming/v380A/Candidate_Manifest.json` stores two `incoming/v380A/…` paths as data.

Also outside the search scope but affected: 8 files under `archive/` already point into these folders (`archive/carrying_v380L/*` ×7, `archive/Natural_Naming_v380R_Part_Four_before_reducing.md`).

### 2c. Targets named from outside, by count

| Target | Pointers | Class of target | Stays in `incoming/` under the recommended filing |
|---|---|---|---|
| `incoming/v380A` | 1 | folder | moves: pointer edit |
| `incoming/v380A/` | 20 | folder | moves: pointer edit |
| `archive/session_v380/v380A/Manager_Handoff.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Momentarying_Sequence_Offering.md` | 4 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Perturbing_Cases.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Progress.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Shared_Receiving_Learnings.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Six_Cycling_Offering.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Surface_Arriving_Plan.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Surface_Construction.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380A/Surface_Receiving_Map.md` | 1 | LAID | moves: pointer edit |
| `incoming/v380A/illustrating` | 1 | folder | stays |
| `incoming/v380A/illustrating/` | 2 | folder | stays |
| `incoming/v380A/illustrating/Concept_And_Consistency.md` | 5 | OPEN | stays |
| `incoming/v380A/illustrating/Origin_Study.md` | 1 | DONE | stays |
| `incoming/v380A/illustrating/README.md` | 1 | DONE | stays |
| `incoming/v380A/illustrating/Teaching_Exploration.md` | 1 | DONE | stays |
| `incoming/v380A/illustrating/Version_And_Workings.md` | 3 | DONE | stays |
| `archive/session_v380/v380G/README.md` | 4 | LAID | moves: pointer edit |
| `incoming/v380L/` | 12 | folder | moves: pointer edit |
| `archive/session_v380/v380L/Carrying_Of_Exhibit_ONE_Sorted.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Carrying_Of_Natural_Intelligence_Sorted.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Carrying_Of_The_Registry_Sorted.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Chaining_A_Selfs_Changing.md` | 3 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Dissolving_Offered.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Each_Break_Inverted.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Exhibit_ONE_Forms_At_The_Registry.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/For_Natural_Naming.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/For_The_Managing.md` | 10 | LAID | moves: pointer edit |
| `incoming/v380L/Gathered_Value_1.md` | 6 | LAID | moves: pointer edit |
| `archive/session_v380/v380L/Incoherings_For_The_Subject.md` | 1 | LAID | moves: pointer edit |
| `incoming/v380L/Progress.md` | 42 | LAID | moves: pointer edit |
| `incoming/v380L/Registry_Negations_Sorted.md` | 1 | OPEN | stays |
| `archive/session_v380/v380L/The_Claim_Broken_Further.md` | 2 | LAID | moves: pointer edit |
| `incoming/v380L/closing_drafts/` | 2 | folder | stays |
| `incoming/v380L/closing_drafts/Natural_Intelligence_Fifty-Four_Read_By_Hand.md` | 1 | OPEN | stays |
| `incoming/v380L/closing_drafts/Registry_Cause_And_Twins.md` | 1 | OPEN | stays |
| `incoming/v380L/closing_drafts/Registry_Negations_At_The_Purpose.md` | 1 | OPEN | stays |
| `incoming/v380L/closing_drafts/Round_At_Four_Parities_Deriving.md` | 1 | OPEN | stays |
| `incoming/v380L/readings/` | 1 | folder | moves: pointer edit |
| `incoming/v380R/` | 3 | folder | moves: pointer edit |
| `archive/session_v380/v380R/Concerns_Of_The_Three_Workings.md` | 2 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Exhibit_ONE_First_Motion_Draft.md` | 1 | DONE | moves: pointer edit |
| `archive/session_v380/v380R/Exhibit_ONE_Improving.md` | 6 | LAID | moves: pointer edit |
| `incoming/v380R/For_The_Workings.md` | 13 | LAID | stays |
| `incoming/v380R/Natural_Naming_Conferring.md` | 1 | OPEN | stays |
| `incoming/v380R/Natural_Naming_Gathering.md` | 2 | OPEN | stays |
| `incoming/v380R/Natural_Naming_Negations_Yet.md` | 3 | OPEN | stays |
| `incoming/v380R/Natural_Naming_Part_Four_Released.md` | 1 | DONE | moves: pointer edit |
| `incoming/v380R/Natural_Networking_From_v380A.md` | 8 | OPEN | stays |
| `archive/session_v380/v380R/One_Self_Followed.md` | 1 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Premise_Alternating_Followed.md` | 4 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Progress.md` | 3 | LAID | moves: pointer edit |
| `incoming/v380R/README.md` | 5 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Rigor_A_Fresh_Reading_And_Three_Workings.md` | 9 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/The_Claim_Broken.md` | 3 | LAID | moves: pointer edit |
| `incoming/v380R/The_Universal_Claim.md` | 5 | OPEN | stays |
| `archive/session_v380/v380R/The_Universal_Claim_Gathered.md` | 3 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Three_Workings_Combined.md` | 3 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Tour_A_Living_Self_Is_A_Carrying.md` | 26 | LAID | moves: pointer edit |
| `archive/session_v380/v380R/Two_Parities_Gathered_And_Worked.md` | 5 | LAID | moves: pointer edit |
| **Total** | **255** | | 53 stay, **202 to edit** |

## Part 3. Each carrying

Entries are paragraphs opening with a bold lead. "Open" is an entry led Ready, Concern, Incoming, Arrived, Opportunity, Marking or The hardest and not closed by its own lead. "Next/plan" is the file's next motion or a plan paragraph. "History" is an entry whose lead says it is met, received and met, withdrawn or already carried, or whose sentences are mostly reports of things entered. "History words" counts the words of sentences, inside any entry, that report a thing entered, mended, withdrawn, merged or met: narrative the Session Record holds or should hold. The split is by lead and wording, not by re-verifying each entry against its living file.

| Carrying | Entries | Open | Next/plan | History entries | History words / entry words | Entries naming `incoming/v380…` |
|---|---|---|---|---|---|---|
| `carry/Exhibit_ONE_Natural_Resolver.md` | 95 | 89 | 2 | 4 | 488 / 18,312 | 63 |
| `carry/Exhibit_THIRTY_Co-Chaining_Logic_Registry.md` | 21 | 18 | 2 | 1 | 424 / 3,817 | 15 |
| `carry/Natural_Intelligence.md` | 44 | 40 | 3 | 1 | 321 / 6,510 | 14 |
| `carry/Exhibit_TWENTY-FOUR_Geodesic_Improving_Method.md` | 36 | 33 | 0 | 3 | 302 / 5,294 | 12 |
| `carry/Exhibit_TWENTY_Natural_Naming.md` | 77 | 69 | 6 | 2 | 249 / 10,567 | 29 |
| `carry/Exhibit_THREE_Natural_Numbers.md` | 11 | 9 | 1 | 1 | 157 / 984 | 4 |
| `carry/Exhibit_SEVENTEEN_Natural_Biology.md` | 26 | 24 | 1 | 1 | 149 / 4,499 | 2 |
| `carry/Exhibit_TWENTY-EIGHT_Equilibria_Registry.md` | 25 | 23 | 1 | 1 | 140 / 5,076 | 2 |
| `carry/Exhibit_FOUR_Natural_Mathematics.md` | 7 | 5 | 0 | 2 | 122 / 767 | 2 |
| `carry/Exhibit_EIGHTEEN_Natural_Physics.md` | 46 | 38 | 5 | 3 | 115 / 8,197 | 2 |
| `carry/Exhibit_TWENTY-SIX_Living_File_Registry.md` | 17 | 16 | 1 | 0 | 86 / 2,109 | 4 |
| `carry/Exhibit_TWO_Natural_Networking.md` | 29 | 26 | 2 | 1 | 85 / 4,682 | 17 |
| `carry/Exhibit_FIVE_Natural_Engineering.md` | 12 | 11 | 1 | 0 | 78 / 1,950 | 0 |
| `carry/Exhibit_SEVEN_Natural_Societies.md` | 10 | 8 | 1 | 1 | 73 / 1,774 | 1 |
| `carry/Exhibit_ELEVEN_Natural_Medicine.md` | 9 | 8 | 1 | 0 | 69 / 1,745 | 1 |
| `carry/Exhibit_SIXTEEN_Natural_Chemistry.md` | 9 | 8 | 1 | 0 | 64 / 1,213 | 0 |
| `carry/Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry.md` | 21 | 19 | 1 | 1 | 60 / 3,291 | 0 |
| `carry/Exhibit_TWENTY-SEVEN_Living_Ghost_Registry.md` | 12 | 10 | 1 | 1 | 56 / 1,050 | 0 |
| `carry/Exhibit_TWENTY-NINE_Natural_Illustrating.md` | 13 | 12 | 1 | 0 | 53 / 1,574 | 6 |
| `carry/Exhibit_THIRTEEN_Resolving_Hard_Problems.md` | 11 | 9 | 1 | 1 | 40 / 1,087 | 2 |
| `carry/Exhibit_NINETEEN_Natural_Philosophy.md` | 4 | 3 | 1 | 0 | 34 / 307 | 0 |
| `carry/Exhibit_TWENTY-FIVE_Living_Society_Registry.md` | 4 | 3 | 1 | 0 | 33 / 449 | 0 |
| `carry/Exhibit_FIFTEEN_Natural_Emanating.md` | 5 | 4 | 1 | 0 | 30 / 541 | 0 |
| `carry/Exhibit_TWELVE_Natural_Explaining.md` | 10 | 9 | 1 | 0 | 20 / 801 | 1 |
| `carry/Exhibit_NINE_Natural_Human_Society.md` | 2 | 1 | 1 | 0 | 13 / 147 | 0 |
| `carry/Exhibit_EIGHT_Natural_Exploring.md` | 3 | 2 | 1 | 0 | 11 / 190 | 0 |
| `carry/Exhibit_FOURTEEN_Natural_Destinies.md` | 2 | 1 | 1 | 0 | 11 / 84 | 0 |
| `carry/Exhibit_SIX_Natural_Transmissioning.md` | 3 | 2 | 1 | 0 | 11 / 223 | 0 |
| `carry/Exhibit_TEN_Natural_Health.md` | 4 | 3 | 1 | 0 | 11 / 325 | 1 |
| `carry/Exhibit_TWENTY-ONE_Hard_Problem_Registry.md` | 9 | 8 | 1 | 0 | 11 / 1,611 | 0 |
| `carry/Exhibit_TWENTY-THREE_Natural_Values.md` | 3 | 2 | 1 | 0 | 11 / 195 | 0 |
| `carry/Natural_Intelligence_Corus.md` | 5 | 4 | 1 | 0 | 11 / 403 | 0 |
| **Total (32 carryings)** | **585** | **517** | **44** | **24** | 3,338 / 89,774 | 178 |

### Part 3 notes

**The three carryings with the most history.**

1. **`carry/Exhibit_ONE_Natural_Resolver.md`** (95 entries, 18,312 words). The wording measure understates it. The working v380L read each of its then ninety entries beside the file by hand (`archive/session_v380/v380L/Carrying_Of_Exhibit_ONE_Sorted.md`, laid at this carrying's line 43): twelve entered, sixteen withdrawn by a later entry, two said of things the file has released, forty-two entered in part, eighteen open. Only three were released since (`archive/carrying_v380L/Exhibit_ONE_Natural_Resolver.md`, 794 words). So about 27 to 30 entries are history now and 42 more carry an entered part beside an open part. `archive/session_v380/v380L/Dissolving_Offered.md` lists the twenty-seven by their opening words.
2. **`carry/Exhibit_THIRTY_Co-Chaining_Logic_Registry.md`** (21 entries). Already dissolved once at v380L (35 entries at `archive/carrying_v380L/`). What remains as history is narrative inside its Ready entries: "this file at v380L … Entered: …" at lines 15 to 23, about 424 words reporting what v380L entered.
3. **`carry/Natural_Intelligence.md`** (44 entries). Also dissolved at v380L (19 entries archived). Line 30 is a 301-word account of what was entered; lines 80 and 94 report breaks withdrawn.

Next after these: `carry/Exhibit_TWENTY-FOUR_Geodesic_Improving_Method.md` (a withdrawn finding at line 78 beside the Ready it withdraws at line 25), `carry/Exhibit_TWENTY_Natural_Naming.md` (77 entries, never sorted by hand; a withdrawn entry at 146; the conferring decided ten namings whose entries are still listed), and `carry/Exhibit_EIGHTEEN_Natural_Physics.md` (46 entries, 31 of them above the `## Ready` heading: the v377 passes, "Arrived, at v377" and "Met at the observing, v376" paragraphs).

**Not verified here.** No carrying other than the three v380L sorted has been read entry by entry against its living file. The 517 "open" count is by lead only.

## Part 4. `carry/Living_Improving_Value.md`, paragraph by paragraph

19 bold-lead paragraphs, 4,263 words. Checked against `carry/Session_Record.md` by phrase: only the paragraph on the concerns of v379 is already there. The others marked history are in no record, so they are moved, not deleted.

| Line | Paragraph (lead) | Words | Standing | Filing |
|---|---|---|---|---|
| 5 | The one carry: at each living file its own carrying… | 16 | Current: subtitle | Keep |
| 7 | This file. | 172 | Current standing: what the front and each carrying hold | Keep |
| 9 | The set now, at v380, at the main line. | 135 | Current in kind, stale in fact: says three workings improving, v380L at 642 sentences in 39 groups (it closed at 661 in 42), v380A at Natural Illustrating, v380G working | Re-say at the close; the paragraph as it is goes to the record |
| 11 | Progress at v380R. | 194 | History: what was decided and entered at v380R | To the Session Record (not there now) |
| 13 | Opportunities, each its own motion. | 122 | Current opportunities; names `Natural_Naming_Negations_Yet.md` and `The_Universal_Claim.md` | Keep |
| 15 | Concerns open, each two sayings parting… | 119 | Current concerns | Keep |
| 17 | The set now, at v379. | 298 | History of v379 | To the Session Record or `archive/` (not in either now) |
| 19 | The emanating of Exhibit ONE at v379 into each living file… | 307 | History, with one open remainder: files still at older names (Natural Networking 173 places, Resolving the Hard Problem Registry 812, Natural Societies 3, Natural Illustrating 33), each said to have its map at its own carrying | Move; first confirm each map is at its carrying |
| 21 | Carried to the next session, each at its own carrying. | 286 | History of v379's close; duplicates concerns that are at the carryings | Move |
| 23 | The workings at v380, beside each other, and the one way each value is carried. | 516 | Mixed. The "one way" sentences repeat line 35; the rest is the state of three workings now ended | Move; nothing unique stays |
| 25 | Exhibit ONE at v380, and the two workings continuing. | 175 | History, with a "Next at Exhibit ONE" list of five things | Move; confirm the five are at Exhibit ONE's carrying |
| 27 | Learned at v380, at the three workings… | 264 | History; its learnings are Ready at the Geodesic Improving Method's carrying (line 25, one sentence withdrawn at line 78) | Move |
| 29 | The concerns of v379 in their order… | 392 | Ordering of concerns, written at v379's close; already in the Session Record and in `archive/session_v379_exhibit_one_first/Session_Report_v379.md` | Remove from the front; if the order still guides, keep one line |
| 31 | Learned at v379, for the next session's helpers. | 399 | History; its findings are Ready at the Geodesic Improving Method's carrying (line 21) | Move |
| 33 | The set at v378. | 181 | History, with two standing sentences (no plan across files; a file's carrying says its own next) | Move; the two sentences are already said at line 7 |
| 35–38 | Arriving, improving, living: the one way into a living file (and its three numbered steps) | ~380 | Current standing: the method of receiving | Keep |
| 40 | The method at every file, one motion at a time. | 204 | Current standing | Keep |
| 42 | The carrying system, the method at the scale of sessions. | 49 | Current standing | Keep |
| 44 | Three loops, run by sessions together and by no one session. | 120 | Current standing; the same paragraph is at the root `README.md` line 41 | Keep, or keep at one place |

Summary: 8 paragraphs current (about 1,180 words with the numbered steps), 1 to re-say (135), 9 history (about 2,810 words, two thirds of the file). Five of the front's path mentions of the four folders sit in the history paragraphs at lines 23, 25 and 27.

## Part 5. Recommended filing

**Destination.** One folder, `archive/session_v380/`, holding `v380A/`, `v380G/`, `v380L/` and `v380R/` with their inner structure as it is, so every moved pointer changes by one prefix: `incoming/v380X/` to `archive/session_v380/v380X/`.

### 5a. What moves now and what stays

| Folder | Moves to `archive/` now | Stays in `incoming/` | Why it stays |
|---|---|---|---|
| `v380G/` | All 6 files | Nothing | One LAID front and five records; two carry entries and the Living File Registry's row point at its README |
| `v380A/` | 64 files: the 39 under `reviews/`, `living_ai_link/`, the 24 top-level files other than the three below (reports, offerings, returned JSON readings, the duplicate `…_working.md`) | 77 files: `Exhibit_TWO_Natural_Networking_candidate.md` with `Candidate_Manifest.json` and `Candidate_Changes.patch`; `illustrating/` whole (9); `kit/` whole (65) | The candidate is OPEN. `illustrating/` holds an OPEN reading and two instruments, and ten links from five sums-covered kit files point into it. `kit/` holds six instruments found nowhere else and its `SHA256SUMS` lists all 64 of its files |
| `v380L/` | 40 files: 28 LAID sources (`Progress.md`, `README.md`, `For_The_Managing.md`, the readings, the sorted carryings, the gathered value) and 12 records (`derivings/*.md`, the transcript, the earlier papers, `instruments_returned.txt`) | 7 files: `closing_drafts/` (4), `Registry_Negations_Sorted.md`, `instruments.py`, `derivings/torus_rule_arithmetic.py` | Four drafts entered at no file, one list a file's next names, two instruments |
| `v380R/` | 17 files: 12 LAID sources and 5 records | 10 files: the 9 OPEN (`The_Universal_Claim.md`, `Natural_Naming_Gathering.md`, `Natural_Naming_Conferring.md`, `Natural_Naming_Negations_Yet.md`, `Natural_Networking_From_v380A.md`, and the four unlaid Natural Naming readings) and `For_The_Workings.md` | The OPEN bodies; `For_The_Workings.md` is LAID but a sums-covered kit file names it, and keeping it avoids renewing sums |
| **Total** | **127 files** | **94 files** | |

### 5b. The smallest set of pointer edits

| Where | Edits | Kind |
|---|---|---|
| 18 files in `carry/` (Exhibit ONE 65, Natural Naming 27, Natural Networking 16, the Registry 15, Geodesic Improving Method 12, Natural Intelligence 12, the front 10, Session Record 9, Natural Illustrating 6, Living File Registry 5, and eight with 1 to 3) | 194 | Prefix replacement on each moved target; folder-level pointers `incoming/v380A/` (21), `incoming/v380L/` (12), `incoming/v380R/` (3) and `incoming/v380L/readings/` (1) are among them |
| `Exhibit_TWENTY-SIX_Living_File_Registry_v380R.md`, table of workings, lines 127 to 131 | 7 | A living file: one motion, re-saying each working's row and its folder's new place |
| `incoming/README.md` | 8 relative links of 12 (6 would break; 2 folder links still resolve and are re-said), and the standing of the rows | The rows for `v380G/`, `v380A/`, `v380L/`; the four links into `v380A/illustrating/` and `v380R/The_Universal_Claim.md` stay as they are |
| `incoming/natural_networking_2026-10-01/README.md` | 1 path and 4 relative links | All to `v380A/` files that move |
| Kits | 0 | Under this filing no sums-covered file changes and no `SHA256SUMS` is renewed |
| **Total** | **214 edits in 21 files** | 202 path mentions, 12 relative links |

53 path mentions and 4 relative links need no edit because their targets stay.

### 5c. Risks

| # | Risk | What it affects | Suggested handling |
|---|---|---|---|
| 1 | Splitting a folder breaks relative links between the part that moves and the part that stays: 30 markdown links (16 in `v380A/`, 14 in `v380R/`), listed below | Moved records such as `v380A/Manager_Handoff.md`, `README.md`, `Session_Report.md` linking the candidate and `kit/`; staying `v380R/For_The_Workings.md` linking moved siblings and the reverse | Either edit these 30 as well, or accept them in records filed "as they arrived" and say so at the archive folder's front. They are outside the 214 |
| 2 | Four OPEN files in `v380R/` are laid at no carrying: `Natural_Naming_Beside_Receiving_Exhibits.md`, `Natural_Naming_Each_Section_Read.md`, `Natural_Naming_Second_Reading.md`, `Natural_Naming_Value_Sorted.md` | Their findings (55 things said only in Natural Naming, 48 sections adding little, one section that may leave) would be lost to a reader of the carryings if archived | Lay one entry at Natural Naming's carrying before any of them moves |
| 3 | `v380L/Carrying_Of_Exhibit_ONE_Sorted.md`, `Carrying_Of_Natural_Intelligence_Sorted.md` and `Dissolving_Offered.md` are classed LAID but are the working lists for dissolving Exhibit ONE's carrying | Part 3's largest history | Dissolve that carrying from them first, or leave these three in `incoming/` until it is done (5 fewer edits) |
| 4 | The front's history paragraphs are in no record | About 2,810 words at `carry/Living_Improving_Value.md` | Append to the Session Record or file whole at `archive/session_v380/` before removing; do not delete |
| 5 | `v380A/kit` scripts do not run as they stand: they open `Exhibit_ONE_Natural_Resolver_v379.md`, which is not at the root or in `archive/`, and find the root by `parents[3]`, which a deeper folder breaks | The five construction scripts | Keep `kit/` where it is. If the new Exhibit TWO is to start from "a kit of no executing", archiving `kit/` whole is a decision for the managing working, not a filing step |
| 6 | Instruments carry their own path in their docstring ("python3 incoming/v380L/instruments.py") and `v380L/instruments.py` globs the root for the newest Exhibit ONE | The two v380L and two v380A illustrating scripts | They stay, so nothing changes; a later move needs the docstring and the README mentions re-said |
| 7 | `v380A/Candidate_Manifest.json` stores `archive/session_v380/v380A/Prior_Passages.md` as data; `Prior_Passages.md` moves | The manifest's second path | Keep `Prior_Passages.md` beside the candidate (one more file stays), or accept the stale path in a record |
| 8 | Editing the Living File Registry is a motion of a living file | Version line, fresh reader, `check_set.py` | Its carrying's next already names this ("Part One's archive standings at this session's releases"); do the seven edits inside that motion |
| 9 | 8 files already in `archive/` point into these folders (`archive/carrying_v380L/*`, `archive/Natural_Naming_v380R_Part_Four_before_reducing.md`) | Their pointers break at the move | Outside the stated scope; either accept in archived records or include in the prefix replacement |
| 10 | `Session_Record.md` holds 9 mentions of the moved files in paragraphs that "stand as they stood" | The record's own convention | Updating a path is not changing a record's saying; if the convention forbids it, add one line at the record naming the new prefix |
| 11 | Branches `working/v380L`, `working/v380A`, `working/illustrating-v380A` and any open pull request still hold these paths | A later merge would re-create `incoming/v380X/` files | Confirm the three workings are merged and closed before the move |
| 12 | `v380R` is the working doing the closing; its `Progress.md` and `README.md` are still being written | Moving them before the last commit | Move `v380R/` last, in the closing commit |
| 13 | `…_working.md` and `…_candidate.md` are byte-identical (24,225 words each) | Nothing breaks | The working copy moves; the candidate stays |

### 5d. The 30 relative links a split would break

| File | Link target | Direction |
|---|---|---|
| `archive/session_v380/v380A/Manager_Handoff.md` | `Exhibit_TWO_Natural_Networking_candidate.md` | moves, links to a staying file |
| `archive/session_v380/v380A/Manager_Handoff.md` | `Candidate_Manifest.json` | moves, links to a staying file |
| `archive/session_v380/v380A/Manager_Handoff.md` | `Candidate_Changes.patch` | moves, links to a staying file |
| `archive/session_v380/v380A/Progress.md` | `Exhibit_TWO_Natural_Networking_candidate.md` | moves, links to a staying file |
| `archive/session_v380/v380A/Progress.md` | `kit/README.md` | moves, links to a staying file |
| `incoming/v380A/README.md` | `illustrating/README.md` | moves, links to a staying file |
| `incoming/v380A/README.md` | `illustrating/Concept_And_Consistency.md` | moves, links to a staying file |
| `incoming/v380A/README.md` | `Exhibit_TWO_Natural_Networking_candidate.md` | moves, links to a staying file |
| `incoming/v380A/README.md` | `kit/README.md` | moves, links to a staying file |
| `incoming/v380A/README.md` | `kit/README.md` | moves, links to a staying file |
| `archive/session_v380/v380A/Session_Report.md` | `Exhibit_TWO_Natural_Networking_candidate.md` | moves, links to a staying file |
| `archive/session_v380/v380A/Session_Report.md` | `kit/INSTRUMENT_STANDING.md` | moves, links to a staying file |
| `incoming/v380A/illustrating/Progress.md` | `../living_ai_link/README.md` | stays, links to a moved file |
| `incoming/v380A/kit/README.md` | `../Improving_Passes.md` | stays, links to a moved file |
| `incoming/v380A/kit/README.md` | `../Session_Report.md` | stays, links to a moved file |
| `incoming/v380A/kit/README.md` | `../Participating_Pair.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `The_Claim_To_Break.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `The_Claim_Broken.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `The_Universal_Claim_Gathered.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `../v380G/README.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `../v380G/Prompts_For_v380G.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `Natural_Naming_Negations_Sorted.md` | stays, links to a moved file |
| `incoming/v380R/For_The_Workings.md` | `Natural_Naming_Part_Four_Released.md` | stays, links to a moved file |
| `archive/session_v380/v380R/Progress.md` | `Natural_Networking_From_v380A.md` | moves, links to a staying file |
| `archive/session_v380/v380R/Progress.md` | `For_The_Workings.md` | moves, links to a staying file |
| `archive/session_v380/v380R/Progress.md` | `For_The_Workings.md` | moves, links to a staying file |
| `archive/session_v380/v380R/Progress.md` | `For_The_Workings.md` | moves, links to a staying file |
| `archive/session_v380/v380R/Progress.md` | `For_The_Workings.md` | moves, links to a staying file |
| `archive/session_v380/v380R/Progress.md` | `For_The_Workings.md` | moves, links to a staying file |
| `archive/session_v380/v380R/Two_Parities_Gathered_And_Worked.md` | `For_The_Workings.md` | moves, links to a staying file |
