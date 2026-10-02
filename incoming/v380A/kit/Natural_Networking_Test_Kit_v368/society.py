"""
society.py - the society of resolving, one instrument.

Coprime resolver-selves coupled and trading. Readings, each a sign:
the surplus present, absent, or captured; the whole gathering as one;
each later joiner adding more than the one before; the shared-factor
joiner adding less; the shared beat capturing where self-pacing holds.
Keys to Exhibit TWO, Part Four. One resolver, imported.
"""
import sys
sys.path.insert(0, '.')
from math import lcm
from living import Life, sign, YES, NO


def gather(sizes, pace='own', beats=None):
    life = Life(sizes, wiring='ring', pace=pace)
    life.gate()
    per = lcm(*[4 * n for n in sizes])
    life.live(beats or min(per * 3 + 1200, 16000))
    life.back = min(len(life.trace) - 10, per * 2)   # the window the society's own
    return life


if __name__ == '__main__':
    print('THE SOCIETY OF RESOLVING - readings as signs\n')
    prev = None
    grew_every = True
    last_mult = 0
    mult_grew = True
    for sizes in ([3, 5], [3, 5, 7], [3, 5, 7, 11]):
        life = gather(sizes)
        j = life.joint_span(life.back)
        if prev:
            if j <= prev: grew_every = False
            m = j / prev
            if m < last_mult: mult_grew = False
            last_mult = m
        prev = j
        print(f'  selves {sizes}: surplus {life.surplus(life.back)}   gathers as one {sign(life.joint_span(life.back)>0 and life.lands()==NO)}')
    print(f'\n  {sign(grew_every)}   every joining grows the whole')
    print(f'  {sign(mult_grew)}   each later joiner adds more than the one before')

    c_=gather([3, 5, 7], beats=1800); coprime=c_.joint_span(c_.back)
    s_=gather([3, 5, 9], beats=1800); shared=s_.joint_span(s_.back)
    print(f'  {sign(shared < coprime)}   the shared-factor joiner adds less: dissolving at the joining')

    clocked = gather([3, 5, 7], pace='clock', beats=1800)
    print(f'  self-paced surplus: {gather([3,5,7],beats=1800).surplus()}   clocked surplus: {clocked.surplus()}')
    print(f'  {sign(clocked.surplus()=="captured")}   the shared beat captures where self-pacing holds')
