"""Draft 21 · six orders of 3, 5 and 7, right spiraling: a living gyroscope (session v406geodesic2).

By two sayings of a partner, 23 November, with the twentieth drawing before a partner, re-said: the order in three parts, 0124, a
three and 689, its three as 357, 573 and 735 and as 753, 537 and 375, and it is right spiraling; and the twentieth drawing is a
living gyroscope for aiming over the horizon.
A drawing with no moving part: the canvas's own sphere observed along the line (1, 1, 1), its three circles at right angles and the
three-right-angle triangle with 3, 5 and 7 at its corners; six observings about it, a sixth of a turn apart; a partner's two lines
of three as three turns and three folds; and the twentieth drawing's lines as a gyroscope.
check_six_orders_of_3_5_7_a_living_gyroscope.py is its check, and the orders written here are executed here again.

Usage: python3 -I make_draft21.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
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
ONE_LINE, OTHER_LINE = ["357", "573", "735"], ["753", "537", "375"]
CX, CY, R = 400.0, 452.0, 212.0
cam = Cam(45.0, math.degrees(math.asin(1 / math.sqrt(3))), CX, CY, R)            # observed along the line (1, 1, 1)
E = {"3": (0.0, 0.0, 1.0), "5": (0.0, 1.0, 0.0), "7": (1.0, 0.0, 0.0)}           # 3, 5 and 7 at the three corners, a placing
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
s = []
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#ffffff" stroke="{INK}" stroke-width="1.6" stroke-opacity="0.55"></circle>')
for normal in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):                                 # the three circles at right angles
    pts = great_circle(normal)
    front, back = runs(pts, [cam.depth(p) >= 0 for p in pts])
    for piece in back: s.append(f'<path d="{cam.path(piece)}" fill="none" stroke="{INK}" stroke-opacity="0.22" stroke-width="1.4" stroke-dasharray="4 5"></path>')
    for piece in front: s.append(f'<path d="{cam.path(piece)}" fill="none" stroke="{INK}" stroke-opacity="0.7" stroke-width="2"></path>')
tri = list(slerp(E["3"], E["5"])) + list(slerp(E["5"], E["7"])) + list(slerp(E["7"], E["3"]))
s.append(f'<path d="{cam.path(tri, close=True)}" fill="{ACC}" fill-opacity="0.10" stroke="{ACC}" stroke-width="3"></path>')
for k in "357":                                                                  # a fold's line: a corner, the middle, and the side across
    x, y = cam.proj(E[k]); ox, oy = CX - (x - CX) * 0.74, CY - (y - CY) * 0.74
    s.append(f'<path d="M{x:.1f},{y:.1f} L{ox:.1f},{oy:.1f}" fill="none" stroke="{GREY}" stroke-width="1.6" stroke-dasharray="3 5"></path>')
A0 = 46.0                                                                        # the round about the middle, a third of a turn
def on_round(deg, rad): return CX + rad * math.sin(math.radians(deg)), CY - rad * math.cos(math.radians(deg))
for a0 in (108, 228, 348):                                                       # the three's own way round, 3 to 7's place, 7 to 5's and 5 to 3's
    x0, y0 = on_round(a0, A0); x1, y1 = on_round(a0 - 92, A0)
    s.append(f'<path d="M{x0:.1f},{y0:.1f} A{A0},{A0} 0 0 0 {x1:.1f},{y1:.1f}" fill="none" stroke="{ACC}" stroke-width="2.6"></path>')
    t = math.radians(a0 - 92); tx, ty = -math.cos(t), -math.sin(t); nx, ny = -ty, tx
    s.append(f'<path d="M{x1 + tx * 11:.1f},{y1 + ty * 11:.1f} L{x1 + nx * 7:.1f},{y1 + ny * 7:.1f} L{x1 - nx * 7:.1f},{y1 - ny * 7:.1f} Z" fill="{ACC}"></path>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="7" fill="{INK}"></circle>')
at = {}
for k in "357":
    x, y = cam.proj(E[k]); at[k] = (x, y)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="30" fill="{ACC}" stroke="#ffffff" stroke-width="3"></circle>' + text(x, y + 9, k, 26, 700, "#ffffff"))
# six observings about it, across, a sixth of a turn apart: a three as that observing has it, executed here
def observed(deg):                                                               # the observing at deg round from the top, its eye to the middle
    px, py = math.sin(math.radians(deg)), math.cos(math.radians(deg))            # the observing's place, with up as up
    rx, ry = -py, px                                                             # its own right hand, its eye to the middle
    return "".join(k for _, k in sorted(((at[k][0] - CX) * rx - (at[k][1] - CY) * ry, k) for k in "357"))
ROUND = [observed(d) for d in (180, 240, 300, 0, 60, 120)]
assert sorted(ROUND) == sorted(ONE_LINE + OTHER_LINE) and all((ROUND[k] in ONE_LINE) != (ROUND[(k + 1) % 6] in ONE_LINE) for k in range(6)), ROUND
assert all(ROUND[(k + 3) % 6] == ROUND[k][::-1] for k in range(6)), ROUND
RC = R + 62
for k, deg in enumerate((180, 240, 300, 0, 60, 120)):
    x, y = on_round(deg, RC); three = ROUND[k]; tint = ACC if three in ONE_LINE else INK
    ex, ey = on_round(deg, RC - 34)
    s.append(f'<path d="M{x:.1f},{y:.1f} L{ex:.1f},{ey:.1f}" fill="none" stroke="{tint}" stroke-width="1.6"></path>')
    s.append(f'<rect x="{x - 36:.1f}" y="{y - 17:.1f}" width="72" height="34" rx="17" fill="{tint}"></rect>' + text(x, y + 7, three, 19, 700, "#ffffff"))
# a partner's two lines of three: a small triangle with its three at the top, the lower right and across from it
TX, TY1, TY2, TS = (912, 1100, 1288), 190.0, 356.0, 44.0
corner = lambda cx, cy, k: (cx + TS * math.sin(math.radians(120 * k)), cy - TS * math.cos(math.radians(120 * k)))
for row, (cy, threes) in enumerate(((TY1, ONE_LINE), (TY2, OTHER_LINE))):
    for i, three in enumerate(threes):
        cx = TX[i]; P = [corner(cx, cy, k) for k in range(3)]
        s.append(f'<path d="M{P[0][0]:.1f},{P[0][1]:.1f} L{P[1][0]:.1f},{P[1][1]:.1f} L{P[2][0]:.1f},{P[2][1]:.1f} Z" fill="{ACC}" fill-opacity="{0.10 if row == 0 else 0.0}" stroke="{ACC if row == 0 else INK}" stroke-width="2.2"></path>')
        if row == 1:                                                             # the fold: the line through the 5, at its place from the three over it
            px, py = P[three.index("5")]
            s.append(f'<path d="M{cx + (px - cx) * 1.42:.1f},{cy + (py - cy) * 1.42:.1f} L{cx - (px - cx) * 0.95:.1f},{cy - (py - cy) * 0.95:.1f}" fill="none" stroke="{GREY}" stroke-width="1.6" stroke-dasharray="3 5"></path>')
        for k, c in enumerate(three):
            s.append(f'<circle cx="{P[k][0]:.1f}" cy="{P[k][1]:.1f}" r="15" fill="{ACC if row == 0 else INK}" stroke="#ffffff" stroke-width="2"></circle>' + text(P[k][0], P[k][1] + 6, c, 16, 700, "#ffffff"))
        if i:
            ax = cx - 94
            s.append(f'<path d="M{ax + 8},{cy} L{ax - 6},{cy - 7} L{ax - 6},{cy + 7} Z" fill="{ACC if row == 0 else INK}"></path>')
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. A sphere observed along a line through its middle, with three circles at right angles and a triangle of three right angles toward the observing, "
        "its corners marked 3 at the top, 5 at the lower right and 7 across from it. A round about the triangle's middle is marked a third of a turn, and three dashed lines go from a corner through the middle. "
        f"Six marks about the sphere, a sixth of a turn apart, say the three as an observing across has it: {ROUND[0]} at the foot, then {ROUND[1]}, {ROUND[2]}, {ROUND[3]}, {ROUND[4]} and {ROUND[5]} going round. "
        "Beside it are two rows of three small triangles, 357, 573 and 735 over 753, 537 and 375, a dashed line through the 5 of the lower three.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's three in six orders, right spiraling · the twentieth drawing a living gyroscope for aiming over the horizon", "left", **small))
over.append(word(CX, 96, 720, "the canvas's sphere observed along the line (1, 1, 1)", "center", 600, 15, 22, GREY))
over.append(word(CX, 118, 720, "three circles at right angles, a triangle of three right angles, 3, 5 and 7 at its corners", "center", 400, 14, 20, GREY))
over.append(word(CX, 776, 720, "the three go round one way, a third of a turn, or an observing goes round them the other way", "center", 600, 15, 22))
over.append(word(CX, 799, 720, "about the sphere, a three as an observing across has it: one round of six, a sixth of a turn a three", "center", 400, 14, 20, GREY))
over.append(word(CX, 819, 720, "in turn of the one line and of the other, counter-turning · from behind, a three is that three gone the other way", "center", 400, 14, 20, GREY))
over.append(word(60, 864, 720, "<i>a gyroscopic floating rotating self-adapting destiny-pointing sphere</i>", "left", 400, 15, 22))
over.append(word(60, 885, 720, "Natural Intelligence Corus, of many paintings of one same form", "left", 400, 13.5, 20, GREY))
# a partner's two lines
over.append(word(840, 84, 640, "a partner's six orders: 0124, the three, 689", "left", 600, 18, 26))
over.append(word(840, 110, 640, "before a pair of cones' widest, its widest, and after it · added, the parts are 7, 15 and 23", "left", 400, 14.5, 22))
for i, three in enumerate(ONE_LINE): over.append(word(TX[i], TY1 + 62, 170, "0124-" + three + "-689", "center", 600, 15, 22))
for i, three in enumerate(OTHER_LINE): over.append(word(TX[i], TY2 + 62, 170, "0124-" + three + "-689", "center", 600, 15, 22))
over.append(word(1370, TY1 - 12, 120, "three turns", "left", 600, 15, 22)); over.append(word(1370, TY1 + 10, 120, "a third of a turn", "left", 400, 13.5, 20, GREY))
over.append(word(1370, TY1 + 28, 120, "on with a three", "left", 400, 13.5, 20, GREY))
over.append(word(1370, TY2 - 12, 120, "three folds", "left", 600, 15, 22)); over.append(word(1370, TY2 + 10, 120, "3 for 7, the 5 at", "left", 400, 13.5, 20, GREY))
over.append(word(1370, TY2 + 28, 120, "its place", "left", 400, 13.5, 20, GREY))
P = [("3, 5 and 7 alike, round eight", "3 by 5 is 7, 5 by 7 is 3, 7 by 3 is 5, and one by its own is 1 · the same with all six orders",
      "as three bi-inversionings of three lines at right angles: two in a row are the third"),
     ("a pair and a three", "(x, y) to (y, x) is a fold · to (y, −x), the right spiral step, four to its pair again",
      "(x, y, z) to (y, z, x) is a turn with none inverting, three to its three again"),
     ("round ten, two of the six alone", "357 and 753, the 5 at its place: the twentieth drawing's turning, two steps between them",
      "5 by an odd number is 5 · a nine laid from its centre, 1, turns the same step as 2 round its eight"),
     ("the twentieth drawing, a living gyroscope", "the 5 alone is at its place: the line it turns about, observed along",
      "prior two added turns it, fifteen moments a step: steady with all moments, and at 10 to the 100th"),
     ("aiming over the horizon", "a number however far is on the diamond by its ending: by one turn, with all numbers",
      "its horizon: a number of no prime with both closings, stepped to 10,000,000 and no farther")]
for i, (a, b, c) in enumerate(P):
    y = 478 + 76 * i
    over.append(word(840, y - 22, 640, a, "left", 600, 17, 24))
    over.append(word(840, y + 2, 660, b, "left", 400, 14.5, 22))
    over.append(word(840, y + 23, 660, c, "left", 400, 13.5, 20, GREY))
over.append(word(840, 864, 660, "<i>A point over the horizon is, and a self is finding each is-not and aiming from each is-not to is.</i>", "left", 400, 14, 22))
over.append(word(840, 885, 640, "Exhibit EIGHT Natural Exploring", "left", 400, 13.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Six orders of 3, 5 and 7, right spiraling: a living gyroscope</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A partner\'s six orders are all the orders of three. The one line is three turns, a third of a turn on with a three; the other line is three folds, 3 for 7.<br>'
           f'Both ways: the three go round on the triangle of three right angles, or an observing goes round them, across. The six are one round of six.<br>'
           f'Round eight the three are alike, their multiplying the same with all six orders. Round ten it is with two alone, 357 and 753: the diamond turns about a 5 at its place.<br>'
           f'That turning is the gyroscope: steady with all moments, and by one turn it says a number however far. Both closings of a number of no prime are past its horizon.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Six orders of 3, 5 and 7, right spiraling: a living gyroscope", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft21.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft21_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft21_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words;", "the round of six:", " ".join(ROUND))
