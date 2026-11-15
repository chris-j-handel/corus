"""v402mgr: Exhibit ONE Natural Resolver's gathered droplets, each form read by the code as it is.
Executes the code block of the living file given as its first argument. Changes nothing."""
import sys, re, itertools
src = open(sys.argv[1], encoding='utf-8').read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
ns = {}; exec(code, ns)
one, nine, seventeen = ns['_1_now_existing'], ns['_9_next_co_discovering'], ns['_17_next_existing']
S = {1: '+', -1: '−', 0: '0', None: '·'}
K = 'k'
def cell(prior, arriving):
    three = [] if prior is None else [(K, prior)]
    ten, eight = one(three, [(K, a) for a in arriving])
    return dict(ten).get(K), dict(eight).get(K)
ok = True
def say(name, cond, extra=''):
    global ok; ok &= bool(cond); print(('  is    ' if cond else '  IS-NOT') + ' · ' + name + (' · ' + extra if extra else ''))

print('1 One cell: a self having a prior p')
for p in (1, -1):
    say(f'p {S[p]}: same arriving, its co-possibling 0 and its next prior p', cell(p, [p]) == (0, p))
    for arr, nm in (([-p], 'the other one'), ([p, -p], 'both'), ([], 'none'), ([0], 'a 0')):
        say(f'p {S[p]}: {nm} arriving, its co-possibling −p and its next prior −p', cell(p, arr) == (-p, -p))
print('2 The code\'s state of no prior')
say('none arriving: no co-possibling and no next prior', cell(None, []) == (None, None))
say('+ arriving: + its co-possibling and its first prior', cell(None, [1]) == (1, 1))
say('− arriving: − its co-possibling and its first prior', cell(None, [-1]) == (-1, -1))
say('+ and − arriving, each order: a 0 its co-possibling and no next prior', cell(None, [1, -1]) == (0, None) and cell(None, [-1, 1]) == (0, None))
print('3 Parities to one sharing: the twelve rows of the living table, 14-next-possibling')
def fourteen(arr):
    # 14 is internal; read it by a self with no prior: its co-possibling is 14 as it is
    return cell(None, arr)[0]
rows = [([], None), ([0], None), ([1], 1), ([-1], -1), ([1, 1], 1), ([-1, -1], -1), ([1, -1], 0), ([-1, 1], 0), ([1, 1, -1], 0), ([-1, -1, 1], 0), ([1, -1, 1], 0), ([0, 1], 1)]
say('each of twelve rows as the living table has it', all(fourteen(a) == r for a, r in rows))
say('each order of each row\'s arrivings: one same return', all(len({fourteen(list(p)) for p in itertools.permutations(a)}) == 1 for a, _ in rows))
print('4 One self, moment by moment, its prior − first, eight moments')
def run(prior, seq):
    tens, priors = [], []
    for arr in seq:
        t, prior = cell(prior, arr); tens.append(t); priors.append(prior)
    return ''.join(S[t] for t in tens), ''.join(S[p] for p in priors)
say('none arriving each moment: + − + − + − + −, each', run(-1, [[]] * 8) == ('+−+−+−+−',) * 2)
say('− each moment: 0 each, its prior − each', run(-1, [[-1]] * 8) == ('0' * 8, '−' * 8))
say('+ each moment: + once and 0 after, its prior + each', run(-1, [[1]] * 8) == ('+' + '0' * 7, '+' * 8))
say('+ and − together each moment: + − + − + − + −, each', run(-1, [[1, -1]] * 8) == ('+−+−+−+−',) * 2)
print('5 17-next-existing: selves along, last to first, by 9-next-co-discovering')
def spiral(n, priors, moments):
    five = {((i), 9): (i % n) + 1 for i in range(1, n + 1)}
    sixteen = {i: (([] if priors[i - 1] is None else [(K, priors[i - 1])]), []) for i in range(1, n + 1)}
    tens, pr = [], []
    for m in range(moments):
        nxt = seventeen(sixteen, five)
        # each self's co-possibling of this moment is what its next self has as its possibling
        tens.append([dict(nxt[(i % n) + 1][1]).get(K) for i in range(1, n + 1)])
        pr.append([dict(nxt[i][0]).get(K) for i in range(1, n + 1)])
        sixteen = nxt
    return tens, pr
living_a = {1: '+0−0+0−0+0−0', 2: '+−+−+−+−+−+−', 3: '+0−+−+−0+−+−', 4: '+−+−+−+−+−+−', 5: '+0−+−+−+−+−0', 6: '+−+−+−+−+−+−', 7: '+0−+−+−+−+−+', 8: '+−+−+−+−+−+−', 9: '+0−+−+−+−+−+', 10: '+−+−+−+−+−+−', 11: '+0−+−+−+−+−+'}
def self1(n, priors): return ''.join(S[t[0]] for t in spiral(n, priors, 12)[0])
alt = lambda n: [-1 * (-1) ** i for i in range(n)]   # self 1 −, each next the other one
say('A spiral of selves, each self having a prior, self 1 −, each next the other one: each of eleven living rows', all(self1(n, alt(n)) == living_a[n] for n in living_a))
only = lambda n: [-1] + [None] * (n - 1)
got = {n: self1(n, only(n)) for n in living_a}
say('the same rows by self 1 only having a prior: same-as by each even number of selves and by one, and by no other odd number', [n for n in living_a if got[n] != living_a[n]] == [3, 5, 7, 9, 11])
print('6 A spiral opening, self 1 having prior − and each other self no prior: each self\'s prior, eight moments')
living3 = ['+··', '−+·', '+−+', '++−', '−−+', '+−−', '−++', '+−+']
living5 = ['+····', '−+···', '+−+··', '−+−+·', '+−+−+', '++−+−', '−−+−+', '+−−+−']
p3 = [''.join(S[x] for x in r) for r in spiral(3, only(3), 8)[1]]
p5 = [''.join(S[x] for x in r) for r in spiral(5, only(5), 8)[1]]
say('a spiral of 3: each of eight living rows', p3 == living3, ' '.join(p3))
say('a spiral of 5: each of eight living rows', p5 == living5, ' '.join(p5))
print('7 Two selves, each its other\'s, both ways')
def two(pa, pb, moments=8):
    five = {(1, 10): 2, (2, 10): 1}
    sixteen = {1: ([(K, pa)], []), 2: ([(K, pb)], [])}
    out = []
    for m in range(moments):
        nxt = seventeen(sixteen, five)
        out.append((dict(nxt[2][1]).get(K), dict(nxt[1][1]).get(K)))
        sixteen = nxt
    return ''.join(S[a] for a, b in out), ''.join(S[b] for a, b in out)
say('priors same-as, +: each one\'s co-possibling − 0 + 0, the two the same each moment', two(1, 1) == ('−0+0−0+0',) * 2, ' / '.join(two(1, 1)))
a, b = two(1, -1)
say('priors other-than: each the other one each moment, and no 0', '0' not in a + b and a == '−+−+−+−+' and b == '+−+−+−+−', a + ' / ' + b)
print('8 6, 10 and 9: one same list; 1-now-existing once by each self')
say('the code has one line of 1-now-existing, inside 17-next-existing', code.count('_1_now_existing(') == 2 and code.count('def _1_now_existing(') == 1)
say('no line executes 17-next-existing', code.count('_17_next_existing(') == 1)
say('6-now-co-possibling is 10-next-co-possibling, one line', '_6_now_co_possibling = _10_next_co_possibling' in code)
print('9 Four bi-foldings: 17 less and a move of 8, the one and the other')
def cyc(start):
    c, x, podal = [start], start, False
    for _ in range(3):
        x = (x + 8 if x <= 8 else x - 8) if podal else 17 - x   # first 8 up or down, then a podal
        podal = not podal; c.append(x)
    return c
# living: 1-9-8-16, 2-15-7-10, 3-11-6-14, 4-13-5-12
def by(c):  # each step is a move of 8 or a podal, and no move of 4
    steps = [(c[i], c[(i + 1) % 4]) for i in range(4)]
    return all(abs(a - b) == 8 or a + b == 17 for a, b in steps), any(abs(a - b) == 4 for a, b in steps)
for c in ([1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12]):
    whole, four = by(c)
    say('-'.join(map(str, c)) + ': each step a move of 8 or 17 less, and no move of 4', whole and not four)
print('ALL IS' if ok else 'A THING IS-NOT')
if '--rows' in sys.argv:
    for n in living_a:
        print(n, 'living', living_a[n], '| each a prior', self1(n, alt(n)), '| self 1 only', self1(n, only(n)))
