"""Draft 40 · the opening: twelve primes, three rounds of four, closing at a cube's shells (session v408illustrating).

The long-open drawing of the one table's row 36, for the opening of the draft of Exhibit THIRTY-TWO Natural Prime Numbering,
v407primes'. It goes on from v406geodesic2's thirty-nine, their look and their method: a candidate beside the last,
its numbers executed ahead of it, its is and its is-not both executed, its placings said apart.
A drawing with no moving part: the primes 2 to 61 as right spiral steps, four a round; the shells 1, 7, 19, 37 and 61 as
one self with rounds of six about it; and six rounds a row, a round's closing beside its shell.
check_the_opening_twelve_primes_three_rounds_of_four.py is its check. The numbers drawn here are executed here again, by
that check's own lines.

Its placings, no execution says them: the hand of the turn on the page, top to right to bottom and on; the closings at the
top; a step's distance from the 1 by its number among the steps, and by no size of its prime; the shells' cells as dots.

Usage: python3 -I make_draft40.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the look of the thirty-nine before, geom.py
from geom import *
spec = importlib.util.spec_from_file_location("the_opening", os.path.join(HERE, "check_the_opening_twelve_primes_three_rounds_of_four.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY = "#4a5160", "#9aa2b1", "#d9dde5"
SANS = "font-family: Inter, system-ui, sans-serif"
# the numbers drawn, executed here again
primes = m.the_primes(100)
rounds = [primes[4 * r:4 * r + 4] for r in range(6)]
shells = [m.shell(k) for k in range(7)]
assert rounds[:4] == [[2, 3, 5, 7], [11, 13, 17, 19], [23, 29, 31, 37], [41, 43, 47, 53]] and shells == [1, 7, 19, 37, 61, 91, 127]
assert [r[3] for r in rounds] == [7, 19, 37, 53, 71, 89] and [shells[k] - rounds[k - 1][3] for k in range(1, 7)] == [0, 0, 0, 8, 20, 38]
assert primes[16:18] == [59, 61]

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
s = []
# ---------- the right spiral: a prime a step, four steps a round, the hand top to right to bottom ----------
CX, CY = 385, 600
def far(t): return 42 * t if t <= 1 else 28 + 14 * t              # a step's distance from the 1, by its number among the steps
def at(t):
    a = math.radians(-90 + 90 * t)
    return CX + far(t) * math.cos(a), CY + far(t) * math.sin(a)
for n in (15, 16, 17, 18):                                        # four facings, faint, out to a facing's outer step
    x, y = at(n)
    s.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="{RAY}" stroke-width="1.2"></line>')
path = lambda t0, t1: " ".join(f"{x:.1f},{y:.1f}" for x, y in (at(t0 + (t1 - t0) * i / 400) for i in range(401)))
s.append(f'<polyline points="{path(0, 12)}" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"></polyline>')
s.append(f'<polyline points="{path(12, 18)}" fill="none" stroke="{FAINT}" stroke-width="1.4" stroke-dasharray="5 5"></polyline>')
x7, y7 = at(4); x37, y37 = at(12); x53, y53 = at(16)
s.append(f'<line x1="{x7:.1f}" y1="{y7:.1f}" x2="{x37:.1f}" y2="{y37:.1f}" stroke="{ACC}" stroke-width="2.4"></line>')
s.append(f'<line x1="{x37:.1f}" y1="{y37:.1f}" x2="{x53:.1f}" y2="{y53:.1f}" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="3 5"></line>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="14" fill="#ffffff" stroke="{INK}" stroke-width="1.8"></circle>' + text(CX, CY + 4.6, "1", 13, 600))
for n, p in enumerate(primes[:18], 1):
    x, y = at(n)
    if n <= 12:
        closes = n % 4 == 0
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{15 if closes else 13.5}" fill="{ACC if closes else INK}" stroke="#ffffff" stroke-width="1.6"></circle>' + text(x, y + 4.5, str(p), 12.5, 600, "#ffffff"))
    elif p == 61:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="#ffffff" stroke="{ACC}" stroke-width="2.4"></circle>' + text(x, y + 4.5, "61", 12.5, 600, ACC))
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13.5" fill="#ffffff" stroke="{FAINT if p != 53 else INK}" stroke-width="{1.4 if p != 53 else 1.8}"></circle>' + text(x, y + 4.5, str(p), 12.5, 600, GREY if p != 53 else INK))
s.append(text(CX, y53 - 26, "a round's closing · the next round's 1", 12.5, 600, GREY))
s.append(text(CX + far(17) + 22, CY + 4.5, "facing as 2", 12.5, 500, GREY, "start"))
s.append(text(CX + 20, CY + far(14) + 31, "facing as 3", 12.5, 500, GREY, "start"))
s.append(text(CX - far(15) - 22, CY + 4.5, "facing as 5", 12.5, 500, GREY, "end"))
s.append(text(CX - 26, CY + far(18) - 3, "61, the shell of 5 cubed less 4 cubed:", 12.5, 600, GREY, "end"))
s.append(text(CX - 26, CY + far(18) + 15, "round five's second step", 12.5, 500, GREY, "end"))
# ---------- a cube's shells about its corner, observed along the corner's line: one self and rounds of six ----------
HS, HY = 17, 392
for k, hx in zip(range(5), (826, 912, 1026, 1170, 1352)):
    for c in m.the_cells(k):
        q, r, _ = m.hexed(c); g = m.ring(m.hexed(c))
        x, y = hx + HS * (q + r / 2), HY + HS * math.sqrt(3) / 2 * r
        look = (f'fill="#ffffff" stroke="{INK}" stroke-width="1.5"' if g == 0 else f'fill="{ACC}"' if g == k else f'fill="{INK}"')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.7" {look} {"opacity=\"0.4\"" if k == 4 else ""}></circle>')
    s.append(text(hx, HY + 96, str(shells[k]), 21, 600, INK if k < 4 else FAINT))
# ---------- six rounds, a round a row: its four primes, its closing, its shell ----------
TX, TY, RH = 800, 640, 31
for i, four in enumerate(rounds):
    y = TY + RH * i; hit = four[3] == shells[i + 1]
    for j, p in enumerate(four):
        last = j == 3
        fill = (ACC if last else INK) if hit else "#ffffff"
        s.append(f'<rect x="{TX + 96 + 46 * j}" y="{y - 12}" width="40" height="24" rx="5" fill="{fill}" stroke="{INK if (hit or last) else FAINT}" stroke-width="1.4"></rect>'
                 + text(TX + 116 + 46 * j, y + 4.5, str(p), 12.5, 600, "#ffffff" if hit else (INK if last else GREY)))
    s.append(f'<rect x="{TX + 316}" y="{y - 12}" width="46" height="24" rx="5" fill="#ffffff" stroke="{ACC}" stroke-width="2.2"></rect>' + text(TX + 339, y + 4.5, str(shells[i + 1]), 12.5, 600, ACC))
ARIA = ("A drawing with no moving part. A spiral line winding outward from a small open circle numbered 1, with eighteen numbered dots on it, one at a right spiral step, "
        "four to a round; twelve are dark, three of them in the accent on one line upward, and six are open. "
        "Beside it five figures of dots in rounds of six about one open dot, of 1, 7, 19, 37 and 61 dots, a figure's outer round in the accent. "
        "Under them six rows of four numbered boxes with a fifth box in an accent edge; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
dot = lambda fill, edge: f'<span style="display: inline-block; width: 10px; height: 10px; border-radius: 6px; background: {fill}; border: 1.5px solid {edge}; margin: 0 6px 0 0; vertical-align: -1px"></span>'
over = []
over.append(word(60, 40, 1400, "for the opening of the draft of Exhibit THIRTY-TWO Natural Prime Numbering · the one table's row 36 · executed from the numbers alone", "left", **small))
for i, t in enumerate(("A prime is a right spiral step.", "Four steps are a round.", "Three rounds close at a cube's shells: 7, 19 and 37.")):
    over.append(word(60, 104 + 36 * i, 760, t, "left", 600, 20, 30))
over.append(note(860, 104, "the draft's opening, v407primes', word for word:", 620))
over.append(note(860, 128, "<i>Its three rounds are the twelve primes 2 to 37, and they close at 7, 19 and 37,</i>", 620))
over.append(note(860, 148, "<i>the shells of a cube about its corner: 2 cubed less 1, 3 cubed less 2 cubed,</i>", 620))
over.append(note(860, 168, "<i>and 4 cubed less 3 cubed.</i>", 620))
over.append(head(60, 250, "the right spiral: a prime a step, four steps a round"))
over.append(note(60, 274, dot(INK, INK) + "a prime, a step &nbsp;&nbsp; " + dot("{{accent}}", "{{accent}}") + "a round's closing, at its shell &nbsp;&nbsp; " + dot("#ffffff", FAINT) + "round four and on, closing at no shell", 680))
over.append(head(800, 250, "a cube's shells about its corner: one self, and rounds of six about it"))
over.append(note(800, 274, "observed along the corner's line · a shell's outer round in the accent: 6, 12, 18, and 24", 660))
for k, hx, cubes, more in zip(range(5), (826, 912, 1026, 1170, 1352), ("1 cubed", "2 cubed less 1", "3 cubed less 2 cubed", "4 cubed less 3 cubed", "5 cubed less 4 cubed"), ("one self", "1 and 6", "and 12", "and 18", "and 24")):
    over.append(word(hx, HY + 114, 170, cubes, "center", 400, 12.5, 18, GREY if k < 4 else FAINT))
    over.append(word(hx, HY + 132, 170, more, "center", 600, 12.5, 18, GREY if k < 4 else FAINT))
over.append(head(800, 572, "a round, its closing and its shell"))
over.append(note(TX + 96, 602, "its four primes", 200)); over.append(note(TX + 316, 602, "its shell", 100))
for i, (name, cubes) in enumerate(zip(("one", "two", "three", "four", "five", "six"), ("2 cubed less 1", "3 cubed less 2 cubed", "4 cubed less 3 cubed", "5 cubed less 4 cubed", "6 cubed less 5 cubed", "7 cubed less 6 cubed"))):
    y = TY + RH * i; lag = shells[i + 1] - rounds[i][3]
    over.append(word(TX, y, 90, "round " + name, "left", 400, 13.5, 20, GREY))
    over.append(word(TX + 374, y, 160, cubes, "left", 400, 13.5, 20, GREY))
    over.append(word(TX + 540, y, 130, "is" if lag == 0 else f"is-not · {lag} short", "left", 600, 14.5, 20, INK if lag == 0 else GREY))
over.append(item(800, 838, "● is: rounds one, two and three close at their shells · 7 is the 4th prime, 19 the 8th, 37 the 12th", 680))
over.append(note(800, 858, "of rounds of 1 to 12 primes, rounds of four alone · with 1 a step ahead of 2, a shell opens a round", 680))
over.append(item(800, 884, "○ is-not: from round four on a closing is short of its shell, by more with all rounds on", 680))
over.append(note(800, 904, "stepped to 250,000 rounds, one million primes · with all rounds it is not shown here", 680))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The opening: twelve primes, three rounds of four, closing at a cube\'s shells</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A prime is a right spiral step, and four steps are a round. Rounds one, two and three close at 7, 19 and 37.<br>'
           f'7, 19 and 37 are a cube\'s shells about its corner: one self, with rounds of six, twelve and eighteen about it.<br>'
           f'A round\'s closing is the next round\'s 1. Round four closes at 53, and its shell is 61, round five\'s second step.<br>'
           f'Stepped to one million primes, no round past the third closes at its shell. A candidate, for the draft\'s opening.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The opening: twelve primes, three rounds of four, closing at a cube's shells", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft40.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft40_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
words += [re.sub(r"<[^>]+>", "", w) for w in re.findall(r"<text[^>]*>([^<]*[a-z]{3}[^<]*)</text>", svg)]   # the drawing's own words
Path(WORK, "draft40_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the closings drawn:", [r[3] for r in rounds], "the shells:", shells[1:])
