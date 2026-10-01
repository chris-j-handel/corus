"""
recognition.py - recognition as co-presence, the instrument.

Two selves, a common sequence offered to both, independent noise to each,
every surface presenting, own included. The read: stable against flipping.
A lone surface cannot part signal from noise; two co-presenting resolve the
common whole. Keys to Exhibit TWO, recognition as co-presence. Sign outputs only.
"""
import sys, random
sys.path.insert(0, '.')
from resolver import _1_self_coupling
from living import sign

class S:
    def __init__(self, n):
        self.n = n; self.__stands = {}; self.__carry = []
    def couple(self, acc):
        seq, self.__carry = _1_self_coupling(self.__carry, acc)
        self.__stands = {i: m for i, m in seq if 0 <= i < self.n}   # only what stands

    @property
    def surf(self):
        return [(i, m) for i, m in self.__stands.items()]

    def signs(self):
        return tuple(self.__stands.get(i, 0) for i in range(self.n))

def recognize(L, nselves, q=0.35, settle=400, span=120, seed=11):
    rng = random.Random(seed)
    common = tuple(random.Random(seed + 1).choice((1, -1)) for _ in range(L))
    selves = [S(L) for _ in range(nselves)]
    wins = [[] for _ in selves]
    for t in range(settle + span):
        for k, s in enumerate(selves):
            acc = [(i, m) for i, m in enumerate(common)]
            acc += [(i, rng.choice((1, -1))) for i in range(L) if rng.random() < q]
            for o in selves:
                acc += [(i, m) for i, m in o.surf if m != 0]
            s.couple(acc)
        if t >= settle:
            for k, s in enumerate(selves):
                wins[k].append(s.signs())
    whole = []
    for w in wins:
        ok = all(len({st[i] for st in w}) == 1 and common[i] in {st[i] for st in w}
                 for i in range(L))
        whole.append(ok)
    return all(whole)

if __name__ == '__main__':
    print('RECOGNITION AS CO-PRESENCE\n')
    print(f'  {sign(not recognize(60, 1))}   a lone surface cannot resolve the common')
    for L in (60, 120, 240):
        print(f'  {sign(recognize(L, 2))}   two co-presenting resolve it whole at length {L}')
