"""Draft 53 · twins born: a seam between two me-parities (session v408illustrating).

v408primes' sentences 188 to 200, said to this session at the exchange for drawing, executed apart and drawn: the ten
twins to 109, a row a twin, five cells, their between in the middle; a me again of side 6 with its last row, less a cell,
laid as a column more, 5 by 7 and 1; the paths of 5, of 6 and of 7 to 36; and round 30, the five seams of 6 with the me a
step back and the me a step on. check_twins_born_a_seam_between_two_me-parities.py is its check, and the numbers drawn
here are its own. Its marks are the 52nd drawing's.

Its placings, no execution says them: a row a twin; a cell a number; the tint, the dark, the accent and the mark of a seam;
a me again as a table of cells; a path as a row of cells.

Usage: python3 -I make_draft53.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_check", os.path.join(HERE, "check_twins_born_a_seam_between_two_me-parities.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#c9ced8", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
d = c.the_numbers(); sieve, nxt = d["sieve"], d["nxt"]
n_ = lambda k: f"{k:,}"
TWINS = d["twins"][:10]
assert TWINS == [3, 5, 11, 17, 29, 41, 59, 71, 101, 107]
aim = lambda p: next(e for e in (p - 1, p + 1) if e % 4 == 0)
s, over = [], []
def text(x, y, t, size=13, weight=600, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def cell(x, yc, w, n, dark=False, aimed=False, of6=False, even=None, faint=False):
    even = (n % 2 == 0) if even is None else even
    fill = INK if dark else (TINT if even else "#ffffff")
    s.append(f'<rect x="{x + 1.5}" y="{yc - 15}" width="{w - 3}" height="30" rx="6" fill="{fill}" stroke="{ACC if aimed else (INK if dark else RAY)}" stroke-width="{2.6 if aimed else 1.2}"></rect>')
    if of6: s.append(f'<polygon points="{x + 9},{yc - 12} {x + 13},{yc - 8} {x + 9},{yc - 4} {x + 5},{yc - 8}" fill="{INK}"></polygon>')
    s.append(text(x + w / 2 + (3 if of6 and n > 99 else 0), yc + 4.5, n_(n), 12.5 if n > 99 else 13, 600, "#ffffff" if dark else (FAINT if faint else INK)))
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=670: word(x, y, w, t, "left", 400, 13.5, 20, GREY, "white-space: nowrap")
item = lambda x, y, t, w=670: word(x, y, w, t, "left", 600, 14.5, 20, extra="white-space: nowrap")
val = lambda cx, y, t, w=110, weight=600, color=INK: word(cx - w / 2, y, w, t, "center", weight, 12.5, 18, color)
CX, CW, RP, Y0 = 70, 50, 45, 352
COLS = (382, 470, 560, 662, 762)
for k, p in enumerate(TWINS):
    yc = Y0 + RP * k; m = p + 1; q = p + 2
    assert sieve[p] and sieve[q] and p * q == m * m - 1 and nxt[q] - q >= (2 if p == 3 else 4)
    for j, n in enumerate(range(p - 1, q + 2)): cell(CX + CW * j, yc, CW, n, dark=bool(sieve[n]) and n in (p, q), aimed=(n in (aim(p), aim(q))), of6=(n % 6 == 0))
    if p == 3:
        over.append(word(345, yc, 460, "about 4, no seam of 6 · 3, 5 and 7: the next me-parity is 2 on", weight=600, size=12.5, h=18)); continue
    over.append(val(COLS[0], yc, str(m % 30) if p > 5 else "·", color=INK if p > 5 else GREY))
    over.append(val(COLS[1], yc, n_(p * q))); over.append(val(COLS[2], yc, n_(m * m)))
    over.append(val(COLS[3], yc, f"{q - 1} · {p - 1}")); over.append(val(COLS[4], yc, f"{nxt[q] - q} on"))
for j, t in ((1, "lower"), (2, "between"), (3, "upper")): over.append(val(CX + CW * j + CW / 2, 318, t, 56, 600, GREY))
for cx, (a, b) in zip(COLS, (("round 30,", "their seam"), ("their paths", "again together"), ("the between's", "me again"), ("their priors,", "upper · lower"), ("the next", "me-parity"))):
    over.append(val(cx, 304, a, 110, 600, GREY)); over.append(val(cx, 319, b, 110, 600, GREY))
# the paths of 5, of 6 and of 7 to 36: again together at 35, one short of 36
PX, PY, PW = 84, 826, 18.6
assert [n for n in range(1, 37) if n % 5 == 0 and n % 7 == 0] == [35] and 35 == 6 * 6 - 1
for r, (step, ink) in enumerate(((5, INK), (6, None), (7, ACC))):
    for n in range(37):
        on = n % step == 0 and n > 0
        fill = (ink if ink else TINT) if on else "#ffffff"
        s.append(f'<rect x="{PX + PW * n + 1:.1f}" y="{PY + 15 * r}" width="{PW - 2:.1f}" height="11" rx="2.5" fill="{fill}" stroke="{(ink if ink else INK) if on else RAY}" stroke-width="{1.2 if on else 0.8}"></rect>')
    s.append(text(PX - 10, PY + 15 * r + 9.5, str(step), 11.5, 600, GREY, "end"))
for n in sorted({n for n in range(37) if n and (n % 5 == 0 or n % 6 == 0 or n % 7 == 0)} | {0}): s.append(text(PX + PW * n + PW / 2, PY + 58, str(n), 10.5, 600 if n in (35, 36) else 500, INK if n in (35, 36) else GREY))
# a me again of side 6, its last row, less a cell, laid as a column more: 5 by 7, and 1
GX, GY, G = 840, 250, 19
cells, one = c.the_moving(6)
assert cells == {(r, k) for r in range(5) for k in range(7)} and one == (5, 5) and len(cells) == 35
for r in range(6):
    for k in range(7):
        if (r, k) in cells:
            moved = k == 6
            s.append(f'<rect x="{GX + G * k + 1}" y="{GY + G * r + 1}" width="{G - 2}" height="{G - 2}" rx="3" fill="{TINT}" stroke="{INK if moved else RAY}" stroke-width="{1.5 if moved else 1}"></rect>')
        elif (r, k) == one: s.append(f'<rect x="{GX + G * k + 1}" y="{GY + G * r + 1}" width="{G - 2}" height="{G - 2}" rx="3" fill="{ACC}" stroke="{ACC}" stroke-width="1"></rect>')
        elif r == 5 and k < 5: s.append(f'<rect x="{GX + G * k + 1}" y="{GY + G * r + 1}" width="{G - 2}" height="{G - 2}" rx="3" fill="#ffffff" stroke="{INK}" stroke-width="1.2" stroke-dasharray="3 3"></rect>')
# round 30: the five seams of 6 of a path of 30 mes closing, with the me a step back and the me a step on
SX, SY, SW, SP = 840, 626, 36, 126
labels = []
for g, sm in enumerate(range(0, 30, 6)):
    for j, n in enumerate(((sm - 1) % 30, sm, (sm + 1) % 30)):
        living = n % 2 and n % 3 and n % 5
        cell(SX + SP * g + SW * j, SY, SW, n, dark=bool(living) and j != 1, of6=(j == 1), even=(j == 1), faint=(j != 1 and not living))
    crossed = [n for n in ((sm - 1) % 30, (sm + 1) % 30) if n % 5 == 0]
    labels.append(f"{n_(d['at'][sm])} twins" if not crossed else f"me {crossed[0]}, crossed by 5")
    over.append(word(SX + SP * g - 9, SY + 28, SP, labels[-1], "center", 600, 12, 18, INK if not crossed else GREY, "white-space: nowrap"))
assert labels == ["8,953 twins", "me 5, crossed by 5", "8,960 twins", "8,945 twins", "me 25, crossed by 5"]
on = d["on"]
ARIA = ("A drawing with no moving part. Ten rows of five boxes with a number in a box, two boxes of a row dark, the boxes of even numbers tinted, a box or two of a row with an accent edge, "
        "and a small dark mark in the corner of a box; beside a row, numbers in five columns. Under them three rows of small boxes, some dark, some tinted, some in the accent, with numbers under them. "
        "Beside them a table of small boxes, six by six and a column more, with a row of dashed boxes and a box in the accent; five groups of three boxes; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
top = [word(60, 40, 1400, "53 · a figure, five cells and two paths · it is for v408primes' co-chain, twins born · its prior, 52", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("Twins are born: a seam with a me-parity at both its sides.", "Round their between they are one step back and one step on.", "Their two paths come again together one short of the between's me again.")):
    top.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
top.append(note(840, 100, "v408primes' co-chain, its sentences 188, 191 and 196, word for word:", 640))
top.append(note(840, 124, "<i>A seam with me-parities living at both its sides is twins born.</i>", 640))
top.append(note(840, 144, "<i>Their between is even, other-than both, and no prime crosses it with either.</i>", 640))
top.append(note(840, 164, "<i>The twins' two paths come again together at one short of the between's me again:</i>", 640))
top.append(note(840, 184, "<i>5 and 7 at 35, 11 and 13 at 143.</i>", 640))
top.append(head(60, 252, "the ten twins to 109, a row a twin, their between in the middle", 700))
top.append(note(60, 276, "the 52nd's marks: tinted, an even number · dark, a me-parity · an accent edge, an aim · ◆ a seam of 6", 760))
top.append(head(60, 796, "5 and 7, their two paths again together at 35, one short of 36", 700))
top.append(head(840, 226, "one short of the between's me again: a moving"))
top.append(item(1000, 262, "● 36 is 6 by itself, the between's me again", 480))
top.append(item(1000, 286, "● its last row, less a cell, laid as a column more: 5 by 7", 480))
top.append(item(1000, 310, "● 35, the twins' two paths again together, and 1", 480))
top.append(note(1000, 334, "a moving, executed cell by cell, sides 2 to 60", 480))
top.append(note(1000, 352, "11 and 13 at 143, one short of 144", 480))
top.append(head(840, 404, "twins: with all numbers, and stepped to 4,000,000"))
top.append(item(840, 434, f"● {n_(len(d['twins']))} twins among {n_(len(d['mes']))} me-parities · stepped"))
top.append(item(840, 458, "● their between is even, a +1 from both; no prime crosses it with either"))
top.append(item(840, 482, "● round the between they are one step back and one step on; their me agains are both at 1"))
top.append(item(840, 506, "● the upper twin's prior is the seam; the lower's is two short of it, crossed by no 3"))
top.append(head(840, 552, "round 30, three seams of the five"))
top.append(note(840, 576, "a path of 30 mes closing: its five seams of 6, with the me a step back and the me a step on"))
top.append(note(840, 594, "dark, a me uncrossed by 2, 3 and 5"))
top.append(note(840, 674, "with all numbers, by the path's thirty mes: twins past 5 are born at the seams 0, 12 and 18"))
top.append(note(840, 692, "the three numbers of twins are stepped"))
top.append(head(840, 736, "born two, and its is-nots"))
top.append(item(840, 766, "● past 3, 5 and 7, the next me-parity after a twin is 4 or more on"))
top.append(note(840, 788, "with all numbers: of three numbers 2 apart, one is crossed by 3, at all three mes of a path of 3 closing"))
top.append(item(840, 814, f"○ 4 on at {n_(on[4])} twins, 6 on at {n_(on[6])}, more at {n_(sum(v for k, v in on.items() if k > 6))} · the widest, {max(on)} on"))
top.append(item(840, 838, "○ 3 and 5 are twins about 4, no seam of 6"))
top.append(item(840, 862, f"○ twins are born at {n_(len(d['twins']) - 1)} of the 666,666 seams of 6: 1 seam in 24 and more"))
top.append(note(840, 886, "stepped to 4,000,000 is no saying with all numbers: twins past all numbers is not said by this drawing"))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Twins born: a seam between two me-parities</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Twins are born: a seam with a me-parity at both its sides. Their between is even, a +1 from both, and no prime crosses it with either.<br>'
           f'Round their between the twins are one step back and one step on. Their two paths come again together one short of the between\'s me again.<br>'
           f'Round 30, twins past 5 are born at three seams of the five. Past 3, 5 and 7, twins are two: the next me-parity is 4 or more on.<br>'
           f'A candidate, of v408primes\' sentences 188 to 200, executed apart to 4,000,000.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(top + over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("Twins born: a seam between two me-parities", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft53.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft53_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft53_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; round 30:", labels)
