"""v410illustrating · the maker of the 60th drawing: Shells of a Cube, 1, 7, 19, 37 and 61.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft60.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The second figure of the reduced set, one drawing beside the five it gathers: the 7th, the 8th, the 40th, the 41st and
the 50th. By a partner's aiming of 27 November it shows how the +1s are living in the seams of natural torusing.
Its check is opened and executed here, and no drawing is made with an is-not.

Its placings, no execution says them: its five parts and its table side by side; the rounds' flat laying, the me's
line up; a shell drawn across the cube's line as a row of cells; the tints of a seam, a +1 and a −1.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_60", os.path.join(HERE, "check_shells_of_a_cube_a_plus_one_in_a_seam.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"

W, H = 1520, 1150
GREY, SLATE, PALE = "#4a5160", "#475569", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
s, over = [], []

def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def bullets(x, y, w, items, size=12.2, step=21):
    for i, t in enumerate(items): over.append(word(x, y + step * i, w, t, size=size))
def dot(x, y, r, fill, stroke=INK, sw=1.2): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"></circle>'

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "60 · figure 2 of twelve, a cube's shells · it gathers the 7th, the 8th, the 40th, the 41st and the 50th drawings · its prior figure: the one triangle, the 59th · "
                 "its next figures: cones of 30 on the co-linear, and rows of 30", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 830, "A round of six closes on the me's line, a seam, and its next round opens one on: a +1.", size=20, h=28))
over.append(word(60, 108, 830, "A cube's shells are 6, 18, 36 and 60 and one more: 7, 19, 37 and 61.", size=20, h=28))
over.append(word(60, 138, 830, "On a torus of a seam's primes the +1 is crossed by none of them.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Natural Numbers · a torus is a sphere with one handle, +1; a +1 between a centre's square and its seam",
                       "Exhibit THIRTY · a torus of mes and its two seams, a me of both seams",
                       "Exhibit ONE, Natural Naming · seventeen names; a prime by its position; same-existing: 4, 8, 12, 16",
                       "Natural Illustrating · for its part of number forming and podaling")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · rounds of six about a 0 =================
CX, CY, S_ = 252, 436, 34.0
def at(p): return CX + 0.866 * S_ * p[0], CY - 0.5 * S_ * p[0] - S_ * p[1]
cells, closing, opening = own["cells"], own["closing"], own["opening"]
x0, y0 = at((0, 0)); x1, y1 = at((0, 4.75)); x2, y2 = at((1, -0.6)); x3, y3 = at((1, 4.6))
s.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{ACC}" stroke-opacity="0.55" stroke-width="17" stroke-linecap="round"></path>')
s.append(f'<path d="M{x2:.1f},{y2:.1f} L{x3:.1f},{y3:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.13" stroke-width="17" stroke-linecap="round"></path>')
for n in range(0, 62):
    x, y = at(cells[n]); prime = c.is_prime(n)
    if n == 0: fill, stroke, sw, col, wt = "#ffffff", INK, 1.6, INK, 600
    elif n in closing: fill, stroke, sw, col, wt = ACC, "#ffffff", 1.6, "#ffffff", 600
    elif n in opening: fill, stroke, sw, col, wt = INK, "#ffffff", 1.6, "#ffffff", 600
    elif n + 1 in closing: fill, stroke, sw, col, wt = "#ffffff", INK, 2.4, INK, 600
    elif prime: fill, stroke, sw, col, wt = PALE, INK, 1.3, INK, 600
    else: fill, stroke, sw, col, wt = "#f7f8fa", "#aab1bf", 1, "#7b8494", 400
    s.append(dot(x, y, 14.4, fill, stroke, sw)); over.append(word(x, y, 28, str(n), "center", wt, 11, 14, col))
over.append(word(60, 196, 440, "1 · rounds of six about a 0", weight=600, size=15))
LG = [(70, ACC, "#ffffff", 1.2, "a seam"), (142, INK, "#ffffff", 1.2, "a +1"), (204, "#ffffff", INK, 2.2, "a −1"), (266, PALE, INK, 1.3, "a prime")]
for x, fill, stroke, sw, t in LG:
    s.append(dot(x, 220, 6.5, fill, stroke, sw)); over.append(word(x + 12, 220, 80, t, size=12.5, color=GREY))
xm, ym = at((0, 4.75)); over.append(word(xm - 8, ym - 16, 110, "the me's line", "right", 600, 12, 14, ACC))
xo, yo = at((1, 4.6)); over.append(word(xo + 16, yo - 6, 150, "a round's opening", size=12, h=14, color=GREY))
bullets(60, 636, 430, ("● a round closes on the me's line: a seam, 6, 18, 36 and 60",
                       "● its next round opens one on: a +1, 1, 7, 19, 37 and 61",
                       "● one before a seam is beside it too: its −1, 5, 17, 35 and 59",
                       "● two primes about a seam at 6, 18 and 60 · 35 is 5 by 7"), step=20)

# ================= 2 · a cube's shells, a +1 on its line =================
LX, LY, DS = 596, 280, 21.0
s.append(f'<path d="M{LX},{LY - 18} L{LX},{LY + 4 * 34 + 20}" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="2 5" stroke-linecap="round"></path>')
shells = own["shells"]
for n in range(1, 6):
    y = LY + 34 * (n - 1)
    for k in range(-(n - 1), n):
        s.append(dot(LX + DS * k, y, 8, INK if k == 0 else PALE, "#ffffff" if k == 0 else INK, 1.4 if k == 0 else 1.1))
    seam = shells[n - 1] - 1
    over.append(word(LX + DS * 4 + 26, y, 190, "1" if n == 1 else f"{seam} and 1: {shells[n - 1]}", size=12.5, weight=600 if n > 1 else 400))
    over.append(word(LX - DS * 4 - 22, y, 80, ("one me", "a cube of 2", "of 3", "of 4", "of 5")[n - 1] + (" less its inner" if n == 2 else ""), "right", size=11, h=14, color=GREY))
over.append(word(LX + 12, LY - 26, 120, "the cube's line", size=11.5, h=14, color=GREY))
over.append(word(500, 196, 480, "2 · a cube's shells, a +1 on its line", weight=600, size=15))
over.append(word(500, 220, 480, "a shell across the cube's line · ● its one more, on the line", size=12.5, color=GREY))
bullets(500, 456, 480, ("● a shell is a seam and one more: 6 by 0, 1, 3, 6 and 10, and 1",
                        "● five shells are a cube of 5: five on its line, and 120 about it",
                        "● observed along the line a shell is a +1 and rounds of six about it"), step=19, size=12)

# ================= 3 · a seam of six, a torus of 2 by 3 =================
GX, GY, CW, CH = 520, 566, 92, 46
over.append(word(500, 522, 480, "3 · a seam of six, a torus of 2 by 3", weight=600, size=15))
over.append(word(500, 543, 480, "a winding by +1 is through all six cells, at its opening again at 6", size=11.5, h=14, color=GREY))
def numbers_of(a, b):
    out = []
    for n in range(0, 42):
        if n % 2 == a and n % 3 == b:
            t = str(n)
            if n in shells and n > 1: t = f'<span style="color: {ACC}; font-weight: 600">{n}</span>'
            elif c.is_prime(n): t = f'<span style="font-weight: 600">{n}</span>'
            else: t = f'<span style="color: #7b8494">{n}</span>'
            out.append(t)
    return out
for a in (0, 1):
    for b in (0, 1, 2):
        x, y = GX + b * CW, GY + a * CH
        fill, op = (ACC, 0.2) if (a, b) == (1, 1) else (SLATE, 0.2) if (a, b) == (1, 2) else ("#ffffff", 1)
        s.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" fill="{fill}" fill-opacity="{op}" stroke="{INK}" stroke-width="1.1"></rect>')
        ns = numbers_of(a, b)
        over.append(word(x + CW / 2, y + 15, CW, " ".join(ns[:4]), "center", size=11, h=14)); over.append(word(x + CW / 2, y + 31, CW, " ".join(ns[4:]), "center", size=11, h=14))
over.append(word(GX + 3 * CW + 10, GY + CH / 2, 180, "the spiral of 2 crosses", size=11, h=14, color=GREY))
over.append(word(GX + 3 * CW + 10, GY + CH + CH / 2 - 8, 180, "a +1 and a −1: crossed", size=11, h=14, color=GREY))
over.append(word(GX + 3 * CW + 10, GY + CH + CH / 2 + 7, 180, "by none", size=11, h=14, color=GREY))
over.append(word(GX, GY + 2 * CH + 12, 470, "the spiral of 3 crosses the cells of 0 and of 3 · a prime past 3 is at the +1 or at the −1", size=11, h=14, color=GREY))
over.append(word(GX, GY + 2 * CH + 28, 470, "0 is the cell of both seams, a seam at it again at all its rounds · in the accent, a shell", size=11, h=14, color=GREY))

# ================= the table: a name a row, its prime beside a six =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("its prime", 196, 42, "right"), ("beside a six", 254, 96, "left"), ("a round of four closing", 352, 152, "left")]
over.append(word(TX, 196, 500, "a name a row · its prime by its position · beside a six", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 504},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
prime_of, names = own["prime_of"], own["names"]
ROUND = {4: "round one, at a shell, 7", 8: "round two, at a shell, 19", 12: "round three, at a shell, 37", 16: "round four, 8 short of 61"}
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="512" height="{RH:.1f}" fill="{PALE}"></rect>')
    p = prime_of[n]
    cells_ = [str(n), names[n], str(p), c.side_of_a_six(p), ROUND.get(n, "")]
    for (t, x, w_, al), v in zip(cols, cells_):
        bold = t in ("n", "its name, Exhibit ONE's own") or (t == "its prime" and p in shells) or (t == "beside a six" and p % 6 == 1)
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if bold else 400, 11.2, 16, extra="font-variant-numeric: tabular-nums;"))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 504},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its prime by its position: the one table of the seventeen names, 2 to 59",
                       "beside a six: 2 and 3 are the seam's own; six primes are a six and 1, and nine a six less 1",
                       "four primes are a round: three rounds close at a shell, at the 4th, the 8th and the 12th,",
                       "the names of same-existing; the 16th is with 53, and 61 is one past the seventeen")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= 4 · seams of the primes multiplied, and their +1s =================
over.append(word(60, 736, 460, "4 · seams of the primes multiplied, and their +1s", weight=600, size=15))
SC = [("a seam", 0, 64, "right"), ("by", 78, 40, "left"), ("its cells crossed by none", 124, 150, "right"), ("its +1", 290, 180, "left")]
for t, x, w_, al in SC:
    over.append(word(60 + x + (w_ if al == "right" else 0), 760, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M60,769 L520,769" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
num = lambda n: f"{n:,}"
for i, (seam, p, living, plus, ps) in enumerate(own["rows"]):
    y = 780 + 17.5 * i
    if i % 2: s.append(f'<rect x="56" y="{y - 8.75:.1f}" width="468" height="17.5" fill="{PALE}"></rect>')
    last = num(plus) + (", a prime" if len(ps) == 1 else ": " + " by ".join(map(str, ps)))
    for (t, x, w_, al), v in zip(SC, (num(seam), ("2" if p == 2 else f"by {p}"), num(living), last)):
        over.append(word(60 + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if (t == "its +1" and len(ps) == 1) else 400, 11.2, 15, extra="font-variant-numeric: tabular-nums;"))

# ================= 5 · the +1s of the opening figure =================
over.append(word(552, 736, 430, "5 · the +1s of the opening figure, the 59th", weight=600, size=15))
bullets(552, 762, 440, ("● 16 and 1: 17 is at 1 again, on a torus of sixteen patches",
                        "● a torus is a sphere with one handle, and its handle is +1",
                        "● 59 and 1: sixty moves of one hand, one moving nothing",
                        "● 35 and 1 is 36, and 36 and 1 is 37: 5 by 7, 6 by 6, a prime",
                        "● a centre's square is its prior by its next, and one more",
                        "● 23 and 25 are beside 24: a prime, and five fives",
                        "● a seam's +1 is one on along all its ways: the cell of ones"), step=20, size=12)

# ================= found, and what this drawing leaves with the five =================
FX, FY = 1004, 652
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the five", weight=600, size=15))
FOUND = [("a +1, said five ways, not one saying yet", ["a round's opening; a shell's cell on the cube's line; the cell of ones on a seam's torus;", "a torus's handle; and a centre's square past its seam"]),
         ("three rounds close at the names of same-existing", ["7, 19 and 37 are the 4th, the 8th and the 12th primes; the 16th is 53, 8 short of 61"]),
         ("a seam's +1 past the primes to 11 is no prime", ["30,031 is 59 by 509, and 510,511 is 19 by 97 by 277: crossed by primes past their seam's"]),
         ("it is no method of a prime's existing", ["a +1 is crossed by none of its seam's primes; what crosses it, or none, its seam does not say"]),
         ("with the five drawings, as they were", ["the 7th's 0 to 120 and its six lines; the 8th's four rounds of 24, 36, 36 and 24; the 40th's right", "spiral of primes; the 41st's 27, 9 and 1; the 50th's ten sixes about the line"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">Shells of a Cube, 1, 7, 19, 37 and 61</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Living a +1 in a Seam of Six, a Round Opening beside Its Closing</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "Numbers wound round a 0 are rounds of six. A round closes on the me's line, a seam, and its next round opens one on, a +1: 1, 7, 19, 37 and 61.<br>"
           "They are a cube's shells: a shell is a seam and one more, the one on the cube's line. Five shells are a cube of 5, five on its line and 120 about it.<br>"
           "A seam of six is a torus of 2 by 3, and a prime past 3 is at its +1 or at its −1. A seam's +1 is crossed by none of its seam's primes.<br>"
           "A candidate, the second figure of twelve, beside the five drawings it gathers and writing in none.</div>")
ARIA = ("Five parts and a table. Sixty-two numbered cells wound in rounds of six about a cell of nought, four of them on one line in the accent. Five rows of cells, 1, 3, 5, 7 and 9, with one line through "
        "their middles. A grid of 2 by 3 with the numbers 0 to 41 by their cells. A table of seven seams and their numbers one more. Seven lines of the 59th drawing's numbers. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("Shells of a Cube, 1, 7, 19, 37 and 61", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft60.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft60_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft60_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
