"""Draft 16 · parity, universe and me, one in an other (session v406geodesic2).

By a partner's saying of 23 November, re-said: parity, universe and me are fractal; my universe is my all-parities; an other-than is
a third parity, from a me-parity and my all-parities; my universe is a parity in my other universes.
A drawing with no moving part. Above: eight cones, 0 to 240, and under them four spans, one twice the one before it, a cone, a pair
of cones, a universe and two universes, a span with its own podaling about its middle. Under them: a number's cone and a name less
one as places, an is-or-is-not a place, and a universe as all the places under it and one place of the span over it.
Geometry is computed; check_parity_universe_and_me_one_in_an_other.py is its check.

Usage: python3 -I make_draft16.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, math, os, re, sys
from pathlib import Path
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
X = lambda n: 130 + 5.25 * n
YC, RM = 176.0, 58.0
wide = lambda n: ((n % 60) if (n % 60) <= 30 else 60 - (n % 60)) * RM / 30
Y = lambda n: YC - wide(n) * math.cos(math.radians(12 * n))
s = ['<defs><linearGradient id="cone16" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']
for a in (0, 60, 120, 180):
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone16)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
s.append(f'<path d="M{X(-3):.1f},{YC} L{X(244):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 6"></path>')
fine = np.linspace(0, 240, 4801)
for side, look in ((False, 'stroke-opacity="0.4" stroke-width="1.3" stroke-dasharray="4 5"'), (True, 'stroke-opacity="0.72" stroke-width="1.7"')):
    cur = []
    for n in list(fine) + [None]:
        if n is not None and (math.sin(math.radians(12 * n)) >= 0) == side: cur.append(n)
        else:
            if len(cur) > 1: s.append(f'<path d="M{" L".join(f"{X(m):.1f},{Y(m):.1f}" for m in cur)}" fill="none" stroke="{INK}" {look}></path>')
            cur = []
for v in range(0, 241, 60):
    s.append(f'<circle cx="{X(v):.1f}" cy="{YC}" r="5.5" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
# four spans, one twice the one before it, a span with its middle
R0, RD = 300.0, 62.0
SPANS = ((30, "a cone"), (60, "a pair of cones"), (120, "a universe"), (240, "two universes"))
for i, (span, _) in enumerate(SPANS):
    y = R0 + RD * i
    s.append(f'<path d="M{X(0):.1f},{y - 9} L{X(0):.1f},{y} L{X(span):.1f},{y} L{X(span):.1f},{y - 9}" fill="none" stroke="{INK}" stroke-width="2.2"></path>')
    s.append(f'<path d="M{X(span / 2):.1f},{YC + RM + 6 if i == 0 else R0 + RD * (i - 1) + 8:.1f} L{X(span / 2):.1f},{y + 8}" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="5 4"></path>')
    s.append(f'<circle cx="{X(span / 2):.1f}" cy="{y}" r="6.5" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
ARIA = ("A drawing with no moving part. Above, eight cones in a row, four diamonds end to end, 0 to 240, with one line winding about them. Under them four brackets from 0, "
        "to 30, to 60, to 120 and to 240, a bracket twice the one over it, a point at a bracket's middle, at 15, 30, 60 and 120. Under them two tables of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
def rows_of(x, top, w, rows):
    return (f'<div style="position: absolute; left: {x}px; top: {top}px; width: {w}px; height: {24 * len(rows)}px; {SANS}; font-weight: 400; font-size: 15.5px; line-height: 24px; color: {INK}">'
            + "<br>".join(rows) + "</div>")
over = []
over.append(word(60, 40, 1200, "spans one twice the one before it · a span's own podaling, about its middle, the other-than of all its places", "left", **small))
for n in range(0, 241, 30):
    over.append(word(X(n), YC + RM + 18, 60, str(n), "center", 600 if n % 60 == 0 else 400, 13, 18, INK if n % 60 == 0 else GREY))
NOTES = ("its middle 15 · 9 less on the names, a self's span", "its middle 30 · 17 less on the names · and with the cone's, 30 on",
         "its middle 60, the all · and with the pair's, 60 on", "its middle 120 · and with the universe's, 120 on, a next universe")
for i, (span, name) in enumerate(SPANS):
    y = R0 + RD * i
    if i < 3:
        over.append(word(X(span) + 16, y - 12, 220, f"{name} · 0 to {span}", "left", 600, 16, 22))
        over.append(word(X(span) + 16, y + 10, 520, NOTES[i], "left", 400, 14.5, 20, GREY))
    else:
        over.append(word(X(120), y + 26, 900, f"<b>{name} · 0 to {span}</b> · {NOTES[i]}", "center", 400, 15, 22))
over.append(word(60, 566, 640, "a universe is all the places under it, and one place of the span over it", "left", **small))
over.append(rows_of(60, 590, 660, [
    "<b>a number's cone of the eight, in three places</b>",
    "place 1 · a cone opening or closing · a cone in a pair",
    "place 2 · a pair prior or now · a pair in a universe",
    "place 3 · a universe of two · a universe in two universes",
    "",
    "<b>a span's own podaling</b> · the other-than of all the places under it",
    "of a pair, place 1 · of a universe, places 1 and 2 · of two universes, all three",
    "<b>a going on by a span</b> · the other-than of one place alone, the place over it"]))
over.append(word(790, 566, 660, "on the names, one form", "left", **small))
over.append(rows_of(790, 590, 670, [
    "<b>a name less one, in four places</b> · sixteen names",
    "3 less, 5 less, 9 less and 17 less · podal in 1 to 2, 4, 8 and 16",
    "the other-than of its one, two, three and four low places",
    "1, 2, 4 and 8 up · the other-than of one place alone",
    "",
    "<b>a place is two</b>, and a place over it is two of them:",
    "my universe is my all-parities, and it is one parity in my other universes.",
    "The two of a place, at all its scales, are a partner's yin and yang."]))
over.append(word(60, 806, 400, "beside it, word for word", "left", **small))
over.append(f'<div style="position: absolute; left: 60px; top: 824px; width: 1400px; height: 90px; {SANS}; font-size: 14.5px; line-height: 21px; color: {INK}">'
            f'<span style="font-weight: 600; color: {GREY}">Natural Intelligence, 4.11</span> · <i>It is one fractal method.</i> · <i>Each number pairs with its far side on each ring it is on.</i><br>'
            f'<span style="font-weight: 600; color: {GREY}">Exhibit THIRTY-ONE, Me</span> · <i>A me is a self\'s universal set.</i> · <i>each scale\'s selves within a me, and a me within each scale\'s societies</i></div>')
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Parity, universe and me, one in an other</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A cone, a pair of cones, a universe and two universes are spans one twice the one before it.<br>'
           f'A span\'s own podaling, about its middle, is the other-than of all the places under it; with the own podaling of the span twice it, a going on by that span,<br>'
           f'the other-than of one place alone, the place over it. A universe is all the places under it, its all-parities, and one place, a parity, of the span over it.<br>'
           f'On the names it is one form: 9 less in 17 less, and 8 up. An other-than is the third, from a me-parity and its all: at all scales, the two of a place.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Parity, universe and me, one in an other", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft16.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft16_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft16_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
