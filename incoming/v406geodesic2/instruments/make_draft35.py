"""Draft 35 · 0 and 3 are all-parity (session v406geodesic2).

A partner's sentences of 24 November, re-said a relation a sentence: 0 and 3 are all-parity; inward of the inward surface and
outward of the outward surface are the same; both are all-parity at a birth and at all living nows.
A drawing with no moving part: a parity as two wires, its four, 0 to 3; a birth of a 0 and of a 3 by the fifteen lines; a 0
and a 3 observed beside a parity; and a parity's own surfacing.
check_0_and_3_are_all-parity_executed.py is its check. The marks drawn here are executed here again, by that check's own
lines and v406Reiman's nand, opened from their own files.

Usage: python3 -I make_draft35.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
spec = importlib.util.spec_from_file_location("all_parity", os.path.join(HERE, "check_0_and_3_are_all-parity_executed.py"))
all_parity = importlib.util.module_from_spec(spec); spec.loader.exec_module(all_parity)
lines = all_parity.lines
its = lines.opened(os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "the_resolver_with_nand_alone.py"), "the_resolver_with_nand_alone")
TWO = its.TWO
PLUS, MINUS, ZERO, THREE = TWO[1], TWO[-1], TWO[0], (True, True)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the marks drawn, executed here again
fifteen = lambda now, observed: tuple(its.a_cell(now, list(observed)))[:2]
BIRTH = {(now, s): fifteen(now, [s] if s else []) for now in (ZERO, THREE) for s in (PLUS, None)}                # its laying and its next
assert all(BIRTH[(now, PLUS)] == (PLUS, PLUS) for now in (ZERO, THREE)) and BIRTH[(ZERO, None)] == (ZERO, ZERO) and BIRTH[(THREE, None)] == (THREE, THREE)
def surfacing_of(observed):                                                      # what surfaces of two observed, by the fifteen lines: a 0 born with it
    return fifteen(ZERO, observed)[1]
BESIDE = {w: surfacing_of([w, PLUS]) for w in (ZERO, THREE)}
assert BESIDE == {ZERO: PLUS, THREE: ZERO}
OWN = {w: all_parity.its_own_surfacing(its, w) for w in (ZERO, PLUS, MINUS, THREE)}
assert OWN == {ZERO: ZERO, PLUS: PLUS, MINUS: MINUS, THREE: ZERO}

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def wires(x, y, w, state, tint=INK):
    """A parity as two wires: its + wire over its − wire, a wire dark with an is."""
    return "".join(f'<rect x="{x:.1f}" y="{y + 16 * i:.1f}" width="{w}" height="10" rx="5" fill="{tint if lit else "#ffffff"}" stroke="{tint}" stroke-width="1.5"></rect>' for i, lit in enumerate(state))
arrow = lambda x1, y, x2: (f'<path d="M{x1},{y} L{x2 - 6},{y}" fill="none" stroke="{GREY}" stroke-width="1.6" stroke-linecap="round"></path>'
                           f'<path d="M{x2 - 12},{y - 5} L{x2 - 5},{y} L{x2 - 12},{y + 5}" fill="none" stroke="{GREY}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>')
s = []
# the four of two wires, 0 to 3
FX, FY = 930, 118
for i, state in enumerate((ZERO, PLUS, MINUS, THREE)):
    s.append(wires(FX + 130 * i, FY, 64, state)); s.append(text(FX + 130 * i + 32, FY + 56, str(i), 20, 700))
s.append(f'<path d="M{FX + 32},{FY - 12} C{FX + 32},{FY - 62} {FX + 422},{FY - 62} {FX + 422},{FY - 12}" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-linecap="round"></path>')
for x in (FX + 32, FX + 422): s.append(f'<circle cx="{x}" cy="{FY - 12}" r="4.4" fill="{ACC}"></circle>')
# a birth by the fifteen lines: a now, what surfaces, its next
for r, now in enumerate((ZERO, THREE)):
    y = 318 + 64 * r
    s.append(wires(96, y, 52, now))
    for c, surf in enumerate((PLUS, None)):
        x = 250 + 250 * c
        s.append(arrow(x - 70, y + 13, x - 14)); s.append(wires(x, y, 52, BIRTH[(now, surf)][1], ACC if surf else INK))
# observed beside a parity, by the fifteen lines
for r, w in enumerate((ZERO, THREE)):
    y = 600 + 64 * r
    s.append(wires(96, y, 52, w)); s.append(wires(176, y, 52, PLUS)); s.append(arrow(250, y + 13, 306)); s.append(wires(320, y, 52, BESIDE[w], ACC))
# a parity's own surfacing
for i, state in enumerate((ZERO, PLUS, MINUS, THREE)):
    x = 880 + 150 * i
    s.append(wires(x, 322, 44, state)); s.append(arrow(x + 50, 335, x + 82)); s.append(wires(x + 86, 322, 44, OWN[state], ACC))
s.append(f'<path d="M805,262 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Four pairs of wires in a row, numbered 0 to 3: neither wire dark, the upper dark, the lower dark, and both dark; with an accent line arching from the 0 to the 3. "
        "Under them, pairs of wires with arrows to pairs of wires: a 0 and a 3 to the same pair, twice; a 0 beside a plus to a plus, and a 3 beside a plus to neither wire; "
        "and four pairs, the 0 and the 3 to neither wire, the two between to themselves; and lines of words.")
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
over.append(word(60, 40, 1400, "a partner's sentences · 0 and 3 are all-parity · executed, their is ● and their is-not ○", "left", **small))
for i, t in enumerate(("0 and 3 are all-parity.", "Inward of the inward surface and outward of the outward surface are the same.", "Both are all-parity at a birth and at all living nows.")):
    over.append(word(60, 110 + 34 * i, 850, t, "left", 600, 20, 30))
over.append(word(FX + 227, FY - 62, 200, "all-parity", "center", 600, 14, 20, "{{accent}}"))
for i, t in enumerate(("neither wire", "a +", "a −", "both wires")): over.append(word(FX + 130 * i + 32, FY + 88, 120, t, "center", 400, 12.5, 18, GREY))
over.append(word(FX + 227, FY + 112, 520, "a parity is two wires, its + wire over its − wire · a wire dark with an is", "center", 400, 12.5, 18, GREY))
over.append(head(60, 280, "a birth, by the fifteen lines: a 0 and a 3, the same"))
over.append(word(180, 302, 130, "a + surfacing", "left", 400, 12.5, 18, GREY)); over.append(word(430, 302, 170, "all-parity surfacing", "left", 400, 12.5, 18, GREY))
over.append(word(60, 331, 30, "0", "left", 700, 16, 20)); over.append(word(60, 395, 30, "3", "left", 700, 16, 20))
over.append(note(580, 331, "a now, and its next a moment on", 220)); over.append(note(580, 395, "a 0 a 0 again, a 3 a 3 again", 220))
over.append(item(60, 446, "● as a now, a 0 and a 3 are the same at a birth and at all moments: all 21 observings"))
over.append(item(60, 470, "● observed alone, a 3 is a 0: no parity surfaces"))
over.append(item(60, 494, "● on a path of 2 to 5 mes closing: the same moments, all 296 openings"))
over.append(head(60, 562, "observed beside a parity, by the fifteen lines: a 0 and a 3 part"))
over.append(note(400, 613, "a 0 beside a +: the + surfaces", 380)); over.append(note(400, 677, "a 3 beside a +: all-parity surfaces", 380))
over.append(item(60, 730, "○ with 12 of 32 observings with a 3"))
over.append(item(60, 754, "○ on a torus of 2 by 2, a 3 for a 0 has other moments with 48 of 64 openings"))
over.append(item(60, 778, "○ this session's two lines of the 34th drawing: a 3 born with a parity lays no parity, 8 of 21"))
over.append(note(60, 812, "a 3 is laid by a me opening as a 3 alone: with a + or a − or a 0 at all openings, no moment has a 3"))
over.append(head(840, 280, "resolved forward: a parity's own surfacing"))
over.append(note(840, 304, "a pair surfaces a + with its + wire alone, a − with its − wire alone, and all-parity with both or neither", 660))
over.append(item(840, 392, "● at a me's now and at all it observes, a 3 and a 0 are the same: all 84 cases", 640))
over.append(item(840, 416, "● with the three, a +, a − and a 0, the two lines are the fifteen lines' still: all 39 cases", 650))
over.append(item(840, 440, "● on the torus of 2 by 2, a 3 for a 0 has the same moments: all 64 openings", 640))
over.append(note(840, 462, "32 nands with no parity observed, and 12 more a thing observed · one form's", 650))
over.append(head(840, 520, "the living code"))
over.append(item(840, 546, "● a + and a − observed together, and no parity observed, are one 0", 640))
over.append(note(840, 568, "○ a me with no prior, and a me with a prior of 0, a call's own, part: the 0 is a + a moment on", 660))
over.append(word(840, 596, 650, "<i>Not carried: a prior 0 a call supplies, which no line of the code makes.</i>", "left", 400, 14, 20))
over.append(note(840, 617, "v406Reiman's lines of nand, at their head", 650))
over.append(head(840, 676, "the word dissolving"))
over.append(note(840, 702, "this session's drawings 32 to 34 name a 0 by the word now dissolving · its name is all-parity", 660))
over.append(item(840, 734, "With all-parity surfacing, a me's next is the other-than of its now.", 640))
over.append(item(840, 758, "An all-parity's other-than is all-parity.", 640))
over.append(note(840, 780, "the 34th drawing's line, said again · two wires crossed: a 0 a 0, and a 3 a 3", 650))
over.append(note(840, 833, "this session's placing: 1 for a + and 2 for a −, the + wire a number's low place", 650))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">0 and 3 are all-parity</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A parity is two wires. A + is its + wire alone, and a − its − wire alone. Neither wire, 0, and both wires, 3, are all-parity.<br>'
           f'By the fifteen lines a 0 and a 3 are the same as a now, at a birth and at all moments, and observed alone.<br>'
           f'Observed beside a parity they part, a surface\'s own case. With a parity\'s own surfacing they are the same at all places.<br>'
           f'A candidate. The word said before for a 0 is dissolving: its name is all-parity.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("0 and 3 are all-parity", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft35.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft35_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft35_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
