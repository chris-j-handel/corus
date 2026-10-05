"""Session v383Op: Exhibit ONE's resolver beside a four-line plain rule, each case.

Runs from the repository root: python3 incoming/v383Op/plain_rule.py
Reads the newest Exhibit ONE at the root and executes its python block.

The plain rule, for one sharing a self carries at parity c (+1 or -1):
    s  = the one parity the offerings agree on, or 0 at none offered, at 0 offered, or at a parting
    c' = s if s != 0 else -c          (the carrying next, 11)
    o  = c' if c' != c else 0         (the changing shared, 10)
For a sharing the self carries none of: o = s, and c' = s if s != 0 else none.

Checked: every list of up to 4 offerings from {+, -, 0} at every carrying {+, -, none} at one
sharing (363 cases), and 20,000 random entries of up to 4 sharings and up to 6 offerings.
"""
import glob, itertools, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']


def plain(carrying, offerings):
    """carrying: dict key -> +1/-1 ; offerings: list of (key, -1/0/+1). Returns (shared dict, next dict)."""
    surfaced = {}
    for key, p in offerings:
        if p == 0:
            continue
        if key not in surfaced:
            surfaced[key] = p
        elif surfaced[key] != p:
            surfaced[key] = 0
    shared, nxt = {}, dict(carrying)
    for key in list(surfaced) + [k for k in carrying if k not in surfaced]:
        s = surfaced.get(key, 0)
        if key in carrying:
            c = carrying[key]
            c2 = s if s != 0 else -c
            shared[key] = c2 if c2 != c else 0
            nxt[key] = c2
        else:
            shared[key] = s
            if s != 0:
                nxt[key] = s
    return shared, nxt


if __name__ == '__main__':
    cases = 0
    for c in (1, -1, None):
        for n in range(0, 5):
            for offs in itertools.product((1, -1, 0), repeat=n):
                carrying = [] if c is None else [('k', c)]
                offerings = [('k', p) for p in offs]
                t, ch = _1(carrying, offerings)
                sh, nx = plain(dict(carrying), offerings)
                assert dict(t) == sh and dict(ch) == nx, (c, offs, t, ch, sh, nx)
                cases += 1
    random.seed(383)
    for _ in range(20000):
        keys = ['a', 'b', 'c', 'd']
        carrying = [(k, random.choice((1, -1))) for k in keys if random.random() < .6]
        offerings = [(random.choice(keys), random.choice((1, -1, 0))) for _ in range(random.randint(0, 6))]
        t, ch = _1(carrying, offerings)
        sh, nx = plain(dict(carrying), offerings)
        assert dict(t) == sh and dict(ch) == nx
    print('Exhibit ONE read at', exhibit_one)
    print('one sharing, each case:', cases, 'of', cases, 'agree')
    print('random entries: 20000 of 20000 agree')

    # the one-sharing cell as a map (c, s) -> (c', o): which arrivals leave the same thing behind
    print('\n(carrying, surfaced) -> (carrying next, shared)')
    seen = {}
    for c in (1, -1):
        for s in (1, -1, 0):
            sh, nx = plain({'k': c}, [('k', s)] if s else [])
            out = (nx['k'], sh['k'])
            seen.setdefault(out, []).append((c, s))
            print('  (%+d, %+d) -> (%+d, %+d)' % (c, s, out[0], out[1]))
    print('six arrivals, %d results; arrivals leaving the same result:' % len(seen),
          [v for v in seen.values() if len(v) > 1])

    # exchange of + and -: the rule is the same rule
    for c in (1, -1):
        for s in (1, -1, 0):
            a = plain({'k': c}, [('k', s)] if s else [])
            b = plain({'k': -c}, [('k', -s)] if s else [])
            assert a[0]['k'] == -b[0]['k'] and a[1]['k'] == -b[1]['k']
    print('exchange of + and - : the rule is alike at each of the six cells')
