"""A walker aiming its own next on the surface, executed beside the table of cases.

The surface: all openings of n is-or-is-nots, 2**n places.
The wiring: clauses, each a not-all of 2 or 3 places (so nand alone writes it).
A place is marked when every clause is met.

The table of cases explores place by place: 2**n.
A walker stands at one place and aims its next from the wiring itself:
it takes a clause not met where it stands, and steps by one is-or-is-not of that clause.
  Walker A: the step is any one of the clause's places (Schoening 1999; with 2-clauses, Papadimitriou 1991).
  Walker B: the step is the place breaking the fewest clauses now met (WalkSAT, Selman, Kautz, Cohen 1994).

Counted: steps to a marked place, on wirings a complete search has shown to have one.
Nothing here is proved. An executing is of the sizes stepped.

    python3 -I incoming/v409pvnp/instruments/a_walker_aiming_its_next_beside_the_table.py .
"""
import random, statistics, sys, time

def wiring(n, k, ratio, rng):
    out = []
    for _ in range(round(ratio * n)):
        vs = rng.sample(range(n), k)
        out.append([(v, rng.random() < 0.5) for v in vs])
    return out

def has_a_marked_place(n, clauses):
    """Complete search with forced steps (DPLL). Used only to keep wirings that have a marked place."""
    sys.setrecursionlimit(10000)
    def go(assign):
        changed = True
        while changed:
            changed = False
            for c in clauses:
                free = None; nfree = 0; met = False
                for v, s in c:
                    a = assign[v]
                    if a is None: nfree += 1; free = (v, s)
                    elif a == s: met = True; break
                if met: continue
                if nfree == 0: return False
                if nfree == 1: assign[free[0]] = free[1]; changed = True
        try: v = assign.index(None)
        except ValueError: return True
        for val in (True, False):
            a2 = assign[:]; a2[v] = val
            if go(a2): return True
        return False
    return go([None] * n)

class Standing:
    def __init__(self, n, clauses, rng):
        self.n, self.clauses, self.rng = n, clauses, rng
        self.occ = [[] for _ in range(n)]
        for ci, c in enumerate(clauses):
            for v, s in c: self.occ[v].append((ci, s))
    def open_at(self):
        r = self.rng
        self.a = [r.random() < 0.5 for _ in range(self.n)]
        self.true = [sum(self.a[v] == s for v, s in c) for c in self.clauses]
        self.unmet = [ci for ci, t in enumerate(self.true) if t == 0]
        self.pos = {ci: i for i, ci in enumerate(self.unmet)}
    def step(self, v):
        a = self.a; a[v] = not a[v]; val = a[v]
        for ci, s in self.occ[v]:
            if s == val:
                self.true[ci] += 1
                if self.true[ci] == 1:
                    i = self.pos.pop(ci); last = self.unmet.pop()
                    if last != ci: self.unmet[i] = last; self.pos[last] = i
            else:
                self.true[ci] -= 1
                if self.true[ci] == 0:
                    self.pos[ci] = len(self.unmet); self.unmet.append(ci)
    def breaks(self, v):
        val = self.a[v]
        return sum(1 for ci, s in self.occ[v] if s == val and self.true[ci] == 1)

def walker_a(st, cap):
    steps = 0
    while steps < cap:
        st.open_at()
        for _ in range(3 * st.n):
            if not st.unmet: return steps
            c = st.clauses[st.rng.choice(st.unmet)]
            st.step(st.rng.choice(c)[0]); steps += 1
        if not st.unmet: return steps
    return cap

def walker_b(st, cap):
    st.open_at(); steps = 0
    while steps < cap:
        if not st.unmet: return steps
        c = st.clauses[st.rng.choice(st.unmet)]
        bs = [(st.breaks(v), v) for v, _ in c]
        m = min(bs)[0]
        if m == 0 or st.rng.random() >= 0.5: v = st.rng.choice([v for b, v in bs if b == m])
        else: v = st.rng.choice(c)[0]
        st.step(v); steps += 1
    return cap

def a_row(n, k, ratio, wirings, runs, cap, rng, walkers):
    kept = []
    while len(kept) < wirings:
        w = wiring(n, k, ratio, rng)
        if has_a_marked_place(n, w): kept.append(w)
    out = []
    for walk in walkers:
        got = []
        for w in kept:
            st = Standing(n, w, rng)
            got += [walk(st, cap) for _ in range(runs)]
        out.append((statistics.median(got), sum(g >= cap for g in got)))
    return out

if __name__ == "__main__":
    rng = random.Random(17)
    print("3-clauses, 4.2 a place, wirings with a marked place")
    print(f"{'places':>7} {'the table':>16} {'walker A':>10} {'walker B':>10}")
    prev = None
    for n in (12, 18, 24, 30, 36, 42):
        t = time.time()
        (a, ca), (b, cb) = a_row(n, 3, 4.2, 40, 5, 3_000_000, rng, (walker_a, walker_b))
        note = ""
        if prev: note = f"   a place more multiplies A by {(a / prev[1]) ** (1 / (n - prev[0])):.3f}, B by {(b / prev[2]) ** (1 / (n - prev[0])):.3f}"
        print(f"{n:>7} {2**n:>16,} {a:>10,.0f} {b:>10,.0f}{note}   [{ca + cb} at the cap, {time.time() - t:.0f}s]", flush=True)
        prev = (n, a, b)
        first3 = locals().get("first3") or (n, a, b); last3 = (n, a, b)
    d = last3[0] - first3[0]
    print(f"  over these sizes a place more multiplies the table by 2, walker A by {(last3[1]/first3[1])**(1/d):.2f}, walker B by {(last3[2]/first3[2])**(1/d):.2f}")
    print()
    print("2-clauses, 0.9 a place, wirings with a marked place")
    print(f"{'places':>7} {'n by n':>10} {'walker A, no reopening':>24}")
    def walker_a2(st, cap):
        st.open_at(); steps = 0
        while st.unmet and steps < cap:
            c = st.clauses[st.rng.choice(st.unmet)]; st.step(st.rng.choice(c)[0]); steps += 1
        return steps
    for n in (25, 50, 100, 200, 400, 800):
        (a, ca), = a_row(n, 2, 0.9, 20, 5, 50 * n * n, rng, (walker_a2,))
        print(f"{n:>7} {n*n:>10,} {a:>24,.0f}   [{ca} at the cap]", flush=True)

    print()
    print("A wiring made to aim walker A away: one marked place, all is; 3-clauses alone")
    print("  with i other-than j and k: not all of (is-not i, is j, is k); and with all three: not all is-not")
    print(f"{'places':>7} {'clauses':>8} {'the table':>14} {'walker A':>10} {'walker B':>10}")
    from itertools import combinations
    first = None
    for n in (8, 12, 16, 20, 24):
        w = [[(i, True), (j, False), (k, False)] for i in range(n) for j, k in combinations([x for x in range(n) if x != i], 2)]
        w += [[(i, True), (j, True), (k, True)] for i, j, k in combinations(range(n), 3)]
        runs = 21
        st = Standing(n, w, rng)
        a = statistics.median(walker_a(st, 10**7) for _ in range(runs))
        b = statistics.median(walker_b(st, 10**7) for _ in range(runs))
        print(f"{n:>7} {len(w):>8,} {2**n:>14,} {a:>10,.0f} {b:>10,.0f}", flush=True)
        first = first or (n, a, b); last = (n, a, b)
    d = last[0] - first[0]
    print(f"  over these sizes a place more multiplies the table by 2, walker A by {(last[1]/first[1])**(1/d):.2f}, walker B by {(last[2]/first[2])**(1/d):.2f}")
