"""Draft 41 · 37, one self: its rounds and its other-thans, two partings of one shell (session v408illustrating).

For 3.2 of the draft of Exhibit THIRTY-TWO Natural Prime Numbering, v407primes', and its next draft's THREE, v406geodesic2's.
It goes on from the 40th drawing, whose third round closes at 37. A drawing with no moving part: a cube of 4 observed along
its corner's line, three sides; and the 37 cells of its shell at their 37 places three times, by their rounds, by their
other-thans of the inner cube, and turned by the six orders of the three ways. Under them, a round by its other-thans, and
five shells beside their inner cubes.
check_37_one_self_its_rounds_and_its_other-thans.py is its check. The numbers drawn here are executed here again, by that
check's own lines.

Its placings, no execution says them: the corner's line toward the eye; which way of the three is to the right; the cells as dots.

Usage: python3 -I make_draft41.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the look of the thirty-nine before, geom.py
from geom import *
spec = importlib.util.spec_from_file_location("the_37", os.path.join(HERE, "check_37_one_self_its_rounds_and_its_other-thans.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY = "#4a5160", "#9aa2b1", "#d9dde5"
SANS = "font-family: Inter, system-ui, sans-serif"
# the numbers drawn, executed here again
cells = m.o.the_cells(3)
ring = {c: m.o.ring(m.o.hexed(c)) for c in cells}
oth = {c: m.others(c) for c in cells}
orders = {c: len(m.the_orders(c)) for c in cells}
assert [sum(r == n for r in ring.values()) for n in range(4)] == [1, 6, 12, 18] and m.by_others(3) == [1, 9, 27]
assert sorted(orders.values()).count(3) == 18 and sorted(orders.values()).count(6) == 18
by_round = [[sum(ring[c] == r and oth[c] == n for c in cells) for n in (3, 2, 1)] for r in range(4)]
assert by_round == [[1, 0, 0], [0, 3, 3], [0, 3, 9], [0, 3, 15]]
shells = [(m.o.shell(k), m.by_others(k), k) for k in (1, 2, 3, 4, 5)]
assert [s[0] for s in shells] == [7, 19, 37, 61, 91] and [s[1] == [1, s[2] ** 2, s[2] ** 3] for s in shells] == [False, False, True, False, False]

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
R3 = math.sqrt(3) / 2
def flat(x, y, z, s):                                             # a place observed along the corner's line, the first way to the right
    q, r = x - y, y - z
    return s * (q + r / 2), s * R3 * r
s = []
FY = 440
# ---------- a cube of 4 observed along its corner's line: three sides, 16 squares a side ----------
CX0, S0 = 190, 26
for way, shade in ((0, "#eef1f6"), (1, "#dfe4ec"), (2, "#cfd6e1")):
    for i in range(4):
        for j in range(4):
            corners = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
            pts = []
            for u, v in corners:
                p = [4, 4, 4]; p[(way + 1) % 3] = u; p[(way + 2) % 3] = v
                x, y = flat(*[c - 4 for c in p], S0); pts.append(f"{CX0 + x:.1f},{FY + y:.1f}")
            s.append(f'<polygon points="{" ".join(pts)}" fill="{shade}" stroke="#ffffff" stroke-width="1.4"></polygon>')
for way in range(3):                                              # its three edges from the corner, a line a way
    p = [0, 0, 0]; p[way] = -4; x, y = flat(*p, S0)
    s.append(f'<line x1="{CX0}" y1="{FY}" x2="{CX0 + x:.1f}" y2="{FY + y:.1f}" stroke="{ACC}" stroke-width="2.2"></line>')
s.append(f'<circle cx="{CX0}" cy="{FY}" r="5" fill="{ACC}" stroke="#ffffff" stroke-width="1.4"></circle>')
# ---------- the 37 cells at their 37 places, three times ----------
SD, RD = 30, 9.6
def spot(cx, c):
    x, y = flat(*[v - 3 for v in c], SD); return cx + x, FY + y
CX1, CX2, CX3 = 560, 900, 1240
for c in cells:                                                   # by its rounds
    x, y = spot(CX1, c); open_ = ring[c] in (0, 2)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{RD}" fill="{"#ffffff" if open_ else INK}" stroke="{INK}" stroke-width="1.6"></circle>')
for way in range(3):                                              # by its other-thans: three lines, a line a way
    p = [3, 3, 3]; p[way] = 0; x, y = spot(CX2, tuple(p))
    s.append(f'<line x1="{CX2}" y1="{FY}" x2="{x:.1f}" y2="{y:.1f}" stroke="{ACC}" stroke-width="1.6" opacity="0.55"></line>')
for c in cells:
    x, y = spot(CX2, c)
    if oth[c] == 3:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{RD + 4.5}" fill="#ffffff" stroke="{ACC}" stroke-width="2"></circle><circle cx="{x:.1f}" cy="{y:.1f}" r="{RD - 1}" fill="{ACC}"></circle>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{RD}" fill="{ACC if oth[c] == 2 else INK}" stroke="#ffffff" stroke-width="1.4"></circle>')
ONE_THREE, ONE_SIX = m.the_orders((3, 3, 1)), m.the_orders((3, 0, 1))
for c in cells:                                                   # turned by the six orders of its three ways
    x, y = spot(CX3, c); n = orders[c]
    if n == 1: look = f'fill="#ffffff" stroke="{INK}" stroke-width="1.6"'
    elif n == 3: look = f'fill="{ACC if c in ONE_THREE else INK}" stroke="#ffffff" stroke-width="1.4"'
    else: look = f'fill="#ffffff" stroke="{ACC if c in ONE_SIX else FAINT}" stroke-width="{2.4 if c in ONE_SIX else 1.6}"'
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{RD}" {look}></circle>')
# ---------- a round by its other-thans ----------
AX, AY, AH = 60, 742, 30
def box(x, y, n, fill, edge, ink, w=44):
    return (f'<rect x="{x}" y="{y - 12}" width="{w}" height="24" rx="5" fill="{fill}" stroke="{edge}" stroke-width="1.5"></rect>' + text(x + w / 2, y + 4.5, str(n), 12.5, 600, ink))
for i, row in enumerate(by_round + [[1, 9, 27]]):
    y = AY + AH * i + (8 if i == 4 else 0)
    for j, n in enumerate(row):
        if n: s.append(box(AX + 150 + 70 * j, y, n, ACC if j < 2 else INK, ACC if j < 2 else INK, "#ffffff"))
    s.append(box(AX + 380, y, sum(row), "#ffffff", INK, INK))
s.append(f'<line x1="{AX}" y1="{AY + AH * 3 + 19}" x2="{AX + 424}" y2="{AY + AH * 3 + 19}" stroke="{RAY}" stroke-width="1.4"></line>')
# ---------- a shell beside its inner cube ----------
BX, BY = 800, 742
for i, (n, (_, twice, once), k) in enumerate(shells):
    y = BY + AH * i; hit = [1, twice, once] == [1, k * k, k ** 3]
    s.append(box(BX + 60, y, n, "#ffffff", ACC, ACC))
    s.append(box(BX + 190, y, once, INK if hit else "#ffffff", INK, "#ffffff" if hit else INK)); s.append(box(BX + 244, y, k ** 3, INK if hit else "#ffffff", INK if hit else FAINT, "#ffffff" if hit else GREY))
    s.append(box(BX + 350, y, twice, ACC if hit else "#ffffff", ACC, "#ffffff" if hit else ACC)); s.append(box(BX + 404, y, k * k, ACC if hit else "#ffffff", ACC if hit else FAINT, "#ffffff" if hit else GREY))
ARIA = ("A drawing with no moving part. A cube observed along the line of one corner, three sides of sixteen squares, with three accent lines from the corner. "
        "Beside it three figures of thirty-seven dots in rounds about one dot: one with its rounds dark and open by turns; one with a ringed centre dot, "
        "nine accent dots on three lines and twenty-seven dark dots; one with eighteen dark dots on six lines and eighteen open dots between them. "
        "Under them two tables of numbered boxes; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "for the draft of Exhibit THIRTY-TWO Natural Prime Numbering, its 3.2 · the one table's row 36 · executed from the numbers alone", "left", **small))
for i, t in enumerate(("37 is one self and three rounds of six.", "37 is a cube of 4 other-than its inner cube of 3.", "Its other-thans are its inner cube's own again: 27, 9 and 1.")):
    over.append(word(60, 104 + 36 * i, 760, t, "left", 600, 20, 30))
over.append(note(860, 104, "the draft's 3.2, v407primes', word for word:", 620))
over.append(note(860, 128, "<i>37 is the one shell whose other-thans are its inner cube's own again:</i>", 620))
over.append(note(860, 148, "<i>once the inner cube, 3 cubed; twice its square, 3 by 3; thrice the one self.</i>", 620))
for cx, top, a, b in ((CX0, "a cube of 4", "observed along its corner's line", "three sides, 16 squares a side: 48"),
                      (CX1, "by its rounds", "one self and rounds of six", "1, 6, 12 and 18"),
                      (CX2, "by its other-thans", "thrice the corner, twice an edge, once a side", "1, 9 and 27"),
                      (CX3, "turned by up, forward and right", "one still self, six threes and three sixes", "1, 18 and 18 · in the accent, one three and one six")):
    over.append(word(cx, 300, 330, top, "center", 600, 17, 24))
    over.append(word(cx, 572, 330, a, "center", 400, 13.5, 20, GREY)); over.append(word(cx, 593, 330, b, "center", 600, 13.5, 20, GREY))
over.append(head(AX, 668, "a round by its other-thans"))
for j, t in enumerate(("thrice", "twice", "once")): over.append(word(AX + 172 + 70 * j, 706, 70, t, "center", 400, 13.5, 20, GREY))
over.append(word(AX + 402, 706, 70, "cells", "center", 400, 13.5, 20, GREY))
for i, t in enumerate(("the corner's cell", "round one", "round two", "round three", "all 37")):
    over.append(word(AX, AY + AH * i + (8 if i == 4 else 0), 140, t, "left", 600 if i == 4 else 400, 13.5, 20, INK if i == 4 else GREY))
over.append(note(AX + 450, AY + AH * 1, "3 twice at all rounds,", 200)); over.append(note(AX + 450, AY + AH * 1 + 20, "one on a way's line:", 200)); over.append(note(AX + 450, AY + AH * 1 + 40, "turns of 120 degrees", 200))
over.append(head(BX, 668, "a shell beside its inner cube"))
over.append(word(BX + 190 + 49, 706, 130, "once · its cube", "center", 400, 13.5, 20, GREY)); over.append(word(BX + 350 + 49, 706, 150, "twice · its square", "center", 400, 13.5, 20, GREY))
for i, (n, (_, twice, once), k) in enumerate(shells):
    y = BY + AH * i; hit = [1, twice, once] == [1, k * k, k ** 3]
    over.append(word(BX, y, 60, "shell", "left", 400, 13.5, 20, GREY))
    over.append(word(BX + 470, y, 190, "is, its inner cube's own" if hit else "is-not", "left", 600, 14.5, 20, INK if hit else GREY))
over.append(item(60, 910, "● a cell is of the shell by a nand of three, v407nanding's · the 37 wrap with no seam, v407primes'", 700))
over.append(item(BX, 898, "● is: at 37 alone, of the shells stepped to 10,000 · three squares of n are n cubed at 3 alone", 680))
over.append(note(BX, 918, "○ is-not: the wrapping is of the shells 7, 19, 61 and 91 too · 37's parting is its other-thans", 680))
title = (f'<div style="position: absolute; left: 60px; top: 946px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">37, one self: its rounds and its other-thans, two partings of one shell</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 996px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'37 is one self and three rounds of six: 1, 6, 12 and 18. 37 is a cube of 4 other-than its inner cube of 3.<br>'
           f'Its cells are other-than the inner cube once, twice or thrice: 27 on its sides, 9 on its edges, 1 at its corner.<br>'
           f'27, 9 and 1 are the inner cube\'s own again: 3 cubed, 3 by 3, and one self. Of the shells stepped it is at 37 alone.<br>'
           f'A round is 3 twice, on the three ways\' lines, with 3, 9 and 15 once. A candidate, for the draft\'s 3.2.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("37, one self: its rounds and its other-thans, two partings of one shell", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft41.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft41_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft41_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; by its rounds:", [sum(r) for r in by_round], "by its other-thans:", m.by_others(3))
