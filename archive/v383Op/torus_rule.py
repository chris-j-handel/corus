"""Session v383Op: the torus of selves, Exhibit ONE's rule worked at more pairs.

Runs from the repository root: python3 incoming/v383Op/torus_rule.py [largest q, default 61]
Reads the newest Exhibit ONE at the root and executes its python block.

Arrangement as Exhibit ONE's table says it: p selves along, q across, each releasing along (9)
to the next along and sharing across (10) to the next across, the last to the first; one sharing;
first momentary one self carries -, the selves alternating along and across; none offered from
beyond. The rule read at the table's header: both numbers odd, p the smaller: the parities come
again at q at a q more than twice p, and at 4p at each other q.

The plain rule (plain_rule.py) is used for speed; it is first matched against the resolver
itself, momentary by momentary, at each torus up to 5 by 7.
"""
import glob, re, sys

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_17 = ns['_17_co_bi_tri_offering']


def opening(p, q):
    return [[-1 if (i + j) % 2 == 0 else 1 for j in range(q)] for i in range(p)]


def step_plain(c, o, p, q):
    """c: carrying; o: what each self shared last momentary (0 at none). Returns next (c, o)."""
    c2 = [[0] * q for _ in range(p)]
    o2 = [[0] * q for _ in range(p)]
    for i in range(p):
        for j in range(q):
            a, b = o[i - 1][j], o[i][j - 1]          # from along, from across
            if a and b:
                s = a if a == b else 0
            else:
                s = a or b
            n = s if s else -c[i][j]
            c2[i][j] = n
            o2[i][j] = n if n != c[i][j] else 0
    return c2, o2


def carried_form(p, q):
    """After the coming again has begun: which of two forms the torus is at.
    'across': each momentary the whole pattern is the last one carried one self on across.
    'along' : two momentaries on, the whole pattern is inverted and carried one self on along."""
    T, first = period(p, q)
    c, o = opening(p, q), [[0] * q for _ in range(p)]
    hist = [c]
    for _ in range(first + 2 * T + 4):
        c, o = step_plain(c, o, p, q)
        hist.append(c)
    span = range(first + 1, first + 2 * T + 2)
    across = all(hist[t + 1] == [[hist[t][i][j - 1] for j in range(q)] for i in range(p)] for t in span)
    along = all(hist[t + 2] == [[-hist[t][i - 1][j] for j in range(q)] for i in range(p)] for t in span)
    return across, along


def run_resolver(p, q, steps):
    society = {(i, j): ([('s', opening(p, q)[i][j])], []) for i in range(p) for j in range(q)}
    joins = {}
    for i in range(p):
        for j in range(q):
            joins[((i, j), 9)] = ((i + 1) % p, j)
            joins[((i, j), 10)] = (i, (j + 1) % q)
    out_carry = []
    for _ in range(steps):
        out = _17(society, joins)
        society = {k: (out[k][0], out[k][1]) for k in society}
        out_carry.append([[dict(society[(i, j)][0])['s'] for j in range(q)] for i in range(p)])
    return out_carry


def period(p, q):
    c, o = opening(p, q), [[0] * q for _ in range(p)]
    seen, t = {}, 0
    while True:
        key = (tuple(map(tuple, c)), tuple(map(tuple, o)))
        if key in seen:
            # period; and the momentary the releasings come again from (Exhibit ONE's column:
            # the releasings of momentary m are what is arriving as momentary m + 1 opens)
            return t - seen[key], seen[key]
        seen[key] = t
        c, o = step_plain(c, o, p, q)
        t += 1


if __name__ == '__main__':
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    print('Exhibit ONE read at', exhibit_one)
    matched = 0
    for p in range(1, 6):
        for q in range(p, 8):
            c, o = opening(p, q), [[0] * q for _ in range(p)]
            ref = run_resolver(p, q, 30)
            for t in range(30):
                c, o = step_plain(c, o, p, q)
                assert c == ref[t], (p, q, t)
            matched += 1
    print('plain rule and resolver alike at each of 30 momentaries: %d of %d toruses, 1 by 1 to 5 by 7' % (matched, matched))

    print("\nExhibit ONE's rows:")
    for p, q, want in ((1, 3, 3), (2, 3, 2), (1, 5, 5), (3, 3, 12), (3, 5, 12), (3, 7, 7), (3, 13, 13),
                       (5, 7, 20), (5, 11, 11), (7, 17, 17), (17, 59, 59)):
        T, first = period(p, q)
        print('  %2d by %2d: %3d, the releasings again from momentary %2d %s' % (p, q, T, first, 'as the table' if T == want else 'TABLE SAYS %d' % want))

    print('\nthe rule at each odd pair, p from 1, q to %d:' % top)
    agree, part = 0, []
    forms = {'across': [0, 0], 'along': [0, 0]}
    onset = {'across': set(), 'along': set()}
    for p in range(1, top + 1, 2):
        for q in range(p, top + 1, 2):
            T, first = period(p, q)
            rule = q if q > 2 * p else 4 * p
            if T == rule:
                agree += 1
            else:
                part.append((p, q, T, rule, first))
            if p >= 3:
                across, along = carried_form(p, q)
                side = 'across' if q > 2 * p else 'along'
                forms[side][1] += 1
                forms[side][0] += (across and not along) if side == 'across' else (along and (not across or p == q))
                onset[side].add(first - 3 * p)
    print('  agreeing: %d of %d' % (agree, agree + len(part)))
    print('  p from 3, q more than twice p: the pattern carried one self on across at each momentary, at %d of %d;'
          % tuple(forms['across']))
    print('     the releasings again from momentary 3p + %s' % sorted(onset['across']))
    print('  p from 3, each other q: two momentaries on the pattern inverted and carried one self on along, at %d of %d;'
          % tuple(forms['along']))
    print('     the releasings again from momentary 3p + %s' % sorted(onset['along']))
    for p, q, T, rule, first in part:
        print('  parting: %2d by %2d comes again at %d, the rule says %d (from momentary %d)' % (p, q, T, rule, first))
