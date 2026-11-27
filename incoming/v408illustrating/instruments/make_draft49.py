"""Draft 49 · Turn's marks again: twins, a next no more than 246 apart, a seam's numbers by its places, and odd and even across (session v408illustrating).

Beside the 46th drawing: its marks made again with v408primes' lines of 25 November, executed apart to 4,194,304.
check_turn_its_marks_again.py is its check. The numbers drawn here are executed here again, by that check's own lines.

Its placings, no execution says them: a mark's row of the form, the form's page's own; a span by 4 a column.

Usage: python3 -I make_draft49.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW   (about a minute)
"""
import importlib.util, json, os, re, sys
from fractions import Fraction
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
from geom import page as lay
spec = importlib.util.spec_from_file_location("marks", os.path.join(HERE, "check_turn_its_marks_again.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
twins, near, widest, past, apart = m.the_numbers()
assert twins[0] == 4 and near[0] == 11 and widest == (148, 2010733) and past == {2: 3, 10: 257, 20: 75037} and apart[0] < 1
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
s = []
X0, CW = 60, 76
def row(y, values, fill, ink, edge):
    for j, v in enumerate(values):
        s.append(f'<rect x="{X0 + CW * j + 3}" y="{y}" width="{CW - 6}" height="30" rx="6" fill="{fill}" stroke="{edge}" stroke-width="1.2"></rect>' + text(X0 + CW * j + CW / 2, y + 20, f"{v:,}" if isinstance(v, int) else v, 12.5, 600, ink))
for j, (a, b) in enumerate(m.SPANS): s.append(text(X0 + CW * j + CW / 2, 336, f"to {b:,}", 10.5, 500, GREY))
row(372, twins, INK, "#ffffff", INK); row(452, near, TINT, INK, RAY)
turns, t, pl = [], 1, 1
for p in (2, 3, 5, 7, 11, 13): t *= p; pl *= p - 1; turns.append((t, Fraction(t, pl)))
for j, (t, f) in enumerate(turns):
    s.append(text(X0 + 112 * j + 53, 596, f"{t:,}", 10.5, 500, GREY))
    s.append(f'<rect x="{X0 + 112 * j + 3}" y="604" width="100" height="30" rx="6" fill="#ffffff" stroke="{ACC}" stroke-width="2"></rect>' + text(X0 + 112 * j + 53, 624, str(f), 12.5, 600, ACC))
ARIA = ("A drawing with no moving part. Two rows of nine numbered boxes, one dark and one tinted, a number greater at all boxes on; under them a row of six boxes with an accent edge; "
        "beside them four blocks of words, one under an other; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=680: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=680: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=680: word(x, y, w, t, "left", 600, 14.5, 20)
over = [word(60, 40, 1400, "49 · a column, Turn · it is for v408primes' lines at Turn's marks · its prior, 46 · beside it now, 46", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A span by 4 is with more twins than the span before.", "A seam's numbers by its places settle at no seam.", "Round a loop, odd and even across are apart by short of 1 in 100.")):
    over.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
over.append(note(860, 104, "v408primes' lines, said to this session at the exchange on 25 November,", 600))
over.append(note(860, 124, "executed here apart to 4,194,304 · its word of a prime is a me-parity", 600))
over.append(head(60, 262, "a span by 4, from 16 to 64 on"))
over.append(note(60, 286, "a column a span, four times the span before", 680))
over.append(item(60, 358, "twins in a span · a last's mark", 680)); over.append(item(60, 438, "a prime with its next no more than 246 apart · a beat's mark", 680))
over.append(note(60, 500, f"○ of one beat: the widest from a prime to its next below 4,000,000 is {widest[0]}, after {widest[1]:,}", 700))
over.append(head(60, 548, "a seam's numbers by its places · a value's mark"))
over.append(note(60, 572, "the seams of 2 to 30,030", 680))
over.append(note(60, 652, f"past 2 at 3, past 10 at {past[10]} and past 20 at {past[20]:,}: settled at no seam", 700))
over.append(head(60, 712, "odd and even across · a parity's mark"))
over.append(note(60, 738, "round all loops of 3 to 30, with all their numbers to 4,194,304:", 700))
over.append(item(60, 762, f"● apart by short of 1 in 100 of a loop's numbers · the most, {apart[0]:.3f} in 100, round {apart[1]} at {apart[2]}", 700))
over.append(head(820, 262, "a mark, the form's page and v408primes' line"))
BLOCKS = (("3 · a completing fixing as a last · twins", "the form's page: named in its cell", "Twins, span by 4, are never fewer: 4, 10, 19, 71, on to 18,325 to 4,000,000.", "its sentence 163 · its table's row of twins: named, stepped"),
          ("7 · a sequencing fixing to one beat · bounded gaps", "the form's page: not yet resolving", "Me-parities with their next no more than 246 apart come at all spans by 4 never fewer", "its sentence 156 · its table's row of bounded gaps: named, stepped"),
          ("8 · a rate fixing as a value · Brun", "the form's page: not yet resolving", "A seam's numbers by its places never settle: past 2 at 3, past 10 at 257, past 20 at 75,037.", "its sentence 162 · its table's row of Brun's adding: named, stepped"),
          ("6 · a parity fixing as a magnitude · the parity wall", "the form's page: a naming", "Round all loops of 3 to 30, at all their places, odd and even across come alike", "its sentence 166 · checked"))
for k, (a, b, c, d) in enumerate(BLOCKS):
    y = 300 + 122 * k
    over.append(item(820, y, a, 640)); over.append(note(820, y + 24, b, 640))
    over.append(word(820, y + 48, 640, "<i>" + c + "</i>", "left", 400, 13, 20, GREY)); over.append(note(820, y + 70, d + " · executed apart here: is", 640))
over.append(item(820, 800, "○ stepped to a number is no saying with all numbers, v406geodesic2's", 640))
over.append(note(820, 822, "a mark is made again; a last, a beat and a value are shown at no span", 640))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Turn\'s marks again: a last, a beat, a value and a parity, by v408primes\' lines</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A span by 4 is with more twins than the span before, and with more primes a next no more than 246 apart.<br>'
           f'A seam\'s numbers by its places settle at no seam. Round a loop, odd and even across are apart by short of 1 in 100.<br>'
           f'The 46th drawing\'s marks of bounded gaps, of Brun and of the parity wall are made again by v408primes\' lines.<br>'
           f'Stepped to 4,194,304 is no saying with all numbers. A candidate, beside the 46th.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = lay("Turn's marks again: a last, a beat, a value and a parity, by v408primes' lines", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft49.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft49_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft49_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
