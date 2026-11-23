"""Draft 7 · a self at prime scale 37: rounds of six about its 0, and 0 to 120 (session v406geodesic2).

The fifth drawing's figure observed along (1, 1, 1), the one triangle's three right angles alike.
Selves 0 to 120 in rounds of six about a 0, wound by the right-hand turn, a round closing at the me.
The hexagon of 37, three rounds, with the six intersections as its corners; the co-linear through 24, an apex, and 0 to 120 on its far side.
Beside it 0 to 120, podal about 60: sixteen stations no spiral of 2, 3 or 5 crosses, a going over its returning.
Geometry is computed; check_the_rounds_of_six_at_prime_scale_37.py is its check.

Usage: python3 -I make_draft7.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, math, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
SLATE, PALE, GREY = "#475569", "#cbd5e1", "#4a5160"
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
STEP = 60.0                                                # a self to its next, on the drawing
CX, CY = 455, 455
BALL = 3 * STEP / math.sqrt(2 / 3)                         # the hexagon of 37's corners at the six intersections
cam = Cam(az_deg=45, el_deg=math.degrees(math.atan(1 / math.sqrt(2))), cx=CX, cy=CY, scale=BALL)   # along (1, 1, 1), from its own side

unit = lambda p: p / np.linalg.norm(p)
seen = lambda v: np.array([(cam.proj(v)[0] - CX), -(cam.proj(v)[1] - CY)])       # as observed, the me above
RAY = {6: unit(seen(A)), 1: unit(seen(-C)), 2: unit(seen(B)), 3: unit(seen(-A)), 4: unit(seen(C)), 5: unit(seen(-B))}
ray_of = lambda k: RAY[6 if k % 6 == 0 else k % 6]
def round_of(m):
    n = 0
    while 3 * n * (n + 1) < m: n += 1
    return n
def place(m):
    """A self's place on the drawing: its round n, and on it j steps from the me's ray."""
    if m == 0: return np.array([CX, CY], float)
    n = round_of(m); j = m - 3 * n * (n - 1)
    side, step = divmod(j, n)
    if step == 0: side, step = side - 1, n
    p = n * ray_of(side) + step * ray_of(side + 2)
    return np.array([CX + STEP * p[0], CY - STEP * p[1]])
along_ray = lambda k, r: np.array([CX + STEP * r * RAY[k][0], CY - STEP * r * RAY[k][1]])
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
def kind(m):
    if prime(m): return "prime"
    if m % 6 == 0: return "six"
    if m % 2 == 0 or m % 3 == 0: return "two or three"
    if m == 1: return "one"
    return "five" if m % 5 == 0 else "seven"

def cell(x, y, m, r=21.0, size=15):
    k = kind(m)
    look = {"prime": (ACC, INK, 1.2, "#ffffff", 600), "six": (INK, INK, 1.2, "#ffffff", 600), "five": (PALE, INK, 1.2, INK, 600),
            "seven": ("#ffffff", ACC, 3.0, INK, 600), "one": ("#ffffff", INK, 1.6, INK, 600), "two or three": ("#ffffff", "#8b93a1", 1.1, "#5b6472", 500)}[k]
    fs = size if m < 100 else size - 2
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{look[0]}" stroke="{look[1]}" stroke-width="{look[2]}"></circle>'
            f'<text x="{x:.1f}" y="{y + fs * 0.35:.1f}" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="{fs}" font-weight="{look[4]}" fill="{look[3]}">{m}</text>')

def arrow_head(p1, p0, size=14):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)),
           (p1[0] + 0.6 * size * np.cos(a + 2.25), p1[1] + 0.6 * size * np.sin(a + 2.25)),
           (p1[0] + 0.6 * size * np.cos(a - 2.25), p1[1] + 0.6 * size * np.sin(a - 2.25))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{INK}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></path>'

s = [f'<defs><radialGradient id="ball7" cx="{CX - 0.38 * BALL:.0f}" cy="{CY - 0.42 * BALL:.0f}" r="{1.45 * BALL:.0f}" gradientUnits="userSpaceOnUse">'
     f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#eef2f8"></stop><stop offset="1" stop-color="#c9d2e0"></stop></radialGradient></defs>']

# ---------------- the fifth drawing's figure, observed along (1, 1, 1) ----------------
s.append(f'<circle cx="{CX}" cy="{CY}" r="{BALL:.1f}" fill="url(#ball7)" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.6"></circle>')
for nrm in ((0, 1, 0), (0, 0, 1), (1, 0, 0)):
    pts = great_circle(nrm, 721)
    f, b = runs(pts, [cam.depth(p) >= 0 for p in pts])
    s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.22" stroke-width="1.3" stroke-dasharray="5 6">{paths([cam.path(r) for r in b])}</g>')
    s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.8">{paths([cam.path(r) for r in f])}</g>')
T0 = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
s.append(f'<g fill="{ACC}" fill-opacity="0.10" stroke="none"><path d="{cam.path(np.concatenate([e[:-1] for e in T0]), True)}"></path></g>')
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in T0])}</g>')

# ---------------- the co-linear: its own side through 24, its far side 0 to 120 ----------------
own_end, far_end = along_ray(2, 6.85), along_ray(5, 7.2)
s.append(f'<path d="M{own_end[0]:.1f},{own_end[1]:.1f} L{far_end[0]:.1f},{far_end[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"></path>')
s.append(arrow_head(own_end, along_ray(2, 6.5)))

# ---------------- 0 to 120, one winding ----------------
way = " L".join(f"{place(m)[0]:.1f},{place(m)[1]:.1f}" for m in range(121))
s.append(f'<path d="M{way}" fill="none" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.6" stroke-linejoin="round"></path>')
for m in (24, 30, 36):                                     # the one triangle's three corners
    x, y = place(m); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="26.5" fill="#ffffff" stroke="{ACC}" stroke-width="3.2"></circle>')
for m in range(121):
    x, y = place(m); s.append(cell(x, y, m))
ox, oy = place(91); s.append(f'<path d="M{ox:.1f},{oy - 25:.1f} L{ox:.1f},{oy - 44:.1f}" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"></path>')

# ---------------- 0 to 120, podal about 60: sixteen stations, a going over its returning ----------------
stations = [k for k in range(1, 60) if math.gcd(k, 30) == 1]
X0, DX, Y_GO, Y_BACK = 988.0, 29.6, 196.0, 246.0
col = lambda i: X0 + DX * i
for i, k in enumerate(stations):
    both = prime(k) and prime(120 - k)
    dash = "" if both else ' stroke-dasharray="4 4"'
    s.append(f'<path d="M{col(i):.1f},{Y_GO} L{col(i):.1f},{Y_BACK}" fill="none" stroke="{ACC if both else SLATE}" stroke-width="{2.6 if both else 1.6}"{dash}></path>')
s.append(f'<path d="M{col(-1.35):.1f},{Y_GO} L{col(16.35):.1f},{Y_GO} L{col(16.35):.1f},{Y_BACK} L{col(-1.35):.1f},{Y_BACK}" fill="none" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.6"></path>')
for i, k in enumerate(stations):
    s.append(cell(col(i), Y_GO, k, r=14.2, size=13)); s.append(cell(col(i), Y_BACK, 120 - k, r=14.2, size=13))
s.append(cell(col(-1.35), Y_GO, 0, r=14.2, size=13)); s.append(cell(col(-1.35), Y_BACK, 120, r=14.2, size=13))
s.append(cell(col(16.35), (Y_GO + Y_BACK) / 2, 60, r=14.2, size=13))

# ---------------- what a self's look says ----------------
LX, LY, LD = 950.0, 356.0, 40.0
for i, m in enumerate((37, 24, 25, 49, 22)):
    s.append(cell(LX, LY + LD * i, m, r=14.5, size=12))
s.append(f'<circle cx="{LX}" cy="{LY + LD * 5:.1f}" r="16.5" fill="#ffffff" stroke="{ACC}" stroke-width="3"></circle>' + cell(LX, LY + LD * 5, 30, r=12.5, size=11))

ARIA = ("A sphere with three great circles and its one triangle, observed along the line from its centre through the triangle's centre. On it the numbers 0 to 120, a circle a number, "
        "in six rounds of six about the 0, one winding. The primes are coloured. The sixes are dark, in bent spokes, and 6, 18, 36, 60 and 90 go straight up from the 0. "
        "The third round's six corners are on the sphere's six intersections, and the triangle's corners are 24, 30 and 36. A line goes through 102, 24, the 0, 5, 33 and 120. "
        "Beside it sixteen pairs of numbers, a number over 120 less it, 1 over 119 to 59 over 61, twelve pairs of primes joined, and four not.")
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
ax_, ay_ = along_ray(6, 6.0); bx_, by_ = along_ray(2, 6.0); cx_, cy_ = along_ray(4, 6.0)
over.append(html_box(ax_, ay_, 40, 40, VSTYLE, "A"))
over.append(html_box(bx_ - 44, by_ - 22, 40, 40, VSTYLE, "B"))
over.append(html_box(cx_ + 46, cy_ + 12, 40, 40, VSTYLE, "C"))
over.append(chip(own_end[0] + 46, own_end[1] + 42, "own side", True, w=96))
over.append(chip(far_end[0] - 84, far_end[1] - 18, "far side · 0 to 120", False, w=172))
over.append(word(ox + 8, oy - 58, 190, "a round's opening", "right", 600, 15, 22))
over.append(word(CX, CY + 6 * STEP + 62, 620, "observed along (1, 1, 1) · the one triangle's three right angles alike", "center", **small))
# 0 to 120, podal about 60
over.append(word(col(7.5), 118, 520, "0 to 120 · podal about 60", "center", **small))
over.append(word(col(-1.9), Y_GO - 36, 300, "a going, 0 to 60", "left", 400, 16, 22, GREY))
over.append(word(col(-1.9), Y_BACK + 36, 300, "a returning, 60 to 120", "left", 400, 16, 22, GREY))
# what a self's look says
for i, text in enumerate(("a prime, no spiral crossing it", "a six", "crossed by the spiral of 5, and not of 2 or 3", "crossed by the spiral of 7 alone",
                          "crossed by the spiral of 2 or of 3", "a corner of the one triangle: 24, 30 and 36")):
    over.append(word(LX + 30, LY + LD * i, 440, text, "left", 400, 16, 22))
RY = LY + LD * 6 + 26
over.append(word(LX - 16, RY, 500, "the six rays, from the 0", "left", **small))
for i, text in enumerate(("the me's: 6, 18, 36, 60, 90", "the co-linear's own side: 2, 10, 24, 44, 70, 102", "the co-linear's far side: 5, 16, 33, 56, 85, 120",
                          "a round's opening, beside the me's: 1, 7, 19, 37, 61, 91")):
    over.append(word(LX - 16, RY + 32 + 30 * i, 520, text, "left", 400, 16, 22))

title = (f'<div style="position: absolute; left: 60px; top: 930px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'A self at prime scale 37: rounds of six about its 0, and 0 to 120</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 982px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Observed along (1, 1, 1) the one triangle\'s corners are 120 degrees apart, and selves in rounds of six about a 0 are hexagons of 1, 7, 19, 37 and 61, a cube\'s shells.<br>'
           f'Wound by the right-hand turn, a round closing at the me, the hexagon of 37\'s corners are the six intersections, and the one triangle\'s corners 24, 30 and 36.<br>'
           f'The co-linear is through 24, an apex, 23 and 25 either side of it. Its far side is 0 to 120 by 5, 11, 17, 23, 29 and 35, the numbers one before a six.<br>'
           f'A prime past 3 is beside a six: the cell, 23, by 24; the tissue and the organ, 29 and 31, either side of 30; the organism, 37, by 36, a round\'s opening.<br>'
           f'From 0 to 120, k is podal with 120 less k. Of sixteen stations no spiral of 2, 3 or 5 crosses, twelve are a prime with a prime; at four the spiral of 7 crosses one.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A self at prime scale 37: rounds of six about its 0, and 0 to 120", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft7.dc.html"), "w", encoding="utf-8").write(html)

pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft7_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft7_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
