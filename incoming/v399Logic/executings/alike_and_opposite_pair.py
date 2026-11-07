# v399Logic, 7 November 2026: a reconstruction of Exhibit ONE v391's one-sharing cell table (its lines 798-811), not Exhibit ONE's own code. Report, Exhibit 15.
# One-sharing resolving per Exhibit ONE's cell table (798-811):
# receiving agreeing with prior -> share 0, prior same; anything else (inverse, 0, empty) -> prior inverts, share it.
def step(p, r):
    return (p, 0, True) if r == p else (-p, -p, False)
def run(pa, pb, n=8):
    ra = rb = None; out=[]
    for _ in range(n):
        pa, sa, ia = step(pa, rb if rb is not None else None) if True else None
        pb, sb, ib = step(pb, ra if ra is not None else None)
        out.append((sa, 'ingest' if ia else '-', sb, 'ingest' if ib else '-'))
        ra, rb = sa, sb
    return out
for name,(a,b) in {'alike':(-1,-1),'opposite':(-1,1)}.items():
    print(name, run(a,b))
