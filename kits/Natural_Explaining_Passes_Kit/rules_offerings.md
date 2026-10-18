# Resolving an offerings file against its living file

For each item standing at `carry/<file>_Offerings_to_<name>.md` (each droplet, insertlet, concern, possible project, aimed-at paragraph), a reader writes one JSON line to `<file>.jsonl`:

`{"line": <1-based line where the item starts>, "head": "<first 100 chars>", "verdict": "...", "where": "...", "why": "...", "of": <line of the item it duplicates, for DUPLICATE>}`

Verdicts, all or none at each item:
- **CARRIED** — the living file already carries the value; `where` names the section and a short quote.
- **RELEASED** — the item rests on a form the living files release (a released word, an earlier resolver name, a released seating); `why` names the release.
- **DUPLICATE** — another item says the same value; `of` is its line.
- **RISE** — the value is not yet at the living file and coheres with it; the reader also writes the insertlet (an `{"old","new"}` pair at the living file) to `<file>_edits.json`, in natural explaining, entered by `apply_pairs.py`.
- **CONCERN** — two sentences part, or the value needs the person; `why` says why it stands.

Then `offerings_resolve.py OFFERINGS <file>.jsonl "<living file title>" <LIVINGFILE>` archives every item whole with its verdict index at `archive/session_vNNN/offerings_dissolved/` and leaves the concerns standing at the offerings file, each with its reason. Concerns are then resolved with the person, one at a time, and archived by `resolve_concerns.py`.
