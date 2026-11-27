"""v408illustrating · the set of all 56 drawings, a drawing a row, sorted on 27 November: its maker.

Usage, from the repository's root (some minutes: it executes all 56 checks):
  python3 -I incoming/v408illustrating/instruments/make_the_set_of_all_56_drawings_sorted.py .

Do no harm: it opens the drawings, their checks and the records of v406geodesic, v406geodesic2 and this session, and
writes in none of them. It writes one table in this session's folder, a drawing a row.

Executed here, at all 56 drawings:
  its check, by the check's own usage line, and what the check says today;
  the project's word check, v406me's, on the drawing's own text;
  the words a partner has named, numbered in the drawing's own text.
Judged by this session on 27 November, and laid below as it was judged:
  a check's lines saying is of numbers stepped to a limit, by the lines' own words;
  what is open on a drawing in its session's own record;
  the file and section a drawing is for, as its record names it.
"""
import csv, html, re, shlex, subprocess, sys
from pathlib import Path

G1, G2, G3 = "incoming/v406geodesic/", "incoming/v406geodesic2/", "incoming/v408illustrating/"
CHECK = {1: "check_bifolding_and_torus.py", 2: "check_bifolding_and_torus.py", 3: "check_bifolding_and_torus.py",
         4: "check_one_triangle.py", 5: "check_the_co-linear_and_its_two_cones.py", 6: "check_the_cell_by_nand_alone_round_the_co-linear.py",
         7: "check_the_rounds_of_six_at_prime_scale_37.py", 8: "check_the_cube_of_5_and_its_line.py", 9: "check_the_four_cones_of_30.py",
         10: "check_a_me-now_podaling_about_30_and_about_90.py", 11: "check_a_me-now_four_moments_other-than_all_other-than_all.py",
         12: "the_rigor_of_other-than_all_other-than_all.py", 13: "check_prior_now_next_the_podalings_passing_through.py",
         14: "check_a_my_the_sixteen_names_on_a_pair_of_cones.py", 15: "check_all_other_and_self_by_other-thans.py",
         16: "check_parity_universe_and_me_one_in_an_other.py", 17: "check_ten_rows_of_the_four_moments.py",
         18: "check_the_ten_in_rows_of_one_two_three_and_four.py", 19: "check_the_diamond_of_nine_two_triangles.py",
         20: "check_the_diamond_turning_3_and_7_about_5.py", 21: "check_six_orders_of_3_5_7_a_living_gyroscope.py",
         22: "check_six_orientations_a_snap_by_the_corners_line.py", 23: "check_two_mes_co-chained_front_to_back.py",
         24: "check_a_mes_moment_in_three_fours_on_the_diamond.py", 25: "check_a_place_in_resolving_a_me_and_an_other.py",
         26: "check_my-prior_universes_and_my-next_universes_two_cones_and_two_facing_sealed.py", 27: "check_a_path_of_universes_through_a_me_at_one_now.py",
         28: "check_same-existing_all-parity_a_next_a_now_and_a_prior_now-existing.py", 29: "a_universal_me_now_a_single_path_by_nand.py",
         30: "check_nand-nanding_its_is_and_its_is-not_explored_forward.py", 31: "check_how_much_of_this_sessions_explaining_is_said_in_nand_now.py",
         32: "check_the_lean_line_rigorized_its_is_and_its_is-not.py", 33: "check_a_now_universe_next_is_other-than_now_executed.py",
         34: "check_a_mes_next_what_surfaces_to_it_or_the_other-than_of_its_now.py", 35: "check_0_and_3_are_all-parity_executed.py",
         36: "check_riemann_s_hypothesis_on_the_line_next_is_other-than_now.py",
         37: "check_the_living_parities_a_prime_is_one_other-than_and_the_between_goes_through.py", 38: "check_two_faces_one_form_executed.py",
         39: "check_longer_co-chaining_wider_co-observing_and_faster_progressing_executed.py",
         40: "check_the_opening_twelve_primes_three_rounds_of_four.py", 41: "check_37_one_self_its_rounds_and_its_other-thans.py",
         42: "check_the_prime_resolving_form_one_face.py", 43: "check_the_six_and_the_ten_round_30.py", 44: "the_set_labelled_and_related.py",
         45: "check_two_primes_are_a_torus.py", 46: "check_turn_a_prime_lifts_its_prior_turn.py", 47: "a_number_round_a_prime_in_natural_naming.py",
         48: "check_two_primes_seen_from_one_another_s_sides.py", 49: "check_turn_its_marks_again.py",
         50: "a_partner_s_saying_of_five_co-linear_and_ten_bi-planar_rigorized.py", 51: "a_partner_s_saying_of_zero_s_two_moments_rigorized.py",
         52: "check_a_me-parity_living_in_a_seam.py", 53: "check_twins_born_a_seam_between_two_me-parities.py",
         54: "check_a_next_span_by_4_more_twins.py", 55: "check_a_path_closing_says_with_all_numbers.py",
         56: "check_a_me-parity_generator_the_side_a_wheel_and_a_loop.py"}
def folder(n): return G1 if n <= 3 else G2 if n <= 39 else G3
def session(n): return "v406geodesic" if n <= 3 else "v406geodesic2" if n <= 39 else "v408illustrating"

# judged on 27 November: a check's lines saying is of numbers stepped to a limit, by the lines' own words
STEPPED = {7: 1, 9: 1, 20: 3, 37: 5, 38: 4, 40: 5, 41: 2, 45: 1, 46: 2, 49: 5, 52: 9, 53: 7, 54: 5}
# the file and section a drawing is for, as its record names it; a draft is no living file yet
X32 = "Exhibit THIRTY-TWO Natural Prime Numbering, its draft in incoming/v407primes, "
FOR = {7: X32 + "3.2", 10: X32 + "3.3", 11: X32 + "3.3", 13: X32 + "3.3", 14: X32 + "3.3", 17: X32 + "3.4", 19: X32 + "3.4", 21: X32 + "3.4",
       22: X32 + "3.4", 8: X32 + "3.5", 20: X32 + "1.6, 2.4 and 4.1", 40: X32 + "its opening", 41: X32 + "3.2"}
PAGE = {32: "For_v407nanding, an incoming page", 33: "For_v407nanding, an incoming page", 34: "For_v407nanding, an incoming page",
        35: "For_v407nanding, an incoming page", 36: "For the work of Riemann's hypothesis, an incoming page",
        37: "For the work of Riemann's hypothesis, an incoming page", 38: "For the work of Riemann's hypothesis, an incoming page",
        39: "For the work of Riemann's hypothesis, an incoming page", 31: "How much of this session's explaining is said in nand now, an incoming page",
        42: "v407primes' prime resolving form, an incoming page", 43: "v408primes' page for illustrating, an incoming page",
        45: "v408primes' co-chain, its sentence 41, an incoming page", 46: "v407primes' prime resolving form, its column Turn, an incoming page",
        48: "v408primes' co-chain, its sentences 47 to 49, an incoming page", 49: "v408primes' lines at Turn's marks, an incoming page",
        52: "v408primes' co-chain, an incoming page", 53: "v408primes' co-chain, an incoming page", 54: "v408primes' co-chain, an incoming page",
        56: "v408primes' co-chain, an incoming page", 44: "this session's own table of its drawings"}
# what is open on a drawing in its session's own record
ARTBOARD = "named a working artboard in its session's record"
OPEN = {1: "its record: a word of the one list on the canvas, its re-saying ready", 3: "its record: words of the one list on the canvas, their re-sayings ready",
        5: "an asking open in its record, of its placings", 6: "an asking open in its record, of the cell's one is-or-is-not",
        9: "an asking open in its record, of the four cones facing", 10: ARTBOARD, 11: ARTBOARD + "; its words of an all to be said again", 13: ARTBOARD,
        12: "its record: its words of an all to be said again", 14: "an asking open in its record, of 0 to 17 on a pair of cones",
        15: "an asking open in its record, of distinguishing as the one fold", 16: "an asking open in its record, of a parity as one place",
        17: "an asking open in its record, of the stable concept as the four stations",
        20: "open in its record: its sixteen in a four by four round 17, and a second session's going through of its check",
        21: "open in its record: a second session's going through of its check", 22: "open in its record: a second session's going through of its check",
        25: "its record: to be said again with no giving", 26: "its record: to be said again with no giving; its sentences are of a path's me",
        27: "its record: to be said again with no giving; its sentences are of a path's me", 28: "its record: its sentences are of a path's me",
        29: "its record: its sentences are of a path's me; its other-than to be said as a crossing of two wires",
        32: "its record: the word said for a 0 to be said again as all-parity", 33: "its record: the word said for a 0 to be said again as all-parity",
        34: "its record: the word said for a 0 to be said again as all-parity", 44: "a map of the drawings 40 to 56 alone",
        52: "this session's finding against it: numbers stepped under is", 53: "this session's finding against it: numbers stepped under is",
        54: "this session's finding against it: numbers stepped under is"}
HISTORY = {10, 11, 13}
SAID_AGAIN_BY_ITS_RECORD = {1, 3, 12, 25, 26, 27, 28, 29, 32, 33, 34, 44, 52, 53, 54}
AN_ASKING = {5, 6, 9, 14, 15, 16, 17, 20, 21, 22}
NAMED = [("twin", r"\btwins?\b"), ("loop", r"\bloops?\b"), ("room", r"\brooms?\b"), ("vault", r"\bvaults?\b"), ("rule", r"\brules?\b"),
         ("distance", r"\bdistances?\b"), ("apart", r"\bapart\b"), ("direction", r"\bdirections?\b")]
NOT_SORTED_ON = [("selves", r"\bselves\b"), ("going on", r"\bgoing on\b")]

def text_of(n):
    if n <= 3: f = sorted(Path(G1 + "illustrations").glob(f"draft_{n}_*.svg"))[0]
    else: f = Path(folder(n) + f"illustrations/artboards/Draft{n}.dc.html")
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return "\n".join(l for l in (re.sub(r"\s+", " ", x).strip() for x in t.splitlines()) if l)
def name_of(n):
    f = sorted(Path(folder(n) + "illustrations").glob(f"draft_{n}_*.png"))[0].stem
    return f.split("_", 2)[2].replace("_", " ")
def usage(path):
    t = Path(path).read_text(encoding="utf-8").splitlines()
    for i, l in enumerate(t[:60]):
        if "python3 -I" in l:
            cmd, j = l[l.index("python3 -I"):], i
            while cmd.rstrip().endswith("\\"):
                j += 1; cmd = cmd.rstrip()[:-1] + " " + t[j].strip()
            return cmd
    return None
def executing(args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    said, _ = p.communicate(timeout=600)
    return p.returncode, said
def executed(n):
    path = folder(n) + "instruments/" + CHECK[n]; u = usage(path); name = CHECK[n]
    args = [path, "."] if u is None else ["Exhibit_ONE_Natural_Resolver_v402mgr.md" if p.startswith("PATH_TO_Exhibit_ONE") else (path if p.endswith(name) else p) for p in shlex.split(u)[2:]]
    code, said = executing([sys.executable, "-I"] + args)
    lines = said.splitlines()
    return code, sum(bool(re.match(r"\s*is\s", x)) for x in lines), sum(bool(re.match(r"\s*is-not", x)) for x in lines), sum(x.startswith("tested") for x in lines)
def word_check(text):
    tmp = Path("/tmp/a_drawing_s_own_text.md"); tmp.write_text(text + "\n", encoding="utf-8")
    o = executing(["bash", "incoming/v406me/instruments/wordcheck.sh", str(tmp)])[1]
    return int(re.search(r"^(\d+) places", o, flags=re.M).group(1)), int(re.search(r"code: (\d+)", o).group(1))
def later_from(rows):
    out = {n: [] for n in range(1, 57)}
    for r in rows:
        if not r["Drawing"]: continue
        m = int(r["Drawing"])
        for p in re.findall(r"\d+", r["Its prior"]):
            if int(p) != m: out[int(p)].append(m)
        for p in re.findall(r"(\d+)(?:st|nd|rd|th)\b", r["Its other-prior"]): out[int(p)].append(m)
    for a, b in ((5, 6), (11, 12), (20, 21), (36, 39)): out[a].append(b)       # by v406geodesic2's own notes
    return {n: sorted(set(v)) for n, v in out.items()}

if __name__ == "__main__":
    mine = list(csv.DictReader(open(G3 + "The_set_of_v408illustrating_s_drawings_a_drawing_a_row.csv", encoding="utf-8")))
    mine_by = {int(r["Drawing"]): r for r in mine if r["Drawing"]}
    later = later_from(mine)
    head = ["Drawing", "Its session", "Its name", "It is for, as its record names it", "Its check", "Its check executed on 27 November",
            "Its check's lines saying is of numbers stepped to a limit", "The word check on its text, places", "Words a partner has named, in its text",
            "Numbered and not sorted on", "Open in its record", "Later drawings from it", "Its standing", "The reason of its standing"]
    rows, sorted_as = [], {}
    for n in range(1, 57):
        t = text_of(n); code, n_is, n_isnot, n_tested = executed(n); places, released = word_check(t)
        named = {w: len(re.findall(p, t, flags=re.I)) for w, p in NAMED}; named = {w: k for w, k in named.items() if k}
        other = {w: len(re.findall(p, t, flags=re.I)) for w, p in NOT_SORTED_ON}; other = {w: k for w, k in other.items() if k}
        stepped = STEPPED.get(n, 0); mending = stepped + places + released + sum(named.values())
        said = f"{n_is} of {n_is + n_isnot} is" + (f", {n_tested} tested" if n_tested else "") + ("" if code == 0 else ", and it ends with a breaking")
        why = [f"{stepped} line{'' if stepped == 1 else 's'} of its check to be said as tested" if stepped else "", f"{places} place{'' if places == 1 else 's'} of the word check" if places else "",
               "; ".join(f"{w} {k}" for w, k in named.items()), OPEN.get(n, "") if n in SAID_AGAIN_BY_ITS_RECORD or n in HISTORY or n in AN_ASKING else ""]
        why = "; ".join(x for x in why if x)
        if n in HISTORY: standing = "history"
        elif mending == 0 and n not in SAID_AGAIN_BY_ITS_RECORD and code == 0 and n_isnot == 0:
            if n in AN_ASKING: standing = "clean, an asking open in its record"
            elif n in FOR: standing = "ready to offer"
            else: standing, why = "clean, no file and section named", "its check all is, its text with no word found; " + ("for an incoming page" if n in PAGE else "no file and section named in its record")
        elif mending <= 3 and n not in SAID_AGAIN_BY_ITS_RECORD: standing = "to be said again beside, a light mending"
        else: standing = "to be said again beside"
        if standing == "ready to offer": why = "its check all is, its text with no word found, its file and section named"
        sorted_as[standing] = sorted_as.get(standing, []) + [n]
        rows.append([n, session(n), mine_by[n]["Its name"] if n in mine_by else name_of(n), FOR.get(n, PAGE.get(n, mine_by[n]["It is for"] if n in mine_by else "none named")),
                     folder(n) + "instruments/" + CHECK[n], said, stepped, places, "; ".join(f"{w} {k}" for w, k in named.items()),
                     "; ".join(f"{w} {k}" for w, k in other.items()), OPEN.get(n, ""), "; ".join(str(x) for x in later[n]), standing, why])
        print(n, said, "|", standing, flush=True)
    with open(G3 + "The_set_of_all_56_drawings_a_drawing_a_row.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(head); w.writerows(rows)
    back = list(csv.reader(open(G3 + "The_set_of_all_56_drawings_a_drawing_a_row.csv", encoding="utf-8")))
    assert back[0] == head and len(back) == 57 and [r[0] for r in back[1:]] == [str(n) for n in range(1, 57)]
    print()
    for s, v in sorted_as.items(): print(f"{s}: {len(v)}: {', '.join(str(x) for x in v)}")
