"""v408illustrating · a number round a prime, in natural naming: a partner's is-not of direction and of a number's place, said again by the lean line.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/a_number_round_a_prime_in_natural_naming.py .

A partner's saying of 25 November, in this session's words: a direction is a drawing's word and none of nature's; and a place
is a me's, with living numbers alone. This session's sentence of a direction and a number's place round a prime is said
again here with no direction and no place of a number: a prime is a path of p mes closing; a number is two moments of it;
and a number is with one me, the me whose now is not other-than its other's now. Executed by the lean line, v407nanding's,
as it is. Its is and its is-not are both executed. It opens one page of the set, and writes none. All or none.
"""
import itertools, sys
from pathlib import Path

NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}
def lean(me_now, other_prior):                                    # the lean line, v407nanding's, as it is
    return me_now, NOT_BOTH[(other_prior, other_prior)]
def step(path):
    """A moment on, on a path of mes closing: a me a prior and a now, its other the me back of it."""
    return tuple(lean(path[i][1], path[i - 1][0]) for i in range(len(path)))
def pairs(path, k=1):
    """The mes whose now (k of 1) or prior (k of 0) is not other-than its other's."""
    return [i for i in range(len(path)) if path[i][k] == path[i - 1][k]]
def again(path):
    t, u = 1, step(path)
    while u != path: t, u = t + 1, step(u)
    return t
openings = lambda p: (tuple(o) for o in itertools.product(itertools.product((True, False), repeat=2), repeat=p))
def with_one_pair(p):
    """A path of p mes, p odd: nows by turns round it, one pair at its closing; a me's prior its now."""
    return tuple((i % 2 == 0, i % 2 == 0) for i in range(p))

if __name__ == "__main__":
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    line("by the lean line, on a path of mes closing: a me whose now is not other-than its other's now is, two moments on, the me one on; at all openings, 2 to 8 mes",
         all(pairs(step(step(s))) == sorted((i + 1) % p for i in pairs(s)) for p in range(2, 9) for s in openings(p)))
    line("a path of an odd number of mes is with one such me at the least, at all openings and all moments: 3, 5 and 7 mes",
         all(len(pairs(s)) >= 1 for p in (3, 5, 7) for s in openings(p)))
    line("is-not: a path of an even number of mes is with none at some openings: 2, 4, 6 and 8 mes",
         all(min(len(pairs(s)) for s in openings(p)) == 0 for p in (2, 4, 6, 8)))
    walk = {}
    for p in (3, 5, 7, 11, 13):
        s = with_one_pair(p); walk[p] = []
        for n in range(2 * p):
            walk[p].append(pairs(s)); s = step(step(s))
    line("a prime is a path of p mes closing, and a number is two moments of it: with one such me, a number is with one me, and the +1 with the me one on; p numbers are with all p mes; 3, 5, 7, 11 and 13",
         all(w == [[n % p] for n in range(2 * p)] for p, w in walk.items()))
    line("the path is again with four times its mes, a number two moments and both parities inverted with p numbers: 12, 20, 28, 44 and 52 moments",
         [again(with_one_pair(p)) for p in (3, 5, 7, 11, 13)] == [12, 20, 28, 44, 52])
    line("a prime's path is again with 4 and with 4p alone, at all openings: 3, 5 and 7 mes; a crossed number's path is again sooner too: 9 mes with 4, 12 and 36",
         [sorted({again(s) for s in openings(p)}) for p in (3, 5, 7, 9)] == [[4, 12], [4, 20], [4, 28], [4, 12, 36]])
    lean_page = (root / "incoming/v407nanding/The_leanest_resolving.md").read_text(encoding="utf-8")
    beside = [("incoming/v407nanding/The_leanest_resolving.md", "A moment on, a me's now is the other-than of its other's prior."),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "A drawing fixes no position as a place."),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "An opening fixing as a place."),
              ("incoming/v406geodesic2/The_value_of_v406geodesic2_at_its_wrap.md", "in resolving the only place is the me")]
    line("four sentences beside it are word for word in their files: the lean line's, two living, and v406geodesic2's with a partner",
         all(s in (root / f).read_text(encoding="utf-8") for f, s in beside))
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
