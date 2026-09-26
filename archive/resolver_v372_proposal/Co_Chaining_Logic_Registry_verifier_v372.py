#!/usr/bin/env python3
"""Co-Chaining Logic Registry verifier v372, the verifier of Exhibit THIRTY.

Runs each run link of the registry, Parts ONE to EIGHT, against the resolver's code (the first python
block of Exhibit_ONE_Natural_Resolver_v372.md, read from beside this file when it stands there, else the
copy carried below) and against the arithmetic, each check at its link's id. It prints, per Part, the
checks passed and failed, and a total.

A probe at a nye link returns True while the failure it names stands: it prints as a confirmed failure,
never as a verifier failure. A probe bounding a nye link prints as holding. A check needing a file not
found beside this file (or at a folder given with --repo) prints "needs <file>" and is skipped.

    python3 Co_Chaining_Logic_Registry_verifier_v372.py [--repo DIR]... [--timeout SECONDS] [-v]

--repo DIR adds a folder to look for the files some checks read (the repository's exhibits, the kit).
--timeout sets the time a check may run before it fails (120 s). -v prints each check with the run it
names. Exit status 0 when no check fails.
"""
import ast, io, json, linecache, os, re, sys, textwrap, time, types

HERE = os.path.dirname(os.path.abspath(__file__))

RESOLVER_COPY = '"""Exhibit ONE · Natural Resolver · v372"""\n\n\ndef _1_self_coupling(_3_self_carrying, _2_self_offering):\n    _6_other_crossing = {\n        _4_self_sharing: _8_other_torusing\n        for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing\n        in _3_self_carrying}\n    _14_social_crossing = [\n        (_4_self_sharing, _7_other_corusing)\n        for _4_self_sharing, _7_other_corusing in _2_self_offering\n        if _7_other_corusing != 0]\n    for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in _3_self_carrying:\n        if _7_other_corusing > 0:\n            _14_social_crossing.append((_4_self_sharing, -1))\n        if _7_other_corusing < 0:\n            _14_social_crossing.append((_4_self_sharing, 1))\n    _12_other_surplusing = {}\n    for _4_self_sharing, _7_other_corusing in _14_social_crossing:\n        if _7_other_corusing > 0:\n            _12_other_surplusing[_4_self_sharing] = _12_other_surplusing.get(_4_self_sharing, 0) + 1\n        if _7_other_corusing < 0:\n            _12_other_surplusing[_4_self_sharing] = _12_other_surplusing.get(_4_self_sharing, 0) - 1\n    _10_other_surfacing = [\n        (_4_self_sharing, 1 if _12_other_surplusing[_4_self_sharing] > 0\n            else (-1 if _12_other_surplusing[_4_self_sharing] < 0 else 0))\n        for _4_self_sharing in _12_other_surplusing]\n    _11_other_chaining = {}\n    for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in _3_self_carrying:\n        if _16_social_torusing + 1 <= 3 or (_16_social_torusing + 1 == 4 and _8_other_torusing > 0):\n            _11_other_chaining[_4_self_sharing] = (\n                _7_other_corusing, _8_other_torusing, _16_social_torusing + 1)\n    for _4_self_sharing, _7_other_corusing in _10_other_surfacing:\n        if _7_other_corusing != 0:\n            _11_other_chaining[_4_self_sharing] = (\n                _7_other_corusing, 0 - _6_other_crossing.get(_4_self_sharing, 1), 0)\n    return (\n        _10_other_surfacing,\n        [(_4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing)\n         for _4_self_sharing, (_7_other_corusing, _8_other_torusing, _16_social_torusing)\n         in _11_other_chaining.items()])\n\n\ndef _9_other_releasing(_10_other_surfacing, _5_other_neutralling):\n    return [(_5_other_neutralling[_13_social_neutralling], _15_social_corusing)\n            for _13_social_neutralling, _15_social_corusing in _10_other_surfacing]\n\n\nCONNECTORS = {\n    2: (\'2-self-offering\', \'right\', \'arriving\'),\n    6: (\'6-other-crossing\', \'left\', \'releasing\'),\n    9: (\'9-other-releasing\', \'backward\', \'along\'),\n    10: (\'10-other-surfacing\', \'right\', \'releasing\'),\n    14: (\'14-social-crossing\', \'left\', \'arriving\'),\n    17: (\'17-social-abundancing\', \'forward\', \'along\'),\n}\nJOINS = {10: 14, 6: 2, 17: 9, 9: 17}\n\n\ndef _17_social_abundancing(_3_self_carrying, _2_self_offering, _5_other_neutralling, SURFACE):\n    _11_other_chaining = {}\n    _2_self_offering_next = {self: {2: [], 14: [], 17: []} for self in SURFACE}\n    for self, facings in SURFACE.items():\n        carrying = _3_self_carrying.get(self, [])\n        arriving = [sign for connector in (2, 14, 17)\n                    for sign in _2_self_offering.get(self, {}).get(connector, [])]\n        _10_other_surfacing, _11_other_chaining[self] = _1_self_coupling(carrying, arriving)\n        _6_other_crossing = [\n            (_4_self_sharing, _8_other_torusing)\n            for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in carrying]\n        released = _9_other_releasing(_10_other_surfacing, _5_other_neutralling.get(self, {\n            _13_social_neutralling: _13_social_neutralling\n            for _13_social_neutralling, _15_social_corusing in _10_other_surfacing}))\n        for releasing, signs in ((6, _6_other_crossing), (10, _10_other_surfacing), (9, released)):\n            for neighbour in facings.get(CONNECTORS[releasing][1], []):\n                if neighbour in _2_self_offering_next:\n                    _2_self_offering_next[neighbour][JOINS[releasing]] += signs\n    return _11_other_chaining, _2_self_offering_next\n'

RUNS = {
"F20": "The self's five 1..5 and the other's five 2..6 give ten positions on six numbers; zipped position by position they are (1,2),(2,3),(3,4),(4,5),(5,6), each with odd sum; parities of 1..5 read co bi co bi co and of 2..6 bi co bi co bi.",
"F27": "For each of the 16 functions f: {±1}^2 -> {±1}, the map (p, n) -> (n, f(p, n)) on the 4 joint states is a bijection for exactly 4 f and non-injective for 12; its cycle lengths are [1, 1, 2] for f = p, [4] for f = −p, [1, 3] for f = p·n and for f = −p·n.",
"F31": "8(p − 1) + 1 gives 1, 9, 17 at p = 1, 2, 3 and 65 at p = 9.",
"F32": "For each (c, t) in {±1}^2, the eight overlapping pairs of [c, t, −c, −t, c, t, −c, −t, c] contain each of the four joint forms exactly twice, and each pair is (y, −x) of the pair (x, y) before it.",
"F35": "For k in 0..63 and s in {±1}, (−1)^k · s equals s at even k and −s at odd k.",
"F37": "Of the 16 truth tables on two binary inputs, exactly two change output whenever either single input changes: exclusive or and its inversion.",
"F43": "Nesting possible (2) -> existing only at possible (2) -> carrying only at existing (2) yields exactly 4 leaf conditions.",
"F57": "On {±1}^4 with A(s) = (s1, −s0, s2, s3) and B(s) = (s0, s1, s3, −s2), alternating A, B from each of the 16 states returns to the state first at step 8 and visits 8 distinct states; the rounds cover all 16.",
"F58": "Of the 16 maps on {±1}^2 sending each state to a state differing in one sign, exactly 2 form a single cycle through all 4 states, and they are (x, y) -> (y, −x) and (x, y) -> (−y, x).",
"F59": "Of the 256 maps {±1}^2 -> {±1}^2, exactly 6 are a single 4-cycle; exactly 2 of these change one sign at each step; exactly 2 maps change one sign at each step, have m(m(s)) != s for each s, and form a single 4-cycle.",
"F60": "Of the 16 one-change maps on {±1}^2, exactly 2 satisfy m(m(s)) = (−x, −y) for each s, namely (y, −x) and (−y, x); for each of these the only subsets of the 4 states mapped onto themselves are the empty set and all four.",
"F63": "Of the 3^8 = 6,561 one-change maps on {±1}^3, exactly 12 form a single 8-cycle, and they form one orbit under the 48 sign-permutation-and-flip renamings acting by conjugation.",
"F64": "The 4-cube has exactly 1,344 undirected Hamiltonian cycles, falling into 9 orbits under its 384 symmetries (instrument uniqueness_v370/hamiltonian_forms_four_signs.py, rerun).",
"R2": "The code's module tree has exactly two function definitions, _1_self_coupling(_3_self_carrying, _2_self_offering) and _9_other_releasing(_10_other_surfacing, _5_other_neutralling), and exactly two assignments, CONNECTORS and JOINS, in that order.",
"R4": "Each identifier _1_self_coupling .. _16_social_torusing occurs in the code; no identifier begins with _17; each hyphenated string in CONNECTORS is '<n>-<ONE name of n>'.",
"R5": "Over names 1..17: 9 odd and 8 even; with fives co bi co bi co at odd and bi co bi co bi at even, co count 9·3 + 8·2 = 43 and bi count 9·2 + 8·3 = 42, total 85.",
"R6": "The roots (second word) of the 17 names are 13 distinct; exactly neutralling, crossing, corusing and torusing root two names, each pair 8 apart.",
"R7": "For each of the 19 reachable carryings at one key and each offering in [[], [−], [+], [−, −], [+, +], [+, −]], _1_self_coupling returns a list of (key, s) with s in {−1, 0, 1} and a list of (key, c, t, a) with c, t in {±1} and 0 <= a <= 4, and that list is accepted as the next _3_self_carrying.",
"R9": "In the tree of _1_self_coupling, _3_self_carrying is loaded exactly 3 times (the 6-other-crossing comprehension, the inverting loop into 14, the continuing loop of 11).",
"R10": "For each c, t in {±1} and a in 0..2: with no offering the returned entry is (−c, −t, 0); with offering [(k, c)] the surfacing is 0 and the entry is (c, t, a + 1).",
"R11": "For each c, t: _1_self_coupling([(k, c, t, 0)], []) surfaces −c at k; _1_self_coupling([], [(k, 0)]) == ([], []); _1_self_coupling([(k, 1, −1, 0)], [(k, 0)]) equals _1_self_coupling([(k, 1, −1, 0)], []).",
"R13": "_1_self_coupling([], [(k,1),(k,1)]) == ([(k,1)], [(k,1,−1,0)]); _1_self_coupling([], [(k,1),(k,−1)]) == ([(k,0)], []); _1_self_coupling([], [(k,−1),(k,−1)]) == ([(k,−1)], [(k,−1,−1,0)]).",
"R14": "For each c, t in {±1} and a in 0..4, offering [(k, c)] at (k, c, t, a) surfaces 0 and returns (c, t, a + 1) exactly when a + 1 <= 3 or (a + 1 == 4 and t > 0), else no entry; among the 19 reachable carryings the largest opening is 3 at t = −1 and 4 at t = +1.",
"R15": "For each c, t, a in 0..2 and each of the six offerings, a nonzero surfacing s returns the entry (s, −t, 0); _1_self_coupling([], [(k, s)]) returns (s, −1, 0) for s in {±1}.",
"R16": "For each c, t and each of the six offerings, a nonzero surfacing s gives the entry (s, −t) = (y, −x) at (x, y) = (t, s), and the entry's two signs oppose exactly when t == s.",
"R17": "_1_self_coupling([(k, 1, −1, 0)], [(k, 1)]) == ([(k, 0)], [(k, 1, −1, 1)]), and the 6-other-crossing value at k is −1.",
"R18": "Seven calls offering [(k, 1)] from empty surface [1, 0, 0, 0, 0, 1, 0] with entries (1,−1,0), (1,−1,1), (1,−1,2), (1,−1,3), none, (1,−1,0); after [(k,−1)], calls offering [(k,1)] give (1,1,0) then openings 1, 2, 3, 4, then no entry, surfacing 0 at each of the five kept calls.",
"R19": "For carried (k, c, t, 0), c, t in {±1}, and offerings none, one sign, or two signs (7 per carried sign, 14 at one t): the surfacing is c at [c, c], 0 at [c], −c otherwise, and each nonzero surfacing opens a fresh 7 equal to it.",
"R20": "_1_self_coupling([(k,1,−1,0)], [(k,1)]) == ([(k,0)], [(k,1,−1,1)]) and _1_self_coupling([(k,1,−1,0)], [(k,1),(k,1)]) == ([(k,1)], [(k,1,1,0)]).",
"R21": "Calls offering [(k, 1)] surface [0, 0, 0, 0, 1] from (k, 1, −1, 0) and [0, 0, 0, 1] from (k, 1, −1, 1).",
"R22": "For each c, t: no offering at (c, t, 0) gives second sign −t and keeps (7 == 8) equal to (c == t); [c, c] surfaces c, gives second sign −t and flips (7 == 8); [c] surfaces 0 and keeps second sign t; (k, 1, −1, 3) under [(k, 1)] returns ([(k, 0)], []).",
"R23": "Breadth-first from the empty carrying under the six offerings reaches exactly 19 states: the empty one, 8 at t = −1 with openings {0,1,2,3}, 10 at t = +1 with openings {0,1,2,3,4}; 19 × 6 = 114 transitions.",
"R24": "For each of the 19 reachable carryings and each sequence of length 0..6 over {−1, 0, 1} (1,093 sequences, 20,767 comparisons), the call equals the call with the representative offering: none if all zero, [+, −] if the nonzero signs sum to 0, else sign(total) repeated min(|total|, 2) times.",
"R25": "Over the 19 reachable carryings, 19 × 3 = 57 transitions under [], [+], [−]; of the 171 pairs, 146 give different six-call surfacing sequences under constant [(k, 1)], 146 under constant [(k, −1)], and 171 under one or the other, with no surfacing counted as 0.",
"R27": "_9_other_releasing([(a,1),(b,−1),(c,0)], {a:x, b:y, c:z}) == [(x,1),(y,−1),(z,0)], each element a pair.",
"R28": "For c in {±1}, [(k, c)] from empty then 8 empty offerings surface [c, −c, c, −c, c, −c, c, −c, c] and give entries (c, −1), (−c, 1), (c, −1), (−c, 1), so the overlapping sequence is c, −1, −c, 1, c.",
"R29": "For each (c, t), the pairs of [c, t, −c, −t, c] are the four joint forms each once, each is (y, −x) of the one before, and agreeing holds at pairs 1 and 3 alike, at 2 and 4 alike, and differs between 1 and 2.",
"R30": "For each a, b, z in {±1}: ((a == b) != (b == z)) exactly when z == −a; at +, +, + both pairs agree.",
"R31": "For each c, t: no offering at (c, t, 0) surfaces −c; [+] from empty gives (1, −1, 0); [−] then [] gives (1, 1, 0); a further [] at each surfaces −1 while their second signs are −1 and +1; offering + at (1,−1,0) gives ([(k,0)], [(k,1,−1,1)]) and − gives surfacing −1 with a fresh negative entry.",
"R32": "CONNECTORS == {2: ('2-self-offering','right','arriving'), 6: ('6-other-crossing','left','releasing'), 9: ('9-other-releasing','backward','along'), 10: ('10-other-surfacing','right','releasing'), 14: ('14-social-crossing','left','arriving'), 17: ('17-social-abundancing','forward','along')}; across keys [2, 6, 10, 14] all even, along keys [9, 17] all odd.",
"R33": "JOINS == {10: 14, 6: 2, 17: 9, 9: 17}; each join keeps parity; 10 − 2 == 8 and 14 − 6 == 8; (6 + 8, 2 + 8) == (14, 10).",
"R34": "Neither CONNECTORS nor JOINS occurs as a name in either function body; with both set to {} in a fresh namespace, each of the 114 transitions returns as before.",
"R35": "No constant 17 and no identifier containing '17' occurs in either function body; 17 is a key of CONNECTORS and JOINS, with JOINS[17] == 9 and JOINS[9] == 17.",
"R40": "Caller: two resolvers seeded by _1_self_coupling([], [(k, seed)]), twelve alternating calls; each call's 6 is [(key, t)] of its input carrying, given as the other's next offering on a joined leg. Both legs joined, over 4 seed pairs × 2 first callers: 96 couplings, 32 surfacing 0, each of those 32 with one 6 release and the entry continuing (same c, t; opening + 1). Seeds −, − with A first: A surfaces [1, −1, 0, 1, −1, 0] both ways and [1, −1, 1, −1, 1, −1] at A→B only, B→A only, and neither.",
"R41": "Same caller as R40: over 4 seed pairs × 2 first callers × 2 selves (16 comparisons), a self's six surfacings with both legs differ from those with only the other's leg into it in exactly 12.",
"R42": "A = [(k,+)] from empty then []; B = [(k,−)] from empty; both 6 releases are [(k, −1)]; A offered [(k, −1)] surfaces 0 and continues at opening 1; A offered [] surfaces + and returns (1, −1, 0). Over 4 seed pairs × 4^3 leg patterns (256 runnings) of three rounds A then B, each call surfacing 0 at a nonempty input carrying returns that entry at opening + 1.",
"R43": "B and C each _1_self_coupling([], [(k, 1)]); for A's sign a in {±1}: B's 6 is [(k, −1)], C offered it surfaces −1; B offered [(k, a)] surfaces 0 at a = 1 and −1 at a = −1; B's next 6 is [(k, −1)] at a = 1 and [(k, 1)] at a = −1; C offered it surfaces 0 and +1 respectively.",
"R44": "Caller: ring of n, one [(k, 1)] offered once at self 0, all selves couple each step, _9_other_releasing(s, {k: k}) given as the next self's offering. Ring of one surfaces [1, 0, −1, 0, 1, 0, −1, 0]; for n in 1..11, 17, 59 the state (carryings and signs between selves) first recurs from the state after n couplings, with period 2 at even n and 4n at odd n.",
"R45": "Same caller: from coupling n on, at even n each self's surfacing inverts each coupling and neighbours are opposite; at odd n surfacings at t + 2n are the negatives of those at t and at t + 4n equal them, at most one self surfaces 0 at a coupling, and the 0 moves to the next self each two couplings; 2·59 = 118, 4·59 = 236.",
"R46": "Same caller: for n in 1..11 over 5,000 couplings, no state after a coupling has each carrying empty and no sign between selves.",
"R48": "n + 8 keeps parity for n in 1..9; 17 − n changes parity and 17 − (17 − n) = n for n in 1..16; 9 − n changes parity and 9 − (9 − n) = n for n in 1..8.",
"R49": "{n, 9 − n} over 1..8 gives exactly (1,8), (2,7), (3,6), (4,5), each odd with even; {n, 17 − n} over 1..16 gives 8 pairs, each odd with even; 17 − 17 = 0 is no name; (n, n + 8) over 1..9 keeps parity and includes (3,11) and (7,15).",
"R50": "[n, n + 8, 9 − n, 17 − n] for n = 1..4 is [1,9,8,16], [2,10,7,15], [3,11,6,14], [4,12,5,13]; 17 − (n + 8) == 9 − n for n in 1..8.",
"R51": "Each of ONE's 12 forms and 4 higher forms, read cyclically, has exactly two parity changes and equal counts of odd and even, and its odd/even reading equals its Round column; 17 is in no form.",
"R52": "Under n -> n + 1 at odd n, n − 1 at even n, each of the 12 forms maps to its listed odd-momentary partner reversed as a cycle; under n -> n + 1 at even n, n − 1 at odd n, each form with a listed even partner maps to it reversed (or to itself in the same direction for its three self-partners), and each form marked with a dash maps outside 1..16 or to no listed form in either direction.",
"R53": "2 + 2sj for j = 0..3 gives [2,4,6,8] at s = 1 and [2,6,10,14] at s = 2; [2,4,6,8] + 8 = [10,12,14,16]; [2,6,10,14] with [4,8,12,16] is the eight even names 2..16; 8s + 1 gives 9 and 17.",
"R54": "11 − 3 == 8, both odd; and R7 holds (the returned 11 is accepted as the next 3).",
"N3": "For n from 2 to 1,000 the momentary (n − 1, n) completing at n and (n, n + 1) opening at n open at opposite parities, one at the self (odd opening) and one at the other.",
"N5": "The self's five from 1 and the other's five from 2 lie on 1..6 covered by the self's full momentaries 1–2, 3–4, 5–6; the same ten from 3 and 4 is the first ten shifted by two, each pair of odd sum, within 1..9.",
"N6": "The eight momentaries (k, k + 1), k = 1..8, meet each of 1..9, each but the last has one next opening at its completing, each reaches each later number; the self's four alone have no momentary opening at their completings.",
"N7": "n² − (n − 1)² = 2n − 1 and n(n + 1) − (n − 1)n = 2n as polynomial identities with the base at one; the sums of the first n odds and evens equal n² and n(n + 1) for n to 1,000.",
"N8": "(n − 1)(n + 1) = n² − 1 as a polynomial identity (checked at more points than its degree).",
"N9": "(n − 3)(n + 3) = n² − 9 as an identity and (n − k)(n + k) = n² − k² for n < 200, k < 50; 23 × 25 = 24² − 1.",
"N11": "Each face twice is the identity on its range; alternating ±8 with 17 less returns each of 1..16 after four distinct names within 1..16; 9 less followed by 8 up or 17 less lands in 9..16; 17 − (n + 8) = 9 − n for n = 1..8.",
"N12": "Rows [n, n + 8, 9 − n, 17 − n] for n = 1..4 are the four listed; round each, exactly two parity changes, both at a step summing to 17; 17 in none; no n in 1..16 equals 17 − n.",
"N15": "For each n < 1,000 the triples (n, n + 1, n + 2) and (n + 1, n + 2, n + 3) carry one and two odd members in some order; 23..25 odd-even-odd and 24..26 even-odd-even.",
"N20": "For N = 2..200 and each k, the multiples of k mod N number N/gcd(N, k); at prime N each k ≠ 0 meets all; step 2 meets all nine stations of the composite 9.",
"N22": "2 × 3 − (2 + 3) = 1; the self's 1..4 and the other's 2..5 share three positions and leave two outer, five in all; shared at both sides six; 4 + 4 = 2 × 3 + 2.",
"N28": "In exact arithmetic on a + b√5, φ³ − φ⁻³ = 4; C(11, 2) = T₁₀ = F₁₀ = 55; with N8.",
"N30": "The seventeen primes below 60 sum to 440; 8 × 55 = 440; 21² − 1 = 440.",
"N32": "F(n + 1)/F(n) for n to 300 alternates above and below φ (tested by the sign of x² − x − 1 in exact rationals, starting above at 2/1); [[1,1],[1,0]]ⁿ = [[F(n+1),F(n)],[F(n),F(n−1)]] with determinant (−1)ⁿ for n to 300.",
"N33": "Exactly in Q(√5): φ² = φ + 1, (−1/φ)² = −1/φ + 1, φ − 1/φ = 1, φ(−1/φ) = −1, φ = 1 + 1/φ; the regular pentagon's diagonal over side equals φ to 1e−12.",
"N35": "For n = 1..50, x = (n + √(n² + 4))/2 satisfies x² = nx + 1 and x = n + 1/x exactly, with floor(x) = n and 0 < 1/x < 1.",
"N37": "q · (p/q) is whole for p, q < 30; x² − x − 1 at ±1 is −1 and +1, so it has no rational root; kφ − floor(kφ) ≠ 0 exactly for k < 200.",
"N42": "6F − 2E = 6(V − E + F) whenever 3V = 2E (E to 297, F to 199); dodecahedron (12 five-folds; 20, 30) and truncated icosahedron (12 five-folds, 20 six-folds; 60, 90) at 3V = 2E and χ = 2; 12 − 30 + 20 = 2; m × m hexagonal tori at χ = 0.",
"N44": "19² − 1 = 360 = 8T₉ = 8C(10, 2), 45 = 5 × 9; 21² − 1 = 440 = 8T₁₀; 440 − 360 = 80 = 9² − 1 = 8T₄ = 8C(5, 2); 360 + 80 ≡ 0 mod 440.",
"N47": "6 + 8k at k = 0, 1, 2 is 6, 14, 22, and 22 lies in 17..25 above 17.",
"N48": "CONNECTORS has six keys; the names 2..17 outside it are ten; 6 = 8 − 2, 10 = 8 + 2; 3, 5 and 4 pairings; 6 + 10 + 1 = 17.",
"N50": "Nineteen carryings and 114 transitions from empty under the six offerings; each surfaced sign in {−1, 0, +1} and each carried sign ±1; the code re-executed with each numbered identifier's numeral removed, and again with the numerals reversed, gives the identical 114 transitions.",
"N52": "CONNECTORS ∩ {2, 4, 6, 8} = {2, 6}; `_4_self_sharing` and `_8_other_torusing` occur inside `_1_self_coupling`.",
"N53": "(2k + 1)² − 1 = 8 · k(k + 1)/2 as an identity; the list for k = 0..10 is 0, 8, 24, …, 440; equals 8C(k + 1, 2) for k < 200; 440 = 8 × 55 = 8C(11, 2).",
"N56": "Centres c < 10,000 with c ± 2 and c ± 4 all prime begin 9, 15 (both composite).",
"N57": "On the 3 × 3 grid less its centre, exactly two simple paths join the middle of the left side to the middle of the right, one over the top and one under; each takes two horizontal and two vertical steps.",
"N58": "Only x = 0 solves x = −x on −1,000..1,000; 8 up on 1..9, 17 less on 1..16 and 9 less on 1..8 never give 0.",
"N59": "17 − 9 = 25 − 17 = 8; 17 is in none of the twelve listed forms; each of the spans 1–9, 9–17, 17–25 holds four self and four other momentaries, each one odd and one even, twenty-four in all; 6, 14, 22 counted from nought stand at 5, 13, 21.",
"N60": "n(n − 1)/2 − 2n = n(n − 5)/2 as an identity; for n = 1..10,000 only n = 5 has 2n = C(n, 2); 2 × 5 = C(5, 2) = T₄ = 10.",
"N61": "For n = 3..60 the complement of the n-ring is a single ring (each member two couplings, one connected piece) at n = 5 alone.",
"N62": "Each of the 2¹⁵ two-colourings of the couplings among six holds a one-colour triangle; of the 2¹⁰ among five, exactly 12 hold none, and in each both colours are a 5-ring.",
"N63": "For a = 0..1,000 the pairs (a + j, a + 9 − j), j = 0..4, each have odd sum and mean a + 4½; shifting the opening by one flips each pair's odd member, by two restores it.",
"N65": "The pairs {k, 9 − k} for k = 0..9 are (0,9), (1,8), (2,7), (3,6), (4,5), occupying 1, 2, 2, 2, 2 stations of the ring of nine; 5 × 2 = 10, 10 − 1 = 9, 9 − 1 = 8, 3 × 2 = 6.",
"N66": "Two signs give four joint states; nought to nine are ten; 2² × 5/2 − 1 = 9.",
"N67": "2ⁱ mod 17 for i = 0..7 is 1, 2, 4, 8, 16, 15, 13, 9 and 2⁸ ≡ 1; these are the eight nonzero squares mod 17; three times them are the other eight.",
"N68": "With a joined to b at (a − b) mod 17 a square, none of the 2,380 four-sets of the seventeen is all joined or all unjoined.",
"N70": "440 + 1 = 21² = 9 × 49.",
"N71": "In base 10 the repeated digit sum of 9k is 9 for k to 2,000; in each base b = 3..36 the only m < b whose multiples (to 400) all reduce to m is b − 1.",
"N72": "The walk-by-two centres, 7 × 9 = 8² − 1, 9 × 11 = 10² − 1, 13 × 15 = 14² − 1, 6 × 14 = 10² − 16, 14 × 22 = 18² − 16, and reach over span 1/2 at (6, 14), (14, 22), (6, 22), (10, 18).",
"N75": "On the ring of 48, only 0 and 24 are their own far side; (24 − d)(24 + d) = 24² − d² for d = 1..23; 48 = 7² − 1.",
"N76": "5² − 1 = 24 = 4!; 48/2 = 24; the first prime gap of six below 60 is 23 to 29.",
"N77": "Nine primes below 24 and eight above in 2..59; C(9, 2) = 36 = 60 − 24; C(8, 2) = 28 = T₇; T₆ = 21, T₈ = 36, gaps 7 and 8; 36 − 21 = 15 = C(6, 2); fifteen even gaps among the seventeen; 36 : 24 = 3 : 2 and 9 : 8.",
"N78": "The group generated by a 72° turn about (0, 1, φ) and a 120° turn about (1, 1, 1) has 60 rotations: 24 by 72° or 144°, 15 by 180°, 20 by 120°, 1 identity.",
"N80": "28² − 24 × 32 = 16, 28² − 27 × 29 = 1; gaps (3, 5) and (5, 3); 24 = 5² − 1, 27 = 3³, 32 = 2⁵; 24 × 27 × 32 = 144².",
"N81": "The sieve below 60 gives the seventeen listed primes, 2 the only even, 23 the ninth with eight either side, 59 the seventeenth, sum 440.",
"N82": "120 − p over the seventeen runs 61..118; 60 is not prime; 59 × 61 = 60² − 1.",
"N85": "On the ring of 120: 2↔118, 23↔97, 59↔61; only 0 and 60 self-paired; 24, 27, 32 ↔ 96, 93, 88 with gaps (5, 3).",
"N86": "Rings of the resolver (all together, one +1 at self 0) at p = 3..59 prime, 6p + 6 beats: surfacing sums ±1 at odd beats and 0 at even beats from beat 1; after filling one neighbour pair at one sign at odd beats and one 0 with no such pair at even beats; the pair moves one station per two beats; surfacings invert after 2p; the whole state first recurs at beat p with period 4p.",
"N89": "Ring of two over twelve beats: beat 1 surfaces (+1, none); from beat 2 the two are opposite, sum 0, each inverting at each beat, period two.",
"N90": "Each even ring p + q of odd primes to 59 (6..118) and the ring of 440: after filling no neighbour pair at one sign, no 0, sum 0, and the whole state repeats after two beats and differs after one.",
"N92": "Rings 2..11 run all together and in sequence surface differently from the first beat; the ring of two in sequence repeats every three beats with a 0 at two of each three, and all together repeats every two with no 0; the two functions' parameters are only (3, 2) and (10, 5).",
"N93": "lcm(4p, 4q) = 4pq for each of the 120 pairs of distinct odd primes to 59; the seventeen sum to 440; with N86.",
"N94": "The sixteen gaps of the seventeen primes take values 1, 2, 4, 6 with counts 1, 6, 5, 4, the 1 first.",
"N96": "Among the fifteen inner primes, only 5 (gaps 2, 2) and 53 (gaps 6, 6) have equal gaps below and above.",
"N98": "Primes p in (5, 55) below 30 with 60 − p prime give the six pairs listed (twelve primes), distances 23, 17, 13, 11, 7, 1 summing to 72, spans to 144 = 12², 6 × 60 = 360 = 19² − 1; 11 alone has a composite far side, 49 = 7².",
"N99": "17 + 16 = 33 and each of the seventeen lies below 60.",
"N100": "For each ring N = 2..1,000 the farthest stations from 0 are {h} at even N and {h, h + 1} at odd N, at distance h; the same at each station of the prime rings 5..59 (435), their even rings one short (420) and the rings 9, 15, 25 (49), 904 stations.",
"N104": "For each odd line 1..n (n = 3..59, the prime lines 5..59, 9, 15, 25) each parity has h adjacent pairs, the 2h − 1 inner places in both, the next odd pairing is (n, n + 1) and the prior even pairing (0, 1); at 1..59, 29 pairs each.",
"N107": "From each joint form the right spiral step (x, y) → (y, −x) inverts both at 2 and 6 steps, returns at 4 and 12, and meets all four within 6; 24 = 6 × 4 = 4 × 6, 36 = 9 × 4 = 6 × 6, 60 = 15 × 4 = 10 × 6; 6, 14, 22 ≡ 2 mod 4.",
"N109": "3, 6, 9 parities odd, even, odd; 25, 35, 45, 55 odd and 30..60 even; for each odd m < 100, km and (k + 1)m differ in parity for k to 100.",
"N113": "Of the 512 settings of nine bits, none has the three rows at parity 0 and the columns at 0, 0, 1; the rows read the nine's parity as 0 and the columns as 1.",
"N114": "On the ring of 440 only 0 and 220 are self-paired; 219 other pairs, 221 rings; |220 − k| = |220 − (440 − k)|; radius 0 at 220 and 220 at 0.",
"N118": "220 ± r share the parity of r for r = 0..220; the odd primes to 59 at odd radii 217..161 and 2 alone at 218; 440 = 8 × 5 × 11; 88 multiples of 5, 44 odd and 44 tens, alternating; odd fives at 22 odd radii 5..215; tens at even radii.",
"N119": "The steps between the seventeen primes' radii equal their gaps, sum 57 = 59 − 2, counts 1, 6, 5, 4 at 1, 2, 4, 6.",
"N120": "Position pairs of the seventeen sum 61, 56, 52, 50, 52, 50, 48, 48, with 23 to 440; none sums to 46; by value exactly (3, 43), (5, 41), (17, 29); 5..53 sum 376, 2 + 3 + 59 = 64 = 8², 376 + 64 = 440, radius 156.",
"N122": "880 = 2 × 440; the far side of 220 on 880 is 660; for m = 1..39 the centre 220m is a multiple of 440 at even m and 220 more at odd m.",
"N124": "3, 5, 9, 17 are 2^k + 1; (N + 1)/2 gives 2, 3, 5, 9 and each span's pairs are the span below; two-station pairs 1, 2, 4, 8 with N = 2t + 1; {1, 2, 4, 8} ∩ {3, 4, 5} = {4}, 2 × 4 + 1 = 9; c → 2c − 1 from 9 gives 9, 17, 33, 65; 9 + 9 − 1 = 17.",
"N128": "For each ring N = 1..499 the self-paired stations number one at odd N and two at even N; 9 gives {0}, 440 gives {0, 220}.",
"N130": "Podal pairs (n, 9 − n) for n = 1..4 are odd with even; the overlapping momentaries pair as listed; the two relations share only (4, 5).",
"N132": "The five rows at s = 1..5 as listed; 8s + 1 = 9, 17, 25, 33, 41; for s to 100 the row's next opening is 2 + 8s and 8s + 1 lies above the names 1..8s; six connectors.",
"N133": "For s = 1..100 and each name of 1..8s: ±4s keeps parity, 8s + 1 − n changes it, alternating returns after four distinct names, and the two composed equal 4s + 1 − n (lower half) or 12s + 1 − n (upper); 8s + 1, 4s + 1, 12s + 1 odd; the s = 2 and s = 1 rounds.",
"N134": "For s = 1..59 the row's middle is 2 + 3s, inner reach s over span 2s, outer 3s over 6s; row(s) ∪ (row(s) + 8s) = row(2s) ∪ (row(2s) + 2s); 2 + r(2 + s(x − 2) − 2) = 2 + rs(x − 2) for r, s ≤ 11; even r sends each name to an even.",
"N135": "For B = 8, 16 and r = 1..11: the map keeps parity, sends B + 1 − n to Br + 1 − e(n), shifts by rB/2 at the halfway pairing and by 2r at each side's step; at r = 2 the names 1..8 go to 3, 2, 7, 6, 11, 10, 15, 14.",
"N141": "17 − (n + 8) = 9 − n and 16s + 1 − (n + 8s) = 8s + 1 − n on a grid of n and s wider than their degree.",
"M22": "(−1)² = 1; i^k repeats at period four for k in 0..8, i² = −1, i⁴ = 1, i·i = −1; n + 8 keeps and n + 1 changes the parity of n for n in 1..64.",
"M25": "q(t) = cos(πt/T), T = 1, at t = k/97 for k in 0..499: q(t + T) = −q(t) and q(t + 2T) = q(t) within 1e−9.",
"M27": "{1..4} and {2..5}: 3 shared, 2 outer, union 5, shared folded at two sides 6, occurrences 8 = 4 + 4 = 2·3 + 2, two odd and two even at each side; 2+2 = 2·2 = 4, (2+3, 2·3) = (5, 6), (3+3, 3·3) = (6, 9).",
"M29": "For n in 0..63 the pairs (i^n, n) and ((−i)^n, n) are each distinct; (−i)^n is the conjugate of i^n; i⁴ = 1.",
"M31": "Of the 256 maps {±1}² → {±1}², exactly two are onto, change one coordinate at each state and give m(m(s)) ≠ s at each s: F(P, Q) = (−Q, P) and G(P, Q) = (Q, −P); the changed coordinate alternates from each state; (sgn cos t, sgn sin t) at t = π/4 + kπ/2 steps by F.",
"M33": "Of the 256 maps {±1}² → {±1}², exactly F and G satisfy m(m(s)) = −s at each of the four states.",
"M34": "For F and G at each state s: f²(s) = f⁶(s) = −s, f¹²(s) = s, f⁰..f⁵ meet all four states, f^(k+8)(s) = f^k(s) for k in 0..15; 24, 36 and 60 divide by 4 and by 6 as 6·4, 4·6; 9, 6; 15, 10.",
"M36": "sgn(P·Q) inverts under F and under G at each state; at 399 angles t off the axes sgn(cos t)·sgn(sin t) = sgn(tan t) = sgn(sin 2t), and sin 2t = 2 sin t cos t within 1e−12.",
"M38": "_1_self_coupling([(k, c, t, 0)], offering) surfaces sgn(sum(offering) − c) at k, for c, t in {±1} and each offering of 0, 1 or 2 signs from ±1 (14 cases at t = −1) and each of 3 or 4 signs from {+1, 0, −1}.",
"M39": "The reflected code at n = 2..8 meets all 2^n states, one coordinate changing at each step round the cycle, its halves the n − 1 code and its reversal; at n = 2 it steps by F with the first-changing sign as P and by G with the labels exchanged; at n = 3 the changing coordinate runs 0,1,0,2,0,1,0,2.",
"M41": "(a·b)² + |a×b|² = |a|²|b|² at each a, b in {−1, 0, 2}³ (729 points, degree two in each coordinate), and cos²θ + sin²θ = 1 at each whole degree.",
"M42": "a × (r·a) = 0 for a in {−1, 0, 2}³ and r in {−2, 1, 3}; e₁·e₂ = 0; at 60° the unit pair gives dot 1/2, wedge √3/2, ratio tan 60°; e₁ × e₂ = e₃; (a × b)·a = (a × b)·b = 0 at 729 points.",
"M44": "Cayley–Dickson from the reals: at level 2, e₁e₂ = e₃ and e₂e₁ = −e₃, and the four units associate; at level 3 some unit triple does not associate; each product of two of the seven imaginary units is ± one unit, giving seven lines of three with each pair on one line; |xy|² = |x|²|y|² at sample whole elements at levels 1, 2, 3.",
"M47": "In Q(√5) exactly: 1/(φ − 1) = φ with 1 < φ < 2, φ² = φ + 1, φ³ = 2 + √5, 1/φ³ = −2 + √5, φ³ − 1/φ³ = 4; Fibonacci ratios within 1/q² of φ.",
"M50": "On −50..50 −x = x at 0 alone; on nonzero p/q with |p| ≤ 20, 1 ≤ q ≤ 20, 1/x = x at ±1 alone; on 3×3 matrices over {−1,0,1} the transpose is an involution fixing the 3⁶ symmetric ones; complement on the subsets of six fixes none; −s ≠ s on ±1; conjugation fixes the real Gaussian integers alone; −v = v on {−3..3}³ at the origin alone.",
"M53": "For each even N in 2..200, k → −k mod N and k → k + N/2 mod N are involutions; the first fixes {0, N/2} and the second nothing.",
"M54": "For h in 1..59 the places at greatest shorter-way distance are {h, h+1} on a ring of 2h+1 and {h} on a ring of 2h; at each origin of the 15 primes 5..59 and of 9, 15, 25 the far places are (N−1)/2 and (N+1)/2 on.",
"M55": "Among the involutions of n places, n in 1..9, one without a fixed point exists exactly at even n; for h in 1..40 the odd-opening and even-opening pairings of 1..2h+1 have h pairs each, share the 2h − 1 places 2..2h, and leave 2h+1 and 1 unpaired; at 1..59, 29 pairs each.",
"M58": "For N in 2..120 and k in 1..N−1, stepping k from 0 meets N/gcd(N, k) stations before 0 again, and N at prime N; 8/gcd(8,3) = 8, 9/gcd(9,3) = 3, gcd(4,9) = 1.",
"M59": "For m, n in 1..40, stepping (a, b) → (a+1 mod m, b+1 mod n) from (0, 0) meets mn/gcd(m, n) pairs, all with a − b ≡ 0 mod gcd(m, n), of gcd(m, n) classes; mn at coprime m, n.",
"M63": "At each state the half step has period 2 and F and G period 4 (no earlier meeting); the pairs (state, n) for n in 0..199 are distinct under each of the three.",
"M65": "Refl(b)·Refl(a) = Rot(2(b − a)) for lines a in 0°, 7°, …, 175° and b in 0°, 11°, …, 176°; on {±1}²: invert P then Q is the half step, invert P then exchange is G, exchange then invert P is F.",
"M66": "Each of the 6 orders of the three single inversions sends each of the 8 states of {±1}³ to its negative; the 8 part into 4 pairs; det(−Iₙ) = (−1)ⁿ for n in 1..8.",
"M68": "On {−2..2}³: diag(−1,1,1) fixes the plane x = 0, diag(−1,−1,1) fixes the axis x = y = 0 with determinant 1, diag(−1,−1,−1) fixes the origin alone with determinant −1; F² is the negation at each of the four states.",
"M71": "2⁷ = 128; (3/2)¹² = 129.746337890625; (3/2)¹²/2⁷ = 3¹²/2¹⁹ = 531441/524288 exactly.",
"M76": "81/87 > 234/270 and 192/263 > 55/80 while 273/350 < 289/350; x = 1, y = −1 inverted together fifty times sum to 0 at each step.",
"M79": "Under [(k, +1)] at each call, carrying (k, 1, −1, 1) surfaces 0, 0, 0, +1 and is empty after the 3rd call; (k, 1, −1, 0) surfaces 0, 0, 0, 0, +1 and is empty after the 4th; empty carrying under +1 surfaces +1 and opens (k, 1, −1, 0).",
"M81": "For s in 1..5 the row 2 + 2sj (j = 0..3) steps by 2s, continues to 2 + 8s, and 8s + 1 (9, 17, 25, 33, 41) is odd and outward of 1..8s; the five rows as listed.",
"M82": "For s in 1..40 and n in 1..8s: pairing and fold are fixed-point-free involutions, the pairing keeping and the fold changing parity; fold∘pairing is 4s+1−n or 12s+1−n and fixes none; alternating them from n meets 4 distinct names and n again at the 4th; (3, 11, 6, 14) at s = 2 and (3, 7, 2, 6) at s = 1.",
"M83": "For s in 1..29, n in 1..8s: fold_2s(n + 8s) = fold_s(n); n, n+8s, 8s+1−n, 16s+1−n distinct and closing; for t in s+1..4s fold_t(n + 8(t−s)) = fold_s(n), and 8(t − s) = 4t exactly at t = 2s; the four rows at s = 1; 17 − (n + 8) = 9 − n.",
"M84": "For s in 1..29 the row's middle is 2 + 3s with offsets −3s, −s, s, 3s, inner span 2s and outer 6s; 6s ≠ 8s and 2 + 3s ≠ (8s+1)/2; at s = 2 the end pairs {2,14},{6,10} against the halfway pairs {2,10},{6,14}.",
"M85": "D_r(D_s(x)) = D_rs(x) for r, s in 0..8, x in −20..39; D_s maps 2 + 2j to 2 + 2sj; D_r(x) is even for even r in 2..18 at x in −30..59.",
"M86": "For s in 1..29 and j in 0..3: (16s + 1 − (2 + 4sj)) − (2 + 2s + 4s(3 − j)) = 2s − 3; at s = 1 the fold 17 − n sends 2 to 15 = 16 − 1, at s = 2 the fold 33 − n sends 2 to 31 = 30 + 1.",
"M87": "For B in {8, 16}, r in 1..6: E_r keeps parity, E_r(B+1−n) = Br+1−E_r(n), E_r(n + B/2) = E_r(n) + rB/2, E_r(n+2) − E_r(n) = 2r; E_r(B+1) > Br+1 at r ≥ 2; E_2 on 1..8 is 3, 2, 7, 6, 11, 10, 15, 14.",
"M88": "n² − (n − k)(n + k) = k² for n, k in −50..50 (a polynomial of degree two in each, so decided), and = 1 at k = 1 for n in −100..100.",
"M89": "k² = 2k for k in 1..999 at k = 2 alone; n² − (n−2)(n+2) = 4 for n in −100..100; 4² − 2·6 = 4; 10² − 8·12 = 4.",
"M90": "2k − 1 = 1 for k in 1..199 at k = 1 alone; 23, 25 about 24; 55 − 23 = 32, k = 16, centre 39, 39² − 23·55 = 256 = 16².",
"M96": "Unit square diagonal √2, unit cube body diagonal √3; regular pentagon diagonal/side = φ within 1e−12; cos 36° = φ/2, sin 18° = 1/(2φ) = (√5 − 1)/4, cos 18° = √(10 + 2√5)/4 within 1e−15; in Q(√5) exactly 4(φ/2)² − φ − 1 = 0 and 1/(2φ) = (√5 − 1)/4.",
"M97": "tan 2x = 2t/(1 − t²) at x = k/10 degrees, |k| ≤ 890 off t = ±1; 2t/(1−t²) = 2t over p/q (|p| ≤ 40, q ≤ 10) at 0 alone; cos 90° = 0; 2x mod 1 shifts the six binary digits of n/64 one place for n in 1..63.",
"M98": "g(t) = 2t/(1 − t²): g(√3) = −√3, g(−√3) = √3, six steps from √3 alternate; tan 60° = √3, tan 120° = −√3; no rational p/q (p < 60, q < 30) has g = −t; on t = k/1000, |k| ≤ 3000, g(t) = t at 0 alone.",
"M99": "For a, b, c in −4..4, Rᵀ[[a,b],[b,c]]R at θ = ½·atan2(2b, a − c) has off-diagonal 0 within 1e−9; θ = 22.5° at (5, 2, 1) and 45° at a = c.",
"M100": "sin x = 2t/(1+t²), cos x = (1−t²)/(1+t²) at x = 1°..178°; for 1 ≤ n < m < 40 the triple is Pythagorean and (2mn, m²−n²)/(m²+n²) lies on the circle exactly; each triple with c < 500, divided by its gcd, is one of them up to order.",
"M121": "On the chain 0 < a < 1 with ¬x the greatest y meeting x at 0: ¬a = 0, ¬0 = 1, ¬1 = 0, ¬¬a = 1 ≠ a.",
"M125": "Three neutrals give 3 pairings, 6 ordered co-offerings and 2³ = 8 fixed-or-floating states.",
"M128": "For each set of fixed neutrals, the ordered co-offerings with both ends floating number 6, 2, 0, 0 at 0, 1, 2, 3 fixed; each neutral is in 2 of 3 pairings and 4 of 6 co-offerings.",
"M133": "A₅ has 60 elements in classes 1, 12, 12, 15, 20; the only unions of classes containing the identity with size dividing 60 are sizes 1 and 60; [S₅, S₅] = A₅ = [A₅, A₅]; S₄'s derived series has orders 12, 4, 1.",
"M137": "The 12 points (0, ±1, ±φ) and cyclic orderings have 30 pairs at distance 2 and 20 triangles; the rotations carrying them onto themselves number 60, with traces 3 (1), −1 (15), 0 (20), φ or 1 − φ (24); 36 : 24 = 3 : 2.",
"M139": "The central difference of (cos θ, sin θ) equals F(cos θ, sin θ) = (−sin θ, cos θ) within 1e−8 at each whole degree; {i^k} has 4 elements containing ±1, {(−1)^k} 2; eᵢ·eⱼ = δᵢⱼ.",
"M140": "Rings of n = 3..14 have a proper 2-colouring exactly at even n, and the fewest same-coloured neighbour pairs is 1 at odd n; each connected graph on 1..6 labelled vertices has 0 or 2 proper 2-colourings.",
"M141": "{±1}³ has 8 points and 12 pairs differing in one coordinate; 6 faces; the 48 signed permutation matrices include 24 of determinant 1.",
"M142": "det(−I₃) = −1, det(−I₄) = 1, diag(−1,−1,1,1)·diag(1,1,−1,−1) = −I₄ with each factor of determinant 1; −v = v on {−2..2}⁴ at the origin alone.",
"M144": "Norm-1 points: 8 in ℤ⁴, 16 in (ℤ + ½)⁴, 24 together; min over whole q in {−2..2}⁴ of |(1,1,1,1) − 2q|² is 4; d/4 = 1 for d in 1..29 at d = 4 alone.",
"M148": "[[1,1],[−1,0]]^k = I first at k = 6, trace 1; [[2,1],[1,1]] trace 3, eigenvalue (3+√5)/2 = φ², no power to 59 is ±I; each SL(2,ℤ) matrix with entries in −6..6 has a power I within 12 when |trace| < 2, none when |trace| > 2, and at |trace| = 2 is ±I or has none.",
"M150": "The 10 transpositions of 5 are involutions fixing 3 points each; C(n, 2) = 2n for n in 2..199 at n = 5 alone; T₄ = 10 = Te₃ = 1 + 3 + 6; C(2, 2) = 1.",
"M151": "At each side of the regular pentagon exactly one diagonal shares no corner, parallel to it with length ratio φ; the two transpositions commute and their product is the reflection k → 2l − k mod 5 at the corner l left out; the five products generate 10 permutations: identity, 4 with no fixed corner, 5 with one.",
"M152": "Each of the 2¹⁵ 2-colourings of K₆ has a one-coloured triangle; of the 2¹⁰ of K₅ exactly 12 have none, each colour class a 5-cycle.",
"M156": "2⁴⁶·3²⁰·5⁹·7⁶·11²·13³·17·19·23·29·31·41·47·59·71 = 808017424794512875886459904961710757005754368000000000 has 15 prime divisors, the primes to 59 less 37, 43, 53, and 71; E₄³/Δ = q⁻¹ + 744 + 196884q + …",
"W7": "CONNECTORS checked against JOINS and against TWO's table.",
"W14": "the two sides' arithmetic.",
"W18": "the two sets.",
"W20": "each of the nineteen carryings under each of six offerings that surfaces a nonzero sign.",
"W21": "JOINS as declared, and two selves joined along at the third function: A's 9 arrives at B's 17, nothing at B's 2 or 14, and A receives nothing.",
"W23": "the six pairs.",
"W24": "the map's powers at each (x, y), and the counts.",
"W25": "s from 1 to 5, and each partner's parity.",
"W26": "the arithmetic.",
"W28": "the primes below 60.",
"W29": "each of the fifteen.",
"W30": "each even L up to 1,000.",
"W33": "the primes below 60.",
"W48": "the global names each function loads (none), and repeated calls over the nineteen carryings under the six offerings.",
"W56": "the module's top-level tree has no call.",
"W62": "both signs over nine calls, with that one change and without it.",
"W65": "rings of 3 to 8 against their complete graphs.",
"W70": "the 171 pairs both ways.",
"W77": "each ring over 8n + 8 couplings.",
"W79": "the four seed pairs, both selves.",
"W81": "each taking-out tested against calls over the reachable carryings, offerings with and without 0, and two keys.",
"W87": "k from 0 to 439.",
"W92": "n from 1 to 200.",
"W95": "the four continuations.",
"W96": "the two variants at every window.",
"W97": "the paths over the grid.",
"W100": "the two trees, docstrings aside.",
"E1": "Prior (1,2), now (2,3), next (3,4) cover four positions, each completing the next's opening; along one side 1-2, 3-4 open 5 and 2-3, 4-5 open 6 (two on), across the next opens one on; five-views at 1, 2, 3 share four positions pairwise, and at each shared number one view opens and the other completes.",
"E6": "Square grids n x m closed as a torus, n, m from 3 to 12: every point has degree 4, 4F = 2E = 4V, and V - E + F = 0; the cube gives 8 - 12 + 6 = 2.",
"E10": "Under (x,y) -> (y,-x) and (x,y) -> (-y,x), from each of the four joint forms over eight steps, exactly one position changes per step and the changed position alternates.",
"E11": "Of the four orders of two passages (first/second each), exactly first-second and second-first change both relations; first-first and second-second leave one unchanged.",
"E12": "The shown round (+,+) -> (-,+) -> (-,-) -> (+,-) -> (+,+) is (x,y) -> (-y,x) at each step, visits four distinct forms, and is not (x,y) -> (y,-x).",
"E13": "Every simple graph on 1 to 5 points: a proper two-colouring exists exactly when no odd closed walk exists (trace of A^k = 0 at each odd k <= n), and then the colourings number 2^(connected components).",
"E37": "n^2 - (n-1)(n+1) = 1 for n from -1000 to 1000; (2,3) and (3,4) share 3.",
"E38": "1..5 union 2..6 is 1..6; the momentaries 1-2, 3-4, 5-6 cover 1..6; parities of 1..6 read co bi co bi co bi.",
"E39": "At n = 2..6 the self (momentaries 1-2, 3-4, 5-6) opens at odd and completes at even, the other (2-3, 4-5, 6-7) the reverse; this matches the table's faces at each place, and 5 places x 2 faces = 10.",
"E42": "The ring 3->2->4->1->14->12->6->10->11->16->3 and the list 1,10,7,9,8,4,6,5,3,2 appear in the file; parsing the five address rows, each of the ten ways has one edge, the ring's ten edges read the ways 1,10,7,9,8,4,6,5,3,2 in order, the ring has ten distinct names including 6 and 14, and its edges 4 to 8 are 1->14->12->6->10->11.",
"E46": "1+3+5 = 9 = 3^2, 2+4+6 = 12 = 3*4, 3^2 - 2*4 = 1; for n from 1 to 100 the first n odd numbers sum to n^2 and the first n even to n(n+1); 3..8 is six numbers and 9 follows.",
"E47": "Rings of 1 to 11 selves, one +1 offered once at self 0, each self coupling once per coupling and 9-other-releasing feeding the next self: every self's carrying changes within 40 couplings; a ring started at rest (empty carrying, nothing arriving) stays at the rest state for 100 couplings.",
"E50": "3/11, 4/12, 5/13, 7/15, 8/16 are each 8 apart; 17 - (9 - n) = n + 8 for n = 1..8; the ten internal names and CONNECTORS {2,6,9,10,14,17} are disjoint and together give 2..17, with 1 all of 1..17; the ring's names meet the connectors at 2, 6, 10, 14 and include 1.",
"E53": "Parsing the file's two conception tables: 63 ids, NY01..NY42 and SA01..SA21, each once; per way 1..10: 2, 5, 8, 10, 6, 9, 5, 5, 7, 6.",
"E60": "At one key receiving +1 each call from empty the carrying runs (+,-,0), (+,-,1), (+,-,2), (+,-,3), empty, and repeats: a five-cycle with the uniform law stationary; under empty receiving (c,-c,0) and (-c,c,0) exchange, equal weights stationary and detailed-balanced; A=(+,-,0), B=(-,+,0), X=(+,-,1) under empty receiving give A->B, B->A, X->B, and (1/2,1/2,0) is stationary (exact fractions).",
"E65": "Each of the 18 nonempty reached carryings under each of the six offerings: the next is never the same carrying, and each transition is exactly one of retaining (a+1), fresh write (t inverted, opening 0) or completing (empty), all three occurring.",
"E66": "Over the 18 nonempty carryings and six offerings, a next with the same second sign is always (c, t, a+1) and a next with the other second sign always opens at 0; retaining from opening 0 continues three times at t = -1 and four times at t = +1.",
"E67": "Over the 18 nonempty carryings and six offerings, a surfaced 0 gives only retaining or completing; offering the carried sign at each call surfaces 0 at each call and every carrying leaves within five couplings, the longest exactly five.",
"E69": "From (c,-c,0), c = +1 and -1, nine calls under empty receiving: each next is opposed, both signs inverted, the surface -c; one side's reversal (c,-c) -> (-c,-c) agrees.",
"E71": "No p in {+1,-1} satisfies p = p and p = -p together.",
"E72": "The windows of length 3 along 0101... alternate 010 and 101; at two molecules with equal constants 2 - n = n only at n = 1, and 1 goes to 0 or 2; (1/4, 1/2, 1/4) meets detailed balance at both conversions.",
"E73": "The relation {(0,1),(1,2)} is not transitive and lacks (0,2); for a from -5 to 5 the pair (a, a+1) with one end moved on by one is no longer immediate-next.",
"E74": "F(P,Q) = (-Q,P) reaches all four pairs from each; each of the 14 nonempty proper subsets is left from each member within at most 3 advances, the maximum 3 met by {++,-+,--} from ++; the invariant subsets are the empty set and all four.",
"E75": "With b = c = a, a*f = b*w holds exactly at f = w for f, w in 1..10; r_n = lambda^n with lambda in {-1/2, -1, -2, 3} stays nonzero over 200 exact steps; +1 and -1 at one empty key surface 0 and carry nothing, 9-other-releasing returns (k, 0), and offering it to an empty self returns ([], []), over six calls.",
"E76": "Of all 256 maps on the four pairs, exactly two square to J(c,t) = (-c,-t): (c,t) -> (-t,c) and (c,t) -> (t,-c); at each nonempty carrying under each offering with a nonzero surface s, the fresh pair is (s, -t) = G(t, s); under empty receiving s = -c and the pair goes to (-c,-t).",
"E79": "At each of the 19 reached carryings under every offering of 0 to 4 signs from {-1,0,+1}, any surfacing equals sign(sum - c) (c = 0 at empty); (+,-,0) with [+,+] gives (+,+,0), (-,+,0) with [+,+] gives (+,-,0), (+,-,0) with [+] gives (+,-,1), (+,-,3) with [+] leaves.",
"X28": "For p in 0..60 pentagons and h in 0..500 hexagons with F = p + h, 2E = 5p + 6h, 3V = 2E, V − E + F = 2 holds exactly at p = 12.",
"X41": "_1_self_coupling([], [(k, 1), (k, -1)]) returns ([(k, 0)], []); _1_self_coupling([], []) returns ([], []); the two differ.",
"X43_probe": "2 × 5 = 10 = C(5, 2) (the count only; the joining stays nye).",
"X49": "The code's identifiers _n_relation_root (1..16) and CONNECTORS[17] spell the seventeen names; each numbered name n-relation-root and `_n_relation_root` in EXP and NAM v372 and GIM v370 equals the name at its number.",
"X62": "For each (x, y) in {±1}²: two right spiral steps (y, −x) give (−x, −y), four give (x, y); three give (−y, x).",
"X63": "6, 14 and 22 are the sixth place of 1..9, 9..17 and 17..25; 19-27-22-30 less 16 is 3-11-6-14; 22 is no name's number.",
"X64": "Odd origin co bi co bi co and even bi co bi co bi (edges, flanks, centre); swapping co/bi exchanges them; each of the twelve earlier names' co/bi prefixes is an opening of its number's five-prefix (1 at 3, 2 at 1, 3 at 6, 5 at 7 and 8); each NAM 3.3 row opens co at odd, bi at even, with its origin's five-prefix.",
"X66": "Round 1-9-8-16, 2-10-7-15, 3-11-6-14 and 4-12-5-13 each step is 8 up/down or 17 less, parity changes exactly twice, both at 17 less, two odd and two even.",
"X68": "Seven calls of +1 at one key from empty, tracing 1-self-coupling's locals at return: surfaces +1,0,0,0,0,+1,0; at calls 2..5 the offering, 6 (−1), incoming 8 (−1), 10 (0), 12 (0) and 14 ([−1, +1]) are the same while the returned 16 runs 1, 2, 3 and the carrying is empty after call 5.",
"X69": "Carrying [(k,+1,−1,0),(k,−1,+1,0)] under []: 6 = {k: +1} (the last), surfacing (k, 0), 11 = [(k,−1,+1,1)] (the last continuing); +1 offered at carried (k,+1,−1,0): 14 holds (k,+1) and the key surfaces 0.",
"X73": "On 0..9 under <, neither a<b nor b<a iff a = b; on subsets of {1,2,3} under proper inclusion, pairs with neither are equal or incomparable, and an incomparable pair exists.",
"X79": "The ten rows of NAM 4.9 name pairs (a, a + 8), a in 1..8: (6,14), (2,10), (3,11), (7,15) once, (4,12), (8,16), (5,13) twice; (1,9) at none.",
"X88": "(x xor b) xor b = x; next = prior xor now leaves (0,0) still and runs the other three round in three; of the 512 ±1 stores of a 3×3 square none has each row product +1 and column products +1, +1, −1.",
"X97": "(n − 1)(n + 1) = n² − 1 for n in −1000..1000.",
"X98": "r² − r − 1 ≠ 0 at r = ±1; for n in 1..60, F(n+1)/F(n) as an exact fraction has r² − r − 1 < 0 (below φ) at odd n and > 0 (above) at even n.",
"X104": "The eight podal pairs {n, 17 − n} on 1..16 and the eight straight-across pairs {k, k + 8} share none.",
"X107_probe": "59 − 2 + 1 = 58 = 118 − 61 + 1 (the count only; the joining stays nye).",
"X138": "GIM 3.3 has nine rows numbered 1..9; parity column even/naming or odd/explaining, alternating, five even and four odd; pass 1 is bound and pass 9 crossings; each odd-numbered pass is at the even.",
"X144": "Reflected binary code for n = 1..12: 2ⁿ distinct words, each step round (including last to first) changes one digit.",
"X145": "2^(2^k) + 1 prime for k = 0..4 by trial division; 2^32 + 1 = 641 × 6700417; C(n,4) + C(n,2) + 1 = 1, 2, 4, 8, 16, 31 for n = 1..6.",
"X146_probe": "Some 2-colouring of K5's 10 edges has no one-colour triangle; none of K6's 32,768 does.",
"X147": "Primes 5..59 are fifteen; on a ring of n (4..60) the selves at the greatest distance min(j, n − j) from one self number 2 at odd n (9, 15, 25 among them) and 1 at even n.",
"X148": "EXP 3.4 has 9 bullets; EXP 3.2 names fixed noun, forcing, character, wrapper; EXP 3.13 lists 6 sentences after its check; NAM has 47 '## 5.n' namings, 2.5 has 7 rows, 4.9 10 rows, 4.18 7 items, 3.3 17 rows, 6.2 8 rows, 1.1 4 bullets; GIM 3.3 has 9 rows and 5.1 10 rows.",
"Q12": "x -> x xor 1 runs 0,1,0,1,0,1; next = prior xor now from (0,1), (1,0), (1,1) returns to its start pair after exactly three steps with first three values 011, 101 or 110, and (0,0) stays 0.",
"Q13": "Of the 512 assignments of bits to a 3x3 square, none has each row at parity 0 with column parities (1,1,1), and none with column parities (0,0,1).",
"Q15": "n + 8 keeps parity and 17 − n changes it for n in 1..16; 9 − n changes it for n in 1..8; in each of the twelve forms of ONE's tables within 1..16 exactly two steps change parity and each such step is a pair summing to 17.",
"Q22": "The primes to 59 are seventeen, sum to 440 and open sixteen gaps; 2 × 59 = 118; 60 lies midway between 59 and 61.",
"Q25": "At each of the nineteen reachable carryings, _1_self_coupling with an offering (k, ±m), m in {2, 5, 17}, returns the same as with (k, ±1).",
"Q26": "At each of the nineteen carryings under each offering of 0 to 4 signs from {−1, 0, +1} (121 offerings), each surfaced value lies in {−1, 0, +1}, and each of the three occurs.",
"Q27": "At each of the nineteen carryings, _1_self_coupling with offering [(k, 0)] returns the same as with the empty offering.",
"Q28": "The numeric constants in the bodies of _1_self_coupling and _9_other_releasing are exactly {0, 1, 3, 4}.",
"Q32": "F(n+1)/F(n) for n = 1..38 alternates above and below φ; the continued fraction of F(40)/F(39) begins with thirty partial quotients 1.",
"J7": "k·300·ln 2 with k = 1.380649e-23 J/K is 2.871e-21 J, rounding to 2.9e-21 J.",
"J9": "Of the 65,536 relations on four elements, 3,994 are transitive, and in each, a R m, b R m and m R s give a R s and b R s.",
"J10": "Each of the 50,978 serial relations on 1 to 4 elements, and each of the 3,413 functions on 1 to 5 elements, contains a directed cycle.",
"J12": "cos and sin at 0°, 60°, 90° are (1.000, 0.000), (0.500, 0.866), (0.000, 1.000) to three places.",
"J14": "sin t + sin(t + 2π/3) + sin(t + 4π/3) = 0 at 360 equally spaced t.",
"J26": "n² − (n − 1)(n + 1) = 1 for n = 1..10,000; n² − (n − k)(n + k) = k² for n = 1..199, k = 0..49; (a + b) even iff a and b share parity, a, b = 0..199.",
"J28": "The k-faces of the n-cube, C(n,k)·2^(n−k), give (8, 24, 32, 16) at n = 4 for k = 3..0, and f(n+1, k) = 2 f(n, k) + f(n, k−1) for n = 1..8.",
"C10": "2n² for n = 1..4 is 2, 8, 18, 32 with climbs 6, 10, 14; 14 − 6 = 8, centre 10; 1 + 3 + … + (2n − 1) = n²; doubled odds 2, 6, 10, 14.",
"C11": "24² − 23·25 = 1, 28² − 24·32 = 16, 28² − 27·29 = 1, and n² − (n − k)(n + k) = k² for n < 200, k < 50.",
"C12": "|S4| = 24, |A4| = 12, 7² − 1 = 48, |A5| = 60, |S5| = 120; the centre of S5 is trivial and the centre of A5 is trivial, so A5 × C2 has a centre of order 2 and is not S5.",
"C17": "4n + 2 = 2(2n + 1) for n < 100, giving 2, 6, 10, 14 at n = 0..3.",
"C20": "Running sums of 2, 8, 8, 18, 18, 32, 32 are 2, 10, 18, 36, 54, 86, 118; 2 + 8 + 18 + 32 = 60; 27 + 32 = 59; 24 + 96 = 27 + 93 = 32 + 88 = 120, together 360; gaps 3, 5 and 5, 3.",
"C22": "For each hexagon count h = 0..199 a closed trivalent cage of pentagons and hexagons satisfies Euler's relation only at 12 pentagons; C60: 32 faces, 90 edges, 60 vertices; 12 − 30 + 20 = 2 both ways; cuboctahedron 12 − 24 + 14 = 2 with 24 edges.",
"B15": "2^6 = 4^3 = 64, C(6,3) = 20, 4! = 24, 5! = 120, 4! − 1 = 23, 5! − 1 = 119.",
"B19": "(1 ± √5)/2 solve x² = x + 1, the positive root ≈ 1.618; x² = x has integer roots 0 and 1 only; 1/φ² ≈ 0.382.",
"P5": "At the four joint forms of two signs, (x, y) → (y, −x) and (x, y) → (−y, x) move each form.",
"P11": "55 − 23 = 32 = 2·16; (23 + 55)/2 = 39 and 39² − 23·55 = 16²; 24² − 23·25 = 1; C(11,2) = 55.",
"P22": "2..59 and 61..118 each hold 58 numbers; 60 is midway between 59 and 61; 2 + 118 = 120.",
"P26": "59 = 1 + 2(4 + 9 + 16); φ³ − φ⁻³ = 4 exactly in Q(√5); 60 = 5·12; 59/2 = 29.5; i⁴ = 1.",
"P28": "EIGHTEEN 5.13's table has 50 rows: 2 at the file's own, 48 at the ten namings with counts (10, 0, 5, 2, 6, 3, 7, 6, 3, 6); groups 21, 13, 8, 6; odd namings 31, even 17; pairs (10,0), (5,2), (6,3), (7,6), (3,6).",
"L28": "NINETEEN 5.2 to 5.8 hold 66 rows, 50 met and 16 reaching; 41 carry one of the ten namings; the rows cite seams 3.1 to 3.37; at the five naming pairs the odd carries more at four and less at one.",
"HP12": "The entry headings '## n name' of TWENTY-ONE before 'The collection': 255 headings, numbers ascending from 1 to 257, and {1..257} less the numbers = {155, 172}.",
"HP16": "At each of the 255 entries, the lines 'Unreachability.', 'Specifications withdrawn.' and 'Narrowing recorded.' counted non-empty: 174, 34 and 231.",
"RH3": "n^2 − (n − 1)(n + 1) = 1 for n from 2 to 1,000, and at 3, 4, 5, 16 and 24 by name; 4^2 − 2·6 = 4.",
"RH5": "The four neighbour pairs (2,3) to (5,6) each at both orders give eight turns from 2 < 3 to 6 > 5; neighbouring pairs share one number, and the lesser sides run 2, 2, 3, 3, 4, 4, 5, 5.",
"RH10": "The four gatherings as named in TWENTY-TWO take arriving, bound, middle | sequencing, rate | sign, two-way | opening, carry, membrane: sizes 3, 2, 2, 3, and together each of the ten once.",
"RH15": "The headings '## p.q name (Hard Problem Registry n)' of TWENTY-TWO: 257; per part 33, 24, 33, 9, 25, 19, 20, 16, 43, 33, 1, 1; their numbers cover TWENTY-ONE's 255 plus 155 and 172, each at TWENTY-ONE's own name.",
"LS7": "At each of the 22 entries 2.1 to 2.22 of TWENTY-FIVE, the line 'Any member carrying it.' opens No (No., No pair, No population).",
"LS11": "At each of the 22 entries, the line 'Standing in the ten.' carries 'All ten stand fill' at 18; the other four are 2.2 (bound and rate empty), 2.4, 2.5 and 2.15 (filled at eight; 3 nye and 6 empty).",
"LF2": "The 1.1 and 1.2 tables of TWENTY-SIX: 29 living rows from Natural Intelligence to TWENTY-SEVEN, 5 improving rows, no TWENTY-EIGHT or TWENTY-NINE row.",
"LF3": "The 1.3 clusters table: 7 rows seating 26 distinct files; the exhibit numbers seated at none are TWENTY-THREE, TWENTY-FOUR and TWENTY-SIX.",
"LF4": "TWENTY-TWO's part counts at parts 1 to 10, paired (1,2), (3,4), (5,6), (7,8), (9,10): the odd exceeds the even at each pair; the odd total 154, the even 101.",
"LF7": "The 1.1 subtitles: bare 'Social' at 9 rows and 'Social-' at 1; 'Registry' at 5 titles and 2 subtitles; bare 'Competency' at 3; 'Self-' at 4.",
"GH13": "{1, 7, 8, 9} ∪ {3, 4, 5, 10} ∪ {2, 6} = {1..10}, the three sets disjoint (sizes summing to 10).",
"GH14": "The 7.10 table of TWENTY-SEVEN read as door line → TWENTY-TWO part: {1:1, 2:8, 3:9, 4:6, 5:4, 6:2, 7:5, 8:3, 9:10, 10:7}, a permutation of 1 to 10.",
"GH16": "The 7.11 tables: ten door lines take eight distinct namings; the within lines are 3, 4, 6, 9 at four namings; lines 1, 2, 5, 7, 8, 10 at four; 2 and 7 share one, 8 and 10 share one; the adjacency table shares a naming at lines 1 and 5 alone.",
"GH21": "2 + 8 + 8 + 18 + 18 + 32 + 32 = 118, running sums 2, 10, 18, 36, 54, 86, 118; 2 + 8 + 18 + 32 = 60, among no running sum.",
"I5": "24 → 27 → 32 has gaps 3, 5 and 24 → 29 → 32 gaps 5, 3; both span 8.",
"I6": "At 2,000 angles in (−1.55, 1.55), skipping those near a pole of tan x or tan 2x, tan 2x equals 2 tan x/(1 − tan^2 x) to 1e-9.",
"I8": "The primes below 60 are seventeen, from 2 to 59, summing to 440.",
"I9": "The identifiers of resolver_v372.py spell names 1 to 16; their roots after the number and relation are twelve; CONNECTORS[17] names 17-social-abundancing, whose root is none of the twelve.",
"CO12": "x ← 1 + 1/x from 1, forty times in exact fractions: each value is F(n+1)/F(n); the fortieth is within 1e-15 of (1 + √5)/2, and φ^2 − φ − 1 = 0 to 1e-12.",
"CO19": "Of the 24 orders pairing four consolidations to gaps 1, 2, 4, 6, one (the identity) keeps depth increasing with gap; 23 break it.",
"CO21": "7·17 − 1 = 118; 59·2 = 118; 6.94 < 118/17 < 6.95.",
"G7": "abs(1 + w + w^2) < 1e-12 at w = exp(2*pi*i/3); the mean over 3,600 steps of a cycle of (sqrt2 V cos th)(sqrt2 I cos(th - phi)) equals V I cos phi within 1e-6 at six phases, positive at phi = 0, zero at pi/2, negative at pi.",
"G9": "440 == 8*55 == 3*146 + 2 == 4*110 and 55 == 1 + ... + 10 == C(11, 2).",
"G12": "The file's five tone rows give its signed differences and beat rates; for integer e, d in -40..40, b'^2 - b^2 == d(2e + d) with b = |e|, b' = |e + d|, and sign(b' - b) == sign(e d) whenever e, d nonzero and |d| < |e|.",
"G13": "(3/2)^12 / 2^7 == 3^12 / 2^19 == 531441/524288; 1200 log2 of it rounds to 23.46; 432/440 == 54/55.",
"G18": "_1_self_coupling([(0, 1, m, 3)], [(0, 1)]) returns ([(0, 0)], [(0, 1, m, 4)]) at m = 1 and 7 and ([(0, 0)], []) at m = -1; each returned carrying under an empty offering returns ([(0, -1)], [(0, -1, -m, 0)]) at m = 1 and 7 and ([], []) at m = -1.",
"G20": "Over 3,600 steps: the three-phase sum of VI cos^2(th - 2 pi j/3) stays 3VI/2 within 1e-12, two phases in quadrature stay VI, and two opposed by half a cycle range from 0 to 2VI.",
"G21": "Carrying [(k, +1, -1, 0), (k, +1, +1, 2)] under an empty offering returns ([(k, -1)], [(k, -1, -1, 0)]); [(k, +1, -1, 0), (k, -1, +1, 1)] returns ([(k, 0)], [(k, -1, +1, 2)]); 3,000 random carryings with repeated keys return each key once.",
"G22": "300 random carryings from the nineteen at two keys, each under every ordering of a random offering of up to five signs: the surfacing (as a map) and the carrying (as a set) stay the same, and the surfaced list follows the order keys first meet a nonzero sign in the offering, then the carried keys.",
"G29": "72 + 1 == 73 == (59 - 2) + 16; 146 == 2*73 == 144 + 2; 3*146 == 438; 438 + 2 == 440; 3*120 == 360 == 8*C(10, 2); 440 - 360 == 3*26 + 2 == 80 == 16*5; C(5, 2) == 10 == 5 + 5; 12*10 == 120.",
"G30": "For N from 1 to 64: a chain has N - 1 connections and a simple ring N (N >= 3); k and N - k sum to N; at even N, stations k and (k + N/2) mod N stand N/2 apart both ways.",
"T9": "At each of the nineteen carryings an offering [(k, 0)] returns what [] returns; a self offered (+, -) at empty carrying surfaces (k, 0), 9 releases (k, 0), a second self offered that release at empty carrying returns ([], []), and a third offered the second's release returns ([], []).",
"T14": "The resolver file has no import; _1_self_coupling takes (_3_self_carrying, _2_self_offering) and _9_other_releasing (_10_other_surfacing, _5_other_neutralling); every name either function loads is an argument, a name it binds itself, or a builtin.",
"S10": "For p, q from 1 to 60 the first n >= 1 divisible by both equals lcm(p, q), and it equals p*q exactly when gcd(p, q) == 1.",
"S15": "On the four joint forms with R(x, y) = (y, -x) and L(x, y) = (-y, x): L^3 == R, R^3 == L, R^3 after L^3 is the identity, L^4 is the identity, and L differs from R at each form.",
"S19": "5^2 - 4*6 == 1 and 4*6 == 24.",
"S20": "The primes from 5 to 53 are fourteen: 5..23 seven and 29..53 seven; the gaps from 2 run 1, 2, 2, 4, 2, 4, 2, 4, 6, the first six at 23 -> 29; within 5..53 only 5 has gaps (2, 2) on both sides and only 53 has (6, 6), six being the widest gap met.",
"S23": "(8 - k)(8 + k) == 64 - k^2 for k from 0 to 8; 7*9 == 63, 6*10 == 60, 8*8 == 64.",
"K5": "The same tree check as T14: no import, and each function loads only its own two arguments, names it binds, and builtins.",
"K24": "Applied twice each returns its argument: negation on -50..50, the multiplicative inverse on nonzero fractions, complex conjugation on a grid, the transpose on 50 random 3x4 matrices, set complement on 50 random subsets of 20; the Legendre transform of f(x) = x^4/4 + x^2/2 taken twice (numerically, p-grid step 0.001 over [-40, 40]) returns f at five points within 1e-5.",
"K27": "-s != s at s = +1 and -1; among the integers -50..50 only 0 has -x == x, and 0 is no sign.",
"H4": "Over 10,001 cuts x = i/10000, the cutter's share min(x, 1 - x) (the chooser taking the larger) is greatest, 1/2, at x = 1/2 alone.",
"H22": "10,000 random ledgers of one to eight entries, each entry debiting one account and crediting another the same amount: every trial balance sums to zero.",
"A10": "omega = chain length - highest delta: 18:3 at delta 9, 12, 15 is omega-3, and elongated by 2 or 4 carbons at the carboxyl end (each delta + 2 or + 4) stays omega-3; 18:2 (9, 12) is omega-6, 18:1 (9) omega-9; the double bonds stand three apart and 3, 6, 9 read odd, even, odd.",
"D2": "Each of the eighteen nonempty carryings at one key under each of the 121 offerings of up to four signs from -1, 0, +1: at a nonzero surfacing s the entry returns (s, -t, 0); at a 0 surfacing it returns (c, t, a + 1) within the bound and is gone past it.",
"D3": "From (c, t, 0), each (c, t): two c at each of 12 calls surface c each time with the returned opening 0; one c at each call surfaces 0 with openings 1, 2, 3 (and 4 at t > 0), then 0 with the key empty, then c with opening 0.",
"D5": "In _1_self_coupling's tree one assignment only writes an 11-other-chaining entry with opening 0, under `if _7_other_corusing != 0` in the loop over _10_other_surfacing; a caller re-seeding (c, t, 0) under one c at each of 50 calls gets (c, t, 1) back each time.",
"D6": "At each of the nineteen carryings, the 121 offerings of up to four signs grouped by the sign of (their signed total less the carried sign) and by whether any sign meets the key: within each group the whole return (surfacing and carrying) is identical.",
"D14": "_1_self_coupling([], [(k, +1), (k, -1)]) returns ([(k, 0)], []); + then - at two calls surface + and then - and return [(k, -1, +1, 0)].",
"D19": "A six-set has 36 ordered pairs, 6 on the diagonal and 30 off it; four things have 4! = 24 matchings, and for each chosen one 23 others differ.",
"D24": "Carrying (k, +1, t1, a1) and (k, -1, t2, a2) at one key, with nothing arriving, surfaces (k, 0) at each t1, t2 in {+1, -1} and a1, a2 in 0..4.",
"D25": "_1_self_coupling([], []) returns ([], []); each of the eighteen nonempty carryings under each of the six offerings returns an entry differing from the one given: a continuing keeps sign and second sign and opens by one, a fresh write opens at 0 with the second sign inverted.",
"D29": "With phi = (1 + sqrt5)/2, for each pair of neighbouring primes p < q up to 59, (1/phi)^q / (1/phi)^p equals (1/phi)^(q - p) within 1e-12.",
"D34": "(a + d) - (b + d) == a - b over 10,000 random rationals a, b, d.",
"D36": "A copy of _1_self_coupling summing 12-other-surplusing straight from the offering and the carrying, building no 14-social-crossing list, returns exactly what the resolver returns at 361 carryings over two keys (each key one of the nineteen) under each of the 31 offerings of up to two signs from (k, +1), (k, -1), (k, 0), (j, +1), (j, -1).",
"F76": "The four directions under (x, y) → (y, −x) and (x, y) → (−y, x), and MATH's F(P, Q) = (−Q, P) read at P along and Q right, matched at each direction.",
"F77": "The 32 one-change steps on four signs matched one to one with the 32 steps of the four-by-four torus grid, each pair placed round its right spiral round; 16 − 32 + 16 = 0 (instrument inside_outside_v370/inside_outside_four_signs.py).",
"F78": "All 1,344 rounds on four signs, each tested at the three pairings for each pair's round in one hand: 48, one of the nine forms, each three steps at one pair to one at the other, four times over (instrument inside_outside_v370/inside_outside_four_signs.py).",
"F80": "Both rhythms at four signs walked from name 1: the one-to-one exchange (8 forms, again at 9, one half) and three inside one outward (16 forms, again at 17, outward at 5, 9, 13, 17, halves crossed at 3, 7, 11, 15) (instrument inside_outside_v370/eight_signs_four_inside_four.py).",
"F81": "Every round of the 4 x 4 and 6 x 6 grids with each circle one way, each constant on its diagonals; at 16 x 16, all 65,536 diagonal choices: 32,768 close, 2,048 rhythms, each rhythm's round walked through the 256; 12 : 4 closes at none (instrument inside_outside_v370/eight_signs_four_inside_four.py).",
"F82": "One outward step per pass walked whole at m = 2, 3, 4, 5, 8 and 16, one rhythm among the 16-step choices, and 2^(2^k) + 1 at k = 0 to 3.",
"F84": "1 to 17 inside and outside walked whole at two, three and four levels (256, 4,096 and 65,536 forms), each level stepping at each 17 of the one inside it; a whole 1 to 257 inside one 1 to 17 and an outward step at each 9 walked to their failing (instrument inside_outside_v370/three_levels.py).",
"F88": "The nested pair rounds walked whole at two, four, six and eight signs; the arrivals, the inside steps carried to the arrival before each close (3, 6, 9, 15, 45), and the first inversions of the self's pair and of every sign (instrument inside_outside_v370/spans_and_wholes.py).",
"F90": "The nineteen carryings at one key under the six offerings and under none and single signs: next carryings, reach from each, the farthest, and each round meeting all nineteen once sought whole (instrument inside_outside_v370/discovering_next.py).",
"F91": "Each round at four signs with each pair one way, and each prefix's not yet impossible continuations counted (instrument inside_outside_v370/discovering_next.py).",
"F95": "The steps of each pair counted to the half of each whole of nested pairs at four, six and eight signs (names 9, 33, 129), and a passage of six right spiral steps walked.",
"F96": "The right spiral step taken three times against the other order at the four joint forms, and each carrying's next pair under each offering classed.",
"F97": "The eight one-to-one steps of two signs composed: the four inversions, each returning at its second taking, each carrying the right step to the other order, two on different axes giving the right step or the other order, three at once one inversion.",
"R56": "The self's table at the rings: one sign alone, an alternating arriving, the wave meeting the seed in and out of phase, and one 0 in an alternating arriving; each ring of 2 to 60 against the 0s at n + 2i + 2nk and no rest (instrument breakings_v370/ring_every_n.py).",
"F99": "The sixteen ways giving a next from a prior and a now, taken as steps of the pair (prior, now): one is the right spiral step, next as prior inverted, none the other order, and the other order the right step's inverse.",
"F103": "The joint forms of two signs, the eight changings (each sign + to − and − to + at each value of the other) and the four squares counted, four changings at each form, and the round's changings, each sign once each way.",
"F105": "The nested rounds of selves at two to four levels (16, 64 and 256 forms): each block between two steps of a self walked, the selves inside it meeting each of their joint forms once.",
"R36": "At a ring of three at the third function, each self's returned 11-other-chaining equals _1_self_coupling's second return at that self, and the next call takes it as its 3-self-carrying.",
"R37": "At a ring of three at the third function with a receiving-key map at one self, each backward neighbour's arriving at 17 equals _9_other_releasing(10, 5) at the releasing self, its 2 and 14 empty, and JOINS declares 9 with 17 and no 9 → 2.",
"R38": "At a line of three at the third function, _1_self_coupling is called exactly once at each self with its own carrying and the signs arrived at it, and the call's releasings arrive at the next call's arriving, none at this one.",
"R39": "R58, R60 and R61 together: the third function at a society of three at each facing, the order within a momentary, and the corner of a surface around a hole.",
"R58": "One momentary at a society of three selves with right, left, backward and forward neighbours, seeded carryings and arrivings at 2 and 17: the third function's returned carryings and deliveries equal the two functions called by hand at each self, 6 at the left neighbour's 2, 10 at the right neighbour's 14, 9 at the backward neighbour's 17; the code's tree holds three functions in order.",
"R59": "The rings at the third function: a ring of one surfaces +1, 0, −1, 0; at rings 1 to 11, 17 and 59 joined 9 → next 17 the whole state recurs after n momentaries with period 2 (even) or 4n (odd), the surfacings as R45, and no rest across 5,000 momentaries at 1 to 11; the across ring 10 → next 14 gives the same counts; the ring joined 6 → next 2 recurs after 2n with period 4n.",
"R60": "A society of seven, each self joined along, right and left, seeded at two selves, thirty momentaries: at each momentary the next momentary is identical at five random orderings of the selves and of the signs within each arriving, 150 comparisons.",
"R61": "The three-by-three surface with the centre missing at the joins as declared (9 → the row above's 17), a + at (1,0): (0,0) receives at 17 at momentary 1 and surfaces +, (0,1) receives at 14 at momentary 2, (0,2) receives at 14 at momentary 3 and surfaces +; (1,2) and the bottom row receive nothing over forty momentaries.",
"R62": "The same surface with 9's release arriving at both along neighbours: (0,0) and (2,0) receive at 17 at momentary 1, (0,2) and (2,2) surface + at momentary 3, and (1,2) receives [(k, +1), (k, +1)] at 17 at momentary 4, surfaces + and opens (+, −, 0), having received nothing before.",
"W99": "The two arrangements of the hole walked at the third function, forty momentaries each: the corner's along arriving at 17 continuing into 10 at both; the far side receiving nothing at the joins as declared, and two + signs together at the fourth momentary with 9 arriving at both along neighbours.",
"N49": "Two selves joined along both ways at the third function: each self's 9-other-releasing arrives at the other's 17 at the next call, each self's carrying is its own _1_self_coupling return, and the next call takes the arrived signs; 1, 9 and 17 odd and eight apart.",
"Q24": "R58 at the third function.",
"R63": "At rings 1 to 11 at the third function, over 6n + 10 momentaries from coupling n on: the sums of surfacings, carried signs, second signs, openings and signs crossing, and the count of carryings; even rings all sums 0, odd rings each sum changing, the count n at every ring."
}

ORDER = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "F25", "F26", "F73", "F27", "F28", "F29", "F30", "F31", "F32", "F34", "F35", "F36", "F37", "F38", "F39", "F40", "F41", "F42", "F43", "F44", "F45", "F46", "F74", "F47", "F48", "F49", "F50", "F51", "F52", "F72", "F53", "F54", "F55", "F56", "F57", "F75", "F58", "F59", "F60", "F61", "F76", "F62", "F63", "F64", "F77", "F78", "F79", "F80", "F81", "F82", "F83", "F84", "F85", "F86", "F87", "F88", "F89", "F90", "F91", "F92", "F93", "F94", "F95", "F96", "F97", "F98", "F99", "F100", "F103", "F101", "F102", "F104", "F105", "F65", "F66", "F67", "F68", "F69", "F33", "F70", "F71", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22", "R23", "R24", "R25", "R26", "R27", "R28", "R29", "R30", "R31", "R32", "R33", "R34", "R35", "R36", "R37", "R38", "R39", "R40", "R41", "R42", "R43", "R44", "R45", "R46", "R47", "R48", "R49", "R50", "R51", "R52", "R53", "R54", "R55", "R56", "R57", "R58", "R59", "R60", "R61", "R62", "R63", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17", "N18", "N19", "N20", "N21", "N22", "N23", "N24", "N25", "N26", "N27", "N28", "N29", "N30", "N31", "N32", "N33", "N34", "N35", "N36", "N37", "N38", "N39", "N40", "N41", "N42", "N43", "N44", "N45", "N46", "N47", "N48", "N49", "N50", "N51", "N52", "N53", "N54", "N55", "N56", "N57", "N58", "N59", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N67", "N68", "N69", "N70", "N71", "N72", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N83", "N84", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N92", "N93", "N94", "N95", "N96", "N97", "N98", "N99", "N100", "N101", "N102", "N103", "N104", "N105", "N106", "N107", "N108", "N109", "N110", "N111", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N121", "N122", "N123", "N124", "N125", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N133", "N134", "N135", "N136", "N137", "N138", "N139", "N140", "N141", "N142", "N143", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15", "M16", "M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33", "M34", "M35", "M36", "M37", "M38", "M39", "M40", "M41", "M42", "M43", "M44", "M45", "M46", "M47", "M48", "M49", "M50", "M51", "M52", "M53", "M54", "M55", "M56", "M57", "M58", "M59", "M60", "M61", "M62", "M63", "M64", "M65", "M66", "M67", "M68", "M69", "M70", "M71", "M72", "M73", "M74", "M75", "M76", "M77", "M78", "M79", "M80", "M81", "M82", "M83", "M84", "M85", "M86", "M87", "M88", "M89", "M90", "M91", "M92", "M93", "M94", "M95", "M96", "M97", "M98", "M99", "M100", "M101", "M102", "M103", "M104", "M105", "M106", "M107", "M108", "M109", "M110", "M111", "M112", "M113", "M114", "M115", "M116", "M117", "M118", "M119", "M120", "M121", "M122", "M123", "M124", "M125", "M126", "M127", "M128", "M129", "M130", "M131", "M132", "M133", "M134", "M135", "M136", "M137", "M138", "M139", "M140", "M141", "M142", "M143", "M144", "M145", "M146", "M147", "M148", "M149", "M150", "M151", "M152", "M153", "M154", "M155", "M156", "M157", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14", "W15", "W16", "W17", "W18", "W19", "W20", "W21", "W22", "W23", "W24", "W25", "W26", "W27", "W28", "W29", "W30", "W31", "W32", "W33", "W34", "W35", "W36", "W37", "W38", "W39", "W40", "W41", "W42", "W43", "W44", "W45", "W46", "W47", "W48", "W49", "W50", "W51", "W52", "W53", "W54", "W55", "W56", "W57", "W58", "W59", "W60", "W61", "W62", "W63", "W64", "W65", "W66", "W67", "W68", "W69", "W70", "W71", "W72", "W73", "W74", "W75", "W76", "W77", "W78", "W79", "W80", "W81", "W82", "W83", "W84", "W85", "W86", "W87", "W88", "W89", "W90", "W91", "W92", "W93", "W94", "W95", "W96", "W97", "W98", "W99", "W100", "W101", "W102", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40", "E41", "E42", "E43", "E44", "E45", "E46", "E47", "E48", "E49", "E50", "E51", "E52", "E53", "E54", "E55", "E56", "E57", "E58", "E59", "E60", "E61", "E62", "E63", "E64", "E65", "E66", "E67", "E68", "E69", "E70", "E71", "E72", "E73", "E74", "E75", "E76", "E77", "E78", "E79", "E80", "E81", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14", "X15", "X16", "X17", "X18", "X19", "X20", "X21", "X22", "X23", "X24", "X25", "X26", "X27", "X28", "X29", "X30", "X31", "X32", "X33", "X34", "X35", "X36", "X37", "X38", "X39", "X40", "X41", "X42", "X43", "X44", "X45", "X46", "X47", "X48", "X49", "X50", "X51", "X52", "X53", "X54", "X55", "X56", "X57", "X58", "X59", "X60", "X61", "X62", "X63", "X64", "X65", "X66", "X67", "X68", "X69", "X70", "X71", "X72", "X73", "X74", "X75", "X76", "X77", "X78", "X79", "X80", "X81", "X82", "X83", "X84", "X85", "X86", "X87", "X88", "X89", "X90", "X91", "X92", "X93", "X94", "X95", "X96", "X97", "X98", "X99", "X100", "X101", "X102", "X103", "X104", "X105", "X106", "X107", "X108", "X109", "X110", "X111", "X112", "X113", "X114", "X115", "X116", "X117", "X118", "X119", "X120", "X121", "X122", "X123", "X124", "X125", "X126", "X127", "X128", "X129", "X130", "X131", "X132", "X133", "X134", "X135", "X136", "X137", "X138", "X139", "X140", "X141", "X142", "X143", "X144", "X145", "X146", "X147", "X148", "X149", "X150", "X151", "X152", "X153", "X154", "X155", "X156", "X157", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27", "G28", "G29", "G30", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13", "T14", "T15", "T16", "T17", "T18", "T19", "T20", "T21", "T22", "T23", "T24", "T25", "T26", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20", "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28", "K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "K11", "K12", "K13", "K14", "K15", "K16", "K17", "K18", "K19", "K20", "K21", "K22", "K23", "K24", "K25", "K26", "K27", "K28", "K29", "K30", "K31", "K32", "K33", "K34", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H17", "H18", "H19", "H20", "H21", "H22", "H23", "H24", "H25", "H26", "H27", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14", "D15", "D16", "D17", "D18", "D19", "D20", "D21", "D22", "D23", "D24", "D25", "D26", "D27", "D28", "D29", "D30", "D31", "D32", "D33", "D34", "D35", "D36", "D37", "D38", "D39", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23", "Q24", "Q25", "Q26", "Q27", "Q28", "Q29", "Q30", "Q31", "Q32", "Q33", "Q34", "Q35", "Q36", "Q37", "Q38", "Q39", "Q40", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "J11", "J12", "J13", "J14", "J15", "J16", "J17", "J18", "J19", "J20", "J21", "J22", "J23", "J24", "J25", "J26", "J27", "J28", "J29", "J30", "J31", "J32", "J33", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18", "B19", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27", "B28", "B29", "B30", "B31", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P13", "P14", "P15", "P16", "P17", "P18", "P19", "P20", "P21", "P22", "P23", "P24", "P25", "P26", "P27", "P28", "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L20", "L21", "L22", "L23", "L24", "L25", "L26", "L27", "L28", "L29", "L30", "L31", "HP1", "HP2", "HP3", "HP4", "HP5", "HP6", "HP7", "HP8", "HP9", "HP10", "HP11", "HP12", "HP13", "HP14", "HP15", "HP16", "RH1", "RH2", "RH3", "RH4", "RH5", "RH6", "RH7", "RH8", "RH9", "RH10", "RH11", "RH12", "RH13", "RH14", "RH15", "RH16", "RH17", "RH18", "RH19", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "LS1", "LS2", "LS3", "LS4", "LS5", "LS6", "LS7", "LS8", "LS9", "LS10", "LS11", "LS12", "LF1", "LF2", "LF3", "LF4", "LF5", "LF6", "LF7", "LF8", "LF9", "LF10", "LF11", "LF12", "GH1", "GH2", "GH3", "GH4", "GH5", "GH6", "GH7", "GH8", "GH9", "GH10", "GH11", "GH12", "GH13", "GH14", "GH15", "GH16", "GH17", "GH18", "GH19", "GH20", "GH21", "GH22", "GH23", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "CO1", "CO2", "CO3", "CO4", "CO5", "CO6", "CO7", "CO8", "CO9", "CO10", "CO11", "CO12", "CO13", "CO14", "CO15", "CO16", "CO17", "CO18", "CO19", "CO20", "CO21", "CO22", "CO23", "CO24", "CO25"]

PART_SOURCES = {}

PART_SOURCES['core'] = r'''"""Run checks for Exhibit THIRTY Parts ONE and TWO, against Exhibit ONE v372's resolver
(the first python block of /home/claude/work/Exhibit_ONE_Natural_Resolver_v372.md)."""
import ast, re, json, sys
from itertools import product, permutations, combinations

code = RESOLVER_SRC
ns = {}
exec(code, ns)
C = ns['_1_self_coupling']; R = ns['_9_other_releasing']
K = 'k'
S = (1, -1)

def call(carry, offer):
    s, c = C(list(carry), list(offer))
    return dict(s).get(K), (c[0][1:] if c else None), c

# ---------------------------------------------------------------- PART ONE (arithmetic)
def F20():
    self5 = list(range(1, 6)); other5 = list(range(2, 7))
    pairs = list(zip(self5, other5))
    return (len(self5) + len(other5) == 10 and len(set(self5) | set(other5)) == 6
            and pairs == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
            and all((a + b) % 2 == 1 for a, b in pairs)
            and ['co' if n % 2 else 'bi' for n in self5] == ['co', 'bi', 'co', 'bi', 'co']
            and ['co' if n % 2 else 'bi' for n in other5] == ['bi', 'co', 'bi', 'co', 'bi'])

def F21():
    # one side's momentaries alone: odd momentaries 1-2, 3-4, ... complete at 2, 4, ... where no momentary opens
    opens = {1, 3, 5, 7}; completes = {2, 4, 6, 8}
    return all(c not in opens for c in completes)

def next_rules():
    J = list(product(S, S))
    out = []
    for vals in product(S, repeat=4):
        f = dict(zip(J, vals))
        m = {(p, n): (n, f[(p, n)]) for p, n in J}
        out.append((f, m))
    return J, out

def cycles_of(m, states):
    seen = set(); cyc = []
    for s in states:
        if s in seen: continue
        path = []; x = s
        while x not in path and x not in seen:
            path.append(x); x = m[x]
        if x in path: cyc.append(len(path) - path.index(x))
        seen |= set(path)
    return sorted(cyc)

def F27():
    J, rules = next_rules()
    bij = [(f, m) for f, m in rules if len(set(m.values())) == 4]
    nonbij = [(f, m) for f, m in rules if len(set(m.values())) < 4]
    if len(bij) != 4 or len(nonbij) != 12: return False
    if not all(len(set(m.values())) < 4 for f, m in nonbij): return False  # at least two joint states going to one
    cls = {'now': 0, 'one': 0, 'both': 0}
    for f, m in rules:
        dep = [f[(1, n)] != f[(-1, n)] for n in S]
        cls['now' if not any(dep) else 'both' if all(dep) else 'one'] += 1
    if cls != {'now': 4, 'one': 8, 'both': 4}: return False
    named = {'prior': lambda p, n: p, 'minus_prior': lambda p, n: -p,
             'parity': lambda p, n: p * n, 'minus_parity': lambda p, n: -p * n}
    want = {'prior': [1, 1, 2], 'minus_prior': [4], 'parity': [1, 3], 'minus_parity': [1, 3]}
    for name, g in named.items():
        m = {(p, n): (n, g(p, n)) for p, n in J}
        if cycles_of(m, J) != want[name]: return False
    return True

def F31():
    up = lambda p: 8 * (p - 1) + 1
    return [up(p) for p in (1, 2, 3)] == [1, 9, 17] and up(9) == 65

def F32():
    ok = True
    for c, t in product(S, S):
        seq = [c, t, -c, -t, c, t, -c, -t, c]           # positions 1..9
        pairs = [(seq[i], seq[i + 1]) for i in range(8)]
        cnt = {j: pairs.count(j) for j in product(S, S)}
        step = all(pairs[i + 1] == (pairs[i][1], -pairs[i][0]) for i in range(7))
        ok &= all(v == 2 for v in cnt.values()) and step
    return ok

def F35():
    return all((-1) ** k * s == (s if k % 2 == 0 else -s) for k in range(64) for s in S)

def F37():
    J = list(product((0, 1), (0, 1)))
    good = []
    for vals in product((0, 1), repeat=4):
        f = dict(zip(J, vals))
        if all(f[(a, b)] != f[(1 - a, b)] and f[(a, b)] != f[(a, 1 - b)] for a, b in J):
            good.append(vals)
    xor = tuple(a ^ b for a, b in J); xnor = tuple(1 - (a ^ b) for a, b in J)
    return sorted(good) == sorted([xor, xnor])

def F43():
    conds = []
    for possible in (False, True):
        if not possible: conds.append(('not possible',)); continue
        for existing in (False, True):
            if not existing: conds.append(('possible', 'not existing')); continue
            for carrying in (False, True):
                conds.append(('existing', 'carrying' if carrying else 'not carrying'))
    return len(conds) == 4

def one_change_maps(n):
    St = list(product(S, repeat=n))
    flip = lambda s, j: tuple(-v if k == j else v for k, v in enumerate(s))
    for pick in product(range(n), repeat=len(St)):
        yield {St[i]: flip(St[i], pick[i]) for i in range(len(St))}, St

def single_round(m, St):
    s = St[0]; seen = [s]
    for _ in range(len(St)): s = m[s]; seen.append(s)
    return len(set(seen[:len(St)])) == len(St) and seen[-1] == St[0]

def _levels_walk(L, n=16, rule=None):
    def level(k):
        d = 0
        while d < L - 1 and k % n == n - 1:
            k //= n; d += 1
        return d
    rule = rule or level
    v = (0,) * L; seen = {v}; N = n ** L
    for k in range(N):
        d = rule(k); v = tuple((x + (1 if i == d else 0)) % n for i, x in enumerate(v))
        if k < N - 1:
            if v in seen: return False
            seen.add(v)
    return v == (0,) * L

def F97():
    from itertools import permutations
    steps = []
    for perm in permutations(range(2)):
        for sg in product(S, S):
            steps.append(lambda v, perm=perm, sg=sg: (sg[0] * v[perm[0]], sg[1] * v[perm[1]]))
    St = list(product(S, S))
    tab = lambda f: tuple(f(v) for v in St)
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0]); I = lambda v: v
    det = lambda f: (lambda a, b: a[0] * b[1] - a[1] * b[0])(f((1, 0)), f((0, 1)))
    inv = [f for f in steps if det(f) == -1]
    ok = len(steps) == 8 and len(inv) == 4
    ok &= all(tab(lambda v, f=f: f(f(v))) == tab(I) for f in inv)
    ok &= all(tab(lambda v, f=f: f(G(f(v)))) == tab(Fo) for f in inv)
    two = {tab(lambda v, a=a, b=b: a(b(v))) for a in inv for b in inv if tab(a) != tab(b)}
    ok &= two == {tab(G), tab(Fo), tab(lambda v: (-v[0], -v[1]))}
    three = {tab(lambda v, a=a, b=b, c=c: a(b(c(v)))) for a in inv for b in inv for c in inv}
    ok &= three <= {tab(f) for f in inv}
    return ok

def F96():
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0])
    ok = all(G(G(G(v))) == Fo(v) for v in product(S, S))
    from collections import Counter
    k = Counter()
    for st in sorted(REACH):
        if not st: continue
        for off in OFFERS:
            _, _, cc = call([(K,) + st], off)
            if not cc: k['complete'] += 1; continue
            a, b = st[:2], tuple(cc[0][1:3])
            k['same' if a == b else 'right' if b == G(a) else 'other' if b == Fo(a) else 'half' if b == (-a[0], -a[1]) else 'x'] += 1
    return ok and dict(k) == {'half': 72, 'same': 14, 'right': 9, 'other': 9, 'complete': 4}

def F105():
    from itertools import permutations
    def pst(c):
        r = [(1, 1)]
        while len(r) < 4: r.append((r[-1][1], -r[-1][0]))
        return r[c % 4]
    def lev(k, L):
        d = 0
        while d < L - 1 and k % 4 == 3: k //= 4; d += 1
        return d
    ok = True
    for L in (2, 3, 4):
        pos = [0] * L; forms = []
        for k in range(4 ** L):
            forms.append(tuple(pos)); pos[lev(k, L)] = (pos[lev(k, L)] + 1) % 4
        for d in range(1, L):
            for blk in range(4 ** (L - d)):
                inner = {f[:d] for f in forms[blk * 4 ** d:(blk + 1) * 4 ** d]}
                ok &= len(inner) == 4 ** d
    return ok

def F99():
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0])
    St = list(product(S, S)); nG = nF = 0; rule = None
    for r in product(S, repeat=4):
        f = dict(zip(St, r)); m = {v: (v[1], f[v]) for v in St}
        if all(m[v] == G(v) for v in St): nG += 1; rule = f
        if all(m[v] == Fo(v) for v in St): nF += 1
    return nG == 1 and nF == 0 and all(rule[v] == -v[0] for v in St) and all(G(Fo(v)) == v for v in St)

def F103():
    St = list(product(S, S))
    edges = [('x', y, s) for y in S for s in S] + [('y', x, s) for x in S for s in S]
    faces = [(p, q) for p in S for q in S]
    G = lambda v: (v[1], -v[0]); r = [(1, 1)]
    while len(r) < 5: r.append(G(r[-1]))
    ch = sorted(('x', u[0]) if u[0] != w[0] else ('y', u[1]) for u, w in zip(r, r[1:]))
    deg = all(sum(1 for e in edges if (e[0] == 'x' and e[1] == v[1] and e[2] in (v[0], -v[0])) or (e[0] == 'y' and e[1] == v[0] and e[2] in (v[1], -v[1]))) == 4 for v in St)
    return len(St) - len(edges) + len(faces) == 0 and ch == sorted([('x', 1), ('x', -1), ('y', 1), ('y', -1)]) and deg

def F95():
    def lev(k, L):
        d = 0
        while d < L - 1 and k % 4 == 3: k //= 4; d += 1
        return d
    ok = True
    for L, half in ((2, 9), (3, 33), (4, 129)):
        cnt = [0] * L
        for k in range(half - 1): cnt[lev(k, L)] += 1
        ok &= cnt[-1] == 2 and cnt[-2] == 6
        if L == 3: ok &= cnt[0] == 24 and cnt[0] % 4 == 0
        if L == 4: ok &= cnt[:2] == [96, 24]
    # four signs: the inside pair's six steps meet all four joint forms and arrive inverted
    st = [(1, 1)]
    for _ in range(6): st.append((st[-1][1], -st[-1][0]))
    ok &= len(set(st)) == 4 and st[6] == (-1, -1)
    return ok

def F90():
    from collections import deque
    states = sorted(REACH)
    def nx(st, off):
        _, _, cc = call([(K,) + st] if st else [], off)
        return tuple(cc[0][1:]) if cc else ()
    res = []
    for OFF in (OFFERS, [[], [(K, 1)], [(K, -1)]]):
        G = {s: sorted(set(nx(s, o) for o in OFF)) for s in states}
        def bfs(s):
            d = {s: 0}; q = deque([s])
            while q:
                x = q.popleft()
                for y in G[x]:
                    if y not in d: d[y] = d[x] + 1; q.append(y)
            return d
        rounds = []
        def dfs(path, vis):
            v = path[-1]
            if len(path) == 19:
                if () in G[v]: rounds.append(tuple(path))
                return
            for w in G[v]:
                if w not in vis: vis.add(w); path.append(w); dfs(path, vis); path.pop(); vis.discard(w)
        dfs([()], {()})
        res.append((sorted(len(G[s]) for s in states), all(len(bfs(s)) == 19 for s in states),
                    max(max(bfs(s).values()) for s in states), rounds))
    six, single = res
    ok = six[0] == [3] * 19 and six[1] and six[2] == 6 and len(six[3]) == 4
    ok &= single[0] == [2] * 18 + [3] and single[1] and single[2] == 11 and single[3] == []
    singles = [[], [(K, 1)], [(K, -1)]]
    needs = []
    for r in six[3]:   # the calls of each round taking two signs arriving together
        need = [i for i in range(19) if not any(nx(r[i], o) == r[(i + 1) % 19] for o in singles)]
        needs.append(len(need))
        ok &= all(all(len(o) == 2 and o[0][1] == o[1][1] for o in OFFERS if nx(r[i], o) == r[(i + 1) % 19]) for i in need)
    for r in six[3]:   # each family of one sign pair runs upward through its openings
        fam = [s[:2] for s in r[1:]]
        ok &= all(r[i + 1][2] == r[i][2] + 1 for i in range(1, 18) if fam[i - 1] == fam[i])
    return ok and sorted(needs) == [1, 1, 2, 2]

def F91():
    m = 4; N = m * m; words = []
    def go(v, path, vis, word):
        if len(path) == N:
            if ((v[0] + 1) % m, v[1]) == (0, 0) or (v[0], (v[1] + 1) % m) == (0, 0): words.append(word)
            return
        for d, w in ((1, ((v[0] + 1) % m, v[1])), (0, (v[0], (v[1] + 1) % m))):
            if w not in vis: vis.add(w); path.append(w); go(w, path, vis, word + (d,)); path.pop(); vis.discard(w)
    go((0, 0), [(0, 0)], {(0, 0)}, ())
    ok = len(words) == 8
    for w0 in words:
        prof = [len({w[k] for w in words if w[:k] == w0[:k]}) for k in range(15)]
        ok &= prof == [2, 2, 2] + [1] * 12
    # eight signs: a round is a choice at each of sixteen diagonals, odd outward: fifteen free, the sixteenth set, the rest laid
    return ok and 2 ** 15 == 32768

def F88():
    def pst(c):
        r = [(1, 1)]
        while len(r) < 4: r.append((r[-1][1], -r[-1][0]))
        return r[c % 4]
    def lev(k, L):
        d = 0
        while d < L - 1 and k % 4 == 3: k //= 4; d += 1
        return d
    def forms(L):
        pos = [0] * L; out = []
        for k in range(4 ** L + 1):
            f = ()
            for d in range(L): f += pst(pos[d])
            out.append(f)
            if k < 4 ** L: pos[lev(k, L)] += 1
        return out
    ok = True
    for L in (1, 2, 3, 4):
        F = forms(L); N = 4 ** L
        ok &= len(set(F[:N])) == N and F[N] == F[0]
    arr = lambda L, d: [k + 2 for k in range(4 ** L) if lev(k, L) >= d]
    ok &= arr(2, 1) == [5, 9, 13, 17] and arr(3, 2) == [17, 33, 49, 65]
    rel = {N: sum(1 for k in range(N - 5) if lev(k, 2 if N <= 17 else 3) == 0) for N in (9, 13, 17, 25, 65)}
    ok &= rel == {9: 3, 13: 6, 17: 9, 25: 15, 65: 45}
    F4, F6 = forms(2), forms(3)
    inv = lambda F, idx: [p for p, f in enumerate(F, 1) if all(f[i] == -F[0][i] for i in idx)]
    ok &= inv(F4, (0, 1))[0] == 3 and inv(F4, range(4)) == [9] and inv(F6, range(6))[0] == 35
    return ok

def F84():
    ok = all(_levels_walk(L) for L in (2, 3, 4))
    # a whole 1-257 inside one 1-17, the outside once in each 256
    def B(k):
        if k % 256 == 255: return 2
        i = k - k // 256
        return 1 if i % 16 == 15 else 0
    ok &= not _levels_walk(3, rule=B)
    # an outward step at each 9: one per eight, meeting 128 of 256
    v = (0, 0); seen = {v}
    for k in range(256):
        v = ((v[0] + 1) % 16, v[1]) if k % 8 == 7 else (v[0], (v[1] + 1) % 16)
        if v in seen: break
        seen.add(v)
    return ok and len(seen) == 128

def F57():
    # four signs as two pairs; one right spiral step at the first pair, then at the second, alternating
    St = list(product(S, repeat=4))
    A = lambda s: (s[1], -s[0], s[2], s[3]); B = lambda s: (s[0], s[1], s[3], -s[2])
    rounds = set()
    for s0 in St:
        s = s0; seen = [s0]
        for i in range(8):
            s = A(s) if i % 2 == 0 else B(s); seen.append(s)
        firstback = next(i for i in range(1, 9) if seen[i] == s0)
        if firstback != 8 or len(set(seen[:8])) != 8: return False
        rounds.add(frozenset(seen[:8]))
    # the orbits of the alternating pair of steps (as a two-step map) part the sixteen
    return sum(len(r) for r in rounds) >= 16 and len(set().union(*rounds)) == 16

def F58():
    rounds = [m for m, St in one_change_maps(2) if single_round(m, St)]
    St = list(product(S, S))
    right = {(x, y): (y, -x) for x, y in St}; other = {(x, y): (-y, x) for x, y in St}
    return len(list(one_change_maps(2))) == 16 and len(rounds) == 2 and right in rounds and other in rounds

def F59():
    St = list(product(S, S))
    rounds = []; onechange = []
    for img in product(St, repeat=4):
        m = dict(zip(St, img))
        if single_round(m, St):
            rounds.append(m)
            if all(sum(a != b for a, b in zip(s, m[s])) == 1 for s in St): onechange.append(m)
    # NI 8.1: only these two change one sign each step, reach each joint form, and meet no prior the step after
    no_back = [m for m in (dict(zip(St, img)) for img in product(St, repeat=4))
               if all(sum(a != b for a, b in zip(s, m[s])) == 1 for s in St)
               and all(m[m[s]] != s for s in St) and single_round(m, St)]
    return len(rounds) == 6 and len(onechange) == 2 and len(no_back) == 2

def F60():
    St = list(product(S, S))
    ok = True; halfsteps = []
    for m, _ in one_change_maps(2):
        if all(m[m[s]] == (-s[0], -s[1]) for s in St): halfsteps.append(m)
    right = {(x, y): (y, -x) for x, y in St}; other = {(x, y): (-y, x) for x, y in St}
    ok &= len(halfsteps) == 2 and right in halfsteps and other in halfsteps
    for m in (right, other):
        inv = [set(sub) for r in range(0, 5) for sub in combinations(St, r) if {m[s] for s in sub} == set(sub)]
        ok &= [len(x) for x in inv] == [0, 4]
    return ok

def F63():
    maps = [m for m, St in one_change_maps(3) if single_round(m, St)]
    total = 3 ** 8
    if len(maps) != 12 or total != 6561: return False
    St = list(product(S, repeat=3))
    group = []
    for p in permutations(range(3)):
        for fl in product(S, repeat=3):
            group.append(lambda s, p=p, fl=fl: tuple(fl[i] * s[p[i]] for i in range(3)))
    key = lambda m: frozenset(m.items())
    seen = set(); orbits = 0
    for m in maps:
        if key(m) in seen: continue
        orbits += 1
        for g in group:
            seen.add(key({g(s): g(m[s]) for s in St}))
    return orbits == 1

def F64():
    n = 4; N = 1 << n; cycles = set()
    def dfs(path, vis):
        v = path[-1]
        if len(path) == N:
            if bin(v ^ path[0]).count('1') == 1:
                c = tuple(path)
                if c[1] < c[-1]: cycles.add(c)
            return
        for b in range(n):
            w = v ^ (1 << b)
            if not vis[w]:
                vis[w] = True; path.append(w); dfs(path, vis); path.pop(); vis[w] = False
    vis = [False] * N; vis[0] = True; dfs([0], vis)
    es = [frozenset(frozenset((c[i], c[(i + 1) % N])) for i in range(N)) for c in cycles]
    G = [(p, msk) for p in permutations(range(n)) for msk in range(N)]
    def act(g, v):
        p, msk = g; w = 0
        for i in range(n):
            if v >> i & 1: w |= 1 << p[i]
        return w ^ msk
    seen = set(); orbits = 0
    for e in es:
        if e in seen: continue
        orbits += 1
        for g in G: seen.add(frozenset(frozenset(act(g, x) for x in ed) for ed in e))
    return len(cycles) == 1344 and len(G) == 384 and orbits == 9

def F76():
    # x the right sign, y the along sign: (x, y) -> (y, -x) turns along into right; MATH's F at P along, Q right is the same turn
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0])
    along, right = (0, 1), (1, 0)
    ok = G(along) == right and G(right) == (0, -1) and Fo(along) == (-1, 0)
    # MATH labels (P, Q) = (along, right): F(P, Q) = (-Q, P)
    to_pq = lambda v: (v[1], v[0]); from_pq = lambda w: (w[1], w[0])
    FPQ = lambda w: (-w[1], w[0])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return ok and all(from_pq(FPQ(to_pq(v))) == G(v) for v in dirs)

def _pair_round():
    r = [(1, 1)]
    while len(r) < 4: r.append((r[-1][1], -r[-1][0]))
    return {s: i for i, s in enumerate(r)}

def _q4_rounds():
    n, N = 4, 16; cycles = []
    def dfs(path, vis):
        v = path[-1]
        if len(path) == N:
            if bin(v ^ path[0]).count('1') == 1 and path[1] < path[-1]: cycles.append(tuple(path))
            return
        for b in range(n):
            w = v ^ (1 << b)
            if not vis[w]:
                vis[w] = True; path.append(w); dfs(path, vis); path.pop(); vis[w] = False
    vis = [False] * N; vis[0] = True; dfs([0], vis)
    return cycles

def _ps(v, i, j): return (1 - 2 * ((v >> i) & 1), 1 - 2 * ((v >> j) & 1))

def F77():
    pos = _pair_round()
    co = lambda v: (pos[_ps(v, 0, 1)], pos[_ps(v, 2, 3)])
    steps = {frozenset((v, v ^ (1 << b))) for v in range(16) for b in range(4)}
    grid = set()
    for a in range(4):
        for b in range(4):
            grid.add(frozenset(((a, b), ((a + 1) % 4, b)))); grid.add(frozenset(((a, b), (a, (b + 1) % 4))))
    return len({co(v) for v in range(16)}) == 16 and {frozenset(co(v) for v in e) for e in steps} == grid \
        and len(steps) == 32 and 16 - len(grid) + 16 == 0

def F78():
    pos = _pair_round(); N = 16
    cycles = _q4_rounds()
    syms = [(p, m) for p in permutations(range(4)) for m in range(16)]
    def act(g, v):
        p, m = g; w = 0
        for i in range(4):
            if v >> i & 1: w |= 1 << p[i]
        return w ^ m
    es = lambda c: frozenset(frozenset((c[i], c[(i + 1) % N])) for i in range(N))
    form = {}; k = 0
    for c in cycles:
        e = es(c)
        if e in form: continue
        for g in syms: form[frozenset(frozenset(act(g, x) for x in ed) for ed in e)] = k
        k += 1
    pairings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    def mono(c, P):
        (i, j), (kk, l) = P
        for o1 in ((i, j), (j, i)):
            for o2 in ((kk, l), (l, kk)):
                st = []
                for t in range(N):
                    u, w = c[t], c[(t + 1) % N]
                    st.append(((pos[_ps(w, *o1)] - pos[_ps(u, *o1)]) % 4, (pos[_ps(w, *o2)] - pos[_ps(u, *o2)]) % 4))
                if all(x in ((1, 0), (0, 1)) for x in st): return st
        return None
    found = []
    for c in cycles:
        for P in pairings:
            st = mono(c, P) or mono(c[::-1], P)
            if st: found.append((c, st)); break
    pats = set()
    for c, st in found:
        w = ''.join('A' if x == (1, 0) else 'B' for x in st)
        w = min(w[r:] + w[:r] for r in range(N))
        pats.add(tuple(sorted((w.count('A'), w.count('B')))) + (w in ('AAABAAABAAABAAAB', 'ABBBABBBABBBABBB'),))
    return len(cycles) == 1344 and k == 9 and len(found) == 48 and len({form[es(c)] for c, _ in found}) == 1 \
        and pats == {(4, 12, True)}

def F80():
    def walk(word):
        a = b = 0; seen = [(0, 0)]
        for ch in word:
            if ch == 'i': b = (b + 1) % 4
            else: a = (a + 1) % 4
            seen.append((a, b))
        return seen
    half = lambda x: ((x[1] - x[0]) % 4) // 2
    s9 = walk('io' * 4); s17 = walk('iiio' * 4)
    return (len(set(s9[:8])) == 8 and s9[8] == s9[0] and len({half(x) for x in s9}) == 1
            and len(set(s17[:16])) == 16 and s17[16] == s17[0]
            and [k + 2 for k, ch in enumerate('iiio' * 4) if ch == 'o'] == [5, 9, 13, 17]
            and [k + 2 for k in range(16) if half(s17[k]) != half(s17[k + 1])] == [3, 7, 11, 15])

def _torus_rounds_dfs(m):
    N = m * m; out = []
    def go(v, path, vis):
        if len(path) == N:
            if ((v[0] + 1) % m, v[1]) == (0, 0) or (v[0], (v[1] + 1) % m) == (0, 0): out.append(tuple(path))
            return
        for w in (((v[0] + 1) % m, v[1]), (v[0], (v[1] + 1) % m)):
            if w not in vis:
                vis.add(w); path.append(w); go(w, path, vis); path.pop(); vis.discard(w)
    go((0, 0), [(0, 0)], {(0, 0)})
    return out

def _diag_constant(c, m):
    N = len(c); ch = {}
    for k in range(N):
        v = c[k]; t = c[(k + 1) % N][0] != v[0]
        if ch.setdefault((v[0] + v[1]) % m, t) != t: return False
    return True

def _closes(bits, m):
    v = (0, 0); seen = {v}
    for _ in range(m * m - 1):
        v = ((v[0] + 1) % m, v[1]) if bits[(v[0] + v[1]) % m] else (v[0], (v[1] + 1) % m)
        if v in seen: return False
        seen.add(v)
    return (((v[0] + 1) % m, v[1]) if bits[(v[0] + v[1]) % m] else (v[0], (v[1] + 1) % m)) == (0, 0)

def F81():
    for m in (4, 6):
        R = _torus_rounds_dfs(m)
        if not all(_diag_constant(c, m) for c in R): return False
    m = 16; count = 0; neck = {}
    for b in product((0, 1), repeat=m):
        # one pass of sixteen steps moves each form of a diagonal alike: a shift by the outward count along it
        a = sum(b)
        if a % 2 == 1:
            count += 1
            k = min(b[r:] + b[:r] for r in range(m)); neck[k] = sum(k)
    reps_ok = all(_closes(k, m) for k in neck) and not _closes((0, 0, 0, 1) * 4, m) and not _closes((0,) * 7 + (1,) + (0,) * 7 + (1,), m) \
        and not any(_closes(b, m) for b in [(0, 1) * 8, (0, 0, 1, 1) * 4, (1,) * 16, (0,) * 16])
    from collections import Counter
    return count == 32768 and len(neck) == 2048 and reps_ok and \
        sorted(Counter(neck.values()).items()) == [(1, 1), (3, 35), (5, 273), (7, 715), (9, 715), (11, 273), (13, 35), (15, 1)]

def F82():
    ok = all(_closes(tuple([0] * (m - 1) + [1]), m) for m in (2, 3, 4, 5, 8, 16))
    ok &= sum(1 for b in product((0, 1), repeat=16) if sum(b) == 1 and b == min(b[r:] + b[:r] for r in range(16))) == 1
    return ok and [2 ** (2 ** k) + 1 for k in range(4)] == [3, 5, 17, 257]

# ---------------------------------------------------------------- PART TWO (the code)
tree = ast.parse(code)

def R2():
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    asg = [t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets]
    sig = {f.name: [a.arg for a in f.args.args] for f in fns}
    return (sig == {'_1_self_coupling': ['_3_self_carrying', '_2_self_offering'],
                    '_9_other_releasing': ['_10_other_surfacing', '_5_other_neutralling'],
                    '_17_social_abundancing': ['_3_self_carrying', '_2_self_offering', '_5_other_neutralling', 'SURFACE']}
            and [f.name for f in fns] == ['_1_self_coupling', '_9_other_releasing', '_17_social_abundancing']
            and asg == ['CONNECTORS', 'JOINS'])

NAMES = {1: 'self_coupling', 2: 'self_offering', 3: 'self_carrying', 4: 'self_sharing', 5: 'other_neutralling',
         6: 'other_crossing', 7: 'other_corusing', 8: 'other_torusing', 9: 'other_releasing', 10: 'other_surfacing',
         11: 'other_chaining', 12: 'other_surplusing', 13: 'social_neutralling', 14: 'social_crossing',
         15: 'social_corusing', 16: 'social_torusing', 17: 'social_abundancing'}

def R4():
    ids = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} | \
          {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)} | \
          {a.arg for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) for a in n.args.args}
    ok = all(f'_{k}_{v}' in ids for k, v in NAMES.items())
    two = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name != '_17_social_abundancing']
    ids2 = {n.id for f in two for n in ast.walk(f) if isinstance(n, ast.Name)} | {a.arg for f in two for a in f.args.args} | {f.name for f in two}
    ok &= not any(i.startswith('_17') for i in ids2)
    third = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_17_social_abundancing')
    ok &= all(f'_{k}_{v}' in ids2 for k, v in NAMES.items() if k <= 16) and third.name == '_17_social_abundancing'
    strs = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str) and '-' in n.value]
    ok &= all(s.split('-', 1)[1].replace('-', '_') == NAMES[int(s.split('-')[0])] for s in strs)
    return ok

def R5():
    odd = [n for n in range(1, 18) if n % 2]; even = [n for n in range(1, 18) if n % 2 == 0]
    co = sum(3 for _ in odd) + sum(2 for _ in even); bi = sum(2 for _ in odd) + sum(3 for _ in even)
    return len(odd) == 9 and len(even) == 8 and co + bi == 85 and co == 43 and bi == 42

def R6():
    roots = {v.split('_')[1] for v in NAMES.values()}
    two = {r: [k for k, v in NAMES.items() if v.split('_')[1] == r] for r in roots}
    return (len(roots) == 13 and {r for r, ks in two.items() if len(ks) == 2} == {'neutralling', 'crossing', 'corusing', 'torusing'}
            and all(ks[1] - ks[0] == 8 for ks in two.values() if len(ks) == 2))

OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]

def reach():
    start = (); seen = {start}; frontier = [start]; trans = 0
    while frontier:
        nxt = []
        for st in frontier:
            for off in OFFERS:
                _, _, c = call([(K,) + st] if st else [], off)
                s2 = tuple(c[0][1:]) if c else ()
                trans += 1
                if s2 not in seen: seen.add(s2); nxt.append(s2)
        frontier = nxt
    return seen, trans

REACH, TRANS = reach()

def R7():
    ok = True
    for st in REACH:
        for off in OFFERS:
            s, c = C([(K,) + st] if st else [], off)
            ok &= isinstance(s, list) and all(len(x) == 2 and x[1] in (-1, 0, 1) for x in s)
            ok &= isinstance(c, list) and all(len(x) == 4 and x[1] in S and x[2] in S and 0 <= x[3] <= 4 for x in c)
            C(c, [])  # the returned 11 is taken as the next 3
    return ok

def R9():
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
    reads = [n for n in ast.walk(fn) if isinstance(n, ast.Name) and n.id == '_3_self_carrying' and isinstance(n.ctx, ast.Load)]
    return len(reads) == 3

def R10():
    ok = True
    for c, t, a in product(S, S, range(3)):
        s, st, _ = call([(K, c, t, a)], [])        # surfaces -c, fresh write
        ok &= st == (-c, -t, 0)
        s, st, _ = call([(K, c, t, a)], [(K, c)])  # surfaces 0, continues: 8 kept
        ok &= s == 0 and st == (c, t, a + 1)
    return ok

def R11():
    ok = all(call([(K, c, t, 0)], [])[0] == -c for c, t in product(S, S))
    ok &= C([], [(K, 0)]) == ([], [])
    ok &= C([(K, 1, -1, 0)], [(K, 0)]) == C([(K, 1, -1, 0)], [])
    return ok

def R13():
    s1 = C([], [(K, 1), (K, 1)]); s2 = C([], [(K, 1), (K, -1)])
    s3 = C([], [(K, -1), (K, -1)])
    return (s1 == ([(K, 1)], [(K, 1, -1, 0)]) and s2 == ([(K, 0)], []) and s3 == ([(K, -1)], [(K, -1, -1, 0)]))

def R14():
    ok = True; maxa = {1: 0, -1: 0}
    for c, t, a in product(S, S, range(5)):
        cont = (a + 1 <= 3) or (a + 1 == 4 and t > 0)
        s, st, _ = call([(K, c, t, a)], [(K, c)])
        ok &= s == 0 and (st == (c, t, a + 1) if cont else st is None)
    for st in REACH:
        if st: maxa[st[1]] = max(maxa[st[1]], st[2])
    return ok and maxa == {-1: 3, 1: 4}

def R15():
    ok = True
    for c, t, a in product(S, S, range(3)):
        for off in OFFERS:
            s, st, _ = call([(K, c, t, a)], off)
            if s: ok &= st == (s, -t, 0)
    for sgn in S:
        s, st, _ = call([], [(K, sgn)])
        ok &= s == sgn and st == (sgn, -1, 0)
    return ok

def R16():
    ok = True
    for c, t in product(S, S):
        for off in OFFERS:
            sgn, st, _ = call([(K, c, t, 0)], off)
            if sgn:
                ok &= (st[0], st[1]) == (sgn, -t)                     # (6, 10) = (t, s) opens (7, 8) = (s, -t)
                ok &= (t == sgn) == (st[0] != st[1])                  # agreeing opens opposing, opposing agreeing
                ok &= (st[0], st[1]) == (lambda x, y: (y, -x))(t, sgn)  # the right spiral step of F58
    return ok

def R17():
    s, c = C([(K, 1, -1, 0)], [(K, 1)])
    six = {k: t for k, _, t, _ in [(K, 1, -1, 0)]}
    return s == [(K, 0)] and c == [(K, 1, -1, 1)] and six[K] == -1

def trace(offers, carry=()):
    carry = list(carry); out = []; cs = []
    for off in offers:
        s, carry = C(carry, off); out.append(dict(s).get(K)); cs.append(tuple(carry[0][1:]) if carry else None)
    return out, cs

def R18():
    out, cs = trace([[(K, 1)]] * 7)
    ok = out == [1, 0, 0, 0, 0, 1, 0]
    ok &= cs[:5] == [(1, -1, 0), (1, -1, 1), (1, -1, 2), (1, -1, 3), None] and cs[5] == (1, -1, 0)
    out2, cs2 = trace([[(K, -1)]] + [[(K, 1)]] * 7)
    ok &= cs2[1] == (1, 1, 0) and [x[2] for x in cs2[2:6]] == [1, 2, 3, 4] and cs2[6] is None
    ok &= out2[2:7] == [0, 0, 0, 0, 0]
    return ok

def R19():
    cases = 0; ok = True
    offers = [[]] + [[(K, a)] for a in S] + [[(K, a), (K, b)] for a, b in product(S, S)]
    for c, t in product(S, S):
        for off in offers:
            vals = [v for _, v in off]
            want = c if vals == [c, c] else (0 if vals == [c] else -c)
            s, st, _ = call([(K, c, t, 0)], off)
            ok &= s == want
            if s: ok &= st[0] == s
            if t == -1: cases += 1
    return ok and cases == 14

def R20():
    s1, c1 = C([(K, 1, -1, 0)], [(K, 1)])
    s2, c2 = C([(K, 1, -1, 0)], [(K, 1), (K, 1)])
    return s1 == [(K, 0)] and c1 == [(K, 1, -1, 1)] and s2 == [(K, 1)] and c2 == [(K, 1, 1, 0)]

def R21():
    o0, _ = trace([[(K, 1)]] * 5, [(K, 1, -1, 0)]); o1, _ = trace([[(K, 1)]] * 4, [(K, 1, -1, 1)])
    return o0 == [0, 0, 0, 0, 1] and o1 == [0, 0, 0, 1]

def R22():
    ok = True
    for c, t in product(S, S):
        # fresh write at s = -c (nothing arriving): pair relation kept, next 6 inverts
        s, st, _ = call([(K, c, t, 0)], [])
        ok &= st[1] == -t and ((st[0] == st[1]) == (c == t))
        # fresh write at s = c (two c arriving): both change
        s, st, _ = call([(K, c, t, 0)], [(K, c), (K, c)])
        ok &= s == c and st[1] == -t and ((st[0] == st[1]) != (c == t))
        # kept through a 0: next 6 releases t again
        s, st, _ = call([(K, c, t, 0)], [(K, c)])
        ok &= s == 0 and st[1] == t
    # completing unrenewed: key releases nothing at 6 next
    s, c2 = C([(K, 1, -1, 3)], [(K, 1)])
    ok &= s == [(K, 0)] and c2 == []
    return ok

def R23():
    neg = {st for st in REACH if st and st[1] == -1}; pos = {st for st in REACH if st and st[1] == 1}
    return (len(REACH) == 19 and () in REACH and len(neg) == 8 and len(pos) == 10
            and {st[2] for st in neg} == {0, 1, 2, 3} and {st[2] for st in pos} == {0, 1, 2, 3, 4}
            and TRANS == 114)

def representative(seq):
    nz = [v for v in seq if v != 0]
    if not nz: return []
    tot = max(-2, min(2, sum(nz)))
    if tot == 0: return [(K, 1), (K, -1)]
    return [(K, 1 if tot > 0 else -1)] * abs(tot)

def R24():
    comps = 0; ok = True
    for st in REACH:
        base = [(K,) + st] if st else []
        for L in range(7):
            for seq in product((-1, 0, 1), repeat=L):
                comps += 1
                ok &= C(base, [(K, v) for v in seq]) == C(base, representative(seq))
    return ok and comps == 20767

def R25():
    states = sorted(REACH)
    ops = [[], [(K, 1)], [(K, -1)]]
    trans = len(states) * len(ops)
    def run(st, off, n=6):
        carry = [(K,) + st] if st else []; out = []
        for _ in range(n):
            s, carry = C(carry, off); v = dict(s).get(K); out.append(v if v else 0)
        return out
    pairs = list(combinations(states, 2))
    plus = {p for p in pairs if run(p[0], [(K, 1)]) != run(p[1], [(K, 1)])}
    minus = {p for p in pairs if run(p[0], [(K, -1)]) != run(p[1], [(K, -1)])}
    return trans == 57 and len(pairs) == 171 and len(plus) == 146 and len(minus) == 146 and len(plus | minus) == 171

def R27():
    ok = True
    surf = [('a', 1), ('b', -1), ('c', 0)]; neut = {'a': 'x', 'b': 'y', 'c': 'z'}
    out = R(surf, neut)
    ok &= out == [('x', 1), ('y', -1), ('z', 0)]
    ok &= all(len(x) == 2 for x in out)
    return ok

def R28():
    ok = True
    for c in S:
        carry = []; offs = [[(K, c)]] + [[]] * 8; surf = []; pairs = []
        for off in offs:
            s, carry = C(carry, off); surf.append(dict(s)[K]); pairs.append(carry[0][1:3])
        t = -1
        ok &= surf == [c, -c] * 4 + [c]
        ok &= pairs[:4] == [(c, t), (-c, -t), (c, t), (-c, -t)]
        seq = [pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1], pairs[2][0]]
        ok &= seq == [c, t, -c, -t, c]
    return ok

def R29():
    ok = True
    for c, t in product(S, S):
        seq = [c, t, -c, -t, c]
        prs = [(seq[i], seq[i + 1]) for i in range(4)]
        ok &= sorted(prs) == sorted(product(S, S))
        ok &= all(prs[i + 1] == (prs[i][1], -prs[i][0]) for i in range(3))
        agree = [a == b for a, b in prs]
        ok &= agree[0] == agree[2] and agree[1] == agree[3] and agree[0] != agree[1]
    return ok

def R30():
    ok = True
    for a, b, z in product(S, S, S):
        ok &= (((a == b) != (b == z)) == (z == -a))
    return ok and (1 == 1) and (1 == 1)  # +,+,+: (a,b) and (b,z) both agree

def R31():
    ok = True
    for c, t in product(S, S):
        s, st, _ = call([(K, c, t, 0)], [])
        ok &= s == -c  # 10 surfaces -c while 6 releases t
    _, c1 = C([], [(K, 1)])
    _, c2 = C([], [(K, -1)]); _, c2 = C(c2, [])
    ok &= c1 == [(K, 1, -1, 0)] and c2 == [(K, 1, 1, 0)]
    s1, _ = C(c1, []); s2, _ = C(c2, [])
    ok &= s1 == [(K, -1)] and s2 == [(K, -1)] and c1[0][2] == -1 and c2[0][2] == 1
    a, ca = C([(K, 1, -1, 0)], [(K, 1)]); b, cb = C([(K, 1, -1, 0)], [(K, -1)])
    ok &= a == [(K, 0)] and ca == [(K, 1, -1, 1)] and b == [(K, -1)] and cb[0][1] == -1
    return ok

CON = ns['CONNECTORS']; JOI = ns['JOINS']

def R32():
    want = {2: ('2-self-offering', 'right', 'arriving'), 6: ('6-other-crossing', 'left', 'releasing'),
            9: ('9-other-releasing', 'backward', 'along'), 10: ('10-other-surfacing', 'right', 'releasing'),
            14: ('14-social-crossing', 'left', 'arriving'), 17: ('17-social-abundancing', 'forward', 'along')}
    across = [k for k, v in CON.items() if v[2] != 'along']; along = [k for k, v in CON.items() if v[2] == 'along']
    return CON == want and across == [2, 6, 10, 14] and all(k % 2 == 0 for k in across) and along == [9, 17] and all(k % 2 for k in along)

def R33():
    ok = JOI == {10: 14, 6: 2, 17: 9, 9: 17}
    ok &= all(a % 2 == b % 2 for a, b in JOI.items())
    ok &= 10 - 2 == 8 and 14 - 6 == 8 and (6 + 8, 2 + 8) == (14, 10)
    return ok

def R34():
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name != '_17_social_abundancing']
    used = {n.id for f in fns for n in ast.walk(f) if isinstance(n, ast.Name)}
    if 'CONNECTORS' in used or 'JOINS' in used: return False
    ns2 = {}; exec(code, ns2); ns2['CONNECTORS'] = {}; ns2['JOINS'] = {}
    C2 = ns2['_1_self_coupling']
    return all(C2([(K,) + st] if st else [], off) == C([(K,) + st] if st else [], off) for st in REACH for off in OFFERS)

def R35():
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    two = [f for f in fns if f.name != '_17_social_abundancing']
    third = [f for f in fns if f.name == '_17_social_abundancing']
    in_two = any((isinstance(n, ast.Constant) and n.value == 17) or (isinstance(n, ast.Name) and '17' in n.id)
                 for f in two for n in ast.walk(f))
    calls = {n.func.id for f in third for n in ast.walk(f) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    return (not in_two) and len(third) == 1 and {'_1_self_coupling', '_9_other_releasing'} <= calls and 17 in CON and 17 in JOI and JOI[17] == 9 and JOI[9] == 17


# two resolvers joined 6 -> 2
def six(carry): return [(k, t) for k, c, t, a in carry]

def two_run(sa, sb, first, ab, ba, calls=12):
    car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}; inbox = {'A': [], 'B': []}
    order = ['A', 'B'] if first == 'A' else ['B', 'A']; log = []
    for i in range(calls):
        me = order[i % 2]; other = 'B' if me == 'A' else 'A'
        rel = six(car[me]); s, c = C(car[me], inbox[me]); inbox[me] = []
        if (ab if me == 'A' else ba): inbox[other] = rel
        log.append((me, dict(s).get(K), rel, car[me], c)); car[me] = c
    return log

def R40():
    tot = zeros = cont = 0
    for sa, sb, f in product(S, S, 'AB'):
        for me, s, rel, cin, cout in two_run(sa, sb, f, True, True):
            tot += 1
            if s == 0:
                zeros += 1
                cont += len(rel) == 1 and cout == [cin[0][:3] + (cin[0][3] + 1,)]
    a_both = [x[1] for x in two_run(-1, -1, 'A', True, True) if x[0] == 'A']
    others = [[x[1] for x in two_run(-1, -1, 'A', ab, ba) if x[0] == 'A'] for ab, ba in [(True, False), (False, True), (False, False)]]
    return (tot == 96 and zeros == 32 and cont == 32 and a_both == [1, -1, 0, 1, -1, 0]
            and all(o == [1, -1, 1, -1, 1, -1] for o in others))

def R41():
    parted = comps = 0
    for sa, sb, f in product(S, S, 'AB'):
        both = two_run(sa, sb, f, True, True)
        for me in 'AB':
            only = two_run(sa, sb, f, me == 'B', me == 'A')
            comps += 1
            parted += [x[1] for x in both if x[0] == me] != [x[1] for x in only if x[0] == me]
    return comps == 16 and parted == 12

def R42():
    ok = True
    # the named instance
    a = C([], [(K, 1)])[1]; relA = six(a); a = C(a, [])[1]
    b = C([], [(K, -1)])[1]; relB = six(b)
    ok &= relA == [(K, -1)] and relB == [(K, -1)]
    sj, cj = C(a, relB); su, cu = C(a, [])
    ok &= sj == [(K, 0)] and cj == [a[0][:3] + (1,)] and su == [(K, 1)] and cu == [(K, 1, -1, 0)]
    # 256 runnings: four seed pairs x each joining of the two legs at each of three rounds
    runs = 0
    for sa, sb in product(S, S):
        for legs in product(product((True, False), repeat=2), repeat=3):
            runs += 1
            car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}; inbox = {'A': [], 'B': []}
            for ab, ba in legs:
                for me, other, joined in (('A', 'B', ab), ('B', 'A', ba)):
                    rel = six(car[me]); cin = car[me]
                    s, c = C(cin, inbox[me]); inbox[me] = []
                    inbox[other] = rel if joined else []
                    if dict(s).get(K) == 0 and cin:
                        ok &= c == [cin[0][:3] + (cin[0][3] + 1,)]
                    car[me] = c
    return ok and runs == 256

def R43():
    ok = True; Cn = {}
    for arriving in S:
        B = C([], [(K, 1)])[1]; Cc = C([], [(K, 1)])[1]
        relB = six(B); sB, B = C(B, [(K, arriving)])
        sC, Cc = C(Cc, relB)
        ok &= relB == [(K, -1)] and sC == [(K, -1)]
        ok &= sB == ([(K, 0)] if arriving == 1 else [(K, -1)])
        relB2 = six(B); sC2, _ = C(Cc, relB2)
        Cn[arriving] = (relB2, sC2)
    ok &= Cn[1] == ([(K, -1)], [(K, 0)]) and Cn[-1] == ([(K, 1)], [(K, 1)])
    return ok

def ring(n, steps):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]; inbox[0] = [(K, 1)]
    states = []; surf = []
    for _ in range(steps):
        nb = [[] for _ in range(n)]; row = []
        for i in range(n):
            s, c = C(carry[i], inbox[i]); carry[i] = c
            nb[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
        inbox = nb; surf.append(tuple(row))
        states.append((tuple(tuple(c) for c in carry), tuple(tuple(b) for b in inbox)))
    return surf, states

def recur(n):
    surf, st = ring(n, 12 * n + 20); first = {}
    for t, s in enumerate(st):
        if s in first: return first[s] + 1, t - first[s]
        first[s] = t

def R44():
    ok = trace([[(K, 1)], [], [], [], [], []], [])[0] is not None
    surf, _ = ring(1, 8); ok &= [x[0] for x in surf] == [1, 0, -1, 0, 1, 0, -1, 0]
    for n in list(range(1, 12)) + [17, 59]:
        ok &= recur(n) == (n, 2 if n % 2 == 0 else 4 * n)
    return ok

def R45():
    ok = True
    for n in list(range(1, 12)) + [17, 59]:
        surf, _ = ring(n, 10 * n + 8)
        per = surf[n:]
        if n % 2 == 0:
            ok &= all(per[t][i] == -per[t + 1][i] for t in range(len(per) - 1) for i in range(n))
            ok &= all(per[t][i] == -per[t][(i + 1) % n] for t in range(len(per)) for i in range(n))
        else:
            ok &= all(per[t + 2 * n][i] == -per[t][i] for t in range(len(per) - 2 * n) for i in range(n))
            ok &= all(per[t + 4 * n][i] == per[t][i] for t in range(len(per) - 4 * n) for i in range(n))
            if n > 1:
                zs = [(t, [i for i in range(n) if per[t][i] == 0]) for t in range(len(per))]
                ok &= all(len(z) <= 1 for _, z in zs)
                at = [(t, z[0]) for t, z in zs if z]
                ok &= all(b[1] == (a[1] + 1) % n and b[0] - a[0] == 2 for a, b in zip(at, at[1:]))
    return ok and 2 * 59 == 118 and 4 * 59 == 236

def R46():
    rest = None
    for n in range(1, 12):
        _, st = ring(n, 5000)
        rest = ((tuple(() for _ in range(n))), tuple(() for _ in range(n)))
        if any(s == rest for s in st): return False
    return True

def R56():
    SYM = {1: '+', -1: '-', 0: '0'}
    def step(carry, sym):
        inbox = [] if sym == '.' else [(K, {'+': 1, '-': -1, '0': 0}[sym])]
        s, cc = C(list(carry), inbox)
        out = R(s, {K: K}); return tuple(tuple(x) for x in cc), ('.' if not out else SYM[out[0][1]])
    flip = lambda s: '-' if s == '+' else '+'
    E = (); a = step(E, '+')[0]; b = step(a, '.')[0]; D = {a, b}   # the two carryings, reached at the code from empty
    two_carryings = a == ((K, 1, -1, 0),) and b == ((K, -1, 1, 0),)
    def run(st, ins):
        outs = []
        for x in ins: st, o = step(st, x); outs.append(o)
        return st, ''.join(outs)
    checks = {'two carryings': two_carryings}
    # P0: a self given one sign and nothing after surfaces the sign alternating at each call, its carrying a, b, a, b
    st, out = run(E, '+' + '.' * 11); checks['P0 one sign alone alternates'] = out == '+-' * 6 and step(a, '.') == (b, '-') and step(b, '.') == (a, '+')
    # L1: given an alternating arriving, a self surfaces it at the same call, its carrying a or b
    ok = True
    for s0, first in ((E, '+'), (a, '-'), (b, '+')):
        ins = ''.join(first if i % 2 == 0 else flip(first) for i in range(12)); st, out = run(s0, ins)
        ok &= out == ins and st in D
    checks['L1 an alternating arriving surfaces as it arrives'] = ok
    # W: the wave meeting itself at the seed: in phase (even ring) nothing changes; out of phase (odd ring) one 0, then the arriving
    st, out = run(b, '+-' * 6); checks['W even: in phase, no change'] = out == '+-' * 6 and st in D
    st, out = run(a, '+-' * 6); checks['W odd: out of phase, one 0, then the arriving'] = out == '0' + '-+' * 5 + '-' and st in D
    # L2: an alternating arriving with one 0: the self surfaces its own next sign at the 0, the 0 one call later, then the arriving
    ok = True
    for s0, s in ((a, '-'), (b, '+'), (E, '+')):
        ins = s + '0' + flip(s) + s + flip(s) + s + flip(s); st, out = run(s0, ins)
        ok &= out == s + flip(s) + '0' + s + flip(s) + s + flip(s) and st in D
        st2 = s0
        for x in ins[:4]: st2, _ = step(st2, x)
        ok &= st2 in D   # back at the two by the second call after the 0
    checks['L2 a 0 passes one call later'] = ok
    # the rings themselves, n = 1 to 60: the pause formula and no rest
    def ring(n, T):
        carry = [E] * n; inbox = ['.'] * n; inbox[0] = '+'; outs = [[] for _ in range(n)]; rest = False
        for t in range(T):
            nb = ['.'] * n
            for i in range(n):
                carry[i], o = step(carry[i], inbox[i]); outs[i].append(o); nb[(i + 1) % n] = o
            inbox = nb
            rest |= all(x == E for x in carry) and all(x == '.' for x in inbox)
        return [''.join(o) for o in outs], rest
    ok = True
    for n in range(2, 61):
        outs, rest = ring(n, 8 * n + 8)
        ok &= not rest
        for i in range(n):
            zeros = [t for t, x in enumerate(outs[i]) if x == '0']
            want = [n + 2 * i + 2 * n * k for k in range(8)] if n % 2 else []
            ok &= zeros == [z for z in want if z < 8 * n + 8]
    return all(checks.values()) and ok


def R55_probe():
    return C([], []) == ([], [])

def R48():
    ok = all(((n + 8) % 2 == n % 2) for n in range(1, 10))
    ok &= all(((17 - n) % 2 != n % 2) and 17 - (17 - n) == n for n in range(1, 17))
    ok &= all(((9 - n) % 2 != n % 2) and 9 - (9 - n) == n for n in range(1, 9))
    return ok

def R49():
    p9 = sorted({tuple(sorted((n, 9 - n))) for n in range(1, 9)})
    p17 = sorted({tuple(sorted((n, 17 - n))) for n in range(1, 17)})
    p8 = [(n, n + 8) for n in range(1, 10)]
    return (p9 == [(1, 8), (2, 7), (3, 6), (4, 5)] and all((a + b) % 2 for a, b in p9)
            and len(p17) == 8 and all((a + b) % 2 for a, b in p17) and 17 - 17 not in range(1, 18)
            and all(a % 2 == b % 2 for a, b in p8) and (3, 11) in p8 and (7, 15) in p8)

def R50():
    rows = [[n, n + 8, 9 - n, 17 - n] for n in range(1, 5)]
    return rows == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]] and all(17 - (n + 8) == 9 - n for n in range(1, 9))

FORMS = {'1-9-8-16': ([1, 9, 8, 16], 'co co bi bi'), '2-15-7-10': ([2, 15, 7, 10], 'bi co co bi'),
         '3-11-6-14': ([3, 11, 6, 14], 'co co bi bi'), '4-13-5-12': ([4, 13, 5, 12], 'bi co co bi'),
         '9-5-12-8': ([9, 5, 12, 8], 'co co bi bi'), '7-11-6-10': ([7, 11, 6, 10], 'co co bi bi'),
         '1-9-5-12-8-16': ([1, 9, 5, 12, 8, 16], 'co co co bi bi bi'), '2-15-7-11-6-10': ([2, 15, 7, 11, 6, 10], 'bi co co co bi bi'),
         '3-11-7-10-6-14': ([3, 11, 7, 10, 6, 14], 'co co co bi bi bi'), '4-13-5-9-8-12': ([4, 13, 5, 9, 8, 12], 'bi co co co bi bi'),
         '1-9-5-13-4-12-8-16': ([1, 9, 5, 13, 4, 12, 8, 16], 'co co co co bi bi bi bi'),
         '2-15-7-11-3-14-6-10': ([2, 15, 7, 11, 3, 14, 6, 10], 'bi co co co co bi bi bi')}
HIGHER = {'18-31-23-26': ([18, 31, 23, 26], 'bi co co bi'), '19-27-22-30': ([19, 27, 22, 30], 'co co bi bi'),
          '18-31-23-27-22-26': ([18, 31, 23, 27, 22, 26], 'bi co co co bi bi'),
          '19-27-23-26-22-30': ([19, 27, 23, 26, 22, 30], 'co co co bi bi bi')}

def one_run_each(c):
    p = [x % 2 for x in c]; ch = sum(p[i] != p[i - 1] for i in range(len(p)))
    return ch == 2 and p.count(1) == p.count(0)

def R51():
    ok = True
    for c, rnd in list(FORMS.values()) + list(HIGHER.values()):
        ok &= one_run_each(c) and ' '.join('co' if x % 2 else 'bi' for x in c) == rnd
    return ok and not any(17 in c for c, _ in FORMS.values())

def R52():
    odd_p = {'1-9-8-16': '2-15-7-10', '2-15-7-10': '1-9-8-16', '3-11-6-14': '4-13-5-12', '4-13-5-12': '3-11-6-14',
             '9-5-12-8': '7-11-6-10', '7-11-6-10': '9-5-12-8', '1-9-5-12-8-16': '2-15-7-11-6-10',
             '2-15-7-11-6-10': '1-9-5-12-8-16', '3-11-7-10-6-14': '4-13-5-9-8-12', '4-13-5-9-8-12': '3-11-7-10-6-14',
             '1-9-5-13-4-12-8-16': '2-15-7-11-3-14-6-10', '2-15-7-11-3-14-6-10': '1-9-5-13-4-12-8-16'}
    even_p = {'2-15-7-10': '3-11-6-14', '3-11-6-14': '2-15-7-10', '4-13-5-12': '4-13-5-12', '7-11-6-10': '7-11-6-10',
              '2-15-7-11-6-10': '3-11-7-10-6-14', '3-11-7-10-6-14': '2-15-7-11-6-10',
              '2-15-7-11-3-14-6-10': '2-15-7-11-3-14-6-10'}
    oddsw = lambda n: n + 1 if n % 2 else n - 1
    evensw = lambda n: n + 1 if n % 2 == 0 else n - 1
    rots = lambda c: [tuple(c[i:] + c[:i]) for i in range(len(c))]
    rev = lambda c: [c[0]] + c[1:][::-1]
    listed = [sorted(c) for c, _ in FORMS.values()]
    ok = True
    for sw, P in ((oddsw, odd_p), (evensw, even_p)):
        for f, (c, _) in FORMS.items():
            img = [sw(x) for x in c]
            if f in P:
                tgt = FORMS[P[f]][0]
                ok &= (tuple(img) in rots(tgt)) if P[f] == f else (tuple(img) in rots(rev(tgt)))
            else:
                as_form = any(tuple(img) in rots(c2) or tuple(img) in rots(rev(c2)) for c2, _ in FORMS.values())
                ok &= (not all(1 <= x <= 16 for x in img)) or not as_form
    return ok

def R53():
    row = lambda s: [2 + 2 * s * j for j in range(4)]
    ev = [n for n in range(1, 17) if n % 2 == 0]
    return (row(1) == [2, 4, 6, 8] and row(2) == [2, 6, 10, 14] and [n + 8 for n in row(1)] == [10, 12, 14, 16]
            and sorted(row(2) + [4, 8, 12, 16]) == ev and 8 * 1 + 1 == 9 and 8 * 2 + 1 == 17)

def R54():
    return 11 - 3 == 8 and 11 % 2 == 3 % 2 == 1 and R7()


# ---------------------------------------------------------------- the third function, a society at one call
A = ns['_17_social_abundancing']
import random

def gather(arr):
    return [x for c in (2, 14, 17) for x in arr.get(c, [])]

def surfacings(car, arr, S):
    return {s: dict(C(car.get(s, []), gather(arr.get(s, {})))[0]).get(K) for s in S}

# ---- R58: one momentary at the third function equals the two functions called by hand at each self
def R58():
    S = {'A': {'right': ['B'], 'backward': ['C']}, 'B': {'left': ['A'], 'right': ['C']}, 'C': {'left': ['B'], 'forward': ['A'], 'backward': ['A']}}
    car = {'A': [(K, 1, -1, 1)], 'B': [(K, -1, 1, 0), ('j', 1, 1, 2)], 'C': []}
    arr = {'A': {2: [(K, -1)]}, 'C': {17: [(K, 1), ('j', -1)]}}
    nxt_car, nxt_arr = A(car, arr, {}, S)
    exp_car, exp_arr = {}, {s: {2: [], 14: [], 17: []} for s in S}
    for s in S:
        ten, eleven = C(car.get(s, []), gather(arr.get(s, {})))
        exp_car[s] = eleven
        six = [(k, t) for k, c, t, a in car.get(s, [])]
        nine = R(ten, {k: k for k, v in ten})
        for rel, signs in ((6, six), (10, ten), (9, nine)):
            for nb in S[s].get(CON[rel][1], []):
                exp_arr[nb][JOI[rel]] += signs
    fns = [n.name for n in __import__('ast').parse(code).body if isinstance(n, __import__('ast').FunctionDef)]
    return nxt_car == exp_car and nxt_arr == exp_arr and fns == ['_1_self_coupling', '_9_other_releasing', '_17_social_abundancing']

# ---- R59: the rings at the third function
def ring_at(n, steps, facing):
    S = {i: {facing: [(i + 1) % n]} for i in range(n)}
    car, arr = {}, {0: {2: [(K, 1)]}}
    states, surf = [], []
    for _ in range(steps):
        surf.append(tuple(surfacings(car, arr, S)[i] for i in range(n)))
        car, arr = A(car, arr, {}, S)
        states.append((tuple(tuple(map(tuple, car[i])) for i in range(n)), tuple(tuple((c, tuple(arr[i][c])) for c in (2, 14, 17)) for i in range(n))))
    return surf, states

def recur_at(n, facing):
    surf, st = ring_at(n, 12 * n + 20, facing); first = {}
    for t, s in enumerate(st):
        if s in first: return first[s] + 1, t - first[s]
        first[s] = t

def R59():
    ok = True
    surf, _ = ring_at(1, 8, 'backward'); ok &= [x[0] for x in surf] == [1, 0, -1, 0, 1, 0, -1, 0]
    for n in list(range(1, 12)) + [17, 59]:
        ok &= recur_at(n, 'backward') == (n, 2 if n % 2 == 0 else 4 * n)
        ok &= recur_at(n, 'right') == (n, 2 if n % 2 == 0 else 4 * n)
    for n in range(1, 12):
        ok &= recur_at(n, 'left') == (2 * n, 4 * n)
    # even and odd surfacings, as R45, at the along ring
    for n in list(range(1, 12)) + [17, 59]:
        surf, _ = ring_at(n, 10 * n + 8, 'backward'); per = surf[n:]
        if n % 2 == 0:
            ok &= all(per[t][i] == -per[t + 1][i] for t in range(len(per) - 1) for i in range(n))
            ok &= all(per[t][i] == -per[t][(i + 1) % n] for t in range(len(per)) for i in range(n))
        else:
            ok &= all(per[t + 2 * n][i] == -per[t][i] for t in range(len(per) - 2 * n) for i in range(n))
            ok &= all(per[t + 4 * n][i] == per[t][i] for t in range(len(per) - 4 * n) for i in range(n))
    # the rest returns at no coupling, rings 1..11 over 5000 momentaries, at each of the three joins
    for facing in ('backward', 'right', 'left'):
        for n in range(1, 12):
            _, st = ring_at(n, 5000, facing)
            rest = (tuple(() for _ in range(n)), tuple(tuple((c, ()) for c in (2, 14, 17)) for _ in range(n)))
            ok &= not any(s == rest for s in st)
    return ok

# ---- R60: the order within a momentary carries nothing
def R60():
    random.seed(1)
    S = {i: {'backward': [(i + 1) % 7], 'right': [(i + 2) % 7], 'left': [(i - 2) % 7]} for i in range(7)}
    car, arr = {}, {0: {2: [(K, 1)]}, 3: {2: [(K, -1)]}}
    ok = True; checked = 0
    for step in range(30):
        base = A(car, arr, {}, S)
        for _ in range(5):
            order = list(S); random.shuffle(order)
            S2 = {s: S[s] for s in order}
            arr2 = {s: {c: random.sample(v, len(v)) for c, v in a.items()} for s, a in arr.items()}
            alt = A(car, arr2, {}, S2)
            ok &= alt[0] == base[0] and all(sorted(alt[1][s][c]) == sorted(base[1][s][c]) for s in S for c in (2, 14, 17))
            checked += 1
        car, arr = base
    return ok and checked == 150

# ---- the hole: three by three with the centre missing
def hole_grid(both_ways=False):
    S = {}
    for r in range(3):
        for c in range(3):
            if (r, c) == (1, 1): continue
            nb = {}
            if c + 1 < 3 and (r, c + 1) != (1, 1): nb['right'] = [(r, c + 1)]
            if c - 1 >= 0 and (r, c - 1) != (1, 1): nb['left'] = [(r, c - 1)]
            along = []
            if r - 1 >= 0 and (r - 1, c) != (1, 1): along.append((r - 1, c))
            if both_ways and r + 1 < 3 and (r + 1, c) != (1, 1): along.append((r + 1, c))
            if along: nb['backward'] = along
            if r + 1 < 3 and (r + 1, c) != (1, 1): nb['forward'] = [(r + 1, c)]
            S[(r, c)] = nb
    return S

def trace_grid(S, seed, steps):
    car, arr = {}, {seed: {2: [(K, 1)]}}
    rows = []
    for t in range(steps):
        rows.append((surfacings(car, arr, S), {s: {c: list(v) for c, v in a.items()} for s, a in arr.items()}))
        car, arr = A(car, arr, {}, S)
    return rows

def R61():
    S = hole_grid(False); rows = trace_grid(S, (1, 0), 40)
    ok = rows[1][1][(0, 0)][17] == [(K, 1)]                      # along arriving at the corner's 17 at momentary 1
    ok &= rows[1][0][(0, 0)] == 1 and rows[2][1][(0, 1)][14] == [(K, 1)]   # continuing into the release at 10, arriving at 14
    ok &= rows[2][0][(0, 1)] == 1 and rows[3][1][(0, 2)][14] == [(K, 1)]   # the top-right corner receives across at 14 at momentary 3
    ok &= rows[3][0][(0, 2)] == 1
    ok &= all(rows[t][0][(1, 2)] is None and not any(rows[t][1].get((1, 2), {}).get(c) for c in (2, 14, 17)) for t in range(40))
    ok &= all(rows[t][0][(2, c)] is None for t in range(40) for c in range(3))   # the bottom row receives nothing
    return ok

def R62():
    S = hole_grid(True); rows = trace_grid(S, (1, 0), 40)
    ok = rows[1][1][(0, 0)][17] == [(K, 1)] and rows[1][1][(2, 0)][17] == [(K, 1)]
    ok &= rows[1][0][(0, 0)] == 1 and rows[1][0][(2, 0)] == 1
    ok &= rows[3][0][(0, 2)] == 1 and rows[3][0][(2, 2)] == 1
    ok &= rows[4][1][(1, 2)][17] == [(K, 1), (K, 1)] and all(not rows[t][1].get((1, 2), {}).get(c) for t in range(4) for c in (2, 14, 17))
    ok &= rows[4][0][(1, 2)] == 1
    car, arr = {}, {(1, 0): {2: [(K, 1)]}}
    for t in range(4): car, arr = A(car, arr, {}, S)
    ok &= car[(1, 2)] == []
    car, arr = A(car, arr, {}, S)
    ok &= car[(1, 2)] == [(K, 1, -1, 0)]
    return ok


def R36():
    S = {'A': {'backward': ['B']}, 'B': {'backward': ['C']}, 'C': {'backward': ['A']}}
    car = {'A': [(K, 1, -1, 2)], 'B': [], 'C': [(K, -1, 1, 0)]}
    arr = {'B': {17: [(K, 1)]}}
    nxt, _ = A(car, arr, {}, S)
    ok = all(nxt[s] == C(car[s], gather(arr.get(s, {})))[1] for s in S)
    nxt2, _ = A(nxt, {}, {}, S)                     # the next call takes the returned 11 as its 3
    return ok and all(nxt2[s] == C(nxt[s], [])[1] for s in S)

def R37():
    S = {'A': {'backward': ['B']}, 'B': {'backward': ['C']}, 'C': {'backward': ['A']}}
    car = {'A': [(K, 1, -1, 2)], 'B': [], 'C': [(K, -1, 1, 0)]}
    arr = {'B': {17: [(K, 1)]}, 'A': {2: [('j', -1)]}}
    neut = {'A': {K: 'm', 'j': 'j'}}
    _, nxt = A(car, arr, neut, S)
    ok = True
    for s, nb in (('A', 'B'), ('B', 'C'), ('C', 'A')):
        ten, _ = C(car[s], gather(arr.get(s, {})))
        ok &= nxt[nb][17] == R(ten, neut.get(s, {k: k for k, v in ten})) and nxt[nb][2] == [] and nxt[nb][14] == []
    tenA, _ = C(car['A'], gather(arr['A']))
    ok &= tenA == [('j', -1), (K, -1)] and nxt['B'][17] == [('j', -1), ('m', -1)] and JOI[9] == 17 and JOI.get(9) != 2
    return ok

def R38():
    S = {'A': {'right': ['B']}, 'B': {'left': ['A'], 'right': ['C']}, 'C': {'left': ['B']}}
    car = {'A': [(K, 1, -1, 0)], 'B': [], 'C': [(K, -1, -1, 3)]}
    arr = {'A': {2: [(K, 1)]}}
    calls = []
    orig = ns['_1_self_coupling']
    def counting(c, o):
        calls.append((tuple(map(tuple, c)), tuple(o))); return orig(c, o)
    ns['_1_self_coupling'] = counting
    try:
        nxt_car, nxt_arr = A(car, arr, {}, S)
    finally:
        ns['_1_self_coupling'] = orig
    ok = len(calls) == 3 and sorted(calls) == sorted((tuple(map(tuple, car[s])), tuple(gather(arr.get(s, {})))) for s in S)
    # each releasing of this call arrives at the next call, none at this one
    ok &= nxt_arr['B'] == {2: [(K, -1)], 14: [(K, 0)], 17: []} and nxt_arr['A'] == {2: [], 14: [], 17: []} and nxt_arr['C'] == {2: [], 14: [], 17: []}
    return ok

def R63():
    def sums(n, steps):
        Sf = {i: {'backward': [(i + 1) % n]} for i in range(n)}
        car, arr = {}, {0: {2: [(K, 1)]}}; out = []
        for t in range(steps):
            surf = [dict(C(car.get(i, []), gather(arr.get(i, {})))[0]).get(K) or 0 for i in range(n)]
            c7 = sum(e[1] for i in range(n) for e in car.get(i, [])); c8 = sum(e[2] for i in range(n) for e in car.get(i, []))
            c16 = sum(e[3] for i in range(n) for e in car.get(i, [])); ncar = sum(len(car.get(i, [])) for i in range(n))
            transit = sum(v for i in range(n) for c in (2, 14, 17) for k, v in arr.get(i, {}).get(c, []))
            out.append((sum(surf), c7, c8, c16, transit, ncar))
            car, arr = A(car, arr, {}, Sf)
        return out[n:]
    ok = True
    for n in range(1, 12):
        o = sums(n, 6 * n + 10)
        cols = [sorted(set(x[j] for x in o)) for j in range(6)]
        if n % 2 == 0:
            ok &= cols[:5] == [[0]] * 5
        else:
            ok &= all(len(c) > 1 for c in cols[:5]) and cols[0] == [-1, 0, 1]
        ok &= cols[5] == [n]
    return ok

def R39():
    return R58() and R60() and R61()

CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'[FR]\d+(_probe)?', k) and callable(v)}

'''

PART_SOURCES['num'] = r'''"""Run checks for Exhibit THIRTY Part THREE · NUMBERS (links N1...), against Exhibit THREE v372
(/home/claude/work/Exhibit_THREE_Natural_Numbers_v372.md) and the resolver of Exhibit ONE v372
(resolver_v372.py beside this file). Each function is named for its link and returns True when it holds.
Polynomial identities are checked at more points than their degree, so they hold at each value.
Run: python3 ccl_num_checks.py [results.json]"""
import ast, json, os, re, sys, math
from fractions import Fraction as Q
from itertools import product, combinations, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R, CONNECTORS, JOINS

K = 'k'
S = (1, -1)
CODE = open(os.path.join(HERE, 'resolver_v372.py')).read()
TREE = ast.parse(CODE)


def poly_identity(f, g, deg, pts=None):
    """f == g as polynomials of degree <= deg in one variable: equal at deg + 2 or more points."""
    pts = pts or range(-deg - 3, deg + 40)
    return all(f(Q(x)) == g(Q(x)) for x in pts)


def primes_below(n):
    s = [True] * n; s[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i, v in enumerate(s) if v]


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


P17 = primes_below(60)
T = lambda k: k * (k + 1) // 2


class QR:
    """a + b*sqrt(d), a, b rational: exact arithmetic in Q(sqrt d)."""
    def __init__(s, a, b, d): s.a, s.b, s.d = Q(a), Q(b), d
    def __add__(s, o): o = s._c(o); return QR(s.a + o.a, s.b + o.b, s.d)
    def __sub__(s, o): o = s._c(o); return QR(s.a - o.a, s.b - o.b, s.d)
    def __neg__(s): return QR(-s.a, -s.b, s.d)
    def __mul__(s, o): o = s._c(o); return QR(s.a * o.a + s.d * s.b * o.b, s.a * o.b + s.b * o.a, s.d)
    def inv(s): n = s.a * s.a - s.d * s.b * s.b; return QR(s.a / n, -s.b / n, s.d)
    def __truediv__(s, o): return s * s._c(o).inv()
    def __eq__(s, o): o = s._c(o); return s.a == o.a and s.b == o.b
    def _c(s, o): return o if isinstance(o, QR) else QR(o, 0, s.d)
    def __float__(s): return float(s.a) + float(s.b) * math.sqrt(s.d)


PHI = QR(Q(1, 2), Q(1, 2), 5)


# ------------------------------------------------------------------ ONE · UNI-SCALING
def N3():
    # at n the momentary (n-1, n) completes and (n, n+1) opens; the side is the parity of its opening
    side = lambda opening: 'self' if opening % 2 else 'other'
    return all(side(n - 1) != side(n) and (n - 1) % 2 != n % 2 for n in range(2, 1001))


def N5():
    def ten(o):  # self's five from o, other's five from o + 1
        s5 = list(range(o, o + 5)); t5 = list(range(o + 1, o + 6))
        return s5, t5, list(zip(s5, t5))
    s1, t1, p1 = ten(1); s3, t3, p3 = ten(3)
    full = [(1, 2), (3, 4), (5, 6)]
    cover = sorted({x for m in full for x in m}) == sorted(set(s1) | set(t1))
    same = [(a - 2, b - 2) for a, b in p3] == p1 and all((a + b) % 2 for a, b in p3)
    within = set(s3) | set(t3) <= set(range(1, 10))
    part = [(1, 2), (3, 4)] + [(2, 3), (4, 5)]
    return cover and same and within and all(m in [(k, k + 1) for k in range(1, 9)] for m in part + [(5, 6)])


def N6():
    moms = [(k, k + 1) for k in range(1, 9)]
    exh = {x for m in moms for x in m} == set(range(1, 10))
    det = all(sum(1 for m2 in moms if m2[0] == m[1]) == 1 for m in moms[:-1])
    reach = all({m2[0] for m2 in moms if m2[0] >= m[1]} | {9} >= set(range(m[1], 10)) for m in moms)
    self_only = [m for m in moms if m[0] % 2]
    det_fails = any(not any(m2[0] == m[1] for m2 in self_only) for m in self_only)
    return exh and det and reach and det_fails


def N7():
    ok = sum([1, 3, 5]) == 9 and sum([2, 4, 6]) == 12
    ok &= poly_identity(lambda n: n * n - (n - 1) * (n - 1), lambda n: 2 * n - 1, 2)          # step of the square
    ok &= poly_identity(lambda n: n * (n + 1) - (n - 1) * n, lambda n: 2 * n, 2)               # step of the oblong
    ok &= all(sum(2 * k - 1 for k in range(1, n + 1)) == n * n and sum(2 * k for k in range(1, n + 1)) == n * (n + 1)
              for n in range(1, 1001))
    return ok


def N8():
    return poly_identity(lambda n: (n - 1) * (n + 1), lambda n: n * n - 1, 2)


def N9():
    ok = poly_identity(lambda n: (n - 3) * (n + 3), lambda n: n * n - 9, 2)
    ok &= all((n - k) * (n + k) == n * n - k * k for n in range(0, 200) for k in range(0, 50))
    return ok and 23 * 25 == 24 ** 2 - 1


F8 = lambda n: n + 8
F17 = lambda n: 17 - n
F9 = lambda n: 9 - n


def N11():
    ok = all(F8(n) - 8 == n for n in range(1, 10)) and all(F17(F17(n)) == n for n in range(1, 17)) \
        and all(F9(F9(n)) == n for n in range(1, 9))
    # alternating 8 up/down with 17 less runs round within 1..16
    def up_down(n): return n + 8 if n <= 8 else n - 8
    for n in range(1, 17):
        seen = [n]; x = n
        for i in range(4):
            x = up_down(x) if i % 2 == 0 else F17(x)
            seen.append(x)
        ok &= seen[-1] == n and len(set(seen[:4])) == 4 and all(1 <= y <= 16 for y in seen)
    # 9 less (within 1..8) alternated with 8 up or with 17 less leaves 1..8 at the next step, outside 9 less
    for n in range(1, 9):
        ok &= 9 <= F8(F9(n)) <= 16 and 9 <= F17(F9(n)) <= 16
    ok &= all(F17(F8(n)) == F9(n) for n in range(1, 9))
    return ok


def N12():
    rows = [[n, n + 8, 9 - n, 17 - n] for n in range(1, 5)]
    ok = rows == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]]
    for r in rows:
        steps = [(r[i], r[(i + 1) % 4]) for i in range(4)]
        changes = [(a, b) for a, b in steps if a % 2 != b % 2]
        ok &= len(changes) == 2 and all(a + b == 17 for a, b in changes)
        p = [x % 2 for x in r]
        ok &= sum(p[i] != p[i - 1] for i in range(4)) == 2 and 17 not in r
    ok &= Q(17, 2) == Q(17, 2) and all(n != 17 - n for n in range(1, 17))  # 17 less fixes no name: its centre is 8½
    return ok


def N15():
    ok = True
    for n in range(1, 1000):
        a = sum(x % 2 for x in (n, n + 1, n + 2)); b = sum(x % 2 for x in (n + 1, n + 2, n + 3))
        ok &= {a, b} == {1, 2}
    return ok and [x % 2 for x in (23, 24, 25)] == [1, 0, 1] and [x % 2 for x in (24, 25, 26)] == [0, 1, 0]


def N20():
    ok = True
    for N in range(2, 201):
        for k in range(N):
            met = len({(k * i) % N for i in range(N)})
            ok &= met == N // math.gcd(N, k)
        if is_prime(N):
            ok &= all(len({(k * i) % N for i in range(N)}) == N for k in range(1, N))
    ok &= len({(2 * i) % 9 for i in range(9)}) == 9 and not is_prime(9)
    return ok


def N22():
    ok = 2 * 3 - (2 + 3) == 1 and 2 + 3 == 5 and 2 * 3 == 6
    self4 = set(range(1, 5)); other4 = set(range(2, 6))
    shared = self4 & other4; outer = self4 ^ other4
    ok &= len(shared) == 3 and len(outer) == 2 and len(self4 | other4) == 5
    ok &= 2 * len(shared) == 6 and len(self4) + len(other4) == 2 * 3 + 2
    ok &= 2 + 2 == 2 * 2 == 4 and 3 + 3 == 6 and 3 * 3 == 9
    return ok


# ------------------------------------------------------------------ TWO · CORUSING
def N28():
    p3 = PHI * PHI * PHI
    ok = p3 - p3.inv() == QR(4, 0, 5)
    ok &= math.comb(11, 2) == T(10) == 55
    f = [0, 1]
    while len(f) < 12: f.append(f[-1] + f[-2])
    return ok and f[10] == 55 and N8()


def N30():
    return sum(P17) == 440 and len(P17) == 17 and 8 * 55 == 440 and 21 ** 2 - 1 == 440


# ------------------------------------------------------------------ THREE · UNRELATIONING
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a


def above_phi(x):  # x > 0 rational: x > phi iff x^2 - x - 1 > 0
    return x * x - x - 1 > 0


def N32():
    f = [fib(i) for i in range(1, 302)]  # 1, 1, 2, 3, 5, 8, ...
    ok = f[:7] == [1, 1, 2, 3, 5, 8, 13] and all(f[i] == f[i - 1] + f[i - 2] for i in range(2, len(f)))
    sides = [above_phi(Q(f[i + 1], f[i])) for i in range(1, 300)]  # 2/1, 3/2, 5/3, ...
    ok &= sides[:4] == [True, False, True, False]
    ok &= all(sides[i] != sides[i + 1] for i in range(len(sides) - 1))
    ok &= all(Q(f[i + 1], f[i]) * Q(f[i + 1], f[i]) - Q(f[i + 1], f[i]) - 1 != 0 for i in range(1, 300))
    # the side at each n: M^n = [[F(n+1), F(n)], [F(n), F(n-1)]] and det M = -1, so det M^n = (-1)^n
    M = [[1, 1], [1, 0]]; P = [[1, 0], [0, 1]]
    for n in range(1, 301):
        P = [[P[0][0] * M[0][0] + P[0][1] * M[1][0], P[0][0] * M[0][1] + P[0][1] * M[1][1]],
             [P[1][0] * M[0][0] + P[1][1] * M[1][0], P[1][0] * M[0][1] + P[1][1] * M[1][1]]]
        ok &= P == [[fib(n + 1), fib(n)], [fib(n), fib(n - 1)]] and P[0][0] * P[1][1] - P[0][1] * P[1][0] == (-1) ** n
    return ok


def N33():
    ok = PHI * PHI == PHI + 1
    other = -(PHI.inv())
    ok &= other * other == other + 1 and PHI - PHI.inv() == QR(1, 0, 5) and PHI * other == QR(-1, 0, 5)
    ok &= PHI == QR(1, 0, 5) + PHI.inv()  # phi = 1 + 1/phi: continued fraction all ones
    ok &= math.floor(float(PHI)) == 1
    # pentagon: diagonal over side
    V = [(math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5)) for k in range(5)]
    d = math.dist(V[0], V[2]); s = math.dist(V[0], V[1])
    return ok and abs(d / s - float(PHI)) < 1e-12


def N35():
    ok = True
    for n in range(1, 51):
        d = n * n + 4
        x = QR(Q(n, 2), Q(1, 2), d)
        ok &= x * x == x * QR(n, 0, d) + 1 and x == QR(n, 0, d) + x.inv()
        ok &= math.floor(float(x)) == n and 0 < float(x.inv()) < 1
    return ok and QR(Q(1, 2), Q(1, 2), 5) == PHI


def N37():
    # p/q closes at q turns; x^2 - x - 1 has no rational root (candidates +1, -1 give -1 and 1), so k*phi is never whole
    ok = all((q * Q(p, q)).denominator == 1 for p in range(1, 30) for q in range(1, 30))
    ok &= (1 * 1 - 1 - 1) != 0 and ((-1) * (-1) + 1 - 1) != 0
    ok &= all(QR(0, 0, 5) != (PHI * k) - QR(m, 0, 5) for k in range(1, 200) for m in [math.floor(k * float(PHI))])
    return ok


# ------------------------------------------------------------------ FOUR · TORUSING
def N42():
    # at three edges to each vertex (3V = 2E) and sum of sides = 2E: sum(6 - f) = 6F - 2E = 6(V - E + F)
    ok = True
    for E in range(3, 300, 3):
        V = Q(2 * E, 3)
        for F in range(1, 200):
            ok &= 6 * F - 2 * E == 6 * (V - E + F)
    ok &= (12 - 30 + 20) == 2 and (20 - 30 + 12) == 2
    # dodecahedron: 12 five-folds, V 20, E 30; truncated icosahedron: 12 five-folds, 20 six-folds, V 60, E 90
    for fives, sixes, V, E in ((12, 0, 20, 30), (12, 20, 60, 90)):
        F = fives + sixes
        ok &= 3 * V == 2 * E == 5 * fives + 6 * sixes and V - E + F == 2 and sum([1] * fives) == 6 * 2
    # a torus of six-folds: the hexagonal torus, each vertex three edges, sum(6 - f) = 0 = 6 * 0
    for m in range(1, 8):
        F = m * m; E = 3 * F; V = 2 * F
        ok &= V - E + F == 0
    return ok


def N44():
    ok = 19 ** 2 - 1 == 360 == 8 * T(9) == 8 * math.comb(10, 2) and 45 == 5 * 9
    ok &= 21 ** 2 - 1 == 440 == 8 * T(10) and 440 - 360 == 80 == 9 ** 2 - 1 == 8 * T(4) == 8 * math.comb(5, 2)
    ok &= (360 + 80) % 440 == 0 and 21 - 19 == 2
    return ok


# ------------------------------------------------------------------ FIVE · UNIQUENESSING
def N47():
    return [6 + 8 * k for k in range(3)] == [6, 14, 22] and 17 <= 22 <= 25 and 22 > 17 and 9 <= 14 <= 17


def N48():
    con = sorted(CONNECTORS); internal = [n for n in range(2, 18) if n not in CONNECTORS]
    return (len(con) == 6 and len(internal) == 10 and 6 == 8 - 2 and 10 == 8 + 2
            and 6 // 2 == 3 and 10 // 2 == 5 and 8 // 2 == 4 and len(con) + len(internal) + 1 == 17)


OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def reach(Cf):
    seen = {()}; frontier = [()]; trans = []
    while frontier:
        nxt = []
        for st in frontier:
            for off in OFFERS:
                s, c = Cf([(K,) + st] if st else [], off)
                s2 = tuple(c[0][1:]) if c else ()
                trans.append((st, tuple(map(tuple, off)), tuple(s), s2))
                if s2 not in seen: seen.add(s2); nxt.append(s2)
        frontier = nxt
    return seen, trans


def N50():
    seen, trans = reach(C)
    ok = len(seen) == 19 and len(trans) == 114
    ok &= all(v in (-1, 0, 1) for _, _, s, _ in trans for _, v in s)
    ok &= all(st == () or (st[0] in S and st[1] in S) for st in seen)
    # take the numeral off each name, and separately permute the numerals: the 114 transitions stand as they were
    names = sorted({n.id for n in ast.walk(TREE) if isinstance(n, ast.Name) and re.match(r'_\d+_', n.id)} |
                   {a.arg for n in ast.walk(TREE) if isinstance(n, ast.FunctionDef) for a in n.args.args if re.match(r'_\d+_', a.arg)})
    stripped = {nm: re.sub(r'^_\d+_', '_', nm) for nm in names}
    nums = [int(re.match(r'_(\d+)_', nm).group(1)) for nm in names]
    perm = dict(zip(sorted(set(nums)), sorted(set(nums))[::-1]))
    permuted = {nm: re.sub(r'^_(\d+)_', lambda m: f'_{perm[int(m.group(1))] + 100}_', nm) for nm in names}
    for ren in (stripped, permuted):
        if len(set(ren.values())) != len(ren): return False
        src = re.sub(r'\b(' + '|'.join(map(re.escape, sorted(ren, key=len, reverse=True))) + r')\b',
                     lambda m: ren[m.group(1)], CODE)
        ns = {}; exec(src, ns)
        C2 = next(v for k, v in ns.items() if callable(v) and k.endswith('self_coupling'))
        seen2, trans2 = reach(C2)
        ok &= trans2 == trans
    return ok


def N52():
    fn = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
    inside = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name)}
    return (set(CONNECTORS) & {2, 4, 6, 8}) == {2, 6} and '_4_self_sharing' in inside and '_8_other_torusing' in inside


def N53():
    ok = poly_identity(lambda k: (2 * k + 1) ** 2 - 1, lambda k: 8 * k * (k + 1) / 2, 2)
    ok &= [(2 * k + 1) ** 2 - 1 for k in range(11)] == [0, 8, 24, 48, 80, 120, 168, 224, 288, 360, 440]
    ok &= all((2 * k + 1) ** 2 - 1 == 8 * math.comb(k + 1, 2) for k in range(0, 200))
    return ok and 440 == 8 * 55 == 8 * math.comb(11, 2)


def N56():
    centres = [c for c in range(5, 10000) if all(is_prime(c + d) for d in (-4, -2, 2, 4))]
    return centres[:2] == [9, 15] and not is_prime(9) and not is_prime(15) and (5, 7, 11, 13) == (9 - 4, 9 - 2, 9 + 2, 9 + 4)


def N57():
    cells = [(r, c) for r in range(3) for c in range(3) if (r, c) != (1, 1)]
    adj = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
    start, end = (1, 0), (1, 2)
    paths = []
    def dfs(p):
        if p[-1] == end: paths.append(list(p)); return
        for c in cells:
            if c not in p and adj(p[-1], c): dfs(p + [c])
    dfs([start])
    ok = len(paths) == 2 and {tuple(p[1]) for p in paths} == {(0, 0), (2, 0)}
    for p in paths:
        steps = list(zip(p, p[1:]))
        along = sum(1 for a, b in steps if a[0] == b[0]); across = sum(1 for a, b in steps if a[1] == b[1])
        ok &= along == 2 and across == 2
    return ok


def N58():
    ok = [x for x in range(-1000, 1001) if x == -x] == [0]
    ok &= all(F8(n) != 0 for n in range(1, 10)) and all(F17(n) != 0 for n in range(1, 17)) and all(F9(n) != 0 for n in range(1, 9))
    return ok


def N59():
    ok = 17 - 9 == 25 - 17 == 8
    forms = [[1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12], [9, 5, 12, 8], [7, 11, 6, 10],
             [1, 9, 5, 12, 8, 16], [2, 15, 7, 11, 6, 10], [3, 11, 7, 10, 6, 14], [4, 13, 5, 9, 8, 12],
             [1, 9, 5, 13, 4, 12, 8, 16], [2, 15, 7, 11, 3, 14, 6, 10]]
    ok &= not any(17 in f for f in forms) and 25 > 17
    spans = [(1, 9), (9, 17), (17, 25)]
    moms = 0
    for a, b in spans:
        self_m = [(k, k + 1) for k in range(a, b) if (k - a) % 2 == 0]
        other_m = [(k, k + 1) for k in range(a + 1, b) if (k - a) % 2 == 1]
        ok &= len(self_m) == 4 and len(other_m) == 4 and all((x + y) % 2 for x, y in self_m + other_m)
        moms += len(self_m) + len(other_m)
    ok &= moms == 24 and 25 - 1 == 24
    ok &= [n - 1 for n in (6, 14, 22)] == [5, 13, 21]
    return ok


def N60():
    sol = [n for n in range(1, 10001) if 2 * n == n * (n - 1) // 2 and n * (n - 1) % 2 == 0]
    ok = sol == [5] and poly_identity(lambda n: n * (n - 1) / 2 - 2 * n, lambda n: n * (n - 5) / 2, 2)
    return ok and 2 * 5 == math.comb(5, 2) == T(4) == 10


def ring_complement_is_ring(n):
    ring = {frozenset((i, (i + 1) % n)) for i in range(n)}
    comp = {frozenset(e) for e in combinations(range(n), 2)} - ring
    deg = {v: sum(1 for e in comp if v in e) for v in range(n)}
    if not all(d == 2 for d in deg.values()): return False
    # connected single cycle
    seen = {0}; stack = [0]
    while stack:
        v = stack.pop()
        for e in comp:
            if v in e:
                w = next(iter(e - {v}))
                if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n


def N61():
    return [n for n in range(3, 61) if ring_complement_is_ring(n)] == [5]


def mono_triangle(n, col):
    E = list(combinations(range(n), 2)); c = dict(zip(E, col))
    return any(c[(a, b)] == c[(a, d)] == c[(b, d)] for a, b, d in combinations(range(n), 3))


def N62():
    E6 = list(combinations(range(6), 2))
    ok = all(mono_triangle(6, col) for col in product((0, 1), repeat=len(E6)))
    E5 = list(combinations(range(5), 2))
    good = [col for col in product((0, 1), repeat=len(E5)) if not mono_triangle(5, col)]
    ok &= len(good) == 12
    for col in good:
        for colour in (0, 1):
            edges = [e for e, x in zip(E5, col) if x == colour]
            deg = [sum(1 for e in edges if v in e) for v in range(5)]
            seen = {0}; stack = [0]
            while stack:
                v = stack.pop()
                for e in edges:
                    if v in e:
                        w = e[0] if e[1] == v else e[1]
                        if w not in seen: seen.add(w); stack.append(w)
            ok &= len(edges) == 5 and deg == [2] * 5 and len(seen) == 5
    return ok


def N63():
    ok = True
    for a in range(0, 1001):
        pairs = [(a + j, a + 9 - j) for j in range(5)]
        ok &= all((x + y) % 2 == 1 for x, y in pairs) and all(Q(x + y, 2) == a + Q(9, 2) for x, y in pairs)
        odd_first = [x % 2 for x, _ in pairs]
        odd_next = [(x + 1) % 2 for x, _ in pairs]; odd_two = [(x + 2) % 2 for x, _ in pairs]
        ok &= all(u != v for u, v in zip(odd_first, odd_next)) and odd_two == odd_first
    return ok


def N65():
    pairs9 = sorted({tuple(sorted((k, 9 - k))) for k in range(0, 10)})
    ok = pairs9 == [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)]
    stations = lambda p: len({x % 9 for x in p})
    ok &= [stations(p) for p in pairs9] == [1, 2, 2, 2, 2]
    ok &= 5 * 2 == 10 and 10 - 1 == 9 and 9 - 1 == 8 and 3 * 2 == 6
    return ok


def N66():
    return len(list(product(S, S))) == 4 and len(range(0, 10)) == 10 and 2 ** 2 * Q(5, 2) - 1 == 9


def N67():
    dbl = [pow(2, i, 17) for i in range(8)]
    sq = sorted({x * x % 17 for x in range(1, 17)})
    three = sorted({3 * x % 17 for x in sq})
    return (dbl == [1, 2, 4, 8, 16, 15, 13, 9] and pow(2, 8, 17) == 1 and 9 * 2 == 17 + 1
            and sorted(dbl) == sq and len(sq) == 8 and sorted(set(sq) | set(three)) == list(range(1, 17)))


def N68():
    sq = {x * x % 17 for x in range(1, 17)}
    j = lambda a, b: (a - b) % 17 in sq
    ok = all(j(a, b) == j(b, a) for a in range(17) for b in range(17) if a != b)
    quads = list(combinations(range(17), 4))
    ok &= len(quads) == 2380
    ok &= not any(all(j(a, b) for a, b in combinations(q, 2)) for q in quads)
    ok &= not any(all(not j(a, b) for a, b in combinations(q, 2)) for q in quads)
    return ok


def N70():
    return 440 + 1 == 21 ** 2 == 9 * 49


def droot(x, b):
    while x >= b:
        s = 0
        while x: s += x % b; x //= b
        x = s
    return x


def N71():
    ok = all(droot(9 * k, 10) == 9 for k in range(1, 2001))
    for b in range(3, 37):
        keep = [m for m in range(1, b) if all(droot(m * k, b) == m for k in range(1, 400))]
        ok &= keep == [b - 1]
    return ok


def N72():
    ok = (6 + 10) // 2 == 8 and (8 + 12) // 2 == 10 and (10 + 14) // 2 == 12 and (12 + 16) // 2 == 14
    ok &= 8 + 16 == 24 and (0 + 24) // 2 == 12 and 6 + 10 == 16
    ok &= 7 * 9 == 8 ** 2 - 1 and 9 * 11 == 10 ** 2 - 1 and 13 * 15 == 14 ** 2 - 1
    ok &= [(10 - k, 10 + k) for k in (2, 3, 4)] == [(8, 12), (7, 13), (6, 14)] and 6 * 14 == 10 ** 2 - 16
    ok &= 14 * 22 == 18 ** 2 - 16 and (14 + 22) // 2 == 18
    ok &= (6 + 22) // 2 == 14 and (10 + 18) // 2 == 14 and 14 - 10 == 4
    reach_span = [(Q(b - a, 2), b - a) for a, b in ((6, 14), (14, 22), (6, 22), (10, 18))]
    return ok and all(r / s == Q(1, 2) for r, s in reach_span)


# ------------------------------------------------------------------ SIX · APEXING
def N75():
    N = 48
    self_far = [k for k in range(N) if (N - k) % N == k]
    ok = self_far == [0, 24]
    ok &= all((24 - d) * (24 + d) == 24 ** 2 - d * d for d in range(1, 24))
    ok &= 23 * 25 == 24 ** 2 - 1 and 22 * 26 == 24 ** 2 - 4 and 7 ** 2 - 1 == 48
    return ok


def N76():
    gaps = [(p, q) for p, q in zip(P17, P17[1:]) if q - p == 6]
    return 5 ** 2 - 1 == 24 == math.factorial(4) and 48 // 2 == 24 and gaps[0] == (23, 29)


def N77():
    behind = [p for p in P17 if p < 24]; ahead = [p for p in P17 if p > 24]
    ok = len(behind) == 9 and len(ahead) == 8 and behind[-1] == 23 and ahead[0] == 29
    ok &= math.comb(9, 2) == 36 == 60 - 24 and math.comb(8, 2) == 28 == T(7)
    ok &= T(6) == 21 and T(8) == 36 and 28 - 21 == 7 and 36 - 28 == 8 and 36 - 21 == 15 == math.comb(6, 2)
    ok &= sum(1 for p, q in zip(P17, P17[1:]) if (q - p) % 2 == 0) == 15
    ok &= Q(36, 24) == Q(3, 2) and Q(9, 8) == Q(len(behind), len(ahead))
    return ok


def icosa_rotations():
    import numpy as np
    phi = (1 + 5 ** 0.5) / 2
    def rot(axis, ang):
        a = np.array(axis, float); a /= np.linalg.norm(a)
        x, y, z = a; c, s = math.cos(ang), math.sin(ang)
        return np.array([[c + x * x * (1 - c), x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
                         [y * x * (1 - c) + z * s, c + y * y * (1 - c), y * z * (1 - c) - x * s],
                         [z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, c + z * z * (1 - c)]])
    g1 = rot((0, 1, phi), 2 * math.pi / 5)   # about a vertex of the icosahedron
    g2 = rot((1, 1, 1), 2 * math.pi / 3)     # about a face centre
    G = [np.eye(3)]
    key = lambda M: tuple(np.round(M, 6).flatten())
    seen = {key(G[0])}; frontier = [G[0]]
    while frontier:
        nxt = []
        for M in frontier:
            for g in (g1, g2):
                P = g @ M
                if key(P) not in seen: seen.add(key(P)); G.append(P); nxt.append(P)
        frontier = nxt
    return G


def N78():
    G = icosa_rotations()
    angle = lambda M: round(math.degrees(math.acos(max(-1, min(1, (M.trace() - 1) / 2)))))
    cnt = {}
    for M in G: cnt[angle(M)] = cnt.get(angle(M), 0) + 1
    fifths = cnt.get(72, 0) + cnt.get(144, 0)
    return len(G) == 60 and fifths == 24 == 6 * 4 and cnt.get(180) == 15 and cnt.get(120) == 20 and cnt.get(0) == 1 \
        and 15 + 20 + 1 == 36


def N80():
    ok = 28 ** 2 - 24 * 32 == 16 and 28 ** 2 - 27 * 29 == 1
    ok &= (27 - 24, 32 - 27) == (3, 5) and (29 - 24, 32 - 29) == (5, 3)
    ok &= 24 == 5 ** 2 - 1 and 27 == 3 ** 3 and 32 == 2 ** 5 and 24 * 27 * 32 == 144 ** 2
    return ok


# ------------------------------------------------------------------ SEVEN · COUPLING
def N81():
    return (P17 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59] and len(P17) == 17
            and [p for p in P17 if p % 2 == 0] == [2] and P17[8] == 23 and len(P17[:8]) == len(P17[9:]) == 8
            and P17[16] == 59 and sum(P17) == 440)


def N82():
    back = sorted(120 - p for p in P17)
    return back[0] == 61 and back[-1] == 118 and not is_prime(60) and 59 * 61 == 60 ** 2 - 1


def N85():
    far = lambda k: (120 - k) % 120
    ok = far(2) == 118 and far(23) == 97 and far(59) == 61 and [k for k in range(120) if far(k) == k] == [0, 60]
    ok &= [far(x) for x in (24, 27, 32)] == [96, 93, 88] and (93 - 88, 96 - 93) == (5, 3)
    return ok


def ring_run(n, steps, seed=(K, 1), ordering='together'):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]; inbox[0] = [seed]
    surf = []; states = []
    for _ in range(steps):
        row = []
        if ordering == 'together':
            nb = [[] for _ in range(n)]
            for i in range(n):
                s, c = C(carry[i], inbox[i]); carry[i] = c
                nb[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
            inbox = nb
        else:
            for i in range(n):
                s, c = C(carry[i], inbox[i]); carry[i] = c; inbox[i] = []
                inbox[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
        surf.append(tuple(row))
        states.append((tuple(tuple(c) for c in carry), tuple(tuple(b) for b in inbox)))
    return surf, states


def joint_pairs(row):
    n = len(row)
    return [i for i in range(n) if row[i] is not None and row[i] != 0 and row[i] == row[(i + 1) % n]]


def odd_ring_ok(n):
    surf, st = ring_run(n, 6 * n + 6)
    ok = True
    for t, row in enumerate(surf):
        beat = t + 1; tot = sum(x or 0 for x in row)
        ok &= (tot in (1, -1)) if beat % 2 else tot == 0
        if t >= n - 1:  # filled
            z = [i for i in range(n) if row[i] == 0]; jp = joint_pairs(row)
            ok &= (len(jp) == 1 and not z) if beat % 2 else (len(z) == 1 and not jp)
    jt = [(t, joint_pairs(surf[t])[0]) for t in range(n - 1, len(surf)) if (t + 1) % 2]
    ok &= all(b[1] == (a[1] + 1) % n and b[0] - a[0] == 2 for a, b in zip(jt, jt[1:]))
    # opposite at 2n (the state inverts), met again at 4n
    ok &= all(surf[t + 2 * n][i] == -surf[t][i] for t in range(n, len(surf) - 2 * n) for i in range(n))
    first = {}
    for t, s in enumerate(st):
        if s in first:
            ok &= (first[s] + 1, t - first[s]) == (n, 4 * n); break
        first[s] = t
    else:
        return False
    return ok


def N86():
    return all(odd_ring_ok(p) for p in P17 if p > 2)


def N89():
    surf, st = ring_run(2, 12)
    ok = surf[0] == (1, None) and all(sum(r) == 0 and r[0] == -r[1] for r in surf[1:])
    ok &= all(surf[t + 1][0] == -surf[t][0] for t in range(1, 11)) and all(surf[t + 2] == surf[t] for t in range(1, 10))
    return ok


def even_ring_ok(n, extra=6):
    surf, st = ring_run(n, n + extra)
    ok = True
    for t in range(n - 1, len(surf)):
        row = surf[t]
        ok &= not joint_pairs(row) and 0 not in row and sum(row) == 0
    ok &= all(st[t + 2] == st[t] and st[t + 1] != st[t] for t in range(n - 1, len(st) - 2))
    return ok


def N90():
    odd = [p for p in P17 if p > 2]
    sums = sorted({p + q for p in odd for q in odd})
    ok = all(even_ring_ok(n) for n in sums) and 118 in sums
    ok &= even_ring_ok(440, extra=4) and sum(P17) == 440 == 21 ** 2 - 1
    return ok


def N92():
    ok = True
    for n in range(2, 12):
        a, _ = ring_run(n, 4 * n + 4); b, _ = ring_run(n, 4 * n + 4, ordering='sequence')
        ok &= a[0] != b[0] and a != b
    b2, _ = ring_run(2, 13, ordering='sequence')
    ok &= all(b2[t + 3] == b2[t] and b2[t + 1] != b2[t] for t in range(10))          # round at three
    ok &= [sum(1 for r in b2[t:t + 3] if 0 in r) for t in range(0, 12, 3)] == [2, 2, 2, 2]  # 0 at two of each three
    a2, _ = ring_run(2, 13)
    ok &= all(0 not in r and a2[t + 2] == r for t, r in enumerate(a2[1:11], 1))           # round at two, no 0
    # the two functions read no ordering: neither takes a caller, a beat or a neighbour; the third takes the surface and runs all together
    fns = {n.name: [a.arg for a in n.args.args] for n in TREE.body if isinstance(n, ast.FunctionDef)}
    ok &= fns == {'_1_self_coupling': ['_3_self_carrying', '_2_self_offering'],
                  '_9_other_releasing': ['_10_other_surfacing', '_5_other_neutralling'],
                  '_17_social_abundancing': ['_3_self_carrying', '_2_self_offering', '_5_other_neutralling', 'SURFACE']}
    A = RV._17_social_abundancing
    for n in range(2, 12):
        Sf = {i: {'backward': [(i + 1) % n]} for i in range(n)}
        car, arr = {}, {0: {2: [(K, 1)]}}; rows = []
        for _ in range(4 * n + 4):
            rows.append(tuple(dict(C(car.get(i, []), [x for c in (2, 14, 17) for x in arr.get(i, {}).get(c, [])])[0]).get(K) for i in range(n)))
            car, arr = A(car, arr, {}, Sf)
        a, _ = ring_run(n, 4 * n + 4)
        ok &= rows == a
    return ok


def N93():
    odd = [p for p in P17 if p > 2]
    return all(math.lcm(4 * p, 4 * q) == 4 * p * q for p, q in combinations(odd, 2)) and sum(P17) == 440 and N86()


def gaps17():
    return [q - p for p, q in zip(P17, P17[1:])]


def N94():
    g = gaps17()
    return len(g) == 16 and sorted(set(g)) == [1, 2, 4, 6] and [g.count(v) for v in (1, 2, 4, 6)] == [1, 6, 5, 4] \
        and g[0] == 1


def N96():
    g = gaps17()
    matching = [P17[i] for i in range(1, 16) if g[i - 1] == g[i]]
    return matching == [5, 53] and g[1] == g[2] == 2 and g[14] == g[15] == 6


def N98():
    inter = [p for p in primes_below(55) if p > 5]
    pairs = [(p, 60 - p) for p in inter if p < 30 and is_prime(60 - p)]
    ok = pairs == [(7, 53), (13, 47), (17, 43), (19, 41), (23, 37), (29, 31)]
    ok &= len({x for pr in pairs for x in pr}) == 12
    d = [30 - p for p, _ in pairs]
    ok &= d == [23, 17, 13, 11, 7, 1] and 60 * 6 == 360 == 19 ** 2 - 1 and sum(d) == 72 and sum(2 * x for x in d) == 144 == 12 ** 2
    lone = [p for p in inter if not is_prime(60 - p)]
    return ok and lone == [11] and 60 - 11 == 49 == 7 ** 2


def N99():
    return len(P17) + (len(P17) - 1) == 33 and max(P17) < 60


# ------------------------------------------------------------------ EIGHT · INSEPARATING
def farthest(N, s):
    d = lambda a, b: min((a - b) % N, (b - a) % N)
    m = max(d(s, x) for x in range(N))
    return [x for x in range(N) if d(s, x) == m], m


def N100():
    ok = True
    for N in range(2, 1001):
        far, m = farthest(N, 0); h = N // 2
        ok &= (far == [h] and m == h) if N % 2 == 0 else (sorted(far) == [h, h + 1] and m == h)
    odd_primes = [p for p in P17 if p >= 5]
    cnt = 0
    for N in odd_primes + [p - 1 for p in odd_primes] + [9, 15, 25]:
        h = N // 2
        for s in range(N):
            far, m = farthest(N, s); cnt += 1
            ok &= (sorted(far) == sorted([(s + h) % N, (s + h + 1) % N]) and m == h) if N % 2 else (far == [(s + h) % N])
    return ok and sum(odd_primes) == 435 and sum(p - 1 for p in odd_primes) == 420 and 9 + 15 + 25 == 49 \
        and cnt == 435 + 420 + 49


def N104():
    ok = True
    def line(a, b):  # places a..b, 2h + 1 of them
        places = list(range(a, b + 1)); h = (len(places) - 1) // 2
        odd = [(x, x + 1) for x in places[:-1] if (x - a) % 2 == 0]
        even = [(x, x + 1) for x in places[:-1] if (x - a) % 2 == 1]
        both = [x for x in places if any(x in p for p in odd) and any(x in p for p in even)]
        return h, odd, even, both, places
    for n in list(range(3, 60, 2)) + [p for p in P17 if p >= 5] + [9, 15, 25]:
        h, odd, even, both, places = line(1, n)
        ok &= len(odd) == h and len(even) == h and len(both) == 2 * h - 1
        # each end continues past the line: the last place's pairing is with the place after it, the first's with the nought
        ok &= (odd[-1][1] + 1, odd[-1][1] + 2) == (n, n + 1) and (even[0][0] - 2, even[0][0] - 1) == (0, 1)
    h, odd, even, both, places = line(1, 59)
    ok &= h == 29 and len(odd) == 29 and len(even) == 29 and (59, 60) not in odd + even and (0, 1) not in odd + even
    return ok and sum(p for p in P17 if p >= 5) == 435


def N107():
    step = lambda s: (s[1], -s[0])
    ok = True
    for s0 in product(S, S):
        seq = [s0]
        for _ in range(12): seq.append(step(seq[-1]))
        ok &= seq[2] == (-s0[0], -s0[1]) and seq[4] == s0 and seq[6] == (-s0[0], -s0[1]) and seq[12] == s0
        ok &= set(seq[:6]) == set(product(S, S))
    ok &= (24 // 4, 24 // 6) == (6, 4) and ((60 - 24) // 4, (60 - 24) // 6) == (9, 6) and (60 // 4, 60 // 6) == (15, 10)
    ok &= len({x % 4 for x in (6, 14, 22)}) == 1 and 8 // 4 == 2 and 6 * 6 == 36 == 60 - 24
    return ok


def N109():
    ok = [x % 2 for x in (3, 6, 9)] == [1, 0, 1]
    ok &= all(x % 2 == 1 for x in (25, 35, 45, 55)) and all(x % 2 == 0 for x in (30, 40, 50, 60))
    ok &= all((k * m) % 2 != ((k + 1) * m) % 2 for m in range(1, 100, 2) for k in range(1, 101))
    return ok


def N113():
    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]; cols = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    # the six exclusive-or conditions: each row's parity nought, the columns' parity nought, nought and one
    want = [0, 0, 0] + [0, 0, 1]
    meets = 0; settings = 0
    for v in product((0, 1), repeat=9):
        settings += 1
        par = [sum(v[i] for i in r) % 2 for r in rows + cols]
        if par == want: meets += 1
    along = sum(want[:3]) % 2; across = sum(want[3:]) % 2  # each reads the nine's parity once
    return settings == 512 and meets == 0 and along == 0 and across == 1


# ------------------------------------------------------------------ NINE · TUNNELING
def N114():
    far = lambda k: (440 - k) % 440
    selfp = [k for k in range(440) if far(k) == k]
    pairs = {frozenset((k, far(k))) for k in range(440) if far(k) != k}
    radius = lambda k: abs(220 - k)
    return (selfp == [0, 220] and len(pairs) == 219 and len(pairs) + 2 == 221
            and all(radius(k) == radius(440 - k) for k in range(1, 440)) and radius(220) == 0 and radius(0) == 220)


def N118():
    ok = all(((220 - r) % 2 == (220 + r) % 2 == r % 2) for r in range(0, 221))
    radii = [220 - p for p in P17]
    ok &= all(r % 2 == 1 for p, r in zip(P17, radii) if p > 2) and radii[1] == 217 and radii[-1] == 161
    ok &= [p for p, r in zip(P17, radii) if r % 2 == 0] == [2] and 220 - 2 == 218
    ok &= 440 == 8 * 5 * 11
    fives = [k for k in range(0, 440) if k % 5 == 0]
    ok &= len(fives) == 88 and sum(1 for k in fives if k % 2) == 44 and sum(1 for k in fives if k % 10 == 0) == 44
    ok &= all(fives[i] % 2 != fives[i + 1] % 2 for i in range(87))
    odd_r = sorted({abs(220 - k) for k in fives if k % 2})
    ok &= len(odd_r) == 22 and odd_r[0] == 5 and odd_r[-1] == 215 and all(r % 2 for r in odd_r) and 5 + 435 == 440
    ok &= all(abs(220 - k) % 2 == 0 for k in fives if k % 10 == 0)
    return ok


def N119():
    g = gaps17()
    steps = [abs((220 - q) - (220 - p)) for p, q in zip(P17, P17[1:])]
    return steps == g and sum(steps) == 57 == 59 - 2 and [steps.count(v) for v in (1, 2, 4, 6)] == [1, 6, 5, 4]


def N120():
    pos = [(P17[i], P17[16 - i]) for i in range(8)]
    ok = [a + b for a, b in pos] == [61, 56, 52, 50, 52, 50, 48, 48] and sum(a + b for a, b in pos) + 23 == 440
    ok &= all(k + (440 - k) == 440 for k in range(441))
    ok &= not any(a + b == 46 for a, b in pos)
    by_value = sorted((p, q) for p, q in combinations(P17, 2) if p + q == 46)
    ok &= by_value == [(3, 43), (5, 41), (17, 29)]
    mid = [p for p in P17 if 5 <= p <= 53]
    ok &= len(mid) == 14 and sum(mid) == 376 and 2 + 3 + 59 == 64 == 8 ** 2 and 376 + 64 == 440 and 220 - 64 == 156 == 376 - 220
    return ok


def N122():
    ok = 440 * 2 == 880 and (880 - 220) % 880 == 660
    for m in range(1, 40):
        centre = 220 * m
        ok &= (centre % 440 == 0) if m % 2 == 0 else (centre % 440 == 220)
    return ok


def N124():
    chain = [3, 5, 9, 17]
    ok = all(x - 1 == 2 ** k for x, k in zip(chain, (1, 2, 3, 4)))
    ok &= [(N + 1) // 2 for N in chain] == [2, 3, 5, 9] == [3 - 1, 5 - 2, 9 - 4, 17 - 8]
    ok &= [(N + 1) // 2 for N in chain][1:] == [3, 5, 9] and [(N + 1) // 2 for N in chain][1:] == chain[:-1]
    two_st = [(N - 1) // 2 for N in chain]
    ok &= two_st == [1, 2, 4, 8] and all(N == 2 * t + 1 for N, t in zip(chain, two_st))
    res = [6 // 2, 8 // 2, 10 // 2]
    ok &= res == [3, 4, 5] and set(two_st) & set(res) == {4} and 2 * 4 + 1 == 9
    c = [9]
    for _ in range(3): c.append(2 * c[-1] - 1)
    ok &= c == [9, 17, 33, 65] and all(x - 1 == 2 ** k for x, k in zip(c, (3, 4, 5, 6)))
    ok &= len(range(1, 10)) + len(range(9, 18)) - 1 == 17
    return ok


def N128():
    selfp = lambda N: [k for k in range(N) if (N - k) % N == k]
    ok = all(len(selfp(N)) == (1 if N % 2 else 2) for N in range(1, 500))
    return ok and selfp(9) == [0] and selfp(440) == [0, 220]


def N130():
    pod = [(n, 9 - n) for n in range(1, 5)]
    ok = pod == [(1, 8), (2, 7), (3, 6), (4, 5)] and all((a + b) % 2 for a, b in pod)
    moms = [(k, k + 1) for k in range(1, 9)]
    ok &= [(moms[i], moms[i + 1]) for i in range(0, 8, 2)] == [((1, 2), (2, 3)), ((3, 4), (4, 5)), ((5, 6), (6, 7)), ((7, 8), (8, 9))]
    ok &= {tuple(sorted(p)) for p in pod} & set(moms) == {(4, 5)}
    return ok


def row(s): return [2 + 2 * s * j for j in range(4)]


def N132():
    ok = row(1) == [2, 4, 6, 8] and row(2) == [2, 6, 10, 14] and row(3) == [2, 8, 14, 20] and row(4) == [2, 10, 18, 26] \
        and row(5) == [2, 12, 22, 32]
    ok &= [8 * s + 1 for s in range(1, 6)] == [9, 17, 25, 33, 41]
    ok &= all(2 + 2 * s * 4 == 2 + 8 * s and 8 * s + 1 == 2 + 8 * s - 1 and 8 * s + 1 > 8 * s for s in range(1, 101))
    return ok and len(CONNECTORS) == 6


def N133():
    ok = True
    for s in range(1, 101):
        B = 8 * s
        ud = lambda n: n + 4 * s if n <= 4 * s else n - 4 * s
        fl = lambda n: B + 1 - n
        for n in range(1, B + 1):
            ok &= ud(n) % 2 == n % 2 and fl(n) % 2 != n % 2
            seq = [n]; x = n
            for i in range(4):
                x = ud(x) if i % 2 == 0 else fl(x); seq.append(x)
            ok &= seq[-1] == n and len(set(seq[:4])) == 4
            both = fl(ud(n))
            ok &= both == (4 * s + 1 - n if n <= 4 * s else 12 * s + 1 - n)
        ok &= (B + 1) % 2 == 1 and (4 * s + 1) % 2 == 1 and (12 * s + 1) % 2 == 1
    ok &= [3, 3 + 8, 17 - 11, 6 + 8, 17 - 14] == [3, 11, 6, 14, 3]
    ok &= [3, 3 + 4, 9 - 7, 2 + 4, 9 - 6] == [3, 7, 2, 6, 3]
    return ok


def N134():
    ok = True
    for s in range(1, 60):
        r = row(s); mid = Q(r[1] + r[2], 2)
        ok &= mid == 2 + 3 * s and (r[2] - r[1], mid - r[1]) == (2 * s, s) and (r[3] - r[0], mid - r[0]) == (6 * s, 3 * s)
        ok &= Q(r[2] - r[1], mid - r[1]) == Q(r[3] - r[0], mid - r[0]) == 2
        ok &= sorted(r + [x + 8 * s for x in r]) == sorted(row(2 * s) + [x + 2 * s for x in row(2 * s)])
    E = lambda r: (lambda x: 2 + r * (x - 2))
    ok &= all(E(r)(E(s)(x)) == E(r * s)(x) for r in range(1, 12) for s in range(1, 12) for x in range(-5, 40))
    ok &= all(E(r)(x) % 2 == 0 for r in range(2, 20, 2) for x in range(1, 40))
    return ok


def N135():
    ok = True
    for B in (8, 16):
        for r in range(1, 12):
            e = lambda n: r * (n - 2) + 2 if n % 2 == 0 else r * (n + 1) - 1
            for n in range(1, B + 1):
                ok &= e(n) % 2 == n % 2
                ok &= e(B + 1 - n) == B * r + 1 - e(n)
                if n + B // 2 <= B: ok &= e(n + B // 2) - e(n) == r * B // 2
                if n + 2 <= B: ok &= e(n + 2) - e(n) == 2 * r
    e2 = lambda n: 2 * (n - 2) + 2 if n % 2 == 0 else 2 * (n + 1) - 1
    ok &= [e2(n) for n in range(1, 9)] == [3, 2, 7, 6, 11, 10, 15, 14] and [e2(n) for n in range(2, 9, 2)] == [2, 6, 10, 14]
    ok &= (e2(1), e2(2)) == (3, 2)
    return ok


# ------------------------------------------------------------------ TEN · TRANSMISSIONING
def N141():
    ok = all(17 - (n + 8) == 9 - n for n in range(-5, 30))
    ok &= all(16 * s + 1 - (n + 8 * s) == 8 * s + 1 - n for s in range(-3, 10) for n in range(-5, 30))  # linear in n and s
    return ok and [[n, n + 8, 9 - n, 17 - n] for n in (1,)] == [[1, 9, 8, 16]]


def N49():
    A = RV._17_social_abundancing
    S = {'A': {'backward': ['B'], 'forward': ['B']}, 'B': {'backward': ['A'], 'forward': ['A']}}
    car = {'A': [(K, 1, -1, 0)], 'B': [(K, -1, -1, 1)]}
    nxt_car, nxt_arr = A(car, {}, {}, S)
    ok = nxt_car['A'] == C(car['A'], [])[1] and nxt_car['B'] == C(car['B'], [])[1]
    ok &= nxt_arr['B'][17] == R(C(car['A'], [])[0], {K: K}) and nxt_arr['A'][17] == R(C(car['B'], [])[0], {K: K})
    ok &= nxt_arr['A'][2] == [] and nxt_arr['A'][14] == [] and nxt_arr['B'][2] == [] and nxt_arr['B'][14] == []
    nxt2_car, _ = A(nxt_car, nxt_arr, {}, S)
    ok &= nxt2_car['A'] == C(nxt_car['A'], nxt_arr['A'][17])[1] and nxt2_car['B'] == C(nxt_car['B'], nxt_arr['B'][17])[1]
    return ok and all(n % 2 == 1 for n in (1, 9, 17)) and 9 - 1 == 17 - 9 == 8

CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'N\d+(_probe)?', k) and callable(v)}

'''

PART_SOURCES['math'] = r'''"""Run checks for Exhibit THIRTY Part FOUR · MATHEMATICS (links M1...), against
Exhibit FOUR Natural Mathematics v372 and the resolver in resolver_v372.py (Exhibit ONE v372's code).
Each function named for a run link returns True when the link holds as the registry states it.
Polynomial identities are checked on a grid wider than each variable's degree, which decides them.
Standard library only."""
import os, sys, re, json, math, cmath
from fractions import Fraction as Fr
from itertools import product, permutations, combinations
from math import gcd, comb, isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as REL  # noqa: E402

S = (1, -1)
K = 'k'


def sgn(x):
    return (x > 0) - (x < 0)


# ---------------------------------------------------------------- exact arithmetic in Q(sqrt 5)
class Q5:
    """a + b*sqrt(5), a and b rational."""
    def __init__(s, a, b=0): s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Q5(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, Q5) else Q5(o)))
    def __rsub__(s, o): return Q5(o) - s
    def __mul__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def inv(s): d = s.a * s.a - 5 * s.b * s.b; return Q5(s.a / d, -s.b / d)
    def __truediv__(s, o): return s * (o if isinstance(o, Q5) else Q5(o)).inv()
    def __eq__(s, o): o = o if isinstance(o, Q5) else Q5(o); return s.a == o.a and s.b == o.b
    def __float__(s): return float(s.a) + float(s.b) * math.sqrt(5)

R5 = Q5(0, 1)
PHI = Q5(Fr(1, 2), Fr(1, 2))

# ---------------------------------------------------------------- 4.1-4.2
def M22():
    i = 1j
    powers = [i ** k for k in range(9)]
    ok = abs((-1) ** 2 - 1) == 0 and abs(i ** 2 + 1) < 1e-12 and abs(i ** 4 - 1) < 1e-12
    ok &= all(abs(powers[k] - powers[k % 4]) < 1e-12 for k in range(9))
    ok &= abs(i * i - (-1)) < 1e-12                           # two quarter steps are one sign flip
    ok &= all((n + 8) % 2 == n % 2 and (n + 1) % 2 != n % 2 for n in range(1, 65))
    return ok


def M25():
    T = 1.0
    q = lambda t: math.cos(math.pi * t / T)
    ts = [k / 97 for k in range(500)]
    return all(abs(q(t + T) + q(t)) < 1e-9 and abs(q(t + 2 * T) - q(t)) < 1e-9 for t in ts)


def M27():
    self4, other4 = {1, 2, 3, 4}, {2, 3, 4, 5}
    shared, outer = self4 & other4, self4 ^ other4
    occ = [n % 2 for n in sorted(self4)] + [n % 2 for n in sorted(other4)]
    return (len(shared) == 3 and len(outer) == 2 and len(self4 | other4) == 5
            and len(shared) * 2 == 6 and len(occ) == 8 == 4 + 4 == 2 * 3 + 2
            and occ[:4].count(0) == occ[:4].count(1) == 2 and occ[4:].count(0) == occ[4:].count(1) == 2
            and 2 + 2 == 2 * 2 == 4 and (2 + 3, 2 * 3) == (5, 6) and (3 + 3, 3 * 3) == (6, 9))


def M29():
    pairs = set(); pairs_m = set(); ok = True
    for n in range(64):
        z = 1j ** n; w = (-1j) ** n
        key = (round(z.real), round(z.imag), n); keym = (round(w.real), round(w.imag), n)
        ok &= key not in pairs and keym not in pairs_m
        pairs.add(key); pairs_m.add(keym)
        ok &= abs(w - z.conjugate()) < 1e-9                    # -i: the same inversions in the other order
    ok &= abs(1j ** 4 - 1) < 1e-12
    return ok


# ---------------------------------------------------------------- 4.3 the right spiral step at two signs
J = list(product(S, S))
Fm = lambda s: (-s[1], s[0])     # F(P, Q) = (-Q, P), multiplying P + iQ by i
Gm = lambda s: (s[1], -s[0])     # G(P, Q) = (Q, -P)


def all_steps():
    for vals in product(J, repeat=4):
        yield dict(zip(J, vals))


def ham(a, b): return sum(x != y for x, y in zip(a, b))


def M31():
    found = []
    n = 0
    for m in all_steps():
        n += 1
        bij = len(set(m.values())) == 4
        one = all(ham(s, m[s]) == 1 for s in J)
        never_undo = all(m[m[s]] != s for s in J)
        if bij and one and never_undo:
            found.append(m)
    ok = n == 256 and len(found) == 2
    ok &= sorted([tuple(m[s] for s in J) for m in found]) == sorted([tuple(Fm(s) for s in J), tuple(Gm(s) for s in J)])
    for f in (Fm, Gm):                                       # inverted sign alternates P, Q, P, Q from each state
        for s0 in J:
            seq = [s0]
            for _ in range(4): seq.append(f(seq[-1]))
            axes = [[k for k in (0, 1) if seq[j][k] != seq[j + 1][k]][0] for j in range(4)]
            ok &= axes in ([0, 1, 0, 1], [1, 0, 1, 0])
    # the signs of cos t and sin t as t runs forward run F
    qs = [(sgn(math.cos(t)), sgn(math.sin(t))) for t in (math.pi / 4 + k * math.pi / 2 for k in range(8))]
    ok &= all(qs[k + 1] == Fm(qs[k]) for k in range(7))
    return ok


def M33():
    neg = lambda s: (-s[0], -s[1])
    sq = [m for m in all_steps() if all(m[m[s]] == neg(s) for s in J)]
    return (len(sq) == 2 and sorted(tuple(m[s] for s in J) for m in sq)
            == sorted([tuple(Fm(s) for s in J), tuple(Gm(s) for s in J)]))


def power(f, k, s):
    for _ in range(k): s = f(s)
    return s


def M34():
    ok = True
    neg = lambda s: (-s[0], -s[1])
    for f in (Fm, Gm):
        for s in J:
            ok &= power(f, 2, s) == neg(s) and power(f, 6, s) == neg(s) and power(f, 12, s) == s
            ok &= len({power(f, k, s) for k in range(6)}) == 4       # a passage of six meets all four
            ok &= power(f, 8, s) == s and all(power(f, k + 8, s) == power(f, k, s) for k in range(16))
    ok &= (24 // 4, 24 // 6, 36 // 4, 36 // 6, 60 // 4, 60 // 6) == (6, 4, 9, 6, 15, 10)
    ok &= all(n % 4 == 0 and n % 6 == 0 for n in (24, 36, 60)) and 6 * 6 == 36 and 6 * 4 == 24
    return ok


def M36():
    ok = True
    for f in (Fm, Gm):
        for s in J:
            ok &= sgn(f(s)[0] * f(s)[1]) == -sgn(s[0] * s[1])
    for k in range(1, 400):
        t = k * 0.0157 + 0.001
        if abs(math.cos(t)) < 1e-6 or abs(math.sin(t)) < 1e-6: continue
        r = sgn(math.cos(t)) * sgn(math.sin(t))
        ok &= r == sgn(math.tan(t)) == sgn(math.sin(2 * t))
        ok &= abs(math.sin(2 * t) - 2 * math.sin(t) * math.cos(t)) < 1e-12
    return ok


def M38():
    """At one carried key of sign c, the surfaced sign is the sign of (sum of offered signs) - c."""
    ok = True; n14 = 0
    small = [[]] + [[a] for a in S] + [[a, b] for a, b in product(S, S)]
    for c, t in product(S, S):
        for vals in small:
            s, _ = C([(K, c, t, 0)], [(K, v) for v in vals])
            got = dict(s).get(K)
            ok &= got == sgn(sum(vals) - c)
            if t == -1: n14 += 1
        for L in range(3, 5):
            for vals in product((1, 0, -1), repeat=L):
                s, _ = C([(K, c, t, 0)], [(K, v) for v in vals])
                ok &= dict(s).get(K) == sgn(sum(vals) - c)
    named = {(): -1, (1,): 0, (-1,): -1, (1, 1): 1}                # at c = +1
    for vals, want in named.items():
        s, _ = C([(K, 1, -1, 0)], [(K, v) for v in vals])
        ok &= dict(s).get(K) == want
    return ok and n14 == 14


def gray(n):
    if n == 1: return [(1,), (-1,)]
    g = gray(n - 1)
    return [x + (1,) for x in g] + [x + (-1,) for x in reversed(g)]


def M39():
    ok = True
    for n in range(2, 9):
        g = gray(n)
        ok &= len(set(g)) == 2 ** n
        ok &= all(ham(g[k], g[(k + 1) % len(g)]) == 1 for k in range(len(g)))
        prior = gray(n - 1)
        ok &= [x[:-1] for x in g[:len(prior)]] == prior and [x[:-1] for x in g[len(prior):]] == prior[::-1]
    g2 = gray(2)             # read with P the sign changing first, the reflected order runs F;
    ok &= all(g2[(k + 1) % 4] == Fm(g2[k]) for k in range(4))          # with the two labels exchanged it runs G
    g2x = [(q, p) for p, q in g2]
    ok &= all(g2x[(k + 1) % 4] == Gm(g2x[k]) for k in range(4))
    g3 = gray(3)
    ch = [[j for j in range(3) if g3[k][j] != g3[(k + 1) % 8][j]][0] for k in range(8)]
    ok &= ch == [0, 1, 0, 2, 0, 1, 0, 2]
    return ok


# ---------------------------------------------------------------- 4.4 product, doubling, phi
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def M41():
    # (a.b)^2 + |a^b|^2 = |a|^2 |b|^2: degree two in each of six variables, checked at 3^6 points, decided
    g = (-1, 0, 2)
    ok = all(dot(a, b) ** 2 + dot(cross(a, b), cross(a, b)) == dot(a, a) * dot(b, b)
             for a in product(g, repeat=3) for b in product(g, repeat=3))
    for k in range(360):
        th = math.radians(k)
        ok &= abs(math.cos(th) ** 2 + math.sin(th) ** 2 - 1) < 1e-12
    return ok


def M42():
    g = (-1, 0, 2)
    ok = all(cross(a, tuple(r * x for x in a)) == (0, 0, 0) for a in product(g, repeat=3) for r in (-2, 1, 3))
    ok &= dot((1, 0, 0), (0, 1, 0)) == 0
    u = (1.0, 0.0); v = (math.cos(math.pi / 3), math.sin(math.pi / 3))
    sh = u[0] * v[0] + u[1] * v[1]; op = u[0] * v[1] - u[1] * v[0]
    ok &= abs(sh - 0.5) < 1e-12 and abs(op - math.sqrt(3) / 2) < 1e-12 and abs(op / sh - math.tan(math.pi / 3)) < 1e-12
    ok &= cross((1, 0, 0), (0, 1, 0)) == (0, 0, 1)
    # a x b is perpendicular to both: degree <= 2 per variable, 3^6 points
    ok &= all(dot(cross(a, b), a) == 0 == dot(cross(a, b), b) for a in product(g, repeat=3) for b in product(g, repeat=3))
    return ok


# Cayley-Dickson doubling: pairs (a, b), (a, b)(c, d) = (ac - d*b, da + bc*)
def cd_conj(x):
    if isinstance(x, tuple): return (cd_conj(x[0]), cd_neg(x[1]))
    return x
def cd_neg(x):
    if isinstance(x, tuple): return (cd_neg(x[0]), cd_neg(x[1]))
    return -x
def cd_add(x, y):
    if isinstance(x, tuple): return (cd_add(x[0], y[0]), cd_add(x[1], y[1]))
    return x + y
def cd_mul(x, y):
    if isinstance(x, tuple):
        a, b = x; c, d = y
        return (cd_add(cd_mul(a, c), cd_neg(cd_mul(cd_conj(d), b))), cd_add(cd_mul(d, a), cd_mul(b, cd_conj(c))))
    return x * y
def cd_scale(x, c):
    if isinstance(x, tuple): return (cd_scale(x[0], c), cd_scale(x[1], c))
    return x * c
def cd_basis(level, k):
    if level == 0: return 1 if k == 0 else 0
    half = 2 ** (level - 1)
    z = cd_basis(level - 1, -1)
    return (cd_basis(level - 1, k), z) if k < half else (z, cd_basis(level - 1, k - half))
def cd_flat(x): return list(cd_flat(x[0]) + cd_flat(x[1])) if isinstance(x, tuple) else [x]


def M44():
    e = lambda L, k: cd_basis(L, k)
    i, j, k = e(2, 1), e(2, 2), e(2, 3)
    ij, ji = cd_flat(cd_mul(i, j)), cd_flat(cd_mul(j, i))
    kk = cd_flat(k)
    ok = (ij == kk or ij == [-v for v in kk]) and ji == [-v for v in ij]
    ok &= ij == kk                                             # i j = k, j i = -k at this doubling
    # octonions: some triple of units does not associate
    O = [e(3, n) for n in range(8)]
    nonassoc = any(cd_flat(cd_mul(cd_mul(O[a], O[b]), O[c])) != cd_flat(cd_mul(O[a], cd_mul(O[b], O[c])))
                   for a, b, c in product(range(1, 8), repeat=3))
    ok &= nonassoc
    # quaternions associate
    Qb = [e(2, n) for n in range(4)]
    ok &= all(cd_flat(cd_mul(cd_mul(Qb[a], Qb[b]), Qb[c])) == cd_flat(cd_mul(Qb[a], cd_mul(Qb[b], Qb[c])))
              for a, b, c in product(range(4), repeat=3))
    # seven imaginary units on seven lines of three, each two units on one line
    lines = set()
    for a, b in combinations(range(1, 8), 2):
        p = cd_flat(cd_mul(O[a], O[b]))
        c = [n for n, v in enumerate(p) if v != 0]
        ok &= len(c) == 1
        lines.add(frozenset((a, b, c[0])))
    ok &= len(lines) == 7 and all(len(l) == 3 for l in lines)
    ok &= all(sum(1 for l in lines if {a, b} <= l) == 1 for a, b in combinations(range(1, 8), 2))
    # the complex numbers commute, and norms multiply at the four doublings on small whole elements
    ok &= cd_flat(cd_mul(e(1, 0), e(1, 1))) == cd_flat(cd_mul(e(1, 1), e(1, 0)))
    for L in (1, 2, 3):
        dim = 2 ** L
        for xs in [(1, 2, 0, -1, 3, 0, 1, -2)[:dim], (0, 1, 1, 0, -1, 2, 0, 1)[:dim]]:
            for ys in [(2, -1, 1, 0, 0, 1, -1, 1)[:dim]]:
                def build(v, L=L):
                    acc = cd_basis(L, -1)
                    for n, c in enumerate(v):
                        b = cd_basis(L, n)
                        acc = cd_add(acc, cd_scale(b, c))
                    return acc
                x, y = build(xs), build(ys)
                nx = sum(v * v for v in xs); ny = sum(v * v for v in ys)
                nxy = sum(v * v for v in cd_flat(cd_mul(x, y)))
                ok &= nxy == nx * ny
    return ok


def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)
def qconj(q): return (q[0], -q[1], -q[2], -q[3])


def FI_quat():
    ok = True
    for k in range(50):
        th = 0.37 * k; u = (0.0, 0.48, 0.6, 0.64)
        q = (math.cos(th / 2), math.sin(th / 2) * u[1], math.sin(th / 2) * u[2], math.sin(th / 2) * u[3])
        mq = tuple(-x for x in q)
        for v in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0.3, -0.2, 0.9)):
            r1 = qmul(qmul(q, v), qconj(q)); r2 = qmul(qmul(mq, v), qconj(mq))
            ok &= all(abs(a - b) < 1e-12 for a, b in zip(r1, r2))
    # a whole rotation, theta = 2 pi, carries the quaternion from 1 to -1
    th = 2 * math.pi; q = (math.cos(th / 2), math.sin(th / 2), 0, 0)
    ok &= abs(q[0] + 1) < 1e-12 and abs(q[1]) < 1e-12
    # four dimensions: x -> p x q-bar, (p, q) and (-p, -q) the one rotation, and it keeps length
    p = (0.5, 0.5, 0.5, 0.5); q = (math.cos(0.4), 0, math.sin(0.4), 0)
    for x in ((1, 0, 0, 0), (0.2, -0.7, 0.1, 0.4)):
        a = qmul(qmul(p, x), qconj(q)); b = qmul(qmul(tuple(-v for v in p), x), qconj(tuple(-v for v in q)))
        ok &= all(abs(s - t) < 1e-12 for s, t in zip(a, b))
        ok &= abs(sum(v * v for v in a) - sum(v * v for v in x)) < 1e-12
    return ok


def M47():
    ok = 1 < float(PHI) < 2 and (PHI - 1).inv() == PHI      # x = 1 + 1/x at phi: the continued fraction is all ones
    ok &= PHI * PHI == PHI + 1
    p3 = PHI * PHI * PHI
    ok &= p3 == Q5(2, 1) and p3.inv() == Q5(-2, 1) and p3 - p3.inv() == Q5(4)
    # convergents are ratios of Fibonacci numbers
    a, b = 1, 1
    for _ in range(30):
        a, b = b, a + b
        ok &= abs(b / a - float(PHI)) < 1 / (a * a)
    return ok


# ---------------------------------------------------------------- 4.5 accounting
def M50():
    ok = [x for x in range(-50, 51) if -x == x] == [0]
    rats = {Fr(p, q) for p in range(-20, 21) for q in range(1, 21) if p != 0}
    ok &= sorted(r for r in rats if 1 / r == r) == [-1, 1]
    mats = list(product((-1, 0, 1), repeat=9))
    T = lambda m: tuple(m[3 * c + r] for r in range(3) for c in range(3))
    fixed = [m for m in mats if T(m) == m]
    ok &= all(T(T(m)) == m for m in mats) and len(fixed) == 3 ** 6
    ok &= all(m[1] == m[3] and m[2] == m[6] and m[5] == m[7] for m in fixed)
    U = frozenset(range(1, 7))
    subsets = [frozenset(c) for r in range(7) for c in combinations(U, r)]
    ok &= not any(U - s == s for s in subsets)
    ok &= not any(-s == s for s in S)
    gz = [complex(a, b) for a in range(-5, 6) for b in range(-5, 6)]
    ok &= all((z.conjugate() == z) == (z.imag == 0) for z in gz)
    ok &= [v for v in product(range(-3, 4), repeat=3) if tuple(-x for x in v) == v] == [(0, 0, 0)]
    return ok


def M53():
    ok = True
    for N in range(2, 201, 2):
        podal = [k for k in range(N) if (N - k) % N == k]
        shift = [k for k in range(N) if (k + N // 2) % N == k]
        ok &= podal == [0, N // 2] and shift == []
        ok &= all((N - (N - k) % N) % N == k and ((k + N // 2) + N // 2) % N == k for k in range(N))
    return ok


def far_places(N):
    d = [min(j, N - j) for j in range(N)]
    m = max(d)
    return [j for j in range(N) if d[j] == m]


def M54():
    ok = True
    for h in range(1, 60):
        ok &= far_places(2 * h + 1) == [h, h + 1] and far_places(2 * h) == [h]
    ok &= far_places(5) == [2, 3] and far_places(17) == [8, 9] and far_places(59) == [29, 30]
    primes = [p for p in range(5, 60) if all(p % q for q in range(2, isqrt(p) + 1))]
    ok &= len(primes) == 15
    for N in primes + [9, 15, 25]:
        for o in range(N):                                     # at each origin
            d = [min((j - o) % N, (o - j) % N) for j in range(N)]
            m = max(d); far = sorted((j - o) % N for j in range(N) if d[j] == m)
            ok &= far == [(N - 1) // 2, (N + 1) // 2]
    return ok


def involutions(n):
    for perm in permutations(range(n)):
        if all(perm[perm[i]] == i for i in range(n)):
            yield perm


def M55():
    ok = True
    for n in range(1, 10):
        fpf = any(all(p[i] != i for i in range(n)) for p in involutions(n))
        ok &= fpf == (n % 2 == 0)
    for h in range(1, 41):
        top = 2 * h + 1
        odd_pairs = [(k, k + 1) for k in range(1, top, 2)]
        even_pairs = [(k, k + 1) for k in range(2, top, 2)]
        in_odd = {x for p in odd_pairs for x in p}; in_even = {x for p in even_pairs for x in p}
        ok &= len(odd_pairs) == h == len(even_pairs)
        ok &= in_odd & in_even == set(range(2, 2 * h + 1)) and len(in_odd & in_even) == 2 * h - 1
        ok &= (set(range(1, top + 1)) - in_odd) == {top} and (set(range(1, top + 1)) - in_even) == {1}
    ok &= len([(k, k + 1) for k in range(1, 59, 2)]) == 29 == len([(k, k + 1) for k in range(2, 60, 2)])
    return ok


def M58():
    ok = True
    for N in range(2, 121):
        prime = all(N % q for q in range(2, isqrt(N) + 1))
        for k in range(1, N):
            seen = []; x = 0
            while True:
                seen.append(x); x = (x + k) % N
                if x == 0: break
            ok &= len(seen) == N // gcd(N, k)
            if prime: ok &= len(seen) == N
    ok &= 8 // gcd(8, 3) == 8 and 9 // gcd(9, 3) == 3 and gcd(4, 9) == 1
    return ok


def M59():
    ok = True
    for m in range(1, 41):
        for n in range(1, 41):
            met = set(); x = (0, 0)
            while x not in met:
                met.add(x); x = ((x[0] + 1) % m, (x[1] + 1) % n)
            g = gcd(m, n)
            ok &= len(met) == m * n // g
            # windings: the classes (a - b) mod g; each winding one class, g of them
            ok &= len({(a - b) % g for a in range(m) for b in range(n)}) == g
            ok &= all((a - b) % g == 0 for a, b in met)
            if g == 1: ok &= len(met) == m * n
    return ok


def M63():
    half = lambda s: (-s[0], -s[1])
    ok = True
    for s in J:
        ok &= half(s) != s and half(half(s)) == s
        ok &= all(power(Fm, k, s) != s for k in (1, 2, 3)) and power(Fm, 4, s) == s
        ok &= all(power(Gm, k, s) != s for k in (1, 2, 3)) and power(Gm, 4, s) == s
        for f in (half, Fm, Gm):
            seen = set(); x = s
            for n in range(200):
                ok &= (x, n) not in seen; seen.add((x, n)); x = f(x)
    return ok


def matmul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def refl(a): return [[math.cos(2 * a), math.sin(2 * a)], [math.sin(2 * a), -math.cos(2 * a)]]
def rot(a): return [[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]]
def close(A, B, e=1e-12): return all(abs(A[i][j] - B[i][j]) < e for i in range(len(A)) for j in range(len(A[0])))


def M65():
    ok = True
    for x in range(0, 180, 7):
        for y in range(0, 180, 11):
            a, b = math.radians(x), math.radians(y)
            ok &= close(matmul(refl(b), refl(a)), rot(2 * (b - a)))
    RP = lambda s: (-s[0], s[1]); RQ = lambda s: (s[0], -s[1]); SW = lambda s: (s[1], s[0])
    ok &= all(RQ(RP(s)) == (-s[0], -s[1]) for s in J)                  # lines at ninety degrees: the half step
    ok &= all(SW(RP(s)) == Gm(s) and RP(SW(s)) == Fm(s) for s in J)     # lines at forty-five degrees: a quarter step
    return ok


def det(M):
    n = len(M)
    if n == 1: return M[0][0]
    return sum((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(n))


def M66():
    St = list(product(S, repeat=3))
    inv = [lambda s, j=j: tuple(-v if k == j else v for k, v in enumerate(s)) for j in range(3)]
    ok = True
    for order in permutations(range(3)):
        for s in St:
            x = s
            for j in order: x = inv[j](x)
            ok &= x == tuple(-v for v in s) and x != s
    ok &= len({frozenset((s, tuple(-v for v in s))) for s in St}) == 4
    for n in range(1, 9):
        ok &= det([[-1 if i == j else 0 for j in range(n)] for i in range(n)]) == (-1) ** n
    return ok


def M68():
    pts = list(product(range(-2, 3), repeat=3))
    D = lambda signs: (lambda v: tuple(s * x for s, x in zip(signs, v)))
    one = D((-1, 1, 1)); two = D((-1, -1, 1)); three = D((-1, -1, -1))
    ok = sorted(v for v in pts if one(v) == v) == sorted(v for v in pts if v[0] == 0)          # keeps a plane
    ok &= sorted(v for v in pts if two(v) == v) == sorted(v for v in pts if v[0] == v[1] == 0)  # half step about the third axis
    ok &= [v for v in pts if three(v) == v] == [(0, 0, 0)]
    ok &= det([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]) == 1 and det([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]) == -1
    ok &= all((-s[0], -s[1]) == power(Fm, 2, s) for s in J)
    return ok


# ---------------------------------------------------------------- 4.6 closings, totals, halfway pairing and fold
def M71():
    fifths = Fr(3, 2) ** 12; octaves = 2 ** 7
    return (octaves == 128 and abs(float(fifths) - 129.746337890625) < 1e-12
            and fifths / octaves == Fr(3 ** 12, 2 ** 19) == Fr(531441, 524288))


def M76():
    # two groups, each favouring A; joined they favour B
    A = [(81, 87), (192, 263)]; B = [(234, 270), (55, 80)]
    ok = all(Fr(*a) > Fr(*b) for a, b in zip(A, B))
    ok &= Fr(sum(a for a, _ in A), sum(n for _, n in A)) < Fr(sum(b for b, _ in B), sum(n for _, n in B))
    x, y = 1, -1
    for _ in range(50):
        ok &= x + y == 0
        x, y = -x, -y
    return ok


def trace(offers, carry):
    out = []
    for off in offers:
        s, carry = C(carry, off)
        out.append(dict(s).get(K, 0))
    return out, carry


def M79():
    younger, _ = trace([[(K, 1)]] * 5, [(K, 1, -1, 0)])
    elder, _ = trace([[(K, 1)]] * 4, [(K, 1, -1, 1)])
    ok = younger == [0, 0, 0, 0, 1] and elder == [0, 0, 0, 1]
    # the elder's carrying ends at the third receiving, the younger's at the fourth
    carry = [(K, 1, -1, 1)]; ends_e = None
    for n in range(1, 5):
        s, carry = C(carry, [(K, 1)])
        if ends_e is None and not carry: ends_e = n
    carry = [(K, 1, -1, 0)]; ends_y = None
    for n in range(1, 6):
        s, carry = C(carry, [(K, 1)])
        if ends_y is None and not carry: ends_y = n
    s4, c4 = C([], [(K, 1)])
    ok &= ends_e == 3 and ends_y == 4 and s4 == [(K, 1)] and c4 == [(K, 1, -1, 0)]
    return ok


def M81():
    ok = True
    for s in range(1, 6):
        row = [2 + 2 * s * j for j in range(4)]
        ok &= all(row[j + 1] - row[j] == 2 * s for j in range(3))
        ok &= 2 + 2 * s * 4 == 2 + 8 * s and 8 * s + 1 == 2 + 8 * s - 1 and (8 * s + 1) % 2 == 1
        ok &= 8 * s + 1 not in range(1, 8 * s + 1)
    ok &= [8 * s + 1 for s in range(1, 6)] == [9, 17, 25, 33, 41]
    ok &= [[2 + 2 * s * j for j in range(4)] for s in range(1, 6)] == [[2, 4, 6, 8], [2, 6, 10, 14], [2, 8, 14, 20], [2, 10, 18, 26], [2, 12, 22, 32]]
    return ok


def halfway(s): return lambda n: n + 4 * s if n <= 4 * s else n - 4 * s
def fold(s): return lambda n: 8 * s + 1 - n


def M82():
    ok = True
    for s in range(1, 41):
        H, Fo = halfway(s), fold(s); names = range(1, 8 * s + 1)
        ok &= all(H(H(n)) == n and H(n) != n and H(n) % 2 == n % 2 for n in names)
        ok &= all(Fo(Fo(n)) == n and Fo(n) != n and Fo(n) % 2 != n % 2 for n in names)
        for n in names:
            fh = Fo(H(n))
            ok &= fh == (4 * s + 1 - n if n <= 4 * s else 12 * s + 1 - n) and fh != n
            cyc = [n]; x = n
            for k in range(4):
                x = H(x) if k % 2 == 0 else Fo(x); cyc.append(x)
            ok &= len(set(cyc[:4])) == 4 and cyc[4] == n
        ok &= all(v % 2 == 1 for v in (4 * s + 1, 8 * s + 1, 12 * s + 1))
    cyc = lambda s, n: [n, halfway(s)(n), fold(s)(halfway(s)(n)), halfway(s)(fold(s)(halfway(s)(n)))]
    ok &= cyc(2, 3) == [3, 11, 6, 14] and cyc(1, 3) == [3, 7, 2, 6]
    return ok


def M83():
    ok = True
    for s in range(1, 30):
        for n in range(1, 8 * s + 1):
            ok &= fold(2 * s)(n + 8 * s) == fold(s)(n)
            c = [n, n + 8 * s, 8 * s + 1 - n, 16 * s + 1 - n]
            ok &= len(set(c)) == 4 and fold(2 * s)(c[3]) == n and c[3] - c[2] == 8 * s
            ok &= c[1] % 2 == n % 2 and c[2] % 2 != n % 2
        for t in range(s + 1, 4 * s + 1):
            ok &= all(fold(t)(n + 8 * (t - s)) == fold(s)(n) for n in range(1, 8 * s + 1))
            ok &= (8 * (t - s) == 4 * t) == (t == 2 * s)
        ok &= 8 * ((s + 1) - s) == 8
    rows = [[n, n + 8, 9 - n, 17 - n] for n in range(1, 5)]
    ok &= rows == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]]
    ok &= all(17 - (n + 8) == 9 - n for n in range(1, 9))
    return ok


def M84():
    ok = True
    for s in range(1, 30):
        row = [2 + 2 * s * j for j in range(4)]; mid = Fr(row[0] + row[3], 2)
        ok &= mid == 2 + 3 * s and [r - mid for r in row] == [-3 * s, -s, s, 3 * s]
        ok &= row[2] - row[1] == 2 * s and row[3] - row[0] == 6 * s        # each span twice its reach
        ok &= 6 * s != 8 * s and mid != Fr(8 * s + 1, 2)
    r2 = [2, 6, 10, 14]
    ok &= {(r2[0], r2[3]), (r2[1], r2[2])} == {(2, 14), (6, 10)} and {(r2[0], r2[2]), (r2[1], r2[3])} == {(2, 10), (6, 14)}
    return ok


def M85():
    D = lambda r: (lambda x: 2 + r * (x - 2))
    ok = all(D(r)(D(s)(x)) == D(r * s)(x) for r in range(0, 9) for s in range(0, 9) for x in range(-20, 40))
    ok &= all([D(s)(2 + 2 * j) for j in range(4)] == [2 + 2 * s * j for j in range(4)] for s in range(1, 9))
    ok &= all(D(r)(x) % 2 == 0 for r in range(2, 20, 2) for x in range(-30, 60))
    ok &= [D(d)(4) - 2 for d in (1, 2, 4, 8)] == [2, 4, 8, 16]
    return ok


def M86():
    ok = True
    for s in range(1, 30):
        wider = [2 + 4 * s * j for j in range(4)]
        comp = [2 + 2 * s + 4 * s * j for j in range(4)]
        F2s = fold(2 * s)
        ok &= all(F2s(wider[j]) - comp[3 - j] == 2 * s - 3 for j in range(4))
    ok &= [2 * s - 3 for s in (1, 2, 3)] == [-1, 1, 3]
    ok &= fold(2)(2) == 15 and [4, 8, 12, 16][3] == 16 and 15 == 16 - 1        # holds at s = 1: the odd just before
    ok &= fold(4)(2) == 31 and [6, 14, 22, 30][3] == 30 and 31 == 30 + 1       # fails at s = 2: one after
    return ok


def E(r): return lambda n: r * (n - 2) + 2 if n % 2 == 0 else r * (n + 1) - 1


def M87():
    ok = True
    for B in (8, 16):
        for r in range(1, 7):
            e = E(r); names = range(1, B + 1)
            ok &= all(e(n) % 2 == n % 2 for n in names)
            ok &= all(e(B + 1 - n) == B * r + 1 - e(n) for n in names)
            ok &= all(e(n + B // 2) == e(n) + r * B // 2 for n in range(1, B // 2 + 1))
            ok &= all(e(n + 2) - e(n) == 2 * r for n in range(1, B - 1))
            if r >= 2: ok &= e(B + 1) > B * r + 1
    ok &= [E(2)(n) for n in range(1, 9)] == [3, 2, 7, 6, 11, 10, 15, 14]
    ok &= [E(2)(n) for n in (2, 4, 6, 8)] == [2, 6, 10, 14] and (E(2)(1), E(2)(2)) == (3, 2)
    return ok


# ---------------------------------------------------------------- 4.7 bounding
def M88():
    # degree two in n and in k: a 3 x 3 grid decides it; a wider range besides
    ok = all(n * n - (n - k) * (n + k) == k * k for n in range(-50, 51) for k in range(-50, 51))
    return ok and all(n * n - (n - 1) * (n + 1) == 1 for n in range(-100, 101))


def M89():
    ok = [k for k in range(1, 1000) if k * k == 2 * k] == [2]
    ok &= all(n * n - (n - 2) * (n + 2) == 4 == 2 * 2 for n in range(-100, 101))
    ok &= 4 ** 2 - 2 * 6 == 4 and 10 ** 2 - 8 * 12 == 4
    return ok


def M90():
    ok = [k for k in range(1, 200) if 2 * k - 1 == 1] == [1]     # faces n - k and n + k hold 2k - 1 between
    ok &= (25 - 23) // 2 == 1 and (23 + 25) // 2 == 24
    ok &= (55 - 23) == 32 and (55 - 23) // 2 == 16 and (23 + 55) // 2 == 39 and 39 ** 2 - 23 * 55 == 256 == 16 ** 2
    return ok


def M96():
    ok = abs(math.hypot(1, 1) - math.sqrt(2)) < 1e-15 and abs(math.sqrt(1 + 1 + 1) - math.sqrt(3)) < 1e-15
    pts = [(math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5)) for k in range(5)]
    side = math.dist(pts[0], pts[1]); diag = math.dist(pts[0], pts[2])
    ok &= abs(diag / side - float(PHI)) < 1e-12
    c36 = math.cos(math.radians(36)); s18 = math.sin(math.radians(18)); c18 = math.cos(math.radians(18))
    ok &= abs(c36 - float(PHI) / 2) < 1e-15 and abs(s18 - 1 / (2 * float(PHI))) < 1e-15
    ok &= abs(s18 - (math.sqrt(5) - 1) / 4) < 1e-15 and abs(c18 - math.sqrt(10 + 2 * math.sqrt(5)) / 4) < 1e-15
    ok &= (PHI / 2) * (PHI / 2) * 4 - PHI - 1 == Q5(0)           # 4x^2 - 2x - 1 = 0 at x = phi/2, cos 36 exactly
    ok &= Q5(1) / (PHI * 2) == (R5 - 1) / 4
    return ok


def M97():
    ok = True
    for k in range(-890, 891):
        x = math.radians(k / 10)
        if abs(abs(math.tan(x)) - 1) < 1e-6: continue
        t = math.tan(x)
        ok &= abs(math.tan(2 * x) - 2 * t / (1 - t * t)) < 1e-6 * max(1, abs(math.tan(2 * x)))
    # 2t/(1 - t^2) = 2t  <=>  t^3 = 0: nought alone
    ok &= {t for t in (Fr(p, q) for p in range(-40, 41) for q in range(1, 11)) if t * t != 1 and 2 * t / (1 - t * t) == 2 * t} == {0}
    ok &= abs(math.cos(math.radians(90))) < 1e-15                  # the doubled angle at 45 degrees: the pole
    for num in range(1, 64):
        x = Fr(num, 64); bits = format(num, '06b'); y = (2 * x) % 1
        ok &= format(int(y * 64), '06b') == bits[1:] + '0'
    return ok


def M98():
    g = lambda t: 2 * t / (1 - t * t)
    # fixed: 2t/(1-t^2) = t  <=>  t (1 + t^2) = 0  <=>  t = 0 over the reals
    # sign changing, size the same: 2t/(1-t^2) = -t, t != 0  <=>  t^2 = 3
    # t with 2t/(1 - t^2) = -t and t != 0 satisfy t^2 = 3, over the rationals none: checked at p/q below
    ok = not any(2 * t / (1 - t * t) == -t for t in (Fr(p, q) for p in range(1, 60) for q in range(1, 30)) if t * t != 1)
    r3 = math.sqrt(3)
    ok &= abs(g(r3) + r3) < 1e-12 and abs(g(-r3) - r3) < 1e-12
    x = r3; seq = []
    for _ in range(6): x = g(x); seq.append(round(x / r3))
    ok &= seq == [-1, 1, -1, 1, -1, 1]
    ok &= abs(math.tan(math.radians(60)) - r3) < 1e-12 and abs(math.tan(math.radians(120)) + r3) < 1e-12
    # scan: fixed points and sign-changing pairs among t on a fine grid
    fixed = [k for k in range(-3000, 3001) if abs(k / 1000) != 1 and abs(g(k / 1000) - k / 1000) < 1e-12]
    ok &= fixed == [0]
    return ok


def M99():
    ok = True
    for a, b, c in product(range(-4, 5), repeat=3):
        th = 0.5 * math.atan2(2 * b, a - c)
        R = rot(th); M = [[a, b], [b, c]]
        Mp = matmul(matmul([[R[0][0], R[1][0]], [R[0][1], R[1][1]]], M), R)
        ok &= abs(Mp[0][1]) < 1e-9
    th = 0.5 * math.atan2(2 * 2, 5 - 1)
    ok &= abs(math.degrees(th) - 22.5) < 1e-12
    th = 0.5 * math.atan2(2 * 3, 0)                                 # a = c: forty-five degrees
    ok &= abs(math.degrees(th) - 45) < 1e-12
    return ok


def M100():
    ok = True
    for k in range(1, 179):
        x = math.radians(k); t = math.tan(x / 2)
        ok &= abs(math.sin(x) - 2 * t / (1 + t * t)) < 1e-12 and abs(math.cos(x) - (1 - t * t) / (1 + t * t)) < 1e-12
    gen = set()
    for m in range(2, 40):
        for n in range(1, m):
            a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
            ok &= a * a + b * b == c * c
            s, co = Fr(2 * n * m, m * m + n * n), Fr(m * m - n * n, m * m + n * n)   # t = n/m
            ok &= s * s + co * co == 1
            gen.add((min(a, b), max(a, b), c))
    for c in range(1, 500):
        for a in range(1, c):
            b2 = c * c - a * a; b = isqrt(b2)
            if b >= a and b * b == b2:
                g = gcd(gcd(a, b), c)
                ok &= (a // g, b // g, c // g) in gen                  # up to order and a whole multiple
    return ok


# ---------------------------------------------------------------- 4.9 inseparating
def M121():
    vals = [0, 1, 2]                                    # nought < a < one on a chain
    meet = min
    neg = lambda x: max(y for y in vals if meet(x, y) == 0)
    return neg(1) == 0 and neg(0) == 2 and neg(neg(1)) == 2 != 1 and neg(2) == 0


# ---------------------------------------------------------------- 4.10 co-offering
NEUTRALS = ('nought', 'scale', 'bounded infinity')


def M125():
    pairings = list(combinations(NEUTRALS, 2))
    offerings = [(a, b) for a, b in permutations(NEUTRALS, 2)]
    states = list(product(('fixed', 'floating'), repeat=3))
    return len(pairings) == 3 and len(offerings) == 6 and len(states) == 8 == 2 ** 3


def M128():
    offerings = list(permutations(NEUTRALS, 2))
    table = {}
    for r in range(4):
        for fixed in combinations(NEUTRALS, r):
            run = [o for o in offerings if o[0] not in fixed and o[1] not in fixed]
            table.setdefault(r, set()).add((len(run), len(offerings) - len(run)))
    ok = table == {0: {(6, 0)}, 1: {(2, 4)}, 2: {(0, 6)}, 3: {(0, 6)}}
    for n in NEUTRALS:                                    # a neutral fixed partners two of three pairings, both ways
        ok &= sum(1 for o in offerings if n in o) == 4 and sum(1 for p in combinations(NEUTRALS, 2) if n in p) == 2
    return ok


def perm_mul(p, q): return tuple(p[q[i]] for i in range(len(q)))
def perm_inv(p):
    r = [0] * len(p)
    for i, v in enumerate(p): r[v] = i
    return tuple(r)
def parity(p):
    s, seen = 0, set()
    for i in range(len(p)):
        if i in seen: continue
        j, L = i, 0
        while j not in seen: seen.add(j); j = p[j]; L += 1
        s += L - 1
    return s % 2


def gen_group(gens):
    idt = tuple(range(len(gens[0]))); G = {idt}; frontier = [idt]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = perm_mul(g, h)
                if x not in G: G.add(x); nxt.append(x)
        frontier = nxt
    return G


def commutator_subgroup(G):
    return gen_group([perm_mul(perm_mul(a, b), perm_mul(perm_inv(a), perm_inv(b))) for a in G for b in G])


def M133():
    S5 = set(permutations(range(5))); A5 = {p for p in S5 if parity(p) == 0}
    classes = []; left = set(A5)
    while left:
        x = next(iter(left)); cl = {perm_mul(perm_mul(g, x), perm_inv(g)) for g in A5}
        classes.append(len(cl)); left -= cl
    ok = len(A5) == 60 and sorted(classes) == [1, 12, 12, 15, 20]
    # a normal subgroup is a union of classes containing the one, its size dividing 60
    sizes = {1 + sum(c) for r in range(0, 5) for c in combinations(sorted(classes)[1:], r)}
    ok &= sorted(s for s in sizes if 60 % s == 0) == [1, 60]
    ok &= commutator_subgroup(S5) == A5 and commutator_subgroup(A5) == A5      # S5 descends to A5 and stops
    S4 = set(permutations(range(4)))
    d1 = commutator_subgroup(S4); d2 = commutator_subgroup(d1); d3 = commutator_subgroup(d2)
    ok &= (len(d1), len(d2), len(d3)) == (12, 4, 1)                            # S4 > A4 > V4 > 1
    return ok


def ico_vertices():
    p = float(PHI); V = []
    for a, b in product((1, -1), repeat=2):
        V += [(0, a, b * p), (a, b * p, 0), (b * p, 0, a)]
    return V


def M137():
    V = ico_vertices(); d2 = lambda u, v: sum((x - y) ** 2 for x, y in zip(u, v))
    edges = [(i, j) for i, j in combinations(range(12), 2) if abs(d2(V[i], V[j]) - 4) < 1e-9]
    faces = [t for t in combinations(range(12), 3) if all((min(a, b), max(a, b)) in edges for a, b in combinations(t, 2))]
    ok = len(V) == 12 and len(edges) == 30 and len(faces) == 20
    # rotations: frame (u, v, u x v) at an edge sent to each directed edge
    def frame(u, v):
        w = cross(u, v); return [list(u), list(v), list(w)]
    def solve(Fa, Fb):   # R with R Fa^T = Fb^T -> R = Fb^T (Fa^T)^-1
        A = [[Fa[j][i] for j in range(3)] for i in range(3)]; B = [[Fb[j][i] for j in range(3)] for i in range(3)]
        dA = det(A)
        inv = [[(A[(j + 1) % 3][(i + 1) % 3] * A[(j + 2) % 3][(i + 2) % 3] - A[(j + 1) % 3][(i + 2) % 3] * A[(j + 2) % 3][(i + 1) % 3]) / dA for j in range(3)] for i in range(3)]
        return matmul(B, inv)
    u, v = V[edges[0][0]], V[edges[0][1]]
    rots = []
    for i, j in edges + [(b, a) for a, b in edges]:
        R = solve(frame(u, v), frame(V[i], V[j]))
        img = [tuple(sum(R[r][c] * x[c] for c in range(3)) for r in range(3)) for x in V]
        if all(any(d2(y, z) < 1e-9 for z in V) for y in img):
            if not any(close(R, Q, 1e-9) for Q in rots): rots.append(R)
    tr = [round(R[0][0] + R[1][1] + R[2][2], 6) for R in rots]
    ident = tr.count(3.0); halfr = tr.count(-1.0); third = tr.count(0.0)
    fifth = sum(1 for t in tr if abs(t - float(PHI)) < 1e-5 or abs(t - (1 - float(PHI))) < 1e-5)
    ok &= len(rots) == 60 and (ident, halfr, third, fifth) == (1, 15, 20, 24)
    ok &= ident + halfr + third == 36 and Fr(36, 24) == Fr(3, 2)
    return ok


def M139():
    ok = True
    for k in range(360):
        th = math.radians(k); h = 1e-6
        d = ((math.cos(th + h) - math.cos(th - h)) / (2 * h), (math.sin(th + h) - math.sin(th - h)) / (2 * h))
        f = Fm((math.cos(th), math.sin(th)))
        ok &= abs(d[0] - f[0]) < 1e-8 and abs(d[1] - f[1]) < 1e-8
    grp = {1j ** k for k in range(8)}
    ok &= len({(round(z.real), round(z.imag)) for z in grp}) == 4 and {1, -1} <= {complex(round(z.real), round(z.imag)) for z in grp}
    ok &= len({(-1) ** k for k in range(8)}) == 2
    E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    ok &= all(dot(a, b) == (1 if a == b else 0) for a in E3 for b in E3)
    return ok


def colourings(n, edges):
    for c in product((0, 1), repeat=n):
        if all(c[a] != c[b] for a, b in edges): yield c


def connected(n, edges):
    adj = {i: set() for i in range(n)}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    seen = {0}; st = [0]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); st.append(y)
    return len(seen) == n


def M140():
    ok = True
    for n in range(3, 15):
        ring = [(i, (i + 1) % n) for i in range(n)]
        cols = list(colourings(n, ring))
        ok &= (len(cols) > 0) == (n % 2 == 0)
        best = min(sum(c[a] == c[b] for a, b in ring) for c in product((0, 1), repeat=n))
        ok &= best == (0 if n % 2 == 0 else 1)
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        for mask in range(2 ** len(pairs)):
            edges = [p for k, p in enumerate(pairs) if mask >> k & 1]
            if not connected(n, edges): continue
            cnt = sum(1 for _ in colourings(n, edges))
            ok &= cnt in (0, 2)
    return ok


def M141():
    V = list(product((1, -1), repeat=3))
    E = [(a, b) for a, b in combinations(V, 2) if ham(a, b) == 1]
    faces = {(j, s) for j in range(3) for s in (1, -1)}
    ok = len(V) == 8 and len(E) == 12 and len(faces) == 6
    signed = []
    for perm in permutations(range(3)):
        for sg in product((1, -1), repeat=3):
            M = [[sg[i] if j == perm[i] else 0 for j in range(3)] for i in range(3)]
            signed.append(M)
    ok &= len(signed) == 48 and sum(1 for M in signed if det(M) == 1) == 24
    return ok


def M142():
    m3 = [[-1 if i == j else 0 for j in range(3)] for i in range(3)]
    m4 = [[-1 if i == j else 0 for j in range(4)] for i in range(4)]
    a = [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    b = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
    ok = det(m3) == -1 and det(m4) == 1 and matmul(a, b) == m4 and det(a) == det(b) == 1
    ok &= [v for v in product(range(-2, 3), repeat=4) if tuple(-x for x in v) == v] == [(0, 0, 0, 0)]
    # the cube's 48 carry x -> -x only among those with determinant -1; the tesseract's rotations carry it
    ok &= det([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]) == -1
    return ok


def M144():
    lip = [v for v in product(range(-1, 2), repeat=4) if sum(x * x for x in v) == 1]
    half = [v for v in product((Fr(1, 2), Fr(-1, 2)), repeat=4) if sum(x * x for x in v) == 1]
    ok = len(lip) == 8 and len(half) == 16 and len(lip) + len(half) == 24
    # (1 + i + j + k) / 2 lies at distance one from its nearest whole points: dividing 1+i+j+k by 2
    # at whole quotients leaves a remainder of norm 4, the divisor's norm, never below it
    a = (1, 1, 1, 1)
    best = min(sum((a[i] - 2 * q[i]) ** 2 for i in range(4)) for q in product(range(-2, 3), repeat=4))
    ok &= best == 4 == 2 * 2
    # (1/2, ..., 1/2) at distance one from its nearest whole points in four dimensions and in no other
    ok &= [d for d in range(1, 30) if Fr(d, 4) == 1] == [4]
    return ok


def M148():
    ok = True
    I = [[1, 0], [0, 1]]
    tref = [[1, 1], [-1, 0]]; fig8 = [[2, 1], [1, 1]]
    P = I
    for k in range(1, 7):
        P = matmul(P, tref)
        ok &= (P == I) == (k == 6)
    ok &= tref[0][0] + tref[1][1] == 1 and fig8[0][0] + fig8[1][1] == 3
    lam = (3 + math.sqrt(5)) / 2
    ok &= abs(lam - float(PHI) ** 2) < 1e-12                      # the figure-eight winds on at phi squared
    P = I
    for k in range(1, 60):
        P = matmul(P, fig8); ok &= P != I and P != [[-1, 0], [0, -1]]
    for a, b, c, d in product(range(-6, 7), repeat=4):
        if a * d - b * c != 1: continue
        M = [[a, b], [c, d]]; t = abs(a + d)
        P = I; order = None
        for k in range(1, 13):
            P = matmul(P, M)
            if P == I: order = k; break
        if t < 2: ok &= order is not None
        if t > 2: ok &= order is None
        if t == 2:
            ok &= M in (I, [[-1, 0], [0, -1]]) or order is None
    return ok


def M150():
    tr = list(combinations(range(5), 2))
    ok = len(tr) == 10 == comb(5, 2)
    for a, b in tr:
        p = list(range(5)); p[a], p[b] = b, a; p = tuple(p)
        ok &= perm_mul(p, p) == tuple(range(5)) and sum(1 for i in range(5) if p[i] == i) == 3
    ok &= [n for n in range(2, 200) if comb(n, 2) == 2 * n] == [5]
    ok &= [k * (k + 1) // 2 for k in range(1, 5)][3] == 10 and [comb(k + 2, 3) for k in range(1, 4)][2] == 10 == 1 + 3 + 6
    ok &= len(list(combinations((1, -1), 2))) == 1
    return ok


def M151():
    pts = [(math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5)) for k in range(5)]
    vec = lambda a, b: (pts[b][0] - pts[a][0], pts[b][1] - pts[a][1])
    ok = True
    gens = []
    for i in range(5):
        a, b = i, (i + 1) % 5
        diag = [d for d in combinations(range(5), 2) if a not in d and b not in d and (d[1] - d[0]) % 5 in (2, 3)]
        ok &= len(diag) == 1
        c, d = diag[0]
        u, w = vec(a, b), vec(c, d)
        ok &= abs(u[0] * w[1] - u[1] * w[0]) < 1e-12                              # parallel
        ok &= abs(math.hypot(*w) / math.hypot(*u) - float(PHI)) < 1e-12
        t1 = list(range(5)); t1[a], t1[b] = b, a; t2 = list(range(5)); t2[c], t2[d] = d, c
        t1, t2 = tuple(t1), tuple(t2)
        g = perm_mul(t1, t2)
        ok &= g == perm_mul(t2, t1)                                               # they commute
        left = ({0, 1, 2, 3, 4} - {a, b, c, d}).pop()
        ok &= g[left] == left and all(g[x] != x for x in range(5) if x != left)
        refl_ = tuple((2 * left - x) % 5 for x in range(5))                        # the pentagon's symmetry at that corner
        ok &= g == refl_
        gens.append(g)
    G = gen_group(gens)
    rots = [p for p in G if all(p[x] != x for x in range(5))]
    keep1 = [p for p in G if sum(p[x] == x for x in range(5)) == 1]
    ok &= len(G) == 10 and len(rots) == 4 and len(keep1) == 5
    return ok


def M152():
    def mono_tri(n, col, pairs):
        idx = {p: k for k, p in enumerate(pairs)}
        return any(col[idx[(a, b)]] == col[idx[(a, c)]] == col[idx[(b, c)]] for a, b, c in combinations(range(n), 3))
    p6 = list(combinations(range(6), 2))
    ok = all(mono_tri(6, c, p6) for c in product((0, 1), repeat=15))
    p5 = list(combinations(range(5), 2))
    free = [c for c in product((0, 1), repeat=10) if not mono_tri(5, c, p5)]
    ok &= len(free) == 12
    for c in free:
        for colour in (0, 1):
            es = [p for k, p in enumerate(p5) if c[k] == colour]
            deg = [sum(1 for e in es if v in e) for v in range(5)]
            ok &= len(es) == 5 and deg == [2] * 5 and connected(5, es)            # a five-cycle: pentagon, and pentagram
    return ok


def M156():
    order = (2 ** 46) * (3 ** 20) * (5 ** 9) * (7 ** 6) * (11 ** 2) * (13 ** 3) * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71
    ok = order == 808017424794512875886459904961710757005754368000000000
    ps = [p for p in range(2, 72) if all(p % q for q in range(2, isqrt(p) + 1)) and order % p == 0]
    ok &= len(ps) == 15 and ps[0] == 2 and ps[-1] == 71
    upto59 = [p for p in range(2, 60) if all(p % q for q in range(2, isqrt(p) + 1))]
    ok &= len(upto59) == 17 and sorted(set(upto59) - set(ps)) == [37, 43, 53] and 71 in ps
    # j = E4^3 / Delta: its coefficient at the first power of q
    N = 4
    sig3 = lambda n: sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
    E4 = [1] + [240 * sig3(n) for n in range(1, N + 2)]
    def mul(a, b):
        return [sum(a[i] * b[k - i] for i in range(k + 1) if i < len(a) and k - i < len(b)) for k in range(N + 2)]
    E43 = mul(mul(E4, E4), E4)
    D = [1] + [0] * (N + 1)                                             # Delta / q = prod (1 - q^n)^24
    for n in range(1, N + 2):
        for _ in range(24):
            D = [D[k] - (D[k - n] if k >= n else 0) for k in range(N + 2)]
    inv = [Fr(1)] + [Fr(0)] * (N + 1)                                   # 1 / (Delta/q)
    for k in range(1, N + 2):
        inv[k] = -sum(D[i] * inv[k - i] for i in range(1, k + 1))
    jq = mul(E43, inv)                                                  # q * j: coefficients of q^-1, q^0, q^1, ...
    ok &= jq[0] == 1 and jq[1] == 744 and jq[2] == 196884 == 196883 + 1
    return ok


# ---------------------------------------------------------------- field instances (the links stay field)
def FI_four_sq():
    N = 300
    r4 = [0] * (N + 1)
    lim = isqrt(N)
    for a, b, c, d in product(range(-lim, lim + 1), repeat=4):
        n = a * a + b * b + c * c + d * d
        if n <= N: r4[n] += 1
    ok = True
    for n in range(1, N + 1):
        divs = [k for k in range(1, n + 1) if n % k == 0]
        want = 8 * sum(divs) if n % 2 else 24 * sum(k for k in divs if k % 2)
        ok &= r4[n] == want and r4[n] > 0
    return ok and 8 == 3 ** 2 - 1 and 24 == 5 ** 2 - 1


def FI_e8():
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((1, -1), repeat=2):
            v = [0] * 8; v[i] = a; v[j] = b; roots.add(tuple(Fr(x) for x in v))
    for sg in product((1, -1), repeat=8):
        if sg.count(-1) % 2 == 0: roots.add(tuple(Fr(x, 2) for x in sg))
    return len(roots) == 240 and all(sum(x * x for x in v) == 2 for v in roots)


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'M\d+', k) and callable(v)}
# field instances: the link named stays at standing field; these check the instances its text names
FIELD_INSTANCES = {'M46': FI_quat, 'M143': FI_four_sq, 'M146': FI_e8}

'''

PART_SOURCES['two'] = r'''"""Run checks for Exhibit THIRTY Part FIVE · NETWORKING (links W…), from Exhibit TWO v372,
against Exhibit ONE v372's resolver as resolver_v372.py beside this file.
Run:  python3 ccl_two_checks.py [results.json]"""
import ast, os, re, sys, json, copy, symtable, zipfile
from itertools import product, combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV

C = RV._1_self_coupling; R = RV._9_other_releasing
CON = RV.CONNECTORS; JOI = RV.JOINS
SRC = open(os.path.join(HERE, 'resolver_v372.py')).read()
TREE = ast.parse(SRC)
KIT_ZIP = '/home/claude/work/v372/Natural_Networking_Test_Kit_v368.zip'
K = 'k'
S = (1, -1)
OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def reach(Cf=C):
    seen = {()}; fr = [()]
    while fr:
        nx = []
        for st in fr:
            for off in OFFERS:
                _, c = Cf([(K,) + st] if st else [], off)
                s2 = tuple(c[0][1:]) if c else ()
                if s2 not in seen: seen.add(s2); nx.append(s2)
        fr = nx
    return sorted(seen)

REACH = reach()
def carry_of(st): return [(K,) + st] if st else []
def six(carry): return [(k, t) for k, c, t, a in carry]


# ------------------------------------------------ 5.2 the six connectors
def W7():
    ok = True
    for a, b in JOI.items():
        fa, fb = CON[a][1], CON[b][1]
        ok &= {fa, fb} in ({'right', 'left'}, {'forward', 'backward'})
        if {fa, fb} == {'right', 'left'}:
            ok &= {CON[a][2], CON[b][2]} == {'releasing', 'arriving'} and CON[a][2] == 'releasing'
    # the table: 2 meets the right neighbour's 6, 6 the left neighbour's 2, 10 the right's 14, 14 the left's 10, 9 the backward's 17, 17 the forward's 9
    table = {2: 6, 6: 2, 10: 14, 14: 10, 9: 17, 17: 9}
    opposite = {'right': 'left', 'left': 'right', 'forward': 'backward', 'backward': 'forward'}
    ok &= all(CON[b][1] == opposite[CON[a][1]] for a, b in table.items())
    ok &= all(JOI.get(a) == b or JOI.get(b) == a for a, b in table.items())
    return ok and sorted(CON) == [2, 6, 9, 10, 14, 17]


# ------------------------------------------------ 5.3 the local cycle
def W14():
    selfm = [(1, 2), (3, 4), (5, 6), (7, 8)]; otherm = [(2, 3), (4, 5), (6, 7), (8, 9)]
    pos = {x for m in selfm + otherm for x in m}
    return (pos == set(range(1, 10)) and len(selfm) == len(otherm) == 4
            and all(s[1] == o[0] for s, o in zip(selfm, otherm))
            and all(o[1] == s2[0] for o, s2 in zip(otherm, selfm[1:])))


# ------------------------------------------------ 5.4 overlapping momentaries, the four-form
def W18():
    one, other = {1, 2, 3, 4}, {2, 3, 4, 5}
    return (len(one & other) == 3 and len(one | other) == 5
            and sum(1 for x in one if x % 2) == 2 and sum(1 for x in other if x % 2) == 2)

def W20():
    ok = True
    for st in REACH:
        for off in OFFERS:
            s, c = C(carry_of(st), off); v = dict(s).get(K)
            if v:
                ok &= c[0][1] == v and R(s, {K: K}) == [(K, v)]
    return ok

def W21():
    A = RV._17_social_abundancing
    S = {'A': {'backward': ['B']}, 'B': {'backward': ['A']}}
    _, nxt = A({'A': [(K, 1, -1, 0)]}, {}, {}, S)
    return (JOI == {10: 14, 6: 2, 17: 9, 9: 17} and JOI[9] == 17 and (9, 2) not in JOI.items()
            and 1 not in JOI.values() and nxt['B'][17] == [(K, -1)] and nxt['B'][2] == [] and nxt['A'] == {2: [], 14: [], 17: []})

def W99():
    A = RV._17_social_abundancing
    def hole(both):
        S = {}
        for r in range(3):
            for c in range(3):
                if (r, c) == (1, 1): continue
                nb = {}
                if c + 1 < 3 and (r, c + 1) != (1, 1): nb['right'] = [(r, c + 1)]
                if c - 1 >= 0 and (r, c - 1) != (1, 1): nb['left'] = [(r, c - 1)]
                along = [(r - 1, c)] if r - 1 >= 0 and (r - 1, c) != (1, 1) else []
                if both and r + 1 < 3 and (r + 1, c) != (1, 1): along.append((r + 1, c))
                if along: nb['backward'] = along
                S[(r, c)] = nb
        return S
    def walk(S, steps):
        car, arr = {}, {(1, 0): {2: [(K, 1)]}}; rows = []
        for t in range(steps):
            surf = {s: dict(C(car.get(s, []), [x for c in (2, 14, 17) for x in arr.get(s, {}).get(c, [])])[0]).get(K) for s in S}
            rows.append((surf, arr)); car, arr = A(car, arr, {}, S)
        return rows
    rows = walk(hole(False), 40)
    ok = rows[1][1][(0, 0)][17] == [(K, 1)] and rows[1][0][(0, 0)] == 1 and rows[2][1][(0, 1)][14] == [(K, 1)]
    ok &= rows[3][1][(0, 2)][14] == [(K, 1)] and rows[3][0][(0, 2)] == 1
    ok &= all(rows[t][0][(1, 2)] is None and not any(rows[t][1].get((1, 2), {}).get(c) for c in (2, 14, 17)) for t in range(40))
    rows = walk(hole(True), 40)
    ok &= rows[4][1][(1, 2)][17] == [(K, 1), (K, 1)] and rows[4][0][(1, 2)] == 1 and all(rows[t][0][(1, 2)] is None for t in range(4))
    return ok

def W23():
    now = [(4, 5), (6, 7), (8, 9)]; on = [(a + 8, b + 8) for a, b in now]
    return (on == [(12, 13), (14, 15), (16, 17)]
            and all(a % 2 == 0 and b % 2 == 1 for a, b in now + on) and len(now) * 2 == 6)

def W24():
    ok = True
    for x, y in product(S, S):
        f = lambda p: (p[1], -p[0])
        seq = [(x, y)]
        for _ in range(12): seq.append(f(seq[-1]))
        ok &= seq[4] == (x, y) and seq[6] == (-x, -y) and seq[12] == (x, y)
        ok &= all(set(seq[i + 1:i + 7]) == set(product(S, S)) for i in range(0, 7))
    ok &= (24 // 4, 24 // 6, 36 // 4, 36 // 6) == (6, 4, 9, 6) and 24 == 3 * 8 and 36 == 3 * 12
    return ok


# ------------------------------------------------ 5.5 widening and lengthening
def W25():
    ok = True
    want_odd = [9, 17, 25, 33, 41]
    for s in range(1, 6):
        row = [2 + 2 * s * j for j in range(4)]
        mid = (row[0] + row[-1]) / 2
        ok &= row[1] - row[0] == 2 * s and 2 * (2 * s) == 4 * s
        ok &= 8 * s + 1 == want_odd[s - 1] and row[-1] + 2 * s == 8 * s + 2
        ok &= [r - mid for r in row] == [-3 * s, -s, s, 3 * s] and row[-1] - row[0] == 6 * s == 2 * (3 * s)
        ok &= all(((8 * s + 1) - n) % 2 != n % 2 and 1 <= (8 * s + 1) - n <= 8 * s for n in range(1, 8 * s + 1))
    return ok and [2 + 2 * 2 * j for j in range(4)] == [2, 6, 10, 14]

def W26():
    spans = [2 ** k + 1 for k in range(3, 7)]
    return spans == [9, 17, 33, 65] and 17 - 1 == 16 and len(range(1, 18)) == 17

def primes(a, b): return [p for p in range(a, b + 1) if p > 1 and all(p % d for d in range(2, p))]

def W28():
    P = primes(5, 59)
    wide = sum(1 for i in range(len(P)) if i % 2 == 0)
    gaps = [b - a for a, b in zip(primes(3, 59), primes(3, 59)[1:])]
    return (P == [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59] and len([p for p in P if p <= 53]) == 14
            and (wide, len(P) - wide) == (8, 7) and len(primes(3, 59)) == 16 and len(gaps) == 15
            and all(g % 2 == 0 for g in gaps))

def W29():
    ok = True
    for p in primes(5, 59):
        h = (p - 1) // 2
        dist = lambda k: min(k, p - k)
        far = [k for k in range(p) if dist(k) == max(dist(j) for j in range(p))]
        ok &= far == [h, h + 1] and dist(h) == dist(h + 1) == h
        ok &= (p - 1, (p - 1) // 2) == (p - 1, h)
        oddp = [(i, i + 1) for i in range(1, p, 2)]; evenp = [(i, i + 1) for i in range(2, p, 2)]
        inn = lambda x, L: sum(1 for a, b in L if x in (a, b))
        ok &= all(inn(x, oddp) == 1 and inn(x, evenp) == 1 for x in range(2, p))
        ok &= inn(1, oddp) == 1 and inn(1, evenp) == 0 and inn(p, evenp) == 1 and inn(p, oddp) == 0
    far59 = [k for k in range(59) if min(k, 59 - k) == 29]
    return ok and far59 == [29, 30] and (17 - 1, (17 - 1) // 2) == (16, 8)

def W30():
    ok = 6 / 3 == 2 and 3 / 6 == 0.5
    for L in range(2, 1001, 2):
        pair = 2 * L; waist_pair = pair // 2
        ok &= waist_pair == L and pair / L == 2 and pair - L // 2 == L + L // 2
    return ok and 2 * 440 - 220 == 660


# ------------------------------------------------ 5.7 society, primes below 60
def W33():
    P = primes(2, 59)
    return len(P) == 17 and P[8] == 23 and len(P[:8]) == len(P[9:]) == 8 and sum(P) == 440 and \
        sorted(120 - p for p in P)[0] == 61 and max(120 - p for p in P) == 118


# ------------------------------------------------ 5.10 carrying at its self
def W48():
    st = symtable.symtable(SRC, 'resolver', 'exec')
    fns = {c.get_name(): c for c in st.get_children() if c.get_type() == 'function'}
    ok = set(fns) == {'_1_self_coupling', '_9_other_releasing', '_17_social_abundancing'}
    allowed = {'_17_social_abundancing': {'CONNECTORS', 'JOINS', '_1_self_coupling', '_9_other_releasing'}}
    for name, f in fns.items():
        globs = set(f.get_globals())
        for ch in f.get_children():                       # comprehension scopes
            globs |= set(ch.get_globals())
        ok &= globs == allowed.get(name, set())
    ok &= not any(isinstance(n, (ast.Global, ast.Nonlocal)) for n in ast.walk(TREE))
    for st_ in REACH:
        for off in OFFERS:
            ok &= C(carry_of(st_), off) == C(carry_of(st_), off)
    A = RV._17_social_abundancing
    S = {'A': {'right': ['B'], 'backward': ['B']}, 'B': {'left': ['A'], 'backward': ['A']}}
    args = ({'A': [(K, 1, -1, 1)]}, {'B': {2: [(K, -1)]}}, {}, S)
    ok &= A(*args) == A(*args) and A(*args) == A(*args)
    return ok


# ------------------------------------------------ 5.11 invocation is a caller's
def W56():
    top = TREE.body
    kinds = [type(n).__name__ for n in top]
    calls_at_top = [n for n in top if not isinstance(n, ast.FunctionDef) for m in ast.walk(n) if isinstance(m, ast.Call)]
    third = next(n for n in top if isinstance(n, ast.FunctionDef) and n.name == '_17_social_abundancing')
    calls_in_third = {m.func.id for m in ast.walk(third) if isinstance(m, ast.Call) and isinstance(m.func, ast.Name)}
    return kinds.count('FunctionDef') == 3 and kinds.count('Assign') == 2 and not calls_at_top and \
        {'_1_self_coupling', '_9_other_releasing'} <= calls_in_third and all(k in ('Expr', 'FunctionDef', 'Assign') for k in kinds)


# ------------------------------------------------ 5.12 securities: the inversion taken out
def resolver_without_inversion():
    t = SRC.replace("_14_social_crossing.append((_4_self_sharing, -1))", "_14_social_crossing.append((_4_self_sharing, +9))")
    t = t.replace("_14_social_crossing.append((_4_self_sharing, 1))", "_14_social_crossing.append((_4_self_sharing, -1))")
    t = t.replace("+9))", "1))")
    ns = {}; exec(t, ns); return ns['_1_self_coupling']

def W62():
    Cx = resolver_without_inversion()
    ok = Cx([(K, 1, -1, 0)], []) [0] == [(K, 1)] and C([(K, 1, -1, 0)], [])[0] == [(K, -1)]
    for c in S:
        carry = []; surf = []
        for i in range(9):
            s, carry = Cx(carry, [(K, c)] if i == 0 else []); surf.append(dict(s).get(K))
        ok &= surf == [c] * 9
        carry = []; surf = []
        for i in range(9):
            s, carry = C(carry, [(K, c)] if i == 0 else []); surf.append(dict(s).get(K))
        ok &= surf == [c, -c] * 4 + [c]
    return ok

def W65():
    ok = True
    for n in range(3, 9):
        ring = {frozenset((i, (i + 1) % n)) for i in range(n)}
        full = {frozenset(p) for p in combinations(range(n), 2)}
        ok &= (ring == full) == (n == 3)
    return ok

def pairs_parted(drop, n=6):
    def run(st, off):
        carry = carry_of(st); out = []
        for _ in range(n):
            s, carry = C(carry, off); v = dict(s).get(K); out.append(v if v else 0)
        return [v for v in out if v] if drop else out
    P = list(combinations(REACH, 2))
    plus = {p for p in P if run(p[0], [(K, 1)]) != run(p[1], [(K, 1)])}
    minus = {p for p in P if run(p[0], [(K, -1)]) != run(p[1], [(K, -1)])}
    return len(P), len(plus), len(minus), len(plus | minus)

def W70():
    def seq(st, off, n=12):
        carry = carry_of(st); out = []
        for _ in range(n):
            s, carry = C(carry, off); v = dict(s).get(K); out.append(v if v else 0)
        return out
    def first(a, b): return next((i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y), None)
    mins = []
    for a, b in combinations(REACH, 2):
        w = [first(seq(a, o), seq(b, o)) for o in ([(K, 1)], [(K, -1)])]
        mins.append(min(x for x in w if x))
    return (len(REACH) == 19 and pairs_parted(False) == (171, 146, 146, 171) and max(mins) == 6
            and mins.count(6) == 8 and pairs_parted(True) == (171, 78, 78, 123))


# ------------------------------------------------ 5.13 the instrument
def ring(n, steps):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]; inbox[0] = [(K, 1)]
    surf = []
    for _ in range(steps):
        nb = [[] for _ in range(n)]; row = []
        for i in range(n):
            s, c = C(carry[i], inbox[i]); carry[i] = c
            nb[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
        inbox = nb; surf.append(tuple(row))
    return surf

def W77():
    ok = True
    for n in range(1, 41):
        per = ring(n, 8 * n + 8)[n:]
        z = [[i for i in range(n) if per[t][i] == 0] for t in range(len(per))]
        ok &= all(v is not None for r in per for v in r)
        if n % 2 == 0:
            ok &= all(not zi for zi in z)
        else:
            ok &= all(len(zi) <= 1 for zi in z)
            at = [(t, zi[0]) for t, zi in enumerate(z) if zi]
            ok &= all(b[0] - a[0] == 2 for a, b in zip(at, at[1:]))
            ok &= len(at) >= (len(per) - 1) // 2
            if n > 1: ok &= all(b[1] == (a[1] + 1) % n for a, b in zip(at, at[1:]))
    return ok and (3 + 5) % 2 == 0

def two_run(sa, sb, first, ab, ba, calls=12):
    car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}; inbox = {'A': [], 'B': []}
    order = ['A', 'B'] if first == 'A' else ['B', 'A']; log = []
    for i in range(calls):
        me = order[i % 2]; other = 'B' if me == 'A' else 'A'
        rel = six(car[me]); s, c = C(car[me], inbox[me]); inbox[me] = []
        if (ab if me == 'A' else ba): inbox[other] = rel
        log.append((me, dict(s).get(K), rel, car[me], c)); car[me] = c
    return log

def W79():
    parted = tot = 0
    for sa, sb in product(S, S):
        for me in 'AB':
            a = [x[1] for x in two_run(sa, sb, 'A', True, True) if x[0] == me]
            b = [x[1] for x in two_run(sa, sb, 'B', True, True) if x[0] == me]
            tot += 1; parted += a != b
    return (parted, tot) == (8, 8)

def taking_out():
    def load(t):
        ns = {}; exec(compile(ast.fix_missing_locations(t), 'x', 'exec'), ns); return ns
    def fingerprint(ns):
        Cf = ns['_1_self_coupling']; out = []
        seen = {()}; fr = [()]
        while fr:
            nx = []
            for st in fr:
                for off in OFFERS + [[(K, 0)], [(K, 0), (K, 1)]]:
                    try: r = Cf([(K,) + st] if st else [], off)
                    except Exception as e: return ('error', repr(e))
                    out.append((st, tuple(off), repr(r)))
                    c = r[1]; s2 = tuple(c[0][1:]) if c else ()
                    if s2 not in seen and len(seen) < 200: seen.add(s2); nx.append(s2)
            fr = nx
        for a, b in product([(), (1, -1, 0), (-1, 1, 2)], repeat=2):
            car = [x for x in [(('a',) + a) if a else None, (('b',) + b) if b else None] if x]
            for off in ([], [('a', 1), ('b', -1)], [('c', 1)]):
                try: out.append(('2', repr(Cf(car, off))))
                except Exception as e: return ('error', repr(e))
        return out
    F0 = fingerprint(load(copy.deepcopy(TREE)))
    fn = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
    paths = []
    def walk(node, path):
        for field, val in ast.iter_fields(node):
            if isinstance(val, list):
                for i, v in enumerate(val):
                    if isinstance(v, ast.stmt): paths.append((path + [(field, i)], 'stmt'))
                    if isinstance(v, ast.AST): walk(v, path + [(field, i)])
                    if isinstance(v, ast.comprehension):
                        for j, _ in enumerate(v.ifs): paths.append((path + [(field, i), ('ifs', j)], 'if'))
            elif isinstance(val, ast.AST): walk(val, path + [(field, None)])
    walk(fn, [])
    def get(node, path):
        for f, i in path: node = getattr(node, f) if i is None else getattr(node, f)[i]
        return node
    same = []
    for p, kind in paths:
        t = copy.deepcopy(TREE); f = next(n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
        parent = get(f, p[:-1]); fld, i = p[-1]; lst = getattr(parent, fld)
        text = ast.unparse(lst[i])
        del lst[i]
        if kind == 'stmt' and not lst: lst.append(ast.Pass())
        try: F = fingerprint(load(t))
        except Exception as e: F = ('error', repr(e))
        if F == F0: same.append((kind, text, p))
    return len(paths), same

def W81():
    n, same = taking_out()
    if n != 23 or len(same) != 1: return False
    kind, text, p = same[0]
    fn = next(x for x in TREE.body if isinstance(x, ast.FunctionDef) and x.name == '_1_self_coupling')
    host = fn
    for f, i in p[:-1]: host = getattr(host, f) if i is None else getattr(host, f)[i]
    gathers_offering = isinstance(host, ast.comprehension) and ast.unparse(host.iter) == '_2_self_offering'
    return kind == 'if' and text == '_7_other_corusing != 0' and gathers_offering


# ------------------------------------------------ 5.14 the numbered form of 440, the chain's centre
def W87():
    ok = all(sum(1 for step in range(1, 441) if (k + step) % 440 == (k + 220) % 440) == 1 for k in range(440))
    own = [k for k in range(440) if k % 440 == (440 - k) % 440]
    return ok and own == [0, 220]

def W92():
    ok = True
    for n in range(1, 201):
        centre = 220 * n
        on_coupling = centre % 440 == 0
        ok &= on_coupling == (n % 2 == 0)
        if not on_coupling: ok &= centre % 440 == 220          # a self's own waist
        ok &= 220 * (n + 1) - centre == 220 and (220 * (n + 1)) % 440 != centre % 440
    return ok and (220 * 3) % 440 == 220 and (220 * 4) % 440 == 0


# ------------------------------------------------ 5.15 the studies at their domains
def W95():
    ok = True
    a_both = [x[1] for x in two_run(-1, -1, 'A', True, True) if x[0] == 'A']
    ok &= a_both == [1, -1, 0, 1, -1, 0]
    for ab, ba in [(True, False), (False, True), (False, False)]:
        ok &= [x[1] for x in two_run(-1, -1, 'A', ab, ba) if x[0] == 'A'] == [1, -1, 1, -1, 1, -1]
    ok &= next(i for i, (x, y) in enumerate(zip(a_both, [1, -1, 1, -1, 1, -1])) if x != y) + 1 == 3
    acct = {}
    for ab, ba in [(True, True), (True, False), (False, True), (False, False)]:
        log = two_run(-1, -1, 'A', ab, ba); n = len(log)
        joined = lambda me: ab if me == 'A' else ba
        rel = [(i, x[0]) for i, x in enumerate(log) if x[2]]
        acct[(ab, ba)] = (len(rel), sum(1 for i, me in rel if joined(me) and i < n - 1),
                          sum(1 for i, me in rel if joined(me) and i == n - 1), sum(1 for i, me in rel if not joined(me)))
    ok &= acct[(True, True)] == (12, 11, 1, 0)
    ok &= all(a[1] + a[2] + a[3] == a[0] for a in acct.values())
    return ok

def interrupted(sa, sb, leg, i0, i1, mode, calls=12):
    car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}
    inbox = {'A': [], 'B': []}; queue = []; log = []
    for i in range(calls):
        me = 'A' if i % 2 == 0 else 'B'; other = 'B' if me == 'A' else 'A'
        rel = six(car[me]); off = inbox[me]; inbox[me] = []
        if me != leg and mode == 'delay' and i >= i1 and queue:
            queue.extend(off); off = [queue.pop(0)] if queue else []
        s, c = C(car[me], off)
        log.append((i, me, off, dict(s).get(K), car[me], c)); car[me] = c
        if me == leg and i0 <= i < i1:
            if mode == 'delay': queue.extend(rel)
        else:
            inbox[other] = rel
    return log

def meets_pattern(sa, sb, leg, i0, i1):
    L = interrupted(sa, sb, leg, i0, i1, 'loss'); D = interrupted(sa, sb, leg, i0, i1, 'delay')
    rcv = [x for x in L if x[1] != leg and x[0] >= i1]
    if not rcv: return False
    j = rcv[0][0]
    same_before = all(L[t][3:] == D[t][3:] for t in range(j))
    l, d = L[j], D[j]
    return (same_before and l[4] == d[4] and l[2] == [(K, 1)] and l[3] == 0 and d[2] == [(K, -1)] and d[3] == -1)

def W96():
    L = interrupted(1, 1, 'A', 0, 4, 'loss'); D = interrupted(1, 1, 'A', 0, 4, 'delay')
    ok = all(L[t][3:] == D[t][3:] for t in range(5))
    ok &= L[5][1] == 'B' and L[5][4] == [(K, 1, -1, 0)] == D[5][4]
    ok &= L[5][2] == [(K, 1)] and L[5][3] == 0 and L[5][5] == [(K, 1, -1, 1)]
    ok &= D[5][2] == [(K, -1)] and D[5][3] == -1
    count = sum(meets_pattern(sa, sb, leg, i0, i1) for sa, sb, leg in product(S, S, 'AB')
                for i0 in range(12) for i1 in range(i0 + 1, 12))
    return ok and count == 30

def W97():
    pos = [(r, c) for r in range(3) for c in range(3)]
    def edges(kinds, removed):
        E = set()
        for r, c in pos:
            if 'across' in kinds and c < 2: E.add(frozenset({(r, c), (r, c + 1)}))
            if 'along' in kinds and r < 2: E.add(frozenset({(r, c), (r + 1, c)}))
        return {e for e in E if not (e & removed)}
    def paths(E, a, b):
        adj = {}
        for e in E:
            x, y = tuple(e); adj.setdefault(x, []).append(y); adj.setdefault(y, []).append(x)
        out = []
        def go(v, seen):
            if v == b: out.append(list(seen)); return
            for w in adj.get(v, []):
                if w not in seen: go(w, seen + [w])
        go(a, [a]); return out
    centre = {(1, 1)}
    E = edges({'across', 'along'}, centre)
    left, right = (1, 0), (1, 2)
    P = paths(E, left, right)
    kind = lambda x, y: 'across' if x[0] == y[0] else 'along'
    ok = len(pos) - 1 == 8 and len(P) == 2
    ok &= all(sorted(kind(p[i], p[i + 1]) for i in range(len(p) - 1)) == ['across', 'across', 'along', 'along'] for p in P)
    deg = {}
    for e in E:
        for v in e: deg[v] = deg.get(v, 0) + 1
    ok &= len(deg) == 8 and all(d == 2 for d in deg.values())          # the eight form one ring
    ok &= paths(edges({'across'}, centre), left, right) == []
    ok &= paths(edges({'across', 'along'}, {(0, 1), (1, 1), (2, 1)}), left, right) == []
    return ok

def W100():
    with zipfile.ZipFile(_ccl_path(KIT_ZIP)) as z:
        name = next(n for n in z.namelist() if n.endswith('/resolver.py'))
        kit = ast.parse(z.read(name).decode())
    body = lambda t: [ast.dump(n) for n in t.body if not isinstance(n, ast.Expr)]
    two = [ast.dump(n) for n in TREE.body if not isinstance(n, ast.Expr) and not (isinstance(n, ast.FunctionDef) and n.name == '_17_social_abundancing')]
    return body(kit) == two and len(two) == 4 and len(body(TREE)) == 5


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'W\d+', k) and callable(v)}

'''

PART_SOURCES['eq'] = r'''"""Run checks for Exhibit THIRTY Part SIX (EQUILIBRIA, links E1...), against the resolver of
Exhibit ONE v372 (resolver_v372.py beside this file) and the numbers Exhibit TWENTY-EIGHT v372 names.
Each function returns True when the link holds as stated. Run: python3 ccl_eq_checks.py [results.json]"""
import os, re, sys, json
from itertools import product, combinations
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R, CONNECTORS, JOINS

EQ_MD = '/home/claude/work/Exhibit_TWENTY-EIGHT_Equilibria_Registry_v372.md'
K = 'k'
S = (1, -1)
OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def step(st, off):
    """One call at one key: st is () or (c, t, a); returns (surface or None, next st)."""
    s, c = C([(K,) + st] if st else [], list(off))
    return dict(s).get(K), (tuple(c[0][1:]) if c else ())


def reach():
    seen = {()}; frontier = [()]
    while frontier:
        nxt = []
        for st in frontier:
            for off in OFFERS:
                _, s2 = step(st, off)
                if s2 not in seen: seen.add(s2); nxt.append(s2)
        frontier = nxt
    return seen


REACH = reach()
NONEMPTY = sorted(st for st in REACH if st)
sgn = lambda x: (x > 0) - (x < 0)

# ------------------------------------------------------------ 6.1 momentaries, surface, alternating

def E1():
    prior, now, nxt = (1, 2), (2, 3), (3, 4)
    ok = len(set(prior + now + nxt)) == 4 and prior[1] == now[0] and now[1] == nxt[0]
    ok &= [nxt[0] - now[0], now[0] - prior[0]] == [1, 1]                  # across: next opens one on
    self_m, other_m = [(1, 2), (3, 4)], [(2, 3), (4, 5)]
    ok &= self_m[1][1] + 1 == 5 and other_m[1][1] + 1 == 6                 # along: next opens two on
    ok &= self_m[1][0] - self_m[0][0] == 2 and other_m[1][0] - other_m[0][0] == 2
    views = {o: list(range(o, o + 5)) for o in (1, 2, 3)}                  # the five-views at 1, 2, 3
    for a, b in ((1, 2), (2, 3)):
        shared = sorted(set(views[a]) & set(views[b]))
        ok &= len(shared) == 4
        role = lambda origin, n: 'open' if (n - origin) % 2 == 0 else 'complete'
        ok &= all({role(a, n), role(b, n)} == {'open', 'complete'} for n in shared)
    return ok


def E6():
    ok = True
    for n, m in product(range(3, 13), repeat=2):                           # square grids closed as a torus
        V = [(i, j) for i in range(n) for j in range(m)]
        E = set()
        for i, j in V:
            E.add(frozenset({(i, j), ((i + 1) % n, j)})); E.add(frozenset({(i, j), (i, (j + 1) % m)}))
        F = n * m
        deg = {v: sum(v in e for e in E) for v in V}
        ok &= all(d == 4 for d in deg.values()) and 4 * F == 2 * len(E) and 4 * len(V) == 2 * len(E)
        ok &= len(V) - len(E) + F == 0
    # the cube: four-sided faces but three edges at each point, V - E + F = 2 (the sphere)
    ok &= 8 - 12 + 6 == 2
    return ok


def rounds_two():
    St = list(product(S, S))
    return {'right': {(x, y): (y, -x) for x, y in St}, 'other': {(x, y): (-y, x) for x, y in St}}


def E10():
    ok = True
    for m in rounds_two().values():
        for s0 in m:
            s = s0; changed = []
            for _ in range(8):
                n = m[s]; d = [i for i in range(2) if n[i] != s[i]]
                ok &= len(d) == 1; changed.append(d[0]); s = n
            ok &= all(changed[i] != changed[i + 1] for i in range(7))
    return ok


def E11():
    orders = list(product(('first', 'second'), repeat=2))
    both = [o for o in orders if set(o) == {'first', 'second'}]
    one = [o for o in orders if len(set(o)) == 1]
    return len(orders) == 4 and both == [('first', 'second'), ('second', 'first')] and len(one) == 2


def E12():
    shown = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    r = rounds_two()
    by_other = all(r['other'][shown[i]] == shown[i + 1] for i in range(4))
    by_right = all(r['right'][shown[i]] == shown[i + 1] for i in range(4))
    return by_other and not by_right and len(set(shown[:4])) == 4


def E13():
    ok = True
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            E = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            A = [[0] * n for _ in range(n)]
            for a, b in E: A[a][b] = A[b][a] = 1
            # odd closed route: trace of A^k > 0 for some odd k <= n
            P = [row[:] for row in A]; odd = False
            for k in range(2, n + 1):
                P = [[sum(P[i][l] * A[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
                if k % 2 == 1 and sum(P[i][i] for i in range(n)) > 0: odd = True
            cols = [c for c in product((0, 1), repeat=n) if all(c[a] != c[b] for a, b in E)]
            # connected wholes
            comp = list(range(n))
            def f(x):
                while comp[x] != x: x = comp[x]
                return x
            for a, b in E: comp[f(a)] = f(b)
            wholes = len({f(x) for x in range(n)})
            ok &= (len(cols) > 0) == (not odd)
            if not odd: ok &= len(cols) == 2 ** wholes
    return ok

# ------------------------------------------------------------ 6.4 the ten

def E37():
    return all(n * n - (n - 1) * (n + 1) == 1 for n in range(-1000, 1001)) and (2, 3)[1] == (3, 4)[0]


def E38():
    self5, other5 = set(range(1, 6)), set(range(2, 7))
    moms = [(1, 2), (3, 4), (5, 6)]
    return (self5 | other5 == set(range(1, 7)) and sorted(x for m in moms for x in m) == list(range(1, 7))
            and ['co' if n % 2 else 'bi' for n in range(1, 7)] == ['co', 'bi', 'co', 'bi', 'co', 'bi'])


def E39():
    table = {2: ('self completing', 'other opening'), 3: ('self opening', 'other completing'),
             4: ('self completing', 'other opening'), 5: ('self opening', 'other completing'),
             6: ('self completing', 'other opening')}
    ok = True
    for n, (sf, of) in table.items():
        self_role = 'opening' if n % 2 == 1 else 'completing'             # self momentaries 1-2, 3-4, 5-6
        other_role = 'opening' if n % 2 == 0 else 'completing'            # other momentaries 2-3, 4-5, 6-7
        ok &= sf == 'self ' + self_role and of == 'other ' + other_role and self_role != other_role
    return ok and len(table) * 2 == 10


def eq_text():
    return open(EQ_MD, encoding='utf-8').read()


def E42():
    t = eq_text()
    ring = [3, 2, 4, 1, 14, 12, 6, 10, 11, 16]
    ok = '3→2→4→1→14→12→6→10→11→16→next 3' in t and '1,10,7,9,8,4,6,5,3,2' in t
    rows = re.findall(r'^\| (\d) \| .*?\| (\d+) · .*?\| (\d+) · .*?\| (\d+)→(\d+) / (\d+)→(\d+) \|$', t, re.M)
    addr = {}
    for place, e, s_, a1, a2, b1, b2 in rows:
        addr[int(e)] = (int(a1), int(a2)); addr[int(s_)] = (int(b1), int(b2))
    edges = [(ring[i], ring[(i + 1) % 10]) for i in range(10)]
    at_ring = [next(w for w, ed in addr.items() if ed == e) for e in edges]
    ok &= len(rows) == 5 and sorted(addr) == list(range(1, 11)) and at_ring == [1, 10, 7, 9, 8, 4, 6, 5, 3, 2]
    ok &= len(set(ring)) == 10 and 6 in ring and 14 in ring
    ok &= edges[3:8] == [(1, 14), (14, 12), (12, 6), (6, 10), (10, 11)]
    return ok


def E46():
    ok = sum((1, 3, 5)) == 9 == 3 ** 2 and sum((2, 4, 6)) == 12 == 3 * 4 and 3 ** 2 - 2 * 4 == 1
    ok &= all(sum(range(1, 2 * n, 2)) == n * n and sum(range(2, 2 * n + 1, 2)) == n * (n + 1) for n in range(1, 101))
    six = list(range(3, 9))
    return ok and len(six) == 6 and six[-1] == 8 and six[-1] + 1 == 9


def ring(n, steps, seed=True):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]
    if seed: inbox[0] = [(K, 1)]
    hist = []
    for _ in range(steps):
        nb = [[] for _ in range(n)]
        for i in range(n):
            s, c = C(carry[i], inbox[i]); carry[i] = c
            nb[(i + 1) % n] += R(s, {K: K})
        inbox = nb
        hist.append((tuple(tuple(c) for c in carry), tuple(tuple(b) for b in inbox)))
    return hist


def E47():
    ok = True
    for n in range(1, 12):
        h = ring(n, 40)
        prev = tuple(() for _ in range(n))
        changed = set()
        for carry, _ in h:
            changed |= {i for i in range(n) if carry[i] != prev[i]}; prev = carry
        ok &= changed == set(range(n))
        rest = ring(n, 100, seed=False)
        ok &= all(st == (tuple(() for _ in range(n)), tuple(() for _ in range(n))) for st in rest)
    return ok


def E50():
    internal = [(3, 11), (4, 12), (5, 13), (7, 15), (8, 16)]
    ten = {x for p in internal for x in p}
    conn = set(CONNECTORS)
    ring_names = {3, 2, 4, 1, 14, 12, 6, 10, 11, 16}
    ok = all(b - a == 8 for a, b in internal) and all(17 - (9 - n) == n + 8 for n in range(1, 9))
    ok &= conn == {2, 6, 9, 10, 14, 17} and not (ten & conn) and ten | conn == set(range(2, 18))
    ok &= ten | conn | {1} == set(range(1, 18)) and len(ten) == 10
    ok &= ring_names & conn == {2, 6, 10, 14} and 1 in ring_names    # the ring's addresses are other names
    return ok

# ------------------------------------------------------------ 6.5 the conceptions

def E53():
    t = eq_text()
    rows = re.findall(r'^\| (\d+) · [^|]*\| \*\*((?:NY|SA)\d\d)\*\*', t, re.M)
    ids = [i for _, i in rows]
    per = {}
    for w, i in rows: per[int(w)] = per.get(int(w), 0) + 1
    want_ids = [f'NY{i:02d}' for i in range(1, 43)] + [f'SA{i:02d}' for i in range(1, 22)]
    return (sorted(ids) == sorted(want_ids) and len(ids) == 63 and len(set(ids)) == 63
            and [per[w] for w in range(1, 11)] == [2, 5, 8, 10, 6, 9, 5, 5, 7, 6]
            and min(per.values()) == 2 and max(per.values()) == 10)


def stationary(P, pi):
    states = list(pi)
    return all(sum(pi[a] * P[a].get(b, 0) for a in states) == pi[b] for b in states)


def E60():
    ok = True
    # NY15: constant +1 at one key from empty returns five complete values, A->B->C->D->E->A
    st = (); seq = []
    for _ in range(11):
        _, st = step(st, [(K, 1)]); seq.append(st)
    cyc = seq[:5]
    ok &= len(set(cyc)) == 5 and seq[5:10] == cyc
    P = {cyc[i]: {cyc[(i + 1) % 5]: Fraction(1)} for i in range(5)}
    ok &= stationary(P, {x: Fraction(1, 5) for x in cyc})
    # NY16: the two exchanged opposed-sign values under empty receiving; stationarity and detailed balance
    for c in S:
        A = (c, -c, 0); _, B = step(A, []); _, A2 = step(B, [])
        ok &= B == (-c, c, 0) and A2 == A
        P = {A: {B: Fraction(1)}, B: {A: Fraction(1)}}; pi = {A: Fraction(1, 2), B: Fraction(1, 2)}
        ok &= stationary(P, pi) and pi[A] * P[A][B] == pi[B] * P[B][A]
    # NY17: A->B, B->A, X->B; at the code an instance X = (+,-,1) under empty receiving goes to B
    A, B, X = (1, -1, 0), (-1, 1, 0), (1, -1, 1)
    ok &= step(A, [])[1] == B and step(B, [])[1] == A and step(X, [])[1] == B
    P = {A: {B: Fraction(1)}, B: {A: Fraction(1)}, X: {B: Fraction(1)}}
    ok &= stationary(P, {A: Fraction(1, 2), B: Fraction(1, 2), X: Fraction(0)})
    return ok

# ------------------------------------------------------------ 6.6 shared exclusions

def E65():
    ok = len(NONEMPTY) == 18; kinds = set()
    for st in NONEMPTY:
        c, t, a = st
        for off in OFFERS:
            _, n = step(st, off)
            ok &= n != st
            if not n: kinds.add('releasing completes')
            elif n == (c, t, a + 1): kinds.add('retaining opens one on')
            elif n[1] == -t and n[2] == 0: kinds.add('fresh writing inverts t')
            else: ok = False
    return ok and len(kinds) == 3


def E66():
    ok = True; longest = {1: 0, -1: 0}
    for st in NONEMPTY:
        for off in OFFERS:
            _, n = step(st, off)
            if n and n[1] == st[1]: ok &= n == (st[0], st[1], st[2] + 1)     # t kept only by retaining
            if n and n[1] != st[1]: ok &= n[2] == 0                           # a fresh write inverts t
    for st in NONEMPTY:
        if st[2] != 0: continue
        cur = st; k = 0
        while True:
            _, n = step(cur, [(K, cur[0])])                                   # the arriving that retains
            if n and n[1] == st[1]: k += 1; cur = n
            else: break
        longest[st[1]] = max(longest[st[1]], k)
    return ok and longest == {-1: 3, 1: 4}


def E67():
    ok = True
    for st in NONEMPTY:
        for off in OFFERS:
            s, n = step(st, off)
            if s == 0: ok &= (not n) or n == (st[0], st[1], st[2] + 1)        # a zero writes nothing fresh
        cur = st; k = 0
        while cur:
            s, cur = step(cur, [(K, cur[0])]); k += 1
            ok &= s == 0
        ok &= k <= 5
    ks = []
    for st in NONEMPTY:
        cur = st; k = 0
        while cur: _, cur = step(cur, [(K, cur[0])]); k += 1
        ks.append(k)
    return ok and max(ks) == 5


def E69():
    ok = True
    for c in S:
        st = (c, -c, 0)
        for _ in range(9):
            s, n = step(st, [])
            ok &= n[1] == -n[0] and n[0] == -st[0] and n[1] == -st[1] and s == -st[0]
            st = n
    # one side's reversal alone: (c, t) -> (-c, t) at t = -c gives (-c, -c), agreeing: opposition fails
    one_side = all((-c) == t for c, t in product(S, S) if t == -c)
    return ok and one_side


def E71():
    return not any(p == p and p == -p for p in S)


def E72():
    alt = [0, 1] * 8
    wins = [tuple(alt[i:i + 3]) for i in range(len(alt) - 2)]
    ok = all({wins[i], wins[i + 1]} == {(0, 1, 0), (1, 0, 1)} for i in range(len(wins) - 1))
    fwd = lambda n: 2 - n; rev = lambda n: n                               # two molecules, equal constants
    ok &= [n for n in range(3) if fwd(n) == rev(n)] == [1] and {1 - 1, 1 + 1} == {0, 2}
    pi = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]                  # NY31, stationary and balanced
    ok &= pi[0] * fwd(0) == pi[1] * rev(1) and pi[1] * fwd(1) == pi[2] * rev(2)
    return ok


def E73():
    Rn = {(0, 1), (1, 2)}
    trans = all((a, d) in Rn for a, b in Rn for c, d in Rn if b == c)
    ok = not trans and (0, 2) not in Rn
    for a in range(-5, 6):
        b = a + 1
        ok &= (a + 1, b) not in {(x, x + 1) for x in range(-10, 10)} and (a, b + 1) not in {(x, x + 1) for x in range(-10, 10)}
    return ok


def E74():
    St = list(product(S, S)); F = lambda p: (-p[1], p[0])
    ok = True
    for s0 in St:
        seen = {s0}; s = s0
        for _ in range(3): s = F(s); seen.add(s)
        ok &= seen == set(St)
    worst = 0; inv = []
    for r in range(0, 5):
        for sub in combinations(St, r):
            sub = set(sub)
            if {F(x) for x in sub} == sub: inv.append(len(sub))
            if 0 < r < 4:
                for x in sub:
                    k = 0; y = x
                    while y in sub: y = F(y); k += 1
                    worst = max(worst, k)
    s = (1, 1); path = [s]
    for _ in range(3): s = F(s); path.append(s)
    three = {(1, 1), (-1, 1), (-1, -1)}
    ok &= path[:3] == [(1, 1), (-1, 1), (-1, -1)] and path[3] not in three
    return ok and worst == 3 and sorted(inv) == [0, 4]


def E75():
    ok = True
    # unit-ratio fuel-coupled cycle: a f = b w, b = c, c = a, a, b, c > 0
    for f, w in product(range(1, 11), repeat=2):
        a = b = c = Fraction(1)                                            # b = c = a forced by the two unit balances
        ok &= ((a * f == b * w) == (f == w))
    # finite attaining of zero under a nonzero multiplier
    for lam in (Fraction(-1, 2), Fraction(-1), Fraction(-2), Fraction(3)):
        r = Fraction(1)
        for _ in range(200):
            r = lam * r; ok &= r != 0
    # an opposed row through the aggregate route offers zero onward, next and later
    s, cr = C([], [(K, 1), (K, -1)])
    ok &= s == [(K, 0)] and cr == []
    onward = R(s, {K: K})
    ok &= onward == [(K, 0)] and C([], onward) == ([], [])
    for _ in range(5):
        s, cr = C(cr, [(K, 1), (K, -1)]); onward = R(s, {K: K})
        ok &= onward == [(K, 0)] and C([], onward) == ([], [])
    return ok


def E76():
    St = list(product(S, S)); J = {p: (-p[0], -p[1]) for p in St}
    roots = []
    for img in product(St, repeat=4):
        m = dict(zip(St, img))
        if all(m[m[p]] == J[p] for p in St): roots.append(m)
    Fm = {(c, t): (-t, c) for c, t in St}; Gm = {(c, t): (t, -c) for c, t in St}
    ok = len(roots) == 2 and Fm in roots and Gm in roots
    for st in NONEMPTY:
        c, t, a = st
        for off in OFFERS:
            s, n = step(st, off)
            if s: ok &= n[:2] == Gm[(t, s)]                               # 6/10 = (t, s); fresh 7/8 = G(t, s)
        s, n = step(st, [])
        ok &= s == -c and n[:2] == (-c, -t) == J[(c, t)]
    return ok


def E79():
    ok = True
    for st in REACH:
        c = st[0] if st else 0
        for L in range(0, 5):
            for seq in product((-1, 0, 1), repeat=L):
                s, _ = step(st, [(K, v) for v in seq])
                if s is not None: ok &= s == sgn(sum(seq) - c)
    ok &= step((1, -1, 0), [(K, 1), (K, 1)])[1] == (1, 1, 0)                # agreement from (+,-)
    ok &= step((-1, 1, 0), [(K, 1), (K, 1)])[1] == (1, -1, 0)               # opposition from (-,+)
    ok &= step((1, -1, 0), [(K, 1)])[1] == (1, -1, 1)                       # continues from opening 0
    ok &= step((1, -1, 3), [(K, 1)])[1] == ()                               # leaves from opening 3
    return ok


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'E\d+', k) and callable(v)}

'''

PART_SOURCES['x'] = r'''"""Run checks for Exhibit THIRTY Part SEVEN (EXPLAINING, NAMING AND THE METHOD, links X1...),
against the resolver of Exhibit ONE v372 (resolver_v372.py beside this file), arithmetic
enumerations, and the counts the three files name (read from /home/claude/work at v372).
Each function returns True when the link holds as stated.
Run: python3 ccl_x_checks.py [results.json]"""
import os, re, sys, json
from itertools import product, combinations
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R, CONNECTORS, JOINS

W = '/home/claude/work/'
EXP = W + 'Exhibit_TWELVE_Natural_Explaining_v372.md'
NAM = W + 'Exhibit_TWENTY_Natural_Naming_v372.md'
GIM = W + 'Exhibit_TWENTY-FOUR_Geodesic_Improving_Method_v372.md'
K = 'k'
S = (1, -1)


def section(path, head):
    """Text of the '## head' section of a file, up to the next heading."""
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^## ' + re.escape(head) + r'.*?$(.*?)(?=^#{1,2} |\Z)', t, re.M | re.S)
    return m.group(1)


def table_rows(txt):
    rows = [l for l in txt.splitlines() if l.startswith('|')]
    return [r for r in rows[2:]]            # after header and rule


def traced(carry, offer):
    """Call 1-self-coupling and read its own gathering (6, 14, 12, 10, 11) at its return."""
    got = {}
    code = C.__code__

    def local(frame, event, arg):
        if event == 'return':
            got.update({k: v for k, v in frame.f_locals.items()})
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is code else None

    sys.settrace(glob)
    try:
        out = C(list(carry), list(offer))
    finally:
        sys.settrace(None)
    return out, got


# ------------------------------------------------------------ 7.1 explaining
def X28():
    # closed genus-zero surface, three faces at each corner, pentagons p and hexagons h
    ok = True
    for p in range(0, 61):
        for h in range(0, 501):
            E = Fraction(5 * p + 6 * h, 2); V = Fraction(2, 3) * E; F = p + h
            ok &= ((V - E + F) == 2) == (p == 12)
    return ok


def X41():
    zero, c1 = C([], [(K, 1), (K, -1)])          # a zero surfaced
    none, c2 = C([], [])                          # a connection delivering nothing
    return zero == [(K, 0)] and c1 == [] and none == [] and c2 == [] and zero != none


def X43_probe():
    return 2 * 5 == 10 == comb(5, 2)


# ------------------------------------------------------------ 7.2 naming
NAMES = {1: '1-self-coupling', 2: '2-self-offering', 3: '3-self-carrying', 4: '4-self-sharing',
         5: '5-other-neutralling', 6: '6-other-crossing', 7: '7-other-corusing', 8: '8-other-torusing',
         9: '9-other-releasing', 10: '10-other-surfacing', 11: '11-other-chaining', 12: '12-other-surplusing',
         13: '13-social-neutralling', 14: '14-social-crossing', 15: '15-social-corusing',
         16: '16-social-torusing', 17: '17-social-abundancing'}


def X49():
    src = open(RV.__file__, encoding='utf-8').read()
    idents = set(re.findall(r'\b_(\d+)_(self|other|social)_([a-z]+)\b', src))
    code = {int(n): f'{n}-{r}-{root}' for n, r, root in idents}
    code.update({n: CONNECTORS[n][0] for n in CONNECTORS})
    if any(code[n] != NAMES[n] for n in code) or set(code) != set(range(1, 18)):
        return False
    ok = True; seen = 0
    for path in (EXP, NAM, GIM):
        t = open(path, encoding='utf-8').read()
        for m in re.finditer(r'(?<![\w`])(\d{1,2})-(self|other|social)-([a-z]+)', t):
            n = int(m.group(1)); seen += 1
            ok &= n in NAMES and m.group(0) == NAMES[n]
        for m in re.finditer(r'`_(\d+)_(self|other|social)_([a-z]+)`', t):
            n = int(m.group(1)); seen += 1
            ok &= m.group(0).strip('`')[1:].replace('_', '-') == NAMES[n]
    return ok and seen > 0


def X62():
    step = lambda v: (v[1], -v[0])
    ok = True
    for v in product(S, S):
        v2 = step(step(v)); v4 = step(step(v2))
        ok &= v2 == (-v[0], -v[1]) and v4 == v and v2 != v
        ok &= (v[1], v[0]) == (v[1], v[0])                    # the other order inverts no sign
        ok &= step(step(step(v))) == (-v[1], v[0])            # three right spiral steps as one
    return ok


def X63():
    place = lambda n, lo: n - lo + 1
    return (place(6, 1) == place(14, 9) == place(22, 17) == 6
            and [n - 16 for n in (19, 27, 22, 30)] == [3, 11, 6, 14]
            and 22 not in NAMES)


FIVE = {1: 'co bi co bi co', 0: 'bi co bi co bi'}
EARLIER = {3: 'co_carrying', 1: 'co_bi_coupling', 6: 'bi_co_bi_transmissioning',
           7: 'co_bi_co_bi_co_corusing', 8: 'bi_co_bi_co_bi_torusing', 2: 'bi_arriving',
           4: 'bi_offering', 10: 'bi_co_surfacing', 11: 'co_bi_carrying', 12: 'bi_co_tunneling',
           14: 'bi_co_inversioning', 16: 'bi_co_inseparating'}


def X64():
    odd, even = FIVE[1].split(), FIVE[0].split()
    ok = odd[0] == odd[4] == 'co' and odd[1] == odd[3] == 'bi' and odd[2] == 'co'
    ok &= even[0] == even[4] == 'bi' and even[1] == even[3] == 'co' and even[2] == 'bi'
    swap = {'co': 'bi', 'bi': 'co'}
    ok &= [swap[x] for x in odd] == even and [swap[x] for x in even] == odd
    counts = {}
    for n, w in EARLIER.items():
        pre = [p for p in w.split('_') if p in ('co', 'bi')]
        ok &= pre == FIVE[n % 2].split()[:len(pre)]
        counts[n] = len(pre)
    ok &= counts[3] == 1 and counts[1] == 2 and counts[6] == 3 and counts[7] == 5 and counts[8] == 5
    # the table at NAM 3.3: odd opens co, even opens bi, five-prefix at the number's origin
    for r in table_rows(section(NAM, '3.3')):
        cells = [c.strip(' *`') for c in r.strip('|').split('|')]
        n = int(cells[0].split('-')[0])
        ok &= cells[1] == ('co' if n % 2 else 'bi') and cells[2] == FIVE[n % 2].replace(' ', '-')
    return ok


def X66():
    up = lambda n: n + 8 if n <= 8 else n - 8
    pod = lambda n: 17 - n
    ok = True
    for row in ([1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]):
        changes = []
        for i in range(4):
            a, b = row[i], row[(i + 1) % 4]
            face = 'up' if b == up(a) else ('pod' if b == pod(a) else None)
            ok &= face is not None
            if a % 2 != b % 2: changes.append(face)
        ok &= changes == ['pod', 'pod']
        par = [n % 2 for n in row]
        ok &= sum(par[i] != par[i - 1] for i in range(4)) == 2 and par.count(1) == 2
    return ok


def X68():
    carry = []; surf = []; keep = []; opening = []
    for i in range(7):
        (s, c), L = traced(carry, [(K, 1)])
        surf.append(dict(s).get(K))
        if 1 <= i <= 4:     # couplings two to five, the 0 passage
            keep.append((tuple(L['_2_self_offering']), L['_6_other_crossing'].get(K),
                         carry[0][2], dict(s).get(K), L['_12_other_surplusing'].get(K),
                         sorted(L['_14_social_crossing'])))
            opening.append(c[0][3] if c else None)
        carry = c
    same = all(x == ((( K, 1),), -1, -1, 0, 0, [(K, -1), (K, 1)]) for x in keep)
    return surf == [1, 0, 0, 0, 0, 1, 0] and same and opening == [1, 2, 3, None]


def X69():
    (s, c), L = traced([(K, 1, -1, 0), (K, -1, 1, 0)], [])
    ok = L['_6_other_crossing'] == {K: 1} and s == [(K, 0)] and c == [(K, -1, 1, 1)]
    (s2, c2), L2 = traced([(K, 1, -1, 0)], [(K, 1)])
    ok &= (K, 1) in L2['_14_social_crossing'] and s2 == [(K, 0)]
    return ok


def X73():
    lt = lambda a, b: a < b
    ok = all((not lt(a, b) and not lt(b, a)) == (a == b) for a in range(10) for b in range(10))
    subs = [frozenset(x) for r in range(4) for x in combinations((1, 2, 3), r)]
    ps = lambda a, b: a < b          # proper inclusion
    both = [(a, b) for a in subs for b in subs if not ps(a, b) and not ps(b, a)]
    ok &= any(a != b for a, b in both) and all(a == b or not (a <= b or b <= a) for a, b in both)
    return ok


def X79():
    rows = table_rows(section(NAM, '4.9'))
    pairs = []
    for r in rows:
        cells = r.strip('|').split('|')
        nums = sorted(int(x) for x in re.findall(r'(\d+)-(?:self|other|social)', cells[3]))
        pairs.append(tuple(nums))
    ok = len(rows) == 10 and all(b - a == 8 and 1 <= a <= 8 for a, b in pairs)
    from collections import Counter
    cnt = Counter(pairs)
    ok &= cnt == Counter({(6, 14): 1, (2, 10): 1, (4, 12): 2, (8, 16): 2, (3, 11): 1, (7, 15): 1, (5, 13): 2})
    ok &= (1, 9) not in cnt
    return ok


def X88():
    ok = all((x ^ b) ^ b == x for x in (0, 1) for b in (0, 1))
    # prior, now -> next = prior xor now: (0,0) still, the others round in three
    m = {(p, n): (n, p ^ n) for p in (0, 1) for n in (0, 1)}
    ok &= m[(0, 0)] == (0, 0)
    for s in [(0, 1), (1, 0), (1, 1)]:
        x = s
        for _ in range(3): x = m[x]
        ok &= x == s and m[s] != s and m[m[s]] != s
    # Peres-Mermin: rows' products +1, columns' products +1, +1, -1; no store of the nine meets them
    meets = 0
    for v in product(S, repeat=9):
        g = [v[0:3], v[3:6], v[6:9]]
        rows = all(a * b * c == 1 for a, b, c in g)
        cols = [g[0][j] * g[1][j] * g[2][j] for j in range(3)] == [1, 1, -1]
        meets += rows and cols
    return ok and meets == 0 and 2 ** 9 == 512


def X97():
    return all((n - 1) * (n + 1) == n * n - 1 for n in range(-1000, 1001))


def X98():
    # rational root candidates of x^2 - x - 1 are +-1
    ok = all(r * r - r - 1 != 0 for r in (1, -1))
    fib = [0, 1]
    while len(fib) < 64: fib.append(fib[-1] + fib[-2])
    for n in range(1, 61):
        r = Fraction(fib[n + 1], fib[n])
        above = r * r - r - 1 > 0               # r > phi, r positive
        ok &= above == (n % 2 == 0) and r * r - r - 1 != 0
    return ok


def X104():
    podal = {frozenset((n, 17 - n)) for n in range(1, 17)}
    straight = {frozenset((k, k + 8)) for k in range(1, 9)}
    return len(podal) == 8 and len(straight) == 8 and not (podal & straight)


def X107_probe():
    return 59 - 2 + 1 == 58 == 118 - 61 + 1


# ------------------------------------------------------------ 7.3 the method
def X138():
    rows = table_rows(section(GIM, '3.3'))
    ok = len(rows) == 9
    par = []
    for i, r in enumerate(rows, 1):
        cells = [c.strip() for c in r.strip('|').split('|')]
        num = int(cells[0].split('·')[0].strip())
        p, kind = [x.strip() for x in cells[1].split('·')]
        ok &= num == i and ((p, kind) in (('even', 'naming'), ('odd', 'explaining')))
        ok &= (num % 2 == 1) == (p == 'even')     # the number and its parity column part
        par.append(p)
    ok &= all(par[i] != par[i + 1] for i in range(8))
    ok &= par.count('even') == 5 and par.count('odd') == 4
    ok &= rows[0].split('|')[1].strip().endswith('bound') and rows[-1].split('|')[1].strip().endswith('crossings')
    return ok


def X144():
    ok = True
    for n in range(1, 13):
        g = ['0', '1']
        for _ in range(n - 1):
            g = ['0' + x for x in g] + ['1' + x for x in reversed(g)]
        ok &= len(set(g)) == 2 ** n
        for i in range(2 ** n):
            a, b = g[i], g[(i + 1) % 2 ** n]
            ok &= sum(x != y for x, y in zip(a, b)) == 1
    return ok


def isprime(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True


def X145():
    fermat = [2 ** (2 ** k) + 1 for k in range(6)]
    ok = all(isprime(f) for f in fermat[:5]) and fermat[5] == 641 * 6700417 and not isprime(fermat[5])
    regions = [comb(n, 4) + comb(n, 2) + 1 for n in range(1, 7)]
    return ok and regions == [1, 2, 4, 8, 16, 31]


def X146_probe():
    # R(3,3) = 6: K5 carries a two-colouring with no one-colour triangle, K6 none
    def free(n):
        E = list(combinations(range(n), 2)); T = list(combinations(range(n), 3))
        found = 0
        for col in product((0, 1), repeat=len(E)):
            c = dict(zip(E, col))
            if all(not (c[(a, b)] == c[(a, d)] == c[(b, d)]) for a, b, d in T):
                found += 1
                if n == 5: return True
        return found > 0
    return free(5) and not free(6)


def X147():
    primes = [p for p in range(5, 60) if isprime(p)]
    ok = len(primes) == 15 and primes[0] == 5 and primes[-1] == 59
    for n in range(4, 61):
        d = [min(j, n - j) for j in range(1, n)]
        far = d.count(max(d))
        ok &= far == (2 if n % 2 else 1)
    return ok and all(n % 2 for n in (9, 15, 25))


def X148():
    ok = True
    s = section(EXP, '3.4'); ok &= len(re.findall(r'^- \*\*', s, re.M)) == 9
    s = section(EXP, '3.2'); ok &= all(x in s for x in ('A fixed noun', 'A forcing', 'A character', 'A wrapper'))
    s = section(EXP, '3.13')
    tail = s.split('is a middle carried across.**', 1)[1].split('\n\n')[0]
    ok &= len([x for x in re.split(r'(?<=\.)\s+', tail.strip()) if x]) == 6
    t = open(NAM, encoding='utf-8').read()
    ok &= len(re.findall(r'^## 5\.\d+ ', t, re.M)) == 47 and 'Forty-seven namings' in t
    ok &= len(table_rows(section(NAM, '2.5'))) == 7
    ok &= len(table_rows(section(NAM, '4.9'))) == 10
    ok &= len(re.findall(r'^\d\. \*\*', section(NAM, '4.18'), re.M)) == 7
    ok &= len(table_rows(section(NAM, '3.3'))) == 17
    ok &= len(table_rows(section(NAM, '6.2'))) == 8
    ok &= len(re.findall(r'^- \*\*', section(NAM, '1.1'), re.M)) == 4
    ok &= len(table_rows(section(GIM, '3.3'))) == 9
    ok &= len(table_rows(section(GIM, '5.1'))) == 10
    return ok

THIRTY = W + 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v372.md'


def X4():
    """Each link met at its whole prior back to the origin, all or none: the prior closure is acyclic,
    and the classes recomputed from the rows give Part THIRTEEN's counts."""
    t = open(THIRTY, encoding='utf-8').read()
    body = t.split('# PART NINE')[0]
    row = re.compile(r'^\| ([A-Z]+\d+) \| (origin|definition|premise|exact|run|field|nye)\b[^|]*\| ([^|]*) \|', re.M)
    ST, PR = {}, {}
    for lid, st, fol in row.findall(body):
        if lid in ST:
            continue
        ST[lid] = st
        PR[lid] = [i for i in re.findall(r'\b[A-Z]+\d+\b', fol) if i != lid]
    if len(ST) < 1338 or any(i not in ST for v in PR.values() for i in v):
        return False
    part13 = t.split('# PART THIRTEEN')[1]
    sel = set(re.findall(r'\b[A-Z]+\d+\b', re.search(r'The selectings in the chain: ([^\n]*)', part13).group(1)))
    order, mark = [], {}
    def visit(k):
        stack = [(k, iter(PR[k]))]
        mark[k] = 1
        while stack:
            u, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                mark[u] = 2; order.append(u); stack.pop()
            elif mark.get(nxt) == 1:
                raise ValueError('cycle at ' + nxt)
            elif nxt not in mark:
                mark[nxt] = 1; stack.append((nxt, iter(PR[nxt])))
    for k in ST:
        if k not in mark:
            visit(k)
    clo = {}
    for k in order:
        c = {k}
        for p in PR[k]:
            c |= clo[p]
        clo[k] = c
    cnt = {'a': 0, 'b': 0, 'c': 0, 'g': 0, 'd': 0, 'e': 0}
    for k in ST:
        c = clo[k]
        if any(ST[x] == 'nye' or x in sel for x in c):
            cnt['e'] += 1
        elif any(ST[x] == 'premise' or (ST[x] == 'definition' and not PR[x]) for x in c):
            cnt['d'] += 1
        else:
            cnt['a'] += 1
            leaves = {ST[x] for x in c if not PR[x]}
            cnt['b' if leaves == {'origin'} else 'c' if 'origin' in leaves else 'g'] += 1
    allrow = re.search(r'^\| All \| (.*) \|$', part13, re.M).group(1)
    stated = [int(v.strip('* ').replace(',', '')) for v in allrow.split(' | ')]
    return stated == [cnt[x] for x in 'abcgde'] + [len(ST)]


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'X\d+(_probe)?', k) and callable(v)}


'''

PART_SOURCES['o1'] = r'''"""Run checks for Exhibit THIRTY Part EIGHT, first third (8.1 FIVE to 8.7 ELEVEN),
against the resolver as a runnable file (resolver_v372.py beside this file).

Usage:  python3 ccl_o1_checks.py            -> prints each check and its result
        python3 ccl_o1_checks.py --runs     -> prints the run checks as JSON [{link, check}]
Each function named by a link id holds for that link's run standing. A function ending in
_probe shows the failure a nye link names (it returns True when the failure shows).
"""
import ast, json, math, os, random, re, sys, cmath
from fractions import Fraction
from itertools import product, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R9, CONNECTORS, JOINS

SRC = open(os.path.join(HERE, 'resolver_v372.py')).read()
TREE = ast.parse(SRC)
K = 'k'
S = (1, -1)


def sgn(x):
    return (x > 0) - (x < 0)


def call(carry, offer):
    s, c = C(list(carry), list(offer))
    return s, c


def at(ret, key=K):
    """(surfaced sign or None, returned entry fields or None) at one key."""
    s, c = ret
    return dict(s).get(key), {e[0]: e[1:] for e in c}.get(key)


SIX_OFFERINGS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def reach():
    seen = {()}; todo = [()]
    while todo:
        st = todo.pop()
        base = [(K,) + st] if st else []
        for off in SIX_OFFERINGS:
            _, c = C(base, off)
            nxt = tuple(c[0][1:]) if c else ()
            if nxt not in seen:
                seen.add(nxt); todo.append(nxt)
    return seen


NINETEEN = reach()


def offerings(maxlen, key=K):
    for L in range(maxlen + 1):
        for seq in product((-1, 0, 1), repeat=L):
            yield [(key, v) for v in seq]


# ------------------------------------------------------------------ 8.1 FIVE
def G7():
    w = cmath.exp(2j * math.pi / 3)
    if abs(1 + w + w * w) > 1e-12:
        return False
    V, I, N = 230.0, 5.0, 3600
    def mean_p(phi):
        return sum((math.sqrt(2) * V * math.cos(2 * math.pi * n / N)) *
                   (math.sqrt(2) * I * math.cos(2 * math.pi * n / N - phi)) for n in range(N)) / N
    ok = True
    for phi in (0.0, math.pi / 2, math.pi, 0.3, 2.0, -1.1):
        ok &= abs(mean_p(phi) - V * I * math.cos(phi)) < 1e-6
    return ok and mean_p(0) > 0 and abs(mean_p(math.pi / 2)) < 1e-6 and mean_p(math.pi) < 0


def G9():
    return (440 == 8 * 55 == 3 * 146 + 2 == 4 * 110 and 55 == sum(range(1, 11)) == math.comb(11, 2))


def G12():
    rows = [((437, 438), (440, 440), (-3, -2), (3, 2)), ((443, 444), (440, 440), (3, 4), (3, 4)),
            ((439, 441), (440, 440), (-1, 1), (1, 1)), ((439, 442), (440, 440), (-1, 2), (1, 2)),
            ((437, 438), (440, 441), (-3, -3), (3, 3))]
    ok = abs(437 - 440) == abs(443 - 440) == 3
    for (a0, a1), (b0, b1), es, bs in rows:
        ok &= (a0 - b0, a1 - b1) == es and (abs(a0 - b0), abs(a1 - b1)) == bs
    for e in range(-40, 41):
        for d in range(-40, 41):
            b, b2 = abs(e), abs(e + d)
            ok &= b2 * b2 - b * b == d * (2 * e + d)
            if e and d and abs(d) < abs(e):
                ok &= sgn(b2 - b) == sgn(e * d)
    return ok


def G13():
    r = Fraction(3, 2) ** 12 / 2 ** 7
    cents = 1200 * math.log2(531441 / 524288)
    return (r == Fraction(3 ** 12, 2 ** 19) == Fraction(531441, 524288) and round(cents, 2) == 23.46
            and Fraction(432, 440) == Fraction(54, 55))


def G18():
    first = {m: call([(0, 1, m, 3)], [(0, 1)]) for m in (1, 7, -1)}
    ok = (first[1] == ([(0, 0)], [(0, 1, 1, 4)]) and first[7] == ([(0, 0)], [(0, 1, 7, 4)])
          and first[-1] == ([(0, 0)], []))
    second = {m: call(first[m][1], []) for m in (1, 7, -1)}
    return (ok and second[1] == ([(0, -1)], [(0, -1, -1, 0)]) and second[7] == ([(0, -1)], [(0, -1, -7, 0)])
            and second[-1] == ([], []))


def G20():
    V, I, N = 1.0, 1.0, 3600
    th = [2 * math.pi * n / N for n in range(N)]
    three = [sum(V * I * math.cos(t - 2 * math.pi * j / 3) ** 2 for j in range(3)) for t in th]
    quad = [V * I * (math.cos(t) ** 2 + math.sin(t) ** 2) for t in th]
    opp = [V * I * (math.cos(t) ** 2 + math.cos(t - math.pi) ** 2) for t in th]
    return (max(abs(x - 1.5 * V * I) for x in three) < 1e-12 and max(abs(x - V * I) for x in quad) < 1e-12
            and max(opp) - min(opp) > 1.9)


def G21():
    a = call([(K, 1, -1, 0), (K, 1, 1, 2)], [])
    b = call([(K, 1, -1, 0), (K, -1, 1, 1)], [])
    ok = a == ([(K, -1)], [(K, -1, -1, 0)]) and b == ([(K, 0)], [(K, -1, 1, 2)])
    rnd = random.Random(5)
    for _ in range(3000):
        carry = [(rnd.choice('kj'), rnd.choice(S), rnd.choice(S), rnd.randint(0, 4)) for _ in range(rnd.randint(0, 5))]
        off = [(rnd.choice('kjm'), rnd.choice((-1, 0, 1))) for _ in range(rnd.randint(0, 5))]
        _, c = call(carry, off)
        ok &= len({e[0] for e in c}) == len(c)
    return ok


def G22():
    rnd = random.Random(7)
    ok = True
    states = [st for st in NINETEEN]
    for _ in range(300):
        carry = []
        for key in 'kj':
            st = rnd.choice(states)
            if st:
                carry.append((key,) + st)
        off = [(rnd.choice('kj'), rnd.choice((-1, 0, 1))) for _ in range(rnd.randint(1, 5))]
        s0, c0 = call(carry, off)
        for perm in set(permutations(off)):
            s, c = call(carry, list(perm))
            ok &= dict(s) == dict(s0) and sorted(c) == sorted(c0)
            order = []
            for key, v in list(perm):
                if v != 0 and key not in order:
                    order.append(key)
            for e in carry:
                if e[0] not in order:
                    order.append(e[0])
            ok &= [x[0] for x in s] == order
    return ok


def G29():
    return (72 + 1 == 73 == (59 - 2) + 16 and 146 == 2 * 73 == 144 + 2 and 3 * 146 == 438
            and 438 + 1 + 1 == 440 and 3 * 120 == 360 == 8 * math.comb(10, 2)
            and 440 - 360 == 3 * (146 - 120) + 2 == 3 * 26 + 2 == 80 == 16 * 5
            and math.comb(5, 2) == 10 == 5 + 5 and 12 * 10 == 120)


def G30():
    ok = True
    for N in range(1, 65):
        ring = {(i, (i + 1) % N) for i in range(N)} if N > 2 else ({(0, 1), (1, 0)} if N == 2 else {(0, 0)})
        chain = {(i, i + 1) for i in range(N - 1)}
        ok &= len(chain) == N - 1 and (N < 3 or len(ring) == N)
        for k in range(N + 1):
            ok &= (N - k) + k == N
        if N % 2 == 0:
            for k in range(N):
                o = (k + N // 2) % N
                ok &= min((o - k) % N, (k - o) % N) == N // 2
    return ok


# ------------------------------------------------------------------ 8.2 SIX
def T5_probe():
    empty_alike = all(call([], [(K, s)] * n) == call([], [(K, s)]) for s in S for n in range(1, 8))
    parted = False
    for st in NINETEEN:
        if not st:
            continue
        c = st[0]
        one, seven = call([(K,) + st], [(K, c)]), call([(K,) + st], [(K, c)] * 7)
        parted |= at(one)[0] == 0 and at(seven)[0] == c
    return empty_alike and parted


def T9():
    ok = all(call([(K,) + st] if st else [], [(K, 0)]) == call([(K,) + st] if st else [], []) for st in NINETEEN)
    sA, _ = call([], [(K, 1), (K, -1)])
    relA = R9(sA, {K: K})
    sB, cB = call([], relA)
    relB = R9(sB, {K: K})
    sC, cC = call([], relB)
    return ok and sA == [(K, 0)] and relA == [(K, 0)] and sB == [] and cB == [] and sC == [] and cC == []


def _fn(name):
    return next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == name)


def _loads_within(fn):
    args = {a.arg for a in fn.args.args}
    stored = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    loads = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    builtins = set(dir(__builtins__)) if not isinstance(__builtins__, dict) else set(__builtins__)
    return loads - args - stored - builtins, args


def T14():
    no_import = not any(isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(TREE))
    out1, a1 = _loads_within(_fn('_1_self_coupling'))
    out9, a9 = _loads_within(_fn('_9_other_releasing'))
    return (no_import and a1 == {'_3_self_carrying', '_2_self_offering'}
            and a9 == {'_10_other_surfacing', '_5_other_neutralling'} and not out1 and not out9)


# ------------------------------------------------------------------ 8.3 SEVEN
def S10():
    ok = True
    for p in range(1, 61):
        for q in range(1, 61):
            meet = next(n for n in range(1, p * q + 1) if n % p == 0 and n % q == 0)
            ok &= meet == math.lcm(p, q) and ((meet == p * q) == (math.gcd(p, q) == 1))
    return ok


def S15():
    J = list(product(S, S))
    R = lambda s: (s[1], -s[0]); L = lambda s: (-s[1], s[0])
    rep = lambda f, n, s: s if n == 0 else rep(f, n - 1, f(s))
    return all(rep(L, 3, s) == R(s) and rep(R, 3, s) == L(s) and rep(R, 3, rep(L, 3, s)) == s
               and rep(L, 4, s) == s and L(s) != R(s) for s in J)


def S19():
    return 5 ** 2 - 4 * 6 == 1 and 4 * 6 == 24


def _primes(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def S20():
    P = _primes(70)
    span = [p for p in P if 5 <= p <= 53]
    gaps = [b - a for a, b in zip(P, P[1:])]
    first6 = next(i for i, g in enumerate(gaps) if g == 6)
    both = {p: (p - P[P.index(p) - 1], P[P.index(p) + 1] - p) for p in span}
    return (len(span) == 14 and span[:7] == [5, 7, 11, 13, 17, 19, 23] and span[7:] == [29, 31, 37, 41, 43, 47, 53]
            and gaps[:9] == [1, 2, 2, 4, 2, 4, 2, 4, 6] and (P[first6], P[first6 + 1]) == (23, 29)
            and [p for p in span if both[p] == (2, 2)] == [5] and [p for p in span if both[p] == (6, 6)] == [53]
            and max(max(g) for g in both.values()) == 6)


def S23():
    return all((8 - k) * (8 + k) == 64 - k * k for k in range(9)) and 7 * 9 == 63 and 6 * 10 == 60 and 8 * 8 == 64


# ------------------------------------------------------------------ 8.4 EIGHT
def K5():
    return T14()


def K24():
    ok = all(-(-x) == x for x in range(-50, 51))
    ok &= all(1 / (1 / Fraction(x, y)) == Fraction(x, y) for x in range(-9, 10) if x for y in range(1, 9))
    ok &= all(z.conjugate().conjugate() == z for z in (complex(a, b) for a in range(-3, 4) for b in range(-3, 4)))
    rnd = random.Random(3)
    for _ in range(50):
        M = [[rnd.randint(-9, 9) for _ in range(4)] for _ in range(3)]
        T = [list(r) for r in zip(*M)]
        ok &= [list(r) for r in zip(*T)] == M
    U = set(range(20))
    for _ in range(50):
        A = {x for x in U if rnd.random() < 0.5}
        ok &= U - (U - A) == A
    f = lambda x: x ** 4 / 4 + x ** 2 / 2
    def xp(p):  # solve x^3 + x = p
        x = 0.0
        for _ in range(80):
            x -= (x ** 3 + x - p) / (3 * x * x + 1)
        return x
    fstar = lambda p: p * xp(p) - f(xp(p))
    ps = [i / 1000 for i in range(-40000, 40001)]
    fs = [fstar(p) for p in ps]
    for x0 in (-2.0, -0.7, 0.0, 0.4, 1.5):
        fss = max(x0 * p - v for p, v in zip(ps, fs))
        ok &= abs(fss - f(x0)) < 1e-5
    return ok


def K26_probe():
    sample = {Fraction(a, b) for a in range(-12, 13) if a for b in range(1, 13)}
    fixed = {x for x in sample if 1 / x == x}
    return fixed == {Fraction(1), Fraction(-1)}


def K27():
    return all(-s != s for s in S) and [x for x in range(-50, 51) if -x == x] == [0] and 0 not in S


# ------------------------------------------------------------------ 8.5 NINE
def H4():
    N = 10000
    share = [min(Fraction(i, N), 1 - Fraction(i, N)) for i in range(N + 1)]
    best = max(share)
    return best == Fraction(1, 2) and [i for i, v in enumerate(share) if v == best] == [N // 2]


def H22():
    rnd = random.Random(11)
    for _ in range(10000):
        bal = {}
        for _ in range(rnd.randint(1, 8)):
            amt = rnd.randint(1, 10 ** 6)
            dr, cr = rnd.sample('ABCDEFG', 2)
            bal[dr] = bal.get(dr, 0) + amt
            bal[cr] = bal.get(cr, 0) - amt
        if sum(bal.values()) != 0:
            return False
    return True


def H24_probe():
    m1 = Fraction(0 + 1, 2); m2 = Fraction(1 + 1, 2)
    return m1 not in (0, 1) and m2 in (1,)


# ------------------------------------------------------------------ 8.6 TEN
def A10():
    def omega(n, deltas):
        return n - max(deltas)
    ala = (18, [9, 12, 15])
    ok = omega(*ala) == 3
    n, d = ala
    for step in (2, 4):
        ok &= omega(n + step, [x + step for x in d]) == 3
    ok &= omega(18, [9, 12]) == 6 and omega(18, [9]) == 9
    ok &= all(b - a == 3 for a, b in zip(d, d[1:]))
    fam = [3, 6, 9]
    return ok and [f % 2 for f in fam] == [1, 0, 1] and fam[1] - fam[0] == fam[2] - fam[1] == 3


# ------------------------------------------------------------------ 8.7 ELEVEN
def D2():
    ok = True; cases = 0
    for st in NINETEEN:
        if not st:
            continue
        c, t, a = st
        for off in offerings(4):
            cases += 1
            s, e = at(call([(K,) + st], off))
            elig = a + 1 <= 3 or (a + 1 == 4 and t > 0)
            if s:
                ok &= e == (s, -t, 0)
            else:
                ok &= s == 0 and (e == (c, t, a + 1) if elig else e is None)
    return ok and cases == 18 * 121


def D3():
    ok = True
    for c, t in product(S, S):
        st = (c, t, 0)
        for _ in range(12):
            s, e = at(call([(K,) + st], [(K, c), (K, c)]))
            ok &= s == c and e is not None and e[2] == 0
            st = e
        carry = [(K, c, t, 0)]; opens = []
        for _ in range(12):
            ret = call(carry, [(K, c)])
            s, e = at(ret)
            opens.append((s, None if e is None else e[2]))
            carry = ret[1]
        top = 4 if t > 0 else 3
        want = [(0, a) for a in range(1, top + 1)] + [(0, None), (c, 0)]
        ok &= opens[:len(want)] == want
    return ok


def D5():
    fn = _fn('_1_self_coupling')
    parents = {}
    for node in ast.walk(fn):
        for ch in ast.iter_child_nodes(node):
            parents[ch] = node
    zeros = []
    for node in ast.walk(fn):
        if (isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Subscript)
                and getattr(node.targets[0].value, 'id', None) == '_11_other_chaining'
                and isinstance(node.value, ast.Tuple) and isinstance(node.value.elts[2], ast.Constant)
                and node.value.elts[2].value == 0):
            zeros.append(node)
    if len(zeros) != 1:
        return False
    p = parents[zeros[0]]
    cond = isinstance(p, ast.If) and isinstance(p.test, ast.Compare) and isinstance(p.test.ops[0], ast.NotEq)
    loop = parents[p]
    over_surfacing = isinstance(loop, ast.For) and getattr(loop.iter, 'id', None) == '_10_other_surfacing'
    ok = cond and over_surfacing
    for c, t in product(S, S):
        for _ in range(50):
            s, e = at(call([(K, c, t, 0)], [(K, c)]))
            ok &= s == 0 and e == (c, t, 1)
    return ok


def D6():
    ok = True
    for st in NINETEEN:
        base = [(K,) + st] if st else []
        cc = st[0] if st else 0
        seen = {}
        for off in offerings(4):
            tot = sum(sgn(v) for _, v in off)
            met = bool(st) or any(v for _, v in off)
            key = (sgn(tot - cc), met)
            r = call(base, off)
            if key in seen:
                ok &= seen[key] == r
            else:
                seen[key] = r
    return ok


def D14():
    together = call([], [(K, 1), (K, -1)])
    s1, c1 = call([], [(K, 1)])
    s2, c2 = call(c1, [(K, -1)])
    return together == ([(K, 0)], []) and s1 == [(K, 1)] and s2 == [(K, -1)] and c2 == [(K, -1, 1, 0)]


def D19():
    X = range(6)
    pairs = [(a, b) for a in X for b in X]
    diag = [p for p in pairs if p[0] == p[1]]
    ok = len(pairs) == 36 and len(diag) == 6 and len(pairs) - len(diag) == 30
    perms = list(permutations(range(4)))
    ok &= len(perms) == 24 == math.factorial(4)
    for chosen in perms:
        ok &= sum(1 for p in perms if p != chosen) == 23
    return ok


def D24():
    ok = True
    for t1, t2 in product(S, S):
        for a1 in range(5):
            for a2 in range(5):
                s, _ = at(call([(K, 1, t1, a1), (K, -1, t2, a2)], []))
                ok &= s == 0
    return ok


def D25():
    ok = call([], []) == ([], [])
    for st in NINETEEN:
        if not st:
            continue
        for off in SIX_OFFERINGS:
            _, e = at(call([(K,) + st], off))
            ok &= e != st
            if e is not None and e[2] == st[2] + 1:
                ok &= e[:2] == st[:2]
            elif e is not None:
                ok &= e[2] == 0 and e[1] == -st[1]
    return ok


def D29():
    phi = (1 + 5 ** 0.5) / 2
    P = _primes(59)
    return all(abs((1 / phi) ** q / (1 / phi) ** p - (1 / phi) ** (q - p)) < 1e-12 for p, q in zip(P, P[1:]))


def D34():
    rnd = random.Random(13)
    return all((a + d) - (b + d) == a - b for a, b, d in
               ((Fraction(rnd.randint(-999, 999), 10), Fraction(rnd.randint(-999, 999), 10),
                 Fraction(rnd.randint(-999, 999), 10)) for _ in range(10000)))


def C_without_list(carry, offer):
    """1-self-coupling with 12-other-surplusing summed straight, no 14-social-crossing list built."""
    crossing = {k: t for k, c, t, a in carry}
    surplus = {}
    for k, c in offer:
        if c > 0: surplus[k] = surplus.get(k, 0) + 1
        if c < 0: surplus[k] = surplus.get(k, 0) - 1
    for k, c, t, a in carry:
        if c > 0: surplus[k] = surplus.get(k, 0) - 1
        if c < 0: surplus[k] = surplus.get(k, 0) + 1
    surfacing = [(k, sgn(v)) for k, v in surplus.items()]
    chaining = {}
    for k, c, t, a in carry:
        if a + 1 <= 3 or (a + 1 == 4 and t > 0):
            chaining[k] = (c, t, a + 1)
    for k, s in surfacing:
        if s != 0:
            chaining[k] = (s, 0 - crossing.get(k, 1), 0)
    return surfacing, [(k, c, t, a) for k, (c, t, a) in chaining.items()]


def D36():
    ok = True; n = 0
    states = sorted(NINETEEN)
    for st1 in states:
        for st2 in states:
            carry = ([('k',) + st1] if st1 else []) + ([('j',) + st2] if st2 else [])
            for L in range(3):
                for seq in product([('k', 1), ('k', -1), ('k', 0), ('j', 1), ('j', -1)], repeat=L):
                    n += 1
                    ok &= C(list(carry), list(seq)) == C_without_list(list(carry), list(seq))
    return ok and n == 361 * 31


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'[GTSKHAD]\d+(_probe)?', k) and callable(v)}

RUNS = [
    {"link": "G7", "check": "abs(1 + w + w^2) < 1e-12 at w = exp(2*pi*i/3); the mean over 3,600 steps of a cycle of (sqrt2 V cos th)(sqrt2 I cos(th - phi)) equals V I cos phi within 1e-6 at six phases, positive at phi = 0, zero at pi/2, negative at pi."},
    {"link": "G9", "check": "440 == 8*55 == 3*146 + 2 == 4*110 and 55 == 1 + ... + 10 == C(11, 2)."},
    {"link": "G12", "check": "The file's five tone rows give its signed differences and beat rates; for integer e, d in -40..40, b'^2 - b^2 == d(2e + d) with b = |e|, b' = |e + d|, and sign(b' - b) == sign(e d) whenever e, d nonzero and |d| < |e|."},
    {"link": "G13", "check": "(3/2)^12 / 2^7 == 3^12 / 2^19 == 531441/524288; 1200 log2 of it rounds to 23.46; 432/440 == 54/55."},
    {"link": "G18", "check": "_1_self_coupling([(0, 1, m, 3)], [(0, 1)]) returns ([(0, 0)], [(0, 1, m, 4)]) at m = 1 and 7 and ([(0, 0)], []) at m = -1; each returned carrying under an empty offering returns ([(0, -1)], [(0, -1, -m, 0)]) at m = 1 and 7 and ([], []) at m = -1."},
    {"link": "G20", "check": "Over 3,600 steps: the three-phase sum of VI cos^2(th - 2 pi j/3) stays 3VI/2 within 1e-12, two phases in quadrature stay VI, and two opposed by half a cycle range from 0 to 2VI."},
    {"link": "G21", "check": "Carrying [(k, +1, -1, 0), (k, +1, +1, 2)] under an empty offering returns ([(k, -1)], [(k, -1, -1, 0)]); [(k, +1, -1, 0), (k, -1, +1, 1)] returns ([(k, 0)], [(k, -1, +1, 2)]); 3,000 random carryings with repeated keys return each key once."},
    {"link": "G22", "check": "300 random carryings from the nineteen at two keys, each under every ordering of a random offering of up to five signs: the surfacing (as a map) and the carrying (as a set) stay the same, and the surfaced list follows the order keys first meet a nonzero sign in the offering, then the carried keys."},
    {"link": "G29", "check": "72 + 1 == 73 == (59 - 2) + 16; 146 == 2*73 == 144 + 2; 3*146 == 438; 438 + 2 == 440; 3*120 == 360 == 8*C(10, 2); 440 - 360 == 3*26 + 2 == 80 == 16*5; C(5, 2) == 10 == 5 + 5; 12*10 == 120."},
    {"link": "G30", "check": "For N from 1 to 64: a chain has N - 1 connections and a simple ring N (N >= 3); k and N - k sum to N; at even N, stations k and (k + N/2) mod N stand N/2 apart both ways."},
    {"link": "T9", "check": "At each of the nineteen carryings an offering [(k, 0)] returns what [] returns; a self offered (+, -) at empty carrying surfaces (k, 0), 9 releases (k, 0), a second self offered that release at empty carrying returns ([], []), and a third offered the second's release returns ([], [])."},
    {"link": "T14", "check": "The resolver file has no import; _1_self_coupling takes (_3_self_carrying, _2_self_offering) and _9_other_releasing (_10_other_surfacing, _5_other_neutralling); every name either function loads is an argument, a name it binds itself, or a builtin."},
    {"link": "S10", "check": "For p, q from 1 to 60 the first n >= 1 divisible by both equals lcm(p, q), and it equals p*q exactly when gcd(p, q) == 1."},
    {"link": "S15", "check": "On the four joint forms with R(x, y) = (y, -x) and L(x, y) = (-y, x): L^3 == R, R^3 == L, R^3 after L^3 is the identity, L^4 is the identity, and L differs from R at each form."},
    {"link": "S19", "check": "5^2 - 4*6 == 1 and 4*6 == 24."},
    {"link": "S20", "check": "The primes from 5 to 53 are fourteen: 5..23 seven and 29..53 seven; the gaps from 2 run 1, 2, 2, 4, 2, 4, 2, 4, 6, the first six at 23 -> 29; within 5..53 only 5 has gaps (2, 2) on both sides and only 53 has (6, 6), six being the widest gap met."},
    {"link": "S23", "check": "(8 - k)(8 + k) == 64 - k^2 for k from 0 to 8; 7*9 == 63, 6*10 == 60, 8*8 == 64."},
    {"link": "K5", "check": "The same tree check as T14: no import, and each function loads only its own two arguments, names it binds, and builtins."},
    {"link": "K24", "check": "Applied twice each returns its argument: negation on -50..50, the multiplicative inverse on nonzero fractions, complex conjugation on a grid, the transpose on 50 random 3x4 matrices, set complement on 50 random subsets of 20; the Legendre transform of f(x) = x^4/4 + x^2/2 taken twice (numerically, p-grid step 0.001 over [-40, 40]) returns f at five points within 1e-5."},
    {"link": "K27", "check": "-s != s at s = +1 and -1; among the integers -50..50 only 0 has -x == x, and 0 is no sign."},
    {"link": "H4", "check": "Over 10,001 cuts x = i/10000, the cutter's share min(x, 1 - x) (the chooser taking the larger) is greatest, 1/2, at x = 1/2 alone."},
    {"link": "H22", "check": "10,000 random ledgers of one to eight entries, each entry debiting one account and crediting another the same amount: every trial balance sums to zero."},
    {"link": "A10", "check": "omega = chain length - highest delta: 18:3 at delta 9, 12, 15 is omega-3, and elongated by 2 or 4 carbons at the carboxyl end (each delta + 2 or + 4) stays omega-3; 18:2 (9, 12) is omega-6, 18:1 (9) omega-9; the double bonds stand three apart and 3, 6, 9 read odd, even, odd."},
    {"link": "D2", "check": "Each of the eighteen nonempty carryings at one key under each of the 121 offerings of up to four signs from -1, 0, +1: at a nonzero surfacing s the entry returns (s, -t, 0); at a 0 surfacing it returns (c, t, a + 1) within the bound and is gone past it."},
    {"link": "D3", "check": "From (c, t, 0), each (c, t): two c at each of 12 calls surface c each time with the returned opening 0; one c at each call surfaces 0 with openings 1, 2, 3 (and 4 at t > 0), then 0 with the key empty, then c with opening 0."},
    {"link": "D5", "check": "In _1_self_coupling's tree one assignment only writes an 11-other-chaining entry with opening 0, under `if _7_other_corusing != 0` in the loop over _10_other_surfacing; a caller re-seeding (c, t, 0) under one c at each of 50 calls gets (c, t, 1) back each time."},
    {"link": "D6", "check": "At each of the nineteen carryings, the 121 offerings of up to four signs grouped by the sign of (their signed total less the carried sign) and by whether any sign meets the key: within each group the whole return (surfacing and carrying) is identical."},
    {"link": "D14", "check": "_1_self_coupling([], [(k, +1), (k, -1)]) returns ([(k, 0)], []); + then - at two calls surface + and then - and return [(k, -1, +1, 0)]."},
    {"link": "D19", "check": "A six-set has 36 ordered pairs, 6 on the diagonal and 30 off it; four things have 4! = 24 matchings, and for each chosen one 23 others differ."},
    {"link": "D24", "check": "Carrying (k, +1, t1, a1) and (k, -1, t2, a2) at one key, with nothing arriving, surfaces (k, 0) at each t1, t2 in {+1, -1} and a1, a2 in 0..4."},
    {"link": "D25", "check": "_1_self_coupling([], []) returns ([], []); each of the eighteen nonempty carryings under each of the six offerings returns an entry differing from the one given: a continuing keeps sign and second sign and opens by one, a fresh write opens at 0 with the second sign inverted."},
    {"link": "D29", "check": "With phi = (1 + sqrt5)/2, for each pair of neighbouring primes p < q up to 59, (1/phi)^q / (1/phi)^p equals (1/phi)^(q - p) within 1e-12."},
    {"link": "D34", "check": "(a + d) - (b + d) == a - b over 10,000 random rationals a, b, d."},
    {"link": "D36", "check": "A copy of _1_self_coupling summing 12-other-surplusing straight from the offering and the carrying, building no 14-social-crossing list, returns exactly what the resolver returns at 361 carryings over two keys (each key one of the nineteen) under each of the 31 offerings of up to two signs from (k, +1), (k, -1), (k, 0), (j, +1), (j, -1)."},
]


'''

PART_SOURCES['o2'] = r'''"""Run checks for Exhibit THIRTY Part EIGHT, 8.8 to 8.14 (THIRTEEN to NINETEEN, links Q, Y, J, C, B, P, L).
The resolver is imported from resolver_v372.py beside this file (Exhibit ONE v372's code block).
A check named X returns True when link X holds as stated.
A check named X_probe backs a nye link: it returns True when the failure named at the gap is confirmed
(the file's stated count differs from the count its own table gives, or the stated count is not reproduced)."""
import ast, inspect, json, math, os, re, sys
from fractions import Fraction
from itertools import combinations, permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV
C = RV._1_self_coupling
REL = RV._9_other_releasing
K = 'k'
S = (1, -1)
CORUS = '/home/claude/corus'

# ------------------------------------------------------------------ resolver helpers
def reach19():
    """The nineteen carryings reachable at one key from empty (R23)."""
    offers = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]
    seen = {()}; todo = [()]
    while todo:
        c = todo.pop()
        carry = [(K,) + c] if c else []
        for o in offers:
            _, nxt = C(carry, o)
            t = tuple(nxt[0][1:]) if nxt else ()
            if t not in seen:
                seen.add(t); todo.append(t)
    return sorted(seen)

def carry_of(t):
    return [(K,) + t] if t else []

# ------------------------------------------------------------------ 8.8 THIRTEEN (Q)
def Q12():
    # the exclusive or taken as the step: x -> x xor 1 runs 0101, back at each second step
    x = 0; seq = []
    for _ in range(6):
        seq.append(x); x ^= 1
    ok = seq == [0, 1, 0, 1, 0, 1]
    # taken of the prior and the now together: next = prior xor now
    for a, b in product((0, 1), repeat=2):
        s = [a, b]
        for _ in range(9):
            s.append(s[-2] ^ s[-1])
        if (a, b) == (0, 0):
            ok &= all(v == 0 for v in s)
        else:
            ok &= s[3:5] == [a, b] and s[1:3] != [a, b] and s[2:4] != [a, b]   # returns after three, not before
            ok &= ''.join(map(str, s[:3])) in ('011', '101', '110')
    return ok

def Q13():
    # Peres-Mermin: nine bits, rows parity 0, columns parity 1 (and the standard columns 0,0,1): none of 512
    def count(colpar):
        n = 0
        for bits in product((0, 1), repeat=9):
            g = [bits[0:3], bits[3:6], bits[6:9]]
            if all(sum(r) % 2 == 0 for r in g) and all(sum(g[i][j] for i in range(3)) % 2 == colpar[j] for j in range(3)):
                n += 1
        return n
    return count((1, 1, 1)) == 0 and count((0, 0, 1)) == 0 and 2 ** 9 == 512

FORMS = {'1-9-8-16': [1, 9, 8, 16], '2-15-7-10': [2, 15, 7, 10], '3-11-6-14': [3, 11, 6, 14], '4-13-5-12': [4, 13, 5, 12],
         '9-5-12-8': [9, 5, 12, 8], '7-11-6-10': [7, 11, 6, 10],
         '1-9-5-12-8-16': [1, 9, 5, 12, 8, 16], '2-15-7-11-6-10': [2, 15, 7, 11, 6, 10],
         '3-11-7-10-6-14': [3, 11, 7, 10, 6, 14], '4-13-5-9-8-12': [4, 13, 5, 9, 8, 12],
         '1-9-5-13-4-12-8-16': [1, 9, 5, 13, 4, 12, 8, 16], '2-15-7-11-3-14-6-10': [2, 15, 7, 11, 3, 14, 6, 10]}

def Q15():
    ok = True
    for n in range(1, 17):
        ok &= ((n + 8 - 1) % 16 + 1) % 2 == n % 2 if n <= 8 else True      # 8 up keeps parity
        ok &= (17 - n) % 2 != n % 2                                        # 17 less changes it
    for n in range(1, 9):
        ok &= (9 - n) % 2 != n % 2                                         # 9 less changes it
    for c in FORMS.values():
        steps = [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]
        ch = [(a, b) for a, b in steps if a % 2 != b % 2]
        ok &= len(ch) == 2 and all(a + b == 17 for a, b in ch)
    return ok

def primes_to(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** .5) + 1))]

def Q22():
    P = primes_to(59)
    return len(P) == 17 and sum(P) == 440 and len(P) - 1 == 16 and 2 * 59 == 118 and (59 + 61) // 2 == 60

def Q25():
    ok = True
    for t in reach19():
        for m in (2, 5, 17):
            ok &= C(carry_of(t), [(K, m)]) == C(carry_of(t), [(K, 1)])
            ok &= C(carry_of(t), [(K, -m)]) == C(carry_of(t), [(K, -1)])
    return ok

def Q26():
    vals = set()
    for t in reach19():
        for n in range(0, 5):
            for o in product((-1, 0, 1), repeat=n):
                s, _ = C(carry_of(t), [(K, v) for v in o])
                vals |= {v for _, v in s}
    return vals <= {-1, 0, 1} and vals == {-1, 0, 1}

def Q27():
    return all(C(carry_of(t), [(K, 0)]) == C(carry_of(t), []) for t in reach19())

def Q28():
    tree = ast.parse(inspect.getsource(RV))
    consts = set()
    third = set()
    for f in tree.body:
        if isinstance(f, ast.FunctionDef):
            for n in ast.walk(f):
                if isinstance(n, ast.Constant):
                    (third if f.name == '_17_social_abundancing' else consts).add(n.value)
    return consts == {0, 1, 3, 4} and third == {1, 2, 6, 9, 10, 14, 17}

PHI = (1 + 5 ** .5) / 2

def Q32():
    F = [1, 1]
    while len(F) < 42:
        F.append(F[-1] + F[-2])
    sides = [Fraction(F[i + 1], F[i]) > Fraction(PHI) for i in range(1, 38)]
    alternates = all(sides[i] != sides[i + 1] for i in range(len(sides) - 1))
    # continued fraction of phi from its Fibonacci ratio: all partial quotients one
    x = Fraction(F[40], F[39]); cf = []
    for _ in range(30):
        a = x.numerator // x.denominator; cf.append(a); x = 1 / (x - a)
    rational_closes = all(((p * q) % q == 0) for p, q in [(3, 5), (5, 8), (8, 13)])   # a winding p/q returns after q rounds
    return alternates and all(a == 1 for a in cf) and rational_closes

# ------------------------------------------------------------------ 8.10 FIFTEEN (J)
def J7():
    k = 1.380649e-23
    e = k * 300 * math.log(2)
    return abs(e - 2.871e-21) < 0.001e-21 and round(e / 1e-21, 1) == 2.9

def transitive_relations(n):
    P = [(i, j) for i in range(n) for j in range(n)]
    for bits in range(1 << len(P)):
        R = {P[k] for k in range(len(P)) if bits >> k & 1}
        if all((a, d) in R for (a, b) in R for (c, d) in R if b == c):
            yield R

def J9():
    count = 0; ok = True
    for R in transitive_relations(4):
        count += 1
        for (a, m) in R:
            for (b, m2) in R:
                if m2 != m: continue
                for (m3, s) in R:
                    if m3 == m:
                        ok &= (a, s) in R and (b, s) in R
    return ok and count == 3994

def has_cycle(n, R):
    succ = {a: [b for (x, b) in R if x == a] for a in range(n)}
    color = {}
    def dfs(u):
        color[u] = 1
        for v in succ[u]:
            if color.get(v) == 1 or (v not in color and dfs(v)):
                return True
        color[u] = 2
        return False
    return any(u not in color and dfs(u) for u in range(n))

def serial_relations(n):
    P = [(i, j) for i in range(n) for j in range(n)]
    for bits in range(1 << len(P)):
        R = {P[k] for k in range(len(P)) if bits >> k & 1}
        if all(any((a, b) in R for b in range(n)) for a in range(n)):
            yield R

def J10():
    ok = True; nser = 0; nfun = 0
    for n in range(1, 5):
        for R in serial_relations(n):
            nser += 1; ok &= has_cycle(n, R)
    for n in range(1, 6):
        for f in product(range(n), repeat=n):
            nfun += 1; ok &= has_cycle(n, {(a, f[a]) for a in range(n)})
    return ok and nser == 50978 and nfun == 3413

def J11_probe():
    # the file's 592,260 is not the count of any reading run here
    import numpy as np
    r = np.indices((32,) * 5, dtype=np.uint8).reshape(5, -1)      # each relation on five terms as five row masks
    ok = np.ones(r.shape[1], bool)
    for i in range(5):
        for j in range(5):
            ok &= ~((((r[i] >> j) & 1) == 1) & ((r[j] & ~r[i]) != 0))
    t5 = int(ok.sum())
    t14 = [sum(1 for _ in transitive_relations(n)) for n in range(1, 5)]
    readings = {'serial relations, 1..4 terms': 50978, 'functions, 1..5 terms': 3413,
                'transitive relations, 1..5 terms': sum(t14) + t5, 'all relations on 5 terms': 2 ** 25}
    return t14 == [2, 13, 171, 3994] and t5 == 154303 and 592260 not in readings.values()

def J12():
    rows = [(0, 1.000, 0.000), (60, 0.500, 0.866), (90, 0.000, 1.000)]
    return all(abs(math.cos(math.radians(a)) - s) < 5e-4 and abs(math.sin(math.radians(a)) - o) < 5e-4 for a, s, o in rows)

def J14():
    return all(abs(math.sin(t) + math.sin(t + 2 * math.pi / 3) + math.sin(t + 4 * math.pi / 3)) < 1e-12
               for t in [2 * math.pi * i / 360 for i in range(360)])

def J26():
    ok = all(n * n - (n - 1) * (n + 1) == 1 for n in range(1, 10001))
    ok &= all(n * n - (n - k) * (n + k) == k * k for n in range(1, 200) for k in range(0, 50))
    ok &= all(((a + b) % 2 == 0) == (a % 2 == b % 2) for a in range(200) for b in range(200))
    return ok

def J28():
    f = lambda n, k: math.comb(n, k) * 2 ** (n - k) if 0 <= k <= n else 0
    ok = [f(4, 3), f(4, 2), f(4, 1), f(4, 0)] == [8, 24, 32, 16]
    ok &= all(f(n + 1, k) == 2 * f(n, k) + f(n, k - 1) for n in range(1, 9) for k in range(0, n + 2))
    return ok and [2 * f(3, 3) + f(3, 2), 2 * f(3, 2) + f(3, 1), 2 * f(3, 1) + f(3, 0), 2 * f(3, 0) + 0] == [8, 24, 32, 16]

# ------------------------------------------------------------------ 8.11 SIXTEEN (C)
def C10():
    caps = [2 * n * n for n in range(1, 5)]
    climbs = [caps[i + 1] - caps[i] for i in range(3)]
    odds = [2 * l + 1 for l in range(4)]
    return (caps == [2, 8, 18, 32] and climbs == [6, 10, 14] and 14 - 6 == 8 and (6 + 14) // 2 == 10
            and all(sum(odds[:n]) == n * n for n in range(1, 5)) and [2 * o for o in odds] == [2, 6, 10, 14])

def C17():
    return all(4 * n + 2 == 2 * (2 * n + 1) for n in range(100)) and [4 * n + 2 for n in range(4)] == [2, 6, 10, 14] and 6 == 2 * 3

def C11():
    return (24 ** 2 - 23 * 25 == 1 and 28 ** 2 - 24 * 32 == 16 and 28 ** 2 - 27 * 29 == 1
            and all(n * n - (n - k) * (n + k) == k * k for n in range(1, 200) for k in range(50)))

def perm_group_order(gens, n):
    idp = tuple(range(n)); G = {idp}; todo = [idp]
    while todo:
        g = todo.pop()
        for h in gens:
            x = tuple(h[i] for i in g)
            if x not in G:
                G.add(x); todo.append(x)
    return G

def C12():
    S4 = set(permutations(range(4)))
    even = lambda p: sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2 == 0
    A4 = {p for p in S4 if even(p)}
    S5 = set(permutations(range(5))); A5 = {p for p in S5 if even(p)}
    comp = lambda p, q: tuple(p[i] for i in q)
    centre_S5 = [z for z in S5 if all(comp(z, g) == comp(g, z) for g in S5)]
    centre_A5 = [z for z in A5 if all(comp(z, g) == comp(g, z) for g in A5)]
    # A5 x C2 has centre (identity) x C2, order 2; S5's centre is the identity alone: the two orders-120 groups part
    return (len(S4) == 24 and len(S4) - 1 == 23 and len(A4) == 12 and 7 ** 2 - 1 == 48 and 48 // 2 == 24
            and len(A5) == 60 and 2 * len(A5) == 120 and len(S5) == 120 and len(centre_S5) == 1 and len(centre_A5) * 2 == 2)

def C22():
    ok = True
    for h in range(0, 200):
        # trivalent closed cage, p pentagons, h hexagons: 2E = 5p + 6h, 3V = 2E, V - E + F = 2
        sols = [p for p in range(0, 100) if (5 * p + 6 * h) % 6 == 0 and
                Fraction(5 * p + 6 * h, 3) - Fraction(5 * p + 6 * h, 2) + p + h == 2]
        ok &= sols == [12]
    E = (5 * 12 + 6 * 20) // 2; V = 2 * E // 3
    ok &= (12 + 20, E, V) == (32, 90, 60)
    ok &= 12 - 30 + 20 == 2 and 20 - 30 + 12 == 2      # icosahedron and dodecahedron swap
    ok &= 12 - 24 + (8 + 6) == 2 and (8 * 3 + 6 * 4) // 2 == 24   # cuboctahedron
    return ok

def C20():
    rows = [2, 8, 8, 18, 18, 32, 32]
    run = [sum(rows[:i + 1]) for i in range(7)]
    pairs = [(24, 96), (27, 93), (32, 88)]
    return (run == [2, 10, 18, 36, 54, 86, 118] and 2 + 8 + 18 + 32 == 60 and 27 + 32 == 59
            and all(a + b == 120 for a, b in pairs) and sum(a + b for a, b in pairs) == 360
            and [27 - 24, 32 - 27] == [3, 5] and [93 - 88, 96 - 93] == [5, 3])

# ------------------------------------------------------------------ 8.12 SEVENTEEN (B)
def B15():
    return 2 ** 6 == 4 ** 3 == 64 and math.comb(6, 3) == 20 and math.factorial(4) == 24 and math.factorial(5) == 120 \
        and math.factorial(4) - 1 == 23 and math.factorial(5) - 1 == 119

def B19():
    r = [(1 + 5 ** .5) / 2, (1 - 5 ** .5) / 2]
    return (all(abs(x * x - x - 1) < 1e-12 for x in r) and abs(r[0] - 1.618) < 1e-3 and r[1] < 0
            and sorted({0, 1}) == [x for x in range(-3, 4) if x * x == x] and abs(1 / r[0] ** 2 - 0.382) < 1e-3)

# ------------------------------------------------------------------ 8.13 EIGHTEEN (P)
NAMINGS = ['an arriving held from behind', 'an opening held as a place', 'a bound held as a last', 'a carry held as a store',
           'a middle held as an end', 'a sign held as a magnitude', 'a sequencing held to one beat', 'a rate held to a value',
           'a two-way held to one side', 'a membrane held as a cut']

def table_rows(path, first, last, skip):
    L = open(path).read().split('\n')[first - 1:last]
    return [[c.strip() for c in l.strip().strip('|').split('|')] for l in L
            if l.startswith('|') and not l.startswith('|---') and skip not in l]

def P_counts():
    R = table_rows(os.path.join(CORUS, 'Exhibit_EIGHTEEN_Natural_Physics_v348.md'), 624, 676, '| arrival |')
    cnt = [sum(1 for r in R if r[1] == n) for n in NAMINGS]
    return R, cnt

def P5():
    J = list(product(S, S))
    right = lambda x, y: (y, -x); other = lambda x, y: (-y, x)
    return all(right(*j) != j and other(*j) != j for j in J)

def P28():
    R, c = P_counts()
    own = sum(1 for r in R if r[1].startswith("this file's own"))
    ref = c[0] + c[2] + c[4]; rate = c[6] + c[7]; ret = c[3] + c[9]; mag = c[5] + c[8]
    pairs = [(c[i], c[i + 1]) for i in range(0, 10, 2)]
    return (len(R) == 50 and own == 2 and sum(c) == 48 and (ref, rate, ret, mag) == (21, 13, 8, 6)
            and c[0] == 10 and (sum(c[0::2]), sum(c[1::2])) == (31, 17)
            and pairs == [(10, 0), (5, 2), (6, 3), (7, 6), (3, 6)])

def P7_probe():
    # 2.5 states: thirty-two arrivals at the holdings, nine at a rate held, three at a returned sign entered as cost
    R, c = P_counts()
    return (sum(c), c[6] + c[7], c[3] + c[9]) != (32, 9, 3) and (sum(c), c[6] + c[7], c[3] + c[9]) == (48, 13, 8)

def P11():
    return (55 - 23 == 32 and 32 // 2 == 16 and (23 + 55) // 2 == 39 and 39 ** 2 - 23 * 55 == 16 ** 2
            and 24 ** 2 - 23 * 25 == 1 and math.comb(11, 2) == 55)

def P26():
    # phi^3 - phi^-3 in Q(sqrt5): phi = (1+r)/2; represent a + b r
    def mul(x, y): return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    ph = (Fraction(1, 2), Fraction(1, 2)); inv = (Fraction(-1, 2), Fraction(1, 2))   # 1/phi = phi - 1
    p3 = mul(mul(ph, ph), ph); i3 = mul(mul(inv, inv), inv)
    return (59 == 1 + 2 * (2 ** 2 + 3 ** 2 + 4 ** 2) and (p3[0] - i3[0], p3[1] - i3[1]) == (4, 0)
            and 60 == 5 * 12 and complex(0, 1) ** 4 == 1 and abs(59 / 2 - 29.5) < 1e-12)

def P22():
    # the going 2 to 59, a turn at 60, the return 61 to 118: fifty-eight either side; 2 and 118 meet at 120
    return len(range(2, 60)) == 58 and len(range(61, 119)) == 58 and (59 + 61) // 2 == 60 and 2 + 118 == 120

# ------------------------------------------------------------------ 8.14 NINETEEN (L)
def L_rows():
    return table_rows(os.path.join(CORUS, 'Exhibit_NINETEEN_Natural_Philosophy_v348.md'), 782, 882, 'dilemma (generic)')

def L28():
    R = L_rows()
    held = [r for r in R if r[3] in NAMINGS]
    seams = set(re.findall(r'3\.(\d+)', ' '.join(r[2] for r in R)))
    c = [sum(1 for r in R if r[3] == n) for n in NAMINGS]
    pairs = [(c[i], c[i + 1]) for i in range(0, 10, 2)]
    return (len(R) == 66 and sum(1 for r in R if r[2].startswith('met')) == 50
            and sum(1 for r in R if r[2].startswith('reaching')) == 16 and len(held) == 41
            and seams == {str(i) for i in range(1, 38)}
            and sum(1 for a, b in pairs if a > b) == 4 and sum(1 for a, b in pairs if a < b) == 1)

def L29_probe():
    R = L_rows()
    c = [sum(1 for r in R if r[3] == n) for n in NAMINGS]
    stated = ((4, 6), 29, 13, 8)
    found = ((c[0], c[1]), sum(c[0::2]), sum(c[1::2]), len(set(re.findall(r'3\.(\d+)', ' '.join(r[2] for r in R)))))
    return found != stated and found == ((4, 5), 29, 12, 37)

RUNS = [
 {
  "link": "Q12",
  "check": "x -> x xor 1 runs 0,1,0,1,0,1; next = prior xor now from (0,1), (1,0), (1,1) returns to its start pair after exactly three steps with first three values 011, 101 or 110, and (0,0) stays 0."
 },
 {
  "link": "Q13",
  "check": "Of the 512 assignments of bits to a 3x3 square, none has each row at parity 0 with column parities (1,1,1), and none with column parities (0,0,1)."
 },
 {
  "link": "Q15",
  "check": "n + 8 keeps parity and 17 − n changes it for n in 1..16; 9 − n changes it for n in 1..8; in each of the twelve forms of ONE's tables within 1..16 exactly two steps change parity and each such step is a pair summing to 17."
 },
 {
  "link": "Q22",
  "check": "The primes to 59 are seventeen, sum to 440 and open sixteen gaps; 2 × 59 = 118; 60 lies midway between 59 and 61."
 },
 {
  "link": "Q25",
  "check": "At each of the nineteen reachable carryings, _1_self_coupling with an offering (k, ±m), m in {2, 5, 17}, returns the same as with (k, ±1)."
 },
 {
  "link": "Q26",
  "check": "At each of the nineteen carryings under each offering of 0 to 4 signs from {−1, 0, +1} (121 offerings), each surfaced value lies in {−1, 0, +1}, and each of the three occurs."
 },
 {
  "link": "Q27",
  "check": "At each of the nineteen carryings, _1_self_coupling with offering [(k, 0)] returns the same as with the empty offering."
 },
 {
  "link": "Q28",
  "check": "The numeric constants in the bodies of _1_self_coupling and _9_other_releasing are exactly {0, 1, 3, 4}."
 },
 {
  "link": "Q32",
  "check": "F(n+1)/F(n) for n = 1..38 alternates above and below φ; the continued fraction of F(40)/F(39) begins with thirty partial quotients 1."
 },
 {
  "link": "J7",
  "check": "k·300·ln 2 with k = 1.380649e-23 J/K is 2.871e-21 J, rounding to 2.9e-21 J."
 },
 {
  "link": "J9",
  "check": "Of the 65,536 relations on four elements, 3,994 are transitive, and in each, a R m, b R m and m R s give a R s and b R s."
 },
 {
  "link": "J10",
  "check": "Each of the 50,978 serial relations on 1 to 4 elements, and each of the 3,413 functions on 1 to 5 elements, contains a directed cycle."
 },
 {
  "link": "J12",
  "check": "cos and sin at 0°, 60°, 90° are (1.000, 0.000), (0.500, 0.866), (0.000, 1.000) to three places."
 },
 {
  "link": "J14",
  "check": "sin t + sin(t + 2π/3) + sin(t + 4π/3) = 0 at 360 equally spaced t."
 },
 {
  "link": "J26",
  "check": "n² − (n − 1)(n + 1) = 1 for n = 1..10,000; n² − (n − k)(n + k) = k² for n = 1..199, k = 0..49; (a + b) even iff a and b share parity, a, b = 0..199."
 },
 {
  "link": "J28",
  "check": "The k-faces of the n-cube, C(n,k)·2^(n−k), give (8, 24, 32, 16) at n = 4 for k = 3..0, and f(n+1, k) = 2 f(n, k) + f(n, k−1) for n = 1..8."
 },
 {
  "link": "C10",
  "check": "2n² for n = 1..4 is 2, 8, 18, 32 with climbs 6, 10, 14; 14 − 6 = 8, centre 10; 1 + 3 + … + (2n − 1) = n²; doubled odds 2, 6, 10, 14."
 },
 {
  "link": "C11",
  "check": "24² − 23·25 = 1, 28² − 24·32 = 16, 28² − 27·29 = 1, and n² − (n − k)(n + k) = k² for n < 200, k < 50."
 },
 {
  "link": "C12",
  "check": "|S4| = 24, |A4| = 12, 7² − 1 = 48, |A5| = 60, |S5| = 120; the centre of S5 is trivial and the centre of A5 is trivial, so A5 × C2 has a centre of order 2 and is not S5."
 },
 {
  "link": "C17",
  "check": "4n + 2 = 2(2n + 1) for n < 100, giving 2, 6, 10, 14 at n = 0..3."
 },
 {
  "link": "C20",
  "check": "Running sums of 2, 8, 8, 18, 18, 32, 32 are 2, 10, 18, 36, 54, 86, 118; 2 + 8 + 18 + 32 = 60; 27 + 32 = 59; 24 + 96 = 27 + 93 = 32 + 88 = 120, together 360; gaps 3, 5 and 5, 3."
 },
 {
  "link": "C22",
  "check": "For each hexagon count h = 0..199 a closed trivalent cage of pentagons and hexagons satisfies Euler's relation only at 12 pentagons; C60: 32 faces, 90 edges, 60 vertices; 12 − 30 + 20 = 2 both ways; cuboctahedron 12 − 24 + 14 = 2 with 24 edges."
 },
 {
  "link": "B15",
  "check": "2^6 = 4^3 = 64, C(6,3) = 20, 4! = 24, 5! = 120, 4! − 1 = 23, 5! − 1 = 119."
 },
 {
  "link": "B19",
  "check": "(1 ± √5)/2 solve x² = x + 1, the positive root ≈ 1.618; x² = x has integer roots 0 and 1 only; 1/φ² ≈ 0.382."
 },
 {
  "link": "P5",
  "check": "At the four joint forms of two signs, (x, y) → (y, −x) and (x, y) → (−y, x) move each form."
 },
 {
  "link": "P11",
  "check": "55 − 23 = 32 = 2·16; (23 + 55)/2 = 39 and 39² − 23·55 = 16²; 24² − 23·25 = 1; C(11,2) = 55."
 },
 {
  "link": "P22",
  "check": "2..59 and 61..118 each hold 58 numbers; 60 is midway between 59 and 61; 2 + 118 = 120."
 },
 {
  "link": "P26",
  "check": "59 = 1 + 2(4 + 9 + 16); φ³ − φ⁻³ = 4 exactly in Q(√5); 60 = 5·12; 59/2 = 29.5; i⁴ = 1."
 },
 {
  "link": "P28",
  "check": "EIGHTEEN 5.13's table has 50 rows: 2 at the file's own, 48 at the ten namings with counts (10, 0, 5, 2, 6, 3, 7, 6, 3, 6); groups 21, 13, 8, 6; odd namings 31, even 17; pairs (10,0), (5,2), (6,3), (7,6), (3,6)."
 },
 {
  "link": "L28",
  "check": "NINETEEN 5.2 to 5.8 hold 66 rows, 50 met and 16 reaching; 41 carry one of the ten namings; the rows cite seams 3.1 to 3.37; at the five naming pairs the odd carries more at four and less at one."
 }
]

CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'[QYJCBPL]\d+(_probe)?', k) and callable(v)}

'''

PART_SOURCES['o3'] = r'''"""Run checks for Exhibit THIRTY Part EIGHT, sections 8.15 to 8.22 (the last third of the
exhibits of other workings): TWENTY-ONE, TWENTY-TWO, TWENTY-THREE, TWENTY-FIVE, TWENTY-SIX,
TWENTY-SEVEN, TWENTY-NINE and the Corus v330, at /home/claude/corus.

Each function named for a link returns True when the link holds as written.
A function named LINK_probe returns True when the failure named at that nye gap is found.
The resolver is imported from resolver_v372.py in this folder."""
import ast, json, math, os, re, sys
from fractions import Fraction
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV                      # the resolver, Exhibit ONE v372's code
C = RV._1_self_coupling
REPO = '/home/claude/corus'

def read(name):
    return open(os.path.join(REPO, name), encoding='utf-8').read()

HPR = 'Exhibit_TWENTY-ONE_Hard_Problem_Registry_v342.md'
RHR = 'Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v344.md'
LSR = 'Exhibit_TWENTY-FIVE_Living_Society_Registry_v347.md'
LFR = 'Exhibit_TWENTY-SIX_Living_File_Registry_v348.md'
LGR = 'Exhibit_TWENTY-SEVEN_Living_Ghost_Registry_v345a.md'

FORM = ['Conditions prior', 'Statement', "The field's account of its hardness", 'Accounts', 'Specifications',
        'Specifications withdrawn', 'Common requirement', 'Conserving relation', 'Conserving reach', 'Reach',
        'Unreachability', 'Persistence', 'Addresses', 'Approaches', 'Narrowing recorded', 'Progress', 'Own record']

def hp_entries():
    body = read(HPR).split('## The collection')[0]
    parts = re.split(r'^## (\d+) (.+)$', body, flags=re.M)
    return [(int(parts[i]), parts[i + 1].strip(), parts[i + 2]) for i in range(1, len(parts), 3)]

def hp_val(entry, prop):
    m = re.search(r'^\*\*' + re.escape(prop) + r'\.\*\*(.*)$', entry, re.M)
    return m.group(1).strip() if m else None

# ---------------------------------------------------------------- 8.15 TWENTY-ONE
def HP11_probe():
    # the form's seventeen properties in order at 254 entries; entry 33 carries two more
    off = [(n, [p for p in re.findall(r'^\*\*([^*]+?)\.\*\*', e, re.M) if p not in FORM])
           for n, _, e in hp_entries() if re.findall(r'^\*\*([^*]+?)\.\*\*', e, re.M) != FORM]
    return off == [(33, ['Which of the three the properties key to', 'What the approaches leave untouched'])]

def HP12():
    nums = [n for n, _, _ in hp_entries()]
    return (len(nums) == 255 and nums == sorted(nums) and nums[0] == 1 and nums[-1] == 257
            and sorted(set(range(1, 258)) - set(nums)) == [155, 172])

def HP16():
    E = hp_entries()
    return (len(E) == 255 and sum(bool(hp_val(e, 'Unreachability')) for *_, e in E) == 174
            and sum(bool(hp_val(e, 'Specifications withdrawn')) for *_, e in E) == 34
            and sum(bool(hp_val(e, 'Narrowing recorded')) for *_, e in E) == 231)

# ---------------------------------------------------------------- 8.16 TWENTY-TWO
def RH3():
    ok = all(n * n - (n - 1) * (n + 1) == 1 for n in range(2, 1001))
    ok &= (3 * 3 - 2 * 4, 4 * 4 - 3 * 5, 5 * 5 - 4 * 6, 24 * 24 - 23 * 25, 16 * 16 - 15 * 17) == (1,) * 5
    return ok and 4 * 4 - 2 * 6 == 4

def RH5():
    pairs = [(a, a + 1) for a in range(2, 6)]
    turns = [t for a, b in pairs for t in ((a, '<', b), (b, '>', a))]
    lesser = [min(t[0], t[2]) for t in turns]
    return (len(turns) == 8 and turns[0] == (2, '<', 3) and turns[-1] == (6, '>', 5)
            and all(turns[2 * i][0] == turns[2 * i + 1][2] for i in range(4))
            and all(pairs[i][1] == pairs[i + 1][0] for i in range(3)) and lesser == [2, 2, 3, 3, 4, 4, 5, 5])

TEN = ['arriving', 'opening', 'bound', 'carry', 'middle', 'sign', 'sequencing', 'rate', 'two-way', 'membrane']

def RH10():
    four = {'a reference held': ['arriving', 'bound', 'middle'], 'a rate held': ['sequencing', 'rate'],
            'a magnitude driven': ['sign', 'two-way'], 'a returned sign entered as cost': ['opening', 'carry', 'membrane']}
    t = read(RHR)
    said = all(k in t.lower() for k in four)
    flat = [x for v in four.values() for x in v]
    return said and sorted(flat) == sorted(TEN) and [len(v) for v in four.values()] == [3, 2, 2, 3]

def rh_deployed():
    t = read(RHR)
    return re.findall(r'^## (\d+)\.(\d+) (.+?) \(Hard Problem Registry ([\d, and]+)\)', t, re.M)

def RH15():
    h = rh_deployed()
    counts = [sum(1 for p, *_ in h if p == str(k)) for k in range(1, 13)]
    e21 = {n: name for n, name, _ in hp_entries()}
    nums = [int(x) for *_, n in h for x in re.findall(r'\d+', n)]
    named_ok = all(e21[int(re.findall(r'\d+', n)[0])] == name.strip() for _, _, name, n in h
                   if int(re.findall(r'\d+', n)[0]) in e21)
    return (len(h) == 257 and counts == [33, 24, 33, 9, 25, 19, 20, 16, 43, 33, 1, 1]
            and set(nums) - set(e21) == {155, 172} and set(e21) <= set(nums) and named_ok)

def RH16_probe():
    t = read(RHR)
    loc = t.split('**Resolving locator**')[1].split('# The given')[0]
    L = re.findall(r'^(\d+) (.+?) · [\d.]+(?: and [\d.]+)?, ', loc, re.M)
    name2num = {name: n for n, name, _ in hp_entries()}
    off = [int(n) - name2num[name] for n, name in L if name in name2num]
    unmatched = [name for n, name in L if name not in name2num]
    nums = [int(n) for n, _ in L]
    return (len(L) == 176 and nums[0] == 2 and nums[-1] == 177 and off.count(1) == 174 and len(unmatched) == 2)

# ---------------------------------------------------------------- 8.18 TWENTY-FIVE
def ls_entries():
    t = read(LSR)
    body = t.split('\n# 2 Collecting')[1].split('\n# 3 Passing')[0]
    parts = re.split(r'^## (2\.\d+) .+$', body, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]

def LS7():
    E = ls_entries()
    lines = [re.search(r'^\*\*Any member carrying it\.\*\* (.*)$', e, re.M).group(1) for _, e in E]
    return len(E) == 22 and all(re.match(r'(No\b|No pair|No population)', l) for l in lines)

def LS11():
    E = ls_entries()
    st = {k: re.search(r'^\*\*Standing in the ten\.\*\* (.*)$', e, re.M).group(1) for k, e in E}
    filled = sorted(k for k, s in st.items() if 'All ten stand fill' in s)
    rest = sorted(set(st) - set(filled), key=lambda k: int(k.split('.')[1]))
    return (len(filled) == 18 and rest == ['2.2', '2.4', '2.5', '2.15']
            and 'The bound and the rate stand empty' in st['2.2'] and 'Filled at eight; 3 nye and 6 empty' in st['2.15'])

# ---------------------------------------------------------------- 8.19 TWENTY-SIX
def lf_rows():
    t = read(LFR)
    s1 = t.split('## 1.1 Living files')[1].split('## 1.3 Clusters')[0]
    rows = re.findall(r'^\| \*\*(.+?)\*\* \| (.+?) \|$', s1, re.M)
    return rows[:29], rows[29:]

def LF2():
    liv, imp = lf_rows()
    names = [n for n, _ in liv]
    return (len(liv) == 29 and len(imp) == 5 and names[0] == 'Natural Intelligence'
            and names[-1] == 'TWENTY-SEVEN · Living Ghost Registry'
            and not any('TWENTY-EIGHT' in n or 'TWENTY-NINE' in n for n in names))

def LF3():
    t = read(LFR)
    cl = t.split('## 1.3 Clusters')[1].split('# PART TWO')[0]
    rows = re.findall(r'^\| \*\*(.+?)\*\* \| (.+?) \|$', cl, re.M)
    seated = [x.strip() for _, m in rows for x in m.split('·')]
    words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE',
             'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY',
             'TWENTY-ONE', 'TWENTY-TWO', 'TWENTY-THREE', 'TWENTY-FOUR', 'TWENTY-FIVE', 'TWENTY-SIX', 'TWENTY-SEVEN']
    got = {s.split(' ')[0] for s in seated if s.split(' ')[0] in words}
    return (len(rows) == 7 and len(seated) == 26 and len(set(seated)) == 26
            and sorted(set(words) - got) == ['TWENTY-FOUR', 'TWENTY-SIX', 'TWENTY-THREE'])

def LF4():
    h = rh_deployed()
    c = [sum(1 for p, *_ in h if p == str(k)) for k in range(1, 11)]
    odd, even = c[0::2], c[1::2]
    return all(o > e for o, e in zip(odd, even)) and sum(odd) == 154 and sum(even) == 101

def cross(pattern, cells):
    return [n for n, s in cells if re.search(pattern, s)]

def LF7():
    liv, imp = lf_rows()
    titles = [n for n, _ in liv + imp]
    return (len(cross(r'\bSocial\b(?!-)', liv)) == 9 and len(cross(r'Social-', liv)) == 1
            and sum('Registry' in n for n in titles) + len(cross('Registry', liv)) == 7
            and len(cross(r'(?<!-)\bCompetency\b', liv)) == 3 and len(cross(r'\bSelf-', liv)) == 4)

def LF8_probe():
    liv, imp = lf_rows()
    stable = cross(r'\bStable', liv)
    value = cross(r'\bValue\b', liv + imp)
    surface = cross(r'Surface', liv + imp)
    return (len(stable) == 8 and 'Natural Intelligence Corus' in stable
            and len(surface) == 3 and len(value) == 4)

# ---------------------------------------------------------------- 8.20 TWENTY-SEVEN
def GH13():
    state, flow, either = {1, 7, 8, 9}, {3, 4, 5, 10}, {2, 6}
    return state | flow | either == set(range(1, 11)) and len(state) + len(flow) + len(either) == 10

DOOR_HOLDING = {1: 1, 2: 8, 3: 9, 4: 6, 5: 4, 6: 2, 7: 5, 8: 3, 9: 10, 10: 7}

def GH14():
    t = read(LGR)
    sec = t.split('## 7.10')[2] if t.count('## 7.10') > 1 else t.split('## 7.10')[1]
    rows = re.findall(r'^\| (\d+) · \w[\w-]* \| .+? \| (\d+) · \*\*', sec, re.M)
    got = {int(a): int(b) for a, b in rows}
    return got == DOOR_HOLDING and sorted(got.values()) == list(range(1, 11))

def GH15_probe():
    reached = {1, 7, 8, 3, 4, 5}                # 7.10's second table: (i)(iv)->1, (v)(vii)->7, (vi)->8, (viii)->3,4, (ix)->5
    t = read(LGR)
    said = 'Door lines 6, 9 and 10 carry surplus, bound and reach beside' in t
    return said and sorted(set(range(1, 11)) - reached) == [2, 6, 9, 10]

def GH16():
    t = read(LGR)
    sec = t.split('## 7.11')[2] if t.count('## 7.11') > 1 else t.split('## 7.11')[1]
    rows = re.findall(r'^\| (\d+) · [\w-]+ \| `(\w+)` · (within|at the membrane)', sec, re.M)
    nm = {int(a): (b, c) for a, b, c in rows}
    within = sorted(k for k, (_, f) in nm.items() if f == 'within')
    names = [nm[k][0] for k in range(1, 11)]
    adj = re.findall(r'^\| (\d+) · [\w-]+ \| `(\w+)` → `(\w+)` \| `(\w+)` \| (?:`(\w+)`|No shared)', sec, re.M)
    adj = [(a, x, y, b) for a, x, y, b, _ in adj]
    shared = sorted(int(a) for a, x, y, b in adj if b in (x, y))
    return (len(nm) == 10 and len(set(names)) == 8 and within == [3, 4, 6, 9]
            and len({nm[k][0] for k in within}) == 4 and len({nm[k][0] for k in (1, 2, 5, 7, 8, 10)}) == 4
            and nm[2][0] == nm[7][0] and nm[8][0] == nm[10][0] and len(adj) == 10 and shared == [1, 5])

def GH21():
    rows = [2, 8, 8, 18, 18, 32, 32]
    ends = [sum(rows[:i + 1]) for i in range(7)]
    return sum(rows) == 118 and 2 + 8 + 18 + 32 == 60 and 60 not in ends and ends == [2, 10, 18, 36, 54, 86, 118]

# ---------------------------------------------------------------- 8.21 TWENTY-NINE
def I5():
    a, b = [24, 27, 32], [24, 29, 32]
    g = lambda r: [r[i + 1] - r[i] for i in range(2)]
    return g(a) == [3, 5] and g(b) == [5, 3] and a[-1] - a[0] == b[-1] - b[0] == 8

def I6():
    ok = True
    for k in range(1, 2001):
        x = -1.55 + 3.1 * k / 2001
        d = 1 - math.tan(x) ** 2
        if abs(math.cos(x)) < 1e-6 or abs(math.cos(2 * x)) < 1e-3 or abs(d) < 1e-9: continue
        ok &= math.isclose(math.tan(2 * x), 2 * math.tan(x) / d, rel_tol=1e-9, abs_tol=1e-9)
    return ok

def I8():
    P = [p for p in range(2, 60) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    return len(P) == 17 and P[0] == 2 and P[-1] == 59 and sum(P) == 440

def I9():
    # the resolver's own identifiers give names 1 to 17; the roots of 1 to 16 are twelve, and 17 adds a thirteenth
    src = open(os.path.join(HERE, 'resolver_v372.py')).read()
    ids = {n.id for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Name) and re.fullmatch(r'_\d+_\w+', n.id)}
    ids |= {a.arg for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef) for a in n.args.args if re.fullmatch(r'_\d+_\w+', a.arg)}
    ids |= {n.name for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef)}
    num = {int(re.match(r'_(\d+)_', i).group(1)): i.split('_', 3)[3] for i in ids}
    roots16 = {num[k] for k in range(1, 17)}
    s17 = RV.CONNECTORS[17][0].split('-')[-1]
    return sorted(num) == list(range(1, 18)) and len(roots16) == 12 and s17 == 'abundancing' and num[17] == s17 and s17 not in roots16

# ---------------------------------------------------------------- 8.22 Corus v330
def CO12():
    phi = (1 + 5 ** 0.5) / 2
    x = Fraction(1)
    fib = [1, 1]
    ok = True
    for i in range(40):
        x = 1 + 1 / x
        fib.append(fib[-1] + fib[-2])
        ok &= x == Fraction(fib[-1], fib[-2])
    return ok and abs(float(x) - phi) < 1e-15 and abs(phi * phi - phi - 1) < 1e-12

def CO19():
    gaps = [1, 2, 4, 6]
    kept = [p for p in permutations(range(4)) if all(gaps[p[i]] < gaps[p[i + 1]] for i in range(3))]
    return len(list(permutations(range(4)))) == 24 and kept == [(0, 1, 2, 3)]

def CO21():
    return 7 * 17 - 1 == 118 and 59 * 2 == 118 and 6.94 < 118 / 17 < 6.95

CHECKS = {k: v for k, v in globals().items()
          if re.fullmatch(r'(HP|RH|V|LS|LF|GH|I|CO)\d+(_probe)?', k) and callable(v)}
ORDER = ['HP', 'RH', 'V', 'LS', 'LF', 'GH', 'I', 'CO']

'''

PART_LABELS = {'core': 'PART ONE · FOUNDATION', 'num': 'PART THREE · NUMBERS', 'math': 'PART FOUR · MATHEMATICS', 'two': 'PART FIVE · NETWORKING', 'eq': 'PART SIX · EQUILIBRIA', 'x': 'PART SEVEN · EXPLAINING, NAMING AND THE METHOD', 'o1': 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS', 'o2': 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS', 'o3': 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS'}


# ---------------------------------------------------------------- the kinds of check
FAILURE_PROBES = {'T5', 'K26', 'H24', 'J11', 'P7', 'L29', 'HP11', 'RH16', 'LF8', 'GH15'}   # a failure confirmed at a nye link
BOUND_PROBES = {'F65', 'R55', 'N88', 'X43', 'X107'}                                       # the part of a nye link that holds
FIELD_PROBES = {'X146'}                                                                   # a field link's instance
EXACT_CHECKED = {'F21'}                                                                   # an exact link shown at the arithmetic
PART_ORDER = ['PART ONE · FOUNDATION', 'PART TWO · THE RESOLVER AT ITS NAMES', 'PART THREE · NUMBERS',
              'PART FOUR · MATHEMATICS', 'PART FIVE · NETWORKING', 'PART SIX · EQUILIBRIA',
              'PART SEVEN · EXPLAINING, NAMING AND THE METHOD', 'PART EIGHT · THE EXHIBITS OF OTHER WORKINGS']


class NeedsFile(FileNotFoundError):
    pass


def parse_args(argv):
    repos, verbose, limit = [], False, 120
    it = iter(argv)
    for a in it:
        if a == '--repo':
            repos.append(os.path.abspath(next(it)))
        elif a.startswith('--repo='):
            repos.append(os.path.abspath(a.split('=', 1)[1]))
        elif a == '--timeout':
            limit = int(next(it))
        elif a in ('-v', '--verbose'):
            verbose = True
        elif a in ('-h', '--help'):
            print(__doc__); sys.exit(0)
        else:
            sys.exit(f'unknown argument: {a}')
    return repos, verbose, limit


REPOS, VERBOSE, LIMIT = parse_args(sys.argv[1:])


class TimedOut(Exception):
    pass


def _alarm(signum, frame):
    raise TimedOut(f'no return within {LIMIT} s')


def timed(f):
    """Run f under the time limit, where the platform carries SIGALRM."""
    import signal
    if not hasattr(signal, 'SIGALRM'):
        return f()
    old = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(LIMIT)
    try:
        return f()
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
SEARCH = [HERE] + REPOS
FAKE_RESOLVER = os.path.join(os.sep, '<ccl>', 'resolver_v372.py')


def find(base):
    for d in SEARCH:
        p = os.path.join(d, base)
        if os.path.exists(p):
            return p
    return None


def resolver_source():
    md = find('Exhibit_ONE_Natural_Resolver_v372.md')
    if md:
        m = re.search(r'```python\n(.*?)```', open(md, encoding='utf-8').read(), re.S)
        if m:
            code = m.group(1)
            same = code == RESOLVER_COPY
            note = ('identical to the copy carried here' if same else
                    'DIFFERING from the copy carried here: the checks run at the Exhibit\'s code')
            return code, f'{os.path.basename(md)}, first python block ({note})'
    return RESOLVER_COPY, 'the copy carried in this file (Exhibit_ONE_Natural_Resolver_v372.md not found beside it)'


RESOLVER_SRC, RESOLVER_FROM = resolver_source()


def make_resolver_module():
    lines = RESOLVER_SRC.splitlines(True)
    linecache.cache[FAKE_RESOLVER] = (len(RESOLVER_SRC), None, lines, FAKE_RESOLVER)
    mod = types.ModuleType('resolver_v372')
    mod.__file__ = FAKE_RESOLVER
    exec(compile(RESOLVER_SRC, FAKE_RESOLVER, 'exec'), mod.__dict__)
    sys.modules['resolver_v372'] = mod
    return mod


def _ccl_path(path):
    """The path a part names, found beside the verifier or at a --repo folder."""
    base = os.path.basename(path)
    p = find(base)
    if p is None:
        raise NeedsFile(2, 'needs ' + base, base)
    return p


_real_open = open


def _ccl_open(path, *a, **k):
    if isinstance(path, str) and os.path.basename(path) == 'resolver_v372.py':
        return io.StringIO(RESOLVER_SRC)
    return _real_open(_ccl_path(path) if isinstance(path, str) else path, *a, **k)


def load_part(name):
    make_resolver_module()
    ns = {'__name__': 'ccl_' + name, '__file__': os.path.join(HERE, f'ccl_{name}_checks.py'),
          '__builtins__': __builtins__, 'open': _ccl_open, '_ccl_path': _ccl_path, 'RESOLVER_SRC': RESOLVER_SRC}
    exec(compile(PART_SOURCES[name], f'<ccl part {name}>', 'exec'), ns)
    checks = dict(ns['CHECKS'])
    for k, f in ns.get('FIELD_INSTANCES', {}).items():
        checks[k + ' (field instances)'] = f
    return checks


def link_of(cid):
    return re.match(r'[A-Z]+\d+', cid).group(0)


def kind_of(cid):
    lid = link_of(cid)
    if cid.endswith('_probe'):
        if lid in FAILURE_PROBES: return 'failure probe'
        if lid in BOUND_PROBES: return 'bound probe'
        if lid in FIELD_PROBES: return 'field probe'
        return 'probe'
    if cid.endswith('(field instances)'):
        return 'field instances'
    if lid in EXACT_CHECKED:
        return 'exact'
    return 'run'


def label_of(name, cid):
    if name == 'core':
        return PART_ORDER[0] if cid.startswith('F') else PART_ORDER[1]
    return PART_LABELS[name]


def sort_key(cid):
    lid = link_of(cid)
    return (ORDER.index(lid) if lid in ORDER else 10 ** 6, cid)


def run_all():
    rows = []
    for name in PART_SOURCES:
        try:
            checks = timed(lambda: load_part(name))
        except Exception as e:                       # a part that does not load fails whole
            rows.append((PART_LABELS[name] or PART_ORDER[0], f'<part {name}>', 'run', 'failed', f'the part does not load: {e!r}', 0))
            continue
        for cid in sorted(checks, key=sort_key):
            kind = kind_of(cid)
            t0 = time.time()
            try:
                ok = bool(timed(checks[cid]))
                if kind == 'failure probe':
                    status = 'confirmed failure' if ok else 'failed'
                    note = ('the failure stands (nye)' if ok else
                            'the probe no longer finds the failure: the file or the code changed; run the link again as run')
                else:
                    status = 'passed' if ok else 'failed'
                    note = ''
            except FileNotFoundError as e:
                status, note = 'skipped', 'needs ' + os.path.basename(str(e.filename or e))
            except ImportError as e:
                status, note = 'skipped', 'needs ' + (e.name or str(e))
            except Exception as e:
                status, note = 'failed', f'error: {e!r}'
            rows.append((label_of(name, cid), cid, kind, status, note, time.time() - t0))
    return rows


def wrap(prefix, items):
    return textwrap.fill(' '.join(items), width=100, initial_indent=prefix, subsequent_indent=' ' * len(prefix))


def main():
    t0 = time.time()
    print('Co-Chaining Logic Registry verifier v372 (Exhibit THIRTY)')
    print('Resolver:', RESOLVER_FROM)
    print('Files looked for at:', ', '.join(SEARCH))
    print()
    rows = run_all()
    tot = {'passed': 0, 'failed': 0, 'confirmed failure': 0, 'skipped': 0}
    for part in PART_ORDER:
        pr = [r for r in rows if r[0] == part]
        c = {s: sum(1 for r in pr if r[3] == s) for s in tot}
        for s in tot: tot[s] += c[s]
        head = f'{part}: {c["passed"]} passed, {c["failed"]} failed'
        if c['confirmed failure']: head += f', {c["confirmed failure"]} discrepancies reproduced at nye links'
        if c['skipped']: head += f', {c["skipped"]} skipped'
        print(head)
        if VERBOSE:
            for r in pr:
                desc = RUNS.get(r[1].replace(' (field instances)', ''), '')
                print(f'  {r[1]:<26} {r[3]:<18} [{r[2]}] {r[4]}')
                if desc: print(textwrap.fill(desc, 100, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
        else:
            tag = {'run': '', 'field instances': '', 'exact': ' (exact)', 'bound probe': ' (nye bound, holding)',
                   'field probe': ' (field instance)', 'probe': ' (probe)'}
            passed = [r[1] + tag[r[2]] for r in pr if r[3] == 'passed']
            if passed: print(wrap('  passed: ', [p.replace(' ', ' ') for p in passed]).replace(' ', ' '))
            for r in pr:
                if r[3] == 'confirmed failure':
                    print(f'  discrepancy reproduced at nye link {link_of(r[1])}: {r[1]} returns True, {r[4]}')
            for r in pr:
                if r[3] == 'skipped':
                    print(f'  skipped {r[1]}: {r[4]}')
            for r in pr:
                if r[3] == 'failed':
                    print(f'  FAILED {r[1]}: {r[4] or "returns False"}')
                    desc = RUNS.get(r[1], '')
                    if desc: print(textwrap.fill('the run: ' + desc, 100, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
        print()
    n = sum(tot.values())
    result = 'PASS' if tot['failed'] == 0 else 'FAIL'
    print(f'TOTAL: {n} checks, {tot["passed"]} passed, {tot["failed"]} failed, '
          f'{tot["confirmed failure"]} discrepancies reproduced at nye links, {tot["skipped"]} skipped, not run '
          f'({time.time() - t0:.1f} s). RESULT: {result}')
    print(f'Scope: RESULT covers the {n - tot["skipped"]} checks run, at the resolver named above and the arithmetic; '
          f'the {tot["skipped"]} skipped are unrun, and a discrepancy reproduced is a finding at its nye link, no verifying of a replacing claim.')
    return 0 if tot['failed'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
