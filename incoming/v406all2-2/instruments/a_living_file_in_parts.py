"""A living file in parts, for a tab of a working document.

Usage: python3 -I a_living_file_in_parts.py <living file> <a line> <b line>

It prints lines a to b of the living file as one string, as a working
document's markdown goes in. A list under a list goes from two spaces of
indent to four; all other words and marks go as they are.
"""
import json
import re
import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1], encoding='utf-8')]
a, b = int(sys.argv[2]), int(sys.argv[3])
part, fenced = [], False
for line in lines[a - 1:b]:
    if line.startswith('```'):
        fenced = not fenced
    if not fenced and re.match(r'^  - ', line):
        line = '  ' + line
    part.append(line)
print(json.dumps('\n'.join(part).strip('\n'), ensure_ascii=False))
