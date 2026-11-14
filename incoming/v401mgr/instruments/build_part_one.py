"""build the page of part one: each place, its living words and its next words; each living string asserted word for word at its line."""
import sys
R=sys.argv[1]
NI='Natural_Intelligence_v401mgr.md'; E1='Exhibit_ONE_Natural_Resolver_v401mgr.md'; NN='Exhibit_TWENTY_Natural_Naming_v401mgr.md'; TH='Exhibit_THIRTY_Co-Chaining_Logic_Registry_v401mgr.md'
W="each self's next prior and the parities it will be observing"
core=[
 (NI,432,"Exhibit ONE inside it, *Seventeen names*","| existing, a next 1 | 0000 again |","| existing | 0000 again |"),
 (NI,800,"Exhibit ONE inside it, the relations of 17","completing with 17-next-existing, a next 1-now-existing","completing with 17-next-existing, "+W),
 (NI,1592,"4.7","a next now, each self's next 1-now-existing with a same-existing-society's momentary.","a next now, "+W+", with a same-existing-society's momentary."),
 (NI,1606,"4.8","**Each step is four names, and 17 a next 1**:","**Each step is four names, and 17 each self's next prior**:"),
 (NI,1612,"4.9","17-next-existing is a next 1-now-existing.","17-next-existing is "+W+"."),
 (E1,138,"*Seventeen names*","| existing, a next 1 | 0000 again |","| existing | 0000 again |"),
 (E1,506,"the relations of 17","completing with 17-next-existing, a next 1-now-existing","completing with 17-next-existing, "+W),
 (NN,504,"3.1","17-next-existing is next 1-now-existing.","17-next-existing is "+W+"."),
 (NN,510,"3.1","and 17-next-existing is next 1-now-existing.","and 17-next-existing is "+W+"."),
 (NN,540,"3.3","| existing, a next 1 | one |","| existing | one |"),
 (NN,542,"3.3","17-next-existing is a next 1, and 1's three is 17's, co-bi-tri, its two priors 16 and 15;","17's three is 1's, co-bi-tri, its two priors 16 and 15;"),
 (NN,550,"3.4","and 17-next-existing is next 1-now-existing.","and 17-next-existing is "+W+"."),
 (NN,1683,"5.63","and with 17 a next now, a next 1, 17-next-existing.","and with 17 a next now, 17-next-existing."),
 (NN,1683,"5.63","and 1-now-existing is its entry, 17's next 1.","and 1-now-existing is its entry."),
 (TH,1086,"23, step 233","With 17 a self opens again, a next 1-now-existing:","With 17 a self has its next prior and the parities it will be observing:"),
 (TH,1381,"24","and 17-next-existing a next 1-now-existing;","and 17-next-existing "+W+";"),
]
numbering=[
 (NI,251,"3.2","as 17 is a next 1 and 9 a next prior.","as 9 is a next prior."),
 (NI,1636,"4.11","8 up alone, twice, is 17, a next 1.","8 up alone, twice, is 17."),
 (NN,469,"2.5","as 17 is next 1 and 9 next prior,","as 9 is next prior,"),
]
edge=[
 (NI,1675,"4.15","its 9, or its 17 and a next's 1."),
 (NI,1675,"4.15","a 17 and a next 1 with now and a 9 with next;"),
 (NN,212,"2.2","its 9 or its 17 and next 1,"),
 (NN,554,"3.4","17-next-existing is next 1-now-existing, and 17 to 24 is a self's span again"),
 (NN,1676,"5.63","nine to seventeen with a next 1"),
 (TH,2047,"30","a 17 and a next 1 with now and a 9 with next;"),
 (TH,3139,"40","with 16 to next 1,"),
]
after=[
 ('Exhibit_EIGHTEEN_Natural_Physics_v401mgr.md',98,"17 a next now, each self's next 1-now-existing;"),
 ('Exhibit_FIVE_Natural_Engineering_v401mgr.md',1505,"17 a next 1,"),
 ('Exhibit_THREE_Natural_Numbers_v401mgr.md',145,"17 a next 1,"),
 ('Exhibit_TWENTY-EIGHT_Equilibria_Registry_v401mgr.md',274,"17-next-existing, a next 1-now-existing, has none of them."),
 ('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v401mgr.md',740,"17-next-existing, a next 1-now-existing, seats none, one resolving."),
 ('Exhibit_TWENTY-SIX_Living_File_Registry_v401mgr.md',191,"17 a next 1 and 1's three 17's,"),
]
cache={}
def line(f,n):
    if f not in cache: cache[f]=open(R+'/'+f).read().split('\n')
    return cache[f][n-1]
for row in core+numbering: assert line(row[0],row[1]).count(row[3])==1,(row[0],row[1],row[3])
for row in edge: assert row[3] in line(row[0],row[1]),(row)
for row in after: assert row[2] in line(row[0],row[1]),(row)
short={NI:'Natural Intelligence',E1:'Exhibit ONE Natural Resolver',NN:'Exhibit TWENTY Natural Naming',TH:'Exhibit THIRTY Co-Chaining Logic Registry'}
def esc(s): return s.replace('|','\\|')
out=[]
out.append("### 3.1 17-next-existing as a next 1-now-existing: each place, its living words and its next words\n")
out.append("| The living file | Its section | The living words | The next words |\n|---|---|---|---|")
for f,n,sec,old,new in core: out.append(f"| {short[f]} | {sec} | {esc(old)} | {esc(new)} |")
out.append("\n### 3.2 17 as a next 1, an example of a numbering: each place\n")
out.append("| The living file | Its section | The living words | The next words |\n|---|---|---|---|")
for f,n,sec,old,new in numbering: out.append(f"| {short[f]} | {sec} | {esc(old)} | {esc(new)} |")
out.append("\n### 3.3 Reached, and not re-said by this part: each place of another thing\n")
out.append("| The living file | Its section | The living words |\n|---|---|---|")
for f,n,sec,old in edge: out.append(f"| {short[f]} | {sec} | {esc(old)} |")
out.append("\n### 3.4 The set after, the plan's stage 7: each other living file having it\n")
out.append("| The living file | The living words |\n|---|---|")
names={'Exhibit_EIGHTEEN_Natural_Physics_v401mgr.md':'Exhibit EIGHTEEN Natural Physics','Exhibit_FIVE_Natural_Engineering_v401mgr.md':'Exhibit FIVE Natural Engineering','Exhibit_THREE_Natural_Numbers_v401mgr.md':'Exhibit THREE Natural Numbers','Exhibit_TWENTY-EIGHT_Equilibria_Registry_v401mgr.md':'Exhibit TWENTY-EIGHT Equilibria Registry','Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v401mgr.md':'Exhibit TWENTY-TWO Resolving the Hard Problem Registry','Exhibit_TWENTY-SIX_Living_File_Registry_v401mgr.md':'Exhibit TWENTY-SIX Living File Registry, a record of a version'}
for f,n,old in after: out.append(f"| {names[f]} | {esc(old)} |")
print('\n'.join(out))
import collections
c=collections.Counter(f for f,*_ in core+numbering)
print('\n<!-- places by file: '+', '.join(f"{short[f]} {c[f]}" for f in (NI,E1,NN,TH))+f"; in all {sum(c.values())}; reached and not re-said {len(edge)} -->", file=sys.stderr)
