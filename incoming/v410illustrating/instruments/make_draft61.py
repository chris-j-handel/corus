"""v410illustrating · the maker of the 61st drawing: Cones of 30 on a Co-Linear.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft61.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The third figure of the reduced set, one drawing beside the nine it gathers, the 9th to the 17th. By a partner's
aiming of 27 November it goes on showing how the +1s are living in the seams of natural torusing.
Its check is opened and executed here, and no drawing is made with an is-not.

Its placings, no execution says them: its five parts and its table side by side; a cone drawn as a width over the
co-linear, a cell at its width; a name's chip over its cell; a me-now's four moments on a cone's other side; the tints
of a seam, a +1 and a −1.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_61", os.path.join(HERE, "check_cones_of_30_on_a_co-linear_podaling_about_a_seam_of_30.py"))
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
def chip(cx, cy, t, filled, w=20, h=16, size=10):
    look = (f"background: {INK}; color: #ffffff; border: 1.3px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 1.3px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 2.6:.0f}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{t}</div>')
def bullets(x, y, w, items, size=12.2, step=21):
    for i, t in enumerate(items): over.append(word(x, y + step * i, w, t, size=size))
def dot(x, y, r, fill, stroke=INK, sw=1.2): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"></circle>'

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "61 · figure 3 of twelve, cones of 30 on the co-linear · it gathers the 9th to the 17th drawings · its prior figure: a cube's shells, the 60th · "
                 "its next figures: the diamond of nine, and rows of 30", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 840, "30 is 2 by 3 by 5, a seam, and eight of its thirty cells are crossed by none: a cone's eight.", size=20, h=28))
over.append(word(60, 108, 840, "A pair of cones is sixteen cells, the names 1 to 16, and 17 is at 61, a next 1.", size=20, h=28))
over.append(word(60, 138, 840, "The names at the me are at the seam's +1, and two of same-existing at its −1.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names; four bi-foldings, 8 up and 17 less",
                       "Natural Numbers · three moves: 8 up, 17 less a podal from 1 to 16, 9 less a podal from 1 to 8",
                       "Exhibit THIRTY, Natural Naming · a torus's seams; podaling; a me-parity, a both-parity, an all-parity",
                       "Natural Illustrating · for its part of number forming and podaling")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · four cones of 30 on the co-linear, 0 to 120 =================
X0, U, Y0, HT = 84.0, 7.0, 404.0, 112.0
X = lambda n: X0 + U * n
def width(n): return HT * (1 - abs((n % 60) - 30) / 30)
tent = " L".join(f"{X(n):.1f},{Y0 - width(n):.1f}" for n in (0, 30, 60, 90, 120))
under = " L".join(f"{X(n):.1f},{Y0 + width(n):.1f}" for n in (0, 30, 60, 90, 120))
s.append(f'<path d="M{tent} L{X(120):.1f},{Y0:.1f} L{X(0):.1f},{Y0:.1f} Z" fill="{ACC}" fill-opacity="0.07" stroke="none"></path>')
s.append(f'<path d="M{under} L{X(120):.1f},{Y0:.1f} L{X(0):.1f},{Y0:.1f} Z" fill="{SLATE}" fill-opacity="0.06" stroke="none"></path>')
s.append(f'<path d="M{tent}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1.2"></path>')
s.append(f'<path d="M{under}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1.2"></path>')
for st in (30, 90):
    s.append(f'<path d="M{X(st):.1f},{Y0 - HT:.1f} L{X(st):.1f},{Y0 + HT:.1f}" fill="none" stroke="{ACC}" stroke-opacity="0.6" stroke-width="1.4" stroke-dasharray="3 4"></path>')
s.append(f'<path d="M{X(0) - 14:.1f},{Y0} L{X(126):.1f},{Y0}" fill="none" stroke="{INK}" stroke-width="1.5"></path>')
s.append(f'<path d="M{X(126):.1f},{Y0} l-9,-4.5 l0,9 Z" fill="{INK}"></path>')
by_cone = own["by_cone"]; cells = [n for cone in by_cone for n in cone]
for k in (0, 1):                                                         # a cell and its podal about a cone's widest, one width of the cone
    for n in by_cone[2 * k]:
        s.append(f'<path d="M{X(n):.1f},{Y0 - width(n):.1f} L{X(60 * k + 60 - (n - 60 * k)):.1f},{Y0 - width(n):.1f}" fill="none" stroke="{INK}" stroke-opacity="0.16" stroke-width="1"></path>')
for st in c.STATIONS:
    s.append(f'<path d="M{X(st):.1f},{Y0 - 7} L{X(st):.1f},{Y0 + 16}" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-linecap="round"></path>')
    over.append(word(X(st), Y0 + 26, 34, str(st), "center", 600, 11.5, 14, ACC, extra="background: #ffffff; border-radius: 6px;"))
name_at = {v: k for k, v in c.ON_CONES.items()}
for n in cells + [121]:
    x, y = X(n), Y0 - width(n) if n <= 120 else Y0 - width(1)
    prime = c.is_prime(n)
    if n % 30 == 1: fill, stroke, sw = INK, "#ffffff", 1.5
    elif n % 30 == 29: fill, stroke, sw = "#ffffff", INK, 2.3
    elif prime: fill, stroke, sw = PALE, INK, 1.3
    else: fill, stroke, sw = "#f7f8fa", "#aab1bf", 1
    if n == 121: fill, stroke, sw = "#ffffff", "#aab1bf", 1
    s.append(dot(x, y, 5.2, fill, stroke, sw))
    dx = 8 if n % 30 == 1 else -8 if n % 30 == 29 else 0
    over.append(word(x + dx, y + 13, 24, str(n), "center", 600 if prime else 400, 9.6, 12, INK if prime else "#7b8494"))
    if n in name_at: over.append(chip(x + (9 if dx > 0 else -9 if dx < 0 else 0), y - 15, str(name_at[n]), name_at[n] in (1, 9, 17), w=17, h=15, size=9.6))
over.append(word(60, 196, 600, "1 · four cones of 30 on the co-linear, 0 to 120", weight=600, size=15))
LG = [(70, ACC, "#ffffff", 1.2, "a seam's round"), (184, INK, "#ffffff", 1.2, "a +1"), (240, "#ffffff", INK, 2.2, "a −1"), (298, PALE, INK, 1.3, "a prime")]
for x, fill, stroke, sw, t in LG:
    s.append(dot(x, 220, 6.2, fill, stroke, sw)); over.append(word(x + 12, 220, 110, t, size=12.5, color=GREY))
over.append(chip(378, 220, "9", True)); over.append(word(394, 220, 260, "a name over its cell: 1 to 16, and 17 at 61", size=12.5, color=GREY))
over.append(word(700, 220, 280, "a line across a cone: a cell and its podal", "left", size=12.5, color=GREY))
over.append(word(60, 240, 920, "0 to 30, a cone opening: prior, the names 1 to 8 · 30 to 60, a cone closing: now, the names 9 to 16 · 60 to 120, a pair of cones on: 30 on is 8 up", size=11.8, h=14, color=GREY))
# a me-now's four moments, on the cones' other side
m37 = own["m37"]
for n, t, filled in ((37, "37 · a me-now", True), (m37[0], "23 · 60 less it", False), (m37[1], "97 · 60 on", False), (m37[2], "83 · 120 less it", False)):
    x, y = X(n), Y0 + width(n)
    s.append(dot(x, y, 6.6, ACC if filled else "#ffffff", "#ffffff" if filled else ACC, 1.6 if filled else 2.2))
    over.append(word(x, y + 15, 130, t, "center", 600, 10.8, 13))
over.append(word(X(126), Y0 + HT + 4, 260, "157 · 120 on: its next universe, past 120", "right", size=10.8, h=13, weight=600))
over.append(word(X(60), Y0 + HT + 26, 520, "a cone's other side: a me-now at 37 and its four moments, a podaling about 30, 60, 90 and 120, one and then the next", "center", size=11.5, h=14, color=GREY))

# ================= 2 · three moves, and four bi-foldings =================
over.append(word(60, 566, 440, "2 · three moves, and four bi-foldings by their numbers", weight=600, size=15))
over.append(word(60, 588, 440, "8 up is 30 on · 17 less, a podaling about 30 · 9 less, about 15", size=11.8, h=14, color=GREY))
NOTE = ["the four beside the seams 30 and 60", "four primes", "49 is 7 by 7", "four primes"]
for i, (b, f_) in enumerate(zip(c.BI_FOLDINGS, own["folds"])):
    y = 612 + 19 * i
    if i % 2 == 0: s.append(f'<rect x="56" y="{y - 9.5}" width="440" height="19" fill="{PALE}"></rect>')
    over.append(word(60, y, 90, "-".join(map(str, b)), weight=600, size=11.6, h=15, extra="font-variant-numeric: tabular-nums;"))
    over.append(word(150, y, 140, ", ".join(map(str, f_[:3])) + f" and {f_[3]}", size=11.6, h=15, extra="font-variant-numeric: tabular-nums;"))
    over.append(word(292, y, 210, NOTE[i], size=11.4, h=15, color=GREY))

# ================= 3 · a me-now's four moments =================
over.append(word(520, 566, 460, "3 · a me-now's four moments, to its next universe", weight=600, size=15))
MC = [("a podaling", 0, 100, "left"), ("from its opening", 108, 100, "left"), ("at 37", 212, 36, "right"), ("", 262, 200, "left")]
for t, x, w_, al in MC:
    over.append(word(520 + x + (w_ if al == "right" else 0), 588, w_, t, al, 600, 10.4, 14, GREY))
ROWS = [("about 30", "60 less it", m37[0], "an other-than, at a widest"), ("then about 60", "60 on", m37[1], "an all, at a vertex"),
        ("then about 90", "120 less it", m37[2], "an other-than"), ("then about 120", "120 on", m37[3], "an all: its next universe")]
for i, row in enumerate(ROWS):
    y = 612 + 19 * i
    if i % 2 == 0: s.append(f'<rect x="516" y="{y - 9.5}" width="466" height="19" fill="{PALE}"></rect>')
    for (t, x, w_, al), v in zip(MC, row):
        over.append(word(520 + x + (w_ if al == "right" else 0), y, w_, str(v), al, 600 if t == "at 37" else 400, 11.6, 15, extra="font-variant-numeric: tabular-nums;"))
over.append(word(520, 692, 460, "23, 97, 83 and 157 are four primes · a podaling: two folds, an other-than of an other-than", size=11, h=14, color=GREY))

# ================= 4 · a seam of 30, a torus of 2 by 3 by 5 =================
over.append(word(60, 736, 440, "4 · a seam of 30, a torus of 2 by 3 by 5", weight=600, size=15))
over.append(word(60, 757, 440, "a row a cell of the seam of six · a column a cell of 5", size=11.5, h=14, color=GREY))
GX, GY, CW, CH = 148, 772, 40, 20
ROWN = {0: "0 · both seams", 1: "a six's +1", 2: "2", 3: "3", 4: "4", 5: "a six's −1"}
for r in range(6):
    over.append(word(GX - 8, GY + r * CH + CH / 2, 100, ROWN[r], "right", 600 if r in (1, 5) else 400, 10.6, 13, INK if r in (1, 5) else GREY))
    for q in range(5):
        n = next(k for k in range(30) if k % 6 == r and k % 5 == q)
        living = r in (1, 5) and q != 0
        fill, op = ((ACC, 0.22) if r == 1 else (SLATE, 0.2)) if living else ("#ffffff", 1)
        s.append(f'<rect x="{GX + q * CW}" y="{GY + r * CH}" width="{CW}" height="{CH}" fill="{fill}" fill-opacity="{op}" stroke="{INK}" stroke-width="{2.2 if n in (1, 29) else 1}"></rect>')
        over.append(word(GX + q * CW + CW / 2, GY + r * CH + CH / 2, CW, str(n), "center", 600 if living else 400, 11, 14, INK if living else "#7b8494"))
for i, t in enumerate(("eight cells are crossed by", "none of 2, 3 and 5:", "four at a six's +1,", "four at its −1", "1 is the cell of ones, the +1;", "29, one before the opening")):
    over.append(word(GX + 5 * CW + 12, GY + 10 + 17 * i, 170, t, size=10.8, h=14, color=GREY if i < 4 else INK))

# ================= 5 · a +1 and a −1 of the seam, at the names =================
over.append(word(520, 736, 460, "5 · a +1 and a −1 of the seam, at the names", weight=600, size=15))
bullets(520, 762, 470, ("● 1, 9 and 17, the names at the me, are at 1, 31 and 61: the seam's +1",
                        "● the 8th and the 16th, of same-existing, are at 29 and 59: its −1",
                        "● the bi-folding 1-9-8-16 is the four beside the seams 30 and 60",
                        "● 17 is at 61, a next 1: 60 and 1, a pair of cones and one on",
                        "● on from 61: 91 is 7 by 13, and 121 is 11 by 11; 151, 181, 211 primes",
                        "● 211 is 210 and 1: the +1 of the seam of 2, 3, 5 and 7 multiplied",
                        "● 29 and 31, 59 and 61: two primes about a seam"), step=20, size=12)

# ================= the table: a name a row, its number on a pair of cones =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("on the cones", 190, 66, "right"), ("17 less", 262, 48, "right"), ("8 up", 316, 40, "right"),
        ("by position", 362, 66, "right"), ("at a seam", 440, 64, "left")]
over.append(word(TX, 196, 500, "a name a row · its number on a pair of cones · its prime by its position", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 504},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
names, prime_of = own["names"], own["prime_of"]
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="512" height="{RH:.1f}" fill="{PALE}"></rect>')
    x_ = c.ON_CONES[n]
    seam = "its +1" if n in (1, 9, 17) else "its −1" if n in (8, 16) else ""
    cells_ = [str(n), names[n], str(x_), str(60 - x_) if n <= 16 else "", str(x_ + 30) if n <= 9 else "", str(prime_of[n]), seam]
    for (t, x, w_, al), v in zip(cols, cells_):
        bold = t in ("n", "its name, Exhibit ONE's own") or (t == "on the cones" and c.is_prime(x_)) or t == "at a seam"
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if bold else 400, 11.2, 16, extra="font-variant-numeric: tabular-nums;"))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 504},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("on the cones: the sixteen cells of a pair of cones, 0 to 60, in their order; 17 at 61 · a prime in bold",
                       "17 less: its podal about 30, 60 less it · 8 up: 30 on",
                       "by position: its prime in the one table of the seventeen names, 2 to 59",
                       "at a seam: one on from 0, 30 and 60, its +1; one before 30 and 60, its −1")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= found, and what this drawing leaves with the nine =================
FX, FY = 1004, 652
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the nine", weight=600, size=15))
FOUND = [("the me's names at a seam's +1, same-existing at its −1", ["1, 9 and 17 at 1, 31 and 61; the 8th and 16th at 29 and 59: one bi-folding beside the seams"]),
         ("a name with two numbers, not one yet", ["its number on the cones is the prime of the name two on by position, from the 2nd name", "to the 13th; the 14th is at 49, 7 by 7"]),
         ("a podaling, said two ways in the nine", ["two folds, an other-than of an other-than, at the 10th; an other-than about a cone's widest", "and an all about a vertex, at the 11th. Both are laid"]),
         ("it is no method of a prime's existing", ["of 32 cells 27 are primes; the spiral of 7 crosses 49, 77, 91 and 119, past the seam's primes"]),
         ("with the nine drawings, as they were", ["the 9th's staircase on its geodesic; the 10th to the 13th's devices of a me-now; the 14th's my;", "the 15th's conscious me; the 16th's spans; the 17th's ten passings"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">Cones of 30 on a Co-Linear</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Podaling a Me-Now about a Seam of 30, to Its Next Universe</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "30 is 2 by 3 by 5, a seam. Eight of its thirty cells are crossed by none, a cone's eight, and 0 to 120 is four cones of 30 on the co-linear.<br>"
           "A pair of cones is sixteen cells, the names 1 to 16: 8 up is 30 on, 17 less a podaling about 30, and 17 is at 61, a next 1.<br>"
           "The names at the me, 1, 9 and 17, are at the seam's +1, and two of same-existing at its −1. A me-now's four moments carry 37 to 157, its next universe.<br>"
           "A candidate, the third figure of twelve, beside the nine drawings it gathers and writing in none.</div>")
ARIA = ("Five parts and a table. A line from 0 to 120 with four widths rising and falling over it, thirty-two numbered cells on them, the numbers 1 to 17 over the cells to 61, and four cells under the line. "
        "A table of four rows of four numbers. A table of four podalings. A grid of six rows by five columns with the numbers 0 to 29. Seven lines of the names at a seam. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("Cones of 30 on a Co-Linear", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft61.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft61_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft61_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
