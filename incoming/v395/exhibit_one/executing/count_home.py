import json, re, collections
d=json.load(open('/home/claude/corus/kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/merged_table_of_contents.json'))
g=json.load(open('/tmp/claude-0/-home-claude/906f769f-68f8-5342-8e15-da9cc999e269/scratchpad/pass/resettling_gathered.json'))
cnt=collections.defaultdict(collections.Counter)
def short(ni):
    # strip leading number
    if ni.startswith('Opening'): return "Natural Intelligence's opening"
    if ni.startswith('Exhibit ONE ·'): return 'Exhibit ONE section'
    return re.sub(r'^\d+\.\d+ ','',ni)
for s in d['shell']:
    for p in s['placed']:
        cnt[p['file']][short(s['ni'])]+=1
for it in g['items']:
    if it['section']!='Head, the whole file' or it['kind']!='explaining': continue
    f=it['file']
    m=re.search(r"stand most, at a first merging, with Natural Intelligence's (.*?)\. Each placing",it['text'])
    named = m.group(1).split('; ') if m else []
    c=cnt[f]
    top=c.most_common(6)
    print('==',f,'total',sum(c.values()))
    print('   named:',named)
    print('   actual:',top)
