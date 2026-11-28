"""v410illustrating · the maker of the 66th drawing: Living Parities of the Numbers.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft66.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

The eighth figure of the reduced set, one drawing beside the three it gathers, the 36th, the 37th and the 39th. It
goes by a partner's sayings of 27 November, and on from the marker, the 64th drawing. Its check is opened and
executed here, and no drawing is made with an is-not. Its numbers are the check's own.

Its placings, no execution says them: its six parts and its table side by side; four rows of 30 as a table, a dark
cell a + and an open cell a −; the 2s and the 3s as a board of two tints; a row of fifteen cells for the eight.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the artboard's page, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_66", os.path.join(HERE, "check_living_parities_of_the_numbers.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"
names, primes, J, L = own["names"], own["primes"], c.join, c.living

W, H = 1520, 1150
GREY, SLATE, PALE = "#4a5160", "#475569", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
NUM = "font-variant-numeric: tabular-nums;"
s, over = [], []
def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def cellbox(x, y, w, h, n, sign, edge=False, size=11.2, pale=False):       # a number's cell: dark a +, open a −
    plus = sign == "+"
    fill, col = (INK, "#ffffff") if plus else ("#ffffff", INK)
    if pale: fill, col = PALE, "#8a93a3"
    s.append(f'<rect x="{x - w / 2 + 1:.1f}" y="{y - h / 2 + 1:.1f}" width="{w - 2}" height="{h - 2}" fill="{fill}" stroke="{ACC if edge else INK}" stroke-opacity="{1 if edge else 0.45}" stroke-width="{2.4 if edge else 1}"></rect>')
    over.append(word(x, y, w, str(n), "center", 600 if (plus or edge) else 400, size, size + 4, col, NUM))

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "66 · figure 8 of twelve, living parities of the numbers · it gathers the 36th, the 37th and the 39th drawings · its prior figure: a me-parity in a seam, the 65th · "
                 "its next figures: a me beside an other, and a path of mes", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 840, "A number's living parity is a + or a −: a prime multiplied in is one other-than.", size=20, h=28))
over.append(word(60, 108, 840, "A me-parity is a −, its square a +; a seam with one multiplied in is one other-than.", size=20, h=28))
over.append(word(60, 138, 840, "Past the window a seam's torus says a cell between, and not its living parity.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names, a name's own number and its prime: a + or a −",
                       "Natural Numbers · a +1 between a centre's square and its prior by its next",
                       "Exhibit THIRTY, Natural Naming · an other-than; an other-than of an other-than; a parity",
                       "Natural Illustrating · for its part of number forming and podaling")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · a number's living parity, 1 to 120 =================
over.append(word(60, 196, 920, "1 · a number's living parity, 1 to 120: four rows of 30", weight=600, size=15))
cellbox(74, 218, 20, 15, "", "+"); over.append(word(90, 218, 250, "a +: an even number of primes multiplied in", size=11.4, color=GREY))
cellbox(352, 218, 20, 15, "", "−"); over.append(word(368, 218, 250, "a −: an odd number of primes multiplied in", size=11.4, color=GREY))
cellbox(626, 218, 20, 15, "", "−", edge=True); over.append(word(642, 218, 250, "an accent edge: a me-parity, one prime, a −", size=11.4, color=GREY))
X1 = lambda q: 80 + 29.2 * q
for r in range(4):
    for q in range(30):
        n = 30 * r + q + 1; cellbox(X1(q), 252 + 27 * r, 28.4, 25, n, L(n), edge=c.is_prime(n), size=10.6)
    over.append(word(X1(29) + 20, 252 + 27 * r, 60, f"{own['plus'][r]} · {30 - own['plus'][r]}", size=10.6, h=13, color=GREY, extra=NUM))
over.append(word(60, 352, 920, f"at a row's far side, its +s and its −s: {J(own['plus'])} are a +, and {J(30 - x for x in own['plus'])} a − · 1 is a +, and a me-parity a −", size=11.6, h=14))

# ================= 2 · multiplying in a prime, one other-than at a step =================
over.append(word(60, 388, 360, "2 · multiplying in a prime: one other-than a step", weight=600, size=15))
over.append(word(60, 408, 360, "the 2s and the 3s: by 2 a column on, by 3 a row on", size=11.5, h=14, color=GREY))
for b in range(4):
    for a in range(5):
        n = own["lat"][b][a]; cellbox(98 + 58 * a, 436 + 26 * b, 56, 24, n, L(n), size=11.6)
over.append(word(60, 540, 360, "a + and a − are next to one another at all steps", size=11.5, h=14, color=GREY))

# ================= 3 · a seam with a me-parity multiplied in is one other-than =================
over.append(word(430, 388, 550, "3 · a me-parity multiplied in a seam is one other-than; its square a +", weight=600, size=15))
R3 = [("a seam", [str(x) for x in c.SEAMS], None), ("its living parity", own["sp"], None),
      ("its −1", [str(x - 1) for x in c.SEAMS], [L(x - 1) for x in c.SEAMS]), ("its +1", [str(x + 1) for x in c.SEAMS], [L(x + 1) for x in c.SEAMS])]
for i, (label, vals, signs) in enumerate(R3):
    y = 418 + 21 * i
    over.append(word(430, y, 110, label, weight=600, size=11.6, h=15, color=GREY if i == 0 else INK))
    for j, v in enumerate(vals):
        x = 560 + 70 * j + 30
        if i == 1: cellbox(x, y, 26, 18, v, v, size=11.6)
        elif signs: cellbox(x, y, 56, 18, v, signs[j], edge=c.is_prime(int(v)), size=10.8)
        else: over.append(word(x, y, 60, v, "center", 600, 11.6, 15, extra=NUM))
over.append(word(430, 506, 550, "a seam is a − and a + in sequence: a me-parity multiplied in, one other-than", size=11.5, h=14))
over.append(word(430, 522, 550, "a side that is a me-parity is a − · a me-parity's square is a +", size=11.5, h=14, color=GREY))
over.append(word(430, 538, 550, f"two about one centre multiplied are a +: {J(p * q for p, q in own['two'][:5])}", size=11.5, h=14, color=GREY))

# ================= 4 · past the window =================
o1, o2 = own["out"]
over.append(word(60, 574, 920, "4 · past the window: a cell between, and its living parity not said", weight=600, size=15))
over.append(word(60, 596, 920, f"at {o1[0]}, past {o1[1]}: of {o1[2]} cells between the crossings, {o1[3]} are a − and {o1[4]} a + · at {o2[0]}, past {o2[1]}: of {o2[2]}, {o2[3]} are a − and {o2[4]} a +", size=12, h=15))
over.append(word(60, 614, 920, f"a − is a me-parity, and at {o2[0]} one of three primes multiplied, {J(o2[6])}; a + is two primes past the seam's own, multiplied · the seam's torus says a cell between, and none of which", size=11.6, h=14, color=GREY))

# ================= 5 · the eight between, their living parities =================
over.append(word(60, 652, 920, "5 · the eight between of a torus of 3 by 5, their living parities", weight=600, size=15))
X5 = lambda n: 84 + 31 * n
for n in range(15):
    if n in own["eight"]: cellbox(X5(n), 690, 28, 25, n, own["le"][n], size=11.6)
    else: cellbox(X5(n), 690, 28, 25, n, "−", pale=True, size=11.6)
le = own["le"]
over.append(word(X5(14) + 30, 682, 440, "a doubling, 1, 2, 4 and 8, is + − + −: a prime multiplied in a step", size=11.6, h=14))
over.append(word(X5(14) + 30, 698, 440, "7 a − and 14 a +; 11 and 13 a − · a pale cell: on a crossing", size=11.6, h=14, color=GREY))
odd_p = [n for n in own["eight"] if n % 2 and le[n] == "+"]; even_p = [n for n in own["eight"] if n % 2 == 0 and le[n] == "+"]
over.append(word(60, 724, 920, f"odd and even is no living parity: of the four odd, {J(odd_p)} is a +; of the four even, {J(even_p)} are a + · a partner's parting of the eight, and this, are two partings", size=11.6, h=14))

# ================= 6 · with the 36th and the 39th, and from the marker =================
over.append(word(60, 762, 920, "6 · with the 36th and the 39th, and from the marker", weight=600, size=15))
over.append(word(60, 784, 920, "the 36th: a field's zeros on a line · the 39th: a longer co-chain gathering the staircase of the me-parities · a field's arithmetic: no line here executes a zero", size=11.6, h=14))
over.append(word(60, 801, 920, "the table of interests' rows 49 and 61 are of this living parity: odd and even close to alike, and crossings not saying a me-parity. This drawing resolves neither", size=11.6, h=14, color=GREY))
over.append(word(60, 818, 920, "by a partner's is, a whole reason is a sentence of a seam and its next, under the window: a me-parity multiplied in, one other-than, is of that form; it is no reason for a row", size=11.6, h=14, color=GREY))
over.append(word(60, 846, 920, "it goes on from the marker, the 64th drawing: a between is one thing from two sides, a partner's is.", size=11.8, h=15, weight=600))
over.append(word(60, 864, 920, "At an is-not, the incohering is sought, and the work is laid on from it, a next laying.", size=11.8, h=15))

# ================= the table: a name a row =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("its number's primes", 196, 110, "left"), ("a", 306, 24, "center"), ("its prime", 334, 50, "right"), ("a", 390, 24, "center"),
        ("its square", 418, 58, "right"), ("a", 482, 24, "center")]
over.append(word(TX, 196, 500, "a name a row · its own number, its prime and its square: a + or a −", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else w_ / 2 if al == "center" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 508},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7; p = primes[n]; pr, sg = own["own_rows"][n]
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="516" height="{RH:.1f}" fill="{PALE}"></rect>')
    over.append(word(TX + 20, y, 20, str(n), "right", 600, 11.2, 16, extra=NUM)); over.append(word(TX + 28, y, 164, names[n], weight=600, size=11.2, h=16))
    over.append(word(TX + 196, y, 110, pr, size=10.8, h=16, extra=NUM)); cellbox(TX + 318, y, 20, 16, sg, sg, size=10.6)
    over.append(word(TX + 384, y, 50, str(p), "right", 600, 11.2, 16, extra=NUM)); cellbox(TX + 402, y, 20, 16, L(p), L(p), size=10.6)
    over.append(word(TX + 476, y, 58, str(p * p), "right", 400, 11.2, 16, extra=NUM)); cellbox(TX + 494, y, 20, 16, L(p * p), L(p * p), size=10.6)
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 508},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its number's primes: the primes multiplied in a name's own number, 1 to 17",
                       "a: its living parity, a dark + or an open −, the 37th drawing's naming",
                       "its prime: by its position, a −, one prime · its square: a +, two")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= found, and what this drawing leaves with the three =================
FX, FY = 1004, 630
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the three", weight=600, size=15))
FOUND = [("a prime multiplied in is one other-than", ["a me-parity a −, its square a +, and a seam and its next a − and a +"]),
         ("a living parity, and odd and even: two partings, not one", ["a + and a − by the primes multiplied in, the 37th's naming; an other-than-all", f"of an even, a partner's: of the four odd of the eight, {J(odd_p)} is a +"]),
         ("past the window, a living parity is not said", [f"at {o1[0]}, {o1[3]} a − and {o1[4]} a +: the table of interests' rows 49 and 61"]),
         ("it is no method, and it resolves no interest", ["known mathematics: a field's function of the primes multiplied in a number"]),
         ("with the three drawings, as they were", ["the 36th's zeros on a line; the 37th's between going through the numbers;", "the 39th's co-chain gathering a staircase: a field's arithmetic, not executed here"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">Living Parities of the Numbers</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Multiplying In a Prime as One Other-Than, a Seam and Its Next a − and a +</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "A number's living parity is a + with an even number of primes multiplied in it, and a − with an odd number. A prime multiplied in is one other-than.<br>"
           "A me-parity is a −, and its square a +. A seam with a me-parity multiplied in is one other-than: the seams 2, 6, 30, 210, 2310 and 30030 are − + − + − +.<br>"
           "Past the window a seam's torus says a cell between the crossings, and not its living parity. Odd and even is an other parting.<br>"
           "A candidate, the eighth figure of twelve, beside the three drawings it gathers and writing in none.</div>")
ARIA = ("Six parts and a table. A table of four rows by thirty columns with the numbers 1 to 120, a dark cell a plus and an open cell a minus. A board of four rows by five columns. "
        "A table of six seams with their two sides. Two lines. A row of fifteen cells. Five lines. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("Living Parities of the Numbers", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft66.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft66_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft66_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
