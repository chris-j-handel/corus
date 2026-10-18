import json, subprocess
def trace(engine,N,turns,mode):
    cmd={'py':['python3','ring_ref_v265.py',str(N),str(turns),str(mode)],
         'c':['./ring_pure_v265',str(N),str(turns),str(mode)],
         'js':['node','ring_pure_v265.js',str(N),str(turns),str(mode)],
         'java':['java','RingPureV265.java',str(N),str(turns),str(mode)],
         'ocaml':['./ring_ml_v265',str(N),str(turns),str(mode)]}[engine]
    return json.loads(subprocess.check_output(cmd))
def attractor(tr): return len(set(tr[len(tr)//3:]))
engines=('py','c','js','java','ocaml')
print("=== v265 FIVE-SUBSTRATE cross-divide (typing x execution square, all four corners) ===")
allident=True
for mode,mn in [(0,'one-way'),(1,'both-ways')]:
    for N in [2,3,4,5,6,7]:
        ts=[trace(e,N,120,mode) for e in engines]
        ident=all(t==ts[0] for t in ts); allident=allident and ident
        print(f"  {mn:9} ring {N}: all-five-identical {ident}  attractor {attractor(ts[0])} {'(N*4='+str(N*4)+')' if mode==0 else ''}")
print(f"\nALL RING TRACES IDENTICAL ACROSS PY/C/JS/JAVA/OCAML: {allident}")
for N in [3,5,7]:
    aa={e:attractor(trace(e,N,200,0)) for e in engines}
    print(f"  competency reader ring {N}: {aa}  all==N*4({N*4}): {all(v==N*4 for v in aa.values())}")
