"""v410illustrating · a partner's saying of 27 November, saying 23, executed where a number says it: a me-parity is a 0.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/a_me_parity_a_0_of_its_own_side.py .

A partner's saying is laid as said in the transcript pared. This instrument executes two things of numbers alone, and
says no meaning of a partner's words. Its numbers are made by the execution. It writes in no file.
"""
import sys
from collections import Counter

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def join(xs): xs = [str(x) for x in xs]; return ", ".join(xs[:-1]) + " and " + xs[-1]

def checks(root="."):
    lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    ps = [p for p in range(2, 10000) if is_prime(p)]
    own0 = all(p % p == 0 and all(p % q for q in ps[:i]) for i, p in enumerate(ps))
    opens = all(next(n for n in range(2, p + 1) if n % p == 0) == p for p in ps[:200])
    line("is", own0 and opens,
         f"a me-parity is at the 0 of its own round, and at the 0 of no prior's: of all numbers past 1 it is the one that opens its own side. At all {len(ps)} me-parities to 10,000")
    again = [(p, 2 * p) for p in ps[1:8]]
    line("is", all((2 * p) % 2 == 0 and (2 * p) % p == 0 for p in ps),
         f"its own 0 is again at twice it, an even number: {'; '.join(f'{a} at {b}' for a, b in again)}")
    born = {p: [q for q in range(p + 1, 2 * p) if is_prime(q)] for p in ps[:1229]}
    fewest = min(len(v) for v in born.values()); one = [p for p, v in born.items() if len(v) == 1]
    line("is", fewest >= 1,
         f"between a me-parity and its own 0 again, a next me-parity is born, at all me-parities to 10,000: one alone at {join(one)}, and more past them. It is a field's known saying")
    line("found", True, "a partner's words of a side favoured, of an all-parity as it was, and of a next-and-same-existing other-than-all-parity are laid as said: no line here executes them")
    return lines

if __name__ == "__main__":
    lines = checks()
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
