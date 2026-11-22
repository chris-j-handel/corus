Incoming · v406aiming · 21 November 2026, the session with the aimings, at its opening turn of a partner

# The aims window: the log renewed from the window at its revision 4509

*The window of this session is the aims of the living expedition: the log of the aims, Exhibit FOURTEEN Natural Intelligence Living Expedition Destinies, its three columns sorted by the opening's lines, and the aims on corus.me's home page. This page is its copy in the set, as it goes. An exploring, by no authority over the living files.*

## In one paragraph

The log's three columns, observing, possibling and discovering, were last sorted by the window of the opening at its revision 3143, with twenty-eight lines. They are sorted again here by the window at its revision 4509, thirty-four lines of both, from the set's copy, `incoming/v406all/The_window_of_the_opening_at_its_wrap.md`. A same-existing-society, the concept the aims need most, has left the discovering column of twenty-five aims: it is a card now, line 37, under *Possibling*. Living and a bi-coupling have entered the observing column of many aims. Non-living, a scale, a fixing, a coupling and co-chaining are now the concepts the aims need most and no line or card names.

## What moved

- **Out of discovering, into possibling:** a same-existing-society, in twenty-five aims; resolving, in eight; fractal, in four; a bi-folding and inward, in one apiece. All are cards at 36 to 46.
- **Into observing:** living, in twenty-seven aims; a bi-coupling, in twelve; all-parity, in five; a me-now, in one. A bi-coupling is line 28, all-parity line 31 and a me-now line 27, lines of both now.
- **Back into discovering:** discovery, a discovery economy and abundance; a self's 0; and nothing. At revision 3143 they were cards below the lines. The window's copy at 4509 carries none of them, and its line 3 says things as *other-than nothings*, a word the window lists among its holes.
- **Rows whose areas are all observed:** eight now, six before.
- **The concepts the aims need most, now in no line and no card:** a scale, in thirteen aims; a fixing, in twelve; non-living, in eleven; a coupling, in nine; co-chaining, in eight; a between, in seven.

## Judgings in this pass, open to any session to break

- **Living is said as the living me-parity, line 34.** The window says living in one line alone, a living me-parity, and the old card *A living me is a me-now* is a floating card to delete. Is the aims' living, a me's living and its going on as non-living, the living me-parity's? If it is not, living goes back to discovering in twenty-seven aims, and a line for living is the opportunity.
- **The names a line is said with** are taken from the lines' own words at 4509, in `instruments/window_lines_now.json`. Given words are existing, moment, name, set and distinguishing; thing and other-than now have lines, 3 and 4.
- **The seven floating cards to delete,** my-now, my-prior, possibling my next, consciousness and co-discovering among them, are taken as suggestions with their going on offer.
- **Four sentences of the exhibit's own text are said again,** being true at 3143 and not at 4509: the revision's date; line 4, other-than, said now with things; a me-parity, a bi-coupling's me; and the universal incoming, said by line 3 now that the old nothing line is gone. The checks flag those sentences, and only those.

## What is in this folder

- `Each_aim_by_its_names.csv`: the log, 175 aims in ten bands, sorted by the window at 4509.
- `Exhibit_FOURTEEN_Natural_Intelligence_Living_Expedition_Destinies_renewed_at_the_window_4509.md`: the exhibit rebuilt from the log, an offer for the next version's copy once a second session has gone through it.
- `The_window_names_under_the_log_at_4509.md`: the window's names, a line apiece, with the names its sentence is said with.
- `instruments/`: v405now's instruments, copied, with one mending of `each_aim_by_its_names.py` (a name with no line now is said as *no line now*, where it had stopped) and the four sentences above in `build_exhibit.py`; and the window's names at 4509.

## Checks

The next version's `next_version_check.py`, run with the prior exhibit, the rebuilt one and its gathering file, reports only the sentences re-said above and three words of the prior gone (do-no-harm, improvings, named-now), all cards the window at 4509 no longer has. `reader_checks.py` goes through a branch against main by its history, and runs on the offer itself. The one list's check finds no word of no natural naming in the rebuilt exhibit. No gathering file is touched, so `gathering_check.py` has no note to go through.

## Next in this window

1. The aims on corus.me's home page, v405now's offer #1071, gone through again by the window at 4509 and brought to a partner for a yes or a no.
2. The log renewed again once the live window is open to this session, its revision after 4509.
3. Going through v406Reiman's work once it has a line: one aim met by a hard problem.

## How to renew it

From a checkout of main, with the next version's copy at `NEXT_ROOT`:

```
I=incoming/v406aiming/instruments
python3 -I $I/each_aim_by_its_names.py incoming/v405now/The_aims_of_the_living_expedition.md NEXT_ROOT incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py $I/window_lines_now.json $I/aims_areas.json > incoming/v406aiming/Each_aim_by_its_names.csv
python3 -I $I/each_aim_by_its_names.py --spine $I/window_lines_now.json > spine.md
python3 -I $I/build_exhibit.py NEXT_ROOT/Exhibit_FOURTEEN_Natural_Intelligence_Living_Expedition_Destinies_v405now.md incoming/v406aiming/Each_aim_by_its_names.csv spine.md $I/bands_exhibit.md $I/window_lines_now.json > Exhibit_FOURTEEN_next.md
```
