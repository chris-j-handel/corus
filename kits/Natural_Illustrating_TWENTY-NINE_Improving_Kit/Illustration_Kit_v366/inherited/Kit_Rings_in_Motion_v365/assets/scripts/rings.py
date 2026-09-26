import os
HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,'..','data'); IMG=os.path.join(HERE,'..','images')
import numpy as np, itertools
k=np.load(os.path.join(DATA,'circles.npy'))
# snap: three centres, three radii
C=[]
for x,y,r in k:
    if not any(np.hypot(x-a,y-b)<10 for a,b in C): C.append((x,y))
C=np.array(C); 
cen={}
for x,y,r in k:
    i=int(np.argmin(np.hypot(C[:,0]-x,C[:,1]-y)))
    cen.setdefault(i,[]).append(r)
names={}
for i,(x,y) in enumerate(C):
    names[i]='top' if y<300 else ('left' if x<220 else 'right')
cc={names[i]:C[i].mean(0) if False else C[i] for i in range(3)}
R={names[i]:sorted(cen[i]) for i in cen}
print('centres:',{n:tuple(np.round(v,1)) for n,v in cc.items()})
print('radii  :',{n:[round(r,1) for r in v] for n,v in R.items()})
def inter(p0,r0,p1,r1):
    d=np.linalg.norm(p1-p0); a=(r0*r0-r1*r1+d*d)/(2*d); h=np.sqrt(max(r0*r0-a*a,0))
    m=p0+a*(p1-p0)/d; perp=np.array([-(p1-p0)[1],(p1-p0)[0]])/d
    return m+h*perp, m-h*perp
groups={}
for A,B in [('left','right'),('top','left'),('top','right')]:
    for ia,ra in enumerate(R[A]):
        for ib,rb in enumerate(R[B]):
            for s,pt in zip(('+','-'),inter(cc[A],ra,cc[B],rb)):
                groups.setdefault((A,B,s),[]).append((ia,ib,pt))
print('groups:',len(groups),' crossings:',sum(len(v) for v in groups.values()))
print()
print('diamond centre dots (middle radius x middle radius), image coords, y down:')
dc={}
for key,v in groups.items():
    for ia,ib,pt in v:
        if ia==1 and ib==1: dc[key]=pt
for key,pt in sorted(dc.items(),key=lambda t:(round(t[1][1]),t[1][0])):
    print(f'  {key[0]:>5}-{key[1]:<5} side {key[2]} : x={pt[0]:6.1f}  y={pt[1]:6.1f}')
np.save(os.path.join(DATA,'diamond_centres.npy'),np.array([[*dc[k]] for k in sorted(dc)]))
