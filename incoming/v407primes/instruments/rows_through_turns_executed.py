"""Rows through turns: each known asking about primes, stepped with whole numbers.

A turn (2, 6, 30, 210, 2,310, 30,030, 510,510) says how many places in it
are open for a row. A surface (4, 16, 64, ... 4^k) says how many of the
row's members have come by its side and by its horizon.
Usage: python3 -I rows_through_turns_executed.py
"""

TURN_PRIMES = [2, 3, 5, 7, 11, 13, 17]
TO = 4 ** 10  # 1,048,576

sieve = bytearray([1]) * (TO * 4 + 3)
sieve[0] = sieve[1] = 0
for p in range(2, int(len(sieve) ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
is_p = lambda n: n < len(sieve) and sieve[n] == 1


def turn_openings(fits):
    """Places r in each turn whose row stays clear of every turn prime."""
    out, turn = [], 1
    for p in TURN_PRIMES:
        turn *= p
        out.append((turn, sum(1 for r in range(turn) if fits(r, turn))))
    return out


def clear(n, turn):
    return all(n % p for p in TURN_PRIMES if turn % p == 0)


rows = {
    "primes": lambda r, t: clear(r, t),
    "twins (n, n+2)": lambda r, t: clear(r, t) and clear(r + 2, t),
    "Sophie Germain (n, 2n+1)": lambda r, t: clear(r, t) and clear(2 * r + 1, t),
    "one past a square (n*n+1)": lambda r, t: clear(r * r + 1, t),
}

print("Openings each turn (a row is closed only if a turn's openings are 0):")
for name, fits in rows.items():
    print(" ", name.ljust(28), [o for _, o in turn_openings(fits)])
# n*n+1 is never even only for even n; it is clear of 2 at odd n? n*n+1 odd iff n even.

print("\nMembers by each surface's side (side = 2^k, surface = 4^k):")
print("  side   primes   twins   SophieG   n*n+1<=surface  Legendre gaps  Goldbach misses")
for k in range(1, 11):
    side, surf = 2 ** k, 4 ** k
    pr = sum(1 for n in range(2, side + 1) if is_p(n))
    tw = sum(1 for n in range(2, side + 1) if is_p(n) and is_p(n + 2))
    sg = sum(1 for n in range(2, side + 1) if is_p(n) and is_p(2 * n + 1))
    sq = sum(1 for n in range(1, side + 1) if is_p(n * n + 1))
    # Legendre: a prime between n*n and (n+1)*(n+1), every n up to the side
    leg = sum(1 for n in range(1, side + 1)
              if not any(is_p(m) for m in range(n * n + 1, (n + 1) * (n + 1))))
    # Goldbach: every even 4..surface is two primes (surface up to 4^8 here)
    gb = "-"
    if k <= 8:
        primes_to = [q for q in range(2, surf + 1) if is_p(q)]
        gb = 0
        for e in range(4, surf + 1, 2):
            if not any(is_p(e - q) for q in primes_to if q <= e // 2):
                gb += 1
    print(f"  {side:5} {pr:7} {tw:7} {sg:8} {sq:12} {leg:14} {str(gb):>12}")

print("\nRows that leap surfaces (each member steps past many horizons):")
fermat = [(k, 2 ** (2 ** k) + 1) for k in range(5)]
print("  Fermat 2^(2^k)+1, k=0..4:", [f for _, f in fermat],
      "all prime:", all(is_p(f) for _, f in fermat))
f5 = 2 ** 32 + 1
print("  k=5:", f5, "= 641 x", f5 // 641, f5 % 641 == 0)
mers = [q for q in range(2, 32) if is_p(q) and all((2 ** q - 1) % d for d in range(2, int((2 ** q - 1) ** 0.5) + 1))]
print("  Mersenne 2^q-1 prime for q =", mers)
print("  perfect numbers from them:", [2 ** (q - 1) * (2 ** q - 1) for q in mers[:5]])
wief = [p for p in range(3, 10000) if is_p(p) and pow(2, p - 1, p * p) == 1]
print("  Wieferich (doubling closes round p*p) below 10,000:", wief)

print("\nThe rate a turn gives, twins to primes (whole numbers, turn by turn):")
for (t, o), (_, tw) in zip(turn_openings(rows["primes"]), turn_openings(rows["twins (n, n+2)"])):
    print(f"  turn {t:7}: {tw} twin places of {o} prime places")
