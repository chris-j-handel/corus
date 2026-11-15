"""A 0 in sequence, each case: Natural Intelligence's sentence of each case checked, executed.

Usage, from outside the set's folder:  python3 -I zero_in_sequence.py <the set's folder>
Returned 15 November 2026, on the main line 574adce:
  2 selves, each of 6, 10 and 9 to either self or to none, each prior: 2916 cases, 0 other-than
  3 selves, each of 10 and 9 to any self or to none, each prior: 32768 cases, 0 other-than

The code is Exhibit ONE Natural Resolver's own, taken from the living file's lines and called by its names as they are.
A case is other-than if a self having a prior has a 0 with 10-next-co-possibling in sequence, over 48 moments,
longer than the selves its parities are from. A check of a reading, and no base of a sentence: it decides nothing.
"""
import glob, itertools, os, re, sys

R = sys.argv[1]
living = glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md'))
assert len(living) == 1, living
code = re.search(r"```python\n(.*?)```", open(living[0], encoding='utf-8').read(), re.S).group(1)
ns = {}
exec(code, ns)
one, seventeen = ns['_1_now_existing'], ns['_17_next_existing']
K = 'one sharing'

def cases(n, names, moments=48):
    total = other_than = 0
    for routes in itertools.product([None] + list(range(n)), repeat=n * len(names)):
        bi_couplings, from_selves = {}, [set() for _ in range(n)]
        for i in range(n):
            for j, name in enumerate(names):
                to = routes[i * len(names) + j]
                if to is not None:
                    bi_couplings[(i, name)] = to
                    from_selves[to].add(i)
        for priors in itertools.product([1, -1], repeat=n):
            total += 1
            society = {i: ([(K, priors[i])], []) for i in range(n)}
            run, longest = [0] * n, [0] * n
            for _ in range(moments):
                for i in range(n):
                    sharing, _next_prior = one(*society[i])
                    if dict(sharing).get(K) == 0:
                        run[i] += 1
                        longest[i] = max(longest[i], run[i])
                    else:
                        run[i] = 0
                society = seventeen(society, bi_couplings)
            if any(longest[i] > len(from_selves[i]) for i in range(n)):
                other_than += 1
    return total, other_than

for n, names, said in ((2, (6, 10, 9), 'each of 6, 10 and 9 to either self or to none'),
                       (3, (10, 9), 'each of 10 and 9 to any self or to none')):
    total, other_than = cases(n, names)
    print(f'{n} selves, {said}, each prior: {total} cases, {other_than} other-than')
