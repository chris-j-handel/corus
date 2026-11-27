"""One me's other-than, carried or lost: all openings of a small surface, all selves living, no opening drawn.

A society is opened twice, the second time with one me's prior laid as its other-than, all else the same.
A self the other-than is in: a self whose own moments are, with some moment, other-than what they were.
Executed until both societies come again, so that never is never.

The twelve lines are opened from the instrument beside this one and are not altered. For all openings at once they
are read as a table of a prior with a surfacing, the table made from the lines and checked against them, all cases.

Three observings:
  all others together       the lines as they are: what all couplings into a self lay, together
  one other a moment        a self observes one coupling a moment, its couplings in turn; two orders of turns
  a co-chain                a self has one coupling into it: Exhibit ONE's spiral

A line ends is or is-not. A line ending sized gives numbers alone. It opens one file, the instrument beside it, and writes none.

    python3 -I incoming/v409pvnp/instruments/an_other_than_carried_or_lost_all_openings.py .
"""
import itertools
import numpy as np
from pathlib import Path

src = (Path(__file__).resolve().parent / "two_me_parities_on_a_surface_of_the_neither.py").read_text()
exec(src[src.index("import collections"):src.index("LAYINGS = [")])
exec(src[src.index("def a_spiral"):src.index("def exhibit_ones_opening")])
out = []

CODE = {NEITHER: 0, PLUS: 1, MINUS: 2}
LAYS = np.zeros((3, 3), np.uint8); NEXT = np.zeros((3, 3), np.uint8)
for prior, pc in CODE.items():
    for surf, sc in CODE.items():
        lays, nxt = now_and_same_existing_me_parity(prior, [] if surf == NEITHER else [surf])
        LAYS[pc, sc], NEXT[pc, sc] = CODE[lays], CODE[nxt]
table_is_the_lines = True
for k in range(0, 5):
    for obs in itertools.product((NEITHER, PLUS, MINUS), repeat=k):
        codes = {CODE[g] for g in obs} - {0}
        sc = codes.pop() if len(codes) == 1 else 0
        for prior, pc in CODE.items():
            lays, nxt = now_and_same_existing_me_parity(prior, list(obs))
            table_is_the_lines &= (CODE[lays], CODE[nxt]) == (LAYS[pc, sc], NEXT[pc, sc])
say("E0 the table of a prior with a surfacing is the twelve lines, with none to four others observed, all cases", table_is_the_lines)
say("E1 by the lines a me observing one parity alone has that parity as its now, with all three priors; its prior is in its laying alone, "
    "none with the same and its now with its other-than or with no prior",
    all(NEXT[p, s] == s for p in (0, 1, 2) for s in (1, 2)) and all(LAYS[s, s] == 0 and LAYS[3 - s, s] == s and LAYS[0, s] == s for s in (1, 2)))

def society(outs, turns=None):
    selves = list(outs); idx = {s: i for i, s in enumerate(selves)}
    ins = [[] for _ in selves]
    for frm, tos in outs.items():
        for to in tos: ins[idx[to]].append(idx[frm])
    if turns: ins = [[idx[f] for f in turns[s]] for s in selves]
    return selves, ins

def a_moment(state, lay, ins, t, in_turn):
    surf = np.zeros_like(state)
    for s in range(state.shape[1]):
        if in_turn: surf[:, s] = lay[:, ins[s][(t - 1) % len(ins[s])]]
        else:
            got = lay[:, ins[s]]
            plus = (got == 1).any(axis=1); minus = (got == 2).any(axis=1)
            surf[:, s] = np.where(plus & ~minus, 1, np.where(minus & ~plus, 2, 0))
    return NEXT[state, surf], LAYS[state, surf]

def carried(outs, in_turn=False, turns=None, the_inverted=None, settle=256, most=20000):
    """All openings; a me inverted, each of the_inverted in turn. Returns cases, cases with all, cases with none, the latest parting moment,
    and how many nows the openings have come to at the settling moment."""
    selves, ins = society(outs, turns); S = len(selves)
    period = int(np.lcm.reduce([len(i) for i in ins])) if in_turn else 1
    openings = np.array(list(itertools.product((1, 2), repeat=S)), np.uint8)
    cases = with_all = with_none = latest = 0; nows = None
    for A in (range(S) if the_inverted is None else the_inverted):
        other = openings.copy(); other[:, A] = 3 - other[:, A]
        s1, l1, s2, l2 = openings.copy(), np.zeros_like(openings), other, np.zeros_like(openings)
        parted = np.zeros(openings.shape, np.int32); snap = None; closed = np.zeros(len(openings), bool); t = 0
        while not closed.all():
            t += 1
            s1, l1 = a_moment(s1, l1, ins, t, in_turn); s2, l2 = a_moment(s2, l2, ins, t, in_turn)
            new = (s1 != s2) & (parted == 0); parted[new] = t
            if snap is None and t >= settle and t % period == 0:
                snap = (s1.copy(), l1.copy(), s2.copy(), l2.copy()); snap_t = t
                if nows is None: nows = len(np.unique(np.concatenate([s1, l1], axis=1), axis=0))
            elif snap is not None and (t - snap_t) % period == 0:
                closed |= ((s1 == snap[0]) & (l1 == snap[1]) & (s2 == snap[2]) & (l2 == snap[3])).all(axis=1)
            if t > most: raise SystemExit("a society did not come again")
        reached = (np.delete(parted, A, axis=1) > 0).sum(axis=1)
        cases += len(reached); with_all += int((reached == S - 1).sum()); with_none += int((reached == 0).sum())
        latest = max(latest, int(parted.max()))
    return cases, with_all, with_none, latest, nows, 2 ** S

def a_row(label, got):
    cases, with_all, with_none, latest, nows, openings = got
    return (f"   {label}: cases {cases:,} · in all other selves {with_all:,} · in none {with_none:,} · the latest parting, moment {latest} · "
            f"{openings:,} openings come to {nows:,} nows")

# a co-chain
rows = []; e2 = True; e2_apart = True; e2_twice = True
for n in (7, 16):
    got = carried(a_spiral(n), the_inverted=[0])           # a spiral's selves are alike by its turning: one self inverted stands for all
    e2 &= got[1] == got[0]; e2_apart &= got[4] == got[5]; e2_twice &= got[3] == 2 * (n - 1)
    rows.append(a_row(f"Exhibit ONE's spiral of {n}", got))
say("E2 on a co-chain, Exhibit ONE's spiral of 7 and of 16, one me's other-than is in all other selves' own moments, with all openings", e2)
say("E3 on a co-chain all openings stay apart: as many nows as openings", e2_apart)
say("E4 on a co-chain the other-than is in the farthest self's moments at twice its couplings along the chain", e2_twice)
for r in rows: say(r, "sized")

# surfaces, the lines as they are
rows = []; e5 = True; merged = True
torus_3_3 = None
for label, outs, inv in (("3 is-or-is-nots", is_or_is_nots(3), [0]), ("a round of 8 both ways", a_round(8), [0]),
                         ("Exhibit ONE's torus 3 by 3", a_torus(3, 3), [0]), ("a closing surface 3 by 3", a_closing_surface(3, 3), None),
                         ("Exhibit ONE's torus 3 by 4", a_torus(3, 4), [0]), ("4 is-or-is-nots, the 1 to 16", is_or_is_nots(4), [0])):
    got = carried(outs, the_inverted=inv); e5 &= got[1] == got[0]; merged &= got[4] < got[5]
    if label == "Exhibit ONE's torus 3 by 3": torus_3_3 = got[4]
    rows.append(a_row(label, got))
say("E5 on a surface, all others together, one me's other-than is in all other selves' own moments, with all openings", e5)
say("E6 on a surface, all others together, openings merge: fewer nows than openings, at all six surfaces", merged)
for r in rows: say(r, "sized")
say(f"   v406geodesic2's sentence 48 has 512 openings of a torus of 3 by 3 coming to 68 nows; here, nows as a self's parity with its laying, {torus_3_3}", "sized")

# surfaces, one other a moment, in turn
rows = []; e7 = True
for n in (3, 4):
    outs = is_or_is_nots(n)
    pairs = {p: [p ^ (1 << i) for i in range(n)] for p in outs}         # all selves in pairs, an is-or-is-not a moment
    got = carried(outs, in_turn=True, turns=pairs, the_inverted=[0]); e7 &= got[1] == got[0]
    rows.append(a_row(f"{n} is-or-is-nots, in pairs, an is-or-is-not a moment", got))
got = carried(is_or_is_nots(3), in_turn=True); e7 &= got[1] == got[0]
rows.append(a_row("3 is-or-is-nots, turns by a self's number, all selves inverted in turn", got))
got = carried(a_closing_surface(3, 3), in_turn=True); e7 &= got[1] == got[0]
rows.append(a_row("a closing surface 3 by 3, turns by a self's number", got))
say("E7 on a surface, one other a moment in turn, one me's other-than is in all other selves' own moments, with all openings", e7)
for r in rows: say(r, "sized")

# the surface's places laid as one co-chain, an other-than a step
n = 4; gray = [i ^ (i >> 1) for i in range(1 << n)]
one_step = all(bin(gray[i] ^ gray[(i + 1) % len(gray)]).count("1") == 1 for i in range(len(gray)))
chain = {gray[i]: [gray[(i + 1) % len(gray)]] for i in range(len(gray))}
got = carried(chain, the_inverted=[0])
say("E8 the 16 places of 4 is-or-is-nots are one co-chain, a place to its next one other-than, the last to the first", one_step)
say("E9 on that co-chain one me's other-than is in all other selves' own moments, with all openings, and all openings stay apart",
    got[1] == got[0] and got[4] == got[5])
say(f"   on it the latest parting is moment {got[3]}; the farthest two places of the surface are {n} couplings apart, and 15 along the co-chain", "sized")

for mark, text in out: print(f"{text}: {mark}" if mark != "sized" else text)
print()
print(sum(m == "is" for m, _ in out), "lines is,", sum(m == "is-not" for m, _ in out), "is-not,", sum(m == "sized" for m, _ in out), "sized")
