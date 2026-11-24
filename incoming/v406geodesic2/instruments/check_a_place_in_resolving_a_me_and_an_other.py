"""v406geodesic2 · the check of the 25th drawing: a place in resolving is a me, and beside it an other.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_place_in_resolving_a_me_and_an_other.py \
      incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py Exhibit_ONE_Natural_Resolver_v402mgr.md

A partner's saying of 24 November is its ground, as said in the transcripts, pared. Re-said: floating is on a surface, neutralling
on a line, and at a place has no name; the drawings' places are vivid and help; in resolving the resolver alone has a place, and
the resolver is the me; the one thing of place is me and other; all else is non-existing in my resolving universe, and
is-or-is-not possibly existing in the universe.
All or none, by the cell by nand, by its step of all mes, and by the living code's own lines.
It opens v406Reiman's cell and step from their own file and Exhibit ONE Natural Resolver for its code, and writes none.
"""
import ast, importlib.util, random, re, sys
from itertools import permutations, product
from pathlib import Path
its_file, exhibit_one = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", its_file)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, str(its_file.resolve().parent))
import resolver_as_it_is as as_it_is
TWO, ONE = its.TWO, its.ONE
results = []
def line(name, ok): results.append((name, bool(ok)))
tree = ast.parse(re.search(r"```python\n(.*?)```", exhibit_one.read_text(encoding="utf-8"), flags=re.S).group(1))
number = lambda name: int(re.match(r"_(\d+)_", name).group(1)) if re.match(r"_(\d+)_", name) else None
numbers = lambda node: {number(n.id) for n in ast.walk(node) if isinstance(n, ast.Name) and number(n.id)} | {number(a.arg) for a in ast.walk(node) if isinstance(a, ast.arg) and number(a.arg)}
fns = {number(f.name): f for f in tree.body if isinstance(f, ast.FunctionDef)}
def a_me(prior, observed):
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next]
THREE = (0, 1, -1)

given = [number(a.arg) for a in fns[1].args.args]
gives = next(st for st in fns[1].body if isinstance(st, ast.Return)).value
line("a me's moment is given two: its prior, a me, and what it observes, an other, the living code's 3 and 2 and the cell's two; and it gives two: its giving, to an other, and its next prior, a me, the code's 10 and 11",
     given == [3, 2] and its.a_cell.__code__.co_argcount == 2 and isinstance(gives, ast.Tuple) and len(gives.elts) == 2 and sorted(numbers(gives)) == [10, 11])
observings = [list(o) for k in range(4) for o in product(THREE, repeat=k)]
line("what a me observes is the same to it in all orders and with all repeats: all orders of an observing of none to three, and the observing twice over, have one giving and one next prior, with all priors; a parity observed is two is-or-is-nots, with nothing of which other gave it",
     all(a_me(p, list(q)) == a_me(p, o) for p in THREE for o in observings for q in set(permutations(o))) and all(a_me(p, o + o) == a_me(p, o) for p in THREE for o in observings)
     and all(len(TWO[v]) == 2 for v in THREE))
WHICH = {5, 13, 16}                                                    # the names saying which me: the bi-couplings, a me going on, and all mes together
line("by the living code the names saying which me, 5, 13 and 16, are in no line of a me's own moment: they are in its going on, with 9 and with 17; and of the nine names 5 alone says which me and which other, the bi-couplings",
     not (numbers(fns[1]) & WHICH) and 5 in numbers(fns[9]) and 13 in numbers(fns[9]) and WHICH <= numbers(fns[17]) and WHICH & set(range(1, 10)) == {5})
S = "one"
def moments(couplings, priors, how_many):
    society = {s: ([(S, priors[s])], []) for s in priors}; out = []
    for _ in range(how_many):
        out.append({s: (dict(society[s][0]).get(S, 0), sorted(v for _, v in society[s][1])) for s in society})
        society = its.step_with_nand(society, couplings)
    return out
def renamed_alike(n, new):                                             # mes renamed, their couplings renamed with them: the same moments, renamed
    couplings, priors = as_it_is.spiral_couplings(n), as_it_is.exhibit_spiral_priors(n)
    renamed = moments({(new[a], by): new[b] for (a, by), b in couplings.items()}, {new[a]: p for a, p in priors.items()}, 4 * n + 2)
    return renamed == [{new[a]: v for a, v in m.items()} for m in moments(couplings, priors, 4 * n + 2)]
random.seed(37)
def namings(n):
    turned = list(range(n))[::-1]; mixed = list(range(n)); random.shuffle(mixed)
    return [dict(zip(range(n), turned)), dict(zip(range(n), mixed)), {a: 100 + 7 * a for a in range(n)}, {a: ("at", a * a) for a in range(n)}]
line("mes renamed, their couplings renamed with them, have the same moments renamed, with spirals of 2 to 7 mes: turned about, mixed, and named by places of a drawing; a place of a me in resolving is its couplings, a me and its others",
     all(renamed_alike(n, new) for n in range(2, 8) for new in namings(n)))
def with_more(n, more_couplings, more_priors):
    couplings, priors = dict(as_it_is.spiral_couplings(n)), dict(as_it_is.exhibit_spiral_priors(n))
    alone = moments(couplings, priors, 4 * n + 2)
    couplings.update(more_couplings); priors.update(more_priors)
    together = moments(couplings, priors, 4 * n + 2)
    return all({a: m[a] for a in range(n)} == mine for m, mine in zip(together, alone)), together
apart = with_more(5, {("x", 9): "y", ("y", 9): "x"}, {"x": -1, "y": 1})            # two more, coupled to one another alone
given_to = with_more(5, {(0, 10): "z"}, {"z": 1})                                   # one more, given to by a me, and giving to none of the five
line("all that is neither me nor my others is non-existing in my resolving: with two mes more coupled to one another alone, and with a me more that a me gives to and that gives to none of mine, all moments of mine are the same as with none of them",
     apart[0] and given_to[0])
line("and they are, in the society: the two apart are one the other's other-than with all moments, again with 2; from my moments alone their is-or-is-not is not said, the same moments of mine with them and with none",
     all(m["x"][0] == -m["y"][0] for m in apart[1]) and apart[1][1]["x"] != apart[1][2]["x"] and apart[0])
reaches = with_more(5, {("w", 9): 0}, {"w": 1})                                     # one more whose giving a me observes: an other
line("an other is a me whose giving a me observes: with one me more giving to a me of mine, the moments of mine are other than with none of it",
     not reaches[0])
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
