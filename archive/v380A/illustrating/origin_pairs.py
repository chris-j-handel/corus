"""Examine v380A's proposed binary sequence and named cycles.

This instrument enumerates mathematical descriptions. It imports no
resolver, examines no self's private carrying, and creates no illustration.
Run from the repository root: python3 incoming/v380A/illustrating/origin_pairs.py
"""
from itertools import product

sign = {1: '+', -1: '-'}
inputs = list(product((1, -1), repeat=2))
descriptions = list(product((1, -1), repeat=4))
sequence = [1, 1, -1, -1, 1, 1]
remaining = descriptions
print('Origin:', ' '.join(f'{i}{sign[p]}' for i, p in enumerate(sequence, 1)))
print('Pairs:', ' -> '.join(sign[a] + sign[b] for a, b in zip(sequence, sequence[1:])))
for n in range(2, len(sequence)):
    pair = tuple(sequence[n-2:n])
    remaining = [d for d in remaining if d[inputs.index(pair)] == sequence[n]]
    print(f'At {n+1}: {len(remaining)} of sixteen descriptions remain')
print('Remaining description, next = -prior:',
      remaining == [tuple(-a for a, b in inputs)])
carrying = [d for d in descriptions if
            all(d[inputs.index((1, b))] != d[inputs.index((-1, b))] for b in (1, -1))]
no_still = [d for d in carrying if
            all((b, d[inputs.index((a, b))]) != (a, b) for a, b in inputs)]
print('Descriptions retaining prior at both values of now:', len(carrying))
print('Of those, descriptions with no fixed joint form:', len(no_still))
proper = [set(p for p, chosen in zip(inputs, selection) if chosen)
          for selection in product((False, True), repeat=4)
          if any(selection) and not all(selection)]
exits = []
for selection in proper:
    for pair in selection:
        p = pair
        for advance in range(1, 5):
            p = (p[1], -p[0])
            if p not in selection:
                exits.append(advance)
                break
print('Nonempty proper selections of the four forms:', len(proper))
print('Greatest first-exit distance from a selected form:', max(exits))
print('Overlay next = now first differs at:',
      next(n+1 for n in range(2, len(sequence)) if sequence[n] != sequence[n-1]))
print('Overlay next = -now first differs at:',
      next(n+1 for n in range(2, len(sequence)) if sequence[n] != -sequence[n-1]))
for root, cycle in [
    ('torusing', (1, 9, 8, 16)),
    ('corusing', (2, 15, 7, 10)),
    ('moralizing', (3, 11, 6, 14)),
    ('competencing', (4, 13, 5, 12)),
]:
    edges = list(zip(cycle, cycle[1:] + cycle[:1]))
    changes = [(a, b) for a, b in edges if a % 2 != b % 2]
    print(root, '-'.join(map(str, cycle)),
          'numerical parity changes:', len(changes),
          'each at 17 less:', all(b == 17-a for a, b in changes))
