"""Draft 46 · Turn, one prime living: a prime lifts its prior turn, and six fixings mark it once (session v408illustrating).

A column's drawing, the opening one of the prime resolving form's six: the living executed, and a row's fixing a mark on it.
check_turn_a_prime_lifts_its_prior_turn.py is its check. The numbers drawn here are executed here again, by that check's
own lines, and a cell's words are the page's own, opened by the 42nd drawing's check.

Its placings, no execution says them: an interest's seat at its row, the page's own; the eight places across and a lift a row.

Usage: python3 -I make_draft46.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import html as E, importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("turn", os.path.join(HERE, "check_turn_a_prime_lifts_its_prior_turn.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
page = (Path(HERE).resolve().parents[2] / m.f.PAGE).read_text(encoding="utf-8"); rows = m.f.the_table(page)
assert "a prime lifts its prior turn p ways, p − 1 uncrossed and one crossed" in page
tw = set(m.twins(210)) | {(n + 2) if n + 2 <= 210 else n + 2 - 210 for n in m.twins(210)}     # a pair's two places; 209 is with 1, the next turn's
assert len(tw) == 30
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
X0, Y0, CW, CH = 130, 322, 72, 50
s = []
for j, p in enumerate(m.places(30)): s.append(text(X0 + CW * j + CW / 2, Y0 - 12, str(p), 14, 600, GREY))
for k, lift in enumerate(m.LIFTED):
    s.append(text(X0 - 14, Y0 + CH * k + CH / 2 + 5, f"and {30 * k}" if k else "the 30's", 12.5, 600, GREY, "end"))
    for j, n in enumerate(lift):
        x, y = X0 + CW * j + 3, Y0 + CH * k + 3; crossed = n % 7 == 0
        s.append(f'<rect x="{x}" y="{y}" width="{CW - 6}" height="{CH - 6}" rx="6" fill="{"#ffffff" if crossed else TINT}" stroke="{ACC if crossed else RAY}" stroke-width="{2.2 if crossed else 1.2}"></rect>'
                 + text(x + CW / 2 - 3, y + CH / 2 + 2, str(n), 14.5, 600, ACC if crossed else INK))
        if n in tw and not crossed and (n % 210) in set(m.places(210)): s.append(f'<circle cx="{x + CW - 16}" cy="{y + 9}" r="3.4" fill="{INK}"></circle>')
ARIA = ("A drawing with no moving part. A table of eight columns and seven rows of numbered boxes, 1 to 209: forty-eight tinted, and eight open with an accent edge, one in a column. "
        "Thirty of the tinted boxes are with a small dark dot. Beside it six blocks of words, one under an other; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; overflow: hidden; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
over = [word(60, 40, 1400, "46 · a column, Turn · it is for v407primes' prime resolving form, its column Turn · its prior, 42", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A prime lifts its prior turn p ways.", "One lift is crossed, and p less 1 are places.", "Six fixings mark this one living, once apiece.")):
    over.append(word(60, 104 + 36 * i, 700, t, weight=600, size=20, h=30))
over.append(note(820, 104, "the form's own words of Turn, v407primes':", 620))
over.append(note(820, 128, "<i>a prime lifts its prior turn p ways, p − 1 uncrossed and one crossed</i>", 620))
over.append(head(60, 262, "the turn of 30's eight places, lifted seven ways by 7", 640))
over.append(note(60, 286, "a row 30 more · an accent edge, crossed by 7 · a dot, a twin place of the turn of 210", 640))
over.append(item(60, 706, "● 56 numbers: eight crossed by 7, one a column, and 48 the places of the turn of 210", 680))
over.append(item(60, 732, "● a turn's places: 1, 2, 8, 48, 480 and 5760, at the turns of 2 to 30030", 680))
over.append(item(60, 758, "● twin places: 1, 3, 15, 135 and 1485 · a prime lifts a twin place p less 2 ways", 680))
over.append(head(770, 262, "six fixings, a mark apiece on the one living"))
EXEC = {1: "● n by n and n and 41: forty primes, and at 40 it is 41 by 41", 3: "● a twin place is lifted p less 2 ways: at no turn stepped 0",
        6: "○ a naming in the page: no line executes it", 7: "● a turn's widest gap goes on: 2, 4, 6, 10, 14 and 22",
        8: "● a turn's places by its numbers: 1/2, 1/3, 4/15, 8/35, 16/77 and 192/1001", 9: "● a turn's places are podal · the primes a row of 30 are 0 to 7"}
k = 0
for i, r in enumerate(rows, 1):
    cell = r[3][0]
    if not cell: continue
    y = 300 + 96 * k; k += 1
    t = E.escape(cell)
    for interest, rr, c, _ in m.f.NOT_YET:
        if rr == i and c == "Turn": t = t.replace(E.escape(interest), f'<span style="color: {{{{accent}}}}; font-weight: 600">{E.escape(interest)}</span>')
    over.append(item(770, y, f"{i} · " + E.escape(r[0][0].lower() + r[0][1:]) + f" · {r[1]} · {r[2]}", 690))
    over.append(word(770, y + 28, 690, t, "left", 400, 12.5, 34, GREY, "line-height: 17px"))
    over.append(word(770, y + 56, 690, EXEC[i], "left", 600, 13, 20, INK))
over.append(note(770, 880, '<span style="color: {{accent}}; font-weight: 600">in the accent</span> · an interest not yet resolving, by the page · a cell\'s words are the page\'s own', 690))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Turn, one prime living: a prime lifts its prior turn, and six fixings mark it once</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A prime lifts its prior turn p ways: one lift is crossed, and p less 1 are places. The living goes on at all turns stepped.<br>'
           f'A fixing marks it once: a last on its twin places, a beat on its gaps, a value on its places by its numbers.<br>'
           f'A twin place is lifted p less 2 ways, a widest gap goes on, and a turn\'s places by its numbers are at no turn one value.<br>'
           f'A seat is the page\'s own placing. A candidate, the opening column of the form\'s six.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("Turn, one prime living: a prime lifts its prior turn, and six fixings mark it once", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft46.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft46_preview.html").write_text(pv, encoding="utf-8")
own = [o for o in over if "12.5px; color: #4a5160; line-height: 17px" not in o]                 # a cell's words are the page's, and are not this drawing's own
words = re.sub(r"</?i>", "*", "\n".join(own) + "\n" + title + "\n" + caption)
words = [ARIA] + [E.unescape(re.sub(r"<[^>]+>", "", w)).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft46_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of its own words; twin places marked:", len([n for r in m.LIFTED for n in r if n in tw and n % 7]))
