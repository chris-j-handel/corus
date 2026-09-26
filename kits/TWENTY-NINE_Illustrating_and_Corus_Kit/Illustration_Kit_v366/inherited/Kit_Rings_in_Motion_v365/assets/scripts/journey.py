"""The podaling journey through the nine-spot diamond, and each equilibria cluster's fixed rule at it.

Writes:
  ../data/journey.json            both journeys, the eight cluster rules, all 256 fixed conditions
  ../data/journey_blockage.md     the same, as tables
  ../podaling_journey.html        the moving form, self-contained (open in any browser)
  ../images/podaling_journey_still.png

The resolving step is Equilibria Definitions v363 section 3.1's aligned comparison,
F(P, Q) = (-Q, P), each sign + or -, from the existing prior (+, -).
Arrivals 0 to 9 are two and one half momentaries of four: prior 0-3, now 4-7, next 8-9.
Odd origin runs co-bi-co-bi (odd arrivals along, even across); even origin runs bi-co-bi-co.
Only the sign pair and the direction at each arrival are used; nothing inside a resolver is touched.
"""
import os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data'); IMG = os.path.join(HERE, '..', 'images'); ASSETS = os.path.join(HERE, '..')

# ---------- the diamond: 0 and 9 at the centre, one station at its two turns ----------
RING = [(0, -1), (.5, -.5), (1, 0), (.5, .5), (0, 1), (-.5, .5), (-1, 0), (-.5, -.5)]  # B, LR, R, UR, T, UL, L, LL
def spot(n):
    if n in (0, 9): return (0.0, 0.0)
    return RING[(3 * (n - 1)) % 8]          # a step of three round eight: the eight-pointed criss-cross
SPOTS = {n: spot(n) for n in range(10)}

# ---------- the resolving ----------
def F(s): P, Q = s; return (-Q, P)
S0 = (1, -1)
SIGNS = [S0]
for _ in range(9): SIGNS.append(F(SIGNS[-1]))
def direction(origin, n):                  # origin 'odd': odd n along (co); origin 'even': odd n across (bi)
    odd = n % 2 == 1
    return ('co' if odd else 'bi') if origin == 'odd' else ('bi' if odd else 'co')
JOURNEYS = {o: [(direction(o, n), SIGNS[n]) for n in range(10)] for o in ('odd', 'even')}
rel = lambda s: 'agree' if s[0] == s[1] else 'oppose'
sg = lambda s: ''.join('+' if x > 0 else '-' for x in s)

# ---------- the eight clusters of Exhibit TWENTY-EIGHT, each as a fixed rule at the arrival ----------
def r1(j, n): d, s = j[n]; return (d, rel(s)) in {('co', 'agree'), ('bi', 'oppose')}
def r2(j, n): d, s = j[n]; return (d, rel(s)) in {('co', 'oppose'), ('bi', 'agree')}
def r3(j, n): return j[n][1] == (-j[n-1][1][0], -j[n-1][1][1])
def r4(j, n):
    for m in range(n):
        if SPOTS[m] == SPOTS[n]: return j[m] == j[n]
    return True
def r5(j, n): return j[n][1] == j[n-1][1]
def r6(j, n): return rel(j[n][1]) == rel(j[n-1][1])
def r7(j, n): return j[n][1][0] == j[n-1][1][0]
def r8(j, n): return max(j[n][1]) > 0
CLUSTERS = [
 (1, 'State–flow–state equilibria', 'a state along, a flow across: along carries agreeing signs, across carries opposing signs', r1),
 (2, 'Flow–state–flow equilibria', 'a flow along, a state across: along carries opposing signs, across carries agreeing signs', r2),
 (3, 'All-changing equilibria with an unchanged distinction', 'both signs change at every arrival while the distinction between them is held', r3),
 (4, 'Returning equilibria sufficient for the whole continuing', 'a station met again carries what it carried before: the return is the whole', r4),
 (5, 'Same-form equilibria identified with immediate-next', 'the next arrival carries the same sign pair as now', r5),
 (6, 'Equilibria as a relation conserved through changing', 'the signs change while their relation, agreeing or opposing, is conserved', r6),
 (7, 'Equilibria without required relational changing', 'one sign is retained while the other changes', r7),
 (8, 'Equilibria as unchanged membership during changing', 'the positive membership is never emptied', r8),
]
def run(rule, j):
    for n in range(1, 10):
        if not rule(j, n): return n
    return None                               # lives through all nine arrivals
clusters = []
for k, name, form, rule in CLUSTERS:
    clusters.append({'k': k, 'name': name, 'form': form,
                     'odd': run(rule, JOURNEYS['odd']), 'even': run(rule, JOURNEYS['even'])})
for c in clusters: assert c['odd'] is not None or c['even'] is not None, c   # every cluster blocks a journey

# ---------- every fixed condition at what one arrival carries: 2^8 = 256 ----------
STATES = [(d, s) for d in ('co', 'bi') for s in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
def run_set(R, j):
    for n in range(1, 10):
        if j[n] not in R: return n
    return None
table = []
for mask in range(256):
    R = {STATES[i] for i in range(8) if mask >> i & 1}
    table.append((mask, run_set(R, JOURNEYS['odd']), run_set(R, JOURNEYS['even'])))
both = [m for m, a, b in table if a is None and b is None]
odd_only = [m for m, a, b in table if a is None and b is not None]
even_only = [m for m, a, b in table if a is not None and b is None]
neither = [m for m, a, b in table if a is not None and b is not None]
assert both == [255] and len(odd_only) == 15 and len(even_only) == 15 and len(neither) == 225
assert max(max(a or 0, b or 0) for _, a, b in table) <= 4        # every blocked journey is blocked by arrival 4

# a condition over a run of w arrivals: the resolving is one-valued, so a run is fixed by its first carrying,
# and every such condition is one of the 256 above; the ten arrivals meet all four runs of each journey up to w = 7
def runs(j, w): return {tuple(j[i:i + w]) for i in range(0, 10 - w + 1)}
reach = {w: (len(runs(JOURNEYS['odd'], w)), len(runs(JOURNEYS['even'], w))) for w in range(1, 10)}
for w in range(1, 8): assert reach[w] == (4, 4)
assert reach[8] == (3, 3)
# check the reduction at every run length up to seven, all 256 conditions at each
for w in range(1, 8):
    firsts = {o: {r[0]: r for r in runs(JOURNEYS[o], w)} for o in JOURNEYS}
    for mask, a, b in table:
        R = {STATES[i] for i in range(8) if mask >> i & 1}
        for o, expect in (('odd', a), ('even', b)):
            j = JOURNEYS[o]; got = None
            for end in range(max(1, w - 1), 10):
                if tuple(j[end - w + 1:end + 1])[0] not in R: got = end; break
            assert (got is None) == (expect is None)

# ---------- write the data ----------
data = {'spots': {n: SPOTS[n] for n in range(10)},
        'journeys': {o: [[d, sg(s), rel(s)] for d, s in JOURNEYS[o]] for o in JOURNEYS},
        'clusters': clusters,
        'states': [[d, sg(s)] for d, s in STATES],
        'all': [[m, a, b] for m, a, b in table],
        'counts': {'both': len(both), 'odd_only': len(odd_only), 'even_only': len(even_only), 'neither': len(neither)},
        'runs_met': {w: reach[w] for w in reach}}
json.dump(data, open(os.path.join(DATA, 'journey.json'), 'w'), indent=1)

L = ['# The podaling journey and the equilibria clusters', '',
     'Returned by `scripts/journey.py`. The resolving step is Equilibria Definitions v363 §3.1, F(P, Q) = (−Q, P), from the existing prior (+, −). Arrivals 0 to 9 are prior 0–3, now 4–7 and next 8–9.', '',
     '## The two journeys', '', '| arrival | spot | sign pair | relation | odd origin | even origin |', '|---:|---|---|---|---|---|']
names = {(0, -1): 'bottom', (.5, -.5): 'lower right', (1, 0): 'right', (.5, .5): 'upper right', (0, 1): 'top',
         (-.5, .5): 'upper left', (-1, 0): 'left', (-.5, -.5): 'lower left', (0.0, 0.0): 'centre'}
for n in range(10):
    L.append(f'| {n} | {names[SPOTS[n]]} | {sg(SIGNS[n])} | {rel(SIGNS[n])} | {JOURNEYS["odd"][n][0]} | {JOURNEYS["even"][n][0]} |')
L += ['', '## Each cluster as a fixed rule', '', '| cluster | the rule at the arrival | odd origin | even origin |', '|---|---|---|---|']
fmt = lambda x: 'lives to 9' if x is None else f'blocked at {x}'
for c in clusters: L.append(f"| {c['k']}. {c['name']} | {c['form']} | {fmt(c['odd'])} | {fmt(c['even'])} |")
L += ['', '## Every fixed condition at what one arrival carries', '',
      f'Eight carryings (along or across, four sign pairs), so 256 conditions. Lives through both journeys: {len(both)}, the condition admitting all eight, which adds nothing. Lives through the odd journey only: {len(odd_only)}. The even only: {len(even_only)}. Neither: {len(neither)}. Every blocked journey is blocked by arrival 4.', '',
      '| run length | distinct runs met, odd | even |', '|---:|---:|---:|']
for w in range(1, 10): L.append(f'| {w} | {reach[w][0]} | {reach[w][1]} |')
open(os.path.join(DATA, 'journey_blockage.md'), 'w').write('\n'.join(L) + '\n')

# ---------- the still ----------
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
ALONG, ACROSS = '#1f6f8b', '#c8553d'
fig, axs = plt.subplots(1, 2, figsize=(10, 5.4))
for ax, o in zip(axs, ('odd', 'even')):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.45, 1.55)
    for n in range(9):
        a, b = SPOTS[n], SPOTS[n + 1]; d = JOURNEYS[o][n + 1][0]
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=14, lw=1.6,
                                     color=ALONG if d == 'co' else ACROSS, shrinkA=13, shrinkB=13,
                                     connectionstyle='arc3,rad=0.12'))
    for n in range(1, 9):
        x, y = SPOTS[n]; ax.scatter([x], [y], s=520, c='white', edgecolors='#333', zorder=3)
        ax.text(x, y, str(n), ha='center', va='center', fontsize=12, zorder=4)
    ax.scatter([0], [0], s=620, c='#eee', edgecolors='#333', zorder=3); ax.text(0, 0, '0·9', ha='center', va='center', fontsize=10, zorder=4)
    ax.set_title(('odd origin · co–bi–co' if o == 'odd' else 'even origin · bi–co–bi'), fontsize=12)
fig.text(.42, .03, 'along (co)', ha='center', color=ALONG, fontsize=11); fig.text(.58, .03, 'across (bi)', ha='center', color=ACROSS, fontsize=11)
fig.savefig(os.path.join(IMG, 'podaling_journey_still.png'), dpi=110, bbox_inches='tight'); plt.close(fig)

# ---------- the moving form ----------
tpl = open(os.path.join(HERE, 'journey_template.html')).read()
open(os.path.join(ASSETS, 'podaling_journey.html'), 'w').write(tpl.replace('/*DATA*/null', json.dumps(data)))
print('clusters:'); [print(' ', c['k'], c['odd'], c['even']) for c in clusters]
print('256:', data['counts'])
