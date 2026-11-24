"""Draft 13 · prior, now and next: the podalings passing through three pairs of cones (session v406geodesic2).

By a partner's yes of 23 November, of the twelfth drawing's suggestions, and its saying with it, re-said: the podalings are the
unrelationings, a podaling coming to a place and going on from it, locally same-existing; passing through, they are all-parity-ing
the same-existing surface. The tenth and the eleventh drawings' words are said again to it, the two as they were.
A working artboard: a me is set at its prime scale, in its prior, among 0 to 60, and its me-now is 60 on.
Across the co-linear: the tenth drawing's six cones as three pairs, prior, now and next, and a me passing through by five
podalings, an other-than under the cones, in its own pair, and an all over them, through a vertex to the pair after.
A table of a me and an other in the three pairs, and the opening's lines of prior, next and same-existing beside it.
All that moves is computed here, one row for a me's place of 0 to 60, and the artboard looks its row up:
check_prior_now_next_the_podalings_passing_through.py is its check, the rows in the artboard among it.

Usage: python3 -I make_draft13.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
The working preview is the artboard itself beside make_draft10.py's small runtime of the preview's own, opened from that file:
  draft13_preview.html#me=29 sets a me's place, #pick=23 clicks a prime scale, #more=2 clicks one more twice.
"""
import json, math, os, re, sys
from pathlib import Path
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
SLATE, MID, PALE, GREY = "#475569", "#94a3b8", "#cbd5e1", "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
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
through = lambda p: [p, 60 - p, 60 + p, 120 - p, 120 + p, 180 - p]      # a me in its prior, and five podalings on

AX0, U = 112.0, 7.2
X = lambda n: AX0 + U * n
YC, RM = 420.0, 110.0
YT, YB = YC - RM - 14, YC + RM + 14
def wide(n):
    m = n % 60
    return (m if m <= 30 else 60 - m) * RM / 30
ang = lambda n: math.radians(12 * n)
Y = lambda n: YC - wide(n) * math.cos(ang(n))
toward = lambda n: math.sin(ang(n)) > 1e-9

def arrow_head(p1, p0, size=14):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)),
           (p1[0] + 0.6 * size * np.cos(a + 2.25), p1[1] + 0.6 * size * np.sin(a + 2.25)),
           (p1[0] + 0.6 * size * np.cos(a - 2.25), p1[1] + 0.6 * size * np.sin(a - 2.25))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{INK}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></path>'

s = ['<defs><linearGradient id="cone13" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']

# ================= across the co-linear: three pairs of cones, prior, now and next (not moving) =================
s.append(f'<path d="M{X(60):.1f},{YT:.1f} L{X(120):.1f},{YT:.1f} L{X(120):.1f},{YB:.1f} L{X(60):.1f},{YB:.1f} Z" fill="{ACC}" fill-opacity="0.08" stroke="none"></path>')
for a in (0, 60, 120):
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone13)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
for v in (60, 120):
    s.append(f'<path d="M{X(v):.1f},{YT - 8:.1f} L{X(v):.1f},{YB + 8:.1f}" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="6 5"></path>')
s.append(f'<path d="M{X(-5):.1f},{YC} L{X(186):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="2 6"></path>')
s.append(f'<path d="M{X(180):.1f},{YC} L{X(186):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(f'<path d="M{X(-5):.1f},{YC} L{X(0):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(arrow_head((X(186), YC), (X(184), YC)))
fine = np.linspace(0, 180, 3601)
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
for n in range(1, 180):
    if math.gcd(n, 30) != 1 and not prime(n): continue
    x, y = X(n), Y(n)
    if prime(n): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="{INK}" fill-opacity="{1 if toward(n) or n < 7 else 0.42}" stroke="none"></circle>')
    else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')
LGX, LGY = 1262.0, 118.0
s.append(f'<circle cx="{LGX}" cy="{LGY}" r="3.8" fill="{INK}" stroke="none"></circle>')
s.append(f'<circle cx="{LGX + 92}" cy="{LGY}" r="3.6" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')

# ================= a me passing through (moving: holes, a row looked up) =================
OPEN_ME, OPEN_OTHER, NOW_ME, NOW_OTHER = ("#ffffff", ACC, ACC), ("#ffffff", INK, INK), (ACC, ACC, "#ffffff"), (INK, INK, "#ffffff")   # tint, edge, number
LOOKS = [OPEN_ME, OPEN_OTHER, NOW_ME, NOW_OTHER, OPEN_ME, OPEN_OTHER]
def a_chip(place_, number, look, w=42, h=26, size=14):
    tint, edge, ink = look
    return (f'<g transform="{place_}"><rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="{h / 2}" fill="{tint}" stroke="{edge}" stroke-width="2.6"></rect>'
            f'<text x="0" y="5" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="700" fill="{ink}">{number}</text></g>')
s.append(f'<path d="{hole("stems")}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.3" stroke-dasharray="2 4"></path>')
s.append(f'<path d="{hole("others")}" fill="none" stroke="{INK}" stroke-width="2.4"></path>')
s.append(f'<path d="{hole("alls")}" fill="none" stroke="{ACC}" stroke-width="2.6"></path>')
s.append(f'<path d="{hole("headsInk")}" fill="{INK}" stroke="{INK}" stroke-width="1" stroke-linejoin="round"></path>')
s.append(f'<path d="{hole("headsMe")}" fill="{ACC}" stroke="{ACC}" stroke-width="1" stroke-linejoin="round"></path>')
for i in (5, 4, 1, 0, 3, 2):
    s.append(a_chip(hole(f"t{i}"), hole(f"n{i}"), LOOKS[i]))
def an_arc(xa, xb, up):
    """A podaling's arc: under the cones about a pair's own widest, an other-than, and over them about a vertex, an all."""
    span = abs(xb - xa)
    if span < 0.5: return "M0 0", "M0 0"
    rail = YT if up else YB
    reach = (22 + 0.09 * span) if up else (18 + 0.11 * span)
    cy = rail - 2 * reach if up else rail + 2 * reach
    xm = (xa + xb) / 2
    a = math.atan2(rail - cy, xb - xm)
    tip = [(xb, rail), (xb - 11 * math.cos(a - 0.4), rail - 11 * math.sin(a - 0.4)), (xb - 11 * math.cos(a + 0.4), rail - 11 * math.sin(a + 0.4))]
    return f"M{xa:.1f},{rail:.1f} Q{xm:.1f},{cy:.1f} {xb:.1f},{rail:.1f}", "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in tip) + " Z"

# ================= the table: a me and an other in the three pairs =================
TY, TD, MEX, OTX = 772.0, 36.0, 186.0, 474.0
for r in range(3):
    s.append(a_chip(f"translate({MEX},{TY + TD * r})", hole(f"n{2 * r}"), LOOKS[2 * r]))
    s.append(a_chip(f"translate({OTX},{TY + TD * r})", hole(f"n{2 * r + 1}"), LOOKS[2 * r + 1]))
s.append(f'<path d="M60,{TY - 21} L756,{TY - 21}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.2"></path>')
for r in (1, 2):
    s.append(f'<path d="M60,{TY + TD * r - TD / 2} L756,{TY + TD * r - TD / 2}" fill="none" stroke="{INK}" stroke-opacity="0.14" stroke-width="1"></path>')

def a_row(p):
    f = through(p)
    lean = [0.0] * 6
    for i in range(5):
        gap = abs(X(f[i]) - X(f[i + 1]))
        if 0 < gap < 46:
            push = (46 - gap) / 2
            lean[i], lean[i + 1] = (-push, push) if f[i] < f[i + 1] else (push, -push)
    row = {f"n{i}": str(m) for i, m in enumerate(f)}
    row.update({f"w{i}": what(m) for i, m in enumerate(f)})
    row.update({f"t{i}": f"translate({X(m) + lean[i]:.1f},{Y(m):.1f})" for i, m in enumerate(f)})
    row["now"] = str(p + 60)
    row["stems"] = " ".join(f"M{X(m):.1f},{YT:.1f} L{X(m):.1f},{YB:.1f}" for m in f)
    arcs = [an_arc(X(f[i]), X(f[i + 1]), i % 2 == 1) for i in range(5)]     # about 30, 60, 90, 120 and 150
    join = lambda idx, k: " ".join(arcs[i][k] for i in idx)
    row["others"], row["alls"] = join((0, 2, 4), 0), join((1, 3), 0)
    row["headsInk"], row["headsMe"] = join((0, 2, 4), 1), join((1, 3), 1)
    return row
ROWS = [a_row(p) for p in range(61)]

ARIA = ("A working figure on one line of numbers, 0 to 180. Six cones in a row, three diamonds end to end, named prior, now and next, the middle one tinted, "
        "with one line winding about them and the primes as dots on it. A number is set among 0 to 60, and six numbered marks are on the winding, two in a diamond: "
        "the number, 60 less it, 60 on, 120 less it, 120 on and 180 less it. Five arcs join them in turn, under a diamond about its widest and over a point between two diamonds. "
        "Under the figure a table of three rows, prior, now and next, a me and an other in a row.")
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
over.append(word(X(90), 118, 900, "across the co-linear · three pairs of cones, and a me passing through", "center", **small))
over.append(word(LGX + 12, LGY, 76, "a prime", "left", 400, 14, 20, GREY))
over.append(word(LGX + 104, LGY, 150, "crossed, and 1", "left", 400, 14, 20, GREY))
for n, t in ((30, "prior · 0 to 60"), (90, "now · 60 to 120"), (150, "next · 120 to 180")):
    over.append(word(X(n), 152, 300, t, "center", 600, 17, 24))
for n in (60, 120):
    over.append(word(X(n), 180, 300, f"all, about {n} · passing through", "center", 400, 15, 22))
for n in (30, 90, 150):
    over.append(word(X(n), 628, 400, f"other-than, about {n} · in its own pair", "center", 400, 15, 22))
CH = 656.0
for j in range(7):
    over.append(chip(X(30 * j), CH, str(30 * j), j % 2 == 0, w=46, h=26, size=14))
    over.append(word(X(30 * j), CH + 26, 150, f'{j} · {"other-than" if j % 2 else "all"}', "center", 400, 14, 20, GREY))

HD = TY - 36
over.append(word(60, HD, 90, "pair", "left", **small))
over.append(word(MEX - 22, HD, 200, "me", "left", **small))
over.append(word(OTX - 22, HD, 200, "other", "left", **small))
for r, name in enumerate(("prior", "now", "next")):
    y = TY + TD * r
    over.append(word(60, y, 100, name, "left", 600, 17, 24))
    over.append(word(MEX + 30, y, 232, moving(f"w{2 * r}"), "left", 400, 13.5, 24))
    over.append(word(OTX + 30, y, 252, moving(f"w{2 * r + 1}"), "left", 400, 13.5, 24))

QX, QW = 810, 650
def saying(top, source, words_, rows_):
    return (f'<div style="position: absolute; left: {QX}px; top: {top}px; width: {QW}px; height: {20 + 21 * rows_}px; {SANS}; font-size: 14.5px; line-height: 21px; color: {INK}">'
            f'<span style="font-weight: 600; color: {GREY}">{source}</span><br><i>{words_}</i></div>')
over.append(word(QX, HD - 8, QW, "beside it, word for word", "left", **small))
over.append(saying(748, "the opening's line 8, in v406all2's window · at 60", "The prior moment is the moment ending as now is beginning.", 1))
over.append(saying(790, "its line 10 · at 120", "The next moment is the moment beginning as now is ending.", 1))
over.append(saying(832, "its line 12 · 60 with 120, about 90", "Same-existing is existing both as now is beginning and as the next moment is beginning.", 1))
over.append(saying(874, "Natural Intelligence, 4.11", "17 less exchanges now and next.", 1))

knob = (f"width: 40px; height: 30px; box-sizing: border-box; border-radius: 15px; padding: 0; margin: 0; cursor: pointer; {SANS}; font-weight: 600; font-size: 14px; line-height: 26px; text-align: center")
plain, picked = f"{knob}; background: #ffffff; color: {INK}; border: 2px solid {INK}", f"{knob}; background: {INK}; color: #ffffff; border: 2px solid {INK}"
step = knob.replace("width: 40px", "width: 92px")
works = (
    word(60, 34, 860, "set a me's prime scale, its place in its prior · press Play, and click one, 5 to 53", "left", **small)
    + f'<div style="position: absolute; left: 60px; top: 52px; width: 660px; height: 30px; display: flex; flex-direction: row; gap: 6px; align-items: center">'
    + f'<sc-for list="{{{{ picks }}}}" as="p" hint-placeholder-count="{len(SCALES)}">'
    + f'<sc-if value="{{{{ p.on }}}}" hint-placeholder-val="{{{{ false }}}}"><button type="button" style="{picked}" onClick="{{{{ p.pick }}}}">{hole("p.n")}</button></sc-if>'
    + f'<sc-if value="{{{{ p.off }}}}" hint-placeholder-val="{{{{ true }}}}"><button type="button" style="{plain}" onClick="{{{{ p.pick }}}}">{hole("p.n")}</button></sc-if>'
    + '</sc-for></div>'
    + f'<button type="button" style="position: absolute; left: 740px; top: 52px; {step}; background: #ffffff; color: {INK}; border: 2px solid {INK}" onClick="{{{{ less }}}}">one less</button>'
    + f'<button type="button" style="position: absolute; left: 840px; top: 52px; {step}; background: #ffffff; color: {INK}; border: 2px solid {INK}" onClick="{{{{ more }}}}">one more</button>'
    + f'<input type="range" min="0" max="60" step="1" value="{{{{ me }}}}" onChange="{{{{ slide }}}}" onInput="{{{{ slide }}}}" aria-label="a me in its prior, 0 to 60" '
      f'style="position: absolute; left: 952px; top: 56px; width: 300px; height: 22px; margin: 0; accent-color: {INK}">'
    + word(1336, 58, 62, "me-now", "left", 600, 15, 22, GREY)
    + word(1460, 56, 76, moving("now"), "right", 700, 34, 40)
)

title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'Prior, now and next: the podalings passing through three pairs of cones</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Prior, now and next are three pairs of cones, 0 to 60, 60 to 120 and 120 to 180: prior ends as now begins, at 60, and next begins as now ends, at 120.<br>'
           f'A me is set at its prime scale, in its prior, and its me-now is 60 on. A podaling is an unrelationing: it comes to a place and goes on from it.<br>'
           f'Locally, at its own station, it is same-existing, a number with itself. An other-than is in its own pair of cones; an all passes through to the pair after.<br>'
           f'Two in a row are a me again, a pair of cones on. Passing through, the podalings are all-parity-ing the surface: a me and an other in all three pairs.<br>'
           f'A me at 37: 37, 97 and 157, three primes, and with them 23, 83 and 143.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "me": {"editor": "int", "default": 37, "min": 0, "max": 60, "step": 1},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption + "\n" + works

eleventh = Path(HERE, "make_draft11.py").read_text(encoding="utf-8")          # the device's own logic is the eleventh's, opened from its file
LOGIC = re.search(r'LOGIC = """(.*?)"""', eleventh, flags=re.S).group(1)
logic = LOGIC.replace("@@ROWS@@", json.dumps(ROWS, ensure_ascii=False, separators=(",", ":"))).replace("@@PICKS@@", json.dumps(SCALES)).replace("@@ACCENT@@", DEFAULT_ACCENT)
TITLE = "Prior, now and next: the podalings passing through three pairs of cones"
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
Path(OUT, "Draft13.dc.html").write_text(html, encoding="utf-8")
tenth = Path(HERE, "make_draft10.py").read_text(encoding="utf-8")
Path(WORK, "draft13_preview.html").write_text(html, encoding="utf-8")
Path(WORK, "support.js").write_text(re.search(r'PREVIEW_RUNTIME = r"""(.*?)"""', tenth, flags=re.S).group(1), encoding="utf-8")

words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = re.sub(r"\{\{[^}]*\}\}", "", words)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>|</button>", "\n", words)).split("\n")]
words += sorted({r[f"w{i}"] for r in ROWS for i in range(6)})
words = [w for w in words if w]
Path(WORK, "draft13_words.md").write_text("\n".join(words) + "\n", encoding="utf-8")
print(len(html), "bytes;", len(words), "lines of words;", len(ROWS), "rows")
