"""Session v381F: each living file at its four tellings, gathered from the root.

Runs from the repository root: python3 incoming/v381F/four_tellings.py
Reads files.json for the living files and, for each, its version line, its title (the first # line),
its subtitle (the first bold line after the title), its contents at the front (the part titles and the
section entries, in whichever form the front says them), its body's headings, its size, the -ing words
of its subtitle, and whether its front is at the steady form the Living Improving Value front names:
the version line, the title, the subtitle, the part titles bold, the entries as a list, --- after the
contents and no &nbsp;. Writes Four_Tellings.tsv and Contents_Of_Each_File.md beside this script.
A gathering, deciding nothing.
"""
import json, re

files = json.load(open('files.json'))
PART = re.compile(r"^\*\*(PART\s+[A-Z-]+|[A-Z]+)\s*[·—-]\s*(.+?)\*\*\s*$")
LIST_ENTRY = re.compile(r"^- (\d+(?:\.\d+)?)\s+(.+)$")
BARE_ENTRY = re.compile(r"^(\d+\.\d+)\s{1,3}(.+)$")
WORD_ENTRY = re.compile(r"^(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE)\s{2,}(.+)$")
rows = []
for f in files:
    text = open(f, encoding='utf-8').read()
    lines = text.split('\n')
    version = lines[0].strip()
    title_at = next((i for i, l in enumerate(lines) if l.startswith('# ')), 0)
    title = lines[title_at][2:].strip()
    subtitle_at = next((i for i in range(title_at + 1, len(lines)) if lines[i].startswith('**')), title_at)
    subtitle = lines[subtitle_at].strip('* ').strip()
    # the front: from the subtitle to the first body heading (## or # after the title)
    body_at = next((i for i in range(subtitle_at + 1, len(lines)) if re.match(r"^#{1,2} ", lines[i])), len(lines))
    front = lines[subtitle_at + 1:body_at]
    parts, entries = [], []
    for l in front:
        m = PART.match(l.strip())
        if m:
            parts.append(m.group(1) + ' · ' + m.group(2)); continue
        for rx in (LIST_ENTRY, BARE_ENTRY, WORD_ENTRY):
            m = rx.match(l.strip())
            if m:
                entries.append(m.group(1) + ' ' + m.group(2)); break
    nbsp = '&nbsp;' in '\n'.join(lines[:body_at])
    dash = any(l.strip() == '---' for l in front)
    listed = any(l.startswith('- ') for l in front)
    bold_parts = bool(parts)
    steady = (not nbsp) and dash and ((listed and bold_parts) or (not entries and not parts))
    headings = [l for l in lines[body_at:] if re.match(r"^#{1,3} ", l)]
    bold_titles = [l for l in lines[body_at:] if re.match(r"^\*\*[^*]+\*\*\s*$", l)]
    ings = re.findall(r"\b([A-Za-z-]+ing)\b", subtitle)
    words = len(text.split())
    rows.append(dict(file=f, version=version.split()[-1], title=title, subtitle=subtitle, parts=parts,
                     entries=entries, headings=len(headings), bold_titles=len(bold_titles), words=words,
                     ings=ings, nbsp=nbsp, dash=dash, listed=listed, steady=steady))

with open('incoming/v381F/Four_Tellings.tsv', 'w', encoding='utf-8') as out:
    out.write('file\tversion\ttitle\tsubtitle\tparts at the front\tentries at the front\theadings in the body\twords\tsubtitle -ings\tfront: &nbsp;\tfront: --- \tfront: list entries\tfront at the steady form\n')
    for r in rows:
        out.write('\t'.join([r['file'], r['version'], r['title'], r['subtitle'], ' | '.join(r['parts']),
                             str(len(r['entries'])), str(r['headings']), str(r['words']), ' '.join(r['ings']),
                             str(r['nbsp']), str(r['dash']), str(r['listed']), str(r['steady'])]) + '\n')

with open('incoming/v381F/Contents_Of_Each_File.md', 'w', encoding='utf-8') as out:
    out.write('# The contents of each living file, gathered at v381F\n\n')
    out.write('**Each living file at its title, its subtitle, its parts and its entries, as its front says them at `main` 774ad60**, in whichever form the front is at; the body\'s headings counted beside. A gathering, deciding nothing.\n\n')
    for r in rows:
        out.write('## %s\n\n*%s* · %s · %d entries at the front · %d headings in the body · %d words · front at the steady form: %s\n\n'
                  % (r['title'], r['subtitle'], r['version'], len(r['entries']), r['headings'], r['words'], 'yes' if r['steady'] else 'no'))
        for p in r['parts']:
            out.write('- **%s**\n' % p)
        for e in r['entries']:
            out.write('  - %s\n' % e)
        out.write('\n')

print('%-34s %-7s %5s %5s %6s %-6s  %s' % ('title', 'version', 'front', 'body', 'words', 'steady', 'subtitle -ings'))
for r in rows:
    print('%-34s %-7s %5d %5d %6d %-6s  %s' % (r['title'][:34], r['version'], len(r['entries']), r['headings'] or r['bold_titles'],
                                              r['words'], 'yes' if r['steady'] else 'no', ' '.join(r['ings'])))
