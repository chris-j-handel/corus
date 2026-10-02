"""
retell.py - retelling, thinning, and the coprime resolver (Exhibit TWO
3.1-3.5). Twin-life divergence: the crossing's travel span per middle;
identity carried through an odd middle; membranes accelerating the thinned
sign; prime chains absorbing. Signs and spans only.
"""
import sys; sys.path.insert(0,'.')
from doors import Row, unrelating_pace
from living import sign

def chain_run(lengths, schedule, beats, pace='own'):
    rows=[Row(n,phase=k%2,alpha=(unrelating_pace(k) if pace=='unrelating' else None))
          for k,n in enumerate(lengths)]
    tr=[]
    for t in range(beats):
        pat=None
        for st,p in schedule:
            if t>=st: pat=p
        for k,r in enumerate(rows):
            acc=[((i+1)%r.n,m) for i,m in r.surf if m!=0]
            if r.opens():
                for kk in [j for j in (k-1,k+1) if 0<=j<len(lengths)]:
                    acc+=[(i%r.n,m) for i,m in rows[kk].surf if m!=0]
            if k==0 and pat:
                acc+=[(i,m) for i,m in enumerate(pat) if m!=0]
            r.beat(acc)
        tr.append(tuple(r.signs() for r in rows))
    return tr

P0=(1,-1,1,1,-1); PB=(-1,1,-1,-1,1); PC=(1,1,-1,1,-1); T1=3000

def travel(lengths, beats=9000, pace='own'):
    w=chain_run(lengths,[(0,P0),(T1,PB)],beats,pace)
    wo=chain_run(lengths,[(0,P0)],beats,pace)
    far=len(lengths)-1
    for t in range(T1,beats):
        if w[t][far]!=wo[t][far]: return t-T1
    return None

if __name__=='__main__':
    print('IDENTITY THROUGH THE RETELLING (odd middle)\n')
    tr=chain_run([5,11,7],[(0,P0),(2500,PB),(5000,P0),(7500,PC)],10000)
    far=2
    sB=frozenset(st[far] for st in tr[4300:4900])
    sC=frozenset(st[far] for st in tr[9300:9900])
    print(f'  two changings, two far livings: {sign(sB!=sC)}\n')
    print('THE LADDER - travel span per middle (twin-life divergence)\n')
    for lengths,name in (([5,7],'direct'),([5,6,7],'one membrane'),
                         ([5,6,4,6,7],'three membranes'),
                         ([5,11,7],'one prime'),([5,11,13,3,7],'three primes')):
        d=travel(lengths)
        print(f'  {name:>16}: arrives after {d if d is not None else "never (the absorption)"}')
