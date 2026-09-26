"""Keep Exhibit ONE one: the standalone file is the source, and its body is written inside Natural Intelligence whole.
Improve the standalone Exhibit ONE, then run this; it writes the same body into Natural Intelligence and checks they are one
and the code runs. The newest version of each file in the folder is taken.
Usage: python3 cohere_one.py <folder holding both files>      (the repository root, as a rule)"""
import re, sys, os, glob

def newest(folder, stem):
    files = glob.glob(os.path.join(folder, stem + '_v*.md'))
    if not files: sys.exit('no ' + stem + ' at ' + folder)
    return max(files, key=lambda f: int(re.search(r'_v(\d+)', f).group(1)))

d = sys.argv[1] if len(sys.argv) > 1 else '.'
resolver_path, intelligence_path = newest(d, 'Exhibit_ONE_Natural_Resolver'), newest(d, 'Natural_Intelligence')
HEAD = '# EXHIBIT ONE · NATURAL RESOLVER\n\n**Geodesic Discovering Logical Method and Form**\n\n'
one = open(resolver_path, encoding='utf-8').read()
body = one.split('\n---\n', 1)[1].strip()
ni = open(intelligence_path, encoding='utf-8').read()
pre, rest = ni.split(HEAD, 1)
old_body, post = rest.split('\n# PART FIVE', 1)
m = re.search(r'(\s*(---|&nbsp;)\s*)+$', old_body)
sep = old_body[m.start():] if m else '\n\n'
new = pre + HEAD + body + sep + '\n# PART FIVE' + post
if new != ni:
    open(intelligence_path, 'w', encoding='utf-8').write(new); print('written inside', os.path.basename(intelligence_path))
check = re.sub(r'(\s*(---|&nbsp;)\s*)+$', '', new.split(HEAD, 1)[1].split('\n# PART FIVE')[0].strip())
assert check == body, 'Exhibit ONE inside Natural Intelligence differs from the standalone'
code = body.split('```python', 1)[1].split('```', 1)[0]
ns = {}
exec(code, ns)
assert next(v for k, v in ns.items() if k.startswith('_1_') and callable(v))([], [('k', 1)]) == ([('k', 1)], [('k', 1)])
print('Exhibit ONE is one, and its code runs:', os.path.basename(resolver_path), 'inside', os.path.basename(intelligence_path))
