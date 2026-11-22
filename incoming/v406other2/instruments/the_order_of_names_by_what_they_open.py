#!/usr/bin/env python3
"""The names Exhibit THIRTY waits on, in the order they open its sentences.

    python3 -I the_order_of_names_by_what_they_open.py REACH.csv [HOW_MANY]

REACH.csv is the marking of Exhibit THIRTY's sentences by the lines, made by
incoming/v405co-chain/instruments/reach.py: a sentence with the names it waits on. A sentence opens
once all the names it waits on have a line. The instrument takes, a name at a turn, the name
opening the most sentences then, and among names opening as many, the name the most sentences wait
on. It sizes an order by the instrument's matching of a name by its word alone, and decides nothing.
"""
import csv, re, sys, collections
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
how_many = int(sys.argv[2]) if len(sys.argv) > 2 else 20
wait = {}
for r in rows:
    names = {re.sub(r"\s+\d+$", "", m.strip()) for m in r["missing"].split(";") if m.strip()}
    if r["status"] == "not yet":
        wait[int(r["step"])] = names
total = len(rows)
open_now = total - len(wait)
on = collections.Counter(n for s in wait.values() for n in s)
print(f"{total} sentences; {open_now} said again or resting on the lines; {len(wait)} waiting on {len(on)} names")
print("turn | name | sentences waiting on it | opening with it | open then, of all")
given = []
for turn in range(1, how_many + 1):
    left = collections.Counter(n for s in wait.values() for n in s)
    if not left:
        break
    opens = collections.Counter()
    for s in wait.values():
        if len(s) == 1:
            opens[next(iter(s))] += 1
    name = max(left, key=lambda n: (opens[n], left[n], n))
    opened = [k for k, s in wait.items() if s == {name}]
    for k in list(wait):
        wait[k].discard(name)
        if not wait[k]:
            del wait[k]
    open_now += len(opened)
    given.append(name)
    print(f"{turn} | {name} | {on[name]} | {len(opened)} | {open_now}")
