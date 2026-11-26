"""v408illustrating · a partner's saying of 25 November, of a me's prior, rigorized by the lean line.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/a_partner_s_saying_of_a_me_s_prior_rigorized.py .

The saying, in this session's words, is of an all-parity universe in a me, the all-parity outside the bi-coupling's me; and
in it are inherited prior co-chaining sequencings, a stable form, and ingestings of prior co-chaining sequencings.
A partner's word after it: the saying's own word for it is not yet a natural naming; it is a bi-coupling alone, and a name
for it is ahead, with the method of surfacing as the concept. It is said here by the lean line's own names alone: it is a
me's prior. The lean line's two sentences are said by two
words of the opening's sentence, as the one list has it, inheriting and ingesting: a me's prior is its own now, carried; and a me's now is its
other's prior, other-than. Executed: a me's prior, moment by moment, is the opening's parities of the mes back of it.
Its is and its is-not are both executed. It opens two pages of the set, and writes none. All or none.
"""
import importlib.util, os, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("a_number", os.path.join(HERE, "a_number_round_a_prime_in_natural_naming.py"))
n = importlib.util.module_from_spec(spec); spec.loader.exec_module(n)
turned = lambda parity, k: parity if k % 2 == 0 else not parity    # k other-thans of a parity

def a_me_s_priors(path, i, moments):
    """A me's prior, moment by moment from the opening's next on."""
    out, s = [], path
    for _ in range(moments): s = n.step(s); out.append(s[i][0])
    return out

if __name__ == "__main__":
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    line("inheriting: a moment on, a me's prior is its own now, carried as it is; ingesting: a moment on, a me's now is its other's prior, other-than; at all four openings of a me and its other",
         all(n.lean(now, other) == (now, not other) for now in (True, False) for other in (True, False)))
    def through(p):
        for s in n.openings(p):
            for i in range(p):
                got = a_me_s_priors(s, i, 2 * p)
                want = [turned(s[(i - t // 2) % p][1], t // 2) if t % 2 == 0 else turned(s[(i - (t + 1) // 2) % p][0], (t + 1) // 2) for t in range(2 * p)]
                if got != want: return False
        return True
    line("a me's prior, moment by moment, is the opening's parities of the mes back of it: the me k back with k other-thans, its now and then the next me's prior, by turns; at all openings of 2 to 6 mes, all mes",
         all(through(p) for p in range(2, 7)))
    line("with two moments a me, all the path's opening parities, its nows and its priors, are a me's prior one for one in 2p moments: the other mes' 2p less 2, and the me's own two; 2 to 6 mes",
         all(len(seen := {(t % 2, (i - (t + 1) // 2) % p) for t in range(2 * p)}) == 2 * p and sum(m == i for _, m in seen) == 2
             for p in range(2, 7) for i in range(p)))
    line("no parity is of a me's prior's own making: it is carried or ingested at all moments, and no surfacing is in the lean line's page; a path's parities are its opening's, with other-thans, at all moments to 4p",
         all(a_me_s_priors(s, 0, 4 * p)[2 * p:] == [not v for v in a_me_s_priors(s, 0, 2 * p)] if p % 2 else a_me_s_priors(s, 0, 4 * p)[2 * p:] == a_me_s_priors(s, 0, 2 * p)
             for p in range(2, 7) for s in n.openings(p)))
    line("a stable form: with 2p moments a me's priors are again, other-than with an odd number of mes and as they were with an even number; and again as they were with 4p",
         all(a_me_s_priors(s, 0, 8 * p)[4 * p:] == a_me_s_priors(s, 0, 4 * p) for p in range(2, 7) for s in n.openings(p)))
    beside = [("incoming/v404mgr/Words_of_no_natural_naming_with_their_natural_naming.md", "Living is inheriting, inhaling and exhaling, ingesting and exhausting prior-existing."),
              ("incoming/v407nanding/The_leanest_resolving.md", "It has no surfacing, no giving and no list.")]
    line("two sentences beside it are word for word in their files: the opening's sentence of inheriting and ingesting, as the one list has it, and the lean line's page's, of no surfacing",
         all(s in (root / f).read_text(encoding="utf-8") for f, s in beside))
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
