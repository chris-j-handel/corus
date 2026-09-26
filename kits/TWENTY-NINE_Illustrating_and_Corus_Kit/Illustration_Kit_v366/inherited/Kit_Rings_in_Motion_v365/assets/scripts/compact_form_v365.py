"""compact_form_v365.py · the co-sequential living condition in two signs, every line checked (notes III01, III02, EEE06)

Standard library only. Run:  python3 compact_form_v365.py

The compact form, as carried at Living Improving Value v365:
  STATE      two signs (P, Q), read as the signs of (cos t, sin t)
  STILL      cos^2 t + sin^2 t = 1: it admits every state, the one of the 256 fixed conditions that adds nothing
  CHANGE     the quarter turn F(P, Q) = (-Q, P), or its mirror (Q, -P): the only steps of all 256 that take no prior
             away, change one sign, and never undo
  RELATION   agree or oppose is the sign of tan t, and it tips to the opposite at every step
  HALF/WHOLE tan 2t = 2 tan t / (1 - tan^2 t); sin 2t = 2 sin t cos t carries the relation as its own sign
  STITCHES   the ten arrivals 0 to 9 pair as (k, 9 - k): five pairs, each one along with one across, one agree with
             one oppose, mirror images with the cosine kept and the sine turned; every condition holding one side
             alone is blocked within the journey
"""
import itertools, math

S = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
STATES = [(d, s) for d in ('co', 'bi') for s in S]
F = lambda s: (-s[1], s[0])
rel = lambda s: 'agree' if s[0] == s[1] else 'oppose'
direction = lambda o, n: ('co' if n % 2 else 'bi') if o == 'odd' else ('bi' if n % 2 else 'co')
angle = {(1, 1): 45, (-1, 1): 135, (-1, -1): 225, (1, -1): 315}


def journey():
    signs = [(1, -1)]
    for _ in range(9):
        signs.append(F(signs[-1]))
    return signs


def check(name, ok):
    print(f'   {"holds" if ok else "FAILS"} · {name}')
    return ok


if __name__ == '__main__':
    signs = journey(); J = {o: [(direction(o, n), signs[n]) for n in range(10)] for o in ('odd', 'even')}
    met = set(J['odd'][1:]) | set(J['even'][1:])
    results = []
    print('STATE')
    results.append(check('each sign pair is the signs of (cos t, sin t) at its angle',
                         all((1 if math.cos(math.radians(angle[s])) > 0 else -1, 1 if math.sin(math.radians(angle[s])) > 0 else -1) == s for s in S)))
    print('STILL')
    still = [st for st in STATES if abs(math.cos(math.radians(angle[st[1]])) ** 2 + math.sin(math.radians(angle[st[1]])) ** 2 - 1) < 1e-12]
    results.append(check('cos² + sin² = 1 admits all eight states', len(still) == 8))
    living = [m for m in range(256) if all(STATES.index(st) in [i for i in range(8) if m >> i & 1] for st in met)]
    results.append(check('of the 256 fixed conditions, only the one admitting all eight lives through both origins', living == [255]))
    print('CHANGE')
    one = lambda a, b: sum(x != y for x, y in zip(a, b)) == 1
    kept = []
    for image in itertools.product(S, repeat=4):
        f = dict(zip(S, image))
        if len(set(image)) == 4 and all(one(s, f[s]) for s in S) and all(f[f[s]] != s for s in S):
            kept.append(f)
    names = sorted('(-Q, P)' if all(f[s] == (-s[1], s[0]) for s in S) else '(Q, -P)' for f in kept)
    results.append(check(f'no prior taken, one sign changed, never undone: {len(kept)} steps of 256, {names}', names == ['(-Q, P)', '(Q, -P)']))
    results.append(check('F is the quarter turn of the angle', all(angle[F(s)] == (angle[s] + 90) % 360 for s in S)))
    print('RELATION')
    results.append(check('agree is the sign of tan being +', all((rel(s) == 'agree') == (math.tan(math.radians(angle[s])) > 0) for s in S)))
    results.append(check('the relation tips at every step', all(rel(signs[n]) != rel(signs[n + 1]) for n in range(9))))
    print('HALF AND WHOLE')
    results.append(check('tan 2t = 2 tan t / (1 − tan² t) away from its poles',
                         all(abs(math.tan(2 * x) - 2 * math.tan(x) / (1 - math.tan(x) ** 2)) < 1e-9 for x in (0.1, 0.5, 1.0, 2.0, 2.9))))
    results.append(check('sin 2t carries the relation as its own sign',
                         all((math.sin(2 * math.radians(angle[s])) > 0) == (rel(s) == 'agree') for s in S)))
    print('STITCHES')
    for k in range(5):
        a, b = signs[k], signs[9 - k]
        ok = a[0] == b[0] and a[1] == -b[1] and rel(a) != rel(b) and direction('odd', k) != direction('odd', 9 - k) \
            and (angle[a] + angle[b]) % 360 == 0
        results.append(check(f'pair ({k}, {9 - k}): {direction("odd", k)} with {direction("odd", 9 - k)}, {rel(a)} with {rel(b)}, '
                             f'cosine kept and sine turned', ok))
    for name, cond in [('relation held at agree', lambda d, s: rel(s) == 'agree'), ('relation held at oppose', lambda d, s: rel(s) == 'oppose'),
                       ('direction held along', lambda d, s: d == 'co'), ('direction held across', lambda d, s: d == 'bi')]:
        blocked = [next((n for n in range(1, 10) if not cond(*J[o][n])), None) for o in ('odd', 'even')]
        results.append(check(f'one side held alone, {name}: blocked at arrivals {blocked} (odd, even)', all(b is not None for b in blocked)))
    print(f'\n{sum(results)} of {len(results)} lines hold')
