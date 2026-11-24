"""v406geodesic2 · the check of the 23rd drawing: two me-nows co-chained front to back, the one's giving the other's observing.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_two_mes_co-chained_front_to_back.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py .

A partner's asking of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said: with our understanding of
resolving, a me-now observing its next universe, other-than an other, is-or-is-not same-existing; two of these co-chained front to
back, in a drawing.
It opens v406Reiman's cell and its step of all selves from their own file, and Exhibit ONE Natural Resolver for its code's names,
and writes none. A me here is that cell, by v406all2-2's saying of its name. Parities are a +, a - and a 0, as the cell has them.
All or none: with one line not is, the check is not.
"""
import importlib.util, sys
from pathlib import Path
its_file, root = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", its_file)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
TWO, ONE, nand = its.TWO, its.ONE, its.nand
results = []
def line(name, ok): results.append((name, bool(ok)))
THREE = (0, 1, -1)
def a_me(prior, observed):                                             # one me, one moment: its giving and its next prior
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next]
def front_to_back(front, back, observed):                              # the front me's giving named the back me's observing: a coupling, no is-or-is-not
    g_front, n_front = a_me(front, [observed]); g_back, n_back = a_me(back, [g_front])
    return g_front, n_front, g_back, n_back

line("one me, one moment, by the cell: with a prior, observing the same as its prior it gives none and is as it was, same-existing; observing its other-than or none it inverts, and gives its inverting; with no prior it gives what it observes and has it",
     all(a_me(p, [o]) == ((0, p) if o == p else (-p, -p)) for p in (1, -1) for o in THREE) and all(a_me(0, [o]) == (o, o) for o in THREE))
opposite = [(p, -p, o) for p in (1, -1) for o in THREE]
line("two mes front to back, their priors one the other's other-than: with all it observes, one of the two alone inverts and the other is as it was; the front same-existing, the back inverts, and the front inverting, the back is same-existing",
     all((n_f == f) != (n_b == b) for f, b, o in opposite for g_f, n_f, g_b, n_b in [front_to_back(f, b, o)])
     and all((n_f == f) == (o == f) for f, b, o in opposite for g_f, n_f, g_b, n_b in [front_to_back(f, b, o)]))
line("the back me gives on the front me's own prior with the front observing it, and none with all else: what is same-existing at the front goes through the two, an other-than of an other-than",
     all(front_to_back(f, b, o)[2] == (o if o == f else 0) for f, b, o in opposite))
line("with no priors what is observed goes on through both as it is; with the two priors the same the back gives their other-than with all the front observes, and none of it goes through",
     all(front_to_back(0, 0, o)[2] == o for o in THREE) and all(front_to_back(p, p, o)[2] == -p for p in (1, -1) for o in THREE))
IS, NOT = True, False
one_giving = lambda prior, plus, minus: its.a_cell(prior, [(plus, minus)])[0][0]
line("one me with a prior a - is an other-than of what it observes; two in a row, with one more observed at the back me, are a nand, all the logic the cell's lines have",
     all(one_giving((NOT, IS), NOT, x) == nand(x, x) for x in (IS, NOT))
     and all(one_giving((NOT, IS), one_giving((NOT, IS), NOT, y), x) == nand(x, y) for x in (IS, NOT) for y in (IS, NOT)))
S = "one"
def moments(couplings, priors, how_many):
    society = {s: ([(S, priors[s])], []) for s in priors}; out = []
    for _ in range(how_many):
        out.append({s: (dict(society[s][0]).get(S, 0), [v for _, v in society[s][1]]) for s in society})
        society = its.step_with_nand(society, couplings)
    return out
closed = moments({(0, 9): 1, (1, 9): 0}, {0: -1, 1: 1}, 9)
opened = moments({(0, 9): 1}, {0: -1, 1: 1}, 9)
line("by the code's own step, two mes snapped along by 9, the last to the one opening it, a - and a +: the two are one the other's other-than with all moments, and are again with 2",
     all(m[0][0] == -m[1][0] for m in closed) and all(closed[t + 2] == closed[t] for t in range(1, 7)) and closed[1] != closed[2])
line("front to back is a moment on: the back me's observing with a moment is the front me's giving with the moment before it",
     all(opened[t + 1][1][1] == [a_me(opened[t][0][0], opened[t][0][1])[0]] for t in range(8)) and all(m[0][1] == [] for m in opened))
sys.path.insert(0, str(its_file.resolve().parent))
import resolver_as_it_is as as_it_is
names, _ = as_it_is.resolver(str(root))
line("the code's own names: Exhibit ONE Natural Resolver's code has 1-now-existing, 9-next-co-discovering and 17-next-existing; by nand a me's moment is as its 1 and all mes' moment as its 17, and a spiral's coupling along is by 9",
     all(n in names for n in ("_1_now_existing", "_9_next_co_discovering", "_17_next_existing")) and "1-now-existing" in its.now_with_nand.__doc__ and "17-next-existing" in its.step_with_nand.__doc__
     and all(by == 9 for (_, by) in as_it_is.spiral_couplings(7)))

# ---- two diamonds of nine, one vertex of both
FRONT = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
BACK = [[n + 8 for n in r] for r in FRONT]
both_of = [n for r in FRONT for n in r] + [n for r in BACK[1:] for n in r]
line("two diamonds of nine with one vertex of both are seventeen, 1 to 17: the back diamond's rows are the front's 8 up, a row odd or even all through, and 1, 9 and 17 are the three vertices",
     sorted(both_of) == list(range(1, 18)) and FRONT[4] == BACK[0] == [9] and (FRONT[0], BACK[4]) == ([1], [17]) and all(len({n % 2 for n in r}) == 1 for r in FRONT + BACK) and 9 + 9 - 1 == 17)
about = lambda twice_station: (lambda n: twice_station - n)                    # a podaling, by twice its station: a station between two numbers is one too
line("the podaling about 9, 18 less, carries the front diamond to the back, a row to a row gone the other way; 8 up is the podaling about 5 and then about 9, 10 less and then 18 less; and on the names it is the living files' 9 less and then 17 less, about stations one place apart",
     [sorted(about(18)(n) for n in r) for r in FRONT] == BACK[::-1] and all(about(18)(about(10)(n)) == n + 8 for n in range(1, 10)) and all(about(17)(about(9)(n)) == n + 8 for n in range(1, 9))
     and (18 - 10, 17 - 9) == (8, 8))
wide = lambda n: (n % 60) if (n % 60) <= 30 else 60 - (n % 60)
line("on the line of cones the two are four cones of 30, 0 to 120: rows of 1, 2, 3, 2, 1, 2, 3, 2 and 1 numbers at 0, 15 and on to 120, the mes at the widests, 30 and 90, and 1, 9 and 17 at the vertices, 0, 60 and 120",
     [1 + wide(n) // 15 for n in range(0, 121, 15)] == [len(r) for r in FRONT] + [len(r) for r in BACK[1:]] and [n for n in range(0, 121, 30) if wide(n) == 30] == [30, 90]
     and [n for n in range(0, 121, 30) if wide(n) == 0] == [0, 60, 120])
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
