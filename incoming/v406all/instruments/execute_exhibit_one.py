"""Execute Exhibit ONE's resolver, taken word for word from its living file,
and set a few of its own tables beside what the execution gives.

Usage: python3 -I execute_exhibit_one.py <path to Exhibit_ONE_...md>
"""
import re
import sys
from math import gcd

text = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", text, re.S).group(1)
ns = {}
exec(compile(code, "exhibit_one_resolver", "exec"), ns)
step = ns["_17_next_existing"]

S = "s"  # one sharing
sign = lambda v: "+" if v > 0 else ("−" if v < 0 else "0")


def run(selves, priors, routes, moments, received_each_moment=None):
    """selves: names; priors: self -> +1/-1/None; routes: (self, 6|9|10) -> receiving self.
    Returns per moment: {self: (sharing parity or None, next prior or None)}."""
    state = {
        x: ([(S, priors[x])] if priors[x] is not None else [], [])
        for x in selves
    }
    out = []
    for m in range(moments):
        if received_each_moment is not None:
            for x in selves:
                state[x] = (state[x][0], list(state[x][1]) + received_each_moment(m, x))
        before = state
        after = step(before, routes)
        row = {}
        for x in selves:
            # the sharing 10-next-co-possibling, recomputed the same way the code does
            ten, eleven = ns["_1_now_existing"](before[x][0], before[x][1])
            sh = dict(ten).get(S)
            nxt = dict(after[x][0]).get(S)
            row[x] = (sh, nxt)
        out.append(row)
        state = after
    return out


def fmt(seq):
    return ", ".join("·" if v is None else sign(v) for v in seq)


print("== One self, moment by moment (prior − first, one sharing)")
cases = {
    "empty with each moment": lambda m, x: [],
    "− with each moment": lambda m, x: [(S, -1)],
    "+ with each moment": lambda m, x: [(S, 1)],
    "+, −, +, − inverting": lambda m, x: [(S, 1 if m % 2 == 0 else -1)],
    "+ and − together with each moment": lambda m, x: [(S, 1), (S, -1)],
}
for name, rec in cases.items():
    r = run(["A"], {"A": -1}, {}, 8, rec)
    print(f"  {name}: sharing {fmt([row['A'][0] for row in r])} | next prior {fmt([row['A'][1] for row in r])}")


def spiral(n, moments):
    selves = list(range(1, n + 1))
    priors = {i: (-1 if i % 2 == 1 else 1) for i in selves}
    routes = {(i, 9): (i % n) + 1 for i in selves}
    return run(selves, priors, routes, moments)


def period(rows, selves):
    seq = [tuple(row[x] for x in selves) for row in rows]
    L = len(seq)
    for p in range(1, L // 3):
        start = L // 2
        if all(seq[t] == seq[t - p] for t in range(start, L)):
            return p
    return None


print("\n== A spiral of selves: self 1's sharing, moments 1 to 12, and moments to parities along again")
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 59]:
    rows = spiral(n, 12 * n + 60)
    a = fmt([row[1][0] for row in rows[:12]])
    print(f"  {n:>2} selves · a: {a} · b: {period(rows, list(range(1, n + 1)))}")

print("\n== Two selves, six moments of sharing")
for pa, pb in [(1, 1), (1, -1)]:
    for label, routes in [
        ("both ways", {("A", 9): "B", ("B", 9): "A"}),
        ("A from B", {("B", 9): "A"}),
        ("B from A", {("A", 9): "B"}),
        ("apart", {}),
    ]:
        r = run(["A", "B"], {"A": pa, "B": pb}, routes, 6)
        print(f"  {sign(pa)}, {sign(pb)} · {label:<9} · A: {fmt([x['A'][0] for x in r])} · B: {fmt([x['B'][0] for x in r])}")

print("\n== Alike selves, a right spiral: one self's prior, moments 0 to 8")
for n in [1, 3, 5]:
    selves = list(range(1, n + 1))
    priors = {i: 1 for i in selves}
    routes = {(i, 9): (i % n) + 1 for i in selves}
    r = run(selves, priors, routes, 8)
    print(f"  a spiral of {n}: {fmt([1] + [row[1][1] for row in r])}")
