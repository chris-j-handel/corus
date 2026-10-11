import csv
from collections import Counter
rows=[dict(h=int(r['height']),t=int(r['timestamp']),n=int(r['tx_count']),nonce=int(r['nonce']),pool=r['pool']) for r in csv.DictReader(open('blocks_970618_970746.csv'))]
assert len(rows)==129
gaps=[rows[i]['t']-rows[i-1]['t'] for i in range(1,129)]
pace=['longer' if gaps[i]>gaps[i-1] else 'shorter' for i in range(1,128)]
alt=sum(1 for a,b in zip(pace,pace[1:]) if a!=b)
runs=[];cur=1
for a,b in zip(pace,pace[1:]):
    if a==b: cur+=1
    else: runs.append(cur);cur=1
runs.append(cur)
print('late stretch 970618-970746: 128 couplings')
print('pace alternations:',alt,'of',len(pace)-1,' longest run',max(runs))
print('negative gaps (now stamped before prior):',sum(1 for g in gaps if g<0), [ (rows[i+1]['h'],gaps[i]) for i in range(128) if gaps[i]<0])
print('gap mean',round(sum(gaps)/len(gaps)),'s min',min(gaps),'max',max(gaps),' pauses>1h:',[(rows[i+1]['h'],round(gaps[i]/3600,1)) for i in range(128) if gaps[i]>3600])
w=[r['n'] for r in rows]
print('width: mean',round(sum(w)/len(w)),'min',min(w),'max',max(w),' blocks of width<=21:',[(r['h'],r['n'],r['pool']) for r in rows if r['n']<=21])
# selves across along: pool changes between consecutive blocks
pools=[r['pool'] for r in rows]
print('distinct selves (pools):',len(set(pools)), Counter(pools).most_common(5))
print('self changes between consecutive blocks:',sum(1 for a,b in zip(pools,pools[1:]) if a!=b),'of 128')
nn=[r for r in rows if r['nonce']>0]
np=['odd' if r['nonce']%2 else 'even' for r in nn]
print('nonce (where recorded, n=%d): odd %d even %d, alternations %d of %d'%(len(nn),np.count('odd'),np.count('even'),sum(1 for a,b in zip(np,np[1:]) if a!=b),len(np)-1))
def pat(n):
    b=n&0xFF; return (0<=b<=9) or (19<=b<=58)
print('nonce low byte inside first-self range:',sum(pat(r['nonce']) for r in nn),'of',len(nn),' expected if no self',round(len(nn)*50/256,1))
