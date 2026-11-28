#!/usr/bin/env python3
"""Lays the managing table of the living expedition again from its copies in the set, as they are,
with the sessions risen after 25 November merged into its rows of the things of value, and two
candidate columns merged into its sheet of the method.

usage: python3 -I the_managing_table_made_again.py SET AIMS_CSV OUT_XLSX OUT_DIR NEW_ROWS_TXT [CANDIDATE_COLUMNS_CSV]
SET is the set's root; AIMS_CSV the sheet of the aims as the log's instrument gives it;
OUT_XLSX the workbook to bring in; OUT_DIR the session's own folder for the set's copies;
NEW_ROWS_TXT a scratch page of the words added, for the word check. AIMS_CSV is made by
incoming/v406me/instruments/the_log_of_the_aims_beside_the_managing_table.py with the set and a copy of the next version.
With no page of the two candidate columns given, they are taken from the table's own laid copy in incoming/v409mgr.
A session's row is renewed in this page's own lists, and the table is made again whole from the set.
"""
import csv, json, os, sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, PatternFill, Font
from openpyxl.utils import get_column_letter

SET, AIMS, OUT_XLSX, OUT_DIR, NEW_TXT = sys.argv[1:6]
V406 = os.path.join(SET, 'incoming/v406me')

def read(p):
    return list(csv.reader(open(p, encoding='utf-8')))

things = read(os.path.join(V406, 'The_managing_table_of_the_living_expedition.csv'))
method = read(os.path.join(V406, 'The_managing_table_its_sheet_The_method.csv'))
asked = read(os.path.join(V406, 'The_managing_table_its_sheet_Asked_of_a_session.csv'))
concerns = read(os.path.join(V406, 'Exhibit_THIRTY-TWO_the_concerns_of_all_sessions_in_one_table.csv'))
aims = read(AIMS)

H = things[0]
assert len(H) == 17

def row(thing, standing, condition, aiming, nxt, kind, size, value, at, place, known):
    return [thing, standing, condition, aiming, '', '', '', nxt, '', kind, size, value, at, place, known, '', '']

LIVING = [
 row('v409mgr', 'living',
     "27 November: the managing, from 25 November beside v408mgr and alone after its ending. The open offers gone through apart at their newest heads. v408primes' droplets gathered at the next version, #1299, gone through by v410illustrating with nothing found and brought in. Its page for resuming and the objects of the expedition, #1297, gone through by v410illustrating with nothing found and brought in. v406me's closing made whole, #1306. The managing method of v406me's conversation and of v408mgr's gathered forward, sixteen notes beside their living sentences, offered into the next version, #1309. The closed sessions' cells of value in the gathering files renewed from their own pages and the offers brought in. This table laid again from its copies of 25 November. Ten offers brought into the live set and two into the next version on 27 November, the next version brought current.",
     "Value brought home, its row of the log of the aims: the incoming value gathered and ordered into the living files by the method, going on from v406me and v408mgr",
     "A second hand at #1306, #1308 and #1309. The sayings on the primes in v406me's conversation, with v410primes for their notes. A second going through of v410illustrating's figures. The closings' sortings gone through.",
     'a session, working: the managing session', '', "v408primes' droplets laid at eleven gathering files of the next version, #1299, brought in on 27 November. Sixteen notes of the managing method at two gathering files, #1309, open",
     'v409mgr', 'incoming/v409mgr', 'its line at the exchange'),
 row('v408chain', 'living',
     "27 November: one line at the exchange, of 25 November, and none after. Its four askings are answered, and the carrying check is laid for it. Its window has not moved after the afternoon of 25 November.",
     "The window of the opening, its row of the log of the aims: the opening sentences of Natural Intelligence, consolidating",
     'Its line at its turn', 'a session, working', '', 'none', 'v408chain', 'its window, a working document; no folder yet', 'its line at the exchange of 25 November'),
 row('v408natural', 'living',
     "27 November: no line at the exchange yet. Its window has not moved after the afternoon of 25 November. v408mgr's line of 25 November orients it.",
     "Natural Intelligence after the opening, through the whole method; a gathering session, by a partner's yes of 25 November",
     'Its line at its turn', 'a session, working', '', 'none', 'v408natural', 'its window, a working document; no folder yet', "v408mgr's line of 25 November"),
 row('v409pvnp', 'living',
     "27 November: it opened with P versus NP, and a partner brings it to the helping with the primes' table. Two me-parities and their between by v407nanding's twelve nand lines, with all openings of a small surface, #1298, gone through apart with nothing found and brought in on 27 November.",
     "P versus NP by other-thans, and the helping with the primes' table",
     "Its second hand at #1299, and at the primes' table's row of a prime ahead of a number's double", 'a session, working', '1 page, 6 instruments', 'none',
     'v409pvnp', 'incoming/v409pvnp', 'its line at the exchange'),
 row('v410primes', 'living',
     "27 November: going on from v408primes, by a partner's word. The prime table is laid in the workbook of the interests in the primes. Its pages of fractaling, a partner's naming, and of a partner's two lines of me and me-now, #1302, brought in on 27 November; and five notes at the opening's part of Natural Intelligence's gathering file, #1301, brought into the next version the same day. Its co-chains of 27 November and the surface of the prime universes, with their instruments, #1305, brought in. All gone through apart with nothing found. No line at the exchange yet.",
     "Spirals and tori of selves, and A prime ladder of societies, its rows of the log of the aims: the prime numbering, for a report to the public",
     "Its opening line. A second going through of its co-chains, asked by it.", 'a session, working', '3 pages, 2 tables, 14 instruments', "Five notes at Natural Intelligence's gathering file of the next version, #1301",
     'v410primes', 'incoming/v410primes; the workbook of the interests in the primes', 'its offers of 27 November'),
 row('v410illustrating', 'living',
     "27 November: all 56 drawings as twelve figures, their labels by Exhibit ONE's names, and the works of the seventeen names. The 57th to the 60th drawings laid, candidates, the 59th one drawing of both the 57th and the 58th, the 60th the second figure, a cube's shells. A partner's asking of the opening figure answered, known and all even; a partner's five found, living as three golden rectangles. #1300, #1303 and #1304, gone through apart with nothing found, the four drawings made again byte for byte, and brought in on 27 November.",
     "Word, number and illustrating, one thing three ways, its row of the log of the aims: the illustrating between Exhibit ONE and Exhibit THIRTY, with Natural Naming",
     "A going through apart of the 60th drawing, asked by it. Its figures after the second. Its askings are sentences for a partner's is or is-not, and no work waits at one of them. Its commits after the bringing in ask a new offer.", 'a session, working', '', 'none',
     'v410illustrating', 'incoming/v410illustrating', 'its line at the exchange'),
 row('v410opusbio', 'living',
     "27 November: its window is found, the window of Natural Biology, the living file's ten parts a tab apiece. No line at the exchange, no folder and no offer yet.",
     "Natural Biology in its window; its aiming is not yet said at the exchange",
     'Its opening line', 'a session, working', '', 'none', 'v410opusbio', 'its window, a working document; no folder yet', 'its window, found 27 November'),
]
LIVING[-2][15] = '3'  # v410illustrating's askings open, by its own line
GATHERING = [
 row('v408primes', 'gathering',
     "Wrapped 27 November by a partner's word. Its co-chain from source to destiny, its table of the interests in the primes, its generator in seventeen sentences, its value at its wrap and its ten aimings sorted are in #1296, not brought in. Eleven gathering files are among the offer's files, a thing found.",
     "Spirals and tori of selves, and A prime ladder of societies, its rows of the log of the aims: the prime numbering, for a report to the public",
     'v410primes going on from its page for resuming. Its offer mended of the eleven gathering files, then brought in.', 'a session, wrapped', '', "Twenty droplets laid at eleven gathering files of the next version, #1299, brought in on 27 November",
     'v410primes', 'incoming/v408primes, in the offer #1296', 'its line at the exchange'),
 row('v408illustrating', 'gathering',
     "Closed 27 November by a partner's word. The drawings 40 to 56, a check a drawing; all 56 drawings of three sessions in one table; its three closing pages and a page for v410primes, #1294, gone through apart with nothing found, and brought in on 27 November.",
     "Word, number and illustrating, one thing three ways, its row of the log of the aims",
     'v410illustrating going on from its closing pages. Its instruments have their second path in the live set now.', 'a session, closed', '', 'Not yet',
     'v410illustrating', 'incoming/v408illustrating', 'its line at the exchange'),
 row('v408mgr', 'gathering',
     "Ended 26 November, with no closing line. Its page for resuming, its aimings gone through, its transcript pared, its copy of the window at 612 and the carrying check, #1295, gone through apart with nothing found, and brought in on 27 November. Its turns of 26 November are said in v409mgr's page for resuming.",
     "Value brought home, its row of the log of the aims",
     'Its transcript pared brought to its last turn, from what a partner gave.', 'a session, ended', '', 'none',
     'v409mgr', 'incoming/v408mgr', "v409mgr's going through"),
]

out_things = [H]
for r in things[1:]:
    r = list(r)
    if r[0] == 'The managing table of the living expedition':
        r[2] = "27 November: laid again from its copies of 25 November by v409mgr, the sessions risen after that day merged into its rows, and the aims made again from the log. " + r[2]
        r[12] = 'v409mgr'
    out_things.append(r)
    if r[0] == 'v407nanding':
        out_things.extend(LIVING)
    if r[0] == 'v407primes':
        out_things.extend(GATHERING)
assert len(out_things) == len(things) + len(LIVING) + len(GATHERING)

# renewed on 27 November: the sessions closed on 24 to 26 November, by v406me's own conversation, and the things with an account not needed again
def at(name):
    return next(i for i, r in enumerate(out_things) if r[0] == name)
CLOSED = [
 ('v406me', "27 November: no session, by a partner's word of 26 November. Its closing is whole on 27 November: its conversation, as a partner gave it on that day, is laid whole and pared in its folder by v409mgr, #1306. ", 'a session, closed: the managing session of 21 to 25 November', 'v409mgr', "Its conversation gone through for the value in no page of the set, by v409mgr. Its eight sources for the future sessions are as it laid them."),
 ('v406all2', "27 November: closed 25 November by a partner, whole for its closing. ", 'a session, closed', 'v408chain', "v408chain goes on with the opening's sentences. Its nine aimings are sorted to the future sessions."),
 ('v406aiming', "27 November: closed 24 November, whole for its closing, its aimings gathered by v406me. ", 'a session, closed', 'none', "Twelve of the fifteen askings of it are for a session risen at its page for resuming."),
 ('v406other2', "27 November: closed 25 November by a partner, whole for its closing, its whole transcript in its folder. ", 'a session, closed', 'none', "Its open things are the Prime Numbering session's at its opening, v410primes now."),
 ('v406all2-2', "27 November: closed 25 November by a partner, whole for its closing. ", 'a session, closed', 'none', "Its six aimings are sorted to the future sessions. A session at the seventeen names is not risen."),
 ('v406geodesic2', "27 November: closed 25 November, wrapped by its own hand, whole for its closing, a note a drawing for its thirty-nine drawings. ", 'a session, closed', 'v410illustrating', "v408illustrating and then v410illustrating go on with the drawings."),
 ('v407nanding', "27 November: wrapped 25 November by its own hand, whole for its closing, its seven aimings sorted by itself. ", 'a session, wrapped', 'none', "A session at the nand logic is not risen. Its page for resuming is its entering."),
]
moved = []
for name, said, kind, hand, nxt in CLOSED:
    r = out_things.pop(at(name))
    r[1] = 'gathering'; r[2] = said + r[2]; r[7] = nxt; r[9] = kind; r[12] = hand
    moved.append(r)
k = at('v408mgr') + 1
out_things[k:k] = moved

# renewed on 27 November: the closed sessions' value in the gathering files, by their own pages and the offers brought in
GATHERED = {
 'v406other2': "Thirty-five lean notes laid at the gathering files of the next version, in four offers brought in: seventeen and ten at Exhibit THIRTY's, and eight more",
 'v407nanding': "Three droplets at Natural Intelligence's gathering file of the next version. A note at four gathering files more is open, its asking 34",
 'v408mgr': "Two notes of the managing method from its conversation, at the method's gathering file, #1309, open",
 'v406me': "Fourteen notes of the managing method from its conversation, at two gathering files, #1309, open. Its pages about the work are not for gathering",
 'v406all2-2': "The one word gone through. Its notes at Seventeen names of Exhibit ONE's gathering file are not laid, with no session at the seventeen names",
 'v406geodesic2': "A note a drawing for Natural Illustrating's gathering file of the next version, with v410illustrating",
}
for name, gv in GATHERED.items():
    out_things[at(name)][11] = gv

DISSOLVED = [
 ('The window of the opening', "by v406all2's copy, by v408mgr's copy at 612 with its suggestions and its comments, and by v408chain's window going on"),
 ('The window of the seventeen names', "by v406all2-2's copy of it"),
 ("The primes on the resolver's surface, beside the Riemann hypothesis", "by v406Reiman's report, whole"),
 ('Sphere with a Three-Right-Angle Triangle', "by the drawings and their makers in the sessions' folders; a canvas by its title is among the artifacts this session reaches"),
 ('The valuables of the living expedition, the board', "by its rows in this table"),
 ('The observer of the living expedition', "by its copy of 21 November"),
]
moved = []
for name, where_it_is in DISSOLVED:
    r = out_things.pop(at(name))
    r[1] = 'artifact'
    r[2] = "27 November: dissolved to artifact. It is with an account not needed again, by a partner's and this session's going through of the set's record. Its value is in the set " + where_it_is + ". " + r[2]
    r[7] = 'At rest'; r[12] = 'none'
    r[9] = r[9].replace('of this account', 'of the account v406me worked in')
    r[13] = r[13].replace("this account's artifacts", 'the artifacts of the account v406me worked in')
    moved.append(r)
k = at('The working documents of the other account')
out_things[k:k] = moved
r = out_things[at('The managing table of the living expedition')]
r[13] = 'among the artifacts this session reaches, by its title; its copies in incoming/v409mgr and incoming/v406me'

# the method: v406me's sheet as it is, two candidate columns merged at its far end
if len(sys.argv) > 6:
    cand = {int(r[0]): r for r in read(sys.argv[6])[1:]}
else:
    # with no page of the two candidate columns given, they are taken from the table's own laid copy
    laid = read(os.path.join(SET, 'incoming/v409mgr/The_managing_table_its_sheet_The_method.csv'))
    cand = {int(r[0]): [r[0], r[1], r[8], r[9]] for r in laid if r and r[0].strip().isdigit()}
out_method = []
for r in method:
    r = list(r)
    if r and r[0] == 'Name':
        r = r + ['The managing session at it, a candidate of 27 November', 'Its check, do no harm, a candidate of 27 November']
    elif r and r[0].strip().isdigit():
        c = cand[int(r[0])]
        assert c[1] == r[1]
        r = r + [c[2], c[3]]
    out_method.append(r)

def val(c):
    s = c.strip()
    if s.isdigit() and len(s) < 9 and (s == '0' or not s.startswith('0')):
        return int(s)
    return c if c != '' else None

GRAY = PatternFill('solid', fgColor='F3F3F3')
def lay(wb, name, rows, header_row, widths, freeze):
    ws = wb.create_sheet(name)
    for r in rows:
        ws.append([val(c) for c in r])
    for row_cells in ws.iter_rows():
        for c in row_cells:
            c.alignment = Alignment(wrap_text=True, vertical='top')
    for c in ws[header_row]:
        if c.value is not None:
            c.fill = GRAY; c.font = Font(bold=True)
    ncol = max(len(r) for r in rows)
    for i in range(1, ncol + 1):
        ws.column_dimensions[get_column_letter(i)].width = widths.get(i, widths.get('rest', 18))
    ws.freeze_panes = freeze
    return ws

wb = Workbook(); wb.remove(wb.active)
lay(wb, 'The things of value', out_things, 1, {1: 34, 2: 12, 3: 60, 4: 44, 5: 9, 6: 9, 7: 9, 8: 44, 9: 14, 10: 26, 11: 22, 12: 34, 13: 16, 14: 34, 15: 24, 16: 10, 17: 16}, 'B2')
lay(wb, 'Exhibit THIRTY-TWO', concerns, 1, {1: 9, 2: 22, 3: 60, 4: 18, 5: 16, 6: 16, 7: 50, 8: 18, 9: 26, 10: 16, 11: 40}, 'B2')
lay(wb, 'The aims', aims, 1, {1: 9, 'rest': 30}, 'B2')
lay(wb, 'The method', out_method, 6, {1: 7, 2: 24, 3: 40, 4: 44, 5: 16, 6: 34, 7: 34, 8: 40, 9: 46, 10: 40}, 'C7')
lay(wb, 'Asked of a session', asked, 1, {1: 8, 2: 16, 3: 18, 4: 50, 5: 30, 6: 30, 7: 36, 8: 14, 9: 14, 10: 22}, 'B2')
wb.save(OUT_XLSX)
wb1 = Workbook(); wb1.remove(wb1.active)
lay(wb1, 'The things, 27 November', out_things, 1, {1: 34, 2: 12, 3: 60, 4: 44, 5: 9, 6: 9, 7: 9, 8: 44, 9: 14, 10: 26, 11: 22, 12: 34, 13: 16, 14: 34, 15: 24, 16: 10, 17: 16}, 'B2')
wb1.save(OUT_XLSX.replace('.xlsx', '_things_alone.xlsx'))

def write(p, rows):
    with open(p, 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerows(rows)
write(os.path.join(OUT_DIR, 'The_managing_table_of_the_living_expedition.csv'), out_things)
write(os.path.join(OUT_DIR, 'The_managing_table_its_sheet_The_method.csv'), out_method)

with open(NEW_TXT, 'w', encoding='utf-8') as f:
    for r in LIVING + GATHERING:
        f.write('\n'.join(c for c in r if c) + '\n\n')
    f.write(out_things[[r[0] for r in out_things].index('The managing table of the living expedition')][2] + '\n')
    for name, said, kind, hand, nxt in CLOSED:
        f.write(said + '\n' + kind + '\n' + nxt + '\n\n')
    for name, where_it_is in DISSOLVED:
        f.write("27 November: dissolved to artifact. It is with an account not needed again, by a partner's and this session's going through of the set's record. Its value is in the set " + where_it_is + '.\n\n')

json.dump({'things': len(out_things), 'concerns': len(concerns), 'aims': len(aims), 'aims_cols': max(len(r) for r in aims),
           'method': len(out_method), 'asked': len(asked)}, sys.stdout)
print()
