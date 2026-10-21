"""registry_entry.py: one living file's entry with the Living File Registry's titles (section 1.1), as a table row
or as a narrow list entry, its keys named once:
  Each entry: **File** · *a* Subtitle · *b* At the repository · *c* Living · *d* Out at · *e* Next
set_entry(text, label, version, cell, prepend, next_) gives the text with that file's entry set: *b* to version;
*c* to cell, before its earlier cells when prepend, alone otherwise; *e* to next_ when given."""


def set_entry(s, label, version, cell, prepend=True, next_=None):
    L = s.split('\n')
    rows = [k for k, r in enumerate(L) if r.startswith('| ' + label + ' |')]
    if rows:
        k = rows[0]
        c = L[k].split(' | ')
        c[2] = version
        c[3] = (cell + '; ' + c[3]) if prepend else cell
        if next_ is not None:
            c[-1] = next_ + ' |'
        L[k] = ' | '.join(c)
        return '\n'.join(L)
    heads = [k for k, r in enumerate(L) if r == '- ' + label]
    assert heads, label
    k = heads[0] + 1
    keys = {}
    while k < len(L) and L[k].startswith('  - *'):
        keys[L[k][5]] = k
        k += 1
    end = k
    assert 'b' in keys and 'c' in keys, label
    L[keys['b']] = '  - *b* ' + version
    old = L[keys['c']][len('  - *c* '):]
    L[keys['c']] = '  - *c* ' + ((cell + '; ' + old) if prepend else cell)
    if next_ is not None:
        if 'e' in keys:
            L[keys['e']] = '  - *e* ' + next_
        else:
            L.insert(end, '  - *e* ' + next_)
    return '\n'.join(L)
