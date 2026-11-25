"""Draft 38 · two faces, one form: the public statement's part, drawn from the numbers (session v406geodesic2).

A partner's word of 24 November, re-said: go on with this, and with the helping and the learning from all the sessions.
The part is v406other2's, with v406me's paring. v406other2's asking of this session: the part of two faces, a drawing.
A drawing with no moving part: a turn of 30 with its eight places, their pairs and their quarter turns; rows of 30 to 360,
a prime dark and a crossed number open with its least prime; and the primes to 4,194,304 by their eight places.
check_two_faces_one_form_executed.py is its check. The marks and numbers drawn here are executed here again, by its lines.

Usage: python3 -I make_draft38.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
spec = importlib.util.spec_from_file_location("two_faces", os.path.join(HERE, "check_two_faces_one_form_executed.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the marks and numbers drawn, executed here again
PLACES = m.PLACES
crossed = m.the_primes(m.TO)
FOUR = [pow(7, k, 30) for k in range(4)]; FLIPS = [30 - x for x in FOUR]
assert FOUR == [1, 7, 19, 13] and sorted(FOUR + FLIPS) == PLACES
def least_prime(n): return next(p for p in range(2, n + 1) if n % p == 0)
BY_PLACE = {x: 0 for x in PLACES}
for n in range(7, m.TO + 1):
    if not crossed[n]: BY_PLACE[n % 30] += 1
assert (min(BY_PLACE.values()), max(BY_PLACE.values())) == (36917, 37036)

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
s = []
# the even face: a turn of 30, its eight places, their pairs and their quarter turns
CX, CY, CR = 300, 452, 150
at = lambda n, r=CR: (CX + r * math.sin(2 * math.pi * n / 30), CY - r * math.cos(2 * math.pi * n / 30))
s.append(f'<circle cx="{CX}" cy="{CY}" r="{CR}" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></circle>')
for x in PLACES[:4]:
    (x1, y1), (x2, y2) = at(x), at(30 - x)
    s.append(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" fill="none" stroke="{GREY}" stroke-width="1.3" stroke-dasharray="3 5"></path>')
for cycle, dash in ((FOUR, ""), (FLIPS, 'stroke-dasharray="7 5"')):
    pts = " ".join(f"{at(x)[0]:.1f},{at(x)[1]:.1f}" for x in cycle + cycle[:1])
    s.append(f'<polyline points="{pts}" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-linejoin="round" {dash}></polyline>')
for n in range(30):
    x, y = at(n)
    if n in PLACES:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{INK}" stroke="#ffffff" stroke-width="1.6"></circle>')
        tx, ty = at(n, CR + 22); s.append(text(tx, ty + 5, str(n), 15, 700))
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{GREY}" fill-opacity="0.55"></circle>')
# the uneven face: rows of 30, the eight places, 1 to 360
GX, GY, GW, GH, PX, PY = 770, 300, 62, 24, 70, 29
for c, x in enumerate(PLACES): s.append(text(GX + PX * c + GW / 2, GY - 10, str(x), 13, 700))
for r in range(12):
    s.append(text(GX - 12, GY + PY * r + 17, str(30 * r), 11.5, 500, GREY, "end"))
    for c, x in enumerate(PLACES):
        n, bx, by = 30 * r + x, GX + PX * c, GY + PY * r
        if n == 1:
            s.append(f'<rect x="{bx}" y="{by}" width="{GW}" height="{GH}" rx="5" fill="#ffffff" stroke="{GREY}" stroke-width="1.2" stroke-dasharray="3 4"></rect>' + text(bx + GW / 2, by + 17, "1", 12.5, 600, GREY))
        elif not crossed[n]:
            s.append(f'<rect x="{bx}" y="{by}" width="{GW}" height="{GH}" rx="5" fill="{INK}" stroke="{INK}" stroke-width="1.3"></rect>' + text(bx + GW / 2, by + 17, str(n), 12.5, 600, "#ffffff"))
        else:
            s.append(f'<rect x="{bx}" y="{by}" width="{GW}" height="{GH}" rx="5" fill="#ffffff" stroke="{ACC}" stroke-width="1.6"></rect>' + text(bx + 16, by + 17, str(n), 12, 600) + text(bx + 45, by + 17, f"by {least_prime(n)}", 10, 600, ACC))
# together even: the primes to 4,194,304 by their eight places
for c, x in enumerate(PLACES):
    h = 46 * BY_PLACE[x] / max(BY_PLACE.values())
    s.append(f'<rect x="{GX + PX * c + 8}" y="{714 - h:.1f}" width="{GW - 16}" height="{h:.1f}" rx="3" fill="{INK}" fill-opacity="0.8"></rect>')
    s.append(text(GX + PX * c + GW / 2, 732, f"{BY_PLACE[x]:,}", 11.5, 600))
s.append(f'<path d="M690,250 L690,770" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. A round of thirty small dots, eight of them large and numbered 1, 7, 11, 13, 17, 19, 23 and 29, joined across in four dashed pairs, with two accent four-sided lines, one whole and one dashed. "
        "Beside it a grid of twelve rows of eight numbered boxes, 1 to 359: most dark, some open with an accent edge and the words by 7, by 11, by 13 or by 17. Under the grid eight bars of one height, numbered 36,917 to 37,036; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t, w=700: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=620: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=620: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "the public statement's part, v406other2's, with v406me's paring · drawn at v406other2's asking · executed from the numbers", "left", **small))
for i, t in enumerate(("One at a time the primes are uneven. Together they are even.", "The even face is the fit. The uneven face is the fracturing.")):
    over.append(word(60, 108 + 38 * i, 900, t, "left", 600, 21, 30))
over.append(note(60, 186, "v406other2's sentences, of its statement for the public", 700))
over.append(head(60, 250, "the even face: a turn of 30, its eight places", 600))
over.append(item(60, 660, "● the same up and down: a place and the turn less it, four pairs"))
over.append(note(60, 681, "the dashed lines across · with the turns of 30, 210, 2,310 and 30,030"))
over.append(item(60, 711, "● round its quarter turns, by 7: 1, 7, 19, 13, and 1 again"))
over.append(note(60, 732, "the accent four · its flips, the dashed four: 29, 23, 11, 17"))
over.append(note(60, 753, "○ with a turn of 6 it is-not: 5 by 5 is 1 again · v406me's finding"))
over.append(head(720, 250, "the uneven face: rows of 30, the eight places, 1 to 359", 700))
over.append(note(770 + 8 * 70 + 16, 320, "a dark box", 130)); over.append(note(770 + 8 * 70 + 16, 339, "a prime", 130))
over.append(word(770 + 8 * 70 + 16, 380, 130, "an accent edge", "left", 400, 13.5, 20, "{{accent}}")); over.append(note(770 + 8 * 70 + 16, 399, "a crossed number,", 130)); over.append(note(770 + 8 * 70 + 16, 418, "by its least prime", 130))
over.append(note(770 + 8 * 70 + 16, 470, "49, 121, 169, 289:", 130)); over.append(note(770 + 8 * 70 + 16, 489, "a prime born", 130)); over.append(note(770 + 8 * 70 + 16, 508, "crosses from its", 130)); over.append(note(770 + 8 * 70 + 16, 527, "own square on", 130))
over.append(note(770 + 8 * 70 + 16, 700, "the primes past 5", 140)); over.append(note(770 + 8 * 70 + 16, 719, "to 4,194,304,", 140)); over.append(note(770 + 8 * 70 + 16, 738, "by their place", 140))
over.append(item(60, 800, "● a place is the prime's times in the next turn: once crossed, the prime less 1 times a place", 720))
over.append(note(60, 821, "the 8 places of 30 are 56 numbers of 210, 8 crossed by 7 and 48 places", 720))
over.append(item(60, 853, "● a prime past 3 is one more than a crossed number and one less than a crossed number", 720))
over.append(note(60, 874, "one of the two is a seam of 6 · one of the two is a seam of 4 · at 13, 12 is the two seams, v406me's finding", 740))
over.append(item(820, 778, "● together even: 36,917 to 37,036 a place, the same to a part in a hundred", 660))
over.append(item(820, 802, "● one at a time uneven: a row of 30 has 0 to 7 primes", 660))
over.append(note(820, 823, "a measuring, to 4,194,304", 660))
over.append(note(820, 853, "this session's living parities at the places: a prime a −, and 49 a +, two primes multiplied", 660))
over.append(note(820, 874, "of the crossed numbers at the places, two in three are a +, a measuring", 660))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Two faces, one form</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'The even face: a turn\'s places are the same up and down, and a turn of 30 has them round its quarter turns, one four and its flips.<br>'
           f'The uneven face: a prime born crosses places from its own square on. One at a time, a row of 30 has 0 to 7 primes.<br>'
           f'Together, to 4,194,304, the eight places have the primes the same to a part in a hundred.<br>'
           f'The statement\'s part, v406other2\'s, drawn from the numbers alone. A candidate.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Two faces, one form", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft38.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft38_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft38_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
