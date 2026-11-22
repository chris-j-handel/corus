"""Exhibit ONE Natural Resolver's code, taken from its living file as it is,
and the spiral and the torus of selves as Exhibit ONE opens them.

No line of the resolver is written here. The code is the first python block of
the living file, executed as it is. What is this page's own: the opening of a
spiral or a torus as Exhibit ONE says it, and the counting of moments.

    python3 -I incoming/v406Reiman/instruments/resolver_as_it_is.py .
"""
import re
import sys
from pathlib import Path

S = "one sharing"


def resolver(root):
    page = next(Path(root).glob("Exhibit_ONE_Natural_Resolver_*.md"))
    code = re.search(r"```python\n(.*?)```", page.read_text(encoding="utf-8"), re.S).group(1)
    names = {}
    exec(compile(code, str(page), "exec"), names)
    return names, page.name


def spiral_couplings(n):
    return {(i, 9): (i + 1) % n for i in range(n)}


def torus_couplings(p, q):
    c = {}
    for a in range(p):
        for b in range(q):
            c[((a, b), 9)] = ((a + 1) % p, b)
            c[((a, b), 10)] = (a, (b + 1) % q)
    return c


def opening(selves, priors):
    return {s: ([(S, priors[s])], []) for s in selves}


def frozen(society):
    return tuple(
        (s, tuple(sorted(prior)), tuple(sorted(received)))
        for s, (prior, received) in sorted(society.items(), key=lambda kv: str(kv[0]))
    )


def moments_again(step, society, couplings, most=20000):
    """The moment from which the society is again, and its moments to again."""
    seen = {}
    t = 0
    while t <= most:
        key = frozen(society)
        if key in seen:
            return seen[key], t - seen[key]
        seen[key] = t
        society = step(society, couplings)
        t += 1
    return None, None


def exhibit_spiral_priors(n):
    """Self 1 with prior -, parities inverting one to the next along."""
    return {i: (-1 if i % 2 == 0 else 1) for i in range(n)}


def exhibit_torus_priors(p, q):
    return {(a, b): (-1 if (a + b) % 2 == 0 else 1) for a in range(p) for b in range(q)}


def self_1_sharings(step, n, moments=12):
    society = opening(range(n), exhibit_spiral_priors(n))
    c = spiral_couplings(n)
    out = []
    for _ in range(moments):
        society = step(society, c)
        got = dict(society[1 % n][1])  # what self 1 passed along, as its next receives it
        v = got.get(S, 0)
        out.append("+" if v > 0 else "−" if v < 0 else "0")
    return out


if __name__ == "__main__":
    root = sys.argv[1]
    names, page = resolver(root)
    step = names["_17_next_existing"]
    print("The resolver:", page, "its first python block, as it is")
    print()
    print("A spiral of selves, as Exhibit ONE opens it")
    said_a = {
        1: "+, 0, −, 0, +, 0, −, 0, +, 0, −, 0",
        2: "+, −, +, −, +, −, +, −, +, −, +, −",
        3: "+, 0, −, +, −, +, −, 0, +, −, +, −",
        5: "+, 0, −, +, −, +, −, +, −, +, −, 0",
        7: "+, 0, −, +, −, +, −, +, −, +, −, +",
    }
    said_b = {1: 4, 2: 2, 3: 12, 4: 2, 5: 20, 6: 2, 7: 28, 8: 2, 9: 36, 10: 2, 11: 44, 17: 68, 59: 236}
    all_is = True
    for n, b in said_b.items():
        a = ", ".join(self_1_sharings(step, n))
        _, again = moments_again(step, opening(range(n), exhibit_spiral_priors(n)), spiral_couplings(n))
        is_a = said_a.get(n) in (None, a)
        is_b = again == b
        all_is = all_is and is_a and is_b
        print(f"  {n:>2} selves · a: {a} · b: {again} · {'is' if is_a and is_b else 'is-not'}")
    print()
    print("A torus of selves, as Exhibit ONE opens it")
    said_t = {(1, 3): 3, (2, 3): 2, (1, 5): 5, (3, 3): 12, (3, 5): 12, (3, 7): 7, (3, 13): 13, (5, 7): 20, (5, 11): 11, (7, 17): 17}
    for (p, q), a in said_t.items():
        selves = [(x, y) for x in range(p) for y in range(q)]
        _, again = moments_again(step, opening(selves, exhibit_torus_priors(p, q)), torus_couplings(p, q))
        all_is = all_is and again == a
        print(f"  {p} along · {q} across · a: {again} · {'is' if again == a else 'is-not'}")
    print()
    print("All is." if all_is else "An is-not is above.")
    sys.exit(0 if all_is else 1)
