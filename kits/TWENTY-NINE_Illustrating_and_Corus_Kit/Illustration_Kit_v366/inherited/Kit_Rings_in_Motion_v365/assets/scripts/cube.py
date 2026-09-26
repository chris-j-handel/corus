from sympy.combinatorics import Permutation, PermutationGroup
def c(*cycles): return Permutation(list(cycles), size=49)
U = c((1,3,8,6),(2,5,7,4),(9,33,25,17),(10,34,26,18),(11,35,27,19))
D = c((41,43,48,46),(42,45,47,44),(14,22,30,38),(15,23,31,39),(16,24,32,40))
L = c((9,11,16,14),(10,13,15,12),(1,17,41,40),(4,20,44,37),(6,22,46,35))
R = c((25,27,32,30),(26,29,31,28),(3,38,43,19),(5,36,45,21),(8,33,48,24))
F = c((17,19,24,22),(18,21,23,20),(6,25,43,16),(7,28,42,13),(8,30,41,11))
B = c((33,35,40,38),(34,37,39,36),(3,9,46,32),(2,12,47,29),(1,14,48,27))
gens=[U,D,L,R,F,B]; names="UDLRFB"
G = PermutationGroup(gens)
print("order G      =", G.order())
print("expected     =", 43252003274489856000)
print("match        =", G.order()==43252003274489856000)
print("gen parity   =", [g.is_even for g in gens], "(False = odd permutation of the 48)")

# corner / edge sticker sets for this labelling
corner_st = {b+k for b in (0,8,16,24,32,40) for k in (1,3,6,8)}
edge_st   = {b+k for b in (0,8,16,24,32,40) for k in (2,4,5,7)}
print("corner stickers", len(corner_st), " edge stickers", len(edge_st))

def report(name, p):
    moved = [i for i in range(1,49) if p(i)!=i]
    mc = [i for i in moved if i in corner_st]; me=[i for i in moved if i in edge_st]
    print(f"\n{name}:  order={p.order()}  stickers moved={len(moved)}"
          f"  corner-stickers={len(mc)} -> {len(mc)//3} corner cubies"
          f"  edge-stickers={len(me)} -> {len(me)//2} edge cubies")
    print("   sticker cycles:", [tuple(cy) for cy in p.cyclic_form])

report("R (one quarter turn)", R)
comm = R*U*(R**-1)*(U**-1)          # sympy: left-to-right composition
report("[R,U] = R U R' U'", comm)
comm2 = U*R*(U**-1)*(R**-1)
report("[U,R]", comm2)
report("[[R,U],[U,R]]", comm*comm2*(comm**-1)*(comm2**-1))

print("\n=== commutating the commutators, with DISTINCT commutators ===")
def K(a,b): return a*b*(a**-1)*(b**-1)
pairs = {"[R,U]":K(R,U), "[F,R]":K(F,R), "[U,F]":K(U,F), "[L,U]":K(L,U)}
for n1,p1 in pairs.items():
    for n2,p2 in pairs.items():
        if n1<n2:
            k=K(p1,p2)
            moved=sum(1 for i in range(1,49) if k(i)!=i)
            print(f"  [{n1},{n2}] order={int(k.order())} stickers moved={moved}")

print("\n=== derived series ===")
G1 = G.derived_subgroup(); o1=G1.order()
print("G'  order =", o1, " index =", G.order()//o1)
G2 = G1.derived_subgroup(); o2=G2.order()
print("G'' order =", o2, " index in G' =", o1//o2)
print("G' perfect (G''==G') :", o2==o1)
