import sys, itertools, os
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', '..', 'kits/Natural_Networking_TWO_Improving_Kit/Natural_Networking_Test_Kit_v368'))
from resolver import _1_self_coupling
# one sharing (name 0). carrying rows: (sharing, corusing ±1/0, torusing ±1, social_torusing age 0..3)
def run(start_carry, offers):
    carry = list(start_carry); out = []
    for o in offers:
        offering = [(0, o)] if o != 0 else []
        surf, carry = _1_self_coupling(carry, offering)
        p = dict(surf).get(0, 0)
        out.append((p, tuple(sorted(carry))))
    return out
results = {}
for start in [[(0, 1, 1, 0)], [(0, -1, 1, 0)], [(0, 1, -1, 0)], []]:
    tally = dict(alternating_six=0, fixed_still=0, own_form_again=0, zero_surfaces=0, total=0, examples=[])
    for offers in itertools.product([-1, 0, 1], repeat=6):
        out = run(start, offers); tally['total'] += 1
        ps = [p for p, _ in out]; carries = [c for _, c in out]
        if all(ps[i] != 0 and ps[i] == -ps[i-1] for i in range(1, 6)) and ps[0] != 0:
            tally['alternating_six'] += 1
            if len(tally['examples']) < 3: tally['examples'].append((offers, ps))
        if any(ps[i] == ps[i-1] and ps[i] != 0 for i in range(1, 6)): tally['fixed_still'] += 1
        if any(c == tuple(sorted(start)) for c in carries): tally['own_form_again'] += 1
        if 0 in ps: tally['zero_surfaces'] += 1
    results[str(start)] = tally
for k, v in results.items():
    print('start', k); 
    for kk, vv in v.items(): print('  ', kk, vv)
# the carry's age cap: chain the start with no offering at all
print('\nno offering, six forward from [(0,1,1,0)]:')
for i, (p, c) in enumerate(run([(0, 1, 1, 0)], [0]*6), 1): print('  step', i, 'surface', p, 'carry', c)
print('no offering, six forward from [(0,1,-1,0)]:')
for i, (p, c) in enumerate(run([(0, 1, -1, 0)], [0]*6), 1): print('  step', i, 'surface', p, 'carry', c)
