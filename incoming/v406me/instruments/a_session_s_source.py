"""A session's source: a page apiece for the eight future sessions, laid from the tables as they are.

python3 -I incoming/v406me/instruments/a_session_s_source.py ROOT        says a session's source and its bumps, a session at a time
python3 -I incoming/v406me/instruments/a_session_s_source.py ROOT OUT    lays the eight pages in OUT
"""
import csv, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
out = sys.argv[2] if len(sys.argv) > 2 else None
me = os.path.join(root, "incoming", "v406me")
V = "incoming/v406me/"

SESSIONS = [
    ("Exhibit ONE, stable form resolver", "Exhibit_ONE_Natural_Resolver_v402mgr.md", "gathering-value/Natural_Resolver.md",
     ["The window of the seventeen names, with its checks: `incoming/v406all2-2`."]),
    ("Exhibit THIRTY, co-chaining, all new learnings", "Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md", "gathering-value/Co-Chaining_Logic_Registry.md",
     ["The boundary claims, twenty-six by six groups: `incoming/v406aiming/The_boundary_claims_as_the_session_gathered_them.csv`.",
      "A learning with no home yet opens here, and goes on to its own file by a partner's word."]),
    ("Illustrating sequential resolving", "Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "gathering-value/Natural_Illustrating.md",
     ["A user's finding, the drawings and the code with their place: `" + V + "A_users_finding_the_drawings_and_the_code_a_thing_with_its_place.csv`.",
      "The drawings of the set: `gathering-value/drawings`. Its kit: `kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit`.",
      "Thirty-nine drawings, a note a drawing: `incoming/v406geodesic2/The_value_of_v406geodesic2_at_its_wrap.md`."]),
    ("Nand logic", None, "gathering-value/Natural_Resolver.md",
     ["It has no living file. Its notes go to Exhibit ONE's gathering file, v406me's placing.",
      "A partner's twelve lines, with their naming: `incoming/v407nanding/The_value_of_v407nanding_at_its_wrap.md`.",
      "The lean line, its is and its is-not: `incoming/v406geodesic2/For_v407nanding_the_lean_line_rigorized_its_is_and_its_is-not.md`."]),
    ("Opening sentences of Natural Intelligence", "Natural_Intelligence_v402mgr.md", "gathering-value/Natural_Intelligence.md",
     ["The window of the opening, its lines from *Now is the existing moment.*: `incoming/v406all2`."]),
    ("Prime Numbering exhibit", None, None,
     ["It has no living file. It is a draft, Exhibit THIRTY-TWO Natural Prime Numbering.",
      "The next draft by its parts, three of six laid: `python3 -I " + V + "instruments/the_next_draft_of_exhibit_thirty-two_by_its_parts.py .`",
      "The one table of all sessions' concerns: `" + V + "Exhibit_THIRTY-TWO_the_concerns_of_all_sessions_in_one_table.csv`.",
      "The public statement, with no writer now: `incoming/v406other2/For_the_public_Riemann_s_hypothesis_and_the_living_prime_numbering_a_statement_to_pare.md`.",
      "Its record, a sentence a row: `" + V + "The_public_statement_of_Riemann_s_hypothesis_and_the_living_prime_numbering_its_record.csv`."]),
    ("Natural Naming exhibit", "Exhibit_TWENTY_Natural_Naming_v402mgr.md", "gathering-value/Natural_Naming.md",
     ["Words dissolved in conversation and still said in the living files: *same-as*, *alike*, *giving*, *none*, *a spiral of one*, *going along*, *four joint forms*.",
      "The words of a page, by the one list and the released words: `" + V + "instruments/wordcheck.sh`."]),
    ("The managing", "Exhibit_TWENTY-FOUR_Geodesic_Improving_Method_v402mgr.md", "gathering-value/Geodesic_Improving_Method.md",
     ["The method, to learn and to begin: `" + V + "The_managing_method_to_learn_and_to_begin.md`.",
      "The closings, a session a row: `" + V + "The_closings_a_session_at_a_turn.csv`.",
      "The things of value: `" + V + "The_managing_table_of_the_living_expedition.csv`."]),
]
NAMES = [s[0] for s in SESSIONS]
GROUPS = {"Exhibit THIRTY-TWO": NAMES[5], "the public statement": NAMES[5], "The aims, its window": NAMES[7],
          "The boundary claims": NAMES[1], "Gathering": NAMES[7], "gathering": NAMES[7], "Gathering, for later": NAMES[7],
          "Better words": NAMES[6], "Its own resuming": NAMES[7], "The session alone has it": NAMES[7]}

aimings = list(csv.reader(open(os.path.join(me, "The_aimings_of_the_closed_sessions_a_future_session_apiece.csv"), newline="")))[1:]
askings = list(csv.reader(open(os.path.join(me, "The_managing_table_its_sheet_Asked_of_a_session.csv"), newline="")))[1:]
open_askings = [r for r in askings if r[7].split(",")[0] not in ("laid", "let go")]
bumps = []


def slug(name):
    return re.sub(r"[^A-Za-z0-9-]+", "_", name).strip("_")


def there_is(path):
    return os.path.exists(os.path.join(root, path))


def page(name, living, gathering, more):
    own = [r for r in aimings if r[2] == name]
    beside = [r for r in aimings if name in [w.strip() for w in r[3].split(";")]]
    asked = [r for r in open_askings if GROUPS.get(r[2]) == name]
    t = ["Incoming · v406me · laid by `a_session_s_source.py` from the tables as they are", "",
         "# The source of a future session: " + name, "",
         "**To begin.** Go through Start here whole, `incoming/v404mgr/The_working_now.md`. Then `" + V + "The_managing_method_to_learn_and_to_begin.md`. Then this page, its pages opened in their order. Execute ahead of a word of your own. Begin your value page at your opening, and renew it at a turn.", "",
         "## Its home", ""]
    t.append("- Its living file: `" + living + "`." if living else "- Its living file: none yet.")
    t.append("- Its gathering file: `" + gathering + "`." if gathering else "- Its gathering file: none yet.")
    for m in more:
        t.append("- " + m)
    t += ["", "## The closed sessions' aimings sorted to it", "",
          "| The session | Its aiming | Its starting page | The sorting's hand |", "|---|---|---|---|"]
    for r in own:
        t.append("| " + r[0] + " | " + r[1] + " | `" + r[4] + "` | " + r[5] + " |")
    for r in beside:
        t.append("| " + r[0] + " | " + r[1] + " It is with this session too: its future session is " + r[2] + ". | `" + r[4] + "` | " + r[5] + " |")
    if not own and not beside:
        t.append("| none | | | |")
    t += ["", "## Askings open in its groups", "", "They were asked of sessions now closed. An asking goes on with this session, or is let go with a line of its reason.", "",
          "| Asking | Asked of | Its group | The thing asked | Its standing |", "|---|---|---|---|---|"]
    for r in asked:
        t.append("| " + r[0] + " | " + r[1] + " | " + r[2] + " | " + r[3] + " | " + r[7] + " |")
    if not asked:
        t.append("| none | | | | |")
    for path in [living, gathering] + [r[4] for r in own + beside] + re.findall(r"`((?:incoming|gathering-value|kits)/[^` ]+)`", " ".join(more)):
        if path and not there_is(path):
            bumps.append(name + ": not in the set: " + path)
    return "\n".join(t) + "\n", len(own), len(beside), len(asked)


for r in aimings:
    for n in [r[2]] + [w.strip() for w in r[3].split(";") if w.strip()]:
        if n not in NAMES:
            bumps.append("an aiming of " + r[0] + " with a future session of no name: " + n)
for r in open_askings:
    if r[2] not in GROUPS:
        bumps.append("asking " + r[0] + ": its group with no future session: " + r[2])

for name, living, gathering, more in SESSIONS:
    text, a, b, c = page(name, living, gathering, more)
    line = f"{name}: {a} aimings its own, {b} beside, {c} askings open"
    if out:
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "The_source_of_" + slug(name) + ".md"), "w", encoding="utf-8").write(text)
    else:
        laid = os.path.join(me, "sources", "The_source_of_" + slug(name) + ".md")
        if os.path.exists(laid):
            line += "; its page laid: " + ("is the tables' now" if open(laid, encoding="utf-8").read() == text else "is-not the tables' now, lay it again")
        else:
            line += "; its page: not laid"
    print(line)
print(f"\n{len(aimings)} aimings of six closed sessions, {len(open_askings)} askings open.")
print("bumps: " + (str(len(bumps)) if bumps else "none"))
for b in bumps:
    print("  " + b)
