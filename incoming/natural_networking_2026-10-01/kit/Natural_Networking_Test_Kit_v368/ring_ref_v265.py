import sys, json
from resolver import _1_self_coupling
def run(N, turns, mode):
    stands={i:(1 if i%2==0 else -1) for i in range(N)}; carry=[]; trace=[]
    for t in range(turns):
        accepted=[]
        for i in range(N):
            L=stands.get((i-1)%N)
            if L: accepted.append((i,L))
            if mode==1:
                R=stands.get((i+1)%N)
                if R: accepted.append((i,R))
        seq,carry=_1_self_coupling(carry,accepted)
        stands={i:m for i,m in seq if 0<=i<N}                 # only what stands
        surface=[stands.get(i,0) for i in range(N)]           # the trace's own line, made here
        carry=sorted(carry)                                   # the writing-down is the trace's
        cstr=";".join(f"{s}:{m}:{c}:{r}" for s,m,c,r in carry)
        trace.append("S="+",".join(map(str,surface))+" C="+cstr)
    return trace
N,turns,mode=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
print(json.dumps(run(N,turns,mode)))
