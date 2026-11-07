# v399Logic, 7 November 2026: the same reconstruction, a spiral of five alike selves along, one self removed at moment 8, the ring re-closing or left open. Report, Exhibit 16.
# Cell-table rule (Exhibit ONE 798-811), one sharing per self, a spiral along: each self receives the one before it.
def step(p, r): return (p, 0) if r == p else (-p, -p)
def run(n=5, steps=16, cut=8, mode="reclose", start=None):
    pri=list(start or [1]*n); shared=[None]*n; alive=list(range(n)); rows=[]
    for t in range(steps):
        if t==cut and mode!="none": alive.remove(2)        # an area of the surface removed
        new=shared[:]
        for k,i in enumerate(alive):
            if mode=="gap" and t>=cut and i==3: r=None      # the self past the removed area: nothing reaches
            else: r=shared[alive[k-1]]                       # the ring re-closing around it
            pri[i], new[i] = step(pri[i], r)
        shared=new
        rows.append(" ".join(f"{new[i]:+d}" if i in alive else " x" for i in range(n)))
    return rows
for mode in ["none","reclose","gap"]:
    rows=run(mode=mode)
    print(f"== {mode}: sharings per moment (selves 0-4)")
    print("   before cut:", " | ".join(rows[4:8]))
    print("   after cut: ", " | ".join(rows[8:14]))
