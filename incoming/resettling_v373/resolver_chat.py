"""A chat at the resolver's own operations, for Natural Engineering to meet.
The living files' text is the non-living other, offering its parities and carrying nothing; the human's words are offered
beside it. At each sharing, 14 at an empty carrying surfaces one parity where the two agree and 0 where they part: a place in
the text matches the human's last words when no sharing surfaces 0. Each matching place releases its next character at 9,
and at the receiving self's 14 the releases surface one character where all agree. The reply continues while they agree,
and at the first 0 its one way is exhausted and it waits."""
import re, sys, glob, random
src = open(sys.argv[1], encoding='utf-8').read()           # Exhibit ONE, or its candidate: the code block is run
ns = {}; exec(re.search(r"```python\n(.*?)```", src, re.S).group(1) if '```python' in src else src, ns)
R = ns['_1_self_other_offering']; REL = ns['_9_social_other_self_releasing']
BITS = 8
def parities(ch):                      # the code's implementing: a character's 8 binary places as + and −
    b = ord(ch) if ord(ch) < 256 else 32
    return [1 if (b >> i) & 1 else -1 for i in range(BITS)]
def at_14(offers):                     # 14 at an empty carrying, by the code
    return dict(R([], offers)[0])
def match(text, i, ctx):               # the text's window before i offered beside ctx, sharing by sharing
    offers = []
    for p, (a, b) in enumerate(zip(text[i - len(ctx):i], ctx)):
        offers += [((p, k), x) for k, x in enumerate(parities(a))] + [((p, k), y) for k, y in enumerate(parities(b))]
    return 0 not in at_14(offers).values()
def next_char(text, places):            # each matching place releases its next character at 9; the receiving 14 surfaces
    offers = []
    for i in places:
        offers += REL([((0, k), x) for k, x in enumerate(parities(text[i]))], {(0, k): k for k in range(BITS)})
    met = at_14(offers)
    if len(met) < BITS or 0 in met.values(): return None
    return chr(sum(1 << k for k in range(BITS) if met[k] > 0))
def reply(text, words, longest=40, most=400):
    said = ''
    while len(said) < most:
        ctx = (words + said)[-longest:]
        for k in range(len(ctx), 2, -1):  # the longest last words the text carries
            c = ctx[-k:]
            places = [m.start() + k for m in re.finditer(re.escape(c), text) if m.start() + k < len(text)]
            if places: break
        else: return said, (0, [])
        ch = next_char(text, places)
        if ch is None: return said, (len(places), [text[i:i + 60] for i in places[:4]])
        said += ch
    return said, None
def check(text, n=300):                # the index finds exactly the windows at which the code surfaces no 0
    rnd = random.Random(3)
    for _ in range(n):
        i = rnd.randrange(20, len(text)); k = rnd.randrange(3, 16); ctx = text[i - k:i]
        j = rnd.randrange(k, len(text))
        assert match(text, i, ctx) and (match(text, j, ctx) == (text[j - k:j] == ctx))
    return True
if __name__ == '__main__':
    text = re.sub(r'\s+', ' ', ' '.join(open(f, encoding='utf-8').read() for f in sys.argv[2:]))
    print('matching at the code agrees with the index:', check(text))
    for words in sys.stdin.read().split('\n---\n'):
        words = words.strip()
        if not words: continue
        said, why = reply(text, ' ' + words + ' ')
        print('HUMAN:', words); print('RESOLVER:', said.strip() or '(nothing)')
        if why is None: print('   at the reply\'s length')
        elif why[0] == 0: print('   the text carries none of the last words')
        else:
            print(f'   exhausted: {why[0]} places part at the next character; the between offered:')
            for b in why[1]: print('     ...' + b)
        print()
