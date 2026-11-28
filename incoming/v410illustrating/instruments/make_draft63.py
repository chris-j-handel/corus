"""v410illustrating · the maker of the 63rd drawing: Rows of 30, Eight Mes a Row.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft63.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The ninth figure of the reduced set, one drawing beside the three it gathers, the 38th, the 46th and the 56th. By a
partner's aiming of 27 November it goes on showing how the +1s are living in the seams of natural torusing.
Its check is opened and executed here, and no drawing is made with an is-not.

Its placings, no execution says them: its five parts and its table side by side; twelve rows as a table of eight
columns; a dark cell a me-parity, an accent edge a square, a crossed me with its least crossing beside it; a
me-parity's square as a dark mark on the co-linear, a seam of 30 over it and a seam of 24 under it.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_63", os.path.join(HERE, "check_rows_of_30_eight_mes_a_row.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"
names, primes, per_row, spans = own["names"], own["primes"], own["per_row"], own["spans"]

W, H = 1520, 1150
GREY, SLATE, PALE = "#4a5160", "#475569", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
s, over = [], []

def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def dot(x, y, r, fill, stroke=INK, sw=1.2, op=1): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"></circle>'
NUM = "font-variant-numeric: tabular-nums;"

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "63 · figure 9 of twelve, the rows of 30, eight mes a row · it gathers the 38th, the 46th and the 56th drawings · its prior figure: the diamond of nine, the 62nd · "
                 "its next figures: a me beside an other, and living parities", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 840, "A row of 30 is eight mes: its cells crossed by none of 2, 3 and 5.", size=20, h=28))
over.append(word(60, 108, 840, "A me crossed by none of its priors is a next me-parity; a seam's +1 says no last.", size=20, h=28))
over.append(word(60, 138, 840, "A me-parity's own crossing opens at its square: its prior by its next, and 1.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names, a prime a name: 2, 3 and 5 the seam's own, 7 to 59 its two rows",
                       "Natural Numbers · primes with no last; a +1 between a centre's square and its prior by its next",
                       "Exhibit THIRTY, Natural Naming · a torus's seams and its spirals crossing; scales of primes",
                       "Natural Illustrating · for its part of number forming and podaling")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · rows of 30, eight mes a row =================
GX, GY, CW, CH = 106, 256, 44, 23.5
over.append(word(60, 196, 440, "1 · rows of 30, eight mes a row: 1 to 359", weight=600, size=15))
s.append(f'<rect x="64" y="210" width="20" height="13" fill="{INK}"></rect>'); over.append(word(89, 216, 90, "a me-parity", size=11.4, color=GREY))
s.append(f'<rect x="166" y="210" width="20" height="13" fill="#ffffff" stroke="{INK}" stroke-opacity="0.45" stroke-width="1"></rect>'); over.append(word(191, 216, 150, "crossed, by its least", size=11.4, color=GREY))
s.append(f'<rect x="316" y="210" width="20" height="13" fill="#ffffff" stroke="{ACC}" stroke-width="2.4"></rect>'); over.append(word(341, 216, 170, "a square: a crossing opens", size=11.4, color=GREY))
over.append(word(98, 244, 44, "from", "right", 600, 10.4, 13, GREY))
for q, m in enumerate(c.MES):
    over.append(word(GX + q * CW + CW / 2, 244, CW, f"the me {m}" if q == 0 else str(m), "center", 600, 10.8, 13, GREY))
over.append(word(GX + CW / 2, 231, CW + 20, "a seam's +1", "center", 600, 10, 12, ACC)); over.append(word(GX + 7 * CW + CW / 2, 231, CW + 20, "its −1", "center", 600, 10, 12, SLATE))
s.append(f'<rect x="{GX}" y="{GY}" width="{CW}" height="{CH * c.ROWS}" fill="{ACC}" fill-opacity="0.10"></rect>')
for r in range(c.ROWS):
    y = GY + r * CH
    over.append(word(98, y + CH / 2, 40, str(30 * r), "right", 600 if r == 7 else 400, 10.8, 13, ACC if r == 7 else GREY, NUM))
    over.append(word(GX + 8 * CW + 8, y + CH / 2, 30, str(per_row[r]), "left", 400, 10.8, 13, GREY, NUM))
    for q, n in enumerate(c.row(r)):
        x = GX + q * CW; square = int(round(n ** 0.5)) ** 2 == n and n > 1
        if c.is_prime(n):
            s.append(f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{CW - 3}" height="{CH - 3}" fill="{INK}"></rect>')
            over.append(word(x + CW / 2, y + CH / 2, CW, str(n), "center", 600, 11.2, 14, "#ffffff", NUM))
        else:
            s.append(f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{CW - 3}" height="{CH - 3}" fill="#ffffff" stroke="{ACC if square else INK}" stroke-opacity="{1 if square else 0.35}" stroke-width="{2.4 if square else 1}"></rect>')
            t = "1" if n == 1 else f'{n}<span style="font-size: 9px; color: {ACC}; font-weight: 600">·{c.least(n)}</span>'
            over.append(word(x + CW / 2, y + CH / 2, CW, t, "center", 400, 11.2, 14, GREY, NUM))
s.append(f'<path d="M{GX - 44},{GY + 7 * CH} L{GX + 8 * CW + 26},{GY + 7 * CH}" fill="none" stroke="{ACC}" stroke-width="1.4" stroke-dasharray="4 4"></path>')
yb1 = GY + c.ROWS * CH
over.append(word(60, yb1 + 12, 440, "at a row's far side, its me-parities · 96 mes: 69 me-parities, 26 crossed, and 1", size=11.3, h=14, color=GREY))
over.append(word(60, yb1 + 28, 440, "seven rows are a seam of 210: 56 mes, eight crossed by 7, and 48 its cells", size=11.3, h=14, color=GREY))

# ================= 2 · a next me-parity, from its own priors =================
over.append(word(530, 196, 450, "2 · a next me-parity, from its own priors", weight=600, size=15))
over.append(word(530, 216, 450, "from a me-parity's square to its next's: a me crossed by none of its priors", size=11.5, h=14, color=GREY))
for t, x, al in (("a span", 530, "left"), ("its priors' crossings", 632, "left"), ("mes", 838, "right"), ("crossed", 900, "right"), ("me-parities", 976, "right")):
    over.append(word(x, 240, 100 if al == "left" else 62, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M530,250 L978,250" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
ROWS2 = [("under 49", "the seam's own: 2, 3 and 5", 12, 0, 12)] + [(f"{p * p} to {q * q}", {7: "7", 11: "7 and 11", 13: "7, 11 and 13", 17: "7, 11, 13 and 17"}[p], a, b, d) for p, q, a, b, d, _ in spans]
for i, (a, b, m_, x_, p_) in enumerate(ROWS2):
    y = 263 + 19 * i
    if i % 2: s.append(f'<rect x="526" y="{y - 9.5}" width="456" height="19" fill="{PALE}"></rect>')
    over.append(word(530, y, 100, a, weight=600, size=11.6, h=15, extra=NUM)); over.append(word(632, y, 170, b, size=11.6, h=15))
    for v, x in ((m_, 838), (x_, 900), (p_, 976)): over.append(word(x, y, 50, str(v), "right", 600 if x == 976 else 400, 11.6, 15, extra=NUM))
over.append(word(530, 364, 450, "a me-parity's own crossing opens at its square: 7 by 7, 11 by 11, 13 by 13, 17 by 17", size=11.5, h=14))
over.append(word(530, 380, 450, "under its square, a number it crosses is crossed by a prior", size=11.5, h=14, color=GREY))

# ================= 3 · a seam with its next me-parity multiplied in, and its +1 =================
over.append(word(530, 410, 450, "3 · a seam with its next me-parity multiplied in, and its +1", weight=600, size=15))
over.append(word(530, 430, 450, "a seam's cells are its prior's, by its me-parity less 1", size=11.5, h=14, color=GREY))
LIFT = ["", "3", "5", "7", "11", "13"]
R3 = [("a seam", [str(x) for x in c.SEAMS]), ("multiplied in", LIFT), ("its cells", [str(c.cells(x)) for x in c.SEAMS]), ("its +1", [str(x) for x in own["plus"]]), ("its −1", [str(x) for x in own["less"]])]
for i, (label, vals) in enumerate(R3):
    y = 454 + 19 * i
    if i in (3,): s.append(f'<rect x="526" y="{y - 9.5}" width="456" height="19" fill="{ACC}" fill-opacity="0.10"></rect>')
    over.append(word(530, y, 90, label, weight=600, size=11.6, h=15, color=GREY if i < 3 else INK))
    for j, v in enumerate(vals):
        mp = i >= 3 and v.isdigit() and c.is_prime(int(v))
        over.append(word(620 + 58 * j + 56, y, 56, v, "right", 600 if (mp or i == 0) else 400, 11.6, 15, INK if (i < 3 or mp) else "#8a93a3", NUM))
s.append(f'<path d="M530,464 L978,464" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
over.append(word(530, 548, 450, "its +1 is crossed by none of the seam's own: a next me-parity, with no last", size=11.5, h=14))
over.append(word(530, 564, 450, "30031 is 59 by 509, and 209 is 11 by 19: crossed, past the seam's own", size=11.5, h=14, color=GREY))

# ================= 4 · a me-parity's square on the co-linear =================
X0, U, Y0 = 84.0, 2.4, 706.0
X = lambda n: X0 + U * n
over.append(word(60, 596, 920, "4 · a me-parity's square on the co-linear: one on from a seam of 24, and at the me 1 or the me 19 of a row", weight=600, size=15))
over.append(word(60, 615, 920, "over the co-linear a seam of 30, 0 to 360; under it a seam of 24 · a dark mark a square, one on from its prior by its next", size=11.5, h=14, color=GREY))
s.append(f'<path d="M{X(0) - 12:.1f},{Y0} L{X(368):.1f},{Y0}" fill="none" stroke="{INK}" stroke-width="1.5"></path>')
s.append(f'<path d="M{X(368):.1f},{Y0} l-9,-4.5 l0,9 Z" fill="{INK}"></path>')
for t_ in range(0, 361, 30):
    s.append(f'<path d="M{X(t_):.1f},{Y0} L{X(t_):.1f},{Y0 - 9}" fill="none" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"></path>')
    over.append(word(X(t_), Y0 - 17, 26, str(t_), "center", 400, 9.6, 12, SLATE, NUM))
SQ = {25: 5, 49: 7, 121: 11, 169: 13, 289: 17, 361: 19}
for t_ in range(0, 361, 24):
    seam = (t_ + 1) in SQ; both = t_ % 30 == 0
    s.append(f'<path d="M{X(t_):.1f},{Y0} L{X(t_):.1f},{Y0 + (13 if seam or both else 8)}" fill="none" stroke="{ACC}" stroke-width="{2.4 if seam or both else 1.6}" stroke-linecap="round"></path>')
    if seam or both: over.append(word(X(t_), Y0 + 22, 30, str(t_), "center", 600, 9.8, 12, ACC, NUM))
for t_, t in ((120, "both seams"), (240, "both: 241 a me-parity"), (360, "both seams")):
    over.append(word(min(X(t_), 978 - 34), Y0 + 35, 130, t, "center", 400, 9.6, 12, GREY))
for n, p in SQ.items():
    x = X(n); s.append(dot(x, Y0, 5.2, INK, INK, 1.4))
    if n == 25:
        s.append(f'<path d="M{x:.1f},{Y0 + 6} L{x:.1f},{Y0 + 44}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1"></path>')
        over.append(word(x, Y0 + 52, 150, "25 · 5 by 5 · 24 and 1", "center", 600, 10.8, 13, extra="background: #ffffff;"))
        over.append(word(x, Y0 + 66, 150, "5 is the seam's own", "center", 400, 10.2, 13, GREY))
    else:
        xm = min(x, 978 - 62)
        s.append(f'<path d="M{x:.1f},{Y0 - 6} L{x:.1f},{Y0 - 40}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1"></path>')
        over.append(word(xm, Y0 - 62, 124, f"{n} · {p} by {p}", "center", 600, 11, 13, extra="background: #ffffff;"))
        over.append(word(xm, Y0 - 48, 124, f"{n - 1} and 1 · the me {n % 30}", "center", 600, 10.6, 13, ACC, extra="background: #ffffff;"))
over.append(word(60, 786, 920, "past 3 a me-parity's seam is twenty-fours: 2 at 7, 5 at 11, 7 at 13, 12 at 17 and 15 at 19 · 121 and 361 are one on from both seams, at the me 1; 49, 169 and 289 at the me 19", size=11.5, h=14, color=GREY))
over.append(word(60, 803, 920, "59 by 61 is 60 by 60 less 1, Natural Numbers' own saying: two rows are a centre, 60, and its prior and its next are me-parities, a seam of 30's −1 and its +1", size=11.5, h=14, color=GREY))

# ================= 5 · a +1 at a seam, four figures =================
over.append(word(60, 836, 920, "5 · a +1 at a seam, four figures", weight=600, size=15))
over.append(word(60, 858, 920, "the 60th: on a cube's line, six round it · the 61st: the names at a me, 30 on a round · the 62nd: a centre's square, eight round a middle", size=12, h=15))
over.append(word(60, 876, 920, "the 63rd: a me-parity's square, its own crossing's opening; and a seam's +1 crossed by none of the seam's own, a next me-parity with no last", size=12, h=15))

# ================= the table: a name a row, its prime in the rows =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("its prime", 192, 48, "right"), ("a row · a me", 254, 80, "left"), ("a seam", 328, 46, "right"),
        ("of 24", 378, 34, "right"), ("its square", 416, 52, "right"), ("its me", 472, 32, "right")]
over.append(word(TX, 196, 500, "a name a row · its prime in the rows · its seam and its square", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 504},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7; p = primes[n]
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="512" height="{RH:.1f}" fill="{PALE}"></rect>')
    cells_ = [str(n), names[n], str(p), "the seam's own" if p < 7 else f"{30 * (p // 30)} · {p % 30}", str(p * p - 1), str((p * p - 1) // 24) if p > 3 else "", str(p * p), str((p * p) % 30) if p > 5 else ""]
    for (t, x, w_, al), v in zip(cols, cells_):
        bold = t in ("n", "its name, Exhibit ONE's own", "its prime", "its square")
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if bold else 400, 11.2, 16, extra=NUM))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 504},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its prime: by its position, of the one table of the seventeen names",
                       "a row · a me: the row's opening number, and the prime's me of the eight",
                       "a seam, its square: its prior by its next, and 1 more · of 24: the seam's twenty-fours",
                       "its me: the square's me of a row, 1 or 19")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= found, and what this drawing leaves with the three =================
FX, FY = 1004, 640
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the three", weight=600, size=15))
FOUND = [("a me-parity's own crossing opens at its square, a seam's +1", ["7 by 7, 11 by 11, 13 by 13 and 17 by 17: 49, 121, 169 and 289, one on from twenty-fours"]),
         ("the names' primes, in the rows of 30", ["the seam of 30 is the primes of the names 1, 2 and 3 multiplied; the names 4 to 17", "are with the fourteen me-parities of its two opening rows, 7 to 59"]),
         ("a me-parity, said two ways, not one yet", ["Exhibit ONE says it of a name's slot, co, with existing; the 56th drawing of a me", "crossed by none of its priors, a prime. Both are laid"]),
         ("it is no method of a far me-parity alone", ["the field's sieve with a wheel, known: a next me-parity is come to by its priors' crossings"]),
         ("with the three drawings, as they were", ["the 38th's two faces and its measurings; the 46th's six fixings;", "the 56th's four reasons and its is-nots"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">Rows of 30, Eight Mes a Row</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Living a Next Me-Parity from Its Own Priors, a Seam\'s +1 at Its Square</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "A row of 30 is eight mes, its cells crossed by none of 2, 3 and 5. A me crossed by none of its priors is a next me-parity, and a seam's +1 says no last.<br>"
           "A me-parity's own crossing opens at its square, its prior by its next and 1: 49, 121, 169 and 289, one on from 48, 120, 168 and 288, twenty-fours.<br>"
           "The seam of 30 is the primes of the names 1, 2 and 3 multiplied, and the names 4 to 17 are with the me-parities of its two opening rows.<br>"
           "A candidate, the ninth figure of twelve, beside the three drawings it gathers and writing in none.</div>")
ARIA = ("Five parts and a table. A table of twelve rows by eight columns of numbers, 1 to 359, a dark cell a prime. A table of five spans. A table of six seams with their cells. "
        "A line from 0 to 360 with marks over it at thirties and under it at twenty-fours, and six dark marks at squares. Two lines of four figures. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("Rows of 30, Eight Mes a Row", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft63.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft63_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft63_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
