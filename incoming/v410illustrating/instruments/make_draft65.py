"""v410illustrating · the maker of the 65th drawing: A Me-Parity in a Seam, Even, Odd, Even.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft65.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The eleventh figure of the reduced set, one drawing beside the five it gathers, the 49th and the 52nd to the 55th. It
goes by a partner's sayings of 27 November, and on from the marker, the 64th drawing. Its check is opened and
executed here, and no drawing is made with an is-not. Its numbers are the check's own.

Its placings, no execution says them: its five parts and its table side by side; the co-linear as a row of cells, a
seam of six a tinted cell and a me-parity a dark cell; two rows of cells one over the other, an arc 15 less and an
arrow a multiplying in of 2.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_65", os.path.join(HERE, "check_a_me_parity_in_a_seam_even_odd_even.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"
names, primes, rows, J = own["names"], own["primes"], own["rows"], c.join

W, H = 1520, 1150
GREY, SLATE, PALE = "#4a5160", "#475569", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
NUM = "font-variant-numeric: tabular-nums;"
s, over = [], []
def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def cellbox(x, y, w, h, n, kind, size=11.5):                              # a number's cell on the co-linear, by its kind
    fill, op, col, sw, st = {"me-parity": (INK, 1, "#ffffff", 1, INK), "seam": (ACC, 0.30, INK, 1.6, ACC), "even": (SLATE, 0.10, GREY, 1, INK),
                             "between": ("#ffffff", 1, INK, 1.8, ACC), "open": ("#ffffff", 1, "#8a93a3", 1, INK)}[kind]
    s.append(f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h}" fill="{fill}" fill-opacity="{op}" stroke="{st}" stroke-opacity="{1 if kind in ("seam", "between") else 0.4}" stroke-width="{sw}"></rect>')
    over.append(word(x, y, w, str(n), "center", 600 if kind in ("me-parity", "seam", "between") else 400, size, size + 4, col, NUM))

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "65 · figure 11 of twelve, a me-parity in a seam · it gathers the 49th and the 52nd to the 55th drawings · its prior figure: two primes with one torus, the 64th, the marker · "
                 "its next figures: living parities, and a me beside an other", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 840, "A me-parity is three cells: even, odd, even. Past 3 one of its evens is a seam of six.", size=20, h=28))
over.append(word(60, 108, 840, "It is the seam's +1 or its −1; a seam with one at both sides is two about one centre.", size=20, h=28))
over.append(word(60, 138, 840, "The eight between are four odd and four even: one step of 15 lays odd onto even.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names, a prime a name: its prior, its own and its next, three cells",
                       "Natural Numbers · a number a waist its prior and next straddle; 59 and 61 straddle 60 by one",
                       "Exhibit THIRTY, Natural Naming · a torus's seams; an other-than; a me-parity",
                       "Natural Illustrating · for its part of number forming and podaling")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · a me-parity in a seam of six, 0 to 36 =================
X1 = lambda n: 78 + 24.6 * n
over.append(word(60, 196, 920, "1 · a me-parity in a seam of six: even, odd, even · 0 to 37", weight=600, size=15))
for x, kind, t in ((66, "me-parity", "a me-parity"), (176, "seam", "a seam of six"), (300, "even", "an even number"), (430, "open", "an odd number, crossed")):
    cellbox(x + 8, 217, 18, 13, "", kind); over.append(word(x + 24, 217, 150, t, size=11.4, color=GREY))
for n in range(0, 38):
    kind = "seam" if n % 6 == 0 else "me-parity" if c.is_prime(n) else "even" if n % 2 == 0 else "open"
    cellbox(X1(n), 290, 22.6, 24, n, kind, 11.2)
for e in range(6, 37, 6):
    sd = c.sides(e); bothsides = len(sd) == 2
    over.append(word(X1(e), 250, 150, f"{e - 1} · {e} · {e + 1}", "center", 600, 11.2, 14, INK if bothsides else GREY, NUM))
    over.append(word(X1(e), 264, 150, "both: two about one centre" if bothsides else f"one side: {sd[0]}", "center", 600 if bothsides else 400, 10.4, 13, ACC if bothsides else GREY))
over.append(word(60, 322, 920, f"a me-parity past 3 is a seam of six's +1 or its −1: {J(own['minus'])} a −1, and {J(own['plus'])} a +1 · of the six seams, {J(own['both'])} are with a me-parity at both sides", size=11.6, h=14))
over.append(word(60, 339, 920, f"of the sixty seams of six to 360, {own['c360'][2]} are with a me-parity at both sides, {own['c360'][1]} at one, and {own['c360'][0]} at none", size=11.6, h=14, color=GREY))

# ================= 2 · the eight between, four odd and four even =================
X2 = lambda n: 78 + 29.2 * n
YA, YB = 436, 522
over.append(word(60, 372, 920, "2 · the eight between, four odd and four even: a partner's saying of 27 November", weight=600, size=15))
odd, even, mes = own["odd"], own["even"], own["mes"]
for n in range(0, 16):
    kind = "me-parity" if n in odd else "between" if n in even else "seam" if n in (0, 15) else "open"
    cellbox(X2(n), YA, 26, 24, n, kind, 11.6)
for n in range(0, 31):
    kind = "me-parity" if n in mes else "seam" if n % 6 == 0 else "even" if n % 2 == 0 else "open"
    cellbox(X2(n), YB, 26, 24, n, kind, 11.6)
    if n in mes: over.append(word(X2(n), YB + 21, 30, "+1" if n in own["mes_plus"] else "−1", "center", 600, 9.6, 12, ACC if n in own["mes_plus"] else SLATE))
for a in odd:                                                             # an arc: 15 less, an odd onto an even
    b = 15 - a; x1, x2 = sorted((X2(a), X2(b))); hgt = 8 + 2.6 * abs(b - a)
    s.append(f'<path d="M{x1:.1f},{YA - 13} Q{(x1 + x2) / 2:.1f},{YA - 13 - hgt:.1f} {x2:.1f},{YA - 13}" fill="none" stroke="{SLATE}" stroke-opacity="0.8" stroke-width="1.3" stroke-dasharray="3 3"></path>')
for a in odd:                                                             # an arrow: 2 multiplied in, an odd as it is
    s.append(f'<path d="M{X2(a):.1f},{YA + 13} L{X2(a):.1f},{YB - 15}" fill="none" stroke="{INK}" stroke-width="1.3"></path><path d="M{X2(a):.1f},{YB - 12} l-3.6,-7 l7.2,0 Z" fill="{INK}"></path>')
for a in even:                                                            # an arrow: an even 15 on
    x1, x2 = X2(a), X2(a + 15)
    s.append(f'<path d="M{x1:.1f},{YA + 13} L{x2:.1f},{YB - 15}" fill="none" stroke="{ACC}" stroke-width="1.3"></path><circle cx="{x2:.1f}" cy="{YB - 15}" r="2.6" fill="{ACC}"></circle>')
over.append(word(X2(15) + 26, YA - 26, 420, f"a torus of 3 by 5, 0 to 15: four odd, {J(odd)}; four even, {J(even)}", size=11.6, h=14, weight=600))
over.append(word(X2(15) + 26, YA - 10, 420, "a dashed arc: 15 less, odd onto even · 0 and 15 are one cell, the opening", size=11.4, h=14, color=GREY))
over.append(word(X2(15) + 26, YA + 6, 420, "a dark arrow: 2 multiplied in, an odd as it is · an accent line: an even, 15 on", size=11.4, h=14, color=GREY))
over.append(word(60, YB + 42, 920, f"with 2 multiplied in the eight are a row's eight mes of 30: four at a seam of six's +1, {J(own['mes_plus'])}, and four at its −1, {J(own['mes_minus'])} · 30 less lays a +1 onto a −1", size=11.6, h=14))
over.append(word(60, YB + 59, 920, "of the eight, 1 with 2, 7 with 8 and 13 with 14 are an odd and its next even; 11 is with a crossing at both sides; and 4 is the centre of the torus's own two, 3 and 5", size=11.6, h=14, color=GREY))

# ================= 3 · two me-parities about one centre =================
over.append(word(60, 612, 920, "3 · two me-parities about one centre: a seam with a me-parity at both its sides", weight=600, size=15))
P3 = [pq for pq in own["pairs"] if pq[0] <= 59][:6]
R3 = [("two me-parities", [f"{p} and {q}" for p, q in P3]), ("their centre, a seam of six", [p + 1 for p, q in P3]), ("the two multiplied: the centre's square less 1", [p * q for p, q in P3])]
for i, (label, vals) in enumerate(R3):
    y = 638 + 19 * i
    if i == 1: s.append(f'<rect x="56" y="{y - 9.5}" width="926" height="19" fill="{ACC}" fill-opacity="0.10"></rect>')
    over.append(word(60, y, 300, label, weight=600, size=11.8, h=15, color=GREY if i == 0 else INK))
    for j, v in enumerate(vals): over.append(word(380 + 98 * j + 86, y, 86, str(v), "right", 600 if i < 2 else 400, 11.8, 15, extra=NUM))
s.append(f'<path d="M60,648 L980,648" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
over.append(word(60, 702, 920, f"their centre is crossed by neither, and their two crossings are together next at the centre's square less 1, the 64th's torus: at all {own['npairs']} to 10,000", size=11.6, h=14))
over.append(word(60, 719, 920, f"a seam's cells with a me at both sides are {J(own['counts'])}, at the seams {J(c.SEAMS)}: with a me-parity multiplied in, that many by the me-parity less 2", size=11.6, h=14, color=GREY))

# ================= 4 · a +1 at a seam, six figures =================
over.append(word(60, 752, 920, "4 · a +1 at a seam, six figures", weight=600, size=15))
over.append(word(60, 774, 920, "the 60th: on a cube's line · the 61st: the names at a me · the 62nd: a centre's square · the 63rd: a me-parity's square · the 64th: a torus's opening", size=12, h=15))
over.append(word(60, 792, 920, "the 65th: a me-parity its own, a seam of six's +1 or its −1; and of two about one centre, both, the seam between them", size=12, h=15))

# ================= 5 · with the 55th, and from the marker =================
over.append(word(60, 826, 920, "5 · with the 55th, and from the marker", weight=600, size=15))
over.append(word(60, 847, 920, "a path closing, all its mes gone through, says with all numbers; a simulation is a breaking test alone: the 55th drawing's saying", size=11.8, h=15))
over.append(word(60, 864, 920, "two about one centre with no last is a field's open asking, and no line here says it · it goes on from the marker, the 64th drawing", size=11.8, h=15))
over.append(word(60, 881, 920, "the marker: a between is one thing from two sides, a partner's is. At an is-not, the incohering is sought, and the work is laid on from it, a next laying.", size=11.8, h=15))

# ================= the table: a name a row, its prime as three cells =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("even · odd · even", 192, 84, "center"), ("of six", 280, 40, "right"), ("at", 328, 40, "left"), ("of 4", 370, 32, "right"),
        ("about one centre", 410, 96, "left")]
over.append(word(TX, 196, 500, "a name a row · its prime as three cells · its seam of six, and of 4", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else w_ / 2 if al == "center" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 508},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7; a, p, b, s6, at_, s4 = rows[n]
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="516" height="{RH:.1f}" fill="{PALE}"></rect>')
    ctr = own["centre"].get(n)
    cells_ = [str(n), names[n], f"{a} · {p} · {b}", str(s6) if s6 else "", at_, str(s4) if s4 else "", f"{ctr}, with {p + 2}" if ctr else ""]
    for (t, x, w_, al), v in zip(cols, cells_):
        bold = t in ("n", "its name, Exhibit ONE's own", "of six", "at")
        over.append(word(TX + x + (w_ if al == "right" else w_ / 2 if al == "center" else 0), y, w_, v, al, 600 if bold else 400, 11.2 if t != "about one centre" else 10.6, 16,
                         ACC if (t == "at" and v == "its +1") else INK, extra=NUM))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 508},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("even · odd · even: its prior, its own, its next; 2 is the one even me-parity",
                       "of six, at: its even that is a seam of six, and itself its +1 or its −1; 2 and 3 are with none",
                       "of 4: its even that is a seam of 4, the 52nd drawing's aim",
                       "about one centre: its centre, with its next name's prime 2 on; the 17th with 61")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= found, and what this drawing leaves with the five =================
FX, FY = 1004, 640
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the five", weight=600, size=15))
FOUND = [("a me-parity is a seam of six's +1 or its −1", ["even, odd, even: past 3 its seam is its prior or its next"]),
         ("the eight between: four odd and four even, a partner's", ["15 less lays odd onto even; with 2 multiplied in they are a row's eight mes,", "four at a seam of six's +1 and four at its −1"]),
         ("two about one centre: a seam, and both its +1 and its −1", ["their crossings are together next at the centre's square less 1"]),
         ("it is no method, and no saying of two with no last", ["known mathematics; two about one centre with no last is a field's open asking"]),
         ("with the five drawings, as they were", ["the 49th's marks and measurings; the 52nd's aims; the 53rd's two paths;", "the 54th's nine spans; the 55th's closing paths, and a simulation a breaking test"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">A Me-Parity in a Seam, Even, Odd, Even</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Resolving a Prime Gap of 2 about a Seam of 6, Its −1 and Its +1 Both Me-Parities</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "A me-parity is three cells, even, odd, even. Past 3 one of its evens is a seam of six, and the me-parity is the seam's +1 or its −1.<br>"
           "A seam of six with a me-parity at both its sides is two about one centre: their crossings are together next at the centre's square less 1.<br>"
           "The eight between of a torus of 3 by 5 are four odd and four even. 15 less lays odd onto even, and with 2 multiplied in they are a row's eight mes.<br>"
           "A candidate, the eleventh figure of twelve, beside the five drawings it gathers and writing in none.</div>")
ARIA = ("Five parts and a table. A row of cells numbered 0 to 37, a dark cell a prime and a tinted cell a multiple of six. Two rows of cells, 0 to 15 over 0 to 30, with arcs and arrows between them. "
        "A table of six pairs of primes about one centre. Four lines. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("A Me-Parity in a Seam, Even, Odd, Even", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft65.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft65_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft65_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
