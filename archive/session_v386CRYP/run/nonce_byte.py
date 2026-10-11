import csv
rows=[dict(h=int(r['height']),nonce=int(r['nonce'])) for r in csv.DictReader(open('blocks_0_134.csv'))]
# field's prior (Lerner): first miner's nonce low byte falls in 0x00-0x09 or 0x13-0x3A; other miners spread over 0x00-0xFF
def patoshi(n):
    b=n & 0xFF
    return (0<=b<=9) or (19<=b<=58)
inside=[r['h'] for r in rows if patoshi(r['nonce'])]
outside=[r['h'] for r in rows if not patoshi(r['nonce'])]
print('blocks 0-134:',len(rows))
print('low byte inside the one-self range:',len(inside))
print('outside:',len(outside),'heights',outside)
# chance that a uniform byte lands inside the range
frac=(10+40)/256
print('range covers',round(frac*100,1),'% of a uniform byte; expected inside if no self:',round(frac*len(rows),1))
# what the byte distribution looks like
from collections import Counter
c=Counter((r['nonce']&0xFF)//16 for r in rows)
print('low byte by 16-wide bins (0x00-0x0F ... 0xF0-0xFF):',[c.get(i,0) for i in range(16)])
