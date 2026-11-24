"""How much of this session's naming and explaining is said in nand now: a measure, executed (session v406geodesic2).

By a partner's word of 24 November, re-said: v407nanding is open; this session's illustrating is to cohere with the nand
explaining; and how much of the naming and explaining is said in nand is worth exploring.

What is numbered here:
  1  a relation of two at one now: all sixteen by nand alone, a relation by its least nands, all circuits gone through;
  2  v406Reiman's own forms, its other-than, its both and its either, at their least;
  3  this session's logic, its fifty-four sentences executed with their nands numbered, a nand a lookup of v406Reiman's table;
  4  a sentence of whole numbers said by nand, to its number of nands: prior two added, round ten, a route of sixty;
  5  a span's podaling by other-thans alone, a nand a place.

The logic's instrument is executed as it is, with one line of it said again, its `line`, to lay the nands' number beside a
sentence's number. Its sentences by kind, in 3, are this session's placing, by its going through of the lines.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_how_much_of_this_sessions_explaining_is_said_in_nand_now.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import contextlib, importlib.util, io, sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
NANDS = [0]


class Numbered(dict):
    """v406Reiman's table of nand, a lookup of it numbered."""
    def __getitem__(self, k):
        NANDS[0] += 1
        return dict.__getitem__(self, k)


_as_it_was = importlib.util.spec_from_file_location


class _Numbering:
    def __init__(self, loader): self.loader = loader
    def create_module(self, spec): return self.loader.create_module(spec)
    def exec_module(self, module):
        self.loader.exec_module(module)
        if isinstance(getattr(module, "NAND", None), dict) and not isinstance(module.NAND, Numbered): module.NAND = Numbered(module.NAND)


def _numbering(name, path, *a, **k):
    spec = _as_it_was(name, path, *a, **k); spec.loader = _Numbering(spec.loader); return spec


def numbered(what):
    NANDS[0] = 0; given = what(); return given, NANDS[0]


# 1 · the sixteen relations of two at one now, a relation its four cases, and its least nands with all circuits gone through
A, B = 0b0011, 0b0101                                                             # a thing and an other, case with case
def the_sixteen_by_their_least_nands(most=5):
    least, now = {A: 0, B: 0}, {frozenset((A, B))}
    for nands in range(1, most + 1):
        nexts = set()
        for has in now:
            for x in has:
                for y in has:
                    new = ~(x & y) & 15
                    if new not in has: nexts.add(has | {new}); least.setdefault(new, nands)
        now = nexts
    return least


# 3 · this session's logic, by its kinds: this session's placing
AT_ITS_OWN_LINE = {6, 7, 25, 26, 27, 29, 33, 34, 35, 36, 37, 38, 40, 41, 48, 49, 50, 51, 52, 53}
FROM_MOMENTS_LAID_AHEAD = {39, 42, 43, 44, 46, 47, 54}                            # moments the nand step laid, ahead of the sentence's own line
OF_WHOLE_NUMBERS = {1, 2, 3, 4, 5, 28} | set(range(8, 25))
OF_NAMES = {30, 31, 32, 45}                                                       # the living code's own lines gone through, and the names' table
def the_logic_with_its_nands_numbered(nand_file):
    logic = HERE / "the_logic_of_podaling_routing_and_orienting_executed.py"
    source = logic.read_text(encoding="utf-8")
    its_line = "def line(n, name, ok): results.append((n, name, bool(ok)))"
    assert len(source.split(its_line)) == 2
    source = source.replace(its_line, "def line(n, name, ok): results.append((n, name, bool(ok))); _beside.append((n, _nands[0]))")
    beside, world = [], {"__name__": "__main__", "__file__": str(logic)}
    world.update(_beside=beside, _nands=NANDS)
    argv, sys.argv, NANDS[0] = sys.argv, [str(logic), nand_file], 0
    importlib.util.spec_from_file_location = _numbering
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            try: exec(compile(source, str(logic), "exec"), world)
            except SystemExit: pass
    finally:
        importlib.util.spec_from_file_location, sys.argv = _as_it_was, argv
    by_sentence, before = {}, 0
    for n, at in beside: by_sentence[n] = at - before; before = at
    return world["results"], by_sentence


if __name__ == "__main__":
    nand_file = sys.argv[1]
    spec = _numbering("the_resolver_with_nand_alone", nand_file)
    its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    least = the_sixteen_by_their_least_nands()
    tally = [sum(1 for v in least.values() if v == k) for k in range(6)]
    line(f"A relation of two at one now, its four cases an is or an is-not, is one of sixteen, and all sixteen are said by nand alone: by their least nands, all circuits gone through, {tally[0]} with none, {tally[1]} with one, {tally[2]} with two, {tally[3]} with three, {tally[4]} with four and {tally[5]} with five",
         len(least) == 16 and tally == [2, 3, 4, 4, 2, 1] and sum(least.values()) == 36)

    cases = [(a, b) for a in (False, True) for b in (False, True)]
    table = lambda form: sum((1 << (3 - i)) for i, (a, b) in enumerate(cases) if form(a, b))
    forms = {"other-than": (lambda a, b: its.other_than(a), 1), "both": (its.both, 2), "either": (its.either, 3), "nand": (its.nand, 1)}
    at_least = all(numbered(lambda f=f: f(True, False))[1] == n == least[table(f)] for f, n in forms.values())
    twice = numbered(lambda: its.other_than(its.other_than(True)))
    line("v406Reiman's own forms are at their least: a nand and an other-than one nand, a both two, an either three; and an other-than of an other-than, two nands, is the thing again, a relation with none",
         at_least and twice == (True, 2) and least[A] == 0)

    results, by_sentence = the_logic_with_its_nands_numbered(nand_file)
    own = {n for n, k in by_sentence.items() if k}
    all_nands = sum(by_sentence.values())
    line(f"This session's logic, its fifty-four sentences all is, executed with its nands numbered: twenty sentences give nands at their own lines, {all_nands:,} nands; seven are executed from moments the nand step laid ahead of them; twenty-three are of whole numbers; four are of names, the living code's own lines and the names' table",
         len(results) == 54 and all(ok for _, _, ok in results) and own == AT_ITS_OWN_LINE and len(own) == 20
         and set(by_sentence) - own == FROM_MOMENTS_LAID_AHEAD | OF_WHOLE_NUMBERS | OF_NAMES
         and [len(FROM_MOMENTS_LAID_AHEAD), len(OF_WHOLE_NUMBERS), len(OF_NAMES)] == [7, 23, 4] and all_nands == 38_067_300)

    places = lambda n, wide: [bool((n >> i) & 1) for i in range(wide)]
    number = lambda ps: sum(1 << i for i, p in enumerate(ps) if p)
    def added_round_ten(a, b):                                                    # two numbers of 0 to 9, four places, added round ten, by nand alone
        s = its.adding_with_nand(a, b)                                            # five places, 0 to 18
        six_on = its.adding_with_nand(s, places(6, 5))                            # its place of sixteen is: ten or more
        ten_or_more = six_on[4]
        return [its.either(its.both(ten_or_more, x), its.both(its.other_than(ten_or_more), y)) for x, y in zip(six_on[:4], s[:4])]
    def a_route(moments):
        prior, now, out = places(0, 4), places(1, 4), []
        for _ in range(moments):
            out.append((number(prior), number(now))); prior, now = now, added_round_ten(prior, now)
        return out
    route, nands_of_it = numbered(lambda: a_route(121))
    whole = [(0, 1)]
    for _ in range(120): whole.append((whole[-1][1], (whole[-1][0] + whole[-1][1]) % 10))
    a_moment = numbered(lambda: added_round_ten(places(7, 4), places(8, 4)))[1]
    line(f"A sentence of whole numbers said by nand, the logic's 13: prior two added, round ten, is a route of sixty moments and no fewer, by nand alone the same as by whole numbers, moment with moment, {a_moment} nands a moment",
         route == whole and route[60] == route[0] and all(route[t] != route[0] for t in range(1, 60)) and nands_of_it == 121 * a_moment and a_moment == 203)        # nineteen a place added, nine places, and eight a place chosen, four places

    def a_podaling(name, of=(0, 1, 2, 3)):                                        # a name of 1 to 16, numbered from none with four places
        ps = places(name - 1, 4)
        return number([its.other_than(p) if i in of else p for i, p in enumerate(ps)]) + 1
    four = numbered(lambda: [a_podaling(k) for k in range(1, 17)])
    one = numbered(lambda: [a_podaling(k, (3,)) for k in range(1, 17)])
    SIXTEEN = [n for n in range(60) if n % 2 and n % 3 and n % 5]
    line("A span's podaling is a nand a place: the sixteen names with four other-thans are their 17 less, and with one, their top place's, their 8 up or 8 less; on the sixteen places of 0 to 60 the four are 60 less and the one is 30 on or 30 less. Said already by this session's sixteenth drawing, and by mes in v407nanding's page",
         four == ([17 - k for k in range(1, 17)], 64) and one == ([(k + 8 - 1) % 16 + 1 for k in range(1, 17)], 16) and len(SIXTEEN) == 16
         and all(SIXTEEN[a_podaling(k) - 1] == 60 - SIXTEEN[k - 1] and abs(SIXTEEN[a_podaling(k, (3,)) - 1] - SIXTEEN[k - 1]) == 30 for k in range(1, 17)))

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
