"""Draft 30 · nand-nanding, its is and its is-not explored forward (session v406geodesic2).

By a partner's word of 24 November, with the 29th drawing before a partner, re-said: to go on exploring forward into the is and
the is-not; one of the two is incohering; and then to go on resolving forward.
A drawing with no moving part: two nands in a row by what they are of; the 29th drawing's concern with its two sides executed
forward, the one cohering and the other incohering; an all of a path's links; and, the same way, the 25th drawing's concern of a
corus at a place.
check_nand-nanding_its_is_and_its_is-not_explored_forward.py is its check. The marks and numbers drawn here are executed here
again, by v406Reiman's nand, its other-than, its both and its step, opened from their own file.

Usage: python3 -I make_draft30.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from itertools import product
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
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
nand, other_than, both, TWO, ONE, S = its.nand, its.other_than, its.both, its.TWO, its.ONE, "one"
def moments(couplings, priors, how_many):
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: dict(pr).get(S, 0) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
# the numbers drawn, executed here again
OF_TWO = [lambda a, b: nand(nand(a, b), nand(a, b)), lambda a, b: nand(nand(a, a), nand(b, b)), lambda a, b: nand(nand(a, b), a),
          lambda a, b: nand(nand(a, b), b), lambda a, b: nand(nand(a, a), b), lambda a, b: nand(nand(b, b), a)]
def of_two(f, p, q): return (f(TWO[p][0], TWO[q][0]), f(TWO[p][1], TWO[q][1]))
AN_ALL = {(p, q): ONE[of_two(OF_TWO[0], p, q)] for p in (1, -1) for q in (1, -1)}
assert AN_ALL == {(1, 1): 1, (1, -1): 0, (-1, 1): 0, (-1, -1): -1}
ABOUT = [(0, 0), (0, -1), (-1, 0), (-1, -1), (1, 0), (1, -1)]
rounds = {n: [moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 4 * n + 8) for op in product((1, -1), repeat=n)] for n in range(3, 9)}
def a_parity_at_all_moments(f, u, v):
    return all(of_two(f, ms[t + u[1]][(a + u[0]) % n], ms[t + v[1]][(a + v[0]) % n]) not in ((False, False), (True, True)) for n, g in rounds.items() for ms in g for t in range(2, 4 * n + 4) for a in range(n))
WAYS = [(f, u, v) for f in OF_TWO for u in ABOUT for v in ABOUT if u != v]
assert len(WAYS) == 180 and not any(a_parity_at_all_moments(*w) for w in WAYS)
N, ME, NOW = 9, 4, 18
ms9 = moments(as_it_is.spiral_couplings(N), dict(enumerate((1, 1, 1, -1, 1, -1, -1, 1, -1))), 44)
ALONG = [ms9[NOW + 2 * j][(ME + j) % N] for j in range(7)]
assert all(ALONG[j] == (-1) ** j * ALONG[0] for j in range(7))
def with_all(ms, n, t): return all(ms[t + 1][a] == -ms[t - 1][(a - 1) % n] for a in range(n))
A_ROUND = [with_all(ms9, N, t) for t in range(1, 13)]
born = moments(as_it_is.spiral_couplings(4), dict(enumerate((1, 0, -1, 0))), 40)
A_NEWBORN = [with_all(born, 4, t) for t in range(1, 13)]
assert all(A_ROUND) and not all(A_NEWBORN[:2]) and all(A_NEWBORN[4:])

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def way(x0, y0, x1, y1, tint, wide=2.0, short=0.0, head=8.0):
    L = math.hypot(x1 - x0, y1 - y0); tx, ty = (x1 - x0) / L, (y1 - y0) / L; x0, y0 = x0 + tx * short, y0 + ty * short; x1, y1 = x1 - tx * short, y1 - ty * short; nx, ny = -ty, tx
    return (f'<path d="M{x0:.1f},{y0:.1f} L{x1 - tx * head * 0.8:.1f},{y1 - ty * head * 0.8:.1f}" fill="none" stroke="{tint}" stroke-width="{wide}"></path>'
            f'<path d="M{x1:.1f},{y1:.1f} L{x1 - tx * head + nx * head * 0.5:.1f},{y1 - ty * head + ny * head * 0.5:.1f} L{x1 - tx * head - nx * head * 0.5:.1f},{y1 - ty * head - ny * head * 0.5:.1f} Z" fill="{tint}"></path>')
def a_mark(x, y, v, r=12, tint=INK):
    if v > 0: return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{tint}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, y + 5, MARK[v], 14, 700, "#ffffff")
    if v < 0: return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r - 1}" fill="#ffffff" stroke="{tint}" stroke-width="2.2"></circle>' + text(x, y + 5, MARK[v], 14, 700, tint)
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r - 1}" fill="#ffffff" stroke="{GREY}" stroke-width="1.6" stroke-dasharray="3 3"></circle>' + text(x, y + 5, MARK[v], 13, 700, GREY)
s = []
# of a thing with itself: a +, a nand, a −, a nand, a +
for i, v in enumerate((1, -1, 1)): s.append(a_mark(560 + 90 * i, 160, v, 12, ACC))
s.append(way(560, 160, 650, 160, ACC, 2.0, 16) + way(650, 160, 740, 160, ACC, 2.0, 16))
# of two things, an all: four cases
for i, ((p, q), r) in enumerate(AN_ALL.items()):
    x = 548 + 62 * i; s.append(a_mark(x - 11, 228, p, 9) + a_mark(x + 11, 228, q, 9) + f'<path d="M{x:.1f},239 L{x:.1f},249" fill="none" stroke="{GREY}" stroke-width="1.4"></path>' + a_mark(x, 262, r, 10))
# of links in a row: an all
for i in range(6): s.append(f'<rect x="{548 + 30 * i}" y="312" width="22" height="22" rx="5" fill="{INK}"></rect>')
s.append(way(732, 323, 760, 323, INK, 2.0, 2) + f'<rect x="764" y="312" width="22" height="22" rx="5" fill="{ACC}"></rect>')
# its is, along the path
PX, PY = 100.0, 652.0
for j, v in enumerate(ALONG):
    x = PX + 105 * j; s.append(a_mark(x, PY, v, 14, ACC if j % 2 == 0 else INK))
    if j < 6: s.append(way(x, PY, x + 105, PY, INK, 1.8, 18))
    s.append(text(x, PY + 34, "now" if j == 0 else f"{2 * j} on", 12, 700 if j == 0 else 600, INK if j == 0 else GREY))
for j in (0, 2, 4):
    x0, x1 = PX + 105 * j, PX + 105 * (j + 2)
    s.append(f'<path d="M{x0:.1f},{PY - 18:.1f} C{x0 + 40:.1f},{PY - 56:.1f} {x1 - 40:.1f},{PY - 56:.1f} {x1:.1f},{PY - 22:.1f}" fill="none" stroke="{ACC}" stroke-width="2"></path><path d="M{x1:.1f},{PY - 16:.1f} l-8,-8 l9,-2 Z" fill="{ACC}"></path>')
# an all of its links, moment after moment
for row, (ys, strip) in enumerate(((842.0, A_ROUND), (870.0, A_NEWBORN))):
    for t, ok in enumerate(strip):
        dashes = "" if ok else 'stroke-dasharray="3 3"'
        s.append(f'<rect x="{230 + 30 * t}" y="{ys - 11}" width="22" height="22" rx="5" fill="{INK if ok else "#ffffff"}" stroke="{INK}" stroke-width="1.6" {dashes}></rect>')
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Three rows of two nands in a row: of a thing with itself, a plus to a minus to a plus; of two things, an all with four cases, a plus with a plus a plus, a minus with a minus a minus, and a 0 with the two other; of links in a row, six marks to one. "
        "Under them seven marks along a path, plus and minus in turn, a line from a mark to the next and a line over two; and two rows of twelve marks, a path's links with all, a row all dark, and a row with two open marks ahead of ten dark. "
        "Beside them a concern with its is, its is-not and its resolving on; a second concern the same way; and a living sentence.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's word · exploring forward into the is and the is-not, one of them incohering, and resolving on · nand-nanding", "left", **small))
over.append(word(60, 84, 730, "two nands in a row, by what they are of", "left", 600, 17, 24))
over.append(word(60, 108, 730, "v406Reiman's nand, its other-than and its both · a parity is two is-or-is-nots", "left", 400, 14, 20, GREY))
KINDS = [(150, "of a thing with itself", "an other-than of an other-than:", "the thing again"), (226, "of two things", "an all, the code's both: the thing again with", "the two the same, and a 0 with two other-thans"),
         (312, "of links in a row", "an all, link after link:", "with all alone")]
for y, a, b, c in KINDS:
    over.append(word(60, y, 470, a, "left", 600, 15.5, 22)); over.append(word(60, y + 22, 470, b, "left", 400, 14, 20)); over.append(word(60, y + 42, 470, c, "left", 400, 14, 20))
over.append(word(60, 398, 730, "its is-not, explored forward: of two me-nows · incohering", "left", 600, 17, 24))
over.append(word(60, 422, 730, "any two of the six me-nows about a me, with any form of the six of two nands in a row: 180 ways", "left", 400, 14, 20, GREY))
NOT = ["none is a parity at all moments, and none is a single path me", "with two other-thans an all is neither a + nor a −, and an either both together: a 0",
       "of a me's prior and what surfaces it is the same now, or neither: one is-or-is-not of two, a co-parity"]
y = 452.0
for i, t in enumerate(NOT): over.append(word(60, y, 730, t, "left", 600 if i == 0 else 400, 14, 20)); y += 22
over.append(word(60, 538, 730, "its is, explored forward: of a me-parity with itself, along the path · cohering", "left", 600, 17, 24))
over.append(word(60, 562, 730, "a nand a coupling, with two moments · an even number, a me again · an odd number, its other-than", "left", 400, 14, 20, GREY))
for j in (0, 2, 4): over.append(word(PX + 105 * (j + 1), PY - 62, 160, "nand-nanding", "center", 600, 12.5, 18, "{{accent}}"))
over.append(word(60, 716, 730, "a path closes by nand-nanding: n mes even, a me its own again with 2n moments; n odd, twice round, with 4n", "left", 400, 14, 20))
over.append(word(60, 737, 730, "a path of one, a me after itself: its own again with four moments", "left", 400, 13.5, 20, GREY))
over.append(word(60, 778, 730, "an all of its links: a path, with all", "left", 600, 17, 24))
over.append(word(60, 802, 730, "a link: a me's now a moment on, the other-than of the prior of the me back of it · v406all2's both, link after link", "left", 400, 14, 20, GREY))
over.append(word(60, 842, 160, "a round of nine", "left", 600, 13.5, 20)); over.append(word(60, 870, 160, "with a newborn", "left", 600, 13.5, 20))
over.append(word(604, 842, 190, "with all, at all moments", "left", 400, 13.5, 20)); over.append(word(604, 870, 190, "with all, from its settling", "left", 400, 13.5, 20))
over.append(word(410, 895, 360, "moments 1 to 12", "center", 400, 12, 18, GREY))
over.append(word(840, 84, 640, "the 29th drawing's concern, its two sides explored forward", "left", 600, 17, 24))
over.append(word(840, 108, 650, "a partner's word: one of the two is incohering, and resolving goes on with its other", "left", 400, 14, 20, GREY))
ROWS = [("its is", "{{accent}}", ["nand-nanding is an other-than of an other-than along the path:", "a me two couplings on, with four moments, a me again"], "cohering: at all moments, on all rounds, and it is a path's own closing"),
        ("its is-not", INK, ["nand-nanding is an all of two me-nows, the code's both"], "incohering as a single path me: a me-now with the two the same alone, and a 0 with other-thans"),
        ("resolving on", "{{accent}}", ["nand-nanding is a single path me two ways, and the two are one:", "of a me-parity with itself, two couplings on, a me again;", "of a path's links, link after link, the path with all"], "of two me-nows it is a co-parity, the same now or neither: an is-or-is-not, and no path")]
y = 148.0
for a, tint, lines_, verdict in ROWS:
    over.append(word(840, y, 640, a, "left", 700, 15.5, 22, tint)); y += 23
    for t in lines_: over.append(word(840, y, 650, t, "left", 400, 14, 20)); y += 21
    over.append(word(840, y, 650, verdict, "left", 400, 13.5, 20, GREY)); y += 34
over.append(word(840, 462, 640, "the same way, an earlier concern: at a place, a corus", "left", 600, 17, 24))
over.append(word(840, 486, 650, "the 25th drawing's · by sentences found and a line executed · this session's judging", "left", 400, 13.5, 20, GREY))
CORUS = [("its is", INK, ["at a place is a corus"], "incohering: a corus is an inverting, of a me-parity; a place, by a partner's words, is a me"),
         ("its is-not", "{{accent}}", ["a corus is a me's own inverting, and at a place has a name of its own"], "going on: in resolving the resolver alone has a place, and the resolver is the me"),
         ("resolving on", "{{accent}}", ["at a place is a me, no parity; a corus is its own inverting,", "+ to −, and neither is its place"], "executed: a me's own inverting, one nand of its own me-parity, at all odd moments of a path")]
y = 524.0
for a, tint, lines_, verdict in CORUS:
    over.append(word(840, y, 640, a, "left", 700, 15.5, 22, tint)); y += 23
    for t in lines_: over.append(word(840, y, 650, t, "left", 400, 14, 20)); y += 21
    over.append(word(840, y, 650, verdict, "left", 400, 13.5, 20, GREY)); y += 32
over.append(word(840, 790, 640, "beside it", "left", 600, 17, 24))
over.append(word(840, 818, 650, "<i>A corus is a self's own inverting, + to −, and neither is its place.</i>", "left", 400, 14, 20))
over.append(word(840, 837, 650, "Exhibit FOUR Natural Mathematics", "left", 400, 13.5, 20, GREY))
over.append(word(840, 864, 650, "v406all2 at the exchange: nandnanding as both, two nands in a row, with all alone", "left", 400, 13, 20, GREY))
over.append(word(840, 883, 650, "v406all2-2 at the exchange: a co-parity, two parities the same, now; and a moment between", "left", 400, 13, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Nand-nanding, its is and its is-not explored forward</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Two nands in a row of a thing with itself are the thing again: along the path a me two couplings on, with four moments, is a me again. Cohering.<br>'
           f'Two nands in a row of two me-nows, in all their forms, are a 0 at some moment: none is a single path me. Incohering.<br>'
           f'Resolving on: an all of two is the same now or neither, a co-parity; and an all of a path\'s links is the path, with all.<br>'
           f'The same way, an earlier concern: at a place is a me, no parity, and a corus is its own inverting.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Nand-nanding, its is and its is-not explored forward", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft30.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft30_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft30_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; along the path:", "".join(MARK[v] for v in ALONG), "· a newborn's links with all:", "".join("1" if x else "0" for x in A_NEWBORN))
