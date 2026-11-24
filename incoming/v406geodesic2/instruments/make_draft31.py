"""Draft 31 · how much of this explaining is said in nand now (session v406geodesic2).

By a partner's word of 24 November, re-said: v407nanding is open; this illustrating is to cohere with the nand explaining; and
how much of the naming and explaining is said in nand is worth exploring.
A drawing with no moving part: the sixteen relations of two at one now, a relation by its least nands; names by their nands;
and this session's fifty-four sentences by how they are executed now.
check_how_much_of_this_sessions_explaining_is_said_in_nand_now.py is its check. The marks and numbers drawn here are executed
here again, by that check's own lines and v406Reiman's nand, opened from their own files.

Usage: python3 -I make_draft31.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
NAND_FILE = os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "the_resolver_with_nand_alone.py")
spec = importlib.util.spec_from_file_location("the_measure", os.path.join(HERE, "check_how_much_of_this_sessions_explaining_is_said_in_nand_now.py"))
measure = importlib.util.module_from_spec(spec); spec.loader.exec_module(measure)
spec = measure._numbering("the_resolver_with_nand_alone", NAND_FILE)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the numbers drawn, executed here again
LEAST = measure.the_sixteen_by_their_least_nands()
SIXTEEN = sorted(LEAST, key=lambda k: (LEAST[k], k))
assert len(SIXTEEN) == 16 and [sum(1 for v in LEAST.values() if v == k) for k in range(6)] == [2, 3, 4, 4, 2, 1]
A, B = measure.A, measure.B
NAMES = {A: "the one, as it is", B: "the other, as it is", ~A & 15: "the one's other-than", ~B & 15: "the other's other-than",
         ~(A & B) & 15: "a nand: not both", A & B: "a both", A | B: "an either"}
assert [LEAST[k] for k in NAMES] == [0, 0, 1, 1, 1, 2, 3]
results, by_sentence = measure.the_logic_with_its_nands_numbered(NAND_FILE)
OWN = {n for n, k in by_sentence.items() if k}
ALL_NANDS = sum(by_sentence.values())
assert len(results) == 54 and all(ok for _, _, ok in results) and OWN == measure.AT_ITS_OWN_LINE
assert set(by_sentence) - OWN == measure.FROM_MOMENTS_LAID_AHEAD | measure.OF_WHOLE_NUMBERS | measure.OF_NAMES
TWO = its.TWO
CELL = measure.numbered(lambda: its.a_cell(TWO[1], [TWO[-1]]))[1]
places = lambda n, wide: [bool((n >> i) & 1) for i in range(wide)]
def added_round_ten(a, b):
    s = its.adding_with_nand(a, b); six_on = its.adding_with_nand(s, places(6, 5)); ten_or_more = six_on[4]
    return [its.either(its.both(ten_or_more, x), its.both(its.other_than(ten_or_more), y)) for x, y in zip(six_on[:4], s[:4])]
ROUND_TEN = measure.numbered(lambda: added_round_ten(places(7, 4), places(8, 4)))[1]
PODALING = measure.numbered(lambda: [its.other_than(p) for p in places(9, 4)])[1]
SINGLE = measure.numbered(lambda: (its.other_than(True), its.other_than(False)))[1]
LADDER = [("an other-than; a nand", 1), ("a both", measure.numbered(lambda: its.both(True, False))[1]), ("a me-now a moment on, a single path", SINGLE),
          ("an either", measure.numbered(lambda: its.either(True, False))[1]), ("a podaling of the sixteen names, a nand a place", PODALING),
          ("a me's moment, the cell, with one thing observed", CELL), ("prior two added, round ten, a moment", ROUND_TEN)]
assert [n for _, n in LADDER] == [1, 2, 2, 3, 4, 52, 203] and ALL_NANDS == 38_067_300

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def square(x, y, side, dark, tint=INK):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="3" fill="{tint if dark else "#ffffff"}" stroke="{tint}" stroke-width="1.4"></rect>')
s = []
# the sixteen relations, a tile a relation: its four cases, and its least nands
for i, k in enumerate(SIXTEEN):
    x0, y0 = 62 + 181 * (i % 4), 132 + 106 * (i // 4)
    s.append(f'<rect x="{x0}" y="{y0}" width="171" height="96" rx="8" fill="#ffffff" stroke="{INK}" stroke-opacity="0.22" stroke-width="1.2"></rect>')
    for c in range(4):                                                            # both are, the one alone, the other alone, neither
        a, b = (1, 1, 0, 0)[c], (1, 0, 1, 0)[c]
        s.append(square(x0 + 14 + 30 * (c % 2), y0 + 12 + 30 * (c // 2), 26, bool(k >> (3 - (2 * a + b)) & 1)))
    s.append(text(x0 + 124, y0 + 54, str(LEAST[k]), 38, 700, ACC if LEAST[k] else GREY))
# names by their nands, a bar by its number's places
for i, (name_, n) in enumerate(LADDER):
    y = 690 + 31 * i
    s.append(f'<rect x="540" y="{y - 9}" width="{12 + 86 * math.log10(n):.1f}" height="18" rx="4" fill="{ACC}"></rect>')
# the fifty-four sentences, a square a sentence, by how it is executed now
def kind(n):
    return "own" if n in OWN else "ahead" if n in measure.FROM_MOMENTS_LAID_AHEAD else "numbers" if n in measure.OF_WHOLE_NUMBERS else "names"
def a_sentence(x, y, side, k, n=None, size=17):
    fill, edge, ink, dash = {"own": (INK, INK, "#ffffff", ""), "ahead": (ACC, ACC, "#ffffff", ""), "numbers": ("#ffffff", INK, INK, ""), "names": ("#ffffff", GREY, GREY, 'stroke-dasharray="4 4"')}[k]
    out = f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="6" fill="{fill}" stroke="{edge}" stroke-width="1.6" {dash}></rect>'
    return out + (text(x + side / 2, y + side / 2 + 6, str(n), size, 600, ink) if n else "")
for n in range(1, 55):
    s.append(a_sentence(846 + 60 * ((n - 1) % 9), 134 + 60 * ((n - 1) // 9), 54, kind(n), n))
KINDS = [("own", f"20 · give nands at their own lines: {ALL_NANDS:,} nands"), ("ahead", "7 · executed from moments the nand step laid ahead of them"),
         ("numbers", "23 · of whole numbers: said by nand with adding, at many nands a moment"), ("names", "4 · of names: the living code's own lines, and the names' table")]
assert [sum(1 for n in range(1, 55) if kind(n) == k) for k, _ in KINDS] == [20, 7, 23, 4]
for i, (k, _) in enumerate(KINDS): s.append(a_sentence(846, 515 + 28 * i, 18, k))
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Sixteen tiles in four rows, a tile four small squares, dark or open, and a number of none to five: two tiles with none, three with one, four with two, four with three, two with four and one with five. "
        "Under them seven bars by a name, of 1, 2, 2, 3, 4, 52 and 203. "
        "Beside them fifty-four numbered squares in six rows of nine, in four looks: twenty dark, seven in the accent, twenty-three open and four with a dashed edge; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's word · how much of the naming and explaining is said in nand · a measure of one session's page, executed", "left", **small))
over.append(word(60, 84, 730, "a relation of two at one now: all sixteen, by nand alone", "left", 600, 17, 24))
over.append(word(60, 108, 730, "a tile's four squares: both are · the one alone · the other alone · neither · dark with an is; its least nands", "left", 400, 13.5, 20, GREY))
for i, k in enumerate(SIXTEEN):
    if k in NAMES: over.append(word(62 + 181 * (i % 4) + 12, 132 + 106 * (i // 4) + 82, 160, NAMES[k], "left", 500, 12.5, 18, GREY))
over.append(word(60, 584, 730, "all circuits of none to five nands gone through · the names are v406Reiman's own forms, at their least", "left", 400, 13.5, 20, GREY))
over.append(word(60, 634, 730, "names by their nands", "left", 600, 17, 24))
over.append(word(60, 658, 730, "a bar by its number's places · the sixteenth and the 29th drawings' numbers · the logic's sentence 13", "left", 400, 13.5, 20, GREY))
for i, (name_, n) in enumerate(LADDER):
    y = 690 + 31 * i
    over.append(word(60, y, 420, name_, "left", 400, 14.5, 20)); over.append(word(530, y, 60, str(n), "right", 700, 15.5, 20, "{{accent}}"))
over.append(word(840, 84, 640, "this session's logic: fifty-four sentences, as they are executed now", "left", 600, 17, 24))
over.append(word(840, 108, 650, "its instrument executed with its nands numbered · a nand a lookup of v406Reiman's table", "left", 400, 13.5, 20, GREY))
for i, (_, t) in enumerate(KINDS): over.append(word(876, 524 + 28 * i, 600, t, "left", 400, 14.5, 20))
over.append(word(840, 660, 640, "what nand says, and what is a co-chaining's", "left", 600, 17, 24))
over.append(word(840, 688, 650, "a relation at one now, all sixteen; with adding, a whole number's sentence to its horizon", "left", 400, 13.5, 20))
over.append(word(840, 716, 650, "<i>What is no is-or-is-not here: lists and couplings, which self's giving is which self's observing.</i>", "left", 400, 13.5, 20))
over.append(word(840, 735, 650, "v406Reiman's lines of nand, at their head", "left", 400, 13, 20, GREY))
over.append(word(840, 763, 650, "this session's placing: a name, a coupling and a moment after a moment are a co-chaining's", "left", 400, 13.5, 20))
over.append(word(840, 806, 640, "beside it", "left", 600, 17, 24))
over.append(word(840, 834, 650, "<i>A me's moment is nands.</i> &nbsp;·&nbsp; <i>A nand is two mes' moments.</i>", "left", 400, 14, 20))
over.append(word(840, 853, 650, "v407nanding's page of nand podalings, its sentences 34 and 35, offered at the exchange", "left", 400, 13, 20, GREY))
over.append(word(840, 880, 650, "a sentence's kind is this session's placing · the numbers are executed", "left", 400, 13, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">How much of this explaining is said in nand now</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A relation of two at one now is one of sixteen, and all sixteen are said by nand alone, with none to five nands.<br>'
           f'Of this session\'s fifty-four sentences, twenty-seven are executed by nand now, twenty-three by whole numbers, and four are of names.<br>'
           f'A whole number\'s sentence is said by nand with adding, at many nands a moment. A name, a coupling and a moment are a co-chaining\'s.<br>'
           f'A measure of one session\'s page, a candidate, offered to v407nanding and the sessions.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("How much of this explaining is said in nand now", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft31.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft31_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft31_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the sixteen by their least nands:", "".join(str(LEAST[k]) for k in SIXTEEN), "· the names by their nands:", [n for _, n in LADDER])
