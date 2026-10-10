"""Session v385M, concern 1, why two. No file is read; this is a count anyone can repeat.
Run from the repository root:  python3 incoming/v385M/three_check.py

A way names a next from a prior and a now, each one of k forms. Asked of each way:
  alike   - does it treat each form alike, the same way whichever form is called which?
  whole   - does it carry the prior whole, no two joint forms going to one?
  no still- does it leave no joint form (prior, now) as it is?
Natural Intelligence 2.4 asks the second and third at two forms. The first is added here: a way that needs the
forms told apart beforehand needs something laid over them from beside."""
import itertools

def ways_alike(k, perms):
    """each way f(prior, now) -> next that is the same way under each relabelling in perms"""
    forms = range(k)
    pairs = [(p, n) for p in forms for n in forms]
    reps, seen = [], set()
    for pr in pairs:                       # one pair from each family of pairs the relabellings carry to each other
        if pr in seen:
            continue
        reps.append(pr)
        for g in perms:
            seen.add((g[pr[0]], g[pr[1]]))
    choices = []
    for (p, n) in reps:                    # a next is allowed at a pair when each relabelling leaving the pair as it is leaves the next as it is
        stay = [g for g in perms if g[p] == p and g[n] == n]
        choices.append([v for v in forms if all(g[v] == v for g in stay)])
    for pick in itertools.product(*choices):
        f = {}
        for (p, n), v in zip(reps, pick):
            for g in perms:
                f[(g[p], g[n])] = g[v]
        yield f

def tell(k, perms, name):
    pairs = [(p, n) for p in range(k) for n in range(k)]
    total = whole = clean = 0
    for f in ways_alike(k, perms):
        total += 1
        step = {pr: (pr[1], f[pr]) for pr in pairs}
        if len(set(step.values())) == len(pairs):
            whole += 1
            if all(step[pr] != pr for pr in pairs):
                clean += 1
                cyc, seen = [], set()
                for pr in pairs:
                    length, t = 0, pr
                    while t not in seen:
                        seen.add(t); t = step[t]; length += 1
                    if length:
                        cyc.append(length)
                print("      a way with no still at %d forms, %s: its joint forms go round in cycles of %s" % (k, name, sorted(cyc)))
    print("   %d forms, %s: ways treating each form alike %d; carrying the prior whole %d; and leaving no joint form still %d"
          % (k, name, total, whole, clean))

print("A. Each form treated alike, nothing laid over the forms")
for k in (2, 3, 4, 5):
    tell(k, list(itertools.permutations(range(k))), "each relabelling")

print("\nB. Brute count at two and three forms, each way of the %d and the %d, the same question" % (2 ** 4, 3 ** 9))
for k in (2, 3):
    pairs = [(p, n) for p in range(k) for n in range(k)]
    perms = list(itertools.permutations(range(k)))
    alike = clean = 0
    for outs in itertools.product(range(k), repeat=len(pairs)):
        f = dict(zip(pairs, outs))
        if any(f[(g[p], g[n])] != g[f[(p, n)]] for g in perms for (p, n) in pairs):
            continue
        alike += 1
        step = {pr: (pr[1], f[pr]) for pr in pairs}
        clean += len(set(step.values())) == len(pairs) and all(step[pr] != pr for pr in pairs)
    print("   %d forms: ways treating each form alike %d; of them carrying the prior whole with no still %d" % (k, alike, clean))

print("\nC. Three forms with one order round them laid over each self, the same at each momentary")
tell(3, [(0, 1, 2), (1, 2, 0), (2, 0, 1)], "turnings of the one order only")

print("\nD. What a form alike at prior and now can go to, each form treated alike")
for k in (2, 3, 4):
    perms = list(itertools.permutations(range(k)))
    stay = [g for g in perms if g[0] == 0]
    free = [v for v in range(k) if all(g[v] == v for g in stay)]
    print("   %d forms: from (a, a) the next can be %s" % (k, "a, or the one other" if len(free) == 2 else "a alone"))
