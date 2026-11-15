"""build_part_four · v401mgr · 14 Nov
A name's three in its name: each of the seventeen names, at each place in each living file, with its three after its number.
The threes are Exhibit TWENTY Natural Naming 3.3's own, read from its table and no list here.
Usage: python3 -I build_part_four.py <root>                         each place counted, a table
       python3 -I build_part_four.py <root> rehearse <copy root> [code]   the next words written into a copy; with 'code', the code's names too
No file of <root> is written.
"""
import sys, re, glob, os
root = sys.argv[1]
nn = [f for f in glob.glob(os.path.join(root, 'Exhibit_TWENTY_Natural_Naming_*.md'))][0]
three, name = {}, {}
for line in open(nn).read().split('\n'):
    m = re.match(r"\| (\d+) \| \*\*(\d+)-([a-z-]+)\*\* \| [^|]+ \| [^|]+ \| ((?:co|bi|tri)-(?:co|bi|tri)-(?:co|bi|tri)) \|", line)
    if m: three[int(m.group(1))] = m.group(4); name[int(m.group(1))] = m.group(3)
assert sorted(three) == list(range(1, 18)), sorted(three)
sent = re.compile(r"(?<![\w-])(" + "|".join(f"{n}-{name[n]}" for n in sorted(name, reverse=True)) + r")(?![\w-])")
code = re.compile(r"(?<![A-Za-z0-9])_(" + "|".join(f"{n}_{name[n].replace('-', '_')}" for n in sorted(name, reverse=True)) + r")(?![A-Za-z0-9_])")
def s_new(m):
    n, rest = m.group(1).split('-', 1); return f"{n}-{three[int(n)]}-{rest}"
def c_new(m):
    n, rest = m.group(1).split('_', 1); return f"_{n}_{three[int(n)].replace('-', '_')}_{rest}"
files = sorted(glob.glob(os.path.join(root, '*.md')))
rows, ts, tc = [], 0, 0
for f in files:
    t = open(f).read(); a = len(sent.findall(t)); b = len(code.findall(t))
    if a or b: rows.append((os.path.basename(f), a, b)); ts += a; tc += b
if len(sys.argv) < 3:
    print("| Living file | A name in a sentence | A name in the code |"); print("|---|---|---|")
    for f, a, b in sorted(rows, key=lambda r: -r[1]): print(f"| {f.rsplit('_v', 1)[0].replace('_', ' ')} | {a} | {b} |")
    print(f"| **Each living file having one, {len(rows)}** | **{ts}** | **{tc}** |")
    print(); print("| Name | With its three in it |"); print("|---|---|")
    for n in range(1, 18): print(f"| {n}-{name[n]} | {n}-{three[n]}-{name[n]} |")
else:
    copy = sys.argv[3]; with_code = len(sys.argv) > 4
    assert os.path.realpath(copy) != os.path.realpath(root)
    for f in sorted(glob.glob(os.path.join(copy, '*.md'))) + sorted(glob.glob(os.path.join(copy, 'gathering-value', '*.md'))):
        t = open(f).read(); u = sent.sub(s_new, t)
        if with_code: u = code.sub(c_new, u)
        if u != t: open(f, 'w').write(u)
    left = sum(len(sent.findall(open(f).read())) for f in glob.glob(os.path.join(copy, '*.md')))
    print("written into the copy; of the names with no three, left in its living files:", left)
