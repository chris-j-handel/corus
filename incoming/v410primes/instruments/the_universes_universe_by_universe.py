# The surface of the prime universes, universe by universe: a named universe, 1 to N.
# A me-parity opens a universe at its me again; the universe is to the number ahead of the next me-parity's me again.
import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**8
s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
i = 2
while i * i <= N:
    if s[i]: s[i*i::i] = bytearray(len(range(i*i, N + 1, i)))
    i += 1
side = int(N ** 0.5)
openers = [p for p in range(2, side + 2) if s[p]]
rows = []
for k in range(len(openers) - 1):
    p, q = openers[k], openers[k + 1]
    a, b = p * p, q * q - 1
    if b > N: break
    seg = s[a:b + 1]
    births = seg.count(1)
    two = sum(1 for n in range(a, b - 1) if s[n] and s[n + 2])
    rows.append((p, a, b, births, two))
print("the named universe: 1 to", N, "; universes whole in it:", len(rows), "; the last opener:", rows[-1][0])
print("opener | the universe | births | births 2 apart")
for r in rows[:12]: print(" ", r[0], "|", r[1], "to", r[2], "|", r[3], "|", r[4])
print("universes with no birth:", sum(1 for r in rows if r[3] == 0))
print("universes with fewer than 4 births:", [r[0] for r in rows if r[3] < 4])
print("universes with no births 2 apart:", [r[0] for r in rows if r[4] == 0])
print("least births past the universe of 3:", min(r[3] for r in rows[2:]), "at the opener", min(rows[2:], key=lambda r: r[3])[0])
print("least births 2 apart past the universe of 3:", min(r[4] for r in rows[2:]), "at the opener", min(rows[2:], key=lambda r: r[4])[0])
# a next opener is born ahead of the opening of the universe: q smaller than p by p
print("a next opener not smaller than the opener's me again:", sum(1 for k in range(len(openers)-1) if openers[k+1] >= openers[k]**2))
# the universe a me-parity is born in: a born me-parity opens a universe of its own
last = rows[-1]
print("births in the last universe whole:", last[3], "; the universe:", last[1], "to", last[2])
