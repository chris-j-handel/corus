"""Draft 24 · a me's moment as three fours and a one on the diamond: a partner's words, gone through with rigor (session v406geodesic2).

By a partner's saying of 24 November, with the 23rd drawing before a partner, re-said: in place of observes and gives, 1, 2, 4, 5
co-observing; 3, 5, 7, 5 co-possibling; 5, 8, 6, 9 co-discovering; and 9 bi-neutralling; to be gone through with rigor, possibly
off, beside, or of no value.
A drawing with no moving part: the front me's diamond of nine with its living names, a partner's three fours laid on it, a mark
coloured by the living code's own parting, a me's own moment or its going on; a me's three steps in a row; and the four ways.
check_a_mes_moment_in_three_fours_on_the_diamond.py is its check. The names and the code's parting are opened here again, from
Exhibit ONE Natural Resolver and the seventeen names' one table.

Usage: python3 -I make_draft24.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import ast, csv, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
ROOT = Path(HERE, "..", "..", "..")
code = re.search(r"```python\n(.*?)```", Path(ROOT, "Exhibit_ONE_Natural_Resolver_v402mgr.md").read_text(encoding="utf-8"), flags=re.S).group(1)
number = lambda name: int(re.match(r"_(\d+)_", name).group(1)) if re.match(r"_(\d+)_", name) else None
a_moment = next(f for f in ast.parse(code).body if isinstance(f, ast.FunctionDef) and number(f.name) == 1)
OWN = {1} | {number(n.id) for n in ast.walk(a_moment) if isinstance(n, ast.Name) and number(n.id)} | {number(a.arg) for a in ast.walk(a_moment) if isinstance(a, ast.arg)}
rows = list(csv.reader(Path(ROOT, "incoming", "v403mgr", "The_seventeen_names_in_one_table.csv").open(encoding="utf-8")))
NAME = {int(r[0]): r[1].split("-", 1)[1] for r in rows[1:]}                       # a name less its number: now-existing, now-possibling, and on
assert OWN & set(range(1, 10)) == {1, 2, 3, 4, 7} and NAME[9] == "next-co-discovering"

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
X0, X1, LY, AC = 150.0, 730.0, 326.0, 122.0
at_x = lambda n: X0 + (X1 - X0) * n / 60.0
SEAT = {1: (0, 0), 4: (15, -0.5), 2: (15, 0.5), 7: (30, -1), 5: (30, 0), 3: (30, 1), 8: (45, -0.5), 6: (45, 0.5), 9: (60, 0)}   # a number: its place along, and across
P = {n: (at_x(a), LY + AC * c) for n, (a, c) in SEAT.items()}
def about(numbers, tint, strength):                                              # a four's ground, wide about its marks
    pts = " ".join(f"{P[n][0]:.1f},{P[n][1]:.1f}" for n in numbers)
    return f'<g opacity="{strength}"><polygon points="{pts}" fill="{tint}" stroke="{tint}" stroke-width="84" stroke-linejoin="round"></polygon></g>'
s = []
s.append(f'<path d="M{X0 - 70},{LY} L{X1 + 70},{LY}" fill="none" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.4" stroke-dasharray="2 6"></path>')
for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)):
    for p, q in ((a, b), (b, c)):
        s.append(f'<path d="M{P[p][0]:.1f},{P[p][1]:.1f} L{P[q][0]:.1f},{P[q][1]:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.16" stroke-width="1.5"></path>')
s.append(about((1, 4, 5, 2), ACC, 0.13))
s.append(about((5, 8, 9, 6), INK, 0.10))
mx = P[5][0]
s.append(f'<rect x="{mx - 44:.1f}" y="{P[7][1] - 46:.1f}" width="88" height="{P[3][1] - P[7][1] + 92:.1f}" rx="44" fill="none" stroke="{GREY}" stroke-width="2.2" stroke-dasharray="7 6"></rect>')
for n, (x, y) in P.items():
    own = n in OWN
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="27" fill="{ACC if own else INK}" stroke="#ffffff" stroke-width="3"></circle>' + text(x, y + 9, n, 25, 700, "#ffffff"))
s.append(f'<circle cx="{P[9][0]:.1f}" cy="{P[9][1]:.1f}" r="35" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="3 4"></circle>')
# a me's three steps in a row
BY, BH = 668.0, 86.0
boxes = [(60, 226, ACC), (310, 226, ACC), (560, 226, INK)]
for x, w, tint in boxes:
    s.append(f'<rect x="{x}" y="{BY}" width="{w}" height="{BH}" rx="10" fill="{tint}" fill-opacity="0.08" stroke="{tint}" stroke-width="1.8"></rect>')
for x in (286, 536):
    s.append(f'<path d="M{x + 2},{BY + BH / 2} L{x + 16},{BY + BH / 2}" fill="none" stroke="{INK}" stroke-width="2"></path><path d="M{x + 24},{BY + BH / 2} L{x + 13},{BY + BH / 2 - 6} L{x + 13},{BY + BH / 2 + 6} Z" fill="{INK}"></path>')
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. One diamond of nine numbered marks along a line, 1 at its opening and 9 at its far end, with a name beside a mark: now-existing, now-possibling, now-co-observing, "
        "now-co-same-existing, now-co-existing, now-co-possibling, now-observing, now-same-existing and next-co-discovering. The marks 1, 2, 3, 4 and 7 are coloured and 5, 6, 8 and 9 are dark. "
        "Three outlines are laid on it: a square about 1, 2, 4 and 5; a dashed band about 7, 5 and 3; and a square about 5, 8, 6 and 9, with 9 ringed. Under it three boxes in a row are a me's three steps. "
        "Beside it are the four ways the three fours are gone through, with what is and what is not.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's three fours and a one, in place of observes and gives · gone through four ways, all or none", "left", **small))
over.append(word(60, 84, 730, "the front me's diamond, a mark with its living name", "left", 600, 17, 24))
over.append(word(60, 108, 730, "coloured: in the lines of a me's own moment, the code's 1 · dark: in its going on alone, the code's 9 and 17", "left", 400, 14, 20, GREY))
for n, dx, dy, align in ((1, 0, 50, "center"), (4, 0, -44, "center"), (2, 0, 46, "center"), (7, 60, -34, "left"), (5, 50, 22, "left"), (3, 60, 34, "left"), (8, 0, -44, "center"), (6, 0, 46, "center"), (9, -28, 58, "center")):
    over.append(word(P[n][0] + dx, P[n][1] + dy, 190, NAME[n], align, 600, 13.5, 18, "{{accent}}" if n in OWN else INK))
over.append(word(at_x(7), 168, 250, "1 2 – 4 5", "center", 600, 17, 22, "{{accent}}")); over.append(word(at_x(7), 189, 250, "a partner's: co-observing", "center", 400, 14, 20, GREY))
over.append(word(at_x(53), 168, 250, "5 8 6 9", "center", 600, 17, 22)); over.append(word(at_x(53), 189, 250, "a partner's: co-discovering", "center", 400, 14, 20, GREY))
over.append(word(mx, 536, 300, "3-5-7-5 · a partner's: co-possibling", "center", 600, 15, 22))
over.append(word(at_x(7), 500, 250, "its own name: 2, possibling", "center", 400, 14, 20, GREY))
over.append(word(at_x(53), 500, 250, "its own: 6 and 9, co-possibling,", "center", 400, 14, 20, GREY)); over.append(word(at_x(53), 519, 250, "co-discovering", "center", 400, 14, 20, GREY))
over.append(word(mx, 558, 400, "its own names: 3 and 7, co-observing and observing", "center", 400, 14, 20, GREY))
over.append(word(60, 632, 730, "a me's moment, three steps in a row, by the code's own numbers", "left", 600, 17, 24))
steps = [(60, "what it observes, to its surfacing", "2, with 4 and 7, to 14", "a partner's: co-observing"), (310, "its surfacing with its prior", "3, to 12: same-existing or not", "a partner's: co-possibling"),
         (560, "its giving and its next prior", "10 and 11, on by 9, with 5, 6 and 8", "a partner's: co-discovering")]
for x, a, b, c in steps:
    over.append(word(x + 113, BY + 20, 222, a, "center", 600, 13.5, 20)); over.append(word(x + 113, BY + 43, 222, b, "center", 400, 13.5, 20)); over.append(word(x + 113, BY + 66, 222, c, "center", 400, 13.5, 20, GREY))
over.append(word(60, 786, 730, "what a me observes enters by its surfacing alone, one of three · a 0 surfaces two ways, none and a + with a −", "left", 400, 14, 20, GREY))
over.append(word(60, 862, 730, "Exhibit ONE Natural Resolver, of co: <i>two both facing forward along, a self and its other</i>", "left", 400, 14.5, 22))
over.append(word(60, 884, 740, "Exhibit FIVE Natural Engineering: <i>Floating-neutralling is bounding-zeroing, each self's own with its coupling.</i>", "left", 400, 13.5, 22))
WAYS = [("by the living code's own lines: is, but for the 5", "the names in no line of a me's own moment are 5, 6, 8 and 9: the back four, all and no other",
         "the front and the middle, less their 5s, are a me's own moment", "2 and 4 of its opening loop, 3 and 7 of its next · 5, the bi-couplings, is in the going on alone"),
        ("by the names' own roots: one word of three", "co-observing is 3, co-possibling 6 and co-discovering 9: one arc, a step of 3",
         "co-discovering is at its own name, 9 in its four", "co-observing's 3 is in the middle four, and co-possibling's 6 in the back"),
        ("by the diamond's own form: is", "two squares, the back the front 4 on, and the widest row between them",
         "steps of 1, of 2 and of 3 · added 12, 20 and 28, 8 on and 8 on, 60 together", ""),
        ("by the cell by nand: three steps in a row, is", "all observings with one surfacing have one giving and one next prior",
         "the three steps' names are a partner's, or the code's: both are laid under the diamond", ""),
        ("the 9, bi-neutralling", "by the code the 9 has no is-or-is-not: a giving carried to the me a coupling names, between two",
         "the word is in no living file; floating neutralling is, and a 0 is more than one thing in a me's moment", "")]
y = 100.0
for a, b, c, d in WAYS:
    over.append(word(840, y, 640, a, "left", 600, 17, 24)); y += 25
    for t in (b, c, d):
        if t: over.append(word(840, y, 650, t, "left", 400, 14, 20, GREY if t is not b else INK)); y += 21
    y += 30
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A me\'s moment as three fours and a one: a partner\'s words, with rigor</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'The three fours are the living code\'s own parting of the nine names: 5, 6, 8 and 9 are in no line of a me\'s own moment, and 1, 2, 3, 4 and 7 are its lines.<br>'
           f'One number is beside: 5, the bi-couplings, is in the going on alone, and a partner has it in all three fours.<br>'
           f'Of the three words, co-discovering is at its own name, 9. By their roots the fours are possibling, co-observing, and co-possibling with co-discovering.<br>'
           f'The 9 has no is-or-is-not in its lines, a giving carried between two. Bi-neutralling is in no living file, and is laid here as a partner\'s word.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A me's moment as three fours and a one: a partner's words, with rigor", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft24.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft24_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft24_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
