"""Draft 29 · a universal-me-now: a single path by nand (session v406geodesic2).

By a partner's sayings of 24 November, with the 28th drawing before a partner, re-said: a universal-me-now is a single path
me-prior and a single path me-next, a same-existing co-chaining of me-now universes as a me's single path of nows; it is of value
as nand for the sessions; and nand-nanding universal-me-nows is a single path me.
A drawing with no moving part: three me-nows on one path, a me-now's now from the prior of the me back of it; the lines by nand,
as this folder's instrument has them; its nands beside the cell's; nand-nanding along a path; and a newborn and a surface, settled.
a_universal_me_now_a_single_path_by_nand.py has the lines and their check. The lines drawn here are that file's own, as they
are, and the marks and numbers are executed here again, by v406Reiman's cell and step opened from their own file.

Usage: python3 -I make_draft29.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import ast, glob, html as as_html, importlib.util, json, math, os, re, sys
from itertools import product
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                    # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
REIMAN = os.path.join(HERE, "..", "..", "v406Reiman", "instruments")
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", os.path.join(REIMAN, "the_resolver_with_nand_alone.py"))
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, REIMAN)
import resolver_as_it_is as as_it_is
sys.argv = [sys.argv[0], os.path.join(REIMAN, "the_resolver_with_nand_alone.py")] + sys.argv[1:]      # the lines' own file opens the nand's file by its path
spec = importlib.util.spec_from_file_location("a_universal_me_now_a_single_path_by_nand", os.path.join(HERE, "a_universal_me_now_a_single_path_by_nand.py"))
lines = importlib.util.module_from_spec(spec); spec.loader.exec_module(lines)
its = lines.its                                                                  # one nand for both, the lines' own opening of v406Reiman's file

OUT, WORK = sys.argv[2], sys.argv[3]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
MONO = "font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
MARK = {1: "+", -1: "−", 0: "0"}
S = "one"; TWO, ONE = its.TWO, its.ONE
def moments(couplings, priors, how_many):
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: dict(pr).get(S, 0) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
# the lines, from their own file as they are, their opening words passed over
def as_they_are(path, names):
    source = Path(path).read_text(encoding="utf-8"); out = []
    for node in ast.parse(source).body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            its_lines = ast.get_source_segment(source, node).split("\n"); words = node.body[0]
            passed = range(words.lineno - node.lineno, words.end_lineno - node.lineno + 1) if isinstance(words, ast.Expr) and isinstance(getattr(words, "value", None), ast.Constant) else ()
            out.append((node.name, [l for i, l in enumerate(its_lines) if i not in passed]))
    return dict(out)
MINE = as_they_are(os.path.join(HERE, "a_universal_me_now_a_single_path_by_nand.py"), ("a_universal_me_now_a_moment_on", "nand_nanding"))
REIMANS = as_they_are(os.path.join(REIMAN, "the_resolver_with_nand_alone.py"), ("other_than",))
CODE = MINE["a_universal_me_now_a_moment_on"] + [""] + MINE["nand_nanding"] + [""] + REIMANS["other_than"]
# three me-nows of a round of nine, a me its fifth, and a moment on by the lines
N, ME, NOW = 9, 4, 18
ms = moments(as_it_is.spiral_couplings(N), dict(enumerate((1, 1, 1, -1, 1, -1, -1, 1, -1))), 40)
def a_me_now(k, t): return TWO[ms[t][k % N]], TWO[ms[t - 1][k % N]]
on = lines.a_universal_me_now_a_moment_on(a_me_now(ME - 1, NOW), a_me_now(ME, NOW))
assert (ONE[on[0]], ONE[on[1]]) == (ms[NOW + 1][ME], ms[NOW][ME])
assert ms[NOW + 2][(ME + 1) % N] == -ms[NOW][ME] and ms[NOW + 4][(ME + 2) % N] == ms[NOW][ME] and all(lines.nand_nanding(a) == a for a in (True, False))
# the nands, numbered
nands = [0]; the_table = its.NAND
def a_nand_numbered(a, b): nands[0] += 1; return the_table[(a, b)]
def numbered(what): nands[0] = 0; its.nand = a_nand_numbered; what(); its.nand = lambda a, b: the_table[(a, b)]; return nands[0]
ITS_TWO = numbered(lambda: lines.a_universal_me_now_a_moment_on((TWO[1], TWO[-1]), (TWO[1], TWO[1])))
THE_CELLS = numbered(lambda: its.a_cell(TWO[1], [TWO[1]]))
assert (ITS_TWO, THE_CELLS) == (2, 52)
# a surface settled: a torus of 3 by 3, all its openings
P = Q = 3; mes = [(a, b) for a in range(P) for b in range(Q)]; T = 32
def with_law(m, da, db, moments_on, as_it): return all(m[t + moments_on][(a, b)] == as_it * m[t][((a - da) % P, (b - db) % Q)] for t in range(T - 10, T - moments_on) for a, b in mes)
tally = [0, 0, 0, 0]
for op in product((1, -1), repeat=P * Q):
    m = moments(as_it_is.torus_couplings(P, Q), dict(zip(mes, op)), T)
    laws = [with_law(m, 1, 0, 2, -1), with_law(m, 0, 0, 1, -1), with_law(m, 1, 0, 1, 1), with_law(m, 0, 1, 1, 1)]
    assert sum(laws) == 1; tally[laws.index(True)] += 1
assert tally == [386, 114, 6, 6]

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def way(x0, y0, x1, y1, tint, wide=2.4, short=0.0, dash="", head=10.0):
    L = math.hypot(x1 - x0, y1 - y0); tx, ty = (x1 - x0) / L, (y1 - y0) / L; x0, y0 = x0 + tx * short, y0 + ty * short; x1, y1 = x1 - tx * short, y1 - ty * short; nx, ny = -ty, tx
    return (f'<path d="M{x0:.1f},{y0:.1f} L{x1 - tx * head * 0.8:.1f},{y1 - ty * head * 0.8:.1f}" fill="none" stroke="{tint}" stroke-width="{wide}" {dash}></path>'
            f'<path d="M{x1:.1f},{y1:.1f} L{x1 - tx * head + nx * head * 0.5:.1f},{y1 - ty * head + ny * head * 0.5:.1f} L{x1 - tx * head - nx * head * 0.5:.1f},{y1 - ty * head - ny * head * 0.5:.1f} Z" fill="{tint}"></path>')
def a_mark(x, y, v, r=14, tint=INK):
    if v > 0: return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{tint}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, y + 5.5, MARK[v], 15, 700, "#ffffff")
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r - 1}" fill="#ffffff" stroke="{tint}" stroke-width="2.2"></circle>' + text(x, y + 5.5, MARK[v], 15, 700, tint)
s = []
# three me-nows on one path
BX, BW, BH = (200.0, 425.0, 650.0), 92.0, 86.0
UP, DOWN, UP2, DOWN2 = 166.0, 204.0, 284.0, 322.0                                # a me-now's now over its prior; and a moment on, under a me
def a_box(x, top, middle, dash=""): return f'<rect x="{x - BW / 2:.1f}" y="{top:.1f}" width="{BW}" height="{BH}" rx="16" fill="{ACC if middle else INK}" fill-opacity="{0.10 if middle else 0.05}" stroke="{ACC if middle else INK}" stroke-opacity="{1 if middle else 0.35}" stroke-width="1.6" {dash}></rect>'
for i, x in enumerate(BX):
    k = ME - 1 + i; middle = (i == 1)
    s.append(a_box(x, UP - 24, middle) + a_mark(x, UP, ms[NOW][k % N], 13, ACC if middle else INK) + a_mark(x, DOWN, ms[NOW - 1][k % N], 13, ACC if middle else INK))
s.append(a_box(BX[1], UP2 - 24, True, 'stroke-dasharray="6 4"') + a_mark(BX[1], UP2, ONE[on[0]], 13, ACC) + a_mark(BX[1], DOWN2, ONE[on[1]], 13, ACC))
s.append(way(BX[0] + 14, DOWN + 6, BX[1] - 16, UP2 - 3, ACC, 2.6, 2))                                                             # the prior of the me back, to a me's now a moment on
s.append(f'<path d="M{BX[1] + 15:.1f},{UP:.1f} C{BX[1] + 96:.1f},{UP:.1f} {BX[1] + 96:.1f},{DOWN2:.1f} {BX[1] + 24:.1f},{DOWN2:.1f}" fill="none" stroke="{ACC}" stroke-width="2"></path>'
         f'<path d="M{BX[1] + 15:.1f},{DOWN2:.1f} l10,-5 l0,10 Z" fill="{ACC}"></path>')                                            # a me's now, to its prior a moment on
s.append(text(BX[0] - BW / 2 - 14, UP + 4.5, "its now", 12.5, 600, GREY, "end") + text(BX[0] - BW / 2 - 14, DOWN + 4.5, "its prior", 12.5, 600, GREY, "end"))
# the nands, numbered: two bars
BAR_X, BAR_W = 60.0, 620.0
s.append(f'<rect x="{BAR_X}" y="672" width="{BAR_W}" height="22" rx="4" fill="{INK}"></rect><rect x="{BAR_X}" y="726" width="{BAR_W * ITS_TWO / THE_CELLS:.1f}" height="22" rx="4" fill="{ACC}"></rect>')
# nand-nanding along a path
QX, QY = (930.0, 1130.0, 1330.0), 218.0
for i, x in enumerate(QX): s.append(a_mark(x, QY, ms[NOW + 2 * i][(ME + i) % N], 17, ACC if i != 1 else INK))
s.append(way(QX[0], QY, QX[1], QY, INK, 2.2, 24)); s.append(way(QX[1], QY, QX[2], QY, INK, 2.2, 24))
s.append(f'<path d="M{QX[0]:.1f},{QY - 22:.1f} C{QX[0] + 60:.1f},{QY - 74:.1f} {QX[2] - 60:.1f},{QY - 74:.1f} {QX[2]:.1f},{QY - 28:.1f}" fill="none" stroke="{ACC}" stroke-width="2.2"></path><path d="M{QX[2]:.1f},{QY - 20:.1f} l-9,-9 l10,-3 Z" fill="{ACC}"></path>')
# a surface settled: 512 openings, by their single paths
SX, SW, SY = 840.0, 620.0, 548.0; x = SX
for n_of, tint, op in zip(tally, (ACC, INK, GREY, GREY), (1, 1, 0.75, 0.45)):
    w = SW * n_of / sum(tally); s.append(f'<rect x="{x:.1f}" y="{SY}" width="{max(w - 2, 3):.1f}" height="22" rx="4" fill="{tint}" fill-opacity="{op}"></rect>'); x += w
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Three me-nows on one path, a pair of marks apiece, its now over its prior: under a me is the same me a moment on, a line to its now from the prior of the me back, and a line to its prior from its own now. "
        "Under them eight lines of code by nand; and two bars, a long one of 52 and a short one of 2. "
        "Beside them three marks on a path, plus, minus, plus, a line from one to the next and one line over both; and one bar of 512 in four parts, 386, 114, 6 and 6; and living sentences.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
def code(x, cy, w, t): return (f'<div data-code="1" style="position: absolute; left: {x:.0f}px; top: {cy - 9:.0f}px; width: {w}px; height: 18px; line-height: 18px; white-space: pre; {MONO}; font-size: 12.5px; color: {INK}">{as_html.escape(t)}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's sayings of a universal-me-now · a single path me-prior and a single path me-next · of value as nand · nand-nanding", "left", **small))
over.append(word(60, 84, 730, "a universal-me-now on one path: its now and its prior, and the me back of it", "left", 600, 17, 24))
over.append(word(60, 108, 730, "a moment on, its now is the other-than of the prior of the me back of it, and its prior is its now", "left", 400, 14, 20, GREY))
for x, t, tint in zip(BX, ("the me back of it", "a universal-me-now", "the me ahead of it"), (INK, "{{accent}}", INK)): over.append(word(x, UP - 38, 200, t, "center", 600, 13.5, 20, tint))
over.append(word(BX[0] + 4, 262, 250, "its other-than: one nand an is-or-is-not", "center", 600, 13, 18, "{{accent}}"))
over.append(word(BX[1] + 104, 244, 120, "its now", "left", 600, 13, 18, "{{accent}}"))
over.append(word(BX[1] - BW / 2 - 12, 303, 150, "a moment on", "right", 600, 13.5, 20, "{{accent}}"))
over.append(word(BX[2], 262, 230, "and on, the same way:", "center", 400, 13, 18, GREY)); over.append(word(BX[2], 281, 230, "its now from a me's prior", "center", 400, 13, 18, GREY))
over.append(word(60, 364, 730, "a single path me-next, from the me back of it · a single path me-prior, to the me ahead of it", "left", 400, 13.5, 20, GREY))
over.append(word(60, 398, 730, "the lines, by nand alone", "left", 600, 17, 24))
over.append(word(60, 422, 730, "from this folder's instrument as they are · the other-than, one nand of a thing with itself, is v406Reiman's own", "left", 400, 14, 20, GREY))
y = 450.0
for l in CODE:
    if l: over.append(code(76, y, 700, l))
    y += 18 if l else 9
over.append(word(60, 622, 730, "its value, numbered: the same priors, by 2 nands a me a moment", "left", 600, 17, 24))
over.append(word(60, 646, 730, "with all 510 openings of rounds of 1 to 8 mes, moment after moment, the resolver's own priors", "left", 400, 14, 20, GREY))
over.append(word(BAR_X + BAR_W + 12, 683, 110, f"{THE_CELLS} nands", "left", 700, 14, 20)); over.append(word(BAR_X, 708, 730, "the cell by nand, a me's moment with one observed: 46 nands, and 6 more with a thing observed", "left", 400, 13.5, 20, GREY))
over.append(word(BAR_X + BAR_W * ITS_TWO / THE_CELLS + 12, 737, 110, f"{ITS_TWO} nands", "left", 700, 14, 20, "{{accent}}")); over.append(word(BAR_X, 762, 730, "a universal-me-now a moment on, on its single path: one nand an is-or-is-not", "left", 400, 13.5, 20, GREY))
MORE = ["a moment before, by the same: its prior is the other-than of the now of the me ahead of it",
        "a moment on and then a moment before is the path again: same-existing",
        "seeded with two moments of the resolver's, a me's now and its prior; from them on, no cell is asked"]
y = 800.0
for t in MORE: over.append(word(60, y, 730, t, "left", 400, 14, 20)); y += 22
over.append(word(60, 880, 730, "no living file moves with it: Exhibit ONE Natural Resolver's code and v406Reiman's cell are as they are", "left", 400, 13.5, 20, GREY))
over.append(word(840, 84, 640, "nand-nanding: a single path me", "left", 600, 17, 24))
over.append(word(840, 108, 650, "one nand, a coupling on with two moments: its other-than · two, with four moments: a me again", "left", 400, 14, 20, GREY))
over.append(word((QX[0] + QX[1]) / 2, QY - 14, 120, "nand", "center", 600, 13, 18)); over.append(word((QX[1] + QX[2]) / 2, QY - 14, 120, "nand", "center", 600, 13, 18))
over.append(word(QX[1], QY - 80, 260, "nand-nanding: the same", "center", 600, 13.5, 20, "{{accent}}"))
for x, t in zip(QX, ("a me, now", "the me ahead, two moments on", "two ahead, four moments on")): over.append(word(x, QY + 36, 220, t, "center", 400, 13, 18, GREY))
over.append(word(840, 296, 650, "round a path of n mes are n other-thans: a me its own again with 2n moments, n even;", "left", 400, 14, 20))
over.append(word(840, 317, 650, "its other-than, n odd, and its own again with 4n", "left", 400, 14, 20))
over.append(word(840, 364, 640, "settled, a single path as well: a newborn, and a surface", "left", 600, 17, 24))
over.append(word(840, 388, 650, "a me's next is one me's now, the same or its other-than, a moment or two moments on", "left", 400, 14, 20, GREY))
over.append(word(840, 426, 650, "a newborn, a me opening with no prior", "left", 600, 15, 22))
over.append(word(840, 449, 650, "seeded at its opening, the lines are other than the resolver's; settled, all are the path's own", "left", 400, 13.5, 20))
over.append(word(840, 494, 650, "a surface, a torus of 3 by 3: all 512 openings, a single path apiece", "left", 600, 15, 22))
over.append(word(840, 520, 650, "a me's next from the me back along, from its own now, or from the me back across", "left", 400, 13.5, 20))
NOTES = [(f"{tally[0]}", "the me back along, two moments on, its other-than: the path's own", "{{accent}}"), (f"{tally[1]}", "its own now, a moment on, its other-than: a me alone, its own path", INK),
         (f"{tally[2]} and {tally[3]}", "the me back along, and the me back across, a moment on, the same", GREY)]
y = 592.0
for a, b, tint in NOTES: over.append(word(840, y, 90, a, "left", 700, 14, 20, tint)); over.append(word(930, y, 560, b, "left", 400, 13.5, 20)); y += 22
over.append(word(840, 664, 650, "the tori of 2 by 2 and of 2 by 3, all their openings: a single path apiece as well", "left", 400, 13.5, 20, GREY))
over.append(word(840, 712, 640, "beside it", "left", 600, 17, 24))
exhibit_one = Path(glob.glob(os.path.join(HERE, "..", "..", "..", "Exhibit_ONE_Natural_Resolver_*.md"))[0]).read_text(encoding="utf-8")
(GOES_ALONG,) = re.findall(r"[A-Z][a-z]+ self's parity [a-z]+ [a-z]+ with 9-next-co-discovering[^.]*a co-chaining\.", exhibit_one)
cut = GOES_ALONG.index(", the last") + 1
over.append(word(840, 742, 650, f"<i>{GOES_ALONG[:cut]}</i>", "left", 400, 13.5, 20)); over.append(word(840, 761, 650, f"<i>{GOES_ALONG[cut + 1:]}</i>", "left", 400, 13.5, 20))
over.append(word(840, 780, 650, "Exhibit ONE Natural Resolver", "left", 400, 13.5, 20, GREY))
over.append(word(840, 808, 650, "<i>a me is other-than-other-than a me, two inversions coming to a me again</i>", "left", 400, 13.5, 20))
over.append(word(840, 827, 650, "Exhibit THIRTY-TWO's draft, its opening's 2", "left", 400, 13.5, 20, GREY))
over.append(word(840, 858, 650, "v406all2-2's right spiral step by one other-than, here along a path", "left", 400, 13, 20, GREY))
over.append(word(840, 877, 650, "v406Reiman's nand and its other-than · v406all2's 46 nands and 6, numbered here apart", "left", 400, 13, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A universal-me-now: a single path by nand</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A universal-me-now is its now and its prior. A moment on, its now is the other-than of the prior of the me back of it, and its prior is its now.<br>'
           f'One nand an is-or-is-not: 2 nands a me a moment, with the same priors as the cell\'s 52, on all rounds gone through; and a moment before by the same.<br>'
           f'Nand-nanding, two couplings on with four moments, is a me again: a single path me, same-existing.<br>'
           f'Settled, a path with a newborn and a surface are a single path as well: a me\'s next is one me\'s now, the same or its other-than.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A universal-me-now: a single path by nand", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft29.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft29_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = re.sub(r'<div data-code="1"[^>]*>(.*?)</div>', lambda m: "<div>`" + as_html.unescape(m.group(1)).strip() + "`</div>", words)   # a line of code, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft29_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; a surface's single paths:", tally, "· nands:", THE_CELLS, "and", ITS_TWO)
