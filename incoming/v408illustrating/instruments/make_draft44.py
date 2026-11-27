"""Draft 44 · the set: a drawing with its prior, its other-prior, its now and its next (session v408illustrating).

The set's own map, made from its table, a drawing a row: a label a drawing, and four relations.
the_set_labelled_and_related.py is its check. Nothing of a row is said again here: a card's words are the table's own.

Its placings, no execution says them: other-prior at one side, next at the other, and the set between them.

Usage: python3 -I make_draft44.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import html as E, importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_set", os.path.join(HERE, "the_set_labelled_and_related.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
rows, parts = m.the_set(Path(HERE).resolve().parents[2])
drawn = [r for r in rows if r["Drawing"] and r["Drawing"] != "44"]; ahead = [r for r in rows if not r["Drawing"]]; own = next(r for r in rows if r["Drawing"] == "44")
others = []
for r in drawn:
    for o in parts(r["Its other-prior"]):
        label = o.split(" = ")[0]
        if label not in others: others.append(label)
s, over = [], []
def word(x, y, w, h, t, size=12, weight=400, color=INK, align="left", lh=None):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {y:.0f}px; width: {w:.0f}px; height: {h:.0f}px; line-height: {lh or h}px; overflow: hidden; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}">{t}</div>')
LX, LW, LH, MX, MW, MH, RX, RW, RH = 60, 300, 28, 470, 520, 42, 1110, 350, 46
ly = {l: 134 + 36 * i for i, l in enumerate(others)}
my = {r["Drawing"]: 130 + 44.5 * i for i, r in enumerate(drawn)}
brackets = 0
ry = {r["Its name"]: 134 + 64 * i for i, r in enumerate(ahead)}
for l, y in ly.items():
    s.append(f'<rect x="{LX}" y="{y}" width="{LW}" height="{LH}" rx="6" fill="{TINT}" stroke="{RAY}" stroke-width="1"></rect>')
    over.append(word(LX + 12, y, LW - 20, LH, E.escape(l), 12.5, 600))
for r in drawn:
    n, y = r["Drawing"], my[r["Drawing"]]
    for o in parts(r["Its other-prior"]):
        s.append(f'<line x1="{LX + LW}" y1="{ly[o.split(" = ")[0]] + LH / 2}" x2="{MX}" y2="{y + MH / 2}" stroke="{FAINT}" stroke-width="1.2"></line>')
    for x in parts(r["Its next"]):
        if x in ry: s.append(f'<line x1="{MX + MW}" y1="{y + MH / 2}" x2="{RX}" y2="{ry[x] + RH / 2}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="5 5"></line>')
    for x in parts(r["Beside it now"]):
        if int(x) > int(n):
            bx = MX + MW + 6 + 16 * (brackets % 2); brackets += 1
            s.append(f'<path d="M {bx} {y + 14} h 12 V {my[x] + MH - 14} h -12" fill="none" stroke="{ACC}" stroke-width="2.4"></path>')
for r in drawn:
    n, y = r["Drawing"], my[r["Drawing"]]
    s.append(f'<rect x="{MX}" y="{y}" width="{MW}" height="{MH}" rx="8" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></rect>')
    over.append(word(MX + 16, y + 1, 60, 40, n, 24, 600, "{{accent}}"))
    over.append(word(MX + 86, y + 1, MW - 100, 15, E.escape(r["Its name"]), 12, 600, lh=15))
    over.append(word(MX + 86, y + 14, MW - 230, 14, "its view · " + E.escape(r["Its view"]), 11.5, 400, GREY))
    if parts(r["Its prior"]): over.append(word(MX + MW - 154, y + 14, 140, 14, "its prior · " + ", ".join(parts(r["Its prior"])), 11.5, 600, INK, "right"))
    over.append(word(MX + 86, y + 27, MW - 100, 14, "it is for · " + E.escape(r["It is for"]), 11.5, 400, GREY))
for r in ahead:
    y = ry[r["Its name"]]
    s.append(f'<rect x="{RX}" y="{y}" width="{RW}" height="{RH}" rx="6" fill="#ffffff" stroke="{FAINT}" stroke-width="1.3" stroke-dasharray="5 4"></rect>')
    over.append(word(RX + 12, y + 5, RW - 20, 18, E.escape(r["Its name"]), 12.5, 600)); over.append(word(RX + 12, y + 24, RW - 20, 16, "its view · " + E.escape(r["Its view"]), 11, 400, GREY))
    for x in parts(r["Its prior"]):                               # a drawing ahead going on from a drawing ahead
        if x in ry: s.append(f'<path d="M {RX + RW} {ry[x] + RH / 2} h 14 V {y + RH / 2} h -14" fill="none" stroke="{INK}" stroke-width="1.2" stroke-dasharray="5 5"></path>')
oy = 852
s.append(f'<rect x="{MX}" y="{oy}" width="{MW}" height="38" rx="8" fill="{TINT}" stroke="{INK}" stroke-width="1.6"></rect>')
over.append(word(MX + 16, oy, 60, 38, "44", 24, 600, "{{accent}}")); over.append(word(MX + 86, oy + 2, MW - 100, 18, "the set's own map, made from its table", 13, 600))
over.append(word(MX + 86, oy + 19, MW - 100, 16, "its prior · " + ", ".join(parts(own["Its prior"])), 11.5, 400, GREY))
ARIA = ("A drawing with no moving part. Three columns of boxes with words: tinted boxes at one side, large numbered boxes between, and open boxes with a dashed edge at the other side. "
        "Thin lines go from the tinted boxes to the numbered ones, dashed lines from the numbered boxes to the open ones and from an open box to an open box, "
        "and accent brackets pair the numbered boxes; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
head = [word(60, 29, 1400, 22, "44 · the set's own map · it is for the set's table, a drawing a row · its prior, " + ", ".join(parts(own["Its prior"])) + " · made again with a row more", 15, 600, GREY)]
head.append(word(LX, 90, LW, 22, "its other-prior", 17, 600)); head.append(word(LX, 110, LW + 60, 18, "an other session's drawing or page it rests on", 12, 400, GREY))
head.append(word(MX, 90, MW, 22, "the set, now", 17, 600)); head.append(word(MX, 110, MW, 18, "its prior, in a card's own words · an accent bracket, beside it now", 12, 400, GREY))
head.append(word(RX, 90, RW, 22, "its next, ahead", 17, 600)); head.append(word(RX, 110, RW, 18, "a dashed line to a drawing planned", 12, 400, GREY))
foot = [word(60, 902, 1400, 20, "● a next and a prior are one relation, said both ways · beside is said both ways · a drawing with no row, or a relation naming nothing, is a bump of the set's instrument", 13.5, 600)]
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The set: a drawing with its prior, its other-prior, its now and its next</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A drawing is a row of one table, and its label is its number, its name, its view and what it is for.<br>'
           f'Its prior is a drawing of the set it goes on from. Its other-prior is an other session\'s drawing or page.<br>'
           f'Beside it now is a drawing of one concept by an other observing. Its next is a drawing ahead.<br>'
           f'The four are the four of a partner\'s saying: prior, now, next and other-prior. A candidate, made from the set\'s table.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(head + over + foot) + "\n" + title + "\n" + caption
html = page("The set: a drawing with its prior, its other-prior, its now and its next", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft44.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft44_preview.html").write_text(pv, encoding="utf-8")
words = [ARIA] + [E.unescape(re.sub(r"<[^>]+>", "", w)).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", "\n".join(head + over + foot) + "\n" + title + "\n" + caption)).split("\n")]
Path(WORK, "draft44_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; drawings:", [r["Drawing"] for r in drawn], "ahead:", len(ahead), "other-priors:", len(others))
