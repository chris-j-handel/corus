"""Six forward at one sharing and at three sharings, on the kit's resolver (sum at 12) and on the re-said one (all or none at 12)."""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'kits', 'Natural_Networking_TWO_Improving_Kit', 'Natural_Networking_Test_Kit_v368'))
import resolver as kit, resolver_allornone as said

def chain(coupling, carry, offers):
    carry = list(carry); out = []
    for offering in offers:
        surf, carry = coupling(carry, offering)
        out.append((tuple(sorted(surf)), tuple(sorted(carry))))
    return out

def report(name, coupling):
    print('==', name)
    # one sharing, offerings in {-1,0,+1}^6
    start = [(0, 1, 1, 0)]
    alt = fixed = own = zero = 0; surfaces = set()
    for offs in itertools.product([-1, 0, 1], repeat=6):
        out = chain(coupling, start, [[(0, o)] if o else [] for o in offs])
        ps = [dict(s).get(0, 0) for s, _ in out]
        if ps[0] and all(ps[i] and ps[i] == -ps[i-1] for i in range(1, 6)): alt += 1; surfaces.add(tuple(ps))
        if any(ps[i] and ps[i] == ps[i-1] for i in range(1, 6)): fixed += 1
        if any(c == tuple(sorted(start)) for _, c in out): own += 1
        if 0 in ps: zero += 1
    print('  one sharing: of 729 offering sequences, six alternating', alt, 'at surface sequences', len(surfaces), '| fixed still', fixed, '| own form again', own, '| a 0 somewhere', zero)
    # two arrivings at one sharing each step, with the carry: the forking case of step 525
    start = [(0, 1, 1, 0)]
    for offs in [[(0, 1), (0, 1)], [(0, -1), (0, -1)], [(0, 1), (0, -1)]]:
        out = chain(coupling, start, [offs] * 6)
        print('  carry +, two arrivings', [p for _, p in offs], 'each step -> surfaces', [dict(s).get(0, 0) for s, _ in out])
    # three sharings, the self alternating at each, offerings at sharing 1 only; does position advance (spiral) or return (ring)?
    start = [(0, 1, 1, 0), (1, -1, 1, 0), (2, 1, -1, 0)]
    out = chain(coupling, start, [[] for _ in range(6)])
    forms = [c for _, c in out]
    print('  three sharings, no offering: carry returns to its start at steps', [i + 1 for i, c in enumerate(forms) if c == tuple(sorted(start))], '| distinct forms in six', len(set(forms)))
    out = chain(coupling, start, [[(1, 1)], [], [(1, 1)], [], [(1, 1)], []])
    print('  three sharings, + offered at sharing 1 every other step: surfaces', [tuple(dict(s).get(k, 0) for k in range(3)) for s, _ in out])

report('kit resolver, 12 as a sum', kit._1_self_coupling)
report('re-said resolver, 12 all or none', said._1_self_coupling)
