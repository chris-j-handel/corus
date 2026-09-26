import os
HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,'..','data'); IMG=os.path.join(HERE,'..','images')
import cv2, numpy as np
img=cv2.imread(os.path.join(IMG,'rings_and_cube_image_A.png'))
sub=img[:, 460:880].copy()
gray=cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY)
circ=cv2.HoughCircles(cv2.medianBlur(gray,3),cv2.HOUGH_GRADIENT,dp=1,minDist=14,param1=80,param2=14,minRadius=7,maxRadius=12)
circ=np.round(circ[0]).astype(int)
def colour(b,g,r):
    if r>235 and g>235 and b>235: return 'white'
    hsv=cv2.cvtColor(np.uint8([[[b,g,r]]]),cv2.COLOR_BGR2HSV)[0,0]; h,s,v=[int(x) for x in hsv]
    if s<60: return 'grey?'
    if h<8 or h>170: return 'red'
    if h<18: return 'orange'
    if h<35: return 'yellow'
    if h<90: return 'green'
    if h<135: return 'blue'
    return '?'
dots=[]
for x,y,r in circ:
    patch=sub[y-3:y+4,x-3:x+4].reshape(-1,3); b,g,rr=np.median(patch,0).astype(int)
    c=colour(b,g,rr)
    if c in ('grey?','?'): continue
    dots.append((x+460,y,c))
from collections import Counter
print('dots found:',len(dots)); print(Counter(c for _,_,c in dots))
np.save(os.path.join(DATA,'dots.npy'),np.array([(x,y) for x,y,_ in dots])); 
open(os.path.join(DATA,'dots_colours.txt'),'w').write('\n'.join(f'{x} {y} {c}' for x,y,c in dots))
