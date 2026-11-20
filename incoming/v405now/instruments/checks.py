#!/usr/bin/env python3
"""Checks of four astounding statements whose ground is a count or an identity.

Usage: python3 -I checks.py
Each check prints what it counts; a check is not a proof, and a count over
small sets says nothing past them.
"""
import itertools, math

# Natural Emanating, three lines: transitive relations on four elements.
n = 4
pairs = [(a, b) for a in range(n) for b in range(n)]
count = 0
for bits in range(1 << len(pairs)):
    R = {pairs[i] for i in range(len(pairs)) if bits >> i & 1}
    if all((a, d) in R for (a, b) in R for (c, d) in R if b == c):
        count += 1
print('transitive relations on four elements:', count)

# A transitive relation: whatever a pair reaches, one of the pair reaches alone.
# Reach of a set is the union of its members' reaches, so in neither alone is none.
print('a pair reaches only what one of it reaches: by the union, for any relation')

# Natural Emanating, nature: the gap of exactly one.
print('gap of one, n = 2..10 000:', all((k - 1) * (k + 1) == k * k - 1 for k in range(2, 10001)))

# THIRTY 175: four-sided faces, four edges at each point.
F = 1
E = 2 * F * 2 // 2  # each face four edges, each edge two faces: E = 2F
V = E // 2          # each point four edges, each edge two points: E = 2V
print('points less edges with faces, four-sided and four at each point:', V - E + F, '(0 for any F)')

# THIRTY 184: Fibonacci ratios about phi, above and below by turns.
phi = (1 + 5 ** 0.5) / 2
f = [1, 1]
while len(f) < 20:
    f.append(f[-1] + f[-2])
signs = [f[i + 1] / f[i] > phi for i in range(1, 19)]
print('ratios alternate about phi:', all(signs[i] != signs[i + 1] for i in range(len(signs) - 1)), round(phi * phi - phi - 1, 12))

# Natural Emanating: sharing and opening of two directions at an angle.
for deg in (0, 60, 90):
    t = math.radians(deg)
    print(f'angle {deg}: sharing {math.cos(t):.3f} opening {math.sin(t):.3f}')
