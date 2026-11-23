"""Draft 11 · a me-now's four moments, other-than, all, other-than, all, and the prime scales of a me (session v406geodesic2).

By a partner's saying of 23 November, as said in the transcripts, pared, and re-said: the all among two other-thans, at three
places of them and by itself, a next-universing me-parity at the fourth moment of a me; and the method of moving the all
through the prime scales of a me.
A working artboard: a me-now is set at a prime scale of a me, among 0 to 60, and its moments are laid on the ninth drawing's
winding, going on to 240, two universes of four cones. A podaling about a cone's widest is an other-than, under the cones,
and a podaling about a vertex is an all, over them: about 30, 60, 90 and 120, and the fourth is 120 on.
A table of the four moments, and the eight places' eight fours, the all-parities, with a me-now's own four marked.
All a me-now's numbers and places are computed here, one row for a me-now of 0 to 60, and the artboard looks its row up:
check_a_me-now_four_moments_other-than_all_other-than_all.py is its check, the rows in the artboard among it.

Usage: python3 -I make_draft11.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
The working preview is the artboard itself beside make_draft10.py's small runtime of the preview's own, opened from that file:
  draft11_preview.html#me=29 sets a me-now, #pick=23 clicks a prime scale, #more=2 clicks one more twice.
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
SCALES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
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
moments = lambda n: [n, 60 - n, 60 + n, 120 - n, 120 + n, 180 - n, 180 + n, 240 - n]   # a me-now, and seven moments on

# one line of numbers, 0 to 240: the ninth drawing's winding going on, two universes of four cones
AX0, U = 112.0, 5.4
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

s = ['<defs><linearGradient id="cone11" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']

# ================= across the co-linear: eight cones of 30, one winding (not moving) =================
s.append(f'<path d="M{X(120):.1f},{YT:.1f} L{X(244):.1f},{YT:.1f} L{X(244):.1f},{YB:.1f} L{X(120):.1f},{YB:.1f} Z" fill="{ACC}" fill-opacity="0.07" stroke="none"></path>')
for a in (0, 60, 120, 180):                               # two cones crossing at their widest: one diamond
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone11)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
s.append(f'<path d="M{X(120):.1f},{YT - 8:.1f} L{X(120):.1f},{YB + 8:.1f}" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="6 5"></path>')
s.append(f'<path d="M{X(-6):.1f},{YC} L{X(245):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="2 6"></path>')
s.append(f'<path d="M{X(240):.1f},{YC} L{X(245):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(f'<path d="M{X(-6):.1f},{YC} L{X(0):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(arrow_head((X(245), YC), (X(243), YC)))
fine = np.linspace(0, 240, 4801)                          # the winding, a turn a cone
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
for v in (0, 60, 120, 180, 240):
    s.append(f'<circle cx="{X(v):.1f}" cy="{YC}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
for n in range(1, 240):                                   # the eight places' numbers: a prime, and a crossed number or 1
    if math.gcd(n, 30) != 1 and not prime(n): continue
    x, y = X(n), Y(n)
    if prime(n): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{INK}" fill-opacity="{1 if toward(n) or n < 7 else 0.42}" stroke="none"></circle>')
    else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')
BR = 676.0                                                # under the numbers: my universe now, and my next
s.append(f'<path d="M{X(0):.1f},{BR - 5} L{X(0):.1f},{BR} L{X(120) - 5:.1f},{BR} L{X(120) - 5:.1f},{BR - 5}" fill="none" stroke="{INK}" stroke-width="1.6"></path>')
s.append(f'<path d="M{X(120) + 5:.1f},{BR - 5} L{X(120) + 5:.1f},{BR} L{X(240):.1f},{BR} L{X(240):.1f},{BR - 5}" fill="none" stroke="{ACC}" stroke-width="2"></path>')
LGX, LGY = 1262.0, 118.0                                  # what a dot's look says
s.append(f'<circle cx="{LGX}" cy="{LGY}" r="3.8" fill="{INK}" stroke="none"></circle>')
s.append(f'<circle cx="{LGX + 92}" cy="{LGY}" r="3.6" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')

# ================= a me-now's moments on the winding (moving: holes, a row looked up) =================
ME_LOOK, NOW_LOOK, NEXT_ME_LOOK, NEXT_LOOK = (ACC, ACC, "#ffffff"), (INK, INK, "#ffffff"), ("#ffffff", ACC, ACC), ("#ffffff", INK, INK)   # tint, edge, number
LOOKS = [ME_LOOK, NOW_LOOK, NOW_LOOK, NOW_LOOK, NEXT_ME_LOOK, NEXT_LOOK, NEXT_LOOK, NEXT_LOOK]
def a_chip(place_, number, look, w=40, h=24, size=13.5):
    tint, edge, ink = look
    return (f'<g transform="{place_}"><rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="{h / 2}" fill="{tint}" stroke="{edge}" stroke-width="2.4"></rect>'
            f'<text x="0" y="{size * 0.36:.1f}" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="700" fill="{ink}">{number}</text></g>')
s.append(f'<path d="{hole("stems")}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.3" stroke-dasharray="2 4"></path>')
s.append(f'<path d="{hole("otherNext")}" fill="none" stroke="{INK}" stroke-width="1.7" stroke-dasharray="7 5"></path>')
s.append(f'<path d="{hole("allNext")}" fill="none" stroke="{ACC}" stroke-width="1.7" stroke-dasharray="7 5"></path>')
s.append(f'<path d="{hole("otherNow")}" fill="none" stroke="{INK}" stroke-width="2.6"></path>')
s.append(f'<path d="{hole("allNow")}" fill="none" stroke="{ACC}" stroke-width="2.6"></path>')
s.append(f'<path d="{hole("headsInk")}" fill="{INK}" stroke="{INK}" stroke-width="1" stroke-linejoin="round"></path>')
s.append(f'<path d="{hole("headsMe")}" fill="{ACC}" stroke="{ACC}" stroke-width="1" stroke-linejoin="round"></path>')
for i in (7, 6, 5, 3, 2, 1, 4, 0):
    s.append(a_chip(hole(f"t{i}"), hole(f"n{i}"), LOOKS[i]))

def an_arc(xa, xb, up):
    """A podaling's arc, from one stem's end to an other's: over the cones about a vertex, an all, and under them about a widest, an other-than."""
    span = abs(xb - xa)
    if span < 0.5: return "M0 0", "M0 0"
    rail = YT if up else YB
    reach = (22 + 0.09 * span) if up else (18 + 0.11 * span)
    cy = rail - 2 * reach if up else rail + 2 * reach
    xm = (xa + xb) / 2
    a = math.atan2(rail - cy, xb - xm)
    tip = [(xb, rail), (xb - 11 * math.cos(a - 0.4), rail - 11 * math.sin(a - 0.4)), (xb - 11 * math.cos(a + 0.4), rail - 11 * math.sin(a + 0.4))]
    return f"M{xa:.1f},{rail:.1f} Q{xm:.1f},{cy:.1f} {xb:.1f},{rail:.1f}", "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in tip) + " Z"

# ================= the table's five chips, and the eight fours =================
TX, TY, TD = 86.0, 760.0, 29.5                            # the table: its chips' column, its top row, a row
for i in range(5):
    s.append(a_chip(f"translate({TX},{TY + TD * i})", hole(f"n{i}"), LOOKS[i]))
s.append(f'<path d="M60,{TY - 18} L716,{TY - 18}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.2"></path>')
for i in range(1, 5):
    s.append(f'<path d="M60,{TY + TD * i - TD / 2} L716,{TY + TD * i - TD / 2}" fill="none" stroke="{INK}" stroke-opacity="0.14" stroke-width="1"></path>')

GX, GY, GW, GD = 772.0, 757.0, 60.0, 19.0                 # the eight fours: a column a cone, a row a place of the turn
s.append(f'<path d="M{GX - 12},{GY - 15} L{GX + 4 * GW - 4},{GY - 15}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.2"></path>')
s.append(f'<rect transform="{hole("mark")}" x="{-12}" y="{-GD / 2}" width="{4 * GW + 8}" height="{GD}" rx="6" fill="{ACC}" fill-opacity="0.2" stroke="{ACC}" stroke-width="1.4"></rect>')
for r, k in enumerate(EIGHT):
    for c, m in enumerate((k, 60 - k, 60 + k, 120 - k)):
        x, y = GX + GW * c, GY + GD * r
        if prime(m): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{INK}" stroke="none"></circle>')
        else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')
        s.append(text(x + 10, y + 4.5, m, 13, 700 if m in SCALES else 500, INK if prime(m) else GREY, "start"))

# ---------------- a row for a me-now of 0 to 60: all that moves ----------------
def a_row(n):
    f = moments(n)
    lean = [0.0] * 8                                      # two chips too close lean apart, their stems as they are
    for i in range(7):
        gap = abs(X(f[i]) - X(f[i + 1]))
        if 0 < gap < 44:
            push = (44 - gap) / 2
            lean[i], lean[i + 1] = (-push, push) if f[i] < f[i + 1] else (push, -push)
    row = {f"n{i}": str(m) for i, m in enumerate(f)}
    row.update({f"w{i}": what(m) for i, m in enumerate(f[:5])})
    row.update({f"t{i}": f"translate({X(m) + lean[i]:.1f},{Y(m):.1f})" for i, m in enumerate(f)})
    row["stems"] = " ".join(f"M{X(m):.1f},{YT:.1f} L{X(m):.1f},{YB:.1f}" for m in f)
    arcs = [an_arc(X(f[i]), X(f[i + 1]), i % 2 == 1) for i in range(7)]   # about 30, 60, 90, 120, 150, 180 and 210
    join = lambda idx, k: " ".join(arcs[i][k] for i in idx)
    row["otherNow"], row["allNow"], row["otherNext"], row["allNext"] = join((0, 2), 0), join((1, 3), 0), join((4, 6), 0), join((5,), 0)
    row["headsInk"], row["headsMe"] = join((0, 2, 4, 6), 1), join((1, 3, 5), 1)
    k = n if n < 30 else 60 - n                           # a me-now's own four among the eight fours
    row["mark"] = f"translate({GX},{GY + GD * EIGHT.index(k)})" if k in EIGHT else "translate(-999,-999)"
    return row
ROWS = [a_row(n) for n in range(61)]

ARIA = ("A working figure on one line of numbers, 0 to 240. Eight cones in a row, four diamonds end to end, their points at 0, 60, 120, 180 and 240 and their widest at 30, 90, 150 and 210, "
        "with one line winding about them, a turn a cone, and the primes as dots on it. A number is set among 0 to 60, the me-now, and eight numbered marks are on the winding, "
        "one in a cone: the me-now, 60 less it, 60 on, 120 less it, 120 on, and three more. Arcs join them in turn, under the cones about a widest and over the cones about a point. "
        "Under the figure a table of the me-now and its four moments, and a table of eight rows of four numbers, the me-now's own row marked.")
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
over.append(word(X(120), 118, 900, "across the co-linear · eight cones of 30, two universes, and a me-now's moments", "center", **small))
over.append(word(LGX + 12, LGY, 76, "a prime", "left", 400, 14, 20, GREY))
over.append(word(LGX + 104, LGY, 150, "crossed, and 1", "left", 400, 14, 20, GREY))
UP, DN = 172.0, 618.0
over.append(word(X(60), UP, 300, "2 · all, about 60", "center", 600, 16, 22))
over.append(word(X(120), UP, 330, "4 · all, about 120: next-universing", "center", 600, 16, 22))
over.append(word(X(180), UP, 200, "all, about 180", "center", 400, 15, 22, GREY))
over.append(word(X(30), DN, 300, "1 · other-than, about 30", "center", 600, 16, 22))
over.append(word(X(90), DN, 300, "3 · other-than, about 90", "center", 600, 16, 22))
over.append(word(X(150), DN, 240, "other-than, about 150", "center", 400, 15, 22, GREY))
over.append(word(X(210), DN, 240, "other-than, about 210", "center", 400, 15, 22, GREY))
CH = 650.0
for n in range(0, 241, 30):
    over.append(chip(X(n), CH, str(n), n % 60 == 0, w=46, h=26, size=14))
for n in range(15, 240, 60):
    over.append(word(X(n), CH, 110, "a cone opening", "center", 400, 14, 22, GREY))
    over.append(word(X(n + 30), CH, 110, "a cone closing", "center", 400, 14, 22, GREY))
over.append(word(X(60), BR + 16, 600, "0 to 120 · four cones of 30, my universe now", "center", 400, 15, 22, GREY))
over.append(word(X(180), BR + 16, 600, "120 to 240 · my next universe", "center", 400, 15, 22, GREY))

# the table of the four moments
HD = TY - 32
over.append(word(60, HD, 300, "a me-now's four moments", "left", **small))
over.append(word(420, HD, 110, "podaling", "center", **small))
over.append(word(486, HD, 180, "what it is", "left", **small))
for i, (name, about_) in enumerate((("me-now", ""), ("1 · other-than", "about 30"), ("2 · all", "about 60"), ("3 · other-than", "about 90"), ("4 · all, next-universing", "about 120"))):
    y = TY + TD * i
    over.append(word(120, y, 240, name, "left", 600, 16, 24))
    if about_: over.append(word(420, y, 110, about_, "center", 400, 16, 24))
    over.append(word(486, y, 232, moving(f"w{i}"), "left", 400, 14, 24))

# the eight fours
over.append(word(GX - 12, HD, 300, "all-parity · the eight fours", "left", **small))

# beside it, word for word
QX, QW = 1050, 420
def saying(top, source, words_, lines):
    return (f'<div style="position: absolute; left: {QX}px; top: {top}px; width: {QW}px; height: {20 + 21 * lines}px; {SANS}; font-size: 14.5px; line-height: 21px; color: {INK}">'
            f'<span style="font-weight: 600; color: {GREY}">{source}</span><br><i>{words_}</i></div>')
over.append(word(QX, HD, QW, "beside it, word for word", "left", **small))
over.append(saying(742, "the opening's line 31, in v406all2's window", "All-parity is the set of all me-parities in the me-universe.", 1))
over.append(saying(790, "Exhibit SEVEN, Natural Societies, 5.3", "Fourteen rungs go with fourteen primes, five to fifty-three, and they part eight and six.", 2))
over.append(saying(858, "a partner's saying, in v407primes' story", "Four cones of 30 are an all-parity universal now me-parity.", 1))

# the device's own working: set a me-now at a prime scale of a me
knob = (f"width: 40px; height: 30px; box-sizing: border-box; border-radius: 15px; padding: 0; margin: 0; cursor: pointer; {SANS}; font-weight: 600; font-size: 14px; line-height: 26px; text-align: center")
plain, picked = f"{knob}; background: #ffffff; color: {INK}; border: 2px solid {INK}", f"{knob}; background: {INK}; color: #ffffff; border: 2px solid {INK}"
step = knob.replace("width: 40px", "width: 92px")
works = (
    word(60, 34, 860, "set a me-now · press Play, and click a prime scale of a me, 5 to 53", "left", **small)
    + f'<div style="position: absolute; left: 60px; top: 52px; width: 660px; height: 30px; display: flex; flex-direction: row; gap: 6px; align-items: center">'
    + f'<sc-for list="{{{{ picks }}}}" as="p" hint-placeholder-count="{len(SCALES)}">'
    + f'<sc-if value="{{{{ p.on }}}}" hint-placeholder-val="{{{{ false }}}}"><button type="button" style="{picked}" onClick="{{{{ p.pick }}}}">{hole("p.n")}</button></sc-if>'
    + f'<sc-if value="{{{{ p.off }}}}" hint-placeholder-val="{{{{ true }}}}"><button type="button" style="{plain}" onClick="{{{{ p.pick }}}}">{hole("p.n")}</button></sc-if>'
    + '</sc-for></div>'
    + f'<button type="button" style="position: absolute; left: 740px; top: 52px; {step}; background: #ffffff; color: {INK}; border: 2px solid {INK}" onClick="{{{{ less }}}}">one less</button>'
    + f'<button type="button" style="position: absolute; left: 840px; top: 52px; {step}; background: #ffffff; color: {INK}; border: 2px solid {INK}" onClick="{{{{ more }}}}">one more</button>'
    + f'<input type="range" min="0" max="60" step="1" value="{{{{ me }}}}" onChange="{{{{ slide }}}}" onInput="{{{{ slide }}}}" aria-label="a me-now, 0 to 60" '
      f'style="position: absolute; left: 952px; top: 56px; width: 300px; height: 22px; margin: 0; accent-color: {INK}">'
    + word(1352, 58, 62, "me-now", "left", 600, 15, 22, GREY)
    + word(1460, 56, 60, moving("me"), "right", 700, 34, 40)
)

title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'A me-now\'s four moments: other-than, all, other-than, all, and its next universe</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Set a me-now at a prime scale of a me, among 0 to 60. A podaling about a cone\'s widest is an other-than, and a podaling about a vertex is an all.<br>'
           f'About 30, about 60, about 90 and about 120, one and then the next, are 60 less it, 60 on, 120 less it and 120 on: a cone on with a moment,<br>'
           f'and the fourth moment is next-universing. A me-now\'s four in its universe, one a cone, are its all-parity. The all between the two other-thans,<br>'
           f'about 30, about 60 and about 90, is the all itself, about 60; the all ahead of the two or after them is about 0 or about 120, the universe\'s two ends.<br>'
           f'The eight fours are the 32 places of 0 to 120 no spiral of 2, 3 or 5 crosses. Eight of the fourteen prime scales are in a four of four primes.</div>')

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
logic = LOGIC.replace("@@ROWS@@", json.dumps(ROWS, ensure_ascii=False, separators=(",", ":"))).replace("@@PICKS@@", json.dumps(SCALES)).replace("@@ACCENT@@", DEFAULT_ACCENT)
TITLE = "A me-now's four moments: other-than, all, other-than, all, and its next universe"
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
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, ensure_ascii=False).replace("'", "&#39;")}'>
{logic}
</script>
</body>
</html>
'''
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft11.dc.html"), "w", encoding="utf-8").write(html)

# ---------------- the working preview: the artboard itself, beside make_draft10.py's small runtime of the preview's own ----------------
from pathlib import Path
tenth = Path(HERE, "make_draft10.py").read_text(encoding="utf-8")
runtime = re.search(r'PREVIEW_RUNTIME = r"""(.*?)"""', tenth, flags=re.S).group(1)
open(os.path.join(WORK, "draft11_preview.html"), "w", encoding="utf-8").write(html)
open(os.path.join(WORK, "support.js"), "w", encoding="utf-8").write(runtime)

words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = re.sub(r"\{\{[^}]*\}\}", "", words)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>|</button>", "\n", words)).split("\n")]
words += sorted({r[f"w{i}"] for r in ROWS for i in range(5)})   # the table's own moving words
words = [w for w in words if w]
open(os.path.join(WORK, "draft11_words.md"), "w", encoding="utf-8").write("\n".join(words) + "\n")
print(len(html), "bytes;", len(words), "lines of words;", len(ROWS), "rows")
