"""v410illustrating · the maker of the 64th drawing: Two Primes, One Torus.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft64.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The tenth figure of the reduced set, one drawing beside the three it gathers, the 43rd, the 45th and the 48th. It goes
by a partner's two sayings of 27 November: the +1s living in the seams of natural torusing, and the numbers between
the prime crossings numbering a surface's cells. Its check is opened and executed here, and no drawing is made with
an is-not. Its numbers are the check's own.

Its placings, no execution says them: its five parts and its table side by side; a torus laid flat as a table, a
column a cell of 5 and a row a cell of 7; the co-linear with a mark a crossing; a cell drawn as seven finer cells;
the tints of a crossing, of the cell of both, and of a between.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_64", os.path.join(HERE, "check_two_primes_one_torus.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"
names, primes, nxt, rows = own["names"], own["primes"], own["nxt"], own["rows"]

W, H = 1520, 1150
GREY, SLATE, PALE = "#4a5160", "#475569", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
NUM = "font-variant-numeric: tabular-nums;"
s, over = [], []
def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def join(xs): xs = [str(x) for x in xs]; return ", ".join(xs[:-1]) + " and " + xs[-1]
def grid(gx, gy, cw, ch, across, down, size=12):                          # a torus laid flat: a column a cell of `across`, a row a cell of `down`
    for r in range(down):
        for q in range(across):
            n = next(k for k in range(across * down) if k % across == q and k % down == r)
            x, y = gx + q * cw, gy + r * ch
            if q == 0 and r == 0: fill, op, col = INK, 1, "#ffffff"
            elif q == 0: fill, op, col = ACC, 0.26, INK
            elif r == 0: fill, op, col = SLATE, 0.26, INK
            else: fill, op, col = "#ffffff", 1, INK
            s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{fill}" fill-opacity="{op}" stroke="{INK}" stroke-opacity="0.55" stroke-width="{2.4 if (q, r) == (1, 1) else 1}"></rect>')
            over.append(word(x + cw / 2, y + ch / 2, cw, str(n), "center", 600 if c.is_prime(n) else 400, size, size + 4, col, NUM))

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "64 · figure 10 of twelve, two primes with one torus · it gathers the 43rd, the 45th and the 48th drawings · its prior figure: the rows of 30, the 63rd · "
                 "its next figures: a me beside an other, and living parities", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 840, "Two me-parities are one torus: a winding by +1 numbers all their cells, a number a cell.", size=20, h=28))
over.append(word(60, 108, 840, "A crossing is a line of it; the numbers between the crossings number its betweens.", size=20, h=28))
over.append(word(60, 138, 840, "Of two about one centre the betweens are a seam, and its +1 the opening, the one cell of both.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names, a prime a name: a name's prime with its next name's, a torus of two",
                       "Natural Numbers · a torus, a sphere with one handle, its handle +1; 59 by 61 is 60 by 60 less 1",
                       "Exhibit THIRTY, Natural Naming · a torus's seams, two lines through its opening; bi-coupling",
                       "Natural Illustrating · for its part of number forming and podaling")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · a torus of 5 by 7 =================
GX, GY, CW, CH = 150, 268, 54, 33
over.append(word(60, 196, 440, "1 · a torus of 5 by 7: thirty-five numbers, a number a cell", weight=600, size=15))
for x, f_, op, t in ((64, ACC, 0.26, "the crossing of 5: seven cells"), (250, SLATE, 0.26, "of 7: five cells"), (370, INK, 1, "0 and 0: of both")):
    s.append(f'<rect x="{x}" y="212" width="18" height="12" fill="{f_}" fill-opacity="{op}" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></rect>'); over.append(word(x + 24, 218, 160, t, size=11.4, color=GREY))
over.append(word(60, 236, 440, "a column its cell of 5, a row its cell of 7 · +1 is one cell on at both · a bold number a me-parity", size=11.3, h=14, color=GREY))
for q in range(5): over.append(word(GX + q * CW + CW / 2, GY - 11, CW, str(q), "center", 600, 10.6, 13, GREY))
for r in range(7): over.append(word(GX - 10, GY + r * CH + CH / 2, 30, str(r), "right", 600, 10.6, 13, GREY))
over.append(word(GX - 10, GY - 11, 80, "of 7 · of 5", "right", 400, 10, 13, GREY))
grid(GX, GY, CW, CH, 5, 7, 13)
for n in range(1, 5):                                                      # a winding by +1, its opening steps: one cell on at both sides
    x1, y1, x2, y2 = GX + (n - 1) * CW + CW * 0.76, GY + (n - 1) * CH + CH * 0.8, GX + n * CW + CW * 0.24, GY + n * CH + CH * 0.2
    s.append(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.6" stroke-width="1.2" stroke-dasharray="2 3"></path>')
over.append(word(GX + 5 * CW + 10, GY + CH * 1.5, 80, "the cell of", size=10.6, h=13, color=GREY)); over.append(word(GX + 5 * CW + 10, GY + CH * 1.5 + 13, 80, "ones: 1, and", size=10.6, h=13, color=GREY))
over.append(word(GX + 5 * CW + 10, GY + CH * 1.5 + 26, 80, "36 again", size=10.6, h=13, color=GREY))
yb1 = GY + 7 * CH
bt = len(c.between((5, 7))); on = len(c.on_a_crossing((5, 7)))
over.append(word(60, yb1 + 14, 440, f"{on} cells are on a crossing, and {bt} between: 4 by 6, 5 by 5 less 1", size=11.5, h=14))
over.append(word(60, yb1 + 30, 440, "with the one cell at 0 and 0, the opening, they are 25: 5 by 5, a seam and its +1", size=11.5, h=14))
over.append(word(60, yb1 + 46, 440, "a winding by +1 is at 0 and 0 again at 35; 36, 6 by 6, is at the cell of ones", size=11.5, h=14, color=GREY))

# ================= 2 · a between, one thing from two sides =================
over.append(word(530, 196, 450, "2 · a between, one thing from two sides", weight=600, size=15))
over.append(word(530, 216, 450, "the same numbers on the co-linear: a crossing a mark, of 5 over it, of 7 under it", size=11.5, h=14, color=GREY))
X = lambda n: 548 + 12 * n
Y0 = 262
s.append(f'<path d="M{X(0) - 8},{Y0} L{X(35) + 10},{Y0}" fill="none" stroke="{INK}" stroke-width="1.4"></path>')
for run in own["runs"]:
    s.append(f'<rect x="{X(run[0]) - 5}" y="{Y0 - 7}" width="{12 * (len(run) - 1) + 10}" height="14" rx="7" fill="{ACC}" fill-opacity="0.10" stroke="{INK}" stroke-opacity="0.3" stroke-width="1"></rect>')
    over.append(word((X(run[0]) + X(run[-1])) / 2, Y0 - 17, 20, str(len(run)), "center", 600, 9.6, 12, GREY))
for n in range(36):
    if n % 5 == 0: s.append(f'<path d="M{X(n)},{Y0} L{X(n)},{Y0 - 12}" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-linecap="round"></path>')
    if n % 7 == 0: s.append(f'<path d="M{X(n)},{Y0} L{X(n)},{Y0 + 12}" fill="none" stroke="{SLATE}" stroke-width="2.4" stroke-linecap="round"></path>')
    if n % 5 and n % 7: s.append(f'<circle cx="{X(n)}" cy="{Y0}" r="2.6" fill="{INK if c.is_prime(n) else "#ffffff"}" stroke="{INK}" stroke-width="1"></circle>')
    over.append(word(X(n), Y0 + (21 if n % 2 == 0 else 32), 16, str(n), "center", 600 if (n % 5 == 0 or n % 7 == 0) else 400, 8.8, 11, ACC if n % 5 == 0 else SLATE if n % 7 == 0 else GREY, NUM))
over.append(word(530, 314, 450, f"between two crossings next to one another: {join(len(r) for r in own['runs'])} numbers", size=11.5, h=14))
over.append(word(530, 330, 450, f"they are {bt}: the numbers of the torus's cells between its two lines", size=11.5, h=14))
over.append(word(530, 346, 450, "with all of 2, 3 and 5 crossing, the eight between are a row's mes: the 63rd", size=11.5, h=14, color=GREY))

# ================= 3 · a surface made finer =================
over.append(word(530, 374, 450, "3 · a surface made finer: a seam lifted", weight=600, size=15))
over.append(word(530, 393, 450, "a torus of 3 by 5 · its cell 1 is seven cells of 3 by 5 by 7, a cell of 7 apiece", size=11.5, h=14, color=GREY))
G3X, G3Y, C3W, C3H = 548, 410, 32, 24
grid(G3X, G3Y, C3W, C3H, 5, 3, 11)
FX0, FY0, FW = 752, 422, 31
s.append(f'<path d="M{G3X + 5 * C3W + 4},{G3Y + C3H * 1.5} L{FX0 - 8},{FY0 + 12}" fill="none" stroke="{INK}" stroke-opacity="0.6" stroke-width="1.2" stroke-dasharray="2 3"></path>')
s.append(f'<path d="M{FX0 - 4},{FY0 + 12} l-8,-4 l0,8 Z" fill="{INK}"></path>')
for i, n in enumerate(own["finer"]):
    crossed = n % 7 == 0
    s.append(f'<rect x="{FX0 + i * FW}" y="{FY0}" width="{FW}" height="24" fill="{SLATE if crossed else "#ffffff"}" fill-opacity="{0.26 if crossed else 1}" stroke="{INK}" stroke-opacity="0.55" stroke-width="1"></rect>')
    over.append(word(FX0 + i * FW + FW / 2, FY0 + 12, FW, str(n), "center", 600 if c.is_prime(n) else 400, 11, 14, extra=NUM))
over.append(word(FX0, FY0 + 36, 230, "six between, and 91 on the crossing of 7", size=10.8, h=13, color=GREY))
cnt = own["counts"]
R3 = [("a seam's cells", [a for a, _ in cnt]), ("between its crossings", [b for _, b in cnt]), ("in 100", [round(100 * b / a) for a, b in cnt])]
for i, (label, vals) in enumerate(R3):
    y = 506 + 18 * i
    over.append(word(530, y, 150, label, weight=600, size=11.6, h=15, color=GREY))
    for j, v in enumerate(vals): over.append(word(700 + 64 * j + 50, y, 50, str(v), "right", 600 if i == 1 else 400, 11.6, 15, extra=NUM))
over.append(word(530, 566, 450, f"lifted by 7, fifteen cells are 105, and eight between are {len(c.between((3, 5, 7)))}: finer, and not none", size=11.5, h=14))

# ================= 4 · two me-parities about one centre =================
over.append(word(60, 600, 920, "4 · two me-parities about one centre, 2 on: their betweens a seam, and its +1 the opening", weight=600, size=15))
R4 = [("two me-parities", [f"{r[0]} by {r[1]}" for r in rows]), ("their centre", [r[2] for r in rows]), ("their torus's cells", [r[3] for r in rows]), ("the centre's square", [r[4] for r in rows]),
      ("cells on a crossing", [r[5] for r in rows]), ("cells between", [r[6] for r in rows]), ("with 0 and 0: the lesser's square", [r[7] for r in rows])]
for i, (label, vals) in enumerate(R4):
    y = 628 + 19 * i
    if i in (2, 5): s.append(f'<rect x="56" y="{y - 9.5}" width="926" height="19" fill="{ACC}" fill-opacity="0.10"></rect>')
    over.append(word(60, y, 240, label, weight=600, size=11.8, h=15, color=GREY if i in (0, 1, 4) else INK))
    for j, v in enumerate(vals): over.append(word(330 + 92 * j + 80, y, 80, str(v), "right", 600 if i in (0, 2, 5) else 400, 11.8, 15, extra=NUM))
s.append(f'<path d="M60,638 L980,638" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
over.append(word(60, 770, 920, "their cells are the centre's square less 1, and their betweens the lesser's square less 1: two seams and two +1s: the cell of ones a round on, and the opening", size=11.5, h=14))
over.append(word(60, 787, 920, f"past 3 and 5 a centre is a seam of six: {join(r[2] for r in rows[1:])} · 59 by 61 is 60 by 60 less 1, Natural Numbers' own saying: the 17th name's prime, and a next 1's", size=11.5, h=14, color=GREY))

# ================= 5 · is-not a torus of two, and a marker =================
over.append(word(60, 822, 920, "5 · is-not a torus of two; and a marker", weight=600, size=15))
over.append(word(60, 844, 920, f"6 and 10 are with 2 in both: a winding by +1 numbers {len(c.numbered((6, 10)))} of their sixty cells, the 43rd · a me-parity with its own, 5 and 5, numbers {len(c.numbered((5, 5)))} of twenty-five, the 45th", size=12, h=15))
over.append(word(60, 862, 920, "a marker, by a partner's word of 27 November: a between is one thing from two sides, an is.", size=12, h=15, weight=600))
over.append(word(60, 880, 920, "At an is-not, the incohering is sought, and the work goes back to this drawing.", size=12, h=15))

# ================= the table: a name a row, its prime with its next name's =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("its prime", 194, 42, "right"), ("its next's", 240, 46, "right"), ("cells", 290, 44, "right"),
        ("crossing", 338, 50, "right"), ("between", 392, 48, "right"), ("2 on", 446, 58, "right")]
over.append(word(TX, 196, 500, "a name a row · its prime with its next name's, a torus of two", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 504},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7; p, q = primes[n], nxt[n]
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="512" height="{RH:.1f}" fill="{PALE}"></rect>')
    cells_ = [str(n), names[n], str(p), str(q), str(p * q), str(p + q - 1), str((p - 1) * (q - 1)), f"{p * p} less 1" if q - p == 2 else ""]
    for (t, x, w_, al), v in zip(cols, cells_):
        bold = t in ("n", "its name, Exhibit ONE's own", "its prime", "between") or (t == "2 on")
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if bold else 400, 11.2 if t != "2 on" else 10.4, 16, ACC if t == "2 on" else INK, extra=NUM))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 504},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its next's: the next name's prime, and the 17th's 61, a next 1's, Natural Numbers' returning",
                       "cells: the two multiplied · crossing: the cells on its two lines, the two added less 1",
                       "between: the cells on no line, the two less 1 apiece and multiplied",
                       "2 on: its next's prime is 2 on, about one centre: its between is its own square less 1, a seam")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= found, and what this drawing leaves with the three =================
FX, FY = 1004, 640
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the three", weight=600, size=15))
FOUND = [("a between, one thing from two sides: a partner's is, a marker", ["on the co-linear, the numbers between two crossings; on the torus, the cells on no line"]),
         ("a +1 at the opening", ["of two me-parities about one centre the betweens are a seam, and with the one cell", "of both lines, 0 and 0, the lesser's square"]),
         ("a surface made finer", ["a seam lifted: a cell is seven finer cells, six between and one on a crossing"]),
         ("it is no method of a far me-parity alone", ["known mathematics: a winding through all cells of two numbers with no part of both"]),
         ("with the three drawings, as they were", ["the 43rd's six and ten round 30; the 45th's all pairs under 100;", "the 48th's quarter of two primes and its diagonal, gathered by its number alone"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">Two Primes, One Torus</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Winding by +1 through All Their Cells, Numbering the Betweens of Their Crossings</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "Two me-parities are one torus, and a winding by +1 numbers all their cells, a number a cell, at 0 and 0 again at the two multiplied.<br>"
           "A me-parity's crossing is a line of the torus. The numbers between the crossings on the co-linear number the cells on no line: a between, one thing from two sides.<br>"
           "Of two me-parities about one centre the betweens are a seam, and with the one cell of both lines a square. A seam lifted is the same round with finer cells.<br>"
           "A candidate, the tenth figure of twelve, beside the three drawings it gathers and writing in none.</div>")
ARIA = ("Five parts and a table. A table of seven rows by five columns with the numbers 0 to 34, a column and a row tinted. A line from 0 to 35 with marks over and under it. "
        "A table of three rows by five columns, and one cell drawn as seven. A table of seven pairs of primes about one centre. Three lines. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("Two Primes, One Torus", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft64.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft64_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft64_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
