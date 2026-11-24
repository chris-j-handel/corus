"""Draft 34 · a me's next: what surfaces to it, or the other-than of its now (session v406geodesic2).

Going on from a partner's sentence of 24 November, next is other-than now, and from the lean line's two is-nots yet open.
A drawing with no moving part: a me's next by its now and what surfaces to it, nine squares; the two lines by nand beside
the fifteen lines; a birth by the living code and by the two lines; and the societies gone through.
check_a_mes_next_what_surfaces_to_it_or_the_other-than_of_its_now.py is its check. The marks and numbers drawn here are
executed here again, by that check's own lines, v406Reiman's nand and Exhibit ONE Natural Resolver's own code.

Usage: python3 -I make_draft34.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from itertools import product
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
ROOT = os.path.join(HERE, "..", "..", "..")
spec = importlib.util.spec_from_file_location("a_mes_next", os.path.join(HERE, "check_a_mes_next_what_surfaces_to_it_or_the_other-than_of_its_now.py"))
lines = importlib.util.module_from_spec(spec); spec.loader.exec_module(lines)
it = lines.opened(os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "resolver_as_it_is.py"), "the_code_as_it_is")
names, _ = it.resolver(ROOT); step = names["_17_next_existing"]
its = lines.opened(os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "the_resolver_with_nand_alone.py"), "the_resolver_with_nand_alone")
its.NAND = lines.Numbered(its.NAND); TWO = its.TWO

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the marks and numbers drawn, executed here again
PARITY = {TWO[1]: 1, TWO[-1]: -1, TWO[0]: 0}
NINE = {(now, s): tuple(PARITY[x] for x in lines.the_two_lines_by_nand(its, TWO[now], [TWO[s]])) for now in (1, -1, 0) for s in (1, -1, 0)}   # its laying, its next
assert all(tuple(its.a_cell(TWO[now], [TWO[s]]))[:2] == lines.the_two_lines_by_nand(its, TWO[now], [TWO[s]]) for now, s in NINE)
assert all(NINE[(now, s)][1] == (s if s else -now) and NINE[(now, s)][0] == (NINE[(now, s)][1] if NINE[(now, s)][1] != now else 0) for now, s in NINE)
def numbered(what): lines.NANDS[0] = 0; what(); return lines.NANDS[0]
CELL, TWO_LINES = numbered(lambda: its.a_cell(TWO[1], [])), numbered(lambda: lines.the_two_lines_by_nand(its, TWO[1], []))
assert (CELL, TWO_LINES) == (46, 26) and numbered(lambda: lines.the_two_lines_by_nand(its, TWO[1], [TWO[-1]])) == 32
BORN = {0: 0, 1: 0, 2: 1}
birth = lines.by_the_living_code(it, step, it.spiral_couplings(3), BORN, 12)
assert birth == lines.by_the_two_lines(it.spiral_couplings(3), BORN, 12)
numbers = {}
for name_, couplings, mes, parities, moments in lines.the_societies(it):
    for opening in product(parities, repeat=len(mes)):
        nows = dict(zip(mes, opening)); numbers[name_] = numbers.get(name_, 0) + 1
        assert lines.by_the_living_code(it, step, couplings, nows, moments) == lines.by_the_two_lines(couplings, nows, moments)
assert list(numbers.values()) == [2046, 360, 252, 117, 1322]

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def a_parity(x, y, side, p):
    if p == 0: return f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="5" fill="#ffffff" stroke="{GREY}" stroke-width="1.3" stroke-dasharray="3 4"></rect>'
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="5" fill="{INK if p == 1 else "#ffffff"}" stroke="{INK}" stroke-width="1.5"></rect>'
            + text(x + side / 2, y + side / 2 + 5, "+" if p == 1 else "−", 15, 600, "#ffffff" if p == 1 else INK))
dot = lambda x, y: f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{ACC}" stroke="#ffffff" stroke-width="1.5"></circle>'
s = []
# nine squares: a me's now a row, what surfaces to it a column, a square its next
NX, NY, NP = 1090, 112, 52
for r, now in enumerate((1, -1, 0)):
    s.append(a_parity(NX - 78, NY + NP * r + 6, 30, now))
    for c, surf in enumerate((1, -1, 0)):
        laid, its_next = NINE[(now, surf)]
        s.append(a_parity(NX + NP * c, NY + NP * r, 42, its_next))
        if laid: s.append(dot(NX + NP * c + 40, NY + NP * r + 2))
for c, surf in enumerate((1, -1, 0)): s.append(a_parity(NX + NP * c + 6, NY - 46, 30, surf))
s.append(f'<path d="M{NX - 14},{NY - 54} L{NX - 14},{NY + 3 * NP - 6}" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
s.append(f'<path d="M{NX - 86},{NY - 8} L{NX + 3 * NP - 6},{NY - 8}" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
# nands: the fifteen lines and the two lines
for i, (n, look) in enumerate(((CELL, INK), (TWO_LINES, ACC))):
    s.append(f'<rect x="230" y="{312 + 34 * i}" width="{6 * n}" height="20" rx="4" fill="{look}"></rect>')
# a birth: a row a me, a column a moment
BX, BY, BP = 96, 520, 40
for a in range(3):
    s.append(text(BX - 12, BY + BP * a + 21, f"me {a + 1}", 12, 500, GREY, "end"))
    for t in range(12):
        s.append(a_parity(BX + BP * t, BY + BP * a, 32, birth[t][a]))
        if t and birth[t - 1][a] == 0 and birth[t][a] != 0: s.append(dot(BX + BP * t + 30, BY + BP * a + 2))
s.append(f'<path d="M805,262 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Nine squares in three rows of three, a row by a me's now, a plus, a minus and a none, and a column by what surfaces to it: "
        "the plus column all a plus, the minus column all a minus, and the none column a minus, a plus and a none; with an accent dot at six of the nine. "
        "Under them two bars, of 46 and of 26; a grid of three rows of twelve squares, some dashed and open, with an accent dot at two; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t: word(x, y, 700, t, "left", 600, 17, 24)
note = lambda x, y, t, w=720: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=720: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "going on from a partner's sentence, next is other-than now · a me's next, a relation a line · its is ● and its is-not ○", "left", **small))
for i, t in enumerate(("A me's next is the parity surfacing to it.", "With none surfacing, its next is the other-than of its now.", "A me lays its next, with its next other-than its now.")):
    over.append(word(60, 110 + 34 * i, 800, t, "left", 600, 22, 30))
over.append(word(NX + 78, 44, 220, "what surfaces to it", "center", 500, 12.5, 18, GREY)); over.append(word(NX - 100, NY + 78, 80, "its now", "right", 500, 12.5, 18, GREY))
over.append(word(NX + 180, NY + 60, 190, "a square its next", "left", 500, 12.5, 18, GREY)); over.append(word(NX + 180, NY + 80, 190, "an accent dot: laid", "left", 500, 12.5, 18, "{{accent}}"))
over.append(word(NX + 180, NY + 114, 200, "a none's other-than is a none", "left", 500, 12.5, 18, GREY))
over.append(head(60, 280, "by nand, a parity two wires"))
over.append(word(60, 322, 160, "the fifteen lines", "left", 500, 14, 20)); over.append(word(60, 356, 160, "the two lines", "left", 500, 14, 20))
over.append(word(230 + 6 * CELL + 12, 322, 300, f"{CELL} nands, none observed", "left", 400, 13.5, 20, GREY)); over.append(word(230 + 6 * TWO_LINES + 12, 356, 400, f"{TWO_LINES} nands, none observed · 6 more a thing observed, with both", "left", 400, 13.5, 20, GREY))
over.append(item(60, 398, "● case with case the fifteen lines' own laying and next: all 39 cases"))
over.append(note(60, 419, "a now of the three, with none, one and two observed of the three"))
over.append(note(60, 440, "○ with both wires, v407nanding's vault, as a now or observed: apart with 21 of 45 cases"))
over.append(head(60, 486, "a birth, by the living code and by the two lines: the same squares"))
over.append(item(60, 664, "● a newborn's next is the parity surfacing to it, as it is, and it lays it"))
over.append(note(60, 685, "a dashed square a none · with none surfacing a none is a none again, two wires crossed"))
over.append(head(60, 732, "the lean line's four is-nots, resolved forward"))
over.append(note(60, 758, "● its opening and its end me: with none surfacing, next is other-than now · the 33rd drawing"))
over.append(note(60, 779, "● a none in the path: a birth is a surfacing as it is"))
over.append(note(60, 800, "● a me observing two: a + and a − together surface none, and two alike surface the one"))
over.append(note(60, 833, "on a path of mes closing, all with priors, the two lines are v407nanding's lean line, two moments a coupling"))
over.append(head(840, 280, "societies, by Exhibit ONE's own code"))
for i, (n, t) in enumerate(zip(numbers.values(), ("paths closing, all with priors: one to ten mes", "paths closing, with newborns: 2 to 5 mes", "paths with an end me, all with priors: 2 to 7 mes",
                                                  "paths with an end me, with newborns: 2 to 4 mes", "tori of 2 by 2 and 2 by 3 with newborns, and of 3 by 3"))):
    over.append(word(900, 312 + 26 * i, 60, f"{n:,}", "right", 600, 14.5, 20)); over.append(word(914, 312 + 26 * i, 560, t, "left", 400, 14, 20))
over.append(item(840, 458, f"● the two lines' moments are the living code's at all moments: all {sum(numbers.values()):,} openings", 640))
over.append(note(840, 479, "○ with none surfacing and a next its now as it is: none of the 2,046", 650))
over.append(head(840, 530, "said already, by its file"))
over.append(word(840, 558, 650, "<i>With no prior, a me-parity is born with a surfacing.</i>", "left", 400, 14, 20))
over.append(word(840, 579, 650, "<i>At all else, a me's now is other-than its prior.</i>", "left", 400, 14, 20))
over.append(note(840, 600, "v407nanding's page, The now and same-existing me-parity: a me with a prior, and a me with none", 660))
over.append(note(840, 628, "here, one relation for the two: a none's other-than is a none", 650))
over.append(note(840, 649, "the fifteen lines, and a + and a − surfacing none: v406Reiman's lines of nand", 650))
over.append(head(840, 700, "this session's placings"))
over.append(note(840, 726, "the two lines as sentences of one relation · their nands are one form's, with no search of a least", 660))
over.append(note(840, 747, "a coupling, which me's laying is which me's observing, is a list, as v406Reiman's head has it", 660))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A me\'s next: what surfaces to it, or the other-than of its now</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A me\'s next is the parity surfacing to it. With none surfacing it is the other-than of its now, and a none\'s other-than is a none.<br>'
           f'A me lays its next, with its next other-than its now. The two lines\' moments are the living code\'s with all societies gone through.<br>'
           f'A birth, an end me, an opening and a me observing two are the one relation\'s own. By nand it is 26 for the fifteen lines\' 46.<br>'
           f'A candidate, offered to v407nanding: one relation for a me with a prior and a me with none.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A me's next: what surfaces to it, or the other-than of its now", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft34.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft34_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft34_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the nine, its laying and its next:", NINE)
