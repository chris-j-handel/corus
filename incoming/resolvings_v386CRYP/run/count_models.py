#!/usr/bin/env python3 -I
"""Enumerate 'models' of FIFTEEN line 141 ("In a closed domain the carrying closes ...
Checked exhaustively to five terms -- 592,260 models, none acyclic") under several readings.

A 'carrying' on a domain of n terms is read as a binary relation R on {0..n-1} where
'follow it from anything' requires every term to have a next: R is serial (total on the left).
Readings vary the extra constraints and whether a self-loop counts as a cycle.
For each reading we count, per n = 1..5, the labeled relations, the unlabeled ones (Burnside),
and how many are acyclic.  Any count equal to 592,260 is flagged.
"""
import itertools, sys
import numpy as np

TARGET = 592260


def relations_np(n):
    """All relations on n terms as an (n, 2^(n*n)) array of row bit-masks (row i = successors of i)."""
    r = np.indices((1 << n,) * n, dtype=np.uint8).reshape(n, -1)
    return r


def props(n, r):
    N = r.shape[1]
    one = np.ones(N, bool)
    p = {}
    bit = lambda i, j: ((r[i] >> j) & 1) == 1
    p['serial'] = one.copy()
    for i in range(n):
        p['serial'] &= r[i] != 0
    p['irreflexive'] = one.copy(); p['reflexive'] = one.copy()
    for i in range(n):
        p['irreflexive'] &= ~bit(i, i); p['reflexive'] &= bit(i, i)
    p['functional'] = one.copy()           # at most one next
    for i in range(n):
        p['functional'] &= (r[i] & (r[i] - 1)) == 0
    p['transitive'] = one.copy()
    for i in range(n):
        for j in range(n):
            p['transitive'] &= ~(bit(i, j) & ((r[j] & ~r[i]) != 0))
    p['antisymmetric'] = one.copy(); p['symmetric'] = one.copy()
    for i in range(n):
        for j in range(i + 1, n):
            p['antisymmetric'] &= ~(bit(i, j) & bit(j, i))
            p['symmetric'] &= ~(bit(i, j) ^ bit(j, i))
    p['injective'] = one.copy()             # each term the next of at most one
    for j in range(n):
        col = np.zeros(N, np.uint8)
        for i in range(n):
            col += bit(i, j).astype(np.uint8)
        p['injective'] &= col <= 1
    p['surjective'] = one.copy()            # each term the next of at least one
    for j in range(n):
        hit = np.zeros(N, bool)
        for i in range(n):
            hit |= bit(i, j)
        p['surjective'] &= hit
    return p


def cyclic_np(n, r):
    """has a cycle (self-loop counts), and has a cycle of length >= 2 (loops ignored), via reachability closure."""
    def closure(rows):
        reach = [x.copy() for x in rows]
        for _ in range(n):
            new = []
            for i in range(n):
                acc = reach[i].copy()
                for j in range(n):
                    acc |= np.where(((reach[i] >> j) & 1) == 1, reach[j], 0).astype(np.uint8)
                new.append(acc)
            reach = new
        return reach
    reach = closure([r[i] for i in range(n)])
    cyc = np.zeros(r.shape[1], bool)
    for i in range(n):
        cyc |= ((reach[i] >> i) & 1) == 1
    noloop = [r[i] & ~np.uint8(1 << i) for i in range(n)]
    reach2 = closure(noloop)
    cyc2 = np.zeros(r.shape[1], bool)
    for i in range(n):
        cyc2 |= ((reach2[i] >> i) & 1) == 1
    return cyc, cyc2


def unlabeled_counts(n, r, masks):
    """Burnside: orbits under S_n of each masked set; one pass over the permutations."""
    perms = list(itertools.permutations(range(n)))
    totals = [0] * len(masks)
    for perm in perms:
        lut = np.zeros(1 << n, np.uint8)
        for m in range(1 << n):
            v = 0
            for j in range(n):
                if m >> j & 1:
                    v |= 1 << perm[j]
            lut[m] = v
        fixed = np.ones(r.shape[1], bool)
        for i in range(n):
            fixed &= lut[r[i]] == r[perm[i]]
        for k, m in enumerate(masks):
            totals[k] += int((fixed & m).sum())
    assert all(t % len(perms) == 0 for t in totals)
    return [t // len(perms) for t in totals]


READINGS = {
    'all relations': [],
    'serial (every term has a next)': ['serial'],
    'serial, irreflexive': ['serial', 'irreflexive'],
    'serial, antisymmetric': ['serial', 'antisymmetric'],
    'serial, irreflexive, antisymmetric': ['serial', 'irreflexive', 'antisymmetric'],
    'serial, transitive': ['serial', 'transitive'],
    'serial, symmetric': ['serial', 'symmetric'],
    'functions (exactly one next)': ['serial', 'functional'],
    'functions, irreflexive': ['serial', 'functional', 'irreflexive'],
    'permutations (one next, one prior)': ['serial', 'functional', 'injective'],
    'partial functions': ['functional'],
    'injective relations': ['injective'],
    'serial, injective': ['serial', 'injective'],
    'serial, surjective': ['serial', 'surjective'],
    'transitive': ['transitive'],
    'reflexive': ['reflexive'],
}


def main():
    per = {k: {} for k in READINGS}
    hits = []
    for n in range(1, 6):
        r = relations_np(n)
        p = props(n, r)
        cyc, cyc2 = cyclic_np(n, r)
        masks = {}
        for name, ps in READINGS.items():
            m = np.ones(r.shape[1], bool)
            for q in ps:
                m &= p[q]
            masks[name] = m
        del p
        names = list(READINGS)
        unl = unlabeled_counts(n, r, [masks[k] for k in names] + [masks[k] & ~cyc for k in names])
        for k, name in enumerate(names):
            m = masks[name]
            lab = int(m.sum())
            acyc_loops = int((m & ~cyc).sum())      # acyclic with loops counting as cycles
            acyc_noloop = int((m & ~cyc2).sum())    # acyclic ignoring self-loops
            per[name][n] = (lab, acyc_loops, acyc_noloop, unl[k], unl[len(names) + k])
        del r, masks, cyc, cyc2
        print(f"n={n} done", file=sys.stderr)
    print(f"{'reading':40s} n  labeled  acyclic(loop=cycle)  acyclic(loops ignored)  unlabeled  unlab.acyclic")
    for name, d in per.items():
        for n, (lab, a1, a2, unl, ua) in d.items():
            print(f"{name:40s} {n}  {lab:9d}  {a1:9d}  {a2:9d}  {unl:9d}  {ua:9d}")
            for v, tag in ((lab, 'labeled'), (a1, 'acyclic'), (a2, 'acyclic-noloop'), (unl, 'unlabeled'), (ua, 'unl-acyclic')):
                if v == TARGET: hits.append((name, n, tag))
        for lo in (1, 2):
            s = [sum(d[n][k] for n in range(lo, 6)) for k in range(5)]
            print(f"{name:40s} {lo}..5 {s[0]:9d}  {s[1]:9d}  {s[2]:9d}  {s[3]:9d}  {s[4]:9d}")
            for v, tag in zip(s, ('labeled', 'acyclic', 'acyclic-noloop', 'unlabeled', 'unl-acyclic')):
                if v == TARGET: hits.append((name, f'{lo}..5', tag))
        # also 'follow it from anything': (model, start term) pairs
        pairs = sum(d[n][0] * n for n in range(1, 6))
        if pairs == TARGET: hits.append((name, '1..5 x start', 'pairs'))
        print()
    print("HITS for 592,260:", hits if hits else "none")


if __name__ == '__main__':
    main()
