"""v386RR · The ways one self at one sharing can go from (its prior, what is offered)
to (its next, its releasing), counted under each condition.

Reads no file. Run:  python3 ways_at_one_sharing_v386RR.py

The space of ways, fixed by three sayings:
  - two parities at a sharing: prior p is + or -, next c is + or -
  - what is offered n is +, -, or none; agreeing offerings surface as one parity,
    parting offerings and no offering surface as none (nothing counted)
  - the releasing is the changing, or nothing: r = c at a changing, 0 at none
A way is a table f(p, n) -> c: 2**6 = 64 ways.

Three conditions then asked of a way:
  alike        + and - read alike: f(-p, -n) = -f(p, n)
  participates the offered parity participates in the next: f(p, +) differs from f(p, -) at some p
  none still   in no closed society does a self stay unchanged through the whole round the
               society comes to. Checked at every closed society of one to three selves
               (a self's own releasing arriving allowed) from every start, and at every
               society of four selves from nothing offered.
"""
from itertools import product

INPUTS = [(p, n) for p in (1, -1) for n in (1, -1, None)]
WAYS = [dict(zip(INPUTS, outs)) for outs in product((1, -1), repeat=6)]
sg = lambda v: '+' if v == 1 else '-'


def neg(n):
    return None if n is None else -n


def alike(f):
    return all(f[(-p, neg(n))] == -f[(p, n)] for p, n in INPUTS)


def participates(f):
    return any(f[(p, 1)] != f[(p, -1)] for p in (1, -1))


def surface(offs):
    s = {o for o in offs if o != 0}
    return s.pop() if len(s) == 1 else None


def a_self_still(f, n, edges, p0, r0):
    p, r = list(p0), list(r0)
    seen, hist = {}, []
    while (tuple(p), tuple(r)) not in seen:
        seen[(tuple(p), tuple(r))] = len(hist)
        hist.append(tuple(p))
        offered = [surface([r[j] for j in range(n) if (j, i) in edges]) for i in range(n)]
        c = [f[(p[i], offered[i])] for i in range(n)]
        r = [c[i] if c[i] != p[i] else 0 for i in range(n)]
        p = c
    cyc = hist[seen[(tuple(p), tuple(r))]:]
    return any(len({h[i] for h in cyc}) == 1 for i in range(n))


def none_still(f):
    for n in (1, 2, 3, 4):
        pairs = [(j, i) for j in range(n) for i in range(n) if n < 4 or i != j]
        for mask in range(2 ** len(pairs)):
            edges = {pairs[k] for k in range(len(pairs)) if mask >> k & 1}
            for p0 in product((1, -1), repeat=n):
                starts = product((1, -1, 0), repeat=n) if n < 4 else [(0,) * n]
                for r0 in starts:
                    if a_self_still(f, n, edges, p0, r0):
                        return False
    return True


def say(f):
    return 'carrying +: offered + -> %s, offered - -> %s, offered none -> %s' % (
        sg(f[(1, 1)]), sg(f[(1, -1)]), sg(f[(1, None)]))


if __name__ == '__main__':
    still = {id(f): none_still(f) for f in WAYS}
    A = [f for f in WAYS if alike(f)]
    print('all ways:', len(WAYS))
    print('alike:', len(A))
    print('alike, the offered parity participating:', len([f for f in A if participates(f)]))
    for f in A:
        print('   %s | participates: %s | none still: %s' % (say(f), participates(f), still[id(f)]))
    keep = [f for f in WAYS if alike(f) and participates(f) and still[id(f)]]
    print('alike, participating, none still:', len(keep))
    for f in keep:
        print('   ', say(f))
    print('each condition is its own:')
    print('   participating and none still, alike not asked:',
          len([f for f in WAYS if participates(f) and still[id(f)]]))
    print('   alike and none still, participating not asked:',
          len([f for f in WAYS if alike(f) and still[id(f)]]))
    print('   alike and participating, none still not asked:',
          len([f for f in WAYS if alike(f) and participates(f)]))
    ns = [f for f in WAYS if still[id(f)]]
    print('none still alone:', len(ns), '| each of them inverts when offered nothing:',
          all(f[(1, None)] == -1 and f[(-1, None)] == 1 for f in ns))
    f = keep[0]
    img = {}
    for p, n in INPUTS:
        c = f[(p, n)]
        img.setdefault((sg(c), sg(c) if c != p else '0'), set()).add(sg(p))
    print('at the first way kept, the prior read back from (next, releasing):',
          {k: sorted(v) for k, v in img.items()})

    states = [(a, b) for a in (1, -1) for b in (1, -1)]
    whole = free = 0
    for outs in product((1, -1), repeat=4):
        g = dict(zip(states, outs))
        step = {s: (s[1], g[s]) for s in states}
        if len(set(step.values())) == 4:
            whole += 1
            free += all(step[s] != s for s in states)
    print('the sixteen ways of (prior, now) -> (now, next): carrying the prior whole', whole,
          '| of those with no joint form still', free)
