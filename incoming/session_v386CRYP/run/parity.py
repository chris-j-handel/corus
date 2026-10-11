import csv
rows=[dict(h=int(r['height']),t=int(r['timestamp']),n=int(r['tx_count']),nonce=int(r['nonce'])) for r in csv.DictReader(open('blocks_0_134.csv'))]
rows=rows[:129]  # blocks 0..128 = 128 couplings
out=[]
for i in range(1,129):
    p,c=rows[i-1],rows[i]
    gap=c['t']-p['t']
    prevgap=(p['t']-rows[i-2]['t']) if i>=2 else None
    pace = None if prevgap is None else ('longer' if gap>prevgap else 'shorter')
    out.append(dict(coupling=i, prior=p['h'], now=c['h'], gap_s=gap, pace=pace,
        second_self='is' if c['n']>1 else 'is not',
        nonce_parity='odd' if c['nonce']%2 else 'even',
        pause='is' if gap>3600 else 'is not'))
with open('couplings_0_128.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())+['possible']); w.writeheader()
    for o in out: o['possible']=''; w.writerow(o)
# observings
pace=[o['pace'] for o in out if o['pace']]
alt=sum(1 for a,b in zip(pace,pace[1:]) if a!=b)
print('couplings',len(out))
print('second self is:',sum(o['second_self']=='is' for o in out),'/ 128')
print('pace longer:',pace.count('longer'),'shorter:',pace.count('shorter'))
print('pace alternations (changes between consecutive couplings):',alt,'of',len(pace)-1)
runs=[];cur=1
for a,b in zip(pace,pace[1:]):
    if a==b: cur+=1
    else: runs.append(cur);cur=1
runs.append(cur)
print('longest same-pace run:',max(runs),' run-length distribution:',{k:runs.count(k) for k in sorted(set(runs))})
np=[o['nonce_parity'] for o in out]
print('nonce odd:',np.count('odd'),'even:',np.count('even'),'alternations:',sum(1 for a,b in zip(np,np[1:]) if a!=b),'of 127')
print('pauses >1h at couplings:',[(o['coupling'],round(o['gap_s']/3600,1)) for o in out if o['pause']=='is'])
gaps=[o['gap_s'] for o in out if o['pause']=='is not']
print('working gaps: n',len(gaps),'mean',round(sum(gaps)/len(gaps)),'s  min',min(gaps),'max',max(gaps))
