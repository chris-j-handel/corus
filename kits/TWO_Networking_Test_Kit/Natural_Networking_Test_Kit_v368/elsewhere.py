"""
elsewhere.py - co-releasing needs an elsewhere (Exhibit TWO 2.5, 2.1-2.4).
One life fed its own emanation at a span of sequence: near spans dead, far
spans living, the response each arrangement's own. Signs only.
"""
import sys; sys.path.insert(0,'.')
from doors import Row, unrelating_pace
from living import sign

def cones_om(trace, W=400, skip=4):
    seen=set(); wins=[]
    for w0 in range(0,len(trace),W):
        win=trace[w0:w0+W]
        wins.append(any(tuple(st) not in seen for st in win))
        for st in win: seen.add(tuple(st))
    return all(wins[skip:] or wins)

def life_self(lengths, beats, D, pace='own'):
    A=[Row(n,phase=k%2,alpha=(unrelating_pace(k) if pace=='unrelating' else None))
       for k,n in enumerate(lengths)]
    tr=[]; hist=[]
    for t in range(beats):
        for k,r in enumerate(A):
            acc=[((i+1)%r.n,m) for i,m in r.surf if m!=0]
            if r.opens():
                for kk in sorted({(k-1)%len(A),(k+1)%len(A)}-{k}):
                    acc+=[(i%r.n,m) for i,m in A[kk].surf if m!=0]
            if k==0 and len(hist)>=D:
                s=hist[-D]
                if s!=0: acc.append((0,s))
            r.beat(acc)
        tr.append(tuple(x.signs() for x in A))
        hist.append(A[2].at(0))                  # the sign at sequencing zero, not the first that stands
    return tr

if __name__=='__main__':
    print('THE ELSEWHERE - the reach per span of self-distance\n')
    for D in (2,21,55,60,65,137):
        om=cones_om(life_self([5,6,7],6000,D))
        print(f'  span {D:>3}: omegaing sustained {sign(om)}')
