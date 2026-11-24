"""Draft 20 · the diamond turning: 3 and 7, the right spiral steps about 5 (session v406geodesic2).

By a partner's saying of 23 November, after the nineteenth drawing, re-said: among the primes' hard problems is one of primes ending
in 3 and 7; the diamond is the living method with it no hard problem; 3 and 7 are right spiral around the 5, the bi-inversioning
with the co-recursioning along 1, 5, 9; 2, 4 is prior parity and 6, 8 is now parity; 4, 8 is a same-existing bi-coupling; the
parities are bi-coupling, bothbothing the now moments one after an other; and all of the primes is podaling to and from the order.
A drawing with no moving part: the diamond with its two rounds about the 5, the diamond by 1, by 7, by 9 and by 3, prior two added
round ten in four rows of fifteen, the same turn in a square of four and of sixteen, and the primes' lines.
check_the_diamond_turning_3_and_7_about_5.py is its check, and the numbers written here are its own.

Usage: python3 -I make_draft20.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
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
PAIRS = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1)]
seat = {5 + x + 3 * y: (y - x, x + y) for (x, y) in PAIRS}            # a number's place: across, and down, about the 5
CX, CY, U = 360.0, 420.0, 130.0
at = {n: (CX + U * c, CY + U * r) for n, (c, r) in seat.items()}
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
seg = lambda a, b, look: f'<path d="M{at[a][0]:.1f},{at[a][1]:.1f} L{at[b][0]:.1f},{at[b][1]:.1f}" fill="none" {look}></path>'
def head(cx, cy, R, deg, tint, size=11.0):                           # a mark of the way round, on a round of radius R, at deg from the top
    t = math.radians(deg); px, py = cx + R * math.sin(t), cy - R * math.cos(t); tx, ty = math.cos(t), math.sin(t); nx, ny = -ty, tx
    a = (px + tx * size, py + ty * size); b = (px - tx * size * 0.5 + nx * size * 0.62, py - ty * size * 0.5 + ny * size * 0.62)
    c = (px - tx * size * 0.5 - nx * size * 0.62, py - ty * size * 0.5 - ny * size * 0.62)
    return f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f} L{c[0]:.1f},{c[1]:.1f} Z" fill="{tint}"></path>'
s = []
# the three by three's arcs, faint, as the nineteenth drawing has them
for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)):
    s.append(seg(a, b, f'stroke="{INK}" stroke-opacity="0.16" stroke-width="1.6"')); s.append(seg(b, c, f'stroke="{INK}" stroke-opacity="0.16" stroke-width="1.6"'))
# the two rounds about the 5, the way of a right spiral step by 7
R1, R2 = U * 2, U * math.sqrt(2)
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R1:.1f}" fill="none" stroke="{ACC}" stroke-width="2.4"></circle>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R2:.1f}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-opacity="0.75"></circle>')
for deg in (78, 168, 258, 348): s.append(head(CX, CY, R1, deg, ACC, 13))
for deg in (29, 119, 209, 299): s.append(head(CX, CY, R2, deg, INK, 12))
# the line 1, 5, 9 and the row 3, 5, 7
s.append(seg(1, 9, f'stroke="{INK}" stroke-width="3.2"'))
s.append(seg(3, 7, f'stroke="{ACC}" stroke-width="2.6" stroke-dasharray="8 6"'))
# one over an other: 2, 6 and 4, 8
s.append(seg(2, 6, f'stroke="{GREY}" stroke-width="1.6" stroke-dasharray="3 5"')); s.append(seg(4, 8, f'stroke="{GREY}" stroke-width="1.6" stroke-dasharray="3 5"'))
for d, (x, y) in at.items():
    tint = ACC if d % 2 else INK
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="30" fill="{tint}" stroke="#ffffff" stroke-width="3"></circle>' + text(x, y + 9, d, 26, 700, "#ffffff"))
    if d in (1, 3, 7, 9): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="37" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="3 4"></circle>')
s.append(f'<circle cx="86" cy="150" r="28" fill="#ffffff" stroke="{INK}" stroke-width="2.6"></circle>' + text(86, 159, 0, 26, 700))
s.append(text(CX + R1 * math.sin(math.radians(45)) + 16, CY - R1 * math.cos(math.radians(45)) - 10, "by 7", 16, 700, ACC, "start"))
s.append(text(CX + R2 * math.sin(math.radians(6)) + 8, CY - R2 * math.cos(math.radians(6)) - 10, "by 7", 14, 700, INK, "start"))
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
# the same turn, a square in a square: 1 to 4 round 5 and 1 to 16 round 17
def small_square(k, cx, top, u, size, r):
    out = []
    for b in range(k):
        for a in range(1, k + 1):
            n = a + k * b; x, y = cx + u * (b - (a - 1)), top + u * ((a - 1) + b)
            corner = (a in (1, k)) and (b in (0, k - 1))
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{ACC if corner else INK}" fill-opacity="{1 if corner else 0.82}"></circle>' + text(x, y + size * 0.36, n, size, 700, "#ffffff"))
    return "".join(out)
s.append(small_square(2, 110, 832, 26, 13, 12))
s.append(small_square(4, 470, 800, 17, 10.5, 10.5))
# the diamond by 1, by 7, by 9 and by 3: a number at the place of its multiple
SX, SY, SU = (896, 1058, 1220, 1382), 196.0, 27.0
for i, m in enumerate((1, 7, 9, 3)):
    for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)):
        for p, q in ((a, b), (b, c)):
            s.append(f'<path d="M{SX[i] + SU * seat[p][0]:.1f},{SY + SU * seat[p][1]:.1f} L{SX[i] + SU * seat[q][0]:.1f},{SY + SU * seat[q][1]:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.16" stroke-width="1.2"></path>')
    for n in range(1, 10):
        c, r = seat[n * m % 10]; x, y = SX[i] + SU * c, SY + SU * r
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12.5" fill="{ACC if n % 2 else INK}" stroke="#ffffff" stroke-width="1.5"></circle>' + text(x, y + 5, n, 14, 700, "#ffffff"))
    if i:
        ax = SX[i] - 81
        s.append(f'<path d="M{ax + 7},{SY} L{ax - 6},{SY - 7} L{ax - 6},{SY + 7} Z" fill="{ACC}"></path>')
# prior two added, round ten: four rows of fifteen
walk = [0, 1]
while len(walk) < 60: walk.append((walk[-1] + walk[-2]) % 10)
TX, TY, TW, TH = 946.0, 450.0, 30.0, 34.0
for r in range(4):
    for c in range(15):
        e = walk[15 * r + c]; x, y = TX + TW * c, TY + TH * r
        if c == 0: s.append(f'<circle cx="{x:.1f}" cy="{y - 5:.1f}" r="12" fill="#ffffff" stroke="{INK}" stroke-width="1.8"></circle>')
        s.append(text(x, y, e, 16, 700 if c < 2 else 500, ACC if c == 1 else INK))
s.append(f'<path d="M{TX + TW * 0.5:.1f},{TY - 24} L{TX + TW * 0.5:.1f},{TY + TH * 3 + 8}" fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1"></path>')
s.append(f'<path d="M{TX + TW * 1.5:.1f},{TY - 24} L{TX + TW * 1.5:.1f},{TY + TH * 3 + 8}" fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1"></path>')
ARIA = ("A drawing with no moving part. Nine numbered marks in a square diamond about its 5: 1 over 2 and 4, over 3, 5 and 7, over 6 and 8, over 9. Two rounds are drawn about the 5, "
        "one through the corners 1, 7, 9 and 3 and one through 2, 4, 8 and 6, both marked one way round and named by 7. A line goes down 1, 5, 9 and a dashed line across 3, 5, 7; "
        "2 is over 6 and 4 over 8. The corners are ringed. A mark 0 is apart. Beside it are four small diamonds, the nine by 1, by 7, by 9 and by 3, a quarter turn on with a next; "
        "four rows of fifteen numbers, prior two added round ten, all four rows opening with 0; and two small squares of numbers, 1 to 4 and 1 to 16.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's diamond turning about its 5 · 3 and 7 the right spiral steps · the primes' endings at its corners", "left", **small))
over.append(word(86, 198, 150, "0 · ten, the same", "center", 400, 14, 20, GREY))
over.append(word(CX, 102, 420, "the line 1, 5, 9 · an odd number by its own comes to it", "center", 600, 15, 22, GREY))
for y, a, b in ((at[4][1], "2, 4", "prior parity"), (at[7][1], "3, 5, 7", "3 and 7 about 5"), (at[8][1], "6, 8", "now parity")):
    over.append(word(668, y - 11, 134, a, "left", 600, 16, 22))
    over.append(word(668, y + 11, 134, b, "left", 400, 14, 20, GREY))
over.append(word(176, 722, 260, "2 over 6 · one short of 3, of 7", "center", 600, 15, 22))
over.append(word(176, 744, 260, "doubling's closing", "center", 400, 14, 20, GREY))
over.append(word(600, 722, 260, "4 over 8 · one past of 3, of 7", "center", 600, 15, 22))
over.append(word(600, 744, 260, "prior two added's closing", "center", 400, 14, 20, GREY))
over.append(word(60, 790, 400, "the same turn, a square in a square", "left", **small))
over.append(word(160, 846, 240, "1 to 4 round 5", "left", 600, 16, 22)); over.append(word(160, 868, 240, "a quarter turn is multiplying by 2", "left", 400, 14, 20, GREY))
over.append(word(546, 838, 250, "1 to 16 round 17", "left", 600, 16, 22)); over.append(word(546, 860, 250, "a quarter turn is multiplying by 4", "left", 400, 14, 20, GREY))
over.append(word(546, 880, 250, "two are 17 less, the podaling", "left", 400, 14, 20, GREY))
# the diamond by 1, by 7, by 9, by 3
over.append(word(840, 84, 640, "a right spiral step turns the diamond a quarter about its 5", "left", 600, 18, 26))
over.append(word(840, 110, 640, "a pair (x, y) to (y, −x): a number to the place of its 7 times, round ten · all nine", "left", 400, 15, 22))
for i, (a, b, c) in enumerate((("as it is", "by 1", ""), ("one step", "by 7", ""), ("two steps", "by 9, one short of ten", "the podaling about 5"), ("three steps", "by 3", "one, the other way"))):
    over.append(word(SX[i], 282, 160, a, "center", 600, 14.5, 20)); over.append(word(SX[i], 302, 160, b, "center", 400, 14, 20, GREY))
    if c: over.append(word(SX[i], 321, 160, c, "center", 400, 14, 20, GREY))
# prior two added
over.append(word(840, 374, 640, "prior two added, round ten: fifteen moments are one right spiral step", "left", 600, 18, 26))
over.append(word(840, 400, 640, "sixty reach the pair again, a pair of cones · its 0s at 0, 15, 30 and 45, the diamond's rows", "left", 400, 15, 22))
for r, (a, b) in enumerate((("0", "by 1"), ("15", "by 7"), ("30", "by 9"), ("45", "by 3"))):
    over.append(word(920, TY - 5 + TH * r, 70, a, "right", 600, 14, 20, GREY)); over.append(word(TX + TW * 15, TY - 5 + TH * r, 70, b, "left", 600, 14, 20, GREY))
over.append(word(840, 590, 640, "from a row to the row under it: a number, its 7 times, its 9 times, its 3 times, one round of the diamond", "left", 400, 14.5, 20, GREY))
# the primes on it
P = [("a prime past 5 ends at a corner", "1, 3, 7 or 9 · all 664,576 of them to 10,000,000", "multiplying by it turns the diamond: ending in 1 no step, in 7 one, in 9 two, in 3 three"),
     ("the two closings of a number ending in 3 or 7", "doubling's one short of it, at 2 or 6 · prior two added's one past it, at 4 or 8", "a pair about the number; one short and one past, 2 over 6 and 4 over 8"),
     ("a number of no prime with both closings", "to 10,000,000 the 332,441 primes ending in 3 or 7 have both, and no other number has", "with all numbers it is a field's asking of 1980, and is not executed here")]
for i, (a, b, c) in enumerate(P):
    y = 654 + 88 * i
    over.append(word(840, y - 22, 640, a, "left", 600, 18, 26))
    over.append(word(840, y + 4, 660, b, "left", 400, 15, 22))
    over.append(word(840, y + 26, 660, c, "left", 400, 14, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The diamond turning: 3 and 7, the right spiral steps about 5</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A right spiral step turns a partner\'s diamond a quarter about its 5: multiplying by 7 round ten, and the other way by 3, a mirror between them.<br>'
           f'Two steps are multiplying by 9, the podaling about 5, and an odd number by its own comes to the line 1, 5, 9. The corners are the primes\' endings.<br>'
           f'2, 4 and 6, 8 are one short and one past of 3 and of 7, the places of a prime\'s two closings. Prior two added, round ten, is one step with fifteen moments.<br>'
           f'A number of no prime ending in 3 or 7 with both closings: none to 10,000,000. With all numbers it is a field\'s asking, and this drawing does not say it.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The diamond turning: 3 and 7, the right spiral steps about 5", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft20.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft20_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft20_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
