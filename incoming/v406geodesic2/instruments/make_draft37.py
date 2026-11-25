"""Draft 37 · the living parities: a prime is one other-than, and the between goes through (session v406geodesic2).

A partner's word of 24 November, re-said: go on, with no equilibria side, the curve as an existing thing to be fitted. The
curve is a non-existing between going through the fractured fractal stable form geodesic surface of living parities.
A drawing with no moving part and no curve: the surface of the 2s and the 3s, a prime one other-than; the numbers 1 to 120
by +1, with their parities; and the walk of the +s less the −s, 1 to 600, with the numbers the between goes through.
check_the_living_parities_a_prime_is_one_other-than_and_the_between_goes_through.py is its check. The parities drawn here
are executed here again, by that check's own lines.

Usage: python3 -I make_draft37.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
spec = importlib.util.spec_from_file_location("the_living_parities", os.path.join(HERE, "check_the_living_parities_a_prime_is_one_other-than_and_the_between_goes_through.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the parities drawn, executed here again
parity, primes = m.the_living_parities(m.TO)
walk = m.the_walk(parity, m.TO)
THROUGH = [n for n in range(1, m.TO + 1) if walk[n] == 0]
assert THROUGH == [2, 4, 6, 10, 16, 26, 40, 96, 586] and max(walk[2:]) == 0
assert all(parity[2 ** a * 3 ** b] == (a + b) % 2 for a in range(8) for b in range(5))

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def a_number(x, y, w, h, n, size=12.5, edge=None):
    plus = parity[n] == 0
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="5" fill="{INK if plus else "#ffffff"}" stroke="{edge or INK}" stroke-width="{2.6 if edge else 1.4}"></rect>'
            + text(x + w / 2, y + h / 2 + size * 0.36, f"{n:,}", size, 600, "#ffffff" if plus else INK))
s = []
# the surface of the 2s and the 3s: by 2 a square on, by 3 a row on
SX, SY, SW, SH = 110, 300, 78, 40
for b in range(5):
    for a in range(8): s.append(a_number(SX + (SW + 6) * a, SY + (SH + 8) * b, SW, SH, 2 ** a * 3 ** b))
# the numbers 1 to 120 by +1, four rows of 30
NX, NY, NP = 846, 300, 21
for n in range(1, 121):
    x, y = NX + NP * ((n - 1) % 30), NY + 34 * ((n - 1) // 30)
    s.append(a_number(x, y, 18, 26, n, 8.5, ACC if n in THROUGH else None))
# the walk of the +s less the −s, 1 to 600: no level line of its own is drawn
WX, WY, WS, WV = 80, 640, 2.26, 6.0
pts = [f"{WX:.1f},{WY:.1f}"]
for n in range(1, 601):
    pts.append(f"{WX + WS * n:.1f},{WY - WV * walk[n - 1]:.1f}" if n > 1 else f"{WX + WS:.1f},{WY:.1f}"); pts.append(f"{WX + WS * n:.1f},{WY - WV * walk[n]:.1f}")
s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></polyline>')
for n in THROUGH: s.append(f'<circle cx="{WX + WS * n:.1f}" cy="{WY:.1f}" r="4.8" fill="{ACC}" stroke="#ffffff" stroke-width="1.4"></circle>')
for n in (96, 586): s.append(text(WX + WS * n, WY - 12, str(n), 12.5, 600, ACC))
ARIA = ("A drawing with no moving part and no curve. A grid of five rows of eight numbered boxes, dark and open in turn along a row and down a row, a board of two looks. "
        "Beside it four rows of thirty small numbered boxes, 1 to 120, dark and open with no turn of their own, eight of them with an accent edge. "
        "Under them a stepping line going down from its opening level, with nine accent dots at that level, the last two numbered 96 and 586; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t, w=700: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=720: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=720: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "a partner's word · no curve, an existing thing to be fitted · the between goes through the surface of living parities · from the numbers alone", "left", **small))
for i, t in enumerate(("A prime multiplied in is one other-than.", "The between is at no number of its own.", "It goes through the numbers with the +s and the −s the same.")):
    over.append(word(60, 104 + 36 * i, 760, t, "left", 600, 20, 30))
over.append(note(860, 104, "a number's living parity: a + with an even number of primes multiplied in it,", 620)); over.append(note(860, 124, "a − with an odd number, and 1 a + · v406other2's naming, a prime an inversion", 620))
over.append(note(860, 156, "this session's lean line on the numbers: a number's parity is the other-than", 620)); over.append(note(860, 176, "of the parity of the number back of it, with one prime less · one nand a number", 620))
over.append(head(60, 250, "multiplying: the surface of the 2s and the 3s"))
over.append(note(60, 274, "by 2 a box on, by 3 a row on · dark a + and open a − · next is other-than now at all steps", 720))
over.append(note(60, 552, "● all a number's backs surface one parity, 2 to 100,000 · a prime's own path is a me alone", 720))
over.append(head(840, 250, "adding 1: the same parities, 1 to 120", 640))
over.append(note(840, 274, "four rows of 30 · an accent edge: a number the between goes through", 640))
over.append(note(840, 448, "○ by +1, next is other-than now at 2,096,902 of 4,194,303 steps: one step in two, a measuring", 660))
over.append(note(840, 469, "along multiplying a line of one me says it, at all steps · along +1 no line of a me alone", 660))
over.append(head(60, 596, "the walk of the +s less the −s, 1 to 600: the between is its opening level, at no number of its own", 1100))
over.append(item(60, 812, "● the between goes through 2, 4, 6, 10, 16, 26, 40, 96 and 586: nine numbers to 4,194,304", 760))
over.append(note(60, 834, "at all other numbers of 2 to 4,194,304 the −s are the more · stepped, to that number", 760))
over.append(note(60, 855, "○ a field has its is-not at 906,150,257, Pólya's of 1919 broken: stepped to a number is no saying with all numbers", 760))
over.append(item(840, 812, "the straying, beside the square's side: a measuring, and no bound", 640))
over.append(note(840, 834, "at the most 1.33 sides from its between, at 96,862 · at 4,194,304 the −s are 582 the more, a side 2,048", 660))
over.append(note(840, 855, "the hypothesis, a field's, from the parities alone: the straying has the side's own power", 660))
over.append(note(840, 876, "not shown here, with all numbers · the 36th drawing is of the curve's side, a field's existing thing", 660))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The living parities: a prime is one other-than, and the between goes through</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'No curve is here. A number\'s parity is the other-than of the parity of the number with one prime less: the lean line, on the numbers.<br>'
           f'Along multiplying, next is other-than now at all steps. Along +1 it is at one step in two, a measuring.<br>'
           f'At the between the +s and the −s are the same. To 4,194,304 it goes through nine numbers, 2 to 586.<br>'
           f'With all numbers, the straying\'s power is not shown here. A candidate, offered to v406other2 and the sessions.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The living parities: a prime is one other-than, and the between goes through", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft37.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft37_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft37_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the walk's lowest to 600:", min(walk[1:601]))
