"""A bi-coupling, executed with Exhibit ONE's own code.

    python3 -I incoming/v405co-chain/instruments/bi_coupling_executed.py EXHIBIT_ONE.md [MOMENTS]

The code block of Exhibit ONE Natural Resolver is executed as it is, with two
selves, A and B, one key, x, and five ways of 5-now-co-existing:

  both ways, the same         A and B to one another, priors +1 and +1
  both ways, other-than same  A and B to one another, priors +1 and -1
  one way                     A to B only
  a third apart               C to A and to B, nothing between A and B
  a self to itself            A to A and B to B, nothing between A and B

Moment by moment it prints the prior of A and of B and the parities they
receive, and whether their priors, and the parities they receive, are the same,
one inversion apart, or other-than both. It sizes and decides nothing.
"""
import re
import sys


def resolver(path):
    text = open(path, encoding="utf-8").read()
    block = re.search(r"```python\n(.*?)```", text, re.S)
    if block is None:
        sys.exit("no python block in " + path)
    names = {}
    exec(compile(block.group(1), path, "exec"), names)
    return names["_17_next_existing"]


def as_one(a, b):
    a, b = sorted(set(a)), sorted(set(b))
    if a == b:
        return "the same"
    if a == sorted(-v for v in b):
        return "one inversion apart"
    return "other-than both"


def go(next_existing, title, five, priors, moments):
    print(title)
    sixteen = {s: ([("x", p)], []) for s, p in priors.items()}
    for m in range(1, moments + 1):
        sixteen = next_existing(sixteen, five)
        row = " | ".join(
            f"{s}: prior {p[0][1]:+d}, receives {[v for _, v in r]}"
            for s, (p, r) in sixteen.items()
        )
        pa, pb = [sixteen["A"][0][0][1]], [sixteen["B"][0][0][1]]
        ra = [v for _, v in sixteen["A"][1]]
        rb = [v for _, v in sixteen["B"][1]]
        print(f"  moment {m}: {row}")
        print(f"            A and B: priors {as_one(pa, pb)}; received {as_one(ra, rb)}")
    print()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    moments = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    nx = resolver(sys.argv[1])
    both = {("A", 6): "B", ("A", 10): "B", ("A", 9): "B",
            ("B", 6): "A", ("B", 10): "A", ("B", 9): "A"}
    one = {("A", 6): "B", ("A", 10): "B", ("A", 9): "B"}
    third = {("C", 6): "A", ("C", 10): "B", ("C", 9): "A"}
    itself = {("A", 6): "A", ("A", 10): "A", ("A", 9): "A",
              ("B", 6): "B", ("B", 10): "B", ("B", 9): "B"}
    go(nx, "Both ways, the same, A +1 and B +1:", both, {"A": 1, "B": 1}, moments)
    go(nx, "Both ways, other-than same, A +1 and B -1:", both, {"A": 1, "B": -1}, moments)
    go(nx, "One way, A to B, A +1 and B +1:", one, {"A": 1, "B": 1}, moments)
    go(nx, "A third apart, C to A and to B, A +1, B -1, C +1:", third, {"A": 1, "B": -1, "C": 1}, moments)
    go(nx, "A self to itself, A to A and B to B, A +1 and B -1:", itself, {"A": 1, "B": -1}, moments)


if __name__ == "__main__":
    main()
