"""Keep Exhibit ONE one: the standalone file is the source, and its body is written inside Natural Intelligence whole.
Improve the standalone Exhibit ONE, then run this; it writes the same body into Natural Intelligence and checks they are one.
Usage: python3 cohere_one.py <folder holding both files>"""
import re, sys
d = sys.argv[1] if len(sys.argv) > 1 else '.'
ONE = f'{d}/Exhibit_ONE_Natural_Resolver_v372.md'
NI = f'{d}/Natural_Intelligence_v372.md'
HEAD = '# EXHIBIT ONE · NATURAL RESOLVER\n\n**Geodesic Discovering Logical Method and Form**\n\n'
one = open(ONE).read()
body = one.split('---\n\n&nbsp;\n\n', 1)[1].strip()
ni = open(NI).read()
pre, rest = ni.split(HEAD, 1)
old_body, post = rest.split('\n# PART FIVE', 1)
tail = old_body[len(old_body.rstrip()) - len(old_body):] if False else ''
m = re.search(r'(\s*(---|&nbsp;)\s*)+$', old_body)
sep = old_body[m.start():] if m else '\n\n'
ni = pre + HEAD + body + sep + '\n# PART FIVE' + post
open(NI, 'w').write(ni)
check = ni.split(HEAD, 1)[1].split('\n# PART FIVE')[0]
check = re.sub(r'(\s*(---|&nbsp;)\s*)+$', '', check.strip())
assert check == body, 'Exhibit ONE inside Natural Intelligence differs from the standalone'
code = body.split('```python', 1)[1].split('```', 1)[0]
ns = {}
exec(code, ns)
assert ns['_1_self_coupling']([], [('k', 1)]) == ([('k', 1)], [('k', 1, -1, 0)])
print('Exhibit ONE is one, and its code runs')
