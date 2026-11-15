"""v402mgr: with the noun momentary re-said as moment in the living files, each sentence in quotation marks in a gathering file,
word for word living before it, is re-said the same way, so it is word for word living after it."""
import sys, re, glob, importlib.util
R = sys.argv[1]
src = open(R + '/incoming/v401mgr/instruments/build_part_three.py', encoding='utf-8').read()
ns = {}
exec(src.split("rows = []")[0].replace("R = sys.argv[1]", "R = None"), ns)   # its transform only
transform = ns['transform']
n_all = 0
for g in sorted(glob.glob(R + '/gathering-value/*.md')):
    t = open(g, encoding='utf-8').read()
    def rep(m):
        global n_all
        new, n, _ = transform(m.group(0)); n_all += n; return new
    new = re.sub(r'"[^"\n]{3,}"', rep, t)
    if new != t: open(g, 'w', encoding='utf-8').write(new)
print('quoted living words re-said in the gathering files:', n_all)
