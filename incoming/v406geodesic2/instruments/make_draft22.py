"""Draft 22 · six orientations: across a round of six, one quarter on all six at one (session v406geodesic2).

By a partner's saying of 23 November, with the 21st drawing before a partner, re-said: the going from one to an other of the six orientations is a
snap, with the angle of the horizon turning one quarter, and from one of the six all five others are next; it is of the six parity
balancing method of cones as universes, three universes with all moments. The saying goes on, and its end is not yet said.
A drawing with no moving part: the canvas's sphere observed across, the corner's line upright, the six orders as six parts of it
between the three folds' planes, a horizon going one quarter from across to along the line and on to all five others; the six
joined two ways; and the three lines' six ends.
check_six_orientations_a_snap_by_the_corners_line.py is its check, and the orders written here are executed here again.

Usage: python3 -I make_draft22.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
import numpy as np

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
ONE_LINE, OTHER_LINE = ["357", "573", "735"], ["753", "537", "375"]
ROUND = ["357", "537", "573", "753", "735", "375"]                               # across, a sixth of a turn a three: the 21st drawing's round
E = {"3": np.array([0.0, 0.0, 1.0]), "5": np.array([0.0, 1.0, 0.0]), "7": np.array([1.0, 0.0, 0.0])}
order = lambda h: "".join(k for _, k in sorted(((float(h @ E[k]), k) for k in "357"), reverse=True))
def middle(three):                                                               # an order's middle, across: its three numbers 1, 0 and -1
    m = E[three[0]] - E[three[2]]; return m / np.linalg.norm(m)
assert all(order(middle(t)) == t for t in ROUND)
ALONG = np.ones(3) / math.sqrt(3)                                                # the corner's line
CX, CY, R = 400.0, 440.0, 250.0
EL = math.radians(24.0)                                                          # observed across, a little from over it, the corner's line upright
d0 = middle("357"); d = math.cos(EL) * d0 + math.sin(EL) * ALONG; up = -math.sin(EL) * d0 + math.cos(EL) * ALONG; right = np.cross(up, d)
proj = lambda p: (CX + R * float(p @ right), CY - R * float(p @ up))
front = lambda p: float(p @ d) >= 0
def path(pts): return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in map(proj, pts))
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def head(p, q, tint, size=10.0):                                                 # a mark of the way, at q, from p
    (x0, y0), (x1, y1) = p, q; L = math.hypot(x1 - x0, y1 - y0) or 1.0; tx, ty = (x1 - x0) / L, (y1 - y0) / L; nx, ny = -ty, tx
    return (f'<path d="M{x1 + tx * size * 0.2:.1f},{y1 + ty * size * 0.2:.1f} L{x1 - tx * size + nx * size * 0.55:.1f},{y1 - ty * size + ny * size * 0.55:.1f} '
            f'L{x1 - tx * size - nx * size * 0.55:.1f},{y1 - ty * size - ny * size * 0.55:.1f} Z" fill="{tint}"></path>')
s = []
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#ffffff" stroke="{INK}" stroke-width="1.6" stroke-opacity="0.55"></circle>')
def circle_of(normal, tint, wide, faint=0.25):
    pts = great_circle(normal); fr, bk = runs(pts, [front(p) for p in pts])
    for piece in bk: s.append(f'<path d="{path(piece)}" fill="none" stroke="{tint}" stroke-opacity="{faint}" stroke-width="1.4" stroke-dasharray="4 5"></path>')
    for piece in fr: s.append(f'<path d="{path(piece)}" fill="none" stroke="{tint}" stroke-width="{wide}"></path>')
for a, b in (("3", "5"), ("5", "7"), ("3", "7")): circle_of(E[a] - E[b], INK, 1.8)   # a fold's plane: two of the three at one place across
circle_of(ALONG, ACC, 2.6, 0.4)                                                      # across: a horizon's three numbers adding to none
# a horizon from 357's middle, across, one quarter to along the corner's line, and on to the five others
m0 = middle("357")
quarter = [math.cos(t) * m0 + math.sin(t) * ALONG for t in np.radians(np.linspace(9, 84, 40))]
s.append(f'<path d="{path(quarter)}" fill="none" stroke="{ACC}" stroke-width="4.2" stroke-linecap="round"></path>' + head(proj(quarter[-3]), proj(quarter[-1]), ACC, 15))
for three in ROUND[1:]:
    m = middle(three); fan = [math.cos(t) * m + math.sin(t) * ALONG for t in np.radians(np.linspace(84, 11 if front(m) else 40, 30))]
    look = f'stroke="{INK}" stroke-width="2"' if front(m) else f'stroke="{INK}" stroke-width="1.6" stroke-opacity="0.45" stroke-dasharray="5 5"'
    s.append(f'<path d="{path(fan)}" fill="none" {look}></path>' + head(proj(fan[-3]), proj(fan[-1]), INK if front(m) else GREY, 11))
px, py = proj(ALONG)
s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="13" fill="#ffffff" stroke="{ACC}" stroke-width="3"></circle><circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{ACC}"></circle>')
# the three lines' six ends: one cone's three about the corner's line, and the other's three
for k in "357":
    for side, e in ((1, E[k]), (-1, -E[k])):
        x, y = proj(e); seen = front(e)
        if side == 1: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="{ACC}" fill-opacity="{1 if seen else 0.3}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, y + 6, k, 17, 700, "#ffffff"))
        else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="#ffffff" fill-opacity="{1 if seen else 0.5}" stroke="{INK}" stroke-opacity="{1 if seen else 0.35}" stroke-width="2.2"></circle>' + text(x, y + 6, k, 17, 700, INK, "middle", "" if seen else 'fill-opacity="0.4"'))
# the six orders, a part of the sphere an order: its name at its middle, across
for three in ROUND:
    m = middle(three); x, y = proj(m); tint = ACC if three in ONE_LINE else INK; seen = front(m)
    s.append(f'<rect x="{x - 33:.1f}" y="{y - 15:.1f}" width="66" height="30" rx="15" fill="{tint}" fill-opacity="{1 if seen else 0.32}"></rect>' + text(x, y + 6.5, three, 17, 700, "#ffffff"))
# the six joined two ways
HX, HY, HR = (960.0, 1300.0), 232.0, 86.0
spot = lambda cx, k: (cx + HR * math.sin(math.radians(60 * k)), HY - HR * math.cos(math.radians(60 * k)))
def exchanges(a, b):
    seen, n = list(a), 0
    for i in range(3):
        if seen[i] != b[i]:
            j = seen.index(b[i]); seen[i], seen[j] = seen[j], seen[i]; n += 1
    return n
for k in range(6):                                                               # across, going on: an order and the two beside it
    (x0, y0), (x1, y1) = spot(HX[0], k), spot(HX[0], (k + 1) % 6)
    s.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{INK}" stroke-width="2.2"></path>')
folds = turns = 0
for i in range(6):                                                               # by the corner's line: an order and all five others
    for j in range(i + 1, 6):
        (x0, y0), (x1, y1) = spot(HX[1], i), spot(HX[1], j); n = exchanges(ROUND[i], ROUND[j])
        folds += n == 1; turns += n == 2
        s.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{INK if n == 1 else ACC}" stroke-width="{1.6 if n == 1 else 2.6}" stroke-opacity="{0.7 if n == 1 else 1}"></path>')
assert (folds, turns) == (9, 6)
for cx in HX:
    for k, three in enumerate(ROUND):
        x, y = spot(cx, k); tint = ACC if three in ONE_LINE else INK
        s.append(f'<rect x="{x - 27:.1f}" y="{y - 13:.1f}" width="54" height="26" rx="13" fill="{tint}" stroke="#ffffff" stroke-width="2"></rect>' + text(x, y + 5.5, three, 14.5, 700, "#ffffff"))
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. A sphere observed across, a line through its middle upright. Three circles through the line's two ends part the sphere in six, and a part has an order of 3, 5 and 7 at its middle: "
        "357 toward the observing with 537 and 375 beside it, and 573, 753 and 735 behind. A coloured circle goes round the sphere's middle, across. A wide line goes from 357 one quarter up to a ringed mark at the upright line's end, "
        "and five lines go on from the mark to the five other orders. Six small marks, 3, 5 and 7 twice, are the three lines' ends. Beside it the six orders are at a hexagon's corners twice: "
        "joined round, an order with the two beside it; and joined all with all, fifteen lines.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's six orientations · a snap, the horizon's angle one quarter on · from one of the six, all five others next", "left", **small))
over.append(word(CX, 96, 720, "the canvas's sphere observed across, the corner's line upright", "center", 600, 15, 22, GREY))
over.append(word(CX, 118, 720, "three planes of the folds through the line part it in six: an order of the three a part", "center", 400, 14, 20, GREY))
over.append(word(px + 16, 166, 300, "along the corner's line: all six at one", "left", 600, 14.5, 20))
qx, qy = proj(math.cos(math.radians(26)) * m0 + math.sin(math.radians(26)) * ALONG)
over.append(word(qx - 14, qy, 110, "one quarter", "right", 600, 14.5, 20, "{{accent}}"))
over.append(word(CX, 742, 720, "a horizon is a line: the three are across in the order of its own three numbers along 3, 5 and 7", "center", 600, 15, 22))
over.append(word(CX, 765, 720, "across, round the sphere's middle, the 21st drawing's round of six: from an order, two are next", "center", 400, 14, 20, GREY))
over.append(word(CX, 785, 720, "one quarter on, along the corner's line, the three are at one place: a snap, and all five are next", "center", 400, 14, 20, GREY))
over.append(word(CX, 805, 720, "the marks 3, 5 and 7 are the three lines' ends, one cone's three coloured and the other's open", "center", 400, 14, 20, GREY))
over.append(word(60, 864, 720, "<i>Navigating is geodesic parity sharing over a horizon, a floating neutralling.</i>", "left", 400, 15, 22))
over.append(word(60, 885, 720, "Exhibit EIGHT Natural Exploring", "left", 400, 13.5, 20, GREY))
over.append(word(840, 84, 640, "the six, joined two ways", "left", 600, 18, 26))
over.append(word(HX[0], 362, 300, "across, going on", "center", 600, 15, 22)); over.append(word(HX[0], 383, 300, "from an order, two are next", "center", 400, 14, 20, GREY))
over.append(word(HX[1], 362, 300, "by the corner's line", "center", 600, 15, 22)); over.append(word(HX[1], 383, 320, "from an order, all five are next", "center", 400, 14, 20, GREY))
over.append(word(HX[1], 402, 340, "nine folds, 3 by 3, and six turns: fifteen", "center", 400, 14, 20, GREY))
P = [("a snap, one quarter from across", "a horizon turning from an order's middle to the corner's line has that one order all the way",
      "at the line it has none, and a hair on it is in one of the six: no other order is between"),
     ("2 of 3 at one place, and 3 of 3", "on a fold's plane two of the three are at one place across: one other order is next",
      "on the corner's line all three are: all five are · the draft's 3.4, 3 of 3"),
     ("three lines with all moments, six ends, two cones", "three lines at right angles, six ends: round the corner's line, in turn of one cone and of the other",
      "three on one cone about the line and three on its other, one vertex · the six added are none"),
     ("both ways: one quarter turn about a line of the three", "its two others are one for the other, one inverting: a fold on, and three of the five are next",
      "the two turns are two such turns on · the three lines' turnings onto the three are 24, four with an order"),
     ("a partner's saying goes on", "its end, of the method, is not yet said", "this drawing waits for it, as a candidate")]
for i, (a, b, c) in enumerate(P):
    y = 462 + 78 * i
    over.append(word(840, y - 22, 640, a, "left", 600, 17, 24))
    over.append(word(840, y + 2, 660, b, "left", 400, 14.5, 22))
    over.append(word(840, y + 23, 660, c, "left", 400, 13.5, 20, GREY))
over.append(word(840, 864, 660, "<i>3 of 3 is the corner's line, its six orders all ending at one</i>", "left", 400, 15, 22))
over.append(word(840, 885, 640, "Exhibit THIRTY-TWO Natural Prime Numbering's opening draft, its 3.4, in v407primes' folder", "left", 400, 13.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Six orientations: across a round of six, one quarter on all six at one</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A horizon is a line, and the three are across in the order of its own three numbers. Across, the six orders are a round, an order with two beside it.<br>'
           f'One quarter on, the horizon is along the corner\'s line and the three are at one place: a snap, and from one of the six all five others are next.<br>'
           f'Nine of the fifteen joinings are folds, 3 by 3, and six are turns. The three lines are three with all moments, six ends on two cones, and added are none.<br>'
           f'Both ways: by one quarter turn about a line of the three, three of the five are next. A partner\'s saying goes on, and this drawing waits for its end.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Six orientations: across a round of six, one quarter on all six at one", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft22.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft22_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft22_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
