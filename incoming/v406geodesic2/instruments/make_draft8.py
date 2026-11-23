"""Draft 8 · the cube of 5: five selves on its line, and 120 about it (session v406geodesic2).

Beside the seventh drawing's rounds, the second saying of all 5s, by a partner's yes.
Across its line: the shells 1, 7, 19, 37 and 61, a shell about the cube before it, from the corus, in the one triangle's own eighth; their five corners one line, along (1, 1, 1).
Along it: the hexagon of 61, a place 5, 4, 3, 2 or 1 selves deep; about the line 24, 36, 36 and 24.
Under the two: 0 to 120 by the four rounds, its primes, and their podaling about 60.
Geometry is computed; check_the_cube_of_5_and_its_line.py is its check.

Usage: python3 -I make_draft8.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import itertools, json, math, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
SLATE, MID, PALE, GREY = "#475569", "#94a3b8", "#cbd5e1", "#4a5160"
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))

def arrow_head(p1, p0, size=14):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)),
           (p1[0] + 0.6 * size * np.cos(a + 2.25), p1[1] + 0.6 * size * np.sin(a + 2.25)),
           (p1[0] + 0.6 * size * np.cos(a - 2.25), p1[1] + 0.6 * size * np.sin(a - 2.25))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{INK}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></path>'

def ball(key, cx, cy, R):
    return (f'<radialGradient id="ball8{key}" cx="{cx - 0.38 * R:.0f}" cy="{cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#eef2f8"></stop><stop offset="1" stop-color="#c9d2e0"></stop></radialGradient>')

def sphere(cam, key):
    """The fifth drawing's figure, light: its sphere, its three circles and the one triangle."""
    out = [f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{cam.s:.1f}" fill="url(#ball8{key})" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.5"></circle>']
    for nrm in ((0, 1, 0), (0, 0, 1), (1, 0, 0)):
        pts = great_circle(nrm, 721)
        f, b = runs(pts, [cam.depth(p) >= 0 for p in pts])
        out.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1.2" stroke-dasharray="5 6">{paths([cam.path(r) for r in b])}</g>')
        out.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.42" stroke-width="1.6">{paths([cam.path(r) for r in f])}</g>')
    T0 = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
    out.append(f'<g fill="{ACC}" fill-opacity="0.10" stroke="none"><path d="{cam.path(np.concatenate([e[:-1] for e in T0]), True)}"></path></g>')
    out.append(f'<g fill="none" stroke="{ACC}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in T0])}</g>')
    return "".join(out)

# ================= across the line: five shells, their corners one line =================
S1 = 62.0                                                 # a self to its next, on this figure
across = Cam(az_deg=68, el_deg=20, cx=420, cy=420, scale=3 * S1)   # the fifth drawing's own view; the sphere is three steps
P = lambda p: np.array(across.proj(np.array(p, float) / 3))
selves = list(itertools.product(range(5), repeat=3))
SHELL = {1: MID, 2: SLATE, 3: ACC, 4: INK}
s = ['<defs>' + ball("a", across.cx, across.cy, across.s) + ball("b", 985, 395, 3 * 46 / math.sqrt(2 / 3)) + '</defs>']
s.append(sphere(across, "a"))
for axis in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    a, b = P((0, 0, 0)), P(tuple(4.75 * v for v in axis))
    s.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1.2"></path>')
for k in (1, 2, 3, 4):                                    # a shell about the cube before it, outward from the corus
    for turn in range(3):
        quad = [[k, 0, 0], [k, k, 0], [k, k, k], [k, 0, k]]
        quad = [[v[(i - turn) % 3] for i in range(3)] for v in quad]
        d = " L".join(f"{P(v)[0]:.1f},{P(v)[1]:.1f}" for v in quad)
        edge = (INK, 0.8, 1.6) if k == 3 else (INK, 0.5, 1.1)
        s.append(f'<path d="M{d} Z" fill="#ffffff" fill-opacity="0.22" stroke="{edge[0]}" stroke-opacity="{edge[1]}" stroke-width="{edge[2]}" stroke-linejoin="round"></path>')
    for p in selves:
        if max(p) == k and min(p) != k:
            x, y = P(p); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.7" fill="{SHELL[k]}" stroke="#ffffff" stroke-width="1"></circle>')
far_end, own_end = P((-1.25, -1.25, -1.25)), P((5.05, 5.05, 5.05))
s.append(f'<path d="M{far_end[0]:.1f},{far_end[1]:.1f} L{own_end[0]:.1f},{own_end[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"></path>')
s.append(arrow_head(own_end, P((4.7, 4.7, 4.7))))
for k in range(5):
    x, y = P((k, k, k))
    look = ("#ffffff", INK) if k == 0 else (SHELL[k], "#ffffff")
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8.5" fill="{look[0]}" stroke="{look[1]}" stroke-width="2.6"></circle>')
    if k: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10.5" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')

# ================= along the line: the hexagon of 61, a place 5 to 1 deep =================
S2 = 46.0
BX, BY = 985, 395
along = Cam(az_deg=45, el_deg=math.degrees(math.atan(1 / math.sqrt(2))), cx=BX, cy=BY, scale=3 * S2 / math.sqrt(2 / 3))
unit = lambda p: p / np.linalg.norm(p)
seen = lambda v: np.array([(along.proj(v)[0] - BX), -(along.proj(v)[1] - BY)])
RAY = {6: unit(seen(A)), 1: unit(seen(-C)), 2: unit(seen(B)), 3: unit(seen(-A)), 4: unit(seen(C)), 5: unit(seen(-B))}
ray_of = lambda k: RAY[6 if k % 6 == 0 else k % 6]
def round_of(m):
    n = 0
    while 3 * n * (n + 1) < m: n += 1
    return n
def place(m):
    if m == 0: return np.array([BX, BY], float)
    n = round_of(m); j = m - 3 * n * (n - 1)
    side, step = divmod(j, n)
    if step == 0: side, step = side - 1, n
    p = n * ray_of(side) + step * ray_of(side + 2)
    return np.array([BX + S2 * p[0], BY - S2 * p[1]])
DEEP = {5: (INK, "#ffffff"), 4: (SLATE, "#ffffff"), 3: (MID, INK), 2: (PALE, INK), 1: ("#ffffff", INK)}
def deep(x, y, n, r=17.5, size=15):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{DEEP[n][0]}" stroke="{INK}" stroke-width="1.2"></circle>'
            f'<text x="{x:.1f}" y="{y + size * 0.35:.1f}" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="600" fill="{DEEP[n][1]}">{n}</text>')
s.append(sphere(along, "b"))
for n in (1, 2, 3, 4):                                    # a round's outline, between it and its next
    outline = " L".join(f"{BX + S2 * (n + 0.5) * RAY[k][0] * 1.0:.1f},{BY - S2 * (n + 0.5) * RAY[k][1]:.1f}" for k in (6, 1, 2, 3, 4, 5))
    s.append(f'<path d="M{outline} Z" fill="none" stroke="{INK}" stroke-opacity="0.28" stroke-width="1.3" stroke-dasharray="3 5"></path>')
for m in range(61):
    x, y = place(m); s.append(deep(x, y, 5 - round_of(m)))
LX, LY, LD = 1250.0, 262.0, 44.0
for i, n in enumerate((5, 4, 3, 2, 1)):
    s.append(deep(LX, LY + LD * i, n, r=15, size=13))

# ================= 0 to 120 by the four rounds: its primes, podal about 60 =================
X0, U, YL = 118.0, 10.7, 850.0
X = lambda k: X0 + U * k
ends = [0, 24, 60, 96, 120]
for i in range(4):
    col, op = (ACC, 0.30) if i in (0, 3) else (SLATE, 0.26)
    s.append(f'<rect x="{X(ends[i]):.1f}" y="{YL - 8}" width="{X(ends[i + 1]) - X(ends[i]):.1f}" height="16" fill="{col}" fill-opacity="{op}"></rect>')
s.append(f'<path d="M{X(0):.1f},{YL} L{X(120):.1f},{YL}" fill="none" stroke="{INK}" stroke-width="1.6"></path>')
for e in ends:
    s.append(f'<path d="M{X(e):.1f},{YL - 14} L{X(e):.1f},{YL + 14}" fill="none" stroke="{INK}" stroke-width="2"></path>')
for k in range(1, 60):
    if prime(k) and prime(120 - k):
        rx = (60 - k) * U
        s.append(f'<path d="M{X(k):.1f},{YL - 7} A{rx:.1f},{rx * 0.2:.1f} 0 0 1 {X(120 - k):.1f},{YL - 7}" fill="none" stroke="{ACC}" stroke-opacity="0.85" stroke-width="1.8"></path>')
for k, far in ((29, 91), (43, 77), (49, 71)):
    rx = (60 - k) * U
    s.append(f'<path d="M{X(k):.1f},{YL - 7} A{rx:.1f},{rx * 0.2:.1f} 0 0 1 {X(far):.1f},{YL - 7}" fill="none" stroke="{SLATE}" stroke-width="1.5" stroke-dasharray="4 4"></path>')
for m in (49, 77, 91):
    s.append(f'<circle cx="{X(m):.1f}" cy="{YL}" r="5.5" fill="#ffffff" stroke="{ACC}" stroke-width="2.4"></circle>')
for m in range(2, 121):
    if prime(m):
        alone = not prime(120 - m)
        s.append(f'<circle cx="{X(m):.1f}" cy="{YL}" r="{6.2 if alone else 5.5}" fill="{ACC}" stroke="{INK if alone else "#ffffff"}" stroke-width="{2 if alone else 1.2}"></circle>')

ARIA = ("Three figures. A cube of five selves a side in the one eighth of a sphere, drawn as four shells about its corner at the sphere's centre, with one line through the centre and the corners of the shells, five dots on it. "
        "The same cube observed along that line: a hexagon of 61 circles, the middle one marked 5, and the rounds about it marked 4, 3, 2 and 1. "
        "Under the two, a line of numbers from 0 to 120 in four parts, to 24, to 60, to 96 and to 120, the primes as dots on it, and twelve arcs joining a prime with 120 less it.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---------------- words, retypable on the canvas ----------------
SANS = "font-family: Inter, system-ui, sans-serif"
def chip(cx, cy, text, filled, w=38, h=30, size=15):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{text}</div>')
def word(x, cy, w, text, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{text}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")

over = []
# ---- across the line
for k, text in enumerate(("1", "7", "19", "37", "61")):
    x, y = P((k, k, k)); over.append(chip(x + 25, y - 25, text, k == 3, w=36, h=26, size=14))
ax_, ay_ = P((0, 0, 3)); bx_, by_ = P((3, 0, 0)); cx_, cy_ = P((0, 3, 0))
over.append(html_box(ax_ + 20, ay_ - 20, 40, 40, VSTYLE, "A"))
over.append(html_box(bx_ - 24, by_ + 16, 40, 40, VSTYLE, "B"))
over.append(html_box(cx_ + 26, cy_ + 12, 40, 40, VSTYLE, "C"))
ox, oy = P((0, 0, 0)); over.append(word(ox + 40, oy + 12, 110, "the corus", "left", 600, 15, 22))
over.append(word(own_end[0] - 16, own_end[1] - 8, 170, "along (1, 1, 1)", "right", 600, 15, 22))
over.append(word(across.cx - 40, 652, 640, "across the line · five shells, their five corners co-linear", "center", **small))
# ---- along the line
over.append(html_box(BX, BY - 5.05 * S2, 40, 40, VSTYLE, "A"))
over.append(html_box(BX + 5.05 * S2 * RAY[2][0] - 6, BY - 5.05 * S2 * RAY[2][1] + 6, 40, 40, VSTYLE, "B"))
over.append(html_box(BX + 5.05 * S2 * RAY[4][0] + 6, BY - 5.05 * S2 * RAY[4][1] + 6, 40, 40, VSTYLE, "C"))
over.append(word(BX, 652, 560, "along the line, toward the corus · the hexagon of 61", "center", **small))
for i, text in enumerate(("on the line: 5 selves", "round 1: 6 places, 4 deep, 24", "round 2: 12 places, 3 deep, 36", "round 3: 18 places, 2 deep, 36", "round 4: 24 places, 1 deep, 24")):
    over.append(word(LX + 26, LY + LD * i, 250, text, "left", 400, 15, 22))
over.append(word(LX - 16, LY + LD * 5 + 8, 250, "120 about the line", "left", 600, 15, 22))
over.append(word(LX - 16, LY + LD * 5 + 44, 250, "a cube of 3, of 4, of 5:", "left", 400, 15, 22))
over.append(word(LX - 16, LY + LD * 5 + 68, 250, "24, 60, 120 about its line", "left", 400, 15, 22))
over.append(word(LX - 16, LY - LD - 4, 250, "a place's selves", "left", **small))
# ---- 0 to 120
over.append(word(X(0), YL - 136, 620, "0 to 120 by the four rounds · its primes, podal about 60", "left", **small))
for e in ends:
    over.append(chip(X(e), YL + 34, str(e), e in (0, 60, 120), w=46, h=26, size=14))
for i, text in enumerate(("24 · nine primes", "36 · eight primes", "36 · seven primes", "24 · six primes")):
    over.append(word((X(ends[i]) + X(ends[i + 1])) / 2, YL + 34, 200, text, "center", 400, 15, 22, GREY))

title = (f'<div style="position: absolute; left: 60px; top: 930px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'The cube of 5: five selves on its line, and 120 about it</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 982px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'The cube of 5 is the shells 1, 7, 19, 37 and 61, a shell about the cube before it, from the corus. Their five corners are co-linear, along (1, 1, 1): all 5s.<br>'
           f'About the line are 120 selves. By shells they are 6, 18, 36 and 60: to 6, to 24, to 60 and to 120. By rounds they are 24, 36, 36 and 24: to 24, to 60, to 96 and to 120.<br>'
           f'Observed along the line the cube is the hexagon of 61, a place 5, 4, 3, 2 or 1 selves deep. A cube of 3, of 4 and of 5 is 24, 60 and 120 about its line.<br>'
           f'0 to 120 by the four rounds is podal about 60, 24 with 24 and 36 with 36. Its primes are nine, eight, seven and six: six podal in a round, and 3, 2, 1 and none more.<br>'
           f'The more are 2, 3 and 5, the spirals of 120 itself; 29 and 43, their podals 91 and 77 crossed by the spiral of 7; and 71, its podal 49, 7 by 7.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The cube of 5: five selves on its line, and 120 about it", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft8.dc.html"), "w", encoding="utf-8").write(html)

pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft8_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft8_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
