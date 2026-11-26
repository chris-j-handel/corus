"""v408illustrating · a partner's saying of 25 November, of zero's two moments, rigorized by the lean line.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/a_partner_s_saying_of_zero_s_two_moments_rigorized.py .

The saying, in this session's words: the one opens at zero's second moment; the even moment alone is of the bi-coupling; and
zero's odd moment is the all-parity in the me. It is of the 47th drawing, whose opening row is one moment of zero.
Executed here: the lean line stepped a moment back; a number's odd moment and even moment; and two co-chains, the nows of the
even moments by the opening's nows alone, and the nows of the odd moments by the opening's priors alone.
The saying's own word for it is not yet a natural naming, by a partner's word after it: it is let go, and no line here is of it. Its is and its is-not are both executed. It writes none.
"""
import importlib.util, os, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("a_number", os.path.join(HERE, "a_number_round_a_prime_in_natural_naming.py"))
n = importlib.util.module_from_spec(spec); spec.loader.exec_module(n)

def back(path):
    """The moment before, by the lean line's own two sentences: a me's now was its prior, and its prior the other-than of the now of the me ahead of it."""
    p = len(path)
    return tuple((not path[(i + 1) % p][1], path[i][0]) for i in range(p))
nows = lambda path: tuple(me[1] for me in path)
priors = lambda path: tuple(me[0] for me in path)

if __name__ == "__main__":
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    line("the lean line is stepped a moment back one way alone: a path is with one path a moment before it, whose nows are its priors; at all openings of 2 to 7 mes",
         all(n.step(back(s)) == s and nows(back(s)) == priors(s) for p in range(2, 8) for s in n.openings(p)))
    path = n.with_one_pair(5); moments = {-1: back(path), 0: path}
    for t in range(1, 21): moments[t] = n.step(moments[t - 1])
    line("a number is two moments, its odd moment and its even moment: on the 47th drawing's path, the number n, its moments 2n less 1 and 2n, is with one me at both, n of 0 to 10",
         all(n.pairs(moments[2 * k - 1]) == n.pairs(moments[2 * k]) == [k % 5] for k in range(11)))
    line("zero's even moment is the opening's, and its odd moment the moment before it, the opening's priors its nows: zero is with me 1 at both, and the one opens a moment on",
         n.pairs(moments[-1]) == n.pairs(moments[0]) == [0] and nows(moments[-1]) == priors(moments[0]) and n.pairs(moments[1]) == [1])
    def chains(p, key, odd):
        seen = {}
        for s in n.openings(p):
            u, row = s, []
            for t in range(1, 13):
                u = n.step(u)
                if t % 2 == odd: row.append(nows(u))
            seen.setdefault(key(s), set()).add(tuple(row))
        return all(len(v) == 1 for v in seen.values())
    line("two co-chains: the nows of the even moments are by the opening's nows alone, and the nows of the odd moments by the opening's priors alone; at all openings of 2 to 6 mes, twelve moments",
         all(chains(p, nows, 0) and chains(p, priors, 1) for p in range(2, 7)))
    line("at an even moment the odd moment's nows are the mes' priors, in the mes, and a moment on the mes' nows are their priors: a me's prior is its now a moment before, at all openings of 2 to 6 mes",
         all(priors(n.step(s)) == nows(s) for p in range(2, 7) for s in n.openings(p)))
    line("is-not, explored: the even co-chain is the nows at an even moment alone; a moment on the nows are the odd co-chain, and the even co-chain is the mes' priors: the two are by turns",
         all(nows(moments[t]) == priors(moments[t + 1]) for t in range(-1, 20)))
    beside = [("incoming/v407nanding/The_leanest_resolving.md", "A moment on, a me's prior is its now."),
              ("incoming/v406geodesic2/The_value_of_v406geodesic2_at_its_wrap.md", "A 0's name is all-parity")]
    line("two sentences beside it are word for word in their files: the lean line's, and v406geodesic2's of a 0's name",
         all(s in (root / f).read_text(encoding="utf-8") for f, s in beside))
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
