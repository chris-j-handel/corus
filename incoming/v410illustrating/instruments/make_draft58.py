"""v410illustrating · the maker of the 58th drawing: One Triangle, Three Golden Rectangles.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft58.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

A drawing beside the 57th, by a partner's is of 27 November: a me-parity, five, a stable-forming surface, outward on
the sphere opening to a torus, is the three golden rectangles' five. It gathers no drawing of the 56: none draws it.
Its check is opened and executed here, and no drawing is made with an is-not.

Its placings, no execution says them: its four parts and its table side by side; a tint and a number, 1 to 5, for a
three of the fifteen; a filled mark for a corner of five and an open mark for a corner of three; the names across at a
rectangle's across and the names along at its along; a strip for nought to sixty.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_58", os.path.join(HERE, "check_one_triangle_three_golden_rectangles.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
f = c.f

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"

W, H = 1520, 1150
GREY, SLATE = "#4a5160", "#475569"
SANS = "font-family: Inter, system-ui, sans-serif"
A, B, C = c.A, c.B, c.C
PHI, RECT, G, P0, INSIDE = c.PHI, c.RECT, c.G, c.P0, c.INSIDE
s, over = [], []

def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def vname(cx, cy, t, size=24):
    return (f'<div style="position: absolute; left: {cx - 20:.0f}px; top: {cy - 16:.0f}px; width: 40px; height: 32px; line-height: 32px; text-align: center; '
            f"font-family: 'STIX Two Text', Georgia, serif; font-style: italic; font-weight: 500; font-size: {size}px; color: {INK}\">{t}</div>")
def ball(cam, key):
    R = cam.s
    return (f'<radialGradient id="ball58{key}" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop></radialGradient>')
k3 = lambda v: tuple(np.round(v, 5) + 0.0)
three_of, n_ = {}, 0                                    # a small triangle's three, 1 to 5, by the one triangle's own round of three
for g in sorted(INSIDE, key=lambda g: -float((g @ P0) @ f.V3)):
    if k3(g @ P0) in three_of: continue
    n_ += 1
    for j in range(3): three_of[k3(np.linalg.matrix_power(f.ROUND3, j) @ g @ P0)] = n_
normals = own["normals"]; own3 = [i for i, nn in enumerate(normals) if max(abs(nn)) > 0.999]
corners = [f.unit(x) for r in RECT for x in r]
threes_all = {k3(g @ f.V3): g @ f.V3 for g in G}
on_it = lambda v: bool(np.all(v > -1e-9))
fives_on, threes_on = [v for v in corners if on_it(v)], [v for v in threes_all.values() if on_it(v)]
assert n_ == 5 and len(own3) == 3 and len(fives_on) == 3 and len(threes_on) == 4

camA = Cam(az_deg=28, el_deg=22, cx=250, cy=432, scale=172)              # three golden rectangles on three mirrors
camB = Cam(az_deg=45, el_deg=35.2644, cx=724, cy=468, scale=250)         # the one triangle, along the line of the three alike
camC = Cam(az_deg=45, el_deg=33, cx=150, cy=832, scale=80)               # twelve corners closing as a sphere, as the 57th's camera
s.append("<defs>" + ball(camA, "a") + ball(camC, "c") + "</defs>")

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1400, "58 · beside the 57th, on the one triangle's own sphere · it gathers no drawing of the 56: none draws it · its prior: the 57th, the opening figure · "
                 "its next figures: a cube's shells, and cones of 30 on the co-linear", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 820, "Three golden rectangles at right angles are on the one triangle's three mirrors.", size=20, h=28))
over.append(word(60, 108, 820, "Their twelve corners close as a sphere, five triangles to a corner, sixty three ways.", size=20, h=28))
over.append(word(60, 138, 820, "The one triangle of three right angles is fifteen of that sphere's 120.", size=20, h=28))
over.append(word(900, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit THIRTY · stable-forming at numbers: 24 an apex, five names to a surface, 59; three golden rectangles",
                       "Natural Naming · bi-tri-volutioning, stable-forming across 1 to 17: across, along, and both",
                       "Natural Mathematics, Natural Numbers · sixty moves as 24 and 36; seventeen primes, 2 to 59",
                       "Natural Illustrating · for its part of a pentagon, rectangles and the twelve corners' form")):
    over.append(word(900, 92 + 18 * i, 600, t, size=11.8, h=16, color=GREY))

# ================= 1 · three golden rectangles, a rectangle a mirror =================
cam = camA; R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball58a)" fill-opacity="0.75"></circle>')
for i in own3:
    pts = great_circle(normals[i], 721); fr, bk = runs(pts, [vis(p) for p in pts])
    s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.4" stroke-width="1.1" stroke-dasharray="3 4">{paths([cam.path(r) for r in bk])}</g>')
    s.append(f'<g fill="none" stroke="{ACC}" stroke-width="2.2" stroke-linecap="round">{paths([cam.path(r) for r in fr])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.5"></circle>')
for r in sorted(RECT, key=lambda r: min(cam.depth(f.unit(x)) for x in r)):
    ring = [f.unit(x) for x in r]
    s.append(f'<path d="{cam.path(ring, True)}" fill="{SLATE}" fill-opacity="0.11" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"></path>')
for v in corners:
    x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.6" fill="{INK}" stroke="#ffffff" stroke-width="1.5"></circle>')
for V, t, dx, dy in ((A, "A", 0, -24), (B, "B", -20, 12), (C, "C", 22, 8)):
    x, y = cam.proj(V); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{ACC}" stroke="#ffffff" stroke-width="1.8"></circle>'); over.append(vname(x + dx, y + dy, t, 22))
r1 = [f.unit(x) for x in RECT[0]]                                         # the rectangle on the mirror through A and C
xa, ya = cam.proj((r1[0] + r1[3]) / 2); xb, yb = cam.proj((r1[0] + r1[1]) / 2)
over.append(word(xa, ya + 13, 80, "across, 2", "center", 600, 11.5, 14)); over.append(word(xb + 8, yb - 4, 80, "along, 2φ", "left", 600, 11.5, 14))
over.append(word(60, 196, 420, "1 · three golden rectangles, a rectangle a mirror", weight=600, size=15))
over.append(word(60, 220, 420, "the one triangle's three mirrors in the accent · ● a corner of five", size=12.5, color=GREY))
for i, t in enumerate(("● a rectangle is 2 across and 2φ along, on a mirror of the three",
                       "● its along sides go through its next, at the middle of that one's across",
                       "● the one triangle's round of three lays a rectangle onto its next",
                       "● with φ alone its nearest corners are 2 from its next's: its own across")):
    over.append(word(60, 632 + 21 * i, 430, t, size=12.2))

# ================= 2 · the one triangle of three right angles, fifteen =================
cam = camB
edges = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
TINT = {1: (ACC, 0.34), 2: (SLATE, 0.26), 3: (ACC, 0.14), 4: (SLATE, 0.10), 5: ("#f1f5f9", 1.0)}
for g in INSIDE:
    p, q, r = g @ f.V5, g @ f.V3, g @ f.V2; t = three_of[k3(g @ P0)]; col, op = TINT[t]
    ring = np.concatenate([slerp(p, q, 24), slerp(q, r, 24)[1:], slerp(r, p, 24)[1:]])
    s.append(f'<path d="{cam.path(ring, True)}" fill="{col}" fill-opacity="{op}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"></path>')
    x, y = cam.proj(f.unit(p + q + r)); over.append(word(x, y, 20, str(t), align="center", size=11.5, weight=600))
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')
for v in threes_on:
    x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.6" fill="#ffffff" stroke="{INK}" stroke-width="1.8"></circle>')
for v in fives_on:
    x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.6" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>')
for V in (A, B, C):
    x, y = cam.proj(V); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
ax, ay = cam.proj(A); bx, by = cam.proj(B); cx_, cy_ = cam.proj(C)
over.append(vname(ax - 4, ay - 24, "A")); over.append(word(ax + 12, ay - 24, 70, "the me", size=13, weight=600))
over.append(vname(bx - 24, by + 8, "B")); over.append(vname(cx_ + 24, cy_ + 8, "C"))
cut = own["cut"]; five_AC, three_AC = f.unit((0, 1, PHI)), f.unit((0, PHI, 1 / PHI))      # the side from A to C, on the mirror of the rectangle drawn with its across and along
for (p, q), t in (((A, five_AC), f"{cut[0]:.1f}"), ((five_AC, three_AC), f"{cut[1]:.1f}"), ((three_AC, C), f"{cut[2]:.1f}")):
    x, y = cam.proj(1.075 * f.unit(p + q)); over.append(word(x + 4, y, 40, t, size=11, h=14, color=GREY))
over.append(word(520, 196, 440, "2 · the one triangle of three right angles, fifteen", weight=600, size=15))
over.append(word(520, 220, 460, "● a corner of five, a rectangle's corner on a side · ○ a corner of three", size=12.5, color=GREY))
for i, t in enumerate(("● a small triangle is of 36, 60 and 90: 6 over 180; 120 of them are 720",
                       "● the one triangle is fifteen: five threes, 1 to 5, by its round of three",
                       "● a side from a corner: 31.7 to its corner of five, 37.4, and 20.9",
                       "● fifteen mirrors are five threes: the 57th's figure is on this sphere five ways")):
    over.append(word(520, 632 + 21 * i, 450, t, size=12.2))

# ================= the table: a name a row, its prime by its position =================
TX, TY0, RH = 1016, 232, 19
cols = [("n", 0, 22, "right"), ("its name, Exhibit ONE's own", 32, 178, "left"), ("its prime", 212, 50, "right"), ("across, along", 282, 100, "left"), ("of the five", 392, 70, "left")]
over.append(word(TX, 196, 490, "a name a row · its prime by its position · across and along", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.6, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 470},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
prime_of, names = own["prime_of"], own["names"]
def lay_of(n): return "across" if n in c.ACROSS else "along" if n in c.ALONG else "across and along" if n in c.BOTH else ""
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="478" height="{RH:.1f}" fill="#eef0f5"></rect>')
    cells = [str(n), names[n], str(prime_of[n]), lay_of(n), "● to 59" if n in c.FIVE_NAMES else ("a surface" if n == 17 else "")]
    for (t, x, w_, al), v in zip(cols, cells):
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if t in ("n", "its name, Exhibit ONE's own") or (n == 12 and t == "its prime") else 400, 11.4, 16,
                         extra="font-variant-numeric: tabular-nums;"))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 470},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its prime by its position: the one table of the seventeen names, 2 to 59",
                       "across, possibling; along, discovering and existing; 12, both: the surface, with 37",
                       "of the five: five names before 10, their primes 5, 7, 11, 17 and 19 adding to 59")):
    over.append(word(TX, yb + 3 + 16 * i, 490, t, size=10.6, h=14, color=GREY))
over.append(word(TX, yb + 58, 100, "Exhibit THIRTY:", weight=600, size=11.4))
over.append(word(TX + 98, yb + 58, 400, "506, 507 and 509 · 512 to 518 · its numbered sentences beside the parts", size=11.2, color=GREY))

# ================= 3 · twelve corners closing as a sphere =================
cam = camC; R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball58c)"></circle>')
pairs = [(i, j) for i in range(12) for j in range(i + 1, 12) if abs(np.linalg.norm(np.array(sum(RECT, [])[i], float) - np.array(sum(RECT, [])[j], float)) - 2) < 1e-9]
for i, j in pairs:
    pts = slerp(corners[i], corners[j], 40); fr, bk = runs(pts, [vis(p) for p in pts])
    s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="0.9" stroke-dasharray="3 4">{paths([cam.path(r) for r in bk])}</g>')
    s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.3" stroke-linecap="round">{paths([cam.path(r) for r in fr])}</g>')
s.append(f'<path d="{cam.path(np.concatenate([edges[0], edges[1][1:], edges[2][1:]]), True)}" fill="{ACC}" fill-opacity="0.2" stroke="{ACC}" stroke-width="2" stroke-linejoin="round"></path>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.4"></circle>')
for v in corners:
    if vis(v):
        x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" fill="{INK}" stroke="#ffffff" stroke-width="1.3"></circle>')
over.append(word(60, 736, 420, "3 · twelve corners closing as a sphere", weight=600, size=15))
for i, t in enumerate(("● 30 sides, 20 triangles, five to a corner",
                       "● 12 by 5, 20 by 3, 30 by 2: sixty",
                       "● sixty moves: 24 by fifths, 36 others",
                       "● four triangles of three about one line",
                       "● a round of five is golden, 1.618",
                       "● closing as a sphere, and winding through",
                       "   one opening as a torus: one, then the other")):
    over.append(word(256, 764 + 20 * i, 270, t, size=11.8, h=16))

# ================= 4 · nought to sixty, seventeen primes =================
SX, SY, U = 566, 818, 6.5
over.append(word(552, 736, 420, "4 · nought to sixty: 24 and 36, seventeen primes", weight=600, size=15))
s.append(f'<path d="M{SX},{SY} L{SX + 60 * U},{SY}" fill="none" stroke="{INK}" stroke-width="1.4"></path>')
for k in range(0, 61):
    h_ = 7 if k % 10 == 0 else 3.5
    s.append(f'<path d="M{SX + k * U:.1f},{SY - h_} L{SX + k * U:.1f},{SY + h_}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1"></path>')
for k in (0, 10, 20, 30, 40, 50, 60):
    over.append(word(SX + k * U, SY + 20, 30, str(k), "center", size=10.5, h=14, color=GREY))
s.append(f'<path d="M{SX + 24 * U:.1f},{SY - 34} L{SX + 24 * U:.1f},{SY + 10}" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-linecap="round"></path>')
over.append(word(SX + 24 * U, SY - 44, 120, "24, an apex", "center", 600, 11.5, 14, ACC))
for p in own["behind"] + own["ahead"]:
    ring = p in (5, 7, 11, 17, 19)
    s.append(f'<circle cx="{SX + p * U:.1f}" cy="{SY}" r="{4.6 if ring else 3.6}" fill="{INK}" stroke="{ACC if ring else "#ffffff"}" stroke-width="{2 if ring else 1.2}"></circle>')
for p, t, dx in ((23, "23", -9), (25, "25", 9), (37, "37", 0), (59, "59, a surface", -26)):
    over.append(word(SX + p * U + dx, SY - 16, 90, t, "center", 600 if p in (37, 59) else 400, 10.8, 14, INK if p != 25 else GREY))
s.append(f'<circle cx="{SX + 25 * U:.1f}" cy="{SY}" r="3.4" fill="#ffffff" stroke="{INK}" stroke-width="1.2"></circle>')
over.append(word(SX + 12 * U, SY + 40, 170, "24 behind it: nine primes", "center", size=11.5, h=14))
over.append(word(SX + 42 * U, SY + 40, 250, "36 ahead of it: eight primes", "center", size=11.5, h=14))
for i, t in enumerate(("● a prime · ringed: the five names' primes, 5, 7, 11, 17 and 19, adding to 59",
                       "○ 25, five fives, beside 24 with 23 · 37, the 12th name's prime")):
    over.append(word(552, SY + 64 + 18 * i, 430, t, size=11.2, h=15, color=GREY))

# ================= found, and what this drawing leaves =================
FX, FY = 1016, 652
over.append(word(FX, FY, 480, "found, and what this drawing leaves", weight=600, size=15))
FOUND = [("the round of five is given", ["24 of the 120 moves are the 57th's own; the round of five is none of them. Its number", "is φ, no whole number: no move of the 57th makes it"]),
         ("a line of fives, said two ways in Exhibit THIRTY", ["its 509 is with its own unsure: five names before 10, or fives going up. The five", "names add to 59; 25, 35, 45 and 55 add to 160. Both are laid"]),
         ("a corner, the middle and a face's middle on one line", ["its 508's own unsure: across the middle from a corner of the twelve is a corner;", "in a form of four corners it is a face's middle"]),
         ("sphere and torus, one and then the other", ["a torus's grid about a patch is with rounds of 1, 2, 3, 4 and 6: the five is outward,", "on a sphere. The 57th's torus of sixteen patches and this sphere are not one drawing yet"]),
         ("a partner's saying of what this form is, not executed here", ["the stable form between of an atom's surface, from the fracturing of an exhausting", "stable form: societies of atom mes bi-tunneling, at all-parity and light's rate"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 470, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 480, t, size=11, h=14, color=GREY))
    y += 47

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">One Triangle, Three Golden Rectangles</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Bi-Tri-Volutioning a Round of Five, Twelve Corners Closing as a Sphere</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "Three golden rectangles at right angles are on the one triangle's three mirrors, a rectangle a mirror, and its round of three lays a rectangle onto its next.<br>"
           "Their twelve corners close as a sphere, five triangles to a corner. The one triangle of three right angles is fifteen of its 120, a rectangle's corner on a side.<br>"
           "Nought to sixty is 24 and 36, as its sixty moves are, with seventeen primes, 2 to 59. Five names before 10 are with primes adding to 59, a surface.<br>"
           "The round of five is given, and golden. A candidate, by a partner's is, beside the 57th drawing and writing in none.</div>")
ARIA = ("Four parts and a table. A sphere with three rectangles at right angles, a rectangle on a great circle of three. One triangle of three right angles in fifteen small triangles, "
        "with the numbers 1 to 5. A sphere with twelve corners, thirty sides and twenty triangles. A strip from nought to sixty with seventeen primes marked. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("One Triangle, Three Golden Rectangles", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft58.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft58_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft58_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
