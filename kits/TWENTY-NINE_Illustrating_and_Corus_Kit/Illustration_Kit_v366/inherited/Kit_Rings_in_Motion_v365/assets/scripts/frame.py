import os
HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,'..','data'); IMG=os.path.join(HERE,'..','images')
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k=np.load(os.path.join(DATA,'circles.npy'))
C={'top':np.array([220.7,262.4]),'left':np.array([171.6,347.0]),'right':np.array([270.3,347.0])}
R={}
for x,y,r in k:
    n=min(C,key=lambda n:np.hypot(*(C[n]-[x,y]))); R.setdefault(n,[]).append(r)
for n in R: R[n]=sorted(R[n])
def inter(p0,r0,p1,r1):
    d=np.linalg.norm(p1-p0); a=(r0*r0-r1*r1+d*d)/(2*d); h=np.sqrt(max(r0*r0-a*a,0))
    m=p0+a*(p1-p0)/d; perp=np.array([-(p1-p0)[1],(p1-p0)[0]])/d
    return m+h*perp, m-h*perp
dots=[];centres=[]
for A,B in [('left','right'),('top','left'),('top','right')]:
    for ia,ra in enumerate(R[A]):
        for ib,rb in enumerate(R[B]):
            for pt in inter(C[A],ra,C[B],rb):
                dots.append(pt)
                if ia==1 and ib==1: centres.append(pt)
dots=np.array(dots); centres=np.array(centres)
ink='#2b2b2b'; muted='#9a9a9a'; accent='#1f5fbf'
fig,ax=plt.subplots(figsize=(7,8),dpi=150)
fig.patch.set_facecolor('white'); ax.set_facecolor('white')
for n in C:
    for r in R[n]:
        ax.add_patch(plt.Circle(C[n],r,fill=False,lw=0.9,color=muted))
ax.scatter(dots[:,0],dots[:,1],s=10,color=ink,zorder=3)
ax.scatter(centres[:,0],centres[:,1],s=70,facecolor='white',edgecolor=ink,lw=1.4,zorder=4)
# axes: along 23 (bottom) -> 25 (top centre); across through the two middle diamonds
b=centres[np.argmax(centres[:,1])]; t=min(centres,key=lambda p:(p[1],abs(p[0]-221)))
mid=sorted([p for p in centres if 300<p[1]<400],key=lambda p:p[0])
ax.plot([b[0],t[0]],[b[1],t[1]],color=accent,lw=2,zorder=2)
ax.plot([mid[0][0],mid[1][0]],[mid[0][1],mid[1][1]],color=accent,lw=2,zorder=2)
X=np.array([(b[0]+t[0])/2,(mid[0][1]+mid[1][1])/2])
ax.add_patch(plt.Circle(X,7,fill=False,lw=1.6,color=accent,ls=(0,(2,2)),zorder=5))
ax.annotate('23',b,xytext=(12,-4),textcoords='offset points',color=ink,fontsize=11)
ax.annotate('25',t,xytext=(-22,8),textcoords='offset points',color=ink,fontsize=11)
ax.annotate('the one nothing:\non no ring, at no crossing',X,xytext=(150,-150),textcoords='offset points',color=accent,fontsize=9,arrowprops=dict(arrowstyle='-',color=accent,lw=0.8))
ax.set_xlim(40,400); ax.set_ylim(480,170); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('The rings as the instrument returned them: 54 crossings, six nine-dot diamonds,\nalong 23 to 25, across through the two middle centres',fontsize=10,color=ink)
fig.savefig(os.path.join(IMG,'rings_returned_first_frame.png'),bbox_inches='tight')
np.savez(os.path.join(DATA,'rings_returned.npz'),ring_centres=np.array(list(C.values())),radii=np.array([R[n] for n in C]),crossings=dots,diamond_centres=centres,nothing=X)
print('nothing at',X.round(1),' dist to centres',[round(float(np.hypot(*(X-C[n]))),1) for n in C])
print('23 to nothing',round(float(np.hypot(*(b-X))),1),' 25 to nothing',round(float(np.hypot(*(t-X))),1))
print('across halves',[round(float(np.hypot(*(p-X))),1) for p in mid])
