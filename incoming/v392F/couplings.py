import re,json,os,sys,collections
root=sys.argv[1]
files=json.load(open(os.path.join(root,'files.json')))
def title(fn):
    m=re.match(r'Exhibit_([A-Z-]+)_(.*)_v\d+\.md',fn)
    return (m.group(1), m.group(2).replace('_',' ')) if m else (None, fn.replace('_v391.md','').replace('_',' '))
names={fn:title(fn) for fn in files}
texts={fn:open(os.path.join(root,fn),encoding='utf-8').read() for fn in files}
# patterns: the file's title, or 'Exhibit N'
pats={}
for fn,(num,t) in names.items():
    alts=[re.escape(t)]
    if num: alts.append(r'Exhibit '+num+r'\b')
    if t=='Natural Resolver': alts.append(r'\bresolver\b')
    pats[fn]=re.compile('|'.join(alts))
M={}
for a in files:
    body=texts[a]
    row={}
    for b in files:
        if a==b: continue
        n=len(pats[b].findall(body))
        if b=='Natural_Intelligence_v391.md':
            n-=len(re.findall(r'Natural Intelligence Corus',body))
        if n>0: row[b]=n
    M[a]=row
short=lambda fn:(names[fn][0] or '')+'·'+names[fn][1][:22]
print("== each file: the files it names most (title or Exhibit number), top 6 ==")
for a in files:
    top=sorted(M[a].items(),key=lambda x:-x[1])[:6]
    print(f"{short(a):30s} " + ", ".join(f"{short(b)}={n}" for b,n in top))
print()
print("== named by most other files (in-degree: number of files naming it, total mentions) ==")
indeg=collections.Counter(); tot=collections.Counter()
for a in files:
    for b,n in M[a].items(): indeg[b]+=1; tot[b]+=n
for b,c in sorted(indeg.items(),key=lambda x:(-x[1],-tot[x[0]])): print(f"{short(b):30s} files={c:2d} mentions={tot[b]}")
json.dump({a:{b:n for b,n in r.items()} for a,r in M.items()},open(os.path.join(root,'incoming/v392F/readers/couplings_by_naming.json'),'w'),indent=0)
