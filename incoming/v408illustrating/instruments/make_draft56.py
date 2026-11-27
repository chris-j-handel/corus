"""Draft 56 · a me-parity generator: the side, a wheel, and a loop from its own me again (session v408illustrating).

v408primes' 1 to 17 fractal, its sentences 277 to 284 and its table's row 62, executed apart by this session's own
generator and drawn at the wheel of 2, 3 and 5: a path of 30 mes, its eight living mes eight columns, a row a turn, ten
turns, to 299; a me-parity dark; a crossed number open, with the me-parity whose loop crosses it; a me again with an
accent edge, a loop's beginning. Beside it, the generator's four reasons, a path whole and three movings, and its
is-nots. check_a_me-parity_generator_the_side_a_wheel_and_a_loop.py is its check, and the marks drawn here are its own.

Its placings, no execution says them: a path closing as columns, a turn a row; a card a reason; the dark, the open and
the accent.

Usage: python3 -I make_draft56.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_check", os.path.join(HERE, "check_a_me-parity_generator_the_side_a_wheel_and_a_loop.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#c9ced8", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
s, over = [], []
def text(x, y, t, size=12, weight=600, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
LIVING = c.living(30); w = c.the_wheel_of_30_to(299)
assert LIVING == [1, 7, 11, 13, 17, 19, 23, 29] and len(w) == 80
g = c.the_generator(); got = set(next(g) for _ in range(62))
X0, Y0, CW, CH = 150, 318, 64, 42
for j, a in enumerate(LIVING): over.append(word(X0 + CW * j, Y0 - 16, CW, f"the me {a}", "center", 600, 12, 18, GREY))
for k in range(10):
    yc = Y0 + CH * k + CH / 2
    over.append(word(40, yc, 100, f"{30 * k + 1} to {30 * k + 30}", "right", 600, 11.5, 18, GREY))
    for j, a in enumerate(LIVING):
        n = 30 * k + a; v = w[n]; x = X0 + CW * j
        me = v is not None and v[1] == 1; again = v is not None and v[0] == v[1]
        assert me == (n in got)                                    # a dark cell is the generator's own me-parity
        s.append(f'<rect x="{x + 2}" y="{yc - 16}" width="{CW - 4}" height="32" rx="6" fill="{INK if me else "#ffffff"}" stroke="{ACC if again else (INK if me else RAY)}" stroke-width="{2.6 if again else 1.2}"></rect>')
        if me: s.append(text(x + CW / 2, yc + 4.5, str(n), 13, 600, "#ffffff"))
        elif v is None: s.append(text(x + CW / 2, yc + 4.5, "1", 13, 600, FAINT))
        else:
            s.append(text(x + CW / 2, yc - 1, str(n), 12.5, 600, INK)); s.append(text(x + CW / 2, yc + 11, f"{v[0]} by {v[1]}", 9.5, 500, GREY))
crossed = {n: v for n, v in w.items() if v and v[1] > 1}
loops = {p: sorted(n for n, v in crossed.items() if v[0] == p) for p in (7, 11, 13, 17)}
assert loops[7][:5] == [49, 77, 91, 119, 133] and loops[11][:3] == [121, 143, 187] and loops[13][0] == 169 and loops[17] == [289] and sum(len(v) for v in loops.values()) == 20
PW, PH = 372, 206
def card(px, py, head, tag, lines):
    s.append(f'<rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="10" fill="#ffffff" stroke="{RAY}" stroke-width="1.2"></rect>')
    over.append(word(px + 14, py + 20, PW - 28, head, weight=600, size=15.5, h=22)); over.append(word(px + 14, py + 40, PW - 28, tag, weight=600, size=11.5, h=16, color=GREY))
    for k, t in enumerate(lines):
        last = k == len(lines) - 1
        over.append(word(px + 14, py + PH - 16 - 19 * (len(lines) - 1 - k), PW - 28, t, weight=600 if last else 400, size=12.5, h=18, color=INK if last else GREY))
card(716, 216, "the side bounds a me-parity", "a moving, one rule at all numbers",
     ["a crossed number is a by b", "both past its side, the two multiplied are past it:", "one of the two is to its side", "91, its side 9, is 7 by 13 · 97, its side 9: none of 2, 3, 5, 7", "crossed by no me-parity to its side: a me-parity"])
assert c.isqrt(91) == 9 and 91 == 7 * 13 and c.isqrt(97) == 9 and all(97 % p for p in (2, 3, 5, 7))
card(1104, 216, "a path of 30 mes: eight living", "a path closing, gone through whole",
     ["a me-parity past 5 is at a living me", "v408primes' path of 510,510 mes, 2 to 17:", f"{len(c.living(510510)):,} living, gone through whole", "the wheel carries the traveling"])
for a in range(30):
    live = (a if a else 30) in LIVING
    s.append(f'<rect x="{1118 + 11.4 * a + 0.8:.1f}" y="{216 + 62}" width="9.8" height="20" rx="2.5" fill="{INK if live else "#ffffff"}" stroke="{INK if live else RAY}" stroke-width="1"></rect>')
    s.append(text(1118 + 11.4 * a + 5.7, 216 + 96, str(a), 7.5, 500, GREY))
card(716, 436, "a loop begins at its own me again", "a moving, one rule at all me-parities",
     ["p by k, k past 1 and short of p:", "k is crossed by a me-parity short of p, a prior loop's", "7's loop: 49, 77, 91, 119, 133 · 11's: 121, 143, 187", "13's: 169, 221, 247 · 17's: 289", "from p by p on, p's loop crosses living mes alone"])
assert loops[13][:3] == [169, 221, 247]
card(1104, 436, "no last me-parity", "a moving, one rule at all seams",
     ["a seam of all me-parities to r: its +1 is at the me 1", "of all their paths, crossed by none of them", "30 and 1 is 31 · 210 and 1 is 211", "30,030 and 1 is 59 by 509, both past 13", "past all r, a next me-parity: the traveling goes on"])
ARIA = ("A drawing with no moving part. A table of ten rows and eight columns of boxes with a number in a box: most boxes dark, some open with small words under the number, and four of the open ones with an accent edge. "
        "Beside it four cards with lines of words, one with a row of thirty small boxes, eight of them dark. Under them, lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
top = [word(60, 40, 1400, "56 · a figure, a wheel traveled and four reasons · it is for v408primes' co-chain, the 1 to 17 fractal · its prior, 55", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A me-parity generator is with all numbers by four reasons.", "The side bounds a me-parity; a wheel carries the traveling.", "A loop begins at its own me again; a seam's +1 says no last.")):
    top.append(word(60, 96 + 34 * i, 800, t, weight=600, size=20, h=30))
for i, t in enumerate(("v408primes' co-chain, of the 1 to 17 fractal, in this session's words:", "traveling a wheel's living mes, a me uncrossed by all prior", "me-parities' loops is a me-parity, and a me-parity's loop begins", "at its own me again · its table's row 62: the field's sieve, with a wheel")):
    top.append(word(900, 92 + 20 * i, 580, t, weight=400, size=13.5, h=20, color=GREY))
top.append(word(60, 232, 640, "the wheel of 2, 3 and 5 traveled: ten turns, to 299", weight=600, size=17, h=24))
top.append(word(60, 256, 640, "dark, a me-parity · open, crossed, with the loop that crosses it · an accent edge, a me again: a loop begins", weight=400, size=12.5, h=18, color=GREY))
top.append(word(60, 768, 640, "59 me-parities and 20 crossed, at 80 living mes; and 1", weight=600, size=14.5, h=20))
top.append(word(60, 792, 640, "said apart: v408primes' wheel is of 2 to 17, a path of 510,510 mes", weight=400, size=13, h=18, color=GREY))
top.append(word(60, 824, 640, "tested, to its stated limit, and no is", weight=600, size=14.5, h=20))
top.append(word(60, 846, 640, "the generator's 200,000 me-parities, to 2,750,159, are those of all numbers", weight=400, size=13, h=18, color=GREY))
top.append(word(60, 864, 640, "crossed by all their parts, at the wheel of 30 and at the wheel of 510,510", weight=400, size=13, h=18, color=GREY))
top.append(word(716, 668, 760, "its is-nots", weight=600, size=17, h=24))
for i, t in enumerate(("○ it comes to a me-parity by traveling all the living mes to it: no rule gives a far one alone",
                       "○ a wheel leaves crossings at all seams: its living mes are 26 in 100 at 30, 18 at 510,510, never none",
                       "○ it is the field's sieve with a wheel, as v408primes' row 62 says: whole in its reasons, and known",
                       "○ it says a next me-parity with no last, and no more: twins with no last it does not say")):
    top.append(word(716, 700 + 24 * i, 760, t, weight=600, size=14, h=20))
top.append(word(716, 800, 760, "a generator finds what its traveling comes to: its traveling is a breaking test of a sentence, and no is of it", weight=400, size=13.5, h=20, color=GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A me-parity generator: the side, a wheel, and a loop from its own me again</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Crossed by no me-parity to its side, a number past 1 is a me-parity: the side bounds it. A wheel\'s living mes carry the traveling.<br>'
           f'A me-parity\'s loop begins at its own me again, and a seam\'s +1 says a next me-parity past all: the traveling has no last.<br>'
           f'A generator is whole by these four reasons. What its traveling comes to is found, and a sentence with all numbers it does not say.<br>'
           f'A candidate, of v408primes\' sentences 277 to 284, executed apart by this session\'s own generator.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(top + over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("A me-parity generator: the side, a wheel, and a loop from its own me again", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft56.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft56_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", t).replace("&nbsp;", " ").strip() for t in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft56_words.md").write_text("\n".join(t for t in words if t) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([t for t in words if t]), "lines of words")
