"""Two executings of Exhibit ONE's code, 6 November 2026, behind the droplets at Natural Resolver's gathering-value.
Run at the repository root of main: python3 incoming/v395/exhibit_one/executed_checks.py Exhibit_ONE_Natural_Resolver_v391.md
1. The order of 2-now-possibling makes no difference to 1-now-existing (each ordering, 3,000 random openings).
2. 1-now-existing with one 4-now-co-same-existing, each prior and each reaching: its 10-next-co-possibling and next prior."""
import sys, random, itertools
src = open(sys.argv[1], encoding='utf-8').read().split('```python')[1].split('```')[0]
ns = {}; exec(src, ns); f1 = ns['_1_now_existing']
random.seed(1); differ = n = 0
for _ in range(3000):
    keys = random.sample(['a', 'b', 'c'], random.randint(1, 3))
    two = [(random.choice(keys), random.choice([1, -1, 0])) for _ in range(random.randint(0, 5))]
    three = [(k, random.choice([1, -1])) for k in random.sample(keys, random.randint(0, len(keys)))]
    base = None
    for perm in itertools.permutations(two):
        o = f1(three, list(perm)); o = (sorted(o[0]), sorted(o[1])); n += 1
        if base is None: base = o
        elif o != base: differ += 1
print('1. orderings executed:', n, ' outcomes differing by order:', differ)
k = 'k'
for prior in ([(k, 1)], [(k, -1)], []):
    for two in ([], [(k, 0)], [(k, 1)], [(k, -1)], [(k, 1), (k, -1)], [(k, 1), (k, 1)]):
        ten, nxt = f1(prior, two)
        print('2. prior', prior[0][1] if prior else 'none', '| reaching', [p[1] for p in two], '| 10', [p[1] for p in ten], '| next prior', [p[1] for p in nxt])
