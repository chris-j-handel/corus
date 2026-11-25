#!/bin/bash
# usage, from the set's root: incoming/v406me/instruments/wordcheck.sh PAGE...
# the one list of words, then the released words outside italics and code
cd "$(git rev-parse --show-toplevel)" || exit 1
for p in "$@"; do
  echo "== $p"
  python3 -I incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py "$p" 2>&1 | tail -6
  python3 -I - "$p" <<'PY'
import re, sys
words = [w.strip() for w in open('kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt', encoding='utf-8') if w.strip() and not w.startswith('#')]
t = open(sys.argv[1], encoding='utf-8').read()
t = re.sub(r'```.*?```', ' ', t, flags=re.S); t = re.sub(r'`[^`]*`', ' ', t); t = t.replace('**', ''); t = re.sub(r'(?<![\w*])\*(?!\s)[^*\n]+?(?<!\s)\*(?![\w*])', ' ', t)
found = []
for i, l in enumerate(t.split('\n'), 1):
    for w in words:
        if re.search(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', l, flags=re.I):
            found.append((i, w, l.strip()[:90]))
print('released words outside italics and code:', len(found))
for f in found[:30]: print('  ', f)
PY
done
