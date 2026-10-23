"""narrow_keys.py FILE...
Each table wider than 80 characters, outside code fences, becomes a narrow list with its words unchanged and none
repeated: one key line names its columns once (its first column bold, each other column a letter), and each row
is one entry with its cells after their letters; an empty cell is left unsaid. Tables 80 wide or narrower stay."""
import sys

WIDE = 80
LETTERS = 'abcdefghjkmnpqrstuvwxyz'


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def narrow(block):
    head = cells(block[0])
    body = [cells(l) for l in block[2:]]
    keys = ['*%s*' % LETTERS[j] for j in range(len(head) - 1)]
    lead = 'Each entry: ' + ' · '.join(([(head[0] if '*' in head[0] else '**%s**' % head[0]) if head[0] else '']
                                        + ['%s %s' % (k, h) for k, h in zip(keys, head[1:])])).lstrip(' ·')
    out = [lead + '\n']
    for r in body:
        first = r[0] if r else ''
        lab = first if '*' in first else ('**%s**' % first if first else '**—**')
        vals = [(keys[j], v) for j, v in enumerate(r[1:]) if j < len(keys) and v]
        if len(vals) <= 2 and all(len(v) <= 60 for _, v in vals):
            out.append('- ' + lab + ''.join(' · %s %s' % kv for kv in vals))
        else:
            out.append('- ' + lab)
            out += ['  - %s %s' % kv for kv in vals]
    return '\n'.join(out)


def narrow_keys(text):
    lines = text.split('\n')
    out, i, code = [], 0, False
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            code = not code
        if not code and l.startswith('|') and i + 1 < len(lines) and lines[i + 1].startswith('|---'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            block = lines[i:j]
            out.append(narrow(block) if max(len(b) for b in block) > WIDE else '\n'.join(block))
            i = j
            continue
        out.append(l)
        i += 1
    return '\n'.join(out)


if __name__ == '__main__':
    for f in sys.argv[1:]:
        t = open(f, encoding='utf-8').read()
        n = narrow_keys(t)
        if n != t:
            open(f, 'w', encoding='utf-8').write(n)
            print('narrowed', f)
