"""Draft 43 · the six and the ten round 30: a number at its place round 6 and its place round 10 (session v408illustrating).

A drawing of v408primes' page for illustrating, a view more of the six and the ten beside the 42nd drawing's sixty cells.
A drawing with no moving part: a table of six by ten, thirty numbers at thirty of its sixty cells.
check_the_six_and_the_ten_round_30.py is its check. The numbers drawn here are executed here again, by that check's own lines.

Its placings, no execution says them: round 6 across and round 10 down; 0 at the table's corner.

Usage: python3 -I make_draft43.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_thirty", os.path.join(HERE, "check_the_six_and_the_ten_round_30.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
rows = m.the_thirty()
at = {(a, b): (n, open_, prime) for n, a, b, open_, prime, _ in rows}
assert len(at) == 30 and sum(o for _, o, _ in at.values()) == 8 and sum(p for *_, p in at.values()) == 10
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
X0, Y0, CW, CH = 190, 306, 90, 50
s = []
for a in range(6): s.append(text(X0 + CW * a + CW / 2, Y0 - 12, str(a), 14, 600, GREY))
for b in range(10): s.append(text(X0 - 16, Y0 + CH * b + CH / 2 + 5, str(b), 14, 600, GREY, "end"))
step = " ".join(f"{X0 + CW * (n % 6) + CW / 2:.0f},{Y0 + CH * (n % 10) + CH / 2:.0f}" for n in range(6))
for a in range(6):
    for b in range(10):
        x, y = X0 + CW * a + 4, Y0 + CH * b + 4
        if (a, b) not in at:
            s.append(f'<rect x="{x}" y="{y}" width="{CW - 8}" height="{CH - 8}" rx="6" fill="#ffffff" stroke="{RAY}" stroke-width="1.2" stroke-dasharray="4 4"></rect>'); continue
        n, open_, prime = at[(a, b)]
        fill, edge, ink = (ACC, ACC, "#ffffff") if open_ and prime else ("#ffffff", ACC, ACC) if open_ else (INK, INK, "#ffffff") if prime else (TINT, RAY, INK)
        s.append(f'<rect x="{x}" y="{y}" width="{CW - 8}" height="{CH - 8}" rx="6" fill="{fill}" stroke="{edge}" stroke-width="{2.2 if open_ and not prime else 1.2}"></rect>' + text(x + CW / 2 - 4, y + CH / 2 + 1, str(n), 15, 600, ink))
s.append(f'<polyline points="{step}" fill="none" stroke="{GREY}" stroke-width="1.3" stroke-dasharray="2 5"></polyline>')
ARIA = ("A drawing with no moving part. A table of six columns and ten rows of boxes: thirty with a number, 0 to 29, on slanting lines, and thirty open with a dashed edge, by turns. "
        "Seven numbered boxes are in the accent and one is with an accent edge, in two columns; three are dark; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
box = lambda fill, edge, dash="solid": f'<span style="display: inline-block; width: 22px; height: 12px; border-radius: 4px; background: {fill}; border: 1.4px {dash} {edge}; margin: 0 7px 0 0; vertical-align: -2px"></span>'
over = [word(60, 40, 1400, "for v408primes' page for illustrating · a view more of the six and the ten, beside the 42nd drawing's sixty cells · executed from the numbers alone", weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")]
for i, t in enumerate(("A number round 30 is at a place round 6 and a place round 10.", "Thirty numbers reach thirty of sixty cells.", "The eight uncrossed are two columns by four rows.")):
    over.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
over.append(note(860, 104, "v408primes' own words of its page:", 600))
over.append(note(860, 128, "<i>the six other-than-other-thans locating and the ten other-thans forming</i>", 600))
over.append(head(X0, 246, "its place round 6, across", 400)); over.append(word(60, 286, 110, "its place<br>round 10,<br>down", weight=600, size=13.5, h=54, color=GREY, extra="line-height: 18px"))
over.append(head(800, 262, "thirty numbers at thirty of sixty cells"))
over.append(item(800, 296, "● a number is at its place round 6 and its place round 10, one for one"))
over.append(item(800, 322, "● +1 is one place on at both, the dotted line · thirty steps reach 0 again"))
over.append(item(800, 348, "● the thirty reached are with both places odd, or both even"))
over.append(note(800, 370, "the thirty more, one place odd and one even, are open cells"))
over.append(head(800, 428, "the eight, two columns by four rows"))
over.append(item(800, 462, "● uncrossed by 2, 3 and 5: the places 1 and 5 round 6, by 1, 3, 7 and 9 round 10"))
over.append(item(800, 488, "● the primes below 30 are ten: 2, 3 and 5, and the eight less 1"))
over.append(item(800, 514, "● podal round 30 is podal round 6 and round 10 both"))
over.append(note(800, 536, "1 with 29, 7 with 23, 11 with 19 and 13 with 17 · 0 and 15 their own podal"))
over.append(note(800, 580, box("{{accent}}", "{{accent}}") + "uncrossed, a prime &nbsp;&nbsp; " + box("#ffffff", "{{accent}}") + "uncrossed, 1 &nbsp;&nbsp; " + box(INK, INK) + "2, 3 and 5 &nbsp;&nbsp; " + box(TINT, RAY) + "crossed &nbsp;&nbsp; " + box("#ffffff", FAINT, "dashed") + "an open cell"))
over.append(head(800, 650, "beside the prime resolving form"))
over.append(note(800, 682, "○ the form is sixty cells too, six columns by ten rows, 34 of them named"))
over.append(note(800, 704, "a seating of its columns and its rows at these places is not executed"))
over.append(item(800, 740, "○ is-not: a table of six by five, or of three by ten, is thirty cells, all reached"))
over.append(note(800, 762, "the table of six by ten alone is with open cells, thirty of its sixty"))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The six and the ten round 30: a number at its place round 6 and its place round 10</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A number round 30 is at a place round 6 and a place round 10, one for one. +1 is one place on at both.<br>'
           f'Of the table\'s sixty cells thirty are reached, both places odd or both even. Thirty are open cells.<br>'
           f'The eight uncrossed by 2, 3 and 5 are two columns by four rows. The primes below 30 are ten.<br>'
           f'A seating of the form\'s columns and rows at these places is not executed. A candidate, of v408primes\' page.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The six and the ten round 30: a number at its place round 6 and its place round 10", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft43.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft43_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft43_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; cells reached:", len(at))
