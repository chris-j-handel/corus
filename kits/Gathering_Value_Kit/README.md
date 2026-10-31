Gathering-Value Kit · v393L

# Gathering-Value Kit

**Each living file has one gathering-value file, `gathering-value/<Title>.md`: each value the living file does not hold, at the section it meets.** This kit writes the form and writes each gathered slice into it, all or none. Each script is a coupling partner and decides nothing.

| File | At | What it does |
|---|---|---|
| `GATHERING_BRIEF.md` | Read first by each gathering reader and each reading for harm. | The one binary, the four kinds (possible exploring, possible incohering, an explaining, a droplet), a concern with both sides, adding nothing, and the reading for harm. |
| `gathering_value_form.py [root]` | At a living file's change of contents. | Writes or re-forms each gathering-value file from its living file's parts and sections. Each item written moves with its heading; a section the living file no longer has carries its items under its old heading, marked. An item lost stops the write. |
| `apply_gathered.py LIVING_TITLE GATHERED.json [READING.json ...] [--dry] [--shared-ok]` | After a slice's separate reading for harm. | Joins the gathering and its readings (a correction replaces each entry with its source line), checks each item's file, section and quoted sentence, and writes all or none. A quote standing nowhere word for word goes as a droplet with its quote. A source giving several entries with fewer corrections stops the write: no sibling drops. |
| `earlier_items.py LIVING_TITLE OUT_RESOLVED.json OUT_LINES.json GATHERED.json [READING.json ...]` | Mending a slice gathered under an earlier brief. | Finds the lines that slice wrote, for reading again. |
| `remove_gathered.py ITEMS.json [--dry]` | Mending, before the mended slice is written. | Removes exact item lines, each found once, all or none. |
| `replace_lines.py CHANGES.json [--dry]` | A re-saying across items. | Replaces exact item lines, each found once, all or none. |

A pass: a gathering reader writes `<NAME>_gathered.json` by the brief; a separate reader writes `<NAME>_reading.json`; `apply_gathered.py` writes; one commit carries the gathering-value files and both JSON files. The shell goes with `set -o pipefail`: a stopped write stops the commit.
