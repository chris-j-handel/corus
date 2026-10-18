"""Exact angles at one declared plane, without a resolver or a visual.

Run from the repository root: python3 incoming/v380A/illustrating/angle_correspondence.py
For the 240-degree rotations, (a, b) denotes a + b * sqrt(3) * i.
This examines only the stated same-plane case, not the user's unspecified
three-dimensional axes or the still-open triangle-to-method correspondence.
"""
from fractions import Fraction as F

def multiply(a, b):
    return a[0]*b[0]-3*a[1]*b[1], a[0]*b[1]+a[1]*b[0]

one = (F(1), F(0))
rotation = (-F(1, 2), -F(1, 2))
opposite = (rotation[0], -rotation[1])
current = one
for n in range(1, 4):
    current = multiply(current, rotation)
    print('240 degrees, repetitions', n, ': (a, b) =',
          tuple(str(t) for t in current), '; original again:', current == one)
print('Opposing 240 degrees in one plane compose to original:',
      multiply(rotation, opposite) == one)

def matrix_times(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

identity = ((1, 0), (0, 1))
right = ((0, 1), (-1, 0))
current = identity
for n in range(1, 5):
    current = matrix_times(current, right)
    print('Right spiral, repetitions', n, ':', current,
          '; original again:', current == identity)
