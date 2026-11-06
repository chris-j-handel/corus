import itertools, importlib.util, collections
spec=importlib.util.spec_from_file_location('r','resolver.py'); r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
sg=lambda v: '+' if v>0 else '-' if v<0 else '0'
rows=collections.Counter()
for prior in (1,-1,None):
    for n in range(0,4):
        for rec in itertools.product((1,-1,0),repeat=n):
            three=[('s',prior)] if prior is not None else []
            two=[('s',p) for p in rec]
            ten,eleven=r._1_now_existing(three,two)
            # what surfaced at 14 (recompute by the same lines)
            surf=None
            for p in rec:
                if p!=0:
                    if surf is None: surf=1 if p>0 else -1
                    elif (surf>0)!=(p>0): surf=0
            shared=dict(ten).get('s')
            nxt=dict(eleven).get('s')
            if prior is None: inn='no prior: '+('empty' if surf is None else 'surfaced 0' if surf==0 else 'surfaced ±')
            else: inn='empty' if surf is None else 'surfaced 0 (parting)' if surf==0 else ('same as prior' if surf==prior else 'inverse of prior')
            out='nothing' if shared is None else ('shares 0' if shared==0 else 'shares ±')
            along='no prior' if prior is None and nxt is None else ('next prior '+('formed' if prior is None else 'same' if nxt==prior else 'inverted'))
            rows[(inn,out,along)]+=1
for k,v in sorted(rows.items()): print(f"{v:3d}  across in: {k[0]:24s} | across out: {k[1]:9s} | along: {k[2]}")
