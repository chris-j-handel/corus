"""v410illustrating · the maker of the 62nd drawing: Diamond of Nine about Its 5.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft62.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The fourth figure of the reduced set, one drawing beside the seven it gathers, the 18th to the 24th. By a partner's
aiming of 27 November it goes on showing how the +1s are living in the seams of natural torusing.
Its check is opened and executed here, and no drawing is made with an is-not.

Its placings, no execution says them: its five parts and its table side by side; the diamond laid with 1 and 9 on the
co-linear; a right spiral step as four arcs about it; a name's own naming under its cell; six diamonds as outlines
on the co-linear; the tints of a corner, a side's middle and its 5.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_62", os.path.join(HERE, "check_diamond_of_nine_about_its_5.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"
names, kind = own["names"], own["kind"]
core = lambda n: re.sub(r"^\d+-(now|next)-", "", names[n])

W, H = 1520, 1150
GREY, SLATE, PALE = "#4a5160", "#475569", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
s, over = [], []

def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def dot(x, y, r, fill, stroke=INK, sw=1.2, op=1): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"></circle>'
def tint(n):                                                              # a cell's tint by what crosses its number round ten
    n = n % 10
    if n in (1, 3, 7, 9): return ACC, 0.24
    if n == 5: return SLATE, 0.26
    return "#ffffff", 1
def at(n): r, col = c.cell(n); return r + col, col - r                   # a cell of the diamond: along the co-linear, and across it

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "62 · figure 4 of twelve, the diamond of nine about its 5 · it gathers the 18th to the 24th drawings · its prior figure: cones of 30, the 61st · "
                 "its next figures: rows of 30, and a me beside an other", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 840, "Nine is three by three: eight round its middle and 1, a seam of eight and its +1.", size=20, h=28))
over.append(word(60, 108, 840, "Its middle row is 3, 5 and 7: a centre's square is a seam's +1, at 9, 25 and 49.", size=20, h=28))
over.append(word(60, 138, 840, "By 3 round ten is a right spiral step about its 5; two steps, a podaling: 10 less.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names: on the co-linear, at a diamond's widest, and on its sides",
                       "Natural Numbers · seams of one eight; a +1 between a centre's square and its prior by its next",
                       "Exhibit THIRTY, Natural Naming · a right spiral step, a pair (x, y) onto (y, −x); podaling",
                       "Natural Illustrating · a local nine, its middle 1, beside a partner's nine, its middle 5")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · a diamond of nine about its 5 =================
CX, CY, S = 270.0, 404.0, 60.0
P = lambda n: (CX + (at(n)[0] - 2) * S, CY - at(n)[1] * S)
over.append(word(60, 196, 420, "1 · a diamond of nine about its 5", weight=600, size=15))
for x, n_, t in ((70, 1, "a corner: by none of 2 and 5"), (270, 2, "a side's middle: by 2"), (418, 5, "its 5")):
    f_, op = tint(n_); s.append(dot(x, 220, 6.2, f_, INK, 1.2, op)); over.append(word(x + 12, 220, 180, t, size=12, color=GREY))
over.append(word(60, 240, 430, "a line through its 5: a number and its podal · an arc: a right spiral step", size=11.6, h=14, color=GREY))
s.append(f'<path d="M{CX - 2 * S:.1f},{CY:.1f} L{CX:.1f},{CY - 2 * S:.1f} L{CX + 2 * S:.1f},{CY:.1f} L{CX:.1f},{CY + 2 * S:.1f} Z" fill="{ACC}" fill-opacity="0.05" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.2"></path>')
for a, b in ((1, 3), (4, 6), (7, 9), (1, 7), (2, 8), (3, 9)):           # the three by three's own lines: a step of 1 one way, a step of 3 the other
    (x1, y1), (x2, y2) = P(a), P(b)
    s.append(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.22" stroke-width="1"></path>')
for a, b in ((3, 7), (2, 8), (4, 6)):                                    # a line through its 5: a number and its podal, 10 less
    (x1, y1), (x2, y2) = P(a), P(b)
    s.append(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" fill="none" stroke="{ACC}" stroke-opacity="0.75" stroke-width="1.5" stroke-dasharray="3 4"></path>')
s.append(f'<path d="M{CX - 2 * S - 46:.1f},{CY:.1f} L{CX + 2 * S + 62:.1f},{CY:.1f}" fill="none" stroke="{INK}" stroke-width="1.5"></path>')
s.append(f'<path d="M{CX + 2 * S + 62:.1f},{CY:.1f} l-9,-4.5 l0,9 Z" fill="{INK}"></path>')
over.append(word(60, CY - 12, 90, "the co-linear", size=11, h=14, color=GREY))
RA, GAP = 2 * S + 26, 18
for a0 in (180, 90, 0, -90):                                             # a right spiral step: a corner onto its next, 1 onto 3, 3 onto 9, 9 onto 7, 7 onto 1
    t0, t1 = math.radians(a0 - GAP), math.radians(a0 - 90 + GAP)
    x0, y0, x1, y1 = CX + RA * math.cos(t0), CY - RA * math.sin(t0), CX + RA * math.cos(t1), CY - RA * math.sin(t1)
    s.append(f'<path d="M{x0:.1f},{y0:.1f} A{RA:.1f},{RA:.1f} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="{ACC}" stroke-width="1.8"></path>')
    tx, ty = math.sin(t1), math.cos(t1); nx, ny = -ty, tx
    s.append(f'<path d="M{x1 + 2 * tx:.1f},{y1 + 2 * ty:.1f} L{x1 - 9 * tx + 4.6 * nx:.1f},{y1 - 9 * ty + 4.6 * ny:.1f} L{x1 - 9 * tx - 4.6 * nx:.1f},{y1 - 9 * ty - 4.6 * ny:.1f} Z" fill="{ACC}"></path>')
over.append(word(CX + 104, CY - 132, 150, "by 3 round ten:", size=11.4, h=14, weight=600, color=ACC))
over.append(word(CX + 104, CY - 117, 150, "a right spiral step", size=11.4, h=14, weight=600, color=ACC))
over.append(word(CX + 104, CY + 117, 130, "2, 6, 8 and 4 go round", size=11.2, h=14, color=GREY))
over.append(word(CX + 104, CY + 132, 130, "as the corners", size=11.2, h=14, color=GREY))
for n in range(1, 10):
    x, y = P(n); f_, op = tint(n)
    s.append(dot(x, y, 17, "#ffffff", "#ffffff", 0)); s.append(dot(x, y, 17, f_, INK, 2.3 if n in (1, 9) else 1.3, op))
    over.append(word(x, y, 34, str(n), "center", 600, 16, 20))
    over.append(word(x, y + 27, 8 + 6.1 * len(core(n)), core(n), "center", 400, 10.4, 13, GREY, extra="background: #ffffff; border-radius: 5px;"))

# ================= 2 · four moves round ten, about its 5 =================
over.append(word(500, 196, 480, "2 · four moves round ten, about its 5", weight=600, size=15))
over.append(word(500, 216, 480, "multiplying round ten: a cell onto a cell · a column a cell of the diamond", size=11.5, h=14, color=GREY))
MOVES = [(None, "a cell"), (1, "by 1 · as it was"), (3, "by 3 · a right spiral step"), (9, "by 9 · two: a podaling, 10 less"), (7, "by 7 · three: a step the other way")]
NX = lambda i: 716 + 30 * i
for n in range(1, 10):
    f_, op = tint(n)
    if f_ != "#ffffff": s.append(f'<rect x="{NX(n - 1) - 13}" y="230" width="26" height="98" fill="{f_}" fill-opacity="{op * 0.6:.2f}"></rect>')
for i, (k, t) in enumerate(MOVES):
    y = 241 + 19.5 * i
    over.append(word(500, y, 204, t, weight=600 if k is None else 400, size=11.6 if k else 10.6, h=15, color=GREY if k is None else INK))
    for n in range(1, 10):
        v = n if k is None else c.round_ten(k, n)
        over.append(word(NX(n - 1), y, 26, str(v), "center", 600 if (k is None or v == 5) else 400, 12, 15, GREY if k is None else INK, extra="font-variant-numeric: tabular-nums;"))
s.append(f'<path d="M500,{251} L976,{251}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
over.append(word(500, 342, 480, "four moves, 1, 3, 9 and 7: the four corners' numbers · its 5 is as it was at all four", size=11.5, h=14, color=GREY))
over.append(word(500, 358, 480, "eight go round it, two rounds of four: 1, 3, 9 and 7, the corners; 2, 6, 8 and 4, the sides", size=11.5, h=14, color=GREY))

# ================= 3 · a seam of ten, a torus of 2 by 5 =================
over.append(word(500, 390, 480, "3 · a seam of ten, a torus of 2 by 5", weight=600, size=15))
over.append(word(500, 410, 480, "a row a cell of 2 · a column a cell of 5 · a winding by +1 is through all ten", size=11.5, h=14, color=GREY))
GX, GY, CW, CH = 566, 424, 44, 27
for r in range(2):
    over.append(word(GX - 8, GY + r * CH + CH / 2, 60, ("even", "odd")[r], "right", 400, 10.8, 13, GREY))
    for q in range(5):
        n = next(k for k in range(10) if k % 2 == r and k % 5 == q)
        f_, op = tint(n) if n else ("#ffffff", 1)
        s.append(f'<rect x="{GX + q * CW}" y="{GY + r * CH}" width="{CW}" height="{CH}" fill="{f_}" fill-opacity="{op}" stroke="{INK}" stroke-width="{2.3 if n in (1, 9) else 1}"></rect>')
        over.append(word(GX + q * CW + CW / 2, GY + r * CH + CH / 2, CW, str(n), "center", 600 if n % 2 and n != 5 else 400, 12.5, 16, INK if n % 2 else "#7b8494"))
for i, (t, col) in enumerate((("four cells crossed by none:", GREY), ("the diamond's four corners", GREY), ("1, the cell of ones: the +1", INK), ("9, one before the opening: the −1", INK))):
    over.append(word(GX + 5 * CW + 12, GY + 6 + 14.5 * i, 190, t, size=10.8, h=14, color=col))
over.append(word(500, 496, 480, "the diamond's nine and an opening, 0, are the ten · a prime past 5 ends at a corner", size=11.5, h=14, color=GREY))
over.append(word(500, 513, 480, "10 less carries the +1 onto the −1, 1 onto 9, about its 5: two right spiral steps", size=11.5, h=14, color=GREY))
over.append(word(500, 530, 480, "8, 9 and 10: nine is one on from eight, 2 by 4, and one before ten, 2 by 5", size=11.5, h=14))
over.append(word(500, 547, 480, "even, odd, even: a nine between two seams, an eight's +1 and a ten's −1", size=11.5, h=14))

# ================= 4 · six diamonds on the co-linear, 1 to 49 =================
X0, U, Y0, HH = 84.0, 17.3, 718.0, 50.0
X = lambda n: X0 + U * n
over.append(word(60, 590, 920, "4 · six diamonds on the co-linear, 1 to 49: a seam, and its +1 a centre's square", weight=600, size=15))
over.append(word(60, 609, 920, "a diamond is 8 on: a vertex at 1, 9, 17, 25, 33, 41 and 49 · the front diamond, 1 to 9, and the back, 9 to 17, are with one vertex of both, and 17 is a next 1", size=11.5, h=14, color=GREY))
for j in range(6):
    a = 1 + 8 * j
    pts = f"M{X(a):.1f},{Y0:.1f} L{X(a + 4):.1f},{Y0 - HH:.1f} L{X(a + 8):.1f},{Y0:.1f} L{X(a + 4):.1f},{Y0 + HH:.1f} Z"
    s.append(f'<path d="{pts}" fill="{(ACC, SLATE)[j % 2] if j < 2 else "#ffffff"}" fill-opacity="{0.08 if j < 2 else 0}" stroke="{INK}" stroke-opacity="{0.6 if j < 2 else 0.38}" stroke-width="1.2"></path>')
s.append(f'<path d="M{X(0) - 12:.1f},{Y0} L{X(51):.1f},{Y0}" fill="none" stroke="{INK}" stroke-width="1.5"></path>')
s.append(f'<path d="M{X(51):.1f},{Y0} l-9,-4.5 l0,9 Z" fill="{INK}"></path>')
for t_ in (10, 20, 30, 40, 50):                                           # a seam of ten: a mark under the co-linear
    s.append(f'<path d="M{X(t_):.1f},{Y0} L{X(t_):.1f},{Y0 + 13}" fill="none" stroke="{SLATE}" stroke-width="2.2" stroke-linecap="round"></path>')
    over.append(word(X(t_), Y0 + 27, 22, str(t_), "center", 600, 9.8, 12, SLATE))
for e in (8, 16, 24, 32, 40, 48):                                         # a seam of eight: a mark over the co-linear
    tall = e in (8, 24, 48)
    s.append(f'<path d="M{X(e):.1f},{Y0} L{X(e):.1f},{Y0 - (HH + 24 if tall else 10)}" fill="none" stroke="{ACC}" stroke-width="{2.4 if tall else 2.2}" stroke-linecap="round" stroke-opacity="{1 if tall else 0.8}"></path>')
for j in range(6):
    a = 1 + 8 * j
    for m in range(1, 10):
        if m == 1 and j: continue
        n = m + 8 * j; dx, dy = at(m); x, y = X(a) + dx * 2 * U, Y0 - dy * HH / 2
        square = n in (9, 25, 49)
        f_, op = tint(n)
        if dy == 0 and dx in (0, 4):
            s.append(dot(x, y, 5.4, INK if square else "#ffffff", INK, 1.6))
            over.append(word(x, y + 16, 18, str(n), "center", 600, 10.4, 12, extra="background: #ffffff; border-radius: 5px;"))
        elif dy == 0:
            s.append(dot(x, y, 3.8, "#ffffff", "#ffffff", 0)); s.append(dot(x, y, 3.8, f_, INK, 1.1, op)); over.append(word(x, y - 11, 22, str(n), "center", 400, 9.6, 12, GREY))
        elif abs(dy) == 2:
            s.append(dot(x, y, 4.2, "#ffffff", "#ffffff", 0)); s.append(dot(x, y, 4.2, f_, INK, 1.1, op)); over.append(word(x, y - 12 if dy > 0 else y + 12, 22, str(n), "center", 400, 9.6, 12, GREY))
        else:
            s.append(dot(x, y, 3.2, "#ffffff", "#aab1bf", 1))
for k_, (e, m) in enumerate(((8, 3), (24, 5), (48, 7))):
    xm = min(X(e + 0.5), 978 - 62)
    over.append(word(xm, 627, 124, f"{e} · {m - 1} by {m + 1} · a seam", "center", 600, 11, 13, ACC, extra="background: #ffffff;"))
    over.append(word(xm, 641, 124, f"{e + 1} · {m} by {m} · its +1", "center", 600, 11, 13, INK, extra="background: #ffffff;"))
over.append(word(60, 792, 920, "a centre's square is a diamond's vertex: 9 one diamond on, 25 three on, 49 six on · over the co-linear a seam of eight, 8 to 48; under it a seam of ten, 10 to 50", size=11.5, h=14, color=GREY))
over.append(word(60, 809, 920, "round ten the vertices are at 1, 9, 7, 5, 3, 1 and 9: 8 on is 2 less round ten · 41 is 40 and 1, one on from both seams · 9 and 49 are an eight's +1 and a ten's −1", size=11.5, h=14, color=GREY))

# ================= 5 · a square's rounds, beside a cube's shells =================
over.append(word(60, 842, 920, "5 · a square's rounds, beside a cube's shells: a +1 at the middle of its seam", weight=600, size=15))
over.append(word(60, 864, 920, "a square: one and its rounds of 8, 16 and 24 are 1, 9, 25 and 49, an eight more a round · its seam 8, 24 and 48, and the +1 at its middle", size=12, h=15))
over.append(word(60, 882, 920, "a cube, the 60th: one and its shells of 6, 12, 18 and 24 are 1, 7, 19, 37 and 61, a six more a round · its seam of six, and the +1 on the cube's line", size=12, h=15))

# ================= the table: a name a row, its cell of a diamond =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("its cell", 198, 92, "left"), ("its podal", 290, 46, "right"), ("by 3", 340, 30, "right"),
        ("at an eight", 380, 60, "left"), ("at a ten", 446, 60, "left")]
over.append(word(TX, 196, 500, "a name a row · its cell of a diamond · its podal · at a seam", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 504},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="512" height="{RH:.1f}" fill="{PALE}"></rect>')
    ten = "its +1" if n % 10 == 1 else "the seam" if n % 10 == 0 else "its −1" if n % 10 == 9 else ""
    cells_ = [str(n), names[n], kind(n), str(10 - n if n <= 9 else 26 - n), str(c.round_ten(3, n)) if n <= 9 else "", c.at_a_seam_of_8(n), ten]
    for (t, x, w_, al), v in zip(cols, cells_):
        bold = t in ("n", "its name, Exhibit ONE's own", "at an eight", "at a ten")
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if bold else 400, 11.2, 16, extra="font-variant-numeric: tabular-nums;"))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 504},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its cell: of the front diamond, 1 to 9, or of the back, 9 to 17; 9 is one vertex of both",
                       "its podal: about its diamond's middle, 10 less about 5, and 26 less about 13",
                       "by 3: a right spiral step round ten, from 1 to 9",
                       "at an eight, at a ten: one on from a seam, its +1; one before it, its −1")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= found, and what this drawing leaves with the seven =================
FX, FY = 1004, 640
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the seven", weight=600, size=15))
FOUND = [("a centre's square is a seam's +1, and a diamond's vertex", ["3 by 3, 5 by 5 and 7 by 7 are 9, 25 and 49, one on from 8, 24 and 48: 1, 3 and 6 diamonds on"]),
         ("Exhibit ONE's names, by their cells of a diamond", ["on the co-linear, existing, co-existing, co-discovering, discovering and existing; at a widest,", "the four of observing; on a side, four of possibling and four of same-existing"]),
         ("a middle and a seam, said more ways than one, not one yet", ["a middle: with nothing at it, Natural Numbers; with 1, a local nine; with 5, a partner's nine", "a seam: a centre's prior by its next, Natural Numbers; a torus's closing, as the 60th's six"]),
         ("it is no method of a prime's existing", ["a prime past 5 ends at a corner; 21, 27, 33 and 39 do too, and 9, 25 and 49 are no primes"]),
         ("with the seven drawings, as they were", ["the 18th's ten in four rows; the 20th's two closings; the 21st's six orders and its gyroscope;", "the 22nd's six orientations; the 23rd's two me-nows; the 24th's three fours and a one"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">Diamond of Nine about Its 5</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Podaling about 5 by Two Right Spiral Steps, a Centre\'s Square a Seam\'s +1</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "Nine is three by three: eight round its middle and 1. A right spiral step about its 5 is multiplying by 3 round ten, and two steps a podaling, 10 less.<br>"
           "Its middle row is 3, 5 and 7, three centres: a centre's prior by its next is a seam, 8, 24 and 48, and a centre's square the seam's +1, at 9, 25 and 49.<br>"
           "Six diamonds on the co-linear are 1 to 49, a vertex 8 on a diamond: nine is one on from eight and one before ten, and 17 is a next 1.<br>"
           "A candidate, the fourth figure of twelve, beside the seven drawings it gathers and writing in none.</div>")
ARIA = ("Five parts and a table. A diamond of nine numbered cells with a line through its middle and four arcs about it. A table of four rows of nine numbers. "
        "A grid of two rows by five columns with the numbers 0 to 9. A line from 0 to 50 with six diamonds on it, marks over it at 8, 24 and 48 and under it at 10 to 50. "
        "Two lines of a square's rounds and a cube's shells. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("Diamond of Nine about Its 5", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft62.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft62_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft62_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
