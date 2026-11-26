"""Draft 55 · a path closing, all its mes gone through, says with all numbers (session v408illustrating).

A partner's sayings of 26 November, of simulation and of a logic that bounds itself, drawn for the 52nd, 53rd and 54th
drawings: six paths closing, of 2, 3, 4, 6, 12 and 30 mes, a path a row of its mes, all gone through; three movings, a
twin's rooms, a me again's cell over, and the pairing of a number's parts, an odd with an even across; and, apart, three
sentences not said by a path or a moving of this session's. check_a_path_closing_says_with_all_numbers.py is its check,
and the marks drawn here are its own.

Its placings, no execution says them: a path closing as a row of its mes; a card a path; the tint, the dark, the accent
and the mark of a seam.

Usage: python3 -I make_draft55.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_check", os.path.join(HERE, "check_a_path_closing_says_with_all_numbers.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#c9ced8", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
s, over = [], []
def text(x, y, t, size=12, weight=600, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def cell(x, yc, w, label, kind="open", edge=False, mark=False, h=26, size=12):
    """A me of a path, or a part of a number: dark, the me said; tint, an even or a seam; open, the others; faint, a me crossed."""
    fill = {"dark": INK, "tint": TINT, "open": "#ffffff", "faint": "#ffffff"}[kind]
    s.append(f'<rect x="{x + 1:.1f}" y="{yc - h / 2:.1f}" width="{w - 2:.1f}" height="{h}" rx="{min(5, w / 4):.1f}" fill="{fill}" stroke="{ACC if edge else (INK if kind == "dark" else RAY)}" stroke-width="{2.4 if edge else 1.1}"></rect>')
    if mark: s.append(f'<polygon points="{x + w / 2:.1f},{yc - h / 2 - 7:.1f} {x + w / 2 + 3.5:.1f},{yc - h / 2 - 3.5:.1f} {x + w / 2:.1f},{yc - h / 2:.1f} {x + w / 2 - 3.5:.1f},{yc - h / 2 - 3.5:.1f}" fill="{INK}"></polygon>')
    s.append(text(x + w / 2, yc + size * 0.36, label, size, 600, "#ffffff" if kind == "dark" else (FAINT if kind == "faint" else INK)))
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
PW, PH, PXS, PYS = 453, 190, (60, 533, 1006), (216, 416, 616)
def card(i, head, tag, lines, bold=None):
    px, py = PXS[i % 3], PYS[i // 3]
    s.append(f'<rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="10" fill="#ffffff" stroke="{RAY}" stroke-width="1.2"></rect>')
    over.append(word(px + 14, py + 20, PW - 28, head, weight=600, size=15.5, h=22))
    over.append(word(px + 14, py + 40, PW - 28, tag, weight=600, size=11.5, h=16, color=GREY))
    for k, t in enumerate(lines): over.append(word(px + 14, py + PH - 16 - 19 * (len(lines) - 1 - k), PW - 28, t, weight=400, size=12.5, h=18, color=INK if k == len(lines) - 1 and bold else GREY, extra="font-weight: 600" if k == len(lines) - 1 and bold else ""))
    return px, py
def row(px, yc, m, kinds, edges=(), marks=(), cw=None, size=12, labels=None):
    cw = cw or min(40, (PW - 28) / m)
    for a in range(m): cell(px + 14 + cw * a, yc, cw, str(a) if labels is None else labels[a], kinds.get(a, "open"), a in edges, a in marks, size=size)
# 1 · a path of 2 mes
px, py = card(0, "a path of 2 mes: even, odd, even", "a path closing, gone through whole · the 52nd's",
              ["past 2, a number at the me 0 is crossed by 2", "a me-parity past 2 is at the me 1: its prior and its next are at the me 0"], True)
row(px, py + 86, 2, {0: "tint", 1: "dark"})
# 2 · a path of 3 mes
px, py = card(1, "a path of 3 mes: twins are two", "a path closing, gone through whole · the 53rd's",
              ["three numbers 2 apart, from the me 0: 0, 2, 1 · from 1: 1, 0, 2 · from 2: 2, 1, 0", "one of the three is at the me 0, crossed by 3: past 3, 5 and 7, no three"], True)
assert [[(a + e) % 3 for e in (0, 2, 4)] for a in range(3)] == [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
row(px, py + 86, 3, {0: "tint"}, edges=(0,))
# 3 · a path of 4 mes
px, py = card(2, "a path of 4 mes: two me agains added", "a path closing, gone through whole · the 52nd's, laid stepped in it",
              ["at the me 3, two me agains added at none: a me-parity aiming next"], True)
again4 = sorted({(a * a) % 4 for a in range(4)}); two4 = sorted({(x + y) % 4 for x in again4 for y in again4}); assert again4 == [0, 1] and two4 == [0, 1, 2]
for k, (label, at) in enumerate((("a me again is at", again4), ("two added are at", two4))):
    over.append(word(px + 14, py + 76 + 34 * k, 130, label, weight=600, size=12, h=18, color=GREY))
    for a in range(4): cell(px + 150 + 40 * a, py + 76 + 34 * k, 40, str(a), "dark" if a in at else "open", edge=(a == 3))
# 4 · a path of 6 mes
px, py = card(3, "a path of 6 mes: living in a seam", "a path closing, gone through whole · the 52nd's",
              ["uncrossed by 2 and by 3: the me one on and the me one back alone", "past 3, a me-parity is a +1 from the me 0, a seam of 6"], True)
assert c.living(6) == [1, 5]
row(px, py + 90, 6, {0: "tint", 1: "dark", 5: "dark", 2: "faint", 3: "faint", 4: "faint"}, marks=(0,))
# 5 · a path of 12 mes
px, py = card(4, "a path of 12 mes: an aim and a seam", "a path closing, gone through whole · the 52nd's, found by drawing it",
              ["at the mes 1 and 11, aim and seam are one even · at 5 and 7, its two evens", "twins aim together about the me 0, and apart about the me 6"], True)
assert c.living(12) == [1, 5, 7, 11] and [a for a in c.living(12) if c.aim(a, 12) == c.seam(a, 12)] == [1, 11]
row(px, py + 90, 12, {**{a: "tint" for a in range(0, 12, 2)}, **{a: "dark" for a in c.living(12)}, 3: "faint", 9: "faint"}, edges=(0, 4, 8), marks=(0, 6), cw=35)
# 6 · a path of 30 mes
px, py = card(5, "a path of 30 mes: three seams of the five", "a path closing, gone through whole · the 53rd's",
              ["a seam of 6 with both its sides uncrossed by 5: the mes 0, 12 and 18", "twins past 5 are born at these three seams"], True)
seams30 = [sm for sm in range(0, 30, 6) if (sm - 1) % 30 in c.living(30) and (sm + 1) % 30 in c.living(30)]; assert seams30 == [0, 12, 18]
row(px, py + 90, 30, {**{a: "faint" for a in range(30)}, **{a: "tint" for a in range(0, 30, 6)}, **{a: "dark" for a in c.living(30)}}, edges=seams30, marks=tuple(range(0, 30, 6)), cw=14.1, size=8.5)
# 7 · a moving: a twin's rooms, drawn at 7
px, py = card(6, "a path of r mes: a twin's rooms", "a moving, one rule at all r past 2 · drawn at 7 · the 54th's",
              ["a twin's between is uncrossed by r at all mes but one on and one back", "the two are 2 steps apart, one me at a path of 2 alone: r − 2 rooms of r"], True)
rooms7 = [m for m in range(7) if (m - 1) % 7 and (m + 1) % 7]; assert rooms7 == [0, 2, 3, 4, 5]
row(px, py + 86, 7, {**{a: "tint" for a in rooms7}, 1: "faint", 6: "faint"}, edges=(1, 6))
# 8 · a moving: a me again, its cell over, drawn at 6
px, py = card(7, "a me again: one cell over", "a moving, one rule at all sides · drawn at 6 · the 53rd's",
              ["a row of n cells is n − 1 cells and 1 cell", "the row, less a cell, is a column more: 5 by 7", "two paths again together, one short of a me again"], True)
cells, one = c.the_moving(6); G = 12; gx, gy = px + 330, py + 52
for r in range(6):
    for k in range(7):
        if (r, k) in cells: s.append(f'<rect x="{gx + G * k + 1}" y="{gy + G * r + 1}" width="{G - 2}" height="{G - 2}" rx="2" fill="{TINT}" stroke="{INK if k == 6 else RAY}" stroke-width="{1.3 if k == 6 else 0.9}"></rect>')
        elif (r, k) == one: s.append(f'<rect x="{gx + G * k + 1}" y="{gy + G * r + 1}" width="{G - 2}" height="{G - 2}" rx="2" fill="{ACC}" stroke="{ACC}" stroke-width="1"></rect>')
        elif r == 5: s.append(f'<rect x="{gx + G * k + 1}" y="{gy + G * r + 1}" width="{G - 2}" height="{G - 2}" rx="2" fill="#ffffff" stroke="{INK}" stroke-width="1" stroke-dasharray="2 2"></rect>')
# 9 · a moving: the pairing of a number's parts, drawn at 35 and 36
px, py = card(8, "the pairing: exhausted into all-parity", "a moving, one rule at all numbers · drawn at 35 and 36 · v408primes' 80",
              ["a number's parts in pairs, an odd with an even across: none over", "a me again's parts: pairs, and one over, a me"], True)
for k, n in enumerate((35, 36)):
    pairs, left = c.the_pairing(n); yc = py + 70 + 40 * k; x = px + 62; cw = 33
    over.append(word(px + 14, yc, 44, str(n), weight=600, size=13, h=18))
    for a, b in sorted(pairs):
        assert c.across(a) != c.across(b)
        for j, d in enumerate((a, b)): cell(x + cw * j, yc, cw, str(d), "dark" if c.across(d) else "tint", h=24, size=11.5)
        s.append(f'<path d="M {x + 4} {yc + 15} v 4 h {2 * cw - 8} v -4" fill="none" stroke="{INK}" stroke-width="1.2"></path>'); x += 2 * cw + 8
    for d in left: cell(x, yc, cw, str(d), "tint", edge=True, h=24, size=11.5)
    assert left == ([36] if n == 36 else [])
over.append(word(px + 222, py + 70, 140, "none over", weight=600, size=12, h=18, color=GREY)); over.append(word(px + 398, py + 110, 44, "a me", weight=600, size=12, h=18, color=GREY))
ARIA = ("A drawing with no moving part. Nine cards in three rows of three. In a card, a row of small boxes with numbers, some dark, some tinted, some with an accent edge, and lines of words under it; "
        "a card is with a small table of boxes with a column more and a box in the accent; a card is with two rows of boxes joined two and two under them, and a last box alone. Under the cards, three lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
top = [word(60, 40, 1400, "55 · a figure, six paths and three movings · it is for a partner's sayings of 26 November, of simulation and of logic · its prior, 52, 53 and 54", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A path closing, all its mes gone through, says with all numbers.", "A moving says it at all sides: all in pairs, or pairs and one over.", "A simulation is a breaking test: it says no is beyond its limit.")):
    top.append(word(60, 96 + 34 * i, 800, t, weight=600, size=20, h=30))
for i, t in enumerate(("a partner's sayings of 26 November, in this session's words:", "a simulation ends at a number, and in a universal set it proves no is;", "it is for rapid breaking testing, not conclusive beyond its stated limits;",
                       "the all-or-none logic ends at its own bound")):
    top.append(word(900, 92 + 20 * i, 580, t, weight=400, size=13.5, h=20, color=GREY))
top.append(word(60, 198, 1400, "dark, the me said · tinted, an even, a seam or a room · an accent edge, the me a sentence is of · ◆ a seam of 6 · faint, a me crossed · in the pairing: dark, odd across; tinted, even across", weight=400, size=12.5, h=18, color=GREY))
top.append(word(60, 834, 1400, "not said by a path or a moving of this session's · a breaking test found none, to its limit: no is", weight=600, size=17, h=24))
for x, a, b in ((60, "○ aiming prior, a me-parity is two me agains added", "tested to 4,000,000, the 52nd's check"), (533, "○ twins are more at a next span by 4", "tested at nine spans, to 4,194,304, the 54th's check"),
                (1006, "○ twins are born past all numbers", "tested to 4,194,304, the 54th's check")):
    top.append(word(x, 864, PW, a, weight=600, size=14.5, h=20)); top.append(word(x + 18, 886, PW - 18, b, weight=400, size=13, h=18, color=GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A path closing, all its mes gone through, says with all numbers</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A sentence with all numbers is said by a path closing with all its mes gone through, or by a moving, one rule at all sides.<br>'
           f'A moving ends all in pairs, or in pairs and one over: odd and even bound it. A me again is pairs and one over, a me.<br>'
           f'A simulation is a breaking test: an is-not it finds is whole, and none found is no is beyond its limit.<br>'
           f'A candidate, of a partner\'s sayings of 26 November, for the 52nd, 53rd and 54th drawings.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(top + over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("A path closing, all its mes gone through, says with all numbers", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft55.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft55_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft55_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
