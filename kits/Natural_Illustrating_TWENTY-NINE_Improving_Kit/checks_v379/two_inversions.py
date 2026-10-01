"""Natural Illustrating 2.6: the right spiral step (x, y) -> (y, -x) as two inversions whose fixed lines are
forty-five degrees apart, Natural Mathematics 3.4: the exchange of P and Q (fixed line the diagonal) and the
inversion of one parity (fixed line an axis). One order gives (y, -x), the other (-y, x), and the first goes
round the four joint forms ++, +-, --, -+, one parity changing at each step. Run from the repository root:
    python3 kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/checks_v379/two_inversions.py
"""
exchange = lambda p: (p[1], p[0])          # fixed line the diagonal x = y, at forty-five degrees
invert_y = lambda p: (p[0], -p[1])         # fixed line the x axis
a = lambda p: invert_y(exchange(p))        # exchange then inversion
b = lambda p: exchange(invert_y(p))        # inversion then exchange
s = lambda p: ('+' if p[0] > 0 else '-') + ('+' if p[1] > 0 else '-')
print("exchange then inversion, (x, y) -> (y, -x): (1, 2) ->", a((1, 2)))
print("inversion then exchange, (x, y) -> (-y, x): (1, 2) ->", b((1, 2)))
p = (1, 1); path = []
for _ in range(5):
    path.append(s(p)); p = a(p)
print("exchange then inversion from ++:", ' '.join(path))
p = (1, 1); path = []
for _ in range(5):
    path.append(s(p)); p = b(p)
print("inversion then exchange from ++:", ' '.join(path))
