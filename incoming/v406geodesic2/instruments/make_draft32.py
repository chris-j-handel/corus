"""Draft 32 · the lean line rigorized, its is and its is-not (session v406geodesic2).

By a partner's word of 24 November, re-said: the nand code is being explored as one line, and this session helps rigorize.
A drawing with no moving part: v407nanding's lean line beside the living code's own moments, on a path closing, at a birth
and on a surface; and a parity of two wires, its other-than a crossing.
check_the_lean_line_rigorized_its_is_and_its_is-not.py is its check. The marks and numbers drawn here are executed here
again, by that check's own lines and Exhibit ONE Natural Resolver's own code, opened from their own files.

Usage: python3 -I make_draft32.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
ROOT = os.path.join(HERE, "..", "..", "..")
spec = importlib.util.spec_from_file_location("the_rigor", os.path.join(HERE, "check_the_lean_line_rigorized_its_is_and_its_is-not.py"))
rigor = importlib.util.module_from_spec(spec); spec.loader.exec_module(rigor)
it = rigor.opened(os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "resolver_as_it_is.py"), "the_code_as_it_is")
names, _ = it.resolver(ROOT); step = names["_17_next_existing"]

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
MONO = "font-family: ui-monospace, SFMono-Regular, Menlo, monospace"
# the moments drawn, executed here again
FIVE = (1, 1, -1, 1, 1)
path = [[m[a] for a in range(5)] for m in rigor.by_the_living_code(it, step, it.spiral_couplings(5), dict(enumerate(FIVE)), 11)]
assert path == rigor.by_the_lean_line(FIVE, 11)
ROLL = [(0, 0), (2, 1), (4, 2), (6, 3), (8, 4)]                                  # a parity rolling: two moments on and one me on, its other-than
assert all(path[t2][a2] == -path[t1][a1] for (t1, a1), (t2, a2) in zip(ROLL, ROLL[1:]))
BORN = (0, 0, 1)
birth = [[m[a] for a in range(3)] for m in rigor.by_the_living_code(it, step, it.spiral_couplings(3), dict(enumerate(BORN)), 12)]
APART = [(t + 2, a) for t in range(10) for a in range(3) if birth[t + 2][a] != -birth[t][(a - 1) % 3]]
assert APART and max(t for t, _ in APART) < 3 + 2 and all(birth[t + 2][a] == -birth[t][(a - 1) % 3] for t in range(3, 10) for a in range(3))
born = {n: rigor.newborns(it, step, n) for n in range(2, 6)}
assert sum(born[n][0] for n in born) == 296 and all(born[n][1] == born[n][0] and born[n][2] == n for n in born)
SURFACES = {k: rigor.a_surface(it, step, *k) for k in ((2, 2), (2, 3), (3, 3))}
KINDS = ["lean", "the me back, a moment, the same", "its own, a moment, its other-than"]
assert [SURFACES[k][0] for k in SURFACES] == [8, 10, 8] and [[SURFACES[k][1][x] for x in KINDS] for k in SURFACES] == [[16, 0, 0], [58, 6, 0], [386, 12, 114]]

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def a_prior(x, y, side, p):
    if p == 0: return f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="5" fill="#ffffff" stroke="{GREY}" stroke-width="1.3" stroke-dasharray="3 4"></rect>'
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="5" fill="{INK if p == 1 else "#ffffff"}" stroke="{INK}" stroke-width="1.5"></rect>'
            + text(x + side / 2, y + side / 2 + 5, "+" if p == 1 else "−", 15, 600, "#ffffff" if p == 1 else INK))
s = []
# a path of five mes closing, by the living code: a row a moment, a square a me's prior
X0, Y0, P = 96, 214, 34
for t, row in enumerate(path):
    s.append(text(X0 - 14, Y0 + P * t + 20, str(t), 12, 500, GREY, "end"))
    for a, p in enumerate(row): s.append(a_prior(X0 + P * a, Y0 + P * t, 28, p))
for a in range(5): s.append(text(X0 + P * a + 14, Y0 - 10, str(a + 1), 12, 500, GREY))
for (t1, a1), (t2, a2) in zip(ROLL, ROLL[1:]):
    x1, y1, x2, y2 = X0 + P * a1 + 14, Y0 + P * t1 + 14, X0 + P * a2 + 14, Y0 + P * t2 + 14
    s.append(f'<path d="M{x1:.1f},{y1 + 16:.1f} L{x2 - 6:.1f},{y2 - 18:.1f}" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-linecap="round"></path>')
    s.append(f'<circle cx="{x2 - 6:.1f}" cy="{y2 - 18:.1f}" r="4.2" fill="{ACC}"></circle>')
# a parity of two wires: its other-than a crossing
for y1, y2 in ((690, 730), (730, 690)):
    s.append(f'<path d="M96,{y1} L170,{y1} C215,{y1} 215,{y2} 260,{y2} L330,{y2}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
# a newborn: a row a me, a column a moment
BX, BY, BP = 916, 150, 42
for a in range(3):
    s.append(text(BX - 14, BY + BP * a + 22, f"me {a + 1}", 12, 500, GREY, "end"))
    for t in range(12): s.append(a_prior(BX + BP * t, BY + BP * a, 32, birth[t][a]))
for t in range(12): s.append(text(BX + BP * t + 16, BY - 10, str(t), 12, 500, GREY))
for t, a in APART: s.append(f'<rect x="{BX + BP * t - 4}" y="{BY + BP * a - 4}" width="40" height="40" rx="8" fill="none" stroke="{ACC}" stroke-width="2.6"></rect>')
# a surface: a bar a torus, its openings by the single line they settle to
SX, SW = 916, 380
for i, k in enumerate(SURFACES):
    y, all_of_it, x = 452 + 40 * i, 2 ** (k[0] * k[1]), SX
    for kind, look in zip(KINDS, (f'fill="{ACC}"', f'fill="{INK}"', f'fill="#ffffff" stroke="{INK}" stroke-width="1.4"')):
        w = SW * SURFACES[k][1][kind] / all_of_it
        if w: s.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="22" rx="3" {look}></rect>')
        x += w
for i, look in enumerate((f'fill="{ACC}"', f'fill="{INK}"', f'fill="#ffffff" stroke="{INK}" stroke-width="1.4"')):
    s.append(f'<rect x="846" y="{579 + 26 * i}" width="16" height="16" rx="3" {look}></rect>')
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. A grid of eleven rows of five squares, dark with a plus or open with a minus, with an accent line stepping two rows down and one square on, four times. "
        "Under it two wires crossing. Beside them a grid of three rows of twelve squares, some dashed and open, with an accent edge about some squares of its opening columns; "
        "and three bars, of one, two and three parts; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t: word(x, y, 640, t, "left", 600, 17, 24)
note = lambda x, y, t, w=520: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=520: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "a partner's word · the nand code explored as one line · rigorized, its is ● and its is-not ○, beside the living code's own lines", "left", **small))
over.append(head(60, 84, "the lean line, as v407nanding's page has it"))
over.append(word(60, 112, 730, "def now_and_same_existing_me_parity(me_now, other_prior):", "left", 500, 13.5, 20, INK, MONO + "; white-space: pre"))
over.append(word(60, 132, 730, "    return me_now, NOT_BOTH[(other_prior, other_prior)]", "left", 500, 13.5, 20, INK, MONO + "; white-space: pre"))
over.append(note(60, 160, "a moment on, a me's prior is its now · its now is the other-than of the prior of the me back of it", 730))
over.append(note(60, 606, "a path of five mes closing, by the living code: a row a moment, a square a me's prior", 730))
LX = 300
for y, t, kind in ((214, "● a path of mes closing, all with priors", item), (235, "one to ten mes, all 2,046 openings, at all moments: one nand a me a moment", note),
                   (256, "the accent line: two moments on and one me on, its other-than", note),
                   (296, "● its opening, one nand more a me, once", item), (317, "a me's opening now is the other-than of its own prior", note),
                   (338, "○ with the opening now the prior itself: none of the 2,046", note),
                   (378, "● one me observing itself", item), (399, "the right spiral step, (x, y) to (y, −x), its own again with four moments", note),
                   (439, "● two mes facing, opening alike", item), (460, "the other's next prior is the me's own now, v407nanding's pair", note),
                   (481, "○ opening unlike: at no moment", note),
                   (518, "● a path with an end me: all mes with a me back of them", item), (539, "from the opening, 2 to 7 mes, all openings", note),
                   (560, "○ the end me, none back of it: one moment, its prior its other-than", note)):
    over.append(kind(LX, y, t, 490))
over.append(head(60, 656, "a parity of two wires: its other-than is a crossing, no nand"))
over.append(note(60, 762, "a + wire and a − wire, crossed", 300))
over.append(item(360, 690, "● a + a −, a − a +, and a none a none", 430))
over.append(note(360, 712, "○ wire by wire, two nands: a none is both wires, no parity", 430))
over.append(note(360, 734, "the 29th drawing's form is wire by wire, right with priors alone", 430))
over.append(head(60, 812, "the twelve lines' more, in v407nanding's own sentence"))
over.append(word(60, 840, 730, "<i>The twelve lines carry more: many others surfacing, and a me with no prior.</i>", "left", 400, 14, 20))
over.append(note(60, 861, "its page, The leanest resolving · executed here: how much more, and at which moments", 730))
over.append(head(840, 84, "a newborn, a me opening with no prior"))
over.append(note(840, 108, "a path of three closing, opening none, none, +, by the living code · a dashed square a none", 650))
over.append(item(840, 300, "● from the moment of its number of mes on, the lean line is the path's", 640))
over.append(note(840, 321, "○ with a none in the path: all 296 openings of 2 to 5 mes part · an accent edge a parting", 650))
over.append(head(840, 384, "a surface, a me observing two"))
over.append(note(840, 408, "tori, all their openings, by the living code · a bar's parts: the single line an opening settles to", 650))
for i, k in enumerate(SURFACES):
    y = 463 + 40 * i
    over.append(word(840, y, 70, f"{k[0]} by {k[1]}", "left", 500, 14, 20))
    over.append(word(916 + 380 + 14, y, 180, f"{SURFACES[k][0]} of {2 ** (k[0] * k[1])} from the opening", "left", 400, 13, 20, GREY))
for i, t in enumerate((f"the lean line, along or across: 16, 58 and 386", "the me back, a moment, the same: 6 and 12", "a me's own, a moment, its other-than: 114")):
    over.append(word(872, 587 + 26 * i, 600, t, "left", 400, 14, 20))
over.append(item(840, 680, "● settled, all openings are a single line's", 640))
over.append(note(840, 701, "○ the lean line's alone: 16 of 16, 58 of 64 and 386 of 512", 650))
over.append(head(840, 760, "said by its file"))
over.append(note(840, 786, "the lean line and its five lines of check: v407nanding's page, one to seven mes by the twelve lines", 650))
over.append(note(840, 807, "a surface settled and a newborn's path as single paths: this session's logic, its sentence 51", 650))
over.append(note(840, 828, "the right spiral of a self and an other, opening alike and unlike: v407nanding's page of it", 650))
over.append(note(840, 861, "the numbers here are by Exhibit ONE Natural Resolver's own code, as v406Reiman's file opens it", 650))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The lean line rigorized, its is and its is-not</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'On a path of mes closing, all with priors, the lean line is the living code\'s own priors at all moments: one nand a me a moment.<br>'
           f'Its opening is one nand more, once. An end me, a none in the path and a me observing two are its is-nots, found by executing.<br>'
           f'Settled, a newborn\'s path is the lean line\'s again, and a surface is the lean line\'s or one more single line\'s.<br>'
           f'With a parity two wires, its other-than is a crossing and no nand. A candidate, offered to v407nanding.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The lean line rigorized, its is and its is-not", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft32.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft32_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
words = [("`" + w + "`") if w.startswith(("def ", "return ")) else w for w in words]
Path(WORK, "draft32_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; partings drawn:", APART, "· surfaces:", {k: v[0] for k, v in SURFACES.items()})
