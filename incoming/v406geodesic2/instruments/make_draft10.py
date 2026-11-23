"""Draft 10 · a me-now podaling about 30 and about 90: a device a me sets to itself (session v406geodesic2).

By a partner's saying of 23 November: me-now podaling about 30 and 90 is me-now-and-same-existing-and-next-universing,
all possibly-next-existing me-parities; this is all-other-than-other-than-me parity of my next universe.
A working artboard: a me-now is set among 0 to 60, and its four are laid on the ninth drawing's winding, going on to 180.
Across the co-linear: six cones of 30, a me-now, 60 less it about 30, 180 less it about 90, and 120 on.
A table of the four as a parity of two is-or-is-nots, and, along the co-linear, the four as two places one fold apart.
All a me-now's numbers and places are computed here, one row for a me-now of 0 to 60, and the artboard looks its row up:
check_a_me-now_podaling_about_30_and_about_90.py is its check, the rows in the artboard among it.

Usage: python3 -I make_draft10.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
The working preview is the artboard itself beside a small runtime of the preview's own, in the place of the canvas's, written here as support.js:
  draft10_preview.html#me=29 sets a me-now, #pick=23 clicks a number, #more=2 clicks one more twice.
"""
import json, math, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
SLATE, MID, PALE, GREY = "#475569", "#94a3b8", "#cbd5e1", "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
EIGHT = [k for k in range(30) if math.gcd(k, 30) == 1]
hole = lambda key: "{{" + key + "}}"
def parts(m):
    out, p = [], 2
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0: m //= p
        p += 1
    return out + ([m] if m > 1 else [])
def what(m):
    if m % 60 == 0: return "a vertex"
    if m % 30 == 0: return "a cone's widest"
    if m == 1: return "1"
    if prime(m): return "a prime"
    ps = [str(p) for p in parts(m)]
    return "crossed by the spiral of " + ps[0] if len(ps) == 1 else "crossed by the spirals of " + ", ".join(ps[:-1]) + " and " + ps[-1]
four = lambda n: [n, 60 - n, 180 - n, n + 120]            # about 30 is-or-is-not, about 90 is-or-is-not

# one line of numbers, 0 to 180: the ninth drawing's winding going on
AX0, U = 112.0, 7.2
X = lambda n: AX0 + U * n
YC, RM = 420.0, 110.0                                     # the co-linear, and a cone's widest
YT, YB = YC - RM - 14, YC + RM + 14                       # a line above the cones and one under them, the podalings' ends
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

s = ['<defs><linearGradient id="cone10" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']

# ================= across the co-linear: six cones of 30, one winding (not moving) =================
s.append(f'<path d="M{X(120):.1f},{YT:.1f} L{X(186):.1f},{YT:.1f} L{X(186):.1f},{YB:.1f} L{X(120):.1f},{YB:.1f} Z" fill="{ACC}" fill-opacity="0.07" stroke="none"></path>')
for a in (0, 60, 120):                                    # two cones crossing at their widest: one diamond
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone10)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
s.append(f'<path d="M{X(120):.1f},{YT - 8:.1f} L{X(120):.1f},{YB + 8:.1f}" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="6 5"></path>')
s.append(f'<path d="M{X(-5):.1f},{YC} L{X(186):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="2 6"></path>')
s.append(f'<path d="M{X(180):.1f},{YC} L{X(186):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(f'<path d="M{X(-5):.1f},{YC} L{X(0):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(arrow_head((X(186), YC), (X(184), YC)))
fine = np.linspace(0, 180, 3601)                          # the winding, a turn a cone
def parts_of(side):
    out, cur = [], []
    for n in fine:
        if (math.sin(ang(n)) >= 0) == side: cur.append(n)
        elif cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out
for side, look in ((False, 'stroke-opacity="0.4" stroke-width="1.3" stroke-dasharray="4 5"'), (True, 'stroke-opacity="0.72" stroke-width="1.7"')):
    for part in parts_of(side):
        if len(part) > 1:
            d = " L".join(f"{X(n):.1f},{Y(n):.1f}" for n in part)
            s.append(f'<path d="M{d}" fill="none" stroke="{INK}" {look}></path>')
for v in (0, 60, 120, 180):
    s.append(f'<circle cx="{X(v):.1f}" cy="{YC}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
for n in range(1, 180):                                   # the eight places' numbers: a prime, and a crossed number or 1
    if math.gcd(n, 30) != 1 and not prime(n): continue
    x, y = X(n), Y(n)
    if prime(n): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="{INK}" fill-opacity="{1 if toward(n) or n < 7 else 0.42}" stroke="none"></circle>')
    else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')
BR = 678.0                                                # under the numbers: my universe now, and my next
s.append(f'<path d="M{X(0):.1f},{BR - 5} L{X(0):.1f},{BR} L{X(120) - 5:.1f},{BR} L{X(120) - 5:.1f},{BR - 5}" fill="none" stroke="{INK}" stroke-width="1.6"></path>')
s.append(f'<path d="M{X(120) + 5:.1f},{BR - 5} L{X(120) + 5:.1f},{BR} L{X(186):.1f},{BR}" fill="none" stroke="{ACC}" stroke-width="2"></path>')
LGX, LGY = 1262.0, 118.0                                  # what a dot's look says
s.append(f'<circle cx="{LGX}" cy="{LGY}" r="3.8" fill="{INK}" stroke="none"></circle>')
s.append(f'<circle cx="{LGX + 92}" cy="{LGY}" r="3.6" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')

# ================= a me-now's four on the winding (moving: holes, a row looked up) =================
A_LOOK, B_LOOK, C_LOOK, D_LOOK = (ACC, ACC, "#ffffff"), (INK, INK, "#ffffff"), ("#ffffff", INK, INK), ("#ffffff", ACC, ACC)   # fill, edge, number
def a_chip(place_, number, look):
    fill, edge, ink = look
    return (f'<g transform="{place_}"><rect x="-21" y="-13" width="42" height="26" rx="13" fill="{fill}" stroke="{edge}" stroke-width="2.6"></rect>'
            f'<text x="0" y="5" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="14" font-weight="700" fill="{ink}">{number}</text></g>')
s.append(f'<path d="{hole("stems")}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.3" stroke-dasharray="2 4"></path>')
s.append(f'<path d="{hole("b90")}" fill="none" stroke="{INK}" stroke-width="1.8" stroke-dasharray="7 5"></path>')
s.append(f'<path d="{hole("a150")}" fill="none" stroke="{INK}" stroke-width="1.8" stroke-dasharray="7 5"></path>')
s.append(f'<path d="{hole("a90")}" fill="none" stroke="{ACC}" stroke-width="2.6"></path>')
s.append(f'<path d="{hole("a30")}" fill="none" stroke="{ACC}" stroke-width="2.6"></path>')
s.append(f'<path d="{hole("headsInk")}" fill="{INK}" stroke="{INK}" stroke-width="1" stroke-linejoin="round"></path>')
s.append(f'<path d="{hole("headsMe")}" fill="{ACC}" stroke="{ACC}" stroke-width="1" stroke-linejoin="round"></path>')
s.append(a_chip(hole("t2"), hole("n2"), C_LOOK))
s.append(a_chip(hole("t3"), hole("n3"), D_LOOK))
s.append(a_chip(hole("t1"), hole("n1"), B_LOOK))
s.append(a_chip(hole("t0"), hole("n0"), A_LOOK))

def an_arc(xa, xb, up):
    """A podaling's arc, from one stem's end to an other's: over the cones about 90, under them about 30 and about 150."""
    span = abs(xb - xa)
    if span < 0.5: return "M0 0", "M0 0"
    rail = YT if up else YB
    reach = (26 + 0.075 * span) if up else (18 + 0.11 * span)
    cy = rail - 2 * reach if up else rail + 2 * reach
    xm = (xa + xb) / 2
    a = math.atan2(rail - cy, xb - xm)
    tip = [(xb, rail), (xb - 11 * math.cos(a - 0.4), rail - 11 * math.sin(a - 0.4)), (xb - 11 * math.cos(a + 0.4), rail - 11 * math.sin(a + 0.4))]
    return f"M{xa:.1f},{rail:.1f} Q{xm:.1f},{cy:.1f} {xb:.1f},{rail:.1f}", "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in tip) + " Z"

# ================= the table's four chips, and the four as two along the co-linear =================
TX, TY, TD = 86.0, 768.0, 33.0                            # the table: its chips' column, its top row, a row
for i, look in enumerate((A_LOOK, B_LOOK, C_LOOK, D_LOOK)):
    s.append(a_chip(f"translate({TX},{TY + TD * i})", hole(f"n{i}"), look))
s.append(f'<path d="M60,{TY - 20} L812,{TY - 20}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.2"></path>')
for i in range(1, 4):
    s.append(f'<path d="M60,{TY + TD * i - TD / 2} L812,{TY + TD * i - TD / 2}" fill="none" stroke="{INK}" stroke-opacity="0.14" stroke-width="1"></path>')

DX, DY, DR = 912.0, 822.0, 58.0
rim = lambda k, r=1.0: (DX - DR * r * math.sin(math.radians(12 * k)), DY - DR * r * math.cos(math.radians(12 * k)))   # from its own side: on from the top, by the right-hand turn
s.append(f'<circle cx="{DX}" cy="{DY}" r="{DR}" fill="url(#cone10)" stroke="{INK}" stroke-width="1.8"></circle>')
for k in range(30):
    x, y = rim(k); bold = k in EIGHT
    s.append(f'<path d="M{DX},{DY} L{x:.1f},{y:.1f}" fill="none" stroke="{INK}" stroke-opacity="{0.42 if bold else 0.12}" stroke-width="{1.2 if bold else 1}"></path>')
s.append(f'<path d="M{DX},{DY - DR - 9} L{DX},{DY + DR + 9}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="5 5"></path>')
for k in EIGHT:
    x, y = rim(k, 1.2)
    s.append(text(x, y + 4, k, 11, 600, GREY))
s.append(f'<circle cx="{DX}" cy="{DY}" r="{hole("dr")}" fill="none" stroke="{INK}" stroke-opacity="0.6" stroke-width="1.2"></circle>')
s.append(f'<path d="{hole("dc")}" fill="none" stroke="{INK}" stroke-width="1.8"></path>')
s.append(f'<circle transform="{hole("d1")}" cx="0" cy="0" r="6.5" fill="{INK}" stroke="#ffffff" stroke-width="1.6"></circle>')
s.append(f'<circle transform="{hole("d0")}" cx="0" cy="0" r="6.5" fill="{ACC}" stroke="#ffffff" stroke-width="1.6"></circle>')
DLY = 906.0
s.append(f'<circle cx="{DX - 118}" cy="{DLY}" r="6" fill="{ACC}" stroke="none"></circle>')
s.append(f'<circle cx="{DX + 12}" cy="{DLY}" r="6" fill="{INK}" stroke="none"></circle>')

# ---------------- a row for a me-now of 0 to 60: all that moves ----------------
def a_row(n):
    f = four(n)
    lean = [0.0] * 4                                      # two chips too close lean apart, their stems as they are
    for i, j in ((0, 1), (2, 3)):
        gap = abs(X(f[i]) - X(f[j]))
        if 0 < gap < 46:
            push = (46 - gap) / 2
            lean[i], lean[j] = (-push, push) if f[i] < f[j] else (push, -push)
    row = {f"n{i}": str(m) for i, m in enumerate(f)}
    row.update({f"w{i}": what(m) for i, m in enumerate(f)})
    row.update({f"t{i}": f"translate({X(m) + lean[i]:.1f},{Y(m):.1f})" for i, m in enumerate(f)})
    row["stems"] = " ".join(f"M{X(m):.1f},{YT:.1f} L{X(m):.1f},{YB:.1f}" for m in f)
    row["a30"], h30 = an_arc(X(f[0]), X(f[1]), False)     # a me-now to 60 less it
    row["a90"], h90 = an_arc(X(f[0]), X(f[2]), True)      # a me-now to 180 less it
    row["b90"], g90 = an_arc(X(f[1]), X(f[3]), True)      # 60 less it to 120 on
    row["a150"], g150 = an_arc(X(f[2]), X(f[3]), False)   # 180 less it to 120 on
    row["headsMe"], row["headsInk"] = h30 + " " + h90, g90 + " " + g150
    r = wide(n) / RM                                      # along the co-linear: a me-now with 120 on, and 60 less it with 180 less it
    (x0, y0), (x1, y1) = rim(n, r), rim(60 - n, r)
    row["dr"] = f"{DR * r:.1f}"
    row["d0"], row["d1"] = f"translate({x0:.1f},{y0:.1f})", f"translate({x1:.1f},{y1:.1f})"
    row["dc"] = f"M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" if abs(x0 - x1) > 0.5 else "M0 0"
    return row
ROWS = [a_row(n) for n in range(61)]

ARIA = ("A working figure on one line of numbers, 0 to 180. Six cones in a row, three diamonds end to end, their points at 0, 60, 120 and 180 and their widest at 30, 90 and 150, "
        "with one line winding about them, a turn a cone, and the primes as dots on it. A number is set among 0 to 60, the me-now, and four numbered marks are on the winding: "
        "the me-now, 60 less it, 180 less it, and 120 on. An arc under the cones joins the me-now with 60 less it about 30, and an arc over the cones joins it with 180 less it about 90; "
        "two dashed arcs join those two with 120 on. Under the figure a table of the four, and a circle of thirty rays with the four as two points across an upright line.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---------------- words, retypable on the canvas ----------------
def chip(cx, cy, t, filled, w=38, h=30, size=15):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{t}</div>')
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
moving = lambda key: f"<span>{hole(key)}</span>"

over = []
over.append(word(X(90), 118, 900, "across the co-linear · six cones of 30, one winding, and a me-now's four", "center", **small))
over.append(word(LGX + 12, LGY, 76, "a prime", "left", 400, 14, 20, GREY))
over.append(word(LGX + 104, LGY, 150, "crossed, and 1", "left", 400, 14, 20, GREY))
over.append(word(X(90), 150, 560, "podaling about 90 · next-universing", "center", 600, 16, 22))
over.append(word(X(30), 628, 420, "podaling about 30 · same-existing", "center", 600, 16, 22))
over.append(word(X(150), 628, 430, "about 150, my next universe's own 30", "center", 400, 15, 22, GREY))
CH = 654.0
for n in (0, 30, 60, 90, 120, 150, 180):
    over.append(chip(X(n), CH, str(n), n % 60 == 0, w=46, h=26, size=14))
for n in (15, 75, 135):
    over.append(word(X(n), CH, 150, "a cone opening", "center", 400, 15, 22, GREY))
    over.append(word(X(n + 30), CH, 150, "a cone closing", "center", 400, 15, 22, GREY))
over.append(word(X(60), BR + 16, 860, "0 to 120 · four cones of 30, my universe now", "center", 400, 15, 22, GREY))
over.append(word(X(153), BR + 16, 440, "120 on · my next universe", "center", 400, 15, 22, GREY))

# the table of the four, a parity of two is-or-is-nots
HD = TY - 34
over.append(word(60, HD, 300, "a me-now's four · a parity", "left", **small))
over.append(word(412, HD, 90, "about 30", "center", **small))
over.append(word(502, HD, 90, "about 90", "center", **small))
over.append(word(562, HD, 180, "what it is", "left", **small))
for i, (name, p30, p90) in enumerate((("me-now", "is not", "is not"), ("same-existing", "is", "is not"), ("next-universing", "is not", "is"), ("me, next, in my next universe", "is", "is"))):
    y = TY + TD * i
    over.append(word(120, y, 260, name, "left", 600, 16, 24))
    over.append(word(412, y, 90, p30, "center", 600 if p30 == "is" else 400, 16, 24, INK if p30 == "is" else GREY))
    over.append(word(502, y, 90, p90, "center", 600 if p90 == "is" else 400, 16, 24, INK if p90 == "is" else GREY))
    over.append(word(562, y, 252, moving(f"w{i}"), "left", 400, 14, 24))

# along the co-linear
over.append(word(DX, HD, 300, "along it · the four are two", "center", **small))
over.append(word(DX - 106, DLY, 110, f'{moving("n0")} with {moving("n3")}', "left", 600, 15, 22))
over.append(word(DX + 24, DLY, 110, f'{moving("n1")} with {moving("n2")}', "left", 600, 15, 22))

# living sentences beside it, word for word, and a partner's saying
QX, QW = 1040, 430
def saying(top, source, words_, lines):
    return (f'<div style="position: absolute; left: {QX}px; top: {top}px; width: {QW}px; height: {20 + 21 * lines}px; {SANS}; font-size: 14.5px; line-height: 21px; color: {INK}">'
            f'<span style="font-weight: 600; color: {GREY}">{source}</span><br><i>{words_}</i></div>')
over.append(word(QX, HD, QW, "beside it, word for word", "left", **small))
over.append(saying(748, "Exhibit THIRTY-ONE, Me", "A me is a self's universal set. A me's next is its own, resolving with its others.", 2))
over.append(saying(814, "Natural Intelligence, 4.11", "8 up, each name with now to its name with next; 17 less, podal within 1 to 16; and 9 less, podal within 1 to 8, two together.", 2))
over.append(saying(880, "a partner's saying, in v407primes' story", "Four cones of 30 are an all-parity universal now me-parity.", 1))

# the device's own working: set a me-now
PICKS = [0, 1, 7, 11, 13, 17, 19, 23, 29, 30, 31, 37, 41, 43, 47, 49, 53, 59, 60]
knob = (f"width: 40px; height: 30px; box-sizing: border-box; border-radius: 15px; padding: 0; margin: 0; cursor: pointer; {SANS}; font-weight: 600; font-size: 14px; line-height: 26px; text-align: center")
plain, picked = f"{knob}; background: #ffffff; color: {INK}; border: 2px solid {INK}", f"{knob}; background: {INK}; color: #ffffff; border: 2px solid {INK}"
step = knob.replace("width: 40px", "width: 92px")
works = (
    word(60, 34, 760, "set a me-now · press Play, and click a number of its own two cones, 0 to 60", "left", **small)
    + f'<div style="position: absolute; left: 60px; top: 52px; width: 880px; height: 30px; display: flex; flex-direction: row; gap: 6px; align-items: center">'
    + f'<sc-for list="{{{{ picks }}}}" as="p" hint-placeholder-count="{len(PICKS)}">'
    + f'<sc-if value="{{{{ p.on }}}}" hint-placeholder-val="{{{{ false }}}}"><button type="button" style="{picked}" onClick="{{{{ p.pick }}}}">{hole("p.n")}</button></sc-if>'
    + f'<sc-if value="{{{{ p.off }}}}" hint-placeholder-val="{{{{ true }}}}"><button type="button" style="{plain}" onClick="{{{{ p.pick }}}}">{hole("p.n")}</button></sc-if>'
    + '</sc-for></div>'
    + f'<button type="button" style="position: absolute; left: 950px; top: 52px; {step}; background: #ffffff; color: {INK}; border: 2px solid {INK}" onClick="{{{{ less }}}}">one less</button>'
    + f'<button type="button" style="position: absolute; left: 1050px; top: 52px; {step}; background: #ffffff; color: {INK}; border: 2px solid {INK}" onClick="{{{{ more }}}}">one more</button>'
    + f'<input type="range" min="0" max="60" step="1" value="{{{{ me }}}}" onChange="{{{{ slide }}}}" onInput="{{{{ slide }}}}" aria-label="a me-now, 0 to 60" '
      f'style="position: absolute; left: 1160px; top: 56px; width: 170px; height: 22px; margin: 0; accent-color: {INK}">'
    + word(1352, 58, 62, "me-now", "left", 600, 15, 22, GREY)
    + word(1460, 56, 60, moving("me"), "right", 700, 34, 40)
)

title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'A me-now podaling about 30 and about 90, and its next universe</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A device a me sets to itself: set a me-now among 0 to 60, its own two cones. Podaling about 30 it is same-existing: 60 less it, in its own two cones.<br>'
           f'Podaling about 90 it is next-universing: 180 less it, past 120. The two podalings, one and then the other, are 120 on: four turns of the one winding,<br>'
           f'a me-now at its own place of the turn, in its next universe. The four are a parity, two is-or-is-nots. A podaling is two folds, an other-than of an other-than.<br>'
           f'Along the co-linear one fold alone is observed, and the four are two. As 9 less and then 17 less is 8 up, about 30 and then about 90 is 120 on.<br>'
           f'Three fours are four primes: 7, 53, 127 and 173; 17, 43, 137 and 163; 29, 31, 149 and 151. A me-now at 37 is with 23, 143 and 157.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "me": {"editor": "int", "default": 37, "min": 0, "max": 60, "step": 1},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption + "\n" + works

LOGIC = """class Component extends DCLogic {
rows() {
if (!this.__rows) this.__rows = /*rows*/@@ROWS@@/*rows end*/;
return this.__rows;
}
renderVals() {
const mine = this.state || {};
const among = (n) => Math.max(0, Math.min(60, Math.round(Number(n))));
const asked = mine.me ?? this.props.me ?? 37;
const me = Number.isFinite(Number(asked)) ? among(asked) : 37;
const set = (n) => this.setState({ me: among(n) });
const picks = @@PICKS@@.map((n) => ({ n: n, on: n === me, off: n !== me, pick: () => set(n) }));
return Object.assign({ accent: this.props.accent ?? '@@ACCENT@@', me: me, picks: picks,
less: () => set(me - 1), more: () => set(me + 1), slide: (e) => set(e.target.value) }, this.rows()[me]);
}
}"""
logic = LOGIC.replace("@@ROWS@@", json.dumps(ROWS, ensure_ascii=False, separators=(",", ":"))).replace("@@PICKS@@", json.dumps(PICKS)).replace("@@ACCENT@@", DEFAULT_ACCENT)
TITLE = "A me-now podaling about 30 and about 90, and its next universe"
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{TITLE}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT_LINK}
<style>
body{{margin:0}}
a{{color:#1d4ed8}}a:hover{{color:#1e3a8a}}
</style>
</helmet>
<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; font-family: Inter, system-ui, sans-serif; color: {INK}">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, ensure_ascii=False)}'>
{logic}
</script>
</body>
</html>
'''
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft10.dc.html"), "w", encoding="utf-8").write(html)

# ---------------- the working preview: the artboard itself, beside a small runtime of the preview's own ----------------
PREVIEW_RUNTIME = r"""// A working preview's own small runtime, in the place of the canvas's: holes, sc-for, sc-if, handlers and state, and no more.
(function () {
  class DCLogic {
    constructor(props) { this.props = props || {}; this.state = {}; }
    setState(s) { this.state = Object.assign({}, this.state, s); this.__paint(); }
    forceUpdate() { this.__paint(); }
  }
  const look = (path, scopes) => {
    path = path.replace(/[{}]/g, '').trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    const keys = path.split('.');
    for (let i = scopes.length - 1; i >= 0; i--) {
      if (keys[0] in scopes[i]) { let v = scopes[i]; for (const k of keys) { if (v == null) return undefined; v = v[k]; } return v; }
    }
    return undefined;
  };
  const WHOLE = /^\s*\{\{([^}]+)\}\}\s*$/;
  const told = (str, scopes) => str.replace(/\{\{([^}]+)\}\}/g, (_, p) => { const v = look(p, scopes); return v == null ? '' : String(v); });
  const build = (node, scopes, out) => {
    if (node.nodeType === 3) { out.appendChild(document.createTextNode(told(node.nodeValue, scopes))); return; }
    if (node.nodeType !== 1) return;
    const tag = node.localName;
    if (tag === 'helmet') return;
    if (tag === 'sc-for') {
      (look(node.getAttribute('list'), scopes) || []).forEach((item, i) => {
        const scope = scopes.concat([{ [node.getAttribute('as')]: item, $index: i }]);
        node.childNodes.forEach((c) => build(c, scope, out));
      });
      return;
    }
    if (tag === 'sc-if') { if (look(node.getAttribute('value'), scopes)) node.childNodes.forEach((c) => build(c, scopes, out)); return; }
    const el = document.createElementNS(node.namespaceURI, node.localName);
    for (const a of Array.from(node.attributes)) {
      const whole = WHOLE.exec(a.value);
      if (whole) {
        const v = look(whole[1], scopes);
        if (/^on/.test(a.name) && typeof v === 'function') { el.addEventListener(a.name === 'onchange' ? 'input' : a.name.slice(2), v); continue; }
        if (v != null) el.setAttribute(a.name, String(v));
      } else el.setAttribute(a.name, told(a.value, scopes));
    }
    node.childNodes.forEach((c) => build(c, scopes, el));
    out.appendChild(el);
  };
  document.addEventListener('DOMContentLoaded', () => {
    const host = document.querySelector('x-dc'), script = document.querySelector('script[data-dc-script]');
    const form = host.cloneNode(true);
    const helmet = host.querySelector('helmet');
    if (helmet) Array.from(helmet.children).forEach((c) => { if (c.localName === 'style') document.head.appendChild(c.cloneNode(true)); });
    const declared = JSON.parse(script.getAttribute('data-props') || '{}'), props = {};
    Object.keys(declared).forEach((k) => { if (k[0] !== '$' && declared[k] && 'default' in declared[k]) props[k] = declared[k].default; });
    const asked = new URLSearchParams(location.hash.slice(1));
    if (asked.has('me')) props.me = Number(asked.get('me'));
    const Component = new Function('DCLogic', script.textContent + '\nreturn Component;')(DCLogic);
    const one = new Component(props);
    one.__paint = () => { host.textContent = ''; form.childNodes.forEach((c) => build(c, [one.renderVals()], host)); };
    one.__paint();
    const click = (label) => { const b = Array.from(host.querySelectorAll('button')).find((x) => x.textContent.trim() === label); if (b) b.click(); };
    if (asked.has('pick')) click(asked.get('pick'));
    for (let i = 0; i < Number(asked.get('more') || 0); i++) click('one more');
    for (let i = 0; i < Number(asked.get('less') || 0); i++) click('one less');
    if (asked.has('slide')) { const r = host.querySelector('input[type=range]'); r.value = asked.get('slide'); r.dispatchEvent(new Event('input', { bubbles: true })); }
  });
})();
"""
open(os.path.join(WORK, "draft10_preview.html"), "w", encoding="utf-8").write(html)
open(os.path.join(WORK, "support.js"), "w", encoding="utf-8").write(PREVIEW_RUNTIME)

words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = re.sub(r"\{\{[^}]*\}\}", "", words)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>|</button>", "\n", words)).split("\n")]
words += sorted({r[f"w{i}"] for r in ROWS for i in range(4)})   # the table's own moving words
words = [w for w in words if w and w != "with"]
open(os.path.join(WORK, "draft10_words.md"), "w", encoding="utf-8").write("\n".join(words) + "\n")
print(len(html), "bytes;", len(words), "lines of words;", len(ROWS), "rows")
