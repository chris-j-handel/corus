"""
diamond.py - geodesic re-routing (Exhibit TWO 5.4-5.5). One near self, two
coprime arms, one far self; the one life forked at successive moments, the
routing read as which arm carries the crossing first. The hold, the waver,
the snap; the routing a reading of no surface configuration - the router
sovereign. Signs, spans, orderings only.
"""
import sys, copy; sys.path.insert(0,'.')
from doors import Row, unrelating_pace
from living import sign

LENGTHS=[7,3,5,11]; ADJ={0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
P0=(1,-1,1,1,-1,1,-1); PB=(-1,1,-1,-1,1,-1,1)

def rows_at(pace='own'):
    """The four rows, each carrying its own pace and nothing beside them."""
    return [Row(n, phase=k % 2, alpha=(unrelating_pace(k) if pace == 'unrelating' else None))
            for k, n in enumerate(LENGTHS)]


def beat_all(rows,pat):
    for k,r in enumerate(rows):
        acc=[((i+1)%r.n,m) for i,m in r.surf if m!=0]
        if r.opens():
            for kk in ADJ[k]:
                acc+=[(i%r.n,m) for i,m in rows[kk].surf if m!=0]
        if k==0 and pat:
            acc+=[(i,m) for i,m in enumerate(pat) if m!=0]
        r.beat(acc)

def routing_string(T0=600, span=240, base_beats=2200, pace='own'):
    rows=rows_at(pace)
    base=[]
    for t in range(base_beats):
        beat_all(rows,P0); base.append(copy.deepcopy(rows))
    def routing(T):
        a=copy.deepcopy(base[T]); b=copy.deepcopy(base[T]); ta=tb=None
        for dt in range(300):
            beat_all(a,PB); beat_all(b,P0)
            if ta is None and a[1].signs()!=b[1].signs(): ta=dt
            if tb is None and a[2].signs()!=b[2].signs(): tb=dt
            if ta is not None and tb is not None: break
        if tb is None or (ta is not None and ta<tb): return 'A'
        if ta is None or tb<ta: return 'B'
        return '='
    return ''.join(routing(T0+i) for i in range(span)), base, T0

if __name__=='__main__':
    R,base,T0=routing_string()
    print('the routing per fork-moment (A the 3-arm, B the 5-arm):\n')
    for c in range(0,len(R),60): print(' ',R[c:c+60])
    holds=any(len(set(R[i:i+12]))==1 for i in range(len(R)-12))
    changes=sum(1 for i in range(1,len(R)) if R[i]!=R[i-1])
    wavers=any(R[i]!=R[i+1] and R[i+1]!=R[i+2] and R[i]==R[i+2] for i in range(len(R)-2))
    print(f'\n  the routing holds and changes {sign(holds and changes>0)}   ({changes} changes)')
    print(f'  the routing wavers around changes {sign(wavers)}')
    d={}; ok=True; reps=0
    for i,r in enumerate(R):
        k=(base[T0+i][1].signs(), base[T0+i][2].signs())
        if k in d:
            reps+=1
            if d[k]!=r: ok=False
        else: d[k]=r
    print(f'  the routing a reading of the coprime pair\'s surface {sign(ok and reps>0)}   ({reps} repeats met) - the router sovereign where no')
