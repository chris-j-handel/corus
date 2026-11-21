"""Turn a Claude Docs prose read (its XML) into markdown, cards marked.

A row proposed for adding is marked as a card, and a row proposed for
deleting as a card to delete; words proposed inside a line are shown as
{+added+} and {-deleted-}. Comments' markers
are left out; the people's mention chip is left out.
"""
import sys
import xml.etree.ElementTree as ET

WHOLE_CARD = [False]


def runs(el):
    """Inline text of a paragraph, with bold, italic and card marks."""
    out = []
    for ch in el:
        tag = ch.tag
        if tag == 'text':
            out.append(text_run(ch))
        elif tag == 'date':
            out.append(ch.get('value', ''))
        elif tag in ('mention', 'comment'):
            continue
    s = ''.join(out)
    return s


def text_run(t):
    s = t.text or ''
    for sub in t:
        s += inner(sub)
        s += sub.tail or ''
    return s


def inner(el):
    s = el.text or ''
    for sub in el:
        s += inner(sub)
        s += sub.tail or ''
    tag = el.tag
    if not s:
        return s
    if tag == 'bold':
        return '**' + s + '**'
    if tag == 'italic':
        return '*' + s + '*'
    if tag == 'ins':
        return s if WHOLE_CARD[0] else '{+' + s + '+}'
    if tag == 'del':
        return s if WHOLE_CARD[0] else '{-' + s + '-}'
    return s


def tidy(s):
    s = s.replace('****', '')
    s = s.replace('** **', ' ')
    return s


def cell_text(cell):
    parts = [tidy(runs(p)) for p in cell if p.tag == 'paragraph']
    return ' '.join(x for x in parts if x).replace('|', '\\|')


def table(el, lines):
    rows = [r for r in el if r.tag == 'row']
    first = True
    for r in rows:
        cells = [c for c in r if c.tag == 'cell']
        sug = r.get('suggest')
        WHOLE_CARD[0] = sug in ('ins', 'del')
        texts = [cell_text(c) for c in cells]
        WHOLE_CARD[0] = False
        if sug == 'ins' and texts:
            texts[0] = texts[0] + ' *(card)*'
        elif sug == 'del' and texts:
            texts[0] = texts[0] + ' *(card: to delete)*'
        if any(c.get('align') == 'right' for c in cells) and texts and not texts[0].startswith('**'):
            texts[0] = '**' + texts[0] + '**' if texts[0] else texts[0]
        lines.append('| ' + ' | '.join(texts) + ' |')
        if first:
            lines.append('| ' + ' | '.join('---' for _ in texts) + ' |')
            first = False
    lines.append('')


def lst(el, lines, depth=0):
    ordered = el.get('kind') == 'ordered'
    n = 0
    for item in el:
        if item.tag != 'listItem':
            continue
        n += 1
        mark = f'{n}.' if ordered else '-'
        pad = '   ' * depth
        first = True
        for ch in item:
            if ch.tag == 'paragraph':
                txt = tidy(runs(ch))
                if first:
                    lines.append(f'{pad}{mark} {txt}')
                    first = False
                else:
                    lines.append(f'{pad}   {txt}')
            elif ch.tag == 'list':
                lst(ch, lines, depth + 1)
    if depth == 0:
        lines.append('')


def main(path):
    root = ET.fromstring(open(path).read())
    lines = []
    for el in root:
        tag = el.tag
        if tag == 'paragraph':
            txt = tidy(runs(el))
            h = el.get('heading')
            if h:
                lines.append('#' * int(h) + ' ' + txt)
                lines.append('')
            elif txt.strip():
                lines.append(txt)
                lines.append('')
        elif tag == 'list':
            lst(el, lines)
        elif tag == 'table':
            table(el, lines)
    sys.stdout.write('\n'.join(lines).rstrip() + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
