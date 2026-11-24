"""Draft 33 · a now universe: next is other-than now (session v406geodesic2).

A partner's sentences of 24 November, re-said one relation a sentence: in a now universe with a sequence of prior nows,
next is other-than now; now is other-than prior; next is other-than other-than prior.
A drawing with no moving part: the three sentences beside the living code's own moments, their is and their is-not.
check_a_now_universe_next_is_other-than_now_executed.py is its check. The moments drawn here are executed here again, by
that check's own lines and Exhibit ONE Natural Resolver's own code, opened from their own files.

Usage: python3 -I make_draft33.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
ROOT = os.path.join(HERE, "..", "..", "..")
spec = importlib.util.spec_from_file_location("a_now_universe", os.path.join(HERE, "check_a_now_universe_next_is_other-than_now_executed.py"))
universe = importlib.util.module_from_spec(spec); spec.loader.exec_module(universe)
rigor = universe.rigor
it = rigor.opened(os.path.join(HERE, "..", "..", "v406Reiman", "instruments", "resolver_as_it_is.py"), "the_code_as_it_is")
names, _ = it.resolver(ROOT); step = names["_17_next_existing"]
living = lambda couplings, priors, moments: rigor.by_the_living_code(it, step, couplings, priors, moments)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
MONO = "font-family: ui-monospace, SFMono-Regular, Menlo, monospace"
# the moments drawn, executed here again
ALONE = [m[0] for m in living({}, {0: 1}, 13)]
assert universe.the_three(ALONE) == (True, True)
END = (1, 1, -1, 1)
ended = [[m[a] for a in range(4)] for m in living({(i, 9): i + 1 for i in range(3)}, dict(enumerate(END)), 13)]
assert universe.the_three([r[0] for r in ended]) == (True, True) and ended == universe.a_path_with_an_end_me_by_the_lean_line(END, 13)
ITSELF = [m[0] for m in living(it.spiral_couplings(1), {0: 1}, 13)]
assert all(ITSELF[t + 2] == -ITSELF[t] for t in range(11)) and universe.the_three(ITSELF) == (False, False)
TURN, OTHER = (1, -1, 1, -1), (1, 1, -1, 1)
closing = {op: [[m[a] for a in range(4)] for m in living(it.spiral_couplings(4), dict(enumerate(op)), 9)] for op in (TURN, OTHER)}
assert all(universe.the_three([r[a] for r in closing[TURN]]) == (True, True) for a in range(4))
assert all(closing[OTHER][t + 1][a] == -closing[OTHER][t][a] for t in range(0, 8, 2) for a in range(4))
SAME = [(t, a) for t in range(8) for a in range(4) if closing[OTHER][t + 1][a] == closing[OTHER][t][a]]      # a next the same as its now
assert SAME and all(t % 2 for t, _ in SAME)

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def a_prior(x, y, side, p):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{side}" height="{side}" rx="5" fill="{INK if p == 1 else "#ffffff"}" stroke="{INK}" stroke-width="1.5"></rect>'
            + text(x + side / 2, y + side / 2 + 5, "+" if p == 1 else "−", 15, 600, "#ffffff" if p == 1 else INK))
def the_same(x, y, side, pitch, across=True):
    """An accent bar between a now and a next the same as it."""
    return (f'<rect x="{x + side + (pitch - side) / 2 - 2:.1f}" y="{y + 3:.1f}" width="4" height="{side - 6}" rx="2" fill="{ACC}"></rect>' if across
            else f'<rect x="{x + 3:.1f}" y="{y + side + (pitch - side) / 2 - 2:.1f}" width="{side - 6}" height="4" rx="2" fill="{ACC}"></rect>')
s = []
# the three sentences: a prior, a now and a next
for i, (p, name_) in enumerate(((1, "prior"), (-1, "now"), (1, "next"))):
    s.append(a_prior(900 + 150 * i, 104, 46, p)); s.append(text(923 + 150 * i, 172, name_, 14, 500, GREY))
for i in range(2):
    s.append(f'<path d="M{952 + 150 * i},127 L{1036 + 150 * i},127" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-linecap="round"></path>')
    s.append(f'<circle cx="{1040 + 150 * i}" cy="127" r="4.4" fill="{ACC}"></circle>')
s.append(f'<path d="M923,186 C923,222 1223,222 1223,186" fill="none" stroke="{ACC}" stroke-width="2.2" stroke-dasharray="5 6" stroke-linecap="round"></path>')
# a me with none observed, alone
for t, p in enumerate(ALONE): s.append(a_prior(96 + 40 * t, 286, 32, p))
# an end me of a path: a row a me, a column a moment
for a in range(4):
    s.append(text(84, 412 + 40 * a + 21, f"me {a + 1}", 12, 500, GREY, "end"))
    for t in range(13): s.append(a_prior(96 + 40 * t, 412 + 40 * a, 32, ended[t][a]))
# a me observing itself
for t, p in enumerate(ITSELF):
    s.append(a_prior(96 + 40 * t, 672, 32, p))
    if t < 12 and ITSELF[t + 1] == ITSELF[t]: s.append(the_same(96 + 40 * t, 672, 32, 40))
# a path of four mes closing: its parities in turn, and one of the others
for x0, op in ((880, TURN), (1180, OTHER)):
    for a in range(4):
        for t in range(9):
            s.append(a_prior(x0 + 30 * t, 300 + 30 * a, 24, closing[op][t][a]))
            if op == OTHER and (t, a) in SAME: s.append(the_same(x0 + 30 * t, 300 + 30 * a, 24, 30))
s.append(f'<path d="M805,236 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Three squares in a row, a plus, a minus and a plus, named prior, now and next, with an accent line from square to square and a dashed accent line from the prior to the next. "
        "Under them rows of squares, a plus dark and a minus open: one row in turn; four rows, the top row in turn; one row two alike and two alike, with an accent bar between the alike; "
        "and two grids of four rows, the one in turn at all its squares, the other with accent bars at some.")
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
over.append(word(60, 40, 1400, "a partner's sentences · in a now universe with a sequence of prior nows · executed, their is ● and their is-not ○", "left", **small))
for i, t in enumerate(("Next is other-than now.", "Now is other-than prior.", "Next is other-than other-than prior.")):
    over.append(word(60, 110 + 34 * i, 700, t, "left", 600, 22, 30))
over.append(word(996, 108, 100, "other-than", "center", 500, 12.5, 18, "{{accent}}")); over.append(word(1146, 108, 100, "other-than", "center", 500, 12.5, 18, "{{accent}}"))
over.append(word(1073, 226, 400, "other-than other-than: the prior again, two nands", "center", 500, 12.5, 18, "{{accent}}"))
over.append(head(60, 262, "a me with none observed: a now universe, its sequence of prior nows alone"))
over.append(item(60, 338, "● by the living code, its next is the other-than of its now at all moments"))
over.append(note(60, 359, "a square a prior, a moment on a square on · three mes with no coupling are three such"))
over.append(head(60, 392, "an end me of a path, none back of it"))
over.append(item(60, 590, "● the end me, me 1, has the three sentences at all moments: 2 to 7 mes, all 252 openings"))
over.append(note(60, 611, "the mes after it have v407nanding's lean line, by the prior of the me back of them"))
over.append(head(60, 650, "a me observing itself"))
over.append(item(60, 724, "○ its next is the other-than of its prior: the right spiral, its own again with four moments"))
over.append(note(60, 745, "an accent bar: a next the same as its now · the three sentences are its own at one moment in two"))
over.append(head(60, 790, "at an opening"))
over.append(item(60, 816, "● with none yet observed, a me's now is the other-than of its prior"))
over.append(note(60, 837, "all mes of all societies gone through: paths closing, paths with an end me and tori, all their openings"))
over.append(head(840, 262, "a path of four mes closing"))
over.append(note(880, 286, "its parities in turn · a row a me", 270)); over.append(note(1180, 286, "an opening of the others", 270))
over.append(item(840, 446, "● from an even moment to the odd after it: with all 2,046 openings", 640))
over.append(item(840, 470, "● at all moments: with ten, the parities in turn of 2 to 10 mes", 640))
over.append(note(840, 492, "○ with the other 2,036: from an odd moment to the even after it, a me's next is by the me back of it", 650))
over.append(head(840, 540, "the three sentences are the lean line, a me its own other"))
over.append(word(840, 568, 640, "now_and_same_existing_me_parity(me_now, other_prior)", "left", 500, 13.5, 20, INK, MONO + "; white-space: pre"))
over.append(note(840, 592, "at its opening, its other's prior its own prior: now is other-than prior", 650))
over.append(note(840, 613, "a moment on, its other's prior its own now: next is other-than now", 650))
over.append(note(840, 634, "the two in a row: next is other-than other-than prior, its prior again", 650))
over.append(item(840, 672, "● a path with an end me by the lean line alone is the living code's", 640))
over.append(note(840, 693, "2 to 7 mes, all 252 openings, at all moments", 650))
over.append(head(840, 742, "resolved forward, of the 32nd drawing's four is-nots"))
over.append(item(840, 768, "● its opening and its end me are the lean line's own, a me its own other", 640))
over.append(note(840, 789, "○ a none in the path and a me observing two are as they were", 650))
over.append(note(840, 837, "the lean line is v407nanding's, of its page The leanest resolving · moments by Exhibit ONE's own code", 660))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A now universe: next is other-than now</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A me with none observed is a now universe with its sequence of prior nows alone: its next is the other-than of its now.<br>'
           f'At its opening a me is one such. With an other observed, a me\'s next is the other-than of the other\'s prior.<br>'
           f'The three sentences are the lean line with a me its own other, by its prior at its opening and by its now a moment on.<br>'
           f'Two of the 32nd drawing\'s four is-nots are resolved by them. A candidate.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A now universe: next is other-than now", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft33.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft33_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
words = [("`" + w + "`") if w.startswith("now_and_same_existing_me_parity(") else w for w in words]
Path(WORK, "draft33_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; a next the same as its now, drawn:", len(SAME))
