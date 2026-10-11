"""The between co-linear aiming into next momentarying, at the code and at the numbers 1 to 441: every 5 neutralling, every 10 floating. Run from the repository root."""
import re
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read(); ns={}
exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']
C=ns['CONNECTORS']
print('1. the along through the four corner dots, at Exhibit ONE: 9', C[9][1:], 'joined both ways with 17', C[17][1:], '; the four corners', {k:C[k][1:] for k in (2,6,10,14)})
comp={(0,9):1}; soc={0:([],[('s',1)]),1:([],[])}
for t in range(3):
    print(f'   momentary {t+1}: self 1 offered {[p for _,p in soc[1][1]]}; self 0 chained {dict(soc[0][0]).get("s")}')
    soc=F(soc,comp)
print('   each changing carried along at 9 arrives at the receiving self at the next momentary, 17 the society\'s next momentary')
print('2. every 5 at 1 to 441, Natural Mathematics line 85: neutralling co, odd, along; floating bi, even, across')
five=[k for k in range(1,442) if k%5==0]
neut=[k for k in five if k%2]; flo=[k for k in five if k%2==0]
print(f'   multiples of 5: {len(five)}; neutralling, odd: {len(neut)} ({neut[:4]}…{neut[-1]}); floating, every 10: {len(flo)} ({flo[:4]}…{flo[-1]})')
print('   alternating at each 5:', all((five[i]%2)!=(five[i+1]%2) for i in range(len(five)-1)))
print('3. at the ring of 440, Natural Numbers 11.1, each number k with its far side 440 - k: each fifth number meets a far side of its own kind')
print('   neutralling to neutralling:', all((440-k)%5==0 and (440-k)%2==1 for k in neut if k<440), '; floating to floating:', all((440-k)%10==0 for k in flo if k<=440))
print('   the waist 220 and the ring 440 floating:', 220%10==0, 440%10==0, '; 441 = 21 x 21, one past the ring:', 21*21)
print('4. at the code\'s seventeen names:', {k:(re.search(r'\| '+str(k)+r' \| ([^|]+) \| (odd|even)', body).group(1).strip(), 'neutralling, co' if k%2 else 'floating, bi') for k in (5,10,15)})
