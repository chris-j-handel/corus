"""Turns each table wider than 80 characters into a narrow list, words unchanged. Usage: python3 narrow_tables.py FILE..."""
import sys

WIDE = 80

def _cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

def _narrow(block):
    rows = [_cells(l) for l in block]
    head, body = rows[0], [r for r in rows[2:]]
    out = []
    h0 = head[0]
    label0 = ''
    if len(h0) > 40:
        first = h0.split('. ')[0]
        rest = h0[len(first):].lstrip('. ').strip()
        if len(first) <= 40:
            label0 = first
            if rest:
                out.append(rest + ('' if rest.rstrip()[-1:] in '.:;' else '.') + '\n')
        else:
            out.append(h0 + ('' if h0.rstrip()[-1:] in '.:;' else '.') + '\n')
    else:
        label0 = h0
    keys, others = [], []
    letters = 'abcdefgh'
    for j, h in enumerate(head[1:]):
        if len(h) > 32:
            k = letters[len(keys)]
            keys.append('- *%s*: %s' % (k, h))
            others.append('*%s*' % k)
        else:
            others.append(('*%s*' % h if '*' not in h else h) if h else '')
    if keys:
        out.append('  \n'.join(k[2:] for k in keys) + '\n')
    for r in body:
        lab = r[0]
        lead = '**%s**' % (lab if not label0 else '%s: %s' % (label0, lab)) if lab else '**—**'
        vals = [(others[j], v) for j, v in enumerate(r[1:]) if j < len(others) and v]
        if len(vals) <= 2 and all(len(v) <= 60 for _, v in vals):
            out.append('- ' + lead + ''.join(' · %s: %s' % (h, v) if h else ' · %s' % v for h, v in vals))
        else:
            out.append('- ' + lead)
            for h, v in vals:
                out.append('  - %s: %s' % (h, v) if h else '  - %s' % v)
    return '\n'.join(out)

def _seventeen(block):
    rows = [_cells(l) for l in block][2:]
    t = ['| n | Name | Step | Is or is nots | Co |', '|---|---|---|---|---|']
    t += ['| %s | %s | %s | %s | %s |' % (r[0], r[1], r[2].replace('now-existing, a next turn', 'now, next turn').replace('-existing', ''), r[3], r[4]) for r in rows]
    t.append('\nWhat code does with each name:\n')
    t += ['- **%s** · %s' % (r[0], r[5]) for r in rows]
    return '\n'.join(t)

def _relations(block):
    rows = [_cells(l) for l in block][2:]
    out, cur = [], None
    for r in rows:
        if r[0] != cur:
            cur = r[0]
            name = next((x[2] for x in rows if x[0] == cur and x[1] == 'Name'), '')
            out.append('%s**%s** · %s' % ('\n' if out else '', cur, name.strip('*')))
        if r[1] != 'Name':
            out.append('- *%s*: %s' % (r[1], r[2]))
    return '\n'.join(out)

def _cyclings(block):
    rows = [_cells(l) for l in block][2:]
    t = ['| Four-cycling | Now | Next | Prior | Same | Between |', '|---|---|---|---|---|---|']
    for r in rows:
        nums = [c.split('-')[0] for c in r[1:5]]
        t.append('| %s | %s | %s |' % (r[0], ' | '.join(nums), r[5]))
    t.append('\nNow and prior are odd; next and same are even. Next is possibling, prior is observing.')
    return '\n'.join(t)

def narrow_tables(text):
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
            if block[0].startswith('| n | Name | Four-cycling step'):
                out.append(_seventeen(block))
            elif block[0].startswith('| n | Relation | For this name'):
                out.append(_relations(block))
            elif block[0].startswith('| Four-cycling | Now-existing, odd'):
                out.append(_cyclings(block))
            elif max(len(b) for b in block) > WIDE:
                out.append(_narrow(block))
            else:
                out.extend(block)
            i = j
            continue
        out.append(l)
        i += 1
    return '\n'.join(out)


if __name__ == '__main__':
    for f in sys.argv[1:]:
        t = open(f, encoding='utf-8').read()
        n = narrow_tables(t)
        if n != t:
            open(f, 'w', encoding='utf-8').write(n)
            print('narrowed', f)
