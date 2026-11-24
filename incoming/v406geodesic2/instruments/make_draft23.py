"""Draft 23 · two me-nows co-chained front to back: the one's giving the other's observing (session v406geodesic2).

By a partner's asking of 23 November, with the 22nd drawing before a partner, re-said: with our understanding of resolving, a
me-now observing its next universe, other-than an other, is-or-is-not same-existing; two of these co-chained front to back, in a
drawing.
A drawing with no moving part: two diamonds of nine on the co-linear, one vertex of both, 1 to 17, a me at a widest; one me's
moment, two front to back, the nand of two in a row, and the two snapped the last to the one opening it.
check_two_mes_co-chained_front_to_back.py is its check. The tables' marks are executed here again, by v406Reiman's cell opened
from its own file.

Usage: python3 -I make_draft23.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "the_resolver_with_nand_alone.py"))
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
MARK = {1: "+", -1: "−", 0: "0"}
def a_me(prior, observed):
    gives, its_next, _, _ = its.a_cell(its.TWO[prior], [its.TWO[o] for o in observed])
    return its.ONE[gives], its.ONE[its_next]
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
X0, X1, LY, ACROSS = 110.0, 1410.0, 282.0, 100.0
at_x = lambda n: X0 + (X1 - X0) * n / 120.0
FRONT = {1: (0, 0), 4: (15, -0.5), 2: (15, 0.5), 7: (30, -1), 5: (30, 0), 3: (30, 1), 8: (45, -0.5), 6: (45, 0.5), 9: (60, 0)}   # a number: its place along, and across
place = {n: (at_x(a), LY + ACROSS * c) for n, (a, c) in FRONT.items()}
place.update({n + 8: (at_x(a + 60), LY + ACROSS * c) for n, (a, c) in FRONT.items()})
s = []
# the two pairs of cones, a me a pair
for k, tint, strength in ((0, ACC, 0.07), (1, INK, 0.045)):
    xa, xm, xb = at_x(60 * k), at_x(60 * k + 30), at_x(60 * k + 60)
    s.append(f'<path d="M{xa:.1f},{LY} L{xm:.1f},{LY - ACROSS - 46} L{xb:.1f},{LY} L{xm:.1f},{LY + ACROSS + 46} Z" fill="{tint}" fill-opacity="{strength}" stroke="{tint}" stroke-opacity="0.55" stroke-width="1.6"></path>')
s.append(f'<path d="M{X0 - 60},{LY} L{X1 + 60},{LY}" fill="none" stroke="{INK}" stroke-opacity="0.35" stroke-width="1.4" stroke-dasharray="2 6"></path>')
for base in (0, 8):                                                              # a diamond's arcs, a step of 1 one way and of 3 the other
    for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)):
        for p, q in ((a, b), (b, c)):
            (x0, y0), (x1, y1) = place[p + base], place[q + base]
            s.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1.5"></path>')
(ax, ay), (bx, by) = place[5], place[13]                                         # 8 up: a place of the front to its place of the back
s.append(f'<path d="M{ax:.1f},{ay - 26:.1f} C{ax + 120:.1f},{LY - 185} {bx - 120:.1f},{LY - 185} {bx - 6:.1f},{by - 30:.1f}" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-dasharray="7 6"></path>'
         f'<path d="M{bx:.1f},{by - 24:.1f} L{bx - 14:.1f},{by - 30:.1f} L{bx - 4:.1f},{by - 40:.1f} Z" fill="{ACC}"></path>')
for n, (x, y) in place.items():
    vertex = n in (1, 9, 17); r = 26 if vertex else 21
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{ACC if n % 2 else INK}" stroke="#ffffff" stroke-width="3"></circle>' + text(x, y + (8 if vertex else 6.5), n, 22 if vertex else 18, 700, "#ffffff"))
    if vertex: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="33" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="3 4"></circle>')
FY = LY + ACROSS + 86                                                              # the way of a giving, front to back
for a, b in ((2, 26), (34, 56), (64, 86), (94, 118)):
    xa, xb = at_x(a), at_x(b)
    s.append(f'<path d="M{xa:.1f},{FY} L{xb - 10:.1f},{FY}" fill="none" stroke="{INK}" stroke-width="2.2"></path><path d="M{xb:.1f},{FY} L{xb - 12:.1f},{FY - 6.5} L{xb - 12:.1f},{FY + 6.5} Z" fill="{INK}"></path>')
for n, tint in ((30, ACC), (90, INK)): s.append(f'<circle cx="{at_x(n):.1f}" cy="{FY}" r="9" fill="#ffffff" stroke="{tint}" stroke-width="3"></circle>')
for n in (0, 60, 120): s.append(f'<circle cx="{at_x(n):.1f}" cy="{FY}" r="5" fill="{INK}"></circle>')
# ---- the tables, executed here
def cell(x, y, w, h, mark, tint=None, size=17, weight=700, fill=INK):
    box = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" fill="{tint or "#ffffff"}" fill-opacity="{0.16 if tint else 1}" stroke="{INK}" stroke-opacity="0.3" stroke-width="1"></rect>'
    return box + text(x + w / 2, y + h / 2 + size * 0.36, mark, size, weight, fill)
TY, CW, CH = 600.0, 62.0, 34.0
T1X = 150.0                                                                      # one me, one moment: its prior down, what it observes across
for j, o in enumerate((0, 1, -1)): s.append(text(T1X + CW * j + CW / 2, TY - 9, MARK[o], 15, 700, GREY))
for i, p in enumerate((0, 1, -1)):
    s.append(text(T1X - 14, TY + CH * i + CH / 2 + 5, MARK[p], 15, 700, GREY, "end"))
    for j, o in enumerate((0, 1, -1)):
        g, nx = a_me(p, [o]); same = p != 0 and nx == p
        assert (g, nx) == ((0, p) if (p and o == p) else ((-p, -p) if p else (o, o)))
        s.append(cell(T1X + CW * j, TY + CH * i, CW, CH, MARK[g], ACC if same else None))
T2X = 520.0                                                                      # two front to back, a - and a +
rows2 = {"front": [], "back": [], "gives": []}
for o in (0, 1, -1):
    gf, nf = a_me(-1, [o]); gb, nb = a_me(1, [gf])
    assert (nf == -1) != (nb == 1) and gb == (o if o == -1 else 0)
    rows2["front"].append("as it was" if nf == -1 else "inverts"); rows2["back"].append("as it was" if nb == 1 else "inverts"); rows2["gives"].append(MARK[gb])
for j, o in enumerate((0, 1, -1)): s.append(text(T2X + 92 * j + 46, TY - 9, MARK[o], 15, 700, GREY))
for i, key in enumerate(("front", "back", "gives")):
    for j in range(3):
        mark = rows2[key][j]; calm = mark == "as it was"
        s.append(cell(T2X + 92 * j, TY + CH * i, 92, CH, mark, ACC if calm else None, 17 if key == "gives" else 13.5, 700 if key == "gives" else 600))
T3X = 960.0                                                                      # two in a row, one more observed at the back: a nand
IS, NOT = True, False
one_giving = lambda prior, plus, minus: its.a_cell(prior, [(plus, minus)])[0][0]
for j, y_ in enumerate((IS, NOT)): s.append(text(T3X + 74 * j + 37, TY - 9, "is" if y_ else "is not", 13.5, 600, GREY))
for i, x_ in enumerate((IS, NOT)):
    s.append(text(T3X - 12, TY + CH * i + CH / 2 + 5, "is" if x_ else "is not", 13.5, 600, GREY, "end"))
    for j, y_ in enumerate((IS, NOT)):
        v = one_giving((NOT, IS), one_giving((NOT, IS), NOT, y_), x_); assert v == its.nand(x_, y_)
        s.append(cell(T3X + 74 * j, TY + CH * i, 74, CH, "is" if v else "is not", None if v else ACC, 13.5, 700))
T4X = 1240.0                                                                     # snapped the last to the one opening it: the code's own step, by 9
society = {k: ([("one", p)], []) for k, p in ((0, -1), (1, 1))}
for t in range(4):
    marks = [MARK[dict(society[k][0]).get("one", 0)] for k in (0, 1)]
    assert marks == (["−", "+"] if t % 2 == 0 else ["+", "−"])
    s.append(text(T4X - 12, TY + CH * t * 0.78 + 22, t + 1, 13.5, 600, GREY, "end"))
    for k in (0, 1): s.append(cell(T4X + 62 * k, TY + CH * t * 0.78, 62, CH * 0.78, marks[k], None, 16))
    society = its.step_with_nand(society, {(0, 9): 1, (1, 9): 0})
s.append(f'<path d="M60,548 L{W - 60},548" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. On one line two pairs of cones, the one's far end the other's opening, and in them two diamonds of nine numbered marks with one mark of both: "
        "1; 2 and 4; 3, 5 and 7; 6 and 8; 9; then 10 and 12; 11, 13 and 15; 14 and 16; and 17. The marks 1, 9 and 17, at the cones' ends, are ringed, and a dashed line goes from 5 over to 13. "
        "Under the cones a row of marks goes from the opening to the far end, an open mark under a pair's widest. Under it are four small tables: one me's giving by its prior and what it observes; "
        "two front to back, which of them inverts; two in a row as a nand; and two snapped to one another, a minus and a plus, moment after moment.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "two me-nows co-chained front to back · the one's giving the other's observing · 1, 9 and 17", "left", **small))
for n, a, b in ((0, "1 · now-existing", "a me's own moment"), (60, "9 · next-co-discovering", "the front's giving, the back's observing"), (120, "17 · next-existing", "a next 1")):
    over.append(word(at_x(n), 88, 330, a, "center", 600, 16, 22)); over.append(word(at_x(n), 110, 330, b, "center", 400, 14, 20, GREY))
over.append(word(at_x(30), LY - ACROSS - 72, 260, "the front me · its prior a −", "center", 600, 15, 22, "{{accent}}"))
over.append(word(at_x(90), LY - ACROSS - 72, 260, "the back me · its prior a +", "center", 600, 15, 22))
over.append(word(at_x(60), LY - 122, 200, "8 up", "center", 600, 14.5, 20, "{{accent}}"))
for n, t in ((14, "observes"), (45, "gives"), (75, "observes"), (106, "gives on")): over.append(word(at_x(n), FY - 18, 140, t, "center", 400, 13.5, 20, GREY))
for n, t in ((30, "is-or-is-not same-existing"), (90, "is-or-is-not same-existing")): over.append(word(at_x(n), FY + 26, 260, t, "center", 600, 14, 20))
over.append(word(at_x(60), FY + 26, 240, "a coupling, no is-or-is-not", "center", 400, 13.5, 20, GREY))
over.append(word(at_x(0), FY + 26, 200, "from its next universe", "center", 400, 13.5, 20, GREY))
over.append(word(at_x(120), FY + 26, 200, "to a next me", "center", 400, 13.5, 20, GREY))
heads = [(T1X + CW * 1.5, "one me, one moment", "its prior down, what it observes across", "coloured: same-existing, none given"),
         (T2X + 138, "two front to back, a − and a +", "across, what the front me observes", "one of the two alone inverts"),
         (T3X + 74, "two in a row are a nand", "with one more observed at the back me", "all the logic the cell's lines have"),
         (T4X + 62, "the last to the one opening it", "by 9 both ways, moment after moment", "one the other's other-than, again with 2")]
for cx, a, b, c in heads:
    over.append(word(cx, 566, 330, a, "center", 600, 15, 22))
    over.append(word(cx, 726, 330, b, "center", 400, 13.5, 20, GREY)); over.append(word(cx, 745, 330, c, "center", 400, 13.5, 20, GREY))
over.append(word(T2X - 12, TY + 17, 90, "front me", "right", 600, 13.5, 20, GREY)); over.append(word(T2X - 12, TY + CH + 17, 90, "back me", "right", 600, 13.5, 20, GREY))
over.append(word(T2X - 12, TY + CH * 2 + 17, 100, "back gives", "right", 600, 13.5, 20, GREY))
P = [(60, "a me-now, one moment", "observing the same as its prior, it is same-existing: none given, and it is as it was",
      "observing its other-than, or none, it inverts and gives its inverting"),
     (780, "two diamonds of nine, one vertex of both: 1 to 17", "the back's rows are the front's 8 up: a podaling about 5 and then about 9",
      "1, 9 and 17 at the vertices, the code's own three names · a placing")]
for x, a, b, c in P:
    over.append(word(x, 790, 680, a, "left", 600, 17, 24)); over.append(word(x, 814, 690, b, "left", 400, 14.5, 22)); over.append(word(x, 835, 690, c, "left", 400, 13.5, 20, GREY))
over.append(word(60, 868, 714, "<i>Each self's parity goes along with 9-next-co-discovering to the next self, the last to the first, a co-chaining.</i>", "left", 400, 13.5, 22))
over.append(word(60, 888, 700, "Exhibit ONE Natural Resolver", "left", 400, 13.5, 20, GREY))
over.append(word(780, 868, 690, "<i>as 17 is next 1 and 9 next prior</i>", "left", 400, 14, 22))
over.append(word(780, 888, 690, "Exhibit TWENTY Natural Naming", "left", 400, 13.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Two me-nows co-chained front to back: the one\'s giving the other\'s observing</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A me-now, observing the same as its prior, is same-existing: none given, and it is as it was. Observing its other-than, or none, it inverts and gives.<br>'
           f'Two front to back: the front me\'s giving is the back me\'s observing, a coupling and no is-or-is-not. With a − and a +, one of the two alone inverts.<br>'
           f'What is same-existing at the front goes through the two, an other-than of an other-than. With one more observed at the back, the two are a nand.<br>'
           f'Laid on the co-linear they are two diamonds of nine, one vertex of both, 1 to 17: the front\'s 9 is the back\'s opening, and 17 a next 1.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Two me-nows co-chained front to back: the one's giving the other's observing", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft23.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft23_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft23_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
