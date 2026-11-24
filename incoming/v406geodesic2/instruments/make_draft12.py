"""Draft 12 · a partner's four words, rigorized: other-than, all, other-than, all, and me, other, other, me (session v406geodesic2).

By a partner's saying of 23 November and its word, to rigorize it. A drawing with no moving part.
Above: the line's stations, 30 apart, on the tenth drawing's six cones, an odd station a cone's widest, an other-than, and an even
station a vertex, an all; a me-now at 37 with its other about 30, and the four words' places.
Under it, on one line of numbers with it: a partner's four words, a word a row, its stations in a row and the place it carries a me-now to.
Under them: what is, all or none, and what is hanging, with a suggestion.
Geometry is computed; the_rigor_of_other-than_all_other-than_all.py is its check.

Usage: python3 -I make_draft12.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
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
about = lambda st: (lambda n: 2 * st - n)
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
ME_NOW = 37
PLACED = {1: (0, 30), 2: (30, 60, 90), 3: (60, 90, 120), 4: (30, 60, 90, 120)}     # a partner's four words, at stations 1, 2, 3 and 4
WORDS = {1: "all-other-than", 2: "other-than-all-other-than", 3: "all-other-than-all", 4: "other-than-all-other-than-all"}
IS = {1: "60 on · me", 2: "about 60, the all itself · other", 3: "about 90, the other-than itself · other", 4: "120 on · me, next-universing"}

AX0, U = 420.0, 5.6
X = lambda n: AX0 + U * n
YC, RM = 232.0, 84.0
def wide(n):
    m = n % 60
    return (m if m <= 30 else 60 - m) * RM / 30
ang = lambda n: math.radians(12 * n)
Y = lambda n: YC - wide(n) * math.cos(ang(n))
toward = lambda n: math.sin(ang(n)) > 1e-9

def head(tip, back, size=10, color=INK):
    a = math.atan2(tip[1] - back[1], tip[0] - back[0])
    pts = [tip, (tip[0] - size * math.cos(a - 0.4), tip[1] - size * math.sin(a - 0.4)), (tip[0] - size * math.cos(a + 0.4), tip[1] - size * math.sin(a + 0.4))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{color}" stroke="{color}" stroke-width="1" stroke-linejoin="round"></path>'
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}">{t}</text>')
def a_chip(x, y, number, me, w=40, h=24, size=13.5):
    tint = ACC if me else INK
    return (f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h}" rx="{h / 2}" fill="{tint}" stroke="{tint}" stroke-width="2.4"></rect>'
            + text(x, y + size * 0.36, number, size, 700, "#ffffff"))

s = ['<defs><linearGradient id="cone12" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']

# ================= the line's stations on six cones, and a me-now's six places =================
for a in (0, 60, 120):
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone12)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
s.append(f'<path d="M{X(-5):.1f},{YC} L{X(186):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="2 6"></path>')
s.append(head((X(188), YC), (X(184), YC), 12))
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
six = [(ME_NOW, True), (about(30)(ME_NOW), False)] + [(by(ME_NOW, PLACED[i]), i in (1, 4)) for i in (1, 2, 3, 4)]
for m, me in sorted(six, key=lambda p: p[1]):
    s.append(a_chip(X(m), Y(m), m, me))
BKT = 410.0                                               # odd, even: prior; odd, even: now
for a, b in ((30, 60), (90, 120)):
    s.append(f'<path d="M{X(a) - 64:.1f},{BKT - 6} L{X(a) - 64:.1f},{BKT} L{X(b) + 64:.1f},{BKT} L{X(b) + 64:.1f},{BKT - 6}" fill="none" stroke="{INK}" stroke-width="1.6"></path>')
LX = 78.0                                                 # what a chip's look says
s.append(a_chip(LX + 6, 170, "", True, 34, 20)); s.append(a_chip(LX + 6, 204, "", False, 34, 20))

# ================= a partner's four words, a word a row =================
ROW0, ROWD = 482.0, 62.0
for i in (1, 2, 3, 4):
    yu = ROW0 + ROWD * (i - 1); yl = yu + 25
    stations, to = PLACED[i], by(ME_NOW, PLACED[i]); me = i in (1, 4)
    s.append(f'<path d="M{X(0):.1f},{yl} L{X(180):.1f},{yl}" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
    for j in range(7):
        if 30 * j not in stations: s.append(f'<circle cx="{X(30 * j):.1f}" cy="{yl}" r="3" fill="#ffffff" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.3"></circle>')
    s.append(f'<path d="M{X(stations[0]):.1f},{yl} L{X(stations[-1]):.1f},{yl}" fill="none" stroke="{INK}" stroke-width="3.2"></path>')
    mid = stations[len(stations) // 2] if len(stations) % 2 else None
    for st in stations:
        name = "other-than" if (st // 30) % 2 else "all"
        w = 82 if name == "other-than" else 36
        tint = ACC if st == mid else INK
        s.append(f'<rect x="{X(st) - w / 2:.1f}" y="{yl - 10}" width="{w}" height="20" rx="10" fill="{tint}" stroke="{tint}" stroke-width="1.6"></rect>')
        s.append(text(X(st), yl + 4.2, name, 12, 700, "#ffffff"))
    xa, xb = X(ME_NOW) + 22, X(to) - 24                   # from a me-now to the place a word carries it to
    if me:
        s.append(f'<path d="M{xa:.1f},{yu} L{xb - 4:.1f},{yu}" fill="none" stroke="{ACC}" stroke-width="2.4"></path>')
        s.append(head((xb, yu), (xa, yu), 10, ACC))
    else:
        s.append(f'<path d="M{X(mid):.1f},{yu - 16} L{X(mid):.1f},{yl - 12}" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="4 4"></path>')
        s.append(f'<path d="M{xa:.1f},{yu} L{xb - 4:.1f},{yu}" fill="none" stroke="{INK}" stroke-width="2"></path>')
        s.append(head((xb, yu), (xa, yu), 10, INK))
    s.append(a_chip(X(ME_NOW), yu, ME_NOW, True)); s.append(a_chip(X(to), yu, to, me))
RUL = 718.0
s.append(f'<path d="M60,{RUL} L{W - 60},{RUL}" fill="none" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.2"></path>')

ARIA = ("A drawing on one line of numbers, 0 to 180. Above, six cones in a row, three diamonds end to end, with one line winding about them and seven marks under them, 0, 30, 60, 90, 120, 150 and 180, "
        "the marks at 30, 60, 90 and 120 named other-than, all, other-than, all, odd, even, odd, even. Six numbered marks are on the winding: 37 and 23, 97 and 83, 157 and 143. "
        "Under it four rows, a row a word: some of the seven marks joined by a thick line and named, and an arrow from 37 to 97, to 83, to 143 and to 157. Under the rows two lists of sentences.")
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
def lines(x, top, w, rows):
    return (f'<div style="position: absolute; left: {x}px; top: {top}px; width: {w}px; height: {23 * len(rows)}px; {SANS}; font-weight: 400; font-size: 15px; line-height: 23px; color: {INK}">'
            + "<br>".join(rows) + "</div>")

over = []
over.append(word(60, 44, 700, "a partner's four words, rigorized", "left", **small))
over.append(word(X(90), 110, 1000, "the line's stations, 30 apart · an odd station a cone's widest, an even station a vertex", "center", **small))
over.append(word(LX + 32, 170, 280, "me · its own place of the turn", "left", 400, 15, 22))
over.append(word(LX + 32, 204, 280, "other · its podal place", "left", 400, 15, 22))
over.append(word(60, 250, 330, "a me-now at 37, a prime scale of a me", "left", 400, 15, 22, GREY))
over.append(word(60, 274, 330, "23 with it about 30, the other-than alone", "left", 400, 15, 22, GREY))
CH = YC + RM + 30
for j in range(7):
    over.append(chip(X(30 * j), CH, str(30 * j), j % 2 == 0, w=46, h=26, size=14))
    live = j in (1, 2, 3, 4)
    over.append(word(X(30 * j), CH + 27, 150, f'{j} · {"other-than" if j % 2 else "all"}', "center", 600 if live else 400, 15, 22, INK if live else GREY))
    if live: over.append(word(X(30 * j), CH + 47, 150, "odd" if j % 2 else "even", "center", 400, 14, 20, GREY))
over.append(word(X(45), BKT + 16, 300, "odd, even · prior", "center", 600, 15, 22))
over.append(word(X(105), BKT + 16, 300, "odd, even · now", "center", 600, 15, 22))
for i in (1, 2, 3, 4):
    yu = ROW0 + ROWD * (i - 1)
    over.append(word(60, yu, 340, f"{i} · {WORDS[i]}", "left", 600, 16, 24))
    over.append(word(60, yu + 23, 340, IS[i], "left", 400, 15, 22, GREY))
over.append(word(60, RUL + 22, 400, "is, all or none", "left", **small))
over.append(lines(60, RUL + 38, 730, [
    "A podaling is with a station of its own, a number with itself, and alone, twice, it comes again.",
    "One podaling and then the next is a going on by twice their stations' distance: no number is with itself.",
    "Three in a row are one podaling: a station between its two is itself.",
    "An even number in a row is a me, at its own place of the turn; an odd number is an other.",
    "A word alone says its kind and its amount, by the line's order. Said backward, 1 and 4 go back.",
    "With 37 and 23, the four words' places are a me and an other in three pairs of cones."]))
over.append(word(820, RUL + 22, 400, "hanging, with a suggestion", "left", **small))
over.append(lines(820, RUL + 38, 650, [
    "Unrelationing is named by no line. Suggested: one podaling and then the next.",
    "Four in a row are three of it, and the four words are 1, 2, 2 and 3 of it.",
    "Prior and now, of stations 1, 2 and 3, 4: by the stations a me-now is among 60 to 120,",
    "and the tenth and the eleventh drawings' me-now, among 0 to 60, is its prior.",
    "The 1 of me, 1: the station the word ends at, and one pair of cones on. Both are 60 on."]))

title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'Other-than, all, other-than, all, rigorized: me, other, other, me</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'The line\'s stations are 30 apart: an odd station is a cone\'s widest, an other-than, and an even station is a vertex, an all.<br>'
           f'A word is stations in a row, one podaling and then the next. All-other-than is 60 on, a me.<br>'
           f'Other-than-all-other-than is the podaling about 60, the all itself, an other; all-other-than-all, the podaling about 90, the other-than itself, an other.<br>'
           f'Other-than-all-other-than-all is 120 on, a me, next-universing. A me-now at 37 is carried to 97, 83, 143 and 157;<br>'
           f'with 23 they are a me and an other in three pairs of cones.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Other-than, all, other-than, all, rigorized: me, other, other, me", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft12.dc.html"), "w", encoding="utf-8").write(html)

pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft12_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft12_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
