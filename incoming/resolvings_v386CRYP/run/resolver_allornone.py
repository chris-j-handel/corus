"""The Natural Resolver's line 12 re-said as Resolving Hard Problems 3.2 says it:
a parity surfaces where every nonzero arriving agrees, 0 where any two part. No sum.
Everything else is the kit's resolver, unchanged. Laid beside the kit, not applied to it."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'kits', 'Natural_Networking_TWO_Improving_Kit', 'Natural_Networking_Test_Kit_v368'))
import resolver as kit

def _1_self_coupling(_3_self_carrying, _2_self_offering):
    _6_other_crossing = {s: t8 for s, c7, t8, t16 in _3_self_carrying}
    _14_social_crossing = [(s, c7) for s, c7 in _2_self_offering if c7 != 0]
    for s, c7, t8, t16 in _3_self_carrying:
        if c7 > 0: _14_social_crossing.append((s, -1))
        if c7 < 0: _14_social_crossing.append((s, 1))
    # 12, all or none at all: the set of parities arriving at each sharing
    _12_other_arrivings = {}
    for s, c7 in _14_social_crossing:
        _12_other_arrivings.setdefault(s, set()).add(1 if c7 > 0 else -1)
    _10_other_surfacing = [(s, next(iter(ps)) if len(ps) == 1 else 0) for s, ps in _12_other_arrivings.items()]
    _11_other_chaining = {}
    for s, c7, t8, t16 in _3_self_carrying:
        if t16 + 1 <= 3 or (t16 + 1 == 4 and t8 > 0):
            _11_other_chaining[s] = (c7, t8, t16 + 1)
    for s, c7 in _10_other_surfacing:
        if c7 != 0:
            _11_other_chaining[s] = (c7, 0 - _6_other_crossing.get(s, 1), 0)
    return (_10_other_surfacing, [(s, c7, t8, t16) for s, (c7, t8, t16) in _11_other_chaining.items()])

_9_other_releasing = kit._9_other_releasing
