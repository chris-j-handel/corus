"""Draft 17 · my now-existing universe, not moving, and ten passings through it (session v406geodesic2).

By a partner's saying of 23 November, re-said: my now-existing universe is the stable concept, and all the parities are flowing
through it; my prior-sequence alone is me in it; my prior-sequence and my now-existing me-parity are the other-than of an other-than
of my all, or my all; and all the podalings arriving and departing, ten in a row, are my next-existing universe.
A drawing with no moving part: the four stations of a universe, and the ten passings, a passing arriving at a station and departing
after a station, with the place it carries a me-now at 37 to. A me's own four, arriving at station 1, are coloured.
check_ten_rows_of_the_four_moments.py is its check.

Usage: python3 -I make_draft17.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
about = lambda st: (lambda n: 2 * st - n)
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
ME = 37
X = lambda n: 470 + 4.1 * n                               # one line of numbers, 0 to 240
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
def a_chip(x, y, number, tint, w=40, h=24):
    return (f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h}" rx="{h / 2}" fill="{tint}" stroke="{tint}" stroke-width="2"></rect>' + text(x, y + 4.8, number, 13.5, 700, "#ffffff"))
s = []
TOPY = 118.0
s.append(f'<path d="M{X(30) - 26:.1f},{TOPY - 34} L{X(120) + 26:.1f},{TOPY - 34} L{X(120) + 26:.1f},{TOPY + 34} L{X(30) - 26:.1f},{TOPY + 34} Z" fill="{ACC}" fill-opacity="0.08" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="6 5"></path>')
s.append(f'<path d="M{X(0):.1f},{TOPY} L{X(240):.1f},{TOPY}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 6"></path>')
passings = [(i, j) for k in range(4) for i in (1, 2, 3, 4) for j in (i + k,) if j <= 4]      # by their and-thens: none, one, two, three
R0, RD, GAP = 214.0, 40.0, 22.0
ys, y = [], R0
for n_, (i, j) in enumerate(passings):
    if n_ in (4, 7, 9): y += GAP
    ys.append(y); y += RD
for (i, j), y in zip(passings, ys):
    own = i == 1
    tint = ACC if own else INK
    stations = tuple(30 * k for k in range(i, j + 1)); to = by(ME, stations); me = (j - i) % 2 == 1
    s.append(f'<path d="M{X(0):.1f},{y} L{X(240):.1f},{y}" fill="none" stroke="{INK}" stroke-opacity="0.16" stroke-width="1"></path>')
    for st in (30, 60, 90, 120):
        if st not in stations: s.append(f'<circle cx="{X(st):.1f}" cy="{y}" r="3" fill="#ffffff" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.2"></circle>')
    s.append(f'<path d="M{X(stations[0]):.1f},{y} L{X(stations[-1]):.1f},{y}" fill="none" stroke="{tint}" stroke-width="4" stroke-linecap="round"></path>')
    for st in stations: s.append(f'<circle cx="{X(st):.1f}" cy="{y}" r="6.5" fill="{tint}" stroke="#ffffff" stroke-width="1.6"></circle>')
    s.append(a_chip(X(to), y, to, ACC if me else INK))
RUL = ys[-1] + 44
s.append(f'<path d="M60,{RUL} L{W - 60},{RUL}" fill="none" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. A line of numbers, 0 to 240, with nine marks, and the four marks 30, 60, 90 and 120 in a box. Under it ten rows: in a row, some of the four marks in a row "
        "are joined by a thick line, one mark, two, three or four of them, and a numbered mark is at a place of the line: 23, 83, 143, 203, 97, 97, 97, 83, 143 and 157.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

def chip(cx, cy, t, filled, w=38, h=30, size=15):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{t}</div>')
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1300, "my now-existing universe, four stations, not moving · ten passings through it, a me-now at 37 carried", "left", **small))
for j in range(9):
    over.append(chip(X(30 * j), TOPY, str(30 * j), j % 2 == 0, w=44, h=24, size=13))
over.append(word(X(75), TOPY - 52, 520, "my now-existing universe · the stable concept", "center", 600, 15, 22))
over.append(word(X(180), TOPY + 40, 420, "my next-existing universe", "center", 400, 14, 20, GREY))
over.append(word(60, 176, 380, "a passing · arriving at, departing after", "left", **small))
NAMES = {0: "an other", 1: "a self, 60 on", 2: "an other", 3: "a self, 120 on: my next universe"}
for (i, j), y in zip(passings, ys):
    own = i == 1
    over.append(word(60, y, 250, f"at {i}, after {j}" + (" · my prior-sequence" if own else ""), "left", 600 if own else 400, 15, 22))
    over.append(word(320, y, 140, NAMES[j - i].split(":")[0], "left", 400, 14, 20, GREY))
over.append(word(60, RUL + 24, 1400, "a passing of one station or of three is an other; of two or of all four, a self, its all again · the ten carry a me-now to six places, three in its universe and three in its next", "left", 400, 15.5, 24))
over.append(word(60, RUL + 50, 1400, "coloured: the four arriving at station 1, a me's own prior-sequence · 23, 97, 83 and 157", "left", 400, 15.5, 24, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">My now-existing universe, not moving, and ten passings through it</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'My now-existing universe is four stations, not moving, and the parities are flowing through it: a passing arrives at a station and departs after a station.<br>'
           f'The passings are ten: four of one station, three of two, two of three and one of all four. Four of them arrive at station 1, a me\'s own prior-sequence.<br>'
           f'With an even number of podalings a me is at its own place of the turn, the other-than of an other-than of its all, its all again.<br>'
           f'The passing of all four is 120 on, my next-existing universe: a me-now at 37 is carried to 157.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("My now-existing universe, not moving, and ten passings through it", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft17.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft17_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft17_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
