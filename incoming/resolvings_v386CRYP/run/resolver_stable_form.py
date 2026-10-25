"""The routing at the six cells of Natural Intelligence 4.3 with Resolving Hard Problems 3.2 at 14.
14 is all or none over the others alone; the self's inversion is at 12; 0 at 14 inverts a carried parity;
at a carrying of none, 0 chains nothing. Beside the kit, referred to and not relied on."""
def _14_surfacing(offerings):
    ps = {1 if c > 0 else -1 for s, c in offerings if c != 0}
    return next(iter(ps)) if len(ps) == 1 else (0 if ps else None)
def _12_coupling(carried, surfaced):
    if carried is None:
        return surfaced if surfaced else None          # colliding: q chained; 0 or none: nothing
    if surfaced == carried:
        return carried                                  # the between: prior carries on
    return -carried                                     # −p, 0 or none: the changing is
def next_parity(carried, offerings):
    return _12_coupling(carried, _14_surfacing(offerings))
if __name__ == '__main__':
    for carried in (1, None):
        for offs in ([], [(0,1)], [(0,-1)], [(0,1),(0,1)], [(0,1),(0,-1)], [(0,1),(0,1),(0,-1)]):
            print('carried', carried, 'others', [c for _, c in offs], '-> next', next_parity(carried, offs))
