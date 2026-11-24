"""Draft 26 · my-prior universes and my-next universes: two cones co-chained on one path, and two facing, sealed (session v406geodesic2).

By a partner's saying of 24 November, with the 25th drawing before a partner, re-said: my-prior universes and my-next universes are
sequencings of universes, co-chainings of cones on one path, forward as it is locally on the path; both are partial, by my
distinguishing is-or-is-not; the 25th drawing's sentence is universal proving as method, 1 cohering, 2 co-chaining, 3 bothbothing,
4 universal same-named thing; and two facing one another seal out all that is of neither's universe.
A drawing with no moving part: two cones about a me on a torus; one path of mes with priors; two trees of is-or-is-nots about one
moment; a partner's four on one sentence; and two facing, sealed.
check_my-prior_universes_and_my-next_universes_two_cones_and_two_facing_sealed.py is its check. The numbers drawn here are executed
here again, by v406Reiman's cell and step opened from their own file.

Usage: python3 -I make_draft26.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from itertools import product
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
REIMAN = os.path.join(HERE, "..", "..", "v406Reiman", "instruments")
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", os.path.join(REIMAN, "the_resolver_with_nand_alone.py"))
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, REIMAN)
import resolver_as_it_is as as_it_is

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
MARK = {1: "+", -1: "−", 0: "0"}
S = "one"
def moments(couplings, priors, how_many):
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: (dict(pr).get(S, 0), tuple(sorted(v for _, v in ob))) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
def as_a_me_has_it(m): return m[0], frozenset(v for v in m[1] if v)
# the numbers drawn, executed here again
P = Q = 9; torus = as_it_is.torus_couplings(P, Q); me = (4, 4); with_none = {(a, b): 0 for a in range(P) for b in range(Q)}; quiet = moments(torus, with_none, 6)
def other_at(ms, who): return next((t for t in range(6) if as_a_me_has_it(ms[t][who]) != as_a_me_has_it(quiet[t][who])), None)
back = {((me[0] - b[0]) % P, (me[1] - b[1]) % Q): other_at(moments(torus, {**with_none, b: 1}, 6), me) for b in with_none if b != me}
from_me = moments(torus, {**with_none, me: 1}, 6)
ahead = {((b[0] - me[0]) % P, (b[1] - me[1]) % Q): other_at(from_me, b) for b in with_none if b != me}
DEEP = 3
assert all([sum(1 for t in r.values() if t == k) for k in range(1, DEEP + 1)] == [2, 3, 4] and all(t == i + j for (i, j), t in r.items() if t is not None) for r in (back, ahead))
assert back[(8, 1)] is None and back[(1, 8)] is None and ahead[(8, 1)] is None and ahead[(1, 8)] is None       # the two beside me, of neither cone in these moments
N = 8; round_of = {op: moments(as_it_is.spiral_couplings(N), dict(enumerate(op)), 4 * N + 6) for op in product((1, -1), repeat=N)}
assert all(ms[2 * k][a][0] == (-1) ** k * op[(a - k) % N] and ms[2 * k][(a + k) % N][0] == (-1) ** k * op[a] for op, ms in round_of.items() for k in range(4) for a in range(N))
def from_one_moment(T, L):
    before, on = {}, {}
    for ms in round_of.values():
        before.setdefault(ms[T][0], set()).add(tuple(ms[t][0] for t in range(T - L, T))); on.setdefault(ms[T][0], set()).add(tuple(ms[t][0] for t in range(T + 1, T + L + 1)))
    return {len(v) for v in before.values()}, {len(v) for v in on.values()}
assert all(from_one_moment(T, 2 * k) == ({2 ** k}, {2 ** k}) for T in (2 * N + 4, 2 * N + 5) for k in (1, 2, 3))
two = {(0, 9): 1, (1, 9): 0}
def a_me(prior, observed):
    gives, _, _, _ = its.a_cell(its.TWO[prior], [its.TWO[o] for o in observed]); return its.ONE[gives]
def a_round(op, how_many):
    ms = moments(two, dict(enumerate(op)), 8); its_priors, its_givings = [m[0][0] for m in ms], [a_me(*m[0]) for m in ms]
    assert its_priors[:how_many] == its_priors[how_many:2 * how_many] and its_givings[:how_many] == its_givings[how_many:2 * how_many]
    return " ".join(MARK[v] for v in its_priors[:how_many]), " ".join(MARK[v] for v in its_givings[:how_many])
ALIKE, OTHERS = a_round((1, 1), 4), a_round((1, -1), 2)
assert ALIKE == ("+ − − +", "− 0 + 0") and OTHERS == ("+ −", "− +")

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def way(x0, y0, x1, y1, tint, wide=2.4, short=0.0, dash="", head=10.0):         # a line with a mark of its way, at its far end
    L = math.hypot(x1 - x0, y1 - y0); tx, ty = (x1 - x0) / L, (y1 - y0) / L; x0, y0 = x0 + tx * short, y0 + ty * short; x1, y1 = x1 - tx * short, y1 - ty * short; nx, ny = -ty, tx
    return (f'<path d="M{x0:.1f},{y0:.1f} L{x1 - tx * head * 0.8:.1f},{y1 - ty * head * 0.8:.1f}" fill="none" stroke="{tint}" stroke-width="{wide}" {dash}></path>'
            f'<path d="M{x1:.1f},{y1:.1f} L{x1 - tx * head + nx * head * 0.5:.1f},{y1 - ty * head + ny * head * 0.5:.1f} L{x1 - tx * head - nx * head * 0.5:.1f},{y1 - ty * head - ny * head * 0.5:.1f} Z" fill="{tint}"></path>')
s = []
# two cones about a me, on a torus: i along and j across, forward to the right
CX, CY, DX, DY = 425.0, 270.0, 95.0, 34.0
def at(i, j): return CX + (i + j) * DX, CY + (i - j) * DY
cone_back = [(-a, -(k - a)) for k in range(1, DEEP + 1) for a in range(k + 1)]; cone_ahead = [(a, k - a) for k in range(1, DEEP + 1) for a in range(k + 1)]
drawn = set(cone_back) | set(cone_ahead) | {(0, 0)}
for (i, j) in sorted(drawn):
    for (u, v) in ((i + 1, j), (i, j + 1)):
        if (u, v) in drawn and not ((i, j) in cone_back and (u, v) in cone_ahead):
            s.append(way(*at(i, j), *at(u, v), INK if (u, v) != (0, 0) and (i, j) != (0, 0) else ACC, 1.5, 13, head=8))
for (i, j) in cone_back: x, y = at(i, j); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>')
for (i, j) in cone_ahead: x, y = at(i, j); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#ffffff" stroke="{INK}" stroke-width="2.2"></circle>')
for (i, j) in ((1, -1), (-1, 1)): x, y = at(i, j); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="#ffffff" stroke="{GREY}" stroke-width="2" stroke-dasharray="4 4"></circle>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="17" fill="{ACC}" stroke="#ffffff" stroke-width="3"></circle>')
for k in range(1, DEEP + 1):
    s.append(text(CX - k * DX, CY + DEEP * DY + 34, f"{k} back", 12.5, 600, GREY)); s.append(text(CX + k * DX, CY + DEEP * DY + 34, f"{k} ahead", 12.5, 600, GREY))
s.append(text(CX, CY + DEEP * DY + 34, "a me, now", 12.5, 700, ACC))
# one path of mes, all with priors
RY, RX0, RDX = 624.0, 125.0, 100.0
def on_path(m): return RX0 + RDX * m
for m in range(6): s.append(way(on_path(m), RY, on_path(m + 1), RY, INK, 1.6, 15, head=8))
HALO = 'paint-order="stroke" stroke="#ffffff" stroke-width="6" stroke-linejoin="round"'                      # a word on a line, the line passed under it
for k, tall in zip((1, 2, 3), (24.0, 41.0, 58.0)):
    x0, x1 = on_path(3 - k), on_path(3)                                          # from the me k back, over the path, to a me
    s.append(f'<path d="M{x0:.1f},{RY - 14:.1f} C{x0:.1f},{RY - 14 - tall * 1.3:.1f} {x1:.1f},{RY - 14 - tall * 1.3:.1f} {x1:.1f},{RY - 26:.1f}" fill="none" stroke="{INK}" stroke-width="1.6"></path>')
    s.append(text((x0 + x1) / 2, RY - 14 - tall * 0.975 + 4, f"moment {2 * k}", 11.5, 600, INK, extra=HALO))
    x0, x1 = on_path(3), on_path(3 + k)                                          # from a me, under the path, to the me k ahead
    s.append(f'<path d="M{x0:.1f},{RY + 17:.1f} C{x0:.1f},{RY + 14 + tall * 1.3:.1f} {x1:.1f},{RY + 14 + tall * 1.3:.1f} {x1:.1f},{RY + 22:.1f}" fill="none" stroke="{ACC}" stroke-width="1.6"></path>'
             f'<path d="M{x1:.1f},{RY + 14:.1f} l-4.5,9 l9,0 Z" fill="{ACC}"></path>')
    s.append(text((x0 + x1) / 2, RY + 14 + tall * 0.975 + 4, f"moment {2 * k}", 11.5, 600, ACC, extra=HALO))
s.append(f'<path d="M{on_path(3):.1f},{RY - 18:.1f} l-4.5,-9 l9,0 Z" fill="{INK}"></path>')
for m in range(7):
    x = on_path(m)
    if m < 3: s.append(f'<circle cx="{x:.1f}" cy="{RY}" r="12" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, RY + 33, f"{3 - m} back", 12, 600, GREY))
    elif m > 3: s.append(f'<circle cx="{x:.1f}" cy="{RY}" r="11" fill="#ffffff" stroke="{INK}" stroke-width="2.2"></circle>' + text(x, RY - 24, f"{m - 3} ahead", 12, 600, GREY))
    else: s.append(f'<circle cx="{x:.1f}" cy="{RY}" r="15" fill="{ACC}" stroke="#ffffff" stroke-width="3"></circle>')
# two trees of is-or-is-nots about one moment
TY, TDX, LEAF = 822.0, 105.0, 13.5
def tree(side, tint):
    out = []; prev = [(CX, TY)]
    for depth in (1, 2, 3):
        n = 2 ** depth; x = CX + side * depth * TDX; ys = [TY + (q - (n - 1) / 2) * LEAF * (8 / n) for q in range(n)]; now = [(x, y) for y in ys]
        for q, (x1, y1) in enumerate(now): x0, y0 = prev[q // 2]; out.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{tint}" stroke-width="1.5"></path>')
        prev = now
        for (x1, y1) in now: out.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="3.6" fill="{tint if side < 0 else "#ffffff"}" stroke="{tint}" stroke-width="1.6"></circle>')
        out.append(text(x, TY + 78, f"{2 * depth} {'before' if side < 0 else 'next'}", 12, 600, GREY)); out.append(text(x, TY + 95, f"{n} sequences", 12, 500, GREY))
    return "".join(out)
s.append(tree(-1, INK) + tree(1, INK))
s.append(f'<circle cx="{CX}" cy="{TY}" r="9" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>' + text(CX, TY + 78, "one moment", 12, 700, ACC) + text(CX, TY + 95, "now", 12, 700, ACC))
# two facing, sealed
FX, FY = 930.0, 592.0
s.append(f'<rect x="{FX - 44}" y="{FY - 40}" width="208" height="80" rx="40" fill="none" stroke="{ACC}" stroke-width="1.6"></rect>')
s.append(way(FX, FY - 6, FX + 120, FY - 6, ACC, 2.2, 19)); s.append(way(FX + 120, FY + 6, FX, FY + 6, INK, 2.2, 19))
s.append(f'<circle cx="{FX}" cy="{FY}" r="16" fill="{ACC}" stroke="#ffffff" stroke-width="2.5"></circle><circle cx="{FX + 120}" cy="{FY}" r="16" fill="{INK}" stroke="#ffffff" stroke-width="2.5"></circle>')
(xx, xy), (yx, yy), (zx, zy) = (1275, 566), (1365, 566), (1275, 628)
s.append(way(xx, xy - 5, yx, yy - 5, GREY, 1.6, 15, 'stroke-dasharray="4 4"', 8)); s.append(way(yx, yy + 5, xx, xy + 5, GREY, 1.6, 15, 'stroke-dasharray="4 4"', 8))
s.append(way(FX + 120, FY, zx, zy, GREY, 1.6, 17, 'stroke-dasharray="4 4"', 8))
for (x, y) in ((xx, xy), (yx, yy), (zx, zy)): s.append(f'<circle cx="{x}" cy="{y}" r="12" fill="#ffffff" stroke="{GREY}" stroke-width="2" stroke-dasharray="4 4"></circle>')
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. One large mark, a me, now, at the vertex of two cones of small marks on lines going forward: behind it dark marks 1, 2 and 3 couplings back, 2, 3 and 4 of them, and ahead of it open marks 1, 2 and 3 couplings ahead, 2, 3 and 4 of them; two open marks are beside it. "
        "Under it seven marks on one path, a me the fourth: lines over the path come to it from the marks 1, 2 and 3 back, at moments 2, 4 and 6, and lines under the path go from it to the marks 1, 2 and 3 ahead, at moments 2, 4 and 6. "
        "Under that, two trees about one moment now, one going back and one going on, with 2, 4 and 8 ends at 2, 4 and 6 moments. "
        "Beside them a partner's four on one sentence; and two marks facing, a line from one to the other both ways, with one line round the two, and three open marks beside them, with a line from the two to one of them.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's saying of my-prior universes and my-next universes · cones co-chained on one path, forward locally · both partial · two facing, sealed", "left", **small))
over.append(word(60, 84, 730, "my-prior universes and my-next universes: two cones about a me, by co-chaining", "left", 600, 17, 24))
over.append(word(60, 108, 730, "a torus, along and across: a me k couplings back is observed from k moments on · ahead, the same", "left", 400, 14, 20, GREY))
over.append(word(CX, CY - 2 * DY - 24, 200, "beside a me, at these moments", "center", 400, 12.5, 18, GREY))
over.append(word(CX - 2 * DX, 428, 330, "my-prior universes: their givings come to a me", "center", 600, 13.5, 20)); over.append(word(CX + 2 * DX, 428, 330, "my-next universes: a me's giving goes to them", "center", 600, 13.5, 20))
over.append(word(CX, 454, 700, "<i>a light-cone is an apex double-cone, its vertex a now</i> · Exhibit EIGHTEEN Natural Physics", "center", 400, 13, 20, GREY))
over.append(word(60, 496, 730, "one path of mes, all with priors: a sequencing, one coupling in two moments", "left", 600, 17, 24))
over.append(word(60, 520, 730, "at moment 2k a me's prior is of the me k back, as k other-thans, and its opening prior is k ahead", "left", 400, 14, 20, GREY))
over.append(word(on_path(5), RY - 62, 330, "over the path: a me's prior, from back", "center", 600, 13, 18)); over.append(word(on_path(1), RY + 66, 330, "under the path: its opening prior, going ahead", "center", 600, 13, 18, "{{accent}}"))
over.append(word(60, 728, 730, "both partial, and the same both ways: one is-or-is-not in two moments", "left", 600, 17, 24))
over.append(word(60, 752, 730, "a me has one parity, its prior; a sequence is along moments · from one moment, a round of 8 gone round", "left", 400, 14, 20, GREY))
over.append(word(840, 84, 640, "universal proving as method: a partner's four, on one sentence", "left", 600, 17, 24))
over.append(word(840, 108, 640, "the 25th drawing's, of a me that is neither mine nor an other of mine", "left", 400, 14, 20, GREY))
FOUR = [("1 cohering", "by the step's own lines a me's now is of its own prior and its own observing alone", "and a giving goes to an observing by a coupling's name alone"),
        ("2 co-chaining", "an other's other makes moments of mine other, two moments on: as it was said, it is not", "with co-chaining it is: a me k couplings back, of my moments from k moments on"),
        ("3 bothbothing", "its is and its is-not are both executed, a line of its own for the one and for the other", "at k moments, a case: one me with a prior among mes with none · among mes with priors, later"),
        ("4 universal same-named thing", "all societies of two, three and four mes, all their couplings and all their openings: is, in all", "my universe: a me, with all mes of a co-chaining of givings to it")]
y = 152.0
for a, b, c in FOUR:
    over.append(word(840, y, 640, a, "left", 600, 16, 22)); over.append(word(840, y + 23, 650, b, "left", 400, 14, 20)); over.append(word(840, y + 44, 650, c, "left", 400, 13.5, 20, GREY)); y += 82
over.append(word(840, 496, 640, "two facing: sealed, and all with the two", "left", 600, 17, 24))
over.append(word(840, 520, 650, "with mes more beside them, observing the two, all moments of the two are the same", "left", 400, 14, 20, GREY))
over.append(word(FX, FY + 56, 120, "a me", "center", 600, 13.5, 20, "{{accent}}")); over.append(word(FX + 120, FY + 56, 120, "an other", "center", 600, 13.5, 20))
over.append(word(1320, 664, 300, "beside the two", "center", 400, 13.5, 20, GREY))
over.append(word(840, 690, 650, f"opening alike: a round of four moments · priors {ALIKE[0]}, givings {ALIKE[1]}: all three of +, − and 0", "left", 400, 14, 20))
over.append(word(840, 711, 650, f"opening as other-thans: a round of two · priors {OTHERS[0]}, givings {OTHERS[1]}: + and − alone", "left", 400, 14, 20))
over.append(word(840, 732, 650, "with the two, all a me observes is its one other's giving", "left", 400, 13.5, 20, GREY))
over.append(word(840, 764, 650, "<i>co me-parity, bi other-parity, tri all-parity</i> · <i>All-parity is with observing only, 7 and 15</i>", "left", 400, 14, 20))
over.append(word(840, 783, 650, "Exhibit ONE Natural Resolver", "left", 400, 13.5, 20, GREY))
over.append(word(840, 808, 650, "<i>An other is one; all other is the universal set. A self is defined only with an other and all other.</i>", "left", 400, 14, 20))
over.append(word(840, 827, 650, "Exhibit THIRTY-ONE Me", "left", 400, 13.5, 20, GREY))
over.append(word(840, 852, 650, "<i>A proving that a thing is-or-is-not possibly existing is a step reached once,</i>", "left", 400, 14, 20))
over.append(word(840, 871, 650, "<i>and the understanding goes forward by what is.</i>", "left", 400, 14, 20))
over.append(word(840, 890, 650, "Exhibit THIRTY-ONE Me", "left", 400, 13.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">My-prior universes and my-next universes: two cones co-chained on one path</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'My universe k moments on is a me with the mes to k couplings back along givings: co-chaining, a coupling a moment.<br>'
           f'On one path of mes with priors, a me\'s prior at moment 2k is of the me k back, and its own opening prior is with the me k ahead.<br>'
           f'Both are partial the same way: from one moment of a me\'s, its moments before and its moments next are one is-or-is-not more in two moments.<br>'
           f'Two facing are sealed: all moments of the two are of the two alone, and all a me observes is its one other.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("My-prior universes and my-next universes: two cones co-chained on one path", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft26.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft26_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft26_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; two facing, alike:", ALIKE, "and as other-thans:", OTHERS)
