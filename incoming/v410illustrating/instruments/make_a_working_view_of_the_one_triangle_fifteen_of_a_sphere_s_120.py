"""v410illustrating · a working view: the one triangle of three right angles, fifteen of a sphere's 120.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_a_working_view_of_the_one_triangle_fifteen_of_a_sphere_s_120.py A_FOLDER_FOR_ITS_WORKING_PREVIEW .

It is a working view and no drawing of the set: no number and no artboard are its own. It lays one way of a
partner's saying of 27 November, a me-parity, five, outward on the sphere opening to a torus, for a partner's is or
is-not ahead of a drawing. What it draws is executed by
`a_five_on_the_sphere_opening_to_a_torus_two_ways_executed.py`, opened here, and no drawing is made with an is-not.

Its placings, no execution says them: the three views side by side; a tint and a number, 1 to 5, for a three of the
fifteen; a filled mark for a corner of five and an open mark for a corner of three.
Do no harm: it writes its preview and its words in the folder given, outside the set.
"""
import importlib.util, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of v406geodesic
from geom import *
def opened(name):
    spec = importlib.util.spec_from_file_location(name[:20], os.path.join(HERE, name)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
f = opened("a_five_on_the_sphere_opening_to_a_torus_two_ways_executed.py")
c57 = opened("check_one_triangle_three_right_angles_bi-folding_1_to_17.py")

WORK = sys.argv[1]
W, H = 1320, 880
GREY, SLATE = "#4a5160", "#475569"
SANS = "font-family: Inter, system-ui, sans-serif"
A, B, C = c57.A, c57.B, c57.C

G = f.made_by(f.MIRRORS + [f.ROUND3, f.ROUND5])
assert len(G) == 120
p0 = f.unit(f.V5 + 1.3 * f.V3 + 0.7 * f.V2)
inside = [g for g in G if np.all(g @ p0 > 1e-9)]
assert len(inside) == 15
k3 = lambda v: tuple(np.round(v, 5) + 0.0)
three_of, n = {}, 0                                    # a small triangle's three, 1 to 5, by the one triangle's own round of three
for g in sorted(inside, key=lambda g: -float((g @ p0) @ f.V3)):
    if k3(g @ p0) in three_of: continue
    n += 1
    for j in range(3): three_of[k3(np.linalg.matrix_power(f.ROUND3, j) @ g @ p0)] = n
assert n == 5
mirrors = [g for g in G if np.linalg.det(g) < 0 and abs(np.trace(g) - 1) < 1e-6]
normals = [f.unit(((np.eye(3) - m) / 2)[:, int(np.argmax(np.abs(np.diag((np.eye(3) - m) / 2))))]) for m in mirrors]
own3 = [i for i, nn in enumerate(normals) if max(abs(nn)) > 0.999]
assert len(mirrors) == 15 and len(own3) == 3
fives = {k3(g @ f.V5): g @ f.V5 for g in G}; threes = {k3(g @ f.V3): g @ f.V3 for g in G}
assert len(fives) == 12 and len(threes) == 20
on_it = lambda v: bool(np.all(v > -1e-9))
fives_on, threes_on = [v for v in fives.values() if on_it(v)], [v for v in threes.values() if on_it(v)]
assert len(fives_on) == 3 and len(threes_on) == 4

def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def vname(cx, cy, t, size=24):
    return (f'<div style="position: absolute; left: {cx - 20:.0f}px; top: {cy - 16:.0f}px; width: 40px; height: 32px; line-height: 32px; text-align: center; '
            f"font-family: 'STIX Two Text', Georgia, serif; font-style: italic; font-weight: 500; font-size: {size}px; color: {INK}\">{t}</div>")
s, over = [], []
s.append('<defs><radialGradient id="ballw" cx="170" cy="330" r="290" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ffffff"></stop>'
         '<stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop></radialGradient></defs>')

# ---- 1 · a sphere, its fifteen mirrors, and the one triangle
cam = Cam(az_deg=45, el_deg=33, cx=250, cy=440, scale=190); R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ballw)"></circle>')
edges = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
s.append(f'<path d="{cam.path(np.concatenate([edges[0], edges[1][1:], edges[2][1:]]), True)}" fill="{ACC}" fill-opacity="0.2" stroke="none"></path>')
for i, nn in enumerate(normals):
    pts = great_circle(nn, 721); fr, bk = runs(pts, [vis(p) for p in pts])
    if i in own3:
        s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.35" stroke-width="1.2" stroke-dasharray="4 5">{paths([cam.path(r) for r in bk])}</g>')
        s.append(f'<g fill="none" stroke="{ACC}" stroke-width="2.4" stroke-linecap="round">{paths([cam.path(r) for r in fr])}</g>')
    else:
        s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1">{paths([cam.path(r) for r in fr])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
for v in fives.values():
    if vis(v) and cam.depth(v) > 0.03:
        x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{INK}" stroke="#ffffff" stroke-width="1.5"></circle>')
ax, ay = cam.proj(A); bx, by = cam.proj(B); cx_, cy_ = cam.proj(C)
over.append(vname(ax - 4, ay - 30, "A")); over.append(vname(bx - 26, by + 10, "B")); over.append(vname(cx_ + 26, cy_ + 10, "C"))
over.append(word(60, 196, 420, "1 · a sphere, its fifteen mirrors", weight=600, size=15))
over.append(word(60, 220, 420, "the opening figure's three in the accent · ● a corner of five", size=12.5, color=GREY))
over.append(word(250, 660, 420, "fifteen mirrors are five threes of mirrors at right angles", align="center", size=12.5, color=GREY))
over.append(word(250, 680, 420, "the opening figure is on this sphere five ways", align="center", size=12.5, color=GREY))

# ---- 2 · the one triangle, fifteen
cam = Cam(az_deg=45, el_deg=35.2644, cx=760, cy=500, scale=272)
TINT = {1: (ACC, 0.34), 2: (SLATE, 0.26), 3: (ACC, 0.14), 4: (SLATE, 0.10), 5: ("#f1f5f9", 1.0)}
for g in inside:
    p, q, r = g @ f.V5, g @ f.V3, g @ f.V2; t = three_of[k3(g @ p0)]; col, op = TINT[t]
    ring = np.concatenate([slerp(p, q, 24), slerp(q, r, 24)[1:], slerp(r, p, 24)[1:]])
    s.append(f'<path d="{cam.path(ring, True)}" fill="{col}" fill-opacity="{op}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"></path>')
    x, y = cam.proj(f.unit(p + q + r)); over.append(word(x, y, 20, str(t), align="center", size=12, weight=600, color=INK))
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')
for v in threes_on:
    x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="1.8"></circle>')
for v in fives_on:
    x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>')
for V in (A, B, C):
    x, y = cam.proj(V); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
ax, ay = cam.proj(A); bx, by = cam.proj(B); cx_, cy_ = cam.proj(C)
over.append(vname(ax, ay - 26, "A")); over.append(word(ax + 16, ay - 26, 70, "the me", size=13, weight=600))
over.append(vname(bx - 26, by + 6, "B")); over.append(vname(cx_ + 26, cy_ + 6, "C"))
over.append(word(520, 196, 520, "2 · the one triangle of three right angles, fifteen", weight=600, size=15))
over.append(word(520, 220, 620, "● a corner of five, three on its sides · ○ a corner of three, one at its middle and three on its sides", size=12.5, color=GREY))
NOTES = ["a small triangle is of 36, 60 and 90: 6 over 180",
         "120 of them are 720, as eight of 90 over are",
         "the one triangle is fifteen of them",
         "five threes, 1 to 5, by its own round of three",
         "a corner of five on a side: a rectangle's corner",
         "a round of five is golden, 1.618: no whole number"]
for i, t in enumerate(NOTES):
    over.append(word(990, 262 + 22 * i, 320, "● " + t, size=12.5, color=INK))

# ---- 3 · three golden rectangles at right angles, a rectangle on a mirror
cam = Cam(az_deg=28, el_deg=22, cx=1140, cy=560, scale=118); R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="#f6f8fb" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.2"></circle>')
for i in own3:
    pts = great_circle(normals[i], 721); fr, bk = runs(pts, [vis(p) for p in pts])
    s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.4" stroke-width="1" stroke-dasharray="3 4">{paths([cam.path(r) for r in bk])}</g>')
    s.append(f'<g fill="none" stroke="{ACC}" stroke-width="1.8" stroke-linecap="round">{paths([cam.path(r) for r in fr])}</g>')
P_ = f.PHI
RECT = [[(0, 1, P_), (0, 1, -P_), (0, -1, -P_), (0, -1, P_)], [(1, P_, 0), (1, -P_, 0), (-1, -P_, 0), (-1, P_, 0)], [(P_, 0, 1), (-P_, 0, 1), (-P_, 0, -1), (P_, 0, -1)]]
for r in sorted(RECT, key=lambda r: min(cam.depth(f.unit(c)) for c in r)):
    ring = [f.unit(c) for c in r]
    s.append(f'<path d="{cam.path(ring, True)}" fill="{SLATE}" fill-opacity="0.10" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></path>')
for r in RECT:
    for c_ in r:
        x, y = cam.proj(f.unit(c_)); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{INK}" stroke="#ffffff" stroke-width="1.4"></circle>')
over.append(word(990, 416, 320, "3 · three golden rectangles at right angles", weight=600, size=15))
over.append(word(1140, 700, 320, "a rectangle is on a mirror of the three", align="center", size=12.5, color=GREY))
over.append(word(1140, 720, 320, "their twelve corners are the twelve corners of five", align="center", size=12.5, color=GREY))

# ---- its head, its title and its lines
over.append(word(60, 34, 1200, "a working view, no drawing of the set · beside the 57th · one way of a partner's saying, executed, for a partner's is or is-not", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 1200, "A me-parity is the other-than of the other-than of all-parity.", size=20, h=28))
over.append(word(60, 108, 1200, "Three golden rectangles at right angles are on the opening figure's three mirrors, a rectangle a mirror.", size=20, h=28))
over.append(word(60, 138, 1200, "Their twelve corners are corners of five, and the one triangle of three right angles is fifteen of a sphere's 120.", size=20, h=28))
title = (f'<div style="position: absolute; left: 0px; top: 746px; width: {W}px; height: 44px; line-height: 44px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 30px; color: {INK}">One Triangle, Three Golden Rectangles</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 790px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 20px; color: {ACC}">Bi-Tri-Volutioning a Round of Five, Outward on a Sphere</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 826px; width: {W}px; height: 24px; line-height: 24px; text-align: center; {SANS}; font-size: 14.5px; color: {GREY}">'
           "A candidate title and subtitle, this session's composing. The opening figure's three mirrors and its round of three are among the 120 moves, and no move of the 57th is other.</div>")
ARIA = ("Three views. A sphere with fifteen great circles, three of them in the accent, and one triangle of three right angles. "
        "Beside it that triangle alone, in fifteen small triangles with the numbers 1 to 5, three corners of five on its sides and four corners of three. "
        "And a small sphere with three rectangles at right angles, a rectangle on a great circle of the three.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>")
body = (svg + "\n" + "\n".join(over) + "\n" + title + "\n" + subtitle + "\n" + caption).replace(ACC, DEFAULT_ACCENT)
os.makedirs(WORK, exist_ok=True)
open(os.path.join(WORK, "working_view_one_triangle_fifteen_preview.html"), "w", encoding="utf-8").write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
    f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body + '</div></body></html>')
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "working_view_one_triangle_fifteen_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(body), "bytes;", len([w for w in words if w]), "lines of words")
