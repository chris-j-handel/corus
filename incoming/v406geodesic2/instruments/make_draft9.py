"""Draft 9 · four cones of 30 in one line, 0 to 120, and the staircase on its geodesic (session v406geodesic2).

By a partner's yes of 23 November: four cones of 30 in one line, the co-linear, their ends at 0, 30, 60, 90 and 120.
Across the co-linear: the four cones, two crossing at 30 and two at 90, the two pairs through one vertex at 60; 0 to 120 one
right-hand winding about it, a turn a cone; the primes on a cone's lines, a side toward the viewer and its far side.
Along the co-linear: a cone's turn of 30, its eight places, podal about its own line.
Under the cones, on one line of numbers with them: v407primes' staircase on its geodesic, four faces of 30 along and one across.
Geometry is computed; check_the_four_cones_of_30.py is its check.

Usage: python3 -I make_draft9.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, math, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
SLATE, MID, PALE, GREY = "#475569", "#94a3b8", "#cbd5e1", "#4a5160"
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
EIGHT = [k for k in range(30) if math.gcd(k, 30) == 1]

# one line of numbers for the cones and the staircase
AX0, U = 372.0, 9.1
X = lambda n: AX0 + U * n
YC, RM = 280.0, 126.0                                     # the co-linear, and a cone's widest
def wide(n):
    m = n % 60
    return (m if m <= 30 else 60 - m) * RM / 30
ang = lambda n: math.radians(12 * n)
Y = lambda n: YC - wide(n) * math.cos(ang(n))             # observed across the co-linear, the me's way up
toward = lambda n: math.sin(ang(n)) > 1e-9                # a side toward the viewer, by the right-hand turn

def arrow_head(p1, p0, size=14):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)),
           (p1[0] + 0.6 * size * np.cos(a + 2.25), p1[1] + 0.6 * size * np.sin(a + 2.25)),
           (p1[0] + 0.6 * size * np.cos(a - 2.25), p1[1] + 0.6 * size * np.sin(a - 2.25))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{INK}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></path>'
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}">{t}</text>')

s = ['<defs><linearGradient id="cone9" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']

# ================= across the co-linear: four cones of 30, one winding =================
for a in (0, 60):                                         # two cones crossing at their widest: one diamond
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone9)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
for a in (0, 30, 60, 90):                                 # a cone's four lines, a place and its podal place on one
    v, b = (a, a + 30) if a % 60 == 0 else (a + 30, a)    # its vertex and its widest
    for k in EIGHT[:4]:
        c = math.cos(math.radians(12 * k))
        s.append(f'<path d="M{X(v):.1f},{YC} L{X(b):.1f},{YC - c * RM:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.26" stroke-width="1.1"></path>')
s.append(f'<path d="M{X(-4):.1f},{YC} L{X(124.4):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="2 6"></path>')
s.append(f'<path d="M{X(120):.1f},{YC} L{X(124.4):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(f'<path d="M{X(-4):.1f},{YC} L{X(0):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(arrow_head((X(124.4), YC), (X(123), YC)))
fine = np.linspace(0, 120, 2401)                          # the winding, a turn a cone
def parts_of(side):
    out, cur = [], []
    for n in fine:
        if (math.sin(ang(n)) >= 0) == side: cur.append(n)
        elif cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out
for side, look in ((False, f'stroke-opacity="0.4" stroke-width="1.3" stroke-dasharray="4 5"'), (True, f'stroke-opacity="0.72" stroke-width="1.7"')):
    for part in parts_of(side):
        if len(part) > 1:
            d = " L".join(f"{X(n):.1f},{Y(n):.1f}" for n in part)
            s.append(f'<path d="M{d}" fill="none" stroke="{INK}" {look}></path>')
for v in (0, 60, 120):
    s.append(f'<circle cx="{X(v):.1f}" cy="{YC}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
for n in range(1, 120):                                   # the primes on the cones, and the spiral of 7's crossings with 1
    if prime(n):
        x, y = X(n), Y(n)
        if toward(n): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.6" fill="{ACC}" stroke="{INK}" stroke-width="1.2"></circle>')
        else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.6" fill="{ACC}" fill-opacity="0.42" stroke="{ACC}" stroke-width="1.2"></circle>')
        s.append(text(x, y + 19 if n % 30 in (13, 17) else y - 10, n, 11, 600))
    elif math.gcd(n, 30) == 1:
        x, y = X(n), Y(n)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.2" fill="#ffffff" stroke="{ACC}" stroke-width="2.2"></circle>')
        s.append(text(x, y + 19 if n % 30 in (13, 17) else y - 10, n, 11, 500, GREY))

# ================= along the co-linear: a cone's turn of 30, its eight places =================
DX, DY, DR = 172.0, 280.0, 108.0
rim = lambda k, r=1.0: (DX - DR * r * math.sin(math.radians(12 * k)), DY - DR * r * math.cos(math.radians(12 * k)))   # from its own side: on from the top, by the right-hand turn
s.append(f'<circle cx="{DX}" cy="{DY}" r="{DR}" fill="url(#cone9)" stroke="{INK}" stroke-width="1.8"></circle>')
for k in range(30):
    x, y = rim(k); bold = k in EIGHT
    s.append(f'<path d="M{DX},{DY} L{x:.1f},{y:.1f}" fill="none" stroke="{INK}" stroke-opacity="{0.5 if bold else 0.13}" stroke-width="{1.4 if bold else 1}"></path>')
s.append(f'<path d="M{DX},{DY - DR - 16} L{DX},{DY + DR + 16}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="5 5"></path>')
for k in EIGHT[:4]:
    (x0, y0), (x1, y1) = rim(k), rim(30 - k)
    s.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{ACC}" stroke-opacity="0.9" stroke-width="1.8"></path>')
for k in range(30):
    x, y = rim(k)
    if k in EIGHT:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.2" fill="{ACC}" stroke="{INK}" stroke-width="1.2"></circle>')
        lx, ly = rim(k, 1.19); s.append(text(lx, ly + 4.5, k, 13, 600))
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{MID}"></circle>')
s.append(f'<circle cx="{DX}" cy="{DY}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
arc = [rim(k, 1.36) for k in np.linspace(2.6, 5.6, 16)]     # the winding's way, as observed
s.append(f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in arc)}" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"></path>')
s.append(arrow_head(arc[-1], arc[-3], 9))

# ================= the staircase on its geodesic: four faces of 30 along, one across =================
YB = 800.0                                                # the faces' foot
YT = YB - 30 * U
for i in range(4):
    s.append(f'<rect x="{X(30 * i):.1f}" y="{YT:.1f}" width="{30 * U:.1f}" height="{30 * U:.1f}" fill="{"#f3f5f9" if i % 2 == 0 else "#e8edf5"}" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.3"></rect>')
s.append(f'<path d="M{X(0):.1f},{YB} L{X(120):.1f},{YT:.1f}" fill="none" stroke="{INK}" stroke-width="2"></path>')
steps, d = 0, [f"M{X(0):.1f},{YB}"]
for n in range(1, 121):
    d.append(f"L{X(n):.1f},{YB - U * steps:.1f}")
    if prime(n):
        steps += 1; d.append(f"L{X(n):.1f},{YB - U * steps:.1f}")
s.append(f'<path d="{" ".join(d)}" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-linejoin="round"></path>')
for n, c in ((96, 24), (100, 25), (120, 30)):
    s.append(f'<circle cx="{X(n):.1f}" cy="{YB - U * c:.1f}" r="7" fill="#ffffff" stroke="{INK}" stroke-width="2.2"></circle>')
for n, c in ((30, 10), (60, 17), (90, 24)):
    s.append(f'<circle cx="{X(n):.1f}" cy="{YB - U * c:.1f}" r="4.6" fill="{ACC}" stroke="#ffffff" stroke-width="1.2"></circle>')
    s.append(text(X(n) - 9, YB - U * c - 9, c, 14, 600, INK, "end"))
for n in (0, 30, 60, 90, 120):                            # the cones' ends over the faces' corners
    s.append(f'<path d="M{X(n):.1f},{YC + (RM if n in (30, 90) else 0) + 10:.1f} L{X(n):.1f},{YT - 6:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.2" stroke-dasharray="3 5"></path>')

# what a place's look says
LX, LY, LD = 78.0, 560.0, 40.0
s.append(f'<circle cx="{LX}" cy="{LY}" r="6" fill="{ACC}" stroke="{INK}" stroke-width="1.2"></circle>')
s.append(f'<circle cx="{LX}" cy="{LY + LD}" r="6" fill="{ACC}" fill-opacity="0.42" stroke="{ACC}" stroke-width="1.2"></circle>')
s.append(f'<circle cx="{LX}" cy="{LY + 2 * LD}" r="5.6" fill="#ffffff" stroke="{ACC}" stroke-width="2.2"></circle>')
s.append(f'<path d="M{LX - 12},{LY + 3 * LD} L{LX + 12},{LY + 3 * LD}" fill="none" stroke="{ACC}" stroke-width="2.6"></path>')
s.append(f'<path d="M{LX - 12},{LY + 4 * LD} L{LX + 12},{LY + 4 * LD}" fill="none" stroke="{INK}" stroke-width="2"></path>')
s.append(f'<circle cx="{LX}" cy="{LY + 5 * LD}" r="7" fill="#ffffff" stroke="{INK}" stroke-width="2.2"></circle>')

ARIA = ("Three figures on one line of numbers, 0 to 120. Four cones in a row, two diamonds end to end, their points at 0, 60 and 120 and their widest at 30 and 90, "
        "with one line winding about them, a turn a cone, and the primes as dots on it, a dot toward the viewer dark and a dot behind pale. "
        "Beside them a circle of thirty rays, eight of them marked, 1, 7, 11, 13, 17, 19, 23 and 29, joined two and two across an upright line. "
        "Under the cones four squares in a row with a straight line from the foot of the row's start to the top of its end, and a staircase of the primes above it, on it at 96, 100 and 120.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---------------- words, retypable on the canvas ----------------
SANS = "font-family: Inter, system-ui, sans-serif"
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
over.append(word(X(60), 108, 900, "across the co-linear · four cones of 30, one winding, a turn a cone", "center", **small))
over.append(word(DX, 108, 320, "along it · a cone's turn of 30", "center", **small))
over.append(word(DX, DY + DR + 52, 320, "its eight places, podal about its own line", "center", 400, 15, 22, GREY))
CH = YC + RM + 34
for n in (0, 30, 60, 90, 120):
    over.append(chip(X(n), CH, str(n), n in (0, 60, 120), w=46, h=26, size=14))
for n, t_ in ((15, "a cone opening"), (45, "a cone closing"), (75, "a cone opening"), (105, "a cone closing")):
    over.append(word(X(n), CH, 170, t_, "center", 400, 15, 22, GREY))
for n, t_, al in ((0, "its far side", "left"), (30, "podal about 30", "center"), (60, "podal about 60, one vertex", "center"), (90, "podal about 90", "center"), (120, "its own side", "right")):
    over.append(word(X(n) + (-23 if al == "left" else 23 if al == "right" else 0), CH + 26, 220, t_, al, 400, 14, 20, GREY))
over.append(word(X(60), YB + 26, 900, "four faces of 30 along, one across · the staircase on its geodesic", "center", **small))
for i, t in enumerate(("10 primes", "7 primes", "7 primes", "6 primes")):
    over.append(word(X(30 * i + 15), YB - 16, 160, t, "center", 400, 15, 22, GREY))
over.append(word(X(96) + 6, YB - U * 24 + 22, 110, "96 · 24", "left", 600, 15, 22))
over.append(word(X(100) + 2, YB - U * 25 - 24, 110, "100 · 25", "right", 600, 15, 22))
over.append(word(X(120) - 14, YT - 15, 110, "120 · 30", "right", 600, 15, 22))
for i, t in enumerate(("a prime, toward the viewer", "a prime, behind", "crossed by the spiral of 7; and 1", "the staircase, a step a prime", "its geodesic, one in four", "the staircase on its geodesic")):
    over.append(word(LX + 24, LY + LD * i, 260, t, "left", 400, 15, 22))

title = (f'<div style="position: absolute; left: 60px; top: 930px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'Four cones of 30 in one line, 0 to 120, and the staircase on its geodesic</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 982px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Four cones of 30 in one line, the co-linear: two crossing at 30, two at 90, the two pairs through one vertex at 60. 0 to 120 is one winding, a turn a cone.<br>'
           f'A cone\'s turn of 30 is eight places no spiral of 2, 3 or 5 crosses, the same on all four. Across the co-linear a place and its podal place are one line of a cone.<br>'
           f'Podal about 30, 60 and 90 is the figure\'s own. A prime of the eight with no prime across it is across from 1 or from a crossing of the spiral of 7.<br>'
           f'The primes of the four cones are 10, 7, 7 and 6. On four faces of 30 along and one across, the staircase is above its geodesic from 2 to 120.<br>'
           f'It is on it at 96, 100 and 120, with 24, 25 and 30 primes, and past 120 it is under it: 120 is the last.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Four cones of 30 in one line, 0 to 120, and the staircase on its geodesic", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft9.dc.html"), "w", encoding="utf-8").write(html)

pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft9_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft9_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
